<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4987daf30687ad3850757c9eae3f5411",
  "translation_date": "2025-10-17T10:13:46+00:00",
  "source_file": "README.md",
  "language_code": "hi"
}
-->
# Phi कुकबुक: Microsoft के Phi मॉडल के साथ व्यावहारिक उदाहरण

Phi Microsoft द्वारा विकसित ओपन सोर्स AI मॉडल की एक श्रृंखला है।

Phi वर्तमान में सबसे शक्तिशाली और किफायती छोटे भाषा मॉडल (SLM) है, जो बहुभाषा, तर्क, टेक्स्ट/चैट जनरेशन, कोडिंग, इमेज, ऑडियो और अन्य परिदृश्यों में बहुत अच्छे बेंचमार्क प्रदान करता है।

आप Phi को क्लाउड या एज डिवाइस पर तैनात कर सकते हैं, और सीमित कंप्यूटिंग पावर के साथ आसानी से जनरेटिव AI एप्लिकेशन बना सकते हैं।

इन संसाधनों का उपयोग शुरू करने के लिए इन चरणों का पालन करें:
1. **रिपॉजिटरी को फोर्क करें**: क्लिक करें [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **रिपॉजिटरी को क्लोन करें**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord समुदाय में शामिल हों और विशेषज्ञों और अन्य डेवलपर्स से मिलें**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 बहुभाषी समर्थन

#### GitHub Action के माध्यम से समर्थित (स्वचालित और हमेशा अद्यतन)

[अरबी](../ar/README.md) | [बंगाली](../bn/README.md) | [बुल्गेरियन](../bg/README.md) | [बर्मी (म्यांमार)](../my/README.md) | [चीनी (सरलीकृत)](../zh/README.md) | [चीनी (पारंपरिक, हांगकांग)](../hk/README.md) | [चीनी (पारंपरिक, मकाऊ)](../mo/README.md) | [चीनी (पारंपरिक, ताइवान)](../tw/README.md) | [क्रोएशियन](../hr/README.md) | [चेक](../cs/README.md) | [डेनिश](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियन](../et/README.md) | [फिनिश](../fi/README.md) | [फ्रेंच](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिंदी](./README.md) | [हंगेरियन](../hu/README.md) | [इंडोनेशियन](../id/README.md) | [इतालवी](../it/README.md) | [जापानी](../ja/README.md) | [कोरियाई](../ko/README.md) | [लिथुआनियन](../lt/README.md) | [मलय](../ms/README.md) | [मराठी](../mr/README.md) | [नेपाली](../ne/README.md) | [नॉर्वेजियन](../no/README.md) | [फारसी (फारसी)](../fa/README.md) | [पोलिश](../pl/README.md) | [पुर्तगाली (ब्राज़ील)](../br/README.md) | [पुर्तगाली (पुर्तगाल)](../pt/README.md) | [पंजाबी (गुरुमुखी)](../pa/README.md) | [रोमानियन](../ro/README.md) | [रूसी](../ru/README.md) | [सर्बियन (सिरिलिक)](../sr/README.md) | [स्लोवाक](../sk/README.md) | [स्लोवेनियन](../sl/README.md) | [स्पेनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिश](../sv/README.md) | [टागालोग (फिलिपिनो)](../tl/README.md) | [तमिल](../ta/README.md) | [थाई](../th/README.md) | [तुर्की](../tr/README.md) | [यूक्रेनी](../uk/README.md) | [उर्दू](../ur/README.md) | [वियतनामी](../vi/README.md)

## सामग्री की सूची

- परिचय
  - [Phi परिवार में आपका स्वागत है](./md/01.Introduction/01/01.PhiFamily.md)
  - [अपने वातावरण को सेटअप करना](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [मुख्य तकनीकों को समझना](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi मॉडल के लिए AI सुरक्षा](./md/01.Introduction/01/01.AISafety.md)
  - [Phi हार्डवेयर समर्थन](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi मॉडल और प्लेटफार्मों पर उपलब्धता](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai और Phi का उपयोग करना](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub मार्केटप्लेस मॉडल](https://github.com/marketplace/models)
  - [Azure AI मॉडल कैटलॉग](https://ai.azure.com)

- विभिन्न वातावरण में Phi का इनफेरेंस
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [GitHub मॉडल](./md/01.Introduction/02/02.GitHubModel.md)
    - [Azure AI Foundry मॉडल कैटलॉग](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi परिवार का इनफेरेंस
    - [iOS में Phi का इनफेरेंस](./md/01.Introduction/03/iOS_Inference.md)
    - [Android में Phi का इनफेरेंस](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson में Phi का इनफेरेंस](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC में Phi का इनफेरेंस](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework के साथ Phi का इनफेरेंस](./md/01.Introduction/03/MLX_Inference.md)
    - [लोकल सर्वर में Phi का इनफेरेंस](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit का उपयोग करके रिमोट सर्वर में Phi का इनफेरेंस](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust के साथ Phi का इनफेरेंस](./md/01.Introduction/03/Rust_Inference.md)
    - [लोकल में Phi--Vision का इनफेरेंस](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers (आधिकारिक समर्थन) के साथ Phi का इनफेरेंस](./md/01.Introduction/03/Kaito_Inference.md)

- [Phi परिवार को क्वांटिफाई करना](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp का उपयोग करके Phi-3.5 / 4 को क्वांटिफाई करना](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime के लिए जनरेटिव AI एक्सटेंशन का उपयोग करके Phi-3.5 / 4 को क्वांटिफाई करना](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO का उपयोग करके Phi-3.5 / 4 को क्वांटिफाई करना](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework का उपयोग करके Phi-3.5 / 4 को क्वांटिफाई करना](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi का मूल्यांकन
    - [उत्तरदायी AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [मूल्यांकन के लिए Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [मूल्यांकन के लिए Promptflow का उपयोग करना](./md/01.Introduction/05/Promptflow.md)

- Azure AI Search के साथ RAG
    - [Azure AI Search के साथ Phi-4-mini और Phi-4-multimodal (RAG) का उपयोग कैसे करें](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi एप्लिकेशन विकास के नमूने
  - टेक्स्ट और चैट एप्लिकेशन
    - Phi-4 नमूने 🆕
      - [📓] [Phi-4-mini ONNX मॉडल के साथ चैट करें](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 लोकल ONNX मॉडल .NET के साथ चैट करें](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Phi-4 ONNX का उपयोग करके .NET कंसोल ऐप में चैट करें (सिमेंटिक कर्नेल के साथ)](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 नमूने
      - [ब्राउज़र में लोकल चैटबॉट, Phi3, ONNX Runtime Web और WebGPU का उपयोग करके](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino चैट](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [मल्टी मॉडल - इंटरएक्टिव Phi-3-mini और OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - एक रैपर बनाना और MLFlow के साथ Phi-3 का उपयोग करना](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [मॉडल ऑप्टिमाइजेशन - ONNX Runtime Web के लिए Phi-3-min मॉडल को Olive के साथ ऑप्टिमाइज़ कैसे करें](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [WinUI3 ऐप Phi-3 mini-4k-instruct-onnx के साथ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [WinUI3 मल्टी मॉडल AI पावर्ड नोट्स ऐप सैंपल](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [कस्टम Phi-3 मॉडल्स को फाइन-ट्यून और प्रॉम्प्ट फ्लो के साथ इंटीग्रेट करें](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Azure AI Foundry में प्रॉम्प्ट फ्लो के साथ कस्टम Phi-3 मॉडल्स को फाइन-ट्यून और इंटीग्रेट करें](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Microsoft के जिम्मेदार AI सिद्धांतों पर ध्यान केंद्रित करते हुए Azure AI Foundry में फाइन-ट्यून किए गए Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करें](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct भाषा भविष्यवाणी सैंपल (चीनी/अंग्रेज़ी)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG चैटबॉट](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU का उपयोग करके Phi-3.5-Instruct ONNX के साथ प्रॉम्प्ट फ्लो समाधान बनाएं](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tflite का उपयोग करके Android ऐप बनाएं](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Microsoft.ML.OnnxRuntime का उपयोग करके स्थानीय ONNX Phi-3 मॉडल के साथ Q&A .NET उदाहरण](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Semantic Kernel और Phi-3 के साथ कंसोल चैट .NET ऐप](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK कोड आधारित सैंपल्स  
  - Phi-4 सैंपल्स 🆕  
    - [📓] [Phi-4-multimodal का उपयोग करके प्रोजेक्ट कोड जनरेट करें](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Phi-3 / 3.5 सैंपल्स  
    - [Microsoft Phi-3 फैमिली के साथ अपना खुद का Visual Studio Code GitHub Copilot चैट बनाएं](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [GitHub मॉडल्स के साथ Phi-3.5 का उपयोग करके अपना खुद का Visual Studio Code चैट Copilot एजेंट बनाएं](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- उन्नत तर्क सैंपल्स  
  - Phi-4 सैंपल्स 🆕  
    - [📓] [Phi-4-mini-reasoning या Phi-4-reasoning सैंपल्स](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Microsoft Olive के साथ Phi-4-mini-reasoning को फाइन-ट्यून करना](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Apple MLX के साथ Phi-4-mini-reasoning को फाइन-ट्यून करना](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [GitHub मॉडल्स के साथ Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Azure AI Foundry मॉडल्स के साथ Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- डेमो  
    - [Hugging Face Spaces पर होस्ट किए गए Phi-4-mini डेमो](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Hugging Face Spaces पर होस्ट किए गए Phi-4-multimodal डेमो](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- विज़न सैंपल्स  
  - Phi-4 सैंपल्स 🆕  
    - [📓] [Phi-4-multimodal का उपयोग करके इमेज पढ़ें और कोड जनरेट करें](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Phi-3 / 3.5 सैंपल्स  
    - [📓][Phi-3-vision-इमेज टेक्स्ट से टेक्स्ट](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP एम्बेडिंग](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [DEMO: Phi-3 रीसाइक्लिंग](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - विजुअल लैंग्वेज असिस्टेंट - Phi3-Vision और OpenVINO के साथ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision मल्टी-फ्रेम या मल्टी-इमेज सैंपल](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Microsoft.ML.OnnxRuntime .NET का उपयोग करके स्थानीय ONNX मॉडल के साथ Phi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Microsoft.ML.OnnxRuntime .NET का उपयोग करके मेनू आधारित Phi-3 Vision स्थानीय ONNX मॉडल](../../md/04.HOL/dotnet/src/LabsPhi304)  

- गणित सैंपल्स  
  - Phi-4-Mini-Flash-Reasoning-Instruct सैंपल्स 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct के साथ गणित डेमो](../../md/02.Application/09.Math/MathDemo.ipynb)  

- ऑडियो सैंपल्स  
  - Phi-4 सैंपल्स 🆕  
    - [📓] [Phi-4-multimodal का उपयोग करके ऑडियो ट्रांसक्रिप्ट्स निकालना](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Phi-4-multimodal ऑडियो सैंपल](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Phi-4-multimodal स्पीच ट्रांसलेशन सैंपल](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [.NET कंसोल एप्लिकेशन का उपयोग करके Phi-4-multimodal ऑडियो से ऑडियो फ़ाइल का विश्लेषण करें और ट्रांसक्रिप्ट जनरेट करें](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- MOE सैंपल्स  
  - Phi-3 / 3.5 सैंपल्स  
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) सोशल मीडिया सैंपल](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, और LlamaIndex के साथ Retrieval-Augmented Generation (RAG) पाइपलाइन बनाना](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- फंक्शन कॉलिंग सैंपल्स  
  - Phi-4 सैंपल्स 🆕  
    - [📓] [Phi-4-mini के साथ फंक्शन कॉलिंग का उपयोग करना](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Phi-4-mini के साथ मल्टी-एजेंट्स बनाने के लिए फंक्शन कॉलिंग का उपयोग करना](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Ollama के साथ फंक्शन कॉलिंग का उपयोग करना](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [ONNX के साथ फंक्शन कॉलिंग का उपयोग करना](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- मल्टीमॉडल मिक्सिंग सैंपल्स  
  - Phi-4 सैंपल्स 🆕  
    - [📓] [Phi-4-multimodal का उपयोग करके एक टेक्नोलॉजी पत्रकार के रूप में काम करना](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [.NET कंसोल एप्लिकेशन का उपयोग करके Phi-4-multimodal के साथ इमेज का विश्लेषण करें](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Phi सैंपल्स का फाइन-ट्यूनिंग  
  - [फाइन-ट्यूनिंग परिदृश्य](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [फाइन-ट्यूनिंग बनाम RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Phi-3 को एक इंडस्ट्री एक्सपर्ट बनने दें](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [VS Code के लिए AI टूलकिट के साथ Phi-3 को फाइन-ट्यून करना](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Azure Machine Learning Service के साथ Phi-3 को फाइन-ट्यून करना](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Lora के साथ Phi-3 को फाइन-ट्यून करना](./md/03.FineTuning/FineTuning_Lora.md)  
  - [QLora के साथ Phi-3 को फाइन-ट्यून करना](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Azure AI Foundry के साथ Phi-3 को फाइन-ट्यून करना](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Azure ML CLI/SDK के साथ Phi-3 को फाइन-ट्यून करना](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Microsoft Olive के साथ फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Microsoft Olive हैंड्स-ऑन लैब के साथ फाइन-ट्यूनिंग](./md/03.FineTuning/olive-lab/readme.md)  
  - [Weights and Bias के साथ Phi-3-vision को फाइन-ट्यून करना](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Apple MLX फ्रेमवर्क के साथ Phi-3 को फाइन-ट्यून करना](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Phi-3-vision को फाइन-ट्यून करना (आधिकारिक समर्थन)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Kaito AKS, Azure Containers के साथ Phi-3 को फाइन-ट्यून करना (आधिकारिक समर्थन)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Phi-3 और 3.5 Vision को फाइन-ट्यून करना](https://github.com/2U1/Phi3-Vision-Finetune)  

- हैंड्स ऑन लैब  
  - [कटिंग-एज मॉडल्स का अन्वेषण: LLMs, SLMs, स्थानीय विकास और अधिक](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [NLP क्षमता को अनलॉक करना: Microsoft Olive के साथ फाइन-ट्यूनिंग](https://github.com/azure/Ignite_FineTuning_workshop)  

- शैक्षणिक शोध पत्र और प्रकाशन  
  - [Textbooks Are All You Need II: phi-1.5 तकनीकी रिपोर्ट](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 तकनीकी रिपोर्ट: एक अत्यधिक सक्षम भाषा मॉडल जो आपके फोन पर चलता है](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 तकनीकी रिपोर्ट](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini तकनीकी रिपोर्ट: Mixture-of-LoRAs के माध्यम से कॉम्पैक्ट लेकिन शक्तिशाली मल्टीमॉडल भाषा मॉडल्स](https://arxiv.org/abs/2503.01743)  
  - [इन-व्हीकल फंक्शन-कॉलिंग के लिए छोटे भाषा मॉडल को ऑप्टिमाइज़ करना](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 को मल्टीपल-चॉइस प्रश्न उत्तर देने के लिए फाइन-ट्यून करना: पद्धति, परिणाम, और चुनौतियां](https://arxiv.org/abs/2501.01588)
  - [Phi-4-रीज़निंग तकनीकी रिपोर्ट](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-मिनी-रीज़निंग तकनीकी रिपोर्ट](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi मॉडल का उपयोग करना

### Azure AI Foundry पर Phi

आप Microsoft Phi का उपयोग करना और अपने विभिन्न हार्डवेयर उपकरणों में E2E समाधान बनाना सीख सकते हैं। Phi का अनुभव करने के लिए, मॉडल के साथ खेलना शुरू करें और अपने परिदृश्यों के लिए Phi को कस्टमाइज़ करें। [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) पर जाकर आप अधिक जानकारी प्राप्त कर सकते हैं। [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) के साथ शुरुआत करने के लिए यहां देखें।

**प्लेग्राउंड**
प्रत्येक मॉडल के पास मॉडल को टेस्ट करने के लिए एक समर्पित प्लेग्राउंड है [Azure AI Playground](https://aka.ms/try-phi3)।

### GitHub मॉडल पर Phi

आप Microsoft Phi का उपयोग करना और अपने विभिन्न हार्डवेयर उपकरणों में E2E समाधान बनाना सीख सकते हैं। Phi का अनुभव करने के लिए, मॉडल के साथ खेलना शुरू करें और अपने परिदृश्यों के लिए Phi को कस्टमाइज़ करें। [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) पर जाकर आप अधिक जानकारी प्राप्त कर सकते हैं। [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) के साथ शुरुआत करने के लिए यहां देखें।

**प्लेग्राउंड**
प्रत्येक मॉडल के पास [मॉडल को टेस्ट करने के लिए एक समर्पित प्लेग्राउंड](/md/02.QuickStart/GitHubModel_QuickStart.md) है।

### Hugging Face पर Phi

आप मॉडल को [Hugging Face](https://huggingface.co/microsoft) पर भी पा सकते हैं।

**प्लेग्राउंड**
 [Hugging Chat प्लेग्राउंड](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## जिम्मेदार AI 

Microsoft अपने ग्राहकों को हमारे AI उत्पादों का जिम्मेदारी से उपयोग करने में मदद करने, हमारे अनुभव साझा करने, और विश्वास-आधारित साझेदारी बनाने के लिए प्रतिबद्ध है। यह उपकरण जैसे Transparency Notes और Impact Assessments के माध्यम से किया जाता है। इनमें से कई संसाधन [https://aka.ms/RAI](https://aka.ms/RAI) पर पाए जा सकते हैं। Microsoft का जिम्मेदार AI के प्रति दृष्टिकोण हमारे AI सिद्धांतों पर आधारित है: निष्पक्षता, विश्वसनीयता और सुरक्षा, गोपनीयता और सुरक्षा, समावेशिता, पारदर्शिता, और जवाबदेही।

बड़े पैमाने पर प्राकृतिक भाषा, छवि, और भाषण मॉडल - जैसे इस नमूने में उपयोग किए गए - संभावित रूप से अनुचित, अविश्वसनीय, या आपत्तिजनक तरीके से व्यवहार कर सकते हैं, जिससे नुकसान हो सकता है। कृपया [Azure OpenAI सेवा Transparency नोट](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) को पढ़ें ताकि जोखिम और सीमाओं के बारे में जानकारी प्राप्त हो सके।

इन जोखिमों को कम करने के लिए अनुशंसित दृष्टिकोण यह है कि आपकी आर्किटेक्चर में एक सुरक्षा प्रणाली शामिल हो जो हानिकारक व्यवहार का पता लगा सके और उसे रोक सके। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) एक स्वतंत्र सुरक्षा परत प्रदान करता है, जो उपयोगकर्ता-जनित और AI-जनित हानिकारक सामग्री का पता लगाने में सक्षम है। Azure AI Content Safety में टेक्स्ट और इमेज API शामिल हैं जो हानिकारक सामग्री का पता लगाने की अनुमति देते हैं। Azure AI Foundry के भीतर, Content Safety सेवा आपको विभिन्न मोडालिटी में हानिकारक सामग्री का पता लगाने के लिए नमूना कोड देखने, एक्सप्लोर करने और आज़माने की अनुमति देती है। निम्नलिखित [क्विकस्टार्ट दस्तावेज़](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) आपको सेवा के लिए अनुरोध करने के माध्यम से मार्गदर्शन करता है।

एक अन्य पहलू जिसे ध्यान में रखना चाहिए वह है समग्र एप्लिकेशन प्रदर्शन। मल्टी-मोडल और मल्टी-मॉडल एप्लिकेशन के साथ, हम प्रदर्शन को यह मानते हैं कि सिस्टम आपके और आपके उपयोगकर्ताओं की अपेक्षाओं के अनुसार कार्य करता है, जिसमें हानिकारक आउटपुट उत्पन्न न करना शामिल है। आपके समग्र एप्लिकेशन के प्रदर्शन का आकलन करना महत्वपूर्ण है [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) का उपयोग करके। आपके पास [कस्टम इवैलुएटर्स](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) बनाने और उनका मूल्यांकन करने की क्षमता भी है।

आप अपने विकास पर्यावरण में [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) का उपयोग करके अपने AI एप्लिकेशन का मूल्यांकन कर सकते हैं। दिए गए परीक्षण डेटा सेट या लक्ष्य के साथ, आपके जनरेटिव AI एप्लिकेशन जनरेशन को आपके द्वारा चुने गए बिल्ट-इन इवैलुएटर्स या कस्टम इवैलुएटर्स के साथ मात्रात्मक रूप से मापा जाता है। Azure AI Evaluation SDK के साथ अपने सिस्टम का मूल्यांकन शुरू करने के लिए, आप [क्विकस्टार्ट गाइड](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) का अनुसरण कर सकते हैं। एक बार जब आप मूल्यांकन रन निष्पादित करते हैं, तो आप [Azure AI Foundry में परिणामों को विज़ुअलाइज़ कर सकते हैं](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)। 

## ट्रेडमार्क

इस प्रोजेक्ट में प्रोजेक्ट्स, उत्पादों, या सेवाओं के लिए ट्रेडमार्क या लोगो हो सकते हैं। Microsoft ट्रेडमार्क या लोगो के अधिकृत उपयोग को [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) का पालन करना चाहिए। 
Microsoft ट्रेडमार्क या लोगो का उपयोग संशोधित संस्करणों में भ्रम पैदा नहीं करना चाहिए या Microsoft प्रायोजन का संकेत नहीं देना चाहिए। किसी भी तृतीय-पक्ष ट्रेडमार्क या लोगो का उपयोग उन तृतीय-पक्ष की नीतियों के अधीन है।

## सहायता प्राप्त करना

यदि आप अटक जाते हैं या AI ऐप्स बनाने के बारे में कोई प्रश्न हैं, तो शामिल हों:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

यदि आपको उत्पाद प्रतिक्रिया या निर्माण के दौरान त्रुटियां मिलती हैं, तो यहां जाएं:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।