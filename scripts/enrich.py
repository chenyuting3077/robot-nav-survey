#!/usr/bin/env python3
"""補齊論文資料：給一串 arXiv 編號，合併多個來源寫到 JSON（可中斷續跑）。

  python3 scripts/enrich.py 輸出.json 2503.11651 2310.07896 ...

來源分工（2026-10 實測）：
- arXiv API `id_list`：一次查 100 篇，拿摘要、備註（常寫專案頁與會議）、journal_ref、DOI。
  作者單位幾乎都是空的，所以機構不靠它。比逐頁抓摘要頁快兩個數量級，也較少被限流。
- Hugging Face Papers API：現成的 githubRepo、projectPage、upvotes、ai_summary。
  抽樣收錄率約七成，2023 年前的論文多半沒有。
- OpenAlex：一次查 50 篇，拿正規化的機構名稱；抽樣約一半論文有機構。
- 上面都查不到機構時，才抓 arXiv HTML 版的作者區塊（每篇一次請求，最慢）。
"""
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

from net import fetch as get

NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}


def arxiv_batch(ids):
    out = {}
    for k in range(0, len(ids), 100):
        chunk = ids[k:k + 100]
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
            {"id_list": ",".join(chunk), "max_results": len(chunk)})
        root = ET.fromstring(get(url))
        for e in root.findall("a:entry", NS):
            aid = re.sub(r"v\d+$", "", e.find("a:id", NS).text.rsplit("/abs/", 1)[-1])
            def t(tag):
                n = e.find(tag, NS)
                return re.sub(r"\s+", " ", n.text).strip() if n is not None and n.text else ""
            out[aid] = {"title": t("a:title"), "abstract": t("a:summary"), "comments": t("x:comment"),
                        "journal_ref": t("x:journal_ref"), "doi": t("x:doi"),
                        "published": t("a:published")[:10]}
        time.sleep(3)  # arXiv API 規範：請求間隔 3 秒
    return out


def hf(aid):
    try:
        p = json.loads(get(f"https://huggingface.co/api/papers/{aid}", tries=4))
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):  # 單篇失敗不中斷整批
        return {}
    return {k: p.get(k) for k in ("githubRepo", "projectPage", "upvotes", "githubStars", "ai_summary")}


def openalex_batch(ids):
    out = {}
    for k in range(0, len(ids), 50):
        chunk = ids[k:k + 50]
        f = "|".join(f"10.48550/arxiv.{i}" for i in chunk)
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode({"filter": f"doi:{f}", "per-page": 50})
        for w in json.loads(get(url))["results"]:
            aid = (w.get("doi") or "").lower().rsplit("arxiv.", 1)[-1]
            insts = []
            for a in w["authorships"]:
                for i in a["institutions"]:
                    if i["display_name"] not in insts:
                        insts.append(i["display_name"])
            out[aid] = {"institutions": insts}
        time.sleep(1)
    return out


def html_authors(aid):
    try:
        s = html.unescape(get(f"https://arxiv.org/html/{aid}", tries=4).decode("utf-8", "ignore"))
    except Exception:
        return ""
    i = s.find('class="ltx_authors')
    blk = s[i:i + 8000]
    j = blk.find("ltx_abstract")
    blk = blk[:j] if j > 0 else blk
    txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", blk))
    return re.sub(r"\S+@\S+", "", txt).strip()[:900]


def main():
    out_path, ids = Path(sys.argv[1]), sys.argv[2:]
    out = json.loads(out_path.read_text()) if out_path.exists() else {}
    todo = [i for i in ids if i not in out]
    if todo:
        print(f"arXiv API：{len(todo)} 篇", flush=True)
        ax = arxiv_batch(todo)
        print("OpenAlex 機構", flush=True)
        oa = openalex_batch(todo)
        print("HF 與 arXiv HTML，逐篇", flush=True)
        for n, aid in enumerate(todo, 1):
            rec = {**ax.get(aid, {}), **oa.get(aid, {"institutions": []}), "hf": hf(aid)}
            if not rec["institutions"]:
                rec["html_authors"] = html_authors(aid)
                time.sleep(3)
            out[aid] = rec
            if n % 20 == 0:
                out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1))
                print(f"{n}/{len(todo)}", flush=True)
            time.sleep(0.3)
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print(f"完成 {len(out)} 篇")


if __name__ == "__main__":
    main()
