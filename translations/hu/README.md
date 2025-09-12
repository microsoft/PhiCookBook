<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T14:09:00+00:00",
  "source_file": "README.md",
  "language_code": "hu"
}
-->
# Phi Szakácskönyv: Gyakorlati példák a Microsoft Phi modellekkel

Phi a Microsoft által fejlesztett nyílt forráskódú AI modellek sorozata.

A Phi jelenleg a legerősebb és legköltséghatékonyabb kis nyelvi modell (SLM), amely kiváló eredményeket ér el többnyelvűség, érvelés, szöveg/chat generálás, kódolás, képek, hangok és más területeken.

A Phi telepíthető felhőbe vagy élő eszközökre, és könnyedén építhető generatív AI alkalmazások korlátozott számítási kapacitással.

Kövesse az alábbi lépéseket, hogy elkezdhesse használni ezeket az erőforrásokat:
1. **Forkolja a repót**: Kattintson [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Klónozza a repót**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Csatlakozzon a Microsoft AI Discord közösséghez, és találkozzon szakértőkkel és fejlesztőtársakkal**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 Többnyelvű támogatás

#### Támogatott GitHub Action által (Automatikus és mindig naprakész)

[Francia](../fr/README.md) | [Spanyol](../es/README.md) | [Német](../de/README.md) | [Orosz](../ru/README.md) | [Arab](../ar/README.md) | [Perzsa (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Kínai (Egyszerűsített)](../zh/README.md) | [Kínai (Hagyományos, Makaó)](../mo/README.md) | [Kínai (Hagyományos, Hongkong)](../hk/README.md) | [Kínai (Hagyományos, Tajvan)](../tw/README.md) | [Japán](../ja/README.md) | [Koreai](../ko/README.md) | [Hindi](../hi/README.md) 
[Bengáli](../bn/README.md) | [Marathi](../mr/README.md) | [Nepáli](../ne/README.md) | [Pandzsábi (Gurmukhi)](../pa/README.md) | [Portugál (Portugália)](../pt/README.md) | [Portugál (Brazília)](../br/README.md) | [Olasz](../it/README.md) | [Lengyel](../pl/README.md) | [Török](../tr/README.md) | [Görög](../el/README.md) | [Thai](../th/README.md) | [Svéd](../sv/README.md) | [Dán](../da/README.md) | [Norvég](../no/README.md) | [Finn](../fi/README.md) | [Holland](../nl/README.md) | [Héber](../he/README.md) | [Vietnámi](../vi/README.md) | [Indonéz](../id/README.md) | [Maláj](../ms/README.md) | [Tagalog (Filippínó)](../tl/README.md) | [Szuahéli](../sw/README.md) | [Magyar](./README.md) | [Cseh](../cs/README.md) | [Szlovák](../sk/README.md) | [Román](../ro/README.md) | [Bolgár](../bg/README.md) | [Szerb (Cirill)](../sr/README.md) | [Horvát](../hr/README.md) | [Szlovén](../sl/README.md)

## Tartalomjegyzék

- Bevezetés
  - [Üdvözöljük a Phi családban](./md/01.Introduction/01/01.PhiFamily.md)
  - [Környezet beállítása](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Kulcstechnológiák megértése](./md/01.Introduction/01/01.Understandingtech.md)
  - [AI biztonság a Phi modellekhez](./md/01.Introduction/01/01.AISafety.md)
  - [Phi hardvertámogatás](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi modellek és elérhetőség különböző platformokon](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai és Phi használata](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace modellek](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- Phi futtatása különböző környezetekben
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [GitHub modellek](./md/01.Introduction/02/02.GitHubModel.md)
    - [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi család futtatása
    - [Phi futtatása iOS-en](./md/01.Introduction/03/iOS_Inference.md)
    - [Phi futtatása Androidon](./md/01.Introduction/03/Android_Inference.md)
    - [Phi futtatása Jetsonon](./md/01.Introduction/03/Jetson_Inference.md)
    - [Phi futtatása AI PC-n](./md/01.Introduction/03/AIPC_Inference.md)
    - [Phi futtatása Apple MLX Frameworkkel](./md/01.Introduction/03/MLX_Inference.md)
    - [Phi futtatása helyi szerveren](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Phi futtatása távoli szerveren AI Toolkit segítségével](./md/01.Introduction/03/Remote_Interence.md)
    - [Phi futtatása Rusttal](./md/01.Introduction/03/Rust_Inference.md)
    - [Phi--Vision futtatása helyben](./md/01.Introduction/03/Vision_Inference.md)
    - [Phi futtatása Kaito AKS, Azure Containers (hivatalos támogatás)](./md/01.Introduction/03/Kaito_Inference.md)

- [Phi család kvantálása](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantálása llama.cpp segítségével](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantálása generatív AI kiterjesztésekkel onnxruntime-hoz](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantálása Intel OpenVINO-val](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantálása Apple MLX Frameworkkel](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi értékelése
    - [Felelős AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry értékeléshez](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow használata értékeléshez](./md/01.Introduction/05/Promptflow.md)

- RAG az Azure AI Search segítségével
    - [Hogyan használjuk Phi-4-mini és Phi-4-multimodal (RAG) modelleket az Azure AI Search-csel](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi alkalmazásfejlesztési minták
  - Szöveg és chat alkalmazások
    - Phi-4 minták 🆕
      - [📓] [Chat Phi-4-mini ONNX modellel](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat Phi-4 helyi ONNX modellel .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Chat .NET konzol alkalmazás Phi-4 ONNX modellel Szemantikus Kernel használatával](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 minták
      - [Helyi chatbot a böngészőben Phi3, ONNX Runtime Web és WebGPU használatával](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Több modell - Interaktív Phi-3-mini és OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Wrapper építése és Phi-3 használata MLFlow-val](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Modell optimalizálás - Hogyan optimalizáljuk a Phi-3-min modellt ONNX Runtime Webhez Olive segítségével](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 alkalmazás Phi-3 mini-4k-instruct-onnx modellel](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3 Több Modell AI által támogatott jegyzetek alkalmazás minta](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Egyedi Phi-3 modellek finomhangolása és integrálása Prompt flow-val](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Egyedi Phi-3 modellek finomhangolása és integrálása Prompt flow-val az Azure AI Foundry-ban](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Finomhangolt Phi-3 / Phi-3.5 modellek értékelése az Azure AI Foundry-ban, a Microsoft Felelős AI alapelveire összpontosítva](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct nyelvi predikciós minta (kínai/angol)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU használata Prompt flow megoldás létrehozásához Phi-3.5-Instruct ONNX-szel](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tflite használata Android alkalmazás létrehozásához](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Kérdések és válaszok .NET példa helyi ONNX Phi-3 modellel a Microsoft.ML.OnnxRuntime használatával](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Konzolos chat .NET alkalmazás Szemantikus Kernel és Phi-3 használatával](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK kód alapú minták 
  - Phi-4 minták 🆕
    - [📓] [Projektkód generálása Phi-4-multimodal használatával](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5 minták
    - [Visual Studio Code GitHub Copilot Chat létrehozása a Microsoft Phi-3 családdal](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [Visual Studio Code Chat Copilot Agent létrehozása Phi-3.5-tel GitHub modellek használatával](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- Haladó érvelési minták
  - Phi-4 minták 🆕
    - [📓] [Phi-4-mini-reasoning vagy Phi-4-reasoning minták](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Phi-4-mini-reasoning finomhangolása Microsoft Olive-val](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning finomhangolása Apple MLX-szel](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning GitHub modellekkel](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Phi-4-mini-reasoning Azure AI Foundry modellekkel](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- Demók
    - [Phi-4-mini demók a Hugging Face Spaces-en](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Phi-4-multimodal demók a Hugging Face Spaces-en](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- Vizuális minták
  - Phi-4 minták 🆕
    - [📓] [Phi-4-multimodal használata képek olvasására és kód generálására](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Phi-3 / 3.5 minták
    - [📓][Phi-3-vision-Kép szövegből szövegbe](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP beágyazás](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [DEMO: Phi-3 Újrahasznosítás](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Vizuális nyelvi asszisztens - Phi3-Vision és OpenVINO használatával](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision több képkocka vagy több kép minta](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Phi-3 Vision helyi ONNX modell a Microsoft.ML.OnnxRuntime .NET használatával](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Menü alapú Phi-3 Vision helyi ONNX modell a Microsoft.ML.OnnxRuntime .NET használatával](../../md/04.HOL/dotnet/src/LabsPhi304)

- Matematikai minták
  - Phi-4-Mini-Flash-Reasoning-Instruct minták 🆕 [Matematikai demó Phi-4-Mini-Flash-Reasoning-Instruct használatával](../../md/02.Application/09.Math/MathDemo.ipynb)

- Audio minták
  - Phi-4 minták 🆕
    - [📓] [Audio átiratok kinyerése Phi-4-multimodal használatával](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodal audio minta](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal beszéd fordítási minta](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET konzolos alkalmazás Phi-4-multimodal használatával audio fájl elemzésére és átirat generálására](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOE minták
  - Phi-3 / 3.5 minták
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) közösségi média minta](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [Retrieval-Augmented Generation (RAG) pipeline építése NVIDIA NIM Phi-3 MOE, Azure AI Search és LlamaIndex használatával](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- Funkcióhívási minták
  - Phi-4 minták 🆕
    - [📓] [Funkcióhívás használata Phi-4-mini-vel](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Funkcióhívás használata több ügynök létrehozásához Phi-4-mini-vel](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Funkcióhívás használata Ollama-val](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [Funkcióhívás használata ONNX-szel](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- Multimodális keverési minták
  - Phi-4 minták 🆕
    - [📓] [Phi-4-multimodal használata technológiai újságíróként](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET konzolos alkalmazás Phi-4-multimodal használatával képek elemzésére](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi finomhangolási minták
  - [Finomhangolási forgatókönyvek](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Finomhangolás vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Finomhangolás: Phi-3 ipari szakértővé válik](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Phi-3 finomhangolása AI Toolkit for VS Code használatával](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Phi-3 finomhangolása Azure Machine Learning Service használatával](./md/03.FineTuning/Introduce_AzureML.md)
  - [Phi-3 finomhangolása Lora-val](./md/03.FineTuning/FineTuning_Lora.md)
  - [Phi-3 finomhangolása QLora-val](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Phi-3 finomhangolása Azure AI Foundry-val](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Phi-3 finomhangolása Azure ML CLI/SDK-val](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Finomhangolás Microsoft Olive-val](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Finomhangolás Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Phi-3-vision finomhangolása Weights and Bias használatával](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Phi-3 finomhangolása Apple MLX Framework használatával](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision finomhangolása (hivatalos támogatás)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Phi-3 finomhangolása Kaito AKS, Azure Containers használatával (hivatalos támogatás)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 és 3.5 Vision finomhangolása](https://github.com/2U1/Phi3-Vision-Finetune)

- Gyakorlati labor
  - [Legmodernebb modellek felfedezése: LLM-ek, SLM-ek, helyi fejlesztés és egyebek](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP potenciál felszabadítása: Finomhangolás Microsoft Olive-val](https://github.com/azure/Ignite_FineTuning_workshop)

- Tudományos kutatási cikkek és publikációk
  - [Textbooks Are All You Need II: phi-1.5 technikai jelentés](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Technikai Jelentés: Egy rendkívül képes nyelvi modell helyben a telefonodon](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Technikai Jelentés](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Technikai Jelentés: Kompakt, de erőteljes multimodális nyelvi modellek Mixture-of-LoRAs használatával](https://arxiv.org/abs/2503.01743)
  - [Kis nyelvi modellek optimalizálása járműben történő funkcióhíváshoz](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 finomhangolása többválasztásos kérdés-válaszra: Módszertan, eredmények és kihívások](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning Technikai Jelentés](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning Technikai Jelentés](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)  

## Phi modellek használata  

### Phi az Azure AI Foundry-n  

Megtanulhatod, hogyan használd a Microsoft Phi-t, és hogyan építs E2E megoldásokat különböző hardvereszközeiden. Ha szeretnéd kipróbálni a Phi-t, kezdj a modellek tesztelésével, és testreszabhatod a Phi-t saját forgatókönyveidhez az [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) segítségével. További információt a [Azure AI Foundry Kezdő lépések](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) oldalon találsz.  

**Játszótér**  
Minden modellhez tartozik egy dedikált játszótér a modell teszteléséhez: [Azure AI Playground](https://aka.ms/try-phi3).  

### Phi a GitHub Modellek között  

Megtanulhatod, hogyan használd a Microsoft Phi-t, és hogyan építs E2E megoldásokat különböző hardvereszközeiden. Ha szeretnéd kipróbálni a Phi-t, kezdj a modellek tesztelésével, és testreszabhatod a Phi-t saját forgatókönyveidhez a [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) segítségével. További információt a [GitHub Model Catalog Kezdő lépések](/md/02.QuickStart/GitHubModel_QuickStart.md) oldalon találsz.  

**Játszótér**  
Minden modellhez tartozik egy dedikált [játszótér a modell teszteléséhez](/md/02.QuickStart/GitHubModel_QuickStart.md).  

### Phi a Hugging Face-en  

A modellt megtalálhatod a [Hugging Face](https://huggingface.co/microsoft) platformon is.  

**Játszótér**  
[Hugging Chat játszótér](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)  

## Felelős AI  

A Microsoft elkötelezett amellett, hogy segítse ügyfeleit AI termékeink felelős használatában, megossza tapasztalatait, és bizalmon alapuló partnerségeket építsen olyan eszközök révén, mint a Transparency Notes és az Impact Assessments. Ezeknek az erőforrásoknak egy része megtalálható itt: [https://aka.ms/RAI](https://aka.ms/RAI).  
A Microsoft felelős AI megközelítése az AI alapelveinkre épül: méltányosság, megbízhatóság és biztonság, adatvédelem és biztonság, befogadás, átláthatóság és elszámoltathatóság.  

A nagyméretű természetes nyelvi, képi és beszédmodellek - mint amilyeneket ebben a mintában használnak - potenciálisan igazságtalan, megbízhatatlan vagy sértő módon viselkedhetnek, ami károkat okozhat. Kérjük, olvasd el az [Azure OpenAI szolgáltatás átláthatósági jegyzetét](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), hogy tájékozódj a kockázatokról és korlátokról.  

A kockázatok mérséklésének ajánlott megközelítése egy biztonsági rendszer beépítése az architektúrába, amely képes felismerni és megelőzni a káros viselkedést. Az [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) egy független védelmi réteget biztosít, amely képes felismerni a felhasználók által generált és AI által generált káros tartalmakat alkalmazásokban és szolgáltatásokban. Az Azure AI Content Safety szöveg- és kép-API-kat tartalmaz, amelyek lehetővé teszik a káros anyagok felismerését. Az Azure AI Foundry-n belül a Content Safety szolgáltatás lehetővé teszi, hogy megtekintsd, felfedezd és kipróbáld a káros tartalom felismerésére szolgáló mintakódokat különböző modalitásokban. Az alábbi [gyorsindítási dokumentáció](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) végigvezet a szolgáltatásra vonatkozó kérések elkészítésén.  

Egy másik szempont, amelyet figyelembe kell venni, az alkalmazás teljesítménye. Többmodalitású és többmodellű alkalmazások esetén a teljesítmény azt jelenti, hogy a rendszer úgy működik, ahogy te és a felhasználóid elvárják, beleértve azt is, hogy nem generál káros kimeneteket. Fontos, hogy értékeld az alkalmazásod teljesítményét az [Teljesítmény és Minőség, valamint Kockázat és Biztonság értékelők](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) segítségével. Lehetőséged van saját [egyedi értékelők](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) létrehozására és értékelésére is.  

AI alkalmazásodat fejlesztési környezetben értékelheted az [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) segítségével. Akár egy tesztadatkészletet, akár egy célt adsz meg, generatív AI alkalmazásod kimeneteit mennyiségileg mérheted beépített vagy saját választású egyedi értékelőkkel. Az Azure AI Evaluation SDK-val való kezdéshez, hogy értékeld a rendszeredet, kövesd a [gyorsindítási útmutatót](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Miután végrehajtottál egy értékelési futtatást, [vizualizálhatod az eredményeket az Azure AI Foundry-ban](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).  

## Védjegyek  

Ez a projekt tartalmazhat védjegyeket vagy logókat projektekhez, termékekhez vagy szolgáltatásokhoz. A Microsoft védjegyek vagy logók engedélyezett használata a [Microsoft Védjegy és Márka Irányelvek](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) betartásának függvénye.  
A Microsoft védjegyek vagy logók módosított verzióinak használata nem okozhat zavart, és nem sugallhatja a Microsoft támogatását. Harmadik fél védjegyeinek vagy logóinak használata az adott harmadik fél irányelveinek hatálya alá tartozik.  

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.