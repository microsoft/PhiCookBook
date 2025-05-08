<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-05-08T06:00:51+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "hk"
}
-->
# **用 Apple MLX Framework 推論 Phi-3**

## **咩係 MLX Framework**

MLX 係 Apple silicon 上用嚟做機器學習研究嘅陣列框架，由 Apple 嘅機器學習研究團隊開發。

MLX 係由機器學習研究員設計，俾機器學習研究員用。呢個框架目標係易用，但同時又有效率去訓練同部署模型。框架本身設計都好簡單易明。我哋希望研究員可以輕鬆擴展同改進 MLX，方便快速試驗新嘅想法。

喺 Apple Silicon 裝置上，可以用 MLX 加速大型語言模型（LLMs），而且可以好方便咁喺本地運行模型。

## **用 MLX 去推論 Phi-3-mini**

### **1. 設定你嘅 MLX 環境**

1. Python 3.11.x
2. 安裝 MLX Library


```bash

pip install mlx-lm

```

### **2. 用 MLX 喺 Terminal 運行 Phi-3-mini**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

結果（我用嘅係 Apple M1 Max，64GB）係

![Terminal](../../../../../translated_images/01.5cf57df8f7407cf9281c0237f4e69c3728b8817253aad0835d14108b07c83c88.hk.png)

### **3. 用 MLX 喺 Terminal 量化 Phi-3-mini**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** 可以用 mlx_lm.convert 去量化模型，預設嘅量化係 INT4。呢個例子係將 Phi-3-mini 量化成 INT4。

模型可以用 mlx_lm.convert 量化，預設係 INT4。呢個例子係將 Phi-3-mini 量化成 INT4。量化完成後，模型會儲存在預設目錄 ./mlx_model。

我哋可以喺 Terminal 測試用 MLX 量化後嘅模型


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

結果係

![INT4](../../../../../translated_images/02.7b188681a8eadbc111aba8d8006e4b3671788947a99a46329261e169dd2ec29f.hk.png)


### **4. 用 MLX 喺 Jupyter Notebook 運行 Phi-3-mini**


![Notebook](../../../../../translated_images/03.b9705a3a5aaa89f9eb0ca04c1a4565dfe4a5e8cc68604227d2eab149fef1d3c7.hk.png)

***Note:*** 請閱讀呢個示範 [click this link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **資源**

1. 學習 Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用此翻譯而引起的任何誤解或誤釋負責。