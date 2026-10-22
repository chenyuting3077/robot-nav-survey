# 局部導航與規劃（diffusion / world model / 探索）

## 在解決的問題

- 從感測器直接輸出可行軌跡，取代手調的代價地圖與規劃器參數。
- 泛化到沒見過的環境與機體：靠跨機體資料或大規模模擬訓練。
- 多解行為（岔路要選一邊）用 diffusion 表達；預測動作後果再規劃則走向 world model。
- 安全保證：學習式策略沒有碰撞保證，常另外疊安全濾波器。

## 最新論文

| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10 | [Physical AI for Intralogistics](https://arxiv.org/abs/2610.28432) | Idealworks / NVIDIA | 把 NVIDIA X-Mobility 與 COMPASS 導航策略放進倉儲數位孿生訓練，再用 Cosmos 生成 sim-to-real 變體資料微調，部署在 Jetson AGX Xavier 差速底盤 | 實機四個場景成功率 65.3%（純模擬訓練）→ 91.7%（加 Cosmos 資料），與量產導航堆疊差 8.3 點 | 未公開 | arXiv |
| 2026-10 | [LiteNWM](https://arxiv.org/abs/2610.12368) | Nanjing Univ. / Imperial / Sony AI | 輕量潛空間 world model，可機上跑 | 實機未見場景 SR 43.3%（NoMaD）→ 83.3% | 未公開 | arXiv |
| 2026-07 | [X-NavDP](https://arxiv.org/abs/2607.28560) · [專案頁](https://yty-sky.github.io/x-navdp-project-page) | Shanghai AI Lab / Fudan / SYSU | NavDP 泛化到新行為與新機體（group Q-score reweighted matching） |  | 未公開 | arXiv |
