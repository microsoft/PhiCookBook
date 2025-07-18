<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-07-16T22:04:46+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "sl"
}
-->
# **Kvantilizacija Phi-3.5 z uporabo Intel OpenVINO**

Intel je najbolj tradicionalni proizvajalec CPU-jev z veliko uporabniki. Z razmahom strojnega učenja in globokega učenja se je Intel pridružil tudi tekmi za pospeševanje AI. Za inferenco modelov Intel ne uporablja le GPU-jev in CPU-jev, ampak tudi NPU-je.

Upamo, da bomo družino Phi-3.x lahko namestili na končni strani, saj želimo postati najpomembnejši del AI računalnika in Copilot računalnika. Nalaganje modela na končni strani je odvisno od sodelovanja različnih proizvajalcev strojne opreme. To poglavje se osredotoča predvsem na uporabo Intel OpenVINO kot kvantitativnega modela.

## **Kaj je OpenVINO**

OpenVINO je odprtokodni komplet orodij za optimizacijo in nameščanje modelov globokega učenja od oblaka do roba. Pospešuje inferenco globokega učenja v različnih primerih uporabe, kot so generativna AI, video, zvok in jezik, z modeli iz priljubljenih ogrodij, kot so PyTorch, TensorFlow, ONNX in drugi. Pretvarja in optimizira modele ter jih namešča na kombinacijo Intel® strojne opreme in okolij, lokalno ali na napravi, v brskalniku ali v oblaku.

Zdaj lahko z OpenVINO hitro kvantizirate GenAI model na Intel strojni opremi in pospešite referenco modela.

OpenVINO zdaj podpira kvantizacijsko pretvorbo Phi-3.5-Vision in Phi-3.5 Instruct.

### **Nastavitev okolja**

Poskrbite, da so nameščene naslednje odvisnosti okolja, to je requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kvantilizacija Phi-3.5-Instruct z OpenVINO**

V terminalu zaženite ta skript

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kvantilizacija Phi-3.5-Vision z OpenVINO**

Zaženite ta skript v Pythonu ali Jupyter labu

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

### **🤖 Primeri za Phi-3.5 z Intel OpenVINO**

| Laboratoriji    | Predstavitev | Pojdi |
| -------- | ------- |  ------- |
| 🚀 Lab-Predstavitev Phi-3.5 Instruct  | Naučite se, kako uporabljati Phi-3.5 Instruct v vašem AI računalniku    |  [Pojdi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Predstavitev Phi-3.5 Vision (slika) | Naučite se, kako uporabiti Phi-3.5 Vision za analizo slike v vašem AI računalniku      |  [Pojdi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Predstavitev Phi-3.5 Vision (video)   | Naučite se, kako uporabiti Phi-3.5 Vision za analizo slike v vašem AI računalniku    |  [Pojdi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Viri**

1. Več o Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub repozitorij [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.