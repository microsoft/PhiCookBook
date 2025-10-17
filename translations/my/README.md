<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4987daf30687ad3850757c9eae3f5411",
  "translation_date": "2025-10-17T10:40:37+00:00",
  "source_file": "README.md",
  "language_code": "my"
}
-->
# Phi Cookbook: Microsoft ရဲ့ Phi မော်ဒယ်များနှင့် လက်တွေ့အသုံးပြုနည်းများ

[![GitHub Codespaces တွင် နမူနာများကို ဖွင့်ပြီး အသုံးပြုပါ](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers တွင် ဖွင့်ပါ](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi သည် Microsoft မှ ဖွံ့ဖြိုးတိုးတက်လာသော အခမဲ့ AI မော်ဒယ်များ ဖြစ်သည်။

Phi သည် လက်ရှိတွင် အကောင်းဆုံးနှင့် စျေးသက်သာဆုံးသော Small Language Model (SLM) ဖြစ်ပြီး ဘာသာစကားများစွာ၊ အကြောင်းအရာဆင်ခြင်း၊ စာသား/စကားပြော ဖန်တီးခြင်း၊ ကုဒ်ရေးခြင်း၊ ပုံများ၊ အသံများနှင့် အခြားအခြေအနေများတွင် အထူးကောင်းမွန်သော စမ်းသပ်မှုရလဒ်များ ရရှိထားသည်။

Phi ကို cloud သို့မဟုတ် edge devices တွင် တင်ဆောင်နိုင်ပြီး အနည်းငယ်သော ကွန်ပျူတာစွမ်းအားဖြင့် Generative AI applications များကို လွယ်ကူစွာ တည်ဆောက်နိုင်ပါသည်။

ဤအရင်းအမြစ်များကို အသုံးပြုရန် အဆင့်များကို လိုက်နာပါ:
1. **Repository ကို Fork လုပ်ပါ**: [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo) ကို နှိပ်ပါ။
2. **Repository ကို Clone လုပ်ပါ**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord Community ကို Join လုပ်ပြီး ကျွမ်းကျင်သူများနှင့် Developer များနှင့် တွေ့ဆုံပါ**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 Multi-Language Support

#### GitHub Action မှတဆင့် ပံ့ပိုးထားသည် (အလိုအလျောက် & အမြဲ Update ဖြစ်နေသည်)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](./README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## အကြောင်းအရာများ

- အကျဉ်းချုပ်
  - [Phi မိသားစုမှ ကြိုဆိုပါသည်](./md/01.Introduction/01/01.PhiFamily.md)
  - [သင့်ပတ်ဝန်းကျင်ကို စနစ်တကျ ပြင်ဆင်ခြင်း](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [အဓိကနည်းပညာများကို နားလည်ခြင်း](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi မော်ဒယ်များအတွက် AI လုံခြုံရေး](./md/01.Introduction/01/01.AISafety.md)
  - [Phi Hardware ပံ့ပိုးမှု](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi မော်ဒယ်များနှင့် Platform များအတွင်း ရရှိနိုင်မှု](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai နှင့် Phi ကို အသုံးပြုခြင်း](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace Models](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- ပတ်ဝန်းကျင်အမျိုးမျိုးတွင် Phi ကို Inference လုပ်ခြင်း
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub Models](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi မိသားစုကို Inference လုပ်ခြင်း
    - [iOS တွင် Phi ကို Inference လုပ်ခြင်း](./md/01.Introduction/03/iOS_Inference.md)
    - [Android တွင် Phi ကို Inference လုပ်ခြင်း](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson တွင် Phi ကို Inference လုပ်ခြင်း](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC တွင် Phi ကို Inference လုပ်ခြင်း](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework ဖြင့် Phi ကို Inference လုပ်ခြင်း](./md/01.Introduction/03/MLX_Inference.md)
    - [Local Server တွင် Phi ကို Inference လုပ်ခြင်း](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Remote Server တွင် AI Toolkit ဖြင့် Phi ကို Inference လုပ်ခြင်း](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust ဖြင့် Phi ကို Inference လုပ်ခြင်း](./md/01.Introduction/03/Rust_Inference.md)
    - [Local တွင် Phi--Vision ကို Inference လုပ်ခြင်း](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (တရားဝင်ပံ့ပိုးမှု) ဖြင့် Phi ကို Inference လုပ်ခြင်း](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi မိသားစုကို Quantify လုပ်ခြင်း](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Phi-3.5 / 4 ကို llama.cpp ဖြင့် Quantize လုပ်ခြင်း](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Generative AI extensions for onnxruntime ဖြင့် Phi-3.5 / 4 ကို Quantize လုပ်ခြင်း](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ဖြင့် Phi-3.5 / 4 ကို Quantize လုပ်ခြင်း](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework ဖြင့် Phi-3.5 / 4 ကို Quantize လုပ်ခြင်း](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi ကို အကဲဖြတ်ခြင်း
    - [Response AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Evaluation အတွက် Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow ကို အသုံးပြု၍ Evaluation လုပ်ခြင်း](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search ဖြင့် RAG
    - [Phi-4-mini နှင့် Phi-4-multimodal (RAG) ကို Azure AI Search ဖြင့် အသုံးပြုနည်း](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi application တည်ဆောက်မှု နမူနာများ
  - စာသားနှင့် စကားပြော Applications
    - Phi-4 နမူနာများ 🆕
      - [📓] [Phi-4-mini ONNX Model ဖြင့် Chat လုပ်ခြင်း](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 local ONNX Model .NET ဖြင့် Chat လုပ်ခြင်း](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel အသုံးပြု၍ Phi-4 ONNX ဖြင့် Chat .NET Console App](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 နမူနာများ
      - [Phi3, ONNX Runtime Web နှင့် WebGPU အသုံးပြု၍ browser တွင် Local Chatbot](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - Phi-3-mini နှင့် OpenAI Whisper ကို Interactive လုပ်ခြင်း](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Wrapper တည်ဆောက်ပြီး Phi-3 ကို MLFlow ဖြင့် အသုံးပြုခြင်း](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Model Optimization - Phi-3-min model ကို ONNX Runtime Web အတွက် Olive ဖြင့် Optimize လုပ်နည်း](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [WinUI3 App with Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [WinUI3 Multi Model AI Powered Notes App Sample](https://github.com/microsoft/ai-powered-notes-winui3-sample)
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
    - [📓] [Phi-4-mini-reasoning with Azure AI Foundry Models](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- Demos  
    - [Phi-4-mini demos hosted on Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Phi-4-multimodal demos hosted on Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- Vision Samples  
  - Phi-4 Samples 🆕  
    - [📓] [Use Phi-4-multimodal to read images and generate code](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Phi-3 / 3.5 Samples  
    - [📓][Phi-3-vision-Image text to text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - Visual language assistant - with Phi3-Vision and OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision multi-frame or multi-image sample](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Phi-3 Vision Local ONNX Model using the Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Menu based Phi-3 Vision Local ONNX Model using the Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- Math Samples  
  - Phi-4-Mini-Flash-Reasoning-Instruct Samples 🆕 [Math Demo with Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)  

- Audio Samples  
  - Phi-4 Samples 🆕  
    - [📓] [Extracting audio transcripts using Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Phi-4-multimodal Audio Sample](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Phi-4-multimodal Speech Translation Sample](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [.NET console application using Phi-4-multimodal Audio to analyze an audio file and generate transcript](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- MOE Samples  
  - Phi-3 / 3.5 Samples  
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) Social Media Sample](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [Building a Retrieval-Augmented Generation (RAG) Pipeline with NVIDIA NIM Phi-3 MOE, Azure AI Search, and LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- Function Calling Samples  
  - Phi-4 Samples 🆕  
    - [📓] [Using Function Calling With Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Using Function Calling to create multi-agents With Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Using Function Calling with Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [Using Function Calling with ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- Multimodal Mixing Samples  
  - Phi-4 Samples 🆕  
    - [📓] [Using Phi-4-multimodal as a Technology journalist](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [.NET console application using Phi-4-multimodal to analyze images](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Fine-tuning Phi Samples  
  - [Fine-tuning Scenarios](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [Fine-tuning vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Fine-tuning Let Phi-3 become an industry expert](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [Fine-tuning Phi-3 with AI Toolkit for VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Fine-tuning Phi-3 with Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)  
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
  - [Exploring cutting-edge models: LLMs, SLMs, local development and more](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [Unlocking NLP Potential: Fine-Tuning with Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- Academic Research Papers and Publications  
  - [Textbooks Are All You Need II: phi-1.5 technical report](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 Technical Report](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini Technical Report: Compact yet Powerful Multimodal Language Models via Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [ကားတွင်းလုပ်ဆောင်ချက်များအတွက် အသေးစားဘာသာစကားမော်ဒယ်များကို အကောင်းဆုံးဖြစ်အောင် ပြုလုပ်ခြင်း](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 ကို Multiple-Choice Question Answering အတွက် Fine-Tuning: နည်းလမ်းများ၊ ရလဒ်များနှင့် စိန်ခေါ်မှုများ](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning နည်းပညာအစီရင်ခံစာ](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning နည်းပညာအစီရင်ခံစာ](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi မော်ဒယ်များ အသုံးပြုခြင်း

### Azure AI Foundry တွင် Phi

Microsoft Phi ကိုဘယ်လိုအသုံးပြုရမလဲ၊ သင့်ရဲ့ hardware စက်ပစ္စည်းများအတွက် E2E ဖြေရှင်းချက်များကို ဘယ်လိုတည်ဆောက်ရမလဲဆိုတာကို သင်လေ့လာနိုင်ပါတယ်။ Phi ကို ကိုယ်တိုင်အတွေ့အကြုံရဖို့အတွက် မော်ဒယ်များကို စမ်းသပ်ပြီး သင့်ရဲ့အခြေအနေများအတွက် Phi ကို customize လုပ်ခြင်းဖြင့် စတင်ပါ။ [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) တွင် သင်ပိုမိုလေ့လာနိုင်ပြီး [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) ကို စတင်အသုံးပြုခြင်းအကြောင်းကိုလည်း သိရှိနိုင်ပါသည်။

**Playground**
မော်ဒယ်တစ်ခုစီမှာ မော်ဒယ်ကို စမ်းသပ်ဖို့အတွက် အထူးပြုထားသော playground ရှိပါတယ် [Azure AI Playground](https://aka.ms/try-phi3)။

### GitHub Models တွင် Phi

Microsoft Phi ကိုဘယ်လိုအသုံးပြုရမလဲ၊ သင့်ရဲ့ hardware စက်ပစ္စည်းများအတွက် E2E ဖြေရှင်းချက်များကို ဘယ်လိုတည်ဆောက်ရမလဲဆိုတာကို သင်လေ့လာနိုင်ပါတယ်။ Phi ကို ကိုယ်တိုင်အတွေ့အကြုံရဖို့အတွက် မော်ဒယ်ကို စမ်းသပ်ပြီး သင့်ရဲ့အခြေအနေများအတွက် Phi ကို customize လုပ်ခြင်းဖြင့် စတင်ပါ။ [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) တွင် သင်ပိုမိုလေ့လာနိုင်ပြီး [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) ကို စတင်အသုံးပြုခြင်းအကြောင်းကိုလည်း သိရှိနိုင်ပါသည်။

**Playground**
မော်ဒယ်တစ်ခုစီမှာ [မော်ဒယ်ကို စမ်းသပ်ဖို့အတွက် playground](/md/02.QuickStart/GitHubModel_QuickStart.md) ရှိပါတယ်။

### Hugging Face တွင် Phi

မော်ဒယ်ကို [Hugging Face](https://huggingface.co/microsoft) တွင်လည်း ရှာဖွေနိုင်ပါတယ်။

**Playground**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## တာဝန်ရှိသော AI 

Microsoft သည် ကျွန်ုပ်တို့၏ AI ထုတ်ကုန်များကို တာဝန်ရှိစွာ အသုံးပြုရန် ကျွန်ုပ်တို့၏ဖောက်သည်များကို ကူညီပေးရန်၊ ကျွန်ုပ်တို့၏အတွေ့အကြုံများကို မျှဝေခြင်းနှင့် Transparency Notes နှင့် Impact Assessments ကဲ့သို့သော tools များမှတစ်ဆင့် ယုံကြည်မှုအခြေခံထားသော မိတ်ဖက်ဆက်ဆံရေးများကို တည်ဆောက်ရန် အတိအကျကတိပြုထားပါသည်။ အများစုသော အရင်းအမြစ်များကို [https://aka.ms/RAI](https://aka.ms/RAI) တွင် ရှာဖွေနိုင်ပါသည်။
Microsoft ၏ တာဝန်ရှိသော AI အပေါ်ရပ်တည်မှုသည် ကျွန်ုပ်တို့၏ AI စည်းမျဉ်းများဖြစ်သော တရားမျှတမှု၊ ယုံကြည်စိတ်ချရမှုနှင့် လုံခြုံမှု၊ ကိုယ်ရေးအချက်အလက်နှင့် လုံခြုံရေး၊ ပါဝင်မှု၊ ထင်ရှားမှုနှင့် တာဝန်ရှိမှုတို့ကို အခြေခံထားပါသည်။

ဤနမူနာတွင် အသုံးပြုထားသော အကြီးစား သဘာဝဘာသာစကား၊ ပုံရိပ်နှင့် အသံမော်ဒယ်များသည် တရားမျှတမှုမရှိခြင်း၊ ယုံကြည်စိတ်ချရမှုမရှိခြင်း သို့မဟုတ် စိတ်ထိခိုက်စေသော အပြုအမူများကို ဖြစ်စေနိုင်ပြီး ထိခိုက်မှုများကို ဖြစ်စေနိုင်ပါသည်။ အန္တရာယ်များနှင့် ကန့်သတ်ချက်များအကြောင်းကို သိရှိရန် [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ကို ကြည့်ရှုပါ။

ဤအန္တရာယ်များကို လျှော့ချရန် အကြံပြုထားသော နည်းလမ်းမှာ သင့် architecture တွင် အန္တရာယ်ရှိသော အပြုအမူများကို ရှာဖွေနိုင်ပြီး ကာကွယ်နိုင်သော safety system တစ်ခုကို ထည့်သွင်းရန်ဖြစ်သည်။ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) သည် လွတ်လပ်သော ကာကွယ်မှုအလွှာတစ်ခုကို ပေးစွမ်းပြီး app များနှင့် ဝန်ဆောင်မှုများတွင် အသုံးပြုသူများဖန်တီးသောအကြောင်းအရာများနှင့် AI ဖန်တီးသောအကြောင်းအရာများကို ရှာဖွေနိုင်သည်။ Azure AI Content Safety တွင် text နှင့် image APIs ပါဝင်ပြီး အန္တရာယ်ရှိသော အကြောင်းအရာများကို ရှာဖွေနိုင်သည်။ Azure AI Foundry တွင် Content Safety service သည် modality များအမျိုးမျိုးတွင် အန္တရာယ်ရှိသော အကြောင်းအရာများကို ရှာဖွေခြင်းအတွက် နမူနာ code ကို ကြည့်ရှု၊ စမ်းသပ်နိုင်ရန် ခွင့်ပြုသည်။ [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) သည် ဝန်ဆောင်မှုသို့ တောင်းဆိုမှုများကို ပြုလုပ်ခြင်းအကြောင်းကို လမ်းညွှန်ပေးသည်။

ထည့်သွင်းစဉ်းစားရန် အခြားအချက်တစ်ခုမှာ application စွမ်းဆောင်ရည်တစ်ခုလုံးဖြစ်သည်။ multi-modal နှင့် multi-models application များတွင် စွမ်းဆောင်ရည်သည် သင်နှင့် သင့်အသုံးပြုသူများ မျှော်မှန်းထားသည့်အတိုင်း စနစ်သည် လုပ်ဆောင်ရမည်ဖြစ်ပြီး အန္တရာယ်ရှိသော output များကို မထုတ်လုပ်ရပါ။ [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ကို အသုံးပြု၍ သင့် application တစ်ခုလုံး၏ စွမ်းဆောင်ရည်ကို အကဲဖြတ်ရန် အရေးကြီးသည်။ သင့်စိတ်ကြိုက် evaluators များဖြင့် [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ကို ဖန်တီးပြီး အကဲဖြတ်နိုင်သည်။

သင့် AI application ကို သင့် development ပတ်ဝန်းကျင်တွင် [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ကို အသုံးပြု၍ အကဲဖြတ်နိုင်သည်။ test dataset သို့မဟုတ် target တစ်ခုကို ပေးပြီး သင့် generative AI application ၏ generation များကို built-in evaluators သို့မဟုတ် သင့်စိတ်ကြိုက် evaluators များဖြင့် အရည်အသွေးကို တိုင်းတာနိုင်သည်။ azure ai evaluation sdk ကို အသုံးပြု၍ သင့်စနစ်ကို အကဲဖြတ်ရန် စတင်လိုပါက [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ကို လိုက်နာနိုင်သည်။ evaluation run တစ်ခုကို အကောင်အထည်ဖော်ပြီးနောက် [Azure AI Foundry တွင် ရလဒ်များကို ကြည့်ရှုနိုင်သည်](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)။

## အမှတ်တံဆိပ်များ

ဤ project တွင် project များ၊ product များ သို့မဟုတ် service များအတွက် အမှတ်တံဆိပ်များ သို့မဟုတ် logo များ ပါဝင်နိုင်သည်။ Microsoft ၏ အမှတ်တံဆိပ် သို့မဟုတ် logo များကို အသုံးပြုရန် ခွင့်ပြုချက်သည် [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ကို လိုက်နာရမည်ဖြစ်သည်။
ဤ project ၏ ပြင်ဆင်ထားသော version များတွင် Microsoft ၏ အမှတ်တံဆိပ် သို့မဟုတ် logo များကို အသုံးပြုခြင်းသည် အလွဲသုံးစားမလုပ်ရမည်ဖြစ်ပြီး Microsoft ၏ အားပေးမှုကို ရည်ညွှန်းရမည်မဟုတ်ပါ။ တတိယပါတီ၏ အမှတ်တံဆိပ် သို့မဟုတ် logo များကို အသုံးပြုခြင်းသည် အတိအကျတိကျသော third-party ၏ မူဝါဒများကို လိုက်နာရမည်ဖြစ်သည်။

## အကူအညီရယူခြင်း

AI app များတည်ဆောက်ရာတွင် အခက်အခဲရှိပါက သို့မဟုတ် မေးခွန်းများရှိပါက အောက်ပါနေရာတွင် ပါဝင်ပါ:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Product feedback သို့မဟုတ် တည်ဆောက်ရာတွင် အမှားများရှိပါက အောက်ပါနေရာသို့ သွားပါ:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။