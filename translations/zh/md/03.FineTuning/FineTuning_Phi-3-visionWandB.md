<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-07T13:29:15+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "zh"
}
-->
# Phi-3-Vision-128K-Instruct 项目概述

## 模型介绍

Phi-3-Vision-128K-Instruct 是本项目的核心，一个轻量级、先进的多模态模型。它属于 Phi-3 模型家族，支持最长 128,000 令牌的上下文长度。该模型在包含合成数据和经过精心筛选的公开网站数据的多样化数据集上训练，重点强调高质量、注重推理的内容。训练过程中采用了监督微调和直接偏好优化，以确保对指令的精准执行，同时具备强大的安全保障。

## 创建样本数据的重要性体现在多个方面：

1. **测试**：样本数据允许你在不同场景下测试应用程序，而不会影响真实数据。这在开发和预发布阶段尤为重要。

2. **性能调优**：使用模拟真实数据规模和复杂度的样本数据，可以识别性能瓶颈并针对性地优化应用。

3. **原型设计**：样本数据可用于制作原型和模型，有助于理解用户需求并获取反馈。

4. **数据分析**：在数据科学领域，样本数据常用于探索性数据分析、模型训练和算法测试。

5. **安全性**：在开发和测试环境中使用样本数据，有助于防止敏感真实数据的意外泄露。

6. **学习**：如果你正在学习新技术或工具，使用样本数据能提供一个实践应用所学内容的途径。

请记住，样本数据的质量会显著影响上述活动，应尽可能在结构和多样性上接近真实数据。

### 样本数据创建
[Generate DataSet Script](./CreatingSampleData.md)

## 数据集

一个很好的样本数据集示例是 [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States)（可在 Huggingface 上获取）。  
该 Burberry 产品样本数据集包含产品类别、价格和标题的元数据，共计 3,040 行，每行代表一个独特的产品。此数据集可用于测试模型理解和解读视觉数据的能力，生成能够捕捉细致视觉细节和品牌特征的描述性文本。

**Note:** 你可以使用任何包含图片的数据集。

## 复杂推理

模型需要仅凭图片推断价格和命名，这不仅要求模型识别视觉特征，还需理解这些特征在产品价值和品牌上的含义。通过从图像合成准确的文本描述，该项目展示了整合视觉数据提升模型在实际应用中性能和多样性的潜力。

## Phi-3 Vision 架构

该模型架构是 Phi-3 的多模态版本，能够处理文本和图像数据，将两者整合成统一序列，以实现全面的理解和生成任务。模型为文本和图像分别使用不同的嵌入层。文本令牌被转换为密集向量，图像则通过 CLIP 视觉模型提取特征嵌入。随后，图像嵌入被投影到与文本嵌入相同的维度，确保能够无缝融合。

## 文本与图像嵌入的整合

文本序列中的特殊令牌指示图像嵌入的插入位置。处理时，这些特殊令牌被对应的图像嵌入替换，使模型能够将文本和图像作为单一序列处理。我们数据集的提示格式使用了特殊的 <|image|> 令牌，如下所示：

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## 示例代码
- [Phi-3-Vision 训练脚本](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias 示例演练](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。