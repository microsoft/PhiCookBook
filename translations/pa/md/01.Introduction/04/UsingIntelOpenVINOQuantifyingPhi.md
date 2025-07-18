<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-07-16T22:00:50+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "pa"
}
-->
# **Intel OpenVINO ਨਾਲ Phi-3.5 ਦੀ Quantizing**

Intel ਸਭ ਤੋਂ ਪਰੰਪਰਾਗਤ CPU ਨਿਰਮਾਤਾ ਹੈ ਜਿਸਦੇ ਬਹੁਤ ਸਾਰੇ ਉਪਭੋਗਤਾ ਹਨ। ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਅਤੇ ਡੀਪ ਲਰਨਿੰਗ ਦੇ ਉਭਾਰ ਨਾਲ, Intel ਵੀ AI ਤੇਜ਼ੀ ਲਈ ਮੁਕਾਬਲੇ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋ ਗਿਆ ਹੈ। ਮਾਡਲ ਇੰਫਰੈਂਸ ਲਈ, Intel ਸਿਰਫ GPUs ਅਤੇ CPUs ਹੀ ਨਹੀਂ, ਬਲਕਿ NPUs ਵੀ ਵਰਤਦਾ ਹੈ।

ਅਸੀਂ Phi-3.x ਪਰਿਵਾਰ ਨੂੰ ਐਂਡ ਸਾਈਡ 'ਤੇ ਤਾਇਨਾਤ ਕਰਨ ਦੀ ਆਸ ਕਰਦੇ ਹਾਂ, ਜੋ AI PC ਅਤੇ Copilot PC ਦਾ ਸਭ ਤੋਂ ਮਹੱਤਵਪੂਰਨ ਹਿੱਸਾ ਬਣ ਸਕੇ। ਐਂਡ ਸਾਈਡ 'ਤੇ ਮਾਡਲ ਲੋਡਿੰਗ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਨਿਰਮਾਤਿਆਂ ਦੇ ਸਹਿਯੋਗ 'ਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ। ਇਹ ਅਧਿਆਇ ਮੁੱਖ ਤੌਰ 'ਤੇ Intel OpenVINO ਦੇ ਇੱਕ ਮਾਤਰਕ ਮਾਡਲ ਦੇ ਤੌਰ 'ਤੇ ਲਾਗੂ ਕਰਨ ਦੇ ਸੰਦਰਭ 'ਤੇ ਧਿਆਨ ਕੇਂਦ੍ਰਿਤ ਕਰਦਾ ਹੈ।


## **OpenVINO ਕੀ ਹੈ**

OpenVINO ਇੱਕ ਖੁੱਲ੍ਹਾ ਸਰੋਤ ਟੂਲਕਿਟ ਹੈ ਜੋ ਕਲਾਉਡ ਤੋਂ ਐਜ ਤੱਕ ਡੀਪ ਲਰਨਿੰਗ ਮਾਡਲਾਂ ਨੂੰ ਅਪਟੀਮਾਈਜ਼ ਅਤੇ ਤਾਇਨਾਤ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ। ਇਹ ਵੱਖ-ਵੱਖ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਵਿੱਚ ਡੀਪ ਲਰਨਿੰਗ ਇੰਫਰੈਂਸ ਨੂੰ ਤੇਜ਼ ਕਰਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਜਨਰੇਟਿਵ AI, ਵੀਡੀਓ, ਆਡੀਓ ਅਤੇ ਭਾਸ਼ਾ, ਅਤੇ ਇਹ ਮਸ਼ਹੂਰ ਫਰੇਮਵਰਕਾਂ ਜਿਵੇਂ PyTorch, TensorFlow, ONNX ਆਦਿ ਦੇ ਮਾਡਲਾਂ ਨਾਲ ਕੰਮ ਕਰਦਾ ਹੈ। ਮਾਡਲਾਂ ਨੂੰ ਬਦਲੋ ਅਤੇ ਅਪਟੀਮਾਈਜ਼ ਕਰੋ, ਅਤੇ Intel® ਹਾਰਡਵੇਅਰ ਅਤੇ ਵਾਤਾਵਰਣਾਂ ਦੇ ਮਿਲਾਪ 'ਤੇ, ਚਾਹੇ ਉਹ ਓਨ-ਪ੍ਰੇਮਿਸ ਹੋਣ ਜਾਂ ਡਿਵਾਈਸ 'ਤੇ, ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਜਾਂ ਕਲਾਉਡ ਵਿੱਚ, ਤਾਇਨਾਤ ਕਰੋ।

ਹੁਣ OpenVINO ਨਾਲ, ਤੁਸੀਂ Intel ਹਾਰਡਵੇਅਰ ਵਿੱਚ GenAI ਮਾਡਲ ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਕਵਾਂਟਾਈਜ਼ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ ਮਾਡਲ ਰੈਫਰੈਂਸ ਨੂੰ ਤੇਜ਼ ਕਰ ਸਕਦੇ ਹੋ।

ਹੁਣ OpenVINO Phi-3.5-Vision ਅਤੇ Phi-3.5 Instruct ਦੀ ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ ਕਨਵਰਜ਼ਨ ਨੂੰ ਸਹਿਯੋਗ ਦਿੰਦਾ ਹੈ।


### **ਵਾਤਾਵਰਣ ਸੈਟਅਪ**

ਕਿਰਪਾ ਕਰਕੇ ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਵਾਤਾਵਰਣ ਦੀਆਂ ਲੋੜਾਂ ਇੰਸਟਾਲ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ, ਇਹ requirement.txt ਹੈ

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```


### **OpenVINO ਨਾਲ Phi-3.5-Instruct ਦੀ Quantizing**

ਟਰਮੀਨਲ ਵਿੱਚ, ਕਿਰਪਾ ਕਰਕੇ ਇਹ ਸਕ੍ਰਿਪਟ ਚਲਾਓ

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```


### **OpenVINO ਨਾਲ Phi-3.5-Vision ਦੀ Quantizing**

ਕਿਰਪਾ ਕਰਕੇ ਇਹ ਸਕ੍ਰਿਪਟ Python ਜਾਂ Jupyter lab ਵਿੱਚ ਚਲਾਓ

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


### **🤖 Intel OpenVINO ਨਾਲ Phi-3.5 ਲਈ ਨਮੂਨੇ**

| ਲੈਬਸ    | ਜਾਣੂ ਕਰਵਾਉਣਾ | ਜਾਓ |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | ਆਪਣੇ AI PC ਵਿੱਚ Phi-3.5 Instruct ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਸਿੱਖੋ    |  [ਜਾਓ](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (ਚਿੱਤਰ) | ਆਪਣੇ AI PC ਵਿੱਚ ਚਿੱਤਰ ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ Phi-3.5 Vision ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਸਿੱਖੋ      |  [ਜਾਓ](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (ਵੀਡੀਓ)   | ਆਪਣੇ AI PC ਵਿੱਚ ਵੀਡੀਓ ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ Phi-3.5 Vision ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਸਿੱਖੋ    |  [ਜਾਓ](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |



## **ਸੰਸਾਧਨ**

1. Intel OpenVINO ਬਾਰੇ ਹੋਰ ਜਾਣੋ [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub ਰਿਪੋ [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।