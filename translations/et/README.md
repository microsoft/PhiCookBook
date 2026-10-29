# Phi kokaraamat: Praktilised näited Microsofti Phi mudelitega

[![Ava ja kasuta näiteid GitHub Codespaces'is](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Ava Dev Containers'is](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub kaastöötajad](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub probleemid](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub tõmbepäringud](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR-d on oodatud](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub jälgijad](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forkid](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub tähed](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi on Microsofti arendatud avatud lähtekoodiga tehisintellekti mudelite seeria.

Phi on praegu kõige võimsam ja kulutõhusam väike keelemudel (SLM), millel on väga head tulemused mitmekeelses, arutlevas, teksti/vestluse genereerimises, kodeerimises, piltides, helis ja teistes stsenaariumites.

Saate deploy'da Phi kas pilve või ääreseadmetele ning luua hõlpsasti generatiivseid tehisintellekti rakendusi piiratud arvutusvõimsusega.

Alustamiseks toimige järgmiselt:
1. **Forki hoidla**: Klõpsake [![GitHub forkid](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Kloneeri hoidla**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Liitu Microsoft AI Discord kogukonnaga ja kohtuge ekspertide ning teiste arendajatega**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/et/cover.eb18d1b9605d754b.webp)

### 🌐 Mitmekeelne tugi

#### Toetatud läbi GitHub Actioni (automatiseeritud ja alati ajakohane)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Araabia](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaaria](../bg/README.md) | [Birma (Myanmar)](../my/README.md) | [Hiina (lihtsustatud)](../zh-CN/README.md) | [Hiina (traditsiooniline, Hongkong)](../zh-HK/README.md) | [Hiina (traditsiooniline, Macau)](../zh-MO/README.md) | [Hiina (traditsiooniline, Taiwan)](../zh-TW/README.md) | [Horvaadi](../hr/README.md) | [Tšehhi](../cs/README.md) | [Taani](../da/README.md) | [Hollandi](../nl/README.md) | [Eesti](./README.md) | [Soome](../fi/README.md) | [Prantsuse](../fr/README.md) | [Saksa](../de/README.md) | [Kreeka](../el/README.md) | [Heebrea](../he/README.md) | [Hindi](../hi/README.md) | [Ungari](../hu/README.md) | [Indoneesia](../id/README.md) | [Itaalia](../it/README.md) | [Jaapani](../ja/README.md) | [Kannada](../kn/README.md) | [Khmeri](../km/README.md) | [Korea](../ko/README.md) | [Leedu](../lt/README.md) | [Malai](../ms/README.md) | [Malajalami](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigeeria pidžin](../pcm/README.md) | [Norra](../no/README.md) | [Pärsia (Farsi)](../fa/README.md) | [Poola](../pl/README.md) | [Portugali (Brasiilia)](../pt-BR/README.md) | [Portugali (Portugal)](../pt-PT/README.md) | [Pundžabi (Gurmukhi)](../pa/README.md) | [Rumeenia](../ro/README.md) | [Vene](../ru/README.md) | [Serbia (kirillitsa)](../sr/README.md) | [Slovaki](../sk/README.md) | [Sloveeni](../sl/README.md) | [Hispaania](../es/README.md) | [Suaheli](../sw/README.md) | [Rootsi](../sv/README.md) | [Tagalogi (Filipino)](../tl/README.md) | [Tamili](../ta/README.md) | [Telugu](../te/README.md) | [Tai](../th/README.md) | [Türgi](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnam](../vi/README.md)

> **Eelistate kohalikku kloonimist?**
>
> See hoidla sisaldab enam kui 50 keele tõlget, mis suurendab oluliselt allalaadimismahtu. Tõlgeteta kloonimiseks kasutage sparse checkout-i:
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
> See annab teile kõik vajaliku kursuse lõpetamiseks palju kiirema allalaadimisega.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Sisukord

- Sissejuhatus
  - [Tere tulemast Phi perekonda](./md/01.Introduction/01/01.PhiFamily.md)
  - [Keskkonna seadistamine](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Oluliste tehnoloogiate mõistmine](./md/01.Introduction/01/01.Understandingtech.md)
  - [AI ohutus Phi mudelite jaoks](./md/01.Introduction/01/01.AISafety.md)
  - [Phi riistvaratugi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi mudelid ja kättesaadavus platvormide lõikes](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai ja Phi kasutamine](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace'i mudelid](https://github.com/marketplace/models)
  - [Azure AI mudelite kataloog](https://ai.azure.com)

- Phi järeldamine erinevates keskkondades
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub mudelid](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Microsoft Foundry mudelite kataloog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI tööriistakomplekt VSCode'is (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry lokaalne](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi perekonna järeldamine
    - [Phi järeldamine iOS-is](./md/01.Introduction/03/iOS_Inference.md)
    - [Phi järeldamine Androidis](./md/01.Introduction/03/Android_Inference.md)
    - [Phi järeldamine Jetsonis](./md/01.Introduction/03/Jetson_Inference.md)
    - [Phi järeldamine AI PC-s](./md/01.Introduction/03/AIPC_Inference.md)
    - [Phi järeldamine Apple MLX raamistikuga](./md/01.Introduction/03/MLX_Inference.md)
    - [Phi järeldamine lokaalses serveris](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Phi järeldamine kaugserveris AI tööriistaga](./md/01.Introduction/03/Remote_Interence.md)
    - [Phi järeldamine Rustiga](./md/01.Introduction/03/Rust_Inference.md)
    - [Phi visiooni järeldamine lokaalselt](./md/01.Introduction/03/Vision_Inference.md)
    - [Phi järeldamine Kaito AKS, Azure konteineritega (ametlik tugi)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi perekonna kvantifitseerimine](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantimine kasutades llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantimine kasutades Generative AI laiendusi onnxruntime'ile](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantimine kasutades Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantimine kasutades Apple MLX raamistikku](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi hindamine
    - [Vastutustundlik AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Microsoft Foundry hindamiseks](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow kasutamine hindamiseks](./md/01.Introduction/05/Promptflow.md)
 
- RAG kasutamine Azure AI otsingus
    - [Kuidas kasutada Phi-4-mini ja Phi-4-multimodal (RAG) Azure AI otsinguga](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)
    - [Null-pilve kohalik hübriid RAG SQLite FTS5 ja phi-4-mini-ga](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-mini_Local_Hybrid_RAG_SQLite_FTS5.ipynb)

- Phi rakenduste arendamise näited
  - Teksti- ja vestlusrakendused
    - Phi-4 näited
      - [📓] [Vestlus Phi-4-mini ONNX mudeliga](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Vestlus Phi-4 lokaalse ONNX mudeliga .NET'is](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Vestluse .NET konsoolirakendus Phi-4 ONNX mudeliga kasutades Semantic Kernelit](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)

    - Phi-3 / 3.5 Näidised
      - [Kohalik vestlusrobot brauseris, kasutades Phi3, ONNX Runtime Web ja WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Vestlus](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Mitmemudeliline - interaktiivne Phi-3-mini ja OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Katteloori loomine ja Phi-3 kasutamine MLFlow’ga](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Mudelid optimeerimine - Kuidas optimeerida Phi-3-minimudelit ONNX Runtime Web jaoks Olive’iga](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 rakendus Phi-3 mini-4k-instruct-onnx’iga](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 mitmemudeliline AI-võimustatud märkmete rakenduse näidis](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Kohandatud Phi-3 mudelite peenhäälestamine ja integreerimine Prompt flow abil](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Kohandatud Phi-3 mudelite peenhäälestamine ja integreerimine Prompt flow abil Microsoft Foundrys](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Peenhäälestatud Phi-3 / Phi-3.5 mudeli hindamine Microsoft Foundry’s, keskendudes Microsofti vastutustundliku tehisintellekti põhimõtetele](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct keele ennustamise näidis (hiina/inglise keel)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG vestlusrobot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windowsi GPU kasutamine Prompt flow lahenduse loomiseks Phi-3.5-Instruct ONNX’iga](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite kasutamine Androidi rakenduse loomiseks](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Küsimused ja vastused .NET näidis, kasutades kohalikku ONNX Phi-3 mudelit Microsoft.ML.OnnxRuntime’iga](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Konsooli vestlus .NET rakendus Semantic Kerneliga ja Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI järeldussõlme koodipõhised näidised
    - Phi-4 näidised
      - [📓] [Projektikoodi genereerimine kasutades Phi-4-multimodaalset](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 näidised
      - [Ehita oma Visual Studio Code GitHub Copilot vestlus Microsoft Phi-3 perekonnaga](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Loo oma Visual Studio Code vestlus Copilot agent Phi-3.5 abil GitHub mudelitega](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Täiustatud arutluse näidised
    - Phi-4 näidised
      - [📓] [Phi-4-mini-arutlus või Phi-4-arutluse näidised](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Phi-4-mini-arutluse peenhäälestamine Microsoft Oliviga](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-arutluse peenhäälestamine Apple MLX’iga](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-arutlus GitHub mudelitega](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-arutlus Microsoft Foundry mudelitega](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demonstreerimised
      - [Phi-4-mini demonstreerimised majutatud Hugging Face Spacesis](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodaalsete demonstreerimised majutatud Hugging Face Spacesis](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Nägemise näidised
    - Phi-4 näidised
      - [📓] [Kasutage Phi-4-multimodaalset piltide lugemiseks ja koodi genereerimiseks](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)
    - Phi-3 / 3.5 näidised
      -  [📓][Phi-3-nägemise pildi tekst tekstiks](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-nägemine-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-nägemise CLIP manustus](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 taaskasutus](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-nägemine - visuaalne keeleassistent - Phi3-Vision ja OpenVINO abil](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision mitme kaadri või mitme pildi näidis](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision kohalik ONNX mudel Microsoft.ML.OnnxRuntime .NET abil](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menüüpõhine Phi-3 Vision kohalik ONNX mudel Microsoft.ML.OnnxRuntime .NET abil](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Arutlus-nägemise näidised
    - Phi-4-Arutlus-Nägemine-15B
      - [📓] [Phi-4-Arutlus-Nägemine-15B kasutamine jaywalkingu tuvastamiseks](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb)
      - [📓] [Phi-4-Arutlus-Nägemine-15B kasutamine matemaatika jaoks](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb)
      - [📓] [Phi-4-Arutlus-Nägemine-15B kasutamine kasutajaliidese tuvastamiseks](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb)

  - Matemaatika näidised
    -  Phi-4-Mini-Flash-Arutlus-Juhised näidised  [Matemaatika demo Phi-4-Mini-Flash-Arutlus-Juhistega](./md/02.Application/09.Math/MathDemo.ipynb)

  - Audio näidised
    - Phi-4 näidised
      - [📓] [Audio transkriptide väljavõtmine kasutades Phi-4-multimodaalset](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodaalne audiomudel](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodaalne kõnetõlke näidis](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET konsoolirakendus, kasutades Phi-4-multimodaalset heli analüüsimiseks ja transkripti genereerimiseks](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE näidised
    - Phi-3 / 3.5 näidised
      - [📓] [Phi-3.5 Ekspertide segu mudelid (MoEs) Sotsiaalmeedia näidis](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Taastamisega rikastatud genereerimise (RAG) torujuhtme loomine NVIDIA NIM Phi-3 MOE, Azure AI Search ja LlamaIndex’iga](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Funktsioonikõne näidised
    - Phi-4 näidised 🆕
      -  [📓] [Funktsioonikõne kasutamine Phi-4-mini’ga](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Funktsioonikõne kasutamine mitme agendi loomiseks Phi-4-mini’ga](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Funktsioonikõne kasutamine Ollamaga](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Funktsioonikõne kasutamine ONNX’iga](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Multimodaalne segamine näidised
    - Phi-4 näidised 🆕
      -  [📓] [Phi-4-multimodaalse kasutamine tehnoloogiauudiste ajakirjanikuna](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET konsoolirakendus, kasutades Phi-4-multimodaalset piltide analüüsimiseks](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi peenhäälestamine
  - [Peenhäälestamise stsenaariumid](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Peenhäälestamine vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Lase Phi-3’l saada tööstuse eksperdiks peenhäälestamise abil](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Phi-3 peenhäälestamine AI Toolkit’i abil VS Code’is](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Phi-3 peenhäälestamine Azure Machine Learning teenusega](./md/03.FineTuning/Introduce_AzureML.md)
  - [Phi-3 peenhäälestamine Loraga](./md/03.FineTuning/FineTuning_Lora.md)
  - [Phi-3 peenhäälestamine QLoraga](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Phi-3 peenhäälestamine Microsoft Foundry’s](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Phi-3 peenhäälestamine Azure ML CLI/SDK abil](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Peenhäälestamine Microsoft Oliviga](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Peenhäälestamine Microsoft Olive praktilises laboris](./md/03.FineTuning/olive-lab/readme.md)
  - [Phi-3-nägemise peenhäälestamine Weights and Bias’iga](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)

  - [Phi-3 peenhäälestamine Apple MLX raamistikuga](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision peenhäälestamine (ametlik tugi)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Phi-3 peenhäälestamine Kaito AKS-iga, Azure konteinerid (ametlik tugi)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 ja 3.5 Vision peenhäälestamine](https://github.com/2U1/Phi3-Vision-Finetune)

- Praktiline töötuba
  - [Uuenduslike mudelite uurimine: LLMid, SLMid, lokaalarendus ja palju muud](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP potentsiaali avamine: Microsoft Olive'ga peenhäälestamine](https://github.com/azure/Ignite_FineTuning_workshop)

- Akadeemilised uurimuspaberid ja väljaanded
  - [Textbooks Are All You Need II: phi-1.5 tehniline aruanne](https://arxiv.org/abs/2309.05463)
  - [Phi-3 tehniline aruanne: võimas keelemudel lokaalselt teie telefonis](https://arxiv.org/abs/2404.14219)
  - [Phi-4 tehniline aruanne](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini tehniline aruanne: kompaktne kuid võimas multimodaalne keelemudel LoRAde seguga](https://arxiv.org/abs/2503.01743)
  - [Väikeste keelemudelite optimeerimine sõidukisiseste funktsioonikõnede jaoks](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 peenhäälestamine mitmevalikuliste küsimuste vastamiseks: meetod, tulemused ja väljakutsed](https://arxiv.org/abs/2501.01588)
  - [Phi-4-lähenemine tehniline aruanne](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-lähenemine tehniline aruanne](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi mudelite kasutamine

### Phi Microsoft Foundrys

Saate õppida, kuidas kasutada Microsoft Phi-d ja kuidas ehitada E2E lahendusi erinevate riistvarade jaoks. Phi kogemiseks alustage mudelitega mängimisest ja Phi kohandamisest oma stsenaariumide jaoks [Microsoft Foundry Azure AI mudelikataloogi](https://aka.ms/phi3-azure-ai) abil, lisateavet leiate juba alustades [Microsoft Foundrys](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Mänguväljak**
Igal mudelil on pühendatud mänguväljak mudeli testimiseks [Azure AI Playground](https://aka.ms/try-phi3).

### Phi GitHubi mudelitel

Saate õppida, kuidas kasutada Microsoft Phi-d ja kuidas ehitada E2E lahendusi erinevate riistvarade jaoks. Phi kogemiseks alustage mudeliga mängimisest ja Phi kohandamisest oma stsenaariumide jaoks [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) abil, lisateavet leiate juba alustades [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Mänguväljak**
Igal mudelil on pühendatud [mänguväljak mudeli testimiseks](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi Hugging Face'is

Mudeli leiate ka [Hugging Face'ist](https://huggingface.co/microsoft)

**Mänguväljak**
 [Hugging Chat mänguväljak](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 Teised kursused

Meie meeskond toodab ka teisi kursuseid! Vaadake:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j algajatele](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js algajatele](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain algajatele](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agendid
[![AZD algajatele](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI algajatele](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP algajatele](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Tehisintellekti agendid algajatele](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatiivse tehisintellekti sari
[![Generatiivne AI algajatele](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatiivne AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatiivne AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatiivne AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Põhiteadmised
[![Masinõpe algajatele](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Andmeteadus algajatele](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI algajatele](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Küberturvalisus algajatele](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Veebiarendus algajatele](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![Asjade internet algajatele](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR arendus algajatele](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot sari
[![Copilot AI paarisprogrammeerimiseks](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET jaoks](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot seiklus](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Vastutustundlik AI

Microsoft on pühendunud aitama klientidel kasutada meie AI tooteid vastutustundlikult, jagades oma kogemusi ja ehitades usaldusel põhinevaid partnerlusi tööriistadega nagu Läbipaistvuse märkmed ja Mõjuhinnangud. Paljusid neist ressurssidest leiab aadressilt [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofti lähenemine vastutustundlikule AI-le põhineb meie AI põhimõtetel: õiglus, usaldusväärsus ja ohutus, privaatsus ja turvalisus, kaasatus, läbipaistvus ning vastutus.

Suurte mahtude loomuliku keele-, pildi- ja kõnemudelid - nagu selles näites kasutatud mudelid - võivad käituda ebaõiglaselt, usaldusväärselt või solvavalt, põhjustades kahju. Palun vaadake [Azure OpenAI teenuse läbipaistvuse märkust](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), et olla teadlik riskidest ja piirangutest.


Nende riskide maandamise soovitatav lähenemisviis on lisada oma arhitektuuri ohutussüsteem, mis suudab tuvastada ja vältida kahjulikku käitumist. [Azure AI sisu turvalisus](https://learn.microsoft.com/azure/ai-services/content-safety/overview) pakub sõltumatut kaitsekihi, mis suudab rakendustes ja teenustes tuvastada kahjulikku kasutaja- ja tehisintellekti loodud sisu. Azure AI sisu turvalisusesse kuuluvad tekstide ja piltide API-d, mis võimaldavad tuvastada kahjulikku materjali. Microsoft Foundry raames võimaldab Content Safety teenus vaadata, uurida ja proovida näitekoodi kahjuliku sisu tuvastamiseks erinevates modaliteetides. Järgmine [kiirjuhendi dokumentatsioon](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) juhendab teid teenusele taotluste tegemisel.

Teine kaalutav aspekt on kogu rakenduse jõudlus. Mitmemodaalsete ja mitmemudelist rakenduste puhul mõistame jõudluse all seda, et süsteem toimib nii, nagu teie ja teie kasutajad ootavad, sealhulgas ei genereeri kahjulikke väljundeid. Oluline on hinnata oma kogu rakenduse jõudlust, kasutades [jõudluse ja kvaliteedi ning riski ja turvalisuse hindajaid](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Teil on ka võimalus luua ja hinnata [kohandatud hindajate](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) abil.

Võite oma AI-rakendust hinnata arenduskeskkonnas, kasutades [Azure AI hindamis-SDK-d](https://microsoft.github.io/promptflow/index.html). Kasutades testandmekogu või eesmärki, mõõdetakse teie generatiivse AI-rakenduse tulemusi kvantitatiivselt kas sisseehitatud või teie valitud kohandatud hindajatega. Alustamiseks Azure AI hindamis-SDK-ga süsteemi hindamiseks võite järgida [kiirjuhendit](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kui olete hindamiskorra käivitanud, saate [tulemusi visualiseerida Microsoft Foundry's](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Kaubamärgid

See projekt võib sisaldada projekte, tooteid või teenuseid tähistavaid kaubamärke või logosid. Microsofti kaubamärkide või logode autoriseeritud kasutamine allub ja peab järgima [Microsofti kaubamärgi- ja brändijuhiseid](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Microsofti kaubamärkide või logode kasutamine selle projekti muudetud versioonides ei tohi tekitada segadust ega viidata Microsofti sponsorlusele. Kolmandate osapoolte kaubamärkide või logode kasutamine allub nende kolmandate osapoolte poliitikatele.

## Abi saamine

Kui teil tekib küsimusi või teil on raskusi AI-rakenduste loomisel, liituge:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Kui teil on toodete tagasisidet või vigu arendamisel, külastage:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->