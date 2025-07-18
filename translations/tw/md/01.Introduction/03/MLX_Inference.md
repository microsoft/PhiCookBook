<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-07-16T21:01:25+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "tw"
}
-->
# **使用 Apple MLX Framework 推論 Phi-3**

## **什麼是 MLX Framework**

MLX 是一個針對 Apple Silicon 上機器學習研究的陣列框架，由 Apple 機器學習研究團隊開發。

MLX 是由機器學習研究人員為機器學習研究人員設計。這個框架旨在使用者友好，同時在訓練和部署模型時保持高效。框架本身的設計概念也相當簡單。我們希望讓研究人員能輕鬆擴展和改進 MLX，以便快速探索新想法。

透過 MLX，LLM 可以在 Apple Silicon 裝置上加速運行，並且模型可以非常方便地在本地執行。

## **使用 MLX 推論 Phi-3-mini**

### **1. 設定你的 MLX 環境**

1. Python 3.11.x  
2. 安裝 MLX 函式庫


```bash

pip install mlx-lm

```

### **2. 在終端機使用 MLX 執行 Phi-3-mini**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

結果（我的環境是 Apple M1 Max，64GB）如下

![Terminal](../../../../../translated_images/01.5cf57df8f7407cf9281c0237f4e69c3728b8817253aad0835d14108b07c83c88.tw.png)

### **3. 在終端機使用 MLX 量化 Phi-3-mini**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** 模型可以透過 mlx_lm.convert 進行量化，預設量化為 INT4。此範例將 Phi-3-mini 量化為 INT4。

模型可以透過 mlx_lm.convert 進行量化，預設量化為 INT4。此範例是將 Phi-3-mini 量化成 INT4。量化後，模型會儲存在預設目錄 ./mlx_model。

我們可以從終端機測試使用 MLX 量化後的模型


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

結果如下

![INT4](../../../../../translated_images/02.7b188681a8eadbc111aba8d8006e4b3671788947a99a46329261e169dd2ec29f.tw.png)


### **4. 在 Jupyter Notebook 使用 MLX 執行 Phi-3-mini**


![Notebook](../../../../../translated_images/03.b9705a3a5aaa89f9eb0ca04c1a4565dfe4a5e8cc68604227d2eab149fef1d3c7.tw.png)

***Note:*** 請閱讀此範例 [點此連結](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **資源**

1. 了解 Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub 倉庫 [https://github.com/ml-explore](https://github.com/ml-explore)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯負責。