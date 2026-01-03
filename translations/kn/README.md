<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef3a50368712b1a7483d0def1f70c490",
  "translation_date": "2025-12-21T15:21:18+00:00",
  "source_file": "README.md",
  "language_code": "kn"
}
-->
# Phi Cookbook: ಪ್ರಾಯೋಗಿಕ ಉದಾಹರಣೆಗಳು ಮೈಕ್ರೋಸಾಫ್ಟ್‌ನ Phi ಮಾದರಿಗಳೊಂದಿಗೆ

[![GitHub Codespaces ನಲ್ಲಿ ಮಾದರಿಗಳನ್ನು ತೆರೆಯಿ ಮತ್ತು ಬಳಸಿರಿ](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers ನಲ್ಲಿ ತೆರೆಯಿರಿ](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub ಕೊಡುಗೆದಾರರು](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ಇಶ್ಯೂಗಳು](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ಪುಲ್-ರಿಕ್ವೆಸ್ಟ್‌ಗಳು](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs ಸ್ವಾಗತ](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub ವೀಕ್ಷಕರು](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ಫೋರ್ಕ್‌ಗಳು](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ಸ್ಟಾರ್ಸ್](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry ಡಿಸ್ಕಾರ್ಡ್](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi ಅನ್ನು ಮೈಕ್ರೋಸಾಫ್ಟ್ ಅಭಿವೃದ್ಧಿಪಡಿಸಿದ ಓಪನ್ ಸೋರ್ಸ್ AI ಮಾದರಿಗಳ ಸರಣಿ ಎಂದು ಪರಿಗಣಿಸಲಾಗಿದೆ.

Phi ಪ್ರಸ್ತುತ ಅತ್ಯಂತ ಶಕ್ತಿಶಾಲಿ ಮತ್ತು ವೆಚ್ಚ-ಪ್ರಭಾವಿ ಸಣ್ಣ ಭಾಷಾ ಮಾದರಿ (SLM) ಆಗಿದ್ದು, ಬಹುಭಾಷಾ, ತರ್ಕ, ಪಠ್ಯ/ಚಾಟ್ ರಚನೆ, ಕೋಡಿಂಗ್, ಚಿತ್ರ, ಆಡಿಯೋ ಮತ್ತು ಇತರ ಸಂದರ್ಭಗಳಲ್ಲಿ ಅತ್ಯುತ್ತಮ ಬೆಂಚ್ಮಾರ್ಕ್ ಫಲಿತಾಂಶಗಳನ್ನು ನೀಡುತ್ತದೆ.

Phi ಅನ್ನು ಕ್ಲೌಡ್ ಅಥವಾ ಎಡ್ಜ್ ಸಾಧನಗಳಿಗೆ ನಿಯೋಜಿಸಬಹುದು, ಮತ್ತು ಸೀಮಿತ ಗಣನ ಶಕ್ತಿಯೊಂದಿಗೆ ಸುಲಭವಾಗಿ ಜನರೇಟಿವ್ AI ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಬಹುದು.

ಈ ಸಂಪನ್ಮೂಲಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಪ್ರಾರಂಭಿಸಲು ಕೆಳಗಿನ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ :
1. **ರಿಪೊಸಿಟರಿಯನ್ನು ಫೋರ್ಕ್ ಮಾಡಿ**: Click [![GitHub ಫೋರ್ಕ್‌ಗಳು](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **ರಿಪೊಸಿಟರಿಯನ್ನು ಕ್ಲೋನ್ ಮಾಡಿ**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord ಸಮುದಾಯಕ್ಕೆ ಸೇರಿ — ತಜ್ಞರು ಮತ್ತು ಇತರ ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರನ್ನು ಭೇಟಿ ಮಾಡಿ**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![ಮುಂಭಾಗ](../../translated_images/cover.eb18d1b9605d754b.kn.png)

### 🌐 ಬಹುಭಾಷಾ ಬೆಂಬಲ

#### GitHub Action ಮೂಲಕ ಬೆಂಬಲಿತ (ಸ್ವಯಂಚಾಲಿತ & ಸದಾ ನವೀಕರಿಸಿದ)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](./README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## ವಿಷಯಸೂಚಿ

- ಪರಿಚಯ
  - [Phi ಕುಟುಂಬಕ್ಕೆ ಸ್ವಾಗತ](./md/01.Introduction/01/01.PhiFamily.md)
  - [ನಿಮ್ಮ ಪರಿಸರವನ್ನು ಹೊಂದಿಸುವುದು](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [ಮುಖ್ಯ ತಂತ್ರಜ್ಞಾನಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi ಮಾದರಿಗಳಿಗಾಗಿ AI ಸುರಕ್ಷತೆ](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ಹಾರ್ಡ್‌ವೇರ್ ಬೆಂಬಲ](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi ಮಾದರಿಗಳು ಮತ್ತು ವಿವಿಧ ವೇದಿಕೆಗಳಲ್ಲಿನ ಲಭ್ಯತೆ](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai ಮತ್ತು Phi ಬಳಸುವುದು](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace Models](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- ವಿಭಿನ್ನ ವಾತಾವರಣಗಳಲ್ಲಿ Phi ಇನ್ಫರೆನ್ಸ್
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub Models](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi ಕುಟುಂಬದಲ್ಲಿ ಇನ್ಫರೆನ್ಸ್
    - [iOS ನಲ್ಲಿ Phi ಇನ್ಫರೆನ್ಸ್](./md/01.Introduction/03/iOS_Inference.md)
    - [Android ನಲ್ಲಿ Phi ಇನ್ಫರೆನ್ಸ್](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson ನಲ್ಲಿ Phi ಇನ್ಫರೆನ್ಸ್](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC ನಲ್ಲಿ Phi ಇನ್ಫರೆನ್ಸ್](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX ಫ್ರೇಮ್ವರ್ಕ್ ಬಳಸಿ Phi ಇನ್ಫರೆನ್ಸ್](./md/01.Introduction/03/MLX_Inference.md)
    - [ಸ್ಥಳೀಯ ಸರ್ವರ್‌ನಲ್ಲಿ Phi ಇನ್ಫರೆನ್ಸ್](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit ಬಳಸಿ ದೂರದ ಸರ್ವರ್‌ನಲ್ಲಿ Phi ಇನ್ಫರೆನ್ಸ್](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust ಬಳಸಿ Phi ಇನ್ಫರೆನ್ಸ್](./md/01.Introduction/03/Rust_Inference.md)
    - [ಸ್ಥಳೀಯ Vision ನಲ್ಲಿ Phi ಇನ್ಫರೆನ್ಸ್](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers(ಅಧಿಕೃತ ಬೆಂಬಲ) ಬಳಸಿ Phi ಇನ್ಫರೆನ್ಸ್](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi ಕುಟುಂಬದ ಪ್ರಮಾಣೀಕರಣ](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ಬಳಸಿ Phi-3.5 / 4 ಅನ್ನು ಪ್ರಮಾಣೀಕರಿಸುವುದು](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime ಗಾಗಿ Generative AI ವಿಸ್ತರಣೆಗಳನ್ನು ಬಳಸಿ Phi-3.5 / 4 ಅನ್ನು ಪ್ರಮಾಣೀಕರಿಸುವುದು](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ಬಳಸಿ Phi-3.5 / 4 ಅನ್ನು ಪ್ರಮಾಣೀಕರಿಸುವುದು](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX ಫ್ರೇಮ್ವರ್ಕ್ ಬಳಸಿ Phi-3.5 / 4 ಅನ್ನು ಪ್ರಮಾಣೀಕರಿಸುವುದು](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi ಮೌಲ್ಯಮಾಪನ
    - [ದಾಯಿತ್ವಪೂರ್ಣ AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [ಮೌಲ್ಯಮಾಪನಕ್ಕೆ Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [ಮೌಲ್ಯಮಾಪನಕ್ಕಾಗಿ Promptflow ಬಳಸುವುದು](./md/01.Introduction/05/Promptflow.md)
 
- RAG ಅನ್ನು Azure AI Search ಜೊತೆ ಬಳಸುವುದು
    - [Phi-4-mini ಮತ್ತು Phi-4-multimodal(RAG) ಅನ್ನು Azure AI Search ಜೊತೆ ಹೇಗೆ ಬಳಸುವುದು](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi ಅಪ್ಲಿಕೇಶನ್ ಅಭಿವೃದ್ಧಿ ಉದಾಹರಣೆಗಳು
  - ಪಠ್ಯ ಮತ್ತು ಚಾಟ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳು
    - Phi-4 ಉದಾಹರಣೆಗಳು 🆕
      - [📓] [Phi-4-mini ONNX ಮಾದರಿಯೊಂದಿಗೆ ಚಾಟ್](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [ಸ್ಥಳೀಯ Phi-4 ONNX ಮಾದರಿಯೊಂದಿಗೆ ಚಾಟ್ (.NET)](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Semantic Kernel ಬಳಸಿ Phi-4 ONNX ಜೊತೆ .NET ಕನ್‌ಸೋಲ್ ಅಪ್ಲಿಕೇಶನ್](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 ಉದಾಹರಣೆಗಳು
      - [ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಸ್ಥಳೀಯ ಚಾಟ್‌ಬಾಟ್ — Phi3, ONNX Runtime Web ಮತ್ತು WebGPU ಬಳಸಿ](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino ಚಾಟ್](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [ಬಹು ಮಾದರಿ - ಇಂಟರ್ಯಾಕ್ಟಿವ್ Phi-3-mini ಮತ್ತು OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ರಾಪರ್ ನಿರ್ಮಿಸಿ ಮತ್ತು MLFlow ಜೊತೆಗೆ Phi-3 ಬಳಸಿ](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Model Optimization - Olive ಬಳಸಿ ONNX Runtime Web ಗೆ Phi-3-min ಮಾದರಿಯನ್ನು ಹೇಗೆ ಆಪ್ಟಿಮೈಸ್ ಮಾಡುವುದು](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 ಅಪ್ಲಿಕೇಶನ್ Phi-3 mini-4k-instruct-onnx ಜೊತೆಗೆ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 ಬಹು-ಮಾದರಿ AI ಚಾಲಿತ ನೋಟ್ಸ್ ಅಪ್ಲಿಕೇಶನ್ ಮಾದರಿ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Prompt flow ಜೊತೆ ಕಸ್ಟಮ್ Phi-3 ಮಾದರಿಗಳನ್ನು ಫೈನ್‑ಟ್ಯೂನ್ ಮಾಡಿ ಮತ್ತು ಏಕೀಕರಿಸುವುದು](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry ನಲ್ಲಿ Prompt flow ಮೂಲಕ ಕಸ್ಟಮ್ Phi-3 ಮಾದರಿಗಳನ್ನು ಫೈನ್‑ಟ್ಯೂನ್ ಮತ್ತು ಏಕೀಕರಿಸುವುದು](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft ನ Responsible AI ತತ್ವಗಳನ್ನು ಗಮನದಲ್ಲಿ ಇಡಿ Azure AI Foundry ನಲ್ಲಿ ಫೈನ್‑ಟ್ಯೂನ್ ಮಾಡಿದ Phi-3 / Phi-3.5 ಮಾದರಿಯನ್ನು ಮೌಲ್ಯಮಾಪನ ಮಾಡಿ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct ಭಾಷಾ ಭವಿಷ್ಯ ನಿರ್ಧಾರ ಉದಾಹರಣೆ (Chinese/English)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG ಚಾಟ್‌ಬಾಟ್](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU ಬಳಸಿ Phi-3.5-Instruct ONNX ಜೊತೆಗೆ Prompt flow ಪರಿಹಾರ ರಚಿಸುವುದು](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite ಬಳಸಿ Android ಅಪ್ಲಿಕೇಶನ್ ರಚಿಸುವುದು](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime ಬಳಸಿ ಸ್ಥಳೀಯ ONNX Phi-3 ಮಾದರಿಯನ್ನು ಬಳಸುವ Q&A .NET ಉದಾಹರಣೆ](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel ಮತ್ತು Phi-3 ಬಳಸಿ Console ಚಾಟ್ .NET ಅಪ್ಲಿಕೇಶನ್](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK Code Based Samples 
    - Phi-4 ಉದಾಹರಣೆಗಳು 🆕
      - [📓] [Phi-4-multimodal ಬಳಸಿ ಪ್ರಾಜೆಕ್ಟ್ ಕೋಡ್ ರಚಿಸುವುದು](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 ಉದಾಹರಣೆಗಳು
      - [Microsoft Phi-3 Family ಮೂಲಕ ನಿಮ್ಮದೇ Visual Studio Code GitHub Copilot Chat ಅನ್ನು ನಿರ್ಮಿಸಿ](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub Models ಮೂಲಕ Phi-3.5 ಬಳಸಿ ನಿಮ್ಮದೇ Visual Studio Code Chat Copilot ಏಜೆಂಟ್ ರಚಿಸಿ](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - ಉನ್ನತ ತರ್ಕದ ಉದಾಹರಣೆಗಳು
    - Phi-4 ಉದಾಹರಣೆಗಳು 🆕
      - [📓] [Phi-4-mini-reasoning ಅಥವಾ Phi-4-reasoning ಉದಾಹರಣೆಗಳು](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive ಬಳಸಿ Phi-4-mini-reasoning ಅನ್ನು ಫೈನ್-ಟ್ಯೂನ್ ಮಾಡುವುದು](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX ಬಳಸಿ Phi-4-mini-reasoning ಅನ್ನು ಫೈನ್-ಟ್ಯೂನ್ ಮಾಡುವುದು](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub Models ಜೊತೆಗೆ Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry Models ಜೊತೆಗೆ Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demos
      - [Phi-4-mini ಡೆಮೊಗಳು Hugging Face Spaces ನಲ್ಲಿ ಹೋಸ್ಟ್ ಆಗಿವೆ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal ಡೆಮೊಗಳು Hugginge Face Spaces ನಲ್ಲಿ ಹೋಸ್ಟ್ ಆಗಿವೆ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Vision Samples
    - Phi-4 ಉದಾಹರಣೆಗಳು 🆕
      - [📓] [ಚಿತ್ರಗಳನ್ನು ಓದಲು ಮತ್ತು ಕೋಡ್ ರಚಿಸಲು Phi-4-multimodal ಅನ್ನು ಬಳಸಿರಿ](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 ಉದಾಹರಣೆಗಳು
      -  [📓][Phi-3-vision — ಚಿತ್ರ ಪಠ್ಯದಿಂದ ಪಠ್ಯಕ್ಕೆ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP ಎಂಬೆಡ್ಡಿಂಗ್](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ಡೇಮೊ: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - ದೃಶ್ಯ ಭಾಷಾ ಸಹಾಯಕ - Phi3-Vision ಮತ್ತು OpenVINO ಜೊತೆಗೆ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision ಬಹು-ಫ್ರೇಮ್ ಅಥವಾ ಬಹು-ಇಮೇಜ್ ಉದಾಹರಣೆ](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision ಸ್ಥಳೀಯ ONNX ಮಾದರಿಯನ್ನು Microsoft.ML.OnnxRuntime .NET ಬಳಸಿ](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [ಮೆನು ಆಧಾರಿತ Phi-3 Vision ಸ್ಥಳೀಯ ONNX ಮಾದರಿಯನ್ನು Microsoft.ML.OnnxRuntime .NET ಬಳಸಿ](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Math Samples
    -  Phi-4-Mini-Flash-Reasoning-Instruct ಉದಾಹರಣೆಗಳು 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct ಜೊತೆಗೆ ಗಣಿತ ಡೆಮೊ](./md/02.Application/09.Math/MathDemo.ipynb)

  - Audio Samples
    - Phi-4 ಉದಾಹರಣೆಗಳು 🆕
      - [📓] [Phi-4-multimodal ಬಳಸಿ ಆಡಿಯೋ ಟ್ರಾನ್ಸ್ಕ್ರಿಪ್ಟ್ ತೆಗೆಯುವುದು](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal ಆಡಿಯೋ ಉದಾಹರಣೆ](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal ಮಾತನಾಡುವ ಭಾಷೆ ಅನುವಾದ ಉದಾಹರಣೆ](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET ಕನ್ಸೋಲ್ ಅಪ್ಲಿಕೇಶನ್ Phi-4-multimodal ಬಳಸಿ ಆಡಿಯೋ ಫೈಲ್ ವಿಶ್ಲೇಷಿಸಿ ಟ್ರಾನ್ಸ್ಕ್ರಿಪ್ಟ್ ರಚಿಸಲು](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE Samples
    - Phi-3 / 3.5 ಉದಾಹರಣೆಗಳು
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) ಸಾಮಾಜಿಕ ಮಾಧ್ಯಮ ಉದಾಹರಣೆ](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, ಮತ್ತು LlamaIndex ಜೊತೆಗೆ Retrieval-Augmented Generation (RAG) ಪೈಪ್‌ಲೈನ್ ನಿರ್ಮಿಸುವುದು](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Function Calling Samples
    - Phi-4 ಉದಾಹರಣೆಗಳು 🆕
      -  [📓] [Phi-4-mini ಜೊತೆ Function Calling ಬಳಸು](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Function Calling ಬಳಸಿ Phi-4-mini ಜೊತೆಗೆ ಬಹು-ಏಜೆಂಟ್ ಗಳು ರಚಿಸುವುದು](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama ಜೊತೆ Function Calling ಬಳಕೆ](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX ಜೊತೆ Function Calling ಬಳಕೆ](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Multimodal Mixing Samples
    - Phi-4 ಉದಾಹರಣೆಗಳು 🆕
      -  [📓] [Phi-4-multimodal ಅನ್ನು ಟೆಕ್ನಾಲಜಿ ಪತ್ರಕರ್ತನಂತೆ ಬಳಸುವುದು](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET ಕನ್ಸೋಲ್ ಅಪ್ಲಿಕೇಶನ್ Phi-4-multimodal ಬಳಸಿ ಚಿತ್ರಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಲು](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi ಫೈನ್-ಟ್ಯೂನಿಂಗ್ ಉದಾಹರಣೆಗಳು
  - [ಫೈನ್-ಟ್ಯೂನಿಂಗ್ ದೃಶ್ಯಗಳು](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ಫೈನ್-ಟ್ಯೂನಿಂಗ್ ವಿರುದ್ಧ RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [ಫೈನ್-ಟ್ಯೂನಿಂಗ್ — Phi-3 ಅನ್ನು ಉದ್ಯಮ ತಜ್ಞನಾಗಿ ಮಾಡಿ](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [AI Toolkit for VS Code ಬಳಸಿ Phi-3 ಫೈನ್-ಟ್ಯೂನಿಂಗ್](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service ಬಳಸಿ Phi-3 ಫೈನ್-ಟ್ಯೂನಿಂಗ್](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora ಬಳಸಿ Phi-3 ಫೈನ್-ಟ್ಯೂನಿಂಗ್](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora ಬಳಸಿ Phi-3 ಫೈನ್-ಟ್ಯೂನಿಂಗ್](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry ಬಳಸಿ Phi-3 ಫೈನ್-ಟ್ಯೂನಿಂಗ್](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK ಬಳಸಿ Phi-3 ಫೈನ್-ಟ್ಯೂನಿಂಗ್](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive ಬಳಸಿ ಫೈನ್-ಟ್ಯೂನಿಂಗ್](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive ಪ್ರಾಯೋಗಿಕ ಲ್ಯಾಬ್ ಜೊತೆ ಫೈನ್-ಟ್ಯೂನಿಂಗ್](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias ಬಳಸಿ Phi-3-vision ಫೈನ್-ಟ್ಯೂನಿಂಗ್](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework ಬಳಸಿ Phi-3 ಫೈನ್-ಟ್ಯೂನಿಂಗ್](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision ಫೈನ್-ಟ್ಯೂನಿಂಗ್ (ಆಧಿಕೃತ ಬೆಂಬಲ)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS , Azure Containers(ಆಧಿಕೃತ ಬೆಂಬಲ) ಬಳಸಿ Phi-3 ಫೈನ್-ಟ್ಯೂನಿಂಗ್](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 ಮತ್ತು 3.5 Vision ಫೈನ್-ಟ್ಯೂನಿಂಗ್](https://github.com/2U1/Phi3-Vision-Finetune)

- ಹ್ಯಾಂಡ್ಸ್ ಆನ್ ಲ್ಯಾಬ್
  - [ಅತ್ಯಾಧುನಿಕ ಮಾದರಿಗಳನ್ನು ಅನ್ವೇಶಿಸಿ: LLMs, SLMs, ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿ ಮತ್ತು ಇನ್ನಷ್ಟು](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP ಸಾಮರ್ಥ್ಯವನ್ನು ಅನ್ಲಾಕ್ ಮಾಡಿ: Microsoft Olive ಬಳಸಿ ಫೈನ್-ಟ್ಯೂನಿಂಗ್](https://github.com/azure/Ignite_FineTuning_workshop)

- ಅಕಾಡೆಮಿಕ್ ಸಂಶೋಧನಾ ಪತ್ರಿಕೆಗಳು ಮತ್ತು ಪ್ರಕಟಣೆಗಳು
  - [Textbooks Are All You Need II: phi-1.5 ತಾಂತ್ರಿಕ ವರದಿ](https://arxiv.org/abs/2309.05463)
  - [Phi-3 ತಾಂತ್ರಿಕ ವರದಿ: ನಿಮ್ಮ ಫೋನಿನಲ್ಲಿ ಸ್ಥಳೀಯವಾಗಿ ಅತ್ಯಂತ ಸಾಮರ್ಥ್ಯಯುಕ್ತ ಭಾಷಾ ಮಾದರಿ](https://arxiv.org/abs/2404.14219)
  - [Phi-4 ತಾಂತ್ರಿಕ ವರದಿ](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini ತಾಂತ್ರಿಕ ವರದಿ: Mixture-of-LoRAs ಮೂಲಕ ಸಂಕ್ಷಿಪ್ತ ಆದರೆ ಶಕ್ತಿಶಾಲಿ ಬಹುಮಾಧ್ಯಮ ಭಾಷಾ ಮಾದರಿಗಳು](https://arxiv.org/abs/2503.01743)
  - [ವಾಹನದೊಳಗಿನ ಫಂಕ್ಷನ್-ಕಾಲ್‌ಗಾಗಿ ಸಣ್ಣ ಭಾಷಾ ಮಾದರಿಗಳ ಕೌಶಲ್ಯವರ್ಧನೆ](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 ಅನ್ನು ಬಹು ಆಯ್ಕೆ ಪ್ರಶ್ನೋತ್ತರಕ್ಕಾಗಿ ಫೈನ್-ಟ್ಯೂನಿಂಗ್: ವಿಧಾನಶಾಸ್ತ್ರ, ಫಲಿತಾಂಶಗಳು ಮತ್ತು ಸವಾಲುಗಳು](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning ತಾಂತ್ರಿಕ ವರದಿ](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning ತಾಂತ್ರಿಕ ವರದಿ](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi ಮಾದರಿಗಳನ್ನು ಬಳಸುವುದು

### Azure AI Foundry ನಲ್ಲಿ Phi

Microsoft Phi ಅನ್ನು ಹೇಗೆ ಬಳಸಬೇಕು ಮತ್ತು ನಿಮ್ಮ ವಿಭಿನ್ನ ಹಾರ್ಡ್‌ವೇರ್ ಸಾಧನಗಳಲ್ಲಿ E2E ಪರಿಹಾರಗಳನ್ನು ಹೇಗೆ ನಿರ್ಮಿಸಬೇಕು ಎಂದು ನೀವು ಕಲಿಯಬಹುದು. Phi ಅನ್ನು ನೇರವಾಗಿ ಅನುಭವಿಸಲು, ಮೊದಲು ಮಾದರಿಗಳೊಂದಿಗೆ ಪ್ರಯೋಗ ಮಾಡಿ ಮತ್ತು ನಿಮ್ಮ ದೃಶ್ಯಗಳಿಗೆ ಅನುಗುಣವಾಗಿ Phi ಅನ್ನು ಕಸ್ಟಮೈಸ್ ಮಾಡಿ, [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ಬಳಸಿ. ಇನ್ನಷ್ಟು ತಿಳಿಯಲು Getting Started with [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) ಅನ್ನು ನೋಡಿ.

**Playground**
ಪ್ರತಿ ಮಾದರಿಗೆ ಮಾದರಿಯನ್ನು ಪರೀಕ್ಷಿಸಲು ಒಂದು ಸಮರ್ಪಿತ ಪ್ಲೇಗ್ರೌಂಡ್ ಇದೆ [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub Models ನಲ್ಲಿ Phi

Microsoft Phi ಅನ್ನು ಹೇಗೆ ಬಳಸಬೇಕು ಮತ್ತು ನಿಮ್ಮ ವಿಭಿನ್ನ ಹಾರ್ಡ್‌ವೇರ್ ಸಾಧನಗಳಲ್ಲಿ E2E ಪರಿಹಾರಗಳನ್ನು ಹೇಗೆ ನಿರ್ಮಿಸಬೇಕು ಎಂದು ನೀವು ಕಲಿಯಬಹುದು. Phi ಅನ್ನು ನೇರವಾಗಿ ಅನುಭವಿಸಲು, ಮೊದಲು ಮಾದರಿಯನ್ನು ಪ್ರಯೋಗಿಸಿ ಮತ್ತು ನಿಮ್ಮ ದೃಶ್ಯಗಳಿಗೆ ಅನುಗುಣವಾಗಿ Phi ಅನ್ನು ಕಸ್ಟಮೈಸ್ ಮಾಡಲು [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ಬಳಸಿ. ಇನ್ನಷ್ಟು ತಿಳಿಯಲು Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) ಅನ್ನು ನೋಡಿ.

**Playground**
ಪ್ರತಿ ಮಾದರಿಗೆ ಮಾದರಿಯನ್ನು ಪರೀಕ್ಷಿಸಲು ಒಂದು ಸಮರ್ಪಿತ [ಪ್ಲೇಗ್ರೌಂಡ್](/md/02.QuickStart/GitHubModel_QuickStart.md) ಇದೆ.

### Hugging Face ನಲ್ಲಿ Phi

ನೀವು ಮಾದರಿಯನ್ನು [Hugging Face](https://huggingface.co/microsoft) ನಲ್ಲಿ ಕೂಡ ಹುಡುಕಬಹುದು

**Playground**
 [Hugging Chat ಪ್ಲೇಗ್ರೌಂಡ್](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 ಇತರ ಪಾಠ್ಯಕ್ರಮಗಳು

ನಮ್ಮ ತಂಡ ಅನ್ಯ ಕೋರ್ಸ್‌ಗಳನ್ನು ಉತ್ಪಾದಿಸುತ್ತದೆ! ಪರಿಶೀಲಿಸಿ:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j ಪ್ರಾರಂಭಿಕರಿಗಾಗಿ](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js ಪ್ರಾರಂಭಿಕರಿಗಾಗಿ](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / ಏಜೆಂಟ್ಸ್
[![AZD ಪ್ರಾರಂಭಿಕರಿಗಾ](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI ಪ್ರಾರಂಭಿಕರಿಗಾಗಿ](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP ಪ್ರಾರಂಭಿಕರಿಗಾಗಿ](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI ಏಜೆಂಟ್ಸ್ ಪ್ರಾರಂಭಿಕರಿಗಾಗಿ](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### ಜನರೇಟಿವ್ AI ಸರಣಿ
[![ಜನರೇಟಿವ್ AI ಪ್ರಾರಂಭಿಕರಿಗಾಗಿ](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![ಜನರೇಟಿವ್ AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![ಜನರೇಟಿವ್ AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![ಜನರೇಟಿವ್ AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### ಮೂಲ ಅಧ್ಯಯನ
[![ML ಪ್ರಾರಂಭಿಕರಿಗಾಗಿ](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![ಡೇಟಾ ಸೈನ್ಸ್ ಪ್ರಾರಂಭಿಕರಿಗಾಗಿ](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI ಪ್ರಾರಂಭಿಕರಿಗಾಗಿ](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![ಸೈಬರ್‌ಸುರಕ್ಷತೆ ಪ್ರಾರಂಭಿಕರಿಗಾಗಿ](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![ವೆಬ್ ಡೆವ್ ಪ್ರಾರಂಭಿಕರಿಗಾಗಿ](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT ಪ್ರಾರಂಭಿಕರಿಗಾಗಿ](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR ಡೆವಲಪ್‌ಮೆಂಟ್ ಪ್ರಾರಂಭಿಕರಿಗಾಗಿ](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot ಸರಣಿ
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET ಗಾಗಿ Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot ಸಾಹಸ](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## ಜವಾಬ್ದಾರಿಯಾದ AI 

Microsoft ನಮ್ಮ ಗ್ರಾಹಕರು ನಮ್ಮ AI ಉತ್ಪನ್ನಗಳನ್ನು ಜವಾಬ್ದಾರಿಯಾಗಿ ಬಳಸಲು ಸಹಾಯ ಮಾಡುವುದಕ್ಕೆ, ನಮ್ಮ ಕಲಿತಿಕೆಗಳನ್ನು ಹಂಚಿಕೊಳ್ಳಲು ಮತ್ತು Transparency Notes ಮತ್ತು Impact Assessmentsಂತಹ ಉಪಕರಣಗಳ ಮೂಲಕ ನಂಬಿಕೆಯಿಂದ ಆಧಾರಿತ ಸಹಭಾಗಿತ್ವಗಳನ್ನು ನಿರ್ಮಿಸಲು ಬದ್ಧವಾಗಿದೆ. ಈ ಸಂಪನ್ಮೂಲಗಳ ಬಹುತೇಕವನ್ನು [https://aka.ms/RAI](https://aka.ms/RAI) ನಲ್ಲಿ ನೀವು ಕಾಣಬಹುದು.
Microsoftನ ಜವಾಬ್ದಾರಿಯಾದ AI ಗೆ ಹೊಂದಿಕೊಳ್ಳುವ ದೃಷ್ಟಿಕೋನವು ನ್ಯಾಯತೆ, ವಿಶ್ವಾಸಾರ್ಹತೆ ಮತ್ತು ಸುರಕ್ಷತೆ, ಗೌಪ್ಯತೆ ಮತ್ತು ಭದ್ರತೆ, ಸಮಾವೇಶತೆ, ಪಾರದರ್ಶಕತೆ ಮತ್ತು ಹಣೆಗಾರಿಕೆಯನ್ನು ಆಧರಿಸಿದೆ.

ಈ ಉದಾಹರಣೆಯಲ್ಲಿ ಬಳಸಿದದಂಥ ದೊಡ್ಡ ಪ್ರಮಾಣದ ನೈಸರ್ಗಿಕ ಭಾಷೆ, ಚಿತ್ರ ಮತ್ತು ವಾಣಿ ಮಾದರಿಗಳು ಅನ್ಯಾಯಕರ, ಅಸ್ಥಿರ ಅಥವಾ ಅಪಮಾನಕಾರಿ ರೀತಿಯಲ್ಲಿ ವರ್ತಿಸಬಹುದು, ಪರಿಣಾಮವಾಗಿ ಹಾನಿ ಉಂಟಾಗಬಹುದು. ಅಪಾಯಗಳು ಮತ್ತು ಮಿತಿಗಳನ್ನು ತಿಳಿಯಲು ದಯವಿಟ್ಟು [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ಅನ್ನು ಪರಿಶೀಲಿಸಿ.

ಈ ಅಪಾಯಗಳನ್ನು ಕಡಿಮೆ ಮಾಡುವ ಶಿಫಾರಸು ಮಾಡಿದ ವಿಧಾನವೆಂದರೆ ನಿಮ್ಮ ಆರ್ಕಿಟೆಕ್ಚರ್‌ನಲ್ಲಿ ಹಾನಿಕಾರಕ ವರ್ತನನ್ನು ಪತ್ತೆಹಚ್ಚಿ ತಡೆಗಟ್ಟಬಲ್ಲ ಸುರಕ್ಷತಾ ವ್ಯವಸ್ಥೆಯನ್ನು ಒಳಗೆ ಸೇರಿಸುವುದು. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ಅಪ್ಲಿಕೇಶನ್‌ಗಳು ಮತ್ತು ಸೇವೆಗಳಲ್ಲಿ ಬಳಕೆದಾರರು ರಚಿಸಿದ ಮತ್ತು AI ರಚಿಸಿದ ಹಾನಿಕಾರಕ ವಿಷಯವನ್ನು ಪತ್ತೆಹಚ್ಚಲು ಸಮರ್ಥವಾದ ಸ್ವತಂತ್ರ ರಕ್ಷಣಾ ಪದರವನ್ನು ಒದಗಿಸುತ್ತದೆ. Azure AI Content Safety ನಲ್ಲಿ ಪಠ್ಯ ಮತ್ತು ಚಿತ್ರ API ಗಳು ಸೇರಿವೆ, ಇವುಗಳ ಮೂಲಕ ನೀವು ಹಾನಿಕಾರಕ ವಿಷಯವನ್ನು ಪತ್ತೆಹಚ್ಚಬಹುದು. Azure AI Foundry ಒಳಗೆ, Content Safety ಸೇವೆ ವಿಭಿನ್ನ ಮೋಡಾಲಿಟಿಗಳಲ್ಲಿನ ಹಾನಿಕಾರಕ ವಿಷಯವನ್ನು ಪತ್ತೆಹಚ್ಚಲು ಮಾದರಿ ಕೋಡ್ ಅನ್ನು ವೀಕ್ಷಿಸಲು, ಅನ್ವೇಷಿಸಲು ಮತ್ತು ಪ್ರಯೋಗಿಸಲು ಅನುಮತಿಸುತ್ತದೆ. ಕೆಳಗಿನ [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ನಿಮಗೆ ಸೇವೆಗೆ ವಿನಂತಿಗಳನ್ನು ಹೇಗೆ ಮಾಡುವುದನ್ನು ಮಾರ್ಗದರ್ಶನ ಮಾಡುತ್ತದೆ.

ಗಣನೆಗೆ ಇನ್ನೊಂದು ಪರಿಗಣಿಸಬೇಕಾದ ಅಂಶವೆಂದರೆ ಒಟ್ಟು ಅಪ್ಲಿಕೇಶನ್ ಕಾರ್ಯಕ್ಷಮತೆ. ಬಹು-ಮೋಡಾಲಿಟಿ ಮತ್ತು ಬಹು-ಮಾದರಿ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಲ್ಲಿ, ಕಾರ್ಯಕ್ಷಮತೆಯ ಅರ್ಥವೆಂದರೆ ಸಿಸ್ಟಮ್ ನಿಮ್ಮ ಮತ್ತು ನಿಮ್ಮ ಬಳಕೆದಾರರ ನಿರೀಕ್ಷೆಗನುಗುಣವಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸಬೇಕು, ಹಾನಿಕಾರಕ outputs ರಚಿಸದೇ ಇರುವುದೂ ಸೇರಿದೆ. ನಿಮ್ಮ ಒಟ್ಟು ಅಪ್ಲಿಕೇಶನ್ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಅಂದಾಜಿಸಲು [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ಬಳಸುವುದು ಮುಖ್ಯ. ನೀವು [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) ಅನ್ನು ರಚಿಸಿ ಮೌಲ್ಯಮಾಪನ ಮಾಡುವ ಸಾಮರ್ಥ್ಯವೂ ಹೊಂದಿದ್ದೀರಿ.

ನೀವು [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ಅನ್ನು ಬಳಸಿಕೊಂಡು ನಿಮ್ಮ ಡೆವಲಪ್‌ಮೆಂಟ್ ಪರಿಸರದಲ್ಲಿ ನಿಮ್ಮ AI ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಮೌಲ್ಯಮಾಪನ ಮಾಡಬಹುದು. ಪರೀಕ್ಷಾ ಡೇಟಾಸೆಟ್ ಅಥವಾ ಗುರಿಯನ್ನು ನೀಡಿದಾಗ, ನಿಮ್ಮ ಜನರೇಟಿವ್ AI ಅಪ್ಲಿಕೇಶನ್ ಉದ್ದಿಗಳನ್ನು встроенные ಏವ್ಯಾಲ್ಯುಯೇಟರ್‌ಗಳು ಅಥವಾ ನಿಮ್ಮ ಆಯ್ಕೆಯ ಕಸ್ಟಮ್ ಏವ್ಯಾಲ್ಯುಯೇಟರ್‌ಗಳೊಂದಿಗೆ ಪ್ರಮಾಣಾತ್ಮಕವಾಗಿ ಅಳೆಯುತ್ತದೆ. ನಿಮ್ಮ ಸಿಸ್ಟಮ್ ಅನ್ನು ಮೌಲ್ಯಮಾಪನ ಮಾಡಲು Azure AI Evaluation SDK ಮೂಲಕ ಪ್ರಾರಂಭಿಸಲು, ನೀವು [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ಅನ್ನು ಅನುಸರಿಸಬಹುದು. ಒಂದು ಮೌಲ್ಯಮಾಪನ ರನ್ ಅನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿದ ನಂತರ, ನೀವು [visualize the results in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) ನಲ್ಲಿ ಫಲಿತಾಂಶಗಳನ್ನು ದೃಶ್ಯೀಕರಿಸಬಹುದು. 

## ಟ್ರೇಡ್‌ಮಾರ್ಕ್‌ಗಳು
ಈ ಯೋಜನೆ ಪ್ರಾಜೆಕ್ಟ್‌ಗಳು, ಉತ್ಪನ್ನಗಳು, ಅಥವಾ ಸೇವೆಗಳಿಗೆ ಸಂಬಂಧಿಸಿದ ಟ್ರೇಡ್‌ಮಾರ್ಕ್‌ಗಳು ಅಥವಾ ಲೋಗೋಗಳನ್ನು ಒಳಗೊಂಡಿರಬಹುದು. Microsoft ಟ್ರೇಡ್‌ಮಾರ್ಕ್‌ಗಳು ಅಥವಾ ಲೋಗೋಗಳ ಅನುಮೋದಿತ ಬಳಕೆ [Microsoft ಟ್ರೇಡ್‌ಮಾರ್ಕ್ ಮತ್ತು ಬ್ರ್ಯಾಂಡ್ ಮಾರ್ಗದರ್ಶಿಗಳು](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) ಗೆ ಅನ್ವಯವಾಗುತ್ತದೆ ಮತ್ತು ಅವನ್ನು ಅನುಸರಿಸಬೇಕು.
ಈ ಯೋಜನೆಯ ಬದಲಾವಣೆಗೊಳಿಸಿದ ಆವೃತ್ತಿಗಳಲ್ಲಿ Microsoft ಟ್ರೇಡ್‌ಮಾರ್ಕ್‌ಗಳು ಅಥವಾ ಲೋಗೋಗಳನ್ನು ಬಳಸುವುದು ಗೊಂದಲ ಉಂಟುಮಾಡಬಾರದು ಅಥವಾ Microsoft ಪ್ರಾಯೋಜನೆಯನ್ನು ಸೂಚಿಸಬಾರದು. ತೃತೀಯ ಪಕ್ಷಗಳ ಟ್ರೇಡ್‌ಮಾರ್ಕ್‌ಗಳು ಅಥವಾ ಲೋಗೋಗಳ ಯಾವುದೇ ಬಳಕೆಯು ಆ ತೃತೀಯ ಪಕ್ಷಗಳ ನೀತಿಗಳ ವ್ಯಾಪ್ತಿಗೆ ಒಳಗಾಗುತ್ತದೆ.

## ಸಹಾಯ

AI ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವಲ್ಲಿ ನೀವು ಅಡಗಿದರೆ ಅಥವಾ ಯಾವುದೇ ಪ್ರಶ್ನೆಗಳಿದ್ದರೆ, ಸೇರಿ:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

ಉತ್ಪನ್ನದ ಪ್ರತಿಕ್ರಿಯೆ ಅಥವಾ ನಿರ್ಮಿಸುವಾಗ ದೋಷಗಳು ಕಂಡುಬಂದರೆ, ಭೇಟಿ ನೀಡಿ:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಜವಾಬ್ದಾರಿ ನಿರಾಕರಣೆ:
ಈ ದસ્તಾವೇಜನ್ನು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ದತೆಗಾಗಿ ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿನ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಪ್ರಾಧಿಕಾರಮಯ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ನಿರ್ಣಾಯಕ ಮಾಹಿತಿಗಳಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಗ್ರಹಿಕೆಗಳು ಅಥವಾ ತಪ್ಪಾಗಿ ವ್ಯಾಖ್ಯಾನಗೊಂಡಿರುವುದಕ್ಕಾಗಿ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->