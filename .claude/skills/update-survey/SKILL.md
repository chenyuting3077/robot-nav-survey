---
name: update-survey
description: 更新這個論文整理 repo 時使用：定期（每三天）加新論文、每月擴充重要論文、使用者推薦論文、新增主題。
---
主題邊界與範圍見 CLAUDE.md。

## 定期更新（加新論文）

1. 上次更新日期看最新月報的「最後更新」。
2. 依 `sources.md` 找新論文並篩選。
3. 收錄的論文用 `python3 scripts/enrich.py 輸出.json <arXiv 編號...>` 一次補齊摘要、備註、HF 的程式碼／專案頁、機構。只看到標題、讀不到摘要的，「重點」只寫標題看得出的內容。
4. 依主題加進 `topics/*.md` 的「最新論文」表，新的放最上面。已收過的（以 arXiv ID 或 DOI 判斷，含 `data/classics.csv`）不重複加；有新版本或被接收時更新原列。
5. 在 `digests/YYYY-MM.md`（當月，沒有就建立）加一段本次新增摘要，更新「最後更新」。新月報要有「## 趨勢」段落：2–4 點，觀察到的寫「觀察」，沒驗證的推論寫「推測」；之後列本月新增論文，連到主題檔。
6. 跑 `python3 scripts/build_readme.py`。它會先跑 `scripts/check_data.py`，格式錯就不產生 README，依訊息修資料後重跑。
7. 開 branch `update/YYYY-MM-DD`，commit，開 PR 到 main；不直接推 main。沒有新論文就不開 PR。

完成條件：PR 已開，README 已重新產生；查不到的來源或日期（被擋、429）寫在 PR 說明。

## 擴充重要論文（每月第一次更新、新增主題、使用者推薦時）

1. 跑 `python3 scripts/harvest.py`（先刪 `data/candidates.json` 才會全部重撈；新主題要先加進 `QUERIES` 和 `ANCHORS`）。
2. 逐篇看標題，只留機器人用得到的；CV 類候選很多，生成模型、人像、醫療、遙測、純自駕不收。
3. 用 `scripts/enrich.py` 補資料，寫進 `data/classics.csv`；使用者推薦的一律收，`tags` 加 `推薦`。
4. 「最新論文」中已達引用或 Star 條件的移到 `classics.csv`，並從主題檔刪除該列。
5. 跑 `python3 scripts/fetch_metrics.py` 刷新引用數、star、HF 按讚數，再跑 `python3 scripts/check_data.py`，處理「刊登處待確認」的警告。
6. 一項收錄條件都不符合的移出（條件見 README「怎樣算重要論文」，門檻在 `scripts/harvest.py` 的 `THRESHOLD`）。
7. 產生 README，開 PR。

完成條件：PR 說明列出新增篇數、移出的論文與原因、哪些欄位沒查證。

## 檔案格式

- `topics/*.md` 固定兩段：`## 在解決的問題`（條列）與 `## 最新論文`（表格）。「在解決的問題」只在領域出現新的主要問題或舊問題被解決時改。
- 重要論文只放 `data/classics.csv`，不放主題檔。
  - `id`：arXiv 編號，沒有就寫 `DOI:...`；都沒有（部落格、技術報告）留空並填 `url`。
  - `repo` 只填官方 repo（`owner/name`），沒有留空；`project` 填專案頁，沒有留空。
  - `tags` 是人工判斷的收錄理由：`獲獎`、`基準`、`機構`、`推薦`。「引用」「Star」「HF」由腳本依數據判斷；Science Robotics、T-RO 自動算「獲獎」。
- 刊登處（`venue` 與「來源」欄）以 arXiv 的 Comments／journal_ref、專案頁、會議論文集為準，查不到就寫 `arXiv`，不憑記憶填。格式：會議或期刊縮寫加年份（`RSS 2026`、`RA-L 2026`）；只有預印本寫 `arXiv`；企業發表寫網站（`NVIDIA Research`），同時有 arXiv 就用頓號並列。會議、期刊名不寫進「重點」。年份以期刊卷號或論文集為準，不用 Semantic Scholar 的 arXiv 年份。

## 「最新論文」表格欄位

`| 日期 | 論文 | 機構 | 重點 | 數據 | 程式碼 | 來源 |`

- 日期：arXiv 首次提交或正式發表的年月。
- 論文：`[名稱](arXiv 網址)`，有專案頁就接 ` · [專案頁](網址)`。專案頁通常在 arXiv Comments 或論文首頁註腳；YouTube、新聞稿、個人首頁不算。
- 機構：以 arXiv 摘要頁或論文首頁的作者單位為準。
- 重點：一句話講方法上和前作不同之處，不抄摘要。
- 數據：作者自報的關鍵數字（benchmark + 數值）；沒看到就留空。
- 程式碼：專案頁上的 Code 按鈕也要查。官方 repo 寫 `[GitHub](網址)`；查過 arXiv、論文、專案頁與 GitHub 搜尋都沒有的寫 `未公開`，第三方重現不算。之後釋出時更新。
