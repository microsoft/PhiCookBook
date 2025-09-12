<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T14:22:27+00:00",
  "source_file": "README.md",
  "language_code": "uk"
}
-->
# Phi Cookbook: Практичні приклади з моделями Phi від Microsoft

Phi — це серія відкритих AI моделей, розроблених Microsoft.

Phi наразі є найпотужнішою та найекономічнішою малою мовною моделлю (SLM), яка демонструє чудові результати в багатомовності, логічному мисленні, генерації тексту/чатів, програмуванні, роботі з зображеннями, аудіо та іншими сценаріями.

Ви можете розгорнути Phi у хмарі або на пристроях периферії, а також легко створювати додатки генеративного AI з обмеженими обчислювальними ресурсами.

Дотримуйтесь цих кроків, щоб почати використовувати ці ресурси:
1. **Форкніть репозиторій**: Натисніть [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Клонуйте репозиторій**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Приєднайтеся до спільноти Microsoft AI Discord та зустріньтеся з експертами та іншими розробниками**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 Підтримка багатомовності

#### Підтримується через GitHub Action (автоматично та завжди актуально)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) 
[Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)

## Зміст

- Вступ
  - [Ласкаво просимо до сім'ї Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Налаштування середовища](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Розуміння ключових технологій](./md/01.Introduction/01/01.Understandingtech.md)
  - [Безпека AI для моделей Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Підтримка обладнання для Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Моделі Phi та доступність на різних платформах](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Використання Guidance-ai та Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Моделі на GitHub Marketplace](https://github.com/marketplace/models)
  - [Каталог моделей Azure AI](https://ai.azure.com)

- Використання Phi в різних середовищах
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [Моделі GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Каталог моделей Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Використання сімейства Phi
    - [Використання Phi на iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Використання Phi на Android](./md/01.Introduction/03/Android_Inference.md)
    - [Використання Phi на Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Використання Phi на AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Використання Phi з Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Використання Phi на локальному сервері](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Використання Phi на віддаленому сервері за допомогою AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Використання Phi з Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Використання Phi--Vision локально](./md/01.Introduction/03/Vision_Inference.md)
    - [Використання Phi з Kaito AKS, Azure Containers (офіційна підтримка)](./md/01.Introduction/03/Kaito_Inference.md)

-  [Квантифікація сімейства Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Квантифікація Phi-3.5 / 4 за допомогою llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Квантифікація Phi-3.5 / 4 за допомогою розширень Generative AI для onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Квантифікація Phi-3.5 / 4 за допомогою Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Квантифікація Phi-3.5 / 4 за допомогою Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Оцінка Phi
    - [Відповідальний AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Оцінка за допомогою Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [Використання Promptflow для оцінки](./md/01.Introduction/05/Promptflow.md)

- RAG з Azure AI Search
    - [Як використовувати Phi-4-mini та Phi-4-multimodal (RAG) з Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Зразки розробки додатків Phi
  - Текстові та чат-додатки
    - Зразки Phi-4 🆕
      - [📓] [Чат з Phi-4-mini ONNX Model](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Чат з Phi-4 локально ONNX Model .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Консольний додаток .NET з Phi-4 ONNX за допомогою Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Зразки Phi-3 / 3.5
      - [Локальний чат-бот у браузері з Phi3, ONNX Runtime Web та WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [Чат OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Мульти-модель - інтерактивний Phi-3-mini та OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - створення обгортки та використання Phi-3 з MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Оптимізація моделі - як оптимізувати модель Phi-3-min для ONNX Runtime Web за допомогою Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Додаток WinUI3 з Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [Зразок додатку WinUI3 Multi Model AI Powered Notes](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Налаштування та інтеграція власних моделей Phi-3 з Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Налаштування та інтеграція власних моделей Phi-3 з Prompt flow в Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Оцінка налаштованої моделі Phi-3 / Phi-3.5 в Azure AI Foundry з акцентом на принципи відповідального AI від Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Зразок прогнозування мов Phi-3.5-mini-instruct (китайська/англійська)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Чат-бот Phi-3.5-Instruct WebGPU RAG](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Використання Windows GPU для створення рішення Prompt flow з Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Використання Microsoft Phi-3.5 tflite для створення Android-додатку](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Приклад Q&A .NET з локальною моделлю ONNX Phi-3 за допомогою Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Консольний чат-додаток .NET із Semantic Kernel та Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Зразки коду SDK для інференсу Azure AI 
  - Зразки Phi-4 🆕
    - [📓] [Генерація коду проекту за допомогою Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Зразки Phi-3 / 3.5
    - [Створіть власний чат GitHub Copilot у Visual Studio Code з сімейством Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [Створіть власного агента чату Copilot у Visual Studio Code з Phi-3.5 за допомогою моделей GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- Зразки розширеного логічного мислення
  - Зразки Phi-4 🆕
    - [📓] [Зразки Phi-4-mini-reasoning або Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Налаштування Phi-4-mini-reasoning за допомогою Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Налаштування Phi-4-mini-reasoning за допомогою Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning з моделями GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Phi-4-mini-reasoning з моделями Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- Демонстрації
    - [Демонстрації Phi-4-mini, розміщені на Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Демонстрації Phi-4-multimodal, розміщені на Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- Зразки Vision
  - Зразки Phi-4 🆕
    - [📓] [Використання Phi-4-multimodal для читання зображень та генерації коду](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Зразки Phi-3 / 3.5
    - [📓][Phi-3-vision-Image text to text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [ДЕМОНСТРАЦІЯ: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Візуальний мовний асистент - з Phi3-Vision та OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision multi-frame або multi-image sample](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Phi-3 Vision Локальна модель ONNX за допомогою Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Меню на основі Phi-3 Vision Локальна модель ONNX за допомогою Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

- Зразки Math
  - Phi-4-Mini-Flash-Reasoning-Instruct Samples 🆕 [Демонстрація Math з Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)

- Зразки Audio
  - Зразки Phi-4 🆕
    - [📓] [Витяг транскриптів аудіо за допомогою Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Зразок аудіо Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Зразок перекладу мовлення Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET консольний додаток з використанням Phi-4-multimodal Audio для аналізу аудіофайлу та створення транскрипту](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- Зразки MOE
  - Зразки Phi-3 / 3.5
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) Зразок соціальних медіа](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [Створення Retrieval-Augmented Generation (RAG) Pipeline з NVIDIA NIM Phi-3 MOE, Azure AI Search та LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- Зразки виклику функцій
  - Зразки Phi-4 🆕
    - [📓] [Використання виклику функцій з Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Використання виклику функцій для створення мультиагентів з Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Використання виклику функцій з Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [Використання виклику функцій з ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- Зразки змішування мультимодальності
  - Зразки Phi-4 🆕
    - [📓] [Використання Phi-4-multimodal як технологічного журналіста](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET консольний додаток з використанням Phi-4-multimodal для аналізу зображень](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Налаштування Phi Зразки
  - [Сценарії налаштування](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Налаштування vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Налаштування Phi-3 для того, щоб стати експертом у галузі](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Налаштування Phi-3 за допомогою AI Toolkit для VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Налаштування Phi-3 за допомогою Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Налаштування Phi-3 за допомогою Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Налаштування Phi-3 за допомогою QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Налаштування Phi-3 за допомогою Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Налаштування Phi-3 за допомогою Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Налаштування за допомогою Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Налаштування за допомогою Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Налаштування Phi-3-vision за допомогою Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Налаштування Phi-3 за допомогою Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Налаштування Phi-3-vision (офіційна підтримка)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Налаштування Phi-3 з Kaito AKS, Azure Containers (офіційна підтримка)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Налаштування Phi-3 та 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Практичні лабораторії
  - [Дослідження передових моделей: LLMs, SLMs, локальна розробка та інше](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Розкриття потенціалу NLP: Налаштування за допомогою Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Академічні дослідницькі статті та публікації
  - [Textbooks Are All You Need II: технічний звіт phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Технічний звіт Phi-3: висококваліфікована мовна модель локально на вашому телефоні](https://arxiv.org/abs/2404.14219)
  - [Технічний звіт Phi-4](https://arxiv.org/abs/2412.08905)
  - [Технічний звіт Phi-4-Mini: компактні, але потужні мультимодальні мовні моделі через Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Оптимізація малих мовних моделей для виклику функцій у транспортних засобах](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Налаштування PHI-3 для відповідей на запитання з множинним вибором: методологія, результати та виклики](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning Технічний звіт](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning Технічний звіт](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)  

## Використання моделей Phi  

### Phi на Azure AI Foundry  

Ви можете дізнатися, як використовувати Microsoft Phi і створювати E2E рішення для різних апаратних пристроїв. Щоб спробувати Phi самостійно, почніть з тестування моделей і налаштування Phi для ваших сценаріїв, використовуючи [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Більше інформації можна знайти в розділі "Початок роботи з [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)".  

**Playground**  
Кожна модель має спеціальний майданчик для тестування моделі [Azure AI Playground](https://aka.ms/try-phi3).  

### Phi на GitHub Models  

Ви можете дізнатися, як використовувати Microsoft Phi і створювати E2E рішення для різних апаратних пристроїв. Щоб спробувати Phi самостійно, почніть з тестування моделі і налаштування Phi для ваших сценаріїв, використовуючи [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Більше інформації можна знайти в розділі "Початок роботи з [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)".  

**Playground**  
Кожна модель має спеціальний [майданчик для тестування моделі](/md/02.QuickStart/GitHubModel_QuickStart.md).  

### Phi на Hugging Face  

Модель також доступна на [Hugging Face](https://huggingface.co/microsoft).  

**Playground**  
[Майданчик Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct).  

## Відповідальний AI  

Microsoft прагне допомогти нашим клієнтам використовувати наші AI-продукти відповідально, ділитися досвідом і будувати партнерства, засновані на довірі, через інструменти, такі як Transparency Notes і Impact Assessments. Багато з цих ресурсів можна знайти за адресою [https://aka.ms/RAI](https://aka.ms/RAI).  
Підхід Microsoft до відповідального AI базується на наших принципах AI: справедливість, надійність і безпека, конфіденційність і захист, інклюзивність, прозорість і відповідальність.  

Масштабні моделі природної мови, зображень і мовлення - такі як ті, що використовуються в цьому прикладі - можуть потенційно поводитися несправедливо, ненадійно або образливо, що може призводити до шкоди. Будь ласка, ознайомтеся з [Transparency note сервісу Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), щоб бути поінформованими про ризики та обмеження.  

Рекомендований підхід до зменшення цих ризиків - включити систему безпеки в вашу архітектуру, яка може виявляти і запобігати шкідливій поведінці. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) забезпечує незалежний рівень захисту, здатний виявляти шкідливий контент, створений користувачами або AI, у додатках і сервісах. Azure AI Content Safety включає текстові та графічні API, які дозволяють виявляти шкідливі матеріали. У межах Azure AI Foundry сервіс Content Safety дозволяє переглядати, досліджувати і тестувати зразки коду для виявлення шкідливого контенту в різних модальностях. Наступна [документація швидкого старту](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) допоможе вам зробити запити до сервісу.  

Ще один аспект, який слід враховувати, - це загальна продуктивність додатка. У багатомодальних і багатомодельних додатках продуктивність означає, що система працює так, як ви і ваші користувачі очікуєте, включаючи запобігання генерації шкідливих результатів. Важливо оцінити продуктивність вашого додатка за допомогою [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Ви також можете створювати і оцінювати за допомогою [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).  

Ви можете оцінити ваш AI-додаток у середовищі розробки, використовуючи [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Використовуючи тестовий набір даних або ціль, генерації вашого додатка з генеративним AI кількісно вимірюються за допомогою вбудованих або користувацьких оцінювачів на ваш вибір. Щоб почати роботу з Azure AI Evaluation SDK для оцінки вашої системи, ви можете скористатися [посібником швидкого старту](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Після виконання оцінки ви можете [візуалізувати результати в Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).  

## Торгові марки  

Цей проект може містити торгові марки або логотипи для проектів, продуктів або послуг. Авторизоване використання торгових марок або логотипів Microsoft підлягає і повинно відповідати [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Використання торгових марок або логотипів Microsoft у модифікованих версіях цього проекту не повинно викликати плутанину або припускати спонсорство Microsoft. Будь-яке використання торгових марок або логотипів третіх сторін підлягає політикам цих третіх сторін.  

---

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, звертаємо вашу увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.