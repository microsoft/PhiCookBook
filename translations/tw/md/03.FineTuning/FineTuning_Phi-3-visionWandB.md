<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "74689a2b87f747d751edfec988ccb7fd",
  "translation_date": "2025-04-04T07:10:36+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Phi-3-visionWandB.md",
  "language_code": "tw"
}
-->
# Phi-3-Vision-128K-Instruct 專案概述

## 模型介紹

Phi-3-Vision-128K-Instruct 是一款輕量化的尖端多模態模型，為本專案的核心。它屬於 Phi-3 模型家族的一部分，支持長達 128,000 個 token 的上下文長度。該模型訓練於多樣化的數據集，包括合成數據以及精心篩選的公開網站，重點在於高質量和需要推理能力的內容。訓練過程包括監督式微調和直接偏好優化，以確保精確遵循指令，同時具備強大的安全性。

## 為什麼建立樣本數據至關重要：

1. **測試**：樣本數據可讓您在各種情境下測試應用程式，而不影響真實數據。這在開發和測試階段尤為重要。

2. **性能調整**：使用模仿真實數據規模和複雜性的樣本數據，可以識別性能瓶頸並相應地優化應用程式。

3. **原型設計**：樣本數據可用於創建原型和模型，有助於理解使用者需求並獲得反饋。

4. **數據分析**：在數據科學中，樣本數據通常用於探索性數據分析、模型訓練和算法測試。

5. **安全性**：在開發和測試環境中使用樣本數據，有助於防止敏感真實數據的意外洩漏。

6. **學習**：如果您正在學習新技術或工具，使用樣本數據是一種實際應用所學知識的方式。

請記住，樣本數據的質量對這些活動的影響非常大。它的結構和變化性應盡可能接近真實數據。

### 樣本數據創建
[生成數據集腳本](./CreatingSampleData.md)

## 數據集

一個很好的樣本數據集例子是 [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States)（可在 Huggingface 上獲取）。  
這是一個包含 Burberry 產品樣本數據集及其元數據的數據集，涵蓋產品類別、價格和標題，共有 3,040 行，每行代表一個獨特的產品。此數據集讓我們能測試模型理解和解釋視覺數據的能力，生成能捕捉精細視覺細節和品牌特徵的描述性文本。

**注意：** 您可以使用任何包含圖像的數據集。

## 複雜推理

模型需要僅基於圖像來推理價格和命名。這要求模型不僅能識別視覺特徵，還能理解這些特徵在產品價值和品牌定位方面的含義。透過從圖像中生成準確的文字描述，該專案突出了整合視覺數據以提升模型在真實應用中性能和多樣性的潛力。

## Phi-3 Vision 架構

模型架構是一個多模態版本的 Phi-3。它同時處理文本和圖像數據，將這些輸入整合到統一的序列中，以完成綜合理解和生成任務。模型使用獨立的嵌入層來處理文本和圖像。文本 token 被轉換為密集向量，而圖像則通過 CLIP 視覺模型提取特徵嵌入。這些圖像嵌入會被投影到與文本嵌入相匹配的維度，確保它們可以無縫整合。

## 文本與圖像嵌入的整合

文本序列中的特殊 token 指示圖像嵌入應插入的位置。在處理過程中，這些特殊 token 被相應的圖像嵌入替換，使模型能夠將文本和圖像作為單一序列進行處理。我們的數據集提示使用特殊的 <|image|> token 格式如下：

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## 範例代碼
- [Phi-3-Vision 訓練腳本](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias 示例講解](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋不承擔責任。