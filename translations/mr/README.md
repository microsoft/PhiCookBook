<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2e4b490f4bd424b095f21e38c6af33b",
  "translation_date": "2026-01-05T02:01:34+00:00",
  "source_file": "README.md",
  "language_code": "mr"
}
-->
# Phi कुकबुक: Microsoft च्या Phi मॉडेल्ससह प्रत्यक्ष उदाहरणे

[![GitHub Codespaces मधील नमुने उघडा आणि वापरा](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers मध्ये उघडा](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub योगदानकर्ते](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub इश्यूज](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub पुल-रिक्वेस्ट](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs स्वागत](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub पाहणारे](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub स्टार्स](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi हा Microsoft द्वारा विकसित केलेल्या मुक्त-स्रोत AI मॉडेल्सची मालिका आहे. 

Phi सध्या सर्वात शक्तिशाली आणि खर्चप्रभावी छोटे भाषा मॉडेल (SLM) आहे, आणि बहुभाषिकता, तर्क, मजकूर/चॅट निर्माण, कोडिंग, प्रतिमा, ऑडिओ आणि इतर अनेक परिदृश्यांमध्ये उत्कृष्ट बेंचमार्क दाखवते. 

आपण Phi ला क्लाऊडवर किंवा एज डिव्हाइसवर तैनात करू शकता, आणि मर्यादित संगणकीय शक्तीसह सहजपणे जनरेटिव्ह AI अनुप्रयोग तयार करू शकता.

या साधनांचा उपयोग सुरू करण्यासाठी खालील पायऱ्या अनुसरा :
1. **रिपॉझिटरी फोर्क करा**: क्लिक करा [![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **रिपॉझिटरी क्लोन करा**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord समुदायात सामील व्हा आणि तज्ज्ञ व सह-विकसकांना भेटा**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![मुखपृष्ठ](../../translated_images/cover.eb18d1b9605d754b.mr.png)

### 🌐 बहुभाषिक समर्थन

#### GitHub Action द्वारे समर्थित (स्वयंचलित आणि नेहमी अद्ययावत)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरबी](../ar/README.md) | [बंगाली](../bn/README.md) | [बुल्गेरियन](../bg/README.md) | [बर्मी ( म्यानमार )](../my/README.md) | [चीनी (सरलीकृत)](../zh/README.md) | [चीनी (परंपरागत, हाँगकाँग)](../hk/README.md) | [चीनी (परंपरागत, मकाऊ)](../mo/README.md) | [चीनी (परंपरागत, तैवान)](../tw/README.md) | [क्रोएशियन](../hr/README.md) | [झेक](../cs/README.md) | [डॅनिश](../da/README.md) | [डच](../nl/README.md) | [इस्टोनियन](../et/README.md) | [फिनिश](../fi/README.md) | [फ्रेंच](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिंदी](../hi/README.md) | [हंगेरीयन](../hu/README.md) | [इंडोनेशियन](../id/README.md) | [इटालियन](../it/README.md) | [जपानी](../ja/README.md) | [कन्नडा](../kn/README.md) | [कोरियन](../ko/README.md) | [लिथुआनियन](../lt/README.md) | [मलय](../ms/README.md) | [मलयाळम](../ml/README.md) | [मराठी](./README.md) | [नेपाळी](../ne/README.md) | [नायजेरियन पिजिन](../pcm/README.md) | [नॉर्वेजियन](../no/README.md) | [फारसी (फार्सी)](../fa/README.md) | [पोलिश](../pl/README.md) | [पोर्तुगीज (ब्राझील)](../br/README.md) | [पोर्तुगीज (पोर्तुगाल)](../pt/README.md) | [पंजाबी (गुरमुखी)](../pa/README.md) | [रोमानियन](../ro/README.md) | [रशियन](../ru/README.md) | [सर्बियन (सिरिलिक)](../sr/README.md) | [स्लोव्हाक](../sk/README.md) | [स्लोव्हेनियन](../sl/README.md) | [स्पॅनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिश](../sv/README.md) | [टागालोग (फिलिपिनो)](../tl/README.md) | [तमिळ](../ta/README.md) | [तेलुगु](../te/README.md) | [थाई](../th/README.md) | [तुर्किश](../tr/README.md) | [युक्रेनियन](../uk/README.md) | [उर्दू](../ur/README.md) | [व्हिएतनामी](../vi/README.md)

> **स्थानिकरित्या क्लोन करायचे आहे का?**

> ह्या रिपॉझिटरीमध्ये 50+ भाषांमध्ये अनुवाद समाविष्ट आहेत ज्यामुळे डाउनलोड साईझ मोठ्या प्रमाणावर वाढते. अनुवादांशिवाय क्लोन करण्यासाठी, sparse checkout वापरा:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> हे आपल्याला कोर्स पूर्ण करण्यासाठी आवश्यक सर्व काही देईल आणि खूपच जलद डाउनलोड मिळेल.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## विषय सूची

- परिचय
  - [Phi कुटुंबात स्वागत](./md/01.Introduction/01/01.PhiFamily.md)
  - [आपले वातावरण सेट करणे](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [महत्वाच्या तंत्रज्ञानांचे आकलन](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi मॉडेल्ससाठी AI सुरक्षा](./md/01.Introduction/01/01.AISafety.md)
  - [Phi हार्डवेअर समर्थन](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [विभिन्न प्लॅटफॉर्मवर Phi मॉडेल्स आणि उपलब्धता](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai आणि Phi चा वापर](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub Marketplace मॉडेल्स](https://github.com/marketplace/models)
  - [Azure AI मॉडेल कॅटलॉग](https://ai.azure.com)

- विविध वातावरणांमध्ये Phi चे इन्फरन्स
    -  [Hugging Face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub Models](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry स्थानिक](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi कुटुंबातील इन्फरन्स
    - [iOS मध्ये Phi चे इन्फरन्स](./md/01.Introduction/03/iOS_Inference.md)
    - [Android मध्ये Phi चे इन्फरन्स](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson मध्ये Phi चे इन्फरन्स](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC मध्ये Phi चे इन्फरन्स](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX फ्रेमवर्कसह Phi चे इन्फरन्स](./md/01.Introduction/03/MLX_Inference.md)
    - [स्थानिक सर्व्हरमध्ये Phi चे इन्फरन्स](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit वापरून रिमोट सर्व्हरमध्ये Phi चे इन्फरन्स](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust सह Phi चे इन्फरन्स](./md/01.Introduction/03/Rust_Inference.md)
    - [स्थानिक में Phi चे व्हिजन इन्फरन्स](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure कंटेनर्ससह Phi चे इन्फरन्स (अधिकृत समर्थन)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi कुटुंबाचे क्वांटायझेशन](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp वापरून Phi-3.5 / 4 चे क्वांटायझेशन](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime साठी Generative AI विस्तार वापरून Phi-3.5 / 4 चे क्वांटायझेशन](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO वापरून Phi-3.5 / 4 चे क्वांटायझेशन](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX फ्रेमवर्क वापरून Phi-3.5 / 4 चे क्वांटायझेशन](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi चे मूल्यांकन
    - [Response AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [मूल्यांकनासाठी Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [मूल्यांकनासाठी Promptflow वापरणे](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search सह RAG
    - [Phi-4-mini आणि Phi-4-multimodal (RAG) Azure AI Search सह कसे वापरायचे](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi अनुप्रयोग विकास नमुने
  - मजकूर आणि चॅट अनुप्रयोग
    - Phi-4 नमुने 🆕
      - [📓] [Phi-4-mini ONNX मॉडेलसह चॅट](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 स्थानिक ONNX मॉडेल .NET सह चॅट](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Semantic Kernel वापरून Phi-4 ONNX सह Chat .NET Console App](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 नमुने
      - [Phi3, ONNX Runtime Web आणि WebGPU वापरून ब्राउझरमध्ये स्थानिक चॅटबॉट](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVINO चॅट](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [मल्टी मॉडेल - इंटरऐक्टिव्ह Phi-3-mini आणि OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - व्रॅपर तयार करणे आणि MLFlow सह Phi-3 वापरणे](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [मॉडेल ऑप्टिमायझेशन - Olive सह ONNX Runtime Web साठी Phi-3-min मॉडेल कसे ऑप्टिमाइझ करायचे](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [WinUI3 अॅप Phi-3 mini-4k-instruct-onnx सह](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 मल्टी मॉडेल AI संचालित नोट्स अॅप नमुना](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [कस्टम Phi-3 मॉडेल्सचे फाईन-ट्यून आणि Prompt flow सह एकत्रीकरण](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry मध्ये Prompt flow सह कस्टम Phi-3 मॉडेल्सचे फाईन-ट्यून आणि एकत्रीकरण](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Azure AI Foundry मध्ये Microsoft's Responsible AI तत्त्वांवर लक्ष केंद्रित करून फाईन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलचे मूल्यांकन](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct भाषा भविष्यवाणी नमुना (中文/English)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU वापरून Phi-3.5-Instruct ONNX सह Prompt flow सोल्यूशन तयार करणे](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite वापरून Android अॅप कसे तयार करावे](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [स्थानिक ONNX Phi-3 मॉडेल वापरताना Microsoft.ML.OnnxRuntime वापरणारा Q&A .NET उदाहरण](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel आणि Phi-3 सह कन्सोल चॅट .NET अॅप](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK कोड-आधारित नमुने 
    - Phi-4 नमुने 🆕
      - [📓] [Phi-4-multimodal वापरून प्रोजेक्ट कोड जनरेट करा](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 नमुने
      - [Microsoft Phi-3 कुटुंबासह आपले स्वतःचे Visual Studio Code GitHub Copilot Chat तयार करा](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub Models द्वारे Phi-3.5 सह आपले स्वतःचे Visual Studio Code Chat Copilot Agent तयार करा](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - प्रगत तर्कनिष्ठ नमुने
    - Phi-4 नमुने 🆕
      - [📓] [Phi-4-mini-reasoning किंवा Phi-4-reasoning नमुने](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive सह Phi-4-mini-reasoning चे फाईन-ट्यूनिंग](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX सह Phi-4-mini-reasoning चे फाईन-ट्यूनिंग](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub Models सह Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry Models सह Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - डेमो
      - [Phi-4-mini डेमो Hugging Face Spaces वर होस्ट केलेले](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal डेमो Hugginge Face Spaces वर होस्ट केलेले](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - व्हिजन नमुने
    - Phi-4 नमुने 🆕
      - [📓] [Phi-4-multimodal वापरून प्रतिमा वाचणे आणि कोड जनरेट करणे](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 नमुने
      -  [📓][Phi-3-vision-Image text to text](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [डेमो: Phi-3 रिसायक्लिंग](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - व्हिज्युअल लँग्वेज असिस्टंट - Phi3-Vision आणि OpenVINO सह](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision मल्टी-फ्रेम किंवा मल्टी-इमेज नमुना](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET वापरून Phi-3 Vision स्थानिक ONNX मॉडेल](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [मेनू आधारित Phi-3 Vision स्थानिक ONNX मॉडेल Microsoft.ML.OnnxRuntime .NET वापरून](../../md/04.HOL/dotnet/src/LabsPhi304)

  - गणित नमुने
    -  Phi-4-Mini-Flash-Reasoning-Instruct नमुने 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct सह गणित डेमो](./md/02.Application/09.Math/MathDemo.ipynb)

  - ऑडिओ नमुने
    - Phi-4 नमुने 🆕
      - [📓] [Phi-4-multimodal वापरून ऑडिओ ट्रान्सक्रिप्ट्स बाहेर काढणे](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal ऑडिओ नमुना](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal स्पीच अनुवाद नमुना](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET कन्सोल अनुप्रयोग जो Phi-4-multimodal ऑडिओ वापरून ऑडिओ फाइलचे विश्लेषण करून ट्रान्सक्रिप्ट जनरेट करतो](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE नमुने
    - Phi-3 / 3.5 नमुने
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) सोशल मीडिया नमुना](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search आणि LlamaIndex सह Retrieval-Augmented Generation (RAG) पाईपलाइन तयार करणे](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - फंक्शन कॉलिंग नमुने
    - Phi-4 नमुने 🆕
      -  [📓] [Phi-4-mini सह Function Calling वापरणे](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Function Calling वापरून Phi-4-mini सह मल्टी-एजंट तयार करणे](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama सह Function Calling वापरणे](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX सह Function Calling वापरणे](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - मल्टीमोडल मिक्सिंग नमुने
    - Phi-4 नमुने 🆕
      -  [📓] [तंत्रज्ञान पत्रकार म्हणून Phi-4-multimodal वापरणे](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET कन्सोल अनुप्रयोग जो प्रतिमा विश्लेषित करण्यासाठी Phi-4-multimodal वापरतो](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi साठी फाईन-ट्यूनिंग नमुने
  - [फाईन-ट्यूनिंग परिस्थिती](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [फाईन-ट्यूनिंग विरुद्ध RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [फाईन-ट्यूनिंग: Phi-3 ला उद्योग तज्ञ बनवा](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [AI Toolkit for VS Code सह Phi-3 चे फाईन-ट्यूनिंग](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure Machine Learning Service सह Phi-3 चे फाईन-ट्यूनिंग](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora सह Phi-3 चे फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora सह Phi-3 चे फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry सह Phi-3 चे फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK सह Phi-3 चे फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive सह फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Lab सह फाईन-ट्यूनिंग](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias सह Phi-3-vision चे फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework सह Phi-3 चे फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision चे फाईन-ट्यूनिंग (अधिकृत समर्थन)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers सह Phi-3 चे फाईन-ट्यूनिंग (अधिकृत समर्थन)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 आणि 3.5 Vision चे फाईन-ट्यूनिंग](https://github.com/2U1/Phi3-Vision-Finetune)

- हँड्स-ऑन लॅब
  - [अत्याधुनिक मॉडेल्स एक्सप्लोर करणे: LLMs, SLMs, स्थानिक विकास आणि बरेच काही](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP क्षमता उघडणे: Microsoft Olive सह फाईन-ट्यूनिंग](https://github.com/azure/Ignite_FineTuning_workshop)

- अकादेमिक संशोधन पेपर्स आणि प्रकाशने
  - [Textbooks Are All You Need II: phi-1.5 तांत्रिक अहवाल](https://arxiv.org/abs/2309.05463)
  - [Phi-3 तांत्रिक अहवाल: आपल्या फोनवर स्थानिकरीत्या चालणारे उच्चक्षम भाषिक मॉडेल](https://arxiv.org/abs/2404.14219)
  - [Phi-4 तांत्रिक अहवाल](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini तांत्रिक अहवाल: Mixture-of-LoRAs द्वारे कॉम्पॅक्ट परंतु शक्तिशाली मल्टीमॉडल भाषिक मॉडेल्स](https://arxiv.org/abs/2503.01743)
  - [वाहनातील फंक्शन-कॉलिंगसाठी लहान भाषिक मॉडेल्सचे ऑप्टिमायझेशन](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 चे मल्टीपल-चॉइस प्रश्नोत्तरासाठी फाईन-ट्यूनिंग: पद्धतशास्त्र, निकाल आणि आव्हाने](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning तांत्रिक अहवाल](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning तांत्रिक अहवाल](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi मॉडेल वापरणे

### Azure AI Foundry वर Phi

You can learn how to use Microsoft Phi and how to build E2E solutions in your different hardware devices. To experience Phi for yourself, start by playing with the models and customizing Phi for your scenarios using the [Azure AI Foundry Azure AI मॉडेल कॅटलॉग](https://aka.ms/phi3-azure-ai) you can learn more at Getting Started with [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**प्लेग्राउंड**
Each model has a dedicated playground to test the model [Azure AI प्लेग्राउंड](https://aka.ms/try-phi3).

### GitHub Models वर Phi

You can learn how to use Microsoft Phi and how to build E2E solutions in your different hardware devices. To experience Phi for yourself, start by playing with the model and customizing Phi for your scenarios using the [GitHub मॉडेल कॅटलॉग](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) you can learn more at Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**प्लेग्राउंड**
Each model has a dedicated [प्लेग्राउंड मॉडेलची चाचणी करण्यासाठी](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Hugging Face वर Phi

You can also find the model on the [Hugging Face](https://huggingface.co/microsoft)

**प्लेग्राउंड**
 [Hugging Chat प्लेग्राउंड](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 इतर कोर्सेस

Our team produces other courses! Check out:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j सुरुवातीसाठी](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js सुरुवातीसाठी](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD सुरुवातीसाठी](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI सुरुवातीसाठी](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP सुरुवातीसाठी](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents सुरुवातीसाठी](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### जनरेटिव्ह AI मालिका
[![जनरेटिव्ह AI सुरुवातीसाठी](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![जनरेटिव्ह AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![जनरेटिव्ह AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![जनरेटिव्ह AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### कोर लर्निंग
[![ML सुरुवातीसाठी](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![डेटा सायन्स सुरुवातीसाठी](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI सुरुवातीसाठी](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![सायबरसुरक्षा सुरुवातीसाठी](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![वेब देव सुरुवातीसाठी](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT सुरुवातीसाठी](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR विकास सुरुवातीसाठी](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot मालिका
[![Copilot AI जोडलेल्या प्रोग्रामिंगसाठी](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET साठी](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot अ‍ॅडव्हेंचर](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## जबाबदार AI 

Microsoft आमच्या ग्राहकांना आमची AI उत्पादने जबाबदारीने वापरण्यात मदत करण्यासाठी, आमच्या शिकल्यान्चे वाटणे सामायिक करण्यासाठी आणि Transparency Notes आणि Impact Assessments सारख्या साधनांद्वारे विश्वासावर आधारित भागीदारी बांधण्यासाठी वचनबद्ध आहे. या संसाधनांपैकी अनेक [https://aka.ms/RAI](https://aka.ms/RAI) वर उपलब्ध आहेत.
Microsoft चा जबाबदार AI कडूनचा दृष्टिकोन आमच्या AI तत्त्वांवर आधारित आहे: न्याय, विश्वासार्हता आणि सुरक्षा, गोपनीयता आणि सुरक्षा, समावेशिता, पारदर्शकता, आणि उत्तरदायित्व.

मोठ्या प्रमाणावर नैसर्गिक भाषा, प्रतिमा आणि भाषण मॉडेल्स - या नमुन्यात वापरल्या गेलेल्या मॉडेल्सप्रमाणे - संभाव्यतः अन्यायकारक, अविश्वसनीय किंवा अपमानजनक वर्तन करु शकतात, ज्यामुळे हानी होऊ शकते. जोखीम आणि मर्यादा याबद्दल माहिती मिळवण्यासाठी कृपया [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) पहा.

या जोखमी कमी करण्यासाठी शिफारस केलेली पद्धत म्हणजे आपल्या आर्किटेक्चरमध्ये अशी सुरक्षा प्रणाली समाविष्ट करणे जी हानिकारक वर्तन शोधू आणि प्रतिबंधित करू शकते. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) स्वतंत्र संरक्षणाची एक थर प्रदान करते, जी अनुप्रयोगांमध्ये आणि सेवांमध्ये हानिकारक वापरकर्ता-निर्मित आणि AI-निर्मित सामग्री ओळखण्यासाठी सक्षम आहे. Azure AI Content Safety मध्ये अशा सामग्रीचे शोध घेण्यासाठी मजकूर आणि प्रतिमा API समाविष्ट आहेत. Azure AI Foundry मध्ये, Content Safety सेवा विविध मोडॅलिटींमधील हानिकारक सामग्री शोधण्यासाठी नमुना कोड पाहण्याची, अन्वेषण करण्याची आणि प्रयत्न करण्याची परवानगी देते. पुढील [क्विकस्टार्ट दस्तऐवजीकरण](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) आपल्याला सेवा कशी विनंती करायची याचे मार्गदर्शन करते.

घ्यायच्या गोष्टींपैकी आणखी एक पैलू म्हणजे एकूण अनुप्रयोगाचे कार्यप्रदर्शन. मल्टी-मॉडॅल आणि मल्टी-मॉडेल्स अनुप्रयोगांसह, आम्ही कार्यप्रदर्शनामुळे अर्थ लावतो की प्रणाली आपण आणि आपल्या वापरकर्त्यांनी अपेक्षेनुसार कार्य करते, ज्यात हानिकारक आउटपुट तयार न करणे समाविष्ट आहे. आपल्या एकूण अनुप्रयोगाचे कार्यप्रदर्शन परीक्षण करण्यासाठी [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) वापरणे महत्त्वाचे आहे. आपल्याकडे [सानुकूल मूल्यांकनकर्ते](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) तयार करण्याची आणि त्यांच्यासोबत मूल्यांकन करण्याची क्षमता देखील आहे.
You can evaluate your AI application in your development environment using the [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Given either a test dataset or a target, your generative AI application generations are quantitatively measured with built-in evaluators or custom evaluators of your choice. To get started with the azure ai evaluation sdk to evaluate your system, you can follow the [द्रुत प्रारंभ मार्गदर्शक](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Once you execute an evaluation run, you can [Azure AI Foundry मध्ये निकाल प्रत्यक्षरूपात पाहू शकता](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results). 

## ट्रेडमार्क

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft चे ट्रेडमार्क आणि ब्रँड मार्गदर्शक](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party's policies.

## मदत मिळवा

If you get stuck or have any questions about building AI apps, join:

[![Azure AI Foundry डिस्कॉर्ड](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

If you have product feedback or errors while building visit:

[![Azure AI Foundry विकसक फोरम](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित करण्यात आला आहे. जरी आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेच्या त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकारप्राप्त स्रोत म्हणून विचारात घ्यावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद शिफारसीय आहे. हा अनुवाद वापरल्यामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलावाबद्दल आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->