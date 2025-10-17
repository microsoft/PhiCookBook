<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4987daf30687ad3850757c9eae3f5411",
  "translation_date": "2025-10-17T10:43:21+00:00",
  "source_file": "README.md",
  "language_code": "ta"
}
-->
# Phi சமையல் புத்தகம்: மைக்ரோசாஃப்ட் Phi மாதிரிகளுடன் செயல்பட உதவும் உதாரணங்கள்

[![GitHub Codespaces-ல் மாதிரிகளை திறந்து பயன்படுத்தவும்](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers-ல் திறக்கவும்](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub பங்களிப்பாளர்கள்](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub பிரச்சினைகள்](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs வரவேற்கப்படுகின்றன](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub பார்வையாளர்கள்](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi என்பது மைக்ரோசாஃப்ட் உருவாக்கிய திறந்த மூல AI மாதிரிகளின் தொடர் ஆகும்.

Phi தற்போது மிகவும் சக்திவாய்ந்த மற்றும் செலவுசெய்யக்கூடிய சிறிய மொழி மாதிரி (SLM) ஆகும், இது பல மொழிகள், காரணம், உரை/அரட்டை உருவாக்கம், குறியீடு, படங்கள், ஆடியோ மற்றும் பிற சூழல்களில் சிறந்த தரவுகளை வழங்குகிறது.

Phi-யை கிளவுட் அல்லது எட்ஜ் சாதனங்களில் நிறுவலாம், மேலும் குறைந்த கணினி சக்தியுடன் உருவாக்கும் AI பயன்பாடுகளை எளிதாக உருவாக்கலாம்.

இந்த வளங்களை பயன்படுத்த தொடங்க இந்த படிகளை பின்பற்றவும்:
1. **களஞ்சியத்தை Fork செய்யவும்**: கிளிக் செய்யவும் [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **களஞ்சியத்தை Clone செய்யவும்**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord சமூகத்தில் சேர்ந்து நிபுணர்களையும் மற்ற டெவலப்பர்களையும் சந்திக்கவும்**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![கவர்](../../imgs/cover.png)

### 🌐 பல மொழி ஆதரவு

#### GitHub Action மூலம் ஆதரிக்கப்படுகிறது (தானியங்கி மற்றும் எப்போதும் புதுப்பிக்கப்பட்டது)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[அரபு](../ar/README.md) | [பெங்காலி](../bn/README.md) | [புல்கேரியன்](../bg/README.md) | [பர்மீஸ் (மியான்மர்)](../my/README.md) | [சீனம் (எளிமைப்படுத்தப்பட்டது)](../zh/README.md) | [சீனம் (சம்பிரதாய, ஹாங்காங்)](../hk/README.md) | [சீனம் (சம்பிரதாய, மக்காவு)](../mo/README.md) | [சீனம் (சம்பிரதாய, தைவான்)](../tw/README.md) | [குரோஷியன்](../hr/README.md) | [செக்](../cs/README.md) | [டேனிஷ்](../da/README.md) | [டச்சு](../nl/README.md) | [எஸ்டோனியன்](../et/README.md) | [பின்னிஷ்](../fi/README.md) | [பிரெஞ்சு](../fr/README.md) | [ஜெர்மன்](../de/README.md) | [கிரேக்கம்](../el/README.md) | [ஹீப்ரு](../he/README.md) | [இந்தி](../hi/README.md) | [ஹங்கேரியன்](../hu/README.md) | [இந்தோனேஷியன்](../id/README.md) | [இத்தாலியன்](../it/README.md) | [ஜப்பானியன்](../ja/README.md) | [கொரியன்](../ko/README.md) | [லிதுவேனியன்](../lt/README.md) | [மலாய்](../ms/README.md) | [மராத்தி](../mr/README.md) | [நேபாளி](../ne/README.md) | [நார்வேஜியன்](../no/README.md) | [பெர்ஷியன் (பார்ஸி)](../fa/README.md) | [போலிஷ்](../pl/README.md) | [போர்ச்சுகீஸ் (பிரேசில்)](../br/README.md) | [போர்ச்சுகீஸ் (போர்ச்சுகல்)](../pt/README.md) | [பஞ்சாபி (குர்முகி)](../pa/README.md) | [ரோமானியன்](../ro/README.md) | [ரஷியன்](../ru/README.md) | [செர்பியன் (சிரிலிக்)](../sr/README.md) | [ஸ்லோவாக்](../sk/README.md) | [ஸ்லோவேனியன்](../sl/README.md) | [ஸ்பானிஷ்](../es/README.md) | [ஸ்வாஹிலி](../sw/README.md) | [ஸ்வீடிஷ்](../sv/README.md) | [டாகாலோக் (பிலிப்பினோ)](../tl/README.md) | [தமிழ்](./README.md) | [தாய்](../th/README.md) | [துருக்கியம்](../tr/README.md) | [உக்ரேனியன்](../uk/README.md) | [உருது](../ur/README.md) | [வியட்நாமியன்](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## உள்ளடக்க அட்டவணை

- அறிமுகம்
  - [Phi குடும்பத்திற்கு வரவேற்கிறோம்](./md/01.Introduction/01/01.PhiFamily.md)
  - [உங்கள் சூழலை அமைத்தல்](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [முக்கிய தொழில்நுட்பங்களை புரிந்துகொள்வது](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi மாதிரிகளுக்கான AI பாதுகாப்பு](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ஹார்ட்வேரின் ஆதரவு](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi மாதிரிகள் & பல்வேறு தளங்களில் கிடைக்கும் நிலை](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai மற்றும் Phi-யை பயன்படுத்துதல்](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace Models](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- பல்வேறு சூழல்களில் Phi-யை Inference செய்யுதல்
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub Models](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi குடும்பத்தை Inference செய்யுதல்
    - [iOS-ல் Phi-யை Inference செய்யுதல்](./md/01.Introduction/03/iOS_Inference.md)
    - [Android-ல் Phi-யை Inference செய்யுதல்](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson-ல் Phi-யை Inference செய்யுதல்](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC-ல் Phi-யை Inference செய்யுதல்](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework-ஐ பயன்படுத்தி Phi-யை Inference செய்யுதல்](./md/01.Introduction/03/MLX_Inference.md)
    - [Local Server-ல் Phi-யை Inference செய்யுதல்](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit-ஐ Remote Server-ல் பயன்படுத்தி Phi-யை Inference செய்யுதல்](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust-ஐ பயன்படுத்தி Phi-யை Inference செய்யுதல்](./md/01.Introduction/03/Rust_Inference.md)
    - [Local-ல் Phi--Vision-ஐ Inference செய்யுதல்](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (அதிகாரப்பூர்வ ஆதரவு)-ஐ பயன்படுத்தி Phi-யை Inference செய்யுதல்](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi குடும்பத்தை Quantify செய்யுதல்](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp-ஐ பயன்படுத்தி Phi-3.5 / 4-ஐ Quantize செய்யுதல்](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime-க்கு Generative AI extensions-ஐ பயன்படுத்தி Phi-3.5 / 4-ஐ Quantize செய்யுதல்](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO-ஐ பயன்படுத்தி Phi-3.5 / 4-ஐ Quantize செய்யுதல்](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework-ஐ பயன்படுத்தி Phi-3.5 / 4-ஐ Quantize செய்யுதல்](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi-யை மதிப்பீடு செய்யுதல்
    - [AI பதில்கள்](./md/01.Introduction/05/ResponsibleAI.md)
    - [மதிப்பீட்டுக்கான Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow-ஐ பயன்படுத்தி மதிப்பீடு செய்யுதல்](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search உடன் RAG
    - [Azure AI Search உடன் Phi-4-mini மற்றும் Phi-4-multimodal (RAG)-ஐ எப்படி பயன்படுத்துவது](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi பயன்பாட்டு மேம்பாட்டு மாதிரிகள்
  - உரை & அரட்டை பயன்பாடுகள்
    - Phi-4 மாதிரிகள் 🆕
      - [📓] [Phi-4-mini ONNX Model உடன் அரட்டை செய்யுங்கள்](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 local ONNX Model .NET உடன் அரட்டை செய்யுங்கள்](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel-ஐ பயன்படுத்தி Phi-4 ONNX உடன் .NET Console App-ல் அரட்டை செய்யுங்கள்](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 மாதிரிகள்
      - [Phi3, ONNX Runtime Web மற்றும் WebGPU-ஐ பயன்படுத்தி உலாவியில் உள்ள உள்ளூர் Chatbot](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - Phi-3-mini மற்றும் OpenAI Whisper-ஐ இணைத்து செயல்படுத்துதல்](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ஒரு wrapper உருவாக்கி Phi-3-ஐ MLFlow உடன் பயன்படுத்துதல்](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Model Optimization - Olive-ஐ பயன்படுத்தி ONNX Runtime Web-க்கு Phi-3-min மாதிரியை எப்படி மேம்படுத்துவது](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [WinUI3 பயன்பாட்டுடன் Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [WinUI3 பல மாதிரி AI இயக்கப்படும் குறிப்புகள் பயன்பாட்டின் மாதிரி](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Prompt flow உடன் தனிப்பயன் Phi-3 மாதிரிகளை Fine-tune மற்றும் ஒருங்கிணைப்பு செய்ய](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Azure AI Foundry இல் Prompt flow உடன் தனிப்பயன் Phi-3 மாதிரிகளை Fine-tune மற்றும் ஒருங்கிணைப்பு செய்ய](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Microsoft இன் பொறுப்பான AI கொள்கைகளில் கவனம் செலுத்தி Azure AI Foundry இல் Fine-tuned Phi-3 / Phi-3.5 மாதிரியை மதிப்பீடு செய்ய](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct மொழி கணிப்பு மாதிரி (சீனம்/ஆங்கிலம்)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU பயன்படுத்தி Phi-3.5-Instruct ONNX உடன் Prompt flow தீர்வை உருவாக்க](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tflite பயன்படுத்தி Android பயன்பாட்டை உருவாக்க](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Microsoft.ML.OnnxRuntime பயன்படுத்தி உள்ளூர் ONNX Phi-3 மாதிரியை கொண்டு Q&A .NET எடுத்துக்காட்டு](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Semantic Kernel மற்றும் Phi-3 உடன் Console chat .NET பயன்பாடு](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK குறியீடு அடிப்படையிலான மாதிரிகள்  
  - Phi-4 மாதிரிகள் 🆕  
    - [📓] [Phi-4-multimodal பயன்படுத்தி திட்டக் குறியீட்டை உருவாக்க](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Phi-3 / 3.5 மாதிரிகள்  
    - [Microsoft Phi-3 குடும்பத்துடன் உங்கள் சொந்த Visual Studio Code GitHub Copilot Chat ஐ உருவாக்க](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [GitHub மாதிரிகள் மூலம் Phi-3.5 உடன் உங்கள் சொந்த Visual Studio Code Chat Copilot முகவரியை உருவாக்க](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- மேம்பட்ட காரணமறிதல் மாதிரிகள்  
  - Phi-4 மாதிரிகள் 🆕  
    - [📓] [Phi-4-mini-reasoning அல்லது Phi-4-reasoning மாதிரிகள்](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Microsoft Olive உடன் Phi-4-mini-reasoning Fine-tuning செய்ய](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Apple MLX உடன் Phi-4-mini-reasoning Fine-tuning செய்ய](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [GitHub மாதிரிகளுடன் Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Azure AI Foundry மாதிரிகளுடன் Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- டெமோக்கள்  
    - [Hugging Face Spaces இல் Phi-4-mini டெமோக்கள்](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Hugging Face Spaces இல் Phi-4-multimodal டெமோக்கள்](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- பார்வை மாதிரிகள்  
  - Phi-4 மாதிரிகள் 🆕  
    - [📓] [Phi-4-multimodal பயன்படுத்தி படங்களை வாசித்து குறியீட்டை உருவாக்க](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Phi-3 / 3.5 மாதிரிகள்  
    - [📓][Phi-3-vision-பட எழுத்து முதல் எழுத்து வரை](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP எம்பெட்டிங்](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [டெமோ: Phi-3 மறுசுழற்சி](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - பார்வை மொழி உதவியாளர் - Phi3-Vision மற்றும் OpenVINO உடன்](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision பல-சட்டம் அல்லது பல-பட மாதிரி](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Microsoft.ML.OnnxRuntime .NET பயன்படுத்தி உள்ளூர் ONNX மாதிரியை கொண்ட Phi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Microsoft.ML.OnnxRuntime .NET பயன்படுத்தி மெனு அடிப்படையிலான Phi-3 Vision உள்ளூர் ONNX மாதிரி](../../md/04.HOL/dotnet/src/LabsPhi304)  

- கணித மாதிரிகள்  
  - Phi-4-Mini-Flash-Reasoning-Instruct மாதிரிகள் 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct உடன் கணித டெமோ](../../md/02.Application/09.Math/MathDemo.ipynb)  

- ஒலி மாதிரிகள்  
  - Phi-4 மாதிரிகள் 🆕  
    - [📓] [Phi-4-multimodal பயன்படுத்தி ஒலி உரைகளை எடுக்க](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Phi-4-multimodal ஒலி மாதிரி](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Phi-4-multimodal பேச்சு மொழிபெயர்ப்பு மாதிரி](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [.NET console பயன்பாட்டை பயன்படுத்தி Phi-4-multimodal ஒலியை பகுப்பாய்வு செய்து உரையை உருவாக்க](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- MOE மாதிரிகள்  
  - Phi-3 / 3.5 மாதிரிகள்  
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) சமூக ஊடக மாதிரி](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, மற்றும் LlamaIndex உடன் Retrieval-Augmented Generation (RAG) குழாய்களை உருவாக்க](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- செயல்பாட்டு அழைப்பு மாதிரிகள்  
  - Phi-4 மாதிரிகள் 🆕  
    - [📓] [Phi-4-mini உடன் செயல்பாட்டு அழைப்பை பயன்படுத்த](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Phi-4-mini உடன் பல முகவரிகளை உருவாக்க செயல்பாட்டு அழைப்பை பயன்படுத்த](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Ollama உடன் செயல்பாட்டு அழைப்பை பயன்படுத்த](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [ONNX உடன் செயல்பாட்டு அழைப்பை பயன்படுத்த](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- பல்முக கலவை மாதிரிகள்  
  - Phi-4 மாதிரிகள் 🆕  
    - [📓] [தொழில்நுட்ப பத்திரிகையாளராக Phi-4-multimodal ஐ பயன்படுத்த](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [.NET console பயன்பாட்டை பயன்படுத்தி Phi-4-multimodal மூலம் படங்களை பகுப்பாய்வு செய்ய](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Phi மாதிரிகளை Fine-tuning  
  - [Fine-tuning சூழல்கள்](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [Fine-tuning vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Phi-3 ஐ தொழில்துறை நிபுணராக மாற்ற Fine-tuning செய்ய](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [VS Code க்கான AI கருவி தொகுப்புடன் Phi-3 ஐ Fine-tuning செய்ய](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Azure Machine Learning சேவையுடன் Phi-3 ஐ Fine-tuning செய்ய](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Lora உடன் Phi-3 ஐ Fine-tuning செய்ய](./md/03.FineTuning/FineTuning_Lora.md)  
  - [QLora உடன் Phi-3 ஐ Fine-tuning செய்ய](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Azure AI Foundry உடன் Phi-3 ஐ Fine-tuning செய்ய](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Azure ML CLI/SDK உடன் Phi-3 ஐ Fine-tuning செய்ய](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Microsoft Olive உடன் Fine-tuning செய்ய](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Microsoft Olive கையேடு ஆய்வகத்துடன் Fine-tuning செய்ய](./md/03.FineTuning/olive-lab/readme.md)  
  - [Weights and Bias உடன் Phi-3-vision ஐ Fine-tuning செய்ய](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Apple MLX Framework உடன் Phi-3 ஐ Fine-tuning செய்ய](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Phi-3-vision ஐ Fine-tuning செய்ய (அதிகாரப்பூர்வ ஆதரவு)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Kaito AKS, Azure Containers உடன் Phi-3 ஐ Fine-tuning செய்ய (அதிகாரப்பூர்வ ஆதரவு)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Phi-3 மற்றும் 3.5 Vision ஐ Fine-tuning செய்ய](https://github.com/2U1/Phi3-Vision-Finetune)  

- கையேடு ஆய்வகங்கள்  
  - [முன்னணி மாதிரிகளை ஆராய்வது: LLMs, SLMs, உள்ளூர் மேம்பாடு மற்றும் பல](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [NLP திறனை திறக்க: Microsoft Olive உடன் Fine-Tuning செய்ய](https://github.com/azure/Ignite_FineTuning_workshop)  

- கல்வி ஆராய்ச்சி கட்டுரைகள் மற்றும் வெளியீடுகள்  
  - [Textbooks Are All You Need II: phi-1.5 தொழில்நுட்ப அறிக்கை](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 தொழில்நுட்ப அறிக்கை: உங்கள் தொலைபேசியில் உள்ளூர் அளவில் திறமையான மொழி மாதிரி](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 தொழில்நுட்ப அறிக்கை](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini தொழில்நுட்ப அறிக்கை: Mixture-of-LoRAs மூலம் சுருக்கமான ஆனால் சக்திவாய்ந்த பல்முக மொழி மாதிரிகள்](https://arxiv.org/abs/2503.01743)  
  - [வாகனத்திற்குள் செயல்பாடுகளை அழைக்கும் சிறிய மொழி மாதிரிகளை மேம்படுத்துதல்](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) பல தேர்வு கேள்விகளுக்கான பதிலளிக்க PHI-3-ஐ நன்றாக அமைத்தல்: முறை, முடிவுகள் மற்றும் சவால்கள்](https://arxiv.org/abs/2501.01588)
  - [Phi-4-காரணம் தொழில்நுட்ப அறிக்கை](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-காரணம் தொழில்நுட்ப அறிக்கை](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi மாதிரிகளை பயன்படுத்துதல்

### Azure AI Foundry-ல் Phi

Microsoft Phi-ஐ எப்படி பயன்படுத்துவது மற்றும் உங்கள் பல்வேறு ஹார்ட்வேரில் E2E தீர்வுகளை உருவாக்குவது பற்றி நீங்கள் அறியலாம். Phi-ஐ நேரடியாக அனுபவிக்க, மாதிரிகளை சோதித்து உங்கள் சூழல்களுக்கு ஏற்ப Phi-ஐ தனிப்பயனாக்குவதன் மூலம் தொடங்குங்கள். [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) மூலம் மேலும் அறியலாம். [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) பற்றிய தொடக்க வழிகாட்டுதலில் மேலும் அறியலாம்.

**Playground**
ஒவ்வொரு மாதிரிக்கும் மாதிரி சோதிக்க தனிப்பட்ட இடம் உள்ளது [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub Models-ல் Phi

Microsoft Phi-ஐ எப்படி பயன்படுத்துவது மற்றும் உங்கள் பல்வேறு ஹார்ட்வேரில் E2E தீர்வுகளை உருவாக்குவது பற்றி நீங்கள் அறியலாம். Phi-ஐ நேரடியாக அனுபவிக்க, மாதிரியை சோதித்து உங்கள் சூழல்களுக்கு ஏற்ப Phi-ஐ தனிப்பயனாக்குவதன் மூலம் தொடங்குங்கள். [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) மூலம் மேலும் அறியலாம். [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) பற்றிய தொடக்க வழிகாட்டுதலில் மேலும் அறியலாம்.

**Playground**
ஒவ்வொரு மாதிரிக்கும் தனிப்பட்ட [மாதிரி சோதிக்க இடம்](/md/02.QuickStart/GitHubModel_QuickStart.md) உள்ளது.

### Hugging Face-ல் Phi

மாதிரியை [Hugging Face](https://huggingface.co/microsoft) இல் காணலாம்.

**Playground**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## பொறுப்பான AI 

Microsoft எங்கள் AI தயாரிப்புகளை பொறுப்புடன் பயன்படுத்துவதற்கு எங்கள் வாடிக்கையாளர்களுக்கு உதவ, எங்கள் அனுபவங்களை பகிர்ந்து, மற்றும் நம்பகத்தன்மை அடிப்படையிலான கூட்டாண்மைகளை உருவாக்க உறுதியாக உள்ளது. Transparency Notes மற்றும் Impact Assessments போன்ற கருவிகள் மூலம் இது செய்யப்படுகிறது. இந்த வளங்கள் பலவற்றை [https://aka.ms/RAI](https://aka.ms/RAI) இல் காணலாம். 
Microsoft-இன் பொறுப்பான AI அணுகுமுறை நியாயம், நம்பகத்தன்மை மற்றும் பாதுகாப்பு, தனியுரிமை மற்றும் பாதுகாப்பு, உள்ளடக்கம், வெளிப்படைத்தன்மை மற்றும் பொறுப்புத்தன்மை ஆகிய AI கொள்கைகளில் அடிப்படையாக உள்ளது.

பெரிய அளவிலான இயற்கை மொழி, படம் மற்றும் பேச்சு மாதிரிகள் - இந்த மாதிரிகள் போன்றவை - சில நேரங்களில் நியாயமற்ற, நம்பகமற்ற அல்லது ஆபத்தான முறையில் செயல்படலாம், இது பாதிப்புகளை ஏற்படுத்தும். [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ஐ அணுகி அபாயங்கள் மற்றும் வரம்புகள் பற்றி அறியவும்.

இந்த அபாயங்களை குறைக்க பரிந்துரைக்கப்படும் அணுகுமுறை உங்கள் கட்டமைப்பில் ஒரு பாதுகாப்பு அமைப்பை சேர்ப்பது, இது ஆபத்தான செயல்பாடுகளை கண்டறிந்து தடுக்க முடியும். [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ஒரு சுயாதீன பாதுகாப்பு அடுக்கு வழங்குகிறது, இது பயன்பாடுகள் மற்றும் சேவைகளில் பயனர் உருவாக்கிய மற்றும் AI உருவாக்கிய ஆபத்தான உள்ளடக்கத்தை கண்டறிய முடியும். Azure AI Content Safety-ல் உள்ள உரை மற்றும் பட APIகள் ஆபத்தான உள்ளடக்கத்தை கண்டறிய உதவுகின்றன. Azure AI Foundry-இல், Content Safety சேவை பல்வேறு முறைகளில் ஆபத்தான உள்ளடக்கத்தை கண்டறிய மாதிரிக் குறியீடுகளை பார்க்க, ஆராய மற்றும் சோதிக்க அனுமதிக்கிறது. [துரித வழிகாட்டுதல் ஆவணம்](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) சேவைக்கு கோரிக்கைகளை செய்ய வழிகாட்டுகிறது.

மற்றொரு முக்கிய அம்சம், மொத்த பயன்பாட்டு செயல்திறனை கருத்தில் கொள்ள வேண்டும். பல்வேறு முறை மற்றும் பல மாதிரிகள் கொண்ட பயன்பாடுகளில், செயல்திறன் என்பது உங்கள் மற்றும் உங்கள் பயனாளர்கள் எதிர்பார்ப்பதற்கேற்ப செயல்பட வேண்டும், அதில் ஆபத்தான வெளியீடுகளை உருவாக்காமல் இருக்க வேண்டும். உங்கள் மொத்த பயன்பாட்டின் செயல்திறனை [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) மூலம் மதிப்பீடு செய்ய முக்கியம். [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) உருவாக்கவும் மதிப்பீடு செய்யவும் நீங்கள் முடியும்.

உங்கள் AI பயன்பாட்டை உங்கள் மேம்பாட்டு சூழலில் [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) மூலம் மதிப்பீடு செய்யலாம். சோதனை தரவுத்தொகுப்பு அல்லது இலக்கு எதுவாக இருந்தாலும், உங்கள் உருவாக்கும் AI பயன்பாட்டின் உருவாக்கங்கள் உங்கள் தேர்வின் அடிப்படையில் உள்ளமைக்கப்பட்ட மதிப்பீட்டாளர்கள் அல்லது தனிப்பயன் மதிப்பீட்டாளர்களுடன் அளவிடப்படும். உங்கள் அமைப்பை மதிப்பீடு செய்ய azure ai evaluation sdk-ஐ பயன்படுத்த தொடங்க, [துரித வழிகாட்டி](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ஐ பின்பற்றலாம். ஒரு மதிப்பீட்டு இயக்கத்தை செயல்படுத்திய பிறகு, [Azure AI Foundry-இல் முடிவுகளை காட்சிப்படுத்தலாம்](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## வர்த்தக முத்திரைகள்

இந்த திட்டத்தில் திட்டங்கள், தயாரிப்புகள் அல்லது சேவைகளுக்கான வர்த்தக முத்திரைகள் அல்லது லோகோக்கள் இருக்கலாம். Microsoft வர்த்தக முத்திரைகள் அல்லது லோகோக்களை அனுமதிக்கப்பட்ட முறையில் பயன்படுத்த Microsoft-இன் [Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ஐ பின்பற்ற வேண்டும்.
Microsoft வர்த்தக முத்திரைகள் அல்லது லோகோக்களை மாற்றியமைக்கப்பட்ட பதிப்புகளில் பயன்படுத்துவது குழப்பத்தை ஏற்படுத்தக்கூடாது அல்லது Microsoft ஆதரவை குறிக்கக்கூடாது. மூன்றாம் தரப்பு வர்த்தக முத்திரைகள் அல்லது லோகோக்களை பயன்படுத்துவது அந்த மூன்றாம் தரப்பின் கொள்கைகளுக்கு உட்பட்டது.

## உதவி பெறுதல்

AI பயன்பாடுகளை உருவாக்குவதில் சிக்கலாக இருந்தால் அல்லது கேள்விகள் இருந்தால், இணைந்திடுங்கள்:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

தயாரிப்பு கருத்துகள் அல்லது பிழைகள் இருந்தால், பார்வையிடுங்கள்:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.