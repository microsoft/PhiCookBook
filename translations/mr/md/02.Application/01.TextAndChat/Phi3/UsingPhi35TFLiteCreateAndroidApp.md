<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:47:47+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "mr"
}
-->
# **Microsoft Phi-3.5 tflite वापरून Android अॅप तयार करणे**

हा Microsoft Phi-3.5 tflite मॉडेल्स वापरून तयार केलेला Android सॅम्पल आहे.

## **📚 माहिती**

Android LLM Inference API तुम्हाला Android अॅप्ससाठी मोठ्या भाषा मॉडेल्स (LLMs) पूर्णपणे डिव्हाइसवर चालवण्याची सुविधा देते, ज्याचा वापर तुम्ही विविध कामांसाठी करू शकता, जसे की मजकूर तयार करणे, नैसर्गिक भाषेत माहिती मिळवणे, आणि दस्तऐवजांचे सारांश बनवणे. हा टास्क अनेक टेक्स्ट-टू-टेक्स्ट मोठ्या भाषा मॉडेल्ससाठी इनबिल्ट सपोर्ट पुरवतो, त्यामुळे तुम्ही तुमच्या Android अॅप्समध्ये नवीनतम ऑन-डिव्हाइस जनरेटिव्ह AI मॉडेल्स वापरू शकता.

Google AI Edge Torch ही एक Python लायब्ररी आहे जी PyTorch मॉडेल्सना .tflite फॉरमॅटमध्ये कन्व्हर्ट करण्यास मदत करते, ज्याला नंतर TensorFlow Lite आणि MediaPipe सह चालवता येते. यामुळे Android, iOS आणि IoT साठी असे अॅप्लिकेशन्स तयार करता येतात जे मॉडेल्स पूर्णपणे डिव्हाइसवर चालवू शकतात. AI Edge Torch CPU चा विस्तृत सपोर्ट देते, तसेच सुरुवातीचा GPU आणि NPU सपोर्टही आहे. AI Edge Torch PyTorch सोबत जवळून इंटिग्रेट होण्याचा प्रयत्न करते, torch.export() वर आधारित असून Core ATen ऑपरेटरचा चांगला कव्हरेज देते.

## **🪬 मार्गदर्शक**

### **🔥 Microsoft Phi-3.5 चे tflite मध्ये कन्व्हर्शन**

0. हा सॅम्पल Android 14+ साठी आहे

1. Python 3.10.12 इन्स्टॉल करा

***सूचना:*** Python environment साठी conda वापरण्याचा सल्ला दिला जातो

2. Ubuntu 20.04 / 22.04 (कृपया [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) वर लक्ष ठेवा)

***सूचना:*** Azure Linux VM किंवा तृतीय पक्ष क्लाउड VM वापरून environment तयार करा

3. Linux bash मध्ये जा आणि Python लायब्ररी इन्स्टॉल करा

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging face वरून Microsoft-3.5-Instruct डाउनलोड करा

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5 चे tflite मध्ये कन्व्हर्शन करा

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```


### **🔥 Microsoft Phi-3.5 चे Android Mediapipe Bundle मध्ये कन्व्हर्शन**

कृपया आधी mediapipe इन्स्टॉल करा

```bash

pip install mediapipe

```

हा कोड [तुमच्या notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) मध्ये चालवा

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


### **🔥 adb वापरून तुमचा टास्क मॉडेल Android डिव्हाइसच्या पाथवर पाठवा**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 तुमचा Android कोड चालवा**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.mr.png)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, परंतु कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद शिफारस केली जाते. या अनुवादाच्या वापरामुळे होणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थ लावण्याबद्दल आम्ही जबाबदार नाही.