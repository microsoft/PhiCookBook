<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "700b9a537ce4426de5a7ccfa8e96e581",
  "translation_date": "2025-04-04T17:50:39+00:00",
  "source_file": "md\\01.Introduction\\03\\MLX_Inference.md",
  "language_code": "hk"
}
-->
# **使用 Apple MLX 框架進行 Phi-3 推理**

## **什麼是 MLX 框架**

MLX 是一個專為 Apple 矽片設計的機器學習研究框架，由 Apple 機器學習研究團隊開發。

MLX 是由機器學習研究人員為機器學習研究人員設計的。這個框架的目的是既能簡單易用又能高效地訓練和部署模型。框架本身的設計也非常直觀，目標是讓研究人員能輕鬆擴展和改進 MLX，以快速探索新想法。

通過 MLX，可以在 Apple 矽片設備上加速 LLMs，並且模型可以非常方便地在本地運行。

## **使用 MLX 推理 Phi-3-mini**

### **1. 設置 MLX 環境**

1. Python 3.11.x  
2. 安裝 MLX 庫  

```bash

pip install mlx-lm

```

### **2. 在終端中使用 MLX 運行 Phi-3-mini**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

執行結果（我的環境是 Apple M1 Max，64GB）如下：

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.hk.png)

### **3. 在終端中使用 MLX 量化 Phi-3-mini**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***注意：*** 模型可以通過 mlx_lm.convert 進行量化，默認量化方式為 INT4。本例將 Phi-3-mini 量化為 INT4。

模型可以通過 mlx_lm.convert 進行量化，默認量化方式為 INT4。本例中將 Phi-3-mini 量化為 INT4。量化後，模型將存儲在默認目錄 ./mlx_model。

我們可以在終端中測試經過 MLX 量化的模型。

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

執行結果如下：

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.hk.png)

### **4. 在 Jupyter Notebook 中使用 MLX 運行 Phi-3-mini**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.hk.png)

***注意：*** 請參考此範例 [點擊此連結](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **資源**

1. 了解 Apple MLX 框架 [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)  
2. Apple MLX GitHub 倉庫 [https://github.com/ml-explore](https://github.com/ml-explore)  

**免責聲明**:  
本文檔已使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於重要信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。