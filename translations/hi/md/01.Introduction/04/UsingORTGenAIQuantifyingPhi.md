# **onnxruntime के लिए Generative AI एक्सटेंशंस का उपयोग करते हुए Phi परिवार का क्वांटाइजेशन**

## **onnxruntime के लिए Generative AI एक्सटेंशंस क्या हैं**

यह एक्सटेंशंस आपको ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) के साथ जनरेटिव AI चलाने में मदद करता है। यह ONNX मॉडल के लिए जनरेटिव AI लूप प्रदान करता है, जिसमें ONNX Runtime के साथ इनफेरेंस, लॉजिट्स प्रोसेसिंग, सर्च और सैंपलिंग, और KV कैश प्रबंधन शामिल हैं। डेवलपर्स उच्च स्तरीय generate() मेथड को कॉल कर सकते हैं, या मॉडल के प्रत्येक इटरेशन को लूप में चला सकते हैं, एक बार में एक टोकन जनरेट करते हुए, और ऑप्शनली लूप के अंदर जनरेशन पैरामीटर अपडेट कर सकते हैं। इसमें टोकन अनुक्रम उत्पन्न करने के लिए ग्रीडी/बीम सर्च और TopP, TopK सैंपलिंग के लिए सपोर्ट है और दोहराव दंड जैसे अंतर्निर्मित लॉजिट्स प्रोसेसिंग शामिल है। आप कस्टम स्कोरिंग भी आसानी से जोड़ सकते हैं।

आवेदन स्तर पर, आप C++/ C# / Python का उपयोग करके Generative AI एक्सटेंशंस का उपयोग करके एप्लिकेशन बना सकते हैं। मॉडल स्तर पर, आप इसे फाइन-ट्यून किए गए मॉडल मर्ज करने और संबंधित मात्रात्मक डिप्लॉयमेंट कार्य करने के लिए उपयोग कर सकते हैं।


## **onnxruntime के लिए Generative AI एक्सटेंशंस की मदद से Phi-3.5 का क्वांटाइजेशन**

### **समर्थित मॉडल**

onnxruntime के लिए Generative AI एक्सटेंशंस Microsoft Phi, Google Gemma, Mistral, Meta LLaMA के क्वांटाइजेशन कन्वर्शन का समर्थन करते हैं।


### **onnxruntime के लिए Generative AI एक्सटेंशंस में मॉडल बिल्डर**

मॉडल बिल्डर से ONNX Runtime generate() API के साथ चलने वाले अनुकूलित और क्वांटाइज्ड ONNX मॉडल बनाना बहुत तेज़ होता है।

मॉडल बिल्डर के माध्यम से, आप मॉडल को INT4, INT8, FP16, FP32 में क्वांटाइज कर सकते हैं, और CPU, CUDA, DirectML, Mobile आदि जैसे विभिन्न हार्डवेयर अकसेलेरेशन तरीकों को संयोजित कर सकते हैं।

मॉडल बिल्डर इस्तेमाल करने के लिए आपको इंस्टॉल करना होगा

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

इंस्टॉलेशन के बाद, आप टर्मिनल से मॉडल बिल्डर स्क्रिप्ट चला कर मॉडल फॉर्मेट और क्वांटाइजेशन कन्वर्शन कर सकते हैं।


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

प्रासंगिक पैरामीटर समझें

1. **model_name** यह Hugging face पर मॉडल है, जैसे microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct आदि। यह उस पाथ भी हो सकता है जहां आप मॉडल स्टोर करते हैं

2. **path_to_output_folder** क्वांटाइज्ड कन्वर्शन सेव पाथ

3. **execution_provider** विभिन्न हार्डवेयर अकसेलेरेशन सपोर्ट, जैसे cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** हम मॉडल को Hugging face से डाउनलोड कर स्थानीय रूप से कैश करते हैं




***नोट：*** <ul>हालांकि onnxruntime के लिए Generative AI एक्सटेंशंस पूर्वावलोकन में हैं, इन्हें Microsoft Olive में शामिल किया गया है, और आप Microsoft Olive के माध्यम से onnxruntime के Generative AI एक्सटेंशंस मॉडल बिल्डर फ़ंक्शंस को कॉल भी कर सकते हैं।</ul>

## **Phi-3.5 क्वांटाइजेशन के लिए मॉडल बिल्डर का उपयोग कैसे करें**

मॉडल बिल्डर अब Phi-3.5 Instruct और Phi-3.5-Vision के लिए ONNX मॉडल क्वांटाइजेशन का समर्थन करता है

### **Phi-3.5-Instruct**


**क्वांटाइज्ड INT 4 का CPU तेज़ कन्वर्शन**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**क्वांटाइज्ड INT 4 का CUDA तेज़ कन्वर्शन**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. टर्मिनल में वातावरण सेट करें

```bash

mkdir models

cd models 

```

2. models फोल्डर में microsoft/Phi-3.5-vision-instruct डाउनलोड करें
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. कृपया ये फाइलें अपने Phi-3.5-vision-instruct फोल्डर में डाउनलोड करें

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. इस फाइल को models फोल्डर में डाउनलोड करें
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. टर्मिनल पर जाएं

    FP32 के साथ ONNX सपोर्ट को कन्वर्ट करें


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **नोट：**

1. मॉडल बिल्डर वर्तमान में Phi-3.5-Instruct और Phi-3.5-Vision के कन्वर्शन का समर्थन करता है, लेकिन Phi-3.5-MoE का नहीं

2. ONNX के क्वांटाइज्ड मॉडल का उपयोग आप onnxruntime के लिए Generative AI एक्सटेंशंस SDK के माध्यम से कर सकते हैं

3. हमें अधिक जिम्मेदार AI पर विचार करना होगा, इसलिए मॉडल क्वांटाइजेशन कन्वर्शन के बाद, यह अधिक प्रभावी परिणाम परीक्षण की सलाह दी जाती है

4. CPU INT4 मॉडल को क्वांटाइज़ करके, हम इसे Edge Device पर डिप्लॉय कर सकते हैं, जिसके उपयोग के बेहतर परिदृश्य हैं, इसलिए हमने Phi-3.5-Instruct का INT 4 के आसपास पूरा किया है


## **संसाधन**

1. onnxruntime के लिए Generative AI एक्सटेंशंस के बारे में अधिक जानें [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. onnxruntime के लिए Generative AI एक्सटेंशंस GitHub रिपॉजिटरी [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->