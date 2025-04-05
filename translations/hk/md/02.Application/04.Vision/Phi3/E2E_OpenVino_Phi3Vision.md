<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "69d48385b1f1b31dd20dbb2405031bff",
  "translation_date": "2025-04-04T18:41:34+00:00",
  "source_file": "md\\02.Application\\04.Vision\\Phi3\\E2E_OpenVino_Phi3Vision.md",
  "language_code": "hk"
}
-->
這個示範展示如何使用預訓練模型根據圖像和文字提示生成Python代碼。

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

以下是逐步的解釋：

1. **導入和設置**：
   - 導入所需的庫和模組，包括 `requests`、`PIL` 用於圖像處理，以及 `transformers` 用於處理模型和數據。

2. **載入並顯示圖像**：
   - 使用 `PIL` 庫打開圖像文件 (`demo.png`) 並顯示。

3. **定義提示**：
   - 創建一個包含圖像和請求生成Python代碼的消息，用於處理圖像並使用 `plt` (matplotlib) 保存。

4. **載入處理器**：
   - 從 `out_dir` 目錄指定的預訓練模型中載入 `AutoProcessor`。該處理器負責處理文字和圖像輸入。

5. **創建提示**：
   - 使用 `apply_chat_template` 方法將消息格式化為適合模型的提示。

6. **處理輸入**：
   - 將提示和圖像處理為模型可以理解的張量。

7. **設置生成參數**：
   - 定義模型生成過程的參數，包括生成新token的最大數量以及是否對輸出進行採樣。

8. **生成代碼**：
   - 模型根據輸入和生成參數生成Python代碼。使用 `TextStreamer` 處理輸出，跳過提示和特殊token。

9. **輸出**：
   - 打印生成的代碼，應包括用於處理圖像並按提示要求保存的Python代碼。

這個示範說明如何利用OpenVino的預訓練模型根據用戶輸入和圖像動態生成代碼。

**免責聲明**:  
此文件經由AI翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。我們致力於確保翻譯準確，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。