<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aed7639909ebbd1960507880cff2ae4c",
  "translation_date": "2025-04-04T17:15:38+00:00",
  "source_file": "code\\04.Finetuning\\olive-ort-example\\README.md",
  "language_code": "hk"
}
-->
# 使用 Olive 微調 Phi3

在這個例子中，你將使用 Olive 來：

1. 微調 LoRA 配接器以將短語分類為 Sad、Joy、Fear、Surprise。
1. 將配接器的權重合併到基礎模型中。
1. 優化並量化模型成 `int4`。

我們還會向你展示如何使用 ONNX Runtime (ORT) Generate API 進行微調模型的推理。

> **⚠️ 微調需要有合適的 GPU，例如 A10、V100、A100。**

## 💾 安裝

創建一個新的 Python 虛擬環境（例如，使用 `conda`）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

接著，安裝 Olive 和微調工作流程所需的依賴：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 使用 Olive 微調 Phi3
[Olive 配置文件](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) 包含一個包含以下 *passes* 的 *workflow*：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

從高層次來看，這個工作流程將：

1. 使用 [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) 數據微調 Phi3（進行 150 步，你可以修改）。
1. 將 LoRA 配接器的權重合併到基礎模型中。這將生成一個 ONNX 格式的單一模型工件。
1. Model Builder 將優化模型以適應 ONNX runtime，並量化模型成 `int4`。

執行工作流程，運行：

```bash
olive run --config phrase-classification.json
```

當 Olive 完成後，你優化過的 `int4` 微調 Phi3 模型可在以下位置找到：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`。

## 🧑‍💻 將微調 Phi3 整合到你的應用中

運行應用：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

該回應應為短語的單詞分類（Sad/Joy/Fear/Surprise）。

**免責聲明**:  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力確保翻譯準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的原文應被視為具權威性的來源。對於關鍵信息，建議使用專業人工翻譯。我們不對因使用此翻譯而產生的任何誤解或誤釋承擔責任。