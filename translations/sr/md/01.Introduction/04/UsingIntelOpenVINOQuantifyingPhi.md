<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-05-09T14:04:05+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "sr"
}
-->
# **Kvantizacija Phi-3.5 koristeći Intel OpenVINO**

Intel je najtradicionalniji proizvođač CPU-a sa mnogo korisnika. Sa porastom mašinskog učenja i dubokog učenja, Intel se takođe uključio u trku za ubrzanje AI. Za izvođenje modela, Intel ne koristi samo GPU i CPU, već i NPU.

Nadamo se da ćemo implementirati Phi-3.x porodicu na krajnjoj strani, sa ciljem da postane najvažniji deo AI PC i Copilot PC. Učitavanje modela na krajnjoj strani zavisi od saradnje različitih proizvođača hardvera. Ovo poglavlje se uglavnom fokusira na primenu Intel OpenVINO kao kvantizovanog modela.

## **Šta je OpenVINO**

OpenVINO je open-source alat za optimizaciju i implementaciju modela dubokog učenja od clouda do edge uređaja. Ubrzava izvođenje dubokog učenja u različitim slučajevima upotrebe, kao što su generativni AI, video, audio i jezik, sa modelima iz popularnih okvira kao što su PyTorch, TensorFlow, ONNX i drugi. Konvertuje i optimizuje modele, i implementira ih na različitim Intel® hardverskim platformama i okruženjima, lokalno ili na uređaju, u pregledaču ili u cloudu.

Sada, sa OpenVINO, možete brzo kvantizovati GenAI modele na Intel hardveru i ubrzati referentni model.

Trenutno OpenVINO podržava kvantizacionu konverziju Phi-3.5-Vision i Phi-3.5 Instruct.

### **Podešavanje okruženja**

Molimo vas da osigurate da su sledeće zavisnosti okruženja instalirane, ovo je requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kvantizacija Phi-3.5-Instruct koristeći OpenVINO**

U Terminalu pokrenite sledeći skript

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kvantizacija Phi-3.5-Vision koristeći OpenVINO**

Pokrenite sledeći skript u Python-u ili Jupyter lab-u

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

### **🤖 Primeri za Phi-3.5 sa Intel OpenVINO**

| Laboratorije    | Uvod | Kreni |
| -------- | ------- |  ------- |
| 🚀 Lab-Uvod Phi-3.5 Instruct  | Naučite kako da koristite Phi-3.5 Instruct na vašem AI PC-u    |  [Kreni](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Uvod Phi-3.5 Vision (slika) | Naučite kako da koristite Phi-3.5 Vision za analizu slike na vašem AI PC-u      |  [Kreni](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Uvod Phi-3.5 Vision (video)   | Naučite kako da koristite Phi-3.5 Vision za analizu slike na vašem AI PC-u    |  [Kreni](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Resursi**

1. Saznajte više o Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub repozitorijum [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Ограничење одговорности**:  
Овај документ је преведен коришћењем АИ сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде прецизан, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на оригиналном језику треба сматрати ауторитетом. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешне интерпретације настале коришћењем овог превода.