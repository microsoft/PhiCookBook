<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3139a6a82f357a9f90f1fe51c4caf65a",
  "translation_date": "2025-07-16T21:58:45+00:00",
  "source_file": "md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md",
  "language_code": "ru"
}
-->
# **Квантование Phi-3.5 с использованием Intel OpenVINO**

Intel — самый традиционный производитель процессоров с большим количеством пользователей. С ростом популярности машинного обучения и глубокого обучения Intel также присоединился к гонке за ускорение ИИ. Для инференса моделей Intel использует не только GPU и CPU, но и NPU.

Мы надеемся развернуть семейство Phi-3.x на конечных устройствах, стремясь стать важнейшей частью AI PC и Copilot PC. Загрузка модели на конечном устройстве зависит от сотрудничества различных производителей аппаратного обеспечения. В этой главе основное внимание уделяется сценарию применения Intel OpenVINO для квантованной модели.

## **Что такое OpenVINO**

OpenVINO — это открытый набор инструментов для оптимизации и развертывания моделей глубокого обучения от облака до периферии. Он ускоряет инференс глубокого обучения в различных сценариях, таких как генеративный ИИ, видео, аудио и обработка языка, с моделями из популярных фреймворков, таких как PyTorch, TensorFlow, ONNX и других. Конвертируйте и оптимизируйте модели, а затем разворачивайте их на различных устройствах и средах Intel®, как локально, так и на устройстве, в браузере или в облаке.

С помощью OpenVINO вы можете быстро выполнить квантование модели GenAI на оборудовании Intel и ускорить работу модели.

В настоящее время OpenVINO поддерживает конвертацию квантованных моделей Phi-3.5-Vision и Phi-3.5 Instruct.

### **Настройка окружения**

Пожалуйста, убедитесь, что установлены все необходимые зависимости, указанные в requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Квантование Phi-3.5-Instruct с помощью OpenVINO**

В терминале выполните следующий скрипт

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Квантование Phi-3.5-Vision с помощью OpenVINO**

Запустите этот скрипт в Python или Jupyter lab

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

### **🤖 Примеры для Phi-3.5 с Intel OpenVINO**

| Лаборатории    | Описание | Перейти |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Узнайте, как использовать Phi-3.5 Instruct на вашем AI PC    |  [Перейти](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (изображение) | Узнайте, как использовать Phi-3.5 Vision для анализа изображений на вашем AI PC      |  [Перейти](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (видео)   | Узнайте, как использовать Phi-3.5 Vision для анализа видео на вашем AI PC    |  [Перейти](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Ресурсы**

1. Подробнее об Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Репозиторий Intel OpenVINO на GitHub [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.