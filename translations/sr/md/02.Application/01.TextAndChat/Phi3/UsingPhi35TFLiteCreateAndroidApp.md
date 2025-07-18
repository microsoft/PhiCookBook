<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:55:25+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "sr"
}
-->
# **Коришћење Microsoft Phi-3.5 tflite за креирање Android апликације**

Ово је пример за Android који користи Microsoft Phi-3.5 tflite моделе.

## **📚 Знање**

Android LLM Inference API вам омогућава да покрећете велике језичке моделе (LLM) потпуно на уређају за Android апликације, које можете користити за извођење широког спектра задатака, као што су генерисање текста, проналажење информација у природном језику и сажимање докумената. Овај задатак пружа уграђену подршку за више текстуалних великих језичких модела, тако да можете применити најновије генеративне AI моделе на уређају у вашим Android апликацијама.

Google AI Edge Torch је Python библиотека која подржава конвертовање PyTorch модела у .tflite формат, који се затим може покретати уз TensorFlow Lite и MediaPipe. Ово омогућава апликације за Android, iOS и IoT које могу да извршавају моделе потпуно на уређају. AI Edge Torch нуди широку подршку за CPU, са почетном подршком за GPU и NPU. AI Edge Torch тежи да се тесно интегрише са PyTorch-ом, надограђујући torch.export() и пружајући добру покривеност Core ATen оператора.

## **🪬 Упутство**

### **🔥 Конвертовање Microsoft Phi-3.5 у tflite формат**

0. Овај пример је за Android 14+

1. Инсталирајте Python 3.10.12

***Препорука:*** користите conda за инсталацију вашег Python окружења

2. Ubuntu 20.04 / 22.04 (обратите пажњу на [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Препорука:*** Користите Azure Linux VM или cloud VM треће стране за креирање окружења

3. Отворите Linux bash и инсталирајте Python библиотеку

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Преузмите Microsoft-3.5-Instruct са Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Конвертујте Microsoft Phi-3.5 у tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Конвертовање Microsoft Phi-3.5 у Android Mediapipe пакет**

прво инсталирајте mediapipe

```bash

pip install mediapipe

```

покрените овај код у [вашем notebook-у](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Копирање модела на Android уређај помоћу adb push**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Покретање вашег Android кода**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1be99ffad0cbf22f4ac0c41530774d51ff903cfaa1d3cd3c8e.sr.png)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.