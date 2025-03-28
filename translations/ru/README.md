<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1377ae1b0bc9daeaa6a989f750977aeb",
  "translation_date": "2025-03-27T02:59:17+00:00",
  "source_file": "README.md",
  "language_code": "ru"
}
-->
# Phi Cookbook: Практические примеры с моделями Phi от Microsoft

[![Открыть и использовать примеры в GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Открыть в Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Участники GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Проблемы GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Запросы на слияние GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![Добро пожаловать в PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Наблюдатели GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Форки GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Звезды GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi — это серия открытых моделей ИИ, разработанных Microsoft.

На данный момент Phi является самой мощной и экономичной маленькой языковой моделью (SLM), демонстрируя отличные результаты в многозадачности, рассуждениях, генерации текста/чата, кодировании, работе с изображениями, аудио и других сценариях.

Phi можно развернуть в облаке или на периферийных устройствах, а также легко создавать приложения генеративного ИИ с ограниченными вычислительными ресурсами.

Следуйте этим шагам, чтобы начать использовать эти ресурсы:
1. **Сделайте форк репозитория**: Нажмите [![Форки GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Клонируйте репозиторий**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Присоединяйтесь к сообществу Microsoft AI Discord, чтобы встретиться с экспертами и другими разработчиками**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.ru.png)

## 🌐 Поддержка нескольких языков
[Французский](../fr/README.md) | [Испанский](../es/README.md) | [Немецкий](../de/README.md) | [Русский](./README.md) | [Арабский](../ar/README.md) | [Персидский (Фарси)](../fa/README.md) | [Урду](../ur/README.md) | [Китайский (упрощенный)](../zh/README.md) | [Китайский (традиционный, Макао)](../mo/README.md) | [Китайский (традиционный, Гонконг)](../hk/README.md) | [Китайский (традиционный, Тайвань)](../tw/README.md) | [Японский](../ja/README.md) | [Корейский](../ko/README.md) | [Хинди](../hi/README.md) | [Бенгальский](../bn/README.md) | [Маратхи](../mr/README.md) | [Непальский](../ne/README.md) | [Панджаби (Гурмукхи)](../pa/README.md) | [Португальский (Португалия)](../pt/README.md) | [Португальский (Бразилия)](../br/README.md) | [Итальянский](../it/README.md) | [Польский](../pl/README.md) | [Турецкий](../tr/README.md) | [Греческий](../el/README.md) | [Тайский](../th/README.md) | [Шведский](../sv/README.md) | [Датский](../da/README.md) | [Норвежский](../no/README.md) | [Финский](../fi/README.md) | [Голландский](../nl/README.md) | [Иврит](../he/README.md) | [Вьетнамский](../vi/README.md) | [Индонезийский](../id/README.md) | [Малайский](../ms/README.md) | [Тагальский (Филиппинский)](../tl/README.md) | [Суахили](../sw/README.md) | [Венгерский](../hu/README.md) | [Чешский](../cs/README.md) | [Словацкий](../sk/README.md) | [Румынский](../ro/README.md) | [Болгарский](../bg/README.md) | [Сербский (Кириллица)](../sr/README.md) | [Хорватский](../hr/README.md) | [Словенский](../sl/README.md)
## Содержание

- Введение
  - [Добро пожаловать в семью Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Настройка окружения](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Понимание ключевых технологий](./md/01.Introduction/01/01.Understandingtech.md)
  - [Безопасность ИИ для моделей Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Поддержка оборудования Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Модели Phi и доступность на различных платформах](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Использование Guidance-ai и Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Модели на GitHub Marketplace](https://github.com/marketplace/models)
  - [Каталог моделей Azure AI](https://ai.azure.com)

- Использование Phi в различных средах
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)
    -  [Модели GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Каталог моделей Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Использование семейства Phi
    - [Использование Phi на iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Использование Phi на Android](./md/01.Introduction/03/Android_Inference.md)
    - [Использование Phi на Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Использование Phi на AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Использование Phi с Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Использование Phi на локальном сервере](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Использование Phi на удаленном сервере с AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Использование Phi с Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Использование Phi--Vision локально](./md/01.Introduction/03/Vision_Inference.md)
    - [Использование Phi с Kaito AKS, контейнерами Azure (официальная поддержка)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Квантификация семейства Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Квантификация Phi-3.5 / 4 с использованием llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Квантификация Phi-3.5 / 4 с использованием расширений Generative AI для onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Квантификация Phi-3.5 / 4 с использованием Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Квантификация Phi-3.5 / 4 с использованием Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Оценка Phi
- [Response AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry для оценки](./md/01.Introduction/05/AIFoundry.md)
    - [Использование Promptflow для оценки](./md/01.Introduction/05/Promptflow.md)
 
- RAG с Azure AI Search
    - [Как использовать Phi-4-mini и Phi-4-multimodal (RAG) с Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Примеры разработки приложений с Phi
  - Текстовые и чат-приложения
    - Примеры Phi-4 🆕
      - [📓] [Чат с моделью Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Чат с локальной моделью Phi-4 ONNX в .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Консольное приложение чата в .NET с Phi-4 ONNX и Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Примеры Phi-3 / 3.5
      - [Локальный чат-бот в браузере с использованием Phi3, ONNX Runtime Web и WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [Чат OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Мульти-модель - интерактивный Phi-3-mini и OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - создание обертки и использование Phi-3 с MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Оптимизация модели - как оптимизировать модель Phi-3-min для ONNX Runtime Web с помощью Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 приложение с Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3 приложение заметок с AI и несколькими моделями](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Тонкая настройка и интеграция кастомных моделей Phi-3 с Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Тонкая настройка и интеграция кастомных моделей Phi-3 с Prompt flow в Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Оценка тонко настроенной модели Phi-3 / Phi-3.5 в Azure AI Foundry с акцентом на принципы ответственного AI от Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Пример языкового предсказания Phi-3.5-mini-instruct (китайский/английский)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Чат-бот RAG на WebGPU с Phi-3.5-Instruct](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Использование Windows GPU для создания решения Prompt flow с Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Создание Android-приложения с использованием Microsoft Phi-3.5 tflite](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Пример Q&A в .NET с локальной моделью ONNX Phi-3 и Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Консольное приложение чата в .NET с Semantic Kernel и Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Примеры на основе SDK для инференса Azure AI 
    - Примеры Phi-4 🆕
      - [📓] [Генерация кода проекта с использованием Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Примеры Phi-3 / 3.5
      - [Создание собственного чата Visual Studio Code GitHub Copilot с семейством Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Создание собственного агента чата Visual Studio Code Copilot с Phi-3.5 с использованием моделей GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Примеры продвинутого рассуждения
    - Примеры Phi-4 🆕
      - [📓] [Примеры рассуждений с Phi-4-mini](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
  
  - Демонстрации
      - [Демонстрации Phi-4-mini, размещенные на Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Демонстрации Phi-4-multimodal, размещенные на Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Примеры для работы с изображениями
    - Примеры Phi-4 🆕
      - [📓] [Использование Phi-4-multimodal для чтения изображений и генерации кода](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Примеры Phi-3 / 3.5
- [📓][Phi-3-vision-Image text to text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ДЕМО: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Визуальный языковой помощник - с Phi3-Vision и OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision multi-frame or multi-image sample](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision Локальная модель ONNX с использованием Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Меню Phi-3 Vision Локальная модель ONNX с использованием Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Аудио примеры
    - Примеры Phi-4 🆕
      - [📓] [Извлечение транскриптов аудио с помощью Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Аудио пример Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Пример перевода речи с помощью Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET консольное приложение, использующее Phi-4-multimodal для анализа аудиофайла и создания транскрипта](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - Примеры MOE
    - Примеры Phi-3 / 3.5
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) Пример социальных сетей](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Создание Retrieval-Augmented Generation (RAG) конвейера с NVIDIA NIM Phi-3 MOE, Azure AI Search и LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
  - Примеры вызова функций
    - Примеры Phi-4 🆕
      - [📓] [Использование вызова функций с Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      - [📓] [Использование вызова функций для создания мульти-агентов с Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      - [📓] [Использование вызова функций с Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
  - Примеры смешивания мультимодальных данных
    - Примеры Phi-4 🆕
      - [📓] [Использование Phi-4-multimodal в роли технологического журналиста](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET консольное приложение, использующее Phi-4-multimodal для анализа изображений](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Настройка Phi
  - [Сценарии настройки](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Настройка vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Настройка: Дать Phi-3 стать экспертом в отрасли](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Настройка Phi-3 с AI Toolkit для VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Настройка Phi-3 с Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Настройка Phi-3 с Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Настройка Phi-3 с QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Настройка Phi-3 с Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Настройка Phi-3 с Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
- [Тонкая настройка с Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Практическое занятие по тонкой настройке с Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)  
  - [Тонкая настройка Phi-3-vision с Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Тонкая настройка Phi-3 с использованием Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Тонкая настройка Phi-3-vision (официальная поддержка)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Тонкая настройка Phi-3 с Kaito AKS и Azure Containers (официальная поддержка)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Тонкая настройка Phi-3 и 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- Практическое занятие  
  - [Изучение передовых моделей: LLMs, SLMs, локальная разработка и многое другое](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [Раскрытие потенциала NLP: тонкая настройка с Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- Научные статьи и публикации  
  - [Textbooks Are All You Need II: технический отчет phi-1.5](https://arxiv.org/abs/2309.05463)  
  - [Технический отчет Phi-3: мощная языковая модель локально на вашем телефоне](https://arxiv.org/abs/2404.14219)  
  - [Технический отчет Phi-4](https://arxiv.org/abs/2412.08905)  
  - [Технический отчет Phi-4-Mini: компактные, но мощные мультимодальные языковые модели через Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [Оптимизация малых языковых моделей для вызова функций в автомобиле](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) Тонкая настройка PHI-3 для ответов на вопросы с множественным выбором: методология, результаты и вызовы](https://arxiv.org/abs/2501.01588)  

## Использование моделей Phi  

### Phi на Azure AI Foundry  

Вы можете узнать, как использовать Microsoft Phi и создавать комплексные решения для различных аппаратных устройств. Чтобы опробовать Phi, начните с работы с моделями и настройки Phi под ваши сценарии, используя [каталог моделей Azure AI Foundry](https://aka.ms/phi3-azure-ai). Подробнее можно узнать в разделе [Начало работы с Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).  

**Песочница**  
Каждая модель имеет свою песочницу для тестирования [Azure AI Playground](https://aka.ms/try-phi3).  

### Phi на GitHub Models  

Вы можете узнать, как использовать Microsoft Phi и создавать комплексные решения для различных аппаратных устройств. Чтобы опробовать Phi, начните с работы с моделью и настройки Phi под ваши сценарии, используя [каталог моделей GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Подробнее можно узнать в разделе [Начало работы с каталогом моделей GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md).  

**Песочница**  
Каждая модель имеет свою [песочницу для тестирования](/md/02.QuickStart/GitHubModel_QuickStart.md).  

### Phi на Hugging Face  

Вы также можете найти модель на [Hugging Face](https://huggingface.co/microsoft).  

**Песочница**  
[Песочница Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct).  

## Ответственный подход к ИИ  

Microsoft стремится помогать своим клиентам использовать продукты ИИ ответственно, делиться своими наработками и строить партнерства, основанные на доверии, через такие инструменты, как Прозрачные заметки и Оценки воздействия. Многие из этих ресурсов можно найти на [https://aka.ms/RAI](https://aka.ms/RAI).  
Подход Microsoft к ответственному ИИ основан на наших принципах: справедливость, надежность и безопасность, конфиденциальность и защита, инклюзивность, прозрачность и подотчетность.  

Крупные модели обработки текста, изображений и речи, как те, что используются в этом примере, могут потенциально вести себя несправедливо, ненадежно или оскорбительно, что может причинить вред. Ознакомьтесь с [заметкой о прозрачности Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), чтобы быть в курсе рисков и ограничений.  

Рекомендуемый подход к снижению этих рисков — включить в архитектуру систему безопасности, способную обнаруживать и предотвращать вредоносное поведение. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) предоставляет независимый уровень защиты, способный обнаруживать вредоносный контент, сгенерированный пользователями или ИИ, в приложениях и сервисах. Azure AI Content Safety включает API для текста и изображений, которые позволяют обнаруживать вредоносные материалы. В Azure AI Foundry сервис Content Safety позволяет просматривать, изучать и тестировать примерный код для обнаружения вредоносного контента в различных модальностях. Следующая [документация для быстрого старта](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) поможет вам сделать запросы к сервису.  

Еще один аспект, который следует учитывать, — это общая производительность приложения. Для мультимодальных и многомодельных приложений производительность означает, что система работает так, как ожидаете вы и ваши пользователи, включая предотвращение генерации вредоносного контента. Важно оценивать производительность всего приложения с помощью [оценщиков производительности, качества, рисков и безопасности](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Вы также можете создавать и оценивать [пользовательские оценщики](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).
Вы можете оценить ваше приложение с искусственным интеллектом в вашей среде разработки, используя [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). С помощью тестового набора данных или целевой задачи, генерации вашего приложения с использованием генеративного ИИ могут быть количественно измерены с помощью встроенных или пользовательских оценщиков на ваш выбор. Чтобы начать работу с Azure AI Evaluation SDK для оценки вашей системы, вы можете воспользоваться [руководством по быстрому старту](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). После выполнения процесса оценки, вы можете [визуализировать результаты в Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Торговые марки

Этот проект может содержать торговые марки или логотипы для проектов, продуктов или услуг. Разрешенное использование торговых марок или логотипов Microsoft должно соответствовать [Руководству по торговым маркам и брендам Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general). Использование торговых марок или логотипов Microsoft в модифицированных версиях этого проекта не должно вызывать путаницу или подразумевать спонсорство со стороны Microsoft. Любое использование торговых марок или логотипов третьих сторон должно соответствовать политике этих сторон.

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке должен считаться авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникающие в результате использования данного перевода.