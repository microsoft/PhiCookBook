<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1cab9282e04f2e1c388a38dca7763c16",
  "translation_date": "2025-05-09T04:01:52+00:00",
  "source_file": "README.md",
  "language_code": "nl"
}
-->
# Phi Cookbook: Praktische Voorbeelden met Microsoft's Phi Modellen

[![Open en gebruik de voorbeelden in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi is een reeks open source AI-modellen ontwikkeld door Microsoft.

Phi is momenteel het krachtigste en meest kostenefficiënte kleine taalmodel (SLM), met uitstekende prestaties op het gebied van meertaligheid, redeneren, tekst-/chatgeneratie, coderen, afbeeldingen, audio en andere toepassingen.

Je kunt Phi inzetten in de cloud of op edge-apparaten, en je kunt eenvoudig generatieve AI-toepassingen bouwen met beperkte rekenkracht.

Volg deze stappen om aan de slag te gaan met deze bronnen:  
1. **Fork de Repository**: Klik op [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **Clone de Repository**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Word lid van de Microsoft AI Discord Community en ontmoet experts en mede-ontwikkelaars**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.2595d43b382944c601aebf88583314636768eece3d94e8e4448e03a4e5bedef4.nl.png)

## 🌐 Meertalige Ondersteuning

### Ondersteund via GitHub Action (Geautomatiseerd & Altijd Up-to-Date)

[Frans](../fr/README.md) | [Spaans](../es/README.md) | [Duits](../de/README.md) | [Russisch](../ru/README.md) | [Arabisch](../ar/README.md) | [Perzisch (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinees (Vereenvoudigd)](../zh/README.md) | [Chinees (Traditioneel, Macau)](../mo/README.md) | [Chinees (Traditioneel, Hong Kong)](../hk/README.md) | [Chinees (Traditioneel, Taiwan)](../tw/README.md) | [Japans](../ja/README.md) | [Koreaans](../ko/README.md) | [Hindi](../hi/README.md)

### Ondersteund via CLI
## Inhoudsopgave

- Inleiding
- [Welkom bij de Phi Family](./md/01.Introduction/01/01.PhiFamily.md)
  - [Je omgeving instellen](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Belangrijke technologieën begrijpen](./md/01.Introduction/01/01.Understandingtech.md)
  - [AI-veiligheid voor Phi-modellen](./md/01.Introduction/01/01.AISafety.md)
  - [Ondersteuning voor Phi-hardware](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi-modellen & beschikbaarheid op verschillende platforms](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Gebruik van Guidance-ai en Phi](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace Modellen](https://github.com/marketplace/models)
  - [Azure AI Modelcatalogus](https://ai.azure.com)

- Inference Phi in verschillende omgevingen
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub Modellen](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry Modelcatalogus](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)

- Inference Phi Family
    - [Inference Phi op iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Inference Phi op Android](./md/01.Introduction/03/Android_Inference.md)
    - [Inference Phi op Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Inference Phi op AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Inference Phi met Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Inference Phi op lokale server](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Inference Phi op remote server met AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Inference Phi met Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Inference Phi–Vision lokaal](./md/01.Introduction/03/Vision_Inference.md)
    - [Inference Phi met Kaito AKS, Azure Containers (officiële ondersteuning)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Quantificeren van Phi Family](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Quantizen van Phi-3.5 / 4 met llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Quantizen van Phi-3.5 / 4 met Generative AI-extensies voor onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Quantizen van Phi-3.5 / 4 met Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Quantizen van Phi-3.5 / 4 met Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Evaluatie Phi
- [Response AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry voor Evaluatie](./md/01.Introduction/05/AIFoundry.md)
    - [Promptflow gebruiken voor Evaluatie](./md/01.Introduction/05/Promptflow.md)
 
- RAG met Azure AI Search
    - [Hoe Phi-4-mini en Phi-4-multimodal (RAG) te gebruiken met Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Voorbeelden voor Phi applicatieontwikkeling
  - Tekst- & Chatapplicaties
    - Phi-4 Voorbeelden 🆕
      - [📓] [Chatten met Phi-4-mini ONNX Model](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Chatten met Phi-4 lokaal ONNX Model .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Chat .NET Console App met Phi-4 ONNX via Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 Voorbeelden
      - [Lokale Chatbot in de browser met Phi3, ONNX Runtime Web en WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - Interactieve Phi-3-mini en OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Een wrapper bouwen en Phi-3 gebruiken met MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Modeloptimalisatie - Hoe Phi-3-mini model te optimaliseren voor ONNX Runtime Web met Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 App met Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3 Multi Model AI Powered Notes App Voorbeeld](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Fijn afstemmen en integreren van aangepaste Phi-3 modellen met Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Fijn afstemmen en integreren van aangepaste Phi-3 modellen met Prompt flow in Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Evaluatie van het fijn afgestemde Phi-3 / Phi-3.5 Model in Azure AI Foundry met focus op Microsoft's Responsible AI Principles](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct taalvoorspellingsvoorbeeld (Chinees/Engels)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU gebruiken om Prompt flow oplossing te maken met Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite gebruiken om Android app te maken](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Q&A .NET Voorbeeld met lokaal ONNX Phi-3 model via Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Console chat .NET app met Semantic Kernel en Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK Code Voorbeelden
    - Phi-4 Voorbeelden 🆕
      - [📓] [Projectcode genereren met Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 Voorbeelden
      - [Bouw je eigen Visual Studio Code GitHub Copilot Chat met Microsoft Phi-3 Familie](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [Maak je eigen Visual Studio Code Chat Copilot Agent met Phi-3.5 via GitHub Modellen](./md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - Geavanceerde Redeneringsvoorbeelden
    - Phi-4 Voorbeelden 🆕
      - [📓] [Phi-4-mini-reasoning of Phi-4-reasoning Voorbeelden](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Fijn afstemmen van Phi-4-mini-reasoning met Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Fijn afstemmen van Phi-4-mini-reasoning met Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning met GitHub Modellen](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
- [📓] [Phi-4-mini redeneren met Azure AI Foundry-modellen](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - Demo's
      - [Phi-4-mini demo's gehost op Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodale demo's gehost op Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - Visie Voorbeelden
    - Phi-4 Voorbeelden 🆕
      - [📓] [Gebruik Phi-4-multimodaal om afbeeldingen te lezen en code te genereren](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 Voorbeelden
      -  [📓][Phi-3-visie Afbeelding tekst naar tekst](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-visie ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-visie CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-visie - Visuele taalassistent - met Phi3-Vision en OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Visie Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Visie OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Visie multi-frame of multi-afbeelding voorbeeld](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Visie lokaal ONNX-model met Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [Menu-gebaseerd Phi-3 Visie lokaal ONNX-model met Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Audio Voorbeelden
    - Phi-4 Voorbeelden 🆕
      - [📓] [Audio transcripties extraheren met Phi-4-multimodaal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodaal audio voorbeeld](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodaal spraakvertaling voorbeeld](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET console-applicatie die Phi-4-multimodaal gebruikt om een audiobestand te analyseren en transcript te genereren](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE Voorbeelden
    - Phi-3 / 3.5 Voorbeelden
      - [📓] [Phi-3.5 Mixture of Experts-modellen (MoEs) Social Media voorbeeld](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [Een Retrieval-Augmented Generation (RAG) pipeline bouwen met NVIDIA NIM Phi-3 MOE, Azure AI Search en LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
  - Function Calling Voorbeelden
    - Phi-4 Voorbeelden 🆕
      -  [📓] [Function Calling gebruiken met Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Function Calling gebruiken om multi-agents te maken met Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Function Calling gebruiken met Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
  - Multimodale Mix Voorbeelden
    - Phi-4 Voorbeelden 🆕
      -  [📓] [Phi-4-multimodaal gebruiken als technologiejournalist](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET console-applicatie die Phi-4-multimodaal gebruikt om afbeeldingen te analyseren](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Fine-tuning Phi Voorbeelden
  - [Fine-tuning scenario's](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Fine-tuning versus RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Fine-tuning Laat Phi-3 een industrie-expert worden](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Fine-tuning Phi-3 met AI Toolkit voor VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Fine-tuning Phi-3 met Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
- [Fijn afstemmen van Phi-3 met Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Fijn afstemmen van Phi-3 met QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Fijn afstemmen van Phi-3 met Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Fijn afstemmen van Phi-3 met Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Fijn afstemmen met Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Fijn afstemmen met Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Fijn afstemmen van Phi-3-vision met Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Fijn afstemmen van Phi-3 met Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Fijn afstemmen van Phi-3-vision (officiële ondersteuning)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Fijn afstemmen van Phi-3 met Kaito AKS, Azure Containers (officiële ondersteuning)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Fijn afstemmen van Phi-3 en 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands-on Lab
  - [Ontdek baanbrekende modellen: LLMs, SLMs, lokale ontwikkeling en meer](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP-potentieel benutten: Fijn afstemmen met Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Academische onderzoeksartikelen en publicaties
  - [Textbooks Are All You Need II: phi-1.5 technisch rapport](https://arxiv.org/abs/2309.05463)
  - [Phi-3 technisch rapport: een krachtig taalmodel lokaal op je telefoon](https://arxiv.org/abs/2404.14219)
  - [Phi-4 technisch rapport](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini technisch rapport: compacte maar krachtige multimodale taalmodellen via Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Optimalisatie van kleine taalmodellen voor functie-aanroepen in voertuigen](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Fijn afstemmen van PHI-3 voor multiple-choice vraagbeantwoording: methodologie, resultaten en uitdagingen](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning technisch rapport](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning technisch rapport](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi-modellen gebruiken

### Phi op Azure AI Foundry

Je kunt leren hoe je Microsoft Phi gebruikt en hoe je end-to-end oplossingen bouwt op verschillende hardwareapparaten. Om Phi zelf te ervaren, begin je met het uitproberen van de modellen en het aanpassen van Phi aan jouw scenario’s via de [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Meer informatie vind je bij Aan de slag met [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Playground**  
Elk model heeft een speciale playground om het model te testen: [Azure AI Playground](https://aka.ms/try-phi3).

### Phi op GitHub Models

Je kunt leren hoe je Microsoft Phi gebruikt en hoe je end-to-end oplossingen bouwt op verschillende hardwareapparaten. Om Phi zelf te ervaren, begin je met het uitproberen van het model en het aanpassen van Phi aan jouw scenario’s via de [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Meer informatie vind je bij Aan de slag met [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Playground**  
Elk model heeft een speciale [playground om het model te testen](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi op Hugging Face

Je kunt het model ook vinden op [Hugging Face](https://huggingface.co/microsoft).

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Verantwoord AI

Microsoft zet zich in om klanten te helpen onze AI-producten op een verantwoorde manier te gebruiken, onze ervaringen te delen en vertrouwen op te bouwen via tools zoals Transparency Notes en Impact Assessments. Veel van deze bronnen zijn te vinden op [https://aka.ms/RAI](https://aka.ms/RAI).  
De aanpak van Microsoft voor verantwoord AI is gebaseerd op onze AI-principes: eerlijkheid, betrouwbaarheid en veiligheid, privacy en beveiliging, inclusiviteit, transparantie en verantwoordelijkheid.
Grootschalige modellen voor natuurlijke taal, beeld en spraak – zoals die gebruikt worden in dit voorbeeld – kunnen zich mogelijk op oneerlijke, onbetrouwbare of aanstootgevende manieren gedragen, wat schade kan veroorzaken. Raadpleeg de [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) om geïnformeerd te worden over risico's en beperkingen.

De aanbevolen aanpak om deze risico's te beperken is het opnemen van een veiligheidssysteem in je architectuur dat schadelijk gedrag kan detecteren en voorkomen. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) biedt een onafhankelijke beschermingslaag die schadelijke door gebruikers en AI gegenereerde inhoud in applicaties en diensten kan detecteren. Azure AI Content Safety bevat tekst- en beeld-API's waarmee je schadelijk materiaal kunt opsporen. Binnen Azure AI Foundry kun je met de Content Safety-service voorbeeldcode bekijken, verkennen en uitproberen om schadelijke inhoud in verschillende modaliteiten te detecteren. De volgende [quickstart-documentatie](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) leidt je door het maken van verzoeken aan de service.

Een ander aspect om rekening mee te houden is de algehele prestaties van de applicatie. Bij multimodale en multimodelapplicaties verstaan we onder prestaties dat het systeem functioneert zoals jij en je gebruikers verwachten, inclusief het niet genereren van schadelijke output. Het is belangrijk om de prestaties van je gehele applicatie te beoordelen met behulp van [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Je hebt ook de mogelijkheid om te creëren en evalueren met [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Je kunt je AI-applicatie evalueren in je ontwikkelomgeving met de [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Op basis van een testdataset of een doel worden de generaties van je generatieve AI-applicatie kwantitatief gemeten met ingebouwde evaluators of evaluators naar keuze. Om aan de slag te gaan met de azure ai evaluation sdk voor het evalueren van je systeem, kun je de [quickstart-gids](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) volgen. Zodra je een evaluatieronde hebt uitgevoerd, kun je de resultaten [visualiseren in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Handelsmerken

Dit project kan handelsmerken of logo’s bevatten van projecten, producten of diensten. Het geautoriseerd gebruik van Microsoft-handelsmerken of logo’s is onderworpen aan en moet voldoen aan de [Microsoft Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Het gebruik van Microsoft-handelsmerken of logo’s in gewijzigde versies van dit project mag geen verwarring veroorzaken of een Microsoft-sponsoring suggereren. Elk gebruik van handelsmerken of logo’s van derden is onderworpen aan het beleid van die derden.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal dient als de gezaghebbende bron te worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.