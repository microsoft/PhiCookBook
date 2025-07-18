<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-07-16T22:24:40+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "sw"
}
-->
## **Jinsi ya kutumia Model Builder kuquantize Phi-3.5**

Model Builder sasa inaunga mkono kuquantize modeli za ONNX za Phi-3.5 Instruct na Phi-3.5-Vision

### **Phi-3.5-Instruct**

**Ubadilishaji wa kuharakishwa na CPU wa INT4 iliyopimwa**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Ubadilishaji wa kuharakishwa na CUDA wa INT4 iliyopimwa**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Weka mazingira kwenye terminal

```bash

mkdir models

cd models 

```

2. Pakua microsoft/Phi-3.5-vision-instruct kwenye folda ya models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Tafadhali pakua faili hizi kwenye folda yako ya Phi-3.5-vision-instruct

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Pakua faili hii kwenye folda ya models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Nenda kwenye terminal

    Badilisha ONNX kuunga mkono FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Kumbuka：**

1. Model Builder kwa sasa inaunga mkono ubadilishaji wa Phi-3.5-Instruct na Phi-3.5-Vision, lakini si Phi-3.5-MoE

2. Ili kutumia modeli iliyopimwa ya ONNX, unaweza kuitumia kupitia Generative AI extensions for onnxruntime SDK

3. Tunahitaji kuzingatia AI yenye uwajibikaji zaidi, hivyo baada ya ubadilishaji wa kuquantize modeli, inashauriwa kufanya majaribio ya matokeo yenye ufanisi zaidi

4. Kwa kuquantize modeli ya CPU INT4, tunaweza kuipeleka kwenye Edge Device, ambayo ina mazingira bora ya matumizi, hivyo tumemaliza Phi-3.5-Instruct kwa INT4

## **Rasilimali**

1. Jifunze zaidi kuhusu Generative AI extensions for onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub Repo [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.