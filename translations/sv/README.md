# Phi Cookbook: Praktiska exempel med Microsofts Phi-modeller

[![Öppna och använd exemplen i GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Öppna i Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub-bidragsgivare](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub-ärenden](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub-pull-förfrågningar](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Välkomna](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub-övervakare](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub-förgreningar](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub-stjärnor](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi är en serie open source AI-modeller utvecklade av Microsoft.

Phi är för närvarande den mest kraftfulla och kostnadseffektiva lilla språkmodellen (SLM), med mycket bra prestanda i flerspråkiga, resonemangs-, text-/chattgenererings-, kodnings-, bild-, ljud- och andra scenarier.

Du kan distribuera Phi till molnet eller till edge-enheter, och du kan enkelt bygga generativa AI-applikationer med begränsad beräkningskraft.

Följ dessa steg för att komma igång med att använda dessa resurser:
1. **Fork:a repositoryt**: Klicka [![GitHub-förgreningar](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Klona repositoryt**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Gå med i Microsofts AI Discord-community och möt experter och andra utvecklare**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/sv/cover.eb18d1b9605d754b.webp)

### 🌐 Flerspråkigt stöd

#### Stöds via GitHub Action (Automatiserat & Alltid Uppdaterat)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabiska](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgariska](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Kinesiska (förenklad)](../zh-CN/README.md) | [Kinesiska (traditionell, Hong Kong)](../zh-HK/README.md) | [Kinesiska (traditionell, Macau)](../zh-MO/README.md) | [Kinesiska (traditionell, Taiwan)](../zh-TW/README.md) | [Kroatiska](../hr/README.md) | [Tjeckiska](../cs/README.md) | [Danska](../da/README.md) | [Nederländska](../nl/README.md) | [Estniska](../et/README.md) | [Finska](../fi/README.md) | [Franska](../fr/README.md) | [Tyska](../de/README.md) | [Grekiska](../el/README.md) | [Hebreiska](../he/README.md) | [Hindi](../hi/README.md) | [Ungerska](../hu/README.md) | [Indonesiska](../id/README.md) | [Italienska](../it/README.md) | [Japanska](../ja/README.md) | [Kannada](../kn/README.md) | [Koreanska](../ko/README.md) | [Litauiska](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalesiska](../ne/README.md) | [Nigeriansk Pidgin](../pcm/README.md) | [Norska](../no/README.md) | [Persiska (Farsi)](../fa/README.md) | [Polska](../pl/README.md) | [Portugisiska (Brasilien)](../pt-BR/README.md) | [Portugisiska (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumänska](../ro/README.md) | [Ryska](../ru/README.md) | [Serbiska (kyrilliska)](../sr/README.md) | [Slovakiska](../sk/README.md) | [Slovenska](../sl/README.md) | [Spanska](../es/README.md) | [Swahili](../sw/README.md) | [Svenska](./README.md) | [Tagalog (Filippinska)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thailändska](../th/README.md) | [Turkiska](../tr/README.md) | [Ukrainska](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamesiska](../vi/README.md)

> **Föredrar du att klona lokalt?**
>
> Detta repository innehåller över 50 språktranslationer vilket avsevärt ökar nedladdningsstorleken. För att klona utan översättningar, använd sparsamt checkout:
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
> Detta ger dig allt du behöver för att genomföra kursen med mycket snabbare nedladdning.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Innehållsförteckning
- Introduktion - [Välkommen till Phi-familjen](./md/01.Introduction/01/01.PhiFamily.md) - [Ställa in din miljö](./md/01.Introduction/01/01.EnvironmentSetup.md) - [Förstå viktiga teknologier](./md/01.Introduction/01/01.Understandingtech.md) - [AI-säkerhet för Phi-modeller](./md/01.Introduction/01/01.AISafety.md) - [Phi hårdvarustöd](./md/01.Introduction/01/01.Hardwaresupport.md) - [Phi-modeller & tillgänglighet över plattformar](./md/01.Introduction/01/01.Edgeandcloud.md) - [Använda Guidance-ai och Phi](./md/01.Introduction/01/01.Guidance.md) - [GitHub Marketplace Modeller](https://github.com/marketplace/models) - [Azure AI Model Catalog](https://ai.azure.com) - Inference Phi i olika miljöer - [Hugging face](./md/01.Introduction/02/01.HF.md) - [GitHub Modeller](./md/01.Introduction/02/02.GitHubModel.md) - [Microsoft Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md) - [Ollama](./md/01.Introduction/02/04.Ollama.md) - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md) - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md) - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md) - Inference Phi-familjen - [Inference Phi i iOS](./md/01.Introduction/03/iOS_Inference.md) - [Inference Phi i Android](./md/01.Introduction/03/Android_Inference.md) - [Inference Phi i Jetson](./md/01.Introduction/03/Jetson_Inference.md) - [Inference Phi i AI-PC](./md/01.Introduction/03/AIPC_Inference.md) - [Inference Phi med Apple MLX-ramverk](./md/01.Introduction/03/MLX_Inference.md) - [Inference Phi i lokala servrar](./md/01.Introduction/03/Local_Server_Inference.md) - [Inference Phi i fjärrserver med AI Toolkit](./md/01.Introduction/03/Remote_Interence.md) - [Inference Phi med Rust](./md/01.Introduction/03/Rust_Inference.md) - [Inference Phi--Vision lokalt](./md/01.Introduction/03/Vision_Inference.md) - [Inference Phi med Kaito AKS, Azure Containers (officiellt stöd)](./md/01.Introduction/03/Kaito_Inference.md) - [Kvantisering av Phi-familjen](./md/01.Introduction/04/QuantifyingPhi.md) - [Kvantisera Phi-3.5 / 4 med llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md) - [Kvantisera Phi-3.5 / 4 med Generative AI-utvidgningar för onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md) - [Kvantisera Phi-3.5 / 4 med Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md) - [Kvantisera Phi-3.5 / 4 med Apple MLX-ramverk](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md) - Utvärdering av Phi - [Ansvarsfull AI](./md/01.Introduction/05/ResponsibleAI.md) - [Microsoft Foundry för utvärdering](./md/01.Introduction/05/AIFoundry.md) - [Använda Promptflow för utvärdering](./md/01.Introduction/05/Promptflow.md) - RAG med Azure AI Search - [Hur man använder Phi-4-mini och Phi-4-multimodal (RAG) med Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb) - Phi applikationsutveckling exempel - Text & chattapplikationer - Phi-4 exempel - [📓] [Chatta med Phi-4-mini ONNX-modell](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md) - [Chatta med Phi-4 lokal ONNX-modell .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) - [Chatt .NET konsolapp med Phi-4 ONNX och Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) - Phi-3 / 3.5 exempel - [Lokal chatbot i webbläsaren med Phi3, ONNX Runtime Web och WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat) - [OpenVINO Chatt](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md) - [Multi Model - Interaktiv Phi-3-mini och OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md) - [MLFlow - Bygga ett wrapper och använda Phi-3 med MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md) - [Modelloptimering - Hur man optimerar Phi-3-minimodell för ONNX Runtime Web med Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3) - [WinUI3-app med Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/) - [WinUI3 Multi Model AI Powered Notes App-exempel](https://github.com/microsoft/ai-powered-notes-winui3-sample) - [Finjustera och integrera egna Phi-3-modeller med Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md) - [Finjustera och integrera egna Phi-3-modeller med Prompt flow i Microsoft Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md) - [Utvärdera den finjusterade Phi-3 / Phi-3.5 modellen i Microsoft Foundry med fokus på Microsofts principer för ansvarsfull AI](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md) - [📓] [Phi-3.5-mini-instruct språköversiktsexempel (kinesiska/engelska)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb) - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md) - [Använda Windows GPU för att skapa Prompt flow-lösning med Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md) - [Använda Microsoft Phi-3.5 tflite för att skapa Android-app](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md) - [Q&A .NET-exempel med lokal ONNX Phi-3-modell med Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301) - [Konsolchatt .NET-app med Semantic Kernel och Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302) - Azure AI Inference SDK kodbaserade exempel - Phi-4 exempel - [📓] [Generera projektkod med Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md) - Phi-3 / 3.5 exempel - [Bygg din egen Visual Studio Code GitHub Copilot Chat med Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md) - [Skapa din egen Visual Studio Code Chat Copilot-agent med Phi-3.5 via GitHub modeller](./md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md) - Avancerade resonemangsexempel - Phi-4 exempel - [📓] [Phi-4-mini-reasoning eller Phi-4-reasoning exempel](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md) - [📓] [Finjustera Phi-4-mini-reasoning med Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Finjustera Phi-4-mini-reasoning med Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Phi-4-mini-reasoning med GitHub-modeller](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb) - [📓] [Phi-4-mini-reasoning med Microsoft Foundry-modeller](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb) -
Demonstrationer - [Phi-4-mini demos hostade på Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo) - [Phi-4-multimodala demos hostade på Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo) - Exempel på vision - Phi-4 Exempel - [📓] [Använd Phi-4-multimodal för att läsa bilder och generera kod](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) - Phi-3 / 3.5 Exempel - [📓][Phi-3-vision-Bild text till text](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html) - [📓][Phi-3-vision CLIP Embeddding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/) - [Phi-3-vision - Visuell språkassistent - med Phi3-Vision och OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html) - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md) - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md) - [📓][Phi-3.5 Vision multi-frame eller multi-image exempel](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb) - [Phi-3 Vision Lokalt ONNX-modell med Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303) - [Menybaserat Phi-3 Vision Lokalt ONNX-modell med Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304) - Exempel på resonemang-vision - Phi-4-Reasoning-Vision-15B - [📓] [Använda Phi-4-Reasoning-Vision-15B för att upptäcka olaglig gatukorsning](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb) - [📓] [Använda Phi-4-Reasoning-Vision-15B för matematik](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb) - [📓] [Använda Phi-4-Reasoning-Vision-15B för att upptäcka UI](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb) - Matematikexempel - Phi-4-Mini-Flash-Reasoning-Instruct Exempel [Matematikdemo med Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb) - Ljudexempel - Phi-4 Exempel - [📓] [Extrahera ljudtranskript med Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md) - [📓] [Phi-4-multimodal ljudexempel](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb) - [📓] [Phi-4-multimodal talöversättningsexempel](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb) - [.NET konsolapplikation som använder Phi-4-multimodal ljud för att analysera en ljudfil och generera transkript](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) - MOE-exempel - Phi-3 / 3.5 Exempel - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) Social Media Exempel](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb) - [📓] [Bygga en Retrieval-Augmented Generation (RAG) Pipeline med NVIDIA NIM Phi-3 MOE, Azure AI Search och LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb) - Funktionanrops-exempel - Phi-4 Exempel 🆕 - [📓] [Använda Funktionanrop med Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md) - [📓] [Använda Funktionanrop för att skapa multi-agenter med Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb) - [📓] [Använda Funktionanrop med Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb) - [📓] [Använda Funktionanrop med ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb) - Multimodala blandningsexempel - Phi-4 Exempel 🆕 - [📓] [Använda Phi-4-multimodal som en teknikjournalist](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb) - [.NET konsolapplikation som använder Phi-4-multimodal för att analysera bilder](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) - Fine-tuning Phi Exempel - [Finjusteringsscenarier](./md/03.FineTuning/FineTuning_Scenarios.md) - [Finjustering vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md) - [Finjustera Låt Phi-3 bli en industriexpert](./md/03.FineTuning/LetPhi3gotoIndustriy.md) - [Finjustera Phi-3 med AI Toolkit för VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md) - [Finjustera Phi-3 med Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md) - [Finjustera Phi-3 med Lora](./md/03.FineTuning/FineTuning_Lora.md) - [Finjustera Phi-3 med QLora](./md/03.FineTuning/FineTuning_Qlora.md) - [Finjustera Phi-3 med Microsoft Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md) - [Finjustera Phi-3 med Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md) - [Finjustera med Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md) - [Finjustera med Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md) - [Finjustera Phi-3-vision med Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md) - [Finjustera Phi-3 med Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md) - [Finjustera Phi-3-vision (officiellt stöd)](./md/03.FineTuning/FineTuning_Vision.md) - [Finjustering av Phi-3 med Kaito AKS, Azure Containers (officiellt stöd)](./md/03.FineTuning/FineTuning_Kaito.md) - [Finjustering av Phi-3 och 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune) - Hands on Lab - [Utforska banbrytande modeller: LLMs, SLMs, lokal utveckling och mer](https://github.com/microsoft/aitour-exploring-cutting-edge-models) - [Frigöra NLP Potential: Finjustering med Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop) - Akademiska forskningsartiklar och publikationer - [Textbooks Are All You Need II: phi-1.5 teknisk rapport](https://arxiv.org/abs/2309.05463) - [Phi-3 Teknisk Rapport: En mycket kapabel språkmodell lokalt på din telefon](https://arxiv.org/abs/2404.14219) - [Phi-4 Teknisk Rapport](https://arxiv.org/abs/2412.08905) - [Phi-4-Mini Teknisk Rapport: Kompakt men kraftfull multimodal språkmodell via Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743) - [Optimering av små språkmodeller för fordonsfunktion-anrop](https://arxiv.org/abs/2501.02342) - [(WhyPHI) Finjustering av PHI-3 för flervalsfrågor: Metodik, resultat och utmaningar](https://arxiv.org/abs/2501.01588) - [Phi-4-resonemang Teknisk Rapport](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-resonerings teknisk rapport](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)
# Phi Cookbook: Praktiska exempel med Microsofts Phi-modeller

[![Öppna och använd exemplen i GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Öppna i Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Öppna&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub bidragsgivare](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Välkomna](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stjärnor](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi är en serie med öppen källkod AI-modeller utvecklade av Microsoft.

Phi är för närvarande den mest kraftfulla och kostnadseffektiva lilla språkmodellen (SLM), med mycket bra prestanda inom flera språk, resonemang, text-/chattgenerering, kodning, bilder, ljud och andra scenarier.

Du kan distribuera Phi till molnet eller till edge-enheter, och du kan enkelt bygga generativa AI-applikationer med begränsad beräkningskraft.

Följ dessa steg för att börja använda dessa resurser:
1. **Gaffla arkivet:** Klicka [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Klona arkivet:** `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Gå med i Microsoft AI Discord Community och träffa experter och andra utvecklare**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/sv/cover.eb18d1b9605d754b.webp)

### 🌐 Stöd för flera språk

#### Stöds via GitHub Action (Automatiserat & Alltid uppdaterat)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabiska](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgariska](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Kinesiska (förenklad)](../zh-CN/README.md) | [Kinesiska (traditionell, Hong Kong)](../zh-HK/README.md) | [Kinesiska (traditionell, Macau)](../zh-MO/README.md) | [Kinesiska (traditionell, Taiwan)](../zh-TW/README.md) | [Kroatiska](../hr/README.md) | [Tjeckiska](../cs/README.md) | [Danska](../da/README.md) | [Nederländska](../nl/README.md) | [Estniska](../et/README.md) | [Finska](../fi/README.md) | [Franska](../fr/README.md) | [Tyska](../de/README.md) | [Grekiska](../el/README.md) | [Hebreiska](../he/README.md) | [Hindi](../hi/README.md) | [Ungerska](../hu/README.md) | [Indonesiska](../id/README.md) | [Italienska](../it/README.md) | [Japanska](../ja/README.md) | [Kannada](../kn/README.md) | [Koreanska](../ko/README.md) | [Litauiska](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigeriansk Pidgin](../pcm/README.md) | [Norska](../no/README.md) | [Persiska (Farsi)](../fa/README.md) | [Polska](../pl/README.md) | [Portugisiska (Brasilien)](../pt-BR/README.md) | [Portugisiska (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumänska](../ro/README.md) | [Ryska](../ru/README.md) | [Serbiska (kyrilliska)](../sr/README.md) | [Slovakiska](../sk/README.md) | [Slovenska](../sl/README.md) | [Spanska](../es/README.md) | [Swahili](../sw/README.md) | [Svenska](./README.md) | [Tagalog (Filippinska)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thailändska](../th/README.md) | [Turkiska](../tr/README.md) | [Ukrainska](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamesiska](../vi/README.md)

> **Föredrar du att klona lokalt?**
>
> Detta arkiv innehåller över 50 språköversättningar vilket avsevärt ökar nedladdningsstorleken. För att klona utan översättningar, använd sparse checkout:
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
> Detta ger dig allt du behöver för att slutföra kursen med en mycket snabbare nedladdning.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Innehållsförteckning

## Att använda Phi-modeller

### Phi på Microsoft Foundry

Du kan lära dig hur du använder Microsoft Phi och hur du bygger E2E-lösningar på dina olika hårdvaruenheter. För att själv uppleva Phi, börja med att leka med modellerna och anpassa Phi för dina scenarier med hjälp av [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Du kan lära dig mer under Kom igång med [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Testmiljö**
Varje modell har en dedikerad testmiljö för att prova modellen [Azure AI Playground](https://aka.ms/try-phi3).

### Phi på GitHub Models

Du kan lära dig hur du använder Microsoft Phi och hur du bygger E2E-lösningar på dina olika hårdvaruenheter. För att själv uppleva Phi, börja med att leka med modellen och anpassa Phi för dina scenarier genom att använda [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Du kan lära dig mer under Kom igång med [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Testmiljö**
Varje modell har en dedikerad [testmiljö för att prova modellen](/md/02.QuickStart/GitHubModel_QuickStart.md).

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
[![LangChain för nybörjare](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agenter
[![AZD för nybörjare](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI för nybörjare](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP för nybörjare](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agenter för nybörjare](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generativ AI-serie
[![Generativ AI för nybörjare](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Kärninlärning
[![ML för nybörjare](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Datavetenskap för nybörjare](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI för nybörjare](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersäkerhet för nybörjare](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webbutveckling för nybörjare](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT för nybörjare](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR-utveckling för nybörjare](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot-serien
[![Copilot för AI samprogrammering](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot för C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot-äventyr](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Ansvarsfull AI

Microsoft är engagerade i att hjälpa våra kunder att använda våra AI-produkter ansvarsfullt, dela våra erfarenheter och bygga förtroendebaserade partnerskap genom verktyg som Transparency Notes och Impact Assessments. Många av dessa resurser finns på [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofts syn på ansvarsfull AI grundar sig i våra AI-principer om rättvisa, pålitlighet och säkerhet, integritet och säkerhet, inkludering, transparens och ansvarstagande.

Storskaliga modeller för naturligt språk, bild och tal – som de som används i detta exempel – kan potentiellt bete sig på sätt som är orättvisa, opålitliga eller stötande, vilket i sin tur kan orsaka skada. Vänligen konsultera [Azure OpenAI-tjänstens Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) för att få information om risker och begränsningar.

Den rekommenderade metoden för att mildra dessa risker är att inkludera ett säkerhetssystem i din arkitektur som kan detektera och förhindra skadligt beteende. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ger ett självständigt skyddslager som kan upptäcka skadligt användargenererat och AI-genererat innehåll i applikationer och tjänster. Azure AI Content Safety inkluderar text- och bild-API:er som låter dig upptäcka material som är skadligt. Inom Microsoft Foundry tillåter Content Safety-tjänsten dig att visa, utforska och testa exempel på kod för att upptäcka skadligt innehåll över olika modaliteter. Följande [quickstart-dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) guidar dig genom hur du skickar förfrågningar till tjänsten.

En annan aspekt att ta hänsyn till är den övergripande prestandan i applikationen. Med multimodala och multimodellsapplikationer menar vi med prestanda att systemet fungerar som du och dina användare förväntar sig, inklusive att inte generera skadliga resultat. Det är viktigt att utvärdera prestandan i din övergripande applikation med hjälp av [Performance and Quality och Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Du har också möjligheten att skapa och utvärdera med [anpassade evaluatorer](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Du kan utvärdera din AI-applikation i din utvecklingsmiljö med hjälp av [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Med antingen en testdataset eller ett mål, mäts dina generativa AI-applikationsgenereringar kvantitativt med inbyggda evaluatorer eller valfria anpassade evaluatorer. För att komma igång med Azure AI Evaluation SDK för att utvärdera ditt system kan du följa [quickstart-guiden](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). När du har kört en utvärderingskörning kan du [visualisera resultaten i Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Varumärken

Detta projekt kan innehålla varumärken eller logotyper för projekt, produkter eller tjänster. Auktoriserad användning av Microsofts varumärken eller logotyper är föremål för och måste följa [Microsofts riktlinjer för varumärken och varumärkesbruk](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Användning av Microsofts varumärken eller logotyper i modifierade versioner av detta projekt får inte orsaka förvirring eller antyda Microsoft-sponsring. All användning av tredjeparts varumärken eller logotyper är föremål för dessa tredjeparts riktlinjer.

## Få hjälp

Om du fastnar eller har frågor om att skapa AI-appar, gå med i:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Om du har produktfeedback eller fel under skapandet, besök:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->