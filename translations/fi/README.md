<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T13:57:56+00:00",
  "source_file": "README.md",
  "language_code": "fi"
}
-->
# Phi Cookbook: Käytännön esimerkkejä Microsoftin Phi-malleilla

Phi on Microsoftin kehittämä avoimen lähdekoodin tekoälymallien sarja.

Phi on tällä hetkellä tehokkain ja kustannustehokkain pieni kielimalli (SLM), joka saavuttaa erinomaisia tuloksia monikielisyydessä, päättelyssä, tekstin/chatin generoinnissa, koodauksessa, kuvissa, äänessä ja muissa skenaarioissa.

Voit ottaa Phi:n käyttöön pilvessä tai reunalaitteilla ja rakentaa helposti generatiivisia tekoälysovelluksia rajallisella laskentateholla.

Seuraa näitä ohjeita aloittaaksesi resurssien käytön:
1. **Haarauta arkisto**: Klikkaa [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Kloonaa arkisto**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Liity Microsoft AI Discord -yhteisöön ja tapaa asiantuntijoita sekä muita kehittäjiä**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 Monikielinen tuki

#### Tuettu GitHub Actionin kautta (automaattinen ja aina ajan tasalla)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) 
[Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](./README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)

## Sisällysluettelo

- Johdanto
  - [Tervetuloa Phi-perheeseen](./md/01.Introduction/01/01.PhiFamily.md)
  - [Ympäristön asennus](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Keskeisten teknologioiden ymmärtäminen](./md/01.Introduction/01/01.Understandingtech.md)
  - [Tekoälyn turvallisuus Phi-malleille](./md/01.Introduction/01/01.AISafety.md)
  - [Phi:n laitteistotuki](./md/01.Introduction/01/01.Hardwaresupport.md)
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
    - [Phi:n käyttö Apple MLX Frameworkilla](./md/01.Introduction/03/MLX_Inference.md)
    - [Phi:n käyttö paikallisessa palvelimessa](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Phi:n käyttö etäpalvelimessa AI Toolkitin avulla](./md/01.Introduction/03/Remote_Interence.md)
    - [Phi:n käyttö Rustilla](./md/01.Introduction/03/Rust_Inference.md)
    - [Phi--Visionin käyttö paikallisesti](./md/01.Introduction/03/Vision_Inference.md)
    - [Phi:n käyttö Kaito AKS:llä, Azure Containersilla (virallinen tuki)](./md/01.Introduction/03/Kaito_Inference.md)

- [Phi-perheen kvantifiointi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Phi-3.5 / 4:n kvantifiointi llama.cpp:llä](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Phi-3.5 / 4:n kvantifiointi Generative AI -laajennuksilla onnxruntimeen](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Phi-3.5 / 4:n kvantifiointi Intel OpenVINOn avulla](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Phi-3.5 / 4:n kvantifiointi Apple MLX Frameworkilla](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi:n arviointi
    - [Vastuullinen tekoäly](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry arviointiin](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow:n käyttö arviointiin](./md/01.Introduction/05/Promptflow.md)

- RAG Azure AI Searchin kanssa
    - [Kuinka käyttää Phi-4-miniä ja Phi-4-multimodal (RAG) Azure AI Searchin kanssa](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi-sovelluskehityksen esimerkit
  - Teksti- ja chat-sovellukset
    - Phi-4-esimerkit 🆕
      - [📓] [Chat Phi-4-mini ONNX-mallin kanssa](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chat Phi-4 paikallisen ONNX-mallin kanssa .NET:ssä](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Chat .NET-konsolisovellus Phi-4 ONNX:llä käyttäen Semantic Kernelia](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5-esimerkit
      - [Paikallinen chatbot selaimessa käyttäen Phi3:a, ONNX Runtime Webiä ja WebGPU:ta](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Monimalli - Interaktiivinen Phi-3-mini ja OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Rakentaminen wrapperille ja Phi-3:n käyttö MLFlow:ssa](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Mallin optimointi - Kuinka optimoida Phi-3-min-malli ONNX Runtime Webille Olive:n avulla](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3-sovellus Phi-3 mini-4k-instruct-onnx:llä](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3 Monimalli AI Powered Notes App -esimerkki](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Hienosäätö ja mukautettujen Phi-3-mallien integrointi Prompt Flow -työkaluun](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Hienosäätö ja mukautettujen Phi-3-mallien integrointi Prompt Flow -työkaluun Azure AI Foundryssa](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Hienosäädetyn Phi-3 / Phi-3.5-mallin arviointi Azure AI Foundryssa keskittyen Microsoftin vastuullisen tekoälyn periaatteisiin](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct kieliennusteen esimerkki (kiina/englanti)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU:n käyttö Prompt Flow -ratkaisun luomiseen Phi-3.5-Instruct ONNX:llä](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tflite:n käyttö Android-sovelluksen luomiseen](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Kysymys-vastaus .NET-esimerkki paikallisella ONNX Phi-3-mallilla käyttäen Microsoft.ML.OnnxRuntimea](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Konsolichat .NET-sovellus Semantic Kernelillä ja Phi-3:lla](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK -koodiesimerkit 
  - Phi-4 Esimerkit 🆕
    - [📓] [Projektikoodin generointi Phi-4-multimodalilla](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5 Esimerkit
    - [Luo oma Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 -perheellä](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [Luo oma Visual Studio Code Chat Copilot Agent Phi-3.5:llä GitHub-malleilla](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- Kehittyneet päättelyesimerkit
  - Phi-4 Esimerkit 🆕
    - [📓] [Phi-4-mini-reasoning tai Phi-4-reasoning esimerkit](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Phi-4-mini-reasoning hienosäätö Microsoft Olivella](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning hienosäätö Apple MLX:llä](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning GitHub-malleilla](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Phi-4-mini-reasoning Azure AI Foundry -malleilla](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- Demot
    - [Phi-4-mini demot Hugging Face Spaces -alustalla](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Phi-4-multimodal demot Hugging Face Spaces -alustalla](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- Näköesimerkit
  - Phi-4 Esimerkit 🆕
    - [📓] [Phi-4-multimodal käyttö kuvien lukemiseen ja koodin generointiin](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Phi-3 / 3.5 Esimerkit
    - [📓][Phi-3-vision-Kuvan tekstistä tekstiin](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP upotus](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [DEMO: Phi-3 Kierrätys](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Visuaalinen kieliavustaja - Phi3-Visionilla ja OpenVINolla](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision monikehys- tai monikuvaesimerkki](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Phi-3 Vision Paikallinen ONNX-malli käyttäen Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Valikkopohjainen Phi-3 Vision Paikallinen ONNX-malli käyttäen Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

- Matematiikkaesimerkit
  - Phi-4-Mini-Flash-Reasoning-Instruct Esimerkit 🆕 [Matematiikkademo Phi-4-Mini-Flash-Reasoning-Instructilla](../../md/02.Application/09.Math/MathDemo.ipynb)

- Ääniesimerkit
  - Phi-4 Esimerkit 🆕
    - [📓] [Äänitranskriptien poiminta Phi-4-multimodalilla](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodal Ääniesimerkki](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal Puheen käännösesimerkki](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET-konsolisovellus Phi-4-multimodalilla äänen analysointiin ja transkriptin luomiseen](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOE Esimerkit
  - Phi-3 / 3.5 Esimerkit
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) Sosiaalisen median esimerkki](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [Hakupohjaisen generoinnin (RAG) putkiston rakentaminen NVIDIA NIM Phi-3 MOE:lla, Azure AI Searchilla ja LlamaIndexillä](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- Funktiokutsuesimerkit
  - Phi-4 Esimerkit 🆕
    - [📓] [Funktiokutsujen käyttö Phi-4-minillä](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Funktiokutsujen käyttö monen agentin luomiseen Phi-4-minillä](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Funktiokutsujen käyttö Ollamalla](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [Funktiokutsujen käyttö ONNX:llä](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- Multimodaalinen yhdistelyesimerkit
  - Phi-4 Esimerkit 🆕
    - [📓] [Phi-4-multimodal käyttö teknologiajournalistina](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET-konsolisovellus Phi-4-multimodalilla kuvien analysointiin](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi-mallien hienosäätöesimerkit
  - [Hienosäätötilanteet](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Hienosäätö vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Hienosäätö: Anna Phi-3:n tulla alan asiantuntijaksi](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Phi-3:n hienosäätö AI Toolkitilla VS Codessa](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Phi-3:n hienosäätö Azure Machine Learning -palvelulla](./md/03.FineTuning/Introduce_AzureML.md)
  - [Phi-3:n hienosäätö Loralla](./md/03.FineTuning/FineTuning_Lora.md)
  - [Phi-3:n hienosäätö QLoralla](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Phi-3:n hienosäätö Azure AI Foundrylla](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Phi-3:n hienosäätö Azure ML CLI/SDK:llä](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Hienosäätö Microsoft Olivella](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Hienosäätö Microsoft Olive Hands-On Labilla](./md/03.FineTuning/olive-lab/readme.md)
  - [Phi-3-visionin hienosäätö Weights and Biasilla](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Phi-3:n hienosäätö Apple MLX Frameworkilla](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-visionin hienosäätö (virallinen tuki)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Phi-3:n hienosäätö Kaito AKS:llä, Azure Containersilla (virallinen tuki)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3:n ja 3.5 Visionin hienosäätö](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands-on Lab
  - [Tutustuminen huippumalleihin: LLM:t, SLM:t, paikallinen kehitys ja paljon muuta](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP:n potentiaalin avaaminen: Hienosäätö Microsoft Olivella](https://github.com/azure/Ignite_FineTuning_workshop)

- Akateemiset tutkimuspaperit ja julkaisut
  - [Textbooks Are All You Need II: phi-1.5 tekninen raportti](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Tekninen raportti: Erittäin kyvykäs kielimalli paikallisesti puhelimellasi](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Tekninen raportti](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Tekninen raportti: Kompakti mutta tehokas multimodaalinen kielimalli Mixture-of-LoRAs-menetelmällä](https://arxiv.org/abs/2503.01743)
  - [Pienten kielimallien optimointi ajoneuvon funktiokutsuille](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Phi-3:n hienosäätö monivalintakysymysten vastaamiseen: Metodologia, tulokset ja haasteet](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning Tekninen Raportti](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning Tekninen Raportti](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)  

## Phi-mallien käyttö  

### Phi Azure AI Foundryssa  

Voit oppia käyttämään Microsoft Phi -malleja ja rakentamaan E2E-ratkaisuja eri laitteillesi. Kokeile Phi-malleja itse ja mukauta niitä omiin käyttötarkoituksiisi käyttämällä [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Lisätietoja saat [Azure AI Foundry Aloitusoppaasta](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).  

**Playground**  
Jokaisella mallilla on oma testialusta [Azure AI Playground](https://aka.ms/try-phi3).  

### Phi GitHub-malleissa  

Voit oppia käyttämään Microsoft Phi -malleja ja rakentamaan E2E-ratkaisuja eri laitteillesi. Kokeile Phi-malleja itse ja mukauta niitä omiin käyttötarkoituksiisi käyttämällä [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Lisätietoja saat [GitHub Model Catalog Aloitusoppaasta](/md/02.QuickStart/GitHubModel_QuickStart.md).  

**Playground**  
Jokaisella mallilla on oma [testialusta](/md/02.QuickStart/GitHubModel_QuickStart.md).  

### Phi Hugging Facessa  

Voit myös löytää mallin [Hugging Facesta](https://huggingface.co/microsoft).  

**Playground**  
[Hugging Chat testialusta](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct).  

## Vastuullinen AI  

Microsoft on sitoutunut auttamaan asiakkaitaan käyttämään AI-tuotteitamme vastuullisesti, jakamaan oppimiamme asioita ja rakentamaan luottamukseen perustuvia kumppanuuksia työkalujen, kuten Transparency Notes ja Impact Assessments, avulla. Monet näistä resursseista löytyvät osoitteesta [https://aka.ms/RAI](https://aka.ms/RAI).  
Microsoftin lähestymistapa vastuulliseen AI:hin perustuu AI-periaatteisiimme: oikeudenmukaisuus, luotettavuus ja turvallisuus, yksityisyys ja tietoturva, osallisuus, läpinäkyvyys ja vastuuvelvollisuus.  

Laajamittaiset luonnollisen kielen, kuvan ja puheen mallit - kuten tässä esimerkissä käytetyt - voivat mahdollisesti käyttäytyä epäoikeudenmukaisesti, epäluotettavasti tai loukkaavasti, mikä voi aiheuttaa haittaa. Tutustu [Azure OpenAI -palvelun Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) -dokumenttiin saadaksesi tietoa riskeistä ja rajoituksista.  

Suositeltu tapa näiden riskien lieventämiseksi on sisällyttää turvallisuusjärjestelmä arkkitehtuuriisi, joka voi havaita ja estää haitallisen käyttäytymisen. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) tarjoaa itsenäisen suojakerroksen, joka pystyy havaitsemaan haitallista käyttäjien tai AI:n tuottamaa sisältöä sovelluksissa ja palveluissa. Azure AI Content Safety sisältää tekstin ja kuvan API:t, joiden avulla voit havaita haitallista materiaalia. Azure AI Foundryssa Content Safety -palvelu mahdollistaa haitallisen sisällön havaitsemisen eri muodoissa ja tarjoaa esimerkkikoodia kokeiltavaksi. Seuraava [aloitusopas](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) opastaa palvelupyyntöjen tekemisessä.  

Toinen huomioon otettava näkökohta on sovelluksen yleinen suorituskyky. Monimodaalisissa ja monimalliratkaisuissa suorituskyky tarkoittaa, että järjestelmä toimii odotetusti, mukaan lukien haitallisten tulosten estäminen. On tärkeää arvioida sovelluksesi suorituskykyä käyttämällä [Performance and Quality ja Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Voit myös luoda ja arvioida [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).  

Voit arvioida AI-sovellustasi kehitysympäristössäsi käyttämällä [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Testidatan tai tavoitteen avulla generatiivisen AI-sovelluksesi tuotoksia mitataan kvantitatiivisesti sisäänrakennetuilla tai valitsemillasi mukautetuilla arviointityökaluilla. Aloittaaksesi Azure AI Evaluation SDK:n käytön järjestelmäsi arvioimiseksi, voit seurata [aloitusopasta](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kun suoritat arviointikierroksen, voit [visualisoida tulokset Azure AI Foundryssa](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).  

## Tavaramerkit  

Tämä projekti saattaa sisältää tavaramerkkejä tai logoja projekteille, tuotteille tai palveluille. Microsoftin tavaramerkkien tai logojen käyttö on sallittua vain Microsoftin [Tavaramerkki- ja Brändiohjeiden](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) mukaisesti.  
Microsoftin tavaramerkkien tai logojen käyttö muokatuissa projektiversioissa ei saa aiheuttaa sekaannusta tai antaa ymmärtää, että Microsoft sponsoroi projektia. Kolmannen osapuolen tavaramerkkien tai logojen käyttö on kyseisten osapuolten politiikkojen alaista.  

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.