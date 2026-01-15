<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2bc0950f44919ac75a88c1a871680c2",
  "translation_date": "2025-07-17T09:01:44+00:00",
  "source_file": "md/03.FineTuning/Finetuning_VSCodeaitoolkit.md",
  "language_code": "fa"
}
-->
## خوش آمدید به AI Toolkit برای VS Code

[AI Toolkit برای VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) مدل‌های مختلفی از Azure AI Studio Catalog و کاتالوگ‌های دیگر مانند Hugging Face را گرد هم آورده است. این ابزار، کارهای رایج توسعه برای ساخت برنامه‌های هوش مصنوعی با استفاده از ابزارها و مدل‌های تولیدی را ساده می‌کند از طریق:
- شروع با کشف مدل و محیط آزمایشی.
- تنظیم دقیق مدل و استنتاج با استفاده از منابع محلی.
- تنظیم دقیق و استنتاج از راه دور با استفاده از منابع Azure

[نصب AI Toolkit برای VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/fa/Aitoolkit.7157953df04812dc.png)


**[Private Preview]** فراهم‌سازی با یک کلیک برای Azure Container Apps جهت اجرای تنظیم دقیق مدل و استنتاج در فضای ابری.

حالا بیایید وارد توسعه برنامه هوش مصنوعی شما شویم:

