<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "700b9a537ce4426de5a7ccfa8e96e581",
  "translation_date": "2025-04-04T07:19:22+00:00",
  "source_file": "md\\03.FineTuning\\03.Inference\\MLX_Inference.md",
  "language_code": "tw"
}
-->
# **使用 Apple MLX 框架推理 Phi-3**

## **什麼是 MLX 框架**

MLX 是一個專為蘋果矽晶片設計的機器學習研究框架，由 Apple 機器學習研究團隊提供。

MLX 是由機器學習研究人員設計，專為機器學習研究人員使用。該框架旨在提供使用者友好的體驗，同時保持高效的模型訓練與部署。框架的設計概念也相對簡單，目的是讓研究人員能輕鬆擴展與改進 MLX，以便快速探索新想法。

透過 MLX，可以在蘋果矽晶片設備上加速 LLMs 的運行，並且能夠非常方便地在本地執行模型。

## **使用 MLX 推理 Phi-3-mini**

### **1. 設置 MLX 環境**

1. Python 3.11.x
2. 安裝 MLX Library

```bash

pip install mlx-lm

```

### **2. 在終端使用 MLX 運行 Phi-3-mini**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

執行結果（我的環境是 Apple M1 Max，64GB）如下：

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.tw.png)

### **3. 在終端使用 MLX 量化 Phi-3-mini**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***注意：*** 模型可以通過 mlx_lm.convert 進行量化，預設的量化方式是 INT4。本範例將 Phi-3-mini 量化為 INT4。

模型可以通過 mlx_lm.convert 進行量化，預設量化方式為 INT4。本範例將 Phi-3-mini 量化為 INT4。量化後的模型會存儲在預設目錄 ./mlx_model。

我們可以在終端測試通過 MLX 量化的模型。

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

執行結果如下：

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.tw.png)

### **4. 在 Jupyter Notebook 使用 MLX 運行 Phi-3-mini**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.tw.png)

***注意：*** 請參考此範例 [點擊此連結](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **資源**

1. 了解 Apple MLX 框架 [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub 資料庫 [https://github.com/ml-explore](https://github.com/ml-explore)

**免責聲明**:  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不精確之處。應以原始語言的文件作為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。