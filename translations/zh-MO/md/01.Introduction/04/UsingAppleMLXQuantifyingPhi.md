# **使用 Apple MLX 框架對 Phi-3.5 進行量化**

MLX 是一個專為 Apple 硅芯片上的機器學習研究打造的陣列框架，由 Apple 機器學習研究團隊開發。

MLX 由機器學習研究人員為機器學習研究人員設計。這個框架旨在用戶友好，同時在訓練和部署模型時保持高效。框架本身的設計概念也相當簡單。我們希望讓研究人員能輕鬆擴展和改進 MLX，以便快速探索新想法。

透過 MLX，Apple 硅芯片設備上的大型語言模型（LLMs）可以加速運行，並且模型能夠非常方便地在本地執行。

目前 Apple MLX 框架支持 Phi-3.5-Instruct 的量化轉換（**Apple MLX Framework support**）、Phi-3.5-Vision（**MLX-VLM Framework support**）以及 Phi-3.5-MoE（**Apple MLX Framework support**）。接下來讓我們試試看：

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

### **🤖 Phi-3.5 與 Apple MLX 的範例**

| 實驗室    | 介紹 | 前往 |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | 學習如何使用 Apple MLX 框架搭配 Phi-3.5 Instruct   |  [前往](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | 學習如何使用 Apple MLX 框架搭配 Phi-3.5 Vision 進行影像分析     |  [前往](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | 學習如何使用 Apple MLX 框架搭配 Phi-3.5 MoE  |  [前往](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **資源**

1. 了解 Apple MLX 框架 [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub 倉庫 [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub 倉庫 [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。