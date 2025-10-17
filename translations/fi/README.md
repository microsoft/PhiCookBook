<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4987daf30687ad3850757c9eae3f5411",
  "translation_date": "2025-10-17T10:26:50+00:00",
  "source_file": "README.md",
  "language_code": "fi"
}
-->
# Phi Cookbook: Käytännön esimerkkejä Microsoftin Phi-malleista

[![Avaa ja käytä esimerkkejä GitHub Codespacesissa](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Avaa Dev Containersissa](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHubin avustajat](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubin ongelmat](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubin pull-pyynnöt](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![Pull-pyynnöt tervetulleita](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHubin seuraajat](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubin haarukat](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubin tähdet](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi on Microsoftin kehittämä avoimen lähdekoodin tekoälymallien sarja.

Phi on tällä hetkellä tehokkain ja kustannustehokkain pieni kielimalli (SLM), joka saavuttaa erinomaisia tuloksia monikielisyydessä, päättelyssä, tekstin/chatin generoinnissa, koodauksessa, kuvissa, äänessä ja muissa skenaarioissa.

Voit ottaa Phin käyttöön pilvessä tai reunalaitteilla, ja voit helposti rakentaa generatiivisia tekoälysovelluksia rajallisella laskentateholla.

Seuraa näitä vaiheita aloittaaksesi näiden resurssien käytön:
1. **Haarukoi arkisto**: Klikkaa [![GitHubin haarukat](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Kloonaa arkisto**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Liity Microsoft AI Discord -yhteisöön ja tapaa asiantuntijoita sekä muita kehittäjiä**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![kansi](../../imgs/cover.png)

### 🌐 Monikielinen tuki

#### Tuettu GitHub Actionin kautta (automaattinen ja aina ajan tasalla)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabia](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaria](../bg/README.md) | [Burma (Myanmar)](../my/README.md) | [Kiina (yksinkertaistettu)](../zh/README.md) | [Kiina (perinteinen, Hongkong)](../hk/README.md) | [Kiina (perinteinen, Macao)](../mo/README.md) | [Kiina (perinteinen, Taiwan)](../tw/README.md) | [Kroatia](../hr/README.md) | [Tšekki](../cs/README.md) | [Tanska](../da/README.md) | [Hollanti](../nl/README.md) | [Viro](../et/README.md) | [Suomi](./README.md) | [Ranska](../fr/README.md) | [Saksa](../de/README.md) | [Kreikka](../el/README.md) | [Heprea](../he/README.md) | [Hindi](../hi/README.md) | [Unkari](../hu/README.md) | [Indonesia](../id/README.md) | [Italia](../it/README.md) | [Japani](../ja/README.md) | [Korea](../ko/README.md) | [Liettua](../lt/README.md) | [Malaiji](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norja](../no/README.md) | [Persia (Farsi)](../fa/README.md) | [Puola](../pl/README.md) | [Portugali (Brasilia)](../br/README.md) | [Portugali (Portugali)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romania](../ro/README.md) | [Venäjä](../ru/README.md) | [Serbia (kyrillinen)](../sr/README.md) | [Slovakki](../sk/README.md) | [Slovenia](../sl/README.md) | [Espanja](../es/README.md) | [Swahili](../sw/README.md) | [Ruotsi](../sv/README.md) | [Tagalog (Filippiinit)](../tl/README.md) | [Tamili](../ta/README.md) | [Thai](../th/README.md) | [Turkki](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnam](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Sisällysluettelo

- Johdanto
  - [Tervetuloa Phi-perheeseen](./md/01.Introduction/01/01.PhiFamily.md)
  - [Ympäristön asennus](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Keskeisten teknologioiden ymmärtäminen](./md/01.Introduction/01/01.Understandingtech.md)
  - [Tekoälyn turvallisuus Phi-malleille](./md/01.Introduction/01/01.AISafety.md)
  - [Phi-laitteistotuki](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi-mallit ja saatavuus eri alustoilla](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai ja Phi:n käyttö](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace -mallit](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- Phi:n käyttö eri ympäristöissä
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub-mallit](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi-perheen käyttö
    - [Phi:n käyttö iOS:ssä](./md/01.Introduction/03/iOS_Inference.md)
    - [Phi:n käyttö Androidissa](./md/01.Introduction/03/Android_Inference.md)
    - [Phi:n käyttö Jetsonissa](./md/01.Introduction/03/Jetson_Inference.md)
    - [Phi:n käyttö AI PC:ssä](./md/01.Introduction/03/AIPC_Inference.md)
    - [Phi:n käyttö Apple MLX Frameworkin kanssa](./md/01.Introduction/03/MLX_Inference.md)
    - [Phi:n käyttö paikallisessa palvelimessa](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Phi:n käyttö etäpalvelimessa AI Toolkitin avulla](./md/01.Introduction/03/Remote_Interence.md)
    - [Phi:n käyttö Rustin kanssa](./md/01.Introduction/03/Rust_Inference.md)
    - [Phi--Visionin käyttö paikallisesti](./md/01.Introduction/03/Vision_Inference.md)
    - [Phi:n käyttö Kaito AKS:n ja Azure Containersin kanssa (virallinen tuki)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi-perheen kvantifiointi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Phi-3.5 / 4:n kvantifiointi käyttämällä llama.cpp:tä](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Phi-3.5 / 4:n kvantifiointi käyttämällä generatiivisia tekoälylaajennuksia onnxruntimeen](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Phi-3.5 / 4:n kvantifiointi käyttämällä Intel OpenVINOa](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Phi-3.5 / 4:n kvantifiointi käyttämällä Apple MLX Frameworkia](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi:n arviointi
    - [Vastuullinen tekoäly](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry arviointiin](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow:n käyttö arviointiin](./md/01.Introduction/05/Promptflow.md)
 
- RAG Azure AI Searchin kanssa
    - [Kuinka käyttää Phi-4-miniä ja Phi-4-multimodal (RAG) Azure AI Searchin kanssa](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi-sovelluskehityksen esimerkit
  - Teksti- ja chat-sovellukset
    - Phi-4 esimerkit 🆕
      - [📓] [Chat Phi-4-mini ONNX-mallin kanssa](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat Phi-4 paikallisen ONNX-mallin kanssa .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Chat .NET konsolisovellus Phi-4 ONNX:n kanssa käyttäen Semantic Kernelia](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 esimerkit
      - [Paikallinen chatbot selaimessa käyttäen Phi3:a, ONNX Runtime Webiä ja WebGPU:ta](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Monimalli - Interaktiivinen Phi-3-mini ja OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Kuinka rakentaa wrapper ja käyttää Phi-3:a MLFlow:n kanssa](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Mallin optimointi - Kuinka optimoida Phi-3-min-malli ONNX Runtime Webille Olive:n avulla](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [WinUI3-sovellus Phi-3 mini-4k-instruct-onnx:lla](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [WinUI3 Multi Model AI Powered Notes App -esimerkkisovellus](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Hienosäätö ja mukautettujen Phi-3-mallien integrointi Prompt flow:n avulla](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Hienosäätö ja mukautettujen Phi-3-mallien integrointi Prompt flow:n avulla Azure AI Foundryssa](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Hienosäädetyn Phi-3 / Phi-3.5-mallin arviointi Azure AI Foundryssa keskittyen Microsoftin vastuullisen AI:n periaatteisiin](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct kieliennusteen esimerkkisovellus (kiina/englanti)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU:n käyttö Prompt flow -ratkaisun luomiseen Phi-3.5-Instruct ONNX:lla](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tflite:n käyttö Android-sovelluksen luomiseen](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Kysymys-vastaus .NET-esimerkki paikallisen ONNX Phi-3-mallin avulla käyttäen Microsoft.ML.OnnxRuntimea](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Konsolichat .NET-sovellus Semantic Kernelin ja Phi-3:n kanssa](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK -koodipohjaiset esimerkit
  - Phi-4-esimerkit 🆕
    - [📓] [Projektikoodin generointi Phi-4-multimodalilla](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5-esimerkit
    - [Luo oma Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 -perheen avulla](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [Luo oma Visual Studio Code Chat Copilot Agent Phi-3.5:n avulla GitHub-malleilla](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- Kehittyneet päättelyesimerkit
  - Phi-4-esimerkit 🆕
    - [📓] [Phi-4-mini-reasoning tai Phi-4-reasoning -esimerkit](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Phi-4-mini-reasoning -hienosäätö Microsoft Oliven avulla](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning -hienosäätö Apple MLX:n avulla](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning GitHub-malleilla](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Phi-4-mini-reasoning Azure AI Foundry -malleilla](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- Demot
    - [Phi-4-mini-demot Hugging Face Spaces -alustalla](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Phi-4-multimodal-demot Hugging Face Spaces -alustalla](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- Näköesimerkit
  - Phi-4-esimerkit 🆕
    - [📓] [Phi-4-multimodalilla kuvien lukeminen ja koodin generointi](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Phi-3 / 3.5-esimerkit
    - [📓][Phi-3-vision-kuvateksti tekstiksi](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP -upotus](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [DEMO: Phi-3 kierrätys](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Visuaalinen kieliavustaja - Phi3-Visionin ja OpenVINOn avulla](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision monikehys- tai monikuvaesimerkki](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Phi-3 Vision paikallinen ONNX-malli käyttäen Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Valikkopohjainen Phi-3 Vision paikallinen ONNX-malli käyttäen Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

- Matematiikkaesimerkit
  - Phi-4-Mini-Flash-Reasoning-Instruct-esimerkit 🆕 [Matematiikkademo Phi-4-Mini-Flash-Reasoning-Instructilla](../../md/02.Application/09.Math/MathDemo.ipynb)

- Ääniesimerkit
  - Phi-4-esimerkit 🆕
    - [📓] [Äänitranskriptien poiminta Phi-4-multimodalilla](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodal-ääniesimerkki](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal puheen käännösesimerkki](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET-konsolisovellus Phi-4-multimodal-äänellä äänen analysointiin ja transkriptin luomiseen](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOE-esimerkit
  - Phi-3 / 3.5-esimerkit
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) -esimerkki sosiaalisen median kanssa](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [Retrieval-Augmented Generation (RAG) -putken rakentaminen NVIDIA NIM Phi-3 MOE:lla, Azure AI Searchilla ja LlamaIndexillä](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- Funktiokutsuesimerkit
  - Phi-4-esimerkit 🆕
    - [📓] [Funktiokutsujen käyttö Phi-4-minin kanssa](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Funktiokutsujen käyttö monen agentin luomiseen Phi-4-minin kanssa](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Funktiokutsujen käyttö Ollaman kanssa](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [Funktiokutsujen käyttö ONNX:n kanssa](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- Multimodaalinen yhdistelyesimerkit
  - Phi-4-esimerkit 🆕
    - [📓] [Phi-4-multimodal teknologian journalistina](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET-konsolisovellus Phi-4-multimodalilla kuvien analysointiin](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi-hienosäätöesimerkit
  - [Hienosäätötilanteet](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Hienosäätö vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Hienosäätö: Anna Phi-3:n tulla alan asiantuntijaksi](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Phi-3:n hienosäätö AI Toolkitilla VS Codea varten](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Phi-3:n hienosäätö Azure Machine Learning Servicen avulla](./md/03.FineTuning/Introduce_AzureML.md)
  - [Phi-3:n hienosäätö Loran avulla](./md/03.FineTuning/FineTuning_Lora.md)
  - [Phi-3:n hienosäätö QLoran avulla](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Phi-3:n hienosäätö Azure AI Foundryssa](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Phi-3:n hienosäätö Azure ML CLI/SDK:lla](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Hienosäätö Microsoft Oliven avulla](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Hienosäätö Microsoft Olive Hands-On Labissa](./md/03.FineTuning/olive-lab/readme.md)
  - [Phi-3-visionin hienosäätö Weights and Biasin avulla](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Phi-3:n hienosäätö Apple MLX Frameworkilla](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-visionin hienosäätö (virallinen tuki)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Phi-3:n ja 3.5 Visionin hienosäätö Kaito AKS:lla, Azure Containersilla (virallinen tuki)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3:n ja 3.5 Visionin hienosäätö](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands-On Lab
  - [Tutustuminen huippumalleihin: LLM:t, SLM:t, paikallinen kehitys ja paljon muuta](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP:n potentiaalin avaaminen: Hienosäätö Microsoft Oliven avulla](https://github.com/azure/Ignite_FineTuning_workshop)

- Akateemiset tutkimuspaperit ja julkaisut
  - [Textbooks Are All You Need II: phi-1.5 tekninen raportti](https://arxiv.org/abs/2309.05463)
  - [Phi-3 tekninen raportti: Erittäin kyvykäs kielimalli paikallisesti puhelimellasi](https://arxiv.org/abs/2404.14219)
  - [Phi-4 tekninen raportti](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini tekninen raportti: Kompaktit mutta tehokkaat multimodaaliset kielimallit Mixture-of-LoRAs:n avulla](https://arxiv.org/abs/2503.01743)
  - [Pienten kielimallien optimointi ajoneuvojen toimintojen kutsumiseen](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3:n hienosäätö monivalintakysymysten vastaamiseen: menetelmät, tulokset ja haasteet](https://arxiv.org/abs/2501.01588)
  - [Phi-4-päättelyn tekninen raportti](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-päättelyn tekninen raportti](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi-mallien käyttö

### Phi Azure AI Foundryssa

Voit oppia käyttämään Microsoft Phi -mallia ja rakentamaan E2E-ratkaisuja eri laitteillesi. Kokeile Phi-mallia itse ja mukauta sitä omiin tarpeisiisi käyttämällä [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Lisätietoja löydät [Azure AI Foundry -aloitusoppaasta](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Leikkikenttä**
Jokaisella mallilla on oma leikkikenttä, jossa voit testata mallia [Azure AI Playground](https://aka.ms/try-phi3).

### Phi GitHub-malleissa

Voit oppia käyttämään Microsoft Phi -mallia ja rakentamaan E2E-ratkaisuja eri laitteillesi. Kokeile Phi-mallia itse ja mukauta sitä omiin tarpeisiisi käyttämällä [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Lisätietoja löydät [GitHub Model Catalog -aloitusoppaasta](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Leikkikenttä**
Jokaisella mallilla on oma [leikkikenttä mallin testaamiseen](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi Hugging Facessa

Mallin löydät myös [Hugging Facesta](https://huggingface.co/microsoft).

**Leikkikenttä**
 [Hugging Chat -leikkikenttä](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Vastuullinen AI 

Microsoft on sitoutunut auttamaan asiakkaitaan käyttämään AI-tuotteitamme vastuullisesti, jakamaan oppimiamme asioita ja rakentamaan luottamukseen perustuvia kumppanuuksia työkalujen, kuten läpinäkyvyysmuistiinpanojen ja vaikutusarvioiden, avulla. Monet näistä resursseista löytyvät osoitteesta [https://aka.ms/RAI](https://aka.ms/RAI). Microsoftin lähestymistapa vastuulliseen AI:hin perustuu AI-periaatteisiimme, jotka ovat oikeudenmukaisuus, luotettavuus ja turvallisuus, yksityisyys ja tietoturva, osallisuus, läpinäkyvyys ja vastuuvelvollisuus.

Laajamittaiset luonnollisen kielen, kuvan ja puheen mallit - kuten tässä esimerkissä käytetyt - voivat mahdollisesti käyttäytyä epäoikeudenmukaisesti, epäluotettavasti tai loukkaavasti, mikä voi aiheuttaa haittaa. Tutustu [Azure OpenAI -palvelun läpinäkyvyysmuistiinpanoon](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) saadaksesi tietoa riskeistä ja rajoituksista.

Suositeltu tapa näiden riskien lieventämiseksi on sisällyttää turvallisuusjärjestelmä arkkitehtuuriin, joka voi havaita ja estää haitallisen käyttäytymisen. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) tarjoaa itsenäisen suojakerroksen, joka pystyy havaitsemaan haitallisen käyttäjien tuottaman ja AI:n tuottaman sisällön sovelluksissa ja palveluissa. Azure AI Content Safety sisältää teksti- ja kuva-API:t, joiden avulla voit havaita haitallista materiaalia. Azure AI Foundryssa Content Safety -palvelu mahdollistaa haitallisen sisällön havaitsemiseen liittyvän esimerkkikoodin tarkastelun, tutkimisen ja kokeilemisen eri muodoissa. Seuraava [aloitusopas](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) opastaa sinua tekemään pyyntöjä palvelulle.

Toinen huomioon otettava näkökohta on sovelluksen yleinen suorituskyky. Monimuotoisissa ja monimallisissa sovelluksissa suorituskyky tarkoittaa, että järjestelmä toimii odotetusti, mukaan lukien haitallisten tulosten välttäminen. On tärkeää arvioida sovelluksen yleistä suorituskykyä käyttämällä [suorituskyvyn ja laadun sekä riskien ja turvallisuuden arviointityökaluja](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Voit myös luoda ja arvioida [mukautettuja arviointityökaluja](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Voit arvioida AI-sovellustasi kehitysympäristössäsi käyttämällä [Azure AI Evaluation SDK:ta](https://microsoft.github.io/promptflow/index.html). Käyttämällä joko testidataa tai tavoitetta, generatiivisen AI-sovelluksesi tuotokset mitataan kvantitatiivisesti sisäänrakennetuilla tai valitsemillasi mukautetuilla arviointityökaluilla. Aloittaaksesi Azure AI Evaluation SDK:n käytön järjestelmäsi arviointiin, voit seurata [aloitusopasta](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kun suoritat arviointikierroksen, voit [visualisoida tulokset Azure AI Foundryssa](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## Tavaramerkit

Tämä projekti saattaa sisältää tavaramerkkejä tai logoja projekteille, tuotteille tai palveluille. Microsoftin tavaramerkkien tai logojen luvallinen käyttö on Microsoftin tavaramerkki- ja brändiohjeiden mukaista ja niitä on noudatettava [Microsoftin tavaramerkki- ja brändiohjeet](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Microsoftin tavaramerkkien tai logojen käyttö muokatuissa projektiversioissa ei saa aiheuttaa sekaannusta tai antaa ymmärtää, että Microsoft sponsoroi projektia. Kolmannen osapuolen tavaramerkkien tai logojen käyttö on kyseisten kolmansien osapuolten politiikkojen alaista.

## Apua saatavilla

Jos jäät jumiin tai sinulla on kysymyksiä AI-sovellusten rakentamisesta, liity:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Jos sinulla on tuotepalautetta tai virheitä sovelluksen rakentamisen aikana, käy:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.