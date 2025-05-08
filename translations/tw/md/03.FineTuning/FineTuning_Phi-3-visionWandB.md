<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-08T05:16:21+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "tw"
}
-->
# Phi-3-Vision-128K-Instruct 專案概覽

## 模型介紹

Phi-3-Vision-128K-Instruct 是這個專案的核心，一個輕量級且先進的多模態模型。它屬於 Phi-3 模型家族，支援最高 128,000 代幣的上下文長度。模型訓練使用多元資料集，包含合成資料與經嚴格篩選的公開網站內容，強調高品質且具推理性的資訊。訓練過程包含監督式微調與直接偏好優化，確保精準遵循指令，同時具備完善的安全機制。

## 為什麼建立樣本資料很重要：

1. **測試**：樣本資料讓你能在不同情境下測試應用程式，而不會影響真實資料，這在開發與測試階段尤其重要。

2. **效能調校**：透過模擬真實資料規模與複雜度的樣本資料，你可以找出效能瓶頸並優化應用程式。

3. **原型設計**：樣本資料可用來建立原型與模型，有助於理解使用者需求並收集回饋。

4. **資料分析**：在資料科學中，樣本資料常用於探索性資料分析、模型訓練與演算法測試。

5. **安全性**：在開發與測試環境使用樣本資料，可避免敏感真實資料意外外洩。

6. **學習**：學習新技術或工具時，使用樣本資料能提供實務操作的機會。

請記得，樣本資料的品質會大幅影響這些活動，應盡可能接近真實資料的結構與多樣性。

### 樣本資料建立
[Generate DataSet Script](./CreatingSampleData.md)

## 資料集

一個很好的樣本資料集範例是 [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States)（可於 Huggingface 取得）。  
Burberry 產品的樣本資料集包含產品分類、價格與標題的元資料，總共 3,040 筆資料，每筆代表一個獨特產品。此資料集讓我們能測試模型理解與解析視覺資料的能力，產生描述細膩視覺細節與品牌特色的文字。

**Note:** 你可以使用任何包含圖片的資料集。

## 複雜推理

模型需要僅根據圖片推理價格與命名。這不僅要求模型辨識視覺特徵，還要理解其在產品價值與品牌上的意涵。透過從圖片合成精確的文字描述，此專案展示結合視覺資料來提升模型在實務應用中表現與多功能性的潛力。

## Phi-3 Vision 架構

模型架構是 Phi-3 的多模態版本，能同時處理文字與圖片資料，將這些輸入整合成統一序列，以利全面理解與生成任務。模型對文字與圖片分別使用不同的 embedding 層。文字代幣轉成密集向量，圖片則經由 CLIP 視覺模型提取特徵 embedding，再將圖片 embedding 投影至與文字 embedding 相同維度，確保能無縫整合。

## 文字與圖片 embedding 的整合

文字序列中的特殊代幣標示圖片 embedding 應插入的位置。處理時，這些特殊代幣會被對應的圖片 embedding 取代，使模型能將文字與圖片視為單一序列處理。我們資料集的提示格式使用特殊 <|image|> 代幣，如下：

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## 範例程式碼
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所引起之任何誤解或誤釋負責。