# **Kvantizacija Phi-3.5 pomoću Intel OpenVINO**

Intel je najtradicionalniji proizvođač CPU-a s velikim brojem korisnika. S razvojem strojnog učenja i dubokog učenja, Intel se također uključio u natjecanje za AI akceleraciju. Za izvođenje modela, Intel ne koristi samo GPU i CPU, već i NPU.

Nadamo se da ćemo obitelj Phi-3.x implementirati na krajnjoj strani, s ciljem da postane najvažniji dio AI PC-a i Copilot PC-a. Učitavanje modela na krajnjoj strani ovisi o suradnji različitih proizvođača hardvera. Ovo poglavlje uglavnom se fokusira na primjenu Intel OpenVINO kao kvantitativnog modela.

## **Što je OpenVINO**

OpenVINO je open-source alatni paket za optimizaciju i implementaciju modela dubokog učenja od oblaka do edge uređaja. Ubrzava izvođenje dubokog učenja u različitim scenarijima, poput generativne AI, videozapisa, zvuka i jezika, koristeći modele iz popularnih okvira kao što su PyTorch, TensorFlow, ONNX i drugi. Pretvarajte i optimizirajte modele te ih implementirajte na kombinaciji Intel® hardvera i okruženja, lokalno ili na uređaju, u pregledniku ili u oblaku.

Sada, uz OpenVINO, možete brzo kvantizirati GenAI model na Intel hardveru i ubrzati referentni model.

OpenVINO sada podržava kvantizaciju Phi-3.5-Vision i Phi-3.5 Instruct.

### **Postavljanje okruženja**

Molimo provjerite jesu li instalirane sljedeće ovisnosti okruženja, ovo je requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kvantizacija Phi-3.5-Instruct pomoću OpenVINO**

U Terminalu pokrenite ovaj skript

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kvantizacija Phi-3.5-Vision pomoću OpenVINO**

Pokrenite ovaj skript u Pythonu ili Jupyter labu

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

### **🤖 Primjeri za Phi-3.5 s Intel OpenVINO**

| Laboratoriji    | Opis | Idi |
| -------- | ------- |  ------- |
| 🚀 Lab-Uvod u Phi-3.5 Instruct  | Naučite kako koristiti Phi-3.5 Instruct na vašem AI PC-u    |  [Idi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Uvod u Phi-3.5 Vision (slika) | Naučite kako koristiti Phi-3.5 Vision za analizu slika na vašem AI PC-u      |  [Idi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Uvod u Phi-3.5 Vision (video)   | Naučite kako koristiti Phi-3.5 Vision za analizu videozapisa na vašem AI PC-u    |  [Idi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Resursi**

1. Saznajte više o Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub repozitorij [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.