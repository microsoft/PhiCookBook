<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:02:28+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "bn"
}
-->
# Olive ব্যবহার করে Phi3 ফাইন-টিউন করুন

এই উদাহরণে আপনি Olive ব্যবহার করে:

1. একটি LoRA অ্যাডাপ্টার ফাইন-টিউন করবেন যাতে বাক্যাংশগুলোকে Sad, Joy, Fear, Surprise হিসেবে শ্রেণীবদ্ধ করা যায়।
1. অ্যাডাপ্টারের ওজনগুলো বেস মডেলের সাথে মার্জ করবেন।
1. মডেলটিকে `int4` এ অপ্টিমাইজ এবং কোয়ান্টাইজ করবেন।

আমরা আপনাকে দেখাবো কিভাবে ONNX Runtime (ORT) Generate API ব্যবহার করে ফাইন-টিউন করা মডেল থেকে ইনফারেন্স করবেন।

> **⚠️ ফাইন-টিউন করার জন্য, আপনার কাছে একটি উপযুক্ত GPU থাকা উচিত - যেমন A10, V100, A100।**

## 💾 ইনস্টল করুন

একটি নতুন Python ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন (উদাহরণস্বরূপ, `conda` ব্যবহার করে):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

এরপর, Olive এবং ফাইন-টিউনিং ওয়ার্কফ্লোর জন্য প্রয়োজনীয় ডিপেন্ডেন্সিগুলো ইনস্টল করুন:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive ব্যবহার করে Phi3 ফাইন-টিউন করুন
[Olive কনফিগারেশন ফাইল](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) একটি *ওয়ার্কফ্লো* ধারণ করে যার মধ্যে নিম্নলিখিত *পাস* রয়েছে:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

উচ্চ স্তরে, এই ওয়ার্কফ্লোটি করবে:

1. Phi3 কে ফাইন-টিউন করবে (১৫০ ধাপের জন্য, যা আপনি পরিবর্তন করতে পারেন) [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) ডেটা ব্যবহার করে।
1. LoRA অ্যাডাপ্টারের ওজনগুলো বেস মডেলের সাথে মার্জ করবে। এর ফলে ONNX ফরম্যাটে একটি একক মডেল আর্টিফ্যাক্ট পাবেন।
1. Model Builder মডেলটিকে ONNX runtime এর জন্য অপ্টিমাইজ করবে *এবং* মডেলটিকে `int4` এ কোয়ান্টাইজ করবে।

ওয়ার্কফ্লো চালানোর জন্য, রান করুন:

```bash
olive run --config phrase-classification.json
```

Olive সম্পন্ন হলে, আপনার অপ্টিমাইজ করা `int4` ফাইন-টিউন করা Phi3 মডেলটি পাওয়া যাবে: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model` এ।

## 🧑‍💻 ফাইন-টিউন করা Phi3 কে আপনার অ্যাপ্লিকেশনে ইন্টিগ্রেট করুন

অ্যাপ চালানোর জন্য:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

এই রেসপন্সটি হবে বাক্যাংশের একটি একক শব্দের শ্রেণীবিভাগ (Sad/Joy/Fear/Surprise)।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।