<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-07-16T22:01:16+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "it"
}
-->
# **Quantizzazione di Phi-3.5 con Intel OpenVINO**

Intel è il produttore di CPU più tradizionale con molti utenti. Con l’ascesa del machine learning e del deep learning, Intel si è unita alla competizione per l’accelerazione dell’AI. Per l’inferenza dei modelli, Intel non utilizza solo GPU e CPU, ma anche NPU.

Speriamo di distribuire la famiglia Phi-3.x sul lato end, con l’obiettivo di diventare la parte più importante del PC AI e del PC Copilot. Il caricamento del modello sul lato end dipende dalla collaborazione di diversi produttori di hardware. Questo capitolo si concentra principalmente sullo scenario applicativo di Intel OpenVINO come modello quantificato.

## **Cos’è OpenVINO**

OpenVINO è un toolkit open-source per ottimizzare e distribuire modelli di deep learning dal cloud al edge. Accelera l’inferenza del deep learning in diversi casi d’uso, come AI generativa, video, audio e linguaggio, con modelli provenienti da framework popolari come PyTorch, TensorFlow, ONNX e altri. Consente di convertire e ottimizzare i modelli, distribuendoli su una combinazione di hardware e ambienti Intel®, on-premises e on-device, nel browser o nel cloud.

Ora con OpenVINO puoi quantizzare rapidamente il modello GenAI su hardware Intel e accelerare il modello di riferimento.

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

### **Quantizzazione di Phi-3.5-Instruct con OpenVINO**

Nel Terminale, esegui questo script

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Quantizzazione di Phi-3.5-Vision con OpenVINO**

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
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Impara come usare Phi-3.5 Instruct nel tuo PC AI    |  [Vai](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (immagine) | Impara come usare Phi-3.5 Vision per analizzare immagini nel tuo PC AI      |  [Vai](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | Impara come usare Phi-3.5 Vision per analizzare video nel tuo PC AI    |  [Vai](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Risorse**

1. Scopri di più su Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Repository GitHub di Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.