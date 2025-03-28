<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-03-27T03:44:31+00:00",
  "source_file": "code\\03.Finetuning\\olive-ort-example\\README.md",
  "language_code": "fa"
}
-->
# تنظیم Phi3 با استفاده از Olive

در این مثال شما از Olive برای انجام موارد زیر استفاده خواهید کرد:

1. تنظیم یک آداپتور LoRA برای دسته‌بندی عبارات به چهار حالت: غم، شادی، ترس، شگفتی.
1. ادغام وزن‌های آداپتور با مدل پایه.
1. بهینه‌سازی و کوانتیزه کردن مدل به `int4`.

همچنین به شما نشان خواهیم داد که چگونه می‌توانید از مدل تنظیم‌شده با استفاده از API تولید ONNX Runtime (ORT) نتیجه‌گیری کنید.

> **⚠️ برای تنظیم، نیاز به یک GPU مناسب دارید - برای مثال، A10، V100، A100.**

## 💾 نصب

یک محیط مجازی جدید پایتون ایجاد کنید (برای مثال با استفاده از `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

سپس، Olive و وابستگی‌های لازم برای یک فرآیند تنظیم را نصب کنید:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 تنظیم Phi3 با استفاده از Olive
[فایل پیکربندی Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) شامل یک *workflow* با *گذرها*ی زیر است:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

در سطح بالا، این workflow موارد زیر را انجام می‌دهد:

1. تنظیم Phi3 (برای ۱۵۰ مرحله، که می‌توانید آن را تغییر دهید) با استفاده از داده‌های [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. ادغام وزن‌های آداپتور LoRA با مدل پایه. این کار به شما یک مصنوع مدل در قالب ONNX می‌دهد.
1. Model Builder مدل را برای ONNX runtime بهینه‌سازی کرده *و* مدل را به `int4` کوانتیزه می‌کند.

برای اجرای این workflow، دستور زیر را اجرا کنید:

```bash
olive run --config phrase-classification.json
```

پس از اتمام Olive، مدل Phi3 تنظیم‌شده و بهینه‌شده `int4` شما در مسیر زیر در دسترس خواهد بود: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 ادغام Phi3 تنظیم‌شده در برنامه شما

برای اجرای برنامه:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

این پاسخ باید یک کلمه باشد که دسته‌بندی عبارت را مشخص کند (غم/شادی/ترس/شگفتی).

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل اشتباهات یا نواقصی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.