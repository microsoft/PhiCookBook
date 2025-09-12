<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T14:15:11+00:00",
  "source_file": "README.md",
  "language_code": "bg"
}
-->
# Phi Cookbook: Практически примери с моделите Phi на Microsoft

Phi е серия от отворени AI модели, разработени от Microsoft.

Phi в момента е най-мощният и икономически ефективен малък езиков модел (SLM), с отлични резултати в многоезичност, логическо мислене, генериране на текст/чат, кодиране, изображения, аудио и други сценарии.

Можете да внедрите Phi в облака или на крайни устройства и лесно да създавате приложения за генеративен AI с ограничена изчислителна мощност.

Следвайте тези стъпки, за да започнете да използвате тези ресурси:
1. **Направете Fork на хранилището**: Кликнете [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Клонирайте хранилището**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Присъединете се към Microsoft AI Discord общността и се срещнете с експерти и други разработчици**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 Поддръжка на много езици

#### Поддържано чрез GitHub Action (Автоматизирано и винаги актуално)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) 
[Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](./README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)

## Съдържание

- Въведение
  - [Добре дошли в семейството Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Настройка на вашата среда](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Разбиране на ключови технологии](./md/01.Introduction/01/01.Understandingtech.md)
  - [AI безопасност за моделите Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Поддръжка на хардуер за Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Модели Phi и наличност на различни платформи](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Използване на Guidance-ai и Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Модели от GitHub Marketplace](https://github.com/marketplace/models)
  - [Каталог на модели в Azure AI](https://ai.azure.com)

- Извеждане на Phi в различни среди
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub модели](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Каталог на модели в Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Извеждане на семейството Phi
    - [Извеждане на Phi в iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Извеждане на Phi в Android](./md/01.Introduction/03/Android_Inference.md)
    - [Извеждане на Phi в Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Извеждане на Phi в AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Извеждане на Phi с Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Извеждане на Phi в локален сървър](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Извеждане на Phi в отдалечен сървър с AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Извеждане на Phi с Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Извеждане на Phi--Vision локално](./md/01.Introduction/03/Vision_Inference.md)
    - [Извеждане на Phi с Kaito AKS, Azure Containers (официална поддръжка)](./md/01.Introduction/03/Kaito_Inference.md)

- [Квантифициране на семейството Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Квантифициране на Phi-3.5 / 4 с llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Квантифициране на Phi-3.5 / 4 с разширения за генеративен AI за onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Квантифициране на Phi-3.5 / 4 с Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Квантифициране на Phi-3.5 / 4 с Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Оценка на Phi
    - [Отговорен AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Оценка с Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [Използване на Promptflow за оценка](./md/01.Introduction/05/Promptflow.md)

- RAG с Azure AI Search
    - [Как да използвате Phi-4-mini и Phi-4-multimodal (RAG) с Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Примери за разработка на приложения с Phi
  - Текстови и чат приложения
    - Примери с Phi-4 🆕
      - [📓] [Чат с Phi-4-mini ONNX модел](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Чат с локален ONNX модел Phi-4 .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Конзолно приложение .NET за чат с Phi-4 ONNX, използвайки Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Примери с Phi-3 / 3.5
      - [Локален чатбот в браузъра, използвайки Phi3, ONNX Runtime Web и WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [Чат с OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Мултимодел - Интерактивен Phi-3-mini и OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Създаване на обвивка и използване на Phi-3 с MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Оптимизация на модел - Как да оптимизирате Phi-3-min модел за ONNX Runtime Web с Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 приложение с Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3 мултимодел AI приложение за бележки](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Фина настройка и интеграция на персонализирани Phi-3 модели с Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Фина настройка и интеграция на персонализирани Phi-3 модели с Prompt flow в Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Оценка на фино настроените Phi-3 / Phi-3.5 модели в Azure AI Foundry с акцент върху принципите на отговорния AI на Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Пример за езиково предсказание с Phi-3.5-mini-instruct (китайски/английски)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Използване на Windows GPU за създаване на решение с Prompt flow и Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Използване на Microsoft Phi-3.5 tflite за създаване на Android приложение](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Пример за Q&A .NET с локален ONNX Phi-3 модел, използвайки Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Конзолно чат приложение .NET със Semantic Kernel и Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Примери за код с Azure AI Inference SDK
  - Примери с Phi-4 🆕
    - [📓] [Генериране на проектен код с Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Примери с Phi-3 / 3.5
    - [Създайте свой собствен Visual Studio Code GitHub Copilot Chat с Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [Създайте свой собствен Visual Studio Code Chat Copilot Agent с Phi-3.5 чрез GitHub модели](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- Примери за напреднало разсъждение
  - Примери с Phi-4 🆕
    - [📓] [Примери с Phi-4-mini-reasoning или Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Фина настройка на Phi-4-mini-reasoning с Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Фина настройка на Phi-4-mini-reasoning с Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning с GitHub модели](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Phi-4-mini-reasoning с модели от Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- Демонстрации
    - [Демонстрации с Phi-4-mini, хоствани в Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Демонстрации с Phi-4-multimodal, хоствани в Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- Примери за визия
  - Примери с Phi-4 🆕
    - [📓] [Използване на Phi-4-multimodal за четене на изображения и генериране на код](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Примери с Phi-3 / 3.5
    - [📓][Phi-3-vision-Image текст към текст](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [ДЕМОНСТРАЦИЯ: Phi-3 Рециклиране](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Визуален езиков асистент - с Phi3-Vision и OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision пример с много кадри или много изображения](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Phi-3 Vision локален ONNX модел, използвайки Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Меню базиран Phi-3 Vision локален ONNX модел, използвайки Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

- Примери за математика
  - Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [Демонстрация на математика с Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)

- Примери за аудио
  - Примери с Phi-4 🆕
    - [📓] [Извличане на аудио транскрипции с Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Пример за аудио с Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Пример за превод на реч с Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET конзолно приложение, използващо Phi-4-multimodal за анализ на аудио файл и генериране на транскрипция](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- Примери за MOE
  - Примери с Phi-3 / 3.5
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) пример за социални медии](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [Създаване на Retrieval-Augmented Generation (RAG) Pipeline с NVIDIA NIM Phi-3 MOE, Azure AI Search и LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- Примери за извикване на функции
  - Примери с Phi-4 🆕
    - [📓] [Използване на извикване на функции с Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Използване на извикване на функции за създаване на много агенти с Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Използване на извикване на функции с Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [Използване на извикване на функции с ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- Примери за мултимодално смесване
  - Примери с Phi-4 🆕
    - [📓] [Използване на Phi-4-multimodal като технологичен журналист](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET конзолно приложение, използващо Phi-4-multimodal за анализ на изображения](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Примери за фина настройка на Phi
  - [Сценарии за фина настройка](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Фина настройка срещу RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Фина настройка: Нека Phi-3 стане експерт в индустрията](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Фина настройка на Phi-3 с AI Toolkit за VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Фина настройка на Phi-3 с Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Фина настройка на Phi-3 с Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Фина настройка на Phi-3 с QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Фина настройка на Phi-3 с Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Фина настройка на Phi-3 с Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Фина настройка с Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Фина настройка с Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Фина настройка на Phi-3-vision с Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Фина настройка на Phi-3 с Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Фина настройка на Phi-3-vision (официална поддръжка)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Фина настройка на Phi-3 с Kaito AKS, Azure Containers (официална поддръжка)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Фина настройка на Phi-3 и 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Практически лаборатории
  - [Изследване на авангардни модели: LLMs, SLMs, локално разработване и други](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Отключване на потенциала на NLP: Фина настройка с Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Академични изследователски статии и публикации
  - [Textbooks Are All You Need II: phi-1.5 технически доклад](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Технически доклад: Висококапацитетен езиков модел локално на вашия телефон](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Технически доклад](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Технически доклад: Компактни, но мощни мултимодални езикови модели чрез Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Оптимизиране на малки езикови модели за извикване на функции в превозни средства](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Фина настройка на PHI-3 за въпроси с множество отговори: Методология, резултати и предизвикателства](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning Технически доклад](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning Технически доклад](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)  

## Използване на Phi модели  

### Phi в Azure AI Foundry  

Можете да научите как да използвате Microsoft Phi и как да изграждате E2E решения на различни хардуерни устройства. За да изпробвате Phi сами, започнете с тестване на моделите и персонализиране на Phi за вашите сценарии, използвайки [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Можете да научите повече в раздела "Започнете" с [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).  

**Playground**  
Всеки модел има специален playground за тестване на модела [Azure AI Playground](https://aka.ms/try-phi3).  

### Phi в GitHub Models  

Можете да научите как да използвате Microsoft Phi и как да изграждате E2E решения на различни хардуерни устройства. За да изпробвате Phi сами, започнете с тестване на модела и персонализиране на Phi за вашите сценарии, използвайки [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Можете да научите повече в раздела "Започнете" с [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).  

**Playground**  
Всеки модел има специален [playground за тестване на модела](/md/02.QuickStart/GitHubModel_QuickStart.md).  

### Phi в Hugging Face  

Можете също да намерите модела в [Hugging Face](https://huggingface.co/microsoft).  

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct).  

## Отговорен AI  

Microsoft се ангажира да помага на своите клиенти да използват AI продуктите отговорно, споделяйки наученото и изграждайки партньорства, базирани на доверие, чрез инструменти като Transparency Notes и Impact Assessments. Много от тези ресурси могат да бъдат намерени на [https://aka.ms/RAI](https://aka.ms/RAI).  
Подходът на Microsoft към отговорния AI се основава на нашите принципи за AI: справедливост, надеждност и безопасност, поверителност и сигурност, приобщаване, прозрачност и отчетност.  

Мащабни модели за естествен език, изображения и реч - като тези, използвани в този пример - могат потенциално да се държат по начини, които са несправедливи, ненадеждни или обидни, което може да причини вреди. Моля, консултирайте се с [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), за да бъдете информирани за рисковете и ограниченията.  

Препоръчаният подход за смекчаване на тези рискове е включването на система за безопасност във вашата архитектура, която може да открива и предотвратява вредно поведение. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) предоставя независим слой защита, способен да открива вредно съдържание, генерирано от потребители или AI, в приложения и услуги. Azure AI Content Safety включва текстови и визуални API, които позволяват откриване на вредни материали. В рамките на Azure AI Foundry, Content Safety услугата ви позволява да разглеждате, изследвате и тествате примерен код за откриване на вредно съдържание в различни модалности. Следната [бърза документация](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ви насочва как да правите заявки към услугата.  

Друг аспект, който трябва да се вземе предвид, е цялостната производителност на приложението. При мултимодални и мултимоделни приложения, производителността означава, че системата работи според очакванията на вас и вашите потребители, включително да не генерира вредни резултати. Важно е да оцените производителността на вашето приложение, използвайки [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Имате възможност да създавате и оценявате с [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).  

Можете да оцените вашето AI приложение в средата за разработка, използвайки [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). С предоставен тестов набор от данни или цел, генериранията на вашето генеративно AI приложение се измерват количествено с вградени или персонализирани оценители по ваш избор. За да започнете с Azure AI Evaluation SDK и да оцените вашата система, можете да следвате [бързия наръчник](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). След като изпълните оценка, можете [да визуализирате резултатите в Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).  

## Търговски марки  

Този проект може да съдържа търговски марки или лога за проекти, продукти или услуги. Употребата на търговски марки или лога на Microsoft трябва да бъде съобразена с [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Употребата на търговски марки или лога на Microsoft в модифицирани версии на този проект не трябва да създава объркване или да предполага спонсорство от Microsoft. Употребата на търговски марки или лога на трети страни трябва да бъде съобразена с политиките на съответните трети страни.  

---

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.