<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T13:17:51+00:00",
  "source_file": "README.md",
  "language_code": "ar"
}
-->
# دليل Phi: أمثلة عملية مع نماذج Phi من مايكروسوفت

Phi هي سلسلة من نماذج الذكاء الاصطناعي مفتوحة المصدر التي طورتها مايكروسوفت.

تُعد Phi حاليًا النموذج اللغوي الصغير (SLM) الأكثر قوة وفعالية من حيث التكلفة، حيث تحقق نتائج ممتازة في اختبارات متعددة اللغات، التفكير، إنشاء النصوص/الدردشة، البرمجة، الصور، الصوت، وغيرها من السيناريوهات.

يمكنك نشر Phi على السحابة أو على الأجهزة الطرفية، كما يمكنك بسهولة بناء تطبيقات ذكاء اصطناعي توليدية باستخدام موارد حوسبة محدودة.

اتبع هذه الخطوات للبدء باستخدام هذه الموارد:
1. **استنساخ المستودع**: انقر على [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **نسخ المستودع**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**انضم إلى مجتمع مايكروسوفت للذكاء الاصطناعي على Discord وتواصل مع الخبراء والمطورين الآخرين**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 دعم متعدد اللغات

#### مدعوم عبر GitHub Action (تلقائي ومحدث دائمًا)

[الفرنسية](../fr/README.md) | [الإسبانية](../es/README.md) | [الألمانية](../de/README.md) | [الروسية](../ru/README.md) | [العربية](./README.md) | [الفارسية](../fa/README.md) | [الأردية](../ur/README.md) | [الصينية (المبسطة)](../zh/README.md) | [الصينية (التقليدية، ماكاو)](../mo/README.md) | [الصينية (التقليدية، هونغ كونغ)](../hk/README.md) | [الصينية (التقليدية، تايوان)](../tw/README.md) | [اليابانية](../ja/README.md) | [الكورية](../ko/README.md) | [الهندية](../hi/README.md) 
[البنغالية](../bn/README.md) | [الماراثية](../mr/README.md) | [النيبالية](../ne/README.md) | [البنجابية (غورموخي)](../pa/README.md) | [البرتغالية (البرتغال)](../pt/README.md) | [البرتغالية (البرازيل)](../br/README.md) | [الإيطالية](../it/README.md) | [البولندية](../pl/README.md) | [التركية](../tr/README.md) | [اليونانية](../el/README.md) | [التايلاندية](../th/README.md) | [السويدية](../sv/README.md) | [الدانماركية](../da/README.md) | [النرويجية](../no/README.md) | [الفنلندية](../fi/README.md) | [الهولندية](../nl/README.md) | [العبرية](../he/README.md) | [الفيتنامية](../vi/README.md) | [الإندونيسية](../id/README.md) | [الماليزية](../ms/README.md) | [التاغالوغية (الفلبينية)](../tl/README.md) | [السواحيلية](../sw/README.md) | [الهنغارية](../hu/README.md) | [التشيكية](../cs/README.md) | [السلوفاكية](../sk/README.md) | [الرومانية](../ro/README.md) | [البلغارية](../bg/README.md) | [الصربية (السيريلية)](../sr/README.md) | [الكرواتية](../hr/README.md) | [السلوفينية](../sl/README.md)

## جدول المحتويات

- المقدمة
  - [مرحبًا بك في عائلة Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [إعداد بيئتك](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [فهم التقنيات الرئيسية](./md/01.Introduction/01/01.Understandingtech.md)
  - [أمان الذكاء الاصطناعي لنماذج Phi](./md/01.Introduction/01/01.AISafety.md)
  - [دعم الأجهزة لنماذج Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [نماذج Phi وتوافرها عبر المنصات](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [استخدام Guidance-ai وPhi](./md/01.Introduction/01/01.Guidance.md)
  - [نماذج سوق GitHub](https://github.com/marketplace/models)
  - [كتالوج نماذج Azure AI](https://ai.azure.com)

- استنتاج Phi في بيئات مختلفة
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [نماذج GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    - [كتالوج نماذج Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [أداة الذكاء الاصطناعي VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- استنتاج عائلة Phi
    - [استنتاج Phi في iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [استنتاج Phi في Android](./md/01.Introduction/03/Android_Inference.md)
    - [استنتاج Phi في Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [استنتاج Phi في AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [استنتاج Phi باستخدام إطار عمل Apple MLX](./md/01.Introduction/03/MLX_Inference.md)
    - [استنتاج Phi في الخادم المحلي](./md/01.Introduction/03/Local_Server_Inference.md)
    - [استنتاج Phi في الخادم البعيد باستخدام أداة الذكاء الاصطناعي](./md/01.Introduction/03/Remote_Interence.md)
    - [استنتاج Phi باستخدام Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [استنتاج Phi--Vision محليًا](./md/01.Introduction/03/Vision_Inference.md)
    - [استنتاج Phi باستخدام Kaito AKS، حاويات Azure (الدعم الرسمي)](./md/01.Introduction/03/Kaito_Inference.md)

- [تكميم عائلة Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [تكميم Phi-3.5 / 4 باستخدام llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [تكميم Phi-3.5 / 4 باستخدام امتدادات الذكاء الاصطناعي التوليدي لـ onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [تكميم Phi-3.5 / 4 باستخدام Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [تكميم Phi-3.5 / 4 باستخدام إطار عمل Apple MLX](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- تقييم Phi
    - [الذكاء الاصطناعي المسؤول](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry للتقييم](./md/01.Introduction/05/AIFoundry.md)
    - [استخدام Promptflow للتقييم](./md/01.Introduction/05/Promptflow.md)

- RAG مع Azure AI Search
    - [كيفية استخدام Phi-4-mini وPhi-4-multimodal (RAG) مع Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- أمثلة تطوير تطبيقات Phi
  - تطبيقات النصوص والدردشة
    - أمثلة Phi-4 🆕
      - [📓] [الدردشة مع نموذج Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [الدردشة مع نموذج Phi-4 المحلي ONNX باستخدام .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [تطبيق Console .NET للدردشة مع Phi-4 ONNX باستخدام Sementic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - أمثلة Phi-3 / 3.5
      - [روبوت محادثة محلي في المتصفح باستخدام Phi3، ONNX Runtime Web وWebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [دردشة OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [نموذج متعدد - Phi-3-mini التفاعلي وOpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - بناء غلاف واستخدام Phi-3 مع MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [تحسين النموذج - كيفية تحسين نموذج Phi-3-min لـ ONNX Runtime Web باستخدام Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [تطبيق WinUI3 مع Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [تطبيق ملاحظات مدعوم بالذكاء الاصطناعي متعدد النماذج WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [تخصيص ودمج نماذج Phi-3 المخصصة باستخدام Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)  
- [تخصيص ودمج نماذج Phi-3 المخصصة باستخدام Prompt flow في Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)  
- [تقييم نموذج Phi-3 / Phi-3.5 المخصص في Azure AI Foundry مع التركيز على مبادئ الذكاء الاصطناعي المسؤول من Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)  
- [📓] [عينة توقع اللغة Phi-3.5-mini-instruct (الصينية/الإنجليزية)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)  
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)  
- [استخدام GPU في Windows لإنشاء حل Prompt flow باستخدام Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)  
- [استخدام Microsoft Phi-3.5 tflite لإنشاء تطبيق Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)  
- [مثال Q&A .NET باستخدام نموذج Phi-3 المحلي ONNX مع Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)  
- [تطبيق دردشة Console .NET مع Semantic Kernel وPhi-3](../../md/04.HOL/dotnet/src/LabsPhi302)  

- عينات Azure AI Inference SDK  
  - عينات Phi-4 🆕  
    - [📓] [إنشاء كود المشروع باستخدام Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - عينات Phi-3 / 3.5  
    - [إنشاء دردشة GitHub Copilot في Visual Studio Code باستخدام عائلة Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [إنشاء وكيل دردشة في Visual Studio Code باستخدام Phi-3.5 ونماذج GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- عينات التفكير المتقدم  
  - عينات Phi-4 🆕  
    - [📓] [عينات Phi-4-mini-reasoning أو Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [تخصيص Phi-4-mini-reasoning باستخدام Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [تخصيص Phi-4-mini-reasoning باستخدام Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Phi-4-mini-reasoning مع نماذج GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Phi-4-mini-reasoning مع نماذج Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  

- العروض التوضيحية  
  - [عروض Phi-4-mini المستضافة على Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
  - [عروض Phi-4-multimodal المستضافة على Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  

- عينات الرؤية  
  - عينات Phi-4 🆕  
    - [📓] [استخدام Phi-4-multimodal لقراءة الصور وإنشاء الكود](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - عينات Phi-3 / 3.5  
    - [📓] [Phi-3-vision-تحويل النص إلى نص من الصور](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓] [Phi-3-vision تضمين CLIP](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [عرض Phi-3 لإعادة التدوير](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - مساعد لغة بصري - باستخدام Phi3-Vision وOpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓] [عينة Phi-3.5 Vision متعددة الإطارات أو متعددة الصور](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Phi-3 Vision نموذج ONNX محلي باستخدام Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [نموذج ONNX محلي Phi-3 Vision مع قائمة باستخدام Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- عينات الرياضيات  
  - عينات Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [عرض رياضيات باستخدام Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)  

- عينات الصوت  
  - عينات Phi-4 🆕  
    - [📓] [استخراج نصوص الصوت باستخدام Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [عينة صوت Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [عينة ترجمة الكلام باستخدام Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [تطبيق Console .NET باستخدام Phi-4-multimodal لتحليل ملف صوتي وإنشاء نص](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- عينات MoE  
  - عينات Phi-3 / 3.5  
    - [📓] [نماذج Phi-3.5 Mixture of Experts (MoEs) عينة وسائل التواصل الاجتماعي](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [بناء خط أنابيب استرجاع معزز (RAG) باستخدام NVIDIA NIM Phi-3 MOE، Azure AI Search، وLlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- عينات استدعاء الوظائف  
  - عينات Phi-4 🆕  
    - [📓] [استخدام استدعاء الوظائف مع Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [استخدام استدعاء الوظائف لإنشاء وكلاء متعددين مع Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [استخدام استدعاء الوظائف مع Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [استخدام استدعاء الوظائف مع ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- عينات المزج متعدد الوسائط  
  - عينات Phi-4 🆕  
    - [📓] [استخدام Phi-4-multimodal كصحفي تقني](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [تطبيق Console .NET باستخدام Phi-4-multimodal لتحليل الصور](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- تخصيص نماذج Phi  
  - [سيناريوهات التخصيص](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [التخصيص مقابل RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [تخصيص Phi-3 ليصبح خبيرًا في الصناعة](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [تخصيص Phi-3 باستخدام أدوات الذكاء الاصطناعي لـ VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [تخصيص Phi-3 باستخدام خدمة Azure Machine Learning](./md/03.FineTuning/Introduce_AzureML.md)  
  - [تخصيص Phi-3 باستخدام Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [تخصيص Phi-3 باستخدام QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [تخصيص Phi-3 باستخدام Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [تخصيص Phi-3 باستخدام Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [تخصيص باستخدام Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [تخصيص باستخدام Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)  
  - [تخصيص Phi-3-vision باستخدام Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [تخصيص Phi-3 باستخدام إطار عمل Apple MLX](./md/03.FineTuning/FineTuning_MLX.md)  
  - [تخصيص Phi-3-vision (الدعم الرسمي)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [تخصيص Phi-3 باستخدام Kaito AKS، Azure Containers (الدعم الرسمي)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [تخصيص Phi-3 وPhi-3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- مختبر عملي  
  - [استكشاف النماذج المتقدمة: LLMs، SLMs، التطوير المحلي والمزيد](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [إطلاق إمكانيات معالجة اللغة الطبيعية: التخصيص باستخدام Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- أوراق البحث الأكاديمي والمنشورات  
  - [Textbooks Are All You Need II: تقرير تقني phi-1.5](https://arxiv.org/abs/2309.05463)  
  - [تقرير تقني Phi-3: نموذج لغة عالي الكفاءة محليًا على هاتفك](https://arxiv.org/abs/2404.14219)  
  - [تقرير تقني Phi-4](https://arxiv.org/abs/2412.08905)  
  - [تقرير تقني Phi-4-Mini: نماذج لغة متعددة الوسائط مدمجة لكنها قوية عبر Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [تحسين نماذج اللغة الصغيرة لاستدعاء الوظائف داخل المركبات](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) تخصيص PHI-3 للإجابة على أسئلة الاختيار المتعدد: المنهجية، النتائج، والتحديات](https://arxiv.org/abs/2501.01588)  
- [Phi-4-reasoning تقرير تقني](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning تقرير تقني](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)  

## استخدام نماذج Phi  

### Phi على Azure AI Foundry  

يمكنك تعلم كيفية استخدام Microsoft Phi وكيفية بناء حلول شاملة على أجهزتك المختلفة. لتجربة Phi بنفسك، ابدأ بتجربة النماذج وتخصيص Phi لسيناريوهاتك باستخدام [كتالوج نماذج Azure AI Foundry](https://aka.ms/phi3-azure-ai). يمكنك معرفة المزيد من خلال البدء بـ [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).  

**الملعب**  
كل نموذج لديه ملعب مخصص لاختبار النموذج [Azure AI Playground](https://aka.ms/try-phi3).  

### Phi على نماذج GitHub  

يمكنك تعلم كيفية استخدام Microsoft Phi وكيفية بناء حلول شاملة على أجهزتك المختلفة. لتجربة Phi بنفسك، ابدأ بتجربة النموذج وتخصيص Phi لسيناريوهاتك باستخدام [كتالوج نماذج GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). يمكنك معرفة المزيد من خلال البدء بـ [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).  

**الملعب**  
كل نموذج لديه [ملعب مخصص لاختبار النموذج](/md/02.QuickStart/GitHubModel_QuickStart.md).  

### Phi على Hugging Face  

يمكنك أيضًا العثور على النموذج على [Hugging Face](https://huggingface.co/microsoft).  

**الملعب**  
[ملعب Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct).  

## الذكاء الاصطناعي المسؤول  

تلتزم Microsoft بمساعدة عملائنا على استخدام منتجات الذكاء الاصطناعي لدينا بشكل مسؤول، ومشاركة ما تعلمناه، وبناء شراكات قائمة على الثقة من خلال أدوات مثل ملاحظات الشفافية وتقييمات التأثير. يمكن العثور على العديد من هذه الموارد في [https://aka.ms/RAI](https://aka.ms/RAI).  
نهج Microsoft تجاه الذكاء الاصطناعي المسؤول يعتمد على مبادئ الذكاء الاصطناعي الخاصة بنا: الإنصاف، الموثوقية والسلامة، الخصوصية والأمان، الشمولية، الشفافية، والمساءلة.  

النماذج الكبيرة للغة الطبيعية والصور والصوت - مثل تلك المستخدمة في هذا المثال - قد تتصرف بطرق غير عادلة أو غير موثوقة أو مسيئة، مما قد يؤدي إلى أضرار. يرجى الرجوع إلى [ملاحظة الشفافية لخدمة Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) للحصول على معلومات حول المخاطر والقيود.  

النهج الموصى به لتقليل هذه المخاطر هو تضمين نظام أمان في بنيتك يمكنه اكتشاف ومنع السلوك الضار. [أمان محتوى Azure AI](https://learn.microsoft.com/azure/ai-services/content-safety/overview) يوفر طبقة حماية مستقلة، قادرة على اكتشاف المحتوى الضار الذي يتم إنشاؤه بواسطة المستخدم أو الذكاء الاصطناعي في التطبيقات والخدمات. يتضمن أمان محتوى Azure AI واجهات برمجة التطبيقات للنصوص والصور التي تسمح لك باكتشاف المواد الضارة. داخل Azure AI Foundry، تتيح لك خدمة أمان المحتوى عرض واستكشاف وتجربة عينات من التعليمات البرمجية لاكتشاف المحتوى الضار عبر وسائط مختلفة. [وثائق البدء السريع](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ترشدك خلال تقديم الطلبات إلى الخدمة.  

جانب آخر يجب أخذه في الاعتبار هو الأداء العام للتطبيق. مع التطبيقات متعددة الوسائط والنماذج، نعتبر الأداء يعني أن النظام يعمل كما تتوقع أنت ومستخدموك، بما في ذلك عدم إنتاج مخرجات ضارة. من المهم تقييم أداء تطبيقك العام باستخدام [مقيمي الأداء والجودة ومقيمي المخاطر والسلامة](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). لديك أيضًا القدرة على إنشاء وتقييم [مقيمي مخصصين](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).  

يمكنك تقييم تطبيق الذكاء الاصطناعي الخاص بك في بيئة التطوير باستخدام [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). باستخدام مجموعة بيانات اختبار أو هدف معين، يتم قياس إنتاجات تطبيق الذكاء الاصطناعي التوليدي الخاص بك بشكل كمي باستخدام مقيمين مدمجين أو مقيمين مخصصين من اختيارك. للبدء باستخدام Azure AI Evaluation SDK لتقييم نظامك، يمكنك اتباع [دليل البدء السريع](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). بمجرد تنفيذ تشغيل التقييم، يمكنك [عرض النتائج في Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).  

## العلامات التجارية  

قد يحتوي هذا المشروع على علامات تجارية أو شعارات لمشاريع أو منتجات أو خدمات. الاستخدام المصرح به لعلامات Microsoft التجارية أو الشعارات يجب أن يتبع [إرشادات العلامات التجارية والعلامات الخاصة بـ Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
استخدام علامات Microsoft التجارية أو الشعارات في نسخ معدلة من هذا المشروع يجب ألا يسبب ارتباكًا أو يوحي برعاية Microsoft. أي استخدام لعلامات تجارية أو شعارات خاصة بأطراف ثالثة يخضع لسياسات تلك الأطراف الثالثة.  

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.