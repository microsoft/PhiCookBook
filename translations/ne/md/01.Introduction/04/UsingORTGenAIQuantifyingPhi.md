## **Model Builder प्रयोग गरेर Phi-3.5 लाई कसरी क्वान्टाइज गर्ने**

Model Builder अब Phi-3.5 Instruct र Phi-3.5-Vision का लागि ONNX मोडेल क्वान्टाइजेसन समर्थन गर्दछ।

### **Phi-3.5-Instruct**

**CPU द्वारा तीव्र गरिएको क्वान्टाइज्ड INT4 रूपान्तरण**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA द्वारा तीव्र गरिएको क्वान्टाइज्ड INT4 रूपान्तरण**

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

2. models फोल्डरमा microsoft/Phi-3.5-vision-instruct डाउनलोड गर्नुहोस्  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. यी फाइलहरू तपाईंको Phi-3.5-vision-instruct फोल्डरमा डाउनलोड गर्नुहोस्

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. models फोल्डरमा यो फाइल डाउनलोड गर्नुहोस्  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. टर्मिनलमा जानुहोस्

    FP32 को साथ ONNX समर्थन रूपान्तरण गर्नुहोस्

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **ध्यान दिनुहोस्：**

1. Model Builder हाल Phi-3.5-Instruct र Phi-3.5-Vision को रूपान्तरण समर्थन गर्दछ, तर Phi-3.5-MoE लाई समर्थन गर्दैन।

2. ONNX को क्वान्टाइज्ड मोडेल प्रयोग गर्न, तपाईं यसलाई Generative AI extensions for onnxruntime SDK मार्फत प्रयोग गर्न सक्नुहुन्छ।

3. हामीले जिम्मेवार AI को बारेमा थप विचार गर्न आवश्यक छ, त्यसैले मोडेल क्वान्टाइजेसन रूपान्तरण पछि, थप प्रभावकारी परिणाम परीक्षण गर्न सिफारिस गरिन्छ।

4. CPU INT4 मोडेल क्वान्टाइज गरेर, हामी यसलाई Edge Device मा तैनाथ गर्न सक्छौं, जसले राम्रो अनुप्रयोग परिदृश्यहरू प्रदान गर्दछ, त्यसैले हामीले Phi-3.5-Instruct लाई INT4 वरिपरि पूरा गरेका छौं।

## **स्रोतहरू**

1. Generative AI extensions for onnxruntime बारे थप जान्न [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub रिपोजिटरी [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।