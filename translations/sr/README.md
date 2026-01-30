# Phi Cookbook: Практични примери са Microsoft Phi моделима

[![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi је серија отворених AI модела развијених од стране Microsoft-а.

Phi је тренутно најмоћнији и најисплатиивији мали језички модел (SLM), са врхунским резултатима у више језика, резоновању, генерисању текста/ћаскања, кодирању, сликама, аудију и другим сценаријима.

Можете да имплементирате Phi у облаку или на уређајима на ивици, а лако можете да изградите генеративне AI апликације уз ограничену рачунарску снагу.

Пратите следеће кораке да започнете коришћење ових ресурса:
1. **Форкујте репозиторијум**: Кликните [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Клонирајте репозиторијум**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Придружите се Microsoft AI Discord заједници и упознајте стручњаке и друге програмере**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/sr/cover.eb18d1b9605d754b.webp)

### 🌐 Подршка за више језика

#### Подржано преко GitHub Action (Аутоматски и увек ажурирано)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](./README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Волите да клонирате локално?**

> Овај репозиторијум укључује преко 50 превода који значајно повећавају величину преузимања. Да бисте клонирали без превода, употребите sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Ово вам даје све што вам треба да завршите курс са знатно бржим преузимањем.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Садржај

- Увод
  - [Добро дошли у Phi породицу](./md/01.Introduction/01/01.PhiFamily.md)
  - [Постављање вашег окружења](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Разумевање кључних технологија](./md/01.Introduction/01/01.Understandingtech.md)
  - [AI безбедност за Phi моделе](./md/01.Introduction/01/01.AISafety.md)
  - [Подршка за Phi хардвер](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi модели и доступност на платформама](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Коришћење Guidance-ai и Phi](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace модели](https://github.com/marketplace/models)
  - [Azure AI каталог модела](https://ai.azure.com)

- Извођење Phi у различитим окружењима
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub модели](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry каталог модела](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry локално](./md/01.Introduction/02/07.FoundryLocal.md)

- Извођење Phi породице
    - [Извођење Phi на iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Извођење Phi на Android](./md/01.Introduction/03/Android_Inference.md)
    - [Извођење Phi на Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Извођење Phi на AI ПЦ](./md/01.Introduction/03/AIPC_Inference.md)
    - [Извођење Phi са Apple MLX Framework-ом](./md/01.Introduction/03/MLX_Inference.md)
    - [Извођење Phi на локалном серверу](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Извођење Phi на даљинском серверу користећи AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Извођење Phi са Rust-ом](./md/01.Introduction/03/Rust_Inference.md)
    - [Извођење Phi--Vision локално](./md/01.Introduction/03/Vision_Inference.md)
    - [Извођење Phi са Kaito AKS, Azure Containers (службена подршка)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Квантификација Phi породице](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Квантификација Phi-3.5 / 4 користећи llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Квантификација Phi-3.5 / 4 користећи Generative AI екстензије за onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Квантификација Phi-3.5 / 4 користећи Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Квантификација Phi-3.5 / 4 користећи Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Евалуација Phi
    - [Одржива AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry за евалуацију](./md/01.Introduction/05/AIFoundry.md)
    - [Коришћење Promptflow за евалуацију](./md/01.Introduction/05/Promptflow.md)
 
- RAG са Azure AI претрагом
    - [Како користити Phi-4-mini и Phi-4-мултимодал (RAG) са Azure AI претрагом](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Примери развоја Phi апликација
  - Текст и ћаскање апликације
    - Phi-4 примери 🆕
      - [📓] [Ћаскање са Phi-4-mini ONNX моделом](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Ћаскање са Phi-4 локалним ONNX моделом .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Console .NET апликација за ћаскање са Phi-4 ONNX користећи Sementic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 примери
      - [Локални ћаскање у прегледачу користећи Phi3, ONNX Runtime Web и WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino ћаскање](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Вишемоделски - интерактивни Phi-3-mini и OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - креирање обавијача и коришћење Phi-3 са MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Оптимизација модела - Како оптимизовати Phi-3-min модел за ONNX Runtime Web помоћу Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 апликација са Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 пример вишемоделске апликације за белешке покретане вештачком интелигенцијом](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Фино подешавање и интеграција прилагођених Phi-3 модела са Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Фино подешавање и интеграција прилагођених Phi-3 модела са Prompt flow у Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Процена фино подешеног Phi-3 / Phi-3.5 модела у Azure AI Foundry са фокусом на Microsoft-ове принципе одговорне вештачке интелигенције](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct пример језичке предикције (кинески/енглески)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Чатбот](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Коришћење Windows GPU за креирање Prompt flow решења са Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Коришћење Microsoft Phi-3.5 tflite за креирање Android апликације](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET пример коришћења локалног ONNX Phi-3 модела уз Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Конзолна чат .NET апликација са Semantic Kernel и Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK пример кода 
    - Phi-4 примери 🆕
      - [📓] [Генериши код пројекта користећи Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 примери
      - [Креирај свој Visual Studio Code GitHub Copilot Chat са Microsoft Phi-3 породицом](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Креирај свог Visual Studio Code Chat Copilot агента са Phi-3.5 користећи GitHub моделе](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Напредни примери резоновања
    - Phi-4 примери 🆕
      - [📓] [Phi-4-mini-reasoning или Phi-4-reasoning примери](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Фино подешавање Phi-4-mini-reasoning са Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Фино подешавање Phi-4-mini-reasoning са Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning са GitHub моделима](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-reasoning са Azure AI Foundry моделима](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Демонстрације
      - [Phi-4-mini демонстрације хостоване на Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal демонстрације хостоване на Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Вид примери
    - Phi-4 примери 🆕
      - [📓] [Користи Phi-4-multimodal за читање слика и генерисање кода](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 примери
      -  [📓][Phi-3-vision-текст слике у текст](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP уградња](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 рециклирање](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - визуелни језички асистент - са Phi3-Vision и OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision пример мулти-фрејма или мулти-слике](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision Локални ONNX модел користећи Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Мени базиран Phi-3 Vision Локални ONNX модел користећи Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Математички примери
    -  Phi-4-Mini-Flash-Reasoning-Instruct примери 🆕 [Математички демо са Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - Аудио примерци
    - Phi-4 примери 🆕
      - [📓] [Извлачење аудио транскриптова користећи Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal аудио пример](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal говорни превод пример](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET конзолна апликација користећи Phi-4-multimodal аудио за анализу аудио фајла и генерисање транскрипта](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE примерци
    - Phi-3 / 3.5 примери
      - [📓] [Phi-3.5 Мешавина експертских модела (MoEs) пример друштвених медија](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Израда Retrieval-Augmented Generation (RAG) пипелина са NVIDIA NIM Phi-3 MOE, Azure AI Search и LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Примери позивања функција
    - Phi-4 примери 🆕
      -  [📓] [Коришћење Позивања Функција са Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Коришћење Позивања Функција за креирање мулти-агената са Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Коришћење Позивања Функција са Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Коришћење Позивања Функција са ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Примери мешања вишемодалности
    - Phi-4 примери 🆕
      -  [📓] [Коришћење Phi-4-multimodal као технолошки новинар](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET конзолна апликација користећи Phi-4-multimodal за анализу слика](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Фино подешавање Phi примерка
  - [Сценарији фино подешавања](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Фино подешавање у поређењу са RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Фино подешавање - Нека Phi-3 постане индустријски стручњак](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Фино подешавање Phi-3 са AI Toolkit за VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Фино подешавање Phi-3 са Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Фино подешавање Phi-3 са Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Фино подешавање Phi-3 са QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Фино подешавање Phi-3 са Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Фино подешавање Phi-3 са Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Фино подешавање са Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Фино подешавање са Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Фино подешавање Phi-3-vision са Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Фино подешавање Phi-3 са Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Фино подешавање Phi-3-vision (званична подршка)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Фино подешавање Phi-3 са Kaito AKS, Azure Контејнери (званична подршка)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Фино подешавање Phi-3 и 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands on Lab
  - [Истраживање најсавременијих модела: LLM, SLM, локални развој и још много тога](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Ослобађање потенцијала NLP: Фино подешавање са Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Академски истраживачки радови и публикације
  - [Udžbenici su sve što vam treba II: tehnički izveštaj phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Tehnički izveštaj: Visoko sposoban jezički model lokalno na vašem telefonu](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Tehnički izveštaj](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Tehnički izveštaj: Kompaktni ali moćni multimodalni jezički modeli putem mešavine LoRAs](https://arxiv.org/abs/2503.01743)
  - [Optimizacija malih jezičkih modela za pozivanje funkcija u vozilu](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Fino podešavanje PHI-3 za odgovaranje na pitanja sa višestrukim izborom: metodologija, rezultati i izazovi](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning Tehnički izveštaj](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning Tehnički izveštaj](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Korišćenje Phi modela

### Phi na Azure AI Foundry

Možete naučiti kako da koristite Microsoft Phi i kako da napravite E2E rešenja na različitim hardverskim uređajima. Da iskusite Phi sami, počnite da eksperimentišete sa modelima i prilagođavate Phi za vaše scenarije koristeći [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Više informacija možete pronaći u Uputstvu za početak rada sa [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Igralište**
Svaki model ima posvećeno igralište za testiranje modela [Azure AI Playground](https://aka.ms/try-phi3).

### Phi na GitHub Modelima

Možete naučiti kako da koristite Microsoft Phi i kako da pravite E2E rešenja na različitim hardverskim uređajima. Da iskusite Phi sami, počnite sa igrom sa modelom i prilagođavanjem Phi za vaše scenarije koristeći [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Više informacija možete pronaći u Uputstvu za početak rada sa [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Igralište**
Svaki model ima posvećeno [igralište za testiranje modela](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi na Hugging Face

Model možete pronaći i na [Hugging Face](https://huggingface.co/microsoft)

**Igralište**  
[Hugging Chat igralište](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 Ostali kursevi

Naš tim proizvodi i druge kurseve! Pogledajte:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j za početnike](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js za početnike](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agenti
[![AZD za početnike](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI za početnike](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP za početnike](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agenti za početnike](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Serija Generativne veštačke inteligencije
[![Generativna veštačka inteligencija za početnike](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativna veštačka inteligencija (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativna veštačka inteligencija (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativna veštačka inteligencija (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### Osnovno učenje
[![Mašinsko učenje za početnike](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Nauka o podacima za početnike](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![Veštačka inteligencija za početnike](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kibernetička bezbednost za početnike](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Veb razvoj za početnike](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![Internet stvari za početnike](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR razvoj za početnike](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Serija Copilot
[![Copilot za AI uparenog programiranja](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot za C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot avantura](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Odgovorna veštačka inteligencija

Microsoft je posvećen tome da pomogne svojim korisnicima da koriste naše AI proizvode na odgovoran način, deleći svoja saznanja i gradeći partnerstva zasnovana na poverenju putem alata kao što su beleške o transparentnosti i procene uticaja. Mnogi od ovih resursa mogu se pronaći na [https://aka.ms/RAI](https://aka.ms/RAI).  
Microsoftov pristup odgovornoj veštačkoj inteligenciji zasnovan je na našim principima AI-a: pravičnost, pouzdanost i bezbednost, privatnost i sigurnost, inkluzivnost, transparentnost i odgovornost.

Veliki prirodni jezički, slikovni i govornički modeli - kao što su oni korišćeni u ovom primeru - mogu potencijalno da se ponašaju na načine koji nisu pravični, pouzdani ili mogu biti uvredljivi, što može dovesti do štete. Molimo vas da pogledate [belešku o transparentnosti Azure OpenAI servisa](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) da biste bili informisani o rizicima i ograničenjima.

Preporučeni pristup za ublažavanje ovih rizika jeste uključivanje sigurnosnog sistema u vašu arhitekturu koji može otkriti i sprečiti štetno ponašanje. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) pruža nezavisni sloj zaštite koji može da detektuje štetan sadržaj generisan od strane korisnika i AI-a u aplikacijama i uslugama. Azure AI Content Safety uključuje API-je za tekst i slike koji omogućavaju otkrivanje štetnog materijala. U okviru Azure AI Foundry, servis Content Safety omogućava vam da pregledate, istražite i isprobate uzorke koda za otkrivanje štetnog sadržaja u različitim modalitetima. Sledeća [dokumentacija za brzo pokretanje](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vodi vas kroz proces postavljanja zahteva servisu.

Još jedan aspekt koji treba uzeti u obzir je ukupna performansa aplikacije. Kod višemodalnih i višemodelskih aplikacija, pod performansom podrazumevamo da sistem radi onako kako vi i vaši korisnici očekujete, uključujući i ne generisanje štetnih rezultata. Važno je proceniti performanse vaše ukupne aplikacije koristeći [evaluatore performansi, kvaliteta, rizika i bezbednosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Takođe imate mogućnost da kreirate i ocenjujete pomoću [prilagođenih evaluatora](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).
Можете да процените своју АИ апликацију у вашем развојном окружењу користећи [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Дато било који тест скуп података или циљ, генерације ваше генеративне АИ апликације се квантитативно мере уграђеним евалуаторима или прилагођеним евалуаторима по вашем избору. Да бисте започели са azure ai evaluation sdk за процену вашег система, можете пратити [ваквни водич](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Када извршите покретање евалуације, можете [визуелизовати резултате у Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Заставни знакови

Овај пројекат може садржати заштитне знакове или логотипе за пројекте, производе или услуге. Овлашћена употреба Microsoft заштитних знакова или логотипа подлеже и мора се придржавати [Microsoft-ових смерница за заштитне знакове и бренд](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general). Употреба Microsoft заштитних знакова или логотипа у модификованим верзијама овог пројекта не сме изазивати забуну нити имплицирати Microsoft покровитељство. Свако коришћење заштитних знакова или логотипа трећих страна подлеже политикама тих трећих страна.

## Добијање помоћи

Ако запнете или имате било каквих питања о изградњи АИ апликација, придружите се:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Ако имате повратне информације о производу или грешке приликом изградње, посетите:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:  
Овај документ је преведен коришћењем АИ преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате на уму да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Не одговарамо за било каква неразумевања или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->