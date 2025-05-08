<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00b7a699de8ac405fa821f4c0f7fc0ab",
  "translation_date": "2025-05-07T13:47:05+00:00",
  "source_file": "md/02.Application/02.Code/Phi3/VSCodeExt/README.md",
  "language_code": "fa"
}
-->
# **ساخت چت GitHub Copilot در Visual Studio Code با خانواده Microsoft Phi-3**

آیا تا به حال از workspace agent در GitHub Copilot Chat استفاده کرده‌اید؟ آیا می‌خواهید عامل کد مخصوص تیم خودتان را بسازید؟ این آزمایشگاه عملی قصد دارد مدل متن‌باز را با هم ترکیب کند تا یک عامل کد تجاری در سطح سازمانی بسازد.

## **مبانی**

### **چرا Microsoft Phi-3 را انتخاب کنیم**

Phi-3 یک خانواده مدل است که شامل phi-3-mini، phi-3-small و phi-3-medium بر اساس پارامترهای مختلف آموزش برای تولید متن، تکمیل گفتگو و تولید کد می‌شود. همچنین phi-3-vision بر اساس Vision وجود دارد. این مدل‌ها برای سازمان‌ها یا تیم‌های مختلف مناسب‌اند تا راه‌حل‌های هوش مصنوعی مولد آفلاین بسازند.

