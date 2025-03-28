<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8fd4bbea0a970872d95cf189202589e1",
  "translation_date": "2025-03-27T16:26:29+00:00",
  "source_file": "md\\04.HOL\\dotnet\\readme.md",
  "language_code": "ar"
}
-->
## مرحبًا بكم في مختبرات Phi باستخدام C#

توجد مجموعة من المختبرات التي تعرض كيفية دمج الإصدارات القوية المختلفة لنماذج Phi في بيئة .NET.

## المتطلبات الأساسية

قبل تشغيل المثال، تأكد من تثبيت ما يلي:

**.NET 9:** تأكد من أن لديك [أحدث إصدار من .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) مثبتًا على جهازك.

**(اختياري) Visual Studio أو Visual Studio Code:** ستحتاج إلى بيئة تطوير أو محرر كود قادر على تشغيل مشاريع .NET. يُوصى باستخدام [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) أو [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**باستخدام git** قم باستنساخ أحد إصدارات Phi-3، Phi3.5 أو Phi-4 المتاحة محليًا من [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**قم بتنزيل نماذج Phi-4 ONNX** على جهازك المحلي:

### انتقل إلى المجلد لتخزين النماذج

```bash
cd c:\phi\models
```

### أضف دعم lfs

```bash
git lfs install 
```

### استنسخ وقم بتنزيل نموذج Phi-4 mini instruct ونموذج Phi-4 multi modal

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**قم بتنزيل نماذج Phi-3 ONNX** على جهازك المحلي:

### استنسخ وقم بتنزيل نموذج Phi-3 mini 4K instruct ونموذج Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**مهم:** العروض الحالية مصممة لاستخدام إصدارات ONNX من النموذج. الخطوات السابقة تستنسخ النماذج التالية.

## حول المختبرات

الحل الرئيسي يحتوي على عدة مختبرات تجريبية تعرض إمكانيات نماذج Phi باستخدام C#.

| المشروع | النموذج | الوصف |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 أو Phi-3.5 | مثال محادثة في وحدة التحكم يسمح للمستخدم بطرح الأسئلة. يقوم المشروع بتحميل نموذج Phi-3 ONNX محلي باستخدام `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. قم بتشغيل المشروع باستخدام الأمر

    ```bash
    dotnet run
    ```

1. يطلب المشروع التجريبي إدخالًا من المستخدم ويجيب باستخدام الوضع المحلي.

   العرض التجريبي أثناء التشغيل يشبه هذا:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يُرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الرسمي. بالنسبة للمعلومات الحرجة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.