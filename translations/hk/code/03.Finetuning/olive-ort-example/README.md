<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aed7639909ebbd1960507880cff2ae4c",
  "translation_date": "2025-04-04T17:12:56+00:00",
  "source_file": "code\\03.Finetuning\\olive-ort-example\\README.md",
  "language_code": "hk"
}
-->
# 用 Olive 微調 Phi3

喺呢個例子入面，你會用 Olive 嚟：

1. 微調 LoRA adapter，將短句分類為 Sad（傷心）、Joy（開心）、Fear（驚慌）、Surprise（驚訝）。
1. 將 adapter 權重合併到基礎模型入面。
1. 優化同量化模型到 `int4`。

我哋仲會教你點樣用 ONNX Runtime (ORT) Generate API 去推理經微調嘅模型。

> **⚠️ 微調需要一個合適嘅 GPU，例如 A10、V100、A100。**

## 💾 安裝

創建一個新嘅 Python 虛擬環境（例如用 `conda`）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

之後，安裝 Olive 同埋微調工作流程所需嘅依賴：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 用 Olive 微調 Phi3
[Olive 配置文件](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) 包含咗一個 *工作流程*，當中有以下 *步驟*：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

從高層次睇，呢個工作流程會：

1. 用 [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) 嘅數據微調 Phi3（150 步，你可以修改呢個數字）。
1. 將 LoRA adapter 權重合併到基礎模型，生成一個 ONNX 格式嘅單一模型工件。
1. 用 Model Builder 優化模型以適配 ONNX runtime，並將模型量化到 `int4`。

執行呢個工作流程：

```bash
olive run --config phrase-classification.json
```

當 Olive 完成之後，你經優化嘅 `int4` 微調 Phi3 模型會喺呢度：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`。

## 🧑‍💻 將微調後嘅 Phi3 整合到你嘅應用程式 

運行應用程式：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

呢個回應應該係短句嘅單字分類（Sad/ Joy/ Fear/ Surprise）。

**免責聲明**：  
此文件已使用AI翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們努力確保翻譯準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原文檔的母語版本應被視為具權威性的來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。