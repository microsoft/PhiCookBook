<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:02:20+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "hi"
}
-->
# Olive का उपयोग करके Phi3 को फाइन-ट्यून करें

इस उदाहरण में आप Olive का उपयोग करेंगे:

1. LoRA एडाप्टर को फाइन-ट्यून करना ताकि वाक्यांशों को Sad, Joy, Fear, Surprise में वर्गीकृत किया जा सके।
1. एडाप्टर वेट्स को बेस मॉडल में मर्ज करना।
1. मॉडल को `int4` में ऑप्टिमाइज़ और क्वांटाइज़ करना।

हम आपको यह भी दिखाएंगे कि ONNX Runtime (ORT) Generate API का उपयोग करके फाइन-ट्यून किए गए मॉडल से कैसे इनफेरेंस करें।

> **⚠️ फाइन-ट्यूनिंग के लिए, आपके पास उपयुक्त GPU होना चाहिए - जैसे कि A10, V100, A100।**

## 💾 इंस्टॉल करें

एक नया Python वर्चुअल एनवायरनमेंट बनाएं (उदाहरण के लिए, `conda` का उपयोग करके):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

इसके बाद, Olive और फाइन-ट्यूनिंग वर्कफ़्लो के लिए आवश्यक डिपेंडेंसीज़ इंस्टॉल करें:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive का उपयोग करके Phi3 को फाइन-ट्यून करें
[Olive कॉन्फ़िगरेशन फ़ाइल](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) में एक *वर्कफ़्लो* है जिसमें निम्नलिखित *पास* शामिल हैं:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

उच्च स्तर पर, यह वर्कफ़्लो निम्न करेगा:

1. Phi3 को फाइन-ट्यून करना (150 स्टेप्स के लिए, जिसे आप बदल सकते हैं) [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) डेटा का उपयोग करके।
1. LoRA एडाप्टर वेट्स को बेस मॉडल में मर्ज करना। इससे आपको ONNX फॉर्मेट में एक सिंगल मॉडल आर्टिफैक्ट मिलेगा।
1. Model Builder मॉडल को ONNX रनटाइम के लिए ऑप्टिमाइज़ करेगा *और* मॉडल को `int4` में क्वांटाइज़ करेगा।

वर्कफ़्लो को चलाने के लिए, निम्न कमांड चलाएं:

```bash
olive run --config phrase-classification.json
```

जब Olive पूरा हो जाएगा, तो आपका ऑप्टिमाइज़्ड `int4` फाइन-ट्यून किया गया Phi3 मॉडल इस लोकेशन पर उपलब्ध होगा: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`।

## 🧑‍💻 फाइन-ट्यून किए गए Phi3 को अपने एप्लिकेशन में इंटीग्रेट करें

ऐप चलाने के लिए:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

यह प्रतिक्रिया वाक्यांश का एक शब्द वर्गीकरण होगी (Sad/Joy/Fear/Surprise)।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।