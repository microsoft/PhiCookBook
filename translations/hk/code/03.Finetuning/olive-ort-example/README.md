<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:01:50+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "hk"
}
-->
# 使用 Olive 微調 Phi3

在這個範例中，你將使用 Olive 來：

1. 微調 LoRA adapter，將短語分類為 Sad、Joy、Fear、Surprise。
1. 將 adapter 權重合併到基礎模型中。
1. 將模型優化並量化為 `int4`。

我們也會示範如何使用 ONNX Runtime (ORT) Generate API 來推理微調後的模型。

> **⚠️ 進行微調時，需要有合適的 GPU，例如 A10、V100、A100。**

## 💾 安裝

建立一個新的 Python 虛擬環境（例如使用 `conda`）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

接著，安裝 Olive 以及微調工作流程所需的依賴：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 使用 Olive 微調 Phi3
[Olive 配置檔](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) 包含一個 *workflow*，裡面有以下 *passes*：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

大致來說，這個工作流程會：

1. 使用 [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) 的資料，微調 Phi3（150 步，可自行調整）。
1. 將 LoRA adapter 權重合併到基礎模型中，產生一個 ONNX 格式的單一模型檔案。
1. Model Builder 會針對 ONNX runtime 優化模型，並將模型量化為 `int4`。

執行工作流程，請運行：

```bash
olive run --config phrase-classification.json
```

當 Olive 完成後，你優化且量化為 `int4` 的微調 Phi3 模型會在：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`。

## 🧑‍💻 將微調後的 Phi3 整合到你的應用程式中

執行應用程式：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

回應應該是對短語的單字分類（Sad/Joy/Fear/Surprise）。

**免責聲明**：  
本文件乃使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。