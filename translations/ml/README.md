# Phi പാചക പുസ്‌തകം: Microsoft-യുടെ Phi മോഡലുകളുമായി കൈകാര്യം ചെയ്യുന്ന ഉദാഹരണങ്ങൾ

[![GitHub Codespaces-ൽ സാമ്പിൾ ഒപ്പുവെച്ച് ഉപയോഗിക്കുക](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers-ൽ തുറക്കുക](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub സംഭാവകർ](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub പ്രശ്നങ്ങൾ](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub പുൾ-റിക്വസ്റ്റ്](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![പുൾ-റിക്വെസ്റ്റുകൾ സ്വാഗതം](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub വാച്ചർമാർ](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ഫോർക്കുകൾ](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub സ്റ്റാർസ്](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi Microsoft വികസിപ്പിച്ചിട്ടുള്ള ഓപ്പൺ സോഴ്സ് AI മോഡലുകളുടെ ഒരു പരമ്പരയാണ്.

Phi നിലവിൽ ഏറ്റവും ശക്തിയും ചെലവ് കാര്യക്ഷമതയുമായി ബന്ധപ്പെട്ടു ചെറിയ ഭാഷാ മോഡലുകളിലേതാണ് (SLM), ബഹുഭാഷാ, ആയോജനം, ടെക്സ്റ്റ്/ചാറ്റ് നിർമ്മാണം, കോഡിംഗ്, ചിത്രങ്ങൾ, ഓഡിയോ എന്നിവയിൽ മികച്ച ബെൻച്മാർക്കുകൾ കൈവരിച്ചിരിക്കുന്നു.

നിങ്ങൾ Phi ക്ലൗഡിലോ എഡ്ജ് ഉപകരണങ്ങളിലോ വിന്യസിക്കാനാകും, കൂടാതെ പരിമിത കംപ്യൂട്ടിങ്ങ് ശേഷിയുള്ളതിനും വളരെ എളുപ്പത്തിൽ ജനറേറ്റീവ് AI ആപ്ലിക്കേഷനുകൾ നിർമ്മിക്കാനാകും.

ഈ റിസോഴ്സുകൾ ഉപയോഗിക്കാൻ തുടങ്ങുന്നതിന് താഴെ കൊടുത്തിട്ടുള്ള ചുവടുകൾ പിന്തുടരുക:
1. **റിപ്പോസിറ്ററി ഫോർക്കുചെയ്യുക**: [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo) ക്ലിക്ക് ചെയ്യുക
2. **റിപ്പോസിറ്ററി ക്ലോണുചെയ്യുക**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord സമൂഹത്തിൽ ചേർന്ന് വിദഗ്ധരുമായും മറ്റ് ഡെവലപ്പർമാരുമായും കണ്ടുമുട്ടുക**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/ml/cover.eb18d1b9605d754b.webp)

### 🌐 ബഹുഭാഷാ പിന്തുണ

#### GitHub ആക്ഷൻ വഴിയുള്ള പിന്തുണ (സ്വയമേവ പ്രവർത്തിക്കുന്നതും എല്ലായ്പ്പോഴും പുതുക്കപ്പെടുന്നതും)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](./README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **പ്രാദേശികമായി ക്ലോൺ ചെയ്യണമോ?**
>
> ഈ റിപ്പോസിറ്ററിയിൽ 50-ലധികം ഭാഷാ പരിഭാഷകൾ ഉള്ളതിനാൽ ഡൗൺലോഡ് സൈസ് വളരെ വലുതാണ്. പരിഭാഷകളില്ലാതെ ക്ലോൺ ചെയ്യാൻ sparse checkout ഉപയോഗിക്കുക:
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
> ഇത് നിങ്ങൾക്ക് വളരെ വേഗത്തിലുള്ള ഡൗൺലോഡോടെ കോഴ്‌സ് പൂർത്തിയാക്കാൻ ആവശ്യമുള്ള എല്ലാ ഫയലുകളും നൽകും.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## ഉള്ളടക്ക പട്ടിക

- പരിചയം
  - [Phi കുടുംബത്തിലേക്ക് സ്വാഗതം](./md/01.Introduction/01/01.PhiFamily.md)
  - [നിങ്ങളുടെ പരിസ്ഥിതി ക്രമീകരിക്കൽ](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [പ്രധാന സാങ്കേതികവിദ്യകൾ മനസിലാക്കുക](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi മോഡലുകൾക്കുള്ള AI സുരക്ഷ](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ഹാർഡ്‌വെയർ പിന്തുണ](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [ഫ്ലാറ്റ്ഫോം വിപുലമായി Phi മോഡലുകളും ലഭ്യതയും](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai և Phi ഉപയോഗിക്കൽ](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub മാർക്കറ്റ് പ്ലേസ് മോഡലുകൾ](https://github.com/marketplace/models)
  - [Azure AI മോഡൽ കാറ്റലോഗ്](https://ai.azure.com)

- വ്യത്യസ്ത പരിസ്ഥിതികളിൽ Phi-ന്റെ ഇൻഫെറൻസ്
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub മോഡലുകൾ](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Microsoft Foundry മോഡൽ കാറ്റലോഗ്](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI ടൂൾകിറ്റ് VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry ലൊക്കൽ](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi കുടുംബത്തിലെ ഇൻഫെറൻസ്
    - [iOS-ൽ ഇൻഫെറൻസ് Phi](./md/01.Introduction/03/iOS_Inference.md)
    - [Android-ൽ ഇൻഫെറൻസ് Phi](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson-ൽ ഇൻഫെറൻസ് Phi](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC-യിൽ ഇൻഫെറൻസ് Phi](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX ഫ്രെയിംവർക്ക് ഉപയോഗിച്ച് Phi ഇൻഫെറൻസ്](./md/01.Introduction/03/MLX_Inference.md)
    - [ലൊക്കൽ സെർവറിൽ ഇൻഫെറൻസ് Phi](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI ടൂൾകിറ്റ് ഉപയോഗിച്ച് റിമോട്ട് സെർവറിൽ ഇൻഫെറൻസ് Phi](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust ഉപയോഗിച്ച് ഇൻഫെറൻസ് Phi](./md/01.Introduction/03/Rust_Inference.md)
    - [ലൊക്കലിൽ ഇൻഫെറൻസ് Phi--Vision](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (ഓഫിഷ്യൽ പിന്തുണ) ഉപയോഗിച്ച് ഇൻഫെറൻസ് Phi](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi കുടുംബം ക്വാണ്ടിഫൈ ചെയ്ത് പരിശോധിക്കൽ](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ഉപയോഗിച്ച് Phi-3.5 / 4 ക്വാണ്ടൈസ് ചെയ്യൽ](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime-നുള്ള ജനറേറ്റീവ് AI എക്സ്റ്റൻസ് വഴി Phi-3.5 / 4 ക്വാണ്ടൈസ് ചെയ്യൽ](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ഉപയോഗിച്ച് Phi-3.5 / 4 ക്വാണ്ടൈസ് ചെയ്യൽ](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX ഫ്രെയിംവർക്ക് ഉപയോഗിച്ച് Phi-3.5 / 4 ക്വാണ്ടൈസ് ചെയ്യൽ](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi-ന്റെ മൂല്യനിർണയം
    - [Responsibile AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Microsoft Foundry മൂല്യനിർണയത്തിന്](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow ഉപയോഗിച്ച് മൂല്യനിർണയം](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI സെർച്ച് ഉപയോഗിച്ച് RAG
    - [Phi-4-miniയും Phi-4-multimodal (RAG)യും Azure AI സെർച്ച് ഉപയോഗിച്ച് എങ്ങനെ ഉപയോഗിക്കാമെന്ന്](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)
    - [Zero-Cloud ലൊക്കൽ ഹൈബ്രിഡ് RAG SQLite FTS5 സജ്ജീകരിച്ച് phi-4-mini](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-mini_Local_Hybrid_RAG_SQLite_FTS5.ipynb)

- Phi ആപ്ലിക്കേഷൻ ഡെവലപ്മെന്റ് സാമ്പിളുകൾ
  - ടെക്സ്റ്റ് & ചാറ്റ് ആപ്ലിക്കേഷനുകൾ
    - Phi-4 സാമ്പിളുകൾ
      - [📓] [Phi-4-mini ONNX മോഡലുമായി ചാറ്റ്](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 ലൊക്കൽ ONNX മോഡലുമായി ചാറ്റ് .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel ഉപയോഗിച്ച് Phi-4 ONNX-ഉള്ള .NET കൺസോൾ ആപ്പ്](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)

    - Phi-3 / 3.5 സാമ്പിളുകൾ
      - [Phi3, ONNX Runtime Web, WebGPU ഉപയോഗിച്ച് ബ്രൗസറിൽ ലോക്കൽ ചാറ്റ്ബോട്ട്](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino ചാറ്റ്](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [മൾട്ടി മോഡൽ - ഇന്ററാക്ടീവ് Phi-3-mini, OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - വ്രാപ്പർ നിർമ്മിക്കൽ, Phi-3 MLFlow ഉപയോഗിച്ച്](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [മോഡൽ ഓപ്റ്റിമൈസേഷൻ - ONNX Runtime Web നിൽക്കാൻ Phi-3-mini മോഡൽ ഓപ്റ്റിമൈസ് ചെയ്യുക Olive ഉപയോഗിച്ച്](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 ആപ്പ് Phi-3 mini-4k-instruct-onnx ഉപയോഗിച്ച്](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 മൾട്ടി മോഡൽ AI പ്രചോദിത നോട്ട്സ് ആപ്പ് സാമ്പിൾ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Fine-tune ചെയ്ത് Prompt flow ഉപയോഗിച്ച് കസ്റ്റം Phi-3 മോഡലുകൾ ഒരു പൂർണ്ണ സംയോജനം](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Microsoft Foundry-ൽ Prompt flow ഉപയോഗിച്ച് കസ്റ്റം Phi-3 മോഡലുകൾ Fine-tune ചെയ്ത് സംയോജനം](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft Foundry-ൽ Phi-3 / Phi-3.5 മോഡലിന്റെ ഫൈൻ-ട്യൂണിങ് വിലയിരുത്തൽ Responsible AI ചട്ടങ്ങൾക്കൊപ്പം](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct ഭാഷാ പ്രവചനം സാമ്പിൾ (ചൈനീസ്/ഇംഗ്ലീഷ്)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG ചാറ്റ്ബോട്ട്](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU ഉപയോഗിച്ച് Phi-3.5-Instruct ONNX പ്രോമ്പ്റ്റ് ഫ്ലോ സൊല്യൂഷൻ നിർമ്മിക്കൽ](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite ഉപയോഗിച്ച് ആൻഡ്രോയിഡ് ആപ്പ് സൃഷ്ടിക്കൽ](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime ഉപയോഗിച്ച് ലോക്കൽ ONNX Phi-3 മോഡൽ ഉപയോഗിക്കുന്ന Q&A .NET ഉദാഹരണം](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel, Phi-3 ഉപയോഗിച്ച് കൺസോൾ ചാറ്റ് .NET ആപ്പ്](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI ഇൻഫെറൻസ് SDK കോഡ് അടിസ്ഥാനമുള്ള സാമ്പിളുകൾ
    - Phi-4 സാമ്പിളുകൾ
      - [📓] [Phi-4-multimodal ഉപയോഗിച്ച് പ്രോജക്ട് കോഡ് ജനറേറ്റ് ചെയ്യുക](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 സാമ്പിളുകൾ
      - [Microsoft Phi-3 ശൃംഖല ഉപയോഗിച്ച് നിങ്ങളുടെ സ്വന്തം Visual Studio Code GitHub Copilot Chat നിർമ്മിക്കുക](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub മോഡലുകൾ ഉപയോഗിച്ച് Phi-3.5 ഉപയോഗിച്ച് Visual Studio Code Chat Copilot ഏജന്റ് സൃഷ്ടിക്കുക](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - അഡ്വാൻസ് ചെയ്ത റീഫീസനിംഗ് സാമ്പിളുകൾ
    - Phi-4 സാമ്പിളുകൾ
      - [📓] [Phi-4-mini-reasoning അല്ലെങ്കിൽ Phi-4-reasoning സാമ്പിളുകൾ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive ഉപയോഗിച്ച് Phi-4-mini-reasoning ഫൈൻ-ട്യൂണിങ്](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX ഉപയോഗിച്ച് Phi-4-mini-reasoning ഫൈൻ-ട്യൂണിങ്](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub മോഡലുകളോടൊപ്പം Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Microsoft Foundry മോഡലുകളോടൊപ്പം Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - ഡെമോകൾ
      - [Hugging Face Spaces-ൽ ഹോസ്റ്റ് ചെയ്ത Phi-4-mini ഡെമോകൾ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Hugging Face Spaces-ൽ ഹോസ്റ്റ് ചെയ്ത Phi-4-multimodal ഡെമോകൾ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - വിഷൻ സാമ്പിളുകൾ
    - Phi-4 സാമ്പിളുകൾ
      - [📓] [Phi-4-multimodal ഉപയോഗിച്ച് ചിത്രം വായിക്കുക, കോഡ് ജനറേറ്റ് ചെയ്യുക](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)
    - Phi-3 / 3.5 സാമ്പിളുകൾ
      -  [📓][Phi-3-vision-ചിത്രം എഴുത്തായി മാറ്റൽ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP എംബഡ്ഡിങ്](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ഡെമോ: Phi-3 റീസൈക്ലിംഗ്](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - ദൃശ്യഭാഷാ അസിസ്റ്റന്റ് - Phi3-vision, OpenVINO ഉപയോഗിച്ചത്](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision മൾട്ടി-ഫ്രेम് അല്ലെങ്കിൽ മൾട്ടി-ഇമേജ് സാമ്പിൾ](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET ഉപയോഗിച്ച് Phi-3 Vision ലോക്കൽ ONNX മോഡൽ](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [മെനു അടിസ്ഥാനത്തിൽ Phi-3 Vision ലോക്കൽ ONNX മോഡൽ Microsoft.ML.OnnxRuntime .NET ഉപയോഗിച്ച്](../../md/04.HOL/dotnet/src/LabsPhi304)

  - റീഫീസനിംഗ്-വിഷൻ സാമ്പിളുകൾ
    - Phi-4-റീഫീസനിംഗ്-വിഷൻ-15B
      - [📓] [Phi-4-റീഫീസനിംഗ്-വിഷൻ-15B ജേ-വാല്കിംഗ് കണ്ടെത്താൻ ഉപയോഗിക്കുന്നു](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb)
      - [📓] [Phi-4-റീഫീസനിംഗ്-വിഷൻ-15B കൊണ്ട് ഗണിതം ചെയ്യുന്നു](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb)
      - [📓] [Phi-4-റീഫീസനിംഗ്-വിഷൻ-15B ഉപയോഗിച്ച് UI കണ്ടെത്തൽ](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb)

  - ഗണിത സാമ്പിളുകൾ
    -  Phi-4-മിനി-ഫ്ലാഷ്-റീഫീസനിംഗ്-ഇൻസ്ട്രക്റ്റ് സാമ്പിളുകൾ  [Phi-4-മിനി-ഫ്ലാഷ്-റീഫീസനിംഗ്-ഇൻസ്ട്രക്റ്റ് ഗണിത ഡെമോ](./md/02.Application/09.Math/MathDemo.ipynb)

  - ഓഡിയോ സാമ്പിളുകൾ
    - Phi-4 സാമ്പിളുകൾ
      - [📓] [Phi-4-multimodal ഉപയോഗിച്ച് ഓഡിയോ ട്രാൻസ്ക്രിപ്റ്റുകൾ എടുക്കുന്നു](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal ഓഡിയോ സാമ്പിൾ](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal സ്പീച്ച് ട്രാൻസ്ലേഷൻ സാമ്പിൾ](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET കൺസോൾ ആപ്പ് Phi-4-multimodal ഉപയോഗിച്ച് ഓഡിയോ ഫയൽ വിശകലനം ചെയ്ത് ട്രാൻസ്ക്രിപ്റ്റ് നിർമ്മിക്കുന്നു](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE സാമ്പിളുകൾ
    - Phi-3 / 3.5 സാമ്പിളുകൾ
      - [📓] [Phi-3.5 എക്സ്പർട്സ് മിക്‌ഷർ (MoEs) സോഷ്യൽ മീഡിയ സാമ്പിൾ](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, LlamaIndex ഉപയോഗിച്ച് റിട്ട്രീവൽ-ഓഗ്മെന്റഡ് ജനറേഷൻ (RAG) പൈപ്പ്‌ലൈൻ നിർമ്മിക്കൽ](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - ഫംഗ്ഷൻ കോൾ ചെയ്യൽ സാമ്പിളുകൾ
    - Phi-4 സാമ്പിളുകൾ 🆕
      -  [📓] [Phi-4-mmini ഉപയോഗിച്ച് ഫംഗ്ഷൻ കോൾ ചെയ്യൽ](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mmini ഉപയോഗിച്ച് മൾട്ടി-ഏജന്റുകൾ സൃഷ്ടിക്കാൻ ഫംഗ്ഷൻ കോൾ ചെയ്യൽ](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama ഉപയോഗിച്ച് ഫംഗ്ഷൻ കോൾ ചെയ്യൽ](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX ഉപയോഗിച്ച് ഫംഗ്ഷൻ കോൾ ചെയ്യൽ](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - മൾട്ടിമോഡൽ മിശ്രിത സാമ്പിളുകൾ
    - Phi-4 സാമ്പിളുകൾ 🆕
      -  [📓] [സാങ്കേതിക മാധ്യമപ്രതിനിധിയായി Phi-4-multimodal ഉപയോഗിക്കൽ](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET കൺസോൾ ആപ്പ് ഇമേജുകൾ വിശകലനം ചെയ്യാൻ Phi-4-multimodal ഉപയോഗിക്കുന്നു](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- ഫൈൻ-ട്യൂണിംഗ് Phi സാമ്പിളുകൾ
  - [ഫൈൻ-ട്യൂണിംഗ് സീനാറിയോകൾ](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ഫൈൻ-ട്യൂണിംഗ് vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 ഒരു വ്യവസായ വിദഗ്ധരാകാൻ അനുവദിക്കുന്ന ഫൈൻ-ട്യൂൺ](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [AI ടൂൾകിറ്റ് വഴി Phi-3 ഫൈൻ-ട്യൂണിംഗ് VS കോഡിൽ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure മെഷീൻ ലേണിംഗ് സേവനം ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Microsoft Foundry ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive ഉപയോഗിച്ച് ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive ഹാൻസ്-ഓൺ ലാബ് ഉപയോഗിച്ച് ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias ഉപയോഗിച്ച് Phi-3-vision ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)

  - [ആപ്പിള്‍ MLX ഫ്രെയിംവര്‍ക്കുമായി Phi-3 ഫൈന്‍-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision ഫൈന്‍-ട്യൂണിംഗ് (അധिकारिक പിന്തുണ)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers ഉപയോഗിച്ച് Phi-3 ഫൈന്‍-ട്യൂണിംഗ് (അധिकारिक പിന്തുണ)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 and 3.5 Vision ഫൈന്‍-ട്യൂണിംഗ്](https://github.com/2U1/Phi3-Vision-Finetune)

- ഹാൻഡ്സ് ഓൺ ലാബ്
  - [ആദ്യ നിര മോഡലുകള്‍ പരീക്ഷിക്കുന്നത്: LLMs, SLMs, ലോക്കൽ ഡെവലപ്മെന്റ് എന്നിവ](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP ശേഷി തെളിയിക്കൽ: Microsoft Olive ഉപയോഗിച്ച് ഫൈന്‍-ട്യൂണിംഗ്](https://github.com/azure/Ignite_FineTuning_workshop)

- അക്കാദമിക് ഗവേഷണ पेപ്പർസും പ്രസിദ്ധീകരണങ്ങളും
  - [Textbooks Are All You Need II: phi-1.5 സാങ്കേതിക റിപ്പോര്‍ട്ട്](https://arxiv.org/abs/2309.05463)
  - [Phi-3 സാങ്കേതിക റിപ്പോര്‍ട്ട്: നിങ്ങളുടെ ഫോണില്‍ highly capable language model](https://arxiv.org/abs/2404.14219)
  - [Phi-4 സാങ്കേതിക റിപ്പോര്ട്ട്](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini സാങ്കേതിക റിപ്പോര്ട്ട്: മിക്സ്ചർ ഓഫ് ലോറാസിലൂടെ ചെറുതും ശക്തിയുള്ള മൾട്ടിമോഡല്‍ ലാംഗ്വേജ് മോഡലുകള്‍](https://arxiv.org/abs/2503.01743)
  - [ഇൻ-വണ്ടിയിലുള്ള ഫംഗ്ഷൻ-കൊല്ലിംഗിനായി ചെറിയ ഭാഷാ മോഡലുകൾ ഓപ്റ്റിമൈസ് ചെയ്യുന്നു](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) ഫൈന്‍-ട്യൂണിംഗ് PHI-3 മൾട്ടിപ്പിൾ-ചോയ്‌സ് ചോദ്യോത്തരത്തിനായി: പ്രക്രിയ, ഫലങ്ങളും വെല്ലുവിളികളും](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning സാങ്കേതിക റിപ്പോര്ട്ട്](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning സാങ്കേതിക റിപ്പോര്ട്ട്](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi മോഡലുകൾ ഉപയോഗിക്കുന്നത്

### Microsoft Foundry ല്‍ Phi

Microsoft Phi ഉപയോഗിക്കുന്നത് പരിശീലിക്കുകയും വിവിധ ഹാർഡ്വെയർ ഉപകരണങ്ങളിൽ end-to-end പരിഹാരങ്ങൾ നിർമ്മിക്കുകയും ചെയ്യാൻ നിങ്ങൾക്ക് ഇതിൽ പഠിക്കാം. Phi നേരിട്ട് അനുഭവിക്കാൻ, മോഡലുകളില്‍ കളിച്ച് നിങ്ങളുടെ സാഹചര്യങ്ങൾക്കനുസരിച്ചു Phi ഇഷ്ടാനുസൃതമാക്കുക [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ഉപയോഗിക്കുക, കൂടാതെ [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) എന്നത് ആരംഭിക്കുക.

**പ്ലേഗ്രൗണ്ട്**
ഓരോ മോഡലിനും പരീക്ഷിക്കാൻ സമർപ്പിച്ച പ്ലേഗ്രൗണ്ട് ഉണ്ട് [Azure AI പ്ലേഗ്രൗണ്ട്](https://aka.ms/try-phi3).

### GitHub മോഡലുകളിൽ Phi

Microsoft Phi ഉപയോഗിച്ച് വേറെയും end-to-end പരിഹാരങ്ങൾ നിങ്ങളുടെ ഹാർഡ്വെയർ ഉപകരണങ്ങളില്‍ എങ്ങിനെയാണ് നിർമ്മിക്കേണ്ടതെന്ന് പഠിക്കാൻ നിങ്ങൾക്ക് കഴിയും. Phi നേരിട്ട് അനുഭവിക്കാനായി മോഡലുമായി കളിച്ച് നിങ്ങളുടെ സാഹചര്യങ്ങൾക്കനുസരിച്ചു Phi ഇഷ്ടാനുസൃതമാക്കുക [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ഉപയോഗിക്കുക, കൂടാതെ [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) ആരംഭിക്കുക.

**പ്ലേഗ്രൗണ്ട്**
ഓരോ മോഡലിനും [പരീക്ഷിക്കാൻ സമർപ്പിച്ച പ്ലേഗ്രൗണ്ട്](/md/02.QuickStart/GitHubModel_QuickStart.md) ഉണ്ട്.

### Hugging Face ല്‍ Phi

മോഡൽ [Hugging Face](https://huggingface.co/microsoft) ല്‍ കണ്ടെത്താനും കഴിയും

**പ്ലേഗ്രൗണ്ട്**
 [Hugging Chat പ്ലേ ഗ്രൗണ്ട്](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 മറ്റ് കോഴ്‌സുകൾ

ഞങ്ങളുടെ ടീമിന് മറ്റ് കോഴ്‌സുകളും ഉണ്ട്! പരിശോധിക്കുക:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / ഏജന്‍റുകൾ
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### ജനറേറ്റീവ് AI പരമ്പര
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### കോർ പഠനം
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### കോപൈലറ്റ് പരമ്പര
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## ഉത്തരവാദിത്തമുള്ള AI 

മൈക്രോസോഫ്റ്റ് നമ്മുടെ AI ഉൽപ്പന്നങ്ങൾ ഉത്തരവാദിത്തത്തോടെ ഉപയോഗിക്കാൻ ഉപഭോക്താക്കളെ സഹായിക്കാനും, പഠനങ്ങൾ പങ്കുവെക്കാനും, ട്രാൻസ്പാരൻസി നോട്ട്‌സ്, ഇംപാക്റ്റ് അസസ്‌മെന്റുകൾ പോലുള്ള ഉപകരണങ്ങളിലൂടെ വിശ്വാസപാരമായ പങ്കാളിത്തങ്ങൾ നിര്‍മിക്കാനും പ്രതിജ്ഞാബദ്ധമാണ്. ഈ സ്രോതസ്സുകളിൽ പലതും [https://aka.ms/RAI](https://aka.ms/RAI) ല്‍ ലഭ്യമാണ്.
മൈക്രോസോഫ്റ്റിന്റെ ഉത്തരവാദിത്തമുള്ള AI സമീപനം, ന്യായത്വം, വിശ്വാസ്യതയും സുരക്ഷയും, സ്വകാര്യതയും സുരക്ഷയും, ഉൾപ്പെടുത്തലും, പരദർശിത്വവും ഉത്തരവാദിത്തവും എന്ന ഞങ്ങളുടെ AI 원칙ങ്ങളിലാണ് അടിസ്ഥിതമായിരിക്കുന്നത്.

വലിയതലത്തിലുള്ള പ്രകൃതി ഭാഷ, ചിത്രം, സംഭാഷണ മോഡലുകൾ - ഈ സാമ്പിളിൽ ഉപയോഗിക്കുന്നവ പോലുള്ള - അനീതിയുള്ള, വിശ്വാസയോഗ്യമല്ലാത്ത, അല്ലെങ്കിൽ അപമാനകരമായ രീതിയിൽ പ്രവർത്തിക്കാനും നുഴഞ്ഞുകയറാനും സാധ്യതയുണ്ട്, ഇത് ഹാനിക്കരമായിരിക്കാം. ദയവായി അപകടങ്ങളും പരിധികളും അറിയാൻ [Azure OpenAI സർവീസ് ട്രാൻസ്പാരൻസി നോട്ട്](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) കാണുക.


ഈ അപകടങ്ങൾ നിയന്ത്രിക്കുന്നതിനുള്ള ശുപാർശ ചെയ്യുന്ന സമീപനം, നിങ്ങളുടെ ആർക്കിടെക്ചറിൽ ഒരു സുരക്ഷാ സംവിധാനം ഉൾപ്പെടുത്തുകയാണ്, ഇത് ഹാനികരമായ പെരുമാറ്റം കണ്ടെത്താനും തടയാനും കഴിയും. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) അവിടെയുള്ള ആപ്പ്‌ളിക്കേഷനുകളിലും സേവനങ്ങളിലും ഹാനികരമായ ഉപയോക്താവ്-സമർപ്പിച്ചും AI-സൃഷ്ടിച്ചും ഉള്ള ഉള്ളടക്കം കണ്ടെത്താനും തടയാനും കഴിയുന്ന സ്വതന്ത്രഏകക സുരക്ഷാ അടിസ്ഥാനമാണ്. Azure AI Content Safety ഹാനികരമായ വിഷയങ്ങൾ കണ്ടെത്താനുള്ള ടെക്സ്റ്റ്‌യും ഇമേജ് API-കളും ഉൾക്കൊള്ളുന്നു. Microsoft Foundry-യിൽ ഉള്ള Content Safety സേവനം, വ്യത്യസ്ത മോഡാലിറ്റികളിലെ ഹാനികരമായ ഉള്ളടക്കം കണ്ടെത്തുന്നതിനുള്ള സാംപിൾ കോഡ് കാണുവാനും പരിശോധന നടത്തുവാനും അനുവദിക്കുന്നു. താഴെപ്പറയുന്ന [ക്വിക്‌സ്റ്റാർട്ട് ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) സേവനത്തിനായി നിർദ്ദേശങ്ങൾ നൽകുന്നു.

മറ്റൊരു പരിഗണിക്കേണ്ട ഘടകം ആകെ ആപ്‌ളിക്കേഷൻ പ്രകടനമാണ്. ബഹുമോദാലിട്ടും ബഹുമോഡൽ ആപ്ലിക്കേഷനുകളിലും, സിസ്റ്റം നിങ്ങളുടെ ഉദ്ദേശപ്രകാരം പ്രവർത്തിക്കുന്നതായും ഉപയോക്താക്കളുടെ പ്രതീക്ഷകൾക്കനുസരിച്ച്, ഹാനികരമായ ഔട്ട്പുട്ടുകൾ സൃഷ്ടിക്കപ്പെടാതിരിക്കുകയും ചെയ്യുന്നതായും പ്രകടനം ഗണിക്കുന്നു. നിങ്ങളുടെ ആകെ ആപ്‌ളിക്കേഷന്റെ പ്രകടനം [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ഉപയോഗിച്ച് വിലയിരുത്തുന്നത് നിർണായകമാണ്. [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) സൃഷ്ടിക്കുകയും അവ ഉപയോഗിച്ചു വിലയിരുത്തുകയും ചെയ്യുന്നതും കഴിയും.

[Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ഉപയോഗിച്ച് നിങ്ങൾക്ക് നിങ്ങളുടെ AI ആപ്ലിക്കേഷൻ വികസന പരിസ്ഥിതിയിൽ തന്നെ വിലയിരുത്താം. ടെസ്റ്റ് ഡാറ്റാസെറ്റ് അല്ലെങ്കിൽ ടാർഗെറ്റ് നൽകിയാൽ, നിങ്ങളുടെ ജനറേറ്റീവ് AI ആപ്ലിക്കേഷന്റെ സൃഷ്ടികൾ സ്‌ഥിതിഗതികൾ ഉൾക്കൊള്ളുന്ന ഇൻ-ബിൽറ്റ് ഇവല്യുവേറ്ററുകൾ അല്ലെങ്കിൽ നിങ്ങളുടെ തെരഞ്ഞെടുക്കുന്ന കസ്റ്റം ഇവല്യുവേറ്ററുകൾ ഉപയോഗിച്ച് സംഖ്യാത്മകമായി അളക്കപ്പെടുന്നു. നിങ്ങളുടെ സിസ്റ്റം വിലയിരുത്താൻ ആഴ്യൂർ AI ഇവല്യുവേഷൻ SDK ഉപയോഗിച്ച് തുടങ്ങുവാൻ [ക്വിക്‌സ്റ്റാർട്ട് ഗൈഡ്](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) പിന്തുടരാം. ഒരു ഇവല്യുവേഷൻ റൺ നടത്തുമ്പോൾ, നിങ്ങൾക്ക് [Microsoft Foundry-ൽ ഫലം ദൃശ്യവത്കരിക്കാൻ](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) കഴിയും.

## ട്രേഡ്മാർക്ക്‌ಗಳು

ഈ പ്രോജക്ടിൽ പ്രോജക്റ്റുകൾ, ഉൽപ്പന്നങ്ങൾ, അല്ലെങ്കിൽ സേവനങ്ങൾക്കുമുള്ള ട്രേഡ്മാർക്ക്‌കളും ലോഗോകളും থাকতে পারে. Microsoft-ന്റെ ട്രേഡ്മാർക്ക് അല്ലെങ്കിൽ ലോഗോകളുടെ അനുമതിയുള്ള ഉപയോഗം [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) പാലിക്കേണ്ടതാണ്.
ഈ പ്രോജക്ടിന്റെ തിരുത്തിയ പതിപ്പുകളിലെ Microsoft ട്രേഡ്മാർക്ക് അല്ലെങ്കിൽ ലോഗോകളുടെ ഉപയോഗം Microsoft പിന്തുണ ഉറപ്പുവരുത്തുകയോ ആശങ്ക സൃഷ്ടിക്കുകയോ ചെയ്യരുത്. മൂന്നാം പാർട്ടി ട്രേഡ്മാർക്ക് അല്ലെങ്കിൽ ലോഗോകളുടെ ഉപയോഗം ആ മൂന്നാം പാർട്ടി നയങ്ങൾക്കു വിധേയമാണ്.

## സഹായം നേടൽ

AI ആപ്ലിക്കേഷനുകള്‍ സൃഷ്ടിക്കുന്നതിനിടെ നിങ്ങൾക്ക് പ്രശ്നങ്ങളോ ചോദ്യങ്ങളോ ഉണ്ടെങ്കിൽ, ചേരുക:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

ഉൽപ്പന്ന ഫീഡ്‌ബാക്കോ പിഴവുകളോ ഉണ്ടെങ്കിൽ സന്ദർശിക്കുക:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->