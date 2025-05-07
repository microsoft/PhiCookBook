<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-05-07T14:53:09+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "ur"
}
-->
## **Phi-3.5 کو کوانٹائز کرنے کے لیے Model Builder کا استعمال کیسے کریں**

اب Model Builder Phi-3.5 Instruct اور Phi-3.5-Vision کے لیے ONNX ماڈل کو کوانٹائز کرنے کی حمایت کرتا ہے۔

### **Phi-3.5-Instruct**

**CPU کی مدد سے کوانٹائزڈ INT 4 کی تبدیلی**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**CUDA کی مدد سے کوانٹائزڈ INT 4 کی تبدیلی**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. ٹرمینل میں ماحول سیٹ کریں

```bash

mkdir models

cd models 

```

2. microsoft/Phi-3.5-vision-instruct کو models فولڈر میں ڈاؤن لوڈ کریں  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. براہ کرم یہ فائلیں اپنے Phi-3.5-vision-instruct فولڈر میں ڈاؤن لوڈ کریں

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. یہ فائل models فولڈر میں ڈاؤن لوڈ کریں  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ٹرمینل پر جائیں

    FP32 کے ساتھ ONNX سپورٹ کی تبدیلی کریں

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **نوٹ:**

1. Model Builder فی الحال Phi-3.5-Instruct اور Phi-3.5-Vision کی تبدیلی کی حمایت کرتا ہے، لیکن Phi-3.5-MoE کی نہیں۔

2. ONNX کے کوانٹائزڈ ماڈل کو استعمال کرنے کے لیے، آپ اسے Generative AI extensions for onnxruntime SDK کے ذریعے استعمال کر سکتے ہیں۔

3. ہمیں زیادہ ذمہ دار AI کے بارے میں سوچنا چاہیے، اس لیے ماڈل کی کوانٹائزیشن تبدیلی کے بعد مؤثر نتائج کے ٹیسٹ کرنے کی سفارش کی جاتی ہے۔

4. CPU INT4 ماڈل کو کوانٹائز کر کے، ہم اسے Edge Device پر تعینات کر سکتے ہیں، جس کے بہتر اطلاقی منظرنامے ہیں، اس لیے ہم نے Phi-3.5-Instruct کو INT 4 کے گرد مکمل کیا ہے۔

## **وسائل**

1. Generative AI extensions for onnxruntime کے بارے میں مزید جانیں  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime GitHub ریپو  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**دسclaimer**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار تراجم میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ذریعہ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ورانہ انسانی ترجمہ تجویز کیا جاتا ہے۔ ہم اس ترجمہ کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