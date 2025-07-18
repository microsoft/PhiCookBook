<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c07bb4c3c89a36c9be332a065a9a33c",
  "translation_date": "2025-07-16T15:30:19+00:00",
  "source_file": "README.md",
  "language_code": "ro"
}
-->
# Phi Cookbook: Exemple practice cu modelele Phi de la Microsoft

[![Deschide și folosește exemplele în GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![Deschide în Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Contribuitori GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![Probleme GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![Pull requests GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Urmăritori GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![Fork-uri GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![Stele GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi este o serie de modele AI open source dezvoltate de Microsoft.

Phi este în prezent cel mai puternic și eficient model mic de limbaj (SLM), cu performanțe foarte bune în multiple limbi, raționament, generare de text/chat, programare, imagini, audio și alte scenarii.

Poți implementa Phi în cloud sau pe dispozitive edge și poți construi cu ușurință aplicații AI generative cu resurse limitate de calcul.

Urmează acești pași pentru a începe să folosești aceste resurse:  
1. **Fă fork la repository**: Click pe [![Fork-uri GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **Clonează repository-ul**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Alătură-te comunității Microsoft AI pe Discord și întâlnește experți și alți dezvoltatori**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.ro.png)

### 🌐 Suport multilingv

#### Suportat prin GitHub Action (automatizat și mereu actualizat)

[Franceză](../fr/README.md) | [Spaniolă](../es/README.md) | [Germană](../de/README.md) | [Rusă](../ru/README.md) | [Arabă](../ar/README.md) | [Persană (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chineză (simplificată)](../zh/README.md) | [Chineză (tradițională, Macau)](../mo/README.md) | [Chineză (tradițională, Hong Kong)](../hk/README.md) | [Chineză (tradițională, Taiwan)](../tw/README.md) | [Japoneză](../ja/README.md) | [Coreeană](../ko/README.md) | [Hindi](../hi/README.md)  
[Bengaleză](../bn/README.md) | [Marathi](../mr/README.md) | [Nepaleză](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portugheză (Portugalia)](../pt/README.md) | [Portugheză (Brazilia)](../br/README.md) | [Italiană](../it/README.md) | [Poloneză](../pl/README.md) | [Turcă](../tr/README.md) | [Greacă](../el/README.md) | [Thailandeză](../th/README.md) | [Suedeză](../sv/README.md) | [Daneză](../da/README.md) | [Norvegiană](../no/README.md) | [Finlandeză](../fi/README.md) | [Olandeză](../nl/README.md) | [Ebraică](../he/README.md) | [Vietnameză](../vi/README.md) | [Indoneziană](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipineză)](../tl/README.md) | [Swahili](../sw/README.md) | [Maghiară](../hu/README.md) | [Cehă](../cs/README.md) | [Slovacă](../sk/README.md) | [Română](./README.md) | [Bulgară](../bg/README.md) | [Sârbă (chirilică)](../sr/README.md) | [Croată](../hr/README.md) | [Slovenă](../sl/README.md)

## Cuprins

- Introducere  
  - [Bine ai venit în familia Phi](./md/01.Introduction/01/01.PhiFamily.md)  
  - [Configurarea mediului tău](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [Înțelegerea tehnologiilor cheie](./md/01.Introduction/01/01.Understandingtech.md)  
  - [Siguranța AI pentru modelele Phi](./md/01.Introduction/01/01.AISafety.md)  
  - [Suport hardware Phi](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [Modele Phi & disponibilitate pe platforme](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [Folosirea Guidance-ai și Phi](./md/01.Introduction/01/01.Guidance.md)  
  - [Modele din GitHub Marketplace](https://github.com/marketplace/models)  
  - [Catalogul modelelor Azure AI](https://ai.azure.com)

- Inferență Phi în diferite medii  
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)  
    -  [Modele GitHub](./md/01.Introduction/02/02.GitHubModel.md)  
    -  [Catalogul modelelor Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)  
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)  
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)  
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Inferență Phi Family  
    - [Inferență Phi pe iOS](./md/01.Introduction/03/iOS_Inference.md)  
    - [Inferență Phi pe Android](./md/01.Introduction/03/Android_Inference.md)  
    - [Inferență Phi pe Jetson](./md/01.Introduction/03/Jetson_Inference.md)  
    - [Inferență Phi pe AI PC](./md/01.Introduction/03/AIPC_Inference.md)  
    - [Inferență Phi cu Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)  
    - [Inferență Phi pe server local](./md/01.Introduction/03/Local_Server_Inference.md)  
    - [Inferență Phi pe server remote folosind AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)  
    - [Inferență Phi cu Rust](./md/01.Introduction/03/Rust_Inference.md)  
    - [Inferență Phi--Vision local](./md/01.Introduction/03/Vision_Inference.md)  
    - [Inferență Phi cu Kaito AKS, Azure Containers (suport oficial)](./md/01.Introduction/03/Kaito_Inference.md)  
-  [Cuantificarea Phi Family](./md/01.Introduction/04/QuantifyingPhi.md)  
    - [Cuantificarea Phi-3.5 / 4 folosind llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
    - [Cuantificarea Phi-3.5 / 4 folosind extensii Generative AI pentru onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
    - [Cuantificarea Phi-3.5 / 4 folosind Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
    - [Cuantificarea Phi-3.5 / 4 folosind Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Evaluarea Phi  
    - [AI Responsabil](./md/01.Introduction/05/ResponsibleAI.md)  
    - [Azure AI Foundry pentru evaluare](./md/01.Introduction/05/AIFoundry.md)  
    - [Folosirea Promptflow pentru evaluare](./md/01.Introduction/05/Promptflow.md)

- RAG cu Azure AI Search  
    - [Cum să folosești Phi-4-mini și Phi-4-multimodal (RAG) cu Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Exemple de dezvoltare aplicații Phi  
  - Aplicații text & chat  
    - Exemple Phi-4 🆕  
      - [📓] [Chat cu modelul Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Chat cu modelul local Phi-4 ONNX .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [Aplicație console Chat .NET cu Phi-4 ONNX folosind Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Exemple Phi-3 / 3.5  
      - [Chatbot local în browser folosind Phi3, ONNX Runtime Web și WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [Chat OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [Model multiplu - Phi-3-mini interactiv și OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - Construirea unui wrapper și folosirea Phi-3 cu MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [Optimizarea modelului - Cum să optimizezi modelul Phi-3-mini pentru ONNX Runtime Web cu Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [Aplicație WinUI3 cu Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [Exemplu aplicație WinUI3 Multi Model AI Powered Notes](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Ajustarea fină și integrarea modelelor personalizate Phi-3 cu Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Ajustarea fină și integrarea modelelor personalizate Phi-3 cu Prompt flow în Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Evaluarea modelului Phi-3 / Phi-3.5 ajustat fin în Azure AI Foundry, cu accent pe principiile AI responsabile ale Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Exemplu de predicție lingvistică Phi-3.5-mini-instruct (chineză/engleză)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Chatbot Phi-3.5-Instruct WebGPU RAG](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Folosirea GPU-ului Windows pentru a crea o soluție Prompt flow cu Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Folosirea Microsoft Phi-3.5 tflite pentru a crea o aplicație Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Exemplu Q&A .NET folosind modelul local ONNX Phi-3 cu Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Aplicație console chat .NET cu Semantic Kernel și Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Exemple bazate pe cod Azure AI Inference SDK  
  - Exemple Phi-4 🆕  
    - [📓] [Generarea codului proiectului folosind Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Exemple Phi-3 / 3.5  
    - [Construiește-ți propriul Visual Studio Code GitHub Copilot Chat cu familia Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [Creează-ți propriul agent Chat Copilot pentru Visual Studio Code cu Phi-3.5 folosind modelele GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- Exemple de raționament avansat  
  - Exemple Phi-4 🆕  
    - [📓] [Exemple Phi-4-mini-reasoning sau Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Ajustarea fină a Phi-4-mini-reasoning cu Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Ajustarea fină a Phi-4-mini-reasoning cu Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Phi-4-mini-reasoning cu modelele GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Phi-4-mini-reasoning cu modelele Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- Demo-uri  
    - [Demo-uri Phi-4-mini găzduite pe Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Demo-uri Phi-4-multimodal găzduite pe Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- Exemple Vision  
  - Exemple Phi-4 🆕  
    - [📓] [Folosește Phi-4-multimodal pentru a citi imagini și a genera cod](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Exemple Phi-3 / 3.5  
    - [📓][Phi-3-vision-Text din imagine în text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - Asistent vizual lingvistic - cu Phi3-Vision și OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision exemplu multi-frame sau multi-imagine](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Model local Phi-3 Vision ONNX folosind Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Model local Phi-3 Vision ONNX bazat pe meniu folosind Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- Exemple Matematică  
  - Exemple Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [Demo matematică cu Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)  

- Exemple Audio  
  - Exemple Phi-4 🆕  
    - [📓] [Extracția transcrierilor audio folosind Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Exemplu audio Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Exemplu de traducere vocală Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [Aplicație console .NET folosind Phi-4-multimodal Audio pentru a analiza un fișier audio și a genera transcriere](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- Exemple MOE  
  - Exemple Phi-3 / 3.5  
    - [📓] [Exemplu Phi-3.5 Mixture of Experts Models (MoEs) pentru Social Media](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [Construirea unui pipeline Retrieval-Augmented Generation (RAG) cu NVIDIA NIM Phi-3 MOE, Azure AI Search și LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- Exemple Function Calling  
  - Exemple Phi-4 🆕  
    - [📓] [Folosirea Function Calling cu Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Folosirea Function Calling pentru a crea multi-agenti cu Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Folosirea Function Calling cu Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [Folosirea Function Calling cu ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- Exemple Multimodal Mixing  
  - Exemple Phi-4 🆕  
    - [📓] [Folosirea Phi-4-multimodal ca jurnalist de tehnologie](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [Aplicație console .NET folosind Phi-4-multimodal pentru a analiza imagini](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Ajustarea fină a modelelor Phi  
  - [Scenarii de ajustare fină](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [Ajustare fină vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Ajustarea fină pentru a transforma Phi-3 într-un expert în industrie](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [Ajustarea fină a Phi-3 cu AI Toolkit pentru VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Ajustarea fină a Phi-3 cu Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Ajustarea fină a Phi-3 cu Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [Ajustarea fină a Phi-3 cu QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Ajustarea fină a Phi-3 cu Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Ajustarea fină a Phi-3 cu Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Ajustarea fină cu Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Laborator practic de ajustare fină cu Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)  
  - [Ajustarea fină a Phi-3-vision cu Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Ajustarea fină a Phi-3 cu Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Ajustarea fină a Phi-3-vision (suport oficial)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Ajustarea fină a Phi-3 cu Kaito AKS, Azure Containers (suport oficial)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Ajustarea fină a Phi-3 și 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- Laborator practic  
  - [Explorarea modelelor de ultimă generație: LLM-uri, SLM-uri, dezvoltare locală și altele](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [Dezvoltarea potențialului NLP: Ajustare fină cu Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- Lucrări și publicații academice  
  - [Textbooks Are All You Need II: raport tehnic phi-1.5](https://arxiv.org/abs/2309.05463)  
  - [Raport tehnic Phi-3: un model lingvistic foarte capabil local pe telefonul tău](https://arxiv.org/abs/2404.14219)  
  - [Raport tehnic Phi-4](https://arxiv.org/abs/2412.08905)  
  - [Raport tehnic Phi-4-Mini: modele multimodale compacte, dar puternice, prin Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [Optimizarea modelelor lingvistice mici pentru Function-Calling în vehicule](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) Ajustarea fină PHI-3 pentru răspunsuri la întrebări cu alegere multiplă: metodologie, rezultate și provocări](https://arxiv.org/abs/2501.01588)
- [Raport Tehnic Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Raport Tehnic Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Utilizarea modelelor Phi

### Phi pe Azure AI Foundry

Poți învăța cum să folosești Microsoft Phi și cum să construiești soluții E2E pe diferitele tale dispozitive hardware. Pentru a experimenta Phi personal, începe prin a testa modelele și a personaliza Phi pentru scenariile tale folosind [Catalogul de modele Azure AI Foundry](https://aka.ms/phi3-azure-ai). Poți afla mai multe din Ghidul de început cu [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Playground**  
Fiecare model are un spațiu dedicat pentru testare, [Azure AI Playground](https://aka.ms/try-phi3).

### Phi pe modelele GitHub

Poți învăța cum să folosești Microsoft Phi și cum să construiești soluții E2E pe diferitele tale dispozitive hardware. Pentru a experimenta Phi personal, începe prin a testa modelul și a personaliza Phi pentru scenariile tale folosind [Catalogul de modele GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Poți afla mai multe din Ghidul de început cu [Catalogul de modele GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Playground**  
Fiecare model are un [spațiu dedicat pentru testare](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi pe Hugging Face

De asemenea, poți găsi modelul pe [Hugging Face](https://huggingface.co/microsoft).

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Inteligență Artificială Responsabilă

Microsoft este dedicat să ajute clienții să folosească produsele noastre AI în mod responsabil, împărtășind experiențele noastre și construind parteneriate bazate pe încredere prin instrumente precum Transparency Notes și Impact Assessments. Multe dintre aceste resurse pot fi găsite la [https://aka.ms/RAI](https://aka.ms/RAI).  
Abordarea Microsoft privind AI responsabilă se bazează pe principiile noastre AI de corectitudine, fiabilitate și siguranță, confidențialitate și securitate, incluziune, transparență și responsabilitate.

Modelele de limbaj natural, imagine și vorbire la scară largă – precum cele folosite în acest exemplu – pot avea comportamente nedrepte, nesigure sau ofensatoare, cauzând astfel daune. Te rugăm să consulți [nota de transparență a serviciului Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) pentru a fi informat despre riscuri și limitări.

Abordarea recomandată pentru a reduce aceste riscuri este să incluzi un sistem de siguranță în arhitectura ta care să poată detecta și preveni comportamentele dăunătoare. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) oferă un strat independent de protecție, capabil să detecteze conținut dăunător generat de utilizatori sau de AI în aplicații și servicii. Azure AI Content Safety include API-uri pentru text și imagine care permit detectarea materialelor dăunătoare. În cadrul Azure AI Foundry, serviciul Content Safety îți permite să vizualizezi, să explorezi și să testezi coduri exemplu pentru detectarea conținutului dăunător în diferite modalități. Următoarea [documentație quickstart](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) te ghidează în realizarea cererilor către serviciu.

Un alt aspect de luat în considerare este performanța generală a aplicației. În aplicațiile multi-modale și multi-modele, performanța înseamnă că sistemul funcționează așa cum te aștepți tu și utilizatorii tăi, inclusiv să nu genereze rezultate dăunătoare. Este important să evaluezi performanța aplicației tale folosind [evaluatori de Performanță, Calitate, Risc și Siguranță](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). De asemenea, ai posibilitatea să creezi și să evaluezi cu [evaluatori personalizați](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Poți evalua aplicația ta AI în mediul de dezvoltare folosind [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Având un set de date de test sau un obiectiv, generațiile aplicației tale AI generative sunt măsurate cantitativ cu evaluatori încorporați sau evaluatori personalizați la alegere. Pentru a începe cu Azure AI Evaluation SDK și a evalua sistemul tău, poți urma [ghidul quickstart](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). După ce execuți o rulare de evaluare, poți [vizualiza rezultatele în Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Mărci înregistrate

Acest proiect poate conține mărci comerciale sau logo-uri pentru proiecte, produse sau servicii. Utilizarea autorizată a mărcilor comerciale sau logo-urilor Microsoft este supusă și trebuie să respecte [Ghidul Microsoft privind Mărcile Comerciale și Brandul](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Utilizarea mărcilor comerciale sau logo-urilor Microsoft în versiuni modificate ale acestui proiect nu trebuie să creeze confuzie sau să sugereze sponsorizarea Microsoft. Orice utilizare a mărcilor comerciale sau logo-urilor terțe este supusă politicilor acelor terțe părți.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.