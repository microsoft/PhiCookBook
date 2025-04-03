<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f766ec7e68d97f6009b58794b471d66",
  "translation_date": "2025-04-03T07:03:42+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "zh"
}
-->
# **使用 Intel OpenVINO 对 Phi-3.5 进行量化**

Intel 是最传统的 CPU 制造商之一，拥有众多用户。随着机器学习和深度学习的兴起，Intel 也加入了 AI 加速的竞争。为了进行模型推理，Intel 不仅使用 GPU 和 CPU，还使用 NPU。

我们希望将 Phi-3.x 系列部署到终端设备上，成为 AI PC 和 Copilot PC 的重要组成部分。模型在终端设备上的加载需要不同硬件制造商的协作。本章主要聚焦于使用 Intel OpenVINO 作为量化模型的应用场景。

## **什么是 OpenVINO**

OpenVINO 是一个开源工具包，用于优化和部署从云到边缘的深度学习模型。它加速了深度学习推理，适用于各种场景，比如生成式 AI、视频、音频和语言处理，并支持来自主流框架（如 PyTorch、TensorFlow、ONNX 等）的模型。通过转换和优化模型，可以在各种 Intel® 硬件和环境中部署，包括本地设备、浏览器或云端。

借助 OpenVINO，您可以快速在 Intel 硬件上量化生成式 AI 模型，并加速模型推理。

目前，OpenVINO 支持对 Phi-3.5-Vision 和 Phi-3.5-Instruct 的量化转换。

### **环境配置**

请确保安装以下环境依赖项，这是 requirement.txt 文件内容：

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **使用 OpenVINO 对 Phi-3.5-Instruct 进行量化**

在终端中运行以下脚本：

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **使用 OpenVINO 对 Phi-3.5-Vision 进行量化**

请在 Python 或 Jupyter Lab 中运行以下脚本：

```python

import requests
from pathlib import Path
from ov_phi3_vision import convert_phi3_model
import nncf

if not Path("ov_phi3_vision.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/ov_phi3_vision.py")
    open("ov_phi3_vision.py", "w").write(r.text)


if not Path("gradio_helper.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/gradio_helper.py")
    open("gradio_helper.py", "w").write(r.text)

if not Path("notebook_utils.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/utils/notebook_utils.py")
    open("notebook_utils.py", "w").write(r.text)



model_id = "microsoft/Phi-3.5-vision-instruct"
out_dir = Path("../model/phi-3.5-vision-128k-instruct-ov")
compression_configuration = {
    "mode": nncf.CompressWeightsMode.INT4_SYM,
    "group_size": 64,
    "ratio": 0.6,
}
if not out_dir.exists():
    convert_phi3_model(model_id, out_dir, compression_configuration)

```

### **🤖 使用 Intel OpenVINO 的 Phi-3.5 示例**

| 实验室    | 介绍 | 前往 |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | 了解如何在您的 AI PC 中使用 Phi-3.5 Instruct    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | 了解如何在您的 AI PC 中使用 Phi-3.5 Vision 分析图像      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | 了解如何在您的 AI PC 中使用 Phi-3.5 Vision 分析视频    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **资源**

1. 了解更多关于 Intel OpenVINO 的信息 [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub 仓库 [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们尽力确保翻译的准确性，但请注意，自动翻译可能会包含错误或不准确之处。原文档的母语版本应被视为权威来源。对于关键信息，建议使用专业的人工翻译服务。我们对于因使用此翻译而产生的任何误解或误读不承担责任。