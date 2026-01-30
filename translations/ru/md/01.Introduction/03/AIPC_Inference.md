# **Инференс Phi-3 на AI ПК**

С развитием генеративного ИИ и улучшением аппаратных возможностей устройств на периферии, всё больше генеративных моделей ИИ можно интегрировать в устройства пользователей с концепцией Bring Your Own Device (BYOD). AI ПК — одни из таких моделей. Начиная с 2024 года, Intel, AMD и Qualcomm сотрудничают с производителями ПК для выпуска AI ПК, которые упрощают развертывание локальных генеративных моделей ИИ за счёт аппаратных изменений. В этом обсуждении мы сосредоточимся на Intel AI ПК и рассмотрим, как развернуть Phi-3 на Intel AI ПК.

### Что такое NPU

NPU (Neural Processing Unit) — это специализированный процессор или вычислительный блок в составе более крупного SoC, предназначенный для ускорения операций нейронных сетей и задач ИИ. В отличие от универсальных CPU и GPU, NPU оптимизированы для параллельных вычислений с данными, что делает их очень эффективными при обработке больших объёмов мультимедийных данных, таких как видео и изображения, а также при работе с нейронными сетями. Они особенно хорошо справляются с задачами ИИ, такими как распознавание речи, размытие фона в видеозвонках и обработка фото- и видеоматериалов, например, обнаружение объектов.

## NPU против GPU

Хотя многие задачи ИИ и машинного обучения выполняются на GPU, между GPU и NPU есть важное различие.  
GPU известны своими возможностями параллельных вычислений, но не все GPU одинаково эффективны вне графической обработки. NPU же специально созданы для сложных вычислений, связанных с нейронными сетями, что делает их очень эффективными для задач ИИ.

В итоге, NPU — это настоящие «математические гении», которые ускоряют вычисления ИИ и играют ключевую роль в новой эре AI ПК!

***Этот пример основан на последнем процессоре Intel Core Ultra***

## **1. Использование NPU для запуска модели Phi-3**

Устройство Intel® NPU — это ускоритель инференса ИИ, интегрированный с клиентскими процессорами Intel, начиная с поколения Intel® Core™ Ultra (ранее известного как Meteor Lake). Он обеспечивает энергоэффективное выполнение задач искусственных нейронных сетей.

![Задержка](../../../../../translated_images/ru/aipcphitokenlatency.2be14f04f30a3bf7.webp)

![Задержка770](../../../../../translated_images/ru/aipcphitokenlatency770.e923609a57c5d394.webp)

**Библиотека ускорения Intel NPU**

Библиотека Intel NPU Acceleration Library [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library) — это Python-библиотека, созданная для повышения эффективности ваших приложений за счёт использования мощности Intel Neural Processing Unit (NPU) для высокоскоростных вычислений на совместимом оборудовании.

Пример Phi-3-mini на AI ПК с процессорами Intel® Core™ Ultra.

![ДемоPhiIntelAIPC](../../../../../imgs/01/03/AIPC/aipcphi3-mini.gif)

Установка Python-библиотеки через pip

```bash

   pip install intel-npu-acceleration-library

```

***Примечание*** Проект всё ещё в разработке, но эталонная модель уже достаточно полная.

### **Запуск Phi-3 с помощью Intel NPU Acceleration Library**

Используя ускорение Intel NPU, эта библиотека не влияет на традиционный процесс кодирования. Вам нужно лишь использовать её для квантизации исходной модели Phi-3, например, в FP16, INT8, INT4, например:

```python
from transformers import AutoTokenizer, pipeline,TextStreamer
from intel_npu_acceleration_library import NPUModelForCausalLM, int4
from intel_npu_acceleration_library.compiler import CompilerConfig
import warnings

model_id = "microsoft/Phi-3-mini-4k-instruct"

compiler_conf = CompilerConfig(dtype=int4)
model = NPUModelForCausalLM.from_pretrained(
    model_id, use_cache=True, config=compiler_conf, attn_implementation="sdpa"
).eval()

tokenizer = AutoTokenizer.from_pretrained(model_id)

text_streamer = TextStreamer(tokenizer, skip_prompt=True)
```

