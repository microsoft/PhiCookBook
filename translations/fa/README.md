<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f2577190cbe70305b9de13df37e1c9a",
  "translation_date": "2025-04-03T05:56:11+00:00",
  "source_file": "README.md",
  "language_code": "fa"
}
-->
# کتاب آشپزی فی: مثال‌های عملی با مدل‌های فی مایکروسافت

فی مجموعه‌ای از مدل‌های هوش مصنوعی متن‌باز است که توسط مایکروسافت توسعه یافته‌اند.

فی در حال حاضر قدرتمندترین و مقرون‌به‌صرفه‌ترین مدل زبان کوچک (SLM) است که در معیارهای چندزبانه، استدلال، تولید متن/چت، کدنویسی، تصاویر، صوت و سایر سناریوها عملکرد بسیار خوبی دارد.

شما می‌توانید فی را در فضای ابری یا دستگاه‌های لبه‌ای مستقر کنید و به راحتی برنامه‌های هوش مصنوعی تولیدی را با قدرت محاسباتی محدود بسازید.

برای شروع استفاده از این منابع، مراحل زیر را دنبال کنید:
1. **مخزن را فورک کنید**: کلیک کنید [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **مخزن را کلون کنید**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**به جامعه دیسکورد هوش مصنوعی مایکروسافت بپیوندید و با کارشناسان و توسعه‌دهندگان دیگر ملاقات کنید**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![کاور](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.fa.png)

## 🌐 پشتیبانی چندزبانه
[فرانسوی](../fr/README.md) | [اسپانیایی](../es/README.md) | [آلمانی](../de/README.md) | [روسی](../ru/README.md) | [عربی](../ar/README.md) | [فارسی](./README.md) | [اردو](../ur/README.md) | [چینی (ساده‌شده)](../zh/README.md) | [چینی (سنتی، ماکائو)](../mo/README.md) | [چینی (سنتی، هنگ کنگ)](../hk/README.md) | [چینی (سنتی، تایوان)](../tw/README.md) | [ژاپنی](../ja/README.md) | [کره‌ای](../ko/README.md) | [هندی](../hi/README.md) | [بنگالی](../bn/README.md) | [مراتی](../mr/README.md) | [نپالی](../ne/README.md) | [پنجابی (گورمخی)](../pa/README.md) | [پرتغالی (پرتغال)](../pt/README.md) | [پرتغالی (برزیل)](../br/README.md) | [ایتالیایی](../it/README.md) | [لهستانی](../pl/README.md) | [ترکی](../tr/README.md) | [یونانی](../el/README.md) | [تایلندی](../th/README.md) | [سوئدی](../sv/README.md) | [دانمارکی](../da/README.md) | [نروژی](../no/README.md) | [فنلاندی](../fi/README.md) | [هلندی](../nl/README.md) | [عبری](../he/README.md) | [ویتنامی](../vi/README.md) | [اندونزیایی](../id/README.md) | [مالایی](../ms/README.md) | [تاگالوگ (فیلیپینی)](../tl/README.md) | [سواحیلی](../sw/README.md) | [مجاری](../hu/README.md) | [چکی](../cs/README.md) | [اسلواکی](../sk/README.md) | [رومانیایی](../ro/README.md) | [بلغاری](../bg/README.md) | [صربی (سیریلیک)](../sr/README.md) | [کرواتی](../hr/README.md) | [اسلوونیایی](../sl/README.md)
## فهرست مطالب

- مقدمه
  - [خوش‌آمدید به خانواده فی](./md/01.Introduction/01/01.PhiFamily.md)
  - [راه‌اندازی محیط خود](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [درک فناوری‌های کلیدی](./md/01.Introduction/01/01.Understandingtech.md)
  - [ایمنی هوش مصنوعی برای مدل‌های فی](./md/01.Introduction/01/01.AISafety.md)
  - [پشتیبانی سخت‌افزاری فی](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [مدل‌های فی و دسترسی در پلتفرم‌های مختلف](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [استفاده از Guidance-ai و فی](./md/01.Introduction/01/01.Guidance.md)
  - [مدل‌های مارکت‌پلیس گیت‌هاب](https://github.com/marketplace/models)
  - [کاتالوگ مدل‌های هوش مصنوعی آژور](https://ai.azure.com)

- استنتاج فی در محیط‌های مختلف
    - [هوجینگ فیس](./md/01.Introduction/02/01.HF.md)
    - [مدل‌های گیت‌هاب](./md/01.Introduction/02/02.GitHubModel.md)
    - [کاتالوگ مدل‌های آژور AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [اولاما](./md/01.Introduction/02/04.Ollama.md)
    - [ابزار هوش مصنوعی VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- استنتاج خانواده فی
    - [استنتاج فی در iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [استنتاج فی در اندروید](./md/01.Introduction/03/Android_Inference.md)
    - [استنتاج فی در Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [استنتاج فی در PC هوش مصنوعی](./md/01.Introduction/03/AIPC_Inference.md)
    - [استنتاج فی با فریم‌ورک MLX اپل](./md/01.Introduction/03/MLX_Inference.md)
    - [استنتاج فی در سرور محلی](./md/01.Introduction/03/Local_Server_Inference.md)
    - [استنتاج فی در سرور راه دور با استفاده از ابزار هوش مصنوعی](./md/01.Introduction/03/Remote_Interence.md)
    - [استنتاج فی با Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [استنتاج فی--ویژن به صورت محلی](./md/01.Introduction/03/Vision_Inference.md)
    - [استنتاج فی با Kaito AKS، کانتینرهای آژور (پشتیبانی رسمی)](./md/01.Introduction/03/Kaito_Inference.md)

- [کوانتیزه کردن خانواده فی](./md/01.Introduction/04/QuantifyingPhi.md)
    - [کوانتیزه کردن Phi-3.5 / 4 با استفاده از llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [کوانتیزه کردن Phi-3.5 / 4 با استفاده از افزونه‌های هوش مصنوعی مولد برای onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [کوانتیزه کردن Phi-3.5 / 4 با استفاده از Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [کوانتیزه کردن Phi-3.5 / 4 با استفاده از فریم‌ورک MLX اپل](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- ارزیابی فی
- [هوش مصنوعی مسئول](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry برای ارزیابی](./md/01.Introduction/05/AIFoundry.md)
    - [استفاده از Promptflow برای ارزیابی](./md/01.Introduction/05/Promptflow.md)

- RAG با Azure AI Search
    - [چگونه از Phi-4-mini و Phi-4-multimodal (RAG) با Azure AI Search استفاده کنیم](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- نمونه‌های توسعه برنامه Phi
  - برنامه‌های متن و چت
    - نمونه‌های Phi-4 🆕
      - [📓] [چت با مدل Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [چت با مدل محلی Phi-4 ONNX در .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [برنامه کنسول چت .NET با Phi-4 ONNX با استفاده از Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - نمونه‌های Phi-3 / 3.5
      - [چت‌بات محلی در مرورگر با استفاده از Phi3، ONNX Runtime Web و WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [چت OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [چند مدل - Phi-3-mini تعاملی و OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ساخت یک Wrapper و استفاده از Phi-3 با MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [بهینه‌سازی مدل - چگونه مدل Phi-3-min را برای ONNX Runtime Web با Olive بهینه کنیم](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [برنامه WinUI3 با Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [برنامه یادداشت‌های AI قدرتمند WinUI3 نمونه چندمدلی](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [تنظیم دقیق و ادغام مدل‌های سفارشی Phi-3 با Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [تنظیم دقیق و ادغام مدل‌های سفارشی Phi-3 با Prompt flow در Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [ارزیابی مدل تنظیم‌شده Phi-3 / Phi-3.5 در Azure AI Foundry با تمرکز بر اصول مسئول هوش مصنوعی مایکروسافت](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [نمونه پیش‌بینی زبان Phi-3.5-mini-instruct (چینی/انگلیسی)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [چت‌بات RAG WebGPU Phi-3.5-Instruct](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [استفاده از GPU ویندوز برای ایجاد راه‌حل Prompt flow با Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [استفاده از Microsoft Phi-3.5 tflite برای ایجاد برنامه اندروید](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [مثال پرسش و پاسخ .NET با استفاده از مدل محلی ONNX Phi-3 با Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [برنامه کنسول چت .NET با Semantic Kernel و Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - نمونه‌های کدنویسی SDK استنتاج Azure AI 
    - نمونه‌های Phi-4 🆕
      - [📓] [ایجاد کد پروژه با استفاده از Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - نمونه‌های Phi-3 / 3.5
      - [ساخت چت Visual Studio Code GitHub Copilot خود با خانواده Phi-3 مایکروسافت](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [ایجاد عامل چت Visual Studio Code خود با Phi-3.5 توسط مدل‌های GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - نمونه‌های استدلال پیشرفته
    - نمونه‌های Phi-4 🆕
      - [📓] [نمونه‌های استدلال Phi-4-mini](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)

  - دموها
      - [دموهای Phi-4-mini میزبانی شده در Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [دموهای Phi-4-multimodal میزبانی شده در Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - نمونه‌های دیداری
    - نمونه‌های Phi-4 🆕
      - [📓] [استفاده از Phi-4-multimodal برای خواندن تصاویر و تولید کد](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)
    - نمونه‌های Phi-3 / 3.5
- [📓][Phi-3-vision-Image text to text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
      - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
      - [دمو: Phi-3 بازیافت](https://github.com/jennifermarsman/PhiRecycling/)  
      - [Phi-3-vision - دستیار بصری زبان - با Phi3-Vision و OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
      - [📓][Phi-3.5 Vision نمونه چند قاب یا چند تصویر](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
      - [Phi-3 Vision مدل ONNX محلی با استفاده از Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
      - [مدل ONNX محلی Phi-3 Vision مبتنی بر منو با استفاده از Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

  - نمونه‌های صوتی  
    - Phi-4 نمونه‌ها 🆕  
      - [📓] [استخراج متن صوتی با استفاده از Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
      - [📓] [نمونه صوتی Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
      - [📓] [نمونه ترجمه گفتار Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
      - [.NET برنامه کنسول با استفاده از Phi-4-multimodal برای تحلیل فایل صوتی و تولید متن](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

  - نمونه‌های MOE  
    - Phi-3 / 3.5 نمونه‌ها  
      - [📓] [مدل‌های ترکیب متخصصین Phi-3.5 (MoEs) نمونه شبکه‌های اجتماعی](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
      - [📓] [ساخت یک خط لوله بازیابی-تقویت‌شده (RAG) با NVIDIA NIM Phi-3 MOE، Azure AI Search، و LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

  - نمونه‌های فراخوانی تابع  
    - Phi-4 نمونه‌ها 🆕  
      - [📓] [استفاده از فراخوانی تابع با Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
      - [📓] [استفاده از فراخوانی تابع برای ایجاد چند عامل با Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
      - [📓] [استفاده از فراخوانی تابع با Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  

  - نمونه‌های ترکیب چندحالته  
    - Phi-4 نمونه‌ها 🆕  
      - [📓] [استفاده از Phi-4-multimodal به عنوان یک روزنامه‌نگار فناوری](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
      - [.NET برنامه کنسول با استفاده از Phi-4-multimodal برای تحلیل تصاویر](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- نمونه‌های تنظیم دقیق Phi  
  - [سناریوهای تنظیم دقیق](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [تنظیم دقیق در مقابل RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [تنظیم دقیق اجازه دهید Phi-3 تبدیل به یک متخصص صنعت شود](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [تنظیم دقیق Phi-3 با ابزار AI برای VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [تنظیم دقیق Phi-3 با سرویس یادگیری ماشین Azure](./md/03.FineTuning/Introduce_AzureML.md)  
  - [تنظیم دقیق Phi-3 با Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [تنظیم دقیق Phi-3 با QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [تنظیم دقیق Phi-3 با Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [تنظیم دقیق Phi-3 با Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
- [فاین‌تیون کردن با Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [آزمایش عملی فاین‌تیون کردن با Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)  
  - [فاین‌تیون کردن Phi-3-vision با Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [فاین‌تیون کردن Phi-3 با فریم‌ورک Apple MLX](./md/03.FineTuning/FineTuning_MLX.md)  
  - [فاین‌تیون کردن Phi-3-vision (پشتیبانی رسمی)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [فاین‌تیون کردن Phi-3 با Kaito AKS و Azure Containers (پشتیبانی رسمی)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [فاین‌تیون کردن Phi-3 و Phi-3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- آزمایش عملی  
  - [بررسی مدل‌های پیشرفته: LLMs، SLMs، توسعه محلی و موارد دیگر](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [آزاد کردن پتانسیل NLP: فاین‌تیون کردن با Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- مقالات تحقیقاتی و انتشارات علمی  
  - [Textbooks Are All You Need II: گزارش فنی phi-1.5](https://arxiv.org/abs/2309.05463)  
  - [گزارش فنی Phi-3: یک مدل زبان بسیار قدرتمند روی گوشی شما](https://arxiv.org/abs/2404.14219)  
  - [گزارش فنی Phi-4](https://arxiv.org/abs/2412.08905)  
  - [گزارش فنی Phi-4-Mini: مدل‌های زبان چندوجهی فشرده اما قدرتمند با استفاده از Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [بهینه‌سازی مدل‌های زبان کوچک برای فراخوانی توابع در خودرو](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) فاین‌تیون کردن PHI-3 برای پاسخ به سوالات چندگزینه‌ای: روش‌شناسی، نتایج و چالش‌ها](https://arxiv.org/abs/2501.01588)  

## استفاده از مدل‌های Phi  

### Phi در Azure AI Foundry  

شما می‌توانید یاد بگیرید چگونه از Microsoft Phi استفاده کنید و چگونه راهکارهای E2E را در دستگاه‌های سخت‌افزاری مختلف خود بسازید. برای تجربه Phi، ابتدا با مدل‌ها کار کنید و Phi را برای سناریوهای خود سفارشی کنید با استفاده از [کاتالوگ مدل Azure AI Foundry Azure AI](https://aka.ms/phi3-azure-ai). اطلاعات بیشتر در مورد شروع کار را می‌توانید در [شروع سریع Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) بیابید.  

**محیط آزمایشی**  
هر مدل یک محیط آزمایشی اختصاصی برای آزمایش دارد [محیط آزمایشی Azure AI](https://aka.ms/try-phi3).  

### Phi در مدل‌های GitHub  

شما می‌توانید یاد بگیرید چگونه از Microsoft Phi استفاده کنید و چگونه راهکارهای E2E را در دستگاه‌های سخت‌افزاری مختلف خود بسازید. برای تجربه Phi، ابتدا با مدل کار کنید و Phi را برای سناریوهای خود سفارشی کنید با استفاده از [کاتالوگ مدل GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). اطلاعات بیشتر در مورد شروع کار را می‌توانید در [شروع سریع کاتالوگ مدل GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md) بیابید.  

**محیط آزمایشی**  
هر مدل یک [محیط آزمایشی اختصاصی برای آزمایش مدل](/md/02.QuickStart/GitHubModel_QuickStart.md) دارد.  

### Phi در Hugging Face  

شما می‌توانید مدل را در [Hugging Face](https://huggingface.co/microsoft) نیز پیدا کنید.  

**محیط آزمایشی**  
[محیط آزمایشی Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)  

## هوش مصنوعی مسئولانه  

مایکروسافت متعهد است که به مشتریان خود کمک کند تا از محصولات هوش مصنوعی ما به صورت مسئولانه استفاده کنند، تجربیات خود را به اشتراک بگذارند و از طریق ابزارهایی مانند یادداشت‌های شفافیت و ارزیابی تأثیر، شراکت‌های مبتنی بر اعتماد ایجاد کنند. بسیاری از این منابع را می‌توانید در [https://aka.ms/RAI](https://aka.ms/RAI) پیدا کنید.  
رویکرد مایکروسافت به هوش مصنوعی مسئولانه بر پایه اصول هوش مصنوعی ما شامل انصاف، قابلیت اطمینان و ایمنی، حریم خصوصی و امنیت، شمول، شفافیت و پاسخگویی است.  

مدل‌های زبان طبیعی، تصویر و گفتار در مقیاس بزرگ - مانند مدل‌هایی که در این نمونه استفاده می‌شوند - ممکن است به روش‌هایی رفتار کنند که ناعادلانه، غیرقابل اعتماد یا توهین‌آمیز باشند و در نتیجه آسیب‌هایی ایجاد کنند. لطفاً یادداشت شفافیت [خدمات Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) را مطالعه کنید تا از خطرات و محدودیت‌ها مطلع شوید.  

رویکرد پیشنهادی برای کاهش این خطرات شامل اضافه کردن یک سیستم ایمنی در معماری شماست که می‌تواند رفتارهای مضر را شناسایی و جلوگیری کند. [ایمنی محتوای Azure AI](https://learn.microsoft.com/azure/ai-services/content-safety/overview) یک لایه محافظتی مستقل ارائه می‌دهد که قادر به شناسایی محتوای مضر تولید شده توسط کاربران و هوش مصنوعی در برنامه‌ها و خدمات است. ایمنی محتوای Azure AI شامل APIهای متن و تصویر است که به شما امکان شناسایی محتوای مضر را می‌دهند. در Azure AI Foundry، خدمات ایمنی محتوا به شما اجازه می‌دهند تا نمونه کدهایی برای شناسایی محتوای مضر در حالت‌های مختلف را مشاهده، بررسی و امتحان کنید. [مستندات شروع سریع](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) شما را در ارسال درخواست‌ها به این سرویس راهنمایی می‌کند.  

جنبه دیگری که باید در نظر گرفت عملکرد کلی برنامه است. در برنامه‌های چندوجهی و چندمدلی، عملکرد به معنای این است که سیستم همان‌طور که شما و کاربران انتظار دارید عمل کند، از جمله تولید نکردن خروجی‌های مضر. ارزیابی عملکرد کلی برنامه شما با استفاده از [ارزیاب‌های عملکرد و کیفیت و ارزیاب‌های خطر و ایمنی](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) اهمیت دارد. همچنین شما می‌توانید با استفاده از [ارزیاب‌های سفارشی](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ایجاد و ارزیابی کنید.  
شما می‌توانید برنامه هوش مصنوعی خود را در محیط توسعه با استفاده از [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ارزیابی کنید. با استفاده از یک مجموعه داده آزمایشی یا یک هدف، تولیدات برنامه هوش مصنوعی شما به صورت کمی با ارزیاب‌های داخلی یا ارزیاب‌های سفارشی انتخابی شما اندازه‌گیری می‌شوند. برای شروع کار با azure ai evaluation sdk جهت ارزیابی سیستم خود، می‌توانید از [راهنمای شروع سریع](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) پیروی کنید. پس از اجرای یک دوره ارزیابی، می‌توانید [نتایج را در Azure AI Foundry مشاهده کنید](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## علائم تجاری

این پروژه ممکن است شامل علائم تجاری یا لوگوهای مربوط به پروژه‌ها، محصولات یا خدمات باشد. استفاده مجاز از علائم تجاری یا لوگوهای Microsoft باید مطابق با [دستورالعمل‌های علائم تجاری و برند Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) باشد. استفاده از علائم تجاری یا لوگوهای Microsoft در نسخه‌های اصلاح‌شده این پروژه نباید باعث سردرگمی یا القای حمایت Microsoft شود. هرگونه استفاده از علائم تجاری یا لوگوهای شخص ثالث باید مطابق با سیاست‌های همان شخص ثالث باشد.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادقتی‌هایی باشند. سند اصلی به زبان اصلی آن باید به‌عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ‌گونه سوءتفاهم یا تفسیر نادرستی که از استفاده از این ترجمه ناشی شود، نیستیم.