#!/usr/bin/env python3
"""檢查 topics/*.md 與 data/classics.csv 的格式，有錯就以非零結束；build_readme.py 會先跑它。

只檢查機械式規則。曾發生過的錯：改欄位時空白格被吃掉，「來源」錯位到「數據」欄；
機構留空；沒有官方程式碼卻沒標「未公開」。
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TAGS = {"獲獎", "基準", "機構", "推薦"}
COLS = 7  # | 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
ARXIV = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})")
DOI = re.compile(r"(?:doi\.org/|/doi/)(10\.\d{4,9}/[^\s)]+)")
# arXiv Comments／journal_ref 裡的「會議 年份」，用來核對 venue 的年份（S2 的年份是 arXiv 年份，不能拿來比）
ARXIV_VENUE = re.compile(r"\b(CVPR|ICCV|ECCV|NeurIPS|NIPS|ICLR|ICML|CoRL|RSS|ICRA|IROS|RA-?L|T-?RO|IJRR|TPAMI|3DV|WACV|AAAI)"
                         r"\s*'?(20\d{2}|\d{2})\b")
ALIAS = {"NIPS": "NeurIPS", "RAL": "RA-L", "TRO": "T-RO"}
# 跳過：workshop、投稿中，以及期刊延伸版（備註寫的是前作會議）
SKIP_NOTE = re.compile(r"workshop|review|submitted|submission|extend", re.I)
# 期刊只比名稱：arXiv 備註常寫接收年，刊登年份以卷號為準（例：AnyLoc 備註 RA-L 2023，卷號是 2024）
JOURNALS = {"RA-L", "T-RO", "IJRR", "TPAMI"}
# Semantic Scholar 的 venue 全名 -> classics.csv 用的縮寫；只列常見的，用來抓憑記憶填錯的刊登處
S2_VENUE = {
    "Computer Vision and Pattern Recognition": "CVPR", "International Conference on Computer Vision": "ICCV",
    "European Conference on Computer Vision": "ECCV", "Neural Information Processing Systems": "NeurIPS",
    "International Conference on Learning Representations": "ICLR", "International Conference on Machine Learning": "ICML",
    "Conference on Robot Learning": "CoRL", "Robotics: Science and Systems": "RSS",
    "International Conference on Robotics and Automation": "ICRA", "Intelligent RObots and Systems": "IROS",
    "Robotics and Automation Letters": "RA-L", "Transactions on robotics": "T-RO", "Science Robotics": "Science Robotics",
    "Int. J. Robotics Res.": "IJRR", "international journal of robotics research": "IJRR",
    "Transactions on Field Robotics": "T-FR", "Pattern Analysis and Machine Intelligence": "TPAMI",
}


def check_topics(topics, errors):
    seen = {}
    for name in topics:
        path = ROOT / "topics" / f"{name}.md"
        text = path.read_text()
        if "## 在解決的問題" not in text or "## 最新論文" not in text:
            errors.append(f"{path.name}：缺「## 在解決的問題」或「## 最新論文」")
            continue
        start = text[:text.index("## 最新論文")].count("\n")
        for n, line in enumerate(text.splitlines()[start:], start + 1):
            if not line.startswith("|") or line.startswith("| 日期") or line.startswith("| ---"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            where = f"{path.name} 第 {n} 行"
            if len(cells) != COLS:
                errors.append(f"{where}：{len(cells)} 欄，應為 {COLS} 欄")
                continue
            date, paper, org, note, data, code, venue = cells
            if not re.fullmatch(r"\d{4}-\d{2}", date):
                errors.append(f"{where}：日期「{date}」不是 YYYY-MM")
            for label, v in (("論文", paper), ("機構", org), ("重點", note), ("來源", venue)):
                if not v:
                    errors.append(f"{where}：{label}欄空白")
            if data == venue or data.lower() == "arxiv":
                errors.append(f"{where}：數據欄是「{data}」，像是來源錯位")
            if not (code == "未公開" or code.startswith("[GitHub](")):
                errors.append(f"{where}：程式碼欄應為 [GitHub](...) 或「未公開」，現在是「{code}」")
            if m := ARXIV.search(paper):
                seen[m.group(1)] = where
            elif m := DOI.search(paper):
                seen[f"DOI:{m.group(1)}"] = where
    return seen


def check_classics(topics, in_topics, errors):
    ids = {}
    if b"\r" in (ROOT / "data" / "classics.csv").read_bytes():  # csv.writer 預設寫 CRLF，混進來 diff 會整行變動
        errors.append("classics.csv：有 CRLF 換行，請用 csv.writer(..., lineterminator=\"\\n\")")
    for n, r in enumerate(csv.DictReader((ROOT / "data" / "classics.csv").open()), 2):
        where = f"classics.csv 第 {n} 行（{r['name']}）"
        if r["topic"] not in topics:
            errors.append(f"{where}：topic「{r['topic']}」不在 TOPICS")
        for col in ("name", "org", "venue", "note"):
            if not r[col].strip():
                errors.append(f"{where}：{col} 空白")
        if not r["id"] and not r["url"]:
            errors.append(f"{where}：id 與 url 都空白")
        if r["id"]:
            if not (re.fullmatch(r"\d{4}\.\d{4,5}", r["id"]) or r["id"].startswith("DOI:")):
                errors.append(f"{where}：id「{r['id']}」不是 arXiv 編號或 DOI:...")
            if r["id"] in ids:
                errors.append(f"{where}：id 與第 {ids[r['id']]} 行重複")
            ids[r["id"]] = n
            if r["id"] in in_topics:
                errors.append(f"{where}：同時出現在 {in_topics[r['id']]}")
        if r["repo"] and not re.fullmatch(r"[\w.-]+/[\w.-]+", r["repo"]):
            errors.append(f"{where}：repo「{r['repo']}」不是 owner/name")
        if bad := {t for t in r["tags"].split(";") if t} - TAGS:
            errors.append(f"{where}：tags 只能用 {'、'.join(sorted(TAGS))}，不能用 {'、'.join(sorted(bad))}")
        if "機構" in r["tags"].split(";") and not r["repo"]:
            errors.append(f"{where}：tag「機構」要求開源，但 repo 空白")


def venue_warnings() -> list[str]:
    """classics.csv 的 venue 與 Semantic Scholar、arXiv Comments 不一致時提醒；兩者都常缺或不準，所以只警告不擋。"""
    path = ROOT / "data" / "metrics.json"
    if not path.exists():
        return []
    metrics = json.loads(path.read_text())
    papers, arxiv = metrics["papers"], metrics.get("arxiv", {})
    out = []
    for r in csv.DictReader((ROOT / "data" / "classics.csv").open()):
        s2 = ((papers.get(r["id"]) or {}).get("venue") or "")
        abbr = next((a for full, a in S2_VENUE.items() if full.lower() in s2.lower()), None)
        if abbr and abbr not in r["venue"]:
            out.append(f"{r['name']}：classics.csv 寫「{r['venue']}」，Semantic Scholar 是「{s2}」")
        ax = arxiv.get(r["id"]) or {}
        note = f"{ax.get('journal_ref', '')} {ax.get('comments', '')}"
        note = re.sub(r"present\w* at \S+\s*\d*", "", note, flags=re.I)  # RA-L 論文常另在 ICRA/IROS 發表
        if SKIP_NOTE.search(note):
            continue
        for conf, year in ARXIV_VENUE.findall(note):
            conf = ALIAS.get(conf.replace("-", ""), conf)
            year = year if len(year) == 4 else f"20{year}"
            if (conf in JOURNALS and conf not in r["venue"]) or (conf not in JOURNALS and f"{conf} {year}" not in r["venue"]):
                out.append(f"{r['name']}：classics.csv 寫「{r['venue']}」，arXiv 備註是「{note.strip()[:80]}」")
                break
    return out


def check(topics) -> list[str]:
    errors = []
    in_topics = check_topics(topics, errors)
    check_classics(topics, in_topics, errors)
    return errors


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from build_readme import TOPICS

    errs = check(TOPICS)
    if warns := venue_warnings():
        print("刊登處待確認（查 arXiv journal_ref、專案頁或論文集後改 venue）：\n" + "\n".join(warns) + "\n")
    print("\n".join(errs) or "OK")
    sys.exit(1 if errs else 0)
