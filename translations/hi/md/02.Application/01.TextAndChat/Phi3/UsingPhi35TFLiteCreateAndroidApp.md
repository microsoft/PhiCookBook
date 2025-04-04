<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2faa9c6d61c5aa2708aec02a39ec464b",
  "translation_date": "2025-04-04T18:23:55+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "hi"
}
-->
# **Microsoft Phi-3.5 tflite का उपयोग करके Android ऐप बनाना**

यह Microsoft Phi-3.5 tflite मॉडल का उपयोग करने वाला एक Android सैंपल है।

## **📚 ज्ञान**

Android LLM Inference API आपको Android एप्लिकेशन के लिए बड़े भाषा मॉडल (LLMs) को पूरी तरह से ऑन-डिवाइस चलाने की सुविधा देता है। इसका उपयोग करके आप कई प्रकार के कार्य कर सकते हैं, जैसे टेक्स्ट जनरेट करना, प्राकृतिक भाषा में जानकारी प्राप्त करना, और दस्तावेज़ों का सारांश बनाना। यह टास्क कई टेक्स्ट-टू-टेक्स्ट बड़े भाषा मॉडल्स के लिए बिल्ट-इन सपोर्ट प्रदान करता है, जिससे आप नवीनतम ऑन-डिवाइस जनरेटिव AI मॉडल्स को अपने Android ऐप्स में लागू कर सकते हैं।

Google AI Edge Torch एक पायथन लाइब्रेरी है जो PyTorch मॉडल्स को .tflite फॉर्मेट में बदलने का समर्थन करती है। इसके बाद इन मॉडल्स को TensorFlow Lite और MediaPipe के साथ चलाया जा सकता है। यह Android, iOS और IoT के लिए ऐसे एप्लिकेशन सक्षम करता है जो मॉडल्स को पूरी तरह से ऑन-डिवाइस चला सकते हैं। AI Edge Torch व्यापक CPU कवरेज प्रदान करता है, और प्रारंभिक GPU और NPU समर्थन के साथ आता है। AI Edge Torch PyTorch के साथ गहराई से इंटीग्रेट करने का प्रयास करता है, torch.export() पर आधारित है और Core ATen ऑपरेटर्स का अच्छा कवरेज प्रदान करता है।

## **🪬 दिशानिर्देश**

### **🔥 Microsoft Phi-3.5 को tflite में बदलने के लिए**

0. यह सैंपल Android 14+ के लिए है

1. Python 3.10.12 इंस्टॉल करें

***सुझाव:*** अपनी Python एन्वायरनमेंट को स्थापित करने के लिए conda का उपयोग करें

2. Ubuntu 20.04 / 22.04 (कृपया [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) पर ध्यान दें)

***सुझाव:*** Azure Linux VM या किसी 3rd पार्टी क्लाउड VM का उपयोग करके अपना एन्वायरनमेंट बनाएं

3. अपने Linux bash पर जाएं और Python लाइब्रेरी इंस्टॉल करें

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging Face से Microsoft-3.5-Instruct डाउनलोड करें

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5 को tflite में बदलें

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5 को Android Mediapipe Bundle में बदलें**

कृपया पहले Mediapipe इंस्टॉल करें

```bash

pip install mediapipe

```

इस कोड को [अपने नोटबुक](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) में चलाएं

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

### **🔥 अपने Android डिवाइस के पाथ में adb push टास्क मॉडल का उपयोग करें**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 अपना Android कोड चलाएं**

![डेमो](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.hi.png)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या गलतियां हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की अनुशंसा की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।