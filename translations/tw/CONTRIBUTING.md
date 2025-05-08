<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-08T04:55:38+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tw"
}
-->
# Contributing

這個專案歡迎各種貢獻和建議。大部分的貢獻都需要你同意一份Contributor License Agreement (CLA)，聲明你有權利且確實授權我們使用你的貢獻。詳細資訊請參考 [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

當你提交 pull request 時，CLA bot 會自動判斷你是否需要提供 CLA，並且在 PR 上做相應標記（例如狀態檢查、留言）。只要依照機器人的指示操作即可。使用我們的 CLA 的所有 repos 只需要做一次。

## Code of Conduct

本專案已採用 [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)。  
更多資訊請參考 [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) 或透過 [opencode@microsoft.com](mailto:opencode@microsoft.com) 聯絡我們，有任何問題或建議都歡迎提出。

## Cautions for creating issues

請不要在 GitHub 上開一般支援問題的 issue，因為 GitHub issue 列表應該用來提交功能需求和錯誤回報。這樣我們才能更有效率地追蹤程式碼上的真正問題或錯誤，並將一般討論和程式碼相關的問題區分開來。

## How to Contribute

### Pull Requests Guidelines

提交 Phi-3 CookBook repository 的 pull request (PR) 時，請遵循以下準則：

- **Fork Repository**：請先將 repository fork 到自己的帳號，再進行修改。

- **分開提交 PR**：
  - 不同類型的修改請分開提交 PR，例如錯誤修正和文件更新應該分開。
  - 拼字錯誤和小幅度文件更新可視情況合併成一個 PR。

- **處理合併衝突**：如果 PR 出現合併衝突，請先更新本地 `main` 分支，使其與主 repository 保持一致，再進行修改。

- **翻譯提交**：提交翻譯 PR 時，請確保翻譯資料夾包含原始資料夾中所有檔案的翻譯。

### Translation Guidelines

> [!IMPORTANT]
>
> 翻譯本 repository 的內容時，請勿使用機器翻譯。只有在你精通該語言的情況下，才可自願協助翻譯。

如果你精通非英文語言，歡迎協助翻譯內容。請依照以下步驟確保翻譯能正確整合：

- **建立翻譯資料夾**：進入對應章節資料夾，建立該語言的翻譯資料夾。例如：
  - 介紹章節：`PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - 快速入門章節：`PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - 其他章節（03.Inference、04.Finetuning 等）依此類推。

- **更新相對路徑**：翻譯時，請在 markdown 檔案中相對路徑前加上 `../../`，以確保連結正確。例如：
  - 將 `(../../imgs/01/phi3aisafety.png)` 改為 `(../../../../imgs/01/phi3aisafety.png)`。

- **整理翻譯檔案**：每個翻譯檔案都應放在對應章節的翻譯資料夾。例如，若翻譯介紹章節成西班牙語，資料夾結構應為：
  - `PhiCookBook/md/01.Introduce/translations/es/`。

- **提交完整 PR**：請確保一個章節的所有翻譯檔案都包含在同一個 PR 中。我們不接受章節的部分翻譯。提交翻譯 PR 時，請確保翻譯資料夾內包含原始資料夾中所有檔案的翻譯。

### Writing Guidelines

為了確保所有文件的一致性，請遵守以下規範：

- **URL 格式**：所有 URL 請用中括號包住，後面緊接小括號，且中間不要有空白。例如：`[example](https://www.microsoft.com)`。

- **相對連結**：使用 `./` 指向當前目錄的檔案或資料夾，使用 `../` 指向上層目錄。例如：`[example](../../path/to/file)` 或 `[example](../../../path/to/file)`。

- **非國家特定語系**：請確保連結中不包含國家特定的語系標示，例如避免 `/en-us/` 或 `/en/`。

- **圖片儲存**：所有圖片請放在 `./imgs` 資料夾。

- **圖片命名**：圖片名稱請用英文、數字和連字號，且具描述性。例如：`example-image.jpg`。

## GitHub Workflows

當你提交 pull request 時，會觸發以下工作流程來驗證變更。請依照下面說明確保你的 PR 能通過檢查：

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

此工作流程確保檔案中所有相對路徑皆正確。

1. 請使用 VS Code 進行以下操作以確認連結正常：
    - 將滑鼠移到檔案中任一連結上。
    - 按住 **Ctrl + Click** 以跳轉連結。
    - 若本地點擊連結無法跳轉，會觸發此工作流程，且在 GitHub 上連結也無法使用。

1. 若發現問題，請依 VS Code 建議的路徑修正：
    - 輸入 `./` 或 `../`。
    - VS Code 會根據輸入提供可選擇的路徑。
    - 點選正確的檔案或資料夾，確保路徑無誤。

修改完成後，請儲存並推送變更。

### Check URLs Don't Have Locale

此工作流程確保所有網路 URL 不包含國家特定的語系標示。因為此 repository 是全球可用，確保 URL 不帶有你所在國家的語系很重要。

1. 請檢查 URL 是否包含類似 `/en-us/`、`/en/` 或其他語系標示。
    - 若 URL 中沒有上述語系標示，即可通過檢查。

1. 若發現問題，請依工作流程提示開啟相關檔案並移除 URL 中的國家語系。

移除後，請儲存並推送變更。

### Check Broken Urls

此工作流程確保檔案中的所有網路 URL 都能正常運作且回傳 200 狀態碼。

1. 請檢查檔案中的 URL 狀態是否正常。

2. 若有壞掉的 URL，請打開該檔案並更新為正確的 URL。

修正完成後，請儲存並推送變更。

> [!NOTE]
>
> 可能會有 URL 檢查失敗但連結仍可用的情況，原因包括：
>
> - **網路限制**：GitHub Actions 伺服器可能有網路限制，無法存取某些 URL。
> - **逾時問題**：回應時間過長的 URL 可能會觸發逾時錯誤。
> - **暫時性伺服器問題**：偶爾伺服器維護或故障，可能導致 URL 在驗證時暫時無法使用。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們致力於準確性，但請注意自動翻譯可能會包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生之任何誤解或誤譯負責。