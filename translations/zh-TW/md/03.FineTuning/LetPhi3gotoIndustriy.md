# **讓 Phi-3 成為產業專家**

要將 Phi-3 模型應用到產業中，需要將產業的業務數據加入 Phi-3 模型。我們有兩種不同的選擇，第一是 RAG（Retrieval Augmented Generation，檢索增強生成），第二是 Fine Tuning（微調）。

## **RAG 與 Fine-Tuning 的比較**

### **檢索增強生成（Retrieval Augmented Generation）**

RAG 是資料檢索加上文本生成。企業的結構化與非結構化資料會存放在向量資料庫中。當搜尋相關內容時，會找到相關的摘要與內容組成上下文，並結合 LLM/SLM 的文本補全能力來生成內容。

### **微調（Fine-tuning）**

微調是基於既有模型的改進，不需要從模型演算法開始，但需要持續累積資料。如果你希望在產業應用中有更精確的術語和語言表達，微調會是更好的選擇。但如果資料經常變動，微調可能會變得複雜。

### **如何選擇**

1. 如果答案需要引入外部資料，RAG 是最佳選擇。

2. 如果需要輸出穩定且精確的產業知識，微調會是好選擇。RAG 優先拉取相關內容，但可能無法完全掌握專業細節。

3. 微調需要高品質的資料集，若資料範圍很小，效果不明顯。RAG 則較為靈活。

4. 微調像是黑盒子，較難理解內部機制；而 RAG 可以更容易追蹤資料來源，有效調整幻覺或內容錯誤，並提供更好的透明度。

### **應用場景**

1. 垂直產業需要特定專業詞彙與表達，***微調*** 是最佳選擇。

2. 問答系統，涉及不同知識點的綜合，***RAG*** 是最佳選擇。

3. 自動化業務流程結合，***RAG + 微調*** 是最佳選擇。

## **如何使用 RAG**

![rag](../../../../translated_images/zh-TW/rag.2014adc59e6f6007.webp)

向量資料庫是以數學形式儲存資料的集合。向量資料庫讓機器學習模型更容易記住先前輸入，支持搜尋、推薦和文本生成等應用。資料可根據相似度指標而非精確匹配來識別，使模型能理解資料的上下文。

向量資料庫是實現 RAG 的關鍵。我們可以透過 text-embedding-3、jina-ai-embedding 等向量模型將資料轉換成向量儲存。

了解更多關於建立 RAG 應用請參考 [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **如何使用微調**

微調常用的演算法有 Lora 和 QLora。該如何選擇？
- [透過此範例筆記本深入了解](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微調範例程式](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora 與 QLora**

![lora](../../../../translated_images/zh-TW/qlora.e6446c988ee04ca0.webp)

LoRA（Low-Rank Adaptation，低秩適配）和 QLoRA（Quantized Low-Rank Adaptation，量化低秩適配）都是用於微調大型語言模型（LLM）的參數高效微調（PEFT）技術。PEFT 技術旨在比傳統方法更有效率地訓練模型。

LoRA 是一種獨立的微調技術，透過對權重更新矩陣進行低秩近似來減少記憶體佔用。它訓練速度快，且性能接近傳統微調方法。

QLoRA 是 LoRA 的擴展版本，結合了量化技術以進一步降低記憶體使用。QLoRA 將預訓練 LLM 權重參數的精度量化到 4 位元，比 LoRA 更節省記憶體。但由於額外的量化與反量化步驟，QLoRA 的訓練速度約比 LoRA 慢 30%。

QLoRA 使用 LoRA 作為輔助來修正量化過程中引入的誤差。QLoRA 使得在相對小型且普及的 GPU 上微調擁有數十億參數的巨型模型成為可能。例如，QLoRA 可以微調一個需要 36 張 GPU 的 700 億參數模型，只需 2 張 GPU 即可完成。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。