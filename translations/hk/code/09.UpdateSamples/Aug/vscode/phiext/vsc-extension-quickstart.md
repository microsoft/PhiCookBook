<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a7479104914787e4f0976e39131e8e3",
  "translation_date": "2025-04-04T17:26:45+00:00",
  "source_file": "code\\09.UpdateSamples\\Aug\\vscode\\phiext\\vsc-extension-quickstart.md",
  "language_code": "hk"
}
-->
# 歡迎使用你的 VS Code 擴展

## 文件夾內容

* 此文件夾包含擴展所需的所有文件。
* `package.json` - 這是聲明你的擴展和指令的清單文件。
  * 範例插件會註冊一個指令並定義其標題和指令名稱。憑藉這些資訊，VS Code 可以在指令面板中顯示該指令，但目前還不需要載入插件。
* `src/extension.ts` - 這是主要文件，提供指令的具體實現。
  * 該文件匯出了一個函數 `activate`，此函數會在擴展首次啟動時被調用（例如執行指令時）。在 `activate` 函數中，我們調用了 `registerCommand`。
  * 我們將包含指令實現的函數作為第二個參數傳遞給 `registerCommand`。

## 設置

* 安裝推薦的擴展（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）。

## 馬上開始使用

* 按 `F5` 打開一個載入了擴展的新窗口。
* 在指令面板中執行你的指令，按下 (`Ctrl+Shift+P` 或 Mac 上的 `Cmd+Shift+P`)，然後輸入 `Hello World`。
* 在 `src/extension.ts` 文件中設置斷點以調試你的擴展。
* 在調試控制台中查看擴展的輸出。

## 修改內容

* 修改 `src/extension.ts` 中的代碼後，可以通過調試工具欄重新啟動擴展。
* 你也可以重新載入 (`Ctrl+R` 或 Mac 上的 `Cmd+R`) VS Code 窗口來應用你的更改。

## 探索 API

* 打開文件 `node_modules/@types/vscode/index.d.ts` 即可查看完整的 API 集。

## 運行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)。
* 通過 **Tasks: Run Task** 指令運行 "watch" 任務。確保此任務正在運行，否則可能無法找到測試。
* 從活動欄中的測試視圖打開並點擊 "Run Test" 按鈕，或使用快捷鍵 `Ctrl/Cmd + ; A`。
* 在測試結果視圖中查看測試結果輸出。
* 修改 `src/test/extension.test.ts` 或在 `test` 文件夾內創建新的測試文件。
  * 提供的測試運行器只會考慮符合命名模式 `**.test.ts` 的文件。
  * 你可以在 `test` 文件夾內創建子文件夾，按任意結構組織你的測試。

## 更深入的操作

* [打包你的擴展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)，減少擴展大小並提升啟動速度。
* 在 VS Code 擴展市場上 [發布你的擴展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 通過設置 [持續集成](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) 自動化構建流程。

**免責聲明**：  
此文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於確保翻譯準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。