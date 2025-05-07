<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-05-07T14:49:55+00:00",
  "source_file": "md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md",
  "language_code": "fa"
}
-->
# **کوانتایز کردن Phi-3.5 با استفاده از فریم‌ورک Apple MLX**

MLX یک فریم‌ورک آرایه‌ای برای تحقیقات یادگیری ماشین روی سیلیکون اپل است که توسط تیم تحقیقاتی یادگیری ماشین اپل ارائه شده است.

MLX توسط محققان یادگیری ماشین برای محققان یادگیری ماشین طراحی شده است. این فریم‌ورک به گونه‌ای طراحی شده که کاربرپسند باشد، اما همچنان برای آموزش و استقرار مدل‌ها کارآمد باشد. طراحی خود فریم‌ورک نیز از نظر مفهومی ساده است. هدف ما این است که برای محققان آسان باشد تا MLX را گسترش داده و بهبود بخشند تا بتوانند ایده‌های جدید را به سرعت بررسی کنند.

مدل‌های زبان بزرگ (LLM) می‌توانند در دستگاه‌های سیلیکون اپل از طریق MLX تسریع شوند و مدل‌ها به صورت محلی به‌راحتی اجرا شوند.

اکنون فریم‌ورک Apple MLX از تبدیل کوانتایز کردن Phi-3.5-Instruct (**پشتیبانی Apple MLX Framework**)، Phi-3.5-Vision (**پشتیبانی MLX-VLM Framework**) و Phi-3.5-MoE (**پشتیبانی Apple MLX Framework**) پشتیبانی می‌کند. بیایید امتحان کنیم:

### **Phi-3.5-Instruct**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-mini-instruct -q

```

### **Phi-3.5-Vision**

```bash

python -m mlxv_lm.convert --hf-path microsoft/Phi-3.5-vision-instruct -q

```

### **Phi-3.5-MoE**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3.5-MoE-instruct  -q

```

### **🤖 نمونه‌هایی برای Phi-3.5 با Apple MLX**

| آزمایشگاه‌ها | معرفی | رفتن |
| -------- | ------- | ------- |
| 🚀 معرفی آزمایشگاه Phi-3.5 Instruct | یاد بگیرید چگونه از Phi-3.5 Instruct با فریم‌ورک Apple MLX استفاده کنید | [رفتن](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb) |
| 🚀 معرفی آزمایشگاه Phi-3.5 Vision (تصویر) | یاد بگیرید چگونه از Phi-3.5 Vision برای تحلیل تصویر با فریم‌ورک Apple MLX استفاده کنید | [رفتن](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb) |
| 🚀 معرفی آزمایشگاه Phi-3.5 Vision (moE) | یاد بگیرید چگونه از Phi-3.5 MoE با فریم‌ورک Apple MLX استفاده کنید | [رفتن](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb) |

## **منابع**

1. آشنایی با فریم‌ورک Apple MLX [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. مخزن GitHub اپل MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. مخزن GitHub MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، استفاده از ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچگونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نیستیم.