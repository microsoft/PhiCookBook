# Phi कुकबुक: Microsoft च्या Phi मॉडेल्ससह हँड्स-ऑन उदाहरणे

[![GitHub Codespaces मध्ये नमुने उघडा आणि वापरा](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers मध्ये उघडा](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub योगदानकर्ते](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub समस्या](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub पुल-रिक्वेस्ट](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs स्वागतार्ह](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub पहारेकरी](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub फोर्क](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub स्टार्स](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi हा Microsoft द्वारे विकसित केलेल्या मुक्त स्त्रोत AI मॉडेल्सची मालिका आहे.

Phi सध्या सर्वात शक्तिशाली आणि किफायतशीर लहान भाषा मॉडेल (SLM) आहे, ज्याला बहुभाषिक, तर्क, मजकूर/चॅट तयार करणे, कोडिंग, प्रतिमा, ऑडिओ आणि इतर अनेक परिदृश्यांमध्ये उत्कृष्ट कामगिरी मिळाली आहे.

तुम्ही Phi क्लाउड किंवा एज डिव्हायसेसवर डिप्लॉय करू शकता, आणि मर्यादित संगणकीय शक्तीसह सहजपणे सर्जनशील AI अनुप्रयोग तयार करू शकता.

या संसाधनांचा वापर सुरू करण्यासाठी खालील चरणांचे अनुसरण करा:
1. **रेपो फोर्क करा**: क्लिक करा [![GitHub फोर्क](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **रेपो क्लोन करा**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord समुदायात सहभागी व्हा आणि तज्ञ व इतर विकसकांशी भेटा**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/mr/cover.eb18d1b9605d754b.webp)

### 🌐 बहुभाषिक समर्थन

#### GitHub Action द्वारे समर्थित (स्वयंचलित आणि नेहमी अद्ययावत)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरबी](../ar/README.md) | [बंगाली](../bn/README.md) | [बुल्गेरियन](../bg/README.md) | [बर्मी (म्यानमार)](../my/README.md) | [चिनी (सरलीकृत)](../zh-CN/README.md) | [चिनी (परंपरागत, हॉंग कॉंग)](../zh-HK/README.md) | [चिनी (परंपरागत, मकाऊ)](../zh-MO/README.md) | [चिनी (परंपरागत, तैवान)](../zh-TW/README.md) | [क्रोएशियन](../hr/README.md) | [चेक](../cs/README.md) | [डॅनिश](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियन](../et/README.md) | [फिनिश](../fi/README.md) | [फ्रेंच](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिंदी](../hi/README.md) | [हंगेरीयन](../hu/README.md) | [इंडोनेशियन](../id/README.md) | [इटालियन](../it/README.md) | [जपानी](../ja/README.md) | [कन्नड](../kn/README.md) | [खमेर](../km/README.md) | [कोरियन](../ko/README.md) | [लिथुआनियन](../lt/README.md) | [मलय](../ms/README.md) | [मलयाळम](../ml/README.md) | [मराठी](./README.md) | [नेपाली](../ne/README.md) | [नायजेरियन पिडगिन](../pcm/README.md) | [नॉर्वेजियन](../no/README.md) | [फारसी (पर्शियन)](../fa/README.md) | [पोलिश](../pl/README.md) | [पोर्तुगीज (ब्राझील)](../pt-BR/README.md) | [पोर्तुगीज (पोर्तुगाल)](../pt-PT/README.md) | [पंजाबी (गुरमुखी)](../pa/README.md) | [रोमानियन](../ro/README.md) | [रशियन](../ru/README.md) | [सर्बियन (सिरिलिक)](../sr/README.md) | [स्लोव्हाक](../sk/README.md) | [स्लोव्हेनियन](../sl/README.md) | [स्पॅनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिश](../sv/README.md) | [टगालॉग (फिलिपिनो)](../tl/README.md) | [तामिळ](../ta/README.md) | [तेलुगू](../te/README.md) | [थाई](../th/README.md) | [तुर्किश](../tr/README.md) | [युक्रेनियन](../uk/README.md) | [उर्दू](../ur/README.md) | [व्हिएतनामीज](../vi/README.md)

> **स्थानिक क्लोन प्राधान्य देता का?**
>
> या रेपॉसिटरीमध्ये ५०+ भाषा भाषांतरांचा समावेश आहे ज्यामुळे डाउनलोड आकार लक्षणीयरीतीने वाढतो. भाषांतरांशिवाय क्लोन करण्यासाठी sparse checkout वापरा:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (विंडोज):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> यामुळे कोर्स पूर्ण करण्यासाठी आवश्यक असलेले सर्व काही आपल्याला जलद डाउनलोडसह मिळेल.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## विषय सूची

- परिचय
  - [Phi कुटुंबात स्वागत आहे](./md/01.Introduction/01/01.PhiFamily.md)
  - [आपले वातावरण सेट करणे](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [मुख्य तंत्रज्ञान समजून घेणे](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi मॉडेल्ससाठी AI सुरक्षा](./md/01.Introduction/01/01.AISafety.md)
  - [Phi हार्डवेअर समर्थन](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [फळा आणि क्लाऊडवर Phi मॉडेल्स आणि उपलब्धता](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai आणि Phi वापरणे](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub मार्केटप्लेस मॉडेल्स](https://github.com/marketplace/models)
  - [Azure AI मॉडेल कॅटलॉग](https://ai.azure.com)

- वेगवेगळ्या वातावरणात Phi चे अनुमान लावणे
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub मॉडेल्स](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Microsoft Foundry मॉडेल कॅटलॉग](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI टूलकिट VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry लोकल](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi कुटुंबाचे अनुमान लावणे
    - [iOS मध्ये Phi चे अनुमान लावणे](./md/01.Introduction/03/iOS_Inference.md)
    - [Android मध्ये Phi चे अनुमान लावणे](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson मध्ये Phi चे अनुमान लावणे](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC मध्ये Phi चे अनुमान लावणे](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX फ्रेमवर्कसह Phi चे अनुमान लावणे](./md/01.Introduction/03/MLX_Inference.md)
    - [लोकल सर्व्हरमध्ये Phi चे अनुमान लावणे](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI टूलकिट वापरून रिमोट सर्व्हरवर Phi चे अनुमान लावणे](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust सह Phi चे अनुमान लावणे](./md/01.Introduction/03/Rust_Inference.md)
    - [लोकलमध्ये Phi--Vision चे अनुमान लावणे](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure कंटेनर्ससह Phi चे अनुमान लावणे (अधिकृत समर्थन)](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi कुटुंबाचे क्वांटिफायिंग](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp वापरून Phi-3.5 / 4 चे क्वांटायझेशन](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime साठी Generative AI विस्तार वापरून Phi-3.5 / 4 चे क्वांटायझेशन](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO वापरून Phi-3.5 / 4 चे क्वांटायझेशन](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX फ्रेमवर्क वापरून Phi-3.5 / 4 चे क्वांटायझेशन](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi चे मूल्यमापन
    - [जवाबदारी AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Microsoft Foundry मूल्यमापनासाठी](./md/01.Introduction/05/AIFoundry.md)
    - [मूल्यमापनासाठी Promptflow वापरणे](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search सह RAG
    - [Phi-4-mini आणि Phi-4-multimodal(RAG) Azure AI Search सह कसे वापरायचे](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)
    - [Zero-Cloud लोकल Hybrid RAG SQLite FTS5 आणि phi-4-mini सह](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-mini_Local_Hybrid_RAG_SQLite_FTS5.ipynb)

- Phi अनुप्रयोग विकास नमुने
  - मजकूर आणि चॅट अनुप्रयोग
    - Phi-4 नमुने
      - [📓] [Phi-4-mini ONNX मॉडेल सह चॅट](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 लोकल ONNX मॉडेल सह चॅट .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel वापरून Phi-4 ONNX सह .NET कन्सोल अ‍ॅप चॅट](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)

    - Phi-3 / 3.5 नमुने
      - [Phi3, ONNX Runtime Web आणि WebGPU वापरून ब्राउझरमधील स्थानिक चॅटबोट](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino चॅट](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [मल्टी मॉडेल - इंटरऍक्टिव्ह Phi-3-mini आणि OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - रॅपर तयार करणे आणि Phi-3 वापरून MLFlow सह वापरणे](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [मॉडेल ऑप्टिमायझेशन - Olive सह ONNX Runtime Web साठी Phi-3-min मॉडेल कसे ऑप्टिमाईज करावे](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx सह WinUI3 अॅप](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 मल्टी मॉडेल AI पॉवर्ड नोट्स अॅप नमुना](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [Prompt flow सह कस्टम Phi-3 मॉडेल्सचा फाइन-ट्यून आणि एकत्रीकरण](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Microsoft Foundry मध्ये Prompt flow सह कस्टम Phi-3 मॉडेल्स फाइन-ट्यून आणि एकत्रीकरण](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft च्या जबाबदार AI तत्त्वांवर लक्ष केंद्रीत करून Microsoft Foundry मध्ये फाइन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलचे मूल्यांकन](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct भाषा भाकीत नमुना (चिनी/इंग्रजी)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG चॅटबोट](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Phi-3.5-Instruct ONNX सह Windows GPU वापरून Prompt flow सोल्यूशन तयार करणे](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite वापरून Android अॅप तयार करणे](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [Microsoft.ML.OnnxRuntime वापरून स्थानिक ONNX Phi-3 मॉडेल वापरणारे Q&A .NET उदाहरण](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel आणि Phi-3 सह Console चॅट .NET अॅप](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK कोड आधारित नमुने 
    - Phi-4 नमुने 
      - [📓] [Phi-4-multimodal वापरून प्रोजेक्ट कोड तयार करणे](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 नमुने
      - [Microsoft Phi-3 कुटुंबासह Visual Studio Code GitHub Copilot चॅट तयार करा](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub मॉडेल्सद्वारे Phi-3.5 सह तुमचा स्वतःचा Visual Studio Code चॅट कॉपिलोٽ एजंट तयार करा](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - प्रगत तर्कशास्त्र नमुने
    - Phi-4 नमुने 
      - [📓] [Phi-4-mini-reasoning किंवा Phi-4-reasoning नमुने](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive सह Phi-4-mini-reasoning फाइन-ट्यूनिंग](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX सह Phi-4-mini-reasoning फाइन-ट्यूनिंग](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub मॉडेल्ससह Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Microsoft Foundry मॉडेल्ससह Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - डेमो
      - [Phi-4-mini डेमो Hugging Face Spaces वर होस्ट केलेले](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal डेमो Hugginge Face Spaces वर होस्ट केलेले](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - दृष्टी नमुने
    - Phi-4 नमुने 
      - [📓] [Phi-4-multimodal वापरून प्रतिमा वाचणे आणि कोड तयार करणे](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 नमुने
      -  [📓][Phi-3-vision-प्रतिमा मजकूर ते मजकूर](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP एम्बेडिंग](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [डेमो: Phi-3 रीसायकलिंग](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - व्हिज्युअल भाषा सहाय्यक - Phi3-Vision आणि OpenVINO सह](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 Vision मल्टी-फ्रेम किंवा मल्टी-इमेज नमुना](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Phi-3 Vision स्थानिक ONNX मॉडेल Microsoft.ML.OnnxRuntime .NET वापरून](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [मेनू-आधारित Phi-3 Vision स्थानिक ONNX मॉडेल Microsoft.ML.OnnxRuntime .NET वापरून](../../md/04.HOL/dotnet/src/LabsPhi304)

  - Reasoning-Vision नमुने
    - Phi-4-Reasoning-Vision-15B 
      - [📓] [Phi-4-Reasoning-Vision-15B वापरून jaywalking शोधणे](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb)
      - [📓] [Phi-4-Reasoning-Vision-15B वापरून गणित](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb)
      - [📓] [Phi-4-Reasoning-Vision-15B वापरून UI शोधणे](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb)

  - गणित नमुने
    -  Phi-4-Mini-Flash-Reasoning-Instruct नमुने  [Phi-4-Mini-Flash-Reasoning-Instruct सह गणित डेमो](./md/02.Application/09.Math/MathDemo.ipynb)

  - ऑडिओ नमुने
    - Phi-4 नमुने 
      - [📓] [Phi-4-multimodal वापरून ऑडिओ ट्रान्सक्रिप्ट्स काढणे](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal ऑडिओ नमुना](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal भाषांतर नमुना](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET कन्सोल अॅप्लिकेशन Phi-4-multimodal वापरून ऑडिओ फाइलचे विश्लेषण आणि ट्रान्सक्रिप्ट तयार करणे](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE नमुने
    - Phi-3 / 3.5 नमुने
      - [📓] [Phi-3.5 मिक्सचर ऑफ एक्स्पर्ट्स मॉडेल्स (MoEs) सोशल मीडिया नमुना](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, आणि LlamaIndex सह रिट्रीवल-ऑगमेंटेड जनरेशन (RAG) पाईपलाइन तयार करणे](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - फंक्शन कॉलिंग नमुने
    - Phi-4 नमुने 🆕
      -  [📓] [Phi-4-mini सह फंक्शन कॉलिंग वापरणे](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini सह मल्टि-एजंट्स तयार करण्यासाठी फंक्शन कॉलिंग वापरणे](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama सह फंक्शन कॉलिंग वापरणे](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX सह फंक्शन कॉलिंग वापरणे](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - मल्टीमॉडल मिक्सिंग नमुने
    - Phi-4 नमुने 🆕
      -  [📓] [Phi-4-multimodal तंत्रज्ञान पत्रकार म्हणून वापरणे](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET कन्सोल अॅप्लिकेशन Phi-4-multimodal वापरून प्रतिमा विश्लेषण करणे](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi नमुने फाइन-ट्यूनिंग
  - [फाइन-ट्यूनिंग परिस्थिती](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [फाइन-ट्यूनिंग विरुद्ध RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [फाइन-ट्यूनिंग Phi-3 ला एक उद्योग तज्ञ बनवा](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [AI टूलकिटसाठी VS कोडसह Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure मशीन लर्निंग सेवा सह Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora सह Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora सह Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Microsoft Foundry सह Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK सह Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive सह फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Lab सह फाइन-ट्यूनिंग](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias सह Phi-3-vision फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)

  - [Apple MLX फ्रेमवर्कसह Phi-3 चे फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision चे फाइन-ट्यूनिंग (अधिकृत समर्थन)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure कंटेनर्ससह Phi-3 चे फाइन-ट्यूनिंग (अधिकृत समर्थन)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 आणि 3.5 Vision चे फाइन-ट्यूनिंग](https://github.com/2U1/Phi3-Vision-Finetune)

- हाताळण्याचे प्रयोगशाळा
  - [काटेकोर मॉडेल्सचे अन्वेषण: LLMs, SLMs, स्थानिक विकास आणि बरेच काही](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP ची क्षमता उघडणे: Microsoft Olive सह फाइन-ट्यूनिंग](https://github.com/azure/Ignite_FineTuning_workshop)

- शैक्षणिक संशोधन पेपर आणि प्रकाशने
  - [Textbooks Are All You Need II: phi-1.5 तांत्रिक अहवाल](https://arxiv.org/abs/2309.05463)
  - [Phi-3 तांत्रिक अहवाल: तुमच्या फोनवर स्थानिकपणे उच्च क्षमता असलेली भाषा मॉडेल](https://arxiv.org/abs/2404.14219)
  - [Phi-4 तांत्रिक अहवाल](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini तांत्रिक अहवाल: मिश्रण-ऑफ-LoRAs द्वारे संक्षिप्त परंतु शक्तिशाली मल्टीमॉडल भाषा मॉडेल्स](https://arxiv.org/abs/2503.01743)
  - [वाहनांमधील फंक्शन-कॉलिंगसाठी लहान भाषा मॉडेल्सचे ऑप्टिमायझेशन](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) मल्टिपल-चॉईस प्रश्नोत्तरेसाठी PHI-3 चे फाइन-ट्यूनिंग: पद्धतीशास्त्र, निकाल आणि आव्हाने](https://arxiv.org/abs/2501.01588)
  - [Phi-4-तर्कशक्ती तांत्रिक अहवाल](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-मिनी-तर्कशक्ती तांत्रिक अहवाल](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi मॉडेल्सचा वापर

### Microsoft Foundry वरील Phi

तुम्ही Microsoft Phi वापरणे आणि तुमच्या वेगवेगळ्या हार्डवेअर डिव्हाइसवर E2E सोल्यूशन्स कसे तयार करायचे हे शिकू शकता. स्वतःसाठी Phi अनुभवण्यासाठी, मॉडेल्सशी खेळायला सुरुवात करा आणि Phi ला तुमच्या परिस्थितीसाठी सानुकूलित करा [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) वापरून. तुम्ही [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) पासून सुरूवात करून अधिक जाणून घेऊ शकता.

**प्लेग्राउंड**
प्रत्येक मॉडेलसाठी मॉडेलची चाचणी करण्यासाठी समर्पित प्लेग्राउंड आहे [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub मॉडेल्स वरील Phi

तुम्ही Microsoft Phi वापरणे आणि तुमच्या वेगवेगळ्या हार्डवेअर डिव्हाइसवर E2E सोल्यूशन्स कसे तयार करायचे हे शिकू शकता. स्वतःसाठी Phi अनुभवण्यासाठी, मॉडेलशी खेळायला सुरुवात करा आणि Phi ला तुमच्या परिस्थितीसाठी सानुकूलित करा [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) वापरून. तुम्ही [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) पासून सुरूवात करून अधिक जाणून घेऊ शकता.

**प्लेग्राउंड**
प्रत्येक मॉडेलसाठी समर्पित [मॉडेल तपासणीसाठी प्लेग्राउंड](/md/02.QuickStart/GitHubModel_QuickStart.md) आहे.

### Hugging Face वरील Phi

तुम्ही मॉडेल [Hugging Face](https://huggingface.co/microsoft) वर देखील शोधू शकता.

**प्लेग्राउंड**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 इतर अभ्यासक्रम

आमची टीम इतर अभ्यासक्रम तयार करते! तपासा:

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
 
### जनरेटिव AI मालिका
[![जनरेटिव AI सुरु करण्यासाठी](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![जनरेटिव AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![जनरेटिव AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![जनरेटिव AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### कोअर शिक्षण
[![कॉम्प्युटर शिक्षण सुरु करण्यासाठी](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![डेटा सायन्स सुरु करण्यासाठी](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI सुरु करण्यासाठी](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![सायबरसुरक्षा सुरु करण्यासाठी](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![वेब विकास सुरु करण्यासाठी](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT सुरु करण्यासाठी](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR विकास सुरु करण्यासाठी](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot मालिका
[![AI जोड्यांसाठी Copilot कार्यक्रम](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET साठी Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot साहस](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## जबाबदार AI

Microsoft आमच्या ग्राहकांना आमचे AI उत्पादने जबाबदारीने वापरण्यास मदत करण्यासाठी, आमचे अनुभव सामायिक करण्यासाठी, आणि पारदर्शकता नोट्स आणि परिणाम मूल्यांकनांसारखे साधने वापरून विश्वासावर आधारित भागीदारी तयार करण्यासाठी कटिबद्ध आहे. या संसाधनांचे अनेक प्रकार तुम्हाला [https://aka.ms/RAI](https://aka.ms/RAI) येथे मिळू शकतात.
Microsoft ची जबाबदार AI धोरण आमच्या AI तत्त्वांवर आधारित आहे ज्यात न्याय, विश्वासार्हता आणि सुरक्षितता, गोपनीयता आणि सुरक्षा, समावेशकता, पारदर्शकता, आणि जबाबदारी या गोष्टींचा समावेश आहे.

मोठ्या प्रमाणावर नैसर्गिक भाषा, प्रतिमा, आणि भाषण मॉडेल्स - जे या नमुन्यात वापरले आहेत - अस्वीकार्य, असमर्थनीय, किंवा असभ्य वर्तन करू शकतात, ज्यामुळे त्रास होऊ शकतो. कृपया धोके आणि मर्यादा जाणून घेण्यासाठी [Azure OpenAI सेवा पारदर्शकता नोट](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) पहा.


या धोके कमी करण्याचा शिफारस केलेला दृष्टिकोन म्हणजे आपल्या आर्किटेक्चरमध्ये एक सुरक्षा प्रणाली समाविष्ट करणे ज्यामुळे हानिकारक वर्तन ओळखता येईल आणि टाळता येईल. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) स्वतंत्र संरक्षणाची एक स्तर प्रदान करते, जी अनुप्रयोगांमध्ये आणि सेवा मध्ये हानिकारक वापरकर्त्याद्वारे तयार केलेला आणि AI-निर्मित सामग्री ओळखू शकते. Azure AI Content Safety मध्ये मजकूर आणि प्रतिमा APIs समाविष्ट आहेत जे तुम्हाला हानिकारक सामग्री ओळखण्याची परवानगी देतात. Microsoft Foundry मध्ये, Content Safety सेवा तुम्हाला विविध प्रकारच्या माध्यमांमध्ये हानिकारक सामग्री ओळखण्यासाठी नमुना कोड पाहण्याची, एक्सप्लोर करण्याची आणि वापरून पाहण्याची परवानगी देते. खालील [जलद प्रारंभ दस्तऐवज](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) तुम्हाला सेवेवर विनंत्या करण्यास मार्गदर्शन करतो.

विचारात घेण्याचा आणखी एक पैलू म्हणजे एकूण अनुप्रयोग कार्यक्षमता. बहु-माध्यम आणि बहु-मॉडेल अनुप्रयोगांसह, आम्ही कार्यक्षमता याचा अर्थ असा घेतो की प्रणाली तुम्ही आणि तुमचे वापरकर्ते अपेक्षित करतात तशी कार्य करते, ज्यात हानिकारक आउटपुट तयार न करणे देखील समाविष्ट आहे. तुमच्या एकूण अनुप्रयोगाच्या कार्यक्षमतेचे मूल्यांकन करणे महत्त्वाचे आहे [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) वापरून. तुम्ही [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) तयार करणे आणि मूल्यांकन करण्याची क्षमता देखील ठेवता.

तुम्ही तुमच्या AI अनुप्रयोगाचे मूल्यांकन तुमच्या विकास वातावरणात [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) वापरून करू शकता. एखाद्या चाचणी डेटासेट किंवा लक्ष्य दिल्यास, तुमच्या जनरेटिव्ह AI अनुप्रयोगाच्या निर्मितीचे सैद्धांतिक मोजमाप केले जातात अंगभूत मूल्यांकन करणाऱ्यांनी किंवा तुमच्या पसंतीनुसार तयार केलेल्या मूल्यांकन करणाऱ्यांनी. तुमच्या सिस्टमचे मूल्यांकन करण्यासाठी azure ai evaluation sdk सह प्रारंभ करण्यासाठी, तुम्ही [जलद प्रारंभ मार्गदर्शक](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) पालन करू शकता. एकदा तुम्ही मूल्यांकन रॅन कार्यान्वित केल्यावर, तुम्ही [Microsoft Foundry मध्ये निकालांचे दृश्य](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) पाहू शकता.

## ट्रेडमार्क्स

हा प्रकल्प प्रकल्प, उत्पादने किंवा सेवा यांचे ट्रेडमार्क किंवा लोगो समाविष्ट करू शकतो. Microsoft ट्रेडमार्क किंवा लोगोच्या अधिकृत वापरावर [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) च्या अटी लागू होतात आणि त्या पाळाव्या लागतात.
Microsoft ट्रेडमार्क किंवा लोगोचा या प्रकल्पाच्या सुधारित आवृत्त्यांमध्ये वापर केल्यास गोंधळ निर्माण होऊ नये किंवा Microsoft च्या प्रायोजकत्वाचा भास होऊ नये. तृतीय पक्षाच्या ट्रेडमार्क किंवा लोगोचा वापर त्या तृतीय पक्षाच्या धोरणांनुसार असेल.

## मदत घेणे

तुम्हाला अडचण आली किंवा AI अनुप्रयोग तयार करण्याबाबत काही प्रश्न असतील तर, सामील व्हा:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

उत्पादन अभिप्राय किंवा त्रुटी असल्यास, भेट द्या:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->