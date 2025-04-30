<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aed7639909ebbd1960507880cff2ae4c",
  "translation_date": "2025-04-04T05:25:36+00:00",
  "source_file": "code\\04.Finetuning\\olive-ort-example\\README.md",
  "language_code": "tw"
}
-->
# 使用 Olive 微調 Phi3

在這個範例中，你將使用 Olive 來：

1. 微調 LoRA 適配器以將短語分類為 Sad、Joy、Fear、Surprise。
2. 將適配器權重合併到基礎模型中。
3. 將模型優化並量化為 `int4`。

我們還會展示如何使用 ONNX Runtime (ORT) 的 Generate API 對微調後的模型進行推理。

> **⚠️ 微調需要可用的合適 GPU，例如 A10、V100、A100。**

## 💾 安裝

創建一個新的 Python 虛擬環境（例如，使用 `conda`）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

接著，安裝 Olive 和微調工作流程所需的依賴項：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 使用 Olive 微調 Phi3
[Olive 配置文件](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) 包含了一個包含以下 *passes* 的 *工作流程*：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

從高層次來看，這個工作流程將執行以下操作：

1. 使用 [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) 數據微調 Phi3（執行 150 步，你可以進行修改）。
2. 將 LoRA 適配器權重合併到基礎模型中。這將生成一個 ONNX 格式的單一模型工件。
3. Model Builder 將優化模型以適配 ONNX runtime *並* 將模型量化為 `int4`。

要執行工作流程，請運行：

```bash
olive run --config phrase-classification.json
```

當 Olive 完成後，優化的 `int4` 微調 Phi3 模型將可用於：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`。

## 🧑‍💻 將微調後的 Phi3 整合到你的應用中

要運行應用：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

此回應應為短語的單詞分類（Sad/Joy/Fear/Surprise）。

**免責聲明**：  
本文檔使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能會包含錯誤或不準確之處。原文檔的母語版本應被視為權威來源。對於重要信息，建議尋求專業人工翻譯。我們不對因使用此翻譯而引起的任何誤解或誤釋承擔責任。