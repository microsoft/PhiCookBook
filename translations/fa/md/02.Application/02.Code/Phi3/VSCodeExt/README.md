<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-07-17T03:33:46+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "fa"
}
-->
# **ساخت GitHub Copilot Chat مخصوص خودتان در Visual Studio Code با خانواده Microsoft Phi-3**

آیا تا به حال از workspace agent در GitHub Copilot Chat استفاده کرده‌اید؟ آیا می‌خواهید عامل کد مخصوص تیم خودتان را بسازید؟ این آزمایشگاه عملی قصد دارد مدل متن‌باز را ترکیب کند تا یک عامل کد تجاری در سطح سازمانی بسازد.

## **مبانی**

### **چرا Microsoft Phi-3 را انتخاب کنیم**

Phi-3 یک سری خانواده است که شامل phi-3-mini، phi-3-small و phi-3-medium می‌شود که بر اساس پارامترهای مختلف آموزش برای تولید متن، تکمیل گفتگو و تولید کد ساخته شده‌اند. همچنین phi-3-vision بر پایه Vision وجود دارد. این مدل برای سازمان‌ها یا تیم‌های مختلف مناسب است تا راهکارهای تولید هوش مصنوعی آفلاین بسازند.

پیشنهاد می‌شود این لینک را مطالعه کنید [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

افزونه GitHub Copilot Chat یک رابط گفتگو به شما می‌دهد که می‌توانید مستقیماً در VS Code با GitHub Copilot تعامل داشته باشید و پاسخ سوالات مرتبط با کدنویسی را بدون نیاز به جستجو در مستندات یا انجمن‌های آنلاین دریافت کنید.

Copilot Chat ممکن است از برجسته‌سازی نحو، تورفتگی و سایر ویژگی‌های قالب‌بندی برای شفاف‌تر کردن پاسخ تولید شده استفاده کند. بسته به نوع سوال کاربر، نتیجه می‌تواند شامل لینک‌هایی به زمینه‌ای باشد که Copilot برای تولید پاسخ استفاده کرده است، مانند فایل‌های کد منبع یا مستندات، یا دکمه‌هایی برای دسترسی به قابلیت‌های VS Code.

- Copilot Chat در جریان کاری توسعه‌دهنده شما ادغام می‌شود و در جایی که نیاز دارید به شما کمک می‌کند:

- شروع یک گفتگوی چت درون‌خطی مستقیماً از ویرایشگر یا ترمینال برای کمک هنگام کدنویسی

- استفاده از نمای Chat برای داشتن یک دستیار هوش مصنوعی در کنار که در هر زمان به شما کمک می‌کند

- راه‌اندازی Quick Chat برای پرسیدن سوال سریع و بازگشت به کار خود

می‌توانید از GitHub Copilot Chat در سناریوهای مختلف استفاده کنید، مانند:

- پاسخ به سوالات کدنویسی درباره بهترین روش حل یک مشکل

- توضیح کد دیگران و پیشنهاد بهبودها

- پیشنهاد اصلاحات کد

- تولید تست‌های واحد

- تولید مستندات کد

پیشنهاد می‌شود این لینک را مطالعه کنید [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

ارجاع به **@workspace** در Copilot Chat به شما امکان می‌دهد سوالاتی درباره کل کدبیس خود بپرسید. بر اساس سوال، Copilot به‌طور هوشمند فایل‌ها و نمادهای مرتبط را بازیابی می‌کند که سپس در پاسخ خود به صورت لینک‌ها و نمونه‌های کد به آن‌ها اشاره می‌کند.

برای پاسخ به سوال شما، **@workspace** از همان منابعی استفاده می‌کند که یک توسعه‌دهنده هنگام مرور کدبیس در VS Code استفاده می‌کند:

- همه فایل‌های موجود در workspace، به جز فایل‌هایی که توسط فایل .gitignore نادیده گرفته شده‌اند

- ساختار دایرکتوری با پوشه‌ها و نام فایل‌های تو در تو

- شاخص جستجوی کد GitHub، اگر workspace یک مخزن GitHub باشد و توسط جستجوی کد ایندکس شده باشد

- نمادها و تعاریف در workspace

- متن انتخاب شده یا متن قابل مشاهده در ویرایشگر فعال

توجه: اگر فایلی باز باشد یا متنی در یک فایل نادیده گرفته شده انتخاب شده باشد، .gitignore نادیده گرفته می‌شود.

پیشنهاد می‌شود این لینک را مطالعه کنید [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **اطلاعات بیشتر درباره این آزمایشگاه**

GitHub Copilot به طور قابل توجهی بهره‌وری برنامه‌نویسی سازمان‌ها را بهبود بخشیده است و هر سازمانی امیدوار است عملکردهای مرتبط با GitHub Copilot را سفارشی کند. بسیاری از سازمان‌ها افزونه‌های سفارشی مشابه GitHub Copilot را بر اساس سناریوهای کسب‌وکار خود و مدل‌های متن‌باز ساخته‌اند. برای سازمان‌ها، افزونه‌های سفارشی کنترل آسان‌تری دارند، اما این موضوع بر تجربه کاربری نیز تأثیر می‌گذارد. به هر حال، GitHub Copilot در برخورد با سناریوهای عمومی و حرفه‌ای عملکرد قوی‌تری دارد. اگر بتوان تجربه را یکسان نگه داشت، بهتر است افزونه سازمانی خود را سفارشی کرد. GitHub Copilot Chat APIهای مرتبطی برای سازمان‌ها فراهم می‌کند تا تجربه چت را گسترش دهند. حفظ تجربه یکسان و داشتن عملکردهای سفارشی تجربه کاربری بهتری است.

این آزمایشگاه عمدتاً از مدل Phi-3 به همراه NPU محلی و ترکیب Azure برای ساخت یک Agent سفارشی در GitHub Copilot Chat ***@PHI3*** استفاده می‌کند تا به توسعه‌دهندگان سازمانی در تکمیل تولید کد ***(@PHI3 /gen)*** و تولید کد بر اساس تصاویر ***(@PHI3 /img)*** کمک کند.

![PHI3](../../../../../../../translated_images/fa/cover.1017ebc9a7c46d09.png)

### ***توجه:*** 

این آزمایشگاه در حال حاضر روی AIPC پردازنده‌های Intel و Apple Silicon پیاده‌سازی شده است. نسخه Qualcomm NPU نیز به‌زودی به‌روزرسانی خواهد شد.


## **آزمایشگاه**


| نام | توضیحات | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - نصب‌ها (✅) | پیکربندی و نصب محیط‌ها و ابزارهای مرتبط | [برو](./HOL/AIPC/01.Installations.md) |[برو](./HOL/Apple/01.Installations.md) |
| Lab1 - اجرای Prompt flow با Phi-3-mini (✅) | ترکیب با AIPC / Apple Silicon، استفاده از NPU محلی برای ایجاد تولید کد از طریق Phi-3-mini | [برو](./HOL/AIPC/02.PromptflowWithNPU.md) |  [برو](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - استقرار Phi-3-vision در Azure Machine Learning Service (✅) | تولید کد با استقرار مدل کاتالوگ Azure Machine Learning Service - تصویر Phi-3-vision | [برو](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[برو](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - ساخت یک عامل @phi-3 در GitHub Copilot Chat (✅)  | ساخت یک عامل سفارشی Phi-3 در GitHub Copilot Chat برای تکمیل تولید کد، تولید کد گراف، RAG و غیره | [برو](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [برو](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| نمونه کد (✅)  | دانلود نمونه کد | [برو](../../../../../../../code/07.Lab/01/AIPC) | [برو](../../../../../../../code/07.Lab/01/Apple) |


## **منابع**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. اطلاعات بیشتر درباره GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. اطلاعات بیشتر درباره GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. اطلاعات بیشتر درباره GitHub Copilot Chat API [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. اطلاعات بیشتر درباره Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. اطلاعات بیشتر درباره کاتالوگ مدل Azure AI Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.