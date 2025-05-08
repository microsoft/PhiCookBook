<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-07T14:50:26+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "zh"
}
-->
# **使用 Apple MLX 框架量化 Phi-3.5**

MLX 是一个专为 Apple 硅芯片上的机器学习研究设计的数组框架，由 Apple 机器学习研究团队推出。

MLX 由机器学习研究人员为机器学习研究人员设计。该框架旨在用户友好，同时在训练和部署模型时保持高效。框架本身的设计理念也非常简单。我们希望让研究人员能够轻松扩展和改进 MLX，以便快速探索新想法。

通过 MLX，LLM 可以在 Apple 硅芯片设备上加速运行，且模型可以非常方便地本地执行。

目前 Apple MLX 框架支持 Phi-3.5-Instruct（**Apple MLX Framework 支持**）、Phi-3.5-Vision（**MLX-VLM Framework 支持**）和 Phi-3.5-MoE（**Apple MLX Framework 支持**）的量化转换。接下来我们来试试：

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

### **🤖 Apple MLX 上 Phi-3.5 示例**

| 实验室    | 介绍 | 入口 |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | 学习如何使用 Apple MLX 框架运行 Phi-3.5 Instruct   |  [入口](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | 学习如何使用 Apple MLX 框架通过 Phi-3.5 Vision 进行图像分析     |  [入口](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | 学习如何使用 Apple MLX 框架运行 Phi-3.5 MoE  |  [入口](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **资源**

1. 了解 Apple MLX 框架 [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub 仓库 [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub 仓库 [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**免责声明**：  
本文件使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。