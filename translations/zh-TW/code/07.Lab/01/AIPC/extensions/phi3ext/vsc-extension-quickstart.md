# 歡迎使用您的 VS Code 擴充功能

## 資料夾內容

* 此資料夾包含您擴充功能所需的所有檔案。
* `package.json` - 這是宣告擴充功能和指令的清單檔案。
  * 範例外掛會註冊一個指令並定義其標題和指令名稱。透過這些資訊，VS Code 可以在指令面板中顯示該指令，但尚未需要載入外掛。
* `src/extension.ts` - 這是主要檔案，您會在此實作指令的功能。
  * 該檔案匯出一個函式 `activate`，當擴充功能第一次被啟動時（本例中是執行指令時）會呼叫它。在 `activate` 函式內，我們呼叫 `registerCommand`。
  * 我們將包含指令實作的函式作為第二個參數傳入 `registerCommand`。

## 設定

* 安裝推薦的擴充功能（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）

## 立即開始使用

* 按下 `F5` 開啟一個載入您擴充功能的新視窗。
* 從指令面板（按下 `Ctrl+Shift+P` 或 Mac 上的 `Cmd+Shift+P`）輸入 `Hello World` 執行您的指令。
* 在 `src/extension.ts` 中設定斷點，方便除錯您的擴充功能。
* 在除錯主控台查看擴充功能的輸出。

## 進行修改

* 修改 `src/extension.ts` 中的程式碼後，可以從除錯工具列重新啟動擴充功能。
* 也可以重新載入 VS Code 視窗（`Ctrl+R` 或 Mac 上的 `Cmd+R`）來套用擴充功能的變更。

## 探索 API

* 開啟 `node_modules/@types/vscode/index.d.ts` 檔案，即可查看完整的 API。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 透過 **Tasks: Run Task** 指令執行「watch」任務。請確保此任務正在執行，否則測試可能無法被偵測。
* 從活動列開啟測試視圖，點擊「Run Test」按鈕，或使用快速鍵 `Ctrl/Cmd + ; A`。
* 在測試結果視圖中查看測試輸出。
* 修改 `src/test/extension.test.ts` 或在 `test` 資料夾內新增測試檔案。
  * 提供的測試執行器只會執行符合 `**.test.ts` 命名規則的檔案。
  * 您可以在 `test` 資料夾內建立子資料夾，自由組織測試檔案。

## 進階應用

* 透過[打包您的擴充功能](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo)來減少擴充功能大小並提升啟動速度。
* 在 VS Code 擴充功能市集中[發佈您的擴充功能](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)。
* 設定[持續整合](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo)來自動化建置流程。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。