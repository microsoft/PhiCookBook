<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-03-27T11:08:07+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "fa"
}
-->
# **استفاده از Microsoft Phi-3.5 tflite برای ساخت اپلیکیشن اندروید**

این یک نمونه اپلیکیشن اندروید است که از مدل‌های Microsoft Phi-3.5 tflite استفاده می‌کند.

## **📚 دانش**

API استنتاج LLM اندروید به شما اجازه می‌دهد مدل‌های زبانی بزرگ (LLM) را به‌طور کامل روی دستگاه برای اپلیکیشن‌های اندروید اجرا کنید. با این قابلیت می‌توانید طیف گسترده‌ای از وظایف را انجام دهید، مانند تولید متن، بازیابی اطلاعات به شکل زبان طبیعی، و خلاصه‌سازی اسناد. این وظیفه پشتیبانی داخلی از چندین مدل زبانی بزرگ متن به متن را فراهم می‌کند، بنابراین می‌توانید جدیدترین مدل‌های تولیدی هوش مصنوعی روی دستگاه را به اپلیکیشن‌های اندروید خود اعمال کنید.

Google AI Edge Torch یک کتابخانه پایتون است که از تبدیل مدل‌های PyTorch به فرمت .tflite پشتیبانی می‌کند. این مدل‌ها سپس می‌توانند با TensorFlow Lite و MediaPipe اجرا شوند. این قابلیت امکان اجرای مدل‌ها به‌طور کامل روی دستگاه را برای اندروید، iOS و IoT فراهم می‌کند. AI Edge Torch پشتیبانی گسترده‌ای از CPU ارائه می‌دهد و پشتیبانی اولیه از GPU و NPU نیز دارد. AI Edge Torch به دنبال یکپارچگی نزدیک با PyTorch است و بر پایه‌ی torch.export() ساخته شده و پوشش خوبی از اپراتورهای Core ATen ارائه می‌دهد.

## **🪬 راهنما**

### **🔥 تبدیل Microsoft Phi-3.5 به فرمت tflite**

0. این نمونه برای اندروید 14 به بالا است.

1. نصب Python 3.10.12

***پیشنهاد:*** از conda برای نصب محیط Python خود استفاده کنید.

2. اوبونتو 20.04 / 22.04 (لطفاً به [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) توجه کنید)

***پیشنهاد:*** استفاده از Azure Linux VM یا ماشین مجازی ابری شخص ثالث برای ایجاد محیط شما.

3. به bash لینوکس خود بروید و کتابخانه پایتون را نصب کنید.

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. دانلود Microsoft-3.5-Instruct از Hugging Face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. تبدیل Microsoft Phi-3.5 به فرمت tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 تبدیل Microsoft Phi-3.5 به Android Mediapipe Bundle**

ابتدا mediapipe را نصب کنید.

```bash

pip install mediapipe

```

این کد را در [نوت‌بوک خود](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) اجرا کنید.

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

### **🔥 استفاده از adb push برای انتقال مدل به مسیر دستگاه اندروید شما**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 اجرای کد اندروید شما**

![دمو](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.fa.png)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل اشتباهات یا نادقتی‌ها باشند. سند اصلی به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.