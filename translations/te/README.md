# ఫై కుక్ బుక్: Microsoft's Phi మోడల్స్‌తో హ్యాండ్స్-ఆన్ ఉదాహరణలు

[![GitHub Codespacesలో నమూనాలు తెరవండి మరియు ఉపయోగించండి](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containersలో తెరవండి](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub కాంట్రిబ్యూటర్స్](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub సమస్యలు](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub పుల్-రివెస్ట్‌లు](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs స్వాగతం](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub వాచర్స్](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ఫోర్క్స్](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub స్టార్‌లు](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

ఫై అనేది Microsoft ద్వారా అభివృద్ధి చేయబడిన ఓపెన్ సోర్స్ AI మోడల్స్ శ్రేణి.

ఫై ప్రస్తుతం అత్యంత శక్తివంతమైన మరియు తక్కువ ఖర్చుతో కూడుకున్న చిన్న భాషా మోడల్ (SLM), ఇది బహుభాషా, కారణం, టెక్స్ట్/చాట్ జెనరేషన్, కోడింగ్, చిత్రం, ఆడియో మరియు ఇతర సన్నివేశాలలో అత్యుత్తమ బెంచ్‌మార్క్‌లను కలిగి ఉంది.

మీరు ఫైని క్లౌడ్ లేదా ఎడ్జ్ పరికరాల్లో పయర్తించవచ్చు, మరియు మీరు పరిమిత కంప్యూటింగ్ శక్తితో సులభంగా జనరేటివ్ AI అనువర్తనాలను నిర్మించవచ్చు.

ఈ వనరులను ఉపయోగించడం ప్రారంభించడానికి ఈ దశలను అనుసరించండి:
1. **రిపాజిటరీని ఫోర్క్ చేయండి**: క్లిక్ చేయండి [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **రిపాజిటరీని క్లోన్ చేయండి**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord కమ్యూనిటీతో చేరండి మరియు నిపుణులు మరియు ఇతర డెవలపర్లను కలుసుకోండి**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/te/cover.eb18d1b9605d754b.webp)

### 🌐 బహుభాషా మద్దతు

#### GitHub యాక్షన్ ద్వారా మద్దతు (ఆటోమేటెడ్ & ఎప్పుడూ తాజా)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](./README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **స్థానికంగా క్లోన్ చేయడం ఇష్టం?**
>
> ఈ రిపాజిటరీలో 50+ భాషా అనువాదాలు ఉన్నాయి, ఇవి డౌన్‌లోడ్ పరిమాణాన్ని గణనీయంగా పెంచుతాయి. అనువాదాలు లేకుండా క్లోన్ చేయడానికి, స్పార్స్ చెకౌట్ ఉపయోగించండి:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> ఇది కోర్సును పూర్తి చేయడానికి అవసరమైన అన్ని విషయాలను చాలా త్వరగా డౌన్‌లోడ్‌ను అందిస్తుంది.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## సూచిక

- పరిచయం
  - [ఫై కుటుంబానికి స్వాగతం](./md/01.Introduction/01/01.PhiFamily.md)
  - [మీ పరిసరాన్ని సెటప్ చేయడం](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [ముఖ్య సాంకేతికతలను అవగాహన చేసుకోవడం](./md/01.Introduction/01/01.Understandingtech.md)
  - [ఫై మోడల్స్ కోసం AI భద్రత](./md/01.Introduction/01/01.AISafety.md)
  - [ఫై హార్డ్‌వేర్ మద్దతు](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [ఫై మోడల్స్ & వేదికలు మీద అందుబాటు](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai మరియు ఫై ఉపయోగించడం](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub మార్కెట్‌ప్లేస్ మోడల్స్](https://github.com/marketplace/models)
  - [Azure AI మోడల్ క్యాటలాగ్](https://ai.azure.com)

- వివిధ పరిసరాల్లో ఫై ఇన్ఫరెన్స్
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub మోడల్స్](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Microsoft Foundry మోడల్ క్యాటలాగ్](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI టూల్‌కిట్ VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry లోకల్](./md/01.Introduction/02/07.FoundryLocal.md)

- ఫై కుటుంబం ఇన్ఫరెన్స్
    - [iOSలో ఫై ఇన్ఫరెన్స్](./md/01.Introduction/03/iOS_Inference.md)
    - [Androidలో ఫై ఇన్ఫరెన్స్](./md/01.Introduction/03/Android_Inference.md)
    - [Jetsonలో ఫై ఇన్ఫరెన్స్](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PCలో ఫై ఇన్ఫరెన్స్](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX ఫ్రేమ్‌వర్క్‌తో ఫై ఇన్ఫరెన్స్](./md/01.Introduction/03/MLX_Inference.md)
    - [లోకల్ సర్వర్‌లో ఫై ఇన్ఫరెన్స్](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI టూల్‌కిట్ ఉపయోగించి రిమోట్ సర్వర్‌లో ఫై ఇన్ఫరెన్స్](./md/01.Introduction/03/Remote_Interence.md)
    - [రస్ట్‌తో ఫై ఇన్ఫరెన్స్](./md/01.Introduction/03/Rust_Inference.md)
    - [లోకల్‌లో ఫై-విజన్ ఇన్ఫరెన్స్](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers(అధికారిక మద్దతు)తో ఫై ఇన్ఫరెన్స్](./md/01.Introduction/03/Kaito_Inference.md)
-  [ఫై కుటుంబం కొలత](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ఉపయోగించి ఫై-3.5 / 4 కి కొలత వేయడం](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime కోసం జనరేటివ్ AI విస్తరణలతో ఫై-3.5 / 4 కి కొలత వేయడం](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ఉపయోగించి ఫై-3.5 / 4 కి కొలత వేయడం](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX ఫ్రేమ్‌వర్క్ ఉపయోగించి ఫై-3.5 / 4 కి కొలత వేయడం](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  ఫై మూల్యాంకనం
    - [స్పందన AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [మూల్యాంకనం కోసం Microsoft Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [మూల్యాంకనం కోసం Promptflow ఉపయోగించడం](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI సెర్చ్‌తో RAG
    - [Azure AI సెర్చ్‌తో Phi-4-mini మరియు Phi-4-мултимోడల్ (RAG) ఎలా ఉపయోగించాలి](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)
    - [SQLite FTS5 మరియు phi-4-mini తో జీరో-క్లౌడ్ లోకల్ హైబ్రిడ్ RAG](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-mini_Local_Hybrid_RAG_SQLite_FTS5.ipynb)

- ఫై అప్లికేషన్ అభివృద్ధి నమూనాలు
  - టెక్స్ట్ & చాట్ అప్లికేషన్లు
    - ఫై-4 నమూనాలు
      - [📓] [Phi-4-mini ONNX మోడల్‌తో చాట్](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 లోకల్ ONNX మోడల్ .NETతో చాట్](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [సెమెంటిక్ కర్నల్ ఉపయోగించి Phi-4 ONNX తో .NET కంసోల్ యాప్‌లో చాట్](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)

    - ఫై-3 / 3.5 నమూనాలు
      - [బ్రౌజర్‌లో లోకల్ చాట్బోట్ వాడకం Phi3, ONNX రన్‌టైమ్ వెబ్ మరియు WebGPU ఉపయోగించి](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [ఓపెన్‌వినో చాట్](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [మల్టీ మోడల్ - ఇంటరాక్టివ్ Phi-3-mini మరియు OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - రాపర్ నిర్మాణం మరియు Phi-3 ను MLFlow తో ఉపయోగించడం](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [మోడల్ ఆప్టిమైజేషన్ - ONNX రన్‌టైమ్ వెబ్ కోసం Phi-3-min మోడల్‌ను Olive తో ఎలా ఆప్టిమైజ్ చేయాలి](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 యాప్ Phi-3 mini-4k-instruct-onnx తో](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 మల్టీ మోడల్ ఏఐ శక్తివంత నోట్స్ యాప్ నమూనా](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [కస్టమ్ Phi-3 మోడల్స్‌ను Prompt flowతో ఫైన్-ట్యూన్ და ఇంటిగ్రేట్ చేయడం](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Microsoft Foundryలో Prompt flowతో కస్టమ్ Phi-3 మోడల్స్‌ను ఫైన్-ట్యూన్ и ఇంటిగ్రేట్ చేయడం](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft Foundryలో ఫైన్-ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్‌ను Microsoft's బాధ్యతాయుత AI సూత్రాలపై కేంద్రీకృతం చేస్తూ అంచనా వేయండి](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct భాషా పలుకుబడి నమూనా (చైనీస్/ఇంగ్లిష్)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG చాట్బోట్](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU ఉపయోగించి Phi-3.5-Instruct ONNXతో Prompt flow పరిష్కారాన్ని సృష్టించడం](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Android యాప్ సృష్టించడానికి Microsoft Phi-3.5 tflite ఉపయోగించడం](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET ఉదాహరణ, Microsoft.ML.OnnxRuntime ఉపయోగించి లోకల్ ONNX Phi-3 మోడల్ ఉపయోగించి](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [సెమాంటిక్ కర్నల్ మరియు Phi-3తో కన్సోల్ చాట్ .NET యాప్](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI ఇన్ఫరెన్స్ SDK కోడ్ ఆధారిత నమూనాలు
    - Phi-4 నమూనాలు
      - [📓] [Phi-4-multimodal ఉపయోగించి ప్రాజెక్ట్ కోడ్ సృష్టించడం](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 నమూనాలు
      - [Microsoft Phi-3 కుటుంబంతో మీ స్వంత Visual Studio Code GitHub Copilot చాట్ నిర్మించండి](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub మోడల్స్‌తో Phi-3.5 ఉపయోగించి మీ స్వంత Visual Studio Code చాట్ కోపిలట్ ఏజెంట్ సృష్టించండి](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - అభివృద్ధి(reasoning) నమూనాలు
    - Phi-4 నమూనాలు
      - [📓] [Phi-4-mini-reasoning లేదా Phi-4-reasoning నమూనాలు](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive తో Phi-4-mini-reasoning ఫైన్-ట్యూనింగ్](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLXతో Phi-4-mini-reasoning ఫైన్-ట్యూనింగ్](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub మోడల్స్ తో Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Microsoft Foundry మోడల్స్ తో Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - డెమోలు
      - [Hugging Face Spacesలో హోస్ట్ చేసిన Phi-4-mini డెమోలు](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Hugginge Face Spacesలో హోస్ట్ చేసిన Phi-4-multimodal డెమోలు](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - విజన్ నమూనాలు
    - Phi-4 నమూనాలు
      - [📓] [Phi-4-multimodal ఉపయోగించి చిత్రాలను చదవడం మరియు కోడ్ సృష్టించడం](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)
    - Phi-3 / 3.5 నమూనాలు
      -  [📓][Phi-3-vision-చిత్రం టెక్స్ట్ నుంచి టెక్స్ట్](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP ఇంబెడ్డింగ్](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [డెమో: Phi-3 రీసైక్లింగ్](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - విజువల్ లాంగ్వేజ్ అసిస్టెంట్ - Phi3-విజన్ మరియు OpenVINOతో](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 విజన్ Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 విజన్ OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 విజన్ మల్టీ-ఫ్రేమ్ లేదా మల్టీ-ఇమేజ్ నమూనా](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET ఉపయోగించి Phi-3 విజన్ లోకల్ ONNX మోడల్](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [మెను ఆధారిత Phi-3 విజన్ లోకల్ ONNX మోడల్ Microsoft.ML.OnnxRuntime .NET ఉపయోగించి](../../md/04.HOL/dotnet/src/LabsPhi304)

  - రీజనింగ్-విజన్ నమూనాలు
    - Phi-4-రిజనింగ్-విజన్-15B
      - [📓] [Phi-4-రిజనింగ్-విజన్-15B ఉపయోగించి జేవాకింగ్ గుర్తించడం](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb)
      - [📓] [Phi-4-రిజనింగ్-విజన్-15B ఉపయోగించి గణితం](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb)
      - [📓] [Phi-4-రిజనింగ్-విజన్-15B ఉపయోగించి UI గుర్తించడం](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb)

  - గణితం నమూనాలు
    -  Phi-4-మినీ-ఫ్లాష్-రిజనింగ్-ఇన్‌స్ట్రక్ట్ నమూనాలు  [Phi-4-మినీ-ఫ్లాష్-రిజనింగ్-ఇన్‌స్ట్రక్ట్ తో గణితం డెమో](./md/02.Application/09.Math/MathDemo.ipynb)

  - ఆడియో నమూనాలు
    - Phi-4 నమూనాలు
      - [📓] [Phi-4-multimodal ఉపయోగించి ఆడియో ట్రాన్స్క్రిప్ట్స్ తీసేసుకోవడం](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal ఆడియో నమూనా](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal స్పీచ్ అనువాద నమూనా](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET కన్సోల్ అప్లికేషన్ Phi-4-multimodal ఆడియో ఉపయోగించి ఆడియో ఫైల్ విశ్లేషించి ట్రాన్స్క్రిప్ట్ రూపొందించడం](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE నమూనాలు
    - Phi-3 / 3.5 నమూనాలు
      - [📓] [Phi-3.5 మిక్చర్ ఆఫ్ ఎక్స్పర్ట్స్ మోడల్స్ (MoEs) సోషల్ మీడియా నమూనా](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI సెర్చ్, మరియు LlamaIndex తో రిట్రీవల్-ఆగ్మెంటెడ్ జనరేషన్ (RAG) పైప్‌లైన్ నిర్మించడం](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - ఫంక్షన్ కాలింగ్ నమూనాలు
    - Phi-4 నమూనాలు 🆕
      -  [📓] [Phi-4-mini తో ఫంక్షన్ కాలింగ్ ఉపయోగించడం](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini తో బహుళ ఏజెంట్స్ సృష్టించడానికి ఫంక్షన్ కాలింగ్ ఉపయోగించడం](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama తో ఫంక్షన్ కాలింగ్ ఉపయోగించడం](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX తో ఫంక్షన్ కాలింగ్ ఉపయోగించడం](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - మల్టీమోడల్ మిక్సింగ్ నమూనాలు
    - Phi-4 నమూనాలు 🆕
      -  [📓] [ఫై-4 మల్టీమోడల్ టెక్నాలజీ జర్నలిస్ట్ గా ఉపయోగించడం](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET కన్సోల్ అప్లికేషన్ Phi-4 మల్టీమోడల్ ఉపయోగించి చిత్రాలను విశ్లేషించడం](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- ఫైన్-ట్యూనింగ్ ఫై నమూనాలు
  - [ఫైన్-ట్యూనింగ్ సన్నివేశాలు](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ఫైన్-ట్యూనింగ్ వర్సెస్ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [ఫైన్-ట్యూనింగ్ ద్వారా ఫై-3ని ఒక పరిశ్రమ నిపుణుడిగా మార్చడం](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [AI టూల్‌కిట్ ఉపయోగించి Phi-3 ఫైన్-ట్యూనింగ్ for VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure మషీన్ లెర్నింగ్ సర్వీస్ తో Phi-3 ఫైన్-ట్యూనింగ్](./md/03.FineTuning/Introduce_AzureML.md)
  - [Loraతో Phi-3 ఫైన్-ట్యూనింగ్](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLoraతో Phi-3 ఫైన్-ట్యూనింగ్](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Microsoft Foundryతో Phi-3 ఫైన్-ట్యూనింగ్](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDKతో Phi-3 ఫైన్-ట్యూనింగ్](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Oliveతో ఫైన్-ట్యూనింగ్](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Labతో ఫైన్-ట్యూనింగ్](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias తో Phi-3 విజన్ ఫైన్-ట్యూనింగ్](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)

  - [Apple MLX ఫ్రేమ్‌వర్క్‌తో Phi-3 ను ఫైన్-ట్యూన్ చేయడం](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision ఫైన్-ట్యూనింగ్ (అధికారిక మద్దతు)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure కంటైనర్లతో Phi-3 ను ఫైన్-ట్యూన్ చేయడం (అధికారిక మద్దతు)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 మరియు 3.5 Vision ఫైన్-ట్యూనింగ్](https://github.com/2U1/Phi3-Vision-Finetune)

- ప్రయోగాల శాల
  - [అత్యాధునిక నమూనాలను అన్వేషించడం: LLMs, SLMs, స్థానిక అభివృద్ధి మరియు మరిన్ని](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP సామర్థ్యాన్ని తెరవడం: Microsoft Olive తో ఫైన్-ట్యూనింగ్](https://github.com/azure/Ignite_FineTuning_workshop)

- అకాడమిక్ పరిశోధనా పత్రాలు మరియు ప్రచురణలు
  - [పాఠ్య పుస్తకాలు అన్ని కావాలి II: phi-1.5 సాంకేతిక నివేదిక](https://arxiv.org/abs/2309.05463)
  - [Phi-3 సాంకేతిక నివేదిక: మీ ఫోన్‌లో స్థానికంగా అధిక సామర్థ్యమైన భాషా నమూనా](https://arxiv.org/abs/2404.14219)
  - [Phi-4 సాంకేతిక నివేదిక](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini సాంకేతిక నివేదిక: మిశ్రమ-LoRAs ద్వారా సన్నబడ్డ కానీ శక్తివంతమైన బహుళమోడ్ భాషా నమూనాలు](https://arxiv.org/abs/2503.01743)
  - [వాహనంలో ఫంక్షన్-కాలింగ్ కోసం చిన్న భాషా నమూనాల оптимైజేషన్](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) ఒకाधिक-ఎంపిక ప్రశ్నల సమాధాన కోసం PHI-3 ఫైన్-ట్యూనింగ్: విధానం, ఫలితాలు, మరియు సవాళ్లు](https://arxiv.org/abs/2501.01588)
  - [Phi-4-రిజనింగ్ సాంకేతిక నివేదిక](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-మినీ-రిజనింగ్ సాంకేతిక నివేదిక](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi నమూనాలను ఉపయోగించడం

### Microsoft Foundry లో Phi

మీరు Microsoft Phi ఎలా ఉపయోగించాలో మరియు మీ వివిధ హార్డ్‌వేర్ పరికరాల్లో E2E పరిష్కారాలను ఎలా నిర్మించాలో నేర్చుకోవచ్చు. Phi ను ప్రత్యక్షంగా అనుభవించడానికి, నమూనాలతో ఆడడం మరియు మీ పరిస్తితుల కోసం Phi ను అనుకూలీకరించడం మొదలుపెట్టండి [Microsoft Foundry Azure AI మోడల్ క్యాటలాగ్](https://aka.ms/phi3-azure-ai) ఉపయోగించండి, మీరు [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) తో ప్రారంభించడంపై మరింత తెలుసుకోండి

**ప్లేగ్రౌండ్**
ప్రతి నమూనాకు నమూనాని పరీక్షించడానికి ప్రత్యేకమైన ప్లేగ్రౌండ్ ఉంది [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub Models లో Phi

మీరు Microsoft Phi ఎలా ఉపయోగించాలో మరియు మీ వివిధ హార్డ్‌వేర్ పరికరాల్లో E2E పరిష్కారాలను ఎలా నిర్మించాలో నేర్చుకోవచ్చు. Phi ను ప్రత్యక్షంగా అనుభవించడానికి, నమూనాతో ఆడడం మరియు మీ పరిస్తితుల కోసం Phi ను అనుకూలీకరించడం మొదలుపెట్టండి [GitHub Model క్యాటలాగ్](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ఉపయోగించండి, మీరు [GitHub Model క్యాటలాగ్](/md/02.QuickStart/GitHubModel_QuickStart.md) తో ప్రారంభించడంపై మరింత తెలుసుకోండి

**ప్లేగ్రౌండ్**
ప్రతి నమూనాకు [ఉదాహరణ కోసం ఒక ప్లేగ్రౌండ్](/md/02.QuickStart/GitHubModel_QuickStart.md) ఉంది.

### Hugging Face లో Phi

మీరు నమూనాను [Hugging Face](https://huggingface.co/microsoft) లో కూడా కనుగొనవచ్చు

**ప్లేగ్రౌండ్**
 [Hugging Chat ప్లేగ్రౌండ్](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 ఇతర కోర్సులు

మా బృందం ఇతర కోర్సులు ఉత్పత్తి చేస్తోంది! చూడండి:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j ప్రారంభికులకు](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js ప్రారంభికులకు](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain ప్రారంభికులకు](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / ఏజెంట్లు
[![AZD ప్రారంభికులకు](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI ప్రారంభికులకు](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP ప్రారంభికులకు](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI ఏజెంట్లు ప్రారంభికులకు](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### జనరేటివ్ AI సిరీస్
[![జనరేటివ్ AI ప్రారంభికులకు](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![జనరేటివ్ AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![జనరేటివ్ AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![జనరేటివ్ AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### కోర్ లెర్నింగ్
[![ML ప్రారంభికులకు](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![డేటా సైన్స్ ప్రారంభికులకు](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI ప్రారంభికులకు](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![సైబర్‌సెక్యూరిటీ ప్రారంభికులకు](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![వెబ్ డెవలప్‌మెంట్ ప్రారంభికులకు](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT ప్రారంభికులకు](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR అభివృద్ధి ప్రారంభికులకు](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### కోపైలట్ సిరీస్
[![AI జంట ప్రోగ్రామింగ్ కోసం Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET కోసం Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot సాహసం](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## బాధ్యతాయుతమైన AI

Microsoft మా కస్టమర్లు మా AI ఉత్పత్తులను బాధ్యతగా ఉపయోగించడంలో సహాయం చేయటానికి, మా అనుభవాలను పంచుకోవటానికి, మరియు Transparency Notes మరియు Impact Assessments వంటి సాధనాల ద్వారా నమ్మకాల ఆధారిత భాగస్వామ్యాలను నిర్మించడానికి కట్టుబడి ఉంది. ఈ వనరులలో చాలా వాటిని మీరు [https://aka.ms/RAI](https://aka.ms/RAI) వద్ద కనుగొనవచ్చు.
Microsoft బాధ్యతాయుతమైన AI పద్ధతులు మా AI సూత్రాలు – న్యాయం, విశ్వాసక్యత మరియు సురక్షత, గోప్యత మరియు భద్రత, సమగ్రత, పారదర్శకత, మరియు బాధ్యతాయుతత – పై ఆధారపడి ఉంటాయి.

ఈ నమూనా వంటి పెద్ద-స్థాయి సహజ భాష, చిత్రం, మరియు గాత్ర నమూనాలు అన్యాయంగా, అసమ్మతంగా లేదా అవమానకరంగానే ప్రవర్తించే అవకాశం ఉంది, ఇది ద్రోహాలను కలిగించవచ్చు. దయచేసి [Azure OpenAI సర్వీస్ Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ను సంప్రదించి ప్రమాదాలు మరియు పరిమితుల గురించి సమాచారం పొందండి.


ఈ ప్రమాదాలను తగ్గించడానికి సూచించబడిన పద్ధతి మీ ఆర్కిటెక్చర్‌లో హానికరమైన ప్రవర్తనను గుర్తించి నిరోధించగల సేఫ్టీ సిస్టమ్‌ను చేర్చడమే. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) అనేది స్వతంత్ర రక్షణా పొరను అందిస్తుంది, ఇది అప్లికేషన్ల మరియు సేవలలో హానికరమైన వాడుకరి-ఉత్పన్నము మరియు AI-ఉత్పన్నము కంటెంట్‌ను గుర్తించగలదు. Azure AI Content Safety టెక్స్ట్ మరియు ఇమేజ్ API లను కలిగి ఉంది, ఇవి హానికరమైన పదార్థాన్ని గుర్తించడానికి అనుమతిస్తాయి. Microsoft Foundry లో, Content Safety సేవ మీకు వివిధ మోడ్‌ల మధ్య హానికరమైన కంటెంట్‌ను గుర్తించడానికి నమూనా కోడ్‌ను వీక్షించడానికి, అన్వేషించడానికి మరియు ప్రయత్నించడానికి అవకాశాన్ని ఇస్తుంది. ఈ క్రింది [quickstart డాక్యుమెంటేషన్](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ఈ సేవకు అభ్యర్థనలు చేసే విధానంలో మీకు మార్గనిర్దేశం చేస్తుంది.

మరొక విషయం పరిగణనలోకి తీసుకోవలసినదైనది మొత్తం అప్లికేషన్ ప్రదర్శన. బహుముఖ మరియు బహుమోడల్ అప్లికేషన్లతో, మేము ప్రదర్శన అంటే మీరు మరియు మీ వినియోగదారులు అనుకున్న విధంగా సిస్టమ్ పనిచేస్తుంది, హానికరమైన ఔట్‌పుట్‌లు ఉత్పత్తి కాకుండా ఉంటాయి అని భావిస్తాము. [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ఉపయోగించి మీ మొత్తం అప్లికేషన్ యొక్క ప్రదర్శనను అంచనా వేయడం ముఖ్యం. మీరు కూడా [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) తో సృష్టించి, అంచనా వేయగల సామర్థ్యం కలిగి ఉన్నారు.

మీరు [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ఉపయోగించి మీ అభివృద్ధి పరిసరంలో మీ AI అప్లికేషన్‌ను అంచనా వేయవచ్చు. ఒక పరీక్ష డేటాసెట్ లేదా ఒక లక్ష్యం ఇవ్వబడినప్పుడు, మీ జనరేటివ్ AI అప్లికేషన్ ఉత్పత్తులను మీరు ఎంచుకున్న బిల్ట్-ఇన్ లేదా అనుకూల అంచనా కారులకు సంఖ్యాబద్ధంగా కొలవబడతాయి. మీ సిస్టమ్‌ను అంచనా లోకి తీసుకోవడానికి Azure AI Evaluation SDK తో ప్రారంభం కాని విధానం కోసం మీరు [quickstart గైడ్](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ను అనుసరించవచ్చు. ఒక సారి మీరు అంచనా నడుపుతుంటే, మీరు ఫలితాలను [Microsoft Foundry లో వీక్షించవచ్చు](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## ట్రేడ్మార్కులు

ఈ ప్రాజెక్ట్ ప్రాజెక్టులు, ఉత్పత్తులు లేదా సేవల కోసం ట్రేడ్మార్కులు లేదా లోగోలు ఉండవచ్చు. Microsoft ట్రేడ్మార్కులు లేదా లోగోలను అధీకృతంగా ఉపయోగించడం [Microsoft యొక్క ట్రేడ్మార్క్ & బ్రాండ్ మార్గదర్శకాలు](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ప్రకారం ఉండాలి మరియు వాటిని అనుసరించాలి.
ఈ ప్రాజెక్ట్ యొక్క మోడిఫైడ్ వెర్షన్‌లలో Microsoft ట్రేడ్మార్కులు లేదా లోగోలను ఉపయోగించడం గందరగోళాన్ని కలిగించకూడదు లేదా Microsoft అనుబంధతను సూచించకూడదు. మూడవ పార్టీ ట్రేడ్మార్కులు లేదా లోగోలను ఉపయోగించడం ఆ మూడవ పార్టీ విధానాలకు లోబడి ఉంటుంది.

## సహాయం పొందడం

మీరు అడ్డంకిలో పడినట్టైతే లేదా AI యాప్‌ల నిర్మాణంపై ఏవైనా ప్రశ్నలు ఉంటే, చేరండి:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

మీరు ఉత్పత్తి ఫీడ్‌బ్యాక్ లేదా దోషాలు ఎదుర్కొని ఉంటే సందర్శించండి:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->