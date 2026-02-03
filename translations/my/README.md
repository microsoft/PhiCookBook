# Phi Cookbook: Microsoft ရဲ့ Phi မော်ဒယ်တွေနဲ့ လက်တွေ့ဥပမာများ

[![GitHub Codespaces မှာ ဥပမာတွေ ဖွင့်ပြီး အသုံးပြုပါ](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers မှာ ဖွင့်ပါ](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub အဖွဲ့ဝင်များ](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ပြဿနာများ](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs ကြိုဆိုပါသည်](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub ကြည့်ရှုသူများ](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub များဝှက်မှု](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ကြယ်များ](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi သည် Microsoft မှ ဖန်တီးထားသော open source AI မော်ဒယ်အစုတစ်ခု ဖြစ်သည်။

Phi သည် လက်ရှိအချိန်တွင် အားသာဆုံးနှင့် စျေးနှုန်းသက်သာဆုံးသော သေးငယ်သောဘာသာစကားမော်ဒယ် (SLM) ဖြစ်ပြီး၊ ဘာသာစကားစုံ၊ သဘောတရားနားလည်မှု၊ စာသား/စကားပြောထုတ်လုပ်မှု၊ ကုဒ်ရေးခြင်း၊ ပုံရိပ်များ၊ အသံနှင့် အခြားအခြေအနေများတွင် ကောင်းမွန်သော စမ်းသပ်မှုများ ရရှိထားသည်။

Phi ကို မိမိ၏ cloud သို့မဟုတ် edge ကိရိယာများတွင် ထည့်သွင်းအသုံးပြုနိုင်ပြီး၊ ကန့်သတ်ထားသော ကွန်ပြူတာစွမ်းအားဖြင့် လွယ်ကူစွာ generative AI အက်ပ်များတည်ဆောက်နိုင်သည်။

ဤရင်းမြစ်များကို အသုံးပြမှုစတင်ရန် အောက်ပါအဆင့်များကို လိုက်နာပါ-
1. **Repository ကို Fork လုပ်ပါ**: Click [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Repository ကို Clone လုပ်ပါ**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord စာရင်းသွင်းပြီး ကျွမ်းကျင်သူများနှင့် အတူဖွံ့ဖြိုးရေးသူများနှင့် တွေ့ဆုံခြင်း**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/my/cover.eb18d1b9605d754b.webp)

### 🌐 ဘာသာစကားစုံအထောက်အပံ့

#### GitHub Action ဖြင့်ထောက်ပံ့သည် (အလိုအလျောက် နှင့် အမြဲတမ်း အသစ်ကြိုက်)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](./README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ဒေသတွင်း Clone သဘောကို ထားပါသလား?**

> ဤ repository တွင် ၅၀ ကျော် ဘာသာစကားဘာသာပြန်ချက်များ ပါဝင်ပြီး ဒါကြောင့် ဒေါင်းလုပ်အရွယ်အစား မြင့်တက်သည်။ ဘာသာပြန်ချက်များ မပါဘဲ clone လုပ်ရန် sparse checkout ကိုအသုံးပြုပါ-
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> ၎င်းက သင်ယူမှုအတွက် လိုအပ်သော အရာအားလုံးကို ပိုမြန်ဆန်စွာ ဒေါင်းလုပ်လုပ်နိုင်စေသည်။
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## စာရွက်စာတမ်း အညွှန်းစာရင်း

- အကြောင်းအရာ
  - [Phi မိသားစုသို့ လာရောက်ကြိုဆိုပါသည်](./md/01.Introduction/01/01.PhiFamily.md)
  - [သင့် ပတ်ဝန်းကျင် စီစဉ်ခြင်း](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [အဓိက နည်းပညာများနားလည်ခြင်း](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi မော်ဒယ်များအတွက် AI လုံခြုံရေး](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ဟာ့ဒ်ဝဲထောက်ပံ့မှု](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi မော်ဒယ်များနှင့် ပလက်ဖောင်းပေါ်ရှိ ရရှိနိုင်မှု](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai နှင့် Phi အသုံးပြုခြင်း](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace မော်ဒယ်များ](https://github.com/marketplace/models)
  - [Azure AI မော်ဒယ်ကတ်တလော](https://ai.azure.com)

- ပတ်ဝန်းကျင်အမျိုးမျိုး၌ Phi မော်ဒယ်ကို ရွေးချယ် အသုံးပြုခြင်း
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub မော်ဒယ်များ](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry မော်ဒယ်ကတ်တလော](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry ဒေသတွင်း](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi မိသားစုမော်ဒယ် ကို အသုံးပြုခြင်း
    - [iOS တွင် Phi မော်ဒယ် အသုံးပြုခြင်း](./md/01.Introduction/03/iOS_Inference.md)
    - [Android တွင် Phi မော်ဒယ် အသုံးပြုခြင်း](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson တွင် Phi မော်ဒယ် အသုံးပြုခြင်း](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC တွင် Phi မော်ဒယ် အသုံးပြုခြင်း](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework ဖြင့် Phi မော်ဒယ် အသုံးပြုခြင်း](./md/01.Introduction/03/MLX_Inference.md)
    - [ဒေသတွင်း ဆာဗာတွင် Phi မော်ဒယ် အသုံးပြုခြင်း](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit အသုံးပြု ကိရိယာခွဲ ဆာဗာ့မှ Phi မော်ဒယ် အသုံးပြုခြင်း](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust ဖြင့် Phi မော်ဒယ် အသုံးပြုခြင်း](./md/01.Introduction/03/Rust_Inference.md)
    - [ဒေသတွင်း Phi Vision မော်ဒယ် အသုံးပြုခြင်း](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (တရားဝင် ထောက်ပံ့မှု) ဖြင့် Phi မော်ဒယ် အသုံးပြုခြင်း](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi မိသားစုကို ရေတွက်ခြင်း](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ဖြင့် Phi-3.5 / 4 ကို Quantize လုပ်ခြင်း](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime အတွက် Generative AI ဆွဲဆောင်မှုများနှင့် Phi-3.5 / 4 ကို Quantize လုပ်ခြင်း](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ဖြင့် Phi-3.5 / 4 ကို Quantize လုပ်ခြင်း](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework ဖြင့် Phi-3.5 / 4 ကို Quantize လုပ်ခြင်း](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi မော်ဒယ် ပိုင်း ဆန်းစစ်ခြင်း
    - [တာဝန်ရှိသော AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry ဖြင့် ဆန်းစစ်ခြင်း](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow အား အသုံးပြုပြီး ဆန်းစစ်ခြင်း](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search နှင့် RAG
    - [Phi-4-mini နှင့် Phi-4-multimodal (RAG) ကို Azure AI Search နှင့် အသုံးပြုနည်း](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi အက်ပ်ဖွံ့ဖြိုးမှု ဥပမာများ
  - စာသား နှင့် စကားပြောအက်ပ်များ
    - Phi-4 ဥပမာများ 🆕
      - [📓] [Phi-4-mini ONNX မော်ဒယ်ဖြင့် စကားပြောခြင်း](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 ဒေသတွင်း ONNX မော်ဒယ် .NET ဖြင့် စကားပြောခြင်း](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Semantic Kernel ဖြင့် Phi-4 ONNX အသုံးပြု .NET Console App စကားပြော](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 ဥပမာများ
      - [Phi3, ONNX Runtime Web နှင့် WebGPU ကို အသုံးပြုပြီး ဒေါင်းလာအတွင်း ဒေသတွင်း စကားပြော chatbot](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino စကားပြော](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - အပြန်အလှန် Phi-3-mini နှင့် OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - wrapper တစ်ခု တည်ဆောက်ခြင်းနှင့် Phi-3 ကို MLFlow ဖြင့် အသုံးပြုခြင်း](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Model Optimization - ONNX Runtime Web 用အတွက် Phi-3-min မော်ဒယ်ကို Olive ဖြင့် မည်သို့ optimize ဆောင်ရွက်မည်ဆိုတာ](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx ဖြင့် WinUI3 App](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 Multi Model AI Powered Notes App Sample](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Fine-tune နှင့် Prompt flow ဖြင့် မိမိစိတ်ကြိုက် Phi-3 မော်ဒယ်များကို ပေါင်းစည်းခြင်း](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry တွင် Prompt flow အသုံးပြုပြီး မိမိစိတ်ကြိုက် Phi-3 မော်ဒယ်များကို Fine-tune နှင့် ပေါင်းစည်းခြင်း](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft ရဲ့ တာဝန်ခံ AI စည်းမျဉ်းစည်းကမ်းများကို အခြေခံ၍ Azure AI Foundry တွင် Fine-tuned Phi-3 / Phi-3.5 မော်ဒယ်ကို အကဲဖြတ်ခြင်း](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct ဘာသာစကားခန့်မှန်းချက် နမူနာ (တရုတ်၊ အင်္ဂလိပ်)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Phi-3.5-Instruct ONNX ဖြင့် Prompt flow ဖြေရှင်းချက်ကို Windows GPU အသုံးပြု၍ ဖန်တီးခြင်း](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite ကို အသုံးပြု၍ Android app ဖန်တီးခြင်း](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime ကို အသုံးပြု၍ ဒေသဆိုင်ရာ ONNX Phi-3 မော်ဒယ်ဖြင့် Q&A .NET နမူနာ](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel နှင့် Phi-3 ဖြင့် Console chat .NET app](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK ကုဒ်အခြေပြု နမူနာများ
    - Phi-4 နမူနာများ 🆕
      - [📓] [Phi-4-multimodal အသုံးပြု၍ စီမံကိန်းကုဒ် ထုတ်လုပ်ခြင်း](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 နမူနာများ
      - [Microsoft Phi-3 မိသားစုဖြင့် မိမိ Visual Studio Code GitHub Copilot Chat ကို တည်ဆောက်ပါ](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub Models ဖြင့် Phi-3.5 ကို အသုံးပြုပြီး မိမိ Visual Studio Code Chat Copilot Agent ဖန်တီးပါ](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - အဆင့်မြင့် အမြှုပ်နှုတ် နမူနာများ
    - Phi-4 နမူနာများ 🆕
      - [📓] [Phi-4-mini-reasoning သို့မဟုတ် Phi-4-reasoning နမူနာများ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive ဖြင့် Phi-4-mini-reasoning ကို fine-tune ဆောင်ရွက်ခြင်း](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX ဖြင့် Phi-4-mini-reasoning ကို fine-tune ဆောင်ရွက်ခြင်း](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub Models ဖြင့် Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry Models ဖြင့် Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - ပြသမှုများ
      - [Phi-4-mini demos များကို Hugging Face Spaces တွင် အဖွင့်ထားမှု](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demos များကို Hugginge Face Spaces တွင် အဖွင့်ထားမှု](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - ရုပ်မြင်သံကြား နမူနာများ
    - Phi-4 နမူနာများ 🆕
      - [📓] [Phi-4-multimodal ကို အသုံးပြု၍ ပုံများ ဖတ်ခြင်းနှင့် ကုဒ်ထုတ်ဖန်တီးခြင်း](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 နမူနာများ
      -  [📓][Phi-3-vision-ပုံမှ စာသားသို့ သို့သွားခြင်း](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ပြသမှု- Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - ရုပ်မြင်သံကြားဘာသာဖြင့် ကူညီကူရွှေ့သူ - Phi3-Vision နှင့် OpenVINO ဖြင့်](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision multi-frame သို့မဟုတ် multi-image နမူနာ](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET ဖြင့် Phi-3 Vision ဒေသဆိုင်ရာ ONNX မော်ဒယ်](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Microsoft.ML.OnnxRuntime .NET ဖြင့် menu အခြေပြု Phi-3 Vision ဒေသဆိုင်ရာ ONNX မော်ဒယ်](../../md/04.HOL/dotnet/src/LabsPhi304)

  - သင်္ချာနမူနာများ
    - Phi-4-Mini-Flash-Reasoning-Instruct နမူနာများ 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct ဖြင့် သင်္ချာ ပြသမှု](./md/02.Application/09.Math/MathDemo.ipynb)

  - အသံနမူနာများ
    - Phi-4 နမူနာများ 🆕
      - [📓] [Phi-4-multimodal ဖြင့် အသံစာသားများ ထုတ်ယူခြင်း](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal အသံနမူနာ](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal စကားပြန်နမူနာ](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET console app ကို Phi-4-multimodal အသံဖိုင်ကို ခွဲခြမ်းစိတ်ဖြာပြီး စာသား ထုတ်လုပ်ရန် အသုံးပြုခြင်း](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE နမူနာများ
    - Phi-3 / 3.5 နမူနာများ
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) လူမှုကွန်ရက် နမူနာ](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search နှင့် LlamaIndex ဖြင့် Retrieval-Augmented Generation (RAG) Pipeline တည်ဆောက်ခြင်း](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Function Calling နမူနာများ
    - Phi-4 နမူနာများ 🆕
      -  [📓] [Phi-4-mini ဖြင့် Function Calling အသုံးပြုခြင်း](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini ဖြင့် multi-agents ဖန်တီးရန် Function Calling အသုံးပြုခြင်း](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama ဖြင့် Function Calling အသုံးပြုခြင်း](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX ဖြင့် Function Calling အသုံးပြုခြင်း](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Multimodal Mixing နမူနာများ
    - Phi-4 နမူနာများ 🆕
      -  [📓] [Phi-4-multimodal ကို နည်းပညာသတင်းထောက်အဖြစ် အသုံးပြုခြင်း](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET console app ကို Phi-4-multimodal ဖြင့် ပုံများ ခွဲခြမ်းစိတ်ဖြာရန် အသုံးပြုခြင်း](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi မော်ဒယ်များ Fine-tuning
  - [Fine-tuning အခြေအနားများ](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Fine-tuning နှင့် RAG ရှုထောင့်](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Fine-tuning - Phi-3 ကို စက်မှုလက်မှု ဗဟုသုတရှင်အဖြစ် ပြုလုပ်ခြင်း](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code အတွက် AI Toolkit ဖြင့် Phi-3 fine-tune ဆောင်ရွက်ခြင်း](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service ဖြင့် Phi-3 fine-tune ဆောင်ရွက်ခြင်း](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora ဖြင့် Phi-3 fine-tune ဆောင်ရွက်ခြင်း](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora ဖြင့် Phi-3 fine-tune ဆောင်ရွက်ခြင်း](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry ဖြင့် Phi-3 fine-tune ဆောင်ရွက်ခြင်း](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK ဖြင့် Phi-3 fine-tune ဆောင်ရွက်ခြင်း](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive ဖြင့် Fine-tuning ဆောင်ရွက်ခြင်း](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Lab ဖြင့် Fine-tuning ဆောင်ရွက်ခြင်း](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias ဖြင့် Phi-3-vision fine-tuning](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework ဖြင့် Phi-3 fine-tuning](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision (တရားဝင် ထောက်ပံ့မှု) fine-tuning](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers (တရားဝင် ထောက်ပံ့မှု) ဖြင့် Phi-3 fine-tuning](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 နှင့် 3.5 Vision fine-tuning](https://github.com/2U1/Phi3-Vision-Finetune)

- လက်တွေ့ လေ့ကျင့်ခန်း
  - [လတ်တလောနည်းပညာများ: LLM နှင့် SLM များ၊ ဒေသတွင်း ဖွံ့ဖြိုးတိုးတက်မှု နှင့် အခြားအရာများကို ရှာဖွေခြင်း](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP တိုးတက်မှု အခွင့်အရေးများ ချိတ်ဆက်ခြင်း: Microsoft Olive ဖြင့် Fine-Tuning](https://github.com/azure/Ignite_FineTuning_workshop)

- ပညာရေးဆိုင်ရာ သုတေသနစာတမ်းများ နှင့် ပုံနှိပ်စာများ
  - [စာအုပ်များသည် သင်လိုအပ်သည့်အရာများအားလုံးဖြစ်သည် II: phi-1.5 နည်းပညာအစီရင်ခံစာ](https://arxiv.org/abs/2309.05463)
  - [Phi-3 နည်းပညာအစီရင်ခံစာ: သင့်ဖုန်းပေါ်တွင် ဒေသန္တရ စွမ်းဆောင်ရည်မြင့် ဘာသာစကားမော်ဒယ်](https://arxiv.org/abs/2404.14219)
  - [Phi-4 နည်းပညာအစီရင်ခံစာ](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini နည်းပညာအစီရင်ခံစာ: Mixture-of-LoRAs ဖြင့် သေးငယ်သော်လည်း အင်အားကြီးသော မျိုးစုံမော်ဒယ်များ](https://arxiv.org/abs/2503.01743)
  - [ယာဉ်ထဲတွင် လုပ်ဆောင်မှုခေါ်ဆိုခြင်းအတွက် သေးငယ်သော ဘာသာစကားမော်ဒယ်များကို အောင့်ချိန်ညှိခြင်း](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 ကို မျိုးစုံရွေးချယ်စစ်ဆေးမှု မေးခွန်းဖြေဆိုမှုအတွက် စဉ်ဆက်မပြတ် ချိန်ညှိခြင်း: နည်းပညာ၊ ရလဒ်များနှင့် စိန်ခေါ်မှုများ](https://arxiv.org/abs/2501.01588)
  - [Phi-4-စဉ်းစားချက် နည်းပညာအစီရင်ခံစာ](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-စဉ်းစားချက် နည်းပညာအစီရင်ခံစာ](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi မော်ဒယ်များ အသုံးပြုခြင်း

### Azure AI Foundry ပေါ်တွင် Phi

Microsoft Phi ကို မည်သို့အသုံးပြုမည်နည်းနှင့် သင့်Hardware များတွင် E2E ဖြေရှင်းချက်များကို မည်သို့တည်ဆောက်မည်နည်းကို သင်ယူနိုင်သည်။ Phi ကို ကိုယ်တိုင်ခံစားလိုပါက မော်ဒယ်များနှင့် ဆော့ကစားခြင်းဖြင့် စတင်ရန်နှင့် သင့်ဖြေရှင်းနည်းများအတွက် Phi ကို အဓိကပြုလုပ်ရန် [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ကို အသုံးပြုပြီး သင်ယူနိုင်သည်။ Getting Started with [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) တွင် ပိုမိုသိရှိနိုင်ပါသည်။

**စမ်းသပ်ကစားရန် နေရာ**  
မော်ဒယ်တိုင်းသည် မော်ဒယ်ကို စမ်းသပ်ရန် အထူးသီးသန့် ဧရိယာတစ်ခုရှိသည် [Azure AI Playground](https://aka.ms/try-phi3)။

### GitHub မော်ဒယ်များပေါ် Phi

Microsoft Phi ကို မည်သို့အသုံးပြုမည်နည်းနှင့် သင့်Hardware များတွင် E2E ဖြေရှင်းချက်များကို မည်သို့တည်ဆောက်မည်နည်းကို သင်ယူနိုင်သည်။ Phi ကို ကိုယ်တိုင်ခံစားလိုပါက မော်ဒယ်နှင့် ဆော့ကစားခြင်းဖြင့် စတင်ပြီး သင့်ဖြေရှင်းနည်းများအတွက် Phi ကို အဓိကပြုလုပ်ရန် [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ကို အသုံးပြုပြီး သင်ယူနိုင်သည်။ Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) တွင် ပိုမိုသိရှိနိုင်ပါသည်။

**စမ်းသပ်ကစားရန် နေရာ**  
မော်ဒယ်တိုင်းတွင် မော်ဒယ်ကို စမ်းသပ်ရန် [စမ်းသပ်ကစားရန် နေရာ](/md/02.QuickStart/GitHubModel_QuickStart.md) တစ်ခုရှိသည်။

### Hugging Face ပေါ် Phi

မော်ဒယ်ကို [Hugging Face](https://huggingface.co/microsoft) ပေါ်တွင်လည်း ရှာဖွေတွေ့ရှိနိုင်သည်။

**စမ်းသပ်ကစားရန် နေရာ**  
[Hugging Chat စမ်းသပ်ကစားရန် နေရာ](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 အခြားသင်တန်းများ

ကျွန်ုပ်တို့အဖွဲ့သည် အခြားသင်တန်းများကို ထုတ်လုပ်ပါတယ်! စစ်ဆေးကြည့်ပါ:

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

## တာဝန်ယူကတိပြု AI

Microsoft သည် ကျွန်ုပ်တို့၏ AI ထုတ်ကုန်များကို တာဝန်ယူဝန်ထမ်းစွာအသုံးပြုရန်၊ သင်ယူချက်များကို မျှဝေရန်နှင့် Transparency Notes နှင့် Impact Assessments ကဲ့သို့သော ကိရိယာများအားဖြင့် ယုံကြည်မှုပေါ်တည်သော မိတ်ဖက်များ တည်ဆောက်ရန် ကတိပြုသည်။ ဤရင်းမြစ်များစွာကို [https://aka.ms/RAI](https://aka.ms/RAI) တွင် ရရှိနိုင်ပါသည်။  
Microsoft ၏ တာဝန်ယူ AI ကို အတည်ပြုမှု၊ယုံကြည်မှုနှင့် လုံခြုံမှု၊ ကိုယ်ရေးကိုယ်တာလုံခြုံမှုနှင့် လုံခြုံရေး၊ ပါဝင်မှု၊ ပေါ်လွင်မှုနှင့် တာဝန်ယူမှုတို့ အခြေခံ၍ မြေတပြင်လုံးရှိအခြေအနေများတွင်အကောင်အထည်ဖော်သည်။

ဒီဥပမာတွင်အသုံးပြုထားသည့် ကြီးမားသော သဘာဝဘာသာစကား၊ ပုံနှင့် အသံ မော်ဒယ်များသည် မတရား၊ ယုံကြည်မရသော သို့မဟုတ် မကြင်နာမှုရှိသော အပြုအမူများ ပြုလုပ်နိုင်ပြီး ထိုကြောင့် အနစ်နာခံမှုများဖြစ်စေနိုင်သည်။ အန္တရာယ်များနှင့် ကန့်သတ်ချက်များအကြောင်း သိရှိရန် [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ကို ပြန်လည်ကြည့်ရှုပါ။

ဤအန္တရာယ်များကို လျှော့ချရန် အကြံပြု ဆောင်ရွက်ချက်မှာ သင့် ဖွဲ့စည်းပုံတွင် အန္တရာယ်အပြုအမူများကို ရှာဖွေတာခြင်းနှင့် တားဆီးနိုင်သော လုံခြုံရေးစနစ် တစ်ခု ထည့်သွင်းခြင်းဖြစ်သည်။ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) သည် လွတ်လပ်သော ကာကွယ်မှု အဆင့်တစ်ခုဖြစ်ပြီး အသုံးပြုသူဖန်တီးသည့် အကြောင်းအရာများနှင့် AI ဖန်တီးထားသည့် အကြောင်းအရာများကို ကာကွယ်နိုင်သည်။ Azure AI Content Safety တွင် အကြောင်းအရာ အန္တရာယ် လက္ခဏာများကို ဖော်ထုတ်နိုင်စေရန် စာသားနှင့် ပုံ API များ ပါဝင်သည်။ Azure AI Foundry တွင် Content Safety ၀န်ဆောင်မှုသည် အမျိုးမျိုးသော မျိုးစုံများအတွက် အန္တရာယ်ရှိသော အကြောင်းအရာများကို ကြည့်ရှု၊ စူးစမ်းရန်နှင့် နမူနာကုဒ်များကို စမ်းသပ်ရန်ခွင့်ပြုသည်။ အောက်ပါ [quickstart စာရွက်စာတမ်း](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) သည် ၀န်ဆောင်မှုထံမှာ တောင်းဆိုမှုများ ပြုလုပ်ရန် လမ်းညွန်သည်။
အသေးစိတ်စဉ်းစားရမည့်အချက်တစ်ခုမှာ လုံးလုံးကြီးသော အက်ပ်လီကေးရှင်းကောင်းမွန်မှု ဖြစ်သည်။ မိုက်တယ်မိုးဒယ်နှင့် မိုက်တယ်မော်ဒယ်များပါဝင်သည့် အက်ပ်လီကေးရှင်းများတွင်၊ စနစ်သည် သင်နှင့် သင့်အသုံးပြုသူများ မျှော်လင့်သလို စွမ်းဆောင်ရည် ပြသရမည်ဟု သဘောထားပါသည်၊ ထိုသည်အပြင် အနုတ်ဆုတ် သို့မဟုတ် ဟန့်တားမှုဖြစ်စေသော ထုတ်လွှင့်ချက်များ မထုတ်ပေးရပါ။ သင့်အက်ပ်လီကေးရှင်း စုစုပေါင်း စွမ်းဆောင်ရည်ကို [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ဖြင့် အရေးကြီးစွာ သုံးသပ်သင့်သည်။ သင်သည် ပြုလုပ်ထားသည့် [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ဖြင့် ဖန်တီးခြင်းနှင့် သုံးသပ်ခြင်းတို့လည်း ပြုလုပ်နိုင်ပါသည်။

[Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ကို အသုံးပြု၍ သင်၏ AI အက်ပ်လီကေးရှင်းကို ဖန်တီးပုံပတ်ဝန်းကျင်တွင် သုံးသပ်နိုင်သည်။ စမ်းသပ်ဒေတာစုံတစ်ခု သို့မဟုတ် ရည်မှန်းချက်တစ်ခုကို ပေးသည့်အခါ၊ သင့်ဖန်တီးထားသော AI အသစ်များကို အလိုအလျောက် တာဝန်ပေးထားသော evaluator များ သို့မဟုတ် သင့်ရွေးချယ်သည့် custom evaluator များဖြင့် အရေအတွက်ပိုင်းကောက်ချက်ထုတ်နိုင်ပါသည်။ စနစ်ကို သုံးသပ်ရန် azure ai evaluation sdk ကို စတင်အသုံးပြုလိုပါက [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ကို ကြည့်ရူနိုင်သည်။ သုံးသပ်မှု လုပ်ငန်းစဉ်များ ပြီးဆုံးသည်နှင့် သင်အကောင်အထည်ဖော်ထားသော [Azure AI Foundry တွင် ရလဒ်များကို ကြည့်ရှုနိုင်ပါသည်](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)။

## အမှတ်တံဆိပ်များ

ဤပရောဂျက်တွင် ပရောဂျက်များ၊ ထုတ်ကုန်များ သို့မဟုတ် ဝန်ဆောင်မှုများအတွက် အမှတ်တံဆိပ်များ သို့မဟုတ် ရုပ်ပုံများ ပါဝင်နိုင်ပါသည်။ Microsoft ၏ အမှတ်တံဆိပ်များ သို့မဟုတ် ရုပ်ပုံများ အသုံးချခြင်းသည် [Microsoft ၏ Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) အတိုင်း ဖွင့်လိုက်ရပါမည်။ Microsoft အမှတ်တံဆိပ်များ သို့မဟုတ် ရုပ်ပုံများကို ဤပရောဂျက်၏ ပြင်ဆင်ထားသော ဗားရှင်းများတွင် အသုံးပြုသောအခါ သဘောတရားမှားယွင်းခြင်း သို့မဟုတ် Microsoft ၏ အားပေးမှု တိုက်ရိုက် သက်သေပြခြင်း မဖြစ်စေရန် သေချာရမည် ဖြစ်သည်။ တတိယပါတီ အမှတ်တံဆိပ်များ သို့မဟုတ် ရုပ်ပုံများ အသုံးပြုခြင်းသည် ထိုတတိယပါတီ၏ နည်းနည်းလမ်းစနစ်များအတိုင်း ဖြစ်ရမည် ဖြစ်သည်။

## အကူအညီရယူခြင်း

AI အက်ပ်များ တည်ဆောက်ရာ၌ ပြဿနာဖြစ်ပါက သို့မဟုတ် မေးခွန်းများရှိပါက အောက်ပါနေရာများသို့ ဝင်ရောက်ပါ-

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

ထုတ်ကုန်တုံ့ပြန်ချက် သို့မဟုတ် အမှားမှုများကို တွေ့ရှိပါက-

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ဆိုရှေပေးချက်**  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါတယ်။ ကျွန်ုပ်တို့မှာ တိကျမှုအတွက် ကြိုးစားပေမယ့် အလိုအလျောက် ဘာသာပြန်ထားမှုများတွင် အမှားများ သို့မဟုတ် တိကျမှုမပြည့်စုံမှုများ ရှိနိုင်ကြောင်း သတိပြုပါရစေ။ မူလစာရွက်စာတမ်းကို မူလဘာသာဖြင့် အကောင်းဆုံးမှတ်ယူသင့်သည်။ အရေးကြီးသည့် အချက်အလက်များအတွက် လူကြီးမင်းတို့ စိတ်ချရသော လူ့ဘာသာပြန် ဝန်ဆောင်မှုကို အသုံးပြုရန်အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာသော မမှန်ကန်မှုများ သို့မဟုတ် အဓိပ္ပာယ်လွဲမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->