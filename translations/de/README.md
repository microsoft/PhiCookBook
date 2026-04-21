# Phi Kochbuch: Praktische Beispiele mit Microsofts Phi-Modellen

[![Öffnen und Verwenden der Beispiele in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![In Dev Containers öffnen](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub-Beitragende](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub-Issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub Pull-Requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Willkommen](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub-Beobachter](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub-Forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub-Sterne](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi ist eine Reihe von Open-Source-KI-Modellen, die von Microsoft entwickelt wurden.

Phi ist derzeit das leistungsstärkste und kosteneffizienteste kleine Sprachmodell (SLM) mit sehr guten Benchmarks in mehrsprachigen, logischen, Text-/Chat-Generierungs-, Codier-, Bild-, Audio- und weiteren Szenarien.

Sie können Phi in der Cloud oder auf Edge-Geräten bereitstellen und generative KI-Anwendungen mit begrenzter Rechenleistung einfach erstellen.

Folgen Sie diesen Schritten, um mit der Nutzung dieser Ressourcen zu beginnen:
1. **Forken Sie das Repository**: Klicken Sie [![GitHub-Forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Klonen Sie das Repository**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Treten Sie der Microsoft AI Discord Community bei und treffen Sie Experten und andere Entwickler**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/de/cover.eb18d1b9605d754b.webp)

### 🌐 Mehrsprachige Unterstützung

#### Unterstützt über GitHub Action (Automatisiert & Immer Aktuell)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabisch](../ar/README.md) | [Bengalisch](../bn/README.md) | [Bulgarisch](../bg/README.md) | [Birmanisch (Myanmar)](../my/README.md) | [Chinesisch (vereinfacht)](../zh-CN/README.md) | [Chinesisch (traditionell, Hongkong)](../zh-HK/README.md) | [Chinesisch (traditionell, Macau)](../zh-MO/README.md) | [Chinesisch (traditionell, Taiwan)](../zh-TW/README.md) | [Kroatisch](../hr/README.md) | [Tschechisch](../cs/README.md) | [Dänisch](../da/README.md) | [Niederländisch](../nl/README.md) | [Estnisch](../et/README.md) | [Finnisch](../fi/README.md) | [Französisch](../fr/README.md) | [Deutsch](./README.md) | [Griechisch](../el/README.md) | [Hebräisch](../he/README.md) | [Hindi](../hi/README.md) | [Ungarisch](../hu/README.md) | [Indonesisch](../id/README.md) | [Italienisch](../it/README.md) | [Japanisch](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Koreanisch](../ko/README.md) | [Litauisch](../lt/README.md) | [Malaiisch](../ms/README.md) | [Malaiischalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalesisch](../ne/README.md) | [Nigerianisches Pidgin](../pcm/README.md) | [Norwegisch](../no/README.md) | [Persisch (Farsi)](../fa/README.md) | [Polnisch](../pl/README.md) | [Portugiesisch (Brasilien)](../pt-BR/README.md) | [Portugiesisch (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumänisch](../ro/README.md) | [Russisch](../ru/README.md) | [Serbisch (Kyrillisch)](../sr/README.md) | [Slowakisch](../sk/README.md) | [Slowenisch](../sl/README.md) | [Spanisch](../es/README.md) | [Suaheli](../sw/README.md) | [Schwedisch](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thailändisch](../th/README.md) | [Türkisch](../tr/README.md) | [Ukrainisch](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamesisch](../vi/README.md)

> **Bevorzugen Sie das lokale Klonen?**
>
> Dieses Repository enthält über 50 Sprachübersetzungen, was die Download-Größe erheblich vergrößert. Um ohne Übersetzungen zu klonen, verwenden Sie sparse checkout:
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
> So erhalten Sie alles, was Sie benötigen, um den Kurs mit einem viel schnelleren Download abzuschließen.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Inhaltsverzeichnis

- Einführung
  - [Willkommen in der Phi-Familie](./md/01.Introduction/01/01.PhiFamily.md)
  - [Einrichten Ihrer Umgebung](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Verstehen der Schlüsseltechnologien](./md/01.Introduction/01/01.Understandingtech.md)
  - [KI-Sicherheit für Phi-Modelle](./md/01.Introduction/01/01.AISafety.md)
  - [Phi Hardware-Unterstützung](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi-Modelle & Verfügbarkeit auf Plattformen](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Verwendung von Guidance-ai und Phi](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace Modelle](https://github.com/marketplace/models)
  - [Azure AI Modell-Katalog](https://ai.azure.com)

- Phi Inferenz in verschiedenen Umgebungen
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub Modelle](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Microsoft Foundry Modell-Katalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Lokal](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi Familien-Inferenz
    - [Phi Inferenz auf iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Phi Inferenz auf Android](./md/01.Introduction/03/Android_Inference.md)
    - [Phi Inferenz auf Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Phi Inferenz auf AI-PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Phi Inferenz mit Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Phi Inferenz auf lokalem Server](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Phi Inferenz auf Remote-Server mit AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Phi Inferenz mit Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Phi--Vision Inferenz lokal](./md/01.Introduction/03/Vision_Inference.md)
    - [Phi Inferenz mit Kaito AKS, Azure Containern (offizielle Unterstützung)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Quantifizierung der Phi-Familie](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Quantifizierung Phi-3.5 / 4 mit llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Quantifizierung Phi-3.5 / 4 mit generativen AI-Erweiterungen für onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Quantifizierung Phi-3.5 / 4 mit Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Quantifizierung Phi-3.5 / 4 mit Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Evaluation Phi
    - [Verantwortliche KI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Microsoft Foundry für Evaluation](./md/01.Introduction/05/AIFoundry.md)
    - [Verwendung von Promptflow für Evaluation](./md/01.Introduction/05/Promptflow.md)
 
- RAG mit Azure AI Search
    - [Wie man Phi-4-mini und Phi-4-multimodal(RAG) mit Azure AI Search verwendet](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi Anwendungsentwicklung Beispiele
  - Text- & Chat-Anwendungen
    - Phi-4 Beispiele 
      - [📓] [Chat mit Phi-4-mini ONNX Modell](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat mit lokalem Phi-4 ONNX Modell .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Chat .NET Konsolen-App mit Phi-4 ONNX unter Verwendung von Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 Beispiele
      - [Lokaler Chatbot im Browser unter Verwendung von Phi3, ONNX Runtime Web und WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Modell - Interaktives Phi-3-mini und OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Erstellen eines Wrappers und Verwendung von Phi-3 mit MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Modelloptimierung - Wie man das Phi-3-mini-Modell für ONNX Runtime Web mit Olive optimiert](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 App mit Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 Multi Model KI-gestützte Notizen App Beispiel](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Feinabstimmung und Integration benutzerdefinierter Phi-3-Modelle mit Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Feinabstimmung und Integration benutzerdefinierter Phi-3-Modelle mit Prompt flow in Microsoft Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Bewertung des feinabgestimmten Phi-3 / Phi-3.5 Modells in Microsoft Foundry mit Fokus auf die Responsible AI Prinzipien von Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct Sprachvorhersagebeispiel (Chinesisch/Englisch)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Verwendung von Windows GPU zur Erstellung einer Prompt flow Lösung mit Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Verwendung von Microsoft Phi-3.5 tflite zur Erstellung einer Android App](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET Beispiel mit lokalem ONNX Phi-3 Modell unter Verwendung von Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Konsolen-Chat .NET App mit Semantic Kernel und Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK Code Beispiele 
    - Phi-4 Beispiele 
      - [📓] [Projekterstellung mit Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 Beispiele
      - [Erstellen Sie Ihren eigenen Visual Studio Code GitHub Copilot Chat mit Microsoft Phi-3 Familie](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Erstellen Sie Ihren eigenen Visual Studio Code Chat Copilot Agent mit Phi-3.5 anhand von GitHub Modellen](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Erweiterte Reasoning Beispiele
    - Phi-4 Beispiele 
      - [📓] [Phi-4-mini-reasoning oder Phi-4-reasoning Beispiele](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Feinabstimmung von Phi-4-mini-reasoning mit Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Feinabstimmung von Phi-4-mini-reasoning mit Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning mit GitHub Modellen](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-reasoning mit Microsoft Foundry Modellen](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demos
      - [Phi-4-mini Demos gehostet auf Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal Demos gehostet auf Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Vision Beispiele
    - Phi-4 Beispiele 
      - [📓] [Verwendung von Phi-4-multimodal zum Lesen von Bildern und zur Codeerzeugung](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 Beispiele
      -  [📓][Phi-3-vision-Bild Text zu Text](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Einbettung](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Visueller Sprachassistent - mit Phi3-Vision und OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision Multi-Frame oder Multi-Image Beispiel](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision Lokales ONNX Modell unter Verwendung von Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menübasiertes Phi-3 Vision Lokales ONNX Modell unter Verwendung von Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Reasoning-Vision Beispiele
    - Phi-4-Reasoning-Vision-15B 
      - [📓] [Verwendung von Phi-4-Reasoning-Vision-15B zur Erkennung von Jaywalking](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb)
      - [📓] [Verwendung von Phi-4-Reasoning-Vision-15B für Mathematik](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb)
      - [📓] [Verwendung von Phi-4-Reasoning-Vision-15B zur UI-Erkennung](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb)

  - Mathematik Beispiele
    -  Phi-4-Mini-Flash-Reasoning-Instruct Beispiele  [Mathematik Demo mit Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - Audio Beispiele
    - Phi-4 Beispiele 
      - [📓] [Extrahieren von Audiotranskripten mit Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal Audio Beispiel](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal Sprachübersetzungsbeispiel](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET Konsolenanwendung mit Phi-4-multimodal Audio zur Analyse einer Audiodatei und Erzeugung eines Transkripts](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE Beispiele
    - Phi-3 / 3.5 Beispiele
      - [📓] [Phi-3.5 Mixture of Experts Modelle (MoEs) Social Media Beispiel](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Erstellen einer Retrieval-Augmented Generation (RAG) Pipeline mit NVIDIA NIM Phi-3 MOE, Azure AI Search und LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Function Calling Beispiele
    - Phi-4 Beispiele 🆕
      -  [📓] [Verwendung von Function Calling mit Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Verwendung von Function Calling zur Erstellung von Multi-Agenten mit Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Verwendung von Function Calling mit Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Verwendung von Function Calling mit ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Beispiel für multimodales Mischen
    - Phi-4 Beispiele 🆕
      -  [📓] [Verwendung von Phi-4-multimodal als Technologiejournalist](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET Konsolenanwendung mit Phi-4-multimodal zur Analyse von Bildern](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Feinabstimmung Phi Beispiele
  - [Feinabstimmungsszenarien](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Feinabstimmung vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Feinabstimmung Lassen Sie Phi-3 ein Industrieexperte werden](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Feinabstimmung von Phi-3 mit AI Toolkit für VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Feinabstimmung von Phi-3 mit Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Feinabstimmung von Phi-3 mit Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Feinabstimmung von Phi-3 mit QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Feinabstimmung von Phi-3 mit Microsoft Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Feinabstimmung von Phi-3 mit Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Feinabstimmung mit Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Feinabstimmung mit Microsoft Olive Hands-On Labor](./md/03.FineTuning/olive-lab/readme.md)
  - [Feinabstimmung von Phi-3-vision mit Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Feinabstimmung von Phi-3 mit Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Feinabstimmung von Phi-3-vision (offizielle Unterstützung)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Feinabstimmung Phi-3 mit Kaito AKS, Azure Containers (offizielle Unterstützung)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Feinabstimmung Phi-3 und 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands-on-Lab
  - [Erkundung hochmoderner Modelle: LLMs, SLMs, lokale Entwicklung und mehr](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Entfesseln des NLP-Potenzials: Feinabstimmung mit Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Wissenschaftliche Forschungsarbeiten und Publikationen
  - [Lehrbücher sind alles, was Sie brauchen II: phi-1.5 technischer Bericht](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Technischer Bericht: Ein hochleistungsfähiges Sprachmodell lokal auf Ihrem Telefon](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Technischer Bericht](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Technischer Bericht: Kompakte und dennoch leistungsstarke multimodale Sprachmodelle durch Mischung von LoRAs](https://arxiv.org/abs/2503.01743)
  - [Optimierung kleiner Sprachmodelle für In-Fahrzeug-Funktionsaufrufe](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Feinabstimmung PHI-3 für Multiple-Choice-Fragen: Methodik, Ergebnisse und Herausforderungen](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning Technischer Bericht](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning Technischer Bericht](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Verwendung von Phi-Modellen

### Phi auf Microsoft Foundry

Sie können lernen, wie man Microsoft Phi verwendet und wie man E2E-Lösungen auf Ihren verschiedenen Hardwaregeräten erstellt. Um Phi selbst zu erleben, beginnen Sie damit, mit den Modellen zu experimentieren und Phi für Ihre Szenarien anzupassen, indem Sie den [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) nutzen. Mehr erfahren Sie unter Erste Schritte mit [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Spielwiese**
Jedes Modell verfügt über eine eigene Spielwiese zum Testen des Modells [Azure AI Playground](https://aka.ms/try-phi3).

### Phi auf GitHub Models

Sie können lernen, wie man Microsoft Phi verwendet und wie man E2E-Lösungen auf Ihren verschiedenen Hardwaregeräten erstellt. Um Phi selbst zu erleben, beginnen Sie damit, mit dem Modell zu experimentieren und Phi für Ihre Szenarien anzupassen, indem Sie den [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) nutzen. Mehr erfahren Sie unter Erste Schritte mit [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Spielwiese**
Jedes Modell hat eine eigene [Spielwiese zum Testen des Modells](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi auf Hugging Face

Sie können das Modell auch auf [Hugging Face](https://huggingface.co/microsoft) finden.

**Spielwiese**
 [Hugging Chat Spielwiese](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 Weitere Kurse

Unser Team produziert weitere Kurse! Schauen Sie vorbei:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j für Anfänger](https://img.shields.io/badge/LangChain4j%20für%20Anfänger-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js für Anfänger](https://img.shields.io/badge/LangChain.js%20für%20Anfänger-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain für Anfänger](https://img.shields.io/badge/LangChain%20für%20Anfänger-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD für Anfänger](https://img.shields.io/badge/AZD%20für%20Anfänger-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI für Anfänger](https://img.shields.io/badge/Edge%20AI%20für%20Anfänger-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP für Anfänger](https://img.shields.io/badge/MCP%20für%20Anfänger-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents für Anfänger](https://img.shields.io/badge/AI%20Agents%20für%20Anfänger-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative KI Serie
[![Generative KI für Anfänger](https://img.shields.io/badge/Generative%20KI%20für%20Anfänger-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative KI (.NET)](https://img.shields.io/badge/Generative%20KI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative KI (Java)](https://img.shields.io/badge/Generative%20KI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative KI (JavaScript)](https://img.shields.io/badge/Generative%20KI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Kernlernen
[![ML für Anfänger](https://img.shields.io/badge/ML%20für%20Anfänger-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Datenwissenschaft für Anfänger](https://img.shields.io/badge/Datenwissenschaft%20für%20Anfänger-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![KI für Anfänger](https://img.shields.io/badge/KI%20für%20Anfänger-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersicherheit für Anfänger](https://img.shields.io/badge/Cybersicherheit%20für%20Anfänger-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webentwicklung für Anfänger](https://img.shields.io/badge/Web%20Dev%20für%20Anfänger-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT für Anfänger](https://img.shields.io/badge/IoT%20für%20Anfänger-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR-Entwicklung für Anfänger](https://img.shields.io/badge/XR%20Entwicklung%20für%20Anfänger-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot-Serie
[![Copilot für KI-Paarprogrammierung](https://img.shields.io/badge/Copilot%20für%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot für C#/.NET](https://img.shields.io/badge/Copilot%20für%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Abenteuer](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Verantwortliche KI

Microsoft engagiert sich dafür, unseren Kunden zu helfen, unsere KI-Produkte verantwortungsvoll zu nutzen, unsere Erkenntnisse zu teilen und vertrauensbasierte Partnerschaften durch Tools wie Transparenz-Notizen und Wirkungseinschätzungen aufzubauen. Viele dieser Ressourcen finden Sie unter [https://aka.ms/RAI](https://aka.ms/RAI).
Der Ansatz von Microsoft zu verantwortlicher KI basiert auf unseren KI-Prinzipien Fairness, Zuverlässigkeit und Sicherheit, Privatsphäre und Sicherheit, Inklusivität, Transparenz und Verantwortlichkeit.

Groß angelegte Sprach-, Bild- und Sprachmodelle – wie die in diesem Beispiel verwendeten – können sich potenziell unfair, unzuverlässig oder anstößig verhalten und dadurch Schäden verursachen. Bitte konsultieren Sie die [Transparenz-Note zum Azure OpenAI-Dienst](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), um über Risiken und Einschränkungen informiert zu sein.
Der empfohlene Ansatz zur Minderung dieser Risiken besteht darin, ein Sicherheitssystem in Ihre Architektur zu integrieren, das schädliches Verhalten erkennen und verhindern kann. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) bietet eine unabhängige Schutzeinheit, die schädliche von Nutzern generierte und KI-generierte Inhalte in Anwendungen und Diensten erkennen kann. Azure AI Content Safety umfasst Text- und Bild-APIs, mit denen Sie schädliches Material erkennen können. Innerhalb von Microsoft Foundry ermöglicht Ihnen der Content Safety-Dienst, Beispielcode zum Erkennen schädlicher Inhalte über verschiedene Modalitäten hinweg anzusehen, zu erkunden und auszuprobieren. Die folgende [Schnellstart-Dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) führt Sie durch das Senden von Anfragen an den Dienst.

Ein weiterer Aspekt, der zu berücksichtigen ist, ist die Gesamtleistung der Anwendung. Bei multimodalen und multimodellen Anwendungen verstehen wir unter Leistung, dass das System so funktioniert, wie Sie und Ihre Benutzer es erwarten, einschließlich der Vermeidung von schädlichen Ausgaben. Es ist wichtig, die Leistung Ihrer gesamten Anwendung mit [Performance- und Qualitäts- sowie Risiko- und Sicherheitsevaluator](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) zu bewerten. Sie haben auch die Möglichkeit, mit [benutzerdefinierten Evaluatoren](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) zu erstellen und zu evaluieren.

Sie können Ihre KI-Anwendung in Ihrer Entwicklungsumgebung mit dem [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) bewerten. Basierend auf einem Testdatensatz oder einem Ziel werden die Generierungen Ihrer generativen KI-Anwendung quantitativ mit eingebauten oder benutzerdefinierten Evaluatoren Ihrer Wahl gemessen. Um mit dem Azure AI Evaluation SDK zur Bewertung Ihres Systems zu beginnen, können Sie der [Schnellstartanleitung](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) folgen. Nachdem Sie eine Evaluierung durchgeführt haben, können Sie die [Ergebnisse in Microsoft Foundry visualisieren](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marken

Dieses Projekt kann Marken oder Logos für Projekte, Produkte oder Dienstleistungen enthalten. Die autorisierte Verwendung von Microsoft-Marken oder -Logos unterliegt den [Microsoft-Marken- und Markenrichtlinien](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) und muss diesen folgen.
Die Verwendung von Microsoft-Marken oder -Logos in modifizierten Versionen dieses Projekts darf keine Verwirrung stiften oder eine Microsoft-Unterstützung implizieren. Jegliche Verwendung von Marken oder Logos Dritter unterliegt den jeweiligen Richtlinien dieser Dritten.

## Hilfe erhalten

Wenn Sie nicht weiterkommen oder Fragen zum Erstellen von KI-Anwendungen haben, treten Sie bei:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Wenn Sie Produktfeedback geben oder Fehler beim Erstellen feststellen, besuchen Sie:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache ist als autoritative Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->