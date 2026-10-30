# **اجرای استنتاج Phi-3 در اندروید**

بیایید بررسی کنیم چگونه می‌توانید استنتاج را با Phi-3-mini در دستگاه‌های اندرویدی انجام دهید. Phi-3-mini یک سری جدید از مدل‌ها از مایکروسافت است که امکان استقرار مدل‌های زبانی بزرگ (LLMs) را در دستگاه‌های لبه و دستگاه‌های اینترنت اشیا فراهم می‌کند.

## Semantic Kernel و استنتاج

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) یک چارچوب برنامه‌نویسی است که به شما امکان می‌دهد برنامه‌هایی ایجاد کنید که با سرویس Azure OpenAI، مدل‌های OpenAI و حتی مدل‌های محلی سازگار باشند. اگر با Semantic Kernel تازه آشنا هستید، پیشنهاد می‌کنیم به [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) نگاهی بیندازید.

### برای دسترسی به Phi-3-mini با استفاده از Semantic Kernel

می‌توانید آن را با اتصال Hugging Face در Semantic Kernel ترکیب کنید. به این [نمونه کد](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo) مراجعه کنید.

به طور پیش‌فرض، این به شناسه مدل در Hugging Face اشاره دارد. با این حال، می‌توانید به سرور مدل Phi-3-mini ساخته شده محلی نیز متصل شوید.

### فراخوانی مدل‌های کم‌یابی شده با Ollama یا LlamaEdge

بسیاری از کاربران ترجیح می‌دهند از مدل‌های کم‌یابی شده برای اجرای مدل‌ها به صورت محلی استفاده کنند. [Ollama](https://ollama.com/) و [LlamaEdge](https://llamaedge.com) به کاربران فردی اجازه می‌دهند مدل‌های کم‌یابی شده مختلف را صدا بزنند:

#### Ollama

شما می‌توانید به‌طور مستقیم `ollama run Phi-3` را اجرا کنید یا به صورت آفلاین با ایجاد یک `Modelfile` که مسیر فایل `.gguf` شما را دارد، آن را پیکربندی کنید.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[نمونه کد](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

اگر می‌خواهید فایل‌های `.gguf` را به‌صورت همزمان در فضای ابری و دستگاه‌های لبه استفاده کنید، LlamaEdge انتخاب بسیار مناسبی است. می‌توانید برای شروع به این [نمونه کد](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) مراجعه کنید.

### نصب و اجرا روی گوشی‌های اندروید

1. **اپلیکیشن MLC Chat** (رایگان) را برای گوشی‌های اندروید دانلود کنید.
2. فایل APK (حجم 148 مگابایت) را دانلود کرده و آن را روی دستگاه خود نصب کنید.
3. اپلیکیشن MLC Chat را اجرا کنید. لیستی از مدل‌های هوش مصنوعی، از جمله Phi-3-mini، خواهید دید.

### اجرای Phi-4-mini-reasoning با LiteRT-LM

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning) به‌عنوان یک بسته int4 تبدیل شده توسط جامعه به صورت `.litertlm` برای زمان اجرای روی دستگاه [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) گوگل در دسترس است. در اندروید، این بسته روی CPU یا GPU از طریق برنامه [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) اجرا می‌شود (بسته را از Hugging Face داخل برنامه وارد کنید) یا از طریق API کاتلین LiteRT-LM؛ همین بسته روی iOS، macOS، لینوکس و ویندوز نیز اجرا می‌شود. کارت مدل سرعت‌های اندازه‌گیری شده و دستورات اجرا را فهرست می‌کند.

در خلاصه، Phi-3-mini امکانات هیجان‌انگیزی برای هوش مصنوعی مولد روی دستگاه‌های لبه فراهم می‌کند، و شما می‌توانید شروع به کاوش قابلیت‌های آن در اندروید کنید.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->