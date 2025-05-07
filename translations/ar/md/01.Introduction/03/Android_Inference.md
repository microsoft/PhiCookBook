<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-07T10:43:47+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "ar"
}
-->
# **الاستدلال Phi-3 على أندرويد**

دعونا نستعرض كيف يمكنك إجراء الاستدلال باستخدام Phi-3-mini على أجهزة أندرويد. تعد Phi-3-mini سلسلة جديدة من النماذج من مايكروسوفت تتيح نشر نماذج اللغة الكبيرة (LLMs) على أجهزة الحافة وأجهزة إنترنت الأشياء.

## Semantic Kernel والاستدلال

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) هو إطار عمل تطبيقي يسمح لك بإنشاء تطبيقات متوافقة مع خدمة Azure OpenAI، ونماذج OpenAI، وحتى النماذج المحلية. إذا كنت جديدًا على Semantic Kernel، نوصيك بالاطلاع على [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### للوصول إلى Phi-3-mini باستخدام Semantic Kernel

يمكنك دمجه مع موصل Hugging Face في Semantic Kernel. راجع هذا [الكود النموذجي](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

افتراضيًا، يتوافق مع معرف النموذج على Hugging Face. ومع ذلك، يمكنك أيضًا الاتصال بخادم نموذج Phi-3-mini المبني محليًا.

### استدعاء النماذج الكمية باستخدام Ollama أو LlamaEdge

يفضل العديد من المستخدمين استخدام النماذج الكمية لتشغيل النماذج محليًا. يتيح [Ollama](https://ollama.com/) و [LlamaEdge](https://llamaedge.com) للمستخدمين الأفراد استدعاء نماذج كمية مختلفة:

#### Ollama

يمكنك تشغيل `ollama run Phi-3` مباشرة أو تكوينه بدون اتصال بإنشاء `Modelfile` مع المسار إلى ملف `.gguf` الخاص بك.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[كود نموذجي](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

إذا كنت ترغب في استخدام ملفات `.gguf` في السحابة وعلى أجهزة الحافة في نفس الوقت، فإن LlamaEdge خيار ممتاز. يمكنك الرجوع إلى هذا [الكود النموذجي](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) للبدء.

### التثبيت والتشغيل على هواتف أندرويد

1. **قم بتنزيل تطبيق MLC Chat** (مجاني) لهواتف أندرويد.  
2. حمّل ملف APK (بحجم 148 ميجابايت) وقم بتثبيته على جهازك.  
3. افتح تطبيق MLC Chat. سترى قائمة بنماذج الذكاء الاصطناعي، بما في ذلك Phi-3-mini.

باختصار، يفتح Phi-3-mini آفاقًا مثيرة للذكاء الاصطناعي التوليدي على أجهزة الحافة، ويمكنك البدء في استكشاف إمكانياته على أندرويد.

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.