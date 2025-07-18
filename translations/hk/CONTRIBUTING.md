<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-16T14:37:18+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hk"
}
-->
# Contributing

本項目歡迎各位貢獻及提出建議。大部分貢獻都需要您同意一份
Contributor License Agreement (CLA)，聲明您有權利並確實授權我們使用您的貢獻。詳情請參閱 [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

當您提交 pull request 時，CLA 機械人會自動判斷您是否需要提供 CLA，並在 PR 上做出相應標示（例如狀態檢查、留言）。只要按照機械人提供的指示操作即可。您只需在所有使用我們 CLA 的倉庫中完成一次此流程。

## Code of Conduct

本項目已採用 [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)。
欲了解更多資訊，請閱讀 [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) 或透過 [opencode@microsoft.com](mailto:opencode@microsoft.com) 聯絡我們，提出任何額外問題或意見。

## Cautions for creating issues

請勿因一般支援問題而開啟 GitHub issue，GitHub 問題列表應用於功能請求及錯誤回報。如此一來，我們能更有效追蹤程式碼中的實際問題或錯誤，並將一般討論與程式碼問題分開。

## How to Contribute

### Pull Requests Guidelines

提交 pull request (PR) 至 Phi-3 CookBook 倉庫時，請遵循以下指引：

- **Fork 倉庫**：在進行修改前，請先將倉庫 fork 到您自己的帳號。

- **分開提交不同類型的 PR**：
  - 每種修改類型請分別提交 PR。例如，錯誤修正與文件更新應分開提交。
  - 拼字錯誤修正及小幅文件更新可視情況合併成一個 PR。

- **處理合併衝突**：若您的 PR 顯示有合併衝突，請先更新本地的 `main` 分支，使其與主倉庫同步，再進行修改。

- **翻譯提交**：提交翻譯 PR 時，請確保翻譯資料夾包含原始資料夾中所有檔案的翻譯。

### Writing Guidelines

為確保所有文件風格一致，請遵守以下指引：

- **URL 格式**：所有 URL 請用中括號包住文字，後接小括號包住網址，中間及內部不留空格。例如：`[example](https://www.microsoft.com)`。

- **相對連結**：指向當前目錄的檔案或資料夾，請使用 `./`；指向上層目錄的，請使用 `../`。例如：`[example](../../path/to/file)` 或 `[example](../../../path/to/file)`。

- **非國家特定語系**：請勿在連結中包含國家特定語系，如 `/en-us/` 或 `/en/`。

- **圖片存放**：所有圖片請存放於 `./imgs` 資料夾。

- **圖片命名**：圖片名稱請具描述性，使用英文字母、數字及連字號。例如：`example-image.jpg`。

## GitHub Workflows

當您提交 pull request 時，以下工作流程會被觸發以驗證您的修改。請依照下列指示確保您的 PR 通過檢查：

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

此工作流程確保您檔案中的所有相對路徑皆正確。

1. 請使用 VS Code 執行以下操作，確認連結是否正常：
    - 將滑鼠移至檔案中的任一連結上方。
    - 按下 **Ctrl + 點擊** 以跳轉連結。
    - 若本地點擊連結無法正常開啟，該連結會觸發工作流程錯誤，且在 GitHub 上也無法使用。

1. 若發現問題，請依照 VS Code 提供的路徑建議修正：
    - 輸入 `./` 或 `../`。
    - VS Code 會根據您輸入的內容提示可選擇的檔案或資料夾。
    - 點擊所需檔案或資料夾，確保路徑正確。

修正完相對路徑後，請儲存並推送您的修改。

### Check URLs Don't Have Locale

此工作流程確保所有網頁 URL 不包含國家特定語系。由於本倉庫全球可訪問，確保 URL 不含您所在國家的語系非常重要。

1. 請檢查您的 URL 是否包含以下文字：

    - `/en-us/`、`/en/` 或其他語言語系代碼。
    - 若 URL 中沒有這些字串，即可通過此檢查。

1. 若有問題，請依照以下步驟修正：
    - 開啟工作流程標示的檔案路徑。
    - 移除 URL 中的國家語系部分。

移除後，請儲存並推送您的修改。

### Check Broken Urls

此工作流程確保您檔案中的所有網頁 URL 都能正常運作並回傳 200 狀態碼。

1. 請檢查檔案中 URL 的狀態是否正常。

2. 若發現壞掉的 URL，請依照以下步驟修正：
    - 開啟包含壞掉 URL 的檔案。
    - 更新 URL 為正確的連結。

修正後，請儲存並推送您的修改。

> [!NOTE]
>
> 有時候 URL 檢查可能會失敗，但連結實際上仍可使用。這可能是因為：
>
> - **網路限制**：GitHub actions 伺服器可能有網路限制，無法存取某些 URL。
> - **逾時問題**：回應時間過長的 URL 可能會觸發逾時錯誤。
> - **暫時性伺服器問題**：伺服器偶爾維護或故障，可能導致驗證期間 URL 暫時無法使用。

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。