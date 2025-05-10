<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-05-09T14:02:13+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "cs"
}
-->
# **使用 Intel OpenVINO 对 Phi-3.5 进行量化**

Intel 是历史最悠久的 CPU 制造商，拥有大量用户。随着机器学习和深度学习的发展，Intel 也加入了 AI 加速的竞争。对于模型推理，Intel 不仅使用 GPU 和 CPU，还使用 NPU。

我们希望将 Phi-3.x 系列部署到终端设备，期望成为 AI PC 和 Copilot PC 最重要的组成部分。终端侧模型的加载依赖于不同硬件厂商的合作。本章主要聚焦于 Intel OpenVINO 作为量化模型的应用场景。


## **什么是 OpenVINO**

OpenVINO 是一个开源工具包，用于优化和部署从云端到边缘的深度学习模型。它加速了各种应用场景下的深度学习推理，如生成式 AI、视频、音频和语言，支持来自 PyTorch、TensorFlow、ONNX 等主流框架的模型。可以转换和优化模型，并部署在多种 Intel® 硬件和环境中，包括本地、设备端、浏览器或云端。

借助 OpenVINO，你可以快速在 Intel 硬件上对 GenAI 模型进行量化，并加速模型推理。

目前 OpenVINO 支持对 Phi-3.5-Vision 和 Phi-3.5 Instruct 的量化转换。

### **环境配置**

请确保已安装以下环境依赖，这是 requirement.txt 内容

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **使用 OpenVINO 量化 Phi-3.5-Instruct**

在终端中运行以下脚本


```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **使用 OpenVINO 量化 Phi-3.5-Vision**

请在 Python 或 Jupyter lab 中运行以下脚本

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

### **🤖 Intel OpenVINO 上的 Phi-3.5 示例**

| 实验室    | 介绍 | 入口 |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | 学习如何在你的 AI PC 上使用 Phi-3.5 Instruct    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | 学习如何使用 Phi-3.5 Vision 分析 AI PC 上的图像      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | 学习如何使用 Phi-3.5 Vision 分析 AI PC 上的视频    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |



## **资源**

1. 了解更多 Intel OpenVINO 信息 [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub 仓库 [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné výklady vzniklé použitím tohoto překladu.