#!/usr/bin/env python3
"""用 Semantic Scholar 依主題關鍵字撈高引用候選論文，寫到 data/candidates.json。

只做「引用門檻」這一條的初篩；相關性與其他收錄條件（獲獎、基準、機構、推薦）
要人工判斷後寫進 data/classics.csv。門檻依年份調整，因為新論文引用還沒累積。
"""
import json
import os
import time
import urllib.parse
from pathlib import Path

from net import fetch_json

ROOT = Path(__file__).resolve().parent.parent
URL = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"
FIELDS = "title,year,citationCount,venue,externalIds"

# 年份 -> 最低引用數；2026 年起的論文不看引用（太新），靠其他條件收錄
THRESHOLD = {2021: 300, 2022: 300, 2023: 150, 2024: 80, 2025: 30}

QUERIES = {
    "vln": ['"vision-and-language navigation"', '"vision-language navigation"', '"object goal navigation"',
            '"object navigation"', '"embodied navigation"', '"language-guided navigation"',
            '"zero-shot navigation"', '"instruction following" navigation robot'],
    "local-nav": ['"visual navigation"', '"navigation foundation model"', '"end-to-end navigation"',
                  '"local planner"', '"navigation policy"', '"autonomous exploration"', '"social navigation"',
                  '"robot navigation" learning'],
    "semantic-map": ['"3D scene graph"', '"open-vocabulary 3D"', '"semantic mapping"', '"open-vocabulary map"',
                     '"language embedded"', '"open-set" mapping'],
    "quadruped": ['quadruped', '"legged robot"', '"legged locomotion"', '"quadrupedal"'],
    "wheel-legged": ['"wheel-legged"', '"wheeled-legged"', '"legged-wheeled"', '"wheeled bipedal"'],
    "slam": ['SLAM', '"visual odometry"', '"lidar odometry"', '"lidar-inertial"', '"visual-inertial"',
             '"place recognition"', '"loop closure"', '"bundle adjustment"'],
    "perception-3d": ['"depth estimation"', '"stereo matching"', '"multi-view stereo"', '"3D reconstruction"',
                      '"gaussian splatting"', '"occupancy prediction"', 'pointmap', '"novel view synthesis"'],
    "spatial": ['"3D object detection" indoor', '"open-vocabulary 3D detection"', '"3D instance segmentation"',
                '"3D visual grounding"', '"3D question answering"', '"3D large language model"',
                '"spatial reasoning" vision-language', '"spatial understanding" multimodal', '"3D scene understanding"'],
    "vision": ['"open-vocabulary detection"', '"open-vocabulary segmentation"', '"open-vocabulary object detection"',
               '"segment anything"', '"vision foundation model"', '"self-supervised" visual representation',
               '"feature matching"', '"point tracking"', '"real-time object detection"'],
    "real2sim": ['"real-to-sim"', 'real2sim', '"digital twin" robot', '"sim-to-real"', '"robot simulation"',
                 '"gaussian splatting" simulation robot', '"world model" robot'],
}


# 錨點論文：撈引用它們的高引用論文，補關鍵字的盲點（2026-10 關鍵字漏掉 VSI-Bench、Omni3D、ScanRefer）。
# 選領域專屬、引用數數千以內的；vision、real2sim 的代表作（CLIP、SAM、Isaac Gym）被引用太廣，撈回來多是雜訊，所以不設。
ANCHORS = {
    "vln": ["1711.07280", "2004.02857"],  # R2R、VLN-CE
    "local-nav": ["2306.14846", "2310.07896"],  # ViNT、NoMaD
    "semantic-map": ["2309.16650", "2210.05714"],  # ConceptGraphs、VLMaps
    "quadruped": ["2109.11978", "2201.08117"],  # Learning to Walk in Minutes、Perceptive Locomotion
    "wheel-legged": ["2405.01792"],  # ETH 輪足自主導航與運動
    "slam": ["2107.06829", "2108.10869"],  # FAST-LIO2、DROID-SLAM
    "perception-3d": ["2312.14132"],  # DUSt3R
    "spatial": ["1912.08830", "2412.14171"],  # ScanRefer、VSI-Bench
}


def citing(aid: str):
    headers = {"x-api-key": key} if (key := os.environ.get("S2_API_KEY")) else {}
    offset = 0
    while offset is not None:
        limit = min(1000, 9999 - offset)  # 2026-10 實測：offset + limit 須 < 10000，否則回錯誤
        if limit <= 0:
            print(f"  {aid} 引用超過 1 萬篇，只撈到前 9999 篇；換一篇較窄的錨點", flush=True)
            return
        url = (f"https://api.semanticscholar.org/graph/v1/paper/ARXIV:{aid}/citations?"
               f"{urllib.parse.urlencode({'fields': FIELDS, 'limit': limit, 'offset': offset})}")
        res = fetch_json(url, headers=headers)
        yield from (c["citingPaper"] for c in res.get("data", []))
        offset = res.get("next")
        time.sleep(3)


def search(query: str):
    headers = {}
    if key := os.environ.get("S2_API_KEY"):
        headers["x-api-key"] = key
    params = {"query": query, "year": "2021-", "minCitationCount": 30,
              "sort": "citationCount:desc", "fields": FIELDS, "fieldsOfStudy": "Computer Science"}
    token = None
    while True:
        if token:
            params["token"] = token
        url = f"{URL}?{urllib.parse.urlencode(params)}"
        res = fetch_json(url, headers=headers)
        yield from res.get("data", [])
        token = res.get("token")
        if not token:
            return
        time.sleep(3)


def main():
    path = ROOT / "data" / "candidates.json"
    out = json.loads(path.read_text()) if path.exists() else {}
    for topic, queries in QUERIES.items():
        if topic in out:  # 中斷後重跑時跳過已完成的主題；要全部重撈就先刪檔
            continue
        found = {}
        sources = [(f"查詢「{q}」", search, q) for q in queries]
        sources += [(f"引用 {a}", citing, a) for a in ANCHORS.get(topic, [])]
        for k, (label, fn, arg) in enumerate(sources, 1):
            print(f"{topic} {k}/{len(sources)}：{label}", flush=True)
            for p in fn(arg):
                year, cites = p.get("year"), p.get("citationCount") or 0
                if year is None or cites < THRESHOLD.get(year, 10**9):
                    continue
                aid = (p.get("externalIds") or {}).get("ArXiv")
                key = aid or p.get("paperId")
                found[key] = {"arxiv": aid, "doi": (p.get("externalIds") or {}).get("DOI"), "title": p["title"], "year": year,
                              "citations": cites, "venue": p.get("venue") or ""}
            time.sleep(3)
        out[topic] = sorted(found.values(), key=lambda x: -x["citations"])
        path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
        print(f"{topic}: {len(out[topic])} 篇", flush=True)


if __name__ == "__main__":
    main()
