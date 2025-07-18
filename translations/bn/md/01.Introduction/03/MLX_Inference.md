<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-07-16T21:02:00+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "bn"
}
-->
# **Apple MLX Framework দিয়ে Phi-3 ইনফারেন্স**

## **MLX Framework কী?**

MLX হলো Apple সিলিকনে মেশিন লার্নিং গবেষণার জন্য একটি অ্যারে ফ্রেমওয়ার্ক, যা Apple মেশিন লার্নিং গবেষণা থেকে এসেছে।

MLX মেশিন লার্নিং গবেষকদের জন্য মেশিন লার্নিং গবেষকরা ডিজাইন করেছেন। ফ্রেমওয়ার্কটি ব্যবহারকারীর জন্য সহজবোধ্য হলেও, মডেল ট্রেনিং ও ডিপ্লয়মেন্টে কার্যকরী। ফ্রেমওয়ার্কের ডিজাইন নিজেও ধারণাগতভাবে সরল। আমরা চাই গবেষকরা সহজেই MLX সম্প্রসারিত ও উন্নত করতে পারেন, যাতে দ্রুত নতুন ধারণা পরীক্ষা করা যায়।

Apple Silicon ডিভাইসে MLX এর মাধ্যমে LLM গুলো দ্রুত চালানো যায়, এবং মডেলগুলো স্থানীয়ভাবে খুবই সুবিধাজনকভাবে রান করানো সম্ভব।

## **MLX ব্যবহার করে Phi-3-mini ইনফারেন্স**

### **১. আপনার MLX পরিবেশ সেটআপ করুন**

1. Python 3.11.x
2. MLX লাইব্রেরি ইনস্টল করুন

```bash

pip install mlx-lm

```

### **২. টার্মিনালে MLX দিয়ে Phi-3-mini চালানো**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

ফলাফল (আমার পরিবেশ Apple M1 Max, 64GB) হলো

![Terminal](../../../../../translated_images/01.5cf57df8f7407cf9281c0237f4e69c3728b8817253aad0835d14108b07c83c88.bn.png)

### **৩. টার্মিনালে MLX দিয়ে Phi-3-mini কোয়ান্টাইজ করা**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** মডেল mlx_lm.convert দিয়ে কোয়ান্টাইজ করা যায়, এবং ডিফল্ট কোয়ান্টাইজেশন INT4। এই উদাহরণে Phi-3-mini কে INT4 তে কোয়ান্টাইজ করা হয়েছে।

মডেল mlx_lm.convert দিয়ে কোয়ান্টাইজ করা যায়, এবং ডিফল্ট কোয়ান্টাইজেশন INT4। এই উদাহরণে Phi-3-mini কে INT4 তে কোয়ান্টাইজ করা হয়েছে। কোয়ান্টাইজেশনের পর এটি ডিফল্ট ডিরেক্টরি ./mlx_model এ সংরক্ষিত হবে।

আমরা টার্মিনাল থেকে MLX দিয়ে কোয়ান্টাইজ করা মডেল পরীক্ষা করতে পারি

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

ফলাফল হলো

![INT4](../../../../../translated_images/02.7b188681a8eadbc111aba8d8006e4b3671788947a99a46329261e169dd2ec29f.bn.png)

### **৪. Jupyter Notebook এ MLX দিয়ে Phi-3-mini চালানো**

![Notebook](../../../../../translated_images/03.b9705a3a5aaa89f9eb0ca04c1a4565dfe4a5e8cc68604227d2eab149fef1d3c7.bn.png)

***Note:*** এই স্যাম্পলটি পড়ুন [এই লিঙ্কে ক্লিক করুন](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **রিসোর্সসমূহ**

1. Apple MLX Framework সম্পর্কে জানুন [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub রিপোজিটরি [https://github.com/ml-explore](https://github.com/ml-explore)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।