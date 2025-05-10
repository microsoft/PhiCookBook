<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-05-09T14:03:33+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "bg"
}
-->
# **Квантизиране на Phi-3.5 с Intel OpenVINO**

Intel е най-традиционният производител на процесори с много потребители. С нарастването на машинното обучение и дълбокото обучение, Intel също се включи в състезанието за ускоряване на изкуствения интелект. За извършване на модели, Intel използва не само GPU и CPU, но и NPU.

Надяваме се да внедрим семейството Phi-3.x на крайното устройство, като се стремим да стане най-важната част от AI PC и Copilot PC. Зареждането на модела на крайното устройство зависи от сътрудничеството на различни хардуерни производители. Тази глава се фокусира главно върху приложния сценарий на Intel OpenVINO като квантизиран модел.

## **Какво е OpenVINO**

OpenVINO е отворен инструментариум за оптимизация и внедряване на модели за дълбоко обучение от облака до периферията. Той ускорява извършването на дълбоко обучение в различни случаи на употреба, като генеративен AI, видео, аудио и език с модели от популярни рамки като PyTorch, TensorFlow, ONNX и други. Конвертирайте и оптимизирайте модели и ги внедрявайте в разнообразие от хардуер и среди на Intel®, локално или на устройството, в браузър или в облака.

Сега с OpenVINO можете бързо да квантизирате GenAI модел в хардуер на Intel и да ускорите препратката на модела.

В момента OpenVINO поддържа квантизационна конверсия на Phi-3.5-Vision и Phi-3.5 Instruct.

### **Настройка на средата**

Моля, уверете се, че следните зависимости на средата са инсталирани, това е requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Квантизиране на Phi-3.5-Instruct с OpenVINO**

В терминала изпълнете този скрипт

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Квантизиране на Phi-3.5-Vision с OpenVINO**

Моля, изпълнете този скрипт в Python или Jupyter lab

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

### **🤖 Примери за Phi-3.5 с Intel OpenVINO**

| Лаборатории    | Въведение | Отиди |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Научете как да използвате Phi-3.5 Instruct в своя AI PC    |  [Отиди](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Научете как да използвате Phi-3.5 Vision за анализ на изображения в своя AI PC      |  [Отиди](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | Научете как да използвате Phi-3.5 Vision за анализ на видео в своя AI PC    |  [Отиди](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Ресурси**

1. Научете повече за Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.