<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-05-09T14:22:45+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "mr"
}
-->
## **Phi-3.5 चे क्वांटायझेशन करण्यासाठी Model Builder कसा वापरायचा**

Model Builder आता Phi-3.5 Instruct आणि Phi-3.5-Vision साठी ONNX मॉडेल क्वांटायझेशनला सपोर्ट करतो.

### **Phi-3.5-Instruct**

**CPU वर INT4 क्वांटायझेशनसाठी जलद रूपांतरण**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA वर INT4 क्वांटायझेशनसाठी जलद रूपांतरण**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. टर्मिनलमध्ये पर्यावरण सेट करा

```bash

mkdir models

cd models 

```

2. microsoft/Phi-3.5-vision-instruct मॉडेल models फोल्डरमध्ये डाउनलोड करा  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. खालील फाइल्स आपल्या Phi-3.5-vision-instruct फोल्डरमध्ये डाउनलोड करा

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. ही फाइल models फोल्डरमध्ये डाउनलोड करा  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. टर्मिनलमध्ये जा

    FP32 सह ONNX सपोर्ट रूपांतरण करा

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **टीप:**

1. Model Builder सध्या Phi-3.5-Instruct आणि Phi-3.5-Vision चे रूपांतरण सपोर्ट करतो, पण Phi-3.5-MoE साठी नाही.

2. ONNX चे क्वांटायझ्ड मॉडेल Generative AI extensions for onnxruntime SDK द्वारे वापरता येऊ शकते.

3. जबाबदार AI चा विचार करता, मॉडेल क्वांटायझेशन नंतर अधिक प्रभावी निकालांची चाचणी करणे शिफारसीय आहे.

4. CPU INT4 मॉडेल क्वांटायझेशनमुळे ते Edge Device वर डिप्लॉय करता येते, ज्यामुळे अधिक चांगल्या अॅप्लिकेशन सीनारियोसना मदत होते; म्हणून Phi-3.5-Instruct चे INT4 क्वांटायझेशन पूर्ण झाले आहे.

## **संसाधने**

1. Generative AI extensions for onnxruntime बद्दल अधिक जाणून घ्या [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अपूर्णता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाच्या माहिती साठी व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीसाठी आम्ही जबाबदार नाही.