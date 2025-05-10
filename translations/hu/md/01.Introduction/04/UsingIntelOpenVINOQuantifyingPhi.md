<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-05-09T14:01:39+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "hu"
}
-->
# **Phi-3.5 kvantálása Intel OpenVINO használatával**

Az Intel a legismertebb CPU gyártó, sok felhasználóval. A gépi tanulás és a mélytanulás térnyerésével az Intel is bekapcsolódott az AI gyorsítás versenyébe. A modell inferencia során az Intel nem csak GPU-kat és CPU-kat használ, hanem NPU-kat is.

Célunk, hogy a Phi-3.x családot az élő oldalon telepítsük, és ezáltal az AI PC és Copilot PC legfontosabb részévé váljunk. A modell betöltése az élő oldalon különböző hardvergyártók együttműködésétől függ. Ez a fejezet elsősorban az Intel OpenVINO kvantált modell alkalmazási esetére fókuszál.

## **Mi az OpenVINO**

Az OpenVINO egy nyílt forráskódú eszközkészlet, amely a mélytanulási modellek optimalizálását és telepítését teszi lehetővé a felhőtől az élő eszközökig. Gyorsítja a mélytanulási inferenciát különböző felhasználási területeken, mint például generatív AI, videó, hang és nyelv, népszerű keretrendszerekből származó modellekkel, mint a PyTorch, TensorFlow, ONNX és mások. Lehetővé teszi a modellek átalakítását és optimalizálását, valamint telepítését Intel® hardvereken és különböző környezetekben, helyben vagy eszközön, böngészőben vagy felhőben.

Most az OpenVINO segítségével gyorsan kvantálhatod a GenAI modellt Intel hardveren, és felgyorsíthatod a modell referenciát.

Jelenleg az OpenVINO támogatja a Phi-3.5-Vision és Phi-3.5 Instruct kvantálási átalakítását.

### **Környezeti beállítás**

Kérjük, győződj meg róla, hogy az alábbi környezeti függőségek telepítve vannak, ez a requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Phi-3.5-Instruct kvantálása OpenVINO-val**

Terminálban futtasd ezt a szkriptet

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Phi-3.5-Vision kvantálása OpenVINO-val**

Futtasd ezt a szkriptet Pythonban vagy Jupyter labban

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

### **🤖 Phi-3.5 minták Intel OpenVINO-val**

| Laborok | Bemutatás | Indítás |
| -------- | ------- | ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Tanuld meg, hogyan használd a Phi-3.5 Instructot az AI PC-den    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (kép) | Tanuld meg, hogyan elemezheted a képeket Phi-3.5 Vision segítségével az AI PC-den      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (videó)   | Tanuld meg, hogyan elemezheted a videókat Phi-3.5 Vision segítségével az AI PC-den    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |


## **Források**

1. Tudj meg többet az Intel OpenVINO-ról [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Jogi nyilatkozat**:  
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt szakmai, emberi fordítást igénybe venni. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.