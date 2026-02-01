# **Microsoft Phi-3.5 tflite'i kasutamine Androidi rakenduse loomiseks**

See on Androidi näidis, mis kasutab Microsoft Phi-3.5 tflite mudeleid.

## **📚 Teadmised**

Android LLM Inference API võimaldab käitada suuri keelemudeleid (LLM) täielikult seadmesiseselt Androidi rakenduste jaoks. Seda saab kasutada mitmesuguste ülesannete täitmiseks, nagu teksti genereerimine, teabe hankimine loomuliku keele vormis ja dokumentide kokkuvõtete loomine. API toetab sisseehitatud mitut tekstist-tekstiks suurt keelemudelit, mis võimaldab rakendada uusimaid seadmesiseseid generatiivse tehisintellekti mudeleid Androidi rakendustes.

Google AI Edge Torch on Python'i teek, mis toetab PyTorch mudelite konverteerimist .tflite formaati, mida saab seejärel käitada TensorFlow Lite'i ja MediaPipe'iga. See võimaldab luua rakendusi Androidi, iOS-i ja IoT jaoks, mis suudavad mudeleid täielikult seadmesiseselt käitada. AI Edge Torch pakub laialdast CPU tuge, esialgse GPU ja NPU toega. AI Edge Torch püüab tihedalt integreeruda PyTorchiga, tuginedes torch.export() funktsioonile ja pakkudes head katvust Core ATen operaatoritele.

## **🪬 Juhend**

### **🔥 Microsoft Phi-3.5 tflite formaati konverteerimine**

0. See näidis on mõeldud Android 14+ jaoks.

1. Installige Python 3.10.12.

***Soovitus:*** kasutage conda't oma Python'i keskkonna installimiseks.

2. Ubuntu 20.04 / 22.04 (palun keskenduge [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch)).

***Soovitus:*** kasutage Azure Linux VM-i või kolmanda osapoole pilve VM-i oma keskkonna loomiseks.

3. Minge oma Linuxi bash'i ja installige Python'i teek.

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Laadige alla Microsoft-3.5-Instruct Hugging Face'ist.

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Konverteerige Microsoft Phi-3.5 tflite formaati.

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```


### **🔥 Microsoft Phi-3.5 konverteerimine Android Mediapipe Bundle'iks**

Installige esmalt mediapipe.

```bash

pip install mediapipe

```

käivitage see kood [oma märkmikus](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb).

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


### **🔥 Mudeli üleslaadimine adb push käsuga Androidi seadme kausta**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Androidi koodi käivitamine**

![demo](../../../../../../imgs/02/android-tf/demo.png)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.