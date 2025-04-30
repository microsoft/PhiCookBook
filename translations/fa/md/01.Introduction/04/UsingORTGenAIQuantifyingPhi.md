<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-03-27T08:47:36+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingORTGenAIQuantifyingPhi.md",
  "language_code": "fa"
}
-->
# **کم‌حجم‌سازی خانواده Phi با استفاده از افزونه‌های هوش مصنوعی مولد برای onnxruntime**

## **افزونه‌های هوش مصنوعی مولد برای onnxruntime چیست؟**

این افزونه‌ها به شما کمک می‌کنند تا هوش مصنوعی مولد را با ONNX Runtime اجرا کنید ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). این ابزار حلقه‌های مولد هوش مصنوعی را برای مدل‌های ONNX فراهم می‌کند، شامل استنتاج با ONNX Runtime، پردازش logits، جستجو و نمونه‌گیری، و مدیریت کش KV. توسعه‌دهندگان می‌توانند از روش سطح بالای generate() استفاده کنند یا هر iteration مدل را در یک حلقه اجرا کنند، هر بار یک token تولید کنند و در صورت نیاز پارامترهای تولید را در داخل حلقه به‌روزرسانی کنند. این ابزار از جستجوی حریصانه/پرتو و نمونه‌گیری TopP، TopK برای تولید توالی‌های token پشتیبانی می‌کند و پردازش logits داخلی مانند جریمه‌های تکرار را نیز ارائه می‌دهد. همچنین می‌توانید امتیازدهی سفارشی را به راحتی اضافه کنید.

در سطح کاربرد، می‌توانید از افزونه‌های هوش مصنوعی مولد برای onnxruntime برای ساخت برنامه‌ها با استفاده از C++/C#/Python استفاده کنید. در سطح مدل، می‌توانید از آن برای ادغام مدل‌های آموزش‌دیده و انجام کارهای مرتبط با استقرار کمی استفاده کنید.

## **کم‌حجم‌سازی Phi-3.5 با افزونه‌های هوش مصنوعی مولد برای onnxruntime**

### **مدل‌های پشتیبانی‌شده**

افزونه‌های هوش مصنوعی مولد برای onnxruntime از تبدیل کم‌حجم‌سازی مدل‌های Microsoft Phi، Google Gemma، Mistral، Meta LLaMA پشتیبانی می‌کنند.

### **سازنده مدل در افزونه‌های هوش مصنوعی مولد برای onnxruntime**

سازنده مدل فرآیند ایجاد مدل‌های بهینه‌سازی‌شده و کم‌حجم‌شده ONNX که با API generate() در ONNX Runtime اجرا می‌شوند را به‌طور قابل توجهی تسریع می‌کند.

از طریق سازنده مدل، می‌توانید مدل را به INT4، INT8، FP16، FP32 کم‌حجم کنید و روش‌های مختلف تسریع سخت‌افزاری مانند CPU، CUDA، DirectML، Mobile و غیره را ترکیب کنید.

برای استفاده از سازنده مدل، باید نصب کنید:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

پس از نصب، می‌توانید اسکریپت سازنده مدل را از ترمینال اجرا کنید تا تبدیل فرمت مدل و کم‌حجم‌سازی را انجام دهید.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

درک پارامترهای مربوطه:

1. **model_name** این مدل در Hugging Face است، مانند microsoft/Phi-3.5-mini-instruct، microsoft/Phi-3.5-vision-instruct و غیره. همچنین می‌تواند مسیری باشد که مدل را در آن ذخیره کرده‌اید.

2. **path_to_output_folder** مسیر ذخیره تبدیل کم‌حجم‌شده.

3. **execution_provider** پشتیبانی از تسریع سخت‌افزاری مختلف، مانند cpu، cuda، DirectML.

4. **cache_dir_to_save_hf_files** ما مدل را از Hugging Face دانلود کرده و به صورت محلی ذخیره می‌کنیم.

***توجه:***

## **چگونه از سازنده مدل برای کم‌حجم‌سازی Phi-3.5 استفاده کنیم**

سازنده مدل اکنون از کم‌حجم‌سازی مدل ONNX برای Phi-3.5 Instruct و Phi-3.5-Vision پشتیبانی می‌کند.

### **Phi-3.5-Instruct**

**تبدیل کم‌حجم‌شده INT 4 با تسریع CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**تبدیل کم‌حجم‌شده INT 4 با تسریع CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. تنظیم محیط در ترمینال

```bash

mkdir models

cd models 

```

2. دانلود microsoft/Phi-3.5-vision-instruct در پوشه models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. لطفاً این فایل‌ها را به پوشه Phi-3.5-vision-instruct خود دانلود کنید:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. این فایل را به پوشه models دانلود کنید:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. به ترمینال بروید:

تبدیل پشتیبانی ONNX با FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **توجه:**

1. سازنده مدل در حال حاضر از تبدیل Phi-3.5-Instruct و Phi-3.5-Vision پشتیبانی می‌کند، اما از Phi-3.5-MoE پشتیبانی نمی‌کند.

2. برای استفاده از مدل کم‌حجم‌شده ONNX، می‌توانید از طریق SDK افزونه‌های هوش مصنوعی مولد برای onnxruntime از آن استفاده کنید.

3. ما باید به هوش مصنوعی مسئولیت‌پذیرتر توجه کنیم، بنابراین پس از تبدیل کم‌حجم‌سازی مدل، توصیه می‌شود آزمایش‌های مؤثرتری انجام دهید.

4. با کم‌حجم‌سازی مدل CPU INT4، می‌توانیم آن را در دستگاه‌های لبه‌ای مستقر کنیم، که سناریوهای کاربردی بهتری دارند. بنابراین ما Phi-3.5-Instruct را حول INT 4 تکمیل کرده‌ایم.

## **منابع**

1. اطلاعات بیشتر درباره افزونه‌های هوش مصنوعی مولد برای onnxruntime [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. مخزن GitHub افزونه‌های هوش مصنوعی مولد برای onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادقتی‌هایی باشند. سند اصلی به زبان مادری باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.