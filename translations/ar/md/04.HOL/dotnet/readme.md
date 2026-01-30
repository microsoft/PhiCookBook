## مرحبًا بكم في مختبرات Phi باستخدام C#

هناك مجموعة من المختبرات التي تعرض كيفية دمج الإصدارات المختلفة والقوية من نماذج Phi في بيئة .NET.

## المتطلبات الأساسية

قبل تشغيل المثال، تأكد من تثبيت ما يلي:

**.NET 9:** تأكد من تثبيت [أحدث إصدار من .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) على جهازك.

**(اختياري) Visual Studio أو Visual Studio Code:** ستحتاج إلى بيئة تطوير متكاملة أو محرر أكواد قادر على تشغيل مشاريع .NET. يُنصح باستخدام [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) أو [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**باستخدام git** قم باستنساخ محليًا أحد إصدارات Phi-3 أو Phi3.5 أو Phi-4 المتاحة من [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**تحميل نماذج Phi-4 ONNX** إلى جهازك المحلي:

### انتقل إلى المجلد لتخزين النماذج

```bash
cd c:\phi\models
```

### أضف دعم lfs

```bash
git lfs install 
```

### استنساخ وتحميل نموذج Phi-4 mini instruct ونموذج Phi-4 متعدد الوسائط

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**تحميل نماذج Phi-3 ONNX** إلى جهازك المحلي:

### استنساخ وتحميل نموذج Phi-3 mini 4K instruct ونموذج Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**مهم:** العروض الحالية مصممة لاستخدام إصدارات ONNX من النموذج. الخطوات السابقة تستنسخ النماذج التالية.

## حول المختبرات

الحل الرئيسي يحتوي على عدة مختبرات نموذجية توضح قدرات نماذج Phi باستخدام C#.

| المشروع | النموذج | الوصف |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 أو Phi-3.5 | دردشة نموذجية في وحدة التحكم تتيح للمستخدم طرح الأسئلة. يقوم المشروع بتحميل نموذج Phi-3 ONNX محلي باستخدام مكتبات `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 أو Phi-3.5 | دردشة نموذجية في وحدة التحكم تتيح للمستخدم طرح الأسئلة. يقوم المشروع بتحميل نموذج Phi-3 ONNX محلي باستخدام مكتبات `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 أو Phi-3.5 | مشروع نموذجي يستخدم نموذج phi3 vision محلي لتحليل الصور. يقوم المشروع بتحميل نموذج Phi-3 Vision ONNX محلي باستخدام مكتبات `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 أو Phi-3.5 | مشروع نموذجي يستخدم نموذج phi3 vision محلي لتحليل الصور. يقوم المشروع بتحميل نموذج Phi-3 Vision ONNX محلي باستخدام مكتبات `Microsoft.ML.OnnxRuntime`. كما يعرض المشروع قائمة بخيارات مختلفة للتفاعل مع المستخدم. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | دردشة نموذجية في وحدة التحكم تتيح للمستخدم طرح الأسئلة. يقوم المشروع بتحميل نموذج Phi-4 ONNX محلي باستخدام مكتبات `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | دردشة نموذجية في وحدة التحكم تتيح للمستخدم طرح الأسئلة. يقوم المشروع بتحميل نموذج Phi-4 ONNX محلي باستخدام مكتبات `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | دردشة نموذجية في وحدة التحكم تتيح للمستخدم طرح الأسئلة. يقوم المشروع بتحميل نموذج Phi-4 ONNX محلي باستخدام مكتبات `Microsoft.ML.OnnxRuntimeGenAI` ويطبق `IChatClient` من `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | دردشة نموذجية في وحدة التحكم تتيح للمستخدم طرح الأسئلة. الدردشة تدعم الذاكرة. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | مشروع نموذجي يستخدم نموذج Phi-4 محلي لتحليل الصور وعرض النتائج في وحدة التحكم. يقوم المشروع بتحميل نموذج Phi-4-`multimodal-instruct-onnx` محلي باستخدام مكتبات `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | مشروع نموذجي يستخدم نموذج Phi-4 محلي لتحليل ملف صوتي، إنشاء نص الملف وعرض النتيجة في وحدة التحكم. يقوم المشروع بتحميل نموذج Phi-4-`multimodal-instruct-onnx` محلي باستخدام مكتبات `Microsoft.ML.OnnxRuntime`. |

## كيفية تشغيل المشاريع

لتشغيل المشاريع، اتبع الخطوات التالية:

1. استنسخ المستودع إلى جهازك المحلي.

1. افتح الطرفية وانتقل إلى المشروع المطلوب. على سبيل المثال، لنشغل `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. شغّل المشروع باستخدام الأمر

    ```bash
    dotnet run
    ```

1. يطلب المشروع النموذجي إدخال من المستخدم ويرد باستخدام النموذج المحلي.

   العرض الجاري مشابه لهذا:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.