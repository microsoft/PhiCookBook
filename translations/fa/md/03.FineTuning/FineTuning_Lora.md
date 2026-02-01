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

ابتدا کتابخانه‌های لازم مانند datasets، transformers، peft، trl و torch را وارد کنید.  
برای پیگیری روند آموزش، لاگ‌گیری را تنظیم کنید.

می‌توانید برخی لایه‌ها را با جایگزین کردن آن‌ها با نمونه‌های پیاده‌سازی شده در loralib تطبیق دهید. در حال حاضر فقط nn.Linear، nn.Embedding و nn.Conv2d پشتیبانی می‌شوند. همچنین MergedLinear را برای مواردی که یک nn.Linear نمایانگر بیش از یک لایه است، مانند برخی پیاده‌سازی‌های پروجکشن qkv توجه (برای جزئیات بیشتر به نکات اضافی مراجعه کنید) پشتیبانی می‌کنیم.

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

هنگام ذخیره یک نقطه بازگشت (checkpoint)، یک state_dict تولید کنید که فقط شامل پارامترهای LoRA باشد.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

هنگام بارگذاری checkpoint با استفاده از load_state_dict، حتماً strict=False تنظیم شود.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

اکنون آموزش می‌تواند به روال معمول ادامه یابد.

**ابرپارامترها**

دو دیکشنری تعریف کنید: training_config و peft_config. training_config شامل ابرپارامترهای آموزش مانند نرخ یادگیری، اندازه بچ و تنظیمات لاگ‌گیری است.

peft_config پارامترهای مرتبط با LoRA مانند rank، dropout و نوع وظیفه را مشخص می‌کند.

**بارگذاری مدل و توکنایزر**

مسیر مدل پیش‌آموزش دیده Phi-3 را مشخص کنید (مثلاً "microsoft/Phi-3-mini-4k-instruct"). تنظیمات مدل شامل استفاده از کش، نوع داده (bfloat16 برای دقت ترکیبی) و پیاده‌سازی توجه را پیکربندی کنید.

**آموزش**

مدل Phi-3 را با استفاده از مجموعه داده دستور گفتگوی سفارشی تنظیم دقیق کنید. از تنظیمات LoRA در peft_config برای تطبیق بهینه استفاده کنید. پیشرفت آموزش را با استراتژی لاگ‌گیری مشخص شده دنبال کنید.  
ارزیابی و ذخیره: مدل تنظیم شده را ارزیابی کنید.  
در طول آموزش، نقاط بازگشت را برای استفاده‌های بعدی ذخیره کنید.

**نمونه‌ها**  
- [یادگیری بیشتر با این دفترچه نمونه](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [نمونه تنظیم دقیق پایتون](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [نمونه تنظیم دقیق Hugging Face Hub با LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [نمونه کارت مدل Hugging Face - نمونه تنظیم دقیق LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [نمونه تنظیم دقیق Hugging Face Hub با QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.