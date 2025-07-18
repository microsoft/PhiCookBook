<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:52:59+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "zh"
}
-->
# **使用 Apple MLX 框架对 Phi-3.5 进行量化**

MLX 是一个面向 Apple 硅芯片的机器学习研究数组框架，由 Apple 机器学习研究团队推出。

MLX 由机器学习研究人员为机器学习研究人员设计。该框架旨在用户友好，同时在训练和部署模型时保持高效。框架本身的设计也非常简洁。我们的目标是让研究人员能够轻松扩展和改进 MLX，以便快速探索新想法。

通过 MLX，Apple 硅芯片设备上的大型语言模型（LLMs）可以加速运行，且模型可以非常方便地在本地执行。

目前 Apple MLX 框架支持 Phi-3.5-Instruct 的量化转换（**Apple MLX Framework support**）、Phi-3.5-Vision（**MLX-VLM Framework support**）以及 Phi-3.5-MoE（**Apple MLX Framework support**）。接下来让我们试试：

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

### **🤖 Apple MLX 上 Phi-3.5 的示例**

| 实验室    | 介绍 | 进入 |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | 学习如何使用 Apple MLX 框架运行 Phi-3.5 Instruct   |  [进入](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | 学习如何使用 Apple MLX 框架通过 Phi-3.5 Vision 分析图像     |  [进入](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | 学习如何使用 Apple MLX 框架运行 Phi-3.5 MoE  |  [进入](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **资源**

1. 了解 Apple MLX 框架 [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub 仓库 [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub 仓库 [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。