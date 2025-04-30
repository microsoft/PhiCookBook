<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "69d48385b1f1b31dd20dbb2405031bff",
  "translation_date": "2025-04-04T06:49:40+00:00",
  "source_file": "md\\02.Application\\04.Vision\\Phi3\\E2E_OpenVino_Phi3Vision.md",
  "language_code": "tw"
}
-->
這個示範展示了如何使用預訓練模型根據圖片和文字提示生成 Python 程式碼。

[範例程式碼](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

以下是逐步的解釋：

1. **匯入與設定**：
   - 匯入必要的函式庫和模組，包括 `requests`、`PIL` 用於圖像處理，以及 `transformers` 用於處理模型和處理。

2. **載入並顯示圖片**：
   - 使用 `PIL` 函式庫打開圖片檔案 (`demo.png`) 並顯示。

3. **定義提示**：
   - 建立一個訊息，其中包含圖片以及生成 Python 程式碼以處理圖片並使用 `plt` (matplotlib) 儲存的請求。

4. **載入處理器**：
   - 從由 `out_dir` 指定的預訓練模型中載入 `AutoProcessor`。此處理器將負責處理文字和圖片輸入。

5. **建立提示**：
   - 使用 `apply_chat_template` 方法將訊息格式化為適合模型的提示。

6. **處理輸入**：
   - 提示和圖片被處理成模型可以理解的張量。

7. **設定生成參數**：
   - 定義模型生成過程的參數，包括生成的新 token 的最大數量以及是否進行取樣。

8. **生成程式碼**：
   - 模型根據輸入和生成參數生成 Python 程式碼。使用 `TextStreamer` 處理輸出，跳過提示和特殊 token。

9. **輸出**：
   - 輸出生成的程式碼，應包括用於處理圖片並按提示要求儲存的 Python 程式碼。

這個示範說明了如何使用 OpenVino 的預訓練模型，根據使用者輸入和圖片動態生成程式碼。

**免責聲明**:  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不精確之處。原始文件的母語版本應被視為最具權威的來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用本翻譯而引起的任何誤解或錯誤解讀概不負責。