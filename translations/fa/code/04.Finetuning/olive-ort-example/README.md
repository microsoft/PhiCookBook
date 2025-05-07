<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-07T15:14:57+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "fa"
}
-->
# ریزتنظیم Phi3 با استفاده از Olive

در این مثال از Olive استفاده خواهید کرد تا:

1. یک آداپتور LoRA را برای طبقه‌بندی عبارات به دسته‌های غمگین، شادی، ترس، تعجب ریزتنظیم کنید.
1. وزن‌های آداپتور را در مدل پایه ادغام کنید.
1. مدل را بهینه‌سازی و به قالب `int4` کمّی‌سازی کنید.

همچنین نحوه استنتاج مدل ریزتنظیم‌شده با استفاده از ONNX Runtime (ORT) Generate API را به شما نشان می‌دهیم.

> **⚠️ برای ریزتنظیم، نیاز به یک GPU مناسب دارید - برای مثال A10، V100، A100.**

## 💾 نصب

یک محیط مجازی پایتون جدید بسازید (برای مثال با استفاده از `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

سپس Olive و وابستگی‌های مربوط به فرآیند ریزتنظیم را نصب کنید:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 ریزتنظیم Phi3 با Olive
فایل پیکربندی [Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) شامل یک *جریان کاری* با *گذرهای* زیر است:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

در سطح کلی، این جریان کاری:

1. Phi3 را برای ۱۵۰ گام (که می‌توانید تغییر دهید) با استفاده از داده‌های [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) ریزتنظیم می‌کند.
1. وزن‌های آداپتور LoRA را در مدل پایه ادغام می‌کند. این کار یک مدل واحد در قالب ONNX به شما می‌دهد.
1. Model Builder مدل را برای ONNX runtime بهینه‌سازی کرده و آن را به قالب `int4` کمّی‌سازی می‌کند.

برای اجرای جریان کاری، دستور زیر را اجرا کنید:

```bash
olive run --config phrase-classification.json
```

پس از اتمام Olive، مدل ریزتنظیم‌شده و بهینه‌شده `int4` در مسیر زیر در دسترس است: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 ادغام Phi3 ریزتنظیم‌شده در برنامه خود

برای اجرای برنامه:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

پاسخ باید یک کلمه باشد که طبقه‌بندی عبارت را نشان می‌دهد (غمگین/شادی/ترس/تعجب).

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که ناشی از استفاده از این ترجمه باشد، نیستیم.