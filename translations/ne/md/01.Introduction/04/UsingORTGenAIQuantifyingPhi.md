<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-05-09T14:23:39+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "ne"
}
-->
## **Model Builder कसरी Phi-3.5 क्वान्टाइज गर्न प्रयोग गर्ने**

Model Builder अहिले Phi-3.5 Instruct र Phi-3.5-Vision का लागि ONNX मोडेल क्वान्टाइजेशनलाई समर्थन गर्छ।

### **Phi-3.5-Instruct**

**CPU एक्सेलेरेटेड क्वान्टाइज्ड INT4 मा रूपान्तरण**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA एक्सेलेरेटेड क्वान्टाइज्ड INT4 मा रूपान्तरण**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. टर्मिनलमा वातावरण सेट गर्नुहोस्

```bash

mkdir models

cd models 

```

2. microsoft/Phi-3.5-vision-instruct मोडेल फोल्डरमा डाउनलोड गर्नुहोस्  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. यी फाइलहरू तपाइँको Phi-3.5-vision-instruct फोल्डरमा डाउनलोड गर्नुहोस्

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. यो फाइल models फोल्डरमा डाउनलोड गर्नुहोस्  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. टर्मिनलमा जानुहोस्

    FP32 को साथ ONNX समर्थन रूपान्तरण गर्नुहोस्

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Note：**

1. Model Builder हाल Phi-3.5-Instruct र Phi-3.5-Vision को रूपान्तरण समर्थन गर्छ, तर Phi-3.5-MoE लाई समर्थन गर्दैन।

2. ONNX को क्वान्टाइज्ड मोडेल प्रयोग गर्न, Generative AI extensions for onnxruntime SDK मार्फत प्रयोग गर्न सकिन्छ।

3. हामीले जिम्मेवार AI लाई ध्यानमा राख्नुपर्छ, त्यसैले मोडेल क्वान्टाइजेशन पछि थप प्रभावकारी परिणाम परीक्षण गर्न सिफारिस गरिन्छ।

4. CPU INT4 मोडेल क्वान्टाइज गरेर हामी यसलाई Edge Device मा तैनाथ गर्न सक्छौं, जसले राम्रो एप्लिकेसन परिदृश्य प्रदान गर्छ, त्यसैले हामीले Phi-3.5-Instruct लाई INT4 वरिपरि पूरा गरिसकेका छौं।

## **स्रोतहरू**

1. Generative AI extensions for onnxruntime बारे थप जान्न [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) को प्रयोग गरी अनुवाद गरिएको हो। हामी सटीकता को प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धिहरू हुन सक्छन्। मूल दस्तावेज़ यसको स्वदेशी भाषामा आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।