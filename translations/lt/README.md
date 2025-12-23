<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef3a50368712b1a7483d0def1f70c490",
  "translation_date": "2025-12-21T14:29:21+00:00",
  "source_file": "README.md",
  "language_code": "lt"
}
-->
# Phi receptų knyga: praktiniai pavyzdžiai su Microsoft's Phi modeliais

[![Atverkite ir naudokite pavyzdžius GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Atidaryti Dev konteineriuose](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub indėlininkai](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub problemos](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR laukiami](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub stebėtojai](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub fork'ai](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub žvaigždės](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi yra atvirojo kodo dirbtinio intelekto modelių serija, sukurta Microsoft. 

Šiuo metu Phi yra galingiausias ir ekonomiškiausias mažos apimties kalbos modelis (SLM), kuris demonstruoja puikius rezultatus daugakalbiškumo, loginio samprotavimo, teksto/pokalbio generavimo, programavimo, vaizdų, garso ir kituose scenarijuose. 

Phi galite diegti debesyje arba periferiniuose įrenginiuose, o su ribotais skaičiavimo ištekliais galite lengvai kurti generatyvines DI programas.

Vykdykite šiuos veiksmus, kad pradėtumėte naudotis šiais ištekliais:
1. **Padarykite saugyklos fork'ą**: Spustelėkite [![GitHub fork'ai](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Klonuokite saugyklą**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Prisijunkite prie Microsoft AI Discord bendruomenės ir susipažinkite su ekspertais bei kitais kūrėjais**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![viršelis](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.lt.png)

### 🌐 Daugiakalbis palaikymas

#### Palaikoma per GitHub Action (automatizuota ir visada atnaujinta)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabų](../ar/README.md) | [Bengalų](../bn/README.md) | [Bulgarų](../bg/README.md) | [Birmos (Mianmaras)](../my/README.md) | [Kinų (supaprastinta)](../zh/README.md) | [Kinų (tradicinė, Honkongas)](../hk/README.md) | [Kinų (tradicinė, Makao)](../mo/README.md) | [Kinų (tradicinė, Taivanas)](../tw/README.md) | [Kroatų](../hr/README.md) | [Čekų](../cs/README.md) | [Danų](../da/README.md) | [Olandų](../nl/README.md) | [Estų](../et/README.md) | [Suomių](../fi/README.md) | [Prancūzų](../fr/README.md) | [Vokiečių](../de/README.md) | [Graikų](../el/README.md) | [Hebrajų](../he/README.md) | [Hindų](../hi/README.md) | [Vengrų](../hu/README.md) | [Indoneziečių](../id/README.md) | [Italų](../it/README.md) | [Japonų](../ja/README.md) | [Kannadų](../kn/README.md) | [Korėjiečių](../ko/README.md) | [Lietuvių](./README.md) | [Malajų](../ms/README.md) | [Malajalamo](../ml/README.md) | [Maratų](../mr/README.md) | [Nepaliečių](../ne/README.md) | [Nigerijos pidžinas](../pcm/README.md) | [Norvegų](../no/README.md) | [Persų (farsų)](../fa/README.md) | [Lenkų](../pl/README.md) | [Portugalų (Brazilija)](../br/README.md) | [Portugalų (Portugalija)](../pt/README.md) | [Pandžabų (Gurmukhi)](../pa/README.md) | [Rumunų](../ro/README.md) | [Rusų](../ru/README.md) | [Serbų (kirilica)](../sr/README.md) | [Slovakų](../sk/README.md) | [Slovėnų](../sl/README.md) | [Ispanų](../es/README.md) | [Svahili](../sw/README.md) | [Švedų](../sv/README.md) | [Tagalogų (filipiniečių)](../tl/README.md) | [Tamilų](../ta/README.md) | [Telugų](../te/README.md) | [Tailandiečių](../th/README.md) | [Turkų](../tr/README.md) | [Ukrainiečių](../uk/README.md) | [Urdų](../ur/README.md) | [Vietnamiečių](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Turinys

- Įvadas
  - [Sveiki atvykę į Phi šeimą](./md/01.Introduction/01/01.PhiFamily.md)
  - [Aplinkos nustatymas](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Pagrindinių technologijų supratimas](./md/01.Introduction/01/01.Understandingtech.md)
  - [DI saugumas Phi modeliams](./md/01.Introduction/01/01.AISafety.md)
  - [Phi aparatinės įrangos palaikymas](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi modeliai ir prieinamumas skirtingose platformose](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai ir Phi naudojimas](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace modeliai](https://github.com/marketplace/models)
  - [Azure AI modelių katalogas](https://ai.azure.com)

- Phi inferencija skirtingose aplinkose
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub modeliai](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry modelių katalogas](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi šeimos inferencija
    - [Phi inferencija iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Phi inferencija Android](./md/01.Introduction/03/Android_Inference.md)
    - [Phi inferencija Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Phi inferencija AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Phi inferencija su Apple MLX karkasu](./md/01.Introduction/03/MLX_Inference.md)
    - [Phi inferencija vietiniame serveryje](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Phi inferencija nuotoliniame serveryje naudojant AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Phi inferencija su Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Phi vizijos inferencija vietoje](./md/01.Introduction/03/Vision_Inference.md)
    - [Phi inferencija su Kaito AKS, Azure Containers(official support)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi šeimos kiekybinimas](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Kvantizavimas Phi-3.5 / 4 naudojant llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Kvantizavimas Phi-3.5 / 4 naudojant Generative AI extensions for onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Kvantizavimas Phi-3.5 / 4 naudojant Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Kvantizavimas Phi-3.5 / 4 naudojant Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi vertinimas
    - [Atsakingas DI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry vertinimui](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow naudojimas vertinimui](./md/01.Introduction/05/Promptflow.md)
 
- RAG su Azure AI Search
    - [Kaip naudoti Phi-4-mini ir Phi-4-multimodal(RAG) su Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi programų kūrimo pavyzdžiai
  - Teksto ir pokalbių programos
    - Phi-4 pavyzdžiai 🆕
      - [📓] [Pokalbis su Phi-4-mini ONNX modeliu](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Pokalbis su Phi-4 vietiniu ONNX modeliu .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Pokalbio .NET konsolės programa su Phi-4 ONNX naudojant Sementic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 pavyzdžiai
      - [Vietinis pokalbių robotas naršyklėje naudojant Phi3, ONNX Runtime Web ir WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVINO pokalbis](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Daugiamodelis - interaktyvus Phi-3-mini ir OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - wrapperio kūrimas ir Phi-3 naudojimas su MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Modelio optimizavimas - kaip optimizuoti Phi-3-min modelį ONNX Runtime Web naudojant Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 programėlė su Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 kelių modelių AI užrašų programėlės pavyzdys](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Smulkiai tobulinti ir integruoti pritaikytus Phi-3 modelius su Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Smulkiai tobulinti ir integruoti pritaikytus Phi-3 modelius su Prompt flow Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Įvertinti smulkiai paruoštą Phi-3 / Phi-3.5 modelį Azure AI Foundry, akcentuojant Microsoft atsakingo AI principus](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct kalbos prognozavimo pavyzdys (kinų/anglų)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG pokalbių robotas](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Naudojant Windows GPU kuriant Prompt flow sprendimą su Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Naudojant Microsoft Phi-3.5 tflite kuriant Android programėlę](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Klausimų-atsakymų .NET pavyzdys naudojant vietinį ONNX Phi-3 modelį su Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Konsolės pokalbių .NET programėlė su Semantic Kernel ir Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK kodo pavyzdžiai
    - Phi-4 pavyzdžiai 🆕
      - [📓] [Generuoti projekto kodą naudojant Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 pavyzdžiai
      - [Sukurkite savo Visual Studio Code GitHub Copilot pokalbį su Microsoft Phi-3 šeima](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Sukurkite savo Visual Studio Code Chat Copilot agentą naudodami Phi-3.5 iš GitHub Models](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Pažangaus samprotavimo pavyzdžiai
    - Phi-4 pavyzdžiai 🆕
      - [📓] [Phi-4-mini-samprotavimo arba Phi-4-samprotavimo pavyzdžiai](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Smulkus Phi-4-mini-samprotavimo tobulinimas su Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Smulkus Phi-4-mini-samprotavimo tobulinimas su Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-samprotavimas su GitHub Models](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-samprotavimas su Azure AI Foundry modeliais](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demonstracijos
      - [Phi-4-mini demonstracijos Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal demonstracijos Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Vizijos pavyzdžiai
    - Phi-4 pavyzdžiai 🆕
      - [📓] [Naudokite Phi-4-multimodal skaityti vaizdus ir generuoti kodą](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 pavyzdžiai
      -  [📓][Phi-3-vision vaizdo tekstas į tekstą](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP įterpiniai](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 perdirbimas](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - vizualinis kalbos asistentas - su Phi3-Vision ir OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision daugiakadris arba kelių vaizdų pavyzdys](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision vietinis ONNX modelis naudojant Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Meniu pagrindu veikiantis Phi-3 Vision vietinis ONNX modelis naudojant Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Matematikos pavyzdžiai
    -  Phi-4-Mini-Flash-Reasoning-Instruct pavyzdžiai 🆕 [Matematikos demonstracija su Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - Garso pavyzdžiai
    - Phi-4 pavyzdžiai 🆕
      - [📓] [Išgauti garso transkriptus naudojant Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal garso pavyzdys](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal kalbos vertimo pavyzdys](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET konsolės programa naudojant Phi-4-multimodal garso analizavimui ir transkripcijos generavimui](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE pavyzdžiai
    - Phi-3 / 3.5 pavyzdžiai
      - [📓] [Phi-3.5 ekspertų mišinių modelių (MoEs) socialinių tinklų pavyzdys](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Sukurti Retrieval-Augmented Generation (RAG) sistemą su NVIDIA NIM Phi-3 MOE, Azure AI Search ir LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Funkcijų kvietimo pavyzdžiai
    - Phi-4 pavyzdžiai 🆕
      -  [📓] [Funkcijų kvietimo naudojimas su Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Funkcijų kvietimo naudojimas kuriant daugiaagentę sistemą su Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Funkcijų kvietimo naudojimas su Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Funkcijų kvietimo naudojimas su ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling_ipynb)
  - Multimodalinio miksavimo pavyzdžiai
    - Phi-4 pavyzdžiai 🆕
      -  [📓] [Naudojant Phi-4-multimodal kaip technologijų žurnalistą](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET konsolės programa naudojant Phi-4-multimodal vaizdų analizei](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi smulkiojo tobulinimo pavyzdžiai
  - [Smulkiojo tobulinimo scenarijai](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Smulkus tobulinimas vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Smulkus tobulinimas: leiskite Phi-3 tapti pramonės ekspertu](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Phi-3 smulkus tobulinimas naudojant AI Toolkit for VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Phi-3 smulkus tobulinimas naudojant Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Phi-3 smulkus tobulinimas su Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Phi-3 smulkus tobulinimas su QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Phi-3 smulkus tobulinimas su Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Phi-3 smulkus tobulinimas su Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Smulkus tobulinimas su Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Smulkus tobulinimas su Microsoft Olive praktinis užsiėmimas](./md/03.FineTuning/olive-lab/readme.md)
  - [Phi-3-vision smulkus tobulinimas su Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Phi-3 smulkus tobulinimas su Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision smulkus tobulinimas (oficiali parama)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Phi-3 smulkus tobulinimas su Kaito AKS , Azure Containers(oficiali parama)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 ir 3.5 Vision smulkus tobulinimas](https://github.com/2U1/Phi3-Vision-Finetune)

- Praktinis užsiėmimas
  - [Exploring cutting-edge models: LLMs, SLMs, local development and more](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Unlocking NLP Potential: Fine-Tuning with Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Akademiniai moksliniai straipsniai ir publikacijos
  - [Textbooks Are All You Need II: phi-1.5 techninis pranešimas](https://arxiv.org/abs/2309.05463)
  - [Phi-3 techninis pranešimas: itin pajėgus kalbos modelis, veikiantis lokaliai jūsų telefone](https://arxiv.org/abs/2404.14219)
  - [Phi-4 techninis pranešimas](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Technical Report: Kompaktiški, bet galingi daugiamodaliai kalbos modeliai per Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Mažų kalbos modelių optimizavimas transporto priemonėje vykdomam funkcijų kvietimui](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 smulkus pritaikymas daugiafunkciams pasirinkimų klausimams atsakyti: metodika, rezultatai ir iššūkiai](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning Techninis pranešimas](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning Techninis pranešimas](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Naudojant Phi modelius

### Phi platformoje Azure AI Foundry

Galite sužinoti, kaip naudoti Microsoft Phi ir kaip kurti E2E sprendimus savo įvairiuose aparatūros įrenginiuose. Norėdami patys išbandyti Phi, pradėkite eksperimentuodami su modeliais ir pritaikydami Phi savo scenarijams, naudodami [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) Daugiau sužinosite skyriuje Getting Started with [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Playground**
Kiekvienam modeliui yra skirta atskira bandomoji aplinka modelio testavimui [Azure AI Playground](https://aka.ms/try-phi3).

### Phi GitHub modeliuose

Galite sužinoti, kaip naudoti Microsoft Phi ir kaip kurti E2E sprendimus savo įvairiuose aparatūros įrenginiuose. Norėdami patys išbandyti Phi, pradėkite eksperimentuodami su modeliu ir pritaikydami Phi savo scenarijams, naudodami [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) Daugiau sužinosite skyriuje Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**
Kiekvienam modeliui yra skirta [bandomoji aplinka modelio testavimui](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi platformoje Hugging Face

Modelį taip pat galite rasti [Hugging Face](https://huggingface.co/microsoft)

**Playground**
 [Hugging Chat bandomoji aplinka](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 Kiti kursai

Mūsų komanda rengia ir kitus kursus! Peržiūrėkite:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j pradedantiesiems](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js pradedantiesiems](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD pradedantiesiems](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI pradedantiesiems](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP pradedantiesiems](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI agentai pradedantiesiems](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatyvinio AI serija
[![Generatyvinis AI pradedantiesiems](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatyvinis AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatyvinis AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatyvinis AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Pagrindiniai kursai
[![ML pradedantiesiems](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Duomenų mokslas pradedantiesiems](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI pradedantiesiems](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kibernetinis saugumas pradedantiesiems](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Tinklapių kūrimas pradedantiesiems](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT pradedantiesiems](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR kūrimas pradedantiesiems](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot serija
[![Copilot poriniam programavimui su AI](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot nuotykiai](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Atsakingas DI

Microsoft siekia padėti klientams atsakingai naudoti mūsų DI produktus, dalintis įžvalgomis ir kurti pasitikėjimu grįstas partnerystes per įrankius, tokius kaip Transparency Notes ir Impact Assessments. Dauguma šių išteklių yra pasiekiami adresu [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft požiūris į atsakingą DI remiasi mūsų AI principais: teisingumu, patikimumu ir saugumu, privatumu ir saugumu, įtrauktimi, skaidrumu ir atskaitomybe.

Didesnio masto natūralios kalbos, vaizdų ir balso modeliai – tokie kaip šioje demonstracijoje naudojami – gali elgtis netinkamai, nepatikimai arba įžeidžiančiai, kas gali sukelti žalą. Prašome susipažinti su [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), kad būtumėte informuoti apie rizikas ir apribojimus.

Rekomenduojamas būdas mažinti šias rizikas yra įtraukti saugos sistemą į savo architektūrą, kuri galėtų aptikti ir užkirsti kelią žalingam elgesiui. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) suteikia nepriklausomą apsaugos sluoksnį, galintį aptikti žalingą vartotojų ir DI sugeneruotą turinį programėlėse ir paslaugose. Azure AI Content Safety apima teksto ir vaizdų API, leidžiančias aptikti žalingą turinį. Azure AI Foundry ribose Content Safety paslauga leidžia peržiūrėti, ištirti ir išbandyti pavyzdinį kodą, skirtą žalingam turiniui aptikti per skirtingas modalidades. Tolimesnė [greito pradžios dokumentacija](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) nukreips jus, kaip pateikti užklausas paslaugai.

Kitas svarstytinas aspektas yra bendras programėlės veikimas. Daugiamodalių ir daugelio modelių programėlių atveju veikimo našumu laikome tai, kad sistema veikia taip, kaip tikitės jūs ir jūsų naudotojai, įskaitant ir tai, kad ji negeneruotų žalingų rezultatų. Svarbu įvertinti visos jūsų programėlės veikimą, naudojant [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Taip pat turite galimybę kurti ir vertinti naudodami [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Galite įvertinti savo DI programėlę kūrimo aplinkoje, naudodami [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Turint testinį duomenų rinkinį arba tikslą, jūsų generatyvinio DI programėlės generacijos kiekybiškai matuojamos naudojant įmontuotus ar pasirinktinius vertintojus pagal jūsų pasirinkimą. Norėdami pradėti naudotis azure ai evaluation sdk savo sistemos vertinimui, galite vadovautis [greito pradžios vadovu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kai vykdysite vertinimo paleidimą, galite [vizualizuoti rezultatus Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## Prekės ženklai
Šis projektas gali turėti projektų, produktų ar paslaugų prekės ženklus arba logotipus. Leidžiamas Microsoft prekės ženklų ar logotipų naudojimas yra reglamentuojamas ir turi atitikti [Microsoft prekės ženklų ir prekės ženklo gairės](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Microsoft prekės ženklų ar logotipų naudojimas modifikuotose šio projekto versijose neturi sukelti painiavos ar daryti prielaidos apie Microsoft rėmimą. Bet koks trečiųjų šalių prekės ženklų ar logotipų naudojimas priklauso tų trečiųjų šalių taisyklėms.

## Pagalba

Jei įstrigote arba turite klausimų apie dirbtinio intelekto programėlių kūrimą, prisijunkite:

[![Azure AI Foundry Discord bendruomenė](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Jei turite atsiliepimų apie produktą arba pastebite klaidų kūrimo metu, apsilankykite:

[![Azure AI Foundry kūrėjų forumas](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Pirminis dokumentas originalo kalba turėtų būti laikomas autoritetingu šaltiniu. Kritiniais atvejais rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->