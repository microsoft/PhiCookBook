<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-05-27T02:41:56+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tw"
}
-->
# Contributing

這個專案歡迎大家的貢獻與建議。大部分的貢獻都需要你同意一份 Contributor License Agreement (CLA)，聲明你有權利並且確實授權我們使用你的貢獻。詳細內容請參考 [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

當你提交 pull request 時，CLA 機器人會自動判斷你是否需要提供 CLA 並在 PR 上做相應標示（例如狀態檢查、留言）。只要照著機器人的指示操作即可。使用我們的 CLA 的所有專案只需要做一次。

## Code of Conduct

本專案已採用 [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)。
更多資訊請參考 [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)，或有其他問題與建議請聯絡 [opencode@microsoft.com](mailto:opencode@microsoft.com)。

## Cautions for creating issues

請勿開 GitHub issue 來詢問一般支援問題，GitHub issue 應用於功能請求與錯誤回報。這樣我們才能更有效率地追蹤真正的程式碼問題或錯誤，並將一般討論與程式碼問題分開。

## How to Contribute

### Pull Requests Guidelines

提交 Phi-3 CookBook 倉庫的 pull request (PR) 時，請遵守以下準則：

- **Fork 倉庫**：在修改之前，請先將倉庫 fork 到自己的帳號。

- **分開的 pull requests (PR)**：
  - 每種修改請分別提交成獨立的 PR，例如錯誤修正與文件更新應分開。
  - 拼字錯誤修正與小幅度文件更新可視情況合併成一個 PR。

- **處理合併衝突**：如果你的 pull request 顯示有合併衝突，請先更新你本地的 `main` 分支，使其與主倉庫同步，再進行修改。

- **翻譯提交**：提交翻譯 PR 時，請確保翻譯資料夾包含原始資料夾中所有檔案的翻譯。

### Writing Guidelines

為了確保所有文件的一致性，請遵守以下規範：

- **URL 格式**：所有 URL 請用中括號包起來，後面接括號，且中間不得有多餘空白。例如：`[example](https://www.microsoft.com)`。

- **相對連結**：指向目前目錄下檔案或資料夾時，使用 `./`；指向上層目錄時，使用 `../`。例如：`[example](../../path/to/file)` 或 `[example](../../../path/to/file)`。

- **非特定國家地區語系**：確保連結中不包含特定國家地區語系，例如避免 `/en-us/` 或 `/en/`。

- **圖片存放**：所有圖片請存放於 `./imgs` 資料夾。

- **圖片命名**：圖片名稱請用英文、數字與連字號描述性命名。例如：`example-image.jpg`。

## GitHub Workflows

當你提交 pull request 時，以下工作流程會被觸發來驗證你的修改。請依照指示確保你的 PR 能通過檢查：

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

此工作流程會確保你檔案中的相對路徑正確無誤。

1. 為了確保連結正常，請使用 VS Code 執行以下步驟：
    - 將滑鼠移到檔案中的連結上。
    - 按 **Ctrl + 點擊** 以跳轉到該連結。
    - 若本地點擊無法開啟，將會觸發工作流程，且在 GitHub 上也無法使用。

1. 若要修正此問題，請使用 VS Code 提供的路徑建議：
    - 輸入 `./` 或 `../`。
    - VS Code 會根據你輸入的內容提示可選擇的檔案或資料夾。
    - 點選正確的檔案或資料夾，確保路徑正確。

加入正確的相對路徑後，請儲存並推送修改。

### Check URLs Don't Have Locale

此工作流程會確保所有網址不包含特定國家地區語系。由於此倉庫是全球可存取，必須確保網址不帶有國家語系。

1. 驗證網址是否包含國家語系，請檢查：

    - 是否有 `/en-us/`、`/en/`，或其他語言地區碼出現在網址中。
    - 若網址中沒有這些內容，即可通過檢查。

1. 若要修正此問題，請：

    - 開啟工作流程標示的檔案路徑。
    - 從網址中移除國家語系。

移除國家語系後，請儲存並推送修改。

### Check Broken Urls

此工作流程會確保你檔案中的所有網頁 URL 都能正常運作並回傳 200 狀態碼。

1. 驗證網址是否正常，請檢查檔案中的 URL 狀態。

2. 若有壞掉的 URL，請：

    - 開啟包含壞掉 URL 的檔案。
    - 將 URL 更新為正確的連結。

修正完 URL 後，請儲存並推送修改。

> [!NOTE]
>
> 有時候即使連結可以正常存取，URL 檢查仍可能失敗，原因包括：
>
> - **網路限制**：GitHub actions 伺服器可能有網路限制，導致無法連到某些網址。
> - **逾時問題**：回應時間過長的網址可能觸發逾時錯誤。
> - **臨時伺服器問題**：伺服器偶爾停機或維護，可能在驗證時造成網址暫時無法使用。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生之任何誤解或誤釋負責。