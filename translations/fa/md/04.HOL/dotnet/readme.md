<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-07T13:09:08+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "fa"
}
-->
﻿## خوش آمدید به آزمایشگاه‌های Phi با استفاده از C#

مجموعه‌ای از آزمایشگاه‌ها وجود دارد که نشان می‌دهد چگونه می‌توان نسخه‌های مختلف قدرتمند مدل‌های Phi را در محیط .NET ادغام کرد.

## پیش‌نیازها

قبل از اجرای نمونه، مطمئن شوید موارد زیر را نصب کرده‌اید:

**.NET 9:** اطمینان حاصل کنید که [آخرین نسخه .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) روی دستگاه شما نصب شده است.

**(اختیاری) Visual Studio یا Visual Studio Code:** به یک IDE یا ویرایشگر کد نیاز دارید که قادر به اجرای پروژه‌های .NET باشد. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) یا [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) توصیه می‌شوند.

**با استفاده از git** یکی از نسخه‌های موجود Phi-3، Phi3.5 یا Phi-4 را از [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) به صورت محلی کلون کنید.

**دانلود مدل‌های Phi-4 ONNX** روی دستگاه محلی خود:

### به پوشه‌ای که مدل‌ها را ذخیره می‌کند بروید

```bash
cd c:\phi\models
```

### افزودن پشتیبانی برای lfs

```bash
git lfs install 
```

### کلون و دانلود مدل Phi-4 mini instruct و مدل چندرسانه‌ای Phi-4

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**دانلود مدل‌های Phi-3 ONNX** روی دستگاه محلی خود:

### کلون و دانلود مدل Phi-3 mini 4K instruct و مدل Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**مهم:** دموهای فعلی برای استفاده از نسخه‌های ONNX مدل طراحی شده‌اند. مراحل قبلی مدل‌های زیر را کلون می‌کنند.

## درباره آزمایشگاه‌ها

راه‌حل اصلی چندین آزمایشگاه نمونه دارد که قابلیت‌های مدل‌های Phi را با استفاده از C# نشان می‌دهد.

| پروژه | مدل | توضیحات |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 یا Phi-3.5 | نمونه چت کنسول که به کاربر اجازه می‌دهد سوال بپرسد. پروژه مدل محلی ONNX Phi-3 را با استفاده از `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Sample console chat that allows the user to ask questions. The chat implements memory. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime` بارگذاری می‌کند.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. پروژه را با دستور زیر اجرا کنید

    ```bash
    dotnet run
    ```

1. پروژه نمونه از کاربر ورودی می‌گیرد و با استفاده از مدل محلی پاسخ می‌دهد.

   دمو در حال اجرا مشابه این است:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوء تفاهم یا تفسیر نادرستی که ناشی از استفاده از این ترجمه باشد، نیستیم.