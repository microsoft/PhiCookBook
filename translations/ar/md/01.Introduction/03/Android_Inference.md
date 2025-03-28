<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-03-27T07:08:13+00:00",
  "source_file": "md\\01.Introduction\\03\\Android_Inference.md",
  "language_code": "ar"
}
-->
# **استخدام Phi-3 في أجهزة الأندرويد**

دعونا نستعرض كيفية إجراء استدلال باستخدام Phi-3-mini على أجهزة الأندرويد. Phi-3-mini هي سلسلة جديدة من النماذج من مايكروسوفت تتيح نشر نماذج اللغة الكبيرة (LLMs) على الأجهزة الطرفية وأجهزة إنترنت الأشياء.

## Semantic Kernel والاستدلال

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) هو إطار عمل للتطبيقات يتيح لك إنشاء تطبيقات متوافقة مع Azure OpenAI Service ونماذج OpenAI وحتى النماذج المحلية. إذا كنت جديدًا على Semantic Kernel، نقترح عليك الاطلاع على [دليل Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### الوصول إلى Phi-3-mini باستخدام Semantic Kernel

يمكنك دمجه مع موصل Hugging Face في Semantic Kernel. راجع هذا [الكود التجريبي](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

بشكل افتراضي، يتوافق مع معرف النموذج في Hugging Face. ومع ذلك، يمكنك أيضًا الاتصال بخادم نموذج Phi-3-mini محلي.

### استدعاء النماذج المضغوطة باستخدام Ollama أو LlamaEdge

يفضل العديد من المستخدمين استخدام النماذج المضغوطة لتشغيل النماذج محليًا. [Ollama](https://ollama.com/) و[LlamaEdge](https://llamaedge.com) تتيحان للمستخدمين الأفراد استدعاء نماذج مضغوطة مختلفة:

#### Ollama

يمكنك تشغيل `ollama run Phi-3` مباشرة أو تكوينه للعمل دون اتصال عن طريق إنشاء `Modelfile` مع المسار إلى ملف `.gguf` الخاص بك.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[الكود التجريبي](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

إذا كنت ترغب في استخدام ملفات `.gguf` في السحابة وعلى الأجهزة الطرفية في نفس الوقت، فإن LlamaEdge هو خيار رائع. يمكنك الرجوع إلى هذا [الكود التجريبي](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) للبدء.

### التثبيت والتشغيل على هواتف الأندرويد

1. **قم بتحميل تطبيق MLC Chat** (مجاني) لهواتف الأندرويد.
2. قم بتحميل ملف APK (بحجم 148 ميغابايت) وثبته على جهازك.
3. افتح تطبيق MLC Chat. ستظهر لك قائمة بالنماذج الذكية، بما في ذلك Phi-3-mini.

باختصار، يفتح Phi-3-mini آفاقًا مثيرة للذكاء الاصطناعي التوليدي على الأجهزة الطرفية، ويمكنك البدء في استكشاف إمكانياته على الأندرويد.

**إخلاء مسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.