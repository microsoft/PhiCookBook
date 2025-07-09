<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e08ce816e23ad813244a09ca34ebb8ac",
  "translation_date": "2025-07-09T20:02:03+00:00",
  "source_file": "md/01.Introduction/03/AIPC_Inference.md",
  "language_code": "uk"
}
-->
# **Інференс Phi-3 на AI ПК**

З розвитком генеративного ШІ та покращенням апаратних можливостей пристроїв на периферії, дедалі більше генеративних моделей ШІ можна інтегрувати у пристрої користувачів Bring Your Own Device (BYOD). AI ПК є одними з таких моделей. Починаючи з 2024 року, Intel, AMD та Qualcomm співпрацюють з виробниками ПК для впровадження AI ПК, які полегшують розгортання локалізованих генеративних моделей ШІ через апаратні модифікації. У цій дискусії ми зосередимося на Intel AI ПК і розглянемо, як розгорнути Phi-3 на Intel AI ПК.

### Що таке NPU

NPU (Neural Processing Unit) — це спеціалізований процесор або обчислювальний блок у складі більшого SoC, призначений для прискорення операцій нейронних мереж та завдань ШІ. На відміну від універсальних CPU та GPU, NPU оптимізовані для паралельних обчислень, орієнтованих на обробку даних, що робить їх надзвичайно ефективними для обробки великих обсягів мультимедійних даних, таких як відео та зображення, а також для обробки даних нейронних мереж. Вони особливо добре справляються із завданнями, пов’язаними з ШІ, такими як розпізнавання мови, розмивання фону під час відеодзвінків, а також процесами редагування фото чи відео, наприклад, виявлення об’єктів.

## NPU проти GPU

Хоча багато завдань ШІ та машинного навчання виконуються на GPU, існує важлива різниця між GPU та NPU.  
GPU відомі своїми можливостями паралельних обчислень, але не всі GPU однаково ефективні поза межами обробки графіки. NPU, навпаки, створені спеціально для складних обчислень, пов’язаних з операціями нейронних мереж, що робить їх надзвичайно ефективними для завдань ШІ.

Підсумовуючи, NPU — це математичні генії, які прискорюють обчислення ШІ, і вони відіграють ключову роль у новій епосі AI ПК!

***Цей приклад базується на останньому процесорі Intel Core Ultra***

## **1. Використання NPU для запуску моделі Phi-3**

Пристрій Intel® NPU — це прискорювач інференсу ШІ, інтегрований з клієнтськими CPU Intel, починаючи з покоління Intel® Core™ Ultra (раніше відомого як Meteor Lake). Він забезпечує енергоефективне виконання завдань штучних нейронних мереж.

![Latency](../../../../../imgs/01/03/AIPC/aipcphitokenlatency.png)

![Latency770](../../../../../imgs/01/03/AIPC/aipcphitokenlatency770.png)

**Intel NPU Acceleration Library**

