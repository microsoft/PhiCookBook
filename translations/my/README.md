<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2e4b490f4bd424b095f21e38c6af33b",
  "translation_date": "2026-01-05T15:45:02+00:00",
  "source_file": "README.md",
  "language_code": "my"
}
-->
# Phi Cookbook: Microsoft's Phi မော်ဒယ်များဖြင့် လက်တွေ့ဥပမာများ

[![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi သည် Microsoft က ဖန်တီးထားသည့် အခမဲ့ AI မော်ဒယ်များ စီးရီးဖြစ်သည်။

Phi သည် လက်ရှိအချိန်မှာ အလွန်ထိရောက်ပြီး စျေးနှုန်းသက်သာဆုံးသော သင်္ကေတအသေးစား ဘာသာစကားမော်ဒယ် (SLM) ဖြစ်ပြီး ဘာသာစကားစုံ၊ စဉ်းစားနားလည်မှု၊ စာသား/စကားပြောထုတ်လုပ်မှု၊ ကုဒ်ရေးခြင်း၊ ပုံများ၊ အသံနှင့် အခြား ရလဒ်စုံအတွက် benchmarks ကောင်းများရှိသည်။

Phi ကို cloud သို့မဟုတ် အနားစွန်းကိရိယာများပေါ်သို့ ဖြန့်ချိနိုင်ပြီး ကွန်ပျူတာစွမ်းအားကန့်သတ်ချက်ရှိသော generative AI လျှောက်လွှာများကို လွယ်ကူစွာ တည်ဆောက်နိုင်သည်။

ဒီအရင်းအမြစ်များကို အသုံးပြုဖို့ စတင်လိုက်ပါ။
1. **သိုလှောင်မှုကို Fork လုပ်ပါ**: Click [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **သိုလှောင်မှုကို Clone လုပ်ပါ**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord Community တို့ကို ဝင်ရောက်ပြီး ကျွမ်းကျင်သူများနှင့် မိတ်ဆွေဖွဲ့ပါ**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.eb18d1b9605d754b.my.png)

### 🌐 ဘာသာစကားစုံကို ထောက်ပံ့ခြင်း

#### GitHub Action ဖြင့် ထောက်ပံ့ထားခြင်း (အလိုအလျောက် & အမြဲတမ်းနောက်ဆုံးပေါ်)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[အာရပ်](../ar/README.md) | [ဘင်္ဂါလီ](../bn/README.md) | [ဘူလ်ဂေးရီးယား](../bg/README.md) | [မြန်မာ (မြန်မာ)](./README.md) | [တရုတ် (ရိုးရိုး)](../zh/README.md) | [တရုတ် (ရိုးရိုး၊ ဟောင်ကောင်)](../hk/README.md) | [တရုတ် (ရိုးရိုး၊ မကာအို)](../mo/README.md) | [တရုတ် (ရိုးရိုး၊ ထိုင်ဝမ်)](../tw/README.md) | [ခရိုအေးရှား](../hr/README.md) | [ချက်](../cs/README.md) | [ဒိန်းမတ်](../da/README.md) | [ဒတ်ချ်](../nl/README.md) | [အက်စတိုးနီးယား](../et/README.md) | [ဖင်နစ်](../fi/README.md) | [ပြင်သစ်](../fr/README.md) | [ဂျာမန်](../de/README.md) | [ဂရိ](../el/README.md) | [ဟီဘရူး](../he/README.md) | [ဟိန္ဒီ](../hi/README.md) | [ဟန်ဂေရီ](../hu/README.md) | [အင်ဒိုနီးရှား](../id/README.md) | [အီတလီ](../it/README.md) | [ဂျပန်](../ja/README.md) | [ကန်နာဒါ](../kn/README.md) | [ကိုရီးယား](../ko/README.md) | [လီသူနီးယား](../lt/README.md) | [မလေး](../ms/README.md) | [မလာရမ်](../ml/README.md) | [မာရသီ](../mr/README.md) | [နေပါလီ](../ne/README.md) | [ไนဂျီရီးယား Pidgin](../pcm/README.md) | [နော်ရဝေ](../no/README.md) | [ပါရှန် (ဖာစီ)](../fa/README.md) | [ပိုလန်](../pl/README.md) | [ပေါ်တူဂီ (ဘရာဇီးလ်)](../br/README.md) | [ပေါ်တူဂီ (ပိုက်တူဂီ)](../pt/README.md) | [ပန်ဂျာဘီ (ဂူမူခီ)](../pa/README.md) | [ရိုမေးနီးယား](../ro/README.md) | [ရုရှား](../ru/README.md) | [ဆားဘီးယား (ဆိုရီလစ်လစ်)](../sr/README.md) | [စလိုဗက်](../sk/README.md) | [စလိုဗေးနီးယား](../sl/README.md) | [စပိန်](../es/README.md) | [စွာဟီလီ](../sw/README.md) | [ဆွီဒင်](../sv/README.md) | [တာဂလို (ဖိလစ်ပိုင်)](../tl/README.md) | [သမီး](../ta/README.md) | [တယ်လူးဂူ](../te/README.md) | [ထိုင်း](../th/README.md) | [တူရကီ](../tr/README.md) | [ယူကရိန်း](../uk/README.md) | [ဥရုဒူး](../ur/README.md) | [ဗီယက်နမ်](../vi/README.md)

> **ဒေသတွင် Clone လုပ်လိုပါသလား?**

> ဒီသိုလှောင်မှုမှာ ဘာသာစကား ၅၀ ထက်မပိုသော ဘာသာပြန်ချက်များပါဝင်ပြီး ဒါကြောင့် ဒေါင်းလုပ်အရွယ်အစားကို အကြီးစားတိုးစေသည်။ ဘာသာပြန်ချက်များမပါဘဲ Clone လုပ်ရန် sparse checkout ကို အသုံးပြုပါ:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> ဒါက သင်ဟာသင်တန်းကို အပြီးသတ်ဖို့ လိုအပ်တဲ့ အရာအားလုံးကို နည်းလမ်းများဖြင့် အရမ်းလျင်မြန်စွာ ဒေါင်းလုပ်ဆွဲနိုင်ပါတယ်။
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## အကြောင်းအရာဇယား

- နိဒါန်း
  - [Phi မိသားစုသို့ ကြိုဆိုပါသည်](./md/01.Introduction/01/01.PhiFamily.md)
  - [သင့်ပတ်ဝန်းကျင်ကို စနစ်တကျပြင်ဆင်ခြင်း](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [အဓိကနည်းပညာများကိုနားလည်ခြင်း](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi မော်ဒယ်များအတွက် AI လုံခြုံရေး](./md/01.Introduction/01/01.AISafety.md)
  - [Phi hardware ထောက်ပံ့မှု](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi မော်ဒယ်များနှင့် platform များပေါ်တွင် ရရှိနိုင်မှု](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai နှင့် Phi အသုံးပြုခြင်း](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace မော်ဒယ်များ](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- အသီးသီးသော ပတ်ဝန်းကျင်များတွင် Phi ကို inference လုပ်ခြင်း
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub Models](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi မိသားစုကို Inference လုပ်ခြင်း
    - [iOS တွင် Phi ကို inference လုပ်ခြင်း](./md/01.Introduction/03/iOS_Inference.md)
    - [Android တွင် Phi ကို inference လုပ်ခြင်း](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson တွင် Phi ကို inference လုပ်ခြင်း](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC တွင် Phi ကို inference လုပ်ခြင်း](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework နှင့် Phi ကို inference လုပ်ခြင်း](./md/01.Introduction/03/MLX_Inference.md)
    - [Local Server တွင် Phi ကို inference လုပ်ခြင်း](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Remote Server တွင် AI Toolkit အသုံးပြု၍ Phi ကို inference လုပ်ခြင်း](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust ဖြင့် Phi ကို inference လုပ်ခြင်း](./md/01.Introduction/03/Rust_Inference.md)
    - [Local သည် Phi--Vision ကို inference လုပ်ခြင်း](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (တရားဝင်ထောက်ပံ့မှု) နှင့် Phi ကို inference လုပ်ခြင်း](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi မိသားစုကို Quantifying လုပ်ခြင်း](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp အသုံးပြု၍ Phi-3.5 / 4 ကို Quantizing လုပ်ခြင်း](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime အတွက် Generative AI extension များ အသုံးပြု၍ Phi-3.5 / 4 ကို Quantizing လုပ်ခြင်း](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ကို အသုံးပြု၍ Phi-3.5 / 4 ကို Quantizing လုပ်ခြင်း](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework ကို အသုံးပြု၍ Phi-3.5 / 4 ကို Quantizing လုပ်ခြင်း](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi ကို သုံးသပ်ခြင်း
    - [တုန့်ပြန်မှု AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry တွင် သုံးသပ်ခြင်း](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow ဖြင့် သုံးသပ်ခြင်း](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search နှင့် RAG
    - [Phi-4-mini နှင့် Phi-4-multimodal (RAG) ကို Azure AI Search နှင့် အသုံးပြုနည်း](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi လျှောက်လွှာဖွံ့ဖြိုးတိုးတက်မှုနမူနာများ
  - စာသားနှင့် စကားပြောစနစ်များ
    - Phi-4 နမူနာများ 🆕
      - [📓] [Phi-4-mini ONNX မော်ဒယ်ဖြင့် စကားပြောခြင်း](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 local ONNX မော်ဒယ်ဖြင့် Chat .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Semantic Kernel ကို အသုံးပြု၍ Phi-4 ONNX ဖြင့် Chat .NET Console App](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 နမူနာများ
      - [Phi3, ONNX Runtime Web နှင့် WebGPU အသုံးပြုပြီး Browser တွင် ဒေသခံ Chatbot](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - အပြန်အလှန် Phi-3-mini နှင့် OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - wrapper တည်ဆောက်ခြင်းနှင့် Phi-3 ကို MLFlow နှင့် အသုံးပြုခြင်း](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Model Optimization - ONNX Runtime Web အတွက် Phi-3-min မော်ဒယ်ကို Olive ဖြင့် မည်သို့ optimized ပြုလုပ်မည်နည်း](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx ဖြင့် WinUI3 App](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 Multi Model AI Powered Notes App နမူနာ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Prompt flow ဖြင့် စိတ်တိုင်းကျ Phi-3 မော်ဒယ်များကို Fine-tune ပြုလုပ်ခြင်းနှင့် ပေါင်းစပ်ခြင်း](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry တွင် Prompt flow ဖြင့် စိတ်တိုင်းကျ Phi-3 မော်ဒယ်များကို Fine-tune ပြုလုပ်ခြင်းနှင့် ပေါင်းစပ်ခြင်း](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft ၏ တာဝန်ရှိသော AI အခြေခံအယူများအား အာရုံစိုက်၍ Azure AI Foundry တွင် Fine-tuned Phi-3 / Phi-3.5 မော်ဒယ်ကို သုံးသပ်ခြင်း](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct ဘာသာပြန်နမူနာ (တရုတ်/အင်္ဂလိပ်)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU ကို အသုံးပြု၍ Phi-3.5-Instruct ONNX ဖြင့် Prompt flow ဖြေရှင်းချက် ဖန်တီးခြင်း](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite ကို အသုံးပြု၍ Android app ဖန်တီးခြင်း](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime ဖြင့် ဒေသတွင်း ONNX Phi-3 မော်ဒယ်ကို အသုံးပြုသော Q&A .NET နမူနာ](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel နှင့် Phi-3 ဖြင့် Console chat .NET app](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK ကုဒ်အခြေခံ နမူနာများ 
    - Phi-4 နမူနာများ 🆕
      - [📓] [Phi-4-multimodal ဖြင့် စာရင်းစီမံကိန်းကုဒ် ဖန်တီးခြင်း](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 နမူနာများ
      - [Microsoft Phi-3 ကွတ်သားတန်းအုပ်စုနှင့် Visual Studio Code GitHub Copilot Chat ကို ကိုယ်ပိုင်ဆောက်ခြင်း](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub မော်ဒယ်များဖြင့် ကိုယ်ပိုင် Visual Studio Code Chat Copilot Agent ဖန်တီးခြင်း Phi-3.5ဖြင့်](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - အဆင့်မြင့် သဘောထားနမူနာများ
    - Phi-4 နမူနာများ 🆕
      - [📓] [Phi-4-mini-reasoning သို့မဟုတ် Phi-4-reasoning နမူနာများ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive ဖြင့် Phi-4-mini-reasoning ကို Fine-tuning ပြုလုပ်ခြင်း](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX ဖြင့် Phi-4-mini-reasoning ကို Fine-tuning ပြုလုပ်ခြင်း](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub မော်ဒယ်များနှင့် Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry မော်ဒယ်များနှင့် Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - ဒေမိုများ
      - [Phi-4-mini demos များ Hugging Face Spaces တွင် ဖျော်ဖြေထားသည်](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demos များ Hugginge Face Spaces တွင် ဖျော်ဖြေထားသည်](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - အမြင် နမူနာများ
    - Phi-4 နမူနာများ 🆕
      - [📓] [Phi-4-multimodal ကို အသုံးပြု၍ ပုံများ ဖတ်ပြီး ကုဒ် ဖန်တီးခြင်း](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 နမူနာများ
      -  [📓][Phi-3-vision- ပုံအကြောင်းအရာ စာလုံးမှ စာလုံးသို့](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP စုပေါင်း](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 ပြန်လည်ထုတ်လုပ်ခြင်း](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - မြင်ကွင်းဘာသာစကား အကူအညီပေးသူ - Phi3-Vision နှင့် OpenVINO ဖြင့်](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision multi-frame သို့မဟုတ် multi-image နမူနာ](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET ကို အသုံးပြု၍ Phi-3 Vision ဒေသခံ ONNX မော်ဒယ်](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [မီနူးအခြေခံ Phi-3 Vision ဒေသခံ ONNX မော်ဒယ် Microsoft.ML.OnnxRuntime .NET ဖြင့်](../../md/04.HOL/dotnet/src/LabsPhi304)

  - သင်္ချာ နမူနာများ
    -  Phi-4-Mini-Flash-Reasoning-Instruct နမူနာများ 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct ဖြင့် သင်္ချာ ဒေမို](./md/02.Application/09.Math/MathDemo.ipynb)

  - အသံ နမူနာများ
    - Phi-4 နမူနာများ 🆕
      - [📓] [Phi-4-multimodal ဖြင့် အသံစာသားများထုတ်ယူခြင်း](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal အသံနမူနာ](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal စကားပြန်ဟောပြော ပြောင်းဆိုခြင်း နမူနာ](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET console application အသုံးပြု၍ Phi-4-multimodal အသံဖိုင် စိစစ် ထုတ်ယူပြီး စာသားထုတ်လုပ်ခြင်း](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE နမူနာများ
    - Phi-3 / 3.5 နမူနာများ
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) လူမှုမီဒီယာ နမူနာ](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search နှင့် LlamaIndex တို့ဖြင့် Retrieval-Augmented Generation (RAG) Pipeline တည်ဆောက်ခြင်း](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Function Calling နမူနာများ
    - Phi-4 နမူနာများ 🆕
      -  [📓] [Phi-4-mini နှင့် Function Calling အသုံးပြုခြင်း](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Function Calling ဖြင့် Phi-4-mini အသုံးပြု multi-agents ဖန်တီးခြင်း](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama နှင့် Function Calling အသုံးပြုခြင်း](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX နှင့် Function Calling အသုံးပြုခြင်း](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Multimodal Mixing နမူနာများ
    - Phi-4 နမူနာများ 🆕
      -  [📓] [နည်းပညာ သတင်းထောက်အဖြစ် Phi-4-multimodal အသုံးပြုခြင်း](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET console application Phi-4-multimodal အသုံးပြု၍ ပုံများ စိစစ်ခြင်း](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi မော်ဒယ်များ Fine-tuning
  - [Fine-tuning များအကြောင်း](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Fine-tuning နှင့် RAG အပြိုင်အဆိုင်](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 ကို စက်မှု လုပ်ငန်း တက်ကြွကျွမ်းကျင်သူအဖြစ် Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code အတွက် AI Toolkit ဖြင့် Phi-3 ကို Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service ဖြင့် Phi-3 ကို Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora ဖြင့် Phi-3 ကို Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora ဖြင့် Phi-3 ကို Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry ဖြင့် Phi-3 ကို Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK ဖြင့် Phi-3 ကို Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive ဖြင့် Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Lab ဖြင့် Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias ဖြင့် Phi-3-vision ကို Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework ဖြင့် Phi-3 ကို Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision (တရားဝင် အထောက်အပံ့) ကို Fine-tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS၊ Azure Containers (တရားဝင် အထောက်အပံ့) ဖြင့် Phi-3 ကို Fine-Tuning ပြုလုပ်ခြင်း](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 နှင့် 3.5 Vision ကို Fine-Tuning ပြုလုပ်ခြင်း](https://github.com/2U1/Phi3-Vision-Finetune)

- လက်တွေ့ လေ့လာခန်း
  - [နောက်ဆုံးပေါ် မော်ဒယ်များ စမ်းသပ်ခြင်း: LLMs, SLMs, ဒေသတွင်း ဖွံ့ဖြိုးတိုးတက်မှု နှင့် အခြားများ](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP စွမ်းရည် ဖော်ဆောင်ခြင်း: Microsoft Olive ဖြင့် Fine-Tuning](https://github.com/azure/Ignite_FineTuning_workshop)

- တက္ကသိုလ် သုတေသနစာတမ်းများနှင့် စာစဉ်များ
  - [စာအုပ်များသာလိုအပ်သည် II: phi-1.5 နည်းပညာအစီရင်ခံစာ](https://arxiv.org/abs/2309.05463)
  - [Phi-3 နည်းပညာအစီရင်ခံစာ: မိုဘိုင်းဖုန်းတွင် ဒေသဆိုင်ရာ အလွန်စွမ်းဆောင်ရည်မြင့် ဘာသာစကားမော်ဒယ်](https://arxiv.org/abs/2404.14219)
  - [Phi-4 နည်းပညာအစီရင်ခံစာ](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini နည်းပညာအစီရင်ခံစာ: Mixture-of-LoRAs ဖြင့် တိုတောင်းသော်လည်း ခိုင်မာသော มူလ်တီမိုဒယ် ဘာသာစကားမော်ဒယ်များ](https://arxiv.org/abs/2503.01743)
  - [ယာဉ်အတွင်း လုပ်ဆောင်ချက်ခေါ်ယူမှုအတွက် စမောလ်ဘာသာစကားမော်ဒယ်များ တိုးတက်အောင်လုပ်ခြင်း](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) ပြိုင်ပွဲမေးခွန်း ဖြေဆိုခြင်းအတွက် PHI-3 ကို တိကျစွာ ပြင်ဆင်ခြင်း: နည်းဗျူဟာ၊ ရလဒ်များနှင့် စိန်ခေါ်မှုများ](https://arxiv.org/abs/2501.01588)
  - [Phi-4-အတွေးမြှင့် နည်းပညာအစီရင်ခံစာ](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-အတွေးမြှင့် နည်းပညာအစီရင်ခံစာ](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi မော်ဒယ်များ အသုံးပြုခြင်း

### Azure AI Foundry တွင် Phi 

Microsoft Phi ကို မည်သို့အသုံးပြုရမည်နှင့် သင့်နည်းပညာပစ္စည်းများ၌ End-to-End လုပ်ဆောင်ချက်များကို မည်သို့တည်ဆောက်ရမည်ကို သင်ယူနိုင်သည်။ Phi ကိုကိုယ်တိုင်ခံစားလိုပါက မော်ဒယ်များဖြင့် ကစား၍ သင့်ရဲ့ အခြေအနေများအတွက် Phi ကို လိုက်ဖက်အောင် ပြင်ဆင်နိုင်သည့် [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ကို အသုံးပြုပါ၊ [Azure AI Foundry စတင်အသုံးပြုခြင်း](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) တွင် ပိုမိုသိရှိနိုင်သည်။

**ကစားကြည့်ရန်နေရာ**  
မော်ဒယ်တိုင်းအတွက် စမ်းသပ်ရန် သီးခြားနေရာရှိသည် [Azure AI Playground](https://aka.ms/try-phi3)။

### GitHub မော်ဒယ်များတွင် Phi 

Microsoft Phi ကို မည်သို့အသုံးပြုရမည်နှင့် သင့်နည်းပညာပစ္စည်းများ၌ End-to-End လုပ်ဆောင်ချက်များကို မည်သို့တည်ဆောက်ရမည်ကို သင်ယူနိုင်သည်။ Phi ကိုကိုယ်တိုင်ခံစားလိုပါက မော်ဒယ်ဖြင့် ကစား၍ သင့်အခြေအနေများအတွက် Phi ကို ပြင်ဆင်နိုင်သည့် [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ကို အသုံးပြုပါ၊ [GitHub Model Catalog စတင်အသုံးပြုခြင်း](/md/02.QuickStart/GitHubModel_QuickStart.md) တွင် ပိုမိုသိရှိနိုင်သည်။

**ကစားကြည့်ရန်နေရာ**  
မော်ဒယ်တိုင်းတွင် စမ်းသပ်ရန် သီးခြား [ကစားရန်နေရာ](/md/02.QuickStart/GitHubModel_QuickStart.md) ရှိသည်။

### Hugging Face တွင် Phi 

မော်ဒယ်ကို [Hugging Face](https://huggingface.co/microsoft) တွင်လည်း ရနိုင်သည်။

**ကစားကြည့်ရန်နေရာ**  
[Hugging Chat ကစားရန်နေရာ](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 အခြား သင်တန်းများ

ကျွန်ုပ်တို့အသင်းအဖွဲ့သည် အခြားသင်တန်းများထုတ်လုပ်ထားပါသည်။ စစ်ဆေးကြည့်ပါ။

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain  
[![စတင်လေ့လာသူများအတွက် LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)  
[![စတင်လေ့လာသူများအတွက် LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents  
[![စတင်လေ့လာသူများအတွက် AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![စတင်လေ့လာသူများအတွက် Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![စတင်လေ့လာသူများအတွက် MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![စတင်လေ့လာသူများအတွက် AI Agents](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI ကန့်သတ်မှုလမ်းကြောင်း  
[![စတင်လေ့လာသူများအတွက် Generative AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Core Learning  
[![စတင်လေ့လာသူများအတွက် ML](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
[![စတင်လေ့လာသူများအတွက် ဒေတာသိပ္ပံ](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
[![စတင်လေ့လာသူများအတွက် AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
[![စတင်လေ့လာသူများအတွက် စိုင်ဘာလုံခြုံရေး](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)  
[![စတင်လေ့လာသူများအတွက် ဝက်ဘ်ဖွံ့ဖြိုးတိုးတက်ရေး](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
[![စတင်လေ့လာသူများအတွက် IoT](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
[![စတင်လေ့လာသူများအတွက် XR ဖြံ့ဖြိုးတိုးတက်ရေး](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot စီးရီး  
[![AI စနစ်နှင့်ဖက်စားသံတော်ဆောင်ရေးအတွက် Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
[![C#/.NET အတွက် Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
[![Copilot စွန့်စားခန်း](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## တာဝန်ရှိသော AI

Microsoft သည် AI ထုတ်ကုန်များကို တာဝန်ရှိစွာ အသုံးပြုနိုင်ရန် အောက်အစီအစဉ်များကို ဖန်တီးပေးရန်၊ သင်ယူမှုများကို ဝေမျှရန်၊ Transparency Notes နှင့် Impact Assessments ကဲ့သို့သော ကိရိယာများမှတဆင့် ယုံကြည်မှုအခြေပြု လက်တွဲဆက်ဆံမှုများ တည်ဆောက်ပေးရန် ကြိုးပမ်းလျက်ရှိပါသည်။ ဤအရင်းအမြစ်များစွာကို [https://aka.ms/RAI](https://aka.ms/RAI) တွင် ရရှိနိုင်ပါသည်။  
Microsoft ၏ တာဝန်ရှိသော AI ဆောင်ရွက်ချက်မှာ တရားမျှတမှု၊ ယုံကြည်ရမှုနှင့် လုံခြုံမှု၊ ကိုယ်ရေးကာကွယ်မှုနှင့် လုံခြုံရေး၊ အပါအဝင်မှု၊ ရိုးရှင်းပြတ်သားမှုနှင့် တာဝန်ယူမှုတို့အပေါ် အခြေခံထားသည်။

ဤနမူနာတွင် အသုံးပြုထားသော ကြီးမားသော ဘာသာစကား၊ ဓာတ်ပုံနှင့် အသံမော်ဒယ်များသည် မတရား၊ ယုံကြည်ရမည်မဟုတ်သော သို့မဟုတ် မေတ္တာမရှိသော စတိုင်ဖြင့် ပြုမူနိုင်ပြီး ထိခိုက်မှုများ ဖြစ်နိုင်သည်။ ထောက်လှမ်းဖို့ အရေးကြီးသောအချက်များနှင့် ကန့်သတ်ချက်များ အကြောင်း သိရှိရန် [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ကို ကြည့်ရှုပါ။

ဤအန္တရာယ်များကို လျှော့ချရန် အကြံပြုချက်မှာ သင်၏ နည်းပညာဆောက်လုပ်မှုတွင် ထိခိုက်မှုရှိစေနိုင်သည့် ဆိုးကျိုးရှိသော ဆက်ဆံမှုများကို ဖော်ထုတ်၍ ကာကွယ်နိုင်သော လုံခြုံရေး စနစ်တစ်ခု ထည့်သွင်းရန် ဖြစ်ပါသည်။ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) သည် လွတ်လပ်စွာ ကာကွယ်ရေးအလွှာတစ်ခု ဖြစ်ပြီး အသုံးပြုသူထုတ်ဖန်သော၊ AI ထုတ်ဖန်သော မလိုလားအပ်သော အကြောင်းအရာများကို လျင်မြန်စွာ ဖော်ထုတ်နိုင်သည်။ Azure AI Content Safety တွင် စာသားနှင့် ဓာတ်ပုံ API များ ပါရှိပြီး ထိခိုက်မှုရှိနိုင်သော အကြောင်းအရာများကို စစ်ဆေးနိုင်သည်။ Azure AI Foundry အတွင်း Content Safety ဝန်ဆောင်မှုသည် မတူညီသော မော်ဒယ်လ်များတွင်ထိခိုက်မှုရှိသော အကြောင်းအရာများကို တွေ့မြင်ရန်၊ ရှာဖွေရန်နှင့် နမူနာကုဒ်များ စမ်းသပ်ရန် ခွင့်ပြုသည်။ အောက်ပါ [quickstart စာတမ်း](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) သည် ဝန်ဆောင်မှုအား တောင်းဆိုမည့်အထိမ်းအမှတ် အဆင့်များကို လမ်းညွှန်ပေးပါသည်။

အခြားတစ်ချက်မှာ ဝန်ဆောင်မှုလုံးဝ၏ လုပ်ဆောင်မှုစွမ်းအင်ကို တွက်ချက်ရမည်ဖြစ်သည်။ မူလတန်းစနစ်များနှင့် မော်ဒယ် များစွာပါဝင်သည့် လျှောက်လွှာများတွင် ယေဘုယျလျှောက်လွှာသည် သင့်နှင့် သုံးစွဲသူများ၏ မျှော်မှန်းချက်များကို ပြည့်မီစေရမည်ဖြစ်ပြီး ထိခိုက်စေသော ရလဒ်များ မထုတ်ပေးရပါ။ သင်၏ လျှောက်လွှာ စုစုပေါင်း၏ လုပ်ဆောင်မှုစွမ်းအားကို [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ဖြင့် သပ်ရပ်စွာ ချွေတာသင့်သည်။ ထိုအပြင် သင့်ကိုယ်ပိုင် စစ်ဆေးသူများဖြင့် [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ဖန်တီး၍ စစ်ဆေးနိုင်ရန် လည်း နှုတ်ခွန်းဆက်ပေးပါသည်။
သင်၏ AI application ကို သင်၏ဖွံ့ဖြိုးမှုပတ်ဝန်းကျင်တွင် [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ကို အသုံးပြုပြီး အကဲဖြတ်နိုင်သည်။ စမ်းသပ်ရန် ဒေတာစနစ် သို့မဟုတ် ရည်မှန်းထားသည့် အချက်အလက် တစ်ခုကို ပေးပြီး သင်၏ generative AI application ၏ ထုတ်ဖြစ်မှုများကို built-in evaluators သို့မဟုတ် သင်လိုအပ်သလို custom evaluators ဖြင့် ပမာဏနှိပ်သတ်နိုင်သည်။ သင့်စနစ်ကို အကဲဖြတ်ရန် azure ai evaluation sdk ဖြင့် စတင်လိုပါက [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ကို လိုက်နာနိုင်ပါသည်။ အကဲဖြတ်မှု run ကို အသုံးပြုပြီးနောက်တွင် [Azure AI Foundry တွင် ရလဒ်များကို ဧည့်ကြည့်နိုင်ပါသည်](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)။

## အမှတ်တံဆိပ်များ

ဤ project တွင် စီမံကိန်းများ၊ ထုတ်ကုန်များ သို့မဟုတ် ၀န်ဆောင်မှုများအတွက် အမှတ်တံဆိပ်များ သို့မဟုတ် လိုဂိုများ ပါဝင်နိုင်ပါသည်။ Microsoft ၏ အမှတ်တံဆိပ် သို့မဟုတ် လိုဂိုအသုံးပြုမှုသည် [Microsoft ၏ Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) အတိုင်း လိုက်နာရမည်ဖြစ်ပြီး ခွင့်ပြုချက်ရှိမှုအပေါ် မူတည်ပါသည်။ ဤ project ၏ ပြင်ဆင်ထားသော ဗားရှင်းများတွင် Microsoft အမှတ်တံဆိပ် သို့မဟုတ် လိုဂိုများကို အသုံးမပြုသင့်ပါ၊ Microsoft ၏ ပံ့ပိုးမှုရှိသည်ဟု လွဲမှားသဘောထား ဖြစ်စေသင့်မည်မဟုတ်ပါ။ တတိယပါတီ၏ အမှတ်တံဆိပ် သို့မဟုတ် လိုဂိုများကို အသုံးပြုခြင်းသည် အဆိုပါ တတိယပါတီ၏ မူဝါဒများအား အညီ ဖြစ်ပါသည်။

## ကူညီမှု ရယူရန်

AI apps ဖန်တီးရာတွင် ပြဿနာတက်ပါက သို့မဟုတ် မေးခွန်းများရှိပါက အောက်ပါနေရာသို့ လက်ခံပါ။

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

ထုတ်ကုန်ဆိုင်ရာတုံ့ပြန်ချက် သို့မဟုတ် အမှားများရှိပါက အောက်ပါနေရာသို့ သွားရောက်ပါ။

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**တာဝန်မရှိခြင်းကြေညာချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်စနစ်ဖြစ်သော [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးပမ်းသောကြောင့်ပါ၊ သို့သော် အလိုအလျောက်ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် တိကျမှုလျော့နည်းမှုများ ရှိနိုင်ကြောင်း သတိပြုခံစားပါ။ မူလစာတမ်းကို မိခင်ဘာသာဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆရန် အကြံပြုပါသည်။ အရေးကြီးသောအချက်အလက်များအတွက် လူ့အလုပ်သမားဘာသာပြန် များဖြင့် ဘာသာပြန်ရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်သည့် နားမလည်မှုများ သို့မဟုတ် မမှန်မှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်လွှဲမပေးပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->