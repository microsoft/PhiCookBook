# Phi szakácskönyv: Gyakorlati példák a Microsoft Phi modelljeivel

[![Nyisd meg és használd a mintákat GitHub Codespaces-ben](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Nyisd meg Dev Containers-ben](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub közreműködők](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub hibák](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-kérelmek](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR kérések üdvözölve](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub figyelők](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub elágazások](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub csillagok](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

A Phi a Microsoft által fejlesztett nyílt forráskódú mesterséges intelligencia modellek sorozata.

A Phi jelenleg a legerősebb és költséghatékonyabb kis nyelvi modell (SLM), kiváló eredményeket elérve többnyelvűség, érvelés, szöveg/chat generálás, kódolás, képek, hang és egyéb feladatok terén.

Telepítheted a Phi modellt felhőbe vagy élő eszközökre, és könnyen építhetsz generatív AI alkalmazásokat korlátozott számítási erőforrással.

Kövesd az alábbi lépéseket a kezdéshez ezekkel az erőforrásokkal:
1. **Készíts Forkot a tárolóról**: Kattints [![GitHub elágazások](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Klónozd a tárolót**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Csatlakozz a Microsoft AI Discord közösséghez, és ismerkedj meg szakértőkkel és fejlesztőtársakkal**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![borító](../../translated_images/hu/cover.eb18d1b9605d754b.webp)

### 🌐 Többnyelvű támogatás

#### GitHub Action révén támogatott (Automatikus és mindig naprakész)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arab](../ar/README.md) | [Bengáli](../bn/README.md) | [Bolgár](../bg/README.md) | [Burmai (Myanmar)](../my/README.md) | [Kínai (egyszerűsített)](../zh-CN/README.md) | [Kínai (hagyományos, Hong Kong)](../zh-HK/README.md) | [Kínai (hagyományos, Makaó)](../zh-MO/README.md) | [Kínai (hagyományos, Tajvan)](../zh-TW/README.md) | [Horvát](../hr/README.md) | [Cseh](../cs/README.md) | [Dán](../da/README.md) | [Holland](../nl/README.md) | [Észt](../et/README.md) | [Finn](../fi/README.md) | [Francia](../fr/README.md) | [Német](../de/README.md) | [Görög](../el/README.md) | [Héber](../he/README.md) | [Hindi](../hi/README.md) | [Magyar](./README.md) | [Indonéz](../id/README.md) | [Olasz](../it/README.md) | [Japán](../ja/README.md) | [Kannada](../kn/README.md) | [Koreai](../ko/README.md) | [Litván](../lt/README.md) | [Maláj](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepáli](../ne/README.md) | [Nigériai pidgin](../pcm/README.md) | [Norvég](../no/README.md) | [Perzsa (Fárszi)](../fa/README.md) | [Lengyel](../pl/README.md) | [Portugál (Brazília)](../pt-BR/README.md) | [Portugál (Portugália)](../pt-PT/README.md) | [Pandzsábi (Gurmukhi)](../pa/README.md) | [Román](../ro/README.md) | [Orosz](../ru/README.md) | [Szerb (cirill)](../sr/README.md) | [Szlovák](../sk/README.md) | [Szlovén](../sl/README.md) | [Spanyol](../es/README.md) | [Szuahéli](../sw/README.md) | [Svéd](../sv/README.md) | [Tagalog (Filipinó)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Török](../tr/README.md) | [Ukrán](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnami](../vi/README.md)

> **Inkábbe helyileg klónoznál?**
>
> Ez a tároló több mint 50 nyelvű fordítást tartalmaz, amelyek jelentősen megnövelik a letöltési méretet. Fordítások nélküli klónozáshoz használd a sparse checkout-ot:
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
> Ez mindent biztosít, amire szükséged van a kurzus teljesítéséhez gyorsabb letöltéssel.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Tartalomjegyzék
- Bevezetés - [Üdvözlünk a Phi Családban](./md/01.Introduction/01/01.PhiFamily.md) - [A környezeted beállítása](./md/01.Introduction/01/01.EnvironmentSetup.md) - [A kulcsfontosságú technológiák megértése](./md/01.Introduction/01/01.Understandingtech.md) - [AI biztonság a Phi modellekhez](./md/01.Introduction/01/01.AISafety.md) - [Phi hardvertámogatás](./md/01.Introduction/01/01.Hardwaresupport.md) - [Phi modellek és elérhetőségük a különböző platformokon](./md/01.Introduction/01/01.Edgeandcloud.md) - [Guidance-ai és Phi használata](./md/01.Introduction/01/01.Guidance.md) - [GitHub Marketplace modellek](https://github.com/marketplace/models) - [Azure AI modell katalógus](https://ai.azure.com) - Phi inferencia különböző környezetben - [Hugging face](./md/01.Introduction/02/01.HF.md) - [GitHub modellek](./md/01.Introduction/02/02.GitHubModel.md) - [Microsoft Foundry modell katalógus](./md/01.Introduction/02/03.AzureAIFoundry.md) - [Ollama](./md/01.Introduction/02/04.Ollama.md) - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md) - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md) - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md) - Phi inferencia család - [Phi inferencia iOS-en](./md/01.Introduction/03/iOS_Inference.md) - [Phi inferencia Androidon](./md/01.Introduction/03/Android_Inference.md) - [Phi inferencia Jetsonon](./md/01.Introduction/03/Jetson_Inference.md) - [Phi inferencia AI PC-n](./md/01.Introduction/03/AIPC_Inference.md) - [Phi inferencia Apple MLX keretrendszerrel](./md/01.Introduction/03/MLX_Inference.md) - [Phi inferencia helyi szerveren](./md/01.Introduction/03/Local_Server_Inference.md) - [Phi inferencia távoli szerveren AI Toolkit használatával](./md/01.Introduction/03/Remote_Interence.md) - [Phi inferencia Rust nyelvvel](./md/01.Introduction/03/Rust_Inference.md) - [Phi inferencia--Vision helyi környezetben](./md/01.Introduction/03/Vision_Inference.md) - [Phi inferencia Kaito AKS, Azure konténerekkel (hivatalos támogatás)](./md/01.Introduction/03/Kaito_Inference.md) - [Phi család kvantálása](./md/01.Introduction/04/QuantifyingPhi.md) - [Phi-3.5 / 4 kvantálása llama.cpp használatával](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md) - [Phi-3.5 / 4 kvantálása Generative AI bővítményekkel onnxruntime-hoz](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md) - [Phi-3.5 / 4 kvantálása Intel OpenVINO használatával](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md) - [Phi-3.5 / 4 kvantálása Apple MLX keretrendszerrel](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md) - Phi értékelése - [Felelős AI](./md/01.Introduction/05/ResponsibleAI.md) - [Microsoft Foundry értékeléshez](./md/01.Introduction/05/AIFoundry.md) - [Promptflow használata értékeléshez](./md/01.Introduction/05/Promptflow.md) - RAG Azure AI Search-sel - [Hogyan használd Phi-4-mini és Phi-4-multimodal (RAG) modelleket Azure AI Search-sel](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb) - Phi alkalmazásfejlesztési minták - Szöveges és csevegő alkalmazások - Phi-4 minták - [📓] [Csevegés Phi-4-mini ONNX modellel](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md) - [Csevegés Phi-4 helyi ONNX modellel .NET-ben](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) - [Csevegő .NET konzolalkalmazás Phi-4 ONNX-szal Sementic Kernel használatával](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) - Phi-3 / 3.5 minták - [Helyi chatbot böngészőben Phi3, ONNX Runtime Web és WebGPU használatával](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat) - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md) - [Többmodell - Interaktív Phi-3-mini és OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md) - [MLFlow - Csomag készítése és Phi-3 használata MLFlow-val](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md) - [Model optimalizálás - Hogyan optimalizáld Phi-3-mini modellt ONNX Runtime Webhez Olive használatával](https://github.com/microsoft/Olive/tree/main/examples/phi3) - [WinUI3 alkalmazás Phi-3 mini-4k-instruct-onnx-szal](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/) - [WinUI3 Többmodeles, mesterséges intelligenciával támogatott jegyzet alkalmazás minta](https://github.com/microsoft/ai-powered-notes-winui3-sample) - [Egyedi Phi-3 modellek finomhangolása és integrálása Prompt flow-val](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md) - [Egyedi Phi-3 modellek finomhangolása és integrálása Prompt flow-val Microsoft Foundry-ban](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md) - [Finomhangolt Phi-3 / Phi-3.5 modell értékelése Microsoft Foundry-ban a Microsoft Felelős MI elveire fókuszálva](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md) - [📓] [Phi-3.5-mini-instruct nyelvi előrejelzés minta (kínai/angol)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb) - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md) - [Windows GPU használata Prompt flow megoldás létrehozásához Phi-3.5-Instruct ONNX-szal](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md) - [Microsoft Phi-3.5 tflite használata Android alkalmazás létrehozásához](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md) - [Kérdés-válasz .NET példa helyi ONNX Phi-3 modellel a Microsoft.ML.OnnxRuntime használatával](../../md/04.HOL/dotnet/src/LabsPhi301) - [Konzol alapú csevegő .NET alkalmazás Semantic Kernel-lel és Phi-3-mal](../../md/04.HOL/dotnet/src/LabsPhi302) - Azure AI Inferencia SDK kód alapú minták - Phi-4 minták - [📓] [Projektkód generálása Phi-4-multimodal használatával](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md) - Phi-3 / 3.5 minták - [Építsd meg saját Visual Studio Code GitHub Copilot Chat-edet Microsoft Phi-3 Családdal](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md) - [Hozd létre saját Visual Studio Code Chat Copilot Agent-ed Phi-3.5-tel GitHub modellekből](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md) - Haladó érvelési minták - Phi-4 minták - [📓] [Phi-4-mini-reasoning vagy Phi-4-reasoning minták](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md) - [📓] [Phi-4-mini-reasoning finomhangolása Microsoft Olive használatával](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Phi-4-mini-reasoning finomhangolása Apple MLX segítségével](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Phi-4-mini-reasoning GitHub modellekkel](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb) - [📓] [Phi-4-mini-reasoning Microsoft Foundry modellekkel](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb) -
Demók - [Phi-4-mini demók a Hugging Face Spaces-en](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo) - [Phi-4-multimodális demók a Hugging Face Spaces-en](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo) - Látási minták - Phi-4 minták - [📓] [Phi-4-multimodális használata képek olvasására és kód generálására](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) - Phi-3 / 3.5 minták - [📓][Phi-3-vision - Kép szövegből szövegbe](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html) - [📓][Phi-3-vision CLIP beágyazás](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [DEMO: Phi-3 újrahasznosítás](https://github.com/jennifermarsman/PhiRecycling/) - [Phi-3-vision - Vizuális nyelvi asszisztens - Phi3-Vision és OpenVINO használatával](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html) - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md) - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md) - [📓][Phi-3.5 Vision többrámás vagy többkép-minta](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb) - [Phi-3 Vision helyi ONNX modell a Microsoft.ML.OnnxRuntime .NET használatával](../../md/04.HOL/dotnet/src/LabsPhi303) - [Menü-alapú Phi-3 Vision helyi ONNX modell a Microsoft.ML.OnnxRuntime .NET használatával](../../md/04.HOL/dotnet/src/LabsPhi304) - Érvelési-látási minták - Phi-4-Reasoning-Vision-15B - [📓] [Phi-4-Reasoning-Vision-15B használata szabálytalan átkelés felismerésére](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb) - [📓] [Phi-4-Reasoning-Vision-15B használata matematikára](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb) - [📓] [Phi-4-Reasoning-Vision-15B használata UI felismerésére](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb) - Matematikai minták - Phi-4-Mini-Flash-Reasoning-Instruct minták [Matematika bemutató Phi-4-Mini-Flash-Reasoning-Instruct-tal](./md/02.Application/09.Math/MathDemo.ipynb) - Hangminták - Phi-4 minták - [📓] [Hangátiratok kinyerése Phi-4-multimodális használatával](./md/02.Application/05.Audio/Phi4/Transciption/README.md) - [📓] [Phi-4-multimodális hangminta](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb) - [📓] [Phi-4-multimodális beszédfordítási minta](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb) - [.NET konzolalkalmazás Phi-4-multimodális hang elemzésére és átirat generálására](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) - MOE minták - Phi-3 / 3.5 minták - [📓] [Phi-3.5 szakértők keveréke modellek (MoEs) közösségi média minta](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb) - [📓] [Hozzon létre Retrieval-Augmented Generation (RAG) csővezetéket NVIDIA NIM Phi-3 MOE, Azure AI Search és LlamaIndex használatával](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb) - - Függvényhívási minták - Phi-4 minták 🆕 - [📓] [Függvényhívás használata Phi-4-mini-vel](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md) - [📓] [Függvényhívás használata töb ügynök létrehozásához Phi-4-mini-vel](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb) - [📓] [Függvényhívás használata Ollama-val](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb) - [📓] [Függvényhívás használata ONNX-szel](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb) - Multimodális keverési minták - Phi-4 minták 🆕 - [📓] [Phi-4-multimodális használata technológiai újságíróként](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb) - [.NET konzolalkalmazás Phi-4-multimodális használatával képelemzéshez](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) - Finomhangoló Phi minták - [Finomhangolási forgatókönyvek](./md/03.FineTuning/FineTuning_Scenarios.md) - [Finomhangolás vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md) - [Finomhangolás: Engedje, hogy Phi-3 iparági szakértővé váljon](./md/03.FineTuning/LetPhi3gotoIndustriy.md) - [Finomhangolás Phi-3-mal az AI Toolkit for VS Code segítségével](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md) - [Finomhangolás Phi-3-mal az Azure Machine Learning Service segítségével](./md/03.FineTuning/Introduce_AzureML.md) - [Finomhangolás Phi-3-mal Lora használatával](./md/03.FineTuning/FineTuning_Lora.md) - [Finomhangolás Phi-3-mal QLora-val](./md/03.FineTuning/FineTuning_Qlora.md) - [Finomhangolás Phi-3-mal a Microsoft Foundry-val](./md/03.FineTuning/FineTuning_AIFoundry.md) - [Finomhangolás Phi-3-mal Azure ML CLI/SDK-val](./md/03.FineTuning/FineTuning_MLSDK.md) - [Finomhangolás Microsoft Olive-dzsal](./md/03.FineTuning/FineTuning_MicrosoftOlive.md) - [Finomhangolás Microsoft Olive gyakorlati laborral](./md/03.FineTuning/olive-lab/readme.md) - [Finomhangolás Phi-3-vision Weights and Bias használatával](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md) - [Finomhangolás Phi-3-mal Apple MLX Framework-kel](./md/03.FineTuning/FineTuning_MLX.md) - [Finomhangolás Phi-3-vision-nel (hivatalos támogatás)](./md/03.FineTuning/FineTuning_Vision.md) - [Finomhangolás Phi-3-mal Kaito AKS, Azure Containers (hivatalos támogatás)](./md/03.FineTuning/FineTuning_Kaito.md) - [Finomhangolás Phi-3-mal és 3.5 Vision-nel](https://github.com/2U1/Phi3-Vision-Finetune) - Gyakorlati labor - [Csúcstechnológiás modellek felfedezése: LLM-ek, SLM-ek, helyi fejlesztés és még sok más](https://github.com/microsoft/aitour-exploring-cutting-edge-models) - [Az NLP potenciáljának kiaknázása: Finomhangolás Microsoft Olive-dzsal](https://github.com/azure/Ignite_FineTuning_workshop) - Tudományos kutatási cikkek és kiadványok - [Textbooks Are All You Need II: phi-1.5 műszaki jelentés](https://arxiv.org/abs/2309.05463) - [Phi-3 műszaki jelentés: Nagyon képzett nyelvi modell helyileg a telefonodon](https://arxiv.org/abs/2404.14219) - [Phi-4 műszaki jelentés](https://arxiv.org/abs/2412.08905) - [Phi-4-Mini műszaki jelentés: Kompakt, mégis erős multimodális nyelvi modellek Mixture-of-LoRAs segítségével](https://arxiv.org/abs/2503.01743) - [Kis nyelvi modellek optimalizálása járműben történő függvényhíváshoz](https://arxiv.org/abs/2501.02342) - [(WhyPHI) PHI-3 finomhangolása többválasztásos kérdésekre: Módszertan, eredmények és kihívások](https://arxiv.org/abs/2501.01588) - [Phi-4-érvelés műszaki jelentés](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-érvelési Műszaki Jelentés](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)
# Phi Cookbook: Gyakorlati példák a Microsoft Phi modelljeivel

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

A Phi a Microsoft által fejlesztett nyílt forráskódú MI modellek sorozata.

A Phi jelenleg a legerősebb és legköltséghatékonyabb kis nyelvi modell (SLM), nagyon jó mérőszámokkal többnyelvűség, következtetés, szöveg-/chatgenerálás, kódolás, képek, hang és egyéb forgatókönyvek terén.

A Phi-t felhőbe vagy élő eszközökre telepítheti, és könnyedén építhet generatív MI alkalmazásokat korlátozott számítási teljesítmény mellett.

Kezdje el a használatot az alábbi lépésekkel:
1. **Forkolja le a tárolót**: Kattintson ide [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Klónozza a tárolót**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Csatlakozzon a Microsoft AI Discord közösséghez, és ismerkedjen meg szakértőkkel és fejlesztőkkel**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/hu/cover.eb18d1b9605d754b.webp)

### 🌐 Többnyelvű támogatás

#### GitHub Action segítségével támogatott (automatikus és naprakész)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arab](../ar/README.md) | [Bengáli](../bn/README.md) | [Bolgár](../bg/README.md) | [Burmai (Myanmar)](../my/README.md) | [Kínai (egyszerűsített)](../zh-CN/README.md) | [Kínai (hagyományos, Hong Kong)](../zh-HK/README.md) | [Kínai (hagyományos, Makaó)](../zh-MO/README.md) | [Kínai (hagyományos, Tajvan)](../zh-TW/README.md) | [Horvát](../hr/README.md) | [Cseh](../cs/README.md) | [Dán](../da/README.md) | [Holland](../nl/README.md) | [Észt](../et/README.md) | [Finn](../fi/README.md) | [Francia](../fr/README.md) | [Német](../de/README.md) | [Görög](../el/README.md) | [Héber](../he/README.md) | [Hindi](../hi/README.md) | [Magyar](./README.md) | [Indonéz](../id/README.md) | [Olasz](../it/README.md) | [Japán](../ja/README.md) | [Kannada](../kn/README.md) | [Koreai](../ko/README.md) | [Litván](../lt/README.md) | [Maláj](../ms/README.md) | [Malajálam](../ml/README.md) | [Maráthi](../mr/README.md) | [Nepáli](../ne/README.md) | [Nigériai Pidgin](../pcm/README.md) | [Norvég](../no/README.md) | [Perzsa (Fárszi)](../fa/README.md) | [Lengyel](../pl/README.md) | [Portugál (Brazília)](../pt-BR/README.md) | [Portugál (Portugália)](../pt-PT/README.md) | [Pandzsábi (Gurmukhi)](../pa/README.md) | [Román](../ro/README.md) | [Orosz](../ru/README.md) | [Szerb (cirill)](../sr/README.md) | [Szlovák](../sk/README.md) | [Szlovén](../sl/README.md) | [Spanyol](../es/README.md) | [Szuahéli](../sw/README.md) | [Svéd](../sv/README.md) | [Tagalog (filippínó)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Török](../tr/README.md) | [Ukrán](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnami](../vi/README.md)

> **Szeretné helyileg klónozni?**
>
> Ez a tároló több mint 50 nyelvi fordítást tartalmaz, ami jelentősen megnöveli a letöltési méretet. Ha fordítások nélkül szeretné klónozni, használja a sparse checkout-ot:
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
> Ez mindent megad, amire szüksége van a kurzus elvégzéséhez, sokkal gyorsabb letöltéssel.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Tartalomjegyzék

## Phi modellek használata

### Phi a Microsoft Foundry-n

Megtanulhatja, hogyan használja a Microsoft Phi-t, és hogyan építsen E2E megoldásokat különböző hardvereszközein. Ahhoz, hogy személyesen megtapasztalja a Phi-t, kezdje azzal, hogy játszik a modellekkel, és testreszabja Phi-t az Ön forgatókönyveihez a [Microsoft Foundry Azure AI Model Katalógus](https://aka.ms/phi3-azure-ai) segítségével. További információt találhat a [Microsoft Foundry-val való kezdésről](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Játszótér**  
Minden modellhez külön játszótér tartozik a teszteléshez: [Azure AI Playground](https://aka.ms/try-phi3).

### Phi GitHub modelleken

Megtanulhatja, hogyan használja a Microsoft Phi-t, és hogyan építsen E2E megoldásokat különböző hardvereszközein. Ahhoz, hogy személyesen megtapasztalja a Phi-t, kezdje azzal, hogy játszik a modellel, és testreszabja Phi-t az Ön forgatókönyveihez a [GitHub Model Katalógus](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) használatával. További információkat talál a [GitHub Model Katalógussal való kezdésről](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Játszótér**  
Minden modellhez külön [játszótér a teszteléshez](/md/02.QuickStart/GitHubModel_QuickStart.md) tartozik.

### Phi a Hugging Face-en

A modellt megtalálhatja a [Hugging Face-en](https://huggingface.co/microsoft)

**Játszótér**  
[Hugging Chat játszótér](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 Egyéb tanfolyamok

Csapatunk más tanfolyamokat is készít! Nézze meg:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain  
[![LangChain4j kezdőknek](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)  
[![LangChain.js kezdőknek](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)  
[![LangChain kezdőknek](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)  
---

### Azure / Edge / MCP / Agentek  
[![AZD kezdőknek](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Edge AI kezdőknek](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![MCP kezdőknek](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![MI Agentek kezdőknek](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)  

---

### Generatív MI sorozat  
[![Generatív MI kezdőknek](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Generatív MI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  

[![Generatív AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Alapvető tanulás
[![Gépi tanulás kezdőknek](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Adattudomány kezdőknek](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![Mesterséges intelligencia kezdőknek](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kiberbiztonság kezdőknek](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webes fejlesztés kezdőknek](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT kezdőknek](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR fejlesztés kezdőknek](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot sorozat
[![Copilot AI társprogramozáshoz](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET-hez](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot kaland](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Felelős MI

A Microsoft elkötelezett amellett, hogy ügyfeleink felelősségteljes módon használják MI-termékeinket, megosszák tanulságainkat, és bizalmon alapuló partnerségeket építsenek olyan eszközök révén, mint a Transzparencia Jegyzetek és Hatásvizsgálatok. Ezen források jelentős része elérhető a [https://aka.ms/RAI](https://aka.ms/RAI) címen.
A Microsoft felelős MI-hez való megközelítése az igazságosság, megbízhatóság és biztonság, adatvédelem és biztonság, befogadás, átláthatóság és elszámoltathatóság MI-elveiben gyökerezik.

A nagy léptékű természetes nyelvi, képi és beszédmodellek – mint amilyenek ebben a mintában is használatosak – potenciálisan igazságtalanul, megbízhatatlanul vagy sértő módon viselkedhetnek, ami károkat okozhat. Kérjük, olvassa el az [Azure OpenAI szolgáltatás Transzparencia jegyzetét](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) a kockázatok és korlátozások megismeréséhez.

A kockázatok enyhítésének ajánlott megközelítése egy olyan biztonsági rendszer beépítése az architektúrába, amely képes felismerni és megelőzni káros viselkedést. Az [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) egy független védelmi réteget biztosít, amely képes kártékony felhasználói és MI által generált tartalom felismerésére alkalmazásokban és szolgáltatásokban. Az Azure AI Content Safety szöveg- és képi API-kat tartalmaz, amelyek lehetővé teszik kártékony anyagok felismerését. A Microsoft Foundry keretében a Content Safety szolgáltatás lehetőséget nyújt a kártékony tartalom különböző modalitások szerinti felismerését célzó minta kódok megtekintésére, felfedezésére és kipróbálására. A következő [gyorstalpaló dokumentáció](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) végigvezeti Önt a szolgáltatás kéréseinek elküldésén.

További szempont az alkalmazás általános teljesítménye. Többmodalitású és többmodellű alkalmazások esetén a teljesítmény alatt azt értjük, hogy a rendszer úgy működik, ahogy Ön és a felhasználói elvárják, beleértve a kártékony eredmények nem előállítását is. Fontos az alkalmazás egészének teljesítményét értékelni a [Teljesítmény és Minőség valamint Kockázat és Biztonság értékelőkkel](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Lehetőség van egyedi értékelők létrehozására és használatára is [egyéni értékelők](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) segítségével.

Az AI-alkalmazás fejlesztői környezetben való értékelésére használhatja az [Azure AI Evaluation SDK-t](https://microsoft.github.io/promptflow/index.html). Akár egy tesztadatkészlet vagy egy cél alapján, generatív MI alkalmazása generációit mennyiségileg mérik beépített vagy általad választott egyéni értékelőkkel. Az azure ai evaluation sdk használatának megkezdéséhez az értékeléshez kövesse a [gyorstalpaló útmutatót](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Értékelés futtatása után az eredményeket [Microsoft Foundry-ban is megjelenítheti](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Védjegyek

Ez a projekt tartalmazhat védjegyeket vagy logókat projektek, termékek vagy szolgáltatások számára. A Microsoft védjegyek vagy logók jogosult használata az [Microsoft Védjegy- és Márka Útmutató](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) szerint engedélyezett és annak megfelelően kell történjen.
A Microsoft védjegyek vagy logók módosított verziókban való használata nem okozhat zavart vagy nem sugallhat Microsoft által szponzorált jelleget. Harmadik fél védjegyeinek vagy logóinak használata az adott harmadik fél irányelvei szerint történik.

## Segítségkérés

Ha elakad vagy kérdése van MI-alkalmazások fejlesztésével kapcsolatban, csatlakozzon:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Ha termék visszajelzést vagy hibákat tapasztal fejlesztés közben, látogasson el ide:

[![Microsoft Foundry fejlesztői fórum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:  
Ez a dokumentum a [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítószolgáltatással készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum anyanyelvű változata tekintendő irányadónak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->