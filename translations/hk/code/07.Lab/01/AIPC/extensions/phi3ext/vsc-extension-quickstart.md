<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-08T06:43:41+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "hk"
}
-->
# 歡迎使用你的 VS Code 擴充功能

## 資料夾內容

* 呢個資料夾包含咗你擴充功能所需嘅所有檔案。
* `package.json` - 呢個係 manifest 檔案，你會喺度宣告你嘅擴充功能同指令。
  * 呢個示範插件會註冊一個指令，並定義佢嘅標題同指令名稱。VS Code 就可以根據呢啲資料喺指令面板顯示該指令。佢仲未需要即刻載入插件。
* `src/extension.ts` - 呢個係主要檔案，你會喺度提供指令嘅實作。
  * 呢個檔案會匯出一個函數 `activate`，係擴充功能第一次被啟動時（例如執行指令時）會被呼叫。喺 `activate` 函數入面，我哋會呼叫 `registerCommand`。
  * 我哋會將包含指令實作嘅函數作為第二個參數傳入 `registerCommand`。

## 設定

* 安裝建議嘅擴充功能（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 同 dbaeumer.vscode-eslint）

## 立即開始

* 按 `F5` 開啟一個新視窗並載入你嘅擴充功能。
* 喺指令面板執行你嘅指令，按 (`Ctrl+Shift+P` 或 Mac 上嘅 `Cmd+Shift+P`) 並輸入 `Hello World`。
* 喺 `src/extension.ts` 裡面嘅程式碼設定斷點，方便除錯你嘅擴充功能。
* 喺除錯主控台查看擴充功能嘅輸出。

## 修改程式碼

* 喺 `src/extension.ts` 改完程式碼後，可以喺除錯工具列重新啟動擴充功能。
* 你亦可以重新載入 (`Ctrl+R` 或 Mac 上嘅 `Cmd+R`) VS Code 視窗，令擴充功能載入你嘅更改。

## 探索 API

* 打開 `node_modules/@types/vscode/index.d.ts` 檔案，就可以睇到完整嘅 API。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 透過 **Tasks: Run Task** 指令執行 "watch" 任務。要確保佢係運行中，否則測試可能唔會被偵測到。
* 喺活動列打開測試檢視，點擊「Run Test」按鈕，或者用快捷鍵 `Ctrl/Cmd + ; A`。
* 喺測試結果檢視睇測試結果嘅輸出。
* 可以修改 `src/test/extension.test.ts`，或者喺 `test` 資料夾新增測試檔案。
  * 提供嘅測試執行器只會處理符合 `**.test.ts` 命名模式嘅檔案。
  * 你可以喺 `test` 資料夾建立子資料夾，自由組織測試。

## 進階發展

* 透過[打包擴充功能](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo)減少擴充功能大小同提升啟動速度。
* 喺 VS Code 擴充功能市集[發佈你嘅擴充功能](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)。
* 設定[持續整合](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo)來自動化建置流程。

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或錯誤詮釋承擔責任。