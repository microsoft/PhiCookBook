<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:50:04+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "ms"
}
-->
# **استفاده از Microsoft Phi-3.5 tflite برای ساخت اپلیکیشن اندروید**

این یک نمونه اندروید است که از مدل‌های Microsoft Phi-3.5 tflite استفاده می‌کند.

## **📚 دانش**

Android LLM Inference API به شما امکان می‌دهد مدل‌های بزرگ زبان (LLM) را به‌طور کامل روی دستگاه اندروید اجرا کنید، که می‌توانید برای انجام طیف گسترده‌ای از وظایف مانند تولید متن، بازیابی اطلاعات به صورت زبان طبیعی و خلاصه‌سازی اسناد استفاده کنید. این قابلیت پشتیبانی داخلی از چندین مدل بزرگ زبان متن به متن دارد، بنابراین می‌توانید جدیدترین مدل‌های تولیدی AI روی دستگاه را در اپلیکیشن‌های اندروید خود به کار ببرید.

Google AI Edge Torch یک کتابخانه پایتون است که از تبدیل مدل‌های PyTorch به فرمت .tflite پشتیبانی می‌کند، که سپس می‌توان آن‌ها را با TensorFlow Lite و MediaPipe اجرا کرد. این امکان را برای اپلیکیشن‌های اندروید، iOS و IoT فراهم می‌کند که مدل‌ها را به‌طور کامل روی دستگاه اجرا کنند. AI Edge Torch پوشش گسترده‌ای از CPUها ارائه می‌دهد و پشتیبانی اولیه از GPU و NPU را دارد. AI Edge Torch به دنبال ادغام نزدیک با PyTorch است، با استفاده از torch.export() و ارائه پوشش خوب برای اپراتورهای Core ATen.

## **🪬 راهنما**

### **🔥 تبدیل Microsoft Phi-3.5 به پشتیبانی tflite**

0. این نمونه برای اندروید 14 به بالا است

1. نصب Python 3.10.12

***پیشنهاد:*** استفاده از conda برای نصب محیط پایتون خود

2. Ubuntu 20.04 / 22.04 (لطفاً روی [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) تمرکز کنید)

***پیشنهاد:*** استفاده از Azure Linux VM یا VM ابری شخص ثالث برای ایجاد محیط خود

3. به bash لینوکس خود بروید و کتابخانه پایتون را نصب کنید

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

### **🔥 استفاده از adb push برای انتقال مدل به مسیر دستگاه اندروید شما**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 اجرای کد اندروید شما**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.ms.png)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.