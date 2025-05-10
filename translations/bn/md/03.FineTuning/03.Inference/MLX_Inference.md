<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-05-09T22:30:39+00:00",
  "source_file": "md/03.FineTuning/03.Inference/MLX_Inference.md",
  "language_code": "bn"
}
-->
# **Inference Phi-3 with Apple MLX Framework**

## **MLX Framework কী**

MLX হল Apple সিলিকনে মেশিন লার্নিং গবেষণার জন্য একটি অ্যারে ফ্রেমওয়ার্ক, যা Apple মেশিন লার্নিং গবেষণা থেকে এসেছে।

MLX মেশিন লার্নিং গবেষকদের জন্য মেশিন লার্নিং গবেষকদের দ্বারা ডিজাইন করা হয়েছে। ফ্রেমওয়ার্কটি ব্যবহারকারী বান্ধব হওয়ার পাশাপাশি মডেল ট্রেনিং এবং ডিপ্লয়মেন্টে কার্যকর হতে ডিজাইন করা হয়েছে। ফ্রেমওয়ার্কের ডিজাইন নিজেও ধারণাগতভাবে সহজ। আমরা গবেষকদের জন্য MLX সম্প্রসারণ এবং উন্নত করা সহজ করতে চাই, যাতে নতুন ধারণাগুলো দ্রুত পরীক্ষা করা যায়।

Apple Silicon ডিভাইসগুলিতে MLX এর মাধ্যমে LLMs গতি বৃদ্ধি পেতে পারে, এবং মডেলগুলি স্থানীয়ভাবে খুব সহজে চালানো যায়।

## **MLX ব্যবহার করে Phi-3-mini inference করা**

### **1. আপনার MLX পরিবেশ সেটআপ করুন**

1. Python 3.11.x
2. MLX লাইব্রেরি ইনস্টল করুন


```bash

pip install mlx-lm

```

### **2. MLX দিয়ে টার্মিনালে Phi-3-mini চালানো**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

ফলাফল (আমার পরিবেশ Apple M1 Max, 64GB) হলো

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.bn.png)

### **3. MLX দিয়ে টার্মিনালে Phi-3-mini কোয়ান্টাইজ করা**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** মডেলটি mlx_lm.convert এর মাধ্যমে কোয়ান্টাইজ করা যায়, এবং ডিফল্ট কোয়ান্টাইজেশন হল INT4। এই উদাহরণে Phi-3-mini কে INT4 এ কোয়ান্টাইজ করা হয়েছে

মডেলটি mlx_lm.convert দিয়ে কোয়ান্টাইজ করা যায়, এবং ডিফল্ট কোয়ান্টাইজেশন INT4। এই উদাহরণে Phi-3-mini কে INT4 এ কোয়ান্টাইজ করা হয়েছে। কোয়ান্টাইজেশনের পর এটি ডিফল্ট ডিরেক্টরি ./mlx_model এ সংরক্ষণ করা হবে।

আমরা টার্মিনাল থেকে MLX দিয়ে কোয়ান্টাইজ করা মডেলটি পরীক্ষা করতে পারি


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

ফলাফল হলো

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.bn.png)


### **4. Jupyter Notebook এ MLX দিয়ে Phi-3-mini চালানো**


![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.bn.png)

***Note:*** এই স্যাম্পলটি পড়ুন [click this link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **সামগ্রী**

1. Apple MLX Framework সম্পর্কে জানুন [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বতন্ত্র ভাষায়ই কর্তৃপক্ষপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।