<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6a7479104914787e4f0976e39131e8e3",
  "translation_date": "2025-04-04T17:21:30+00:00",
  "source_file": "code\\07.Lab\\01\\Apple\\phi3ext\\vsc-extension-quickstart.md",
  "language_code": "hk"
}
-->
# 歡迎使用你的 VS Code 擴展功能

## 文件夾內容

* 此文件夾包含你的擴展所需的所有文件。
* `package.json` - 這是清單文件，你可以在此聲明擴展及命令。
  * 示例插件註冊了一個命令並定義了它的標題和命令名稱。有了這些資訊，VS Code 就可以在命令面板中顯示該命令，但目前還不需要加載插件。
* `src/extension.ts` - 這是主要文件，你將在這裡提供命令的具體實現。
  * 該文件導出了一個函數 `activate`，當你的擴展首次被激活時（例如執行命令時）會調用它。在 `activate` 函數內部，我們調用 `registerCommand`。
  * 我們將包含命令實現的函數作為第二個參數傳遞給 `registerCommand`。

## 設置

* 安裝推薦的擴展（amodio.tsl-problem-matcher, ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）

## 馬上開始使用

* 按 `F5` 打開一個載入了你的擴展的新窗口。
* 從命令面板執行你的命令，按 (`Ctrl+Shift+P` 或 `Cmd+Shift+P` 在 Mac 上) 然後輸入 `Hello World`。
* 在 `src/extension.ts` 文件中設置斷點，調試你的擴展。
* 在調試控制台中查看你的擴展輸出。

## 修改代碼

* 修改 `src/extension.ts` 文件中的代碼後，可以從調試工具欄重新啟動擴展。
* 也可以重新載入 (`Ctrl+R` 或 `Cmd+R` 在 Mac 上) VS Code 窗口來載入你的修改。

## 探索 API

* 打開 `node_modules/@types/vscode/index.d.ts` 文件，你可以查看我們完整的 API 集。

## 運行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通過 **Tasks: Run Task** 命令運行 "watch" 任務。確保它正在運行，否則測試可能無法被發現。
* 從活動欄打開測試視圖，點擊 "Run Test" 按鈕，或者使用快捷鍵 `Ctrl/Cmd + ; A`。
* 在測試結果視圖中查看測試結果的輸出。
* 修改 `src/test/extension.test.ts` 或在 `test` 文件夾內創建新的測試文件。
  * 提供的測試運行器只會考慮匹配名稱模式 `**.test.ts` 的文件。
  * 你可以在 `test` 文件夾內創建子文件夾，按你需要的方式組織測試。

## 深入探索

* 通過 [打包你的擴展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) 減少擴展大小並提高啟動速度。
* 在 VS Code 擴展市場上 [發布你的擴展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 設置 [持續集成](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) 來自動化構建流程。

**免責聲明**:  
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。