<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8d36fc444748a50558d017e8a0772437",
  "translation_date": "2025-04-04T05:28:40+00:00",
  "source_file": "code\\07.Lab\\01\\AIPC\\extensions\\phi3ext\\vsc-extension-quickstart.md",
  "language_code": "tw"
}
-->
# 歡迎使用您的 VS Code 擴展

## 資料夾內容

* 此資料夾包含您的擴展所需的所有檔案。
* `package.json` - 這是宣告擴展和命令的清單檔案。
  * 範例插件註冊了一個命令並定義了它的標題和命令名稱。根據這些資訊，VS Code 能在命令面板中顯示該命令。目前還不需要載入插件。
* `src/extension.ts` - 這是您提供命令實作的主要檔案。
  * 該檔案匯出了一個函數 `activate`，當您的擴展首次啟動時（例如執行命令時）會調用它。在 `activate` 函數內，我們呼叫 `registerCommand`。
  * 我們將包含命令實作的函數作為第二個參數傳遞給 `registerCommand`。

## 設定

* 安裝推薦的擴展（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）。

## 快速啟動

* 按 `F5` 開啟載入擴展的新視窗。
* 從命令面板執行命令，按下 (`Ctrl+Shift+P` 或在 Mac 上按 `Cmd+Shift+P`)，然後輸入 `Hello World`。
* 在 `src/extension.ts` 中設置斷點以調試您的擴展。
* 在除錯主控台中查看擴展的輸出。

## 修改內容

* 修改 `src/extension.ts` 中的程式碼後，您可以從除錯工具列重新啟動擴展。
* 您也可以重新載入 VS Code 視窗 (`Ctrl+R` 或在 Mac 上按 `Cmd+R`) 以載入您的更改。

## 探索 API

* 您可以開啟 `node_modules/@types/vscode/index.d.ts` 檔案來查看完整的 API 集。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)。
* 通過 **Tasks: Run Task** 命令執行 "watch" 任務。確保該任務正在執行，否則可能無法檢測到測試。
* 從活動欄打開測試視圖，點擊 "Run Test" 按鈕，或使用快捷鍵 `Ctrl/Cmd + ; A`。
* 在測試結果視圖中查看測試結果輸出。
* 修改 `src/test/extension.test.ts` 或在 `test` 資料夾中建立新的測試檔案。
  * 提供的測試運行器僅會考慮符合名稱模式 `**.test.ts` 的檔案。
  * 您可以在 `test` 資料夾中建立子資料夾，以任何方式組織您的測試。

## 深入探索

* 透過[打包您的擴展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo)來減少擴展大小並提升啟動速度。
* 在 VS Code 擴展市場上[發布您的擴展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)。
* 設定[持續整合](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo)來自動化構建流程。

**免責聲明**：  
本文檔使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。