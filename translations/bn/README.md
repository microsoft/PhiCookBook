<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2e042b12a63c59931dc121c2c638bc58",
  "translation_date": "2025-07-09T18:12:04+00:00",
  "source_file": "README.md",
  "language_code": "bn"
}
-->
# Phi কুকবুক: Microsoft-এর Phi মডেল নিয়ে হাতে কলমে উদাহরণসমূহ

[![GitHub Codespaces-এ স্যাম্পলগুলো খুলুন ও ব্যবহার করুন](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![Dev Containers-এ খুলুন](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub অবদানকারীরা](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub ইস্যুগুলো](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub পুল-রিকোয়েস্ট](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![PRs স্বাগত](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub ওয়াচাররা](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub ফর্ক](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub স্টার](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi হলো Microsoft কর্তৃক তৈরি একটি ওপেন সোর্স AI মডেল সিরিজ।

Phi বর্তমানে সবচেয়ে শক্তিশালী এবং খরচে সাশ্রয়ী ছোট ভাষা মডেল (SLM), যা বহু ভাষা, যুক্তি, টেক্সট/চ্যাট জেনারেশন, কোডিং, ছবি, অডিও এবং অন্যান্য ক্ষেত্রে খুব ভালো পারফরম্যান্স দেখায়।

আপনি Phi কে ক্লাউডে বা এজ ডিভাইসে ডিপ্লয় করতে পারেন, এবং সীমিত কম্পিউটিং ক্ষমতা নিয়ে সহজেই জেনারেটিভ AI অ্যাপ্লিকেশন তৈরি করতে পারবেন।

এই রিসোর্সগুলো ব্যবহার শুরু করতে নিচের ধাপগুলো অনুসরণ করুন:  
1. **রিপোজিটরি ফর্ক করুন**: ক্লিক করুন [![GitHub ফর্ক](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **রিপোজিটরি ক্লোন করুন**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Microsoft AI Discord কমিউনিটিতে যোগ দিন এবং বিশেষজ্ঞ ও অন্যান্য ডেভেলপারদের সাথে পরিচিত হন**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

## 🌐 বহু-ভাষা সমর্থন

### GitHub Action-এর মাধ্যমে সমর্থিত (স্বয়ংক্রিয় ও সর্বদা আপডেটেড)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md)  
[Bengali](./README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)

## বিষয়বস্তু সূচি

- পরিচিতি  
  - [Phi পরিবারের স্বাগতম](./md/01.Introduction/01/01.PhiFamily.md)  
  - [আপনার পরিবেশ সেটআপ করা](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [মূল প্রযুক্তিগুলো বোঝা](./md/01.Introduction/01/01.Understandingtech.md)  
  - [Phi মডেলের জন্য AI নিরাপত্তা](./md/01.Introduction/01/01.AISafety.md)  
  - [Phi হার্ডওয়্যার সমর্থন](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [Phi মডেল ও প্ল্যাটফর্ম অনুযায়ী প্রাপ্যতা](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [Guidance-ai এবং Phi ব্যবহার](./md/01.Introduction/01/01.Guidance.md)  
  - [GitHub মার্কেটপ্লেস মডেলসমূহ](https://github.com/marketplace/models)  
  - [Azure AI মডেল ক্যাটালগ](https://ai.azure.com)

- বিভিন্ন পরিবেশে Phi ইনফারেন্স  
  - [Hugging face](./md/01.Introduction/02/01.HF.md)  
  - [GitHub মডেলসমূহ](./md/01.Introduction/02/02.GitHubModel.md)  
  - [Azure AI Foundry মডেল ক্যাটালগ](./md/01.Introduction/02/03.AzureAIFoundry.md)  
  - [Ollama](./md/01.Introduction/02/04.Ollama.md)  
  - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
  - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)  
  - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi পরিবারের ইনফারেন্স  
  - [iOS-এ Phi ইনফারেন্স](./md/01.Introduction/03/iOS_Inference.md)  
  - [Android-এ Phi ইনফারেন্স](./md/01.Introduction/03/Android_Inference.md)  
  - [Jetson-এ Phi ইনফারেন্স](./md/01.Introduction/03/Jetson_Inference.md)  
  - [AI PC-তে Phi ইনফারেন্স](./md/01.Introduction/03/AIPC_Inference.md)  
  - [Apple MLX Framework দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/MLX_Inference.md)  
  - [লোকাল সার্ভারে Phi ইনফারেন্স](./md/01.Introduction/03/Local_Server_Inference.md)  
  - [AI Toolkit ব্যবহার করে রিমোট সার্ভারে Phi ইনফারেন্স](./md/01.Introduction/03/Remote_Interence.md)  
  - [Rust দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/Rust_Inference.md)  
  - [লোকালে Phi--Vision ইনফারেন্স](./md/01.Introduction/03/Vision_Inference.md)  
  - [Kaito AKS, Azure Containers (সরকারি সমর্থন) দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/Kaito_Inference.md)

- [Phi পরিবারের কোয়ান্টিফিকেশন](./md/01.Introduction/04/QuantifyingPhi.md)  
  - [llama.cpp ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজেশন](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
  - [onnxruntime-এর জন্য Generative AI এক্সটেনশন ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজেশন](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
  - [Intel OpenVINO ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজেশন](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
  - [Apple MLX Framework ব্যবহার করে Phi-3.5 / 4 কোয়ান্টাইজেশন](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi মূল্যায়ন  
  - [Responsible AI](./md/01.Introduction/05/ResponsibleAI.md)  
  - [Azure AI Foundry মূল্যায়নের জন্য](./md/01.Introduction/05/AIFoundry.md)  
  - [Promptflow ব্যবহার করে মূল্যায়ন](./md/01.Introduction/05/Promptflow.md)

- Azure AI Search-এর সাথে RAG  
  - [Phi-4-mini এবং Phi-4-multimodal(RAG) Azure AI Search-এর সাথে ব্যবহার করার পদ্ধতি](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi অ্যাপ্লিকেশন ডেভেলপমেন্ট স্যাম্পলস  
  - টেক্সট ও চ্যাট অ্যাপ্লিকেশন  
    - Phi-4 স্যাম্পলস 🆕  
      - [📓] [Phi-4-mini ONNX মডেলের সাথে চ্যাট](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Phi-4 লোকাল ONNX মডেলের সাথে চ্যাট .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [Semantic Kernel ব্যবহার করে Phi-4 ONNX সহ .NET কনসোল অ্যাপ চ্যাট](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 স্যাম্পলস  
      - [Phi3, ONNX Runtime Web এবং WebGPU ব্যবহার করে ব্রাউজারে লোকাল চ্যাটবট](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [OpenVino চ্যাট](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [মাল্টি মডেল - ইন্টারেক্টিভ Phi-3-mini এবং OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - একটি র‍্যাপার তৈরি ও Phi-3 MLFlow-এর সাথে ব্যবহার](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [মডেল অপটিমাইজেশন - Phi-3-mini মডেল ONNX Runtime Web-এর জন্য Olive দিয়ে অপটিমাইজ করা](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [WinUI3 অ্যাপ Phi-3 mini-4k-instruct-onnx দিয়ে](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [WinUI3 মাল্টি মডেল AI চালিত নোটস অ্যাপ স্যাম্পল](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Prompt flow-এর সাথে কাস্টম Phi-3 মডেল ফাইন-টিউন এবং ইন্টিগ্রেট করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Azure AI Foundry-তে Prompt flow-এর সাথে কাস্টম Phi-3 মডেল ফাইন-টিউন এবং ইন্টিগ্রেট করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Microsoft-এর Responsible AI নীতিমালা অনুসারে Azure AI Foundry-তে ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেল মূল্যায়ন করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct ভাষা পূর্বাভাস নমুনা (চীনা/ইংরেজি)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG চ্যাটবট](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU ব্যবহার করে Phi-3.5-Instruct ONNX দিয়ে Prompt flow সমাধান তৈরি করা](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tflite ব্যবহার করে Android অ্যাপ তৈরি করা](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Microsoft.ML.OnnxRuntime ব্যবহার করে স্থানীয় ONNX Phi-3 মডেল দিয়ে Q&A .NET উদাহরণ](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Semantic Kernel এবং Phi-3 সহ কনসোল চ্যাট .NET অ্যাপ](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK কোড ভিত্তিক নমুনা
  - Phi-4 নমুনা 🆕
    - [📓] [Phi-4-multimodal ব্যবহার করে প্রকল্প কোড তৈরি করুন](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5 নমুনা
    - [Microsoft Phi-3 পরিবার ব্যবহার করে নিজের Visual Studio Code GitHub Copilot Chat তৈরি করুন](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [GitHub মডেল দিয়ে Phi-3.5 ব্যবহার করে নিজের Visual Studio Code Chat Copilot Agent তৈরি করুন](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- উন্নত যুক্তি নমুনা
  - Phi-4 নমুনা 🆕
    - [📓] [Phi-4-mini-reasoning বা Phi-4-reasoning নমুনা](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Microsoft Olive দিয়ে Phi-4-mini-reasoning ফাইন-টিউনিং](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Apple MLX দিয়ে Phi-4-mini-reasoning ফাইন-টিউনিং](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [GitHub মডেল দিয়ে Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Azure AI Foundry মডেল দিয়ে Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- ডেমো
    - [Hugging Face Spaces-এ হোস্ট করা Phi-4-mini ডেমো](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Hugging Face Spaces-এ হোস্ট করা Phi-4-multimodal ডেমো](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- ভিশন নমুনা
  - Phi-4 নমুনা 🆕
    - [📓] [Phi-4-multimodal ব্যবহার করে ছবি পড়া এবং কোড তৈরি করা](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)
  - Phi-3 / 3.5 নমুনা
    - [📓][Phi-3-vision-ছবি থেকে টেক্সট অনলাইন এন্ডপয়েন্টে টেক্সট রূপান্তর](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP এম্বেডিং](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [ডেমো: Phi-3 রিসাইক্লিং](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - ভিজ্যুয়াল ভাষা সহকারী - Phi3-Vision এবং OpenVINO সহ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision মাল্টি-ফ্রেম বা মাল্টি-ইমেজ নমুনা](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Microsoft.ML.OnnxRuntime .NET ব্যবহার করে Phi-3 Vision স্থানীয় ONNX মডেল](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [মেনু ভিত্তিক Phi-3 Vision স্থানীয় ONNX মডেল Microsoft.ML.OnnxRuntime .NET ব্যবহার করে](../../md/04.HOL/dotnet/src/LabsPhi304)

- গণিত নমুনা
  - Phi-4-Mini-Flash-Reasoning-Instruct নমুনা 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct সহ গণিত ডেমো](../../md/02.Application/09.Math/MathDemo.ipynb)

- অডিও নমুনা
  - Phi-4 নমুনা 🆕
    - [📓] [Phi-4-multimodal ব্যবহার করে অডিও ট্রান্সক্রিপ্ট বের করা](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodal অডিও নমুনা](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal স্পিচ ট্রান্সলেশন নমুনা](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [Phi-4-multimodal অডিও ব্যবহার করে অডিও ফাইল বিশ্লেষণ এবং ট্রান্সক্রিপ্ট তৈরি করার .NET কনসোল অ্যাপ্লিকেশন](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOE নমুনা
  - Phi-3 / 3.5 নমুনা
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) সামাজিক মিডিয়া নমুনা](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, এবং LlamaIndex দিয়ে Retrieval-Augmented Generation (RAG) পাইপলাইন তৈরি করা](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- ফাংশন কলিং নমুনা
  - Phi-4 নমুনা 🆕
    - [📓] [Phi-4-mini দিয়ে ফাংশন কলিং ব্যবহার করা](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Phi-4-mini দিয়ে মাল্টি-এজেন্ট তৈরি করতে ফাংশন কলিং ব্যবহার করা](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Ollama দিয়ে ফাংশন কলিং ব্যবহার করা](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [ONNX দিয়ে ফাংশন কলিং ব্যবহার করা](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- মাল্টিমোডাল মিক্সিং নমুনা
  - Phi-4 নমুনা 🆕
    - [📓] [প্রযুক্তি সাংবাদিক হিসেবে Phi-4-multimodal ব্যবহার করা](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [Phi-4-multimodal ব্যবহার করে ছবি বিশ্লেষণ করার .NET কনসোল অ্যাপ্লিকেশন](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi ফাইন-টিউনিং
  - [ফাইন-টিউনিং পরিস্থিতি](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ফাইন-টিউনিং বনাম RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 কে একটি শিল্প বিশেষজ্ঞ বানান ফাইন-টিউনিং করে](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [AI Toolkit for VS Code দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive দিয়ে ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Lab দিয়ে ফাইন-টিউনিং](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias দিয়ে Phi-3-vision ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework দিয়ে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision ফাইন-টিউনিং (সরকারি সমর্থন)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers দিয়ে Phi-3 ফাইন-টিউনিং (সরকারি সমর্থন)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 এবং 3.5 Vision ফাইন-টিউনিং](https://github.com/2U1/Phi3-Vision-Finetune)

- হ্যান্ডস অন ল্যাব
  - [সর্বাধুনিক মডেল অনুসন্ধান: LLMs, SLMs, স্থানীয় ডেভেলপমেন্ট এবং আরও অনেক কিছু](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP সম্ভাবনা উন্মোচন: Microsoft Olive দিয়ে ফাইন-টিউনিং](https://github.com/azure/Ignite_FineTuning_workshop)

- একাডেমিক গবেষণা পত্র এবং প্রকাশনা
  - [Textbooks Are All You Need II: phi-1.5 প্রযুক্তিগত প্রতিবেদন](https://arxiv.org/abs/2309.05463)
  - [Phi-3 প্রযুক্তিগত প্রতিবেদন: আপনার ফোনে স্থানীয়ভাবে একটি অত্যন্ত সক্ষম ভাষা মডেল](https://arxiv.org/abs/2404.14219)
  - [Phi-4 প্রযুক্তিগত প্রতিবেদন](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini প্রযুক্তিগত প্রতিবেদন: Mixture-of-LoRAs এর মাধ্যমে সংক্ষিপ্ত কিন্তু শক্তিশালী মাল্টিমোডাল ভাষা মডেল](https://arxiv.org/abs/2503.01743)
  - [গাড়ির ভিতরে ফাংশন কলিংয়ের জন্য ছোট ভাষা মডেল অপ্টিমাইজেশন](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) একাধিক-চয়েস প্রশ্নোত্তরের জন্য PHI-3 ফাইন-টিউনিং: পদ্ধতি, ফলাফল এবং চ্যালেঞ্জ](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning Technical Report](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-reasoning Technical Report](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi মডেল ব্যবহার করা

### Azure AI Foundry-তে Phi

আপনি Microsoft Phi কীভাবে ব্যবহার করবেন এবং বিভিন্ন হার্ডওয়্যার ডিভাইসে E2E সমাধান কীভাবে তৈরি করবেন তা শিখতে পারেন। Phi নিজে থেকে অনুভব করতে, মডেলগুলোর সাথে খেলতে শুরু করুন এবং আপনার পরিস্থিতির জন্য Phi কাস্টমাইজ করুন [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ব্যবহার করে। আরও জানতে পারেন [Azure AI Foundry শুরু করার গাইডে](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)।

**Playground**  
প্রতিটি মডেলের জন্য একটি নির্দিষ্ট প্লেগ্রাউন্ড রয়েছে মডেল পরীক্ষা করার জন্য [Azure AI Playground](https://aka.ms/try-phi3)।

### GitHub মডেলে Phi

আপনি Microsoft Phi কীভাবে ব্যবহার করবেন এবং বিভিন্ন হার্ডওয়্যার ডিভাইসে E2E সমাধান কীভাবে তৈরি করবেন তা শিখতে পারেন। Phi নিজে থেকে অনুভব করতে, মডেলের সাথে খেলতে শুরু করুন এবং আপনার পরিস্থিতির জন্য Phi কাস্টমাইজ করুন [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ব্যবহার করে। আরও জানতে পারেন [GitHub Model Catalog শুরু করার গাইডে](/md/02.QuickStart/GitHubModel_QuickStart.md)।

**Playground**  
প্রতিটি মডেলের জন্য একটি নির্দিষ্ট [প্লেগ্রাউন্ড রয়েছে মডেল পরীক্ষা করার জন্য](/md/02.QuickStart/GitHubModel_QuickStart.md)।

### Hugging Face-এ Phi

আপনি মডেলটি [Hugging Face](https://huggingface.co/microsoft) থেকেও পেতে পারেন।

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## দায়িত্বশীল AI

Microsoft আমাদের গ্রাহকদের AI পণ্যগুলি দায়িত্বশীলভাবে ব্যবহার করতে সাহায্য করতে প্রতিশ্রুতিবদ্ধ, আমাদের শেখাগুলো শেয়ার করে এবং Transparency Notes ও Impact Assessments-এর মতো টুলসের মাধ্যমে বিশ্বাসভিত্তিক অংশীদারিত্ব গড়ে তোলে। এই রিসোর্সগুলোর অনেকগুলো পাওয়া যায় [https://aka.ms/RAI](https://aka.ms/RAI) এ।  
Microsoft-এর দায়িত্বশীল AI-এর দৃষ্টিভঙ্গি আমাদের AI নীতিমালা—ন্যায়পরায়ণতা, নির্ভরযোগ্যতা ও নিরাপত্তা, গোপনীয়তা ও সুরক্ষা, অন্তর্ভুক্তি, স্বচ্ছতা এবং জবাবদিহিতার উপর ভিত্তি করে গড়ে উঠেছে।

বড় আকারের প্রাকৃতিক ভাষা, ছবি এবং ভাষণ মডেলগুলো—যেমন এই নমুনায় ব্যবহৃত মডেলগুলো—সম্ভাব্যভাবে এমন আচরণ করতে পারে যা অন্যায়, অবিশ্বস্ত বা আপত্তিকর হতে পারে, যা ক্ষতি ডেকে আনতে পারে। ঝুঁকি ও সীমাবদ্ধতা সম্পর্কে অবহিত হতে [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) দেখুন।

এই ঝুঁকিগুলো কমানোর জন্য সুপারিশকৃত পদ্ধতি হলো আপনার আর্কিটেকচারে একটি নিরাপত্তা ব্যবস্থা অন্তর্ভুক্ত করা যা ক্ষতিকর আচরণ সনাক্ত ও প্রতিরোধ করতে পারে। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) একটি স্বাধীন সুরক্ষা স্তর প্রদান করে, যা অ্যাপ্লিকেশন ও সেবায় ক্ষতিকর ব্যবহারকারী-উত্পাদিত এবং AI-উত্পাদিত বিষয়বস্তু সনাক্ত করতে সক্ষম। Azure AI Content Safety-তে টেক্সট ও ইমেজ API রয়েছে যা ক্ষতিকর উপাদান সনাক্ত করতে সাহায্য করে। Azure AI Foundry-র মধ্যে Content Safety সার্ভিস আপনাকে বিভিন্ন মাধ্যম জুড়ে ক্ষতিকর বিষয়বস্তু সনাক্ত করার জন্য নমুনা কোড দেখতে, অন্বেষণ করতে এবং চেষ্টা করতে দেয়। নিম্নলিখিত [quickstart ডকুমেন্টেশন](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) আপনাকে সার্ভিসে রিকোয়েস্ট পাঠানোর প্রক্রিয়ায় গাইড করবে।

আরেকটি বিষয় যা বিবেচনা করতে হবে তা হলো সামগ্রিক অ্যাপ্লিকেশন পারফরম্যান্স। মাল্টি-মোডাল এবং মাল্টি-মডেল অ্যাপ্লিকেশনগুলোর ক্ষেত্রে, পারফরম্যান্স বলতে আমরা বুঝি যে সিস্টেমটি আপনার এবং আপনার ব্যবহারকারীদের প্রত্যাশা অনুযায়ী কাজ করে, যার মধ্যে ক্ষতিকর আউটপুট তৈরি না করাও অন্তর্ভুক্ত। আপনার সামগ্রিক অ্যাপ্লিকেশনের পারফরম্যান্স মূল্যায়ন করা গুরুত্বপূর্ণ [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ব্যবহার করে। এছাড়াও আপনি [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) তৈরি ও মূল্যায়ন করার ক্ষমতাও রাখেন।

আপনি আপনার AI অ্যাপ্লিকেশনটি আপনার ডেভেলপমেন্ট পরিবেশে [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ব্যবহার করে মূল্যায়ন করতে পারেন। একটি টেস্ট ডেটাসেট বা লক্ষ্য দেওয়ার মাধ্যমে, আপনার জেনারেটিভ AI অ্যাপ্লিকেশনের জেনারেশনগুলো built-in evaluators বা আপনার পছন্দের custom evaluators দিয়ে পরিমাণগতভাবে মাপা হয়। Azure AI Evaluation SDK দিয়ে আপনার সিস্টেম মূল্যায়ন শুরু করতে, আপনি [quickstart গাইড](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) অনুসরণ করতে পারেন। একবার আপনি একটি মূল্যায়ন রান সম্পন্ন করলে, আপনি [Azure AI Foundry-তে ফলাফলগুলো ভিজ্যুয়ালাইজ করতে পারেন](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)।

## ট্রেডমার্ক

এই প্রকল্পে প্রকল্প, পণ্য বা সেবার ট্রেডমার্ক বা লোগো থাকতে পারে। Microsoft ট্রেডমার্ক বা লোগোর অনুমোদিত ব্যবহার অবশ্যই [Microsoft-এর Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) অনুসরণ করতে হবে।  
Microsoft ট্রেডমার্ক বা লোগো এই প্রকল্পের সংশোধিত সংস্করণে ব্যবহার করলে বিভ্রান্তি সৃষ্টি করা বা Microsoft-এর স্পন্সরশিপ বোঝানো যাবে না। তৃতীয় পক্ষের ট্রেডমার্ক বা লোগোর যেকোনো ব্যবহার সেই পক্ষের নীতিমালা অনুসারে হতে হবে।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।