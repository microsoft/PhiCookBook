# Phi कुकबुक: Microsoft का Phi मोडेलहरूका साथ हैण्ड्स-ऑन उदाहरणहरू

[![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi Microsoft द्वारा विकास गरिएको खुला स्रोत AI मोडेलहरूको श्रृंखला हो।

Phi हाल सबैभन्दा शक्तिशाली र लागत-प्रभावकारी सानो भाषा मोडेल (SLM) हो, जसले बहुभाषी, तर्कशक्ति, पाठ/च्याट उत्पादन, कोडिङ, छवि, अडियो र अन्य परिदृश्यहरूमा राम्रो प्रदर्शन गर्छ।

तपाईं Phi लाई क्लाउड वा एज डिभाइसहरूमा डिप्लोय गर्न सक्नुहुन्छ, र सीमित कम्प्युटिङ शक्ति सहित सजिलै जनरेटिभ AI अनुप्रयोगहरू बनाउन सक्नुहुन्छ।

यी स्रोतहरू प्रयोग गर्न सुरु गर्न यी चरणहरू अनुसरण गर्नुहोस्:
1. **रिपोजिटोरी फोर्क गर्नुहोस्**: क्लिक गर्नुहोस् [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **रिपोजिटोरी क्लोन गर्नुहोस्**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord समुदायमा जोडिनुहोस् र विशेषज्ञ तथा सह-विकासकर्ताहरूसँग भेटघाट गर्नुहोस्**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/ne/cover.eb18d1b9605d754b.webp)

### 🌐 बहुभाषिक समर्थन

#### GitHub Action मार्फत समर्थन (स्वचालित र सधैं अपडेटमा)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](./README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **स्थानीय रूपमा क्लोन गर्न चाहनुहुन्छ?**
>
> यो रिपोजिटोरीमा ५०+ भाषा अनुवादहरू छन् जसले डाउनलोड आकार धेरै बढाउँछ। अनुवादहरू बिना क्लोन गर्न, sparse checkout प्रयोग गर्नुहोस्:
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
> यसले तपाईँलाई कोर्स पूरा गर्न आवश्यक सबै कुरा छिटो डाउनलोड गर्न दिन्छ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## सुची सूची (Table of Contents)
- परिचय - [फाइ परिवारमा स्वागत छ](./md/01.Introduction/01/01.PhiFamily.md) - [तपाईंको वातावरण सेटअप गर्दै](./md/01.Introduction/01/01.EnvironmentSetup.md) - [मुख्य प्रविधिहरू बुझ्दै](./md/01.Introduction/01/01.Understandingtech.md) - [फाइ मोडेलहरूको लागि एआई सुरक्षा](./md/01.Introduction/01/01.AISafety.md) - [फाइ हार्डवेयर समर्थन](./md/01.Introduction/01/01.Hardwaresupport.md) - [फाइ मोडेलहरू र प्लेटफर्महरूमा उपलब्धता](./md/01.Introduction/01/01.Edgeandcloud.md) - [Guidance-ai र फाइको प्रयोग](./md/01.Introduction/01/01.Guidance.md) - [GitHub मार्केटप्लेस मोडेलहरू](https://github.com/marketplace/models) - [Azure AI मोडेल क्याटलग](https://ai.azure.com) - विभिन्न वातावरणमा फाइ अनुमान लगाउने - [Hugging face](./md/01.Introduction/02/01.HF.md) - [GitHub मोडेलहरू](./md/01.Introduction/02/02.GitHubModel.md) - [Microsoft Foundry मोडेल क्याटलग](./md/01.Introduction/02/03.AzureAIFoundry.md) - [ओलामा](./md/01.Introduction/02/04.Ollama.md) - [AI टूलकिट VSCode (AITK)](./md/01.Introduction/02/05.AITK.md) - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md) - [Foundry लोकल](./md/01.Introduction/02/07.FoundryLocal.md) - फाइ परिवारमा अनुमान लगाउने - [iOS मा फाइ अनुमान](./md/01.Introduction/03/iOS_Inference.md) - [एन्ड्रोइडमा फाइ अनुमान](./md/01.Introduction/03/Android_Inference.md) - [जेटसनमा फाइ अनुमान](./md/01.Introduction/03/Jetson_Inference.md) - [एआई पिसीमा फाइ अनुमान](./md/01.Introduction/03/AIPC_Inference.md) - [एप्पल MLX फ्रेमवर्कसँग फाइ अनुमान](./md/01.Introduction/03/MLX_Inference.md) - [लोकल सर्भरमा फाइ अनुमान](./md/01.Introduction/03/Local_Server_Inference.md) - [AI टूलकिट प्रयोग गरी रिमोट सर्भरमा फाइ अनुमान](./md/01.Introduction/03/Remote_Interence.md) - [रस्टसँग फाइ अनुमान](./md/01.Introduction/03/Rust_Inference.md) - [स्थानीय Vision मा फाइ अनुमान](./md/01.Introduction/03/Vision_Inference.md) - [Kaito AKS, Azure कन्टेनरहरूसँग (अधिकृत समर्थन) फाइ अनुमान](./md/01.Introduction/03/Kaito_Inference.md) - [फाइ परिवारको मात्रांकन](./md/01.Introduction/04/QuantifyingPhi.md) - [llama.cpp प्रयोग गरी फाइ-3.5 / 4 को मात्रांकन](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md) - [onnxruntime को लागि जनरेटिभ AI विस्तारहरू प्रयोग गरी फाइ-3.5 / 4 को मात्रांकन](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md) - [Intel OpenVINO प्रयोग गरी फाइ-3.5 / 4 को मात्रांकन](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md) - [एप्पल MLX फ्रेमवर्क प्रयोग गरी फाइ-3.5 / 4 को मात्रांकन](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md) - फाइको मूल्याङ्कन - [जिम्मेवार AI](./md/01.Introduction/05/ResponsibleAI.md) - [माइक्रोसफ्ट फाउंड्री मूल्याङ्कनका लागि](./md/01.Introduction/05/AIFoundry.md) - [मूल्याङ्कनका लागि प्रॉम्प्टफ्लो प्रयोग गर्दै](./md/01.Introduction/05/Promptflow.md) - Azure AI खोजीसँग RAG - [Azure AI खोजीमा Phi-4-mini र Phi-4-multimodal (RAG) कसरी प्रयोग गर्ने](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb) - फाइ अनुप्रयोग विकास नमूनाहरू - टेक्स्ट र कुराकानी अनुप्रयोगहरू - फाइ-4 नमूनाहरू - [📓] [Phi-4-mini ONNX मोडेलसँग कुराकानी](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md) - [Phi-4 स्थानीय ONNX मोडेल .NET सँग कुराकानी](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) - [Phi-4 ONNX प्रयोग गरी .NET कन्सोल एप सेमेन्टिक कर्नेलका साथ कुराकानी](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) - फाइ-3 / 3.5 नमूनाहरू - [ब्राउजरमा Phi3, ONNX Runtime Web र WebGPU प्रयोग गरेर स्थानीय च्याटबोट](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat) - [OpenVino च्याट](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md) - [बहु मोडेल - अन्तरक्रियात्मक Phi-3-mini र OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md) - [MLFlow - र्यापर निर्माण र Phi-3 सँग MLFlow प्रयोग गर्दै](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md) - [मोडेल अप्टिमाइजेसन - Phi-3-min मोडेललाई ONNX Runtime Web को लागि Olive संग कसरी अनुकूलन गर्ने](https://github.com/microsoft/Olive/tree/main/examples/phi3) - [WinUI3 एप Phi-3 mini-4k-instruct-onnx सँग](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/) - [WinUI3 बहु मोडेल AI सक्षम नोट्स एप नमूना](https://github.com/microsoft/ai-powered-notes-winui3-sample) - [प्रॉम्प्ट फ्लो सँग अनुकूलन गरी कस्टम Phi-3 मोडेलहरू समाहित गर्ने](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md) - [Microsoft Foundry मा प्रॉम्प्ट फ्लो सँग कस्टम Phi-3 मोडेलहरूको अनुकूलन र समावेशन](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md) - [Microsoft का जिम्मेवार AI सिद्धान्तहरूमा केन्द्रित Microsoft Foundry मा अनुकूलित Phi-3 / Phi-3.5 मोडेलको मूल्याङ्कन](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md) - [📓] [Phi-3.5-mini-instruct भाषा पूर्वानुमान नमूना (चिनी/अंग्रेजी)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb) - [Phi-3.5-Instruct WebGPU RAG च्याटबोट](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md) - [Windows GPU प्रयोग गरी Phi-3.5-Instruct ONNX सँग प्रॉम्प्ट फ्लो समाधान सिर्जना गर्दै](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md) - [Android एप सिर्जना गर्न Microsoft Phi-3.5 tflite प्रयोग गर्दै](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md) - [स्थानीय ONNX Phi-3 मोडेल प्रयोग गरी Q&A .NET उदाहरण Microsoft.ML.OnnxRuntime सँग](../../md/04.HOL/dotnet/src/LabsPhi301) - [सेमेन्टिक कर्नेल र Phi-3 सँग कन्सोल च्याट .NET एप](../../md/04.HOL/dotnet/src/LabsPhi302) - Azure AI अनुमान SDK कोडमा आधारित नमूनाहरू - फाइ-4 नमूनाहरू - [📓] [Phi-4-multimodal प्रयोग गरी प्रोजेक्ट कोड उत्पादन](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md) - फाइ-3 / 3.5 नमूनाहरू - [Microsoft Phi-3 परिवारसँग आफ्नो Visual Studio Code GitHub Copilot च्याट बनाउनुहोस्](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md) - [GitHub मोडेलहरूद्वारा Phi-3.5 सँग आफ्नो Visual Studio Code च्याट कोपिलट एजेन्ट बनाउनुहोस्](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md) - उन्नत तर्क नमूनाहरू - फाइ-4 नमूनाहरू - [📓] [Phi-4-mini-तर्क वा Phi-4-तर्क नमूनाहरू](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md) - [📓] [Microsoft Olive सँग Phi-4-mini-तर्कको अनुकूलन](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [एप्पल MLX सँग Phi-4-mini-तर्कको अनुकूलन](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [GitHub मोडेलहरू सहित Phi-4-mini-तर्क](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb) - [📓] [Microsoft Foundry मोडेलहरू सहित Phi-4-mini-तर्क](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb) -
डेमोहरू - [Phi-4-मिनी डेमोहरू जुन Hugging Face Spaces मा होस्ट गरिएको छ](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo) - [Phi-4-मल्टिमोडल डेमोहरू जुन Hugging Face Spaces मा होस्ट गरिएको छ](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo) - भिजन नमूनाहरू - Phi-4 नमूनाहरू - [📓] [Phi-4-मल्टिमोडल प्रयोग गरेर छविहरू पढ्न र कोड उत्पन्न गर्न](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) - Phi-3 / 3.5 नमूनाहरू - [📓][Phi-3-भिजन-छवि टेक्स्ट देखि टेक्स्ट](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [Phi-3-भिजन-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html) - [📓][Phi-3-भिजन CLIP एम्बेडिङ](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [डेमो: Phi-3 रीसाइकलिङ](https://github.com/jennifermarsman/PhiRecycling/) - [Phi-3-भिजन - भिजुअल भाषा सहायक - Phi3-भिजन र OpenVINO संग](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html) - [Phi-3 भिजन Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md) - [Phi-3 भिजन OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md) - [📓][Phi-3.5 भिजन मल्टि-फ्रेम वा मल्टि-इमेज नमूना](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb) - [Phi-3 भिजन स्थानीय ONNX मोडेल Microsoft.ML.OnnxRuntime .NET प्रयोग गरी](../../md/04.HOL/dotnet/src/LabsPhi303) - [मेनु आधारित Phi-3 भिजन स्थानीय ONNX मोडेल Microsoft.ML.OnnxRuntime .NET प्रयोग गरी](../../md/04.HOL/dotnet/src/LabsPhi304) - तर्क-भिजन नमूनाहरू - Phi-4-तर्क-भिजन-15B - [📓] [Phi-4-तर्क-भिजन-15B प्रयोग गरेर जेवलकिङ पत्ता लगाउने](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb) - [📓] [Phi-4-तर्क-भिजन-15B प्रयोग गरेर गणित गर्ने](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb) - [📓] [Phi-4-तर्क-भिजन-15B प्रयोग गरेर UI पत्ता लगाउने](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb) - गणित नमूनाहरू - Phi-4-मिनी-फ्ल्यास-तर्क-इन्स्ट्रक्ट नमूनाहरू [Phi-4-मिनी-फ्ल्यास-तर्क-इन्स्ट्रक्ट संग गणित डेमो](./md/02.Application/09.Math/MathDemo.ipynb) - अडियो नमूनाहरू - Phi-4 नमूनाहरू - [📓] [Phi-4-मल्टिमोडल प्रयोग गरेर अडियो ट्रान्सक्रिप्ट निकाल्ने](./md/02.Application/05.Audio/Phi4/Transciption/README.md) - [📓] [Phi-4-मल्टिमोडल अडियो नमूना](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb) - [📓] [Phi-4-मल्टिमोडल स्पीच ट्रान्सलेसन नमूना](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb) - [.NET कन्सोल एप्लिकेसन Phi-4-मल्टिमोडल अडियो प्रयोग गरी अडियो फाइल विश्लेषण र ट्रान्सक्रिप्ट उत्पन्न गर्न](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) - MOE नमूनाहरू - Phi-3 / 3.5 नमूनाहरू - [📓] [Phi-3.5 विशेषज्ञहरूको मिश्रण मोडेल (MoEs) सामाजिक मिडिया नमूना](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb) - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, र LlamaIndex प्रयोग गरेर Retrieval-Augmented Generation (RAG) पाइपलाइन निर्माण](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb) - - फङ्शन कलिङ नमूनाहरू - Phi-4 नमूनाहरू 🆕 - [📓] [Phi-4-मिनी संग फङ्शन कलिङ प्रयोग गर्ने](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md) - [📓] [Phi-4-मिनी संग फङ्शन कलिङ प्रयोग गरेर मल्टि-एजेन्टहरू निर्माण गर्ने](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb) - [📓] [Ollama संग फङ्शन कलिङ प्रयोग गर्ने](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb) - [📓] [ONNX संग फङ्शन कलिङ प्रयोग गर्ने](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb) - मल्टिमोडल मिसिङ नमूनाहरू - Phi-4 नमूनाहरू 🆕 - [📓] [Phi-4-मल्टिमोडललाई प्रविधि पत्रकारको रूपमा प्रयोग गर्ने](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb) - [.NET कन्सोल एप्लिकेसन Phi-4-मल्टिमोडल प्रयोग गरी छविहरू विश्लेषण गर्न](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) - फाइन-ट्युनिङ Phi नमूनाहरू - [फाइन-ट्युनिङ परिदृश्यहरू](./md/03.FineTuning/FineTuning_Scenarios.md) - [फाइन-ट्युनिङ vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md) - [Phi-3 लाई उद्योग विशेषज्ञ बनाउने फाइन-ट्युनिङ](./md/03.FineTuning/LetPhi3gotoIndustriy.md) - [VS Code का लागि AI टूलकिट सहित Phi-3 फाइन-ट्युनिङ](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md) - [Azure Machine Learning सेवा संग Phi-3 फाइन-ट्युनिङ](./md/03.FineTuning/Introduce_AzureML.md) - [Lora संग Phi-3 फाइन-ट्युनिङ](./md/03.FineTuning/FineTuning_Lora.md) - [QLora संग Phi-3 फाइन-ट्युनिङ](./md/03.FineTuning/FineTuning_Qlora.md) - [Microsoft Foundry संग Phi-3 फाइन-ट्युनिङ](./md/03.FineTuning/FineTuning_AIFoundry.md) - [Azure ML CLI/SDK संग Phi-3 फाइन-ट्युनिङ](./md/03.FineTuning/FineTuning_MLSDK.md) - [Microsoft Olive संग फाइन-ट्युनिङ](./md/03.FineTuning/FineTuning_MicrosoftOlive.md) - [Microsoft Olive ह्यान्ड्स-ओन ल्याब सहित फाइन-ट्युनिङ](./md/03.FineTuning/olive-lab/readme.md) - [Weights and Bias संग Phi-3-भिजन फाइन-ट्युनिङ](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md) - [Apple MLX Framework संग Phi-3 फाइन-ट्युनिङ](./md/03.FineTuning/FineTuning_MLX.md) - [Phi-3-भिजन (अधिकारिक समर्थन) फाइन-ट्युनिङ](./md/03.FineTuning/FineTuning_Vision.md) - [Kaito AKS, Azure Containers (अधिकारिक समर्थन) संग Phi-3 फाइन-ट्युनिङ](./md/03.FineTuning/FineTuning_Kaito.md) - [Phi-3 र 3.5 भिजन फाइन-ट्युनिङ](https://github.com/2U1/Phi3-Vision-Finetune) - ह्यान्ड्स-ओन ल्याब - [आधुनिकतम मोडेलहरू अन्वेषण गर्दै: LLMs, SLMs, स्थानीय विकास र थप](https://github.com/microsoft/aitour-exploring-cutting-edge-models) - [NLP को सम्भावनाहरू खुलाउने: Microsoft Olive संग फाइन-ट्युनिङ](https://github.com/azure/Ignite_FineTuning_workshop) - शैक्षिक अनुसन्धान कागज र प्रकाशनहरू - [Textbooks Are All You Need II: phi-1.5 प्राविधिक रिपोर्ट](https://arxiv.org/abs/2309.05463) - [Phi-3 प्राविधिक रिपोर्ट: तपाईंको फोनमा स्थानीय रूपमा अत्यधिक सक्षम भाषा मोडेल](https://arxiv.org/abs/2404.14219) - [Phi-4 प्राविधिक रिपोर्ट](https://arxiv.org/abs/2412.08905) - [Phi-4-मिनी प्राविधिक रिपोर्ट: प्याक्ट र शक्तिशाली मल्टिमोडल भाषा मोडेलहरू Mixture-of-LoRAs मार्फत](https://arxiv.org/abs/2503.01743) - [सवारीसाधनमा कार्य-कलिङका लागि साना भाषा मोडेलहरू अनुकूलन गर्ने](https://arxiv.org/abs/2501.02342) - [(WhyPHI) बहुविकल्प प्रश्न उत्तरका लागि PHI-3 को फाइन-ट्युनिङ: विधि, नतिजा, र चुनौतीहरू](https://arxiv.org/abs/2501.01588) - [Phi-4-तर्क प्राविधिक रिपोर्ट](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-तर्क रिपोर्ट](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)
# Phi कुकबुक: Microsoft का Phi मोडेलहरूसँग प्रत्यक्ष उदाहरणहरू

[![GitHub Codespaces मा नमूनाहरू खोल्नुहोस् र प्रयोग गर्नुहोस्](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers मा खोल्नुहोस्](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub योगदानकर्ताहरू](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub समस्याहरू](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub पुल अनुरोधहरू](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs स्वागतयोग्य](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub अवलोकनकर्ताहरू](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub फोर्कहरू](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub स्टारहरू](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi Microsoft द्वारा विकास गरिएका खुला स्रोत AI मोडेलहरूको एउटा शृंखला हो।

Phi वर्तमानमा सबैभन्दा शक्तिशाली र लागत-प्रभावकारी सानो भाषा मोडेल (SLM) हो, जसले बहुभाषिक, तर्क, पाठ/च्याट उत्पादन, कोडिङ, छवि, अडियो र अन्य परिदृश्यहरूमा उत्कृष्ट बेंचमार्कहरू देखाउँछ।

तपाईं Phi लाई क्लाउडमा वा एज उपकरणहरूमा तैनाथ गर्न सक्नुहुन्छ, र सीमित कम्प्युटिङ शक्तिका साथ सजिलै जेनेरेटिभ AI अनुप्रयोगहरू निर्माण गर्न सक्नुहुन्छ।

यी स्रोतहरू प्रयोग गर्न सुरूवात गर्न यी चरणहरू पालना गर्नुहोस्:
1. **रेपोजिटोरी फोर्क गर्नुहोस्**: क्लिक गर्नुहोस् [![GitHub फोर्कहरू](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **रेपोजिटोरी क्लोन गर्नुहोस्**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord समुदायमा सामेल हुनुहोस् र विशेषज्ञहरू र सहकर्मी विकासकर्ताहरूसँग भेट्नुहोस्**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/ne/cover.eb18d1b9605d754b.webp)

### 🌐 बहुभाषिक समर्थन

#### GitHub Action द्वारा समर्थन (स्वचालित र सधैं अद्यावधिक)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरबी](../ar/README.md) | [बंगाली](../bn/README.md) | [बुल्गेरियन](../bg/README.md) | [बर्मी (म्यानमार)](../my/README.md) | [चिनी (सरलीकृत)](../zh-CN/README.md) | [चिनी (परम्परागत, हङकङ)](../zh-HK/README.md) | [चिनी (परम्परागत, मकाउ)](../zh-MO/README.md) | [चिनी (परम्परागत, ताइवान)](../zh-TW/README.md) | [क्रोएशियन](../hr/README.md) | [चेक](../cs/README.md) | [डेनिश](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियन](../et/README.md) | [फिनिश](../fi/README.md) | [फ्रेन्च](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हेब्रू](../he/README.md) | [हिन्दी](../hi/README.md) | [हंगेरियन](../hu/README.md) | [इन्डोनेशियन](../id/README.md) | [इतालियन](../it/README.md) | [जापानी](../ja/README.md) | [कन्नड](../kn/README.md) | [खमेर](../km/README.md) | [कोरियन](../ko/README.md) | [लिथुवेनियन](../lt/README.md) | [मलय](../ms/README.md) | [मलयालम](../ml/README.md) | [मराठी](../mr/README.md) | [नेपाली](./README.md) | [नाइजेरियन पिडगिन](../pcm/README.md) | [नर्वेजियन](../no/README.md) | [फारसी (पर्शियन)](../fa/README.md) | [पोलिश](../pl/README.md) | [पुर्तगाली (ब्राजिल)](../pt-BR/README.md) | [पुर्तगाली (पुर्तगाल)](../pt-PT/README.md) | [पञ्जाबी (गुरुमुखी)](../pa/README.md) | [रोमानियन](../ro/README.md) | [रूसी](../ru/README.md) | [सर्बियाली (सिरिलिक)](../sr/README.md) | [स्लोभाक](../sk/README.md) | [स्लोभेनियाली](../sl/README.md) | [स्पेनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्विडिश](../sv/README.md) | [टागालग (फिलिपिनो)](../tl/README.md) | [तामिल](../ta/README.md) | [तेलुगु](../te/README.md) | [थाई](../th/README.md) | [टर्किश](../tr/README.md) | [युक्रेनी](../uk/README.md) | [उर्दू](../ur/README.md) | [भियतनामी](../vi/README.md)

> **स्थानीय रूपमा क्लोन गर्न चाहनुहुन्छ?**
>
> यस रेपोजिटोरिमा ५०+ भाषा अनुवादहरू छन् जसले डाउनलोड साइज धेरै बढाउँछ। अनुवाद बिना क्लोन गर्न, sparse checkout प्रयोग गर्नुहोस्:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (विन्डोज):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> यसले तपाईंलाई धेरै छिटो डाउनलोडसँग पाठ्यक्रम पूरा गर्न आवश्यक सबै कुरा दिन्छ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## सामग्री तालिका

## Phi मोडेलहरू प्रयोग गर्दै

### Microsoft Foundry मा Phi

तपाईं Microsoft Phi कसरी प्रयोग गर्ने र विभिन्न हार्डवेयर उपकरणहरूमा E2E समाधानहरू कसरी बनाउने जान्न सक्नुहुन्छ। आफैले Phi अनुभव गर्नको लागि, मोडेलहरूसँग खेल्न सुरु गर्नुहोस् र आफ्नो परिदृश्यहरूका लागि Phi अनुकूलित गर्नुहोस् [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) बाट तपाईं [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) सँग कसरी सुरु गर्ने जान्न सक्नुहुन्छ।

**प्लेराउन्ड**
प्रत्येक मोडेलसँग परीक्षण गर्नको लागि समर्पित प्लेराउन्ड छ [Azure AI Playground](https://aka.ms/try-phi3)।

### GitHub मोडेलहरूमाथि Phi

तपाईं Microsoft Phi कसरी प्रयोग गर्ने र विभिन्न हार्डवेयर उपकरणहरूमा E2E समाधानहरू कसरी बनाउने जान्न सक्नुहुन्छ। आफैले Phi अनुभव गर्नको लागि, मोडेलसँग खेल्न सुरु गर्नुहोस् र आफ्नो परिदृश्यहरूका लागि Phi अनुकूलित गर्नुहोस् [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) बाट तपाईं [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) सँग कसरी सुरु गर्ने जान्न सक्नुहुन्छ।

**प्लेराउन्ड**
प्रत्येक मोडेलसँग परीक्षण गर्नको लागि समर्पित [प्लेराउन्ड छ](/md/02.QuickStart/GitHubModel_QuickStart.md)।

### Hugging Face मा Phi

तपाईं मोडेल [Hugging Face](https://huggingface.co/microsoft) मा पनि फेला पार्न सक्नुहुन्छ।

**प्लेराउन्ड**
[Hugging Chat प्लेराउन्ड](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🎒 अन्य पाठ्यक्रमहरू

हाम्रो टोलीले अन्य पाठ्यक्रमहरू पनि उत्पादन गर्छ! हेर्नुहोस्:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![शुरुआतीहरूको लागि LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![शुरुआतीहरूको लागि LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![शुरुआतीहरूको लागि LangChain](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / एजेन्टहरू
[![शुरुआतीहरूको लागि AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![शुरुआतीहरूको लागि Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![शुरुआतीहरूको लागि MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![शुरुआतीहरूको लागि AI एजेन्टहरू](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### जेनेरेटिभ AI शृंखला
[![शुरुआतीहरूको लागि जेनेरेटिभ AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![जेनेरेटिभ AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
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
 
### कोपिलट शृंखला
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## जिम्मेवार AI 

माइक्रोसफ्ट हाम्रा ग्राहकहरूलाई हाम्रा AI उत्पादनहरू जिम्मेवार रूपमा प्रयोग गर्न मद्दत गर्न प्रतिबद्ध छ, हाम्रा सिकाइहरू साझा गर्दै, र Transparency Notes र Impact Assessments जस्ता उपकरणहरू मार्फत विश्वास-आधारित साझेदारीहरू निर्माण गर्दै। यी धेरै स्रोतहरू [https://aka.ms/RAI](https://aka.ms/RAI) मा फेला पार्न सकिन्छ।
माइक्रोसफ्टको जिम्मेवार AI को दृष्टिकोण हामीलाई AI का सिद्धान्तहरूमा आधारित छ: न्याय, विश्वसनीयता र सुरक्षा, गोपनीयता र सुरक्षा, समावेशिता, पारदर्शिता, र जवाफदेही।

विशाल-स्तरका प्राकृतिक भाषा, छवि, र भाषण मोडलहरू - जस्तै यस नमुना प्रयोग गरिएको - सम्भावित रूपमा अन्यायपूर्ण, अविश्वसनीय, वा आक्रामक तरिकाले व्यवहार गर्न सक्छन्, जसले नोक्सानी पुर्याउन सक्छ। कृपया जोखिमहरू र सीमाहरूको जानकारी लिन [Azure OpenAI सेवा Transparency नोट](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) सल्लाह लिनुहोस्।

यी जोखिमहरू कम गर्न सिफारिस गरिएको दृष्टिकोण भनेको तपाईंको वास्तुकलामा एक सुरक्षा प्रणाली समावेश गर्नु हो जसले हानिकारक व्यवहार पत्ता लगाउन र रोक्न सक्छ। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) स्वतन्त्र सुरक्षा तह प्रदान गर्दछ, जसले अनुप्रयोगहरू र सेवाहरूमा हानिकारक प्रयोगकर्ता-निर्मित र AI-निर्मित सामग्री पत्ता लगाउन सक्छ। Azure AI Content Safety ले पाठ र छवि API हरू प्रदान गर्दछ जसले हानिकारक सामग्री पत्ता लगाउन सक्षम पार्छ। Microsoft Foundry भित्र, Content Safety सेवा तपाईलाई विभिन्न मोडालिटिज़मा हानिकारक सामग्री पत्ता लगाउन नमूना कोडहरू हेर्न, अन्वेषण गर्न र प्रयास गर्न अनुमति दिन्छ। तलको [छिटो आरम्भ गर्ने कागजात](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) सेवा प्रयोग गर्न निर्देशन दिन्छ।

अर्को पक्ष हो समग्र अनुप्रयोग प्रदर्शनलाई ध्यान दिनु। बहु-मोडाल र बहु-मोडेल अनुप्रयोगहरूसँग, हामी प्रदर्शन भन्नाले प्रणालीले तपाईं र तपाईंका प्रयोगकर्ताहरूले अपेक्षा गरे जस्तो प्रदर्शन गर्ने कुरा बुझ्छौं, जसले हानिकारक आउटपुटहरू पनि सिर्जना नगर्नुपर्छ। तपाईंको समग्र अनुप्रयोगको प्रदर्शन [Performance and Quality and Risk and Safety परिवेक्षकहरू](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) प्रयोग गरेर मूल्याङ्कन गर्नु महत्त्वपूर्ण छ। तपाईंले [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) सँग सिर्जना र मूल्याङ्कन गर्ने क्षमता पनि राख्नुहुन्छ।

तपाईं आफ्नो AI अनुप्रयोगलाई विकास वातावरणमा [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) प्रयोग गरेर मूल्याङ्कन गर्न सक्नुहुन्छ। परीक्षण डेटासेट वा लक्ष्य दिइएको अवस्थामा, तपाईंको जनरेटिभ AI अनुप्रयोगका उत्पादनहरूले जुन मूल्याङ्कन छनौट गर्नु भएको छ, बिल्ट-इन या कस्टम मूल्याङ्ककहरूसँग मात्रात्मक नापिन्छ। आफ्नो प्रणाली मूल्याङ्कन गर्न azure ai evaluation sdk सँग सुरु गर्न, तपाईं [छिटो आरम्भ मार्गदर्शक](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) लाई पालना गर्न सक्नुहुन्छ। एक पटक मूल्याङ्कन रन चलाएपछि, तपाईं [Microsoft Foundry मा नतिजाहरू दृश्यात्मक रूपले देख्न सक्नुहुन्छ](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)।

## ट्रेडमार्कहरू

यस परियोजनामा परियोजनाहरू, उत्पादनहरू, वा सेवाहरूको ट्रेडमार्क वा लोगोहरू समावेश हुन सक्छन्। माइक्रोसफ्ट ट्रेडमार्क वा लोगोहरूको अधिकृत प्रयोग [Microsoft को ट्रेडमार्क र ब्रान्ड दिशानिर्देशहरू](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) अनुसार हुनुपर्छ र यसको पालना गर्नुपर्छ।
यस परियोजनाका संशोधित संस्करणहरूमा माइक्रोसफ्ट ट्रेडमार्क वा लोगोहरूको प्रयोगले भ्रम सिर्जना गर्न वा माइक्रोसफ्टको प्रायोजन संकेत गर्न हुँदैन। तेस्रो पक्षका ट्रेडमार्क वा लोगोहरूको कुनै पनि प्रयोग तेस्रो पक्षका नीतिहरूको अधीनमा हुन्छ।

## सहयोग प्राप्त गर्ने तरिका

यदि तपाईं अड्किनुभयो वा AI अनुप्रयोगहरू निर्माण गर्दा कुनै प्रश्न छ भने, सामेल हुनुहोस्:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

यदि तपाईंले निर्माता प्रतिक्रिया वा त्रुटिहरू छ भने:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा असत्यताहरू हुन सक्दछन्। मूल दस्तावेज यसको मूल भाषामा नै आधिकारिक स्रोत मानिनु पर्छ। महत्त्वपूर्ण जानकारीका लागि व्यावसायिक मानवीय अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट हुने कुनै पनि गलतफहमी वा गलत व्याख्याहरूका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->