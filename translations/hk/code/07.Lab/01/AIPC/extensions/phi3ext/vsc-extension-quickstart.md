<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8d36fc444748a50558d017e8a0772437",
  "translation_date": "2025-04-04T17:18:13+00:00",
  "source_file": "code\\07.Lab\\01\\AIPC\\extensions\\phi3ext\\vsc-extension-quickstart.md",
  "language_code": "hk"
}
-->
# 歡迎使用 VS Code 擴展

## 文件夾內有什麼

* 這個文件夾包含擴展所需的所有文件。
* `package.json` - 這是宣告擴展和命令的 manifest 文件。
  * 示例插件註冊了一個命令，並定義了它的標題和命令名稱。有了這些資訊，VS Code 可以在命令面板中顯示該命令，但暫時不需要加載插件。
* `src/extension.ts` - 這是您提供命令實現的主文件。
  * 該文件導出了一個函數 `activate`，它在您的擴展首次啟動時被調用（在此情況下是執行命令）。在 `activate` 函數內，我們調用了 `registerCommand`。
  * 我們將包含命令實現的函數作為第二個參數傳遞給 `registerCommand`。

## 設置

* 安裝推薦的擴展 (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, 和 dbaeumer.vscode-eslint)

## 馬上開始

* 按 `F5` 打開一個加載了您的擴展的新窗口。
* 在命令面板中運行您的命令，按 (`Ctrl+Shift+P` 或 `Cmd+Shift+P` 在 Mac 上) 並輸入 `Hello World`。
* 在 `src/extension.ts` 文件內設置斷點來調試您的擴展。
* 在調試控制台中找到您的擴展的輸出。

## 修改內容

* 修改 `src/extension.ts` 中的代碼後，您可以從調試工具欄重新啟動擴展。
* 您也可以重新加載 (`Ctrl+R` 或 `Cmd+R` 在 Mac 上) VS Code 窗口以加載您的更改。

## 探索 API

* 您可以在打開文件 `node_modules/@types/vscode/index.d.ts` 時查看我們完整的 API 集。

## 運行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通過 **Tasks: Run Task** 命令運行 "watch" 任務。確保此任務正在運行，否則可能無法發現測試。
* 從活動欄的測試視圖中點擊 "Run Test" 按鈕，或使用快捷鍵 `Ctrl/Cmd + ; A`。
* 在測試結果視圖中查看測試結果的輸出。
* 修改 `src/test/extension.test.ts` 或在 `test` 文件夾內創建新的測試文件。
  * 提供的測試運行器只會考慮名稱模式匹配 `**.test.ts` 的文件。
  * 您可以在 `test` 文件夾內創建子文件夾，按照您的需求結構化測試。

## 更深入

* 通過[打包您的擴展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo)來減少擴展大小並提升啟動速度。
* 在 VS Code 擴展市場[發布您的擴展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)。
* 通過設置[持續集成](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo)來自動化構建。

**免責聲明**：  
此文件是使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯的。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議尋求專業的人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。