<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef3a50368712b1a7483d0def1f70c490",
  "translation_date": "2025-12-21T15:12:15+00:00",
  "source_file": "README.md",
  "language_code": "te"
}
-->
# ఫై కుక్‌బుక్: Microsoft యొక్క Phi మోడల్స్‌తోHands-On ఉదాహరణలు

[![GitHub Codespacesలో సాంపిల్స్ ఓపెన్ చేసి ఉపయోగించండి](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containersలో ఓపెన్ చేయండి](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub కాంట్రిబ్యూటర్లు](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub సమస్యలు](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub పుల్-రిక్వెస్ట్లు](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs స్వాగతం](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub వీక్షకులు](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ఫోర్క్స్](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub స్టార్స్](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry డిస్కార్డ్](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi అనేది Microsoft అభివృద్ధి చేసిన ఓపెన్ సోర్స్ AI మోడల్స్ సిరీస్.

Phi ప్రస్తుతం అత్యంత శక్తివంతమైన మరియు వ్యయపరంగా సమర్థవంతమైన స్మాల్ లాంగ్వేజ్ మోడల్ (SLM) గా ఉంది, బహుభాషా, కారణాన్ని అర్థమാക്കడం, టెక్స్ట్/చాట్ జనరేషన్, కోడింగ్, ఇమేజ్‌లు, ఆడియో మరియు ఇతర సన్నివేశాలలో చాలా మంచి బెంచ్‌మార్క్‌లను చూపుతుంది.

మీరు Phi ను క్లౌడ్‌లో లేదా ఎడ్జ్ డివైసుల్లో డిప్లాయ్ చేయవచ్చు, మరియు పరిమిత కంప్యూటింగ్ శక్తితో సులభంగా జనరేటివ్ AI అప్లికేషన్‌లను నిర్మించవచ్చు.

ఈ వనరులను ఉపయోగించడం ప్రారంభించడానికి ఈ దశలను అనుసరించండి :
1. **రిపోజిటరీని ఫోర్క్ చేయండి**: క్లిక్ చేయండి [![GitHub ఫోర్క్స్](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **రిపోజిటరీని క్లోన్ చేయండి**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord Communityలో చేరి నిపుణులు మరియు ఇతర డెవలపర్లను కలవండి**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![కవర్](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.te.png)

### 🌐 బహుభాషా మద్దతు

#### GitHub Action ద్వారా మద్దతు (ఆటోమేటెడ్ & ఎప్పుడూ నవీకరించబడే)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[అరబిక్](../ar/README.md) | [బెంగాలీ](../bn/README.md) | [బల్గేరియన్](../bg/README.md) | [బర్మీస్ (మయన్మార్)](../my/README.md) | [చైనీస్ (సరళీకృత)](../zh/README.md) | [చైనీస్ (సాంప్రదాయ, హాంగ్ కాంగ్)](../hk/README.md) | [చైనీస్ (సాంప్రదాయ, మకావ్)](../mo/README.md) | [చైనీస్ (సాంప్రదాయ, తైవాన్)](../tw/README.md) | [క్రోవేషియన్](../hr/README.md) | [చెక్](../cs/README.md) | [డేనిష్](../da/README.md) | [డచ్](../nl/README.md) | [ఎస్టోనియన్](../et/README.md) | [ఫిన్నిష్](../fi/README.md) | [ఫ్రెంచ్](../fr/README.md) | [జర్మన్](../de/README.md) | [గ్రీకు](../el/README.md) | [హేబ్రూ](../he/README.md) | [హిందీ](../hi/README.md) | [హంగేరియన్](../hu/README.md) | [ఇండోనేషియన్](../id/README.md) | [ఇటాలియన్](../it/README.md) | [జపనీస్](../ja/README.md) | [కన్నడ](../kn/README.md) | [కోరియన్](../ko/README.md) | [లిథువేనియన్](../lt/README.md) | [మలయ్](../ms/README.md) | [మలయాళం](../ml/README.md) | [మరాఠీ](../mr/README.md) | [నేపాలి](../ne/README.md) | [నైజీరియన్ పిడ్జిన్](../pcm/README.md) | [నార్వేజియన్](../no/README.md) | [పర్స్ (ఫార్సీ)](../fa/README.md) | [పోలిష్](../pl/README.md) | [పార్తుగీస్ (బ్రెజిల్)](../br/README.md) | [పార్తుగీస్ (పోర్చుగల్)](../pt/README.md) | [పంజాబీ (గుర్ముఖీ)](../pa/README.md) | [రోమానియన్](../ro/README.md) | [రష్యన్](../ru/README.md) | [సెర్బియన్ (సిరిలిక్)](../sr/README.md) | [స్లోవాక్](../sk/README.md) | [స్లోవేనియన్](../sl/README.md) | [స్పానిష్](../es/README.md) | [స్వాహిలి](../sw/README.md) | [స్వీడిష్](../sv/README.md) | [టాగალోగ్ (ఫిలిపినో)](../tl/README.md) | [తమిళం](../ta/README.md) | [తెలుగు](./README.md) | [థాయ్](../th/README.md) | [టర్కిష్](../tr/README.md) | [ఉక్రెనియన్](../uk/README.md) | [ఉర్దూ](../ur/README.md) | [వియత్నామీస్](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## విషయ సూచిక

- పరిచయం
  - [Phi కుటుంబానికి స్వాగతం](./md/01.Introduction/01/01.PhiFamily.md)
  - [మీ పరిసరాన్ని సెటప్ చేయడం](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [ప్రధాన టెక్నాలజీలను అర్థం చేసుకోవడం](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi మోడల్స్ కోసం AI భద్రత](./md/01.Introduction/01/01.AISafety.md)
  - [Phi హార్డ్వేర్ మద్దతు](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [ప్లాట్‌ఫారమ్‌లలో Phi మోడల్స్ & అందుబాటుదనం](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai మరియు Phi ఉపయోగించడం](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace Models](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- విభిన్న పరిసరాల్లో Phi ఇన్ఫెరెన్స్
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub మోడల్స్](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry మోడల్ క్యాటలాగ్](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi ఫ్యామిలీలో ఇన్ఫెరెన్స్
    - [iOSలో Phi ఇన్ఫెరెన్స్](./md/01.Introduction/03/iOS_Inference.md)
    - [Androidలో Phi ఇన్ఫెరెన్స్](./md/01.Introduction/03/Android_Inference.md)
    - [Jetsonలో Phi ఇన్ఫెరెన్స్](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PCలో Phi ఇన్ఫెరెన్స్](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX ఫ్రేమ్‌వర్క్‌తో Phi ఇన్ఫెరెన్స్](./md/01.Introduction/03/MLX_Inference.md)
    - [లోకల్ సర్వర్‌లో Phi ఇన్ఫెరెన్స్](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit ఉపయోగించి రిమోట్ సర్వర్‌లో Phi ఇన్ఫెరెన్స్](./md/01.Introduction/03/Remote_Interence.md)
    - [Rustతో Phi ఇన్ఫెరెన్స్](./md/01.Introduction/03/Rust_Inference.md)
    - [లోకల్‌లో Phi విజన్ ఇన్ఫెరెన్స్](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers తో Phi ఇన్ఫెరెన్స్ (ఆధికారిక మద్దతు)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi ఫ్యామిలీని క్వాంటిఫై చేయడం](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ఉపయోగించి Phi-3.5 / 4 క్వాంటైజింగ్](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Generative AI extensions for onnxruntime ఉపయోగించి Phi-3.5 / 4 క్వాంటైజింగ్](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ఉపయోగించి Phi-3.5 / 4 క్వాంటైజింగ్](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework ఉపయోగించి Phi-3.5 / 4 క్వాంటైజింగ్](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi మూల్యాంకనం
    - [బాధ్యతాయుత AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [మూల్యాంకనానికి Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [మూల్యాంకనానికి Promptflow ఉపయోగించడం](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search తో RAG
    - [Azure AI Search తో Phi-4-mini మరియు Phi-4-multimodal(RAG) ఎలా ఉపయోగించాలో](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi అప్లికేషన్ అభివృద్ధి నమూనాలు
  - పాఠ్యం & చాట్ అప్లికేషన్లు
    - Phi-4 నమూనాలు 🆕
      - [📓] [Phi-4-mini ONNX మోడల్‌తో చాట్](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 స్థానిక ONNX మోడల్‌తో చాట్ .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel ఉపయోగించి Phi-4 ONNXతో .NET కన్సోల్ అప్లికేషన్ ద్వారా చాట్](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 నమూనాలు
      - [Phi3, ONNX Runtime Web మరియు WebGPU ఉపయోగించి బ్రౌసర్‌లో లోకల్ చాట్‌బాట్](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino చాట్](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [మల్టీ మోడల్ - ఇంటరాక్టివ్ Phi-3-mini మరియు OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ఒక ర్యాపర్ నిర్మించటం మరియు MLFlow తో Phi-3 ఉపయోగించడం](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [మోడల్ ఆప్టిమైజేషన్ - Olive తో ONNX Runtime Web కోసం Phi-3-min మోడల్‌ను ఎలా ఆప్టిమైజ్ చేయాలి](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx తో WinUI3 యాప్](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 బహుమోడల్ AI-ప్రేరిత నోట్స్ యాప్ సాంపుల్](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Prompt flow తో కస్టమ్ Phi-3 మోడల్స్‌ను ఫైన్‑ట్యూన్ చేసి అనుసంధానం చేయండి](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry లో Prompt flow తో కస్టమ్ Phi-3 మోడల్స్‌ను ఫైన్‑ట్యూన్ చేసి అనుసంధానించండి](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft యొక్క జవాబుదారీతన AI సిద్ధాంతాలపై దృష్టి సారిస్తూ Azure AI Foundry లో ఫైన్‑ట్యూన్ చేసిన Phi-3 / Phi-3.5 మోడల్‌ను మూల్యాంకనం చేయండి](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct భాష పూర్వానుమాన నమూనా (చైనీస్/ఇంగ్లీష్)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG చాట్‌బాట్](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Phi-3.5-Instruct ONNX తో Prompt flow పరిష్కారాన్ని సృష్టించడానికి Windows GPU ఉపయోగించడం](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Android యాప్ సృష్టించడానికి Microsoft Phi-3.5 tflite ఉపయోగించడం](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime ఉపయోగించి స్థానిక ONNX Phi-3 మోడల్ ఉపయోగించే Q&A .NET ఉదాహరణ](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel మరియు Phi-3 తో Console chat .NET యాప్](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK Code Based Samples 
    - Phi-4 ఉదాహరణలు 🆕
      - [📓] [Phi-4-multimodal ఉపయోగించి ప్రాజెక్ట్ కోడ్ ఉత్పత్తి చేయండి](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 ఉదాహరణలు
      - [మీ స్వంత Visual Studio Code కోసం GitHub Copilot Chat ను Microsoft Phi-3 ఫ్యామిలీతో నిర్మించండి](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub Models ద్వారా Phi-3.5 తో మీ స్వంత Visual Studio Code Chat Copilot Agent ను సృష్టించండి](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - అడ్వాన్స్‌డ్ రీజనింగ్ ఉదాహరణలు
    - Phi-4 ఉదాహరణలు 🆕
      - [📓] [Phi-4-mini-reasoning లేదా Phi-4-reasoning ఉదాహరణలు](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive తో Phi-4-mini-reasoning ను ఫైన్‑ట్యూన్ చేయడం](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX తో Phi-4-mini-reasoning ను ఫైన్‑ట్యూన్ చేయడం](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub Models తో Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry Models తో Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demos
      - [Hugging Face Spaces లో హోస్ట్ చేసిన Phi-4-mini డెమోస్](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Hugginge Face Spaces లో హోస్ట్ చేసిన Phi-4-multimodal డెమోస్](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Vision Samples
    - Phi-4 ఉదాహరణలు 🆕
      - [📓] [Phi-4-multimodal ఉపయోగించి చిత్రాలను చదవడం మరియు కోడ్ రూపొందించడం](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 ఉదాహరణలు
      -  [📓][Phi-3-vision-చిత్రం టెక్స్ట్ నుండి టెక్స్ట్](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP ఎంబెడింగ్](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [డెమో: Phi-3 రీసైక్లింగ్](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - విజువల్ భాష సహాయకుడు - Phi3-Vision మరియు OpenVINO తో](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 విజన్ Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 విజన్ OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 విజన్ మల్టీఫ్రేమ్ లేదా మల్టీ‑ఇమేజ్ నమూనా](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET ఉపయోగించి Phi-3 విజన్ స్థానిక ONNX మోడల్](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [మెనూ ఆధారిత Phi-3 విజన్ స్థానిక ONNX మోడల్ Microsoft.ML.OnnxRuntime .NET ఉపయోగించి](../../md/04.HOL/dotnet/src/LabsPhi304)

  - గణితం ఉదాహరణలు
    -  Phi-4-Mini-Flash-Reasoning-Instruct ఉదాహరణలు 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct తో గణితం డెమో](./md/02.Application/09.Math/MathDemo.ipynb)

  - ఆడియో ఉదాహరణలు
    - Phi-4 ఉదాహరణలు 🆕
      - [📓] [Phi-4-multimodal ఉపయోగించి ఆడియో ట్రాన్స్క్రిప్ట్‌లను పొందడం](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal ఆడియో సాంపుల్](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal స్పీచ్ అనువాద నమూనా](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET కాంసోల్ అప్లికేషన్ Phi-4-multimodal ఆడియో ఉపయోగించి ఆడియో ఫైల్‌ను విశ్లేషించడానికి మరియు ట్రాన్స్క్రిప్ట్ ఉత్పత్తి చేయడానికి](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE ఉదాహరణలు
    - Phi-3 / 3.5 ఉదాహరణలు
      - [📓] [Phi-3.5 మిక్స్చర్ ఆఫ్ ఎక్స్‌పర్ట్స్ మోడల్స్ (MoEs) సోషల్‌మీడియా నమూనా](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, మరియు LlamaIndex ఉపయోగించి Retrieval-Augmented Generation (RAG) పైప్‌లైన్ నిర్మించడం](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - ఫంక్షన్ కాలింగ్ ఉదాహરણలు
    - Phi-4 ఉదాహరణలు 🆕
      -  [📓] [Phi-4-mini తో ఫంక్షన్ కాలింగ్ ఉపయోగించడం](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini తో బహు-ఏజెంట్స్ సృష్టించడానికి ఫంక్షన్ کالింగ్ ఉపయోగించడం](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama తో ఫంక్షన్ కాలింగ్ ఉపయోగించడం](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX తో ఫంక్షన్ కాలింగ్ ఉపయోగించడం](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - మల్టీమోడల్ మిక్సింగ్ ఉదాహరణలు
    - Phi-4 ఉదాహరణలు 🆕
      -  [📓] [టెక్నాలజీ జర్నలిస్ట్‌గా Phi-4-multimodal ఉపయోగించడం](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET కాంసోల్ అప్లికేషన్ Phi-4-multimodal ఉపయోగించి చిత్రాలను విశ్లేషించడానికి](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi ఫైన్‑ట్యూనింగ్ ఉదాహరణలు
  - [ఫైన్‑ట్యూనింగ్ సన్నివేశాలు](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ఫైన్‑ట్యూనింగ్ vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [ఫైన్‑ట్యూనింగ్: Phi-3 ను ఒక పరిశ్రమ నిపుణుడిగా మార్చండి](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code కోసం AI Toolkit తో Phi-3 ను ఫైన్‑ట్యూన్ చేయడం](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service తో Phi-3 ను ఫైన్‑ట్యూన్ చేయడం](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora తో Phi-3 ను ఫైన్‑ట్యూన్ చేయడం](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora తో Phi-3 ను ఫైన్‑ట్యూన్ చేయడం](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry తో Phi-3 ను ఫైన్‑ట్యూన్ చేయడం](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK తో Phi-3 ను ఫైన్‑ట్యూన్ చేయడం](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive తో ఫైన్‑ట్యూనింగ్](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive హ్యాండ్స్‑ఆన్ లాబ్ తో ఫైన్‑ట్యూనింగ్](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias తో Phi-3‑విజన్ ఫైన్‑ట్యూనింగ్](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework తో Phi-3 ను ఫైన్‑ట్యూన్ చేయడం](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3‑విజన్ ఫైన్‑ట్యూనింగ్ (ప్రాధికారిక మద్దతు)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS , Azure Containers తో Phi-3 ను ఫైన్‑ట్యూన్ (ప్రాధికారిక మద్దతు)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 మరియు 3.5 విజన్ ఫైన్‑ట్యూనింగ్](https://github.com/2U1/Phi3-Vision-Finetune)

- హ్యాండ్స్ ఆన్ ల్యాబ్
  - [అత్యాధునిక మోడల్స్‌ను అన్వేషించడం: LLMs, SLMs, లోకల్ డెవలప్‌మెంట్ మరియు మరికొన్ని](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP సామర్థ్యాన్ని అన్లాక్ చేయడం: Microsoft Olive తో ఫైన్‑ట్యూనింగ్](https://github.com/azure/Ignite_FineTuning_workshop)

- అకాడెమిక్ పరిశోధనా పత్రాలు మరియు ప్రచురణలు
  - [Textbooks Are All You Need II: phi-1.5 సాంకేతిక నివేదిక](https://arxiv.org/abs/2309.05463)
  - [Phi-3 సాంకేతిక నివేదిక: మీ ఫోన్‌లో స్థానికంగా అత్యంత సామర్థ్యవంతమైన భాషా మోడల్](https://arxiv.org/abs/2404.14219)
  - [Phi-4 సాంకేతిక నివేదిక](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini సాంకేతిక నివేదిక: Mixture-of-LoRAs ద్వారా సంక్షిప్త కాని శక్తివంతమైన బహుమాధ్యమ భాషా నమూనాలు](https://arxiv.org/abs/2503.01743)
  - [వాహనంలో ఫంక్షన్-కాల్ కోసం చిన్న భాషా నమూనాలను ఆప్టిమైజ్ చేయడం](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3ని బహుళ ఎంపిక ప్రశ్నల సమాధానాల కోసం ఫైన్-ట్యూన్ చేయడం: విధానం, ఫలితాలు మరియు సవాళ్లు](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning సాంకేతిక నివేదిక](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning సాంకేతిక నివేదిక](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi మోడల్స్ ఉపయోగించడం

### Azure AI Foundryలో Phi

Microsoft Phiని ఎలా ఉపయోగించాలో మరియు మీ విభిన్న హార్డ్‌వేర్ పరికరాలలో E2E పరిష్కారాలను ఎలా నిర్మించాలో మీరు తెలుసుకోవచ్చు. Phiని స్వయంగా అనుభవించడానికి, మోడల్స్‌తో ఆడటం మొదలుపెట్టి మీ సందర్భాల కోసం Phiను అనుకూలీకరించటానికి [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai)ను ఉపయోగించండి మీరు Getting Started with [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) వద్ద మరిన్ని వివరాలు తెలుసుకోవచ్చు

**ప్లేగ್ರౌండ్**
ప్రతి మోడల్‌కు ఆ మోడల్‌ను పరీక్షించడానికి ప్రత్యేక ప్లేగ్రౌండ్ ఉంది [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub మోడల్స్‌లో Phi

Microsoft Phiని ఎలా ఉపయోగించాలో మరియు మీ విభిన్న హార్డ్‌వేర్ పరికరాలలో E2E పరిష్కారాలను ఎలా నిర్మించాలో మీరు తెలుసుకోవచ్చు. Phiను స్వయంగా అనుభవించడానికి, మొదట మోడల్‌తో ఆడటం మరియు మీ సందర్భాల కోసం Phiను అనుకూలీకరించటం ప్రారంభించండి, [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo)ను ఉపయోగించండి మీరు Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) వద్ద మరిన్ని వివరాలు తెలుసుకోవచ్చు

**ప్లేగ్రౌండ్**
ప్రతి మోడల్‌కు పరీక్షించేందుకు ప్రత్యేక [ప్లేగ్రౌండ్ to test the model](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Hugging Faceలో Phi

మీరు మోడల్‌ను [Hugging Face](https://huggingface.co/microsoft) లో కూడా కనుగొనవచ్చు

**ప్లేగ్రౌండ్**
 [Hugging Chat ప్లేగ్రౌండ్](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 ఇతర కోర్సులు

మన బృందం మరిన్ని కోర్సులను తయారు చేస్తోంది! వీటిని చూడండి:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j ప్రారంభకులకు](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js ప్రారంభకులకు](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD ప్రారంభకులకు](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI ప్రారంభకులకు](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP ప్రారంభకులకు](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents ప్రారంభకులకు](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![జనరేటివ్ AI ప్రారంభకులకు](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![జనరేటివ్ AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![జనరేటివ్ AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![జనరేటివ్ AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### ముఖ్య అభ్యాసం
[![ML ప్రారంభకులకు](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![డేటా సైన్స్ ప్రారంభకులకు](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI ప్రారంభకులకు](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![సైబర్‌సెక్యూరిటీ ప్రారంభకులకు](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![వెబ్ డెవ్ ప్రారంభకులకు](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT ప్రారంభకులకు](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR డెవలప్‌మెంట్ ప్రారంభకులకు](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot సిరీస్
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## బాధ్యతాయుత AI 

Microsoft మా కస్టమర్‌లు మా AI ఉత్పత్తులను బాధ్యతాయుతంగా ఉపయోగించుకునేలా సహాయపడటానికి, మా అనుభవాలను పంచుకోవడానికి, మరియు Transparency Notes మరియు Impact Assessments వంటి సాధనాల ద్వారా నమ్మకంపై ఆధారపడిన భాగస్వామ్యాలను నిర్మించుకోవడానికి అంకితం అయ్యింది. ఈ వనరులలో అనేకం [https://aka.ms/RAI](https://aka.ms/RAI) వద్ద అందుబాటులో ఉన్నాయి.
Microsoft యొక్క బాధ్యతాయుత AI దృష్టికోణం న్యాయత్వం, నమ్మకదారితనం మరియు భద్రత, గోప్యత మరియు భద్రత, సమగ్రత, పారదర్శకత మరియు బాధ్యత వంటి మా AI స 원 놓శల మీద ఆధారపడి ఉంది.

ఈ నమూనాల్లో ఉపయోగించినట్లు పెద్ద ఎత్తు సహజ భాష, చిత్రం, మరియు శ్రవణ నమూనాలు అన్యాయమైన, అనిశ్చితమైన లేదా అపకారకంగా ప్రవర్తించవచ్చు, ఫలితంగా హానికరమైన ప్రభావాలు కలిగే అవకాశము ఉంది. రిస్కులు మరియు పరిమితుల గురించి సమాచారం కోసం దయచేసి [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) చూడండి.

ఈ రిస్కులను తగ్గించేందుకు సూచించబడిన దృష్టికోణం మీ ఆర్కిటెక్టర్‌లో హానికర ప్రవర్తనను గుర్తించి నిరోధించే ఒక సేఫ్టీ సిస్టమ్‌ను చేర్చడం. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) అనేది అప్లికేషన్లు మరియు సేవలలో వినియోగదారు ఉత్పత్తి చేసిన మరియు AI ఉత్పత్తి చేసిన హానికర కంటెంట్‌ను గుర్తించగల స్వతంత్ర రక్షణ పొరను అందిస్తుంది. Azure AI Content Safetyలో మీరు హానికరమైన విషయాన్ని గుర్తించే టెక్స్ట్ మరియు ఇమేజ్ API లను పొందవచ్చు. Azure AI Foundryలో, Content Safety సేవ మీకు విభిన్న మోడాలిటీలపై హానికర కంటెంట్‌ను గుర్తించడానికి నమూనా కోడ్‌ను వీక్షించడానికి, అన్వేషించడానికి మరియు ప్రయోగించడానికి అనుమతిస్తుంది. క్రింది [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) మీరు సేవకు ఎలా అభ్యర్థనలు పంపాలో మార్గనిర్దేశిస్తుంది.

ఇంక另一 అంశం మొత్తం అప్లికేషన్ పనితీరు. బహు-మోడల్ మరియు బహు-మోడాలిటీ అప్లికేషన్లలో, పనితీరు అంటే సిస్టమ్ మీకు మరియు మీ వినియోగదారులకు ఆశించిన విధంగా పని చేయడం, హానికరమైన అవుట్‌పుట్‌ను ఉత్పత్తి చేయకపోవడం కూడా. మీ మొత్తం అప్లికేషన్ పనితీరును మూల్యాంకించటం ముఖ్యము — దీని కోసం [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) చూడండి. మీరు 또한 [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) తో కస్టమ్‌గా రూపొందించి మూల్యాంకించవచ్చు.

మీరు మీ అభివృద్ధి పరిసరాలలోని AI అప్లికేషన్‌ను [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ఉపయోగించి మూల్యాంకించవచ్చు. ఒక టెస్ట్ డేటాసెట్ లేదా లక్ష్యాన్ని ఇచ్చినప్పుడు, మీ జనరేటివ్ AI అప్లికేషన్ ఉత్పత్తులను బిల్ట్-ఇన్ ఎవాల్యుయేటర్లు లేదా మీ ఎంపికలోని కస్టమ్ ఎవాల్యుయేటర్లు తో గణితాత్మకంగా కొలుస్తారు. మీ సిస్టమ్‌ను మూల్యాంకించడానికి azure ai evaluation sdk తో ప్రారంభించాలంటే మీరు [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) అనుసరించవచ్చు. మీరు ఒక ఎవాల్యుయేషన్ రన్‌ను అమలు చేసిన తర్వాత, మీరు [Azure AI Foundryలో ఫలితాలను విజువలైజ్](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) చేయవచ్చు. 

## ట్రేడ్‌మార్క్లు
ఈ ప్రాజెక్ట్‌లో ప్రాజెక్టులు, ఉత్పత్తులు లేదా సేవలకు సంబంధించిన ట్రేడ్‌మార్క్‌లు లేదా లోగోలు ఉండవచ్చు. Microsoft ట్రేడ్‌మార్క్‌లు లేదా లోగోల వినియోగానికి అనుమతి ఈ క్రింది [Microsoft యొక్క ట్రేడ్‌మార్క్ & బ్రాండ్ మార్గదర్శకాలు](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) కు అనుగుణంగా ఉండాలి మరియు వాటిని పాటించాలి.
ఈ ప్రాజెక్ట్‌ యొక్క మార్చబడిన సంస్కరణల్లో Microsoft ట్రేడ్‌మార్క్‌లు లేదా లోగోలు ఉపయోగించడం అయోమయం సృష్టించకూడదు లేదా Microsoft స్పాన్సర్‌షిప్ ఉందంటూ భావింపబడకూడదు. మూడవ పక్షాల ట్రేడ్‌మార్క్‌లు లేదా లోగోల ఏమైనా వినియోగం ఆ మూడవ పక్షాల విధానాలకు దిగ్బంధితం.

## సహాయం పొందడం

If you get stuck or have any questions about building AI apps, join:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

If you have product feedback or errors while building visit:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ:
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించాము. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, స్వయంచాలక అనువాదాల్లో పొరపాట్లు లేదా అచూకీ తప్పిదాలు ఉండే అవకాశం ఉందని దయచేసి గమనించండి. మూల పత్రాన్ని దాని మాతృభాషలోనే అధికారిక వనరుగా పరిగణించాలి. కీలకమైన సమాచారం కోసం వృత్తిపరులచే చేయబడిన మానవ అనువాదాన్ని సిఫార్సు చేస్తున్నాము. ఈ అనువాదం వాడకాన్ని పొంచి జరిగిన ఏ అపార్థాలు లేదా తప్పుగా అర్థం చేసుకోవడంపై మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->