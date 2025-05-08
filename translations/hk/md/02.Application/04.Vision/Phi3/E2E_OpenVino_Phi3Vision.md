<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-08T05:26:43+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "hk"
}
-->
呢個示範展示咗點樣用一個預訓練模型，根據一張圖片同文字提示去生成 Python 代碼。

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

以下係逐步解釋：

1. **導入同設置**：
   - 導入咗所需嘅庫同模組，包括用於圖像處理嘅 `requests`、`PIL`，以及處理模型同流程嘅 `transformers`。

2. **加載同顯示圖片**：
   - 用 `PIL` 庫打開咗一個圖片文件（`demo.png`）並顯示出嚟。

3. **定義提示語**：
   - 建立咗一個信息，包含圖片同請求生成用於處理圖片並用 `plt`（matplotlib）保存嘅 Python 代碼。

4. **加載處理器**：
   - 從 `out_dir` 目錄指定嘅預訓練模型加載 `AutoProcessor`。呢個處理器會處理文字同圖片輸入。

5. **創建提示**：
   - 用 `apply_chat_template` 方法將信息格式化成適合模型嘅提示語。

6. **處理輸入**：
   - 將提示語同圖片處理成模型能理解嘅張量。

7. **設置生成參數**：
   - 定義模型生成過程嘅參數，包括最大生成新 token 數量同是否採樣輸出。

8. **生成代碼**：
   - 模型根據輸入同生成參數生成 Python 代碼。用 `TextStreamer` 處理輸出，跳過提示語同特殊 token。

9. **輸出**：
   - 打印生成嘅代碼，應該包括用於處理圖片並按提示保存嘅 Python 代碼。

呢個示範說明咗點樣利用 OpenVino 嘅預訓練模型，根據用戶輸入同圖片動態生成代碼。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我哋致力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件嘅母語版本應被視為權威來源。對於重要資料，建議採用專業人手翻譯。對因使用此翻譯而引起嘅任何誤解或誤釋，我哋概不負責。