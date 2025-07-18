<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-07-16T22:18:19+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "mr"
}
-->
## **Phi-3.5 चे क्वांटायझेशन करण्यासाठी Model Builder कसा वापरायचा**

Model Builder आता Phi-3.5 Instruct आणि Phi-3.5-Vision साठी ONNX मॉडेल क्वांटायझेशनला समर्थन देतो.

### **Phi-3.5-Instruct**

**CPU द्वारे क्वांटाइज्ड INT4 चे जलद रूपांतरण**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA द्वारे क्वांटाइज्ड INT4 चे जलद रूपांतरण**

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

2. microsoft/Phi-3.5-vision-instruct मॉडेल फोल्डरमध्ये डाउनलोड करा  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. कृपया खालील फाइल्स आपल्या Phi-3.5-vision-instruct फोल्डरमध्ये डाउनलोड करा

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. ही फाइल models फोल्डरमध्ये डाउनलोड करा  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. टर्मिनलमध्ये जा

    FP32 सह ONNX समर्थन रूपांतरण करा

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **टीप：**

1. Model Builder सध्या Phi-3.5-Instruct आणि Phi-3.5-Vision चे रूपांतरण समर्थित करतो, पण Phi-3.5-MoE चे नाही.

2. ONNX चे क्वांटाइज्ड मॉडेल वापरण्यासाठी, तुम्ही Generative AI extensions for onnxruntime SDK वापरू शकता.

3. अधिक जबाबदार AI साठी, मॉडेल क्वांटायझेशन नंतर अधिक प्रभावी निकालांची चाचणी करणे शिफारसीय आहे.

4. CPU INT4 मॉडेल क्वांटायझेशन करून, आपण ते Edge Device वर तैनात करू शकतो, ज्यामुळे अधिक चांगले अनुप्रयोग परिस्थिती निर्माण होतात; म्हणून Phi-3.5-Instruct साठी INT4 चा वापर पूर्ण केला आहे.

## **संसाधने**

1. Generative AI extensions for onnxruntime बद्दल अधिक जाणून घ्या [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub रेपो [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.