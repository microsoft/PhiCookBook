# Кулінарна книга Phi: Практичні приклади з моделями Phi від Microsoft

[![Відкрити та використовувати приклади в GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Відкрити в Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Учасники GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Проблеми GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Запити на Pull GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Ласкаво просимо](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Спостерігачі GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Форки GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Зірки GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Discord Microsoft Foundry](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi — це серія відкритих AI-моделей, розроблених Microsoft.

На сьогодні Phi є найпотужнішою та найефективнішою за вартістю маленькою мовною моделлю (SLM), з дуже хорошими результатами у багатомовних завданнях, логічному мисленні, генерації тексту/чатів, кодуванні, роботі з зображеннями, аудіо та інших сценаріях.

Ви можете розгорнути Phi в хмарі або на пристроях на межі мережі, а також легко створювати генеративні AI-застосунки з обмеженими обчислювальними ресурсами.

Виконайте ці кроки, щоб почати працювати з цими ресурсами:
1. **Форкніть репозиторій**: Натисніть [![Форки GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Клонуйте репозиторій**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Приєднуйтесь до спільноти Microsoft AI Discord та спілкуйтесь з експертами й іншими розробниками**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/uk/cover.eb18d1b9605d754b.webp)

### 🌐 Підтримка багатьох мов

#### Підтримується через GitHub Action (Автоматично та завжди актуально)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](./README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Віддаєте перевагу локальному клонуванню?**
>
> У цьому репозиторії є понад 50 мовних перекладів, що значно збільшує розмір завантаження. Щоб клонувати без перекладів, використовуйте sparse checkout:
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
> Це дає вам усе необхідне для проходження курсу з набагато швидшим завантаженням.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Зміст

- Вступ
  - [Ласкаво просимо до сімейства Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Налаштування вашого середовища](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Розуміння ключових технологій](./md/01.Introduction/01/01.Understandingtech.md)
  - [Безпека ШІ для моделей Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Підтримка апаратного забезпечення Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Моделі Phi та їх доступність на різних платформах](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Використання Guidance-ai та Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Моделі на GitHub Marketplace](https://github.com/marketplace/models)
  - [Каталог моделей Azure AI](https://ai.azure.com)

- Запуск Phi в різних середовищах
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [Моделі GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Каталог моделей Microsoft Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Запуск сімейства Phi
    - [Запуск Phi на iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Запуск Phi на Android](./md/01.Introduction/03/Android_Inference.md)
    - [Запуск Phi на Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Запуск Phi на AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Запуск Phi з Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Запуск Phi на локальному сервері](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Запуск Phi на віддаленому сервері з AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Запуск Phi із Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Запуск Phi--Vision локально](./md/01.Introduction/03/Vision_Inference.md)
    - [Запуск Phi з Kaito AKS, Azure Containers (офіційна підтримка)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Квантифікація сімейства Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Квантування Phi-3.5 / 4 за допомогою llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Квантування Phi-3.5 / 4 з розширеннями Generative AI для onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Квантування Phi-3.5 / 4 з Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Квантування Phi-3.5 / 4 з Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Оцінка Phi
    - [Відповідальний ШІ](./md/01.Introduction/05/ResponsibleAI.md)
    - [Microsoft Foundry для оцінки](./md/01.Introduction/05/AIFoundry.md)
    - [Використання Promptflow для оцінки](./md/01.Introduction/05/Promptflow.md)
 
- RAG з Azure AI Search
    - [Як використовувати Phi-4-mini та Phi-4-мультимодальний (RAG) з Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)
    - [Zero-Cloud локальний гібридний RAG з SQLite FTS5 та phi-4-mini](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-mini_Local_Hybrid_RAG_SQLite_FTS5.ipynb)

- Зразки розробки застосунків Phi
  - Текстові та чат-застосунки
    - Зразки Phi-4 
      - [📓] [Чат з моделлю Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Чат з локальною моделлю Phi-4 ONNX .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Консольний чат-додаток .NET з Phi-4 ONNX за допомогою Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)

    - Phi-3 / 3.5 Зразки
      - [Локальний чат-бот у браузері з використанням Phi3, ONNX Runtime Web та WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Мульти модель - інтерактивний Phi-3-mini та OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Створення оболонки та використання Phi-3 з MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Оптимізація моделі - Як оптимізувати модель Phi-3-min для ONNX Runtime Web за допомогою Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 додаток з Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 Мульти модель AI Powered Notes App Sample](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Тонке налаштування та інтеграція кастомних моделей Phi-3 з Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Тонке налаштування та інтеграція кастомних моделей Phi-3 з Prompt flow у Microsoft Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Оцінка тонко налаштованих моделей Phi-3 / Phi-3.5 у Microsoft Foundry з акцентом на принципи Відповідального AI від Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Приклад прогнозування мови Phi-3.5-mini-instruct (китайська/англійська)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Чат-бот](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Використання GPU Windows для створення рішення Prompt flow з Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Використання Microsoft Phi-3.5 tflite для створення Android-додатку](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Приклад Q&A .NET з використанням локальної ONNX моделі Phi-3 через Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Консольний чат .NET додаток з Semantic Kernel та Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Приклади коду Azure AI Inference SDK 
    - Зразки Phi-4 
      - [📓] [Генерація коду проекту з використанням Phi-4-мультимодального](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Зразки Phi-3 / 3.5
      - [Створіть власний чат Copilot GitHub у Visual Studio Code з Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Створіть власного агента Chat Copilot для Visual Studio Code з Phi-3.5 за моделями GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Приклади розширеного мислення
    - Зразки Phi-4 
      - [📓] [Phi-4-mini-мислення або Phi-4-мислення зразки](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Тонке налаштування Phi-4-mini-мислення з Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Тонке налаштування Phi-4-mini-мислення з Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-мислення з моделями GitHub](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-мислення з моделями Microsoft Foundry](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Демонстрації
      - [Phi-4-mini демо, розміщені на Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-мультимодальні демо, розміщені на Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Приклади зору
    - Зразки Phi-4 
      - [📓] [Використання Phi-4-мультимодального для читання зображень і генерації коду](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Зразки Phi-3 / 3.5
      -  [📓][Phi-3-vision-Перетворення тексту на текст із зображенням](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Переробка](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - візуальний мовний асистент - з Phi3-Vision та OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision мультифрейм або мультизображення приклад](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision Локальна ONNX модель з використанням Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Меню на основі Phi-3 Vision Локальна ONNX модель з використанням Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Приклади мислення-зором
    - Phi-4-Мислення-Зор-15B 
      - [📓] [Використання Phi-4-Мислення-Зор-15B для виявлення порушень правил переходу в недозволеному місці](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb)
      - [📓] [Використання Phi-4-Мислення-Зор-15B для математики](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb)
      - [📓] [Використання Phi-4-Мислення-Зор-15B для виявлення UI](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb)

  - Приклади математики
    -  Зразки Phi-4-Mini-Flash-Reasoning-Instruct  [Математична демонстрація з Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - Приклади аудіо
    - Зразки Phi-4 
      - [📓] [Витяг аудіотранскриптів з Phi-4-мультимодального](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-мультимодальний аудіо приклад](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-мультимодальний приклад перекладу мови](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET консольний додаток з використанням Phi-4-мультимодального аудіо для аналізу аудіофайлу та генерації транскрипту](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE Приклади
    - Зразки Phi-3 / 3.5
      - [📓] [Phi-3.5 Моделі змішання експертів (MoEs) приклад з соціальних мереж](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Створення конвеєра із генерацією з використанням RAG, NVIDIA NIM Phi-3 MOE, Azure AI Search та LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Функціональні зразки виклику
    - Зразки Phi-4 🆕
      -  [📓] [Використання виклику функції з Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Використання виклику функції для створення мультиагентів з Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Використання виклику функції з Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Використання виклику функції з ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Приклади змішування мультимодальних моделей
    - Зразки Phi-4 🆕
      -  [📓] [Використання Phi-4-мультимодального як технологічного журналіста](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET консольний додаток з використанням Phi-4-мультимодального для аналізу зображень](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Тонке налаштування Phi зразків
  - [Сценарії тонкого налаштування](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Тонке налаштування проти RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Тонке налаштування: нехай Phi-3 стане галузевим експертом](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Тонке налаштування Phi-3 з AI Toolkit для VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Тонке налаштування Phi-3 з Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Тонке налаштування Phi-3 з Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Тонке налаштування Phi-3 з QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Тонке налаштування Phi-3 з Microsoft Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Тонке налаштування Phi-3 з Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Тонке налаштування з Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Тонке налаштування з Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Тонке налаштування Phi-3-vision з Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)

  - [Тонке налаштування Phi-3 за допомогою Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Тонке налаштування Phi-3-vision (офіційна підтримка)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Тонке налаштування Phi-3 з Kaito AKS, Azure Containers (офіційна підтримка)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Тонке налаштування Phi-3 та 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Практична лабораторія
  - [Вивчення новітніх моделей: LLMs, SLMs, локальна розробка та інше](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Розкриття потенціалу NLP: тонке налаштування з Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Наукові дослідні роботи та публікації
  - [Підручники — все, що потрібно II: технічний звіт phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Технічний звіт Phi-3: високо здібна мовна модель локально на вашому телефоні](https://arxiv.org/abs/2404.14219)
  - [Технічний звіт Phi-4](https://arxiv.org/abs/2412.08905)
  - [Технічний звіт Phi-4-Mini: компактні, але потужні мультимодальні мовні моделі за допомогою Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Оптимізація малих мовних моделей для виклику функцій у транспортному засобі](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Тонке налаштування PHI-3 для відповідей на запитання з вибором відповіді: методологія, результати та виклики](https://arxiv.org/abs/2501.01588)
  - [Технічний звіт Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Технічний звіт Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Використання моделей Phi

### Phi на Microsoft Foundry

Ви можете навчитися користуватися Microsoft Phi та створювати комплексні рішення для різних апаратних пристроїв. Щоб самостійно випробувати Phi, почніть гратися з моделями та налаштовувати Phi для своїх сценаріїв за допомогою [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai), докладніше можна дізнатися в посібнику Getting Started with [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Плейграунд**
Кожна модель має власний майданчик для тестування - [Azure AI Playground](https://aka.ms/try-phi3).

### Phi на GitHub Models

Ви можете навчитися користуватися Microsoft Phi та створювати комплексні рішення для різних апаратних пристроїв. Щоб самостійно випробувати Phi, почніть гратися з моделлю та налаштовувати Phi для своїх сценаріїв за допомогою [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo), докладніше можна дізнатися в посібнику Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Плейграунд**
Кожна модель має присвячений [плейграунд для тестування моделі](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi на Hugging Face

Також модель можна знайти на [Hugging Face](https://huggingface.co/microsoft)

**Плейграунд**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 Інші курси

Наша команда також створює інші курси! Ознайомтеся:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j для початківців](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js для початківців](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain для початківців](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Агенти
[![AZD для початківців](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI для початківців](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP для початківців](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Агенти для початківців](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Серія Generative AI
[![Generative AI для початківців](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Основи навчання
[![ML для початківців](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science для початківців](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI для початківців](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Кібербезпека для початківців](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Веб-розробка для початківців](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT для початківців](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR розробка для початківців](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Серія Copilot
[![Copilot для AI парного програмування](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot для C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Відповідальний ШІ 

Microsoft прагне допомогти своїм клієнтам відповідально використовувати продукти ШІ, ділитися набутим досвідом і будувати партнерства на основі довіри за допомогою інструментів, таких як Transparency Notes та Impact Assessments. Багато з цих ресурсів можна знайти за адресою [https://aka.ms/RAI](https://aka.ms/RAI).
Підхід Microsoft до відповідального ШІ ґрунтується на наших принципах ШІ: справедливість, надійність і безпека, конфіденційність і безпека, інклюзивність, прозорість і підзвітність.

Великі моделі природної мови, зображень і мовлення — як ті, що використовуються у цьому прикладі — можуть потенційно поводитися несправедливо, ненадійно або образливо, що може спричинити шкоду. Будь ласка, ознайомтеся з [Приміткою прозорості сервісу Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), щоб бути поінформованими про ризики та обмеження.


Рекомендований підхід до пом'якшення цих ризиків полягає у включенні системи безпеки у вашу архітектуру, яка може виявляти та запобігати шкідливій поведінці. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) забезпечує незалежний рівень захисту, здатний виявляти шкідливий контент, створений користувачами та ШІ у додатках і сервісах. Azure AI Content Safety включає API для тексту та зображень, які дозволяють виявляти шкідливий матеріал. У межах Microsoft Foundry служба Content Safety дозволяє переглядати, досліджувати та випробовувати прикладний код для виявлення шкідливого контенту в різних модальностях. Наступна [документація швидкого старту](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) проводить вас через процес надсилання запитів до служби.

Ще одним аспектом, який слід враховувати, є загальна продуктивність застосунку. У випадку мультимодальних та мультимодельних застосунків під продуктивністю ми розуміємо, що система працює так, як ви та ваші користувачі очікують, включно з тим, що вона не генерує шкідливий вихід. Важливо оцінити продуктивність вашого загального застосунку за допомогою [оцінювачів продуктивності, якості, ризику та безпеки](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Ви також маєте можливість створювати та оцінювати за допомогою [власних оцінювачів](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Ви можете оцінити ваш AI-застосунок у вашому середовищі розробки, використовуючи [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). За наявності тестового набору даних або цілі, генерації вашого генеративного AI-застосунку кількісно вимірюються за допомогою вбудованих або власних оцінювачів на ваш вибір. Щоб розпочати роботу з azure ai evaluation sdk для оцінки вашої системи, ви можете слідувати за [інструкцією швидкого старту](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Після запуску оцінювання ви можете [візуалізувати результати в Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Торгові марки

Цей проект може містити торгові марки або логотипи проектів, продуктів або сервісів. Дозволене використання торгових марок або логотипів Microsoft підпорядковується та має відповідати [Керівництву Microsoft щодо торгових марок і брендів](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Використання торгових марок або логотипів Microsoft у змінених версіях цього проекту не повинно викликати плутанину або натякати на спонсорство Microsoft. Будь-яке використання торгових марок або логотипів сторонніх організацій підпорядковується політикам цих сторонніх організацій.

## Отримання допомоги

Якщо ви застрягли або маєте запитання щодо створення AI-застосунків, приєднуйтесь:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Якщо у вас є відгуки про продукт або помилки під час розробки, відвідайте:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->