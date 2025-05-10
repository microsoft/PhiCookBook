<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-05-09T13:53:35+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "pa"
}
-->
# **Intel OpenVINO ਨਾਲ Phi-3.5 ਨੂੰ Quantize ਕਰਨਾ**

Intel ਸਭ ਤੋਂ ਪਰੰਪਰਾਗਤ CPU ਨਿਰਮਾਤਾ ਹੈ ਜਿਸਦੇ ਬਹੁਤ ਸਾਰੇ ਉਪਭੋਗਤਾ ਹਨ। ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਅਤੇ ਡੀਪ ਲਰਨਿੰਗ ਦੇ ਉਭਾਰ ਨਾਲ, Intel ਵੀ AI ਐਕਸਲੇਰੇਸ਼ਨ ਦੀ ਮੁਕਾਬਲੇਬਾਜ਼ੀ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋ ਗਿਆ ਹੈ। ਮਾਡਲ ਇੰਫਰੰਸ ਲਈ, Intel ਸਿਰਫ GPUs ਅਤੇ CPUs ਹੀ ਨਹੀਂ ਵਰਤਦਾ, ਬਲਕਿ NPUs ਵੀ ਵਰਤਦਾ ਹੈ।

ਅਸੀਂ Phi-3.x ਪਰਿਵਾਰ ਨੂੰ ਐਂਡ ਸਾਈਡ 'ਤੇ ਡਿਪਲੋਇ ਕਰਨ ਦੀ ਆਸ ਕਰਦੇ ਹਾਂ, ਤਾਂ ਜੋ ਇਹ AI PC ਅਤੇ Copilot PC ਦਾ ਸਭ ਤੋਂ ਮਹੱਤਵਪੂਰਨ ਹਿੱਸਾ ਬਣ ਸਕੇ। ਐਂਡ ਸਾਈਡ 'ਤੇ ਮਾਡਲ ਲੋਡਿੰਗ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਨਿਰਮਾਤਿਆਂ ਦੇ ਸਹਿਯੋਗ 'ਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ। ਇਹ ਅਧਿਆਇ ਮੁੱਖ ਤੌਰ 'ਤੇ Intel OpenVINO ਦੇ ਕਵਾਂਟਾਈਜ਼ ਮਾਡਲ ਦੇ ਐਪਲੀਕੇਸ਼ਨ ਸਿਨਾਰਿਓ 'ਤੇ ਧਿਆਨ ਕੇਂਦ੍ਰਿਤ ਕਰਦਾ ਹੈ।

## **OpenVINO ਕੀ ਹੈ**

OpenVINO ਇੱਕ ਖੁੱਲਾ ਸ੍ਰੋਤ ਟੂਲਕਿਟ ਹੈ ਜੋ ਡੀਪ ਲਰਨਿੰਗ ਮਾਡਲਾਂ ਨੂੰ ਕਲਾਉਡ ਤੋਂ ਐਜ ਤੱਕ ਅਪਟਿਮਾਈਜ਼ ਅਤੇ ਡਿਪਲੋਇ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ। ਇਹ ਜਨਰੇਟਿਵ AI, ਵੀਡੀਓ, ਆਡੀਓ, ਅਤੇ ਭਾਸ਼ਾ ਵਰਗੇ ਵੱਖ-ਵੱਖ ਮਾਮਲਿਆਂ ਵਿੱਚ ਡੀਪ ਲਰਨਿੰਗ ਇੰਫਰੰਸ ਨੂੰ ਤੇਜ਼ ਕਰਦਾ ਹੈ, ਜਿੱਥੇ PyTorch, TensorFlow, ONNX ਅਤੇ ਹੋਰ ਲੋਕਪ੍ਰਿਯ ਫਰੇਮਵਰਕਾਂ ਦੇ ਮਾਡਲ ਵਰਤੇ ਜਾਂਦੇ ਹਨ। ਮਾਡਲਾਂ ਨੂੰ ਕਨਵਰਟ ਅਤੇ ਅਪਟਿਮਾਈਜ਼ ਕਰੋ, ਅਤੇ Intel® ਹਾਰਡਵੇਅਰ ਅਤੇ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ, ਚਾਹੇ ਉਹ ਓਨ-ਪ੍ਰੈਮਿਸਿਜ਼ ਹੋਣ ਜਾਂ ਡਿਵਾਈਸ 'ਤੇ, ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਜਾਂ ਕਲਾਉਡ ਵਿੱਚ, ਡਿਪਲੋਇ ਕਰੋ।

ਹੁਣ OpenVINO ਨਾਲ, ਤੁਸੀਂ Intel ਹਾਰਡਵੇਅਰ 'ਤੇ GenAI ਮਾਡਲ ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਕਵਾਂਟਾਈਜ਼ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ ਮਾਡਲ ਰੈਫਰੈਂਸ ਨੂੰ ਐਕਸਲੇਰੇਟ ਕਰ ਸਕਦੇ ਹੋ।

ਹੁਣ OpenVINO Phi-3.5-Vision ਅਤੇ Phi-3.5 Instruct ਦੀ ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ ਕਨਵਰਜ਼ਨ ਨੂੰ ਸਹਿਯੋਗ ਦਿੰਦਾ ਹੈ।

### **ਵਾਤਾਵਰਣ ਸੈਟਅਪ**

ਕਿਰਪਾ ਕਰਕੇ ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਹੇਠਾਂ ਦਿੱਤੇ ਵਾਤਾਵਰਣ ਨਿਰਭਰਤਾਵਾਂ ਇੰਸਟਾਲ ਹਨ, ਇਹ requirement.txt ਹੈ

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **OpenVINO ਨਾਲ Phi-3.5-Instruct ਨੂੰ Quantize ਕਰਨਾ**

Terminal ਵਿੱਚ, ਕਿਰਪਾ ਕਰਕੇ ਇਹ ਸਕ੍ਰਿਪਟ ਚਲਾਓ

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **OpenVINO ਨਾਲ Phi-3.5-Vision ਨੂੰ Quantize ਕਰਨਾ**

Python ਜਾਂ Jupyter lab ਵਿੱਚ ਇਹ ਸਕ੍ਰਿਪਟ ਚਲਾਓ

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

### **🤖 Intel OpenVINO ਨਾਲ Phi-3.5 ਲਈ ਸੈਂਪਲ**

| Labs    | ਜਾਣ-ਪਛਾਣ | ਜਾਓ |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | ਆਪਣੀ AI PC ਵਿੱਚ Phi-3.5 Instruct ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਸਿੱਖੋ    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | ਆਪਣੀ AI PC ਵਿੱਚ Phi-3.5 Vision ਨਾਲ ਤਸਵੀਰਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਿਵੇਂ ਕਰਨਾ ਸਿੱਖੋ      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | ਆਪਣੀ AI PC ਵਿੱਚ Phi-3.5 Vision ਨਾਲ ਵੀਡੀਓ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਿਵੇਂ ਕਰਨਾ ਸਿੱਖੋ    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **ਸੰਸਾਧਨ**

1. Intel OpenVINO ਬਾਰੇ ਹੋਰ ਜਾਣੋ [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub ਰਿਪੋ [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪ੍ਰੋਫੈਸ਼ਨਲ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।