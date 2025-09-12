<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T14:23:56+00:00",
  "source_file": "README.md",
  "language_code": "lt"
}
-->
# Phi Receptų Knyga: Praktiniai Pavyzdžiai su Microsoft Phi Modeliais

Phi yra Microsoft sukurti atvirojo kodo dirbtinio intelekto modeliai.

Phi šiuo metu yra galingiausias ir ekonomiškiausias mažas kalbos modelis (SLM), pasižymintis puikiais rezultatais daugiakalbystės, logikos, teksto/pokalbių generavimo, kodavimo, vaizdų, garso ir kitose srityse.

Jūs galite diegti Phi debesyje arba kraštiniuose įrenginiuose ir lengvai kurti generatyvaus dirbtinio intelekto programas su ribotais skaičiavimo ištekliais.

Sekite šiuos žingsnius, kad pradėtumėte naudotis šiais ištekliais:
1. **Fork'uokite saugyklą**: Spustelėkite [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Klonuokite saugyklą**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Prisijunkite prie Microsoft AI Discord bendruomenės ir susipažinkite su ekspertais bei kitais kūrėjais**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 Daugiakalbė Parama

#### Palaikoma per GitHub Action (Automatizuota ir visada atnaujinta)

[Prancūzų](../fr/README.md) | [Ispanų](../es/README.md) | [Vokiečių](../de/README.md) | [Rusų](../ru/README.md) | [Arabų](../ar/README.md) | [Persų (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Kinų (Supaprastinta)](../zh/README.md) | [Kinų (Tradicinė, Makao)](../mo/README.md) | [Kinų (Tradicinė, Honkongas)](../hk/README.md) | [Kinų (Tradicinė, Taivanas)](../tw/README.md) | [Japonų](../ja/README.md) | [Korėjiečių](../ko/README.md) | [Hindi](../hi/README.md) 
[Bengalų](../bn/README.md) | [Marathi](../mr/README.md) | [Nepalų](../ne/README.md) | [Pundžabi (Gurmukhi)](../pa/README.md) | [Portugalų (Portugalija)](../pt/README.md) | [Portugalų (Brazilija)](../br/README.md) | [Italų](../it/README.md) | [Lenkų](../pl/README.md) | [Turkų](../tr/README.md) | [Graikų](../el/README.md) | [Tajų](../th/README.md) | [Švedų](../sv/README.md) | [Danų](../da/README.md) | [Norvegų](../no/README.md) | [Suomių](../fi/README.md) | [Olandų](../nl/README.md) | [Hebrajų](../he/README.md) | [Vietnamiečių](../vi/README.md) | [Indoneziečių](../id/README.md) | [Malajų](../ms/README.md) | [Tagalog (Filipiniečių)](../tl/README.md) | [Svahilių](../sw/README.md) | [Vengrų](../hu/README.md) | [Čekų](../cs/README.md) | [Slovakų](../sk/README.md) | [Rumunų](../ro/README.md) | [Bulgarų](../bg/README.md) | [Serbų (Kirilica)](../sr/README.md) | [Kroatų](../hr/README.md) | [Slovėnų](../sl/README.md)

## Turinys

- Įvadas
  - [Sveiki atvykę į Phi šeimą](./md/01.Introduction/01/01.PhiFamily.md)
  - [Aplinkos paruošimas](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Pagrindinių technologijų supratimas](./md/01.Introduction/01/01.Understandingtech.md)
  - [Dirbtinio intelekto saugumas Phi modeliams](./md/01.Introduction/01/01.AISafety.md)
  - [Phi techninės įrangos palaikymas](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi modeliai ir jų prieinamumas įvairiose platformose](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Naudojant Guidance-ai ir Phi](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace Modeliai](https://github.com/marketplace/models)
  - [Azure AI Modelių Katalogas](https://ai.azure.com)

- Phi įžvalgos skirtingose aplinkose
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [GitHub Modeliai](./md/01.Introduction/02/02.GitHubModel.md)
    - [Azure AI Foundry Modelių Katalogas](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi šeimos įžvalgos
    - [Phi įžvalgos iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Phi įžvalgos Android](./md/01.Introduction/03/Android_Inference.md)
    - [Phi įžvalgos Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Phi įžvalgos AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Phi įžvalgos su Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Phi įžvalgos vietiniame serveryje](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Phi įžvalgos nuotoliniame serveryje naudojant AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Phi įžvalgos su Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Phi--Vision įžvalgos vietoje](./md/01.Introduction/03/Vision_Inference.md)
    - [Phi įžvalgos su Kaito AKS, Azure Containers (oficialus palaikymas)](./md/01.Introduction/03/Kaito_Inference.md)

- [Phi šeimos kvantifikavimas](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantifikavimas naudojant llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantifikavimas naudojant generatyvaus AI plėtinius onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantifikavimas naudojant Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantifikavimas naudojant Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi vertinimas
    - [Atsakingas AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry vertinimui](./md/01.Introduction/05/AIFoundry.md)
    - [Naudojant Promptflow vertinimui](./md/01.Introduction/05/Promptflow.md)

- RAG su Azure AI Paieška
    - [Kaip naudoti Phi-4-mini ir Phi-4-multimodal (RAG) su Azure AI Paieška](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi programų kūrimo pavyzdžiai
  - Teksto ir pokalbių programos
    - Phi-4 Pavyzdžiai 🆕
      - [📓] [Pokalbis su Phi-4-mini ONNX modeliu](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Pokalbis su Phi-4 vietiniu ONNX modeliu .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Pokalbis .NET konsolės programoje su Phi-4 ONNX naudojant Semantinį Kernelį](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 Pavyzdžiai
      - [Vietinis pokalbių robotas naršyklėje naudojant Phi3, ONNX Runtime Web ir WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Pokalbis](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Daugiamodelinis - Interaktyvus Phi-3-mini ir OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Apvalkalo kūrimas ir Phi-3 naudojimas su MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Modelio optimizavimas - Kaip optimizuoti Phi-3-min modelį ONNX Runtime Web su Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 programa su Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3 Daugiamodelinė AI Pagrįsta Užrašų Programos Pavyzdys](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Tobulinkite ir integruokite pritaikytus Phi-3 modelius su Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Tobulinkite ir integruokite pritaikytus Phi-3 modelius su Prompt flow Azure AI Foundry aplinkoje](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Įvertinkite pritaikytą Phi-3 / Phi-3.5 modelį Azure AI Foundry, laikantis Microsoft atsakingo AI principų](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct kalbos prognozavimo pavyzdys (kinų/anglų)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG pokalbių robotas](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Naudojant Windows GPU sukurti Prompt flow sprendimą su Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Naudojant Microsoft Phi-3.5 tflite sukurti Android programėlę](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Q&A .NET pavyzdys naudojant vietinį ONNX Phi-3 modelį su Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Konsolės pokalbių .NET programėlė su Semantic Kernel ir Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK kodo pavyzdžiai 
  - Phi-4 pavyzdžiai 🆕
    - [📓] [Generuoti projekto kodą naudojant Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5 pavyzdžiai
    - [Sukurkite savo Visual Studio Code GitHub Copilot pokalbių robotą su Microsoft Phi-3 šeima](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [Sukurkite savo Visual Studio Code pokalbių agentą su Phi-3.5 naudojant GitHub modelius](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- Pažangūs samprotavimo pavyzdžiai
  - Phi-4 pavyzdžiai 🆕
    - [📓] [Phi-4-mini-reasoning arba Phi-4-reasoning pavyzdžiai](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Phi-4-mini-reasoning tobulinimas su Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning tobulinimas su Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning su GitHub modeliais](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Phi-4-mini-reasoning su Azure AI Foundry modeliais](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- Demonstracijos
    - [Phi-4-mini demonstracijos, talpinamos Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Phi-4-multimodal demonstracijos, talpinamos Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- Vaizdo pavyzdžiai
  - Phi-4 pavyzdžiai 🆕
    - [📓] [Naudoti Phi-4-multimodal skaityti vaizdus ir generuoti kodą](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Phi-3 / 3.5 pavyzdžiai
    - [📓][Phi-3-vision-Image tekstas į tekstą](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP įterpimas](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [DEMO: Phi-3 perdirbimas](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Vizualinis kalbos asistentas - su Phi3-Vision ir OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision kelių kadrų arba kelių vaizdų pavyzdys](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Phi-3 Vision vietinis ONNX modelis naudojant Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Meniu pagrįstas Phi-3 Vision vietinis ONNX modelis naudojant Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

- Matematikos pavyzdžiai
  - Phi-4-Mini-Flash-Reasoning-Instruct pavyzdžiai 🆕 [Matematikos demonstracija su Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)

- Garso pavyzdžiai
  - Phi-4 pavyzdžiai 🆕
    - [📓] [Garso transkripcijų išgavimas naudojant Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodal garso pavyzdys](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal kalbos vertimo pavyzdys](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET konsolės programėlė naudojant Phi-4-multimodal garso analizę ir transkripcijos generavimą](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOE pavyzdžiai
  - Phi-3 / 3.5 pavyzdžiai
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) socialinių tinklų pavyzdys](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [RAG pipeline kūrimas su NVIDIA NIM Phi-3 MOE, Azure AI Search ir LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- Funkcijų kvietimo pavyzdžiai
  - Phi-4 pavyzdžiai 🆕
    - [📓] [Funkcijų kvietimas naudojant Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Funkcijų kvietimas kuriant kelių agentų sprendimus su Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Funkcijų kvietimas su Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [Funkcijų kvietimas su ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- Multimodalinio maišymo pavyzdžiai
  - Phi-4 pavyzdžiai 🆕
    - [📓] [Phi-4-multimodal naudojimas kaip technologijų žurnalistas](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET konsolės programėlė naudojant Phi-4-multimodal vaizdų analizei](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi tobulinimo pavyzdžiai
  - [Tobulinimo scenarijai](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Tobulinimas vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Tobulinimas: leiskite Phi-3 tapti pramonės ekspertu](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Phi-3 tobulinimas su AI Toolkit for VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Phi-3 tobulinimas su Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Phi-3 tobulinimas su Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Phi-3 tobulinimas su QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Phi-3 tobulinimas su Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Phi-3 tobulinimas su Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Tobulinimas su Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Tobulinimas su Microsoft Olive praktiniu užsiėmimu](./md/03.FineTuning/olive-lab/readme.md)
  - [Phi-3-vision tobulinimas su Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Phi-3 tobulinimas su Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision tobulinimas (oficiali parama)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Phi-3 tobulinimas su Kaito AKS, Azure Containers (oficiali parama)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 ir 3.5 Vision tobulinimas](https://github.com/2U1/Phi3-Vision-Finetune)

- Praktiniai užsiėmimai
  - [Pažangių modelių tyrinėjimas: LLM, SLM, vietinis vystymas ir daugiau](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP potencialo atskleidimas: tobulinimas su Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Akademiniai tyrimai ir publikacijos
  - [Textbooks Are All You Need II: phi-1.5 techninė ataskaita](https://arxiv.org/abs/2309.05463)
  - [Phi-3 techninė ataskaita: labai pajėgus kalbos modelis jūsų telefone](https://arxiv.org/abs/2404.14219)
  - [Phi-4 techninė ataskaita](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini techninė ataskaita: kompaktiški, bet galingi multimodaliniai kalbos modeliai per Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Mažų kalbos modelių optimizavimas transporto priemonėse funkcijų kvietimui](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Phi-3 tobulinimas daugiapakopiam klausimų atsakymui: metodologija, rezultatai ir iššūkiai](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning Techninė ataskaita](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning Techninė ataskaita](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)  

## Naudojimasis Phi modeliais  

### Phi Azure AI Foundry platformoje  

Galite sužinoti, kaip naudoti Microsoft Phi ir kurti E2E sprendimus įvairiuose techninės įrangos įrenginiuose. Norėdami patys išbandyti Phi, pradėkite nuo modelių testavimo ir Phi pritaikymo savo scenarijams naudodami [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Daugiau informacijos rasite skyriuje „Pradžia su [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)“.  

**Testavimo aplinka**  
Kiekvienas modelis turi dedikuotą testavimo aplinką [Azure AI Playground](https://aka.ms/try-phi3).  

### Phi GitHub modeliuose  

Galite sužinoti, kaip naudoti Microsoft Phi ir kurti E2E sprendimus įvairiuose techninės įrangos įrenginiuose. Norėdami patys išbandyti Phi, pradėkite nuo modelio testavimo ir Phi pritaikymo savo scenarijams naudodami [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Daugiau informacijos rasite skyriuje „Pradžia su [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)“.  

**Testavimo aplinka**  
Kiekvienas modelis turi dedikuotą [testavimo aplinką](/md/02.QuickStart/GitHubModel_QuickStart.md).  

### Phi Hugging Face platformoje  

Modelį taip pat galite rasti [Hugging Face](https://huggingface.co/microsoft).  

**Testavimo aplinka**  
[Hugging Chat testavimo aplinka](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct).  

## Atsakingas AI  

Microsoft siekia padėti savo klientams atsakingai naudoti mūsų AI produktus, dalintis savo patirtimi ir kurti pasitikėjimu grįstus partnerystės ryšius, pasitelkiant tokias priemones kaip skaidrumo pastabos ir poveikio vertinimai. Daugelį šių išteklių galite rasti adresu [https://aka.ms/RAI](https://aka.ms/RAI).  
Microsoft požiūris į atsakingą AI grindžiamas mūsų AI principais: sąžiningumu, patikimumu ir saugumu, privatumu ir apsauga, įtrauktimi, skaidrumu ir atskaitomybe.  

Didelio masto natūralios kalbos, vaizdų ir kalbos modeliai – kaip tie, kurie naudojami šiame pavyzdyje – gali elgtis nesąžiningai, nepatikimai ar įžeidžiamai, taip sukeldami žalą. Prašome peržiūrėti [Azure OpenAI paslaugos Skaidrumo pastabą](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), kad būtumėte informuoti apie rizikas ir apribojimus.  

Rekomenduojamas būdas šių rizikų mažinimui yra įtraukti saugumo sistemą į savo architektūrą, kuri galėtų aptikti ir užkirsti kelią žalingam elgesiui. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) suteikia nepriklausomą apsaugos sluoksnį, galintį aptikti žalingą vartotojų sukurtą ir AI sukurtą turinį programose ir paslaugose. Azure AI Content Safety apima teksto ir vaizdų API, leidžiančius aptikti žalingą medžiagą. Azure AI Foundry platformoje Content Safety paslauga leidžia peržiūrėti, tyrinėti ir išbandyti pavyzdinį kodą, skirtą žalingo turinio aptikimui įvairiose modalumose. Ši [greito starto dokumentacija](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) padės jums atlikti užklausas paslaugai.  

Kitas aspektas, kurį reikia apsvarstyti, yra bendras programos našumas. Naudojant multimodalines ir daugiamodelines programas, našumas reiškia, kad sistema veikia taip, kaip tikitės jūs ir jūsų vartotojai, įskaitant žalingų rezultatų negeneravimą. Svarbu įvertinti bendrą programos našumą naudojant [Našumo ir kokybės bei Rizikos ir saugumo vertinimo priemones](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Taip pat galite sukurti ir vertinti naudodami [individualius vertinimo įrankius](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).  

Savo AI programą galite įvertinti kūrimo aplinkoje naudodami [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Turėdami testavimo duomenų rinkinį arba tikslą, jūsų generatyvios AI programos generacijos yra kiekybiškai matuojamos naudojant įmontuotus arba jūsų pasirinktus individualius vertinimo įrankius. Norėdami pradėti naudotis Azure AI Evaluation SDK savo sistemos vertinimui, galite sekti [greito starto vadovą](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kai atliksite vertinimo procesą, galite [vizualizuoti rezultatus Azure AI Foundry platformoje](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).  

## Prekių ženklai  

Šis projektas gali turėti prekių ženklų ar logotipų, susijusių su projektais, produktais ar paslaugomis. Leidžiamas Microsoft prekių ženklų ar logotipų naudojimas turi atitikti ir laikytis [Microsoft Prekių ženklų ir prekės ženklo gairių](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Microsoft prekių ženklų ar logotipų naudojimas modifikuotose šio projekto versijose neturi sukelti painiavos ar sudaryti įspūdžio, kad Microsoft remia projektą. Bet koks trečiųjų šalių prekių ženklų ar logotipų naudojimas turi atitikti tų trečiųjų šalių politiką.  

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.