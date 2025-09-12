<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T13:40:38+00:00",
  "source_file": "README.md",
  "language_code": "ne"
}
-->
# Phi कुकबुक: माइक्रोसफ्टको Phi मोडेलहरूसँग व्यावहारिक उदाहरणहरू

Phi माइक्रोसफ्टद्वारा विकसित ओपन सोर्स AI मोडेलहरूको श्रृंखला हो।

Phi हालको समयमा सबैभन्दा शक्तिशाली र लागत-प्रभावकारी सानो भाषा मोडेल (SLM) हो, जसले बहुभाषा, तर्क, पाठ/च्याट उत्पादन, कोडिङ, छविहरू, अडियो र अन्य परिदृश्यहरूमा उत्कृष्ट प्रदर्शन गर्दछ।

तपाईं Phi लाई क्लाउड वा एज उपकरणहरूमा तैनात गर्न सक्नुहुन्छ, र सीमित कम्प्युटिङ पावरको साथ सजिलै जेनेरेटिभ AI एप्लिकेसनहरू निर्माण गर्न सक्नुहुन्छ।

यी स्रोतहरू प्रयोग गर्न सुरु गर्नका लागि निम्न चरणहरू अनुसरण गर्नुहोस्:
1. **रिपोजिटरीलाई फोर्क गर्नुहोस्**: क्लिक गर्नुहोस् [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **रिपोजिटरीलाई क्लोन गर्नुहोस्**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**माइक्रोसफ्ट AI डिस्कोर्ड समुदायमा सामेल हुनुहोस् र विशेषज्ञहरू तथा अन्य डेभलपरहरूसँग भेट गर्नुहोस्**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 बहुभाषा समर्थन

#### GitHub Action मार्फत समर्थित (स्वचालित र सधैं अद्यावधिक)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) 
[Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](./README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)

## सामग्री तालिका

- परिचय
  - [Phi परिवारमा स्वागत छ](./md/01.Introduction/01/01.PhiFamily.md)
  - [आफ्नो वातावरण सेटअप गर्नुहोस्](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [मुख्य प्रविधिहरू बुझ्दै](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi मोडेलहरूको लागि AI सुरक्षा](./md/01.Introduction/01/01.AISafety.md)
  - [Phi हार्डवेयर समर्थन](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi मोडेलहरू र प्लेटफर्महरूमा उपलब्धता](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai र Phi प्रयोग गर्दै](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace मोडेलहरू](https://github.com/marketplace/models)
  - [Azure AI मोडेल क्याटलग](https://ai.azure.com)

- विभिन्न वातावरणमा Phi को इनफरेन्स
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [GitHub मोडेलहरू](./md/01.Introduction/02/02.GitHubModel.md)
    - [Azure AI Foundry मोडेल क्याटलग](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi परिवारको इनफरेन्स
    - [iOS मा Phi को इनफरेन्स](./md/01.Introduction/03/iOS_Inference.md)
    - [Android मा Phi को इनफरेन्स](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson मा Phi को इनफरेन्स](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC मा Phi को इनफरेन्स](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework सँग Phi को इनफरेन्स](./md/01.Introduction/03/MLX_Inference.md)
    - [स्थानीय सर्भरमा Phi को इनफरेन्स](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit प्रयोग गरेर रिमोट सर्भरमा Phi को इनफरेन्स](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust सँग Phi को इनफरेन्स](./md/01.Introduction/03/Rust_Inference.md)
    - [स्थानीयमा Phi--Vision को इनफरेन्स](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (औपचारिक समर्थन) सँग Phi को इनफरेन्स](./md/01.Introduction/03/Kaito_Inference.md)

- [Phi परिवारको क्वान्टिफाइङ](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp प्रयोग गरेर Phi-3.5 / 4 को क्वान्टिफाइङ](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime को लागि जेनेरेटिभ AI एक्सटेन्सन प्रयोग गरेर Phi-3.5 / 4 को क्वान्टिफाइङ](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO प्रयोग गरेर Phi-3.5 / 4 को क्वान्टिफाइङ](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework प्रयोग गरेर Phi-3.5 / 4 को क्वान्टिफाइङ](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi को मूल्याङ्कन
    - [उत्तरदायी AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [मूल्याङ्कनको लागि Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [मूल्याङ्कनको लागि Promptflow प्रयोग गर्दै](./md/01.Introduction/05/Promptflow.md)

- Azure AI Search सँग RAG
    - [Azure AI Search सँग Phi-4-mini र Phi-4-multimodal (RAG) कसरी प्रयोग गर्ने](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi एप्लिकेसन विकास नमूनाहरू
  - पाठ र च्याट एप्लिकेसनहरू
    - Phi-4 नमूनाहरू 🆕
      - [📓] [Phi-4-mini ONNX मोडेलसँग च्याट गर्नुहोस्](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [स्थानीय ONNX मोडेल .NET सँग Phi-4 च्याट गर्नुहोस्](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel प्रयोग गरेर Phi-4 ONNX सँग .NET कन्सोल एप च्याट गर्नुहोस्](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 नमूनाहरू
      - [ब्राउजरमा Phi3, ONNX Runtime Web र WebGPU प्रयोग गरेर स्थानीय च्याटबोट](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino च्याट](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [मल्टी मोडेल - Phi-3-mini र OpenAI Whisper सँग अन्तरक्रियात्मक](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Wrapper निर्माण गर्दै र MLFlow सँग Phi-3 प्रयोग गर्दै](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [मोडेल अनुकूलन - Olive प्रयोग गरेर ONNX Runtime Web को लागि Phi-3-min मोडेल कसरी अनुकूलित गर्ने](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx सँग WinUI3 एप](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3 मल्टी मोडेल AI Powered Notes App नमूना](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [कस्टम Phi-3 मोडेलहरूलाई Prompt Flow सँग Fine-tune र Integrate गर्नुहोस्](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Azure AI Foundry मा Prompt Flow सँग कस्टम Phi-3 मोडेलहरू Fine-tune र Integrate गर्नुहोस्](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Microsoft को Responsible AI सिद्धान्तहरूमा केन्द्रित गर्दै Azure AI Foundry मा Fine-tuned Phi-3 / Phi-3.5 मोडेलको मूल्याङ्कन गर्नुहोस्](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct भाषा भविष्यवाणी नमूना (चिनियाँ/अंग्रेजी)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU प्रयोग गरेर Phi-3.5-Instruct ONNX सँग Prompt Flow समाधान सिर्जना गर्नुहोस्](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tflite प्रयोग गरेर Android एप सिर्जना गर्नुहोस्](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Microsoft.ML.OnnxRuntime प्रयोग गरेर स्थानीय ONNX Phi-3 मोडेलको साथ Q&A .NET उदाहरण](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Semantic Kernel र Phi-3 सँग Console chat .NET एप](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK कोड आधारित नमूनाहरू 
  - Phi-4 नमूनाहरू 🆕
    - [📓] [Phi-4-multimodal प्रयोग गरेर प्रोजेक्ट कोड सिर्जना गर्नुहोस्](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5 नमूनाहरू
    - [Microsoft Phi-3 परिवारको साथ Visual Studio Code GitHub Copilot Chat निर्माण गर्नुहोस्](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [GitHub मोडेलहरूद्वारा Phi-3.5 प्रयोग गरेर Visual Studio Code Chat Copilot Agent सिर्जना गर्नुहोस्](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- उन्नत तर्क नमूनाहरू
  - Phi-4 नमूनाहरू 🆕
    - [📓] [Phi-4-mini-reasoning वा Phi-4-reasoning नमूनाहरू](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Microsoft Olive सँग Phi-4-mini-reasoning Fine-tuning](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Apple MLX सँग Phi-4-mini-reasoning Fine-tuning](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [GitHub मोडेलहरू सँग Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Azure AI Foundry मोडेलहरू सँग Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- डेमोहरू
    - [Hugging Face Spaces मा होस्ट गरिएको Phi-4-mini डेमोहरू](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Hugging Face Spaces मा होस्ट गरिएको Phi-4-multimodal डेमोहरू](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- दृष्टि नमूनाहरू
  - Phi-4 नमूनाहरू 🆕
    - [📓] [Phi-4-multimodal प्रयोग गरेर छविहरू पढ्नुहोस् र कोड सिर्जना गर्नुहोस्](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Phi-3 / 3.5 नमूनाहरू
    - [📓][Phi-3-vision-छवि पाठलाई पाठमा रूपान्तरण गर्नुहोस्](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [DEMO: Phi-3 पुन: प्रयोग](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - दृश्य भाषा सहायक - Phi3-Vision र OpenVINO सँग](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
    - [📓][Phi-3.5 Vision बहु-फ्रेम वा बहु-छवि नमूना](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
    - [Microsoft.ML.OnnxRuntime .NET प्रयोग गरेर स्थानीय ONNX मोडेलको साथ Phi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi303)
    - [Microsoft.ML.OnnxRuntime .NET प्रयोग गरेर स्थानीय ONNX मोडेलको साथ मेनु आधारित Phi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi304)

- गणित नमूनाहरू
  - Phi-4-Mini-Flash-Reasoning-Instruct नमूनाहरू 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct सँग गणित डेमो](../../md/02.Application/09.Math/MathDemo.ipynb)

- अडियो नमूनाहरू
  - Phi-4 नमूनाहरू 🆕
    - [📓] [Phi-4-multimodal प्रयोग गरेर अडियो ट्रान्सक्रिप्टहरू निकाल्नुहोस्](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
    - [📓] [Phi-4-multimodal अडियो नमूना](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
    - [📓] [Phi-4-multimodal भाषण अनुवाद नमूना](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET कन्सोल एप्लिकेसन Phi-4-multimodal अडियो प्रयोग गरेर अडियो फाइल विश्लेषण गर्न र ट्रान्सक्रिप्ट सिर्जना गर्न](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOE नमूनाहरू
  - Phi-3 / 3.5 नमूनाहरू
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) सामाजिक मिडिया नमूना](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, र LlamaIndex सँग Retrieval-Augmented Generation (RAG) पाइपलाइन निर्माण गर्नुहोस्](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- फङ्सन कलिङ नमूनाहरू
  - Phi-4 नमूनाहरू 🆕
    - [📓] [Phi-4-mini सँग फङ्सन कलिङ प्रयोग गर्नुहोस्](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Phi-4-mini सँग बहु-एजेन्टहरू सिर्जना गर्न फङ्सन कलिङ प्रयोग गर्नुहोस्](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Ollama सँग फङ्सन कलिङ प्रयोग गर्नुहोस्](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [ONNX सँग फङ्सन कलिङ प्रयोग गर्नुहोस्](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- बहु-मोडल मिक्सिङ नमूनाहरू
  - Phi-4 नमूनाहरू 🆕
    - [📓] [प्रविधि पत्रकारको रूपमा Phi-4-multimodal प्रयोग गर्नुहोस्](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET कन्सोल एप्लिकेसन Phi-4-multimodal प्रयोग गरेर छविहरू विश्लेषण गर्नुहोस्](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Fine-tuning Phi नमूनाहरू
  - [Fine-tuning परिदृश्यहरू](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [Fine-tuning बनाम RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Fine-tuning Phi-3 लाई उद्योग विशेषज्ञ बनाउनुहोस्](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code को लागि AI Toolkit सँग Phi-3 Fine-tuning गर्नुहोस्](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service सँग Phi-3 Fine-tuning गर्नुहोस्](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora सँग Phi-3 Fine-tuning गर्नुहोस्](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora सँग Phi-3 Fine-tuning गर्नुहोस्](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry सँग Phi-3 Fine-tuning गर्नुहोस्](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK सँग Phi-3 Fine-tuning गर्नुहोस्](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive सँग Fine-tuning गर्नुहोस्](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Lab सँग Fine-tuning गर्नुहोस्](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias सँग Phi-3-vision Fine-tuning गर्नुहोस्](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework सँग Phi-3 Fine-tuning गर्नुहोस्](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision (औपचारिक समर्थन) Fine-tuning गर्नुहोस्](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers (औपचारिक समर्थन) सँग Phi-3 Fine-tuning गर्नुहोस्](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 र 3.5 Vision Fine-Tuning](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands-on Lab
  - [उन्नत मोडेलहरू अन्वेषण गर्दै: LLMs, SLMs, स्थानीय विकास र थप](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP क्षमता अनलक गर्दै: Microsoft Olive सँग Fine-Tuning](https://github.com/azure/Ignite_FineTuning_workshop)

- शैक्षिक अनुसन्धान पत्रहरू र प्रकाशनहरू
  - [Textbooks Are All You Need II: phi-1.5 प्राविधिक रिपोर्ट](https://arxiv.org/abs/2309.05463)
  - [Phi-3 प्राविधिक रिपोर्ट: अत्यधिक सक्षम भाषा मोडेल तपाईंको फोनमा स्थानीय रूपमा](https://arxiv.org/abs/2404.14219)
  - [Phi-4 प्राविधिक रिपोर्ट](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini प्राविधिक रिपोर्ट: Mixture-of-LoRAs मार्फत कम्प्याक्ट तर शक्तिशाली बहु-मोडल भाषा मोडेलहरू](https://arxiv.org/abs/2503.01743)
  - [साना भाषा मोडेलहरूलाई In-Vehicle Function-Calling को लागि अनुकूलित गर्दै](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) Multiple-Choice Question Answering को लागि PHI-3 Fine-Tuning: पद्धति, परिणामहरू, र चुनौतीहरू](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning प्राविधिक प्रतिवेदन](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-reasoning प्राविधिक प्रतिवेदन](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi मोडेलहरू प्रयोग गर्दै

### Azure AI Foundry मा Phi

तपाईं Microsoft Phi कसरी प्रयोग गर्ने र विभिन्न हार्डवेयर उपकरणहरूमा E2E समाधानहरू निर्माण गर्ने सिक्न सक्नुहुन्छ। Phi अनुभव गर्नको लागि, मोडेलहरूसँग खेल्न सुरु गर्नुहोस् र आफ्नो परिदृश्यहरूका लागि Phi अनुकूलन गर्नुहोस् [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) प्रयोग गरेर। थप जानकारीको लागि [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) मा सुरु गर्ने तरिका हेर्नुहोस्।

**Playground**  
प्रत्येक मोडेलको परीक्षण गर्नको लागि समर्पित playground छ [Azure AI Playground](https://aka.ms/try-phi3)।

### GitHub मा Phi मोडेलहरू

तपाईं Microsoft Phi कसरी प्रयोग गर्ने र विभिन्न हार्डवेयर उपकरणहरूमा E2E समाधानहरू निर्माण गर्ने सिक्न सक्नुहुन्छ। Phi अनुभव गर्नको लागि, मोडेलहरूसँग खेल्न सुरु गर्नुहोस् र आफ्नो परिदृश्यहरूका लागि Phi अनुकूलन गर्नुहोस् [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) प्रयोग गरेर। थप जानकारीको लागि [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) मा सुरु गर्ने तरिका हेर्नुहोस्।

**Playground**  
प्रत्येक मोडेलको परीक्षण गर्नको लागि समर्पित [playground](/md/02.QuickStart/GitHubModel_QuickStart.md) छ।

### Hugging Face मा Phi

तपाईं मोडेललाई [Hugging Face](https://huggingface.co/microsoft) मा पनि पाउन सक्नुहुन्छ।

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## जिम्मेवार AI

Microsoft हाम्रो ग्राहकहरूलाई हाम्रो AI उत्पादनहरू जिम्मेवारीपूर्वक प्रयोग गर्न मद्दत गर्न, हाम्रो सिकाइहरू साझा गर्न, र विश्वासमा आधारित साझेदारीहरू निर्माण गर्न प्रतिबद्ध छ। यसका लागि Transparency Notes र Impact Assessments जस्ता उपकरणहरू उपलब्ध छन्। यी स्रोतहरू धेरै [https://aka.ms/RAI](https://aka.ms/RAI) मा पाउन सकिन्छ।  
Microsoft को जिम्मेवार AI को दृष्टिकोण हाम्रो AI सिद्धान्तहरूमा आधारित छ: निष्पक्षता, विश्वसनीयता र सुरक्षा, गोपनीयता र सुरक्षा, समावेशिता, पारदर्शिता, र उत्तरदायित्व।

ठूलो-स्तरको प्राकृतिक भाषा, छवि, र आवाज मोडेलहरू - जस्तै यस नमूनामा प्रयोग गरिएका - कहिलेकाहीं अन्यायपूर्ण, अविश्वसनीय, वा आपत्तिजनक व्यवहार गर्न सक्छन्, जसले हानि पुर्‍याउन सक्छ। कृपया [Azure OpenAI सेवा Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) परामर्श गर्नुहोस् ताकि जोखिम र सीमाहरूको बारेमा जानकारी प्राप्त गर्न सकियोस्।

यी जोखिमहरू कम गर्नको लागि सिफारिस गरिएको दृष्टिकोण भनेको तपाईंको आर्किटेक्चरमा सुरक्षा प्रणाली समावेश गर्नु हो, जसले हानिकारक व्यवहार पत्ता लगाउन र रोक्न सक्छ। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) एक स्वतन्त्र सुरक्षा तह प्रदान गर्दछ, जसले प्रयोगकर्ता-निर्मित र AI-निर्मित सामग्रीलाई हानिकारक सामग्रीको रूपमा पत्ता लगाउन सक्षम छ। Azure AI Content Safety मा पाठ र छवि API समावेश छ, जसले हानिकारक सामग्री पत्ता लगाउन मद्दत गर्दछ। Azure AI Foundry भित्र, Content Safety सेवाले विभिन्न मोडालिटीहरूमा हानिकारक सामग्री पत्ता लगाउन नमूना कोड हेर्न, अन्वेषण गर्न र प्रयास गर्न अनुमति दिन्छ। [Quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ले सेवा अनुरोध गर्न मार्गदर्शन गर्दछ।

अर्को पक्ष भनेको समग्र अनुप्रयोग प्रदर्शन हो। बहु-मोडालिटी र बहु-मोडेल अनुप्रयोगहरूसँग, प्रदर्शनको अर्थ प्रणालीले तपाईं र तपाईंका प्रयोगकर्ताहरूको अपेक्षाहरू पूरा गर्छ, जसमा हानिकारक आउटपुटहरू उत्पन्न नगर्ने पनि समावेश छ। तपाईंको समग्र अनुप्रयोगको प्रदर्शन मूल्याङ्कन गर्न [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) प्रयोग गर्न महत्त्वपूर्ण छ। तपाईंले [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) सिर्जना र मूल्याङ्कन गर्न पनि सक्नुहुन्छ।

तपाईं आफ्नो विकास वातावरणमा [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) प्रयोग गरेर आफ्नो AI अनुप्रयोग मूल्याङ्कन गर्न सक्नुहुन्छ। परीक्षण डेटासेट वा लक्ष्य दिएर, तपाईंको जेनेरेटिभ AI अनुप्रयोगको उत्पादनहरूलाई तपाईंको रोजाइका बिल्ट-इन वा कस्टम मूल्याङ्कनकर्ताहरूले मात्रात्मक रूपमा मापन गरिन्छ। Azure AI Evaluation SDK प्रयोग गरेर प्रणाली मूल्याङ्कन गर्न सुरु गर्न, तपाईं [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) अनुसरण गर्न सक्नुहुन्छ। एकपटक मूल्याङ्कन रन कार्यान्वयन गरेपछि, तपाईं [Azure AI Foundry मा नतिजाहरू देख्न सक्नुहुन्छ](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)।

## ट्रेडमार्कहरू

यस परियोजनामा परियोजनाहरू, उत्पादनहरू, वा सेवाहरूका लागि ट्रेडमार्क वा लोगोहरू समावेश हुन सक्छ। Microsoft ट्रेडमार्क वा लोगोहरूको अधिकृत प्रयोग [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) पालना गर्नुपर्छ।  
यस परियोजनाको परिमार्जित संस्करणहरूमा Microsoft ट्रेडमार्क वा लोगोहरूको प्रयोगले भ्रम उत्पन्न गर्नु हुँदैन वा Microsoft प्रायोजनको संकेत गर्नु हुँदैन। तेस्रो-पक्ष ट्रेडमार्क वा लोगोहरूको कुनै पनि प्रयोग ती तेस्रो-पक्षको नीतिहरूको अधीनमा हुन्छ।

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी यथार्थताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटि वा अशुद्धता हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।