پیشنهاد می‌شود این لینک را مطالعه کنید [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

افزونه GitHub Copilot Chat یک رابط چت در اختیار شما قرار می‌دهد که به شما امکان می‌دهد مستقیماً در VS Code با GitHub Copilot تعامل کنید و پاسخ سوالات مرتبط با کدنویسی را بدون نیاز به جستجو در مستندات یا انجمن‌های آنلاین دریافت کنید.

Copilot Chat ممکن است از برجسته‌سازی سینتکس، تورفتگی و سایر ویژگی‌های قالب‌بندی برای واضح‌تر کردن پاسخ تولید شده استفاده کند. بسته به نوع سوال کاربر، نتیجه می‌تواند شامل لینک‌هایی به منابعی باشد که Copilot برای تولید پاسخ استفاده کرده، مانند فایل‌های کد منبع یا مستندات، یا دکمه‌هایی برای دسترسی به قابلیت‌های VS Code.

- Copilot Chat در جریان کاری توسعه‌دهنده شما ادغام می‌شود و در جایی که نیاز دارید به شما کمک می‌کند:

- شروع یک گفتگوی چت درون خطی مستقیماً از ویرایشگر یا ترمینال برای کمک هنگام کدنویسی

- استفاده از نمای Chat برای داشتن یک دستیار هوش مصنوعی در کنار شما در هر زمان

- راه‌اندازی Quick Chat برای پرسیدن سوال سریع و بازگشت سریع به کار خود

شما می‌توانید از GitHub Copilot Chat در موقعیت‌های مختلف استفاده کنید، مانند:

- پاسخ به سوالات کدنویسی درباره بهترین روش حل یک مشکل

- توضیح کد دیگران و پیشنهاد بهبودها

- پیشنهاد رفع اشکال کد

- تولید تست‌های واحد

- تولید مستندات کد

پیشنهاد می‌شود این لینک را مطالعه کنید [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

استفاده از **@workspace** در Copilot Chat به شما امکان می‌دهد سوالاتی درباره کل کدبیس خود بپرسید. بر اساس سوال، Copilot به‌صورت هوشمند فایل‌ها و نمادهای مرتبط را بازیابی می‌کند و سپس آنها را به صورت لینک‌ها و مثال‌های کد در پاسخ خود ارجاع می‌دهد.

برای پاسخ به سوال شما، **@workspace** از همان منابعی استفاده می‌کند که یک توسعه‌دهنده هنگام مرور کدبیس در VS Code استفاده می‌کند:

- همه فایل‌های موجود در workspace، به جز فایل‌هایی که توسط .gitignore نادیده گرفته شده‌اند

- ساختار دایرکتوری با نام‌های پوشه‌ها و فایل‌های تو در تو

- شاخص جستجوی کد GitHub، اگر workspace یک مخزن GitHub باشد و توسط جستجوی کد ایندکس شده باشد

- نمادها و تعاریف موجود در workspace

- متن انتخاب شده یا متن قابل مشاهده در ویرایشگر فعال

توجه: اگر فایلی باز باشد یا متنی در یک فایل نادیده گرفته شده انتخاب شده باشد، .gitignore نادیده گرفته می‌شود.

پیشنهاد می‌شود این لینک را مطالعه کنید [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **آشنایی بیشتر با این آزمایشگاه**

GitHub Copilot به طور چشمگیری کارایی برنامه‌نویسی سازمان‌ها را بهبود بخشیده و هر سازمانی امیدوار است عملکردهای مرتبط با GitHub Copilot را شخصی‌سازی کند. بسیاری از سازمان‌ها افزونه‌های مشابه GitHub Copilot را بر اساس سناریوهای کسب‌وکار خود و مدل‌های متن‌باز سفارشی کرده‌اند. برای سازمان‌ها، افزونه‌های سفارشی کنترل‌پذیرتر هستند، اما این موضوع بر تجربه کاربری نیز تاثیر می‌گذارد. به هر حال، GitHub Copilot در مواجهه با سناریوهای عمومی و حرفه‌ای عملکرد قوی‌تری دارد. اگر تجربه کاربری بتواند یکسان حفظ شود، بهتر است افزونه سازمانی خود را سفارشی کنند. GitHub Copilot Chat APIهای مرتبطی برای گسترش تجربه چت در اختیار سازمان‌ها قرار می‌دهد. حفظ تجربه یکسان و داشتن عملکردهای سفارشی تجربه کاربری بهتری است.

این آزمایشگاه عمدتاً از مدل Phi-3 همراه با NPU محلی و Azure هیبرید استفاده می‌کند تا یک Agent سفارشی در GitHub Copilot Chat به نام ***@PHI3*** بسازد که به توسعه‌دهندگان سازمانی در تکمیل تولید کد***(@PHI3 /gen)*** و تولید کد بر اساس تصاویر ***(@PHI3 /img)*** کمک می‌کند.

![PHI3](../../../../../../../translated_images/cover.1017ebc9a7c46d095fe0b942687287803c03933d2d1d439d14e10fa1442a864d.fa.png)

### ***توجه:*** 

این آزمایشگاه در حال حاضر در AIPC پردازنده Intel و Apple Silicon پیاده‌سازی شده است. ما به‌روزرسانی نسخه Qualcomm NPU را ادامه خواهیم داد.


## **آزمایشگاه**


| نام | توضیحات | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installations(✅) | پیکربندی و نصب محیط‌ها و ابزارهای مرتبط | [برو](./HOL/AIPC/01.Installations.md) |[برو](./HOL/Apple/01.Installations.md) |
| Lab1 - Run Prompt flow with Phi-3-mini (✅) | ترکیب با AIPC / Apple Silicon، استفاده از NPU محلی برای ایجاد تولید کد از طریق Phi-3-mini | [برو](./HOL/AIPC/02.PromptflowWithNPU.md) |  [برو](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision on Azure Machine Learning Service(✅) | تولید کد با استقرار مدل کاتالوگ Azure Machine Learning Service - تصویر Phi-3-vision | [برو](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[برو](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Create a @phi-3 agent in GitHub Copilot Chat(✅)  | ساخت یک عامل سفارشی Phi-3 در GitHub Copilot Chat برای تکمیل تولید کد، تولید کد گراف، RAG و غیره | [برو](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [برو](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Sample Code (✅)  | دانلود کد نمونه | [برو](../../../../../../../code/07.Lab/01/AIPC) | [برو](../../../../../../../code/07.Lab/01/Apple) |


## **منابع**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. اطلاعات بیشتر درباره GitHub Copilot [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. اطلاعات بیشتر درباره GitHub Copilot Chat [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. اطلاعات بیشتر درباره API چت GitHub Copilot [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. اطلاعات بیشتر درباره Azure AI Foundry [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. اطلاعات بیشتر درباره کاتالوگ مدل Azure AI Foundry [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده شود. ما مسئول هیچ‌گونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نیستیم.