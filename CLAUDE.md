# Robot Nav Survey

- 加論文、擴充重要論文、新增主題時，先用 Skill 工具呼叫 `update-survey`（`.claude/skills/update-survey/`）。
- README 由 `scripts/build_readme.py` 產生，改 `topics/`、`data/`、`digests/` 後重跑，不手改 README。
- 一律用繁體中文（台灣用語）；commit message 用英文、conventional 前綴（`docs: ...`）。
- 範圍：AMR（輪式）、四足、輪足的導航，以及機器人用得到的視覺、3D 感知、SLAM、Real2Sim。純操作（manipulation）、純人形全身控制、純自駕不收，除非方法可直接用在上述機體。

## 主題邊界

一篇只放一個主題，以主要貢獻判斷：

- `vln.md`：用語言或高階目標下指令的導航，含導航基礎模型、VLA。
- `local-nav.md`：從感測器到軌跡或速度的局部導航策略（diffusion、world model、RL）。
- `semantic-map.md`：給導航查詢用的語意地圖、場景圖。
- `quadruped.md` / `wheel-legged.md`：該機體特有的運動控制與導航。
- `slam.md`：SLAM、VO、LIO、重定位、回環。
- `perception-3d.md`：深度估計、feed-forward 3D 重建、occupancy；沒有做定位的才放這裡，有做的放 slam。
- `spatial.md`：3D 偵測、3D 實例分割、3D grounding、空間推理 VLM 與其 benchmark。以單一場景的理解為主；要累積成給導航查詢的地圖才放 semantic-map。純自駕的室外 LiDAR／BEV 偵測不收。
- `vision.md`：2D 偵測、分割、追蹤、視覺基礎模型。
- `real2sim.md`：把真實場景重建成可模擬、可訓練或可評估策略的環境。
