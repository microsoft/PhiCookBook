<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-07T10:43:01+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "ar"
}
-->
في سياق Phi-3-mini، يشير الاستدلال إلى عملية استخدام النموذج لإجراء التنبؤات أو توليد المخرجات بناءً على بيانات الإدخال. دعني أوضح لك المزيد عن Phi-3-mini وقدراته في الاستدلال.

يُعد Phi-3-mini جزءًا من سلسلة نماذج Phi-3 التي أصدرتها مايكروسوفت. تم تصميم هذه النماذج لإعادة تعريف ما هو ممكن مع نماذج اللغة الصغيرة (SLMs).

إليك بعض النقاط الرئيسية حول Phi-3-mini وقدراته في الاستدلال:

## **نظرة عامة على Phi-3-mini:**
- يمتلك Phi-3-mini حجم معلمات يبلغ 3.8 مليار.
- يمكن تشغيله ليس فقط على أجهزة الحوسبة التقليدية، بل أيضًا على أجهزة الحافة مثل الأجهزة المحمولة وأجهزة إنترنت الأشياء.
- يتيح إصدار Phi-3-mini للأفراد والمؤسسات نشر نماذج اللغة الصغيرة على أجهزة مختلفة، خاصة في البيئات ذات الموارد المحدودة.
- يغطي تنسيقات نموذج متعددة، بما في ذلك تنسيق PyTorch التقليدي، النسخة المكممة من تنسيق gguf، والنسخة المكممة المعتمدة على ONNX.

## **الوصول إلى Phi-3-mini:**
للوصول إلى Phi-3-mini، يمكنك استخدام [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) في تطبيق Copilot. يتوافق Semantic Kernel عمومًا مع خدمة Azure OpenAI، النماذج مفتوحة المصدر على Hugging Face، والنماذج المحلية.
يمكنك أيضًا استخدام [Ollama](https://ollama.com) أو [LlamaEdge](https://llamaedge.com) لاستدعاء النماذج المكممة. يسمح Ollama للمستخدمين الأفراد باستدعاء نماذج مكممة مختلفة، بينما يوفر LlamaEdge توفرًا عبر المنصات لنماذج GGUF.

## **النماذج المكممة:**
يفضل العديد من المستخدمين استخدام النماذج المكممة للاستدلال المحلي. على سبيل المثال، يمكنك تشغيل Phi-3 مباشرة عبر Ollama أو تكوينه دون اتصال باستخدام Modelfile. يحدد Modelfile مسار ملف GGUF وصيغة الموجه.

## **إمكانيات الذكاء الاصطناعي التوليدي:**
يتيح الجمع بين نماذج اللغة الصغيرة مثل Phi-3-mini إمكانيات جديدة للذكاء الاصطناعي التوليدي. الاستدلال هو الخطوة الأولى فقط؛ يمكن استخدام هذه النماذج في مهام متنوعة في سيناريوهات محدودة الموارد، وذات زمن استجابة محدود، وذات تكلفة مقيدة.

## **فتح إمكانيات الذكاء الاصطناعي التوليدي مع Phi-3-mini: دليل للاستدلال والنشر**
تعلم كيفية استخدام Semantic Kernel، وOllama/LlamaEdge، وONNX Runtime للوصول إلى نماذج Phi-3-mini والاستدلال عليها، واستكشف إمكانيات الذكاء الاصطناعي التوليدي في سيناريوهات تطبيقية متنوعة.

**الميزات**
استدلال نموذج phi3-mini في:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

باختصار، يتيح Phi-3-mini للمطورين استكشاف تنسيقات نموذج مختلفة والاستفادة من الذكاء الاصطناعي التوليدي في سيناريوهات تطبيقية متنوعة.

**إخلاء مسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاستعانة بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.