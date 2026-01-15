<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2e4b490f4bd424b095f21e38c6af33b",
  "translation_date": "2026-01-05T16:28:26+00:00",
  "source_file": "README.md",
  "language_code": "hi"
}
-->
# Phi कुकबुक: Microsoft के Phi मॉडल के साथ व्यावहारिक उदाहरण

[![GitHub Codespaces में नमूने खोलें और उपयोग करें](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers में खोलें](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub योगदानकर्ता](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub मुद्दे](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub पुल अनुरोध](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs स्वागत है](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub वॉचर्स](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub स्टार्स](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi Microsoft द्वारा विकसित किए गए खुले स्रोत AI मॉडलों की एक श्रृंखला है।

Phi वर्तमान में सबसे शक्तिशाली और लागत-कुशल छोटे भाषा मॉडल (SLM) है, जिसमें बहु-भाषा, तर्क, टेक्स्ट/चैट जनरेशन, कोडिंग, छवियां, ऑडियो और अन्य परिदृश्यों में बहुत अच्छे मानक हैं।

आप Phi को क्लाउड या एज उपकरणों पर तैनात कर सकते हैं, और आप सीमित कंप्यूटिंग पावर के साथ सहजता से जनरेटिव AI अनुप्रयोग बना सकते हैं।

इन संसाधनों का उपयोग शुरू करने के लिए निम्नलिखित कदमों का पालन करें:
1. **रिपोजिटरी को फोर्क करें**: क्लिक करें [![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **रिपोजिटरी को क्लोन करें**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord समुदाय में शामिल हों और विशेषज्ञों तथा अन्य डेवलपर्स से मिलें**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/hi/cover.eb18d1b9605d754b.png)

### 🌐 बहु-भाषा समर्थन

#### GitHub Action के माध्यम से समर्थित (स्वचालित और हमेशा अद्यतन)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरबी](../ar/README.md) | [बंगाली](../bn/README.md) | [बुल्गारियाई](../bg/README.md) | [बर्मी (म्यांमार)](../my/README.md) | [चीनी (सरलीकृत)](../zh/README.md) | [चीनी (परंपरागत, हॉन्ग कॉन्ग)](../hk/README.md) | [चीनी (परंपरागत, मकाऊ)](../mo/README.md) | [चीनी (परंपरागत, ताइवान)](../tw/README.md) | [क्रोएशियाई](../hr/README.md) | [चेक](../cs/README.md) | [डेनिश](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियाई](../et/README.md) | [फ़िनिश](../fi/README.md) | [फ्रेंच](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिंदी](./README.md) | [हंगेरियन](../hu/README.md) | [इंडोनेशियाई](../id/README.md) | [इतालवी](../it/README.md) | [जापानी](../ja/README.md) | [कन्नड़](../kn/README.md) | [कोरियाई](../ko/README.md) | [लिथुआनियाई](../lt/README.md) | [मलय](../ms/README.md) | [मलयालम](../ml/README.md) | [मराठी](../mr/README.md) | [नेपाली](../ne/README.md) | [नाइजीरियाई पेड्जिन](../pcm/README.md) | [नॉर्वेजियन](../no/README.md) | [फ़ारसी (पर्शियन)](../fa/README.md) | [पोलिश](../pl/README.md) | [पुर्तगाली (ब्राजील)](../br/README.md) | [पुर्तगाली (पुर्तगाल)](../pt/README.md) | [पंजाबी (गुरमुखी)](../pa/README.md) | [रोमानियाई](../ro/README.md) | [रूसी](../ru/README.md) | [सर्बियाई (सिरिलिक)](../sr/README.md) | [स्लोवाक](../sk/README.md) | [स्लोवेनियाई](../sl/README.md) | [स्पेनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिश](../sv/README.md) | [टैगलॉग (फिलीपीनो)](../tl/README.md) | [तमिल](../ta/README.md) | [तेलुगु](../te/README.md) | [थाई](../th/README.md) | [तुर्की](../tr/README.md) | [यूक्रेनी](../uk/README.md) | [उर्दू](../ur/README.md) | [वियतनामी](../vi/README.md)

> **स्थानीय रूप से क्लोन करना पसंद करें?**

> इस रिपोजिटरी में 50+ भाषाओं के अनुवाद शामिल हैं जो डाउनलोड साइज को काफी बढ़ा देते हैं। अनुवाद के बिना क्लोन करने के लिए sparse checkout का उपयोग करें:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> यह आपको कोर्स पूरा करने के लिए आवश्यक सब कुछ देता है, साथ ही डाउनलोड भी बहुत तेज़ होता है।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## सामग्री सूची

- परिचय
  - [Phi परिवार में आपका स्वागत है](./md/01.Introduction/01/01.PhiFamily.md)
  - [अपने पर्यावरण की सेटिंग करना](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [मुख्य तकनीकों को समझना](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi मॉडलों के लिए AI सुरक्षा](./md/01.Introduction/01/01.AISafety.md)
  - [Phi हार्डवेयर समर्थन](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [फ़िए मॉडल और प्लेटफ़ॉर्म पर उपलब्धता](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai और Phi का उपयोग](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub मार्केटप्लेस मॉडल](https://github.com/marketplace/models)
  - [Azure AI मॉडल कैटलॉग](https://ai.azure.com)

- विभिन्न पर्यावरण में Phi की इंफ़ेरेंस
    -  [हगिंग फेस](./md/01.Introduction/02/01.HF.md)
    -  [GitHub मॉडल](./md/01.Introduction/02/02.GitHubModel.md)
    -  [Azure AI Foundry मॉडल कैटलॉग](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [ओल्लामा](./md/01.Introduction/02/04.Ollama.md)
    -  [AI टूलकिट VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry लोकल](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi परिवार की इंफ़ेरेंस
    - [iOS में Phi की इंफ़ेरेंस](./md/01.Introduction/03/iOS_Inference.md)
    - [Android में Phi की इंफ़ेरेंस](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson में Phi की इंफ़ेरेंस](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC में Phi की इंफ़ेरेंस](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX फ्रेमवर्क के साथ Phi की इंफ़ेरेंस](./md/01.Introduction/03/MLX_Inference.md)
    - [लोकल सर्वर में Phi की इंफ़ेरेंस](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI टूलकिट का उपयोग करके रिमोट सर्वर में Phi की इंफ़ेरेंस](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust के साथ Phi की इंफ़ेरेंस](./md/01.Introduction/03/Rust_Inference.md)
    - [लोकल में Phi--विजन की इंफ़ेरेंस](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure कंटेनर (आधिकारिक समर्थन) के साथ Phi की इंफ़ेरेंस](./md/01.Introduction/03/Kaito_Inference.md)
-  [Phi परिवार के क्वांटिफ़ाइंग](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp का उपयोग करके Phi-3.5 / 4 का क्वांटाइजेशन](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime के लिए जनरेटिव AI एक्सटेंशंस का उपयोग कर Phi-3.5 / 4 का क्वांटाइजेशन](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO का उपयोग करके Phi-3.5 / 4 का क्वांटाइजेशन](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX फ्रेमवर्क का उपयोग करके Phi-3.5 / 4 का क्वांटाइजेशन](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  Phi का मूल्यांकन
    - [जिम्मेदार AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [मूल्यांकन के लिए Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [मूल्यांकन के लिए Promptflow का उपयोग](./md/01.Introduction/05/Promptflow.md)
 
- Azure AI Search के साथ RAG
    - [Azure AI Search के साथ Phi-4-mini और Phi-4-multimodal (RAG) का उपयोग कैसे करें](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi अनुप्रयोग विकास नमूने
  - टेक्स्ट और चैट अनुप्रयोग
    - Phi-4 नमूने 🆕
      - [📓] [Phi-4-mini ONNX मॉडल के साथ चैट करें](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 लोकल ONNX मॉडल .NET के साथ चैट](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Semantic Kernel का उपयोग कर Phi-4 ONNX के साथ .NET कंसोल ऐप में चैट](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 नमूने
      - [Phi3, ONNX रनटाइम वेब और WebGPU का उपयोग करके ब्राउज़र में लोकल चैटबोट](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino चैट](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [मल्टी मॉडल - इंटरैक्टिव Phi-3-मिनी और OpenAI व्हिस्पर](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - एक रैपर बनाना और MLFlow के साथ Phi-3 का उपयोग करना](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [मॉडल अनुकूलन - Olive के साथ ONNX Runtime Web के लिए Phi-3-mini मॉडल को कैसे ऑप्टिमाइज़ करें](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 मिनी-4k-instruct-onnx के साथ WinUI3 ऐप](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      -[WinUI3 मल्टी मॉडल AI संचालित नोट्स ऐप नमूना](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [कस्टम Phi-3 मॉडलों को फाइन-ट्यून और इंटीग्रेट करें Prompt flow के साथ](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [Azure AI Foundry में Prompt flow के साथ कस्टम Phi-3 मॉडलों को फाइन-ट्यून और इंटीग्रेट करें](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [Microsoft के Responsible AI Principles पर ध्यान केंद्रित करते हुए Azure AI Foundry में फाइन-ट्यून Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करें](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [Phi-3.5-मिनी-इंस्ट्रक्ट भाषा भविष्यवाणी नमूना (चीनी/अंग्रेजी)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [Phi-3.5-Instruct WebGPU RAG चैटबॉट](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [Phi-3.5-Instruct ONNX के साथ विंडोज GPU का उपयोग करके Prompt flow समाधान बनाना](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [Microsoft Phi-3.5 tflite का उपयोग करके Android ऐप बनाना](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [स्थानीय ONNX Phi-3 मॉडल का उपयोग करके .NET उदाहरण प्रश्नोत्तर Microsoft.ML.OnnxRuntime के साथ](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [Semantic Kernel और Phi-3 के साथ कंसोल चैट .NET ऐप](../../md/04.HOL/dotnet/src/LabsPhi302)

  - Azure AI Inference SDK कोड आधारित नमूने 
    - Phi-4 नमूने 🆕
      - [📓] [Phi-4-multimodal का उपयोग करके प्रोजेक्ट कोड बनाएँ](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - Phi-3 / 3.5 नमूने
      - [Microsoft Phi-3 परिवार के साथ अपना Visual Studio Code GitHub Copilot Chat बनाएँ](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [GitHub मॉडलों के साथ Phi-3.5 द्वारा अपना Visual Studio Code चैट कॉपिलट एजेंट बनाएँ](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - उन्नत तर्क नमूने
    - Phi-4 नमूने 🆕
      - [📓] [Phi-4-mini-तर्क या Phi-4-तर्क नमूने](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [Microsoft Olive के साथ Phi-4-mini-तर्क का फाइन-ट्यूनिंग](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Apple MLX के साथ Phi-4-mini-तर्क का फाइन-ट्यूनिंग](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [GitHub मॉडलों के साथ Phi-4-mini-तर्क](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Azure AI Foundry मॉडलों के साथ Phi-4-mini-तर्क](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - डेमो
      - [Phi-4-mini डेमो Hugging Face Spaces पर होस्ट किए गए](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [Phi-4-multimodal डेमो Hugging Face Spaces पर होस्ट किए गए](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - विज़न नमूने
    - Phi-4 नमूने 🆕
      - [📓] [Phi-4-multimodal का उपयोग करके छवियाँ पढ़ें और कोड जनरेट करें](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - Phi-3 / 3.5 नमूने
      -  [📓][Phi-3-विजन-छवि पाठ से पाठ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-विजन-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-विजन CLIP एम्बेडिंग](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [डेमो: Phi-3 रीसायक्लिंग](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-विजन - विज़ुअल भाषा सहायक - Phi3-विजन और OpenVINO के साथ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 विज़न Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 विज़न OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][Phi-3.5 विज़न मल्टी-फ्रेम या मल्टी-इमेज नमूना](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [Microsoft.ML.OnnxRuntime .NET का उपयोग करके Phi-3 विज़न लोकल ONNX मॉडल](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [मेनू आधारित Phi-3 विज़न लोकल ONNX मॉडल Microsoft.ML.OnnxRuntime .NET का उपयोग करके](../../md/04.HOL/dotnet/src/LabsPhi304)

  - गणित नमूने
    -  Phi-4-Mini-Flash-Reasoning-Instruct नमूने 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct के साथ मैथ डेमो](./md/02.Application/09.Math/MathDemo.ipynb)

  - ऑडियो नमूने
    - Phi-4 नमूने 🆕
      - [📓] [Phi-4-multimodal का उपयोग करके ऑडियो ट्रांसक्रिप्ट निकालना](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [Phi-4-multimodal ऑडियो नमूना](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [Phi-4-multimodal स्पीच ट्रांसलेशन नमूना](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [.NET कंसोल एप्लिकेशन जो Phi-4-multimodal ऑडियो का उपयोग करके एक ऑडियो फ़ाइल का विश्लेषण करता है और ट्रांसक्रिप्ट जनरेट करता है](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - MOE नमूने
    - Phi-3 / 3.5 नमूने
      - [📓] [Phi-3.5 मिक्सचर ऑफ एक्सपर्ट्स मॉडलों (MoEs) सोशल मीडिया नमूना](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, और LlamaIndex के साथ Retrieval-Augmented Generation (RAG) पाइपलाइन बनाना](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - फ़ंक्शन कॉलिंग नमूने
    - Phi-4 नमूने 🆕
      -  [📓] [Phi-4-mini के साथ फ़ंक्शन कॉलिंग का उपयोग करना](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [Phi-4-mini के साथ मल्टी-एजेंट्स बनाने के लिए फ़ंक्शन कॉलिंग का उपयोग करना](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [ओल्लामा के साथ फ़ंक्शन कॉलिंग का उपयोग करना](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [ONNX के साथ फ़ंक्शन कॉलिंग का उपयोग करना](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - मल्टीमोडल मिक्सिंग नमूने
    - Phi-4 नमूने 🆕
      -  [📓] [Phi-4-multimodal का उपयोग एक तकनीकी पत्रकार के रूप में करना](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [.NET कंसोल एप्लिकेशन जो Phi-4-multimodal का उपयोग करके छवियों का विश्लेषण करता है](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi नमूनों का फाइन-ट्यूनिंग
  - [फाइन-ट्यूनिंग परिदृश्य](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [फाइन-ट्यूनिंग बनाम RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 को एक उद्योग विशेषज्ञ बनने दें फाइन-ट्यूनिंग](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [VS कोड के लिए AI टूलकिट के साथ Phi-3 का फाइन-ट्यूनिंग](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [Azure मशीन लर्निंग सेवा के साथ Phi-3 का फाइन-ट्यूनिंग](./md/03.FineTuning/Introduce_AzureML.md)
  - [Lora के साथ Phi-3 का फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Lora.md)
  - [QLora के साथ Phi-3 का फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Qlora.md)
  - [Azure AI Foundry के साथ Phi-3 का फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [Azure ML CLI/SDK के साथ Phi-3 का फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [Microsoft Olive के साथ फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [Microsoft Olive हैंड्स-ऑन लैब के साथ फाइन-ट्यूनिंग](./md/03.FineTuning/olive-lab/readme.md)
  - [Weights and Bias के साथ Phi-3-विजन का फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [Apple MLX फ्रेमवर्क के साथ Phi-3 का फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLX.md)
  - [Phi-3-विजन (आधिकारिक समर्थन)](./md/03.FineTuning/FineTuning_Vision.md)
  - [Kaito AKS, Azure कंटेनरों के साथ Phi-3 का फाइन-ट्यूनिंग (आधिकारिक समर्थन)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [Phi-3 और 3.5 विज़न का फाइन-ट्यूनिंग](https://github.com/2U1/Phi3-Vision-Finetune)

- हैंड्स ऑन लैब
  - [अत्याधुनिक मॉडलों का अन्वेषण: LLMs, SLMs, स्थानीय विकास और अधिक](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [NLP संभावनाओं का अनलॉक: Microsoft Olive के साथ फाइन-ट्यूनिंग](https://github.com/azure/Ignite_FineTuning_workshop)

- अकादमिक शोध पत्र और प्रकाशन
  - [पाठ्यपुस्तकें ही आपके लिए पर्याप्त हैं II: phi-1.5 तकनीकी रिपोर्ट](https://arxiv.org/abs/2309.05463)
  - [Phi-3 तकनीकी रिपोर्ट: आपके फोन पर स्थानीय रूप से एक अत्यंत सक्षम भाषा मॉडल](https://arxiv.org/abs/2404.14219)
  - [Phi-4 तकनीकी रिपोर्ट](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini तकनीकी रिपोर्ट: मिश्रण-ऑफ-लोरा के माध्यम से कॉम्पैक्ट लेकिन शक्तिशाली मल्टीमॉडल भाषा मॉडल](https://arxiv.org/abs/2503.01743)
  - [वाहन कार्य-कालिंग के लिए छोटे भाषा मॉडल का अनुकूलन](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) बहुविकल्पीय प्रश्नोत्तरी के लिए PHI-3 का फाइन-ट्यूनिंग: पद्धति, परिणाम, और चुनौतियाँ](https://arxiv.org/abs/2501.01588)
  - [Phi-4-तर्क तकनीकी रिपोर्ट](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-मिनी-तर्क तकनीकी रिपोर्ट](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi मॉडल का उपयोग करना

### Azure AI Foundry पर Phi

आप सीख सकते हैं कि Microsoft Phi का कैसे उपयोग करें और अपने विभिन्न हार्डवेयर उपकरणों में E2E समाधान कैसे बनाएं। खुद Phi का अनुभव करने के लिए, मॉडल के साथ खेलना शुरू करें और Phi को अपनी स्थिति के अनुसार अनुकूलित करें, [Azure AI Foundry Azure AI मॉडल कैटलॉग](https://aka.ms/phi3-azure-ai) का उपयोग करके। आप [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) के साथ शुरुआत करने के बारे में अधिक जान सकते हैं।

**प्लेग्राउंड**  
प्रत्येक मॉडल के पास मॉडल का परीक्षण करने के लिए एक समर्पित प्लेग्राउंड है [Azure AI Playground](https://aka.ms/try-phi3)।

### GitHub मॉडल्स पर Phi

आप सीख सकते हैं कि Microsoft Phi का कैसे उपयोग करें और अपने विभिन्न हार्डवेयर उपकरणों में E2E समाधान कैसे बनाएं। खुद Phi का अनुभव करने के लिए, मॉडल के साथ खेलना शुरू करें और Phi को अपनी स्थिति के अनुसार अनुकूलित करें, [GitHub मॉडल कैटलॉग](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) का उपयोग करके। आप [GitHub मॉडल कैटलॉग](/md/02.QuickStart/GitHubModel_QuickStart.md) के साथ शुरुआत करने के बारे में अधिक जान सकते हैं।

**प्लेग्राउंड**  
प्रत्येक मॉडल के पास मॉडल का परीक्षण करने के लिए एक समर्पित [प्लेग्राउंड](/md/02.QuickStart/GitHubModel_QuickStart.md) है।

### Hugging Face पर Phi

आप मॉडल को [Hugging Face](https://huggingface.co/microsoft) पर भी पा सकते हैं।

**प्लेग्राउंड**  
[Hugging Chat प्लेग्राउंड](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 अन्य पाठ्यक्रम

हमारी टीम अन्य पाठ्यक्रम भी बनाती है! देखें:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain  
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)  
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / एजेंट्स  
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### जनरेटिव AI सीरीज  
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### कोर लर्निंग  
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)  
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Copilot सीरीज  
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## जिम्मेदार AI

Microsoft अपने ग्राहकों को हमारे AI उत्पादों का जिम्मेदारी से उपयोग करने में मदद करने के लिए प्रतिबद्ध है, हमारे अनुभव साझा करता है, और पारदर्शिता नोट्स और प्रभाव आकलनों जैसे उपकरणों के माध्यम से भरोसेमंद साझेदारी बनाता है। इन संसाधनों में से कई को आप [https://aka.ms/RAI](https://aka.ms/RAI) पर पा सकते हैं।  
Microsoft का जिम्मेदार AI के प्रति दृष्टिकोण हमारे AI सिद्धांतों पर आधारित है: निष्पक्षता, विश्वसनीयता और सुरक्षा, गोपनीयता और सुरक्षा, समावेशन, पारदर्शिता, और जवाबदेही।

बड़े पैमाने पर प्राकृतिक भाषा, छवि, और भाषण मॉडल — जैसे इस उदाहरण में उपयोग किए गए मॉडल — ऐसे व्यवहार कर सकते हैं जो अनुचित, अप्रत्याशित, या अपमानजनक हो सकते हैं, जिससे नुकसान हो सकता है। कृपया जोखिम और सीमाओं के बारे में सूचित होने के लिए [Azure OpenAI सेवा पारदर्शिता नोट](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) देखें।

इन जोखिमों को कम करने की अनुशंसित विधि यह है कि आपके आर्किटेक्चर में एक सुरक्षा प्रणाली शामिल हो जो हानिकारक व्यवहार का पता लगा सके और रोक सके। [Azure AI कंटेंट सुरक्षा](https://learn.microsoft.com/azure/ai-services/content-safety/overview) एक स्वतंत्र सुरक्षा परत प्रदान करता है, जो अनुप्रयोगों और सेवाओं में हानिकारक उपयोगकर्ता-जनित और AI-जनित सामग्री का पता लगा सकता है। Azure AI कंटेंट सुरक्षा में टेक्स्ट और छवि API शामिल हैं जो आपको हानिकारक सामग्री का पता लगाने की अनुमति देते हैं। Azure AI Foundry के भीतर, कंटेंट सुरक्षा सेवा विभिन्न प्रकार के माध्यमों में हानिकारक सामग्री का पता लगाने के लिए नमूना कोड देखने, एक्सप्लोर करने और आज़माने की सुविधा प्रदान करती है। निम्नलिखित [त्वरित प्रारंभ दस्तावेज़](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) आपको सेवा को अनुरोध भेजने के लिए मार्गदर्शन करता है।

एक अन्य पहलू जो ध्यान में रखना आवश्यक है वह है समग्र अनुप्रयोग प्रदर्शन। मल्टी-मॉडल और मल्टी-मॉडल्स अनुप्रयोगों के साथ, हम प्रदर्शन को इस रूप में लेते हैं कि सिस्टम आपकी और आपके उपयोगकर्ताओं की अपेक्षा के अनुसार कार्य करे, जिसमें हानिकारक आउटपुट न उत्पन्न करना भी शामिल है। अपने पूरे अनुप्रयोग के प्रदर्शन का मूल्यांकन करना महत्वपूर्ण है, [प्रदर्शन और गुणवत्ता तथा जोखिम और सुरक्षा मूल्यांकनों](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) का उपयोग करके। आपके पास [कस्टम मूल्यांकों](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) के साथ निर्माण और मूल्यांकन करने की भी क्षमता है।
आप अपने विकास वातावरण में [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) का उपयोग करके अपने AI एप्लिकेशन का मूल्यांकन कर सकते हैं। एक परीक्षण डेटासेट या लक्ष्य में से किसी एक के आधार पर, आपके जेनेरेटिव AI एप्लिकेशन की पीढ़ियों को अंतर्निर्मित मूल्याकनों या आपकी पसंद के कस्टम मूल्याकनों के साथ मात्रात्मक रूप से मापा जाता है। अपने सिस्टम का मूल्यांकन करने के लिए azure ai evaluation sdk के साथ शुरुआत करने के लिए, आप [त्वरित प्रारंभ गाइड](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) का पालन कर सकते हैं। एक बार जब आप मूल्यांकन रन निष्पादित कर लेते हैं, तो आप परिणामों को [Azure AI Foundry में विज़ुअलाइज़](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) कर सकते हैं।

## ट्रेडमार्क्स

इस परियोजना में परियोजनाओं, उत्पादों, या सेवाओं के लिए ट्रेडमार्क या लोगो हो सकते हैं। Microsoft ट्रेडमार्क या लोगो के अधिकृत उपयोग के लिए [Microsoft के ट्रेडमार्क और ब्रांड दिशा-निर्देश](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) का पालन करना आवश्यक है। इस परियोजना के संशोधित संस्करणों में Microsoft ट्रेडमार्क या लोगो के उपयोग से भ्रम नहीं होना चाहिए या Microsoft के प्रायोजन का संकेत नहीं देना चाहिए। किसी तीसरे पक्ष के ट्रेडमार्क या लोगो के उपयोग के लिए उन तीसरे पक्ष की नीतियां लागू होती हैं।

## सहायता प्राप्त करना

यदि आप फंस गए हैं या AI ऐप्स बनाने के बारे में कोई प्रश्न हैं, तो जुड़ें:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

यदि आपके पास उत्पाद प्रतिक्रिया या निर्माण के दौरान त्रुटियां हैं तो जाएं:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया सावधान रहें कि स्वचालित अनुवादों में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल भाषा में मूल दस्तावेज़ को अधिकारप्राप्त स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->