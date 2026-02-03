# Phi कुकबुक: Microsoft का Phi मोडेलहरूसँग हातेमालो गर्ने उदाहरणहरू

[![GitHub Codespaces मा नमूनाहरू खोल्नुहोस् र प्रयोग गर्नुहोस्](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers मा खोल्नुहोस्](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub सहयोगीहरू](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub इश्यूहरू](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub पुल-रिक्वेस्टहरू](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR स्वागतयोग्य](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub वाचरहरू](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub फोर्कहरू](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub स्टारहरू](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi Microsoft द्वारा विकास गरिएको खुला स्रोत AI मोडेलहरूको श्रृंखला हो।

Phi हाल सबैभन्दा शक्तिशाली र लागत-प्रभावकारी सानो भाषा मोडेल (SLM) हो, जसले बहुभाषिक, तर्क, पाठ/च्याट उत्पादन, कोडिङ, छवि, अडियो र अन्य परिदृश्यमा धेरै राम्रो प्रदर्शन देखाउँछ।

तपाईं Phi लाई क्लाउड वा एज उपकरणहरूमा तैनाथ गर्न सक्नुहुन्छ, र सीमित कम्प्युटिङ शक्ति प्रयोग गर्दै सजिलैसँग जनरेटिभ AI एप्लिकेसनहरू निर्माण गर्न सक्नुहुन्छ।

यी स्रोतहरू प्रयोग गरेर सुरु गर्न यी चरणहरू पालना गर्नुहोस्:
1. **रिपोजिटरीलाई फोर्क गर्नुहोस्**: क्लिक गर्नुहोस् [![GitHub फोर्कहरू](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **रिपोजिटरी क्लोन गर्नुहोस्**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord कम्युनिटीमा सामेल हुनुहोस् र विशेषज्ञ तथा अन्य विकासकर्ताहरूलाई भेट्नुहोस्**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/ne/cover.eb18d1b9605d754b.webp)

### 🌐 बहुभाषिक समर्थन

#### GitHub Action मार्फत समर्थित (स्वचालित र सधैं अपडेट हुने)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](./README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **स्थानीय रूपमा क्लोन गर्न प्राथमिकता दिनुहुन्छ?**

> यस रिपोजिटरीमा ५०+ भाषा अनुवादहरू छन् जसले डाउनलोड साइज धेरै बढाउँछ। भाषाहरू बिना क्लोन गर्न स्पार्स चेकआउट प्रयोग गर्नुहोस्:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> यसले तपाईंलाई कोर्स पूरा गर्न आवश्यक सबै सामग्री धेरै छिटो डाउनलोड गर्दै दिन्छ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## विषय सूची

- परिचय
  - [Phi परिवारमा स्वागत छ](./md/01.Introduction/01/01.PhiFamily.md)
  - [आफ्नो वातावरण सेट अप गर्ने तरिका](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [प्रमुख प्रविधिहरू बुझ्न](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi मोडेलहरूको लागि AI सुरक्षा](./md/01.Introduction/01/01.AISafety.md)
  - [Phi हार्डवेयर समर्थन](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi मोडेलहरू र प्लेटफर्महरूमा उपलब्धता](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai र Phi को प्रयोग](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub मार्केटप्लेस मोडेलहरू](https://github.com/marketplace/models)
  - [Azure AI मोडेल क्याटलग](https://ai.azure.com)

- विभिन्न वातावरणहरूमा Phi इनफरेन्स
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub मोडेलहरू](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry मोडेल क्याटलग](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry स्थानीय](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi परिवारको इनफरेन्स
    - [iOS मा Phi को इनफरेन्स](./md/01.Introduction/03/iOS_Inference.md)
    - [Android मा Phi को इनफरेन्स](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson मा Phi को इनफरेन्स](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC मा Phi को इनफरेन्स](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX फ्रेमवर्क सहित Phi को इनफरेन्स](./md/01.Introduction/03/MLX_Inference.md)
    - [स्थानिय सर्भरमा Phi को इनफरेन्स](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit प्रयोग गरेर रिमोट सर्भरमा Phi को इनफरेन्स](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust सहित Phi को इनफरेन्स](./md/01.Introduction/03/Rust_Inference.md)
    - [स्थानियमा Phi--भिजन इनफरेन्स](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (आधिकारिक समर्थन) सहित Phi को इनफरेन्स](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi परिवारको क्वान्टिफाइङ](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp प्रयोग गरेर Phi-3.5 / 4 को क्वान्टाइजिङ](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime को लागि जनरेटिभ AI एक्स्टेन्सनहरू प्रयोग गरेर Phi-3.5 / 4 को क्वान्टाइजिङ](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO प्रयोग गरेर Phi-3.5 / 4 को क्वान्टाइजिङ](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX फ्रेमवर्क प्रयोग गरेर Phi-3.5 / 4 को क्वान्टाइजिङ](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi मूल्याङ्कन
    - [जिम्मेवार AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [मूल्याङ्कनका लागि Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [मूल्याङ्कनका लागि Promptflow को प्रयोग](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI खोजसँग RAG
    - [Azure AI खोजसँग Phi-4-mini र Phi-4-multimodal (RAG) कसरी प्रयोग गर्ने](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi एप्लिकेसन विकास नमूना
  - पाठ र च्याट एप्लिकेसनहरू
    - Phi-4 नमूनाहरू 🆕
      - [📓] [Phi-4-mini ONNX मोडेलसँग च्याट गर्नुहोस्](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 स्थानीय ONNX मोडेल .NET सँग च्याट गर्नुहोस्](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Semantic Kernel प्रयोग गर्दै Phi-4 ONNX सँग .NET कन्सोल एप्लिकेसनमा च्याट गर्नुहोस्](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 नमूनाहरू
      - [Phi3, ONNX Runtime Web र WebGPU सँग ब्राउजरमा स्थानीय च्याटबोट](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino च्याट](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [बहु मोडेल - अन्तरक्रियात्मक Phi-3-मिनी र OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Phi-3 सँग एजम्पर बनाउने र MLFlow प्रयोग गर्ने](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [मोडेल अनुकूलन - Olive सँग ONNX Runtime Web का लागि Phi-3-मिन मोडेल कसरी अनुकूलन गर्ने](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 मिनी-4k-निर्देशन-onnx सँग WinUI3 एप](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 बहु मोडेल एआई सञ्चालित नोट्स एप नमूना](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Prompt flow सँग अनुकूलित Phi-3 मोडेलहरूलाई फाइन-ट्यून र एकीकरण गर्ने](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry मा Prompt flow सँग अनुकूलित Phi-3 मोडेलहरूलाई फाइन-ट्यून र एकीकरण गर्ने](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Azure AI Foundry मा माईक्रोसफ्टको जिम्मेवार AI सिद्धान्तहरूमा केन्द्रित फाइन-ट्यून गरिएको Phi-3 / Phi-3.5 मोडेलको मूल्यांकन गर्ने](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-मिनी-निर्देशन भाषा पूर्वानुमान नमूना (चिनी/अंग्रेजी)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-निर्देशन WebGPU RAG च्याटबोट](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU प्रयोग गरेर Phi-3.5-निर्देशन ONNX सँग Prompt flow समाधान बनाउने](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [माइक्रोसफ्ट Phi-3.5 tflite प्रयोग गरेर Android एप बनाउने](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime प्रयोग गर्दै स्थानीय ONNX Phi-3 मोडेलसहित Q&A .NET उदाहरण](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel र Phi-3 सँग कन्सोल च्याट .NET एप](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK कोड आधारित नमूनाहरू 
    - Phi-4 नमूनाहरू 🆕
      - [📓] [Phi-4-मल्टि मोडलबाट परियोजना कोड उत्पन्न गर्ने](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 नमूनाहरू
      - [माइक्रोसफ्ट Phi-3 परिवारसँग आफ्नो Visual Studio Code GitHub Copilot Chat बनाउनुहोस्](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub मोडेलहरू प्रयोग गरेर Phi-3.5 सहित आफ्नो Visual Studio Code Chat Copilot Agent सिर्जना गर्नुहोस्](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - उन्नत तर्क नमूनाहरू
    - Phi-4 नमूनाहरू 🆕
      - [📓] [Phi-4-मिनी-तर्क वा Phi-4-तर्क नमूनाहरू](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [माइक्रोसफ्ट Olive सँग Phi-4-मिनी-तर्क फाइन-ट्यून गर्ने](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX सँग Phi-4-मिनी-तर्क फाइन-ट्यून गर्ने](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub मोडेलहरूसँग Phi-4-मिनी-तर्क](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry मोडेलहरूसँग Phi-4-मिनी-तर्क](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - डेमोहरू
      - [Hugging Face Spaces मा होस्ट गरिएको Phi-4-मिनी डेमोहरू](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Hugging Face Spaces मा होस्ट गरिएको Phi-4-मल्टिमोडल डेमोहरू](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - भिजन नमूनाहरू
    - Phi-4 नमूनाहरू 🆕
      - [📓] [Phi-4-मल्टिमोडल प्रयोग गरेर छविहरू पढ्ने र कोड उत्पन्न गर्ने](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 नमूनाहरू
      -  [📓][Phi-3-भिजन-छवि पाठबाट पाठमा](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-भिजन-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-भिजन CLIP एम्बेडिङ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [डेमो: Phi-3 रीसाइकलिंग](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-भिजन - दृश्य भाषा सहायक - Phi3-भिजन र OpenVINO सँग](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 भिजन Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 भिजन OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 भिजन बहु-फ्रेम वा बहु-छवि नमूना](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET प्रयोग गरेर Phi-3 भिजन स्थानीय ONNX मोडेल](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [मेनु आधारित Phi-3 भिजन स्थानीय ONNX मोडेल Microsoft.ML.OnnxRuntime .NET प्रयोग गरेर](../../md/04.HOL/dotnet/src/LabsPhi304)

  - गणित नमूनाहरू
    -  Phi-4-मिनी-फ्ल्यास-तर्क-निर्देशन नमूनाहरू 🆕 [Phi-4-मिनी-फ्ल्यास-तर्क-निर्देशन सहित गणित डेमो](./md/02.Application/09.Math/MathDemo.ipynb)

  - अडियो नमूनाहरू
    - Phi-4 नमूनाहरू 🆕
      - [📓] [Phi-4-मल्टिमोडल प्रयोग गरेर अडियो लिप्यन्तरण निकाल्ने](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-मल्टिमोडल अडियो नमूना](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-मल्टिमोडल भाषण अनुवाद नमूना](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [Phi-4-मल्टिमोडल अडियो प्रयोग गरेर अडियो फाइल विश्लेषण र लिप्यन्तरण उत्पन्न गर्ने .NET कन्सोल एप्लिकेसन](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE नमूनाहरू
    - Phi-3 / 3.5 नमूनाहरू
      - [📓] [Phi-3.5 विशेषज्ञ मिश्रण मोडेलहरू (MoEs) सामाजिक मिडिया नमूना](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, र LlamaIndex सँग Retrieval-Augmented Generation (RAG) पाइपलाइन बनाउने](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - कार्यसम्पादन कलिङ नमूनाहरू
    - Phi-4 नमूनाहरू 🆕
      -  [📓] [Phi-4-मिनी सँग कार्यसम्पादन कलिङ प्रयोग गर्ने](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-मिनी सँग बहु-एजेन्टहरू सिर्जना गर्न कार्यसम्पादन कलिङ प्रयोग गर्ने](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama सँग कार्यसम्पादन कलिङ प्रयोग गर्ने](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX सँग कार्यसम्पादन कलिङ प्रयोग गर्ने](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - मल्टिमोडल मिश्रण नमूनाहरू
    - Phi-4 नमूनाहरू 🆕
      -  [📓] [प्रविधि पत्रकारको रूपमा Phi-4-मल्टिमोडल प्रयोग गर्ने](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET कन्सोल एप्लिकेसन जसले Phi-4-मल्टिमोडल प्रयोग गरेर छविहरू विश्लेषण गर्छ](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- फाइन-ट्यूनिङ Phi नमूनाहरू
  - [फाइन-ट्यूनिङ दृश्यहरू](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [फाइन-ट्यूनिङ र RAG को तुलनात्मक विश्लेषण](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 लाई उद्योग विशेषज्ञ बनाउन फाइन-ट्यूनिङ](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code को लागि AI उपकरण किटसहित Phi-3 फाइन-ट्यूनिङ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning सेवा सँग Phi-3 फाइन-ट्यूनिङ](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora सँग Phi-3 फाइन-ट्यूनिङ](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora सँग Phi-3 फाइन-ट्यूनिङ](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry सँग Phi-3 फाइन-ट्यूनिङ](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK सँग Phi-3 फाइन-ट्यूनिङ](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive सँग फाइन-ट्यूनिङ](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Lab सँग फाइन-ट्यूनिङ](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias प्रयोग गरेर Phi-3-भिजन फाइन-ट्यूनिङ](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework सँग Phi-3 फाइन-ट्यूनिङ](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-भिजन (आधिकारिक समर्थन)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS , Azure Containers (आधिकारिक समर्थन) सहित Phi-3 फाइन-ट्यूनिङ](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 र 3.5 भिजन फाइन-ट्यूनिङ](https://github.com/2U1/Phi3-Vision-Finetune)

- प्रयोगात्मक कार्यशाला
  - [उन्नत मोडेलहरूको अन्वेषण: LLMs, SLMs, स्थानीय विकास र अन्य](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP क्षमता अनलकिंग: Microsoft Olive सँग फाइन-ट्यूनिङ](https://github.com/azure/Ignite_FineTuning_workshop)

- शैक्षिक अनुसन्धान कागजातहरू र प्रकाशनहरू
  - [पाठ्यपुस्तकहरू मात्र तपाईंलाई आवश्यक छ II: phi-1.5 प्राविधिक रिपोर्ट](https://arxiv.org/abs/2309.05463)
  - [Phi-3 प्राविधिक रिपोर्ट: तपाईँको फोनमा स्थानीय रूपमा अत्यन्त सक्षम भाषा मोडेल](https://arxiv.org/abs/2404.14219)
  - [Phi-4 प्राविधिक रिपोर्ट](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini प्राविधिक रिपोर्ट: मिश्रण-को-LoRAs मार्फत स-सानो तर शक्तिशाली बहुमाध्यम भाषा मोडेलहरू](https://arxiv.org/abs/2503.01743)
  - [सवारीसाधन कार्यकारी कलिंगका लागि साना भाषा मोडेलहरू अनुकूलन गर्दै](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) बहुविकल्प प्रश्न उत्तरका लागि PHI-3 को राम्रो प्रशिक्षण: पद्धति, नतिजा, र चुनौतीहरू](https://arxiv.org/abs/2501.01588)
  - [Phi-4-तर्क प्राविधिक रिपोर्ट](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-मिनी-तर्क प्राविधिक रिपोर्ट](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi मोडेलहरूको प्रयोग

### Azure AI Foundry मा Phi

तपाईंले Microsoft Phi कसरी प्रयोग गर्ने र विभिन्न हार्डवेयर उपकरणहरूमा E2E समाधानहरू कसरी निर्माण गर्ने सिक्न सक्नुहुन्छ। आफैं Phi अनुभव गर्न, मोडेलहरूसँग खेल्न सुरु गर्नुहोस् र तपाईँका परिदृश्यहरूका लागि Phi अनुकूलन गर्नुहोस् [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) प्रयोग गरेर। तपाईं [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) बाट सुरु गर्ने बारे थप जान्न सक्नुहुन्छ।

**प्लेसग्राउण्ड**  
प्रत्येक मोडेलसँग मोडेल परीक्षणको लागि समर्पित प्लेसग्राउण्ड छ [Azure AI Playground](https://aka.ms/try-phi3)।

### GitHub मोडेलहरूमा Phi

तपाईं Microsoft Phi कसरी प्रयोग गर्ने र विभिन्न हार्डवेयर उपकरणहरूमा E2E समाधानहरू कसरी निर्माण गर्ने सिक्न सक्नुहुन्छ। आफैं Phi अनुभव गर्न, मोडेलसँग खेल्न सुरु गर्नुहोस् र आफ्नो परिदृश्यहरूको लागि Phi अनुकूलन गर्नुहोस् [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) प्रयोग गरेर। तपाईं [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) बाट सुरु गर्ने बारे थप जान्न सक्नुहुन्छ।

**प्लेसग्राउण्ड**  
प्रत्येक मोडेलसँग मोडेल परीक्षणको लागि समर्पित [प्लेसग्राउण्ड](/md/02.QuickStart/GitHubModel_QuickStart.md) छ।

### Hugging Face मा Phi

तपाईं मोडेल [Hugging Face](https://huggingface.co/microsoft) मा पनि फेला पार्न सक्नुहुन्छ।

**प्लेसग्राउण्ड**  
[Hugging Chat प्लेसग्राउण्ड](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 अन्य पाठ्यक्रमहरू

हाम्रो टोलीले अन्य पाठ्यक्रमहरू उत्पादन गर्दछ! यी जाँच गर्नुहोस्:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Core Learning
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Series
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## जिम्मेवार AI

Microsoft हाम्रा ग्राहकहरूलाई हाम्रो AI उत्पादनहरू जिम्मेवार तरिकाले प्रयोग गर्न सहयोग पुर्‍याउन प्रतिबद्ध छ, हाम्रो सिकाइहरू साझा गर्दै, र पारदर्शिता नोटहरू र प्रभाव मूल्यांकनहरू जस्ता उपकरणहरू मार्फत विश्वास आधारित साझेदारीहरू निर्माण गर्दै। यी मध्ये धेरै स्रोतहरू [https://aka.ms/RAI](https://aka.ms/RAI) मा भेट्न सकिन्छ।  
Microsoft को जिम्मेवार AI को दृष्टिकोण हाम्रो AI सिद्धान्तहरूमा आधारित छ, जसमा न्याय, विश्वासनीयता र सुरक्षा, गोपनीयता र सुरक्षा, समावेशी, पारदर्शिता, र जवाफदेहिता छन्।

ठूलो-परिमाण प्राकृतिक भाषा, छवि, र आवाज मोडेलहरू - जस्तै यस नमूनामा प्रयोग गरिएका - सम्भवतः अन्यायपूर्ण, अविश्वसनीय, वा आक्रामक तरिकाले व्यवहार गर्न सक्छन्, जसले हानिहरू निम्त्याउन सक्छ। कृपया जोखिमहरू र सीमाहरू बारे जानकारी पाउन [Azure OpenAI सेवा पारदर्शिता नोट](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) सल्लाह लिनुहोस्।

यी जोखिमहरूलाई घटाउने सिफारिस गरिएको तरिका हो तपाईंको वास्तुकलामा एउटा सुरक्षा प्रणाली समावेश गर्ने जुन हानिकारक व्यवहार पत्ता लगाउन र रोक्न सक्छ। [Azure AI सामग्री सुरक्षा](https://learn.microsoft.com/azure/ai-services/content-safety/overview) एक स्वतन्त्र सुरक्षा तह प्रदान गर्दछ, जुन अनुप्रयोगहरू र सेवाहरूमा हानिकारक प्रयोगकर्ता-निर्मित र AI-निर्मित सामग्री पत्ता लगाउन सक्षम छ। Azure AI सामग्री सुरक्षा मा टेक्स्ट र छवि APIहरू समावेश छन् जसले हानिकारक सामग्री पत्ता लगाउन अनुमति दिन्छ। Azure AI Foundry भित्र, सामग्री सुरक्षा सेवा विभिन्न मोडलिटीजमा हानिकारक सामग्री पत्ता लगाउन नमूना कोड हेर्न, अन्वेषण गर्न, र प्रयास गर्न अनुमति दिन्छ। तलको [द्रुत सुरु कागजात](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) तपाईंलाई सेवामा अनुरोधहरू गर्ने तरिका मार्गनिर्देशन गर्दछ।
अर्को पक्षमा पुरा अनुप्रयोगको प्रदर्शनलाई विचार गर्नु पर्छ। बहु-मोडल र बहु-मोडेल अनुप्रयोगहरूमा, हामीले प्रदर्शन भन्नाले प्रणाली तपाईं र तपाईंका प्रयोगकर्ताहरूले अपेक्षा गरेजस्तो काम गर्दछ, जसमा हानिकारक आउटपुट उत्पादन नगर्ने कुरा पनि समावेश छ। तपाईंले आफ्नो पुरा अनुप्रयोगको प्रदर्शन मापन गर्न [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) को प्रयोग गर्नु महत्त्वपूर्ण छ। तपाईंले [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) सिर्जना गरी मूल्याङ्कन गर्न सक्ने क्षमता पनिहरू छ।

तपाईं आफ्नो विकास वातावरणमा [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) को प्रयोग गरेर आफ्नो AI अनुप्रयोग मूल्याङ्कन गर्न सक्नुहुन्छ। परीक्षण डेटासेट वा लक्ष्य दिइएपछि, तपाईंको जेनेरेटिभ AI अनुप्रयोगका उत्पादनहरू तपाईंले रोज्नु भएको बिल्ट-इन वा अनुकूल evaluators द्वारा मात्रात्मक रूपमा मापन गरिन्छ। आफ्नो प्रणाली मूल्याङ्कन गर्न Azure AI Evaluation SDK प्रयोग गर्ने सुरु गर्न, तपाईं [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) लाई अनुसरण गर्न सक्नुहुन्छ। एक पटक मूल्याङ्कन चलाएपछि, तपाईंले परिणामहरू [Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) मा visualization गर्न सक्नुहुन्छ।

## ट्रेडमार्कहरू

यो परियोजनाले परियोजना, उत्पादन, वा सेवाहरूका लागि ट्रेडमार्कहरू वा लोगोहरू समावेश गर्न सक्छ। Microsoft का ट्रेडमार्कहरू वा लोगोहरूको अधिकृत प्रयोगको लागि [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) पछ्याउन आवश्यक छ। यस परियोजनाको परिमार्जित संस्करणहरूमा Microsoft का ट्रेडमार्क वा लोगोहरूको प्रयोगले भ्रम उत्पन्न गर्नु हुँदैन वा Microsoft प्रायोजन भएको संकेत गर्नु हुँदैन। तेस्रो पक्षका ट्रेडमार्क वा लोगोहरू प्रयोग गर्दा ती पक्षका नीति अनुसार हुनु पर्छ।

## सहयोग पाउन

यदि तपाईं अल्झन्नुभयो वा AI अनुप्रयोग निर्माण सम्बन्धी प्रश्न छ भने, निम्न स्थानमा सामेल हुनुहोस्:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

यदि तपाईंलाई उत्पादन प्रतिक्रिया वा त्रुटि छ भने, यहाँ जानुहोस्:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यस दस्तावेजलाई AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं भने पनि, कृपया कुरा बुझ्नुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यस भाषामा रहेको स्रोत मानिनेछ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानवीय अनुवादको सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->