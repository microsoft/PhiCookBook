# फाई कुकबुक: माइक्रोसॉफ्ट के फाई मॉडल्स के साथ हाथों-हाथ उदाहरण

[![GitHub Codespaces में सैंपल खोलें और उपयोग करें](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers में खोलें](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub योगदानकर्ताओं](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub मुद्दे](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub पुल अनुरोध](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![पीआर स्वागत योग्य](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub वॉचर्स](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub स्टार्स](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

फाई माइक्रोसॉफ्ट द्वारा विकसित एक श्रृंखला है खुला स्रोत AI मॉडल्स की।

फाई वर्तमान में सबसे शक्तिशाली और लागत-कुशल छोटा भाषा मॉडल (SLM) है, जो बहुभाषी, तर्क, टेक्स्ट/चैट जेनरेशन, कोडिंग, चित्र, ऑडियो और अन्य परिदृश्यों में बहुत अच्छे बेंचमार्क प्रदर्शित करता है।

आप फाई को क्लाउड पर या एज डिवाइसेज़ पर डिप्लॉय कर सकते हैं, और सीमित कंप्यूटिंग पावर के साथ आसानी से जनरेटिव AI एप्लिकेशन बना सकते हैं।

शुरू करने के लिए इन चरणों का पालन करें:
1. **रिपॉजिटरी को फोर्क करें**: क्लिक करें [![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **रिपॉजिटरी क्लोन करें**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI डिस्कॉर्ड समुदाय में शामिल हों और विशेषज्ञों तथा अन्य डेवलपर्स से मिलें**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/hi/cover.eb18d1b9605d754b.webp)

### 🌐 बहुभाषी सहायता

#### GitHub Action के माध्यम से समर्थित (स्वचालित और हमेशा अपडेटेड)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](./README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **स्थानीय रूप से क्लोन करना पसंद करते हैं?**
>
> यह रिपॉजिटरी 50+ भाषा अनुवाद शामिल करता है जो डाउनलोड आकार को काफी बढ़ाता है। अनुवाद के बिना क्लोन करने के लिए स्पार्स चेकआउट का उपयोग करें:
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
> इससे आपको तेजी से डाउनलोड के साथ कोर्स पूरा करने के लिए आवश्यक सब कुछ मिल जाएगा।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## सामग्री तालिका
- परिचय - [Phi परिवार में आपका स्वागत है](./md/01.Introduction/01/01.PhiFamily.md) - [अपने पर्यावरण को सेटअप करना](./md/01.Introduction/01/01.EnvironmentSetup.md) - [प्रमुख प्रौद्योगिकियों को समझना](./md/01.Introduction/01/01.Understandingtech.md) - [Phi मॉडलों के लिए AI सुरक्षा](./md/01.Introduction/01/01.AISafety.md) - [Phi हार्डवेयर समर्थन](./md/01.Introduction/01/01.Hardwaresupport.md) - [Phi मॉडल और प्लेटफार्मों पर उपलब्धता](./md/01.Introduction/01/01.Edgeandcloud.md) - [Guidance-ai और Phi का उपयोग](./md/01.Introduction/01/01.Guidance.md) - [GitHub मार्केटप्लेस मॉडल्स](https://github.com/marketplace/models) - [Azure AI मॉडल सूची](https://ai.azure.com) - विभिन्न पर्यावरण में Phi की व्याख्या - [Hugging face](./md/01.Introduction/02/01.HF.md) - [GitHub मॉडल्स](./md/01.Introduction/02/02.GitHubModel.md) - [Microsoft Foundry मॉडल सूची](./md/01.Introduction/02/03.AzureAIFoundry.md) - [Ollama](./md/01.Introduction/02/04.Ollama.md) - [AI टूलकिट VSCode (AITK)](./md/01.Introduction/02/05.AITK.md) - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md) - [Foundry स्थानीय](./md/01.Introduction/02/07.FoundryLocal.md) - Phi परिवार में व्याख्या - [iOS में Phi व्याख्या](./md/01.Introduction/03/iOS_Inference.md) - [Android में Phi व्याख्या](./md/01.Introduction/03/Android_Inference.md) - [Jetson में Phi व्याख्या](./md/01.Introduction/03/Jetson_Inference.md) - [AI पीसी में Phi व्याख्या](./md/01.Introduction/03/AIPC_Inference.md) - [Apple MLX फ्रेमवर्क के साथ Phi व्याख्या](./md/01.Introduction/03/MLX_Inference.md) - [स्थानीय सर्वर में Phi व्याख्या](./md/01.Introduction/03/Local_Server_Inference.md) - [AI टूलकिट का उपयोग करके दूरस्थ सर्वर में Phi व्याख्या](./md/01.Introduction/03/Remote_Interence.md) - [Rust के साथ Phi व्याख्या](./md/01.Introduction/03/Rust_Inference.md) - [स्थानीय में Phi--Vision व्याख्या](./md/01.Introduction/03/Vision_Inference.md) - [Kaito AKS, Azure कंटेनरों (आधिकारिक समर्थन) के साथ Phi व्याख्या](./md/01.Introduction/03/Kaito_Inference.md) - [Phi परिवार का मात्रांकन](./md/01.Introduction/04/QuantifyingPhi.md) - [llama.cpp का उपयोग कर Phi-3.5 / 4 को मात्रा में परिवर्तित करना](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md) - [onnxruntime के लिए जनरेटिव AI विस्तारों का उपयोग कर Phi-3.5 / 4 को मात्रा में परिवर्तित करना](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md) - [Intel OpenVINO का उपयोग कर Phi-3.5 / 4 को मात्रा में परिवर्तित करना](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md) - [Apple MLX फ्रेमवर्क का उपयोग कर Phi-3.5 / 4 को मात्रा में परिवर्तित करना](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md) - Phi का मूल्यांकन - [जिम्मेदार AI](./md/01.Introduction/05/ResponsibleAI.md) - [मूल्यांकन के लिए Microsoft Foundry](./md/01.Introduction/05/AIFoundry.md) - [मूल्यांकन के लिए Promptflow का उपयोग](./md/01.Introduction/05/Promptflow.md) - Azure AI Search के साथ RAG - [Azure AI Search के साथ Phi-4-mini और Phi-4-multimodal (RAG) का उपयोग कैसे करें](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb) - Phi एप्लिकेशन विकास नमूने - टेक्स्ट और चैट एप्लिकेशन - Phi-4 नमूने - [📓] [Phi-4-mini ONNX मॉडल के साथ चैट करें](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md) - [स्थानीय ONNX मॉडल .NET के साथ Phi-4 चैट करें](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) - [Sementic Kernel का उपयोग कर Phi-4 ONNX के साथ .NET कंसोल चैट ऐप](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) - Phi-3 / 3.5 नमूने - [Phi3, ONNX Runtime Web और WebGPU का उपयोग कर ब्राउज़र में स्थानीय चैटबोट](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat) - [OpenVino चैट](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md) - [मल्टी मॉडल - इंटरैक्टिव Phi-3-mini और OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md) - [MLFlow - एक रैपर बनाना और Phi-3 के साथ MLFlow का उपयोग](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md) - [मॉडल अनुकूलन - Olive के साथ ONNX Runtime Web के लिए Phi-3-min मॉडल को अनुकूलित कैसे करें](https://github.com/microsoft/Olive/tree/main/examples/phi3) - [WinUI3 ऐप Phi-3 mini-4k-instruct-onnx के साथ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/) -[WinUI3 मल्टी मॉडल AI संचालित नोट्स ऐप नमूना](https://github.com/microsoft/ai-powered-notes-winui3-sample) - [परिमार्जित और कस्टम Phi-3 मॉडलों को Prompt flow के साथ एकीकृत करें](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md) - [Microsoft Foundry में Prompt flow के साथ कस्टम Phi-3 मॉडलों को परिमार्जित और एकीकृत करें](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md) - [Microsoft की जिम्मेदार AI नीतियों पर ध्यान केंद्रित करते हुए Microsoft Foundry में परिमार्जित Phi-3 / Phi-3.5 मॉडल का मूल्यांकन करें](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md) - [📓] [Phi-3.5-mini-instruct भाषा भविष्यवाणी नमूना (चीनी/अंग्रेजी)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb) - [Phi-3.5-Instruct WebGPU RAG चैटबोट](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md) - [Phi-3.5-Instruct ONNX के साथ विंडोज GPU का उपयोग कर Prompt flow समाधान बनाना](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md) - [एंड्रॉइड ऐप बनाने के लिए Microsoft Phi-3.5 tflite का उपयोग](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md) - [Microsoft.ML.OnnxRuntime का उपयोग कर स्थानीय ONNX Phi-3 मॉडल के साथ Q&A .NET उदाहरण](../../md/04.HOL/dotnet/src/LabsPhi301) - [Semantic Kernel और Phi-3 के साथ कंसोल चैट .NET ऐप](../../md/04.HOL/dotnet/src/LabsPhi302) - Azure AI Inference SDK कोड आधारित नमूने - Phi-4 नमूने - [📓] [Phi-4-multimodal का उपयोग कर परियोजना कोड उत्पन्न करें](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md) - Phi-3 / 3.5 नमूने - [Microsoft Phi-3 परिवार के साथ अपना Visual Studio Code GitHub Copilot चैट बनाएं](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md) - [GitHub मॉडल्स द्वारा Phi-3.5 के साथ अपना Visual Studio Code चैट कॉपिलट एजेंट बनाएं](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md) - उन्नत तर्क नमूने - Phi-4 नमूने - [📓] [Phi-4-mini-reasoning या Phi-4-reasoning नमूने](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md) - [📓] [Microsoft Olive के साथ Phi-4-mini-reasoning का परिमार्जन](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Apple MLX के साथ Phi-4-mini-reasoning का परिमार्जन](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [GitHub मॉडलों के साथ Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb) - [📓] [Microsoft Foundry मॉडलों के साथ Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb) -
डेमो - [Phi-4-mini डेमो Hugging Face Spaces पर होस्ट किए गए](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo) - [Phi-4-multimodal डेमो Hugging Face Spaces पर होस्ट किए गए](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo) - विज़न नमूने - Phi-4 नमूने - [📓] [Phi-4-multimodal का उपयोग चित्र पढ़ने और कोड जनरेट करने के लिए](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) - Phi-3 / 3.5 नमूने - [📓][Phi-3-vision-इमेज टेक्स्ट से टेक्स्ट](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html) - [📓][Phi-3-vision CLIP एम्बेडिंग](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [डेमो: Phi-3 रीसाइक्लिंग](https://github.com/jennifermarsman/PhiRecycling/) - [Phi-3-vision - विज़ुअल लैंग्वेज असिस्टेंट - Phi3-विज़न और OpenVINO के साथ](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html) - [Phi-3 विज़न Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md) - [Phi-3 विज़न OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md) - [📓][Phi-3.5 विज़न मल्टी-फ्रेम या मल्टी-इमेज नमूना](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb) - [Phi-3 विज़न लोकल ONNX मॉडल Microsoft.ML.OnnxRuntime .NET का उपयोग करते हुए](../../md/04.HOL/dotnet/src/LabsPhi303) - [मेनू आधारित Phi-3 विज़न लोकल ONNX मॉडल Microsoft.ML.OnnxRuntime .NET का उपयोग करते हुए](../../md/04.HOL/dotnet/src/LabsPhi304) - रीज़निंग-विज़न नमूने - Phi-4-रीज़निंग-विज़न-15B - [📓] [Phi-4-रीज़निंग-विज़न-15B का उपयोग jaywalking पहचानने के लिए](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb) - [📓] [Phi-4-रीज़निंग-विज़न-15B का उपयोग गणित के लिए](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb) - [📓] [Phi-4-रीज़निंग-विज़न-15B का उपयोग UI पहचानने के लिए](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb) - गणित नमूने - Phi-4-Mini-Flash-रीज़निंग-इंस्ट्रक्ट नमूने [Phi-4-Mini-Flash-रीज़निंग-इंस्ट्रक्ट के साथ गणित डेमो](./md/02.Application/09.Math/MathDemo.ipynb) - ऑडियो नमूने - Phi-4 नमूने - [📓] [Phi-4-multimodal के उपयोग से ऑडियो ट्रांसक्रिप्ट्स निकालना](./md/02.Application/05.Audio/Phi4/Transciption/README.md) - [📓] [Phi-4-multimodal ऑडियो नमूना](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb) - [📓] [Phi-4-multimodal स्पीच ट्रांसलेशन नमूना](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb) - [.NET कंसोल एप्लिकेशन जो Phi-4-multimodal ऑडियो का उपयोग करके ऑडियो फ़ाइल का विश्लेषण करता है और ट्रांसक्रिप्ट जनरेट करता है](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) - MOE नमूने - Phi-3 / 3.5 नमूने - [📓] [Phi-3.5 मिश्र विशेषज्ञ मॉडेल्स (MoEs) सोशल मीडिया नमूना](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb) - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, और LlamaIndex के साथ रिट्रीवल-ऑगमेंटेड जनरेशन (RAG) पाइपलाइन बनाना](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb) - - फंक्शन कॉलिंग नमूने - Phi-4 नमूने 🆕 - [📓] [Phi-4-mini के साथ फंक्शन कॉलिंग का उपयोग](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md) - [📓] [Phi-4-mini के साथ मल्टी-एजेंट बनाने के लिए फंक्शन कॉलिंग का उपयोग](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb) - [📓] [Ollama के साथ फंक्शन कॉलिंग का उपयोग](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb) - [📓] [ONNX के साथ फंक्शन कॉलिंग का उपयोग](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb) - मल्टीमोडल मिक्सिंग नमूने - Phi-4 नमूने 🆕 - [📓] [Phi-4-multimodal का उपयोग टेक्नोलॉजी पत्रकार के रूप में](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb) - [.NET कंसोल एप्लिकेशन जो Phi-4-multimodal का उपयोग कर चित्रों का विश्लेषण करता है](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) - फाइन-ट्यूनिंग Phi नमूने - [फाइन-ट्यूनिंग परिदृश्य](./md/03.FineTuning/FineTuning_Scenarios.md) - [फाइन-ट्यूनिंग बनाम RAG](./md/03.FineTuning/FineTuning_vs_RAG.md) - [Phi-3 को उद्योग विशेषज्ञ बनने के लिए फाइन-ट्यूनिंग](./md/03.FineTuning/LetPhi3gotoIndustriy.md) - [VS Code के लिए AI टूलकिट के साथ Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md) - [Azure मशीन लर्निंग सेवा के साथ Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/Introduce_AzureML.md) - [Lora के साथ Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Lora.md) - [QLora के साथ Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Qlora.md) - [Microsoft Foundry के साथ Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_AIFoundry.md) - [Azure ML CLI/SDK के साथ Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLSDK.md) - [Microsoft Olive के साथ फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MicrosoftOlive.md) - [Microsoft Olive हैंड्स-ऑन लैब के साथ फाइन-ट्यूनिंग](./md/03.FineTuning/olive-lab/readme.md) - [Weights and Bias के साथ Phi-3-vision फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md) - [Apple MLX Framework के साथ Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLX.md) - [Phi-3-vision फाइन-ट्यूनिंग (आधिकारिक समर्थन)](./md/03.FineTuning/FineTuning_Vision.md) - [Kaito AKS, Azure Containers के साथ Phi-3 फाइन-ट्यूनिंग (आधिकारिक समर्थन)](./md/03.FineTuning/FineTuning_Kaito.md) - [Phi-3 और 3.5 विज़न फाइन-ट्यूनिंग](https://github.com/2U1/Phi3-Vision-Finetune) - हैंड्स ऑन लैब - [उन्नत मॉडलों का अन्वेषण: LLMs, SLMs, लोकल डेवलपमेंट और अधिक](https://github.com/microsoft/aitour-exploring-cutting-edge-models) - [NLP क्षमता खोलना: Microsoft Olive के साथ फाइन-ट्यूनिंग](https://github.com/azure/Ignite_FineTuning_workshop) - शैक्षणिक शोध पत्र और प्रकाशन - [पाठ्यपुस्तकें सर्वथा आवश्यक हैं II: phi-1.5 तकनीकी रिपोर्ट](https://arxiv.org/abs/2309.05463) - [Phi-3 तकनीकी रिपोर्ट: आपके फोन पर एक अत्यधिक सक्षम भाषा मॉडल](https://arxiv.org/abs/2404.14219) - [Phi-4 तकनीकी रिपोर्ट](https://arxiv.org/abs/2412.08905) - [Phi-4-Mini तकनीकी रिपोर्ट: मिश्र LoRAs के माध्यम से कॉम्पैक्ट लेकिन शक्तिशाली मल्टीमोडल भाषा मॉडल्स](https://arxiv.org/abs/2503.01743) - [वाहन में फंक्शन-कॉलिंग के लिए छोटे भाषा मॉडलों का अनुकूलन](https://arxiv.org/abs/2501.02342) - [(WhyPHI) बहुविकल्पीय प्रश्न उत्तर के लिए PHI-3 फाइन-ट्यूनिंग: पद्धति, परिणाम और चुनौतियां](https://arxiv.org/abs/2501.01588) - [Phi-4-रीज़निंग तकनीकी रिपोर्ट](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf) 
- [Phi-4-मिनी-तर्क तकनीकी रिपोर्ट](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)
# Phi कुकबुक: Microsoft के Phi मॉडल के साथ व्यावहारिक उदाहरण

[![GitHub कोडस्पेसेस में नमूने खोलें और उपयोग करें](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev कंटेनरों में खोलें](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub योगदानकर्ता](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub मुद्दे](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub पुल-रिक्वेस्ट](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs स्वागत है](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub वॉचर्स](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub सितारे](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry डिस्कॉर्ड](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi Microsoft द्वारा विकसित एक ओपन सोर्स AI मॉडल श्रृंखला है। 

Phi वर्तमान में सबसे शक्तिशाली और किफायती स्मॉल लैंग्वेज मॉडल (SLM) है, जो बहुभाषी, तर्क, टेक्स्ट/चैट जनरेशन, कोडिंग, छवियों, ऑडियो और अन्य परिदृश्यों में बहुत अच्छे बेंचमार्क प्रस्तुत करता है। 

आप Phi को क्लाउड या एज डिवाइसों पर तैनात कर सकते हैं, और सीमित कंप्यूटिंग शक्ति के साथ आसानी से जनरेटिव AI एप्लिकेशन बना सकते हैं।

इन संसाधनों का उपयोग शुरू करने के लिए ये कदम उठाएँ:
1. **रिपॉजिटरी को फोर्क करें**: क्लिक करें [![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **रिपॉजिटरी को क्लोन करें**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI डिस्कॉर्ड समुदाय में शामिल हों और विशेषज्ञों और अन्य डेवलपर्स से मिलें**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/hi/cover.eb18d1b9605d754b.webp)

### 🌐 बहुभाषी समर्थन

#### GitHub Action के माध्यम से समर्थित (स्वचालित और हमेशा अद्यतन)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](./README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **स्थानीय रूप से क्लोन करना पसंद है?**
>
> यह रिपॉजिटरी 50+ भाषा अनुवाद शामिल करती है जो डाउनलोड आकार को काफी बढ़ा देती है। बिना अनुवाद के क्लोन करने के लिए, sparse checkout का उपयोग करें:
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
> यह आपको बहुत तेज डाउनलोड के साथ पाठ्यक्रम पूरा करने के लिए आवश्यक सब कुछ प्रदान करता है।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## सामग्री तालिका

## Phi मॉडल का उपयोग

### Microsoft Foundry पर Phi

आप Microsoft Phi का उपयोग कैसे करें और अपने विभिन्न हार्डवेयर उपकरणों में E2E समाधान कैसे बनाएं, यह सीख सकते हैं। Phi का अनुभव पाने के लिए, मॉडल के साथ खेलना शुरू करें और अपने परिदृश्यों के लिए Phi को अनुकूलित करें [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) का उपयोग करके। आप और अधिक जान सकते हैं Getting Started with [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**प्लेटग्राउंड**  
प्रत्येक मॉडल के पास मॉडल को टेस्ट करने के लिए एक समर्पित प्लेग्राउंड है [Azure AI Playground](https://aka.ms/try-phi3)।

### GitHub मॉडल्स पर Phi

आप Microsoft Phi का उपयोग कैसे करें और अपने विभिन्न हार्डवेयर उपकरणों में E2E समाधान कैसे बनाएं, यह सीख सकते हैं। Phi का अनुभव पाने के लिए, मॉडल के साथ खेलना शुरू करें और अपने परिदृश्यों के लिए Phi को अनुकूलित करें [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) का उपयोग करके। आप और अधिक जान सकते हैं Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**प्लेटग्राउंड**  
प्रत्येक मॉडल के पास मॉडल को टेस्ट करने के लिए एक समर्पित [प्लेग्राउंड](/md/02.QuickStart/GitHubModel_QuickStart.md) है।

### Hugging Face पर Phi

आप [Hugging Face](https://huggingface.co/microsoft) पर भी मॉडल ढूंढ सकते हैं।

**प्लेटग्राउंड**  
[Hugging Chat प्लेग्राउंड](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 अन्य पाठ्यक्रम

हमारी टीम अन्य पाठ्यक्रम भी बनाती है! देखें:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j शुरुआती के लिए](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js शुरुआती के लिए](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain शुरुआती के लिए](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / एज / MCP / एजेंट्स
[![AZD शुरुआती के लिए](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![एज AI शुरुआती के लिए](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP शुरुआती के लिए](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI एजेंट्स शुरुआती के लिए](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### जनरेटिव AI श्रृंखला
[![जनरेटिव AI शुरुआती के लिए](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![जनरेटिव AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### कोर सीखना
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### कॉपिलट श्रृंखला
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## जिम्मेदार AI 

Microsoft हमारे ग्राहकों को हमारे AI उत्पादों का जिम्मेदारी से उपयोग करने में मदद देने, हमारे अनुभव साझा करने, और Transparency Notes और Impact Assessments जैसे उपकरणों के माध्यम से विश्वास-आधारित साझेदारी बनाने के लिए प्रतिबद्ध है। इन संसाधनों में से कई [https://aka.ms/RAI](https://aka.ms/RAI) पर उपलब्ध हैं।
Microsoft की जिम्मेदार AI की दृष्टिकोण हमारे AI के सिद्धांतों पर आधारित है: निष्पक्षता, विश्वसनीयता और सुरक्षा, गोपनीयता और सुरक्षा, समावेशन, पारदर्शिता, और जवाबदेही।

बड़े पैमाने पर प्राकृतिक भाषा, छवि, और भाषण मॉडल - जैसे कि इस उदाहरण में उपयोग किए गए - संभावित रूप से उन तरीकों से व्यवहार कर सकते हैं जो अनुचित, अविश्वसनीय, या आपत्तिजनक हो सकते हैं, जिससे हानि हो सकती है। कृपया जोखिमों और सीमाओं के बारे में सूचित रहने के लिए [Azure OpenAI सेवा पारदर्शिता नोट](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) देखें।

इन जोखिमों को कम करने के लिए अनुशंसित तरीका है कि आप अपनी आर्किटेक्चर में एक सुरक्षा प्रणाली शामिल करें जो हानिकारक व्यवहार का पता लगा सके और उसे रोक सके। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) एक स्वतंत्र सुरक्षा परत प्रदान करता है, जो एप्लिकेशन और सेवाओं में हानिकारक उपयोगकर्ता-जनित और AI-जनित सामग्री का पता लगा सकता है। Azure AI Content Safety में टेक्स्ट और इमेज API शामिल हैं जो हानिकारक सामग्री का पता लगाने में सक्षम हैं। Microsoft Foundry के भीतर, Content Safety सेवा आपको विभिन्न तरीकों में हानिकारक सामग्री का पता लगाने के लिए नमूना कोड देखने, खोजने और आज़माने की अनुमति देती है। निम्नलिखित [तात्कालिक दस्तावेज़](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) आपको सेवा के अनुरोधों का मार्गदर्शन करता है।

एक अन्य पहलू जो ध्यान में रखना है वह है समग्र अनुप्रयोग प्रदर्शन। मल्टी-मोडल और मल्टी-मॉडल एप्लिकेशन के साथ, हम प्रदर्शन को इस रूप में देखते हैं कि सिस्टम आपकी और आपके उपयोगकर्ताओं की अपेक्षाओं के अनुसार प्रदर्शन करता है, जिसमें हानिकारक आउटपुट उत्पन्न न करना शामिल है। अपनी समग्र एप्लिकेशन के प्रदर्शन का आकलन करना महत्वपूर्ण है, जिसके लिए आप [प्रदर्शन और गुणवत्ता और जोखिम और सुरक्षा मूल्यांककों](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) का उपयोग कर सकते हैं। आपके पास [कस्टम मूल्यांककों](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) के साथ सृजन और मूल्यांकन करने की क्षमता भी है।

आप अपने विकास वातावरण में [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) का उपयोग करके अपने AI एप्लिकेशन का मूल्यांकन कर सकते हैं। दिए गए परीक्षण डेटासेट या लक्ष्य के आधार पर, आपकी जनरेटिव AI एप्लिकेशन की पीढ़ी को अंतर्निर्मित या आपकी पसंद के कस्टम मूल्यांककों के साथ मात्रात्मक रूप से मापा जाता है। अपने सिस्टम के मूल्यांकन के लिए azure ai evaluation sdk के साथ शुरू करने हेतु आप [तात्कालिक गाइड](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) का पालन कर सकते हैं। एक बार जब आप मूल्यांकन रन निष्पादित करते हैं, तो आप [Microsoft Foundry में परिणामों का दृश्यांकन](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) कर सकते हैं।

## ट्रेडमार्क

यह प्रोजेक्ट परियोजनाओं, उत्पादों, या सेवाओं के ट्रेडमार्क या लोगो शामिल कर सकता है। Microsoft ट्रेडमार्क या लोगो के अधिकृत उपयोग पर Microsoft के ट्रेडमार्क और ब्रांड दिशानिर्देशों का पालन अनिवार्य है: [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)।
इस प्रोजेक्ट के संशोधित संस्करणों में Microsoft ट्रेडमार्क या लोगो का उपयोग भ्रम उत्पन्न नहीं करना चाहिए या Microsoft प्रायोजन का संकेत नहीं देना चाहिए। किसी तीसरे पक्ष के ट्रेडमार्क या लोगो के उपयोग पर उन तीसरे पक्ष की नीतियाँ लागू होती हैं।

## सहायता प्राप्त करना

यदि आप फंस गए हैं या AI एप्लिकेशन बनाने के बारे में कोई प्रश्न है, तो शामिल हों:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

यदि आपके पास उत्पाद फीडबैक है या निर्माण के दौरान त्रुटियाँ हैं, तो जाएं:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनूदित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->