# **onnxruntime का लागि Generative AI एक्सटेन्सनहरू प्रयोग गरेर Phi परिवारलाई गुणांकन गर्ने**

## **onnxruntime का लागि Generative AI एक्सटेन्सनहरू के हुन्**

यो एक्सटेन्सनहरूले तपाईंलाई ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) सँग generative AI चलाउन मद्दत गर्छ। यसले ONNX मोडेलहरूको लागि generative AI लूप प्रदान गर्दछ, जसमा ONNX Runtime सँग inference, logits प्रक्रिया, खोज र स्याम्पलिंग, र KV cache व्यवस्थापन समावेश छन्। विकासकर्ताहरूले उच्च स्तरको generate() विधि कल गर्न सक्छन्, वा मोडेलको प्रत्येक पुनरावृत्ति लूपमा चलाएर एक पटकमा एउटा टोकन उत्पन्न गर्न सक्छन्, र इच्छानुसार लूपभित्र उत्पादन प्यारामिटरहरू अद्यावधिक गर्न सक्छन्। यसले greedy/beam search र TopP, TopK स्याम्पलिंग समर्थन गर्दछ टोकन अनुक्रमहरू उत्पन्न गर्न र पुनरावृत्ति सजायहरू जस्तै अन्तर्निर्मित logits प्रक्रिया। तपाईं सजिलै अनुकूलन स्कोरिङ पनि थप्न सक्नुहुन्छ।

अनुप्रयोग स्तरमा, तपाईं Generative AI एक्सटेन्सनहरूलाई C++/ C# / Python प्रयोग गरेर अनुप्रयोगहरू निर्माण गर्न प्रयोग गर्न सक्नुहुन्छ। मोडेल स्तरमा, तपाईं यसलाई राम्रो गरी ट्यून गरिएका मोडेलहरू मर्ज गर्न र सम्बन्धित गुणात्मक परिनियोजन कार्य गर्न प्रयोग गर्न सक्नुहुन्छ।


## **onnxruntime का लागि Generative AI एक्सटेन्सनहरूसँग Phi-3.5 लाई गुणांकन गर्ने**

### **समर्थित मोडेलहरू**

onnxruntime का लागि Generative AI एक्सटेन्सनहरूले Microsoft Phi, Google Gemma, Mistral, Meta LLaMA को गुणांकन रूपान्तरण समर्थन गर्दछन्।


### **onnxruntime का लागि Generative AI एक्सटेन्सनहरूमा मोडेल बिल्डर**

मोडेल बिल्डरले ONNX Runtime generate() API सँग चल्ने अनुकूलित र गुणांकित ONNX मोडेलहरू बनाउन ठूलो छिटो बनाउँछ।

मोडेल बिल्डरमार्फत, तपाईं मोडेललाई INT4, INT8, FP16, FP32 मा गुणांक गर्न सक्नुहुन्छ र CPU, CUDA, DirectML, मोबाइल जस्ता विभिन्न हार्डवेयर एक्सेलेरेसन विधिहरू संयोजन गर्न सक्नुहुन्छ।

मोडेल बिल्डर प्रयोग गर्न तपाईंलाई स्थापना गर्न आवश्यक छ

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

स्थापना पछि, तपाईं मोडेल प्रारूप र गुणांकन रूपान्तरण प्रदर्शन गर्न टर्मिनलबाट मोडेल बिल्डर स्क्रिप्ट चलाउन सक्नुहुन्छ।


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

सम्बन्धित प्यारामिटरहरू बुझ्नुहोस्

1. **model_name** यो Hugging face मा भएको मोडेल हो, जस्तै microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, आदि। यो त्यहाँ मोडेल संग्रह गरिएको पथ पनि हुन सक्छ

2. **path_to_output_folder** गुणांकित रूपान्तरण बचत गर्ने पथ

3. **execution_provider** विभिन्न हार्डवेयर एक्सेलेरेसन समर्थन, जस्तै cpu, cuda, DirectML

4. **cache_dir_to_save_hf_files** हामी मोडेल Hugging face बाट डाउनलोड गर्छौं र स्थानीय रूपमा क्यास गर्छौं




***टिप्पणी：*** <ul>यद्यपि onnxruntime का लागि Generative AI एक्सटेन्सनहरू पूर्वावलोकनमा छन्, ती Microsoft Olive मा समावेश भइसकेका छन्, र तपाईं Generative AI एक्सटेन्सनहरूको मोडेल बिल्डर कार्यहरू Microsoft Olive मार्फत पनि कल गर्न सक्नुहुन्छ।</ul>

## **Phi-3.5 गुणांक गर्न मोडेल बिल्डर कसरी प्रयोग गर्ने**

मोडेल बिल्डर अहिले Phi-3.5 Instruct र Phi-3.5-Vision का लागि ONNX मोडेल गुणांकन समर्थन गर्दछ

### **Phi-3.5-Instruct**


**गुणांकित INT 4 को CPU एक्सेलेरेसन रूपान्तरण**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**गुणांकित INT 4 को CUDA एक्सेलेरेसन रूपान्तरण**

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

3. कृपया यी फाइलहरू तपाईंको Phi-3.5-vision-instruct फोल्डरमा डाउनलोड गर्नुहोस्

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. models फोल्डरमा यो फाइल डाउनलोड गर्नुहोस्
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. टर्मिनलमा जानुहोस्

    FP32 सँग ONNX समर्थन रूपान्तरण गर्नुहोस्


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **टिप्पणी：**

1. मोडेल बिल्डर हाल Phi-3.5-Instruct र Phi-3.5-Vision को रूपान्तरण समर्थन गर्दछ, तर Phi-3.5-MoE होइन

2. ONNX को गुणांकित मोडेललाई तपाईं Generative AI एक्सटेन्सनहरूका माध्यमबाट प्रयोग गर्न सक्नुहुन्छ

3. हामीलाई अधिक जिम्मेवार AI विचार गर्न आवश्यक छ, त्यसैले मोडेल गुणांकन रूपान्तरण पछि थप प्रभावकारी परिणाम परीक्षण गर्नु सिफारिस गरिन्छ

4. CPU INT4 मोडेल गुणांकन गरेर हामी यसलाई Edge Device मा परिनियोजन गर्न सक्छौं जुन राम्रो अनुप्रयोग परिदृश्यहरूमा छ, त्यसैले हामीले Phi-3.5-Instruct लाई INT 4 वरिपरि पूरा गरेका छौं


## **स्रोतहरू**

1. onnxruntime का लागि Generative AI एक्सटेन्सनहरू बारे थप जान्न [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. onnxruntime का लागि Generative AI एक्सटेन्सनहरू GitHub रिपोजिटरी [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->