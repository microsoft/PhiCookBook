# Phi Receptų Knyga: Praktiniai Pavyzdžiai su Microsoft Phi Modeliais

[![Atidarykite ir naudokite pavyzdžius GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Atidaryti Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub bendradarbiai](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub problemos](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Sveiki](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub stebėtojai](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub šakės](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub žvaigždutės](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi yra atvirų šaltinių DI modelių serija, sukurta Microsoft. 

Phi šiuo metu yra galingiausias ir ekonomiškiausias mažų kalbos modelių (SLM) variantas, turintis labai gerus rodiklius daugiakalbystėje, samprotavime, teksto/pokalbio generavime, programavime, vaizduose, garse ir kituose scenarijuose. 

Galite diegti Phi į debesį arba krašto įrenginius, ir galite lengvai kurti generuojančias DI programas su ribota skaičiavimo galia.

Laikykitės šių žingsnių, kad pradėtumėte naudoti šiuos išteklius:
1. **Atšakykite Repozitoriją**: Spauskite [![GitHub šakės](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Klonuokite Repozitoriją**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Prisijunkite prie Microsoft AI Discord bendruomenės ir susipažinkite su ekspertais bei kitais kūrėjais**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/lt/cover.eb18d1b9605d754b.webp)

### 🌐 Daugiakalbystės palaikymas

#### Palaikoma per GitHub Action (Automatizuota ir Visada Naujausia)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabų](../ar/README.md) | [Bengalų](../bn/README.md) | [Bulgarų](../bg/README.md) | [Birmos (Mianmaro)](../my/README.md) | [Kinų (supaprastinta)](../zh-CN/README.md) | [Kinų (tradicinė, Honkongas)](../zh-HK/README.md) | [Kinų (tradicinė, Makao)](../zh-MO/README.md) | [Kinų (tradicinė, Taivanas)](../zh-TW/README.md) | [Kroatų](../hr/README.md) | [Čekų](../cs/README.md) | [Danų](../da/README.md) | [Olandų](../nl/README.md) | [Estų](../et/README.md) | [Suomių](../fi/README.md) | [Prancūzų](../fr/README.md) | [Vokiečių](../de/README.md) | [Graikų](../el/README.md) | [Hebrajų](../he/README.md) | [Hindi](../hi/README.md) | [Vengrų](../hu/README.md) | [Indoneziečių](../id/README.md) | [Italų](../it/README.md) | [Japonų](../ja/README.md) | [Kannados](../kn/README.md) | [Korėjiečių](../ko/README.md) | [Lietuvių](./README.md) | [Malajų](../ms/README.md) | [Malajalamo](../ml/README.md) | [Maratų](../mr/README.md) | [Nepaliečių](../ne/README.md) | [Nigerijos pīdzinas](../pcm/README.md) | [Norvegų](../no/README.md) | [Persų (Farsi)](../fa/README.md) | [Lenkų](../pl/README.md) | [Portugalų (Brazilija)](../pt-BR/README.md) | [Portugalų (Portugalija)](../pt-PT/README.md) | [Pandžabių (Gurmukhi)](../pa/README.md) | [Rumunų](../ro/README.md) | [Rusų](../ru/README.md) | [Serbų (kirilica)](../sr/README.md) | [Slovakų](../sk/README.md) | [Slovėnų](../sl/README.md) | [Ispanų](../es/README.md) | [Svahelių](../sw/README.md) | [Švedų](../sv/README.md) | [Tagalogų (Filipinų)](../tl/README.md) | [Tamilų](../ta/README.md) | [Telugų](../te/README.md) | [Tajų](../th/README.md) | [Turkų](../tr/README.md) | [Ukrainiečių](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamiečių](../vi/README.md)

> **Norite klonuoti vietoje?**

> Ši repozitorija apima daugiau nei 50 kalbų vertimų, todėl ženkliai padidėja atsisiuntimo dydis. Norėdami klonuoti be vertimų, naudokite sparsų nuskaitymą (sparse checkout):
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Tai suteikia viską, ko reikia kursui užbaigti, daug greičiau atsisiunčiant.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Turinys

- Įvadas
  - [Sveiki atvykę į Phi šeimą](./md/01.Introduction/01/01.PhiFamily.md)
  - [Aplinkos nustatymas](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Pagrindinių technologijų supratimas](./md/01.Introduction/01/01.Understandingtech.md)
  - [DI saugumas Phi modeliams](./md/01.Introduction/01/01.AISafety.md)
  - [Phi aparatūros palaikymas](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi modeliai ir prieinamumas platformose](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai ir Phi naudojimas](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace modeliai](https://github.com/marketplace/models)
  - [Azure AI modelių katalogas](https://ai.azure.com)

- Phi apdorojimas skirtingose aplinkose
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub modeliai](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry modelių katalogas](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry vietinis](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi šeimos apdorojimas
    - [Phi apdorojimas iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Phi apdorojimas Android](./md/01.Introduction/03/Android_Inference.md)
    - [Phi apdorojimas Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Phi apdorojimas AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Phi apdorojimas su Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Phi apdorojimas vietiniame serveryje](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Phi apdorojimas nuotoliniame serveryje naudojant AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Phi apdorojimas su Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Phi – vizijos apdorojimas vietoje](./md/01.Introduction/03/Vision_Inference.md)
    - [Phi apdorojimas su Kaito AKS, Azure konteineriais (oficialus palaikymas)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi šeimos kvantavimas](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantavimas naudojant llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantavimas naudojant Generatyvios DI plėtinius onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantavimas naudojant Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantavimas su Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi vertinimas
    - [Atsakingas DI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry vertinimui](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow naudojimas vertinimui](./md/01.Introduction/05/Promptflow.md)
 
- RAG su Azure AI Search
    - [Kaip naudoti Phi-4-mini ir Phi-4-multimodal (RAG) su Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi programėlių kūrimo pavyzdžiai
  - Teksto ir pokalbių programos
    - Phi-4 pavyzdžiai 🆕
      - [📓] [Pokalbis su Phi-4-mini ONNX modeliu](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Pokalbis su Phi-4 vietiniu ONNX modeliu .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Pokalbių .NET konsolės programa su Phi-4 ONNX naudojant Sementic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 pavyzdžiai
      - [Vietinis pokalbių robotas naršyklėje naudojant Phi3, ONNX Runtime Web ir WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino pokalbis](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - Interaktyvus Phi-3-mini ir OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Korpuso kūrimas ir Phi-3 naudojimas su MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Modelio optimizavimas - Kaip optimizuoti Phi-3-min modelį ONNX Runtime Web su Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 programa su Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 daugiamodelių DI palaikoma užrašų programėlės pavyzdys](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Tinkinkite ir integruokite pasirinktinius Phi-3 modelius su Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Tinkinkite ir integruokite pasirinktinius Phi-3 modelius su Prompt flow Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Įvertinkite pritaikytą Phi-3 / Phi-3.5 modelį Azure AI Foundry, atkreipdami dėmesį į Microsoft atsakingos DI principus](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct kalbos prognozės pavyzdys (Kinų/Anglų)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG pokalbių robotas](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Naudojant Windows GPU sukurti Prompt flow sprendimą su Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Naudojant Microsoft Phi-3.5 tflite sukurti Android programėlę](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Klausimai ir atsakymai .NET pavyzdys, naudojant vietinį ONNX Phi-3 modelį su Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Konsolinė .NET pokalbių programa su Semantic Kernel ir Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK kodo pavyzdžiai 
    - Phi-4 pavyzdžiai 🆕
      - [📓] [Sugeneruoti projekto kodą naudojant Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 pavyzdžiai
      - [Sukurkite savo Visual Studio Code GitHub Copilot pokalbių programėlę su Microsoft Phi-3 šeima](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Sukurkite savo Visual Studio Code pokalbių Copilot agentą su Phi-3.5 pagal GitHub modelius](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Pažangių samprotavimų pavyzdžiai
    - Phi-4 pavyzdžiai 🆕
      - [📓] [Phi-4-mini-samprotavimų arba Phi-4-samprotavimų pavyzdžiai](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Phi-4-mini-samprotavimų perdėliojimas naudojant Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-samprotavimų perdėliojimas naudojant Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-samprotavimų su GitHub modeliais](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-samprotavimų su Azure AI Foundry modeliais](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demonstracijos
      - [Phi-4-mini demonstracijos talpinamos Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demonstracijos talpinamos Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Vizijos pavyzdžiai
    - Phi-4 pavyzdžiai 🆕
      - [📓] [Naudokite Phi-4-multimodal paveikslėlių skaitymui ir kodo generavimui](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 pavyzdžiai
      -  [📓][Phi-3-vizijos paveikslėlio tekstas į tekstą](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vizija ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vizijos CLIP įterpimas](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 perdirbimas](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vizija - Vaizdinės kalbos asistentas - su Phi3-Vizija ir OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 vizija Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 vizija OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vizijos daugiaekranis arba daugiapaveikslis pavyzdys](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vizija vietinis ONNX modelis naudojant Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Meniu pagrindu Phi-3 Vizija vietinis ONNX modelis naudojant Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Matematikos pavyzdžiai
    -  Phi-4-Mini-Flash-Samprotavimų-Instrukcijų pavyzdžiai 🆕 [Matematikos demonstracija su Phi-4-Mini-Flash-Samprotavimų-Instrukcijų modeliu](./md/02.Application/09.Math/MathDemo.ipynb)

  - Garso pavyzdžiai
    - Phi-4 pavyzdžiai 🆕
      - [📓] [Garso transkripcijos išgavimas naudojant Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal garso pavyzdys](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal kalbos vertimo pavyzdys](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET konsolinė programa naudojant Phi-4-multimodal garso analizę ir transkripcijos generavimą](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE pavyzdžiai
    - Phi-3 / 3.5 pavyzdžiai
      - [📓] [Phi-3.5 Ekspertų mišinių modelių (MoEs) socialinės medijos pavyzdys](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Atrankomis pagrįstos generacijos (RAG) pipeline kūrimas su NVIDIA NIM Phi-3 MOE, Azure AI Search ir LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Funkcijų kvietimų pavyzdžiai
    - Phi-4 pavyzdžiai 🆕
      -  [📓] [Funkcijų kvietimų naudojimas su Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Funkcijų kvietimų naudojimas kuriant daugiaagentus su Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Funkcijų kvietimų naudojimas su Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Funkcijų kvietimų naudojimas su ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Daugiamodelių maišymo pavyzdžiai
    - Phi-4 pavyzdžiai 🆕
      -  [📓] [Phi-4-multimodal naudojimas kaip technologijų žurnalistas](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET konsolinė programa naudojant Phi-4-multimodal paveikslėlių analizei](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi modelių pritaikymas
  - [Priderinimo scenarijai](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Priderinimas vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Leiskite Phi-3 tapti pramonės ekspertu](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Phi-3 priderinimas naudojant AI Toolkit for VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Phi-3 priderinimas naudojant Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Phi-3 priderinimas su Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Phi-3 priderinimas su QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Phi-3 priderinimas su Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Phi-3 priderinimas su Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Priderinimas su Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Priderinimas su Microsoft Olive praktinis laboratorinis darbas](./md/03.FineTuning/olive-lab/readme.md)
  - [Phi-3-vizijos priderinimas su Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Phi-3 priderinimas su Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vizijos priderinimas (oficialus palaikymas)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Phi-3 priderinimas su Kaito AKS, Azure konteineriai (oficialus palaikymas)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 ir 3.5 Vizijos priderinimas](https://github.com/2U1/Phi3-Vision-Finetune)

- Praktinis laboratorinis darbas
  - [Naujausių modelių tyrinėjimas: LLM, SLM, vietinė plėtra ir dar daugiau](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP potencialo atrakinimas: Priderinimas su Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Akademiniai tyrimai ir publikacijos
  - [Vadovėliai yra viskas, ko reikia II: phi-1.5 techninė ataskaita](https://arxiv.org/abs/2309.05463)
  - [Phi-3 techninė ataskaita: labai pajėgus kalbos modelis vietoje jūsų telefone](https://arxiv.org/abs/2404.14219)
  - [Phi-4 techninė ataskaita](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini techninė ataskaita: kompaktiški, tačiau galingi multimodalūs kalbos modeliai per LoRA mišinius](https://arxiv.org/abs/2503.01743)
  - [Mažų kalbos modelių optimizavimas funkcijų skambučiams automobilyje](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 smulkus derinimas daugelio pasirenkamųjų klausimų atsakymui: metodologija, rezultatai ir iššūkiai](https://arxiv.org/abs/2501.01588)
  - [Phi-4 sprendimų techninė ataskaita](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini sprendimų techninė ataskaita](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi modelių naudojimas

### Phi Azure AI Foundry platformoje

Jūs galite sužinoti, kaip naudoti Microsoft Phi ir kaip kurti galutinius sprendimus skirtinguose savo įrenginiuose. Norėdami patirti Phi patys, pradėkite žaisti su modeliais ir pritaikyti Phi savo scenarijams naudodami [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Daugiau sužinosite pradėję nuo [Azure AI Foundry įžangos](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Žaidimų aikštelė**  
Kiekvienas modelis turi skirta žaidimų aikštelę modeliui išbandyti [Azure AI Playground](https://aka.ms/try-phi3).

### Phi GitHub modeliuose

Jūs galite sužinoti, kaip naudoti Microsoft Phi ir kaip kurti galutinius sprendimus skirtinguose savo įrenginiuose. Norėdami patirti Phi patys, pradėkite žaisti su modeliu ir pritaikyti Phi savo scenarijams naudodami [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Daugiau sužinosite pradėję nuo [GitHub Model Catalog įžangos](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Žaidimų aikštelė**  
Kiekvienas modelis turi skirtą [žaidimų aikštelę modeliui išbandyti](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi Hugging Face platformoje

Modelį taip pat galite rasti [Hugging Face](https://huggingface.co/microsoft).

**Žaidimų aikštelė**  
[Hugging Chat žaidimų aikštelė](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 Kiti kursai

Mūsų komanda kuria ir kitus kursus! Patikrinkite:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j pradedantiesiems](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js pradedantiesiems](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agentai
[![AZD pradedantiesiems](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI pradedantiesiems](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP pradedantiesiems](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI agentai pradedantiesiems](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Generatyvioji AI serija
[![Generatyvioji AI pradedantiesiems](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatyvioji AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatyvioji AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatyvioji AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### Pagrindinis mokymasis
[![ML pradedantiesiems](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Duomenų mokslas pradedantiesiems](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![DI pradedantiesiems](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kibernetinis saugumas pradedantiesiems](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Tinklalapių kūrimas pradedantiesiems](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![Daiktų internetas pradedantiesiems](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR kūrimas pradedantiesiems](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Copilot serija
[![Copilot DI porinėje programavime](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot nuotykiai](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Atsakingas DI

Microsoft siekia padėti mūsų klientams naudoti mūsų DI produktus atsakingai, dalinantis mūsų patirtimi ir kuriant pasitikėjimu grįstas partnerystes su tokiais įrankiais kaip Skaidrumo užrašai ir poveikio vertinimai. Daugelį šių išteklių galite rasti adresu [https://aka.ms/RAI](https://aka.ms/RAI).  
Microsoft atsakingo DI požiūris grindžiamas mūsų DI principais: sąžiningumu, patikimumu ir saugumu, privatumu ir saugumu, įtrauktimi, skaidrumu ir atsakomybe.

Didelio masto natūralios kalbos, vaizdų ir balso modeliai – kaip ir šio pavyzdžio – gali elgtis neteisingai, nepatikimai arba įžeidžiančiai, taip sukeldami žalos. Prašome konsultuotis su [Azure OpenAI paslaugos Skaidrumo užrašu](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), kad būtumėte informuoti apie rizikas ir apribojimus.

Rekomenduojamas požiūris rizikoms sumažinti yra įtraukti saugumo sistemą į savo architektūrą, kuri gali aptikti ir užkirsti kelią žalingam elgesiui. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) suteikia nepriklausomą apsaugos sluoksnį, galintį aptikti žalingą vartotojų ir DI generuotą turinį programėlėse bei paslaugose. Azure AI Content Safety apima teksto ir vaizdų API, leidžiančias aptikti žalingą medžiagą. Azure AI Foundry Content Safety paslauga leidžia peržiūrėti, tyrinėti ir išbandyti pavyzdinį kodą žalingam turiniui aptikti įvairiose modalumose. Tolimesnė [greitojo pradžios dokumentacija](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) jums padės atlikti užklausas paslaugai.

Kita svarbi dalis – bendra programėlės našumo vertinimas. Su daugiapmodalėmis ir daugiamodelių programėlėmis, našumas reiškia, kad sistema veikia lygiai taip, kaip jūs ir jūsų naudotojai tikitės, įskaitant ir neženklinant žalingų išvesties rezultatų. Svarbu įvertinti jūsų bendrą programėlės veikimą naudojant [Našumo, kokybės, rizikos ir saugumo vertintojus](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Taip pat galite kurti ir vertinti naudodami [individualius vertintojus](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).
Jūs galite įvertinti savo DI programą savo kūrimo aplinkoje naudodami [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Turint testinį duomenų rinkinį arba tikslą, jūsų generatyvinės DI programos generavimai yra kiekybiškai matuojami su įmontuotais vertintojais arba jūsų pasirinktais pasirinktiniais vertintojais. Norėdami pradėti naudotis azure ai evaluation sdk ir įvertinti savo sistemą, galite sekti [greitojo starto gidą](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Įvykdžius vertinimo paleidimą, galite [vizualizuoti rezultatus Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Prekių ženklai

Šis projektas gali turėti prekių ženklus arba logotipus, skirtus projektams, produktams ar paslaugoms. Leidžiama naudoti Microsoft prekių ženklus ar logotipus pagal [Microsoft prekių ženklų ir prekės ženklo gaires](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Microsoft prekių ženklų ar logotipų naudojimas modifikuotose šio projekto versijose negali klaidinti arba sieti su Microsoft rėmimu. Bet koks trečiųjų šalių prekių ženklų ar logotipų naudojimas yra reglamentuojamas tų trečiųjų šalių taisyklių.

## Pagalbos gavimas

Jei įstringate arba turite klausimų apie DI programų kūrimą, prisijunkite prie:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Jei turite produkto atsiliepimų arba klaidų kūrimo metu, apsilankykite:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas pagrindiniu ir autoritetingu šaltiniu. Svarbiai informacijai rekomenduojamas profesionalus žmogiškasis vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->