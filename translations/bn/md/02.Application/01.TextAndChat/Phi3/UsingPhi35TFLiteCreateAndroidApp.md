<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:47:37+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "bn"
}
-->
# **Microsoft Phi-3.5 tflite ব্যবহার করে Android অ্যাপ তৈরি করা**

এটি Microsoft Phi-3.5 tflite মডেল ব্যবহার করে একটি Android স্যাম্পল।

## **📚 জ্ঞান**

Android LLM Inference API আপনাকে Android অ্যাপ্লিকেশনের জন্য সম্পূর্ণ ডিভাইস-অভিযুক্ত বড় ভাষার মডেল (LLMs) চালানোর সুযোগ দেয়, যার মাধ্যমে আপনি বিভিন্ন কাজ করতে পারেন, যেমন টেক্সট তৈরি করা, প্রাকৃতিক ভাষায় তথ্য অনুসন্ধান করা এবং ডকুমেন্ট সংক্ষিপ্ত করা। এই টাস্কটি একাধিক টেক্সট-টু-টেক্সট বড় ভাষার মডেল সমর্থন করে, তাই আপনি সর্বশেষ ডিভাইস-অভিযুক্ত জেনারেটিভ AI মডেলগুলো আপনার Android অ্যাপে প্রয়োগ করতে পারবেন।

Googld AI Edge Torch একটি পাইথন লাইব্রেরি যা PyTorch মডেলকে .tflite ফরম্যাটে রূপান্তর করার সমর্থন দেয়, যা পরে TensorFlow Lite এবং MediaPipe দিয়ে চালানো যায়। এটি Android, iOS এবং IoT অ্যাপ্লিকেশনগুলির জন্য সম্পূর্ণ ডিভাইস-অভিযুক্ত মডেল চালানোর সুযোগ করে দেয়। AI Edge Torch বিস্তৃত CPU সমর্থন প্রদান করে, প্রাথমিক GPU এবং NPU সমর্থন সহ। AI Edge Torch PyTorch এর সাথে ঘনিষ্ঠভাবে একীভূত হতে চায়, torch.export() এর উপরে তৈরি করে এবং Core ATen অপারেটরগুলোর ভালো সমর্থন দেয়।

## **🪬 নির্দেশিকা**

### **🔥 Microsoft Phi-3.5 কে tflite সমর্থনে রূপান্তর করা**

0. এই স্যাম্পলটি Android 14+ এর জন্য।

1. Python 3.10.12 ইনস্টল করুন

***প্রস্তাবনা:*** conda ব্যবহার করে আপনার Python পরিবেশ ইনস্টল করুন

2. Ubuntu 20.04 / 22.04 (অনুগ্রহ করে [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) এর দিকে মনোযোগ দিন)

***প্রস্তাবনা:*** Azure Linux VM অথবা তৃতীয় পক্ষের ক্লাউড VM ব্যবহার করে আপনার পরিবেশ তৈরি করুন

3. আপনার Linux bash এ যান এবং Python লাইব্রেরি ইনস্টল করুন

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Hugging face থেকে Microsoft-3.5-Instruct ডাউনলোড করুন

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Microsoft Phi-3.5 কে tflite এ রূপান্তর করুন

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5 কে Android Mediapipe Bundle এ রূপান্তর করা**

প্রথমে mediapipe ইনস্টল করুন

```bash

pip install mediapipe

```

[আপনার নোটবুকে](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) এই কোড চালান

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

### **🔥 adb push ব্যবহার করে আপনার Android ডিভাইসের পাথে টাস্ক মডেল পাঠানো**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 আপনার Android কোড চালানো**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.bn.png)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে দয়া করে জানুন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায় কর্তৃত্বপূর্ণ উৎস হিসাবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।