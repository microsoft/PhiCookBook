<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec5e22bbded16acb7bdb9fa568ab5781",
  "translation_date": "2025-03-27T08:27:59+00:00",
  "source_file": "md\\01.Introduction\\04\\UsingAppleMLXQuantifyingPhi.md",
  "language_code": "fa"
}
-->
# **کوانتایز کردن Phi-3.5 با استفاده از چارچوب Apple MLX**

MLX یک چارچوب آرایه‌ای برای تحقیقات یادگیری ماشین بر روی تراشه‌های سیلیکونی اپل است که توسط تیم تحقیقاتی یادگیری ماشین اپل ارائه شده است.

MLX توسط محققان یادگیری ماشین و برای محققان یادگیری ماشین طراحی شده است. این چارچوب به گونه‌ای طراحی شده که کاربرپسند باشد اما همچنان برای آموزش و استقرار مدل‌ها کارآمد باقی بماند. طراحی این چارچوب به‌طور مفهومی ساده است و هدف این است که محققان به راحتی بتوانند MLX را گسترش داده و بهبود دهند تا ایده‌های جدید را به سرعت بررسی کنند.

مدل‌های زبانی بزرگ (LLMs) می‌توانند با استفاده از MLX بر روی دستگاه‌های سیلیکونی اپل شتاب بگیرند و مدل‌ها به‌راحتی به‌صورت محلی اجرا شوند.

اکنون چارچوب Apple MLX از تبدیل کوانتایز Phi-3.5-Instruct (**پشتیبانی چارچوب Apple MLX**)، Phi-3.5-Vision (**پشتیبانی چارچوب MLX-VLM**) و Phi-3.5-MoE (**پشتیبانی چارچوب Apple MLX**) پشتیبانی می‌کند. بیایید آن را امتحان کنیم:

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

### **🤖 نمونه‌ها برای Phi-3.5 با Apple MLX**

| آزمایشگاه‌ها    | معرفی | برو |
| -------- | ------- |  ------- |
| 🚀 معرفی آزمایشگاه Phi-3.5 Instruct  | یاد بگیرید چگونه از Phi-3.5 Instruct با چارچوب Apple MLX استفاده کنید   |  [برو](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-instruct.ipynb)    |
| 🚀 معرفی آزمایشگاه Phi-3.5 Vision (تصویر) | یاد بگیرید چگونه از Phi-3.5 Vision برای تحلیل تصاویر با چارچوب Apple MLX استفاده کنید     |  [برو](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-vision.ipynb)    |
| 🚀 معرفی آزمایشگاه Phi-3.5 Vision (MoE)   | یاد بگیرید چگونه از Phi-3.5 MoE با چارچوب Apple MLX استفاده کنید  |  [برو](../../../../../code/09.UpdateSamples/Aug/mlx-phi35-moe.ipynb)    |

## **منابع**

1. درباره چارچوب Apple MLX بیشتر بدانید [https://ml-explore.github.io/mlx/](https://ml-explore.github.io/mlx/)

2. مخزن GitHub چارچوب Apple MLX [https://github.com/ml-explore](https://github.com/ml-explore/mlx)

3. مخزن GitHub چارچوب MLX-VLM [https://github.com/Blaizzy/mlx-vlm](https://github.com/Blaizzy/mlx-vlm)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم تا دقت ترجمه را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان مادری باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.