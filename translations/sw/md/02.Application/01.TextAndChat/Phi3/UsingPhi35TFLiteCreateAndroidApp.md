<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:50:18+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "sw"
}
-->
# **Kutumia Microsoft Phi-3.5 tflite kuunda app ya Android**

Hii ni mfano wa Android kutumia modeli za Microsoft Phi-3.5 tflite.

## **📚 Maarifa**

Android LLM Inference API inakuwezesha kuendesha modeli kubwa za lugha (LLMs) kabisa ndani ya kifaa kwa ajili ya programu za Android, ambazo unaweza kutumia kufanya kazi mbalimbali, kama kuandika maandishi, kupata taarifa kwa lugha ya kawaida, na kufupisha nyaraka. Kazi hii ina msaada wa moja kwa moja kwa modeli nyingi kubwa za lugha za aina ya maandishi-kwa-maandishi, hivyo unaweza kutumia modeli za kisasa za AI zinazotumia kifaa moja kwa moja kwenye programu zako za Android.

Googld AI Edge Torch ni maktaba ya python inayosaidia kubadilisha modeli za PyTorch kuwa muundo wa .tflite, ambao unaweza kuendeshwa kwa TensorFlow Lite na MediaPipe. Hii inaruhusu programu za Android, iOS na IoT kuendesha modeli moja kwa moja kwenye kifaa. AI Edge Torch ina msaada mpana wa CPU, na msaada wa awali wa GPU na NPU. AI Edge Torch inalenga kuunganishwa kwa karibu na PyTorch, ikijengwa juu ya torch.export() na kutoa msaada mzuri kwa Core ATen operators.


## **🪬 Mwongozo**

### **🔥 Badilisha Microsoft Phi-3.5 kuwa tflite**

0. Mfano huu ni kwa Android 14+

1. Sakinisha Python 3.10.12

***Pendekezo:*** tumia conda kusakinisha mazingira yako ya Python

2. Ubuntu 20.04 / 22.04 (tafadhali zingatia [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Pendekezo:*** Tumia Azure Linux VM au cloud VM ya mtu wa tatu kuunda mazingira yako

3. Nenda kwenye bash ya Linux yako, kusakinisha maktaba za Python

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Pakua Microsoft-3.5-Instruct kutoka Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Badilisha Microsoft Phi-3.5 kuwa tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```


### **🔥 Badilisha Microsoft Phi-3.5 kuwa Android Mediapipe Bundle**

tafadhali sakinisha mediapipe kwanza

```bash

pip install mediapipe

```

endesha msimbo huu katika [daftari lako](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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


### **🔥 Tumia adb push kuhamisha modeli ya task kwenye njia ya kifaa chako cha Android**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Kuendesha msimbo wako wa Android**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.sw.png)

**Kiarifu cha Kutokujali**:  
Hati hii imetafsiriwa kwa kutumia huduma ya utafsiri wa AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inashauriwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.