<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a7479104914787e4f0976e39131e8e3",
  "translation_date": "2025-04-04T05:31:42+00:00",
  "source_file": "code\\07.Lab\\01\\Apple\\phi3ext\\vsc-extension-quickstart.md",
  "language_code": "tw"
}
-->
# 歡迎使用 VS Code 擴展

## 資料夾內容

* 此資料夾包含所有擴展所需的檔案。
* `package.json` - 這是宣告擴展及命令的清單檔案。
  * 範例插件註冊了一個命令並定義了它的標題和命令名稱。有了這些資訊，VS Code 可以在命令面板中顯示該命令，但目前還不需要載入插件。
* `src/extension.ts` - 這是您提供命令實作的主要檔案。
  * 此檔案匯出了一個名為 `activate` 的函式，該函式會在擴展首次啟動時被呼叫（在此例中是執行命令時）。在 `activate` 函式中，我們呼叫 `registerCommand`。
  * 我們將包含命令實作的函式作為第二個參數傳遞給 `registerCommand`。

## 設定

* 安裝推薦的擴展（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）

## 立即開始使用

* 按 `F5` 開啟一個載入擴展的新視窗。
* 在命令面板中執行您的命令，按下 (`Ctrl+Shift+P` 或 Mac 上的 `Cmd+Shift+P`)，然後輸入 `Hello World`。
* 在 `src/extension.ts` 中設置斷點以偵錯您的擴展。
* 在偵錯主控台中查看擴展的輸出。

## 修改擴展

* 修改 `src/extension.ts` 中的程式碼後，您可以從偵錯工具列重新啟動擴展。
* 您也可以重新載入 (`Ctrl+R` 或 Mac 上的 `Cmd+R`) VS Code 視窗以載入您的更改。

## 探索 API

* 您可以開啟 `node_modules/@types/vscode/index.d.ts` 檔案以查看我們完整的 API 集。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通過 **Tasks: Run Task** 指令執行 "watch" 任務。確保該任務正在執行，否則測試可能無法被發現。
* 從活動列中的測試視圖開啟並點擊 "Run Test" 按鈕，或使用快捷鍵 `Ctrl/Cmd + ; A`。
* 在測試結果視圖中查看測試結果的輸出。
* 修改 `src/test/extension.test.ts` 或在 `test` 資料夾內新增測試檔案。
  * 提供的測試執行工具僅會考慮符合名稱模式 `**.test.ts` 的檔案。
  * 您可以在 `test` 資料夾內建立子資料夾，以任意方式組織您的測試。

## 深入探索

* 通過[打包擴展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)來減少擴展大小並改善啟動時間。
* 在 VS Code 擴展市場上[發布您的擴展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 設置[持續整合](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)以自動化建置流程。

**免責聲明**：  
本文檔使用AI翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀不承擔責任。