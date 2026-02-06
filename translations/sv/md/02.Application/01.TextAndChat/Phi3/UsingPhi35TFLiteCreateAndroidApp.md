# **Använda Microsoft Phi-3.5 tflite för att skapa Android-app**

Detta är ett Android-exempel som använder Microsoft Phi-3.5 tflite-modeller.

## **📚 Kunskap**

Android LLM Inference API låter dig köra stora språkmodeller (LLMs) helt på enheten för Android-appar, vilket du kan använda för att utföra en mängd olika uppgifter, som att generera text, hämta information i naturligt språk och sammanfatta dokument. Uppgiften har inbyggt stöd för flera text-till-text stora språkmodeller, så att du kan använda de senaste generativa AI-modellerna direkt på enheten i dina Android-appar.

Googld AI Edge Torch är ett Python-bibliotek som stödjer konvertering av PyTorch-modeller till .tflite-format, vilket sedan kan köras med TensorFlow Lite och MediaPipe. Detta möjliggör appar för Android, iOS och IoT som kan köra modeller helt på enheten. AI Edge Torch erbjuder bred CPU-täckning, med initialt stöd för GPU och NPU. AI Edge Torch strävar efter att integreras nära med PyTorch, bygger på torch.export() och ger bra täckning av Core ATen-operatorer.

## **🪬 Riktlinje**

### **🔥 Konvertera Microsoft Phi-3.5 till tflite-stöd**

0. Detta exempel är för Android 14+

1. Installera Python 3.10.12

***Förslag:*** använd conda för att installera din Python-miljö

2. Ubuntu 20.04 / 22.04 (fokusera på [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Förslag:*** Använd Azure Linux VM eller tredjeparts moln-vm för att skapa din miljö

3. Gå till din Linux bash för att installera Python-biblioteket

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Ladda ner Microsoft-3.5-Instruct från Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Konvertera Microsoft Phi-3.5 till tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Konvertera Microsoft Phi-3.5 till Android Mediapipe Bundle**

vänligen installera mediapipe först

```bash

pip install mediapipe

```

kör denna kod i [din notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Använd adb push för att överföra task-modellen till din Android-enhets sökväg**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Köra din Android-kod**

![demo](../../../../../../translated_images/sv/demo.06d5a4246f057d1b.webp)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.