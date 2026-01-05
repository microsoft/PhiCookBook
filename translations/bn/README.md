<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2e4b490f4bd424b095f21e38c6af33b",
  "translation_date": "2026-01-05T01:46:31+00:00",
  "source_file": "README.md",
  "language_code": "bn"
}
-->
# Phi কুকবুক: Microsoft-এর Phi মডেলগুলির সাথে ব্যবহারিক উদাহরণ

[![GitHub Codespaces-এ স্যাম্পল খুলুন এবং ব্যবহার করুন](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers-এ খুলুন](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub অবদানকারী](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ইস্যু](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub পুল-রিকোয়েস্ট](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs স্বাগত](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub পর্যবেক্ষক](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ফর্ক](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub স্টার](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi হল Microsoft দ্বারা উন্নত একটি ওপেন সোর্স AI মডেল সিরিজ।

Phi বর্তমানে সবচেয়ে শক্তিশালী এবং খরচ-কার্যকর স্মল ল্যাঙ্গুয়েজ মডেল (SLM), যা বহু-ভাষা, যুক্তি, টেক্সট/চ্যাট জেনারেশন, কোডিং, ইমেজ, অডিও এবং অন্যান্য পরিস্থিতিতে খুব ভালো বেঞ্চমার্ক দেখায়।

আপনি Phi ক্লাউডে বা এজ ডিভাইসে ডিপ্লয় করতে পারবেন, এবং সীমিত কম্পিউটিং শক্তি দিয়ে সহজেই জেনেরেটিভ AI অ্যাপ্লিকেশন তৈরি করতে পারবেন।

এই রিসোর্সগুলো ব্যবহার শুরু করতে নিম্নলিখিত ধাপগুলো অনুসরণ করুন :
1. **রিপোজিটোরি ফর্ক করুন**: ক্লিক করুন [![GitHub ফর্ক](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **রিপোজিটোরি ক্লোন করুন**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord কমিউনিটিতে যোগ দিন এবং বিশেষজ্ঞ ও সহ-ডেভেলপারদের 만나ুন**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![কভার](../../translated_images/cover.eb18d1b9605d754b.bn.png)

### 🌐 বহুভাষিক সমর্থন

#### GitHub Action দ্বারা সমর্থিত (স্বয়ংক্রিয় ও সর্বদা আপ-টু-ডেট)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[আরবি](../ar/README.md) | [বাংলা](./README.md) | [বুলগেরিয়ান](../bg/README.md) | [বর্মী (মিয়ানমার)](../my/README.md) | [চীনা (সরলীকৃত)](../zh/README.md) | [চীনা (প্রথাগত, হংকং)](../hk/README.md) | [চীনা (প্রথাগত, ম্যাকাও)](../mo/README.md) | [চীনা (প্রথাগত, তাইওয়ান)](../tw/README.md) | [ক্রোয়েশিয়ান](../hr/README.md) | [চেক](../cs/README.md) | [ড্যানিশ](../da/README.md) | [ডাচ](../nl/README.md) | [এস্তোনীয়](../et/README.md) | [ফিনিশ](../fi/README.md) | [ফরাসি](../fr/README.md) | [জার্মান](../de/README.md) | [গ্রিক](../el/README.md) | [হিব্রু](../he/README.md) | [হিন্দি](../hi/README.md) | [হাঙ্গেরীয়](../hu/README.md) | [ইন্দোনেশীয়](../id/README.md) | [ইতালিয়ান](../it/README.md) | [জাপানি](../ja/README.md) | [কন্নড়](../kn/README.md) | [কোরিয়ান](../ko/README.md) | [লিথুয়ানিয়ান](../lt/README.md) | [মালয়](../ms/README.md) | [মালয়ালম](../ml/README.md) | [মরাঠি](../mr/README.md) | [নেপালি](../ne/README.md) | [নাইজেরীয়ান পিজিন](../pcm/README.md) | [নরওয়েজিয়ান](../no/README.md) | [ফার্সি (পার্সি)](../fa/README.md) | [পোলিশ](../pl/README.md) | [পোর্তুগিজ (ব্রাজিল)](../br/README.md) | [পোর্তুগিজ (পর্তুগাল)](../pt/README.md) | [পাঞ্জাবি (গুরমুখী)](../pa/README.md) | [রোমানিয়ান](../ro/README.md) | [রুশ](../ru/README.md) | [সার্বিয়ান (সিরিলিক)](../sr/README.md) | [স্লোভাক](../sk/README.md) | [স্লোভেনীয়](../sl/README.md) | [স্প্যানিশ](../es/README.md) | [সোয়াহিলি](../sw/README.md) | [সুইডিশ](../sv/README.md) | [ট্যাগালগ (ফিলিপিনো)](../tl/README.md) | [তামিল](../ta/README.md) | [তেলুগু](../te/README.md) | [থাই](../th/README.md) | [তুর্কি](../tr/README.md) | [ইউক্রেনীয়](../uk/README.md) | [উর্দু](../ur/README.md) | [ভিয়েতনামি](../vi/README.md)

> **স্থানীয়ভাবে ক্লোন করতে চান?**

> এই রিপোজিটোরিতে 50+ ভাষার অনুবাদ রয়েছে যা ডাউনলোড সাইজ উল্লেখযোগ্যভাবে বাড়ায়। অনুবাদ ছাড়া ক্লোন করার জন্য sparse checkout ব্যবহার করুন:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> এটি আপনাকে দ্রুত ডাউনলোডে কোর্স সম্পন্ন করতে যা প্রয়োজন তা সব দেয়।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## বিষয়সূচি

- ভূমিকা
  - [Phi পরিবারের স্বাগতম](./md/01.Introduction/01/01.PhiFamily.md)
  - [আপনার পরিবেশ সেটআপ করা](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [মূল প্রযুক্তি বোঝা](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi মডেলগুলির জন্য AI নিরাপত্তা](./md/01.Introduction/01/01.AISafety.md)
  - [Phi হার্ডওয়্যার সমর্থন](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi মডেলসমূহ ও প্ল্যাটফর্ম জুড়ে উপলভ্যতা](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai এবং Phi ব্যবহার করা](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace মডেলসমূহ](https://github.com/marketplace/models)
  - [Azure AI মডেল ক্যাটালগ](https://ai.azure.com)

- বিভিন্ন পরিবেশে Phi ইনফারেন্স
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub মডেলস](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry মডেল ক্যাটালগ](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI টুলকিট VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi পরিবারে ইনফারেন্স
    - [iOS-এ Phi ইনফারেন্স](./md/01.Introduction/03/iOS_Inference.md)
    - [Android-এ Phi ইনফারেন্স](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson-এ Phi ইনফারেন্স](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC-এ Phi ইনফারেন্স](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework ব্যবহার করে Phi ইনফারেন্স](./md/01.Introduction/03/MLX_Inference.md)
    - [লোকাল সার্ভারে Phi ইনফারেন্স](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit ব্যবহার করে রিমোট সার্ভারে Phi ইনফারেন্স](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/Rust_Inference.md)
    - [লোকালে Phi -- ভিশন ইনফারেন্স](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (আধিকৃত সমর্থন) দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi পরিবারের পরিমাণগত বিশ্লেষণ](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Generative AI extensions for onnxruntime ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi মূল্যায়ন
    - [দায়িত্বশীল AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [মূল্যায়নের জন্য Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [মূল্যায়নের জন্য Promptflow ব্যবহার করা](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search-এর সাথে RAG
    - [Phi-4-mini এবং Phi-4-multimodal(RAG) কীভাবে Azure AI Search-এর সাথে ব্যবহার করবেন](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi অ্যাপ্লিকেশন ডেভেলপমেন্ট স্যাম্পলসমূহ
  - টেক্সট ও চ্যাট অ্যাপ্লিকেশন
    - Phi-4 স্যাম্পলস 🆕
      - [📓] [Phi-4-mini ONNX মডেলের সাথে চ্যাট করুন](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 লোকাল ONNX মডেলের সাথে চ্যাট (.NET)](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel ব্যবহার করে Phi-4 ONNX সহ Chat .NET কনসোল অ্যাপ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 স্যাম্পলস
      - [Phi3, ONNX Runtime Web এবং WebGPU ব্যবহার করে ব্রাউজারে লোকাল চ্যাটবট](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVINO চ্যাট](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [মাল্টি মডেল - ইন্টারঅ্যাকটিভ Phi-3-mini এবং OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - একটি র‍্যাপার নির্মাণ এবং Phi-3 কে MLFlow দিয়ে ব্যবহার করা](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [মডেল অপ্টিমাইজেশন - Olive ব্যবহার করে ONNX Runtime Web এর জন্য Phi-3-min মডেল কিভাবে অপ্টিমাইজ করবেন](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 অ্যাপ Phi-3 mini-4k-instruct-onnx সহ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 মাল্টি মডেল AI-চালিত নোটস অ্যাপ স্যাম্পল](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [ফাইন-টিউন এবং কাস্টম Phi-3 মডেলগুলিকে Prompt flow এর সাথে ইন্টিগ্রেট করা](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry তে Prompt flow দিয়ে কাস্টম Phi-3 মডেলগুলোকে ফাইন-টিউন এবং ইন্টিগ্রেট করা](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft-এর Responsible AI নীতির উপর গুরুত্ব দিয়ে Azure AI Foundry-তে ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেল মূল্যায়ন করা](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct ভাষা পূর্বাভাস স্যাম্পল (চীনা/ইংরেজি)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG চ্যাটবট](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU ব্যবহার করে Phi-3.5-Instruct ONNX দিয়ে Prompt flow সলিউশন তৈরি করা](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite ব্যবহার করে Android অ্যাপ তৈরি করা](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET উদাহরণ যা স্থানীয় ONNX Phi-3 মডেল এবং Microsoft.ML.OnnxRuntime ব্যবহার করে](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel এবং Phi-3 সহ কনসোল চ্যাট .NET অ্যাপ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK Code Based Samples 
    - Phi-4 স্যাম্পলসমূহ 🆕
      - [📓] [Phi-4-multimodal ব্যবহার করে প্রজেক্ট কোড জেনারেট করা](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 স্যাম্পলসমূহ
      - [Microsoft Phi-3 Family দিয়ে আপনার নিজস্ব Visual Studio Code GitHub Copilot Chat তৈরি করা](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub Models দ্বারা Phi-3.5 ব্যবহার করে আপনার নিজস্ব Visual Studio Code Chat Copilot Agent তৈরি করা](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - উন্নত রিজনিং স্যাম্পলসমূহ
    - Phi-4 স্যাম্পলসমূহ 🆕
      - [📓] [Phi-4-mini-reasoning বা Phi-4-reasoning স্যাম্পলসমূহ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive দিয়ে Phi-4-mini-reasoning ফাইন-টিউন করা](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX দিয়ে Phi-4-mini-reasoning ফাইন-টিউন করা](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub Models দিয়ে Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry Models দিয়ে Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demos
      - [Phi-4-mini ডেমোসমূহ Hugging Face Spaces-এ হোস্ট করা হয়েছে](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal ডেমোসমূহ Hugginge Face Spaces-এ হোস্ট করা হয়েছে](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Vision Samples
    - Phi-4 স্যাম্পলসমূহ 🆕
      - [📓] [Phi-4-multimodal ব্যবহার করে ছবিসমূহ পড়া ও কোড তৈরি করা](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 স্যাম্পলসমূহ
      -  [📓][Phi-3-vision- ইমেজ টেক্সট টু টেক্সট](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP এমবেডিং](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 রিসাইক্লিং](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - ভিজ্যুয়াল ভাষা অ্যাসিস্ট্যান্ট - Phi3-Vision এবং OpenVINO সহ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision মাল্টি-ফ্রেম বা মাল্টি-ইমেজ স্যাম্পল](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision লোকাল ONNX মডেল Microsoft.ML.OnnxRuntime .NET ব্যবহার করে](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [মেনু-ভিত্তিক Phi-3 Vision লোকাল ONNX মডেল Microsoft.ML.OnnxRuntime .NET ব্যবহার করে](../../md/04.HOL/dotnet/src/LabsPhi304)

  - গণিত স্যাম্পলসমূহ
    -  Phi-4-Mini-Flash-Reasoning-Instruct স্যাম্পলসমূহ 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct সহ ম্যাথ ডেমো](./md/02.Application/09.Math/MathDemo.ipynb)

  - অডিও স্যাম্পলসমূহ
    - Phi-4 স্যাম্পলসমূহ 🆕
      - [📓] [Phi-4-multimodal ব্যবহার করে অডিও ট্রান্সক্রিপ্ট বের করা](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal অডিও স্যাম্পল](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal স্পিচ ট্রান্সলেশন স্যাম্পল](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET কনসোল অ্যাপ Phi-4-multimodal অডিও ব্যবহার করে একটি অডিও ফাইল বিশ্লেষণ এবং ট্রান্সক্রিপ্ট জেনারেট করে](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE স্যাম্পলসমূহ
    - Phi-3 / 3.5 স্যাম্পলসমূহ
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) সামাজিক মিডিয়া স্যাম্পল](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, এবং LlamaIndex দিয়ে Retrieval-Augmented Generation (RAG) পাইপলাইন তৈরি করা](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - ফাংশন কলিং স্যাম্পলসমূহ
    - Phi-4 স্যাম্পলসমূহ 🆕
      -  [📓] [Phi-4-mini-এ ফাংশন কলিং ব্যবহার করা](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini দিয়ে মাল্টি-এজেন্ট তৈরি করতে ফাংশন কলিং ব্যবহার করা](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama সহ ফাংশন কলিং ব্যবহার করা](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX সহ ফাংশন কলিং ব্যবহার করা](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - মাল্টিমডাল মিশ্রণ স্যাম্পলসমূহ
    - Phi-4 স্যাম্পলসমূহ 🆕
      -  [📓] [Phi-4-multimodal একজন প্রযুক্তি সাংবাদিক হিসেবে ব্যবহার করা](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET কনসোল অ্যাপ Phi-4-multimodal ব্যবহার করে ছবিসমূহ বিশ্লেষণ করে](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- ফাইন-টিউনিং Phi স্যাম্পলসমূহ
  - [ফাইন-টিউনিং সিনারিওস](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ফাইন-টিউনিং বনাম RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [ফাইন-টিউনিং: Phi-3 কে একটি ইন্ডাস্ট্রি এক্সপার্ট বানান](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [AI Toolkit for VS Code দিয়ে Phi-3 ফাইন-টিউন করা](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service দিয়ে Phi-3 ফাইন-টিউন করা](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora দিয়ে Phi-3 ফাইন-টিউন করা](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora দিয়ে Phi-3 ফাইন-টিউন করা](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry দিয়ে Phi-3 ফাইন-টিউন করা](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK দিয়ে Phi-3 ফাইন-টিউন করা](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive দিয়ে ফাইন-টিউন করা](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive হ্যান্ডস-অন ল্যাব দিয়ে ফাইন-টিউনিং](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias দিয়ে Phi-3-vision ফাইন-টিউন করা](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework ব্যবহার করে Phi-3 ফাইন-টিউন করা](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision ফাইন-টিউন (অফিশিয়াল সাপোর্ট)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers দিয়ে Phi-3 ফাইন-টিউন (অফিশিয়াল সাপোর্ট)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 এবং 3.5 Vision ফাইন-টিউন](https://github.com/2U1/Phi3-Vision-Finetune)

- হ্যান্ডস-অন ল্যাব
  - [অত্যাধুনিক মডেলগুলো অন্বেষণ: LLMs, SLMs, লোকাল ডেভেলপমেন্ট এবং আরও](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP সম্ভাবনা উন্মোচন: Microsoft Olive দিয়ে ফাইন-টিউনিং](https://github.com/azure/Ignite_FineTuning_workshop)

- একাডেমিক গবেষণা পেপার এবং প্রকাশনা
  - [টেক্সটবুকস আর অল ইউ নিড II: phi-1.5 প্রযুক্তিগত রিপোর্ট](https://arxiv.org/abs/2309.05463)
  - [Phi-3 প্রযুক্তিগত রিপোর্ট: আপনার ফোনে স্থানীয়ভাবে একটি উচ্চ সক্ষমতা সম্পন্ন ভাষা মডেল](https://arxiv.org/abs/2404.14219)
  - [Phi-4 প্রযুক্তিগত রিপোর্ট](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini প্রযুক্তিগত রিপোর্ট: Mixture-of-LoRAs এর মাধ্যমে সংক্ষিপ্ত কিন্তু শক্তিশালী মাল্টিমডাল ভাষা মডেল](https://arxiv.org/abs/2503.01743)
  - [ইন-ভেহিকল ফাংশন-কলিংয়ের জন্য ছোট ভাষা মডেল অপ্টিমাইজ করা](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 কে বহুনির্বাচনী প্রশ্নোত্তর জন্য ফাইন-টিউন করা: পদ্ধতি, ফলাফল, এবং চ্যালেঞ্জসমূহ](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning প্রযুক্তিগত রিপোর্ট](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning প্রযুক্তিগত রিপোর্ট](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi মডেল ব্যবহার

### Azure AI Foundry-এ Phi

আপনি শিখতে পারবেন কিভাবে Microsoft Phi ব্যবহার করতে হয় এবং কিভাবে আপনার বিভিন্ন হার্ডওয়্যার ডিভাইসে E2E সমাধান তৈরি করতে হয়। Phi নিজে দিয়ে অভিজ্ঞতা অর্জন করতে, মডেলগুলোর সাথে খেলতে এবং আপনার সিনারিওর জন্য Phi কাস্টমাইজ করতে শুরু করুন [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ব্যবহার করে। আপনি আরও জানতে পারেন Getting Started with [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**প্লেগ্রাউন্ড**
প্রতিটি মডেলের মডেল পরীক্ষা করার জন্য একটি বিশেষ প্লেগ্রাউন্ড রয়েছে [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub মডেলগুলিতে Phi

আপনি শিখতে পারবেন কিভাবে Microsoft Phi ব্যবহার করতে হয় এবং কিভাবে আপনার বিভিন্ন হার্ডওয়্যার ডিভাইসে E2E সমাধান তৈরি করতে হয়। Phi নিজে দিয়ে অভিজ্ঞতা অর্জন করতে, মডেলের সাথে খেলতে এবং আপনার সিনারিওর জন্য Phi কাস্টমাইজ করতে শুরু করুন [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ব্যবহার করে। আপনি আরও জানতে পারেন Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**প্লেগ্রাউন্ড**
প্রতিটি মডেলের একটি নিবেদিত [মডেল পরীক্ষা করার প্লেগ্রাউন্ড](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Hugging Face-এ Phi

আপনি মডেলটি [Hugging Face](https://huggingface.co/microsoft) থেকেও খুঁজে পেতে পারেন

**প্লেগ্রাউন্ড**
 [Hugging Chat প্লেগ্রাউন্ড](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 অন্যান্য কোর্স

Our team produces other courses! Check out:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j নবীনদের জন্য](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js নবীনদের জন্য](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD নবীনদের জন্য](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI নবীনদের জন্য](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP নবীনদের জন্য](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents নবীনদের জন্য](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![Generative AI নবীনদের জন্য](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Core Learning
[![ML নবীনদের জন্য](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science নবীনদের জন্য](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI নবীনদের জন্য](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![সাইবারসিকিউরিটি নবীনদের জন্য](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![ওয়েব ডেভ নবীনদের জন্য](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT নবীনদের জন্য](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR ডেভেলপমেন্ট নবীনদের জন্য](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Series
[![AI Paired Programming-এর জন্য Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET-এর জন্য Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot অ্যাডভেঞ্চার](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## দায়িত্বশীল AI 
Microsoft আমাদের গ্রাহকদের আমাদের AI পণ্যগুলি দায়িত্বশীলভাবে ব্যবহার করতে সাহায্য করতে প্রতিশ্রুতিবদ্ধ, আমাদের শিক্ষাগুলি শেয়ার করা, এবং Transparency Notes এবং Impact Assessments-এর মতো টুলগুলোর মাধ্যমে বিশ্বাসভিত্তিক অংশীদারিত্ব নির্মাণ করা। এই সংস্থানগুলোর অনেকগুলি [https://aka.ms/RAI](https://aka.ms/RAI) এ পাওয়া যাবে।
Microsoft-এর দায়িত্বশীল AI নীতি আমাদের AI নীতিগুলোর ওপর ভিত্তি করে—ন্যায়, নির্ভরযোগ্যতা এবং নিরাপত্তা, গোপনীয়তা এবং সুরক্ষা, অন্তর্ভুক্তি, স্বচ্ছতা, এবং একাউন্টেবিলিটি।

বৃহৎ-স্কেলের প্রাকৃতিক ভাষা, চিত্র, এবং স্পিচ মডেলগুলি — যেমন এই নমুনায় ব্যবহৃত মডেলগুলো — সম্ভাব্যভাবে এমনভাবে আচরণ করতে পারে যা অন্যায়, অবিশ্বস্ত, বা আপত্তিকর হতে পারে, এবং ফলে ক্ষতি ঘটতে পারে। ঝুঁকি ও সীমাবদ্ধতা সম্পর্কে পরিচিত হতে অনুগ্রহ করে [Azure OpenAI পরিষেবার স্বচ্ছতা নোট](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) দেখুন।

এই ঝুঁকিগুলো হ্রাস করার জন্য প্রস্তাবিত পদ্ধতি হলো আপনার আর্কিটেকচারে একটি সেফটি সিস্টেম অন্তর্ভুক্ত করা যা ক্ষতিকর আচরণ সনাক্ত এবং প্রতিরোধ করতে পারে। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) একটি স্বাধীন সুরক্ষা স্তর প্রদান করে, যা অ্যাপ্লিকেশন এবং সার্ভিসগুলোতে ক্ষতিকর ব্যবহারকারী-উত্পাদিত এবং AI-উত্পাদিত সামগ্রী সনাক্ত করতে সক্ষম। Azure AI Content Safety টেক্সট এবং ছবি API অন্তর্ভুক্ত করে যা আপনাকে ক্ষতিকর উপাদান সনাক্ত করতে দেয়। Azure AI Foundry-র মধ্যে, Content Safety সার্ভিস আপনাকে বিভিন্ন মডালিটির মধ্যে ক্ষতিকর সামগ্রী সনাক্ত করার জন্য উদাহরণ কোড দেখতে, অন্বেষণ করতে এবং চেষ্টা করে দেখার সুযোগ দেয়। নিম্নলিখিত [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) আপনাকে সার্ভিসটিতে অনুরোধ পাঠানোর মাধ্যমে গাইড করবে।

আরেকটি বিষয় যা বিবেচনা করতে হবে তা হলো সামগ্রিক অ্যাপ্লিকেশনের কার্যক্ষমতা। মাল্টি-মডাল এবং মাল্টি-মডেল অ্যাপ্লিকেশনগুলির ক্ষেত্রে, আমরা কার্যক্ষমতা বলতে বোঝায় যে সিস্টেমটি আপনার এবং আপনার ব্যবহারকারীদের প্রত্যাশা অনুযায়ী কাজ করে, যার মধ্যে ক্ষতিকর আউটপুট তৈরি না করাও অন্তর্ভুক্ত। আপনার সামগ্রিক অ্যাপ্লিকেশনটির কার্যক্ষমতা মূল্যায়ন করা গুরুত্বপূর্ণ [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ব্যবহার করে। আপনার কাছে [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) তৈরি এবং মূল্যায়ন করার ক্ষমতাও রয়েছে।
আপনি আপনার ডেভেলপমেন্ট পরিবেশে [Azure AI মূল্যায়ন SDK](https://microsoft.github.io/promptflow/index.html) ব্যবহার করে আপনার AI অ্যাপ্লিকেশন মূল্যায়ন করতে পারেন। একটি টেস্ট ডেটাসেট বা একটি লক্ষ্য প্রদান করলে, আপনার জেনারেটিভ AI অ্যাপ্লিকেশন থেকে তৈরি ফলাফলগুলি বিল্ট-ইন ইভ্যালুয়েটর অথবা আপনার পছন্দের কাস্টম ইভ্যালুয়েটর দিয়ে পরিমাণগতভাবে পরিমাপ করা হয়। আপনার সিস্টেম মূল্যায়ন শুরু করতে [দ্রুত শুরু নির্দেশিকা](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) অনুসরণ করতে পারেন। একবার আপনি একটি মূল্যায়ন রান চালালে, আপনি [Azure AI Foundry-এ ফলাফল ভিজ্যুয়ালাইজ করতে পারেন](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)। 

## ট্রেডমার্ক

এই প্রকল্পে প্রকল্প, পণ্য, বা পরিষেবাগুলোর ট্রেডমার্ক বা লোগো থাকতে পারে। Microsoft ট্রেডমার্ক বা লোগো ব্যবহারের অনুমোদিত শর্তাবলী [Microsoft-এর ট্রেডমার্ক ও ব্র্যান্ড নির্দেশিকা](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) অনুযায়ী হতে হবে এবং তা অনুসরণ করা আবশ্যক।
এই প্রকল্পের পরিবর্তিত সংস্করণে Microsoft ট্রেডমার্ক বা লোগো ব্যবহারে বিভ্রান্তি সৃষ্টি করা যাবে না বা Microsoft-এর স্পনসরশিপ বোঝাতে পারবে না। তৃতীয় পক্ষের ট্রেডমার্ক বা লোগো ব্যবহারের ক্ষেত্রে সেই তৃতীয় পক্ষের নীতিমালা প্রযোজ্য হবে।

## সহায়তা

যদি আপনি আটকে যান বা AI অ্যাপ তৈরি সম্পর্কে কোনো প্রশ্ন থাকে, যোগ দিন:

[![Azure AI Foundry ডিসকর্ড](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

যদি আপনার পণ্য সম্পর্কিত প্রতিক্রিয়া থাকে বা বিল্ড করার সময় ত্রুটি দেখা দেয় তাহলে দেখুন:

[![Azure AI Foundry ডেভেলপার ফোরাম](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
অস্বীকৃতি:
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। যদিও আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, অনুগ্রহ করে মাথায় রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা ভুল থাকতে পারে। মূল নথিটি তার নিজ ভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের ক্ষেত্রে পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হচ্ছে। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট যে কোনো ভুলবোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->