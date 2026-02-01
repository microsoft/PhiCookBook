# **Phi-3.5 kvantavimas naudojant Intel OpenVINO**

Intel yra vienas tradiciškiausių procesorių gamintojų, turintis daugybę vartotojų. Su mašininio mokymosi ir giluminio mokymosi augimu, Intel taip pat prisijungė prie AI spartinimo konkurencijos. Modelių įžvalgoms Intel naudoja ne tik GPU ir CPU, bet ir NPU.

Tikimės, kad Phi-3.x šeima bus diegiama galutiniame įrenginyje, siekiant tapti svarbiausia AI PC ir Copilot PC dalimi. Modelio įkrovimas galutiniame įrenginyje priklauso nuo skirtingų aparatūros gamintojų bendradarbiavimo. Šis skyrius daugiausia dėmesio skiria Intel OpenVINO taikymo scenarijui kaip kvantinio modelio.

## **Kas yra OpenVINO**

OpenVINO yra atvirojo kodo įrankių rinkinys, skirtas giluminio mokymosi modelių optimizavimui ir diegimui nuo debesies iki krašto. Jis spartina giluminio mokymosi įžvalgas įvairiuose naudojimo atvejuose, tokiuose kaip generatyvinis AI, vaizdo įrašai, garsas ir kalba, naudojant modelius iš populiarių sistemų, tokių kaip PyTorch, TensorFlow, ONNX ir kt. Konvertuokite ir optimizuokite modelius bei diekite juos įvairioje Intel® aparatūroje ir aplinkose, vietoje arba įrenginyje, naršyklėje ar debesyje.

Dabar su OpenVINO galite greitai kvantuoti GenAI modelį Intel aparatūroje ir paspartinti modelio įžvalgas.

Šiuo metu OpenVINO palaiko Phi-3.5-Vision ir Phi-3.5 Instruct kvantavimo konversiją.

### **Aplinkos paruošimas**

Įsitikinkite, kad įdiegėte šias aplinkos priklausomybes, tai yra requirement.txt 

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Phi-3.5-Instruct kvantavimas naudojant OpenVINO**

Terminale paleiskite šį skriptą

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Phi-3.5-Vision kvantavimas naudojant OpenVINO**

Paleiskite šį skriptą Python arba Jupyter lab aplinkoje

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

### **🤖 Pavyzdžiai Phi-3.5 su Intel OpenVINO**

| Laboratorijos    | Aprašymas | Eiti |
| -------- | ------- |  ------- |
| 🚀 Laboratorija - Phi-3.5 Instruct pristatymas  | Sužinokite, kaip naudoti Phi-3.5 Instruct savo AI PC    |  [Eiti](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Laboratorija - Phi-3.5 Vision (vaizdas) | Sužinokite, kaip naudoti Phi-3.5 Vision analizuoti vaizdą savo AI PC      |  [Eiti](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Laboratorija - Phi-3.5 Vision (vaizdo įrašas)   | Sužinokite, kaip naudoti Phi-3.5 Vision analizuoti vaizdą savo AI PC    |  [Eiti](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Ištekliai**

1. Sužinokite daugiau apie Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub saugykla [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.