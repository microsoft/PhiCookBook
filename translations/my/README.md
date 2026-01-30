# Phi Cookbook: Microsoft ရဲ့ Phi မော်ဒယ်တွေနဲ့ လက်တွေ့ အသုံးပြုမှု နမူနာများ

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

Phi သည် Microsoft မှ ဖန်တီးတဲ့ အဲဒီအောင်မြင်ပြီး အခမဲ့ အသုံးပြုနိုင်တဲ့ AI မော်ဒယ် စီးရီးတစ်ခုဖြစ်ပါတယ်။

Phi သည် လက်ရှိအချိန်မှာ အခြားငယ်မော်ဒယ်(Small Language Model, SLM) များထက် ပြင်းထန်ပြီး စျေးနှုန်းသက်သာဆုံး ဖြစ်ကာ၊ မျိုးစုံဘာသာစကားများ၊ ထောက်လှမ်းချက်၊ စာသား/စကားပြော ထုတ်လုပ်ခြင်း၊ ကုဒ်ရေးခြင်း၊ ပုံများ၊ အသံများနှင့် အခြားသော အခြေအနေများတွင် များစွာကောင်းမွန်တဲ့ ဘဏ္ဍာရေးစံချိန်များရှိပါသည်။

Phi ကို မိုးကောင်းကင်ပေါ်သို့ သို့မဟုတ် အနယ်နယ်အရပ်ရပ်တွင် တပ်ဆင်နိုင်ပြီး ၊ အစွမ်းသတ္တိ နည်းပါးသော ကွန်ပြူတာပါဝင်ပစ္စည်းများဖြင့် အလွယ်တကူ မျိုးထုတ် AI အက်ပလီကေးရှင်းများ တည်ဆောက်နိုင်ပါသည်။

ဤရင်းမြစ်များ များကို အသုံးပြု၍ စတင်ရန် အောက်ပါခြေလှမ်းများကို လိုက်နာပါ -
1. **Repository ကို Fork တင်ပါ**: Click [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Repository ကို Clone လုပ်ပါ**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord အသိုင်းအဝိုင်းထဲ ဝင်ရောက်ပြီး ကျွမ်းကျင်သူများနှင့် Developer များနှင့် တွေ့ဆုံကြပါ**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/my/cover.eb18d1b9605d754b.webp)

### 🌐 မျိုးစုံဘာသာစကား အထောက်အပံ့

