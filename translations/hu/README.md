<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2e4b490f4bd424b095f21e38c6af33b",
  "translation_date": "2026-01-05T09:22:59+00:00",
  "source_file": "README.md",
  "language_code": "hu"
}
-->
# Phi szakácskönyv: Gyakorlati példák a Microsoft Phi modelljeivel

[![Nyisd meg és használd a példákat GitHub Codespaces-ben](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Megnyitás Dev Containers-ben](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub közreműködők](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub hibák](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-kérelmek](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![Küldj PR-t, szívesen fogadjuk](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub figyelők](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub csillagok](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

A Phi a Microsoft által fejlesztett nyílt forráskódú AI modellek sorozata.

A Phi jelenleg a legfejlettebb és leggazdaságosabb kis nyelvi modell (SLM), nagyon jó teljesítménymérőkkel többnyelvűség, érvelés, szöveg/csevegés generálás, programozás, képek, hang és egyéb helyzetekben.

Telepítheted a Phi-t a felhőbe vagy élő eszközökre is, és könnyen építhetsz generatív AI alkalmazásokat korlátozott számítási teljesítménnyel.

Kövessük az alábbi lépéseket ezeknek az erőforrásoknak a használatának megkezdéséhez:
1. **Forkold le a tárolót**: Kattints a [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Klónozd a tárolót**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Csatlakozz a Microsoft AI Discord közösséghez, és találkozz szakértőkkel és fejlesztőtársakkal**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![borító](../../translated_images/hu/cover.eb18d1b9605d754b.webp)

### 🌐 Többnyelvű támogatás

#### GitHub Action által támogatott (Automatikus és mindig friss)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arab](../ar/README.md) | [Bengáli](../bn/README.md) | [Bolgár](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Kínai (egyszerűsített)](../zh/README.md) | [Kínai (hagyományos, Hongkong)](../hk/README.md) | [Kínai (hagyományos, Makaó)](../mo/README.md) | [Kínai (hagyományos, Tajvan)](../tw/README.md) | [Horvát](../hr/README.md) | [Cseh](../cs/README.md) | [Dán](../da/README.md) | [Holland](../nl/README.md) | [Észt](../et/README.md) | [Finn](../fi/README.md) | [Francia](../fr/README.md) | [Német](../de/README.md) | [Görög](../el/README.md) | [Héber](../he/README.md) | [Hindi](../hi/README.md) | [Magyar](./README.md) | [Indonéz](../id/README.md) | [Olasz](../it/README.md) | [Japán](../ja/README.md) | [Kannada](../kn/README.md) | [Koreai](../ko/README.md) | [Litván](../lt/README.md) | [Maláj](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepáli](../ne/README.md) | [Nigériai pidgin](../pcm/README.md) | [Norvég](../no/README.md) | [Perzsa (fárszi)](../fa/README.md) | [Lengyel](../pl/README.md) | [Portugál (Brazília)](../br/README.md) | [Portugál (Portugália)](../pt/README.md) | [Pandzsábi (Gurmukhi)](../pa/README.md) | [Román](../ro/README.md) | [Orosz](../ru/README.md) | [Szerb (cirill)](../sr/README.md) | [Szlovák](../sk/README.md) | [Szlovén](../sl/README.md) | [Spanyol](../es/README.md) | [Szvahiili](../sw/README.md) | [Svéd](../sv/README.md) | [Tagalog (filippínó)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Török](../tr/README.md) | [Ukrán](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnami](../vi/README.md)

> **Inkább helyben klónoznál?**

> Ez a tároló 50+ nyelvi fordítást tartalmaz, ami jelentősen megnöveli a letöltés méretét. Ha fordítások nélkül szeretnéd klónozni, használd a sparse checkout-ot:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Így minden szükséges anyagot megszerzel a kurzus elvégzéséhez sokkal gyorsabb letöltéssel.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Tartalomjegyzék

- Bevezetés
  - [Üdvözölünk a Phi családban](./md/01.Introduction/01/01.PhiFamily.md)
  - [A környezeted beállítása](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Fontos technológiák megértése](./md/01.Introduction/01/01.Understandingtech.md)
  - [AI biztonság a Phi modellekhez](./md/01.Introduction/01/01.AISafety.md)
  - [Phi hardver támogatás](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi modellek és elérhetőség platformokon](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai és Phi használata](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace modellek](https://github.com/marketplace/models)
  - [Azure AI Modell katalógus](https://ai.azure.com)

- Phi inferencia különböző környezetekben
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub modellek](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry modell katalógus](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry helyi](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi család inferencia
    - [Phi inferencia iOS-en](./md/01.Introduction/03/iOS_Inference.md)
    - [Phi inferencia Androidon](./md/01.Introduction/03/Android_Inference.md)
    - [Phi inferencia Jetsonon](./md/01.Introduction/03/Jetson_Inference.md)
    - [Phi inferencia AI PC-n](./md/01.Introduction/03/AIPC_Inference.md)
    - [Phi inferencia Apple MLX keretrendszerrel](./md/01.Introduction/03/MLX_Inference.md)
    - [Phi inferencia helyi szerveren](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Phi inferencia távoli szerveren AI Toolkit használatával](./md/01.Introduction/03/Remote_Interence.md)
    - [Phi inferencia Rust-tal](./md/01.Introduction/03/Rust_Inference.md)
    - [Phi inferencia--Látás helyben](./md/01.Introduction/03/Vision_Inference.md)
    - [Phi inferencia Kaito AKS, Azure konténerek használatával (hivatalos támogatás)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi család kvantálása](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantálása llama.cpp-vel](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantálása Generative AI bővítményekkel onnxruntime-hoz](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantálása Intel OpenVINO-val](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantálása Apple MLX keretrendszerrel](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi értékelése
    - [Felelősségteljes AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry értékeléshez](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow használata értékeléshez](./md/01.Introduction/05/Promptflow.md)
 
- RAG Azure AI kereséssel
    - [Hogyan használd a Phi-4-mini és Phi-4-multimodal (RAG) modelleket Azure AI kereséssel](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi alkalmazás fejlesztési minták
  - Szöveg- és csevegőalkalmazások
    - Phi-4 minták 🆕
      - [📓] [Csevegj Phi-4-mini ONNX modellel](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Csevegj Phi-4 helyi ONNX modellel .NET-ben](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Csevegő .NET konzolalkalmazás Phi-4 ONNX-szel Sementic Kernel használatával](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 minták
      - [Helyi chatbot böngészőben Phi3, ONNX Runtime Web és WebGPU használatával](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino csevegő](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Többmodellezés - Interaktív Phi-3-mini és OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Wrapper készítése és Phi-3 használata MLFlow-val](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Model optimalizálás - Hogyan optimalizáljuk a Phi-3-minimodellt ONNX Runtime Web-hez Olive segítségével](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 alkalmazás Phi-3 mini-4k-instruct-onnx-szal](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 Többmodellű AI-meghajtású jegyzet alkalmazás minta](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Egyedi Phi-3 modellek finomhangolása és integrálása Prompt flow-val](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Egyedi Phi-3 modellek finomhangolása és integrálása Prompt flow-val az Azure AI Foundry-ban](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [A finomhangolt Phi-3 / Phi-3.5 modell értékelése az Azure AI Foundry-ban, különös tekintettel a Microsoft Felelős AI alapelveire](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct nyelv előrejelző minta (kínai/angol)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU használata Prompt flow megoldás létrehozásához Phi-3.5-Instruct ONNX-szal](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite használata Android alkalmazás készítéséhez](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Kérdések és válaszok .NET példa helyi ONNX Phi-3 modellel a Microsoft.ML.OnnxRuntime használatával](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Konzol chat .NET alkalmazás Semantic Kernel-lel és Phi-3-mal](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK kód alapú minták 
    - Phi-4 minták 🆕
      - [📓] [Projektkód generálása Phi-4-multimodal használatával](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 minták
      - [Saját Visual Studio Code GitHub Copilot Chat felépítése Microsoft Phi-3 családdal](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Saját Visual Studio Code Chat Copilot ügynök létrehozása Phi-3.5-tel GitHub modellekkel](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Fejlett érvelési minták
    - Phi-4 minták 🆕
      - [📓] [Phi-4-mini-érvelési vagy Phi-4-érvelési minták](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Phi-4-mini-érvelés finomhangolása Microsoft Olive-dal](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-érvelés finomhangolása Apple MLX-szel](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-érvelés GitHub modellekkel](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-érvelés Azure AI Foundry modellekkel](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Bemutatók
      - [Phi-4-mini demo az Hugging Face Spaces-en](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demo az Hugginge Face Spaces-en](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Látás minták
    - Phi-4 minták 🆕
      - [📓] [Phi-4-multimodal használata képek olvasására és kód generálására](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 minták
      -  [📓][Phi-3-látás-kép szöveg átalakítása szöveggé](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-látás-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-látás CLIP beágyazás](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 újrahasznosítás](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-látás - Vizualis nyelvi asszisztens - Phi3-Vision és OpenVINO használatával](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Látás Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Látás OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Látás több képkockás vagy több képes minta](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Látás helyi ONNX modell a Microsoft.ML.OnnxRuntime .NET használatával](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menü alapú Phi-3 Látás helyi ONNX modell a Microsoft.ML.OnnxRuntime .NET használatával](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Matematikai minták
    -  Phi-4-Mini-Flash-Reasoning-Instruct minták 🆕 [Matematikai demo Phi-4-Mini-Flash-Reasoning-Instruct használatával](./md/02.Application/09.Math/MathDemo.ipynb)

  - Hangminták
    - Phi-4 minták 🆕
      - [📓] [Hangátiratok kivonása Phi-4-multimodal segítségével](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal hangminta](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal beszédfordítási minta](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET konzolalkalmazás Phi-4-multimodal hangfájl elemzésére és átírás generálására](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MoE minták
    - Phi-3 / 3.5 minták
      - [📓] [Phi-3.5 Mixture of Experts modellek (MoEs) közösségi média minta](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Retrieval-Augmented Generation (RAG) csővezeték építése NVIDIA NIM Phi-3 MOE, Azure AI Search és LlamaIndex segítségével](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Függvényhívó minták
    - Phi-4 minták 🆕
      -  [📓] [Függvényhívás használata Phi-4-mini-vel](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Függvényhívással több ügynök létrehozása Phi-4-mini-vel](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Függvényhívás használata Ollama-val](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Függvényhívás használata ONNX-szal](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Többmodelles keverési minták
    - Phi-4 minták 🆕
      -  [📓] [Phi-4-multimodal használata technológiai újságíróként](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET konzolalkalmazás Phi-4-multimodal képelemzésre](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi finomhangolás minták
  - [Finomhangolási Szenáriók](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Finomhangolás vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Engedd, hogy a Phi-3 iparági szakértővé váljon](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Phi-3 finomhangolása AI Toolkit for VS Code-dal](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Phi-3 finomhangolása Azure Machine Learning Service-szel](./md/03.FineTuning/Introduce_AzureML.md)
  - [Phi-3 finomhangolása Lora-val](./md/03.FineTuning/FineTuning_Lora.md)
  - [Phi-3 finomhangolása QLora-val](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Phi-3 finomhangolása Azure AI Foundry-val](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Phi-3 finomhangolása Azure ML CLI/SDK-val](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Finomhangolás Microsoft Olive-dal](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive gyakorlati labor](./md/03.FineTuning/olive-lab/readme.md)
  - [Phi-3-látás finomhangolása Weights and Bias használatával](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Phi-3 finomhangolása Apple MLX Frameworkkel](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-látás finomhangolása (hivatalos támogatás)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Phi-3 finomhangolás Kaito AKS, Azure tárolók használatával (hivatalos támogatás)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 és 3.5 Látás finomhangolása](https://github.com/2U1/Phi3-Vision-Finetune)

- Gyakorlati labor
  - [Élvonalbeli modellek felfedezése: LLM-ek, SLM-ek, helyi fejlesztés és egyebek](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Az NLP lehetőségeinek kibontakoztatása: Finomhangolás Microsoft Olive-dal](https://github.com/azure/Ignite_FineTuning_workshop)

- Tudományos kutatási cikkek és kiadványok
  - [Tankönyvek minden, amire szükséged van II: phi-1.5 műszaki jelentés](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Műszaki Jelentés: Egy rendkívül képzett nyelvi modell helyileg a telefonodon](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Műszaki Jelentés](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Műszaki Jelentés: Kompakt, de erőteljes multimodális nyelvi modellek Mixture-of-LoRAs segítségével](https://arxiv.org/abs/2503.01743)
  - [Kis nyelvi modellek optimalizálása járművön belüli funkcióhíváshoz](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 finomhangolása feleletválasztós kérdésválaszoláshoz: Módszertan, eredmények és kihívások](https://arxiv.org/abs/2501.01588)
  - [Phi-4-érvelés Műszaki Jelentés](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-érvelés Műszaki Jelentés](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi modellek használata

### Phi az Azure AI Foundry-n

Megtanulhatod, hogyan használhatod a Microsoft Phi-t és hogyan építhetsz E2E megoldásokat különböző hardveres eszközeiden. Ahhoz, hogy saját magad is megtapasztald Phi-t, kezdd azzal, hogy játszol a modellekkel és testre szabod Phi-t a saját eseteidhez az [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) segítségével. További információkat megtalálhatsz az [Azure AI Foundry kezdőlépései](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) dokumentumban.

**Játszótér**
Minden modellhez tartozik egy dedikált játszótér a modell kipróbálásához [Azure AI Playground](https://aka.ms/try-phi3).

### Phi a GitHub Modelleken

Megtanulhatod, hogyan használhatod a Microsoft Phi-t és hogyan építhetsz E2E megoldásokat különböző hardveres eszközeiden. Ahhoz, hogy saját magad is megtapasztald Phi-t, kezdd azzal, hogy játszol a modellel, és testre szabod Phi-t a saját eseteidhez a [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) használatával. További információkat megtalálhatsz a [GitHub Model Catalog kezdőlépései](/md/02.QuickStart/GitHubModel_QuickStart.md) dokumentumban.

**Játszótér**
Minden modellhez tartozik egy dedikált [játszótér a modell kipróbálásához](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi a Hugging Face-en

A modellt megtalálhatod a [Hugging Face](https://huggingface.co/microsoft) oldalon is.

**Játszótér**  
[Hugging Chat játszótér](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 Egyéb tanfolyamok

Csapatunk más tanfolyamokat is kínál! Nézd meg:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j kezdőknek](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js kezdőknek](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Ügynökök
[![AZD kezdőknek](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI kezdőknek](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP kezdőknek](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Ügynökök kezdőknek](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Generatív AI sorozat
[![Generatív AI kezdőknek](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### Alapvető tanulás
[![ML kezdőknek](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Adattudomány kezdőknek](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI kezdőknek](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kiberbiztonság kezdőknek](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webfejlesztés kezdőknek](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT kezdőknek](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR fejlesztés kezdőknek](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Copilot sorozat
[![Copilot AI páros programozáshoz](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET-hez](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot kalandok](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Felelős MI

A Microsoft elkötelezett amellett, hogy ügyfeleink felelősségteljesen használhassák MI-termékeinket, megosztva tapasztalatainkat és bizalmon alapuló partnerségeket építve olyan eszközök révén, mint a Transzparencia jegyzetek és Hatásértékelések. Ezeknek az erőforrásoknak nagy része megtalálható a [https://aka.ms/RAI](https://aka.ms/RAI) címen.  
A Microsoft felelős MI-hez való megközelítése a méltányosság, megbízhatóság és biztonság, adatvédelem és biztonság, befogadás, átláthatóság és elszámoltathatóság elveire épül.

A nagy méretű, természetes nyelvi, kép- és beszédmodellek – mint az ebben a mintában használtak – potenciálisan méltánytalan, megbízhatatlan vagy sértő módon viselkedhetnek, ezáltal károkat okozva. Kérjük, tekintsd meg az [Azure OpenAI szolgáltatás transzparencia jegyzetét](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), hogy tájékozódj a kockázatokról és korlátokról.

A kockázatok csökkentésének ajánlott megközelítése egy biztonsági rendszer beépítése az architektúrába, amely képes észlelni és megakadályozni a káros viselkedést. Az [Azure AI Tartalombiztonság](https://learn.microsoft.com/azure/ai-services/content-safety/overview) egy független védelmi réteget biztosít, amely képes érzékelni a felhasználók által létrehozott és az MI által generált káros tartalmakat az alkalmazásokban és szolgáltatásokban. Az Azure AI Tartalombiztonság szöveg- és képi API-kat tartalmaz, amelyekkel észlelhetőek a káros anyagok. Az Azure AI Foundry-n belül a Tartalombiztonsági szolgáltatás lehetővé teszi, hogy megtekints, felfedezz és kipróbálj mintakódokat azokhoz a különböző modalitású káros tartalmak észlelésére. A következő [gyors kezdési dokumentáció](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) segít a szolgáltatás kérésének elkészítésében.

Fontos továbbá az alkalmazás általános teljesítménye. A multimodális és több modellből álló alkalmazások esetén a teljesítmény azt jelenti, hogy a rendszer úgy működik, ahogy te és a felhasználóid elvárják, beleértve, hogy ne generáljon káros kimeneteket. Fontos értékelni az alkalmazás teljesítményét a [Teljesítmény és minőség valamint Kockázat és biztonság értékelőkkel](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Emellett lehetőséged van [egyéni értékelők](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) létrehozására és értékelésére is.
Az AI alkalmazásodat kiértékelheted a fejlesztési környezetedben az [Azure AI értékelő SDK](https://microsoft.github.io/promptflow/index.html) segítségével. Adott egy teszt adatállomány vagy egy cél, a generatív AI alkalmazás generációit mennyiségileg mérik beépített vagy általad választott egyéni értékelők. Ha el szeretnéd kezdeni az azure ai értékelő sdk használatát a rendszered kiértékeléséhez, kövesd a [gyors kezdési útmutatót](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Miután végrehajtottad az értékelési futást, [meg is jelenítheted az eredményeket az Azure AI Foundry-ban](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Védjegyek

Ez a projekt tartalmazhat védjegyeket vagy logókat projektekhez, termékekhez vagy szolgáltatásokhoz. A Microsoft védjegyek vagy logók jogosult használata alá van vetve és be kell tartania a [Microsoft védjegy- és márkaarculati irányelveit](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
A Microsoft védjegyek vagy logók használata a projekt módosított változataiban nem okozhat zavart vagy nem sugallhatja a Microsoft szponzorálását. A harmadik féltől származó védjegyek vagy logók bármilyen használata a harmadik fél irányelveinek van alávetve.

## Segítségkérés

Ha elakadnál vagy kérdésed van az AI alkalmazások fejlesztésével kapcsolatban, csatlakozz:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Ha termék-visszajelzésed vagy hibák vannak fejlesztés közben, látogass el ide:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felelősség kizárása**:
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár igyekszünk a pontosságra, kérjük vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti, anyanyelvi dokumentum tekinthető hiteles forrásnak. Fontos információk esetén szakember általi humán fordítást javasolunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->