<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-05-08T05:19:29+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "hk"
}
-->
# **令 Phi-3 成為行業專家**

要將 Phi-3 模型應用到行業中，需要將行業業務數據加入 Phi-3 模型。我們有兩個不同的選擇，第一是 RAG（檢索增強生成），第二是微調（Fine Tuning）。

## **RAG 與微調比較**

### **檢索增強生成**

RAG 是數據檢索 + 文字生成。企業的結構化和非結構化數據存儲在向量數據庫中。當搜索相關內容時，會找到相關的摘要和內容形成上下文，並結合 LLM/SLM 的文本補全能力來生成內容。

### **微調**

微調是基於對某個模型的改進。它不需要從模型算法開始，但需要不斷積累數據。如果你想在行業應用中獲得更精確的術語和語言表達，微調會是更好的選擇。但如果你的數據經常變動，微調會變得較為複雜。

### **如何選擇**

1. 如果答案需要引入外部數據，RAG 是最佳選擇

2. 如果需要輸出穩定且精確的行業知識，微調會是不錯的選擇。RAG 優先拉取相關內容，但未必能完全掌握專業細節。

3. 微調需要高質量數據集，且如果數據範圍較小，效果不大。RAG 則更靈活。

4. 微調是個黑盒子，較難理解其內部機制。但 RAG 可以更容易追蹤數據來源，有效調整幻覺或內容錯誤，提供更好的透明度。

### **應用場景**

1. 垂直行業需要特定專業詞彙和表達，***微調*** 是最佳選擇

2. 問答系統，涉及不同知識點的綜合，***RAG*** 是最佳選擇

3. 自動化業務流程結合，***RAG + 微調*** 是最佳方案

## **如何使用 RAG**

![rag](../../../../translated_images/rag.2014adc59e6f6007bafac13e800a6cbc3e297fbb9903efe20a93129bd13987e9.hk.png)

向量數據庫是以數學形式存儲數據的集合。向量數據庫讓機器學習模型更容易記住之前的輸入，支持搜索、推薦和文本生成等應用。數據可基於相似度指標識別，而非精確匹配，使模型能理解數據的上下文。

向量數據庫是實現 RAG 的關鍵。我們可以通過 text-embedding-3、jina-ai-embedding 等向量模型將數據轉換為向量存儲。

了解更多如何創建 RAG 應用 [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **如何使用微調**

微調中常用的算法有 Lora 和 QLora。如何選擇？
- [參考此示例筆記本了解更多](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微調示例](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora 和 QLora**

![lora](../../../../translated_images/qlora.e6446c988ee04ca08807488bb7d9e2c0ea7ef4af9d000fc6d13032b4ac2de18d.hk.png)

LoRA（低秩調整）和 QLoRA（量化低秩調整）都是用於微調大型語言模型（LLM）的參數高效微調（PEFT）技術。PEFT 技術旨在比傳統方法更高效地訓練模型。

LoRA 是一種獨立的微調技術，通過對權重更新矩陣進行低秩近似，減少記憶體佔用。它訓練速度快，性能接近傳統微調方法。

QLoRA 是 LoRA 的擴展版本，加入了量化技術進一步降低記憶體使用。QLoRA 將預訓練 LLM 的權重參數精度量化到 4 位，比 LoRA 更節省記憶體。但由於多了量化和反量化步驟，QLoRA 的訓練速度比 LoRA 慢約 30%。

QLoRA 使用 LoRA 來修正量化引入的誤差。QLoRA 能在較小且易得的 GPU 上微調擁有數十億參數的超大模型。例如，QLoRA 可以用 2 張 GPU 微調原本需要 36 張 GPU 的 70B 參數模型。

**免責聲明**：  
本文件係用AI翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我哋盡力確保準確性，但請注意自動翻譯可能會有錯誤或不準確之處。原始文件嘅母語版本應被視為權威來源。對於重要資料，建議採用專業人工翻譯。我哋對因使用本翻譯而引起嘅任何誤解或誤譯概不負責。