#### GitHub Action မှ တကြိမ် သတ်မှတ်ပြီး အမြဲတမ်း Update လုပ်နေသည်

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](./README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **သင့်အား ဒေသခံအတိုင်း Clone လုပ်ချင်ပါသလား?**

> ဤ Repository တွင် ဘာသာစကား ၅၀ ကျော်ပါဝင်ပြီး ဒါကြောင့် ဒေါင်းလုပ် အရွယ်အစား တိုးစေပါတယ်။ ဘာသာပြန်မပါဘဲ Clone လုပ်ရန် အောက်ပါ sparse checkout ကို အသုံးပြုပါ:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> ဒါက သင်သင်ယူရမယ့် အရာအားလုံးကို အမြန်ဆင်းနိုင်စေပါလိမ့်မယ်။
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## အကြောင်းအရာ သိမ်းဆည်းမှု

- နိဒါန်း
  - [Phi မိသားစုသို့ ကြိုဆိုပါတယ်](./md/01.Introduction/01/01.PhiFamily.md)
  - [သင့်ပတ်ဝန်းကျင် ကို ပြင်ဆင်ခြင်း](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [ အဓိက နည်းပညာများ ကို နားလည်ခြင်း](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi မော်ဒယ်များအတွက် AI လုံခြုံရေး](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ပြောင်းလဲနိုင်မှု အထောက်အပံ့](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi မော်ဒယ်များနှင့် ပလက်ဖောင်းများအတွင်း အသုံးပြုနိုင်မှု](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai နှင့် Phi အသုံးပြုခြင်း](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace မော်ဒယ်များ](https://github.com/marketplace/models)
  - [Azure AI မော်ဒယ်ကတ်တာလော့(ကတ်လော့)မြေပုံ](https://ai.azure.com)

- Phi ကို မတူညီသော ပတ်ဝန်းကျင်များတွင် ဆောင်ရွက်ခြင်း
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub မော်ဒယ်များ](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry မော်ဒယ်ကတ်တာလော့](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi မိသားစုကို ဆောင်ရွက်ခြင်း
    - [iOS တွင် Phi ကို ဆောင်ရွက်ခြင်း](./md/01.Introduction/03/iOS_Inference.md)
    - [Android တွင် Phi ကို ဆောင်ရွက်ခြင်း](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson တွင် Phi ကို ဆောင်ရွက်ခြင်း](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC တွင် Phi ကို ဆောင်ရွက်ခြင်း](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework ဖြင့် Phi ကို ဆောင်ရွက်ခြင်း](./md/01.Introduction/03/MLX_Inference.md)
    - [Local Server တွင် Phi ကို ဆောင်ရွက်ခြင်း](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit အသုံးပြု၍ Remote Server တွင် Phi ကို ဆောင်ရွက်ခြင်း](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust ဖြင့် Phi ကို ဆောင်ရွက်ခြင်း](./md/01.Introduction/03/Rust_Inference.md)
    - [Vision Phi ကို Local တွင် ဆောင်ရွက်ခြင်း](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (တရားဝင်အထောက်အပံ့)ဖြင့် Phi ကို ဆောင်ရွက်ခြင်း](./md/01.Introduction/03/Kaito_Inference.md)

-  [Phi မိသားစု Quantifying](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ဖြင့် Phi-3.5 / 4 ကို Quantize လုပ်ခြင်း](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime အတွက် Generative AI extension ကို အသုံးပြု၍ Phi-3.5 / 4 ကို Quantize လုပ်ခြင်း](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ကို အသုံးပြု Phi-3.5 / 4 ကို Quantize လုပ်ခြင်း](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework ကို အသုံးပြု၍ Phi-3.5 / 4 ကို Quantize လုပ်ခြင်း](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi အကဲဖြတ်ခြင်း
    - [Responsible AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry ဖြင့် အကဲဖြတ်ခြင်း](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow အသုံးပြုပြီး အကဲဖြတ်ခြင်း](./md/01.Introduction/05/Promptflow.md)

- RAG နှင့် Azure AI Search
    - [Phi-4-mini နှင့် Phi-4-multimodal (RAG) ကို Azure AI Search နဲ့ အသုံးပြုပုံ](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi အက်ပလီကေးရှင်း ဖွံ့ဖြိုးတိုးတက်မှု နမူနာများ
  - စာသား နှင့် စကားပြော အက်ပလီကေးရှင်းများ
    - Phi-4 နမူနာများ 🆕
      - [📓] [Phi-4-mini ONNX မော်ဒယ်ဖြင့် စကားပြောပါ](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 local ONNX Model .NET ဖြင့် Chat](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Semantic Kernel ကို အသုံးပြု၍ Phi-4 ONNX ဖြင့် .NET Console App စကားပြော](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 နမူနာများ
      - [Phi3, ONNX Runtime Web နှင့် WebGPU ကို အသုံးပြု Local Browser Chatbot](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino မှ Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - အပြန်အလှန် Phi-3-mini နှင့် OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Wrapper တည်ဆောက်ခြင်းနှင့် Phi-3 ကို MLFlow နှင့်အသုံးပြုခြင်း](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Model Optimization - ONNX Runtime Web အတွက် Phi-3-min မော်ဒယ်ကို Olive ဖြင့် မည်သို့ပြုပြင်မည်နည်း](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx နှင့် WinUI3 အက်ပ်](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 Multi Model AI စွမ်းအားမြင့် မှတ်စုများ အက်ပ် နမူနာ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Prompt flow နှင့်အတူ စိတ်ကြိုက် Phi-3 မော်ဒယ်များကို Fine-tune နှင့် ပေါင်းစပ်ခြင်း](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry တွင် Prompt flow နှင့်အတူ စိတ်ကြိုက် Phi-3 မော်ဒယ်များကို Fine-tune နှင့် ပေါင်းစပ်ခြင်း](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft ရဲ့ တာဝန်ရှိ AI 원칙များကို အခြေခံ၍ Azure AI Foundry တွင် Fine-tuned Phi-3 / Phi-3.5 မော်ဒယ်ကို သုံးသပ်ခြင်း](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct ဘာသာစကားခန့်မှန်းမှု နမူနာ (တရုတ်/အင်္ဂလိပ်)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU အသုံးပြု၍ Phi-3.5-Instruct ONNX ဖြင့် Prompt flow ဖြေရှင်းချက် ဖန်တီးခြင်း](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite သုံးပြီး Android အက်ပ် ဖန်တီးခြင်း](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime ကို အသုံးပြု၍ ဒေသတွင်း ONNX Phi-3 မော်ဒယ်ဖြင့် Q&A .NET နမူနာ](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel နှင့် Phi-3 တို့ဖြင့် Console chat .NET အက်ပ်](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK ကုဒ်အခြေခံ နမူနာများ 
    - Phi-4 နမူနာများ 🆕
      - [📓] [Phi-4-multimodal ကို အသုံးပြု၍ စီမံကိန်းကုဒ် ပြုလုပ်ခြင်း](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 နမူနာများ
      - [Microsoft Phi-3 မိသားစုဖြင့် သင်၏ကိုယ်ပိုင် Visual Studio Code GitHub Copilot Chat တည်ဆောက်ခြင်း](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub မော်ဒယ်များဖြင့် Phi-3.5 အသုံးပြု၍ သင်၏ကိုယ်ပိုင် Visual Studio Code Chat Copilot Agent ဖန်တီးခြင်း](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - တိုးတက်သောအကြောင်းပြချက် နမူနာများ
    - Phi-4 နမူနာများ 🆕
      - [📓] [Phi-4-mini-reasoning သို့မဟုတ် Phi-4-reasoning နမူနာများ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive ဖြင့် Phi-4-mini-reasoning ကို Fine-tune လုပ်ခြင်း](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX ဖြင့် Phi-4-mini-reasoning ကို Fine-tune လုပ်ခြင်း](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub မော်ဒယ်များဖြင့် Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry မော်ဒယ်များဖြင့် Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - မျက်မှောက်ပြသချက်များ
      - [Phi-4-mini demos Hugging Face Spaces တွင် ဟိုပ်(Hosted)](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demos Hugginge Face Spaces တွင် ဟိုပ်(Hosted)](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - မြင်ကွင်း နမူနာများ
    - Phi-4 နမူနာများ 🆕
      - [📓] [Phi-4-multimodal ကို သုံး၍ ပုံများ ဖတ်ခြင်းနှင့် ကုဒ်ဖန်တီးခြင်း](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 နမူနာများ
      -  [📓][Phi-3-vision-ပုံစာသားမှ စာသားသို့](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [မော်ဒယ် ပြသချက်: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - မြင်ကွင်းဘာသာစကားအကူအညီ - Phi3-Vision နှင့် OpenVINO ဖြင့်](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision multi-frame သို့မဟုတ် multi-image နမူနာ](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET ကို အသုံးပြု၍ Phi-3 Vision ဒေသခံ ONNX မော်ဒယ်](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Microsoft.ML.OnnxRuntime .NET ကို အသုံးပြု၍ မီနူးအခြေခံ Phi-3 Vision ဒေသခံ ONNX မော်ဒယ်](../../md/04.HOL/dotnet/src/LabsPhi304)

  - သင်္ချာ နမူနာများ
    -  Phi-4-Mini-Flash-Reasoning-Instruct နမူနာများ 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct ဖြင့် သင်္ချာပညာ ပြသချက်](./md/02.Application/09.Math/MathDemo.ipynb)

  - အသံ နမူနာများ
    - Phi-4 နမူနာများ 🆕
      - [📓] [Phi-4-multimodal ဖြင့် အသံထုတ်ပြန်ချက်များ ဆွဲထုတ်ခြင်း](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal အသံ နမူနာ](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal စကားပြန်ခြင်း နမူနာ](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET console application ကို Phi-4-multimodal အသုံးပြု၍ အသံဖိုင် ခွဲခြမ်းစိတ်ဖြာပြီး transcript ဖန်တီးရန်](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE နမူနာများ
    - Phi-3 / 3.5 နမူနာများ
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) လူမှုမီဒီယာ နမူနာ](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search နှင့် LlamaIndex နှင့် အသုံးပြု၍ Retrieval-Augmented Generation (RAG) Pipeline တည်ဆောက်ခြင်း](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Function Calling နမူနာများ
    - Phi-4 နမူနာများ 🆕
      -  [📓] [Phi-4-mini ဖြင့် Function Calling ကို အသုံးပြုခြင်း](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini နှင့် Function Calling ကို အသုံးပြု၍ မျိုးစုံ အေးဂျင့်များ ဖန်တီးခြင်း](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama နှင့် Function Calling ကို အသုံးပြုခြင်း](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX နှင့် Function Calling ကို အသုံးပြုခြင်း](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Multimodal Mixing နမူနာများ
    - Phi-4 နမူနာများ 🆕
      -  [📓] [Phi-4-multimodal ကို နည်းပညာသတင်းထောက်အဖြစ် အသုံးပြုခြင်း](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET console application ကို Phi-4-multimodal ဖြင့် ပုံများကို ခွဲခြမ်းစိတ်ဖြာရန်](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi ကို Fine-tuning လုပ်ခြင်း နမူနာများ
  - [Fine-tuning အခြေအနေများ](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Fine-tuning နှင့် RAG ၏ ကွာခြားချက်](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 ကို စက်မှုအတွေ့အကြုံကျွမ်းကျင်သူအဖြစ် ပြောင်းလဲ fine-tuning လုပ်ခြင်း](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [AI Toolkit for VS Code ဖြင့် Phi-3 ကို Fine-tuning လုပ်ခြင်း](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service ဖြင့် Phi-3 ကို Fine-tuning လုပ်ခြင်း](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora ဖြင့် Phi-3 ကို Fine-tuning လုပ်ခြင်း](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora ဖြင့် Phi-3 ကို Fine-tuning လုပ်ခြင်း](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry ဖြင့် Phi-3 ကို Fine-tuning လုပ်ခြင်း](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK ဖြင့် Phi-3 ကို Fine-tuning လုပ်ခြင်း](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive ဖြင့် Fine-tuning လုပ်ခြင်း](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Lab ဖြင့် Fine-tuning](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias အသုံးပြု၍ Phi-3-vision အတွက် Fine-tuning](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework ဖြင့် Phi-3 ကို Fine-tuning လုပ်ခြင်း](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision (တရားဝင်ထောက်ပံ့မှု) ကို Fine-tuning လုပ်ခြင်း](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers (တရားဝင်ထောက်ပံ့မှု) ဖြင့် Phi-3 ကို Fine-tuning လုပ်ခြင်း](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 နှင့် 3.5 Vision ကို Fine-Tuning လုပ်ခြင်း](https://github.com/2U1/Phi3-Vision-Finetune)

- လက်တွေ့လေ့ကျင့်မှုဌာန
  - [သော့ချက်ဖြင့် မော်ဒယ်လတ်ဆတ်ခြင်း: LLMs, SLMs, ဒေသခံဖွံ့ဖြိုးတိုးတက်မှု နှင့် အခြားများ](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP စွမ်းအားဖွင့်လှစ်ခြင်း: Microsoft Olive ဖြင့် Fine-Tuning](https://github.com/azure/Ignite_FineTuning_workshop)

- ပညာရှင် သုတေသနစာတမ်းများ နှင့် ထုတ်ဝေစာမျက်နှာများ
  - [စာအုပ်များသာလိုအပ်သည် II: phi-1.5 နည်းပညာအစီရင်ခံစာ](https://arxiv.org/abs/2309.05463)
  - [Phi-3 နည်းပညာအစီရင်ခံစာ: သင်၏ဖုန်းပေါ်တွင် တိုက်ရိုက်အသုံးပြုနိုင်သော မြင့်မားသောစွမ်းဆောင်ရည်ရှိသော ဘာသာစကားမော်ဒယ်](https://arxiv.org/abs/2404.14219)
  - [Phi-4 နည်းပညာအစီရင်ခံစာ](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini နည်းပညာအစီရင်ခံစာ: Mixture-of-LoRAs ဖြင့် တင်းကျပ်ပြီး စွမ်းအားပြင်းသော Multimodal ဘာသာစကားမော်ဒယ်များ](https://arxiv.org/abs/2503.01743)
  - [ကားထဲတွင် လုပ်ဆောင်နိုင်သော Function-Calling များအတွက် အသေးစား ဘာသာစကားမော်ဒယ်များကို ထိရောက်စွာ တိုးတက်အောင် ပြုလုပ်ခြင်း](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) မျိုးစုံ ရွေးချယ်မေးခွန်း ဖြေဆိုရေးအတွက် PHI-3 ကို စိစစ်ညှိနှိုင်းခြင်း: နည်းလမ်းစနစ်၊ ရလဒ်များနှင့် စိန်ခေါ်မှုများ](https://arxiv.org/abs/2501.01588)
  - [Phi-4-ကြောင့် ဖြစ်ပေါ်မှု နည်းပညာအစီရင်ခံစာ](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-ကြောင့် ဖြစ်ပေါ်မှု နည်းပညာအစီရင်ခံစာ](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi မော်ဒယ်များကို အသုံးပြုခြင်း

### Azure AI Foundry မှာ Phi

သင်သည် Microsoft Phi ကို ဘယ်လို အသုံးပြုရမည်၊ သင့်စက်ပစ္စည်းများတွင် E2E ဖြေရှင်းချက်များ ဘယ်လို တည်ဆောက်ရမည်ကို သင်ယူနိုင်ပါသည်။ Phi ကို ကိုယ်တိုင်ခံစားရန်၊ မော်ဒယ်များနှင့် ကစားပြီး သင့်ဖြေရှင်းမှုအတွက် Phi ကို စိတ်တိုင်းကျပြင်ဆင်ပါ။ [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) တွင် သင်ပါဝင်နိုင်ပြီး [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) မှ စတင်ယူသင်ယူနိုင်ပါသည်။

**ကစားကွင်း**  
မော်ဒယ်တိုင်းအတွက် စမ်းသပ်နိုင်သော ကစားကွင်းတစ်ခုရှိသည် [Azure AI Playground](https://aka.ms/try-phi3)။

### GitHub Models တွင် Phi

သင်သည် Microsoft Phi ကို ဘယ်လို အသုံးပြုရမည်၊ သင့်စက်ပစ္စည်းများတွင် E2E ဖြေရှင်းချက်များ ဘယ်လို တည်ဆောက်ရမည်ကို သင်ယူနိုင်ပါသည်။ Phi ကို ကိုယ်တိုင်ခံစားရန်၊ မော်ဒယ်နှင့် ကစားပြီး သင့်ဖြေရှင်းမှုအတွက် Phi ကို စိတ်တိုင်းကျပြင်ဆင်ပါ။ [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) တွင် သင်ယင်းအား လေ့လာနိုင်ပြီး [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) မှ စတင်နိုင်ပါသည်။

**ကစားကွင်း**  
မော်ဒယ်တိုင်းအတွက် စမ်းသပ်နိုင်သော [ကစားကွင်းရှိသည်](/md/02.QuickStart/GitHubModel_QuickStart.md)။

### Hugging Face တွင် Phi

သင်သည် မော်ဒယ်ကို [Hugging Face](https://huggingface.co/microsoft) တွင်လည်း ရှာဖွေတွေ့ရှိနိုင်သည်။

**ကစားကွင်း**  
[Hugging Chat ကစားကွင်း](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 အခြားသင်တန်းများ

ကျွန်ုပ်တို့အဖွဲ့သည် အခြားသင်တန်းများကို ထုတ်လုပ်လျက်ရှိသည်။ ပြန်ကြည့်ပါ-

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

## တာဝန်ယူသော AI

Microsoft သည် ကျွန်ုပ်တို့၏ ग्राहकများအား AI ထုတ်ကုန်များကို တာဝန်ယူစွာ အသုံးပြုနိုင်ရန် ကူညီပေးရန်၊ ကျွန်ုပ်တို့၏သင်ယူမှုများကို မျှဝေရန်နှင့် Transparency Notes နှင့် Impact Assessments ကဲ့သို့သော ကိရိယာများမှတဆင့် ယုံကြည်မှုအခြေပြု မိတ်ဖက်ဆက်ဆံရေးများ တည်ဆောက်ရန် ကြိုးပမ်းနေသည်။ ဤရင်းမြစ်များအချို့ကို [https://aka.ms/RAI](https://aka.ms/RAI) တွင် ရှာဖွေတွေ့ရှိနိုင်သည်။  
Microsoft ၏ တာဝန်ယူသော AI မှုလုပ်ငန်းစဥ်သည် တရားမျှတမှု၊ ယုံကြည်စိတ်ချရမှုနှင့် လုံခြုံမှု၊ ကိုယ်ရေးကိုယ်တာရေးရာနှင့် လုံခြုံမှု၊ ထည့်သွင်းဝင်စားမှု၊ ထင်ဟပ်ပြတ်သားမှုနှင့် တာဝန်ယူမှုတို့ကို အခြေခံသည်။

ဤနမူနာတွင် အသုံးပြုသော ကြီးမားသော ပုံမှန်ဘာသာစကား၊ ပုံရိပ်နှင့် အသံ မော်ဒယ်များသည် မတရားမှု၊ ယုံကြည်ရမှုမရှိမှု သို့မဟုတ် မရိုးသားမှု အပြုအမူများ ပြုလုပ်နိုင်ပြီး ထိုဖြစ်နိုင်ခြေများကြောင့် အန္တရာယ်များ ဖြစ်ပေါ်နိုင်သည်။ အန္တရာယ်များနှင့် ကန့်သတ်ချက်များအကြောင်း သတိပေးချက်များကို သိရှိရန် [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ကို အကြံပြုပါသည်။

ဤအန္တရာယ်များကို လျော့ပါးစေရန် အကြံပြုထားသည့်နည်းလမ်းမှာ သင့်လိပ်စာမှအန္တရာယ်ရှိသော အပြုအမူများကို ရှာဖွေကာ တားဆီးနိုင်သည့် လုံခြုံရေးစနစ်တစ်ခု ထည့်သွင်းဆောင်ရွက်ခြင်းဖြစ်သည်။ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) သည် လွတ်လပ်သည့် ကာကွယ်မှုအဆင့်တစ်ခု ပေးကာ အသုံးပြုသူများနှင့် AI မှ ထုတ်လုပ်သော အန္တရာယ်များရှိနိုင်သော အကြောင်းအရာများကို တိုင်းထွာကာ ရှာဖွေပေးနိုင်သည်။ Azure AI Content Safety သည် စာသားနှင့် ပုံရိပ် API များပါဝင်ပြီး အန္တရာယ်ရှိနိုင်သည့် အကြောင်းအရာများကို ရှာဖွေစစ်ဆေးနိုင်သည်။ Azure AI Foundry အတွင်း Content Safety ၀န်ဆောင်မှုသည် မတူညီသော ပုံစံများဖြင့် အန္တရာယ်ရှိသော အကြောင်းအရာများကို တွေ့ရှိရန် နမူနာကုဒ်ကို ကြည့်ရှု၊ သုတေသနလုပ်ခြင်းနှင့် စမ်းသပ်အသုံးပြုခွင့် ပေးသည်။ နောက်ပါ [အလျင်အမြန်စတင် အသုံးပြုခြင်း ဉပမာစာတမ်း](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) သည် ၀န်ဆောင်မှုအား တောင်းဆိုပုံ လမ်းညွှန်ပေးသည်။

တစ်ခုရော အခြားတစ်ခုအား ထည့်သွင်းစဉ်းစားရမည့်အချက်မှာ တိုးတက်မှု စနစ်၏ စုစုပေါင်း ဆောင်ရွက်မှု ဖြစ်သည်။ မျိုးစုံပုံစံနှင့် မော်ဒယ်များ ဖြင့်ဖွဲ့စည်းထားသော အသုံးပြုမှုများတွင်၊ ယင်းစနစ်သည် သင့်နှင့် သင့်အသုံးပြုသူများ စောင့်ကြည့်သည့်အတိုင်း လုပ်ဆောင်နိုင်ရမည်ဖြစ်ပြီး အန္တရာယ်ဖြစ်ပေါ်စေသော အထွက်အပေါ် မထုတ်ပေးသော ဖြစ်ရမည်။ သင့်စုစုပေါင်း application ၏ စွမ်းဆောင်ရည်ကို [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) အသုံးပြုကာ သုံးသပ်ရန် အရေးကြီးသည်။ သင်မှာ [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ဖြင့် ဖန်တီးခြင်းနှင့် သုံးသပ်နိုင်ခွင့်ရှိသည်။
သင်၏ AI အက်ပ်လီကေးရှင်းကို သင်၏ ဖန်တီးရေးပတ်ဝန်းကျင်တွင် [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) အသုံးပြု၍ သတ်မှတ်နိုင်ပါသည်။ စမ်းသပ်ဒေတာသိုလုပ်ဆောင်ချက်တစ်ခု သို့မဟုတ် ရည်ရွယ်ချက်တစ်ခုကို ပေးလိုက်ပါက သင်၏ကြိုတင်ဖန်တီး AI အက်ပ်လီကေးရှင်း၏ ဖန်တီးမှုများကို အဆင့်သတ်မှတ်သည့် အပြုအမူအခြေခံ ထည့်သွင်းထားသော အကဲဖြတ်သူများ သို့မဟုတ် သင်ရွေးချယ်ထားသော အကဲဖြတ်သူများဖြင့် အရေတွက် ဖော်ပြနိုင်သည်။ သင်၏ စနစ်ကို သတ်မှတ်ရန် azure ai evaluation sdk နှင့် စတင်ရန်၊ [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ကို လိုက်နာနိုင်ပါသည်။ အကဲဖြတ်ပြေးနေစဉ်အား ပြီးစီးသည်နှင့် ချက်ချင်း [Azure AI Foundry တွင် ရလဒ်များကို ကြည့်ရှု](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) နိုင်ပါသည်။

## အမှတ်တံဆိပ်များ

ဤ ပရောဂျက်တွင် ပရောဂျက်၊ ထုတ်ကုန်များ သို့မဟုတ် ဝန်ဆောင်မှုများအတွက် အမှတ်တံဆိပ်များ သို့မဟုတ် လိုဂိုများ ပါဝင်နိုင်သည်။ Microsoft ၏ အမှတ်တံဆိပ်များ သို့မဟုတ် လိုဂိုများကို အတည်ပြုထားခြင်းနှင့် အသုံးပြုခြင်းမှာ [Microsoft ၏ အမှတ်တံဆိပ်နှင့် အမှတ်တံဆိပ် လမ်းညွှန်ချက်များ](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) အတိုင်း လိုက်နာသင့်ပါသည်။
Microsoft အမှတ်တံဆိပ်များ သို့မဟုတ် လိုဂိုများကို ပြင်ဆင်ထားသော ဗားရှင်းများတွင် အသုံးပြုခြင်းသည် ရောထွေးမှု ဖြစ်စေခြင်း သို့မဟုတ် Microsoft အား ထောက်ပံ့ကြောင်း သက်မှတ်ခြင်း မဖြစ်အောင် သတိထားရမည်။ တတိယဘက် အမှတ်တံဆိပ်များ သို့မဟုတ် လိုဂိုများကို အသုံးပြုခြင်းသည် အဆိုပါ တတိယဘက်၏ စည်းမျဉ်းစည်းကမ်းများအောက်တွင် ဖြစ်သည်။

## ကူညီမှု ရယူရန်

AI အက်ပ်များ ဖန်တီးရာတွင် အခက်အခဲ ရှိပါက သို့မဟုတ် မေးခွန်းများရှိပါက ဝင်ပါ -

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

ထုတ်ကုန်တုံ့ပြန်ချက် သို့မဟုတ် အမှားများရှိပါက ဖန်တီးရာတွင် ဝင်ရောက်ကြည့်ရှုနိုင်ပါသည်-

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အကြောင်းကြားချက်**  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှုဖြစ်သည့် [Co-op Translator](https://github.com/Azure/co-op-translator) အားအသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ သင်္ကေတတိကျမှုရှိစေရန်ကြိုးစားပေမယ့် အလိုအလျောက်ဘာသာပြန်ချက်များတွင် မှားယွင်းချက်များ သို့မဟုတ် တိကျမှုမြင့်မမှန်ကန်မှုများ ပါဝင်နိုင်ကြောင်း ဂရုပြုပါရန် တောင်းဆိုအပ်ပါသည်။ မူလစာရွက်စာတမ်းကို မိခင်ဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသောအရင်းအမြစ်အဖြစ် သတ်မှတ်စဉ်းစားသင့်ပါသည်။ အရေးကြီးသောအချက်အလက်များအတွက် သက်ဆိုင်ရာ ဝန်ဆောင်မှုပေးသူများမှ လူ့ဘာသာပြန်ချက်ကို လက်ခံအသုံးပြုရန်အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများ၊ အနားမလည်မှုများအတွက် ကျွန်ုပ်တို့မှာ တာဝန်မရှိပါကြောင်း အသိပေးအပ်ပါသည်။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->