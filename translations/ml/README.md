# ഫി കുക്ക്ബുക്ക്: Microsoft-യുടെ Phi മോഡലുകളുമായുള്ള ഹാൻഡ്‌സോൺ ഉദാഹരണങ്ങൾ

[![GitHub Codespaces-ൽ സാമ്പിളുകൾ തുറന്ന് ഉപയോഗിക്കുക](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers-ൽ തുറക്കുക](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub സംഭാവകർ](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub പ്രശ്നങ്ങൾ](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub പുൾ അഭ്യർത്ഥനകൾ](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs സ്വാഗതം ചെയ്യുന്നു](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub വാച്ചേഴ്സ്](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ഫോർക്കുകൾ](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub സ്റ്റാർസ്](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi Microsoft വികസിപ്പിച്ച ഒരു ഓപ്പൺ സോഴ്‌സ് AI മോഡലുകളുടെ പരമ്പരയാണ്.

Phi നിലവിൽ വളരെ ശക്തവും ചെലവുകുറഞ്ഞതുമായ ചെറിയ ഭാഷാ മോഡലാണ് (SLM), മൾട്ടി-ഭാഷ, ബോധവത്കരണം, എഴുത്ത്/ചാറ്റ് üret generation, കോഡിംഗ്, ചിത്രം, ഓഡിയോ എന്നിവയടക്കമുള്ള വിവിധ പ്രയോഗങ്ങളിൽ മികച്ച പ്രകടനം കാഴ്ചവെക്കുന്നു.

നിങ്ങൾ Phi ക്ലൗഡിലും എഡ്ജ് ഉപകരണങ്ങളിലും മൊരിയ്ക്കാം, കൂടാതെ കുറഞ്ഞ കംപ്യൂട്ടിംഗ് ശേഷിയുള്ള ജനന AI അപേക്ഷകൾ आसानीയോടെ നിർമ്മിക്കാം.

ഈ ഘട്ടങ്ങൾ പിന്തുടർന്ന് ഈ സ്രോതസ്സുകൾ ഉപയോഗിച്ച് തുടക്കം കുറിക്കുക:
1. **റിപ്പോസിറ്ററി ഫോർക്കുചെയ്യുക**: ക്ലിക്ക് ചെയ്യുക [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **റിപ്പോസിറ്ററി ക്ലോൺ ചെയ്യുക**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord കമ്മ്യൂണിറ്റിയിൽ ചേരുക, വിദഗ്ദ്ധരെയും സഹപ്രവർത്തകരെയും കാണുക**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/ml/cover.eb18d1b9605d754b.webp)

### 🌐 മൾട്ടി-ഭാഷാ പിന്തുണ

#### GitHub Action വഴി പിന്തുണ (തത്സമയം & എല്ലായ്പ്പോഴും പുതുക്കപ്പെട്ടത്)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](./README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **സ്ഥലീയമായി ക്ലോൺ ചെയ്യാൻ ഇഷ്ടപ്പെടുന്നുണ്ടോ?**
>
> ഈ റിപോസിറ്ററിയിൽ 50-ലധികം ഭാഷാ പരിഭാഷകൾ ഉൾപ്പെടുത്തിയിട്ടുണ്ട്, ഇത് ഡൗൺലോഡ് വലുപ്പം ഗണ്യമായി വർദ്ധിപ്പിക്കുന്നു. പരിഭാഷകൾ ഇല്ലാതെ ക്ലോൺ ചെയ്യാൻ sparse checkout ഉപയോഗിക്കുക:
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
> ഇത് കോഴ്‌സ് പൂര്‍ത്തിയാക്കാൻ ആവശ്യമായ എല്ലാ ഘടകങ്ങളും വേഗത്തിൽ ഡൗൺലോഡ് ചെയ്യാൻ സഹായിക്കും.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## ഉള്ളടക്ക പട്ടിക

- പരിചയപ്പെടുത്തൽ
  - [Phi കുടുംബത്തിലേക്ക് സ്വാഗതം](./md/01.Introduction/01/01.PhiFamily.md)
  - [നിങ്ങളുടെ പരിസ്ഥിതി ക്രമീകരിക്കൽ](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [പ്രധാന സാങ്കേതികവിദ്യകൾ മനസ്സിലാക്കുക](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi മോഡലുകൾക്കുള്ള AI സുരക്ഷ](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ഹാർഡ്വെയർ പിന്തുണ](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [വിവിധ പ്ലാറ്റ്ഫോമുകളിൽ Phi മോഡലുകളും ലഭ്യതയും](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai ഉം Phi ഉം ഉപയോഗിക്കുക](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub മാർക്കറ്റ്‌പ്ലേസ് മോഡലുകൾ](https://github.com/marketplace/models)
  - [Azure AI മോഡൽ കാറ്റലോഗ്](https://ai.azure.com)

- വ്യത്യസ്ത പരിസ്ഥിതികളിൽ Phi ഇൻഫറൻസ്
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub മോഡലുകൾ](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Microsoft Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI ടൂൾകിറ്റ് VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry ലോക്കൽ](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi കുടുംബത്തിന്റെ ഇൻഫറൻസ്
    - [iOS-ൽ Phi ഇൻഫറൻസ്](./md/01.Introduction/03/iOS_Inference.md)
    - [Android-ൽ Phi ഇൻഫറൻസ്](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson-ൽ Phi ഇൻഫറൻസ്](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC-ൽ Phi ഇൻഫറൻസ്](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework ഉപയോഗിച്ച് Phi ഇൻഫറൻസ്](./md/01.Introduction/03/MLX_Inference.md)
    - [ലോക്കൽ സെർവറിൽ Phi ഇൻഫറൻസ്](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI ടൂൾകിറ്റ് ഉപയോഗിച്ച് റിമോട്ട് സെർവറിൽ Phi ഇൻഫറൻസ്](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust ഉപയോഗിച്ച് Phi ഇൻഫറൻസ്](./md/01.Introduction/03/Rust_Inference.md)
    - [ലോക്കലിൽ Phi-യുടെ വിഷൻ ഇൻഫറൻസ്](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (അധികൃത പിന്തുണ) ഉപയോഗിച്ച് Phi ഇൻഫറൻസ്](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi കുടുംബത്തിന്റെ ക്വാണ്ടിഫിക്കേഷൻ](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ഉപയോഗിച്ച് Phi-3.5 / 4 ക്വാണ്ടൈസിംഗ്](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime-നുള്ള Generative AI വിപുലീകരണങ്ങൾ ഉപയോഗിച്ച് Phi-3.5 / 4 ക്വാണ്ടൈസിംഗ്](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ഉപയോഗിച്ച് Phi-3.5 / 4 ക്വാണ്ടൈസിംഗ്](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework ഉപയോഗിച്ച് Phi-3.5 / 4 ക്വാണ്ടൈസിംഗ്](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi மதிப்பீடு
    - [ഉത്തരം നൽകുന്ന AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [മൈക്രോസോഫ്റ്റ് ഫൗണ്ട്രി വിലയിരുത്തലിനായി](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow ഉപയോഗിച്ച് വിലയിരുത്തൽ](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search ഉപയോഗിച്ച് RAG
    - [Phi-4-mini, Phi-4-multimodal(RAG) Azure AI Search-ലുമായി എങ്ങനെ ഉപയോഗിക്കാമെന്നത്](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi ആപ്ലിക്കേഷൻ ഡവലപ്പ്മെന്റ് സാമ്പിളുകൾ
  - എഴുത്ത് & ചാറ്റ് ആപ്ലിക്കേഷനുകൾ
    - Phi-4 സാമ്പിളുകൾ
      - [📓] [Phi-4-mini ONNX മോഡലുമായി ചാറ്റ്](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 ലോക്കൽ ONNX മോഡലുമായി ചാറ്റ് .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [സെമെന്റിക് കെർണൽ ഉപയോഗിച്ച് Phi-4 ONNX ഉപയോഗിക്കുന്ന ചാറ്റ് .NET കൺസോൾ ആപ്പ്](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 സാമ്പിളുകൾ
      - [Phi3, ONNX Runtime Web, WebGPU ഉപയോഗിച്ച് ബ്രൗസറായി ലോക്കൽ ചാറ്റ്‌ബോട്ടോ](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino ചാറ്റ്](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [മൾട്ടി മോഡൽ - ഇൻററാക്ടീവ് Phi-3-മിനി ആൻഡ് OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ഒരു റാപ്പർ നിർമ്മിക്കുകയും Phi-3 MLFlow ഉപയോഗിച്ച് ഉപയോഗിക്കുകയും ചെയ്യുന്നത്](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [മോഡൽsgiving - ONNX റൺടൈം വെബിനായി Phi-3-മിനി മോഡൽ ഒപ്റ്റിമൈസ് ചെയ്യുന്നത് Olive ഉപയോഗിച്ച് എങ്ങനെ](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 ആപ്പ് Phi-3 മിനി-4k-ഇൻസ്ട്രക്ട്-onnx ഉളളത്](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 മൾട്ടി മോഡൽ AI പവേർഡ് നോട്ട്സ് ആപ്പ് സാമ്പിൾ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [കസ്റ്റം Phi-3 മോഡലുകൾ ഫൈൻ-ട്യൂൺ ചെയ്ത് പ്രോമ്പ്റ്റ് ഫ്ലോവിനൊപ്പം എങ്ങനെയാണ് സംയോജിപ്പിക്കുന്നത്](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [മൈക്രോസോഫ്റ്റ് ഫൗണ്ടറിയിൽ പ്രോമ്പ്റ്റ് ഫ്ലോവിനൊപ്പം കസ്റ്റം Phi-3 മോഡലുകൾ ഫൈൻ-ട്യൂൺ ചെയ്ത് സംയോജിപ്പിക്കുന്നത്](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [മൈക്രോസോഫ്റ്റിന്റെ ഉത്തരവാദിത്വമുള്ള AI സിദ്ധാന്തങ്ങളിൽ പോടി വെച്ച് ഫൈൻ-ട്യൂൺ ചെയ്ത Phi-3 / Phi-3.5 മോഡൽ മൈക്രോസോഫ്റ്റ് ഫൗണ്ടറിയിൽ ഫലപ്രദമായി പരിശോധിക്കുക](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-മിനി-ഇൻസ്ട്രക്ട് ലാംഗ്വേജ് പ്രവചന സാമ്പിൾ (ചൈനീസ്/ഇംഗ്ലീഷ്)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-ഇൻസ്ട്രക്ട് WebGPU RAG ചാറ്റ്‌ബോട്ട്](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Phi-3.5-ഇൻസ്ട്രക്ട് ONNX ഉപയോഗിച്ച് പ്രോമ്പ്റ്റ് ഫ്ലോ സൊല്യൂഷൻ നിർമ്മിക്കുന്നതിനായി Windows GPU ഉപയോഗിക്കുന്നത്](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [മൈക്രോസോഫ്റ്റ് Phi-3.5 tflite ഉപയോഗിച്ച് ആൻഡ്രോയ്ഡ് ആപ്പ് നിർമ്മിക്കുക](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [ക്യു & എ .NET ഉദാഹരണം കണിക ONNX Phi-3 മോഡൽ ഉപയോഗിച്ച് Microsoft.ML.OnnxRuntime ഉപയോഗിക്കുന്നത്](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [സെമാന്റിക് കർണൽ Phi-3 ഉപയോഗിച്ച് കൺസോൾ ചാറ്റ് .NET ആപ്പ്](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI ഇൻഫറൻസ് SDK കോഡ് അടിസ്ഥാനമാക്കിയ സാമ്പിളുകൾ 
    - Phi-4 സാമ്പിളുകൾ 
      - [📓] [Phi-4-മൾട്ടിമോഡൽ ഉപയോഗിച്ച് പ്രോജക്ട് കോഡ് സൃഷ്ടിക്കുക](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 സാമ്പിളുകൾ
      - [മൈക്രോസോഫ്റ്റ് Phi-3 കുടുംബവുമായി നിങ്ങളുടെ സ്വന്തം Visual Studio Code GitHub Copilot ചാറ്റ് നിർമ്മിക്കുക](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub മോഡലുകളുമായി Phi-3.5 ഉപയോഗിച്ച് നിങ്ങളുടെ സ്വന്തം Visual Studio Code ചാറ്റ് കോപിലറ്റ് ഏജന്റ് സൃഷ്ടിക്കുക](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - പുരോഗമിച്ച ലജ്ജാപൂർവക സാമ്പിളുകൾ
    - Phi-4 സാമ്പിളുകൾ 
      - [📓] [Phi-4-മിനി-ലജ്ജാപൂർവക അല്ലെങ്കിൽ Phi-4-ലജ്ജാപൂർവക സാമ്പിളുകൾ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [മൈക്രോസോഫ്റ്റ് ഓലീവ് ഉപയോഗിച്ച് Phi-4-മിനി-ലജ്ജാപൂർവക ഫൈൻ-ട്യൂൺ ചെയ്യുന്നത്](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [ആപ്പിൾ MLX ഉപയോഗിച്ച് Phi-4-മിനി-ലജ്ജാപൂർവക ഫൈൻ-ട്യൂൺ ചെയ്യുന്നത്](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub മോഡലുകളുമായി Phi-4-മിനി-ലജ്ജാപൂർവക](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [മൈക്രോസോഫ്റ്റ് ഫൗണ്ടറി മോഡലുകളുമായി Phi-4-മിനി-ലജ്ജാപൂർവക](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - ഡെമോകൾ
      - [Phi-4-മിനി ഡെമോകൾ Hugging Face Spaces-ൽ ഹോസ്റ്റ് ചെയ്തു](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-മൾട്ടിമോഡൽ ഡെമോകൾ Hugginge Face Spaces-ൽ ഹോസ്റ്റ് ചെയ്തു](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - കാഴ്ച സാമ്പിളുകൾ
    - Phi-4 സാമ്പിളുകൾ 
      - [📓] [ചിത്രങ്ങൾ വായിക്കാന്‍ Phi-4-മൾട്ടിമോഡൽ ഉപയോഗിച്ച് കോഡ് സൃഷ്ടിക്കുക](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 സാമ്പിളുകൾ
      -  [📓][Phi-3-കാഴ്ച-ചിത്രം എഴുത്തിൽ നിന്ന് എഴുത്തിലേക്ക്](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-കാഴ്ച-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-കാഴ്ച CLIP എംബെഡ്ഡിങ്ങ്](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ഡെമോ: Phi-3 റീസൈക്ലിങ്](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-കാഴ്ച - ദൃശ്യ ഭാഷാ സഹായി - Phi3-കാഴ്ചയും OpenVINO-യും ഉപയോഗിച്ച്](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 ദൃശ്യം Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 ദൃശ്യം OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 ദൃശ്യം മൾട്ടി-ഫ്രെയിം അല്ലെങ്കിൽ മൾട്ടി-ചിത്രം സാമ്പിൾ](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 ദൃശ്യം ഒരു ലൊക്കൽ ONNX മോഡൽ Microsoft.ML.OnnxRuntime .NET ഉപയോഗിച്ച്](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [മെനു അടിസ്ഥാനമാക്കിയ Phi-3 ദൃശ്യം ലൊക്കൽ ONNX മോഡൽ Microsoft.ML.OnnxRuntime .NET ഉപയോഗിച്ച്](../../md/04.HOL/dotnet/src/LabsPhi304)

  - ലജ്ജാപൂർവക-കാഴ്ച സാമ്പിളുകൾ
    - Phi-4-ലജ്ജാപൂർവക-കാഴ്ച-15B 
      - [📓] [Phi-4-ലജ്ജാപൂർവക-കാഴ്ച-15B ഉപയോഗിച്ച് ജെവാക്കിങ് കണ്ടെത്തൽ](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb)
      - [📓] [Phi-4-ലജ്ജാപൂർവക-കാഴ്ച-15B ഉപയോഗിച്ച് ഗണിതം](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb)
      - [📓] [Phi-4-ലജ്ജാപൂർവക-കാഴ്ച-15B ഉപയോഗിച്ച് UI കണ്ടെത്തലും](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb)

  - ഗണിത സാമ്പിളുകൾ
    -  Phi-4-മിനി-ഫ്ലാഷ്-ലജ്ജാപൂർവക-ഇൻസ്ട്രക്ട് സാമ്പിളുകൾ  [Phi-4-മിനി-ഫ്ലാഷ്-ലജ്ജാപൂർവക-ഇൻസ്ട്രക്ട് ഉപയോഗിച്ചുള്ള ഗണിത ഡെമോ](./md/02.Application/09.Math/MathDemo.ipynb)

  - ശബ്ദ സാമ്പിളുകൾ
    - Phi-4 സാമ്പിളുകൾ 
      - [📓] [Phi-4-മൾട്ടിമോഡൽ ഉപയോഗിച്ച് ശബ്ദ ട്രാൻസ്‌ക്രിപ്റ്റുകൾ എടുക്കുന്നു](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-മൾട്ടിമോഡൽ ശബ്ദ സാമ്പിൾ](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-മൾട്ടിമോഡൽ ശബ്ദ വിവർത്തനം സാമ്പിൾ](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET കൺസോൾ ആപ്ലിക്കേഷൻ Phi-4-മൾട്ടിമോഡൽ ശബ്ദം വിശകലനം ചെയ്യുന്നതിനും ട്രാൻസ്‌ക്രിപ്റ്റ് സൃഷ്ടിക്കുന്നതിനും ഉപയോഗിക്കുന്നു](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE സാമ്പിളുകൾ
    - Phi-3 / 3.5 സാമ്പിളുകൾ
      - [📓] [Phi-3.5 സ്പെഷ്യലിസ്റ്റ് മിശ്രിത മോഡലുകൾ (MoEs) സോഷ്യൽ മീഡിയ സാമ്പിൾ](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, LlamaIndex ഉപയോഗിച്ചുള്ള Retrieval-Augmented Generation (RAG) പൈപ്പ്‌ലൈൻ നിർമ്മാണം](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - ഫംഗ്ഷൻ കോളിംഗ് സാമ്പിളുകൾ
    - Phi-4 സാമ്പിളുകൾ 🆕
      -  [📓] [Phi-4-മിനി ഉപയോഗിച്ച് ഫംഗ്ഷൻ കോളിംഗ് ഉപയോഗിക്കുന്നു](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-മിനി ഉപയോഗിച്ച് മൾട്ടി-ഏജന്റുമാർ സൃഷ്ടിക്കാൻ ഫംഗ്ഷൻ കോളിംഗ് ഉപയോഗിക്കുന്നു](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama-വുമായുള്ള ഫംഗ്ഷൻ കോളിംഗ് ഉപയോഗിക്കുന്നത്](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX-വുമായുള്ള ഫംഗ്ഷൻ കോളിംഗ് ഉപയോഗിക്കുന്നു](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - മൾട്ടിമോഡൽ മിക്സിങ് സാമ്പിളുകൾ
    - Phi-4 സാമ്പിളുകൾ 🆕
      -  [📓] [ടെക്നോളജി പത്രകാരൻ ആയി Phi-4-മൾട്ടിമോഡൽ ഉപയോഗിക്കുന്നത്](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET കൺസോൾ ആപ്ലിക്കേഷൻ Phi-4-മൾട്ടിമോഡൽ ഉപയോഗിച്ച് ചിത്രങ്ങൾ വിശകലനം ചെയ്യുന്നതിന്](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- ഫൈൻ-ട്യൂണിംഗ് Phi സാമ്പിളുകൾ
  - [ഫൈൻ-ട്യൂണിംഗ് സീനാരിയോകൾ](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ഫൈൻ-ട്യൂണിംഗ് vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 വ്യവസായ വിദഗ്ധനാകാൻ അനുവദിക്കുക ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS കോഡ് എഐ ടൂൾകിറ്റ് ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [അസ്യൂർ മെഷീൻ ലേണിംഗ് സർവീസ് ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Microsoft Foundry ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive ഉപയോഗിച്ച് ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive ഹാൻഡ്‌സ്-ഓൺ ലാബ് ഉപയോഗിച്ച് ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias ഉപയോഗിച്ച് Phi-3-vision ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX ഫ്‌റെയിംവർക്ക് ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision ഫൈൻ-ട്യൂണിംഗ് (അധികൃത പിന്തുണ)](./md/03.FineTuning/FineTuning_Vision.md)
  - [കൈറ്റോ AKS, അസ്യൂർ കന്റെയ്‌നർമാർ (അധികൃത പിന്തുണ) ഉപയോഗിച്ച് ഫൈ-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_Kaito.md)
  - [ഫൈ-3 ആൻഡ് 3.5 വിഷൻ ഫൈൻ-ട്യൂണിംഗ്](https://github.com/2U1/Phi3-Vision-Finetune)

- ഹാൻഡ്സ് ഓൺ ലാബ്
  - [അത്യാധുനിക മോഡലുകൾ പഠനം: LLMകൾ, SLMകൾ, പ്രാദേശിക ഡെവലപ്പ്മെന്റ് ഉൾപ്പെടെ](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP ശേഷി തുറക്കൽ: Microsoft Olive ഉപയോഗിച്ച് ഫൈൻ-ട്യൂണിംഗ്](https://github.com/azure/Ignite_FineTuning_workshop)

- അക്കാദമിക് ഗവേഷണ പേപ്പറുകളും പ്രസിദ്ധീകരണങ്ങളും
  - [Textbooks Are All You Need II: phi-1.5 സാങ്കേതിക റിപ്പോർട്ട്](https://arxiv.org/abs/2309.05463)
  - [Phi-3 സാങ്കേതിക റിപ്പോർട്ട്: നിങ്ങളുടെ ഫോണിൽ ലോക്കലായി എല്ലാ കഴിവുള്ള ഭാഷാ മോഡൽ](https://arxiv.org/abs/2404.14219)
  - [Phi-4 സാങ്കേതിക റിപ്പോർട്ട്](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini സാങ്കേതിക റിപ്പോർട്ട്: കംപാക്റ്റും ശക്തിയേറിയ മൾട്ടിമോഡൽ ഭാഷാ മോഡലുകൾ Mixture-of-LoRAs വഴി](https://arxiv.org/abs/2503.01743)
  - [കാറിനായി ചെറിയ ഭാഷാ മോഡലുകൾ ഫംഗ്ഷൻ-കോൾക്കായി ഓപ്റ്റിമൈസ് ചെയ്യുന്നു](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3-ന്റെ मल्टिൾ ചോയ്സ് ക്വഷൻ ആൻസറിംഗിനുള്ള ഫൈൻ-ട്യൂണിംഗ്: രീതിശാസ്ത്രം, ഫലങ്ങൾ, വെല്ലുവിളികൾ](https://arxiv.org/abs/2501.01588)
  - [Phi-4-റീസണിംഗ് സാങ്കേതിക റിപ്പോർട്ട്](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mMini-റീസണിംഗ് സാങ്കേതിക റിപ്പോർട്ട്](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi മോഡലുകൾ ഉപയോഗിക്കൽ

### Microsoft Foundry-യിൽ Phi

നിങ്ങളുടെ വ്യത്യസ്ത ഹാർഡ്വെയർ ഉപകരണങ്ങളിൽ Microsoft Phi എങ്ങനെ ഉപയോഗിക്കാമെന്ന്, എ2ഇ പരിഹാരങ്ങൾ എങ്ങനെ നിർമ്മിക്കാമെന്ന് നിങ്ങൾക്ക് പഠിക്കാം. Phi സ്വയം അനുഭവിക്കാനായി, മോഡലുകൾ ഉപയോഗിച്ച് കളിച്ചുകൊണ്ട് നിങ്ങളുടെ സ്ഥിതിഗതികൾക്കായി Phi കസ്റ്റമൈസ് ചെയ്യാൻ [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ഉപയോഗിക്കാമെന്ന് നിങ്ങൾക്ക് പഠിക്കാം. കൂടുതൽ അറിവിന് [Microsoft Foundry]-ന്റെ തുടക്കം / QuickStart കാണുക (/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**പ്ലേഗ്രൗണ്ട്**  
ഓരോ മോഡലിനും പരീക്ഷിക്കാൻ സങ്കല്പിതമായൊരു [Azure AI Playground](https://aka.ms/try-phi3) ഉണ്ട്.

### GitHub മോഡലുകളിൽ Phi

നിങ്ങളുടെ വിവിധ ഹാർഡ്വെയർ ഉപകരണങ്ങളിൽ Microsoft Phi എങ്ങനെ ഉപയോഗിക്കാമെന്ന്, എ2ഇ പരിഹാരങ്ങൾ എങ്ങനെ നിർമ്മിക്കാമെന്ന് നിങ്ങൾക്ക് പഠിക്കാം. Phi സ്വയം അനുഭവിക്കാനായി, മോഡൽ ഉപയോഗിച്ച് കളിച്ചുകൊണ്ട് നിങ്ങളുടെ സ്ഥിതിഗതികൾക്കായി Phi കസ്റ്റമൈസ് ചെയ്യാൻ [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ഉപയോഗിക്കാവുന്നതാണ്. കൂടുതൽ അറിവിന് [GitHub Model Catalog]-ന്റെ തുടക്കം / QuickStart കാണുക (/md/02.QuickStart/GitHubModel_QuickStart.md).

**പ്ലേഗ്രൗണ്ട്**  
ഓരോ മോഡലിനും പരീക്ഷിക്കാൻ പ്രത്യേക [പ്ലേഗ്രൗണ്ട്](/md/02.QuickStart/GitHubModel_QuickStart.md) ഉണ്ട്.

### Hugging Face-ൽ Phi

മോഡൽ [Hugging Face](https://huggingface.co/microsoft) ൽ ലഭ്യമാണ്.

**പ്ലേഗ്രൗണ്ട്**  
[Hugging Chat പ്ലേഗ്രൗണ്ട്](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 മറ്റ് കോഴ്‌സുകൾ

നമ്മുടെ ടീം മറ്റ് കോഴ്‌സുകളും ഒരുക്കുന്നു! പരിശോധിക്കുക:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain  
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)  
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)  
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)  
---

### Azure / Edge / MCP / ഏജന്റുമാർ  
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)  
---

### ജനറേറ്റീവ് AI സീരീസ്  
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)  
---

### കോർ ലേണിങ്  
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)  
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  
---

### കോപൈലറ്റ് സീരീസ്  
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## ഉത്തരവാദിത്വമുള്ള AI

Microsoft നമ്മുടെ ഉപഭോക്താക്കൾ AI ഉൽപ്പന്നങ്ങൾ ഉത്തരവാദിത്വത്തോടെ ഉപയോഗിക്കാൻ സഹായിക്കാനും, നമുക്ക് നിന്ന് പഠനങ്ങൾ പങ്കുവെക്കാനും, ട്രാൻസ്‌പറൻസി നോട്ടുകളും പ്രഭാവം വിലയിരുത്തലുകളും പോലുള്ള ഉപകരണങ്ങളിലൂടെ വിശ്വാസം അടങ്ങിയ പങ്കാളിത്തങ്ങൾ സൃഷ്ടിക്കാനും പ്രതിജ്ഞാബദ്ധമാണ്. ഈ പിന്തുണകൾ [https://aka.ms/RAI](https://aka.ms/RAI) എന്നത് കാണാവുന്നതാണ്.  
Microsoft‍റെ ഉത്തരവാദിത്വ AI സമീപനം നീതിമാന്മാരാകൽ, വിശ്വാസ്യതയും സുരക്ഷയും, സ്വകാര്യതയും സുരക്ഷയും, ഉൾക്കൊള്ളൽ, സുതാര്യത, ഉത്തരവാദിത്വം തുടങ്ങിയ AI സ 원 ത്തുകളിലടിസ്ഥാനമാണ്.

ഈ ഉദാഹരണത്തിൽ ഉപയോഗിച്ച വലിയ പരിധിയിലെ സ്വാഭാവിക ഭാഷ, ചിത്രങ്ങൾ, ശബ്ദ മോഡലുകൾ അനീതി, വിശ്വാസ്യതകളില്ലായ്ന്ന് അല്ലെങ്കിൽ അപമാനകരമായി പെരുമാറാൻ സാധ്യതയുള്ളതിനാൽ കേടുപാടുകൾ ഉണ്ടാക്കും. ദയവായി അപകടങ്ങളും പരിമിതികളും അറിയാൻ [Azure OpenAI സേവന ട്രാൻസ്‌പറൻസി നോട്ടും](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) പരിശോധിക്കുക.
ഈ അപകടങ്ങൾ കുറയ്ക്കാൻ ശിപാർസുചെയ്ത സമീപനം നിങ്ങളുടെ വാസ്തുവിദ്യയിൽ സുരക്ഷാ സംവിധാനം ഉൾപ്പെടുത്തുകയാണ്, ഇത് ഹാനികരമായ പെരുമാറ്റം കണ്ടെത്തിയും തടഞ്ഞു നിർത്തിയും കഴിയും. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) സ്വതന്ത്രമായ ഒറ്റ പാളി സംരക്ഷണം നൽകുന്നു, ആപ്ലിക്കേഷനുകളും സേവനങ്ങളിലും ഹാനികരമായ ഉപയോക്താവ് സൃഷ്ടിച്ചും AI സൃഷ്ടിച്ചും ഉള്ള ഉള്ളടക്കം കണ്ടെത്താൻ കഴിയും. Azure AI Content Safety ല് ടെക്സ്റ് ಮತ್ತು ഇമേജ് API-കൾ ഉൾക്കൊള്ളുന്നു, അവ ഹാനികരമായ ഉള്ളടക്കം കണ്ടെത്താൻ സഹായിക്കുന്നു. Microsoft Foundry-യിൽ, Content Safety സേവനം വിവിധ രൂപത്തിലുള്ള ഹാനികരമായ ഉള്ളടക്കം കണ്ടെത്തുന്നതിനുള്ള സാമ്പിൾ കോഡ് കാണാനും പരീക്ഷിക്കാനും സഹായിക്കുന്നു. താഴെ ഡോക്യുമെന്റേഷനിലുള്ള [ക്വിക്ക്‌സ്റ്റാർട്ട്](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) സേവനത്തിന് അഭ്യർത്ഥനകൾ പടിഞ്ഞിരിക്കുന്നു.

ആനുകൂല്യമായി പരിഗണിക്കേണ്ട മറ്റൊരു ഘടകം ആപ്ലിക്കേഷൻ സമഗ്ര പ്രകടനമാണ്. മൾട്ടി-മോഡൽ, മൾട്ടി-മോഡൽ ആപ്ലിക്കേഷനുകളുടെ സാഹചര്യത്തിൽ, പ്രകടനം എന്ന് അർത്ഥമാക്കുന്നത് നിങ്ങൾക്കും നിങ്ങളുടെ ഉപയോക്താക്കളും പ്രതീക്ഷിക്കുന്ന പോലെ സിസ്റ്റം പ്രവർത്തിക്കണമെന്നും, ഹാനികരമായ ഔട്ട്പുട്ടുകൾ സൃഷ്ടിക്കാതിരിക്കണമെന്നും ആണ്. നിങ്ങളുടെ ആപ്ലിക്കേഷന്റെ സമഗ്ര പ്രകടനം [പ്രകടനവും ഗുണനിലവാരവും അപകടം സുരക്ഷാ വിവരങ്ങളും കുറിച്ച് സ്റ്റാൻഡേർഡ് വിലയിരുത്തലുകളിലൂടെ](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) വിലയിരുത്തുന്നത് അത്യന്താപേക്ഷിതമാണ്. നിങ്ങൾക്ക് അതോടൊപ്പം [കസ്റ്റം വിലയിരുത്തലുകൾ](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) സൃഷ്ടിച്ചും അവലോകനം നടത്തിയും ചെയ്യാനുള്ള കഴിവുണ്ട്.

നിങ്ങളുടെ AI ആപ്ലിക്കേഷൻ വികസന പരിസ്ഥിതിയിൽ [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ഉപയോഗിച്ച് നിങ്ങൾക്ക് വിലയിരുത്താം. ഒരു ടെസ്റ്റ് ഡാറ്റാസെറ്റ് അല്ലെങ്കിൽ ലക്ഷ്യം നൽകിയാൽ, നിങ്ങളുടെ ജനറേറ്റീവ് AI ആപ്ലിക്കേഷൻ ജനറേഷനുകൾ ഉൾപ്പെടുത്തിയിട്ടുള്ളവയോ നിങ്ങൾ തെരഞ്ഞെടുത്ത കസ്റ്റം വിലയിരുത്തലുകളോ ഉപയോഗിച്ച് കണക്ക് കൂട്ടി അളക്കപ്പെടും. നിങ്ങളുടെ സിസ്റ്റം വിലയിരുത്താൻ azure ai evaluation sdk തുടങ്ങി തുടങ്ങി വേണ്ടി, നിങ്ങൾക്ക് താഴെപ്പറയുന്ന [ക്വിക്ക്‌സ്റ്റാർട്ട് ഗൈഡ്](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) പിന്തുടരാം. ഒരു വിലയിരുത്തൽ റൺ പ്രവർത്തിപ്പിച്ചശേഷം, നിങ്ങൾക്ക് [Microsoft Foundry-യിൽ ഫലങ്ങൾ ദൃശ്യമാക്കാം](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## ട്രേഡ്മാർക്കുകൾ

ഈ പ്രോജക്ടിൽ പ്രോജക്ടുകൾ, ഉൽപ്പന്നങ്ങൾ, സേവനങ്ങൾ എന്നിവയുടെ ട്രേഡ്മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകൾ ഉണ്ടാകാവുന്നതാണ്. മൈക്രോസോഫ്റ്റ് ട്രേഡ്മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകൾ അനുമതിപ്‌തു ഉപയോഗിക്കുന്നത് [Microsoft-ന്റെ ട്രേഡ്മാർക് & ബ്രാൻഡ് മാർഗനിർദ്ദേശങ്ങൾ](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) അനുസരിച്ച് ആയിരിക്കണം.
മൈക്രോസോഫ്റ്റ് ട്രേഡ്മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകൾ ഉപയോഗം കൊണ്ടുള്ള തിരുത്തിയ പതിപ്പുകളിൽ ആശയം അല്ലെങ്കിൽ Microsoft-ന്റെ കായികത ഉറപ്പില്ലാതാക്കരുത്. മൂന്നാർക്കുള്ള ട്രേഡ്മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകൾ ഉപയോഗിക്കുമ്പോൾ ആ തൃतीयരുടെ നയങ്ങൾ പ്രധാനം ചെയ്യും.

## സഹായം നേടുക

AI ആപ്പുകൾ നിർമ്മിക്കുന്നതിൽ നിങ്ങൾ കുടുങ്ങുകയോ ചോദ്യങ്ങളുണ്ടെങ്കിലോ, ചേരുക:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

നിഗമനസമ്മതം നൽകാൻ അല്ലെങ്കിൽ പിഴവുകളുണ്ടെങ്കിൽ:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസ്വീകാരം**:  
ഈ പ്രമാണം AI പരിഭാഷ സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം ശരിയായ വിവർത്തനത്തിനായി ശ്രമിക്കുമ്പോഴും, യന്ത്രം ചെയ്ത വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുള്ളതിനാൽ ദയവായി ശ്രദ്ധിക്കുക. സ്വതന്ത്രമായ ഭാഷയിലുള്ള പ്രാഥമിക പ്രമാണം പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശിപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽനിന്ന് വരുന്ന എന്തു തെറ്റിദ്ധാരണകളെയും കൃത്യമായ വ്യാഖ്യാനങ്ങളെയും കാരണം ഞങ്ങൾ ഉത്തരവാദിത്വം ഏറ്റെടുക്കുന്നില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->