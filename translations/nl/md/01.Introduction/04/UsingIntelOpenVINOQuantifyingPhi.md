<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-05-09T13:58:35+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "nl"
}
-->
# **Quantizen van Phi-3.5 met Intel OpenVINO**

Intel is de meest traditionele CPU-fabrikant met veel gebruikers. Met de opkomst van machine learning en deep learning is Intel ook de strijd aangegaan om AI-versnelling. Voor modelinference gebruikt Intel niet alleen GPU's en CPU's, maar ook NPU's.

We hopen de Phi-3.x-familie aan de rand te kunnen inzetten, met de ambitie om het belangrijkste onderdeel te worden van AI-pc's en Copilot-pc's. Het laden van het model aan de rand hangt af van de samenwerking tussen verschillende hardwarefabrikanten. Dit hoofdstuk richt zich vooral op de toepassing van Intel OpenVINO als kwantitatief model.

## **Wat is OpenVINO**

OpenVINO is een open-source toolkit voor het optimaliseren en inzetten van deep learning modellen van cloud tot edge. Het versnelt deep learning inference in verschillende toepassingen, zoals generatieve AI, video, audio en taal, met modellen uit populaire frameworks zoals PyTorch, TensorFlow, ONNX en meer. Converteer en optimaliseer modellen en zet ze in op een mix van Intel® hardware en omgevingen, zowel on-premises als op het apparaat, in de browser of in de cloud.

Met OpenVINO kun je nu snel GenAI-modellen kwantiseren op Intel-hardware en de modelreferentie versnellen.

OpenVINO ondersteunt nu de kwantisatieconversie van Phi-3.5-Vision en Phi-3.5 Instruct.

### **Omgevingsinstelling**

Zorg ervoor dat de volgende omgevingsafhankelijkheden zijn geïnstalleerd, dit is requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Quantizen van Phi-3.5-Instruct met OpenVINO**

Voer dit script uit in de terminal

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Quantizen van Phi-3.5-Vision met OpenVINO**

Voer dit script uit in Python of Jupyter lab

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

### **🤖 Voorbeelden voor Phi-3.5 met Intel OpenVINO**

| Labs    | Introductie | Ga naar |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Leer hoe je Phi-3.5 Instruct gebruikt op je AI-pc    |  [Ga](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (afbeelding) | Leer hoe je Phi-3.5 Vision gebruikt om afbeeldingen te analyseren op je AI-pc      |  [Ga](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | Leer hoe je Phi-3.5 Vision gebruikt om video te analyseren op je AI-pc    |  [Ga](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Bronnen**

1. Lees meer over Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal dient als de gezaghebbende bron te worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.