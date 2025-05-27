<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-05-27T02:41:07+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hk"
}
-->
# Contributing

呢個項目歡迎大家嘅貢獻同建議。大部分嘅貢獻都需要你同意一份Contributor License Agreement (CLA)，聲明你有權利並且實際授權我哋使用你嘅貢獻。詳情請瀏覽 [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

當你提交 pull request 嘅時候，CLA bot 會自動判斷你係咪需要提供 CLA，並且會適當地標示 PR（例如狀態檢查、評論）。只需跟隨 bot 嘅指示操作即可。你只需要喺所有使用我哋 CLA 嘅倉庫中做一次。

## Code of Conduct

呢個項目已經採用咗 [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)。
想了解更多，可以閱讀 [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) 或者電郵聯絡 [opencode@microsoft.com](mailto:opencode@microsoft.com) 提問或提供意見。

## Cautions for creating issues

請唔好喺 GitHub 開 general support 問題，因為 GitHub 嘅 issue list 係用嚟提交功能請求同埋報告錯誤。咁樣我哋可以更容易追蹤實際嘅問題或者程式錯誤，同時將一般討論同實際程式碼分開。

## How to Contribute

### Pull Requests Guidelines

當你向 Phi-3 CookBook 倉庫提交 pull request (PR) 嘅時候，請遵守以下指引：

- **Fork 倉庫**：喺你修改之前，請先將倉庫 fork 去你自己嘅帳戶。

- **分開嘅 pull requests (PR)**：
  - 每種改動都應該分開提交，例如錯誤修正同文件更新應該係不同嘅 PR。
  - 拼寫錯誤修正同細微嘅文件更新可以合併成一個 PR。

- **處理合併衝突**：如果你嘅 pull request 顯示有合併衝突，請先更新你本地嘅 `main` 分支，使佢同主倉庫保持一致，然後先做修改。

- **翻譯提交**：提交翻譯嘅 PR 時，請確保翻譯資料夾包含原始資料夾所有檔案嘅翻譯。

### Writing Guidelines

為咗確保所有文件嘅一致性，請使用以下指引：

- **URL 格式**：所有 URL 請用方括號包住，跟住用括號括住 URL，內外唔好有多餘空格。例如：`[example](https://www.microsoft.com)`。

- **相對連結**：對於指向當前目錄嘅檔案或資料夾，使用 `./`；對於上層目錄嘅，使用 `../`。例如：`[example](../../path/to/file)` 或 `[example](../../../path/to/file)`。

- **唔好用國家地區特定嘅語言版本**：確保你嘅連結唔包含國家地區特定嘅語言版本，例如避免使用 `/en-us/` 或 `/en/`。

- **圖片儲存**：所有圖片請儲存在 `./imgs` 資料夾。

- **描述性圖片命名**：用英文字符、數字同連字號命名圖片。例如：`example-image.jpg`。

## GitHub Workflows

當你提交 pull request 時，以下工作流程會自動運行以驗證你嘅改動。請跟從以下指示，確保你嘅 PR 通過工作流程檢查：

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

呢個工作流程確保你文件中嘅所有相對路徑都正確。

1. 為咗確保你嘅連結正常，請喺 VS Code 做以下操作：
    - 將滑鼠移到文件中嘅任何連結上。
    - 按 **Ctrl + Click** 跳轉到該連結。
    - 如果你點擊連結但本地唔工作，工作流程就會觸發，GitHub 上亦會無法使用。

1. 為咗修正呢個問題，請用 VS Code 提供嘅路徑建議做以下操作：
    - 輸入 `./` 或 `../`。
    - VS Code 會根據你輸入嘅內容提示可用選項。
    - 按想要嘅文件或資料夾選擇正確路徑。

加咗正確嘅相對路徑後，記得儲存並推送改動。

### Check URLs Don't Have Locale

呢個工作流程確保所有網頁 URL 裡面冇包含國家地區特定嘅語言版本。由於呢個倉庫係全球可訪問，確保 URL 裡面冇你國家地區嘅語言版本好重要。

1. 為咗驗證你嘅 URL 冇包含地區語言版本，請做以下檢查：

    - 搜尋 URL 裡面有冇 `/en-us/`、`/en/` 或其他語言地區代碼。
    - 如果 URL 裡冇呢啲內容，就通過咗檢查。

1. 修正方法：
    - 打開工作流程標示嘅文件路徑。
    - 從 URL 中移除地區語言代碼。

移除地區語言代碼後，記得儲存並推送改動。

### Check Broken Urls

呢個工作流程確保你文件入面嘅所有網頁 URL 都能正常運作，並返回 200 狀態碼。

1. 為咗驗證你嘅 URL 正常運作，請檢查文件中 URL 嘅狀態。

2. 修正損壞 URL 嘅方法：
    - 打開包含損壞 URL 嘅文件。
    - 更新 URL 至正確嘅地址。

修正 URL 後，記得儲存並推送改動。

> [!NOTE]
>
> 有時候 URL 檢查可能會失敗，但連結其實仍然可用。呢啲情況可能因為：
>
> - **網絡限制**：GitHub actions 伺服器可能有限制，阻止訪問某啲 URL。
> - **超時問題**：URL 回應時間太長可能會令工作流程出現超時錯誤。
> - **臨時伺服器問題**：偶爾伺服器維護或停機可能令 URL 喺驗證期間暫時無法使用。

**免責聲明**：  
本文件係用AI翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我哋盡力確保準確，但自動翻譯可能會有錯誤或不準確嘅地方。原始文件嘅母語版本應視為權威來源。對於重要資訊，建議使用專業人工翻譯。我哋對因使用本翻譯而引起嘅任何誤解或錯誤解讀概不負責。