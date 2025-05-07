<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-07T13:29:58+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "fa"
}
-->
# **تنظیم دقیق Phi-3 با Lora**

تنظیم دقیق مدل زبان Phi-3 Mini مایکروسافت با استفاده از [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) روی یک مجموعه داده دستور گفتگوی سفارشی.

LORA به بهبود درک مکالمه و تولید پاسخ کمک می‌کند.

## راهنمای گام به گام برای تنظیم دقیق Phi-3 Mini:

**وارد کردن و راه‌اندازی**

نصب loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

ابتدا کتابخانه‌های مورد نیاز مانند datasets، transformers، peft، trl و torch را وارد کنید.  
برای پیگیری روند آموزش، لاگ‌گیری را تنظیم کنید.

می‌توانید برخی لایه‌ها را با جایگزین کردن آن‌ها با نمونه‌های پیاده‌سازی‌شده در loralib تطبیق دهید. در حال حاضر فقط nn.Linear، nn.Embedding و nn.Conv2d پشتیبانی می‌شوند. همچنین MergedLinear را برای مواقعی که یک nn.Linear نماینده بیش از یک لایه است، مانند برخی پیاده‌سازی‌های projection qkv در attention، پشتیبانی می‌کنیم (برای جزئیات بیشتر به یادداشت‌های اضافی مراجعه کنید).

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

قبل از شروع حلقه آموزش، فقط پارامترهای LoRA را به عنوان قابل آموزش علامت‌گذاری کنید.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

هنگام ذخیره یک checkpoint، یک state_dict تولید کنید که فقط شامل پارامترهای LoRA باشد.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

هنگام بارگذاری checkpoint با استفاده از load_state_dict، حتماً مقدار strict=False را تنظیم کنید.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

اکنون آموزش می‌تواند به روال معمول ادامه یابد.

**ابرپارامترها**

دو دیکشنری تعریف کنید: training_config و peft_config. training_config شامل ابرپارامترهای آموزش مانند نرخ یادگیری، اندازه دسته و تنظیمات لاگ‌گیری است.

peft_config پارامترهای مربوط به LoRA مانند رتبه، dropout و نوع کار را مشخص می‌کند.

**بارگذاری مدل و توکنایزر**

مسیر مدل پیش‌آموزش‌دیده Phi-3 را مشخص کنید (مثلاً "microsoft/Phi-3-mini-4k-instruct"). تنظیمات مدل شامل استفاده از کش، نوع داده (bfloat16 برای دقت ترکیبی) و پیاده‌سازی attention را پیکربندی کنید.

**آموزش**

مدل Phi-3 را با استفاده از مجموعه داده دستور گفتگوی سفارشی تنظیم دقیق کنید. از تنظیمات LoRA در peft_config برای تطبیق کارآمد استفاده کنید. پیشرفت آموزش را با استراتژی لاگ‌گیری مشخص شده نظارت کنید.  
ارزیابی و ذخیره: مدل تنظیم‌شده را ارزیابی کنید.  
در حین آموزش، checkpoints را برای استفاده‌های بعدی ذخیره کنید.

**نمونه‌ها**  
- [مطالعه بیشتر با این دفترچه نمونه](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [نمونه‌ای از تنظیم دقیق پایتون](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [نمونه‌ای از تنظیم دقیق Hugging Face Hub با LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [نمونه کارت مدل Hugging Face - نمونه تنظیم دقیق LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [نمونه‌ای از تنظیم دقیق Hugging Face Hub با QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه ماشینی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی اشتباهات یا نواقصی باشند. سند اصلی به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.