# كتاب وصفات Phi: أمثلة عملية مع نماذج Phi من مايكروسوفت

[![افتح واستخدم العينات في GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![فتح في حاويات التطوير](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![مساهمو GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![قضايا GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![طلبات السحب في GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![طلبات السحب مرحب بها](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![مراقبو GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![تفرعات GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![نجوم GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![خادم Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi هو سلسلة من نماذج الذكاء الاصطناعي مفتوحة المصدر طورتها مايكروسوفت.

يعتبر Phi حالياً أقوى نموذج لغة صغير (SLM) من حيث الأداء والتكلفة، مع مؤشرات أداء جيدة جداً في اللغات المتعددة، والاستدلال، وتوليد النصوص/الدردشة، والبرمجة، والصور، والصوت، وسيناريوهات أخرى.

يمكنك نشر Phi على السحابة أو على أجهزة الحافة، ويمكنك بناء تطبيقات ذكاء اصطناعي توليدية بسهولة باستخدام قوة حوسبية محدودة.

اتبع هذه الخطوات للبدء في استخدام هذه الموارد:
1. **انسخ المستودع**: انقر على [![تفرعات GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **انسخ المستودع محلياً**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**انضم إلى مجتمع Discord للذكاء الاصطناعي من مايكروسوفت وتعرف على الخبراء والمطورين الزملاء**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/ar/cover.eb18d1b9605d754b.webp)

### 🌐 دعم متعدد اللغات

#### مدعوم عبر GitHub Action (آلي ومحدث دائماً)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[العربية](./README.md) | [البنغالية](../bn/README.md) | [البلغارية](../bg/README.md) | [البورمية (ميانمار)](../my/README.md) | [الصينية (المبسطة)](../zh-CN/README.md) | [الصينية (التقليدية، هونغ كونغ)](../zh-HK/README.md) | [الصينية (التقليدية، ماكاو)](../zh-MO/README.md) | [الصينية (التقليدية، تايوان)](../zh-TW/README.md) | [الكرواتية](../hr/README.md) | [التشيكية](../cs/README.md) | [الدنماركية](../da/README.md) | [الهولندية](../nl/README.md) | [الإستونية](../et/README.md) | [الفنلندية](../fi/README.md) | [الفرنسية](../fr/README.md) | [الألمانية](../de/README.md) | [اليونانية](../el/README.md) | [العبرية](../he/README.md) | [الهندية](../hi/README.md) | [الهنغارية](../hu/README.md) | [الإندونيسية](../id/README.md) | [الإيطالية](../it/README.md) | [اليابانية](../ja/README.md) | [الكانادا](../kn/README.md) | [الكورية](../ko/README.md) | [اللتوانية](../lt/README.md) | [الماليزية](../ms/README.md) | [المالايالامية](../ml/README.md) | [الماراثية](../mr/README.md) | [النيبالية](../ne/README.md) | [البيدجن النيجيرية](../pcm/README.md) | [النرويجية](../no/README.md) | [الفارسية (اللغة)](../fa/README.md) | [البولندية](../pl/README.md) | [البرتغالية (البرازيل)](../pt-BR/README.md) | [البرتغالية (البرتغال)](../pt-PT/README.md) | [البنجابية (الغورموخي)](../pa/README.md) | [الرومانية](../ro/README.md) | [الروسية](../ru/README.md) | [الصربية (السيريلية)](../sr/README.md) | [السلوفاكية](../sk/README.md) | [السلوفينية](../sl/README.md) | [الإسبانية](../es/README.md) | [السواحيلية](../sw/README.md) | [السويدية](../sv/README.md) | [التاغالوغ (الفلبينية)](../tl/README.md) | [التاميلية](../ta/README.md) | [التيلجو](../te/README.md) | [التايلاندية](../th/README.md) | [التركية](../tr/README.md) | [الأوكرانية](../uk/README.md) | [الأردية](../ur/README.md) | [الفيتنامية](../vi/README.md)

> **تفضل النسخ محلياً؟**
>
> يحتوي هذا المستودع على أكثر من 50 ترجمة للغات مما يزيد بشكل كبير من حجم التنزيل. للنسخ بدون الترجمات، استخدم sparse checkout:
>
> **باش / ماك أو إس / لينكس:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (ويندوز):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> هذا يمنحك كل ما تحتاجه لإكمال الدورة مع تنزيل أسرع بكثير.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## جدول المحتويات
- المقدمة - [مرحبًا بك في عائلة فاي](./md/01.Introduction/01/01.PhiFamily.md) - [إعداد بيئتك](./md/01.Introduction/01/01.EnvironmentSetup.md) - [فهم التقنيات الرئيسية](./md/01.Introduction/01/01.Understandingtech.md) - [سلامة الذكاء الاصطناعي لنماذج فاي](./md/01.Introduction/01/01.AISafety.md) - [دعم أجهزة فاي](./md/01.Introduction/01/01.Hardwaresupport.md) - [نماذج فاي والتوافر عبر المنصات](./md/01.Introduction/01/01.Edgeandcloud.md) - [استخدام Guidance-ai وفاي](./md/01.Introduction/01/01.Guidance.md) - [نماذج سوق GitHub](https://github.com/marketplace/models) - [كتالوج نماذج Azure AI](https://ai.azure.com) - استدلال فاي في بيئات مختلفة - [Hugging face](./md/01.Introduction/02/01.HF.md) - [نماذج GitHub](./md/01.Introduction/02/02.GitHubModel.md) - [كتالوج نماذج Microsoft Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md) - [Ollama](./md/01.Introduction/02/04.Ollama.md) - [أداة AI لـ VSCode (AITK)](./md/01.Introduction/02/05.AITK.md) - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md) - [Foundry المحلي](./md/01.Introduction/02/07.FoundryLocal.md) - استدلال عائلة فاي - [استدلال فاي على iOS](./md/01.Introduction/03/iOS_Inference.md) - [استدلال فاي على أندرويد](./md/01.Introduction/03/Android_Inference.md) - [استدلال فاي على Jetson](./md/01.Introduction/03/Jetson_Inference.md) - [استدلال فاي على كمبيوتر AI](./md/01.Introduction/03/AIPC_Inference.md) - [استدلال فاي بإطار عمل Apple MLX](./md/01.Introduction/03/MLX_Inference.md) - [استدلال فاي على الخادم المحلي](./md/01.Introduction/03/Local_Server_Inference.md) - [استدلال فاي على الخادم البعيد باستخدام أداة AI](./md/01.Introduction/03/Remote_Interence.md) - [استدلال فاي مع Rust](./md/01.Introduction/03/Rust_Inference.md) - [استدلال فاي--الرؤية محليًا](./md/01.Introduction/03/Vision_Inference.md) - [استدلال فاي مع Kaito AKS، حاويات Azure (الدعم الرسمي)](./md/01.Introduction/03/Kaito_Inference.md) - [تكميم عائلة فاي](./md/01.Introduction/04/QuantifyingPhi.md) - [تكميم Phi-3.5 / 4 باستخدام llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md) - [تكميم Phi-3.5 / 4 باستخدام امتدادات الذكاء الاصطناعي التوليدي لـ onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md) - [تكميم Phi-3.5 / 4 باستخدام Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md) - [تكميم Phi-3.5 / 4 باستخدام إطار عمل Apple MLX](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md) - تقييم فاي - [ذكاء اصطناعي مسؤول](./md/01.Introduction/05/ResponsibleAI.md) - [Microsoft Foundry للتقييم](./md/01.Introduction/05/AIFoundry.md) - [استخدام Promptflow للتقييم](./md/01.Introduction/05/Promptflow.md) - RAG مع Azure AI Search - [كيفية استخدام Phi-4-mini و Phi-4-multimodal(RAG) مع Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb) - أمثلة تطوير تطبيقات فاي - تطبيقات النص والدردشة - عينات Phi-4 - [📓] [الدردشة مع نموذج Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md) - [الدردشة مع نموذج Phi-4 ONNX محلي .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) - [تطبيق الدردشة .NET Console مع Phi-4 ONNX باستخدام Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) - عينات Phi-3 / 3.5 - [بوت دردشة محلي في المتصفح باستخدام Phi3، ONNX Runtime Web و WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat) - [دردشة OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md) - [نموذج متعدد - تفاعل Phi-3-mini مع OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md) - [MLFlow - إنشاء غلاف واستخدام Phi-3 مع MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md) - [تحسين النموذج - كيفية تحسين نموذج Phi-3-min لـ ONNX Runtime Web باستخدام Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3) - [تطبيق WinUI3 مع Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/) - [تطبيق WinUI3 متعدد النماذج مع ملاحظات مدعومة بالذكاء الاصطناعي](https://github.com/microsoft/ai-powered-notes-winui3-sample) - [الضبط الدقيق ودمج نماذج Phi-3 المخصصة مع Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md) - [الضبط الدقيق ودمج نماذج Phi-3 المخصصة مع Prompt flow في Microsoft Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md) - [تقييم نموذج Phi-3 / Phi-3.5 المضبوط بدقة في Microsoft Foundry مع التركيز على مبادئ الذكاء الاصطناعي المسؤول لشركة مايكروسوفت](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md) - [📓] [عينة توقع اللغة Phi-3.5-mini-instruct (صينية/إنجليزية)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb) - [بوت دردشة Phi-3.5-Instruct WebGPU RAG](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md) - [استخدام GPU في ويندوز لإنشاء حل Prompt flow مع Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md) - [استخدام Microsoft Phi-3.5 tflite لإنشاء تطبيق أندرويد](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md) - [مثال سؤال وجواب .NET باستخدام نموذج Phi-3 ONNX محلي باستخدام Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301) - [تطبيق دردشة Console .NET مع Semantic Kernel و Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302) - أمثلة SDK لبرمجيات استدلال Azure AI مبنية على الكود - عينات Phi-4 - [📓] [توليد كود المشروع باستخدام Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md) - عينات Phi-3 / 3.5 - [بناء مساعد دردشة GitHub الخاص بك لبرنامج Visual Studio Code مع عائلة Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md) - [إنشاء وكيل مساعد دردشة برنامج Visual Studio Code الخاص بك مع Phi-3.5 باستخدام نماذج GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md) - عينات التفكير المتقدم - عينات Phi-4 - [📓] [عينات Phi-4-mini-reasoning أو Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md) - [📓] [الضبط الدقيق لـ Phi-4-mini-reasoning مع Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [الضبط الدقيق لـ Phi-4-mini-reasoning مع Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Phi-4-mini-reasoning مع نماذج GitHub](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb) - [📓] [Phi-4-mini-reasoning مع نماذج Microsoft Foundry](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb) -
العروض التوضيحية - [عروض Phi-4-mini المقدمة على مساحات Hugging Face](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo) - [عروض Phi-4-multimodal المقدمة على مساحات Hugging Face](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo) - عينات الرؤية - عينات Phi-4 - [📓] [استخدام Phi-4-multimodal لقراءة الصور وتوليد الشيفرة](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) - عينات Phi-3 / 3.5 - [📓][نص إلى نص صورة Phi-3-vision](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html) - [📓][تضمين CLIP لإصدار Phi-3-vision](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [توضيح: تدوير Phi-3](https://github.com/jennifermarsman/PhiRecycling/) - [Phi-3-vision - مساعد لغة مرئي - مع Phi3-Vision و OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html) - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md) - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md) - [📓][عينة Phi-3.5 Vision متعددة الإطارات أو متعددة الصور](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb) - [نموذج ONNX محلي لـ Phi-3 Vision باستخدام Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303) - [نموذج ONNX محلي قائم على القائمة لـ Phi-3 Vision باستخدام Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304) - عينات الاستدلال والرؤية - Phi-4-Reasoning-Vision-15B - [📓] [استخدام Phi-4-Reasoning-Vision-15B لرصد عبور المشاة الخاطئ](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb) - [📓] [استخدام Phi-4-Reasoning-Vision-15B في الرياضيات](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb) - [📓] [استخدام Phi-4-Reasoning-Vision-15B لاكتشاف واجهة المستخدم](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb) - عينات الرياضيات - عينات Phi-4-Mini-Flash-Reasoning-Instruct [توضيح الرياضيات مع Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb) - عينات الصوت - عينات Phi-4 - [📓] [استخراج النصوص الصوتية باستخدام Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md) - [📓] [عينة صوتية Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb) - [📓] [عينة ترجمة الكلام Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb) - [تطبيق .NET لوحدة التحكم يستخدم Phi-4-multimodal لتحليل ملف صوتي وإنشاء النصوص](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) - عينات MoE - عينات Phi-3 / 3.5 - [📓] [نموذج Phi-3.5 خلطة الخبراء (MoEs) نموذج وسائل التواصل الاجتماعي](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb) - [📓] [بناء خط أنابيب التوليد المعزز بالاسترجاع (RAG) باستخدام NVIDIA NIM Phi-3 MOE، Azure AI Search، و LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb) - - عينات استدعاء الدالة - عينات Phi-4 🆕 - [📓] [استخدام استدعاء الدالة مع Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md) - [📓] [استخدام استدعاء الدالة لإنشاء وكلاء متعددين مع Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb) - [📓] [استخدام استدعاء الدالة مع Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb) - [📓] [استخدام استدعاء الدالة مع ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb) - عينات المزج متعدد الوسائط - عينات Phi-4 🆕 - [📓] [استخدام Phi-4-multimodal كصحفي تقني](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb) - [تطبيق .NET لوحدة التحكم يستخدم Phi-4-multimodal لتحليل الصور](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) - عينات ضبط النموذج - [سيناريوهات الضبط الدقيق](./md/03.FineTuning/FineTuning_Scenarios.md) - [الضبط الدقيق مقابل RAG](./md/03.FineTuning/FineTuning_vs_RAG.md) - [الضبط الدقيق لجعل Phi-3 خبيرًا صناعيًا](./md/03.FineTuning/LetPhi3gotoIndustriy.md) - [الضبط الدقيق لـ Phi-3 مع مجموعة أدوات AI لـ VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md) - [الضبط الدقيق لـ Phi-3 مع خدمة Azure Machine Learning](./md/03.FineTuning/Introduce_AzureML.md) - [الضبط الدقيق لـ Phi-3 مع Lora](./md/03.FineTuning/FineTuning_Lora.md) - [الضبط الدقيق لـ Phi-3 مع QLora](./md/03.FineTuning/FineTuning_Qlora.md) - [الضبط الدقيق لـ Phi-3 مع Microsoft Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md) - [الضبط الدقيق لـ Phi-3 مع Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md) - [الضبط الدقيق مع Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md) - [مختبر عملي للضبط الدقيق مع Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md) - [الضبط الدقيق لـ Phi-3-vision مع Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md) - [الضبط الدقيق لـ Phi-3 مع إطار عمل Apple MLX](./md/03.FineTuning/FineTuning_MLX.md) - [الضبط الدقيق لـ Phi-3-vision (الدعم الرسمي)](./md/03.FineTuning/FineTuning_Vision.md) - [الضبط الدقيق لـ Phi-3 مع Kaito AKS و Azure Containers (الدعم الرسمي)](./md/03.FineTuning/FineTuning_Kaito.md) - [الضبط الدقيق لـ Phi-3 و 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune) - المختبر العملي - [استكشاف النماذج المتطورة: نماذج اللغة الكبيرة، نماذج اللغة الصغيرة، التطوير المحلي والمزيد](https://github.com/microsoft/aitour-exploring-cutting-edge-models) - [فتح إمكانيات معالجة اللغة الطبيعية: الضبط الدقيق مع Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop) - أوراق بحثية أكاديمية ومنشورات - [الكتب الدراسية هي كل ما تحتاجه II: التقرير الفني phi-1.5](https://arxiv.org/abs/2309.05463) - [التقرير الفني لـ Phi-3: نموذج لغة عالي القدرات يعمل محليًا على هاتفك](https://arxiv.org/abs/2404.14219) - [التقرير الفني لـ Phi-4](https://arxiv.org/abs/2412.08905) - [التقرير الفني لـ Phi-4-Mini: نماذج لغوية متعددة الوسائط مدمجة وقوية عبر خليط من LoRAs](https://arxiv.org/abs/2503.01743) - [تحسين نماذج اللغة الصغيرة لاستدعاء الوظائف داخل المركبة](https://arxiv.org/abs/2501.02342) - [(لماذا PHI) الضبط الدقيق لـ PHI-3 للإجابة على أسئلة الاختيار من متعدد: المنهجية، النتائج، والتحديات](https://arxiv.org/abs/2501.01588) - [تقرير فني Phi-4-Reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [تقرير فني Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)
# كتاب طهي Phi: أمثلة عملية مع نماذج Phi من Microsoft

[![افتح واستخدم العينات في GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![افتح في حاويات التطوير](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![المساهمون على GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![المشاكل على GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![طلبات السحب على GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![طلبات السحب مرحب بها](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![المراقبون على GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![فروع GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![النجوم على GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![خادم Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi هي سلسلة من نماذج الذكاء الاصطناعي مفتوحة المصدر تم تطويرها بواسطة Microsoft.

Phi هو حاليًا أقوى وأكفأ نموذج لغة صغير (SLM) من حيث التكلفة، مع نتائج ممتازة في لغات متعددة، والتفكير المنطقي، وتوليد النص/الدردشة، والبرمجة، والصور، والصوت، وسيناريوهات أخرى.

يمكنك نشر Phi في السحابة أو على أجهزة الحافة، ويمكنك ببساطة بناء تطبيقات الذكاء الاصطناعي التوليدية مع قدرة حوسبة محدودة.

اتبع هذه الخطوات للبدء باستخدام هذه الموارد:
1. **انشئ نسخة من المستودع**: اضغط على [![فروع GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **انسخ المستودع**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**انضم إلى مجتمع Microsoft AI على Discord والتقِ بالخبراء والمطورين الآخرين**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/ar/cover.eb18d1b9605d754b.webp)

### 🌐 دعم متعدد اللغات

#### مدعوم عبر GitHub Action (آلي ومحدث دائمًا)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[العربية](./README.md) | [البنغالية](../bn/README.md) | [البلغارية](../bg/README.md) | [البورمية (ميانمار)](../my/README.md) | [الصينية المبسطة](../zh-CN/README.md) | [الصينية التقليدية (هونغ كونغ)](../zh-HK/README.md) | [الصينية التقليدية (ماكاو)](../zh-MO/README.md) | [الصينية التقليدية (تايوان)](../zh-TW/README.md) | [الكرواتية](../hr/README.md) | [التشيكية](../cs/README.md) | [الدنماركية](../da/README.md) | [الهولندية](../nl/README.md) | [الإستونية](../et/README.md) | [الفنلندية](../fi/README.md) | [الفرنسية](../fr/README.md) | [الألمانية](../de/README.md) | [اليونانية](../el/README.md) | [العبرية](../he/README.md) | [الهندية](../hi/README.md) | [الهنغارية](../hu/README.md) | [الإندونيسية](../id/README.md) | [الإيطالية](../it/README.md) | [اليابانية](../ja/README.md) | [الكانادا](../kn/README.md) | [الكورية](../ko/README.md) | [الليتوانية](../lt/README.md) | [المالية](../ms/README.md) | [المالايالامية](../ml/README.md) | [الماراثية](../mr/README.md) | [النيبالية](../ne/README.md) | [النيجيرية بيدجين](../pcm/README.md) | [النرويجية](../no/README.md) | [الفارسية (اللغة الفارسية)](../fa/README.md) | [البولندية](../pl/README.md) | [البرتغالية (البرازيل)](../pt-BR/README.md) | [البرتغالية (البرتغال)](../pt-PT/README.md) | [البنجابية (جورموخي)](../pa/README.md) | [الرومانية](../ro/README.md) | [الروسية](../ru/README.md) | [الصربية (السيريلية)](../sr/README.md) | [السلوفاكية](../sk/README.md) | [السلوفينية](../sl/README.md) | [الإسبانية](../es/README.md) | [السواحيلية](../sw/README.md) | [السويدية](../sv/README.md) | [التاغالوغ (الفلبينية)](../tl/README.md) | [التاميلية](../ta/README.md) | [التيلجو](../te/README.md) | [التايلاندية](../th/README.md) | [التركية](../tr/README.md) | [الأوكرانية](../uk/README.md) | [الأردية](../ur/README.md) | [الفيتنامية](../vi/README.md)

> **هل تفضل الاستنساخ محليًا؟**
>
> يتضمن هذا المستودع أكثر من 50 ترجمة للغات مما يزيد بشكل كبير من حجم التنزيل. للاستنساخ بدون الترجمات، استخدم السحب البطيء:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (ويندوز):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> هذا يمنحك كل ما تحتاجه لإكمال الدورة مع تنزيل أسرع بكثير.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## جدول المحتويات

## استخدام نماذج Phi

### Phi على Microsoft Foundry

يمكنك تعلم كيفية استخدام Microsoft Phi وكيفية بناء حلول شاملة في أجهزتك المختلفة. لتجربة Phi بنفسك، ابدأ بالتعامل مع النماذج وتخصيص Phi لسيناريوهاتك باستخدام [كتالوج نماذج الذكاء الاصطناعي Azure من Microsoft Foundry](https://aka.ms/phi3-azure-ai) يمكنك معرفة المزيد في البداية مع [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**ملعب التجربة**
لكل نموذج ملعب مخصص لاختباره [Azure AI Playground](https://aka.ms/try-phi3).

### Phi على نماذج GitHub

يمكنك تعلم كيفية استخدام Microsoft Phi وكيفية بناء حلول شاملة في أجهزتك المختلفة. لتجربة Phi بنفسك، ابدأ بالتعامل مع النموذج وتخصيص Phi لسيناريوهاتك باستخدام [كتالوج نماذج GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) يمكنك معرفة المزيد في البداية مع [كتالوج نماذج GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md)

**ملعب التجربة**
لكل نموذج يوجد ملعب مخصص [لاختبار النموذج](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi على Hugging Face

يمكنك أيضًا العثور على النموذج على [Hugging Face](https://huggingface.co/microsoft)

**ملعب التجربة**
 [ملعب Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 دورات أخرى

فريقنا ينتج دورات أخرى! تفقد:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j للمبتدئين](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js للمبتدئين](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain للمبتدئين](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD للمبتدئين](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![الذكاء الاصطناعي على الحافة للمبتدئين](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP للمبتدئين](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![وكلاء الذكاء الاصطناعي للمبتدئين](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### سلسلة الذكاء الاصطناعي التوليدي
[![الذكاء الاصطناعي التوليدي للمبتدئين](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![الذكاء الاصطناعي التوليدي (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![الذكاء الاصطناعي التوليدي (جافا)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![الذكاء الاصطناعي التوليدي (جافا سكريبت)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### التعليم الأساسي
[![التعلم الآلي للمبتدئين](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![علوم البيانات للمبتدئين](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![الذكاء الاصطناعي للمبتدئين](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![الأمن السيبراني للمبتدئين](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![تطوير الويب للمبتدئين](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![إنترنت الأشياء للمبتدئين](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![تطوير الواقع الممتد للمبتدئين](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### سلسلة كوبيلوت
[![كوبيلوت للبرمجة المزدوجة باستخدام الذكاء الاصطناعي](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![كوبيلوت لـ C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![مغامرات كوبيلوت](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## الذكاء الاصطناعي المسؤول

تلتزم مايكروسوفت بمساعدة عملائنا على استخدام منتجات الذكاء الاصطناعي لدينا بمسؤولية، ومشاركة تجاربنا، وبناء شراكات قائمة على الثقة من خلال أدوات مثل ملاحظات الشفافية وتقييمات الأثر. يمكن العثور على العديد من هذه الموارد على [https://aka.ms/RAI](https://aka.ms/RAI).
 تستند مقاربة مايكروسوفت للذكاء الاصطناعي المسؤول إلى مبادئ الذكاء الاصطناعي لدينا التي تشمل العدالة والموثوقية والسلامة والخصوصية والأمان والشمولية والشفافية والمساءلة.

النماذج الكبيرة للنصوص الطبيعية والصور والكلام - مثل تلك المستخدمة في هذا المثال - قد تتصرف بطرق غير عادلة أو غير موثوقة أو مسيئة، مما قد يتسبب في أضرار. يرجى الاطلاع على [ملاحظة الشفافية لخدمة Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) لتكون على دراية بالمخاطر والقيود.

النهج الموصى به للتخفيف من هذه المخاطر هو تضمين نظام أمان في هيكليتك يمكنه اكتشاف السلوك الضار ومنعه. يوفر [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) طبقة حماية مستقلة، قادرة على اكتشاف المحتوى الضار الذي ينشئه المستخدمون أو الذكاء الاصطناعي في التطبيقات والخدمات. يتضمن Azure AI Content Safety واجهات برمجة تطبيقات للنصوص والصور تتيح لك اكتشاف المواد الضارة. ضمن Microsoft Foundry، تتيح خدمة Content Safety لك عرض المحتوى الضار واستكشافه وتجربة نموذجية من الشفرة لاكتشاف المحتوى الضار بمختلف الأنماط. يرشدك الوثائق التالية [الدليل السريع](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) خلال كيفية إرسال الطلبات إلى الخدمة.

جانب آخر يجب وضعه في الاعتبار هو أداء التطبيق ككل. في التطبيقات متعددة الأنماط ومتعددة النماذج، نعني بالأداء أن النظام يعمل كما تتوقع أنت ومستخدموك، بما في ذلك عدم توليد مخرجات ضارة. من المهم تقييم أداء تطبيقك الكلي باستخدام [مقاييس الأداء والجودة ومقاييس المخاطر والسلامة](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). لديك أيضًا القدرة على إنشاء وتقييم باستخدام [مقَيّمين مخصصين](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

يمكنك تقييم تطبيق الذكاء الاصطناعي الخاص بك في بيئة التطوير الخاصة بك باستخدام [مجموعة تطوير برمجيات تقييم Azure AI](https://microsoft.github.io/promptflow/index.html). وفقًا لبيانات اختبار أو هدف معين، يتم قياس مخرجات تطبيق الذكاء الاصطناعي التوليدي لديك كمياً بواسطة المقَيّمين المدمجين أو المقَيّمين المخصصين من اختيارك. للبدء باستخدام azure ai evaluation sdk لتقييم نظامك، يمكنك اتباع [الدليل السريع](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). بمجرد تنفيذ تشغيل التقييم، يمكنك [عرض النتائج في Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## العلامات التجارية

قد يحتوي هذا المشروع على علامات تجارية أو شعارات لمشاريع أو منتجات أو خدمات. يخضع الاستخدام المصرح به لعلامات مايكروسوفت التجارية أو الشعارات إلى و يجب أن يتبع [إرشادات علامة مايكروسوفت التجارية والهوية البصرية](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
يجب ألا يسبب استخدام علامات مايكروسوفت التجارية أو الشعارات في نسخ معدلة من هذا المشروع أي ارتباك أو يوحي برعاية من مايكروسوفت. يخضع أي استخدام لعلامات تجارية أو شعارات لأطراف ثالثة لسياسات تلك الأطراف.

## الحصول على المساعدة

إذا واجهت صعوبة أو كان لديك أي أسئلة حول بناء تطبيقات الذكاء الاصطناعي، انضم إلى:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

إذا كان لديك تعليقات على المنتج أو أخطاء أثناء البناء، قم بزيارة:

[![منتدى مطوري Microsoft Foundry](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يُرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للمعلومات الحساسة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->