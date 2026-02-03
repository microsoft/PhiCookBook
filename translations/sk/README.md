# Phi Cookbook: Praktické príklady s Microsoft Phi modelmi

[![Otvorte a používajte príklady v GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Otvorte v Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Otvoriť&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Prispievatelia GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Problémy GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Žiadosti o stiahnutie (pull-requests)](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Vitáme](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Sledujúci na GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Sledujte)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Rozvetvenia GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Hviezdičky GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Hviezdička)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi je séria open source AI modelov vyvinutých spoločnosťou Microsoft.

Phi je momentálne najsilnejší a nákladovo najefektívnejší malý jazykový model (SLM) s veľmi dobrými benchmarkami v multi-jazyku, uvažovaní, generovaní textu/rozhovorov, programovania, obrázkov, audia a ďalších scenároch.

Môžete nasadiť Phi do cloudu alebo na hraničné zariadenia a ľahko vytvoriť generatívne AI aplikácie s obmedzenou výpočtovou kapacitou.

Postupujte podľa týchto krokov, aby ste začali používať tieto zdroje:
1. **Vytvorte fork repozitára**: Kliknite [![Rozvetvenia GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Skopírujte repozitár**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Pridajte sa do komunity Microsoft AI Discord a stretnite sa s expertmi a ďalšími vývojármi**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/sk/cover.eb18d1b9605d754b.webp)

### 🌐 Podpora viacerých jazykov

#### Podporované cez GitHub Action (automatizované a vždy aktuálne)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabčina](../ar/README.md) | [Bengálčina](../bn/README.md) | [Bulharčina](../bg/README.md) | [Barmčina (Myanmar)](../my/README.md) | [Čínština (zjednodušená)](../zh-CN/README.md) | [Čínština (tradičná, Hongkong)](../zh-HK/README.md) | [Čínština (tradičná, Macau)](../zh-MO/README.md) | [Čínština (tradičná, Taiwan)](../zh-TW/README.md) | [Chorvátčina](../hr/README.md) | [Čeština](../cs/README.md) | [Dánčina](../da/README.md) | [Holandčina](../nl/README.md) | [Estónčina](../et/README.md) | [Fínčina](../fi/README.md) | [Francúzština](../fr/README.md) | [Nemčina](../de/README.md) | [Gréčtina](../el/README.md) | [Hebrejčina](../he/README.md) | [Hindčina](../hi/README.md) | [Maďarčina](../hu/README.md) | [Indonézčina](../id/README.md) | [Taliančina](../it/README.md) | [Japončina](../ja/README.md) | [Kannadčina](../kn/README.md) | [Kórejčina](../ko/README.md) | [Litovčina](../lt/README.md) | [Malayčina](../ms/README.md) | [Malayalam](../ml/README.md) | [Maráthčina](../mr/README.md) | [Nepálčina](../ne/README.md) | [Nigérijský pidžin](../pcm/README.md) | [Nórčina](../no/README.md) | [Perzština (fársí)](../fa/README.md) | [Poľština](../pl/README.md) | [Portugalčina (Brazília)](../pt-BR/README.md) | [Portugalčina (Portugalsko)](../pt-PT/README.md) | [Pandžábčina (Gurmukhi)](../pa/README.md) | [Rumunčina](../ro/README.md) | [Ruština](../ru/README.md) | [Srbčina (cyrilika)](../sr/README.md) | [Slovenčina](./README.md) | [Slovinčina](../sl/README.md) | [Španielčina](../es/README.md) | [Swahili](../sw/README.md) | [Švédčina](../sv/README.md) | [Tagalčina (Filipíny)](../tl/README.md) | [Tamilčina](../ta/README.md) | [Telugčina](../te/README.md) | [Thajčina](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinčina](../uk/README.md) | [Urdčina](../ur/README.md) | [Vietnamčina](../vi/README.md)

> **Radšej klonovať lokálne?**

> Tento repozitár obsahuje vyše 50 jazykových prekladov, čo výrazne zväčšuje veľkosť sťahovania. Ak chcete klonovať bez prekladov, použite sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Toto vám dá všetko potrebné na dokončenie kurzu s oveľa rýchlejším sťahovaním.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Obsah

- Úvod
  - [Vitajte v rodine Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Nastavenie prostredia](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Porozumenie kľúčovým technológiám](./md/01.Introduction/01/01.Understandingtech.md)
  - [Bezpečnosť AI pre Phi modely](./md/01.Introduction/01/01.AISafety.md)
  - [Podpora hardvéru Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi modely a dostupnosť naprieč platformami](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Používanie Guidance-ai a Phi](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace modely](https://github.com/marketplace/models)
  - [Azure AI katalóg modelov](https://ai.azure.com)

- Inferencia Phi v rôznom prostredí
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub modely](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry katalóg modelov](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Inferencia Phi Family
    - [Inferencia Phi v iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inferencia Phi v Android](./md/01.Introduction/03/Android_Inference.md)
    - [Inferencia Phi v Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inferencia Phi v AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inferencia Phi s Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Inferencia Phi na lokálnom serveri](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inferencia Phi na vzdialenom serveri pomocou AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inferencia Phi pomocou Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inferencia Phi--Vision lokálne](./md/01.Introduction/03/Vision_Inference.md)
    - [Inferencia Phi s Kaito AKS, Azure Containers (oficiálna podpora)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Kvantifikácia Phi Family](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Kvantifikácia Phi-3.5 / 4 pomocou llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Kvantifikácia Phi-3.5 / 4 pomocou rozšírení Generative AI pre onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Kvantifikácia Phi-3.5 / 4 pomocou Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Kvantifikácia Phi-3.5 / 4 pomocou Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Hodnotenie Phi
    - [Zodpovedné AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry pre hodnotenie](./md/01.Introduction/05/AIFoundry.md)
    - [Použitie Promptflow pre hodnotenie](./md/01.Introduction/05/Promptflow.md)
 
- RAG s Azure AI Search
    - [Ako používať Phi-4-mini a Phi-4-multimodal (RAG) s Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Vzorky vývoja Phi aplikácií
  - Textové a chatové aplikácie
    - Phi-4 Ukážky 🆕
      - [📓] [Chat s Phi-4-mini ONNX modelom](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat s Phi-4 lokálnym ONNX modelom .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Chat .NET konzolová aplikácia s Phi-4 ONNX pomocou Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 Ukážky
      - [Lokálny chatbot v prehliadači pomocou Phi3, ONNX Runtime Web a WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVINO Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi model - Interaktívny Phi-3-mini a OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Vytvorenie wrapperu a použitie Phi-3 s MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Optimalizácia modelu - Ako optimalizovať model Phi-3-min pre ONNX Runtime Web s Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 aplikácia s Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 Multi Model AI poháňaná aplikácia Poznámky - ukážka](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Doladenie a integrácia vlastných modelov Phi-3 s Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Doladenie a integrácia vlastných modelov Phi-3 s Prompt flow v Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Vyhodnotenie doladeného modelu Phi-3 / Phi-3.5 v Azure AI Foundry so zameraním na zásady zodpovednej AI spoločnosti Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Vzorka predikcie jazyka Phi-3.5-mini-instruct (čínska/anglická)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Použitie Windows GPU na vytvorenie riešenia Prompt flow s Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Použitie Microsoft Phi-3.5 tflite na vytvorenie Android aplikácie](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET príklad použitia lokálneho ONNX Phi-3 modelu s Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Konzolová chat .NET aplikácia so Semantic Kernel a Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Ukážky kódu založené na Azure AI Inference SDK
    - Ukážky Phi-4 🆕
      - [📓] [Generovanie kódu projektu pomocou Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Ukážky Phi-3 / 3.5
      - [Vytvorte si vlastný Visual Studio Code GitHub Copilot Chat s rodinou Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Vytvorte si vlastného agenta Visual Studio Code Chat Copilot s Phi-3.5 pomocou GitHub modelov](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Ukážky pokročilého uvažovania
    - Ukážky Phi-4 🆕
      - [📓] [Phi-4-mini-reasoning alebo Phi-4-reasoning ukážky](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Doladenie Phi-4-mini-reasoning pomocou Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Doladenie Phi-4-mini-reasoning pomocou Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning pomocou GitHub modelov](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-reasoning pomocou Azure AI Foundry modelov](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Ukážky
      - [Phi-4-mini ukážky hostované na Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal ukážky hostované na Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Ukážky vidieť
    - Ukážky Phi-4 🆕
      - [📓] [Použitie Phi-4-multimodal na čítanie obrázkov a generovanie kódu](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Ukážky Phi-3 / 3.5
      -  [📓][Phi-3-vision-Prepis textu k textu z obrázka](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Vizualny jazykový asistent - s Phi3-Vision a OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision viacrámcový alebo viacobrázkový príklad](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision lokálny ONNX model s použitím Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menu založený Phi-3 Vision lokálny ONNX model s použitím Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Ukážky matematiky
    -  Phi-4-Mini-Flash-Reasoning-Instruct ukážky 🆕 [Matematická ukážka s Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - Ukážky zvuku
    - Ukážky Phi-4 🆕
      - [📓] [Extrahovanie audio prepisov pomocou Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal zvuková ukážka](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal ukážka prekladu reči](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET konzolová aplikácia s použitím Phi-4-multimodal Audio na analýzu audio súboru a generovanie prepisu](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - Ukážky MOE
    - Ukážky Phi-3 / 3.5
      - [📓] [Phi-3.5 modely Mixture of Experts (MoEs) ukážka sociálnych médií](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Vytváranie Retrieval-Augmented Generation (RAG) pipeline s NVIDIA NIM Phi-3 MOE, Azure AI Search a LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Ukážky volania funkcií
    - Ukážky Phi-4 🆕
      -  [📓] [Použitie volania funkcií s Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Použitie volania funkcií na vytvorenie multi-agentov s Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Použitie volania funkcií s Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Použitie volania funkcií s ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Ukážky multimodálneho mixovania
    - Ukážky Phi-4 🆕
      -  [📓] [Použitie Phi-4-multimodal ako technologického novinára](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET konzolová aplikácia používajúca Phi-4-multimodal na analýzu obrázkov](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Doladenie Phi ukážok
  - [Scenáre doladenia](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Doladenie verzus RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Doladenie, nech sa Phi-3 stane odborníkom v odvetví](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Doladenie Phi-3 s AI Toolkit pre VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Doladenie Phi-3 s Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Doladenie Phi-3 pomocou Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Doladenie Phi-3 pomocou QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Doladenie Phi-3 s Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Doladenie Phi-3 s Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Doladenie pomocou Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Praktický lab doladenia pomocou Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)
  - [Doladenie Phi-3-vision pomocou Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Doladenie Phi-3 pomocou Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Doladenie Phi-3-vision (oficiálna podpora)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Doladenie Phi-3 s Kaito AKS, Azure kontajnery (oficiálna podpora)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Doladenie Phi-3 a 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Praktický lab
  - [Preskúmanie špičkových modelov: LLM, SLM, lokálny vývoj a viac](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Odblokovanie potenciálu NLP: doladenie s Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Akademické výskumné práce a publikácie
  - [Učebnice sú všetko, čo potrebujete II: technická správa phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Technická správa Phi-3: Vysoko schopný jazykový model lokálne na vašom telefóne](https://arxiv.org/abs/2404.14219)
  - [Technická správa Phi-4](https://arxiv.org/abs/2412.08905)
  - [Technická správa Phi-4-Mini: Kompaktné, no výkonné multimodálne jazykové modely cez zmes LoRA](https://arxiv.org/abs/2503.01743)
  - [Optimalizácia malých jazykových modelov pre volanie funkcií vo vozidle](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Doladenie PHI-3 pre odpovedanie na otázky s viacerými možnosťami: metodológia, výsledky a výzvy](https://arxiv.org/abs/2501.01588)
  - [Technická správa Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Technická správa Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Používanie modelov Phi

### Phi na Azure AI Foundry

Môžete sa naučiť, ako používať Microsoft Phi a ako vytvárať end-to-end riešenia vo vašich rôznych hardvérových zariadeniach. Ak chcete Phi sami vyskúšať, začnite hraním sa s modelmi a prispôsobovaním Phi pre svoje scenáre pomocou [Katalógu modelov Azure AI Foundry](https://aka.ms/phi3-azure-ai). Viac sa dozviete v návode Začíname s [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Playground**  
Každý model má vyhradený playground na testovanie modelu [Azure AI Playground](https://aka.ms/try-phi3).

### Phi na GitHub Modeloch

Môžete sa naučiť, ako používať Microsoft Phi a ako vytvárať end-to-end riešenia vo vašich rôznych hardvérových zariadeniach. Ak chcete Phi sami vyskúšať, začnite hraním sa s modelom a prispôsobovaním Phi pre svoje scenáre pomocou [Katalógu modelov GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Viac sa dozviete v návode Začíname s [Katalógom modelov GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**  
Každý model má vyhradený [playground na testovanie modelu](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi na Hugging Face

Model nájdete aj na [Hugging Face](https://huggingface.co/microsoft)

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 Ďalšie kurzy

Náš tím pripravuje aj ďalšie kurzy! Pozrite si:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j pre začiatočníkov](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js pre začiatočníkov](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain pre začiatočníkov](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agentov
[![AZD pre začiatočníkov](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI pre začiatočníkov](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP pre začiatočníkov](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agentov pre začiatočníkov](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Séria Generatívnej AI
[![Generatívna AI pre začiatočníkov](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatívna AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatívna AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatívna AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Základné vzdelávanie
[![ML pre začiatočníkov](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Dátová veda pre začiatočníkov](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI pre začiatočníkov](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kybernetická bezpečnosť pre začiatočníkov](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webový vývoj pre začiatočníkov](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT pre začiatočníkov](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![Vývoj XR pre začiatočníkov](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Séria Copilot
[![Copilot pre AI párované programovanie](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot pre C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Zodpovedná AI

Microsoft sa zaväzuje pomáhať našim zákazníkom zodpovedne využívať naše AI produkty, zdieľať naše skúsenosti a budovať vzťahy založené na dôvere prostredníctvom nástrojov ako Transparency Notes a Impact Assessments. Mnohé z týchto zdrojov nájdete na [https://aka.ms/RAI](https://aka.ms/RAI).  
Prístup Microsoftu k zodpovednej AI je založený na našich princípoch AI: spravodlivosť, spoľahlivosť a bezpečnosť, súkromie a bezpečnosť, inkluzívnosť, priehľadnosť a zodpovednosť.

Veľké modely prirodzeného jazyka, obrazov a reči - ako tie použité v tomto príklade - môžu potenciálne konať nespravodlivo, nespoľahlivo alebo urážlivo, čo môže viesť k poškodeniam. Prosím, konzultujte [Poznámku o transparentnosti služby Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), aby ste boli informovaní o rizikách a obmedzeniach.

Odporúčaný prístup k zmierneniu týchto rizík je začleniť do svojej architektúry bezpečnostný systém, ktorý dokáže rozpoznať a zabrániť škodlivému správaniu. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) poskytuje nezávislú ochrannú vrstvu, schopnú detegovať škodlivý obsah vytváraný používateľmi aj AI v aplikáciách a službách. Azure AI Content Safety zahŕňa API pre text a obrázky, ktoré umožňujú detegovať škodlivý materiál. V Azure AI Foundry služba Content Safety umožňuje prehliadať, skúmať a vyskúšať ukážkové kódy na detekciu škodlivého obsahu naprieč rôznymi modalitami. Nasledujúca [dokumentácia rýchleho štartu](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vás prevedie vytváraním požiadaviek na službu.
Ďalším aspektom, ktorý treba zohľadniť, je celkový výkon aplikácie. Pri viacmodálnych a viacmodelových aplikáciách považujeme výkon za to, že systém funguje tak, ako vy a vaši používatelia očakávate, vrátane nevytvárania škodlivých výstupov. Je dôležité zhodnotiť výkon vašej celkovej aplikácie pomocou [hodnotiacich nástrojov Výkon a Kvalita a Riziko a Bezpečnosť](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Tiež máte možnosť vytvárať a hodnotiť pomocou [vlastných hodnotiacich nástrojov](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Svoju AI aplikáciu môžete hodnotiť vo vašom vývojovom prostredí pomocou [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Na základe testovacej dátovej množiny alebo cieľa sa generácie vašej generatívnej AI aplikácie kvantitatívne merajú pomocou vstavaných alebo vlastných hodnotiacich nástrojov podľa vášho výberu. Aby ste mohli začať s Azure AI Evaluation SDK na hodnotenie vášho systému, môžete sledovať [rýchly návod](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po spustení hodnotiaceho behu môžete [vizualizovať výsledky v Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ochranné známky

Tento projekt môže obsahovať ochranné známky alebo logá projektov, produktov alebo služieb. Autorizované používanie ochranných známok alebo log Microsoftu je predmetom a musí sa riadiť [Pravidlami Microsoftu o ochranných známkach a značkách](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general). Použitie ochranných známok alebo log Microsoftu v upravených verziách tohto projektu nesmie spôsobovať zmätok ani naznačovať sponzorstvo Microsoftom. Akékoľvek použitie ochranných známok alebo log tretích strán podlieha pravidlám týchto tretích strán.

## Získanie pomoci

Ak sa zaseknete alebo máte akékoľvek otázky o vývoji AI aplikácií, pripojte sa:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Ak máte spätnú väzbu na produkt alebo chyby pri vývoji, navštívte:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->