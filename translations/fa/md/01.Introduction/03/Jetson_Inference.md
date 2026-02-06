# **استنتاج Phi-3 در Nvidia Jetson**

Nvidia Jetson مجموعه‌ای از بردهای محاسباتی تعبیه‌شده از شرکت Nvidia است. مدل‌های Jetson TK1، TX1 و TX2 همگی دارای پردازنده Tegra (یا SoC) از Nvidia هستند که واحد پردازش مرکزی (CPU) با معماری ARM را در خود جای داده‌اند. Jetson سیستمی کم‌مصرف است و برای تسریع برنامه‌های یادگیری ماشین طراحی شده است. Nvidia Jetson توسط توسعه‌دهندگان حرفه‌ای برای خلق محصولات پیشرفته هوش مصنوعی در تمامی صنایع استفاده می‌شود و همچنین دانشجویان و علاقه‌مندان برای یادگیری عملی هوش مصنوعی و ساخت پروژه‌های شگفت‌انگیز از آن بهره می‌برند. SLM در دستگاه‌های لبه‌ای مانند Jetson مستقر می‌شود که امکان پیاده‌سازی بهتر سناریوهای کاربردی هوش مصنوعی مولد صنعتی را فراهم می‌کند.

## استقرار روی NVIDIA Jetson:
توسعه‌دهندگانی که روی رباتیک خودران و دستگاه‌های تعبیه‌شده کار می‌کنند، می‌توانند از Phi-3 Mini بهره ببرند. اندازه نسبتاً کوچک Phi-3 آن را برای استقرار در لبه ایده‌آل می‌کند. پارامترها در طول آموزش با دقت تنظیم شده‌اند تا دقت بالایی در پاسخ‌ها تضمین شود.

### بهینه‌سازی TensorRT-LLM:
کتابخانه [TensorRT-LLM شرکت NVIDIA](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) استنتاج مدل‌های زبان بزرگ را بهینه می‌کند. این کتابخانه از پنجره متنی طولانی Phi-3 Mini پشتیبانی می‌کند و هم توان عملیاتی و هم تأخیر را بهبود می‌بخشد. بهینه‌سازی‌ها شامل تکنیک‌هایی مانند LongRoPE، FP8 و پردازش دسته‌ای در حال اجرا هستند.

### در دسترس بودن و استقرار:
توسعه‌دهندگان می‌توانند Phi-3 Mini با پنجره متنی 128K را در [NVIDIA AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/) بررسی کنند. این مدل به صورت یک NVIDIA NIM بسته‌بندی شده است، یک میکروسرویس با API استاندارد که می‌توان آن را در هر جایی مستقر کرد. همچنین، پیاده‌سازی‌های [TensorRT-LLM در گیت‌هاب](https://github.com/NVIDIA/TensorRT-LLM) در دسترس است.

## **1. آماده‌سازی**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+

c. Cuda 11.8

d. Python 3.8+

## **2. اجرای Phi-3 در Jetson**

می‌توانیم از [Ollama](https://ollama.com) یا [LlamaEdge](https://llamaedge.com) استفاده کنیم.

اگر می‌خواهید از gguf همزمان در فضای ابری و دستگاه‌های لبه‌ای استفاده کنید، LlamaEdge را می‌توان به عنوان WasmEdge در نظر گرفت (WasmEdge یک محیط اجرای WebAssembly سبک، با عملکرد بالا و مقیاس‌پذیر است که برای برنامه‌های بومی ابری، لبه و غیرمتمرکز مناسب است. این محیط از برنامه‌های بدون سرور، توابع تعبیه‌شده، میکروسرویس‌ها، قراردادهای هوشمند و دستگاه‌های IoT پشتیبانی می‌کند. شما می‌توانید مدل کمی‌شده gguf را از طریق LlamaEdge روی دستگاه‌های لبه‌ای و فضای ابری مستقر کنید).

![llamaedge](../../../../../translated_images/fa/llamaedge.e9d6ff96dff11cf7.webp)

مراحل استفاده به شرح زیر است:

1. نصب و دانلود کتابخانه‌ها و فایل‌های مرتبط

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**توجه**: فایل‌های llama-api-server.wasm و chatbot-ui باید در یک پوشه قرار داشته باشند.

2. اجرای اسکریپت‌ها در ترمینال

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

نتیجه اجرای برنامه به شکل زیر است:

![llamaedgerun](../../../../../translated_images/fa/llamaedgerun.bed921516c9a821c.webp)

***نمونه کد*** [نمونه دفترچه Phi-3 mini WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

در مجموع، Phi-3 Mini جهشی بزرگ در مدل‌سازی زبان است که کارایی، آگاهی از زمینه و توان بهینه‌سازی NVIDIA را ترکیب می‌کند. چه در حال ساخت ربات باشید و چه برنامه‌های لبه‌ای، Phi-3 Mini ابزاری قدرتمند است که باید آن را بشناسید.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده از این ترجمه ناشی شود، نیستیم.