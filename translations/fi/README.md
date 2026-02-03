# Phi Keittokirja: Käytännön esimerkkejä Microsoftin Phi-malleilla

[![Avaa ja käytä näytteitä GitHub Codespacesissa](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Avaa Dev Containersissa](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub osallistujat](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub ongelmat](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub vetopyynnöt](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR:t tervetulleita](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub seuraajat](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub haarukat](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub tähdet](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi on Microsoftin kehittämä sarja avoimen lähdekoodin tekoälymalleja.

Phi on tällä hetkellä tehokkain ja kustannustehokkain pieni kielimalli (SLM), jolla on erinomaiset suorituskykymittaukset monikielisyydessä, päättelyssä, tekstin/chatin generoinnissa, koodauksessa, kuvissa, äänessä ja muissa käyttötarkoituksissa.

Voit ottaa Phin käyttöön pilvessä tai reunalaitteissa, ja voit helposti rakentaa generatiivisia tekoälysovelluksia rajallisella laskentateholla.

Noudata näitä ohjeita aloittaaksesi näiden resurssien käytön:
1. **Haaraudu arkistosta**: Klikkaa [![GitHub haarukat](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Kloonaa arkisto**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Liity Microsoft AI Discord -yhteisöön ja tapaa asiantuntijoita sekä muita kehittäjiä**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![kansi](../../translated_images/fi/cover.eb18d1b9605d754b.webp)

### 🌐 Monikielituki

#### Tuettu GitHub-toiminnon kautta (automaattinen ja aina ajan tasalla)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabia](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaria](../bg/README.md) | [Burma (Myanmar)](../my/README.md) | [Kiina (yksinkertaistettu)](../zh-CN/README.md) | [Kiina (perinteinen, Hongkong)](../zh-HK/README.md) | [Kiina (perinteinen, Macao)](../zh-MO/README.md) | [Kiina (perinteinen, Taiwan)](../zh-TW/README.md) | [Kroatia](../hr/README.md) | [Tšekki](../cs/README.md) | [Tanska](../da/README.md) | [Hollanti](../nl/README.md) | [Viro](../et/README.md) | [Suomi](./README.md) | [Ranska](../fr/README.md) | [Saksa](../de/README.md) | [Kreikka](../el/README.md) | [Heprea](../he/README.md) | [Hindi](../hi/README.md) | [Unkari](../hu/README.md) | [Indonesia](../id/README.md) | [Italia](../it/README.md) | [Japani](../ja/README.md) | [Kannada](../kn/README.md) | [Korea](../ko/README.md) | [Liettua](../lt/README.md) | [Malaiji](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norja](../no/README.md) | [Persia (Farsi)](../fa/README.md) | [Puola](../pl/README.md) | [Portugali (Brasilia)](../pt-BR/README.md) | [Portugali (Portugali)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romania](../ro/README.md) | [Venäjä](../ru/README.md) | [Serbia (kyrillinen)](../sr/README.md) | [Slovakia](../sk/README.md) | [Slovenia](../sl/README.md) | [Espanja](../es/README.md) | [Swahili](../sw/README.md) | [Ruotsi](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamili](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkki](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnam](../vi/README.md)

> **Haluatko mieluummin kloonata paikallisesti?**

> Tässä arkistossa on yli 50 kielen käännökset, jotka kasvattavat merkittävästi latauskokoa. Jos haluat kloonata ilman käännöksiä, käytä sparse checkoutia:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Tämä antaa sinulle kaiken tarvittavan kurssin suorittamiseen paljon nopeammin.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Sisällysluettelo

- Johdanto
  - [Tervetuloa Phi-perheeseen](./md/01.Introduction/01/01.PhiFamily.md)
  - [Ympäristön asennus](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Keskeisten teknologioiden ymmärtäminen](./md/01.Introduction/01/01.Understandingtech.md)
  - [Tekoälyn turvallisuus Phi-malleille](./md/01.Introduction/01/01.AISafety.md)
  - [Phi-laitetuki](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi-mallit ja saatavuus eri alustoilla](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai:n ja Phin käyttö](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace -mallit](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- Phin päättely eri ympäristöissä
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub-mallit](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi-perheen päättely
    - [Phin päättely iOS:ssä](./md/01.Introduction/03/iOS_Inference.md)
    - [Phin päättely Androidissa](./md/01.Introduction/03/Android_Inference.md)
    - [Phin päättely Jetsossa](./md/01.Introduction/03/Jetson_Inference.md)
    - [Phin päättely AI-PC:ssä](./md/01.Introduction/03/AIPC_Inference.md)
    - [Phin päättely Apple MLX -kehikolla](./md/01.Introduction/03/MLX_Inference.md)
    - [Phin päättely paikallisella palvelimella](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Phin päättely etäpalvelimella AI Toolkitillä](./md/01.Introduction/03/Remote_Interence.md)
    - [Phin päättely Rustilla](./md/01.Introduction/03/Rust_Inference.md)
    - [Phin päättely – Näköaisti paikallisesti](./md/01.Introduction/03/Vision_Inference.md)
    - [Phin päättely Kaito AKS:llä, Azure Containers (virallinen tuki)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phin perheen kvantisointi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Phi-3.5/4 kvantisointi llama.cpp:llä](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Phi-3.5/4 kvantisointi Generative AI -laajennuksilla onnxruntimeen](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Phi-3.5/4 kvantisointi Intel OpenVINOlla](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Phi-3.5/4 kvantisointi Apple MLX -kehikolla](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phin arviointi
    - [Vastuullinen tekoäly](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry arviointia varten](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow:n käyttö arvioinnissa](./md/01.Introduction/05/Promptflow.md)

- RAG Azure AI Searchin kanssa
    - [Phi-4-mini ja Phi-4-multimodal (RAG) käyttö Azure AI Searchin kanssa](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi-sovelluskehitysesimerkit
  - Teksti- ja chat-sovellukset
    - Phi-4-esimerkit 🆕
      - [📓] [Chattaile Phi-4-mini ONNX -mallin kanssa](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chattaile Phi-4 paikallisen ONNX-mallin kanssa .NET:ssä](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Chat .NET-konsolisovellus Phi-4 ONNX:llä käyttäen Semantic Kernelia](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 esimerkit
      - [Paikallinen chatbot selaimessa käyttäen Phi3:ta, ONNX Runtime Web:ia ja WebGPU:ta](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - Interaktiivinen Phi-3-mini ja OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Wrapperin rakentaminen ja Phi-3:n käyttäminen MLFlow’n kanssa](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Mallin optimointi - Kuinka optimoida Phi-3-minimalli ONNX Runtime Webiä varten Olivellä](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3-sovellus Phi-3 mini-4k-instruct-onnx:llä](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 Multi Model AI -voimalla toimivan muistiinpanosovelluksen esimerkki](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Hienosäädä ja integroi mukautetut Phi-3-mallit Prompt flown kanssa](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Hienosäädä ja integroi mukautetut Phi-3-mallit Prompt flown kanssa Azure AI Foundryssa](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Arvioi hienosäädetty Phi-3 / Phi-3.5 -malli Azure AI Foundryssa keskittyen Microsoftin vastuullisen tekoälyn periaatteisiin](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct kielen ennustusnäyte (kiina/englanti)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG -chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windowsin GPU:n käyttö Prompt flow -ratkaisun luontiin Phi-3.5-Instruct ONNX:n kanssa](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tfliten käyttö Android-sovelluksen luontiin](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Kysymys & vastaus .NET-esimerkki paikallisella ONNX Phi-3 -mallilla käyttäen Microsoft.ML.OnnxRuntimea](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Konsolipohjainen chat .NET-sovellus Semantic Kernelilla ja Phi-3:lla](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK -koodiesimerkit
    - Phi-4-esimerkit 🆕
      - [📓] [Projektikoodin generointi Phi-4-multimodalilla](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 -esimerkit
      - [Rakenna oma Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 -perheen avulla](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Luo oma Visual Studio Code Chat Copilot Agent Phi-3.5:lla GitHub-mallien avulla](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Edistyneet päättelyesimerkit
    - Phi-4-esimerkit 🆕
      - [📓] [Phi-4-mini-päättely tai Phi-4-päättelyesimerkit](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Phi-4-mini-päättelyn hienosäätö Microsoft Olivella](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-päättelyn hienosäätö Apple MLX:llä](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-päättely GitHub-malleilla](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-päättely Azure AI Foundry -malleilla](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demonstratiiviset esimerkit
      - [Phi-4-mini-demot Hugging Face Spacesissa](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal-demot Hugginge Face Spacesissa](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Näköesimerkit
    - Phi-4-esimerkit 🆕
      - [📓] [Phi-4-multimodalin käyttö kuvien lukemiseen ja koodin generointiin](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 -esimerkit
      -  [📓][Phi-3-näkökuvan teksti tekstiksi](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-näkö ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-näkö CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 kierrätys](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-näkö - Visuaalinen kielen avustaja - Phi3-Vision ja OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision monikehyksinen tai monikuvainen näyte](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision paikallinen ONNX-malli Microsoft.ML.OnnxRuntime .NETillä](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Valikkopohjainen Phi-3 Vision paikallinen ONNX-malli Microsoft.ML.OnnxRuntime .NETillä](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Matemaattiset esimerkit
    -  Phi-4-Mini-Flash-Reasoning-Instruct -esimerkit 🆕 [Matematiikka-demo Phi-4-Mini-Flash-Reasoning-Instructilla](./md/02.Application/09.Math/MathDemo.ipynb)

  - Ääni-esimerkit
    - Phi-4-esimerkit 🆕
      - [📓] [Äänitallenteiden muuttaminen tekstiksi Phi-4-multimodalilla](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodalin ääninäyte](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal-äänenkäännösnäyte](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET-konsolisovellus käyttäen Phi-4-multimodalia äänen analysointiin ja transkription luontiin](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE-esimerkit
    - Phi-3 / 3.5 -esimerkit
      - [📓] [Phi-3.5 Sekoitusopeuttajien (MoEs) sosiaalisen median näyte](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Hakuun perustuvan generoinnin (RAG) putken rakentaminen NVIDIA NIM Phi-3 MOE:lla, Azure AI Searchilla ja LlamaIndexillä](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Funktioiden kutsun esimerkit
    - Phi-4-esimerkit 🆕
      -  [📓] [Funktioiden kutsun käyttö Phi-4-minillä](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Funktioiden kutsun käyttö moni-agenttien luontiin Phi-4-minin kanssa](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Funktioiden kutsun käyttö Ollaman kanssa](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Funktioiden kutsun käyttö ONNX:n kanssa](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Monimodaalisen sekoituksen esimerkit
    - Phi-4-esimerkit 🆕
      -  [📓] [Phi-4-multimodalin käyttö teknologiatoimittajana](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET-konsolisovellus käyttäen Phi-4-multimodalia kuvien analysointiin](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi-mallien hienosäätö
  - [Hienosäätötapaukset](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Hienosäätö vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Hienosäätö: Anna Phi-3:n tulla alan asiantuntijaksi](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Phi-3:n hienosäätö AI Toolkitilla Visual Studio Codea varten](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Phi-3:n hienosäätö Azure Machine Learning Serviceä käyttäen](./md/03.FineTuning/Introduce_AzureML.md)
  - [Phi-3:n hienosäätö Loralla](./md/03.FineTuning/FineTuning_Lora.md)
  - [Phi-3:n hienosäätö QLoralla](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Phi-3:n hienosäätö Azure AI Foundryssa](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Phi-3:n hienosäätö Azure ML CLI/SDK:lla](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Hienosäätö Microsoft Olivella](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Hienosäätö Microsoft Olive Hands-On Labilla](./md/03.FineTuning/olive-lab/readme.md)
  - [Phi-3-näön hienosäätö Weights and Biasin kanssa](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Phi-3:n hienosäätö Apple MLX Frameworkilla](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-näön hienosäätö (virallinen tuki)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Phi-3:n hienosäätö Kaito AKS:ssa, Azure Containersissa (virallinen tuki)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3:n ja 3.5 Vision hienosäätö](https://github.com/2U1/Phi3-Vision-Finetune)

- Käytännön harjoitus
  - [Edistyneiden mallien tutkiminen: LLM:t, SLM:t, paikallinen kehitys ja muuta](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP:n potentiaalin vapauttaminen: Hienosäätö Microsoft Olivella](https://github.com/azure/Ignite_FineTuning_workshop)

- Tieteelliset tutkimuspaperit ja julkaisut
  - [Tiedekirjat ovat kaikki mitä tarvitset II: phi-1.5 tekninen raportti](https://arxiv.org/abs/2309.05463)
  - [Phi-3 tekninen raportti: erittäin kykenevä kielimalli paikallisesti puhelimellasi](https://arxiv.org/abs/2404.14219)
  - [Phi-4 tekninen raportti](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini tekninen raportti: tiivis mutta tehokas multimodaalinen kielimalli LoRA-sekoituksen avulla](https://arxiv.org/abs/2503.01743)
  - [Pienten kielimallien optimointi ajoneuvossa tapahtuvaan toimintokutsujen hallintaan](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3-mallin hienosäätö monivalintakysymysten vastaamiseen: menetelmät, tulokset ja haasteet](https://arxiv.org/abs/2501.01588)
  - [Phi-4-päättely tekninen raportti](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-päättely tekninen raportti](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi-mallien käyttäminen

### Phi Azure AI Foundryssä

Voit oppia, miten Microsoft Phitä käytetään ja miten rakennetaan E2E-ratkaisuja eri laitteillasi. Kokeillaksesi Phiä, aloita leikkimällä malleilla ja räätälöimällä Phitä omiin käyttötapauksiisi käyttämällä [Azure AI Foundry Azure AI Model Catalogia](https://aka.ms/phi3-azure-ai). Lisätietoja saat kohdasta Aloittaminen [Azure AI Foundryn kanssa](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Leikkikenttä**  
Jokaisella mallilla on oma leikkikenttä mallin testaamista varten [Azure AI Playground](https://aka.ms/try-phi3).

### Phi GitHub-malleissa

Voit oppia, miten Microsoft Phitä käytetään ja miten rakennetaan E2E-ratkaisuja eri laitteillasi. Kokeillaksesi Phiä, aloita leikkimällä mallilla ja räätälöimällä Phitä omiin käyttötapauksiisi käyttämällä [GitHub Model Catalogia](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Lisätietoja saat kohdasta Aloittaminen [GitHub Model Catalogin kanssa](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Leikkikenttä**  
Jokaisella mallilla on oma [leikkikenttä mallin testaamiseen](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi Hugging Facessa

Mallin voi myös löytää [Hugging Face -palvelusta](https://huggingface.co/microsoft).

**Leikkikenttä**  
[Hugging Chat -leikkikenttä](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 Muut kurssit

Tiimimme tuottaa myös muita kursseja! Katso:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain  
[![LangChain4j aloittelijoille](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)  
[![LangChain.js aloittelijoille](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)  
[![LangChain aloittelijoille](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)  
---

### Azure / Edge / MCP / Agentit  
[![AZD aloittelijoille](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Edge AI aloittelijoille](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![MCP aloittelijoille](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI Agentit aloittelijoille](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)  
  
---

### Generatiivinen AI-sarja  
[![Generatiivinen AI aloittelijoille](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Generatiivinen AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
[![Generatiivinen AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)  
[![Generatiivinen AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)  
  
---

### Perusoppiminen  
[![Koneoppiminen aloittelijoille](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
[![Data Science aloittelijoille](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI aloittelijoille](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
[![Kyberturvallisuus aloittelijoille](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)  
[![Web-kehitys aloittelijoille](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
[![IoT aloittelijoille](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
[![XR-kehitys aloittelijoille](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  
  
---

### Copilot-sarja  
[![Copilot AI-paired programmingiin](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
[![Copilot C#/.NET-kehittäjille](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Vastuullinen tekoäly

Microsoft sitoutuu auttamaan asiakkaitaan käyttämään tekoälytuotteitaan vastuullisesti, jakamaan oppimaamme ja rakentamaan luottamukseen perustuvia kumppanuuksia työkaluilla kuten Läpinäkyvyysmuistiot ja Vaikutusten arvioinnit. Monet näistä resursseista löytyvät osoitteesta [https://aka.ms/RAI](https://aka.ms/RAI).  
Microsoftin vastuullisen tekoälyn lähestymistapa perustuu tekoälyn periaatteisiimme oikeudenmukaisuudesta, luotettavuudesta ja turvallisuudesta, yksityisyydestä ja turvallisuudesta, inklusiivisuudesta, läpinäkyvyydestä sekä vastuullisuudesta.

Laajamittaiset luonnollisen kielen, kuvan ja puheen mallit — kuten tässä esimerkissä käytetyt — voivat käyttäytyä tavoilla, jotka ovat epäoikeudenmukaisia, epäluotettavia tai loukkaavia, ja aiheuttaa vahinkoja. Tutustu [Azure OpenAI -palvelun läpinäkyvyysmuistioon](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) saadaksesi tietoa riskeistä ja rajoituksista.

Suositeltu tapa vähentää näitä riskejä on sisällyttää arkkitehtuuriisi turvallisuusjärjestelmä, joka voi havaita ja estää haitallista käyttäytymistä. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) tarjoaa itsenäisen suojauskerroksen, joka pystyy havaitsemaan haitallisen käyttäjän tai tekoälyn generoiman sisällön sovelluksissa ja palveluissa. Azure AI Content Safetyn tekstin ja kuvan API:t mahdollistavat haitallisen materiaalin tunnistamisen. Azure AI Foundryn sisällä Content Safety -palvelu antaa mahdollisuuden tarkastella, tutkia ja kokeilla esimerkkikoodeja haitallisen sisällön havaitsemiseksi eri modalitiessa. Seuraava [pikakäynnistyksen dokumentaatio](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) opastaa sinut palvelupyynnön tekemisessä.
Toinen huomioon otettava seikka on koko sovelluksen suorituskyky. Monimodaalisissa ja monimallipohjaisissa sovelluksissa suorituskyvyllä tarkoitetaan sitä, että järjestelmä toimii odotustesi ja käyttäjiesi odotusten mukaisesti, mukaan lukien haitallisten tulosteiden välttäminen. On tärkeää arvioida koko sovelluksesi suorituskykyä käyttämällä [Suorituskyky- ja Laatu- sekä Riski- ja Turvallisuusarvioijia](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Sinulla on myös mahdollisuus luoda ja arvioida [mukautetuilla arvioijilla](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Voit arvioida tekoälysovellustasi kehitysympäristössäsi käyttämällä [Azure AI Evaluation SDK:ta](https://microsoft.github.io/promptflow/index.html). Kun käytössäsi on joko testidatasarja tai tavoite, generatiivisen tekoälysi tuotokset mitataan kvantitatiivisesti sisäänrakennetuilla arvioijilla tai valitsemillasi mukautetuilla arvioijilla. Aloittaaksesi järjestelmäsi arvioinnin azure ai evaluation sdk:lla voit seurata [aloitusopasta](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kun suoritat arviointiajon, voit [visualisoida tulokset Azure AI Foundryssa](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Tavaranmerkit

Tämä projekti voi sisältää tavaramerkkejä tai logoja projekteista, tuotteista tai palveluista. Microsoftin tavaramerkkien tai logojen luvallinen käyttö on Microsoftin tavaramerkkiohjeiden [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) mukaista ja sen mukaista.
Microsoftin tavaramerkkien tai logojen käyttö muokatuissa versioissa tästä projektista ei saa aiheuttaa sekaannusta eikä antaa vaikutelmaa Microsoftin sponsoroinnista. Kolmansien osapuolten tavaramerkkien tai logojen käyttö on näiden kolmansien osapuolten politiikkojen alaista.

## Apua saat

Jos juutut tai sinulla on kysyttävää tekoälysovellusten rakentamisesta, liity:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Jos sinulla on tuotepalautetta tai rakennusvirheitä, käy:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttäen tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ota huomioon, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä tulisi pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->