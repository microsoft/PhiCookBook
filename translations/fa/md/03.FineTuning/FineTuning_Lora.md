<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-03-27T14:01:53+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Lora.md",
  "language_code": "fa"
}
-->
# **تنظیم دقیق Phi-3 با Lora**

تنظیم دقیق مدل زبان Phi-3 Mini مایکروسافت با استفاده از [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) روی یک مجموعه داده سفارشی برای دستورالعمل‌های چت.

LoRA به بهبود درک مکالمه و تولید پاسخ کمک می‌کند.

## راهنمای گام‌به‌گام برای تنظیم دقیق Phi-3 Mini:

**وارد کردن کتابخانه‌ها و تنظیمات اولیه**

نصب loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

ابتدا کتابخانه‌های ضروری مانند datasets، transformers، peft، trl و torch را وارد کنید.  
برای پیگیری فرآیند آموزش، لاگ‌گیری را تنظیم کنید.

می‌توانید برخی از لایه‌ها را با جایگزینی آن‌ها با نسخه‌های پیاده‌سازی‌شده در loralib تطبیق دهید. در حال حاضر تنها nn.Linear، nn.Embedding و nn.Conv2d پشتیبانی می‌شوند. همچنین یک MergedLinear برای مواردی که یک nn.Linear نماینده چندین لایه است، مانند برخی پیاده‌سازی‌های پیش‌بینی qkv در توجه، پشتیبانی می‌شود (برای اطلاعات بیشتر به یادداشت‌های اضافی مراجعه کنید).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

وارد کردن loralib به عنوان lora:

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

پیش از شروع حلقه آموزشی، تنها پارامترهای LoRA را به‌عنوان قابل آموزش علامت‌گذاری کنید.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

هنگام ذخیره یک نقطه بررسی (checkpoint)، یک state_dict تولید کنید که فقط شامل پارامترهای LoRA باشد.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

هنگام بارگذاری یک نقطه بررسی با استفاده از load_state_dict، مطمئن شوید که strict=False تنظیم شده باشد.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

اکنون آموزش می‌تواند به صورت معمول ادامه یابد.

**ابرپارامترها**

دو دیکشنری تعریف کنید: training_config و peft_config.  
training_config شامل ابرپارامترهایی برای آموزش است، مانند نرخ یادگیری، اندازه دسته، و تنظیمات لاگ‌گیری.

peft_config پارامترهای مرتبط با LoRA مانند rank، dropout و نوع وظیفه را مشخص می‌کند.

**بارگذاری مدل و توکنایزر**

مسیر مدل از پیش‌آموزش‌دیده Phi-3 را مشخص کنید (برای مثال، "microsoft/Phi-3-mini-4k-instruct").  
تنظیمات مدل را پیکربندی کنید، از جمله استفاده از کش، نوع داده (bfloat16 برای دقت ترکیبی) و پیاده‌سازی توجه.

**آموزش**

مدل Phi-3 را با استفاده از مجموعه داده سفارشی برای دستورالعمل‌های چت تنظیم دقیق کنید.  
از تنظیمات LoRA در peft_config برای تطبیق کارآمد استفاده کنید.  
پیشرفت آموزش را با استفاده از استراتژی لاگ‌گیری مشخص‌شده نظارت کنید.

**ارزیابی و ذخیره‌سازی:**  
مدل تنظیم دقیق‌شده را ارزیابی کنید.  
در طول آموزش، نقاط بررسی را برای استفاده بعدی ذخیره کنید.

**نمونه‌ها**
- [اطلاعات بیشتر با این دفترچه نمونه](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [نمونه‌ای از اسکریپت پایتون برای تنظیم دقیق](../../../../code/03.Finetuning/FineTrainingScript.py)
- [نمونه‌ای از تنظیم دقیق در Hugging Face Hub با LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [نمونه کارت مدل Hugging Face - تنظیم دقیق با LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [نمونه‌ای از تنظیم دقیق در Hugging Face Hub با QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادقتی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.