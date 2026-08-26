# Phi Cookbook: Praktické příklady s modely Phi od Microsoftu

[![Otevřít a použít ukázky v GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Otevřít ve vývojových kontejnerech](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Přispěvatelé na GitHubu](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Problémy na GitHubu](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Pull requesty na GitHubu](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi je řada open source AI modelů vyvinutých společností Microsoft.

Phi je v současné době nejsilnější a nejefektivnější malý jazykový model (SLM) s velmi dobrými výsledky v oblasti vícejazyčnosti, uvažování, generování textu/chatů, kódování, obrázků, audia a dalších scénářů.

Phi můžete nasadit na cloud nebo na edge zařízení a snadno si postavit generativní AI aplikace s omezeným výpočetním výkonem.

Postupujte podle těchto kroků, jak začít používat tyto zdroje:
1. **Vytvořte fork repozitáře**: Klikněte na [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Klonujte repozitář**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Přidejte se do Microsoft AI Discord komunity a potkejte odborníky a další vývojáře**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cs/cover.eb18d1b9605d754b.webp)

### 🌐 Podpora více jazyků

#### Podporováno pomocí GitHub Action (Automatické a vždy aktuální)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabština](../ar/README.md) | [Bengálština](../bn/README.md) | [Bulharština](../bg/README.md) | [Barmsky (Myanmar)](../my/README.md) | [Čínština (zjednodušená)](../zh-CN/README.md) | [Čínština (tradiční, Hongkong)](../zh-HK/README.md) | [Čínština (tradiční, Macao)](../zh-MO/README.md) | [Čínština (tradiční, Taiwan)](../zh-TW/README.md) | [Chorvatština](../hr/README.md) | [Čeština](./README.md) | [Dánština](../da/README.md) | [Nizozemština](../nl/README.md) | [Estonština](../et/README.md) | [Finština](../fi/README.md) | [Francouzština](../fr/README.md) | [Němčina](../de/README.md) | [Řečtina](../el/README.md) | [Hebrejština](../he/README.md) | [Hindština](../hi/README.md) | [Maďarština](../hu/README.md) | [Indonéština](../id/README.md) | [Italština](../it/README.md) | [Japonština](../ja/README.md) | [Kannadština](../kn/README.md) | [Khmerština](../km/README.md) | [Korejština](../ko/README.md) | [Litevština](../lt/README.md) | [Malajština](../ms/README.md) | [Malajalámština](../ml/README.md) | [Maráthština](../mr/README.md) | [Nepálština](../ne/README.md) | [Nigerijská pidžin](../pcm/README.md) | [Norština](../no/README.md) | [Perština (Farsi)](../fa/README.md) | [Polština](../pl/README.md) | [Portugalština (Brazílie)](../pt-BR/README.md) | [Portugalština (Portugalsko)](../pt-PT/README.md) | [Paňdžábština (Gurmukhi)](../pa/README.md) | [Rumunština](../ro/README.md) | [Ruština](../ru/README.md) | [Srbština (cyrilice)](../sr/README.md) | [Slovenština](../sk/README.md) | [Slovinština](../sl/README.md) | [Španělština](../es/README.md) | [Svahilština](../sw/README.md) | [Švédština](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamilština](../ta/README.md) | [Telugština](../te/README.md) | [Thajština](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinština](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamština](../vi/README.md)

> **Raději klonovat lokálně?**
>
> Tento repozitář obsahuje více než 50 jazykových překladů, což výrazně zvětšuje velikost ke stažení. Pro klonování bez překladů použijte sparse checkout:
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
> To vám poskytne vše, co potřebujete ke splnění kurzu, s mnohem rychlejším stahováním.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Obsah

- Úvod
  - [Vítejte v rodině Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Nastavení vašeho prostředí](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Porozumění klíčovým technologiím](./md/01.Introduction/01/01.Understandingtech.md)
  - [Bezpečnost AI pro modely Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Podpora hardwaru Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Modely Phi a dostupnost na různých platformách](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Používání Guidance-ai a Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Modely na GitHub Marketplace](https://github.com/marketplace/models)
  - [Katalog AI modelů Azure](https://ai.azure.com)

- Inferenční Phi v různém prostředí
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub modely](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Microsoft Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Inferenční Phi rodiny
    - [Inference Phi na iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inference Phi na Androidu](./md/01.Introduction/03/Android_Inference.md)
    - [Inference Phi na Jetsonu](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inference Phi na AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inference Phi s Apple MLX Frameworkem](./md/01.Introduction/03/MLX_Inference.md)
    - [Inference Phi na lokálním serveru](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inference Phi na vzdáleném serveru pomocí AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inference Phi s Rustem](./md/01.Introduction/03/Rust_Inference.md)
    - [Inference Phi–Vision lokálně](./md/01.Introduction/03/Vision_Inference.md)
    - [Inference Phi s Kaito AKS, Azure kontejnery (oficiální podpora)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Kvantifikace Phi rodiny](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Kvantizace Phi-3.5 / 4 pomocí llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Kvantizace Phi-3.5 / 4 pomocí Generative AI rozšíření pro onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Kvantizace Phi-3.5 / 4 pomocí Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Kvantizace Phi-3.5 / 4 pomocí Apple MLX Frameworku](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Hodnocení Phi
    - [Zodpovědná AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Microsoft Foundry pro hodnocení](./md/01.Introduction/05/AIFoundry.md)
    - [Použití Promptflow pro hodnocení](./md/01.Introduction/05/Promptflow.md)
 
- RAG s Azure AI Search
    - [Jak používat Phi-4-mini a Phi-4-multimodal (RAG) s Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)
    - [Zero-Cloud lokální hybridní RAG s SQLite FTS5 a phi-4-mini](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-mini_Local_Hybrid_RAG_SQLite_FTS5.ipynb)

- Příklady vývoje aplikací Phi
  - Textové a chat aplikace
    - Phi-4 příklady 
      - [📓] [Chat s Phi-4-mini ONNX modelem](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat s Phi-4 lokálním ONNX modelem v .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Console aplikace v .NET pro chat s Phi-4 ONNX pomocí Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)

    - Vzorky Phi-3 / 3.5
      - [Místní chatbot v prohlížeči používající Phi3, ONNX Runtime Web a WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - Interaktivní Phi-3-mini a OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Vytváření wrapperu a použití Phi-3 s MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Optimalizace modelu - Jak optimalizovat model Phi-3-min pro ONNX Runtime Web s Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 aplikace s Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 Multi Model AI Powered Notes App Sample](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Doladění a integrace vlastních modelů Phi-3 pomocí Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Doladění a integrace vlastních modelů Phi-3 pomocí Prompt flow v Microsoft Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Vyhodnocení doladěného modelu Phi-3 / Phi-3.5 v Microsoft Foundry se zaměřením na zásady odpovědné AI Microsoftu](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Vzorek jazykové predikce Phi-3.5-mini-instruct (čínština/angličtina)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Použití Windows GPU k vytvoření řešení Prompt flow s Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Použití Microsoft Phi-3.5 tflite k vytvoření Android aplikace](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET příklad používající lokální ONNX model Phi-3 pomocí Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Konzolová chatovací .NET aplikace s Semantic Kernel a Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Kódové ukázky Azure AI Inference SDK
    - Vzorky Phi-4
      - [📓] [Generování kódu projektu pomocí Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Vzorky Phi-3 / 3.5
      - [Vytvořte si vlastní Visual Studio Code GitHub Copilot Chat s Microsoft Phi-3 rodinou](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Vytvořte si vlastního chatovacího agenta Visual Studio Code Copilot s Phi-3.5 pomocí GitHub modelů](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Ukázky pokročilého uvažování
    - Vzorky Phi-4
      - [📓] [Vzorky Phi-4-mini-reasoning nebo Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Doladění Phi-4-mini-reasoning pomocí Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Doladění Phi-4-mini-reasoning pomocí Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning s GitHub modely](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-reasoning s Microsoft Foundry modely](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demo
      - [Phi-4-mini demo hostované na Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demo hostované na Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Ukázky Vision
    - Vzorky Phi-4
      - [📓] [Použití Phi-4-multimodal ke čtení obrázků a generování kódu](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)
    - Vzorky Phi-3 / 3.5
      -  [📓][Phi-3-vision-Image text to text](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - vizuální jazykový asistent - s Phi3-Vision a OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision vzorek více snímků nebo více obrázků](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision místní ONNX model používající Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menu založený Phi-3 Vision místní ONNX model používající Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Ukázky Reasoning-Vision
    - Phi-4-Reasoning-Vision-15B
      - [📓] [Použití Phi-4-Reasoning-Vision-15B k detekci přecházení mimo přechod](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb)
      - [📓] [Použití Phi-4-Reasoning-Vision-15B k matematice](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb)
      - [📓] [Použití Phi-4-Reasoning-Vision-15B k detekci UI](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb)

  - Ukázky matematiky
    -  Vzorky Phi-4-Mini-Flash-Reasoning-Instruct  [Ukázka matematiky s Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - Ukázky zvuku
    - Vzorky Phi-4
      - [📓] [Extrahování přepisů zvuku pomocí Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Vzorek zvuku Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Vzorek překladu řeči Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET konzolová aplikace používající Phi-4-multimodal ke zpracování zvukového souboru a generování přepisu](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - Ukázky MOE
    - Vzorky Phi-3 / 3.5
      - [📓] [Vzorek sociálních médií s Phi-3.5 Mixture of Experts Models (MoEs)](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Vytváření Retrieval-Augmented Generation (RAG) pipeline s NVIDIA NIM Phi-3 MOE, Azure AI Search a LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Ukázky volání funkcí
    - Vzorky Phi-4 🆕
      -  [📓] [Použití volání funkcí s Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Použití volání funkcí k vytvoření multi-agentů s Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Použití volání funkcí s Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Použití volání funkcí s ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Ukázky multimodálního míchání
    - Vzorky Phi-4 🆕
      -  [📓] [Použití Phi-4-multimodal jako technologického novináře](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET konzolová aplikace používající Phi-4-multimodal k analýze obrázků](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Doladění Phi vzorků
  - [Scénáře doladění](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Doladění vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Doladění Nechte Phi-3 stát se průmyslovým expertem](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Doladění Phi-3 s AI Toolkit pro VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Doladění Phi-3 s Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Doladění Phi-3 s Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Doladění Phi-3 s QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Doladění Phi-3 s Microsoft Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Doladění Phi-3 s Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Doladění s Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Doladění s Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Doladění Phi-3-vision s Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)

  - [Jemné doladění Phi-3 s Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Jemné doladění Phi-3-vision (oficiální podpora)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Jemné doladění Phi-3 s Kaito AKS, Azure kontejnery (oficiální podpora)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Jemné doladění Phi-3 a 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Praktická laboratoř
  - [Objevování nejmodernějších modelů: LLM, SLM, lokální vývoj a další](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Odemknutí potenciálu NLP: Jemné doladění s Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Akademické výzkumné články a publikace
  - [Textbooks Are All You Need II: technická zpráva phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Technická zpráva Phi-3: Vysoce schopný jazykový model přímo ve vašem telefonu](https://arxiv.org/abs/2404.14219)
  - [Technická zpráva Phi-4](https://arxiv.org/abs/2412.08905)
  - [Technická zpráva Phi-4-Mini: Kompaktní, ale výkonné multimodální jazykové modely pomocí Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Optimalizace malých jazykových modelů pro volání funkcí ve vozidle](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Jemné doladění PHI-3 pro odpovídání na otázky s více možnostmi: Metodologie, výsledky a výzvy](https://arxiv.org/abs/2501.01588)
  - [Technická zpráva Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Technická zpráva Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Používání Phi modelů

### Phi na Microsoft Foundry

Můžete se naučit, jak používat Microsoft Phi a jak stavět E2E řešení na různých hardwarech. Chcete-li Phi sami vyzkoušet, začněte hraním s modely a přizpůsobováním Phi svým scénářům pomocí [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Více se dozvíte v Začínáme s [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Hřiště (Playground)**
Každý model má své vlastní hřiště pro testování modelu [Azure AI Playground](https://aka.ms/try-phi3).

### Phi na GitHub modelech

Můžete se naučit, jak používat Microsoft Phi a jak stavět E2E řešení na různých hardwarech. Chcete-li Phi sami vyzkoušet, začněte hrát s modelem a přizpůsobovat Phi svým scénářům pomocí [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Více se dozvíte v Začínáme s [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Hřiště (Playground)**
Každý model má vyhrazené [hřiště pro testování modelu](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi na Hugging Face

Model lze také najít na [Hugging Face](https://huggingface.co/microsoft)

**Hřiště (Playground)**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 Další kurzy

Náš tým produkuje další kurzy! Podívejte se:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j pro začátečníky](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js pro začátečníky](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain pro začátečníky](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD pro začátečníky](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI pro začátečníky](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP pro začátečníky](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents pro začátečníky](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Séria Generativní AI
[![Generativní AI pro začátečníky](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Základní učení
[![Strojové učení pro začátečníky](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science pro začátečníky](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI pro začátečníky](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kybernetická bezpečnost pro začátečníky](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webový vývoj pro začátečníky](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT pro začátečníky](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR vývoj pro začátečníky](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Séria Copilot
[![Copilot pro AI párové programování](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot pro C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Odpovědná AI 

Microsoft se zavazuje pomáhat našim zákazníkům používat naše AI produkty odpovědně, sdílet naše poznatky a budovat partnerství založená na důvěře prostřednictvím nástrojů jako jsou Transparency Notes a Impact Assessments. Mnoho z těchto zdrojů najdete na [https://aka.ms/RAI](https://aka.ms/RAI).
Přístup Microsoftu k odpovědné AI je založen na našich AI principech: spravedlnost, spolehlivost a bezpečnost, soukromí a zabezpečení, inkluzivita, transparentnost a odpovědnost.

Velké modely pro přirozený jazyk, obrázky a řeč - jako ty použité v tomto příkladu - se mohou potenciálně chovat nespravedlivě, nespolehlivě nebo urážlivě, což může způsobit škodu. Prosím nahlédněte do [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), abyste byli informováni o rizicích a omezeních.


Doporučeným přístupem k zmírnění těchto rizik je zahrnout do vaší architektury bezpečnostní systém, který dokáže detekovat a zabránit škodlivému chování. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) poskytuje nezávislou vrstvu ochrany, která dokáže detekovat škodlivý obsah generovaný uživateli i AI v aplikacích a službách. Azure AI Content Safety zahrnuje API pro text a obrázky, které vám umožňují detekovat škodlivý materiál. V Microsoft Foundry služba Content Safety umožňuje prohlížet, zkoumat a vyzkoušet ukázkové kódy pro detekci škodlivého obsahu napříč různými modalitami. Následující [dokumentace quickstart](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vás provede vytvářením požadavků na službu.

Dalším aspektem, který je třeba vzít v úvahu, je celkový výkon aplikace. U multimodálních a multimodelových aplikací považujeme za výkon, že systém funguje podle očekávání vás a vašich uživatelů, včetně nevytváření škodlivých výstupů. Je důležité posoudit výkon vaší celkové aplikace pomocí [hodnotitelů Výkon a Kvalita a Riziko a Bezpečnost](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Máte také možnost vytvářet a hodnotit pomocí [vlastních hodnotitelů](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Můžete hodnotit vaši AI aplikaci ve vašem vývojovém prostředí pomocí [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Na základě testovacího datasetu nebo cíle jsou generace vaší generativní AI aplikace kvantitativně měřeny pomocí vestavěných hodnotitelů nebo vlastních hodnotitelů podle vašeho výběru. Pro začátek s Azure AI Evaluation SDK, abyste mohli hodnotit váš systém, můžete sledovat [průvodce rychlým startem](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po spuštění hodnocení můžete [vizualizovat výsledky v Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## Ochranné známky

Tento projekt může obsahovat ochranné známky nebo loga projektů, produktů či služeb. Autorizované používání ochranných známek nebo log Microsoft podléhá a musí se řídit [Pokyny Microsoftu pro ochranné známky a značky](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Používání ochranných známek nebo log Microsoft v upravených verzích tohoto projektu nesmí způsobovat záměnu ani naznačovat sponzorství ze strany Microsoftu. Jakékoliv použití ochranných známek nebo log třetích stran podléhá zásadám těchto třetích stran.

## Získání pomoci

Pokud se zaseknete nebo máte jakékoliv dotazy týkající se tvorby AI aplikací, připojte se:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Pokud máte zpětnou vazbu k produktu nebo narazíte na chyby při vývoji, navštivte:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->