# Phi-keittokirja: Käytännön esimerkkejä Microsoftin Phi-malleilla

[![Avaa ja käytä esimerkkejä GitHub Codespacesissa](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Avaa Dev Containersissa](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub-toimittajat](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub-ongelmat](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub vetopyynnöt](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![Vetopyynnöt tervetulleita](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub seuraajat](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub haarukat](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub tähdet](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi on Microsoftin kehittämä avoimen lähdekoodin tekoälymallien sarja.

Phi on tällä hetkellä tehokkain ja kustannustehokkain pieni kielimalli (SLM), jolla on erittäin hyvät vertailuarvot monikielisissä tehtävissä, päättelyssä, tekstin/ keskustelun generoinnissa, koodauksessa, kuvissa, äänessä ja muissa skenaarioissa.

Voit ottaa Phi:n käyttöön pilvessä tai reunalaitteissa, ja voit helposti rakentaa generatiivisia tekoälysovelluksia rajallisella laskentateholla.

Seuraa näitä vaiheita aloittaaksesi näiden resurssien käytön:
1. **Tee haarukka repositoriosta**: Klikkaa [![GitHub haarukat](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Kloonaa repositorio**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Liity Microsoftin AI Discord -yhteisöön ja tutustu asiantuntijoihin ja kehittäjätovereihin**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/fi/cover.eb18d1b9605d754b.webp)

### 🌐 Monikielituki

#### Tuettu GitHub Actionin kautta (automaattinen ja aina ajan tasalla)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[arabia](../ar/README.md) | [bengali](../bn/README.md) | [bulgaria](../bg/README.md) | [burman kieli (Myanmar)](../my/README.md) | [kiina (yksinkertaistettu)](../zh-CN/README.md) | [kiina (perinteinen, Hongkong)](../zh-HK/README.md) | [kiina (perinteinen, Macao)](../zh-MO/README.md) | [kiina (perinteinen, Taiwan)](../zh-TW/README.md) | [kroatia](../hr/README.md) | [tšekki](../cs/README.md) | [tanska](../da/README.md) | [hollanti](../nl/README.md) | [viro](../et/README.md) | [suomi](./README.md) | [ranska](../fr/README.md) | [saksa](../de/README.md) | [kreikka](../el/README.md) | [heprea](../he/README.md) | [hindi](../hi/README.md) | [unkari](../hu/README.md) | [indonesian kieli](../id/README.md) | [italia](../it/README.md) | [japani](../ja/README.md) | [kannada](../kn/README.md) | [khmer](../km/README.md) | [korea](../ko/README.md) | [liettua](../lt/README.md) | [malaiji](../ms/README.md) | [malayalam](../ml/README.md) | [marathi](../mr/README.md) | [nepali](../ne/README.md) | [nigerian pidgin](../pcm/README.md) | [norja](../no/README.md) | [persia (farsi)](../fa/README.md) | [puola](../pl/README.md) | [portugali (Brasilia)](../pt-BR/README.md) | [portugali (Portugali)](../pt-PT/README.md) | [pandžabi (Gurmukhi)](../pa/README.md) | [romania](../ro/README.md) | [venäjä](../ru/README.md) | [serbia (kyrillinen)](../sr/README.md) | [slovakki](../sk/README.md) | [sloveeni](../sl/README.md) | [espanja](../es/README.md) | [swahili](../sw/README.md) | [ruotsi](../sv/README.md) | [tagalog (filippiini)](../tl/README.md) | [tamili](../ta/README.md) | [telugu](../te/README.md) | [thai](../th/README.md) | [turkki](../tr/README.md) | [ukraina](../uk/README.md) | [urdu](../ur/README.md) | [vietnam](../vi/README.md)

> **Haluatko mieluummin kloonata paikallisesti?**
>
> Tämä repositorio sisältää yli 50 kielen käännökset, mikä lisää merkittävästi latauskokoa. Jos haluat kloonata ilman käännöksiä, käytä 'sparse checkout' -toimintoa:
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
> Näin saat kaiken tarvittavan kurssin suorittamiseen huomattavasti nopeammalla latauksella.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Sisällysluettelo
- Johdanto - [Tervetuloa Phi-perheeseen](./md/01.Introduction/01/01.PhiFamily.md) - [Ympäristön asetukset](./md/01.Introduction/01/01.EnvironmentSetup.md) - [Keskeisten teknologioiden ymmärtäminen](./md/01.Introduction/01/01.Understandingtech.md) - [AI:n turvallisuus Phi-malleille](./md/01.Introduction/01/01.AISafety.md) - [Phi-laitetuki](./md/01.Introduction/01/01.Hardwaresupport.md) - [Phi-mallit ja saatavuus eri alustoilla](./md/01.Introduction/01/01.Edgeandcloud.md) - [Guidance-ai:n ja Phin käyttö](./md/01.Introduction/01/01.Guidance.md) - [GitHub Marketplace -mallit](https://github.com/marketplace/models) - [Azure AI -malliluettelo](https://ai.azure.com) - Phi-inferencia eri ympäristöissä - [Hugging face](./md/01.Introduction/02/01.HF.md) - [GitHub-mallit](./md/01.Introduction/02/02.GitHubModel.md) - [Microsoft Foundry -malliluettelo](./md/01.Introduction/02/03.AzureAIFoundry.md) - [Ollama](./md/01.Introduction/02/04.Ollama.md) - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md) - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md) - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md) - Phi-perheen inferenssi - [Phi-inferencia iOS:ssä](./md/01.Introduction/03/iOS_Inference.md) - [Phi-inferencia Androidissa](./md/01.Introduction/03/Android_Inference.md) - [Phi-inferencia Jetsoneilla](./md/01.Introduction/03/Jetson_Inference.md) - [Phi-inferencia AI-PC:llä](./md/01.Introduction/03/AIPC_Inference.md) - [Phi-inferencia Apple MLX -kehyksen kanssa](./md/01.Introduction/03/MLX_Inference.md) - [Phi-inferencia paikallisella palvelimella](./md/01.Introduction/03/Local_Server_Inference.md) - [Phi-inferencia etäpalvelimella AI Toolkitin avulla](./md/01.Introduction/03/Remote_Interence.md) - [Phi-inferencia Rustin kanssa](./md/01.Introduction/03/Rust_Inference.md) - [Phi Vision -inferenssi paikallisesti](./md/01.Introduction/03/Vision_Inference.md) - [Phi-inferencia Kaito AKS:llä, Azure-konttien virallisella tuella](./md/01.Introduction/03/Kaito_Inference.md) - [Phi-perheen kvantisointi](./md/01.Introduction/04/QuantifyingPhi.md) - [Phi-3.5 / 4 -mallien kvantisointi llama.cpp:llä](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md) - [Phi-3.5 / 4 kvantisointi Generative AI -laajennuksilla onnxruntimeen](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md) - [Phi-3.5 / 4 kvantisointi Intel OpenVINOlla](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md) - [Phi-3.5 / 4 kvantisointi Apple MLX -kehyksen avulla](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md) - Phi-arviointi - [Vastuullinen AI](./md/01.Introduction/05/ResponsibleAI.md) - [Microsoft Foundry arviointiin](./md/01.Introduction/05/AIFoundry.md) - [Promptflow:n käyttö arviointiin](./md/01.Introduction/05/Promptflow.md) - RAG Azure AI Searchin kanssa - [Kuinka käyttää Phi-4-miniä ja Phi-4-multimodalia (RAG) Azure AI Searchin kanssa](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb) - Phi-sovelluskehitysesimerkit - Teksti- ja chat-sovellukset - Phi-4-esimerkit - [📓] [Chattaaminen Phi-4-mini ONNX -mallin kanssa](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md) - [Chat Phi-4 paikallisen ONNX-mallin kanssa .NETillä](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) - [Chat .NET Konsolisovellus Phi-4 ONNX:n kanssa käyttäen Semantic Kernel -kirjastoa](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) - Phi-3 / 3.5 -esimerkit - [Paikallinen chatbotti selaimessa käyttäen Phi3:sta, ONNX Runtime Webiä ja WebGPU:ta](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat) - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md) - [Monimalli - interaktiivinen Phi-3-mini ja OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md) - [MLFlow - Rakentaminen wrapperille ja Phi-3:n käyttö MLFlow:n kanssa](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md) - [Mallien optimointi - Kuinka optimoida Phi-3-minimalli ONNX Runtime Webille Olive-työkalulla](https://github.com/microsoft/Olive/tree/main/examples/phi3) - [WinUI3-sovellus Phi-3 mini-4k-instruct-onnx:lla](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/) -[WinUI3 monimalli AI-avusteinen muistiinpanosovellus](https://github.com/microsoft/ai-powered-notes-winui3-sample) - [Hienosäädä ja integroi mukautetut Phi-3-mallit Prompt flown avulla](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md) - [Hienosäädä ja integroi mukautetut Phi-3-mallit Prompt flown avulla Microsoft Foundryssa](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md) - [Arvioi hienosäädetty Phi-3 / Phi-3.5 malli Microsoft Foundryssa keskittyen Microsoftin vastuullisen tekoälyn periaatteisiin](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md) - [📓] [Phi-3.5-mini-instruct kieliennusteesimerkki (kiina/englanti)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb) - [Phi-3.5-Instruct WebGPU RAG chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md) - [Windows GPU:n käyttö Prompt flow -ratkaisun luomiseen Phi-3.5-Instruct ONNX:n kanssa](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md) - [Microsoft Phi-3.5 tfliten käyttö Android-sovelluksen luomisessa](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md) - [Q&A .NET-esimerkki paikallisella ONNX Phi-3 -mallilla käyttäen Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301) - [Konsoli chat .NET -sovellus Semantic Kernelin ja Phi-3:n kanssa](../../md/04.HOL/dotnet/src/LabsPhi302) - Azure AI Inferenssi SDK:n koodipohjaiset esimerkit - Phi-4-esimerkit - [📓] [Projektikoodin luominen Phi-4-multimodalilla](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md) - Phi-3 / 3.5 -esimerkit - [Rakenna oma Visual Studio Code GitHub Copilot Chat Microsoft Phi-3 -perheen kanssa](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md) - [Luo oma Visual Studio Code Chat Copilot Agent Phi-3.5:lla GitHub-malleilla](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md) - Edistyneet päättelyesimerkit - Phi-4-esimerkit - [📓] [Phi-4-mini-päättely- tai Phi-4-päättelyesimerkit](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md) - [📓] [Phi-4-mini-päättelyn hienosäätö Microsoft Olivella](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Phi-4-mini-päättelyn hienosäätö Apple MLX:llä](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Phi-4-mini-päättely GitHub-malleilla](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb) - [📓] [Phi-4-mini-päättely Microsoft Foundry -malleilla](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb) -
Demot - [Phi-4-mini-demot Hugging Face Spacesissa](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo) - [Phi-4-monimuotodemot Hugging Face Spacesissa](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo) - Näkymänäytteet - Phi-4-näytteet - [📓] [Käytä Phi-4-multimodaalia kuvien lukemiseen ja koodin generointiin](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) - Phi-3 / 3.5 -näytteet - [📓][Phi-3-vision-kuvateksti tekstiksi](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html) - [📓][Phi-3-vision CLIP -upotus](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [DEMO: Phi-3 kierrätys](https://github.com/jennifermarsman/PhiRecycling/) - [Phi-3-vision - Visuaalinen kieliavustaja - Phi3-Vision ja OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html) - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md) - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md) - [📓][Phi-3.5 Vision monikehys- tai moni-kuvannäyte](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb) - [Phi-3 Vision paikallinen ONNX-malli Microsoft.ML.OnnxRuntime .NET käyttöliittymällä](../../md/04.HOL/dotnet/src/LabsPhi303) - [Valikkopohjainen Phi-3 Vision paikallinen ONNX-malli Microsoft.ML.OnnxRuntime .NET käyttöliittymällä](../../md/04.HOL/dotnet/src/LabsPhi304) - Päättely-Näytteet - Phi-4-Päättely-Vision-15B - [📓] [Phi-4-Päättely-Vision-15B:n käyttö pikkutien ylityksen havaitsemiseen](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb) - [📓] [Phi-4-Päättely-Vision-15B:n käyttö matematiikassa](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb) - [📓] [Phi-4-Päättely-Vision-15B:n käyttö käyttöliittymän havaitsemiseen](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb) - Matematiikkamallit - Phi-4-Mini-Flash-Päättely-Ohje Näytteet [Matematiikka Demo Phi-4-Mini-Flash-Päättely-Ohjeella](./md/02.Application/09.Math/MathDemo.ipynb) - Ääni Näytteet - Phi-4 Näytteet - [📓] [Äänitallenteiden tekstityksen poiminta Phi-4-multimodaalilla](./md/02.Application/05.Audio/Phi4/Transciption/README.md) - [📓] [Phi-4-multimodaalinen ääni näyte](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb) - [📓] [Phi-4-multimodaalinen puheen kääntönäyte](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb) - [.NET-konsolisovellus Phi-4-multimodaalisen äänen analysointiin ja tekstityksen generointiin](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) - MOE Näytteet - Phi-3 / 3.5 Näytteet - [📓] [Phi-3.5 Eksperttien sekamallit (MoEs) sosiaalisen median näyte](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb) - [📓] [Haku- ja generointiputken rakentaminen NVIDIA NIM Phi-3 MOE:lla, Azure AI Searchilla ja LlamaIndexillä](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb) - - Funktiokutsun Näytteet - Phi-4 Näytteet 🆕 - [📓] [Funktiokutsujen käyttö Phi-4-mini kanssa](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md) - [📓] [Funktiokutsujen käyttö moniagenttien luomiseen Phi-4-mini kanssa](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb) - [📓] [Funktiokutsujen käyttö Ollaman kanssa](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb) - [📓] [Funktiokutsujen käyttö ONNX:n kanssa](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb) - Monimuotoinen sekoitus Näytteet - Phi-4 Näytteet 🆕 - [📓] [Phi-4-multimodaalin käyttö teknologiatoimittajana](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb) - [.NET-konsolisovellus Phi-4-multimodaalin kuvan analysointiin](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) - Hienosäätö Phi Näytteet - [Hienosäätötilanteet](./md/03.FineTuning/FineTuning_Scenarios.md) - [Hienosäätö vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md) - [Hienosäätö: Anna Phi-3:n tulla teollisuusasiantuntijaksi](./md/03.FineTuning/LetPhi3gotoIndustriy.md) - [Hienosäätö Phi-3:lla AI Toolkit VS Code -ympäristössä](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md) - [Hienosäätö Phi-3:lla Azure Machine Learning -palvelun avulla](./md/03.FineTuning/Introduce_AzureML.md) - [Hienosäätö Phi-3:lla Lora-menetelmällä](./md/03.FineTuning/FineTuning_Lora.md) - [Hienosäätö Phi-3:lla QLora-menetelmällä](./md/03.FineTuning/FineTuning_Qlora.md) - [Hienosäätö Phi-3:lla Microsoft Foundrylla](./md/03.FineTuning/FineTuning_AIFoundry.md) - [Hienosäätö Phi-3:lla Azure ML CLI/SDK:lla](./md/03.FineTuning/FineTuning_MLSDK.md) - [Hienosäätö Microsoft Olivella](./md/03.FineTuning/FineTuning_MicrosoftOlive.md) - [Hienosäätö Microsoft Olive Hands-On Labissa](./md/03.FineTuning/olive-lab/readme.md) - [Hienosäätö Phi-3-visionia Weights and Biasilla](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md) - [Hienosäätö Phi-3:lla Apple MLX -kehyksellä](./md/03.FineTuning/FineTuning_MLX.md) - [Hienosäätö Phi-3-visionilla (virallinen tuki)](./md/03.FineTuning/FineTuning_Vision.md) - [Hienosäätö Phi-3:lla Kaito AKS:lla, Azure Containers (virallinen tuki)](./md/03.FineTuning/FineTuning_Kaito.md) - [Hienosäätö Phi-3:lla ja 3.5 Visionilla](https://github.com/2U1/Phi3-Vision-Finetune) - Käytännön harjoitukset - [Huipputason mallien tutkimista: LLM:t, SLM:t, paikallinen kehitys ja muuta](https://github.com/microsoft/aitour-exploring-cutting-edge-models) - [NLP:n potentiaalin vapauttaminen: hienosäätö Microsoft Olivella](https://github.com/azure/Ignite_FineTuning_workshop) - Akateemiset tutkimuspaperit ja julkaisut - [Textbooks Are All You Need II: phi-1.5 tekninen raportti](https://arxiv.org/abs/2309.05463) - [Phi-3 Tekninen raportti: erittäin kykenevä kielimalli paikallisesti puhelimellasi](https://arxiv.org/abs/2404.14219) - [Phi-4 Tekninen raportti](https://arxiv.org/abs/2412.08905) - [Phi-4-Mini Tekninen raportti: Kompakti mutta tehokas monimuotoinen kielimalli Mixture-of-LoRAs -menetelmällä](https://arxiv.org/abs/2503.01743) - [Pienten kielimallien optimointi ajoneuvon sisäiseen funktiokutsuun](https://arxiv.org/abs/2501.02342) - [(WhyPHI) PHI-3 hienosäätö monivalintakysymysten vastaamiseen: menetelmä, tulokset ja haasteet](https://arxiv.org/abs/2501.01588) - [Phi-4-päättely tekninen raportti](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-päättelytekninen raportti](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)
# Phi Cookbook: Käytännön esimerkkejä Microsoftin Phi-malleilla

[![Avaa ja käytä esimerkkejä GitHub Codespaces -ympäristössä](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Avaa Dev Containers -ympäristössä](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHubin kontribuuttorit](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubin ongelmat](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubin pull-pyynnöt](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR:t tervetulleita](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHubin seuraajat](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubin haarukat](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubin tähdet](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi on sarja Microsoftin kehittämiä avoimen lähdekoodin tekoälymalleja. 

Phi on tällä hetkellä tehokkain ja kustannustehokkain pieni kielimalli (SLM), jolla on erittäin hyvät suorituskykymittarit monikielisyydessä, päättelyssä, tekstin/ chatin generoinnissa, koodauksessa, kuvissa, äänessä ja muissa käyttötarkoituksissa. 

Voit ottaa Phi-mallin käyttöön pilvessä tai reunalaitteissa, ja voit helposti rakentaa generatiivisia tekoälysovelluksia rajallisilla laskentatehoilla.

Seuraa näitä askelia aloittaaksesi näiden resurssien käytön:
1. **Haarauta repositorio**: Klikkaa [![GitHubin haarukat](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Kloonaa repositorio**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Liity Microsoft AI Discord -yhteisöön ja tapaa asiantuntijoita ja muita kehittäjiä**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/fi/cover.eb18d1b9605d754b.webp)

### 🌐 Monikielinen tuki

#### Tuettu GitHub Actionin kautta (automaattinen & aina ajan tasalla)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabia](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaria](../bg/README.md) | [Burma (Myanmar)](../my/README.md) | [Kiina (yksinkertaistettu)](../zh-CN/README.md) | [Kiina (perinteinen, Hongkong)](../zh-HK/README.md) | [Kiina (perinteinen, Macau)](../zh-MO/README.md) | [Kiina (perinteinen, Taiwan)](../zh-TW/README.md) | [Kroatia](../hr/README.md) | [Tšekki](../cs/README.md) | [Tanska](../da/README.md) | [Hollanti](../nl/README.md) | [Viro](../et/README.md) | [Suomi](./README.md) | [Ranska](../fr/README.md) | [Saksa](../de/README.md) | [Kreikka](../el/README.md) | [Heprea](../he/README.md) | [Hindi](../hi/README.md) | [Unkari](../hu/README.md) | [Indonesia](../id/README.md) | [Italia](../it/README.md) | [Japani](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korea](../ko/README.md) | [Liettua](../lt/README.md) | [Malaiji](../ms/README.md) | [Malajalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norja](../no/README.md) | [Persia (farsi)](../fa/README.md) | [Puola](../pl/README.md) | [Portugali (Brasilia)](../pt-BR/README.md) | [Portugali (Portugali)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romania](../ro/README.md) | [Venäjä](../ru/README.md) | [Serbia (kyrillinen)](../sr/README.md) | [Slovakki](../sk/README.md) | [Slovenia](../sl/README.md) | [Espanja](../es/README.md) | [Swahili](../sw/README.md) | [Ruotsi](../sv/README.md) | [Tagalog (filippiini)](../tl/README.md) | [Tamili](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkki](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnam](../vi/README.md)

> **Haluatko kloonata paikallisesti?**
>
> Tämä repositorio sisältää yli 50 kielen käännökset, mikä lisää huomattavasti latauskoon määrää. Jos haluat kloonata ilman käännöksiä, käytä laajennettua sparse checkout -toimintoa:
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
> Tämä antaa sinulle kaiken tarvitsemasi kurssin suorittamiseen paljon nopeammalla latauksella.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Sisällysluettelo

## Phi-mallien käyttö

### Phi Microsoft Foundryssa

Voit oppia käyttämään Microsoft Phi -malleja ja rakentamaan end-to-end-ratkaisuja eri laitteillasi. Kokeillaksesi Phi-mallia itse, aloita leikkimällä malleilla ja muokkaamalla Phi:tä omiin käyttötarkoituksiisi käyttämällä [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) -katalogia. Lisätietoja saat aloitusoppaasta [Microsoft Foundryn kanssa](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Leikkikenttä**
Jokaiselle mallille on oma testileikkikenttä [Azure AI Playground](https://aka.ms/try-phi3).

### Phi GitHub-malleilla

Voit oppia käyttämään Microsoft Phi -malleja ja rakentamaan end-to-end-ratkaisuja eri laitteillasi. Kokeillaksesi Phi-mallia itse, aloita leikkimällä mallilla ja muokkaamalla Phi:tä omiin käyttötarkoituksiisi käyttämällä [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) -katalogia. Lisätietoja saat aloitusoppaasta [GitHub Model Catalogin kanssa](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Leikkikenttä**
Jokaiselle mallille on oma [leikkikenttä mallin testaamiseen](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi Hugging Facessa

Mallin löydät myös [Hugging Facen](https://huggingface.co/microsoft) sivuilta

**Leikkikenttä**
 [Hugging Chat -leikkikenttä](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 Muut kurssit

Tiimimme tuottaa muitakin kursseja! Tutustu:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j aloittelijoille](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js aloittelijoille](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain aloittelijoille](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Reuna / MCP / Agentit
[![AZD aloittelijoille](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Reuna-AI aloittelijoille](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP aloittelijoille](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI-agentit aloittelijoille](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatiivisen tekoälyn sarja
[![Generatiivinen tekoäly aloittelijoille](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatiivinen tekoäly (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Perusoppiminen
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot -sarja
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Vastuullinen tekoäly 

Microsoft sitoutuu auttamaan asiakkaitaan käyttämään tekoälytuotteitamme vastuullisesti, jakamaan oppejamme ja rakentamaan luottamukseen perustuvia kumppanuuksia Työkalujen, kuten Transparency Notes ja Impact Assessments, avulla. Monet näistä resursseista löytyvät osoitteesta [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoftin lähestymistapa vastuulliseen tekoälyyn perustuu tekoälyn periaatteisiimme, jotka ovat oikeudenmukaisuus, luotettavuus ja turvallisuus, yksityisyys ja tietoturva, yhdenvertaisuus, läpinäkyvyys ja vastuullisuus.

Laajamittaiset luonnollisen kielen, kuvan ja puheen mallit – kuten tässä esimerkissä käytetyt – voivat mahdollisesti käyttäytyä tavoilla, jotka ovat epäoikeudenmukaisia, epäluotettavia tai loukkaavia, aiheuttaen siten haittaa. Tutustu [Azure OpenAI -palvelun Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) saadaksesi tietoa riskeistä ja rajoituksista.

Suositeltava tapa pienentää näitä riskejä on sisällyttää turvallisuusjärjestelmä arkkitehtuuriisi, joka voi havaita ja estää vahingollisen käytöksen. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) tarjoaa itsenäisen suojakerroksen, joka pystyy havaitsemaan sovelluksissa ja palveluissa käyttäjien ja tekoälyn tuottamaa haitallista sisältöä. Azure AI Content Safety sisältää teksti- ja kuva-API:t, joiden avulla voit havaita haitallista materiaalia. Microsoft Foundryn sisällä Content Safety -palvelu antaa mahdollisuuden tarkastella, tutkia ja kokeilla esimerkkikoodeja haitallisen sisällön havaitsemiseen eri muodoissa. Seuraava [nopean aloituksen dokumentaatio](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) opastaa sinua tekemään palvelupyynnöt.

Toinen huomioon otettava seikka on koko sovelluksen suorituskyky. Monimodaalisissa ja monimallipohjaisissa sovelluksissa suorituskyvyllä tarkoitetaan, että järjestelmä toimii odotustesi ja käyttäjiesi odotusten mukaisesti, mukaan lukien haitallisten tulosteiden välttäminen. On tärkeää arvioida koko sovelluksen suorituskykyä käyttämällä [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Sinulla on myös mahdollisuus luoda ja arvioida [mukautetuilla arvioijilla](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Voit arvioida tekoälysovellustasi kehitysympäristössäsi käyttäen [Azure AI Evaluation SDK:ta](https://microsoft.github.io/promptflow/index.html). Olipa käytössäsi testiaineisto tai tavoite, generatiivisen tekoälysovelluksesi tuotokset mitataan kvantitatiivisesti valmiilla arvioijilla tai valitsemillasi mukautetuilla arvioijilla. Jos haluat aloittaa järjestelmäsi arvioinnin azure ai evaluation sdk:lla, voit seurata [nopean aloituksen opasta](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kun suoritat arviointikierroksen, voit [visualisoida tulokset Microsoft Foundryssa](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## Tavara- ja palvelumerkit

Tämä projekti saattaa sisältää tavara- tai palvelumerkkejä projekteista, tuotteista tai palveluista. Microsoftin tavara- tai palvelumerkkien valtuutettu käyttö on sidottu ja sen on noudatettava [Microsoftin tavara- ja brändiohjeita](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Microsoftin tavara- tai palvelumerkkien käyttö tämän projektin muokatuissa versioissa ei saa aiheuttaa sekaannusta tai antaa vaikutelmaa Microsoftin sponsoroimasta toiminnasta. Kolmansien osapuolten tavara- tai palvelumerkkien käyttö on sidottu näiden osapuolten käytäntöihin.

## Apua saatavilla

Jos jumitut tai sinulla on kysymyksiä tekoälysovellusten rakentamisesta, liity:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Jos sinulla on tuotepalautetta tai kohtaat virheitä rakentaessasi, käy:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen omalla kielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->