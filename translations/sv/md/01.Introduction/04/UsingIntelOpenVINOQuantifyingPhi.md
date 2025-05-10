<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-05-09T13:56:56+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "sv"
}
-->
# **Kvantifiering av Phi-3.5 med Intel OpenVINO**

Intel är den mest traditionella CPU-tillverkaren med många användare. Med framväxten av maskininlärning och djupinlärning har Intel också gått med i tävlingen om AI-acceleration. För modellinferens använder Intel inte bara GPU:er och CPU:er, utan även NPU:er.

Vi hoppas kunna distribuera Phi-3.x-familjen på ändenheten och bli den viktigaste delen av AI-PC och Copilot-PC. Modellens laddning på ändenheten beror på samarbetet mellan olika hårdvarutillverkare. Detta kapitel fokuserar främst på tillämpningsscenariot för Intel OpenVINO som en kvantitativ modell.

## **Vad är OpenVINO**

OpenVINO är ett open source-verktyg för att optimera och distribuera djupinlärningsmodeller från molnet till kanten. Det påskyndar djupinlärningsinferens över olika användningsområden, som generativ AI, video, ljud och språk med modeller från populära ramverk som PyTorch, TensorFlow, ONNX och fler. Konvertera och optimera modeller och distribuera över en blandning av Intel®-hårdvara och miljöer, lokalt och på enheten, i webbläsaren eller i molnet.

Med OpenVINO kan du snabbt kvantifiera GenAI-modellen i Intel-hårdvara och accelerera modellreferensen.

Nu stödjer OpenVINO kvantifieringskonvertering av Phi-3.5-Vision och Phi-3.5 Instruct.

### **Miljöinställning**

Se till att följande miljöberoenden är installerade, detta är requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kvantifiering av Phi-3.5-Instruct med OpenVINO**

Kör detta skript i Terminal

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kvantifiering av Phi-3.5-Vision med OpenVINO**

Kör detta skript i Python eller Jupyter lab

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

### **🤖 Exempel för Phi-3.5 med Intel OpenVINO**

| Labs    | Introduktion | Gå till |
| -------- | ----------- | ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Lär dig hur du använder Phi-3.5 Instruct i din AI-PC    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (bild) | Lär dig hur du använder Phi-3.5 Vision för att analysera bilder i din AI-PC      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | Lär dig hur du använder Phi-3.5 Vision för att analysera video i din AI-PC    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Resurser**

1. Läs mer om Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.