## **Model Builder का उपयोग करके Phi-3.5 को क्वांटाइज़ कैसे करें**

Model Builder अब Phi-3.5 Instruct और Phi-3.5-Vision के लिए ONNX मॉडल क्वांटाइज़ेशन का समर्थन करता है।

### **Phi-3.5-Instruct**

**क्वांटाइज़्ड INT4 का CPU त्वरित रूपांतरण**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**क्वांटाइज़्ड INT4 का CUDA त्वरित रूपांतरण**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. टर्मिनल में पर्यावरण सेट करें

```bash

mkdir models

cd models 

```

2. models फ़ोल्डर में microsoft/Phi-3.5-vision-instruct डाउनलोड करें  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. कृपया ये फाइलें अपने Phi-3.5-vision-instruct फ़ोल्डर में डाउनलोड करें

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. models फ़ोल्डर में यह फाइल डाउनलोड करें  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. टर्मिनल पर जाएं

    FP32 के साथ ONNX सपोर्ट को कन्वर्ट करें

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **ध्यान दें：**

1. Model Builder वर्तमान में Phi-3.5-Instruct और Phi-3.5-Vision के रूपांतरण का समर्थन करता है, लेकिन Phi-3.5-MoE का नहीं करता।

2. ONNX के क्वांटाइज़्ड मॉडल का उपयोग Generative AI extensions for onnxruntime SDK के माध्यम से किया जा सकता है।

3. हमें अधिक जिम्मेदार AI पर विचार करना चाहिए, इसलिए मॉडल क्वांटाइज़ेशन के बाद अधिक प्रभावी परिणाम परीक्षण करने की सलाह दी जाती है।

4. CPU INT4 मॉडल को क्वांटाइज़ करके, हम इसे Edge Device पर तैनात कर सकते हैं, जो बेहतर अनुप्रयोग परिदृश्य प्रदान करता है, इसलिए हमने Phi-3.5-Instruct को INT4 के आसपास पूरा किया है।

## **संसाधन**

1. Generative AI extensions for onnxruntime के बारे में अधिक जानें [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub रिपॉजिटरी [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।