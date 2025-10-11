<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a73c59eecd7ad4ec494fd4333a29e208",
  "translation_date": "2025-10-11T10:34:49+00:00",
  "source_file": "README.md",
  "language_code": "ur"
}
-->
# Phi کُک بُک: Microsoft کے Phi ماڈلز کے ساتھ عملی مثالیں

[![GitHub Codespaces میں نمونے کھولیں اور استعمال کریں](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers میں کھولیں](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi Microsoft کے تیار کردہ اوپن سورس AI ماڈلز کی ایک سیریز ہے۔

Phi اس وقت سب سے طاقتور اور کم خرچ چھوٹا زبان ماڈل (SLM) ہے، جو مختلف زبانوں، استدلال، متن/چیٹ جنریشن، کوڈنگ، تصاویر، آڈیو اور دیگر منظرناموں میں بہترین کارکردگی فراہم کرتا ہے۔

آپ Phi کو کلاؤڈ یا ایج ڈیوائسز پر تعینات کر سکتے ہیں، اور محدود کمپیوٹنگ پاور کے ساتھ آسانی سے جنریٹو AI ایپلیکیشنز بنا سکتے ہیں۔

ان وسائل کو استعمال کرنے کے لیے درج ذیل مراحل پر عمل کریں:
1. **ریپوزیٹری کو فورک کریں**: کلک کریں [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **ریپوزیٹری کو کلون کریں**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord کمیونٹی میں شامل ہوں اور ماہرین اور دیگر ڈویلپرز سے ملاقات کریں**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 کثیر زبان کی حمایت

#### GitHub Action کے ذریعے سپورٹ (خودکار اور ہمیشہ اپ ڈیٹ)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[عربی](../ar/README.md) | [بنگالی](../bn/README.md) | [بلغاریائی](../bg/README.md) | [برمی (میانمار)](../my/README.md) | [چینی (سادہ)](../zh/README.md) | [چینی (روایتی، ہانگ کانگ)](../hk/README.md) | [چینی (روایتی، مکاؤ)](../mo/README.md) | [چینی (روایتی، تائیوان)](../tw/README.md) | [کروشین](../hr/README.md) | [چیک](../cs/README.md) | [ڈینش](../da/README.md) | [ڈچ](../nl/README.md) | [ایسٹونین](../et/README.md) | [فنش](../fi/README.md) | [فرانسیسی](../fr/README.md) | [جرمن](../de/README.md) | [یونانی](../el/README.md) | [عبرانی](../he/README.md) | [ہندی](../hi/README.md) | [ہنگریائی](../hu/README.md) | [انڈونیشیائی](../id/README.md) | [اطالوی](../it/README.md) | [جاپانی](../ja/README.md) | [کوریائی](../ko/README.md) | [لتھوانیائی](../lt/README.md) | [ملائی](../ms/README.md) | [مراٹھی](../mr/README.md) | [نیپالی](../ne/README.md) | [نارویجین](../no/README.md) | [فارسی (ایرانی)](../fa/README.md) | [پولش](../pl/README.md) | [پرتگالی (برازیل)](../br/README.md) | [پرتگالی (پرتگال)](../pt/README.md) | [پنجابی (گرمکھی)](../pa/README.md) | [رومانیائی](../ro/README.md) | [روسی](../ru/README.md) | [سربیائی (سیریلک)](../sr/README.md) | [سلوواک](../sk/README.md) | [سلووینیائی](../sl/README.md) | [ہسپانوی](../es/README.md) | [سواحلی](../sw/README.md) | [سویڈش](../sv/README.md) | [ٹیگالوگ (فلپائنی)](../tl/README.md) | [تمل](../ta/README.md) | [تھائی](../th/README.md) | [ترکی](../tr/README.md) | [یوکرینیائی](../uk/README.md) | [اردو](./README.md) | [ویتنامی](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## مواد کی فہرست

- تعارف
  - [Phi فیملی میں خوش آمدید](./md/01.Introduction/01/01.PhiFamily.md)
  - [اپنا ماحول ترتیب دینا](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [اہم ٹیکنالوجیز کو سمجھنا](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi ماڈلز کے لیے AI سیفٹی](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ہارڈویئر سپورٹ](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi ماڈلز اور پلیٹ فارمز پر دستیابی](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai اور Phi کا استعمال](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace ماڈلز](https://github.com/marketplace/models)
  - [Azure AI ماڈل کیٹلاگ](https://ai.azure.com)

- مختلف ماحول میں Phi کا انفرنس
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub ماڈلز](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry ماڈل کیٹلاگ](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi فیملی کا انفرنس
    - [iOS میں Phi کا انفرنس](./md/01.Introduction/03/iOS_Inference.md)
    - [Android میں Phi کا انفرنس](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson میں Phi کا انفرنس](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC میں Phi کا انفرنس](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework کے ساتھ Phi کا انفرنس](./md/01.Introduction/03/MLX_Inference.md)
    - [لوکل سرور میں Phi کا انفرنس](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit کے ذریعے ریموٹ سرور میں Phi کا انفرنس](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust کے ساتھ Phi کا انفرنس](./md/01.Introduction/03/Rust_Inference.md)
    - [لوکل میں Phi--Vision کا انفرنس](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS، Azure Containers کے ساتھ Phi کا انفرنس (سرکاری سپورٹ)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi فیملی کی مقدار بندی](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp کے ذریعے Phi-3.5 / 4 کی مقدار بندی](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Generative AI extensions for onnxruntime کے ذریعے Phi-3.5 / 4 کی مقدار بندی](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO کے ذریعے Phi-3.5 / 4 کی مقدار بندی](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework کے ذریعے Phi-3.5 / 4 کی مقدار بندی](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi کا جائزہ
    - [ذمہ دار AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [جائزے کے لیے Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [جائزے کے لیے Promptflow کا استعمال](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search کے ساتھ RAG
    - [Azure AI Search کے ساتھ Phi-4-mini اور Phi-4-multimodal (RAG) کا استعمال کیسے کریں](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi ایپلیکیشن ڈیولپمنٹ کے نمونے
  - متن اور چیٹ ایپلیکیشنز
    - Phi-4 نمونے 🆕
      - [📓] [Phi-4-mini ONNX ماڈل کے ساتھ چیٹ کریں](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 لوکل ONNX ماڈل .NET کے ساتھ چیٹ کریں](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Phi-4 ONNX کے ساتھ .NET کنسول ایپ چیٹ، Semantic Kernel کا استعمال کرتے ہوئے](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 نمونے
      - [Phi3، ONNX Runtime Web اور WebGPU کا استعمال کرتے ہوئے براؤزر میں لوکل چیٹ بوٹ](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino چیٹ](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [ملٹی ماڈل - Phi-3-mini اور OpenAI Whisper کے ساتھ انٹرایکٹو](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ایک ریپر بنانا اور MLFlow کے ساتھ Phi-3 کا استعمال](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [ماڈل کی اصلاح - Olive کے ساتھ ONNX Runtime Web کے لیے Phi-3-min ماڈل کو کیسے بہتر بنائیں](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [WinUI3 ایپ کے ساتھ Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [WinUI3 ملٹی ماڈل AI پاورڈ نوٹس ایپ سیمپل](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Phi-3 ماڈلز کو Fine-tune کریں اور Prompt flow کے ساتھ انٹیگریٹ کریں](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Azure AI Foundry میں Phi-3 ماڈلز کو Fine-tune کریں اور Prompt flow کے ساتھ انٹیگریٹ کریں](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Azure AI Foundry میں Fine-tuned Phi-3 / Phi-3.5 ماڈل کا جائزہ لیں، Microsoft کے Responsible AI اصولوں پر توجہ مرکوز کرتے ہوئے](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct لینگویج پریڈکشن سیمپل (چینی/انگریزی)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG چیٹ بوٹ](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU کا استعمال کرتے ہوئے Phi-3.5-Instruct ONNX کے ساتھ Prompt flow حل بنائیں](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tflite کا استعمال کرتے ہوئے اینڈرائیڈ ایپ بنائیں](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Q&A .NET مثال، Microsoft.ML.OnnxRuntime کے ذریعے لوکل ONNX Phi-3 ماڈل کا استعمال کرتے ہوئے](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Semantic Kernel اور Phi-3 کے ساتھ کنسول چیٹ .NET ایپ](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK کوڈ پر مبنی سیمپلز  
  - Phi-4 سیمپلز 🆕  
    - [📓] [Phi-4-multimodal کا استعمال کرتے ہوئے پروجیکٹ کوڈ جنریٹ کریں](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Phi-3 / 3.5 سیمپلز  
    - [Microsoft Phi-3 فیملی کے ساتھ اپنا Visual Studio Code GitHub Copilot چیٹ بنائیں](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [Phi-3.5 کے ساتھ اپنا Visual Studio Code چیٹ Copilot ایجنٹ بنائیں، GitHub ماڈلز کے ذریعے](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- ایڈوانسڈ ریزننگ سیمپلز  
  - Phi-4 سیمپلز 🆕  
    - [📓] [Phi-4-mini-reasoning یا Phi-4-reasoning سیمپلز](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Microsoft Olive کے ساتھ Phi-4-mini-reasoning کو Fine-tune کریں](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Apple MLX کے ساتھ Phi-4-mini-reasoning کو Fine-tune کریں](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [GitHub ماڈلز کے ساتھ Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Azure AI Foundry ماڈلز کے ساتھ Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- ڈیموز  
    - [Phi-4-mini ڈیموز، Hugging Face Spaces پر ہوسٹ کیے گئے](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Phi-4-multimodal ڈیموز، Hugging Face Spaces پر ہوسٹ کیے گئے](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- وژن سیمپلز  
  - Phi-4 سیمپلز 🆕  
    - [📓] [Phi-4-multimodal کا استعمال کرتے ہوئے تصاویر پڑھیں اور کوڈ جنریٹ کریں](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Phi-3 / 3.5 سیمپلز  
    - [📓][Phi-3-vision-تصویر سے متن تک](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP ایمبیڈنگ](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [ڈیمو: Phi-3 ری سائیکلنگ](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - بصری زبان کا معاون - Phi3-Vision اور OpenVINO کے ساتھ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision ملٹی فریم یا ملٹی امیج سیمپل](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Phi-3 Vision لوکل ONNX ماڈل، Microsoft.ML.OnnxRuntime .NET کا استعمال کرتے ہوئے](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Menu-based Phi-3 Vision لوکل ONNX ماڈل، Microsoft.ML.OnnxRuntime .NET کا استعمال کرتے ہوئے](../../md/04.HOL/dotnet/src/LabsPhi304)  

- میتھ سیمپلز  
  - Phi-4-Mini-Flash-Reasoning-Instruct سیمپلز 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct کے ساتھ میتھ ڈیمو](../../md/02.Application/09.Math/MathDemo.ipynb)  

- آڈیو سیمپلز  
  - Phi-4 سیمپلز 🆕  
    - [📓] [Phi-4-multimodal کا استعمال کرتے ہوئے آڈیو ٹرانسکرپٹس نکالیں](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Phi-4-multimodal آڈیو سیمپل](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Phi-4-multimodal اسپیک ٹرانسلیشن سیمپل](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [.NET کنسول ایپلیکیشن، Phi-4-multimodal آڈیو کا استعمال کرتے ہوئے آڈیو فائل کا تجزیہ کریں اور ٹرانسکرپٹ جنریٹ کریں](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- MOE سیمپلز  
  - Phi-3 / 3.5 سیمپلز  
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) سوشل میڈیا سیمپل](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [NVIDIA NIM Phi-3 MOE، Azure AI Search، اور LlamaIndex کے ساتھ Retrieval-Augmented Generation (RAG) پائپ لائن بنائیں](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- فنکشن کالنگ سیمپلز  
  - Phi-4 سیمپلز 🆕  
    - [📓] [Phi-4-mini کے ساتھ فنکشن کالنگ کا استعمال کریں](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Phi-4-mini کے ساتھ ملٹی ایجنٹس بنانے کے لیے فنکشن کالنگ کا استعمال کریں](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Ollama کے ساتھ فنکشن کالنگ کا استعمال کریں](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [ONNX کے ساتھ فنکشن کالنگ کا استعمال کریں](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- ملٹی ماڈل مکسنگ سیمپلز  
  - Phi-4 سیمپلز 🆕  
    - [📓] [Phi-4-multimodal کا استعمال کرتے ہوئے ٹیکنالوجی جرنلسٹ کے طور پر کام کریں](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [.NET کنسول ایپلیکیشن، Phi-4-multimodal کا استعمال کرتے ہوئے تصاویر کا تجزیہ کریں](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Fine-tuning Phi سیمپلز  
  - [Fine-tuning کے منظرنامے](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [Fine-tuning بمقابلہ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Fine-tuning Phi-3 کو انڈسٹری ایکسپرٹ بننے دیں](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [Fine-tuning Phi-3، AI Toolkit for VS Code کے ساتھ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Fine-tuning Phi-3، Azure Machine Learning Service کے ساتھ](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Fine-tuning Phi-3، Lora کے ساتھ](./md/03.FineTuning/FineTuning_Lora.md)  
  - [Fine-tuning Phi-3، QLora کے ساتھ](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Fine-tuning Phi-3، Azure AI Foundry کے ساتھ](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Fine-tuning Phi-3، Azure ML CLI/SDK کے ساتھ](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Microsoft Olive کے ساتھ Fine-tuning](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Microsoft Olive Hands-On Lab کے ساتھ Fine-tuning](./md/03.FineTuning/olive-lab/readme.md)  
  - [Fine-tuning Phi-3-vision، Weights and Bias کے ساتھ](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Fine-tuning Phi-3، Apple MLX Framework کے ساتھ](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Fine-tuning Phi-3-vision (سرکاری سپورٹ)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Fine-Tuning Phi-3، Kaito AKS، Azure Containers (سرکاری سپورٹ)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Fine-Tuning Phi-3 اور 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- Hands-on Lab  
  - [جدید ماڈلز کی دریافت: LLMs، SLMs، لوکل ڈیولپمنٹ اور مزید](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [NLP کی صلاحیت کو ان لاک کریں: Microsoft Olive کے ساتھ Fine-Tuning](https://github.com/azure/Ignite_FineTuning_workshop)  

- تعلیمی تحقیقاتی مقالے اور اشاعتیں  
  - [Textbooks Are All You Need II: phi-1.5 تکنیکی رپورٹ](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 تکنیکی رپورٹ: ایک انتہائی قابل زبان ماڈل، آپ کے فون پر لوکل طور پر](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 تکنیکی رپورٹ](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini تکنیکی رپورٹ: Mixture-of-LoRAs کے ذریعے کمپیکٹ لیکن طاقتور ملٹی ماڈل زبان ماڈلز](https://arxiv.org/abs/2503.01743)  
  - [گاڑی کے اندر فنکشن کالنگ کے لیے چھوٹے زبان کے ماڈلز کو بہتر بنانا](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 کو ملٹیپل چوائس سوالات کے جواب دینے کے لیے فائن ٹیون کرنا: طریقہ کار، نتائج، اور چیلنجز](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning تکنیکی رپورٹ](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning تکنیکی رپورٹ](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi ماڈلز کا استعمال

### Azure AI Foundry پر Phi

آپ Microsoft Phi کا استعمال سیکھ سکتے ہیں اور مختلف ہارڈویئر ڈیوائسز میں E2E حل بنا سکتے ہیں۔ Phi کو خود تجربہ کرنے کے لیے، ماڈلز کے ساتھ کھیلنا شروع کریں اور اپنے منظرناموں کے لیے Phi کو حسب ضرورت بنائیں۔ [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) پر مزید معلومات حاصل کریں۔ مزید جاننے کے لیے [Azure AI Foundry کے ساتھ شروعات کریں](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)۔

**پلے گراؤنڈ**
ہر ماڈل کے لیے ایک مخصوص پلے گراؤنڈ موجود ہے تاکہ ماڈل کو آزمایا جا سکے [Azure AI Playground](https://aka.ms/try-phi3)۔

### GitHub ماڈلز پر Phi

آپ Microsoft Phi کا استعمال سیکھ سکتے ہیں اور مختلف ہارڈویئر ڈیوائسز میں E2E حل بنا سکتے ہیں۔ Phi کو خود تجربہ کرنے کے لیے، ماڈل کے ساتھ کھیلنا شروع کریں اور اپنے منظرناموں کے لیے Phi کو حسب ضرورت بنائیں۔ [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) پر مزید معلومات حاصل کریں۔ مزید جاننے کے لیے [GitHub Model Catalog کے ساتھ شروعات کریں](/md/02.QuickStart/GitHubModel_QuickStart.md)۔

**پلے گراؤنڈ**
ہر ماڈل کے لیے ایک مخصوص [پلے گراؤنڈ موجود ہے تاکہ ماڈل کو آزمایا جا سکے](/md/02.QuickStart/GitHubModel_QuickStart.md)۔

### Hugging Face پر Phi

آپ ماڈل کو [Hugging Face](https://huggingface.co/microsoft) پر بھی تلاش کر سکتے ہیں۔

**پلے گراؤنڈ**
[Hugging Chat پلے گراؤنڈ](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## ذمہ دار AI 

Microsoft اپنے صارفین کو AI مصنوعات کو ذمہ داری سے استعمال کرنے میں مدد دینے، اپنے تجربات شیئر کرنے، اور اعتماد پر مبنی شراکت داری قائم کرنے کے لیے پرعزم ہے۔ یہ سب کچھ شفافیت نوٹس اور اثرات کے جائزوں جیسے ٹولز کے ذریعے کیا جاتا ہے۔ ان وسائل میں سے بہت سے [https://aka.ms/RAI](https://aka.ms/RAI) پر دستیاب ہیں۔ Microsoft کا ذمہ دار AI کے لیے نقطہ نظر ہمارے AI اصولوں پر مبنی ہے، جن میں انصاف، قابل اعتماد اور حفاظت، پرائیویسی اور سیکیورٹی، شمولیت، شفافیت، اور جوابدہی شامل ہیں۔

بڑے پیمانے پر قدرتی زبان، تصویر، اور آواز کے ماڈلز - جیسے کہ اس نمونے میں استعمال کیے گئے ہیں - ممکنہ طور پر غیر منصفانہ، ناقابل اعتماد، یا توہین آمیز رویے کر سکتے ہیں، جو نقصان کا باعث بن سکتے ہیں۔ خطرات اور حدود کے بارے میں آگاہ ہونے کے لیے براہ کرم [Azure OpenAI سروس شفافیت نوٹس](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) سے مشورہ کریں۔

ان خطرات کو کم کرنے کے لیے تجویز کردہ طریقہ یہ ہے کہ آپ اپنی آرکیٹیکچر میں ایک حفاظتی نظام شامل کریں جو نقصان دہ رویے کا پتہ لگا سکے اور اسے روک سکے۔ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ایک آزاد حفاظتی پرت فراہم کرتا ہے، جو ایپلیکیشنز اور سروسز میں نقصان دہ صارف یا AI سے پیدا کردہ مواد کا پتہ لگا سکتا ہے۔ Azure AI Content Safety میں متن اور تصویر APIs شامل ہیں جو نقصان دہ مواد کا پتہ لگانے کی اجازت دیتے ہیں۔ Azure AI Foundry کے اندر، Content Safety سروس آپ کو مختلف طریقوں میں نقصان دہ مواد کا پتہ لگانے کے لیے نمونہ کوڈ دیکھنے، دریافت کرنے اور آزمانے کی اجازت دیتی ہے۔ درج ذیل [Quickstart دستاویزات](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) آپ کو سروس کے لیے درخواستیں کرنے کے طریقے سے رہنمائی کرتی ہیں۔

ایک اور پہلو جس پر غور کرنا ضروری ہے وہ مجموعی ایپلیکیشن کی کارکردگی ہے۔ ملٹی ماڈل اور ملٹی ماڈلز ایپلیکیشنز کے ساتھ، ہم کارکردگی کو اس طرح سمجھتے ہیں کہ نظام آپ اور آپ کے صارفین کی توقعات کے مطابق کام کرے، بشمول نقصان دہ نتائج پیدا نہ کرنا۔ اپنی مجموعی ایپلیکیشن کی کارکردگی کا جائزہ لینا ضروری ہے، جس کے لیے [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) کا استعمال کیا جا سکتا ہے۔ آپ اپنی مرضی کے مطابق [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) بھی بنا سکتے ہیں اور ان کا جائزہ لے سکتے ہیں۔

آپ اپنی AI ایپلیکیشن کو اپنے ترقیاتی ماحول میں [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) کا استعمال کرتے ہوئے جانچ سکتے ہیں۔ دیے گئے ٹیسٹ ڈیٹا سیٹ یا ہدف کے ساتھ، آپ کی جنریٹو AI ایپلیکیشن کی تخلیقات کو بلٹ ان ایویلیوٹرز یا آپ کی پسند کے کسٹم ایویلیوٹرز کے ذریعے مقداری طور پر ماپا جاتا ہے۔ Azure AI Evaluation SDK کے ساتھ اپنے نظام کا جائزہ لینے کے لیے شروعات کرنے کے لیے، آپ [Quickstart گائیڈ](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) پر عمل کر سکتے ہیں۔ ایک بار جب آپ ایویلیوایشن رن انجام دیتے ہیں، تو آپ [Azure AI Foundry میں نتائج کو بصری طور پر دیکھ سکتے ہیں](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)۔

## ٹریڈ مارکس

یہ پروجیکٹ ممکنہ طور پر پروجیکٹس، مصنوعات، یا خدمات کے لیے ٹریڈ مارکس یا لوگوز پر مشتمل ہو سکتا ہے۔ Microsoft کے ٹریڈ مارکس یا لوگوز کے مجاز استعمال کو [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) کے مطابق ہونا چاہیے اور ان کی پیروی کرنی چاہیے۔
Microsoft کے ٹریڈ مارکس یا لوگوز کا استعمال اس پروجیکٹ کے ترمیم شدہ ورژنز میں الجھن پیدا نہیں کرنا چاہیے یا Microsoft کی اسپانسرشپ کا اشارہ نہیں دینا چاہیے۔ کسی بھی تیسرے فریق کے ٹریڈ مارکس یا لوگوز کا استعمال ان تیسرے فریق کی پالیسیوں کے تابع ہے۔

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا خامیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