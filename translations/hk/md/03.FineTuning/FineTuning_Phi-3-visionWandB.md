<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-07-17T08:06:40+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "hk"
}
-->
# Phi-3-Vision-128K-Instruct 專案概覽

## 模型介紹

Phi-3-Vision-128K-Instruct 是一款輕量級、先進的多模態模型，是本專案的核心。它屬於 Phi-3 模型家族，支援最高 128,000 個 token 的上下文長度。該模型訓練於多元化資料集，包含合成數據及經過嚴格篩選的公開網站資料，重點在於高品質且具推理性的內容。訓練過程涵蓋監督式微調與直接偏好優化，確保模型能精準遵循指令，同時具備強健的安全機制。

## 建立範例資料的重要性有以下幾點：

1. **測試**：範例資料讓你能在不同情境下測試應用程式，而不會影響真實資料。這在開發與測試階段尤其重要。

2. **效能調校**：使用模擬真實資料規模與複雜度的範例資料，可以幫助找出效能瓶頸並優化應用程式。

3. **原型設計**：範例資料可用於製作原型與模型，有助於理解使用者需求並收集回饋。

4. **資料分析**：在資料科學領域，範例資料常用於探索性資料分析、模型訓練及演算法測試。

5. **安全性**：在開發與測試環境使用範例資料，有助於避免敏感真實資料的意外外洩。

6. **學習**：學習新技術或工具時，使用範例資料能提供實務操作的機會。

請記得，範例資料的品質會大幅影響上述活動，應盡可能在結構與變異性上接近真實資料。

### 範例資料建立
[Generate DataSet Script](./CreatingSampleData.md)

## 資料集

一個不錯的範例資料集是 [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States)（可於 Huggingface 取得）。  
這個 Burberry 產品範例資料集包含產品類別、價格與標題等元資料，共有 3,040 筆資料，每筆代表一個獨特產品。此資料集讓我們能測試模型理解與詮釋視覺資料的能力，生成能捕捉細緻視覺細節及品牌特性的描述文字。

**Note:** 你可以使用任何包含圖片的資料集。

## 複雜推理

模型需要僅憑圖片推理價格與命名，這不僅要求模型辨識視覺特徵，還要理解這些特徵在產品價值與品牌上的意涵。透過從圖片合成精確的文字描述，本專案展示了結合視覺資料提升模型在實務應用中表現與多樣性的潛力。

## Phi-3 Vision 架構

模型架構是 Phi-3 的多模態版本，能同時處理文字與圖片資料，將這些輸入整合成統一序列，以進行全面的理解與生成任務。模型對文字與圖片分別使用不同的嵌入層。文字 token 會轉換成密集向量，圖片則透過 CLIP 視覺模型提取特徵嵌入。接著將圖片嵌入投影至與文字嵌入相同維度，確保能無縫整合。

## 文字與圖片嵌入的整合

文字序列中的特殊 token 用來標示圖片嵌入應插入的位置。處理時，這些特殊 token 會被對應的圖片嵌入取代，使模型能將文字與圖片視為單一序列。資料集的提示格式使用特殊的 <|image|> token，如下所示：

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## 範例程式碼
- [Phi-3-Vision 訓練腳本](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias 範例教學](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。