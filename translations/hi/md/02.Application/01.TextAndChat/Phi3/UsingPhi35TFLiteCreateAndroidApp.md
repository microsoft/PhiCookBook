<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:51:05+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "hi"
}
-->
# **Microsoft Phi-3.5 tflite का उपयोग करके Android ऐप बनाना**

यह Microsoft Phi-3.5 tflite मॉडल्स का उपयोग करते हुए एक Android सैंपल है।

## **📚 ज्ञान**

Android LLM Inference API आपको Android ऐप्स के लिए बड़े भाषा मॉडल (LLMs) को पूरी तरह से डिवाइस पर चलाने की सुविधा देता है, जिसका उपयोग आप टेक्स्ट जनरेट करने, प्राकृतिक भाषा में जानकारी प्राप्त करने, और दस्तावेज़ों का सारांश बनाने जैसे कई कार्यों के लिए कर सकते हैं। यह टास्क कई टेक्स्ट-टू-टेक्स्ट बड़े भाषा मॉडलों के लिए बिल्ट-इन सपोर्ट प्रदान करता है, जिससे आप अपने Android ऐप्स में नवीनतम ऑन-डिवाइस जनरेटिव AI मॉडल्स लागू कर सकते हैं।

Google AI Edge Torch एक पायथन लाइब्रेरी है जो PyTorch मॉडल्स को .tflite फॉर्मेट में कन्वर्ट करने का समर्थन करती है, जिसे बाद में TensorFlow Lite और MediaPipe के साथ चलाया जा सकता है। यह Android, iOS और IoT के लिए ऐसे ऐप्लिकेशन सक्षम बनाता है जो मॉडल्स को पूरी तरह से डिवाइस पर चला सकते हैं। AI Edge Torch व्यापक CPU सपोर्ट प्रदान करता है, साथ ही प्रारंभिक GPU और NPU सपोर्ट भी देता है। AI Edge Torch PyTorch के साथ गहरे एकीकरण का प्रयास करता है, torch.export() के ऊपर आधारित है और Core ATen ऑपरेटर्स का अच्छा कवरेज प्रदान करता है।

## **🪬 मार्गदर्शन**

### **🔥 Microsoft Phi-3.5 को tflite सपोर्ट में कन्वर्ट करना**

0. यह सैंपल Android 14+ के लिए है

1. Python 3.10.12 इंस्टॉल करें

***सुझाव:*** Python एन्वायरनमेंट स्थापित करने के लिए conda का उपयोग करें

2. Ubuntu 20.04 / 22.04 (कृपया [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) पर ध्यान दें)

***सुझाव:*** अपना एन्वायरनमेंट बनाने के लिए Azure Linux VM या किसी थर्ड पार्टी क्लाउड VM का उपयोग करें

3. अपने Linux bash में जाएं, और Python लाइब्रेरी इंस्टॉल करें

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

5. Microsoft Phi-3.5 को tflite में कन्वर्ट करें

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5 को Android Mediapipe Bundle में कन्वर्ट करना**

कृपया पहले mediapipe इंस्टॉल करें

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

### **🔥 adb push के जरिए मॉडल को अपने Android डिवाइस के पाथ पर भेजना**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 अपने Android कोड को चलाना**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1be99ffad0cbf22f4ac0c41530774d51ff903cfaa1d3cd3c8e.hi.png)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।