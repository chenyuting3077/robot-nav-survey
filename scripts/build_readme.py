#!/usr/bin/env python3
"""把 topics/*.md、data/classics.csv（+ metrics.json）與最新月報組成一頁到底的 README.md。

topics/ 與 data/ 是資料來源，README 由本腳本產生，不要手改。
"""
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from harvest import THRESHOLD  # noqa: E402
from check_data import check  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TOPICS = [
    "vln", "local-nav", "semantic-map", "quadruped", "wheel-legged",
    "slam", "perception-3d", "spatial", "vision", "real2sim",
]
STAR_BAR = 500  # 收錄條件「Star」
HF_BAR = 20  # 收錄條件「HF」：約是 2026-10 候選中按讚數的前 15%

HEADER = """# Robot Nav Survey

AMR、四足、輪足機器人的導航、視覺、3D 感知、SLAM 與 Real2Sim 前沿論文整理，每三天自動更新。

<!-- 本檔由 scripts/build_readme.py 產生，請改 topics/、data/ 或 digests/ 後重跑 -->

- 每三天由排程 agent 依 [update-survey](.claude/skills/update-survey/SKILL.md) 的流程搜尋新論文並開 PR，審過再 merge。
- 手動更新：在 repo 裡開 Claude Code，說「更新論文整理」。
- 每個主題分三段：在解決的問題、重要論文（2021 年起，開創性的不限年份）、最新論文。
- 程式碼標「未公開」：論文頁、arXiv 頁與 GitHub 搜尋都找不到作者釋出的官方程式碼（第三方重現不算）。

## 怎樣算重要論文

符合任一條就收錄，「理由」欄標出符合哪幾條：

| 理由 | 條件 |
|---|---|
| 引用 | 引用數達年份門檻：2021–22 年 ≥ 300、2023 年 ≥ 150、2024 年 ≥ 80、2025 年 ≥ 30（Semantic Scholar） |
| Star | 官方 repo star ≥ 500 |
| HF | Hugging Face Papers 按讚數 ≥ 20 |
| 獲獎 | 頂會最佳論文（含入圍）或 oral，或刊在 Science Robotics、T-RO |
| 基準 | 提出被廣泛採用的 benchmark、資料集，或常被當比較基準的方法 |
| 機構 | [定期追蹤的來源](#定期追蹤的來源)名單內機構發表，且有實機實驗與開源 |
| 推薦 | 人工推薦 |

候選由 `scripts/harvest.py` 依主題關鍵字從 Semantic Scholar 撈出，再人工確認相關性。分級：**奠基** 引用達門檻 4 倍、star ≥ 10k，或 2021 年前的開創性論文；**主流** 達引用或 Star 條件；其餘（只符合獲獎、基準、機構、推薦）為**新興**。「年」是 arXiv 首次公開年份，「來源」是正式刊登的會議或期刊。

## 定期追蹤的來源

完整查法與關鍵字見 [sources.md](.claude/skills/update-survey/sources.md)。

- **NVIDIA Research**（每次必查）：[Robotics](https://research.nvidia.com/research-area/robotics)、[Computer Vision](https://research.nvidia.com/research-area/computer-vision)、[Seattle Robotics Lab](https://research.nvidia.com/labs/srl)、[GEAR](https://research.nvidia.com/labs/gear/)、[NVlabs GitHub](https://github.com/NVlabs)
- **企業**：Google DeepMind、Meta FAIR、Physical Intelligence、Skild AI、Mistral、Alibaba、ByteDance Seed、Tencent Robotics X、Huawei、Unitree、LimX、ANYbotics、Boston Dynamics
- **實驗室**：[ETH RSL](https://rsl.ethz.ch)、[ETH ASL](https://asl.ethz.ch)、[MIT SPARK](https://web.mit.edu/sparklab/)、[CMU AirLab](https://theairlab.org)、[Berkeley RAIL](https://rail.eecs.berkeley.edu)、[UCSD Xiaolong Wang](https://xiaolonw.github.io)、[PKU EPIC](https://pku-epic.github.io)、[InternRobotics](https://github.com/InternRobotics)、[Oxford VGG](https://www.robots.ox.ac.uk/~vgg/)、[Oxford DRS](https://dynamic.robots.ox.ac.uk)、[Freiburg](https://rl.uni-freiburg.de)、[TUM CVG](https://cvg.cit.tum.de)、[HKU MaRS](https://mars.hku.hk)、[ZJU FAST Lab](https://github.com/ZJU-FAST-Lab)、[KAIST RaiLab](https://railab.kaist.ac.kr)
- **arXiv**：cs.RO、cs.CV 的每日 RSS 與 API，依主題關鍵字查上次更新後的新投稿
- **Hugging Face Daily Papers**：社群每日精選，按讚數是收錄條件之一
- **期刊**：Science Robotics、RA-L、T-RO
- **會議**：CoRL、RSS、ICRA、IROS、CVPR（接收論文公布時）
"""


