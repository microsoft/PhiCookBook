# Phi Kokaraamat: Käed-küljes näited Microsofti Phi mudelitega

[![Ava ja kasuta näiteid GitHub Codespaces'is](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Ava Dev Containers'is](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub'i panustajad](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub'i probleemid](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub'i tõmbepäringud](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR-id on oodatud](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub'i jälgijad](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub'i fork'id](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub'i tähed](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi on Microsofti arendatud avatud lähtekoodiga tehisintellekti mudelite seeria.

Phi on praegu kõige võimsam ja kulutõhusam väike keelemudel (SLM), millel on väga head võrdlusmõõdikud mitmekeelses kasutuses, mõtlemises, teksti/vestluse genereerimises, kodeerimises, piltides, helis ja muudes stsenaariumites.

Saate Phi juurutada pilve või servaseadmetesse ning saate hõlpsasti luua generatiivseid tehisintellekti rakendusi piiratud arvutusvõimsusega.

Alustamiseks järgige neid samme selle ressurssi kasutamiseks:
1. **Forki hoidla**: Klõpsake [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Clone'i hoidla**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Liitu Microsoft AI Discord kogukonnaga ja saa tuttavaks ekspertide ning kaastootjatega**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/et/cover.eb18d1b9605d754b.webp)

### 🌐 Mitmekeelne tugi

#### Toetatud GitHub Actioni kaudu (automaatne ja alati ajakohane)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Araabia](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaaria](../bg/README.md) | [Birma (Myanmar)](../my/README.md) | [Hiina (lihtsustatud)](../zh-CN/README.md) | [Hiina (traditsiooniline, Hongkong)](../zh-HK/README.md) | [Hiina (traditsiooniline, Macau)](../zh-MO/README.md) | [Hiina (traditsiooniline, Taiwan)](../zh-TW/README.md) | [Horvaatia](../hr/README.md) | [Tšehhi](../cs/README.md) | [Taani](../da/README.md) | [Hollandi](../nl/README.md) | [Eesti](./README.md) | [Soome](../fi/README.md) | [Prantsuse](../fr/README.md) | [Saksa](../de/README.md) | [Kreeka](../el/README.md) | [Heebrea](../he/README.md) | [Hindi](../hi/README.md) | [Ungari](../hu/README.md) | [Indoneesia](../id/README.md) | [Itaalia](../it/README.md) | [Jaapani](../ja/README.md) | [Kannada](../kn/README.md) | [Korea](../ko/README.md) | [Leedu](../lt/README.md) | [Malai](../ms/README.md) | [Malajalami](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigeeria pidžin](../pcm/README.md) | [Norra](../no/README.md) | [Pärsia (Farsi)](../fa/README.md) | [Poola](../pl/README.md) | [Portugali (Brasiilia)](../pt-BR/README.md) | [Portugali (Portugal)](../pt-PT/README.md) | [Pandžabi (Gurmukhi)](../pa/README.md) | [Rumeenia](../ro/README.md) | [Vene](../ru/README.md) | [Serbia (kirillitsa)](../sr/README.md) | [Slovaki](../sk/README.md) | [Sloveeni](../sl/README.md) | [Hispaania](../es/README.md) | [Suahiili](../sw/README.md) | [Rootsi](../sv/README.md) | [Tagalogi (filipino)](../tl/README.md) | [Tamili](../ta/README.md) | [Telugu](../te/README.md) | [Tai](../th/README.md) | [Türgi](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnami](../vi/README.md)

> **Eelistad kohalikku kloonimist?**

> See hoidla sisaldab üle 50 keele tõlkeid, mis oluliselt suurendab allalaaditava faili suurust. Tõlgeteta kloonimiseks kasuta sparse checkout’i:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> See annab sulle kõik vajaliku kursuse läbimiseks palju kiirema allalaadimisega.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Sisukord

- Sissejuhatus
  - [Tere tulemast Phi perekonda](./md/01.Introduction/01/01.PhiFamily.md)
  - [Keskkonna seadistamine](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Oluliste tehnoloogiate mõistmine](./md/01.Introduction/01/01.Understandingtech.md)
  - [Tehisintellekti turvalisus Phi mudelite jaoks](./md/01.Introduction/01/01.AISafety.md)
  - [Phi riistvara tugi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi mudelid ja kättesaadavus platvormide lõikes](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai ja Phi kasutamine](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace mudelid](https://github.com/marketplace/models)
  - [Azure AI mudelite kataloog](https://ai.azure.com)

- Phi klassifitseerimine erinevates keskkondades
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub mudelid](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry mudelite kataloog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI tööriistakomplekt VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry lokaalne](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi pere kasutamine
    - [Phi kasutamine iOS-is](./md/01.Introduction/03/iOS_Inference.md)
    - [Phi kasutamine Androidis](./md/01.Introduction/03/Android_Inference.md)
    - [Phi kasutamine Jetsonil](./md/01.Introduction/03/Jetson_Inference.md)
    - [Phi kasutamine AI PC-s](./md/01.Introduction/03/AIPC_Inference.md)
    - [Phi kasutamine Apple MLX raamistikuga](./md/01.Introduction/03/MLX_Inference.md)
    - [Phi kasutamine lokaalses serveris](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Phi kasutamine kaugserveris AI tööriistakomplekti abil](./md/01.Introduction/03/Remote_Interence.md)
    - [Phi kasutamine Rustiga](./md/01.Introduction/03/Rust_Inference.md)
    - [Phi nägemise kasutamine kohapeal](./md/01.Introduction/03/Vision_Inference.md)
    - [Phi kasutamine Kaito AKS, Azure Containers (ametlik tugi)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi pere kvantifitseerimine](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantifitseerimine kasutades llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantifitseerimine kasutades generatiivse AI laiendusi onnxruntime jaoks](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantifitseerimine kasutades Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantifitseerimine kasutades Apple MLX raamistikku](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi hindamine
    - [Vastutustundlik AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry hindamiseks](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow kasutamine hindamiseks](./md/01.Introduction/05/Promptflow.md)
 
- RAG Azure AI Otsinguga
    - [Kuidas kasutada Phi-4-mini ja Phi-4-multimodal (RAG) Azure AI Otsinguga](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi rakenduste arenduse näited
  - Teksti- ja vestlusrakendused
    - Phi-4 näited 🆕
      - [📓] [Vestlus Phi-4-mini ONNX mudeliga](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Vestlus Phi-4 lokaalse ONNX mudeliga .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Vestlus .NET konsoolirakenduses Phi-4 ONNX-ga, kasutades Sementic Kernelit](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 näited
      - [Lokaalne vestlusbot brauseris, kasutades Phi3, ONNX Runtime Web ja WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino vestlus](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Mitme mudeliga – Interaktiivne Phi-3-mini ja OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow – Kesta loomine ja Phi-3 kasutamine MLFlowga](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Mudeliparandus – Kuidas optimeerida Phi-3-minimudelit ONNX Runtime Webi jaoks Olive'iga](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 rakendus Phi-3 mini-4k-instruct-onnx-ga](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 mitme mudeliga tehisintellekti toetatud märkmete rakenduse näidis](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Kohandatud Phi-3 mudelite peenhäälestamine ja integreerimine Prompt flow'ga](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Kohandatud Phi-3 mudelite peenhäälestamine ja integreerimine Prompt flow'ga Azure AI Foundrys](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Peenhäälestatud Phi-3 / Phi-3.5 mudeli hindamine Azure AI Foundrys, pöörates tähelepanu Microsofti vastutustundliku AI põhimõtetele](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct keeleprognoosi näidis (hiina/inglise)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG vestlusrobot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windowsi GPU kasutamine Prompt flow lahenduse loomiseks Phi-3.5-Instruct ONNX-ga](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite kasutamine Androidi rakenduse loomiseks](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Küsimuste ja vastuste .NET näidis, kasutades kohalikku ONNX Phi-3 mudelit ja Microsoft.ML.OnnxRuntime'i](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Käsurea vestlus .NET rakendus Semantic Kerneliga ja Phi-3-ga](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK koodinäidised 
    - Phi-4 näidised 🆕
      - [📓] [Projekti koodi genereerimine kasutades Phi-4-multimodalit](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 näidised
      - [Loo oma Visual Studio Code GitHub Copilot vestlus Microsoft Phi-3 perekonnaga](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Loo oma Visual Studio Code vestlus Copilot agent Phi-3.5-ga GitHubi mudelite abil](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Täiustatud järeldamise näidised
    - Phi-4 näidised 🆕
      - [📓] [Phi-4-mini-järeldamine või Phi-4-järeldamise näidised](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Phi-4-mini-järeldamise peenhäälestamine Microsoft Olive'iga](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-järeldamise peenhäälestamine Apple MLX-iga](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-järeldamine GitHubi mudelitega](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-järeldamine Azure AI Foundry mudelitega](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demo'd
      - [Phi-4-mini demo'd Hugging Face Spaces'is](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demo'd Hugging Face Spaces'is](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Visiooni näidised
    - Phi-4 näidised 🆕
      - [📓] [Phi-4-multimodalit kasutades piltide lugemine ja koodi genereerimine](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 näidised
      -  [📓][Phi-3-vision-pildi tekst tekstiks](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP sisendvektorid](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 taaskasutus](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision – Visuaalne keeleassistent – Phi3-Vision ja OpenVINOGA](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision mitme kaadri või mitme pildi näidis](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision kohalik ONNX mudel kasutades Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menüü-põhine Phi-3 Vision kohalik ONNX mudel kasutades Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Matemaatika näidised
    -  Phi-4-Mini-Flash-Järeldamise-Juhendatud näidised 🆕 [Matemaatika demo Phi-4-Mini-Flash-Järeldamise-Juhendatud mudeliga](./md/02.Application/09.Math/MathDemo.ipynb)

  - Helinäidised
    - Phi-4 näidised 🆕
      - [📓] [Helitekstide väljavõtmine Phi-4-multimodaliga](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal heli näidis](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal kõnetõlke näidis](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET käsurea rakendus, mis kasutab Phi-4-multimodali heli analüüsimiseks ja transkriptsiooni genereerimiseks](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE näidised
    - Phi-3 / 3.5 näidised
      - [📓] [Phi-3.5 Ekspertide segude (MoEs) sotsiaalmeedia näidis](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Tagasitoomisega täiustatud generatsiooni (RAG) torujuhtme ehitamine NVIDIA NIM Phi-3 MOE, Azure AI Search ja LlamaIndexiga](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Funktsiooni kutsumise näidised
    - Phi-4 näidised 🆕
      -  [📓] [Funktsiooni kutsumise kasutamine Phi-4-miniga](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Funktsiooni kutsumise kasutamine mitme agendi loomiseks Phi-4-miniga](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Funktsiooni kutsumise kasutamine Ollama puhul](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Funktsiooni kutsumise kasutamine ONNX-iga](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Mitmemodaalsed segamisnäidised
    - Phi-4 näidised 🆕
      -  [📓] [Phi-4-multimodali kasutamine tehnoloogiaajakirjanikuna](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET käsurea rakendus, kasutades Phi-4-multimodali piltide analüüsimiseks](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi mudelite peenhäälestamine
  - [Peenhäälestamise stsenaariumid](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Peenhäälestamine vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Las Phi-3 saab tööstuseksperdiks – peenhäälestamine](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Phi-3 peenhäälestamine AI tööriistakomplektiga VS Code'i jaoks](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Phi-3 peenhäälestamine Azure Machine Learning Service'iga](./md/03.FineTuning/Introduce_AzureML.md)
  - [Phi-3 peenhäälestamine Lora abil](./md/03.FineTuning/FineTuning_Lora.md)
  - [Phi-3 peenhäälestamine QLora abil](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Phi-3 peenhäälestamine Azure AI Foundryga](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Phi-3 peenhäälestamine Azure ML CLI/SDK abil](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Peenhäälestamine Microsoft Olive'iga](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive praktiline labor – peenhäälestamine](./md/03.FineTuning/olive-lab/readme.md)
  - [Phi-3-vision peenhäälestamine Weights and Biasiga](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Phi-3 peenhäälestamine Apple MLX raamistikuga](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision peenhäälestamine (ametlik tugi)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Phi-3 peenhäälestamine Kaito AKS ja Azure konteineritega (ametlik tugi)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 ja 3.5 Vision peenhäälestamine](https://github.com/2U1/Phi3-Vision-Finetune)

- Praktiline labor
  - [Uuenduslike mudelite uurimine: LLM-id, SLM-id, kohalik arendus ja muud](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Loodusliku keele töötlemise potentsiaali avamine: peenhäälestamine Microsoft Olive'iga](https://github.com/azure/Ignite_FineTuning_workshop)

- Akadeemilised teadustööd ja väljaanded
  - [Õpikud on kõik, mida vajate II: phi-1.5 tehniline aruanne](https://arxiv.org/abs/2309.05463)
  - [Phi-3 tehniline aruanne: Võimas keelemudel kohapeal teie telefonis](https://arxiv.org/abs/2404.14219)
  - [Phi-4 tehniline aruanne](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini tehniline aruanne: Kompaktne, kuid võimas multimodaalne keelemudel LoRAde seguga](https://arxiv.org/abs/2503.01743)
  - [Väikeste keelemudelite optimeerimine sõidukisiseste funktsioonikõnede jaoks](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 peenhäälestamine mitmevalikvastustega küsimustele vastamiseks: metoodika, tulemused ja väljakutsed](https://arxiv.org/abs/2501.01588)
  - [Phi-4-põhise järeldamise tehniline aruanne](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-põhine järeldamise tehniline aruanne](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi mudelite kasutamine

### Phi Azure AI Foundry’s

Saate õppida, kuidas kasutada Microsoft Phi-d ja kuidas ehitada E2E lahendusi erinevates riistvaraseadmetes. Phi kogemiseks alustage mudelitega mängimist ja kohandage Phi oma stsenaariumite jaoks, kasutades [Azure AI Foundry Azure AI mudelite kataloogi](https://aka.ms/phi3-azure-ai). Rohkem infot leiate juhisena Azure AI Foundryga alustamiseks [Azure AI Foundry juhendist](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Mänguruum**
Igal mudelil on oma testimiskoht [Azure AI Playground](https://aka.ms/try-phi3).

### Phi GitHubi mudelites

Saate õppida, kuidas kasutada Microsoft Phi-d ja kuidas ehitada E2E lahendusi erinevates riistvaraseadmetes. Phi kogemiseks alustage mudeliga mängimist ja kohandage Phi oma stsenaariumite jaoks, kasutades [GitHub Model Catalogu](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Rohkem infot leiate juhisena GitHub Model Cataloguga alustamisest [GitHub Model Catalog juhendist](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Mänguruum**
Igal mudelil on oma [testimismänguruum](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi Hugging Face’il

Mudeli leiate ka [Hugging Face’ilt](https://huggingface.co/microsoft)

**Mänguruum**
[Hugging Chat mänguruum](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 Muud kursused

Meie meeskond toodab ka teisi kursuseid! Vaadake:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j algajatele](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js algajatele](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain algajatele](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agentid
[![AZD algajatele](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI algajatele](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP algajatele](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI agentid algajatele](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Generatiivse AI sari
[![Generatiivne AI algajatele](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatiivne AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatiivne AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatiivne AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### Põhioskused
[![Masinõpe algajatele](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Andmeteadus algajatele](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![Tehisintellekt algajatele](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Küberjulgeolek algajatele](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Veebiarendus algajatele](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT algajatele](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR arendus algajatele](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Copiloti sari
[![Copilot AI paarisprogrammeerimiseks](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET jaoks](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copiloti seiklus](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Vastutustundlik AI

Microsoft on pühendunud aitamaks oma kliente kasutada meie AI tooteid vastutustundlikult, jagades oma kogemusi ja luues usaldusel põhinevaid partnerlusi selliste tööriistade kaudu nagu Läbipaistvuse märkmed ja Mõjuhinnangud. Paljusid neist ressurssidest leiate aadressilt [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofti lähenemine vastutustundlikule AI-le põhineb meie AI põhimõtetel, mis on õiglus, usaldusväärsus ja turvalisus, privaatsus ja turvalisus, kaasatus, läbipaistvus ja vastutus.

Suurte loomuliku keele, pildi ja kõnemudelitega - nagu selles näites kasutatavad - võivad potentsiaalselt käituda ebaõiglaselt, usaldamatult või solvavalt, mis võib põhjustada kahju. Riskidest ja piirangutest teavitamiseks palun tutvuge [Azure OpenAI teenuse Läbipaistvuse märkmega](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text).

Soovitatav lähenemine nende riskide maandamiseks on lisada oma arhitektuuri turvasüsteem, mis suudab tuvastada ja vältida kahjulikku käitumist. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) pakub sõltumatut kaitset, mis võimaldab rakendustes ja teenustes tuvastada kahjulikku kasutajate ja AI loodud sisu. Azure AI Content Safety sisaldab teksti ja pildi API-sid, mis võimaldavad tuvastada kahjulikke materjale. Azure AI Foundry sees võimaldab Content Safety teenus vaadata, uurida ja proovida näitekoodi kahjuliku sisu tuvastamiseks eri modaliteetides. Järgmine [kiiramist dokumentatsioon](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) juhendab teid teenuse päringute tegemisel.
Teine aspekt, mida tuleb arvestada, on üldine rakenduse jõudlus. Mitme modaalsete ja mitme mudeliga rakenduste puhul mõistame jõudluse all süsteemi toimimist vastavalt teie ja teie kasutajate ootustele, sealhulgas kahjulike väljundite mitte genereerimist. Oluline on hinnata teie üldise rakenduse jõudlust, kasutades [jõudluse, kvaliteedi, riski ja turvalisuse hindajaid](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Teil on ka võimalus luua ja hinnata [kohandatud hindajatega](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Saate oma AI-rakendust oma arenduskeskkonnas hinnata, kasutades [Azure AI Evaluation SDK-d](https://microsoft.github.io/promptflow/index.html). Kasutades kas testandmeruumi või sihti, mõõdetakse teie generatiivse AI rakenduse tulemusi kvantitatiivselt kas sisseehitatud hindajate või teie valitud kohandatud hindajate abil. Süsteemi hindamiseks Azure AI Evaluation SDK-ga saate alustada, järgides [kiirstart juhendit](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kui olete hindamisprotsessi käivitanud, saate [visualiseerida tulemusi Azure AI Foundrys](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Kaubamärgid

See projekt võib sisaldada projekti, toote või teenuse kaubamärke või logosid. Microsofti kaubamärkide või logode volitatud kasutamine on allutatud ja vastab [Microsofti kaubamärgi ja brändi juhistele](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general). Muudetud versioonide kasutamisel ei tohi Microsofti kaubamärkide või logode kasutamine tekitada segadust ega viidata Microsofti sponsorlusele. Kolmandate osapoolte kaubamärkide või logode kasutamine allub vastava kolmanda osapoole poliitikale.

## Abi saamine

Kui teil tekib takistusi või küsimusi AI-rakenduste ehitamisel, liituge:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Kui teil on toodete tagasisidet või ehitamisel esineb vigu, külastage:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vabandus**:
See dokument on tõlgitud tehisintellektil põhineva tõlke teenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame täpsust, võivad automaatsed tõlked sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Kriitilise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste ega valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->