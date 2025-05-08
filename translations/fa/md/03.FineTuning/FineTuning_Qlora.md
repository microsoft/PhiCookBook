<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-07T13:14:50+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "fa"
}
-->
**تنظیم دقیق Phi-3 با QLoRA**

تنظیم دقیق مدل زبان Phi-3 Mini مایکروسافت با استفاده از [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA به بهبود درک مکالمه و تولید پاسخ کمک می‌کند.

برای بارگذاری مدل‌ها در 4 بیت با استفاده از transformers و bitsandbytes، باید accelerate و transformers را از سورس نصب کنید و مطمئن شوید که جدیدترین نسخه کتابخانه bitsandbytes را دارید.

**نمونه‌ها**
- [یادگیری بیشتر با این دفترچه نمونه](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [نمونه تنظیم دقیق پایتون](../../../../code/03.Finetuning/FineTrainingScript.py)
- [نمونه تنظیم دقیق در Hugging Face Hub با LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [نمونه تنظیم دقیق در Hugging Face Hub با QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه ماشینی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی اشتباهات یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا برداشت نادرستی که از استفاده از این ترجمه ناشی شود، نیستیم.