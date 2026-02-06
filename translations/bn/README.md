# Phi রন্ধনপ্রণালী: Microsoft এর Phi মডেলগুলির সঙ্গে হাতে-কলমে উদাহরণসমূহ

[![GitHub Codespaces-এ স্যাম্পলগুলো খুলুন ও ব্যবহার করুন](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers-এ খুলুন](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub সহযোদ্ধারা](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ইস্যুগুলো](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub পুল-রিকোয়েস্টস](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR-গুলি স্বাগত](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub ওয়াচাররা](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ফর্কস](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub তারকাসমূহ](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry ডিসকর্ড](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi হল Microsoft কর্তৃক উন্নত একটি সিরিজের ওপেন সোর্স AI মডেল। 

Phi বর্তমানে সবচেয়ে শক্তিশালী এবং খরচ-সাশ্রয়ী ছোট ভাষা মডেল (SLM), যার বহুভাষিক, যুক্তিবিদ্যা, টেক্সট/চ্যাট জেনারেশন, কোডিং, ছবি, অডিও এবং অন্যান্য পরিস্থিতিতে খুবই ভালো বেঞ্চমার্ক রয়েছে। 

আপনি Phi-কে ক্লাউডে বা এজ ডিভাইসগুলোতে ডেপ্লয় করতে পারেন, এবং সীমিত কম্পিউটিং ক্ষমতা নিয়ে সহজেই জেনারেটিভ AI অ্যাপ্লিকেশন তৈরি করতে পারেন।

এই উপাদানগুলো ব্যবহার শুরু করার জন্য নিম্নলিখিত পদক্ষেপগুলো অনুসরণ করুন:
1. **রিপোজিটরি ফর্ক করুন**: ক্লিক করুন [![GitHub ফর্কস](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **রিপোজিটরি ক্লোন করুন**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI ডিসকর্ড কমিউনিটিতে যোগ দিন এবং বিশেষজ্ঞ ও অন্যান্য ডেভেলপারদের সাথে মিলিত হোন**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/bn/cover.eb18d1b9605d754b.webp)

### 🌐 বহুভাষিক সহায়তা

#### GitHub Action-এর মাধ্যমে সমর্থিত (স্বয়ংক্রিয় এবং সর্বদা আপ-টু-ডেট)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](./README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **স্থানীয়ভাবে ক্লোন করতে চান?**

> এই রিপোজিটরিতে ৫০+ ভাষার অনুবাদ রয়েছে যা ডাউনলোড আকার অনেক বৃদ্ধি করে। অনুবাদ ছাড়া ক্লোন করতে sparse checkout ব্যবহার করুন:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> এটা আপনাকে কোর্স শেষ করার জন্য সবকিছু দ্রুত ডাউনলোড দেয়।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## বিষয়সূচী

- পরিচিতি
  - [Phi পরিবারের স্বাগতম](./md/01.Introduction/01/01.PhiFamily.md)
  - [আপনার পরিবেশ সেটআপ](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [প্রধান প্রযুক্তিগুলি বোঝা](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi মডেলগুলির জন্য AI নিরাপত্তা](./md/01.Introduction/01/01.AISafety.md)
  - [Phi হার্ডওয়্যার সমর্থন](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi মডেল ও প্ল্যাটফর্মে উপলব্ধতা](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai ও Phi ব্যবহার](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace মডেলসমূহ](https://github.com/marketplace/models)
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
    - [Android-এ Phi ইনফারেন্স](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson-এ Phi ইনফারেন্স](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC-তে Phi ইনফারেন্স](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX ফ্রেমওয়ার্ক দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/MLX_Inference.md)
    - [স্থানীয় সার্ভারে Phi ইনফারেন্স](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit ব্যবহার করে রিমোট সার্ভারে Phi ইনফারেন্স](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/Rust_Inference.md)
    - [স্থানীয়ভাবে Phi--Vision ইনফারেন্স](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (অফিসিয়াল সাপোর্ট) দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi পরিবারের কোয়ান্টিফিকেশন](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime-এর জন্য জেনারেটিভ AI এক্সটেনশন্স ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX ফ্রেমওয়ার্ক ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজিং](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi মূল্যায়ন
    - [Responsible AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [মুল্যায়নের জন্য Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [মুল্যায়নের জন্য Promptflow ব্যবহার](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search সহ RAG
    - [Phi-4-mini এবং Phi-4-multimodal(RAG) Azure AI Search সঙ্গে ব্যবহার](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi অ্যাপ্লিকেশন ডেভেলপমেন্ট স্যাম্পলস
  - টেক্সট এবং চ্যাট অ্যাপ্লিকেশনস
    - Phi-4 স্যাম্পলস 🆕
      - [📓] [Phi-4-mini ONNX মডেলের সাথে চ্যাট](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 লোকাল ONNX মডেল .NET সহ চ্যাট](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel ব্যবহার করে Phi-4 ONNX সহ .NET কনসোল অ্যাপ চ্যাট](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 স্যাম্পলস
      - [Phi3, ONNX Runtime Web এবং WebGPU ব্যবহার করে ব্রাউজারে লোকাল চ্যাটবট](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino চ্যাট](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [মাল্টি মডেল - ইন্টারেক্টিভ ফাই-৩-মিনি এবং ওপেনএআই হুইসপার](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [এমএলফ্লো - র‍্যাপার তৈরি এবং Phi-3 এর সাথে এমএলফ্লো ব্যবহার](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [মডেল অপটিমাইজেশন - অলিভের সাথে ONNX রানটাইম ওয়েবের জন্য Phi-3-মিন মডেল কীভাবে অপ্টিমাইজ করবেন](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 মিনি-4k-ইন্সট্রাক্ট-অনক্স দিয়ে WinUI3 অ্যাপ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 মাল্টি মডেল এআই চালিত নোটস অ্যাপ স্যাম্পল](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [কাস্টম Phi-3 মডেলগুলি ফাইন-টিউন এবং প্রম্পট ফ্লোতে ইন্টিগ্রেট করা](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [কাস্টম Phi-3 মডেলগুলি Azure AI Foundry তে প্রম্পট ফ্লো সহ ফাইন-টিউন এবং ইন্টিগ্রেট করা](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Azure AI Foundry তে মাইক্রোসফটের রেসপনসিবল AI নীতিমালার উপর মনোযোগ দিয়ে ফাইন-টিউন্ড Phi-3 / Phi-3.5 মডেল মূল্যায়ন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-মিনি-ইন্সট্রাক্ট ভাষা ভবিষ্যদ্বাণী নমুনা (চীনা/ইংরেজি)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-ইন্সট্রাক্ট ওয়েবজিপিইউ RAG চ্যাটবট](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [উইন্ডোজ GPU ব্যবহার করে Phi-3.5-ইন্সট্রাক্ট ONNX সহ প্রম্পট ফ্লো সলিউশন তৈরি](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [মাইক্রোসফট Phi-3.5 tflite ব্যবহার করে অ্যান্ড্রয়েড অ্যাপ তৈরি](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime ব্যবহার করে স্থানীয় ONNX Phi-3 মডেল দিয়ে প্রশ্নোত্তর .NET উদাহরণ](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [সেমনটিক কার্নেল এবং Phi-3 সহ কনসোল চ্যাট .NET অ্যাপ](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI ইনফারেন্স SDK কোড ভিত্তিক নমুনা
    - Phi-4 নমুনা 🆕
      - [📓] [Phi-4-মাল্টিমোডাল ব্যবহার করে প্রকল্প কোড তৈরি করুন](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 নমুনা
      - [মাইক্রোসফট Phi-3 পরিবারের সাথে আপনার নিজের Visual Studio Code GitHub Copilot Chat তৈরি করুন](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub মডেল সহ Phi-3.5 দিয়ে আপনার নিজের Visual Studio Code Chat Copilot Agent তৈরি করুন](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - উন্নত যুক্তি নমুনা
    - Phi-4 নমুনা 🆕
      - [📓] [Phi-4-মিনি-যুক্তি বা Phi-4 যুক্তি নমুনা](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [মাইক্রোসফট অলিভ দিয়ে Phi-4-মিনি-যুক্তি ফাইন-টিউনিং](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [অ্যাপল MLX দিয়ে Phi-4-মিনি-যুক্তি ফাইন-টিউনিং](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub মডেল সহ Phi-4-মিনি-যুক্তি](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry মডেল সহ Phi-4-মিনি-যুক্তি](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - ডেমো
      - [Hugging Face Spaces এ হোস্ট করা Phi-4-মিনি ডেমো](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Hugginge Face Spaces এ হোস্ট করা Phi-4-মাল্টিমোডাল ডেমো](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - ভিশন নমুনা
    - Phi-4 নমুনা 🆕
      - [📓] [Phi-4-মাল্টিমোডাল ব্যবহার করে ছবি পড়ুন এবং কোড তৈরি করুন](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)
    - Phi-3 / 3.5 নমুনা
      -  [📓][Phi-3-ভিশন-ইমেজ টেক্সট টু টেক্সট](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-ভিশন-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-ভিশন CLIP এম্বেডিং](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ডেমো: Phi-3 রিসাইক্লিং](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-ভিশন - ভিজ্যুয়াল ল্যাঙ্গুয়েজ অ্যাসিস্ট্যান্ট - Phi3-ভিশন এবং OpenVINO সহ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 ভিশন Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 ভিশন OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 ভিশন মাল্টি-ফ্রেম অথবা মাল্টি-ইমেজ নমুনা](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET ব্যবহার করে Phi-3 ভিশন স্থানীয় ONNX মডেল](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [মেনু ভিত্তিক Phi-3 ভিশন স্থানীয় ONNX মডেল Microsoft.ML.OnnxRuntime .NET ব্যবহার করে](../../md/04.HOL/dotnet/src/LabsPhi304)

  - গাণিতিক নমুনা
    -  Phi-4-মিনি-ফ্ল্যাশ-যুক্তি-ইনস্ট্রাক্ট নমুনা 🆕 [Phi-4-মিনি-ফ্ল্যাশ-যুক্তি-ইনস্ট্রাক্ট এর সাথে ম্যাথ ডেমো](./md/02.Application/09.Math/MathDemo.ipynb)

  - অডিও নমুনা
    - Phi-4 নমুনা 🆕
      - [📓] [Phi-4-মাল্টিমোডাল ব্যবহার করে অডিও ট্রান্সক্রিপ্ট বের করা](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-মাল্টিমোডাল অডিও নমুনা](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-মাল্টিমোডাল স্পিচ ট্রান্সলেশন নমুনা](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET কনসোল অ্যাপ্লিকেশন Phi-4-মাল্টিমোডাল অডিও ব্যবহার করে একটি অডিও ফাইল বিশ্লেষণ এবং ট্রান্সক্রিপ্ট তৈরি](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE নমুনা
    - Phi-3 / 3.5 নমুনা
      - [📓] [Phi-3.5 মিশ্র এক্সপার্টস মডেল (MoEs) সামাজিক মিডিয়া নমুনা](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI সার্চ, এবং LlamaIndex দিয়ে রিট্রিভাল-অগমেন্টেড জেনারেশন (RAG) পাইপলাইন তৈরি](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - ফাংশন কলিং নমুনা
    - Phi-4 নমুনা 🆕
      -  [📓] [Phi-4-মিনি দিয়ে ফাংশন কলিং ব্যবহার](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-মিনি দিয়ে মাল্টি-এজেন্ট তৈরি করতে ফাংশন কলিং ব্যবহার](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama সঙ্গে ফাংশন কলিং ব্যবহার](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX সঙ্গে ফাংশন কলিং ব্যবহার](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - মাল্টিমোডাল মিক্সিং নমুনা
    - Phi-4 নমুনা 🆕
      -  [📓] [Phi-4-মাল্টিমোডাল ব্যবহার করে একজন প্রযুক্তি সাংবাদিক হিসাবে](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET কনসোল অ্যাপ্লিকেশন Phi-4-মাল্টিমোডাল ব্যবহার করে ছবি বিশ্লেষণ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi ফাইন-টিউনিং নমুনা
  - [ফাইন-টিউনিং পরিস্থিতি](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ফাইন-টিউনিং বনাম RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 কে একটি শিল্প বিশেষজ্ঞ হতে দিন ফাইন-টিউনিং](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS কোডের জন্য AI টুলকিট দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure মেশিন লার্নিং সার্ভিসের সাথে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry সহ Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive সহ ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On ল্যাব সহ ফাইন-টিউনিং](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias ব্যবহার করে Phi-3-ভিশন ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [অ্যাপল MLX ফ্রেমওয়ার্ক সহ Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-ভিশন ফাইন-টিউনিং (আধिकारिक সমর্থন)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers (আধिकारिक সমর্থন) সহ Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 এবং 3.5 ভিশন ফাইন-টিউনিং](https://github.com/2U1/Phi3-Vision-Finetune)

- হ্যান্ডস অন ল্যাব
  - [সর্বশেষ মডেলগুলি অনুসন্ধান: LLMs, SLMs, স্থানীয় ডেভেলপমেন্ট এবং আরও অনেক কিছু](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [এনএলপি সম্ভাবনা উন্মোচন: Microsoft Olive এর সাথে ফাইন-টিউনিং](https://github.com/azure/Ignite_FineTuning_workshop)

- একাডেমিক গবেষণা পত্রিকা এবং প্রকাশনা
  - [পাঠ্যপুস্তক শুধুমাত্র আপনার প্রয়োজন II: phi-1.5 প্রযুক্তিগত প্রতিবেদন](https://arxiv.org/abs/2309.05463)
  - [Phi-3 প্রযুক্তিগত প্রতিবেদন: একটি উচ্চ সক্ষম ভাষা মডেল আপনার ফোনে স্থানীয়ভাবে](https://arxiv.org/abs/2404.14219)
  - [Phi-4 প্রযুক্তিগত প্রতিবেদন](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini প্রযুক্তিগত প্রতিবেদন: মিশ্রণের মাধ্যমে সংক্ষিপ্ত কিন্তু শক্তিশালী মাল্টিমোডাল ভাষা মডেল - LoRAs](https://arxiv.org/abs/2503.01743)
  - [যানবাহনের ভিতরে ফাংশন কল করার জন্য ছোট ভাষা মডেলগুলির অপ্টিমাইজেশন](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) একাধিক বিকল্প প্রশ্ন উত্তর দেওয়ার জন্য PHI-3 এর ফাইন-টিউনিং: পদ্ধতি, ফলাফল এবং চ্যালেঞ্জ](https://arxiv.org/abs/2501.01588)
  - [Phi-4-যুক্তিযুক্ত প্রযুক্তিগত প্রতিবেদন](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-যুক্তিযুক্ত প্রযুক্তিগত প্রতিবেদন](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi মডেল ব্যবহার

### Azure AI Foundry-এ Phi

আপনি Microsoft Phi কীভাবে ব্যবহার করবেন এবং কীভাবে আপনার বিভিন্ন হার্ডওয়্যার ডিভাইসে E2E সমাধান তৈরি করবেন তা শিখতে পারেন। Phi নিজেই অনুভব করতে, মডেলগুলি ব্যবহার করে শুরু করুন এবং আপনার পরিস্থিতির জন্য Phi কাস্টমাইজ করুন [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ব্যবহার করে। আপনি আরও জানতে পারেন [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) এ শুরু করার মাধ্যমে।

**প্লেগ্রাউন্ড**  
প্রতি মডেলের একটি নির্দিষ্ট প্লেগ্রাউন্ড রয়েছে মডেলটি পরীক্ষা করার জন্য [Azure AI Playground](https://aka.ms/try-phi3)।

### GitHub মডেল-এ Phi

আপনি Microsoft Phi কীভাবে ব্যবহার করবেন এবং কীভাবে আপনার বিভিন্ন হার্ডওয়্যার ডিভাইসে E2E সমাধান তৈরি করবেন তা শিখতে পারেন। Phi নিজেই অনুভব করতে, মডেলটি ব্যবহার করে শুরু করুন এবং আপনার পরিস্থিতির জন্য Phi কাস্টমাইজ করুন [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ব্যবহার করে। আপনি আরও জানতে পারেন [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) এ শুরু করার মাধ্যমে।

**প্লেগ্রাউন্ড**  
প্রতি মডেলের একটি নির্দিষ্ট [প্লেগ্রাউন্ড রয়েছে মডেল পরীক্ষা করার জন্য](/md/02.QuickStart/GitHubModel_QuickStart.md)।

### Hugging Face-এ Phi

আপনি মডেলটি [Hugging Face](https://huggingface.co/microsoft) এও খুঁজে পেতে পারেন।

**প্লেগ্রাউন্ড**  
[Hugging Chat প্লেগ্রাউন্ড](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 অন্যান্য কোর্সসমূহ

আমাদের টিম অন্যান্য কোর্সও তৈরি করে! দেখে নিন:

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

### Generative AI সিরিজ  
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### কোর লার্নিং  
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)  
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Copilot সিরিজ  
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## দায়িত্বশীল AI

Microsoft আমাদের গ্রাহকদের AI পণ্য দায়িত্বশীলভাবে ব্যবহারে সাহায্য করতে প্রতিশ্রুতিবদ্ধ, আমাদের শেখাগুলো শেয়ার করে এবং ট্রান্সপারেন্সি নোট ও প্রভাব মূল্যায়নের মতো সরঞ্জামগুলোর মাধ্যমে বিশ্বাসভিত্তিক অংশীদারিত্ব গড়ে তোলে। এই সমস্ত রিসোর্সগুলি [https://aka.ms/RAI](https://aka.ms/RAI) এ পাওয়া যায়।  
Microsoft-এর দায়িত্বশীল AI-র দৃষ্টিভঙ্গি আমাদের AI নীতি—ন্যায়পরায়ণতা, নির্ভরযোগ্যতা ও নিরাপত্তা, গোপনীয়তা ও নিরাপত্তা, অন্তর্ভুক্তি, স্বচ্ছতা এবং জবাবদিহিতার উপর ভিত্তি করে প্রতিষ্ঠিত।  

বড় পরিসরের প্রাকৃতিক ভাষা, ছবি এবং বক্তৃতা মডেলগুলি - যেমন এই নমুনায় ব্যবহৃত - সম্ভাব্যভাবে এমন আচরণ করতে পারে যা ন্যায়সঙ্গত নয়, অবিশ্বাস্য বা আপত্তিকর, যার ফলে ক্ষতি হতে পারে। দয়া করে [Azure OpenAI পরিষেবা ট্রান্সপারেন্সি নোট](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) পরামর্শ করুন যা ঝুঁকি এবং সীমাবদ্ধতা সম্পর্কে অবগত করবে।  

এই ঝুঁকিগুলো কমাতে সুপারিশকৃত পদ্ধতি হল একটি নিরাপত্তা ব্যবস্থা আপনার স্থাপত্যে অন্তর্ভুক্ত করা যা ক্ষতিকর আচরণ সনাক্ত এবং প্রতিরোধ করতে পারে। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) একটি স্বতন্ত্র সুরক্ষা স্তর সরবরাহ করে, যা অ্যাপ্লিকেশন এবং পরিষেবাগুলিতে ব্যবহারকারী-উত্পন্ন এবং AI-উত্পন্ন ক্ষতিকর সামগ্রী সনাক্ত করতে সক্ষম। Azure AI Content Safety-তে টেক্সট এবং ইমেজ API রয়েছে যা ক্ষতিকর উপাদান সনাক্ত করার অনুমতি দেয়। Azure AI Foundry-এর মধ্যে, Content Safety পরিষেবাটি ক্ষতিকর সামগ্রী বিভিন্ন মোডালিটির মধ্যে সনাক্ত করতে নমুনা কোড দেখার, পরীক্ষা করার এবং চেষ্টা করার সুযোগ দেয়। নিম্নলিখিত [দ্রুত শুরু নথিপত্র](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) আপনাকে পরিষেবায় অনুরোধ পাঠানোর দিকনির্দেশনা দেয়।  

অন্য একটি দিক যা বিবেচনা করা জরুরি তা হলো সামগ্রিক অ্যাপ্লিকেশন কর্মক্ষমতা। মাল্টি-মোডাল এবং মাল্টি-মডেল অ্যাপ্লিকেশনগুলিতে, আমরা কর্মক্ষমতা বলতে বুঝি সিস্টেমটি যেমন আপনি এবং আপনার ব্যবহারকারীরা প্রত্যাশা করেন ঠিক তেমনই কাজ করে, যার মধ্যে ক্ষতিকর আউটপুট তৈরি না করাও অন্তর্ভুক্ত। আপনার সামগ্রিক অ্যাপ্লিকেশনের কর্মক্ষমতা মূল্যায়ন করা গুরুত্বপূর্ণ, [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ব্যবহার করে। আপনি নিজের তৈরি [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) তৈরি এবং মূল্যায়ন করার সুবিধাও পাবেন।
আপনি আপনার ডেভেলপমেন্ট পরিবেশে [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ব্যবহার করে আপনার AI অ্যাপ্লিকেশন মূল্যায়ন করতে পারেন। একটি টেস্ট ডেটাসেট বা একটি লক্ষ্য প্রদান করার মাধ্যমে, আপনার জেনারেটিভ AI অ্যাপ্লিকেশন তৈরি করা ফলাফলগুলি অন্তর্নির্মিত মূল্যায়কদের বা আপনার পছন্দ অনুযায়ী কাস্টম মূল্যায়কদের মাধ্যমে পরিমাণগতভাবে পরিমাপ করা হয়। আপনার সিস্টেম মূল্যায়ন করতে azure ai evaluation sdk ব্যবহার শুরু করতে, আপনি [কুইকস্টার্ট গাইড](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) অনুসরণ করতে পারেন। একবার আপনি একটি মূল্যায়ন রান সম্পাদন করলে, আপনি [Azure AI Foundry তে ফলাফলগুলি ভিজ্যুয়ালাইজ করতে পারেন](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)।

## ট্রেডমার্কস

এই প্রকল্পে প্রকল্প, পণ্য, বা সেবার ট্রেডমার্ক বা লোগো থাকতে পারে। মাইক্রোসফটের ট্রেডমার্ক বা লোগোর অনুমোদিত ব্যবহার [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) অনুসারে হতে হবে এবং তা অনুসরণ করতে হবে। এই প্রকল্পের সংশোধিত সংস্করণে মাইক্রোসফটের ট্রেডমার্ক বা লোগোর ব্যবহার বিভ্রান্তি সৃষ্টি করতে পারবে না বা মাইক্রোসফট স্পন্সরশিপ বোঝাতে পারবে না। তৃতীয় পক্ষের ট্রেডমার্ক বা লোগो ব্যবহার সেই তৃতীয় পক্ষের নীতিমালা অনুযায়ী হবে।

## সাহায্য পাওয়া

যদি আপনি আটকে যান বা AI অ্যাপ তৈরি সম্পর্কে কোনো প্রশ্ন থাকে, যোগ দিন:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

যদি আপনার কোনো প্রোডাক্ট ফিডব্যাক বা ত্রুটি থাকে নির্মাণকালে, যান:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**দায়িত্বসীমা:**
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা সঠিকতার জন্য চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে তা দয়া করে জানুন। মূল নথিটি তার স্বামীভাষায় authoritative উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানুষ দ্বারা অনুবাদ করানোই উত্তম। এই অনুবাদের ব্যবহারে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->