def anchor(title: str) -> str:
    # GitHub 標題錨點：小寫、去標點、空白轉 -
    s = re.sub(r"[^\w\- ]", "", title.lower(), flags=re.UNICODE)
    return s.replace(" ", "-")


def reasons(year: int, cites: int, stars: int, upvotes: int, venue: str, tags: str) -> list[str]:
    out = []
    if year in THRESHOLD and cites >= THRESHOLD[year]:
        out.append("引用")
    if stars >= STAR_BAR:
        out.append("Star")
    if upvotes >= HF_BAR:
        out.append("HF")
    manual = [t for t in tags.split(";") if t]
    # 刊在這兩本期刊直接算「獲獎」；頂會最佳論文、oral 要人工標
    if venue.startswith(("Science Robotics", "T-RO")) and "獲獎" not in manual:
        out.append("獲獎")
    return out + manual


def tier(year: int, cites: int, stars: int) -> str:
    bar = THRESHOLD.get(year)
    if year < 2021 or stars >= 10000 or (bar and cites >= 4 * bar):
        return "奠基"
    if stars >= STAR_BAR or (bar and cites >= bar):
        return "主流"
    return "新興"


def paper_link(r) -> str:
    if r["url"]:
        href = r["url"]
    elif r["id"].startswith("DOI:"):
        href = f"https://doi.org/{r['id'][4:]}"
    else:
        href = f"https://arxiv.org/abs/{r['id']}"
    link = f"[{r['name']}]({href})"
    return link + (f" · [專案頁]({r['project']})" if r["project"] else "")


def classics_table(rows, metrics) -> str:
    items = []
    for r in rows:
        p = metrics["papers"].get(r["id"]) or {}
        cites = p.get("citationCount") or 0
        year = p.get("year") or (int("20" + r["id"][:2]) if r["id"][:2].isdigit() else 0)
        stars = metrics["stars"].get(r["repo"]) or 0
        upvotes = metrics.get("hf", {}).get(r["id"]) or 0
        items.append((r, year, cites, stars, upvotes, tier(year, cites, stars)))
    order = {"奠基": 0, "主流": 1, "新興": 2}
    items.sort(key=lambda x: (order[x[5]], -x[2]))

    lines = ["| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |",
             "|---|---|---|---|---|---|---|---|---|"]
    for r, year, cites, stars, upvotes, t in items:
        star = f"[{stars:,}](https://github.com/{r['repo']})" if r["repo"] else "未公開"
        why = "、".join(reasons(year, cites, stars, upvotes, r["venue"], r["tags"]))
        lines.append(f"| {t} | {why} | {year or ''} | {paper_link(r)} | {r['org']} | {r['note']} "
                     f"| {r['venue']} | {cites:,} | {star} |")
    return "\n".join(lines)


def main() -> None:
    if errors := check(TOPICS):
        sys.exit("資料格式錯誤，README 未產生：\n" + "\n".join(errors))
    classics = list(csv.DictReader((ROOT / "data" / "classics.csv").open()))
    metrics = json.loads((ROOT / "data" / "metrics.json").read_text())

    sections = []
    for name in TOPICS:
        text = (ROOT / "topics" / f"{name}.md").read_text().strip()
        title, body = text.split("\n", 1)
        problems, latest = body.split("## 最新論文", 1)
        problems = problems.replace("## 在解決的問題", "").strip()
        rows = [r for r in classics if r["topic"] == name]
        parts = [f"## {title.lstrip('# ').strip()}", "### 在解決的問題", problems]
        if rows:
            parts += [f"### 重要論文（資料日期 {metrics['fetched']}）", classics_table(rows, metrics)]
        parts += ["### 最新論文", latest.strip()]
        sections.append((title.lstrip("# ").strip(), "\n\n".join(parts)))

    digests = sorted((ROOT / "digests").glob("*.md"), reverse=True)
    latest = digests[0].read_text()
    trend = latest.split("## 趨勢", 1)[1].split("\n## ", 1)[0].strip()
    updated = re.search(r"最後更新：(\S+)", latest).group(1)

    out = [HEADER, f"最後更新：{updated}\n", "## 目錄\n"]
    out.append(f"- [本月趨勢（{digests[0].stem}）](#本月趨勢{anchor(digests[0].stem)})")
    out += [f"- [{t}](#{anchor(t)})" for t, _ in sections]
    out.append("- [月報](#月報)\n")
    out.append(f"## 本月趨勢（{digests[0].stem}）\n\n{trend}\n")
    out += [f"{s}\n" for _, s in sections]
    out.append("## 月報\n")
    out += [f"- [{d.stem}](digests/{d.name})" for d in digests]

    (ROOT / "README.md").write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
