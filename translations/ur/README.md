<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "43d47725683976a8f4f74656848bad45",
  "translation_date": "2025-05-07T13:01:57+00:00",
  "source_file": "README.md",
  "language_code": "ur"
}
-->
# Phi Cookbook: Microsoft کے Phi ماڈلز کے ساتھ عملی مثالیں

[![GitHub Codespaces میں نمونے کھولیں اور استعمال کریں](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![Dev Containers میں کھولیں](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi مائیکروسافٹ کی طرف سے تیار کردہ اوپن سورس AI ماڈلز کی ایک سیریز ہے۔

Phi اس وقت سب سے طاقتور اور کم قیمت چھوٹے زبان کے ماڈل (SLM) میں سے ہے، جو متعدد زبانوں، منطق، متن/چیٹ کی تخلیق، کوڈنگ، تصاویر، آڈیو اور دیگر حالات میں بہت اچھے بنچ مارکس رکھتا ہے۔

آپ Phi کو کلاؤڈ یا ایج ڈیوائسز پر تعینات کر سکتے ہیں، اور محدود کمپیوٹنگ پاور کے ساتھ آسانی سے تخلیقی AI ایپلیکیشنز بنا سکتے ہیں۔

ان وسائل کو استعمال شروع کرنے کے لیے یہ اقدامات کریں:  
1. **ریپوزیٹری کو فورک کریں**: کلک کریں [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **ریپوزیٹری کلون کریں**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Microsoft AI Discord کمیونٹی میں شامل ہوں اور ماہرین اور دوسرے ڈویلپرز سے ملاقات کریں**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.ur.png)

## 🌐 کثیراللسانی معاونت

### GitHub Action کے ذریعے سپورٹ شدہ (خودکار اور ہمیشہ تازہ ترین)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](./README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md)

### CLI کے ذریعے سپورٹ - زیرِ تکمیل
## فہرست مضامین

- تعارف
- [Phi فیملی میں خوش آمدید](./md/01.Introduction/01/01.PhiFamily.md)
  - [اپنے ماحول کی ترتیب](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [اہم ٹیکنالوجیز کو سمجھنا](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi ماڈلز کے لیے AI کی حفاظت](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ہارڈویئر کی حمایت](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi ماڈلز اور پلیٹ فارمز پر دستیابی](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai اور Phi کا استعمال](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace ماڈلز](https://github.com/marketplace/models)
  - [Azure AI ماڈل کیٹلاگ](https://ai.azure.com)

- مختلف ماحول میں Inference Phi
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub ماڈلز](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry ماڈل کیٹلاگ](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Inference Phi فیملی
    - [iOS میں Inference Phi](./md/01.Introduction/03/iOS_Inference.md)
    - [Android میں Inference Phi](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson میں Inference Phi](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC میں Inference Phi](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX فریم ورک کے ساتھ Inference Phi](./md/01.Introduction/03/MLX_Inference.md)
    - [مقامی سرور میں Inference Phi](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit استعمال کرتے ہوئے ریموٹ سرور میں Inference Phi](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust کے ساتھ Inference Phi](./md/01.Introduction/03/Rust_Inference.md)
    - [مقامی میں Inference Phi--Vision](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS، Azure Containers (سرکاری حمایت) کے ساتھ Inference Phi](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi فیملی کی مقدار کا تعین](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp استعمال کرتے ہوئے Phi-3.5 / 4 کی مقدار کا تعین](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime کے لیے Generative AI ایکسٹینشنز کے ساتھ Phi-3.5 / 4 کی مقدار کا تعین](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO استعمال کرتے ہوئے Phi-3.5 / 4 کی مقدار کا تعین](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX فریم ورک استعمال کرتے ہوئے Phi-3.5 / 4 کی مقدار کا تعین](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi کی جانچ پڑتال
- [Response AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry for Evaluation](./md/01.Introduction/05/AIFoundry.md)
    - [Using Promptflow for Evaluation](./md/01.Introduction/05/Promptflow.md)
 
- RAG with Azure AI Search
    - [How to use Phi-4-mini and Phi-4-multimodal(RAG) with Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi application development samples
  - Text & Chat Applications
    - Phi-4 Samples 🆕
      - [📓] [Chat With Phi-4-mini ONNX Model](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat with Phi-4 local ONNX Model .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Chat .NET Console App with Phi-4 ONNX using Sementic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 Samples
      - [Local Chatbot in the browser using Phi3, ONNX Runtime Web and WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - Interactive Phi-3-mini and OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Building a wrapper and using Phi-3 with MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Model Optimization - How to optimize Phi-3-min model for ONNX Runtime Web with Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 App with Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 Multi Model AI Powered Notes App Sample](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Fine-tune and Integrate custom Phi-3 models with Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Fine-tune and Integrate custom Phi-3 models with Prompt flow in Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Evaluate the Fine-tuned Phi-3 / Phi-3.5 Model in Azure AI Foundry Focusing on Microsoft's Responsible AI Principles](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct language prediction sample (Chinese/English)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Using Windows GPU to create Prompt flow solution with Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Using Microsoft Phi-3.5 tflite to create Android app](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET Example using local ONNX Phi-3 model using the Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Console chat .NET app with Semantic Kernel and Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK Code Based Samples 
    - Phi-4 Samples 🆕
      - [📓] [Generate project code using Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 Samples
      - [Build your own Visual Studio Code GitHub Copilot Chat with Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Create your own Visual Studio Code Chat Copilot Agent with Phi-3.5 by GitHub Models](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Advanced Reasoning Samples
    - Phi-4 Samples 🆕
      - [📓] [Phi-4-mini-reasoning or Phi-4-reasoning Samples](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Fine-tuning Phi-4-mini-reasoning with Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Fine-tuning Phi-4-mini-reasoning with Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning with GitHub Models](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
- [📓] [Phi-4-mini reasoning with Azure AI Foundry Models](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demos
      - [Phi-4-mini demos hosted on Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demos hosted on Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Vision Samples
    - Phi-4 Samples 🆕
      - [📓] [تصاویر پڑھنے اور کوڈ بنانے کے لیے Phi-4-multimodal کا استعمال](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 Samples
      -  [📓][Phi-3-vision-تصویر سے متن تک](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP ایمبیڈنگ](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 ری سائیکلنگ](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - بصری زبان کا معاون - Phi3-Vision اور OpenVINO کے ساتھ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision کثیر فریم یا کثیر تصویر کا نمونہ](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision مقامی ONNX ماڈل Microsoft.ML.OnnxRuntime .NET استعمال کرتے ہوئے](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [مینو پر مبنی Phi-3 Vision مقامی ONNX ماڈل Microsoft.ML.OnnxRuntime .NET استعمال کرتے ہوئے](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Audio Samples
    - Phi-4 Samples 🆕
      - [📓] [Phi-4-multimodal کے ذریعے آڈیو ٹرانسکرپٹس نکالنا](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal آڈیو نمونہ](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal تقریر ترجمہ کا نمونہ](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET کنسول ایپلیکیشن جو Phi-4-multimodal آڈیو استعمال کرتے ہوئے آڈیو فائل کا تجزیہ اور ٹرانسکرپٹ تیار کرتی ہے](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE Samples
    - Phi-3 / 3.5 Samples
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) سوشل میڈیا نمونہ](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE، Azure AI Search، اور LlamaIndex کے ساتھ Retrieval-Augmented Generation (RAG) پائپ لائن بنانا](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
  - Function Calling Samples
    - Phi-4 Samples 🆕
      -  [📓] [Phi-4-mini کے ساتھ Function Calling کا استعمال](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini کے ساتھ ملٹی ایجنٹس بنانے کے لیے Function Calling کا استعمال](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama کے ساتھ Function Calling کا استعمال](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
  - Multimodal Mixing Samples
    - Phi-4 Samples 🆕
      -  [📓] [Phi-4-multimodal کو ٹیکنالوجی صحافی کے طور پر استعمال کرنا](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET کنسول ایپلیکیشن جو Phi-4-multimodal استعمال کرتے ہوئے تصاویر کا تجزیہ کرتی ہے](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Fine-tuning Phi Samples
  - [Fine-tuning کے منظرنامے](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Fine-tuning بمقابلہ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Fine-tuning تاکہ Phi-3 صنعت کا ماہر بن جائے](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Fine-tuning Phi-3 AI Toolkit for VS Code کے ساتھ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Fine-tuning Phi-3 Azure Machine Learning Service کے ساتھ](./md/03.FineTuning/Introduce_AzureML.md)
- [Fine-tuning Phi-3 with Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Fine-tuning Phi-3 with QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Fine-tuning Phi-3 with Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Fine-tuning Phi-3 with Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Fine-tuning with Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Fine-tuning with Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Fine-tuning Phi-3-vision with Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Fine-tuning Phi-3 with Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Fine-tuning Phi-3-vision (official support)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Fine-Tuning Phi-3 with Kaito AKS , Azure Containers(official Support)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Fine-Tuning Phi-3 and 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands on Lab
  - [جدید ترین ماڈلز کی تلاش: LLMs, SLMs, مقامی ترقی اور مزید](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP کی صلاحیتوں کو کھولنا: Microsoft Olive کے ساتھ Fine-Tuning](https://github.com/azure/Ignite_FineTuning_workshop)

- Academic Research Papers and Publications
  - [Textbooks Are All You Need II: phi-1.5 تکنیکی رپورٹ](https://arxiv.org/abs/2309.05463)
  - [Phi-3 تکنیکی رپورٹ: آپ کے فون پر ایک انتہائی قابل زبان ماڈل](https://arxiv.org/abs/2404.14219)
  - [Phi-4 تکنیکی رپورٹ](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini تکنیکی رپورٹ: کمپیکٹ مگر طاقتور ملٹی موڈل زبان ماڈلز Mixture-of-LoRAs کے ذریعے](https://arxiv.org/abs/2503.01743)
  - [گاڑی میں فنکشن کالنگ کے لیے چھوٹے زبان ماڈلز کی بہتر سازی](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 کو ملٹیپل چوائس سوالات کے جواب دینے کے لیے Fine-Tuning: طریقہ کار، نتائج، اور چیلنجز](https://arxiv.org/abs/2501.01588)
  - [Phi-4-Reasoning تکنیکی رپورٹ](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-Mini-Reasoning تکنیکی رپورٹ](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi ماڈلز کا استعمال

### Phi on Azure AI Foundry

آپ سیکھ سکتے ہیں کہ Microsoft Phi کو کیسے استعمال کریں اور مختلف ہارڈویئر ڈیوائسز میں E2E حل کیسے بنائیں۔ خود Phi کو آزمانے کے لیے، ماڈلز کے ساتھ کھیلنا شروع کریں اور اپنے سیناریوز کے لیے Phi کو حسب ضرورت بنائیں [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) کا استعمال کرتے ہوئے۔ آپ مزید معلومات حاصل کر سکتے ہیں Getting Started with [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) پر۔

**Playground**  
ہر ماڈل کے لیے ایک مخصوص playground ہے جہاں آپ ماڈل کو آزما سکتے ہیں [Azure AI Playground](https://aka.ms/try-phi3)۔

### Phi on GitHub Models

آپ سیکھ سکتے ہیں کہ Microsoft Phi کو کیسے استعمال کریں اور مختلف ہارڈویئر ڈیوائسز میں E2E حل کیسے بنائیں۔ خود Phi کو آزمانے کے لیے، ماڈل کے ساتھ کھیلنا شروع کریں اور اپنے سیناریوز کے لیے Phi کو حسب ضرورت بنائیں [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) کا استعمال کرتے ہوئے۔ آپ مزید معلومات حاصل کر سکتے ہیں Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) پر۔

**Playground**  
ہر ماڈل کے لیے ایک مخصوص [playground ہے جہاں ماڈل کو آزمایا جا سکتا ہے](/md/02.QuickStart/GitHubModel_QuickStart.md)۔

### Phi on Hugging Face

آپ ماڈل کو [Hugging Face](https://huggingface.co/microsoft) پر بھی تلاش کر سکتے ہیں۔

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## ذمہ دار AI

Microsoft ہمارے صارفین کی مدد کے لیے پرعزم ہے کہ وہ ہمارے AI مصنوعات کو ذمہ داری سے استعمال کریں، اپنی سیکھنے والی باتیں شیئر کریں، اور Transparency Notes اور Impact Assessments جیسے ٹولز کے ذریعے اعتماد پر مبنی شراکت داریاں قائم کریں۔ ان میں سے کئی وسائل [https://aka.ms/RAI](https://aka.ms/RAI) پر دستیاب ہیں۔  
Microsoft کا ذمہ دار AI کا طریقہ کار ہمارے AI کے اصولوں پر مبنی ہے جن میں انصاف، اعتبار اور حفاظت، رازداری اور سیکیورٹی، شمولیت، شفافیت، اور جوابدہی شامل ہیں۔
نمونے میں استعمال ہونے والے بڑے پیمانے پر قدرتی زبان، تصویر، اور تقریر کے ماڈلز ممکنہ طور پر غیر منصفانہ، ناقابل اعتماد، یا توہین آمیز طریقوں سے برتاؤ کر سکتے ہیں، جو نقصان کا باعث بن سکتے ہیں۔ براہ کرم خطرات اور حدود کے بارے میں آگاہی کے لیے [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ملاحظہ کریں۔

ان خطرات کو کم کرنے کے لیے تجویز کردہ طریقہ یہ ہے کہ آپ کی ساخت میں ایک حفاظتی نظام شامل کیا جائے جو نقصان دہ رویے کا پتہ لگا سکے اور اسے روک سکے۔ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ایک آزاد حفاظتی تہہ فراہم کرتا ہے، جو ایپلیکیشنز اور خدمات میں نقصان دہ صارف اور AI سے پیدا شدہ مواد کا پتہ لگا سکتا ہے۔ Azure AI Content Safety میں ٹیکسٹ اور تصویر کے API شامل ہیں جو نقصان دہ مواد کی شناخت کی اجازت دیتے ہیں۔ Azure AI Foundry کے اندر، Content Safety سروس آپ کو مختلف طریقوں سے نقصان دہ مواد کی شناخت کے لیے نمونہ کوڈ دیکھنے، تلاش کرنے اور آزمانے کی سہولت دیتی ہے۔ درج ذیل [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) آپ کو سروس کو درخواستیں بھیجنے کے عمل میں رہنمائی کرتی ہے۔

ایک اور پہلو جسے مدنظر رکھنا ضروری ہے وہ مجموعی ایپلیکیشن کی کارکردگی ہے۔ کثیر الوضعی اور کثیر ماڈلز ایپلیکیشنز کے ساتھ، ہم کارکردگی سے مراد یہ لیتے ہیں کہ نظام آپ اور آپ کے صارفین کی توقعات کے مطابق کام کرے، جس میں نقصان دہ نتائج پیدا نہ کرنا بھی شامل ہے۔ اپنے مجموعی ایپلیکیشن کی کارکردگی کا اندازہ لگانے کے لیے [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) استعمال کریں۔ آپ کے پاس [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) بنانے اور ان کا جائزہ لینے کی صلاحیت بھی موجود ہے۔

آپ اپنے AI ایپلیکیشن کا جائزہ اپنے ترقیاتی ماحول میں [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) استعمال کرتے ہوئے لے سکتے ہیں۔ چاہے آپ کے پاس ٹیسٹ ڈیٹا سیٹ ہو یا کوئی ہدف، آپ کی جنریٹو AI ایپلیکیشن کی جنریشنز کو بلٹ ان یا اپنی پسند کے کسٹم ایویلیویٹرز کے ذریعے مقداری طور پر ماپا جاتا ہے۔ اپنے نظام کا جائزہ لینے کے لیے azure ai evaluation sdk کے ساتھ شروع کرنے کے لیے، آپ [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) پر عمل کر سکتے ہیں۔ ایک بار جب آپ جائزہ چلائیں گے، تو آپ [Azure AI Foundry میں نتائج کو دیکھ سکتے ہیں](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)۔

## Trademarks

یہ پروجیکٹ ممکنہ طور پر پروجیکٹس، مصنوعات، یا خدمات کے ٹریڈ مارکس یا لوگوز پر مشتمل ہو سکتا ہے۔ Microsoft کے ٹریڈ مارکس یا لوگوز کا مجاز استعمال [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) کے تابع ہے اور ان کی پیروی کرنا ضروری ہے۔ Microsoft کے ٹریڈ مارکس یا لوگوز کا اس پروجیکٹ کے ترمیم شدہ ورژنز میں استعمال الجھن پیدا نہیں کرنا چاہیے اور نہ ہی Microsoft کی سرپرستی کا تاثر دینا چاہیے۔ کسی تیسرے فریق کے ٹریڈ مارکس یا لوگوز کا استعمال ان فریقوں کی پالیسیوں کے تابع ہے۔

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