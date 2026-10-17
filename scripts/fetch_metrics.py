#!/usr/bin/env python3
"""抓 data/classics.csv 每篇的引用數（Semantic Scholar）、GitHub star、HF 按讚數與 arXiv 備註，存到 data/metrics.json。

arXiv 的 Comments／journal_ref 給 check_data.py 核對刊登處的會議與年份。

Semantic Scholar 未登入時共用限流，常回 429，所以用指數退避重試；
有 S2_API_KEY 環境變數就帶上。GitHub 優先用 gh CLI（已登入，限額高），沒有就用
GITHUB_TOKEN 或匿名 API（每小時 60 次，約夠一輪）。
"""
import csv
import datetime
import json
import os
import shutil
import subprocess
import time
import urllib.error
from pathlib import Path

from enrich import arxiv_batch
from net import fetch_json

ROOT = Path(__file__).resolve().parent.parent
S2_URL = "https://api.semanticscholar.org/graph/v1/paper/batch?fields=title,year,venue,citationCount"


def s2_id(pid: str) -> str:
    # classics.csv 的 id：arXiv 編號，或 `DOI:...`
    return pid if pid.startswith("DOI:") else f"ARXIV:{pid}"


def fetch_papers(ids):
    headers = {"Content-Type": "application/json"}
    if key := os.environ.get("S2_API_KEY"):
        headers["x-api-key"] = key
    body = json.dumps({"ids": [s2_id(i) for i in ids]}).encode()
    res = fetch_json(S2_URL, data=body, headers=headers)
    return {
        i: (None if p is None else {k: p[k] for k in ("title", "year", "venue", "citationCount")})
        for i, p in zip(ids, res)
    }


def fetch_stars(repo):
    if shutil.which("gh"):
        out = subprocess.run(["gh", "api", f"repos/{repo}", "--jq", ".stargazers_count"],
                             capture_output=True, text=True)
        return int(out.stdout) if out.returncode == 0 else None
    headers = {"Accept": "application/vnd.github+json"}
    if token := os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    try:
        return fetch_json(f"https://api.github.com/repos/{repo}", headers=headers)["stargazers_count"]
    except urllib.error.HTTPError:
        return None


def fetch_hf_upvotes(aid):
    # Hugging Face Papers 的按讚數；沒收錄的論文回 None（多半是 2023 年前或冷門的）
    try:
        p = fetch_json(f"https://huggingface.co/api/papers/{aid}", tries=4)
        return p.get("upvotes")
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):  # 單篇失敗不中斷整批
        return None


def main():
    rows = list(csv.DictReader((ROOT / "data" / "classics.csv").open()))
    ids = [r["id"] for r in rows if r["id"]]  # 沒有 id 的（部落格、技術報告）不查引用
    print(f"Semantic Scholar：{len(ids)} 篇", flush=True)
    papers = fetch_papers(ids)
    repos = sorted({r["repo"] for r in rows if r["repo"]})
    print(f"GitHub star：{len(repos)} 個 repo", flush=True)
    stars = {repo: fetch_stars(repo) for repo in repos}
    hf_ids = [i for i in ids if not i.startswith("DOI:")]
    hf = {}
    for n, i in enumerate(hf_ids, 1):
        hf[i] = fetch_hf_upvotes(i)
        if n % 50 == 0:
            print(f"HF 按讚數 {n}/{len(hf_ids)}", flush=True)
        time.sleep(0.3)
    print(f"arXiv 備註：{len(hf_ids)} 篇", flush=True)
    arxiv = {i: {k: v[k] for k in ("comments", "journal_ref")} for i, v in arxiv_batch(hf_ids).items()}
    out = {"fetched": datetime.date.today().isoformat(), "papers": papers, "stars": stars, "hf": hf, "arxiv": arxiv}
    (ROOT / "data" / "metrics.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    for i in ids:
        if papers[i] is None:
            print(f"找不到：{i}")
    for repo, s in stars.items():
        if s is None:
            print(f"抓不到 star：{repo}")


if __name__ == "__main__":
    main()
