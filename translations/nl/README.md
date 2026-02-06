# Phi Kookboek: Praktische Voorbeelden met Microsoft's Phi Modellen

[![Open en gebruik de voorbeelden in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub bijdragers](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-verzoeken](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welkom](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub volgers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub sterren](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi is een reeks open source AI-modellen ontwikkeld door Microsoft.

Phi is momenteel het krachtigste en meest kosteneffectieve kleine taalmodel (SLM), met zeer goede benchmarks in meertaligheid, redeneren, tekst/chat generatie, coderen, beelden, audio en andere scenario's.

Je kunt Phi implementeren in de cloud of op edge-apparaten, en je kunt eenvoudig generatieve AI-toepassingen bouwen met beperkte rekenkracht.

Volg deze stappen om te beginnen met het gebruik van deze resources:
1. **Fork de Repository**: Klik op [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Clone de Repository**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Word lid van de Microsoft AI Discord Community en ontmoet experts en mede-ontwikkelaars**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/nl/cover.eb18d1b9605d754b.webp)

### 🌐 Ondersteuning voor meerdere talen

#### Ondersteund via GitHub Action (Geautomatiseerd & Altijd Up-to-Date)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabisch](../ar/README.md) | [Bengaals](../bn/README.md) | [Bulgaars](../bg/README.md) | [Birmaans (Myanmar)](../my/README.md) | [Chinees (Vereenvoudigd)](../zh-CN/README.md) | [Chinees (Traditioneel, Hong Kong)](../zh-HK/README.md) | [Chinees (Traditioneel, Macau)](../zh-MO/README.md) | [Chinees (Traditioneel, Taiwan)](../zh-TW/README.md) | [Kroatisch](../hr/README.md) | [Tsjechisch](../cs/README.md) | [Deens](../da/README.md) | [Nederlands](./README.md) | [Estisch](../et/README.md) | [Fins](../fi/README.md) | [Frans](../fr/README.md) | [Duits](../de/README.md) | [Grieks](../el/README.md) | [Hebreeuws](../he/README.md) | [Hindi](../hi/README.md) | [Hongaars](../hu/README.md) | [Indonesisch](../id/README.md) | [Italiaans](../it/README.md) | [Japans](../ja/README.md) | [Kannada](../kn/README.md) | [Koreaans](../ko/README.md) | [Litouws](../lt/README.md) | [Maleis](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalees](../ne/README.md) | [Nigeriaans Pidgin](../pcm/README.md) | [Noors](../no/README.md) | [Perzisch (Farsi)](../fa/README.md) | [Pools](../pl/README.md) | [Portugees (Brazilië)](../pt-BR/README.md) | [Portugees (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Roemeens](../ro/README.md) | [Russisch](../ru/README.md) | [Servisch (Cyrillisch)](../sr/README.md) | [Slowaaks](../sk/README.md) | [Sloveens](../sl/README.md) | [Spaans](../es/README.md) | [Swahili](../sw/README.md) | [Zweeds](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turks](../tr/README.md) | [Oekraïens](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamees](../vi/README.md)

> **Liever lokaal clonen?**

> Deze repository bevat meer dan 50 taalvertalingen wat de downloadgrootte aanzienlijk vergroot. Om te clonen zonder vertalingen, gebruik sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Dit geeft je alles wat je nodig hebt om de cursus te voltooien met een veel snellere download.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Inhoudsopgave

- Introductie
  - [Welkom bij de Phi Familie](./md/01.Introduction/01/01.PhiFamily.md)
  - [Je omgeving opzetten](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Belangrijke technologieën begrijpen](./md/01.Introduction/01/01.Understandingtech.md)
  - [AI Veiligheid voor Phi Modellen](./md/01.Introduction/01/01.AISafety.md)
  - [Phi Hardware Ondersteuning](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi Modellen & Beschikbaarheid op verschillende platforms](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Gebruik van Guidance-ai en Phi](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace Modellen](https://github.com/marketplace/models)
  - [Azure AI Model Catalogus](https://ai.azure.com)

- Inference Phi in verschillende omgevingen
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub Modellen](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry Model Catalogus](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolbox VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Lokaal](./md/01.Introduction/02/07.FoundryLocal.md)

- Inference Phi Familie
    - [Inference Phi op iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inference Phi op Android](./md/01.Introduction/03/Android_Inference.md)
    - [Inference Phi op Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inference Phi op AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inference Phi met Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Inference Phi op Lokale Server](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inference Phi op Afstand Server met AI Toolbox](./md/01.Introduction/03/Remote_Interence.md)
    - [Inference Phi met Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inference Phi--Visie lokaal](./md/01.Introduction/03/Vision_Inference.md)
    - [Inference Phi met Kaito AKS, Azure Containers (officiële ondersteuning)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Quantificeren van Phi Familie](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Quantificeren van Phi-3.5 / 4 met llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Quantificeren van Phi-3.5 / 4 met Generative AI extensies voor onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Quantificeren van Phi-3.5 / 4 met Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Quantificeren van Phi-3.5 / 4 met Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Evaluatie Phi
    - [Verantwoordelijke AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry voor Evaluatie](./md/01.Introduction/05/AIFoundry.md)
    - [Gebruik van Promptflow voor Evaluatie](./md/01.Introduction/05/Promptflow.md)
 
- RAG met Azure AI Search
    - [Hoe Phi-4-mini en Phi-4-multimodal (RAG) gebruiken met Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi applicatie ontwikkelingsvoorbeelden
  - Tekst & Chat Applicaties
    - Phi-4 Voorbeelden 🆕
      - [📓] [Chat met Phi-4-mini ONNX Model](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat met Phi-4 lokaal ONNX Model .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Chat .NET Console App met Phi-4 ONNX met gebruik van Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 Voorbeelden
      - [Lokale Chatbot in de browser met Phi3, ONNX Runtime Web en WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - Interactieve Phi-3-mini en OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Een wrapper bouwen en Phi-3 gebruiken met MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Modeloptimalisatie - Hoe het Phi-3-min model te optimaliseren voor ONNX Runtime Web met Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3-app met Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 Multi Model AI aangedreven Notities App Voorbeeld](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Fijn afstemmen en integreren van aangepaste Phi-3 modellen met Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Fijn afstemmen en integreren van aangepaste Phi-3 modellen met Prompt flow in Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Evalueer het fijn afgestemde Phi-3 / Phi-3.5 Model in Azure AI Foundry met focus op Microsoft's Principes voor Verantwoordelijke AI](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct taalvoorspellingsvoorbeeld (Chinees/Engels)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU gebruiken om Prompt flow oplossing te maken met Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite gebruiken om Android app te maken](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET Voorbeeld met lokaal ONNX Phi-3 model met Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Console chat .NET app met Semantic Kernel en Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK Code-gebaseerde Voorbeelden 
    - Phi-4 Voorbeelden 🆕
      - [📓] [Projectcode genereren met Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 Voorbeelden
      - [Bouw je eigen Visual Studio Code GitHub Copilot Chat met Microsoft Phi-3 Familielijn](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Maak je eigen Visual Studio Code Chat Copilot Agent met Phi-3.5 door GitHub Modellen](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Geavanceerde Redenering Voorbeelden
    - Phi-4 Voorbeelden 🆕
      - [📓] [Phi-4-mini-redenering of Phi-4-redenering Voorbeelden](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Fijn afstemmen Phi-4-mini-redenering met Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Fijn afstemmen Phi-4-mini-redenering met Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-redenering met GitHub Modellen](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-redenering met Azure AI Foundry Modellen](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demo's
      - [Phi-4-mini demo's gehost op Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demo's gehost op Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Visie Voorbeelden
    - Phi-4 Voorbeelden 🆕
      - [📓] [Gebruik Phi-4-multimodal om afbeeldingen te lezen en code te genereren](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 Voorbeelden
      -  [📓][Phi-3-vision-Afbeelding-tekst naar tekst](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Visuele taalassistent - met Phi3-Vision en OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Visie Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Visie OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Visie multi-frame of multi-afbeelding voorbeeld](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Visie Lokaal ONNX Model met Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menu-gebaseerd Phi-3 Visie Lokaal ONNX Model met Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Wiskunde Voorbeelden
    -  Phi-4-Mini-Flash-Reasoning-Instruct Voorbeelden 🆕 [Wiskunde Demo met Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - Audio Voorbeelden
    - Phi-4 Voorbeelden 🆕
      - [📓] [Audio transcripties extraheren met Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal Audio Voorbeeld](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal Spraakvertaling Voorbeeld](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET console applicatie die Phi-4-multimodal Audio gebruikt om een audiobestand te analyseren en transcript te genereren](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE Voorbeelden
    - Phi-3 / 3.5 Voorbeelden
      - [📓] [Phi-3.5 Mixture of Experts Modellen (MoEs) Social Media Voorbeeld](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Een Retrieval-Augmented Generation (RAG) Pipeline bouwen met NVIDIA NIM Phi-3 MOE, Azure AI Search, en LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Function Calling Voorbeelden
    - Phi-4 Voorbeelden 🆕
      -  [📓] [Function Calling gebruiken met Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Function Calling gebruiken om multi-agents te creëren met Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Function Calling gebruiken met Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Function Calling gebruiken met ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Multimodale Mix Voorbeelden
    - Phi-4 Voorbeelden 🆕
      -  [📓] [Phi-4-multimodal gebruiken als technologiejournalist](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET console applicatie die Phi-4-multimodal gebruikt om afbeeldingen te analyseren](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Fijn-afstemming Phi Voorbeelden
  - [Fijn-afstemmingsscenario's](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Fijn-afstemming versus RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Fijn-afstemming Laat Phi-3 een industrie-expert worden](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Fijn-afstemming Phi-3 met AI Toolkit voor VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Fijn-afstemming Phi-3 met Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Fijn-afstemming Phi-3 met Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Fijn-afstemming Phi-3 met QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Fijn-afstemming Phi-3 met Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Fijn-afstemming Phi-3 met Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Fijn-afstemming met Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Fijn-afstemming met Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Fijn-afstemming Phi-3-visie met Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Fijn-afstemming Phi-3 met Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Fijn-afstemming Phi-3-visie (officiële ondersteuning)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Fijn-afstemming Phi-3 met Kaito AKS, Azure Containers (officiële ondersteuning)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Fijn-afstemming Phi-3 en 3.5 Visie](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands-on Lab
  - [Ontdek baanbrekende modellen: LLM's, SLM's, lokale ontwikkeling en meer](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Ontgrendel NLP Potentieel: Fijn-afstemming met Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Academische Onderzoeksartikelen en Publicaties
  - [Leerboeken zijn alles wat je nodig hebt II: phi-1.5 technisch rapport](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Technisch Rapport: een krachtig taalmodel lokaal op je telefoon](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Technisch Rapport](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Technisch Rapport: compacte maar krachtige multimodale taalmodellen via Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Optimalisatie van kleine taalmodellen voor functieaanroepen in voertuigen](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Fijnstemmen van PHI-3 voor meerkeuzevragen: methodologie, resultaten en uitdagingen](https://arxiv.org/abs/2501.01588)
  - [Phi-4-redenering Technisch Rapport](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-redenering Technisch Rapport](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi Modellen Gebruiken

### Phi op Azure AI Foundry

Je kunt leren hoe je Microsoft Phi gebruikt en hoe je end-to-end oplossingen bouwt op je verschillende hardwareapparaten. Om Phi zelf te ervaren, begin je met spelen met de modellen en het aanpassen van Phi aan je scenario's met behulp van de [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Meer informatie vind je bij Aan de Slag met [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Speelterrein**
Elk model heeft een toegewijd speelterrein om het model te testen op [Azure AI Playground](https://aka.ms/try-phi3).

### Phi op GitHub Modellen

Je kunt leren hoe je Microsoft Phi gebruikt en hoe je end-to-end oplossingen bouwt op je verschillende hardwareapparaten. Om Phi zelf te ervaren, begin je met spelen met het model en het aanpassen van Phi aan je scenario's met behulp van de [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Meer informatie vind je bij Aan de Slag met [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Speelterrein**
Elk model heeft een toegewijd [speelterrein om het model te testen](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi op Hugging Face

Je kunt het model ook vinden op de [Hugging Face](https://huggingface.co/microsoft)

**Speelterrein**
 [Hugging Chat speelterrein](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 Andere Cursussen

Ons team produceert ook andere cursussen! Bekijk:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j voor Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js voor Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain voor Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD voor Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI voor Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP voor Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents voor Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatieve AI Serie
[![Generatieve AI voor Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatieve AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatieve AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatieve AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Kernleren
[![ML voor Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Datawetenschap voor Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI voor Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity voor Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webontwikkeling voor Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT voor Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Ontwikkeling voor Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Serie
[![Copilot voor AI Geassisteerd Programmeren](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot voor C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Avontuur](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Verantwoorde AI

Microsoft zet zich in om onze klanten te helpen onze AI-producten op een verantwoorde manier te gebruiken, onze inzichten te delen en op vertrouwen gebaseerde samenwerkingen op te bouwen via tools zoals Transparantienotities en Impactbeoordelingen. Veel van deze bronnen zijn te vinden op [https://aka.ms/RAI](https://aka.ms/RAI).
De benadering van Microsoft voor verantwoorde AI is gebaseerd op onze AI-principes van rechtvaardigheid, betrouwbaarheid en veiligheid, privacy en beveiliging, inclusiviteit, transparantie en verantwoordelijkheid.

Grootschalige modellen voor natuurlijke taal, beeld en spraak - zoals die gebruikt worden in dit voorbeeld - kunnen zich mogelijk oneerlijk, onbetrouwbaar of aanstootgevend gedragen, wat schade kan veroorzaken. Raadpleeg de [Azure OpenAI service Transparantienotitie](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) om geïnformeerd te zijn over risico's en beperkingen.

De aanbevolen aanpak om deze risico's te beperken is het opnemen van een veiligheidssysteem in je architectuur dat schadelijk gedrag kan detecteren en voorkomen. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) biedt een onafhankelijke beschermingslaag, in staat om schadelijke door gebruikers en AI gegenereerde inhoud te detecteren in applicaties en diensten. Azure AI Content Safety omvat tekst- en beeld-API's waarmee je schadelijk materiaal kunt detecteren. Binnen Azure AI Foundry stelt de Content Safety-service je in staat om voorbeeldcode te bekijken, te verkennen en uit te proberen voor het detecteren van schadelijke inhoud in verschillende modaliteiten. De volgende [quickstart-documentatie](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) begeleidt je bij het doen van verzoeken aan de service.
Een ander aspect om rekening mee te houden is de algemene prestatie van de applicatie. Bij multimodale en multimodel-toepassingen beschouwen we prestaties als het systeem dat presteert zoals jij en je gebruikers verwachten, inclusief het niet genereren van schadelijke output. Het is belangrijk om de prestaties van je gehele applicatie te beoordelen met behulp van [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Je hebt ook de mogelijkheid om te creëren en te evalueren met [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Je kunt je AI-applicatie evalueren in je ontwikkelomgeving met behulp van de [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Gegeven een testdataset of een doel, worden de generaties van je generatieve AI-applicatie kwantitatief gemeten met ingebouwde evaluators of aangepaste evaluators naar keuze. Om aan de slag te gaan met de Azure AI Evaluation SDK voor het evalueren van je systeem, kun je de [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) volgen. Zodra je een evaluatieloop uitvoert, kun je [de resultaten visualiseren in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Handelsmerken

Dit project kan handelsmerken of logo's bevatten voor projecten, producten of diensten. Het geautoriseerde gebruik van Microsoft-handelsmerken of logo's is onderworpen aan en moet volgen volgens de [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Het gebruik van Microsoft-handelsmerken of logo's in gewijzigde versies van dit project mag geen verwarring veroorzaken of Microsoft-sponsoring impliceren. Elk gebruik van handelsmerken of logo's van derden is onderworpen aan het beleid van die derden.

## Hulp Krijgen

Als je vastloopt of vragen hebt over het bouwen van AI-apps, sluit je aan bij:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Als je productfeedback of fouten hebt tijdens het bouwen, bezoek dan:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel wij streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->