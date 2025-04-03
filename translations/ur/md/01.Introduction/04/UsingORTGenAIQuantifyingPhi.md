<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b96f9dc2389500e24a2c2c4debf30908",
  "translation_date": "2025-04-03T07:05:21+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingORTGenAIQuantifyingPhi.md",
  "language_code": "ur"
}
-->
# **اونکس رن ٹائم کے لیے جنریٹیو AI ایکسٹینشنز کا استعمال کرتے ہوئے Phi فیملی کو کوانٹائز کرنا**

## **اونکس رن ٹائم کے لیے جنریٹیو AI ایکسٹینشنز کیا ہیں؟**

یہ ایکسٹینشنز آپ کو اونکس رن ٹائم کے ساتھ جنریٹیو AI چلانے میں مدد دیتی ہیں ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai))۔ یہ اونکس ماڈلز کے لیے جنریٹیو AI لوپ فراہم کرتی ہیں، جن میں اونکس رن ٹائم کے ساتھ انفرنس، لاجٹس پروسیسنگ، سرچ اور سیمپلنگ، اور KV کیش مینجمنٹ شامل ہیں۔ ڈیولپرز ایک ہائی لیول generate() میتھڈ کو کال کر سکتے ہیں یا ماڈل کے ہر انٹرنیشن کو لوپ میں چلا سکتے ہیں، ایک وقت میں ایک ٹوکن جنریٹ کرتے ہوئے، اور لوپ کے اندر جنریشن پیرامیٹرز کو اختیاری طور پر اپڈیٹ کرتے ہوئے۔ یہ گریڈی/ بیم سرچ اور TopP، TopK سیمپلنگ کی سپورٹ فراہم کرتی ہے تاکہ ٹوکن سیکوئنسز کو جنریٹ کیا جا سکے اور لاجٹس پروسیسنگ جیسے ریپیٹیشن پینلٹیز کو بلٹ ان سپورٹ کرتی ہے۔ آپ آسانی سے کسٹم اسکورنگ بھی شامل کر سکتے ہیں۔

ایپلیکیشن لیول پر، آپ اونکس رن ٹائم کے لیے جنریٹیو AI ایکسٹینشنز کا استعمال کرتے ہوئے C++/ C# / Python میں ایپلیکیشنز بنا سکتے ہیں۔ ماڈل لیول پر، آپ اسے فائن ٹیونڈ ماڈلز کو مرج کرنے اور متعلقہ کوانٹیٹیٹو ڈپلائمنٹ کام کرنے کے لیے استعمال کر سکتے ہیں۔

## **جنریٹیو AI ایکسٹینشنز کے ساتھ Phi-3.5 کو کوانٹائز کرنا**

### **سپورٹڈ ماڈلز**

اونکس رن ٹائم کے لیے جنریٹیو AI ایکسٹینشنز Microsoft Phi، Google Gemma، Mistral، Meta LLaMA کے کوانٹائزیشن کنورژن کی سپورٹ کرتی ہیں۔

### **جنریٹیو AI ایکسٹینشنز میں ماڈل بلڈر**

ماڈل بلڈر اونکس ماڈلز کو آپٹیمائزڈ اور کوانٹائز کرنے میں نمایاں تیزی فراہم کرتا ہے جو اونکس رن ٹائم generate() API کے ساتھ چلتے ہیں۔

ماڈل بلڈر کے ذریعے، آپ ماڈل کو INT4، INT8، FP16، FP32 میں کوانٹائز کر سکتے ہیں اور مختلف ہارڈویئر ایکسیلریشن میتھڈز جیسے کہ CPU، CUDA، DirectML، Mobile وغیرہ کو کمبائن کر سکتے ہیں۔

ماڈل بلڈر استعمال کرنے کے لیے آپ کو انسٹال کرنا ہوگا:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

انسٹالیشن کے بعد، آپ ٹرمینل سے ماڈل بلڈر اسکرپٹ چلا سکتے ہیں تاکہ ماڈل فارمیٹ اور کوانٹائزیشن کنورژن انجام دیا جا سکے۔

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

متعلقہ پیرامیٹرز کو سمجھیں:

1. **model_name** یہ Hugging Face پر موجود ماڈل ہے، جیسے microsoft/Phi-3.5-mini-instruct، microsoft/Phi-3.5-vision-instruct وغیرہ۔ یہ وہ راستہ بھی ہو سکتا ہے جہاں آپ نے ماڈل محفوظ کیا ہے۔

2. **path_to_output_folder** کوانٹائزڈ کنورژن کو محفوظ کرنے کا راستہ۔

3. **execution_provider** مختلف ہارڈویئر ایکسیلریشن کی سپورٹ، جیسے cpu، cuda، DirectML۔

4. **cache_dir_to_save_hf_files** ہم Hugging Face سے ماڈل ڈاؤن لوڈ کرتے ہیں اور اسے لوکل طور پر کیش کرتے ہیں۔

***نوٹ:***

## **ماڈل بلڈر کے ذریعے Phi-3.5 کو کوانٹائز کرنے کا طریقہ**

ماڈل بلڈر اب Phi-3.5-Instruct اور Phi-3.5-Vision کے لیے اونکس ماڈل کوانٹائزیشن کی سپورٹ فراہم کرتا ہے۔

### **Phi-3.5-Instruct**

**کوانٹائزڈ INT 4 کے لیے CPU ایکسیلریٹڈ کنورژن**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**کوانٹائزڈ INT 4 کے لیے CUDA ایکسیلریٹڈ کنورژن**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. ٹرمینل میں ماحول سیٹ کریں:

```bash

mkdir models

cd models 

```

2. microsoft/Phi-3.5-vision-instruct کو ماڈلز فولڈر میں ڈاؤن لوڈ کریں:
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. یہ فائلیں اپنے Phi-3.5-vision-instruct فولڈر میں ڈاؤن لوڈ کریں:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. یہ فائل models فولڈر میں ڈاؤن لوڈ کریں:
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ٹرمینل پر جائیں:

    FP32 کے ساتھ اونکس سپورٹ کنورٹ کریں:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **نوٹ:**

1. ماڈل بلڈر فی الحال Phi-3.5-Instruct اور Phi-3.5-Vision کے کنورژن کی سپورٹ فراہم کرتا ہے، لیکن Phi-3.5-MoE کی نہیں۔

2. اونکس کے کوانٹائزڈ ماڈل کو استعمال کرنے کے لیے، آپ اسے اونکس رن ٹائم کے لیے جنریٹیو AI ایکسٹینشنز SDK کے ذریعے استعمال کر سکتے ہیں۔

3. ہمیں زیادہ ذمہ دار AI پر غور کرنے کی ضرورت ہے، لہذا ماڈل کوانٹائزیشن کنورژن کے بعد، زیادہ مؤثر نتائج کی جانچ کرنے کی سفارش کی جاتی ہے۔

4. CPU INT4 ماڈل کو کوانٹائز کرکے، ہم اسے Edge Device پر ڈپلائے کر سکتے ہیں، جو بہتر ایپلیکیشن کے منظرنامے فراہم کرتا ہے۔ اسی لیے ہم نے Phi-3.5-Instruct کو INT 4 کے ارد گرد مکمل کیا ہے۔

## **وسائل**

1. اونکس رن ٹائم کے لیے جنریٹیو AI ایکسٹینشنز کے بارے میں مزید جانیں:
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. اونکس رن ٹائم کے لیے جنریٹیو AI ایکسٹینشنز کا GitHub ریپو:
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا بے ضابطگیاں ہوسکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