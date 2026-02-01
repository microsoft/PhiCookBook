# फाइ कुकबुक: माइक्रोसफ्टका फाइ मोडेलहरूसँग हातेमालो गर्दै उदाहरणहरू

[![GitHub Codespaces मा नमूनाहरू खोल्नुहोस् र प्रयोग गर्नुहोस्](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers मा खोल्नुहोस्](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub योगदानकर्ताहरू](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub समस्या](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub पुल अनुरोधहरू](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PR हरू स्वागत छन्](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub वेचरहरू](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub फोर्कहरू](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub स्टारहरू](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

फाइ माइक्रोसफ्टद्वारा विकास गरिएको खुला स्रोत AI मोडेलहरूको श्रृंखला हो।

फाइ अहिले सबैभन्दा शक्तिशाली र लागत-कुशल सानो भाषा मोडेल (SLM) हो, जसले बहुभाषिक, तर्क, पाठ/च्याट सिर्जना, कोडिङ, छविहरू, अडियो र अन्य परिदृश्यहरूमा राम्रो असरहरू देखाउँछ।

तपाईं फाइलाई क्लाउडमा वा एज उपकरणहरूमा तैनाथ गर्न सक्नुहुन्छ, र सीमित कम्प्युटिङ शक्ति साथ सजिलै रूपमा जनरेटिभ AI अनुप्रयोगहरू निर्माण गर्न सक्नुहुन्छ।

यी संसाधनहरू प्रयोग गर्न सुरु गर्ने चरणहरू पछ्याउनुहोस्:
1. **रेपो फोर्क गर्नुहोस्**: क्लिक गर्नुहोस् [![GitHub फोर्कहरू](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **रेपो क्लोन गर्नुहोस्**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord समुदायमा सामेल हुनुहोस् र विशेषज्ञ तथा सह-डेभलपर्ससँग भेट्नुहोस्**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/ne/cover.eb18d1b9605d754b.webp)

### 🌐 बहुभाषिक समर्थन

#### GitHub Action मार्फत समर्थित (स्वचालित र सधैं अपडेट रहने)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरबी](../ar/README.md) | [बंगाली](../bn/README.md) | [बुल्गेरियन](../bg/README.md) | [बर्मी (म्यानमार)](../my/README.md) | [चीनियाँ (सरलीकृत)](../zh-CN/README.md) | [चीनियाँ (परम्परागत, हङकङ)](../zh-HK/README.md) | [चीनियाँ (परम्परागत, मकाउ)](../zh-MO/README.md) | [चीनियाँ (परम्परागत, ताइवान)](../zh-TW/README.md) | [क्रोएसियन](../hr/README.md) | [चेक](../cs/README.md) | [ड्यानिश](../da/README.md) | [डच](../nl/README.md) | [एस्चोनियन](../et/README.md) | [फिन्निश](../fi/README.md) | [फ्रेन्च](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रु](../he/README.md) | [हिन्दी](../hi/README.md) | [हंगेरीयन](../hu/README.md) | [इन्डोनेसियन](../id/README.md) | [इटालियन](../it/README.md) | [जापानी](../ja/README.md) | [कन्नड](../kn/README.md) | [कोरियन](../ko/README.md) | [लिथुनियन](../lt/README.md) | [मलय](../ms/README.md) | [मलयालम](../ml/README.md) | [मराठी](../mr/README.md) | [नेपाली](./README.md) | [नाइजेरियन पिड्गिन](../pcm/README.md) | [नर्वेजियन](../no/README.md) | [फारसी (पर्सियन)](../fa/README.md) | [पोलिश](../pl/README.md) | [पोर्चुगिज (ब्राजिल)](../pt-BR/README.md) | [पोर्चुगिज (पुर्तगाल)](../pt-PT/README.md) | [पञ्जाबी (गुरुमुखी)](../pa/README.md) | [रोमानियन](../ro/README.md) | [रुसियन](../ru/README.md) | [सर्बियन (सिरिलिक)](../sr/README.md) | [स्लोभाक](../sk/README.md) | [स्लोभेनीयन](../sl/README.md) | [स्पेनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिस](../sv/README.md) | [टगालोग (फिलिपिनो)](../tl/README.md) | [तमिल](../ta/README.md) | [तेलुगु](../te/README.md) | [थाई](../th/README.md) | [टर्किस](../tr/README.md) | [यूक्रेनीयन](../uk/README.md) | [उर्दू](../ur/README.md) | [भियतनामी](../vi/README.md)

> **स्थानीय रूपमा क्लोन गर्न मन छ?**

> यो रिपोजिटोरी ५०+ भाषाको अनुवादहरू समावेश गर्दछ जसले डाउनलोड साइजलाई उल्लेखनीय रूपमा बढाउन सक्छ। अनुवादहरू बिना क्लोन गर्न, sparse checkout प्रयोग गर्नुहोस्:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> यसले तपाईंलाई कोर्स पूरा गर्न आवश्यक सबै दिन्छ र डाउनलोड छिटो हुन्छ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## सामग्री तालिका

- परिचय
  - [फाइ परिवारमा स्वागत छ](./md/01.Introduction/01/01.PhiFamily.md)
  - [आफ्नो वातावरण सेटअप गर्दै](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [प्रमुख प्रविधिहरू बुझ्दै](./md/01.Introduction/01/01.Understandingtech.md)
  - [फाइ मोडेलहरूको लागि AI सुरक्षा](./md/01.Introduction/01/01.AISafety.md)
  - [फाइ हार्डवेयर समर्थन](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [फाइ मोडेलहरू र प्ल्याटफर्महरूमा उपलब्धता](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai र फाइ प्रयोग गर्दै](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace मोडेलहरू](https://github.com/marketplace/models)
  - [Azure AI मोडेल सूची](https://ai.azure.com)

- विभिन्न वातावरणमा फाइ इन्फरेन्स
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub मोडेलहरू](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry मोडेल सूची](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- फाइ परिवारमा इन्फरेन्स
    - [iOS मा फाइ इन्फरेन्स](./md/01.Introduction/03/iOS_Inference.md)
    - [Android मा फाइ इन्फरेन्स](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson मा फाइ इन्फरेन्स](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC मा फाइ इन्फरेन्स](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX फ्रेमवर्कद्वारा फाइ इन्फरेन्स](./md/01.Introduction/03/MLX_Inference.md)
    - [स्थानीय सर्भरमा फाइ इन्फरेन्स](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit उपयोग गरेर रिमोट सर्भरमा फाइ इन्फरेन्स](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust सँग फाइ इन्फरेन्स](./md/01.Introduction/03/Rust_Inference.md)
    - [स्थानीयमा फाइ--भिजन इन्फरेन्स](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (आधिकारिक समर्थन) सँग फाइ इन्फरेन्स](./md/01.Introduction/03/Kaito_Inference.md)
-  [फाइ परिवार क्वान्टिफाइ गर्दै](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp प्रयोग गरेर Phi-3.5 / 4 को क्वान्टाइजिङ](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime का लागि जनरेटिभ AI एक्सटेन्सनहरू प्रयोग गरेर Phi-3.5 / 4 को क्वान्टाइजिङ](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO प्रयोग गरेर Phi-3.5 / 4 को क्वान्टाइजिङ](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX फ्रेमवर्क प्रयोग गरेर Phi-3.5 / 4 को क्वान्टाइजिङ](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- फाइ मूल्यांकन
    - [जिम्मेवार AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [मूल्यांकनका लागि Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [मूल्यांकनका लागि Promptflow प्रयोग गर्दै](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search सँग RAG
    - [Phi-4-mini र Phi-4-multimodal (RAG) Azure AI Search सँग कसरी प्रयोग गर्ने](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- फाइ अनुप्रयोग विकास नमूनाहरू
  - पाठ र च्याट अनुप्रयोगहरू
    - Phi-4 नमूनाहरू 🆕
      - [📓] [Phi-4-mini ONNX मोडेलसँग च्याट गर्नुहोस्](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [स्थानीय ONNX मोडेल Phi-4 सँग च्याट .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Semantic Kernel प्रयोग गरेर Phi-4 ONNX सँग .NET कन्सोल एपमा च्याट](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 नमूनाहरू
      - [Phi3, ONNX Runtime Web र WebGPU उपयोग गरी ब्राउजरमा स्थानीय च्याटबोट](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino च्याट](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [मल्टि मोडेल - अन्तरक्रियात्मक Phi-3-मिनी र OpenAI व्हिस्पर](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - एक र्यापर बनाउँदै र MLFlow सँग Phi-3 को प्रयोग गर्दै](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [मोडेल अनुकूलन - कसरी Phi-3-मिनि मोडेललाई ONNX Runtime Web संग Olive मार्फत अनुकूलन गर्ने](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 एप Phi-3 मिनी-4k-instruct-onnx सँग](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 मल्टि मोडेल AI संचालित नोट्स एप नमूना](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [कस्टम Phi-3 मोडेलहरूलाई Prompt flow सँग फाइन-ट्युन र इंटिग्रेट गर्ने](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry मा Prompt flow सँग कस्टम Phi-3 मोडेलहरू फाइन-ट्युन र इंटिग्रेट गर्ने](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft को उत्तरदायी AI सिद्धान्तहरूमा ध्यान केन्द्रित गर्दै Azure AI Foundry मा फाइन-ट्युन गरिएको Phi-3 / Phi-3.5 मोडेलको मूल्यांकन गर्नुहोस्](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-मिनी-इन्स्ट्रक्ट भाषा भविष्यवाणी नमूना (चिनियाँ/अंग्रेजी)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-इन्स्ट्रक्ट WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU प्रयोग गरेर Phi-3.5-इन्स्ट्रक्ट ONNX सँग Prompt flow समाधान बनाउने](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite प्रयोग गरेर Android एप बनाउने](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [स्थानिय ONNX Phi-3 मोडेल प्रयोग गर्दै Microsoft.ML.OnnxRuntime प्रयोग गरी Q&A .NET उदाहरण](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel र Phi-3 सहित कन्सोल च्याट .NET एप](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK कोड आधारित नमूनाहरू
    - Phi-4 नमूनाहरू 🆕
      - [📓] [Phi-4-मल्टिमोडल प्रयोग गरेर प्रोजेक्ट कोड उत्पन्न गर्नुहोस्](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 नमूनाहरू
      - [Microsoft Phi-3 परिवारसहित आफ्नो Visual Studio Code GitHub Copilot Chat बनाउनुहोस्](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub मोडेलहरूसँग Phi-3.5 का साथ आफ्नो Visual Studio Code Chat Copilot एजेन्ट बनाउनुहोस्](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - उन्नत तर्क नमूनाहरू
    - Phi-4 नमूनाहरू 🆕
      - [📓] [Phi-4-मिनी-तर्क वा Phi-4-तर्क नमूनाहरू](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive सँग Phi-4-मिनी-तर्कको फाइन-ट्युनिङ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX सँग Phi-4-मिनी-तर्कको फाइन-ट्युनिङ](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub मोडेलहरूले Phi-4-मिनी-तर्क](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry मोडेलहरूसँग Phi-4-मिनी-तर्क](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - डेमोहरू
      - [Phi-4-मिनी डेमोहरू Hugging Face Spaces मा होस्ट गरिएको](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-मल्टिमोडल डेमोहरू Hugging Face Spaces मा होस्ट गरिएको](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - भिजन नमूनाहरू
    - Phi-4 नमूनाहरू 🆕
      - [📓] [चित्रहरू पढ्न र कोड उत्पन्न गर्न Phi-4-मल्टिमोडल प्रयोग गर्नुहोस्](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 नमूनाहरू
      -  [📓][Phi-3-भिजन-इमेज टेक्स्टदेखि टेक्स्टसम्म](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-भिजन-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-भिजन CLIP एम्बेडिङ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [डेमो: Phi-3 रिसाइकलिङ](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-भिजन - दृश्य भाषा सहायक - Phi3-भिजन र OpenVINO सँग](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 भिजन Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 भिजन OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 भिजन मल्टि-फ्रे임 वा मल्टि-इमेज नमूना](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET प्रयोग गर्दै Phi-3 भिजन स्थानीय ONNX मोडेल](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [मेनु आधारित Phi-3 भिजन स्थानीय ONNX मोडेल Microsoft.ML.OnnxRuntime .NET सँग](../../md/04.HOL/dotnet/src/LabsPhi304)

  - गणित नमूनाहरू
    - Phi-4-मिनी-फ्ल्यास-तर्क-इन्स्ट्रक्ट नमूनाहरू 🆕 [Phi-4-मिनी-फ्ल्यास-तर्क-इन्स्ट्रक्टसँग गणित डेमो](./md/02.Application/09.Math/MathDemo.ipynb)

  - अडियो नमूनाहरू
    - Phi-4 नमूनाहरू 🆕
      - [📓] [Phi-4-मल्टिमोडल प्रयोग गरेर अडियो ट्रान्सक्रिप्टहरू निकाल्दै](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-मल्टिमोडल अडियो नमूना](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-मल्टिमोडल स्पीच अनुवाद नमूना](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET कन्सोल अनुप्रयोग Phi-4-मल्टिमोडल अडियो प्रयोग गरेर अडियो फाइल विश्लेषण गर्न र ट्रान्सक्रिप्ट निर्माण गर्न](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE नमूनाहरू
    - Phi-3 / 3.5 नमूनाहरू
      - [📓] [Phi-3.5 विशेषज्ञहरूको मिश्र (MoEs) सामाजिक मिडिया नमूना](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, र LlamaIndex सँग Retrieval-Augmented Generation (RAG) पाइपलाइन बनाउँदै](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - फंक्शन कलिङ नमूनाहरू
    - Phi-4 नमूनाहरू 🆕
      -  [📓] [Phi-4-मिनी सँग फंक्शन कलिङ प्रयोग गर्दै](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-मिनी सँग मल्टि-एजेन्ट बनाउन फंक्शन कलिङ प्रयोग गर्दै](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama सँग फंक्शन कलिङ प्रयोग गर्दै](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX सँग फंक्शन कलिङ प्रयोग गर्दै](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - मल्टिमोडल मिक्सिङ नमूनाहरू
    - Phi-4 नमूनाहरू 🆕
      -  [📓] [प्रविधि पत्रकारको रूपमा Phi-4-मल्टिमोडल प्रयोग गर्ने](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET कन्सोल अनुप्रयोग Phi-4-मल्टिमोडल प्रयोग गरी छविहरू विश्लेषण गर्न](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- फाइन-ट्युनिङ Phi नमूनाहरू
  - [फाइन-ट्युनिङ परिदृश्यहरू](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [फाइन-ट्युनिङ विरुद्ध RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 लाई औद्योगिक विशेषज्ञ बन्न दिनुहोस्](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code का लागि AI उपकरण सेटसँग Phi-3 फाइन-ट्युनिङ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service सँग Phi-3 फाइन-ट्युनिङ](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora सँग Phi-3 फाइन-ट्युनिङ](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora सँग Phi-3 फाइन-ट्युनिङ](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry सँग Phi-3 फाइन-ट्युनिङ](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK सँग Phi-3 फाइन-ट्युनिङ](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive सँग फाइन-ट्युनिङ](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Lab सँग फाइन-ट्युनिङ](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias सँग Phi-3-भिजन फाइन-ट्युनिङ](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework सँग Phi-3 फाइन-ट्युनिङ](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-भिजन (आधिकारिक समर्थन) फाइन-ट्युनिङ](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure कन्टेनरहरूसँग Phi-3 फाइन-ट्युनिङ (आधिकारिक समर्थन)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 र 3.5 भिजन फाइन-ट्युनिङ](https://github.com/2U1/Phi3-Vision-Finetune)

- Hands on Lab
  - [अत्याधुनिक मोडेलहरूको अन्वेषण: LLMs, SLMs, स्थानिय विकास र थप](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP क्षमता अनलक गर्नुहोस्: Microsoft Olive सँग फाइन-ट्युनिङ](https://github.com/azure/Ignite_FineTuning_workshop)

- शैक्षिक अनुसन्धान पत्रहरू र प्रकाशनहरू
  - [पाठ्यपुस्तकहरू सबै आवश्यक छन् II: phi-1.5 प्राविधिक प्रतिवेदन](https://arxiv.org/abs/2309.05463)
  - [Phi-3 प्राविधिक प्रतिवेदन: तपाईंको फोनमा स्थानीय रूपमा अत्यधिक सक्षम भाषा मोडल](https://arxiv.org/abs/2404.14219)
  - [Phi-4 प्राविधिक प्रतिवेदन](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini प्राविधिक प्रतिवेदन: मिश्रण-ऑफ-लोरा मार्फत компакт तर शक्तिशाली बहुमुखी भाषा मोडेलहरू](https://arxiv.org/abs/2503.01743)
  - [सवारी साधन भित्रको कार्य-कल्लाई लागि साना भाषा मोडेलहरूको अनुकूलन](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) बहु-चयन प्रश्न उत्तरका लागि PHI-3 को फाइन-ट्यूनिङ: पद्धति, नतिजा, र चुनौतीहरू](https://arxiv.org/abs/2501.01588)
  - [Phi-4-तर्क प्राविधिक प्रतिवेदन](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-तर्क प्राविधिक प्रतिवेदन](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi मोडेलहरूको प्रयोग

### Azure AI Foundry मा Phi

तपाईं Microsoft Phi कसरी प्रयोग गर्ने र विभिन्न हार्डवेयर उपकरणहरूमा E2E समाधानहरू कसरी निर्माण गर्ने जान्न सक्नुहुन्छ। Phi आफैं अनुभव गर्नको लागि, मोडेलहरूसँग खेल्न सुरु गर्नुहोस् र तपाईंका परिदृश्यहरूका लागि Phi अनुकूलित गर्नुहोस् [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) प्रयोग गरेर। तपाईं [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) बाट सुरूवात कसरी गर्ने थप जान्न सक्नुहुन्छ।

**प्लेटग्राउण्ड**
प्रत्येक मोडलको परीक्षणका लागि समर्पित प्लेटग्राउण्ड छ [Azure AI Playground](https://aka.ms/try-phi3)।

### GitHub मोडेलहरूमा Phi

तपाईं Microsoft Phi कसरी प्रयोग गर्ने र विभिन्न हार्डवेयर उपकरणहरूमा E2E समाधानहरू कसरी निर्माण गर्ने जान्न सक्नुहुन्छ। Phi आफैं अनुभव गर्नको लागि, मोडेलसँग खेल्न सुरु गर्नुहोस् र तपाईंका परिदृश्यहरूका लागि Phi अनुकूलित गर्नुहोस् [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) प्रयोग गरेर। तपाईं [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) बाट सुरूवात कसरी गर्ने थप जान्न सक्नुहुन्छ।

**प्लेटग्राउण्ड**
प्रत्येक मोडलको परीक्षणका लागि समर्पित [प्लेटग्राउण्ड](/md/02.QuickStart/GitHubModel_QuickStart.md) छ।

### Hugging Face मा Phi

तपाईं मोडेल [Hugging Face](https://huggingface.co/microsoft) मा पनि फेला पार्न सक्नुहुन्छ।

**प्लेटग्राउण्ड**
 [Hugging Chat प्लेटग्राउण्ड](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 अन्य पाठ्यक्रमहरू

हाम्रो टिमले अन्य पाठ्यक्रमहरू उत्पादन गर्दछ! जाँच गर्नुहोस्:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / एजेन्टहरू
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### जनरेटिभ AI सिरिज
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### मुख्य सिकाइ
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### कोपाइलट सिरिज
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## उत्तरदायी AI 

Microsoft हाम्रा ग्राहकहरूलाई हाम्रो AI उत्पादनहरू जिम्मेवार तरिकाले प्रयोग गर्न मद्दत गर्न प्रतिबद्ध छ, हाम्रा सिकाइहरू साझा गर्ने, र पारदर्शिता नोटहरू र प्रभाव मूल्यांकन जस्ता उपकरणहरू मार्फत विश्वास-आधारित साझेदारीहरू निर्माण गर्ने। यी मध्ये धेरै स्रोतहरू [https://aka.ms/RAI](https://aka.ms/RAI) मा फेला पार्न सकिन्छ।
Microsoft को जिम्मेवार AI दृष्टिकोण हाम्रो न्याय, विश्वसनीयता र सुरक्षा, गोपनीयता र सुरक्षा, समावेशिता, पारदर्शिता, र जवाफदेहिताको AI सिद्धान्तहरूमा आधारित छ।

ठूला-स्तर प्राकृतिक भाषा, छवि, र भाषण मोडेलहरू - यस नमूनामा प्रयोग गरिएका जस्ता - सम्भावित रूपमा अन्यायपूर्ण, अविश्वसनीय, वा आपत्तिजनक व्यवहार गर्न सक्छन्, जसले नतिजा स्वरूप हानि पुर्‍याउन सक्छ। कृपया जोखिम र सीमाहरूको जानकारीका लागि [Azure OpenAI सेवा पारदर्शिता नोट](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) हेर्नुहोस्।

यी जोखिमहरूलाई कम गर्ने सिफारिश गरिएको तरिका भनेको तपाईंको संरचनामा यस्तो सुरक्षा प्रणाली समावेश गर्नु हो जसले हानिकारक व्यवहार पत्ता लगाउन र रोक्न सक्छ। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) एक स्वतन्त्र सुरक्षा तह हो, जसले प्रयोगकर्ता-उत्पादित र AI-उत्पादित हानिकारक सामग्रीहरू पत्ता लगाउन सक्षम छ। Azure AI Content Safety मा पाठ र छवि API हरू छन् जसले तपाईंलाई हानिकारक सामग्री पत्ता लगाउन अनुमति दिन्छ। Azure AI Foundry भित्र, Content Safety सेवा तपाईंलाई फरक-फरक मोडालिटीहरूमा हानिकारक सामग्री पत्ता लगाउन नमूना कोड हेर्न, अन्वेषण गर्न र प्रयास गर्न अनुमति दिन्छ। तलको [द्रुत शुरुवात कागजात](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) सेवा अनुरोध गर्ने प्रक्रिया मार्गनिर्देशन गर्दछ।

अर्को विचार गर्ने पक्ष भनेको समग्र अनुप्रयोग प्रदर्शन हो। बहु-मोडाल र बहु-मोडेल अनुप्रयोगहरूसँग, हामी प्रदर्शनलाई अर्थ लगाउँछौं कि प्रणाली तपाईं र तपाईंका प्रयोगकर्ताहरूले अपेक्षा गरेजस्तो काम गर्दछ, जसमा हानिकारक आउटपुट जनाउन नहुनु पनि समावेश छ। तपाईंले समग्र अनुप्रयोगको प्रदर्शन [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) प्रयोग गरी मूल्याङ्कन गर्न सक्नुहुन्छ। तपाईंसँग [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) सिर्जना र मूल्याङ्कन गर्ने क्षमता पनि छ।
तपाईंले [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) प्रयोग गरी आफ्नो विकास वातावरणमा आफ्नो AI अनुप्रयोगको मूल्याङ्कन गर्न सक्नुहुन्छ। परीक्षण डेटासेट वा लक्ष्य दिइएमा, तपाईंको जेनेरेटिभ AI अनुप्रयोगका उत्पादनहरू बिल्ट-इन मूल्याङ्ककहरू वा तपाईँको रोजाइका अनुकूलित मूल्याङ्ककहरूसँग मात्रात्मक रूपमा मापन गरिन्छ। आफ्नो प्रणाली मूल्याङ्कन गर्न azure ai evaluation sdk प्रयोग गरेर सुरु गर्न, तपाईं [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) अनुसरण गर्न सक्नुहुन्छ। मूल्याङ्कन रन सञ्चालन गरेपछि, तपाईं [Azure AI Foundry मा परिणामहरू दृश्यात्मक रूपमा देख्न](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) सक्नुहुन्छ।

## ट्रेडमार्कहरू

यो परियोजनामा परियोजना, उत्पादन, वा सेवाहरूका लागि ट्रेडमार्क वा लोगोहरू समावेश हुन सक्छन्। Microsoft ट्रेडमार्क वा लोगोहरूको अधिकृत प्रयोग [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) अनुसार गर्नुपर्नेछ र त्यसलाई पालना गर्नुपर्छ। यो परियोजनाको संशोधित संस्करणहरूमा Microsoft ट्रेडमार्क वा लोगोहरूको प्रयोगले भ्रम उत्पन्न गर्नु हुँदैन वा Microsoft को प्रायोजनलाई संकेत गर्नु हुँदैन। तेस्रो पक्षका ट्रेडमार्क वा लोगोहरूको प्रयोग तिनका नीति अनुसार हुनेछ।

## मद्दत प्राप्त गर्ने

यदि तपाईं अड्किनुभयो वा AI अनुप्रयोग बनाउने विषयमा कुनै प्रश्न छ भने, सामेल हुनुहोस्:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

यदि तपाईंलाई निर्माण गर्दा उत्पादन प्रतिकृया वा त्रुटिहरू छन् भने भ्रमण गर्नुहोस्:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यस कागजातलाई AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) मार्फत अनुवाद गरिएको हो। हामी सही अनुवादका लागि प्रयासरत हुन्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा असत्यता हुनसक्छ। मूल कागजात यसको मूल भाषामा प्रामाणिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवादको सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट हुने कुनै पनि सम्झना भ्रामकता वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->