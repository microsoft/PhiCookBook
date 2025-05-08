<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-08T05:16:01+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "hk"
}
-->
# Phi-3-Vision-128K-Instruct 項目概覽

## 模型簡介

Phi-3-Vision-128K-Instruct 係呢個項目嘅核心，一個輕量化、先進嘅多模態模型。佢屬於 Phi-3 模型家族，支持最高 128,000 個 token 嘅上下文長度。模型喺一個多元化嘅數據集上訓練，包括合成數據同經過嚴格篩選嘅公開網站內容，重點係高質素、需要推理嘅內容。訓練過程包含監督式微調同直接偏好優化，確保模型準確跟隨指示，並且有完善嘅安全措施。

## 創建樣本數據嘅重要原因：

1. **測試**：樣本數據可以喺唔影響真實數據嘅情況下，測試應用喺唔同場景嘅表現。呢點喺開發同測試階段尤其重要。

2. **性能調校**：用模擬真實數據規模同複雜度嘅樣本數據，可以識別性能瓶頸，從而優化應用。

3. **原型設計**：樣本數據可以用嚟做原型同模擬，有助理解用戶需求同收集反饋。

4. **數據分析**：喺數據科學領域，樣本數據經常用於探索性分析、模型訓練同算法測試。

5. **安全**：喺開發同測試環境用樣本數據，有助防止意外洩漏敏感真實數據。

6. **學習**：學習新技術或工具時，使用樣本數據可以實踐所學。

記住，樣本數據嘅質素對以上活動影響重大，佢嘅結構同變異性應盡量貼近真實數據。

### 樣本數據創建
[Generate DataSet Script](./CreatingSampleData.md)

## 數據集

一個好嘅樣本數據集例子係 [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States)（喺 Huggingface 有提供）。  
Burberry 產品嘅樣本數據集，連同產品分類、價格同標題嘅元數據，總共有 3,040 行，每行代表一件獨特產品。呢個數據集可以用嚟測試模型理解同解讀視覺數據嘅能力，生成捕捉細緻視覺細節同品牌特徵嘅描述性文本。

**Note:** 你可以用任何包含圖片嘅數據集。

## 複雜推理

模型需要根據圖片推理價格同命名。呢點唔單止要識別視覺特徵，仲要理解呢啲特徵喺產品價值同品牌定位上嘅含義。透過從圖片合成準確嘅文字描述，項目展示咗整合視覺數據喺提升模型喺現實應用中表現同多功能性嘅潛力。

## Phi-3 Vision 架構

模型架構係 Phi-3 嘅多模態版本。佢同時處理文本同圖片數據，將呢啲輸入整合成一個統一序列，方便全面理解同生成任務。模型用獨立嘅嵌入層處理文本同圖片。文本 token 會轉成密集向量，圖片則透過 CLIP vision 模型抽取特徵嵌入。之後將圖片嵌入投影到同文本嵌入相同維度，確保可以無縫整合。

## 文本同圖片嵌入整合

文本序列入面嘅特殊 token 用嚟標示插入圖片嵌入嘅位置。處理時，呢啲特殊 token 會被對應嘅圖片嵌入替換，令模型可以將文本同圖片當作一條序列處理。我哋嘅數據集 prompt 用咗特殊嘅 <|image|> token 格式如下：

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## 範例程式碼
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原文文件的母語版本應被視為權威來源。對於重要資料，建議使用專業人工翻譯。我們不對因使用此翻譯而引致的任何誤解或誤釋負責。