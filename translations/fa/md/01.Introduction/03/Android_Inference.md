<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-03-27T07:09:14+00:00",
  "source_file": "md\\01.Introduction\\03\\Android_Inference.md",
  "language_code": "fa"
}
-->
# **استنتاج Phi-3 در اندروید**

بیایید بررسی کنیم که چگونه می‌توانید استنتاج Phi-3-mini را روی دستگاه‌های اندرویدی انجام دهید. Phi-3-mini یک سری جدید از مدل‌های مایکروسافت است که امکان استفاده از مدل‌های زبانی بزرگ (LLMs) را روی دستگاه‌های لبه و دستگاه‌های IoT فراهم می‌کند.

## Semantic Kernel و استنتاج

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) یک چارچوب برنامه‌نویسی است که به شما اجازه می‌دهد برنامه‌هایی سازگار با Azure OpenAI Service، مدل‌های OpenAI، و حتی مدل‌های محلی ایجاد کنید. اگر با Semantic Kernel آشنا نیستید، پیشنهاد می‌کنیم به [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) مراجعه کنید.

### دسترسی به Phi-3-mini با استفاده از Semantic Kernel

می‌توانید از این چارچوب همراه با Hugging Face Connector در Semantic Kernel استفاده کنید. به این [نمونه کد](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) مراجعه کنید.

به طور پیش‌فرض، این مدل با شناسه مدل در Hugging Face سازگار است. با این حال، شما می‌توانید به یک سرور مدل Phi-3-mini که به صورت محلی ساخته شده نیز متصل شوید.

### اجرای مدل‌های کم‌حجم‌شده با Ollama یا LlamaEdge

بسیاری از کاربران ترجیح می‌دهند از مدل‌های کم‌حجم‌شده برای اجرای مدل‌ها به صورت محلی استفاده کنند. [Ollama](https://ollama.com/) و [LlamaEdge](https://llamaedge.com) به کاربران اجازه می‌دهند مدل‌های کم‌حجم‌شده مختلفی را اجرا کنند:

#### Ollama

می‌توانید به طور مستقیم `ollama run Phi-3` را اجرا کنید یا آن را به صورت آفلاین با ایجاد یک `Modelfile` که به مسیر فایل `.gguf` شما اشاره می‌کند، پیکربندی کنید.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[نمونه کد](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

اگر می‌خواهید از فایل‌های `.gguf` هم در فضای ابری و هم روی دستگاه‌های لبه استفاده کنید، LlamaEdge یک انتخاب عالی است. می‌توانید برای شروع به این [نمونه کد](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) مراجعه کنید.

### نصب و اجرا روی گوشی‌های اندرویدی

1. **اپلیکیشن MLC Chat را دانلود کنید** (رایگان) برای گوشی‌های اندرویدی.
2. فایل APK (148 مگابایت) را دانلود و روی دستگاه خود نصب کنید.
3. اپلیکیشن MLC Chat را اجرا کنید. لیستی از مدل‌های هوش مصنوعی از جمله Phi-3-mini را مشاهده خواهید کرد.

به طور خلاصه، Phi-3-mini امکان‌های هیجان‌انگیزی را برای هوش مصنوعی مولد روی دستگاه‌های لبه فراهم می‌کند و شما می‌توانید از قابلیت‌های آن روی اندروید بهره‌مند شوید.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را رعایت کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه انسانی حرفه‌ای استفاده کنید. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.