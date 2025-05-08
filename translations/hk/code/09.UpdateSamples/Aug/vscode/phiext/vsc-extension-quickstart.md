<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-08T06:47:04+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "hk"
}
-->
# 歡迎使用你的 VS Code 擴充功能

## 資料夾內有咩

* 呢個資料夾包含你擴充功能所需嘅所有檔案。
* `package.json` - 呢個係 manifest 檔案，喺度你會宣告你嘅擴充功能同指令。
  * 呢個範例外掛會註冊一個指令，並定義佢嘅標題同指令名稱。VS Code 就可以喺指令面板顯示呢個指令，仲未需要載入外掛。
* `src/extension.ts` - 呢個係主要檔案，你會喺度實作你嘅指令。
  * 呢個檔案匯出咗一個函數 `activate`，係你擴充功能第一次啟動嘅時候會被呼叫（今次係執行指令時）。喺 `activate` 函數入面，我哋會呼叫 `registerCommand`。
  * 我哋會將包含指令實作嘅函數作為第二個參數傳畀 `registerCommand`。

## 設定

* 安裝建議嘅擴充功能（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 同 dbaeumer.vscode-eslint）

## 即刻開始用

* 撳 `F5` 開新視窗，並載入你嘅擴充功能。
* 喺指令面板用 `Ctrl+Shift+P` 或 Mac 上嘅 `Cmd+Shift+P` 撳，再打 `Hello World` 來執行你嘅指令。
* 喺 `src/extension.ts` 裡面嘅程式碼設定斷點，方便除錯你嘅擴充功能。
* 喺除錯主控台睇你擴充功能嘅輸出。

## 做修改

* 喺 `src/extension.ts` 改完程式碼後，可以喺除錯工具列重新啟動擴充功能。
* 你亦可以喺 VS Code 視窗用 `Ctrl+R` 或 Mac 上嘅 `Cmd+R` 重新載入，咁就會套用你嘅修改。

## 探索 API

* 打開 `node_modules/@types/vscode/index.d.ts` 檔案就可以睇到我哋完整嘅 API。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 用 **Tasks: Run Task** 指令執行「watch」任務。記住要保持佢運行，否則測試可能搵唔到。
* 喺活動列開啟測試視圖，撳「Run Test」按鈕，或者用快捷鍵 `Ctrl/Cmd + ; A`。
* 喺測試結果視圖睇測試結果嘅輸出。
* 喺 `src/test/extension.test.ts` 改測試，或者喺 `test` 資料夾新增測試檔案。
  * 提供嘅測試執行器只會認得符合 `**.test.ts` 命名模式嘅檔案。
  * 你可以喺 `test` 裡面建立資料夾，按你想要嘅方式組織測試。

## 更進一步

* 透過 [打包你嘅擴充功能](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) 減少擴充功能大小同提升啟動速度。
* 喺 VS Code 擴充功能市集 [發佈你嘅擴充功能](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 設定 [持續整合](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) 來自動化建置。

**免責聲明**：  
本文件係用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋致力確保準確性，但請注意，自動翻譯可能會包含錯誤或不準確之處。原文（以原語言版本為準）應被視為具權威性嘅版本。如涉及重要資訊，建議使用專業人工翻譯。我哋對因使用此翻譯而引起嘅任何誤解或誤譯概不負責。