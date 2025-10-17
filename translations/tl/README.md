<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4987daf30687ad3850757c9eae3f5411",
  "translation_date": "2025-10-17T10:32:02+00:00",
  "source_file": "README.md",
  "language_code": "tl"
}
-->
# Phi Cookbook: Mga Praktikal na Halimbawa gamit ang Phi Models ng Microsoft

[![Buksan at gamitin ang mga sample sa GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Buksan sa Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Mga Contributor sa GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![Mga Isyu sa GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![Mga Pull Request sa GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![Malugod na tinatanggap ang PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Mga Tagamasid sa GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![Mga Fork sa GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![Mga Bituin sa GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Ang Phi ay isang serye ng mga open source AI models na binuo ng Microsoft.

Ang Phi ay kasalukuyang pinakamakapangyarihan at pinaka-matipid na small language model (SLM), na may napakahusay na benchmark sa multi-language, reasoning, text/chat generation, coding, mga imahe, audio, at iba pang mga senaryo.

Maaaring i-deploy ang Phi sa cloud o sa mga edge devices, at madali kang makakagawa ng generative AI applications kahit limitado ang computing power.

Sundin ang mga hakbang na ito upang magsimula sa paggamit ng mga resource na ito:
1. **I-fork ang Repository**: I-click [![Mga Fork sa GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **I-clone ang Repository**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Sumali sa Microsoft AI Discord Community at makipagtagpo sa mga eksperto at kapwa developer**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 Suporta sa Multi-Language

#### Sinusuportahan sa pamamagitan ng GitHub Action (Automated at Laging Napapanahon)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](./README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Talaan ng Nilalaman

- Panimula
  - [Maligayang Pagdating sa Pamilya ng Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Pag-set up ng iyong environment](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Pag-unawa sa Mga Pangunahing Teknolohiya](./md/01.Introduction/01/01.Understandingtech.md)
  - [AI Safety para sa Phi Models](./md/01.Introduction/01/01.AISafety.md)
  - [Suporta sa Hardware ng Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Mga Phi Models at Availability sa iba't ibang platform](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Paggamit ng Guidance-ai at Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Mga Model sa GitHub Marketplace](https://github.com/marketplace/models)
  - [Azure AI Model Catalog](https://ai.azure.com)

- Pag-inference ng Phi sa iba't ibang environment
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [Mga Model sa GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Pag-inference ng Pamilya ng Phi
    - [Pag-inference ng Phi sa iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Pag-inference ng Phi sa Android](./md/01.Introduction/03/Android_Inference.md)
    - [Pag-inference ng Phi sa Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Pag-inference ng Phi sa AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Pag-inference ng Phi gamit ang Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Pag-inference ng Phi sa Local Server](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Pag-inference ng Phi sa Remote Server gamit ang AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Pag-inference ng Phi gamit ang Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Pag-inference ng Phi--Vision sa Lokal](./md/01.Introduction/03/Vision_Inference.md)
    - [Pag-inference ng Phi gamit ang Kaito AKS, Azure Containers (opisyal na suporta)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Pag-quantify ng Pamilya ng Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Pag-quantize ng Phi-3.5 / 4 gamit ang llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Pag-quantize ng Phi-3.5 / 4 gamit ang Generative AI extensions para sa onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Pag-quantize ng Phi-3.5 / 4 gamit ang Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Pag-quantize ng Phi-3.5 / 4 gamit ang Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Pagsusuri sa Phi
    - [Response AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry para sa Pagsusuri](./md/01.Introduction/05/AIFoundry.md)
    - [Paggamit ng Promptflow para sa Pagsusuri](./md/01.Introduction/05/Promptflow.md)
 
- RAG gamit ang Azure AI Search
    - [Paano gamitin ang Phi-4-mini at Phi-4-multimodal (RAG) gamit ang Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Mga sample ng pag-develop ng Phi application
  - Mga Text & Chat Application
    - Mga Sample ng Phi-4 🆕
      - [📓] [Makipag-chat gamit ang Phi-4-mini ONNX Model](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Makipag-chat gamit ang Phi-4 lokal na ONNX Model .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Chat .NET Console App gamit ang Phi-4 ONNX gamit ang Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Mga Sample ng Phi-3 / 3.5
      - [Lokal na Chatbot sa browser gamit ang Phi3, ONNX Runtime Web at WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Multi Model - Interactive Phi-3-mini at OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Pagbuo ng wrapper at paggamit ng Phi-3 gamit ang MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Model Optimization - Paano i-optimize ang Phi-3-min model para sa ONNX Runtime Web gamit ang Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [WinUI3 App gamit ang Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [WinUI3 Multi Model AI Powered Notes App Sample](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Pag-fine-tune at Integrasyon ng custom Phi-3 models gamit ang Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Pag-fine-tune at Integrasyon ng custom Phi-3 models gamit ang Prompt flow sa Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Pagsusuri sa Fine-tuned Phi-3 / Phi-3.5 Model sa Azure AI Foundry na nakatuon sa Responsible AI Principles ng Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct language prediction sample (Chinese/English)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Paggamit ng Windows GPU para gumawa ng Prompt flow solution gamit ang Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Paggamit ng Microsoft Phi-3.5 tflite para gumawa ng Android app](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Q&A .NET Example gamit ang local ONNX Phi-3 model gamit ang Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Console chat .NET app gamit ang Semantic Kernel at Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK Code Based Samples 
  - Phi-4 Samples 🆕
    - [📓] [Pagbuo ng project code gamit ang Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5 Samples
    - [Gumawa ng sarili mong Visual Studio Code GitHub Copilot Chat gamit ang Microsoft Phi-3 Family](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [Gumawa ng sarili mong Visual Studio Code Chat Copilot Agent gamit ang Phi-3.5 sa pamamagitan ng GitHub Models](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- Advanced Reasoning Samples
  - Phi-4 Samples 🆕
    - [📓] [Phi-4-mini-reasoning o Phi-4-reasoning Samples](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Pag-fine-tune ng Phi-4-mini-reasoning gamit ang Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Pag-fine-tune ng Phi-4-mini-reasoning gamit ang Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Phi-4-mini-reasoning gamit ang GitHub Models](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Phi-4-mini-reasoning gamit ang Azure AI Foundry Models](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- Mga Demo
    - [Phi-4-mini demos na naka-host sa Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Phi-4-multimodal demos na naka-host sa Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- Vision Samples
  - Phi-4 Samples 🆕
    - [📓] [Gamitin ang Phi-4-multimodal para basahin ang mga imahe at bumuo ng code](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Phi-3 / 3.5 Samples
    - [📓][Phi-3-vision-Image text to text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Visual language assistant - gamit ang Phi3-Vision at OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision multi-frame o multi-image sample](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Phi-3 Vision Local ONNX Model gamit ang Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Menu based Phi-3 Vision Local ONNX Model gamit ang Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

- Math Samples
  - Phi-4-Mini-Flash-Reasoning-Instruct Samples 🆕 [Math Demo gamit ang Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)

- Audio Samples
  - Phi-4 Samples 🆕
    - [📓] [Pagkuha ng audio transcripts gamit ang Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodal Audio Sample](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal Speech Translation Sample](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET console application gamit ang Phi-4-multimodal Audio para suriin ang isang audio file at gumawa ng transcript](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOE Samples
  - Phi-3 / 3.5 Samples
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) Social Media Sample](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [Pagbuo ng Retrieval-Augmented Generation (RAG) Pipeline gamit ang NVIDIA NIM Phi-3 MOE, Azure AI Search, at LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- Function Calling Samples
  - Phi-4 Samples 🆕
    - [📓] [Paggamit ng Function Calling Gamit ang Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Paggamit ng Function Calling para gumawa ng multi-agents Gamit ang Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Paggamit ng Function Calling gamit ang Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [Paggamit ng Function Calling gamit ang ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- Multimodal Mixing Samples
  - Phi-4 Samples 🆕
    - [📓] [Paggamit ng Phi-4-multimodal bilang Technology journalist](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET console application gamit ang Phi-4-multimodal para suriin ang mga imahe](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Fine-tuning Phi Samples
  - [Mga Senaryo ng Fine-tuning](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Fine-tuning vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Fine-tuning: Hayaan ang Phi-3 na maging eksperto sa industriya](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [Fine-tuning Phi-3 gamit ang AI Toolkit para sa VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Fine-tuning Phi-3 gamit ang Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)
  - [Fine-tuning Phi-3 gamit ang Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [Fine-tuning Phi-3 gamit ang QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Fine-tuning Phi-3 gamit ang Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Fine-tuning Phi-3 gamit ang Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Fine-tuning gamit ang Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Fine-tuning gamit ang Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [Fine-tuning Phi-3-vision gamit ang Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Fine-tuning Phi-3 gamit ang Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [Fine-tuning Phi-3-vision (opisyal na suporta)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Fine-Tuning Phi-3 gamit ang Kaito AKS, Azure Containers (opisyal na Suporta)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Fine-Tuning Phi-3 at 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands on Lab
  - [Paggalugad sa mga makabagong modelo: LLMs, SLMs, lokal na pag-develop at iba pa](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [Pag-unlock ng NLP Potential: Fine-Tuning gamit ang Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- Academic Research Papers and Publications
  - [Textbooks Are All You Need II: phi-1.5 technical report](https://arxiv.org/abs/2309.05463)
  - [Phi-3 Technical Report: Isang Highly Capable Language Model Locally sa Iyong Telepono](https://arxiv.org/abs/2404.14219)
  - [Phi-4 Technical Report](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini Technical Report: Compact ngunit Makapangyarihang Multimodal Language Models gamit ang Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)
  - [Pag-optimize ng Maliit na Language Models para sa Pagtawag ng Function sa Sasakyan](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Fine-Tuning PHI-3 para sa Multiple-Choice Question Answering: Metodolohiya, Resulta, at Hamon](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning Technical Report](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning Technical Report](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Paggamit ng Phi Models

### Phi sa Azure AI Foundry

Matutunan mo kung paano gamitin ang Microsoft Phi at kung paano bumuo ng mga E2E na solusyon sa iba't ibang hardware devices. Para maranasan ang Phi, magsimula sa pamamagitan ng paggamit ng mga modelo at i-customize ang Phi para sa iyong mga senaryo gamit ang [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). Maaari kang matuto pa sa Getting Started with [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Playground**  
Ang bawat modelo ay may nakalaang playground para subukan ang modelo [Azure AI Playground](https://aka.ms/try-phi3).

### Phi sa GitHub Models

Matutunan mo kung paano gamitin ang Microsoft Phi at kung paano bumuo ng mga E2E na solusyon sa iba't ibang hardware devices. Para maranasan ang Phi, magsimula sa pamamagitan ng paggamit ng modelo at i-customize ang Phi para sa iyong mga senaryo gamit ang [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Maaari kang matuto pa sa Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Playground**  
Ang bawat modelo ay may nakalaang [playground para subukan ang modelo](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi sa Hugging Face

Maaari mo ring makita ang modelo sa [Hugging Face](https://huggingface.co/microsoft).

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Responsableng AI 

Ang Microsoft ay nakatuon sa pagtulong sa aming mga customer na gamitin ang aming mga AI na produkto nang responsable, ibahagi ang aming mga natutunan, at bumuo ng mga partnership na nakabase sa tiwala sa pamamagitan ng mga tool tulad ng Transparency Notes at Impact Assessments. Marami sa mga resources na ito ay matatagpuan sa [https://aka.ms/RAI](https://aka.ms/RAI).  
Ang diskarte ng Microsoft sa responsableng AI ay nakabatay sa aming mga prinsipyo ng AI: pagiging patas, pagiging maaasahan at kaligtasan, privacy at seguridad, pagiging inklusibo, transparency, at pananagutan.

Ang malakihang natural language, image, at speech models - tulad ng mga ginagamit sa sample na ito - ay maaaring magpakita ng mga hindi patas, hindi maaasahan, o nakakasakit na pag-uugali, na maaaring magdulot ng pinsala. Mangyaring konsultahin ang [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) upang malaman ang mga panganib at limitasyon.

Ang inirerekomendang diskarte upang mabawasan ang mga panganib na ito ay ang pagsama ng safety system sa iyong arkitektura na maaaring mag-detect at mag-prevent ng mapanganib na pag-uugali. Ang [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ay nagbibigay ng independent layer ng proteksyon, na kayang mag-detect ng mapanganib na user-generated at AI-generated na content sa mga aplikasyon at serbisyo. Ang Azure AI Content Safety ay may kasamang text at image APIs na nagbibigay-daan sa iyo upang mag-detect ng materyal na mapanganib. Sa loob ng Azure AI Foundry, ang Content Safety service ay nagbibigay-daan sa iyo upang makita, galugarin, at subukan ang sample code para sa pag-detect ng mapanganib na content sa iba't ibang modalities. Ang sumusunod na [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ay gagabay sa iyo sa paggawa ng mga request sa serbisyo.

Isa pang aspeto na dapat isaalang-alang ay ang kabuuang performance ng aplikasyon. Sa mga multi-modal at multi-models na aplikasyon, ang performance ay nangangahulugan na ang sistema ay gumagana ayon sa inaasahan mo at ng iyong mga user, kabilang ang hindi pagbuo ng mapanganib na outputs. Mahalagang suriin ang performance ng iyong kabuuang aplikasyon gamit ang [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). May kakayahan ka ring gumawa at mag-evaluate gamit ang [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Maaari mong i-evaluate ang iyong AI application sa iyong development environment gamit ang [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Gamit ang test dataset o target, ang mga generation ng iyong generative AI application ay sinusukat nang quantitatively gamit ang built-in evaluators o custom evaluators na iyong pinili. Para magsimula sa Azure AI Evaluation SDK upang i-evaluate ang iyong sistema, maaari mong sundan ang [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kapag naisagawa mo na ang evaluation run, maaari mong [i-visualize ang mga resulta sa Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Mga Trademark

Ang proyektong ito ay maaaring naglalaman ng mga trademark o logo para sa mga proyekto, produkto, o serbisyo. Ang awtorisadong paggamit ng mga trademark o logo ng Microsoft ay dapat sumunod sa at sundin ang [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Ang paggamit ng mga trademark o logo ng Microsoft sa mga binagong bersyon ng proyektong ito ay hindi dapat magdulot ng kalituhan o magpahiwatig ng sponsorship ng Microsoft. Ang anumang paggamit ng mga third-party na trademark o logo ay dapat sumunod sa mga patakaran ng third-party na iyon.

## Pagkuha ng Tulong

Kung ikaw ay nahihirapan o may mga tanong tungkol sa paggawa ng AI apps, sumali sa:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Kung mayroon kang feedback sa produkto o mga error habang gumagawa, bisitahin:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.