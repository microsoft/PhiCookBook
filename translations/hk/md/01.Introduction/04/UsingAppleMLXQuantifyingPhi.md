<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "340bd4c009524ef84102b78d06eea735",
  "translation_date": "2025-04-04T17:56:52+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingAppleMLXQuantifyingPhi.md",
  "language_code": "hk"
}
-->
# **使用 Apple MLX 框架量化 Phi-3.5**

MLX 是 Apple 機器學習研究團隊開發的一個陣列框架，專為 Apple Silicon 上的機器學習研究設計。

MLX 是由機器學習研究人員為機器學習研究人員設計的框架。該框架旨在保持用戶友好，同時仍然高效地進行模型訓練和部署。框架本身的設計概念也非常簡單。我們希望研究人員能夠輕鬆擴展和改進 MLX，以快速探索新想法為目標。

在 Apple Silicon 設備上，可以通過 MLX 加速 LLMs，並且模型可以非常方便地在本地運行。

現在，Apple MLX 框架支持 Phi-3.5-Instruct（**Apple MLX Framework 支持**）、Phi-3.5-Vision（**MLX-VLM Framework 支持**）以及 Phi-3.5-MoE（**Apple MLX Framework 支持**）的量化轉換。接下來讓我們試試看：

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

### **🤖 使用 Apple MLX 的 Phi-3.5 示例**

| 實驗室    | 介紹 | 前往 |
| -------- | ------- |  ------- |
| 🚀 實驗室 - 介紹 Phi-3.5 Instruct  | 學習如何使用 Apple MLX 框架的 Phi-3.5 Instruct   |  [前往](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 實驗室 - 介紹 Phi-3.5 Vision（圖像） | 學習如何使用 Apple MLX 框架的 Phi-3.5 Vision 來分析圖像     |  [前往](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 實驗室 - 介紹 Phi-3.5 Vision（MoE）   | 學習如何使用 Apple MLX 框架的 Phi-3.5 MoE  |  [前往](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **資源**

1. 了解 Apple MLX 框架 [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub 倉庫 [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub 倉庫 [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**免責聲明**：  
此文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為具權威性的來源。對於重要信息，建議尋求專業的人類翻譯。我們不對因使用此翻譯而產生的任何誤解或錯誤解釋承擔責任。