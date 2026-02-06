# Phi কুকবুক: Microsoft-এর Phi মডেল সহ হাতেকলমে উদাহরণ

[![GitHub Codespaces-এ স্যাম্পলগুলো খুলুন এবং ব্যবহার করুন](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers-এ খুলুন](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub অবদানকারীরা](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ইস্যুগুলো](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub পুল রিকোয়েস্ট](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs স্বাগত](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub ওয়াচাররা](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ফর্ক](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub তারকা](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi হল Microsoft দ্বারা বিকাশিত একটি ওপেন সোর্স AI মডেলের সিরিজ।

Phi বর্তমানে সবচেয়ে শক্তিশালী এবং খরচ-কার্যকর ছোট ভাষার মডেল (SLM), যা মাল্টি-ল্যাঙ্গুয়েজ, যুক্তি, টেক্সট/চ্যাট জেনারেশন, কোডিং, ছবি, অডিও এবং অন্যান্য পরিস্থিতিতে খুব ভাল বেঞ্চমার্ক রয়েছে।

আপনি Phi কে ক্লাউডে বা এডজ ডিভাইসে ডিপ্লয় করতে পারেন, এবং সীমিত কম্পিউটিং ক্ষমতা নিয়ে সহজেই জেনারেটিভ AI অ্যাপ্লিকেশন তৈরি করতে পারেন।

এই রিসোর্সগুলি ব্যবহার শুরু করতে নিম্নলিখিত ধাপগুলি অনুসরণ করুন:
1. **রিপোসিটরি ফর্ক করুন**: ক্লিক করুন [![GitHub ফর্ক](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **রিপোসিটরি ক্লোন করুন**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord কমিউনিটিতে যোগ দিন এবং বিশেষজ্ঞ ও সহ-ডেভেলপারদের সাথে পরিচিত হন**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/bn/cover.eb18d1b9605d754b.webp)

### 🌐 বহু-ভাষা সমর্থন

#### GitHub Action এর মাধ্যমে সমর্থিত (স্বয়ংক্রিয় এবং সর্বদা আপ-টু-ডেট)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[আরবি](../ar/README.md) | [বাংলা](./README.md) | [বুলগেরিয়ান](../bg/README.md) | [বর্মিজ (মায়ানমার)](../my/README.md) | [চীনা (সরলীকৃত)](../zh-CN/README.md) | [চীনা (প্রচলিত, হংকং)](../zh-HK/README.md) | [চীনা (প্রচলিত, মাকাউ)](../zh-MO/README.md) | [চীনা (প্রচলিত, তাইওয়ান)](../zh-TW/README.md) | [ক্রোয়েশিয়ান](../hr/README.md) | [চেক](../cs/README.md) | [ড্যানিশ](../da/README.md) | [ডাচ](../nl/README.md) | [এস্তোনিয়ান](../et/README.md) | [ফিনিশ](../fi/README.md) | [ফরাসি](../fr/README.md) | [জার্মান](../de/README.md) | [গ্রীক](../el/README.md) | [হিব্রু](../he/README.md) | [হিন্দি](../hi/README.md) | [হাঙ্গেরিয়ান](../hu/README.md) | [ইন্দোনেশিয়ান](../id/README.md) | [ইতালিয়ান](../it/README.md) | [জাপানি](../ja/README.md) | [কন্নড়](../kn/README.md) | [কোরিয়ান](../ko/README.md) | [লিথুয়ানিয়ান](../lt/README.md) | [মালয়](../ms/README.md) | [মালায়ালাম](../ml/README.md) | [মারাঠি](../mr/README.md) | [নেপালি](../ne/README.md) | [নাইজেরিয়ান পিজিন](../pcm/README.md) | [নরওয়েজিয়ান](../no/README.md) | [পারসিয়ান (ফার্সি)](../fa/README.md) | [পোলিশ](../pl/README.md) | [পর্তুগিজ (ব্রাজিল)](../pt-BR/README.md) | [পর্তুগিজ (পর্তুগাল)](../pt-PT/README.md) | [পাঞ্জাবী (গুরুমুখি)](../pa/README.md) | [রোমানীয়ান](../ro/README.md) | [রাশিয়ান](../ru/README.md) | [সার্বীয় (সিরিলিক)](../sr/README.md) | [স্লোভাক](../sk/README.md) | [স্লোভেনিয়ান](../sl/README.md) | [স্প্যানিশ](../es/README.md) | [সোয়াহিলি](../sw/README.md) | [সুইডিশ](../sv/README.md) | [টাগালগ (ফিলিপিনো)](../tl/README.md) | [তামিল](../ta/README.md) | [তেলুগু](../te/README.md) | [থাই](../th/README.md) | [তুর্কিশ](../tr/README.md) | [ইউক্রেনিয়ান](../uk/README.md) | [উর্দু](../ur/README.md) | [ভিয়েতনামীজ](../vi/README.md)

> **স্থানীয়ভাবে ক্লোন করতে চান?**

> এই রিপোসিটরিতে ৫০+ ভাষার অনুবাদ রয়েছে যা ডাউনলোড সাইজ অনেক বৃদ্ধি করে। অনুবাদ ছাড়া ক্লোন করতে sparse checkout ব্যবহার করুন:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> যা কোর্স সম্পূর্ণ করার জন্য আপনার সবকিছু আরও দ্রুত ডাউনলোড দেবে।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## বিষয়বস্তু

- পরিচিতি
  - [Phi পরিবারে স্বাগতম](./md/01.Introduction/01/01.PhiFamily.md)
  - [আপনার পরিবেশ সেটআপ করা](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [মূল প্রযুক্তিগুলো বোঝা](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi মডেলগুলোর জন্য AI নিরাপত্তা](./md/01.Introduction/01/01.AISafety.md)
  - [Phi হার্ডওয়্যার সমর্থন](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi মডেলস এবং প্ল্যাটফর্মগুলিতে প্রাপ্যতা](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai এবং Phi ব্যবহার](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub মার্কেটপ্লেস মডেলস](https://github.com/marketplace/models)
  - [Azure AI মডেল ক্যাটালগ](https://ai.azure.com)

- বিভিন্ন পরিবেশে Phi ইনফারেন্স
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub মডেলস](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry মডেল ক্যাটালগ](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi পরিবার ইনফারেন্স
    - [iOS-এ Phi ইনফারেন্স](./md/01.Introduction/03/iOS_Inference.md)
    - [Android-এ Phi ইনফারেন্স](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson-এ Phi ইনফারেন্স](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC-তে Phi ইনফারেন্স](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/MLX_Inference.md)
    - [স্থানীয় সার্ভারে Phi ইনফারেন্স](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit ব্যবহার করে রিমোট সার্ভারে Phi ইনফারেন্স](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/Rust_Inference.md)
    - [স্থানীয়ভাবে Phi--Vision ইনফারেন্স](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (আফিসিয়াল সাপোর্ট) ব্যবহার করে Phi ইনফারেন্স](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi পরিবারের কোয়ান্টিফিকেশন](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime এর জন্য Generative AI এক্সটেনশান ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi মূল্যায়ন
    - [দায়িত্বশীল AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry দ্বারা মূল্যায়ন](./md/01.Introduction/05/AIFoundry.md)
    - [মূল্যায়নের জন্য Promptflow ব্যবহার](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search এর সাথে RAG
    - [Phi-4-mini এবং Phi-4-multimodal (RAG) Azure AI Search-এ কিভাবে ব্যবহার করা যায়](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi অ্যাপ্লিকেশন উন্নয়নের স্যাম্পলস
  - টেক্সট এবং চ্যাট অ্যাপ্লিকেশন
    - Phi-4 স্যাম্পলস 🆕
      - [📓] [Phi-4-mini ONNX মডেল দিয়ে চ্যাট করুন](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 স্থানীয় ONNX মডেল দিয়ে .NET-এ চ্যাট](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Semantic Kernel ব্যবহার করে Phi-4 ONNX দিয়ে .NET কনসোল অ্যাপের চ্যাট](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 স্যাম্পলস
      - [Phi3, ONNX Runtime Web এবং WebGPU ব্যবহার করে ব্রাউজারে স্থানীয় চ্যাটবট](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino চ্যাট](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [মাল্টি মডেল - ইন্টারেক্টিভ Phi-3-mini এবং OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - একটি র‍্যাপার তৈরি এবং Phi-3 কে MLFlow এর সাথে ব্যবহার](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [মডেল অপ্টিমাইজেশন - Olive সহ ONNX Runtime Web এর জন্য Phi-3-mini মডেল কীভাবে অপ্টিমাইজ করবেন](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx সহ WinUI3 অ্যাপ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 মাল্টি মডেল AI চালিত নোটস অ্যাপ স্যাম্পল](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Prompt flow এর সাথে কাস্টম Phi-3 মডেল ফাইন-টিউন এবং ইন্টিগ্রেট করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry তে Prompt flow এর সাথে কাস্টম Phi-3 মডেল ফাইন-টিউন এবং ইন্টিগ্রেট করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft এর দায়িত্বশীল AI নীতিমালা ফোকাস করে Azure AI Foundry তে ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেল মূল্যায়ন করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct ভাষা পূর্বাভাস স্যাম্পল (চীনা/ইংরেজি)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG চ্যাটবট](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU ব্যবহার করে Phi-3.5-Instruct ONNX এর সাহায্যে Prompt flow সমাধান তৈরি](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite ব্যবহার করে Android অ্যাপ তৈরি](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [স্থানীয় ONNX Phi-3 মডেল ব্যবহার করে Microsoft.ML.OnnxRuntime যথাক্রমে Q&A .NET উদাহরণ](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel এবং Phi-3 সহ কনসোল চ্যাট .NET অ্যাপ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK কোড ভিত্তিক স্যাম্পল 
    - Phi-4 স্যাম্পল 🆕
      - [📓] [Phi-4-multimodal ব্যবহার করে প্রজেক্ট কোড তৈরি করুন](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 স্যাম্পল
      - [Microsoft Phi-3 পরিবার ব্যবহার করে আপনার নিজের Visual Studio Code GitHub Copilot চ্যাট তৈরি করুন](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub মডেল দ্বারা Phi-3.5 সহ আপনার নিজস্ব Visual Studio Code চ্যাট কপিলট এজেন্ট তৈরি করুন](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - উন্নত যুক্তিবাদ স্যাম্পল
    - Phi-4 স্যাম্পল 🆕
      - [📓] [Phi-4-mini-reasoning বা Phi-4-reasoning স্যাম্পল](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive দিয়ে Phi-4-mini-reasoning ফাইন-টিউনিং](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX দিয়ে Phi-4-mini-reasoning ফাইন-টিউনিং](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub মডেলসহ Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry মডেল সহ Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - ডেমো
      - [Hugging Face Spaces এ হোস্ট করা Phi-4-mini ডেমো](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Hugginge Face Spaces এ হোস্ট করা Phi-4-multimodal ডেমো](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - ভিশন স্যাম্পল
    - Phi-4 স্যাম্পল 🆕
      - [📓] [Phi-4-multimodal ব্যবহার করে ছবি পড়ুন এবং কোড তৈরি করুন](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 স্যাম্পল
      -  [📓][Phi-3-vision-ছবি থেকে টেক্সট টু টেক্সট](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP এমবেডিং](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ডেমো: Phi-3 রিসাইক্লিং](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - ভিজ্যুয়াল ভাষা সহকারী - Phi3-Vision এবং OpenVINO সহ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 ভিশন Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 ভিশন OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 ভিশন মাল্টি-ফ্রেম বা মাল্টি-ইমেজ স্যাম্পল](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET ব্যবহার করে Phi-3 Vision লোকাল ONNX মডেল](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [মেনু ভিত্তিক Phi-3 Vision লোকাল ONNX মডেল Microsoft.ML.OnnxRuntime .NET ব্যবহার করে](../../md/04.HOL/dotnet/src/LabsPhi304)

  - গাণিতিক স্যাম্পল
    -  Phi-4-Mini-Flash-Reasoning-Instruct স্যাম্পল 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct সহ গাণিতিক ডেমো](./md/02.Application/09.Math/MathDemo.ipynb)

  - অডিও স্যাম্পল
    - Phi-4 স্যাম্পল 🆕
      - [📓] [Phi-4-multimodal ব্যবহার করে অডিও ট্রান্সক্রিপ্ট বের করা](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal অডিও স্যাম্পল](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal স্পিচ ট্রান্সলেশন স্যাম্পল](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET কনসোল অ্যাপ্লিকেশন Phi-4-multimodal অডিও ব্যবহার করে একটি অডিও ফাইল বিশ্লেষণ এবং ট্রান্সক্রিপ্ট তৈরি](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE স্যাম্পল
    - Phi-3 / 3.5 স্যাম্পল
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) সোশ্যাল মিডিয়া স্যাম্পল](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, এবং LlamaIndex সহ রিট্রিভাল-অগুমেন্টেড জেনারেশন (RAG) পাইপলাইন তৈরি](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - ফাংশন কলিং স্যাম্পল
    - Phi-4 স্যাম্পল 🆕
      -  [📓] [Phi-4-mini সহ ফাংশন কলিং ব্যবহার](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini সহ মাল্টি-এজেন্ট তৈরি করার জন্য ফাংশন কলিং ব্যবহার](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama সহ ফাংশন কলিং ব্যবহার](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX সহ ফাংশন কলিং ব্যবহার](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - মাল্টিমডাল মিক্সিং স্যাম্পল
    - Phi-4 স্যাম্পল 🆕
      -  [📓] [Phi-4-multimodal কে প্রযুক্তি সাংবাদিক হিসাবে ব্যবহার](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET কনসোল অ্যাপ্লিকেশন Phi-4-multimodal ব্যবহার করে ছবি বিশ্লেষণ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi ফাইন-টিউনিং স্যাম্পল
  - [ফাইন-টিউনিং পরিস্থিতি](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ফাইন-টিউনিং বনাম RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 কে একটি শিল্প বিশেষজ্ঞ বানান ফাইন-টিউনিং](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [AI Toolkit for VS Code সহ Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service সহ Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora সহ Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora সহ Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry সহ Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK সহ Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive সহ ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Lab সহ ফাইন-টিউনিং](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias সহ Phi-3-vision ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework সহ Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision ফাইন-টিউনিং (সরকারি সমর্থন)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers সহ Phi-3 ফাইন-টিউনিং (সরকারি সমর্থন)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 এবং 3.5 Vision ফাইন-টিউনিং](https://github.com/2U1/Phi3-Vision-Finetune)

- হ্যান্ডস অন ল্যাব
  - [সর্বাধুনিক মডেল অনুসন্ধান: LLMs, SLMs, স্থানীয় উন্নয়ন এবং আরও অনেক কিছু](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP সম্ভাবনা শিখুন: Microsoft Olive এর সাহায্যে ফাইন-টিউনিং](https://github.com/azure/Ignite_FineTuning_workshop)

- একাডেমিক গবেষণা পেপার এবং প্রকাশনা
  - [শিক্ষাপুস্তকেই সবকিছুই দরকার: phi-1.5 প্রযুক্তিগত প্রতিবেদন](https://arxiv.org/abs/2309.05463)
  - [Phi-3 প্রযুক্তিগত প্রতিবেদন: আপনার ফোনে স্থানীয়ভাবে অত্যন্ত সক্ষম ভাষা মডেল](https://arxiv.org/abs/2404.14219)
  - [Phi-4 প্রযুক্তিগত প্রতিবেদন](https://arxiv.org/abs/2412.08905)
  - [Phi-4-মিনি প্রযুক্তিগত প্রতিবেদন: মিক্সচার-অফ-লোরাসের মাধ্যমে সংক্ষিপ্ত তবুও শক্তিশালী মাল্টিমোডাল ভাষা মডেল](https://arxiv.org/abs/2503.01743)
  - [গাড়ির মধ্যে ফাংশন-কলিংয়ের জন্য ছোট ভাষা মডেলগুলিকে অপ্টিমাইজ করা](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) একাধিক-বিকল্প প্রশ্নোত্তরের জন্য PHI-3 ফাইন-টিউনিং: পদ্ধতি, ফলাফল, এবং চ্যালেঞ্জ](https://arxiv.org/abs/2501.01588)
  - [Phi-4-যুক্তি প্রযুক্তিগত প্রতিবেদন](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-মিনি-যুক্তি প্রযুক্তিগত প্রতিবেদন](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi মডেলগুলির ব্যবহার

### Azure AI Foundry-তে Phi

আপনি শিখতে পারেন কিভাবে Microsoft Phi ব্যবহার করতে হয় এবং কিভাবে আপনার বিভিন্ন হার্ডওয়্যার ডিভাইসগুলিতে E2E সমাধান তৈরি করতে হয়। Phi নিজে অনুভব করার জন্য, মডেলগুলির সাথে ইন্টারঅ্যাক্ট করা শুরু করুন এবং আপনার পরিস্থিতির জন্য Phi কাস্টমাইজ করুন [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ব্যবহার করে। আপনি আরও জানতে পারেন [Azure AI Foundry-এর সাথে শুরুর পথনির্দেশিকা](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) থেকে।

**Playground**  
প্রতি মডেলের জন্য একটি নিবেদিত প্লে গ্রাউন্ড রয়েছে যেখানে আপনি মডেল পরীক্ষা করতে পারবেন [Azure AI Playground](https://aka.ms/try-phi3)।

### GitHub মডেলগুলিতে Phi

আপনি শিখতে পারেন কিভাবে Microsoft Phi ব্যবহার করতে হয় এবং কিভাবে আপনার বিভিন্ন হার্ডওয়্যার ডিভাইসগুলিতে E2E সমাধান তৈরি করতে হয়। Phi নিজে অনুভব করার জন্য, মডেলের সাথে খেলা শুরু করুন এবং আপনার পরিস্থিতির জন্য Phi কাস্টমাইজ করুন [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ব্যবহার করে। আপনি আরও জানতে পারেন [GitHub Model Catalog-এর সাথে শুরুর পথনির্দেশিকা](/md/02.QuickStart/GitHubModel_QuickStart.md) থেকে।

**Playground**  
প্রতি মডেলের জন্য একটি নিবেদিত [প্লেগ্রাউন্ড রয়েছে মডেলটি পরীক্ষা করার জন্য](/md/02.QuickStart/GitHubModel_QuickStart.md)।

### Hugging Face-এ Phi

আপনি মডেলটি [Hugging Face](https://huggingface.co/microsoft) এও পেতে পারেন।

**Playground**  
[Hugging Chat প্লে গ্রাউন্ড](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 অন্যান্য কোর্স

আমাদের দল অন্যান্য কোর্সও তৈরি করে! দেখে নিন:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![প্রারম্ভিকদের জন্য LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![প্রারম্ভিকদের জন্য LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![প্রারম্ভিকদের জন্য LangChain](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / এজেন্ট
[![প্রারম্ভিকদের জন্য AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![প্রারম্ভিকদের জন্য Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![প্রারম্ভিকদের জন্য MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![প্রারম্ভিকদের জন্য AI Agents](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### জেনারেটিভ AI সিরিজ
[![প্রারম্ভিকদের জন্য জেনারেটিভ AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![জেনারেটিভ AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![জেনারেটিভ AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![জেনারেটিভ AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### মূল শিক্ষণ
[![প্রারম্ভিকদের জন্য ML](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![প্রারম্ভিকদের জন্য ডেটা সায়েন্স](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![প্রারম্ভিকদের জন্য AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![প্রারম্ভিকদের জন্য সাইবারসিকিউরিটি](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![প্রারম্ভিকদের জন্য ওয়েব ডেভেলপমেন্ট](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![প্রারম্ভিকদের জন্য IoT](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![প্রারম্ভিকদের জন্য XR ডেভেলপমেন্ট](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### কোপাইলট সিরিজ
[![AI যৌথ প্রোগ্রামিংয়ের জন্য কোপাইলট](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET এর জন্য কোপাইলট](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![কোপাইলট অ্যাডভেঞ্চার](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## দায়িত্বশীল AI

Microsoft আমাদের গ্রাহকদের আমাদের AI পণ্যসমূহ দায়িত্বশীলভাবে ব্যবহার করতে সাহায্য করতে প্রতিশ্রুতিবদ্ধ, আমাদের শেখানো বিষয়গুলি শেয়ার করে এবং এ ধরনের সরঞ্জাম যেমন Transparency Notes এবং Impact Assessments-এর মাধ্যমে বিশ্বাস ভিত্তিক অংশীদারিত্ব গড়ে তোলায় মনোযোগ দেয়। এই সংস্থানগুলোর অনেকগুলো পাওয়া যায় [https://aka.ms/RAI](https://aka.ms/RAI)-এ।  
Microsoft-এর দায়িত্বশীল AI-এর পন্থা হল ন্যায্যতা, নির্ভরযোগ্যতা ও নিরাপত্তা, গোপনীয়তা ও সুরক্ষা, অন্তর্ভুক্তি, স্বচ্ছতা এবং জবাবদিহিতার AI নীতির ভিত্তিতে প্রতিষ্ঠিত।  

বিস্তৃত স্কেলের প্রাকৃতিক ভাষা, চিত্র, এবং বক্তৃতা মডেল - যেমন এই নমুনাতে ব্যবহৃত - সম্ভবত এমনভাবে আচরণ করতে পারে যা হয় অন্যানীতিপূর্ণ, অস্থির, বা আপত্তিকর, যা পরবর্তীতে ক্ষতি ডেকে আনতে পারে। অনুগ্রহ করে সঙ্কট এবং সীমাবদ্ধতা সম্পর্কে জানার জন্য [Azure OpenAI সার্ভিস Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) পরামর্শ করুন।  

এতে ঝুঁকি প্রশমন করার সুপারিশকৃত পন্থা হল আপনার আর্কিটেকচারে একটি সেফটি সিস্টেম অন্তর্ভুক্ত করা যা ক্ষতিকর আচরণ শনাক্ত ও রোধ করতে পারে। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) একটি স্বতন্ত্র সুরক্ষা স্তর সরবরাহ করে, যা অ্যাপ্লিকেশন ও সেবাগুলিতে ক্ষতিকর ব্যবহারকারী-তৈরি এবং AI-তৈরি বিষয়বস্তু শনাক্ত করতে সক্ষম। Azure AI Content Safety-তে টেক্সট এবং চিত্র API রয়েছে যা আপনাকে ক্ষতিকর সামগ্রী শনাক্ত করতে দেয়। Azure AI Foundry-এর মধ্যে Content Safety সার্ভিসটি বিভিন্ন মোডালিটিজ জুড়ে ক্ষতিকর সামগ্রী শনাক্তের নমুনা কোড দেখতে, অন্বেষণ করতে এবং ব্যবহার করতে দেয়। নিম্নলিখিত [দ্রুত শুরু ডকুমেন্টেশন](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) আপনাকে সার্ভিসে রিকুয়েস্ট পাঠানোর প্রক্রিয়া সম্পর্কে নির্দেশনা প্রদান করে।
আরেকটি বিবেচ্য দিক হল সার্বিক অ্যাপ্লিকেশন পারফরম্যান্স। মাল্টি-মোডাল এবং মাল্টি-মডেল অ্যাপ্লিকেশনগুলির ক্ষেত্রে, আমরা পারফরম্যান্স বলতে বুঝি যে সিস্টেমটি আপনি এবং আপনার ব্যবহারকারীরা প্রত্যাশা করা অনুযায়ী কাজ করে, যার মধ্যে ক্ষতিকারক আউটপুট তৈরি না করাও অন্তর্ভুক্ত। [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ব্যবহার করে আপনার সার্বিক অ্যাপ্লিকেশনের পারফরম্যান্স মূল্যায়ন করা গুরুত্বপূর্ণ। এছাড়াও, আপনার কাছে [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) তৈরি এবং মূল্যায়নের ক্ষমতাও রয়েছে।

আপনি আপনার ডেভেলপমেন্ট পরিবেশে [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ব্যবহার করে আপনার AI অ্যাপ্লিকেশন মূল্যায়ন করতে পারেন। একটি টেস্ট ডেটাসেট বা লক্ষ্য দেওয়া হলে, আপনার generative AI অ্যাপ্লিকেশন থেকে তৈরি ফলাফলগুলি বিল্ট-ইন বা আপনার পছন্দের কাস্টম ইভ্যালুয়েটরের মাধ্যমে পরিমাণগতভাবে মাপা হয়। আপনার সিস্টেম মূল্যায়নের জন্য azure ai evaluation sdk দিয়ে শুরু করতে, আপনি [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) অনুসরণ করতে পারেন। একটি মূল্যায়ন রান সম্পাদনের পর, আপনি [Azure AI Foundry-তে ফলাফলগুলি দেখতে পারেন](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)।

## ট্রেডমার্কস

এই প্রকল্পে প্রকল্প, পণ্য বা পরিষেবার ট্রেডমার্ক বা লোগো থাকতে পারে। Microsoft- এর ট্রেডমার্ক বা লোগোর অনুমোদিত ব্যবহার [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) অনুসরণ করতে হবে এবং সেসবের অধীনেই থাকতে হবে। এই প্রকল্পের পরিবর্তিত সংস্করণে Microsoft ট্রেডমার্ক বা লোগো ব্যবহারে বিভ্রান্তি সৃষ্টি বা Microsoft স্পন্সরশিপ বোঝানো যাবে না। তৃতীয় পক্ষের ট্রেডমার্ক বা লোগোর যে কোনও ব্যবহার সেই তৃতীয় পক্ষের নীতিমালা অনুসরণ করবে।

## সাহায্য নেওয়া

যদি আপনি আটকে যান বা AI অ্যাপ নির্মাণ সম্পর্কে কোনো প্রশ্ন থাকে, তাহলে যোগ দিন:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

যদি আপনার পণ্য সম্পর্কিত মতামত বা সমস্যা থাকে, তাহলে দেখুন:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথি [Co-op Translator](https://github.com/Azure/co-op-translator) নামক AI অনুবাদ সেবার মাধ্যমে অনূদিত হয়েছে। যদিও আমরা নির্ভুলতার জন্য চেষ্টা করি, স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে দয়া করে তা বিবেচনা করুন। মূল নথির নিজস্ব ভাষায় সংস্করণই কর্তৃপক্ষপ্রাপ্ত উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুলবুঝাবুঝি বা গলত অর্থব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->