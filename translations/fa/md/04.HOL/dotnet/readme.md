<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:31:35+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "fa"
}
-->
﻿## خوش آمدید به آزمایشگاه‌های Phi با استفاده از C#

مجموعه‌ای از آزمایشگاه‌ها وجود دارد که نشان می‌دهد چگونه می‌توان نسخه‌های مختلف قدرتمند مدل‌های Phi را در محیط .NET ادغام کرد.

## پیش‌نیازها

قبل از اجرای نمونه، مطمئن شوید که موارد زیر را نصب کرده‌اید:

**.NET 9:** اطمینان حاصل کنید که [جدیدترین نسخه .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) روی دستگاه شما نصب شده است.

**(اختیاری) Visual Studio یا Visual Studio Code:** به یک IDE یا ویرایشگر کد نیاز دارید که قادر به اجرای پروژه‌های .NET باشد. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) یا [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) توصیه می‌شوند.

**استفاده از git** یکی از نسخه‌های موجود Phi-3، Phi3.5 یا Phi-4 را از [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) به صورت محلی کلون کنید.

**دانلود مدل‌های Phi-4 ONNX** به دستگاه محلی خود:

### به پوشه‌ای که می‌خواهید مدل‌ها را ذخیره کنید بروید

```bash
cd c:\phi\models
```

### افزودن پشتیبانی برای lfs

```bash
git lfs install 
```

### کلون و دانلود مدل Phi-4 mini instruct و مدل Phi-4 چندرسانه‌ای

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**دانلود مدل‌های Phi-3 ONNX** به دستگاه محلی خود:

### کلون و دانلود مدل Phi-3 mini 4K instruct و مدل Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**مهم:** دموهای فعلی برای استفاده از نسخه‌های ONNX مدل طراحی شده‌اند. مراحل قبلی مدل‌های زیر را کلون می‌کنند.

## درباره آزمایشگاه‌ها

راه‌حل اصلی شامل چندین آزمایشگاه نمونه است که قابلیت‌های مدل‌های Phi را با استفاده از C# نشان می‌دهد.

| پروژه | مدل | توضیحات |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 یا Phi-3.5 | چت کنسول نمونه که به کاربر اجازه می‌دهد سوال بپرسد. پروژه یک مدل ONNX Phi-3 محلی را با استفاده از کتابخانه‌های `Microsoft.ML.OnnxRuntime` بارگذاری می‌کند. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 یا Phi-3.5 | چت کنسول نمونه که به کاربر اجازه می‌دهد سوال بپرسد. پروژه یک مدل ONNX Phi-3 محلی را با استفاده از کتابخانه‌های `Microsoft.Semantic.Kernel` بارگذاری می‌کند. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 یا Phi-3.5 | این یک پروژه نمونه است که از مدل بینایی phi3 محلی برای تحلیل تصاویر استفاده می‌کند. پروژه یک مدل ONNX Phi-3 Vision محلی را با استفاده از کتابخانه‌های `Microsoft.ML.OnnxRuntime` بارگذاری می‌کند. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 یا Phi-3.5 | این یک پروژه نمونه است که از مدل بینایی phi3 محلی برای تحلیل تصاویر استفاده می‌کند. پروژه یک مدل ONNX Phi-3 Vision محلی را با استفاده از کتابخانه‌های `Microsoft.ML.OnnxRuntime` بارگذاری می‌کند. همچنین پروژه منویی با گزینه‌های مختلف برای تعامل با کاربر ارائه می‌دهد. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | چت کنسول نمونه که به کاربر اجازه می‌دهد سوال بپرسد. پروژه یک مدل ONNX Phi-4 محلی را با استفاده از کتابخانه‌های `Microsoft.ML.OnnxRuntime` بارگذاری می‌کند. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | چت کنسول نمونه که به کاربر اجازه می‌دهد سوال بپرسد. پروژه یک مدل ONNX Phi-4 محلی را با استفاده از کتابخانه‌های `Semantic Kernel` بارگذاری می‌کند. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | چت کنسول نمونه که به کاربر اجازه می‌دهد سوال بپرسد. پروژه یک مدل ONNX Phi-4 محلی را با استفاده از کتابخانه‌های `Microsoft.ML.OnnxRuntimeGenAI` بارگذاری می‌کند و `IChatClient` از `Microsoft.Extensions.AI` را پیاده‌سازی می‌کند. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | چت کنسول نمونه که به کاربر اجازه می‌دهد سوال بپرسد. چت حافظه را پیاده‌سازی می‌کند. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | این یک پروژه نمونه است که از مدل Phi-4 محلی برای تحلیل تصاویر استفاده می‌کند و نتیجه را در کنسول نمایش می‌دهد. پروژه یک مدل Phi-4-`multimodal-instruct-onnx` محلی را با استفاده از کتابخانه‌های `Microsoft.ML.OnnxRuntime` بارگذاری می‌کند. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | این یک پروژه نمونه است که از مدل Phi-4 محلی برای تحلیل یک فایل صوتی استفاده می‌کند، متن فایل را تولید می‌کند و نتیجه را در کنسول نمایش می‌دهد. پروژه یک مدل Phi-4-`multimodal-instruct-onnx` محلی را با استفاده از کتابخانه‌های `Microsoft.ML.OnnxRuntime` بارگذاری می‌کند. |

## نحوه اجرای پروژه‌ها

برای اجرای پروژه‌ها، مراحل زیر را دنبال کنید:

1. مخزن را به دستگاه محلی خود کلون کنید.

1. یک ترمینال باز کنید و به پروژه مورد نظر بروید. به عنوان مثال، پروژه `LabsPhi4-Chat-01OnnxRuntime` را اجرا می‌کنیم.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. پروژه را با دستور زیر اجرا کنید

    ```bash
    dotnet run
    ```

1. پروژه نمونه از کاربر ورودی می‌گیرد و با استفاده از مدل محلی پاسخ می‌دهد.

   دمو در حال اجرا مشابه نمونه زیر است:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.