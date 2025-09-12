<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T14:16:30+00:00",
  "source_file": "README.md",
  "language_code": "sr"
}
-->
# Phi Кувар: Практични Примери са Microsoft-овим Phi Моделима

Phi је серија отворених AI модела које је развио Microsoft.

Phi је тренутно најмоћнији и најисплативији мали језички модел (SLM), са одличним резултатима у вишејезичности, резоновању, генерисању текста/ћаскања, кодирању, сликама, аудио и другим сценаријима.

Можете да примените Phi у облаку или на уређајима на ивици мреже, и лако можете да изградите генеративне AI апликације са ограниченом рачунарском снагом.

Пратите ове кораке да бисте започели коришћење ових ресурса:
1. **Fork-ујте Репозиторијум**: Кликните [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Клонирајте Репозиторијум**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Придружите се Microsoft AI Discord Заједници и упознајте стручњаке и друге програмере**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 Подршка за више језика

#### Подржано преко GitHub Action-а (Аутоматски и увек ажурирано)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) 
[Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](./README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)

## Садржај

- Увод
  - [Добродошли у Phi породицу](./md/01.Introduction/01/01.PhiFamily.md)
  - [Подешавање вашег окружења](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Разумевање кључних технологија](./md/01.Introduction/01/01.Understandingtech.md)
  - [AI Безбедност за Phi моделе](./md/01.Introduction/01/01.AISafety.md)
  - [Подршка за Phi хардвер](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi модели и доступност на различитим платформама](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Коришћење Guidance-ai и Phi](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace Модели](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- Инференција Phi у различитим окружењима
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub Модели](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Инференција Phi породице
    - [Инференција Phi на iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Инференција Phi на Android](./md/01.Introduction/03/Android_Inference.md)
    - [Инференција Phi на Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Инференција Phi на AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Инференција Phi са Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Инференција Phi на локалном серверу](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Инференција Phi на удаљеном серверу користећи AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Инференција Phi са Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Инференција Phi--Vision локално](./md/01.Introduction/03/Vision_Inference.md)
    - [Инференција Phi са Kaito AKS, Azure Containers (званична подршка)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Квантификација Phi породице](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Квантификација Phi-3.5 / 4 користећи llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Квантификација Phi-3.5 / 4 користећи генеративне AI екстензије за onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Квантификација Phi-3.5 / 4 користећи Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Квантификација Phi-3.5 / 4 користећи Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Евалуација Phi
    - [Одговорна AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry за евалуацију](./md/01.Introduction/05/AIFoundry.md)
    - [Коришћење Promptflow за евалуацију](./md/01.Introduction/05/Promptflow.md)
 
- RAG са Azure AI Search
    - [Како користити Phi-4-mini и Phi-4-multimodal (RAG) са Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Примери развоја Phi апликација
  - Текст & Ћаскање Апликације
    - Phi-4 Примери 🆕
      - [📓] [Ћаскање са Phi-4-mini ONNX моделом](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Ћаскање са Phi-4 локалним ONNX моделом .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Ћаскање .NET Console App са Phi-4 ONNX користећи Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 Примери
      - [Локални chatbot у прегледачу користећи Phi3, ONNX Runtime Web и WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Ћаскање](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Мулти Модел - Интерактивни Phi-3-mini и OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Изградња омотача и коришћење Phi-3 са MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Оптимизација модела - Како оптимизовати Phi-3-min модел за ONNX Runtime Web са Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 Апликација са Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3 Мулти Модел AI Powered Notes Апликација Пример](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Фино подешавање и интеграција прилагођених Phi-3 модела са Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)  
- [Фино подешавање и интеграција прилагођених Phi-3 модела са Prompt flow у Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)  
- [Евалуација фино подешаног Phi-3 / Phi-3.5 модела у Azure AI Foundry са фокусом на принципе одговорне AI технологије компаније Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)  
- [📓] [Phi-3.5-mini-instruct пример предвиђања језика (кинески/енглески)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)  
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)  
- [Коришћење Windows GPU за креирање Prompt flow решења са Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)  
- [Коришћење Microsoft Phi-3.5 tflite за креирање Android апликације](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)  
- [Q&A .NET пример коришћењем локалног ONNX Phi-3 модела уз Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)  
- [Конзолна апликација за ћаскање у .NET са Semantic Kernel и Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)  

- Azure AI Inference SDK узорци кода  
  - Phi-4 узорци 🆕  
    - [📓] [Генерисање кода пројекта коришћењем Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Phi-3 / 3.5 узорци  
    - [Креирајте свој Visual Studio Code GitHub Copilot Chat уз Microsoft Phi-3 породицу](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [Креирајте свој Visual Studio Code Chat Copilot Agent уз Phi-3.5 и GitHub моделе](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- Напредни узорци резоновања  
  - Phi-4 узорци 🆕  
    - [📓] [Phi-4-mini-reasoning или Phi-4-reasoning узорци](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Фино подешавање Phi-4-mini-reasoning уз Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Фино подешавање Phi-4-mini-reasoning уз Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Phi-4-mini-reasoning уз GitHub моделе](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Phi-4-mini-reasoning уз Azure AI Foundry моделе](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- Демонстрације  
    - [Phi-4-mini демонстрације хостоване на Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Phi-4-multimodal демонстрације хостоване на Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- Узорци за визију  
  - Phi-4 узорци 🆕  
    - [📓] [Коришћење Phi-4-multimodal за читање слика и генерисање кода](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Phi-3 / 3.5 узорци  
    - [📓][Phi-3-vision-Image текст у текст](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [ДЕМОНСТРАЦИЈА: Phi-3 Рециклирање](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - Визуелни језички асистент - уз Phi3-Vision и OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision узорак за више кадрова или више слика](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Phi-3 Vision локални ONNX модел уз Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Мени базирани Phi-3 Vision локални ONNX модел уз Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- Узорци за математику  
  - Phi-4-Mini-Flash-Reasoning-Instruct узорци 🆕 [Демонстрација математике уз Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)  

- Узорци за аудио  
  - Phi-4 узорци 🆕  
    - [📓] [Екстракција транскрипта аудио записа уз Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Phi-4-multimodal аудио узорак](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Phi-4-multimodal узорак за превод говора](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [.NET конзолна апликација уз Phi-4-multimodal за анализу аудио записа и генерисање транскрипта](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- MOE узорци  
  - Phi-3 / 3.5 узорци  
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) узорак за друштвене мреже](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [Изградња Retrieval-Augmented Generation (RAG) система уз NVIDIA NIM Phi-3 MOE, Azure AI Search и LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- Узорци за позивање функција  
  - Phi-4 узорци 🆕  
    - [📓] [Коришћење позивања функција уз Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Коришћење позивања функција за креирање више агената уз Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Коришћење позивања функција уз Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [Коришћење позивања функција уз ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- Узорци за мешање мултимодалних података  
  - Phi-4 узорци 🆕  
    - [📓] [Коришћење Phi-4-multimodal као технолошки новинар](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [.NET конзолна апликација уз Phi-4-multimodal за анализу слика](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Фино подешавање Phi узорака  
  - [Сценарији фино подешавања](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [Фино подешавање vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Фино подешавање: Нека Phi-3 постане индустријски експерт](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [Фино подешавање Phi-3 уз AI Toolkit за VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Фино подешавање Phi-3 уз Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Фино подешавање Phi-3 уз Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [Фино подешавање Phi-3 уз QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Фино подешавање Phi-3 уз Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Фино подешавање Phi-3 уз Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Фино подешавање уз Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Фино подешавање уз Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)  
  - [Фино подешавање Phi-3-vision уз Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Фино подешавање Phi-3 уз Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Фино подешавање Phi-3-vision (званична подршка)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Фино подешавање Phi-3 уз Kaito AKS, Azure Containers (званична подршка)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Фино подешавање Phi-3 и 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- Практична лабораторија  
  - [Истраживање најсавременијих модела: LLMs, SLMs, локални развој и више](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [Откључавање NLP потенцијала: Фино подешавање уз Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- Академски истраживачки радови и публикације  
  - [Textbooks Are All You Need II: phi-1.5 технички извештај](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 технички извештај: Високо способан језички модел локално на вашем телефону](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 технички извештај](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini технички извештај: Компактни али моћни мултимодални језички модели уз Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [Оптимизација малих језичких модела за позивање функција у возилу](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) Фино подешавање PHI-3 за одговарање на питања са вишеструким избором: Методологија, резултати и изазови](https://arxiv.org/abs/2501.01588)  
- [Phi-4-reasoning Технички извештај](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning Технички извештај](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)  

## Коришћење Phi модела  

### Phi на Azure AI Foundry  

Можете научити како да користите Microsoft Phi и како да изградите E2E решења на различитим хардверским уређајима. Да бисте сами искусили Phi, започните тестирањем модела и прилагођавањем Phi за ваше сценарије користећи [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Више информација можете пронаћи у одељку [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).  

**Playground**  
Сваки модел има посебан playground за тестирање модела [Azure AI Playground](https://aka.ms/try-phi3).  

### Phi на GitHub Models  

Можете научити како да користите Microsoft Phi и како да изградите E2E решења на различитим хардверским уређајима. Да бисте сами искусили Phi, започните тестирањем модела и прилагођавањем Phi за ваше сценарије користећи [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Више информација можете пронаћи у одељку [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).  

**Playground**  
Сваки модел има посебан [playground за тестирање модела](/md/02.QuickStart/GitHubModel_QuickStart.md).  

### Phi на Hugging Face  

Модел можете пронаћи и на [Hugging Face](https://huggingface.co/microsoft).  

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct).  

## Одговорна употреба AI  

Microsoft је посвећен помагању својим корисницима да одговорно користе наше AI производе, делећи своја искуства и градећи партнерства заснована на поверењу кроз алате као што су Transparency Notes и Impact Assessments. Многи од ових ресурса могу се пронаћи на [https://aka.ms/RAI](https://aka.ms/RAI).  
Приступ Microsoft-а одговорној употреби AI заснован је на нашим принципима AI: праведност, поузданост и безбедност, приватност и сигурност, инклузивност, транспарентност и одговорност.  

Модели великог обима за обраду природног језика, слике и говора - као што су они коришћени у овом примеру - могу потенцијално да се понашају на начин који је неправедан, непоуздан или увредљив, што може довести до штетних последица. Молимо вас да консултујете [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) како бисте били информисани о ризицима и ограничењима.  

Препоручени приступ за ублажавање ових ризика је укључивање система за безбедност у вашу архитектуру који може открити и спречити штетно понашање. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) пружа независан слој заштите, способан да открије штетан садржај који генеришу корисници или AI у апликацијама и услугама. Azure AI Content Safety укључује API-је за текст и слике који омогућавају откривање штетног материјала. У оквиру Azure AI Foundry, Content Safety услуга омогућава вам да прегледате, истражујете и испробате пример кода за откривање штетног садржаја у различитим модалитетима. Следећа [документација за брзи почетак](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) води вас кроз процес слања захтева услузи.  

Још један аспект који треба узети у обзир је укупна перформанса апликације. Код мултимодалних и мултимодел апликација, перформанса подразумева да систем ради онако како ви и ваши корисници очекујете, укључујући и то да не генерише штетне резултате. Важно је проценити перформансе ваше апликације користећи [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Такође имате могућност да креирате и процењујете помоћу [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).  

Можете проценити вашу AI апликацију у вашем развојном окружењу користећи [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Уз помоћ тест датасета или циља, генерисања ваше генеративне AI апликације се квантитативно мере помоћу уграђених или прилагођених евалуатора по вашем избору. Да бисте започели са Azure AI Evaluation SDK за процену вашег система, можете пратити [водич за брзи почетак](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Након што извршите евалуацију, можете [визуализовати резултате у Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).  

## Заштитни знаци  

Овај пројекат може садржати заштитне знаке или логотипе за пројекте, производе или услуге. Овлашћена употреба Microsoft заштитних знакова или логотипа подлеже и мора следити [Microsoft-ове смернице за употребу заштитних знакова и брендова](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Употреба Microsoft заштитних знакова или логотипа у модификованим верзијама овог пројекта не сме изазвати забуну или имплицирати спонзорство од стране Microsoft-а. Свака употреба заштитних знакова или логотипа трећих страна подлеже политикама тих трећих страна.  

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.