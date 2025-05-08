<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-08T06:10:30+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "tw"
}
-->
# **使用 Apple MLX Framework 量化 Phi-3.5**


MLX 是 Apple 矽晶片上用於機器學習研究的陣列框架，由 Apple 機器學習研究團隊開發。

MLX 是由機器學習研究者為機器學習研究者設計。這個框架旨在讓使用者友善，同時在訓練和部署模型時仍具效率。框架本身的設計也很簡單明瞭。我們希望讓研究者能輕鬆擴充和改進 MLX，目標是快速探索新想法。

在 Apple Silicon 裝置上，透過 MLX 可以加速大型語言模型（LLMs），並且能非常方便地在本地運行模型。

現在 Apple MLX Framework 支援 Phi-3.5-Instruct 的量化轉換（**Apple MLX Framework 支援**）、Phi-3.5-Vision（**MLX-VLM Framework 支援**）以及 Phi-3.5-MoE（**Apple MLX Framework 支援**）。接下來一起試試看：

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



### **🤖 Apple MLX 上 Phi-3.5 範例**

| 實驗室    | 介紹 | 前往 |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | 學習如何使用 Apple MLX framework 搭配 Phi-3.5 Instruct   |  [前往](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | 學習如何用 Apple MLX framework 透過 Phi-3.5 Vision 分析圖片     |  [前往](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | 學習如何使用 Apple MLX framework 搭配 Phi-3.5 MoE  |  [前往](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |


## **資源**

1. 了解 Apple MLX Framework [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub Repo [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生的任何誤解或誤譯負責。