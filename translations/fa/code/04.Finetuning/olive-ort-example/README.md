<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-03-27T04:02:54+00:00",
  "source_file": "code\\04.Finetuning\\olive-ort-example\\README.md",
  "language_code": "fa"
}
-->
# تنظیم دقیق Phi3 با استفاده از Olive

در این مثال، شما از Olive برای انجام موارد زیر استفاده خواهید کرد:

1. تنظیم دقیق یک LoRA adapter برای دسته‌بندی عبارات به غم، شادی، ترس، شگفتی.
1. ادغام وزن‌های آداپتر در مدل پایه.
1. بهینه‌سازی و کمینه‌سازی مدل به `int4`.

همچنین نحوه استفاده از مدل تنظیم‌شده برای استنتاج با استفاده از API تولید ONNX Runtime (ORT) را نشان خواهیم داد.

> **⚠️ برای تنظیم دقیق، باید یک GPU مناسب در دسترس داشته باشید - به عنوان مثال، A10، V100، A100.**

## 💾 نصب

یک محیط مجازی جدید برای Python ایجاد کنید (برای مثال، با استفاده از `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

سپس Olive و وابستگی‌های لازم برای جریان کاری تنظیم دقیق را نصب کنید:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 تنظیم دقیق Phi3 با استفاده از Olive

[فایل تنظیمات Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) شامل یک *جریان کاری* با *مراحل* زیر است:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

در سطح کلی، این جریان کاری موارد زیر را انجام خواهد داد:

1. تنظیم دقیق Phi3 (برای 150 مرحله، که می‌توانید تغییر دهید) با استفاده از داده‌های [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. ادغام وزن‌های آداپتر LoRA در مدل پایه. این کار یک اثر هنری مدل واحد در قالب ONNX ایجاد خواهد کرد.
1. Model Builder مدل را برای زمان اجرای ONNX بهینه‌سازی کرده و همچنین مدل را به `int4` کمینه‌سازی خواهد کرد.

برای اجرای جریان کاری، دستور زیر را اجرا کنید:

```bash
olive run --config phrase-classification.json
```

پس از تکمیل Olive، مدل تنظیم‌شده Phi3 بهینه‌سازی‌شده `int4` در مسیر زیر در دسترس خواهد بود:  
`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 ادغام Phi3 تنظیم‌شده در برنامه شما

برای اجرای برنامه:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

پاسخ باید یک کلمه واحد برای دسته‌بندی عبارت باشد (غم/شادی/ترس/شگفتی).

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی خود باید به‌عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه انسانی حرفه‌ای توصیه می‌شود. ما مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.