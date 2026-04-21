# Phi कुकबुक: Microsoft के Phi मॉडलों के साथ व्यावहारिक उदाहरण

[![GitHub Codespaces में नमूने खोलें और उपयोग करें](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![डेव कंटेनरों में खोलें](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub योगदानकर्ता](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub मुद्दे](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub पुल-रिक्वेस्ट](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs स्वागत है](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub वॉचर्स](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub स्टार्स](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry डिस्कॉर्ड](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi Microsoft द्वारा विकसित मुक्त स्रोत AI मॉडलों की एक श्रृंखला है।

Phi वर्तमान में सबसे शक्तिशाली और किफायती छोटे भाषा मॉडल (SLM) है, जिसमें बहुभाषी, तर्कशक्ति, टेक्स्ट/चैट जनरेशन, कोडिंग, छवियाँ, ऑडियो और अन्य परिदृश्यों में बहुत अच्छे बेंचमार्क हैं।

आप Phi को क्लाउड या एज उपकरणों पर तैनात कर सकते हैं, और सीमित कंप्यूटिंग शक्ति के साथ आसानी से जनरेटिव AI अनुप्रयोग बना सकते हैं।

इन संसाधनों का उपयोग शुरू करने के लिए इन चरणों का पालन करें:
1. **संग्रहालय को फोर्क करें**: क्लिक करें [![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **संग्रहालय क्लोन करें**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI डिस्कॉर्ड समुदाय से जुड़ें और विशेषज्ञों तथा अन्य डेवलपर्स से मिलें**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/hi/cover.eb18d1b9605d754b.webp)

### 🌐 बहुभाषी समर्थन

#### GitHub Action द्वारा समर्थित (स्वचालित और हमेशा अप-टू-डेट)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अंग्रेज़ी](../ar/README.md) | [बंगाली](../bn/README.md) | [बुल्गेरियाई](../bg/README.md) | [बर्मीज़ (म्यांमार)](../my/README.md) | [चीनी (सरलीकृत)](../zh-CN/README.md) | [चीनी (पारंपरिक, हॉन्ग कॉन्ग)](../zh-HK/README.md) | [चीनी (पारंपरिक, मकाओ)](../zh-MO/README.md) | [चीनी (पारंपरिक, ताइवान)](../zh-TW/README.md) | [क्रोएशियाई](../hr/README.md) | [चेक](../cs/README.md) | [डेनिश](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियाई](../et/README.md) | [फ़िनिश](../fi/README.md) | [फ्रेंच](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिन्दी](./README.md) | [हंगेरियन](../hu/README.md) | [इंडोनेशियाई](../id/README.md) | [इटालियन](../it/README.md) | [जापानी](../ja/README.md) | [कन्नड़](../kn/README.md) | [ख़मेर](../km/README.md) | [कोरियाई](../ko/README.md) | [लिथुआनियाई](../lt/README.md) | [मलय](../ms/README.md) | [मलयालम](../ml/README.md) | [मराठी](../mr/README.md) | [नेपाली](../ne/README.md) | [नाइजीरियाई पिजिन](../pcm/README.md) | [नॉर्वेजियन](../no/README.md) | [फारसी (पर्शियन)](../fa/README.md) | [पोलिश](../pl/README.md) | [पुर्तगाली (ब्राज़ील)](../pt-BR/README.md) | [पुर्तगाली (पुर्तगाल)](../pt-PT/README.md) | [पंजाबी (गुरमुखी)](../pa/README.md) | [रोमानियाई](../ro/README.md) | [रूसी](../ru/README.md) | [सर्बियाई (सिरिलिक)](../sr/README.md) | [स्लोवाक](../sk/README.md) | [स्लोवेनियाई](../sl/README.md) | [स्पेनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिश](../sv/README.md) | [टागालोग (फिलीपीनी)](../tl/README.md) | [तमिल](../ta/README.md) | [तेलुगू](../te/README.md) | [थाई](../th/README.md) | [तुर्की](../tr/README.md) | [यूक्रेनी](../uk/README.md) | [उर्दू](../ur/README.md) | [वियतनामी](../vi/README.md)

> **स्थानीय रूप से क्लोन करना पसंद है?**
>
> इस संग्रहालय में 50+ भाषा अनुवाद शामिल हैं जो डाउनलोड आकार को काफी बढ़ा देते हैं। अनुवादों के बिना क्लोन करने के लिए sparse checkout का उपयोग करें:
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
> यह आपको कोर्स पूरा करने के लिए आवश्यक सब कुछ बहुत तेज़ डाउनलोड के साथ देता है।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## विषय सूची

- परिचय
  - [Phi परिवार में आपका स्वागत है](./md/01.Introduction/01/01.PhiFamily.md)
  - [आपका पर्यावरण सेट अप करना](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [मुख्य तकनीकों को समझना](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi मॉडलों के लिए AI सुरक्षा](./md/01.Introduction/01/01.AISafety.md)
  - [Phi हार्डवेयर समर्थन](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi मॉडल और प्लेटफार्मों पर उपलब्धता](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai और Phi का उपयोग करना](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub मार्केटप्लेस मॉडल्स](https://github.com/marketplace/models)
  - [Azure AI मॉडल कैटलॉग](https://ai.azure.com)

- विभिन्न वातावरण में Phi का अनुमान
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [GitHub मॉडल](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Microsoft Foundry मॉडल कैटलॉग](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI टूलकिट VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry स्थानीय](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi परिवार का अनुमान
    - [iOS में Phi का अनुमान](./md/01.Introduction/03/iOS_Inference.md)
    - [Android में Phi का अनुमान](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson में Phi का अनुमान](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC में Phi का अनुमान](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX फ्रेमवर्क के साथ Phi का अनुमान](./md/01.Introduction/03/MLX_Inference.md)
    - [स्थानीय सर्वर में Phi का अनुमान](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI टूलकिट का उपयोग कर रिमोट सर्वर में Phi का अनुमान](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust के साथ Phi का अनुमान](./md/01.Introduction/03/Rust_Inference.md)
    - [स्थानीय में Phi--विजन का अनुमान](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure कंटेनरों (आधिकारिक समर्थन) के साथ Phi का अनुमान](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi परिवार का क्वांटिफिकेशन](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp का उपयोग करके Phi-3.5 / 4 का क्वांटाइजेशन](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime के लिए जनरेटिव AI एक्सटेंशन्स का उपयोग करके Phi-3.5 / 4 का क्वांटाइजेशन](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO का उपयोग करके Phi-3.5 / 4 का क्वांटाइजेशन](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX फ्रेमवर्क का उपयोग करके Phi-3.5 / 4 का क्वांटाइजेशन](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi का मूल्यांकन
    - [जिम्मेदार AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [मूल्यांकन के लिए Microsoft Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [मूल्यांकन के लिए Promptflow का उपयोग](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI सर्च के साथ RAG
    - [Azure AI सर्च के साथ Phi-4-mini और Phi-4-multimodal (RAG) कैसे उपयोग करें](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi एप्लिकेशन विकास नमूने
  - टेक्स्ट और चैट एप्लिकेशन
    - Phi-4 नमूने 
      - [📓] [Phi-4-mini ONNX मॉडल के साथ चैट करें](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 स्थानीय ONNX मॉडल .NET के साथ चैट करें](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Sementic Kernel का उपयोग कर Phi-4 ONNX के साथ .NET कंसोल ऐप में चैट](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 नमूने
      - [Phi3, ONNX Runtime Web और WebGPU का उपयोग करके ब्राउज़र में स्थानीय चैटबोट](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino चैट](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [मल्टी मॉडल - इंटरैक्टिव Phi-3-mini और OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - एक रैपर बनाना और Phi-3 को MLFlow के साथ उपयोग करना](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [मॉडल अनुकूलन - ONNX Runtime Web के लिए Phi-3-min मॉडल को Olive के साथ कैसे अनुकूलित करें](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx के साथ WinUI3 ऐप](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 मल्टी मॉडल एआई पावर्ड नोट्स ऐप सैंपल](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [कस्टम Phi-3 मॉडल्स को फाइन-ट्यून और इंटीग्रेट करें Prompt flow के साथ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Microsoft Foundry में Prompt flow के साथ कस्टम Phi-3 मॉडल्स को फाइन-ट्यून और इंटीग्रेट करें](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft के जिम्मेदार AI सिद्धांतों पर ध्यान केंद्रित करते हुए Microsoft Foundry में फाइन-ट्यून किए गए Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करें](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-mini-instruct भाषा भविष्यवाणी सैंपल (चीनी/अंग्रेज़ी)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG चैटबॉट](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Windows GPU का उपयोग करके Prompt flow समाधान बनाना Phi-3.5-Instruct ONNX के साथ](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite का उपयोग करके Android ऐप बनाना](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [स्थानीय ONNX Phi-3 मॉडल का उपयोग करते हुए Q&A .NET उदाहरण Microsoft.ML.OnnxRuntime के साथ](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel और Phi-3 के साथ कंसोल चैट .NET ऐप](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK कोड आधारित सैंपल्स
    - Phi-4 सैंपल्स
      - [📓] [Phi-4-multimodal का उपयोग करके प्रोजेक्ट कोड जेनरेट करें](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 सैंपल्स
      - [Microsoft Phi-3 परिवार के साथ अपना Visual Studio Code GitHub Copilot Chat बनाएं](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub मॉडल्स के साथ Phi-3.5 द्वारा अपना Visual Studio Code चैट कोपिलट एजेंट बनाएं](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - एडवांस्ड रीजनिंग सैंपल्स
    - Phi-4 सैंपल्स
      - [📓] [Phi-4-mini-रीज़निंग या Phi-4-रीज़निंग सैंपल्स](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive के साथ Phi-4-mini-रीज़निंग का फाइन-ट्यूनिंग](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX के साथ Phi-4-mini-रीज़निंग का फाइन-ट्यूनिंग](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub मॉडल्स के साथ Phi-4-mini-रीज़निंग](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Microsoft Foundry मॉडल्स के साथ Phi-4-mini-रीज़निंग](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - डेमोस
      - [Phi-4-mini डेमोस जो Hugging Face Spaces पर होस्ट किए गए हैं](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal डेमोस जो Hugginge Face Spaces पर होस्ट किए गए हैं](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - विज़न सैंपल्स
    - Phi-4 सैंपल्स
      - [📓] [Phi-4-multimodal का उपयोग करके इमेज पढ़ें और कोड जनरेट करें](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)
    - Phi-3 / 3.5 सैंपल्स
      -  [📓][Phi-3-विजन-इमेज टेक्स्ट से टेक्स्ट](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-विजन-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-विजन CLIP एम्बेडिंग](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [डेमो: Phi-3 रीसायक्लिंग](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-विजन - विज़ुअल भाषा सहायक - Phi3-विजन और OpenVINO के साथ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 विज़न Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 विज़न OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 विज़न मल्टी-फ्रेम या मल्टी-इमेज सैंपल](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET का उपयोग करके Phi-3 विज़न लोकल ONNX मॉडल](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [मेन्यू आधारित Phi-3 विज़न लोकल ONNX मॉडल Microsoft.ML.OnnxRuntime .NET के साथ](../../md/04.HOL/dotnet/src/LabsPhi304)

  - रीजनिंग-विजन सैंपल्स
    - Phi-4-रीजनिंग-विजन-15B
      - [📓] [Phi-4-रीजनिंग-विजन-15B का उपयोग करते हुए जायकिंग डिटेक्ट करना](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb)
      - [📓] [Phi-4-रीजनिंग-विजन-15B का उपयोग करते हुए गणना करना](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb)
      - [📓] [Phi-4-रीजनिंग-विजन-15B का उपयोग करते हुए UI डिटेक्ट करना](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb)

  - मैथ सैंपल्स
    - Phi-4-मिनी-फ्लैश-रीजनिंग-इंस्ट्रक्ट सैंपल्स  [Phi-4-मिनी-फ्लैश-रीजनिंग-इंस्ट्रक्ट के साथ मैथ डेमो](./md/02.Application/09.Math/MathDemo.ipynb)

  - ऑडियो सैंपल्स
    - Phi-4 सैंपल्स
      - [📓] [Phi-4-multimodal का उपयोग करके ऑडियो ट्रांस्क्रिप्ट निकालना](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal ऑडियो सैंपल](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal भाषण अनुवाद सैंपल](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET कंसोल एप्लिकेशन जो Phi-4-multimodal ऑडियो का उपयोग करके ऑडियो फ़ाइल का विश्लेषण करता है और ट्रांस्क्रिप्ट जेनरेट करता है](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE सैंपल्स
    - Phi-3 / 3.5 सैंपल्स
      - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) सोशल मीडिया सैंपल](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, और LlamaIndex के साथ एक Retrieval-Augmented Generation (RAG) पाइपलाइन बनाना](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - फंक्शन कॉलिंग सैंपल्स
    - Phi-4 सैंपल्स 🆕
      -  [📓] [Phi-4-mini के साथ फंक्शन कॉलिंग का उपयोग](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini के साथ मल्टी-एजेंट्स बनाने के लिए फंक्शन कॉलिंग का उपयोग](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [Ollama के साथ फंक्शन कॉलिंग का उपयोग](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX के साथ फंक्शन कॉलिंग का उपयोग](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - मल्टीमॉडल मिक्सिंग सैंपल्स
    - Phi-4 सैंपल्स 🆕
      -  [📓] [Phi-4-multimodal का उपयोग एक टेक्नोलॉजी पत्रकार के रूप में](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET कंसोल एप्लिकेशन जो Phi-4-multimodal का उपयोग करके इमेज का विश्लेषण करता है](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi फाइन-ट्यूनिंग सैंपल्स
  - [फाइन-ट्यूनिंग परिदृश्य](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [फाइन-ट्यूनिंग बनाम RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 को एक उद्योग विशेषज्ञ बनने दें फाइन-ट्यूनिंग](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS कोड के लिए AI टूलकिट के साथ Phi-3 का फाइन-ट्यूनिंग](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure मशीन लर्निंग सेवा के साथ Phi-3 का फाइन-ट्यूनिंग](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora के साथ Phi-3 का फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora के साथ Phi-3 का फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Microsoft Foundry के साथ Phi-3 का फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK के साथ Phi-3 का फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive के साथ फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive Hands-On Lab के साथ फाइन-ट्यूनिंग](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias के साथ Phi-3-vision का फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX Framework के साथ Phi-3 का फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-vision का फाइन-ट्यूनिंग (आधिकारिक समर्थन)](./md/03.FineTuning/FineTuning_Vision.md)
  - [काइटो AKS के साथ Phi-3 का फाइन-ट्यूनिंग, Azure कंटेनर (आधिकारिक समर्थन)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 और 3.5 विजन का फाइन-ट्यूनिंग](https://github.com/2U1/Phi3-Vision-Finetune)

- हैंड्स ऑन लैब
  - [प्रगतिशील मॉडलों का अन्वेषण: LLMs, SLMs, स्थानीय विकास और भी बहुत कुछ](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP की क्षमता का अनलॉकिंग: Microsoft Olive के साथ फाइन-ट्यूनिंग](https://github.com/azure/Ignite_FineTuning_workshop)

- शैक्षणिक शोध पत्र और प्रकाशन
  - [Textbooks Are All You Need II: phi-1.5 तकनीकी रिपोर्ट](https://arxiv.org/abs/2309.05463)
  - [Phi-3 तकनीकी रिपोर्ट: एक अत्यंत सक्षम भाषा मॉडल आपके फोन पर स्थानीय](https://arxiv.org/abs/2404.14219)
  - [Phi-4 तकनीकी रिपोर्ट](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini तकनीकी रिपोर्ट: मिश्रण-ऑफ़-LoRAs के माध्यम से कॉम्पैक्ट फिर भी शक्तिशाली मल्टीमॉडल भाषा मॉडल](https://arxiv.org/abs/2503.01743)
  - [वाहन के अंदर फ़ंक्शन-कॉलिंग के लिए छोटे भाषा मॉडलों का अनुकूलन](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) बहुविकल्पीय प्रश्न उत्तर देने के लिए PHI-3 का फाइन-ट्यूनिंग: कार्यप्रणाली, परिणाम और चुनौतियां](https://arxiv.org/abs/2501.01588)
  - [Phi-4-तर्क तकनीकी रिपोर्ट](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-मिनी-तर्क तकनीकी रिपोर्ट](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi मॉडल का उपयोग करना

### Microsoft Foundry पर Phi

आप Microsoft Phi का उपयोग कैसे करें और अपने विभिन्न हार्डवेयर उपकरणों में E2E समाधान कैसे बनाएं, यह सीख सकते हैं। Phi का अनुभव करने के लिए, मॉडल के साथ खेलने और अपने परिदृश्यों के लिए Phi को अनुकूलित करने से शुरू करें [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) का उपयोग कर सकते हैं। आप [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) के साथ शुरू करना सीख सकते हैं।

**प्लेस्टेशन**
प्रत्येक मॉडल के पास उसके परीक्षण के लिए समर्पित प्लेग्राउंड है [Azure AI Playground](https://aka.ms/try-phi3)।

### GitHub Models पर Phi

आप Microsoft Phi का उपयोग कैसे करें और अपने विभिन्न हार्डवेयर उपकरणों में E2E समाधान कैसे बनाएं, यह सीख सकते हैं। Phi का अनुभव करने के लिए, मॉडल के साथ खेलने और अपने परिदृश्यों के लिए Phi को अनुकूलित करने से शुरू करें [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) का उपयोग कर सकते हैं। आप [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) के साथ शुरू करना सीख सकते हैं।

**प्लेस्टेशन**
प्रत्येक मॉडल के लिए समर्पित परीक्षण [प्लेग्राउंड](/md/02.QuickStart/GitHubModel_QuickStart.md) उपलब्ध है।

### Hugging Face पर Phi

आप यह मॉडल [Hugging Face](https://huggingface.co/microsoft) पर भी पा सकते हैं।

**प्लेस्टेशन**
[Hugging Chat प्लेग्राउंड](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 अन्य कोर्स

हमारी टीम अन्य कोर्स भी बनाती है! देखें:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / एजेंट्स
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### जनरेटिव AI श्रृंखला
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### कोर लर्निंग
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![साइबरसुरक्षा शुरुआती के लिए](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev शुरुआती के लिए](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT शुरुआती के लिए](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development शुरुआती के लिए](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### कॉपिलट श्रृंखला
[![AI जोड़ीदार प्रोग्रामिंग के लिए कॉपिलट](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET के लिए कॉपिलट](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![कॉपिलट एडवेंचर](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## ज़िम्मेदार AI

Microsoft हमारे ग्राहकों को हमारे AI उत्पादों का जिम्मेदारी से उपयोग करने में सहायता करने के लिए प्रतिबद्ध है, हमारे अनुभव साझा करता है, और पारदर्शिता नोट्स और प्रभाव आकलनों जैसे उपकरणों के माध्यम से भरोसेमंद साझेदारी बनाता है। इन संसाधनों में से कई [https://aka.ms/RAI](https://aka.ms/RAI) पर पाए जा सकते हैं।  
Microsoft का जिम्मेदार AI के लिए दृष्टिकोण हमारे AI सिद्धांतों पर आधारित है: निष्पक्षता, विश्वसनीयता और सुरक्षा, गोपनीयता और सुरक्षा, समावेशन, पारदर्शिता, और जवाबदेही।

विस्तृत पैमाने पर प्राकृतिक भाषा, छवि, और भाषण मॉडल - जैसे इस नमूने में उपयोग किए गए - संभावित रूप से अनुचित, अविश्वसनीय, या अपमानजनक व्यवहार कर सकते हैं, जिससे हानि हो सकती है। कृपया जोखिमों और सीमाओं के बारे में सूचित रहने के लिए [Azure OpenAI सेवा पारदर्शिता नोट](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) देखें।
इन जोखिमों को कम करने के लिए अनुशंसित तरीका यह है कि आपकी आर्किटेक्चर में एक सुरक्षा प्रणाली शामिल की जाए जो हानिकारक व्यवहार का पता लगा सके और उसे रोक सके। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) एक स्वतंत्र सुरक्षा परत प्रदान करता है, जो अनुप्रयोगों और सेवाओं में हानिकारक उपयोगकर्ता-जनित और AI-जनित सामग्री का पता लगाने में सक्षम है। Azure AI Content Safety में टेक्स्ट और इमेज API शामिल हैं जो आपको हानिकारक सामग्री का पता लगाने की अनुमति देते हैं। Microsoft Foundry के भीतर, Content Safety सेवा आपको विभिन्न माध्यमों में हानिकारक सामग्री का पता लगाने के लिए नमूना कोड देखने, एक्सप्लोर करने और आज़माने की सुविधा प्रदान करती है। निम्नलिखित [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) आपको सेवा को अनुरोध भेजने में मार्गदर्शन करती है।

एक अन्य पहलू जिसे ध्यान में रखना आवश्यक है, वह है समग्र आवेदन प्रदर्शन। मल्टी-मॉडल और मल्टी-मॉडल्स एप्लिकेशन के साथ, हम प्रदर्शन को इस रूप में देखते हैं कि प्रणाली आपकी और आपके उपयोगकर्ताओं की अपेक्षा के अनुसार कार्य करती है, जिसमें हानिकारक आउटपुट उत्पन्न न करना भी शामिल है। आपके पूरे आवेदन के प्रदर्शन का मूल्यांकन करना महत्वपूर्ण है, इसके लिए [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) का उपयोग करें। आपके पास [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) बनाने और उनका मूल्यांकन करने की भी क्षमता है।

आप अपने विकास पर्यावरण में [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) का उपयोग करके अपने AI आवेदन का मूल्यांकन कर सकते हैं। चाहे आपके पास एक परीक्षण डेटासेट हो या कोई लक्ष्य, आपके जनरेटिव AI आवेदन के जनरेशन को बिल्ट-इन एवालुएटर्स या आपकी पसंद के कस्टम इवालुएटर्स के साथ मात्रात्मक रूप से मापा जाता है। अपने सिस्टम का मूल्यांकन करने के लिए azure ai evaluation sdk के साथ आरंभ करने के लिए, आप [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) का पालन कर सकते हैं। एक बार जब आप एक मूल्यांकन रन निष्पादित करते हैं, तो आप [Microsoft Foundry में परिणामों का विज़ुअलीकरण कर सकते हैं](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)।

## ट्रेडमार्क

यह परियोजना परियोजनाओं, उत्पादों, या सेवाओं के ट्रेडमार्क या लोगो शामिल कर सकती है। माइक्रोसॉफ्ट ट्रेडमार्क या लोगो के अधिकृत उपयोग को [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) का पालन करना आवश्यक है।
माइक्रोसॉफ्ट ट्रेडमार्क या लोगो का इस परियोजना के परिवर्तित संस्करणों में उपयोग भ्रम पैदा नहीं करना चाहिए या माइक्रोसॉफ्ट प्रायोजन का संकेत नहीं देना चाहिए। किसी भी तृतीय-पक्ष ट्रेडमार्क या लोगो का उपयोग तृतीय-पक्ष की नीतियों के अनुसार होगा।

## सहायता प्राप्त करना

यदि आप फंस जाते हैं या AI ऐप्स बनाने के संबंध में कोई प्रश्न है, तो जुड़ें:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

यदि आपके पास उत्पाद प्रतिक्रिया है या निर्माण के दौरान त्रुटियाँ होती हैं तो देखें:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद एआई अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान रखें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ उसकी स्वदेशी भाषा में ही आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->