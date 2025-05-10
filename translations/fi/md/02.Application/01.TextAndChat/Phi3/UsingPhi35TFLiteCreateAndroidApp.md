<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:49:27+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "fi"
}
-->
# **Microsoft Phi-3.5 tflite:n käyttäminen Android-sovelluksen luomiseen**

Tämä on Android-esimerkki, joka käyttää Microsoft Phi-3.5 tflite -malleja.

## **📚 Tietoa**

Android LLM Inference API mahdollistaa suurten kielimallien (LLM) ajamisen kokonaan laitteella Android-sovelluksissa. Voit käyttää sitä monenlaisiin tehtäviin, kuten tekstin luomiseen, luonnollisen kielen muotoisen tiedon hakemiseen ja dokumenttien tiivistämiseen. Tehtävä tukee useita tekstistä tekstiin -suuret kielimallit, joten voit hyödyntää uusimpia generatiivisen tekoälyn malleja suoraan Android-sovelluksissasi.

Googld AI Edge Torch on Python-kirjasto, joka tukee PyTorch-mallien muuntamista .tflite-muotoon, jota voi sitten käyttää TensorFlow Liten ja MediaPipen kanssa. Tämä mahdollistaa sovellukset Androidille, iOS:lle ja IoT-laitteille, jotka voivat ajaa malleja kokonaan laitteella. AI Edge Torch tarjoaa laajan CPU-tuen sekä alkuvaiheen GPU- ja NPU-tuen. AI Edge Torch pyrkii tiiviiseen integraatioon PyTorchin kanssa hyödyntäen torch.export()-toimintoa ja kattavaa Core ATen -operaattoreiden tukea.

## **🪬 Ohjeet**

### **🔥 Microsoft Phi-3.5:n muuntaminen tflite-muotoon**

0. Tämä esimerkki on tarkoitettu Android 14+:lle

1. Asenna Python 3.10.12

***Vinkki:*** käytä condaa Python-ympäristön asentamiseen

2. Ubuntu 20.04 / 22.04 (kiinnitä huomiota [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Vinkki:*** käytä Azure Linux VM:ää tai kolmannen osapuolen pilvipalvelua ympäristön luomiseen

3. Mene Linuxin bashiin ja asenna Python-kirjasto

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Lataa Microsoft-3.5-Instruct Hugging Facesta

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Muunna Microsoft Phi-3.5 tflite-muotoon

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Muunna Microsoft Phi-3.5 Android Mediapipe Bundleksi**

asenna ensin mediapipe

```bash

pip install mediapipe

```

Suorita tämä koodi [muistikirjassasi](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Lähetä task-malli adb push -komennolla Android-laitteesi polkuun**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Suorita Android-koodisi**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.fi.png)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ota huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.