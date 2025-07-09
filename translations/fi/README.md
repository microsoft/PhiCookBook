<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2e042b12a63c59931dc121c2c638bc58",
  "translation_date": "2025-07-09T18:30:22+00:00",
  "source_file": "README.md",
  "language_code": "fi"
}
-->
# Phi Cookbook: Käytännön esimerkkejä Microsoftin Phi-malleilla

[![Avaa ja käytä esimerkkejä GitHub Codespacesissa](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![Avaa Dev Containersissa](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHubin kontribuuttorit](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHubin ongelmat](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHubin pull-pyynnöt](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![PR:t tervetulleita](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHubin seuraajat](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHubin haarukat](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHubin tähdet](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi on Microsoftin kehittämä avoimen lähdekoodin tekoälymallien sarja.

Phi on tällä hetkellä tehokkain ja kustannustehokkain pieni kielimalli (SLM), jolla on erinomaiset tulokset monikielisyydessä, päättelyssä, tekstin/keskustelun generoinnissa, koodauksessa, kuvissa, äänissä ja muissa käyttötapauksissa.

Voit ottaa Phin käyttöön pilvessä tai reunalaitteissa, ja voit helposti rakentaa generatiivisia tekoälysovelluksia rajallisella laskentateholla.

Seuraa näitä ohjeita aloittaaksesi näiden resurssien käytön:  
1. **Forkkaa repositorio**: Klikkaa [![GitHubin haarukat](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **Kloonaa repositorio**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Liity Microsoft AI Discord -yhteisöön ja tapaa asiantuntijoita sekä muita kehittäjiä**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![kansi](../../imgs/cover.png)

## 🌐 Monikielinen tuki

### Tuettu GitHub Actionin kautta (automaattinen ja aina ajan tasalla)

[Ranska](../fr/README.md) | [Espanja](../es/README.md) | [Saksa](../de/README.md) | [Venäjä](../ru/README.md) | [Arabia](../ar/README.md) | [Persia (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Kiina (yksinkertaistettu)](../zh/README.md) | [Kiina (perinteinen, Macao)](../mo/README.md) | [Kiina (perinteinen, Hongkong)](../hk/README.md) | [Kiina (perinteinen, Taiwan)](../tw/README.md) | [Japani](../ja/README.md) | [Korea](../ko/README.md) | [Hindi](../hi/README.md)  
[Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portugali (Portugali)](../pt/README.md) | [Portugali (Brasilia)](../br/README.md) | [Italia](../it/README.md) | [Puola](../pl/README.md) | [Turkki](../tr/README.md) | [Kreikka](../el/README.md) | [Thai](../th/README.md) | [Ruotsi](../sv/README.md) | [Tanska](../da/README.md) | [Norja](../no/README.md) | [Suomi](./README.md) | [Hollanti](../nl/README.md) | [Heprea](../he/README.md) | [Vietnam](../vi/README.md) | [Indonesia](../id/README.md) | [Malaiji](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Unkari](../hu/README.md) | [Tšekki](../cs/README.md) | [Slovakki](../sk/README.md) | [Romania](../ro/README.md) | [Bulgaria](../bg/README.md) | [Serbia (kyrillinen)](../sr/README.md) | [Kroatia](../hr/README.md) | [Sloveeni](../sl/README.md)

## Sisällysluettelo

- Johdanto  
  - [Tervetuloa Phi-perheeseen](./md/01.Introduction/01/01.PhiFamily.md)  
  - [Ympäristön asennus](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [Keskeisten teknologioiden ymmärtäminen](./md/01.Introduction/01/01.Understandingtech.md)  
  - [Tekoälyn turvallisuus Phi-malleille](./md/01.Introduction/01/01.AISafety.md)  
  - [Phi-laitteistotuki](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [Phi-mallit ja saatavuus eri alustoilla](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [Guidance-ai:n ja Phin käyttö](./md/01.Introduction/01/01.Guidance.md)  
  - [GitHub Marketplace -mallit](https://github.com/marketplace/models)  
  - [Azure AI Model Catalog](https://ai.azure.com)

- Phi-päätelmät eri ympäristöissä  
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)  
    -  [GitHub-mallit](./md/01.Introduction/02/02.GitHubModel.md)  
    -  [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)  
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)  
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)  
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi-perheen päätelmät  
    - [Phi-päätelmät iOS:llä](./md/01.Introduction/03/iOS_Inference.md)  
    - [Phi-päätelmät Androidilla](./md/01.Introduction/03/Android_Inference.md)  
    - [Phi-päätelmät Jetsoneilla](./md/01.Introduction/03/Jetson_Inference.md)  
    - [Phi-päätelmät AI-PC:llä](./md/01.Introduction/03/AIPC_Inference.md)  
    - [Phi-päätelmät Apple MLX -kehyksellä](./md/01.Introduction/03/MLX_Inference.md)  
    - [Phi-päätelmät paikallisella palvelimella](./md/01.Introduction/03/Local_Server_Inference.md)  
    - [Phi-päätelmät etäpalvelimella AI Toolkitin avulla](./md/01.Introduction/03/Remote_Interence.md)  
    - [Phi-päätelmät Rustilla](./md/01.Introduction/03/Rust_Inference.md)  
    - [Phi-päätelmät – Vision paikallisesti](./md/01.Introduction/03/Vision_Inference.md)  
    - [Phi-päätelmät Kaito AKS:llä, Azure Containers (virallinen tuki)](./md/01.Introduction/03/Kaito_Inference.md)  
-  [Phi-perheen kvantisointi](./md/01.Introduction/04/QuantifyingPhi.md)  
    - [Phi-3.5 / 4 kvantisointi llama.cpp:llä](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
    - [Phi-3.5 / 4 kvantisointi Generative AI -laajennuksilla onnxruntimeen](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
    - [Phi-3.5 / 4 kvantisointi Intel OpenVINO:lla](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
    - [Phi-3.5 / 4 kvantisointi Apple MLX -kehyksellä](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi:n arviointi  
    - [Responsible AI](./md/01.Introduction/05/ResponsibleAI.md)  
    - [Azure AI Foundry arviointiin](./md/01.Introduction/05/AIFoundry.md)  
    - [Promptflow:n käyttö arvioinnissa](./md/01.Introduction/05/Promptflow.md)

- RAG Azure AI Searchin kanssa  
    - [Phi-4-mini ja Phi-4-multimodal (RAG) käyttö Azure AI Searchin kanssa](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi-sovelluskehityksen esimerkit  
  - Teksti- ja keskustelusovellukset  
    - Phi-4-esimerkit 🆕  
      - [📓] [Keskustele Phi-4-mini ONNX -mallin kanssa](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Keskustele Phi-4 paikallisen ONNX-mallin kanssa .NET:llä](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [Keskustelu .NET-konsolisovelluksella Phi-4 ONNX:llä käyttäen Semantic Kernelia](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 -esimerkit  
      - [Paikallinen chatbot selaimessa käyttäen Phi3:ta, ONNX Runtime Webiä ja WebGPU:ta](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [Monimalli – interaktiivinen Phi-3-mini ja OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow – Wrapperin rakentaminen ja Phi-3:n käyttö MLFlow’n kanssa](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [Mallin optimointi – Kuinka optimoida Phi-3-mini-malli ONNX Runtime Webille Olive-työkalulla](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [WinUI3-sovellus Phi-3 mini-4k-instruct-onnx:lla](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [WinUI3 monimalli tekoälyllä toimiva muistiinpanosovellus – esimerkki](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Hienosäädä ja integroi mukautetut Phi-3-mallit Prompt flow'n kanssa](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Hienosäädä ja integroi mukautetut Phi-3-mallit Prompt flow'n kanssa Azure AI Foundryssa](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Arvioi hienosäädetty Phi-3 / Phi-3.5 -malli Azure AI Foundryssa keskittyen Microsoftin vastuullisen tekoälyn periaatteisiin](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct kieliennusteen esimerkki (kiina/englanti)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU:n käyttö Prompt flow -ratkaisun luomiseen Phi-3.5-Instruct ONNX:n kanssa](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tflite:n käyttö Android-sovelluksen luomiseen](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Q&A .NET-esimerkki paikallisella ONNX Phi-3 -mallilla käyttäen Microsoft.ML.OnnxRuntimea](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Konsolipohjainen chat .NET-sovellus Semantic Kernelin ja Phi-3:n kanssa](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK:n koodipohjaiset esimerkit  
  - Phi-4-esimerkit 🆕  
    - [📓] [Projektikoodin generointi Phi-4-multimodalilla](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Phi-3 / 3.5 -esimerkit  
    - [Rakenna oma Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 -perheen avulla](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [Luo oma Visual Studio Code Chat Copilot Agent Phi-3.5:llä GitHub-mallien avulla](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- Edistyneet päättelyesimerkit  
  - Phi-4-esimerkit 🆕  
    - [📓] [Phi-4-mini-päättely tai Phi-4-päättelyesimerkit](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Phi-4-mini-päättelyn hienosäätö Microsoft Oliven avulla](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Phi-4-mini-päättelyn hienosäätö Apple MLX:n avulla](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Phi-4-mini-päättely GitHub-mallien kanssa](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Phi-4-mini-päättely Azure AI Foundry -mallien kanssa](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- Demoja  
    - [Phi-4-mini-demoja Hugging Face Spacesissa](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Phi-4-multimodal-demoja Hugging Face Spacesissa](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- Vision-esimerkit  
  - Phi-4-esimerkit 🆕  
    - [📓] [Käytä Phi-4-multimodalia kuvien lukemiseen ja koodin generointiin](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Phi-3 / 3.5 -esimerkit  
    - [📓][Phi-3-vision-kuvateksti tekstiksi](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP -upotukset](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [DEMO: Phi-3 kierrätys](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision – visuaalinen kieliavustaja Phi3-Visionin ja OpenVINOn kanssa](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision monikehys- tai monikuvaesimerkki](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Phi-3 Vision paikallinen ONNX-malli Microsoft.ML.OnnxRuntime .NETillä](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Valikkopohjainen Phi-3 Vision paikallinen ONNX-malli Microsoft.ML.OnnxRuntime .NETillä](../../md/04.HOL/dotnet/src/LabsPhi304)

- Matematiikkaesimerkit  
  - Phi-4-Mini-Flash-Reasoning-Instruct -esimerkit 🆕 [Matematiikkademo Phi-4-Mini-Flash-Reasoning-Instructilla](../../md/02.Application/09.Math/MathDemo.ipynb)

- Ääniesimerkit  
  - Phi-4-esimerkit 🆕  
    - [📓] [Äänitallenteiden tekstitysten poiminta Phi-4-multimodalilla](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Phi-4-multimodal ääninäyte](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Phi-4-multimodal puheen käännösnäyte](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [.NET-konsolisovellus, joka käyttää Phi-4-multimodalia äänitiedoston analysointiin ja tekstityksen generointiin](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOE-esimerkit  
  - Phi-3 / 3.5 -esimerkit  
    - [📓] [Phi-3.5 Mixture of Experts (MoEs) sosiaalisen median esimerkki](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [Retrieval-Augmented Generation (RAG) -putken rakentaminen NVIDIA NIM Phi-3 MOE:n, Azure AI Searchin ja LlamaIndexin avulla](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- Funktiokutsuesimerkit  
  - Phi-4-esimerkit 🆕  
    - [📓] [Funktiokutsujen käyttö Phi-4-minin kanssa](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Funktiokutsujen käyttö moniagenttien luomiseen Phi-4-minin kanssa](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Funktiokutsujen käyttö Ollaman kanssa](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [Funktiokutsujen käyttö ONNX:n kanssa](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- Monimodaalisen yhdistämisen esimerkit  
  - Phi-4-esimerkit 🆕  
    - [📓] [Phi-4-multimodalin käyttö teknologiatoimittajana](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [.NET-konsolisovellus, joka käyttää Phi-4-multimodalia kuvien analysointiin](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi-mallien hienosäätö  
  - [Hienosäätötilanteet](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [Hienosäätö vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Anna Phi-3:n kehittyä alan asiantuntijaksi](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [Phi-3:n hienosäätö AI Toolkitin avulla VS Codessa](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Phi-3:n hienosäätö Azure Machine Learning Servicen avulla](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Phi-3:n hienosäätö Loralla](./md/03.FineTuning/FineTuning_Lora.md)  
  - [Phi-3:n hienosäätö QLoralla](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Phi-3:n hienosäätö Azure AI Foundryssa](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Phi-3:n hienosäätö Azure ML CLI/SDK:lla](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Hienosäätö Microsoft Oliven avulla](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Microsoft Oliven käytännön harjoitus](./md/03.FineTuning/olive-lab/readme.md)  
  - [Phi-3-vision hienosäätö Weights and Biasin avulla](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Phi-3:n hienosäätö Apple MLX Frameworkilla](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Phi-3-vision hienosäätö (virallinen tuki)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Phi-3:n hienosäätö Kaito AKS:lla, Azure Containers (virallinen tuki)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Phi-3 ja 3.5 Vision hienosäätö](https://github.com/2U1/Phi3-Vision-Finetune)

- Käytännön harjoitukset  
  - [Huippumallien tutkiminen: LLM:t, SLM:t, paikallinen kehitys ja muuta](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [NLP:n potentiaalin avaaminen: Hienosäätö Microsoft Oliven avulla](https://github.com/azure/Ignite_FineTuning_workshop)

- Akateemiset tutkimuspaperit ja julkaisut  
  - [Textbooks Are All You Need II: phi-1.5 tekninen raportti](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 tekninen raportti: erittäin kykenevä kielimalli paikallisesti puhelimellasi](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 tekninen raportti](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini tekninen raportti: kompakti mutta tehokas multimodaalinen kielimalli Mixture-of-LoRAs -menetelmällä](https://arxiv.org/abs/2503.01743)  
  - [Pienten kielimallien optimointi ajoneuvon funktiokutsuihin](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) PHI-3:n hienosäätö monivalintakysymysten vastaamiseen: menetelmät, tulokset ja haasteet](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning Technical Report](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning Technical Report](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi-mallien käyttö

### Phi Azure AI Foundryssa

Voit oppia, miten Microsoft Phiä käytetään ja miten rakennetaan E2E-ratkaisuja eri laitteillasi. Kokeillaksesi Phiä itse, aloita leikkimällä malleilla ja räätälöimällä Phiä omiin käyttötapauksiisi käyttämällä [Azure AI Foundry Azure AI Model Catalogia](https://aka.ms/phi3-azure-ai). Lisätietoja löydät oppaasta Getting Started with [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Playground**  
Jokaisella mallilla on oma testiympäristö mallin kokeilemiseen [Azure AI Playground](https://aka.ms/try-phi3).

### Phi GitHub-malleissa

Voit oppia, miten Microsoft Phiä käytetään ja miten rakennetaan E2E-ratkaisuja eri laitteillasi. Kokeillaksesi Phiä itse, aloita leikkimällä mallilla ja räätälöimällä Phiä omiin käyttötapauksiisi käyttämällä [GitHub Model Catalogia](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Lisätietoja löydät oppaasta Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Playground**  
Jokaisella mallilla on oma [testiympäristö mallin kokeilemiseen](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi Hugging Facessa

Mallin löydät myös [Hugging Facesta](https://huggingface.co/microsoft).

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Vastuullinen tekoäly

Microsoft on sitoutunut auttamaan asiakkaitaan käyttämään tekoälytuotteitamme vastuullisesti, jakamaan oppejamme ja rakentamaan luottamukseen perustuvia kumppanuuksia esimerkiksi Transparency Notes- ja Impact Assessments -työkalujen avulla. Monet näistä resursseista löytyvät osoitteesta [https://aka.ms/RAI](https://aka.ms/RAI).  
Microsoftin vastuullisen tekoälyn lähestymistapa perustuu tekoälyn periaatteisiimme: oikeudenmukaisuus, luotettavuus ja turvallisuus, yksityisyys ja tietoturva, osallisuus, läpinäkyvyys ja vastuullisuus.

Laajamittaiset luonnollisen kielen, kuvan ja puheen mallit – kuten tässä esimerkissä käytetyt – voivat käyttäytyä tavoilla, jotka ovat epäoikeudenmukaisia, epäluotettavia tai loukkaavia, aiheuttaen haittaa. Tutustu [Azure OpenAI -palvelun Transparency noteen](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) saadaksesi tietoa riskeistä ja rajoituksista.

Suositeltu tapa vähentää näitä riskejä on sisällyttää arkkitehtuuriisi turvajärjestelmä, joka pystyy havaitsemaan ja estämään haitallisen käytöksen. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) tarjoaa itsenäisen suojakerroksen, joka tunnistaa haitallisen käyttäjän tai tekoälyn tuottaman sisällön sovelluksissa ja palveluissa. Azure AI Content Safety sisältää tekstin ja kuvan API:t, joiden avulla voit havaita haitallista materiaalia. Azure AI Foundryssa Content Safety -palvelu mahdollistaa haitallisen sisällön tunnistamisen eri muodoissa, ja voit tutustua sekä kokeilla esimerkkikoodeja. Seuraava [quickstart-dokumentaatio](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) opastaa palvelupyynnön tekemisessä.

Toinen huomioon otettava seikka on sovelluksen kokonaisvaltainen suorituskyky. Monimodaalisissa ja monimallipohjaisissa sovelluksissa suorituskyvyllä tarkoitetaan sitä, että järjestelmä toimii odotetusti sinulta ja käyttäjiltäsi, mukaan lukien haitallisten tulosten välttäminen. On tärkeää arvioida sovelluksesi suorituskykyä käyttämällä [Performance and Quality sekä Risk and Safety -arvioijia](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Voit myös luoda ja arvioida [omilla arvioijilla](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Voit arvioida tekoälysovellustasi kehitysympäristössäsi käyttämällä [Azure AI Evaluation SDK:ta](https://microsoft.github.io/promptflow/index.html). Testidatan tai tavoitteen perusteella generatiivisen tekoälysovelluksesi tuotokset mitataan määrällisesti sisäänrakennetuilla tai omilla arvioijilla. Aloittaaksesi Azure AI Evaluation SDK:n käytön järjestelmäsi arviointiin, voit seurata [quickstart-opasta](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kun arviointiajo on suoritettu, voit [visualisoida tulokset Azure AI Foundryssa](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Tavara- ja palvelumerkit

Tämä projekti saattaa sisältää tavara- tai palvelumerkkejä tai logoja projekteista, tuotteista tai palveluista. Microsoftin tavara- ja palvelumerkkien tai logojen käyttö on sallittua vain Microsoftin tavara- ja brändiohjeiden [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) mukaisesti.  
Microsoftin tavara- ja palvelumerkkien tai logojen käyttö muokatuissa versioissa tästä projektista ei saa aiheuttaa sekaannusta tai antaa vaikutelmaa Microsoftin sponsoroimasta. Kolmansien osapuolten tavara- ja palvelumerkkien tai logojen käyttö on näiden osapuolten sääntöjen alaista.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.