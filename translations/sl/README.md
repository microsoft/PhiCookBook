# Phi Kuharska Knjiga: Praktični primeri z Microsoftovimi Phi modeli

[![Odpri in uporabljaj vzorce v GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Odpri v Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub sodelavci](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub težave](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub zahteve za pull](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR dobrodošli](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub gledalci](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub vilice](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub zvezdice](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi je serija odprtokodnih AI modelov, ki jih je razvilo Microsoft.

Phi je trenutno najmočnejši in stroškovno najučinkovitejši majhen jezikovni model (SLM), z zelo dobrimi rezultati v večjezičnosti, sklepanju, generiranju besedil/pogovorov, programiranju, slikah, zvoku in drugih scenarijih.

Phi lahko namestite v oblak ali na robne naprave, in lahko enostavno ustvarjate generativne AI aplikacije z omejeno računalniško močjo.

Sledite tem korakom, da začnete uporabljati ta vir:
1. **Razveji repozitorij**: Klikni [![GitHub vilice](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Kloniraj repozitorij**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Pridruži se Microsoft AI Discord skupnosti in spoznaj strokovnjake ter druge razvijalce**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/sl/cover.eb18d1b9605d754b.webp)

### 🌐 Večjezična Podpora

#### Podprto preko GitHub Action (avtomatsko in vedno posodobljeno)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabščina](../ar/README.md) | [Bengalščina](../bn/README.md) | [Bolgarščina](../bg/README.md) | [Burmanski (Myanmar)](../my/README.md) | [Kitajščina (poenostavljena)](../zh-CN/README.md) | [Kitajščina (tradicionalna, Hong Kong)](../zh-HK/README.md) | [Kitajščina (tradicionalna, Macau)](../zh-MO/README.md) | [Kitajščina (tradicionalna, Taiwan)](../zh-TW/README.md) | [Hrvaščina](../hr/README.md) | [Češčina](../cs/README.md) | [Danska](../da/README.md) | [Nizozemščina](../nl/README.md) | [Estonščina](../et/README.md) | [Finščina](../fi/README.md) | [Francosko](../fr/README.md) | [Nemščina](../de/README.md) | [Grščina](../el/README.md) | [Hebrejščina](../he/README.md) | [Hindujščina](../hi/README.md) | [Madžarščina](../hu/README.md) | [Indonezijščina](../id/README.md) | [Italijanščina](../it/README.md) | [Japonščina](../ja/README.md) | [Kannada](../kn/README.md) | [Korejščina](../ko/README.md) | [Litovščina](../lt/README.md) | [Malezijščina](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalščina](../ne/README.md) | [Nigerijska Pidgin](../pcm/README.md) | [Norveščina](../no/README.md) | [Perzijščina (Farsi)](../fa/README.md) | [Poljščina](../pl/README.md) | [Portugalščina (Brazilija)](../pt-BR/README.md) | [Portugalščina (Portugalska)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romunščina](../ro/README.md) | [Ruščina](../ru/README.md) | [Srbščina (cirilica)](../sr/README.md) | [Slovaščina](../sk/README.md) | [Slovenščina](./README.md) | [Španščina](../es/README.md) | [Svaheli](../sw/README.md) | [Švedščina](../sv/README.md) | [Tagalog (Filipinsko)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Tajščina](../th/README.md) | [Turščina](../tr/README.md) | [Ukrajinščina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamščina](../vi/README.md)

> **Raje lokalno kloniraš?**
>
> Ta repozitorij vključuje več kot 50 jezikovnih prevodov, kar precej poveča velikost prenosa. Za kloniranje brez prevodov uporabi sparse checkout:
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
> Tako pridobiš vse, kar potrebuješ za dokončanje tečaja z veliko hitrejšim prenosom.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Kazalo vsebine

- Uvod
  - [Dobrodošli v Phi družino](./md/01.Introduction/01/01.PhiFamily.md)
  - [Nastavitev okolja](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Razumevanje ključnih tehnologij](./md/01.Introduction/01/01.Understandingtech.md)
  - [Varnost AI za Phi modele](./md/01.Introduction/01/01.AISafety.md)
  - [Podpora za Phi strojno opremo](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi modeli in razpoložljivost na različnih platformah](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Uporaba Guidance-ai in Phi](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace modeli](https://github.com/marketplace/models)
  - [Azure AI kataloški modeli](https://ai.azure.com)

- Inferenca Phi v različnih okoljih
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub modeli](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry katalog modelov](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Inferenca Phi družine
    - [Inferenca Phi na iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inferenca Phi na Androidu](./md/01.Introduction/03/Android_Inference.md)
    - [Inferenca Phi na Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inferenca Phi na AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inferenca Phi z Apple MLX okvirjem](./md/01.Introduction/03/MLX_Inference.md)
    - [Inferenca Phi na lokalnem strežniku](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inferenca Phi na oddaljenem strežniku z uporabo AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inferenca Phi z Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inferenca Phi--Vision lokalno](./md/01.Introduction/03/Vision_Inference.md)
    - [Inferenca Phi z Kaito AKS, Azure Containers (uradna podpora)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Kvantiﬁkacija Phi družine](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Kvantiﬁkacija Phi-3.5 / 4 z llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Kvantiﬁkacija Phi-3.5 / 4 z Generative AI razširitvami za onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Kvantiﬁkacija Phi-3.5 / 4 z Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Kvantiﬁkacija Phi-3.5 / 4 z Apple MLX okvirjem](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Evaluacija Phi
    - [Odgovorna AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry za evalvacijo](./md/01.Introduction/05/AIFoundry.md)
    - [Uporaba Promptflow za evalvacijo](./md/01.Introduction/05/Promptflow.md)
 
- RAG z Azure AI Search
    - [Kako uporabljati Phi-4-mini in Phi-4-multimodal (RAG) z Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Vzorci za razvoj aplikacij Phi
  - Besedilne in pogovorne aplikacije
    - Phi-4 Vzorci 🆕
      - [📓] [Pogovor s Phi-4-mini ONNX modelom](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Pogovor z Phi-4 lokalnim ONNX Modelom .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Pogovorna .NET konzolna aplikacija s Phi-4 ONNX z uporabo Sementic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 Vzorci
      - [Lokalni klepetalnik v brskalniku z uporabo Phi3, ONNX Runtime Web in WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Več modelov - interaktivni Phi-3-mini in OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - izdelava ovojnice in uporaba Phi-3 z MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Optimizacija modela - Kako optimizirati model Phi-3-mini za ONNX Runtime Web z Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 aplikacija s Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [Vzorec WinUI3 aplikacije z več modeli, ki jih poganja AI](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Natančno nastavljanje in integracija prilagojenih Phi-3 modelov s Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Natančno nastavljanje in integracija prilagojenih Phi-3 modelov s Prompt flow v Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Ocena natančno nastavljenega modela Phi-3 / Phi-3.5 v Azure AI Foundry s poudarkom na Microsoftovih načelih odgovorne AI](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Vzorec jezikovne napovedi Phi-3.5-mini-instruct (kitajski/angleški)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Uporaba Windows GPU za ustvarjanje rešitve Prompt flow s Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Uporaba Microsoft Phi-3.5 tflite za ustvarjanje Android aplikacije](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET primer z lokalnim ONNX Phi-3 modelom z uporabo Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Konzolna chat .NET aplikacija z Semantic Kernel in Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK primeri na osnovi kode
    - Phi-4 primeri 🆕
      - [📓] [Generiraj kodo projekta z uporabo Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 primeri
      - [Izdelajte svoj Visual Studio Code GitHub Copilot Chat s Microsoft Phi-3 družino](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Ustvarite svojega Visual Studio Code Chat Copilot agenta s Phi-3.5 po modelih GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Napredni vzorci sklepanja
    - Phi-4 primeri 🆕
      - [📓] [Phi-4-mini-reasoning ali Phi-4-reasoning primeri](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Natančno nastavljanje Phi-4-mini-reasoning z Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Natančno nastavljanje Phi-4-mini-reasoning z Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning z GitHub modeli](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-reasoning z Azure AI Foundry modeli](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demos
      - [Phi-4-mini demoji gostovani na Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demoji gostovani na Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Vidni vzorci
    - Phi-4 primeri 🆕
      - [📓] [Uporabite Phi-4-multimodal za branje slik in generiranje kode](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 primeri
      -  [📓][Phi-3-vision-Slika besedilo v besedilo](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP vdelava](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 recikliranje](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - vizualni jezikovni pomočnik - s Phi3-Vision in OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 vizija Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 vizija OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 vizija več okvirjev ali več slik vzorec](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 vizija lokalni ONNX model z uporabo Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Meni na osnovi Phi-3 vizija lokalnega ONNX modela z uporabo Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Matematični vzorci
    -  Phi-4-Mini-Flash-Reasoning-Instruct primeri 🆕 [Matematični demo s Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - Zvočni vzorci
    - Phi-4 primeri 🆕
      - [📓] [Izvleček zvočnih prepisov z uporabo Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal zvočni primer](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal vzorec za prevajanje govora](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET konzolna aplikacija z uporabo Phi-4-multimodal za analizo zvočne datoteke in izdelavo prepisa](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE vzorci
    - Phi-3 / 3.5 primeri
      - [📓] [Phi-3.5 Mešanice strokovnjakov modeli (MoEs) vzorec za družbena omrežja](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Izdelava Retrieval-Augmented Generation (RAG) cevi z NVIDIA NIM Phi-3 MOE, Azure AI Search in LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Primeri klicev funkcij
    - Phi-4 primeri 🆕
      -  [📓] [Uporaba klicev funkcij s Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Uporaba klicev funkcij za ustvarjanje večagentov s Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Uporaba klicev funkcij z Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Uporaba klicev funkcij z ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Primeri mešanja multimodalnosti
    - Phi-4 primeri 🆕
      -  [📓] [Uporaba Phi-4-multimodal kot tehnološki novinar](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET konzolna aplikacija za analizo slik z uporabo Phi-4-multimodal](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Natančno nastavljanje Phi vzorcev
  - [Scenariji natančnega nastavljanja](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Natančno nastavljanje v primerjavi z RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Naj Phi-3 postane industrijski strokovnjak](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Natančno nastavljanje Phi-3 z AI orodjem za VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Natančno nastavljanje Phi-3 z Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Natančno nastavljanje Phi-3 z Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Natančno nastavljanje Phi-3 z QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Natančno nastavljanje Phi-3 z Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Natančno nastavljanje Phi-3 z Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Natančno nastavljanje z Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Natančno nastavljanje z Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Natančno nastavljanje Phi-3-vision z Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Natančno nastavljanje Phi-3 z Apple MLX okvirjem](./md/03.FineTuning/FineTuning_MLX.md)
  - [Natančno nastavljanje Phi-3-vision (uradna podpora)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Natančno nastavljanje Phi-3 s Kaito AKS, Azure Containers (uradna podpora)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Natančno nastavljanje Phi-3 in 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Praktična delavnica
  - [Raziskovanje najsodobnejših modelov: LLM, SLM, lokalni razvoj in še več](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Odklepanje potenciala NLP: natančno nastavljanje z Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)
- Akademske raziskovalne naloge in publikacije
  - [Učbeniki so vse, kar potrebujete II: tehnično poročilo phi-1.5](https://arxiv.org/abs/2309.05463)
  - [Tehnično poročilo Phi-3: zelo zmogljiv jezikovni model lokalno na vašem telefonu](https://arxiv.org/abs/2404.14219)
  - [Tehnično poročilo Phi-4](https://arxiv.org/abs/2412.08905)
  - [Tehnično poročilo Phi-4-Mini: kompaktni a močni multimodalni jezikovni modeli preko mešanice LoRA](https://arxiv.org/abs/2503.01743)
  - [Optimizacija majhnih jezikovnih modelov za klicanje funkcij v vozilu](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Fine-tuning PHI-3 za večkratno izbiro odgovora: metodologija, rezultati in izzivi](https://arxiv.org/abs/2501.01588)
  - [Tehnično poročilo Phi-4-razmišljanje](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Tehnično poročilo Phi-4-mini-razmišljanje](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Uporaba modelov Phi

### Phi na Azure AI Foundry

Lahko se naučite, kako uporabljati Microsoft Phi ter kako graditi E2E rešitve na različnih strojnih napravah. Da Phi sami preizkusite, začnite z igranjem z modeli in prilagajanjem Phi za vaše scenarije z uporabo [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Več lahko izveste v Pričetek uporabe z [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Igralnica**
Vsak model ima svojo igralnico za testiranje modela [Azure AI Playground](https://aka.ms/try-phi3).

### Phi na GitHub modelih

Lahko se naučite, kako uporabljati Microsoft Phi ter kako graditi E2E rešitve na različnih strojnih napravah. Da Phi sami preizkusite, začnite z igranjem z modelom in prilagajanjem Phi za vaše scenarije z uporabo [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Več lahko izveste v Pričetek uporabe z [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Igralnica**
Vsak model ima namensko [igralnico za testiranje modela](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi na Hugging Face

Model lahko najdete tudi na [Hugging Face](https://huggingface.co/microsoft)

**Igralnica**
 [Hugging Chat igralnica](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 Drugi tečaji

Naša skupina pripravlja tudi druge tečaje! Oglejte si:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j za začetnike](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js za začetnike](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain za začetnike](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agentje
[![AZD za začetnike](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI za začetnike](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP za začetnike](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI agenti za začetnike](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serija generativne AI
[![Generativna AI za začetnike](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativna AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativna AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativna AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Osnovno učenje
[![ML za začetnike](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Podatkovna znanost za začetnike](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI za začetnike](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kibernetska varnost za začetnike](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Razvoj spletnih strani za začetnike](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT za začetnike](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR razvoj za začetnike](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serija Copilot
[![Copilot za AI programiranje v paru](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot za C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot avantura](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Odgovorna umetna inteligenca

Microsoft se zavezuje, da bo pomagal svojim strankam odgovorno uporabljati naše izdelke umetne inteligence, deliti naše izkušnje in graditi partnerske odnose, ki temeljijo na zaupanju, preko orodij, kot so opombe o preglednosti in ocenah vpliva. Veliko teh virov lahko najdete na [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoftov pristop k odgovorni umetni inteligenci temelji na naših načelih umetne inteligence o pravičnosti, zanesljivosti in varnosti, zasebnosti in varnosti, vključevanju, preglednosti in odgovornosti.

Veliki naravni jezikovni, slikovni in govorni modeli — kot so tisti, uporabljeni v tem vzorcu — se lahko vedenjsko kažejo na načine, ki so nepravični, nezanesljivi ali žaljivi, kar lahko povzroči škodo. Prosimo, preberite [Azure OpenAI storitve opombo o preglednosti](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), da se seznanite z tveganji in omejitvami.

Priporočeni pristop za ublažitev teh tveganj je vključitev varnostnega sistema v vašo arhitekturo, ki lahko zazna in prepreči škodljivo vedenje. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) nudi neodvisno zaščitno plast, ki lahko zazna škodljivo vsebino, ustvarjeno s strani uporabnikov ali umetne inteligence, v aplikacijah in storitvah. Azure AI Content Safety vključuje API-je besedila in slik, ki vam omogočajo zaznavanje škodljivega gradiva. Znotraj Azure AI Foundry storitev Content Safety omogoča ogled, raziskovanje in preizkušanje vzorčnih kod za zaznavanje škodljive vsebine v različnih modalnostih. Naslednja [dokumentacija za hitro začetek](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vas vodi skozi poizvedbe na storitev.
Drugi vidik, ki ga je treba upoštevati, je splošna zmogljivost aplikacije. Pri aplikacijah z večmodalnimi in večmodelnimi pristopi zmogljivost razumemo kot to, da sistem deluje tako, kot pričakujete vi in vaši uporabniki, vključno s tem, da ne generira škodljivih izhodov. Pomembno je oceniti zmogljivost vaše celotne aplikacije z uporabo [ocenjevalcev zmogljivosti, kakovosti, tveganja in varnosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Prav tako imate možnost ustvariti in oceniti z [lastnimi ocenjevalci](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Svoje AI aplikacije lahko ocenjujete v razvojnem okolju z uporabo [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Na podlagi testne podatkovne množice ali cilja se generacije vaše generativne AI aplikacije kvantitativno merijo z vgrajenimi ocenjevalci ali ocenjevalci po meri, ki jih izberete. Za začetek uporabe azure ai evaluation sdk za ocenjevanje vašega sistema sledite [vodniku za hitro začetek](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Ko izvedete ocenjevalno izvedbo, lahko [vizualizirate rezultate v Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Znamke

Ta projekt lahko vsebuje blagovne znamke ali logotipe projektov, izdelkov ali storitev. Pooblaščena uporaba Microsoftovih blagovnih znamk ali logotipov je predmet in mora slediti [Microsoftovim smernicam za blagovne znamke in znamčenje](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Uporaba Microsoftovih blagovnih znamk ali logotipov v spremenjenih različicah tega projekta ne sme povzročati zmede ali nakazovati sponzorstva Microsofta. Vsakršna uporaba blagovnih znamk ali logotipov tretjih oseb je predmet pravil teh tretjih oseb.

## Iskanje pomoči

Če se zataknete ali imate kakršnakoli vprašanja o gradnji AI aplikacij, se pridružite:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Če imate povratne informacije o izdelku ali napake med gradnjo, obiščite:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko samodejni prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitna nerazumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->