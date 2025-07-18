<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-07-16T22:04:28+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "sr"
}
-->
# **Квантизација Phi-3.5 помоћу Intel OpenVINO**

Intel је најтрадиционалнији произвођач процесора са великим бројем корисника. Са порастом машинског учења и дубоког учења, Intel се такође укључио у трку за убрзање вештачке интелигенције. За извршавање модела, Intel не користи само GPU и CPU, већ и NPU.

Надамо се да ћемо распоредити Phi-3.x породицу на крајњој страни, са жељом да постане најважнији део AI рачунара и Copilot рачунара. Учитавање модела на крајњој страни зависи од сарадње различитих произвођача хардвера. Ово поглавље се углавном фокусира на примену Intel OpenVINO као квантитативног модела.

## **Шта је OpenVINO**

OpenVINO је алат отвореног кода за оптимизацију и распоређивање модела дубоког учења од облака до ивице мреже. Убрзава извршавање дубоког учења у различитим случајевима употребе, као што су генеративна AI, видео, аудио и језик, са моделима из популарних оквира као што су PyTorch, TensorFlow, ONNX и други. Конвертујте и оптимизујте моделе и распоредите их на различитим Intel® хардверима и окружењима, локално или на уређају, у прегледачу или у облаку.

Сада, уз OpenVINO, можете брзо квантизовати GenAI модел на Intel хардверу и убрзати референцу модела.

OpenVINO сада подржава конверзију квантизације за Phi-3.5-Vision и Phi-3.5 Instruct.

### **Подешавање окружења**

Молимо вас да обезбедите да су следеће зависности окружења инсталиране, ово је requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Квантизација Phi-3.5-Instruct помоћу OpenVINO**

У терминалу покрените овај скрипт

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Квантизација Phi-3.5-Vision помоћу OpenVINO**

Покрените овај скрипт у Python-у или Jupyter lab-у

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

### **🤖 Примери за Phi-3.5 са Intel OpenVINO**

| Лабораторије    | Увод | Иди |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Научите како да користите Phi-3.5 Instruct на вашем AI рачунару    |  [Иди](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (слика) | Научите како да користите Phi-3.5 Vision за анализу слика на вашем AI рачунару      |  [Иди](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (видео)   | Научите како да користите Phi-3.5 Vision за анализу видео записа на вашем AI рачунару    |  [Иди](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Ресурси**

1. Сазнајте више о Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub репозиторијум [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.