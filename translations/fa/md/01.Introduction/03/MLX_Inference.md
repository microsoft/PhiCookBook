<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-03-27T07:51:08+00:00",
  "source_file": "md\\01.Introduction\\03\\MLX_Inference.md",
  "language_code": "fa"
}
-->
# **استنتاج Phi-3 با استفاده از چارچوب Apple MLX**

## **چارچوب MLX چیست**

MLX یک چارچوب آرایه‌ای برای پژوهش‌های یادگیری ماشین روی تراشه‌های اپل سیلیکون است که توسط تیم تحقیقاتی یادگیری ماشین اپل ارائه شده است.

MLX توسط محققان یادگیری ماشین و برای محققان یادگیری ماشین طراحی شده است. این چارچوب به گونه‌ای طراحی شده که کاربرپسند باشد و در عین حال بتواند مدل‌ها را به طور کارآمد آموزش داده و اجرا کند. طراحی این چارچوب به طور مفهومی ساده است. هدف ما این است که محققان بتوانند به راحتی MLX را گسترش داده و بهبود دهند تا ایده‌های جدید را به سرعت بررسی کنند.

مدل‌های زبانی بزرگ (LLMs) می‌توانند روی دستگاه‌های اپل سیلیکون با استفاده از MLX شتاب داده شوند و مدل‌ها به راحتی به صورت محلی اجرا شوند.

## **استفاده از MLX برای استنتاج Phi-3-mini**

### **۱. تنظیم محیط MLX**

1. پایتون نسخه 3.11.x  
2. نصب کتابخانه MLX  

```bash

pip install mlx-lm

```

### **۲. اجرای Phi-3-mini در ترمینال با MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

نتیجه (محیط من: Apple M1 Max، رم ۶۴ گیگابایت) به صورت زیر است:

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.fa.png)

### **۳. کوانتایز کردن Phi-3-mini با MLX در ترمینال**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***توجه:*** مدل از طریق mlx_lm.convert می‌تواند کوانتایز شود و کوانتایز پیش‌فرض INT4 است. این مثال Phi-3-mini را به INT4 کوانتایز می‌کند.

مدل از طریق mlx_lm.convert می‌تواند کوانتایز شود و کوانتایز پیش‌فرض INT4 است. این مثال Phi-3-mini را به INT4 کوانتایز می‌کند. پس از کوانتایز، مدل در مسیر پیش‌فرض ./mlx_model ذخیره خواهد شد.

ما می‌توانیم مدل کوانتایز شده را از طریق ترمینال با MLX تست کنیم.

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

نتیجه به صورت زیر است:

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.fa.png)

### **۴. اجرای Phi-3-mini با MLX در Jupyter Notebook**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.fa.png)

***توجه:*** لطفاً این نمونه را مطالعه کنید [روی این لینک کلیک کنید](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **منابع**

1. درباره چارچوب Apple MLX بیشتر بدانید: [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. مخزن GitHub اپل MLX: [https://github.com/ml-explore](https://github.com/ml-explore)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.