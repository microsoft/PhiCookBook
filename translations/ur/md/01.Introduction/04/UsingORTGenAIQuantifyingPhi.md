# **آنکس رن ٹائم کے لیے جنریٹو اے آئی ایکسٹینشنز کا استعمال کرتے ہوئے فی خاندان کا کوانٹائزیشن**

## **آنکس رن ٹائم کے لیے جنریٹو اے آئی ایکسٹینشنز کیا ہیں**

یہ ایکسٹینشنز آپ کو ONNX رن ٹائم ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) کے ساتھ جنریٹو اے آئی چلانے میں مدد دیتی ہیں۔ یہ ONNX ماڈلز کے لیے جنریٹو AI لوپ فراہم کرتی ہیں، جس میں ONNX رن ٹائم کے ساتھ انفیرنس، لاجٹس پروسیسنگ، سرچ اور سیمپلنگ، اور KV کیش مینجمنٹ شامل ہیں۔ ڈویلپرز ہائی لیول generate() میتھڈ کال کر سکتے ہیں، یا ماڈل کی ہر دور کو لوپ میں چلا سکتے ہیں، ایک وقت میں ایک ٹوکن جنریٹ کرتے ہوئے، اور آپشنلی جنریشن پیرا میٹرز کو لوپ کے اندر اپ ڈیٹ کر سکتے ہیں۔ اس میں گریڈی/بیم سرچ اور TopP، TopK سیمپلنگ کی سپورٹ ہے تاکہ ٹوکن سیکوئنسز بنائے جا سکیں اور لاجٹس پروسیسنگ جیسے ریپیٹیشن پینالٹیز بھی بلٹ ان ہیں۔ آپ آسانی سے کسٹم اسکورنگ بھی شامل کر سکتے ہیں۔

ایپلیکیشن کی سطح پر، آپ آنکس رن ٹائم کے لیے جنریٹو اے آئی ایکسٹینشنز کو C++/ C# / Python استعمال کرتے ہوئے ایپلیکیشنز بنانے کے لیے استعمال کر سکتے ہیں۔ ماڈل کی سطح پر، آپ اسے فائن ٹون کردہ ماڈلز کو مرج کرنے اور متعلقہ معیاری تعیناتی کے کام کرنے کے لیے استعمال کر سکتے ہیں۔


## **آنکس رن ٹائم کے لیے جنریٹو اے آئی ایکسٹینشنز کے ساتھ فی-3.5 کو کوانٹائز کرنا**

### **سپورٹ کردہ ماڈلز**

آنکس رن ٹائم کے لیے جنریٹو اے آئی ایکسٹینشنز مائیکروسافٹ فی، گوگل جیما، میسٹریل، میٹا LLaMA کے کوانٹائزیشن تبدیلی کی حمایت کرتے ہیں۔


### **آنکس رن ٹائم کے لیے جنریٹو اے آئی ایکسٹینشنز میں ماڈل بلڈر**

ماڈل بلڈر ONNX رن ٹائم generate() API کے ساتھ چلنے والے بہتر بنائے گئے اور کوانٹائزڈ ONNX ماڈلز بنانے کو بہت تیز کر دیتا ہے۔

ماڈل بلڈر کے ذریعے، آپ ماڈل کو INT4، INT8، FP16، FP32 میں کوانٹائز کر سکتے ہیں، اور مختلف ہارڈویئر ایکسلیریشن کے طریقے جیسے CPU، CUDA، DirectML، موبائل وغیرہ کو ملا سکتے ہیں۔

ماڈل بلڈر استعمال کرنے کے لیے آپ کو انسٹال کرنا ہوگا

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

انسٹالیشن کے بعد، آپ ماڈل بلڈر اسکرپٹ کو ٹرمینل سے چلا کر ماڈل فارمیٹ اور کوانٹائزیشن تبدیلی کر سکتے ہیں۔


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

متعلقہ پیرا میٹرز کو سمجھیں

1. **model_name** یہ Hugging face پر ماڈل ہے، جیسے microsoft/Phi-3.5-mini-instruct، microsoft/Phi-3.5-vision-instruct، وغیرہ۔ یہ وہ راستہ بھی ہو سکتا ہے جہاں آپ ماڈل اسٹور کرتے ہیں۔

2. **path_to_output_folder** کوانٹائز تبدیلی کی محفوظ شدہ جگہ

3. **execution_provider** مختلف ہارڈویئر ایکسلیریشن سپورٹ، جیسے cpu، cuda، DirectML

4. **cache_dir_to_save_hf_files** ہم ماڈل کو Hugging face سے ڈاؤن لوڈ کرتے ہیں اور اسے مقامی طور پر کیش کرتے ہیں۔




***نوٹ:*** <ul>اگرچہ آنکس رن ٹائم کے لیے جنریٹو اے آئی ایکسٹینشنز اب بھی پریویو میں ہیں، انہیں Microsoft Olive میں شامل کیا جا چکا ہے، اور آپ Microsoft Olive کے ذریعے آنکس رن ٹائم کے لیے جنریٹو AI ایکسٹینشنز ماڈل بلڈر فنکشنز کو بھی کال کر سکتے ہیں۔</ul>

## **ماڈل بلڈر کو فی-3.5 کو کوانٹائز کرنے کے لیے کیسے استعمال کریں**

ماڈل بلڈر اب Phi-3.5 Instruct اور Phi-3.5-Vision کے لیے ONNX ماڈل کوانٹائزیشن کی حمایت کرتا ہے۔

### **Phi-3.5-Instruct**


**کوانٹائزڈ INT 4 کی CPU ایکسلیریٹڈ تبدیلی**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**کوانٹائزڈ INT 4 کی CUDA ایکسلیریٹڈ تبدیلی**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```



```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```


### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. ٹرمینل میں ماحول مقرر کریں

```bash

mkdir models

cd models 

```

2. models فولڈر میں microsoft/Phi-3.5-vision-instruct ڈاؤن لوڈ کریں
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. براہ کرم یہ فائلیں اپنے Phi-3.5-vision-instruct فولڈر میں ڈاؤن لوڈ کریں

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. اس فائل کو models فولڈر میں ڈاؤن لوڈ کریں
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ٹرمینل پر جائیں

    FP32 کے ساتھ ONNX کی سپورٹ کو تبدیل کریں


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **نوٹ:**

1. ماڈل بلڈر فی الحال Phi-3.5-Instruct اور Phi-3.5-Vision کی تبدیلی کی حمایت کرتا ہے، لیکن Phi-3.5-MoE کی نہیں۔

2. ONNX کے کوانٹائزڈ ماڈل کو آپ آنکس رن ٹائم کے جنریٹو AI ایکسٹینشنز SDK کے ذریعے استعمال کر سکتے ہیں۔

3. ہمیں مزید ذمہ دار AI پر غور کرنا چاہیے، اس لیے ماڈل کی کوانٹائزیشن تبدیلی کے بعد، زیادہ مؤثر نتائج کی جانچ کی سفارش کی جاتی ہے۔

4. CPU INT4 ماڈل کو کوانٹائز کر کے، ہم اسے ایج ڈیوائس پر تعینات کر سکتے ہیں، جس کے اطلاقی منظرنامے بہتر ہیں، اس لیے ہم نے فی-3.5 انسٹرکٹ کو تقریباً INT 4 کے گرد مکمل کر لیا ہے۔


## **وسائل**

1. آنکس رن ٹائم کے لیے جنریٹو AI ایکسٹینشنز کے بارے میں مزید جاننے کے لیے [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. آنکس رن ٹائم کے لیے جنریٹو AI ایکسٹینشنز کا GitHub ریپو [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->