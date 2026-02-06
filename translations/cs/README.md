# Phi Cookbook: Praktické příklady s modely Phi od Microsoftu

[![Otevřete a použijte ukázky v GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Otevřít v Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Přispěvatelé na GitHubu](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Problémy na GitHubu](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Pull requesty na GitHubu](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Vítány](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Sledující na GitHubu](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Forky na GitHubu](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Hvězdy na GitHubu](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi je řada open source AI modelů vyvinutých společností Microsoft.

Phi je v současné době nejsilnější a nejefektivnější malý jazykový model (SLM) s velmi dobrými výsledky v oblasti multijazyčného zpracování, uvažování, generování textu/chatů, kódování, obrázků, zvuku a dalších scénářů.

Phi můžete nasadit do cloudu nebo na edge zařízení a můžete snadno vytvářet generativní AI aplikace i s omezeným výpočetním výkonem.

Postupujte podle těchto kroků, jak začít používat tyto zdroje:
1. **Vytvořte Fork Repozitáře**: Klikněte na [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Naklonujte Repozitář**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Připojte se ke komunitě Microsoft AI Discord a setkejte se s experty a dalšími vývojáři**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cs/cover.eb18d1b9605d754b.webp)

### 🌐 Vícejazyčná podpora

#### Podporováno přes GitHub Actions (automaticky a vždy aktuální)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabština](../ar/README.md) | [Bengálština](../bn/README.md) | [Bulharština](../bg/README.md) | [Barmsky (Myanmar)](../my/README.md) | [Čínština (zjednodušená)](../zh-CN/README.md) | [Čínština (tradiční, Hong Kong)](../zh-HK/README.md) | [Čínština (tradiční, Macau)](../zh-MO/README.md) | [Čínština (tradiční, Taiwan)](../zh-TW/README.md) | [Chorvatština](../hr/README.md) | [Čeština](./README.md) | [Dánština](../da/README.md) | [Nizozemština](../nl/README.md) | [Estonština](../et/README.md) | [Finština](../fi/README.md) | [Francouzština](../fr/README.md) | [Němčina](../de/README.md) | [Řečtina](../el/README.md) | [Hebrejština](../he/README.md) | [Hindština](../hi/README.md) | [Maďarština](../hu/README.md) | [Indonéština](../id/README.md) | [Italština](../it/README.md) | [Japonština](../ja/README.md) | [Kannadština](../kn/README.md) | [Korejština](../ko/README.md) | [Litevština](../lt/README.md) | [Malajština](../ms/README.md) | [Malayalam](../ml/README.md) | [Maráthština](../mr/README.md) | [Nepálština](../ne/README.md) | [Nigérijská pidžin](../pcm/README.md) | [Norština](../no/README.md) | [Perština (Farsi)](../fa/README.md) | [Polština](../pl/README.md) | [Portugalština (Brazílie)](../pt-BR/README.md) | [Portugalština (Portugalsko)](../pt-PT/README.md) | [Paňdžábština (Gurmukhi)](../pa/README.md) | [Rumunština](../ro/README.md) | [Ruština](../ru/README.md) | [Srbština (cyrilice)](../sr/README.md) | [Slovenština](../sk/README.md) | [Slovinština](../sl/README.md) | [Španělština](../es/README.md) | [Svahilština](../sw/README.md) | [Švédština](../sv/README.md) | [Tagalog (Filipínsky)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thajština](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinština](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamština](../vi/README.md)

> **Preferujete klonování lokálně?**

> Tento repozitář obsahuje přes 50 jazykových překladů, což výrazně zvyšuje velikost stahování. Pro klonování bez překladů použijte sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> To vám poskytne vše potřebné pro dokončení kurzu s mnohem rychlejším stažením.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Obsah

- Úvod
  - [Vítejte v rodině Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Nastavení prostředí](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Porozumění klíčovým technologiím](./md/01.Introduction/01/01.Understandingtech.md)
  - [Bezpečnost AI pro modely Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Podpora hardwaru Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Modely Phi & dostupnost napříč platformami](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Používání Guidance-ai a Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Modely na GitHub Marketplace](https://github.com/marketplace/models)
  - [Katalog modelů Azure AI](https://ai.azure.com)

- Inferenční použití Phi v různých prostředích
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub modely](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry katalog modelů](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Inferenční použití Phi Family
    - [Inference Phi v iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inference Phi v Androidu](./md/01.Introduction/03/Android_Inference.md)
    - [Inference Phi v Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inference Phi v AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inference Phi s Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Inference Phi na lokálním serveru](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inference Phi na vzdáleném serveru pomocí AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inference Phi s jazykem Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inferenční použití Phi--Vision lokálně](./md/01.Introduction/03/Vision_Inference.md)
    - [Inference Phi s Kaito AKS, Azure kontejnery (oficiální podpora)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Kvantifikace Phi Family](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Kvantifikace Phi-3.5 / 4 pomocí llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Kvantifikace Phi-3.5 / 4 pomocí Generative AI extensions pro onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Kvantifikace Phi-3.5 / 4 pomocí Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Kvantifikace Phi-3.5 / 4 pomocí Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Hodnocení Phi
    - [Odpovědná AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry pro hodnocení](./md/01.Introduction/05/AIFoundry.md)
    - [Použití Promptflow pro hodnocení](./md/01.Introduction/05/Promptflow.md)
 
- RAG s Azure AI Search
    - [Jak používat Phi-4-mini a Phi-4-multimodal(RAG) s Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Ukázky vývoje aplikací Phi
  - Textové a chatovací aplikace
    - Ukázky Phi-4 🆕
      - [📓] [Chatování s modelem Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chatování s lokálním modelem Phi-4 ONNX v .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Chatovací konzolová aplikace .NET s Phi-4 ONNX pomocí Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Ukázky Phi-3 / 3.5
      - [Lokální chatbot v prohlížeči pomocí Phi3, ONNX Runtime Web a WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - Interaktivní Phi-3-mini a OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Vytvoření wrapperu a použití Phi-3 s MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Optimalizace modelu - Jak optimalizovat model Phi-3-min pro ONNX Runtime Web s Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 Aplikace s Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 Multi Model AI Powered Notes App Sample](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Doladění a integrace vlastních modelů Phi-3 s Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Doladění a integrace vlastních modelů Phi-3 s Prompt flow v Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Hodnocení doladěného modelu Phi-3 / Phi-3.5 v Azure AI Foundry se zaměřením na zásady odpovědné AI Microsoftu](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Vzorek předpovědi jazyka Phi-3.5-mini-instruct (čínština/angličtina)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Použití Windows GPU pro vytvoření řešení Prompt flow s Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Použití Microsoft Phi-3.5 tflite pro vytvoření Android aplikace](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET příklad používající lokální ONNX model Phi-3 s Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Konzolová chatovací .NET aplikace se Semantic Kernel a Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Ukázky kódu Azure AI Inference SDK 
    - Phi-4 Ukázky 🆕
      - [📓] [Generování kódu projektu pomocí Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 Ukázky
      - [Vytvořte si vlastní Visual Studio Code GitHub Copilot Chat s rodinou Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Vytvořte si vlastního Visual Studio Code Chat Copilot agenta s Phi-3.5 pomocí GitHub modelů](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Ukázky pokročilého uvažování
    - Phi-4 Ukázky 🆕
      - [📓] [Ukázky Phi-4-mini-reasoning nebo Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Doladění Phi-4-mini-reasoning s Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Doladění Phi-4-mini-reasoning s Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning s GitHub modely](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-reasoning s Azure AI Foundry modely](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demo
      - [Phi-4-mini demo hostované na Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demo hostované na Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Ukázky pro práci s vizí
    - Phi-4 Ukázky 🆕
      - [📓] [Použití Phi-4-multimodal k čtení obrázků a generování kódu](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 Ukázky
      -  [📓][Phi-3-vision-Text z obrázku do textu](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Recyklace](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Asistent vizuálního jazyka - s Phi3-Vision a OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision více snímků nebo vzorek více obrázků](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision Lokální ONNX model používající Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menu založené Phi-3 Vision Lokální ONNX model používající Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Ukázky matematiky
    -  Phi-4-Mini-Flash-Reasoning-Instruct Ukázky 🆕 [Matematické demo s Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - Ukázky zvuku
    - Phi-4 Ukázky 🆕
      - [📓] [Extrahování přepisů zvuku pomocí Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal Zvuková ukázka](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal Ukázka překladu řeči](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET konzolová aplikace používající Phi-4-multimodal Audio k analýze zvukového souboru a generování přepisu](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - Ukázky MoE
    - Phi-3 / 3.5 Ukázky
      - [📓] [Modely Phi-3.5 Mixture of Experts (MoEs) ukázka sociálních médií](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Vytvoření Retrieval-Augmented Generation (RAG) Pipeline s NVIDIA NIM Phi-3 MOE, Azure AI Search a LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Ukázky volání funkcí
    - Phi-4 Ukázky 🆕
      -  [📓] [Použití volání funkcí s Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Použití volání funkcí k vytvoření multi-agentů s Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Použití volání funkcí s Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Použití volání funkcí s ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Ukázky multimodálního míchání
    - Phi-4 Ukázky 🆕
      -  [📓] [Použití Phi-4-multimodal jako technologického novináře](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET konzolová aplikace používající Phi-4-multimodal k analýze obrázků](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Doladění Phi ukázek
  - [Scénáře doladění](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Doladění vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Doladění: Nechte Phi-3 stát se průmyslovým expertem](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Doladění Phi-3 s AI Toolkit pro VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Doladění Phi-3 s Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Doladění Phi-3 s Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Doladění Phi-3 s QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Doladění Phi-3 s Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Doladění Phi-3 s Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Doladění s Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Doladění s Microsoft Olive Praktický lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Doladění Phi-3-vision s Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Doladění Phi-3 s Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Doladění Phi-3-vision (oficiální podpora)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Doladění Phi-3 s Kaito AKS , Azure Containers (oficiální podpora)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Doladění Phi-3 a 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Praktický lab
  - [Objevování nejmodernějších modelů: LLMs, SLMs, lokální vývoj a další](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Odemknutí potenciálu NLP: Doladění s Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Akademické výzkumné práce a publikace
  - [Učebnice jsou vše, co potřebujete II: technická zpráva phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Technická zpráva Phi-3: Vysoce schopný jazykový model lokálně na vašem telefonu](https://arxiv.org/abs/2404.14219)
  - [Technická zpráva Phi-4](https://arxiv.org/abs/2412.08905)
  - [Technická zpráva Phi-4-Mini: Kompaktní, ale výkonné multimodální jazykové modely pomocí směsi LoRAs](https://arxiv.org/abs/2503.01743)
  - [Optimalizace malých jazykových modelů pro volání funkcí ve vozidle](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Doladění PHI-3 pro otázky s výběrem odpovědi: metodologie, výsledky a výzvy](https://arxiv.org/abs/2501.01588)
  - [Technická zpráva Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Technická zpráva Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Používání modelů Phi

### Phi na Azure AI Foundry

Můžete se naučit, jak používat Microsoft Phi a jak vytvářet end-to-end řešení na různých hardwarových zařízeních. Abyste si Phi sami vyzkoušeli, začněte hraním si s modely a přizpůsobením Phi pro vaše scénáře pomocí [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Více se dozvíte v průvodci Začínáme s [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Hřiště**
Každý model má vyhrazené hřiště pro testování modelu [Azure AI Playground](https://aka.ms/try-phi3).

### Phi na GitHub modelech

Můžete se naučit, jak používat Microsoft Phi a jak vytvářet end-to-end řešení na různých hardwarových zařízeních. Abyste si Phi sami vyzkoušeli, začněte hraním si s modelem a přizpůsobením Phi pro vaše scénáře pomocí [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Více se dozvíte v průvodci Začínáme s [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Hřiště**
Každý model má vyhrazené [hřiště pro testování modelu](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi na Hugging Face

Model můžete také najít na [Hugging Face](https://huggingface.co/microsoft).

**Hřiště**
 [Hugging Chat hřiště](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 Další kurzy

Náš tým připravuje i další kurzy! Podívejte se na:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j pro začátečníky](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js pro začátečníky](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain pro začátečníky](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agenti
[![AZD pro začátečníky](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI pro začátečníky](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP pro začátečníky](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents pro začátečníky](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Série generativní AI
[![Generativní AI pro začátečníky](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Základní vzdělávání
[![Strojové učení pro začátečníky](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science pro začátečníky](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI pro začátečníky](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kybernetická bezpečnost pro začátečníky](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webový vývoj pro začátečníky](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT pro začátečníky](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR vývoj pro začátečníky](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Série Copilot
[![Copilot pro AI párované programování](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot pro C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Odpovědná AI

Microsoft se zavazuje pomáhat svým zákazníkům používat naše AI produkty odpovědně, sdílet naše poznatky a budovat důvěryhodná partnerství prostřednictvím nástrojů jako Transparency Notes a Impact Assessments. Mnoho z těchto zdrojů najdete na [https://aka.ms/RAI](https://aka.ms/RAI).
Přístup Microsoftu k odpovědné AI vychází z našich principů AI: spravedlnost, spolehlivost a bezpečnost, ochrana soukromí a zabezpečení, začlenění, transparentnost a odpovědnost.

Velké modely pro přirozený jazyk, obraz a řeč – jako ty použité v tomto příkladu – se potenciálně mohou chovat nespravedlivě, nespolehlivě nebo urážlivě, což může vést k újmu. Pro informace o rizicích a omezeních konzultujte [Transparency note služby Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text).

Doporučeným přístupem k omezení těchto rizik je začlenění bezpečnostního systému do vaší architektury, který dokáže detekovat a zabránit škodlivému chování. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) poskytuje nezávislou vrstvu ochrany, schopnou detekovat škodlivý obsah generovaný uživateli i AI v aplikacích a službách. Azure AI Content Safety zahrnuje textové a obrazové API, která umožňují detekovat škodlivý materiál. V Azure AI Foundry služba Content Safety umožňuje zobrazovat, prozkoumávat a vyzkoušet ukázkový kód pro detekci škodlivého obsahu napříč různými modalitami. Následující [rychlý start dokumentace](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vás provede používáním požadavků na tuto službu.
Dalším aspektem, který je třeba vzít v úvahu, je celkový výkon aplikace. U multimodálních a multimodelových aplikací znamená výkon to, že systém funguje tak, jak vy a vaši uživatelé očekáváte, včetně nevytváření škodlivého obsahu. Je důležité posoudit výkon vaší celkové aplikace pomocí [hodnotitelů výkonu, kvality, rizika a bezpečnosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Máte také možnost vytvářet a hodnotit s použitím [vlastních hodnotitelů](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Svoji AI aplikaci můžete vyhodnocovat ve svém vývojovém prostředí pomocí [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Na základě testovací datové sady nebo cíle jsou generace vaší generativní AI aplikace kvantitativně měřeny pomocí vestavěných hodnotitelů nebo vlastních hodnotitelů dle vašeho výběru. Pro začátek s azure ai evaluation sdk k vyhodnocení vašeho systému můžete sledovat [rychlý průvodce](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po spuštění hodnocení můžete [vizualizovat výsledky v Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ochranné známky

Tento projekt může obsahovat ochranné známky nebo loga projektů, produktů nebo služeb. Autorizované použití ochranných známek nebo log Microsoftu podléhá a musí být v souladu s [pravidly Microsoft pro ochranné známky a značky](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Použití ochranných známek nebo log Microsoftu v upravených verzích tohoto projektu nesmí způsobovat záměnu ani neimplikovat sponzorství Microsoftu. Jakékoli použití ochranných známek nebo log třetích stran podléhá pravidlům těchto třetích stran.

## Jak získat pomoc

Pokud se zaseknete nebo máte nějaké otázky ohledně vytváření AI aplikací, připojte se:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Pokud máte zpětnou vazbu k produktu nebo narazíte na chyby při vývoji, navštivte:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace je doporučován profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->