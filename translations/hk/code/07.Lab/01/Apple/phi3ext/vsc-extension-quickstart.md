<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-08T06:45:24+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "hk"
}
-->
# 歡迎使用你的 VS Code 擴充功能

## 資料夾內容

* 呢個資料夾包含你擴充功能所需嘅所有檔案。
* `package.json` - 呢個係 manifest 檔案，你喺度宣告你嘅擴充功能同指令。
  * 呢個範例外掛會註冊一個指令，並定義佢嘅標題同指令名稱。VS Code 可以用呢啲資料喺指令面板顯示該指令，暫時未需要載入外掛。
* `src/extension.ts` - 呢個係主要檔案，你會喺度實作你嘅指令。
  * 呢個檔案會輸出一個函式 `activate`，當擴充功能第一次被啟動（呢個例子係執行指令時）就會呼叫。喺 `activate` 裡面，我哋會呼叫 `registerCommand`。
  * 我哋會將包含指令實作嘅函式作為第二個參數傳入 `registerCommand`。

## 設定

* 安裝推薦嘅擴充功能（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 同 dbaeumer.vscode-eslint）


## 立即開始使用

* 按 `F5` 開啟一個新視窗並載入你嘅擴充功能。
* 喺指令面板執行指令，按 (`Ctrl+Shift+P` 或 Mac 用戶按 `Cmd+Shift+P`) 然後輸入 `Hello World`。
* 喺 `src/extension.ts` 裡面嘅程式碼設定斷點，方便偵錯擴充功能。
* 喺偵錯主控台睇你擴充功能嘅輸出。

## 進行修改

* 喺 `src/extension.ts` 改完程式碼後，可以喺偵錯工具列重新啟動擴充功能。
* 亦可以重新載入 VS Code 視窗（`Ctrl+R` 或 Mac 用戶用 `Cmd+R`）以載入修改。

## 探索 API

* 打開 `node_modules/@types/vscode/index.d.ts` 檔案，就可以睇到我哋嘅完整 API。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 用 **Tasks: Run Task** 指令執行「watch」任務，確保佢係運行中，否則可能搵唔到測試。
* 喺活動欄開啟測試視圖，按「Run Test」按鈕，或者用快捷鍵 `Ctrl/Cmd + ; A`。
* 喺測試結果視圖睇測試輸出。
* 修改 `src/test/extension.test.ts` 或喺 `test` 資料夾新增測試檔案。
  * 提供嘅測試執行器只會識別符合 `**.test.ts` 命名規則嘅檔案。
  * 你可以喺 `test` 資料夾內建立子資料夾，自由組織測試。

## 更進一步

* 透過[打包擴充功能](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)減少擴充功能大小同提升啟動速度。
* 喺 VS Code 擴充功能市集[發佈你嘅擴充功能](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 設定[持續整合](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)自動化建置流程。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我哋努力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原文文件以其母語版本為準。對於重要資料，建議採用專業人工翻譯。我哋對因使用此翻譯而引起嘅任何誤解或誤釋概不負責。