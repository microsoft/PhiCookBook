<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2e4b490f4bd424b095f21e38c6af33b",
  "translation_date": "2026-01-05T14:42:54+00:00",
  "source_file": "README.md",
  "language_code": "et"
}
-->
# Phi Kokkuraamat: Praktilised näited Microsofti Phi mudelitega

[![Ava ja kasuta näidiseid GitHub Codespaces'is](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Ava Dev Containers'is](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub panustajad](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub probleemid](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-päringud](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR-d on teretulnud](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub jälgijad](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forkid](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub tärnid](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi on Microsofti arendatud avatud lähtekoodiga tehisintellekti mudelite sari.

Phi on hetkel kõige võimsam ja kulutõhusam väikese keelemudeliga (SLM), mis annab väga head tulemused mitmekeelses tekstis, põhjendamises, teksti/vestluse genereerimises, kodeerimises, piltides, helis ja muudes stsenaariumides.

Saate Phi paigaldada kas pilve või servaseadmetesse ning lihtsasti ehitada generatiivseid tehisintellekti rakendusi piiratud arvutusvõimsusega.

Alustamiseks tehke järgmist:
1. **Tehke hoidlast Fork**: Vajutage [![GitHub forkid](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Kloonige hoidla**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Liituge Microsoft AI Discord kogukonnaga ja kohtuge ekspertide ning kaasaarendajatega**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/et/cover.eb18d1b9605d754b.webp)

### 🌐 Mitmekeelne tugi

#### Toetatud GitHub Actioni kaudu (automaatne ja alati ajakohane)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Araabia](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaaria](../bg/README.md) | [Birma (Myanmar)](../my/README.md) | [Hiina (simplified)](../zh/README.md) | [Hiina (traditsiooniline, Hong Kong)](../hk/README.md) | [Hiina (traditsiooniline, Macau)](../mo/README.md) | [Hiina (traditsiooniline, Taiwan)](../tw/README.md) | [Horvaadi](../hr/README.md) | [Tšehhi](../cs/README.md) | [Taani](../da/README.md) | [Hollandi](../nl/README.md) | [Eesti](./README.md) | [Soome](../fi/README.md) | [Prantsuse](../fr/README.md) | [Saksa](../de/README.md) | [Kreeka](../el/README.md) | [Heebrea](../he/README.md) | [Hindi](../hi/README.md) | [Ungari](../hu/README.md) | [Indoneesia](../id/README.md) | [Itaalia](../it/README.md) | [Jaapani](../ja/README.md) | [Kannada](../kn/README.md) | [Korea](../ko/README.md) | [Leedu](../lt/README.md) | [Malai](../ms/README.md) | [Malajalami](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigeeria pidžin](../pcm/README.md) | [Norra](../no/README.md) | [Pärsia (Farsi)](../fa/README.md) | [Poola](../pl/README.md) | [Portugali (Brasiilia)](../br/README.md) | [Portugali (Portugal)](../pt/README.md) | [Pandžabi (Gurmukhi)](../pa/README.md) | [Rumeenia](../ro/README.md) | [Vene](../ru/README.md) | [Serbia (kyrillitsa)](../sr/README.md) | [Slovaki](../sk/README.md) | [Sloveeni](../sl/README.md) | [Hispaania](../es/README.md) | [Suahiili](../sw/README.md) | [Rootsi](../sv/README.md) | [Tagalogi (Filipiinid)](../tl/README.md) | [Tamili](../ta/README.md) | [Telugu](../te/README.md) | [Tai](../th/README.md) | [Türgi](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnam](../vi/README.md)

> **Eelistate kohalikku kloonimist?**

> See hoidla sisaldab üle 50 keele tõlkeid, mis oluliselt suurendab allalaadimismahtu. Tõlgeteta kloonimiseks kasutage sparse checkout'i:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> See annab teile kõik vajaliku kursuse lõpuleviimiseks palju kiirema allalaadimisega.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Sisukord

- Sissejuhatus
  - [Tere tulemast Phi perekonda](./md/01.Introduction/01/01.PhiFamily.md)
  - [Keskkonna seadistamine](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Oluliste tehnoloogiate mõistmine](./md/01.Introduction/01/01.Understandingtech.md)
  - [Tehisintellekti ohutus Phi mudelite puhul](./md/01.Introduction/01/01.AISafety.md)
  - [Phi riistvaraline tugi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi mudelid ja platvormidel saadavus](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai ja Phi kasutamine](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace mudelid](https://github.com/marketplace/models)
  - [Azure AI mudelite kataloog](https://ai.azure.com)

- Phi inferents erinevates keskkondades
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub mudelid](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry mudelite kataloog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi perekonna inferents
    - [Phi inferents iOS-is](./md/01.Introduction/03/iOS_Inference.md)
    - [Phi inferents Androidis](./md/01.Introduction/03/Android_Inference.md)
    - [Phi inferents Jetsonis](./md/01.Introduction/03/Jetson_Inference.md)
    - [Phi inferents AI arvutis](./md/01.Introduction/03/AIPC_Inference.md)
    - [Phi inferents Apple MLX raamistiku abil](./md/01.Introduction/03/MLX_Inference.md)
    - [Phi inferents kohalikus serveris](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Remote serveri Phi inferents AI Toolkituga](./md/01.Introduction/03/Remote_Interence.md)
    - [Phi inferents Rustiga](./md/01.Introduction/03/Rust_Inference.md)
    - [Phi--Vision inferents kohapeal](./md/01.Introduction/03/Vision_Inference.md)
    - [Phi inferents Kaito AKS, Azure konteineritega (ametlik tugi)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi perekonna kvantifitseerimine](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantifitseerimine kasutades llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantifitseerimine kasutades generatiivse AI laiendusi onnxruntime jaoks](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantifitseerimine kasutades Intel OpenVINO't](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantifitseerimine kasutades Apple MLX raamistiku](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi hindamine
    - [Vastutustundlik AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry hindamine](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow kasutamine hindamiseks](./md/01.Introduction/05/Promptflow.md)
 
- RAG koos Azure AI otsinguga
    - [Kuidas kasutada Phi-4-mini ja Phi-4-multimodaalset (RAG) Azure AI otsinguga](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi rakenduste arendamise näited
  - Teksti- ja vestlusrakendused
    - Phi-4 näited 🆕
      - [📓] [Vestle Phi-4-mini ONNX mudeliga](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Vestlus Phi-4 kohaliku ONNX mudeliga .NET-is](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Vestlus .NET konsoolirakenduses Phi-4 ONNX kasutades Semantic Kernelit](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 näited
      - [Kohalik chatbot brauseris kasutades Phi3, ONNX Runtime Webi ja WebGPU-t](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVINO vestlus](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Mitmemudeliline - interaktiivne Phi-3-mini ja OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Põranda ehitamine ja Phi-3 kasutamine MLFlowga](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Mudeli optimeerimine - Kuidas optimeerida Phi-3-minimudelit ONNX Runtime Web jaoks Olive’ga](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 rakendus Phi-3 mini-4k-instruct-onnx-ga](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 mitmemudeliline tehisintellektiga märkmiku rakenduse näidis](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Kohandatud Phi-3 mudelite täpsustamine ja integreerimine Prompt flow abil](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Kohandatud Phi-3 mudelite täpsustamine ja integreerimine Prompt flow abil Azure AI Foundrys](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Täpsustatud Phi-3 / Phi-3.5 mudeli hindamine Azure AI Foundrys, keskendudes Microsofti vastutustundliku AI põhimõtetele](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct keeleprognoosi näidis (hiina/inglise)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG vestlusrobot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU kasutamine Prompt flow lahenduse loomiseks Phi-3.5-Instruct ONNX-ga](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite kasutamine Androidi rakenduse loomiseks](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Küsimuste ja vastuste .NET näidis lokaalse ONNX Phi-3 mudeliga, kasutades Microsoft.ML.OnnxRuntime'i](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Käsurea vestlus .NET rakendus Semantic Kernel ja Phi-3-ga](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK koodipõhised näidised 
    - Phi-4 näidised 🆕
      - [📓] [Projektikoodi genereerimine Phi-4-multimodal abil](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 näidised
      - [Ehita oma Visual Studio Code GitHub Copiloti vestlus Microsoft Phi-3 perekonnaga](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Loo oma Visual Studio Code vestlus Copilot agent Phi-3.5-ga GitHub mudelite kaudu](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Täiustatud arutluse näidised
    - Phi-4 näidised 🆕
      - [📓] [Phi-4-mini-tarklemine või Phi-4-tarklemise näidised](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Phi-4-mini-tarklemise täpsustamine Microsoft Olive'ga](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-tarklemise täpsustamine Apple MLX-ga](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-tarklemine GitHub mudelitega](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-tarklemine Azure AI Foundry mudelitega](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demo’s
      - [Phi-4-mini demo’d Hugging Face Spaces’is majutatud](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demo’d Hugging Face Spaces’is majutatud](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Nägemise näidised
    - Phi-4 näidised 🆕
      - [📓] [Kasutage Phi-4-multimodali piltide lugemiseks ja koodi genereerimiseks](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 näidised
      -  [📓][Phi-3-nägemis piltide tekst tekstiks](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-nägemis ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-nägemis CLIP manustus](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 taaskasutus](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-nägemis - visuaalne keeleassistent - Phi3-Nägemis ja OpenVINO-ga](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 nägemine Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 nägemine OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Nägemine mitme kaadri või mitme pildi näidis](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 nägemine kohalik ONNX mudel, kasutades Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menüü põhine Phi-3 nägemine kohalik ONNX mudel, kasutades Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Matemaatika näidised
    - Phi-4-Mini-Flash-Tarklemise juhiste näidised 🆕 [Matemaatika demo Phi-4-Mini-Flash-Tarklemise juhistega](./md/02.Application/09.Math/MathDemo.ipynb)

  - Audio näidised
    - Phi-4 näidised 🆕
      - [📓] [Audiotekstide väljavõtmine Phi-4-multimodal abil](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal audio näidis](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal kõnetõlke näidis](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET käsurea rakendus Phi-4-multimodal audio kasutamiseks heli faili analüüsimiseks ja transkriptsiooni genereerimiseks](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE näidised
    - Phi-3 / 3.5 näidised
      - [📓] [Phi-3.5 Ekspertide segu mudelid (MoEs) sotsiaalmeedia näidis](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Päringu-põhise genereerimise (RAG) torujuhtme loomine NVIDIA NIM Phi-3 MOE, Azure AI Search ja LlamaIndex abil](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Funktsioonikõnede näidised
    - Phi-4 näidised 🆕
      -  [📓] [Funktsioonikõnede kasutamine Phi-4-mini’ga](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Funktsioonikõnede kasutamine mitmeagendiliste loomiseks Phi-4-mini’ga](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Funktsioonikõnede kasutamine Ollama’ga](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Funktsioonikõnede kasutamine ONNX’iga](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Mitmemodaalne segamine näidised
    - Phi-4 näidised 🆕
      -  [📓] [Phi-4-multimodal kasutamine tehnoloogiajournalistina](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET käsurea rakendus Phi-4-multimodal piltide analüüsiks](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi täpsustamine
  - [Täpsustamise stsenaariumid](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Täpsustamine vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Las Phi-3 saab tööstuse eksperdiks täpsustamisel](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Phi-3 täpsustamine AI tööriistakomplektiga VS Code jaoks](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Phi-3 täpsustamine Azure Machine Learning Teenusega](./md/03.FineTuning/Introduce_AzureML.md)
  - [Phi-3 täpsustamine Loraga](./md/03.FineTuning/FineTuning_Lora.md)
  - [Phi-3 täpsustamine QLoraga](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Phi-3 täpsustamine Azure AI Foundry-ga](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Phi-3 täpsustamine Azure ML CLI/SDK-ga](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Täpsustamine Microsoft Olive’ga](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive praktiline töölaud](./md/03.FineTuning/olive-lab/readme.md)
  - [Phi-3-nägemise täpsustamine Weights and Biases’ga](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Phi-3 täpsustamine Apple MLX raamistiku abil](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-nägemise täpsustamine (ametlik tugi)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Phi-3 täpsustamine KaiTo AKS, Azure konteineritega (ametlik tugi)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 ja 3.5 nägemise täpsustamine](https://github.com/2U1/Phi3-Vision-Finetune)

- Praktilised töötoad
  - [Uuenduslike mudelite uurimine: LLMid, SLMid, kohalik arendus ja palju muud](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP potentsiaali avamine: täpsustamine Microsoft Olive’ga](https://github.com/azure/Ignite_FineTuning_workshop)

- Akadeemilised uurimispaberid ja väljaanded
  - [Õpikud on kõik, mida vaja II: phi-1.5 tehniline aruanne](https://arxiv.org/abs/2309.05463)
  - [Phi-3 tehniline aruanne: väga võimekas keelemudel teie telefoni kohapeal](https://arxiv.org/abs/2404.14219)
  - [Phi-4 tehniline aruanne](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini tehniline aruanne: kompaktsed, ent võimsad multimodaalsed keelemudelid LoRAde seguga](https://arxiv.org/abs/2503.01743)
  - [Väikeste keelemudelite optimeerimine sõiduki sees funktsioonikutsumiseks](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 peenhäälestamine valikvastustega küsimustele vastamiseks: metoodika, tulemused ja väljakutsed](https://arxiv.org/abs/2501.01588)
  - [Phi-4-loogika tehniline aruanne](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-loogika tehniline aruanne](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi mudelite kasutamine

### Phi Azure AI Foundryl

Saate õppida, kuidas kasutada Microsoft Phi ja kuidas ehitada E2E lahendusi erinevatel riistvaraseadmetel. Phi enda kogemiseks alustage mudelitega mängimist ja Phi kohandamist oma stsenaariumite jaoks, kasutades [Azure AI Foundry Azure AI Mudelikataloogi](https://aka.ms/phi3-azure-ai). Lisateavet leiate juhendist Alustamine [Azure AI Foundryga](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Mänguväljak**
Igal mudelil on oma pühendatud testimiskeskkond [Azure AI Playground](https://aka.ms/try-phi3).

### Phi GitHubi mudelites

Saate õppida, kuidas kasutada Microsoft Phi ja kuidas ehitada E2E lahendusi erinevatel riistvaraseadmetel. Phi enda kogemiseks alustage mudeliga mängimist ja Phi kohandamist oma stsenaariumite jaoks, kasutades [GitHubi mudelikataloogi](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Lisateavet leiate juhendist Alustamine [GitHub mudelikataloogiga](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Mänguväljak**
Igal mudelil on pühendatud [testimiskeskkond mudeli proovimiseks](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi Hugging Face’is

Mudelit leiate ka [Hugging Face’i lehelt](https://huggingface.co/microsoft).

**Mänguväljak**
[Hugging Chat mänguväljak](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 Teised kursused

Meie meeskond pakub ka teisi kursuseid! Vaadake:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j algajatele](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js algajatele](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agendid
[![AZD algajatele](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI algajatele](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP algajatele](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agendid algajatele](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatiivse tehisintellekti sari
[![Generatiivne tehisintellekt algajatele](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatiivne AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatiivne AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatiivne AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Põhiteadmised
[![Masinõpe algajatele](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Andmeteadus algajatele](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![Tehisintellekt algajatele](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kyberturvalisus algajatele](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Veebiarendus algajatele](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT algajatele](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR arendus algajatele](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot sari
[![Copilot AI paarisprogrammeerimiseks](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET jaoks](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot seiklus](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Vastutustundlik AI

Microsoft on pühendunud aitama klientidel kasutada meie tehisintellekti tooteid vastutustundlikult, jagada oma õppetunde ja luua usaldusel põhinevaid partnerlusi tööriistade nagu Läbipaistvuse märkmed ja Mõju hindamised abil. Paljusid neist ressurssidest leiate aadressilt [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofti lähenemine vastutustundlikule tehisintellektile põhineb meie AI põhimõtetel: õiglus, usaldusväärsus ja turvalisus, privaatsus ja turvalisus, kaasamine, läbipaistvus ja aruandekohustus.

Suurte keele-, pildi- ja kõnemudelite - nagu selles näites kasutatavad - käitumine võib potentsiaalselt olla ebaõiglane, ebakindel või solvav, mis võib tekitada kahju. Palun tutvuge [Azure OpenAI teenuse läbipaistvuse märkmega](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), et olla teadlik riskidest ja piirangutest.

Soovitatav lähenemine nende riskide leevendamiseks on lisada oma arhitektuuri turvasüsteem, mis suudab tuvastada ja ennetada kahjulikku käitumist. [Azure AI Sisuturvalisus](https://learn.microsoft.com/azure/ai-services/content-safety/overview) pakub sõltumatut kaitsekihi, mis suudab rakendustes ja teenustes tuvastada kahjulikku kasutajate ja tehisintellekti poolt genereeritud sisu. Azure AI Sisuturvalisus sisaldab teksti- ja pildirakendusliideseid, mis võimaldavad tuvastada kahjulikku materjali. Azure AI Foundrys võimaldab Sisuturvalisuse teenus vaadata, uurida ja proovida näitekoodi kahjuliku sisu tuvastamiseks erinevates modaliteetides. Järgmine [kiirjuhendi dokumentatsioon](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) juhendab teid teenusele päringute tegemisel.

Teine oluline aspekt on kogu rakenduse jõudlus. Multimodaalsete ja mitmemudelist rakenduste puhul mõistame jõudlust nii, et süsteem toimib teie ja teie kasutajate ootustele vastavalt, sh mitte kahjulikke tulemusi genereerides. Oluline on hinnata kogu rakenduse jõudlust, kasutades [Jõudluse ja Kvaliteedi ning Riskide ja Turvalisuse hindajaid](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Teil on ka võimalus luua ja hinnata [kohandatud hindajatega](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).
Saate oma tehisintellekti rakendust hinnata oma arenduskeskkonnas, kasutades [Azure AI Evaluation SDK-d](https://microsoft.github.io/promptflow/index.html). Kasutades kas testandmestikku või sihtmärki, mõõdetakse teie genereeriva tehisintellekti rakenduse tulemusi kvantitatiivselt sisseehitatud hindajate või teie valitud kohandatud hindajatega. Azure AI Evaluation SDK-ga süsteemi hindamise alustamiseks võite järgida [kiirstart juhendit](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kui olete hindamise käivitanud, saate [tulemusi visualiseerida Azure AI Foundrys](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Kaubamärgid

See projekt võib sisaldada kaubamärke või logosid projektide, toodete või teenuste jaoks. Microsofti kaubamärkide või logode autoriseeritud kasutamine allub ja peab järgima [Microsofti kaubamärkide ja brändi juhiseid](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general). Microsofti kaubamärkide või logode kasutamine selle projekti muudetud versioonides ei tohi põhjustada segadust ega viidata Microsofti toetusele. Kolmandate osapoolte kaubamärkide või logode kasutamine allub nende kolmandate osapoolte poliitikatele.

## Abi saamine

Kui teil tekib takistusi või teil on küsimusi tehisintellekti rakenduste loomise kohta, liituge:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Kui teil on tootearenduse tagasisidet või vigu, külastage:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:
See dokument on tõlgitud tehisintellekti tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsuse, tuleb arvestada, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta tõlgendustest või arusaamatustest, mis võivad tekkida selle tõlke kasutamisest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->