<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:16:52+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "fa"
}
-->
**تنظیم دقیق Phi-3 با QLoRA**

تنظیم دقیق مدل زبان Phi-3 Mini مایکروسافت با استفاده از [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA به بهبود درک مکالمه و تولید پاسخ کمک می‌کند.

برای بارگذاری مدل‌ها در حالت ۴ بیت با استفاده از transformers و bitsandbytes، باید accelerate و transformers را از سورس نصب کنید و مطمئن شوید که آخرین نسخه کتابخانه bitsandbytes را دارید.

**نمونه‌ها**
- [با این دفترچه نمونه بیشتر یاد بگیرید](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [نمونه‌ای از تنظیم دقیق پایتون](../../../../code/03.Finetuning/FineTrainingScript.py)
- [نمونه‌ای از تنظیم دقیق در Hugging Face Hub با LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [نمونه‌ای از تنظیم دقیق در Hugging Face Hub با QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده از این ترجمه ناشی شود، نیستیم.