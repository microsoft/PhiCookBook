<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:51:22+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "bn"
}
-->
**QLoRA দিয়ে Phi-3 ফাইন-টিউনিং**

Microsoft এর Phi-3 Mini ভাষা মডেল QLoRA (Quantum Low-Rank Adaptation) ব্যবহার করে ফাইন-টিউন করা হচ্ছে।

QLoRA কথোপকথনের বোঝাপড়া এবং প্রতিক্রিয়া উৎপাদন উন্নত করতে সাহায্য করবে।

transformers এবং bitsandbytes দিয়ে 4bits মডেল লোড করতে, আপনাকে accelerate এবং transformers সোর্স থেকে ইনস্টল করতে হবে এবং নিশ্চিত করতে হবে যে bitsandbytes লাইব্রেরির সর্বশেষ সংস্করণ আপনার কাছে রয়েছে।

**নমুনা**
- [এই নমুনা নোটবুক দিয়ে আরও জানুন](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning নমুনার উদাহরণ](../../../../code/03.Finetuning/FineTrainingScript.py)
- [LORA দিয়ে Hugging Face Hub Fine Tuning এর উদাহরণ](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [QLORA দিয়ে Hugging Face Hub Fine Tuning এর উদাহরণ](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**অস্বীকারোক্তি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে লক্ষ্য করুন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বতন্ত্র ভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনও ভুলবোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।