<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-08T06:36:17+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "hk"
}
-->
# 用 Olive 微調 Phi3

喺呢個例子，你會用 Olive 去：

1. 微調一個 LoRA adapter，將短語分類成 Sad、Joy、Fear、Surprise。
1. 將 adapter 權重合併到基礎模型。
1. 將模型優化同量化成 `int4`。

我哋亦會示範點樣用 ONNX Runtime (ORT) Generate API 去推理微調後嘅模型。

> **⚠️ 微調時，你需要有合適嘅 GPU，例如 A10、V100、A100。**

## 💾 安裝

建立一個新嘅 Python 虛擬環境（例如用 `conda`）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

然後安裝 Olive 同微調工作流程嘅依賴：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 用 Olive 微調 Phi3
[Olive 配置文件](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) 包含一個 *workflow*，有以下嘅 *passes*：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

大致上，呢個工作流程會：

1. 用 [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) 數據微調 Phi3（150 步，可自行修改）。
1. 將 LoRA adapter 權重合併到基礎模型，得到一個 ONNX 格式嘅單一模型文件。
1. Model Builder 會為 ONNX runtime 優化模型，並且將模型量化成 `int4`。

執行工作流程，請運行：

```bash
olive run --config phrase-classification.json
```

完成後，你優化同微調過嘅 `int4` Phi3 模型會喺：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`。

## 🧑‍💻 將微調嘅 Phi3 整合到你嘅應用程式

運行應用程式：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

呢個回應會係短語嘅單一字分類（Sad/Joy/Fear/Surprise）。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我哋盡力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件嘅母語版本應視為權威來源。對於重要資料，建議採用專業人工翻譯。我哋對因使用此翻譯而引起嘅任何誤解或誤釋概不負責。