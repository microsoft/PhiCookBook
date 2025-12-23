<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef3a50368712b1a7483d0def1f70c490",
  "translation_date": "2025-12-21T11:59:13+00:00",
  "source_file": "README.md",
  "language_code": "sv"
}
-->
# Phi Cookbook: Praktiska exempel med Microsofts Phi-modeller

[![Öppna och använd exemplen i GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Öppna i Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub-bidragsgivare](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub-ärenden](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-förfrågningar](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs välkomna](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub-bevakare](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub-forkar](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub-stjärnor](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi är en serie öppna AI-modeller utvecklade av Microsoft. 

Phi är för närvarande den mest kraftfulla och kostnadseffektiva lilla språkmodellen (SLM), med mycket bra benchmarkresultat inom flerspråkighet, resonemang, text-/chattgenerering, kodning, bilder, ljud och andra scenarier. 

Du kan distribuera Phi till molnet eller till edge-enheter, och du kan enkelt bygga generativa AI-applikationer med begränsad beräkningskapacitet.

Följ dessa steg för att komma igång med dessa resurser:
1. **Forka förvaret**: Click [![GitHub-forkar](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Klona förvaret**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Gå med i Microsoft AI Discord-gemenskapen och träffa experter och andra utvecklare**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![omslag](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.sv.png)

### 🌐 Flerspråkigt stöd

#### Stöds via GitHub Action (Automatiserat & alltid uppdaterat)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabiska](../ar/README.md) | [Bengalska](../bn/README.md) | [Bulgariska](../bg/README.md) | [Burmesiska (Myanmar)](../my/README.md) | [Kinesiska (förenklad)](../zh/README.md) | [Kinesiska (traditionell, Hongkong)](../hk/README.md) | [Kinesiska (traditionell, Macau)](../mo/README.md) | [Kinesiska (traditionell, Taiwan)](../tw/README.md) | [Kroatiska](../hr/README.md) | [Tjeckiska](../cs/README.md) | [Danska](../da/README.md) | [Nederländska](../nl/README.md) | [Estniska](../et/README.md) | [Finska](../fi/README.md) | [Franska](../fr/README.md) | [Tyska](../de/README.md) | [Grekiska](../el/README.md) | [Hebreiska](../he/README.md) | [Hindi](../hi/README.md) | [Ungerska](../hu/README.md) | [Indonesiska](../id/README.md) | [Italienska](../it/README.md) | [Japanska](../ja/README.md) | [Kannada](../kn/README.md) | [Koreanska](../ko/README.md) | [Litauiska](../lt/README.md) | [Malajiska](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalesiska](../ne/README.md) | [Nigeriansk Pidgin](../pcm/README.md) | [Norska](../no/README.md) | [Persiska (Farsi)](../fa/README.md) | [Polska](../pl/README.md) | [Portugisiska (Brasilien)](../br/README.md) | [Portugisiska (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumänska](../ro/README.md) | [Ryska](../ru/README.md) | [Serbiska (kyrilliska)](../sr/README.md) | [Slovakiska](../sk/README.md) | [Slovenska](../sl/README.md) | [Spanska](../es/README.md) | [Swahili](../sw/README.md) | [Svenska](./README.md) | [Tagalog (filippinska)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thailändska](../th/README.md) | [Turkiska](../tr/README.md) | [Ukrainska](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamesiska](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Innehållsförteckning

- Introduktion
  - [Välkommen till Phi-familjen](./md/01.Introduction/01/01.PhiFamily.md)
  - [Konfigurera din miljö](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Förstå viktiga teknologier](./md/01.Introduction/01/01.Understandingtech.md)
  - [AI-säkerhet för Phi-modeller](./md/01.Introduction/01/01.AISafety.md)
  - [Phi hårdvarustöd](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi-modeller och tillgänglighet över plattformar](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Använda Guidance-ai och Phi](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace-modeller](https://github.com/marketplace/models)
  - [Azure AI-modellkatalog](https://ai.azure.com)

- Inferens av Phi i olika miljöer
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub-modeller](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry modellkatalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Inferens för Phi-familjen
    - [Inferens av Phi på iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inferens av Phi på Android](./md/01.Introduction/03/Android_Inference.md)
    - [Inferens av Phi på Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inferens av Phi på AI-PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inferens av Phi med Apple MLX-ramverket](./md/01.Introduction/03/MLX_Inference.md)
    - [Inferens av Phi på lokal server](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inferens av Phi på fjärrserver med AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inferens av Phi med Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inferens av Phi – Vision lokalt](./md/01.Introduction/03/Vision_Inference.md)
    - [Inferens av Phi med Kaito AKS, Azure Containers (officiellt stöd)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Kvantisering av Phi-familjen](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Kvantisering av Phi-3.5 / 4 med llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Kvantisering av Phi-3.5 / 4 med Generative AI extensions för onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Kvantisering av Phi-3.5 / 4 med Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Kvantisering av Phi-3.5 / 4 med Apple MLX-ramverket](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Utvärdering av Phi
    - [Ansvarsfull AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry för utvärdering](./md/01.Introduction/05/AIFoundry.md)
    - [Använda Promptflow för utvärdering](./md/01.Introduction/05/Promptflow.md)
 
- RAG med Azure AI Search
    - [Hur man använder Phi-4-mini och Phi-4-multimodal(RAG) med Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Exempel på Phi-applikationsutveckling
  - Text- och chattapplikationer
    - Phi-4-exempel 🆕
      - [📓] [Chatta med Phi-4-mini ONNX-modellen](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chatt med Phi-4 lokal ONNX-modell (.NET)](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Chatt .NET-konsolapp med Phi-4 ONNX med Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5-exempel
      - [Lokal chatbot i webbläsaren med Phi3, ONNX Runtime Web och WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino-chatt](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Flermodell - Interaktiv Phi-3-mini och OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Bygga en wrapper och använda Phi-3 med MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Modelloptimering - Hur man optimerar Phi-3-min-modellen för ONNX Runtime Web med Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3-app med Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3-exempel på AI-driven anteckningsapp med flera modeller](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Finjustera och integrera anpassade Phi-3-modeller med Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Finjustera och integrera anpassade Phi-3-modeller med Prompt flow i Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Utvärdera den finjusterade Phi-3 / Phi-3.5-modellen i Azure AI Foundry med fokus på Microsofts principer för ansvarsfull AI](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct exempel på språkprediktion (kinesiska/engelska)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG-chattbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Använda Windows GPU för att skapa Prompt flow-lösning med Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Använda Microsoft Phi-3.5 tflite för att skapa Android-app](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET-exempel som använder lokal ONNX Phi-3-modell med Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Konsolchatt .NET-app med Semantic Kernel och Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK kodbaserade exempel 
    - Phi-4-exempel 🆕
      - [📓] [Generera projektkod med Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5-exempel
      - [Bygg din egen Visual Studio Code GitHub Copilot-chatt med Microsoft Phi-3-familjen](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Skapa din egen Visual Studio Code Chat Copilot-agent med Phi-3.5 från GitHub Models](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Avancerade resonemangsexempel
    - Phi-4-exempel 🆕
      - [📓] [Phi-4-mini-reasoning eller Phi-4-reasoning-exempel](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Finjustera Phi-4-mini-reasoning med Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Finjustera Phi-4-mini-reasoning med Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning med GitHub Models](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-reasoning med Azure AI Foundry-modeller](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demoer
      - [Phi-4-mini-demoer värd på Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demoer värd på Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Vision-exempel
    - Phi-4-exempel 🆕
      - [📓] [Använd Phi-4-multimodal för att läsa bilder och generera kod](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5-exempel
      -  [📓][Phi-3-vision-Bildtext till text](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP-inbäddning](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3-återvinning](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Visuell språkassistent - med Phi3-Vision och OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision exempel med flera ramar eller flera bilder](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision lokal ONNX-modell som använder Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menybaserad Phi-3 Vision lokal ONNX-modell som använder Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Matematikexempel
    -  Phi-4-Mini-Flash-Reasoning-Instruct-exempel 🆕 [Matematikdemo med Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - Ljudexempel
    - Phi-4-exempel 🆕
      - [📓] [Extrahera ljudutskrifter med Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal ljudexempel](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal exempel på talsöversättning](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET-konsolapplikation som använder Phi-4-multimodal Audio för att analysera en ljudfil och generera transkript](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE-exempel
    - Phi-3 / 3.5-exempel
      - [📓] [Phi-3.5 Mixture of Experts-modeller (MoEs) exempel för sociala medier](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Bygga en Retrieval-Augmented Generation (RAG)-pipeline med NVIDIA NIM Phi-3 MOE, Azure AI Search, och LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Function Calling-exempel
    - Phi-4-exempel 🆕
      -  [📓] [Använda Function Calling med Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Använda Function Calling för att skapa multi-agenter med Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Använda Function Calling med Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Använda Function Calling med ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling_ipynb)
  - Multimodala blandningsexempel
    - Phi-4-exempel 🆕
      -  [📓] [Använda Phi-4-multimodal som teknikjournalist](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET-konsolapplikation som använder Phi-4-multimodal för att analysera bilder](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Finjustering av Phi-exempel
  - [Finjusteringsscenarier](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Finjustering vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Finjustering: Låt Phi-3 bli en branschexpert](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Finjustera Phi-3 med AI Toolkit för VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Finjustera Phi-3 med Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Finjustera Phi-3 med Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Finjustera Phi-3 med QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Finjustera Phi-3 med Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Finjustera Phi-3 med Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Finjustering med Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Finjustering med Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Finjustera Phi-3-vision med Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Finjustera Phi-3 med Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Finjustera Phi-3-vision (officiellt stöd)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Finjustera Phi-3 med Kaito AKS , Azure Containers(officiellt stöd)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Finjustera Phi-3 och 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Praktiska labb
  - [Utforska banbrytande modeller: LLMs, SLMs, lokal utveckling och mer](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Frigöra NLP-potential: Finjustering med Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Akademiska forskningsartiklar och publikationer
  - [Textbooks Are All You Need II: phi-1.5 teknisk rapport](https://arxiv.org/abs/2309.05463)
  - [Phi-3 teknisk rapport: En mycket kapabel språkmodell lokalt på din telefon](https://arxiv.org/abs/2404.14219)
  - [Phi-4 teknisk rapport](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Teknisk rapport: Kompakta men kraftfulla multimodala språkmodeller via Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Optimera små språkmodeller för funktionsanrop i fordon](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Finjustering av PHI-3 för flervalsfrågesvar: Metodik, resultat och utmaningar](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning Teknisk rapport](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning Teknisk rapport](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Använda Phi-modeller

### Phi på Azure AI Foundry

Du kan lära dig hur du använder Microsoft Phi och hur du bygger E2E-lösningar på dina olika hårdvaruenheter. För att uppleva Phi själv, börja med att testa modellerna och anpassa Phi för dina scenarier med hjälp av [Azure AI Foundry Azure AI Modellkatalog](https://aka.ms/phi3-azure-ai) du kan lära dig mer i Komma igång med [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Testmiljö**
Varje modell har en dedikerad testmiljö för att testa modellen [Azure AI Playground](https://aka.ms/try-phi3).

### Phi på GitHub-modeller

Du kan lära dig hur du använder Microsoft Phi och hur du bygger E2E-lösningar på dina olika hårdvaruenheter. För att uppleva Phi själv, börja med att testa modellen och anpassa Phi för dina scenarier med hjälp av [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) du kan lära dig mer i Komma igång med [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Testmiljö**
Varje modell har en dedikerad [testmiljö för att testa modellen](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi på Hugging Face

Du kan också hitta modellen på [Hugging Face](https://huggingface.co/microsoft)

**Testmiljö**
 [Hugging Chat testmiljö](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 Andra kurser

Vårt team producerar andra kurser! Kolla in:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j för nybörjare](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js för nybörjare](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agenter
[![AZD för nybörjare](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI för nybörjare](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP för nybörjare](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI-agenter för nybörjare](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generativ AI-serie
[![Generativ AI för nybörjare](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Grundläggande lärande
[![ML för nybörjare](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science för nybörjare](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI för nybörjare](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersäkerhet för nybörjare](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webbutveckling för nybörjare](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT för nybörjare](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR-utveckling för nybörjare](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot-serien
[![Copilot för AI-assisterad parprogrammering](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot för C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot-äventyr](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Ansvarsfull AI 

Microsoft är engagerat i att hjälpa våra kunder att använda våra AI-produkter ansvarsfullt, dela våra erfarenheter och bygga förtroendebaserade partnerskap genom verktyg som Transparency Notes och Impact Assessments. Många av dessa resurser finns på [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofts syn på ansvarsfull AI är grundad i våra AI-principer om rättvisa, tillförlitlighet och säkerhet, integritet och säkerhet, inkludering, transparens och ansvarsskyldighet.

Storskaliga modeller för naturligt språk, bild och tal - som de som används i det här exemplet - kan potentiellt uppträda på sätt som är orättvisa, opålitliga eller stötande, vilket i sin tur kan orsaka skada. Var vänlig konsultera [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) för att bli informerad om risker och begränsningar.

Den rekommenderade metoden för att mildra dessa risker är att inkludera ett säkerhetssystem i din arkitektur som kan upptäcka och förhindra skadligt beteende. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) tillhandahåller ett oberoende skyddsskikt som kan upptäcka skadligt användargenererat och AI-genererat innehåll i applikationer och tjänster. Azure AI Content Safety inkluderar text- och bild-API:er som låter dig upptäcka material som är skadligt. Inom Azure AI Foundry tillåter Content Safety-tjänsten att du kan visa, utforska och prova exempel på kod för att upptäcka skadligt innehåll över olika modaliteter. Följande [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) guidar dig genom att göra förfrågningar till tjänsten.

En annan aspekt att beakta är den övergripande applikationsprestandan. För multimodala och multimodellsapplikationer anser vi att prestanda innebär att systemet fungerar som du och dina användare förväntar sig, inklusive att inte generera skadliga utskrifter. Det är viktigt att utvärdera prestandan för din övergripande applikation med hjälp av [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Du har också möjlighet att skapa och utvärdera med [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Du kan utvärdera din AI-applikation i din utvecklingsmiljö med hjälp av [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Givet antingen en testdataset eller ett mål, mäts din generativa AI-applikations genereringar kvantitativt med inbyggda evaluatorer eller anpassade evaluatorer efter ditt val. För att komma igång med azure ai evaluation sdk för att utvärdera ditt system kan du följa [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). När du har kört en utvärdering kan du [visualisera resultaten i Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## Varumärken
Detta projekt kan innehålla varumärken eller logotyper för projekt, produkter eller tjänster. Auktoriserad användning av Microsofts varumärken eller logotyper är föremål för och måste följa [Microsofts riktlinjer för varumärken och varumärkesprofil](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Användning av Microsofts varumärken eller logotyper i modifierade versioner av detta projekt får inte orsaka förvirring eller antyda Microsofts sponsring. All användning av tredjeparts varumärken eller logotyper omfattas av respektive tredjeparts policyer.

## Få hjälp

Om du kör fast eller har frågor om att bygga AI-appar, gå med i:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Om du har produktfeedback eller stöter på fel när du bygger, besök:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell, mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->