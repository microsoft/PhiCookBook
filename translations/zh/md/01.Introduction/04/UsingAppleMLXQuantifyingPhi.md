<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "340bd4c009524ef84102b78d06eea735",
  "translation_date": "2025-04-03T07:02:41+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingAppleMLXQuantifyingPhi.md",
  "language_code": "zh"
}
-->
# **使用 Apple MLX 框架量化 Phi-3.5**

MLX 是一个专为 Apple Silicon 设备设计的机器学习研究框架，由 Apple 机器学习研究团队推出。

MLX 专为机器学习研究人员设计，旨在提供友好的用户体验，同时仍保持高效的模型训练和部署能力。框架的设计理念非常简单直观，方便研究人员扩展和优化 MLX，以快速探索新的研究思路。

通过 MLX，可以在 Apple Silicon 设备上加速 LLM，并且能够非常方便地在本地运行模型。

现在 Apple MLX 框架支持 Phi-3.5-Instruct（**Apple MLX 框架支持**）、Phi-3.5-Vision（**MLX-VLM 框架支持**）和 Phi-3.5-MoE（**Apple MLX 框架支持**）的量化转换。接下来让我们试试：

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 使用 Apple MLX 的 Phi-3.5 示例**

| 实验室    | 简介       | 访问链接  |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | 学习如何使用 Apple MLX 框架运行 Phi-3.5 Instruct   |  [访问](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | 学习如何使用 Apple MLX 框架运行 Phi-3.5 Vision 分析图像     |  [访问](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | 学习如何使用 Apple MLX 框架运行 Phi-3.5 MoE   |  [访问](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **资源**

1. 了解 Apple MLX 框架 [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub 仓库 [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub 仓库 [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言版本的文件作为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而引起的任何误解或误读不承担责任。