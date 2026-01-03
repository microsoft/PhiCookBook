<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef3a50368712b1a7483d0def1f70c490",
  "translation_date": "2025-12-21T10:55:30+00:00",
  "source_file": "README.md",
  "language_code": "bn"
}
-->
# Phi কুকবুক: Microsoft-এর Phi মডেলগুলোর হাতে-কলমে উদাহরণ

[![GitHub Codespaces-এ স্যাম্পলগুলো খুলে ব্যবহার করুন](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers-এ খুলুন](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub অবদানকারী](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ইস্যু](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub পুল-রিকুয়েস্টস](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs স্বাগত](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub পর্যবেক্ষক](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ফর্ক](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub স্টার](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi হল Microsoft কর্তৃক তৈরি একটি ওপেন সোর্স AI মডেলের সিরিজ। 

Phi বর্তমানে সবচেয়ে শক্তিশালী এবং খরচ-কার্যকর ছোট ভাষা মডেল (SLM), যা বহু-ভাষা, যুক্তি, টেক্সট/চ্যাট জেনারেশন, কোডিং, চিত্র, অডিও এবং অন্যান্য দৃশ্যে খুব ভালো বেঞ্চমার্ক প্রদর্শন করে। 

আপনি Phi-কে ক্লাউডে বা এজ ডিভাইসে ডিপ্লয় করতে পারেন, এবং সীমিত কম্পিউটিং ক্ষমতা দিয়ে সহজেই জেনারেটিভ AI অ্যাপ্লিকেশন তৈরি করতে পারবেন।

এই রিসোর্স ব্যবহার শুরু করতে নিচের ধাপগুলো অনুসরণ করুন :
1. **রিপোজিটরি ফর্ক করুন**: ক্লিক করুন [![GitHub ফর্ক](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **রিপোজিটরি ক্লোন করুন**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord কমিউনিটিতে যোগ দিন এবং বিশেষজ্ঞ ও অন্যান্য ডেভেলপারদের সাথে পরিচিত হন**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![কভার](../../translated_images/cover.eb18d1b9605d754b.bn.png)

### 🌐 বহু-ভাষা সমর্থন

#### GitHub Action দ্বারা সমর্থিত (স্বয়ংক্রিয় ও সর্বদা আপ-টু-ডেট)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[আরবি](../ar/README.md) | [বাংলা](./README.md) | [বুলগেরিয়ান](../bg/README.md) | [বার্মিজ (মায়ানমার)](../my/README.md) | [চীনা (সরলীকৃত)](../zh/README.md) | [চীনা (প্রথাগত, হংকং)](../hk/README.md) | [চীনা (প্রথাগত, ম্যাকাও)](../mo/README.md) | [চীনা (প্রথাগত, তাইওয়ান)](../tw/README.md) | [ক্রোয়েশিয়ান](../hr/README.md) | [চেক](../cs/README.md) | [ড্যানিশ](../da/README.md) | [ডাচ](../nl/README.md) | [এস্তোনীয়](../et/README.md) | [ফিনিশ](../fi/README.md) | [ফরাসি](../fr/README.md) | [জার্মান](../de/README.md) | [গ্রিক](../el/README.md) | [হিবরু](../he/README.md) | [হিন্দি](../hi/README.md) | [হাঙ্গেরীয়](../hu/README.md) | [ইন্দোনেশীয়](../id/README.md) | [ইতালিয়ান](../it/README.md) | [জাপানি](../ja/README.md) | [কন্নড়](../kn/README.md) | [কোরিয়ান](../ko/README.md) | [লিথুয়ানীয়](../lt/README.md) | [মালয়](../ms/README.md) | [মালায়ালম](../ml/README.md) | [মারাঠি](../mr/README.md) | [নেপালি](../ne/README.md) | [নাইজেরিয়ান পিজিন](../pcm/README.md) | [নরওয়েজিয়ান](../no/README.md) | [ফার্সি (পারসি)](../fa/README.md) | [পোলিশ](../pl/README.md) | [পর্তুগিজ (ব্রাজিল)](../br/README.md) | [পর্তুগিজ (পর্তুগাল)](../pt/README.md) | [পাঞ্জাবি (গুরুমুখি)](../pa/README.md) | [রোমানিয়ান](../ro/README.md) | [রাশিয়ান](../ru/README.md) | [সার্বিয়ান (সিরিলিক)](../sr/README.md) | [স্লোভাক](../sk/README.md) | [স্লোভেনীয়](../sl/README.md) | [স্প্যানিশ](../es/README.md) | [স্বাহিলি](../sw/README.md) | [সুইডিশ](../sv/README.md) | [টাগালগ (ফিলিপিনো)](../tl/README.md) | [তামিল](../ta/README.md) | [তেলুগু](../te/README.md) | [থাই](../th/README.md) | [তুর্কি](../tr/README.md) | [উক্রেনীয়](../uk/README.md) | [উর্দু](../ur/README.md) | [ভিয়েতনামী](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## বিষয়সূচী

- পরিচিতি
  - [Phi পরিবারে স্বাগতম](./md/01.Introduction/01/01.PhiFamily.md)
  - [আপনার পরিবেশ সেট আপ করা](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [প্রধান প্রযুক্তিগুলি বোঝা](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi মডেলগুলির জন্য AI নিরাপত্তা](./md/01.Introduction/01/01.AISafety.md)
  - [Phi হার্ডওয়্যার সমর্থন](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi মডেল এবং প্ল্যাটফর্ম জুড়ে প্রাপ্যতা](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai এবং Phi ব্যবহার করা](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub মার্কেটপ্লেস মডেল](https://github.com/marketplace/models)
  - [Azure AI মডেল ক্যাটালগ](https://ai.azure.com)

- বিভিন্ন পরিবেশে Phi ইনফারেন্স
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub মডেল](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry মডেল ক্যাটালগ](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi পরিবারের ইনফারেন্স
    - [iOS-এ Phi ইনফারেন্স](./md/01.Introduction/03/iOS_Inference.md)
    - [Android-এ Phi ইনফারেন্স](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson-এ Phi ইনফারেন্স](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC-এ Phi ইনফারেন্স](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX ফ্রেমওয়ার্কের সাথে Phi ইনফারেন্স](./md/01.Introduction/03/MLX_Inference.md)
    - [লোকাল সার্ভারে Phi ইনফারেন্স](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit ব্যবহার করে রিমোট সার্ভারে Phi ইনফারেন্স](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust-এর সাথে Phi ইনফারেন্স](./md/01.Introduction/03/Rust_Inference.md)
    - [লোকাল-এ ভিশন ইনফারেন্স](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers(official support) দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi পরিবার কোয়ান্টাইজ করা](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজ করা](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Generative AI extensions for onnxruntime ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজ করা](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজ করা](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX ফ্রেমওয়ার্ক ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজ করা](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi মূল্যায়ন
    - [রেসপন্স AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [মূল্যায়নের জন্য Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [মূল্যায়নের জন্য Promptflow ব্যবহার করা](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search দিয়ে RAG
    - [Azure AI Search-এ Phi-4-mini এবং Phi-4-multimodal(RAG) কীভাবে ব্যবহার করবেন](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi অ্যাপ্লিকেশন ডেভেলপমেন্ট স্যাম্পলস
  - টেক্সট ও চ্যাট অ্যাপ্লিকেশন
    - Phi-4 স্যাম্পলস 🆕
      - [📓] [Phi-4-mini ONNX মডেলের সাথে চ্যাট](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 লোকাল ONNX মডেলের সাথে চ্যাট .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Phi-4 ONNX ব্যবহার করে Sementic Kernel সহ Chat .NET কনসোল অ্যাপ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 স্যাম্পলস
      - [Phi3, ONNX Runtime Web এবং WebGPU ব্যবহার করে ব্রাউজারে লোকাল চ্যাটবট](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino চ্যাট](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [মাল্টি মডেল - ইন্টার‌্যাকটিভ Phi-3-mini এবং OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - একটি র‍্যাপার তৈরি করা এবং MLFlow দিয়ে Phi-3 ব্যবহার করা](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [মডেল অপ্টিমাইজেশন - ONNX Runtime Web-এর জন্য Phi-3-min মডেল Olive দিয়ে কীভাবে অপ্টিমাইজ করবেন](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 অ্যাপ Phi-3 mini-4k-instruct-onnx-এর সাথে](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 মাল্টি-মডেল AI-পাওয়ার্ড নোটস অ্যাপ স্যাম্পল](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [কাস্টম Phi-3 মডেলগুলোকে Prompt flow দিয়ে ফাইন-টিউন এবং ইন্টিগ্রেট করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry-এ Prompt flow দিয়ে কাস্টম Phi-3 মডেলগুলোকে ফাইন-টিউন এবং ইন্টিগ্রেট করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft-এর Responsible AI নীতিকে কেন্দ্র করে Azure AI Foundry-এ ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেল মূল্যায়ন করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct ভাষা প্রেডিকশন নমুনা (চীনা/ইংরেজি)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG চ্যাটবট](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU ব্যবহার করে Phi-3.5-Instruct ONNX দিয়ে Prompt flow সমাধান তৈরি করা](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite ব্যবহার করে Android অ্যাপ তৈরি করা](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET উদাহরণ: Microsoft.ML.OnnxRuntime ব্যবহার করে লোকাল ONNX Phi-3 মডেল ব্যবহার](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel ও Phi-3 সহ কনসোল চ্যাট .NET অ্যাপ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK Code Based Samples 
    - Phi-4 নমুনা 🆕
      - [📓] [Phi-4-multimodal ব্যবহার করে প্রজেক্ট কোড জেনারেট করুন](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 নমুনা
      - [Microsoft Phi-3 Family ব্যবহার করে নিজের Visual Studio Code GitHub Copilot Chat তৈরি করুন](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub Models দ্বারা Phi-3.5 ব্যবহার করে নিজের Visual Studio Code Chat Copilot Agent তৈরি করুন](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Advanced Reasoning Samples
    - Phi-4 নমুনা 🆕
      - [📓] [Phi-4-mini-reasoning বা Phi-4-reasoning নমুনা](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive দিয়ে Phi-4-mini-reasoning ফাইন-টিউন করা](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX দিয়ে Phi-4-mini-reasoning ফাইন-টিউন করা](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub Models সহ Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry Models সহ Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demos
      - [Hugging Face Spaces-এ হোস্ট করা Phi-4-mini ডেমো](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Hugging Face Spaces-এ হোস্ট করা Phi-4-multimodal ডেমো](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Vision Samples
    - Phi-4 নমুনা 🆕
      - [📓] [Phi-4-multimodal ব্যবহার করে ইমেজ পড়া এবং কোড জেনারেট করা](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 নমুনা
      -  [📓][Phi-3-vision-ছবি টেক্সট থেকে টেক্সট](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP এম্বেডিং](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ডেমো: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - ভিজ্যুয়াল ল্যাঙ্গুয়েজ অ্যাসিস্ট্যান্ট - Phi3-Vision এবং OpenVINO-এর সাথে](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision মাল্টি-ফ্রেম বা মাল্টি-ইমেজ নমুনা](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET ব্যবহার করে Phi-3 Vision লোকাল ONNX মডেল](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [মেনু-ভিত্তিক Phi-3 Vision লোকাল ONNX মডেল Microsoft.ML.OnnxRuntime .NET ব্যবহার করে](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Math Samples
    -  Phi-4-Mini-Flash-Reasoning-Instruct নমুনা 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct সহ Math ডেমো](./md/02.Application/09.Math/MathDemo.ipynb)

  - Audio Samples
    - Phi-4 নমুনা 🆕
      - [📓] [Phi-4-multimodal ব্যবহার করে অডিও ট্রান্সক্রিপ্ট বের করা](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal অডিও নমুনা](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal স্পিচ অনুবাদ নমুনা](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET কনসোল অ্যাপ্লিকেশন: Phi-4-multimodal অডিও ব্যবহার করে একটি অডিও ফাইল বিশ্লেষণ করে ট্রান্সক্রিপ্ট জেনারেট করা](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE Samples
    - Phi-3 / 3.5 নমুনা
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) সোশ্যাল মিডিয়া নমুনা](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, এবং LlamaIndex ব্যবহার করে একটি Retrieval-Augmented Generation (RAG) পাইপলাইন তৈরি করা](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Function Calling Samples
    - Phi-4 নমুনা 🆕
      -  [📓] [Phi-4-mini-এর সাথে Function Calling ব্যবহার করা](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini দিয়ে মাল্টি-এজেন্ট তৈরি করার জন্য Function Calling ব্যবহার করা](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama-র সাথে Function Calling ব্যবহার করা](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX-এ Function Calling ব্যবহার করা](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Multimodal Mixing Samples
    - Phi-4 নমুনা 🆕
      -  [📓] [একজন টেকনোলজি সাংবাদিক হিসেবে Phi-4-multimodal ব্যবহার করা](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET কনসোল অ্যাপ্লিকেশন: ছবিগুলো বিশ্লেষণ করার জন্য Phi-4-multimodal ব্যবহার করা](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Fine-tuning Phi Samples
  - [ফাইন-টিউনিং সিনারিওগুলো](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ফাইন-টিউনিং বনাম RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [ফাইন-টিউনিং: Phi-3-কে শিল্প বিশেষজ্ঞ বানানো](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [AI Toolkit for VS Code দিয়ে Phi-3 ফাইন-টিউন করা](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service দিয়ে Phi-3 ফাইন-টিউন করা](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora দিয়ে Phi-3 ফাইন-টিউন করা](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora দিয়ে Phi-3 ফাইন-টিউন করা](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry দিয়ে Phi-3 ফাইন-টিউন করা](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK দিয়ে Phi-3 ফাইন-টিউন করা](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive দিয়ে ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Lab দিয়ে ফাইন-টিউনিং](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias দিয়ে Phi-3-vision ফাইন-টিউন করা](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework দিয়ে Phi-3 ফাইন-টিউন করা](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision ফাইন-টিউনিং (আধিকারিক সমর্থন)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers দিয়ে Phi-3 ফাইন-টিউনিং (আধিকারিক সমর্থন)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 এবং 3.5 Vision ফাইন-টিউনিং](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands on Lab
  - [আধুনিক মডেল অন্বেষণ: LLMs, SLMs, লোকাল ডেভেলপমেন্ট এবং আরও অনেক কিছু](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP ক্ষমতা উন্মোচন: Microsoft Olive দিয়ে ফাইন-টিউনিং](https://github.com/azure/Ignite_FineTuning_workshop)

- Academic Research Papers and Publications
  - [Textbooks Are All You Need II: phi-1.5 কারিগরি রিপোর্ট](https://arxiv.org/abs/2309.05463)
  - [Phi-3 কারিগরি রিপোর্ট: আপনার ফোনে লোকালি একটি অত্যন্ত সক্ষম ভাষা মডেল](https://arxiv.org/abs/2404.14219)
  - [Phi-4 কারিগরি রিপোর্ট](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini প্রযুক্তিগত প্রতিবেদন: Mixture-of-LoRAs মাধ্যমে সংকীর্ণ কিন্তু শক্তিশালী বহু-মোডাল ভাষা মডেল](https://arxiv.org/abs/2503.01743)
  - [ইন-ভেহিকেল ফাংশন-কলিং-এর জন্য ছোট ভাষা মডেল অপ্টিমাইজ করা](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 এর জন্য মাল্টিপল-চয়েস প্রশ্নোত্তর ফাইন-টিউনিং: পদ্ধতি, ফলাফল, এবং চ্যালেঞ্জসমূহ](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning প্রযুক্তিগত প্রতিবেদন](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning প্রযুক্তিগত প্রতিবেদন](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi মডেল ব্যবহার

### Azure AI Foundry-এ Phi

আপনি শিখতে পারবেন কিভাবে Microsoft Phi ব্যবহার করতে হয় এবং কিভাবে আপনার বিভিন্ন হার্ডওয়্যার ডিভাইসে end-to-end (E2E) সমাধান তৈরি করা যায়। নিজে Phi অনুভব করার জন্য, মডেলগুলো নিয়ে পরীক্ষা করা এবং আপনার ব্যবহারের ক্ষেত্রে Phi কাস্টমাইজ করা শুরু করুন [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ব্যবহার করে — আপনি আরও জানতে পারেন [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) নিয়ে শুরু করে।

**প্লেগ্রাউন্ড**
প্রতিটি মডেলের একটি নিবেদিত প্লেগ্রাউন্ড আছে মডেলটি পরীক্ষা করার জন্য [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub মডেলগুলোতে Phi

আপনি শিখতে পারবেন কিভাবে Microsoft Phi ব্যবহার করতে হয় এবং কিভাবে আপনার বিভিন্ন হার্ডওয়্যার ডিভাইসে end-to-end (E2E) সমাধান তৈরি করা যায়। নিজে Phi অনুভব করার জন্য, মডেল নিয়ে পরীক্ষা করা এবং আপনার ব্যবহারের ক্ষেত্রে Phi কাস্টমাইজ করা শুরু করুন [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ব্যবহার করে — আপনি আরও জানতে পারেন [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) নিয়ে শুরু করে।

**প্লেগ্রাউন্ড**
প্রতিটি মডেলের একটি নিবেদিত [মডেল পরীক্ষা করার প্লেগ্রাউন্ড](/md/02.QuickStart/GitHubModel_QuickStart.md) আছে।

### Hugging Face-এ Phi

আপনি মডেলটি [Hugging Face](https://huggingface.co/microsoft) থেকেও খুঁজে পেতে পারেন

**প্লেগ্রাউন্ড**
 [Hugging Chat প্লেগ্রাউন্ড](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 অন্যান্য কোর্স

আমাদের দল অন্যান্য কোর্সও তৈরি করে! দেখে নিন:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Core Learning
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Series
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## দায়িত্বশীল AI 

Microsoft আমাদের গ্রাহকদের সহায়তা করতে প্রতিশ্রুতিবদ্ধ যাতে তারা আমাদের AI পণ্যগুলি দায়িত্বশীলভাবে ব্যবহার করে, আমাদের শিখনগুলি ভাগ করে, এবং Transparency Notes এবং Impact Assessments-এর মতো সরঞ্জামগুলির মাধ্যমে বিশ্বাসভিত্তিক অংশীদারিত্ব গড়ে তোলে। এই রিসোর্সগুলোর অনেকগুলো আপনি [https://aka.ms/RAI](https://aka.ms/RAI) এ পেতে পারেন। Microsoft-এর দায়িত্বশীল AI-এর 접근 পদ্ধতি আমাদের AI নীতিমালার ন্যায়পরতা, নির্ভরযোগ্যতা ও নিরাপত্তা, গোপনীয়তা ও নিরাপত্তা, অন্তর্ভুক্তি, স্বচ্ছতা এবং জবাবদিহিতার উপর ভিত্তি করে গঠিত।

বৃহৎ-স্কেলের প্রাকৃতিক ভাষা, চিত্র, এবং স্পিচ মডেল—যেমন এই নমুনায় ব্যবহৃত মডেলগুলো—সম্ভবত এমনভাবে আচরণ করতে পারে যা অন্যায়, অ reliable নয়, বা আপত্তিকর হতে পারে, এবং এভাবে ক্ষতি ডেকে আনতে পারে। ঝুঁকি ও সীমাবদ্ধতা সম্পর্কে অবহিত হতে অনুগ্রহ করে [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) দেখুন।

এই ঝুঁকিগুলো প্রশমন করার জন্য সুপারিশকৃত পদ্ধতি হল আপনার আর্কিটেকচারে একটি সেফটি সিস্টেম অন্তর্ভুক্ত করা যা ক্ষতিকারক আচরণ সনাক্ত ও প্রতিরোধ করতে পারে। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) একটি স্বাধীন সুরক্ষা স্তর প্রদান করে, যা অ্যাপ্লিকেশন ও সার্ভিসে ক্ষতিকারক ব্যবহারকারী-তৈরী এবং AI-তৈরী কন্টেন্ট সনাক্ত করতে সক্ষম। Azure AI Content Safety-এ টেক্সট এবং ইমেজ API রয়েছে যা ক্ষতিকারক উপকরণ সনাক্ত করতে দেয়। Azure AI Foundry-এর মধ্যে, Content Safety সার্ভিসটি আপনাকে বিভিন্ন মোডালিটি জুড়ে ক্ষতিকারক কনটেন্ট সনাক্ত করার জন্য নমুনা কোড দেখার, অন্বেষণ করার এবং পরীক্ষা করার সুযোগ দেয়। নিম্নলিখিত [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) আপনাকে সার্ভিসটিতে অনুরোধ পাঠানোর মাধ্যমে গাইড করবে।

আরেকটি বিবেচ্য বিষয় হল সামগ্রিক অ্যাপ্লিকেশন পারফরম্যান্স। মাল্টি-মোডাল এবং মাল্টি-মডেল অ্যাপ্লিকেশনে, আমরা পারফরম্যান্স বলতে বোঝাই যে সিস্টেমটি আপনার এবং আপনার ব্যবহারকারীদের প্রত্যাশানুসারে কাজ করে, যার মধ্যে ক্ষতিকারক আউটপুট তৈরি না করাও অন্তর্ভুক্ত। আপনার মোট অ্যাপ্লিকেশনের পারফরম্যান্স মূল্যায়ন করা গুরুত্বপূর্ণ, [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ব্যবহার করে। আপনার ইচ্ছা হলে আপনি [কাস্টম ইভালুয়েটরস](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) তৈরি এবং ব্যবহার করেও মূল্যায়ন করতে পারেন।

আপনি আপনার ডেভেলপমেন্ট পরিবেশে [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ব্যবহার করে আপনার AI অ্যাপ্লিকেশন মূল্যায়ন করতে পারেন। একটি টেস্ট ডেটাসেট বা টার্গেট প্রদত্ত হলে, আপনার জেনারেটিভ AI অ্যাপ্লিকেশন জেনারেশনগুলো নির্মিত ইভালুয়েটরস বা আপনার পছন্দের কাস্টম ইভালুয়েটরস দিয়ে পরিমাণগতভাবে মাপা হয়। আপনার সিস্টেম মূল্যায়ন শুরু করার জন্য azure ai evaluation sdk সম্পর্কে শুরু করার নির্দেশিকা অনুসরণ করতে পারেন: [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk)। একবার আপনি একটি ইভালুয়েশন চালালে, আপনি [Azure AI Foundry-তে ফলাফল ভিজ্যুয়ালাইজ করতে পারেন](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)। 

## ট্রেডমার্ক
এই প্রকল্পে প্রকল্প, পণ্য, বা পরিষেবার ট্রেডমার্ক বা লোগো থাকতে পারে। অনুমোদিতভাবে Microsoft-এর ট্রেডমার্ক বা লোগো ব্যবহারের বিষয়টি [Microsoft-এর ট্রেডমার্ক ও ব্র্যান্ড নির্দেশিকা](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)-এর অধীন এবং তা অনুসরণ করা আবশ্যক।
এই প্রকল্পের পরিবর্তিত সংস্করণে Microsoft-এর ট্রেডমার্ক বা লোগো ব্যবহারে বিভ্রান্তি সৃষ্টি করা যাবে না বা Microsoft-এর স্পনসরশিপ বোঝানো উচিত নয়। তৃতীয়-পক্ষের ট্রেডমার্ক বা লোগো ব্যবহার সেই তৃতীয়-পক্ষের নীতিমালার আইনগত অধীনে থাকবে।

## সহায়তা পান

যদি আপনি আটকে যান বা AI অ্যাপ তৈরি করার বিষয়ে কোনো প্রশ্ন থাকে, যোগ দিন:

[![অ্যাজুর এআই ফাউন্ড্রি ডিসকর্ড](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

যদি আপনার পণ্য সম্পর্কিত প্রতিক্রিয়া থাকে বা বিল্ড করার সময় কোনো ত্রুটি ঘটে, দেখুন:

[![অ্যাজুর এআই ফাউন্ড্রি ডেভেলপার ফোরাম](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
অস্বীকারোক্তি:
এই নথিটি AI অনুবাদ পরিষেবা Co-op Translator (https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। যদিও আমরা যথাসম্ভব নির্ভুল হওয়ার চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসামঞ্জস্য থাকতে পারে। মূল নথিটি তার নিজভাষায় প্রামাণ্য উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ করা পরামর্শযোগ্য। এই অনুবাদের ব্যবহারের ফলে সৃষ্ট কোনো ভুলবোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->