<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c07bb4c3c89a36c9be332a065a9a33c",
  "translation_date": "2025-07-16T15:36:39+00:00",
  "source_file": "README.md",
  "language_code": "uk"
}
-->
# Phi Cookbook: Практичні приклади з моделями Phi від Microsoft

[![Відкрити та використовувати приклади в GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![Відкрити в Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Учасники GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![Проблеми GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![Запити на злиття GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Спостерігачі GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![Форки GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![Зірки GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi — це серія відкритих моделей штучного інтелекту, розроблених Microsoft.

На сьогодні Phi є найпотужнішою та найбільш економічною малою мовною моделлю (SLM), яка демонструє відмінні результати у багатомовності, логічному мисленні, генерації тексту/чатів, кодуванні, роботі з зображеннями, аудіо та інших сценаріях.

Ви можете розгортати Phi у хмарі або на пристроях на периферії, а також легко створювати генеративні AI-додатки з обмеженими обчислювальними ресурсами.

Виконайте ці кроки, щоб почати роботу з цим ресурсом:  
1. **Форкніть репозиторій**: натисніть [![Форки GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **Клонуйте репозиторій**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Приєднуйтесь до спільноти Microsoft AI в Discord, щоб поспілкуватися з експертами та іншими розробниками**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.uk.png)

### 🌐 Підтримка багатьох мов

#### Підтримується через GitHub Action (автоматично та завжди актуально)

[Французька](../fr/README.md) | [Іспанська](../es/README.md) | [Німецька](../de/README.md) | [Російська](../ru/README.md) | [Арабська](../ar/README.md) | [Перська (фарсі)](../fa/README.md) | [Урду](../ur/README.md) | [Китайська (спрощена)](../zh/README.md) | [Китайська (традиційна, Макао)](../mo/README.md) | [Китайська (традиційна, Гонконг)](../hk/README.md) | [Китайська (традиційна, Тайвань)](../tw/README.md) | [Японська](../ja/README.md) | [Корейська](../ko/README.md) | [Гінді](../hi/README.md)  
[Бенгальська](../bn/README.md) | [Маратхі](../mr/README.md) | [Непальська](../ne/README.md) | [Пенджабі (гурмухі)](../pa/README.md) | [Португальська (Португалія)](../pt/README.md) | [Португальська (Бразилія)](../br/README.md) | [Італійська](../it/README.md) | [Польська](../pl/README.md) | [Турецька](../tr/README.md) | [Грецька](../el/README.md) | [Тайська](../th/README.md) | [Шведська](../sv/README.md) | [Данська](../da/README.md) | [Норвезька](../no/README.md) | [Фінська](../fi/README.md) | [Голландська](../nl/README.md) | [Іврит](../he/README.md) | [В’єтнамська](../vi/README.md) | [Індонезійська](../id/README.md) | [Малайська](../ms/README.md) | [Тагальська (філіппінська)](../tl/README.md) | [Свахілі](../sw/README.md) | [Угорська](../hu/README.md) | [Чеська](../cs/README.md) | [Словацька](../sk/README.md) | [Румунська](../ro/README.md) | [Болгарська](../bg/README.md) | [Сербська (кирилиця)](../sr/README.md) | [Хорватська](../hr/README.md) | [Словенська](../sl/README.md)

## Зміст

- Вступ  
  - [Ласкаво просимо до сім’ї Phi](./md/01.Introduction/01/01.PhiFamily.md)  
  - [Налаштування вашого середовища](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [Розуміння ключових технологій](./md/01.Introduction/01/01.Understandingtech.md)  
  - [Безпека ШІ для моделей Phi](./md/01.Introduction/01/01.AISafety.md)  
  - [Підтримка апаратного забезпечення Phi](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [Моделі Phi та їх доступність на різних платформах](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [Використання Guidance-ai та Phi](./md/01.Introduction/01/01.Guidance.md)  
  - [Моделі на GitHub Marketplace](https://github.com/marketplace/models)  
  - [Каталог моделей Azure AI](https://ai.azure.com)

- Виконання Phi в різних середовищах  
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)  
    -  [Моделі GitHub](./md/01.Introduction/02/02.GitHubModel.md)  
    -  [Каталог моделей Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)  
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)  
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)  
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Виконання Phi Family  
    - [Виконання Phi на iOS](./md/01.Introduction/03/iOS_Inference.md)  
    - [Виконання Phi на Android](./md/01.Introduction/03/Android_Inference.md)  
    - [Виконання Phi на Jetson](./md/01.Introduction/03/Jetson_Inference.md)  
    - [Виконання Phi на AI ПК](./md/01.Introduction/03/AIPC_Inference.md)  
    - [Виконання Phi з Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)  
    - [Виконання Phi на локальному сервері](./md/01.Introduction/03/Local_Server_Inference.md)  
    - [Виконання Phi на віддаленому сервері за допомогою AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)  
    - [Виконання Phi з Rust](./md/01.Introduction/03/Rust_Inference.md)  
    - [Виконання Phi–Vision локально](./md/01.Introduction/03/Vision_Inference.md)  
    - [Виконання Phi з Kaito AKS, Azure Containers (офіційна підтримка)](./md/01.Introduction/03/Kaito_Inference.md)  
-  [Квантифікація Phi Family](./md/01.Introduction/04/QuantifyingPhi.md)  
    - [Квантифікація Phi-3.5 / 4 за допомогою llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
    - [Квантифікація Phi-3.5 / 4 за допомогою розширень Generative AI для onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
    - [Квантифікація Phi-3.5 / 4 за допомогою Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
    - [Квантифікація Phi-3.5 / 4 за допомогою Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Оцінка Phi  
    - [Відповідальний ШІ](./md/01.Introduction/05/ResponsibleAI.md)  
    - [Azure AI Foundry для оцінки](./md/01.Introduction/05/AIFoundry.md)  
    - [Використання Promptflow для оцінки](./md/01.Introduction/05/Promptflow.md)

- RAG з Azure AI Search  
    - [Як використовувати Phi-4-mini та Phi-4-multimodal (RAG) з Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Приклади розробки додатків на основі Phi  
  - Текстові та чат-додатки  
    - Phi-4 Приклади 🆕  
      - [📓] [Чат з моделлю Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Чат з локальною моделлю Phi-4 ONNX .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [Чат .NET консольний додаток з Phi-4 ONNX за допомогою Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 Приклади  
      - [Локальний чат-бот у браузері з Phi3, ONNX Runtime Web та WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [OpenVino Чат](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [Мульти-модель - інтерактивний Phi-3-mini та OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - створення обгортки та використання Phi-3 з MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [Оптимізація моделі - як оптимізувати Phi-3-min для ONNX Runtime Web за допомогою Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [WinUI3 додаток з Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [WinUI3 мульти-модельний додаток для нотаток з AI](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Тонке налаштування та інтеграція кастомних моделей Phi-3 з Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Тонке налаштування та інтеграція кастомних моделей Phi-3 з Prompt flow в Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Оцінка тонко налаштованої моделі Phi-3 / Phi-3.5 в Azure AI Foundry з акцентом на принципи відповідального ШІ Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Приклад прогнозування мови Phi-3.5-mini-instruct (китайська/англійська)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG чат-бот](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Використання Windows GPU для створення рішення Prompt flow з Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Використання Microsoft Phi-3.5 tflite для створення Android додатку](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Приклад Q&A .NET з локальною ONNX моделлю Phi-3 за допомогою Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Консольний чат .NET додаток з Semantic Kernel та Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK Приклади на основі коду  
  - Phi-4 Приклади 🆕  
    - [📓] [Генерація коду проекту з використанням Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Phi-3 / 3.5 Приклади  
    - [Створіть власний чат GitHub Copilot для Visual Studio Code з Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [Створіть власного агента чату для Visual Studio Code з Phi-3.5 за допомогою моделей GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- Приклади розширеного мислення  
  - Phi-4 Приклади 🆕  
    - [📓] [Приклади Phi-4-mini-reasoning або Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Тонке налаштування Phi-4-mini-reasoning з Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Тонке налаштування Phi-4-mini-reasoning з Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Phi-4-mini-reasoning з моделями GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Phi-4-mini-reasoning з моделями Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- Демонстрації  
    - [Phi-4-mini демонстрації, розміщені на Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Phi-4-multimodal демонстрації, розміщені на Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- Приклади для Vision  
  - Phi-4 Приклади 🆕  
    - [📓] [Використання Phi-4-multimodal для читання зображень та генерації коду](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Phi-3 / 3.5 Приклади  
    - [📓][Phi-3-vision: перетворення тексту з зображення в текст](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [ДЕМО: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - Візуальний мовний асистент з Phi3-Vision та OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision приклад з мультифреймами або мультизображеннями](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Phi-3 Vision локальна ONNX модель з Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Меню на основі Phi-3 Vision локальна ONNX модель з Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- Приклади з математики  
  - Phi-4-Mini-Flash-Reasoning-Instruct Приклади 🆕 [Демо з математики з Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)  

- Приклади з аудіо  
  - Phi-4 Приклади 🆕  
    - [📓] [Витяг аудіотранскриптів за допомогою Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Phi-4-multimodal аудіо приклад](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Phi-4-multimodal приклад перекладу мови](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [Консольний .NET додаток, що використовує Phi-4-multimodal Audio для аналізу аудіофайлу та генерації транскрипту](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- MOE Приклади  
  - Phi-3 / 3.5 Приклади  
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) приклад для соціальних мереж](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [Створення Retrieval-Augmented Generation (RAG) пайплайну з NVIDIA NIM Phi-3 MOE, Azure AI Search та LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- Приклади виклику функцій  
  - Phi-4 Приклади 🆕  
    - [📓] [Використання виклику функцій з Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Використання виклику функцій для створення мультиагентів з Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Використання виклику функцій з Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [Використання виклику функцій з ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- Приклади мультимодального змішування  
  - Phi-4 Приклади 🆕  
    - [📓] [Використання Phi-4-multimodal як технологічного журналіста](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [Консольний .NET додаток, що використовує Phi-4-multimodal для аналізу зображень](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Тонке налаштування Phi Прикладів  
  - [Сценарії тонкого налаштування](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [Тонке налаштування проти RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Тонке налаштування: нехай Phi-3 стане експертом у галузі](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [Тонке налаштування Phi-3 з AI Toolkit для VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Тонке налаштування Phi-3 з Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Тонке налаштування Phi-3 з Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [Тонке налаштування Phi-3 з QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Тонке налаштування Phi-3 з Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Тонке налаштування Phi-3 з Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Тонке налаштування з Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Практична лабораторія з тонкого налаштування з Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)  
  - [Тонке налаштування Phi-3-vision з Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Тонке налаштування Phi-3 з Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Тонке налаштування Phi-3-vision (офіційна підтримка)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Тонке налаштування Phi-3 з Kaito AKS, Azure Containers (офіційна підтримка)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Тонке налаштування Phi-3 та 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- Практична лабораторія  
  - [Вивчення передових моделей: LLMs, SLMs, локальна розробка та інше](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [Розкриття потенціалу NLP: тонке налаштування з Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- Академічні дослідження та публікації  
  - [Textbooks Are All You Need II: технічний звіт phi-1.5](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 Технічний звіт: потужна мовна модель локально на вашому телефоні](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 Технічний звіт](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini Технічний звіт: компактні, але потужні мультимодальні мовні моделі через Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [Оптимізація малих мовних моделей для виклику функцій у транспортних засобах](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) Тонке налаштування PHI-3 для відповідей на питання з множинним вибором: методологія, результати та виклики](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning Технічний звіт](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning Технічний звіт](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Використання моделей Phi

### Phi на Azure AI Foundry

Ви можете дізнатися, як використовувати Microsoft Phi та як створювати комплексні рішення для різних апаратних пристроїв. Щоб спробувати Phi на власному досвіді, почніть з експериментів з моделями та налаштування Phi під ваші сценарії за допомогою [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Більше інформації можна знайти в розділі Початок роботи з [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Пісочниця**  
Кожна модель має власну пісочницю для тестування [Azure AI Playground](https://aka.ms/try-phi3).

### Phi на GitHub Models

Ви можете дізнатися, як використовувати Microsoft Phi та як створювати комплексні рішення для різних апаратних пристроїв. Щоб спробувати Phi на власному досвіді, почніть з експериментів з моделлю та налаштування Phi під ваші сценарії за допомогою [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Більше інформації можна знайти в розділі Початок роботи з [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Пісочниця**  
Кожна модель має власну [пісочницю для тестування моделі](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi на Hugging Face

Модель також доступна на [Hugging Face](https://huggingface.co/microsoft)

**Пісочниця**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Відповідальний ШІ

Microsoft прагне допомагати своїм клієнтам відповідально використовувати наші продукти ШІ, ділитися набутим досвідом та будувати партнерські відносини на основі довіри за допомогою інструментів, таких як Transparency Notes та Impact Assessments. Багато з цих ресурсів доступні за адресою [https://aka.ms/RAI](https://aka.ms/RAI).  
Підхід Microsoft до відповідального ШІ базується на наших принципах ШІ: справедливість, надійність і безпека, конфіденційність і захист, інклюзивність, прозорість та підзвітність.

Великі моделі природної мови, зображень і мовлення — як ті, що використовуються в цьому прикладі — можуть потенційно поводитися несправедливо, ненадійно або образливо, що може призводити до шкоди. Будь ласка, ознайомтеся з [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), щоб дізнатися про ризики та обмеження.

Рекомендований підхід до зменшення цих ризиків — включити в архітектуру систему безпеки, яка може виявляти та запобігати шкідливій поведінці. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) забезпечує незалежний рівень захисту, здатний виявляти шкідливий контент, створений користувачами або ШІ, у додатках і сервісах. Azure AI Content Safety включає API для тексту та зображень, які дозволяють виявляти шкідливі матеріали. У межах Azure AI Foundry сервіс Content Safety дає змогу переглядати, досліджувати та тестувати приклади коду для виявлення шкідливого контенту в різних модальностях. Наступна [документація для швидкого старту](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) допоможе вам зробити запити до сервісу.

Ще один аспект, який варто враховувати — загальна продуктивність додатку. У багатомодальних і багатомодельних додатках продуктивність означає, що система працює так, як ви та ваші користувачі очікують, включно з тим, що не генерує шкідливі результати. Важливо оцінювати продуктивність вашого додатку за допомогою [оцінювачів продуктивності, якості, ризиків і безпеки](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Ви також можете створювати та оцінювати за допомогою [кастомних оцінювачів](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Ви можете оцінити свій ШІ-додаток у середовищі розробки за допомогою [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Використовуючи тестовий набір даних або ціль, генерації вашого генеративного ШІ-додатку кількісно вимірюються вбудованими або кастомними оцінювачами на ваш вибір. Щоб почати роботу з Azure AI Evaluation SDK для оцінки вашої системи, скористайтеся [керівництвом для швидкого старту](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Після запуску оцінювання ви можете [візуалізувати результати в Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Торгові марки

Цей проєкт може містити торгові марки або логотипи проєктів, продуктів чи сервісів. Авторизоване використання торгових марок або логотипів Microsoft підпорядковується та має відповідати [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Використання торгових марок або логотипів Microsoft у змінених версіях цього проєкту не повинно викликати плутанину або створювати враження спонсорства Microsoft. Використання торгових марок або логотипів третіх сторін підпорядковується політикам відповідних третіх сторін.

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.