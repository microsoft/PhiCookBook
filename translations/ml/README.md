<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef3a50368712b1a7483d0def1f70c490",
  "translation_date": "2025-12-21T15:17:07+00:00",
  "source_file": "README.md",
  "language_code": "ml"
}
-->
# Phi കുക്ക്ബുക്ക്: Microsoft's Phi മോഡലുകളോടുള്ള പ്രായോഗിക ഉദാഹരണങ്ങൾ

[![GitHub Codespaces-ൽ സാംപിളുകൾ തുറന്ന് ഉപയോഗിക്കുക](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers-ൽ തുറക്കുക](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub സംഭാവകർ](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ഇഷ്യൂസുകൾ](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub പുൾ അഭ്യർത്ഥനകൾ](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![പി.ആർ-കൾ സ്വാഗതം](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub വാച്ചേഴ്‌സ്](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ഫോർക്കുകൾ](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub സ്‌റ്റാർസ്](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi മൈക്രോസോഫ്റ്റ് വികസിപ്പിച്ച ഒരു ഓപ്പൺ സോഴ്സ് എഐ മോഡലുകളുടെ പരമ്പരയാണ്.

Phi ഇപ്പോൾ ഏറ്റവും ശക്തിയും ചെലവു-പ്രയോഗക്ഷമതയുമുള്ള സ്മോൾ ഭാഷാ മോഡലുകളിലൊന്നാണ് (SLM), ബഹുഭാഷാ, നിര്ണയശേഷി, ടെക്സ്റ്/ചാറ്റ് ജനറേഷൻ, കോഡിംഗ്, ഇമേജുകൾ, ഓഡിയോ എന്നിവയിലും മറ്റു السينാരികളിലും വളരെ നല്ല ബൻച്മാർക്കുകൾ കാണിക്കുന്നു.

Phi നെ ക്ലൗഡിലോ എഡ്ജ് ഡിവൈസുകളിലോ വിന്യസിച്ച്, സ محدود കമ്പ്യൂട്ടിങ് ശേഷിയുള്ള സാഹചര്യമീറ്റിലും നിങ്ങൾ എളുപ്പത്തിൽ ജനറേറ്റീവ് എഐ അപ്ലിക്കേഷനുകൾ നിർമ്മിക്കാവുന്നതാണ്.

ഈ വിഭവങ്ങൾ ഉപയോഗിച്ച് ആരംഭിക്കാൻ താഴെയുള്ള നടപടികൾ പിന്തുടരുക :
1. **റിപോസിറ്ററി ഫോർക്ക് ചെയ്യുക**: Click [![GitHub ഫോർക്കുകൾ](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **റിപോസിറ്ററി ക്ലോൺ ചെയ്യുക**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord കമ്മ്യൂണിറ്റിയിൽ ചേരുക, വിദഗ്ധരെയും മറ്റ് ഡെവലപ്പർമാരെയും പരിചയപ്പെടുക**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![കവർ](../../translated_images/cover.eb18d1b9605d754b.ml.png)

### 🌐 ബഹുഭാഷാ പിന്തുണ

#### GitHub Action വഴി പിന്തുണ (സ്വയംക്രമീകരിച്ചും എപ്പോഴും പുതുക്കിപ്പെടുന്ന)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[അറബിക്](../ar/README.md) | [ബംഗാളി](../bn/README.md) | [ബുല്ഗേറിയൻ](../bg/README.md) | [ബർമീസ് (മ്യാന്മാർ)](../my/README.md) | [ചൈനീസ് (ലളിതീകൃതം)](../zh/README.md) | [ചൈനീസ് (പരമ്പരാഗതം, ഹോങ്കോങ്)](../hk/README.md) | [ചൈനീസ് (പരമ്പരാഗതം, മക്കാവു)](../mo/README.md) | [ചൈനീസ് (പരമ്പരാഗതം, തായ്‍വാൻ)](../tw/README.md) | [ക്രൊവേഷ്യൻ](../hr/README.md) | [ചെക്ക്](../cs/README.md) | [ഡാനിഷ്](../da/README.md) | [ഡച്ച്](../nl/README.md) | [എസ്റ്റോണിയൻ](../et/README.md) | [ഫിന്നിഷ്](../fi/README.md) | [ഫ്രഞ്ച്](../fr/README.md) | [ജർമ്മൻ](../de/README.md) | [ഗ്രീക്](../el/README.md) | [ഹീബ്രു](../he/README.md) | [ഹിന്ദി](../hi/README.md) | [ഹംഗേറിയൻ](../hu/README.md) | [ഇൻഡൊനേഷ്യൻ](../id/README.md) | [ഇറ്റാലിയൻ](../it/README.md) | [ജാപ്പനീസ്](../ja/README.md) | [കന്നഡ](../kn/README.md) | [കൊറിയൻ](../ko/README.md) | [ലിതുവേനിയൻ](../lt/README.md) | [മലായ്](../ms/README.md) | [മലയാളം](./README.md) | [മറാത്തി](../mr/README.md) | [നേപ്പാളി](../ne/README.md) | [നൈജീരിയൻ പിഡ്ജിൻ](../pcm/README.md) | [നോർവീജിയൻ](../no/README.md) | [പെർഷ്യൻ (ഫാർസി)](../fa/README.md) | [പോളിഷ്](../pl/README.md) | [പോർചുഗീസ് (ബ്രസീൽ)](../br/README.md) | [പോർചുഗീസ് (പോർച്ചുഗൽ)](../pt/README.md) | [പഞ്ചാബി (ഗുരുമുഖി)](../pa/README.md) | [റൊമാനിയൻ](../ro/README.md) | [റഷ്യൻ](../ru/README.md) | [സെർബിയൻ (സിറിലിക്)](../sr/README.md) | [സ്വലോവാക്](../sk/README.md) | [സ്ലോവേനിയൻ](../sl/README.md) | [സ്പാനിഷ്](../es/README.md) | [സ്വാഹിലി](../sw/README.md) | [സ്വീഡിഷ്](../sv/README.md) | [തഗാലോഗ് (ഫിലിപ്പീൻസ്)](../tl/README.md) | [തമിഴ്](../ta/README.md) | [తెలుగు](../te/README.md) | [തായ്](../th/README.md) | [തുർക്കിഷ്](../tr/README.md) | [ഉക്രെയ്നിയൻ](../uk/README.md) | [ഉറുദു](../ur/README.md) | [വിയറ്റ്നാമീസ്](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## ഉള്ളടക്ക പട്ടിക

- പരിചയം
  - [Phi കുടുംബത്തിലേക്ക് സ്വാഗതം](./md/01.Introduction/01/01.PhiFamily.md)
  - [നിങ്ങളുടെ പരിസ്ഥിതി ക്രമീകരിക്കൽ](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [പ്രധാന സാങ്കേതികവിദ്യകൾ മനസ്സിലാക്കുക](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi മോഡലുകൾക്കുള്ള AI സുരക്ഷ](./md/01.Introduction/01/01.AISafety.md)
  - [Phi ഹാർഡ്‌വെയർ പിന്തുണ](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [പ്ലാറ്റ്‌ഫോമുകൾവ്യാപകമായി Phi മോഡലുകളും ലഭ്യതയും](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-aiയും Phiയും ഉപയോഗിക്കൽ](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace മോഡലുകൾ](https://github.com/marketplace/models)
  - [Azure AI മോഡൽ കാറ്റലോഗ്](https://ai.azure.com)

- വിവിധ പരിസ്ഥിതികളിൽ Phi ഇൻഫറൻസ്
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub മോഡലുകൾ](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry മോഡൽ കാറ്റലോഗ്](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry ലോക്കൽ](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi കുടുംബത്തിലെ ഇൻഫറൻസ്
    - [iOS-ൽ Phi ഇൻഫറൻസ്](./md/01.Introduction/03/iOS_Inference.md)
    - [Android-ൽ Phi ഇൻഫറൻസ്](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson-ൽ Phi ഇൻഫറൻസ്](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC-യിൽ Phi ഇൻഫറൻസ്](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX ഫ്രെയിംവർക്കുമായി Phi ഇൻഫറൻസ്](./md/01.Introduction/03/MLX_Inference.md)
    - [লোকൽ സെർവറിൽ Phi ഇൻഫറൻസ്](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit ഉപയോഗിച്ച് റിമോട്ട് സെർവറിൽ Phi ഇൻഫറൻസ്](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust ഉപയോഗിച്ച് Phi ഇൻഫറൻസ്](./md/01.Introduction/03/Rust_Inference.md)
    - [लोकൽ വാതാവരണത്തിൽ Phi-ദൃഷুটি (Vision) ഇൻഫറൻസ്](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers ഉപയോഗിച്ച് Phi ഇൻഫറൻസ് (അഫീഷ്യൽ പിന്തുണ)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi കുടുംബത്തെ ക്വാണ്ടിഫൈ ചെയ്യൽ](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp ഉപയോഗിച്ച് Phi-3.5 / 4 ക്വാണ്ടൈസിങ്](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime-ലെ Generative AI എക്സ്റ്റൻഷനുകൾ ഉപയോഗിച്ച് Phi-3.5 / 4 ക്വാണ്ടൈസിങ്](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO ഉപയോഗിച്ച് Phi-3.5 / 4 ക്വാണ്ടൈസിങ്](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX ഫ്രെയിംവർക്കിലൂടെ Phi-3.5 / 4 ക്വാണ്ടൈസിങ്](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi മൂല്യനിർണ്ണയം
    - [Responsible AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [മൂല്യനിർണ്ണയത്തിനായി Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [വിലയിരുത്തലിനായി Promptflow ഉപയോഗിക്കൽ](./md/01.Introduction/05/Promptflow.md)
 
- RAG Azure AI Search ഉപയോഗിച്ച്
    - [Azure AI Search ഉപയോഗിച്ച് Phi-4-mini және Phi-4-multimodal(RAG) ഉപയോഗിക്കുന്നത് എങ്ങനെ](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi അപ്ലിക്കേഷൻ ഡവലപ്പ്മെന്റ് സാംപിളുകൾ
  - ടെക്സ്റ്റ് & ചാറ്റ് അപ്ലിക്കേഷനുകൾ
    - Phi-4 സാമ്പിളുകൾ 🆕
      - [📓] [Phi-4-mini ONNX മോഡലുമായി ചാറ്റ്](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 ലോക്കൽ ONNX മോഡലുമായുള്ള ചാറ്റ് .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Semantic Kernel ഉപയോഗിച്ച് Phi-4 ONNX ഉപയോഗിക്കുന്ന .NET കൺസോൾ ആപ്പ്](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 സാമ്പിളുകൾ
      - [Phi3, ONNX Runtime Web, WebGPU ഉപയോഗിച്ച് ബ്രൗസറിൽ ലോക്കൽ ചാറ്റ്ബോട്ട്](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino ചാറ്റ്](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [മൾട്ടി മോഡൽ - ഇന്ററാക്ടീവ് Phi-3-mini மற்றும் OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - ഒരു റാപ്പർ നിർമ്മിച്ച് MLFlow ഉപയോഗിച്ച് Phi-3 ഉപയോഗിക്കൽ](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [മോഡൽ ഓപ്റ്റിമൈസേഷൻ - Olive ഉപയോഗിച്ച് ONNX Runtime Web-കായി Phi-3-min മോഡൽ എങ്ങനെ ഒപ്റ്റിമൈസ് ചെയ്യാം](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx ഉപയോഗിച്ചുള്ള WinUI3 ആപ്പ്](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 മൾട്ടി മോഡൽ AI-സജ്ജ നോട്ട്സ് ആപ്പ് സാമ്പിൾ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Prompt flow ഉപയോഗിച്ച് കസ്റ്റം Phi-3 മോഡലുകൾ ഫൈന്റ്റ്യൂൺ ചെയ്ത് സംയോജിപ്പിക്കുക](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry-ൽ Prompt flow ഉപയോഗിച്ച് കസ്റ്റം Phi-3 മോഡലുകൾ ഫൈന്റ്റ്യൂൺ ചെയ്ത് സംയോജിപ്പിക്കുക](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft-ന്റെ ഉത്തരവാദിത്വപരമായ AI സിദ്ധാന്തങ്ങളെ കേന്ദ്രീകരിച്ച് Azure AI Foundry-യിൽ ഫൈൻ-ട്യൂൺ ചെയ്ത Phi-3 / Phi-3.5 മോഡൽ വിലയിരുത്തുക](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct ഭാഷാ പ്രവചന സാമ്പിൾ (ചൈനീസ്/ഇംഗ്ലീഷ്)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG ചാറ്റ്ബോട്ട്](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU ഉപയോഗിച്ച് Phi-3.5-Instruct ONNX ഉപയോഗിച്ചുള്ള Prompt flow സൊലൂഷൻ ഉണ്ടാക്കൽ](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite ഉപയോഗിച്ച് ആൻഡ്രോയിഡ് ആപ്പ് ഉണ്ടാക്കുന്നത്](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime ഉപയോഗിച്ച് ലോക്കൽ ONNX Phi-3 മോഡൽ ഉപയോഗിക്കുന്ന Q&A .NET ഉദാഹരണം](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernelയും Phi-3-ഉം ഉപയോഗിച്ചുള്ള കോൺസോൾ ചാറ്റ് .NET ആപ്പ്](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK കോഡ് അടിസ്ഥാനത്തിലുള്ള സാമ്പിളുകൾ 
    - Phi-4 സാമ്പിളുകൾ 🆕
      - [📓] [Phi-4-multimodal ഉപയോഗിച്ച് പ്രോജക്ട് കോഡ് സൃഷ്ടിക്കുക](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 സാമ്പിളുകൾ
      - [നിങ്ങളുടെ സ്വന്തം Visual Studio Code GitHub Copilot ചാറ്റ് Microsoft Phi-3 കുടുംബത്തിലൂടെ നിർമ്മിക്കുക](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub മോഡലുകൾ ഉപയോഗിച്ച് Phi-3.5 ഉപയോഗിച്ച് നിങ്ങളുടെ സ്വന്തം Visual Studio Code Chat Copilot ഏജന്റ് സൃഷ്ടിക്കുക](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - അഡ്വാൻസ്ഡ് റീസണിംഗ് സാമ്പിളുകൾ
    - Phi-4 സാമ്പിളുകൾ 🆕
      - [📓] [Phi-4-mini-reasoning അല്ലെങ്കിൽ Phi-4-reasoning സാമ്പിളുകൾ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive ഉപയോഗിച്ച് Phi-4-mini-reasoning ഫൈൻ-ട്യൂൺ ചെയ്യൽ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX ഉപയോഗിച്ച് Phi-4-mini-reasoning ഫൈൻ-ട്യൂൺ ചെയ്യൽ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub മോഡലുകളുമായി Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry മോഡലുകളുമായി Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demos
      - [Hugging Face Spaces-ൽ ഹോസ്റ്റ് ചെയ്യപ്പെട്ട Phi-4-mini ഡെമോകൾ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Hugginge Face Spaces-ൽ ഹോസ്റ്റ് ചെയ്യപ്പെട്ട Phi-4-multimodal ഡെമോകൾ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Vision Samples
    - Phi-4 സാമ്പിളുകൾ 🆕
      - [📓] [ചിത്രങ്ങൾ വായിക്കുകയും കോഡ് സൃഷ്ടിക്കുകയും ചെയ്യാൻ Phi-4-multimodal ഉപയോഗിക്കുക](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 സാമ്പിളുകൾ
      -  [📓][Phi-3-vision - ചിത്രം മുതൽ ടെക്സ്റ്റ് വരെ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP എംബെഡിംഗ്](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 റീസൈക്ലിംഗ്](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - വിസ്വൽ ഭാഷാ അസിസ്റ്റന്റ് - Phi3-Vision மற்றும் OpenVINO ഉപയോഗിച്ച്](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision മൾട്ടി-ഫ്രെയിം അല്ലെങ്കിൽ മൾട്ടി-ഇമേജ് സാമ്പിൾ](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET ഉപയോഗിച്ച് Phi-3 Vision ലോക്കൽ ONNX മോഡൽ](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [മെനു അടിസ്ഥാനത്തിലുള്ള Phi-3 Vision ലോക്കൽ ONNX മോഡൽ Microsoft.ML.OnnxRuntime .NET ഉപയോഗിച്ച്](../../md/04.HOL/dotnet/src/LabsPhi304)

  - ഗണിത സാമ്പിളുകൾ
    -  Phi-4-Mini-Flash-Reasoning-Instruct സാമ്പിളുകൾ 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct ഉപയോഗിച്ചുള്ള ഗണിത ഡെമോ](./md/02.Application/09.Math/MathDemo.ipynb)

  - ഓഡിയോ സാമ്പിളുകൾ
    - Phi-4 സാമ്പിളുകൾ 🆕
      - [📓] [Phi-4-multimodal ഉപയോഗിച്ച് ഓഡിയോ ട്രാൻസ്ക്രിപ്റ്റുകൾ എക്സ്ട്രാക്റ്റ് ചെയ്യൽ](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal ഓഡിയോ സാമ്പിൾ](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal സ്പീച്ച് ട്രാൻസ്ലേഷൻ സാമ്പിൾ](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET കോൺസോൾ അപ്ലിക്കേഷൻ Phi-4-multimodal ഉപയോഗിച്ച് ഒരു ഓഡിയോ ഫയൽ വിശകലനം ചെയ്ത് ട്രാൻസ്ക്രിപ്റ്റ് സൃഷ്ടിക്കാൻ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE സാമ്പിളുകൾ
    - Phi-3 / 3.5 സാമ്പിളുകൾ
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) സോഷ്യൽ മീഡിയ സാമ്പിൾ](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, കൂടാതെ LlamaIndex ഉപയോഗിച്ച് Retrieval-Augmented Generation (RAG) പൈപ്പ്ലൈൻ നിർമ്മിക്കൽ](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - ഫംഗ്ഷൻ കോളിംഗ് സാമ്പിളുകൾ
    - Phi-4 സാമ്പിളുകൾ 🆕
      -  [📓] [Phi-4-mini-യോടുള്ള ഫംഗ്ഷൻ കോളിംഗ് ഉപയോഗിക്കൽ](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini ഉപയോഗിച്ച് മൾട്ടി-ഏജന്റുകൾ സൃഷ്ടിക്കാൻ ഫംഗ്ഷൻ കോളിംഗ് ഉപയോഗിക്കുക](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama-യോടുള്ള ഫംഗ്ഷൻ കോളിംഗ് ഉപയോഗിക്കൽ](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX-യോടുള്ള ഫംഗ്ഷൻ കോളിംഗ് ഉപയോഗിക്കൽ](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - മൾട്ടിമോഡൽ മിക്സിംഗ് സാമ്പിളുകൾ
    - Phi-4 സാമ്പിളുകൾ 🆕
      -  [📓] [ടെക്നോളജി ജേർണലിസ്റ്റായി Phi-4-multimodal ഉപയോഗിക്കുക](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET കോൺസോൾ അപ്ലിക്കേഷൻ Phi-4-multimodal ഉപയോഗിച്ച് ചിത്രങ്ങൾ വിശകലനം ചെയ്യാൻ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi ഫൈൻ-ട്യൂണിംഗ് സാമ്പിളുകൾ
  - [ഫൈൻ-ട്യൂണിംഗ് സാഹചര്യങ്ങൾ](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [ഫൈൻ-ട്യൂണിംഗ് vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [ഫൈൻ-ട്യൂണിംഗ്: Phi-3-നെ വ്യവസായ വിദഗ്ധനാക്കി മാറ്റുക](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code-ക്കുള്ള AI Toolkit ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂൺ ചെയ്യൽ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂൺ ചെയ്യൽ](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂൺ ചെയ്യൽ](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂൺ ചെയ്യൽ](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂൺ ചെയ്യൽ](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂൺ ചെയ്യൽ](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive ഉപയോഗിച്ചുള്ള ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive ഹാൻഡ്സ്-ഓൺ ലാബുമായി ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias ഉപയോഗിച്ച് Phi-3-vision ഫൈൻ-ട്യൂൺ ചെയ്യൽ](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX ഫ്രെയിംവർക്കുമായി Phi-3 ഫൈൻ-ട്യൂൺ ചെയ്യൽ](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision ഫൈൻ-ട്യൂണിംഗ് (ഓഫിഷ്യൽ പിന്തുണ)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS , Azure Containers(official Support) ഉപയോഗിച്ച് Phi-3 ഫൈൻ-ട്യൂണിംഗ്](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 and 3.5 Vision ഫൈൻ-ട്യൂണിംഗ്](https://github.com/2U1/Phi3-Vision-Finetune)

- ഹാൻഡ്സ്-ഓൺ ലാബ്
  - [കട്ടിംഗ്-എജ് മോഡലുകൾ പരിശോധിക്കൽ: LLMs, SLMs, ലോക്കൽ ഡെവലപ്മെന്റ് എന്നിവയും മറ്റും](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP ശേഷി തുറക്കൽ: Microsoft Olive ഉപയോഗിച്ചുള്ള ഫൈൻ-ട്യൂണിംഗ്](https://github.com/azure/Ignite_FineTuning_workshop)

- അക്കാദമിക് ഗവേഷണ ലേഖനങ്ങളും പ്രസിദ്ധീകരണങ്ങളും
  - [Textbooks Are All You Need II: phi-1.5 സാങ്കേതിക റിപ്പോർട്ട്](https://arxiv.org/abs/2309.05463)
  - [Phi-3 സാങ്കേതിക റിപ്പോർട്ട്: നിങ്ങളുടെ ഫോണിൽ ലോക്കലായി പ്രവർത്തിക്കുന്ന 매우 കഴിവുള്ള ഭാഷാ മോഡൽ](https://arxiv.org/abs/2404.14219)
  - [Phi-4 സാങ്കേതിക റിപ്പോർട്ട്](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini സാങ്കേതിക റിപ്പോർട്ട്: Mixture-of-LoRAs മുഖേന കമ്പാക്ട് എന്നാൽ ശക്തമായ ബഹുമാധ്യമ ഭാഷാ മോഡലുകൾ](https://arxiv.org/abs/2503.01743)
  - [വാഹനത്തിനുള്ള ഫംഗ്ഷൻ-കോളിംഗിനായി ചെറുകിട ഭാഷാ മോഡലുകൾ ഓപ്‌ടിമൈസ് ചെയ്യൽ](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) മൾട്ടിപ്പിള്‍-ചോയ്സ് ചോദ്യോത്തരങ്ങൾക്ക് PHI-3 ഫൈൻ-ട്യൂണിംഗ്: രീതി, ഫലങ്ങൾ, വെല്ലുവിളികൾ](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning സാങ്കേതിക റിപ്പോർട്ട്](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning സാങ്കേതിക റിപ്പോർട്ട്](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi മോഡലുകൾ ഉപയോഗിക്കൽ

### Azure AI Foundry-ൽ Phi

നിങ്ങൾ Microsoft Phi എങ്ങനെ ഉപയോഗിക്കാമെന്നും, നിങ്ങളുടെ വ്യത്യസ്ത ഹാർഡ്‌വെയർ ഡിവൈസുകളിൽ E2E പരിഹാരങ്ങൾ എങ്ങനെ നിർമ്മിക്കാമെന്നും പഠിക്കാം. Phi ന്റെ അനുഭവം നിങ്ങളെത്തന്നെ അനുഭവിക്കാൻ, ആദ്യം മോഡലുകൾ പരീക്ഷിച്ച് നിങ്ങളുടെ സാഹചര്യങ്ങൾക്ക് അനുയോജ്യമായി Phi വ്യക്തിഗതമാക്കാൻ [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ഉപയോഗിക്കുക; കൂടുതൽ വിവരങ്ങൾക്ക് Getting Started with [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) കാണുക

**പ്ലേഗ്രൗണ്ട്**
പ്രതിയൊരു മോഡലിനും മോഡൽ പരീക്ഷിക്കാൻ സമർപ്പിത പ്ലേഗ്രൗണ്ട് ഉണ്ട് [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub Models-ൽ Phi

Microsoft Phi എങ്ങനെ ഉപയോഗിക്കാമെന്നും, നിങ്ങളുടെ വ്യത്യസ്ത ഹാർഡ്‌വെയർ ഡിവൈസുകളില്‍ E2E പരിഹാരങ്ങള്‍ എങ്ങനെ നിര്‍മ്മിക്കാമെന്നും നിങ്ങൾക്കു പഠിക്കാവുന്നതാണ്. Phi ന്റെ അനുഭവം സ്വന്തമായി അനുഭവിക്കുവാൻ, ആദ്യം മോഡൽ പരീക്ഷിച്ച് നിങ്ങളുടെ സാഹചര്യങ്ങൾക്ക് അനുയോജ്യമായി Phi താങ്കൾക്ക് ഇഷ്ടാനുസരിച്ച് ക്രമീകരിക്കാൻ [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ഉപയോഗിക്കുക; കൂടുതൽ അറിവിന് Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) നോക്കുക

**പ്ലേഗ്രൗണ്ട്**
പ്രതിയൊരു മോഡലിനും മോഡൽ പരീക്ഷിക്കാൻ സമർപ്പിത [മോഡൽ പരീക്ഷിക്കാൻ ഉള്ള പ്ലേഗ്രൗണ്ട്](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Hugging Face-ൽ Phi

മോഡൽ നിങ്ങൾക്ക് [Hugging Face](https://huggingface.co/microsoft) ലും ലഭ്യമാണ്

**പ്ലേഗ്രൗണ്ട്**
 [Hugging Chat പ്ലേഗ്രൗണ്ട്](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 മറ്റു കോഴ്സുകൾ

ഞങ്ങളുടെ ടീം മറ്റു കോഴ്‌സുകളും നിർമ്മിക്കുന്നു! പരിശോധിച്ചു കാണുക:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j - തുടക്കക്കാർക്ക്](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js - തുടക്കക്കാർക്ക്](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / ഏജന്റുകൾ
[![AZD - തുടക്കക്കാർക്ക്](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI - തുടക്കക്കാർക്ക്](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP - തുടക്കക്കാർക്ക്](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents - തുടക്കക്കാർക്ക്](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![Generative AI - തുടക്കക്കാർക്ക്](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### കോർ ലേണിംഗ്
[![ML - തുടക്കക്കാര്ക്ക്](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![ഡാറ്റ സയൻസ് - തുടക്കക്കാർക്ക്](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI - തുടക്കക്കാർക്ക്](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![സൈബര്‌സെക്യൂരിറ്റി - തുടക്കക്കാർക്ക്](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![വെബ് ഡെവ് - തുടക്കക്കാർക്ക്](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT - തുടക്കക്കാർക്ക്](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR ഡെവലപ്പ്മെന്റ് - തുടക്കക്കാർക്ക്](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot സീരീസ്
[![Copilot - AI പേയർഡ് പ്രോഗ്രാമിംഗിനായി](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot - C#/.NET ഉപയോഗിക്കുവാൻ](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## ഉത്തരവാദിത്വമുള്ള AI 

Microsoft ഞങ്ങളുടെ ഉപഭോക്താക്കൾക്കു നമ്മുടെ AI ഉൽപ്പന്നങ്ങൾ ഉത്തരവാദിത്വത്തോടെ ഉപയോഗിക്കാൻ സഹായിക്കുക, ഞങ്ങളുടെ പഠനങ്ങൾ പങ്കുവെക്കുക, Transparency Notes, Impact Assessments പോലുള്ള ഉപകരണങ്ങളിലൂടെ വിശ്വാസം അടിസ്ഥാനമാക്കി പങ്കാളിത്തങ്ങൾ നിർമ്മിക്കുക എന്നിവയ്ക്ക് പ്രതിജ്ഞാബദ്ധമാണ്. ഇവയിൽ പലതും [https://aka.ms/RAI](https://aka.ms/RAI) ൽ കണ്ടെത്താവുന്നതാണ്.
Microsoftയുടെ ഉത്തരവാദിത്വമുള്ള AI ന്‍റെ സമീപനത്തിന് അടിസ്ഥാനം നോക്കുമ്പോൾ നമ്മുടെ AI 원칙ങ്ങൾ—സമത്വം, വിശ്വാസ്യതയും സുരക്ഷ, ഗോപ്യതയും സുരക്ഷ, ഉൾക്കൊള്ളൽ, പാരദർശിത്വം, ഉത്തരവാദിത്വം—ആണ്.

ഈ സാമ്പിൾവ്യവസ്ഥയിൽ ഉപയോഗിച്ചിരിക്കുന്നതുപോലുളള വലുതളവിലുള്ള സ്വാഭാവിക ഭാഷ, ചിത്രം, ശബ്ദ മോഡലുകൾ അനീതിപൂർണ്ണമായോ, വിശ്വസനീയമല്ലാത്തോ, അപകൃതമായോ പ്രവർത്തിക്കാമെന്ന് കാണുന്നു, ഇതുവഴി ഹാനികരം ഉണ്ടാകാം. അപകടങ്ങൾക്കും പരിമിതികളുമായി ബന്ധപ്പെട്ട് കൂടുതൽ അറിയാൻ [Azure OpenAI സർവീസ് ട്രാൻസ്പെയൻസി കുറിപ്പ്](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) പരിശോധിക്കുക.

ഇതിലെ അപകടങ്ങൾ കുറയ്ക്കാനായി ശുപാർശ ചെയ്യപ്പെട്ട സമീപനം നിങ്ങളുടെ ഘടനയിൽ ഒരു സുരക്ഷാ സിസ്റ്റം ഉൾപ്പെടുത്തലാണ്, അത് ഹാനികരമായ പെരുമാറ്റം കണ്ടെത്തുകയും തടയുകയും ചെയ്യുന്നു. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ദുരിതകരമായ ഉപയോക്തൃ-ജനിതമായ ಮತ್ತು AI-ജനിതമായ ഉള്ളടക്കം കണ്ടെത്താൻ കഴിവുള്ള സ്വതന്ത്ര സംരക്ഷണ പാളി നൽകുന്നു. Azure AI Content Safety എന്നത് ടെക്സ്റ്റ് மற்றும் ഇമേജ് APIകൾ ഉൾപ്പെടുത്തിയിട്ടുണ്ട്, ഹാനികരമായ ഉള്ളടക്കം കണ്ടെത്താൻ ഇത് സഹായിക്കും. Azure AI Foundry-ൽ Content Safety സർവീസ് വിവിധ മോഡാലിറ്റികളിലൂടെയും ഹാനികരമായ ഉള്ളടക്കം കണ്ടെത്തുന്നതിനുള്ള സാമ്പിൾ കോഡ് കാണാനും പരീക്ഷിക്കാനും സാദ്ധ്യമാക്കുന്നു. താഴെ കാണുന്ന [ക്വിക്സ്റ്റാർട്ട് ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) സർവീസിലേക്ക് അഭ്യർത്ഥനകൾ ചെയ്യുന്നത് നയിക്കുന്നു.

മറ്റൊരു പരിഗണന മൊത്തം ആപ്പ്ലിക്കേഷൻ പ്രകടനമാണ്. മൾട്ടി-മോഡൽ, മൾട്ടി-മോഡൽ ആപ്ലിക്കേഷനുകളിൽ, സിസ്റ്റം നിങ്ങൾക്കും നിങ്ങളുടെ ഉപയോക്താക്കൾക്കും പ്രതീക്ഷിക്കുന്നത那യിരിക്കുക എന്നതാണ് പ്രകടനം എന്നതുടർന്നുള്ള അർഥം, ഹാനികരമായ പുറംവഴികൾ ഉൽപാദിപ്പിക്കാതിരിക്കുക ഉൾപ്പെടെ. നിങ്ങളുടെ മൊത്തം ആപ്ലിക്കേഷന്റെ പ്രകടനം മൂല്യനിർണ്ണയിക്കാൻ [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ഉപയോഗിക്കുക. നിങ്ങൾക്ക് [ഇഷ്ടാനുസൃത ഇവാലുവേറ്ററുകൾ](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) സൃഷ്ടിക്കാനും മൂല്യനിർണ്ണയം നടത്താനും കഴിയും.

വികസന പരിസരത്തിൽ നിങ്ങളുടെ AI ആപ്ലിക്കേഷൻ വിലയിരുത്താൻ നിങ്ങൾക്ക് [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) ഉപയോഗിച്ച് സാധ്യമാണ്. ഒരു ടെസ്റ്റ് ഡാറ്റാസെറ്റ് അല്ലെങ്കിൽ ലക്ഷ്യം നൽകിയാൽ, നിങ്ങള്‍ സൃഷ്ടിക്കുന്ന ജനറേറ്റീവ് AI ഔട്ട്പുട്ടുകൾ സ്വതന്ത്രമായി നിർമ്മിച്ച ഇൻബിൽറ്റ് ഇവാലുവേറ്ററുകൾ അല്ലെങ്കിൽ നിങ്ങളുടെ തിരഞ്ഞെടുക്കുന്ന ഇഷ്ടാനുസൃത ഇവാലുവേറ്ററുകൾ ഉപയോഗിച്ച് അളക്കപ്പെടും. നിങ്ങളുടെ സിസ്റ്റം മൂല്യനിർണ്ണയിക്കാൻ azure ai evaluation sdk ഉപയോഗിച്ച് തുടങ്ങി എങ്ങനെ എന്നാണ് അറിയാൻ [ക്വിക്ഷ്‌ടാർട്ട് ഗൈഡ്](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) പിന്തുടരാം. ഒരു ഇവാലുവേഷൻ റൺ നടപ്പാക്കിയതിനു ശേഷം, [Azure AI Foundry-ൽ ഫലങ്ങൾ ദൃശ്യമാക്കാം](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## ട്രേഡ്‌മാർക്കുകൾ
ഈ പ്രോജക്ടിൽ പദ്ധതികൾ, ഉൽപ്പന്നങ്ങൾ, അല്ലെങ്കിൽ സേവനങ്ങൾക്കുള്ള ട്രേഡ്മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകൾ ഉൾപ്പെടാതെ ഇരിക്കണം. Microsoft ന്റെ ട്രേഡ്മാർക്കുകൾക്കും ലോഗോകൾക്കും അനുവദിതമായ ഉപയോഗം [Microsoft ന്റെ ട്രേഡ്മാർക്ക് & ബ്രാൻഡ് മാർഗനിർദ്ദേശങ്ങൾ](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) അനുസരിച്ചിരിക്കണം.
ഈ പ്രോജക്റ്റിന്റെ തിരുത്തിയ പതിപ്പുകളിൽ Microsoft ന്റെ ട്രേഡ്മാർക്കുകൾ അല്ലെങ്കിൽ ലോഗോകൾ ഉപയോഗിക്കുന്നത് ആശയക്കുഴപ്പം സൃഷ്ടിക്കരുത് അല്ലെങ്കിൽ Microsoft ന്റെ സ്പോൺസർഷിപ്പ് ഉണ്ടെന്ന് സൂചിപ്പിക്കരുത്. മൂന്നാം കക്ഷിയുടെ ട്രേഡ്മാർക്കുകളോ ലോഗോകളോ ഉപയോഗിക്കുന്നത് ആ മൂന്നാം കക്ഷിയുടെ നയങ്ങൾക്ക് വിധേയമാണ്.

## സഹായം

AI ആപ്പുകൾ നിർമ്മിക്കുന്നതിൽ നിങ്ങൾ കുടുങ്ങുകയാണെങ്കിൽ അല്ലെങ്കിൽ എന്തു പോലും ചോദിക്കാനുണ്ടെങ്കിൽ, ചേരുക:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

നിർമിക്കുന്നത് സംബന്ധിച്ചുണ്ടാകുന്ന ഉൽപ്പന്ന ഫീഡ്ബാക്ക് അല്ലെങ്കിൽ പിശകുകൾ ഉണ്ടെങ്കിൽ സന്ദർശിക്കുക:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്‌ക്ലെയ്മർ:
ഈ രേഖ AI തർജ്ജമാ സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിച്ചാലും, ഓട്ടോമേറ്റഡ് തർജ്മകളിൽ പിശകുകളും തെറ്റുകളും ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള മൂല പ്രമാണം അധികാരപരമായ സ്രോതസ്സായി കണക്കാക്കണം. നിർണ്ണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കും തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കും ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->