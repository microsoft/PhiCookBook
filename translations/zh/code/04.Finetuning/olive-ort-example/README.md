<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aed7639909ebbd1960507880cff2ae4c",
  "translation_date": "2025-04-03T06:18:37+00:00",
  "source_file": "code\\04.Finetuning\\olive-ort-example\\README.md",
  "language_code": "zh"
}
-->
# 使用 Olive 微调 Phi3

在这个示例中，你将使用 Olive 来完成以下任务：

1. 微调一个 LoRA 适配器，将短语分类为 Sad、Joy、Fear、Surprise。
2. 将适配器权重合并到基础模型中。
3. 优化并量化模型为 `int4`。

我们还将向你展示如何使用 ONNX Runtime (ORT) 的生成 API 对微调后的模型进行推理。

> **⚠️ 微调需要一块合适的 GPU，例如 A10、V100、A100。**

## 💾 安装

创建一个新的 Python 虚拟环境（例如使用 `conda`）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

接下来，安装 Olive 和微调工作流所需的依赖：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 使用 Olive 微调 Phi3

[Olive 配置文件](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) 包含一个 *工作流*，包括以下 *passes*：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

从高层次来看，这个工作流将执行以下任务：

1. 使用 [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) 数据对 Phi3 进行微调（150步，你可以修改这个值）。
2. 将 LoRA 适配器权重合并到基础模型中。这将生成一个 ONNX 格式的单一模型文件。
3. Model Builder 将优化模型以适配 ONNX Runtime，并将模型量化为 `int4`。

要执行这个工作流，请运行：

```bash
olive run --config phrase-classification.json
```

当 Olive 完成后，优化的 `int4` 微调 Phi3 模型将位于以下路径：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`。

## 🧑‍💻 将微调后的 Phi3 集成到你的应用中

运行应用程序：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

输出将是短语的单词分类结果（Sad/Joy/Fear/Surprise）。

**免责声明**:  
本文档使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们尽力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对于因使用此翻译而产生的任何误解或误读不承担责任。