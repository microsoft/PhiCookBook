# **Phi-3.5 kvantiseerimine Intel OpenVINO abil**

Intel on traditsiooniline CPU tootja, millel on palju kasutajaid. Masinõppe ja süvaõppe populaarsuse kasvuga on Intel samuti liitunud AI kiirenduse võistlusega. Mudelite järelduste tegemiseks kasutab Intel mitte ainult GPU-sid ja CPU-sid, vaid ka NPU-sid.

Me soovime juurutada Phi-3.x perekonda lõppkasutaja seadmetes, lootes saada AI PC ja Copilot PC kõige olulisemaks osaks. Mudeli laadimine lõppkasutaja seadmetes sõltub erinevate riistvaratootjate koostööst. See peatükk keskendub peamiselt Intel OpenVINO rakendusskeemile kvantitatiivse mudelina.

## **Mis on OpenVINO**

OpenVINO on avatud lähtekoodiga tööriistakomplekt, mis on mõeldud süvaõppe mudelite optimeerimiseks ja juurutamiseks pilvest serva. See kiirendab süvaõppe järeldusi erinevates kasutusvaldkondades, nagu generatiivne AI, video, audio ja keel, kasutades populaarsete raamistikude, nagu PyTorch, TensorFlow, ONNX ja teiste, mudeleid. Konverteeri ja optimeeri mudeleid ning juuruta neid erinevatel Intel® riistvaradel ja keskkondades, olgu see kohapeal, seadmes, brauseris või pilves.

OpenVINO abil saate nüüd kiiresti kvantiseerida GenAI mudeli Intel riistvaral ja kiirendada mudeli järeldusi.

OpenVINO toetab nüüd Phi-3.5-Vision ja Phi-3.5 Instruct kvantiseerimise konversiooni.

### **Keskkonna seadistamine**

Palun veenduge, et järgmised keskkonna sõltuvused on paigaldatud, see on requirement.txt 

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Phi-3.5-Instruct kvantiseerimine OpenVINO abil**

Terminalis käivitage palun järgmine skript

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Phi-3.5-Vision kvantiseerimine OpenVINO abil**

Käivitage palun see skript Pythonis või Jupyter labis

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

### **🤖 Näidised Phi-3.5 jaoks Intel OpenVINO abil**

| Laborid    | Tutvustus | Mine |
| -------- | ------- |  ------- |
| 🚀 Lab-Tutvustus Phi-3.5 Instruct  | Õpi, kuidas kasutada Phi-3.5 Instruct oma AI PC-s    |  [Mine](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Tutvustus Phi-3.5 Vision (pilt) | Õpi, kuidas kasutada Phi-3.5 Visioni piltide analüüsimiseks oma AI PC-s      |  [Mine](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Tutvustus Phi-3.5 Vision (video)   | Õpi, kuidas kasutada Phi-3.5 Visioni videote analüüsimiseks oma AI PC-s    |  [Mine](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |


## **Ressursid**

1. Lisateave Intel OpenVINO kohta [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.