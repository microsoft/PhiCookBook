<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef3a50368712b1a7483d0def1f70c490",
  "translation_date": "2025-12-21T09:59:28+00:00",
  "source_file": "README.md",
  "language_code": "ar"
}
-->
# دليل Phi: أمثلة عملية على نماذج Phi من مايكروسوفت

[![افتح واستخدم الأمثلة في GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![افتح في Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![مساهمو GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![مشكلات GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![طلبات سحب GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![طلبات السحب مرحب بها](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![المراقبون في GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Forks على GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![نجوم GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![خادم Discord لـ Microsoft Azure AI Foundry](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi هي سلسلة من نماذج الذكاء الاصطناعي مفتوحة المصدر التي طورتها مايكروسوفت. 

Phi هو حاليًا أقوى وأكثر نماذج اللغة الصغيرة (SLM) فعالية من حيث التكلفة، مع نتائج معيارية جيدة جدًا في تعدد اللغات، والتفكير المنطقي، وتوليد النص/المحادثة، والترميز، والصور، والصوت وسيناريوهات أخرى. 

يمكنك نشر Phi في السحابة أو على أجهزة الحافة، ويمكنك بسهولة بناء تطبيقات توليدية للذكاء الاصطناعي بقدرة حوسبة محدودة.

اتبع هذه الخطوات للبدء باستخدام هذه الموارد :
1. **افتح Fork للمستودع**: Click [![Forks على GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **استنساخ المستودع**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**انضم إلى مجتمع Microsoft AI على Discord والتقِ بالخبراء والمطورين الآخرين**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![الغلاف](../../translated_images/cover.eb18d1b9605d754b.ar.png)

### 🌐 دعم متعدد اللغات

#### مدعوم عبر GitHub Action (مؤتمت ومحدث دائمًا)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[العربية](./README.md) | [البنغالية](../bn/README.md) | [البلغارية](../bg/README.md) | [البورمية (ميانمار)](../my/README.md) | [الصينية (المبسطة)](../zh/README.md) | [الصينية (التقليدية، هونغ كونغ)](../hk/README.md) | [الصينية (التقليدية، ماكاو)](../mo/README.md) | [الصينية (التقليدية، تايوان)](../tw/README.md) | [الكرواتية](../hr/README.md) | [التشيكية](../cs/README.md) | [الدنماركية](../da/README.md) | [الهولندية](../nl/README.md) | [الإستونية](../et/README.md) | [الفنلندية](../fi/README.md) | [الفرنسية](../fr/README.md) | [الألمانية](../de/README.md) | [اليونانية](../el/README.md) | [العبرية](../he/README.md) | [الهندية](../hi/README.md) | [المجرية](../hu/README.md) | [الإندونيسية](../id/README.md) | [الإيطالية](../it/README.md) | [اليابانية](../ja/README.md) | [الكانادية](../kn/README.md) | [الكورية](../ko/README.md) | [الليتوانية](../lt/README.md) | [الماليزية](../ms/README.md) | [المالايالامية](../ml/README.md) | [الماراثية](../mr/README.md) | [النيبالية](../ne/README.md) | [البيجن النيجيرية](../pcm/README.md) | [النرويجية](../no/README.md) | [الفارسية (Farsi)](../fa/README.md) | [البولندية](../pl/README.md) | [البرتغالية (البرازيل)](../br/README.md) | [البرتغالية (البرتغال)](../pt/README.md) | [البنجابية (Gurmukhi)](../pa/README.md) | [الرومانية](../ro/README.md) | [الروسية](../ru/README.md) | [الصربية (السيريلية)](../sr/README.md) | [السلوفاكية](../sk/README.md) | [السلوفينية](../sl/README.md) | [الإسبانية](../es/README.md) | [السواحيلية](../sw/README.md) | [السويدية](../sv/README.md) | [التاغالوغية (الفلبينية)](../tl/README.md) | [التاميلية](../ta/README.md) | [التيلجو](../te/README.md) | [التايلاندية](../th/README.md) | [التركية](../tr/README.md) | [الأوكرانية](../uk/README.md) | [الأردية](../ur/README.md) | [الفيتنامية](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## جدول المحتويات

- المقدمة
  - [مرحبًا بك في عائلة Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [إعداد بيئتك](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [فهم التقنيات الرئيسية](./md/01.Introduction/01/01.Understandingtech.md)
  - [السلامة في الذكاء الاصطناعي لنماذج Phi](./md/01.Introduction/01/01.AISafety.md)
  - [دعم الأجهزة لنماذج Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [نماذج Phi وتوفرها عبر المنصات](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [استخدام Guidance-ai وPhi](./md/01.Introduction/01/01.Guidance.md)
  - [نماذج GitHub Marketplace](https://github.com/marketplace/models)
  - [كتالوج نماذج Azure AI](https://ai.azure.com)

- تشغيل استدلال Phi في بيئات مختلفة
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)
    -  [نماذج GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [كتالوج نماذج Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [مجموعة أدوات AI لـ VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry المحلية](./md/01.Introduction/02/07.FoundryLocal.md)

- استدلال عائلة Phi
    - [استدلال Phi على iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [استدلال Phi على Android](./md/01.Introduction/03/Android_Inference.md)
    - [استدلال Phi على Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [استدلال Phi على AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [استدلال Phi باستخدام إطار Apple MLX](./md/01.Introduction/03/MLX_Inference.md)
    - [استدلال Phi على خادم محلي](./md/01.Introduction/03/Local_Server_Inference.md)
    - [استدلال Phi على خادم بعيد باستخدام مجموعة أدوات AI](./md/01.Introduction/03/Remote_Interence.md)
    - [استدلال Phi باستخدام Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [استدلال Phi - الرؤية محليًا](./md/01.Introduction/03/Vision_Inference.md)
    - [استدلال Phi باستخدام Kaito AKS وAzure Containers (دعم رسمي)](./md/01.Introduction/03/Kaito_Inference.md)
-  [تكميم عائلة Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [تكميم Phi-3.5 / 4 باستخدام llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [تكميم Phi-3.5 / 4 باستخدام امتدادات Generative AI لـ onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [تكميم Phi-3.5 / 4 باستخدام Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [تكميم Phi-3.5 / 4 باستخدام إطار Apple MLX](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  تقييم Phi
    - [الذكاء الاصطناعي المسؤول](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry للتقييم](./md/01.Introduction/05/AIFoundry.md)
    - [استخدام Promptflow للتقييم](./md/01.Introduction/05/Promptflow.md)
 
- RAG مع Azure AI Search
    - [كيفية استخدام Phi-4-mini وPhi-4-multimodal(RAG) مع Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- عينات تطوير تطبيقات Phi
  - تطبيقات النص والدردشة
    - نماذج Phi-4 🆕
      - [📓] [الدردشة مع نموذج Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [الدردشة مع نموذج Phi-4 المحلي ONNX (.NET)](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [تطبيق وحدة تحكم .NET للدردشة مع Phi-4 ONNX باستخدام Sementic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - نماذج Phi-3 / 3.5
      - [روبوت دردشة محلي في المتصفح باستخدام Phi3 وONNX Runtime Web وWebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [دردشة OpenVINO](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [نموذج متعدد - Phi-3-mini التفاعلي وOpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - بناء غلاف واستخدام Phi-3 مع MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [تحسين النموذج - كيفية تحسين نموذج Phi-3-min لـ ONNX Runtime Web باستخدام Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [تطبيق WinUI3 مع Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[مثال تطبيق ملاحظات مدعوم بالذكاء الاصطناعي متعدد النماذج لـ WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [الضبط الدقيق ودمج نماذج Phi-3 المخصّصة مع Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [الضبط الدقيق ودمج نماذج Phi-3 المخصّصة مع Prompt flow في Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [تقييم نموذج Phi-3 / Phi-3.5 بعد الضبط الدقيق في Azure AI Foundry مع التركيز على مبادئ المسؤولية في الذكاء الاصطناعي لدى Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [مثال توقع اللغة لـ Phi-3.5-mini-instruct (الصينية/الإنجليزية)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [روبوت دردشة RAG لـ Phi-3.5-Instruct على WebGPU](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [استخدام GPU في Windows لإنشاء حل Prompt flow مع Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [استخدام Microsoft Phi-3.5 tflite لإنشاء تطبيق Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [مثال سؤال وجواب .NET باستخدام نموذج Phi-3 محلي ONNX عبر Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [تطبيق سطر أوامر .NET للدردشة مع Semantic Kernel وPhi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - عيّنات برمجية لـ Azure AI Inference SDK 
    - Phi-4 Samples 🆕
      - [📓] [توليد كود المشروع باستخدام Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 Samples
      - [ابنِ دردشة GitHub Copilot في Visual Studio Code خاصة بك باستخدام عائلة Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [أنشئ وكيلاً للدردشة في Visual Studio Code باستخدام Phi-3.5 من GitHub Models](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - عينات التفكير المتقدم
    - Phi-4 Samples 🆕
      - [📓] [عينات Phi-4-mini-reasoning أو Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [الضبط الدقيق لـ Phi-4-mini-reasoning باستخدام Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [الضبط الدقيق لـ Phi-4-mini-reasoning باستخدام Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning مع GitHub Models](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-reasoning مع نماذج Azure AI Foundry](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demos
      - [عروض Phi-4-mini المستضافة على Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [عروض Phi-4-multimodal المستضافة على Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Vision Samples
    - Phi-4 Samples 🆕
      - [📓] [استخدام Phi-4-multimodal لقراءة الصور وتوليد الكود](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 Samples
      -  [📓][Phi-3-vision-Image text to text](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][تضمين CLIP لـ Phi-3-vision](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [عرض توضيحي: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - مساعد اللغة البصرية - مع Phi3-Vision وOpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][مثال Phi-3.5 Vision متعدد الإطارات أو متعدد الصور](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [نموذج Phi-3 Vision محلي ONNX باستخدام Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [نموذج Phi-3 Vision محلي ONNX قائم على القائمة باستخدام Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - نماذج الرياضيات
    -  Phi-4-Mini-Flash-Reasoning-Instruct Samples 🆕 [عرض رياضي مع Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - نماذج الصوت
    - Phi-4 Samples 🆕
      - [📓] [استخراج نصوص الصوت باستخدام Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [مثال صوتي لـ Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [مثال ترجمة كلامية لـ Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET console application using Phi-4-multimodal Audio to analyze an audio file and generate transcript](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE Samples
    - Phi-3 / 3.5 Samples
      - [📓] [مثال وسائل التواصل الاجتماعي لنماذج Phi-3.5 Mixture of Experts (MoEs)](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [بناء خط أنابيب الاسترجاع المعزز بالتوليد (RAG) باستخدام NVIDIA NIM Phi-3 MOE وAzure AI Search وLlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - نماذج استدعاء الدوال
    - Phi-4 Samples 🆕
      -  [📓] [استخدام استدعاء الدوال مع Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [استخدام استدعاء الدوال لإنشاء وكلاء متعددين مع Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [استخدام استدعاء الدوال مع Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [استخدام استدعاء الدوال مع ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling_ipynb)
  - نماذج المزج متعدد الوسائط
    - Phi-4 Samples 🆕
      -  [📓] [استخدام Phi-4-multimodal كصحفي تقني](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET console application using Phi-4-multimodal to analyze images](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- عينات الضبط الدقيق لنماذج Phi
  - [سيناريوهات الضبط الدقيق](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [الضبط الدقيق مقابل RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [الضبط الدقيق: جعل Phi-3 خبيرًا صناعيًا](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [الضبط الدقيق لـ Phi-3 باستخدام AI Toolkit لـ VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [الضبط الدقيق لـ Phi-3 باستخدام Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [الضبط الدقيق لـ Phi-3 باستخدام Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [الضبط الدقيق لـ Phi-3 باستخدام QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [الضبط الدقيق لـ Phi-3 باستخدام Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [الضبط الدقيق لـ Phi-3 باستخدام Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [الضبط الدقيق باستخدام Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [الضبط الدقيق مع مختبر Microsoft Olive العملي](./md/03.FineTuning/olive-lab/readme.md)
  - [الضبط الدقيق لـ Phi-3-vision باستخدام Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [الضبط الدقيق لـ Phi-3 باستخدام إطار عمل Apple MLX](./md/03.FineTuning/FineTuning_MLX.md)
  - [الضبط الدقيق لـ Phi-3-vision (دعم رسمي)](./md/03.FineTuning/FineTuning_Vision.md)
  - [الضبط الدقيق لـ Phi-3 مع Kaito AKS وAzure Containers (دعم رسمي)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [الضبط الدقيق لـ Phi-3 و3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- مختبر عملي
  - [استكشاف النماذج المتطورة: LLMs، SLMs، التطوير المحلي والمزيد](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [فتح إمكانات معالجة اللغة الطبيعية: الضبط الدقيق باستخدام Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- الأوراق البحثية والمنشورات الأكاديمية
  - [Textbooks Are All You Need II: تقرير تقني عن phi-1.5](https://arxiv.org/abs/2309.05463)
  - [تقرير تقني Phi-3: نموذج لغة عالي القدرة يعمل محليًا على هاتفك](https://arxiv.org/abs/2404.14219)
  - [تقرير تقني Phi-4](https://arxiv.org/abs/2412.08905)
  - [تقرير تقني Phi-4-Mini: نماذج لغوية متعددة الوسائط صغيرة لكنها قوية عبر Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [تحسين نماذج اللغة الصغيرة لاستدعاء الوظائف داخل المركبة](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) ضبط دقيق لـ PHI-3 للإجابة على أسئلة الاختيار من متعدد: المنهجية، النتائج، والتحديات](https://arxiv.org/abs/2501.01588)
  - [تقرير تقني Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [تقرير تقني Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## استخدام نماذج Phi

### Phi على Azure AI Foundry

يمكنك معرفة كيفية استخدام مايكروسوفت Phi وكيفية بناء حلول شاملة من طرف إلى طرف على أجهزتك المختلفة. لتجربة Phi بنفسك، ابدأ بالتجربة مع النماذج وتخصيص Phi لسيناريوهاتك باستخدام [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) يمكنك معرفة المزيد في البدء السريع مع [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**بيئة تجريبية**
كل نموذج لديه بيئة تجريب مخصصة لاختبار النموذج [بيئة اختبار Azure AI](https://aka.ms/try-phi3).

### Phi على نماذج GitHub

يمكنك معرفة كيفية استخدام مايكروسوفت Phi وكيفية بناء حلول شاملة من طرف إلى طرف على أجهزتك المختلفة. لتجربة Phi بنفسك، ابدأ بالتجربة مع النموذج وتخصيص Phi لسيناريوهاتك باستخدام الـ [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) يمكنك معرفة المزيد في البدء السريع مع [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**بيئة تجريبية**
كل نموذج لديه [بيئة تجريب مخصصة لاختبار النموذج](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi على Hugging Face

يمكنك أيضًا العثور على النموذج على [Hugging Face](https://huggingface.co/microsoft)

**بيئة تجريبية**
 [بيئة Hugging Chat التجريبية](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 دورات أخرى

فريقنا ينتج دورات أخرى! اطلع على:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j للمبتدئين](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js للمبتدئين](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / الوكلاء
[![AZD للمبتدئين](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI للمبتدئين](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP للمبتدئين](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![وكلاء الذكاء الاصطناعي للمبتدئين](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### سلسلة الذكاء التوليدي
[![الذكاء التوليدي للمبتدئين](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![الذكاء التوليدي (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![الذكاء التوليدي (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![الذكاء التوليدي (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### التعلم الأساسي
[![تعلم الآلة للمبتدئين](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![علوم البيانات للمبتدئين](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![الذكاء الاصطناعي للمبتدئين](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![الأمن السيبراني للمبتدئين](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![تطوير الويب للمبتدئين](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![إنترنت الأشياء للمبتدئين](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![تطوير الواقع الممتد للمبتدئين](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### سلسلة كوبيلوت
[![كوبيلوت للبرمجة الزوجية المدعومة بالذكاء الاصطناعي](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![كوبيلوت لـ C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![مغامرة كوبيلوت](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## الذكاء الاصطناعي المسؤول

تلتزم مايكروسوفت بمساعدة عملائنا على استخدام منتجات الذكاء الاصطناعي لدينا بمسؤولية، ومشاركة ما تعلمناه، وبناء شراكات قائمة على الثقة من خلال أدوات مثل ملاحظات الشفافية وتقييمات الأثر. يمكن العثور على العديد من هذه الموارد على [https://aka.ms/RAI](https://aka.ms/RAI).
نهج مايكروسوفت تجاه الذكاء الاصطناعي المسؤول قائم على مبادئنا للذكاء الاصطناعي وهي: الإنصاف، والموثوقية والسلامة، والخصوصية والأمن، والشمولية، والشفافية، والمساءلة.

يمكن أن تتصرف نماذج اللغة والصورة والصوت واسعة النطاق - مثل تلك المستخدمة في هذا المثال - بطرق قد تكون غير عادلة أو غير موثوقة أو مسيئة، مما قد يسبب أضرارًا. يرجى الاطلاع على [مذكرة الشفافية لخدمة Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) للاطّلاع على المخاطر والقيود.

النهج الموصى به للتخفيف من هذه المخاطر هو تضمين نظام أمان في بنية التطبيق الخاص بك يمكنه اكتشاف ومنع السلوك الضار. توفر [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) طبقة حماية مستقلة، قادرة على اكتشاف المحتوى الضار الذي ينشئه المستخدم أو المحتوى الناتج عن الذكاء الاصطناعي في التطبيقات والخدمات. يتضمن Azure AI Content Safety واجهات برمجة تطبيقات النص والصورة التي تتيح لك اكتشاف المواد الضارة. داخل Azure AI Foundry، تتيح خدمة Content Safety عرض واستكشاف وتجربة أمثلة التعليمات البرمجية لاكتشاف المحتوى الضار عبر وسائط مختلفة. توجهك الوثائق التالية لبدء الاستخدام [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) في كيفية إرسال الطلبات إلى الخدمة.

جانب آخر يجب أخذه في الاعتبار هو أداء التطبيق بشكل عام. مع تطبيقات متعددة الوسائط ومتعددة النماذج، نعتبر أن الأداء يعني أن النظام يعمل كما تتوقع أنت ومستخدموك، بما في ذلك عدم إنتاج مخرجات ضارة. من المهم تقييم أداء تطبيقك العام باستخدام [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). لديك أيضًا القدرة على الإنشاء والتقييم باستخدام [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

يمكنك تقييم تطبيق الذكاء الاصطناعي الخاص بك في بيئة التطوير باستخدام [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). سواء باستخدام مجموعة بيانات اختبار أو هدف معين، يتم قياس مخرجات تطبيق الذكاء الاصطناعي التوليدي الخاص بك كمياً باستخدام مقيمين مدمجين أو المقيمين المخصصين من اختيارك. للبدء باستخدام azure ai evaluation sdk لتقييم نظامك، يمكنك اتباع [دليل البدء السريع](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). بمجرد تنفيذ تشغيل التقييم، يمكنك [عرض النتائج مرئيًا في Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## العلامات التجارية
قد يحتوي هذا المشروع على علامات تجارية أو شعارات لمشاريع أو منتجات أو خدمات. الاستخدام المصرح به لعلامات مايكروسوفت التجارية أو شعاراتها يخضع ويجب أن يتوافق مع [إرشادات العلامة التجارية والهوية لمايكروسوفت](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
يجب أن لا يتسبب استخدام علامات مايكروسوفت التجارية أو شعاراتها في نسخ معدلة من هذا المشروع في حدوث لبس أو الإيحاء برعاية مايكروسوفت. أي استخدام لعلامات تجارية أو شعارات طرف ثالث يخضع لسياسات تلك الأطراف.

## الحصول على المساعدة

إذا علقت أو كانت لديك أي أسئلة حول بناء تطبيقات الذكاء الاصطناعي، انضم إلى:

[![خادم Discord الخاص بـ Azure AI Foundry](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

إذا كان لديك ملاحظات عن المنتج أو أخطاء أثناء البناء، قم بزيارة:

[![منتدى مطوري Azure AI Foundry](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
إخلاء مسؤولية:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية Co-op Translator (https://github.com/Azure/co-op-translator). بينما نسعى جاهدين لتحقيق الدقة، يُرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد. للمعلومات الحرجة، يُنصح بالاستعانة بترجمة بشرية محترفة. لا نتحمل أي مسؤولية عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->