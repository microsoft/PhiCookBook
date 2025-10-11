<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a73c59eecd7ad4ec494fd4333a29e208",
  "translation_date": "2025-10-11T11:30:19+00:00",
  "source_file": "README.md",
  "language_code": "ta"
}
-->
# Phi குக்க்புக்: மைக்ரோசாஃப்ட் Phi மாடல்களுடன் கைகூலி உதாரணங்கள்

[![GitHub Codespaces-ல் உதாரணங்களை திறந்து பயன்படுத்தவும்](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers-ல் திறக்கவும்](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub பங்களிப்பாளர்கள்](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub பிரச்சினைகள்](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs வரவேற்கப்படுகின்றன](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi என்பது மைக்ரோசாஃப்ட் உருவாக்கிய ஓர் திறந்த மூல AI மாடல்களின் தொடர் ஆகும்.

Phi தற்போது மிகவும் சக்திவாய்ந்த மற்றும் செலவுச்செலவான சிறிய மொழி மாடல் (SLM) ஆகும், இது பல மொழிகள், காரணம் கூறுதல், உரை/அரட்டை உருவாக்கம், குறியீடு, படங்கள், ஆடியோ மற்றும் பிற சூழல்களில் சிறந்த அளவீடுகளை கொண்டுள்ளது.

Phi-ஐ மேகத்தில் அல்லது எட்ஜ் சாதனங்களில் நிறுவலாம், மேலும் குறைந்த கணினி சக்தியுடன் உருவாக்கும் AI பயன்பாடுகளை எளிதாக உருவாக்கலாம்.

இந்த வளங்களைப் பயன்படுத்தத் தொடங்க இந்த படிகளைப் பின்பற்றவும்:
1. **கிடையலாக்கவும்**: [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo) கிளிக் செய்யவும்.
2. **கிளோன் செய்யவும்**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord சமூகத்தில் சேர்ந்து நிபுணர்களையும் மற்ற டெவலப்பர்களையும் சந்திக்கவும்**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 பல மொழி ஆதரவு

#### GitHub Action மூலம் ஆதரிக்கப்படுகிறது (தானியங்கி மற்றும் எப்போதும் புதுப்பிக்கப்பட்டது)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[அரபு](../ar/README.md) | [பெங்காலி](../bn/README.md) | [பல்கேரியன்](../bg/README.md) | [பர்மீஸ் (மியான்மர்)](../my/README.md) | [சீனம் (எளிமைப்படுத்தப்பட்டது)](../zh/README.md) | [சீனம் (பாரம்பரிய, ஹாங்காங்)](../hk/README.md) | [சீனம் (பாரம்பரிய, மக்காவ்)](../mo/README.md) | [சீனம் (பாரம்பரிய, தைவான்)](../tw/README.md) | [குரோஷியன்](../hr/README.md) | [செக்](../cs/README.md) | [டேனிஷ்](../da/README.md) | [டச்சு](../nl/README.md) | [எஸ்டோனியன்](../et/README.md) | [பின்னிஷ்](../fi/README.md) | [பிரெஞ்சு](../fr/README.md) | [ஜெர்மன்](../de/README.md) | [கிரேக்கம்](../el/README.md) | [ஹீப்ரூ](../he/README.md) | [இந்தி](../hi/README.md) | [ஹங்கேரியன்](../hu/README.md) | [இந்தோனேஷியன்](../id/README.md) | [இத்தாலியன்](../it/README.md) | [ஜப்பானீஸ்](../ja/README.md) | [கொரியன்](../ko/README.md) | [லிதுவேனியன்](../lt/README.md) | [மலாய்](../ms/README.md) | [மராத்தி](../mr/README.md) | [நேபாளி](../ne/README.md) | [நார்வேஜியன்](../no/README.md) | [பாரசீக (பார்ஸி)](../fa/README.md) | [போலிஷ்](../pl/README.md) | [போர்ச்சுகீஸ் (பிரேசில்)](../br/README.md) | [போர்ச்சுகீஸ் (போர்ச்சுகல்)](../pt/README.md) | [பஞ்சாபி (குர்முகி)](../pa/README.md) | [ரோமானியன்](../ro/README.md) | [ரஷ்யன்](../ru/README.md) | [செர்பியன் (சிரிலிக்)](../sr/README.md) | [ஸ்லோவாக்](../sk/README.md) | [ஸ்லோவேனியன்](../sl/README.md) | [ஸ்பானிஷ்](../es/README.md) | [சுவாஹிலி](../sw/README.md) | [ஸ்வீடிஷ்](../sv/README.md) | [டகாலோக் (பிலிப்பைனோ)](../tl/README.md) | [தமிழ்](./README.md) | [தாய்](../th/README.md) | [துருக்கி](../tr/README.md) | [உக்ரைனியன்](../uk/README.md) | [உருது](../ur/README.md) | [வியட்நாமீஸ்](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## உள்ளடக்க அட்டவணை

- அறிமுகம்
  - [Phi குடும்பத்திற்கு வரவேற்கிறோம்](./md/01.Introduction/01/01.PhiFamily.md)
  - [உங்கள் சூழலை அமைத்தல்](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [முக்கிய தொழில்நுட்பங்களைப் புரிந்துகொள்வது](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi மாடல்களுக்கு AI பாதுகாப்பு](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ஹார்ட்வேர் ஆதரவு](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi மாடல்கள் மற்றும் தளங்களில் கிடைக்கும் நிலை](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai மற்றும் Phi பயன்படுத்துதல்](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub மார்க்கெட்பிளேஸ் மாடல்கள்](https://github.com/marketplace/models)
  - [Azure AI மாடல் பட்டியல்](https://ai.azure.com)

- வெவ்வேறு சூழல்களில் Phi-ஐ பயன்படுத்துதல்
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub மாடல்கள்](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry மாடல் பட்டியல்](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi குடும்பத்தை பயன்படுத்துதல்
    - [iOS-ல் Phi பயன்படுத்துதல்](./md/01.Introduction/03/iOS_Inference.md)
    - [Android-ல் Phi பயன்படுத்துதல்](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson-ல் Phi பயன்படுத்துதல்](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC-ல் Phi பயன்படுத்துதல்](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework உடன் Phi பயன்படுத்துதல்](./md/01.Introduction/03/MLX_Inference.md)
    - [உள்ளூர் சர்வரில் Phi பயன்படுத்துதல்](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit மூலம் தொலைநிலை சர்வரில் Phi பயன்படுத்துதல்](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust உடன் Phi பயன்படுத்துதல்](./md/01.Introduction/03/Rust_Inference.md)
    - [உள்ளூரில் Phi--Vision பயன்படுத்துதல்](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (அதிகாரப்பூர்வ ஆதரவு) உடன் Phi பயன்படுத்துதல்](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi குடும்பத்தை அளவிடுதல்](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp பயன்படுத்தி Phi-3.5 / 4-ஐ அளவிடுதல்](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime க்கான Generative AI விரிவாக்கங்களைப் பயன்படுத்தி Phi-3.5 / 4-ஐ அளவிடுதல்](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO பயன்படுத்தி Phi-3.5 / 4-ஐ அளவிடுதல்](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework பயன்படுத்தி Phi-3.5 / 4-ஐ அளவிடுதல்](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi மதிப்பீடு
    - [பொறுப்பான AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [மதிப்பீட்டுக்கான Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [மதிப்பீட்டுக்கான Promptflow பயன்படுத்துதல்](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI தேடலுடன் RAG
    - [Azure AI தேடலுடன் Phi-4-mini மற்றும் Phi-4-multimodal (RAG) பயன்படுத்துவது எப்படி](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi பயன்பாட்டு மேம்பாட்டு உதாரணங்கள்
  - உரை & அரட்டை பயன்பாடுகள்
    - Phi-4 உதாரணங்கள் 🆕
      - [📓] [Phi-4-mini ONNX மாடலுடன் அரட்டை செய்யவும்](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 உள்ளூர் ONNX மாடலுடன் .NET அரட்டை செய்யவும்](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel பயன்படுத்தி Phi-4 ONNX உடன் .NET கன்சோல் பயன்பாடு](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 உதாரணங்கள்
      - [உள்ளூர் உலாவியில் Phi3, ONNX Runtime Web மற்றும் WebGPU பயன்படுத்தி அரட்டைபேசும் பயன்பாடு](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino அரட்டை](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [பல மாடல் - Phi-3-mini மற்றும் OpenAI Whisper உடன் இடைமுகம்](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ஒரு மடக்கு உருவாக்குதல் மற்றும் MLFlow உடன் Phi-3 பயன்படுத்துதல்](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Olive உடன் ONNX Runtime Web க்கான Phi-3-min மாடலை எப்படி மேம்படுத்துவது](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [WinUI3 App with Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [WinUI3 பல மாடல் AI இயக்கப்படும் குறிப்புகள் பயன்பாட்டு மாதிரி](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Prompt flow உடன் தனிப்பயன் Phi-3 மாடல்களை Fine-tune செய்து ஒருங்கிணைத்தல்](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Azure AI Foundry-யில் Prompt flow உடன் தனிப்பயன் Phi-3 மாடல்களை Fine-tune செய்து ஒருங்கிணைத்தல்](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Microsoft-இன் பொறுப்பான AI கொள்கைகளை மையமாகக் கொண்டு Azure AI Foundry-யில் Fine-tuned Phi-3 / Phi-3.5 மாடலை மதிப்பீடு செய்தல்](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct மொழி கணிப்பு மாதிரி (சீனம்/ஆங்கிலம்)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU-ஐப் பயன்படுத்தி Phi-3.5-Instruct ONNX உடன் Prompt flow தீர்வை உருவாக்குதல்](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tflite-ஐப் பயன்படுத்தி Android பயன்பாட்டை உருவாக்குதல்](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Microsoft.ML.OnnxRuntime-ஐப் பயன்படுத்தி உள்ளூர் ONNX Phi-3 மாடலுடன் Q&A .NET எடுத்துக்காட்டு](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Semantic Kernel மற்றும் Phi-3 உடன் Console chat .NET பயன்பாடு](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK அடிப்படையிலான எடுத்துக்காட்டுகள் 
  - Phi-4 எடுத்துக்காட்டுகள் 🆕
    - [📓] [Phi-4-multimodal-ஐப் பயன்படுத்தி திட்டக் குறியீட்டை உருவாக்குதல்](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5 எடுத்துக்காட்டுகள்
    - [Microsoft Phi-3 குடும்பத்துடன் உங்கள் சொந்த Visual Studio Code GitHub Copilot Chat-ஐ உருவாக்குதல்](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [GitHub மாடல்களுடன் Phi-3.5-ஐப் பயன்படுத்தி உங்கள் சொந்த Visual Studio Code Chat Copilot Agent-ஐ உருவாக்குதல்](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- மேம்பட்ட காரணமறிதல் எடுத்துக்காட்டுகள்
  - Phi-4 எடுத்துக்காட்டுகள் 🆕
    - [📓] [Phi-4-mini-reasoning அல்லது Phi-4-reasoning எடுத்துக்காட்டுகள்](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Microsoft Olive உடன் Phi-4-mini-reasoning-ஐ Fine-tune செய்தல்](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Apple MLX உடன் Phi-4-mini-reasoning-ஐ Fine-tune செய்தல்](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [GitHub மாடல்களுடன் Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Azure AI Foundry மாடல்களுடன் Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- டெமோக்கள்
    - [Hugging Face Spaces-ல் Phi-4-mini டெமோக்கள்](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Hugging Face Spaces-ல் Phi-4-multimodal டெமோக்கள்](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- காட்சி எடுத்துக்காட்டுகள்
  - Phi-4 எடுத்துக்காட்டுகள் 🆕
    - [📓] [Phi-4-multimodal-ஐப் பயன்படுத்தி படங்களைப் படித்து குறியீட்டை உருவாக்குதல்](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Phi-3 / 3.5 எடுத்துக்காட்டுகள்
    - [📓][Phi-3-vision-பட எழுத்தை எழுத்தாக மாற்றுதல்](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP எம்பெடிங்](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [DEMO: Phi-3 மறுசுழற்சி](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - காட்சி மொழி உதவியாளர் - Phi3-Vision மற்றும் OpenVINO உடன்](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision பல-சட்டம் அல்லது பல-பட எடுத்துக்காட்டு](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Microsoft.ML.OnnxRuntime .NET-ஐப் பயன்படுத்தி உள்ளூர் ONNX மாடலுடன் Phi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Microsoft.ML.OnnxRuntime .NET-ஐப் பயன்படுத்தி மெனு அடிப்படையிலான உள்ளூர் ONNX மாடலுடன் Phi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi304)

- கணித எடுத்துக்காட்டுகள்
  - Phi-4-Mini-Flash-Reasoning-Instruct எடுத்துக்காட்டுகள் 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct உடன் கணித டெமோ](../../md/02.Application/09.Math/MathDemo.ipynb)

- ஆடியோ எடுத்துக்காட்டுகள்
  - Phi-4 எடுத்துக்காட்டுகள் 🆕
    - [📓] [Phi-4-multimodal-ஐப் பயன்படுத்தி ஆடியோ உரைகளை எடுப்பது](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodal ஆடியோ எடுத்துக்காட்டு](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal பேச்சு மொழிபெயர்ப்பு எடுத்துக்காட்டு](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET console பயன்பாட்டை பயன்படுத்தி Phi-4-multimodal ஆடியோ மூலம் ஆடியோ கோப்பை பகுப்பாய்வு செய்து உரையை உருவாக்குதல்](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOE எடுத்துக்காட்டுகள்
  - Phi-3 / 3.5 எடுத்துக்காட்டுகள்
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) சமூக ஊடக எடுத்துக்காட்டு](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search மற்றும் LlamaIndex உடன் Retrieval-Augmented Generation (RAG) குழாய்வழி உருவாக்குதல்](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- செயல்பாடு அழைக்கும் எடுத்துக்காட்டுகள்
  - Phi-4 எடுத்துக்காட்டுகள் 🆕
    - [📓] [Phi-4-mini உடன் Function Calling பயன்படுத்துதல்](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Phi-4-mini உடன் Function Calling மூலம் பல-முகவர்களை உருவாக்குதல்](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Ollama உடன் Function Calling பயன்படுத்துதல்](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [ONNX உடன் Function Calling பயன்படுத்துதல்](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- பலமாதிரி கலவை எடுத்துக்காட்டுகள்
  - Phi-4 எடுத்துக்காட்டுகள் 🆕
    - [📓] [தொழில்நுட்ப பத்திரிகையாளராக Phi-4-multimodal-ஐப் பயன்படுத்துதல்](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET console பயன்பாட்டை பயன்படுத்தி Phi-4-multimodal மூலம் படங்களை பகுப்பாய்வு செய்தல்](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi Fine-tuning எடுத்துக்காட்டுகள்
  - [Fine-tuning சூழல்கள்](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Fine-tuning vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3-ஐ தொழில்துறை நிபுணராக மாற்ற Fine-tuning](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code-க்கு AI Toolkit உடன் Phi-3-ஐ Fine-tune செய்தல்](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service உடன் Phi-3-ஐ Fine-tune செய்தல்](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora உடன் Phi-3-ஐ Fine-tune செய்தல்](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora உடன் Phi-3-ஐ Fine-tune செய்தல்](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry உடன் Phi-3-ஐ Fine-tune செய்தல்](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK உடன் Phi-3-ஐ Fine-tune செய்தல்](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive உடன் Fine-tuning](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Lab உடன் Fine-tuning](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias உடன் Phi-3-vision-ஐ Fine-tune செய்தல்](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework உடன் Phi-3-ஐ Fine-tune செய்தல்](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision-ஐ Fine-tune செய்தல் (அதிகாரப்பூர்வ ஆதரவு)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers உடன் Phi-3-ஐ Fine-Tune செய்தல் (அதிகாரப்பூர்வ ஆதரவு)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 மற்றும் 3.5 Vision-ஐ Fine-Tune செய்தல்](https://github.com/2U1/Phi3-Vision-Finetune)

- கையால் செய்யும் ஆய்வகம்
  - [முன்னணி மாடல்களை ஆராய்தல்: LLMs, SLMs, உள்ளூர் மேம்பாடு மற்றும் பல](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP திறனை திறக்குதல்: Microsoft Olive உடன் Fine-Tuning](https://github.com/azure/Ignite_FineTuning_workshop)

- கல்வி ஆராய்ச்சி ஆவணங்கள் மற்றும் வெளியீடுகள்
  - [Textbooks Are All You Need II: phi-1.5 தொழில்நுட்ப அறிக்கை](https://arxiv.org/abs/2309.05463)
  - [Phi-3 தொழில்நுட்ப அறிக்கை: உங்கள் தொலைபேசியில் உள்ளூர் அளவில் மிகவும் திறன் வாய்ந்த மொழி மாடல்](https://arxiv.org/abs/2404.14219)
  - [Phi-4 தொழில்நுட்ப அறிக்கை](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini தொழில்நுட்ப அறிக்கை: Mixture-of-LoRAs மூலம் சுருக்கமான ஆனால் சக்திவாய்ந்த பலமாதிரி மொழி மாடல்கள்](https://arxiv.org/abs/2503.01743)
  - [வாகனங்களுக்குள் செயல்பாடுகளை அழைக்க சிறிய மொழி மாதிரிகளை மேம்படுத்துதல்](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) பல்தேர்வு கேள்வி பதிலளிக்க PHI-3 ஐ நயம்செய்தல்: முறை, முடிவுகள் மற்றும் சவால்கள்](https://arxiv.org/abs/2501.01588)
  - [Phi-4-காரண விளக்கம் தொழில்நுட்ப அறிக்கை](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-காரண விளக்கம் தொழில்நுட்ப அறிக்கை](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi மாதிரிகளைப் பயன்படுத்துதல்

### Azure AI Foundry இல் Phi

Microsoft Phi ஐ எப்படி பயன்படுத்துவது மற்றும் உங்கள் பல்வேறு ஹார்ட்வேர் சாதனங்களில் E2E தீர்வுகளை உருவாக்குவது என்பதை நீங்கள் கற்றுக்கொள்ளலாம். Phi ஐ நேரடியாக அனுபவிக்க, மாதிரிகளை சோதித்து, உங்கள் சூழல்களுக்கு ஏற்ப Phi ஐ தனிப்பயனாக்குவதன் மூலம் தொடங்குங்கள். [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ஐப் பயன்படுத்தி மேலும் அறியலாம். [Azure AI Foundry உடன் தொடங்குதல்](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) பற்றிய தகவல்களையும் பார்க்கலாம்.

**பயிற்சி மையம்**
ஒவ்வொரு மாதிரிக்கும் [Azure AI Playground](https://aka.ms/try-phi3) எனும் தனித்துவமான பயிற்சி மையம் உள்ளது.

### GitHub மாதிரிகளில் Phi

Microsoft Phi ஐ எப்படி பயன்படுத்துவது மற்றும் உங்கள் பல்வேறு ஹார்ட்வேர் சாதனங்களில் E2E தீர்வுகளை உருவாக்குவது என்பதை நீங்கள் கற்றுக்கொள்ளலாம். Phi ஐ நேரடியாக அனுபவிக்க, மாதிரிகளை சோதித்து, உங்கள் சூழல்களுக்கு ஏற்ப Phi ஐ தனிப்பயனாக்குவதன் மூலம் தொடங்குங்கள். [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ஐப் பயன்படுத்தி மேலும் அறியலாம். [GitHub Model Catalog உடன் தொடங்குதல்](/md/02.QuickStart/GitHubModel_QuickStart.md) பற்றிய தகவல்களையும் பார்க்கலாம்.

**பயிற்சி மையம்**
ஒவ்வொரு மாதிரிக்கும் [மாதிரியை சோதிக்க தனித்துவமான பயிற்சி மையம் உள்ளது](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Hugging Face இல் Phi

மாதிரியை [Hugging Face](https://huggingface.co/microsoft) இல் காணலாம்.

**பயிற்சி மையம்**
[Hugging Chat பயிற்சி மையம்](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## பொறுப்பான செயற்கை நுண்ணறிவு

Microsoft, எங்கள் வாடிக்கையாளர்கள் எங்கள் AI தயாரிப்புகளை பொறுப்புடன் பயன்படுத்த உதவுவதற்கும், எங்கள் அனுபவங்களைப் பகிர்வதற்கும், மற்றும் நம்பகமான கூட்டாண்மைகளை உருவாக்குவதற்கும் உறுதியாக உள்ளது. Transparency Notes மற்றும் Impact Assessments போன்ற கருவிகள் மூலம் இதைச் செய்கிறது. இந்த வளங்களின் பலவற்றை [https://aka.ms/RAI](https://aka.ms/RAI) இல் காணலாம். 
Microsoft இன் பொறுப்பான AI யின் அணுகுமுறை நியாயம், நம்பகத்தன்மை மற்றும் பாதுகாப்பு, தனியுரிமை மற்றும் பாதுகாப்பு, உள்ளடக்கம், வெளிப்படைத்தன்மை மற்றும் பொறுப்புத்தன்மை ஆகிய AI கொள்கைகளில் அடிப்படையாக உள்ளது.

இந்த மாதிரியில் பயன்படுத்தப்படும் பெரிய அளவிலான இயற்கை மொழி, படங்கள் மற்றும் குரல் மாதிரிகள் - அவை அநியாயமான, நம்பகமற்ற அல்லது ஆபத்தான முறையில் நடந்து கொள்ளக்கூடும், இதனால் தீங்கு ஏற்பட வாய்ப்பு உள்ளது. அபாயங்கள் மற்றும் வரம்புகள் குறித்து தகவலறிந்து கொள்ள [Azure OpenAI சேவை வெளிப்படைத்தன்மை குறிப்பு](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ஐப் பார்க்கவும்.

இந்த அபாயங்களை குறைப்பதற்கான பரிந்துரைக்கப்பட்ட அணுகுமுறை, உங்கள் கட்டமைப்பில் ஒரு பாதுகாப்பு அமைப்பைச் சேர்ப்பது ஆகும், இது தீங்கு விளைவிக்கும் நடத்தை கண்டறிந்து தடுக்க முடியும். [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) என்பது ஒரு சுயாதீன பாதுகாப்பு அடுக்கு, இது பயன்பாடுகள் மற்றும் சேவைகளில் பயனர் உருவாக்கிய மற்றும் AI உருவாக்கிய தீங்கு விளைவிக்கும் உள்ளடக்கத்தை கண்டறிய முடியும். Azure AI Content Safety இல் உரை மற்றும் பட API கள் உள்ளன, அவை தீங்கு விளைவிக்கும் உள்ளடக்கத்தை கண்டறிய உதவுகின்றன. Azure AI Foundry இல், Content Safety சேவை பல்வேறு வடிவங்களில் தீங்கு விளைவிக்கும் உள்ளடக்கத்தை கண்டறிய மாதிரிக் குறியீடுகளைப் பார்க்க, ஆராய்ந்து முயற்சிக்க அனுமதிக்கிறது. இந்த [விரைவான தொடக்க ஆவணம்](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) சேவைக்கு கோரிக்கைகளைச் செய்ய உங்களை வழிநடத்துகிறது.

கணக்கில் கொள்ள வேண்டிய மற்றொரு அம்சம், மொத்த பயன்பாட்டு செயல்திறன் ஆகும். பல்துறை மற்றும் பல்மாதிரி பயன்பாடுகளுடன், செயல்திறன் என்பது உங்கள் மற்றும் உங்கள் பயனர்களின் எதிர்பார்ப்புகளுக்கு ஏற்ப அமைவது என்று கருதப்படுகிறது, அதில் தீங்கு விளைவிக்கும் வெளியீடுகளை உருவாக்காமல் இருப்பதும் அடங்கும். உங்கள் மொத்த பயன்பாட்டின் செயல்திறனை [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ஐப் பயன்படுத்தி மதிப்பீடு செய்வது முக்கியம். மேலும், நீங்கள் [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ஐ உருவாக்கி மதிப்பீடு செய்யும் திறனையும் பெறுகிறீர்கள்.

உங்கள் மேம்பாட்டு சூழலில் உங்கள் AI பயன்பாட்டை [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ஐப் பயன்படுத்தி மதிப்பீடு செய்யலாம். சோதனை தரவுத்தொகுப்பு அல்லது இலக்கு ஒன்றை வழங்கிய பிறகு, உங்கள் உருவாக்கும் AI பயன்பாட்டின் உருவாக்கங்கள், உங்கள் தேர்வின் உள்ளமைக்கப்பட்ட மதிப்பீட்டாளர்கள் அல்லது தனிப்பயன் மதிப்பீட்டாளர்களுடன் அளவிடப்படும். உங்கள் அமைப்பை மதிப்பீடு செய்ய azure ai evaluation sdk உடன் தொடங்க, [விரைவான தொடக்க வழிகாட்டியை](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) பின்பற்றலாம். ஒரு மதிப்பீட்டு இயக்கத்தைச் செயல்படுத்திய பிறகு, [Azure AI Foundry இல் முடிவுகளை காட்சிப்படுத்தலாம்](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## வர்த்தக முத்திரைகள்

இந்த திட்டத்தில் திட்டங்கள், தயாரிப்புகள் அல்லது சேவைகளுக்கான வர்த்தக முத்திரைகள் அல்லது லோகோக்கள் இருக்கலாம். Microsoft வர்த்தக முத்திரைகள் அல்லது லோகோக்களை அங்கீகரிக்கப்பட்ட முறையில் பயன்படுத்துவது [Microsoft இன் வர்த்தக முத்திரை மற்றும் பிராண்ட் வழிகாட்டுதல்களை](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) பின்பற்ற வேண்டும். 
இந்த திட்டத்தின் மாற்றியமைக்கப்பட்ட பதிப்புகளில் Microsoft வர்த்தக முத்திரைகள் அல்லது லோகோக்களைப் பயன்படுத்துவது குழப்பத்தை ஏற்படுத்தக்கூடாது அல்லது Microsoft ஆதரவை குறிக்கக்கூடாது. மூன்றாம் தரப்பு வர்த்தக முத்திரைகள் அல்லது லோகோக்களைப் பயன்படுத்துவது அந்த மூன்றாம் தரப்பின் கொள்கைகளுக்கு உட்பட்டது.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.