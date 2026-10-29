# كتاب فاراي: أمثلة عملية مع نماذج Phi من مايكروسوفت

[![افتح واستخدم العينات في GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![افتح في حاويات التطوير](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![مساهمو GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![مشاكل GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![طلبات السحب في GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![مرحب بطلبات السحب](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![مشاهدو GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![تفريعات GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![نجوم GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![ديسكورد Microsoft Foundry](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi هي سلسلة من نماذج الذكاء الاصطناعي مفتوحة المصدر التي طورتها مايكروسوفت.

Phi هو حالياً أصغر نموذج لغة قوي وفعال من حيث التكلفة (SLM)، مع مؤشرات أداء جيدة جداً في تعدد اللغات، الاستدلال، إنشاء النصوص/الدردشة، الترميز، الصور، الصوت وسيناريوهات أخرى.

يمكنك نشر Phi على السحابة أو على أجهزة الحافة، ويمكنك بسهولة بناء تطبيقات الذكاء الاصطناعي التوليدية مع قدرة حسابية محدودة.

اتبع هذه الخطوات لتبدأ باستخدام هذه الموارد:
1. **افتح مستودع النسخة**: اضغط [![تفريعات GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **انسخ المستودع**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**انضم إلى مجتمع مايكروسوفت AI على ديسكورد والتق بخبراء ومطوّرين آخرين**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/ar/cover.eb18d1b9605d754b.webp)

### 🌐 دعم متعدد اللغات

#### مدعوم عبر GitHub Action (آلي ومُحدّث دائماً)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[العربية](./README.md) | [البنغالية](../bn/README.md) | [البلغارية](../bg/README.md) | [البورمية (ميانمار)](../my/README.md) | [الصينية (المبسطة)](../zh-CN/README.md) | [الصينية (التقليدية، هونغ كونغ)](../zh-HK/README.md) | [الصينية (التقليدية، ماكاو)](../zh-MO/README.md) | [الصينية (التقليدية، تايوان)](../zh-TW/README.md) | [الكرواتية](../hr/README.md) | [التشيكية](../cs/README.md) | [الدانمركية](../da/README.md) | [الهولندية](../nl/README.md) | [الإستونية](../et/README.md) | [الفنلندية](../fi/README.md) | [الفرنسية](../fr/README.md) | [الألمانية](../de/README.md) | [اليونانية](../el/README.md) | [العبرية](../he/README.md) | [الهندية](../hi/README.md) | [الهنغارية](../hu/README.md) | [الإندونيسية](../id/README.md) | [الإيطالية](../it/README.md) | [اليابانية](../ja/README.md) | [الكانتادية](../kn/README.md) | [الخمرية](../km/README.md) | [الكورية](../ko/README.md) | [الليتوانية](../lt/README.md) | [الملايوية](../ms/README.md) | [المالايالامية](../ml/README.md) | [الماراثية](../mr/README.md) | [النيبالية](../ne/README.md) | [النيجيرية بيدجين](../pcm/README.md) | [النرويجية](../no/README.md) | [الفارسية (الفرسية)](../fa/README.md) | [البولندية](../pl/README.md) | [البرتغالية (البرازيل)](../pt-BR/README.md) | [البرتغالية (البرتغال)](../pt-PT/README.md) | [البنجابية (غورموخي)](../pa/README.md) | [الرومانية](../ro/README.md) | [الروسية](../ru/README.md) | [الصربية (السيريلية)](../sr/README.md) | [السلوفاكية](../sk/README.md) | [السلوفينية](../sl/README.md) | [الإسبانية](../es/README.md) | [السواحيلية](../sw/README.md) | [السويدية](../sv/README.md) | [التاغالوغ (الفلبينية)](../tl/README.md) | [التاميلية](../ta/README.md) | [التيلجو](../te/README.md) | [التايلاندية](../th/README.md) | [التركية](../tr/README.md) | [الأوكرانية](../uk/README.md) | [الأردية](../ur/README.md) | [الفيتنامية](../vi/README.md)

> **هل تفضل النسخ محلياً؟**
>
> يشمل هذا المستودع أكثر من 50 ترجمة لغوية مما يزيد بشكل كبير من حجم التنزيل. للنسخ بدون الترجمات، استخدم الفحص المتفرق:
>
> **باش / ماك أو إس / لينكس:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **موجه الأوامر (ويندوز):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> هذا يوفر لك كل ما تحتاجه لإكمال الدورة مع تحميل أسرع بكثير.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## جدول المحتويات

- مقدمة
  - [مرحباً بكم في عائلة Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [إعداد بيئتك](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [فهم التقنيات الأساسية](./md/01.Introduction/01/01.Understandingtech.md)
  - [أمان الذكاء الاصطناعي لنماذج Phi](./md/01.Introduction/01/01.AISafety.md)
  - [دعم الأجهزة لنماذج Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [نماذج Phi وتوافرها عبر المنصات](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [استخدام Guidance-ai و Phi](./md/01.Introduction/01/01.Guidance.md)
  - [نماذج سوق GitHub](https://github.com/marketplace/models)
  - [كتالوج نماذج Azure AI](https://ai.azure.com)

- الاستدلال باستخدام Phi في بيئات مختلفة
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [نماذج GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [كتالوج نماذج Microsoft Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [أدوات AI لـ VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- استدلال عائلة Phi
    - [الاستدلال باستخدام Phi في iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [الاستدلال باستخدام Phi في Android](./md/01.Introduction/03/Android_Inference.md)
    - [الاستدلال باستخدام Phi في Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [الاستدلال باستخدام Phi في الحاسوب AI](./md/01.Introduction/03/AIPC_Inference.md)
    - [الاستدلال باستخدام Phi مع إطار Apple MLX](./md/01.Introduction/03/MLX_Inference.md)
    - [الاستدلال باستخدام Phi في الخادم المحلي](./md/01.Introduction/03/Local_Server_Inference.md)
    - [الاستدلال باستخدام Phi في الخادم البعيد باستخدام AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [الاستدلال باستخدام Phi مع Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [الاستدلال برؤية Phi محلياً](./md/01.Introduction/03/Vision_Inference.md)
    - [الاستدلال باستخدام Phi مع Kaito AKS، حاويات Azure (الدعم الرسمي)](./md/01.Introduction/03/Kaito_Inference.md)
-  [تكميم عائلة Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [تكميم Phi-3.5 / 4 باستخدام llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [تكميم Phi-3.5 / 4 باستخدام امتدادات الذكاء الاصطناعي التوليدي لـ onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [تكميم Phi-3.5 / 4 باستخدام Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [تكميم Phi-3.5 / 4 باستخدام إطار Apple MLX](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  تقييم Phi
    - [ذكاء اصطناعي مسؤول](./md/01.Introduction/05/ResponsibleAI.md)
    - [مايكروسوفت فوندري للتقييم](./md/01.Introduction/05/AIFoundry.md)
    - [استخدام Promptflow للتقييم](./md/01.Introduction/05/Promptflow.md)
 
- RAG مع Azure AI Search
    - [كيفية استخدام Phi-4-mini و Phi-4-multimodal(RAG) مع Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)
    - [RAG هجين محلي بدون سحابة مع SQLite FTS5 و phi-4-mini](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-mini_Local_Hybrid_RAG_SQLite_FTS5.ipynb)

- عينات تطوير تطبيقات Phi
  - تطبيقات النص والدردشة
    - عينات Phi-4 
      - [📓] [دردشة مع نموذج Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [دردشة مع نموذج Phi-4 محلي ONNX .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [تطبيق دردشة .NET Console مع Phi-4 ONNX باستخدام السيمانتك كيرنل](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)

    - عينات Phi-3 / 3.5
      - [دردشة بوت محلي في المتصفح باستخدام Phi3، ONNX Runtime Web و WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [دردشة OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [نموذج متعدد - Phi-3-mini تفاعلي و OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - بناء غلاف واستخدام Phi-3 مع MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [تحسين النموذج - كيفية تحسين نموذج Phi-3-min لـ ONNX Runtime Web باستخدام Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [تطبيق WinUI3 مع Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[مثال لتطبيق ملاحظات متعدد النماذج مدعوم بالذكاء الاصطناعي WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [ضبط دقيق ودمج نماذج Phi-3 مخصصة مع Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [ضبط دقيق ودمج نماذج Phi-3 مخصصة مع Prompt flow في Microsoft Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [تقييم نموذج Phi-3 / Phi-3.5 المضبوط بدقة في Microsoft Foundry مع التركيز على مبادئ الذكاء الاصطناعي المسؤول من Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [مثال تنبؤ لغوي بـ Phi-3.5-mini-instruct (بالصينية/الإنجليزية)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [بوت الدردشة Phi-3.5-Instruct WebGPU RAG](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [استخدام GPU في ويندوز لإنشاء حل Prompt flow مع Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [استخدام Microsoft Phi-3.5 tflite لإنشاء تطبيق أندرويد](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [مثال أسئلة وأجوبة .NET باستخدام نموذج ONNX Phi-3 المحلي بواسطة Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [تطبيق دردشة وحدة التحكم .NET مع Semantic Kernel و Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - عينات SDK الاستدلال لـ Azure AI 
    - عينات Phi-4 
      - [📓] [توليد رمز المشروع باستخدام Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - عينات Phi-3 / 3.5
      - [بناء دردشة GitHub Copilot الخاصة بك في Visual Studio Code مع عائلة Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [إنشاء وكيل دردشة GitHub Copilot خاص بك في Visual Studio Code مع Phi-3.5 بواسطة نماذج GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - عينات التفكير المتقدم
    - عينات Phi-4 
      - [📓] [عينات Phi-4-mini-reasoning أو Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [ضبط دقيق لـ Phi-4-mini-reasoning مع Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [ضبط دقيق لـ Phi-4-mini-reasoning مع Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning مع نماذج GitHub](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-reasoning مع نماذج Microsoft Foundry](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - عروض توضيحية
      - [عروض Phi-4-mini مستضافة على Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [عروض Phi-4-multimodal مستضافة على Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - عينات رؤية
    - عينات Phi-4 
      - [📓] [استخدام Phi-4-multimodal لقراءة الصور وتوليد الشفرة](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - عينات Phi-3 / 3.5
      -  [📓][Phi-3-vision-تحويل نص الصورة إلى نص](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision تضمين CLIP](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [عرض توضيحي: تدوير Phi-3](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - مساعد لغة بصري - مع Phi3-Vision و OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][عينة رؤى متعددة الإطارات أو متعددة الصور بـ Phi-3.5 Vision](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [نموذج ONNX محلي لرؤية Phi-3 باستخدام Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [نموذج ONNX محلي لرؤية Phi-3 قائم على القائمة باستخدام Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - عينات التفكير والرؤية
    - Phi-4-Reasoning-Vision-15B 
      - [📓] [استخدام Phi-4-Reasoning-Vision-15B لاكتشاف عبور المشاة غير القانوني](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb)
      - [📓] [استخدام Phi-4-Reasoning-Vision-15B في الرياضيات](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb)
      - [📓] [استخدام Phi-4-Reasoning-Vision-15B لاكتشاف واجهة المستخدم](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb)

  - عينات الرياضيات
    -  عينات Phi-4-Mini-Flash-Reasoning-Instruct  [عرض تجريبي للرياضيات مع Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - عينات الصوت
    - عينات Phi-4 
      - [📓] [استخراج نصوص الصوت باستخدام Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [عينة صوت Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [عينة ترجمة الكلام Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [تطبيق وحدة التحكم .NET باستخدام Phi-4-multimodal لتحليل ملف صوتي وتوليد نص](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - عينات MOE
    - عينات Phi-3 / 3.5
      - [📓] [نماذج خليط الخبراء Phi-3.5 (MoEs) عينة وسائل التواصل الاجتماعي](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [بناء خط إنتاج التوليد المعزز بالاستخراج (RAG) باستخدام NVIDIA NIM Phi-3 MOE، Azure AI Search، و LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - عينات استدعاء الوظائف
    - عينات Phi-4 🆕
      -  [📓] [استخدام استدعاء الوظائف مع Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [استخدام استدعاء الوظائف لإنشاء وكلاء متعددين مع Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [استخدام استدعاء الوظائف مع Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [استخدام استدعاء الوظائف مع ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - عينات الخلط المتعدد الأنماط
    - عينات Phi-4 🆕
      -  [📓] [استخدام Phi-4-multimodal كصحفي تقني](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [تطبيق وحدة التحكم .NET باستخدام Phi-4-multimodal لتحليل الصور](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- ضبط دقيق لعينة Phi
  - [سيناريوهات الضبط الدقيق](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [الضبط الدقيق مقابل RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [اضبط Phi-3 ليصبح خبيرًا في الصناعة](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [ضبط دقيق لـ Phi-3 باستخدام مجموعة أدوات AI لـ VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [ضبط دقيق لـ Phi-3 باستخدام خدمة تعلم الآلة Azure](./md/03.FineTuning/Introduce_AzureML.md)
  - [ضبط دقيق لـ Phi-3 مع Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [ضبط دقيق لـ Phi-3 مع QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [ضبط دقيق لـ Phi-3 مع Microsoft Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [ضبط دقيق لـ Phi-3 باستخدام Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [الضبط الدقيق مع Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [الضبط الدقيق مع مختبر عملي Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)
  - [ضبط دقيق لرؤية Phi-3 باستخدام Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)

  - [تخصيص Phi-3 باستخدام إطار عمل Apple MLX](./md/03.FineTuning/FineTuning_MLX.md)
  - [تخصيص Phi-3-vision (الدعم الرسمي)](./md/03.FineTuning/FineTuning_Vision.md)
  - [تخصيص Phi-3 باستخدام Kaito AKS ، حاويات Azure (الدعم الرسمي)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [تخصيص Phi-3 و 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- مختبر عملي
  - [استكشاف النماذج المتطورة: LLMs، SLMs، التطوير المحلي والمزيد](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [إطلاق إمكانيات معالجة اللغة الطبيعية: التخصيص باستخدام Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- أوراق وأبحاث أكاديمية ومنشورات
  - [الكتب الدراسية هي كل ما تحتاجه II: تقرير فني phi-1.5](https://arxiv.org/abs/2309.05463)
  - [تقرير فني Phi-3: نموذج لغة عالي الكفاءة محليًا على هاتفك](https://arxiv.org/abs/2404.14219)
  - [تقرير فني Phi-4](https://arxiv.org/abs/2412.08905)
  - [تقرير فني Phi-4-Mini: نماذج لغوية متعددة الوسائط مدمجة وقوية من خلال خليط من LoRAs](https://arxiv.org/abs/2503.01743)
  - [تحسين النماذج اللغوية الصغيرة لاستدعاء الوظائف في المركبات](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) تخصيص PHI-3 للإجابة على أسئلة الاختيار من متعدد: المنهجية، النتائج، والتحديات](https://arxiv.org/abs/2501.01588)
  - [تقرير فني Phi-4 للتفكير](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [تقرير فني Phi-4-mini للتفكير](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## استخدام نماذج Phi

### Phi على Microsoft Foundry

يمكنك معرفة كيفية استخدام Microsoft Phi وكيفية بناء حلول شاملة في أجهزتك المختلفة. لتجربة Phi بنفسك، ابدأ بالتفاعل مع النماذج وتخصيص Phi لسيناريوهاتك باستخدام [كتالوج نماذج Microsoft Foundry Azure AI](https://aka.ms/phi3-azure-ai) يمكنك معرفة المزيد في البدء مع [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**ميدان اللعب**
لكل نموذج ميدان لعب مخصص لاختبار النموذج [Azure AI Playground](https://aka.ms/try-phi3).

### Phi على نماذج GitHub

يمكنك تعلم كيفية استخدام Microsoft Phi وكيفية بناء حلول شاملة في أجهزتك المختلفة. لتجربة Phi بنفسك، ابدأ باللعب مع النموذج وتخصيص Phi لسيناريوهاتك باستخدام [كتالوج نماذج GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) يمكنك معرفة المزيد في البدء مع [كتالوج نماذج GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md)

**ميدان اللعب**
لكل نموذج [ميدان لعب مخصص لاختبار النموذج](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi على Hugging Face

يمكنك أيضًا العثور على النموذج على [Hugging Face](https://huggingface.co/microsoft)

**ميدان اللعب**
 [ميدان لعب Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 دورات أخرى

يقوم فريقنا بإنتاج دورات أخرى! اطلع على:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j للمبتدئين](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js للمبتدئين](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain للمبتدئين](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / الوكلاء
[![AZD للمبتدئين](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI للمبتدئين](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP للمبتدئين](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![وكلاء الذكاء الاصطناعي للمبتدئين](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### سلسلة الذكاء الاصطناعي التوليدي
[![الذكاء الاصطناعي التوليدي للمبتدئين](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![الذكاء الاصطناعي التوليدي (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![الذكاء الاصطناعي التوليدي (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![الذكاء الاصطناعي التوليدي (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### التعلم الأساسي
[![التعلم الآلي للمبتدئين](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![علوم البيانات للمبتدئين](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![الذكاء الاصطناعي للمبتدئين](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![الأمن السيبراني للمبتدئين](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![تطوير الويب للمبتدئين](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![انترنت الأشياء للمبتدئين](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![تطوير XR للمبتدئين](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### سلسلة Copilot
[![Copilot للبرمجة المصاحبة بالذكاء الاصطناعي](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot لـ C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![مغامرة Copilot](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## الذكاء الاصطناعي المسؤول

تلتزم مايكروسوفت بمساعدة عملائنا على استخدام منتجات الذكاء الاصطناعي لدينا بمسؤولية، ومشاركة خبراتنا، وبناء شراكات قائمة على الثقة من خلال أدوات مثل ملاحظات الشفافية وتقييمات التأثير. يمكن العثور على العديد من هذه الموارد في [https://aka.ms/RAI](https://aka.ms/RAI).
يعتمد نهج مايكروسوفت تجاه الذكاء الاصطناعي المسؤول على مبادئ الذكاء الاصطناعي لدينا المتعلقة بالإنصاف، والموثوقية والسلامة، والخصوصية والأمان، والشمولية، والشفافية، والمسائلة.

يمكن للنماذج الطبيعية واسعة النطاق للغة والصورة والصوت - مثل تلك المستخدمة في هذا المثال - أن تتصرف ربما بطرق غير عادلة أو غير موثوقة أو مسيئة، مما قد يسبب أضرارًا. يرجى الاطلاع على [ملاحظة الشفافية لخدمة Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) للتعرف على المخاطر والقيود.


النهج الموصى به للتقليل من هذه المخاطر هو تضمين نظام أمان في البنية التحتية الخاصة بك يمكنه اكتشاف ومنع السلوك الضار. يوفر [أمان المحتوى في Azure AI](https://learn.microsoft.com/azure/ai-services/content-safety/overview) طبقة حماية مستقلة، قادرة على اكتشاف المحتوى الضار الذي يُنتجه المستخدمون أو الذكاء الاصطناعي في التطبيقات والخدمات. يشمل أمان المحتوى في Azure AI واجهات برمجة التطبيقات للنصوص والصور التي تتيح لك اكتشاف المواد الضارة. داخل Microsoft Foundry، تتيح لك خدمة أمان المحتوى عرض واستكشاف وتجربة أكواد تجريبية لاكتشاف المحتوى الضار عبر أنماط متعددة. الوثائق [التمهيدية السريعة](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) التالية ترشدك خلال كيفية إرسال الطلبات إلى الخدمة.

جانب آخر يجب أخذه في الاعتبار هو الأداء العام للتطبيق. بالنسبة للتطبيقات متعددة الأنماط والنماذج، نعتبر أن الأداء يعني أن النظام يعمل كما تتوقع أنت ومستخدموك، بما في ذلك عدم توليد مخرجات ضارة. من المهم تقييم أداء تطبيقك العام باستخدام [مقاييس الأداء والجودة والمخاطر والسلامة](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). لديك أيضًا القدرة على الإنشاء والتقييم باستخدام [مقاييس مخصصة](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

يمكنك تقييم تطبيق الذكاء الاصطناعي الخاص بك في بيئة التطوير باستخدام [مجموعة أدوات تقييم Azure AI](https://microsoft.github.io/promptflow/index.html). استنادًا إلى مجموعة بيانات اختبار أو هدف، يتم قياس توليدات تطبيق الذكاء الاصطناعي التوليدي لديك بشكل كمي باستخدام المقاييس المدمجة أو المقاييس المخصصة التي تختارها. لبدء استخدام مجموعة أدوات تقييم Azure AI لتقييم نظامك، يمكنك اتباع [دليل البدء السريع](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). بمجرد تنفيذ تشغيل التقييم، يمكنك [عرض النتائج في Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## العلامات التجارية

قد يحتوي هذا المشروع على علامات تجارية أو شعارات لمشاريع أو منتجات أو خدمات. الاستخدام المصرح به لعلامات أو شعارات Microsoft يجب أن يتبع ويخضع لـ [إرشادات العلامة التجارية والهوية التجارية لشركة Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
يجب ألا يتسبب استخدام علامات أو شعارات Microsoft في نسخ معدلة من هذا المشروع في حدوث ارتباك أو يوحي برعاية Microsoft. أي استخدام لعلامات أو شعارات تتبع طرفًا ثالثًا يخضع لسياسات ذلك الطرف الثالث.

## الحصول على المساعدة

إذا واجهت صعوبة أو كان لديك أي أسئلة حول بناء تطبيقات الذكاء الاصطناعي، انضم إلى:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

إذا كان لديك ملاحظات على المنتج أو أخطاء أثناء البناء، قم بزيارة:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->