# Phi Cookbook: Praktické příklady s modely Phi od Microsoftu

[![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi je řada open source AI modelů vyvinutých společností Microsoft.

Phi je v současnosti nejsilnější a zároveň nákladově nejefektivnější malý jazykový model (SLM) s velmi dobrými výsledky v oblasti vícejazyčnosti, odvozování, generování textu/chatů, programování, obrázků, zvuku a dalších scénářů.

Phi můžete nasadit do cloudu nebo na okrajová zařízení a snadno vytvořit generativní AI aplikace s omezeným výpočetním výkonem.

Postupujte podle těchto kroků a začněte využívat tyto zdroje:
1. **Vytvořte fork repozitáře**: Klikněte na [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Zkopírujte repozitář**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Připojte se ke komunitě Microsoft AI na Discordu a potkejte experty a další vývojáře**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cs/cover.eb18d1b9605d754b.webp)

### 🌐 Podpora vícejazyčnosti

#### Podporováno pomocí GitHub Action (automatizováno a stále aktuální)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](./README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Raději klonovat lokálně?**
>
> Tento repozitář obsahuje více než 50 překladů do různých jazyků, což výrazně zvětšuje velikost stažení. Pro klonování bez překladů použijte sparse checkout:
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
> To vám poskytne vše potřebné ke kompletnímu absolvování kurzu s mnohem rychlejším stažením.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Obsah pokračuje...
- Úvod - [Vítejte v rodině Phi](./md/01.Introduction/01/01.PhiFamily.md) - [Nastavení vašeho prostředí](./md/01.Introduction/01/01.EnvironmentSetup.md) - [Porozumění klíčovým technologiím](./md/01.Introduction/01/01.Understandingtech.md) - [Bezpečnost AI pro modely Phi](./md/01.Introduction/01/01.AISafety.md) - [Podpora hardwaru Phi](./md/01.Introduction/01/01.Hardwaresupport.md) - [Modely Phi a dostupnost napříč platformami](./md/01.Introduction/01/01.Edgeandcloud.md) - [Používání Guidance-ai a Phi](./md/01.Introduction/01/01.Guidance.md) - [Modely na GitHub Marketplace](https://github.com/marketplace/models) - [Katalog modelů Azure AI](https://ai.azure.com) - Inference Phi v různém prostředí - [Hugging face](./md/01.Introduction/02/01.HF.md) - [Modely na GitHubu](./md/01.Introduction/02/02.GitHubModel.md) - [Katalog modelů Microsoft Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md) - [Ollama](./md/01.Introduction/02/04.Ollama.md) - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md) - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md) - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md) - Inference Phi Family - [Inference Phi na iOS](./md/01.Introduction/03/iOS_Inference.md) - [Inference Phi na Androidu](./md/01.Introduction/03/Android_Inference.md) - [Inference Phi na Jetson](./md/01.Introduction/03/Jetson_Inference.md) - [Inference Phi na AI PC](./md/01.Introduction/03/AIPC_Inference.md) - [Inference Phi s Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md) - [Inference Phi na místním serveru](./md/01.Introduction/03/Local_Server_Inference.md) - [Inference Phi na vzdáleném serveru pomocí AI Toolkit](./md/01.Introduction/03/Remote_Interence.md) - [Inference Phi s Rust](./md/01.Introduction/03/Rust_Inference.md) - [Inference Phi – Vision lokálně](./md/01.Introduction/03/Vision_Inference.md) - [Inference Phi s Kaito AKS, Azure Containers (oficiální podpora)](./md/01.Introduction/03/Kaito_Inference.md) - [Kvantilace Phi Family](./md/01.Introduction/04/QuantifyingPhi.md) - [Kvantilace Phi-3.5 / 4 pomocí llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md) - [Kvantilace Phi-3.5 / 4 pomocí Generative AI rozšíření pro onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md) - [Kvantilace Phi-3.5 / 4 pomocí Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md) - [Kvantilace Phi-3.5 / 4 pomocí Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md) - Hodnocení Phi - [Odpovědná AI](./md/01.Introduction/05/ResponsibleAI.md) - [Microsoft Foundry pro hodnocení](./md/01.Introduction/05/AIFoundry.md) - [Používání Promptflow pro hodnocení](./md/01.Introduction/05/Promptflow.md) - RAG s Azure AI Search - [Jak používat Phi-4-mini a Phi-4-multimodal (RAG) s Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb) - Ukázky vývoje aplikací Phi - Textové a chatové aplikace - Ukázky Phi-4 - [📓] [Chat s Phi-4-mini ONNX modelem](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md) - [Chat s Phi-4 místním ONNX modelem .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) - [Chat .NET konzolová aplikace s Phi-4 ONNX pomocí Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) - Ukázky Phi-3 / 3.5 - [Lokální chatbot v prohlížeči pomocí Phi3, ONNX Runtime Web a WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat) - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md) - [Multi model - interaktivní Phi-3-mini a OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md) - [MLFlow - Vytváření wrapperu a používání Phi-3 s MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md) - [Optimalizace modelu - Jak optimalizovat model Phi-3-min pro ONNX Runtime Web pomocí Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3) - [WinUI3 aplikace s Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/) -[Ukázka WinUI3 aplikace Multi Model AI Powered Notes](https://github.com/microsoft/ai-powered-notes-winui3-sample) - [Jemné doladění a integrace vlastních modelů Phi-3 s Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md) - [Jemné doladění a integrace vlastních modelů Phi-3 s Prompt flow v Microsoft Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md) - [Hodnocení jemně vyladěného modelu Phi-3 / Phi-3.5 v Microsoft Foundry se zaměřením na principy odpovědné AI Microsoftu](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md) - [📓] [Ukázka predikce jazyka Phi-3.5-mini-instruct (čínština/angličtina)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb) - [Phi-3.5-Instruct WebGPU RAG chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md) - [Použití Windows GPU pro vytvoření řešení Prompt flow s Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md) - [Použití Microsoft Phi-3.5 tflite k vytvoření Android aplikace](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md) - [Příklad Q&A .NET pomocí místního ONNX Phi-3 modelu s Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301) - [Konzolová chat .NET aplikace s Semantic Kernel a Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302) - Ukázky kódu Azure AI Inference SDK - Ukázky Phi-4 - [📓] [Generování projektového kódu pomocí Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md) - Ukázky Phi-3 / 3.5 - [Vytvořte si vlastní chat GitHub Copilot ve Visual Studio Code s Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md) - [Vytvořte si vlastního chatovacího Copilot agenta ve Visual Studio Code s Phi-3.5 pomocí GitHub modelů](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md) - Ukázky pokročilého uvažování - Ukázky Phi-4 - [📓] [Ukázky Phi-4-mini-reasoning nebo Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md) - [📓] [Jemné doladění Phi-4-mini-reasoning s Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Jemné doladění Phi-4-mini-reasoning s Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Phi-4-mini-reasoning s GitHub modely](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb) - [📓] [Phi-4-mini-reasoning s Microsoft Foundry modely](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb) -
Ukázky - [Ukázky Phi-4-mini hostované na Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo) - [Ukázky Phi-4-multimodal hostované na Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo) - Vzorky pro vidění - Ukázky Phi-4 - [📓] [Použití Phi-4-multimodal pro čtení obrázků a generování kódu](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) - Ukázky Phi-3 / 3.5 - [📓][Phi-3-vision-Obrazový text na text](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html) - [📓][Phi-3-vision CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/) - [Phi-3-vision - Pomocník vizuálního jazyka - s Phi3-Vision a OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html) - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md) - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md) - [📓][Ukázka Phi-3.5 Vision více snímků nebo více obrázků](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb) - [Phi-3 Vision Lokální ONNX Model s Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303) - [Menu založený Phi-3 Vision Lokální ONNX Model s Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304) - Vzorky pro zobrazovací uvažování - Phi-4-Reasoning-Vision-15B - [📓] [Použití Phi-4-Reasoning-Vision-15B pro detekci přecházení mimo přechod](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb) - [📓] [Použití Phi-4-Reasoning-Vision-15B pro matematiku](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb) - [📓] [Použití Phi-4-Reasoning-Vision-15B pro detekci UI](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb) - Vzorky matematiky - Ukázky Phi-4-Mini-Flash-Reasoning-Instruct [Ukázka matematiky s Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb) - Vzorky zvuku - Ukázky Phi-4 - [📓] [Extrahování přepisů zvuku pomocí Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md) - [📓] [Ukázka zvuku Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb) - [📓] [Ukázka překladu řeči Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb) - [Konzolová aplikace .NET používající Phi-4-multimodal Audio ke zpracování zvukového souboru a generování přepisu](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) - Vzorky MoE - Ukázky Phi-3 / 3.5 - [📓] [Ukázka modelů směsi expertů (MoEs) Phi-3.5 na sociálních médiích](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb) - [📓] [Vytváření pipeline Retrieval-Augmented Generation (RAG) s NVIDIA NIM Phi-3 MOE, Azure AI Search a LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb) - - Ukázky volání funkcí - Ukázky Phi-4 🆕 - [📓] [Použití volání funkcí s Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md) - [📓] [Použití volání funkcí k vytvoření multi-agentů s Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb) - [📓] [Použití volání funkcí s Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb) - [📓] [Použití volání funkcí s ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb) - Ukázky multimodálního mixování - Ukázky Phi-4 🆕 - [📓] [Použití Phi-4-multimodal jako technologického novináře](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb) - [Konzolová aplikace .NET používající Phi-4-multimodal k analýze obrázků](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) - Ukázky dolaďování Phi - [Scénáře dolaďování](./md/03.FineTuning/FineTuning_Scenarios.md) - [Dolaďování vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md) - [Dolaďování Nechte Phi-3 stát se průmyslovým expertem](./md/03.FineTuning/LetPhi3gotoIndustriy.md) - [Dolaďování Phi-3 s AI Toolkit pro VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md) - [Dolaďování Phi-3 s Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md) - [Dolaďování Phi-3 s Lora](./md/03.FineTuning/FineTuning_Lora.md) - [Dolaďování Phi-3 s QLora](./md/03.FineTuning/FineTuning_Qlora.md) - [Dolaďování Phi-3 s Microsoft Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md) - [Dolaďování Phi-3 s Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md) - [Dolaďování s Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md) - [Dolaďovací laboratoř Microsoft Olive Hands-On](./md/03.FineTuning/olive-lab/readme.md) - [Dolaďování Phi-3-vision s Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md) - [Dolaďování Phi-3 s Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md) - [Dolaďování Phi-3-vision (oficiální podpora)](./md/03.FineTuning/FineTuning_Vision.md) - [Dolaďování Phi-3 s Kaito AKS, Azure kontejnery (oficiální podpora)](./md/03.FineTuning/FineTuning_Kaito.md) - [Dolaďování Phi-3 a 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune) - Praktická laboratoř - [Prozkoumání nejmodernějších modelů: LLM, SLM, lokální vývoj a další](https://github.com/microsoft/aitour-exploring-cutting-edge-models) - [Odemknutí potenciálu NLP: Dolaďování s Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop) - Akademické vědecké práce a publikace - [Textbooks Are All You Need II: technická zpráva phi-1.5](https://arxiv.org/abs/2309.05463) - [Technická zpráva Phi-3: Vysoce schopný jazykový model lokálně na vašem telefonu](https://arxiv.org/abs/2404.14219) - [Technická zpráva Phi-4](https://arxiv.org/abs/2412.08905) - [Technická zpráva Phi-4-Mini: Kompaktní, ale výkonné multimodální jazykové modely přes směs LoRA](https://arxiv.org/abs/2503.01743) - [Optimalizace malých jazykových modelů pro volání funkcí v automobilu](https://arxiv.org/abs/2501.02342) - [(WhyPHI) Dolaďování PHI-3 pro odpovídání na otázky s více možnostmi: Metodologie, výsledky a výzvy](https://arxiv.org/abs/2501.01588) - [Technická zpráva Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Technická zpráva Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)
# Phi Cookbook: Praktické příklady s modely Phi od Microsoftu

[![Otevřete a použijte ukázky v GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Otevřete v Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Přispěvatelé na GitHubu](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Problémy na GitHubu](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Pull requesty na GitHubu](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs vítány](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Watcher na GitHubu](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Forky na GitHubu](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Hvězdy na GitHubu](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi je série open source AI modelů vyvinutých společností Microsoft.

Phi je v současné době nejsilnějším a nákladově nejekonomičtějším malým jazykovým modelem (SLM), s velmi dobrými výsledky v vícejazyčném prostředí, u odvozování, generování textu/rozhovorů, kódu, obrázků, zvuku a dalších scénářů.

Phi můžete nasadit do cloudu nebo na edge zařízení a snadno vytvářet generativní AI aplikace s omezeným výpočetním výkonem.

Postupujte podle těchto kroků pro začátek práce s těmito zdroji:
1. **Vytvořte fork repozitáře**: Klikněte na [![Forky na GitHubu](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Naklonujte repozitář**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Přidejte se do komunity Microsoft AI na Discordu a setkejte se s experty a dalšími vývojáři**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cs/cover.eb18d1b9605d754b.webp)

### 🌐 Vícejazyčná podpora

#### Podporováno přes GitHub Action (automaticky a vždy aktuální)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabština](../ar/README.md) | [Bengálština](../bn/README.md) | [Bulharština](../bg/README.md) | [Barmsky (Myanmar)](../my/README.md) | [Čínština (zjednodušená)](../zh-CN/README.md) | [Čínština (tradiční, Hongkong)](../zh-HK/README.md) | [Čínština (tradiční, Macau)](../zh-MO/README.md) | [Čínština (tradiční, Tchaj-wan)](../zh-TW/README.md) | [Chorvatština](../hr/README.md) | [Čeština](./README.md) | [Dánština](../da/README.md) | [Nizozemština](../nl/README.md) | [Estonština](../et/README.md) | [Finština](../fi/README.md) | [Francouzština](../fr/README.md) | [Němčina](../de/README.md) | [Řečtina](../el/README.md) | [Hebrejština](../he/README.md) | [Hindština](../hi/README.md) | [Maďarština](../hu/README.md) | [Indonéština](../id/README.md) | [Italština](../it/README.md) | [Japonština](../ja/README.md) | [Kannadština](../kn/README.md) | [Korejština](../ko/README.md) | [Litevština](../lt/README.md) | [Malajština](../ms/README.md) | [Malayalam](../ml/README.md) | [Maráthština](../mr/README.md) | [Nepálština](../ne/README.md) | [Nigerijský pidžin](../pcm/README.md) | [Norština](../no/README.md) | [Perština (Fársí)](../fa/README.md) | [Polština](../pl/README.md) | [Portugalština (Brazílie)](../pt-BR/README.md) | [Portugalština (Portugalsko)](../pt-PT/README.md) | [Paňdžábština (Gurmukhí)](../pa/README.md) | [Rumunština](../ro/README.md) | [Ruština](../ru/README.md) | [Srbština (cyrilice)](../sr/README.md) | [Slovenština](../sk/README.md) | [Slovinština](../sl/README.md) | [Španělština](../es/README.md) | [Svahilština](../sw/README.md) | [Švédština](../sv/README.md) | [Tagalog (Filipínština)](../tl/README.md) | [Tamilština](../ta/README.md) | [Telugština](../te/README.md) | [Thajština](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinština](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamština](../vi/README.md)

> **Dáváte přednost klonování lokálně?**
>
> Tento repozitář obsahuje více než 50 překladů do různých jazyků, což výrazně zvyšuje velikost stahování. Pro klonování bez překladů použijte sparse checkout:
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
> Tím získáte vše potřebné ke kompletnímu dokončení kurzu s mnohem rychlejším stažením.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Obsah

## Použití modelů Phi

### Phi na Microsoft Foundry

Můžete se naučit, jak používat Microsoft Phi a jak vytvářet end-to-end řešení na různých hardwarových zařízeních. Pro vyzkoušení Phi začněte hraním s modely a přizpůsobením Phi pro vaše scénáře pomocí [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Více se dozvíte v začátečnickém průvodci s [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Playground**
Každý model má vyhrazenou hřiště pro testování modelu na [Azure AI Playground](https://aka.ms/try-phi3).

### Phi na GitHub Models

Můžete se naučit, jak používat Microsoft Phi a jak vytvářet end-to-end řešení na různých hardwarových zařízeních. Pro vyzkoušení Phi začněte hraním s modelem a přizpůsobením Phi pro vaše scénáře pomocí [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Více se dozvíte v začátečnickém průvodci s [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**
Každý model má vyhrazené [playground k testování modelu](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi na Hugging Face

Model najdete také na [Hugging Face](https://huggingface.co/microsoft)

**Playground**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 Další kurzy

Náš tým vytváří další kurzy! Podívejte se:

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

### Série Generativní AI
[![Generativní AI pro začátečníky](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Základní učení
[![ML pro začátečníky](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science pro začátečníky](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI pro začátečníky](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kybernetická bezpečnost pro začátečníky](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webový vývoj pro začátečníky](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT pro začátečníky](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR vývoj pro začátečníky](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Série Copilot
[![Copilot pro AI párové programování](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot pro C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot dobrodružství](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Odpovědná AI

Microsoft se zavazuje pomáhat svým zákazníkům používat naše AI produkty odpovědně, sdílet naše poznatky a budovat partnerství založená na důvěře prostřednictvím nástrojů, jako jsou Poznámky o transparentnosti a Hodnocení dopadů. Mnoho těchto zdrojů naleznete na [https://aka.ms/RAI](https://aka.ms/RAI).
Přístup Microsoftu k odpovědné AI je založen na našich principiích AI: spravedlnost, spolehlivost a bezpečnost, ochrana soukromí a zabezpečení, inkluzivita, transparentnost a odpovědnost.

Velké modely pro přirozený jazyk, obraz a řeč – jako ty použité v tomto příkladu – mohou potenciálně vykazovat chování, které je nespravedlivé, nespolehlivé nebo urážlivé, což může způsobovat škody. Pro informace o rizicích a omezeních si prosím prostudujte [Poznámku o transparentnosti služby Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text).

Doporučený přístup ke zmírnění těchto rizik je začlenit do své architektury bezpečnostní systém, který dokáže detekovat a zabránit škodlivému chování. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) poskytuje nezávislou vrstvu ochrany, která dokáže v aplikacích a službách rozpoznat škodlivý obsah vytvořený uživateli i AI. Azure AI Content Safety zahrnuje API pro text a obraz, které umožňují odhalovat škodlivý materiál. V rámci Microsoft Foundry služba Content Safety umožňuje zobrazit, prozkoumat a vyzkoušet ukázkový kód pro detekci škodlivého obsahu v různých multimodálních formátech. Následující [dokumentace rychlého startu](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vás provede voláním této služby.

Dalším aspektem je celkový výkon aplikace. U multimodálních a vícemodelových aplikací považujeme výkon za to, že systém funguje tak, jak očekáváte vy i vaši uživatelé, včetně neprodukování škodlivých výstupů. Je důležité hodnotit výkon vaší aplikace pomocí [hodnotitelů výkonu, kvality, rizik a bezpečnosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Máte také možnost vytvářet a hodnotit pomocí [vlastních hodnotitelů](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Své AI aplikace můžete hodnotit ve svém vývojovém prostředí pomocí [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Vaše generativní AI výstupy jsou kvantitativně měřeny pomocí vestavěných nebo vlastních hodnotitelů podle zvoleného testovacího datasetu nebo cíle. Pro začátek s azure ai evaluation sdk a hodnocení systému můžete použít [průvodce rychlým startem](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po provedení běhu hodnocení můžete [vizualizovat výsledky v Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ochranné známky

Tento projekt může obsahovat ochranné známky nebo loga projektů, produktů či služeb. Autorizované použití ochranných známek nebo log Microsoftu podléhá a musí dodržovat [Pravidla užívání ochranných známek a značek Microsoftu](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Použití ochranných známek nebo log Microsoftu v upravených verzích tohoto projektu nesmí vést k záměně nebo naznačovat sponzorství Microsoftem. Jakékoli použití ochranných známek nebo log třetích stran podléhá zásadám těchto třetích stran.

## Získání pomoci

Pokud narazíte na problémy nebo máte otázky ohledně vytváření AI aplikací, připojte se:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Pokud máte zpětnou vazbu k produktu nebo řešíte chyby během vývoje, navštivte:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo mylné výklady vyplývající z používání tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->