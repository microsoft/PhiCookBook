<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef3a50368712b1a7483d0def1f70c490",
  "translation_date": "2025-12-21T10:11:01+00:00",
  "source_file": "README.md",
  "language_code": "ur"
}
-->
# Phi Cookbook: Hands-On Examples with Microsoft's Phi Models

[![GitHub Codespaces میں نمونے کھولیں اور استعمال کریں](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers میں کھولیں](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub شراکت کنندگان](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub مسائل](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub پل درخواستیں](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs خوش آمدید](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub واچرز](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub فورکس](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ستارے](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry ڈسکارڈ](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi مائیکروسافٹ کی جانب سے تیار کردہ اوپن سورس AI ماڈلز کی ایک سیریز ہے۔ 

Phi اس وقت سب سے طاقتور اور لاگت کے لحاظ سے موثر چھوٹے لینگویج ماڈلز (SLM) میں سے ایک ہے، جس نے کثیر زبان، منطق، متن/چیٹ جنریشن، کوڈنگ، تصاویر، آڈیو اور دیگر منظرناموں میں بہت اچھے بنچ مارکس دکھائے ہیں۔ 

آپ Phi کو کلاؤڈ یا ایج ڈیوائسز پر ڈیپلائے کر سکتے ہیں، اور محدود کمپیوٹنگ پاور کے ساتھ آساني سے جنریٹو AI ایپلیکیشنز بنا سکتے ہیں۔

شروع کرنے کے لیے ان وسائل کو استعمال کرنے کے لیے یہ اقدامات کریں:
1. **ریپوزیٹری فورک کریں**: کلک کریں [![GitHub فورکس](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **ریپوزیٹری کلون کریں**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord کمیونٹی میں شامل ہوں اور ماہرین اور دوسرے ڈویلپرز سے ملیں**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![سرورق](../../translated_images/cover.eb18d1b9605d754b.ur.png)

### 🌐 کثیر زبانوں کی حمایت

#### GitHub Action کے ذریعے معاون (خودکار اور ہمیشہ تازہ ترین)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[عربی](../ar/README.md) | [بنگالی](../bn/README.md) | [بلغاریائی](../bg/README.md) | [برمی (میانمار)](../my/README.md) | [چینی (سادہ)](../zh/README.md) | [چینی (روایتی، ہانگ کانگ)](../hk/README.md) | [چینی (روایتی، مکاؤ)](../mo/README.md) | [چینی (روایتی، تائیوان)](../tw/README.md) | [کروشین](../hr/README.md) | [چیک](../cs/README.md) | [ڈینش](../da/README.md) | [ڈچ](../nl/README.md) | [اسٹونین](../et/README.md) | [فنش](../fi/README.md) | [فرانسیسی](../fr/README.md) | [جرمن](../de/README.md) | [یونانی](../el/README.md) | [عبرانی](../he/README.md) | [ہندی](../hi/README.md) | [ہنگیرین](../hu/README.md) | [انڈونیشیائی](../id/README.md) | [اطالوی](../it/README.md) | [جاپانی](../ja/README.md) | [کنڑ](../kn/README.md) | [کوریائی](../ko/README.md) | [لیتھوینین](../lt/README.md) | [ملائی](../ms/README.md) | [مالایالم](../ml/README.md) | [مراٹھی](../mr/README.md) | [نیپالی](../ne/README.md) | [نائیجیریائی پیڈگن](../pcm/README.md) | [ناروِجی](../no/README.md) | [فارسی](../fa/README.md) | [پولش](../pl/README.md) | [پرتگالی (برازیل)](../br/README.md) | [پرتگالی (پرتگال)](../pt/README.md) | [پنجابی (گرمکھی)](../pa/README.md) | [رومانیائی](../ro/README.md) | [روسی](../ru/README.md) | [سربیائی (سیریلک)](../sr/README.md) | [سلاواک](../sk/README.md) | [سلووینیائی](../sl/README.md) | [ہسپانوی](../es/README.md) | [سواحلی](../sw/README.md) | [سویڈش](../sv/README.md) | [ٹاگالوک (فلپائنی)](../tl/README.md) | [تمل](../ta/README.md) | [تیلگو](../te/README.md) | [تھائی](../th/README.md) | [ترک](../tr/README.md) | [یوکرائنی](../uk/README.md) | [اردو](./README.md) | [ویتنامی](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## فہرستِ مضامین

- تعارف
  - [Phi خاندان میں خوش آمدید](./md/01.Introduction/01/01.PhiFamily.md)
  - [اپنے ماحول کی ترتیب](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [اہم ٹیکنالوجیز کو سمجھنا](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi ماڈلز کے لیے AI کی حفاظت](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ہارڈویئر کی حمایت](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi ماڈلز اور مختلف پلیٹ فارمز پر دستیابی](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai اور Phi کا استعمال](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace ماڈلز](https://github.com/marketplace/models)
  - [Azure AI ماڈل کیٹلاگ](https://ai.azure.com)

- مختلف ماحول میں Phi کی انفرنس
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub Models](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi خاندان میں انفرنس
    - [iOS میں Phi کی انفرنس](./md/01.Introduction/03/iOS_Inference.md)
    - [Android میں Phi کی انفرنس](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson میں Phi کی انفرنس](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC میں Phi کی انفرنس](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX فریم ورک کے ساتھ Phi کی انفرنس](./md/01.Introduction/03/MLX_Inference.md)
    - [مقامی سرور میں Phi کی انفرنس](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit استعمال کرتے ہوئے ریموٹ سرور میں Phi کی انفرنس](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust کے ساتھ Phi کی انفرنس](./md/01.Introduction/03/Rust_Inference.md)
    - [مقامی سطح پر Phi--Vision کی انفرنس](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (سرکاری حمایت) کے ساتھ Phi کی انفرنس](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi خاندان کا مقداری جائزہ](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp استعمال کرتے ہوئے Phi-3.5 / 4 کو کوانٹائز کرنا](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Generative AI extensions for onnxruntime استعمال کرتے ہوئے Phi-3.5 / 4 کو کوانٹائز کرنا](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO استعمال کرتے ہوئے Phi-3.5 / 4 کو کوانٹائز کرنا](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX فریم ورک استعمال کرتے ہوئے Phi-3.5 / 4 کو کوانٹائز کرنا](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi کا جائزہ
    - [ذمہ دار AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Evaluation کے لیے Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [جائزہ کے لیے Promptflow کا استعمال](./md/01.Introduction/05/Promptflow.md)
 
- RAG with Azure AI Search
    - [Phi-4-mini اور Phi-4-multimodal(RAG) کو Azure AI Search کے ساتھ کیسے استعمال کریں](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi ایپلیکیشن ڈویلپمنٹ نمونے
  - متن اور چیٹ ایپلیکیشنز
    - Phi-4 Samples 🆕
      - [📓] [Phi-4-mini ONNX ماڈل کے ساتھ چیٹ کریں](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 لوکل ONNX ماڈل کے ساتھ چیٹ .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel استعمال کرتے ہوئے Phi-4 ONNX کے ساتھ چیٹ .NET کنسول ایپ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 نمونے
      - [Phi3، ONNX Runtime Web اور WebGPU استعمال کرتے ہوئے براؤزر میں مقامی چیٹ بوٹ](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino چیٹ](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [ملٹی ماڈل - تفاعلی Phi-3-mini اور OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ایک ریپر بنانا اور MLFlow کے ساتھ Phi-3 کا استعمال](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [ماڈل کی اصلاح - ONNX Runtime Web کے لیے Phi-3-min ماڈل کو Olive کے ساتھ کیسے بہتر کریں](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 ایپ Phi-3 mini-4k-instruct-onnx کے ساتھ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 ملٹی ماڈل AI سے چلنے والی نوٹس ایپ کا نمونہ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [کسٹم Phi-3 ماڈلز کو Prompt flow کے ساتھ فائن ٹون اور ضم کریں](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry میں Prompt flow کے ساتھ کسٹم Phi-3 ماڈلز کو فائن ٹون اور ضم کریں](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Azure AI Foundry میں فائن ٹون شدہ Phi-3 / Phi-3.5 ماڈل کا جائزہ لیں، مائیکروسافٹ کے ذمہ دار AI اصولوں پر توجہ دیتے ہوئے](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct زبان پیشگوئی نمونہ (چینی/انگریزی)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG چیٹ بوٹ](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU استعمال کرتے ہوئے Phi-3.5-Instruct ONNX کے ساتھ Prompt flow حل بنانا](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite استعمال کرکے Android ایپ بنانا](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET مثال جس میں مقامی ONNX Phi-3 ماڈل Microsoft.ML.OnnxRuntime کے ذریعے استعمال ہوتا ہے](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Console chat .NET ایپ Semantic Kernel اور Phi-3 کے ساتھ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK Code Based Samples 
    - Phi-4 Samples 🆕
      - [📓] [Phi-4-multimodal استعمال کرکے پروجیکٹ کوڈ تیار کریں](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 Samples
      - [اپنا Visual Studio Code GitHub Copilot چیٹ Microsoft Phi-3 فیملی کے ساتھ بنائیں](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub Models کے ذریعے Phi-3.5 کے ساتھ اپنا Visual Studio Code Chat Copilot ایجنٹ بنائیں](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - اعلیٰ استدلال کے نمونے
    - Phi-4 Samples 🆕
      - [📓] [Phi-4-mini-reasoning یا Phi-4-reasoning نمونے](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive کے ساتھ Phi-4-mini-reasoning کو فائن ٹون کرنا](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX کے ساتھ Phi-4-mini-reasoning کو فائن ٹون کرنا](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub Models کے ساتھ Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry Models کے ساتھ Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - ڈیموز
      - [Phi-4-mini ڈیموز جو Hugging Face Spaces پر میزبانی ہیں](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal ڈیموز جو Hugging Face Spaces پر میزبانی ہیں](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - ویژن نمونے
    - Phi-4 Samples 🆕
      - [📓] [Phi-4-multimodal استعمال کرکے تصاویر پڑھیں اور کوڈ جنریٹ کریں](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 Samples
      -  [📓][Phi-3-vision - تصویر سے متن تک](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP ایمبیڈنگ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - بصری زبان اسسٹنٹ - Phi3-Vision اور OpenVINO کے ساتھ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision ملٹی فریم یا ملٹی امیج نمونہ](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision مقامی ONNX ماڈل Microsoft.ML.OnnxRuntime .NET استعمال کرتے ہوئے](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menu based Phi-3 Vision Local ONNX Model using the Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Math Samples
    -  Phi-4-Mini-Flash-Reasoning-Instruct Samples 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct کے ساتھ ریاضی کا ڈیمو](./md/02.Application/09.Math/MathDemo.ipynb)

  - Audio Samples
    - Phi-4 Samples 🆕
      - [📓] [Phi-4-multimodal استعمال کرکے آڈیو ٹرانسکرپٹس نکالنا](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal آڈیو نمونہ](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal تقریر ترجمہ نمونہ](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET کنسول ایپلیکیشن جو Phi-4-multimodal آڈیو استعمال کرتی ہے تاکہ آڈیو فائل کا تجزیہ کرے اور ٹرانسکرپٹ تیار کرے](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE Samples
    - Phi-3 / 3.5 Samples
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) سوشل میڈیا نمونہ](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE، Azure AI Search، اور LlamaIndex کے ساتھ Retrieval-Augmented Generation (RAG) پائپ لائن بنانا](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - فنکشن کالنگ نمونے
    - Phi-4 Samples 🆕
      -  [📓] [Phi-4-mini کے ساتھ فنکشن کالنگ استعمال کرنا](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini کے ساتھ فنکشن کالنگ استعمال کرکے ملٹی ایجنٹس بنانا](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama کے ساتھ فنکشن کالنگ استعمال کرنا](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX کے ساتھ فنکشن کالنگ استعمال کرنا](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - ملٹی موڈل مکسنگ نمونے
    - Phi-4 Samples 🆕
      -  [📓] [Phi-4-multimodal کو بطور ٹیکنالوجی جرنلسٹ استعمال کرنا](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET کنسول ایپلیکیشن جو تصاویر کا تجزیہ کرنے کے لئے Phi-4-multimodal استعمال کرتی ہے](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi ماڈلز کی فائن ٹوننگ
  - [فائن ٹوننگ کے منظرنامے](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [فائن ٹوننگ بمقابلہ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [فائن ٹوننگ: Phi-3 کو صنعت کا ماہر بننے دیں](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [AI Toolkit for VS Code کے ساتھ Phi-3 کی فائن ٹوننگ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service کے ساتھ Phi-3 کی فائن ٹوننگ](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora کے ساتھ Phi-3 کی فائن ٹوننگ](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora کے ساتھ Phi-3 کی فائن ٹوننگ](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry کے ساتھ Phi-3 کی فائن ٹوننگ](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK کے ساتھ Phi-3 کی فائن ٹوننگ](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive کے ساتھ فائن ٹوننگ](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive ہینڈز آن لیب کے ساتھ فائن ٹوننگ](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias کے ساتھ Phi-3-vision کی فائن ٹوننگ](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework کے ساتھ Phi-3 کی فائن ٹوننگ](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision کی فائن ٹوننگ (سرکاری سپورٹ)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS , Azure Containers کے ساتھ Phi-3 کی فائن ٹوننگ(official Support)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 اور 3.5 Vision کی فائن ٹوننگ](https://github.com/2U1/Phi3-Vision-Finetune)

- ہینڈز آن لیب
  - [جدید ترین ماڈلز کی تلاش: LLMs، SLMs، لوکل ڈیولپمنٹ اور مزید](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP کی صلاحیت کو کھولنا: Microsoft Olive کے ساتھ فائن ٹوننگ](https://github.com/azure/Ignite_FineTuning_workshop)

- اکیڈمک ریسرچ پیپرز اور اشاعتیں
  - [Textbooks Are All You Need II: phi-1.5 تکنیکی رپورٹ](https://arxiv.org/abs/2309.05463)
  - [Phi-3 تکنیکی رپورٹ: آپ کے فون پر مقامی طور پر ایک انتہائی قابل زبان ماڈل](https://arxiv.org/abs/2404.14219)
  - [Phi-4 تکنیکی رپورٹ](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini تکنیکی رپورٹ: Mixture-of-LoRAs کے ذریعے کمپیکٹ مگر طاقتور ملٹی ماڈل زبان کے ماڈلز](https://arxiv.org/abs/2503.01743)
  - [گاڑی میں فنکشن کالنگ کے لیے چھوٹے زبان ماڈلز کی اصلاح](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 کی فائن-ٹیوننگ برائے کثیر الانتخابی سوالات کے جواب: طریقہ کار، نتائج، اور چیلنجز](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning تکنیکی رپورٹ](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning تکنیکی رپورٹ](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi ماڈلز کا استعمال

### Azure AI Foundry میں Phi

آپ سیکھ سکتے ہیں کہ Microsoft Phi کا استعمال کیسے کریں اور اپنے مختلف ہارڈویئر ڈیوائسز میں E2E حل کیسے بنائیں۔ Phi کو خود تجربہ کرنے کے لیے، ماڈلز کے ساتھ کھیلنا شروع کریں اور اپنے منظرناموں کے لیے Phi کو حسبِ منشاء بنائیں، استعمال کرتے ہوئے [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) آپ [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) کے ساتھ شروعات کرنے کے بارے میں مزید جان سکتے ہیں۔

**پلے گراؤنڈ**
ہر ماڈل کے پاس ماڈل کی جانچ کے لیے ایک مخصوص پلے گراؤنڈ موجود ہے [Azure AI پلے گراؤنڈ](https://aka.ms/try-phi3).

### GitHub Models پر Phi

آپ سیکھ سکتے ہیں کہ Microsoft Phi کا استعمال کیسے کریں اور اپنے مختلف ہارڈویئر ڈیوائسز میں E2E حل کیسے بنائیں۔ Phi کو خود تجربہ کرنے کے لیے، ماڈل کے ساتھ کھیلنا شروع کریں اور اپنے منظرناموں کے لیے Phi کو حسبِ منشاء بنائیں، استعمال کرتے ہوئے [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) آپ [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) کے ساتھ شروعات کرنے کے بارے میں مزید جان سکتے ہیں

**پلے گراؤنڈ**
ہر ماڈل کا ایک مخصوص [ماڈل کی جانچ کے لیے پلے گراؤنڈ](/md/02.QuickStart/GitHubModel_QuickStart.md) ہوتا ہے۔

### Hugging Face پر Phi

آپ ماڈل کو [Hugging Face](https://huggingface.co/microsoft) پر بھی پا سکتے ہیں

**پلے گراؤنڈ**
 [Hugging Chat پلے گراؤنڈ](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 دیگر کورسز

ہماری ٹیم دیگر کورسز بھی تیار کرتی ہے! دیکھیں:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j برائے مبتدی](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js برائے مبتدی](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD برائے مبتدی](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI برائے مبتدی](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP برائے مبتدی](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI ایجنٹس برائے مبتدی](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI سیریز
[![Generative AI برائے مبتدی](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### بنیادی سیکھنے
[![ML برائے مبتدی](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science برائے مبتدی](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI برائے مبتدی](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![سائبر سیکیورٹی برائے مبتدی](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev برائے مبتدی](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT برائے مبتدی](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development برائے مبتدی](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot سیریز
[![Copilot برائے AI جوڑی پروگرامنگ](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot برائے C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot ایڈونچر](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## ذمہ دار AI 

Microsoft پرعزم ہے کہ وہ اپنے صارفین کو ہمارے AI مصنوعات کا ذمہ دارانہ استعمال کرنے میں مدد دے، اپنے تجربات شیئر کرے، اور Transparency Notes اور Impact Assessments جیسے اوزاروں کے ذریعے اعتماد پر مبنی شراکت داری قائم کرے۔ ان میں سے بہت سے وسائل [https://aka.ms/RAI](https://aka.ms/RAI) پر دستیاب ہیں۔
Microsoft کا ذمہ دار AI کا طریقہ کار ہمارے AI اصولوں پر مبنی ہے: انصاف، قابلِ اعتمادیت اور حفاظت، رازداری اور سیکیورٹی، شمولیت، شفافیت، اور جوابدہی۔

بڑے پیمانے پر قدرتی زبان، امیج، اور اسپِیچ ماڈلز — جیسا کہ اس نمونے میں استعمال ہونے والے ماڈلز — ممکنہ طور پر ایسے رویے اختیار کر سکتے ہیں جو ناعادلانہ، غیر قابلِ اعتماد، یا توہین آمیز ہوں، اور نتیجتاً نقصان پہنچا سکتے ہیں۔ خطرات اور حدود سے آگاہی کے لیے براہِ کرم [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ملاحظہ کریں۔

ان خطرات کو کم کرنے کے لیے تجویز کردہ طریقہ یہ ہے کہ اپنی فن تعمیر میں ایک حفاظتی نظام شامل کریں جو مضر رویے کا پتہ لگا سکے اور اسے روکے۔ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ایک آزاد حفاظتی پرت فراہم کرتا ہے، جو ایپلیکیشنز اور سروسز میں صارف-جنریٹڈ اور AI-جنریٹڈ مضر مواد کا پتہ لگا سکتا ہے۔ Azure AI Content Safety میں ٹیکسٹ اور امیج APIs شامل ہیں جو آپ کو نقصان دہ مواد کی شناخت کرنے کی اجازت دیتی ہیں۔ Azure AI Foundry کے اندر، Content Safety سروس آپ کو مختلف موڈیلیٹیز میں مضر مواد کا پتہ لگانے کے لیے نمونہ کوڈ دیکھنے، دریافت کرنے اور آزمانے کی سہولت دیتی ہے۔ درج ذیل [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) آپ کو سروس کو درخواستیں بھیجنے کے عمل میں رہنمائی فراہم کرتی ہے۔

ایک اور پہلو جسے مدِ نظر رکھنا ضروری ہے وہ مجموعی ایپلیکیشن کارکردگی ہے۔ ملٹی موڈل اور ملٹی ماڈل ایپلیکیشنز کے ساتھ، ہم کارکردگی سے مراد یہ لیتے ہیں کہ سسٹم ویسا ہی کام کرے جیسا آپ اور آپ کے صارفین توقع رکھتے ہیں، بشمول نقصان دہ آؤٹ پٹس پیدا نہ کرنا۔ اپنے مجموعی ایپلیکیشن کی کارکردگی کا اندازہ لگانے کے لیے [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) استعمال کرنا اہم ہے۔ آپ کے پاس [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) کے ساتھ تخلیق اور تشخیص کرنے کی صلاحیت بھی موجود ہے۔

آپ اپنے ڈویلپمنٹ ماحول میں [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) استعمال کرتے ہوئے اپنے AI اپلیکیشن کا جائزہ لے سکتے ہیں۔ چاہے آپ کے پاس ٹیسٹ ڈیٹاسیٹ ہو یا کوئی ہدف، آپ کی جنریٹو AI ایپلیکیشن کی جنریشنز کو بلٹ اِن ایویلیو ایٹرز یا آپ کے منتخب کردہ کسٹم ایویلیو ایٹرز کے ذریعے مقداری طور پر ماپا جاتا ہے۔ اپنے سسٹم کا جائزہ لینے کے لیے azure ai evaluation sdk کے ساتھ شروعات کرنے کے لیے، آپ [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) پر عمل کر سکتے ہیں۔ ایک بار جب آپ ایک ایویلیوایشن رَن انجام دیتے ہیں، تو آپ [Azure AI Foundry میں نتائج کو بصری شکل میں دیکھ سکتے ہیں](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)。 

## ٹریڈ مارکس
یہ پروجیکٹ منصوبوں، مصنوعات، یا خدمات کے لیے ٹریڈ مارکس یا لوگوز پر مشتمل ہو سکتا ہے۔ مائیکروسافٹ کے ٹریڈ مارکس یا لوگوز کے مجاز استعمال کا انحصار ان کے قواعد و ضوابط پر ہے اور اس کی پابندی ضروری ہے ([مائیکروسافٹ کے ٹریڈ مارک اور برانڈ رہنما اصول](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)).
اس پروجیکٹ کے ترمیم شدہ ورژنز میں مائیکروسافٹ کے ٹریڈ مارکس یا لوگوز کے استعمال سے الجھن پیدا نہیں ہونی چاہیے اور نہ ہی یہ مائیکروسافٹ کی اسپانسرشپ کا تاثر دے۔ کسی بھی تیسری پارٹی کے ٹریڈ مارکس یا لوگوز کا استعمال متعلقہ فریق کی پالیسیوں کے تابع ہے۔

## مدد حاصل کریں

اگر آپ پھنس جائیں یا AI ایپس بنانے کے بارے میں آپ کے کوئی سوالات ہوں تو شامل ہوں:

[![Azure AI Foundry ڈسکارڈ](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

اگر آپ کے پاس پروڈکٹ کے بارے میں تاثرات ہیں یا بنانے کے دوران کوئی غلطی پیش آئے تو ملاحظہ کریں:

[![Azure AI Foundry ڈیولپر فورم](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
اخطاریہ:
یہ دستاویز مصنوعی ذہانت پر مبنی ترجمہ سروس Co-op Translator (https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہِ کرم نوٹ کریں کہ خودکار تراجم میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مادری زبان میں معتبر ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تعبیر کے لیے ہم ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->