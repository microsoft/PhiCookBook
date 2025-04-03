<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "74689a2b87f747d751edfec988ccb7fd",
  "translation_date": "2025-04-03T08:19:09+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Phi-3-visionWandB.md",
  "language_code": "zh"
}
-->
# Phi-3-Vision-128K-Instruct 项目概览

## 模型

Phi-3-Vision-128K-Instruct 是本项目的核心，它是一款轻量级、先进的多模态模型，属于 Phi-3 模型家族，支持最长 128,000 个 token 的上下文长度。该模型基于多样化的数据集进行训练，数据集包括合成数据和经过严格筛选的公开网站内容，重点关注高质量、需要复杂推理的内容。训练过程中包含监督微调和直接偏好优化，以确保对指令的精准遵循，同时实施了强大的安全措施。

## 创建样本数据至关重要的几个原因：

1. **测试**：样本数据允许您在各种场景下测试应用程序，而不会影响真实数据。这在开发和测试阶段尤为重要。

2. **性能调优**：使用模拟真实数据规模和复杂性的样本数据，您可以识别性能瓶颈并优化应用程序。

3. **原型设计**：样本数据可用于创建原型和模型，有助于理解用户需求并获得反馈。

4. **数据分析**：在数据科学中，样本数据通常用于探索性数据分析、模型训练和算法测试。

5. **安全性**：在开发和测试环境中使用样本数据可以防止敏感真实数据意外泄漏。

6. **学习**：如果您正在学习新技术或工具，使用样本数据可以为您提供实践应用所学知识的机会。

请记住，样本数据的质量对这些活动的影响非常重要。它的结构和变异性应尽可能接近真实数据。

### 样本数据创建
[生成数据集脚本](./CreatingSampleData.md)

## 数据集

一个好的样本数据集示例是 [DBQ/Burberry.Product.prices.United.States 数据集](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States)（可在 Huggingface 上获取）。  
该样本数据集包含 Burberry 产品的相关信息，以及产品类别、价格和标题的元数据，共计 3,040 行，每行代表一个独特产品。此数据集可用于测试模型理解和解释视觉数据的能力，生成捕捉复杂视觉细节和品牌特征的描述性文本。

**注意：** 您可以使用任何包含图像的数据集。

## 复杂推理

模型需要仅通过图像对价格和命名进行推理。这要求模型不仅能够识别视觉特征，还能理解这些特征在产品价值和品牌方面的意义。通过从图像生成准确的文本描述，这个项目展示了将视觉数据整合以增强模型在实际应用中的性能和多功能性的潜力。

## Phi-3 Vision 架构

该模型架构是 Phi-3 的多模态版本，能够同时处理文本和图像数据，将这些输入整合为统一序列，用于全面理解和生成任务。模型为文本和图像分别使用独立的嵌入层。文本 token 被转换为密集向量，而图像则通过 CLIP 视觉模型处理以提取特征嵌入。这些图像嵌入随后被投射以匹配文本嵌入的维度，从而确保它们可以无缝整合。

## 文本和图像嵌入的整合

文本序列中的特殊 token 指示图像嵌入应插入的位置。在处理过程中，这些特殊 token 被对应的图像嵌入替换，使模型能够将文本和图像作为单一序列进行处理。我们数据集的提示格式使用特殊的 <|image|> token，如下所示：

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## 示例代码
- [Phi-3-Vision 训练脚本](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias 示例讲解](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的原始文档作为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而引发的任何误解或误读承担责任。