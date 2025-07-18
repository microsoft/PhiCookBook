<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-07-17T09:52:45+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "mo"
}
-->
# **讓 Phi-3 成為產業專家**

要將 Phi-3 模型應用到產業中，您需要將產業的業務數據加入到 Phi-3 模型中。我們有兩種不同的選擇，第一種是 RAG（檢索增強生成），第二種是微調（Fine Tuning）。

## **RAG 與微調的比較**

### **檢索增強生成**

RAG 是資料檢索加上文本生成。企業的結構化資料和非結構化資料會被存放在向量資料庫中。當搜尋相關內容時，會找到相關的摘要和內容來形成上下文，並結合 LLM/SLM 的文本補全能力來生成內容。

### **微調**

微調是基於某個模型的改進。它不需要從模型演算法開始，但需要持續累積資料。如果您希望在產業應用中有更精確的術語和語言表達，微調會是更好的選擇。但如果您的資料經常變動，微調可能會變得複雜。

### **如何選擇**

1. 如果我們的回答需要引入外部資料，RAG 是最佳選擇。

2. 如果您需要輸出穩定且精確的產業知識，微調會是好選擇。RAG 優先拉取相關內容，但可能無法完全掌握專業細節。

3. 微調需要高品質的資料集，如果資料範圍很小，效果不會太明顯。RAG 則較為靈活。

4. 微調像是一個黑盒子，較難理解其內部機制；而 RAG 可以更容易找到資料來源，有效調整幻覺或內容錯誤，並提供更好的透明度。

### **應用場景**

1. 垂直產業需要特定專業詞彙和表達，***微調*** 是最佳選擇。

2. 問答系統，涉及不同知識點的綜合，***RAG*** 是最佳選擇。

3. 自動化業務流程結合，***RAG + 微調*** 是最佳選擇。

## **如何使用 RAG**

![rag](../../../../translated_images/rag.2014adc59e6f6007bafac13e800a6cbc3e297fbb9903efe20a93129bd13987e9.mo.png)

向量資料庫是以數學形式儲存資料的集合。向量資料庫讓機器學習模型更容易記住先前的輸入，使機器學習能夠支援搜尋、推薦和文本生成等應用。資料可以根據相似度指標而非精確匹配來識別，讓電腦模型能理解資料的上下文。

向量資料庫是實現 RAG 的關鍵。我們可以透過 text-embedding-3、jina-ai-embedding 等向量模型將資料轉換成向量儲存。

了解更多關於建立 RAG 應用：[https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **如何使用微調**

微調中常用的演算法有 Lora 和 QLora。如何選擇？
- [透過此範例筆記本了解更多](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 微調範例程式](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora 與 QLora**

![lora](../../../../translated_images/qlora.e6446c988ee04ca08807488bb7d9e2c0ea7ef4af9d000fc6d13032b4ac2de18d.mo.png)

LoRA（低秩適配）和 QLoRA（量化低秩適配）都是用於微調大型語言模型（LLM）的參數高效微調（PEFT）技術。PEFT 技術旨在比傳統方法更有效率地訓練模型。

LoRA 是一種獨立的微調技術，透過對權重更新矩陣進行低秩近似來減少記憶體佔用。它提供快速的訓練時間，且性能接近傳統微調方法。

QLoRA 是 LoRA 的擴展版本，結合了量化技術以進一步降低記憶體使用。QLoRA 將預訓練 LLM 的權重參數量化到 4 位元精度，比 LoRA 更節省記憶體。但由於額外的量化與反量化步驟，QLoRA 的訓練速度約比 LoRA 慢 30%。

QLoRA 使用 LoRA 作為輔助來修正量化過程中引入的誤差。QLoRA 使得在相對小型且普及的 GPU 上微調擁有數十億參數的巨型模型成為可能。例如，QLoRA 可以微調一個需要 36 張 GPU 的 700 億參數模型，只需 2 張 GPU 即可完成。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。