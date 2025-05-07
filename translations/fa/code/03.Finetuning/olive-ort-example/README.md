<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-07T15:17:37+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "fa"
}
-->
# ریزتنظیم Phi3 با استفاده از Olive

در این مثال از Olive استفاده خواهید کرد برای:

1. ریزتنظیم یک آداپتور LoRA برای دسته‌بندی عبارات به Sad، Joy، Fear، Surprise.
1. ادغام وزن‌های آداپتور در مدل پایه.
1. بهینه‌سازی و کوانتیزه کردن مدل به صورت `int4`.

همچنین نحوه استنتاج مدل ریزتنظیم شده با استفاده از ONNX Runtime (ORT) Generate API را نشان خواهیم داد.

> **⚠️ برای ریزتنظیم، نیاز به یک GPU مناسب دارید - مثلاً A10، V100، A100.**

## 💾 نصب

یک محیط مجازی پایتون جدید بسازید (مثلاً با استفاده از `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

سپس Olive و وابستگی‌های مربوط به جریان کاری ریزتنظیم را نصب کنید:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 ریزتنظیم Phi3 با استفاده از Olive
[فایل پیکربندی Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) شامل یک *جریان کاری* با *گذرها*ی زیر است:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

در سطح کلی، این جریان کاری:

1. Phi3 را برای ۱۵۰ مرحله (که می‌توانید تغییر دهید) با استفاده از داده‌های [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) ریزتنظیم می‌کند.
1. وزن‌های آداپتور LoRA را در مدل پایه ادغام می‌کند. این به شما یک مدل واحد در فرمت ONNX می‌دهد.
1. ModelBuilder مدل را برای ONNX runtime بهینه‌سازی می‌کند *و* مدل را به صورت `int4` کوانتیزه می‌کند.

برای اجرای جریان کاری، دستور زیر را اجرا کنید:

```bash
olive run --config phrase-classification.json
```

وقتی Olive کارش را تمام کرد، مدل ریزتنظیم شده و بهینه‌شده `int4` شما در مسیر `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model` در دسترس است.

## 🧑‍💻 ادغام Phi3 ریزتنظیم شده در برنامه شما

برای اجرای برنامه:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

این پاسخ باید یک کلمه برای دسته‌بندی عبارت باشد (Sad/Joy/Fear/Surprise).

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نواقصی باشند. سند اصلی به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا برداشت نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.