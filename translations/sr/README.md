<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c07bb4c3c89a36c9be332a065a9a33c",
  "translation_date": "2025-07-16T15:32:16+00:00",
  "source_file": "README.md",
  "language_code": "sr"
}
-->
# Phi Cookbook: Практични примери са Microsoft-овим Phi моделима

[![Отворите и користите примере у GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![Отворите у Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub сарадници](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub проблеми](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub pull-захтеви](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub пратиоци](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub форкови](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub звезде](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi је серија open source AI модела које је развио Microsoft.

Phi је тренутно најмоћнији и најисплативији мали језички модел (SLM), са одличним резултатима у вишејезичности, резоновању, генерисању текста/четова, програмирању, сликама, аудију и другим сценаријима.

Можете да имплементирате Phi у облак или на edge уређаје, и лако градите генеративне AI апликације чак и са ограниченом рачунарском снагом.

Пратите ове кораке да бисте почели да користите ове ресурсе:  
1. **Форкујте репозиторијум**: Кликните [![GitHub форкови](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **Клонирајте репозиторијум**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Придружите се Microsoft AI Discord заједници и упознајте стручњаке и друге програмере**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.sr.png)

### 🌐 Подршка за више језика

#### Подржано преко GitHub Action (аутоматски и увек ажурирано)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md)  
[Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](./README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)

## Садржај

- Увод  
  - [Добродошли у Phi породицу](./md/01.Introduction/01/01.PhiFamily.md)  
  - [Подешавање окружења](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [Разумевање кључних технологија](./md/01.Introduction/01/01.Understandingtech.md)  
  - [AI безбедност за Phi моделе](./md/01.Introduction/01/01.AISafety.md)  
  - [Подршка за Phi хардвер](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [Phi модели и доступност на платформама](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [Коришћење Guidance-ai и Phi](./md/01.Introduction/01/01.Guidance.md)  
  - [GitHub Marketplace модели](https://github.com/marketplace/models)  
  - [Azure AI каталог модела](https://ai.azure.com)

- Инференција Phi у различитим окружењима  
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)  
    -  [GitHub модели](./md/01.Introduction/02/02.GitHubModel.md)  
    -  [Azure AI Foundry каталог модела](./md/01.Introduction/02/03.AzureAIFoundry.md)  
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)  
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)  
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Инференција Phi породице  
    - [Инференција Phi на iOS](./md/01.Introduction/03/iOS_Inference.md)  
    - [Инференција Phi на Android](./md/01.Introduction/03/Android_Inference.md)  
    - [Инференција Phi на Jetson-у](./md/01.Introduction/03/Jetson_Inference.md)  
    - [Инференција Phi на AI PC-у](./md/01.Introduction/03/AIPC_Inference.md)  
    - [Инференција Phi са Apple MLX Framework-ом](./md/01.Introduction/03/MLX_Inference.md)  
    - [Инференција Phi на локалном серверу](./md/01.Introduction/03/Local_Server_Inference.md)  
    - [Инференција Phi на удаљеном серверу користећи AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)  
    - [Инференција Phi са Rust-ом](./md/01.Introduction/03/Rust_Inference.md)  
    - [Инференција Phi--Vision локално](./md/01.Introduction/03/Vision_Inference.md)  
    - [Инференција Phi са Kaito AKS, Azure Containers (званична подршка)](./md/01.Introduction/03/Kaito_Inference.md)  
-  [Квантификација Phi породице](./md/01.Introduction/04/QuantifyingPhi.md)  
    - [Квантификација Phi-3.5 / 4 користећи llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
    - [Квантификација Phi-3.5 / 4 користећи Generative AI екстензије за onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
    - [Квантификација Phi-3.5 / 4 користећи Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
    - [Квантификација Phi-3.5 / 4 користећи Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Евалуација Phi  
    - [Одговорни AI](./md/01.Introduction/05/ResponsibleAI.md)  
    - [Azure AI Foundry за евалуацију](./md/01.Introduction/05/AIFoundry.md)  
    - [Коришћење Promptflow за евалуацију](./md/01.Introduction/05/Promptflow.md)

- RAG са Azure AI Search  
    - [Како користити Phi-4-mini и Phi-4-multimodal (RAG) са Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Примери развоја Phi апликација  
  - Текст и чет апликације  
    - Phi-4 примери 🆕  
      - [📓] [Ћаскање са Phi-4-mini ONNX моделом](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Ћаскање са Phi-4 локалним ONNX моделом .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [Ћаскање .NET конзолна апликација са Phi-4 ONNX користећи Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 примери  
      - [Локални четбот у прегледачу користећи Phi3, ONNX Runtime Web и WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [OpenVino чет](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [Више модела - интерактивни Phi-3-mini и OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - прављење wrapper-а и коришћење Phi-3 са MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [Оптимизација модела - како оптимизовати Phi-3-mini модел за ONNX Runtime Web са Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [WinUI3 апликација са Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [WinUI3 Multi Model AI Powered Notes App пример](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Фино подешавање и интеграција прилагођених Phi-3 модела са Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Фино подешавање и интеграција прилагођених Phi-3 модела са Prompt flow у Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Евалуација фино подешеног Phi-3 / Phi-3.5 модела у Azure AI Foundry са фокусом на Microsoft-ове принципе одговорног AI](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Пример предвиђања језика Phi-3.5-mini-instruct (кинески/енглески)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG Чатбот](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Коришћење Windows GPU за креирање Prompt flow решења са Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Коришћење Microsoft Phi-3.5 tflite за креирање Android апликације](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Q&A .NET пример коришћења локалног ONNX Phi-3 модела уз Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Конзолна .NET апликација за ћаскање са Semantic Kernel и Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK примери засновани на коду  
  - Phi-4 примери 🆕  
    - [📓] [Генерисање кода пројекта користећи Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Phi-3 / 3.5 примери  
    - [Креирајте свој Visual Studio Code GitHub Copilot Chat са Microsoft Phi-3 породицом](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [Креирајте свог Visual Studio Code Chat Copilot агента са Phi-3.5 користећи GitHub моделе](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- Напредни примери резоновања  
  - Phi-4 примери 🆕  
    - [📓] [Phi-4-mini-reasoning или Phi-4-reasoning примери](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Фино подешавање Phi-4-mini-reasoning са Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Фино подешавање Phi-4-mini-reasoning са Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Phi-4-mini-reasoning са GitHub моделима](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Phi-4-mini-reasoning са Azure AI Foundry моделима](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- Демонстрације  
    - [Phi-4-mini демонстрације хостоване на Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Phi-4-multimodal демонстрације хостоване на Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- Визуелни примери  
  - Phi-4 примери 🆕  
    - [📓] [Коришћење Phi-4-multimodal за читање слика и генерисање кода](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Phi-3 / 3.5 примери  
    - [📓][Phi-3-vision-Image текст у текст](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP уграђивање](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [ДЕМО: Phi-3 рециклирање](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - Визуелни језички асистент - са Phi3-Vision и OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision пример са више кадрова или више слика](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Phi-3 Vision локални ONNX модел користећи Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Мени засновани Phi-3 Vision локални ONNX модел користећи Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- Математички примери  
  - Phi-4-Mini-Flash-Reasoning-Instruct примери 🆕 [Математички демо са Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)  

- Аудио примери  
  - Phi-4 примери 🆕  
    - [📓] [Извлачење аудио транскрипата користећи Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Phi-4-multimodal аудио пример](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Phi-4-multimodal пример превода говора](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [.NET конзолна апликација користећи Phi-4-multimodal аудио за анализу аудио фајла и генерисање транскрипта](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- MOE примери  
  - Phi-3 / 3.5 примери  
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) пример за друштвене мреже](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [Креирање Retrieval-Augmented Generation (RAG) пипелина са NVIDIA NIM Phi-3 MOE, Azure AI Search и LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- Примери позива функција  
  - Phi-4 примери 🆕  
    - [📓] [Коришћење Function Calling са Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Коришћење Function Calling за креирање мулти-агената са Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Коришћење Function Calling са Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [Коришћење Function Calling са ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- Примери мултимодалног мешања  
  - Phi-4 примери 🆕  
    - [📓] [Коришћење Phi-4-multimodal као технолошког новинара](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [.NET конзолна апликација користећи Phi-4-multimodal за анализу слика](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Фино подешавање Phi примера  
  - [Сценарији фино подешавања](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [Фино подешавање у односу на RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Фино подешавање: Нека Phi-3 постане индустријски стручњак](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [Фино подешавање Phi-3 са AI Toolkit за VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Фино подешавање Phi-3 са Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Фино подешавање Phi-3 са Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [Фино подешавање Phi-3 са QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Фино подешавање Phi-3 са Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Фино подешавање Phi-3 са Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Фино подешавање са Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Hands-On лабораторија за фино подешавање са Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)  
  - [Фино подешавање Phi-3-vision са Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Фино подешавање Phi-3 са Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Фино подешавање Phi-3-vision (званична подршка)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Фино подешавање Phi-3 са Kaito AKS, Azure Containers (званична подршка)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Фино подешавање Phi-3 и 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- Hands on Lab  
  - [Истраживање најсавременијих модела: LLM, SLM, локални развој и више](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [Откључавање потенцијала NLP: Фино подешавање са Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- Академски истраживачки радови и публикације  
  - [Textbooks Are All You Need II: phi-1.5 технички извештај](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 технички извештај: Високо способан језички модел локално на вашем телефону](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 технички извештај](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini технички извештај: Компактан али моћан мултимодални језички модел преко Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [Оптимизација малих језичких модела за позив функција у возилу](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) Фино подешавање PHI-3 за одговарање на питања са више избора: Методологија, резултати и изазови](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning Technical Report](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-reasoning Technical Report](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Коришћење Phi модела

### Phi на Azure AI Foundry

Можете научити како да користите Microsoft Phi и како да направите E2E решења на различитим хардверским уређајима. Да бисте сами испробали Phi, почните тако што ћете се играти моделима и прилагодити Phi за своје сценарије користећи [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Више информација можете пронаћи у упутству за почетак рада са [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Playground**  
Сваки модел има посебан playground за тестирање модела [Azure AI Playground](https://aka.ms/try-phi3).

### Phi на GitHub моделима

Можете научити како да користите Microsoft Phi и како да направите E2E решења на различитим хардверским уређајима. Да бисте сами испробали Phi, почните тако што ћете се играти моделом и прилагодити Phi за своје сценарије користећи [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Више информација можете пронаћи у упутству за почетак рада са [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Playground**  
Сваки модел има посебан [playground за тестирање модела](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi на Hugging Face

Модел можете пронаћи и на [Hugging Face](https://huggingface.co/microsoft).

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Одговорни AI

Microsoft је посвећен томе да помогне својим корисницима да одговорно користе наше AI производе, делећи своја сазнања и градећи партнерства заснована на поверењу кроз алате као што су Transparency Notes и Impact Assessments. Многи од ових ресурса доступни су на [https://aka.ms/RAI](https://aka.ms/RAI).  
Приступ Microsoft-а одговорном AI заснован је на нашим AI принципима правичности, поузданости и безбедности, приватности и сигурности, инклузивности, транспарентности и одговорности.

Велики модели за природни језик, слике и говор – као што су они коришћени у овом примеру – могу потенцијално да се понашају на начине који нису праведни, поуздани или који могу бити увредљиви, што може изазвати штету. Молимо вас да консултујете [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) како бисте били информисани о ризицима и ограничењима.

Препоручени приступ за смањење ових ризика је да у архитектуру укључите систем безбедности који може да открије и спречи штетно понашање. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) пружа независни слој заштите, способан да открије штетни садржај који корисници или AI генеришу у апликацијама и услугама. Azure AI Content Safety укључује API-је за текст и слике који вам омогућавају да откријете штетни материјал. У оквиру Azure AI Foundry, сервис Content Safety вам омогућава да прегледате, истражујете и испробате пример кода за откривање штетног садржаја у различитим модалитетима. Следећа [quickstart документација](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) вас води кроз процес слања захтева сервису.

Још један аспект који треба узети у обзир је укупна перформанса апликације. Код мултимодалних и мултимоделских апликација, перформансе подразумевају да систем ради онако како ви и ваши корисници очекујете, укључујући и то да не генерише штетне излазе. Важно је проценити перформансе ваше апликације користећи [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Такође имате могућност да креирате и процењујете помоћу [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Можете проценити своју AI апликацију у развојном окружењу користећи [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Уз тест скуп података или циљ, генерације ваше генеративне AI апликације се квантитативно мере уграђеним или прилагођеним евалуаторима по вашем избору. Да бисте почели са azure ai evaluation sdk за процену вашег система, можете пратити [quickstart водич](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Када извршите процену, можете [визуализовати резултате у Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Заштитни знаци

Овај пројекат може садржати заштитне знакове или логотипе пројеката, производа или услуга. Овлашћена употреба Microsoft заштитних знакова или логотипа подлеже и мора се придржавати [Microsoft-ових смерница за заштитне знакове и бренд](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Употреба Microsoft заштитних знакова или логотипа у модификованим верзијама овог пројекта не сме изазивати забуну нити имплицирати да Microsoft сponзориše пројекат. Свака употреба заштитних знакова или логотипа трећих страна подлеже правилима тих трећих страна.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.