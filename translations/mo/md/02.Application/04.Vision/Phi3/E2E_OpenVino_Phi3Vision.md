<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-07-17T05:01:21+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "mo"
}
-->
此示範展示如何使用預訓練模型，根據圖片和文字提示生成 Python 程式碼。

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

以下是逐步說明：

1. **匯入與設定**：
   - 匯入所需的函式庫和模組，包括用於影像處理的 `requests`、`PIL`，以及用於模型和處理的 `transformers`。

2. **載入並顯示圖片**：
   - 使用 `PIL` 函式庫開啟圖片檔案（`demo.png`）並顯示。

3. **定義提示詞**：
   - 建立一段訊息，包含圖片及請求生成用於處理圖片並使用 `plt`（matplotlib）儲存的 Python 程式碼。

4. **載入處理器**：
   - 從指定的 `out_dir` 目錄載入預訓練模型的 `AutoProcessor`，此處理器將負責文字和圖片的輸入。

5. **建立提示詞**：
   - 使用 `apply_chat_template` 方法將訊息格式化成適合模型的提示詞。

6. **處理輸入**：
   - 將提示詞和圖片處理成模型可理解的張量。

7. **設定生成參數**：
   - 定義模型生成過程的參數，包括最大生成新標記數量及是否採樣輸出。

8. **生成程式碼**：
   - 模型根據輸入和生成參數產生 Python 程式碼。使用 `TextStreamer` 來處理輸出，跳過提示詞和特殊標記。

9. **輸出結果**：
   - 印出生成的程式碼，應包含用於處理圖片並依提示儲存的 Python 程式碼。

此示範說明如何利用 OpenVino 的預訓練模型，根據使用者輸入和圖片動態生成程式碼。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。