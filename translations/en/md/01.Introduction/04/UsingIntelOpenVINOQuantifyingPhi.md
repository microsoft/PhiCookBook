# **Quantizing Phi-3.5 using Intel OpenVINO**

Intel is the most traditional CPU manufacturer with a large user base. With the rise of machine learning and deep learning, Intel has also entered the AI acceleration race. For model inference, Intel utilizes not only GPUs and CPUs but also NPUs.

We aim to deploy the Phi-3.x Family on edge devices, hoping it becomes a key component of AI PCs and Copilot PCs. Loading the model on edge devices depends on collaboration with various hardware manufacturers. This chapter mainly focuses on the application scenario of Intel OpenVINO as a quantization tool.

## **What’s OpenVINO**

OpenVINO is an open-source toolkit for optimizing and deploying deep learning models from cloud to edge. It speeds up deep learning inference across various use cases such as generative AI, video, audio, and language, supporting models from popular frameworks like PyTorch, TensorFlow, ONNX, and more. It allows you to convert and optimize models and deploy them across a range of Intel® hardware and environments, whether on-premises, on-device, in the browser, or in the cloud.

With OpenVINO, you can quickly quantize GenAI models on Intel hardware and accelerate model inference.

Currently, OpenVINO supports quantization conversion for Phi-3.5-Vision and Phi-3.5 Instruct.

### **Environment Setup**

Please make sure the following environment dependencies are installed, as listed in requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Quantizing Phi-3.5-Instruct using OpenVINO**

In the terminal, please run this script

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Quantizing Phi-3.5-Vision using OpenVINO**

Please run this script in Python or Jupyter Lab

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

### **🤖 Samples for Phi-3.5 with Intel OpenVINO**

| Labs    | Description | Go |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Learn how to use Phi-3.5 Instruct on your AI PC    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Learn how to use Phi-3.5 Vision to analyze images on your AI PC      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | Learn how to use Phi-3.5 Vision to analyze videos on your AI PC    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Resources**

1. Learn more about Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.