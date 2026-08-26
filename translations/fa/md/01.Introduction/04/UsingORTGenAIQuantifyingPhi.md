# **کوانتیزه کردن خانواده فی با استفاده از افزونه‌های هوش مصنوعی مولد برای onnxruntime**

## **افزونه‌های هوش مصنوعی مولد برای onnxruntime چیست؟**

این افزونه‌ها به شما کمک می‌کنند تا هوش مصنوعی مولد را با ONNX Runtime ( [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)) اجرا کنید. این افزونه‌ها حلقه هوش مصنوعی مولد را برای مدل‌های ONNX فراهم می‌کنند، شامل استنتاج با ONNX Runtime، پردازش لوگیت‌ها، جستجو و نمونه‌گیری، و مدیریت کش KV. توسعه‌دهندگان می‌توانند متد سطح بالای generate() را فراخوانی کنند، یا هر تکرار مدل را در یک حلقه اجرا کنند و یک توکن در هر بار تولید کنند، و به صورت اختیاری پارامترهای تولید را داخل حلقه به‌روزرسانی کنند. این افزونه از جستجوی حریصانه/تراس و نمونه‌گیری TopP، TopK برای تولید توکن‌ها و پردازش لوگیت تعبیه‌شده مانند جریمه‌های تکرار پشتیبانی می‌کند. همچنین می‌توانید به سادگی امتیازدهی سفارشی را اضافه کنید.

در سطح برنامه، می‌توانید از افزونه‌های هوش مصنوعی مولد برای onnxruntime برای ساخت برنامه‌ها با C++/ C# / Python استفاده کنید. در سطح مدل، می‌توانید برای ادغام مدل‌های فاین تیون شده و انجام امور مربوط به استقرار کمی از آن بهره ببرید.


## **کوانتیزه کردن Phi-3.5 با افزونه‌های هوش مصنوعی مولد برای onnxruntime**

### **مدل‌های پشتیبانی شده**

افزونه‌های هوش مصنوعی مولد برای onnxruntime پشتیبانی تبدیل کوانتیزه مایکروسافت Phi ، گوگل Gemma، Mistral، Meta LLaMA را فراهم می‌کنند.


### **سازنده مدل در افزونه‌های هوش مصنوعی مولد برای onnxruntime**

سازنده مدل به طور قابل توجهی سرعت ایجاد مدل‌های ONNX بهینه و کوانتیزه شده که با API generate() در ONNX Runtime اجرا می‌شوند را افزایش می‌دهد.

با استفاده از سازنده مدل می‌توانید مدل را به INT4، INT8، FP16، FP32 کوانتیزه کنید و روش‌های مختلف شتاب‌دهنده سخت‌افزاری مانند CPU، CUDA، DirectML، Mobile و غیره را ترکیب کنید.

برای استفاده از سازنده مدل باید نصب کنید

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

پس از نصب، می‌توانید اسکریپت سازنده مدل را از ترمینال اجرا کنید تا تبدیل فرمت مدل و کوانتیزه شدن را انجام دهید.


```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

پارامترهای مرتبط را درک کنید

1. **model_name** این مدل در Hugging face است، مانند microsoft/Phi-3.5-mini-instruct، microsoft/Phi-3.5-vision-instruct و غیره. همچنین می‌تواند مسیر ذخیره مدل باشد

2. **path_to_output_folder** مسیر ذخیره تبدیل کوانتیزه شده

3. **execution_provider** پشتیبانی سخت‌افزاری مختلف مانند cpu، cuda، DirectML

4. **cache_dir_to_save_hf_files** ما مدل را از Hugging face دانلود کرده و به صورت محلی کش می‌کنیم




***توضیح：*** <ul>اگرچه افزونه‌های هوش مصنوعی مولد برای onnxruntime در پیش‌نمایش هستند، اما در Microsoft Olive گنجانده شده‌اند و شما همچنین می‌توانید از طریق Microsoft Olive به تابع سازنده مدل افزونه‌های هوش مصنوعی مولد برای onnxruntime دسترسی داشته باشید.</ul>

## **چگونه با استفاده از سازنده مدل Phi-3.5 را کوانتیزه کنیم**

سازنده مدل اکنون از کوانتیزه کردن مدل ONNX برای Phi-3.5 Instruct و Phi-3.5-Vision پشتیبانی می‌کند

### **Phi-3.5-Instruct**


**تبدیل کوانتیزه شده INT4 شتاب‌یافته توسط CPU**


```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**تبدیل کوانتیزه شده INT4 شتاب‌یافته توسط CUDA**

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

3. لطفاً این فایل‌ها را به پوشه Phi-3.5-vision-instruct خود دانلود کنید

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)


4. این فایل را به پوشه models دانلود کنید
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. به ترمینال بروید

تبدیل ONNX پشتیبانی شده با FP32


```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```


### **توضیح:**

1. سازنده مدل در حال حاضر تبدیل Phi-3.5-Instruct و Phi-3.5-Vision را پشتیبانی می‌کند ولی Phi-3.5-MoE را نه

2. برای استفاده از مدل کوانتیزه شده ONNX، می‌توانید از طریق SDK افزونه‌های هوش مصنوعی مولد برای onnxruntime آن را به کار ببرید

3. ما باید ملاحظات مسئولیت‌پذیرتری در هوش مصنوعی داشته باشیم، لذا پس از تبدیل کوانتیزه مدل، توصیه می‌شود آزمایش اثربخشی نتایج را انجام دهید

4. با کوانتیزه کردن مدل CPU INT4 می‌توانیم آن را روی دستگاه‌های Edge مستقر کنیم که سناریوهای کاربردی بهتری دارد، بنابراین حول INT4 کوانتیزه کردن Phi-3.5-Instruct را انجام داده‌ایم


## **منابع**

1. برای کسب اطلاعات بیشتر در مورد افزونه‌های هوش مصنوعی مولد برای onnxruntime به [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/) مراجعه کنید

2. مخزن GitHub افزونه‌های هوش مصنوعی مولد برای onnxruntime [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->