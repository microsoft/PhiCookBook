<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T13:37:39+00:00",
  "source_file": "README.md",
  "language_code": "bn"
}
-->
# Phi কুকবুক: মাইক্রোসফটের Phi মডেলগুলোর হাতে-কলমে উদাহরণ

Phi হলো মাইক্রোসফটের দ্বারা উন্নতকৃত ওপেন সোর্স AI মডেলের একটি সিরিজ।

Phi বর্তমানে সবচেয়ে শক্তিশালী এবং খরচ-সাশ্রয়ী ছোট ভাষা মডেল (SLM), যা বহু-ভাষা, যুক্তি, টেক্সট/চ্যাট জেনারেশন, কোডিং, ছবি, অডিও এবং অন্যান্য ক্ষেত্রে খুব ভালো মানদণ্ড প্রদর্শন করে।

আপনি Phi মডেল ক্লাউডে বা এজ ডিভাইসে ডিপ্লয় করতে পারেন এবং সীমিত কম্পিউটিং ক্ষমতা দিয়ে সহজেই জেনারেটিভ AI অ্যাপ্লিকেশন তৈরি করতে পারেন।

এই রিসোর্সগুলো ব্যবহার শুরু করতে নিচের ধাপগুলো অনুসরণ করুন:
1. **রিপোজিটরি ফর্ক করুন**: ক্লিক করুন [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **রিপোজিটরি ক্লোন করুন**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**মাইক্রোসফট AI ডিসকর্ড কমিউনিটিতে যোগ দিন এবং বিশেষজ্ঞ ও অন্যান্য ডেভেলপারদের সাথে পরিচিত হন**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![কভার](../../imgs/cover.png)

### 🌐 বহু-ভাষার সমর্থন

#### GitHub Action এর মাধ্যমে সমর্থিত (স্বয়ংক্রিয় এবং সর্বদা আপডেটেড)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) 
[Bengali](./README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)

## বিষয়বস্তুর তালিকা

- পরিচিতি
  - [Phi পরিবারের সাথে পরিচিত হন](./md/01.Introduction/01/01.PhiFamily.md)
  - [আপনার পরিবেশ সেটআপ করুন](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [মূল প্রযুক্তিগুলো বুঝুন](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi মডেলের জন্য AI নিরাপত্তা](./md/01.Introduction/01/01.AISafety.md)
  - [Phi হার্ডওয়্যার সমর্থন](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi মডেল এবং প্ল্যাটফর্মে উপলব্ধতা](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai এবং Phi ব্যবহার](./md/01.Introduction/01/01.Guidance.md)
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
    - [AI PC-তে Phi ইনফারেন্স](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/MLX_Inference.md)
    - [লোকাল সার্ভারে Phi ইনফারেন্স](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit ব্যবহার করে রিমোট সার্ভারে Phi ইনফারেন্স](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/Rust_Inference.md)
    - [লোকাল Vision Phi ইনফারেন্স](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (অফিশিয়াল সাপোর্ট) দিয়ে Phi ইনফারেন্স](./md/01.Introduction/03/Kaito_Inference.md)

- [Phi পরিবারের কোয়ান্টিফাই করা](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ব্যবহার করে Phi-3.5 / 4 কোয়ান্টিফাই করা](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime এর জেনারেটিভ AI এক্সটেনশন ব্যবহার করে Phi-3.5 / 4 কোয়ান্টিফাই করা](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ব্যবহার করে Phi-3.5 / 4 কোয়ান্টিফাই করা](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework ব্যবহার করে Phi-3.5 / 4 কোয়ান্টিফাই করা](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi মূল্যায়ন
    - [Response AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [মূল্যায়নের জন্য Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [মূল্যায়নের জন্য Promptflow ব্যবহার](./md/01.Introduction/05/Promptflow.md)

- Azure AI Search দিয়ে RAG
    - [Phi-4-mini এবং Phi-4-multimodal (RAG) Azure AI Search এর সাথে ব্যবহার করার পদ্ধতি](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi অ্যাপ্লিকেশন ডেভেলপমেন্ট নমুনা
  - টেক্সট ও চ্যাট অ্যাপ্লিকেশন
    - Phi-4 নমুনা 🆕
      - [📓] [Phi-4-mini ONNX মডেল দিয়ে চ্যাট করুন](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 লোকাল ONNX মডেল .NET দিয়ে চ্যাট করুন](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Phi-4 ONNX ব্যবহার করে সেম্যান্টিক কের্নেল সহ .NET কনসোল অ্যাপ চ্যাট](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 নমুনা
      - [Phi3, ONNX Runtime Web এবং WebGPU ব্যবহার করে ব্রাউজারে লোকাল চ্যাটবট](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino চ্যাট](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [মাল্টি মডেল - Phi-3-mini এবং OpenAI Whisper এর ইন্টারঅ্যাকটিভ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Phi-3 এর জন্য একটি র‍্যাপার তৈরি এবং MLFlow ব্যবহার](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [মডেল অপ্টিমাইজেশন - Olive দিয়ে ONNX Runtime Web এর জন্য Phi-3-min মডেল অপ্টিমাইজ করার পদ্ধতি](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx সহ WinUI3 অ্যাপ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3 মাল্টি মডেল AI চালিত নোটস অ্যাপ নমুনা](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [কাস্টম Phi-3 মডেল ফাইন-টিউন এবং Prompt flow এর সাথে ইন্টিগ্রেট করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Azure AI Foundry-তে কাস্টম Phi-3 মডেল ফাইন-টিউন এবং Prompt flow এর সাথে ইন্টিগ্রেট করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Microsoft-এর Responsible AI Principles-কে কেন্দ্র করে Azure AI Foundry-তে ফাইন-টিউন করা Phi-3 / Phi-3.5 মডেল মূল্যায়ন করুন](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct ভাষা পূর্বাভাস নমুনা (চীনা/ইংরেজি)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG চ্যাটবট](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU ব্যবহার করে Phi-3.5-Instruct ONNX এর সাথে Prompt flow সমাধান তৈরি করুন](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tflite ব্যবহার করে Android অ্যাপ তৈরি করুন](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Microsoft.ML.OnnxRuntime ব্যবহার করে স্থানীয় ONNX Phi-3 মডেলের সাথে Q&A .NET উদাহরণ](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Semantic Kernel এবং Phi-3 সহ Console chat .NET অ্যাপ](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK কোড ভিত্তিক নমুনা 
  - Phi-4 নমুনা 🆕
    - [📓] [Phi-4-multimodal ব্যবহার করে প্রজেক্ট কোড তৈরি করুন](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5 নমুনা
    - [Microsoft Phi-3 Family ব্যবহার করে নিজের Visual Studio Code GitHub Copilot Chat তৈরি করুন](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [GitHub মডেল ব্যবহার করে Phi-3.5 এর সাথে নিজের Visual Studio Code Chat Copilot Agent তৈরি করুন](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- উন্নত যুক্তি নমুনা
  - Phi-4 নমুনা 🆕
    - [📓] [Phi-4-mini-reasoning বা Phi-4-reasoning নমুনা](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Microsoft Olive ব্যবহার করে Phi-4-mini-reasoning ফাইন-টিউনিং](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Apple MLX ব্যবহার করে Phi-4-mini-reasoning ফাইন-টিউনিং](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [GitHub মডেল ব্যবহার করে Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Azure AI Foundry মডেল ব্যবহার করে Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- ডেমো
    - [Hugging Face Spaces-এ হোস্ট করা Phi-4-mini ডেমো](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Hugging Face Spaces-এ হোস্ট করা Phi-4-multimodal ডেমো](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- ভিশন নমুনা
  - Phi-4 নমুনা 🆕
    - [📓] [Phi-4-multimodal ব্যবহার করে ছবি পড়ুন এবং কোড তৈরি করুন](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Phi-3 / 3.5 নমুনা
    - [📓][Phi-3-vision-Image টেক্সট থেকে টেক্সট](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [ডেমো: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - ভিজ্যুয়াল ভাষা সহকারী - Phi3-Vision এবং OpenVINO সহ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision মাল্টি-ফ্রেম বা মাল্টি-ইমেজ নমুনা](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Microsoft.ML.OnnxRuntime .NET ব্যবহার করে Phi-3 Vision স্থানীয় ONNX মডেল](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Microsoft.ML.OnnxRuntime .NET ব্যবহার করে মেনু ভিত্তিক Phi-3 Vision স্থানীয় ONNX মডেল](../../md/04.HOL/dotnet/src/LabsPhi304)

- গণিত নমুনা
  - Phi-4-Mini-Flash-Reasoning-Instruct নমুনা 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct সহ গণিত ডেমো](../../md/02.Application/09.Math/MathDemo.ipynb)

- অডিও নমুনা
  - Phi-4 নমুনা 🆕
    - [📓] [Phi-4-multimodal ব্যবহার করে অডিও ট্রান্সক্রিপ্ট বের করুন](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodal অডিও নমুনা](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal স্পিচ অনুবাদ নমুনা](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET কনসোল অ্যাপ্লিকেশন ব্যবহার করে Phi-4-multimodal অডিও দিয়ে অডিও ফাইল বিশ্লেষণ এবং ট্রান্সক্রিপ্ট তৈরি করুন](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOE নমুনা
  - Phi-3 / 3.5 নমুনা
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) সোশ্যাল মিডিয়া নমুনা](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search এবং LlamaIndex ব্যবহার করে Retrieval-Augmented Generation (RAG) পাইপলাইন তৈরি করুন](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- ফাংশন কলিং নমুনা
  - Phi-4 নমুনা 🆕
    - [📓] [Phi-4-mini ব্যবহার করে ফাংশন কলিং](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Phi-4-mini ব্যবহার করে মাল্টি-এজেন্ট তৈরি করতে ফাংশন কলিং](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Ollama ব্যবহার করে ফাংশন কলিং](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [ONNX ব্যবহার করে ফাংশন কলিং](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- মাল্টিমোডাল মিক্সিং নমুনা
  - Phi-4 নমুনা 🆕
    - [📓] [Phi-4-multimodal ব্যবহার করে প্রযুক্তি সাংবাদিক হিসেবে কাজ করুন](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET কনসোল অ্যাপ্লিকেশন ব্যবহার করে Phi-4-multimodal দিয়ে ছবি বিশ্লেষণ করুন](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi নমুনা ফাইন-টিউনিং
  - [ফাইন-টিউনিং পরিস্থিতি](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ফাইন-টিউনিং বনাম RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 কে শিল্প বিশেষজ্ঞ বানানোর জন্য ফাইন-টিউনিং](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code এর AI Toolkit ব্যবহার করে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service ব্যবহার করে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora ব্যবহার করে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora ব্যবহার করে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry ব্যবহার করে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK ব্যবহার করে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive ব্যবহার করে ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Lab ব্যবহার করে ফাইন-টিউনিং](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias ব্যবহার করে Phi-3-vision ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework ব্যবহার করে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision (অফিসিয়াল সাপোর্ট) ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers (অফিসিয়াল সাপোর্ট) ব্যবহার করে Phi-3 ফাইন-টিউনিং](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 এবং 3.5 Vision ফাইন-টিউনিং](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands on Lab
  - [কাটিং-এজ মডেলগুলি অন্বেষণ করুন: LLMs, SLMs, স্থানীয় ডেভেলপমেন্ট এবং আরও অনেক কিছু](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP সম্ভাবনা আনলক করুন: Microsoft Olive দিয়ে ফাইন-টিউনিং](https://github.com/azure/Ignite_FineTuning_workshop)

- একাডেমিক গবেষণা পেপার এবং প্রকাশনা
  - [Textbooks Are All You Need II: phi-1.5 টেকনিক্যাল রিপোর্ট](https://arxiv.org/abs/2309.05463)
  - [Phi-3 টেকনিক্যাল রিপোর্ট: একটি অত্যন্ত সক্ষম ভাষা মডেল আপনার ফোনে স্থানীয়ভাবে](https://arxiv.org/abs/2404.14219)
  - [Phi-4 টেকনিক্যাল রিপোর্ট](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini টেকনিক্যাল রিপোর্ট: Mixture-of-LoRAs এর মাধ্যমে কমপ্যাক্ট কিন্তু শক্তিশালী মাল্টিমোডাল ভাষা মডেল](https://arxiv.org/abs/2503.01743)
  - [In-Vehicle Function-Calling এর জন্য ছোট ভাষা মডেল অপ্টিমাইজ করা](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Phi-3 কে Multiple-Choice Question Answering এর জন্য ফাইন-টিউনিং: পদ্ধতি, ফলাফল এবং চ্যালেঞ্জ](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning টেকনিক্যাল রিপোর্ট](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-reasoning টেকনিক্যাল রিপোর্ট](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi মডেল ব্যবহার করা

### Azure AI Foundry-তে Phi

আপনি Microsoft Phi কীভাবে ব্যবহার করবেন এবং কীভাবে বিভিন্ন হার্ডওয়্যার ডিভাইসে E2E সমাধান তৈরি করবেন তা শিখতে পারেন। Phi নিজে থেকে অভিজ্ঞতা নিতে, মডেলগুলোর সাথে কাজ শুরু করুন এবং আপনার পরিস্থিতি অনুযায়ী Phi কাস্টমাইজ করুন [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ব্যবহার করে। আরও জানতে, [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) এর সাথে শুরু করুন।

**প্লেগ্রাউন্ড**
প্রতিটি মডেলের জন্য একটি নির্দিষ্ট প্লেগ্রাউন্ড রয়েছে যেখানে আপনি মডেল পরীক্ষা করতে পারেন [Azure AI Playground](https://aka.ms/try-phi3)।

### GitHub মডেলগুলোর উপর Phi

আপনি Microsoft Phi কীভাবে ব্যবহার করবেন এবং কীভাবে বিভিন্ন হার্ডওয়্যার ডিভাইসে E2E সমাধান তৈরি করবেন তা শিখতে পারেন। Phi নিজে থেকে অভিজ্ঞতা নিতে, মডেলের সাথে কাজ শুরু করুন এবং আপনার পরিস্থিতি অনুযায়ী Phi কাস্টমাইজ করুন [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ব্যবহার করে। আরও জানতে, [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) এর সাথে শুরু করুন।

**প্লেগ্রাউন্ড**
প্রতিটি মডেলের জন্য একটি নির্দিষ্ট [প্লেগ্রাউন্ড রয়েছে যেখানে আপনি মডেল পরীক্ষা করতে পারেন](/md/02.QuickStart/GitHubModel_QuickStart.md)।

### Hugging Face-এ Phi

আপনি মডেলটি [Hugging Face](https://huggingface.co/microsoft) এও খুঁজে পেতে পারেন।

**প্লেগ্রাউন্ড**
[Hugging Chat প্লেগ্রাউন্ড](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## দায়িত্বশীল AI

Microsoft আমাদের গ্রাহকদের AI পণ্যগুলি দায়িত্বশীলভাবে ব্যবহার করতে সাহায্য করার জন্য, আমাদের অভিজ্ঞতা শেয়ার করার জন্য এবং বিশ্বাসভিত্তিক অংশীদারিত্ব গড়ে তোলার জন্য Transparency Notes এবং Impact Assessments-এর মতো টুল সরবরাহ করতে প্রতিশ্রুতিবদ্ধ। এই সমস্ত রিসোর্স [https://aka.ms/RAI](https://aka.ms/RAI) এ পাওয়া যাবে। Microsoft-এর দায়িত্বশীল AI-এর পদ্ধতি আমাদের AI নীতিমালার উপর ভিত্তি করে তৈরি, যা ন্যায্যতা, নির্ভরযোগ্যতা এবং নিরাপত্তা, গোপনীয়তা এবং সুরক্ষা, অন্তর্ভুক্তি, স্বচ্ছতা এবং জবাবদিহিতা নিশ্চিত করে।

বড় আকারের প্রাকৃতিক ভাষা, ছবি এবং বক্তৃতা মডেল - যেমন এই নমুনায় ব্যবহৃত মডেলগুলো - কখনও কখনও এমন আচরণ করতে পারে যা অন্যায়, অস্থির বা আপত্তিকর হতে পারে, যা ক্ষতির কারণ হতে পারে। ঝুঁকি এবং সীমাবদ্ধতা সম্পর্কে সচেতন হতে [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) পরামর্শ করুন।

এই ঝুঁকিগুলো কমানোর জন্য প্রস্তাবিত পদ্ধতি হলো আপনার আর্কিটেকচারে একটি নিরাপত্তা ব্যবস্থা অন্তর্ভুক্ত করা যা ক্ষতিকর আচরণ সনাক্ত এবং প্রতিরোধ করতে পারে। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) একটি স্বাধীন সুরক্ষা স্তর প্রদান করে, যা অ্যাপ্লিকেশন এবং পরিষেবাগুলিতে ক্ষতিকর ব্যবহারকারী-উৎপন্ন এবং AI-উৎপন্ন বিষয়বস্তু সনাক্ত করতে সক্ষম। Azure AI Content Safety টেক্সট এবং ইমেজ API অন্তর্ভুক্ত করে যা ক্ষতিকর উপাদান সনাক্ত করতে সাহায্য করে। Azure AI Foundry-তে, Content Safety পরিষেবা বিভিন্ন মোডালিটিতে ক্ষতিকর বিষয়বস্তু সনাক্ত করার জন্য নমুনা কোড দেখার, অন্বেষণ করার এবং চেষ্টা করার সুযোগ দেয়। নিম্নলিখিত [কুইকস্টার্ট ডকুমেন্টেশন](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) আপনাকে পরিষেবার জন্য অনুরোধ করার প্রক্রিয়া শেখায়।

আরেকটি গুরুত্বপূর্ণ বিষয় হলো সামগ্রিক অ্যাপ্লিকেশন পারফরম্যান্স। মাল্টি-মোডাল এবং মাল্টি-মডেল অ্যাপ্লিকেশনের ক্ষেত্রে, পারফরম্যান্স বলতে বোঝায় যে সিস্টেমটি আপনার এবং আপনার ব্যবহারকারীদের প্রত্যাশা অনুযায়ী কাজ করে, যার মধ্যে ক্ষতিকর আউটপুট তৈরি না করাও অন্তর্ভুক্ত। আপনার সামগ্রিক অ্যাপ্লিকেশনের পারফরম্যান্স মূল্যায়ন করতে [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ব্যবহার করুন। আপনি [কাস্টম ইভ্যালুয়েটর](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) তৈরি এবং মূল্যায়ন করার ক্ষমতাও পাবেন।

আপনার ডেভেলপমেন্ট এনভায়রনমেন্টে [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ব্যবহার করে আপনার AI অ্যাপ্লিকেশন মূল্যায়ন করতে পারেন। একটি টেস্ট ডেটাসেট বা একটি লক্ষ্য দেওয়া হলে, আপনার জেনারেটিভ AI অ্যাপ্লিকেশনের আউটপুটগুলো বিল্ট-ইন ইভ্যালুয়েটর বা আপনার পছন্দের কাস্টম ইভ্যালুয়েটর দিয়ে পরিমাণগতভাবে পরিমাপ করা হয়। আপনার সিস্টেম মূল্যায়ন করতে Azure AI Evaluation SDK দিয়ে শুরু করতে, [কুইকস্টার্ট গাইড](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) অনুসরণ করুন। একবার আপনি একটি মূল্যায়ন রান সম্পন্ন করলে, আপনি [Azure AI Foundry-তে ফলাফল ভিজুয়ালাইজ করতে পারেন](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)।

## ট্রেডমার্ক

এই প্রকল্পে প্রকল্প, পণ্য বা পরিষেবার জন্য ট্রেডমার্ক বা লোগো থাকতে পারে। Microsoft ট্রেডমার্ক বা লোগো ব্যবহারের অনুমোদিত ব্যবহার [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) অনুসরণ করতে হবে। এই প্রকল্পের পরিবর্তিত সংস্করণে Microsoft ট্রেডমার্ক বা লোগো ব্যবহার বিভ্রান্তি সৃষ্টি করতে বা Microsoft স্পনসরশিপ বোঝাতে পারে না। তৃতীয় পক্ষের ট্রেডমার্ক বা লোগো ব্যবহার সেই তৃতীয় পক্ষের নীতিমালার অধীন।

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।