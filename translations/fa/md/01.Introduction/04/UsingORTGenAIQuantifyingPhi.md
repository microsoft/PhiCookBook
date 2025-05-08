<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3bb9f5c926673593287eddc3741226cb",
  "translation_date": "2025-05-07T14:52:03+00:00",
  "source_file": "md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md",
  "language_code": "fa"
}
-->
## **چگونه از Model Builder برای کوانتیزه کردن Phi-3.5 استفاده کنیم**

Model Builder اکنون از کوانتیزه کردن مدل‌های ONNX برای Phi-3.5 Instruct و Phi-3.5-Vision پشتیبانی می‌کند.

### **Phi-3.5-Instruct**

**تبدیل کوانتیزه شده INT4 با شتاب‌دهی CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**تبدیل کوانتیزه شده INT4 با شتاب‌دهی CUDA**

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

3. لطفاً این فایل‌ها را در پوشه Phi-3.5-vision-instruct خود دانلود کنید

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. این فایل را در پوشه models دانلود کنید  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. به ترمینال بروید

    تبدیل ONNX با پشتیبانی FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **توجه:**

1. Model Builder در حال حاضر از تبدیل Phi-3.5-Instruct و Phi-3.5-Vision پشتیبانی می‌کند، اما Phi-3.5-MoE را پوشش نمی‌دهد.

2. برای استفاده از مدل کوانتیزه شده ONNX، می‌توانید از طریق SDK افزونه‌های Generative AI برای onnxruntime استفاده کنید.

3. باید مسئولیت‌پذیری بیشتری در زمینه هوش مصنوعی در نظر بگیریم، بنابراین پس از تبدیل کوانتیزه مدل، توصیه می‌شود آزمایش‌های موثرتری روی نتایج انجام شود.

4. با کوانتیزه کردن مدل CPU INT4، می‌توانیم آن را روی دستگاه‌های Edge مستقر کنیم که سناریوهای کاربردی بهتری دارد، بنابراین Phi-3.5-Instruct حول INT4 تکمیل شده است.

## **منابع**

1. برای کسب اطلاعات بیشتر درباره افزونه‌های Generative AI برای onnxruntime  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. مخزن GitHub افزونه‌های Generative AI برای onnxruntime  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده شود. ما مسئول هیچ گونه سوء تفاهم یا تفسیر نادرستی که ناشی از استفاده از این ترجمه باشد، نیستیم.