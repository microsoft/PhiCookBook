<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a7479104914787e4f0976e39131e8e3",
  "translation_date": "2025-04-04T05:36:42+00:00",
  "source_file": "code\\09.UpdateSamples\\Aug\\vscode\\phiext\\vsc-extension-quickstart.md",
  "language_code": "tw"
}
-->
# 歡迎使用您的 VS Code 擴展

## 資料夾內容

* 此資料夾包含所有擴展所需的檔案。
* `package.json` - 這是宣告您的擴展和命令的清單檔案。
  * 範例插件註冊了一個命令並定義了它的標題和命令名稱。透過這些資訊，VS Code 可以在命令面板中顯示該命令。目前還不需要載入插件。
* `src/extension.ts` - 這是您提供命令實作的主要檔案。
  * 此檔案匯出了一個函式 `activate`，當您的擴展第一次被啟動時（例如執行命令）會被呼叫。在 `activate` 函式內，我們呼叫了 `registerCommand`。
  * 我們將包含命令實作的函式作為第二個參數傳遞給 `registerCommand`。

## 設定

* 安裝推薦的擴展（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）

## 立即開始使用

* 按 `F5` 開啟一個載入了擴展的新視窗。
* 從命令面板執行您的命令，按下 `Ctrl+Shift+P` 或 `Cmd+Shift+P`（Mac 上）並輸入 `Hello World`。
* 在 `src/extension.ts` 中設定斷點以偵錯您的擴展。
* 在偵錯主控台中找到您的擴展輸出。

## 進行修改

* 修改 `src/extension.ts` 中的程式碼後，可以從偵錯工具列重新啟動擴展。
* 您也可以重新載入 (`Ctrl+R` 或 `Cmd+R` 在 Mac 上) VS Code 視窗以載入修改後的擴展。

## 探索 API

* 開啟 `node_modules/@types/vscode/index.d.ts` 檔案即可查看完整的 API。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 透過 **Tasks: Run Task** 命令執行 "watch" 任務。確保任務正在執行，否則可能無法發現測試。
* 從活動欄中打開 Testing 檢視，點擊 "Run Test" 按鈕，或使用快捷鍵 `Ctrl/Cmd + ; A`。
* 在 Test Results 檢視中查看測試結果輸出。
* 修改 `src/test/extension.test.ts` 或在 `test` 資料夾中建立新的測試檔案。
  * 提供的測試執行器僅會考慮檔名符合 `**.test.ts` 格式的檔案。
  * 您可以在 `test` 資料夾內建立子資料夾，以任何您想要的方式組織測試。

## 深入探索

* [打包您的擴展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)，減少擴展大小並提升啟動速度。
* 在 VS Code 擴展市場上 [發布您的擴展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 設置 [持續整合](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) 以自動化構建流程。

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不精確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議尋求專業的人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋不承擔責任。