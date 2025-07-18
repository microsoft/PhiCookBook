<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-07-16T21:53:54+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "bn"
}
-->
# **Apple MLX Framework ব্যবহার করে Phi-3.5 কোয়ান্টাইজেশন**

MLX হলো Apple সিলিকনে মেশিন লার্নিং গবেষণার জন্য একটি অ্যারে ফ্রেমওয়ার্ক, যা Apple মেশিন লার্নিং গবেষণা থেকে এসেছে।

MLX মেশিন লার্নিং গবেষকদের জন্য মেশিন লার্নিং গবেষকরা ডিজাইন করেছেন। ফ্রেমওয়ার্কটি ব্যবহারকারী বান্ধব হওয়ার পাশাপাশি মডেল ট্রেনিং এবং ডিপ্লয়মেন্টে দক্ষ হওয়ার জন্য তৈরি। ফ্রেমওয়ার্কের ডিজাইন নিজেও ধারণাগতভাবে সহজ। আমরা গবেষকদের জন্য MLX সম্প্রসারণ এবং উন্নত করা সহজ করতে চাই, যাতে তারা দ্রুত নতুন ধারণা পরীক্ষা করতে পারেন।

Apple সিলিকন ডিভাইসগুলোতে MLX এর মাধ্যমে LLM গুলো দ্রুততর করা যায়, এবং মডেলগুলো স্থানীয়ভাবে খুব সহজে চালানো যায়।

এখন Apple MLX Framework Phi-3.5-Instruct(**Apple MLX Framework support**), Phi-3.5-Vision(**MLX-VLM Framework support**), এবং Phi-3.5-MoE(**Apple MLX Framework support**) এর কোয়ান্টাইজেশন রূপান্তর সমর্থন করে। চলুন পরবর্তী ধাপে চেষ্টা করি:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 Apple MLX সহ Phi-3.5 এর নমুনা**

| ল্যাবস    | পরিচিতি | যান |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Apple MLX ফ্রেমওয়ার্ক দিয়ে Phi-3.5 Instruct ব্যবহার করার পদ্ধতি শিখুন   |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Apple MLX ফ্রেমওয়ার্ক দিয়ে ছবি বিশ্লেষণের জন্য Phi-3.5 Vision ব্যবহার শিখুন     |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Apple MLX ফ্রেমওয়ার্ক দিয়ে Phi-3.5 MoE ব্যবহার করার পদ্ধতি শিখুন  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **রিসোর্সসমূহ**

1. Apple MLX Framework সম্পর্কে জানুন [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub রিপোজিটরি [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub রিপোজিটরি [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।