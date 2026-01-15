<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2e4b490f4bd424b095f21e38c6af33b",
  "translation_date": "2026-01-05T12:26:16+00:00",
  "source_file": "README.md",
  "language_code": "da"
}
-->
# Phi Cookbook: Praktiske eksempler med Microsofts Phi-modeller

[![Åbn og brug eksemplerne i GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Åbn i Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub bidragydere](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Velkommen](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub observatører](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stjerner](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi er en serie af open source AI-modeller udviklet af Microsoft.

Phi er i øjeblikket den mest kraftfulde og omkostningseffektive lille sprogmodel (SLM) med meget gode benchmarks inden for flersprog, ræsonnering, tekst/chat-generering, kodning, billeder, lyd og andre scenarier.

Du kan udrulle Phi til skyen eller til edge-enheder, og du kan nemt bygge generative AI-applikationer med begrænset computerkraft.

Følg disse trin for at komme i gang med at bruge disse ressourcer:
1. **Fork depotet**: Klik [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Klon depotet**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Deltag i Microsoft AI Discord-fællesskabet og mød eksperter og medudviklere**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/da/cover.eb18d1b9605d754b.webp)

### 🌐 Flersprogsunderstøttelse

#### Understøttet via GitHub Action (Automatiseret & Altid Opdateret)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabisk](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarsk](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Kinesisk (Forenklet)](../zh/README.md) | [Kinesisk (Traditionel, Hong Kong)](../hk/README.md) | [Kinesisk (Traditionel, Macau)](../mo/README.md) | [Kinesisk (Traditionel, Taiwan)](../tw/README.md) | [Kroatisk](../hr/README.md) | [Tjekkisk](../cs/README.md) | [Dansk](./README.md) | [Hollandsk](../nl/README.md) | [Estisk](../et/README.md) | [Finsk](../fi/README.md) | [Fransk](../fr/README.md) | [Tysk](../de/README.md) | [Græsk](../el/README.md) | [Hebraisk](../he/README.md) | [Hindi](../hi/README.md) | [Ungarsk](../hu/README.md) | [Indonesisk](../id/README.md) | [Italiensk](../it/README.md) | [Japansk](../ja/README.md) | [Kannada](../kn/README.md) | [Koreansk](../ko/README.md) | [Litauisk](../lt/README.md) | [Malayisk](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalesisk](../ne/README.md) | [Nigeriansk Pidgin](../pcm/README.md) | [Norsk](../no/README.md) | [Persisk (Farsi)](../fa/README.md) | [Polsk](../pl/README.md) | [Portugisisk (Brasilien)](../br/README.md) | [Portugisisk (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumænsk](../ro/README.md) | [Russisk](../ru/README.md) | [Serbisk (Kyrillisk)](../sr/README.md) | [Slovakisk](../sk/README.md) | [Slovensk](../sl/README.md) | [Spansk](../es/README.md) | [Swahili](../sw/README.md) | [Svensk](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thailandsk](../th/README.md) | [Tyrkisk](../tr/README.md) | [Ukrainsk](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamesisk](../vi/README.md)

> **Foretrækker du at klone lokalt?**

> Dette repository inkluderer 50+ sprogoversættelser, som væsentligt forøger downloadstørrelsen. For at klone uden oversættelser, brug sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Dette giver dig alt, hvad du behøver for at gennemføre kurset med meget hurtigere download.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Indholdsfortegnelse

- Introduktion
  - [Velkommen til Phi-familien](./md/01.Introduction/01/01.PhiFamily.md)
  - [Opsætning af dit miljø](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Forståelse af centrale teknologier](./md/01.Introduction/01/01.Understandingtech.md)
  - [AI-sikkerhed for Phi-modeller](./md/01.Introduction/01/01.AISafety.md)
  - [Phi hardwareunderstøttelse](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi-modeller & tilgængelighed på tværs af platforme](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Brug af Guidance-ai og Phi](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace-modeller](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- Inference Phi i forskellige miljøer
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub Modeller](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Inference Phi-familien
    - [Inference Phi på iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inference Phi på Android](./md/01.Introduction/03/Android_Inference.md)
    - [Inference Phi på Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inference Phi på AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inference Phi med Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Inference Phi på lokal server](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inference Phi på fjernserver ved brug af AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inference Phi med Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inference Phi--Vision lokalt](./md/01.Introduction/03/Vision_Inference.md)
    - [Inference Phi med Kaito AKS, Azure Containers (officiel understøttelse)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Kvantisering af Phi-familien](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Kvantisering af Phi-3.5 / 4 vha. llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Kvantisering af Phi-3.5 / 4 vha. Generative AI-udvidelser for onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Kvantisering af Phi-3.5 / 4 vha. Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Kvantisering af Phi-3.5 / 4 vha. Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Evaluering af Phi
    - [Ansvarlig AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry til evaluering](./md/01.Introduction/05/AIFoundry.md)
    - [Brug af Promptflow til evaluering](./md/01.Introduction/05/Promptflow.md)
 
- RAG med Azure AI Search
    - [Sådan bruger du Phi-4-mini og Phi-4-multimodal (RAG) med Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi applikationsudviklings eksempler
  - Tekst- & Chat-applikationer
    - Phi-4 eksempler 🆕
      - [📓] [Chat med Phi-4-mini ONNX Model](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat med Phi-4 lokal ONNX Model .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Chat .NET Console App med Phi-4 ONNX ved brug af Sementic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 eksempler
      - [Lokal chatbot i browser med Phi3, ONNX Runtime Web og WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - Interaktiv Phi-3-mini og OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Byg en wrapper og brug Phi-3 med MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Modeloptimering - Hvordan man optimerer Phi-3-minimodel til ONNX Runtime Web med Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3-app med Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 Multi Model AI Powered Notes App Eksempel](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Finjuster og integrer brugerdefinerede Phi-3 modeller med Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Finjuster og integrer brugerdefinerede Phi-3 modeller med Prompt flow i Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Evaluer den finjusterede Phi-3 / Phi-3.5 model i Azure AI Foundry med fokus på Microsofts principper for ansvarlig AI](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct sprogforudsigelseseksempel (kinesisk/engelsk)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Brug af Windows GPU til at skabe Prompt flow-løsning med Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Brug af Microsoft Phi-3.5 tflite til at skabe Android-app](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET eksempel ved brug af lokal ONNX Phi-3 model med Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Konsolchat .NET-app med Semantic Kernel og Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK kodebaserede eksempler 
    - Phi-4 Eksempler 🆕
      - [📓] [Generer projektkode med Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 Eksempler
      - [Byg din egen Visual Studio Code GitHub Copilot Chat med Microsoft Phi-3 familien](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Skab din egen Visual Studio Code Chat Copilot Agent med Phi-3.5 ved GitHub Modeller](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Avancerede Resonerings Eksempler
    - Phi-4 Eksempler 🆕
      - [📓] [Phi-4-mini-resonering eller Phi-4-resonering Eksempler](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Finjustering af Phi-4-mini-resonering med Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Finjustering af Phi-4-mini-resonering med Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-resonering med GitHub Modeller](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-resonering med Azure AI Foundry Modeller](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demoer
      - [Phi-4-mini demoer hostet på Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demoer hostet på Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Vision Eksempler
    - Phi-4 Eksempler 🆕
      - [📓] [Brug Phi-4-multimodal til at læse billeder og generere kode](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 Eksempler
      -  [📓][Phi-3-vision-Billede tekst til tekst](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Indlejring](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Genbrug](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Visuel sprogassistent - med Phi3-Vision og OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision multi-frame eller multi-billede eksempel](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision Lokal ONNX Model ved brug af Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menu-baseret Phi-3 Vision Lokal ONNX Model ved brug af Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Matematik Eksempler
    -  Phi-4-Mini-Flash-Reasoning-Instruct Eksempler 🆕 [Matematik Demo med Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - Audio Eksempler
    - Phi-4 Eksempler 🆕
      - [📓] [Udtrækning af lydtransskripter med Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal Lyd Eksempel](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal Taleoversættelseseksempel](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET konsolapplikation ved brug af Phi-4-multimodal Audio til at analysere en lydfil og generere transskription](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE Eksempler
    - Phi-3 / 3.5 Eksempler
      - [📓] [Phi-3.5 Mixture of Experts Modeller (MoEs) Social Media Eksempel](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Opbygning af en Retrieval-Augmented Generation (RAG) Pipeline med NVIDIA NIM Phi-3 MOE, Azure AI Search og LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Funktionskald Eksempler
    - Phi-4 Eksempler 🆕
      -  [📓] [Brug af Funktionskald med Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Brug af Funktionskald til at skabe multi-agenter med Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Brug af Funktionskald med Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Brug af Funktionskald med ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Multimodal Blanding Eksempler
    - Phi-4 Eksempler 🆕
      -  [📓] [Brug af Phi-4-multimodal som teknologijournalist](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET konsolapplikation ved brug af Phi-4-multimodal til at analysere billeder](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Finjustering af Phi Eksempler
  - [Finjusteringsscenarier](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Finjustering vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Finjustering: Lad Phi-3 blive en brancheekspert](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Finjustering af Phi-3 med AI Toolkit til VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Finjustering af Phi-3 med Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Finjustering af Phi-3 med Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Finjustering af Phi-3 med QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Finjustering af Phi-3 med Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Finjustering af Phi-3 med Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Finjustering med Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Finjustering med Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Finjustering af Phi-3-vision med Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Finjustering af Phi-3 med Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Finjustering af Phi-3-vision (officiel support)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Finjustering af Phi-3 med Kaito AKS , Azure Containers (officiel support)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Finjustering af Phi-3 og 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands on Lab
  - [Udforskning af banebrydende modeller: LLMs, SLMs, lokal udvikling og mere](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Frigørelse af NLP potentiale: Finjustering med Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Akademiske forskningspapirer og publikationer
  - [Lærebøger er alt, hvad du behøver II: phi-1.5 teknisk rapport](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Teknisk Rapport: En meget kapabel sprogmodel lokalt på din telefon](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Teknisk Rapport](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Teknisk Rapport: Kompakte, men kraftfulde multimodale sprogmodeller via Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Optimering af små sprogmodeller til funktion-opkald i køretøj](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Finjustering af PHI-3 til multiple-choice spørgsmål: Metodologi, resultater og udfordringer](https://arxiv.org/abs/2501.01588)
  - [Phi-4-resonering Teknisk Rapport](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-resonering Teknisk Rapport](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Brug af Phi Modeller

### Phi på Azure AI Foundry

Du kan lære, hvordan du bruger Microsoft Phi, og hvordan du bygger E2E-løsninger i dine forskellige hardwareenheder. For at opleve Phi selv, start med at lege med modellerne og tilpasse Phi til dine scenarier ved hjælp af [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Du kan lære mere under Kom godt i gang med [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Playground**
Hver model har en dedikeret legeplads til at teste modellen [Azure AI Playground](https://aka.ms/try-phi3).

### Phi på GitHub Modeller

Du kan lære, hvordan du bruger Microsoft Phi, og hvordan du bygger E2E-løsninger i dine forskellige hardwareenheder. For at opleve Phi selv, start med at lege med modellen og tilpasse Phi til dine scenarier ved hjælp af [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Du kan lære mere under Kom godt i gang med [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Playground**
Hver model har en dedikeret [legeplads til at teste modellen](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi på Hugging Face

Du kan også finde modellen på [Hugging Face](https://huggingface.co/microsoft).

**Playground**
 [Hugging Chat legeplads](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 Andre Kurser

Vores team producerer flere kurser! Tjek:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agenter
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generativ AI Serie
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Kerne læring
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Serie
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Ansvarlig AI

Microsoft er engageret i at hjælpe vores kunder med at bruge vores AI-produkter ansvarligt, dele vores erfaringer og opbygge tillidsbaserede partnerskaber gennem værktøjer som Transparency Notes og Impact Assessments. Mange af disse ressourcer findes på [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofts tilgang til ansvarlig AI er funderet i vores AI-principper for retfærdighed, pålidelighed og sikkerhed, privatliv og sikkerhed, inklusivitet, gennemsigtighed og ansvarlighed.

Store sprog-, billede- og tale-modeller i stor skala – som dem, der bruges i dette eksempel – kan potentielt opføre sig på måder, der er uretfærdige, upålidelige eller krænkende, hvilket kan forårsage skade. Konsulter venligst [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) for at blive informeret om risici og begrænsninger.

Den anbefalede tilgang til at mindske disse risici er at inkludere et sikkerhedssystem i din arkitektur, der kan opdage og forhindre skadelig adfærd. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) giver et uafhængigt beskyttelseslag, der kan opdage skadeligt brugergenereret og AI-genereret indhold i applikationer og tjenester. Azure AI Content Safety inkluderer tekst- og billede-API'er, som gør det muligt at opdage materiale, der er skadeligt. Inden for Azure AI Foundry giver Content Safety-tjenesten dig mulighed for at se, udforske og prøve eksempel-kode til at opdage skadeligt indhold på tværs af forskellige modaliteter. Følgende [kom-godt-i-gang dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) guider dig gennem at lave forespørgsler til tjenesten.

En anden vigtig faktor er den samlede ydeevne af applikationen. Med multimodale og multimodellerede applikationer betragter vi ydeevne som, at systemet fungerer som du og dine brugere forventer, inklusive ikke at generere skadelige output. Det er vigtigt at vurdere ydelsen for din samlede applikation ved hjælp af [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Du har også mulighed for at skabe og evaluere med [tilpassede evalueringer](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).
Du kan evaluere din AI-applikation i dit udviklingsmiljø ved hjælp af [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Givet enten et testdatasæt eller et mål, bliver dine generative AI-applikationsgenerationer kvantitativt målt med indbyggede evaluatorer eller brugerdefinerede evaluatorer efter eget valg. For at komme i gang med azure ai evaluation sdk for at evaluere dit system kan du følge [quickstart-guiden](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Når du har kørt en evalueringskørsel, kan du [visualisere resultaterne i Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## Varemærker

Dette projekt kan indeholde varemærker eller logoer for projekter, produkter eller tjenesteydelser. Autoriseret brug af Microsofts varemærker eller logoer er underlagt og skal følge [Microsofts retningslinjer for varemærker og brand](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Brug af Microsofts varemærker eller logoer i ændrede versioner af dette projekt må ikke skabe forvirring eller antyde Microsoft-sponsorering. Enhver brug af tredjepartsvaremærker eller logoer er underlagt disse tredjeparts politikker.

## Få hjælp

Hvis du sidder fast eller har spørgsmål om at bygge AI-apps, skal du deltage i:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Hvis du har produktfeedback eller fejl under udviklingen, besøg:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->