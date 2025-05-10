<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-05-09T13:54:54+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "it"
}
-->
# **Quantizzare Phi-3.5 usando Intel OpenVINO**

Intel è il produttore di CPU più tradizionale con molti utenti. Con l’ascesa del machine learning e del deep learning, Intel ha anche iniziato a competere nell’accelerazione AI. Per l’inferenza dei modelli, Intel non utilizza solo GPU e CPU, ma anche NPU.

Vogliamo distribuire la famiglia Phi-3.x sul lato end, con l’obiettivo di diventare la parte più importante degli AI PC e Copilot PC. Il caricamento del modello sul lato end dipende dalla collaborazione di diversi produttori hardware. Questo capitolo si concentra principalmente sullo scenario applicativo di Intel OpenVINO come modello quantizzato.

## **Cos’è OpenVINO**

OpenVINO è un toolkit open-source per ottimizzare e distribuire modelli di deep learning dal cloud all’edge. Accelera l’inferenza deep learning in diversi casi d’uso, come AI generativa, video, audio e linguaggio, con modelli provenienti da framework popolari come PyTorch, TensorFlow, ONNX e altri. Consente di convertire e ottimizzare modelli, e di distribuirli su una combinazione di hardware e ambienti Intel®, on-premises e on-device, nel browser o nel cloud.

Con OpenVINO puoi ora quantizzare rapidamente modelli GenAI su hardware Intel e accelerare i modelli di riferimento.

OpenVINO supporta ora la conversione di quantizzazione di Phi-3.5-Vision e Phi-3.5 Instruct.

### **Configurazione dell’ambiente**

Assicurati che le seguenti dipendenze ambientali siano installate, questo è requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Quantizzare Phi-3.5-Instruct usando OpenVINO**

Nel Terminale, esegui questo script

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Quantizzare Phi-3.5-Vision usando OpenVINO**

Esegui questo script in Python o Jupyter lab

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

### **🤖 Esempi per Phi-3.5 con Intel OpenVINO**

| Labs    | Introduzione | Vai |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Scopri come usare Phi-3.5 Instruct nel tuo AI PC    |  [Vai](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (immagine) | Scopri come usare Phi-3.5 Vision per analizzare immagini nel tuo AI PC      |  [Vai](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | Scopri come usare Phi-3.5 Vision per analizzare video nel tuo AI PC    |  [Vai](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |


## **Risorse**

1. Per saperne di più su Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale effettuata da un essere umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.