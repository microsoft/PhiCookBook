<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-10-11T12:27:29+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "ta"
}
-->
# **Phi-3.5 ஐ Intel OpenVINO பயன்படுத்தி அளவீடு செய்வது**

Intel என்பது மிகவும் பாரம்பரியமான CPU உற்பத்தியாளர், பல பயனர்களைக் கொண்டுள்ளது. இயந்திரக் கற்றல் மற்றும் ஆழமான கற்றல் வளர்ச்சியுடன், Intel AI வேகப்படுத்தலில் போட்டியில் இணைந்துள்ளது. மாடல் முடிவெடுப்புக்காக, Intel GPUக்கள் மற்றும் CPUக்களை மட்டுமல்லாமல், NPUக்களையும் பயன்படுத்துகிறது.

Phi-3.x குடும்பத்தை முடிவில் பயன்படுத்த deploy செய்ய நாங்கள் நம்புகிறோம், இது AI PC மற்றும் Copilot PC-யின் மிக முக்கியமான பகுதியாக மாற வேண்டும். முடிவில் மாடலை ஏற்றுவது வெவ்வேறு ஹார்ட்வேர உற்பத்தியாளர்களின் ஒத்துழைப்பை சார்ந்துள்ளது. இந்த அத்தியாயம் Intel OpenVINO-வை ஒரு அளவீட்டு மாடலாக பயன்படுத்தும் பயன்பாட்டு சூழலுக்கு முக்கியமாக கவனம் செலுத்துகிறது.

## **OpenVINO என்றால் என்ன**

OpenVINO என்பது மேகத்திலிருந்து விளிம்புக்கு ஆழமான கற்றல் மாடல்களை மேம்படுத்தவும், deploy செய்யவும் உதவும் ஓர் திறந்த மூல கருவி தொகுப்பு. இது PyTorch, TensorFlow, ONNX போன்ற பிரபலமான frameworks-களின் மாடல்களுடன் உருவாக்கும் AI, வீடியோ, ஆடியோ மற்றும் மொழி போன்ற பல பயன்பாடுகளில் ஆழமான கற்றல் முடிவெடுப்பை வேகப்படுத்துகிறது. மாடல்களை மாற்றவும், மேம்படுத்தவும், Intel® ஹார்ட்வேர்களும் சூழல்களும் கலந்த deploy செய்யவும், on-premises மற்றும் on-device, browser அல்லது cloud-ல் பயன்படுத்தவும் உதவுகிறது.

இப்போது OpenVINO-வுடன், Intel ஹார்ட்வேரில் GenAI மாடலை விரைவாக அளவீடு செய்யவும், மாடல் குறிப்பு (reference) வேகப்படுத்தவும் முடியும்.

OpenVINO தற்போது Phi-3.5-Vision மற்றும் Phi-3.5 Instruct-இன் அளவீட்டு மாற்றத்தை ஆதரிக்கிறது.

### **சூழல் அமைப்பு**

தயவுசெய்து கீழே உள்ள சூழல் சார்ந்த தேவைகள் நிறுவப்பட்டுள்ளதா என்பதை உறுதிப்படுத்தவும், இது requirement.txt 

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **OpenVINO-வை பயன்படுத்தி Phi-3.5-Instruct-ஐ அளவீடு செய்வது**

Terminal-ல், இந்த script-ஐ இயக்கவும்

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **OpenVINO-வை பயன்படுத்தி Phi-3.5-Vision-ஐ அளவீடு செய்வது**

Python அல்லது Jupyter lab-ல் இந்த script-ஐ இயக்கவும்

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

### **🤖 Intel OpenVINO உடன் Phi-3.5-க்கு மாதிரிகள்**

| Labs    | அறிமுகம் | செல்லவும் |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | உங்கள் AI PC-யில் Phi-3.5 Instruct-ஐ எப்படி பயன்படுத்துவது என்பதை கற்றுக்கொள்ளவும்    |  [செல்லவும்](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | உங்கள் AI PC-யில் Phi-3.5 Vision-ஐ பயன்படுத்தி படத்தை எப்படி பகுப்பாய்வு செய்வது என்பதை கற்றுக்கொள்ளவும்      |  [செல்லவும்](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | உங்கள் AI PC-யில் Phi-3.5 Vision-ஐ பயன்படுத்தி வீடியோவை எப்படி பகுப்பாய்வு செய்வது என்பதை கற்றுக்கொள்ளவும்    |  [செல்லவும்](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |



## **வளங்கள்**

1. Intel OpenVINO பற்றி மேலும் அறிக [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.