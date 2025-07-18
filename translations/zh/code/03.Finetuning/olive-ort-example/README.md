<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:01:36+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "zh"
}
-->
# 使用 Olive 微调 Phi3

在本示例中，你将使用 Olive 来：

1. 微调一个 LoRA 适配器，将短语分类为 Sad、Joy、Fear、Surprise。
1. 将适配器权重合并到基础模型中。
1. 优化并量化模型为 `int4`。

我们还将演示如何使用 ONNX Runtime (ORT) Generate API 推理微调后的模型。

> **⚠️ 进行微调时，需要有合适的 GPU 可用，例如 A10、V100、A100。**

## 💾 安装

创建一个新的 Python 虚拟环境（例如，使用 `conda`）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

接下来，安装 Olive 及微调工作流所需的依赖：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 使用 Olive 微调 Phi3
[Olive 配置文件](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) 包含一个带有以下 *passes* 的 *workflow*：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

从整体上看，该工作流将：

1. 使用 [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) 数据微调 Phi3（共 150 步，可修改）。
1. 将 LoRA 适配器权重合并到基础模型中，生成一个单一的 ONNX 格式模型文件。
1. Model Builder 会针对 ONNX 运行时优化模型，并将模型量化为 `int4`。

执行工作流，运行：

```bash
olive run --config phrase-classification.json
```

当 Olive 完成后，你优化并量化为 `int4` 的微调 Phi3 模型将保存在：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`。

## 🧑‍💻 将微调后的 Phi3 集成到你的应用中

运行应用：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

该响应应为短语的单词分类结果（Sad/Joy/Fear/Surprise）。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。