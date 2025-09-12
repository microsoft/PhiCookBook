<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T14:20:42+00:00",
  "source_file": "README.md",
  "language_code": "my"
}
-->
# Phi Cookbook: Microsoft ရဲ့ Phi မော်ဒယ်များနှင့် လက်တွေ့အသုံးပြုနည်းများ

Phi သည် Microsoft မှ ဖွံ့ဖြိုးတိုးတက်စေသော အခမဲ့ AI မော်ဒယ်များ စီးရီးတစ်ခုဖြစ်သည်။

Phi သည် လက်ရှိအချိန်တွင် အကောင်းဆုံးနှင့် စျေးနှုန်းသက်သာသော Small Language Model (SLM) ဖြစ်ပြီး၊ ဘာသာစကားများစွာ၊ အကြောင်းအရာဆင်ခြင်း၊ စာသား/စကားပြော ဖန်တီးခြင်း၊ ကုဒ်ရေးခြင်း၊ ပုံများ၊ အသံများနှင့် အခြားအခြေအနေများတွင် အလွန်ကောင်းမွန်သော စမ်းသပ်မှုရလဒ်များ ရရှိထားသည်။

Phi ကို cloud သို့မဟုတ် edge devices တွင် တင်ဆောင်နိုင်ပြီး၊ အနည်းငယ်သော ကွန်ပျူတာစွမ်းအားဖြင့် Generative AI အက်ပလီကေးရှင်းများကို လွယ်ကူစွာ တည်ဆောက်နိုင်သည်။

ဤအရင်းအမြစ်များကို အသုံးပြုရန် အောက်ပါအဆင့်များကို လိုက်နာပါ:
1. **Repository ကို Fork လုပ်ပါ**: [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo) ကို နှိပ်ပါ။
2. **Repository ကို Clone လုပ်ပါ**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord Community ကို Join လုပ်ပြီး ကျွမ်းကျင်သူများနှင့် ဖွံ့ဖြိုးသူများနှင့် တွေ့ဆုံပါ**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 Multi-Language Support

#### GitHub Action မှတဆင့် ပံ့ပိုးထားသည် (အလိုအလျောက် & အမြဲ Update ဖြစ်နေသည်)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) 
[Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)

## အကြောင်းအရာများ

