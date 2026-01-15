<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:54:01+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "id"
}
-->
# **Menggunakan Microsoft Phi-3.5 tflite untuk membuat aplikasi Android**

Ini adalah contoh Android yang menggunakan model Microsoft Phi-3.5 tflite.

## **📚 Pengetahuan**

Android LLM Inference API memungkinkan Anda menjalankan large language models (LLM) sepenuhnya di perangkat untuk aplikasi Android, yang dapat digunakan untuk melakukan berbagai tugas, seperti menghasilkan teks, mengambil informasi dalam bentuk bahasa alami, dan meringkas dokumen. Task ini menyediakan dukungan bawaan untuk berbagai model large language text-to-text, sehingga Anda dapat menerapkan model AI generatif terbaru yang berjalan di perangkat ke aplikasi Android Anda.

Google AI Edge Torch adalah pustaka python yang mendukung konversi model PyTorch ke format .tflite, yang kemudian dapat dijalankan dengan TensorFlow Lite dan MediaPipe. Ini memungkinkan aplikasi untuk Android, iOS, dan IoT yang dapat menjalankan model sepenuhnya di perangkat. AI Edge Torch menawarkan cakupan CPU yang luas, dengan dukungan awal untuk GPU dan NPU. AI Edge Torch berupaya untuk terintegrasi erat dengan PyTorch, membangun di atas torch.export() dan menyediakan cakupan operator Core ATen yang baik.

## **🪬 Panduan**

### **🔥 Konversi Microsoft Phi-3.5 ke dukungan tflite**

0. Contoh ini untuk Android 14+

1. Instal Python 3.10.12

***Saran:*** gunakan conda untuk mengatur lingkungan Python Anda

2. Ubuntu 20.04 / 22.04 (harap fokus pada [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Saran:*** Gunakan Azure Linux VM atau VM cloud pihak ketiga untuk membuat lingkungan Anda

3. Buka bash Linux Anda, untuk menginstal pustaka Python

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Unduh Microsoft-3.5-Instruct dari Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Konversi Microsoft Phi-3.5 ke tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Konversi Microsoft Phi-3.5 ke Android Mediapipe Bundle**

harap instal mediapipe terlebih dahulu

```bash

pip install mediapipe

```

jalankan kode ini di [notebook Anda](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

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

### **🔥 Menggunakan adb push untuk mengirim model task ke path perangkat Android Anda**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Menjalankan kode Android Anda**

![demo](../../../../../../translated_images/id/demo.06d5a4246f057d1b.png)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.