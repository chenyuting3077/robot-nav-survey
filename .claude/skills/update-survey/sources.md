# 新論文的搜尋來源

改動來源清單時，同步改 `scripts/build_readme.py` 裡 README 的「定期追蹤的來源」。

0. **先查重點來源**（最優先）：arXiv API 無法依機構篩選，所以先逐一查下列來源的近期發表，再做第 1 步。
   - **NVIDIA**（每次都要查）：
     - https://research.nvidia.com/research-area/robotics 、 https://research.nvidia.com/research-area/computer-vision ：依年份列出論文，只顯示年份，月份看論文網址 slug。網站常比 arXiv 晚上架，所以兩邊都要查。
     - https://research.nvidia.com/publications ：全部論文，`?page=N` 翻頁，只能依會議篩選（例如 CoRL `?f%5B0%5D=publication_events%3A35`），不能依領域篩選。
     - 實驗室：Seattle Robotics Lab https://research.nvidia.com/labs/srl 、GEAR https://research.nvidia.com/labs/gear/ 。
     - 程式碼：https://github.com/NVlabs 。
     - 再用 WebSearch `NVIDIA <主題關鍵字> <年月>` 補查 Isaac、Cosmos、GR00T 等產品線的技術報告。
     - research.nvidia.com/labs/ 首頁會擋爬蟲（403），直接用上面的子頁。
   - **企業**：Google DeepMind、Meta FAIR、Physical Intelligence、Skild AI、Mistral、Alibaba（AMAP、DAMO）、ByteDance Seed、Tencent Robotics X、Huawei、Unitree、LimX、ANYbotics、Boston Dynamics。
   - **實驗室**（括號內為主要相關主題）：
     - ETH RSL https://rsl.ethz.ch （四足、輪足）、ETH ASL https://asl.ethz.ch （SLAM、導航）
     - MIT SPARK https://web.mit.edu/sparklab/ （SLAM、場景圖）
     - CMU AirLab https://theairlab.org （SLAM、導航）
     - Berkeley RAIL https://rail.eecs.berkeley.edu （導航基礎模型）
     - UCSD Xiaolong Wang https://xiaolonw.github.io （腿式 VLA）
     - PKU EPIC https://pku-epic.github.io （VLN）
     - 上海 AI Lab InternRobotics https://github.com/InternRobotics （局部導航）
     - Oxford VGG https://www.robots.ox.ac.uk/~vgg/ （3D 重建）、Oxford DRS https://dynamic.robots.ox.ac.uk （場景圖、SLAM）
     - Freiburg https://rl.uni-freiburg.de （場景圖）、TUM CVG https://cvg.cit.tum.de （SLAM、3D）
     - HKU MaRS https://mars.hku.hk （LiDAR SLAM）、浙大 FAST Lab https://github.com/ZJU-FAST-Lab （規劃）
     - KAIST RaiLab https://railab.kaist.ac.kr （四足）
   - 查法：看上列頁面近期發表，或 WebSearch `<機構> <主題關鍵字> <年月>`。
1. **arXiv 新投稿**：
   - 主要用 RSS：`https://rss.arxiv.org/rss/cs.RO`、`https://rss.arxiv.org/rss/cs.CV`，一次請求拿到當天全部新投稿，再用下表關鍵字比對標題與摘要。RSS 只有當天，距上次更新超過一天的日子用下一項補。
   - 補查漏掉的日期用 arXiv API：`https://export.arxiv.org/api/query`（只能用 https，http 在雲端連不上），`search_query` 加 `submittedDate:[上次更新日 TO 今天]`，`sortBy=submittedDate`，`max_results=100`。請求間隔 3 秒以上，429 就退避重試；被擋住時在 PR 註明哪幾天沒查到。
   - **HF Daily Papers**：`https://huggingface.co/api/daily_papers?date=YYYY-MM-DD` 逐日查，挑與範圍相關的；按讚數是收錄條件「HF」的依據。
   - WebFetch 失敗時改用 curl。

   | 主題 | 分類 | 關鍵字（abs 或 ti，OR 串接） |
   |---|---|---|
   | vln | cs.RO, cs.CV | "vision-language navigation", "object goal navigation", "embodied navigation", "navigation foundation model" |
   | local-nav | cs.RO | "visual navigation" AND (diffusion OR "world model" OR "reinforcement learning"), "end-to-end navigation" |
   | semantic-map | cs.RO, cs.CV | "scene graph", "open-vocabulary map", "semantic mapping" |
   | quadruped | cs.RO | (quadruped OR legged) AND (perceptive OR navigation OR terrain) |
   | wheel-legged | cs.RO | "wheel-legged", "wheeled-legged", "legged-wheeled" |
   | slam | cs.RO, cs.CV | SLAM, "visual odometry", "LiDAR-inertial", "place recognition", relocalization |
   | perception-3d | cs.CV, cs.RO | "depth estimation", "feed-forward reconstruction", "3D reconstruction" AND (VGGT OR pointmap), occupancy |
   | spatial | cs.CV, cs.RO | "3D object detection" AND (indoor OR open-vocabulary), "3D visual grounding", "spatial reasoning" AND (VLM OR "vision-language"), "3D LLM" |
   | vision | cs.CV | "open-vocabulary detection", "open-vocabulary segmentation", "vision foundation model" |
   | real2sim | cs.RO, cs.CV | "real-to-sim", real2sim, "digital twin" AND robot, "Gaussian splatting" AND simulation |

2. **補充來源**（WebSearch）：Science Robotics、RA-L、T-RO 新刊；當期 CoRL / RSS / ICRA / IROS / CVPR 接收論文。
3. **篩選**：每主題每次最多收 5 篇，NVIDIA 的不佔名額。名額優先給第 0 步名單內的機構，其次依：有實機實驗 > 開源程式或權重 > 標準 benchmark 上宣稱 SOTA。純 benchmark 微幅改進、只在遙測或醫療影像上驗證的不收。機構以 arXiv 摘要頁或論文首頁的作者單位為準，「機構」欄要填。
