<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-08T06:47:23+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "tw"
}
-->
# 歡迎使用你的 VS Code 擴充功能

## 資料夾裡有什麼

* 這個資料夾包含你擴充功能所需的所有檔案。
* `package.json` - 這是宣告你的擴充功能和指令的 manifest 檔案。
  * 範例外掛會註冊一個指令，並定義它的標題和指令名稱。藉由這些資訊，VS Code 可以在指令選單中顯示該指令，但此時還不需要載入外掛。
* `src/extension.ts` - 這是主要檔案，你會在這裡實作你的指令。
  * 該檔案匯出一個函式 `activate`，它會在擴充功能第一次啟動時被呼叫（在這個案例中是執行指令時）。在 `activate` 函式裡，我們會呼叫 `registerCommand`。
  * 我們把包含指令實作的函式當作第二個參數傳給 `registerCommand`。

## 設定

* 安裝建議的擴充功能（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner、和 dbaeumer.vscode-eslint）

## 立即開始使用

* 按 `F5` 開啟一個載入你擴充功能的新視窗。
* 從指令選單執行你的指令，按下 (`Ctrl+Shift+P` 或 Mac 上的 `Cmd+Shift+P`) 並輸入 `Hello World`。
* 在 `src/extension.ts` 裡的程式碼中設置中斷點來除錯你的擴充功能。
* 在除錯主控台查看你的擴充功能輸出。

## 修改程式碼

* 修改 `src/extension.ts` 後，可以從除錯工具列重新啟動擴充功能。
* 你也可以重新載入 (`Ctrl+R` 或 Mac 上的 `Cmd+R`) VS Code 視窗，讓擴充功能載入你的變更。

## 探索 API

* 開啟 `node_modules/@types/vscode/index.d.ts` 檔案即可查看完整的 API。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 透過 **Tasks: Run Task** 指令執行 "watch" 任務。請確保它正在執行，否則測試可能無法被偵測到。
* 從活動列開啟測試檢視，點擊「Run Test」按鈕，或使用快捷鍵 `Ctrl/Cmd + ; A`
* 在測試結果檢視中查看測試輸出。
* 修改 `src/test/extension.test.ts` 或在 `test` 資料夾內建立新的測試檔案。
  * 提供的測試執行器只會考慮符合 `**.test.ts` 命名規則的檔案。
  * 你可以在 `test` 資料夾內建立子資料夾，自由組織你的測試。

## 更進一步

* 透過[打包你的擴充功能](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)來減少擴充功能大小並提升啟動速度。
* 在 VS Code 擴充功能市集[發佈你的擴充功能](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 設定[持續整合](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)來自動化建置流程。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不精確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生之任何誤解或誤釋負責。