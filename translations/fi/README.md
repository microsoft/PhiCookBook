# Phi-keittokirja: Käytännön esimerkkejä Microsoftin Phi-malleilla

[![Avaa ja käytä esimerkkejä GitHub Codespacesissa](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Avaa Dev Containers -ympäristössä](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub-yhteistyökumppanit](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub-ongelmat](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub vetopyynnöt](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![Vetopyynnöt tervetulleita](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub-seuraajat](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub-haarat](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub-tähdet](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi on Microsoftin kehittämä avoimen lähdekoodin tekoälymallisarja.

Phi on tällä hetkellä tehokkain ja kustannustehokkain pieni kielimalli (SLM), jolla on erinomaiset vertailuarvot monikielisyydessä, päättelyssä, tekstin/chatin generoinnissa, koodauksessa, kuvissa, äänissä ja muissa käyttötarkoituksissa.

Voit ottaa Phin käyttöön pilvessä tai reunalaitteissa, ja voit helposti rakentaa generatiivisia tekoälysovelluksia rajallisella laskentateholla.

Aloita näiden vaiheiden avulla tämän resurssin käyttö:
1. **Forkkaa repositorio**: Klikkaa [![GitHub-haarat](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Kloonaa repositorio**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Liity Microsoft AI Discord -yhteisöön ja tapaa asiantuntijoita ja kehittäjiä**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/fi/cover.eb18d1b9605d754b.webp)

### 🌐 Monikielituki

#### Tuettu GitHub-toiminnon kautta (automaattinen ja aina ajan tasalla)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[arabia](../ar/README.md) | [bengali](../bn/README.md) | [bulgaria](../bg/README.md) | [burma (Myanmar)](../my/README.md) | [kiina (yksinkertaistettu)](../zh-CN/README.md) | [kiina (perinteinen, Hongkong)](../zh-HK/README.md) | [kiina (perinteinen, Macao)](../zh-MO/README.md) | [kiina (perinteinen, Taiwan)](../zh-TW/README.md) | [kroatia](../hr/README.md) | [tsekit](../cs/README.md) | [tanska](../da/README.md) | [hollanti](../nl/README.md) | [viro](../et/README.md) | [suomi](./README.md) | [ranska](../fr/README.md) | [saksa](../de/README.md) | [kreikka](../el/README.md) | [heprea](../he/README.md) | [hindi](../hi/README.md) | [unkari](../hu/README.md) | [indonesia](../id/README.md) | [italia](../it/README.md) | [japani](../ja/README.md) | [kannada](../kn/README.md) | [korea](../ko/README.md) | [liettua](../lt/README.md) | [malaiji](../ms/README.md) | [malajalami](../ml/README.md) | [marathi](../mr/README.md) | [nepali](../ne/README.md) | [nigerian pidgin](../pcm/README.md) | [norja](../no/README.md) | [persia (Farsi)](../fa/README.md) | [puola](../pl/README.md) | [portugali (Brasilia)](../pt-BR/README.md) | [portugali (Portugali)](../pt-PT/README.md) | [pandžabi (Gurmukhi)](../pa/README.md) | [romania](../ro/README.md) | [venäjä](../ru/README.md) | [serbia (kyrillinen)](../sr/README.md) | [slovakki](../sk/README.md) | [sloveeni](../sl/README.md) | [espanja](../es/README.md) | [swahili](../sw/README.md) | [ruotsi](../sv/README.md) | [tagalog (filippiini)](../tl/README.md) | [tamili](../ta/README.md) | [telugu](../te/README.md) | [thai](../th/README.md) | [turkki](../tr/README.md) | [ukraina](../uk/README.md) | [urdu](../ur/README.md) | [vietnam](../vi/README.md)

> **Haluatko mieluummin kloonata paikallisesti?**

> Tämä repositorio sisältää yli 50 käännöstä, mikä kasvattaa merkittävästi latauskokoa. Jos haluat kloonata ilman käännöksiä, käytä harvaa checkouttia:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Tämä antaa sinulle kaiken, mitä tarvitset kurssin läpivientiin huomattavasti nopeammalla latauksella.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Sisällysluettelo

- Johdanto
  - [Tervetuloa Phi-perheeseen](./md/01.Introduction/01/01.PhiFamily.md)
  - [Ympäristön asennus](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Keskeisten teknologioiden ymmärtäminen](./md/01.Introduction/01/01.Understandingtech.md)
  - [Tekoälyn turvallisuus Phi-malleissa](./md/01.Introduction/01/01.AISafety.md)
  - [Phi-laitetuki](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi-mallit ja saatavuus eri alustoilla](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai:n ja Phin käyttö](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace -mallit](https://github.com/marketplace/models)
  - [Azure AI Malliluettelo](https://ai.azure.com)

- Phin päättely eri ympäristöissä
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub-mallit](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry Malliluettelo](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi-perheen päättely
    - [Phin päättely iOS:ssä](./md/01.Introduction/03/iOS_Inference.md)
    - [Phin päättely Androidilla](./md/01.Introduction/03/Android_Inference.md)
    - [Phin päättely Jetsonilla](./md/01.Introduction/03/Jetson_Inference.md)
    - [Phin päättely AI PC:llä](./md/01.Introduction/03/AIPC_Inference.md)
    - [Phin päättely Apple MLX Frameworkin avulla](./md/01.Introduction/03/MLX_Inference.md)
    - [Phin päättely paikallisessa palvelimessa](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Phin päättely etäpalvelimella AI Toolkitin avulla](./md/01.Introduction/03/Remote_Interence.md)
    - [Phin päättely Rustilla](./md/01.Introduction/03/Rust_Inference.md)
    - [Phin päättely – Vision paikallisesti](./md/01.Introduction/03/Vision_Inference.md)
    - [Phin päättely Kaito AKS:llä, Azure Containers (virallinen tuki)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phin kvantisointi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantisointi llama.cpp:llä](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantisointi Generative AI -laajennuksilla onnxruntimeen](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantisointi Intel OpenVINO:lla](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Phi-3.5 / 4 kvantisointi Apple MLX Frameworkilla](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi-arviointi
    - [Vastuullinen tekoäly](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry arviointiin](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow'n käyttö arvioinnissa](./md/01.Introduction/05/Promptflow.md)
 
- RAG Azure AI Searchin kanssa
    - [Kuinka käyttää Phi-4-mini- ja Phi-4-multimodal (RAG) Azure AI Searchin kanssa](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi-sovelluskehityksen esimerkit
  - Teksti- ja chat-sovellukset
    - Phi-4-esimerkit 🆕
      - [📓] [Chat Phi-4-minin ONNX-mallin kanssa](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat Phi-4 paikallisen ONNX-mallin kanssa .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Chat .NET-konsolisovellus Phi-4 ONNX:llä Semantic Kernelin avulla](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 -esimerkit
      - [Paikallinen chatbot selaimessa käyttäen Phi3, ONNX Runtime Web ja WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Monimalli - Interaktiivinen Phi-3-mini ja OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Kääreen rakentaminen ja Phi-3:n käyttö MLFlow’n kanssa](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Mallin optimointi - Kuinka optimoida Phi-3-minimalli ONNX Runtime Webille Olivea käyttäen](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3-sovellus Phi-3 mini-4k-instruct-onnx:llä](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 Monimalli tekoälyllä toimiva muistiinpanosovelluksen esimerkki](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Hienosäädä ja integroi Mukautetut Phi-3-mallit Prompt flow’n kanssa](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Hienosäädä ja integroi Mukautetut Phi-3-mallit Prompt flow’ssa Azure AI Foundryssä](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Arvioi hienosäädetty Phi-3 / Phi-3.5 malli Azure AI Foundryssä, painottaen Microsoftin vastuullisen tekoälyn periaatteita](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct kielen ennustus esimerkki (kiina/englanti)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU:n käyttö Prompt flow -ratkaisun luomiseen Phi-3.5-Instruct ONNX:llä](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite:n käyttö Android-sovelluksen luomiseen](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Kysymys & vastaus .NET-esimerkki paikallista ONNX Phi-3 mallia käyttäen Microsoft.ML.OnnxRuntime -kirjastolla](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Konsolichat .NET-sovellus Semantic Kernelilla ja Phi-3:lla](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK Koodipohjaiset Esimerkit 
    - Phi-4 Esimerkit 🆕
      - [📓] [Luo projektikoodi käyttäen Phi-4-multimodaalia](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 Esimerkit
      - [Rakenna oma Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 Perheen avulla](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Luo oma Visual Studio Code Chat Copilot Agent Phi-3.5:llä GitHub-mallien avulla](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Edistyneet Päättelyesimerkit
    - Phi-4 Esimerkit 🆕
      - [📓] [Phi-4-mini-päättely tai Phi-4-päättelyn esimerkit](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Phi-4-mini-päättelyn hienosäätö Microsoft Olivella](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-päättelyn hienosäätö Apple MLX:llä](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-päättely GitHub-mallien kanssa](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-päättely Azure AI Foundry -mallien kanssa](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demosovellukset
      - [Phi-4-mini demonstraatiot Hugging Face Spaces -palvelussa](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodaalit demonstraatiot Hugging Face Spaces -palvelussa](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Vision Esimerkit
    - Phi-4 Esimerkit 🆕
      - [📓] [Käytä Phi-4-multimodaalia kuvien lukemiseen ja koodin generointiin](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 Esimerkit
      -  [📓][Phi-3-vision-Kuvasta tekstiin tekstiksi](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP -upotus](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Uudelleenkäyttö](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Visuaalinen kieliavustaja - Phi3-Visionilla ja OpenVINOlla](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision monikehyksinen tai monikuva esimerkki](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision paikallinen ONNX-malli Microsoft.ML.OnnxRuntime .NET:illä](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Valikkopohjainen Phi-3 Vision paikallinen ONNX-malli Microsoft.ML.OnnxRuntime .NET:illä](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Matematiikan Esimerkit
    -  Phi-4-Mini-Flash-Päättely-Instruct Esimerkit 🆕 [Matematiikka-demo Phi-4-Mini-Flash-Päättely-Instructilla](./md/02.Application/09.Math/MathDemo.ipynb)

  - Ääni Esimerkit
    - Phi-4 Esimerkit 🆕
      - [📓] [Äänitallenteiden tekstitys Phi-4-multimodaalilla](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodaalinen ääninäyte](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodaalinen puheen käännösnäyte](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET-konsolisovellus käyttäen Phi-4-multimodaalista ääntä audiotiedoston analysointiin ja tekstityksen generointiin](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE Esimerkit
    - Phi-3 / 3.5 Esimerkit
      - [📓] [Phi-3.5 Mixture of Experts (MoEs) sosiaalisen median esimerkki](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Hakua lisäävän generoinnin (RAG) putken rakentaminen NVIDIA NIM Phi-3 MOE:lla, Azure AI Searchilla ja LlamaIndexillä](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - Funktioiden kutsuminen Esimerkit
    - Phi-4 Esimerkit 🆕
      -  [📓] [Funktioiden kutsumisen käyttö Phi-4-minin kanssa](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Funktioiden kutsumista monien agenttien luomiseksi Phi-4-minillä](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Funktioiden kutsumisen käyttö Ollaman kanssa](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [Funktioiden kutsumisen käyttö ONNX:llä](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - Monimodaalinen yhdistäminen Esimerkit
    - Phi-4 Esimerkit 🆕
      -  [📓] [Phi-4-multimodaalia teknologiajournalistina käyttäminen](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET-konsolisovellus käyttäen Phi-4-multimodaalia kuvien analysointiin](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi-mallien hienosäätö
  - [Hienosäätöskenaariot](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Hienosäätö vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Hienosäätö - Anna Phi-3:n tulla alan asiantuntijaksi](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Phi-3 hienosäätö AI Toolkitilla VS Codeen](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Phi-3 hienosäätö Azure Machine Learning Servicellä](./md/03.FineTuning/Introduce_AzureML.md)
  - [Phi-3 hienosäätö Loralla](./md/03.FineTuning/FineTuning_Lora.md)
  - [Phi-3 hienosäätö QLoralla](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Phi-3 hienosäätö Azure AI Foundryllä](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Phi-3 hienosäätö Azure ML CLI/SDK:lla](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Hienosäätö Microsoft Olivella](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Hienosäätö Microsoft Olive Hands-On Labissa](./md/03.FineTuning/olive-lab/readme.md)
  - [Phi-3-vision hienosäätö Weights and Biasin kanssa](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Phi-3 hienosäätö Apple MLX Frameworkilla](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-visionin hienosäätö (virallinen tuki)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Phi-3:n hienosäätö Kaitolla AKS:ssa, Azure Containerseissa (virallinen tuki)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 ja 3.5 Vision hienosäätö](https://github.com/2U1/Phi3-Vision-Finetune)

- Käytännön harjoitustila
  - [Huipputason mallien tutkiminen: LLM:t, SLM:t, paikallinen kehitys ja muuta](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP:n potentiaalin avaaminen: Hienosäätö Microsoft Olivella](https://github.com/azure/Ignite_FineTuning_workshop)

- Akateemiset tutkimusraportit ja julkaisut
  - [Kirjat ovat kaikki mitä tarvitset II: phi-1.5 tekninen raportti](https://arxiv.org/abs/2309.05463)
  - [Phi-3 tekninen raportti: Erittäin kyvykäs kielimalli paikallisesti puhelimellasi](https://arxiv.org/abs/2404.14219)
  - [Phi-4 tekninen raportti](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini tekninen raportti: Kompakti mutta tehokas multimodaalinen kielimalli LoRA-yhdistelmien avulla](https://arxiv.org/abs/2503.01743)
  - [Pienten kielimallien optimointi ajoneuvon toimintokutsuissa](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 hienosäätö monivalintakysymysten vastaamiseen: Menetelmät, tulokset ja haasteet](https://arxiv.org/abs/2501.01588)
  - [Phi-4-päätelmä tekninen raportti](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-päätelmä tekninen raportti](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi-mallien käyttö

### Phi Azure AI Foundryssa

Voit oppia käyttämään Microsoft Phitä ja rakentamaan E2E-ratkaisuja erilaisissa laitteissasi. Kokeillaksesi Phitä itse, aloita leikkimällä malleilla ja mukauttamalla Phitä omiin käyttötarkoituksiisi käyttämällä [Azure AI Foundryn Azure AI -mallikatalogia](https://aka.ms/phi3-azure-ai). Lisätietoa löydät aloituksesta kohdasta [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Leikkikenttä**  
Jokaisella mallilla on oma leikkikenttä mallin testaamiseen [Azure AI Playground](https://aka.ms/try-phi3).

### Phi GitHub-malleissa

Voit oppia käyttämään Microsoft Phitä ja rakentamaan E2E-ratkaisuja erilaisissa laitteissasi. Kokeillaksesi Phitä itse, aloita mallin kanssa leikkimällä ja mukauttamalla Phi käyttötapauksiisi käyttämällä [GitHub-mallikatalogia](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Lisätietoa löydät aloituksesta kohdassa [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Leikkikenttä**  
Jokaisella mallilla on oma [leikkikenttä mallin testaamiseen](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi Hugging Facessa

Mallin löydät myös [Hugging Face -sivustolta](https://huggingface.co/microsoft)

**Leikkikenttä**  
[Hugging Chat -leikkikenttä](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 Muut kurssit

Tiimimme tuottaa myös muita kursseja! Tutustu:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain  
[![LangChain4j aloittelijoille](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)  
[![LangChain.js aloittelijoille](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agentit  
[![AZD aloittelijoille](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Edge AI aloittelijoille](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![MCP aloittelijoille](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI-agentit aloittelijoille](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Generatiivinen AI -sarja  
[![Generatiivinen AI aloittelijoille](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Generatiivinen AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
[![Generatiivinen AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)  
[![Generatiivinen AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### Perusopetus  
[![ML aloittelijoille](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
[![Data-analytiikka aloittelijoille](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI aloittelijoille](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
[![Kyberturvallisuus aloittelijoille](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)  
[![Web-kehitys aloittelijoille](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
[![IoT aloittelijoille](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
[![XR-kehitys aloittelijoille](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Copilot-sarja  
[![Copilot AI-pariohjelmoinnissa](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
[![Copilot C#/.NET:lle](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Vastuullinen AI

Microsoft sitoutuu auttamaan asiakkaitaan käyttämään tekoälytuotteitamme vastuullisesti, jakamaan oppejamme ja rakentamaan luottamukseen perustuvia kumppanuuksia työkaluilla kuten Transparency Notes ja Impact Assessments. Monet näistä resursseista löytyvät osoitteesta [https://aka.ms/RAI](https://aka.ms/RAI).  
Microsoftin vastuullisen tekoälyn lähestymistapa perustuu tekoälyperiaatteisiimme: oikeudenmukaisuus, luotettavuus ja turvallisuus, yksityisyys ja tietoturva, osallisuus, läpinäkyvyys ja vastuullisuus.

Laajamittaiset luonnollisen kielen, kuvan ja puheen mallit – kuten tässä näytteessä käytetyt – voivat käyttäytyä epäoikeudenmukaisesti, epäluotettavasti tai loukkaavasti, aiheuttaen haittaa. Ole hyvä ja tutustu [Azure OpenAI -palvelun Transparency Noteen](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) saadaksesi tietoa riskeistä ja rajoituksista.

Suositeltu tapa hallita näitä riskejä on sisällyttää arkkitehtuuriisi turvallisuusjärjestelmä, joka pystyy havaitsemaan ja estämään haitallista käyttäytymistä. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) tarjoaa riippumattoman suojakerroksen, joka pystyy havaitsemaan sovelluksissa ja palveluissa käyttäjien luoman ja tekoälyn tuottaman haitallisen sisällön. Azure AI Content Safety sisältää tekstin ja kuvan API:t, joiden avulla voit tunnistaa haitallista materiaalia. Azure AI Foundryn Content Safety -palvelussa voit tarkastella, tutkia ja kokeilla esimerkkikoodeja haitallisen sisällön tunnistamiseen eri muodoissa. Seuraava [aloitusopas](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ohjaa tekemään pyyntöjä palveluun.

Toinen huomioon otettava näkökulma on koko sovelluksen suorituskyky. Monimodaalisissa ja monimallipohjaisissa sovelluksissa suorituskyvyllä tarkoitetaan, että järjestelmä toimii odotustesi ja käyttäjiesi odotusten mukaisesti, mukaan lukien haitallisten tulosteiden välttäminen. On tärkeää arvioida koko sovelluksen suorituskykyä käyttäen [Suorituskyky- ja laatu- sekä riski- ja turvallisuusarvioijia](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Sinulla on myös mahdollisuus luoda ja arvioida [mukautetuilla arvioijilla](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).
Voit arvioida tekoälysovellustasi kehitysympäristössäsi käyttämällä [Azure AI Evaluation SDK:ta](https://microsoft.github.io/promptflow/index.html). Olipa käytössäsi testiaineisto tai kohde, generatiivisen tekoälysovelluksesi luomukset mitataan määrällisesti sisäänrakennettujen arvioijien tai vapaavalintaisten mukautettujen arvioijien avulla. Järjestelmän arvioinnin aloittamiseksi azure ai evaluation sdk:lla voit seurata [aloitusoppaan ohjeita](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kun suoritat arviointikierroksen, voit [visualisoida tulokset Azure AI Foundryssä](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Tavaranmerkit

Tämä projekti saattaa sisältää tavaramerkkejä tai logoja projekteista, tuotteista tai palveluista. Microsoftin tavaramerkkien tai logojen luvallinen käyttö edellyttää Microsoftin tavaramerkki- ja brändiohjeiden [noudattamista](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Microsoftin tavaramerkkien tai logojen käyttö muokatuissa versioissa tästä projektista ei saa aiheuttaa sekaannusta tai antaa vaikutelmaa Microsoftin suosionosoituksesta. Kolmansien osapuolten tavaramerkkien tai logojen käyttö on näiden kolmansien osapuolten säädösten alaista.

## Apua saatavilla

Jos juutut tai sinulla on kysyttävää tekoälysovellusten rakentamisesta, liity:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Jos sinulla on tuotepalautetta tai kohtaat virheitä rakennusvaiheessa, käy:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä katsotaan viralliseksi lähteeksi. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->