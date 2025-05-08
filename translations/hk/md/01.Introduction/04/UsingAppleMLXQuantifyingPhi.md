<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-08T06:10:16+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "hk"
}
-->
# **用 Apple MLX Framework 量化 Phi-3.5**

MLX 係 Apple 硅片上用作機器學習研究嘅陣列框架，由 Apple 機器學習研究團隊開發。

MLX 係由機器學習研究人員為機器學習研究人員設計。呢個框架旨在用戶友善，但同時又高效，方便訓練同部署模型。框架本身嘅設計概念亦好簡單。我哋希望方便研究人員擴展同改進 MLX，目標係快速探索新嘅想法。

喺 Apple 硅片裝置上，透過 MLX 可以加速大型語言模型（LLMs），而且模型可以喺本地非常方便咁運行。

而家 Apple MLX Framework 支援 Phi-3.5-Instruct 嘅量化轉換（**Apple MLX Framework 支援**）、Phi-3.5-Vision（**MLX-VLM Framework 支援**）同 Phi-3.5-MoE（**Apple MLX Framework 支援**）。一齊試下啦：

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```


### **🤖 Apple MLX 嘅 Phi-3.5 範例**

| Labs    | 介紹 | 前往 |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | 學習點樣用 Apple MLX framework 搭配 Phi-3.5 Instruct   |  [前往](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | 學習點樣用 Phi-3.5 Vision 配合 Apple MLX framework 分析圖片     |  [前往](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | 學習點樣用 Apple MLX framework 搭配 Phi-3.5 MoE  |  [前往](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |


## **資源**

1. 認識 Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**免責聲明**：  
本文件乃使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們致力於準確，但請注意自動翻譯可能包含錯誤或不準確之處。原文文件以其原生語言版本為權威來源。對於重要資料，建議採用專業人工翻譯。我們對因使用此翻譯而引致的任何誤解或誤釋概不負責。