# Phi কুকবুক: Microsoft-এর Phi মডেলগুলোর সঙ্গে হাতে কলমে উদাহরণ

[![GitHub Codespaces-এ স্যাম্পলগুলো খুলুন এবং ব্যবহার করুন](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers-এ খুলুন](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub অবদানকারীরা](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub সমস্যা](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub পুল রিকোয়েস্ট](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs স্বাগত](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub ওয়াচার্স](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ফর্কস](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub স্টারস](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi Microsoft কর্তৃক উন্নত একটি ওপেন সোর্স AI মডেল সিরিজ।

Phi বর্তমানে সবচেয়ে শক্তিশালী এবং খরচ-কার্যকর ছোট ভাষা মডেল (SLM), যা বহু-ভাষা, রিজনিং, টেক্সট/চ্যাট সৃষ্টিকরণ, কোডিং, ছবি, অডিও এবং অন্যান্য দৃশ্যপটে খুব ভালো বেঞ্চমার্ক দেখিয়েছে।

আপনি Phi ক্লাউড বা এজ ডিভাইসগুলোতে স্থাপন করতে পারেন, এবং আপনি সীমিত কম্পিউটিং ক্ষমতা দিয়ে সহজে জেনারেটিভ AI অ্যাপ্লিকেশন তৈরি করতে পারবেন।

এই রিসোর্স ব্যবহার শুরু করার জন্য নিচের ধাপগুলো অনুসরণ করুন:
1. **রিপোজিটরি ফর্ক করুন**: ক্লিক করুন [![GitHub ফর্কস](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **রিপোজিটরি ক্লোন করুন**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord কমিউনিটিতে যোগদান করুন এবং বিশেষজ্ঞ এবং সহ-ডেভেলপারদের সাথে পরিচিত হোন**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/bn/cover.eb18d1b9605d754b.webp)

### 🌐 বহু-ভাষা সমর্থন

#### GitHub Action দ্বারা সমর্থিত (স্বয়ংক্রিয় ও সর্বদা আপ-টু-ডেট)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [বাংলা](./README.md) | [বুলগেরিয়ান](../bg/README.md) | [বর্মী (মায়ানমার)](../my/README.md) | [চাইনিজ (সরলীকৃত)](../zh-CN/README.md) | [চাইনিজ (রক্ষণশীল, হংকং)](../zh-HK/README.md) | [চাইনিজ (রক্ষণশীল, ম্যাকাও)](../zh-MO/README.md) | [চাইনিজ (রক্ষণশীল, তাইওয়ান)](../zh-TW/README.md) | [ক্রোয়েশিয়ান](../hr/README.md) | [চেক](../cs/README.md) | [ডেনিশ](../da/README.md) | [ডাচ](../nl/README.md) | [এস্তোনিয়ান](../et/README.md) | [ফিনিশ](../fi/README.md) | [ফরাসি](../fr/README.md) | [জার্মান](../de/README.md) | [গ্রিক](../el/README.md) | [হিব্রু](../he/README.md) | [হিন্দি](../hi/README.md) | [হাঙ্গেরিয়ান](../hu/README.md) | [ইন্দোনেশিয়ান](../id/README.md) | [ইতালিয়ান](../it/README.md) | [জাপানি](../ja/README.md) | [কন্নড়](../kn/README.md) | [কোরিয়ান](../ko/README.md) | [লিথুয়ানিয়ান](../lt/README.md) | [মালয়](../ms/README.md) | [মালায়ালাম](../ml/README.md) | [মারাঠি](../mr/README.md) | [নেপালি](../ne/README.md) | [নাইজেরিয়ান পিডগিন](../pcm/README.md) | [নরওয়েজিয়ান](../no/README.md) | [ফার্সি (পর্শিয়ান)](../fa/README.md) | [পোলিশ](../pl/README.md) | [পর্তুগিজ (ব্রাজিল)](../pt-BR/README.md) | [পর্তুগিজ (পর্তুগাল)](../pt-PT/README.md) | [পাঞ্জাবি (গুরমুখি)](../pa/README.md) | [রোমানিয়ান](../ro/README.md) | [রাশিয়ান](../ru/README.md) | [সার্বিয়ান (সিরিলিক)](../sr/README.md) | [স্লোভাক](../sk/README.md) | [স্লোভেনিয়ান](../sl/README.md) | [স্প্যানিশ](../es/README.md) | [স্বাহিলি](../sw/README.md) | [সুইডিশ](../sv/README.md) | [টাগালগ (ফিলিপিনো)](../tl/README.md) | [তামিল](../ta/README.md) | [তেলুগু](../te/README.md) | [থাই](../th/README.md) | [তুর্কিশ](../tr/README.md) | [ইউক্রেনিয়ান](../uk/README.md) | [উর্দু](../ur/README.md) | [ভিয়েতনামী](../vi/README.md)

> **স্থানীয়ভাবে ক্লোন করতে চান?**

> এই রিপোজিটরিতে ৫০+ ভাষার অনুবাদ অন্তর্ভুক্ত রয়েছে যা ডাউনলোড সাইজ অনেক বৃদ্ধি করে। অনুবাদ ছাড়া ক্লোন করতে sparse checkout ব্যবহার করুন:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> এটি আপনাকে কোর্স সম্পন্ন করার জন্য প্রয়োজনীয় সব কিছু দেবে, অনেক দ্রুত ডাউনলোড সহ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## সূচিপত্র

- পরিচিতি
  - [Phi পরিবারের কাছে স্বাগতম](./md/01.Introduction/01/01.PhiFamily.md)
  - [আপনার পরিবেশ সেটআপ করা](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [প্রধান প্রযুক্তি বোঝা](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi মডেলগুলোর জন্য AI নিরাপত্তা](./md/01.Introduction/01/01.AISafety.md)
  - [Phi হার্ডওয়্যার সমর্থন](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi মডেল এবং বিভিন্ন প্ল্যাটফর্মে উপলভ্যতা](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai এবং Phi ব্যবহার করা](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub মার্কেটপ্লেস মডেলসমূহ](https://github.com/marketplace/models)
  - [Azure AI মডেল ক্যাটালগ](https://ai.azure.com)

- বিভিন্ন পরিবেশে Phi ইনফারেন্স
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub মডেলসমূহ](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry মডেল ক্যাটালগ](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi পরিবারের ইনফারেন্স
    - [iOS-এ Phi ইনফারেন্স](./md/01.Introduction/03/iOS_Inference.md)
    - [অ্যান্ড্রয়েডে Phi ইনফারেন্স](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson-এ Phi ইনফারেন্স](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC-এ Phi ইনফারেন্স](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX ফ্রেমওয়ার্ক সহ Phi ইনফারেন্স](./md/01.Introduction/03/MLX_Inference.md)
    - [লোকাল সার্ভারে Phi ইনফারেন্স](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit ব্যবহার করে রিমোট সার্ভারে Phi ইনফারেন্স](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/Rust_Inference.md)
    - [লোকালে Phi--Vision ইনফারেন্স](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers সহ Phi ইনফারেন্স (সরকারি সমর্থন)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi পরিবারের কোয়ান্টিফাইং](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime-এর জন্য জেনারেটিভ AI এক্সটেনশন ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX ফ্রেমওয়ার্ক ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- মূল্যায়ন Phi
    - [দায়িত্বশীল AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [মূল্যায়নের জন্য Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [মূল্যায়নের জন্য Promptflow ব্যবহার](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI অনুসন্ধানের সঙ্গে RAG
    - [কিভাবে Phi-4-mini এবং Phi-4-multimodal(RAG) Azure AI অনুসন্ধানের সঙ্গে ব্যবহার করবেন](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi অ্যাপ্লিকেশন উন্নয়ন স্যাম্পল
  - টেক্সট ও চ্যাট অ্যাপ্লিকেশনসমূহ
    - Phi-4 স্যাম্পলস 🆕
      - [📓] [Phi-4-mini ONNX মডেলের সঙ্গে চ্যাট](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 লোকাল ONNX মডেলের সঙ্গে .NET চ্যাট](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [সেম্যান্টিক কার্নেল ব্যবহার করে Phi-4 ONNX এর সঙ্গে .NET কনসোল অ্যাপ চ্যাট](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 স্যাম্পলস
      - [ব্রাউজারে Phi3, ONNX Runtime Web এবং WebGPU ব্যবহার করে লোকাল চ্যাটবট](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino চ্যাট](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [মাল্টি মডেল - ইন্টারেক্টিভ ফাই-৩-মিনি এবং ওপেনএআই হুইস্পার](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [এমএলফ্লো - ওয়াকার তৈরি এবং এমএলফ্লোর সঙ্গে ফাই-৩ ব্যবহার](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [মডেল অপ্টিমাইজেশন - অলিভের মাধ্যমে ONNX Runtime Web এর জন্য ফাই-৩- মিন মডেল কীভাবে অপ্টিমাইজ করবেন](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 অ্যাপ সহ ফাই-৩ মিনি-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 মাল্টি মডেল AI চালিত নোটস অ্যাপ স্যাম্পল](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [ফাইন-টিউন এবং প্রম্পট ফ্লোর সাথে কাস্টম ফাই-৩ মডেল ইন্টিগ্রেট করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [অ্যাজুর AI ফাউন্ড্রিতে প্রম্পট ফ্লোর সাথে কাস্টম ফাই-৩ মডেল ফাইন-টিউন এবং ইন্টিগ্রেট করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [অ্যাজুর AI ফাউন্ড্রিতে মাইক্রোসফট-এর রেসপন্সিবল AI নীতিমালার ওপর ফোকাস করে ফাইন-টিউন করা ফাই-৩ / ফাই-৩.৫ মডেল মূল্যায়ন করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [ফাই-৩.৫-মিনি-ইনস্ট্রাক্ট ভাষা পূর্বাভাস নমুনা (চীনা/ইংরেজি)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [ফাই-৩.৫-ইনস্ট্রাক্ট WebGPU RAG চ্যাটবট](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU ব্যবহার করে ফাই-৩.৫-ইনস্ট্রাক্ট ONNX নিয়ে প্রম্পট ফ্লো সলিউশন তৈরি](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [মাইক্রোসফট ফাই-৩.৫ tflite ব্যবহার করে অ্যান্ড্রয়েড অ্যাপ তৈরি](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [স্থানীয় ONNX ফাই-৩ মডেল ব্যবহার করে Microsoft.ML.OnnxRuntime দিয়ে Q&A .NET উদাহরণ](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel এবং ফাই-৩ দিয়ে কনসোল চ্যাট .NET অ্যাপ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI ইনফারেন্স SDK কোড ভিত্তিক স্যাম্পল
    - ফাই-৪ স্যাম্পল 🆕
      - [📓] [ফাই-৪-মাল্টিমডাল ব্যবহার করে প্রজেক্ট কোড তৈরি করুন](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - ফাই-৩ / ৩.৫ স্যাম্পল
      - [মাইক্রোসফট ফাই-৩ পরিবার দিয়ে আপনার নিজস্ব Visual Studio Code GitHub Copilot চ্যাট তৈরি করুন](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub মডেল দিয়ে ফাই-৩.৫ দিয়ে আপনার নিজস্ব Visual Studio Code Chat Copilot এজেন্ট তৈরি করুন](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - উন্নত যুক্তি স্যাম্পল
    - ফাই-৪ স্যাম্পল 🆕
      - [📓] [ফাই-৪-মিনি-রিজনিং অথবা ফাই-৪-রিজনিং স্যাম্পল](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [মাইক্রোসফট অলিভ দিয়ে ফাই-৪-মিনি-রিজনিং ফাইন-টিউনিং](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [অ্যাপল MLX দিয়ে ফাই-৪-মিনি-রিজনিং ফাইন-টিউনিং](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub মডেলের সাথে ফাই-৪-মিনি-রিজনিং](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [অ্যাজুর AI ফাউন্ড্রির মডেলের সাথে ফাই-৪-মিনি-রিজনিং](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - ডেমো
      - [হাগিং ফেস স্পেসে হোস্টকৃত ফাই-৪-মিনি ডেমো](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [হাগিং ফেস স্পেসে হোস্টকৃত ফাই-৪-মাল্টিমডাল ডেমো](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - ভিশন স্যাম্পল
    - ফাই-৪ স্যাম্পল 🆕
      - [📓] [ফাই-৪-মাল্টিমডাল ব্যবহার করে ইমেজ পড়ুন এবং কোড তৈরি করুন](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)
    - ফাই-৩ / ৩.৫ স্যাম্পল
      -  [📓][ফাই-৩-ভিশন-ইমেজ টেক্সট থেকে টেক্সট](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ফাই-৩-ভিশন-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][ফাই-৩-ভিশন ক্লিপ এমবেডিং](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ডেমো: ফাই-৩ রিসাইক্লিং](https://github.com/jennifermarsman/PhiRecycling/)
      - [ফাই-৩-ভিশন - ভিজ্যুয়াল ল্যাংগুয়েজ অ্যাসিস্ট্যান্ট - ফাই3-ভিশন এবং ওপেনভিনো সহ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [ফাই-৩ ভিশন এনভিডিয়া NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [ফাই-৩ ভিশন ওপেনভিনো](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][ফাই-৩.৫ ভিশন মাল্টি-ফ্রেম বা মাল্টি-ইমেজ স্যাম্পল](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET ব্যবহার করে ফাই-৩ ভিশন লোকাল ONNX মডেল](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [মেনু ভিত্তিক ফাই-৩ ভিশন লোকাল ONNX মডেল Microsoft.ML.OnnxRuntime .NET দিয়ে](../../md/04.HOL/dotnet/src/LabsPhi304)

  - গণিত স্যাম্পল
    -  ফাই-৪-মিনি-ফ্ল্যাশ-রিজনিং-ইন্সট্রাক্ট স্যাম্পল 🆕 [ফাই-৪-মিনি-ফ্ল্যাশ-রিজনিং-ইন্সট্রাক্ট সহ গণিত ডেমো](./md/02.Application/09.Math/MathDemo.ipynb)

  - অডিও স্যাম্পল
    - ফাই-৪ স্যাম্পল 🆕
      - [📓] [ফাই-৪-মাল্টিমডাল ব্যবহার করে অডিও ট্রান্সক্রিপ্ট বের করা](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [ফাই-৪-মাল্টিমডাল অডিও স্যাম্পল](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [ফাই-৪-মাল্টিমডাল স্পিচ ট্রান্সলেশন স্যাম্পল](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET কনসোল অ্যাপ্লিকেশন ফাই-৪-মাল্টিমডাল অডিও ব্যবহার করে একটি অডিও ফাইল বিশ্লেষণ ও ট্রান্সক্রিপ্ট তৈরি করতে](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE স্যাম্পল
    - ফাই-৩ / ৩.৫ স্যাম্পল
      - [📓] [ফাই-৩.৫ মিক্সচার অফ এক্সপার্টস মডেল (MoEs) সোশ্যাল মিডিয়া স্যাম্পল](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM ফাই-৩ MOE, অ্যাজুর AI সার্চ এবং LlamaIndex দিয়ে রিট্রিভাল-অগমেন্টেড জেনারেশন (RAG) পাইপলাইন তৈরি](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - ফাংশন কলিং স্যাম্পল
    - ফাই-৪ স্যাম্পল 🆕
      -  [📓] [ফাই-৪-মিনি দিয়ে ফাংশন কলিং ব্যবহার করা](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [ফাই-৪-মিনি দিয়ে মাল্টি-এজেন্ট তৈরি করতে ফাংশন কলিং ব্যবহার](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [ওল্লামার সাথে ফাংশন কলিং ব্যবহার](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX দিয়ে ফাংশন কলিং ব্যবহার](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - মাল্টিমডাল মিক্সিং স্যাম্পল
    - ফাই-৪ স্যাম্পল 🆕
      -  [📓] [ফাই-৪-মাল্টিমডাল প্রযুক্তি সাংবাদিক হিসেবে ব্যবহার](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET কনসোল অ্যাপ্লিকেশন ফাই-৪-মাল্টিমডাল ব্যবহার করে ছবি বিশ্লেষণ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- ফাইন-টিউনিং ফাই স্যাম্পল
  - [ফাইন-টিউনিং সিনারিও](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ফাইন-টিউনিং বনাম RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [ফাইন-টিউনিং ফাই-৩ কে একটি শিল্প বিশেষজ্ঞ বানান](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS কোডের জন্য AI টুলকিট ব্যবহার করে ফাই-৩ ফাইন-টিউনিং](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [অ্যাজুর মেশিন লার্নিং সার্ভিস ব্যবহার করে ফাই-৩ ফাইন-টিউনিং](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora ব্যবহার করে ফাই-৩ ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora ব্যবহার করে ফাই-৩ ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Qlora.md)
  - [অ্যাজুর AI ফাউন্ড্রি ব্যবহার করে ফাই-৩ ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [অ্যাজুর ML CLI/SDK ব্যবহার করে ফাই-৩ ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [মাইক্রোসফট অলিভ দিয়ে ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [মাইক্রোসফট অলিভ হ্যান্ডস-অন ল্যাব দিয়ে ফাইন-টিউনিং](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias দিয়ে ফাই-৩-ভিশন ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [অ্যাপল MLX ফ্রেমওয়ার্ক নিয়ে ফাই-৩ ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MLX.md)
  - [ফাই-৩-ভিশন (সরকারি সাপোর্ট) ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, অ্যাজুর কন্টেইনারস (সরকারি সাপোর্ট) দিয়ে ফাই-৩ ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Kaito.md)
  - [ফাই-৩ এবং ৩.৫ ভিশন ফাইন-টিউনিং](https://github.com/2U1/Phi3-Vision-Finetune)

- হ্যান্ডস-অন ল্যাব
  - [সর্বাধুনিক মডেল অন্বেষণ: LLM, SLM, লোকাল ডেভেলপমেন্ট এবং আরও অনেক কিছু](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [এনএলপি সম্ভাবনা উন্মোচন: মাইক্রোসফট অলিভ দিয়ে ফাইন-টিউনিং](https://github.com/azure/Ignite_FineTuning_workshop)

- একাডেমিক গবেষণা পত্র ও প্রকাশনা
  - [Textbooks Are All You Need II: phi-1.5 প্রযুক্তিগত প্রতিবেদন](https://arxiv.org/abs/2309.05463)
  - [Phi-3 প্রযুক্তিগত প্রতিবেদন: আপনার ফোনে স্থানীয়ভাবে একটি অত্যন্ত সক্ষম ভাষা মডেল](https://arxiv.org/abs/2404.14219)
  - [Phi-4 প্রযুক্তিগত প্রতিবেদন](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini প্রযুক্তিগত প্রতিবেদন: মিক্সচার-অফ-লোআরএএস এর মাধ্যমে কমপ্যাক্ট তবে শক্তিশালী মাল্টিমোডাল ভাষা মডেল](https://arxiv.org/abs/2503.01743)
  - [গাড়ির ভিতরের ফাংশন-কলের জন্য ছোট ভাষা মডেলগুলি অপ্টিমাইজ করা](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) একাধিক-বিকল্প প্রশ্ন উত্তর দেওয়ার জন্য PHI-3 এর ফাইন-টিউনিং: পদ্ধতি, ফলাফল এবং চ্যালেঞ্জ](https://arxiv.org/abs/2501.01588)
  - [Phi-4-তর্ক প্রযুক্তিগত প্রতিবেদন](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-তর্ক প্রযুক্তিগত প্রতিবেদন](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi মডেল ব্যবহার করা

### Azure AI Foundry তে Phi

আপনি শিখতে পারেন কীভাবে Microsoft Phi ব্যবহার করবেন এবং কীভাবে আপনার বিভিন্ন হার্ডওয়্যার ডিভাইসে E2E সমাধান তৈরি করবেন। নিজে Phi অভিজ্ঞতা করতে, শুরু করুন মডেলগুলি নিয়ে খেলতে এবং আপনার ব্যবহার ক্ষেত্রে Phi কাস্টমাইজ করতে [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ব্যবহার করে। আরও জানতে দেখতে পারেন Getting Started with [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Playground**  
প্রতি মডেলের জন্য একটি নিবেদিত প্লেগ্রাউন্ড রয়েছে মডেল পরীক্ষা করার জন্য [Azure AI Playground](https://aka.ms/try-phi3)।

### GitHub মডেলে Phi

আপনি শিখতে পারেন কীভাবে Microsoft Phi ব্যবহার করবেন এবং কীভাবে আপনার বিভিন্ন হার্ডওয়্যার ডিভাইসে E2E সমাধান তৈরি করবেন। নিজে Phi অভিজ্ঞতা করতে, শুরু করুন মডেল নিয়ে খেলতে এবং আপনার ব্যবহার ক্ষেত্রে Phi কাস্টমাইজ করতে [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ব্যবহার করে। আরও জানতে দেখতে পারেন Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**  
প্রতি মডেলের জন্য একটি নিবেদিত [প্লেগ্রাউন্ডে মডেল পরীক্ষা করা হয়](/md/02.QuickStart/GitHubModel_QuickStart.md)।

### Hugging Face তে Phi

আপনি মডেলটি [Hugging Face](https://huggingface.co/microsoft) থেকেও খুঁজে পেতে পারেন।

**Playground**  
[Hugging Chat প্লেগ্রাউন্ড](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 অন্যান্য কোর্স

আমাদের দল অন্যান্য কোর্স তৈরি করে! দেখুন:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain  
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)  
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)  
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)  
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

## জবাবদিহিমূলক AI

Microsoft আমাদের গ্রাহকদের সহায়তা করতে প্রতিশ্রুতিবদ্ধ যাতে তারা আমাদের AI পণ্যগুলি দায়িত্বপূর্ণভাবে ব্যবহার করতে পারেন, আমাদের শেখানো শেয়ার করেন, এবং ট্রাস্ট-ভিত্তিক অংশীদারিত্ব তৈরি করেন Transparency Notes এবং Impact Assessments মত সরঞ্জামের মাধ্যমে। এই রিসোর্সগুলির অনেকগুলো পাওয়া যেতে পারে [https://aka.ms/RAI](https://aka.ms/RAI)।  
Microsoft এর দায়িত্বপূর্ণ AI পন্থা আমাদের AI নীতিমালা - ন্যায়পরায়ণতা, নির্ভরযোগ্যতা এবং নিরাপত্তা, গোপনীয়তা এবং সুরক্ষা, অন্তর্ভুক্তি, স্বচ্ছতা, এবং দায়বদ্ধতার উপর ভিত্তি করে গড়ে উঠেছে।

বৃহৎমাত্রার প্রাকৃতিক ভাষা, ছবি, এবং বক্তৃতা মডেলগুলি - যেমন এই নমুনায় ব্যবহৃত - সম্ভবত অনুপযুক্ত, অবিশ্বাস্য, বা অপমানজনক আচরণ করতে পারে, যার ফলে ক্ষতি হতে পারে। অনুগ্রহ করে ঝুঁকি ও সীমাবদ্ধতা সম্পর্কে জানার জন্য [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) পরামর্শ করুন।

এই ঝুঁকি মোকাবেলার সুপারিশকৃত পদ্ধতি হল আপনার স্থাপত্যে একটি নিরাপত্তা ব্যবস্থা অন্তর্ভুক্ত করা যা ক্ষতিকারক আচরণ সনাক্ত এবং প্রতিরোধ করতে পারে। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) একটি স্বাধীন সুরক্ষা স্তর প্রদান করে, যা অ্যাপ্লিকেশন এবং সেবাগুলিতে ক্ষতিকারক ব্যবহারকারীর তৈরি এবং AI-উত্পাদিত সামগ্রী সনাক্ত করতে সক্ষম। Azure AI Content Safety-তে টেক্সট এবং চিত্র API রয়েছে যা আপনাকে ক্ষতিকারক উপাদান সনাক্ত করতে দেয়। Azure AI Foundry এর মধ্যে, Content Safety সেবা বিভিন্ন মোডালিটি জুড়ে ক্ষতিকারক সামগ্রী সনাক্ত করার জন্য নমুনা কোড দেখতে, পর্যালোচনা করতে এবং চেষ্টা করতে দেয়। নিম্নলিখিত [দ্রুত শুরু ডিজিটাল ডকুমেন্টেশন](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) আপনাকে সেবাটিতে অনুরোধ পাঠানোর জন্য গাইড করে।
আরেকটি দিক বিবেচনায় নেওয়া উচিত হলো সামগ্রিক অ্যাপ্লিকেশন পারফরম্যান্স। মাল্টি-মোডাল এবং মাল্টি-মডেলের অ্যাপ্লিকেশনগুলির ক্ষেত্রে, আমরা পারফরম্যান্সকে বুঝি এমন একটি সিস্টেম যা আপনি এবং আপনার ব্যবহারকারীরা আশা করেন, যার মধ্যে ক্ষতিকারক আউটপুট তৈরি করা অন্তর্ভুক্ত নয়। আপনার সামগ্রিক অ্যাপ্লিকেশনের পারফরম্যান্স মূল্যায়ন করার জন্য [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ব্যবহার করা গুরুত্বপূর্ণ। এছাড়াও, আপনি [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) তৈরি এবং মূল্যায়ন করার সুবিধা পাচ্ছেন।

আপনি আপনার উন্নয়ন পরিবেশে [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ব্যবহার করে আপনার AI অ্যাপ্লিকেশন মূল্যায়ন করতে পারেন। একটি টেস্ট ডেটাসেট বা একটি লক্ষ্য দেওয়া হলে, আপনার জেনারেটিভ AI অ্যাপ্লিকেশনের জেনারেশনগুলি ইনবিল্ট ইভ্যালুয়েটর অথবা আপনার পছন্দসই কাস্টম ইভ্যালুয়েটর দ্বারা পরিমাণগতভাবে পরিমাপ করা হয়। আপনার সিস্টেম মূল্যায়নের জন্য azure ai evaluation sdk দিয়ে শুরু করতে, আপনি [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) অনুসরণ করতে পারেন। একবার আপনি একটি মূল্যায়ন চালিয়ে ফেললে, আপনি [Azure AI Foundry তে ফলাফলগুলি ভিজ্যুয়ালাইজ](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) করতে পারেন।

## ট্রেডমার্কস

এই প্রকল্পে প্রকল্প, পণ্য বা পরিষেবাগুলির জন্য ট্রেডমার্ক বা লোগো থাকতে পারে। Microsoft ট্রেডমার্ক বা লোগোর অনুমোদিত ব্যবহার [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) অনুসারে এবং সে অনুযায়ী হতে হবে।এই প্রকল্পের পরিবর্তিত সংস্করণগুলিতে Microsoft ট্রেডমার্ক বা লোগো ব্যবহারে বিভ্রান্তি সৃষ্টিকারী বা Microsoft স্পনসরশিপ বোঝাপড়ার কারণ হওয়া চলবে না। তৃতীয় পক্ষের ট্রেডমার্ক বা লোগোর কোনও ব্যবহার সেই তৃতীয় পক্ষের নীতিমালা অনুসারে হবে।

## সহায়তা পাওয়া

যদি আপনি আটকা পড়েন বা AI অ্যাপ তৈরি করার বিষয়ে কোনও প্রশ্ন থাকে, তাহলে যোগ দিন:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

যদি আপনার পণ্যের প্রতিক্রিয়া বা ত্রুটি থাকে তখন দেখুন:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা সঠিকতার জন্য চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা ভুল থাকতে পারে বলে অনুগ্রহ করে অবগত থাকুন। নথিটির মূল ভাষার সংস্করণই সর্বাধিক নৈতিক উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহার থেকে উদ্ভূত যেকোনো ভুল বোঝাবুঝি বা ব্যাখ্যাভ্রান্তির জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->