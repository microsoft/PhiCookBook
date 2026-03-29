# Phi Cookbook: Microsoft च्या Phi मॉडेल्ससह प्रत्यक्ष उदाहरणे

[![GitHub Codespaces मध्ये नमुने उघडा आणि वापरा](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers मध्ये उघडा](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub योगदानकर्ते](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub मुद्दे](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub पुल-रिक्वेस्ट्स](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs स्वागतार्ह](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub अनुयायी](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub स्टार्स](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi ही Microsoft कडून विकसित केलेली एआय मॉडेल्सची एक मालिका आहे.

Phi सध्याच्या काळात बहुभाषिक, तर्कशक्ती, मजकूर/चॅट जनरेशन, कोडिंग, प्रतिमा, ऑडिओ आणि इतर परिस्थितींमध्ये खूप चांगल्या बेंचमार्कसह सर्वात शक्तिशाली आणि किंमतीच्या दृष्टीने प्रभावी लहान भाषा मॉडेल (SLM) आहे.

आपण Phi क्लाऊड किंवा एज उपकरणांवर तैनात करू शकता, आणि आपल्याला मर्यादित संगणकीय शक्तीने सहज जनरेटिव्ह एआय अनुप्रयोग तयार करता येतात.

या साधनाचा वापर सुरू करण्यासाठी खालील पावले फॉलो करा:
1. **रिपॉझिटरी फोर्क करा**: Click [![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **रिपॉझिटरी क्लोन करा**:  `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord Community मध्ये सामील व्हा आणि तज्ञ व सहकारी विकासकांशी भेटा**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/mr/cover.eb18d1b9605d754b.webp)

### 🌐 बहुभाषिक समर्थन

#### GitHub Action द्वारे समर्थित (स्वयंचलित व नेहमी अद्ययावत)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](./README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **स्थानिक क्लोन करणे पसंत आहे?**
>
> या रिपॉझिटरीमध्ये ५०+ भाषांमध्ये भाषांतर आहे जी डाउनलोड आकार मोठा करतात. भाषांतरांशिवाय क्लोन करण्यासाठी sparse checkout वापरा:
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
> यामुळे तुम्हाला कोर्स पूर्ण करण्यासाठी आवश्यक सर्व काही मिळते, आणि डाउनलोड जलद होते.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## अनुक्रमणिका
- परिचय - [Phi कुटुंबात आपले स्वागत आहे](./md/01.Introduction/01/01.PhiFamily.md) - [आपले वातावरण सेट करणे](./md/01.Introduction/01/01.EnvironmentSetup.md) - [मूळ तंत्रज्ञान समजून घेणे](./md/01.Introduction/01/01.Understandingtech.md) - [Phi मॉडेलसाठी AI सुरक्षा](./md/01.Introduction/01/01.AISafety.md) - [Phi हार्डवेअर समर्थन](./md/01.Introduction/01/01.Hardwaresupport.md) - [प्लॅटफॉर्मवर Phi मॉडेल्स आणि उपलब्धता](./md/01.Introduction/01/01.Edgeandcloud.md) - [Guidance-ai आणि Phi वापरणे](./md/01.Introduction/01/01.Guidance.md) - [GitHub मार्केटप्लेस मॉडेल्स](https://github.com/marketplace/models) - [Azure AI मॉडेल कॅटलॉग](https://ai.azure.com) - विविध वातावरणात Phi चे अनुमान - [Hugging face](./md/01.Introduction/02/01.HF.md) - [GitHub मॉडेल्स](./md/01.Introduction/02/02.GitHubModel.md) - [Microsoft Foundry मॉडेल कॅटलॉग](./md/01.Introduction/02/03.AzureAIFoundry.md) - [Ollama](./md/01.Introduction/02/04.Ollama.md) - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md) - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md) - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md) - Phi कुटुंबाचा अनुमान - [iOS वर Phi चे अनुमान](./md/01.Introduction/03/iOS_Inference.md) - [Android वर Phi चे अनुमान](./md/01.Introduction/03/Android_Inference.md) - [Jetson वर Phi चे अनुमान](./md/01.Introduction/03/Jetson_Inference.md) - [AI PC वर Phi चे अनुमान](./md/01.Introduction/03/AIPC_Inference.md) - [Apple MLX फ्रेमवर्कसह Phi चे अनुमान](./md/01.Introduction/03/MLX_Inference.md) - [स्थानिक सर्व्हरमध्ये Phi चे अनुमान](./md/01.Introduction/03/Local_Server_Inference.md) - [AI Toolkit वापरून रिमोट सर्व्हरमध्ये Phi चे अनुमान](./md/01.Introduction/03/Remote_Interence.md) - [Rust सह Phi चे अनुमान](./md/01.Introduction/03/Rust_Inference.md) - [स्थानिक Vision मध्ये Phi चे अनुमान](./md/01.Introduction/03/Vision_Inference.md) - [Kaito AKS, Azure कंटेनर्ससह Phi चे अनुमान (अधिकृत समर्थन)](./md/01.Introduction/03/Kaito_Inference.md) - [Phi कुटुंबाचे मात्रा मापन](./md/01.Introduction/04/QuantifyingPhi.md) - [llama.cpp वापरून Phi-3.5 / 4 क्वांटायजिंग](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md) - [onnxruntime साठी Generative AI एक्सटेंशन्स वापरून Phi-3.5 / 4 क्वांटायजिंग](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md) - [Intel OpenVINO वापरून Phi-3.5 / 4 क्वांटायजिंग](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md) - [Apple MLX फ्रेमवर्क वापरून Phi-3.5 / 4 क्वांटायजिंग](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md) - Phi चे मूल्यांकन - [जबाबदार AI](./md/01.Introduction/05/ResponsibleAI.md) - [मूल्यांकनासाठी Microsoft Foundry](./md/01.Introduction/05/AIFoundry.md) - [मूल्यांकनासाठी Promptflow वापरणे](./md/01.Introduction/05/Promptflow.md) - Azure AI शोधासह RAG - [Azure AI शोधासह Phi-4-mini आणि Phi-4-multimodal (RAG) कसे वापरावे](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb) - Phi अनुप्रयोग विकास नमुने - मजकूर आणि चॅट अनुप्रयोग - Phi-4 नमुने - [📓] [Phi-4-mini ONNX मॉडेलसह चॅट](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md) - [स्थानीक Phi-4 ONNX मॉडेलसह चॅट .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) - [Semantic Kernel वापरून Phi-4 ONNX सह .NET कन्सोल चॅट अ‍ॅप](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) - Phi-3 / 3.5 नमुने - [Phi3, ONNX Runtime वेब आणि WebGPU वापरून ब्राउझरमध्ये स्थानिक चॅटबॉट](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat) - [OpenVino चॅट](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md) - [मल्टि मॉडेल - इंटरअ‍ॅक्टिवPhi-3-mini आणि OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md) - [MLFlow - Phi-3 सह एक wrapper तयार करणे आणि वापरणे](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md) - [मॉडेल ऑप्टिमायझेशन - Phi-3-mini मॉडेल ONNX Runtime वेबसाठी कसे ऑप्टिमाईज करावे Olive वापरून](https://github.com/microsoft/Olive/tree/main/examples/phi3) - [Phi-3 मिनी-4k-instruct-onnx सह WinUI3 अ‍ॅप](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/) - [WinUI3 मल्टि मॉडेल AI आधारित नोट्स अ‍ॅप नमुना](https://github.com/microsoft/ai-powered-notes-winui3-sample) - [Prompt flow सह कस्टम Phi-3 मॉडेल्स फाईन-ट्यून आणि इंटिग्रेट करा](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md) - [Microsoft Foundry मध्ये Prompt flow सह कस्टम Phi-3 मॉडेल्स फाईन-ट्यून आणि इंटिग्रेट करा](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md) - [Microsoft च्या जबाबदार AI तत्त्वांवर केंद्रित Microsoft Foundry मध्ये फाइन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलचे मूल्यांकन करा](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md) - [📓] [Phi-3.5-mini-instruct भाषा भाकित नमुना (चिनी/इंग्रजी)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb) - [Phi-3.5-Instruct WebGPU RAG चॅटबॉट](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md) - [Phi-3.5-Instruct ONNX सह Windows GPU वापरून Prompt flow सोल्यूशन्स तयार करणे](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md) - [Microsoft Phi-3.5 tflite वापरून Android अ‍ॅप तयार करणे](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md) - [स्थानिक ONNX Phi-3 मॉडेल वापरून Q&A .NET उदाहरण Microsoft.ML.OnnxRuntime वापरून](../../md/04.HOL/dotnet/src/LabsPhi301) - [Semantic Kernel आणि Phi-3 सह .NET कन्सोल चॅट अ‍ॅप](../../md/04.HOL/dotnet/src/LabsPhi302) - Azure AI Inference SDK कोड आधारित नमुने - Phi-4 नमुने - [📓] [Phi-4-multimodal वापरून प्रोजेक्ट कोड तयार करा](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md) - Phi-3 / 3.5 नमुने - [Microsoft Phi-3 कुटुंबासह आपले स्वतःचे Visual Studio Code GitHub Copilot चॅट तयार करा](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md) - [GitHub मॉडेल्स वापरून Phi-3.5 सह आपला स्वतःचा Visual Studio Code चॅट Copilot एजंट तयार करा](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md) - प्रगत तर्क नमुने - Phi-4 नमुने - [📓] [Phi-4-mini-reasoning किंवा Phi-4-reasoning नमुने](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md) - [📓] [Microsoft Olive सह Phi-4-mini-reasoning फाइन-ट्यूनिंग](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Apple MLX सह Phi-4-mini-reasoning फाइन-ट्यूनिंग](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [GitHub मॉडेल्ससह Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb) - [📓] [Microsoft Foundry मॉडेल्ससह Phi-4-mini-reasoning](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb) -
डेमो - [Phi-4-mini डेमो Hugging Face Spaces वर होस्ट केलेले](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo) - [Phi-4-multimodal डेमो Hugging Face Spaces वर होस्ट केलेले](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo) - व्हिजन सॅंपल्स - Phi-4 सॅंपल्स - [📓] [प्रतिमा वाचण्यासाठी आणि कोड जनरेट करण्यासाठी Phi-4-multimodal वापरा](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) - Phi-3 / 3.5 सॅंपल्स - [📓][Phi-3-vision-प्रतिमा मजकूर ते मजकूर](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html) - [📓][Phi-3-vision CLIP एम्बेडिंग](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [डेमो: Phi-3 रिसायक्लिंग](https://github.com/jennifermarsman/PhiRecycling/) - [Phi-3-vision - व्हिज्युअल भाषा सहाय्यक - Phi3-Vision आणि OpenVINO सह](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html) - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md) - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md) - [📓][Phi-3.5 Vision मल्टि-फ्रेम किंवा मल्टि-इमेज सॅंपल](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb) - [Phi-3 Vision Microsoft.ML.OnnxRuntime .NET वापरून लोकल ONNX मॉडेल](../../md/04.HOL/dotnet/src/LabsPhi303) - [मेनू आधारित Phi-3 Vision Microsoft.ML.OnnxRuntime .NET वापरून लोकल ONNX मॉडेल](../../md/04.HOL/dotnet/src/LabsPhi304) - रिझनिंग-व्हिजन सॅंपल्स - Phi-4-Reasoning-Vision-15B - [📓] [Phi-4-Reasoning-Vision-15B वापरून जॉवॉकिंग ओळखणे](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb) - [📓] [Phi-4-Reasoning-Vision-15B वापरून गणित](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb) - [📓] [Phi-4-Reasoning-Vision-15B वापरून UI ओळखणे](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb) - गणित सॅंपल्स - Phi-4-Mini-Flash-Reasoning-Instruct सॅंपल्स [Phi-4-Mini-Flash-Reasoning-Instruct सह गणित डेमो](./md/02.Application/09.Math/MathDemo.ipynb) - ऑडिओ सॅंपल्स - Phi-4 सॅंपल्स - [📓] [Phi-4-multimodal वापरून ऑडिओ ट्रान्सक्रिप्ट्स काढणे](./md/02.Application/05.Audio/Phi4/Transciption/README.md) - [📓] [Phi-4-multimodal ऑडिओ सॅंपल](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb) - [📓] [Phi-4-multimodal स्पीच ट्रान्सलेशन सॅंपल](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb) - [Phi-4-multimodal ऑडिओ वापरून एका аудिओ फाइलचे विश्लेषण करण्यासाठी .NET कन्सोल अनुप्रयोग आणि ट्रान्सक्रिप्ट जनरेट करणे](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) - MOE सॅंपल्स - Phi-3 / 3.5 सॅंपल्स - [📓] [Phi-3.5 मिक्सचर ऑफ एक्सपर्ट्स मॉडेल्स (MoEs) सोशल मीडिया सॅंपल](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb) - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI शोध, आणि LlamaIndex सह रिट्रीव्हल-ऑगमेंटेड जनरेशन (RAG) पाईपलाइन तयार करणे](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb) - - फंक्शन कॉलिंग सॅंपल्स - Phi-4 सॅंपल्स 🆕 - [📓] [Phi-4-mini सह फंक्शन कॉलिंग वापरणे](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md) - [📓] [Phi-4-mini सह मल्टि-एजंट तयार करण्यासाठी फंक्शन कॉलिंग वापरणे](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb) - [📓] [Ollama सह फंक्शन कॉलिंग वापरणे](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb) - [📓] [ONNX सह फंक्शन कॉलिंग वापरणे](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb) - मल्टीमोडल मिक्सिंग सॅंपल्स - Phi-4 सॅंपल्स 🆕 - [📓] [तंत्रज्ञान पत्रकार म्हणून Phi-4-multimodal वापरणे](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb) - [Phi-4-multimodal वापरून प्रतिमा विश्लेषणासाठी .NET कन्सोल अनुप्रयोग](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) - फाईन-ट्यूनिंग Phi सॅंपल्स - [फाईन-ट्यूनिंग परिस्थिती](./md/03.FineTuning/FineTuning_Scenarios.md) - [फाईन-ट्यूनिंग विरुद्ध RAG](./md/03.FineTuning/FineTuning_vs_RAG.md) - [Phi-3 ला उद्योग तज्ञ बनवण्यासाठी फाईन-ट्यूनिंग](./md/03.FineTuning/LetPhi3gotoIndustriy.md) - [VS Code साठी AI टूलकिट वापरून Phi-3 फाईन-ट्युनिंग](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md) - [Azure Machine Learning Service सह Phi-3 फाईन-ट्यूनिंग](./md/03.FineTuning/Introduce_AzureML.md) - [Lora सह Phi-3 फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Lora.md) - [QLora सह Phi-3 फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Qlora.md) - [Microsoft Foundry सह Phi-3 फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_AIFoundry.md) - [Azure ML CLI/SDK सह Phi-3 फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLSDK.md) - [Microsoft Olive सह फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MicrosoftOlive.md) - [Microsoft Olive Hands-On Lab सह फाईन-ट्यूनिंग](./md/03.FineTuning/olive-lab/readme.md) - [Weights and Bias सह Phi-3-vision फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md) - [Apple MLX फ्रेमवर्क सह Phi-3 फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLX.md) - [Phi-3-vision (अधिकृत समर्थन) फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Vision.md) - [Kaito AKS, Azure कंटेनर (अधिकृत समर्थन) सह Phi-3 फाईन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Kaito.md) - [Phi-3 आणि 3.5 Vision फाईन-ट्यूनिंग](https://github.com/2U1/Phi3-Vision-Finetune) - Hands on Lab - [आधुनिक मॉडेल्स: LLMs, SLMs, स्थानिक विकास आणि अधिक यांचा शोध](https://github.com/microsoft/aitour-exploring-cutting-edge-models) - [NLP क्षमतेचे अनलॉकिंग: Microsoft Olive सह फाईन-ट्यूनिंग](https://github.com/azure/Ignite_FineTuning_workshop) - अकादमिक संशोधन पेपर आणि प्रकाशने - [Textbooks Are All You Need II: phi-1.5 तांत्रिक अहवाल](https://arxiv.org/abs/2309.05463) - [Phi-3 तांत्रिक अहवाल: आपल्याच फोनवर उच्च क्षमतावान भाषा मॉडेल](https://arxiv.org/abs/2404.14219) - [Phi-4 तांत्रिक अहवाल](https://arxiv.org/abs/2412.08905) - [Phi-4-Mini तांत्रिक अहवाल: मिश्रण-ऑफ-LoRAs द्वारे कॉम्पॅक्ट पण शक्तिशाली मल्टीमोडल भाषा मॉडेल्स](https://arxiv.org/abs/2503.01743) - [वाहनामध्ये फंक्शन-कालिंगसाठी लहान भाषा मॉडेल्सचे ऑप्टिमायझेशन](https://arxiv.org/abs/2501.02342) - [(WhyPHI) बहु-विकल्प प्रश्नोत्तरीसाठी PHI-3 ची फाईन-ट्यूनिंग: पद्धतशास्त्र, निकाल आणि आव्हाने](https://arxiv.org/abs/2501.01588) - [Phi-4-Reasoning तांत्रिक अहवाल](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-कारण तांत्रिक अहवाल](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)
# Phi कुकबुक: Microsoft च्या Phi मॉडेल्ससह प्रत्यक्ष उदाहरणे

[![GitHub Codespaces मध्ये नमुने उघडा आणि वापरा](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![Dev Containers मध्ये उघडा](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub योगदानकर्ते](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub समस्या](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub पुल-रिक्वेस्ट](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs स्वागतयोग्य](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub पाहणारे](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub स्टार्स](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi ही Microsoft ने विकसित केलेल्या मुक्त स्रोत AI मॉडेल्सची एक मालिका आहे.

Phi सध्या सर्वात सामर्थ्यशाली आणि खर्चिकदृष्ट्या कार्यक्षम लहान भाषा मॉडेल (SLM) आहे, ज्यात बहुभाषिक, तर्कशक्ति, मजकूर/चॅट निर्मिती, कोडिंग, प्रतिमा, ऑडिओ आणि इतर परिस्थितींमध्ये खूप चांगली मोजमाप आहेत.

आपण Phi ला क्लाउड किंवा एज डिव्हाइसेसवर तैनात करू शकता, आणि मर्यादित संगणकीय शक्तीने सहजपणे जनरेटिव्ह AI अनुप्रयोग तयार करू शकता.

हे संसाधने वापरण्यास सुरुवात करण्यासाठी खालील चरणांचे अनुसरण करा:
1. **रिपॉझिटरी फोर्क करा**: क्लिक करा [![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **रिपॉझिटरी क्लोन करा**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord समुदायात सामील व्हा आणि तज्ञ व सहकार्यांशी भेटा**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/mr/cover.eb18d1b9605d754b.webp)

### 🌐 बहुभाषिक समर्थन

#### GitHub अ‍ॅक्शनद्वारे समर्थित (स्वयंचलित आणि नेहमी अद्ययावत)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरबी](../ar/README.md) | [बंगाली](../bn/README.md) | [बल्गेरियन](../bg/README.md) | [बर्मी (म्यानमार)](../my/README.md) | [चिनी (सरलीकृत)](../zh-CN/README.md) | [चिनी (परंपरागत, हॉंगकॉंग)](../zh-HK/README.md) | [चिनी (परंपरागत, मकाऊ)](../zh-MO/README.md) | [चिनी (परंपरागत, तैवान)](../zh-TW/README.md) | [क्रोएशियन](../hr/README.md) | [चेक](../cs/README.md) | [डॅनिश](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियन](../et/README.md) | [फिन्निश](../fi/README.md) | [फ्रेंच](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिंदी](../hi/README.md) | [हंगेरियन](../hu/README.md) | [इंडोनेशियन](../id/README.md) | [इटालियन](../it/README.md) | [जपानी](../ja/README.md) | [कन्नड](../kn/README.md) | [कोरियन](../ko/README.md) | [लिथुआनियन](../lt/README.md) | [मलय](../ms/README.md) | [मल्याळम](../ml/README.md) | [मराठी](./README.md) | [नेपाली](../ne/README.md) | [नायजेरियन पिडगिन](../pcm/README.md) | [नॉर्वेजियन](../no/README.md) | [फ़ारसी (परसी)](../fa/README.md) | [पोलिश](../pl/README.md) | [पोर्तुगीज (ब्राझील)](../pt-BR/README.md) | [पोर्तुगीज (पोर्तुगाल)](../pt-PT/README.md) | [पंजाबी (गुरमुखी)](../pa/README.md) | [रोमेनियन](../ro/README.md) | [रशियन](../ru/README.md) | [सर्बियन (सिरिलिक)](../sr/README.md) | [स्लोव्हाक](../sk/README.md) | [स्लोव्हेनियन](../sl/README.md) | [स्पॅनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिश](../sv/README.md) | [टगलॉग (फिलिपिनो)](../tl/README.md) | [तमिळ](../ta/README.md) | [तेलुगू](../te/README.md) | [थाई](../th/README.md) | [तुर्की](../tr/README.md) | [युक्रेनियन](../uk/README.md) | [उर्दू](../ur/README.md) | [व्हिएतनामी](../vi/README.md)

> **स्थानिक पद्धतीने क्लोन करायला आवडेल?**
>
> या रिपॉझिटरीमध्ये 50+ भाषा भाषांतर समाविष्ट आहेत ज्यामुळे डाउनलोड आकार लक्षणीय वाढतो. भाषांतरांशिवाय क्लोन करण्यासाठी sparse checkout वापरा:
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
> हे तुम्हाला कोर्स पूर्ण करण्यासाठी आवश्यक सर्व काही देईल आणि डाउनलोड जलद होईल.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## विषय सूची

## Phi मॉडेल्सचा वापर

### Microsoft Foundry वरील Phi

आपण Microsoft Phi कसा वापरायचा आणि आपल्या विविध हार्डवेअर उपकरणांमध्ये E2E सोल्यूशन्स कसे तयार करायचे ते शिकू शकता. स्वतःसाठी Phi अनुभवण्यासाठी, मॉडेल्ससह खेळायला सुरुवात करा आणि आपली परिस्थितींसाठी Phi सानुकूलित करा, तसेच [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) वापरा. [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) सह सुरू करण्याबद्दल अधिक माहिती मिळवा.

**प्लेखाऊंड**
प्रत्येक मॉडेलसाठी समर्पित प्लेखाऊंड आहे जिथे मॉडेलची चाचणी करता येते [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub मॉडेल्सवरील Phi

आपण Microsoft Phi कसा वापरायचा आणि आपल्या विविध हार्डवेअर उपकरणांमध्ये E2E सोल्यूशन्स कसे तयार करायचे ते शिकू शकता. स्वतःसाठी Phi अनुभवण्यासाठी, मॉडेलसह खेळायला सुरुवात करा आणि आपली परिस्थितींसाठी Phi सानुकूलित करा, तसेच [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) वापरा. [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) सह सुरू करण्याबद्दल अधिक माहिती मिळवा.

**प्लेखाऊंड**
प्रत्येक मॉडेलसाठी समर्पित [प्लेखाऊंड आहे जिथे मॉडेलची चाचणी करता येते](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Hugging Face वरील Phi

आपण [Hugging Face](https://huggingface.co/microsoft) वरही मॉडेल शोधू शकता.

**प्लेखाऊंड**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 इतर कोर्सेस

आमची टीम इतर कोर्सेस तयार करते! यावर नजर टाका:

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
 
### जनरेटिव्ह AI मालिका
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)

[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### मुख्य शिक्षण
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### कॉपायलट सिरीज
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## जबाबदार AI 

मायक्रोसॉफ्ट आपल्या ग्राहकांना आमच्या AI उत्पादनांचा जबाबदारीने वापर करण्यास मदत करण्यासाठी, आमच्या शिकवण्या सामायिक करण्यासाठी आणि पारदर्शकता नोट्स आणि परिणाम मूल्यांकनांसारख्या साधनांद्वारे विश्वास-आधारित भागीदारी तयार करण्यासाठी कटिबद्ध आहे. या संसाधनांचे बरेचसे [https://aka.ms/RAI](https://aka.ms/RAI) येथे आढळू शकतात.
जबाबदार AI साठी मायक्रोसॉफ्टची दृष्टीमानता समावेश, पारदर्शकता, विमुक्तता, गोपनीयता आणि सुरक्षा, विश्वासार्हता आणि सुरक्षितता, तसेच जबाबदारीच्या AI तत्त्वांवर आधारित आहे.

या नमुन्यात वापरल्या गेलेल्या मोठ्या प्रमाणावर नैसर्गिक भाषा, प्रतिमा आणि भाषण मॉडेल्स - ज्यांच्या वापरामुळे ते गैरवाजवी, अविश्वसनीय किंवा अपमानास्पद वर्तन करू शकतात, ज्यामुळे हानी होऊ शकते. कृपया धोके आणि मर्यादा याबाबत माहितीसाठी [Azure OpenAI सेवा पारदर्शकता नोट](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) पहा.

या धोके कमी करण्यासाठी शिफारस केलेली पद्धत म्हणजे आपल्या आर्किटेक्चरमध्ये एक सुरक्षा प्रणाली समाविष्ट करणे जी हानिकारक वर्तन ओळखू आणि प्रतिबंधित करू शकेल. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) स्वतंत्र सुरक्षा स्तर प्रदान करते, जी अ‍ॅप्लिकेशन्स आणि सेवांमध्ये हानिकारक वापरकर्ता निर्मित आणि AI-निर्मित सामग्री शोधू शकते. Azure AI Content Safety मध्ये अशा मजकूर आणि प्रतिमा API समाविष्ट आहेत जे हानिकारक सामग्री ओळखण्यास मदत करतात. Microsoft Foundry मध्ये, कंटेंट सेफ्टी सेवा विविध प्रकारांमध्ये हानिकारक सामग्री शोधण्यासाठी नमुना कोड पाहण्याची, एक्सप्लोर करण्याची आणि प्रयत्न करण्याची सुविधा देते. पुढील [जलद प्रारंभ दस्तऐवज](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) आपणाला सेवेवर विनंत्या करण्यास मार्गदर्शन करतो.

दुसरी बाब म्हणजे एकूण अॅप्लिकेशन कार्यक्षमता लक्षात घेणे. बहु-मोडल आणि बहु-मॉडेल्स अॅप्लिकेशन्ससह, कार्यक्षमता म्हणजे प्रणाली आपण आणि आपले वापरकर्ते जशी अपेक्षा करतात तसे कार्य करते, ज्यात हानिकारक परिणाम तयार न करणे याचा समावेश आहे. आपली एकूण अॅप्लिकेशन कार्यक्षमता [कार्यक्षमता आणि गुणवत्ता तसेच धोका आणि सुरक्षितता मूल्यांकन करणाऱ्यांचा वापर करून](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) तपासणे महत्त्वाचे आहे. तसेच आपण [सानुकूल मूल्यांकन करणारे](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) तयार आणि वापरू शकता.

आपण आपल्या AI अॅप्लिकेशनचा विकास वातावरणात [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) वापरून मूल्यमापन करू शकता. डेटा साठा किंवा लक्ष्य असो, आपल्या जनरेटिव्ह AI अॅप्लिकेशनच्या निर्मितीची मोजणी अंतर्निर्मित मूल्यांकन करणाऱ्या किंवा आपल्या पसंतीच्या सानुकूल मूल्यांकन करणाऱ्यांद्वारे संख्याशास्त्रीय केली जाते. आपल्या प्रणालीचे मूल्यमापन करण्यासाठी azure ai evaluation sdk सह सुरुवात करण्यासाठी, आपण [जलद प्रारंभ मार्गदर्शक](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) अनुसरू शकता. एक वेळ मूल्यमापन चालविल्यानंतर, आपण [Microsoft Foundry मध्ये निकालांचे दृश्यांकन](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) करू शकता.

## ट्रेडमार्क

हा प्रकल्प प्रकल्प, उत्पादने किंवा सेवा यांचे ट्रेडमार्क किंवा लोगो असू शकतो. Microsoft ट्रेडमार्क किंवा लोगोचा अधिकृत वापर [Microsoft च्या ट्रेडमार्क आणि ब्रँड मार्गदर्शक तत्त्वांचे](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) पालन करणे आवश्यक आहे.
या प्रकल्पाच्या सुधारित आवृत्त्यांमध्ये Microsoft ट्रेडमार्क किंवा लोगो वापरल्यास भ्रम टाळावा किंवा Microsoft अधिकृतपणा दर्शवू नये. तृतीय-पक्ष ट्रेडमार्क किंवा लोगो वापर तृतीय-पक्षाच्या धोरणांनुसार असणार आहे.

## मदत मिळवा

आपण अडकलात किंवा AI अ‍ॅप्स तयार करताना काही प्रश्न असतील तर सामील व्हा:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

आपल्याकडे उत्पादन अभिप्राय किंवा तयार करताना त्रुटी असल्यास भेट द्या:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा तंतोतंत नसणे संभव आहे. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्त्रोत मानावा. महत्त्वाची माहिती मिळवण्यासाठी व्यावसायिक मानवी अनुवाद शिफारस करण्यात येतो. या अनुवादाच्या वापरामुळे होणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थाने आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->