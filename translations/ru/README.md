<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10139744c0f1757a5ade1c66749e803f",
  "translation_date": "2025-05-04T13:32:11+00:00",
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
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Наблюдатели GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Форки GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Звёзды GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)


[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi — это серия открытых моделей искусственного интеллекта, разработанных Microsoft.

В настоящее время Phi является самой мощной и экономичной небольшой языковой моделью (SLM) с отличными результатами в многоязычии, логическом мышлении, генерации текста/чата, программировании, работе с изображениями, аудио и других сценариях.

Вы можете развернуть Phi в облаке или на периферийных устройствах, а также легко создавать генеративные AI-приложения с ограниченными вычислительными ресурсами.

Следуйте этим шагам, чтобы начать работу с этими ресурсами:
1. **Сделайте форк репозитория**: Нажмите [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Клонируйте репозиторий**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Присоединяйтесь к сообществу Microsoft AI в Discord, чтобы общаться с экспертами и другими разработчиками**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.ru.png)

## 🌐 Поддержка нескольких языков
[Французский](../fr/README.md) | [Испанский](../es/README.md) | [Немецкий](../de/README.md) | [Русский](./README.md) | [Арабский](../ar/README.md) | [Персидский (Фарси)](../fa/README.md) | [Урду](../ur/README.md) | [Китайский (упрощенный)](../zh/README.md) | [Китайский (традиционный, Макао)](../mo/README.md) | [Китайский (традиционный, Гонконг)](../hk/README.md) | [Китайский (традиционный, Тайвань)](../tw/README.md) | [Японский](../ja/README.md) | [Корейский](../ko/README.md) | [Хинди](../hi/README.md) [Бенгальский](../bn/README.md) | [Маратхи](../mr/README.md) | [Непальский](../ne/README.md) | [Пенджабский (Гурмукхи)](../pa/README.md) | [Португальский (Португалия)](../pt/README.md) | [Португальский (Бразилия)](../br/README.md) | [Итальянский](../it/README.md) | [Польский](../pl/README.md) | [Турецкий](../tr/README.md) | [Греческий](../el/README.md) | [Тайский](../th/README.md) | [Шведский](../sv/README.md) | [Датский](../da/README.md) | [Норвежский](../no/README.md) | [Финский](../fi/README.md) | [Нидерландский](../nl/README.md) | [Иврит](../he/README.md) | [Вьетнамский](../vi/README.md) | [Индонезийский](../id/README.md) | [Малайский](../ms/README.md) | [Тагальский (филиппинский)](../tl/README.md) | [Суахили](../sw/README.md) | [Венгерский](../hu/README.md) | [Чешский](../cs/README.md) | [Словацкий](../sk/README.md) | [Румынский](../ro/README.md) | [Болгарский](../bg/README.md) | [Сербский (кириллица)](../sr/README.md) | [Хорватский](../hr/README.md) | [Словенский](../sl/README.md)
## Содержание

- Введение
  - [Добро пожаловать в семью Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Настройка вашей среды](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Понимание ключевых технологий](./md/01.Introduction/01/01.Understandingtech.md)
  - [Безопасность ИИ для моделей Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Поддержка аппаратного обеспечения Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Модели Phi и их доступность на разных платформах](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Использование Guidance-ai и Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Модели на GitHub Marketplace](https://github.com/marketplace/models)
  - [Каталог моделей Azure AI](https://ai.azure.com)

- Запуск Phi в разных средах
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [Модели на GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Каталог моделей Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit для VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Запуск Phi Family
    - [Запуск Phi на iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Запуск Phi на Android](./md/01.Introduction/03/Android_Inference.md)
    - [Запуск Phi на Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Запуск Phi на AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Запуск Phi с помощью Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Запуск Phi на локальном сервере](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Запуск Phi на удалённом сервере с использованием AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Запуск Phi с Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Запуск Phi--Vision локально](./md/01.Introduction/03/Vision_Inference.md)
    - [Запуск Phi с Kaito AKS, Azure Containers (официальная поддержка)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Квантизация Phi Family](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Квантизация Phi-3.5 / 4 с использованием llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Квантизация Phi-3.5 / 4 с помощью расширений Generative AI для onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Квантизация Phi-3.5 / 4 с использованием Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Квантизация Phi-3.5 / 4 с использованием Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Оценка Phi
- [Response AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry для оценки](./md/01.Introduction/05/AIFoundry.md)
    - [Использование Promptflow для оценки](./md/01.Introduction/05/Promptflow.md)
 
- RAG с Azure AI Search
    - [Как использовать Phi-4-mini и Phi-4-multimodal (RAG) с Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Примеры разработки приложений Phi
  - Текстовые и чат-приложения
    - Примеры Phi-4 🆕
      - [📓] [Чат с моделью Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Чат с локальной моделью Phi-4 ONNX на .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Консольное чат-приложение на .NET с Phi-4 ONNX и Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Примеры Phi-3 / 3.5
      - [Локальный чатбот в браузере с использованием Phi3, ONNX Runtime Web и WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Мультимодель - интерактивный Phi-3-mini и OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - создание обертки и использование Phi-3 с MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Оптимизация модели - как оптимизировать Phi-3-mini для ONNX Runtime Web с Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 приложение с Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3 Мультимодельное приложение для заметок с ИИ](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Тонкая настройка и интеграция кастомных моделей Phi-3 с Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Тонкая настройка и интеграция кастомных моделей Phi-3 с Prompt flow в Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Оценка тонко настроенной модели Phi-3 / Phi-3.5 в Azure AI Foundry с акцентом на принципы ответственного ИИ Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Пример предсказания языка Phi-3.5-mini-instruct (китайский/английский)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG чатбот](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Использование Windows GPU для создания решения Prompt flow с Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Использование Microsoft Phi-3.5 tflite для создания Android-приложения](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Пример Q&A на .NET с локальной моделью ONNX Phi-3 с Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Консольное чат-приложение на .NET с Semantic Kernel и Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Примеры кода с использованием Azure AI Inference SDK
    - Примеры Phi-4 🆕
      - [📓] [Генерация кода проекта с использованием Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Примеры Phi-3 / 3.5
      - [Создайте собственный чат GitHub Copilot для Visual Studio Code с Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Создайте собственного агента чата для Visual Studio Code с Phi-3.5 на базе моделей GitHub](./md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Примеры расширенного рассуждения
    - Примеры Phi-4 🆕
      - [📓] [Примеры Phi-4-mini-reasoning или Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Тонкая настройка Phi-4-mini-reasoning с помощью Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Тонкая настройка Phi-4-mini-reasoning с Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning с моделями GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
- [📓] [Phi-4-mini reasoning с моделями Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Демонстрации
      - [Phi-4-mini демонстрации на Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-мультимодальные демонстрации на Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Примеры Vision
    - Примеры Phi-4 🆕
      - [📓] [Использование Phi-4-мультимодального для чтения изображений и генерации кода](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Примеры Phi-3 / 3.5
      -  [📓][Phi-3-vision: преобразование текста на изображении в текст](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ДЕМО: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Визуальный языковой ассистент с Phi3-Vision и OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision пример с несколькими кадрами или изображениями](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision локальная ONNX модель с использованием Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Меню для Phi-3 Vision локальной ONNX модели с использованием Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Примеры Audio
    - Примеры Phi-4 🆕
      - [📓] [Извлечение транскриптов аудио с помощью Phi-4-мультимодального](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Пример аудио с Phi-4-мультимодальным](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Пример перевода речи с Phi-4-мультимодальным](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET консольное приложение с использованием Phi-4-мультимодального Audio для анализа аудиофайла и генерации транскрипта](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - Примеры MOE
    - Примеры Phi-3 / 3.5
      - [📓] [Пример модели Mixture of Experts (MoEs) Phi-3.5 для социальных сетей](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Построение RAG-пайплайна с NVIDIA NIM Phi-3 MOE, Azure AI Search и LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
  - Примеры вызова функций
    - Примеры Phi-4 🆕
      -  [📓] [Использование вызова функций с Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Использование вызова функций для создания мультиагентов с Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Использование вызова функций с Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
  - Примеры мультимодального смешивания
    - Примеры Phi-4 🆕
      -  [📓] [Использование Phi-4-мультимодального в роли технологического журналиста](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET консольное приложение с использованием Phi-4-мультимодального для анализа изображений](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Примеры тонкой настройки Phi
  - [Сценарии тонкой настройки](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Тонкая настройка против RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Тонкая настройка: сделайте Phi-3 экспертом в индустрии](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Тонкая настройка Phi-3 с AI Toolkit для VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Тонкая настройка Phi-3 с помощью Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
- [Тонкая настройка Phi-3 с помощью Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Тонкая настройка Phi-3 с QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Тонкая настройка Phi-3 с Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Тонкая настройка Phi-3 с Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Тонкая настройка с Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Практическая лаборатория по тонкой настройке с Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)
  - [Тонкая настройка Phi-3-vision с Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Тонкая настройка Phi-3 с Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Тонкая настройка Phi-3-vision (официальная поддержка)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Тонкая настройка Phi-3 с Kaito AKS, Azure Containers (официальная поддержка)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Тонкая настройка Phi-3 и 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Практическая лаборатория
  - [Изучение передовых моделей: LLM, SLM, локальная разработка и многое другое](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Раскрытие потенциала NLP: тонкая настройка с Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Научные статьи и публикации
  - [Textbooks Are All You Need II: технический отчет phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Технический отчет Phi-3: мощная языковая модель, работающая локально на вашем телефоне](https://arxiv.org/abs/2404.14219)
  - [Технический отчет Phi-4](https://arxiv.org/abs/2412.08905)
  - [Технический отчет Phi-4-Mini: компактные, но мощные мультимодальные языковые модели с помощью Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Оптимизация небольших языковых моделей для вызова функций в автомобиле](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Тонкая настройка PHI-3 для ответов на вопросы с несколькими вариантами: методология, результаты и вызовы](https://arxiv.org/abs/2501.01588)
  - [Технический отчет Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Технический отчет Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Использование моделей Phi

### Phi на Azure AI Foundry

Вы можете узнать, как использовать Microsoft Phi и создавать комплексные решения для разных аппаратных устройств. Чтобы попробовать Phi самостоятельно, начните с экспериментов с моделями и настройки Phi под ваши задачи с помощью [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Подробнее можно узнать в разделе Начало работы с [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Площадка для тестирования**  
Для каждой модели предусмотрена отдельная площадка для тестирования — [Azure AI Playground](https://aka.ms/try-phi3).

### Phi на GitHub Models

Вы можете узнать, как использовать Microsoft Phi и создавать комплексные решения для разных аппаратных устройств. Чтобы попробовать Phi самостоятельно, начните с экспериментов с моделью и настройки Phi под ваши задачи с помощью [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Подробнее можно узнать в разделе Начало работы с [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Площадка для тестирования**  
Для каждой модели предусмотрена отдельная [площадка для тестирования модели](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi на Hugging Face

Модель также доступна на [Hugging Face](https://huggingface.co/microsoft).

**Площадка для тестирования**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Ответственный ИИ

Microsoft стремится помогать клиентам ответственно использовать наши AI-продукты, делиться опытом и строить доверительные партнерства с помощью инструментов, таких как Transparency Notes и Impact Assessments. Многие из этих ресурсов доступны по адресу [https://aka.ms/RAI](https://aka.ms/RAI).  
Подход Microsoft к ответственному ИИ основан на принципах справедливости, надежности и безопасности, конфиденциальности и защите данных, инклюзивности, прозрачности и подотчетности.
Крупномасштабные модели обработки естественного языка, изображений и речи — такие, как используемые в этом примере — могут иногда вести себя несправедливо, ненадёжно или оскорбительно, что может привести к негативным последствиям. Пожалуйста, ознакомьтесь с [заметкой о прозрачности сервиса Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), чтобы узнать о рисках и ограничениях.

Рекомендуемый способ снижения этих рисков — включить в архитектуру систему безопасности, которая способна обнаруживать и предотвращать вредоносное поведение. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) предоставляет независимый уровень защиты, позволяющий выявлять вредоносный контент, созданный пользователями или ИИ, в приложениях и сервисах. Azure AI Content Safety включает API для работы с текстом и изображениями, которые помогают обнаруживать вредоносные материалы. В рамках Azure AI Foundry сервис Content Safety позволяет просматривать, исследовать и тестировать пример кода для обнаружения вредоносного контента в различных форматах. Следующая [документация для быстрого старта](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) поможет вам научиться делать запросы к сервису.

Ещё один важный аспект — общая производительность приложения. В приложениях с несколькими модальностями и моделями под производительностью понимается то, что система работает так, как ожидаете вы и ваши пользователи, включая отсутствие генерации вредоносного контента. Важно оценивать производительность всего приложения с помощью [оценщиков производительности, качества, риска и безопасности](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Также у вас есть возможность создавать и использовать [пользовательские оценщики](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Вы можете оценить своё AI-приложение в среде разработки с помощью [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). При наличии тестового набора данных или целевого результата генерации вашего AI-приложения измеряются количественные показатели с использованием встроенных или пользовательских оценщиков на ваш выбор. Чтобы начать работу с Azure AI Evaluation SDK для оценки вашей системы, следуйте [руководству для быстрого старта](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). После выполнения оценки вы можете [визуализировать результаты в Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Товарные знаки

Этот проект может содержать товарные знаки или логотипы проектов, продуктов или сервисов. Авторизованное использование товарных знаков или логотипов Microsoft регулируется и должно соответствовать [Руководству по товарным знакам и брендам Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general). Использование товарных знаков или логотипов Microsoft в изменённых версиях этого проекта не должно вводить в заблуждение или подразумевать спонсорство Microsoft. Любое использование товарных знаков или логотипов третьих сторон подчиняется правилам этих третьих сторон.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.