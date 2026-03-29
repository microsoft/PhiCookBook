# Phi Raamatukogu: Praktilised näited Microsofti Phi mudelitega

[![Ava ja kasuta näidiseid GitHub Codespaces-is](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Ava Dev Containers-is](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub kaastöötajad](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub probleemid](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-päringud](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR-d on teretulnud](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub jälgijad](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forkid](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub tähed](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi on Microsofti välja töötatud avatud lähtekoodiga tehisintellekti mudelite sari.

Phi on hetkel kõige võimsam ja kulutõhusam väike keelemudel (SLM), millel on väga head tulemused mitmekeelse, arutelu, teksti/vestluse genereerimise, kodeerimise, piltide, heli ja teiste stsenaariumide osas.

Saate Phi paigaldada kas pilve või servaseadmetele ning luua hõlpsasti generatiivseid tehisintellekti rakendusi piiratud arvutusvõimsusega.

Järgige neid samme, et alustada nende ressursside kasutamist:
1. **Forkige hoidla**: Klõpsake [![GitHub forkid](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Kloonige hoidla**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Liituge Microsofti AI Discord kogukonnaga ja kohtuge ekspertide ning kaasaarendajatega**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/et/cover.eb18d1b9605d754b.webp)

### 🌐 Mitmekeelne tugi

#### Toetatud GitHub Actioni kaudu (automatiseeritud ja alati ajakohane)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[araabia](../ar/README.md) | [bengali](../bn/README.md) | [bulgaaria](../bg/README.md) | [birma (Myanmar)](../my/README.md) | [hiina (lihtsustatud)](../zh-CN/README.md) | [hiina (traditsiooniline, Hongkong)](../zh-HK/README.md) | [hiina (traditsiooniline, Macau)](../zh-MO/README.md) | [hiina (traditsiooniline, Taiwan)](../zh-TW/README.md) | [horvaadi](../hr/README.md) | [tšehhi](../cs/README.md) | [taani](../da/README.md) | [hollandi](../nl/README.md) | [eesti](./README.md) | [soome](../fi/README.md) | [prantsuse](../fr/README.md) | [saksa](../de/README.md) | [kreeka](../el/README.md) | [heebrea](../he/README.md) | [hindi](../hi/README.md) | [ungari](../hu/README.md) | [indoneesia](../id/README.md) | [itaalia](../it/README.md) | [jaapani](../ja/README.md) | [kannada](../kn/README.md) | [korea](../ko/README.md) | [leedu](../lt/README.md) | [malai](../ms/README.md) | [malajalami](../ml/README.md) | [marathi](../mr/README.md) | [nepali](../ne/README.md) | [Nigeeria pidgin](../pcm/README.md) | [norra](../no/README.md) | [pärsia (farsi)](../fa/README.md) | [poola](../pl/README.md) | [portugali (Brasiilia)](../pt-BR/README.md) | [portugali (Portugal)](../pt-PT/README.md) | [pandžabi (Gurmukhi)](../pa/README.md) | [rumeenia](../ro/README.md) | [vene](../ru/README.md) | [serbia (kirillitsa)](../sr/README.md) | [slovaki](../sk/README.md) | [sloveeni](../sl/README.md) | [hispaania](../es/README.md) | [suahiili](../sw/README.md) | [rootsi](../sv/README.md) | [tagalogi (filipino)](../tl/README.md) | [tamil](../ta/README.md) | [telugu](../te/README.md) | [tai](../th/README.md) | [türgi](../tr/README.md) | [ukraina](../uk/README.md) | [urdu](../ur/README.md) | [vietnami](../vi/README.md)

> **Eelistad kloonida lokaalselt?**
>
> See hoidla sisaldab üle 50 keele tõlkeid, mis suurendavad oluliselt allalaaditavat mahku. Kui soovid kloonida ilma tõlgeteta, kasuta sparse checkout-i:
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
> See annab sulle kõik vajaliku kursuse läbimiseks palju kiirema allalaadimisega.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Sisukord
- Sissejuhatus - [Tere tulemast Phi pere juurde](./md/01.Introduction/01/01.PhiFamily.md) - [Keskkonna seadistamine](./md/01.Introduction/01/01.EnvironmentSetup.md) - [Oluliste tehnoloogiate mõistmine](./md/01.Introduction/01/01.Understandingtech.md) - [Tehisintellekti ohutus Phi mudelite jaoks](./md/01.Introduction/01/01.AISafety.md) - [Phi riistvara tugi](./md/01.Introduction/01/01.Hardwaresupport.md) - [Phi mudelid ja kättesaadavus platvormide lõikes](./md/01.Introduction/01/01.Edgeandcloud.md) - [Guidance-ai ja Phi kasutamine](./md/01.Introduction/01/01.Guidance.md) - [GitHub Marketplace mudelid](https://github.com/marketplace/models) - [Azure AI mudelite kataloog](https://ai.azure.com) - Phi järeldamine erinevates keskkondades - [Hugging face](./md/01.Introduction/02/01.HF.md) - [GitHub mudelid](./md/01.Introduction/02/02.GitHubModel.md) - [Microsoft Foundry mudelite kataloog](./md/01.Introduction/02/03.AzureAIFoundry.md) - [Ollama](./md/01.Introduction/02/04.Ollama.md) - [AI tööriistakast VSCode’is (AITK)](./md/01.Introduction/02/05.AITK.md) - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md) - [Foundry kohalik](./md/01.Introduction/02/07.FoundryLocal.md) - Phi perekonna järeldamine - [Phi järeldamine iOS-is](./md/01.Introduction/03/iOS_Inference.md) - [Phi järeldamine Androidis](./md/01.Introduction/03/Android_Inference.md) - [Phi järeldamine Jetsonis](./md/01.Introduction/03/Jetson_Inference.md) - [Phi järeldamine AI PC-s](./md/01.Introduction/03/AIPC_Inference.md) - [Phi järeldamine Apple MLX raamistikuga](./md/01.Introduction/03/MLX_Inference.md) - [Phi järeldamine kohalikus serveris](./md/01.Introduction/03/Local_Server_Inference.md) - [Phi järeldamine kaugserveris AI tööriistakasti abil](./md/01.Introduction/03/Remote_Interence.md) - [Phi järeldamine Rustiga](./md/01.Introduction/03/Rust_Inference.md) - [Phi--Vision järeldamine kohalikus keskkonnas](./md/01.Introduction/03/Vision_Inference.md) - [Phi järeldamine Kaito AKS ja Azure konteineritega (ametlik tugi)](./md/01.Introduction/03/Kaito_Inference.md) - [Phi perekonna kvantimine](./md/01.Introduction/04/QuantifyingPhi.md) - [Phi-3.5 / 4 kvantimine kasutades llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md) - [Phi-3.5 / 4 kvantimine kasutades generatiivse AI laiendusi onnxruntime jaoks](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md) - [Phi-3.5 / 4 kvantimine Intel OpenVINO abil](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md) - [Phi-3.5 / 4 kvantimine Apple MLX raamistiku abil](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md) - Phi hindamine - [Vastutustundlik AI](./md/01.Introduction/05/ResponsibleAI.md) - [Microsoft Foundry hindamiseks](./md/01.Introduction/05/AIFoundry.md) - [Promptflow kasutamine hindamiseks](./md/01.Introduction/05/Promptflow.md) - RAG Azure AI Searchiga - [Kuidas kasutada Phi-4-mini ja Phi-4-multimodal(RAG) Azure AI Searchiga](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb) - Phi rakenduste arenduse näited - Teksti ja vestluse rakendused - Phi-4 näited - [📓] [Vestlus Phi-4-mini ONNX mudeliga](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md) - [Vestlus Phi-4 kohaliku ONNX mudeliga .NET-is](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) - [Vestlus .NET käsurea rakendusega Semantic Kernel ja Phi-4 ONNX abil](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) - Phi-3 / 3.5 näited - [Kohalik vestlusrobot brauseris Phi3, ONNX Runtime Webi ja WebGPU abil](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat) - [OpenVINO vestlus](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md) - [Mitme mudeli vestlus - interaktiivne Phi-3-mini ja OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md) - [MLFlow - kestade ehitamine ja Phi-3 kasutamine MLFlow-ga](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md) - [Mudeliparandus - kuidas optimeerida Phi-3-mini mudelit ONNX Runtime Webi jaoks Olive’iga](https://github.com/microsoft/Olive/tree/main/examples/phi3) - [WinUI3 rakendus Phi-3 mini-4k-instruct-onnx abil](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/) -[WinUI3 mitme mudeli AI võimendatud märkmete rakenduse näide](https://github.com/microsoft/ai-powered-notes-winui3-sample) - [Kohandatud Phi-3 mudelite täpsustamine ja integreerimine Prompt Flow abil](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md) - [Kohandatud Phi-3 mudelite täpsustamine ja integreerimine Prompt Flow abil Microsoft Foundrys](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md) - [Täpsustatud Phi-3 / Phi-3.5 mudeli hindamine Microsoft Foundrys, keskendudes Microsofti vastutustundliku AI põhimõtetele](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md) - [📓] [Phi-3.5-mini-instruct keele ennustamise näide (hiina/inglise keel)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb) - [Phi-3.5-Instruct WebGPU RAG vestlusrobot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md) - [Windows GPU kasutamine Prompt Flow lahenduse loomiseks Phi-3.5-Instruct ONNX-iga](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md) - [Microsoft Phi-3.5 tflite kasutamine Androidi rakenduse loomiseks](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md) - [Q&A .NET näide, kasutades kohalikku ONNX Phi-3 mudelit koos Microsoft.ML.OnnxRuntime’iga](../../md/04.HOL/dotnet/src/LabsPhi301) - [Käsurea vestlus .NET rakendus Semantic Kerneliga ja Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302) - Azure AI järeldusrakenduste SDK koodi põhised näited - Phi-4 näited - [📓] [Projekti koodi genereerimine Phi-4-multimodaliga](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md) - Phi-3 / 3.5 näited - [Ehita oma Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 perekonnaga](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md) - [Loo oma Visual Studio Code Chat Copilot agent Phi-3.5-ga GitHub mudelite abil](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md) - Täiustatud mõtlemise näited - Phi-4 näited - [📓] [Phi-4-mini-reasoning või Phi-4-reasoning näited](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md) - [📓] [Phi-4-mini-reasoningu täpsustamine Microsoft Olive abil](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Phi-4-mini-reasoningu täpsustamine Apple MLX abil](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Phi-4-mini-reasoning GitHub mudelitega](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb) - [📓] [Phi-4-mini-reasoning Microsoft Foundry mudelitega](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb) -
Demo'd - [Phi-4-mini demo'd Hugging Face Spaces hostitudel](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo) - [Phi-4-multimodal demo'd Hugginge Face Spaces hostitudel](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo) - Visiooni Näidised - Phi-4 Näidised - [📓] [Kasutage Phi-4-multimodal piltide lugemiseks ja koodi genereerimiseks](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) - Phi-3 / 3.5 Näidised - [📓][Phi-3-visioon-pildi tekst tekstiks](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [Phi-3-visioon-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html) - [📓][Phi-3-visioon CLIP embedimine](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [DEMO: Phi-3 taaskasutus](https://github.com/jennifermarsman/PhiRecycling/) - [Phi-3-visioon - Visuaalne keeleassistent - Phi3-Visiooni ja OpenVINO-ga](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html) - [Phi-3 Visioon Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md) - [Phi-3 Visioon OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md) - [📓][Phi-3.5 Visioon mitmekordne raam või mitme pildiga näidis](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb) - [Phi-3 Visioon Kohalik ONNX mudel Microsoft.ML.OnnxRuntime .NET kasutades](../../md/04.HOL/dotnet/src/LabsPhi303) - [Menüü-põhine Phi-3 Visioon Kohalik ONNX mudel Microsoft.ML.OnnxRuntime .NET kasutades](../../md/04.HOL/dotnet/src/LabsPhi304) - Põhjendamise-Visiooni Näidised - Phi-4-Põhjendamine-Visioon-15B - [📓] [Phi-4-Põhjendamine-Visioon-15B kasutamine jaywalking tuvastamiseks](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb) - [📓] [Phi-4-Põhjendamine-Visioon-15B kasutamine matemaatikas](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb) - [📓] [Phi-4-Põhjendamine-Visioon-15B kasutamine kasutajaliidese tuvastamiseks](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb) - Matemaatika Näidised - Phi-4-Mini-Flash-Põhjendamine-Juhend Näidised [Matemaatika Demo Phi-4-Mini-Flash-Põhjendamine-Juhendiga](./md/02.Application/09.Math/MathDemo.ipynb) - Audio Näidised - Phi-4 Näidised - [📓] [Audio transkriptsioonide väljavõtmine Phi-4-multimodal kasutades](./md/02.Application/05.Audio/Phi4/Transciption/README.md) - [📓] [Phi-4-multimodal audio näidis](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb) - [📓] [Phi-4-multimodal kõnetõlke näidis](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb) - [.NET konsoolirakendus Phi-4-multimodal audio kasutamiseks helifaili analüüsimiseks ja transkriptsiooni genereerimiseks](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) - MOE Näidised - Phi-3 / 3.5 Näidised - [📓] [Phi-3.5 Ekspertide Segud (MoEs) Sotsiaalmeedia Näidis](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb) - [📓] [Taastamis-põhise Generatsiooni (RAG) töövoo ehitamine NVIDIA NIM Phi-3 MOE, Azure AI Search ja LlamaIndex'iga](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb) - - Funktsioonikõnede Näidised - Phi-4 Näidised 🆕 - [📓] [Funktsioonikõnede kasutamine Phi-4-mini'ga](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md) - [📓] [Funktsioonikõnede kasutamine mitme agendi loomiseks Phi-4-mini'ga](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb) - [📓] [Funktsioonikõnede kasutamine Ollamaga](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb) - [📓] [Funktsioonikõnede kasutamine ONNX-iga](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb) - Multimodaalse Segamise Näidised - Phi-4 Näidised 🆕 - [📓] [Phi-4-multimodal kasutamine tehnoloogiauudiste ajakirjanikuna](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb) - [.NET konsoolirakendus Phi-4-multimodal kasutamiseks piltide analüüsimiseks](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) - Peenhäälestamise Phi Näidised - [Peenhäälestamise stsenaariumid](./md/03.FineTuning/FineTuning_Scenarios.md) - [Peenhäälestamine vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md) - [Peenhäälestamine Las Phi-3 saada tööstuseksperdiks](./md/03.FineTuning/LetPhi3gotoIndustriy.md) - [Peenhäälestamine Phi-3 AI Toolkit VS Code'is](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md) - [Peenhäälestamine Phi-3 Azure Masinõppeteenusega](./md/03.FineTuning/Introduce_AzureML.md) - [Peenhäälestamine Phi-3 Lora abil](./md/03.FineTuning/FineTuning_Lora.md) - [Peenhäälestamine Phi-3 QLora abil](./md/03.FineTuning/FineTuning_Qlora.md) - [Peenhäälestamine Phi-3 Microsoft Foundryga](./md/03.FineTuning/FineTuning_AIFoundry.md) - [Peenhäälestamine Phi-3 Azure ML CLI/SDK-ga](./md/03.FineTuning/FineTuning_MLSDK.md) - [Peenhäälestamine Microsoft Olive'iga](./md/03.FineTuning/FineTuning_MicrosoftOlive.md) - [Peenhäälestamine Microsoft Olive praktilises laboris](./md/03.FineTuning/olive-lab/readme.md) - [Peenhäälestamine Phi-3-visioon Weights and Bias'iga](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md) - [Peenhäälestamine Phi-3 Apple MLX raamistikuga](./md/03.FineTuning/FineTuning_MLX.md) - [Peenhäälestamine Phi-3-visioon (ametlik tugi)](./md/03.FineTuning/FineTuning_Vision.md) - [Peenhäälestamine Phi-3 Kaito AKS, Azure konteineritega (ametlik tugi)](./md/03.FineTuning/FineTuning_Kaito.md) - [Peenhäälestamine Phi-3 ja 3.5 visioon](https://github.com/2U1/Phi3-Vision-Finetune) - Praktiline Labor - [Tipptasemel mudelite uurimine: LLM-id, SLM-id, kohalik arendus ja rohkem](https://github.com/microsoft/aitour-exploring-cutting-edge-models) - [NLP potentsiaali avamine: peenhäälestamine Microsoft Olive'iga](https://github.com/azure/Ignite_FineTuning_workshop) - Akadeemilised uurimused ja publikatsioonid - [Textbooks Are All You Need II: phi-1.5 tehniline raport](https://arxiv.org/abs/2309.05463) - [Phi-3 tehniline raport: võimekas keelemudel teie telefonis lokaalselt](https://arxiv.org/abs/2404.14219) - [Phi-4 tehniline raport](https://arxiv.org/abs/2412.08905) - [Phi-4-Mini tehniline raport: kompaktsed, kuid võimsad multimodaalsed keelemudelid Mixture-of-LoRAs abil](https://arxiv.org/abs/2503.01743) - [Väikeste keelemudelite optimeerimine sõiduki funktsioonikõnede jaoks](https://arxiv.org/abs/2501.02342) - [(WhyPHI) PHI-3 peenhäälestamine mitmikvalikvastuste küsimustele vastamiseks: metoodika, tulemused ja väljakutsed](https://arxiv.org/abs/2501.01588) - [Phi-4-põhjendamise tehniline raport](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-põhjendamine Tehniline aruanne](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)
# Phi Kokkiraamat: Microsofti Phi Mudelite praktilised näited

[![Ava ja kasuta näidiseid GitHub Codespaces'is](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Ava Dev Containers'is](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub kaastöötajad](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub probleemid](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub tõmbepäringud](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![Tõmbepäringud on teretulnud](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub jälgijad](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub hargnemised](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub tähed](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi on Microsofti välja töötatud avatud lähtekoodiga tehisintellekti mudelite sari.

Phi on praegu kõige võimsam ja kuluefektiivsem väike keelemudel (SLM), millel on väga head mitmekeelsed, loogikapõhised, teksti/vestluse genereerimise, kodeerimise, piltide, heli ja muudes stsenaariumides toimivuse näitajad.

Saate Phi paigaldada kas pilve või servaseadmetesse ning lihtsa vaevaga luua generatiivseid tehisintellekti rakendusi piiratud arvutusvõimsusega.

Järgige neid samme, et alustada nende ressursside kasutamist:
1. **Tee hoidla fork:** Klõpsa [![GitHub hargnemised](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Kloonige hoidla:** `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Liitu Microsoft AI Discord kogukonnaga ja kohtuge ekspertide ning teiste arendajatega**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/et/cover.eb18d1b9605d754b.webp)

### 🌐 Mitmekeelne tugi

#### Toetatud GitHub Actioni kaudu (automaatne ja alati ajakohane)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Araabia](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaaria](../bg/README.md) | [Birma (Myanmar)](../my/README.md) | [Hiina (lihtsustatud)](../zh-CN/README.md) | [Hiina (traditsiooniline, Hongkong)](../zh-HK/README.md) | [Hiina (traditsiooniline, Macau)](../zh-MO/README.md) | [Hiina (traditsiooniline, Taiwan)](../zh-TW/README.md) | [Horvaadi](../hr/README.md) | [Tšehhi](../cs/README.md) | [Taani](../da/README.md) | [Hollandi](../nl/README.md) | [Eesti](./README.md) | [Soome](../fi/README.md) | [Prantsuse](../fr/README.md) | [Saksa](../de/README.md) | [Kreeka](../el/README.md) | [Heebrea](../he/README.md) | [Hindi](../hi/README.md) | [Ungari](../hu/README.md) | [Indoneesia](../id/README.md) | [Itaalia](../it/README.md) | [Jaapani](../ja/README.md) | [Kannada](../kn/README.md) | [Korea](../ko/README.md) | [Leedu](../lt/README.md) | [Malai](../ms/README.md) | [Malajalami](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigeeria pidgin](../pcm/README.md) | [Norra](../no/README.md) | [Pärsia (Farsi)](../fa/README.md) | [Poola](../pl/README.md) | [Portugali (Brasiilia)](../pt-BR/README.md) | [Portugali (Portugal)](../pt-PT/README.md) | [Pandžabi (Gurmukhi)](../pa/README.md) | [Rumeenia](../ro/README.md) | [Vene](../ru/README.md) | [Serbia (kirilitsas)](../sr/README.md) | [Slovaki](../sk/README.md) | [Sloveeni](../sl/README.md) | [Hispaania](../es/README.md) | [Suaheli](../sw/README.md) | [Rootsi](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamili](../ta/README.md) | [Telugu](../te/README.md) | [Tai](../th/README.md) | [Türgi](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnami](../vi/README.md)

> **Eelistad lokaalselt kloonida?**
>
> See hoidla sisaldab 50+ keele tõlkeid, mis suurendab oluliselt allalaadimise mahtu. Tõlgeteta kloonimiseks kasuta sparse checkout'i:
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
> See annab sulle kõik vajaliku kursuse läbimiseks palju kiirema allalaadimisega.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Sisukord

## Phi Mudelite kasutamine

### Phi Microsoft Foundry keskkonnas

Saate õppida, kuidas Microsoft Phi kasutada ja kuidas ehitada E2E lahendusi erinevatele riistvaraseadmetele. Et Phi'd ise kogeda, alustage mudelitega mängimist ja kohandage Phi oma stsenaariumite jaoks [Microsoft Foundry Azure AI Mudelikataloogi](https://aka.ms/phi3-azure-ai) abil. Lisateavet leiate juhendist Alustamine [Microsoft Foundryga](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Mänguväljak**
Igal mudelil on spetsiaalne testimise mänguväljak [Azure AI Playground](https://aka.ms/try-phi3).

### Phi GitHub mudelites

Saate õppida, kuidas Microsoft Phi kasutada ja kuidas ehitada E2E lahendusi erinevatele riistvaraseadmetele. Et Phi'd ise kogeda, alustage mudeliga mängimist ja kohandage Phi oma stsenaariumite jaoks [GitHub Mudelikataloogi](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) abil. Lisateavet leiate juhendist Alustamine [GitHub Mudelikataloogiga](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Mänguväljak**
Igal mudelil on [pühendatud testimise mänguväljak](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi Hugging Face platvormil

Leiate mudeli ka [Hugging Face](https://huggingface.co/microsoft) platvormilt.

**Mänguväljak**
[Hugging Chat mänguväljak](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 Muud kursused

Meie meeskond toodab ka teisi kursuseid! Vaadake lähemalt:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j algajatele](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js algajatele](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain algajatele](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agendid
[![AZD algajatele](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI algajatele](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP algajatele](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agendid algajatele](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatiivse AI seeria
[![Generatiivne AI algajatele](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatiivne AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatiivne tehisintellekt (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatiivne tehisintellekt (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Põhialgne õppimine
[![ML algajatele](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Andmeteadus algajatele](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![Tehisintellekt algajatele](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Küberjulgeolek algajatele](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Veebiarendus algajatele](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![Asjade internet algajatele](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR arendus algajatele](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copiloti sari
[![Copilot AI paarisprogrammeerimiseks](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET jaoks](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copiloti seiklus](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Vastutustundlik tehisintellekt 

Microsoft on pühendunud aitama oma klientidel kasutada meie tehisintellekti tooteid vastutustundlikult, jagades oma õppetunde ja luues usaldusel põhinevaid partnerlusi selliste tööriistade abil nagu läbipaistvuse märkmed ja mõju hindamised. Paljusid neist ressurssidest leiate aadressilt [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofti lähenemine vastutustundlikule tehisintellektile põhineb meie tehisintellekti põhimõtetel: õiglus, usaldusväärsus ja ohutus, privaatsus ja turvalisus, kaasamine, läbipaistvus ning vastutustundlikkus.

Suurte keele-, pildi- ja kõnemudelite - nagu selles näites kasutatud mudelite - käitumine võib potentsiaalselt olla ebaõiglane, ebakindel või solvav, põhjustades sellega kahju. Palun tutvuge [Azure OpenAI teenuse läbipaistvuse märkmega](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), et olla teadlik riskidest ja piirangutest.

Soovitatav lähenemine nende riskide maandamiseks on lisada oma arhitektuuri turvasüsteem, mis suudab tuvastada ja vältida kahjulikku käitumist. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) pakub sõltumatut kaitsekihi, mis suudab rakendustes ja teenustes tuvastada kahjulikku kasutajate loodud ja tehisintellekti loodud sisu. Azure AI Content Safety sisaldab teksti ja pildi API-sid, mis võimaldavad tuvastada kahjulikku materjali. Microsoft Foundrys võimaldab Content Safety teenus vaadata, uurida ja proovida näidiskoodi kahjuliku sisu tuvastamiseks erinevates modaliteetides. Järgmine [algusjuhend](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) juhendab teid teenusele päringute tegemisel.

Veel üks aspekt, mida arvesse võtta, on kogu rakenduse jõudlus. Mitmemodaalsete ja mitmemudeliliste rakenduste puhul mõistame jõudlust kui seda, et süsteem toimib nii nagu teie ja teie kasutajad ootavad, sealhulgas mitte genereerides kahjulikke väljundeid. Oluline on hinnata oma kogu rakenduse jõudlust, kasutades [jõudluse ja kvaliteedi ning riski ja ohutuse hindajaid](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Samuti on teil võimalus luua ja hinnata [kohandatud hindajate](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) abil.

Te saate hinnata oma tehisintellekti rakendust oma arenduskeskkonnas, kasutades [Azure AI hindamise SDK-d](https://microsoft.github.io/promptflow/index.html). Olgu teil testandmestik või eesmärk, mõõdetakse teie generatiivse tehisintellekti rakenduse genereeringuid kvantitatiivselt sisseehitatud hindajate või teie valitud kohandatud hindajate abil. Azure AI hindamise SDK-ga alustamiseks ja süsteemi hindamiseks võite järgida [algusjuhendit](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kui olete hindamissoorituse läbi viinud, saate tulemusi [visualiseerida Microsoft Foundrys](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## Kaubamärgid

See projekt võib sisaldada kaubamärke või logosi projektide, toodete või teenuste jaoks. Microsofti kaubamärkide või logode autoriseeritud kasutamine sõltub ja peab järgima [Microsofti kaubamärkide ja brändi juhiseid](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Microsofti kaubamärkide või logode kasutamine muudetud versioonides ei tohi tekitada segadust ega viidata Microsofti sponsorlusele. Kolmandate osapoolte kaubamärkide või logode kasutamine on nende osapoolte poliitikate suhtes kohaldatav.

## Abi saamine

Kui takerduksite või teil on küsimusi tehisintellekti rakenduste loomise kohta, liituge:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Kui teil on toote tagasisidet või ehitamisel esineb vigu, külastage:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument oma emakeeles peaks olema autoriteetne allikas. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->