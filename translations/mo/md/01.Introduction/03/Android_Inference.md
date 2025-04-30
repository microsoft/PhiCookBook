<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b909b4ac6465d33e81adb17df38deef3",
  "translation_date": "2025-04-04T11:59:27+00:00",
  "source_file": "md\\01.Introduction\\03\\Android_Inference.md",
  "language_code": "mo"
}
-->
# **Inference Phi-3 په Android کې**

راځئ چې وګورو څنګه کولای شئ په Android وسیلو کې د Phi-3-mini سره inference ترسره کړئ. Phi-3-mini د مایکروسافټ نوې ماډل لړۍ ده چې د لوی ژبنیو ماډلونو (LLMs) د edge وسیلو او IoT وسیلو کې ځای پر ځای کولو ته اجازه ورکوي.

## د Semantic Kernel او Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) یو اپلیکیشن چوکاټ دی چې تاسو ته اجازه درکوي د Azure OpenAI Service، د OpenAI ماډلونو، او حتی محلي ماډلونو سره سازګار اپلیکیشنونه جوړ کړئ. که تاسو د Semantic Kernel سره نوي یاست، موږ وړاندیز کوو چې د [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) وګورئ.

### د Phi-3-mini ته د لاسرسي لپاره د Semantic Kernel کارول

تاسو کولی شئ دا د Semantic Kernel کې د Hugging Face Connector سره یوځای کړئ. د دې لپاره دې [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) ته مراجعه وکړئ.

په ډیفالټ توګه، دا د Hugging Face د ماډل ID سره مطابقت لري. خو تاسو کولی شئ د محلي جوړ شوي Phi-3-mini ماډل سرور سره هم وصل شئ.

### د Quantized ماډلونو غوښتنه د Ollama یا LlamaEdge سره

ډیری کاروونکي د ماډلونو محلي چلولو لپاره د Quantized ماډلونو کارولو ته ترجیح ورکوي. [Ollama](https://ollama.com/) او [LlamaEdge](https://llamaedge.com) انفرادي کاروونکو ته اجازه ورکوي چې مختلف Quantized ماډلونه وغواړي:

#### Ollama

تاسو کولی شئ په مستقیم ډول `ollama run Phi-3` اجرا کړئ یا دا آفلاین ترتیب کړئ د `Modelfile` په جوړولو سره چې د `.gguf` فایل ته لارښود کوي.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

که تاسو غواړئ `.gguf` فایلونه په کلاوډ او edge وسیلو کې په یو وخت کې وکاروئ، LlamaEdge یوه غوره انتخاب ده. د پیل لپاره تاسو دې [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) ته مراجعه وکړئ.

### په Android موبایلونو کې نصب او چلول

1. **د MLC Chat اپلیکیشن ډاونلوډ کړئ** (وړیا) د Android موبایلونو لپاره.
2. د APK فایل (148MB) ډاونلوډ کړئ او په خپل وسیله یې نصب کړئ.
3. د MLC Chat اپلیکیشن لانچ کړئ. تاسو به د AI ماډلونو لیست وګورئ چې Phi-3-mini پکې شامل دی.

په لنډ ډول، Phi-3-mini د جنریټیف AI لپاره په edge وسیلو کې د زړه پورې امکاناتو دروازې پرانیزي، او تاسو کولی شئ په Android کې د دې وړتیاوې وپلټئ.

It seems like "mo" might refer to a specific language, but it's not clear which one you're referring to. Could you please clarify the language you'd like me to translate the text into? For example, is it Maori, Mongolian, or something else? Let me know so I can assist you accurately!