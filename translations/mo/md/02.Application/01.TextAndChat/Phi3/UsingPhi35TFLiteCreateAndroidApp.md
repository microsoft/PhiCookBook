<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2faa9c6d61c5aa2708aec02a39ec464b",
  "translation_date": "2025-04-04T12:43:56+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "mo"
}
-->
# **Microsoft Phi-3.5 tflite ka yi amfani da shi don ƙirƙirar aikace-aikacen Android**

Wannan misali ne na Android da ke amfani da samfuran Microsoft Phi-3.5 tflite.

## **📚 Ilimi**

Android LLM Inference API yana ba ka damar gudanar da manyan samfuran harshe (LLMs) gaba ɗaya a kan na'urar don aikace-aikacen Android, wanda zaka iya amfani da shi don aiwatar da ayyuka iri-iri, kamar samar da rubutu, samun bayanai cikin harshe na halitta, da taƙaitawa takardu. Wannan aikin yana ba da tallafi na gina a ciki don samfuran manyan harshe na rubutu-zuwa-rubutu, don haka zaka iya amfani da sabbin samfuran AI na ƙirƙira akan na'urar don aikace-aikacen Android.

Googld AI Edge Torch wata ɗakunan karatu ne na python wanda ke tallafawa canza samfuran PyTorch zuwa tsari na .tflite, wanda daga nan za a iya gudanar da shi tare da TensorFlow Lite da MediaPipe. Wannan yana ba da damar aikace-aikace don Android, iOS da IoT wanda zai iya gudanar da samfuran gaba ɗaya a kan na'urar. AI Edge Torch yana ba da tallafi mai faɗi ga CPU, tare da tallafi na farko don GPU da NPU. AI Edge Torch yana neman haɗin kai sosai tare da PyTorch, gina a saman torch.export() da kuma ba da tallafi mai kyau ga Core ATen masu aiki.

## **🪬 Jagora**

### **🔥 Canza Microsoft Phi-3.5 zuwa tallafi na tflite**

0. Wannan misali yana da Android 14+

1. Shigar da Python 3.10.12

***Shawara:*** yin amfani da conda don shigar da yanayin Python ɗinka

2. Ubuntu 20.04 / 22.04 (da fatan a mai da hankali kan [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Shawara:*** Amfani da Azure Linux VM ko VM na cloud na ɓangare na uku don ƙirƙirar yanayin ɗinka

3. Je zuwa bash ɗin Linux ɗinka, don shigar da ɗakunan karatu na Python 

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Zazzage Microsoft-3.5-Instruct daga Hugging face


```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Canza Microsoft Phi-3.5 zuwa tflite


```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```


### **🔥 Canza Microsoft Phi-3.5 zuwa Android Mediapipe Bundle**

da fatan za a fara shigar da mediapipe

```bash

pip install mediapipe

```

gudanar da wannan lambar a cikin [notebook ɗinku](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)



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


### **🔥 Yin amfani da adb don turawa samfurin aikin zuwa hanyar na'urar Android ɗinka**


```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Gudanar da lambar Android ɗinka**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.mo.png)

It seems you want the text translated into "mo," but could you clarify what "mo" refers to? Are you asking for translation into Māori, Montenegrin, or another language?