- အကျဉ်းချုပ်
  - [Phi မိသားစုမှ ကြိုဆိုပါသည်](./md/01.Introduction/01/01.PhiFamily.md)
  - [သင့်ပတ်ဝန်းကျင်ကို စတင်တည်ဆောက်ခြင်း](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [အဓိကနည်းပညာများကို နားလည်ခြင်း](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi မော်ဒယ်များအတွက် AI လုံခြုံရေး](./md/01.Introduction/01/01.AISafety.md)
  - [Phi Hardware ပံ့ပိုးမှု](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi မော်ဒယ်များနှင့် Platform များအတွင်း ရရှိနိုင်မှု](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai နှင့် Phi ကို အသုံးပြုခြင်း](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace Models](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- Phi ကို အခြားပတ်ဝန်းကျင်များတွင် Inference လုပ်ခြင်း
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
    - [AI Toolkit အသုံးပြု၍ Remote Server တွင် Phi ကို Inference လုပ်ခြင်း](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust ဖြင့် Phi ကို Inference လုပ်ခြင်း](./md/01.Introduction/03/Rust_Inference.md)
    - [Local တွင် Phi--Vision ကို Inference လုပ်ခြင်း](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (တရားဝင်ပံ့ပိုးမှု) ဖြင့် Phi ကို Inference လုပ်ခြင်း](./md/01.Introduction/03/Kaito_Inference.md)

-  [Phi မိသားစုကို Quantify လုပ်ခြင်း](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ဖြင့် Phi-3.5 / 4 ကို Quantize လုပ်ခြင်း](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime အတွက် Generative AI extensions ဖြင့် Phi-3.5 / 4 ကို Quantize လုပ်ခြင်း](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ဖြင့် Phi-3.5 / 4 ကို Quantize လုပ်ခြင်း](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework ဖြင့် Phi-3.5 / 4 ကို Quantize လုပ်ခြင်း](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi ကို အကဲဖြတ်ခြင်း
    - [Response AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Evaluation အတွက် Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow ကို အသုံးပြု၍ Evaluation လုပ်ခြင်း](./md/01.Introduction/05/Promptflow.md)

- Azure AI Search ဖြင့် RAG
    - [Phi-4-mini နှင့် Phi-4-multimodal (RAG) ကို Azure AI Search ဖြင့် အသုံးပြုနည်း](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi အက်ပလီကေးရှင်း ဖွံ့ဖြိုးမှု နမူနာများ
  - စာသားနှင့် စကားပြော အက်ပလီကေးရှင်းများ
    - Phi-4 နမူနာများ 🆕
      - [📓] [Phi-4-mini ONNX Model ဖြင့် Chat လုပ်ခြင်း](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 local ONNX Model .NET ဖြင့် Chat လုပ်ခြင်း](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel အသုံးပြု၍ Phi-4 ONNX ဖြင့် .NET Console App Chat](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 နမူနာများ
      - [Phi3, ONNX Runtime Web နှင့် WebGPU အသုံးပြု၍ browser တွင် Local Chatbot](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - Phi-3-mini နှင့် OpenAI Whisper ကို Interactive လုပ်ခြင်း](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Wrapper တည်ဆောက်ပြီး Phi-3 ကို MLFlow ဖြင့် အသုံးပြုခြင်း](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Model Optimization - Olive ဖြင့် ONNX Runtime Web အတွက် Phi-3-min model ကို Optimize လုပ်နည်း](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 App ဖြင့် Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3 Multi Model AI Powered Notes App နမူနာ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Fine-tune နှင့် Prompt flow ဖြင့် အထူးပြု Phi-3 မော်ဒယ်များကို ပေါင်းစပ်အသုံးပြုခြင်း](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)  
- [Azure AI Foundry တွင် Prompt flow ဖြင့် အထူးပြု Phi-3 မော်ဒယ်များကို ပေါင်းစပ်အသုံးပြုခြင်း](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)  
- [Microsoft ၏ တာဝန်ရှိ AI မူဝါဒများကို အခြေခံ၍ Azure AI Foundry တွင် Fine-tuned Phi-3 / Phi-3.5 မော်ဒယ်ကို အကဲဖြတ်ခြင်း](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)  
- [📓] [Phi-3.5-mini-instruct ဘာသာစကားခန့်မှန်းမှု နမူနာ (တရုတ်/အင်္ဂလိပ်)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)  
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)  
- [Windows GPU ကို အသုံးပြု၍ Phi-3.5-Instruct ONNX ဖြင့် Prompt flow ဖြေရှင်းချက် ဖန်တီးခြင်း](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)  
- [Microsoft Phi-3.5 tflite ကို အသုံးပြု၍ Android အက်ပ် ဖန်တီးခြင်း](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)  
- [Microsoft.ML.OnnxRuntime ကို အသုံးပြု၍ ဒေသခံ ONNX Phi-3 မော်ဒယ်ဖြင့် Q&A .NET နမူနာ](../../md/04.HOL/dotnet/src/LabsPhi301)  
- [Semantic Kernel နှင့် Phi-3 ဖြင့် Console chat .NET အက်ပ်](../../md/04.HOL/dotnet/src/LabsPhi302)  

- Azure AI Inference SDK ကို အခြေခံထားသော နမူနာများ  
  - Phi-4 နမူနာများ 🆕  
    - [📓] [Phi-4-multimodal ကို အသုံးပြု၍ ပရောဂျက်ကုဒ် ဖန်တီးခြင်း](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Phi-3 / 3.5 နမူနာများ  
    - [Microsoft Phi-3 မျိုးဆက်ဖြင့် သင့် Visual Studio Code GitHub Copilot Chat ကို ဖန်တီးခြင်း](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [GitHub မော်ဒယ်များဖြင့် Phi-3.5 ဖြင့် သင့် Visual Studio Code Chat Copilot Agent ကို ဖန်တီးခြင်း](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- အဆင့်မြင့် အကြောင်းအရာဆန်းစစ် နမူနာများ  
  - Phi-4 နမူနာများ 🆕  
    - [📓] [Phi-4-mini-reasoning သို့မဟုတ် Phi-4-reasoning နမူနာများ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Microsoft Olive ဖြင့် Phi-4-mini-reasoning ကို Fine-tuning ပြုလုပ်ခြင်း](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Apple MLX ဖြင့် Phi-4-mini-reasoning ကို Fine-tuning ပြုလုပ်ခြင်း](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [GitHub မော်ဒယ်များဖြင့် Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Azure AI Foundry မော်ဒယ်များဖြင့် Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  

- နမူနာများ  
  - [Hugging Face Spaces တွင် ဖော်ပြထားသော Phi-4-mini နမူနာများ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
  - [Hugging Face Spaces တွင် ဖော်ပြထားသော Phi-4-multimodal နမူနာများ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  

- ရုပ်ပုံနမူနာများ  
  - Phi-4 နမူနာများ 🆕  
    - [📓] [Phi-4-multimodal ကို အသုံးပြု၍ ရုပ်ပုံများ ဖတ်ပြီး ကုဒ် ဖန်တီးခြင်း](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Phi-3 / 3.5 နမူနာများ  
    - [📓][Phi-3-vision-Image text to text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [DEMO: Phi-3 ပြန်လည်အသုံးပြုခြင်း](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - Visual language assistant - Phi3-Vision နှင့် OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision multi-frame သို့မဟုတ် multi-image နမူနာ](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Microsoft.ML.OnnxRuntime .NET ကို အသုံးပြု၍ ဒေသခံ ONNX မော်ဒယ်ဖြင့် Phi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Menu အခြေပြု Phi-3 Vision ဒေသခံ ONNX မော်ဒယ်](../../md/04.HOL/dotnet/src/LabsPhi304)  

- သင်္ချာနမူနာများ  
  - Phi-4-Mini-Flash-Reasoning-Instruct နမူနာများ 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct ဖြင့် သင်္ချာ နမူနာ](../../md/02.Application/09.Math/MathDemo.ipynb)  

- အသံနမူနာများ  
  - Phi-4 နမူနာများ 🆕  
    - [📓] [Phi-4-multimodal ကို အသုံးပြု၍ အသံစာတမ်းများ ထုတ်ယူခြင်း](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Phi-4-multimodal အသံနမူနာ](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Phi-4-multimodal အသံဘာသာပြန်နမူနာ](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [.NET console application ကို အသုံးပြု၍ Phi-4-multimodal အသံဖိုင်ကို ခွဲခြမ်းစိတ်ဖြာပြီး စာတမ်းထုတ်ယူခြင်း](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- MOE နမူနာများ  
  - Phi-3 / 3.5 နမူနာများ  
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) လူမှုမီဒီယာ နမူနာ](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, နှင့် LlamaIndex ဖြင့် RAG Pipeline တည်ဆောက်ခြင်း](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- Function Calling နမူနာများ  
  - Phi-4 နမူနာများ 🆕  
    - [📓] [Phi-4-mini ဖြင့် Function Calling အသုံးပြုခြင်း](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Phi-4-mini ဖြင့် multi-agents ဖန်တီးရန် Function Calling အသုံးပြုခြင်း](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Ollama ဖြင့် Function Calling အသုံးပြုခြင်း](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [ONNX ဖြင့် Function Calling အသုံးပြုခြင်း](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- Multimodal Mixing နမူနာများ  
  - Phi-4 နမူနာများ 🆕  
    - [📓] [Phi-4-multimodal ကို နည်းပညာသတင်းထောက်အဖြစ် အသုံးပြုခြင်း](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [.NET console application ကို အသုံးပြု၍ Phi-4-multimodal ဖြင့် ရုပ်ပုံများ ခွဲခြမ်းစိတ်ဖြာခြင်း](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Fine-tuning Phi နမူနာများ  
  - [Fine-tuning ရှုခင်းများ](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [Fine-tuning နှင့် RAG နှိုင်းယှဉ်ခြင်း](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Fine-tuning ဖြင့် Phi-3 ကို စက်မှုလုပ်ငန်းကျွမ်းကျင်သူအဖြစ် ပြောင်းလဲခြင်း](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [AI Toolkit for VS Code ဖြင့် Phi-3 ကို Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Azure Machine Learning Service ဖြင့် Phi-3 ကို Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Lora ဖြင့် Phi-3 ကို Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/FineTuning_Lora.md)  
  - [QLora ဖြင့် Phi-3 ကို Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Azure AI Foundry ဖြင့် Phi-3 ကို Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Azure ML CLI/SDK ဖြင့် Phi-3 ကို Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Microsoft Olive ဖြင့် Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Microsoft Olive Hands-On Lab ဖြင့် Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/olive-lab/readme.md)  
  - [Weights and Bias ဖြင့် Phi-3-vision ကို Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Apple MLX Framework ဖြင့် Phi-3 ကို Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Phi-3-vision ကို Fine-tuning ပြုလုပ်ခြင်း (တရားဝင်ပံ့ပိုးမှု)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Kaito AKS နှင့် Azure Containers ဖြင့် Phi-3 ကို Fine-tuning ပြုလုပ်ခြင်း (တရားဝင်ပံ့ပိုးမှု)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Phi-3 နှင့် 3.5 Vision ကို Fine-tuning ပြုလုပ်ခြင်း](https://github.com/2U1/Phi3-Vision-Finetune)  

- လက်တွေ့အလုပ်ခန်း  
  - [အဆင့်မြင့်မော်ဒယ်များကို စူးစမ်းခြင်း: LLMs, SLMs, ဒေသခံဖွံ့ဖြိုးမှုနှင့် အခြားများ](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [NLP အလားအလာကို ဖွင့်လှစ်ခြင်း: Microsoft Olive ဖြင့် Fine-Tuning](https://github.com/azure/Ignite_FineTuning_workshop)  

- ပညာရေးသုတေသနစာတမ်းများနှင့် ထုတ်ပြန်ချက်များ  
  - [Textbooks Are All You Need II: phi-1.5 နည်းပညာအစီရင်ခံစာ](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 နည်းပညာအစီရင်ခံစာ: သင့်ဖုန်းပေါ်တွင် ဒေသခံအခြေပြု အလွန်တော်သော ဘာသာစကားမော်ဒယ်](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 နည်းပညာအစီရင်ခံစာ](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini နည်းပညာအစီရင်ခံစာ: Mixture-of-LoRAs ဖြင့် Compact သို့မဟုတ် အင်အားကြီးသော Multimodal ဘာသာစကားမော်ဒယ်များ](https://arxiv.org/abs/2503.01743)  
  - [In-Vehicle Function-Calling အတွက် Small Language Models ကို အကောင်းဆုံးဖြစ်အောင် ပြုလုပ်ခြင်း](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) Fine-Tuning PHI-3 for Multiple-Choice Question Answering: နည်းလမ်းများ, ရလဒ်များ, နှင့် စိန်ခေါ်မှုများ](https://arxiv.org/abs/2501.01588)  
- [Phi-4-reasoning Technical Report](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning Technical Report](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)  

## Phi မော်ဒယ်များ အသုံးပြုခြင်း  

### Azure AI Foundry တွင် Phi  

Microsoft Phi ကို ဘယ်လိုအသုံးပြုရမလဲ၊ သင့် hardware စက်ပစ္စည်းများတွင် E2E ဖြေရှင်းချက်များကို ဘယ်လိုတည်ဆောက်ရမလဲကို သင်ယူနိုင်ပါသည်။ Phi ကို ကိုယ်တိုင်အတွေ့အကြုံရရှိရန်၊ မော်ဒယ်များကို စမ်းသပ်ပြီး သင့်အခြေအနေများအတွက် Phi ကို customize လုပ်ခြင်းဖြင့် စတင်ပါ။ [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) တွင် သင်ယူနိုင်ပြီး [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) တွင် စတင်အသုံးပြုရန် လမ်းညွှန်ချက်များကိုလည်း ရှာဖွေနိုင်ပါသည်။  

**Playground**  
မော်ဒယ်တစ်ခုစီတွင် မော်ဒယ်ကို စမ်းသပ်ရန်အတွက် အထူးပြုထားသော playground ရှိပါသည်။ [Azure AI Playground](https://aka.ms/try-phi3) တွင် စမ်းသပ်နိုင်ပါသည်။  

### GitHub Models တွင် Phi  

Microsoft Phi ကို ဘယ်လိုအသုံးပြုရမလဲ၊ သင့် hardware စက်ပစ္စည်းများတွင် E2E ဖြေရှင်းချက်များကို ဘယ်လိုတည်ဆောက်ရမလဲကို သင်ယူနိုင်ပါသည်။ Phi ကို ကိုယ်တိုင်အတွေ့အကြုံရရှိရန်၊ မော်ဒယ်ကို စမ်းသပ်ပြီး သင့်အခြေအနေများအတွက် Phi ကို customize လုပ်ခြင်းဖြင့် စတင်ပါ။ [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) တွင် သင်ယူနိုင်ပြီး [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) တွင် စတင်အသုံးပြုရန် လမ်းညွှန်ချက်များကိုလည်း ရှာဖွေနိုင်ပါသည်။  

**Playground**  
မော်ဒယ်တစ်ခုစီတွင် [မော်ဒယ်ကို စမ်းသပ်ရန်အတွက် playground](/md/02.QuickStart/GitHubModel_QuickStart.md) ရှိပါသည်။  

### Hugging Face တွင် Phi  

မော်ဒယ်ကို [Hugging Face](https://huggingface.co/microsoft) တွင်လည်း ရှာဖွေနိုင်ပါသည်။  

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)  

## တာဝန်ယူမှုရှိသော AI  

Microsoft သည် AI ထုတ်ကုန်များကို တာဝန်ယူမှုရှိစွာ အသုံးပြုရန်အတွက် ကျွန်ုပ်တို့၏ဖောက်သည်များကို ကူညီပေးရန်၊ ကျွန်ုပ်တို့၏အတွေ့အကြုံများကို မျှဝေရန်နှင့် Transparency Notes နှင့် Impact Assessments ကဲ့သို့သော tools များမှတစ်ဆင့် ယုံကြည်မှုအခြေခံထားသော မိတ်ဖက်ဆက်ဆံရေးများ တည်ဆောက်ရန် အတတ်နိုင်ဆုံး ကြိုးစားနေပါသည်။ အများစုသော အရင်းအမြစ်များကို [https://aka.ms/RAI](https://aka.ms/RAI) တွင် ရှာဖွေနိုင်ပါသည်။  
Microsoft ၏ တာဝန်ယူမှုရှိသော AI အပေါ်ရပ်တည်မှုသည် ကျွန်ုပ်တို့၏ AI အခြေခံသဘောတရားများဖြစ်သော တရားမျှတမှု၊ ယုံကြည်စိတ်ချရမှုနှင့် လုံခြုံမှု၊ ကိုယ်ရေးအချက်အလက်နှင့် လုံခြုံရေး၊ ပါဝင်မှု၊ ထင်ရှားမှုနှင့် တာဝန်ယူမှုတို့ကို အခြေခံထားပါသည်။  

ဤနမူနာတွင် အသုံးပြုထားသော သဘာဝဘာသာစကား၊ ပုံရိပ်နှင့် အသံ မော်ဒယ်များက မတရား၊ ယုံကြည်စိတ်မချရမှု သို့မဟုတ် စိတ်ထိခိုက်စေသော အပြုအမူများကို ဖြစ်ပေါ်စေနိုင်ပြီး ထိခိုက်မှုများ ဖြစ်ပေါ်စေနိုင်ပါသည်။ [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ကို ဖတ်ရှုခြင်းဖြင့် အန္တရာယ်များနှင့် ကန့်သတ်ချက်များအကြောင်းကို သိရှိနိုင်ပါသည်။  

ဤအန္တရာယ်များကို လျှော့ချရန် အကြံပြုထားသော နည်းလမ်းမှာ သင့် architecture တွင် အန္တရာယ်ရှိသော အပြုအမူများကို ရှာဖွေပြီး ကာကွယ်နိုင်သော safety system တစ်ခုကို ထည့်သွင်းရန်ဖြစ်သည်။ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) သည် အန္တရာယ်ရှိသော user-generated နှင့် AI-generated content ကို applications နှင့် services တွင် ရှာဖွေနိုင်သော လွတ်လပ်သော ကာကွယ်မှုအလွှာတစ်ခုကို ပေးစွမ်းပါသည်။ Azure AI Content Safety တွင် အန္တရာယ်ရှိသော အကြောင်းအရာများကို ရှာဖွေရန် text နှင့် image APIs ပါဝင်ပြီး၊ Azure AI Foundry တွင် Content Safety service သည် modality များအနှံ့ အန္တရာယ်ရှိသော အကြောင်းအရာများကို ရှာဖွေရန် နမူနာ code များကို ကြည့်ရှု၊ စမ်းသပ်နိုင်ရန် ခွင့်ပြုပါသည်။ [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) သည် service သို့ request များလုပ်ရန် လမ်းညွှန်ချက်များကို ပေးပါသည်။  

တစ်ခြားအရေးပါသော အချက်မှာ application စွမ်းဆောင်ရည်အားလုံးကို ထည့်သွင်းစဉ်းစားရန်ဖြစ်သည်။ multi-modal နှင့် multi-models applications တွင် စွမ်းဆောင်ရည်သည် သင့်နှင့် သင့် user များ၏ မျှော်လင့်ချက်နှင့်အညီ စနစ်က အလုပ်လုပ်သည်ကို ဆိုလိုပြီး အန္တရာယ်ရှိသော output များကို မထုတ်လုပ်ပါ။ [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ကို အသုံးပြုခြင်းဖြင့် application စွမ်းဆောင်ရည်ကို အကဲဖြတ်ရန် အရေးကြီးပါသည်။ သင့်စနစ်ကို အကဲဖြတ်ရန် [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ကို ဖန်တီးပြီး အကဲဖြတ်နိုင်ပါသည်။  

သင့် AI application ကို development environment တွင် [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ကို အသုံးပြု၍ အကဲဖြတ်နိုင်ပါသည်။ test dataset သို့မဟုတ် target တစ်ခုကို အသုံးပြု၍ သင့် generative AI application ၏ generation များကို built-in evaluators သို့မဟုတ် သင့်ရွေးချယ်မှုအတိုင်း custom evaluators များဖြင့် အရည်အသွေးကို တိုင်းတာနိုင်ပါသည်။ azure ai evaluation sdk ကို အသုံးပြု၍ သင့်စနစ်ကို အကဲဖြတ်ရန် [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ကို လိုက်နာနိုင်ပါသည်။ evaluation run တစ်ခုကို အကောင်အထည်ဖော်ပြီးနောက် [Azure AI Foundry တွင် ရလဒ်များကို ကြည့်ရှုနိုင်ပါသည်](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)။  

## အမှတ်တံဆိပ်များ  

ဤ project တွင် project များ၊ product များ သို့မဟုတ် service များအတွက် အမှတ်တံဆိပ်များ သို့မဟုတ် logo များ ပါဝင်နိုင်ပါသည်။ Microsoft အမှတ်တံဆိပ်များ သို့မဟုတ် logo များကို အသုံးပြုရန် ခွင့်ပြုချက်သည် [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ကို လိုက်နာရမည်ဖြစ်သည်။  
ဤ project ၏ ပြင်ဆင်ထားသော version များတွင် Microsoft အမှတ်တံဆိပ်များ သို့မဟုတ် logo များကို အသုံးပြုခြင်းသည် ရှုပ်ထွေးမှုများ ဖြစ်ပေါ်စေခြင်း သို့မဟုတ် Microsoft ၏ အားပေးမှုကို ဖော်ပြခြင်း မဖြစ်စေရပါ။ တတိယအဖွဲ့အစည်း၏ အမှတ်တံဆိပ်များ သို့မဟုတ် logo များကို အသုံးပြုခြင်းသည် အဆိုပါ တတိယအဖွဲ့အစည်း၏ မူဝါဒများကို လိုက်နာရမည်ဖြစ်သည်။  

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှု ဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။