<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:01:21+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "fa"
}
-->
# تنظیم دقیق Phi3 با استفاده از Olive

در این مثال، شما با Olive موارد زیر را انجام خواهید داد:

1. تنظیم دقیق یک آداپتور LoRA برای دسته‌بندی عبارات به چهار دسته غمگین، شادی، ترس، تعجب.
1. ادغام وزن‌های آداپتور در مدل پایه.
1. بهینه‌سازی و کمّی‌سازی مدل به صورت `int4`.

همچنین نحوه استنتاج مدل تنظیم دقیق شده با استفاده از ONNX Runtime (ORT) Generate API را به شما نشان خواهیم داد.

> **⚠️ برای تنظیم دقیق، نیاز به یک GPU مناسب دارید - مثلاً A10، V100، A100.**

## 💾 نصب

یک محیط مجازی جدید پایتون ایجاد کنید (برای مثال با استفاده از `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

سپس Olive و وابستگی‌های مربوط به جریان کاری تنظیم دقیق را نصب کنید:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 تنظیم دقیق Phi3 با استفاده از Olive
[فایل پیکربندی Olive](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) شامل یک *جریان کاری* با *مراحل* زیر است:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

در سطح کلی، این جریان کاری موارد زیر را انجام می‌دهد:

1. تنظیم دقیق Phi3 (برای ۱۵۰ مرحله که قابل تغییر است) با استفاده از داده‌های [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. ادغام وزن‌های آداپتور LoRA در مدل پایه. این کار یک مدل واحد در فرمت ONNX به شما می‌دهد.
1. Model Builder مدل را برای اجرای ONNX بهینه‌سازی کرده و مدل را به صورت `int4` کمّی‌سازی می‌کند.

برای اجرای جریان کاری، دستور زیر را اجرا کنید:

```bash
olive run --config phrase-classification.json
```

پس از اتمام Olive، مدل تنظیم دقیق شده و بهینه‌شده `int4` شما در مسیر زیر در دسترس است: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 ادغام Phi3 تنظیم دقیق شده در برنامه شما

برای اجرای برنامه:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

پاسخ باید یک کلمه باشد که دسته‌بندی عبارت را نشان دهد (غمگین/شادی/ترس/تعجب).

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.