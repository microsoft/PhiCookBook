<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "340bd4c009524ef84102b78d06eea735",
  "translation_date": "2025-04-04T06:06:06+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingAppleMLXQuantifyingPhi.md",
  "language_code": "tw"
}
-->
# **使用 Apple MLX 框架量化 Phi-3.5**

MLX 是由 Apple 機器學習研究團隊推出的一個專為 Apple Silicon 設計的機器學習框架。

MLX 是為機器學習研究者量身打造的框架，既注重使用者友好性，又兼具高效性以便進行模型的訓練與部署。該框架的設計理念簡單明瞭，旨在讓研究者能輕鬆擴展和改進 MLX，以快速探索新想法。

透過 MLX，可以在 Apple Silicon 設備上加速大型語言模型的運行，並能夠方便地在本地執行模型。

現在 Apple MLX 框架已支援 Phi-3.5-Instruct 的量化轉換(**Apple MLX Framework 支援**)、Phi-3.5-Vision(**MLX-VLM Framework 支援**)，以及 Phi-3.5-MoE(**Apple MLX Framework 支援**)。接下來讓我們試試看：

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

### **🤖 使用 Apple MLX 的 Phi-3.5 範例**

| 實驗室   | 介紹       | 連結    |
| -------- | ---------- | ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | 學習如何使用 Apple MLX 框架操作 Phi-3.5 Instruct   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | 學習如何使用 Apple MLX 框架分析 Phi-3.5 Vision 的影像資料     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | 學習如何使用 Apple MLX 框架操作 Phi-3.5 MoE  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **資源**

1. 了解 Apple MLX 框架 [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub 資源庫 [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub 資源庫 [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**免責聲明**：  
本文檔使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為具有權威性的來源。對於關鍵信息，建議使用專業的人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤釋不承擔責任。