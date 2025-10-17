<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4987daf30687ad3850757c9eae3f5411",
  "translation_date": "2025-10-17T10:20:08+00:00",
  "source_file": "README.md",
  "language_code": "it"
}
-->
# Phi Cookbook: Esempi pratici con i modelli Phi di Microsoft

Phi è una serie di modelli AI open source sviluppati da Microsoft.

Phi è attualmente il modello linguistico piccolo (SLM) più potente ed economico, con ottimi risultati nei benchmark per multilingua, ragionamento, generazione di testo/chat, codifica, immagini, audio e altri scenari.

Puoi distribuire Phi nel cloud o su dispositivi edge e costruire facilmente applicazioni di AI generativa con risorse di calcolo limitate.

Segui questi passaggi per iniziare a utilizzare queste risorse:
1. **Fai un fork del repository**: Clicca [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Clona il repository**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Unisciti alla community Microsoft AI su Discord e incontra esperti e altri sviluppatori**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 Supporto multilingua

#### Supportato tramite GitHub Action (Automatizzato e sempre aggiornato)

[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](./README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

## Indice

- Introduzione
  - [Benvenuto nella famiglia Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Configurare il tuo ambiente](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Comprendere le tecnologie chiave](./md/01.Introduction/01/01.Understandingtech.md)
  - [Sicurezza AI per i modelli Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Supporto hardware per Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Modelli Phi e disponibilità su diverse piattaforme](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Utilizzare Guidance-ai e Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Modelli su GitHub Marketplace](https://github.com/marketplace/models)
  - [Catalogo modelli Azure AI](https://ai.azure.com)

- Inferenza Phi in diversi ambienti
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [Modelli GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    - [Catalogo modelli Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    - [Foundry Locale](./md/01.Introduction/02/07.FoundryLocal.md)

- Inferenza Famiglia Phi
    - [Inferenza Phi su iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inferenza Phi su Android](./md/01.Introduction/03/Android_Inference.md)
    - [Inferenza Phi su Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inferenza Phi su PC AI](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inferenza Phi con Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Inferenza Phi su server locale](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inferenza Phi su server remoto usando AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inferenza Phi con Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inferenza Phi--Vision in locale](./md/01.Introduction/03/Vision_Inference.md)
    - [Inferenza Phi con Kaito AKS, Azure Containers (supporto ufficiale)](./md/01.Introduction/03/Kaito_Inference.md)
- [Quantificazione Famiglia Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Quantificazione Phi-3.5 / 4 usando llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Quantificazione Phi-3.5 / 4 usando estensioni di AI generativa per onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Quantificazione Phi-3.5 / 4 usando Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Quantificazione Phi-3.5 / 4 usando Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Valutazione Phi
    - [AI Responsabile](./md/01.Introduction/05/ResponsibleAI.md)
    - [Valutazione con Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [Utilizzo di Promptflow per la valutazione](./md/01.Introduction/05/Promptflow.md)

- RAG con Azure AI Search
    - [Come utilizzare Phi-4-mini e Phi-4-multimodal (RAG) con Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Esempi di sviluppo di applicazioni Phi
  - Applicazioni di testo e chat
    - Esempi Phi-4 🆕
      - [📓] [Chat con il modello Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat con il modello Phi-4 locale ONNX .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [App console .NET per chat con Phi-4 ONNX usando Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Esempi Phi-3 / 3.5
      - [Chatbot locale nel browser usando Phi3, ONNX Runtime Web e WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [Chat OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Modello interattivo - Phi-3-mini e OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Creare un wrapper e utilizzare Phi-3 con MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Ottimizzazione del modello - Come ottimizzare il modello Phi-3-min per ONNX Runtime Web con Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [App WinUI3 con Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [App Note AI con Multi Modello WinUI3 - Esempio](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Ottimizzazione e integrazione di modelli personalizzati Phi-3 con Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Ottimizzazione e integrazione di modelli personalizzati Phi-3 con Prompt flow in Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Valutazione del modello ottimizzato Phi-3 / Phi-3.5 in Azure AI Foundry con focus sui principi di AI responsabile di Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Esempio di previsione linguistica Phi-3.5-mini-instruct (Cinese/Inglese)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Chatbot WebGPU RAG con Phi-3.5-Instruct](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Utilizzo della GPU di Windows per creare una soluzione Prompt flow con Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Utilizzo di Microsoft Phi-3.5 tflite per creare un'app Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Esempio Q&A .NET utilizzando il modello locale ONNX Phi-3 con Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [App console chat .NET con Semantic Kernel e Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Esempi di codice SDK di inferenza Azure AI
  - Esempi Phi-4 🆕
    - [📓] [Generare codice di progetto utilizzando Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Esempi Phi-3 / 3.5
    - [Crea il tuo GitHub Copilot Chat per Visual Studio Code con la famiglia Phi-3 di Microsoft](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [Crea il tuo agente Chat Copilot per Visual Studio Code con Phi-3.5 utilizzando i modelli GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- Esempi di ragionamento avanzato
  - Esempi Phi-4 🆕
    - [📓] [Esempi di ragionamento Phi-4-mini o Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Ottimizzazione di Phi-4-mini-reasoning con Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Ottimizzazione di Phi-4-mini-reasoning con Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning con modelli GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Phi-4-mini-reasoning con modelli Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- Demo
    - [Demo Phi-4-mini ospitati su Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Demo Phi-4-multimodal ospitati su Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- Esempi di Vision
  - Esempi Phi-4 🆕
    - [📓] [Utilizzare Phi-4-multimodal per leggere immagini e generare codice](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Esempi Phi-3 / 3.5
    - [📓][Phi-3-vision - Da testo immagine a testo](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [DEMO: Phi-3 Riciclaggio](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Assistente visivo linguistico - con Phi3-Vision e OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision esempio multi-frame o multi-immagine](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Phi-3 Vision Modello Locale ONNX utilizzando Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Modello Locale ONNX Phi-3 Vision basato su menu utilizzando Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

- Esempi di Matematica
  - Esempi Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [Demo Matematica con Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)

- Esempi Audio
  - Esempi Phi-4 🆕
    - [📓] [Estrazione di trascrizioni audio utilizzando Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Esempio Audio Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Esempio di traduzione vocale Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [Applicazione console .NET utilizzando Phi-4-multimodal Audio per analizzare un file audio e generare una trascrizione](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- Esempi MOE
  - Esempi Phi-3 / 3.5
    - [📓] [Modelli Mixture of Experts Phi-3.5 (MoEs) - Esempio Social Media](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [Costruire una pipeline di generazione aumentata da recupero (RAG) con NVIDIA NIM Phi-3 MOE, Azure AI Search e LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- Esempi di chiamata di funzioni
  - Esempi Phi-4 🆕
    - [📓] [Utilizzo della chiamata di funzioni con Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Utilizzo della chiamata di funzioni per creare multi-agenti con Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Utilizzo della chiamata di funzioni con Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [Utilizzo della chiamata di funzioni con ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- Esempi di mescolanza multimodale
  - Esempi Phi-4 🆕
    - [📓] [Utilizzo di Phi-4-multimodal come giornalista tecnologico](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [Applicazione console .NET utilizzando Phi-4-multimodal per analizzare immagini](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Esempi di ottimizzazione Phi
  - [Scenari di ottimizzazione](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Ottimizzazione vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Ottimizzazione: Trasformare Phi-3 in un esperto del settore](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Ottimizzazione di Phi-3 con AI Toolkit per VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Ottimizzazione di Phi-3 con Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Ottimizzazione di Phi-3 con Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Ottimizzazione di Phi-3 con QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Ottimizzazione di Phi-3 con Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Ottimizzazione di Phi-3 con Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Ottimizzazione con Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Laboratorio pratico di ottimizzazione con Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)
  - [Ottimizzazione di Phi-3-vision con Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Ottimizzazione di Phi-3 con il framework Apple MLX](./md/03.FineTuning/FineTuning_MLX.md)
  - [Ottimizzazione di Phi-3-vision (supporto ufficiale)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Ottimizzazione di Phi-3 con Kaito AKS, Azure Containers (supporto ufficiale)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Ottimizzazione di Phi-3 e 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Laboratorio pratico
  - [Esplorare modelli all'avanguardia: LLMs, SLMs, sviluppo locale e altro](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Sbloccare il potenziale NLP: Ottimizzazione con Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Articoli di ricerca accademica e pubblicazioni
  - [Textbooks Are All You Need II: rapporto tecnico phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Rapporto tecnico Phi-3: un modello linguistico altamente capace localmente sul tuo telefono](https://arxiv.org/abs/2404.14219)
  - [Rapporto tecnico Phi-4](https://arxiv.org/abs/2412.08905)
  - [Rapporto tecnico Phi-4-Mini: modelli linguistici multimodali compatti ma potenti tramite Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Ottimizzazione di piccoli modelli linguistici per il richiamo di funzioni nei veicoli](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Fine-Tuning di PHI-3 per rispondere a domande a scelta multipla: metodologia, risultati e sfide](https://arxiv.org/abs/2501.01588)
  - [Rapporto tecnico su Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Rapporto tecnico su Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Utilizzo dei modelli Phi

### Phi su Azure AI Foundry

Puoi imparare a utilizzare Microsoft Phi e a costruire soluzioni end-to-end sui tuoi diversi dispositivi hardware. Per provare Phi, inizia a sperimentare con i modelli e personalizza Phi per i tuoi scenari utilizzando il [Catalogo modelli di Azure AI Foundry](https://aka.ms/phi3-azure-ai). Puoi saperne di più consultando la guida introduttiva [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Playground**  
Ogni modello ha un playground dedicato per testare il modello [Azure AI Playground](https://aka.ms/try-phi3).

### Phi su GitHub Models

Puoi imparare a utilizzare Microsoft Phi e a costruire soluzioni end-to-end sui tuoi diversi dispositivi hardware. Per provare Phi, inizia a sperimentare con il modello e personalizza Phi per i tuoi scenari utilizzando il [Catalogo modelli su GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Puoi saperne di più consultando la guida introduttiva [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Playground**  
Ogni modello ha un [playground dedicato per testare il modello](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi su Hugging Face

Puoi trovare il modello anche su [Hugging Face](https://huggingface.co/microsoft).

**Playground**  
[Playground Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct).

## AI Responsabile

Microsoft si impegna ad aiutare i propri clienti a utilizzare i prodotti di intelligenza artificiale in modo responsabile, condividendo le proprie esperienze e costruendo partnership basate sulla fiducia attraverso strumenti come le Note di Trasparenza e le Valutazioni di Impatto. Molte di queste risorse sono disponibili su [https://aka.ms/RAI](https://aka.ms/RAI).  
L'approccio di Microsoft all'AI responsabile si basa sui principi di equità, affidabilità e sicurezza, privacy e sicurezza, inclusività, trasparenza e responsabilità.

I modelli su larga scala di linguaggio naturale, immagini e voce - come quelli utilizzati in questo esempio - possono potenzialmente comportarsi in modi ingiusti, inaffidabili o offensivi, causando danni. Consulta la [Nota di trasparenza del servizio Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) per essere informato sui rischi e le limitazioni.

L'approccio raccomandato per mitigare questi rischi è includere un sistema di sicurezza nella tua architettura che possa rilevare e prevenire comportamenti dannosi. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) fornisce un livello indipendente di protezione, in grado di rilevare contenuti dannosi generati dagli utenti e dall'AI nelle applicazioni e nei servizi. Azure AI Content Safety include API di testo e immagini che consentono di rilevare materiale dannoso. All'interno di Azure AI Foundry, il servizio Content Safety permette di visualizzare, esplorare e provare codice di esempio per rilevare contenuti dannosi in diverse modalità. La seguente [documentazione introduttiva](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ti guida nella creazione di richieste al servizio.

Un altro aspetto da considerare è la performance complessiva dell'applicazione. Con applicazioni multi-modali e multi-modello, consideriamo la performance come la capacità del sistema di soddisfare le aspettative tue e dei tuoi utenti, inclusa la non generazione di output dannosi. È importante valutare la performance complessiva della tua applicazione utilizzando [Valutatori di Performance e Qualità e di Rischi e Sicurezza](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Hai anche la possibilità di creare e valutare con [valutatori personalizzati](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Puoi valutare la tua applicazione AI nel tuo ambiente di sviluppo utilizzando l'[Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Dato un dataset di test o un obiettivo, le generazioni della tua applicazione AI generativa vengono misurate quantitativamente con valutatori integrati o personalizzati a tua scelta. Per iniziare con l'Azure AI Evaluation SDK per valutare il tuo sistema, puoi seguire la [guida introduttiva](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Una volta eseguita una valutazione, puoi [visualizzare i risultati in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marchi

Questo progetto potrebbe contenere marchi o loghi relativi a progetti, prodotti o servizi. L'uso autorizzato dei marchi o loghi Microsoft è soggetto e deve seguire le [Linee guida sui marchi e sul brand di Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
L'uso dei marchi o loghi Microsoft in versioni modificate di questo progetto non deve causare confusione o implicare sponsorizzazione da parte di Microsoft. Qualsiasi utilizzo di marchi o loghi di terze parti è soggetto alle politiche di tali terze parti.

## Ottenere Aiuto

Se hai difficoltà o domande sulla creazione di app AI, unisciti a:

[![Discord Azure AI Foundry](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Se hai feedback sui prodotti o riscontri errori durante la creazione, visita:

[![Forum degli sviluppatori Azure AI Foundry](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.