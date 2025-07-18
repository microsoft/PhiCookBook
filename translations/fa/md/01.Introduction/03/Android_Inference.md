<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-07-16T20:11:04+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "fa"
}
-->
# **استنتاج Phi-3 در اندروید**

بیایید ببینیم چگونه می‌توانید با Phi-3-mini روی دستگاه‌های اندرویدی استنتاج انجام دهید. Phi-3-mini یک سری مدل جدید از مایکروسافت است که امکان استقرار مدل‌های زبان بزرگ (LLM) را روی دستگاه‌های لبه و دستگاه‌های اینترنت اشیا فراهم می‌کند.

## Semantic Kernel و استنتاج

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) یک چارچوب برنامه‌نویسی است که به شما اجازه می‌دهد برنامه‌هایی سازگار با Azure OpenAI Service، مدل‌های OpenAI و حتی مدل‌های محلی بسازید. اگر با Semantic Kernel آشنا نیستید، پیشنهاد می‌کنیم به [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) نگاهی بیندازید.

### دسترسی به Phi-3-mini با استفاده از Semantic Kernel

می‌توانید آن را با Hugging Face Connector در Semantic Kernel ترکیب کنید. به این [نمونه کد](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) مراجعه کنید.

به طور پیش‌فرض، این به شناسه مدل در Hugging Face اشاره دارد. اما همچنین می‌توانید به سرور مدل Phi-3-mini ساخته شده به صورت محلی متصل شوید.

### فراخوانی مدل‌های کوانتیزه شده با Ollama یا LlamaEdge

بسیاری از کاربران ترجیح می‌دهند از مدل‌های کوانتیزه شده برای اجرای مدل‌ها به صورت محلی استفاده کنند. [Ollama](https://ollama.com/) و [LlamaEdge](https://llamaedge.com) به کاربران فردی اجازه می‌دهند مدل‌های کوانتیزه مختلف را فراخوانی کنند:

#### Ollama

می‌توانید به طور مستقیم دستور `ollama run Phi-3` را اجرا کنید یا به صورت آفلاین با ایجاد یک `Modelfile` که مسیر فایل `.gguf` شما را دارد، آن را پیکربندی کنید.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[نمونه کد](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

اگر می‌خواهید از فایل‌های `.gguf` به صورت همزمان در فضای ابری و دستگاه‌های لبه استفاده کنید، LlamaEdge گزینه بسیار خوبی است. می‌توانید برای شروع به این [نمونه کد](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) مراجعه کنید.

### نصب و اجرا روی گوشی‌های اندرویدی

1. **اپلیکیشن MLC Chat را دانلود کنید** (رایگان) برای گوشی‌های اندرویدی.
2. فایل APK (با حجم ۱۴۸ مگابایت) را دانلود و روی دستگاه خود نصب کنید.
3. اپلیکیشن MLC Chat را اجرا کنید. فهرستی از مدل‌های هوش مصنوعی، از جمله Phi-3-mini، مشاهده خواهید کرد.

در مجموع، Phi-3-mini امکانات هیجان‌انگیزی برای هوش مصنوعی مولد روی دستگاه‌های لبه فراهم می‌کند و می‌توانید شروع به کاوش قابلیت‌های آن روی اندروید کنید.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.