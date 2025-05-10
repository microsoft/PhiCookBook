<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-09T13:41:18+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "bn"
}
-->
# **Apple MLX Framework ব্যবহার করে Phi-3.5 কোয়ান্টাইজেশন**

MLX হলো Apple সিলিকন ভিত্তিক মেশিন লার্নিং গবেষণার জন্য একটি অ্যারে ফ্রেমওয়ার্ক, যা Apple মেশিন লার্নিং গবেষণা থেকে এসেছে।

MLX মেশিন লার্নিং গবেষকদের জন্য মেশিন লার্নিং গবেষক দ্বারা ডিজাইন করা হয়েছে। ফ্রেমওয়ার্কটি ব্যবহারকারীর জন্য সহজবোধ্য হতে তৈরি, তবে মডেল প্রশিক্ষণ এবং ডিপ্লয়মেন্টে দক্ষ। ফ্রেমওয়ার্কের ডিজাইন নিজেই ধারণাগতভাবে সরল। আমরা গবেষকদের জন্য MLX সম্প্রসারণ এবং উন্নত করা সহজ করতে চাই, যাতে দ্রুত নতুন ধারণা অনুসন্ধান করা যায়।

Apple সিলিকন ডিভাইসে MLX-এর মাধ্যমে LLMs গতি বাড়ানো যায়, এবং মডেলগুলো স্থানীয়ভাবে খুবই সুবিধাজনকভাবে চালানো যায়।

এখন Apple MLX Framework Phi-3.5-Instruct(**Apple MLX Framework support**), Phi-3.5-Vision(**MLX-VLM Framework support**) এবং Phi-3.5-MoE(**Apple MLX Framework support**) এর কোয়ান্টাইজেশন রূপান্তর সমর্থন করে। চলুন পরবর্তী ধাপে চেষ্টা করি:

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



### **🤖 Apple MLX সহ Phi-3.5 এর নমুনাসমূহ**

| ল্যাবস    | পরিচিতি | যান |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Apple MLX ফ্রেমওয়ার্কের সাথে Phi-3.5 Instruct ব্যবহারের পদ্ধতি শিখুন  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Apple MLX ফ্রেমওয়ার্কের মাধ্যমে Phi-3.5 Vision ব্যবহার করে ছবি বিশ্লেষণ শিখুন  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (moE)   | Apple MLX ফ্রেমওয়ার্কের সাথে Phi-3.5 MoE ব্যবহারের পদ্ধতি শিখুন  |  [Go](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |


## **সংশ্লিষ্ট তথ্য**

1. Apple MLX Framework সম্পর্কে জানুন [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. Apple MLX GitHub রিপোজিটরি [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. MLX-VLM GitHub রিপোজিটরি [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা সঠিকতার জন্য চেষ্টা করি, তবে দয়া করে জানুন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহার থেকে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।