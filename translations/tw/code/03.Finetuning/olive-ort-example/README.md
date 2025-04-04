<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aed7639909ebbd1960507880cff2ae4c",
  "translation_date": "2025-04-04T05:23:15+00:00",
  "source_file": "code\\03.Finetuning\\olive-ort-example\\README.md",
  "language_code": "tw"
}
-->
# 使用 Olive 微調 Phi3

在這個範例中，你將使用 Olive 來：

1. 微調 LoRA 適配器以將短語分類為 Sad（悲傷）、Joy（喜悅）、Fear（恐懼）、Surprise（驚訝）。
2. 將適配器的權重合併到基礎模型中。
3. 優化並量化模型為 `int4`。

我們還會向你展示如何使用 ONNX Runtime (ORT) 的 Generate API 來推論微調後的模型。

> **⚠️ 微調需要有合適的 GPU，例如 A10、V100、A100。**

## 💾 安裝

建立一個新的 Python 虛擬環境（例如，使用 `conda`）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

接下來，安裝 Olive 和微調工作流程所需的依賴項：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 使用 Olive 微調 Phi3
[Olive 配置檔案](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) 包含一個包含以下 *步驟* 的 *工作流程*：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

在高層次上，這個工作流程會執行以下操作：

1. 使用 [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) 數據對 Phi3 進行微調（進行 150 步，你可以自行修改）。
2. 將 LoRA 適配器的權重合併到基礎模型中。這將生成一個 ONNX 格式的單一模型文件。
3. 使用 Model Builder 優化模型以適配 ONNX runtime，並將模型量化為 `int4`。

執行工作流程的命令如下：

```bash
olive run --config phrase-classification.json
```

當 Olive 完成後，你的經過優化的 `int4` 微調 Phi3 模型將位於：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`。

## 🧑‍💻 將微調後的 Phi3 整合到你的應用中 

執行應用程式：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

這個回應應該是一個單詞，用來分類短語（Sad/Joy/Fear/Surprise）。

**免責聲明**：  
本文檔使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力保證翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不精確之處。原始語言的文件應被視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們不對因使用此翻譯而引起的任何誤解或誤讀承擔責任。