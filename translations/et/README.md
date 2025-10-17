<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4987daf30687ad3850757c9eae3f5411",
  "translation_date": "2025-10-17T10:44:25+00:00",
  "source_file": "README.md",
  "language_code": "et"
}
-->
# Phi Kokkuraamat: Praktilised näited Microsofti Phi mudelitega

[![Avage ja kasutage näidiseid GitHub Codespaces'is](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Avage Dev Containers'is](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHubi kaastöölised](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubi probleemid](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubi tõmbepäringud](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR-d on teretulnud](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHubi jälgijad](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubi harud](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubi tähed](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi on Microsofti poolt välja töötatud avatud lähtekoodiga tehisintellekti mudelite seeria.

Phi on praegu kõige võimsam ja kulutõhusam väike keelemudel (SLM), mis saavutab suurepäraseid tulemusi mitmes keeles, loogilises mõtlemises, teksti/vestluse genereerimises, kodeerimises, piltides, audios ja muudes valdkondades.

Phi saab juurutada pilves või servaseadmetes ning generatiivsete tehisintellekti rakenduste loomine on võimalik ka piiratud arvutusvõimsusega.

Järgi neid samme, et alustada nende ressursside kasutamist:
1. **Haru tegemine**: Klõpsa [![GitHubi harud](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Kloonige hoidla**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Liitu Microsoft AI Discordi kogukonnaga ja kohtuge ekspertide ning teiste arendajatega**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![kaas](../../imgs/cover.png)

### 🌐 Mitmekeelne tugi

#### Toetatud GitHub Actioni kaudu (automaatne ja alati ajakohane)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Araabia](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaaria](../bg/README.md) | [Birma (Myanmar)](../my/README.md) | [Hiina (lihtsustatud)](../zh/README.md) | [Hiina (traditsiooniline, Hongkong)](../hk/README.md) | [Hiina (traditsiooniline, Macau)](../mo/README.md) | [Hiina (traditsiooniline, Taiwan)](../tw/README.md) | [Horvaatia](../hr/README.md) | [Tšehhi](../cs/README.md) | [Taani](../da/README.md) | [Hollandi](../nl/README.md) | [Eesti](./README.md) | [Soome](../fi/README.md) | [Prantsuse](../fr/README.md) | [Saksa](../de/README.md) | [Kreeka](../el/README.md) | [Heebrea](../he/README.md) | [Hindi](../hi/README.md) | [Ungari](../hu/README.md) | [Indoneesia](../id/README.md) | [Itaalia](../it/README.md) | [Jaapani](../ja/README.md) | [Korea](../ko/README.md) | [Leedu](../lt/README.md) | [Malai](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norra](../no/README.md) | [Pärsia (Farsi)](../fa/README.md) | [Poola](../pl/README.md) | [Portugali (Brasiilia)](../br/README.md) | [Portugali (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumeenia](../ro/README.md) | [Vene](../ru/README.md) | [Serbia (kirillitsa)](../sr/README.md) | [Slovaki](../sk/README.md) | [Sloveeni](../sl/README.md) | [Hispaania](../es/README.md) | [Suahiili](../sw/README.md) | [Rootsi](../sv/README.md) | [Tagalogi (Filipiinid)](../tl/README.md) | [Tamili](../ta/README.md) | [Tai](../th/README.md) | [Türgi](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnami](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Sisukord

- Sissejuhatus
  - [Tere tulemast Phi perekonda](./md/01.Introduction/01/01.PhiFamily.md)
  - [Keskkonna seadistamine](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Põhitehnoloogiate mõistmine](./md/01.Introduction/01/01.Understandingtech.md)
  - [AI turvalisus Phi mudelite jaoks](./md/01.Introduction/01/01.AISafety.md)
  - [Phi riistvara tugi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi mudelid ja saadavus platvormidel](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai ja Phi kasutamine](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace mudelid](https://github.com/marketplace/models)
  - [Azure AI mudelikataloog](https://ai.azure.com)

- Phi järeldamine erinevates keskkondades
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHubi mudelid](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry mudelikataloog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi perekonna järeldamine
    - [Phi järeldamine iOS-is](./md/01.Introduction/03/iOS_Inference.md)
    - [Phi järeldamine Androidis](./md/01.Introduction/03/Android_Inference.md)
    - [Phi järeldamine Jetsonis](./md/01.Introduction/03/Jetson_Inference.md)
    - [Phi järeldamine AI PC-s](./md/01.Introduction/03/AIPC_Inference.md)
    - [Phi järeldamine Apple MLX Frameworkiga](./md/01.Introduction/03/MLX_Inference.md)
    - [Phi järeldamine kohalikus serveris](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Phi järeldamine kaugserveris AI Toolkitiga](./md/01.Introduction/03/Remote_Interence.md)
    - [Phi järeldamine Rustiga](./md/01.Introduction/03/Rust_Inference.md)
    - [Phi--Vision järeldamine kohalikus keskkonnas](./md/01.Introduction/03/Vision_Inference.md)
    - [Phi järeldamine Kaito AKS, Azure Containers (ametlik tugi)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi perekonna kvantifitseerimine](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantifitseerimine llama.cpp abil](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantifitseerimine Generative AI laiendustega onnxruntime jaoks](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantifitseerimine Intel OpenVINO abil](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantifitseerimine Apple MLX Frameworkiga](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi hindamine
    - [Vastutustundlik AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry hindamiseks](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow kasutamine hindamiseks](./md/01.Introduction/05/Promptflow.md)
 
- RAG Azure AI otsinguga
    - [Kuidas kasutada Phi-4-mini ja Phi-4-multimodal (RAG) Azure AI otsinguga](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi rakenduste arendamise näidised
  - Teksti- ja vestlusrakendused
    - Phi-4 näidised 🆕
      - [📓] [Vestlus Phi-4-mini ONNX mudeliga](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Vestlus Phi-4 kohaliku ONNX mudeliga .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Vestlus .NET konsoolirakendus Phi-4 ONNX-iga, kasutades Semantilist Kernelit](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 näidised
      - [Kohalik vestlusrobot brauseris, kasutades Phi3, ONNX Runtime Webi ja WebGPU-d](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino vestlus](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Mitme mudeli interaktiivne Phi-3-mini ja OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Kuidas luua wrapper ja kasutada Phi-3 MLFlow'ga](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Mudelite optimeerimine - Kuidas optimeerida Phi-3-min mudelit ONNX Runtime Webi jaoks Olive'iga](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [WinUI3 rakendus Phi-3 mini-4k-instruct-onnx-iga](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [WinUI3 mitme mudeliga AI-põhine märkmete rakenduse näidis](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Kohandatud Phi-3 mudelite peenhäälestamine ja integreerimine Prompt flow'ga](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Kohandatud Phi-3 mudelite peenhäälestamine ja integreerimine Prompt flow'ga Azure AI Foundry's](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Peenhäälestatud Phi-3 / Phi-3.5 mudeli hindamine Azure AI Foundry's, keskendudes Microsofti vastutustundliku AI põhimõtetele](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct keele ennustamise näidis (hiina/inglise)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG vestlusrobot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU kasutamine Prompt flow lahenduse loomiseks Phi-3.5-Instruct ONNX-iga](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tflite kasutamine Androidi rakenduse loomiseks](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Küsimuste ja vastuste .NET näidis, kasutades kohalikku ONNX Phi-3 mudelit Microsoft.ML.OnnxRuntime abil](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Konsoli vestluse .NET rakendus Semantilise Kerneliga ja Phi-3-ga](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK koodipõhised näidised
  - Phi-4 näidised 🆕
    - [📓] [Projekti koodi genereerimine Phi-4-multimodal abil](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5 näidised
    - [Ehita oma Visual Studio Code GitHub Copilot vestlus Microsoft Phi-3 perekonnaga](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [Loo oma Visual Studio Code vestlus Copilot agent Phi-3.5 abil GitHub mudelitega](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- Täiustatud põhjendamise näidised
  - Phi-4 näidised 🆕
    - [📓] [Phi-4-mini-reasoning või Phi-4-reasoning näidised](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Phi-4-mini-reasoning peenhäälestamine Microsoft Olive abil](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning peenhäälestamine Apple MLX abil](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning GitHub mudelitega](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Phi-4-mini-reasoning Azure AI Foundry mudelitega](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- Demod
    - [Phi-4-mini demod, mis on majutatud Hugging Face Spaces'is](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Phi-4-multimodal demod, mis on majutatud Hugging Face Spaces'is](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- Visiooni näidised
  - Phi-4 näidised 🆕
    - [📓] [Phi-4-multimodal kasutamine piltide lugemiseks ja koodi genereerimiseks](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Phi-3 / 3.5 näidised
    - [📓][Phi-3-vision-pildi tekst tekstiks](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [DEMO: Phi-3 taaskasutus](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Visuaalne keeleassistent - Phi3-Visioni ja OpenVINO abil](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision mitme kaadri või mitme pildi näidis](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Phi-3 Vision kohalik ONNX mudel, kasutades Microsoft.ML.OnnxRuntime .NET-i](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Menüü põhine Phi-3 Vision kohalik ONNX mudel, kasutades Microsoft.ML.OnnxRuntime .NET-i](../../md/04.HOL/dotnet/src/LabsPhi304)

- Matemaatika näidised
  - Phi-4-Mini-Flash-Reasoning-Instruct näidised 🆕 [Matemaatika demo Phi-4-Mini-Flash-Reasoning-Instruct abil](../../md/02.Application/09.Math/MathDemo.ipynb)

- Audio näidised
  - Phi-4 näidised 🆕
    - [📓] [Helitranskriptsioonide väljavõtmine Phi-4-multimodal abil](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodal audio näidis](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal kõnetõlke näidis](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET konsoolirakendus, mis kasutab Phi-4-multimodal audio analüüsimiseks ja transkriptsiooni genereerimiseks](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOE näidised
  - Phi-3 / 3.5 näidised
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) sotsiaalmeedia näidis](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [Retrieval-Augmented Generation (RAG) torujuhtme loomine NVIDIA NIM Phi-3 MOE, Azure AI Searchi ja LlamaIndexi abil](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- Funktsioonikutsumise näidised
  - Phi-4 näidised 🆕
    - [📓] [Funktsioonikutsumise kasutamine Phi-4-mini abil](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Funktsioonikutsumise kasutamine mitme agendi loomiseks Phi-4-mini abil](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Funktsioonikutsumise kasutamine Ollama abil](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [Funktsioonikutsumise kasutamine ONNX-iga](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- Multimodaalsed segamisnäidised
  - Phi-4 näidised 🆕
    - [📓] [Phi-4-multimodal kasutamine tehnoloogiaajakirjanikuna](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET konsoolirakendus, mis kasutab Phi-4-multimodal piltide analüüsimiseks](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi näidiste peenhäälestamine
  - [Peenhäälestamise stsenaariumid](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Peenhäälestamine vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Peenhäälestamine: las Phi-3 muutub tööstuseksperdiks](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Phi-3 peenhäälestamine AI Toolkitiga VS Code jaoks](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Phi-3 peenhäälestamine Azure Machine Learning Service abil](./md/03.FineTuning/Introduce_AzureML.md)
  - [Phi-3 peenhäälestamine Lora abil](./md/03.FineTuning/FineTuning_Lora.md)
  - [Phi-3 peenhäälestamine QLora abil](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Phi-3 peenhäälestamine Azure AI Foundry abil](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Phi-3 peenhäälestamine Azure ML CLI/SDK abil](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Peenhäälestamine Microsoft Olive abil](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Peenhäälestamine Microsoft Olive Hands-On Lab abil](./md/03.FineTuning/olive-lab/readme.md)
  - [Phi-3-vision peenhäälestamine Weights and Bias abil](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Phi-3 peenhäälestamine Apple MLX Framework abil](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision peenhäälestamine (ametlik tugi)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Phi-3 ja 3.5 Visioni peenhäälestamine Kaito AKS-i ja Azure Containersi abil (ametlik tugi)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 ja 3.5 Visioni peenhäälestamine](https://github.com/2U1/Phi3-Vision-Finetune)

- Praktiline labor
  - [Tipptasemel mudelite uurimine: LLM-id, SLM-id, kohalik arendus ja palju muud](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP potentsiaali avamine: peenhäälestamine Microsoft Olive abil](https://github.com/azure/Ignite_FineTuning_workshop)

- Akadeemilised uurimistööd ja publikatsioonid
  - [Textbooks Are All You Need II: phi-1.5 tehniline aruanne](https://arxiv.org/abs/2309.05463)
  - [Phi-3 tehniline aruanne: väga võimekas keelemudel teie telefonis](https://arxiv.org/abs/2404.14219)
  - [Phi-4 tehniline aruanne](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini tehniline aruanne: kompaktne, kuid võimas multimodaalne keelemudel LoRAs'i segamise kaudu](https://arxiv.org/abs/2503.01743)
  - [Väikeste keelemudelite optimeerimine sõidukisiseste funktsioonide jaoks](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 peenhäälestamine valikvastustega küsimustele vastamiseks: metoodika, tulemused ja väljakutsed](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning tehniline aruanne](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning tehniline aruanne](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi mudelite kasutamine

### Phi Azure AI Foundry's

Saate õppida, kuidas kasutada Microsoft Phi-d ja luua E2E lahendusi erinevates riistvaraseadmetes. Et ise Phi-d kogeda, alustage mudelitega katsetamisest ja Phi kohandamisest oma stsenaariumide jaoks, kasutades [Azure AI Foundry Azure AI mudelikataloogi](https://aka.ms/phi3-azure-ai). Lisateavet leiate [Azure AI Foundry alustamise juhendist](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Mänguväljak**  
Igal mudelil on oma mänguväljak mudeli testimiseks [Azure AI Playground](https://aka.ms/try-phi3).

### Phi GitHubi mudelites

Saate õppida, kuidas kasutada Microsoft Phi-d ja luua E2E lahendusi erinevates riistvaraseadmetes. Et ise Phi-d kogeda, alustage mudeli katsetamisest ja Phi kohandamisest oma stsenaariumide jaoks, kasutades [GitHubi mudelikataloogi](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Lisateavet leiate [GitHubi mudelikataloogi alustamise juhendist](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Mänguväljak**  
Igal mudelil on oma [mänguväljak mudeli testimiseks](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi Hugging Face'is

Mudel on saadaval ka [Hugging Face'is](https://huggingface.co/microsoft).

**Mänguväljak**  
[Hugging Chat mänguväljak](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Vastutustundlik AI

Microsoft on pühendunud aitama oma klientidel kasutada meie AI tooteid vastutustundlikult, jagades oma kogemusi ja luues usaldusel põhinevaid partnerlusi selliste tööriistade kaudu nagu läbipaistvuse märkmed ja mõju hinnangud. Paljud neist ressurssidest on saadaval aadressil [https://aka.ms/RAI](https://aka.ms/RAI).  
Microsofti lähenemine vastutustundlikule AI-le põhineb meie AI põhimõtetel: õiglus, usaldusväärsus ja ohutus, privaatsus ja turvalisus, kaasatus, läbipaistvus ja vastutus.

Suuremahulised loomuliku keele, pildi ja kõne mudelid - nagu need, mida selles näites kasutatakse - võivad potentsiaalselt käituda ebaõiglaselt, ebausaldusväärselt või solvavalt, põhjustades kahju. Palun tutvuge [Azure OpenAI teenuse läbipaistvuse märkmega](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), et olla teadlik riskidest ja piirangutest.

Soovitatav lähenemine nende riskide leevendamiseks on lisada oma arhitektuuri turvasüsteem, mis suudab tuvastada ja ennetada kahjulikku käitumist. [Azure AI sisuturvalisus](https://learn.microsoft.com/azure/ai-services/content-safety/overview) pakub sõltumatut kaitsekihti, mis suudab tuvastada kahjulikku kasutaja loodud ja AI loodud sisu rakendustes ja teenustes. Azure AI sisuturvalisus sisaldab teksti- ja pildirakenduste liideseid, mis võimaldavad tuvastada kahjulikku materjali. Azure AI Foundry's võimaldab sisuturvalisuse teenus vaadata, uurida ja proovida näidiskoodi kahjuliku sisu tuvastamiseks erinevates vormides. Järgmine [kiire alustamise dokumentatsioon](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) juhendab teid teenusele päringute tegemisel.

Teine aspekt, mida arvesse võtta, on kogu rakenduse jõudlus. Multimodaalsete ja mitmemudeliliste rakenduste puhul tähendab jõudlus seda, et süsteem toimib nii, nagu teie ja teie kasutajad ootavad, sealhulgas ei genereeri kahjulikke väljundeid. Oluline on hinnata kogu rakenduse jõudlust, kasutades [jõudluse ja kvaliteedi ning riski ja ohutuse hindajaid](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Teil on ka võimalus luua ja hinnata [kohandatud hindajatega](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Teie AI rakendust saab arenduskeskkonnas hinnata, kasutades [Azure AI hindamise SDK-d](https://microsoft.github.io/promptflow/index.html). Kasutades kas testandmestikku või sihtmärki, mõõdetakse teie generatiivse AI rakenduse väljundeid kvantitatiivselt sisseehitatud hindajate või teie valitud kohandatud hindajatega. Azure AI hindamise SDK-ga alustamiseks ja süsteemi hindamiseks saate järgida [kiire alustamise juhendit](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kui olete hindamisjooksu teostanud, saate [visualiseerida tulemusi Azure AI Foundry's](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Kaubamärgid

See projekt võib sisaldada kaubamärke või logosid projektide, toodete või teenuste jaoks. Microsofti kaubamärkide või logode volitatud kasutamine peab järgima [Microsofti kaubamärkide ja brändi juhiseid](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Microsofti kaubamärkide või logode kasutamine projekti muudetud versioonides ei tohi tekitada segadust ega viidata Microsofti sponsorlusele. Kolmandate osapoolte kaubamärkide või logode kasutamine peab järgima nende kolmandate osapoolte poliitikat.

## Abi saamine

Kui jääte hätta või teil on küsimusi AI rakenduste loomise kohta, liituge:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Kui teil on tootetagasisidet või vigu rakenduse loomisel, külastage:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.