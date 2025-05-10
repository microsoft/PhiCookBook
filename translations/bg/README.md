<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1cab9282e04f2e1c388a38dca7763c16",
  "translation_date": "2025-05-09T04:13:25+00:00",
  "source_file": "README.md",
  "language_code": "bg"
}
-->
# Phi Cookbook: Практически примери с Phi моделите на Microsoft

[![Отворете и използвайте примерите в GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Отворете в Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)


[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi е серия от отворени AI модели, разработени от Microsoft.

В момента Phi е най-мощният и ефективен малък езиков модел (SLM), с отлични резултати в многоезична поддръжка, логическо мислене, генериране на текст/чат, програмиране, изображения, аудио и други сценарии.

Можете да разположите Phi в облака или на крайни устройства и лесно да създавате генеративни AI приложения с ограничени изчислителни ресурси.

Следвайте тези стъпки, за да започнете да използвате тези ресурси:
1. **Fork-нете хранилището**: Кликнете [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Клонирайте хранилището**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Присъединете се към Microsoft AI Discord общността и се срещнете с експерти и други разработчици**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.bg.png)

## 🌐 Многоезична поддръжка

### Поддържа се чрез GitHub Action (Автоматично и винаги актуално)

[Френски](../fr/README.md) | [Испански](../es/README.md) | [Немски](../de/README.md) | [Руски](../ru/README.md) | [Арабски](../ar/README.md) | [Персийски (Фарси)](../fa/README.md) | [Урду](../ur/README.md) | [Китайски (опростен)](../zh/README.md) | [Китайски (традиционен, Макао)](../mo/README.md) | [Китайски (традиционен, Хонконг)](../hk/README.md) | [Китайски (традиционен, Тайван)](../tw/README.md) | [Японски](../ja/README.md) | [Корейски](../ko/README.md) | [Хинди](../hi/README.md)

### Поддържа се чрез CLI
[Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](./README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)


## Съдържание

- Въведение
- [Добре дошли в семейството Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Настройване на вашата среда](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Разбиране на ключовите технологии](./md/01.Introduction/01/01.Understandingtech.md)
  - [AI безопасност за Phi модели](./md/01.Introduction/01/01.AISafety.md)
  - [Поддръжка на хардуер Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi модели и наличност на различни платформи](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Използване на Guidance-ai и Phi](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace модели](https://github.com/marketplace/models)
  - [Azure AI каталог на модели](https://ai.azure.com)

- Извеждане на Phi в различни среди
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub модели](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry каталог на модели](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Извеждане на Phi семейство
    - [Извеждане на Phi в iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Извеждане на Phi в Android](./md/01.Introduction/03/Android_Inference.md)
    - [Извеждане на Phi в Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Извеждане на Phi в AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Извеждане на Phi с Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Извеждане на Phi на локален сървър](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Извеждане на Phi на отдалечен сървър с AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Извеждане на Phi с Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Извеждане на Phi--Vision локално](./md/01.Introduction/03/Vision_Inference.md)
    - [Извеждане на Phi с Kaito AKS, Azure контейнери (официална поддръжка)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Квантуване на Phi семейство](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Квантуване на Phi-3.5 / 4 с llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Квантуване на Phi-3.5 / 4 с помощта на разширения за генеративен AI за onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Квантуване на Phi-3.5 / 4 с Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Квантуване на Phi-3.5 / 4 с Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Оценка на Phi
- [Response AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry за оценка](./md/01.Introduction/05/AIFoundry.md)
    - [Използване на Promptflow за оценка](./md/01.Introduction/05/Promptflow.md)
 
- RAG с Azure AI Search
    - [Как да използвате Phi-4-mini и Phi-4-multimodal(RAG) с Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Примери за разработка на Phi приложения
  - Текстови и чат приложения
    - Phi-4 Примери 🆕
      - [📓] [Чат с Phi-4-mini ONNX модел](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Чат с локален Phi-4 ONNX модел .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Чат .NET конзолно приложение с Phi-4 ONNX и Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 Примери
      - [Локален чатбот в браузъра с Phi3, ONNX Runtime Web и WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Чат](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Мулти модел - Интерактивен Phi-3-mini и OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Създаване на обвивка и използване на Phi-3 с MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Оптимизация на модел - Как да оптимизирате Phi-3-mini модел за ONNX Runtime Web с Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 приложение с Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3 мулти модел AI приложение за бележки - пример](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Фина настройка и интеграция на персонализирани Phi-3 модели с Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Фина настройка и интеграция на персонализирани Phi-3 модели с Prompt flow в Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Оценка на фино настроения Phi-3 / Phi-3.5 модел в Azure AI Foundry с фокус върху принципите на отговорен AI на Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Пример за езикова прогноза с Phi-3.5-mini-instruct (китайски/английски)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG чатбот](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Използване на Windows GPU за създаване на Prompt flow решение с Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Използване на Microsoft Phi-3.5 tflite за създаване на Android приложение](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Пример Q&A .NET с локален ONNX Phi-3 модел с Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Конзолно чат .NET приложение с Semantic Kernel и Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Примери с Azure AI Inference SDK базирани на код 
    - Phi-4 Примери 🆕
      - [📓] [Генериране на проектен код с Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 Примери
      - [Създайте свой Visual Studio Code GitHub Copilot чат с Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Създайте собствен Visual Studio Code Chat Copilot агент с Phi-3.5 чрез GitHub модели](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Примери за напреднали разсъждения
    - Phi-4 Примери 🆕
      - [📓] [Phi-4-mini-reasoning или Phi-4-reasoning примери](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Фина настройка на Phi-4-mini-reasoning с Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Фина настройка на Phi-4-mini-reasoning с Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning с GitHub модели](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
- [📓] [Phi-4-mini разсъждения с Azure AI Foundry модели](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Демонстрации
      - [Phi-4-mini демонстрации, хоствани в Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-мултимодални демонстрации, хоствани в Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Примери за зрение
    - Phi-4 Примери 🆕
      - [📓] [Използване на Phi-4-мултимодален за четене на изображения и генериране на код](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 Примери
      -  [📓][Phi-3-vision - преобразуване на изображение в текст](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP вграждане](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [ДЕМО: Phi-3 рециклиране](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - визуален езиков асистент - с Phi3-Vision и OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision пример с много кадри или много изображения](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision локален ONNX модел с Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Меню базиран Phi-3 Vision локален ONNX модел с Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Примери за аудио
    - Phi-4 Примери 🆕
      - [📓] [Извличане на аудио транскрипти с Phi-4-мултимодален](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-мултимодален аудио пример](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-мултимодален пример за речев превод](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET конзолно приложение, използващо Phi-4-мултимодален аудио за анализ на аудио файл и генериране на транскрипция](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE Примери
    - Phi-3 / 3.5 Примери
      - [📓] [Phi-3.5 модели с микс от експерти (MoEs) пример за социални медии](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Създаване на Retrieval-Augmented Generation (RAG) pipeline с NVIDIA NIM Phi-3 MOE, Azure AI Search и LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
  - Примери за извикване на функции
    - Phi-4 Примери 🆕
      -  [📓] [Използване на извикване на функции с Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Използване на извикване на функции за създаване на мултиагенти с Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Използване на извикване на функции с Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
  - Примери за мултимодално смесване
    - Phi-4 Примери 🆕
      -  [📓] [Използване на Phi-4-мултимодален като технологичен журналист](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET конзолно приложение, използващо Phi-4-мултимодален за анализ на изображения](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Финно настройване на Phi Примери
  - [Сценарии за финно настройване](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Финно настройване срещу RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Финно настройване: Нека Phi-3 стане индустриален експерт](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Финно настройване на Phi-3 с AI Toolkit за VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Финно настройване на Phi-3 с Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
- [Фино настройване на Phi-3 с Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Фино настройване на Phi-3 с QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Фино настройване на Phi-3 с Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Фино настройване на Phi-3 с Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Фино настройване с Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Фино настройване с Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Фино настройване на Phi-3-vision с Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Фино настройване на Phi-3 с Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Фино настройване на Phi-3-vision (официална поддръжка)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Фино настройване на Phi-3 с Kaito AKS, Azure Containers (официална поддръжка)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Фино настройване на Phi-3 и 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands on Lab
  - [Изследване на най-новите модели: LLMs, SLMs, локална разработка и още](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Отключване на потенциала на NLP: Фино настройване с Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Академични изследователски статии и публикации
  - [Textbooks Are All You Need II: phi-1.5 технически доклад](https://arxiv.org/abs/2309.05463)
  - [Phi-3 технически доклад: Много способен езиков модел локално на вашия телефон](https://arxiv.org/abs/2404.14219)
  - [Phi-4 технически доклад](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini технически доклад: Компактен, но мощен мултимодален езиков модел чрез Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Оптимизиране на малки езикови модели за извикване на функции в превозни средства](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Фино настройване на PHI-3 за отговаряне на въпроси с множествен избор: Методология, резултати и предизвикателства](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning технически доклад](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning технически доклад](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Използване на Phi модели

### Phi в Azure AI Foundry

Можете да научите как да използвате Microsoft Phi и как да изграждате цялостни решения за различни хардуерни устройства. За да изпробвате Phi, започнете с работа с моделите и персонализиране на Phi за вашите сценарии чрез [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Повече информация можете да намерите в Запознаване с [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Playground**  
Всеки модел има собствена тестова среда за проверка на модела [Azure AI Playground](https://aka.ms/try-phi3).

### Phi в GitHub модели

Можете да научите как да използвате Microsoft Phi и как да изграждате цялостни решения за различни хардуерни устройства. За да изпробвате Phi, започнете с работа с модела и персонализиране на Phi за вашите сценарии чрез [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Повече информация можете да намерите в Запознаване с [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**  
Всеки модел има собствен [playground за тестване на модела](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi в Hugging Face

Моделът е достъпен и в [Hugging Face](https://huggingface.co/microsoft)

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Отговорен AI

Microsoft се ангажира да помага на клиентите си да използват нашите AI продукти отговорно, като споделя наученото и изгражда партньорства, основани на доверие чрез инструменти като Transparency Notes и Impact Assessments. Много от тези ресурси могат да бъдат намерени на [https://aka.ms/RAI](https://aka.ms/RAI).  
Подходът на Microsoft към отговорния AI е базиран на нашите принципи за справедливост, надеждност и безопасност, поверителност и сигурност, включване, прозрачност и отчетност.
Големи модели за естествен език, изображения и реч – като тези, използвани в този пример – могат потенциално да се държат по начини, които са несправедливи, ненадеждни или обидни, което може да причини вреди. Моля, консултирайте се с [Бележката за прозрачност на Azure OpenAI услугата](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), за да се информирате за рисковете и ограниченията.

Препоръчителният подход за намаляване на тези рискове е да включите в архитектурата си система за безопасност, която може да открива и предотвратява вредно поведение. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) предоставя независим слой защита, способен да разпознава вредно съдържание, генерирано от потребители и от AI, в приложения и услуги. Azure AI Content Safety включва текстови и образни API-та, които ви позволяват да откривате вреден материал. В рамките на Azure AI Foundry, услугата Content Safety ви дава възможност да разглеждате, изследвате и изпробвате примерен код за откриване на вредно съдържание в различни модалности. Следната [документация за бърз старт](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ви води през процеса на изпращане на заявки към услугата.

Друг аспект, който трябва да се вземе предвид, е общото представяне на приложението. При мултимодални и мултимоделни приложения, под производителност разбираме, че системата работи според очакванията на вас и вашите потребители, включително да не генерира вредни резултати. Важно е да оцените представянето на цялото приложение, използвайки [Оценители за производителност, качество, риск и безопасност](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Също така имате възможност да създавате и оценявате с [персонализирани оценители](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Можете да оцените вашето AI приложение в средата за разработка, използвайки [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Като имате тестов набор от данни или цел, генерациите на вашето генеративно AI приложение се измерват количествено с вградени или персонализирани оценители по ваш избор. За да започнете с Azure AI Evaluation SDK и да оцените вашата система, можете да следвате [ръководството за бърз старт](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). След като изпълните оценъчен цикъл, можете да [визуализирате резултатите в Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Търговски марки

Този проект може да съдържа търговски марки или лога на проекти, продукти или услуги. Употребата на търговски марки или лога на Microsoft е разрешена само при спазване на [Правилата за търговски марки и бранд на Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general). Използването на търговски марки или лога на Microsoft в модифицирани версии на този проект не трябва да създава объркване или да намеква за спонсорство от Microsoft. Всяко използване на търговски марки или лога на трети страни подлежи на правилата на съответните трети страни.

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или неправилни тълкувания, произтичащи от използването на този превод.