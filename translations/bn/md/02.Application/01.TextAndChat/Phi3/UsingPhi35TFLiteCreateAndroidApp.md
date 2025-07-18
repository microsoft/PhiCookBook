<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-07-17T02:51:13+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "bn"
}
-->
# **Microsoft Phi-3.5 tflite ব্যবহার করে Android অ্যাপ তৈরি করা**

এটি Microsoft Phi-3.5 tflite মডেল ব্যবহার করে একটি Android স্যাম্পল।

## **📚 জ্ঞান**

Android LLM Inference API আপনাকে Android অ্যাপ্লিকেশনের জন্য সম্পূর্ণ ডিভাইস-ভিত্তিক বড় ভাষা মডেল (LLMs) চালানোর সুযোগ দেয়, যা আপনি বিভিন্ন কাজের জন্য ব্যবহার করতে পারেন, যেমন টেক্সট তৈরি করা, প্রাকৃতিক ভাষায় তথ্য অনুসন্ধান করা এবং ডকুমেন্ট সারাংশ তৈরি করা। এই টাস্কটি একাধিক টেক্সট-টু-টেক্সট বড় ভাষা মডেলের জন্য বিল্ট-ইন সাপোর্ট প্রদান করে, তাই আপনি আপনার Android অ্যাপে সর্বশেষ ডিভাইস-ভিত্তিক জেনারেটিভ AI মডেল প্রয়োগ করতে পারবেন।

Google AI Edge Torch একটি পাইথন লাইব্রেরি যা PyTorch মডেলকে .tflite ফরম্যাটে রূপান্তর করার সাপোর্ট দেয়, যা পরে TensorFlow Lite এবং MediaPipe দিয়ে চালানো যায়। এটি Android, iOS এবং IoT অ্যাপ্লিকেশনগুলির জন্য উপযোগী, যা মডেলগুলো সম্পূর্ণ ডিভাইসে চালাতে সক্ষম। AI Edge Torch বিস্তৃত CPU সাপোর্ট দেয়, প্রাথমিকভাবে GPU এবং NPU সাপোর্ট সহ। AI Edge Torch PyTorch-এর সাথে ঘনিষ্ঠভাবে ইন্টিগ্রেট করার চেষ্টা করে, torch.export() এর উপর ভিত্তি করে এবং Core ATen অপারেটরগুলোর ভালো কভারেজ প্রদান করে।

## **🪬 নির্দেশিকা**

### **🔥 Microsoft Phi-3.5 কে tflite ফরম্যাটে রূপান্তর করা**

0. এই স্যাম্পলটি Android 14+ এর জন্য।

1. Python 3.10.12 ইনস্টল করুন

***পরামর্শ:*** conda ব্যবহার করে আপনার Python পরিবেশ ইনস্টল করুন

2. Ubuntu 20.04 / 22.04 (দয়া করে [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) এ ফোকাস করুন)

***পরামর্শ:*** Azure Linux VM বা তৃতীয় পক্ষের ক্লাউড VM ব্যবহার করে আপনার পরিবেশ তৈরি করুন

3. আপনার Linux bash-এ যান এবং Python লাইব্রেরি ইনস্টল করুন

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

5. Microsoft Phi-3.5 কে tflite ফরম্যাটে রূপান্তর করুন

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Microsoft Phi-3.5 কে Android Mediapipe Bundle এ রূপান্তর করা**

প্রথমে mediapipe ইনস্টল করুন

```bash

pip install mediapipe

```

এই কোডটি [আপনার নোটবুকে](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) চালান

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

### **🔥 adb push ব্যবহার করে মডেলটি আপনার Android ডিভাইসের পাথে পাঠানো**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 আপনার Android কোড চালানো**

![demo](../../../../../../translated_images/demo.06d5a4246f057d1be99ffad0cbf22f4ac0c41530774d51ff903cfaa1d3cd3c8e.bn.png)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।