<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-03-27T15:10:59+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Qlora.md",
  "language_code": "fa"
}
-->
**تنظیم دقیق Phi-3 با QLoRA**

تنظیم دقیق مدل زبان Phi-3 Mini مایکروسافت با استفاده از [QLoRA (تطبیق کوانتومی با رتبه پایین)](https://github.com/artidoro/qlora).

QLoRA به بهبود درک مکالمه و تولید پاسخ کمک می‌کند.

برای بارگذاری مدل‌ها در حالت ۴ بیت با استفاده از transformers و bitsandbytes، باید accelerate و transformers را از منبع نصب کنید و مطمئن شوید که جدیدترین نسخه از کتابخانه bitsandbytes را دارید.

**نمونه‌ها**
- [اطلاعات بیشتر با این دفترچه نمونه](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [نمونه‌ای از اسکریپت تنظیم دقیق در پایتون](../../../../code/03.Finetuning/FineTrainingScript.py)
- [نمونه‌ای از تنظیم دقیق با Hugging Face Hub و LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [نمونه‌ای از تنظیم دقیق با Hugging Face Hub و QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت ترجمه را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نواقصی باشند. سند اصلی به زبان اصلی باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا برداشت‌های نادرست ناشی از استفاده از این ترجمه نداریم.