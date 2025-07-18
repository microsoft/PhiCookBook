<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:17:50+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "bn"
}
-->
**Fine-tuning Phi-3 with QLoRA**

Microsoft-এর Phi-3 Mini ভাষা মডেলটি [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) ব্যবহার করে ফাইন-টিউন করা হচ্ছে।

QLoRA কথোপকথনের বোঝাপড়া এবং প্রতিক্রিয়া তৈরিতে উন্নতি করতে সাহায্য করবে।

transformers এবং bitsandbytes ব্যবহার করে 4bits-এ মডেল লোড করতে, আপনাকে accelerate এবং transformers সোর্স থেকে ইনস্টল করতে হবে এবং নিশ্চিত করতে হবে যে আপনার কাছে bitsandbytes লাইব্রেরির সর্বশেষ সংস্করণ রয়েছে।

**Samples**
- [এই স্যাম্পল নোটবুক দিয়ে আরও জানুন](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning স্যাম্পলের উদাহরণ](../../../../code/03.Finetuning/FineTrainingScript.py)
- [LORA দিয়ে Hugging Face Hub Fine Tuning এর উদাহরণ](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [QLORA দিয়ে Hugging Face Hub Fine Tuning এর উদাহরণ](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।