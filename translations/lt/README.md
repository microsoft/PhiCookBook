# Phi Receptų Knyga: Praktiniai Pavyzdžiai su Microsoft Phi Modeliais

[![Atidarykite ir naudokite pavyzdžius GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Atidaryti Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub bendradarbiai](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub problemos](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub stebėtojai](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub šakos](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub žvaigždutės](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi yra atviro kodo dirbtinio intelekto modelių serija, sukurta Microsoft.

Phi šiuo metu yra galingiausias ir ekonomiškiausias mažas kalbos modelis (SLM), turintis labai gerus rezultatus daugia kalbų, mąstymo, teksto/šnekamosios kalbos generavimo, kodavimo, vaizdų, garso ir kitose srityse.

Phi galite diegti debesyje arba periferinėse įrenginiuose, ir galite lengvai kurti generacines DI programas su ribota skaičiavimo galia.

Sekite šiuos žingsnius, kad pradėtumėte naudoti šiuos išteklius:
1. **Fork'inkite Repozitoriją**: Spauskite [![GitHub šakos](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Klonuokite Repozitoriją**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Prisijunkite prie Microsoft DI Discord Bendruomenės ir susipažinkite su ekspertais bei kolegomis kūrėjais**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/lt/cover.eb18d1b9605d754b.webp)

### 🌐 Daugiakalbė Parama

#### Palaikoma naudojant GitHub Action (automatiškai ir visada atnaujinta)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabų](../ar/README.md) | [Bengalų](../bn/README.md) | [Bulgarų](../bg/README.md) | [Birmos (Mianmaro)](../my/README.md) | [Kinų (Supaprastinta)](../zh-CN/README.md) | [Kinų (Tradicinė, Honkongas)](../zh-HK/README.md) | [Kinų (Tradicinė, Makao)](../zh-MO/README.md) | [Kinų (Tradicinė, Taivanas)](../zh-TW/README.md) | [Kroatų](../hr/README.md) | [Čekų](../cs/README.md) | [Danų](../da/README.md) | [Olandų](../nl/README.md) | [Estų](../et/README.md) | [Suomių](../fi/README.md) | [Prancūzų](../fr/README.md) | [Vokiečių](../de/README.md) | [Graikų](../el/README.md) | [Hebrajų](../he/README.md) | [Hindi](../hi/README.md) | [Vengrų](../hu/README.md) | [Indoneziečių](../id/README.md) | [Italų](../it/README.md) | [Japonų](../ja/README.md) | [Kannados](../kn/README.md) | [Korėjiečių](../ko/README.md) | [Lietuvių](./README.md) | [Malajų](../ms/README.md) | [Malajalamo](../ml/README.md) | [Maratų](../mr/README.md) | [Nepaliečių](../ne/README.md) | [Nigerijos pidžinų](../pcm/README.md) | [Norvegų](../no/README.md) | [Persų (Farsi)](../fa/README.md) | [Lenkų](../pl/README.md) | [Portugalų (Brazilijos)](../pt-BR/README.md) | [Portugalų (Portugalijos)](../pt-PT/README.md) | [Pandžabų (Gurmuchi)](../pa/README.md) | [Rumunų](../ro/README.md) | [Rusų](../ru/README.md) | [Serbų (Kiriliška)](../sr/README.md) | [Slovakų](../sk/README.md) | [Slovėnų](../sl/README.md) | [Ispanų](../es/README.md) | [Svahelių](../sw/README.md) | [Švedų](../sv/README.md) | [Tagalogų (Filipinų)](../tl/README.md) | [Tamilų](../ta/README.md) | [Telugų](../te/README.md) | [Tajų](../th/README.md) | [Turkų](../tr/README.md) | [Ukrainiečių](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamiečių](../vi/README.md)

> **Pageidaujate klonuoti vietoje?**
>
> Ši repozitorija turi daugiau nei 50 vertimų, kas žymiai padidina atsisiuntimo dydį. Norėdami klonuoti be vertimų, naudokite sparse checkout:
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
> Tai suteikia viską, ko reikia kursui baigti, bet daug greitesniu atsisiuntimu.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Turinys
- Įvadas - [Sveiki atvykę į Phi šeimą](./md/01.Introduction/01/01.PhiFamily.md) - [Aplinkos nustatymas](./md/01.Introduction/01/01.EnvironmentSetup.md) - [Pagrindinių technologijų supratimas](./md/01.Introduction/01/01.Understandingtech.md) - [Dirbtinio intelekto saugumas Phi modeliams](./md/01.Introduction/01/01.AISafety.md) - [Phi aparatinės įrangos palaikymas](./md/01.Introduction/01/01.Hardwaresupport.md) - [Phi modeliai ir jų prieinamumas skirtingose platformose](./md/01.Introduction/01/01.Edgeandcloud.md) - [Guidance-ai ir Phi naudojimas](./md/01.Introduction/01/01.Guidance.md) - [GitHub Marketplace modeliai](https://github.com/marketplace/models) - [Azure AI modelių katalogas](https://ai.azure.com) - Phi inferencija skirtingose aplinkose - [Hugging face](./md/01.Introduction/02/01.HF.md) - [GitHub modeliai](./md/01.Introduction/02/02.GitHubModel.md) - [Microsoft Foundry modelių katalogas](./md/01.Introduction/02/03.AzureAIFoundry.md) - [Ollama](./md/01.Introduction/02/04.Ollama.md) - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md) - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md) - [Foundry vietinis](./md/01.Introduction/02/07.FoundryLocal.md) - Phi šeimos inferencija - [Phi inferencija iOS](./md/01.Introduction/03/iOS_Inference.md) - [Phi inferencija Android](./md/01.Introduction/03/Android_Inference.md) - [Phi inferencija Jetson](./md/01.Introduction/03/Jetson_Inference.md) - [Phi inferencija AI PC](./md/01.Introduction/03/AIPC_Inference.md) - [Phi inferencija su Apple MLX sistema](./md/01.Introduction/03/MLX_Inference.md) - [Phi inferencija vietiniame serveryje](./md/01.Introduction/03/Local_Server_Inference.md) - [Phi inferencija nuotoliniame serveryje naudojant AI Toolkit](./md/01.Introduction/03/Remote_Interence.md) - [Phi inferencija naudojant Rust](./md/01.Introduction/03/Rust_Inference.md) - [Phi - Vision vietinė inferencija](./md/01.Introduction/03/Vision_Inference.md) - [Phi inferencija su Kaito AKS, Azure konteineriais (oficialus palaikymas)](./md/01.Introduction/03/Kaito_Inference.md) - [Phi šeimos kiekybinimas](./md/01.Introduction/04/QuantifyingPhi.md) - [Phi-3.5 / 4 kiekybinimas naudojant llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md) - [Phi-3.5 / 4 kiekybinimas naudojant Generative AI pratęsimas onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md) - [Phi-3.5 / 4 kiekybinimas naudojant Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md) - [Phi-3.5 / 4 kiekybinimas naudojant Apple MLX sistemą](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md) - Phi vertinimas - [Atsakingas DI](./md/01.Introduction/05/ResponsibleAI.md) - [Microsoft Foundry vertinimui](./md/01.Introduction/05/AIFoundry.md) - [Vertinimas naudojant Promptflow](./md/01.Introduction/05/Promptflow.md) - RAG su Azure AI Search - [Kaip naudoti Phi-4-mini ir Phi-4-multimodal (RAG) su Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb) - Phi programų kūrimo pavyzdžiai - Teksto ir pokalbių programos - Phi-4 pavyzdžiai - [📓] [Pokalbiai su Phi-4-mini ONNX modeliu](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md) - [Pokalbiai su Phi-4 vietiniu ONNX modeliui .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) - [Pokalbiai .NET konsolėje su Phi-4 ONNX naudojant Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) - Phi-3 / 3.5 pavyzdžiai - [Vietinis pokalbių robotas naršyklėje naudojant Phi3, ONNX Runtime Web ir WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat) - [OpenVino pokalbių pavyzdys](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md) - [Multi Model - interaktyvus Phi-3-mini ir OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md) - [MLFlow - apvalkalo kūrimas ir Phi-3 naudojimas su MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md) - [Modelio optimizavimas - kaip optimizuoti Phi-3-min modelį ONNX Runtime Web naudojimui su Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3) - [WinUI3 programėlė su Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/) - [WinUI3 Multi Model AI pagrįstos užrašų programėlės pavyzdys](https://github.com/microsoft/ai-powered-notes-winui3-sample) - [Fine-tune ir integruokite individualius Phi-3 modelius su Promptflow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md) - [Fine-tune ir integruokite individualius Phi-3 modelius su Promptflow Microsoft Foundry aplinkoje](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md) - [Įvertinkite Fine-tuned Phi-3 / Phi-3.5 modelius Microsoft Foundry, atsižvelgiant į Microsoft atsakingo DI principus](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md) - [📓] [Phi-3.5-mini-instruct kalbos prognozavimo pavyzdys (kinų/anglų)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb) - [Phi-3.5-Instruct WebGPU RAG pokalbių robotas](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md) - [Windows GPU naudojimas kuriant Promptflow sprendimą su Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md) - [Microsoft Phi-3.5 tflite naudojimas Android programėlei kurti](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md) - [Klausimai ir atsakymai .NET pavyzdys naudojant vietinį ONNX Phi-3 modelį su Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301) - [Konsolinė pokalbių .NET programa su Semantic Kernel ir Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302) - Azure AI inferencijos SDK kodo pavyzdžiai - Phi-4 pavyzdžiai - [📓] [Projektinio kodo generavimas naudojant Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md) - Phi-3 / 3.5 pavyzdžiai - [Sukurkite savo Visual Studio Code GitHub Copilot pokalbių agentą su Microsoft Phi-3 šeima](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md) - [Sukurkite savo Visual Studio Code Chat Copilot agentą su Phi-3.5, naudodami GitHub modelius](./md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md) - Pažangių sprendimų pavyzdžiai - Phi-4 pavyzdžiai - [📓] [Phi-4-mini-reasoning arba Phi-4-reasoning pavyzdžiai](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md) - [📓] [Phi-4-mini-reasoning tikslinimas su Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Phi-4-mini-reasoning tikslinimas su Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Phi-4-mini-reasoning su GitHub modeliais](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb) - [📓] [Phi-4-mini-reasoning su Microsoft Foundry modeliais](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb) -
Demonstruotės - [Phi-4-mini demonstracijos, talpinamos Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo) - [Phi-4-multimodal demonstracijos, talpinamos Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo) - Vizijos pavyzdžiai - Phi-4 pavyzdžiai - [📓] [Naudokite Phi-4-multimodal vaizdams skaityti ir kodo generavimui](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) - Phi-3 / 3.5 pavyzdžiai - [📓][Phi-3-vision- Vaizdo tekstas į tekstą](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html) - [📓][Phi-3-vision CLIP Įterptis](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [DEMO: Phi-3 Perdirbimas](https://github.com/jennifermarsman/PhiRecycling/) - [Phi-3-vision - Vaizdinis kalbos asistentas - su Phi3-Vision ir OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html) - [Phi-3 Vizija Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md) - [Phi-3 Vizija OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md) - [📓][Phi-3.5 Vizijos daugiakadris arba daugiaformatės pavyzdys](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb) - [Phi-3 Vizijos vietinis ONNX modelis naudojant Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303) - [Meniu pagrindu veikiantis Phi-3 Vizijos vietinis ONNX modelis naudojant Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304) - Samprotavimo-Vizijos pavyzdžiai - Phi-4-Samprotavimo-Vizijos-15B - [📓] [Naudojant Phi-4-Samprotavimo-Vizijos-15B avariniam eismui aptikti](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb) - [📓] [Naudojant Phi-4-Samprotavimo-Vizijos-15B matematikai](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb) - [📓] [Naudojant Phi-4-Samprotavimo-Vizijos-15B UI aptikimui](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb) - Matematikos pavyzdžiai - Phi-4-Mini-Flash-Samprotavimas-Instrukcija pavyzdžiai [Matematikos demonstracija su Phi-4-Mini-Flash-Samprotavimas-Instrukcija](./md/02.Application/09.Math/MathDemo.ipynb) - Garso pavyzdžiai - Phi-4 pavyzdžiai - [📓] [Garso transkriptų išgavimas naudojant Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md) - [📓] [Phi-4-multimodal garso pavyzdys](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb) - [📓] [Phi-4-multimodal kalbos vertimo pavyzdys](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb) - [.NET konsolinė programa, naudojanti Phi-4-multimodal garsui analizuoti ir transkriptui generuoti](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) - MOE pavyzdžiai - Phi-3 / 3.5 pavyzdžiai - [📓] [Phi-3.5 Mišrių ekspertų modelių (MoEs) socialinių tinklų pavyzdys](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb) - [📓] [RAG (Retrieval-Augmented Generation) sistemos kūrimas su NVIDIA NIM Phi-3 MOE, Azure AI Search ir LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb) - Funkcijų kvietimo pavyzdžiai - Phi-4 pavyzdžiai 🆕 - [📓] [Funkcijų kvietimas su Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md) - [📓] [Funkcijų kvietimas kuriant daugialypius agentus su Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb) - [📓] [Funkcijų kvietimas su Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb) - [📓] [Funkcijų kvietimas su ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb) - Daugiamodalių mišinys pavyzdžiai - Phi-4 pavyzdžiai 🆕 - [📓] [Phi-4-multimodal naudojimas kaip technologijų žurnalistas](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb) - [.NET konsolinė programa, naudojanti Phi-4-multimodal vaizdų analizei](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) - Phi koregavimo pavyzdžiai - [Koregavimo scenarijai](./md/03.FineTuning/FineTuning_Scenarios.md) - [Koregavimas prieš RAG](./md/03.FineTuning/FineTuning_vs_RAG.md) - [Koregavimas: Leiskite Phi-3 tapti pramonės ekspertu](./md/03.FineTuning/LetPhi3gotoIndustriy.md) - [Phi-3 koregavimas su AI įrankių rinkiniu VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md) - [Phi-3 koregavimas su Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md) - [Phi-3 koregavimas su Lora](./md/03.FineTuning/FineTuning_Lora.md) - [Phi-3 koregavimas su QLora](./md/03.FineTuning/FineTuning_Qlora.md) - [Phi-3 koregavimas su Microsoft Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md) - [Phi-3 koregavimas su Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md) - [Koregavimas su Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md) - [Koregavimas su Microsoft Olive praktinis užsiėmimas](./md/03.FineTuning/olive-lab/readme.md) - [Phi-3-vision koregavimas su Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md) - [Phi-3 koregavimas su Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md) - [Phi-3-vision koregavimas (oficialus palaikymas)](./md/03.FineTuning/FineTuning_Vision.md) - [Phi-3 koregavimas su Kaito AKS, Azure konteineriais (oficialus palaikymas)](./md/03.FineTuning/FineTuning_Kaito.md) - [Phi-3 ir 3.5 Vizijos koregavimas](https://github.com/2U1/Phi3-Vision-Finetune) - Praktiniai užsiėmimai - [Pažangių modelių tyrinėjimas: LLMs, SLMs, vietinė plėtra ir daugiau](https://github.com/microsoft/aitour-exploring-cutting-edge-models) - [NLP galimybių atrakinti: koregavimas su Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop) - Akademiniai tyrimų straipsniai ir publikacijos - [Textbooks Are All You Need II: phi-1.5 techninis pranešimas](https://arxiv.org/abs/2309.05463) - [Phi-3 techninis pranešimas: galingas kalbos modelis vietoje jūsų telefone](https://arxiv.org/abs/2404.14219) - [Phi-4 techninis pranešimas](https://arxiv.org/abs/2412.08905) - [Phi-4-Mini techninis pranešimas: kompaktiški, bet galingi multimodaliniai kalbos modeliai per Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743) - [Mažų kalbos modelių optimizavimas transporto priemonėse naudojamiems funkcijų kvietimams](https://arxiv.org/abs/2501.02342) - [(WhyPHI) PHI-3 koregavimas daugkartiniams pasirinkimo klausimams atsakyti: metodologija, rezultatai ir iššūkiai](https://arxiv.org/abs/2501.01588) - [Phi-4-samprotavimo techninis pranešimas](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-mąstymo techninė ataskaita](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)
# Phi receptų knyga: praktiniai pavyzdžiai su Microsoft Phi modeliais

[![Atidarykite ir naudokite pavyzdžius GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Atidaryti Dev konteineriuose](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub autoriai](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub problemos](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub užklausos](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub stebėtojai](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub šakos](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub žvaigždutės](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi yra atviro kodo AI modelių serija, sukurta Microsoft.

Phi šiuo metu yra galingiausias ir ekonomiškiausias mažas kalbos modelis (SLM), turintis labai gerus tarptautinius, loginio mąstymo, teksto/ pokalbių generavimo, kodavimo, vaizdų, garso ir kitų scenarijų rezultatus.

Galite paleisti Phi debesyje arba krašto įrenginiuose, ir lengvai kurti generatyvias AI programas su ribotais kompiuterių ištekliais.

Sekite šiuos žingsnius, kad pradėtumėte naudotis šiomis priemonėmis:
1. **Fork'inkite repozitoriją**: Spustelėkite [![GitHub šakos](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Klonuokite repozitoriją**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Prisijunkite prie Microsoft AI Discord bendruomenės ir susipažinkite su ekspertais bei kitais kūrėjais**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/lt/cover.eb18d1b9605d754b.webp)

### 🌐 Daugiakalbė palaikymas

#### Palaikoma per GitHub Action (automatizuota ir visada atnaujinama)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](./README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Norite klonuoti lokaliai?**
>
> Ši repozitorija apima daugiau nei 50 kalbų vertimų, todėl atsisiuntimo dydis žymiai padidėja. Norėdami klonuoti be vertimų, naudokite „sparse checkout“:
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
> Tai suteikia jums viską, ko reikia užbaigti kursą daug greičiau atsisiunčiant.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Turinys

## Phi modelių naudojimas

### Phi Microsoft Foundry platformoje

Galite sužinoti, kaip naudoti Microsoft Phi ir kaip kurti E2E sprendimus skirtinguose savo techninės įrangos įrenginiuose. Kad patirtumėte Phi patys, pradėkite žaisti su modeliais ir pritaikyti Phi savo scenarijams naudodami [Microsoft Foundry Azure AI modelių katalogą](https://aka.ms/phi3-azure-ai). Daugiau sužinokite pradėję su [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Playground**
Kiekvienas modelis turi atskirą testavimo aikštelę [Azure AI Playground](https://aka.ms/try-phi3).

### Phi GitHub modeliuose

Galite sužinoti, kaip naudoti Microsoft Phi ir kaip kurti E2E sprendimus skirtinguose savo techninės įrangos įrenginiuose. Kad patirtumėte Phi patys, pradėkite žaisti su modeliu ir pritaikyti Phi savo scenarijams naudodami [GitHub modelių katalogą](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Daugiau sužinokite pradėję su [GitHub modelių katalogu](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**
Kiekvienas modelis turi atskirą [testavimo aikštelę](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi Hugging Face platformoje

Modelį taip pat galite rasti [Hugging Face](https://huggingface.co/microsoft) svetainėje.

**Playground**
 [Hugging Chat aikštelė](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 Kiti kursai

Mūsų komanda kuria ir kitus kursus! Apsilankykite:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j skirtas pradedantiesiems](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js skirtas pradedantiesiems](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain skirtas pradedantiesiems](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agentai
[![AZD skirtas pradedantiesiems](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI skirtas pradedantiesiems](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP skirtas pradedantiesiems](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI agentai skirtas pradedantiesiems](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatyvios AI serijos
[![Generatyvioji AI pradedantiesiems](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatyvioji AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatyvinis DI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatyvinis DI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Pagrindinis mokymasis
[![ML pradedantiesiems](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Duomenų mokslas pradedantiesiems](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![DI pradedantiesiems](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kibernetinis saugumas pradedantiesiems](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Interneto svetainių kūrimas pradedantiesiems](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![Daiktų internetas pradedantiesiems](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR kūrimas pradedantiesiems](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot serija
[![Copilot DI poriniam programavimui](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot nuotykiai](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Atsakingas DI

„Microsoft“ įsipareigoja padėti savo klientams atsakingai naudoti mūsų DI produktus, dalytis savo patirtimi ir kurti pasitikėjimu grįstus partnerystės santykius, naudodamiesi įrankiais, tokiais kaip Skaidrumo pastabos ir poveikio vertinimai. Daugelį šių išteklių rasite adresu [https://aka.ms/RAI](https://aka.ms/RAI).
„Microsoft“ požiūris į atsakingą DI pagrįstas mūsų DI principais: sąžiningumas, patikimumas ir saugumas, privatumas ir saugumas, įtrauktis, skaidrumas ir atskaitomybė.

Didelio masto natūralios kalbos, vaizdų ir balso modeliai – tokie, kokie naudojami šiame pavyzdyje – gali elgtis neteisingai, nepateisintai ar įžeidžiančiai, sukeldami žalą. Prašome pasitikrinti [Azure OpenAI paslaugos Skaidrumo pastabą](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), kad sužinotumėte apie rizikas ir apribojimus.

Rekomenduojamas būdas sumažinti šias rizikas yra į architektūrą įtraukti saugumo sistemą, kuri gali aptikti ir užkirsti kelią žalingam elgesiui. [Azure DI turinio sauga](https://learn.microsoft.com/azure/ai-services/content-safety/overview) suteikia nepriklausomą apsaugos sluoksnį, galintį aptikti žalingą naudotojo sukurtą ir DI sugeneruotą turinį programėlėse ir paslaugose. Azure DI turinio sauga apima teksto ir vaizdų API, leidžiančias aptikti žalingą medžiagą. „Microsoft Foundry“ platformoje Turinio saugos paslauga leidžia jums peržiūrėti, tyrinėti ir išbandyti pavyzdinį kodą, aptinkant žalingą turinį įvairių režimų. Ši [greitos pradžios dokumentacija](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) jus nukreipia, kaip siųsti užklausas paslaugai.

Kitas aspektas, kurį reikia apsvarstyti, yra bendras programėlės našumas. Darant daugialapių ir daugiamodelių programų atveju, našumo samprata yra, kad sistema veikia taip, kaip tikitės jūs ir jūsų naudotojai, įskaitant ir neleidimą generuoti žalingų išvesties rezultatų. Svarbu įvertinti bendrą programėlės našumą naudodami [Našumo ir kokybės bei Rizikos ir saugos vertintojus](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Taip pat turite galimybę kurti ir vertinti naudodami [adaptuotus vertintojus](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Galite įvertinti savo DI programėlę savo kūrimo aplinkoje naudodami [Azure DI evaluacijos SDK](https://microsoft.github.io/promptflow/index.html). Turėdami testinį duomenų rinkinį arba tikslą, jūsų generatyvinio DI programos generavimai kiekybiškai įvertinami su įmontuotais ar pasirinktinais vertintojais. Norėdami pradėti naudotis azure ai evaluation sdk įvertinant savo sistemą, galite vadovautis [greitos pradžios vadovu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Atlikus įvertinimą, galite [vizualizuoti rezultatus Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## Prekių ženklai

Šiame projekte gali būti prekių ženklų arba logotipų, skirtų projektams, produktams ar paslaugoms. Leidžiamas „Microsoft“ prekių ženklų ar logotipų naudojimas priklauso ir turi laikytis [„Microsoft“ Prekių ženklų ir prekės ženklo gairių](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
„Microsoft“ prekių ženklų ar logotipų naudojimas modifikuotose šio projekto versijose neturi sukelti painiavos arba rodyti Microsoft rėmimą. Bet koks trečiųjų šalių prekių ženklų ar logotipų naudojimas priklauso nuo tų trečiųjų šalių politikos.

## Pagalba

Jei susiduriate su kliūtimis ar turite klausimų apie DI programėlių kūrimą, prisijunkite prie:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Jei turite produkto atsiliepimų ar klaidų, kurias norite pranešti, lankykitės:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už jokius nesusipratimus ar neteisingus interpretavimus, kylančius naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->