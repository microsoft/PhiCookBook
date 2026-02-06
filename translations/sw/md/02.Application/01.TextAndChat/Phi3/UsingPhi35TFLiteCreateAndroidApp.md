# **Kutumia Microsoft Phi-3.5 tflite kuunda app ya Android**

Hii ni mfano wa Android unaotumia mifano ya Microsoft Phi-3.5 tflite.

## **📚 Maarifa**

Android LLM Inference API inakuwezesha kuendesha mifano mikubwa ya lugha (LLMs) kabisa kwenye kifaa kwa ajili ya programu za Android, ambazo unaweza kutumia kufanya kazi mbalimbali, kama vile kuunda maandishi, kupata taarifa kwa lugha ya asili, na kufupisha nyaraka. Kazi hii ina msaada wa ndani kwa mifano mingi ya lugha kubwa ya maandishi kwa maandishi, hivyo unaweza kutumia mifano ya kisasa ya AI ya kizazi inayotumia kifaa moja kwa moja kwenye programu zako za Android.

Google AI Edge Torch ni maktaba ya python inayounga mkono kubadilisha mifano ya PyTorch kuwa muundo wa .tflite, ambayo inaweza kuendeshwa kwa TensorFlow Lite na MediaPipe. Hii inaruhusu programu za Android, iOS na IoT kuendesha mifano kabisa kwenye kifaa. AI Edge Torch inatoa msaada mpana wa CPU, pamoja na msaada wa awali wa GPU na NPU. AI Edge Torch inalenga kuunganishwa kwa karibu na PyTorch, ikijengwa juu ya torch.export() na kutoa msaada mzuri wa Core ATen operators.

## **🪬 Mwongozo**

### **🔥 Badilisha Microsoft Phi-3.5 kuwa tflite**

0. Mfano huu ni kwa Android 14+

1. Sakinisha Python 3.10.12

***Pendekezo:*** tumia conda kusakinisha mazingira yako ya Python

2. Ubuntu 20.04 / 22.04 (tafadhali zingatia [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Pendekezo:*** Tumia Azure Linux VM au cloud vm ya mtu wa tatu kuunda mazingira yako

3. Nenda kwenye bash ya Linux yako, kusakinisha maktaba ya Python

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

### **🔥 Tumia adb push kuhamisha mfano wa kazi kwenye njia ya vifaa vyako vya Android**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Kuendesha msimbo wako wa Android**

![demo](../../../../../../translated_images/sw/demo.06d5a4246f057d1b.webp)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.