После успешной квантизации продолжайте выполнение, чтобы вызвать NPU для запуска модели Phi-3.

```python
generation_args = {
   "max_new_tokens": 1024,
   "return_full_text": False,
   "temperature": 0.3,
   "do_sample": False,
   "streamer": text_streamer,
}

pipe = pipeline(
   "text-generation",
   model=model,
   tokenizer=tokenizer,
)

query = "<|system|>You are a helpful AI assistant.<|end|><|user|>Can you introduce yourself?<|end|><|assistant|>"

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    pipe(query, **generation_args)
```

При выполнении кода можно наблюдать состояние работы NPU через Диспетчер задач

![NPU](../../../../../translated_images/ru/aipc_NPU.7a3cb6db47b377e1.webp)

***Примеры*** : [AIPC_NPU_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)

## **2. Использование DirectML + ONNX Runtime для запуска модели Phi-3**

### **Что такое DirectML**

[DirectML](https://github.com/microsoft/DirectML) — это высокопроизводительная аппаратно-ускоренная библиотека DirectX 12 для машинного обучения. DirectML обеспечивает ускорение на GPU для распространённых задач машинного обучения на широком спектре поддерживаемого оборудования и драйверов, включая все GPU с поддержкой DirectX 12 от таких производителей, как AMD, Intel, NVIDIA и Qualcomm.

При самостоятельном использовании API DirectML представляет собой низкоуровневую библиотеку DirectX 12, подходящую для высокопроизводительных приложений с низкой задержкой, таких как фреймворки, игры и другие приложения реального времени. Бесшовная совместимость DirectML с Direct3D 12, а также низкие накладные расходы и единообразие работы на разном оборудовании делают DirectML идеальным для ускорения машинного обучения, когда важны высокая производительность и надёжность результатов на разных устройствах.

***Примечание*** : Последняя версия DirectML уже поддерживает NPU (https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/)

### Сравнение DirectML и CUDA по возможностям и производительности:

**DirectML** — библиотека машинного обучения от Microsoft, предназначенная для ускорения задач машинного обучения на устройствах с Windows, включая настольные ПК, ноутбуки и периферийные устройства.  
- Основана на DX12: DirectML построена на DirectX 12, что обеспечивает широкую поддержку оборудования, включая GPU от NVIDIA и AMD.  
- Широкая поддержка: благодаря DX12 DirectML работает с любыми GPU, поддерживающими DX12, включая интегрированные.  
- Обработка изображений: DirectML обрабатывает изображения и другие данные с помощью нейронных сетей, что подходит для задач распознавания изображений, обнаружения объектов и др.  
- Простота настройки: установка DirectML проста и не требует специфичных SDK или библиотек от производителей GPU.  
- Производительность: в некоторых случаях DirectML работает быстрее CUDA, особенно для определённых задач.  
- Ограничения: однако в некоторых сценариях DirectML может работать медленнее, особенно при больших пакетах с float16.

**CUDA** — платформа параллельных вычислений и программная модель от NVIDIA, позволяющая разработчикам использовать мощь GPU NVIDIA для общих вычислений, включая машинное обучение и научные симуляции.  
- Специфично для NVIDIA: CUDA тесно интегрирована с GPU NVIDIA и предназначена именно для них.  
- Высокая оптимизация: обеспечивает отличную производительность для задач с ускорением на GPU, особенно на GPU NVIDIA.  
- Широкое использование: многие фреймворки и библиотеки машинного обучения (например, TensorFlow и PyTorch) поддерживают CUDA.  
- Настройка: разработчики могут тонко настраивать CUDA для конкретных задач, что позволяет добиться оптимальной производительности.  
- Ограничения: зависимость от оборудования NVIDIA ограничивает совместимость с другими GPU.

### Выбор между DirectML и CUDA

Выбор между DirectML и CUDA зависит от конкретных задач, доступного оборудования и предпочтений.  
Если нужна широкая совместимость и простота настройки, DirectML может быть хорошим выбором. Если у вас есть GPU NVIDIA и требуется максимальная оптимизация, CUDA остаётся сильным вариантом. В итоге и DirectML, и CUDA имеют свои плюсы и минусы, поэтому учитывайте свои требования и доступное оборудование при выборе.

### **Генеративный ИИ с ONNX Runtime**

В эпоху ИИ важна переносимость моделей. ONNX Runtime позволяет легко развертывать обученные модели на разных устройствах. Разработчикам не нужно заботиться о фреймворке инференса — используется единый API для выполнения инференса. В эпоху генеративного ИИ ONNX Runtime также оптимизирует код (https://onnxruntime.ai/docs/genai/). Благодаря оптимизированному ONNX Runtime квантизированную генеративную модель ИИ можно запускать на разных устройствах. В Generative AI с ONNX Runtime можно выполнять инференс моделей ИИ через Python, C#, C/C++. Развёртывание на iPhone может использовать преимущества C++ API Generative AI с ONNX Runtime.

[Пример кода](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***Компиляция библиотеки Generative AI с ONNX Runtime***

```bash

winget install --id=Kitware.CMake  -e

git clone https://github.com/microsoft/onnxruntime.git

cd .\onnxruntime\

./build.bat --build_shared_lib --skip_tests --parallel --use_dml --config Release

cd ../

git clone https://github.com/microsoft/onnxruntime-genai.git

cd .\onnxruntime-genai\

mkdir ort

cd ort

mkdir include

mkdir lib

copy ..\onnxruntime\include\onnxruntime\core\providers\dml\dml_provider_factory.h ort\include

copy ..\onnxruntime\include\onnxruntime\core\session\onnxruntime_c_api.h ort\include

copy ..\onnxruntime\build\Windows\Release\Release\*.dll ort\lib

copy ..\onnxruntime\build\Windows\Release\Release\onnxruntime.lib ort\lib

python build.py --use_dml


```

**Установка библиотеки**

```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

Результат выполнения

![DML](../../../../../translated_images/ru/aipc_DML.52a44180393ab491.webp)

***Примеры*** : [AIPC_DirectML_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. Использование Intel OpenVINO для запуска модели Phi-3**

### **Что такое OpenVINO**

[OpenVINO](https://github.com/openvinotoolkit/openvino) — это открытый набор инструментов для оптимизации и развертывания моделей глубокого обучения. Он обеспечивает ускорение глубокого обучения для моделей зрения, аудио и языка из популярных фреймворков, таких как TensorFlow, PyTorch и других. Начните работу с OpenVINO. OpenVINO также можно использовать в сочетании с CPU и GPU для запуска модели Phi-3.

***Примечание***: В настоящее время OpenVINO не поддерживает NPU.

### **Установка библиотеки OpenVINO**

```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **Запуск Phi-3 с OpenVINO**

Как и NPU, OpenVINO выполняет вызов генеративных моделей ИИ через запуск квантизированных моделей. Сначала нужно квантизировать модель Phi-3 и выполнить квантизацию через командную строку с помощью optimum-cli.

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

Преобразованный формат выглядит так

![openvino_convert](../../../../../translated_images/ru/aipc_OpenVINO_convert.9e6360b65331ffca.webp)

Загрузите пути к модели (model_dir), соответствующие настройки (ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""}) и аппаратно-ускоренные устройства (GPU.0) через OVModelForCausalLM

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

При выполнении кода можно наблюдать состояние работы GPU через Диспетчер задач

![openvino_gpu](../../../../../translated_images/ru/aipc_OpenVINO_GPU.20180edfffd91e55.webp)

***Примеры*** : [AIPC_OpenVino_Demo.ipynb](../../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***Примечание*** : Все три описанных метода имеют свои преимущества, но для инференса на AI ПК рекомендуется использовать ускорение через NPU.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.