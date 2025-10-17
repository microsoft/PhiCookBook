<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4987daf30687ad3850757c9eae3f5411",
  "translation_date": "2025-10-17T10:39:49+00:00",
  "source_file": "README.md",
  "language_code": "sl"
}
-->
# Phi Cookbook: Praktični primeri z Microsoftovimi Phi modeli

Phi je serija odprtokodnih AI modelov, ki jih je razvil Microsoft.

Phi je trenutno najzmogljivejši in stroškovno najučinkovitejši majhen jezikovni model (SLM), ki dosega odlične rezultate pri večjezičnosti, sklepanju, generiranju besedil/klepeta, kodiranju, slikah, zvoku in drugih scenarijih.

Phi lahko namestite v oblak ali na robne naprave, prav tako pa lahko z omejenimi računalniškimi zmogljivostmi enostavno ustvarjate aplikacije generativne umetne inteligence.

Sledite tem korakom, da začnete uporabljati te vire:
1. **Forkajte repozitorij**: Kliknite [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Klonirajte repozitorij**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Pridružite se Microsoft AI Discord skupnosti in spoznajte strokovnjake ter druge razvijalce**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 Podpora za več jezikov

#### Podprto prek GitHub Action (Avtomatizirano in vedno posodobljeno)

[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](./README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

## Kazalo

- Uvod
  - [Dobrodošli v družini Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Nastavitev okolja](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Razumevanje ključnih tehnologij](./md/01.Introduction/01/01.Understandingtech.md)
  - [Varnost AI za modele Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Podpora za strojno opremo Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi modeli in razpoložljivost na različnih platformah](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Uporaba Guidance-ai in Phi](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace modeli](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- Inference Phi v različnih okoljih
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [GitHub modeli](./md/01.Introduction/02/02.GitHubModel.md)
    - [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Inference Phi družine
    - [Inference Phi v iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inference Phi v Androidu](./md/01.Introduction/03/Android_Inference.md)
    - [Inference Phi v Jetsonu](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inference Phi v AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inference Phi z Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Inference Phi na lokalnem strežniku](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inference Phi na oddaljenem strežniku z AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inference Phi z Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inference Phi--Vision lokalno](./md/01.Introduction/03/Vision_Inference.md)
    - [Inference Phi z Kaito AKS, Azure Containers (uradna podpora)](./md/01.Introduction/03/Kaito_Inference.md)
- [Kvantifikacija Phi družine](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Kvantifikacija Phi-3.5 / 4 z llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Kvantifikacija Phi-3.5 / 4 z generativnimi AI razširitvami za onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Kvantifikacija Phi-3.5 / 4 z Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Kvantifikacija Phi-3.5 / 4 z Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Evalvacija Phi
    - [Odgovorna AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry za evalvacijo](./md/01.Introduction/05/AIFoundry.md)
    - [Uporaba Promptflow za evalvacijo](./md/01.Introduction/05/Promptflow.md)

- RAG z Azure AI Search
    - [Kako uporabljati Phi-4-mini in Phi-4-multimodal (RAG) z Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Primeri razvoja aplikacij s Phi
  - Besedilne in klepetalne aplikacije
    - Phi-4 Primeri 🆕
      - [📓] [Klepet s Phi-4-mini ONNX modelom](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Klepet s Phi-4 lokalnim ONNX modelom .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Konzolna aplikacija za klepet .NET s Phi-4 ONNX z uporabo Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 Primeri
      - [Lokalni chatbot v brskalniku z uporabo Phi3, ONNX Runtime Web in WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino klepet](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - Interaktivni Phi-3-mini in OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Izdelava ovojnice in uporaba Phi-3 z MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Optimizacija modela - Kako optimizirati Phi-3-min model za ONNX Runtime Web z Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [WinUI3 aplikacija s Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [WinUI3 večmodelna AI aplikacija za zapiske](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Prilagoditev in integracija prilagojenih Phi-3 modelov s Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Prilagoditev in integracija prilagojenih Phi-3 modelov s Prompt flow v Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Ocena prilagojenega Phi-3 / Phi-3.5 modela v Azure AI Foundry s poudarkom na Microsoftovih načelih odgovorne AI](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct primer napovedovanja jezika (kitajščina/angleščina)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Uporaba Windows GPU za ustvarjanje Prompt flow rešitve s Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Uporaba Microsoft Phi-3.5 tflite za ustvarjanje Android aplikacije](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Q&A .NET primer z lokalnim ONNX Phi-3 modelom z uporabo Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Konzolna aplikacija za klepet .NET s Semantic Kernel in Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK vzorčne kode
  - Phi-4 vzorci 🆕
    - [📓] [Generiranje projektne kode z uporabo Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5 vzorci
    - [Ustvarite svoj Visual Studio Code GitHub Copilot Chat z Microsoft Phi-3 družino](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [Ustvarite svoj Visual Studio Code Chat Copilot Agent z Phi-3.5 z GitHub modeli](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- Napredni vzorci sklepanja
  - Phi-4 vzorci 🆕
    - [📓] [Phi-4-mini-reasoning ali Phi-4-reasoning vzorci](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Prilagoditev Phi-4-mini-reasoning z Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Prilagoditev Phi-4-mini-reasoning z Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning z GitHub modeli](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Phi-4-mini-reasoning z Azure AI Foundry modeli](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- Demos
    - [Phi-4-mini demoji na Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Phi-4-multimodal demoji na Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- Vzorci za vizijo
  - Phi-4 vzorci 🆕
    - [📓] [Uporaba Phi-4-multimodal za branje slik in generiranje kode](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Phi-3 / 3.5 vzorci
    - [📓][Phi-3-vision-Image besedilo v besedilo](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP vdelava](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [DEMO: Phi-3 recikliranje](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Vizualni jezikovni asistent - z Phi3-Vision in OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision večokvirni ali večslikovni vzorec](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Phi-3 Vision lokalni ONNX model z uporabo Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Meni temelječ Phi-3 Vision lokalni ONNX model z uporabo Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

- Vzorci za matematiko
  - Phi-4-Mini-Flash-Reasoning-Instruct vzorci 🆕 [Matematični demo z Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)

- Vzorci za zvok
  - Phi-4 vzorci 🆕
    - [📓] [Izvleček zvočnih prepisov z uporabo Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodal zvočni vzorec](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal vzorec za prevajanje govora](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET konzolna aplikacija z uporabo Phi-4-multimodal za analizo zvočne datoteke in generiranje prepisa](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- Vzorci MOE
  - Phi-3 / 3.5 vzorci
    - [📓] [Phi-3.5 MoE modeli (MoEs) vzorec za družbena omrežja](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [Izgradnja Retrieval-Augmented Generation (RAG) pipeline z NVIDIA NIM Phi-3 MOE, Azure AI Search in LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- Vzorci za klic funkcij
  - Phi-4 vzorci 🆕
    - [📓] [Uporaba klica funkcij s Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Uporaba klica funkcij za ustvarjanje več agentov s Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Uporaba klica funkcij z Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [Uporaba klica funkcij z ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- Vzorci za multimodalno mešanje
  - Phi-4 vzorci 🆕
    - [📓] [Uporaba Phi-4-multimodal kot tehnološki novinar](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET konzolna aplikacija z uporabo Phi-4-multimodal za analizo slik](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Prilagoditev Phi vzorcev
  - [Scenariji prilagoditve](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Prilagoditev vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Prilagoditev: Naj Phi-3 postane industrijski strokovnjak](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Prilagoditev Phi-3 z AI Toolkit za VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Prilagoditev Phi-3 z Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Prilagoditev Phi-3 z Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Prilagoditev Phi-3 z QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Prilagoditev Phi-3 z Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Prilagoditev Phi-3 z Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Prilagoditev z Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Prilagoditev z Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Prilagoditev Phi-3-vision z Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Prilagoditev Phi-3 z Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Prilagoditev Phi-3-vision (uradna podpora)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Prilagoditev Phi-3 z Kaito AKS, Azure Containers (uradna podpora)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Prilagoditev Phi-3 in 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands-on Lab
  - [Raziskovanje najsodobnejših modelov: LLMs, SLMs, lokalni razvoj in več](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Odklepanje NLP potenciala: Prilagoditev z Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Akademske raziskovalne publikacije
  - [Textbooks Are All You Need II: phi-1.5 tehnično poročilo](https://arxiv.org/abs/2309.05463)
  - [Phi-3 tehnično poročilo: Zelo zmogljiv jezikovni model lokalno na vašem telefonu](https://arxiv.org/abs/2404.14219)
  - [Phi-4 tehnično poročilo](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini tehnično poročilo: Kompaktni, a zmogljivi multimodalni jezikovni modeli prek Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Optimizacija majhnih jezikovnih modelov za klicanje funkcij v vozilu](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Fino prilagajanje PHI-3 za odgovarjanje na vprašanja z več izbirami: metodologija, rezultati in izzivi](https://arxiv.org/abs/2501.01588)
  - [Tehnično poročilo o razmišljanju Phi-4](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Tehnično poročilo o razmišljanju Phi-4-mini](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Uporaba modelov Phi

### Phi na Azure AI Foundry

Lahko se naučite, kako uporabljati Microsoft Phi in kako graditi E2E rešitve na različnih strojnih napravah. Da bi sami izkusili Phi, začnite z uporabo modelov in prilagodite Phi za svoje scenarije z [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Več informacij najdete v razdelku Začetek z [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Igralnica**
Vsak model ima namensko igralnico za testiranje modela [Azure AI Playground](https://aka.ms/try-phi3).

### Phi na GitHub Models

Lahko se naučite, kako uporabljati Microsoft Phi in kako graditi E2E rešitve na različnih strojnih napravah. Da bi sami izkusili Phi, začnite z uporabo modela in prilagodite Phi za svoje scenarije z [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Več informacij najdete v razdelku Začetek z [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Igralnica**
Vsak model ima namensko [igralnico za testiranje modela](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi na Hugging Face

Model lahko najdete tudi na [Hugging Face](https://huggingface.co/microsoft).

**Igralnica**
 [Hugging Chat igralnica](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct).

## Odgovorna umetna inteligenca 

Microsoft se zavezuje, da bo svojim strankam pomagal odgovorno uporabljati naše AI izdelke, delil svoje izkušnje in gradil partnerstva, ki temeljijo na zaupanju, z orodji, kot so Opombe o transparentnosti in Ocene vpliva. Veliko teh virov najdete na [https://aka.ms/RAI](https://aka.ms/RAI). 
Pristop Microsofta k odgovorni AI temelji na naših AI načelih pravičnosti, zanesljivosti in varnosti, zasebnosti in varnosti, vključenosti, transparentnosti in odgovornosti.

Veliki jezikovni, slikovni in govorni modeli - kot so tisti, uporabljeni v tem vzorcu - lahko potencialno delujejo na načine, ki so nepravični, nezanesljivi ali žaljivi, kar lahko povzroči škodo. Prosimo, da si ogledate [Opombo o transparentnosti storitve Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), da se seznanite z morebitnimi tveganji in omejitvami.

Priporočeni pristop za zmanjšanje teh tveganj je vključitev varnostnega sistema v vašo arhitekturo, ki lahko zazna in prepreči škodljivo vedenje. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) zagotavlja neodvisno zaščitno plast, ki lahko zazna škodljivo vsebino, ki jo ustvarijo uporabniki ali AI, v aplikacijah in storitvah. Azure AI Content Safety vključuje API-je za besedilo in slike, ki omogočajo zaznavanje škodljivega materiala. Znotraj Azure AI Foundry storitev Content Safety omogoča ogled, raziskovanje in preizkušanje vzorčne kode za zaznavanje škodljive vsebine v različnih modalnostih. Naslednja [dokumentacija za hiter začetek](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vas vodi skozi pošiljanje zahtevkov storitvi.

Drug vidik, ki ga je treba upoštevati, je splošna zmogljivost aplikacije. Pri večmodalnih in večmodelnih aplikacijah zmogljivost pomeni, da sistem deluje, kot vi in vaši uporabniki pričakujete, vključno s tem, da ne generira škodljivih rezultatov. Pomembno je oceniti zmogljivost vaše celotne aplikacije z uporabo [Ocenjevalcev zmogljivosti in kakovosti ter tveganja in varnosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Prav tako imate možnost ustvariti in oceniti z [lastnimi ocenjevalci](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Vašo AI aplikacijo lahko ocenite v vašem razvojnem okolju z uporabo [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Na podlagi testnega nabora podatkov ali cilja se generacije vaše generativne AI aplikacije kvantitativno merijo z vgrajenimi ocenjevalci ali lastnimi ocenjevalci po vaši izbiri. Za začetek z Azure AI Evaluation SDK za ocenjevanje vašega sistema lahko sledite [vodniku za hiter začetek](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Ko izvedete ocenjevalni postopek, lahko [vizualizirate rezultate v Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Blagovne znamke

Ta projekt lahko vsebuje blagovne znamke ali logotipe za projekte, izdelke ali storitve. Dovoljena uporaba blagovnih znamk ali logotipov Microsofta mora biti skladna z [Microsoftovimi smernicami za uporabo blagovnih znamk in logotipov](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Uporaba blagovnih znamk ali logotipov Microsofta v spremenjenih različicah tega projekta ne sme povzročiti zmede ali nakazovati sponzorstva s strani Microsofta. Vsaka uporaba blagovnih znamk ali logotipov tretjih oseb je predmet politik teh tretjih oseb.

## Pomoč

Če se zataknete ali imate kakršna koli vprašanja o gradnji AI aplikacij, se pridružite:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Če imate povratne informacije o izdelku ali napake med gradnjo, obiščite:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.