<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "74689a2b87f747d751edfec988ccb7fd",
  "translation_date": "2025-04-04T19:01:37+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Phi-3-visionWandB.md",
  "language_code": "hk"
}
-->
# Phi-3-Vision-128K-Instruct 計劃概覽

## 模型

Phi-3-Vision-128K-Instruct 是一個輕量化、最尖端的多模態模型，是此計劃的核心。它屬於 Phi-3 模型家族，支持最長 128,000 個 tokens 的上下文長度。模型訓練使用了多樣化的數據集，包括合成數據和精心篩選的公開網站，重點在於高質量和需要深入推理的內容。訓練過程包含監督式微調和直接偏好優化，以確保精準執行指令，並採取了強大的安全措施。

## 創建樣本數據的重要性：

1. **測試**：樣本數據可以在不同情境下測試應用程式，而不影響真實數據。這在開發和測試階段尤為重要。

2. **性能調整**：利用模仿真實數據規模和複雜性的樣本數據，可以識別性能瓶頸並相應優化應用程式。

3. **原型設計**：樣本數據可用於創建原型和模型，有助於理解用戶需求並獲得反饋。

4. **數據分析**：在數據科學領域，樣本數據通常用於探索性數據分析、模型訓練和算法測試。

5. **安全性**：在開發和測試環境中使用樣本數據，可以防止敏感真實數據的意外洩露。

6. **學習**：如果正在學習一項新技術或工具，使用樣本數據可以提供一種實際應用所學知識的方法。

請記住，樣本數據的質量會顯著影響這些活動。它的結構和變化性應盡可能接近真實數據。

### 創建樣本數據
[生成數據集腳本](./CreatingSampleData.md)

## 數據集

一個好的樣本數據集例子是 [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States)（可在 Huggingface 上獲得）。  
這個 Burberry 產品的樣本數據集包含產品分類、價格和標題的元數據，共有 3,040 行，每行代表一個獨特產品。該數據集讓我們測試模型理解和解釋視覺數據的能力，生成能捕捉細緻視覺細節和品牌特徵的描述性文字。

**注意：** 你可以使用任何包含圖片的數據集。

## 複雜推理

模型需要僅憑圖片進行價格和命名的推理。這要求模型不僅能識別視覺特徵，還要理解這些特徵在產品價值和品牌定位上的含義。通過從圖片生成準確的文本描述，這個計劃突出了整合視覺數據以提升模型在實際應用中的性能和多功能性的潛力。

## Phi-3 Vision 架構

模型架構是一個 Phi-3 的多模態版本。它處理文本和圖片數據，將這些輸入整合到統一序列中，用於全面的理解和生成任務。模型為文本和圖片分別使用嵌入層。文本 tokens 被轉換為密集向量，而圖片通過 CLIP 視覺模型處理以提取特徵嵌入。這些圖片嵌入隨後被投射到與文本嵌入相匹配的維度，確保它們可以無縫整合。

## 文本與圖片嵌入的整合

文本序列中的特殊 tokens 指示圖片嵌入應插入的位置。在處理過程中，這些特殊 tokens 被相應的圖片嵌入替換，讓模型能夠將文本和圖片作為一個序列進行處理。我們數據集的提示格式使用特殊的 <|image|> token，如下所示：

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## 範例代碼
- [Phi-3-Vision 訓練腳本](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias 示例操作指南](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**免責聲明**：  
本文件使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯準確性，但請注意，機器翻譯可能存在錯誤或不準確之處。應以原始語言版本的文件作為權威來源。對於重要信息，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤概不負責。