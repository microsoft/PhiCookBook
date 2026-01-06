<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2e4b490f4bd424b095f21e38c6af33b",
  "translation_date": "2026-01-05T15:01:32+00:00",
  "source_file": "README.md",
  "language_code": "ml"
}
-->
# Phi കുക്ക്‌ബുക്ക്: മൈക്രോസോഫ്റ്റിന്റെ Phi മോഡലുകളുമായി കൈകാര്യം ചെയ്യുന്ന ഉദാഹരണങ്ങൾ

[![GitHub കോഡ്സ്പേസുകളിൽ സാമ്പിളുകൾ തുറക്കാനും ഉപയോഗിക്കാനും](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers-ൽ തുറക്കുക](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub സംഭാവനക്കാർ](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub പ്രശ്നങ്ങൾ](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub പുൾ-റിക്വസ്റ്റുകൾ](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![പുൾ-റിക്വസ്റ്റുകൾ സ്വാഗതം](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub വാച്ചേഴ്സ്](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ഫോർക്കുകൾ](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub സ്റ്റോർസ്](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi മൈക്രോസോഫ്റ്റ് വികസിപ്പിച്ച ഒരു open source AI മോഡലുകളുടെ പരമ്പരയാണ്.

Phi നിലവിൽ ഏറ്റവും શક്തമായും ചെലവ് കാര്യക്ഷമവുമായ ചെറിയ ഭാഷ മോഡലാണ് (SLM), അത് വിവിധ ഭാഷകളിൽ, ആധികാരിക ചിന്തನೆ, 텍സ്റ്റു/ചാറ്റ് സൃഷ്ടി, കോഡിംഗ്, ചിത്രങ്ങൾ, ഓഡിയോ തുടങ്ങിയ വാനരൂപങ്ങളിൽ മികച്ച ബെഞ്ച്മാർക്കുകൾ കാണിക്കുന്നു.

Phi-യെ ക്ലൗഡിലോ എജ്ജ് ഉപകരണങ്ങളിലോ വിന്യസിക്കാവുന്നതാണ്, കൂടാതെ അനേകം കംപ്യൂട്ടിംഗ് ശേഷിയുള്ളതിനാൽ ലളിതമായി ജനനാത്മക AI ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കാം.

ഈ വിഭവങ്ങൾ ഉപയോഗിച്ച് ആരംഭിക്കാൻ ഈ ഘട്ടങ്ങൾ പിന്തുടരുക:
1. **റിപ്പോസിറ്ററി ഫോർക്ക് ചെയ്യുക**: ക്ലിക്ക് ചെയ്യുക [![GitHub ഫോർക്കുകൾ](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **റിപ്പോസിറ്ററി ക്ലോണുചെയ്യുക**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord സമൂഹത്തിൽ ചേരുക, വിദഗ്ദ്ധരെയും സഹ-വികസകരെയും കണ്ടുമുട്ടുക**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.eb18d1b9605d754b.ml.png)

### 🌐 ബഹുഭാഷാ പിന്തുണ

#### GitHub ആക്ഷൻ വഴി സഹായിപ്പിക്കപ്പെടുന്നു (ഓട്ടോമേറ്റഡ് & എല്ലായ്പ്പോഴും അപ്-ടു-ഡേറ്റ്)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](./README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **പ്രാദേശികമായി ക്ലോൺ ചെയ്യാൻ ഇഷ്ടപ്പെടുന്നുണ്ടോ?**

> ഈ റിപ്പോസിറ്ററിയിൽ 50+ ഭാഷാ വിവർത്തനങ്ങൾ ഉൾക്കൊള്ളുന്നു, ഇത് ഡൗൺലോഡ് വലുപ്പം വൻതോതിൽ വർദ്ധിപ്പിക്കുന്നു. വിവർത്തനങ്ങൾ ഇല്ലാതെ ക്ലോൺ ചെയ്യാൻ sparse checkout ഉപയോഗിക്കുക:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> കോഴ്സ് പൂർത്തിയാക്കാൻ വേണ്ടതെല്ലാം വളരെ വേഗത്തിൽ ലഭിക്കുന്നതാണ്.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## ഉള്ളടക്ക പട്ടിക

- പരിചയം
  - [Phi കുടുംബത്തിലേക്ക് സ്വാഗതം](./md/01.Introduction/01/01.PhiFamily.md)
  - [നിങ്ങളുടെ പരിപ്രേക്ഷ്‌യം സജ്ജമാക്കൽ](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [പ്രധാനം സാങ്കേതികവിദ്യകൾ മനസ്സിലാക്കുക](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi മോഡലുകൾക്കുള്ള AI സുരക്ഷ](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ഹാർഡ്വെയർ പിന്തുണ](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi മോഡലുകളും പ്ലാറ്റ്ഫോമുകൾക്ക് ഇടയിൽ ലഭ്യത](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-aiയും Phiയും ഉപയോഗിക്കൽ](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub മാർക്കറ്റ്ജ് മോഡലുകൾ](https://github.com/marketplace/models)
  - [Azure AI മോഡൽ കാറ്റലോഗ്](https://ai.azure.com)

- വ്യത്യസ്ത പരിപ്രേക്ഷങ്ങളിൽ Phi നിർമ്മിതി
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub മോഡലുകൾ](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry മോഡൽ കാറ്റലോഗ്](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI ടൂൾകിറ്റ് VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi കുടുംബ നിർമാണം
    - [iOS-ൽ Phi നിർമ്മിതി](./md/01.Introduction/03/iOS_Inference.md)
    - [Android-ൽ Phi നിർമ്മിതി](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson-ൽ Phi നിർമ്മിതി](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC-യിൽ Phi നിർമ്മിതി](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX ഫ്രെയിംവർക്ക് ഉപയോഗിച്ച് Phi നിർമ്മിതി](./md/01.Introduction/03/MLX_Inference.md)
    - [ലോക്കൽ സെർവറിൽ Phi നിർമ്മിതി](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI ടൂൾകിറ്റ് ഉപയോഗിച്ച് റിമോട്ട് സെർവറിൽ Phi നിർമ്മിതി](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust-ഇൻ്റെ സഹായത്തോടെ Phi നിർമ്മിതി](./md/01.Introduction/03/Rust_Inference.md)
    - [Phi--Vision-നൊപ്പം ലൊക്കലിൽ Phi നിർമ്മിതി](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers(ഫലപ്രദമായ പിന്തുണ) ഉപയോഗിച്ച് Phi നിർമ്മിതി](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi കുടുംബം ക്വാണ്ടിഫൈ ചെയ്യൽ](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ഉപയോഗിച്ച് Phi-3.5 / 4 ക്വാണ്ടൈസ് ചെയ്യൽ](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime ക്ക് Generative AI വിപുലീകരണങ്ങൾ ഉപയോഗിച്ച് Phi-3.5 / 4 ക്വാണ്ടൈസ് ചെയ്യൽ](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ഉപയോഗിച്ച് Phi-3.5 / 4 ക്വാണ്ടൈസ് ചെയ്യൽ](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX ഫ്രെയിംവർക്ക് ഉപയോഗിച്ച് Phi-3.5 / 4 ക്വാണ്ടൈസ് ചെയ്യൽ](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi മൂല്യനിർണ്ണയം
    - [ഉത്തരം AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry മൂല്യനിർണ്ണയത്തിനായി](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow ഉപയോഗിച്ച് മൂല്യനിർണ്ണയം](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search ഉപയോഗിച്ച് RAG
    - [Phi-4-mini, Phi-4-multimodal(RAG) Azure AI Search-നൊപ്പം എങ്ങനെ ఉపయోగിക്കാം](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi ആപ്ലിക്കേഷൻ വികസന സാമ്പിളുകൾ
  - ടെക്സ്റ്റ് & ചാറ്റ് ആപ്ലിക്കേഷനുകൾ
    - Phi-4 സാമ്പിളുകൾ 🆕
      - [📓] [Phi-4-mini ONNX മോഡലുമായി ചാറ്റ്](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 ലോക്കൽ ONNX മോഡലുമായി ചാറ്റ് .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Semantic Kernel ഉപയോഗിച്ച് Phi-4 ONNX-യോടെ ചാറ്റ് .NET കൺസോൾ ആപ്പ്](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 സാമ്പിളുകൾ
      - [Phi3, ONNX Runtime Web, WebGPU ഉപയോഗിച്ച് ബ്രൗസറിൽ ലോക്കൽ ചാറ്റ്‌ബോട്ട്](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [മൾട്ടി മോഡൽ - ഇന്ററാക്ടീവ് ഫി-3-മിനി ആൻഡ് ഓപ്പൺഎഐ വിസ്പർ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ഒരു റാപ്പർ നിർമ്മിച്ച് Phi-3 MLFlow ഉപയോഗിച്ച്](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [മോഡൽ ഓപ്റ്റിമൈസേഷൻ - Olive ഉപയോഗിച്ച് ONNX റൺടൈം വെബിനായി Phi-3-മിൻ മോഡൽ എങ്ങനെ ഒപ്റ്റിമൈസ് ചെയ്യാം](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 ആപ്പ് Phi-3 മിനി-4k-ഇൻസ്ട്രക്റ്റ്-onnx ഉപയോഗിച്ച്](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 മൾട്ടി മോഡൽ AI പവർഡ് നോട്ട്സ് ആപ് സാംപിൾ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [കസ്റ്റം Phi-3 മോഡലുകൾ Fine-tune ചെയ്ത് പ്രോണ്പ്റ്റ് ഫ്ലോവിൽ സംയോജിപ്പിക്കുക](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry-യിൽ പ്രോണ്പ്റ്റ് ഫ്ലോവിൽ കസ്റ്റം Phi-3 മോഡലുകൾ Fine-tune ചെയ്ത് സംയോജിപ്പിക്കുക](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft-ന്റെ ഉത്തരവാദിത്വ AI സിദ്ധാന്തങ്ങളെ കേന്ദ്രീകരിച്ച് Azure AI Foundry-യിൽ Fine-tuned Phi-3 / Phi-3.5 മോഡൽ വിലയിരുത്തുക](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-മിനി-ഇൻസ്ട്രക്റ്റ് ഭാഷ പ്രവചന സാംപിൾ (ചൈനീസ്/ഇംഗ്ലീഷ്)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-ഇൻസ്ട്രക്റ്റ് WebGPU RAG ചാറ്റ്ബോട്ട്](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU ഉപയോഗിച്ച് Phi-3.5-ഇൻസ്ട്രക്റ്റ് ONNX ഉപയോഗിച്ച് പ്രോണ്പ്റ്റ് ഫ്ലോ സൊല്യൂഷൻ സൃഷ്ടിക്കൽ](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite ഉപയോഗിച്ച് ആൻഡ്രോയ്ഡ് ആപ്പ് സൃഷ്ടിക്കൽ](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime ഉപയോഗിച്ച് പ്രാദേശിക ONNX Phi-3 മോഡൽ ഉപയോഗിച്ചുള്ള Q&A .NET ഉദാഹരണം](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel మరియు Phi-3 ഉപയോഗിച്ചുള്ള കോൺസോൾ ചാറ്റ് .NET ആപ്പ്](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK കോഡ് അടിസ്ഥാനമുള്ള സാംപിൾസ് 
    - Phi-4 സാംപിൾസ് 🆕
      - [📓] [Phi-4-multimodal ഉപയോഗിച്ച് പ്രൊജക്റ്റ് കോഡ് സൃഷ്ടിക്കുക](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 സാംപിൾസ്
      - [Microsoft Phi-3 കുടുംബത്തോടുകൂടിയ നിങ്ങളുടെ സ്വന്തം Visual Studio Code GitHub Copilot Chat നിർമ്മിക്കുക](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub മോഡലുകൾ ഉപയോഗിച്ചുള്ള Phi-3.5 Visual Studio Code Chat Copilot ഏജന്റ് നിർമ്മിക്കുക](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - ആഡ്‌വാൻസ്ഡ് റീസണിംഗ് സാംപിൾസ്
    - Phi-4 സാംപിൾസ് 🆕
      - [📓] [Phi-4-മിനി-റീസണിംഗ് അല്ലെങ്കിൽ Phi-4-റീസണിംഗ് സാംപിൾസ്](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive-ഉപയോഗിച്ച് Phi-4-മിനി-റീസണിംഗ് ഫൈൻട്യൂണിംഗ്](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX ഉപയോഗിച്ച് Phi-4-മിനി-റീസണിംഗ് ഫൈൻട്യൂണിംഗ്](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub മോഡലുകളോടുള്ള Phi-4-മിനി-റീസണിംഗ്](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry മോഡലുകളോടുള്ള Phi-4-മിനി-റീസണിംഗ്](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - ഡെമോസ്
      - [Phi-4-മിനി ഡെമോസ് Hugging Face Spaces ൽ ഹോസ്റ്റുചെയ്‌തത്](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-മൾട്ടിമോഡൽ ഡെമോസ് Hugginge Face Spaces ൽ ഹോസ്റ്റുചെയ്‌തത്](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - വിഷൻ സാംപിൾസ്
    - Phi-4 സാംപിൾസ് 🆕
      - [📓] [Phi-4-multimodal ഉപയോഗിച്ച് ചിത്രങ്ങൾ വായിക്കുകയും കോഡ് ജനറേറ്റ് ചെയ്യുകയും ചെയ്യുക](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 സാംപിൾസ്
      -  [📓][Phi-3-വിഷൻ-ഇമേജ് ടെക്സ്റ്റ് ടു ടെക്സ്റ്റ്](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-വിഷൻ-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-വിഷൻ CLIP എംബെഡിങ്ങ്](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ഡെമോ: Phi-3 റിസൈക്കിൾ](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-വിഷൻ - വിഷ്വൽ ഭാഷ അസിസ്റ്റന്റ് - Phi3-വിഷൻ ആൻഡ് OpenVINO ഉപയോഗിച്ച്](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 വിഷൻ Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 വിഷൻ OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 വിഷൻ മൾട്ടി-ഫ്രെയിം അല്ലെങ്കിൽ മൾട്ടി-ഇമേജ് സാംപിൾ](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 വിഷൻ പ്രാദേശിക ONNX മോഡൽ Microsoft.ML.OnnxRuntime .NET ഉപയോഗിച്ച്](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [മീനു അടിസ്ഥാനമായ Phi-3 വിഷൻ പ്രാദേശിക ONNX മോഡൽ Microsoft.ML.OnnxRuntime .NET ഉപയോഗിച്ച്](../../md/04.HOL/dotnet/src/LabsPhi304)

  - ഗണിത സാംപിൾസ്
    -  Phi-4-മിനി-ഫ്ലാഷ്-റീസണിംഗ്-ഇൻസ്ട്രക്റ്റ് സാംപിൾസ് 🆕 [Phi-4-മിനി-ഫ്ലാഷ്-റീസണിംഗ്-ഇൻസ്ട്രക്റ്റ് ഗണിത ഡെമോ](./md/02.Application/09.Math/MathDemo.ipynb)

  - ഓഡിയോ സാംപിൾസ്
    - Phi-4 സാംപിൾസ് 🆕
      - [📓] [Phi-4-multimodal ഉപയോഗിച്ച് ഓഡിയോ ട്രാൻസ്‌ക്രിപ്റ്റുകൾ എക്സ്ട്രാക്ഷൻ](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal ഓഡിയോ സാംപിൾ](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal സ്പീച്ച് ട്രാൻസ്ലേഷൻ സാംപിൾ](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET കോൺസോൾ അപ്ലിക്കേഷൻ Phi-4-multimodal ഓഡിയോ ഉപയോഗിച്ച് ഒരു ഓഡിയോ ഫയൽ വിശകലനം ചെയ്ത് ട്രാൻസ്‌ക്രിപ്റ്റ് സൃഷ്ടിക്കാൻ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE സാംപിൾസ്
    - Phi-3 / 3.5 സാംപിൾസ്
      - [📓] [Phi-3.5 മിക്‌സ്ചർ ഓഫ് എക്സ്പർട്ട്സ് മോഡലുകൾ (MoEs) സോഷ്യൽ മീഡിയ സാംപിൾ](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, LlamaIndex ഉപയോഗിച്ച് Retrieval-Augmented Generation (RAG) പൈപ്പ്‌ലൈൻ നിർമ്മിക്കുന്നു](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - ഫങ്ഷൻ കോളിങ് സാംപിൾസ്
    - Phi-4 സാംപിൾസ് 🆕
      -  [📓] [Phi-4-മിനി ഉപയോഗിച്ച് ഫങ്ഷൻ കോളിങ് ഉപയോഗിക്കൽ](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-മിനി ഉപയോഗിച്ച് മൾട്ടി-ഏജന്റുകൾ സൃഷ്ടിക്കാൻ ഫങ്ഷൻ കോളിങ് ഉപയോഗിക്കൽ](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama-യോടൊപ്പം ഫങ്ഷൻ കോളിങ് ഉപയോഗിക്കൽ](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX-യോടൊപ്പം ഫങ്ഷൻ കോളിങ് ഉപയോഗിക്കൽ](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - മൾട്ടിമോഡൽ മിക്‌സ് സാംപിൾസ്
    - Phi-4 സാംപിൾസ് 🆕
      -  [📓] [ടെക്നോളജി ജേർണലിസ്റ്റായി Phi-4-multimodal ഉപയോഗിക്കുന്നത്](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET കോൺസോൾ അപ്ലിക്കേഷൻ Phi-4-multimodal ഉപയോഗിച്ച് ചിത്രങ്ങൾ വിശകലനം ചെയ്യാൻ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- ഫൈൻ-ട്യൂണിംഗ് Phi സാംപിൾസ്
  - [ഫൈൻ-ട്യൂണിംഗ് സമീപനങ്ങൾ](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ഫൈൻ-ട്യൂണിംഗ് vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [ഫൈൻ-ട്യൂണിംഗ് Phi-3 എങ്ങനെ ഒരു വ്യവസായ വിദഗ്ധനാക്കാം](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code-അയേക്കുള്ള AI ടൂൾകിറ്റ് ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure മെഷീൻ ലേണിംഗ് സർവീസ് ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive ഉപയോഗിച്ച് ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive ഹാൻഡ്‌സ്-ഓൺ ലാബ് ഉപയോഗിച്ച് ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias ഉപയോഗിച്ച് Phi-3-വിഷൻ ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-വിഷൻ (അധികൃത പിന്തുണ)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers (അധികൃത പിന്തുണ) ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3, 3.5 വിഷൻ ഫൈൻ-ട്യൂണിംഗ്](https://github.com/2U1/Phi3-Vision-Finetune)

- ഹാൻഡ്‌സ് ഓൺ ലാബ്
  - [അത്യാധുനിക മോഡലുകൾ പരിശോധിക്കൽ: LLMs, SLMs, പ്രാദേശിക ഡിവെലപ്‌മെന്റ് മുതലായവ](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP സാധ്യതകൾ തുറക്കുന്നു: Microsoft Olive ഉപയോഗിച്ച് ഫൈൻ-ട്യൂണിംഗ്](https://github.com/azure/Ignite_FineTuning_workshop)

- അക്കാദമിക് ഗവേഷണ പേപ്പറുകളും പ്രസിദ്ധീകരണങ്ങളും
  - [സ്കൂൾപുസ്തകങ്ങൾ മുട്ടി മാത്രമാണ് വേണ്ടത് II: phi-1.5 സാങ്കേതിക റിപ്പോർട്ട്](https://arxiv.org/abs/2309.05463)
  - [Phi-3 സാങ്കേതിക റിപ്പോർട്ട്: നിങ്ങളുടെ ഫോൺൽ ലൊക്കലായി ഉയർന്ന ശേഷിയുള്ള ഭാഷ മോഡൽ](https://arxiv.org/abs/2404.14219)
  - [Phi-4 സാങ്കേതിക റിപ്പോർട്ട്](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini സാങ്കേതിക റിപ്പോർട്ട്: മിശ്രിത-ഓഫ്-ലോറാസ് മുഖേന കോംപാക്റ്റും ശക്തിയുക്തവും മൾട്ടിമോഡൽ ഭാഷ മോഡലുകൾ](https://arxiv.org/abs/2503.01743)
  - [വാഹനത്തിനുള്ളിൽ ഫംഗ്ഷൻ കോളിംഗിനായി ചെറുഭാഷ മോഡലുകൾ ഒപ്റ്റിമൈസ് ചെയ്യൽ](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) ബഹുജന-ചോദ്യോത്തരത്തിനായി PHI-3 ഫൈൻ-ട്യൂണിംഗ്: മാർഗ്ഗനിർദ്ദേശങ്ങൾ, ഫലങ്ങൾ, വെല്ലുവിളികൾ](https://arxiv.org/abs/2501.01588)
  - [Phi-4-റീസണിംഗ് സാങ്കേതിക റിപ്പോർട്ട്](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-മിനി-റീസണിംഗ് സാങ്കേതിക റിപ്പോർട്ട്](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi മോഡലുകൾ ഉപയോഗിക്കുന്നത്

### Azure AI Foundry-ൽ Phi

Microsoft Phi എങ്ങനെ ഉപയോഗിക്കാമെന്ന്, നിങ്ങളുടെ വിവിധ ഹാർഡ്‌വെയർ ഉപകരണങ്ങളിൽ എ2ഇ പരിഹാരങ്ങൾ എങ്ങനെ നിർമ്മിക്കാമെന്ന് നിങ്ങൾക്ക് പഠിക്കാം. Phi-യുടെ അനുഭവം നേടുവാനായി, മോഡലുകൾ ഉപയോഗിച്ച് കളിച്ച് നിങ്ങളുടെ സാഹചര്യങ്ങൾക്ക് അനുയോജ്യമാക്കുന്നതിലൂടെ തുടങ്ങുക, [Azure AI Foundry Azure AI മോഡൽ കാറ്റലോഗ്](https://aka.ms/phi3-azure-ai) വഴി [Azure AI Foundry-വുമായിരിക്കാൻ തുടങ്ങുക](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) എന്നത് കാണൂ.

**പ്ലേഗ്രൗണ്ട്**  
ഓരോ മോഡലിനും മodel് പരിശോധിക്കാനുള്ള പ്രത്യേക പ്ലേഗ്രൗണ്ട് ഉണ്ട് [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub മോഡലുകളിൽ Phi

Microsoft Phi എങ്ങനെ ഉപയോഗിക്കാമെന്നും, നിങ്ങളുടെ വ്യത്യസ്ത ഹാർഡ്‌വെയർ ഉപകരണങ്ങളിൽ എ2ഇ പരിഹാരങ്ങൾ എങ്ങനെ നിർമ്മിക്കാമെന്നും നിങ്ങൾക്ക് പഠിക്കാം. Phi-യുടെ അനുഭവം നേടുവാനായി, മോഡൽ ഉപയോഗിച്ച് കളിച്ച് നിങ്ങളുടെ സാഹചര്യങ്ങൾക്ക് അനുയോജ്യമാക്കുന്നതിലൂടെ തുടങ്ങുക, [GitHub മോഡൽ കാറ്റലോഗ്](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) വഴി [GitHub മോഡൽ കാറ്റലോഗ്‌ ഉപയോഗിച്ച് ആരംഭിക്കുക](/md/02.QuickStart/GitHubModel_QuickStart.md) എന്നത് വായിക്കാം.

**പ്ലേഗ്രൗണ്ട്**  
ഓരോ മോഡലിനും പ്രത്യേക [മodel് പരിശോധിക്കാൻ പ്ലേഗ്രൗണ്ട്](/md/02.QuickStart/GitHubModel_QuickStart.md) ഉണ്ട്.

### Hugging Face-ൽ Phi

മോഡൽ നിങ്ങളുടെ [Hugging Face](https://huggingface.co/microsoft) ൽ ലഭ്യമാണ്.

**പ്ലേഗ്രൗണ്ട്**  
[Hugging Chat പ്ലേഗ്രൗണ്ട്](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 മറ്റു കോഴ്സുകൾ

നമ്മുടെ ടീം മറ്റു കോഴ്സുകളും നിർമ്മിക്കുന്നു! പരിശോധിക്കുക:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain  
[![പുരോഗമനപരമായ LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)  
[![പുരോഗമനപരമായ LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / ഏജൻറുമാർ  
[![AZD തുടക്കക്കാർക്ക്](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Edge AI തുടക്കക്കാർക്ക്](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![MCP തുടക്കക്കാർക്ക്](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI ഏജൻറുമാർ തുടക്കക്കാർക്ക്](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### ജനറേറ്റീവ് AI പരമ്പര  
[![ജനറേറ്റീവ് AI തുടക്കക്കാർക്ക്](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![ജനറേറ്റീവ് AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
[![ജനറേറ്റീവ് AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)  
[![ജനറേറ്റീവ് AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### കോർ പഠനം  
[![ML തുടക്കക്കാർക്ക്](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
[![ഡേറ്റാ സയൻസ് തുടക്കക്കാർക്ക്](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI തുടക്കക്കാർക്ക്](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
[![സൈബർസെക്യൂരിറ്റി തുടക്കക്കാർക്ക്](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)  
[![വെബ് ഡെവലപ്പ്മെന്റ് തുടക്കക്കാർക്ക്](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
[![IoT തുടക്കക്കാർക്ക്](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
[![XR ഡെവലപ്പ്മെന്റ് തുടക്കക്കാർക്ക്](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### കോപൈലറ്റ് പരമ്പര  
[![AI പ്രധാനപ്പെട്ട പ്രോഗ്രാമിംഗ് കോപൈലറ്റ്](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
[![C#/.NET-കായി കോപൈലറ്റ്](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
[![കോപൈലറ്റ് സാഹസം](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## ഉത്തരവാദിത്തമുള്ള AI

Microsoft നമ്മുടേയും ഉപഭോക്താക്കളുടെയും AI ഉൽപ്പന്നങ്ങൾ ഉത്തരവാദിത്തപൂർവം ഉപയോഗിക്കാൻ സഹായിക്കുകയും, ഞങ്ങൾക്ക് നിന്നുള്ള പഠനങ്ങൾ പങ്കുവെക്കുകയും, Transparency Notes പോലുള്ള ഉപകരണങ്ങളിലൂടെ വിശ്വസനീയ പങ്കാളിത്തങ്ങൾ നിർമ്മിക്കുകയും ചെയ്യുന്നു. ഈ വിഭവങ്ങളിൽ പലതും [https://aka.ms/RAI](https://aka.ms/RAI) ൽ കണ്ടുപിടിക്കാം.  
Microsoft-ന്റെ ഉത്തരവാദിത്തമുള്ള AI സമീപനം ന്യായം, വിശ്വാസ്യതയും സുരക്ഷയും, സ്വകാര്യതയും ആർക്ക inclusiveത്വവും, പാരദർശിത്വവും, ഉത്തരവാദിത്വവും എന്നിവ അടിസ്ഥാനമാക്കി ആധാരമാണ്.

വലിയ തോതിലുള്ള സ്വാഭാവിക ഭാഷ, ചിത്രം, ശബ്ദ മോഡലുകൾ - ഈ സാമ്പിൾ ഉപയോഗിക്കുന്നവ പോലുള്ളവ - അപകൃതമായ, വിശ്വാസിക്കുന്നില്ലാത്ത, അല്ലെങ്കിൽ അപമാനകരമായ രീതിയിൽ പെരുമാറാം, ഇത് നാശനഷ്ടങ്ങൾ ഉണ്ടാക്കാം. അപകടങ്ങളും പരിമിതികളും കുറിക്കാൻ [Azure OpenAI സേവന Transparency Note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ശ്രദ്ധിക്കുക.

ഈ അപകടങ്ങൾ കുറയ്ക്കാനുള്ള ശുപാർശ ചെയ്യുന്ന മാർഗ്ഗം നിങ്ങളുടെ ആർക്കിടെക്ചറിൽ ഒരു സുരക്ഷാ സംവിധാനമുപയോഗിക്കുക ആണ്, അത് ദുഷ്പ്രവൃത്തി കണ്ടെത്തി തടയാൻ കഴിയും. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) സ്വതന്ത്രമായ സംരക്ഷണ ലെയർ നല്കുന്നു, ആപ്ലിക്കേഷനുകളിലും സേവനങ്ങളിലുമുള്ള ദുഷ്പ്രവൃത്തി സൃഷ്ടിക്കുന്ന ഉപയോക്തൃ സൃഷ്ടികൾക്കും AI സൃഷ്ടികൾക്കും തിരിച്ചറിയാൻ കഴിയും. Azure AI Content Safety ടെക്സ്റ്റ്, ചിത്രം APIകൾ ഉൾക്കൊള്ളുന്നു, ദുഷ്പ്രവൃത്തി ഉള്ള വസ്തുക്കൾ കണ്ടെത്താൻ സഹായിക്കുന്നു. Azure AI Foundry-യിലെ Content Safety സേവനം, വിവിധ ഉപാധികൾ വഴി ഹാനികരമായ ഉള്ളടക്കം കണ്ടെത്താനുള്ള സാമ്പിൾ കോഡുകൾ കാണാനും പരീക്ഷിക്കാനും അനുവദിക്കുന്നു. താഴെപ്പറയുന്ന [ക്വിക്‌സ്റ്റാർട്ട് ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) സേവനത്തിന് അഭ്യർത്ഥനകൾ കൈകാര്യം ചെയ്യുന്നതിൽ നിങ്ങളെ സഹായിക്കും.

മറ്റ് ഒരു പരിഗണനാ വിഷയമായത് മൊത്തത്തിലുള്ള ആപ്ലിക്കേഷൻ പ്രകടനമാണ്. മൾട്ടി-മോഡൽ, മൾട്ടി-മോഡൽ ആപ്ലിക്കേഷനുകളിൽ, പ്രകടനം എന്ന് പറഞ്ഞാൽ ആ സിസ്റ്റം നിങ്ങൾക്കും നിങ്ങളുടെ ഉപയോക്താക്കൾക്കും പ്രതീക്ഷിക്കുമ്പോളുള്ള വിധത്തിൽ പ്രവർത്തിക്കുമെന്നുള്ള അർത്ഥവുമാണ്; ഹാനികരമായ ഔട്ട്പുട്ടുകൾ സൃഷ്ടിക്കാതെ. നിങ്ങളുടെ മൊത്തമുള്ള ആപ്ലിക്കേഷന്റെ പ്രകടനം [പ്രകടനവും ഗുണനിലവാരവും , അപകടവും സുരക്ഷയും മൂല്യനിർണ്ണയകരും](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ഉപയോഗിച്ച് നിർവചിച്ച് വിലയിരുത്തുക പ്രധാനമാണ്. നിങ്ങൾക്ക് [സ്വന്തം മൂല്യനിർണ്ണയക്കാർ](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) സൃഷ്ടിച്ച് ഉപയോഗിക്കാനുള്ള കഴിവും ഉണ്ട്.
നിങ്ങളുടെ AI അപ്ലിക്കേഷൻ [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ഉപയോഗിച്ച് നിങ്ങളുടെ ഡെവലപ്പ്‌മെന്റ് പരിസ്ഥിതിയിൽ വിലയിരുത്താനാകും. ടെസ്റ്റ് ഡാറ്റാസെറ്റ് അല്ലെങ്കിൽ ലക്ഷ്യം നൽകിയാൽ, നിങ്ങളുടെ ജനറേറ്റീവ് AI അപ്ലിക്കേഷന്റെ ജനറേഷനുകൾ അകത്ത് നിർമിച്ചിട്ടുള്ള എവാലുവേറ്റർമാരും നിങ്ങളുടെ തിരഞ്ഞെടുക്കുന്ന കസ്റ്റം എവാലുവേറ്റർമാരും ഉപയോഗിച്ച് അളക്കപ്പെടുന്നു. നിങ്ങളുടെ സിസ്റ്റം വിലയിരുത്താൻ azure ai evaluation sdk ഉപയോഗിച്ച് ആരംഭിക്കാൻ, നിങ്ങൾക്ക് [quickstart ഗൈഡ്](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) പാലിക്കാൻ കഴിയും. ഒരു എവാലുവേഷൻ റൺ നടത്തുമ്പോൾ, നിങ്ങൾ [Azure AI Foundry-യിലുടനീളം ഫലങ്ങൾ വിസ്വലൈസ് ചെയ്യാം](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## ട്രേഡ്‌മാർക്കുകൾ

ഈ പ്രോജക്ടിൽ പ്രോജക്ടുകൾ, ഉൽപ്പന്നങ്ങൾ, അല്ലെങ്കിൽ സേവനങ്ങളുടെ ട്രേഡ്‌മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകൾ ഉണ്ടായിരിക്കலாம். മൈക്രോസോഫ്റ്റ് ട്രേഡ്‌മാർക്കുകളോ ലോഗോകളോ അനുമതി നൽകിയ ഉപയോഗം [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) അനുസരിച്ചിരിക്കണം. ഈ പ്രോജക്ടിന്റെ മാറ്റിയ പതിപ്പുകളിൽ മൈക്രോസോഫ്റ്റ് ട്രേഡ്‌മാർക്കുകളോ ലോഗോകളോ ഉപയോഗിക്കുന്നത് മൈക്രോസോഫ്റ്റ് സ്‌പോൺസർഷിപ്പ് ഉള്ളതായി തെറ്റിദ്ധരിപ്പിക്കാത്തതും ഉപയോഗത്തിന്റെ ആശയക്കുഴപ്പങ്ങൾ ഉണ്ടാക്കാത്തതും ആയിരിക്കണം. തൃശാംഘടിത ട്രേഡ്‌മാർക്കുകളോ ലോഗോകളോ ഉപയോഗിക്കുന്നത് അതിന്റെ അതൃപ്തി നയങ്ങളുടെ വിധേയമാണ്.

## സഹായം ലഭ്യമാക്കൽ

നിങ്ങൾ കുടുങ്ങിയോ AI ആപ്സ് നിർമ്മിക്കുന്നതിനെ കുറിച്ച് സംശയങ്ങളുണ്ടെങ്കിൽ, ചേരുക:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

ഉൽപ്പന്ന ഫീഡ്ബാക്കോ പിഴവുകളോ ഉണ്ടെങ്കിൽ സന്ദർശിക്കുക:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാകുറിപ്പ്**:  
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. നാം ശരിയായ വിവർത്തനത്തിന് ശ്രമിക്കുമ്പോഴും, ഓട്ടോമാറ്റഡ് വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ അസത്യതകൾ ഉണ്ടായിരിക്കാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. പ്രാഥമിക ഭാഷയിൽ ഉള്ള оригинൽ രേഖയാണ് പ്രാമാണിക ഉറവിടം ആയി പരിഗണിക്കേണ്ടത്. പ്രധാന വിവരങ്ങൾക്കായി പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ നിർദേശിച്ചിരിക്കുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗം മൂലം ഉണ്ടാകാവുന്ന തെറ്റിദ്ധാരണകൾക്കോ വ്യാഖ്യാന പിശകുകൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->