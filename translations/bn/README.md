<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2e4b490f4bd424b095f21e38c6af33b",
  "translation_date": "2026-01-05T16:35:43+00:00",
  "source_file": "README.md",
  "language_code": "bn"
}
-->
# Phi কুকবুক: Microsoft-এর Phi মডেলের হাতে কলমে উদাহরণ

[![GitHub Codespaces-এ স্যাম্পলস খুলুন এবং ব্যবহার করুন](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers-এ খুলুন](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub অবদানকারীগণ](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ইস্যুগুলো](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub পুল-রিকোয়েস্ট](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs স্বাগত](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub ওয়াচাররা](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub স্টারস](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi হলো Microsoft দ্বারা উন্নত একটি ওপেন সোর্স AI মডেল সিরিজ।

Phi বর্তমানে সবচেয়ে শক্তিশালী এবং খরচ-পরিষ্কার ছোট ভাষার মডেল (SLM), যা বহু ভাষা, যুক্তি, টেক্সট/চ্যাট জেনারেশন, কোডিং, ছবি, অডিও এবং অন্যান্য পরিস্থিতিতে খুব ভাল বেঞ্চমার্ক প্রদর্শন করে।

আপনি Phi ক্লাউডে অথবা এজ ডিভাইসেও ডেপ্লয় করতে পারেন, এবং সীমিত কম্পিউটিং শক্তি ব্যবহার করেও সহজেই জেনারেটিভ AI অ্যাপ্লিকেশন তৈরি করতে পারেন।

এই রিসোর্স ব্যবহার শুরু করার জন্য নিম্নলিখিত ধাপগুলি অনুসরণ করুন:
1. **রিপোজিটোরি ফরকি করুন**: ক্লিক করুন [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **রিপোজিটোরি ক্লোন করুন**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord কমিউনিটিতে যোগ দিন এবং বিশেষজ্ঞ ও অন্যান্য ডেভেলপারদের সাথে পরিচিত হন**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.eb18d1b9605d754b.bn.png)

### 🌐 বহু-ভাষা সমর্থন

#### GitHub Action এর মাধ্যমে সমর্থিত (স্বয়ংক্রিয় এবং সর্বদা আপ-টু-ডেট)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[আরবি](../ar/README.md) | [বাংলা](./README.md) | [বুলগেরিয়ান](../bg/README.md) | [বার্মিজ (মায়ানমার)](../my/README.md) | [চীনা (সরলীকৃত)](../zh/README.md) | [চীনা (প্রথাগত, হংকং)](../hk/README.md) | [চীনা (প্রথাগত, মাকাও)](../mo/README.md) | [চীনা (প্রথাগত, তাইওয়ান)](../tw/README.md) | [ক্রোয়েশিয়ান](../hr/README.md) | [চেক](../cs/README.md) | [ড্যানিশ](../da/README.md) | [ডাচ](../nl/README.md) | [এস্টোনিয়ান](../et/README.md) | [ফিনিশ](../fi/README.md) | [ফরাসি](../fr/README.md) | [জার্মান](../de/README.md) | [গ্রীক](../el/README.md) | [হিব্রু](../he/README.md) | [হিন্দি](../hi/README.md) | [হাঙ্গেরিয়ান](../hu/README.md) | [ইন্দোনেশীয়ান](../id/README.md) | [ইতালিয়ান](../it/README.md) | [জাপানি](../ja/README.md) | [কন্নড়](../kn/README.md) | [কোরিয়ান](../ko/README.md) | [লিথুয়ানিয়ান](../lt/README.md) | [মালয়](../ms/README.md) | [মালায়ালাম](../ml/README.md) | [মারাঠি](../mr/README.md) | [নেপালি](../ne/README.md) | [নাইজেরিয়ান পিডগিন](../pcm/README.md) | [নরওয়েজিয়ান](../no/README.md) | [ফার্সি (পারসি)](../fa/README.md) | [পোলিশ](../pl/README.md) | [পর্তুগিজ (ব্রাজিল)](../br/README.md) | [পর্তুগিজ (পর্তুগাল)](../pt/README.md) | [পাঞ্জাবি (গুরমুখি)](../pa/README.md) | [রোমানিয়ান](../ro/README.md) | [রাশিয়ান](../ru/README.md) | [সার্বিয়ান (সিরিলিক)](../sr/README.md) | [সলভাক](../sk/README.md) | [সলভেনিয়ান](../sl/README.md) | [স্প্যানিশ](../es/README.md) | [সোয়াহিলি](../sw/README.md) | [সুইডিশ](../sv/README.md) | [টাগালগ (ফিলিপিনো)](../tl/README.md) | [তামিল](../ta/README.md) | [তেলুগু](../te/README.md) | [থাই](../th/README.md) | [তুর্কি](../tr/README.md) | [ইউক্রেনিয়ান](../uk/README.md) | [উর্দু](../ur/README.md) | [ভিয়েতনামি](../vi/README.md)

> **লোকালি ক্লোন করতেই চান?**

> এই রিপোজিটোরিতে ৫০+ ভাষার অনুবাদ রয়েছে, যা ডাউনলোড সাইজ অনেক বাড়িয়ে দেয়। অনুবাদগুলি ছাড়া ক্লোন করতে, sparse checkout ব্যবহার করুন:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> এটি আপনাকে অনেক দ্রুত ডাউনলোড সহ কোর্স সম্পন্ন করার জন্য প্রয়োজনীয় সবকিছু দেবে।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## সূচিপত্র

- পরিচিতি
  - [Phi ফ্যামিলিতে স্বাগতম](./md/01.Introduction/01/01.PhiFamily.md)
  - [আপনার পরিবেশ সেটআপ করা](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [মূল প্রযুক্তিগুলো বোঝা](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi মডেলগুলোর জন্য AI নিরাপত্তা](./md/01.Introduction/01/01.AISafety.md)
  - [Phi হার্ডওয়্যার সমর্থন](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi মডেল ও প্ল্যাটফর্ম জুড়ে উপলব্ধতা](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai ও Phi ব্যবহার](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub মার্কেটপ্লেস মডেল](https://github.com/marketplace/models)
  - [Azure AI মডেল ক্যাটালগ](https://ai.azure.com)

- বিভিন্ন পরিবেশে Phi ইনফারেন্স
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub মডেল](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry মডেল ক্যাটালগ](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry লোকাল](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi ফ্যামিলি ইনফারেন্স
    - [iOS-এ Phi ইনফারেন্স](./md/01.Introduction/03/iOS_Inference.md)
    - [অ্যান্ড্রয়েড-এ Phi ইনফারেন্স](./md/01.Introduction/03/Android_Inference.md)
    - [জেটসনে Phi ইনফারেন্স](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC-তে Phi ইনফারেন্স](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX ফ্রেমওয়ার্ক দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/MLX_Inference.md)
    - [লোকাল সার্ভারে Phi ইনফারেন্স](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit ব্যবহার করে রিমোট সার্ভারে Phi ইনফারেন্স](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/Rust_Inference.md)
    - [লোকালে Phi-ভিশন ইনফারেন্স](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (সরকারী সমর্থন) দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi ফ্যামিলি কোয়ান্টিফিকেশন](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp দিয়ে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime এর জন্য Generative AI এক্সটেনশন ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX ফ্রেমওয়ার্ক ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi মূল্যায়ন
    - [দায়িত্বশীল AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry মূল্যায়নের জন্য](./md/01.Introduction/05/AIFoundry.md)
    - [মূল্যায়নের জন্য Promptflow ব্যবহার](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search সহ RAG
    - [Azure AI Search সহ Phi-4-mini এবং Phi-4-multimodal(RAG) ব্যবহার করার উপায়](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi অ্যাপ্লিকেশন উন্নয়ন নমুনাসমূহ
  - টেক্সট ও চ্যাট অ্যাপ্লিকেশনসমূহ
    - Phi-4 নমুনা 🆕
      - [📓] [Phi-4-mini ONNX মডেলের সাথে চ্যাট](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 লোকাল ONNX মডেল .NET দিয়ে চ্যাট](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel ব্যবহার করে Phi-4 ONNX সহ চ্যাট .NET কনসোল অ্যাপ](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 নমুনাসমূহ
      - [ব্রাউজারে Phi3, ONNX Runtime Web এবং WebGPU ব্যবহার করে লোকাল চ্যাটবট](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino চ্যাট](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [মাল্টি মডেল - ইন্টারেক্টিভ Phi-3-mini এবং OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - একটি র‍্যাপার তৈরি করা এবং MLFlow এর সাথে Phi-3 ব্যবহার করা](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [মডেল অপ্টিমাইজেশন - Olive দিয়ে ONNX Runtime Web-এর জন্য Phi-3-min মডেল কীভাবে অপ্টিমাইজ করবেন](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx সহ WinUI3 অ্যাপ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 মাল্টি মডেল AI চালিত নোটস অ্যাপ স্যাম্পল](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [প্রম্পট ফ্লো সহ কাস্টম Phi-3 মডেল ফাইন-টিউন এবং ইন্টিগ্রেট করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry-তে প্রম্পট ফ্লো সহ কাস্টম Phi-3 মডেল ফাইন-টিউন এবং ইন্টিগ্রেট করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft এর রেসপনসিবল AI নীতিমালা কেন্দ্র করে Azure AI Foundry-তে ফাইন-টিউনকৃত Phi-3 / Phi-3.5 মডেলের মূল্যায়ন করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct ভাষা পূর্বানুমান নমুনা (চাইনিজ/ইংরেজি)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG চ্যাটবট](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Phi-3.5-Instruct ONNX সঙ্গে উইন্ডোজ GPU ব্যবহার করে প্রম্পট ফ্লো সলিউশন তৈরি করা](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [মাইক্রোসফট Phi-3.5 tflite ব্যবহার করে অ্যান্ড্রয়েড অ্যাপ তৈরি করা](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [স্থানীয় ONNX Phi-3 মডেল ব্যবহার করে Q&A .NET উদাহরণ Microsoft.ML.OnnxRuntime ব্যবহার করে](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel এবং Phi-3 সহ কনসোল চ্যাট .NET অ্যাপ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK কোড ভিত্তিক স্যাম্পল 
    - Phi-4 স্যাম্পল 🆕
      - [📓] [Phi-4-multimodal ব্যবহার করে প্রকল্প কোড তৈরি করুন](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 স্যাম্পল
      - [মাইক্রোসফট Phi-3 পরিবার দিয়ে নিজের Visual Studio Code GitHub Copilot Chat তৈরি করুন](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub মডেল দিয়ে Phi-3.5 সহ নিজের Visual Studio Code চ্যাট কোপিলট এজেন্ট তৈরি করুন](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - উন্নত যুক্তি স্যাম্পল
    - Phi-4 স্যাম্পল 🆕
      - [📓] [Phi-4-mini-reasoning বা Phi-4-reasoning স্যাম্পল](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive দিয়ে Phi-4-mini-reasoning ফাইন-টিউনিং](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX দিয়ে Phi-4-mini-reasoning ফাইন-টিউনিং](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub মডেল দিয়ে Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry মডেল দিয়ে Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - ডেমো
      - [Phi-4-mini ডেমো Hugging Face Spaces এ হোস্ট করা](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal ডেমো Hugginge Face Spaces এ হোস্ট করা](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - ভিশন স্যাম্পল
    - Phi-4 স্যাম্পল 🆕
      - [📓] [ছবি পড়তে এবং কোড তৈরি করতে Phi-4-multimodal ব্যবহার করুন](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 স্যাম্পল
      -  [📓][Phi-3-vision-ছবির টেক্সট থেকে টেক্সট অনলাইন এন্ডপয়েন্ট](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP এম্বেডিং](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ডেমো: Phi-3 রিসাইক্লিং](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - ভিজ্যুয়াল ভাষা সহকারী - Phi3-Vision এবং OpenVINO সহ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision মাল্টি-ফ্রেম বা মাল্টি-ইমেজ স্যাম্পল](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET ব্যবহার করে Phi-3 Vision স্থানীয় ONNX মডেল](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [মেনু ভিত্তিক Phi-3 Vision স্থানীয় ONNX মডেল Microsoft.ML.OnnxRuntime .NET ব্যবহার করে](../../md/04.HOL/dotnet/src/LabsPhi304)

  - গণিত স্যাম্পল
    -  Phi-4-Mini-Flash-Reasoning-Instruct স্যাম্পল 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct সহ গণিত ডেমো](./md/02.Application/09.Math/MathDemo.ipynb)

  - অডিও স্যাম্পল
    - Phi-4 স্যাম্পল 🆕
      - [📓] [Phi-4-multimodal ব্যবহার করে অডিও ট্রান্সক্রিপ্ট বের করা](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal অডিও স্যাম্পল](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal ভাষণ অনুবাদ স্যাম্পল](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET কনসোল অ্যাপ্লিকেশন যা Phi-4-multimodal অডিও ব্যবহার করে একটি অডিও ফাইল বিশ্লেষণ করে এবং ট্রান্সক্রিপ্ট তৈরি করে](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE স্যাম্পল
    - Phi-3 / 3.5 স্যাম্পল
      - [📓] [Phi-3.5 মিশ্র বিশেষজ্ঞ মডেল (MoEs) সোশ্যাল মিডিয়া স্যাম্পল](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, এবং LlamaIndex দিয়ে রিট্রিভাল-অগমেন্টেড জেনারেশন (RAG) পাইপলাইন তৈরি](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - ফাংশন কলিং স্যাম্পল
    - Phi-4 স্যাম্পল 🆕
      -  [📓] [Phi-4-mini এর সাথে ফাংশন কলিং ব্যবহার](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini দিয়ে মাল্টি-এজেন্ট তৈরি করতে ফাংশন কলিং ব্যবহার](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama এর সাথে ফাংশন কলিং ব্যবহার](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX এর সাথে ফাংশন কলিং ব্যবহার](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - মাল্টিমোডাল মিক্সিং স্যাম্পল
    - Phi-4 স্যাম্পল 🆕
      -  [📓] [Phi-4-multimodal কে একজন প্রযুক্তি সাংবাদিক হিসাবে ব্যবহার করুন](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET কনসোল অ্যাপ্লিকেশন যা Phi-4-multimodal দিয়ে ছবি বিশ্লেষণ করে](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- ফাইন-টিউনিং Phi স্যাম্পল
  - [ফাইন-টিউনিং পরিস্থিতি](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ফাইন-টিউনিং বনাম RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 কে একটি শিল্প বিশেষজ্ঞ হতে দিন ফাইন-টিউনিং](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS কোড এর জন্য AI টুলকিট দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure মেশিন লার্নিং সার্ভিস দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive দিয়ে ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive হ্যান্ডস-অন ল্যাব দিয়ে ফাইন-টিউনিং](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias দিয়ে Phi-3-vision ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX ফ্রেমওয়ার্ক দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision ফাইন-টিউনিং (সরকারী সমর্থন)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers (সরকারী সমর্থন) সহ Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 এবং 3.5 Vision ফাইন-টিউনিং](https://github.com/2U1/Phi3-Vision-Finetune)

- হ্যান্ডস অন ল্যাব
  - [সর্বাধুনিক মডেল গবেষণা: LLM, SLM, স্থানীয় উন্নয়ন এবং আরও অনেক কিছু](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP সম্ভাবনা উন্মোচন: Microsoft Olive দিয়ে ফাইন-টিউনিং](https://github.com/azure/Ignite_FineTuning_workshop)

- একাডেমিক গবেষণা পত্র এবং প্রকাশনা
  - [পাঠ্যপুস্তকগুলি সবই আপনার প্রয়োজন II: phi-1.5 প্রযুক্তিগত প্রতিবেদন](https://arxiv.org/abs/2309.05463)
  - [Phi-3 প্রযুক্তিগত প্রতিবেদন: আপনার ফোনে স্থানীয়ভাবে একটি উচ্চ ক্ষমতাসম্পন্ন ভাষা মডেল](https://arxiv.org/abs/2404.14219)
  - [Phi-4 প্রযুক্তিগত প্রতিবেদন](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini প্রযুক্তিগত প্রতিবেদন: মিশ্রণ-মাধ্যমে LoRAs-এর মাধ্যমে কমপ্যাক্ট কিন্তু শক্তিশালী মাল্টিমোডাল ভাষা মডেলসমূহ](https://arxiv.org/abs/2503.01743)
  - [গাড়ির ভিতরে ফাংশন-কলিং-এর জন্য ছোট ভাষা মডেল অপ্টিমাইজেশন](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) বহু-বিকল্প প্রশ্নোত্তরের জন্য PHI-3 ফাইন-টিউনিং: পদ্ধতি, ফলাফল এবং চ্যালেঞ্জসমূহ](https://arxiv.org/abs/2501.01588)
  - [Phi-4-রিজনিং প্রযুক্তিগত প্রতিবেদন](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-মিনি-রিজনিং প্রযুক্তিগত প্রতিবেদন](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi মডেল ব্যবহার

### Azure AI Foundry-তে Phi

আপনি Microsoft Phi কীভাবে ব্যবহার করবেন এবং কীভাবে আপনার বিভিন্ন হার্ডওয়্যার ডিভাইসে E2E সমাধান তৈরি করবেন তা শিখতে পারেন। Phi নিজে অনুভব করতে, মডেলগুলোর সাথে শুরু করুন এবং আপনার পরিস্থিতির জন্য Phi কাস্টমাইজ করুন [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ব্যবহার করে। আপনি আরও জানতে পারেন Getting Started with [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) থেকে।

**Playground**
প্রতিটি মডেলের জন্য একটি নিবেদিত প্লেগ্রাউন্ড আছে মডেল পরীক্ষা করার জন্য [Azure AI Playground](https://aka.ms/try-phi3)।

### GitHub মডেলে Phi

আপনি Microsoft Phi কীভাবে ব্যবহার করবেন এবং কীভাবে আপনার বিভিন্ন হার্ডওয়্যার ডিভাইসে E2E সমাধান তৈরি করবেন তা শিখতে পারেন। Phi নিজে অনুভব করতে, মডেলের সাথে শুরু করুন এবং আপনার পরিস্থিতির জন্য Phi কাস্টমাইজ করুন [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ব্যবহার করে। আপনি আরও জানতে পারেন Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) থেকে।

**Playground**
প্রতিটি মডেলের জন্য একটি নিবেদিত [প্লেগ্রাউন্ড আছে মডেল পরীক্ষা করার জন্য](/md/02.QuickStart/GitHubModel_QuickStart.md)।

### Hugging Face-এ Phi

আপনি মডেলটি [Hugging Face](https://huggingface.co/microsoft) এ খুঁজেও পেতে পারেন।

**Playground**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 অন্যান্য কোর্সসমূহ

আমাদের দল অন্যান্য কোর্সও তৈরি করে! দেখে নিন:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![শিশুদের জন্য LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![শিশুদের জন্য LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![শিশুদের জন্য AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![শিশুদের জন্য Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![শিশুদের জন্য MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![শিশুদের জন্য AI Agents](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI সিরিজ
[![শিশুদের জন্য Generative AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### মূল শিখন
[![শিশুদের জন্য ML](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![শিশুদের জন্য ডেটা সাইন্স](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![শিশুদের জন্য AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![শিশুদের জন্য সাইবারসিকিউরিটি](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![শিশুদের জন্য ওয়েব ডেভেলপমেন্ট](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![শিশুদের জন্য IoT](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![শিশুদের জন্য XR ডেভেলপমেন্ট](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### কপিলট সিরিজ
[![AI মার্কা প্রোগ্রামিংয়ের জন্য কপিলট](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET জন্য কপিলট](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![কপিলট অ্যাডভেঞ্চার](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## দায়িত্বশীল AI 

Microsoft দায়বদ্ধ আমাদের গ্রাহকদের AI পণ্যগুলি দায়িত্বশীলভাবে ব্যবহার করতে সাহায্য করার জন্য, আমাদের শেখানো বিষয়গুলো শেয়ার করার জন্য, এবং ট্রাস্ট-ভিত্তিক অংশীদারিত্ব নির্মাণ করার জন্য যেমন Transparency Notes এবং Impact Assessments এর মতো টুলস ব্যবহার করে। এই রিসোর্সগুলোর অনেককিছু পাওয়া যায় এখানে [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft এর দায়িত্বশীল AI দৃষ্টিভঙ্গি আমাদের AI নীতি অনুযায়ী যা ন্যায্যতা, নির্ভরযোগ্যতা ও নিরাপত্তা, গোপনীয়তা ও সুরক্ষা, অন্তর্ভুক্তি, স্বচ্ছতা, এবং দায়বদ্ধতার উপর ভিত্তি করে।

বড় আকারের স্বাভাবিক ভাষা, ছবি, এবং ভাষণ মডেলগুলো - যেমন এই উদাহরণে ব্যবহৃত মডেলগুলো - সম্ভবত এমন আচরণ করতে পারে যা ন্যায্য নয়, নির্ভরযোগ্য নয়, অথবা আপত্তিকর হতে পারে, ফলে ক্ষতি ঘটাতে পারে। দয়া করে ঝুঁকি ও সীমাবদ্ধতার তথ্যের জন্য [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) পরামর্শ নিন।

এই ঝুঁকিগুলো কমানোর জন্য প্রস্তাবিত পদ্ধতি হলো আর্কিটেকচারে একটি সুরক্ষা ব্যবস্থা অন্তর্ভুক্ত করা যা ক্ষতিকর আচরণ সনাক্ত এবং প্রতিরোধ করতে পারে। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) একটি স্বাধীন সুরক্ষা স্তর প্রদান করে, যা অ্যাপ্লিকেশন ও সেবায় ক্ষতিকর ইউজার-জেনারেটেড এবং AI-জেনারেটেড কন্টেন্ট সনাক্ত করতে সক্ষম। Azure AI Content Safety টেক্সট এবং ছবি API অন্তর্ভুক্ত করে যা ক্ষতিকর পদার্থ সনাক্ত করতে সাহায্য করে। Azure AI Foundry এর মধ্যে Content Safety সার্ভিসটি আপনাকে বিভিন্ন মোডালিটিতে ক্ষতিকর সামগ্রী সনাক্ত করার জন্য নমুনা কোড দেখার, অনুসন্ধান করার এবং চেষ্টা করার সুযোগ দেয়। নিম্নোক্ত [quickstart ডকুমেন্টেশন](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) আপনাকে সার্ভিসে রিকোয়েস্ট করার নির্দেশনা দেয়।

আরেকটি বিষয় বিবেচনা করতে হবে তা হলো সার্বিক অ্যাপ্লিকেশন পারফরম্যান্স। মাল্টি-মোডাল এবং মাল্টি-মডেল অ্যাপ্লিকেশনগুলোর ক্ষেত্রে, পারফরম্যান্স বলতে আমরা বুঝি যে সিস্টেমটি আপনি এবং আপনার ব্যবহারকারীরা প্রত্যাশা অনুযায়ী কাজ করছে, এর মধ্যে ক্ষতিকর আউটপুট তৈরি না করাও অন্তর্ভুক্ত। আপনার সার্বিক অ্যাপ্লিকেশনের পারফরম্যান্স মূল্যায়ন করা গুরুত্বপূর্ণ [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ব্যবহার করে। এছাড়াও আপনার নিজস্ব [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) তৈরি এবং মূল্যায়ন করার ক্ষমতাও রয়েছে।
আপনি আপনার AI অ্যাপ্লিকেশনটি আপনার উন্নয়ন পরিবেশে [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ব্যবহার করে মূল্যায়ন করতে পারেন। একটি টেস্ট ডেটাসেট অথবা একটি লক্ষ্য দেওয়া হলে, আপনার জেনেরেটিভ AI অ্যাপ্লিকেশন জেনারেশনগুলি অন্তর্নির্মিত মূল্যায়ক বা আপনার পছন্দের কাস্টম মূল্যায়ক ব্যবহার করে পরিমাণগতভাবে মাপা হয়। আপনার সিস্টেম মূল্যায়নের জন্য azure ai evaluation sdk দিয়ে শুরু করতে, আপনি [কুইকস্টার্ট গাইডটি](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) অনুসরণ করতে পারেন। একবার আপনি একটি মূল্যায়ন রান সম্পাদন করলে, আপনি [Azure AI Foundry-তে ফলাফলগুলি ভিজ্যুয়ালাইজ করতে পারেন](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)। 

## ট্রেডমার্কস

এই প্রকল্পটিতে প্রকল্প, পণ্য, বা সেবার ট্রেডমার্ক বা লোগো থাকতে পারে। Microsoft-এর ট্রেডমার্ক বা লোগোর অনুমোদিত ব্যবহার [Microsoft-এর ট্রেডমার্ক ও ব্র্যান্ড গাইডলাইনস](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) অনুসরণ করতে হবে এবং তার অধীনেই থাকবে। এই প্রকল্পের সংশোধিত সংস্করণে Microsoft ট্রেডমার্ক বা লোগোর ব্যবহার বিভ্রান্তি সৃষ্টি করবে না বা Microsoft-এর স্পনসরশিপ বোঝাবে না। তৃতীয় পক্ষের ট্রেডমার্ক বা লোগোর যে কোনও ব্যবহার সেই তৃতীয় পক্ষের নীতিমালা অনুসরণ করবে।

## সাহায্য পাওয়া

যদি আপনি আটকে যান বা AI অ্যাপ তৈরি সম্পর্কে কোনো প্রশ্ন থাকে, তাহলে যোগ দিন:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

আপনি যদি পণ্য প্রতিক্রিয়া বা নির্মাণকালে ত্রুটি পান, তাহলে দেখুন:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে অনুগ্রহ করে মনোযোগ দিন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণের পরামর্শ দেওয়া হয়। এই অনুবাদ ব্যবহারে সৃষ্ট কোনও ভুলবুঝনা বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নয়।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->