- [خوش آمدید به AI Toolkit برای VS Code](../../../../md/03.FineTuning)
- [توسعه محلی](../../../../md/03.FineTuning)
  - [آمادگی‌ها](../../../../md/03.FineTuning)
  - [فعال‌سازی Conda](../../../../md/03.FineTuning)
  - [تنظیم دقیق فقط مدل پایه](../../../../md/03.FineTuning)
  - [تنظیم دقیق مدل و استنتاج](../../../../md/03.FineTuning)
  - [تنظیم دقیق مدل](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [نمونه‌ها و منابع تنظیم دقیق](../../../../md/03.FineTuning)
- [**\[Private Preview\]** توسعه از راه دور](../../../../md/03.FineTuning)
  - [پیش‌نیازها](../../../../md/03.FineTuning)
  - [راه‌اندازی پروژه توسعه از راه دور](../../../../md/03.FineTuning)
  - [فراهم‌سازی منابع Azure](../../../../md/03.FineTuning)
  - [\[اختیاری\] افزودن توکن Huggingface به راز Azure Container App](../../../../md/03.FineTuning)
  - [اجرای تنظیم دقیق](../../../../md/03.FineTuning)
  - [فراهم‌سازی نقطه پایانی استنتاج](../../../../md/03.FineTuning)
  - [استقرار نقطه پایانی استنتاج](../../../../md/03.FineTuning)
  - [استفاده پیشرفته](../../../../md/03.FineTuning)

## توسعه محلی
### آمادگی‌ها

1. مطمئن شوید درایور NVIDIA روی میزبان نصب شده است.
2. اگر از HF برای استفاده از دیتاست استفاده می‌کنید، دستور `huggingface-cli login` را اجرا کنید.
3. توضیحات تنظیمات کلید `Olive` برای هر چیزی که مصرف حافظه را تغییر می‌دهد.

### فعال‌سازی Conda
از آنجا که ما از محیط WSL استفاده می‌کنیم و این محیط مشترک است، باید به صورت دستی محیط conda را فعال کنید. پس از این مرحله می‌توانید تنظیم دقیق یا استنتاج را اجرا کنید.

```bash
conda activate [conda-env-name] 
```

### فقط تنظیم دقیق مدل پایه
برای امتحان کردن مدل پایه بدون تنظیم دقیق، پس از فعال‌سازی conda می‌توانید این دستور را اجرا کنید.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### تنظیم دقیق مدل و استنتاج

وقتی فضای کاری در یک کانتینر توسعه باز شد، یک ترمینال باز کنید (مسیر پیش‌فرض ریشه پروژه است)، سپس دستور زیر را برای تنظیم دقیق یک LLM روی دیتاست انتخاب شده اجرا کنید.

```bash
python finetuning/invoke_olive.py 
```

نقاط بررسی و مدل نهایی در پوشه `models` ذخیره خواهند شد.

سپس استنتاج را با مدل تنظیم دقیق شده از طریق چت‌ها در `کنسول`، `مرورگر وب` یا `prompt flow` اجرا کنید.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

برای استفاده از `prompt flow` در VS Code، لطفاً به این [شروع سریع](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html) مراجعه کنید.

### تنظیم دقیق مدل

سپس، بسته به وجود GPU در دستگاه خود، مدل زیر را دانلود کنید.

برای شروع جلسه تنظیم دقیق محلی با استفاده از QLoRA، مدلی را که می‌خواهید تنظیم دقیق کنید از کاتالوگ ما انتخاب کنید.
| پلتفرم‌ها | GPU موجود | نام مدل | حجم (گیگابایت) |
|---------|---------|--------|--------|
| ویندوز | بله | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| لینوکس | بله | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| ویندوز<br>لینوکس | خیر | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_توجه_** برای دانلود مدل‌ها نیازی به حساب Azure ندارید.

مدل Phi3-mini (int4) حدود ۲ تا ۳ گیگابایت حجم دارد. بسته به سرعت شبکه شما، دانلود آن ممکن است چند دقیقه طول بکشد.

ابتدا نام پروژه و محل آن را انتخاب کنید.
سپس مدلی از کاتالوگ مدل انتخاب کنید. از شما خواسته می‌شود قالب پروژه را دانلود کنید. سپس می‌توانید روی "پیکربندی پروژه" کلیک کنید تا تنظیمات مختلف را تغییر دهید.

### Microsoft Olive

ما از [Olive](https://microsoft.github.io/Olive/why-olive.html) برای اجرای تنظیم دقیق QLoRA روی مدل PyTorch از کاتالوگ خود استفاده می‌کنیم. تمام تنظیمات با مقادیر پیش‌فرض بهینه شده‌اند تا فرآیند تنظیم دقیق به صورت محلی با استفاده بهینه از حافظه اجرا شود، اما می‌توان آن را برای شرایط شما تنظیم کرد.

### نمونه‌ها و منابع تنظیم دقیق

- [راهنمای شروع تنظیم دقیق](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [تنظیم دقیق با دیتاست HuggingFace](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [تنظیم دقیق با دیتاست ساده](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Private Preview]** توسعه از راه دور

### پیش‌نیازها

1. برای اجرای تنظیم دقیق مدل در محیط Azure Container App از راه دور، مطمئن شوید اشتراک شما ظرفیت GPU کافی دارد. برای درخواست ظرفیت مورد نیاز برای برنامه خود، یک [تیکت پشتیبانی](https://azure.microsoft.com/support/create-ticket/) ارسال کنید. [اطلاعات بیشتر درباره ظرفیت GPU](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)
2. اگر از دیتاست خصوصی در HuggingFace استفاده می‌کنید، مطمئن شوید که یک [حساب HuggingFace](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) دارید و [توکن دسترسی](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo) تولید کرده‌اید.
3. ویژگی تنظیم دقیق و استنتاج از راه دور را در AI Toolkit برای VS Code فعال کنید:
   1. تنظیمات VS Code را با انتخاب *File -> Preferences -> Settings* باز کنید.
   2. به بخش *Extensions* بروید و *AI Toolkit* را انتخاب کنید.
   3. گزینه *"Enable Remote Fine-tuning And Inference"* را فعال کنید.
   4. VS Code را مجدداً بارگذاری کنید تا تغییرات اعمال شود.

- [تنظیم دقیق از راه دور](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### راه‌اندازی پروژه توسعه از راه دور
1. از پالت فرمان دستور `AI Toolkit: Focus on Resource View` را اجرا کنید.
2. به بخش *Model Fine-tuning* بروید تا به کاتالوگ مدل دسترسی پیدا کنید. نامی برای پروژه خود انتخاب کرده و محل آن را روی دستگاه خود مشخص کنید. سپس روی دکمه *"Configure Project"* کلیک کنید.
3. پیکربندی پروژه
    1. گزینه *"Fine-tune locally"* را فعال نکنید.
    2. تنظیمات پیکربندی Olive با مقادیر پیش‌فرض ظاهر می‌شود. لطفاً این تنظیمات را بر اساس نیاز خود تنظیم و تکمیل کنید.
    3. به مرحله *Generate Project* بروید. این مرحله از WSL استفاده می‌کند و شامل راه‌اندازی محیط جدید Conda است، آماده‌سازی برای به‌روزرسانی‌های آینده که شامل Dev Containers خواهد بود.
4. روی *"Relaunch Window In Workspace"* کلیک کنید تا پروژه توسعه از راه دور شما باز شود.

> **توجه:** پروژه در حال حاضر یا به صورت محلی یا از راه دور در AI Toolkit برای VS Code کار می‌کند. اگر هنگام ایجاد پروژه گزینه *"Fine-tune locally"* را انتخاب کنید، پروژه فقط در WSL اجرا می‌شود و قابلیت توسعه از راه دور ندارد. اما اگر این گزینه را فعال نکنید، پروژه محدود به محیط Azure Container App از راه دور خواهد بود.

### فراهم‌سازی منابع Azure
برای شروع، باید منابع Azure را برای تنظیم دقیق از راه دور فراهم کنید. این کار را با اجرای دستور `AI Toolkit: Provision Azure Container Apps job for fine-tuning` از پالت فرمان انجام دهید.

پیشرفت فراهم‌سازی را از طریق لینکی که در کانال خروجی نمایش داده می‌شود، دنبال کنید.

### [اختیاری] افزودن توکن Huggingface به راز Azure Container App
اگر از دیتاست خصوصی HuggingFace استفاده می‌کنید، توکن HuggingFace خود را به عنوان یک متغیر محیطی تنظیم کنید تا نیازی به ورود دستی به Hugging Face Hub نباشد.
می‌توانید این کار را با دستور `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning` انجام دهید. با این دستور، می‌توانید نام راز را [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) قرار داده و توکن Hugging Face خود را به عنوان مقدار راز استفاده کنید.

### اجرای تنظیم دقیق
برای شروع کار تنظیم دقیق از راه دور، دستور `AI Toolkit: Run fine-tuning` را اجرا کنید.

برای مشاهده لاگ‌های سیستم و کنسول، می‌توانید از طریق لینک موجود در پنل خروجی به پورتال Azure مراجعه کنید (مراحل بیشتر در [مشاهده و جستجوی لاگ‌ها در Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). یا می‌توانید لاگ‌های کنسول را مستقیماً در پنل خروجی VSCode با اجرای دستور `AI Toolkit: Show the running fine-tuning job streaming logs` مشاهده کنید.
> **توجه:** ممکن است کار در صف قرار گیرد به دلیل کمبود منابع. اگر لاگ نمایش داده نشد، دستور `AI Toolkit: Show the running fine-tuning job streaming logs` را اجرا کنید، کمی صبر کنید و سپس دوباره دستور را اجرا کنید تا به لاگ استریم متصل شوید.

در این فرآیند، QLoRA برای تنظیم دقیق استفاده می‌شود و آداپتورهای LoRA را برای مدل جهت استفاده در استنتاج ایجاد می‌کند.
نتایج تنظیم دقیق در Azure Files ذخیره خواهند شد.

### فراهم‌سازی نقطه پایانی استنتاج
پس از آموزش آداپتورها در محیط از راه دور، از یک برنامه ساده Gradio برای تعامل با مدل استفاده کنید.
مشابه فرآیند تنظیم دقیق، باید منابع Azure را برای استنتاج از راه دور با اجرای دستور `AI Toolkit: Provision Azure Container Apps for inference` از پالت فرمان فراهم کنید.

به طور پیش‌فرض، اشتراک و گروه منابع برای استنتاج باید با آنچه برای تنظیم دقیق استفاده شده است، مطابقت داشته باشد. استنتاج از همان محیط Azure Container App استفاده می‌کند و به مدل و آداپتور مدل ذخیره شده در Azure Files که در مرحله تنظیم دقیق ایجاد شده‌اند، دسترسی دارد.

### استقرار نقطه پایانی استنتاج
اگر می‌خواهید کد استنتاج را بازبینی کنید یا مدل استنتاج را مجدداً بارگذاری کنید، لطفاً دستور `AI Toolkit: Deploy for inference` را اجرا کنید. این کار کد جدید شما را با Azure Container App همگام‌سازی کرده و نسخه را مجدداً راه‌اندازی می‌کند.

پس از اتمام موفقیت‌آمیز استقرار، می‌توانید با کلیک روی دکمه "*Go to Inference Endpoint*" که در اعلان VSCode نمایش داده می‌شود، به API استنتاج دسترسی پیدا کنید. یا نقطه پایانی وب API را می‌توانید در `ACA_APP_ENDPOINT` در فایل `./infra/inference.config.json` و در پنل خروجی پیدا کنید. اکنون آماده ارزیابی مدل با استفاده از این نقطه پایانی هستید.

### استفاده پیشرفته
برای اطلاعات بیشتر درباره توسعه از راه دور با AI Toolkit، به مستندات [تنظیم دقیق مدل‌ها از راه دور](https://aka.ms/ai-toolkit/remote-provision) و [استنتاج با مدل تنظیم دقیق شده](https://aka.ms/ai-toolkit/remote-inference) مراجعه کنید.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.