<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2e042b12a63c59931dc121c2c638bc58",
  "translation_date": "2025-07-09T18:20:14+00:00",
  "source_file": "README.md",
  "language_code": "it"
}
-->
# Phi Cookbook: Esempi Pratici con i Modelli Phi di Microsoft

[![Apri e usa gli esempi in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![Apri in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Contributori GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![Issue GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![Pull request GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Watcher GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![Fork GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![Star GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi è una serie di modelli AI open source sviluppati da Microsoft.

Attualmente Phi è il modello linguistico piccolo (SLM) più potente ed economico, con ottime prestazioni in più lingue, ragionamento, generazione di testo/chat, coding, immagini, audio e altri scenari.

Puoi distribuire Phi sul cloud o su dispositivi edge, e costruire facilmente applicazioni di AI generativa anche con risorse di calcolo limitate.

Segui questi passaggi per iniziare a usare queste risorse:  
1. **Forka il Repository**: Clicca su [![Fork GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **Clona il Repository**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Unisciti alla Community Microsoft AI su Discord e incontra esperti e sviluppatori**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

## 🌐 Supporto Multilingue

### Supportato tramite GitHub Action (Automatizzato e Sempre Aggiornato)

[Francese](../fr/README.md) | [Spagnolo](../es/README.md) | [Tedesco](../de/README.md) | [Russo](../ru/README.md) | [Arabo](../ar/README.md) | [Persiano (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Cinese (Semplificato)](../zh/README.md) | [Cinese (Tradizionale, Macao)](../mo/README.md) | [Cinese (Tradizionale, Hong Kong)](../hk/README.md) | [Cinese (Tradizionale, Taiwan)](../tw/README.md) | [Giapponese](../ja/README.md) | [Coreano](../ko/README.md) | [Hindi](../hi/README.md)  
[Bengalese](../bn/README.md) | [Marathi](../mr/README.md) | [Nepalese](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portoghese (Portogallo)](../pt/README.md) | [Portoghese (Brasile)](../br/README.md) | [Italiano](./README.md) | [Polacco](../pl/README.md) | [Turco](../tr/README.md) | [Greco](../el/README.md) | [Thailandese](../th/README.md) | [Svedese](../sv/README.md) | [Danese](../da/README.md) | [Norvegese](../no/README.md) | [Finlandese](../fi/README.md) | [Olandese](../nl/README.md) | [Ebraico](../he/README.md) | [Vietnamita](../vi/README.md) | [Indonesiano](../id/README.md) | [Malese](../ms/README.md) | [Tagalog (Filippino)](../tl/README.md) | [Swahili](../sw/README.md) | [Ungherese](../hu/README.md) | [Ceco](../cs/README.md) | [Slovacco](../sk/README.md) | [Rumeno](../ro/README.md) | [Bulgaro](../bg/README.md) | [Serbo (Cirillico)](../sr/README.md) | [Croato](../hr/README.md) | [Sloveno](../sl/README.md)

## Indice

- Introduzione  
  - [Benvenuto nella Famiglia Phi](./md/01.Introduction/01/01.PhiFamily.md)  
  - [Configurazione dell’ambiente](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [Comprendere le Tecnologie Chiave](./md/01.Introduction/01/01.Understandingtech.md)  
  - [Sicurezza AI per i Modelli Phi](./md/01.Introduction/01/01.AISafety.md)  
  - [Supporto Hardware Phi](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [Modelli Phi & Disponibilità sulle piattaforme](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [Usare Guidance-ai e Phi](./md/01.Introduction/01/01.Guidance.md)  
  - [Modelli GitHub Marketplace](https://github.com/marketplace/models)  
  - [Catalogo Modelli Azure AI](https://ai.azure.com)

- Inferenza Phi in ambienti diversi  
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)  
    -  [Modelli GitHub](./md/01.Introduction/02/02.GitHubModel.md)  
    -  [Catalogo Modelli Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)  
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)  
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)  
    -  [Foundry Locale](./md/01.Introduction/02/07.FoundryLocal.md)

- Inferenza Phi Family  
    - [Inferenza Phi su iOS](./md/01.Introduction/03/iOS_Inference.md)  
    - [Inferenza Phi su Android](./md/01.Introduction/03/Android_Inference.md)  
    - [Inferenza Phi su Jetson](./md/01.Introduction/03/Jetson_Inference.md)  
    - [Inferenza Phi su AI PC](./md/01.Introduction/03/AIPC_Inference.md)  
    - [Inferenza Phi con Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)  
    - [Inferenza Phi su Server Locale](./md/01.Introduction/03/Local_Server_Inference.md)  
    - [Inferenza Phi su Server Remoto usando AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)  
    - [Inferenza Phi con Rust](./md/01.Introduction/03/Rust_Inference.md)  
    - [Inferenza Phi--Vision in Locale](./md/01.Introduction/03/Vision_Inference.md)  
    - [Inferenza Phi con Kaito AKS, Azure Containers (supporto ufficiale)](./md/01.Introduction/03/Kaito_Inference.md)  
-  [Quantizzazione Phi Family](./md/01.Introduction/04/QuantifyingPhi.md)  
    - [Quantizzazione Phi-3.5 / 4 usando llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
    - [Quantizzazione Phi-3.5 / 4 usando estensioni Generative AI per onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
    - [Quantizzazione Phi-3.5 / 4 usando Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
    - [Quantizzazione Phi-3.5 / 4 usando Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Valutazione Phi  
    - [AI Responsabile](./md/01.Introduction/05/ResponsibleAI.md)  
    - [Azure AI Foundry per la Valutazione](./md/01.Introduction/05/AIFoundry.md)  
    - [Usare Promptflow per la Valutazione](./md/01.Introduction/05/Promptflow.md)

- RAG con Azure AI Search  
    - [Come usare Phi-4-mini e Phi-4-multimodal (RAG) con Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Esempi di sviluppo applicazioni Phi  
  - Applicazioni Testo & Chat  
    - Phi-4 Esempi 🆕  
      - [📓] [Chat con modello Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Chat con modello Phi-4 locale ONNX .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [App Console Chat .NET con Phi-4 ONNX usando Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 Esempi  
      - [Chatbot locale nel browser usando Phi3, ONNX Runtime Web e WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [Chat OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [Multi Modello - Phi-3-mini interattivo e OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - Creare un wrapper e usare Phi-3 con MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [Ottimizzazione Modello - Come ottimizzare Phi-3-mini per ONNX Runtime Web con Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [App WinUI3 con Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [Esempio App Note AI Multi Modello WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Affina e integra modelli Phi-3 personalizzati con Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Affina e integra modelli Phi-3 personalizzati con Prompt flow in Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Valuta il modello Phi-3 / Phi-3.5 affinato in Azure AI Foundry con focus sui principi di AI responsabile di Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Esempio di previsione linguistica Phi-3.5-mini-instruct (Cinese/Inglese)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Chatbot RAG Phi-3.5-Instruct WebGPU](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Utilizzo della GPU Windows per creare una soluzione Prompt flow con Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Utilizzo di Microsoft Phi-3.5 tflite per creare un'app Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Esempio Q&A .NET usando modello ONNX Phi-3 locale con Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [App console chat .NET con Semantic Kernel e Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Campioni basati su codice Azure AI Inference SDK  
  - Campioni Phi-4 🆕  
    - [📓] [Genera codice progetto usando Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Campioni Phi-3 / 3.5  
    - [Costruisci il tuo Visual Studio Code GitHub Copilot Chat con Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [Crea il tuo agente Chat Copilot per Visual Studio Code con Phi-3.5 usando modelli GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- Campioni di ragionamento avanzato  
  - Campioni Phi-4 🆕  
    - [📓] [Campioni Phi-4-mini-reasoning o Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Affinamento di Phi-4-mini-reasoning con Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Affinamento di Phi-4-mini-reasoning con Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Phi-4-mini-reasoning con modelli GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Phi-4-mini-reasoning con modelli Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- Demo  
    - [Demo Phi-4-mini ospitati su Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Demo Phi-4-multimodal ospitati su Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- Campioni Vision  
  - Campioni Phi-4 🆕  
    - [📓] [Usa Phi-4-multimodal per leggere immagini e generare codice](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Campioni Phi-3 / 3.5  
    - [📓][Phi-3-vision - da immagine a testo](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [DEMO: Riciclaggio Phi-3](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - Assistente linguistico visivo - con Phi3-Vision e OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Esempio Phi-3.5 Vision multi-frame o multi-immagine](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Modello ONNX locale Phi-3 Vision usando Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Modello ONNX locale Phi-3 Vision basato su menu usando Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- Campioni Math  
  - Campioni Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [Demo Math con Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)  

- Campioni Audio  
  - Campioni Phi-4 🆕  
    - [📓] [Estrazione di trascrizioni audio usando Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Esempio audio Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Esempio di traduzione vocale Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [Applicazione console .NET che usa Phi-4-multimodal Audio per analizzare un file audio e generare trascrizione](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- Campioni MOE  
  - Campioni Phi-3 / 3.5  
    - [📓] [Esempio Phi-3.5 Mixture of Experts Models (MoEs) per social media](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [Costruzione di una pipeline Retrieval-Augmented Generation (RAG) con NVIDIA NIM Phi-3 MOE, Azure AI Search e LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  
-  
- Campioni Function Calling  
  - Campioni Phi-4 🆕  
    - [📓] [Uso di Function Calling con Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Uso di Function Calling per creare multi-agenti con Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Uso di Function Calling con Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [Uso di Function Calling con ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  
- Campioni Multimodali  
  - Campioni Phi-4 🆕  
    - [📓] [Uso di Phi-4-multimodal come giornalista tecnologico](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [Applicazione console .NET che usa Phi-4-multimodal per analizzare immagini](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Affinamento Phi  
  - [Scenari di affinamento](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [Affinamento vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Affina Phi-3 per farlo diventare un esperto di settore](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [Affinamento Phi-3 con AI Toolkit per VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Affinamento Phi-3 con Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Affinamento Phi-3 con Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [Affinamento Phi-3 con QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Affinamento Phi-3 con Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Affinamento Phi-3 con Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Affinamento con Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Laboratorio pratico di affinamento con Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)  
  - [Affinamento Phi-3-vision con Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Affinamento Phi-3 con Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Affinamento Phi-3-vision (supporto ufficiale)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Affinamento Phi-3 con Kaito AKS, Azure Containers (supporto ufficiale)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Affinamento Phi-3 e 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- Laboratori pratici  
  - [Esplorare modelli all’avanguardia: LLM, SLM, sviluppo locale e altro](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [Sbloccare il potenziale NLP: affinamento con Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- Articoli accademici e pubblicazioni  
  - [Textbooks Are All You Need II: rapporto tecnico phi-1.5](https://arxiv.org/abs/2309.05463)  
  - [Rapporto tecnico Phi-3: un modello linguistico altamente capace localmente sul tuo telefono](https://arxiv.org/abs/2404.14219)  
  - [Rapporto tecnico Phi-4](https://arxiv.org/abs/2412.08905)  
  - [Rapporto tecnico Phi-4-Mini: modelli linguistici multimodali compatti ma potenti tramite Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [Ottimizzazione di piccoli modelli linguistici per Function-Calling in veicoli](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) Affinamento PHI-3 per domande a scelta multipla: metodologia, risultati e sfide](https://arxiv.org/abs/2501.01588)
- [Rapporto Tecnico Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Rapporto Tecnico Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Utilizzo dei Modelli Phi

### Phi su Azure AI Foundry

Puoi imparare come utilizzare Microsoft Phi e come costruire soluzioni E2E sui tuoi diversi dispositivi hardware. Per provare Phi direttamente, inizia a sperimentare con i modelli e a personalizzare Phi per i tuoi scenari utilizzando il [Catalogo Modelli Azure AI Foundry](https://aka.ms/phi3-azure-ai). Puoi approfondire con la guida Introduzione a [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Playground**  
Ogni modello ha un playground dedicato per testare il modello su [Azure AI Playground](https://aka.ms/try-phi3).

### Phi su Modelli GitHub

Puoi imparare come utilizzare Microsoft Phi e come costruire soluzioni E2E sui tuoi diversi dispositivi hardware. Per provare Phi direttamente, inizia a sperimentare con il modello e a personalizzare Phi per i tuoi scenari utilizzando il [Catalogo Modelli GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Puoi approfondire con la guida Introduzione a [Catalogo Modelli GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**  
Ogni modello ha un [playground dedicato per testare il modello](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi su Hugging Face

Puoi anche trovare il modello su [Hugging Face](https://huggingface.co/microsoft)

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## AI Responsabile

Microsoft si impegna ad aiutare i propri clienti a utilizzare i prodotti di AI in modo responsabile, condividendo le nostre esperienze e costruendo partnership basate sulla fiducia attraverso strumenti come Transparency Notes e Impact Assessments. Molte di queste risorse sono disponibili su [https://aka.ms/RAI](https://aka.ms/RAI).  
L’approccio di Microsoft all’AI responsabile si basa sui nostri principi di AI: equità, affidabilità e sicurezza, privacy e protezione, inclusività, trasparenza e responsabilità.

I modelli su larga scala per linguaggio naturale, immagini e voce - come quelli usati in questo esempio - possono potenzialmente comportarsi in modi ingiusti, inaffidabili o offensivi, causando danni. Consulta la [Transparency note del servizio Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) per essere informato sui rischi e le limitazioni.

L’approccio raccomandato per mitigare questi rischi è includere un sistema di sicurezza nella tua architettura in grado di rilevare e prevenire comportamenti dannosi. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) fornisce un livello di protezione indipendente, capace di rilevare contenuti dannosi generati dagli utenti o dall’AI nelle applicazioni e nei servizi. Azure AI Content Safety include API per testo e immagini che permettono di individuare materiale dannoso. All’interno di Azure AI Foundry, il servizio Content Safety consente di visualizzare, esplorare e provare esempi di codice per rilevare contenuti dannosi in diverse modalità. La seguente [documentazione quickstart](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ti guida nell’effettuare richieste al servizio.

Un altro aspetto da considerare è la performance complessiva dell’applicazione. Con applicazioni multi-modali e multi-modello, per performance intendiamo che il sistema funzioni come tu e i tuoi utenti vi aspettate, incluso il non generare output dannosi. È importante valutare la performance della tua applicazione complessiva utilizzando i [valutatori di Performance, Qualità, Rischio e Sicurezza](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Hai anche la possibilità di creare e valutare con [valutatori personalizzati](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Puoi valutare la tua applicazione AI nel tuo ambiente di sviluppo usando l’[Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Dato un dataset di test o un obiettivo, le generazioni della tua applicazione AI generativa vengono misurate quantitativamente con valutatori integrati o personalizzati a tua scelta. Per iniziare con l’Azure AI Evaluation SDK e valutare il tuo sistema, puoi seguire la [guida quickstart](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Una volta eseguita una valutazione, puoi [visualizzare i risultati in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marchi

Questo progetto può contenere marchi o loghi di progetti, prodotti o servizi. L’uso autorizzato dei marchi o loghi Microsoft è soggetto e deve seguire le [Linee Guida sui Marchi e Brand di Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
L’uso di marchi o loghi Microsoft in versioni modificate di questo progetto non deve causare confusione né implicare sponsorizzazione da parte di Microsoft. Qualsiasi uso di marchi o loghi di terze parti è soggetto alle politiche di tali terze parti.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.