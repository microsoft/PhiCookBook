<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-08T04:53:00+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "hk"
}
-->
# Contributing

呢個項目歡迎大家提供貢獻同建議。大部分貢獻都需要你同意一份Contributor License Agreement (CLA)，聲明你有權利並確實授權我哋使用你嘅貢獻。詳情請瀏覽 [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

當你提交pull request嘅時候，CLA機械人會自動判斷你係咪需要提供CLA，並且適當標示PR（例如狀態檢查、評論）。只需要跟住機械人嘅指示做就得。所有用緊我哋CLA嘅repo，你只需要做一次。

## Code of Conduct

呢個項目採用咗[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)。
想知多啲，可以睇[Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)或者發電郵去[opencode@microsoft.com](mailto:opencode@microsoft.com)查詢。

## Cautions for creating issues

唔好用GitHub issues嚟問一般支援問題，因為GitHub嘅issues主要用嚟提交功能請求同埋錯誤報告。咁樣我哋可以更容易追蹤實際嘅問題或錯誤，亦可以將一般討論同代碼問題分開。

## How to Contribute

### Pull Requests Guidelines

當你向Phi-3 CookBook嘅repo提交pull request (PR)時，請跟以下指引：

- **Fork Repository**：改動之前，記住先fork個repo到自己帳戶。

- **分開pull requests (PR)**：
  - 每種改動應該分開用唔同嘅PR提交。例如，錯誤修正同文檔更新要分開。
  - 打錯字修正同細微文檔更新可以合併成一個PR。

- **處理合併衝突**：如果你嘅PR出現合併衝突，請先更新本地`main`分支，令佢同主repo同步，然後再做改動。

- **翻譯提交**：提交翻譯PR時，要確保翻譯資料夾包含咗原始資料夾所有檔案嘅翻譯。

### Translation Guidelines

> [!IMPORTANT]
>
> 喺呢個repo做翻譯唔好用機械翻譯。只接受對該語言有能力嘅義工幫手翻譯。

如果你熟識非英語語言，可以幫手翻譯內容。為咗確保翻譯嘅貢獻能夠順利整合，請跟以下指引：

- **建立翻譯資料夾**：去相應章節資料夾，為你翻譯嘅語言建立翻譯資料夾。例如：
  - 導言章節：`PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - 快速入門章節：`PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - 其他章節如03.Inference、04.Finetuning等等，依此類推。

- **更新相對路徑**：翻譯時，調整markdown檔案內相對路徑，喺路徑開頭加`../../`，確保連結正確。例如：
  - 將`(../../imgs/01/phi3aisafety.png)`改成`(../../../../imgs/01/phi3aisafety.png)`

- **整理翻譯檔案**：每個翻譯檔案應該放喺對應章節嘅翻譯資料夾。例如，如果你係翻譯導言章節成西班牙文，就係咁做：
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **提交完整PR**：確保一個章節嘅所有翻譯檔案都包含喺一個PR度。我哋唔接受章節嘅部分翻譯。提交翻譯PR時，請確保翻譯資料夾包含咗原始資料夾所有檔案嘅翻譯。

### Writing Guidelines

為咗確保所有文件嘅一致性，請跟以下指引：

- **URL格式**：所有URL要用中括號包住，再用括號包住URL，兩邊唔好有多餘空格。例如：`[example](https://www.microsoft.com)`。

- **相對連結**：指向當前目錄嘅檔案或資料夾，請用`./`；指向父目錄嘅用`../`。例如：`[example](../../path/to/file)`或者`[example](../../../path/to/file)`。

- **唔好用國家特定嘅語言代碼**：連結唔好帶有國家特定嘅locale，例如避免`/en-us/`或者`/en/`。

- **圖片儲存**：所有圖片放喺`./imgs`資料夾。

- **圖片命名要描述性**：用英文字符、數字同連字號命名。例如：`example-image.jpg`。

## GitHub Workflows

當你提交pull request，以下workflow會被觸發，用嚟驗證改動。請跟指示確保你嘅PR通過檢查：

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

呢個workflow會確保你檔案入面所有相對路徑都正確。

1. 用VS Code檢查連結：
    - 將滑鼠移到任何連結上。
    - 按**Ctrl + Click**去打開連結。
    - 如果連結喺本地唔work，就會觸發workflow，GitHub度都唔work。

1. 用VS Code嘅路徑建議修正問題：
    - 輸入`./`或者`../`。
    - VS Code會提示你揀選合適嘅路徑。
    - 按選定檔案或資料夾，確保路徑正確。

加咗正確路徑後，記得儲存同推送改動。

### Check URLs Don't Have Locale

呢個workflow確保所有web URL冇帶有國家特定嘅locale。因為呢個repo係全球可用，URL唔應該包含你嘅國家locale。

1. 檢查URL唔帶國家locale：
    - 搜尋URL入面有冇`/en-us/`、`/en/`或者其他語言locale。
    - 冇嘅話就通過檢查。

1. 修正方法：
    - 打開workflow標示嘅檔案路徑。
    - 將URL入面嘅國家locale移除。

移除locale後，記得儲存同推送改動。

### Check Broken Urls

呢個workflow確保你檔案入面嘅web URL正常運作，返回200狀態碼。

1. 驗證URL狀態：
    - 檢查檔案入面URL嘅狀態。

2. 修正壞URL：
    - 打開有問題嘅URL所在檔案。
    - 更新URL到正確嘅。

修正完URL後，記得儲存同推送改動。

> [!NOTE]
>
> 有時URL檢查會失敗，但連結其實可以打開。原因可能包括：
>
> - **網絡限制**：GitHub actions伺服器可能有限制，阻止存取某啲URL。
> - **超時問題**：URL響應太耐，workflow會報超時錯誤。
> - **暫時伺服器問題**：伺服器偶爾停機或維護，驗證時URL暫時無法使用。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋努力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原文文件嘅母語版本應被視為權威來源。對於重要資料，建議採用專業人工翻譯。對於因使用本翻譯而引致嘅任何誤解或誤釋，我哋概不負責。