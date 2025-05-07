<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-07T14:07:11+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "fa"
}
-->
# **استفاده از Microsoft Phi-3.5 tflite برای ساخت اپلیکیشن اندروید**

این نمونه‌ای از اندروید است که از مدل‌های Microsoft Phi-3.5 tflite استفاده می‌کند.

## **📚 دانش**

API استنتاج LLM اندروید به شما اجازه می‌دهد مدل‌های بزرگ زبان (LLM) را به‌صورت کامل روی دستگاه برای برنامه‌های اندروید اجرا کنید، که می‌توانید برای انجام طیف وسیعی از کارها مانند تولید متن، بازیابی اطلاعات به شکل زبان طبیعی و خلاصه‌سازی اسناد از آن استفاده کنید. این تسک از چندین مدل بزرگ زبان متن به متن به صورت داخلی پشتیبانی می‌کند، بنابراین می‌توانید جدیدترین مدل‌های تولیدی AI روی دستگاه را در اپلیکیشن‌های اندروید خود به‌کار ببرید.

Googld AI Edge Torch کتابخانه‌ای در پایتون است که از تبدیل مدل‌های PyTorch به فرمت .tflite پشتیبانی می‌کند، که سپس می‌توان آن‌ها را با TensorFlow Lite و MediaPipe اجرا کرد. این امکان را برای برنامه‌های اندروید، iOS و IoT فراهم می‌کند که مدل‌ها را به‌صورت کامل روی دستگاه اجرا کنند. AI Edge Torch پوشش گسترده‌ای برای CPU دارد و پشتیبانی اولیه از GPU و NPU ارائه می‌دهد. AI Edge Torch به دنبال ادغام نزدیک با PyTorch است، بر پایه torch.export() ساخته شده و پوشش خوبی از اپراتورهای Core ATen ارائه می‌دهد.

## **🪬 راهنما**

### **🔥 تبدیل Microsoft Phi-3.5 به پشتیبانی tflite**

0. این نمونه برای اندروید ۱۴ به بالا است

1. نصب Python 3.10.12

***پیشنهاد:*** استفاده از conda برای نصب محیط پایتون خود

2. اوبونتو ۲۰.۰۴ / ۲۲.۰۴ (لطفاً روی [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) تمرکز کنید)

***پیشنهاد:*** استفاده از Azure Linux VM یا VM ابری شخص ثالث برای ایجاد محیط خود

3. به ترمینال لینوکس خود بروید و کتابخانه پایتون را نصب کنید

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. دانلود Microsoft-3.5-Instruct از Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. تبدیل Microsoft Phi-3.5 به tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 تبدیل Microsoft Phi-3.5 به بسته Mediapipe اندروید**

لطفاً ابتدا mediapipe را نصب کنید

```bash

pip install mediapipe

```

این کد را در [دفترچه یادداشت خود](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) اجرا کنید

```python

import mediapipe as mp
from mediapipe.tasks.python.genai import bundler

config = bundler.BundleConfig(
    tflite_model='Your Phi-3.5 tflite model path',
    tokenizer_model='Your Phi-3.5 tokenizer model path',
    start_token='start_token',
    stop_tokens=[STOP_TOKENS],
    output_filename='Your Phi-3.5 task model path',
    enable_bytes_to_unicode_mapping=True or Flase,
)
bundler.create_bundle(config)

```

### **🔥 استفاده از adb push برای انتقال مدل تسک به مسیر دستگاه‌های اندروید شما**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 اجرای کد اندروید شما**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1be99ffad0cbf22f4ac0c41530774d51ff903cfaa1d3cd3c8e.fa.png)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه نیستیم.