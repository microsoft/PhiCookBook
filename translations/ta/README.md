# Phi சமையல் புத்தகம்: Microsoft-ன் Phi மாதிரிகள் கொண்டு கைமுறை உதாரணங்கள்

[![GitHub Codespaces-ல் எடுத்துக்காட்டு சம்மேளினைகளை திறந்து பயன்பாடு செய்யவும்](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers-ல் திறக்கவும்](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub பங்களிப்பாளர்கள்](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub பிரச்சினைகள்](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub உருவாக்க வேண்டுகோள்கள்](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![உருவாக்க வேண்டுகோள்கள் வரவேற்கப்படுகின்றன](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub பார்வையிடுபவர்கள்](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub பிரிந்துபோக்கள்](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub நட்சத்திரங்கள்](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi என்பது Microsoft நிறுவனத்தால் உருவாக்கப்பட்ட ஓர் தொடர் திறந்த மூல AI மாதிரிகளாகும்.

Phi தற்போது மிகவும் சக்திவாய்ந்த மற்றும் குறைந்த செலவுடைய சிறிய மொழி மாதிரி (SLM) ஆகும், இது பல்வேறு மொழிகள், தீர்க்கமான நினைவூட்டல், எழுத்து/குரல் உருவாக்கம், குறியீடு, படங்கள், ஒலி மற்றும் பிற சூழல்களில் சிறந்த பண்புகளை வழங்குகிறது.

Phi-வை மேகம் அல்லது முனையப் பொருட்களில் பயன்படுத்தலாம், மற்றும் குறைந்த கணினி சக்தியுடன் உருவாக்கும் AI பயன்பாடுகளை எளிதாக உருவாக்கலாம்.

இந்த ஆதாரங்களைப் பயன்படுத்த தொடங்க கீழ்காணும் படிகளை பின்பற்றவும்:
1. **கிட ஹப்பில் கொள்கையை கிளோன் செய்யவும்**: கிளிக் செய்யவும் [![GitHub பிரிந்துபோக்கள்](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **கிட ஹப்பைக் க்ளோன் செய்யவும்**:  `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord சமூகத்தில் சேர்ந்து நிபுணர்களையும் தங்களோடு தொகுப்பு செய்பவர்களையும் சந்திக்கவும்**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/ta/cover.eb18d1b9605d754b.webp)

### 🌐 பல்மொழி ஆதரவு

#### GitHub Action மூலம் ஆதரவு (தானியங்கி மற்றும் எப்போதும் புதுப்பிப்பு)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](./README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **உள்ளூரில் க்ளோன் செய்வது விரும்புகிறீர்களா?**
>
> இந்தக் கொள்கை 50+ மொழி மொழிபெயர்ப்புகளையும் கொண்டுள்ளது, இதனால் பதிவிறக்கம் அளவு பெரிதாக இருக்கும். மொழிபெயர்ப்புகள் இல்லாமல் க்ளோன் செய்ய sparse checkout பயன்படுத்தவும்:
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
> இது பாடநெறியை முடிக்க தேவையான அனைத்தையும் குறைந்த நேரத்தில் தரும்.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## உள்ளடக்க அட்டவணை
- அறிமுகம் - [பை குடும்பத்திற்கு வரவேற்கிறோம்](./md/01.Introduction/01/01.PhiFamily.md) - [உங்கள் சூழலை அமைத்தல்](./md/01.Introduction/01/01.EnvironmentSetup.md) - [முக்கிய தொழில்நுட்பங்களை புரிந்துகொள்வது](./md/01.Introduction/01/01.Understandingtech.md) - [பை மாதிரிகளுக்கான எஐ பாதுகாப்பு](./md/01.Introduction/01/01.AISafety.md) - [பை ஹார்ட்வேரின் ஆதரவு](./md/01.Introduction/01/01.Hardwaresupport.md) - [பை மாதிரிகள் மற்றும் தளங்களின் விலைமதிப்பு](./md/01.Introduction/01/01.Edgeandcloud.md) - [Guidance-ai மற்றும் பை பயன்படுத்துதல்](./md/01.Introduction/01/01.Guidance.md) - [GitHub மார்க்கெட்பிளேஸ் மாதிரிகள்](https://github.com/marketplace/models) - [அஸ்யூர் எஐ மாதிரி பட்டியல்](https://ai.azure.com) - வேறுவேறு சூழலில் பை தீர்மானம் - [Hugging face](./md/01.Introduction/02/01.HF.md) - [GitHub மாதிரிகள்](./md/01.Introduction/02/02.GitHubModel.md) - [Microsoft Foundry மாதிரி பட்டியல்](./md/01.Introduction/02/03.AzureAIFoundry.md) - [Ollama](./md/01.Introduction/02/04.Ollama.md) - [ஏஐ டூல்கிட் VSCode (AITK)](./md/01.Introduction/02/05.AITK.md) - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md) - [Foundry ஒ.resultsறியிடம்](./md/01.Introduction/02/07.FoundryLocal.md) - பை குடும்பத்தில் தீர்மானம் - [iOS இல் பை தீர்மானம்](./md/01.Introduction/03/iOS_Inference.md) - [ஆண்ட்ராய்டில் பை தீர்மானம்](./md/01.Introduction/03/Android_Inference.md) - [ஜெட்‌സனில் பை தீர்மானம்](./md/01.Introduction/03/Jetson_Inference.md) - [ஏஐ பிசியில் பை தீர்மானம்](./md/01.Introduction/03/AIPC_Inference.md) - [ஆப்பிள் MLX கட்டமைப்புடன் பை தீர்மானம்](./md/01.Introduction/03/MLX_Inference.md) - [உள் சேவையகத்தில் பை தீர்மானம்](./md/01.Introduction/03/Local_Server_Inference.md) - [ஏஐ டூல்கிட் பயன்படுத்தி தொலை சேவையகத்தில் பை தீர்மானம்](./md/01.Introduction/03/Remote_Interence.md) - [ரஸ்ட் உடன் பை தீர்மானம்](./md/01.Introduction/03/Rust_Inference.md) - [உள் பகுதியிலுள்ள பை--விஷன் தீர்மானம்](./md/01.Introduction/03/Vision_Inference.md) - [Kaito AKS, Azure டக்கர் கொண்டெய்னர்கள் (அதிகாரப்பூர்வ ஆதரவு) உடன் பை தீர்மானம்](./md/01.Introduction/03/Kaito_Inference.md) - [பை குடும்பத்தை தொகுக்குதல்](./md/01.Introduction/04/QuantifyingPhi.md) - [llama.cpp பயன்படுத்தி பை-3.5 / 4 தொகுக்கல்](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md) - [onnxruntime க்கான உருவாக்கும் ஏஐ நீட்சிகளுடன் பை-3.5 / 4 தொகுக்கல்](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md) - [Intel OpenVINO பயன்படுத்தி பை-3.5 / 4 தொகுக்கல்](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md) - [ஆப்பிள் MLX கட்டமைப்பு பயன்படுத்தி பை-3.5 / 4 தொகுக்கல்](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md) - பை மதிப்பீடு - [பதில் எஐ](./md/01.Introduction/05/ResponsibleAI.md) - [மைக்ரோசாப்ட் Foundry மூலம் மதிப்பீடு](./md/01.Introduction/05/AIFoundry.md) - [மதிப்பீட்டுக்கான Promptflow பயன்பாடு](./md/01.Introduction/05/Promptflow.md) - அஸ்யூர் எஐ தேடும் மூலம் RAG - [அஸ்யூர் எஐ தேடும் மூலம் Phi-4-mini மற்றும் Phi-4-multimodal(RAG) பயன்படுத்துவது எப்படி](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb) - பை பயன்பாடு மேம்பாட்டு மாதிரிகள் - உரை & உரையாடல் பயன்பாடுகள் - பை-4 மாதிரிகள் - [📓] [Phi-4-mini ONNX மாதிரி உடன் உரையாடல்](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md) - [பை-4 உள்ளூர் ONNX மாதிரி .NET உடன் உரையாடல்](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) - [சாமானிய கர்னல் பயன்படுத்தி பை-4 ONNX உடன் .NET கமாண்டு வரி செயலி உரையாடல்](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) - பை-3 / 3.5 மாதிரிகள் - [உலாவியில் உள்ளூர் சாட்பாட் பை3, ONNX Runtime Web மற்றும் WebGPU பயன்படுத்தி](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat) - [OpenVino உரையாடல்](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md) - [பல்வகை மாதிரி - பை-3-mini மற்றும் OpenAI Whisper இணைந்த உரையாடல்](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md) - [MLFlow - ஒரு ஓரங்கத்தை உருவாக்கி பை-3 உடன் MLFlow பயன்படுத்துதல்](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md) - [மாதிரி மென்மைப்படுத்தல் - ONNX Runtime Web க்கான பை-3-min மாதிரியை Olive உடன் எண்ணெயப்படுத்துதல்](https://github.com/microsoft/Olive/tree/main/examples/phi3) - [WinUI3 செயலி பை-3 mini-4k-instruct-onnx உடன்](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/) -[WinUI3 பலவகை மாதிரி AI மூலம் இயக்கப்படும் குறிப்பு செயலி மாதிரி](https://github.com/microsoft/ai-powered-notes-winui3-sample) - [சந்தா-நேர்த்தியுடன் மற்றும் Prompt flow உடன் தனிப்பயன் பை-3 மாதிரிகளை நுட்பமாக மாற்றுதல் மற்றும் இணைத்தல்](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md) - [Microsoft Foundry இல் Prompt flow உடன் தனிப்பயன் பை-3 மாதிரிகளை நுட்பமாக மாற்றுதல் மற்றும் இணைத்தல்](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md) - [Microsoft இன் பொறுப்பான AIக் கொள்கைகளை கவனித்து Microsoft Foundry இல் நுட்பமாக மாற்றப்பட்ட பை-3 / பை-3.5 மாதிரியை மதிப்பீடு செய்தல்](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md) - [📓] [பை-3.5-mini-instruct மொழி முன்னறிவிப்பு மாதிரி (சீன/ஆங்கில)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb) - [பை-3.5-Instruct WebGPU RAG சாட்பாட்](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md) - [Windows GPU பயன்படுத்தி பை-3.5-Instruct ONNX உடன் Prompt flow தீர்வு உருவாக்குதல்](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md) - [மைக்ரோசாப்ட் பை-3.5 tflite பயன்படுத்தி ஆண்ட்ராய்டு செயலி உருவாக்குதல்](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md) - [உள்ளூர் ONNX பை-3 மாதிரியை Microsoft.ML.OnnxRuntime பயன்படுத்தி Q&A .NET உதாரணம்](../../md/04.HOL/dotnet/src/LabsPhi301) - [சாமானிய கர்னல் மற்றும் பை-3 உடன் கமாண்டு வரி உரையாடல் .NET செயலி](../../md/04.HOL/dotnet/src/LabsPhi302) - அஸ்யூர் எஐ தீர்மான SDK குறியீடு அடிப்படையிலான மாதிரிகள் - பை-4 மாதிரிகள் - [📓] [பை-4-multimodal பயன்படுத்தி திட்ட குறியீடு உருவாக்குதல்](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md) - பை-3 / 3.5 மாதிரிகள் - [உங்கள் சொந்த Visual Studio Code GitHub Copilot உரையாடலை Microsoft பை-3 குடும்பத்துடன் உருவாக்குதல்](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md) - [GitHub மாதிரிகள் கொண்டு பை-3.5 உடன் உங்கள் சொந்த Visual Studio Code உரையாடல் Copilot முகவரியை உருவாக்குதல்](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md) - மேம்பட்ட காரணமும் மாதிரிகள் - பை-4 மாதிரிகள் - [📓] [பை-4-mini-காரணம் அல்லது பை-4-காரணம் மாதிரிகள்](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md) - [📓] [Microsoft Olive உடன் பை-4-mini-காரணம் நுட்பமாக மாற்றுதல்](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [ஆப்பிள் MLX உடன் பை-4-mini-காரணம் நுட்பமாக மாற்றுதல்](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [GitHub மாதிரிகளுடன் பை-4-mini-காரணம்](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb) - [📓] [Microsoft Foundry மாதிரிகளுடன் பை-4-mini-காரணம்](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb) -
டெமோஸ் - [ஹக்கிங் பேஸ் ஸ்பேஸ்களில் ஹோஸ்ட் செய்யப்பட்ட Phi-4-mini டெமோஸ்](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo) - [ஹக்கிங்க் பேஸ் ஸ்பேஸ்களில் ஹோஸ்ட் செய்யப்பட்ட Phi-4-multimodal டெமோஸ்](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo) - காட்சி மாதிரிகள் - Phi-4 மாதிரிகள் - [📓] [புகைப்படங்களை வாசித்து குறியீடு உருவாக்க Phi-4-multimodal பயன்படுத்தவும்](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) - Phi-3 / 3.5 மாதிரிகள் - [📓][Phi-3-vision-புகைப்படம் உரை க்கு தமிழாக்கம்](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html) - [📓][Phi-3-vision CLIP எம்பெட்டிங்](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [டெமோ: Phi-3 மறுசுழற்சி](https://github.com/jennifermarsman/PhiRecycling/) - [Phi-3-vision - காட்சி மொழி உதவியாளர் - Phi3-Vision மற்றும் OpenVINO உடன்](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html) - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md) - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md) - [📓][Phi-3.5 Vision பல-ஃப்ரேம் அல்லது பல-புகைப்பட மாதிரி](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb) - [Microsoft.ML.OnnxRuntime .NET பயன்படுத்தி Phi-3 Vision உள்ளூர் ONNX மாதிரி](../../md/04.HOL/dotnet/src/LabsPhi303) - [மெனு அடித்த Phi-3 Vision உள்ளூர் ONNX மாதிரி Microsoft.ML.OnnxRuntime .NET மூலம்](../../md/04.HOL/dotnet/src/LabsPhi304) - காரணம்-காட்சி மாதிரிகள் - Phi-4-காரணம்-காட்சி-15B - [📓] [Phi-4-காரணம்-காட்சி-15B எடுத்துக்காட்டி jaywalking கண்டறிதல்](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb) - [📓] [Phi-4-காரணம்-காட்சி-15B கொண்டு கணிதம்](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb) - [📓] [Phi-4-காரணம்-காட்சி-15B கொண்டு UI கண்டறிதல்](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb) - கணித மாதிரிகள் - Phi-4-Mini-Flash-காரணம்-கேற்கூறல் மாதிரிகள் [Phi-4-Mini-Flash-காரணம்-கேற்கூறல் உடன் கணித டெமோ](./md/02.Application/09.Math/MathDemo.ipynb) - ஒலி மாதிரிகள் - Phi-4 மாதிரிகள் - [📓] [Phi-4-multimodal உபயோகித்து ஒலி பதிவுகளை எடுக்க](./md/02.Application/05.Audio/Phi4/Transciption/README.md) - [📓] [Phi-4-multimodal ஒலி மாதிரி](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb) - [📓] [Phi-4-multimodal பேசும் மொழி மொழிபெயர்ப்பு மாதிரி](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb) - [Phi-4-multimodal ஒலி பயன் படுத்தி ஒரு ஒலி கோப்பை பகுப்பாய்வு செய்து பெயர்ப்பிரதி உருவாக்கும் .NET கலக்கு பயன்பாடு](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) - MOE மாதிரிகள் - Phi-3 / 3.5 மாதிரிகள் - [📓] [Phi-3.5 நிபுணர்களின் கலவை மாதிரிகள் (MoEs) சமூக ஊடக மாதிரி](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb) - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI தேடல், மற்றும் LlamaIndex உடன் Retrieval-Augmented Generation (RAG) குழாய் கட்டமைத்தல்](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb) - - செயல் அழைப்பு மாதிரிகள் - Phi-4 மாதிரிகள் 🆕 - [📓] [Phi-4-mini உடன் செயல் அழைப்பை பயன்படுத்துதல்](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md) - [📓] [Phi-4-mini உடன் பன்முக முகவர்களை உருவாக்க செயல் அழைப்பை பயன்படுத்துதல்](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb) - [📓] [Ollama உடன் செயல் அழைப்பை பயன்படுத்துதல்](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb) - [📓] [ONNX உடன் செயல் அழைப்பை பயன்படுத்துதல்](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb) - பன்முக கிளைமைமை கலவை மாதிரிகள் - Phi-4 மாதிரிகள் 🆕 - [📓] [தொழில்நுட்ப செய்தியாளர் போல Phi-4-multimodal பயன்படுத்துதல்](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb) - [Phi-4-multimodal கொண்டு படங்களை பகுப்பாய்வு செய்ய .NET கலக்கு பயன்பாடு](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) - மேம்படுத்தல் Phi மாதிரிகள் - [மேம்படுத்தல் காட்சிகள்](./md/03.FineTuning/FineTuning_Scenarios.md) - [மேம்படுத்தல் மற்றும் RAG இன் ஒப்பீடு](./md/03.FineTuning/FineTuning_vs_RAG.md) - [Phi-3 ஐ ஒரு தொழிற்சாலை நிபுணனாக்கும் மேம்படுத்தல்](./md/03.FineTuning/LetPhi3gotoIndustriy.md) - [VS Code ஐற்கான AI கருவிகள் மூலம் Phi-3 மேம்படுத்தல்](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md) - [Azure Machine Learning சேவையுடன் Phi-3 மேம்படுத்தல்](./md/03.FineTuning/Introduce_AzureML.md) - [Lora மூலம் Phi-3 மேம்படுத்தல்](./md/03.FineTuning/FineTuning_Lora.md) - [QLora மூலம் Phi-3 மேம்படுத்தல்](./md/03.FineTuning/FineTuning_Qlora.md) - [Microsoft Foundry உடன் Phi-3 மேம்படுத்தல்](./md/03.FineTuning/FineTuning_AIFoundry.md) - [Azure ML CLI/SDK உடன் Phi-3 மேம்படுத்தல்](./md/03.FineTuning/FineTuning_MLSDK.md) - [Microsoft Olive உடன் மேம்படுத்தல்](./md/03.FineTuning/FineTuning_MicrosoftOlive.md) - [Microsoft Olive கைபிடித்தல் ஆய்வு](./md/03.FineTuning/olive-lab/readme.md) - [Weights and Bias உதவியுடன் Phi-3-vision மேம்படுத்தல்](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md) - [Apple MLX கட்டமைப்புடன் Phi-3 மேம்படுத்தல்](./md/03.FineTuning/FineTuning_MLX.md) - [அங்கீகரிக்கப்பட்ட Phi-3-vision மேம்படுத்தல்](./md/03.FineTuning/FineTuning_Vision.md) - [Kaito AKS, Azure Containers உடன் Phi-3 மேம்படுத்தல் (அங்கீகரிக்கப்பட்ட ஆதரவு)](./md/03.FineTuning/FineTuning_Kaito.md) - [Phi-3 மற்றும் 3.5 Vision மேம்படுத்தல்](https://github.com/2U1/Phi3-Vision-Finetune) - ஆய்வக ஆய்வு - [அதிக நுட்ப LLMs, SLMs, உள்ளூர் வளர்ச்சியை ஆராய்வு](https://github.com/microsoft/aitour-exploring-cutting-edge-models) - [மொழி செயலாக்க திறன்களை திறக்க Microsoft Olive உடன் மேம்படுத்தல்](https://github.com/azure/Ignite_FineTuning_workshop) - கல்வி ஆய்வு கட்டுரைகள் மற்றும் வெளியீடுகள் - [Textbooks Are All You Need II: phi-1.5 தொழில்நுட்ப அறிக்கை](https://arxiv.org/abs/2309.05463) - [Phi-3 தொழில்நுட்ப அறிக்கை: உங்கள் கைபேசியில் உள்ள மிகவும் திறமையான மொழி மாதிரி](https://arxiv.org/abs/2404.14219) - [Phi-4 தொழில்நுட்ப அறிக்கை](https://arxiv.org/abs/2412.08905) - [Phi-4-Mini தொழில்நுட்ப அறிக்கை: கலவை-ஓப்-ஏலோராஸ் மூலம் கம்பெக்ட் ஆனால் சக்திவாய்ந்த பன்முக மொழி மாதிரிகள்](https://arxiv.org/abs/2503.01743) - [கோப்புறுதி செயல்பாட்டுக்கான சிறிய மொழி மாதிரிகளை விருத்தி செய்தல்](https://arxiv.org/abs/2501.02342) - [(WhyPHI) பன்மடங்கு-தேர்ந்தெடுக்கும் கேள்வி பதில் பயிற்சிக்காக PHI-3 மேம்படுத்தல்: முறை, முடிவுகள் மற்றும் சவால்கள்](https://arxiv.org/abs/2501.01588) - [Phi-4-காரணம் தொழில்நுட்ப அறிக்கை](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-காரணம் தொழில்நுட்ப அறிக்கை](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)
# Phi Cookbook: Microsoft-ன் Phi மாதிரிகளுடன் நேரடியாக உதாரணங்கள்

[![GitHub Codespaces-இல் எடுத்துக்காட்டு கோப்புகளை திறந்து பயன்படுத்துக](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers-இல் திறக்கவும்](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub நோக்கர்கள்](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub பண்பொருள்](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub எடுக்கும் கோரிக்கைகள்](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs வரவேற்கப்படுகின்றன](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub கவனிக்கவர்கள்](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub கிளோன்கள்](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub நட்சத்திரங்கள்](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi என்பது Microsoft әзுமாக உருவாக்கப்பட்ட ஒரு தொடர் திறந்த மூல AI மாதிரிகள் ஆகும்.

Phi தற்போது மிகவும் சக்திவாய்ந்த மற்றும் செலவு குறைவான சிறிய மொழி மாதிரி (SLM), மற்றும் பன்மொழி, காரணமயம், உரை/செய்தி உருவாக்கம், குறியீடு, படங்கள், ஒலி மற்றும் பிற நிலைகளில் சிறந்த மீட்டுகளைக் கொண்டுள்ளது.

Phi-வை மேகத்தில் அல்லது எட்ஜ் சாதனங்களில் நாட்டிக் கொண்டு செல்லலாம், மேலும் குறைந்த கணினி சக்தியுடனும் உருவாக்கும் AI செயலிகளை எளிதாக கட்டமைக்கலாம்.

இந்த வளங்களைப் பயன்படுத்தத் தொடங்க பின்வரும் படிகளை பின்பற்றவும்:
1. **கிடப்பார்வையை பிரிக்கவும்**: கிளிக் செய்க [![GitHub கிளோன்கள்](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **கிடப்பார்வையை கிளோன் செய்க**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord சமூகத்தில் சேர்ந்து நிபுணர்களையும் மற்ற டெவலப்பர்களையும் சந்திக்கவும்**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/ta/cover.eb18d1b9605d754b.webp)

### 🌐 பன்மொழி ஆதரவு

#### GitHub செயல்பாட்டினால் ஆதரிக்கப்படுகிறது (தானியங்கி மற்றும் எப்போதும் புதுப்பிக்கப்படும்)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[அரபு](../ar/README.md) | [பெங்காலி](../bn/README.md) | [பல்கேரியன்](../bg/README.md) | [பர்மேஸ் (மியன்னார்)](../my/README.md) | [சீன (எளிமைப்படுத்தப்பட்ட)](../zh-CN/README.md) | [சீன (பாரம்பரிய, ஹாங்கொங்)](../zh-HK/README.md) | [சீன (பாரம்பரிய, மேக்காவ்)](../zh-MO/README.md) | [சீன (பாரம்பரிய, தைவான்)](../zh-TW/README.md) | [குரோஷியன்](../hr/README.md) | [செக்](../cs/README.md) | [டேனிஷ்](../da/README.md) | [டச்சு](../nl/README.md) | [எஸ்டோனியன்](../et/README.md) | [பின்னிஷ்](../fi/README.md) | [பிரஞ்சு](../fr/README.md) | [ஜெர்மன்](../de/README.md) | [கிரேக்கு](../el/README.md) | [ஹீப்ரூ](../he/README.md) | [ஹிந்தி](../hi/README.md) | [ஹங்கேரியன்](../hu/README.md) | [இந்தோனேஷியன்](../id/README.md) | [இத்தாலியன்](../it/README.md) | [ஜப்பானீஸ்](../ja/README.md) | [கன்னடம்](../kn/README.md) | [கொரியன்](../ko/README.md) | [லிதுவேனியன்](../lt/README.md) | [மலாய்](../ms/README.md) | [மலையாளம்](../ml/README.md) | [மராத்தி](../mr/README.md) | [நேபாளி](../ne/README.md) | [நைஜீரியன் பிஜின்](../pcm/README.md) | [நார்வேஜியன்](../no/README.md) | [பர்ஷியன் (பார்ஸி)](../fa/README.md) | [போலிஷ்](../pl/README.md) | [போர்ச்சுகீஸ் (பிரேசில்)](../pt-BR/README.md) | [போர்ச்சுகீஸ் (போர்ச்சுகல்)](../pt-PT/README.md) | [பஞ்சாபி (குருமுகி)](../pa/README.md) | [ரோமானியன்](../ro/README.md) | [ரஷ்யன்](../ru/README.md) | [செர்பியன் (சிிரிலிக்)](../sr/README.md) | [ஸ்லோவாக்](../sk/README.md) | [ஸ்லோவேனியன்](../sl/README.md) | [ஸ்பானிஷ்](../es/README.md) | [ஸ்வாஹிலி](../sw/README.md) | [ஸ்வீடிஷ்](../sv/README.md) | [டாகாலோக் (பிலிப்பைன்ஸ்)](../tl/README.md) | [தமிழ்](./README.md) | [தேலுகு](../te/README.md) | [தாய்](../th/README.md) | [துருக்கிய](../tr/README.md) | [உக்ரைனியன்](../uk/README.md) | [உருது](../ur/README.md) | [வியட்நாமீஸ்](../vi/README.md)

> **உள்ளூரில் கிளோன் செய்ய விரும்புகிறீர்களா?**
>
> இந்த கிடப்பார்வை 50+ மொழி மொழிபெயர்ப்புகளை கொண்டுள்ளது, இதனால் பதிவிறக்கம் அளவு பெருக்கப்படுகிறது. மொழிபெயர்ப்புகள் இல்லாமல் கிளோன் செய்ய sparse checkout பயன்படுத்தவும்:
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
> இது பாடத்திட்டத்தை முடிக்க தேவையான அனைத்தையும் வேகமாக பதிவிறக்கம் செய்ய உதவும்.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## உள்ளடக்க பட்டியல்

## Phi மாதிரிகளை பயன்படுத்துதல்

### Microsoft Foundry-இல் Phi

Microsoft Phi-வை எப்படி பயன்படுத்துவது மற்றும் உங்கள் வேறுபட்ட இயந்திர சாதனங்களில் முழுமை முடிவுகளை கட்டமைப்பது கற்றுக்கொள்ளலாம். Phi-வை உங்கள் காட்சிகளுக்கு தனிப்பயனாக்கி மாதிரிகளுடன் விளையாடி அனுபவிக்க, [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ஐ பயன்படுத்தவும். மேலும் அறிய [Microsoft Foundry உடன் தொடங்குதல்](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**பிளேக்ரவுண்ட்**
ஒவ்வொரு மாதிரிக்கும் மாதிரியை சோதிக்க அர்ப்பணிக்கப்பட்ட பிளேக்ரவுண்ட் உள்ளது [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub மாதிரிகளிலான Phi

Microsoft Phi-வை எப்படி பயன்படுத்துவது மற்றும் உங்கள் வேறுபட்ட இயந்திர சாதனங்களில் முழுமை முடிவுகளை கட்டமைப்பது கற்றுக்கொள்ளலாம். Phi-வை உங்கள் காட்சிகளுக்கு தனிப்பயனாக்கி மாதிரிகளுடன் விளையாடி அனுபவிக்க, [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ஐ பயன்படுத்தவும். மேலும் அறிய [GitHub Model Catalog உடன் தொடங்குதல்](/md/02.QuickStart/GitHubModel_QuickStart.md)

**பிளேக்ரவுண்ட்**
ஒவ்வொரு மாதிரிக்கும் மாதிரியை சோதிக்க அர்ப்பணிக்கப்பட்ட [பிளேக்ரவுண்ட்](/md/02.QuickStart/GitHubModel_QuickStart.md) உள்ளது.

### Hugging Face-இல் Phi

மாதிரியை [Hugging Face](https://huggingface.co/microsoft) இல் காணலாம்.

**பிளேக்ரவுண்ட்**
 [Hugging Chat பிளேக்ரவுண்ட்](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 பிற பாடத்திட்டங்கள்

எங்கள் குழு மற்ற பாடத்திட்டங்களையும் உருவாக்குகிறது! பாருங்கள்:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j தொடக்கத்திற்கானது](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js தொடக்கத்திற்கானது](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain தொடக்கத்திற்கானது](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / முகவரிகள்
[![AZD தொடக்கத்திற்கானது](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI தொடக்கத்திற்கானது](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP தொடக்கத்திற்கானது](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI முகவரிகள் தொடக்கத்திற்கானது](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### உருவாக்கும் AI தொடர்
[![உருவாக்கும் AI தொடக்கத்திற்கானது](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![உருவாக்கும் AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### முக்கிய கற்றல்
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### கோபைலட் தொடர்
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## பொறுப்புள்ள AI 

Microsoft எங்கள் AI தயாரிப்புகளை பெறுமதிகரமாகவும் பொறுப்புடன் பயன்படுத்துக, எங்கள் கற்றல்களை பகிரவும், Transparency Notes மற்றும் Impact Assessments போன்ற கருவிகள் மூலம் நம்பிக்கையுடன் கூடிய கூட்டாளித்துவத்தை கட்டமைக்க முயற்சிக்கிறது. இவை போன்ற பல வளங்கள் [https://aka.ms/RAI](https://aka.ms/RAI) ல் கிடைக்கின்றன.
Microsoft இன் பொறுப்புள்ள AI அணுகுமுறை நியாயம், நம்பகத்தன்மை மற்றும் பாதுகாப்பு, தனியுரிமை மற்றும் பாதுகாப்பு, உள்ளடக்கம், தெளிவுத்தன்மை மற்றும் பொறுப்புதன்மை ஆகிய AI 원칙ங்களின் அடிப்படையில் உள்ளது.

பெரிய அளவிலான இயற்கை மொழி, படம் மற்றும் பேச்சு மாதிரிகள் - இதுவரை இந்த மாதிரிகள் பயன்படுத்தியுள்ள மாதிரிகள் போன்றவை - சில நேரங்களில் நீதிமற்றவைகளாக, நம்ப முடியாதவைகளாக அல்லது தடங்கலானவையாக இருக்கக்கூடும், இது தீங்க்களை ஏற்படுத்தும். ஆபத்துக்கள் மற்றும் வரம்புகள் குறித்து அறிவதற்கு [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ஐ அணுகவும்.

இந்த ஆபத்துக்களை குறைக்க பரிந்துரைக்கப்படும் முறையானது உங்கள் கட்டமைப்பில் தீங்கான நடத்தையை கண்டறிந்து தடுக்கக்கூடிய பாதுகாப்பு அமைப்பை சேர்ப்பதாகும். [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) தனித்துவமான பாதுகாப்பு நிலையை வழங்குகிறது, பயன்பாடுகளில் மற்றும் சேவைகளில் தீங்கு விளைவிக்கும் பயனர் உருவாக்கிய மற்றும் AI உருவாக்கிய உள்ளடக்கத்தை கண்டறியக்கூடியது. Azure AI Content Safety உரை மற்றும் படம் APIs கொண்டுள்ளது, இது தீங்கு விளைவிக்கும் பொருள்களை கண்டறிய உதவுகிறது. Microsoft Foundry இல் Content Safety சேவை, வேறு வகை உள்ளடக்கங்களில் தீங்கு விளைவிக்கும் உள்ளடக்கத்தை கண்டறிய மாதிரி குறியீடுகளை பார்க்க, ஆராய்ந்து முயற்சிக்க அனுமதிக்கிறது. மேற்கண்ட [விரைவு வழிகாட்டி ஆவணம்](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) உங்களுக்கு சேவைக்கு கோரிக்கைகளைச் செய்ய வழிகாட்டுகிறது.

மேலும் கவனிக்க வேண்டிய அம்சம் முழுமையான பயன்பாட்டு செயல்திறன் ஆகும். பன்முக மற்றும் பல மாதிரி பயன்பாடுகளில், செயல்திறன் என்பது தொகுத்தமைப்பும் உங்கள் மற்றும் உங்கள் பயனர்கள் எதிர்பார்க்கும் படி செயல்படுதல் என்பதைக் குறிக்கும், இதில் தீங்கு விளைவிக்கும் முடிவுகள் உருவாக்கப்படாமலும் உள்ளது. உங்கள் முழுமையான பயன்பாட்டின் செயல்திறனை [Performance and Quality and Risk and Safety évaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) மூலம் வடிவமைத்து மதிப்பிடுவது முக்கியம். நீங்கள் வெவ்வேறு [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) உருவாக்கி மதிப்பீடு செய்ய முடியும்.

[Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) மூலம் உங்கள் AI பயன்பாட்டை உங்கள் மேம்பாட்டு சூழலில் மதிப்பிடலாம். தேர்வுப் தரவுத்தொகை அல்லது இலக்கைப் பொருத்து, உங்கள் ஜெனெரேட்டிவ் AI பயன்பாட்டின் உருவாக்கங்கள் கட்டமைக்கப்பட்ட மதிப்பீட்டாளர்களோ அல்லது உங்கள் விருப்ப.custom evaluators கொண்டு கணக்கிடப்படும். உங்கள் செயல்திறனை மதிப்பிட Azure AI Evaluation SDK பயன்படுத்த [விரைவு வழிகாட்டி](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) இனை பின்பற்றலாம். மதிப்பீடு ஓட்டத்தை இயக்கிய பிறகு, நீங்கள் முடிவுகளை [Microsoft Foundry இல் காட்சி படுத்த](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) முடியும்.

## வர்த்தக அடையாளங்கள்

இந்தத் திட்டத்தில் திட்டங்கள், தயாரிப்புகள் அல்லது சேவைகளின் வர்த்தக அடையாளங்கள் அல்லது லோகோக்கள் இருக்கலாம். Microsoft வர்த்தக அடையாளங்கள் அல்லது லோகோக்களை உரிய முறையில் பயன்படுத்துவதற்கு [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ஐ பின்பற்ற வேண்டும்.
Microsoft வர்த்தக அடையாளங்களை அல்லது லோகோக்களை திருத்தப்பட்ட பதிப்புகளில் பயன்படுத்துவதால் குழப்பம் ஏற்படக்கூடாது அல்லது Microsoft ஆதரவாக இருப்பதாக புரியக்கூடாது. முப்பக்கத் தரப்புகளின் வர்த்தக அடையாளங்கள் மற்றும் லோகோக்களைப் பயன்படுத்துவது அவர்களின் கொள்கைகளுக்கு உட்பட்டது.

## உதவி பெறுதல்

AI பயன்பாடுகளை உருவாக்குவதில் சிக்கல் ஏற்பட்டால் அல்லது கேள்விகள் இருந்தால், இங்கே சேர்ந்துக்கொள்க:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

பொருள் கருத்துக்களோ அல்லது பிழைகளோ இருந்தால்:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்புரை**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் சரியான மொழிபெயர்ப்பிற்காக முயற்சித்தாலும், தானாக மொழிபெயர்ப்பு செய்ததில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதனை தயவு செய்து கவனிக்கவும். சொந்த நாட்டின் மொழியில் உள்ள அசல் ஆவணத்தை அதிகாரப்பூர்வ வடிவமாக எடுத்துக் கொள்ள வேண்டும். முக்கியமான தகவலுக்காக, தொழில்முறை மனித மொழிபெயர்ப்பை பரிந்துரைக்கிறோம். இந்த மொழிபெயர்ப்பை பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பதிலாக இருக்க மாட்டோம்.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->