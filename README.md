# Robot Nav Survey

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

候選由 `scripts/harvest.py` 依主題關鍵字從 Semantic Scholar 撈出，再人工確認相關性；頂會得獎名單另外逐一查官網補收。只有 arXiv 預印本的，只收[定期追蹤的來源](#定期追蹤的來源)名單內機構的論文，且首次公開超過一年仍未刊登就移出；官方 repo star ≥ 500 或人工推薦的除外。分級：**奠基** 引用達門檻 4 倍、star ≥ 10k，或 2021 年前的開創性論文；**主流** 達引用或 Star 條件；其餘（只符合獲獎、基準、機構、推薦）為**新興**。「年」是 arXiv 首次公開年份，「來源」是正式刊登的會議或期刊。

## 定期追蹤的來源

完整查法與關鍵字見 [sources.md](.claude/skills/update-survey/sources.md)。

- **NVIDIA Research**（每次必查）：[Robotics](https://research.nvidia.com/research-area/robotics)、[Computer Vision](https://research.nvidia.com/research-area/computer-vision)、[Seattle Robotics Lab](https://research.nvidia.com/labs/srl)、[GEAR](https://research.nvidia.com/labs/gear/)、[NVlabs GitHub](https://github.com/NVlabs)
- **企業**：Google DeepMind、Meta FAIR、Physical Intelligence、Skild AI、Mistral、Alibaba、ByteDance Seed、Tencent Robotics X、Huawei、Unitree、LimX、ANYbotics、Boston Dynamics、Waymo、Sony AI、Adobe、Samsung、Baidu、Microsoft、Apple
- **實驗室**：[ETH RSL](https://rsl.ethz.ch)、[ETH ASL](https://asl.ethz.ch)、[MIT SPARK](https://web.mit.edu/sparklab/)、[CMU AirLab](https://theairlab.org)、[Berkeley RAIL](https://rail.eecs.berkeley.edu)、[UCSD Xiaolong Wang](https://xiaolonw.github.io)、[PKU EPIC](https://pku-epic.github.io)、[InternRobotics](https://github.com/InternRobotics)、[Oxford VGG](https://www.robots.ox.ac.uk/~vgg/)、[Oxford DRS](https://dynamic.robots.ox.ac.uk)、[Freiburg](https://rl.uni-freiburg.de)、[TUM CVG](https://cvg.cit.tum.de)、[HKU MaRS](https://mars.hku.hk)、[ZJU FAST Lab](https://github.com/ZJU-FAST-Lab)、[KAIST RaiLab](https://railab.kaist.ac.kr)
- **arXiv**：cs.RO、cs.CV 的每日 RSS 與 API，依主題關鍵字查上次更新後的新投稿
- **Hugging Face Daily Papers**：社群每日精選，按讚數是收錄條件之一
- **期刊**：Science Robotics、RA-L、T-RO
- **會議**：CoRL、RSS、ICRA、IROS、CVPR（接收論文公布時）

最後更新：2026-10-22

## 目錄

- [本月趨勢（2026-10）](#本月趨勢2026-10)
- [VLN 與導航基礎模型](#vln-與導航基礎模型)
- [局部導航與規劃（diffusion / world model / 探索）](#局部導航與規劃diffusion--world-model--探索)
- [四足](#四足)
- [輪足（雙足輪、四足輪）](#輪足雙足輪四足輪)
- [SLAM 與定位](#slam-與定位)
- [3D 場景重建（feed-forward、SfM、3DGS／NeRF）](#3d-場景重建feed-forwardsfm3dgsnerf)
- [深度估計與 occupancy](#深度估計與-occupancy)
- [語意地圖與場景圖](#語意地圖與場景圖)
- [3D 偵測與分割（點雲骨幹、3D 偵測、語意／實例分割）](#3d-偵測與分割點雲骨幹3d-偵測語意實例分割)
- [3D 空間理解（3D grounding、空間推理 VLM、3D-LLM）](#3d-空間理解3d-grounding空間推理-vlm3d-llm)
- [電腦視覺（偵測、分割、視覺基礎模型）](#電腦視覺偵測分割視覺基礎模型)
- [模擬與 Real2Sim](#模擬與-real2sim)
- [月報](#月報)

## 本月趨勢（2026-10）

- 觀察：VLN 往「慢 VLM 給影像錨點 + 快 waypoint 層」雙層架構走（ABot-N1、Robostral Navigate），且開始只用單眼 RGB。
- 觀察：局部導航從 diffusion policy 轉向 world model（LiteNWM）。
- 觀察：雙足輪研究多停在運動控制，與語言導航結合的很少。
- 觀察：SLAM 大量改用 VGGT 類 feed-forward 模型當前端（VGGT-SLAM 2.0、Scal3R），後端仍是 factor graph 或分層優化。
- 觀察：Real2Sim 從「重建出能看的場景」走向「能互動的場景」（ArtiTwinSplat 輸出 URDF 關節並匯入 Isaac Sim）。
- 推測：單眼 RGB 方案能否上 AMR 取決於機上算力；可量 Jetson 上推論延遲驗證。

## VLN 與導航基礎模型

### 在解決的問題

- 語言對應到空間：把「走到廚房冰箱旁」對到畫面與地圖上的位置。
- 長程、部分可觀測：指令長、環境沒看過，需要記憶與探索。
- sim-to-real：benchmark 多在 Habitat 模擬，實機成功率落差大。
- 推論延遲：數 B 參數的 VLM 難以機上即時跑，近期多改成「慢 VLM 推理 + 快控制層」。
- 跨機體：同一模型用在輪式、四足、人形。

### 重要論文（資料日期 2026-10-20）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | Star、基準、推薦 | 2017 | [R2R](https://arxiv.org/abs/1711.07280) | ANU / Adelaide / QUT 等 | R2R 資料集與 Matterport3D 模擬器，開創 VLN | CVPR 2018 | 2,043 | [717](https://github.com/peteanderson80/Matterport3DSimulator) |
| 奠基 | Star、基準、推薦 | 2020 | [VLN-CE](https://arxiv.org/abs/2004.02857) · [專案頁](https://jacobkrantz.github.io/vlnce) | Oregon State / Georgia Tech / Meta | VLN 從導航圖移到連續環境底層動作 | ECCV 2020 | 707 | [895](https://github.com/jacobkrantz/VLN-CE) |
| 奠基 | 引用 | 2024 | [NaVid](https://arxiv.org/abs/2402.15852) · [專案頁](https://pku-epic.github.io/NaVid/) | PKU | 只用單眼 RGB 影片的 VLM 做 VLN，不需地圖與深度 | RSS 2024 | 346 | [456](https://github.com/jzhzhang/NaVid-VLN-CE) |
| 奠基 | 引用、Star、推薦 | 2024 | [NaVILA](https://arxiv.org/abs/2412.04453) · [專案頁](https://navila-bot.github.io/) | UCSD / NVIDIA | VLM 輸出中層語言動作，低層腿式運動策略執行 | RSS 2025 | 338 | [720](https://github.com/AnjieCheng/NaVILA) |
| 奠基 | 引用、Star、HF、機構 | 2025 | [StreamVLN](https://arxiv.org/abs/2507.05240) · [專案頁](https://streamvln.github.io/) | Shanghai AI Lab / Zhejiang / SJTU 等 | SlowFast 上下文加 KV cache 重用做串流 VLN | ICRA 2026 | 178 | [634](https://github.com/OpenRobotLab/StreamVLN) |
| 奠基 | 引用、Star | 2025 | [JanusVLN](https://arxiv.org/abs/2509.22548) · [專案頁](https://miv-xjtu.github.io/JanusVLN.github.io/) | Xi'an Jiaotong / Alibaba | 語意與空間幾何拆成雙隱式記憶，固定大小免記憶膨脹 | ICLR 2026 | 137 | [602](https://github.com/MIV-XJTU/JanusVLN) |
| 奠基 | 引用 | 2025 | [UniGoal](https://arxiv.org/abs/2503.10630) · [專案頁](https://bagh2178.github.io/UniGoal/) | Tsinghua / NTU | 統一圖表示把類別、影像、文字目標做零樣本導航 | CVPR 2025 | 123 | [370](https://github.com/bagh2178/UniGoal) |
| 奠基 | 獲獎 | 2020 | [3D-MOS (Multi-Resolution POMDP)](https://arxiv.org/abs/2005.02878) | Brown / MIT | 多解析度八叉樹信念的 POMDP，在 3D 空間有效率地搜尋多個目標物件 | IROS 2021 | 32 | 未公開 |
| 主流 | 引用 | 2022 | [LM-Nav](https://arxiv.org/abs/2207.04429) · [專案頁](https://sites.google.com/view/lmnav) | UC Berkeley | 用現成 LLM + VLM + ViNT 類導航模型組合，不需標註語言資料就能照指令走 | CoRL 2022 | 825 | [272](https://github.com/blazejosinski/lm_nav) |
| 主流 | 引用 | 2023 | [NavGPT](https://arxiv.org/abs/2305.16986) | Adelaide / ANU | 純 LLM 推理做 VLN，把觀測轉文字 | AAAI 2024 | 501 | [353](https://github.com/GengzeZhou/NavGPT) |
| 主流 | 引用、Star、獲獎、推薦 | 2023 | [VLFM](https://arxiv.org/abs/2312.03275) · [專案頁](http://naoki.io/vlfm) | Boston Dynamics AI Institute | VLM 算語意價值地圖引導 frontier 探索，Spot 實機 zero-shot 物件導航 | ICRA 2024 | 453 | [826](https://github.com/bdaiinstitute/vlfm) |
| 主流 | 引用 | 2021 | [HAMT](https://arxiv.org/abs/2110.13309) · [專案頁](https://cshizhe.github.io/projects/vln_hamt.html) | Inria / ENS | 階層式 ViT 編碼完整全景歷史取代 RNN 記憶 | NeurIPS 2021 | 434 | [152](https://github.com/cshizhe/VLN-HAMT) |
| 主流 | 引用 | 2022 | [CoW (CLIP on Wheels)](https://arxiv.org/abs/2203.10421) · [專案頁](https://cow.cs.columbia.edu/) | Columbia | 把 CLIP 接上探索策略做 zero-shot 物件導航 | CVPR 2023 | 365 | [158](https://github.com/real-stanford/cow) |
| 主流 | 引用 | 2022 | [ZSON](https://arxiv.org/abs/2206.12403) | Georgia Tech | CLIP 目標嵌入讓 ImageNav 策略零樣本找物件 | NeurIPS 2022 | 352 | [110](https://github.com/gunagg/zson) |
| 主流 | 引用、獲獎 | 2022 | [DUET](https://arxiv.org/abs/2202.11742) · [專案頁](https://cshizhe.github.io/projects/vln_duet.html) | Inria / ENS / IIIT Hyderabad | 線上拓撲圖做全域規劃，搭配局部細粒度跨模態推理 | CVPR 2022 | 327 | [293](https://github.com/cshizhe/VLN-DUET) |
| 主流 | 引用 | 2021 | [EmbCLIP](https://arxiv.org/abs/2111.09888) | AI2 | 只換 CLIP 視覺骨幹不加任務設計就超越多項導航基線 | CVPR 2022 | 304 | [131](https://github.com/allenai/embodied-clip) |
| 主流 | 引用 | 2023 | [ETPNav](https://arxiv.org/abs/2304.03047) | UCAS / CASIA 等 | 連續環境 VLN 用線上拓撲圖做高層規劃 | TPAMI 2024 | 298 | [497](https://github.com/MarSaKi/ETPNav) |
| 主流 | 引用 | 2023 | [ESC](https://arxiv.org/abs/2301.13166) | UC Santa Cruz / Samsung Research | LLM 常識轉成軟性邏輯約束引導 frontier 探索 | ICML 2023 | 298 | 未公開 |
| 主流 | 引用 | 2024 | [Uni-NaVid](https://arxiv.org/abs/2412.06224) · [專案頁](https://pku-epic.github.io/Uni-NaVid/) | PKU | 一個 VLM 統一 VLN、物件導航、問答、跟人等導航任務 | RSS 2025 | 232 | [359](https://github.com/jzhzhang/Uni-NaVid) |
| 主流 | 引用 | 2024 | [SG-Nav](https://arxiv.org/abs/2410.08189) · [專案頁](https://bagh2178.github.io/SG-Nav/) | Tsinghua / BUPT | 線上 3D 場景圖分層提示 LLM 做零樣本物件導航 | NeurIPS 2024 | 231 | [356](https://github.com/bagh2178/SG-Nav) |
| 主流 | 引用 | 2023 | [NaviLLM](https://arxiv.org/abs/2312.02010) | CUHK / Shanghai AI Lab | schema 化提示讓單一 LLM 統一多種導航任務 | CVPR 2024 | 218 | [241](https://github.com/zd11024/NaviLLM) |
| 主流 | Star、推薦 | 2022 | [VLN Survey](https://arxiv.org/abs/2203.12667) | UC Santa Cruz / Adelaide / USC | 依溝通複雜度與任務目標分類整理 VLN 任務與方法 | ACL 2022 | 215 | [610](https://github.com/UCSB-AI/awesome-vision-language-navigation) |
| 主流 | 引用 | 2023 | [GridMM](https://arxiv.org/abs/2307.12907) | ICT-CAS / UCAS | 動態成長的俯視網格記憶地圖結構化已訪環境 | ICCV 2023 | 205 | [107](https://github.com/MrZihan/GridMM) |
| 主流 | 引用、獲獎、基準 | 2023 | [ScaleVLN](https://arxiv.org/abs/2307.15644) | Shanghai AI Lab / Adelaide / UNC 等 | 用 1200+ 場景合成 490 萬筆 VLN 訓練資料 | ICCV 2023 | 189 | [228](https://github.com/wz0919/ScaleVLN) |
| 主流 | 引用 | 2024 | [MapGPT](https://arxiv.org/abs/2401.07314) · [專案頁](https://chen-judge.github.io/MapGPT/) | HKU / SYSU / Meituan | 線上拓撲地圖轉成提示讓 GPT 做全域路徑規劃 | ACL 2024 | 171 | [138](https://github.com/chen-judge/MapGPT) |
| 主流 | 引用 | 2023 | [GOAT](https://arxiv.org/abs/2311.06430) | UIUC / CMU / Georgia Tech 等 | 多模態目標、終身記憶的通用導航系統，實機長時間部署 | RSS 2024 | 164 | 未公開 |
| 主流 | 引用 | 2023 | [LGX](https://arxiv.org/abs/2303.03480) | UMD | LLM 序列決策加開放詞彙偵測找語言描述的目標物 | RA-L 2024 | 163 | [72](https://github.com/vdorbala/LGX) |
| 主流 | 引用、基準 | 2024 | [GOAT-Bench](https://arxiv.org/abs/2404.06609) · [專案頁](https://mukulkhanna.github.io/goat-bench) | Georgia Tech / CMU / UIUC 等 | 多模態目標的終身導航基準 | CVPR 2024 | 155 | [165](https://github.com/Ram81/goat-bench) |
| 主流 | 引用 | 2024 | [NavGPT-2](https://arxiv.org/abs/2407.12366) | Adelaide / Adobe / UNC 等 | 凍結 LLM 的 VLM 特徵接拓撲圖策略，保留可解釋推理 | ECCV 2024 | 153 | [257](https://github.com/GengzeZhou/NavGPT-2) |
| 主流 | 引用 | 2023 | [PixNav](https://arxiv.org/abs/2309.10309) | Southeast Univ. / PKU / Shanghai AI Lab | 以像素為目標的導航技能銜接基礎模型與底層移動 | ICRA 2024 | 152 | [139](https://github.com/wzcai99/Pixel-Navigator) |
| 主流 | 引用 | 2024 | [NavCoT](https://arxiv.org/abs/2403.07376) | SYSU / Huawei Noah's Ark | LLM 自我引導解耦推理（想像、篩選、預測）並參數高效微調 | TPAMI 2025 | 152 | [144](https://github.com/expectorlin/NavCoT) |
| 主流 | 引用 | 2024 | [OpenFMNav](https://arxiv.org/abs/2402.10670) | PKU / Notre Dame | LLM 解析自由指令加 VLM 建語意地圖做開放集物件導航 | NAACL 2024 Findings | 135 | [64](https://github.com/yxKryptonite/OpenFMNav) |
| 主流 | 引用、基準 | 2024 | [HM3D-OVON](https://arxiv.org/abs/2409.14296) | Georgia Tech / Meta | 379 類開放詞彙物件導航資料集與基準 | IROS 2024 | 123 | [149](https://github.com/naokiyokoyama/ovon) |
| 主流 | 引用、推薦 | 2024 | [VLN Foundation Model Survey](https://arxiv.org/abs/2407.07035) | Michigan State / UMich / UNC 等 | 以規劃推理框架整理基礎模型時代的 VLN 方法 | TMLR 2024 | 119 | [306](https://github.com/zhangyuejoslin/VLN-Survey-with-Foundation-Models) |
| 主流 | 引用 | 2024 | [VoroNav](https://arxiv.org/abs/2401.02695) | PKU / Shanghai AI Lab / HKU | 簡化 Voronoi 圖萃取探索路徑節點交給 LLM 決策 | ICML 2024 | 119 | 未公開 |
| 主流 | 引用 | 2025 | [NavFoM](https://arxiv.org/abs/2509.12129) · [專案頁](https://pku-epic.github.io/NavFoM-Web/) | PKU / Galbot / USTC 等 | 跨載具跨任務導航基礎模型，800 萬筆多機種資料訓練 | ICLR 2026 | 110 | 未公開 |
| 主流 | 引用 | 2024 | [LH-VLN](https://arxiv.org/abs/2412.09082) · [專案頁](https://hcplab-sysu.github.io/LH-VLN/) | SYSU | 多階段長程 VLN 任務，含自動資料生成平台與基準 | CVPR 2025 | 107 | [267](https://github.com/HCPLab-SYSU/LH-VLN) |
| 主流 | 引用 | 2024 | [AO-Planner](https://arxiv.org/abs/2407.05890) | HKU / SYSU / Meituan | VLM 預測可行走路徑點，補上連續 VLN 底層控制 | AAAI 2025 | 106 | [49](https://github.com/chen-judge/AO-Planner) |
| 主流 | 引用 | 2024 | [Mobility VLA](https://arxiv.org/abs/2407.07775) | Google DeepMind | 長脈絡 VLM 看導覽影片建拓撲圖，再照多模態指令導航 | CoRL 2024 | 103 | 未公開 |
| 主流 | 引用 | 2024 | [Open-Nav](https://arxiv.org/abs/2409.18794) | Adelaide / SCUT | 開源 LLM 搭配時空 CoT 做連續環境零樣本 VLN | ICRA 2025 | 103 | [187](https://github.com/YanyuanQiao/Open-Nav) |
| 主流 | 引用 | 2024 | [VER](https://arxiv.org/abs/2403.14158) | Zhejiang | 多視角 2D 特徵聚合成 3D 體素表示環境 | CVPR 2024 | 99 | [143](https://github.com/DefaultRui/VLN-VER) |
| 主流 | 引用、推薦 | 2025 | [MapNav](https://arxiv.org/abs/2502.13451) | HKUST(GZ) / BAAI / Tsinghua | 標註語意俯視地圖取代歷史影格當 VLM 記憶 | ACL 2025 | 97 | [34](https://github.com/linglingxiansen/MapNav) |
| 主流 | 引用、Star、HF、機構、推薦 | 2025 | [DualVLN](https://arxiv.org/abs/2512.08186) · [專案頁](https://internrobotics.github.io/internvla-n1-dualvln.github.io/) | Shanghai AI Lab / Zhejiang / Tsinghua 等 | VLM 慢速預測路徑點、輕量策略快速執行的雙系統 VLN | arXiv | 97 | [1,142](https://github.com/InternRobotics/InternNav) |
| 主流 | 引用 | 2024 | [HNR](https://arxiv.org/abs/2404.01943) | ICT-CAS / UCAS | 神經輻射表示預測候選點未來特徵做前瞻探索 | CVPR 2024 | 94 | [110](https://github.com/MrZihan/HNR-VLN) |
| 主流 | 引用 | 2025 | [MTU3D](https://arxiv.org/abs/2507.04047) · [專案頁](https://mtu3d.github.io) | Tsinghua / BIGAI / BIT 等 | 3D 視覺定位與主動探索合一，支援多種目標模態 | ICCV 2025 | 91 | [275](https://github.com/MTU3D/MTU3D) |
| 主流 | 引用、獲獎 | 2024 | [PoliFormer](https://arxiv.org/abs/2406.20083) · [專案頁](https://poliformer.allen.ai) | AI2 | 大規模 RL 訓練 Transformer 策略，RGB 直接轉實機 | CoRL 2024 | 89 | [106](https://github.com/allenai/PoliFormer) |
| 主流 | 引用 | 2024 | [GOAT (causal VLN)](https://arxiv.org/abs/2404.10241) | Tongji | 因果推論去除視覺、語言、歷史中的資料偏差 | CVPR 2024 | 86 | [104](https://github.com/CrystalSixone/VLN-GOAT) |
| 主流 | 引用、推薦 | 2024 | [CA-Nav](https://arxiv.org/abs/2412.10137) | CASIA / UCAS | 零樣本 VLN-CE 拆成約束感知的子指令完成流程 | TPAMI 2025 | 81 | [85](https://github.com/Chenkehan21/CA-Nav-code) |
| 主流 | 引用、Star | 2025 | [VLN-R1](https://arxiv.org/abs/2506.17221) · [專案頁](https://vlnr1.github.io) | Shanghai AI Lab / HKU | LVLM 以 GRPO 強化微調直接輸出連續導航動作 | arXiv | 79 | [544](https://github.com/Qi-Zhangyang/GPT4Scene-and-VLN-R1) |
| 主流 | 引用 | 2025 | [ApexNav](https://arxiv.org/abs/2504.14478) | HKUST(GZ) / SUSTech | 依語意線索強弱切換探索策略，目標中心融合抗誤檢 | RA-L 2025 | 76 | [474](https://github.com/SYSU-STAR/ApexNav) |
| 主流 | 引用、獲獎 | 2025 | [WMNav](https://arxiv.org/abs/2503.02247) | CASIA / Wuhan Univ. / UTS | VLM 當世界模型預測決策結果並回饋策略 | IROS 2025 | 75 | [182](https://github.com/B0B8K1ng/WMNavigation) |
| 主流 | 引用、推薦 | 2025 | [NavMorph](https://arxiv.org/abs/2506.23468) | CASIA / UCAS | 隱空間自我演化世界模型，導航中線上適應環境 | ICCV 2025 | 62 | [94](https://github.com/Feliciaxyao/NavMorph) |
| 主流 | 引用 | 2025 | [OmniNav](https://arxiv.org/abs/2509.25687) | Alibaba / PKU | 單一架構統一指令、物件、點目標導航與探索 | ICLR 2026 | 62 | [238](https://github.com/amap-cvlab/OmniNav) |
| 主流 | 引用、機構 | 2025 | [OmniVLA](https://arxiv.org/abs/2509.19480) | UC Berkeley / Toyota / Princeton | 語言、座標、影像多種目標模態共用的導航 VLA | ICRA 2026 | 61 | [362](https://github.com/NHirose/OmniVLA) |
| 主流 | 引用 | 2025 | [VLN-PE](https://arxiv.org/abs/2507.13019) | Tongji / Shanghai AI Lab / SJTU | 支援人形、四足、輪式的物理真實 VLN 平台與評測 | ICCV 2025 | 47 | 未公開 |
| 主流 | 引用 | 2025 | [OctoNav](https://arxiv.org/abs/2506.09839) · [專案頁](https://buaa-colalab.github.io/OctoNav) | Beihang / NUS / PKU 等 | 多模態多能力自由指令基準，加先思考再行動的 R1 模型 | CVPR 2026 | 43 | [78](https://github.com/buaa-colalab/OctoNav-R1) |
| 主流 | 引用 | 2025 | [SmartWay](https://arxiv.org/abs/2503.10069) · [專案頁](https://sxyxs.github.io/smartway/) | Adelaide | 強化路徑點預測器加可回溯的 MLLM 導航器 | IROS 2025 | 41 | [20](https://github.com/sxyxs/SmartWay-Code) |
| 主流 | 引用、推薦 | 2025 | [CorrectNav](https://arxiv.org/abs/2508.10416) | PKU | 從錯誤軌跡自動產生自我修正資料反覆後訓練 | AAAI 2026 | 38 | [33](https://github.com/owlet914/CorrectNav) |
| 主流 | 引用、獲獎 | 2025 | [Dynam3D](https://arxiv.org/abs/2505.11383) | NUS | 動態分層 3D token 當 VLM 輸入，隨環境更新 | NeurIPS 2025 | 37 | [95](https://github.com/MrZihan/Dynam3D) |
| 主流 | 引用 | 2025 | [BeliefMapNav](https://arxiv.org/abs/2506.06487) | SJTU / UMich | 3D 體素信念地圖估計目標分布，結合序列路徑規劃 | NeurIPS 2025 | 34 | [51](https://github.com/ZiboKNOW/BeliefMapNav) |
| 主流 | 引用 | 2025 | [OpenIN](https://arxiv.org/abs/2501.04279) | BIT | 載體關係場景圖追蹤會移動的物件實例 | RA-L 2025 | 31 | 未公開 |
| 主流 | 引用 | 2025 | [MoRE](https://arxiv.org/abs/2503.08007) | Zhejiang / Westlake / Monash 等 | 多 LoRA 專家 VLA 搭配 RL 微調，用混合品質資料 | ICRA 2025 | 30 | 未公開 |
| 新興 | 獲獎 | 2022 | [ViKiNG](https://arxiv.org/abs/2202.11271) · [專案頁](https://sites.google.com/view/viking-release) | UC Berkeley | 學習式局部可通行性加上衛星圖、路網等地理提示做啟發式搜尋，實機走到公里級目標 | RSS 2022 | 115 | 未公開 |
| 新興 | 推薦 | 2021 | [VLN Survey and Taxonomy](https://arxiv.org/abs/2108.11544) | 未確認 | VLN 任務分類與方法綜述 | Neural Computing and Applications 2024 | 91 | 未公開 |
| 新興 | 推薦 | 2026 | [HSAN](https://arxiv.org/abs/2606.01565) | HUST / NTU / UCL | 分層語意場景圖加最佳傳輸做連續環境 VLN 規劃 | NeurIPS 2025 | 24 | 未公開 |
| 新興 | 獲獎 | 2025 | [SocialNav](https://arxiv.org/abs/2511.21135) | Amap Alibaba | 「大腦-動作」階層架構，以 700 萬筆 SocNav 資料訓練遵守社會規範的導航基礎模型 | CVPR 2026 | 22 | 未公開 |
| 新興 | 推薦 | 2025 | [MobileVLA-R1](https://arxiv.org/abs/2511.17889) · [專案頁](https://aigeeksgroup.github.io/MobileVLA-R1/) | PKU | CoT 對齊加 GRPO 讓四足 VLA 推理並連續控制 | arXiv | 16 | [118](https://github.com/AIGeeksGroup/MobileVLA-R1) |
| 新興 | 推薦 | 2025 | [3D Gaussian Map VLN](https://arxiv.org/abs/2605.26500) | Zhejiang | 線上建 3D 高斯地圖並做開放集語意分組 | ICCV 2025 | 13 | [10](https://github.com/Gaozzzz/3D-Gaussian-Map-VLN) |
| 新興 | 獲獎、推薦 | 2025 | [VL-Nav](https://arxiv.org/abs/2502.00931) | Univ. at Buffalo / CMU | 神經符號：3D 場景圖與影像記憶輔助 VLM 拆解任務 | IROS 2026 | 11 | 未公開 |
| 新興 | 推薦 | 2026 | [NaVIDA](https://arxiv.org/abs/2601.18188) | SUSTech / MBZUAI / SpatialTemporal AI | 加入逆動力學監督，學動作如何改變觀測 | arXiv | 10 | [35](https://github.com/waynechu1021/NAVIDA) |
| 新興 | 推薦 | 2026 | [HSGM](https://arxiv.org/abs/2606.00095) | ECNU / Bosch / KAUST | 分層語意幾何地圖把 3D 資訊轉成 VLM 可用格式 | CVPR 2026 | 10 | [41](https://github.com/Teacher-Tom/HSGM_public) |
| 新興 | 獲獎 | 2024 | [MiniVLN](https://arxiv.org/abs/2409.18800) | CASIA | 兩階段漸進式知識蒸餾，小模型保有 VLN 表現以利部署 | ICRA 2025 | 10 | 未公開 |
| 新興 | 獲獎 | 2023 | [Dynamic Navigation Goal from Dialogue](https://doi.org/10.1109/IROS55552.2023.10342509) | Shanghai Inst. of Tech. / Tsinghua 等 | 從自然語言對話中抽取會移動的目標（如人）的位置作為導航目標 | IROS 2023 | 7 | 未公開 |
| 新興 | 推薦 | 2026 | [Uncertainty-Aware Gaussian Map](https://arxiv.org/abs/2605.26503) | Zhejiang / Huawei | 語意高斯地圖顯式建模幾何、語意、外觀不確定性 | arXiv | 4 | [10](https://github.com/Gaozzzz/Uncertainty-Aware-VLN) |
| 新興 | 機構、推薦 | 2026 | [WildOS](https://arxiv.org/abs/2602.19308) · [專案頁](https://leggedrobotics.github.io/wildos/) | NASA JPL / ETH 等 | 戶外長程物件搜尋：稀疏導航圖加基礎模型可通行性推理 | T-FR 2026 | 3 | [159](https://github.com/nasa-jpl/nebula2-wildos) |
| 新興 | 獲獎 | 2026 | [SoftNav](https://arxiv.org/abs/2607.14586) | Shandong / Zhejiang | 3D 場景改以 embedding token 直接注入 VLM，取代轉成文字描述 | IROS 2026 | 1 | 未公開 |
| 新興 | 推薦 | 2026 | [NavOne](https://arxiv.org/abs/2605.06317) | SCUT | 在預建俯視地圖上一步預測整條全域路徑 | arXiv | 0 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [AVALON](https://arxiv.org/abs/2610.21586) | HKU | 只需平面圖與地點線索，以人給的分層拓撲記憶做節點驗證式導航，不建全域 SLAM 圖；人與機器人共同更新記憶 | Unitree Go2 實機 12.81 m 任務 46.4 s（5/5），比 DimOS-Go2 少 40.9% 時間 | 未公開 | arXiv |
| 2026-07 | [Robostral Navigate](https://arxiv.org/abs/2607.20785) · [專案頁](https://mistral.ai/news/robostral-navigate) | Mistral AI | 8B VLM 只用單眼 RGB，在畫面上指出下一個目標點；目標不在視野時輸出局部座標位移 | R2R-CE val-unseen SR 76.6%；online RL +3.2% | 未公開 | arXiv、Mistral 官網 |
| 2026-07 | [ABot-N1](https://arxiv.org/abs/2607.10383) · [專案頁](https://amap-cvlab.github.io/ABot-Navigation/ABot-N1/) | Alibaba AMAP | 慢 VLM 推理出影像錨點，快模組轉成連續 waypoint；同一架構做 point/object/POI/指令/跟人五種任務 | 室內 95.4%、室外 92.9% SR；POI 抵達 77.3% | [GitHub](https://github.com/amap-cvlab/ABot-Navigation) | arXiv |
| 2026-04 | [Robot Navigation via Foundation Language Models: A Review](https://dl.acm.org/doi/10.1145/3802539) | ECNU / HIT 等 | ACM CSUR 綜述 |  | 未公開 | ACM Computing Surveys 2026 |

## 局部導航與規劃（diffusion / world model / 探索）

### 在解決的問題

- 從感測器直接輸出可行軌跡，取代手調的代價地圖與規劃器參數。
- 泛化到沒見過的環境與機體：靠跨機體資料或大規模模擬訓練。
- 多解行為（岔路要選一邊）用 diffusion 表達；預測動作後果再規劃則走向 world model。
- 安全保證：學習式策略沒有碰撞保證，常另外疊安全濾波器。

### 重要論文（資料日期 2026-10-20）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | Star、推薦 | 2020 | [FUEL](https://arxiv.org/abs/2010.11561) | HKUST | 增量前沿結構加分層規劃的快速無人機探索 | RA-L 2021 | 414 | [1,497](https://github.com/HKUST-Aerial-Robotics/FUEL) |
| 奠基 | 引用、Star、獲獎 | 2024 | [Navigation World Models](https://arxiv.org/abs/2412.03572) · [專案頁](https://www.amirbar.net/nwm/) | Meta | 可控影片生成的導航 world model，用想像軌跡做規劃 | CVPR 2025 | 367 | [701](https://github.com/facebookresearch/nwm) |
| 奠基 | 獲獎 | 2020 | [BADGR](https://arxiv.org/abs/2002.05700) | UC Berkeley | 從實機自動收集的經驗自監督學習導航，不靠幾何地圖，能學出高草可通行等語意 | RA-L 2021 | 348 | 未公開 |
| 主流 | 引用 | 2021 | [Embodied AI Survey](https://arxiv.org/abs/2103.04918) | A*STAR / NTU | 從模擬器出發整理具身 AI 研究任務的綜述 | TETCI 2022 | 599 | 未公開 |
| 主流 | 引用、Star、獲獎、推薦 | 2023 | [NoMaD](https://arxiv.org/abs/2310.07896) · [專案頁](https://general-navigation-models.github.io/nomad/) | UC Berkeley | diffusion policy 統一有目標導航與無目標探索 | ICRA 2024 | 456 | [1,328](https://github.com/robodhruv/visualnav-transformer) |
| 主流 | 引用、Star | 2023 | [ViNT](https://arxiv.org/abs/2306.14846) · [專案頁](https://visualnav-transformer.github.io) | UC Berkeley | 導航基礎模型：Transformer + 影像目標，可微調到新任務 | CoRL 2023 | 422 | [1,328](https://github.com/robodhruv/visualnav-transformer) |
| 主流 | 引用、Star | 2022 | [GNM](https://arxiv.org/abs/2210.03370) · [專案頁](https://sites.google.com/view/drive-any-robot) | UC Berkeley | 跨多種機器人資料訓練的通用視覺導航模型 | ICRA 2023 | 313 | [1,328](https://github.com/robodhruv/visualnav-transformer) |
| 主流 | 引用 | 2023 | [Social Nav Eval Guidelines](https://arxiv.org/abs/2306.16740) | 未確認 | 社交導航演算法評估的原則、指標與情境建議 | THRI 2025 | 215 | 未公開 |
| 主流 | 引用、機構 | 2024 | [CrossFormer](https://arxiv.org/abs/2408.11812) · [專案頁](https://crossformer-model.github.io/) | UC Berkeley / CMU | 單一 Transformer 策略控制手臂、足式、無人機等 | CoRL 2024 | 174 | [283](https://github.com/rail-berkeley/crossformer) |
| 主流 | 引用、獲獎 | 2024 | [Splat-Nav](https://arxiv.org/abs/2403.02751) | Stanford | 在 3DGS 地圖用多面體走廊做安全規劃與定位 | T-RO 2025 | 127 | [148](https://github.com/chengine/splatnav) |
| 主流 | 引用 | 2024 | [VLM-Social-Nav](https://arxiv.org/abs/2404.00210) | George Mason / UMD | 用 VLM 打分當社交合規成本項引導導航 | RA-L 2025 | 119 | 未公開 |
| 主流 | Star | 2023 | [ViPlanner](https://arxiv.org/abs/2310.00982) | ETH | 加入語意的可微分局部規劃，腿式機器人實機 | ICRA 2024 | 111 | [678](https://github.com/leggedrobotics/viplanner) |
| 主流 | 引用、Star、推薦 | 2024 | [NavRL](https://arxiv.org/abs/2409.15634) | CMU | PPO + 安全護盾的動態環境導航（原為無人機，方法可用於地面） | RA-L 2025 | 107 | [1,647](https://github.com/Zhefan-Xu/NavRL) |
| 主流 | 引用 | 2024 | [Cross-Embodiment Nav-Manip](https://arxiv.org/abs/2402.19432) | Stanford / UC Berkeley / Google DeepMind | 導航與操作資料共同訓練，驗證跨型態正向遷移 | RSS 2024 | 100 | 未公開 |
| 主流 | Star、獲獎 | 2021 | [FAR Planner](https://arxiv.org/abs/2110.09460) | CMU | 未知環境中邊建可視圖邊規劃的快速路徑規劃 | IROS 2022 | 90 | [1,025](https://github.com/MichaelFYang/far_planner) |
| 主流 | 引用、Star | 2025 | [NavDP](https://arxiv.org/abs/2505.08712) · [專案頁](https://wzcai99.github.io/navigation-diffusion-policy.github.io) | Shanghai AI Lab | 純模擬訓練 diffusion 導航策略 + 特權資訊引導，zero-shot sim-to-real | ICRA 2026 | 90 | [815](https://github.com/InternRobotics/NavDP) |
| 主流 | 引用 | 2024 | [GaussNav](https://arxiv.org/abs/2403.11625) | USTC | 以 3DGS 地圖取代 BEV 做實例影像目標導航 | TPAMI 2025 | 85 | [220](https://github.com/XiaohanLei/GaussNav) |
| 主流 | 引用 | 2025 | [NaviDiffusor](https://arxiv.org/abs/2504.10003) | Sun Yat-sen | 推論時以成本函數引導擴散模型生成導航路徑 | ICRA 2025 | 48 | [60](https://github.com/SYSU-RoboticsLab/NaviD) |
| 主流 | 引用 | 2025 | [NaviBridger](https://arxiv.org/abs/2504.10041) | Sun Yat-sen | 用先驗分佈取代高斯雜訊的擴散橋導航策略 | CVPR 2025 | 34 | [83](https://github.com/hren20/NaiviBridger) |
| 主流 | 引用、獲獎、機構 | 2025 | [FDM](https://arxiv.org/abs/2504.19322) | ETH / NVIDIA / MPI-IS | 學習感知前向動力學模型評估路徑安全性 | RSS 2025 | 32 | [360](https://github.com/leggedrobotics/fdm) |
| 新興 | 獲獎 | 2021 | [Legged-Aerial Subterranean Exploration](https://arxiv.org/abs/2111.06482) | NTNU | 四足與無人機協同探索地下環境，以圖式規劃與通訊感知的資料交換分配探索 | ICRA 2022 | 122 | 未公開 |
| 新興 | 獲獎、基準 | 2022 | [TartanDrive](https://arxiv.org/abs/2205.01791) | CMU AirLab | ATV 越野駕駛約 20 萬筆、7 種感測器的資料集，用於學習越野動力學模型 | ICRA 2022 | 108 | [127](https://github.com/castacks/tartan_drive) |
| 新興 | 獲獎 | 2023 | [Sequential Neural Barriers](https://arxiv.org/abs/2307.03015) | （論文未列單位） | 依序學習神經控制障壁函數，動態障礙物數量增加時仍能擴展且對分布漂移較穩 | IROS 2023 | 29 | 未公開 |
| 新興 | 獲獎 | 2025 | [Realm](https://arxiv.org/abs/2502.15162) | Chongqing / Sichuan / I2R | 未知環境中直接以感測資料建立視線連通約束，多機器人導航時保持彼此可見 | ICRA 2025 | 15 | 未公開 |
| 新興 | 獲獎 | 2025 | [Arm-Pushing Interactive Navigation](https://arxiv.org/abs/2503.01474) | HKUST(GZ) / HKUST | 腿式機械臂學習用手臂推開障礙物，在窄空間開出較短路徑 | IROS 2025 | 13 | 未公開 |
| 新興 | 獲獎 | 2022 | [Confidence-based Nav under Occlusion](https://doi.org/10.1109/ICRA46639.2022.9812090) | KAIST | 感測器被髒污遮擋時，以信心度驅動 RL 主動探索確保可見度 | ICRA 2022 | 12 | 未公開 |
| 新興 | 獲獎 | 2024 | [Hiking Trail Navigation](https://arxiv.org/abs/2409.15671) | West Virginia University | 語意分割判斷步道、幾何分析判斷可通行，必要時可離開步道 | IROS 2025 | 4 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [Physical AI for Intralogistics](https://arxiv.org/abs/2610.28432) | Idealworks / NVIDIA | 把 NVIDIA X-Mobility 與 COMPASS 導航策略放進倉儲數位孿生訓練，再用 Cosmos 生成 sim-to-real 變體資料微調，部署在 Jetson AGX Xavier 差速底盤 | 實機四個場景成功率 65.3%（純模擬訓練）→ 91.7%（加 Cosmos 資料），與量產導航堆疊差 8.3 點 | 未公開 | arXiv |
| 2026-10 | [LiteNWM](https://arxiv.org/abs/2610.12368) | Nanjing Univ. / Imperial / Sony AI | 輕量潛空間 world model，可機上跑 | 實機未見場景 SR 43.3%（NoMaD）→ 83.3% | 未公開 | arXiv |
| 2026-07 | [X-NavDP](https://arxiv.org/abs/2607.28560) · [專案頁](https://yty-sky.github.io/x-navdp-project-page) | Shanghai AI Lab / Fudan / SYSU | NavDP 泛化到新行為與新機體（group Q-score reweighted matching） |  | 未公開 | arXiv |

## 四足

### 在解決的問題

- 感知不可靠時仍要穩（反光、草叢、高度圖雜訊）：融合外部感知與本體感知。
- sim-to-real：大規模平行模擬 + domain randomization + 特權教師蒸餾。
- 敏捷技能（跑酷、跳躍、越溝）與技能切換。
- 從「跟隨速度指令」走向「運動與導航一體」，直接走到目標。

### 重要論文（資料日期 2026-10-20）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、獲獎 | 2022 | [Perceptive Locomotion in the Wild](https://arxiv.org/abs/2201.08117) | ETH | 高度圖感知 + 本體感知的注意力融合，ANYmal 野外實機 | Science Robotics 2022 | 1,265 | 未公開 |
| 主流 | 引用、Star | 2021 | [Learning to Walk in Minutes](https://arxiv.org/abs/2109.11978) · [專案頁](https://leggedrobotics.github.io/legged_gym/) | ETH | GPU 大規模平行 RL，幾分鐘訓練出運動策略（legged_gym） | CoRL 2021 | 1,183 | [3,151](https://github.com/leggedrobotics/legged_gym) |
| 主流 | 引用 | 2021 | [RMA](https://arxiv.org/abs/2107.04034) · [專案頁](https://ashish-kmr.github.io/rma-legged-robots/) | UC Berkeley / CMU | 快速自適應模組：以本體感知線上估計環境參數 | RSS 2021 | 1,132 | 未公開 |
| 主流 | 引用、機構 | 2022 | [DayDreamer](https://arxiv.org/abs/2206.14176) · [專案頁](https://danijar.com/daydreamer) | UC Berkeley | 世界模型讓實體機器人免模擬器直接在線學習 | CoRL 2022 | 623 | [466](https://github.com/danijar/daydreamer) |
| 主流 | 引用、獲獎 | 2023 | [ANYmal Parkour](https://arxiv.org/abs/2306.14874) · [專案頁](https://sites.google.com/leggedrobotics.com/agile-navigation) | ETH | 感知、移動、技能選擇分模組的跑酷導航 | Science Robotics 2024 | 486 | 未公開 |
| 主流 | 引用、Star | 2023 | [Extreme Parkour](https://arxiv.org/abs/2309.14341) · [專案頁](https://extreme-parkour.github.io/) | CMU | 單一神經網路以深度相機做極限跑酷 | ICRA 2024 | 424 | [1,187](https://github.com/chengxuxin/extreme-parkour) |
| 主流 | 引用、機構 | 2022 | [Rapid Locomotion](https://arxiv.org/abs/2205.02824) | MIT | 自適應課程 RL 讓 Mini Cheetah 跑出紀錄速度 | RSS 2022 | 423 | [302](https://github.com/Improbable-AI/rapid-locomotion-rl) |
| 主流 | 引用、獲獎 | 2022 | [Legged Locomotion with Egocentric Vision](https://arxiv.org/abs/2211.07638) · [專案頁](https://vision-locomotion.github.io) | CMU / Berkeley | 直接用深度影像端到端學運動，不建高度圖 | CoRL 2022 | 367 | 未公開 |
| 主流 | 引用、Star、獲獎 | 2023 | [Robot Parkour Learning](https://arxiv.org/abs/2309.05665) · [專案頁](https://robot-parkour.github.io) | Stanford / Shanghai Qi Zhi | 低成本四足以深度相機學跑酷技能 | CoRL 2023 | 348 | [1,137](https://github.com/ZiwenZhuang/parkour) |
| 主流 | 引用、Star | 2022 | [Walk These Ways](https://arxiv.org/abs/2212.03238) · [專案頁](https://gmargo11.github.io/walk-these-ways/) | MIT | 多樣行為參數化的單一策略，可調步態 | CoRL 2022 | 346 | [1,467](https://github.com/Improbable-AI/walk-these-ways) |
| 主流 | 引用、獲獎 | 2022 | [Legged Optimization Control Survey](https://arxiv.org/abs/2211.11644) | Notre Dame / UPenn / LAAS-CNRS 等 | 回顧足式機器人模型式最佳化控制的綜述 | T-RO 2024 | 316 | 未公開 |
| 主流 | 引用、獲獎 | 2022 | [Perceptive NMPC](https://arxiv.org/abs/2208.08373) | ETH | 以凸落腳區約束嵌入全身 NMPC 的感知式運動 | T-RO 2023 | 313 | 未公開 |
| 主流 | 引用 | 2023 | [DreamWaQ](https://arxiv.org/abs/2301.10602) · [專案頁](https://sites.google.com/view/dreamwaq) | KAIST | 無外部感知的盲走策略，用隱式地形想像過複雜地形 | ICRA 2023 | 259 | 未公開 |
| 主流 | 引用、獲獎 | 2023 | [Locomotion on Deformable Terrain](https://doi.org/10.1126/scirobotics.ade2256) | KAIST | 在沙地等可變形地形上的四足 RL 運動，模擬可變形接觸 | Science Robotics 2023 | 252 | 未公開 |
| 主流 | Star | 2022 | [Elevation Mapping CuPy](https://arxiv.org/abs/2204.12876) | ETH | GPU 加速的機器人中心高度圖，多數感知式運動策略的輸入 | IROS 2022 | 206 | [1,132](https://github.com/leggedrobotics/elevation_mapping_cupy) |
| 主流 | 引用、獲獎 | 2023 | [DTC](https://arxiv.org/abs/2309.15462) | ETH | RL 策略追蹤軌跡最佳化參考，兼顧精準與強健 | Science Robotics 2024 | 201 | 未公開 |
| 主流 | 引用、Star、HF、獲獎 | 2024 | [ABS](https://arxiv.org/abs/2401.17583) · [專案頁](https://agile-but-safe.github.io/) | CMU | 敏捷策略 + 學到的可達避碰價值函數，高速且安全 | RSS 2024 | 183 | [634](https://github.com/LeCAR-Lab/ABS) |
| 主流 | 引用、獲獎 | 2023 | [Legged Planetary Exploration Team](https://arxiv.org/abs/2307.10079) | ETH | 多隻技能互補的四足機器人團隊探勘行星類比地形 | Science Robotics 2023 | 166 | 未公開 |
| 主流 | 引用、Star、機構 | 2024 | [DrEureka](https://arxiv.org/abs/2406.01967) · [專案頁](https://eureka-research.github.io/dr-eureka/) | UPenn / NVIDIA / UT Austin | LLM 自動設計獎勵與域隨機化參數做 sim-to-real | RSS 2024 | 137 | [947](https://github.com/eureka-research/DrEureka) |
| 主流 | 引用、Star、獲獎、機構 | 2024 | [DIAL-MPC](https://arxiv.org/abs/2409.15610) · [專案頁](https://lecar-lab.github.io/dial-mpc/) | CMU | 擴散式退火取樣 MPC，免訓練做全階力矩控制 | ICRA 2025 | 116 | [1,011](https://github.com/LeCAR-Lab/dial-mpc) |
| 主流 | 引用、獲獎 | 2025 | [Attention Map Encoding](https://arxiv.org/abs/2506.09588) | ETH / Disney Research | 以本體感知為條件的注意力地圖編碼，泛化稀疏落腳地形 | Science Robotics 2025 | 105 | 未公開 |
| 主流 | 引用 | 2024 | [PIE](https://arxiv.org/abs/2408.13740) | Zhejiang | 單階段隱式＋顯式雙層估計的端到端跑酷策略 | RA-L 2024 | 92 | 未公開 |
| 主流 | 引用、機構 | 2024 | [DiffuseLoco](https://arxiv.org/abs/2404.19264) | UC Berkeley / Simon Fraser | 從離線資料訓練擴散策略並即時跑在實機 | CoRL 2024 | 83 | [199](https://github.com/HybridRobotics/DiffuseLoco) |
| 主流 | 引用 | 2025 | [Parkour in the Wild](https://arxiv.org/abs/2505.11164) | ETH RSL | 多專家策略蒸餾後再 RL 微調的通用敏捷運動 | IJRR 2026 | 68 | 未公開 |
| 主流 | 引用、獲獎 | 2025 | [High-Speed Legged Navigation](https://arxiv.org/abs/2506.02835) | KAIST | 取樣式落腳規劃加物理模擬篩選的高速離散地形導航 | Science Robotics 2025 | 61 | 未公開 |
| 主流 | 引用、機構 | 2025 | [MoE-Loco](https://arxiv.org/abs/2503.08564) · [專案頁](https://moe-loco.github.io/) | Tsinghua / Shanghai Qi Zhi / MIT | 混合專家緩解多任務 RL 梯度衝突，單策略跨地形 | IROS 2025 | 51 | [61](https://github.com/hrh6666/MoE-Loco) |
| 主流 | 引用 | 2025 | [TRG-planner](https://arxiv.org/abs/2501.01806) | KAIST | 以穿越風險圖兼顧地形安全與距離的路徑規劃 | RA-L 2025 | 36 | [31](https://github.com/wasahaiah/TRG-planner) |
| 主流 | 引用、獲獎 | 2025 | [LocoFormer](https://arxiv.org/abs/2509.23745) | Skild AI | 在程序生成的大量機體上做長上下文 RL，測試時靠歷史自行適應未見過的腿式與輪式機體 | CoRL 2025 | 35 | 未公開 |
| 主流 | 引用、機構 | 2025 | [SPI-Active](https://arxiv.org/abs/2505.14266) · [專案頁](https://lecar-lab.github.io/spi-active_/) | CMU / Google DeepMind | 取樣式系統辨識加主動探索縮小 sim-to-real 差距 | CoRL 2025 | 32 | [230](https://github.com/LeCAR-Lab/SPI-Active) |
| 主流 | 引用、獲獎 | 2025 | [Unified Force-Position Policy](https://arxiv.org/abs/2505.20829) · [專案頁](https://unified-force.github.io/) | BUPT / BIGAI | 不靠力感測器，單一策略同時建模接觸力與位置控制，用於四足帶手臂的接觸型移動操作 | CoRL 2025 | 31 | 未公開 |
| 新興 | 獲獎 | 2022 | [AMP for Locomotion](https://arxiv.org/abs/2203.15103) | UC Berkeley / Google | 用對抗式動作先驗取代繁瑣的手調獎勵，四足實機學出自然且節能的步態 | IROS 2022 | 203 | 未公開 |
| 新興 | 獲獎 | 2021 | [Fast and Efficient Gait Transitions](https://arxiv.org/abs/2104.04644) · [專案頁](https://sites.google.com/view/fast-and-efficient) | University of Washington / Google | 高層策略以 ES 學步態選擇、低層 MPC 執行，只用能耗獎勵就自然長出隨速度切換步態 | CoRL 2021 | 139 | [93](https://github.com/yxyang/fast_and_efficient) |
| 新興 | 獲獎 | 2021 | [Robotic Guide Dog](https://arxiv.org/abs/2103.14300) | UC Berkeley | 四足以牽繩混合物理互動引導人通過狹窄雜亂空間，牽繩鬆緊納入規劃 | ICRA 2021 | 120 | 未公開 |
| 新興 | 獲獎 | 2022 | [Quadruped Soccer Shooting](https://arxiv.org/abs/2208.01160) | UC Berkeley / Mila | 階層式 RL：高層規劃踢球軌跡、低層追蹤，四足實機精準把球踢向指定目標 | IROS 2022 | 90 | 未公開 |
| 新興 | 獲獎 | 2024 | [Confined-Space Legged Locomotion](https://arxiv.org/abs/2403.00187) | ETH RSL | 以 3D 體素表示輸入 RL 策略，四足能調整姿態鑽過狹窄空間 | ICRA 2024 | 68 | 未公開 |
| 新興 | 獲獎 | 2023 | [Resilient Legged Local Navigation](https://arxiv.org/abs/2310.03581) | ETH RSL | 把感知失效建模成看不見的障礙與坑洞，RL 局部導航策略學會靠本體感覺應變 | ICRA 2024 | 51 | 未公開 |
| 新興 | 獲獎 | 2022 | [Distributed DDPC Collaborative Legged](https://arxiv.org/abs/2211.06917) | Virginia Tech / Caltech | 以行為系統理論建模多台互相拘束的四足，分散式資料驅動預測控制協同行走 | ICRA 2023 | 33 | 未公開 |
| 新興 | 獲獎 | 2024 | [Quadruped Ladder Climbing](https://arxiv.org/abs/2409.17731) · [專案頁](https://sites.google.com/leggedrobotics.com/climbingladders) | ETH RSL | 特製鉤爪加上 RL 策略，四足實機可靠爬工業爬梯 | IROS 2025 | 26 | 未公開 |
| 新興 | 獲獎 | 2022 | [PI-ARS](https://arxiv.org/abs/2207.13224) · [專案頁](https://kuanghuei.github.io/piars) | Google Research | 以預測資訊表示壓縮視覺輸入，讓演化策略能訓練較大的視覺步行策略 | IROS 2022 | 21 | 未公開 |
| 新興 | 獲獎 | 2023 | [Steep Planetary Terrain Locomotion](https://doi.org/10.1109/IROS55552.2023.10341665) | ETH Zurich | 針對行星陡坡與鬆軟地形的四足行走策略 | IROS 2023 | 21 | 未公開 |
| 新興 | 獲獎 | 2024 | [Leader Following Quadruped](https://arxiv.org/abs/2410.00572) | ETH RSL | 四足以視覺追蹤領隊者並同時避障，免手動遙控跟隨 | ICRA 2025 | 18 | 未公開 |
| 新興 | 獲獎 | 2022 | [Motion Primitive Graph](https://arxiv.org/abs/2209.07503) | Caltech | 在動作基元圖上規劃，依擾動即時切換步態基元，提升腿式機器人穩健性 | ICRA 2023 | 16 | 未公開 |
| 新興 | 獲獎 | 2021 | [Mini Cheetah Optimal Landing](https://arxiv.org/abs/2110.02799) | MIT / UMass Amherst | 不預設接觸序列，即時最佳化落地姿勢與反作用力，從各種墜落狀態恢復 | ICRA 2022 | 8 | 未公開 |
| 新興 | 獲獎 | 2026 | [DAWN](https://arxiv.org/abs/2609.29092) | KOREATECH | 在 world model 裡學習去除深度雜訊，跑酷策略不需手調深度濾波器 | IROS 2026 | 1 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-07 | [APT-RL: Agile perceptive multi-skill locomotion](https://arxiv.org/abs/2607.13579) · [專案頁](https://skillquadsr.github.io/) | KAIST 等 | 軌跡最佳化 8 分鐘產生 18 萬條動作先驗，再用 RL + 機載感知適應 3D 地形 | 單一策略過樓梯／欄／踏石／溝；瞬間最高 6 m/s | 未公開 | Science Robotics 2026 |
| 2026-06 | [Perceptive Platform Adaptive Locomotion](https://arxiv.org/abs/2606.25179) | Oxford DRS | 感知只給 critic，感知有雜訊時比完全感知策略穩 |  | 未公開 | arXiv |
| 2026-06 | [GUIDE](https://arxiv.org/abs/2606.10832) · [專案頁](https://guide-navigation.github.io/) | Zhejiang / TeleAI / Oxford 等 | 端到端腿式導航 |  | 未公開 | arXiv |
| 2026-04 | [HiPAN](https://arxiv.org/abs/2604.26504) · [專案頁](https://sgvr.kaist.ac.kr/~Jeil/project_page_HiPAN/) | KAIST | 非結構 3D 環境的姿態自適應分層導航 |  | 未公開 | RA-L 2026 |

## 輪足（雙足輪、四足輪）

### 在解決的問題

- 混合運動：何時滾、何時走、何時跨越，以及模式切換。
- 高速下的感知延遲：建圖更新跟不上速度（Lee et al. 2024 指出這限制了自主時的速度）。
- 硬體負載：輪驅動改變關節受力（Go2-W 髖關節過熱）。
- 雙足輪的平衡與越障；研究多停在運動控制，經典論文少。

### 重要論文（資料日期 2026-10-20）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 主流 | 引用、獲獎 | 2024 | [Wheeled-Legged Urban Navigation](https://arxiv.org/abs/2405.01792) | ETH | 階層式 RL 導航 + 運動，都市公里級自主任務 | Science Robotics 2024 | 217 | 未公開 |
| 新興 | 獲獎 | 2022 | [Track-leg / Wheel-leg TrajOpt](https://doi.org/10.1109/ICRA46639.2022.9812199) | Florida State | 具平滑解析導數的軌跡最佳化，讓履帶腿、輪腿機器人規劃翻越大型障礙 | ICRA 2022 | 4 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-02 | [Sparse MoE multi-mode locomotion](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1788395/full) | Beijing Institute of Technology | 雙足輪；稀疏 MoE RL，在滾動與越障間自動切換 |  | 未公開 | Frontiers in Robotics and AI 2026 |

## SLAM 與定位

### 在解決的問題

- 退化場景：長廊、隧道、空曠處 LiDAR 或視覺特徵不足。
- 多感測器緊耦合：LiDAR、IMU、相機融合。
- 學習式前端：用 DROID、MASt3R、VGGT 等取代手工特徵，處理無紋理、免校正相機。
- 稠密且寫實的地圖：NeRF／3DGS SLAM。
- 大尺度、長期：回環、地點辨識、多機器人、場景隨時間變化。

### 重要論文（資料日期 2026-10-20）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | Star、獲獎 | 2020 | [ORB-SLAM3](https://arxiv.org/abs/2007.11898) | Zaragoza | 視覺／視覺慣性／多地圖 SLAM 的標準基線 | T-RO 2021 | 4,769 | [9,163](https://github.com/UZ-SLAMLab/ORB_SLAM3) |
| 奠基 | 引用、Star、獲獎 | 2021 | [FAST-LIO2](https://arxiv.org/abs/2107.06829) | HKU MaRS | 直接點雲配準 + ikd-tree 的快速 LiDAR 慣性里程計 | T-RO 2022 | 1,906 | [5,290](https://github.com/hku-mars/FAST_LIO) |
| 奠基 | 引用、Star | 2021 | [DROID-SLAM](https://arxiv.org/abs/2108.10869) | Princeton | 可微分 BA 的深度學習視覺 SLAM | NeurIPS 2021 | 1,273 | [2,712](https://github.com/princeton-vl/DROID-SLAM) |
| 奠基 | 引用、Star | 2023 | [SplaTAM](https://arxiv.org/abs/2312.02126) · [專案頁](https://spla-tam.github.io/) | CMU | 3D Gaussian Splatting 的 RGB-D SLAM | CVPR 2024 | 756 | [2,213](https://github.com/spla-tam/SplaTAM) |
| 奠基 | 引用、Star | 2023 | [Gaussian Splatting SLAM](https://arxiv.org/abs/2312.06741) · [專案頁](https://rmurai.co.uk/projects/GaussianSplattingSLAM/) | Imperial | 單眼即時 3DGS SLAM | CVPR 2024 | 742 | [2,183](https://github.com/muskie82/MonoGS) |
| 奠基 | 引用、Star | 2024 | [MASt3R-SLAM](https://arxiv.org/abs/2412.12392) · [專案頁](https://edexheim.github.io/mast3r-slam/) | Imperial | 以 MASt3R 3D 重建先驗做即時稠密單眼 SLAM | CVPR 2025 | 330 | [3,221](https://github.com/rmurai0610/MASt3R-SLAM) |
| 奠基 | 引用、Star | 2025 | [VGGT-SLAM](https://arxiv.org/abs/2505.12549) | MIT SPARK | 用 VGGT 子地圖 + SL(4) 流形優化的 feed-forward SLAM | NeurIPS 2025 | 185 | [1,161](https://github.com/MIT-SPARK/VGGT-SLAM) |
| 奠基 | 引用、Star | 2025 | [VGGT-Long](https://arxiv.org/abs/2507.16443) | Nankai / Nanjing Univ. | 分塊、迴環、對齊讓 VGGT 擴展到公里級序列 | ICRA 2026 | 150 | [909](https://github.com/DengKaiCQ/VGGT-Long) |
| 奠基 | 獲獎 | 2020 | [Multi-Modal Landmark LVIO](https://arxiv.org/abs/2011.06838) | Oxford DRS | 從 LiDAR 抽線與平面基元，與視覺、慣性在同一因子圖緊耦合做里程計 | RA-L 2021 | 121 | 未公開 |
| 奠基 | 獲獎 | 2020 | [CodeVIO](https://arxiv.org/abs/2012.10133) | Zhejiang / Delaware | 把可最佳化的稠密深度 code 緊耦合進 VIO，同時輸出狀態估計與稠密深度 | ICRA 2021 | 58 | 未公開 |
| 主流 | 引用、Star | 2021 | [NICE-SLAM](https://arxiv.org/abs/2112.12130) · [專案頁](https://pengsongyou.github.io/nice-slam) | ETH / Zhejiang | 階層式神經隱式表示的稠密 SLAM | CVPR 2022 | 1,151 | [1,600](https://github.com/cvg/nice-slam) |
| 主流 | 引用 | 2021 | [iMAP](https://arxiv.org/abs/2103.12352) | Imperial | 首次以單一 MLP 作為即時 RGB-D SLAM 的地圖 | ICCV 2021 | 941 | 未公開 |
| 主流 | 引用、Star | 2022 | [KISS-ICP](https://arxiv.org/abs/2209.15397) | Bonn | 極簡、免調參的 point-to-point ICP LiDAR 里程計 | RA-L 2023 | 609 | [2,353](https://github.com/PRBonn/kiss-icp) |
| 主流 | 引用 | 2023 | [GS-SLAM](https://arxiv.org/abs/2311.11700) · [專案頁](https://gs-slam.github.io/) | Shanghai AI Lab / HKUST / Fudan 等 | 首個用 3D Gaussian 表示的稠密 RGB-D SLAM | CVPR 2024 | 574 | 未公開 |
| 主流 | 引用、Star | 2021 | [LVI-SAM](https://arxiv.org/abs/2104.10831) | MIT / Stevens | 因子圖緊耦合 LiDAR、視覺與慣性的里程計 | ICRA 2021 | 571 | [1,890](https://github.com/TixiaoShan/LVI-SAM) |
| 主流 | 引用、Star | 2022 | [GeoTransformer](https://arxiv.org/abs/2202.06688) | NUDT / TUM 等 | 以超點間的幾何結構編碼做無關鍵點匹配，低重疊配準不需 RANSAC 也很穩 | CVPR 2022 | 518 | [984](https://github.com/qinzheng93/GeoTransformer) |
| 主流 | 引用、Star | 2021 | [Patch-NetVLAD](https://arxiv.org/abs/2103.01486) | QUT | 從 NetVLAD 殘差取多尺度局部描述子做地點辨識重排序 | CVPR 2021 | 497 | [601](https://github.com/QVPR/Patch-NetVLAD) |
| 主流 | 引用、Star | 2021 | [R3LIVE](https://arxiv.org/abs/2109.07982) | HKU MaRS | LiDAR-慣性-視覺緊耦合，即時彩色地圖 | ICRA 2022 | 428 | [2,475](https://github.com/hku-mars/r3live) |
| 主流 | 引用、Star | 2022 | [Faster-LIO](https://doi.org/10.1109/LRA.2022.3152830) | HKU / Idriverplus 等 | 以平行稀疏增量體素取代 ikd-tree，LIO 更快 | RA-L 2022 | 423 | [1,645](https://github.com/gaoxiang12/faster-lio) |
| 主流 | 引用、Star、機構 | 2021 | [Kimera](https://arxiv.org/abs/2101.06894) | MIT SPARK | 從度量語意 SLAM 建出分層 3D 動態場景圖 | IJRR 2021 | 413 | [2,141](https://github.com/MIT-SPARK/Kimera) |
| 主流 | 引用、Star | 2021 | [F-LOAM](https://arxiv.org/abs/2107.00822) | NTU | 兩階段失真補償取代迭代的快速 LiDAR 里程計 | IROS 2021 | 403 | [1,145](https://github.com/wh200720041/floam) |
| 主流 | 引用 | 2021 | [PointDSC](https://arxiv.org/abs/2103.05465) | HKUST / CityU | 把空間一致性做成可學習的離群點剔除，提升特徵式點雲配準的穩健度 | CVPR 2021 | 399 | 未公開 |
| 主流 | 引用、Star | 2022 | [NeRF-SLAM](https://arxiv.org/abs/2210.13641) | MIT SPARK | 稠密單目 SLAM 提供位姿與深度不確定度即時訓練 NeRF | IROS 2023 | 397 | [1,266](https://github.com/ToniRV/NeRF-SLAM) |
| 主流 | 引用 | 2023 | [Co-SLAM](https://arxiv.org/abs/2304.14377) · [專案頁](https://hengyiwang.github.io/projects/CoSLAM) | UCL | 座標編碼與雜湊網格混合表示的神經 RGB-D SLAM | CVPR 2023 | 389 | [475](https://github.com/HengyiWang/Co-SLAM) |
| 主流 | 引用、Star、獲獎 | 2021 | [GVINS](https://arxiv.org/abs/2103.07899) | HKUST | GNSS 原始量測緊耦合視覺慣性的無漂移狀態估測 | T-RO 2022 | 386 | [1,166](https://github.com/HKUST-Aerial-Robotics/GVINS) |
| 主流 | 引用 | 2021 | [CoFiNet](https://arxiv.org/abs/2110.14076) | NUDT / TUM / Siemens | 由粗到細的對應：先在超點層級匹配再細化到點，不依賴重複性關鍵點 | NeurIPS 2021 | 376 | 未公開 |
| 主流 | 引用、獲獎 | 2022 | [Active SLAM Survey](https://arxiv.org/abs/2207.00254) | Zaragoza / MIT SPARK / UCSD 等 | 主動 SLAM 與多機器人協作探索的綜述 | T-RO 2023 | 367 | 未公開 |
| 主流 | 引用、Star | 2021 | [PixLoc](https://arxiv.org/abs/2103.09213) | ETH / Chalmers / Microsoft 等 | 對齊多尺度深度特徵的場景無關相機定位 | CVPR 2021 | 360 | [802](https://github.com/cvg/pixloc) |
| 主流 | 引用、獲獎、機構 | 2021 | [Scan Context++](https://arxiv.org/abs/2109.13494) | KAIST / NAVER LABS / SNU | 對旋轉與橫向位移穩健的 LiDAR 結構地點描述子 | T-RO 2022 | 358 | [347](https://github.com/gisbi-kim/scancontext_tro) |
| 主流 | 引用、獲獎 | 2021 | [Kimera-Multi](https://arxiv.org/abs/2106.14386) | MIT SPARK | 多機器人分散式度量-語意 SLAM | T-RO 2022 | 350 | [417](https://github.com/MIT-SPARK/Kimera-Multi) |
| 主流 | 引用、Star | 2022 | [DPVO](https://arxiv.org/abs/2208.04726) | Princeton | 稀疏 patch 的深度視覺里程計，比 DROID 輕量 | NeurIPS 2023 | 328 | [1,136](https://github.com/princeton-vl/DPVO) |
| 主流 | 引用 | 2023 | [Point-SLAM](https://arxiv.org/abs/2304.04278) | ETH / KU Leuven / Univ. of Amsterdam | 依資訊密度動態佈點的神經點雲稠密 SLAM | ICCV 2023 | 326 | [486](https://github.com/eriksandstroem/Point-SLAM) |
| 主流 | 引用 | 2023 | [MixVPR](https://arxiv.org/abs/2303.02190) | Laval | 以 MLP 特徵混合聚合全域描述子的視覺地點辨識 | WACV 2023 | 322 | [337](https://github.com/amaralibey/MixVPR) |
| 主流 | 引用、Star | 2023 | [AnyLoc](https://arxiv.org/abs/2308.00688) · [專案頁](https://anyloc.github.io/) | CMU / IIIT | 用基礎模型特徵做通用視覺地點辨識 | RA-L 2024 | 321 | [646](https://github.com/AnyLoc/AnyLoc) |
| 主流 | 引用、Star、基準 | 2021 | [M2DGR](https://arxiv.org/abs/2112.13659) | SJTU | 地面機器人多感測器多場景 SLAM 資料集 | RA-L 2022 | 318 | [1,215](https://github.com/SJTU-ViSYS/M2DGR) |
| 主流 | 引用 | 2022 | [REGTR](https://arxiv.org/abs/2203.14517) | NUS | 用 transformer 直接輸出對應點，免最近鄰匹配與 RANSAC，端到端點雲配準 | CVPR 2022 | 315 | 未公開 |
| 主流 | 引用 | 2022 | [ESLAM](https://arxiv.org/abs/2211.11704) · [專案頁](https://www.idiap.ch/paper/eslam/) | Idiap / EPFL / ams OSRAM | 多尺度軸對齊特徵平面表示 SDF 的高效稠密 SLAM | CVPR 2023 | 306 | [224](https://github.com/idiap/ESLAM) |
| 主流 | 引用、Star | 2023 | [Photo-SLAM](https://arxiv.org/abs/2311.16728) · [專案頁](https://huajianup.github.io/research/Photo-SLAM/) | HKUST / SYSU | 特徵點定位搭配超原語 Gaussian 的即時寫實建圖 | CVPR 2024 | 293 | [780](https://github.com/HuajianUP/Photo-SLAM) |
| 主流 | 引用、Star、獲獎、推薦 | 2024 | [FAST-LIVO2](https://arxiv.org/abs/2408.14035) | HKU MaRS | LiDAR-慣性-視覺直接法緊耦合里程計 | T-RO 2025 | 282 | [4,780](https://github.com/hku-mars/FAST-LIVO2) |
| 主流 | 引用、Star | 2023 | [Gaussian-SLAM](https://arxiv.org/abs/2312.10070) | Univ. of Amsterdam | 子地圖組織 3D Gaussian 的可擴展寫實 RGB-D SLAM | arXiv | 278 | [1,185](https://github.com/VladimirYugay/Gaussian-SLAM) |
| 主流 | 引用、獲獎 | 2023 | [NICER-SLAM](https://arxiv.org/abs/2302.03594) | ETH / MPI-IS / Lund 等 | 僅用 RGB 並以單目先驗監督的神經隱式稠密 SLAM | 3DV 2024 | 277 | [217](https://github.com/cvg/nicer-slam) |
| 主流 | 引用、Star | 2023 | [Point-LIO](https://doi.org/10.1002/aisy.202200459) | HKU MaRS | 逐點更新的高頻寬 LIO，可承受劇烈運動與 IMU 飽和 | Advanced Intelligent Systems 2023 | 274 | [1,360](https://github.com/hku-mars/Point-LIO) |
| 主流 | 引用、Star、獲獎 | 2024 | [MegaSaM](https://arxiv.org/abs/2412.04463) · [專案頁](https://mega-sam.github.io/) | Google DeepMind / UC Berkeley / Univ. of Michigan | 動態影片也能穩定估計相機與深度的 SLAM 系統 | CVPR 2025 | 268 | [1,367](https://github.com/mega-sam/mega-sam) |
| 主流 | 引用 | 2023 | [SALAD](https://arxiv.org/abs/2311.15937) | Zaragoza | 以最佳傳輸與 dustbin 重構 NetVLAD 聚合 | CVPR 2024 | 257 | [385](https://github.com/serizba/salad) |
| 主流 | 引用 | 2023 | [GO-SLAM](https://arxiv.org/abs/2309.02436) · [專案頁](https://youmi-zym.github.io/projects/GO-SLAM/) | Bologna | 迴環與全域 BA 即時更新神經重建的稠密 SLAM | ICCV 2023 | 255 | [442](https://github.com/youmi-zym/GO-SLAM) |
| 主流 | 引用、獲獎 | 2024 | [SLAM in Extreme Environments (SubT)](https://doi.org/10.1109/TRO.2023.3323938) | NASA JPL / CMU / ETH 等 | DARPA SubT 各隊 SLAM 系統與地下環境經驗總整理 | T-RO 2024 | 240 | 未公開 |
| 主流 | 引用、Star、獲獎 | 2023 | [MAC (Maximal Cliques)](https://arxiv.org/abs/2305.10854) | Northwestern Polytechnical | 放寬最大團限制，從相容圖中挖出多個極大團產生位姿假設，點雲配準更穩 | CVPR 2023 | 220 | [545](https://github.com/zhangxy0517/3D-Registration-with-Maximal-Cliques) |
| 主流 | 引用、Star | 2023 | [Swarm-SLAM](https://arxiv.org/abs/2301.06230) | Polytechnique Montréal | 稀疏去中心化的多機器人協作 SLAM | RA-L 2024 | 217 | [715](https://github.com/MISTLab/Swarm-SLAM) |
| 主流 | 引用、Star | 2024 | [SGS-SLAM](https://arxiv.org/abs/2402.03246) | DUT / Univ. of Tokyo / Columbia 等 | 多通道優化外觀幾何語意的 Gaussian 語意 SLAM | ECCV 2024 | 204 | [730](https://github.com/ShuhongLL/SGS-SLAM) |
| 主流 | 引用 | 2023 | [EigenPlaces](https://arxiv.org/abs/2308.10832) | PoliTo | 依主成分方向分群取多視角訓練的視角穩健 VPR | ICCV 2023 | 181 | [163](https://github.com/gmberton/EigenPlaces) |
| 主流 | 引用 | 2023 | [R2Former](https://arxiv.org/abs/2304.03410) | ByteDance / UCF | 單一 Transformer 統一檢索與重排序的地點辨識 | CVPR 2023 | 171 | [104](https://github.com/bytedance/R2Former) |
| 主流 | 引用 | 2023 | [LiDAR Odometry Survey](https://arxiv.org/abs/2312.17487) | SNU | 依感測器融合方式分類的 LiDAR 里程計綜述 | Intelligent Service Robotics 2024 | 152 | 未公開 |
| 主流 | 引用、獲獎 | 2024 | [NeRF/3DGS SLAM Survey](https://arxiv.org/abs/2402.13255) | Bologna / ETH / Univ. of Amsterdam 等 | NeRF 與 3DGS 在 SLAM 應用的綜述 | T-RO 2026 | 145 | 未公開 |
| 主流 | 引用、Star | 2024 | [GS-ICP SLAM](https://arxiv.org/abs/2403.12550) | SKKU | G-ICP 與 3DGS 共用 Gaussian 地圖的高速 SLAM | ECCV 2024 | 140 | [540](https://github.com/Lab-of-AI-and-Robotics/GS_ICP_SLAM) |
| 主流 | 引用、Star、獲獎 | 2024 | [PIN-SLAM](https://arxiv.org/abs/2401.09101) | Bonn | 點式隱式神經地圖可隨迴環彈性變形的 LiDAR SLAM | T-RO 2024 | 132 | [630](https://github.com/PRBonn/PIN_SLAM) |
| 主流 | 引用、Star、獲獎 | 2024 | [AirSLAM](https://arxiv.org/abs/2408.03520) | NTU / Univ. at Buffalo 等 | 學習式點線特徵搭配傳統後端的抗光照視覺 SLAM | T-RO 2025 | 123 | [1,211](https://github.com/sair-lab/AirSLAM) |
| 主流 | 引用 | 2024 | [Splat-SLAM](https://arxiv.org/abs/2405.16544) | Google / ETH / Univ. of Amsterdam 等 | 全域優化追蹤並隨之變形 Gaussian 地圖的純 RGB SLAM | CVPRW 2025 | 121 | [363](https://github.com/google-research/Splat-SLAM) |
| 主流 | 引用 | 2024 | [CricaVPR](https://arxiv.org/abs/2402.19231) | Tsinghua / Peng Cheng Lab / UCAS | 批次內跨影像注意力學習相關性感知的 VPR 表示 | CVPR 2024 | 116 | [173](https://github.com/Lu-Feng/CricaVPR) |
| 主流 | 引用、Star | 2024 | [DPV-SLAM](https://arxiv.org/abs/2408.01654) | Princeton | DPVO 加上迴環的單 GPU 低記憶體深度視覺 SLAM | ECCV 2024 | 115 | [1,136](https://github.com/princeton-vl/DPVO) |
| 主流 | 引用 | 2024 | [LoopSplat](https://arxiv.org/abs/2408.10154) · [專案頁](https://loopsplat.github.io/) | Stanford / Univ. of Amsterdam / ETH | 直接配準 3DGS 子地圖做迴環的 Gaussian SLAM | 3DV 2025 | 107 | [400](https://github.com/GradientSpaces/LoopSplat) |
| 主流 | 引用 | 2024 | [BoQ](https://arxiv.org/abs/2405.07364) | Laval | 以一組可學習全域查詢聚合特徵的單階段 VPR | CVPR 2024 | 106 | [195](https://github.com/amaralibey/bag-of-queries) |
| 主流 | 引用 | 2024 | [CG-SLAM](https://arxiv.org/abs/2403.16095) · [專案頁](https://zju3dv.github.io/cg-slam) | Zhejiang | 不確定度感知且幾何一致的 Gaussian 場 RGB-D SLAM | ECCV 2024 | 104 | [125](https://github.com/hjr37/CG-SLAM) |
| 主流 | 引用、Star | 2024 | [iG-LIO](https://doi.org/10.1109/LRA.2024.3349915) | Zhejiang | 增量 GICP 緊耦合 LIO，兼顧速度與精度 | RA-L 2024 | 104 | [524](https://github.com/zijiechenrobotics/ig_lio) |
| 主流 | 引用 | 2024 | [SelaVPR](https://arxiv.org/abs/2402.14505) | Tsinghua / Peng Cheng Lab / UCAS | 以輕量 adapter 做全域與局部調適的基礎模型 VPR | ICLR 2024 | 101 | [269](https://github.com/Lu-Feng/SelaVPR) |
| 主流 | 引用、Star | 2025 | [WildGS-SLAM](https://arxiv.org/abs/2504.03886) · [專案頁](https://wildgs-slam.github.io/) | ETH / Microsoft / Stanford | DINOv2 不確定度圖剔除動態物的單目 3DGS SLAM | CVPR 2025 | 100 | [658](https://github.com/GradientSpaces/WildGS-SLAM) |
| 主流 | 引用、基準 | 2024 | [MCD](https://arxiv.org/abs/2403.11496) | NTU / KTH 等 | 跨歐亞三校園多感測器且含語意標註的資料集 | CVPR 2024 | 99 | 未公開 |
| 主流 | 引用、Star、獲獎、機構 | 2024 | [Khronos](https://arxiv.org/abs/2402.13817) | MIT SPARK | 統一處理短期動態與長期變化的時空度量語意 SLAM | RSS 2024 | 99 | [547](https://github.com/MIT-SPARK/Khronos) |
| 主流 | 引用、獲獎 | 2024 | [BTC](https://doi.org/10.1109/TRO.2024.3353076) | HKU MaRS | 二值 + 三角形組合描述子的 3D LiDAR 地點辨識 | T-RO 2024 | 84 | [373](https://github.com/hku-mars/btc_descriptor) |
| 主流 | 引用 | 2025 | [MegaLoc](https://arxiv.org/abs/2502.17237) | PoliTo / Focoos AI | 合併多資料集訓練的通用影像檢索定位模型 | CVPRW 2025 | 83 | [311](https://github.com/gmberton/MegaLoc) |
| 主流 | 引用 | 2024 | [LIV-GaussMap](https://arxiv.org/abs/2401.14857) | HKUST / HKUST (GZ) 等 | LiDAR 慣性視覺融合的即時 Gaussian 輻射場建圖 | RA-L 2024 | 81 | [160](https://github.com/sheng00125/LIV-GaussMap) |
| 主流 | 引用、推薦 | 2025 | [LiDAR-IMU-Camera Fusion SLAM Review](https://doi.org/10.1007/s10462-025-11187-w) | 未確認 | LiDAR、IMU、相機融合 SLAM 的系統性綜述 | Artificial Intelligence Review 2025 | 75 | 未公開 |
| 主流 | 引用、基準 | 2025 | [TartanGround](https://arxiv.org/abs/2505.10696) · [專案頁](https://tartanair.org/tartanground) | ETH RSL / CMU 等 | 大規模模擬地面機器人感知與導航資料集 | IROS 2025 | 44 | [128](https://github.com/castacks/tartanairpy) |
| 主流 | 引用 | 2025 | [S3PO-GS](https://arxiv.org/abs/2507.03737) · [專案頁](https://3dagentworld.github.io/S3PO-GS/) | HKUST (GZ) | 以 3DGS 點圖錨定追蹤避免尺度漂移的戶外單目 SLAM | ICCV 2025 | 36 | [138](https://github.com/3DAgentWorld/S3PO-GS) |
| 主流 | 引用 | 2025 | [Adaptive-LIO](https://arxiv.org/abs/2503.05077) | 未確認 | 依環境自適應分段與地圖解析度的 LiDAR 慣性里程計 | IoT-J 2025 | 36 | [272](https://github.com/chengwei0427/Adaptive-LIO) |
| 主流 | 引用 | 2025 | [Ground-Fusion++](https://arxiv.org/abs/2507.08364) | Chongqing / Nankai / ZJUT 等 | GNSS、RGB-D、LiDAR、IMU、輪速的模組化融合 | IROS 2025 | 34 | [228](https://github.com/sjtuyinjie/Ground-Fusion2) |
| 主流 | 引用、Star | 2025 | [KISS-SLAM](https://arxiv.org/abs/2503.12660) | Bonn / Sapienza | 延續 KISS-ICP 免調參、泛化強的 LiDAR SLAM 基線 | IROS 2025 | 33 | [541](https://github.com/PRBonn/kiss-slam) |
| 主流 | 引用、Star、獲獎、機構 | 2025 | [GS-LIVO](https://arxiv.org/abs/2501.08672) | HKUST / HKU MaRS / SJTU | 可在嵌入式即時運行的 LiDAR 慣性視覺 Gaussian 建圖 | T-RO 2025 | 32 | [505](https://github.com/HKUST-Aerial-Robotics/GS-LIVO) |
| 主流 | 引用 | 2025 | [OpenGS-SLAM (outdoor)](https://arxiv.org/abs/2502.15633) | HKUST (GZ) | 點圖回歸加自適應尺度的戶外純 RGB Gaussian SLAM | ICRA 2025 | 32 | [215](https://github.com/3DAgentWorld/OpenGS-SLAM) |
| 主流 | 引用、獲獎 | 2025 | [VINGS-Mono](https://arxiv.org/abs/2501.08286) | Fudan | 視覺慣性單目 Gaussian SLAM 擴展到公里級戶外 | T-RO 2025 | 31 | [306](https://github.com/Fudan-MAGIC-Lab/VINGS-Mono) |
| 主流 | 引用、獲獎 | 2025 | [OKVIS2-X](https://arxiv.org/abs/2510.04612) | TUM | 可選配稠密深度、LiDAR 與 GNSS 的關鍵幀 VI-SLAM | T-RO 2025 | 31 | [421](https://github.com/ethz-mrl/OKVIS2-X) |
| 新興 | 獲獎 | 2021 | [CT-ICP](https://arxiv.org/abs/2109.12979) | MINES ParisTech / Kitware | 每幀以起訖兩個位姿連續插值處理掃描畸變，加上回環偵測組成完整 LiDAR SLAM | ICRA 2022 | 295 | 未公開 |
| 新興 | 獲獎、基準 | 2021 | [VIODE](https://arxiv.org/abs/2102.05965) | EPFL / Tokyo | 模擬無人機在漸增動態物體場景中的 VIO 資料集，專測動態環境穩健度 | RA-L 2021 | 63 | 未公開 |
| 新興 | 獲獎 | 2022 | [Localizability Estimation](https://arxiv.org/abs/2203.05698) | ETH RSL | 從點雲直接學習各方向的可定位性，隧道等退化場景提前偵測並調整 LiDAR 定位 | IROS 2022 | 53 | 未公開 |
| 新興 | 獲獎 | 2023 | [Multi-IMU Proprioceptive Odometry](https://doi.org/10.1109/IROS55552.2023.10342061) | CMU | 在每條小腿加裝 IMU，以 EKF 融合做低漂移的腿式本體感覺里程計 | IROS 2023 | 41 | 未公開 |
| 新興 | 獲獎 | 2022 | [EDPLVO](https://doi.org/10.1109/ICRA46639.2022.9812133) | Meituan / UNC / CMU | 把共線約束有效納入直接法，點線並用的高效直接視覺里程計 | ICRA 2022 | 40 | 未公開 |
| 新興 | 獲獎 | 2023 | [NGEL-SLAM](https://arxiv.org/abs/2311.09525) | Zhejiang | 特徵式追蹤加回環確保全域一致，多個神經隱式子地圖做低延遲稠密建圖 | ICRA 2024 | 39 | 未公開 |
| 新興 | 獲獎 | 2024 | [MAC-VO](https://arxiv.org/abs/2409.09479) | CMU / SJTU | 學出度量感知的匹配不確定性，同時用來挑關鍵點與加權位姿圖殘差 | ICRA 2025 | 33 | 未公開 |
| 新興 | 獲獎 | 2025 | [Back on Track](https://arxiv.org/abs/2504.14516) · [專案頁](https://wrchen530.github.io/projects/batrack/) | TUM / Oxford / Microsoft | 用 3D 點追蹤把動態點的運動拆成相機與物體分量，讓 BA 能直接處理動態影片 | ICCV 2025 | 26 | 未公開 |
| 新興 | 獲獎 | 2021 | [Ground Encoding](https://arxiv.org/abs/2103.15317) | CMU | 把透地雷達訊號學成因子圖量測模型，不需事前地圖或 GPS 就能定位 | IROS 2021 | 20 | 未公開 |
| 新興 | 獲獎 | 2023 | [MESA](https://arxiv.org/abs/2310.12320) | CMU | 在流形上的共識 ADMM 後端，多機器人非同步分散式最佳化 SLAM | ICRA 2024 | 20 | 未公開 |
| 新興 | 獲獎 | 2023 | [Semantic Object Map Localization](https://arxiv.org/abs/2303.04658) | MIT | 以物件語意地圖做跨視角配準，不依賴道路特徵，在非都市環境做全域定位與重定位 | IROS 2023 | 16 | 未公開 |
| 新興 | 獲獎 | 2022 | [Data-driven Event Feature Tracking](https://arxiv.org/abs/2211.12826) | UZH RPG | 第一個資料驅動的事件相機特徵追蹤器，有無影像幀都能用，自監督適應真實資料 | CVPR 2023、TPAMI 2025 | 16 | 未公開 |
| 新興 | 獲獎 | 2021 | [Unsupervised LiDAR Features](https://arxiv.org/abs/2102.11261) | University of Toronto | 在高斯變分推論框架內非監督學習 LiDAR 特徵，與軌跡估計共用單一目標 | RA-L 2021 | 16 | 未公開 |
| 新興 | 獲獎 | 2023 | [iMODE](https://doi.org/10.1109/ICRA48891.2023.10161538) | Imperial | 以稀疏 SLAM 位姿與深度監督，即時從頭訓練單目稠密語意神經場 | ICRA 2023 | 16 | 未公開 |
| 新興 | 獲獎 | 2025 | [Ground-Optimized 4D Radar-Inertial Odometry](https://arxiv.org/abs/2502.08093) | SNU | 地面最佳化的雜訊濾除，加上以高斯過程連續積分速度的雷達慣性里程計 | ICRA 2025 | 13 | 未公開 |
| 新興 | 獲獎 | 2024 | [Censible](https://doi.org/10.1109/ICRA57147.2024.10611697) | Caltech / JPL | 行星車全域定位框架，取代人工比對軌道影像 | ICRA 2024 | 13 | 未公開 |
| 新興 | 獲獎 | 2021 | [Interval-Based Visual-LiDAR Fusion](https://doi.org/10.1109/LRA.2021.3057572) | Leibniz University Hannover | 以區間分析保守建模 LiDAR 距離指派給影像特徵的不確定性 | RA-L 2021 | 12 | 未公開 |
| 新興 | 獲獎 | 2023 | [Cross-View Place Recognition](https://doi.org/10.1109/IROS55552.2023.10341898) | University of Maryland | 保留視覺、空間、幾何資訊的語意地點辨識，用於空地協同的跨視角跨模態定位 | IROS 2023 | 10 | 未公開 |
| 新興 | 獲獎 | 2024 | [Square-Root Filter VINS](https://doi.org/10.1109/ICRA57147.2024.10610916) | University of Delaware | 改用平方根共變異數濾波，在嵌入式裝置上更快且數值更穩 | ICRA 2024 | 10 | 未公開 |
| 新興 | 獲獎、推薦 | 2024 | [BAE](https://arxiv.org/abs/2409.12190) | Univ. at Buffalo / Georgia Tech / Purdue 等 | PyTorch eager 模式下的 GPU 稀疏 BA 函式庫 | T-RO 2026 | 8 | [371](https://github.com/pypose/bae) |
| 新興 | 獲獎 | 2025 | [Doppler Correspondence](https://arxiv.org/abs/2502.11461) | UNIST / KAIST | 用 4D LiDAR／雷達的 Doppler 速度直接建立對應，掃描匹配不需迭代，在隧道、惡劣天氣更穩 | RSS 2025 | 6 | 未公開 |
| 新興 | 獲獎 | 2025 | [FUSER](https://arxiv.org/abs/2512.09373) | NTU / Nanjing / Nankai / Alibaba | 一次處理所有掃描直接回歸全域位姿，免成對匹配，再以 SE(3)^N diffusion 精修 | CVPR 2026 | 6 | 未公開 |
| 新興 | 獲獎 | 2023 | [GMCR](https://arxiv.org/abs/2303.04032) | TUM / Glasgow / Radboud | 以圖式最大共識估計做點雲配準，在高離群比例下仍穩健 | ICRA 2023 | 6 | 未公開 |
| 新興 | 機構、推薦 | 2026 | [ScaRF-SLAM](https://arxiv.org/abs/2606.00307) | Oxford ORI / Georgia Tech | 定位交給傳統視覺 SLAM，feed-forward 幾何模型只做深度與稠密重建，再以跨幀與子地圖的尺度一致性最佳化串起來；單目、雙目、多相機、有無 IMU 都能套 | RA-L 2026 | 3 | [282](https://github.com/ori-drs/ScaRF-SLAM) |
| 新興 | 獲獎 | 2026 | [KISS-IMU](https://arxiv.org/abs/2603.06205) | Inha University | 不需真值的自監督慣性里程計，以運動平衡學習與不確定性感知推論提升泛化 | ICRA 2026 | 1 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [Line-Augmented cuVSLAM](https://arxiv.org/abs/2610.20958) | Analog Devices、NVIDIA | 在 NVIDIA cuVSLAM 加線特徵（Plücker 參數化、點線殘差進 Gauss-Newton 位姿解與滑窗 BA），點特徵稀少時自動加重線的權重，針對倉庫等低紋理場景 | RGB-D：TUM Freiburg3 22 條序列 ATE 降 38.5%，Replica 8 條降 30.1% | 未公開 | arXiv |
| 2026-09 | [Scal3R](https://arxiv.org/abs/2609.04201) · [專案頁](https://linjohnss.github.io/scal3r/) | NYCU / NVIDIA | 凍結 CUT3R、STream3R 骨幹，只加約 1% 參數的位姿 token 對多個過去關鍵幀並行查相對位姿，再以線上位姿圖與回環融合，長影片不再累積漂移 | KITTI 平均 ATE 比線上基線降 60% 以上；回環示範 ATE 49.8 m → 6.4 m | [GitHub](https://github.com/NVlabs/scal3r) | ECCV 2026 |
| 2026-09 | [FFVO](https://arxiv.org/abs/2609.13733) | Waymo / UW | feed-forward 位姿解碼器做長距離 VO |  | 未公開 | arXiv |
| 2026-04 | [BIEVR-LIO](https://arxiv.org/abs/2604.14421) | ETH ASL / RSL | 幾何資訊貧乏場景，用 bump image 強化 voxel map，不需額外感測器 |  | [GitHub](https://github.com/ethz-asl/BIEVR-LIO) | arXiv |
| 2026-01 | [VGGT-SLAM 2.0](https://arxiv.org/abs/2601.19887) | MIT SPARK | 新 factor graph 設計消除子地圖對齊的 15-DoF 漂移與平面退化；直接用 VGGT attention 層驗證回環，不需額外訓練 | TUM 位姿誤差比 VGGT-SLAM 低約 23%；Jetson Thor 地面機器人即時運行 | [GitHub](https://github.com/MIT-SPARK/VGGT-SLAM) | RSS 2026 |

## 3D 場景重建（feed-forward、SfM、3DGS／NeRF）

### 在解決的問題

- feed-forward 重建：不跑 SfM 優化，一次前向得到相機與幾何；挑戰在大規模與串流輸入。
- 傳統 SfM 的速度與穩健度：全域最佳化、位姿圖初始化。
- 3D 表示：3DGS 取代 NeRF，可即時渲染；表面品質與無位姿輸入仍在改進。
- 動態場景：同時重建幾何、運動與相機。

### 重要論文（資料日期 2026-10-20）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、Star、HF | 2023 | [3D Gaussian Splatting](https://arxiv.org/abs/2308.04079) · [專案頁](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) | Inria | 即時可微分高斯渲染，取代 NeRF 成為主流 3D 表示 | SIGGRAPH 2023 | 10,958 | [24,271](https://github.com/graphdeco-inria/gaussian-splatting) |
| 奠基 | 引用、Star | 2022 | [Instant-NGP](https://arxiv.org/abs/2201.05989) · [專案頁](https://nvlabs.github.io/instant-ngp) | NVIDIA | 多解析度雜湊編碼，秒級訓練 NeRF | SIGGRAPH 2022 | 6,480 | [17,578](https://github.com/NVlabs/instant-ngp) |
| 奠基 | 引用、Star | 2023 | [DUSt3R](https://arxiv.org/abs/2312.14132) | Naver Labs | 免相機參數直接回歸 pointmap 的 3D 重建 | CVPR 2024 | 2,048 | [7,348](https://github.com/naver/dust3r) |
| 奠基 | 引用、Star、HF、獲獎 | 2025 | [VGGT](https://arxiv.org/abs/2503.11651) · [專案頁](https://vgg-t.github.io/) | Oxford VGG / Meta | 單次前向同時估相機、深度、點圖、追蹤 | CVPR 2025 | 2,033 | [14,535](https://github.com/facebookresearch/vggt) |
| 奠基 | 引用、Star、HF | 2024 | [2D Gaussian Splatting](https://arxiv.org/abs/2403.17888) · [專案頁](https://surfsplatting.github.io) | ShanghaiTech / Tübingen | 幾何準確的表面重建，可輸出網格 | SIGGRAPH 2024 | 1,728 | [3,314](https://github.com/hbb1/2d-gaussian-splatting) |
| 奠基 | 引用、Star | 2024 | [MASt3R](https://arxiv.org/abs/2406.09756) | Naver Labs | DUSt3R 加特徵匹配頭，提升匹配與定位 | ECCV 2024 | 1,259 | [3,134](https://github.com/naver/mast3r) |
| 奠基 | 引用、Star | 2023 | [Nerfstudio](https://arxiv.org/abs/2302.04264) · [專案頁](https://nerf.studio) | UC Berkeley | 模組化 NeRF／3DGS 重建框架 | SIGGRAPH 2023 | 1,073 | [12,085](https://github.com/nerfstudio-project/nerfstudio) |
| 奠基 | 引用、Star、HF | 2023 | [SuGaR](https://arxiv.org/abs/2311.12775) · [專案頁](https://anttwo.github.io/sugar/) | ENPC | 從 3DGS 抽出可編輯網格 | CVPR 2024 | 988 | [3,539](https://github.com/Anttwo/SuGaR) |
| 奠基 | 引用、基準 | 2023 | [ScanNet++](https://arxiv.org/abs/2308.11417) · [專案頁](https://cy94.github.io/scannetpp/) | TUM | 雷射掃描＋單眼相機＋iPhone 的高精度室內資料集 | ICCV 2023 | 963 | [412](https://github.com/scannetpp/scannetpp) |
| 奠基 | 引用、Star、獲獎 | 2023 | [pixelSplat](https://arxiv.org/abs/2312.12337) · [專案頁](https://dcharatan.github.io/pixelsplat) | MIT / Simon Fraser / Univ. of Toronto | 由兩張影像前向預測 3D 高斯的通用重建 | CVPR 2024 | 863 | [1,285](https://github.com/dcharatan/pixelsplat) |
| 奠基 | 引用、Star | 2024 | [MVSplat](https://arxiv.org/abs/2403.14627) · [專案頁](https://donydchen.github.io/mvsplat) | Monash / ETH / Univ. of Tübingen 等 | 以平面掃描代價體定位高斯中心的稀疏視角 3DGS | ECCV 2024 | 672 | [1,316](https://github.com/donydchen/mvsplat) |
| 奠基 | 引用、Star | 2025 | [CUT3R](https://arxiv.org/abs/2501.12387) · [專案頁](https://cut3r.github.io/) | UC Berkeley / Google | 持續狀態更新的串流 3D 重建 | CVPR 2025 | 645 | [1,512](https://github.com/CUT3R/CUT3R) |
| 奠基 | 引用、Star、HF | 2024 | [MonST3R](https://arxiv.org/abs/2410.03825) · [專案頁](https://monst3r-project.github.io/) | UC Berkeley / Google DeepMind / Stability AI 等 | 逐幀 pointmap 推廣到動態場景的幾何估計 | ICLR 2025 | 499 | [1,390](https://github.com/Junyi42/monst3r) |
| 奠基 | 引用 | 2024 | [PGSR](https://arxiv.org/abs/2406.06521) · [專案頁](https://zju3dv.github.io/pgsr/) | Zhejiang / SenseTime | 把高斯壓成平面並加多視角幾何約束，3DGS 得到高精度表面且保留快速訓練 | TVCG 2024 | 446 | 未公開 |
| 奠基 | 引用、Star | 2025 | [Fast3R](https://arxiv.org/abs/2501.13928) · [專案頁](https://fast3r-3d.github.io/) | Meta / Univ. of Michigan | 單次前向處理上千張影像，免兩兩配對 | CVPR 2025 | 445 | [1,592](https://github.com/facebookresearch/fast3r) |
| 奠基 | 引用、Star | 2024 | [gsplat](https://arxiv.org/abs/2409.06765) · [專案頁](https://docs.gsplat.studio/) | UC Berkeley | 開源 CUDA 高斯潑濺函式庫 | JMLR 2025 | 408 | [5,811](https://github.com/nerfstudio-project/gsplat) |
| 奠基 | 引用 | 2024 | [3DGS Survey](https://arxiv.org/abs/2401.03890) | Zhejiang | 系統整理 3DGS 技術並附統一效能比較 | ACM Computing Surveys | 387 | [114](https://github.com/guikunchen/Awesome3DGS) |
| 奠基 | 引用、Star | 2025 | [MapAnything](https://arxiv.org/abs/2509.13414) · [專案頁](https://map-anything.github.io/) | Meta / CMU | 可接受多種輸入（內參、位姿、深度）的通用 feed-forward 重建 | 3DV 2026 | 383 | [3,836](https://github.com/facebookresearch/map-anything) |
| 奠基 | 引用、Star、HF | 2025 | [π³](https://arxiv.org/abs/2507.13347) · [專案頁](https://yyfz.github.io/pi3/) | Shanghai AI Lab 等 | 無參考視角的置換等變 feed-forward 重建 | arXiv | 356 | [2,220](https://github.com/yyfz/Pi3) |
| 奠基 | 引用、Star | 2024 | [DepthSplat](https://arxiv.org/abs/2410.13862) · [專案頁](https://haofeixu.github.io/depthsplat/) | ETH / Univ. of Tübingen / Univ. of Bonn 等 | 單眼深度特徵與前向 3DGS 結合並互相增益 | CVPR 2025 | 348 | [1,268](https://github.com/cvg/depthsplat) |
| 奠基 | 引用、Star、HF、獲獎 | 2025 | [SAM 3D](https://arxiv.org/abs/2511.16624) · [專案頁](https://ai.meta.com/sam3d/) | Meta | 單張自然影像重建物體幾何、紋理與擺放 | arXiv | 313 | [7,545](https://github.com/facebookresearch/sam-3d-objects) |
| 奠基 | 引用、Star、HF | 2025 | [AnySplat](https://arxiv.org/abs/2505.23716) · [專案頁](https://city-super.github.io/anysplat/) | USTC / Shanghai AI Lab | 無校正多視角一次前向輸出 3DGS 與相機參數 | SIGGRAPH Asia 2025 | 297 | [958](https://github.com/InternRobotics/AnySplat) |
| 奠基 | 引用、Star | 2025 | [FLARE](https://arxiv.org/abs/2502.12138) · [專案頁](https://zhanghe3z.github.io/FLARE/) | Zhejiang / Ant Group / Oxford 等 | 先估相機再推幾何與外觀的級聯 feed-forward 模型 | CVPR 2025 | 213 | [728](https://github.com/ant-research/FLARE) |
| 奠基 | 引用、Star | 2025 | [StreamVGGT](https://arxiv.org/abs/2507.11539) · [專案頁](https://wzzheng.net/StreamVGGT/) | Tsinghua | 因果注意力與快取把 VGGT 改成串流 4D 重建 | arXiv | 176 | [986](https://github.com/wzzheng/StreamVGGT) |
| 奠基 | 引用 | 2025 | [MUSt3R](https://arxiv.org/abs/2503.01661) | Naver Labs Europe | DUSt3R 擴展為多視角對稱架構並加入記憶機制 | CVPR 2025 | 174 | [344](https://github.com/naver/must3r) |
| 奠基 | 引用、Star | 2025 | [TTT3R](https://arxiv.org/abs/2509.26645) · [專案頁](https://rover-xingyu.github.io/TTT3R/) | Zhejiang / Westlake / Univ. of Tübingen | 把記憶更新視為測試期訓練，免重訓延長序列長度 | ICLR 2026 | 148 | [735](https://github.com/Inception3D/TTT3R) |
| 奠基 | Star、HF、推薦 | 2026 | [LingBot-Map](https://arxiv.org/abs/2604.14141) · [專案頁](https://technology.robbyant.com/lingbot-map) | Robbyant (Ant Group) | 借鏡 SLAM 設計錨點與軌跡記憶的串流重建 | arXiv | 47 | [18,154](https://github.com/robbyant/lingbot-map) |
| 主流 | 引用、Star、獲獎、基準 | 2021 | [CO3D](https://arxiv.org/abs/2109.00512) | Meta / UCL | 大規模真實物件多視角影片資料集，含相機位姿與點雲，用於類別級 3D 重建評估 | ICCV 2021 | 796 | [1,185](https://github.com/facebookresearch/co3d) |
| 主流 | 引用、Star | 2021 | [PoinTr](https://arxiv.org/abs/2108.08839) | Tsinghua | 把點雲補全改成集合到集合的翻譯，以幾何感知 transformer 由殘缺點雲生成缺漏部分 | ICCV 2021 | 684 | [868](https://github.com/yuxumin/PoinTr) |
| 主流 | 引用、Star、獲獎 | 2021 | [NeuralRecon](https://arxiv.org/abs/2104.00681) · [專案頁](https://zju3dv.github.io/neuralrecon/) | Zhejiang / SenseTime | 直接增量重建 TSDF，不再逐幀估深度後融合 | CVPR 2021 | 405 | [2,289](https://github.com/zju3dv/NeuralRecon) |
| 主流 | 引用 | 2021 | [SnowflakeNet](https://arxiv.org/abs/2108.04444) | Tsinghua / JD.com 等 | 以雪花式點反卷積逐步分裂點，skip-transformer 保留局部結構，補全細節更清楚 | ICCV 2021 | 369 | 未公開 |
| 主流 | 引用、Star | 2021 | [Shape As Points](https://arxiv.org/abs/2106.03452) · [專案頁](https://pengsongyou.github.io/sap) | MPI-IS / ETH / Tübingen 等 | 可微分 Poisson 求解器把點雲轉成隱式表面，比神經隱式表示快且可端到端最佳化 | NeurIPS 2021 | 313 | [643](https://github.com/autonomousvision/shape_as_points) |
| 主流 | 引用、Star、獲獎 | 2024 | [Spann3R](https://arxiv.org/abs/2408.16061) · [專案頁](https://hengyiwang.github.io/projects/spanner) | UCL | 以空間記憶逐幀增量回歸 pointmap，免全域對齊 | 3DV 2025 | 310 | [1,145](https://github.com/hengyiwang/spann3r) |
| 主流 | 引用、Star、獲獎 | 2021 | [PixSfM](https://arxiv.org/abs/2108.08291) | ETH / Microsoft | 以深度特徵度量精修關鍵點與 BA，提升 SfM 精度 | ICCV 2021 | 303 | [1,494](https://github.com/cvg/pixel-perfect-sfm) |
| 主流 | 引用、Star、獲獎 | 2024 | [NoPoSplat](https://arxiv.org/abs/2410.24207) · [專案頁](https://noposplat.github.io/) | ETH / NVIDIA / Microsoft 等 | 免相機位姿、直接在標準空間預測 3D 高斯 | ICLR 2025 | 295 | [1,003](https://github.com/cvg/NoPoSplat) |
| 主流 | 引用、Star | 2023 | [VGGSfM](https://arxiv.org/abs/2312.04563) · [專案頁](https://vggsfm.github.io/) | Oxford VGG / Meta | 全流程可微分的深度 SfM，取代增量式配對與三角化 | CVPR 2024 | 289 | [1,429](https://github.com/facebookresearch/vggsfm) |
| 主流 | 引用、Star | 2024 | [DN-Splatter](https://arxiv.org/abs/2403.17822) | ETH / Tampere / Aalto 等 | 以深度與法向量先驗約束 3DGS 並直接抽網格 | WACV 2025 | 217 | [847](https://github.com/maturk/dn-splatter) |
| 主流 | 引用、Star | 2024 | [3DGRT](https://arxiv.org/abs/2407.07090) · [專案頁](https://gaussiantracer.github.io/) | NVIDIA / Univ. of Toronto | 以 GPU 光線追蹤取代光柵化渲染 3D 高斯粒子 | SIGGRAPH Asia 2024 | 205 | [2,463](https://github.com/nv-tlabs/3dgrut) |
| 主流 | 引用、Star、獲獎 | 2024 | [MASt3R-SfM](https://arxiv.org/abs/2409.19152) | Naver Labs Europe | 以 MASt3R 匹配與檢索建構免調參的全整合 SfM | 3DV 2025 | 202 | [3,134](https://github.com/naver/mast3r) |
| 主流 | 引用、Star | 2023 | [AdaPoinTr](https://arxiv.org/abs/2301.04545) | Tsinghua | PoinTr 加自適應查詢與去噪任務，補全更快更準，並延伸到場景級補全 | TPAMI 2023 | 192 | [868](https://github.com/yuxumin/PoinTr) |
| 主流 | 引用、Star | 2024 | [MV-DUSt3R+](https://arxiv.org/abs/2412.06974) | Meta / UIUC | 單階段多視角同時重建，免兩兩配對後全域對齊 | CVPR 2025 | 173 | [606](https://github.com/facebookresearch/mvdust3r) |
| 主流 | 引用、Star、推薦 | 2023 | [NKSR](https://arxiv.org/abs/2305.19590) · [專案頁](https://research.nvidia.com/labs/toronto-ai/NKSR/) | NVIDIA | 以神經核場從帶雜訊的大規模點雲重建表面，稀疏體素加梯度擬合，可一次處理整個場景並泛化到未見過的資料 | CVPR 2023 | 156 | [1,002](https://github.com/nv-tlabs/nksr) |
| 主流 | 引用、Star | 2024 | [SLAM3R](https://arxiv.org/abs/2412.09401) | PKU / HKU / Aalto 等 | 前饋點圖回歸逐窗重建的即時單目稠密重建 | CVPR 2025 | 137 | [1,380](https://github.com/PKU-VCL-3DV/SLAM3R) |
| 主流 | 引用、Star | 2024 | [3DGUT](https://arxiv.org/abs/2412.12507) · [專案頁](https://research.nvidia.com/labs/toronto-ai/3DGUT) | NVIDIA / Univ. of Toronto | 以無跡變換投影高斯，支援畸變相機與二次光線 | CVPR 2025 | 122 | [2,463](https://github.com/nv-tlabs/3dgrut) |
| 主流 | 引用、Star | 2025 | [SpatialTrackerV2](https://arxiv.org/abs/2507.12462) · [專案頁](https://spatialtracker.github.io) | Zhejiang / Oxford / Ant Group 等 | 統一點追蹤、深度與相機運動的前向 3D 追蹤 | ICCV 2025 | 103 | [1,005](https://github.com/henry123-boy/SpaTrackerV2) |
| 主流 | Star、推薦 | 2023 | [nvblox](https://arxiv.org/abs/2311.00626) | NVIDIA / ETH | GPU 加速的增量式 TSDF／ESDF 建圖，即時產出供路徑規劃用的距離場 | ICRA 2024 | 98 | [1,324](https://github.com/nvidia-isaac/nvblox) |
| 主流 | 引用 | 2025 | [Point3R](https://arxiv.org/abs/2507.02863) · [專案頁](https://ykiwu.github.io/Point3R/) | Tsinghua | 以綁定 3D 位置的顯式指標記憶做串流重建 | NeurIPS 2025 | 95 | [201](https://github.com/YkiWu/Point3R) |
| 主流 | 引用、HF | 2025 | [STream3R](https://arxiv.org/abs/2508.10893) · [專案頁](https://nirvanalan.github.io/projects/stream3r/) | NTU / Shanghai AI Lab | 以因果 Transformer 串流預測 pointmap | ICLR 2026 | 89 | [412](https://github.com/NIRVANALAN/STream3R) |
| 主流 | 引用、獲獎 | 2025 | [RayZer](https://arxiv.org/abs/2505.00702) | UT Austin / Adobe / Cornell 等 | 完全不用位姿或 3D 標註，自我預測相機後渲染新視角做自監督，訓練出大型視角合成模型 | ICCV 2025 | 84 | 未公開 |
| 主流 | 引用 | 2025 | [Pow3R](https://arxiv.org/abs/2503.17316) | Naver Labs / UCL | 可選擇輸入內參、位姿、深度先驗的前向重建 | CVPR 2025 | 81 | [244](https://github.com/naver/pow3r) |
| 主流 | 引用、Star | 2025 | [WorldMirror](https://arxiv.org/abs/2510.10726) · [專案頁](https://3d-models.hunyuan.tencent.com/world/) | Tencent / CUHK / Zhejiang | 可注入任意幾何先驗並同時輸出多種 3D 表示 | ICML 2026 | 77 | [1,214](https://github.com/Tencent-Hunyuan/HunyuanWorld-Mirror) |
| 主流 | 引用、HF、獲獎、推薦 | 2025 | [D4RT](https://arxiv.org/abs/2512.08924) · [專案頁](https://d4rt-paper.github.io/) | Google DeepMind / UCL / Oxford | 單一 transformer 從影片同時推深度、時空對應與相機參數，用逐點查詢取代逐幀稠密解碼，動態場景 4D 重建又快又輕 | CVPR 2026 | 65 | 未公開 |
| 主流 | 引用 | 2025 | [LONG3R](https://arxiv.org/abs/2507.18255) · [專案頁](https://zgchen33.github.io/LONG3R/) | Shanghai AI Lab / Tsinghua / Shanghai Qi Zhi | 記憶閘控與雙源注意力支撐長序列串流重建 | ICCV 2025 | 55 | [45](https://github.com/zgchen33/LONG3R) |
| 主流 | 引用 | 2025 | [Light3R-SfM](https://arxiv.org/abs/2501.14914) | NVIDIA / Vector Institute / Univ. of Toronto | 以可學習潛在全域對齊取代 BA 的前向 SfM | CVPR 2025 | 53 | 未公開 |
| 主流 | 引用 | 2025 | [Dynamic Point Maps](https://arxiv.org/abs/2503.16318) · [專案頁](https://www.robots.ox.ac.uk/~vgg/research/dynamic-point-maps/) | Oxford VGG | 把 DUSt3R 的點圖擴展為帶時間的動態點圖，一次得到動態場景的幾何與運動 | ICCV 2025 | 53 | 未公開 |
| 主流 | 引用 | 2025 | [SuperPC](https://arxiv.org/abs/2503.14558) | University at Buffalo | 單一 diffusion 模型同時處理點雲補全、上採樣、去噪與上色，避免各任務串接誤差 | CVPR 2025 | 30 | 未公開 |
| 新興 | 獲獎 | 2021 | [Learning to Solve Hard Minimal Problems](https://arxiv.org/abs/2112.03424) | Georgia Tech / CTU Prague | 學習挑選起始問題解對做同倫延拓，只算出需要的那個解，大幅加速難的最小問題求解 | CVPR 2022 | 42 | 未公開 |
| 新興 | 獲獎 | 2026 | [VGGT-Ω](https://arxiv.org/abs/2605.15195) | Meta / Oxford VGG | 驗證 feed-forward 重建品質隨模型與資料規模可預測地提升，並擴展到動態場景 | CVPR 2026 | 18 | 未公開 |
| 新興 | 獲獎 | 2025 | [FastMap](https://arxiv.org/abs/2505.04612) · [專案頁](https://jiahao.ai/fastmap) | TTIC / Toyota Research Institute | 只用一階最佳化的全域 SfM，GPU 上比 COLMAP、GLOMAP 快約 10 倍、位姿精度相當 | 3DV 2026 | 7 | 未公開 |
| 新興 | 獲獎 | 2025 | [Anisotropic Rotation Averaging](https://arxiv.org/abs/2503.07353) | Lund / Chalmers | 把量測的各向異性不確定性放進旋轉平均，並給出可驗證全域最優的鬆弛解 | ICCV 2025 | 3 | 未公開 |
| 新興 | 獲獎 | 2026 | [LSRM](https://arxiv.org/abs/2604.05182) | Meta Reality Labs | 大幅擴大 transformer 上下文中的物件與影像 token，讓 feed-forward 物件重建逼近稠密最佳化品質 | ECCV 2026 | 3 | 未公開 |
| 新興 | 獲獎 | 2026 | [Global-Aware Edge Prioritization](https://arxiv.org/abs/2602.21963) | CTU Prague / ETH | SfM 位姿圖初始化時考慮全域一致性來挑選候選邊，取代只看 kNN 檢索 | CVPR 2026 | 1 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-04 | [Feed-forward 3D scene modeling survey](https://arxiv.org/abs/2604.14025) · [專案頁](https://ff3d-survey.github.io) | Zhejiang / NTU / Monash / ETH / Tübingen | feed-forward 3D 重建綜述，涵蓋 Point3R、IncVGGT、ZipMap 等串流／增量版本 |  | [GitHub](https://github.com/ziplab/Awesome-Feed-Forward-3D) | arXiv |
| 2026-02 | [VGG-T³](https://arxiv.org/abs/2602.23361) · [專案頁](https://research.nvidia.com/labs/dvl/projects/vgg-ttt) | NVIDIA / Toronto | 大規模離線 feed-forward 重建 |  | [GitHub](https://github.com/nv-dvl/vgg-ttt) | CVPR 2026 |
| 2025-11 | [AMB3R](https://arxiv.org/abs/2511.20343) · [專案頁](https://hengyiwang.github.io/projects/amber) | UCL | feed-forward 公制尺度重建 + 稀疏體素後端，不微調即可延伸到 VO／SLAM |  | [GitHub](https://github.com/HengyiWang/amb3r) | CVPR 2026 |

## 深度估計與 occupancy

### 在解決的問題

- 單眼公制深度：要有絕對尺度，且相機內參常未知。
- 雙目深度的零樣本泛化。
- 透明、反光表面讓深度感測器失效。
- occupancy：多源自自駕，室內與開放詞彙版本正在補上。

### 重要論文（資料日期 2026-10-20）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、Star | 2021 | [DPT](https://arxiv.org/abs/2103.13413) | Intel | ViT 做稠密預測，後續單眼深度模型的骨幹設計 | ICCV 2021 | 3,182 | [2,330](https://github.com/isl-org/DPT) |
| 奠基 | 引用、Star、HF | 2024 | [Depth Anything V2](https://arxiv.org/abs/2406.09414) · [專案頁](https://depth-anything-v2.github.io) | HKU / TikTok | 以合成資料標註提升細節的深度模型 | NeurIPS 2024 | 2,394 | [8,999](https://github.com/DepthAnything/Depth-Anything-V2) |
| 奠基 | 引用、Star、HF | 2024 | [Depth Anything](https://arxiv.org/abs/2401.10891) · [專案頁](https://depth-anything.github.io) | HKU / TikTok | 大規模未標註資料訓練的單眼深度基礎模型 | CVPR 2024 | 2,243 | [8,241](https://github.com/LiheYoung/Depth-Anything) |
| 奠基 | 引用、Star | 2023 | [ZoeDepth](https://arxiv.org/abs/2302.12288) | Intel | 相對深度預訓練 + 公制深度頭，零樣本公制深度 | arXiv | 1,065 | [2,836](https://github.com/isl-org/ZoeDepth) |
| 奠基 | 引用、Star、HF、推薦 | 2025 | [Depth Anything 3](https://arxiv.org/abs/2511.10647) · [專案頁](https://depth-anything-3.github.io/) | ByteDance Seed | 任意視角數的深度與位姿估計 | arXiv | 840 | [6,528](https://github.com/ByteDance-Seed/Depth-Anything-3) |
| 奠基 | 引用、Star、HF | 2024 | [Depth Pro](https://arxiv.org/abs/2410.02073) | Apple | 免相機內參、一秒內輸出銳利邊緣的公制深度 | ICLR 2025 | 603 | [5,757](https://github.com/apple/ml-depth-pro) |
| 奠基 | 引用、Star | 2024 | [Metric3D v2](https://arxiv.org/abs/2404.15506) · [專案頁](https://JUGGHM.github.io/Metric3Dv2) | HKUST 等 | 零樣本公制深度與法向量 | TPAMI 2024 | 590 | [2,330](https://github.com/YvanYin/Metric3D) |
| 奠基 | 引用、Star | 2024 | [UniDepth](https://arxiv.org/abs/2403.18913) | ETH | 同時估計相機內參的通用公制深度 | CVPR 2024 | 529 | [1,273](https://github.com/lpiccinelli-eth/UniDepth) |
| 奠基 | 引用、Star | 2024 | [MoGe](https://arxiv.org/abs/2410.19115) · [專案頁](https://wangrc.site/MoGePage/) | Microsoft | 單張影像估計仿射不變點雲 | CVPR 2025 | 375 | [3,071](https://github.com/microsoft/MoGe) |
| 奠基 | 引用、Star | 2024 | [GeoWizard](https://arxiv.org/abs/2403.12013) · [專案頁](https://fuxiao0719.github.io/projects/geowizard/) | CUHK / Univ. of Adelaide / HKUST 等 | 用擴散先驗聯合估計深度與法向量 | ECCV 2024 | 349 | [943](https://github.com/fuxiao0719/GeoWizard) |
| 奠基 | 獲獎 | 2020 | [LeReS](https://arxiv.org/abs/2012.09365) | Adelaide / Adobe | 先估到尺度與平移未定的深度，再以點雲網路補回位移與焦距，從單張影像還原 3D 場景形狀 | CVPR 2021 | 340 | 未公開 |
| 奠基 | 引用、Star、獲獎 | 2025 | [FoundationStereo](https://arxiv.org/abs/2501.09898) · [專案頁](https://nvlabs.github.io/FoundationStereo/) | NVIDIA | 零樣本雙目深度基礎模型 | CVPR 2025 | 317 | [2,957](https://github.com/NVlabs/FoundationStereo) |
| 奠基 | 引用、Star、HF | 2025 | [Video Depth Anything](https://arxiv.org/abs/2501.12375) · [專案頁](https://videodepthanything.github.io) | ByteDance | 時序頭加一致性損失，超長影片保持深度穩定 | CVPR 2025 | 283 | [2,278](https://github.com/DepthAnything/Video-Depth-Anything) |
| 奠基 | 引用、Star | 2025 | [UniDepthV2](https://arxiv.org/abs/2502.20110) | ETH / Toyota Motor Europe / INSAIT | 同時估計相機與深度的通用公制深度簡化版 | TPAMI 2026 | 236 | [1,273](https://github.com/lpiccinelli-eth/unidepth) |
| 主流 | 引用、Star | 2021 | [RAFT-Stereo](https://arxiv.org/abs/2109.07547) | Princeton | 迭代更新的雙目深度估計 | 3DV 2021 | 754 | [1,134](https://github.com/princeton-vl/RAFT-Stereo) |
| 主流 | 引用、Star | 2023 | [Metric3D](https://arxiv.org/abs/2307.10984) | DJI / Tencent / Zhejiang 等 | 正規相機空間轉換解決焦距歧義的零樣本公制深度 | ICCV 2023 | 517 | [2,330](https://github.com/YvanYin/Metric3D) |
| 主流 | 引用、Star | 2023 | [Marigold](https://arxiv.org/abs/2312.02145) · [專案頁](https://marigoldmonodepth.github.io) | ETH | 把影像 diffusion 模型轉成深度估計器 | CVPR 2024 | 516 | [3,243](https://github.com/prs-eth/Marigold) |
| 主流 | 引用、Star | 2023 | [IGEV-Stereo](https://arxiv.org/abs/2303.06615) | HUST | 以幾何編碼體積取代全配對相關性做迭代雙目匹配 | CVPR 2023 | 444 | [693](https://github.com/gangweix/IGEV) |
| 主流 | 引用、Star | 2022 | [UniMatch](https://arxiv.org/abs/2211.05783) · [專案頁](https://haofeixu.github.io/unimatch) | ETH / Univ. of Tübingen / Univ. of Sydney 等 | 光流、雙目、深度統一為稠密匹配的單一模型 | TPAMI 2023 | 438 | [1,384](https://github.com/autonomousvision/unimatch) |
| 主流 | 引用、Star | 2022 | [CREStereo](https://arxiv.org/abs/2203.11483) | Megvii / Tencent 等 | 階層式遞迴網路搭配自適應相關，適用實拍雙目 | CVPR 2022 | 430 | [638](https://github.com/megvii-research/CREStereo) |
| 主流 | 引用、Star | 2023 | [MiDaS v3.1](https://arxiv.org/abs/2307.14460) | Intel | 多種 Transformer 骨幹的相對深度模型庫 | arXiv | 300 | [5,418](https://github.com/isl-org/MiDaS) |
| 主流 | 引用、Star、HF | 2024 | [DepthCrafter](https://arxiv.org/abs/2409.02095) · [專案頁](https://depthcrafter.github.io) | Tencent / HKUST | 以影片擴散模型生成時序一致的長影片深度 | CVPR 2025 | 244 | [1,593](https://github.com/Tencent/DepthCrafter) |
| 主流 | 引用 | 2024 | [IGEV++](https://arxiv.org/abs/2409.00638) | HUST | 多範圍幾何編碼體積處理大視差與病態區域 | TPAMI 2025 | 129 | [328](https://github.com/gangweix/igev-plusplus) |
| 主流 | 引用、Star | 2024 | [PromptDA](https://arxiv.org/abs/2412.14015) · [專案頁](https://PromptDA.github.io/) | Zhejiang / ByteDance Seed / SJTU 等 | 以低解析 LiDAR 當提示，輸出 4K 公制深度 | CVPR 2025 | 113 | [1,175](https://github.com/DepthAnything/PromptDA) |
| 主流 | 引用 | 2025 | [DEFOM-Stereo](https://arxiv.org/abs/2501.09466) · [專案頁](https://insta360-research-team.github.io/DEFOM-Stereo/) | Insta360 / CUHK-Shenzhen | 把深度基礎模型嵌入遞迴雙目匹配框架 | CVPR 2025 | 103 | [306](https://github.com/Insta360-Research-Team/DEFOM-Stereo) |
| 主流 | 引用、Star | 2025 | [UniK3D](https://arxiv.org/abs/2503.16591) | ETH / Toyota Motor Europe / INSAIT | 以球面光線表示支援任意相機模型的單眼 3D | CVPR 2025 | 82 | [756](https://github.com/lpiccinelli-eth/UniK3D) |
| 主流 | 引用 | 2025 | [Depth Any Camera](https://arxiv.org/abs/2501.02464) · [專案頁](https://yuliangguo.github.io/depth-any-camera) | Bosch / CMU / Simon Fraser 等 | 透視相機訓練即可泛化到魚眼與 360 度公制深度 | CVPR 2025 | 57 | [361](https://github.com/yuliangguo/depth_any_camera) |
| 主流 | 引用、Star | 2025 | [Fast-FoundationStereo](https://arxiv.org/abs/2512.11130) · [專案頁](https://nvlabs.github.io/Fast-FoundationStereo/) | NVIDIA | 蒸餾加架構搜尋，首次即時零樣本雙目匹配 | arXiv | 50 | [1,545](https://github.com/NVlabs/Fast-FoundationStereo) |
| 主流 | 引用、Star | 2025 | [Prior Depth Anything](https://arxiv.org/abs/2505.10565) · [專案頁](https://prior-depth-anything.github.io/) | Zhejiang / HKU | 融合任意稀疏公制先驗與相對深度預測補全深度 | arXiv | 50 | [533](https://github.com/SpatialVision/Prior-Depth-Anything) |
| 主流 | Star、HF、推薦 | 2026 | [LingBot-Depth](https://arxiv.org/abs/2601.17895) · [專案頁](https://technology.robbyant.com/lingbot-depth) | Robbyant (Ant Group) | 把感測器深度缺陷當遮罩訊號做深度補全 | arXiv | 39 | [1,680](https://github.com/Robbyant/lingbot-depth) |
| 主流 | 引用、推薦 | 2025 | [MVSAnywhere](https://arxiv.org/abs/2503.22430) · [專案頁](https://nianticlabs.github.io/mvsanywhere/) | Niantic / Univ. of Zaragoza / UCL 等 | 可變視角數並自估深度範圍的零樣本多視角立體 | CVPR 2025 | 37 | [341](https://github.com/nianticlabs/mvsanywhere) |
| 主流 | 引用 | 2025 | [MonSter++](https://arxiv.org/abs/2501.08643) | HUST | 單眼深度先驗雙分支融合，統一雙目與多視角立體 | TPAMI 2026 | 37 | 未公開 |
| 主流 | 引用 | 2025 | [EmbodiedOcc++](https://arxiv.org/abs/2504.09540) | PKU | 平面正則與不確定性取樣改進室內高斯佔據預測 | ACM MM 2025 | 34 | [33](https://github.com/PKUHaoWang/EmbodiedOcc2) |
| 新興 | 獲獎 | 2021 | [Binary TTC](https://arxiv.org/abs/2101.04777) | NVIDIA / UCSB | 把碰撞時間估計改成逐像素二元分類（是否在時限內碰撞），單目、免校正即可當時間柵欄 | CVPR 2021 | 40 | 未公開 |
| 新興 | 獲獎 | 2021 | [Neural Disparity Refinement](https://arxiv.org/abs/2110.15367) · [專案頁](https://cvlab-unibo.github.io/neural-disparity-refinement-web) | Bologna | 連續式視差精修網路，可輸出任意解析度，適合手機上高低解析度不對稱的雙目 | 3DV 2021 | 34 | 未公開 |
| 新興 | 獲獎 | 2025 | [Zero-Shot Scene Flow](https://arxiv.org/abs/2501.10357) · [專案頁](https://research.nvidia.com/labs/lpr/zero_msf/) | NVIDIA / Brown | 聯合估幾何與運動並大規模混合資料訓練，單目場景流首次能 zero-shot 泛化 | CVPR 2025 | 24 | 未公開 |
| 新興 | 獲獎 | 2026 | [Indoor Open-Vocab Occupancy](https://arxiv.org/abs/2602.22667) | HKUST(GZ) | 針對室內密集幾何與細粒度語意，從單目影像預測開放詞彙 3D occupancy | CVPR 2026 | 8 | 未公開 |
| 新興 | 獲獎、推薦 | 2026 | [GlassRecon](https://arxiv.org/abs/2604.18336) | HKUST / HKU / SUSTech / ASTRI | 免訓練，用局部 RANSAC 把深度基礎模型對齊到感測器深度，避開玻璃區的錯誤量測並補回公制尺度 | IROS 2026 | 2 | [9](https://github.com/jarvisyjw/GlassRecon) |
| 新興 | 獲獎 | 2025 | [DiFuse-Net](https://arxiv.org/abs/2506.14709) | Samsung Research India | 把 RGB 與手機雙像素（dual-pixel）分開編碼後以雙向視差注意力融合估深度 | IROS 2025 | 0 | 未公開 |
| 新興 | 獲獎 | 2026 | [SeeGroup](https://arxiv.org/abs/2605.28735) | Princeton | 讓模型自行決定點的分層方式，估計透明表面與其後物體的多層深度 | CVPR 2026 | 0 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-09 | [Monocular Depth Estimation: Progress and Opportunities](https://arxiv.org/abs/2609.01172) | HKU | 單眼深度綜述 |  | [GitHub](https://github.com/CVMI-Lab/Depth_Survey) | arXiv |
| 2026-07 | [ARDepth](https://arxiv.org/abs/2607.12433) | SYSU / Baidu | 自回歸單眼深度估計 |  | 未公開 | arXiv |

## 語意地圖與場景圖

### 在解決的問題

- 開放詞彙：不限定類別，能用任意語言查物件與區域。
- 可擴展：稠密特徵地圖太大，改用物件／房間／樓層的階層場景圖壓縮。
- 即時、增量：邊走邊建，並處理場景變動。
- 當成 LLM／VLM 規劃的介面。

### 重要論文（資料日期 2026-10-20）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、Star | 2023 | [LERF](https://arxiv.org/abs/2303.09553) · [專案頁](https://lerf.io) | UC Berkeley | 把 CLIP 特徵嵌進 NeRF 做語言查詢 | ICCV 2023 | 768 | [734](https://github.com/kerrj/lerf) |
| 奠基 | 引用、Star、推薦 | 2023 | [ConceptGraphs](https://arxiv.org/abs/2309.16650) · [專案頁](https://concept-graphs.github.io/) | Toronto / MIT | 用 2D 基礎模型建開放詞彙 3D 場景圖，支援 LLM 規劃 | ICRA 2024 | 685 | [975](https://github.com/concept-graphs/concept-graphs) |
| 奠基 | 引用、Star | 2024 | [HOV-SG](https://arxiv.org/abs/2403.17846) · [專案頁](http://hovsg.github.io/) | Freiburg | 樓層／房間／物件階層開放詞彙場景圖，跨樓層語言導航 | RSS 2024 | 358 | [556](https://github.com/hovsg/HOV-SG) |
| 主流 | 引用、Star、推薦 | 2022 | [VLMaps](https://arxiv.org/abs/2210.05714) · [專案頁](https://vlmaps.github.io) | Freiburg / Google | 把 VLM 特徵融合進 3D 地圖，可用語言查空間位置 | ICRA 2023 | 714 | [730](https://github.com/vlmaps/vlmaps) |
| 主流 | 引用、Star | 2023 | [LangSplat](https://arxiv.org/abs/2312.16084) · [專案頁](https://langsplat.github.io/) | Tsinghua / Harvard | 以 3D Gaussian 承載 SAM 階層語意的 CLIP 語言場 | CVPR 2024 | 594 | [1,096](https://github.com/minghanqin/LangSplat) |
| 主流 | 引用、獲獎 | 2021 | [Semantic-NeRF](https://arxiv.org/abs/2103.15875) · [專案頁](https://shuaifengzhi.com/Semantic-NeRF/) | Imperial | NeRF 同時編碼語意，少量標註即可補全場景標籤 | ICCV 2021 | 587 | [462](https://github.com/Harry-Zhi/semantic_nerf) |
| 主流 | 引用、獲獎 | 2023 | [SayPlan](https://arxiv.org/abs/2307.06135) · [專案頁](https://sayplan.github.io) | QUT / Univ. of Adelaide | LLM 在 3D 場景圖上語意搜尋做大尺度任務規劃 | CoRL 2023 | 541 | 未公開 |
| 主流 | 引用 | 2023 | [ConceptFusion](https://arxiv.org/abs/2302.07241) · [專案頁](https://concept-fusion.github.io) | MIT / Toronto | 把基礎模型特徵融合成開放集合 3D 地圖 | RSS 2023 | 458 | [247](https://github.com/concept-fusion/concept-fusion) |
| 主流 | 引用、Star | 2022 | [Hydra](https://arxiv.org/abs/2201.13360) | MIT SPARK | 即時建立階層式 3D 場景圖（物件／房間／樓層） | RSS 2022 | 396 | [1,182](https://github.com/MIT-SPARK/Hydra) |
| 主流 | 引用 | 2023 | [LEGaussians](https://arxiv.org/abs/2311.18482) | Beihang | 量化壓縮語言特徵嵌入 3D Gaussian 做開放詞彙查詢 | CVPR 2024 | 265 | [174](https://github.com/buaavrcg/LEGaussians) |
| 主流 | 引用 | 2024 | [Clio](https://arxiv.org/abs/2404.13696) | MIT SPARK | 依任務決定物件粒度的場景圖（information bottleneck） | RA-L 2024 | 157 | [263](https://github.com/MIT-SPARK/Clio) |
| 主流 | 引用 | 2024 | [FMGS](https://arxiv.org/abs/2401.01970) · [專案頁](https://xingxingzuo.github.io/fmgs) | Google | 3DGS 結合多解析度雜湊編碼嵌入基礎模型特徵 | IJCV 2025 | 137 | 未公開 |
| 主流 | 引用 | 2024 | [Open3DSG](https://arxiv.org/abs/2402.12259) · [專案頁](https://kochsebastian.com/open3dsg) | Bosch / Ulm / TU Vienna | 從點雲預測開放詞彙物件與開放集合關係的場景圖 | CVPR 2024 | 134 | [166](https://github.com/boschresearch/Open3DSG) |
| 主流 | 引用、推薦 | 2024 | [3D-Mem](https://arxiv.org/abs/2411.17735) · [專案頁](https://umass-embodied-agi.github.io/3D-Mem/) | UMass Amherst / CUHK / Columbia 等 | 以多視角快照影像當 3D 場景記憶支援探索與推理 | CVPR 2025 | 118 | [280](https://github.com/UMass-Embodied-AGI/3D-Mem) |
| 主流 | 引用、推薦 | 2024 | [ReMEmbR](https://arxiv.org/abs/2409.13682) · [專案頁](https://nvidia-ai-iot.github.io/remembr/) | NVIDIA / USC / UT Austin | VILA 把機器人影片轉成帶位置與時間的描述存進向量資料庫，LLM 迴圈檢索回答長時間部署中的空間、時間與描述性問題 | ICRA 2025 | 117 | [360](https://github.com/NVIDIA-AI-IOT/remembr) |
| 主流 | 引用 | 2024 | [Semantic Gaussians](https://arxiv.org/abs/2403.15624) · [專案頁](https://semantic-gaussians.github.io) | BIGAI / Tsinghua | 免訓練將 2D 預訓練模型語意蒸餾到 3D Gaussian | TCSVT 2026 | 105 | [280](https://github.com/sharinka0715/semantic-gaussians) |
| 主流 | 引用 | 2024 | [SemGauss-SLAM](https://arxiv.org/abs/2403.07494) | SJTU / Cambridge | 語意特徵嵌入 3D Gaussian 的稠密語意 SLAM | IROS 2025 | 103 | [82](https://github.com/IRMVLab/SemGauss-SLAM) |
| 主流 | 引用 | 2025 | [OpenFunGraph](https://arxiv.org/abs/2503.19199) · [專案頁](https://openfungraph.github.io/) | Tsinghua / ETH / Microsoft 等 | 含功能元件與互動關係的開放詞彙功能性場景圖 | CVPR 2025 | 78 | [58](https://github.com/ZhangCYG/OpenFunGraph) |
| 主流 | 引用 | 2025 | [Dr. Splat](https://arxiv.org/abs/2502.16652) | POSTECH / KAIST / NVIDIA | 把語言特徵直接登錄到 3D Gaussian 上，不必逐視角渲染特徵，查詢更快 | CVPR 2025 | 67 | [107](https://github.com/kaist-ami/Dr-Splat) |
| 主流 | 引用、機構 | 2025 | [RayFronts](https://arxiv.org/abs/2504.06994) | CMU | 以語意射線前緣同時表示範圍內與超出範圍的語意 | IROS 2025 | 43 | [149](https://github.com/RayFronts/RayFronts) |
| 主流 | 引用 | 2025 | [FunGraph](https://arxiv.org/abs/2503.07909) · [專案頁](https://fungraph.github.io) | Univ. of Stuttgart / Bonn | 偵測可操作部件的功能感知 3D 場景圖 | IROS 2025 | 31 | [19](https://github.com/DennisRotondi/FunGraph) |
| 主流 | 引用 | 2025 | [OpenGS-SLAM](https://arxiv.org/abs/2503.01646) | BIT | Gaussian 投票濺射的開放集合物件級語意 SLAM | ICRA 2025 | 31 | [315](https://github.com/YOUNG-bit/open_semantic_slam) |
| 新興 | 獲獎 | 2025 | [FindAnything](https://arxiv.org/abs/2504.08603) | TUM / Imperial | 把視覺語言特徵併入物件中心的體素子地圖，即時、可擴展的開放詞彙探索建圖 | ICRA 2026 | 16 | 未公開 |
| 新興 | 獲獎、推薦 | 2026 | [LT-Mem](https://arxiv.org/abs/2608.19059) | DGIST | 多 session SLAM 對齊物件後，依物件變動程度選擇覆寫、保留或多假設，保存跨 session 的物件身分與歷史，可回答「某物去過哪裡」 | IROS 2026 | 0 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [Industrial ReMEmbR](https://arxiv.org/abs/2610.28624) | Idealworks / NVIDIA | 把 ReMEmbR 擴成多機器人共用的時空記憶：機上只上傳嵌入與視覺 token，描述改為查詢時才生成，並把人像遮掉 | NaVQA 首次解析失敗率 20.7% → 13.8%；快取 token 解碼 450 次與原模型輸出一致 | 未公開 | arXiv |
| 2026-05 | [LEXI-SG](https://arxiv.org/abs/2605.13741) · [專案頁](https://ori-drs.github.io/lexisg-web/) | Oxford | 只用單眼 RGB 建開放詞彙 3D 場景圖，以房間為單位 feed-forward 重建 | 評估在 HM3D 與自錄辦公室序列，未做實機導航 | 未公開 | RA-L 2026 |

## 3D 偵測與分割（點雲骨幹、3D 偵測、語意／實例分割）

### 在解決的問題

- 點雲骨幹：在大場景上兼顧準確與速度，並靠自監督或 2D 基礎模型蒸餾減少 3D 標註。
- 開放詞彙 3D 偵測與實例分割：3D 標註少，靠 2D 基礎模型（CLIP、SAM）的結果提升到 3D。
- 物件位姿與形狀：從點雲或單張影像估計物件 6D／9D 位姿。

### 重要論文（資料日期 2026-10-20）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、Star | 2022 | [PointNeXt](https://arxiv.org/abs/2206.04670) | KAUST / Microsoft | 只改訓練策略與縮放就讓 PointNet++ 追上新架構，提供強而簡單的點雲基線 | NeurIPS 2022 | 1,296 | [1,088](https://github.com/guochengqian/pointnext) |
| 奠基 | 引用 | 2021 | [Point-BERT](https://arxiv.org/abs/2111.14819) · [專案頁](https://point-bert.ivg-research.xyz) | Tsinghua / PKU / BAAI | 把 BERT 遮罩建模搬到點雲，以離散 token 做點雲 transformer 預訓練 | CVPR 2022 | 1,241 | 未公開 |
| 奠基 | 引用、Star、HF | 2023 | [Point Transformer V3](https://arxiv.org/abs/2312.10035) | HKU / Shanghai AI Lab / MIT 等 | 用序列化取代精確鄰域搜尋，換取大感受野與速度，以規模取勝的點雲骨幹 | CVPR 2024 | 1,183 | [1,978](https://github.com/Pointcept/PointTransformerV3) |
| 奠基 | 引用、Star | 2023 | [FoundationPose](https://arxiv.org/abs/2312.08344) · [專案頁](https://nvlabs.github.io/FoundationPose/) | NVIDIA | 單一模型同時支援有 CAD 與只有少量參考影像兩種設定，對未見過的物件做 6D 位姿估計與追蹤 | CVPR 2024 | 875 | [3,644](https://github.com/NVlabs/FoundationPose) |
| 奠基 | 引用、Star | 2024 | [PointMamba](https://arxiv.org/abs/2402.10739) | HUST / Baidu | 以狀態空間模型取代注意力，線性複雜度的點雲分析骨幹 | NeurIPS 2024 | 394 | [550](https://github.com/LMD0311/PointMamba) |
| 奠基 | 引用、Star | 2025 | [Sonata](https://arxiv.org/abs/2503.16429) · [專案頁](https://xywu.me/sonata/) | Meta Reality Labs / HKU | 找出自監督點雲模型的幾何捷徑問題並修正，linear probing 即可用於多種 3D 任務 | CVPR 2025 | 157 | [806](https://github.com/facebookresearch/sonata) |
| 主流 | 引用 | 2022 | [Point Transformer V2](https://arxiv.org/abs/2210.05666) | HKU 等 | 分組向量注意力與分區池化，降低 Point Transformer 的計算並提升分割表現 | NeurIPS 2022 | 938 | 未公開 |
| 主流 | 引用、Star | 2022 | [Point-MAE](https://arxiv.org/abs/2203.06604) | PKU / Tencent | 點雲版的遮罩自編碼器，遮掉點塊再重建做自監督預訓練 | ECCV 2022 | 824 | [646](https://github.com/Pang-Yatian/Point-MAE) |
| 主流 | 引用、Star | 2022 | [OpenScene](https://arxiv.org/abs/2211.15654) · [專案頁](https://pengsongyou.github.io/openscene) | ETH / Google | 零樣本開放詞彙 3D 場景理解 | CVPR 2023 | 810 | [853](https://github.com/pengsongyou/openscene) |
| 主流 | 引用、Star | 2021 | [3DETR](https://arxiv.org/abs/2109.08141) · [專案頁](https://facebookresearch.github.io/3detr) | Meta FAIR | 純 transformer 編碼解碼器直接輸出 3D 框，不需手工設計的 3D 算子，室內點雲偵測的簡潔基線 | ICCV 2021 | 652 | [717](https://github.com/facebookresearch/3detr) |
| 主流 | 引用、Star、基準 | 2021 | [ARKitScenes](https://arxiv.org/abs/2111.08897) | Apple | 用 iPad LiDAR 拍的大規模室內 RGB-D 資料集，附高精度雷射掃描與 3D 框 | NeurIPS 2021 Datasets and Benchmarks | 546 | [971](https://github.com/apple/ARKitScenes) |
| 主流 | 引用、Star | 2022 | [Mask3D](https://arxiv.org/abs/2210.03105) · [專案頁](https://jonasschult.github.io/Mask3D/) | RWTH Aachen / ETH / NVIDIA | 以 Transformer 實例查詢直接預測 3D 實例遮罩，不需手工分群 | ICRA 2023 | 482 | [748](https://github.com/JonasSchult/Mask3D) |
| 主流 | 引用 | 2022 | [ULIP](https://arxiv.org/abs/2212.05171) | Salesforce / Stanford | 以影像-文字-點雲三模態對比學習，把 CLIP 空間延伸到 3D | CVPR 2023 | 446 | 未公開 |
| 主流 | 引用 | 2022 | [Stratified Transformer](https://arxiv.org/abs/2203.14508) | HKU / CUHK / SmartMore 等 | 近處密、遠處稀的分層取樣 key，讓點雲分割模型能建模長距離關係 | CVPR 2022 | 426 | [430](https://github.com/dvlab-research/Stratified-Transformer) |
| 主流 | 引用 | 2023 | [OpenMask3D](https://arxiv.org/abs/2306.13631) · [專案頁](https://openmask3d.github.io/) | ETH / Microsoft / Google | 多視角融合 CLIP 特徵的零樣本開放詞彙 3D 實例分割 | NeurIPS 2023 | 397 | [273](https://github.com/OpenMask3D/openmask3d) |
| 主流 | 引用 | 2022 | [SoftGroup](https://arxiv.org/abs/2203.01509) | KAIST | 點雲 3D 實例分割，以軟語意分數分群減少語意誤判造成的實例錯誤 | CVPR 2022 | 370 | [461](https://github.com/thangvubk/SoftGroup) |
| 主流 | 引用 | 2021 | [DepthContrast](https://arxiv.org/abs/2101.02691) | Meta FAIR / UT Austin | 不限點雲格式的對比式自監督預訓練，單視角深度掃描也能用 | ICCV 2021 | 354 | 未公開 |
| 主流 | 引用、基準 | 2022 | [ScanNet200](https://arxiv.org/abs/2204.07761) · [專案頁](https://rozdavid.github.io/scannet200) | TUM / NVIDIA | 把 ScanNet 擴到 200 類長尾室內語意分割基準，並用 CLIP 文字特徵預訓練點雲特徵改善少見類別 | ECCV 2022 | 336 | [124](https://github.com/RozDavid/LanguageGroundedSemseg) |
| 主流 | 引用、Star | 2023 | [Uni3D](https://arxiv.org/abs/2310.06773) | BAAI / Tsinghua / PKU | 以 2D ViT 初始化並擴到 10 億參數的 3D 表示模型，對齊影像文字特徵做零樣本 3D 辨識 | ICLR 2024 | 291 | [687](https://github.com/baaivision/Uni3D) |
| 主流 | 引用 | 2023 | [CLIP2Scene](https://arxiv.org/abs/2301.04926) | Shanghai AI Lab / HKU 等 | 把 CLIP 知識蒸餾到 3D 點雲網路，標註少或零標註也能做場景語意分割 | CVPR 2023 | 282 | [188](https://github.com/runnanchen/clip2scene) |
| 主流 | 引用 | 2023 | [OctFormer](https://arxiv.org/abs/2305.03045) | Peking University | 以八叉樹排序切窗做注意力，複雜度線性，大場景點雲分割與偵測更快 | SIGGRAPH 2023 | 239 | 未公開 |
| 主流 | Star、基準 | 2022 | [Omni3D / Cube R-CNN](https://arxiv.org/abs/2207.10660) · [專案頁](https://garrickbrazil.com/omni3d) | Meta AI | 整合室內外多資料集的單張影像 3D 偵測基準，Cube R-CNN 跨相機與場景通用 | CVPR 2023 | 227 | [854](https://github.com/facebookresearch/omni3d) |
| 主流 | 引用、Star | 2023 | [OneFormer3D](https://arxiv.org/abs/2311.14405) | Samsung Research | 單一 transformer 同時做點雲語意、實例與全景分割 | CVPR 2024 | 205 | [617](https://github.com/oneformer3d/oneformer3d) |
| 主流 | 引用 | 2023 | [Open3DIS](https://arxiv.org/abs/2312.10671) · [專案頁](https://open3dis.github.io/) | VinAI / UMass Amherst / MIT-IBM Watson AI Lab | 聚合跨幀 2D 實例遮罩補足 3D 開放詞彙實例分割 | CVPR 2024 | 173 | [138](https://github.com/VinAIResearch/Open3DIS) |
| 主流 | 引用、Star | 2023 | [Superpoint Transformer](https://arxiv.org/abs/2306.08045) | IGN / Univ Gustave Eiffel | 先把點雲分成階層超點再做注意力，大場景語意分割參數少、訓練快 | ICCV 2023 | 171 | [1,066](https://github.com/drprojects/superpoint_transformer) |
| 主流 | 引用 | 2024 | [OA-CNNs](https://arxiv.org/abs/2403.14418) | HKU / CUHK 等 | 讓稀疏 CNN 自適應調整感受野，在點雲分割上追平 transformer 且更快 | CVPR 2024 | 103 | 未公開 |
| 主流 | 引用 | 2024 | [MaskClustering](https://arxiv.org/abs/2401.07745) | PKU / BAAI / Galbot | 以視角共識率做遮罩圖分群的開放詞彙 3D 實例分割 | CVPR 2024 | 83 | [133](https://github.com/PKU-EPIC/MaskClustering) |
| 主流 | 引用、Star、HF | 2025 | [Concerto](https://arxiv.org/abs/2510.23607) · [專案頁](https://pointcept.github.io/Concerto/) | HKU / CUHK / HIT(SZ) | 2D-3D 聯合自監督學習，單用點雲也能喚起與影像一致的空間表示 | NeurIPS 2025 | 50 | [542](https://github.com/Pointcept/Concerto) |
| 主流 | 引用 | 2025 | [DITR (DINO in the Room)](https://arxiv.org/abs/2503.18944) · [專案頁](https://vision.rwth-aachen.de/ditr) | RWTH Aachen / Bosch | 把 DINOv2 影像特徵投影到點雲注入 3D 分割骨幹，或在無影像時用來蒸餾 | 3DV 2026 | 48 | [116](https://github.com/VisualComputingInstitute/DITR) |
| 主流 | Star、獲獎 | 2022 | [EPro-PnP](https://arxiv.org/abs/2203.13254) | Tongji / Alibaba | 把 PnP 輸出改成位姿機率分布，使 2D-3D 對應能端到端學習，用於單目物件位姿估計 | CVPR 2022 | 3 | [1,177](https://github.com/tjiiv-cprg/EPro-PnP) |
| 新興 | 獲獎 | 2022 | [InterObject3D](https://arxiv.org/abs/2204.07183) | ETH / RWTH Aachen | 使用者點擊迭代修正的互動式 3D 實例分割，可泛化到訓練外類別 | ICRA 2023 | 35 | 未公開 |
| 新興 | 獲獎 | 2021 | [Category-level Pose and Shape](https://arxiv.org/abs/2104.08383) | MIT | 給類別 CAD 庫的主動形狀模型，以可驗證全域最優的凸鬆弛同時解物件位姿與形狀，對離群點穩健 | RSS 2021 | 29 | 未公開 |
| 新興 | 獲獎 | 2025 | [Chorus](https://arxiv.org/abs/2512.17817) · [專案頁](https://gaussianworld.github.io/Chorus) | Amsterdam / ETH / INSAIT | 從多個 2D 基礎模型蒸餾，學出 feed-forward 的 3DGS 場景編碼器，提供通用 3D 特徵 | CVPR 2026 | 12 | 未公開 |
| 新興 | 獲獎 | 2024 | [HEGN](https://doi.org/10.1109/ICRA57147.2024.10610562) | Siemens / TUM | 階層式等變圖網路做含縮放的 9DoF 點雲配準，用於類別級位姿估計 | ICRA 2024 | 1 | 未公開 |
| 新興 | 獲獎 | 2025 | [SNAP](https://arxiv.org/abs/2510.11565) · [專案頁](https://neu-vi.github.io/SNAP/) | Northeastern / MathWorks | 跨室內、室外、空拍點雲的互動式 3D 分割，同時支援點選與文字提示 | 3DV 2026 | 0 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |

## 3D 空間理解（3D grounding、空間推理 VLM、3D-LLM）

### 在解決的問題

- 3D grounding：把「沙發右邊的桌子」這類含空間關係的描述對到 3D 中的特定物件。
- VLM 的空間推理：VLM 多用 2D 圖文訓練，距離、方位、大小常答錯；做法是用 3D 資料合成空間問答，或接上深度、點雲輸入。
- 從影片理解空間：機器人只有連續影像、沒有完整點雲時，要從影片累積對空間的記憶與推理。

### 重要論文（資料日期 2026-10-20）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、HF | 2024 | [SpatialVLM](https://arxiv.org/abs/2401.12168) · [專案頁](https://spatial-vlm.github.io/) | Google DeepMind / Google Research | 用網路圖片加深度與物件偵測自動合成大規模 3D 空間問答，讓 VLM 能回答距離、大小等定量問題 | CVPR 2024 | 1,129 | 未公開 |
| 奠基 | 引用、Star、HF、基準 | 2024 | [VSI-Bench](https://arxiv.org/abs/2412.14171) · [專案頁](https://vision-x-nyu.github.io/thinking-in-space.github.io/) | NYU / Yale / Stanford | 從室內影片測 MLLM 空間記憶與推理的 benchmark，發現模型會在內部形成局部認知地圖 | CVPR 2025 | 849 | [750](https://github.com/vision-x-nyu/thinking-in-space) |
| 奠基 | 基準 | 2019 | [ScanRefer](https://arxiv.org/abs/1912.08830) · [專案頁](https://daveredrum.github.io/ScanRefer/) | TUM / Simon Fraser Univ. | 第一個 RGB-D 掃描上的 3D 語言 grounding 資料集與基線 | ECCV 2020 | 675 | [306](https://github.com/daveredrum/ScanRefer) |
| 奠基 | 引用 | 2024 | [SpatialRGPT](https://arxiv.org/abs/2406.01584) · [專案頁](https://www.anjiecheng.me/SpatialRGPT) | UC San Diego / NVIDIA | 以區域提示加深度輸入，讓 VLM 對指定區域做相對方向與距離推理 | NeurIPS 2024 | 437 | [340](https://github.com/AnjieCheng/SpatialRGPT) |
| 奠基 | 引用、HF | 2025 | [Spatial-MLLM](https://arxiv.org/abs/2505.23747) · [專案頁](https://diankun-wu.github.io/Spatial-MLLM/) | Tsinghua | 在 2D 視覺編碼器旁加 VGGT 幾何編碼器，只用影片就提升 MLLM 的空間推理 | NeurIPS 2025 | 258 | [496](https://github.com/diankun-wu/Spatial-MLLM) |
| 奠基 | 引用、基準 | 2025 | [MMSI-Bench](https://arxiv.org/abs/2505.23764) · [專案頁](https://runsenxu.com/projects/MMSI_Bench) | Shanghai AI Lab / CUHK 等 | 多張影像的空間推理 benchmark，人工出題，最強模型與人類差距仍大 | ICLR 2026 | 218 | [109](https://github.com/OpenRobotLab/MMSI-Bench) |
| 奠基 | 引用 | 2025 | [VLM-3R](https://arxiv.org/abs/2505.20279) · [專案頁](https://vlm-3r.github.io) | UT Austin / UCLA / Meta 等 | 從單眼影片重建 3D 特徵並與指令對齊，讓 VLM 做空間與時間推理 | CVPR 2026 | 189 | [451](https://github.com/VITA-Group/VLM-3R) |
| 奠基 | 引用、HF | 2025 | [RoboRefer](https://arxiv.org/abs/2506.04308) · [專案頁](https://zhoues.github.io/RoboRefer/) | Beihang / PKU / BAAI | 以 SFT 加 RL 訓練能多步推理的空間指代 VLM，輸出機器人要去或放的點 | NeurIPS 2025 | 168 | [268](https://github.com/Zhoues/RoboRefer) |
| 奠基 | 引用、Star、HF | 2025 | [Cambrian-S](https://arxiv.org/abs/2511.04670) · [專案頁](https://cambrian-mllm.github.io/) | NYU / Stanford | 從影片做空間超感知：以預測下一幀的驚訝度決定記憶與事件切分，並提出 VSI-SUPER | arXiv | 156 | [571](https://github.com/cambrian-mllm/cambrian-s) |
| 奠基 | 引用 | 2025 | [SPAR](https://arxiv.org/abs/2503.22976) · [專案頁](https://logosroboticsgroup.github.io/SPAR/) | Fudan / Huawei Noah's Ark | 從 3D 掃描自動生成 700 萬筆空間問答（SPAR-7M），只用 2D 輸入就提升 VLM 3D 推理 | NeurIPS 2025 | 148 | [97](https://github.com/fudan-zvg/spar) |
| 奠基 | 引用 | 2025 | [VG LLM](https://arxiv.org/abs/2505.24625) · [專案頁](https://lavi-lab.github.io/VG-LLM/) | CUHK | 在 MLLM 中加 3D 幾何編碼器，直接從影片抽出 3D 先驗，不需點雲或深度 | NeurIPS 2025 | 141 | [260](https://github.com/LaVi-Lab/VG-LLM) |
| 奠基 | 引用、Star | 2025 | [GPT4Scene](https://arxiv.org/abs/2501.01428) · [專案頁](https://gpt4scene.github.io/) | HKU / Shanghai AI Lab | 從影片重建鳥瞰圖並在畫面與鳥瞰圖標上一致的物件編號，讓 VLM 建立全域空間關係 | arXiv | 124 | [544](https://github.com/Qi-Zhangyang/GPT4Scene-and-VLN-R1) |
| 奠基 | 引用、HF、基準 | 2025 | [OmniSpatial](https://arxiv.org/abs/2506.03135) · [專案頁](https://qizekun.github.io/omnispatial/) | Tsinghua / PKU / Galbot 等 | 涵蓋動態推理、視角轉換等進階空間推理的 benchmark | ICLR 2026 | 122 | [95](https://github.com/qizekun/OmniSpatial) |
| 主流 | 引用、基準 | 2021 | [ScanQA](https://arxiv.org/abs/2112.10482) | Kyoto Univ. / RIKEN AIP | 提出 3D 問答任務與資料集：在室內掃描上回答空間問題並定位相關物件 | CVPR 2022 | 508 | [165](https://github.com/ATR-DBI/ScanQA) |
| 主流 | 引用 | 2023 | [LEO](https://arxiv.org/abs/2311.12871) · [專案頁](https://embodied-generalist.github.io/) | BIGAI 等 | 在 3D 場景中同時做描述、問答、導航與操作的具身通用模型 | ICML 2024 | 464 | [490](https://github.com/embodied-generalist/embodied-generalist) |
| 主流 | 引用、獲獎 | 2023 | [PointLLM](https://arxiv.org/abs/2308.16911) | Shanghai AI Lab / CUHK | 把彩色物件點雲接進 LLM，依指令描述、問答物件 | ECCV 2024 | 460 | 未公開 |
| 主流 | 引用、基準 | 2022 | [VSR](https://arxiv.org/abs/2205.00363) | Univ. of Cambridge | 圖文配對形式的空間關係 benchmark，顯示 VLM 在方位關係上遠落後人類 | TACL 2023 | 400 | [150](https://github.com/cambridgeltl/visual-spatial-reasoning) |
| 主流 | 引用 | 2023 | [LL3DA](https://arxiv.org/abs/2311.18651) · [專案頁](https://ll3da.github.io/) | Fudan / Tencent PCG / NUS | 直接吃點雲並接受點擊、框選等視覺提示的 3D 助理，做描述、問答與規劃 | CVPR 2024 | 296 | [320](https://github.com/Open3DA/LL3DA) |
| 主流 | 引用 | 2023 | [Chat-Scene](https://arxiv.org/abs/2312.08168) | Zhejiang / Shanghai AI Lab / ByteDance | 給場景中每個物件一個識別碼 token，讓 LLM 用識別碼指涉物件做 grounding 與問答 | NeurIPS 2024 | 241 | [222](https://github.com/ZzZZCHS/Chat-Scene) |
| 主流 | 引用、基準 | 2023 | [Multi3DRefer](https://arxiv.org/abs/2309.05251) · [專案頁](https://3dlg-hcvc.github.io/multi3drefer/) | Simon Fraser Univ. | 3D grounding 擴充為一句描述可對應零到多個物件，附資料集與基線 | ICCV 2023 | 212 | [98](https://github.com/3dlg-hcvc/M3DRef-CLIP) |
| 主流 | 引用、獲獎、基準 | 2024 | [RoboSpatial](https://arxiv.org/abs/2411.16537) · [專案頁](https://chanh.ee/RoboSpatial) | Ohio State / NVIDIA | 機器人視角的大規模空間理解資料集（含參考座標系與可放置位置），訓練 2D/3D VLM | CVPR 2025 | 211 | [153](https://github.com/NVlabs/RoboSpatial) |
| 主流 | 引用、Star、基準 | 2023 | [EmbodiedScan](https://arxiv.org/abs/2312.16170) | Shanghai AI Lab 等 | 以機器人第一人稱 RGB-D 視角標註的 3D 偵測、occupancy 與 grounding 基準 | CVPR 2024 | 210 | [680](https://github.com/InternRobotics/EmbodiedScan) |
| 主流 | 引用 | 2023 | [LLM-Grounder](https://arxiv.org/abs/2309.12311) · [專案頁](https://chat-with-nerf.github.io/) | Univ. of Michigan | LLM 當代理拆解查詢並呼叫工具做 3D 視覺定位 | ICRA 2024 | 205 | [322](https://github.com/sled-group/chat-with-nerf) |
| 主流 | 引用、HF | 2024 | [LLaVA-3D](https://arxiv.org/abs/2409.18125) · [專案頁](https://zcmax.github.io/projects/LLaVA-3D/) | HKU / Shanghai AI Lab | 在 LLaVA 的 2D patch 上加 3D 位置編碼，沿用 2D 預訓練權重快速獲得 3D 理解 | ICCV 2025 | 201 | [392](https://github.com/ZCMax/LLaVA-3D) |
| 主流 | 引用、HF、基準 | 2024 | [SceneVerse](https://arxiv.org/abs/2401.09340) · [專案頁](https://scene-verse.github.io) | BIGAI | 約 6.8 萬個室內場景、數百萬句 3D 語言標註，用來預訓練 3D grounding 模型 | ECCV 2024 | 176 | [291](https://github.com/scene-verse/SceneVerse) |
| 主流 | 引用 | 2024 | [Video-3D LLM](https://arxiv.org/abs/2412.00493) | CUHK | 把 3D 場景當影片，在影片特徵加 3D 座標編碼做 3D 理解 | CVPR 2025 | 176 | [224](https://github.com/LaVi-Lab/Video-3D-LLM) |
| 主流 | 引用 | 2024 | [PQ3D](https://arxiv.org/abs/2405.11442) · [專案頁](https://pq3d.github.io) | Tsinghua / BIGAI | 可提示查詢的統一 3D 視覺語言模型，同時吃點雲、多視角影像等多種場景表示 | ECCV 2024 | 103 | 未公開 |
| 主流 | 引用、基準 | 2025 | [MM-Spatial](https://arxiv.org/abs/2503.13111) | Apple | 提出室內 3D 空間問答資料集 CA-VQA，訓練能估深度與 3D 位置的 MLLM | ICCV 2025 | 96 | [449](https://github.com/apple/ml-cubifyanything) |
| 主流 | 引用、HF | 2025 | [VST](https://arxiv.org/abs/2511.05491) · [專案頁](https://yangr116.github.io/vst_project/) | ByteDance Seed | 以空間感知與空間推理兩段資料漸進訓練 VLM，不改架構提升空間能力 | arXiv | 94 | [214](https://github.com/Yangr116/VST) |
| 主流 | 引用、Star、HF | 2025 | [SpatialLM](https://arxiv.org/abs/2506.07491) · [專案頁](https://manycore-research.github.io/SpatialLM) | Manycore Tech / HKUST | LLM 吃點雲直接輸出牆、門窗與物件 3D 框的結構化場景描述 | NeurIPS 2025 | 92 | [5,094](https://github.com/manycore-research/SpatialLM) |
| 主流 | 引用 | 2024 | [SeeGround](https://arxiv.org/abs/2412.04383) · [專案頁](https://seeground.github.io/) | HKUST(GZ) / NUS / A*STAR | 零樣本 3D grounding：選視角渲染畫面加物件位置文字，交給 2D VLM 判斷 | CVPR 2025 | 91 | [224](https://github.com/iris0329/SeeGround) |
| 主流 | 引用 | 2025 | [SpatialReasoner](https://arxiv.org/abs/2504.20024) · [專案頁](https://spatial-reasoner.github.io) | Johns Hopkins 等 | 讓 VLM 推理時先寫出明確的 3D 位置與方向，再據此回答 | NeurIPS 2025 | 80 | [45](https://github.com/johnson111788/SpatialReasoner) |
| 主流 | 引用 | 2025 | [Inst3D-LMM](https://arxiv.org/abs/2503.00513) | Zhejiang | 以實例為單位融合 2D 語意與 3D 幾何，一個模型做多種 3D 理解任務 | CVPR 2025 | 64 | [134](https://github.com/hanxunyu/Inst3D-LMM) |
| 主流 | 引用、HF | 2025 | [MindJourney](https://arxiv.org/abs/2507.12508) · [專案頁](https://umass-embodied-agi.github.io/MindJourney/) | UMass Amherst / JHU / Microsoft 等 | 推理時用影片 world model 想像換視角後的畫面，提升 VLM 空間推理，不需重新訓練 | NeurIPS 2025 | 57 | [154](https://github.com/UMass-Embodied-AGI/MindJourney) |
| 主流 | 引用 | 2025 | [G2VLM](https://arxiv.org/abs/2511.21688) · [專案頁](https://gordonhu608.github.io/g2vlm.github.io/) | Shanghai AI Lab / HKU 等 | 同一個 VLM 同時做 3D 重建與空間推理，幾何特徵直接支援問答 | arXiv | 48 | [360](https://github.com/InternRobotics/G2VLM) |
| 主流 | 引用、HF、基準 | 2025 | [OST-Bench](https://arxiv.org/abs/2507.07984) · [專案頁](https://rbler1234.github.io/OSTBench.github.io/) | Shanghai AI Lab / HKU 等 | 邊走邊看的線上時空理解 benchmark，模擬機器人探索時的空間記憶 | NeurIPS 2025 | 33 | [83](https://github.com/OpenRobotLab/OST-Bench) |
| 主流 | 引用 | 2025 | [SR-3D](https://arxiv.org/abs/2509.13317) · [專案頁](https://www.anjiecheng.me/sr3d) | UC San Diego / MIT / NVIDIA | 在 2D 特徵加 3D 位置編碼，可在任一視角框選區域並跨視角推理 | ICLR 2026 | 33 | [32](https://github.com/AnjieCheng/SR-3D) |
| 主流 | 引用 | 2025 | [3DLLM-Mem](https://arxiv.org/abs/2505.22657) · [專案頁](https://3dllm-mem.github.io) | UCLA / Google Research | 給具身 3D LLM 長期時空記憶，在多房間任務中選擇性取用過去觀察 | NeurIPS 2025 | 31 | 未公開 |
| 主流 | 引用 | 2025 | [Locate 3D](https://arxiv.org/abs/2504.14151) | Meta FAIR | 以 3D-JEPA 自監督學習點雲特徵，依指代語句在真實 RGB-D 感測資料中定位物件，可上機器人 | ICML 2025 | 31 | [456](https://github.com/facebookresearch/locate-3d) |
| 主流 | Star、HF | 2023 | [3D-LLM](https://arxiv.org/abs/2307.12981) · [專案頁](https://vis-www.cs.umass.edu/3dllm/) | UCLA / UMass Amherst / MIT-IBM Watson AI Lab | 把多視角 2D 特徵提升成 3D 特徵輸入 LLM，一個模型做 3D 問答、描述、grounding | NeurIPS 2023 | 0 | [1,216](https://github.com/UMass-Embodied-AGI/3D-LLM) |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |

## 電腦視覺（偵測、分割、視覺基礎模型）

### 在解決的問題

- 開放詞彙：偵測、分割不限類別（CLIP、Grounding DINO、SAM 3）。
- 通用視覺特徵：自監督預訓練（DINO）供深度、匹配、分割等下游任務。
- 即時性：能在機上跑（RT-DETR、YOLO-World）。
- 時序一致：點追蹤、影片分割（CoTracker、SAM 2）。

### 重要論文（資料日期 2026-10-20）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、Star、HF | 2021 | [CLIP](https://arxiv.org/abs/2103.00020) | OpenAI | 影像-文字對比預訓練，開放詞彙感知的起點 | ICML 2021 | 58,028 | [34,494](https://github.com/openai/CLIP) |
| 奠基 | 引用、獲獎 | 2021 | [Swin Transformer](https://arxiv.org/abs/2103.14030) | Microsoft Research Asia | 移位視窗的階層式 ViT，計算量隨解析度線性成長，可當偵測、分割通用骨幹 | ICCV 2021 | 36,640 | 未公開 |
| 奠基 | 引用、Star、獲獎 | 2023 | [SAM](https://arxiv.org/abs/2304.02643) · [專案頁](https://segment-anything.com) | Meta | 可提示的通用分割基礎模型 | ICCV 2023 | 16,270 | [55,039](https://github.com/facebookresearch/segment-anything) |
| 奠基 | 引用、Star | 2021 | [MAE](https://arxiv.org/abs/2111.06377) | Meta | 遮罩自編碼自監督預訓練 | CVPR 2022 | 13,228 | [8,360](https://github.com/facebookresearch/mae) |
| 奠基 | 引用、Star | 2022 | [YOLOv7](https://arxiv.org/abs/2207.02696) | Academia Sinica | E-ELAN 架構加重參數化訓練技巧的即時偵測器 | CVPR 2023 | 11,469 | [14,157](https://github.com/WongKinYiu/yolov7) |
| 奠基 | 引用、Star | 2023 | [DINOv2](https://arxiv.org/abs/2304.07193) | Meta | 自監督視覺特徵，免微調可用於深度、分割、匹配 | TMLR 2024 | 11,391 | [13,453](https://github.com/facebookresearch/dinov2) |
| 奠基 | 引用、Star | 2024 | [YOLOv10](https://arxiv.org/abs/2405.14458) | Tsinghua | 一致雙重標籤分配，免 NMS 的端到端 YOLO | NeurIPS 2024 | 6,265 | [11,341](https://github.com/THU-MIG/yolov10) |
| 奠基 | 引用、Star | 2023 | [Grounding DINO](https://arxiv.org/abs/2303.05499) | IDEA | 語言引導的開放集合物件偵測 | ECCV 2024 | 5,298 | [10,690](https://github.com/IDEA-Research/GroundingDINO) |
| 奠基 | 引用、Star | 2023 | [RT-DETR](https://arxiv.org/abs/2304.08069) · [專案頁](https://zhao-yian.github.io/RTDETR) | Baidu | 即時 DETR 偵測器 | CVPR 2024 | 4,732 | [5,608](https://github.com/lyuwenyu/RT-DETR) |
| 奠基 | 引用、Star、HF | 2024 | [SAM 2](https://arxiv.org/abs/2408.00714) · [專案頁](https://ai.meta.com/sam2) | Meta | 支援影片的可提示分割 | ICLR 2025 | 4,580 | [20,023](https://github.com/facebookresearch/sam2) |
| 奠基 | 引用、Star | 2023 | [SigLIP](https://arxiv.org/abs/2303.15343) | Google | sigmoid 損失的影像-文字預訓練，多數 VLM 的視覺編碼器 | ICCV 2023 | 4,107 | [3,554](https://github.com/google-research/big_vision) |
| 奠基 | 引用、Star | 2021 | [LoFTR](https://arxiv.org/abs/2104.00680) · [專案頁](https://zju3dv.github.io/loftr/) | Zhejiang / SenseTime | 無偵測器的 Transformer 粗到細半稠密匹配 | CVPR 2021 | 2,154 | [2,972](https://github.com/zju3dv/LoFTR) |
| 奠基 | 引用、Star、HF | 2025 | [DINOv3](https://arxiv.org/abs/2508.10104) | Meta | 擴大規模並改善稠密特徵的自監督視覺模型 | arXiv | 1,772 | [11,591](https://github.com/facebookresearch/dinov3) |
| 奠基 | 引用 | 2021 | [ViLD](https://arxiv.org/abs/2104.13921) | Google / NVIDIA | 把 CLIP 知識蒸餾到偵測器做開放詞彙偵測 | ICLR 2022 | 1,437 | 未公開 |
| 奠基 | 引用、Star | 2024 | [Grounded SAM](https://arxiv.org/abs/2401.14159) | IDEA | Grounding DINO + SAM 組合做開放詞彙分割 | arXiv | 1,375 | [17,773](https://github.com/IDEA-Research/Grounded-Segment-Anything) |
| 奠基 | 引用、Star | 2023 | [LightGlue](https://arxiv.org/abs/2306.13643) | ETH | 快速自適應的特徵匹配，SLAM 前端常用 | ICCV 2023 | 1,275 | [4,831](https://github.com/cvg/LightGlue) |
| 奠基 | 引用、Star、HF | 2025 | [SAM 3](https://arxiv.org/abs/2511.16719) | Meta | 以概念（文字／範例）提示的分割與追蹤 | arXiv | 1,275 | [12,039](https://github.com/facebookresearch/sam3) |
| 奠基 | 引用、Star、HF | 2024 | [YOLO-World](https://arxiv.org/abs/2401.17270) | Tencent | 即時開放詞彙偵測 | CVPR 2024 | 1,144 | [6,586](https://github.com/AILab-CVC/YOLO-World) |
| 奠基 | 引用、Star | 2023 | [SEEM](https://arxiv.org/abs/2304.06718) | UW-Madison / Microsoft / HKUST | 點框文字音訊等多種提示統一的互動分割 | NeurIPS 2023 | 903 | [4,792](https://github.com/UX-Decoder/Segment-Everything-Everywhere-All-At-Once) |
| 奠基 | 引用、Star | 2023 | [MobileSAM](https://arxiv.org/abs/2306.14289) | Kyung Hee | 解耦蒸餾 SAM 影像編碼器，行動裝置可跑 | arXiv | 726 | [5,892](https://github.com/ChaoningZhang/MobileSAM) |
| 奠基 | 引用、Star | 2023 | [HQ-SAM](https://arxiv.org/abs/2306.01567) | HKUST / ETH / Dartmouth | 加入高品質輸出 token 提升 SAM 遮罩邊緣 | NeurIPS 2023 | 720 | [4,264](https://github.com/SysCV/sam-hq) |
| 奠基 | 引用、Star | 2023 | [CoTracker](https://arxiv.org/abs/2307.07635) · [專案頁](https://co-tracker.github.io/) | Meta / Oxford | 聯合追蹤大量點的影片點追蹤 | ECCV 2024 | 690 | [5,162](https://github.com/facebookresearch/co-tracker) |
| 奠基 | 引用、HF | 2023 | [Florence-2](https://arxiv.org/abs/2311.06242) | Microsoft | 統一提示式文字輸出的多任務視覺基礎模型 | CVPR 2024 | 660 | 未公開 |
| 奠基 | 引用、Star、HF | 2023 | [FastSAM](https://arxiv.org/abs/2306.12156) | CAS / UCAS | 以 YOLOv8-seg 實例分割取代 SAM，大幅加速 | arXiv | 602 | [8,425](https://github.com/CASIA-IVA-Lab/FastSAM) |
| 奠基 | 引用、Star | 2024 | [DEIM](https://arxiv.org/abs/2412.04234) · [專案頁](https://www.shihuahuang.cn/DEIM/) | Intellindust / CityU / Great Bay | 稠密一對一匹配加速 DETR 收斂 | CVPR 2025 | 404 | [1,636](https://github.com/ShihuaHuang95/DEIM) |
| 奠基 | 引用、Star、HF | 2025 | [Perception Encoder](https://arxiv.org/abs/2504.13181) | Meta | 對比式圖文預訓練，對齊中間層特徵供各下游任務 | NeurIPS 2025 | 383 | [2,393](https://github.com/facebookresearch/perception_models) |
| 奠基 | 引用、Star、HF、獲獎 | 2024 | [Molmo](https://arxiv.org/abs/2409.17146) | AI2 / University of Washington | 不蒸餾私有 VLM，全靠人工收集的 PixMo 資料訓練開放 VLM，並能以點指出物件位置 | CVPR 2025 | 326 | [940](https://github.com/allenai/molmo) |
| 主流 | 引用、Star | 2021 | [RegionCLIP](https://arxiv.org/abs/2112.09106) | Microsoft / UW-Madison | 區域與文字對齊預訓練，用於開放詞彙偵測 | CVPR 2022 | 1,011 | [819](https://github.com/microsoft/RegionCLIP) |
| 主流 | 引用、Star、獲獎 | 2021 | [GMFlow](https://arxiv.org/abs/2111.13680) | Monash / Sydney / JD Explore | 以全域匹配取代 cost volume 迴歸的光流 | CVPR 2022 | 585 | [804](https://github.com/haofeixu/gmflow) |
| 主流 | 引用、Star | 2023 | [OWLv2](https://arxiv.org/abs/2306.09683) | Google DeepMind | 網路圖文對自訓練偽標註，擴大開放詞彙偵測 | NeurIPS 2023 | 505 | [3,844](https://github.com/google-research/scenic) |
| 主流 | 引用、Star | 2023 | [RoMa](https://arxiv.org/abs/2305.15404) | Linköping / ECUST / Chalmers | DINOv2 粗特徵加分類式回歸的穩健稠密匹配 | CVPR 2024 | 462 | [1,319](https://github.com/Parskatt/RoMa) |
| 主流 | 引用、Star | 2022 | [OWL-ViT](https://arxiv.org/abs/2205.06230) | Google | 用 CLIP 式骨幹做開放詞彙偵測 | ECCV 2022 | 457 | [3,844](https://github.com/google-research/scenic) |
| 主流 | 引用、Star | 2023 | [Track Anything](https://arxiv.org/abs/2304.11968) | SUSTech | SAM 結合 XMem 的互動式影片物件追蹤 | arXiv | 365 | [7,011](https://github.com/gaomingqi/Track-Anything) |
| 主流 | 引用、Star、基準 | 2022 | [TAP-Vid](https://arxiv.org/abs/2211.03726) | Google DeepMind / Oxford | 定義任意點追蹤任務並提供真實影片標註基準 | NeurIPS 2022 | 346 | [2,227](https://github.com/google-deepmind/tapnet) |
| 主流 | 引用、Star | 2023 | [EfficientSAM](https://arxiv.org/abs/2312.00863) | Meta | 以 SAM 特徵遮罩重建預訓練輕量分割模型 | CVPR 2024 | 328 | [2,498](https://github.com/yformer/EfficientSAM) |
| 主流 | 引用 | 2022 | [DKM](https://arxiv.org/abs/2202.00667) | Linköping | 核回歸全域匹配加深度引導細化的稠密匹配 | CVPR 2023 | 302 | [487](https://github.com/Parskatt/DKM) |
| 主流 | 引用、Star | 2023 | [SAM-Track](https://arxiv.org/abs/2305.06558) | Zhejiang | SAM 結合 DeAOT 的多模態互動影片分割追蹤 | arXiv | 283 | [3,142](https://github.com/z-x-yang/Segment-and-Track-Anything) |
| 主流 | 引用、Star | 2024 | [Efficient LoFTR](https://arxiv.org/abs/2403.04765) · [專案頁](https://zju3dv.github.io/efficientloftr/) | Zhejiang | 聚合注意力讓半稠密匹配接近稀疏方法速度 | CVPR 2024 | 278 | [1,058](https://github.com/zju3dv/EfficientLoFTR) |
| 主流 | 引用、Star | 2024 | [XFeat](https://arxiv.org/abs/2404.19174) | UFMG / Google / Univ. Bourgogne 等 | CPU 也能即時的輕量特徵偵測與匹配 | CVPR 2024 | 267 | [1,747](https://github.com/verlab/accelerated_features) |
| 主流 | 引用、Star、獲獎 | 2023 | [OmniMotion](https://arxiv.org/abs/2306.05422) | Cornell / Google / UC Berkeley | 測試時最佳化全域一致的準 3D 表示，對整段影片每個像素做長時距、跨遮擋追蹤 | ICCV 2023 | 254 | [2,268](https://github.com/qianqianwang68/omnimotion) |
| 主流 | 引用、Star、獲獎 | 2024 | [SEA-RAFT](https://arxiv.org/abs/2405.14793) | Princeton | 改用混合 Laplace 損失、直接回歸初始光流並以剛體運動預訓練，比 RAFT 更快更準 | ECCV 2024 | 251 | [718](https://github.com/princeton-vl/SEA-RAFT) |
| 主流 | 引用、Star | 2023 | [AM-RADIO](https://arxiv.org/abs/2312.06709) | NVIDIA | 多教師蒸餾融合 CLIP、DINOv2、SAM 的單一骨幹 | CVPR 2024 | 213 | [1,976](https://github.com/NVlabs/RADIO) |
| 主流 | 引用、Star | 2024 | [CoTracker3](https://arxiv.org/abs/2410.11831) | Meta / Oxford | 以偽標籤在真實影片半監督訓練的簡化點追蹤 | arXiv | 175 | [5,162](https://github.com/facebookresearch/co-tracker) |
| 主流 | Star、HF、獲獎 | 2026 | [Molmo2](https://arxiv.org/abs/2601.10611) | AI2 | 把 Molmo 延伸到影片理解與時空 grounding，資料與權重全開放 | CVPR 2026 | 156 | [748](https://github.com/allenai/molmo2) |
| 主流 | 引用、Star | 2024 | [SAMURAI](https://arxiv.org/abs/2411.11922) · [專案頁](https://yangchris11.github.io/samurai/) | UW | SAM 2 加運動感知記憶選擇的零樣本追蹤 | arXiv | 155 | [7,117](https://github.com/yangchris11/samurai) |
| 主流 | 引用、Star | 2024 | [DINO-X](https://arxiv.org/abs/2411.14347) | IDEA | 支援免提示的開放世界偵測與理解統一模型 | arXiv | 121 | [1,422](https://github.com/IDEA-Research/DINO-X-API) |
| 主流 | 引用、Star | 2024 | [OmniGlue](https://arxiv.org/abs/2405.12979) | UT Austin / Google | 用 DINOv2 引導關鍵點匹配，提升跨域泛化 | CVPR 2024 | 117 | [711](https://github.com/google-research/omniglue) |
| 主流 | 引用、Star | 2024 | [RADIOv2.5](https://arxiv.org/abs/2412.07679) | NVIDIA | 解決解析度模式切換並擴大規模的聚合骨幹 | CVPR 2025 | 112 | [1,976](https://github.com/NVlabs/RADIO) |
| 主流 | 引用、Star | 2024 | [LW-DETR](https://arxiv.org/abs/2406.03459) | Baidu / Adelaide / Beihang 等 | ViT 編碼器加淺層解碼器，取代 YOLO 的即時 DETR | arXiv | 97 | [514](https://github.com/Atten4Vis/LW-DETR) |
| 主流 | 引用、HF | 2024 | [Theia](https://arxiv.org/abs/2407.20179) | Stony Brook / The AI Institute | 蒸餾多個視覺基礎模型成機器人學習用小模型 | CoRL 2024 | 87 | [284](https://github.com/bdaiinstitute/theia) |
| 主流 | 引用 | 2025 | [AllTracker](https://arxiv.org/abs/2506.07310) · [專案頁](https://alltracker.github.io) | Stanford / CMU / TRI 等 | 以多幀光流估計做高解析度全像素點追蹤 | ICCV 2025 | 72 | [432](https://github.com/aharley/alltracker) |
| 主流 | 引用、Star | 2025 | [DEIMv2](https://arxiv.org/abs/2509.20787) · [專案頁](https://intellindust-ai-lab.github.io/projects/DEIMv2/) | Intellindust / Xiamen | DEIM 接上 DINOv3 特徵，涵蓋 GPU 到行動端 | arXiv | 71 | [2,067](https://github.com/Intellindust-AI-Lab/DEIMv2) |
| 主流 | 引用、Star | 2025 | [RoMa v2](https://arxiv.org/abs/2511.15706) | Linköping / Chalmers / Amsterdam 等 | 改良架構與訓練，更快更準的稠密匹配 | ECCV 2026 | 60 | [746](https://github.com/Parskatt/romav2) |
| 主流 | 引用、Star | 2025 | [RT-DETRv4](https://arxiv.org/abs/2510.25257) | PKU | 訓練時蒸餾基礎模型特徵，推論零額外成本 | arXiv | 39 | [663](https://github.com/RT-DETRs/RT-DETRv4) |
| 主流 | 引用、Star | 2025 | [EdgeTAM](https://arxiv.org/abs/2501.07256) | Meta / NTU | 2D 空間感知器壓縮記憶，讓 SAM 2 手機即時 | CVPR 2025 | 31 | [1,001](https://github.com/facebookresearch/EdgeTAM) |
| 新興 | 獲獎 | 2023 | [OvSGTR](https://arxiv.org/abs/2311.10988) | CASIA / PolyU | 物件與關係都開放詞彙的場景圖生成，以視覺概念對齊並保留知識避免遺忘 | ECCV 2024 | 50 | 未公開 |
| 新興 | 獲獎 | 2024 | [Evidential OOD Segmentation](https://doi.org/10.1109/ICRA57147.2024.10611342) | MIT / ARL | 不需 OOD 樣本，以證據式深度學習估計語意分割的逐像素不確定性，偵測未知障礙 | ICRA 2024 | 26 | 未公開 |
| 新興 | 獲獎 | 2025 | [LAPA](https://arxiv.org/abs/2512.04213) · [專案頁](https://ostadabbas.github.io/lapa.github.io/) | Northeastern | 端到端 transformer 同時做外觀匹配與幾何約束，多相機點追蹤不再拆成偵測、關聯、追蹤 | 3DV 2026 | 5 | [8](https://github.com/ostadabbas/Look-Around-and-Pay-Attention-LAPA-) |
| 新興 | 獲獎、基準 | 2026 | [GuideTWSI](https://arxiv.org/abs/2603.07060) | UMass Amherst / UT Austin / Maine | 合成加真實的導盲磚分割資料集，用於視障者導航輔助 | ICRA 2026 | 2 | 未公開 |
| 新興 | 獲獎 | 2026 | [Day-to-Night Agri Translation](https://arxiv.org/abs/2607.12065) | Kennesaw State / Lincoln | 非監督式日轉夜跨模態影像轉換，用白天標註訓練夜間農業視覺導航 | IROS 2026 | 0 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |

## 模擬與 Real2Sim

### 在解決的問題

- 視覺擬真：模擬器畫面和真實影像有落差，改用 NeRF／3DGS 重建真實場景來渲染。
- 物理可用：重建的場景要有碰撞網格、關節、材質，才能互動與訓練。
- 低成本擷取：手機或手持相機掃描就能建。
- 在數位分身裡訓練或評估策略，再部署回實機（real-to-sim-to-real）。
- 另一路線是生成式 world model（如 Cosmos）直接產生訓練資料。

### 重要論文（資料日期 2026-10-20）

| 分級 | 理由 | 年 | 論文 | 機構 | 重點 | 來源 | 引用 | Star |
|---|---|---|---|---|---|---|---|---|
| 奠基 | 引用、Star | 2021 | [Isaac Gym](https://arxiv.org/abs/2108.10470) · [專案頁](https://sites.google.com/view/isaacgym-nvidia) | NVIDIA | GPU 端到端物理模擬，大規模平行 RL | NeurIPS 2021 | 2,039 | [2,952](https://github.com/isaac-sim/IsaacGymEnvs) |
| 奠基 | 引用、Star、HF | 2025 | [Cosmos](https://arxiv.org/abs/2501.03575) · [專案頁](https://research.nvidia.com/labs/dir/cosmos1/) | NVIDIA | 物理 AI 的 world foundation model 平台 | arXiv | 960 | [12,076](https://github.com/NVIDIA/Cosmos) |
| 奠基 | 引用、Star、HF、機構 | 2025 | [V-JEPA 2](https://arxiv.org/abs/2506.09985) | Meta | 網路影片自監督預訓練，少量機器人資料即可規劃 | arXiv | 929 | [4,790](https://github.com/facebookresearch/vjepa2) |
| 奠基 | 引用、Star | 2023 | [Orbit / Isaac Lab](https://arxiv.org/abs/2301.04195) · [專案頁](https://isaac-orbit.github.io/) | NVIDIA / ETH | 基於 Isaac Sim 的機器人學習框架 | RA-L 2023 | 623 | [8,391](https://github.com/isaac-sim/IsaacLab) |
| 奠基 | 引用、Star、基準、機構 | 2024 | [SIMPLER](https://arxiv.org/abs/2405.05941) | UCSD / Stanford / Google DeepMind 等 | 縮小視覺與控制差距，用模擬評估真實操作策略 | CoRL 2024 | 602 | [1,177](https://github.com/simpler-env/SimplerEnv) |
| 奠基 | 引用、Star、HF | 2025 | [GEN3C](https://arxiv.org/abs/2503.03751) · [專案頁](https://research.nvidia.com/labs/toronto-ai/GEN3C/) | NVIDIA / Toronto / Vector | 以 3D 快取引導影片生成，精準相機控制 | CVPR 2025 | 395 | [1,439](https://github.com/nv-tlabs/GEN3C) |
| 奠基 | 引用、Star、基準 | 2024 | [ManiSkill3](https://arxiv.org/abs/2410.00425) · [專案頁](http://maniskill.ai/) | UCSD / Hillbot | GPU 平行模擬與渲染的通用操作平台 | arXiv | 364 | [3,436](https://github.com/haosulab/ManiSkill) |
| 奠基 | 引用 | 2025 | [PhysTwin](https://arxiv.org/abs/2503.17973) · [專案頁](https://jianghanxiao.github.io/phystwin-web/) | Columbia / UIUC | 從稀疏互動影片重建彈簧質點物理的變形物件分身 | ICCV 2025 | 134 | [471](https://github.com/Jianghanxiao/PhysTwin) |
| 奠基 | 引用、Star、基準、機構 | 2025 | [MuJoCo Playground](https://arxiv.org/abs/2502.08844) | UC Berkeley / Google DeepMind / Toronto 等 | 基於 MJX 的 GPU 模擬，分鐘級訓練並零樣本轉移 | arXiv | 128 | [2,259](https://github.com/google-deepmind/mujoco_playground) |
| 奠基 | 推薦 |  | [World Labs Atlas](https://www.worldlabs.ai/blog/atlas) | World Labs | 文字／影像／影片／3D 通用模型，可從手機影片重建場景並生成模擬用 RGB-D | 部落格 2026 | 0 | 未公開 |
| 主流 | 引用、基準 | 2021 | [HM3D](https://arxiv.org/abs/2109.08238) | Meta / UT Austin / Georgia Tech 等 | 千棟真實建築 3D 重建的具身 AI 場景資料集 | NeurIPS 2021 | 870 | [216](https://github.com/facebookresearch/habitat-matterport3d-dataset) |
| 主流 | 引用、Star | 2021 | [Habitat 2.0](https://arxiv.org/abs/2106.14405) | Meta | 可互動的室內重建場景模擬器，具身 AI 標準平台 | NeurIPS 2021 | 843 | [3,163](https://github.com/facebookresearch/habitat-lab) |
| 主流 | 引用、Star、基準 | 2023 | [Habitat 3.0](https://arxiv.org/abs/2310.13724) · [專案頁](http://aihabitat.org/habitat3) | Meta | 加入人形化身與真人在環的人機協作模擬平台 | ICLR 2024 | 346 | [3,163](https://github.com/facebookresearch/habitat-lab) |
| 主流 | 引用 | 2024 | [RialTo](https://arxiv.org/abs/2403.03949) · [專案頁](https://real-to-sim-to-real.github.io/RialTo/) | MIT | 真實場景重建成模擬環境，在模擬中強化學習修正策略 | RSS 2024 | 236 | [223](https://github.com/real-to-sim-to-real/RialToPolicyLearning) |
| 主流 | 引用、Star、基準 | 2023 | [Infinigen](https://arxiv.org/abs/2306.09310) | Princeton | 全程序化生成無限照片級自然場景 | CVPR 2023 | 215 | [7,347](https://github.com/princeton-vl/infinigen) |
| 主流 | 引用、機構 | 2024 | [ACDC](https://arxiv.org/abs/2410.07408) | Stanford | 用相似而非精確複製的數位表親場景訓練穩健策略 | CoRL 2024 | 149 | [255](https://github.com/cremebrule/digital-cousins) |
| 主流 | 引用 | 2024 | [Articulate-Anything](https://arxiv.org/abs/2410.13882) · [專案頁](https://articulate-anything.github.io/) | UPenn | VLM 生成程式碼並自我批評建立關節物件 | ICLR 2025 | 126 | [225](https://github.com/vlongle/articulate-anything) |
| 主流 | 引用 | 2024 | [SplatSim](https://arxiv.org/abs/2409.10161) · [專案頁](https://splatsim.github.io) | CMU | 用 3DGS 取代模擬器渲染，縮小視覺 sim-to-real 差距 | ICRA 2025 | 103 | [162](https://github.com/qureshinomaan/SplatSim) |
| 主流 | 引用 | 2024 | [DigitalTwinArt](https://arxiv.org/abs/2404.01440) | NVIDIA / Stanford | 兩次 RGBD 掃描重建未知關節物件數位分身 | CVPR 2024 | 93 | [74](https://github.com/NVlabs/DigitalTwinArt) |
| 主流 | 引用、Star、HF、基準 | 2024 | [GRUtopia](https://arxiv.org/abs/2407.10943) | Shanghai AI Lab / Zhejiang / SJTU 等 | 十萬互動場景的城市級具身模擬社會 | arXiv | 85 | [1,303](https://github.com/openrobotlab/grutopia) |
| 主流 | 引用、Star、基準、機構 | 2025 | [RoboVerse](https://arxiv.org/abs/2504.18904) · [專案頁](https://roboverseorg.github.io/) | UC Berkeley / PKU / USC 等 | 統一多種模擬器的機器人資料與基準平台 | arXiv | 83 | [1,872](https://github.com/RoboVerseOrg/RoboVerse) |
| 主流 | 引用 | 2025 | [ArtGS](https://arxiv.org/abs/2502.19459) · [專案頁](https://articulate-gs.github.io) | Tsinghua / BIGAI / PKU | 規範高斯加骨架式變形建模多部件關節物件 | ICLR 2025 | 78 | [83](https://github.com/YuLiu-LY/ArtGS) |
| 主流 | 引用、機構 | 2025 | [R2R2R](https://arxiv.org/abs/2505.09601) · [專案頁](https://real2render2real.com) | UC Berkeley / TRI | 手機掃描加人類示範影片渲染訓練資料，免動力學模擬 | CoRL 2025 | 70 | [377](https://github.com/uynitsuj/real2render2real) |
| 主流 | 引用、Star、機構 | 2025 | [RWM](https://arxiv.org/abs/2501.10100) · [專案頁](https://sites.google.com/view/roboticworldmodel) | ETH | 自迴歸神經模擬器，想像中訓練策略並實機部署 | arXiv | 64 | [690](https://github.com/leggedrobotics/robotic_world_model) |
| 主流 | 引用、機構 | 2025 | [Re3Sim](https://arxiv.org/abs/2502.08645) · [專案頁](http://xshenhan.github.io/Re3Sim/) | SJTU / Shanghai AI Lab / HKU | 3D 重建加神經渲染的照片級 real2sim 資料生成 | ICRA 2026 | 62 | [181](https://github.com/OpenRobotLab/Re3Sim) |
| 主流 | 引用、HF | 2025 | [Veo World Simulator](https://arxiv.org/abs/2512.10675) · [專案頁](https://veo-robotics.github.io/) | Google DeepMind | 把 Veo 影片模型改成以動作為條件、多視角一致的世界模擬器，用來排序策略、測 OOD 泛化與紅隊找不安全行為；1600+ 次實機評估顯示預測與實際成功率高度相關 | arXiv | 60 | 未公開 |
| 主流 | 引用 | 2025 | [Reality Gap Review](https://arxiv.org/abs/2510.20808) | UZH / NVIDIA / UW | 整理 sim-to-real 落差來源與對策的綜述 | ARCRAS 2026 | 55 | 未公開 |
| 主流 | 引用、Star、HF | 2025 | [GigaWorld-0](https://arxiv.org/abs/2511.19861) · [專案頁](https://giga-world-0.github.io/) | GigaAI | 影片生成加 3D 生成的世界模型作為 VLA 資料引擎 | arXiv | 54 | [1,617](https://github.com/open-gigaai/giga-world-0) |
| 主流 | 引用 | 2025 | [Vid2Sim](https://arxiv.org/abs/2501.06693) · [專案頁](https://metadriverse.github.io/vid2sim/) | UCLA / UIUC | 從影片重建可互動 3DGS 城市環境訓練導航 | CVPR 2025 | 51 | [292](https://github.com/Vid2Sim/Vid2Sim) |
| 主流 | 引用、機構 | 2025 | [Scalable Real2Sim](https://arxiv.org/abs/2503.00370) · [專案頁](https://scalable-real2sim.github.io/) | MIT | 機器人抓放自動辨識幾何與慣性參數產生模擬資產 | IROS 2025 | 48 | [165](https://github.com/nepfaff/scalable-real2sim) |
| 主流 | 引用 | 2025 | [ArticulatedGS](https://arxiv.org/abs/2503.08135) | USTC / NUDT | 兩種關節狀態影像自監督重建關節物件 3DGS | CVPR 2025 | 46 | 未公開 |
| 主流 | 引用 | 2025 | [DRAWER](https://arxiv.org/abs/2504.15278) · [專案頁](https://drawer-art.github.io/) | UIUC / UW / AI2 等 | 單段影片轉成可互動關節的照片級室內環境 | CVPR 2025 | 40 | [174](https://github.com/xiahongchi/DRAWER) |
| 主流 | 引用、Star、HF | 2025 | [Lyra](https://arxiv.org/abs/2509.19296) · [專案頁](https://research.nvidia.com/labs/toronto-ai/lyra/) | NVIDIA / Toronto / Vector 等 | 影片擴散模型自蒸餾成 3DGS 場景生成 | arXiv | 39 | [2,763](https://github.com/nv-tlabs/lyra) |
| 主流 | 引用 | 2025 | [MetaScenes](https://arxiv.org/abs/2505.02388) · [專案頁](https://meta-scenes.github.io/) | BIGAI | 自動把真實掃描物件替換成可模擬資產 | CVPR 2025 | 39 | [69](https://github.com/meta-scenes/MetaScenes) |
| 主流 | 引用、推薦 | 2025 | [VR-Robo](https://arxiv.org/abs/2502.01536) · [專案頁](https://vr-robo.github.io/) | Tsinghua | 3DGS 重建場景做視覺導航與運動控制的 real-to-sim-to-real | RA-L 2025 | 36 | [195](https://github.com/zst1406217/VR-Robo) |
| 主流 | 引用、推薦 | 2025 | [GaussGym](https://arxiv.org/abs/2510.15352) | UC Berkeley / ETH / Amazon FAR | 3DGS 嵌入 IsaacGym 向量化渲染，從像素學運動 | arXiv | 33 | 未公開 |
| 主流 | 引用、機構 | 2025 | [GSWorld](https://arxiv.org/abs/2510.20813) · [專案頁](https://3dgsworld.github.io) | UCSD / UCLA / Meta | GSDF 格式結合 3DGS 與物理引擎的閉環操作模擬 | ICRA 2026 | 31 | [230](https://github.com/luccachiang/GSWorld) |
| 主流 | 引用、HF、基準 | 2025 | [InternScenes](https://arxiv.org/abs/2509.10813) · [專案頁](https://marjordcpz.github.io/InternScenes.github.io/) | Shanghai AI Lab / SJTU / Beihang 等 | 含真實佈局與小物件的大規模可模擬室內場景 | NeurIPS 2025 | 31 | [276](https://github.com/InternRobotics/InternScenes) |
| 主流 | Star、推薦 | 2026 | [TripoSplat](https://arxiv.org/abs/2605.16355) | Tsinghua / VAST | 高斯中心由學到的密度取樣，利於生成式建模 | SIGGRAPH 2026 | 4 | [1,398](https://github.com/VAST-AI-Research/TripoSplat) |
| 新興 | 獲獎 | 2022 | [NeRF2Real](https://arxiv.org/abs/2210.04932) | DeepMind | 手機影片建 NeRF 取得接觸幾何與新視角渲染，在模擬中訓練視覺策略後轉移到實機 | ICRA 2023 | 80 | 未公開 |
| 新興 | 推薦 | 2026 | [SimFoundry](https://arxiv.org/abs/2606.28276) · [專案頁](https://research.nvidia.com/labs/gear/simfoundry/) | NVIDIA / Stanford / Georgia Tech / UT Austin 等 | 單支真實場景影片自動拆成遮罩、深度、2D→3D 物件網格與 3DGS 背景並做物理檢查，各模組可隨基礎模型替換，另生成 digital cousins 擴增訓練 | NVIDIA Research、arXiv | 23 | [427](https://github.com/NVlabs/SimFoundry) |
| 新興 | 推薦 | 2026 | [GATOR](https://arxiv.org/abs/2610.11215) · [專案頁](https://research.nvidia.com/labs/lpr/gator/) | NVIDIA / Simon Fraser | 從雜亂場景的隨手拍照片生成完整物件與場景相對位姿，再由 agent 在 Blender 編輯網格、只保留與原圖相符的修改，免重訓生成器 | NVIDIA Research、arXiv | 0 | 未公開 |

### 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [GRASE](https://arxiv.org/abs/2610.21498) | 西安交通大學、福州大學、Adobe、西湖大學 | 把影片當持續參照的 agent 流程：渲染結果與影像不符就回頭修正房間結構與物件擺放，而非一次到底 |  | 未公開 | arXiv |
| 2026-09 | [ReVeal](https://arxiv.org/abs/2609.23910) | Purdue / Samsung SDS | 考慮重建品質的 real-to-sim VLA 策略評估 |  | 未公開 | arXiv |
| 2026-06 | [ArtiTwinSplat](https://arxiv.org/abs/2606.24628) | ETH / Microsoft / Bonn | 手持 RGB-D 影片重建可互動數位分身（3DGS），輸出碰撞網格、門／抽屜關節、URDF，可直接匯入 Isaac Sim |  | 未公開 | arXiv |
| 2026-06 | [Robots Need More than VLA and World Models](https://arxiv.org/abs/2606.06556) | Motoniq.ai / Stanford / ETH 等 | 立場論文；整理 3DGS 模擬器訓練的導航策略可 zero-shot 轉移到實機（SOUS VIDE、SINGER、GRaD-Nav） |  | 未公開 | arXiv |
| 2025-12 | [PolaRiS](https://arxiv.org/abs/2512.16881) · [專案頁](https://polaris-evals.github.io/) | UW / UC Berkeley / Stanford / TRI / Physical Intelligence 等 | 可擴展的 real-to-sim 通用策略評估 |  | [GitHub](https://github.com/arhanjain/polaris) | arXiv |
| 2025-09 | [EmbodiedSplat](https://arxiv.org/abs/2509.17430) · [專案頁](https://gchhablani.github.io/embodied-splat) | Georgia Tech / TRI | 手機掃描建 3DGS 場景，在 Habitat-Sim 裡微調導航策略後部署回實機 |  | [GitHub](https://github.com/gchhablani/embodied-splat-v1) | ICCV 2025 |

## 月報

- [2026-10](digests/2026-10.md)
