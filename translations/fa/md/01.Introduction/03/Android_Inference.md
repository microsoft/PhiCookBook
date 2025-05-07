<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-07T14:31:03+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "fa"
}
-->
# **استنتاج Phi-3 در اندروید**

بیایید بررسی کنیم چگونه می‌توانید با Phi-3-mini روی دستگاه‌های اندرویدی استنتاج انجام دهید. Phi-3-mini سری جدیدی از مدل‌های مایکروسافت است که امکان استقرار مدل‌های زبان بزرگ (LLM) را روی دستگاه‌های لبه و اینترنت اشیاء فراهم می‌کند.

## Semantic Kernel و استنتاج

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) یک چارچوب کاربردی است که به شما اجازه می‌دهد برنامه‌هایی سازگار با Azure OpenAI Service، مدل‌های OpenAI و حتی مدل‌های محلی بسازید. اگر با Semantic Kernel تازه‌کار هستید، پیشنهاد می‌کنیم به [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) نگاهی بیندازید.

### دسترسی به Phi-3-mini با استفاده از Semantic Kernel

می‌توانید آن را با Hugging Face Connector در Semantic Kernel ترکیب کنید. به این [کد نمونه](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) مراجعه کنید.

به طور پیش‌فرض، این به شناسه مدل در Hugging Face مربوط می‌شود. با این حال، می‌توانید به سرور مدل Phi-3-mini ساخته شده به صورت محلی نیز متصل شوید.

### فراخوانی مدل‌های کوانتیزه شده با Ollama یا LlamaEdge

بسیاری از کاربران ترجیح می‌دهند برای اجرای مدل‌ها به صورت محلی از مدل‌های کوانتیزه شده استفاده کنند. [Ollama](https://ollama.com/) و [LlamaEdge](https://llamaedge.com) به کاربران فردی اجازه می‌دهند مدل‌های کوانتیزه مختلف را فراخوانی کنند:

#### Ollama

می‌توانید به طور مستقیم `ollama run Phi-3` را اجرا کنید یا به صورت آفلاین آن را با ایجاد یک `Modelfile` که مسیر فایل `.gguf` شما را دارد، پیکربندی کنید.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[کد نمونه](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

اگر می‌خواهید از فایل‌های `.gguf` به طور همزمان در فضای ابری و دستگاه‌های لبه استفاده کنید، LlamaEdge گزینه بسیار خوبی است. می‌توانید برای شروع به این [کد نمونه](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) مراجعه کنید.

### نصب و اجرا روی گوشی‌های اندروید

1. **برنامه MLC Chat را دانلود کنید** (رایگان) برای گوشی‌های اندروید.
2. فایل APK (با حجم ۱۴۸ مگابایت) را دانلود کرده و روی دستگاه خود نصب کنید.
3. برنامه MLC Chat را اجرا کنید. فهرستی از مدل‌های هوش مصنوعی از جمله Phi-3-mini را خواهید دید.

در خلاصه، Phi-3-mini امکانات هیجان‌انگیزی برای هوش مصنوعی مولد روی دستگاه‌های لبه فراهم می‌کند و می‌توانید قابلیت‌های آن را روی اندروید شروع به کاوش کنید.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی اشتباهات یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که ناشی از استفاده از این ترجمه باشد، نیستیم.