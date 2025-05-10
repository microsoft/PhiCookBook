<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:50:56+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "bg"
}
-->
# **Използване на Microsoft Phi-3.5 tflite за създаване на Android приложение**

Това е пример за Android, използващ Microsoft Phi-3.5 tflite модели.

## **📚 Знания**

Android LLM Inference API позволява да изпълнявате големи езикови модели (LLM) изцяло на устройството за Android приложения, което можете да използвате за изпълнение на различни задачи, като генериране на текст, извличане на информация на естествен език и обобщаване на документи. Тази задача предлага вградена поддръжка за множество големи езикови модели тип текст към текст, така че можете да приложите най-новите генеративни AI модели на устройството към вашите Android приложения.

Google AI Edge Torch е Python библиотека, която поддържа конвертиране на PyTorch модели в .tflite формат, който след това може да се изпълнява с TensorFlow Lite и MediaPipe. Това позволява приложения за Android, iOS и IoT, които могат да изпълняват модели изцяло на устройството. AI Edge Torch предлага широка поддръжка за CPU, с начална поддръжка за GPU и NPU. AI Edge Torch се стреми към тясна интеграция с PyTorch, изграждайки се върху torch.export() и осигурявайки добра поддръжка на Core ATen оператори.

## **🪬 Насоки**

### **🔥 Конвертиране на Microsoft Phi-3.5 към tflite формат**

0. Този пример е за Android 14+

1. Инсталирайте Python 3.10.12

***Препоръка:*** използвайте conda за инсталиране на вашата Python среда

2. Ubuntu 20.04 / 22.04 (моля, обърнете внимание на [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Препоръка:*** Използвайте Azure Linux VM или трета страна облачен VM за създаване на вашата среда

3. Отидете в Linux bash, за да инсталирате Python библиотеката

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Изтеглете Microsoft-3.5-Instruct от Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Конвертирайте Microsoft Phi-3.5 към tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Конвертиране на Microsoft Phi-3.5 към Android Mediapipe Bundle**

моля първо инсталирайте mediapipe

```bash

pip install mediapipe

```

изпълнете този код във [вашия notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

```python

import mediapipe as mp
from mediapipe.tasks.python.genai import bundler

config = bundler.BundleConfig(
    tflite_model='Your Phi-3.5 tflite model path',
    tokenizer_model='Your Phi-3.5 tokenizer model path',
    start_token='start_token',
    stop_tokens=[STOP_TOKENS],
    output_filename='Your Phi-3.5 task model path',
    enable_bytes_to_unicode_mapping=True or Flase,
)
bundler.create_bundle(config)

```

### **🔥 Използване на adb push за прехвърляне на модела към пътя на вашето Android устройство**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Стартиране на вашия Android код**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.bg.png)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия оригинален език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, възникнали от използването на този превод.