<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-07-09T19:45:27+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "uk"
}
-->
# **Квантизація Phi-3.5 за допомогою Intel OpenVINO**

Intel — це найтрадиційніший виробник процесорів з великою кількістю користувачів. З розвитком машинного навчання та глибинного навчання Intel також приєдналася до змагання за прискорення ШІ. Для інференсу моделей Intel використовує не лише GPU та CPU, а й NPU.

Ми прагнемо розгорнути сімейство Phi-3.x на кінцевих пристроях, сподіваючись стати найважливішою частиною AI PC та Copilot PC. Завантаження моделі на кінцевому пристрої залежить від співпраці різних виробників апаратного забезпечення. Цей розділ зосереджений на сценарії застосування Intel OpenVINO як інструменту для квантизації моделей.

## **Що таке OpenVINO**

OpenVINO — це відкритий набір інструментів для оптимізації та розгортання моделей глибинного навчання від хмари до периферії. Він прискорює інференс глибинного навчання у різних випадках використання, таких як генеративний ШІ, відео, аудіо та мова, з моделями з популярних фреймворків, таких як PyTorch, TensorFlow, ONNX та інших. Конвертуйте та оптимізуйте моделі, розгортаючи їх на різноманітному апаратному забезпеченні Intel® та в різних середовищах — локально, на пристрої, у браузері або в хмарі.

З OpenVINO ви можете швидко квантизувати модель GenAI на апаратному забезпеченні Intel та прискорити роботу моделі.

Наразі OpenVINO підтримує конвертацію квантизації для Phi-3.5-Vision та Phi-3.5 Instruct.

### **Налаштування середовища**

Будь ласка, переконайтеся, що встановлені всі необхідні залежності, наведені у файлі requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Квантизація Phi-3.5-Instruct за допомогою OpenVINO**

У терміналі запустіть цей скрипт

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Квантизація Phi-3.5-Vision за допомогою OpenVINO**

Запустіть цей скрипт у Python або Jupyter lab

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

### **🤖 Приклади для Phi-3.5 з Intel OpenVINO**

| Лабораторії    | Опис | Перейти |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Дізнайтеся, як використовувати Phi-3.5 Instruct на вашому AI PC    |  [Перейти](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (зображення) | Дізнайтеся, як використовувати Phi-3.5 Vision для аналізу зображень на вашому AI PC      |  [Перейти](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (відео)   | Дізнайтеся, як використовувати Phi-3.5 Vision для аналізу відео на вашому AI PC    |  [Перейти](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Ресурси**

1. Дізнайтеся більше про Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Репозиторій Intel OpenVINO на GitHub [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.