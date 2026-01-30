## **چگونه از Model Builder برای کم‌حجم‌سازی Phi-3.5 استفاده کنیم**

Model Builder اکنون از کم‌حجم‌سازی مدل‌های ONNX برای Phi-3.5 Instruct و Phi-3.5-Vision پشتیبانی می‌کند.

### **Phi-3.5-Instruct**

**تبدیل کم‌حجم‌سازی شده با شتاب‌دهی CPU به INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**تبدیل کم‌حجم‌سازی شده با شتاب‌دهی CUDA به INT4**

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

3. لطفاً این فایل‌ها را در پوشه Phi-3.5-vision-instruct خود دانلود کنید:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. این فایل را در پوشه models دانلود کنید  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. به ترمینال بروید و تبدیل ONNX با پشتیبانی FP32 را انجام دهید

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **توجه:**

1. در حال حاضر Model Builder از تبدیل Phi-3.5-Instruct و Phi-3.5-Vision پشتیبانی می‌کند، اما Phi-3.5-MoE را پشتیبانی نمی‌کند.

2. برای استفاده از مدل‌های کم‌حجم‌شده ONNX، می‌توانید از طریق SDK افزونه‌های Generative AI برای onnxruntime استفاده کنید.

3. برای مسئولیت‌پذیری بیشتر در هوش مصنوعی، پس از تبدیل کم‌حجم‌سازی مدل، توصیه می‌شود آزمایش‌های موثرتری روی نتایج انجام شود.

4. با کم‌حجم‌سازی مدل CPU INT4، می‌توانیم آن را روی دستگاه‌های Edge مستقر کنیم که سناریوهای کاربردی بهتری دارد، بنابراین ما Phi-3.5-Instruct را حول INT4 تکمیل کرده‌ایم.

## **منابع**

1. برای اطلاعات بیشتر درباره Generative AI extensions for onnxruntime به [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/) مراجعه کنید.

2. مخزن GitHub افزونه‌های Generative AI برای onnxruntime در [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai) موجود است.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.