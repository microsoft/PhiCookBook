<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-08T06:45:42+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "tw"
}
-->
# 歡迎使用你的 VS Code 擴充功能

## 資料夾內容

* 這個資料夾包含你擴充功能所需的所有檔案。
* `package.json` - 這是宣告擴充功能和指令的清單檔。
  * 範例外掛會註冊一個指令並定義它的標題和指令名稱。透過這些資訊，VS Code 可以在指令選單中顯示該指令，還不需要載入外掛。
* `src/extension.ts` - 這是主要檔案，你會在這裡實作你的指令。
  * 這個檔案匯出一個函式 `activate`，當你的擴充功能第一次被啟用（在這裡是執行指令時）會呼叫它。在 `activate` 函式裡，我們呼叫 `registerCommand`。
  * 我們把包含指令實作的函式當作第二個參數傳給 `registerCommand`。

## 設定

* 安裝推薦的擴充功能（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）

## 立即開始使用

* 按 `F5` 開啟一個新視窗並載入你的擴充功能。
* 從指令選單執行你的指令，按下（Mac 上是 `Ctrl+Shift+P` 或 `Cmd+Shift+P`）並輸入 `Hello World`。
* 在 `src/extension.ts` 裡設定斷點來除錯你的擴充功能。
* 在除錯主控台查看擴充功能的輸出。

## 進行修改

* 修改 `src/extension.ts` 裡的程式碼後，可以從除錯工具列重新啟動擴充功能。
* 你也可以重新載入（Mac 上是 `Ctrl+R` 或 `Cmd+R`）VS Code 視窗來套用擴充功能的變更。

## 探索 API

* 打開 `node_modules/@types/vscode/index.d.ts` 檔案即可查看完整的 API。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 使用 **Tasks: Run Task** 指令執行「watch」任務。請確保它正在執行，否則測試可能無法被偵測到。
* 從活動列開啟測試視圖，點選「Run Test」按鈕，或使用快速鍵 `Ctrl/Cmd + ; A`。
* 在測試結果視圖中查看測試輸出。
* 修改 `src/test/extension.test.ts` 或在 `test` 資料夾裡新增測試檔案。
  * 提供的測試執行器只會執行符合 `**.test.ts` 命名規則的檔案。
  * 你可以在 `test` 資料夾裡建立子資料夾，依照你想要的方式組織測試。

## 進階操作

* 透過[打包你的擴充功能](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)來減少擴充功能大小並提升啟動速度。
* 在 VS Code 擴充功能市集[發佈你的擴充功能](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 設定[持續整合](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)來自動化建置流程。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。本公司不對因使用本翻譯所產生之任何誤解或誤釋負責。