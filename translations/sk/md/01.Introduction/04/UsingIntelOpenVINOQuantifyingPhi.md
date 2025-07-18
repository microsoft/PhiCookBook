<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-07-16T22:04:00+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "sk"
}
-->
# **Kvantizácia Phi-3.5 pomocou Intel OpenVINO**

Intel je najtradičnejší výrobca CPU s množstvom používateľov. S nástupom strojového učenia a hlbokého učenia sa Intel tiež zapojil do súťaže o zrýchlenie AI. Pre inferenciu modelov Intel využíva nielen GPU a CPU, ale aj NPU.

Dúfame, že nasadíme rodinu Phi-3.x na koncovej strane, s cieľom stať sa najdôležitejšou súčasťou AI PC a Copilot PC. Načítanie modelu na koncovej strane závisí od spolupráce rôznych výrobcov hardvéru. Táto kapitola sa zameriava hlavne na aplikačný scenár Intel OpenVINO ako kvantitatívneho modelu.

## **Čo je OpenVINO**

OpenVINO je open-source nástrojový balík na optimalizáciu a nasadenie modelov hlbokého učenia od cloudu po edge. Umožňuje zrýchlenie inferencie hlbokého učenia v rôznych prípadoch použitia, ako sú generatívna AI, video, audio a jazyk, s modelmi z populárnych frameworkov ako PyTorch, TensorFlow, ONNX a ďalších. Konvertujte a optimalizujte modely a nasadzujte ich na rôzne Intel® hardvérové platformy a prostredia, či už lokálne, na zariadení, v prehliadači alebo v cloude.

S OpenVINO teraz môžete rýchlo kvantizovať GenAI model na Intel hardvéri a zrýchliť referenciu modelu.

OpenVINO teraz podporuje konverziu kvantizácie Phi-3.5-Vision a Phi-3.5 Instruct.

### **Nastavenie prostredia**

Uistite sa, že máte nainštalované nasledujúce závislosti prostredia, toto je requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kvantizácia Phi-3.5-Instruct pomocou OpenVINO**

V termináli spustite tento skript

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kvantizácia Phi-3.5-Vision pomocou OpenVINO**

Skript spustite v Pythone alebo Jupyter lab

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

### **🤖 Ukážky pre Phi-3.5 s Intel OpenVINO**

| Laboratóriá    | Popis | Spustiť |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Naučte sa, ako používať Phi-3.5 Instruct vo vašom AI PC    |  [Spustiť](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (obrázok) | Naučte sa, ako používať Phi-3.5 Vision na analýzu obrázkov vo vašom AI PC      |  [Spustiť](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | Naučte sa, ako používať Phi-3.5 Vision na analýzu videa vo vašom AI PC    |  [Spustiť](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Zdroje**

1. Viac o Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.