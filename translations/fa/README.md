<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T13:19:08+00:00",
  "source_file": "README.md",
  "language_code": "fa"
}
-->
# کتاب آشپزی فی: مثال‌های عملی با مدل‌های فی مایکروسافت

فی مجموعه‌ای از مدل‌های هوش مصنوعی متن‌باز است که توسط مایکروسافت توسعه داده شده است.

فی در حال حاضر قدرتمندترین و مقرون‌به‌صرفه‌ترین مدل زبان کوچک (SLM) است که در زمینه‌های چندزبانه، استدلال، تولید متن/چت، کدنویسی، تصاویر، صوت و سایر سناریوها عملکرد بسیار خوبی دارد.

شما می‌توانید فی را در فضای ابری یا دستگاه‌های لبه‌ای مستقر کنید و به راحتی برنامه‌های هوش مصنوعی تولیدی را با قدرت محاسباتی محدود بسازید.

برای شروع استفاده از این منابع، مراحل زیر را دنبال کنید:
1. **فورک کردن مخزن**: کلیک کنید [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **کلون کردن مخزن**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**به انجمن دیسکورد هوش مصنوعی مایکروسافت بپیوندید و با کارشناسان و توسعه‌دهندگان دیگر ملاقات کنید**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 پشتیبانی چندزبانه

#### پشتیبانی شده از طریق GitHub Action (خودکار و همیشه به‌روز)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](./README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) 
[Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)

## فهرست مطالب

- مقدمه
  - [خوش آمدید به خانواده فی](./md/01.Introduction/01/01.PhiFamily.md)
  - [راه‌اندازی محیط شما](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [درک فناوری‌های کلیدی](./md/01.Introduction/01/01.Understandingtech.md)
  - [ایمنی هوش مصنوعی برای مدل‌های فی](./md/01.Introduction/01/01.AISafety.md)
  - [پشتیبانی سخت‌افزاری فی](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [مدل‌های فی و دسترسی در پلتفرم‌های مختلف](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [استفاده از Guidance-ai و فی](./md/01.Introduction/01/01.Guidance.md)
  - [مدل‌های بازار GitHub](https://github.com/marketplace/models)
  - [کاتالوگ مدل Azure AI](https://ai.azure.com)

- استنتاج فی در محیط‌های مختلف
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [مدل‌های GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [کاتالوگ مدل Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- استنتاج خانواده فی
    - [استنتاج فی در iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [استنتاج فی در اندروید](./md/01.Introduction/03/Android_Inference.md)
    - [استنتاج فی در Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [استنتاج فی در AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [استنتاج فی با Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [استنتاج فی در سرور محلی](./md/01.Introduction/03/Local_Server_Inference.md)
    - [استنتاج فی در سرور راه دور با استفاده از AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [استنتاج فی با Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [استنتاج فی--Vision در محلی](./md/01.Introduction/03/Vision_Inference.md)
    - [استنتاج فی با Kaito AKS، کانتینرهای Azure (پشتیبانی رسمی)](./md/01.Introduction/03/Kaito_Inference.md)

- [کوانتیزه کردن خانواده فی](./md/01.Introduction/04/QuantifyingPhi.md)
    - [کوانتیزه کردن Phi-3.5 / 4 با استفاده از llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [کوانتیزه کردن Phi-3.5 / 4 با استفاده از افزونه‌های هوش مصنوعی تولیدی برای onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [کوانتیزه کردن Phi-3.5 / 4 با استفاده از Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [کوانتیزه کردن Phi-3.5 / 4 با استفاده از Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- ارزیابی فی
    - [هوش مصنوعی مسئول](./md/01.Introduction/05/ResponsibleAI.md)
    - [ارزیابی با Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [استفاده از Promptflow برای ارزیابی](./md/01.Introduction/05/Promptflow.md)

- RAG با Azure AI Search
    - [چگونه از Phi-4-mini و Phi-4-multimodal (RAG) با Azure AI Search استفاده کنیم](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- نمونه‌های توسعه برنامه فی
  - برنامه‌های متن و چت
    - نمونه‌های Phi-4 🆕
      - [📓] [چت با مدل Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [چت با مدل محلی Phi-4 ONNX .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [برنامه کنسول .NET چت با Phi-4 ONNX با استفاده از Sementic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - نمونه‌های Phi-3 / 3.5
      - [چت‌بات محلی در مرورگر با استفاده از Phi3، ONNX Runtime Web و WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [چت OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [مدل چندگانه - تعامل Phi-3-mini و OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ساخت یک wrapper و استفاده از Phi-3 با MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [بهینه‌سازی مدل - چگونه مدل Phi-3-min را برای ONNX Runtime Web با Olive بهینه کنیم](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [برنامه WinUI3 با Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [نمونه برنامه یادداشت‌های هوش مصنوعی چندمدلی WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [تنظیم دقیق و یکپارچه‌سازی مدل‌های سفارشی Phi-3 با Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [تنظیم دقیق و یکپارچه‌سازی مدل‌های سفارشی Phi-3 با Prompt flow در Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [ارزیابی مدل تنظیم‌شده Phi-3 / Phi-3.5 در Azure AI Foundry با تمرکز بر اصول مسئولیت‌پذیری هوش مصنوعی مایکروسافت](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [نمونه پیش‌بینی زبان Phi-3.5-mini-instruct (چینی/انگلیسی)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [چت‌بات RAG مبتنی بر WebGPU و Phi-3.5-Instruct](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [استفاده از GPU ویندوز برای ایجاد راه‌حل Prompt flow با Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [استفاده از Microsoft Phi-3.5 tflite برای ایجاد اپلیکیشن اندروید](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [نمونه پرسش و پاسخ .NET با استفاده از مدل محلی ONNX Phi-3 و Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [اپلیکیشن چت کنسولی .NET با Semantic Kernel و Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- نمونه‌های کدنویسی SDK استنتاج Azure AI  
  - نمونه‌های Phi-4 🆕  
    - [📓] [تولید کد پروژه با استفاده از Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - نمونه‌های Phi-3 / 3.5  
    - [ایجاد چت GitHub Copilot در Visual Studio Code با خانواده Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [ایجاد عامل چت Copilot در Visual Studio Code با Phi-3.5 توسط مدل‌های GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- نمونه‌های استدلال پیشرفته  
  - نمونه‌های Phi-4 🆕  
    - [📓] [نمونه‌های Phi-4-mini-reasoning یا Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [تنظیم دقیق Phi-4-mini-reasoning با Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [تنظیم دقیق Phi-4-mini-reasoning با Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Phi-4-mini-reasoning با مدل‌های GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Phi-4-mini-reasoning با مدل‌های Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- دموها  
    - [دموهای Phi-4-mini در Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [دموهای Phi-4-multimodal در Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- نمونه‌های Vision  
  - نمونه‌های Phi-4 🆕  
    - [📓] [استفاده از Phi-4-multimodal برای خواندن تصاویر و تولید کد](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - نمونه‌های Phi-3 / 3.5  
    - [📓][Phi-3-vision-تبدیل متن تصویر به متن](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [دمو: بازیافت Phi-3](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - دستیار زبان بصری - با Phi3-Vision و OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][نمونه چند فریمی یا چند تصویری Phi-3.5 Vision](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Phi-3 Vision مدل محلی ONNX با استفاده از Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [مدل محلی ONNX Phi-3 Vision مبتنی بر منو با استفاده از Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- نمونه‌های ریاضی  
  - نمونه‌های Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [دموی ریاضی با Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)  

- نمونه‌های صوتی  
  - نمونه‌های Phi-4 🆕  
    - [📓] [استخراج متن‌های صوتی با استفاده از Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [نمونه صوتی Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [نمونه ترجمه گفتار Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [اپلیکیشن کنسولی .NET با استفاده از Phi-4-multimodal برای تحلیل فایل صوتی و تولید متن](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- نمونه‌های MOE  
  - نمونه‌های Phi-3 / 3.5  
    - [📓] [نمونه‌های مدل‌های Mixture of Experts (MoEs) Phi-3.5 در شبکه‌های اجتماعی](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [ساخت یک خط لوله Retrieval-Augmented Generation (RAG) با NVIDIA NIM Phi-3 MOE، Azure AI Search و LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- نمونه‌های فراخوانی تابع  
  - نمونه‌های Phi-4 🆕  
    - [📓] [استفاده از فراخوانی تابع با Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [استفاده از فراخوانی تابع برای ایجاد چند عامل با Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [استفاده از فراخوانی تابع با Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [استفاده از فراخوانی تابع با ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- نمونه‌های ترکیب چندمدلی  
  - نمونه‌های Phi-4 🆕  
    - [📓] [استفاده از Phi-4-multimodal به عنوان یک خبرنگار فناوری](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [اپلیکیشن کنسولی .NET با استفاده از Phi-4-multimodal برای تحلیل تصاویر](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- نمونه‌های تنظیم دقیق Phi  
  - [سناریوهای تنظیم دقیق](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [تنظیم دقیق در مقابل RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [تنظیم دقیق Phi-3 برای تبدیل شدن به یک متخصص صنعتی](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [تنظیم دقیق Phi-3 با AI Toolkit برای VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [تنظیم دقیق Phi-3 با سرویس Azure Machine Learning](./md/03.FineTuning/Introduce_AzureML.md)  
  - [تنظیم دقیق Phi-3 با Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [تنظیم دقیق Phi-3 با QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [تنظیم دقیق Phi-3 با Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [تنظیم دقیق Phi-3 با Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [تنظیم دقیق با Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [تنظیم دقیق با آزمایشگاه عملی Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)  
  - [تنظیم دقیق Phi-3-vision با Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [تنظیم دقیق Phi-3 با چارچوب Apple MLX](./md/03.FineTuning/FineTuning_MLX.md)  
  - [تنظیم دقیق Phi-3-vision (پشتیبانی رسمی)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [تنظیم دقیق Phi-3 با Kaito AKS، کانتینرهای Azure (پشتیبانی رسمی)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [تنظیم دقیق Phi-3 و 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- آزمایشگاه عملی  
  - [کاوش مدل‌های پیشرفته: LLMs، SLMs، توسعه محلی و بیشتر](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [باز کردن پتانسیل NLP: تنظیم دقیق با Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- مقالات تحقیقاتی و انتشارات علمی  
  - [کتاب‌های درسی همه چیزی هستند که نیاز دارید II: گزارش فنی phi-1.5](https://arxiv.org/abs/2309.05463)  
  - [گزارش فنی Phi-3: یک مدل زبان بسیار توانمند به صورت محلی روی تلفن شما](https://arxiv.org/abs/2404.14219)  
  - [گزارش فنی Phi-4](https://arxiv.org/abs/2412.08905)  
  - [گزارش فنی Phi-4-Mini: مدل‌های زبان چندمدلی فشرده اما قدرتمند از طریق Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [بهینه‌سازی مدل‌های زبان کوچک برای فراخوانی توابع درون‌خودرویی](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) تنظیم دقیق PHI-3 برای پاسخ به سوالات چندگزینه‌ای: روش‌شناسی، نتایج و چالش‌ها](https://arxiv.org/abs/2501.01588)  
- [گزارش فنی Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [گزارش فنی Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)  

## استفاده از مدل‌های Phi  

### Phi در Azure AI Foundry  

شما می‌توانید یاد بگیرید که چگونه از Microsoft Phi استفاده کنید و راه‌حل‌های انتها به انتها (E2E) را در دستگاه‌های سخت‌افزاری مختلف خود بسازید. برای تجربه Phi، ابتدا با مدل‌ها کار کنید و Phi را برای سناریوهای خود سفارشی کنید. از طریق [کاتالوگ مدل Azure AI Foundry](https://aka.ms/phi3-azure-ai) می‌توانید اطلاعات بیشتری کسب کنید. برای شروع، به [راهنمای شروع Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) مراجعه کنید.  

**محیط آزمایشی**  
هر مدل یک محیط آزمایشی اختصاصی دارد تا بتوانید مدل را تست کنید: [Azure AI Playground](https://aka.ms/try-phi3).  

### Phi در مدل‌های GitHub  

شما می‌توانید یاد بگیرید که چگونه از Microsoft Phi استفاده کنید و راه‌حل‌های انتها به انتها (E2E) را در دستگاه‌های سخت‌افزاری مختلف خود بسازید. برای تجربه Phi، ابتدا با مدل‌ها کار کنید و Phi را برای سناریوهای خود سفارشی کنید. از طریق [کاتالوگ مدل GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) می‌توانید اطلاعات بیشتری کسب کنید. برای شروع، به [راهنمای شروع کاتالوگ مدل GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md) مراجعه کنید.  

**محیط آزمایشی**  
هر مدل یک [محیط آزمایشی اختصاصی برای تست مدل](/md/02.QuickStart/GitHubModel_QuickStart.md) دارد.  

### Phi در Hugging Face  

شما همچنین می‌توانید مدل را در [Hugging Face](https://huggingface.co/microsoft) پیدا کنید.  

**محیط آزمایشی**  
[محیط آزمایشی Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)  

## هوش مصنوعی مسئولانه  

مایکروسافت متعهد است که به مشتریان خود کمک کند تا محصولات هوش مصنوعی را به‌صورت مسئولانه استفاده کنند، تجربیات خود را به اشتراک بگذارند و از طریق ابزارهایی مانند یادداشت‌های شفافیت و ارزیابی‌های تأثیر، همکاری‌های مبتنی بر اعتماد ایجاد کنند. بسیاری از این منابع در [https://aka.ms/RAI](https://aka.ms/RAI) قابل دسترسی هستند.  
رویکرد مایکروسافت به هوش مصنوعی مسئولانه بر اصول هوش مصنوعی شامل انصاف، قابلیت اطمینان و ایمنی، حریم خصوصی و امنیت، فراگیری، شفافیت و پاسخگویی استوار است.  

مدل‌های بزرگ مقیاس زبان طبیعی، تصویر و گفتار - مانند مدل‌های استفاده‌شده در این نمونه - ممکن است به‌طور بالقوه رفتارهایی ناعادلانه، غیرقابل‌اعتماد یا توهین‌آمیز داشته باشند که می‌تواند آسیب‌هایی ایجاد کند. لطفاً به [یادداشت شفافیت سرویس Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) مراجعه کنید تا از خطرات و محدودیت‌ها مطلع شوید.  

رویکرد توصیه‌شده برای کاهش این خطرات، شامل یک سیستم ایمنی در معماری شما است که می‌تواند رفتارهای مضر را شناسایی و جلوگیری کند. [ایمنی محتوای Azure AI](https://learn.microsoft.com/azure/ai-services/content-safety/overview) یک لایه محافظ مستقل ارائه می‌دهد که قادر به شناسایی محتوای مضر تولیدشده توسط کاربران و هوش مصنوعی در برنامه‌ها و خدمات است. ایمنی محتوای Azure AI شامل API‌های متن و تصویر است که به شما امکان می‌دهد محتوای مضر را شناسایی کنید. در Azure AI Foundry، سرویس ایمنی محتوا به شما امکان می‌دهد کد نمونه‌ای برای شناسایی محتوای مضر در حالت‌های مختلف مشاهده، بررسی و آزمایش کنید. [مستندات شروع سریع](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) شما را در ارسال درخواست‌ها به این سرویس راهنمایی می‌کند.  

جنبه دیگری که باید در نظر گرفته شود، عملکرد کلی برنامه است. در برنامه‌های چندحالتی و چندمدلی، عملکرد به معنای این است که سیستم همان‌طور که شما و کاربران انتظار دارید عمل کند، از جمله عدم تولید خروجی‌های مضر. ارزیابی عملکرد برنامه کلی شما با استفاده از [ارزیاب‌های عملکرد و کیفیت و ارزیاب‌های خطر و ایمنی](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) مهم است. همچنین می‌توانید با استفاده از [ارزیاب‌های سفارشی](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ارزیابی کنید.  

شما می‌توانید برنامه هوش مصنوعی خود را در محیط توسعه با استفاده از [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ارزیابی کنید. با استفاده از یک مجموعه داده آزمایشی یا هدف، تولیدات برنامه هوش مصنوعی شما به‌صورت کمی با ارزیاب‌های داخلی یا ارزیاب‌های سفارشی موردنظر شما اندازه‌گیری می‌شوند. برای شروع با Azure AI Evaluation SDK جهت ارزیابی سیستم خود، می‌توانید [راهنمای شروع سریع](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) را دنبال کنید. پس از اجرای یک ارزیابی، می‌توانید [نتایج را در Azure AI Foundry مشاهده کنید](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).  

## علائم تجاری  

این پروژه ممکن است شامل علائم تجاری یا لوگوهایی برای پروژه‌ها، محصولات یا خدمات باشد. استفاده مجاز از علائم تجاری یا لوگوهای مایکروسافت باید مطابق با [راهنمای علائم تجاری و برند مایکروسافت](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) باشد.  
استفاده از علائم تجاری یا لوگوهای مایکروسافت در نسخه‌های اصلاح‌شده این پروژه نباید باعث سردرگمی یا القای حمایت مایکروسافت شود. هرگونه استفاده از علائم تجاری یا لوگوهای شخص ثالث تابع سیاست‌های آن‌ها است.  

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.