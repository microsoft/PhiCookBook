<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4987daf30687ad3850757c9eae3f5411",
  "translation_date": "2025-10-17T10:38:01+00:00",
  "source_file": "README.md",
  "language_code": "sr"
}
-->
# Phi Кувар: Практични примери са Microsoft-овим Phi моделима

Phi је серија отворених AI модела које је развио Microsoft.

Phi је тренутно најмоћнији и најисплативији мали језички модел (SLM), са одличним резултатима у вишејезичности, резоновању, генерисању текста/ћаскања, кодирању, сликама, аудио и другим сценаријима.

Можете применити Phi у облаку или на уређајима на ивици мреже, и лако изградити генеративне AI апликације са ограниченом рачунарском снагом.

Пратите ове кораке да бисте започели коришћење ових ресурса:
1. **Fork-ујте репозиторијум**: Кликните [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Клонирајте репозиторијум**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Придружите се Microsoft AI Discord заједници и упознајте стручњаке и друге програмере**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 Подршка за више језика

#### Подржано преко GitHub Action (Аутоматски и увек ажурирано)

[Арапски](../ar/README.md) | [Бенгалски](../bn/README.md) | [Бугарски](../bg/README.md) | [Бирмански (Мјанмар)](../my/README.md) | [Кинески (поједностављени)](../zh/README.md) | [Кинески (традиционални, Хонг Конг)](../hk/README.md) | [Кинески (традиционални, Макао)](../mo/README.md) | [Кинески (традиционални, Тајван)](../tw/README.md) | [Хрватски](../hr/README.md) | [Чешки](../cs/README.md) | [Дански](../da/README.md) | [Холандски](../nl/README.md) | [Естонски](../et/README.md) | [Фински](../fi/README.md) | [Француски](../fr/README.md) | [Немачки](../de/README.md) | [Грчки](../el/README.md) | [Хебрејски](../he/README.md) | [Хинди](../hi/README.md) | [Мађарски](../hu/README.md) | [Индонежански](../id/README.md) | [Италијански](../it/README.md) | [Јапански](../ja/README.md) | [Корејски](../ko/README.md) | [Литвански](../lt/README.md) | [Малајски](../ms/README.md) | [Марати](../mr/README.md) | [Непалски](../ne/README.md) | [Норвешки](../no/README.md) | [Персијски (Фарси)](../fa/README.md) | [Пољски](../pl/README.md) | [Португалски (Бразил)](../br/README.md) | [Португалски (Португал)](../pt/README.md) | [Пенџабски (Гурмуки)](../pa/README.md) | [Румунски](../ro/README.md) | [Руски](../ru/README.md) | [Српски (Ћирилица)](./README.md) | [Словачки](../sk/README.md) | [Словеначки](../sl/README.md) | [Шпански](../es/README.md) | [Свахили](../sw/README.md) | [Шведски](../sv/README.md) | [Тагалог (Филипински)](../tl/README.md) | [Тамилски](../ta/README.md) | [Тајландски](../th/README.md) | [Турски](../tr/README.md) | [Украјински](../uk/README.md) | [Урду](../ur/README.md) | [Вијетнамски](../vi/README.md)

## Садржај

- Увод
  - [Добродошли у Phi породицу](./md/01.Introduction/01/01.PhiFamily.md)
  - [Подешавање вашег окружења](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Разумевање кључних технологија](./md/01.Introduction/01/01.Understandingtech.md)
  - [AI безбедност за Phi моделе](./md/01.Introduction/01/01.AISafety.md)
  - [Подршка за Phi хардвер](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi модели и доступност на различитим платформама](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Коришћење Guidance-ai и Phi](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace модели](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- Инференција Phi у различитим окружењима
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub модели](./md/01.Introduction/02/02.GitHubModel.md)
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
    - [Одговорни AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry за евалуацију](./md/01.Introduction/05/AIFoundry.md)
    - [Коришћење Promptflow за евалуацију](./md/01.Introduction/05/Promptflow.md)
 
- RAG са Azure AI Search
    - [Како користити Phi-4-mini и Phi-4-multimodal (RAG) са Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Примери развоја Phi апликација
  - Текст & Ћаскање апликације
    - Phi-4 Примери 🆕
      - [📓] [Ћаскање са Phi-4-mini ONNX моделом](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Ћаскање са Phi-4 локалним ONNX моделом .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Ћаскање .NET Console апликација са Phi-4 ONNX користећи Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 Примери
      - [Локални chatbot у прегледачу користећи Phi3, ONNX Runtime Web и WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Ћаскање](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Мулти модел - Интерактивни Phi-3-mini и OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Изградња омотача и коришћење Phi-3 са MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Оптимизација модела - Како оптимизовати Phi-3-min модел за ONNX Runtime Web са Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [WinUI3 Апликација са Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [WinUI3 Апликација за белешке са вишеструким AI моделима - пример](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Фино подешавање и интеграција прилагођених Phi-3 модела са Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Фино подешавање и интеграција прилагођених Phi-3 модела са Prompt flow у Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Евалуација фино подешаног Phi-3 / Phi-3.5 модела у Azure AI Foundry са фокусом на принципе одговорне AI технологије компаније Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct пример предвиђања језика (кинески/енглески)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Коришћење Windows GPU за креирање Prompt flow решења са Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Коришћење Microsoft Phi-3.5 tflite за креирање Android апликације](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Q&A .NET пример са локалним ONNX Phi-3 моделом користећи Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Конзолна chat .NET апликација са Semantic Kernel и Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK Примери кода
  - Phi-4 Примери 🆕
    - [📓] [Генерисање кода пројекта користећи Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5 Примери
    - [Креирајте свој Visual Studio Code GitHub Copilot Chat са Microsoft Phi-3 породицом](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [Креирајте свој Visual Studio Code Chat Copilot Agent са Phi-3.5 користећи GitHub моделе](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- Напредни примери резоновања
  - Phi-4 Примери 🆕
    - [📓] [Phi-4-mini-reasoning или Phi-4-reasoning Примери](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Фино подешавање Phi-4-mini-reasoning са Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Фино подешавање Phi-4-mini-reasoning са Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning са GitHub моделима](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Phi-4-mini-reasoning са Azure AI Foundry моделима](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- Демо
    - [Phi-4-mini демо на Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Phi-4-multimodal демо на Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- Примери за визију
  - Phi-4 Примери 🆕
    - [📓] [Коришћење Phi-4-multimodal за читање слика и генерисање кода](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Phi-3 / 3.5 Примери
    - [📓][Phi-3-vision-Претварање текста из слике у текст](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [ДЕМО: Phi-3 Рециклирање](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Визуелни језички асистент - са Phi3-Vision и OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision пример са више фрејмова или више слика](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Phi-3 Vision Локални ONNX Модел користећи Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Мени базиран Phi-3 Vision Локални ONNX Модел користећи Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

- Примери за математику
  - Phi-4-Mini-Flash-Reasoning-Instruct Примери 🆕 [Демо за математику са Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)

- Примери за аудио
  - Phi-4 Примери 🆕
    - [📓] [Извлачење транскрипта аудио записа користећи Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodal Аудио Пример](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal Пример превода говора](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET конзолна апликација користећи Phi-4-multimodal Аудио за анализу аудио фајла и генерисање транскрипта](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOE Примери
  - Phi-3 / 3.5 Примери
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) Пример за друштвене мреже](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [Креирање Retrieval-Augmented Generation (RAG) Платформе са NVIDIA NIM Phi-3 MOE, Azure AI Search, и LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- Примери за позивање функција
  - Phi-4 Примери 🆕
    - [📓] [Коришћење позивања функција са Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Коришћење позивања функција за креирање мулти-агената са Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Коришћење позивања функција са Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [Коришћење позивања функција са ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- Примери за мешање мултимодалности
  - Phi-4 Примери 🆕
    - [📓] [Коришћење Phi-4-multimodal као технолошки новинар](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET конзолна апликација користећи Phi-4-multimodal за анализу слика](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Фино подешавање Phi Примера
  - [Сценарији фино подешавања](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Фино подешавање vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Фино подешавање: Нека Phi-3 постане индустријски експерт](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
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
  - [Фино подешавање Phi-3 са Kaito AKS, Azure Containers (званична подршка)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Фино подешавање Phi-3 и 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Практична лабораторија
  - [Истраживање најновијих модела: LLMs, SLMs, локални развој и више](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Откључавање NLP потенцијала: Фино подешавање са Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Академски истраживачки радови и публикације
  - [Textbooks Are All You Need II: phi-1.5 технички извештај](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Технички извештај: Високо способан језички модел локално на вашем телефону](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Технички извештај](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Технички извештај: Компактан али моћан мултимодални језички модел кроз Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
- [Optimizacija malih jezičkih modela za pozivanje funkcija u vozilu](https://arxiv.org/abs/2501.02342)  
- [(WhyPHI) Fino podešavanje PHI-3 za odgovaranje na pitanja sa višestrukim izborom: metodologija, rezultati i izazovi](https://arxiv.org/abs/2501.01588)  
- [Tehnički izveštaj o Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Tehnički izveštaj o Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)  

## Korišćenje Phi modela  

### Phi na Azure AI Foundry  

Možete naučiti kako da koristite Microsoft Phi i kako da izgradite E2E rešenja na različitim hardverskim uređajima. Da biste sami iskusili Phi, počnite sa testiranjem modela i prilagođavanjem Phi za vaše scenarije koristeći [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Više informacija možete pronaći u vodiču [Kako početi sa Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).  

**Igralište**  
Svaki model ima posvećeno igralište za testiranje modela [Azure AI Playground](https://aka.ms/try-phi3).  

### Phi na GitHub modelima  

Možete naučiti kako da koristite Microsoft Phi i kako da izgradite E2E rešenja na različitim hardverskim uređajima. Da biste sami iskusili Phi, počnite sa testiranjem modela i prilagođavanjem Phi za vaše scenarije koristeći [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Više informacija možete pronaći u vodiču [Kako početi sa GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).  

**Igralište**  
Svaki model ima posvećeno [igralište za testiranje modela](/md/02.QuickStart/GitHubModel_QuickStart.md).  

### Phi na Hugging Face  

Model možete pronaći i na [Hugging Face](https://huggingface.co/microsoft).  

**Igralište**  
[Igralište za Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct).  

## Odgovorna AI  

Microsoft se zalaže za pomoć korisnicima u odgovornom korišćenju naših AI proizvoda, deljenje naučenih lekcija i izgradnju poverenja kroz alate kao što su Beleške o transparentnosti i Procene uticaja. Mnogi od ovih resursa mogu se pronaći na [https://aka.ms/RAI](https://aka.ms/RAI).  
Pristup Microsoft-a odgovornoj AI zasnovan je na našim principima AI: pravičnost, pouzdanost i sigurnost, privatnost i bezbednost, inkluzivnost, transparentnost i odgovornost.  

Veliki jezički, slikovni i govorni modeli - poput onih korišćenih u ovom uzorku - mogu potencijalno delovati na način koji je nepravedan, nepouzdan ili uvredljiv, što može izazvati štetu. Molimo vas da konsultujete [Belešku o transparentnosti za Azure OpenAI servis](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) kako biste se informisali o rizicima i ograničenjima.  

Preporučeni pristup za ublažavanje ovih rizika je uključivanje sistema za bezbednost u vašu arhitekturu koji može otkriti i sprečiti štetno ponašanje. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) pruža nezavisni sloj zaštite, sposoban da otkrije štetan sadržaj generisan od strane korisnika ili AI u aplikacijama i uslugama. Azure AI Content Safety uključuje API-je za tekst i slike koji omogućavaju otkrivanje štetnog materijala. U okviru Azure AI Foundry, servis za bezbednost sadržaja omogućava vam da pregledate, istražujete i isprobate uzorke koda za otkrivanje štetnog sadržaja u različitim modalitetima. Sledeća [dokumentacija za brzi početak](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vodi vas kroz proces slanja zahteva servisu.  

Još jedan aspekt koji treba uzeti u obzir je ukupna performansa aplikacije. Kod aplikacija sa više modaliteta i modela, performansa podrazumeva da sistem funkcioniše kako vi i vaši korisnici očekujete, uključujući i to da ne generiše štetne rezultate. Važno je proceniti performanse vaše aplikacije koristeći [Evaluatore performansi i kvaliteta, kao i rizika i bezbednosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Takođe imate mogućnost da kreirate i procenjujete sa [prilagođenim evaluatorima](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).  

Možete proceniti vašu AI aplikaciju u razvojnom okruženju koristeći [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Na osnovu testnog skupa podataka ili cilja, generacije vaše generativne AI aplikacije se kvantitativno mere koristeći ugrađene ili prilagođene evaluatore po vašem izboru. Da biste započeli sa Azure AI Evaluation SDK za procenu vašeg sistema, možete pratiti [vodič za brzi početak](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Nakon što izvršite procenu, možete [vizualizovati rezultate u Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).  

## Zaštitni znakovi  

Ovaj projekat može sadržavati zaštitne znakove ili logotipe za projekte, proizvode ili usluge. Ovlašćena upotreba Microsoft-ovih zaštitnih znakova ili logotipa podložna je i mora slediti [Microsoft-ove smernice za zaštitne znakove i brend](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Upotreba Microsoft-ovih zaštitnih znakova ili logotipa u modifikovanim verzijama ovog projekta ne sme izazvati zabunu ili implicirati sponzorstvo od strane Microsoft-a. Svaka upotreba zaštitnih znakova ili logotipa trećih strana podložna je politikama tih trećih strana.  

## Pomoć  

Ako se zaglavite ili imate bilo kakva pitanja o izradi AI aplikacija, pridružite se:  

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)  

Ako imate povratne informacije o proizvodu ili greške tokom izrade, posetite:  

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)  

---

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуге за превођење вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу произаћи из коришћења овог превода.