Бібліотека Intel NPU Acceleration Library [https://github.com/intel/intel-npu-acceleration-library](https://github.com/intel/intel-npu-acceleration-library) — це Python-бібліотека, створена для підвищення ефективності ваших додатків за рахунок використання потужностей Intel Neural Processing Unit (NPU) для високошвидкісних обчислень на сумісному обладнанні.

Приклад Phi-3-mini на AI ПК з процесорами Intel® Core™ Ultra.

![DemoPhiIntelAIPC](../../../../../imgs/01/03/AIPC/aipcphi3-mini.gif)

Встановіть Python-бібліотеку за допомогою pip

```bash

   pip install intel-npu-acceleration-library

```

***Примітка*** Проєкт ще розробляється, але референтна модель вже досить повна.

### **Запуск Phi-3 з Intel NPU Acceleration Library**

Використовуючи прискорення Intel NPU, ця бібліотека не впливає на традиційний процес кодування. Вам потрібно лише використати цю бібліотеку для квантизації оригінальної моделі Phi-3, наприклад FP16, INT8, INT4, як показано нижче

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

Після успішної квантизації продовжуйте виконання, щоб викликати NPU для запуску моделі Phi-3.

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

Під час виконання коду можна переглянути стан роботи NPU через Диспетчер завдань

![NPU](../../../../../imgs/01/03/AIPC/aipc_NPU.png)

***Приклади*** : [AIPC_NPU_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_NPU_DEMO.ipynb)

## **2. Використання DirectML + ONNX Runtime для запуску моделі Phi-3**

### **Що таке DirectML**

[DirectML](https://github.com/microsoft/DirectML) — це високопродуктивна апаратно-прискорена бібліотека DirectX 12 для машинного навчання. DirectML забезпечує прискорення на GPU для поширених завдань машинного навчання на широкому спектрі підтримуваного обладнання та драйверів, включно з усіма GPU, сумісними з DirectX 12, від таких виробників, як AMD, Intel, NVIDIA та Qualcomm.

Коли використовується окремо, API DirectML є низькорівневою бібліотекою DirectX 12 і підходить для високопродуктивних додатків з низькою затримкою, таких як фреймворки, ігри та інші додатки в реальному часі. Безшовна взаємодія DirectML з Direct3D 12, а також низькі накладні витрати і сумісність на різному обладнанні роблять DirectML ідеальним для прискорення машинного навчання, коли потрібна висока продуктивність і надійність результатів на різних пристроях.

***Примітка*** : Остання версія DirectML вже підтримує NPU (https://devblogs.microsoft.com/directx/introducing-neural-processor-unit-npu-support-in-directml-developer-preview/)

### Порівняння DirectML і CUDA за можливостями та продуктивністю:

**DirectML** — це бібліотека машинного навчання, розроблена Microsoft. Вона призначена для прискорення завдань машинного навчання на пристроях Windows, включно з настільними ПК, ноутбуками та периферійними пристроями.  
- Базується на DX12: DirectML побудована на DirectX 12 (DX12), що забезпечує широку підтримку апаратного забезпечення на GPU, включно з NVIDIA та AMD.  
- Широка підтримка: Оскільки вона використовує DX12, DirectML може працювати з будь-яким GPU, що підтримує DX12, навіть інтегрованими.  
- Обробка зображень: DirectML обробляє зображення та інші дані за допомогою нейронних мереж, що робить її придатною для завдань розпізнавання зображень, виявлення об’єктів тощо.  
- Простота налаштування: Налаштування DirectML просте і не вимагає специфічних SDK або бібліотек від виробників GPU.  
- Продуктивність: У деяких випадках DirectML працює добре і може бути швидшим за CUDA, особливо для певних завдань.  
- Обмеження: Однак іноді DirectML може працювати повільніше, особливо при великих пакетах float16.

**CUDA** — це платформа паралельних обчислень і модель програмування від NVIDIA. Вона дозволяє розробникам використовувати потужності GPU NVIDIA для загальних обчислень, включно з машинним навчанням і науковими симуляціями.  
- Специфічна для NVIDIA: CUDA тісно інтегрована з GPU NVIDIA і розроблена спеціально для них.  
- Висока оптимізація: Забезпечує відмінну продуктивність для завдань з прискоренням на GPU, особливо на GPU NVIDIA.  
- Широке використання: Багато фреймворків і бібліотек машинного навчання (наприклад, TensorFlow і PyTorch) підтримують CUDA.  
- Налаштування: Розробники можуть тонко налаштовувати CUDA для конкретних завдань, що може призвести до оптимальної продуктивності.  
- Обмеження: Однак залежність від апаратного забезпечення NVIDIA може бути обмеженням, якщо потрібна ширша сумісність з різними GPU.

### Вибір між DirectML і CUDA

Вибір між DirectML і CUDA залежить від вашого конкретного випадку використання, наявного обладнання та уподобань.  
Якщо вам потрібна ширша сумісність і простота налаштування, DirectML може бути хорошим вибором. Якщо ж у вас є GPU NVIDIA і потрібна висока оптимізована продуктивність, CUDA залишається сильним кандидатом. Підсумовуючи, обидві технології мають свої переваги та недоліки, тому враховуйте ваші вимоги та доступне обладнання при прийнятті рішення.

### **Генеративний ШІ з ONNX Runtime**

В епоху ШІ портативність моделей дуже важлива. ONNX Runtime дозволяє легко розгортати навчені моделі на різних пристроях. Розробникам не потрібно турбуватися про фреймворк інференсу — вони використовують уніфікований API для виконання інференсу моделі. В епоху генеративного ШІ ONNX Runtime також виконує оптимізацію коду (https://onnxruntime.ai/docs/genai/). Завдяки оптимізованому ONNX Runtime квантизована генеративна модель ШІ може виконуватися на різних пристроях. У Generative AI з ONNX Runtime можна викликати API моделі ШІ через Python, C#, C / C++. Звісно, розгортання на iPhone може використовувати C++ API Generative AI з ONNX Runtime.

[Приклад коду](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx)

***компіляція бібліотеки generative AI з ONNX Runtime***

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

**Встановлення бібліотеки**

```bash

pip install .\onnxruntime_genai_directml-0.3.0.dev0-cp310-cp310-win_amd64.whl

```

Ось результат виконання

![DML](../../../../../imgs/01/03/AIPC/aipc_DML.png)

***Приклади*** : [AIPC_DirectML_DEMO.ipynb](../../../../../code/03.Inference/AIPC/AIPC_DirectML_DEMO.ipynb)

## **3. Використання Intel OpenVino для запуску моделі Phi-3**

### **Що таке OpenVINO**

[OpenVINO](https://github.com/openvinotoolkit/openvino) — це відкритий набір інструментів для оптимізації та розгортання моделей глибокого навчання. Він забезпечує підвищену продуктивність глибокого навчання для моделей з обробки зору, аудіо та мови з популярних фреймворків, таких як TensorFlow, PyTorch та інших. Почніть роботу з OpenVINO. OpenVINO також можна використовувати у поєднанні з CPU та GPU для запуску моделі Phi-3.

***Примітка***: Наразі OpenVINO не підтримує NPU.

### **Встановлення бібліотеки OpenVINO**

```bash

 pip install git+https://github.com/huggingface/optimum-intel.git

 pip install git+https://github.com/openvinotoolkit/nncf.git

 pip install openvino-nightly

```

### **Запуск Phi-3 з OpenVINO**

Як і NPU, OpenVINO виконує виклик генеративних моделей ШІ через запуск квантизованих моделей. Спочатку потрібно квантизувати модель Phi-3 і завершити квантизацію через командний рядок за допомогою optimum-cli

**INT4**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code ./openvinomodel/phi3/int4

```

**FP16**

```bash

optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format fp16 --trust-remote-code ./openvinomodel/phi3/fp16

```

конвертований формат виглядає так

![openvino_convert](../../../../../imgs/01/03/AIPC/aipc_OpenVINO_convert.png)

Завантажте шляхи до моделі (model_dir), відповідні конфігурації (ov_config = {"PERFORMANCE_HINT": "LATENCY", "NUM_STREAMS": "1", "CACHE_DIR": ""}) та апаратно-прискорені пристрої (GPU.0) через OVModelForCausalLM

```python

ov_model = OVModelForCausalLM.from_pretrained(
     model_dir,
     device='GPU.0',
     ov_config=ov_config,
     config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
     trust_remote_code=True,
)

```

Під час виконання коду можна переглянути стан роботи GPU через Диспетчер завдань

![openvino_gpu](../../../../../imgs/01/03/AIPC/aipc_OpenVINO_GPU.png)

***Приклади*** : [AIPC_OpenVino_Demo.ipynb](../../../../../code/03.Inference/AIPC/AIPC_OpenVino_Demo.ipynb)

### ***Примітка*** : Кожен із трьох наведених методів має свої переваги, але для інференсу на AI ПК рекомендується використовувати прискорення NPU.

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.