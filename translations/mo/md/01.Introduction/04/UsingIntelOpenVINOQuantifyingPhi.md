<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f766ec7e68d97f6009b58794b471d66",
  "translation_date": "2025-04-04T12:13:37+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "mo"
}
-->
# **Quantizing Phi-3.5 using Intel OpenVINO**

Intel është një nga prodhuesit më tradicionalë të CPU-ve me shumë përdorues. Me rritjen e mësimit të makinerive dhe të thellë, Intel ka hyrë gjithashtu në garën për përshpejtimin e AI-së. Për inferencën e modeleve, Intel jo vetëm që përdor GPU dhe CPU, por edhe NPU.

Ne shpresojmë të shpërndajmë Familjen Phi-3.x në pajisjet fundore, duke synuar të bëhet pjesa më e rëndësishme e PC-ve AI dhe PC-ve Copilot. Ngarkimi i modelit në pajisjet fundore varet nga bashkëpunimi i prodhuesve të ndryshëm të harduerit. Ky kapitull fokusohet kryesisht në skenarin e aplikimit të Intel OpenVINO si model i kuantifikuar.

## **Çfarë është OpenVINO**

OpenVINO është një mjet me burim të hapur për optimizimin dhe shpërndarjen e modeleve të mësimit të thellë nga cloud-i te pajisjet fundore. Ai përshpejton inferencën e mësimit të thellë në përdorime të ndryshme, si AI gjenerues, video, audio dhe gjuhë me modele nga kornizat e njohura si PyTorch, TensorFlow, ONNX dhe më shumë. Konvertoni dhe optimizoni modele, dhe shpërndajini në një kombinim të harduerëve dhe mjediseve Intel®, në premisa dhe në pajisje, në shfletues ose në cloud.

Tani me OpenVINO, ju mund të kuantifikoni shpejt modelin GenAI në harduerin Intel dhe të përshpejtoni referencën e modelit.

Tani OpenVINO mbështet konvertimin e kuantifikimit të Phi-3.5-Vision dhe Phi-3.5 Instruct.

### **Konfigurimi i Mjedisit**

Ju lutemi sigurohuni që varësitë e mjedisit të mëposhtëm të jenë instaluar, kjo është requirement.txt 

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kuantifikimi i Phi-3.5-Instruct duke përdorur OpenVINO**

Në Terminal, ju lutemi ekzekutoni këtë skript

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kuantifikimi i Phi-3.5-Vision duke përdorur OpenVINO**

Ju lutemi ekzekutoni këtë skript në Python ose Jupyter lab

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

### **🤖 Shembuj për Phi-3.5 me Intel OpenVINO**

| Laboratorë    | Prezantim | Shko |
| -------- | ------- |  ------- |
| 🚀 Laborator-Prezanto Phi-3.5 Instruct  | Mësoni si të përdorni Phi-3.5 Instruct në PC-në tuaj AI    |  [Shko](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Laborator-Prezanto Phi-3.5 Vision (imazh) | Mësoni si të përdorni Phi-3.5 Vision për të analizuar imazhe në PC-në tuaj AI      |  [Shko](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Laborator-Prezanto Phi-3.5 Vision (video)   | Mësoni si të përdorni Phi-3.5 Vision për të analizuar video në PC-në tuaj AI    |  [Shko](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Burime**

1. Mësoni më shumë rreth Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Repo-ja GitHub e Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

It seems like you want the text translated into "mo," but could you clarify what "mo" refers to? Are you asking for a translation into a specific language, such as Maori, Mongolian, or another language? Let me know so I can assist you accurately!