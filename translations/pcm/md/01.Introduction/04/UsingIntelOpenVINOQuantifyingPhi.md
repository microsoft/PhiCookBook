# **Quantizing Phi-3.5 wit Intel OpenVINO**

Intel na di most traditional CPU manufacturer wey get plenty users. As machine learning and deep learning don dey rise, Intel don join di competition for AI acceleration. For model inference, Intel no dey use only GPUs and CPUs, e still dey use NPUs.

We dey hope to deploy Phi-3.x Family for di end side, want make e turn di most important part of AI PC and Copilot PC. How model dey load for di end side depend on cooperation between different hardware manufacturers. Dis chapter mainly dey focus on how Intel OpenVINO dey apply for model quantization.

## **Wetin be OpenVINO**

OpenVINO na open-source toolkit wey dem dey use to optimize and deploy deep learning models from cloud go edge. E dey accelerate deep learning inference for many use cases like generative AI, video, audio, and language with models from popular frameworks like PyTorch, TensorFlow, ONNX, and more. You fit convert and optimize models, then deploy across mix of Intel® hardware and environments — on-premises and on-device, for di browser or for di cloud.

Now with OpenVINO, you fit quick-quick quantize di GenAI model for Intel hardware and speed up di model reference.

Now OpenVINO dey support quantization conversion of Phi-3.5-Vision and Phi-3.5 Instruct

### **How to set up di environment**

Please make sure say di following environment dependencies don install, dis na requirement.txt 

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Quantizing Phi-3.5-Instruct wit OpenVINO**

For Terminal, abeg run dis script


```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Quantizing Phi-3.5-Vision wit OpenVINO**

Abeg run dis script for Python or Jupyter lab

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

### **🤖 Samples for Phi-3.5 wit Intel OpenVINO**

| Labs    | Introduce | Go |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Make you sabi how to use Phi-3.5 Instruct for your AI PC    |  [Open](../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Make you sabi how to use Phi-3.5 Vision to analyze image for your AI PC      |  [Open](../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | Make you sabi how to use Phi-3.5 Vision to analyze image for your AI PC    |  [Open](../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |



## **Resources**

1. Make yourself sabi more about Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate by AI translation service [Co-op Translator]. Even though we dey try make am correct, abeg sabi say automated translations fit get mistakes or inaccuracies. Di original document for im native language na di main/official source. If na important information, make you use professional human translator. We no go take responsibility for any misunderstanding or wrong interpretation wey fit come from using this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->