<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:29:53+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "bn"
}
-->
# **Lora দিয়ে Phi-3 ফাইন-টিউনিং**

Microsoft-এর Phi-3 Mini ভাষা মডেলকে [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) ব্যবহার করে একটি কাস্টম চ্যাট ইনস্ট্রাকশন ডেটাসেটে ফাইন-টিউন করা হচ্ছে।

LoRA কথোপকথনের বোঝাপড়া এবং প্রতিক্রিয়া তৈরিতে উন্নতি করতে সাহায্য করবে।

## Phi-3 Mini ফাইন-টিউন করার ধাপে ধাপে গাইড:

**ইম্পোর্ট এবং সেটআপ**

loralib ইনস্টল করা

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

প্রয়োজনীয় লাইব্রেরি যেমন datasets, transformers, peft, trl, এবং torch ইম্পোর্ট করে শুরু করুন।  
ট্রেনিং প্রক্রিয়া ট্র্যাক করার জন্য লগিং সেটআপ করুন।

আপনি কিছু লেয়ারকে loralib-এ ইমপ্লিমেন্ট করা সমতুল্য দিয়ে প্রতিস্থাপন করে অ্যাডাপ্ট করতে পারেন। আপাতত আমরা nn.Linear, nn.Embedding, এবং nn.Conv2d সাপোর্ট করি। এছাড়া MergedLinear সাপোর্ট করি যেখানে একটি nn.Linear একাধিক লেয়ার প্রতিনিধিত্ব করে, যেমন কিছু attention qkv projection ইমপ্লিমেন্টেশনে (বিস্তারিত জানতে Additional Notes দেখুন)।

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

ট্রেনিং লুপ শুরু হওয়ার আগে, শুধুমাত্র LoRA প্যারামিটারগুলোকে ট্রেনেবল হিসেবে চিহ্নিত করুন।

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

চেকপয়েন্ট সেভ করার সময়, এমন একটি state_dict তৈরি করুন যাতে শুধুমাত্র LoRA প্যারামিটার থাকে।

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dict ব্যবহার করে চেকপয়েন্ট লোড করার সময় strict=False সেট করতে ভুলবেন না।

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

এখন ট্রেনিং স্বাভাবিকভাবে চালিয়ে যেতে পারেন।

**হাইপারপ্যারামিটারস**

দুটি ডিকশনারি ডিফাইন করুন: training_config এবং peft_config। training_config-এ ট্রেনিংয়ের জন্য প্রয়োজনীয় হাইপারপ্যারামিটার যেমন লার্নিং রেট, ব্যাচ সাইজ, এবং লগিং সেটিংস থাকবে।

peft_config-এ LoRA সম্পর্কিত প্যারামিটার যেমন rank, dropout, এবং টাস্ক টাইপ উল্লেখ করুন।

**মডেল এবং টোকেনাইজার লোডিং**

প্রি-ট্রেইনড Phi-3 মডেলের পাথ নির্দিষ্ট করুন (যেমন "microsoft/Phi-3-mini-4k-instruct")। মডেল সেটিংস কনফিগার করুন, যেমন ক্যাশ ব্যবহার, ডেটা টাইপ (মিশ্র প্রিসিশনের জন্য bfloat16), এবং attention ইমপ্লিমেন্টেশন।

**ট্রেনিং**

কাস্টম চ্যাট ইনস্ট্রাকশন ডেটাসেট ব্যবহার করে Phi-3 মডেল ফাইন-টিউন করুন। দক্ষ অ্যাডাপ্টেশনের জন্য peft_config থেকে LoRA সেটিংস ব্যবহার করুন। নির্দিষ্ট লগিং স্ট্র্যাটেজি দিয়ে ট্রেনিং প্রগ্রেস মনিটর করুন।  
মূল্যায়ন এবং সেভিং: ফাইন-টিউন করা মডেল মূল্যায়ন করুন।  
ট্রেনিং চলাকালীন চেকপয়েন্ট সেভ করুন পরবর্তীতে ব্যবহারের জন্য।

**নমুনা**
- [এই স্যাম্পল নোটবুক দিয়ে আরও জানুন](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Python FineTuning Sample এর উদাহরণ](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Hugging Face Hub এ LORA দিয়ে Fine Tuning এর উদাহরণ](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Hugging Face Model Card - LORA Fine Tuning Sample এর উদাহরণ](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Hugging Face Hub এ QLORA দিয়ে Fine Tuning এর উদাহরণ](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।