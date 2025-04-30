<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b96f9dc2389500e24a2c2c4debf30908",
  "translation_date": "2025-04-04T18:00:26+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingORTGenAIQuantifyingPhi.md",
  "language_code": "hi"
}
-->
# **Generative AI extensions for onnxruntime का उपयोग करके Phi परिवार को क्वांटाइज़ करना**

## **Generative AI extensions for onnxruntime क्या है**

ये एक्सटेंशन आपको ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) के साथ जनरेटिव AI चलाने में मदद करता है। यह ONNX मॉडल्स के लिए जनरेटिव AI लूप प्रदान करता है, जिसमें ONNX Runtime के साथ इनफेरेंस, लॉजिट्स प्रोसेसिंग, सर्च और सैंपलिंग, और KV कैश प्रबंधन शामिल हैं। डेवलपर्स हाई-लेवल generate() मेथड का उपयोग कर सकते हैं, या मॉडल के प्रत्येक इटरेशन को एक लूप में चला सकते हैं, एक समय में एक टोकन जनरेट करते हुए, और लूप के अंदर जनरेशन पैरामीटर को अपडेट कर सकते हैं। यह ग्रीडी/बीम सर्च और TopP, TopK सैंपलिंग का समर्थन करता है ताकि टोकन सीक्वेंस जनरेट किए जा सकें और बिल्ट-इन लॉजिट्स प्रोसेसिंग जैसे रिपीटेशन पेनल्टी का उपयोग किया जा सके। आप आसानी से कस्टम स्कोरिंग भी जोड़ सकते हैं।

एप्लिकेशन स्तर पर, आप Generative AI extensions for onnxruntime का उपयोग करके C++/C#/Python में एप्लिकेशन बना सकते हैं। मॉडल स्तर पर, आप इसका उपयोग फाइन-ट्यून किए गए मॉडल्स को मर्ज करने और संबंधित क्वांटिटेटिव डिप्लॉयमेंट कार्य करने के लिए कर सकते हैं। 

## **Generative AI extensions for onnxruntime का उपयोग करके Phi-3.5 को क्वांटाइज़ करना**

### **सपोर्टेड मॉडल्स**

Generative AI extensions for onnxruntime Microsoft Phi, Google Gemma, Mistral, Meta LLaMA के क्वांटाइजेशन कन्वर्ज़न का समर्थन करता है।

### **Generative AI extensions for onnxruntime में मॉडल बिल्डर**

मॉडल बिल्डर ONNX Runtime generate() API के साथ चलने वाले ऑप्टिमाइज़्ड और क्वांटाइज़्ड ONNX मॉडल्स को बनाने की प्रक्रिया को बहुत तेज करता है।

मॉडल बिल्डर के माध्यम से, आप मॉडल को INT4, INT8, FP16, FP32 में क्वांटाइज़ कर सकते हैं और CPU, CUDA, DirectML, Mobile आदि जैसे विभिन्न हार्डवेयर एक्सेलेरेशन तरीकों को जोड़ सकते हैं।

मॉडल बिल्डर का उपयोग करने के लिए आपको इसे इंस्टॉल करना होगा:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

इंस्टॉल करने के बाद, आप टर्मिनल से मॉडल बिल्डर स्क्रिप्ट चला सकते हैं ताकि मॉडल फॉर्मेट और क्वांटाइजेशन कन्वर्ज़न किया जा सके।

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

संबंधित पैरामीटर समझें:

1. **model_name** यह Hugging Face पर मॉडल है, जैसे microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct आदि। यह वह पथ भी हो सकता है जहां आप मॉडल को स्टोर करते हैं।

2. **path_to_output_folder** क्वांटाइज़्ड कन्वर्ज़न को सेव करने का पथ।

3. **execution_provider** विभिन्न हार्डवेयर एक्सेलेरेशन सपोर्ट, जैसे cpu, cuda, DirectML।

4. **cache_dir_to_save_hf_files** हम Hugging Face से मॉडल डाउनलोड करते हैं और इसे स्थानीय रूप से कैश करते हैं।

***नोट:*** 

## **Phi-3.5 को क्वांटाइज़ करने के लिए Model Builder का उपयोग कैसे करें**

मॉडल बिल्डर अब Phi-3.5 Instruct और Phi-3.5-Vision के लिए ONNX मॉडल क्वांटाइजेशन का समर्थन करता है।

### **Phi-3.5-Instruct**

**क्वांटाइज़्ड INT 4 का CPU एक्सेलेरेटेड कन्वर्ज़न**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**क्वांटाइज़्ड INT 4 का CUDA एक्सेलेरेटेड कन्वर्ज़न**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. टर्मिनल में वातावरण सेट करें:

```bash

mkdir models

cd models 

```

2. models फ़ोल्डर में microsoft/Phi-3.5-vision-instruct डाउनलोड करें:
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. कृपया इन फाइल्स को अपनी Phi-3.5-vision-instruct फ़ोल्डर में डाउनलोड करें:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. इस फाइल को models फ़ोल्डर में डाउनलोड करें:
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. टर्मिनल पर जाएं:

    ONNX सपोर्ट को FP32 के साथ कन्वर्ट करें:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **नोट:**

1. मॉडल बिल्डर फिलहाल Phi-3.5-Instruct और Phi-3.5-Vision का कन्वर्ज़न सपोर्ट करता है, लेकिन Phi-3.5-MoE का नहीं।

2. ONNX के क्वांटाइज़्ड मॉडल का उपयोग करने के लिए, आप इसे Generative AI extensions for onnxruntime SDK के माध्यम से उपयोग कर सकते हैं।

3. हमें अधिक जिम्मेदार AI पर विचार करना चाहिए, इसलिए मॉडल क्वांटाइजेशन कन्वर्ज़न के बाद, अधिक प्रभावी परिणाम परीक्षण करने की सिफारिश की जाती है।

4. CPU INT4 मॉडल को क्वांटाइज़ करके, हम इसे Edge Device पर डिप्लॉय कर सकते हैं, जिससे बेहतर एप्लिकेशन परिदृश्य मिलते हैं। इसलिए हमने Phi-3.5-Instruct को INT4 के आसपास पूरा किया है।

## **संसाधन**

1. Generative AI extensions for onnxruntime के बारे में अधिक जानें: [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime का GitHub Repo: [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़, जो इसकी मूल भाषा में है, को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की अनुशंसा की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।