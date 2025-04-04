<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aed7639909ebbd1960507880cff2ae4c",
  "translation_date": "2025-04-04T17:15:51+00:00",
  "source_file": "code\\04.Finetuning\\olive-ort-example\\README.md",
  "language_code": "hi"
}
-->
# Olive का उपयोग करके Phi3 को फाइन-ट्यून करें

इस उदाहरण में, आप Olive का उपयोग करके निम्नलिखित करेंगे:

1. LoRA एडेप्टर को फाइन-ट्यून करें ताकि वाक्यांशों को Sad, Joy, Fear, Surprise में वर्गीकृत किया जा सके।
1. एडेप्टर वज़न को बेस मॉडल में मर्ज करें।
1. मॉडल को `int4` में ऑप्टिमाइज़ और क्वांटाइज़ करें।

हम आपको यह भी दिखाएंगे कि ONNX Runtime (ORT) Generate API का उपयोग करके फाइन-ट्यून किए गए मॉडल का इन्फ़रेंस कैसे करें।

> **⚠️ फाइन-ट्यूनिंग के लिए, आपके पास उपयुक्त GPU उपलब्ध होना चाहिए - उदाहरण के लिए, A10, V100, A100।**

## 💾 इंस्टॉल

एक नया Python वर्चुअल एन्वायरनमेंट बनाएं (उदाहरण के लिए, `conda` का उपयोग करके):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

इसके बाद, Olive और फाइन-ट्यूनिंग वर्कफ़्लो के लिए आवश्यक डिपेंडेंसी इंस्टॉल करें:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive का उपयोग करके Phi3 को फाइन-ट्यून करें
[Olive कॉन्फ़िगरेशन फ़ाइल](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) में एक *वर्कफ़्लो* है जिसमें निम्नलिखित *पास* शामिल हैं:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

इस वर्कफ़्लो का उच्च-स्तरीय उद्देश्य है:

1. Phi3 को फाइन-ट्यून करें (150 स्टेप्स के लिए, जिसे आप संशोधित कर सकते हैं) [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) डेटा का उपयोग करके।
1. LoRA एडेप्टर वज़न को बेस मॉडल में मर्ज करें। इससे आपको ONNX फॉर्मेट में एक सिंगल मॉडल आर्टिफैक्ट मिलेगा।
1. Model Builder मॉडल को ONNX रनटाइम के लिए ऑप्टिमाइज़ करेगा *और* मॉडल को `int4` में क्वांटाइज़ करेगा।

वर्कफ़्लो को चलाने के लिए, निम्नलिखित कमांड चलाएं:

```bash
olive run --config phrase-classification.json
```

जब Olive प्रक्रिया पूरी कर लेगा, तो आपका ऑप्टिमाइज़ किया गया `int4` फाइन-ट्यून किया हुआ Phi3 मॉडल इस स्थान पर उपलब्ध होगा: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 अपने एप्लिकेशन में फाइन-ट्यून किए गए Phi3 को इंटीग्रेट करें 

एप्लिकेशन चलाने के लिए:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

इस प्रतिक्रिया में वाक्यांश का एक सिंगल वर्ड वर्गीकरण होना चाहिए (Sad/Joy/Fear/Surprise)।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल भाषा में लिखा गया दस्तावेज़ ही आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या व्याख्या के लिए हम जिम्मेदार नहीं हैं।