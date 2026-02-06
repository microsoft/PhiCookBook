# फाय कुकबुक: मायक्रोसॉफ्टच्या फाय मॉडेल्ससह प्रत्यक्ष उदाहरणे

[![GitHub Codespaces मध्ये नमुने उघडा आणि वापरा](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers मध्ये उघडा](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub योगदानकर्ते](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub समस्या](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub पुल-रिक्वेस्ट्स](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs स्वागतार्ह](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub वॉचर्स](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub स्टार्स](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![मायक्रोसॉफ्ट Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

फाय ही मायक्रोसॉफ्टकडून विकसित करण्यात आलेली एक सिरीज ओपन सोर्स AI मॉडेल्सची आहे.

फाय सध्या सर्वात शक्तिशाली आणि किफायतशीर लहान भाषा मॉडेल (SLM) आहे, ज्यामध्ये बहुभाषिक, विचारप्रवणता, मजकूर/चॅट जनरेशन, कोडिंग, प्रतिमा, ऑडिओ आणि इतर परिस्थितींमध्ये अत्यंत चांगले परफॉर्मन्स मिळते.

तुम्ही फाय क्लाउड मध्ये किंवा एज डिव्हाइसेसवर तैनात करू शकता, आणि मर्यादित संगणकीय शक्तीने सहजपणे जनरेटिव्ह AI अनुप्रयोग तयार करू शकता.

हे स्रोत वापरायला सुरुवात करण्यासाठी खालील पायऱ्या फॉलो करा:
1. **रेपॉझिटरी फोर्क करा**: क्लिक करा [![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **रेपॉझिटरी क्लोन करा**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**मायक्रोसॉफ्ट AI Discord समुदायात सामील व्हा आणि तज्ञ व इतर विकासकांशी भेटा**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/mr/cover.eb18d1b9605d754b.webp)

### 🌐 बहुभाषिक सहाय्य

#### GitHub Action द्वारे समर्थित (स्वयंचलित आणि नेहमी अद्ययावत)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरबी](../ar/README.md) | [बंगाली](../bn/README.md) | [बल्गेरियन](../bg/README.md) | [बर्मी (म्यानमार)](../my/README.md) | [चिनी (सोपे)](../zh-CN/README.md) | [चिनी (परंपरागत, हाँगकाँग)](../zh-HK/README.md) | [चिनी (परंपरागत, मकाउ)](../zh-MO/README.md) | [चिनी (परंपरागत, तैवान)](../zh-TW/README.md) | [क्रोएशियन](../hr/README.md) | [जेक](../cs/README.md) | [डेन्मार्की](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियन](../et/README.md) | [फिन्निश](../fi/README.md) | [फ्रेंच](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिंदी](../hi/README.md) | [हंगेरीयन](../hu/README.md) | [इंडोनेशियन](../id/README.md) | [इटालियन](../it/README.md) | [जपानी](../ja/README.md) | [कन्नड](../kn/README.md) | [कोरियन](../ko/README.md) | [लिथुआनियन](../lt/README.md) | [मलय](../ms/README.md) | [मलयाळम](../ml/README.md) | [मराठी](./README.md) | [नेपाली](../ne/README.md) | [नायजेरियन पिजिन](../pcm/README.md) | [नॉर्वेजियन](../no/README.md) | [फारसी (पर्शियन)](../fa/README.md) | [पोलिश](../pl/README.md) | [ब्राझीलियन पोर्तुगीज](../pt-BR/README.md) | [पुर्तगाली (पुर्तगाल)](../pt-PT/README.md) | [पंजाबी (गुरमुखी)](../pa/README.md) | [रोमानियन](../ro/README.md) | [रशियन](../ru/README.md) | [सर्बियन (सिरिलिक)](../sr/README.md) | [स्लोवाक](../sk/README.md) | [स्लोव्हेनियन](../sl/README.md) | [स्पॅनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिश](../sv/README.md) | [टागालॉग (फिलीपिनो)](../tl/README.md) | [तमिळ](../ta/README.md) | [तेलुगू](../te/README.md) | [थाई](../th/README.md) | [तुर्की](../tr/README.md) | [युक्रेनियन](../uk/README.md) | [उर्दू](../ur/README.md) | [व्हिएतनामी](../vi/README.md)

> **स्थानिकरित्या क्लोन करणे प्राधान्यदर्शक?**

> या रेपॉझिटरीमध्ये ५०+ भाषांमध्ये भाषांतर समाविष्ट आहे ज्यामुळे डाउनलोड आकार लक्षणीय वाढतो. भाषांतरे न घेता क्लोन करण्यासाठी, sparse checkout वापरा:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> हे तुम्हाला कोर्स पूर्ण करण्यासाठी आवश्यक सर्वकाही अधिक वेगवान डाउनलोडसह देते.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## अनुक्रमणिका

- परिचय
  - [फाय कुटुंबात आपले स्वागत आहे](./md/01.Introduction/01/01.PhiFamily.md)
  - [आपले वातावरण सेट करणे](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [महत्वाच्या तंत्रज्ञानांची समजूत](./md/01.Introduction/01/01.Understandingtech.md)
  - [फाय मॉडेल्ससाठी AI सुरक्षा](./md/01.Introduction/01/01.AISafety.md)
  - [फाय हार्डवेअर समर्थन](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [फाय मॉडेल्स आणि प्लॅटफॉर्म्सवर उपलब्धता](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai आणि फाय वापरणे](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub मार्केटप्लेस मॉडेल्स](https://github.com/marketplace/models)
  - [Azure AI मॉडेल कॅटलॉग](https://ai.azure.com)

- विविध वातावरणात फायचा इन्फरन्स
    -  [हगिंग फेस](./md/01.Introduction/02/01.HF.md)
    -  [GitHub मॉडेल्स](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry मॉडेल कॅटलॉग](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI टूलकिट VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry स्थानिक](./md/01.Introduction/02/07.FoundryLocal.md)

- फाय कुटुंबातील इन्फरन्स
    - [iOS मध्ये फायचा इन्फरन्स](./md/01.Introduction/03/iOS_Inference.md)
    - [Android मध्ये फायचा इन्फरन्स](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson मध्ये फायचा इन्फरन्स](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC मध्ये फायचा इन्फरन्स](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX फ्रेमवर्कसह फायचा इन्फरन्स](./md/01.Introduction/03/MLX_Inference.md)
    - [स्थानिक सर्व्हरमध्ये फायचा इन्फरन्स](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI टूलकिट वापरून रिमोट सर्व्हरमध्ये फायचा इन्फरन्स](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust सह फायचा इन्फरन्स](./md/01.Introduction/03/Rust_Inference.md)
    - [स्थानिकमध्ये फाय-व्हिजनचा इन्फरन्स](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure कंटेनर्स (अधिकृत समर्थन) सह फायचा इन्फरन्स](./md/01.Introduction/03/Kaito_Inference.md)
-  [फाय कुटुंबाचे प्रमाणांकन](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp वापरून फाय-3.5 / 4 प्रमाणांकन](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime साठी जनरेटिव्ह AI विस्तार वापरून फाय-3.5 / 4 प्रमाणांकन](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO वापरून फाय-3.5 / 4 प्रमाणांकन](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX फ्रेमवर्क वापरून फाय-3.5 / 4 प्रमाणांकन](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  फायचे मूल्यमापन
    - [जबाबदार AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [मूल्यमापनासाठी Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [मूल्यमापनासाठी Promptflow वापरणे](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search सह RAG
    - [Azure AI Search सह Phi-4-mini आणि Phi-4-multimodal (RAG) कसे वापरावे](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- फाय अनुप्रयोग विकास नमुने
  - मजकूर आणि चॅट अनुप्रयोग
    - Phi-4 नमुने 🆕
      - [📓] [Phi-4-mini ONNX मॉडेलशी चॅट करा](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 स्थानिक ONNX मॉडेल .NET शी चॅट](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Phi-4 ONNX वापरून Sementic Kernel सह .NET कन्सोल अनुप्रयोगात चॅट](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 नमुने
      - [ब्राउझरमध्ये Phi3, ONNX Runtime Web आणि WebGPU वापरून स्थानिक चॅटबॉट](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino चॅट](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [मल्टी मॉडेल - इंटरऐक्टिव Phi-3-mini आणि OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - एक रॅपर तयार करणे आणि MLFlow सह Phi-3 वापरणे](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [मॉडेल ऑप्टिमायझेशन - Olive सह ONNX Runtime Web साठी Phi-3-min मॉडेल कसे ऑप्टिमाइझ करावे](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx सह WinUI3 अॅप](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 मल्टी मॉडेल एआय पॉवर्ड नोट्स अॅप सॅम्पल](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [कस्टम Phi-3 मॉडेल्सना Fine-tune आणि Prompt flow सह इंटिग्रेट करा](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry मध्ये Prompt flow सह कस्टम Phi-3 मॉडेल्सना Fine-tune आणि इंटिग्रेट करा](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft च्या जबाबदार AI तत्त्वांवर लक्ष केंद्रित करून Azure AI Foundry मध्ये Fine-tuned Phi-3 / Phi-3.5 मॉडेलचे मूल्यांकन करा](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct भाषा भाकित करण्याचा सॅम्पल (चिनी/इंग्रजी)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG चॅटबॉट](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU वापरून Phi-3.5-Instruct ONNX सह Prompt flow सोल्यूशन तयार करणे](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite वापरून Android अॅप तयार करणे](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime वापरून स्थानिक ONNX Phi-3 मॉडेलसह Q&A .NET उदाहरण](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel आणि Phi-3 सह कन्सोल चॅट .NET अॅप](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK कोड आधारित सॅम्पल्स 
    - Phi-4 सॅम्पल्स 🆕
      - [📓] [Phi-4-multimodal वापरून प्रोजेक्ट कोड तयार करा](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 सॅम्पल्स
      - [Microsoft Phi-3 कुटुंबासह आपला स्वतःचा Visual Studio Code GitHub Copilot Chat तयार करा](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub मॉडेल्सने Phi-3.5 सह आपला स्वतःचा Visual Studio Code Chat Copilot एजंट तयार करा](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - प्रगत तर्कसंगत सॅम्पल्स
    - Phi-4 सॅम्पल्स 🆕
      - [📓] [Phi-4-mini-reasoning किंवा Phi-4-reasoning सॅम्पल्स](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive सह Phi-4-mini-reasoning चे Fine-tuning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX सह Phi-4-mini-reasoning चे Fine-tuning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub मॉडेल्ससह Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry मॉडेल्ससह Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - डेमो
      - [Phi-4-mini डेमो जे Hugging Face Spaces वर होस्टेड आहेत](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal डेमो जे Hugging Face Spaces वर होस्टेड आहेत](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - व्हिजन सॅम्पल्स
    - Phi-4 सॅम्पल्स 🆕
      - [📓] [Phi-4-multimodal वापरून प्रतिमा वाचा आणि कोड तयार करा](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 सॅम्पल्स
      -  [📓][Phi-3-vision-इमेज टेक्स्ट ते टेक्स्ट](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP एम्बेडिंग](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [डेमो: Phi-3 पुनर्चक्रण](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - Visual language assistant - Phi3-Vision आणि OpenVINO सह](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision मल्टी-फ्रेम किंवा मल्टी-इमेज सॅम्पल](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET वापरून स्थानिक ONNX मॉडेलसह Phi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [मेन्‍यू आधारित Microsoft.ML.OnnxRuntime .NET वापरून स्थानिक ONNX मॉडेलसह Phi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi304)

  - गणित सॅम्पल्स
    -  Phi-4-Mini-Flash-Reasoning-Instruct सॅम्पल्स 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct सह गणित डेमो](./md/02.Application/09.Math/MathDemo.ipynb)

  - ऑडिओ सॅम्पल्स
    - Phi-4 सॅम्पल्स 🆕
      - [📓] [Phi-4-multimodal वापरून ऑडिओ ट्रान्सक्रिप्ट्स काढणे](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal ऑडिओ सॅम्पल](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal स्पीच ट्रान्सलेशन सॅम्पल](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET कन्सोल अनुप्रयोग ज्याचा वापर Phi-4-multimodal ऑडिओ फाईलचे विश्लेषण करण्यासाठी आणि ट्रान्सक्रिप्ट तयार करण्यासाठी होतो](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE सॅम्पल्स
    - Phi-3 / 3.5 सॅम्पल्स
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) सोशल मीडिया सॅम्पल](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI शोध आणि LlamaIndex सह Retrieval-Augmented Generation (RAG) पाइपलाइन तयार करणे](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - फंक्शन कॉलिंग सॅम्पल्स
    - Phi-4 सॅम्पल्स 🆕
      -  [📓] [Phi-4-mini सह फंक्शन कॉलिंग वापरणे](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini सह मल्टी-एजंट तयार करण्यासाठी फंक्शन कॉलिंग वापरणे](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama सह फंक्शन कॉलिंग वापरणे](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX सह फंक्शन कॉलिंग वापरणे](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - मल्टीमॉडल मिश्रण सॅम्पल्स
    - Phi-4 सॅम्पल्स 🆕
      -  [📓] [Phi-4-multimodal तंत्रज्ञान पत्रकार म्हणून वापरणे](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET कन्सोल अॅप्लिकेशन ज्याचा वापर Phi-4-multimodal वापरून प्रतिमांचे विश्लेषण करण्यासाठी होतो](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi चे फाईन-ट्यूनिंग सॅम्पल्स
  - [फाईन-ट्यूनिंग परिस्थिती](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [फाईन-ट्यूनिंग vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 ला उद्योग विशेषज्ञ होऊ द्या (Fine-tuning)](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS Code साठी AI टूलकिट वापरून Phi-3 ची फाईन-ट्यूनिंग](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure मशीन लर्निंग सेवा वापरून Phi-3 ची फाईन-ट्यूनिंग](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora सह Phi-3 ची फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora सह Phi-3 ची फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry सह Phi-3 ची फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK वापरून Phi-3 ची फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive सह फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Lab सह फाईन-ट्यूनिंग](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias सह Phi-3-vision ची फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework सह Phi-3 ची फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLX.md)
  - [औपचारिक समर्थनासह Phi-3-vision ची फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure Containers (औपचारिक समर्थन) सह Phi-3 ची फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 आणि 3.5 Vision चे फाईन-ट्यूनिंग](https://github.com/2U1/Phi3-Vision-Finetune)

- हँड्स ऑन लॅब
  - [कटिंग-एज मॉडेल्सचे अन्वेषण: LLMs, SLMs, स्थानिक विकास आणि बरेच काही](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP क्षमता अनलॉक करणे: Microsoft Olive सह फाईन-ट्यूनिंग](https://github.com/azure/Ignite_FineTuning_workshop)

- अकादमिक संशोधन कागदपत्रे आणि प्रकाशने
  - [पाठ्यपुस्तक हेच पुरेसे आहेत II: phi-1.5 तांत्रिक अहवाल](https://arxiv.org/abs/2309.05463)
  - [Phi-3 तांत्रिक अहवाल: तुमच्या फोनवर स्थानिकपणे एक अत्यंत सक्षम भाषा मॉडेल](https://arxiv.org/abs/2404.14219)
  - [Phi-4 तांत्रिक अहवाल](https://arxiv.org/abs/2412.08905)
  - [Phi-4-मिनी तांत्रिक अहवाल: मिश्रण-ऑफ-LoRAs द्वारे संकुचित तरी शक्तिशाली मल्टिमोडल भाषा मॉडेल्स](https://arxiv.org/abs/2503.01743)
  - [वाहनातील फंक्शन-कॉलिंगसाठी लहान भाषा मॉडेल्सचे ऑप्टिमायझेशन](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) बहुविकल्पीय प्रश्न उत्तरेसाठी PHI-3 चे फाइन-ट्यूनिंग: पद्धती, निकाल, आणि आव्हाने](https://arxiv.org/abs/2501.01588)
  - [Phi-4-तर्कशास्त्र तांत्रिक अहवाल](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-मिनी-तर्कशास्त्र तांत्रिक अहवाल](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi मॉडेल्सचा वापर

### Azure AI Foundry वर Phi

आपण Microsoft Phi कसे वापरायचे आणि आपल्या वेगवेगळ्या हार्डवेअर उपकरणांमध्ये E2E सोल्यूशन्स कसे तयार करायचे हे शिकू शकता. स्वतःसाठी Phi अनुभवण्यासाठी, मॉडेल्ससह खेळण्यापासून सुरू करा आणि आपल्या परिस्थितींसाठी Phi सानुकूलित करा [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) वापरून. अधिक जाणून घेण्यासाठी [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) सह सुरू करा.

**प्लेलँड**
प्रत्येक मॉडेलसाठी समर्पित प्लेग्राउंड आहे जिथे तुम्ही मॉडेलची चाचणी करू शकता [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub मॉडेल्सवर Phi

आपण Microsoft Phi कसे वापरायचे आणि आपल्या वेगवेगळ्या हार्डवेअर उपकरणांमध्ये E2E सोल्यूशन्स कसे तयार करायचे हे शिकू शकता. स्वतःसाठी Phi अनुभवण्यासाठी, मॉडेलसह खेळण्यापासून सुरू करा आणि आपल्या परिस्थितींसाठी Phi सानुकूलित करा [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) वापरून. अधिक जाणून घेण्यासाठी [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) सह सुरू करा.

**प्लेलँड**
प्रत्येक मॉडेलसाठी समर्पित [प्लेग्राउंड जिथे आपण मॉडेल तपासू शकता](/md/02.QuickStart/GitHubModel_QuickStart.md) आहे.

### Hugging Face वर Phi

आपण [Hugging Face](https://huggingface.co/microsoft) वर देखील मॉडेल शोधू शकता.

**प्लेलँड**
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 इतर कोर्सेस

आमची टीम इतर कोर्सेस देखील तयार करते! येथे पाहा:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![बिगनर्ससाठी LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![बिगनर्ससाठी LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![बिगनर्ससाठी LangChain](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / एजंट्स
[![बिगनर्ससाठी AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![बिगनर्ससाठी Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![बिगनर्ससाठी MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![बिगनर्ससाठी AI एजंट्स](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### जनरेटिव AI सिरीज
[![बिगनर्ससाठी जनरेटिव AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![जनरेटिव AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![जनरेटिव AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![जनरेटिव AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### कोअर शिक्षण
[![बिगनर्ससाठी ML](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![बिगनर्ससाठी डेटा सायन्स](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![बिगनर्ससाठी AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![बिगनर्ससाठी सायबरसुरक्षा](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![बिगनर्ससाठी वेब डेव्हलपमेंट](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![बिगनर्ससाठी IoT](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![बिगनर्ससाठी XR विकास](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot सिरीज
[![AI जोडलेल्या प्रोग्रामिंगसाठी Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET साठी Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot साहस](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## जबाबदार AI

Microsoft आमच्या ग्राहकांना आमची AI उत्पादने जबाबदारीने वापरण्यास मदत करण्यास प्रतिबद्ध आहे, आमची शिकवण शेअर करणे आणि ट्रान्सपरन्सी नोट्स आणि प्रभाव मूल्यांकनांसारख्या साधनाद्वारे विश्वासावर आधारित भागीदारी तयार करणे. या संसाधनांपैकी बर्‍याचचा शोध [https://aka.ms/RAI](https://aka.ms/RAI) येथे घेता येतो.  
Microsoft चा जबाबदार AI दृष्टिकोन आम्हा AI तत्त्वांवर आधारित आहे - न्यायसंगतता, विश्वसनीयता आणि सुरक्षा, गोपनीयता आणि सुरक्षा, समावेशकता, पारदर्शकता, आणि उत्तरदायित्व.

या नमुन्यातील मोठ्या प्रमाणात नैसर्गिक भाषा, प्रतिमा, आणि भाषण मॉडेल्स - जसे की वापरलेले आहेत - संभाव्य असमान, अविश्वसनीय किंवा अपमानास्पद वर्तन करू शकतात, ज्यामुळे त्रास होऊ शकतो. कृपया धोके आणि मर्यादा जाणून घेण्यासाठी [Azure OpenAI सेवा ट्रान्सपरन्सी नोट](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) पहा.

या धोके कमी करण्यासाठी शिफारस केलेला दृष्टिकोन म्हणजे तुमच्या वास्तुकलेमध्ये एक सुरक्षितता प्रणाली समाविष्ट करणे जी हानिकारक वर्तन ओळखू आणि प्रतिबंध करू शकते. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) स्वतंत्र संरक्षण स्तर प्रदान करतो, जे अनुप्रयोगांमध्ये आणि सेवांमध्ये हानिकारक वापरकर्ता-निर्मित आणि AI-निर्मित सामग्री शोधू शकते. Azure AI Content Safety मध्ये मजकूर आणि प्रतिमा APIs आहेत जे तुम्हाला हानिकारक सामग्री ओळखण्यास मदत करतात. Azure AI Foundry मध्ये, Content Safety सेवा तुम्हाला वेगवेगळ्या प्रकारांतील हानिकारक सामग्री ओळखण्यासाठी नमुना कोड पाहण्याची, एक्सप्लोर करण्याची आणि प्रयत्न करण्याची परवानगी देते. खालील [क्विकस्टार्ट दस्तऐवज](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) तुम्हाला सेवेला विनंत्या कशा करायच्या याचे मार्गदर्शन करतो.
अजून एक बाब लक्षात घेण्यासारखी म्हणजे संपूर्ण अनुप्रयोग कार्यक्षमता. मल्टी-मॉडेल आणि मल्टी-모डेल अनुप्रयोगांसह, कार्यक्षमतेचा अर्थ असा आहे की प्रणाली आपल्याला आणि आपल्या वापरकर्त्यांना अपेक्षित त्या प्रकारे कार्य करते, ज्यात हानिकारक आउटपुट जनरेट न करणे याचा समावेश आहे. आपल्या संपूर्ण अनुप्रयोगाची कार्यक्षमता [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) वापरून मोजणे महत्त्वाचे आहे. आपल्याकडे [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) वापरून तयार करण्याची आणि मूल्यांकन करण्याची क्षमता देखील आहे.

आपण आपल्या विकास वातावरणात [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) वापरून आपल्या AI अनुप्रयोगाचे मूल्यांकन करू शकता. चाचणी डेटासेट किंवा लक्ष्य दिल्यास, आपले जनरेटिव्ह AI अनुप्रयोग जनरेशन्स अंगभूत मूल्यांकनकारक किंवा निवडीच्या कस्टम मूल्यांकनकारकांनी संख्यात्मकरित्या मोजले जातात. आपल्या प्रणालीचे मूल्यांकन करण्यासाठी azure ai evaluation sdk कसे सुरू करायचे ते जाणून घेण्यासाठी आपण [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) चे अनुसरण करू शकता. एकदा आपण मूल्यांकन रन चालविल्यानंतर, आपण [Azure AI Foundry मध्ये निकालांचे दृश्यरूप पाहू शकता](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## ट्रेडमार्क

या प्रकल्पामध्ये प्रकल्प, उत्पादने किंवा सेवा यांचे ट्रेडमार्क किंवा लोगो असू शकतात. Microsoft ट्रेडमार्क्स किंवा लोगोचा अधिकृत वापर [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) च्या अटी व नियमांचे पालन करणे आवश्यक आहे.
या प्रकल्पाच्या बदललेल्या आवृत्त्यांमध्ये Microsoft ट्रेडमार्क्स किंवा लोगोचा वापर गोंधळ उभा करणार नाही किंवा Microsoft सहाय्यता दर्शवण्याचा अर्थ लावणार नाही. तृतीय पक्ष ट्रेडमार्क्स किंवा लोगोचा कोणताही वापर त्या तृतीय पक्षाच्या धोरणांनुसार असेल.

## मदत मिळवा

जर आपल्याला अडचण येत असेल किंवा AI अनुप्रयोग तयार करताना कोणतेही प्रश्न असतील तर सहभागी व्हा:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

जर आपल्याकडे उत्पादनाबाबत अभिप्राय किंवा त्रुटी असतील तर भेट द्या:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील आहोत, परंतु कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेतील त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्त्रोत मानला जावा. महत्त्वाच्या माहिती साठी व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाचा वापर केल्यामुळे झालेल्या कुठल्याही गैरसमज किंवा चुकीच्या अर्थ लावण्याबद्दल आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->