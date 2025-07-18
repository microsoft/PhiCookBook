<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c07bb4c3c89a36c9be332a065a9a33c",
  "translation_date": "2025-07-16T15:04:39+00:00",
  "source_file": "README.md",
  "language_code": "mr"
}
-->
# Phi Cookbook: Microsoft च्या Phi मॉडेल्ससह प्रत्यक्ष उदाहरणे

[![GitHub Codespaces मध्ये नमुने उघडा आणि वापरा](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![Dev Containers मध्ये उघडा](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![GitHub योगदानकर्ते](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub समस्या](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub पुल-रिक्वेस्ट्स](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub वॉचर्स](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![GitHub स्टार्स](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi ही Microsoft द्वारे विकसित केलेली एक ओपन सोर्स AI मॉडेल्सची मालिका आहे.

Phi सध्या सर्वात शक्तिशाली आणि किफायतशीर लहान भाषा मॉडेल (SLM) आहे, ज्याला बहुभाषिक, तर्कशास्त्र, मजकूर/चॅट जनरेशन, कोडिंग, प्रतिमा, ऑडिओ आणि इतर अनेक परिस्थितींमध्ये उत्कृष्ट कामगिरी मिळाली आहे.

तुम्ही Phi ला क्लाउडवर किंवा एज डिव्हाइसेसवर तैनात करू शकता, आणि मर्यादित संगणकीय शक्तीने सहजपणे जनरेटिव्ह AI अनुप्रयोग तयार करू शकता.

हे स्त्रोत वापरण्यास सुरुवात करण्यासाठी खालील पायऱ्या फॉलो करा:  
1. **रिपॉझिटरी फोर्क करा**: क्लिक करा [![GitHub फोर्क्स](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **रिपॉझिटरी क्लोन करा**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Microsoft AI Discord Community मध्ये सामील व्हा आणि तज्ञ व इतर विकसकांशी भेटा**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.mr.png)

### 🌐 बहुभाषिक समर्थन

#### GitHub Action द्वारे समर्थित (स्वयंचलित आणि नेहमी अद्ययावत)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md)  
[Bengali](../bn/README.md) | [Marathi](./README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)

## अनुक्रमणिका

- परिचय  
  - [Phi कुटुंबात आपले स्वागत आहे](./md/01.Introduction/01/01.PhiFamily.md)  
  - [आपले वातावरण सेट करणे](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [महत्त्वाच्या तंत्रज्ञानांची समज](./md/01.Introduction/01/01.Understandingtech.md)  
  - [Phi मॉडेल्ससाठी AI सुरक्षा](./md/01.Introduction/01/01.AISafety.md)  
  - [Phi हार्डवेअर समर्थन](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [Phi मॉडेल्स आणि प्लॅटफॉर्मवर उपलब्धता](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [Guidance-ai आणि Phi चा वापर](./md/01.Introduction/01/01.Guidance.md)  
  - [GitHub मार्केटप्लेस मॉडेल्स](https://github.com/marketplace/models)  
  - [Azure AI मॉडेल कॅटलॉग](https://ai.azure.com)

- विविध वातावरणात Phi चे इन्फरन्स  
  - [Hugging face](./md/01.Introduction/02/01.HF.md)  
  - [GitHub मॉडेल्स](./md/01.Introduction/02/02.GitHubModel.md)  
  - [Azure AI Foundry Model Catalog](./md/01.Introduction/02/03.AzureAIFoundry.md)  
  - [Ollama](./md/01.Introduction/02/04.Ollama.md)  
  - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
  - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)  
  - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi कुटुंबाचा इन्फरन्स  
  - [iOS मध्ये Phi चे इन्फरन्स](./md/01.Introduction/03/iOS_Inference.md)  
  - [Android मध्ये Phi चे इन्फरन्स](./md/01.Introduction/03/Android_Inference.md)  
  - [Jetson मध्ये Phi चे इन्फरन्स](./md/01.Introduction/03/Jetson_Inference.md)  
  - [AI PC मध्ये Phi चे इन्फरन्स](./md/01.Introduction/03/AIPC_Inference.md)  
  - [Apple MLX Framework सह Phi चे इन्फरन्स](./md/01.Introduction/03/MLX_Inference.md)  
  - [स्थानिक सर्व्हरमध्ये Phi चे इन्फरन्स](./md/01.Introduction/03/Local_Server_Inference.md)  
  - [AI Toolkit वापरून रिमोट सर्व्हरमध्ये Phi चे इन्फरन्स](./md/01.Introduction/03/Remote_Interence.md)  
  - [Rust सह Phi चे इन्फरन्स](./md/01.Introduction/03/Rust_Inference.md)  
  - [स्थानिक Vision मध्ये Phi चे इन्फरन्स](./md/01.Introduction/03/Vision_Inference.md)  
  - [Kaito AKS, Azure Containers (अधिकृत समर्थन) सह Phi चे इन्फरन्स](./md/01.Introduction/03/Kaito_Inference.md)  
- [Phi कुटुंबाचे क्वांटिफायिंग](./md/01.Introduction/04/QuantifyingPhi.md)  
  - [llama.cpp वापरून Phi-3.5 / 4 चे क्वांटायझेशन](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
  - [onnxruntime साठी Generative AI विस्तार वापरून Phi-3.5 / 4 चे क्वांटायझेशन](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
  - [Intel OpenVINO वापरून Phi-3.5 / 4 चे क्वांटायझेशन](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
  - [Apple MLX Framework वापरून Phi-3.5 / 4 चे क्वांटायझेशन](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi चे मूल्यांकन  
  - [Responsible AI](./md/01.Introduction/05/ResponsibleAI.md)  
  - [Azure AI Foundry द्वारे मूल्यांकन](./md/01.Introduction/05/AIFoundry.md)  
  - [Promptflow वापरून मूल्यांकन](./md/01.Introduction/05/Promptflow.md)

- Azure AI Search सह RAG  
  - [Phi-4-mini आणि Phi-4-multimodal (RAG) Azure AI Search सह कसे वापरायचे](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi अनुप्रयोग विकास नमुने  
  - मजकूर आणि चॅट अनुप्रयोग  
    - Phi-4 नमुने 🆕  
      - [📓] [Phi-4-mini ONNX मॉडेलसह चॅट](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Phi-4 स्थानिक ONNX मॉडेलसह चॅट .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [Semantic Kernel वापरून Phi-4 ONNX सह .NET कन्सोल अॅपमध्ये चॅट](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Phi-3 / 3.5 नमुने  
      - [Phi3, ONNX Runtime Web आणि WebGPU वापरून ब्राउझरमध्ये स्थानिक चॅटबॉट](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [OpenVino चॅट](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [मल्टी मॉडेल - इंटरऐक्टिव्ह Phi-3-mini आणि OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - Phi-3 सह रॅपर तयार करणे आणि MLFlow वापरणे](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [मॉडेल ऑप्टिमायझेशन - ONNX Runtime Web साठी Phi-3-min मॉडेल कसे ऑप्टिमाइझ करायचे Olive वापरून](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [WinUI3 अॅप Phi-3 mini-4k-instruct-onnx सह](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [WinUI3 मल्टी मॉडेल AI पॉवर्ड नोट्स अॅप नमुना](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Prompt flow सह सानुकूल Phi-3 मॉडेल्सचे फाइन-ट्यूनिंग आणि एकत्रीकरण](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Azure AI Foundry मध्ये Prompt flow सह सानुकूल Phi-3 मॉडेल्सचे फाइन-ट्यूनिंग आणि एकत्रीकरण](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Microsoft च्या जबाबदार AI तत्त्वांवर लक्ष केंद्रित करून Azure AI Foundry मध्ये फाइन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलचे मूल्यांकन](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct भाषा भाकीत नमुना (चिनी/इंग्रजी)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG चॅटबॉट](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU वापरून Phi-3.5-Instruct ONNX सह Prompt flow सोल्यूशन तयार करणे](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tflite वापरून Android अॅप तयार करणे](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Microsoft.ML.OnnxRuntime वापरून स्थानिक ONNX Phi-3 मॉडेलसह Q&A .NET उदाहरण](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Semantic Kernel आणि Phi-3 सह Console चॅट .NET अॅप](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK कोड आधारित नमुने  
  - Phi-4 नमुने 🆕  
    - [📓] [Phi-4-multimodal वापरून प्रोजेक्ट कोड तयार करणे](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Phi-3 / 3.5 नमुने  
    - [Microsoft Phi-3 कुटुंबासह आपला स्वतःचा Visual Studio Code GitHub Copilot Chat तयार करा](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [GitHub मॉडेल्स वापरून Phi-3.5 सह आपला स्वतःचा Visual Studio Code Chat Copilot एजंट तयार करा](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- प्रगत तर्क नमुने  
  - Phi-4 नमुने 🆕  
    - [📓] [Phi-4-mini-reasoning किंवा Phi-4-reasoning नमुने](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Microsoft Olive सह Phi-4-mini-reasoning चे फाइन-ट्यूनिंग](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Apple MLX सह Phi-4-mini-reasoning चे फाइन-ट्यूनिंग](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [GitHub मॉडेल्ससह Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Azure AI Foundry मॉडेल्ससह Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- डेमो  
    - [Hugging Face Spaces वर होस्ट केलेले Phi-4-mini डेमो](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Hugging Face Spaces वर होस्ट केलेले Phi-4-multimodal डेमो](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- व्हिजन नमुने  
  - Phi-4 नमुने 🆕  
    - [📓] [Phi-4-multimodal वापरून प्रतिमा वाचणे आणि कोड तयार करणे](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Phi-3 / 3.5 नमुने  
    - [📓][Phi-3-vision-प्रतिमा मजकूर ते मजकूर](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP एम्बेडिंग](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [डेमो: Phi-3 रीसायक्लिंग](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - व्हिज्युअल भाषा सहाय्यक - Phi3-Vision आणि OpenVINO सह](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision मल्टी-फ्रेम किंवा मल्टी-इमेज नमुना](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Microsoft.ML.OnnxRuntime .NET वापरून Phi-3 Vision स्थानिक ONNX मॉडेल](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [मेनू आधारित Phi-3 Vision स्थानिक ONNX मॉडेल Microsoft.ML.OnnxRuntime .NET वापरून](../../md/04.HOL/dotnet/src/LabsPhi304)  

- गणित नमुने  
  - Phi-4-Mini-Flash-Reasoning-Instruct नमुने 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct सह गणित डेमो](../../md/02.Application/09.Math/MathDemo.ipynb)  

- ऑडिओ नमुने  
  - Phi-4 नमुने 🆕  
    - [📓] [Phi-4-multimodal वापरून ऑडिओ ट्रान्सक्रिप्ट्स काढणे](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Phi-4-multimodal ऑडिओ नमुना](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Phi-4-multimodal स्पीच ट्रान्सलेशन नमुना](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [Phi-4-multimodal वापरून ऑडिओ फाइलचे विश्लेषण आणि ट्रान्सक्रिप्ट तयार करणारे .NET कन्सोल अॅप्लिकेशन](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- MOE नमुने  
  - Phi-3 / 3.5 नमुने  
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) सोशल मीडिया नमुना](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, आणि LlamaIndex सह Retrieval-Augmented Generation (RAG) पाइपलाइन तयार करणे](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- फंक्शन कॉलिंग नमुने  
  - Phi-4 नमुने 🆕  
    - [📓] [Phi-4-mini सह फंक्शन कॉलिंग वापरणे](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Phi-4-mini सह मल्टी-एजंट तयार करण्यासाठी फंक्शन कॉलिंग वापरणे](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Ollama सह फंक्शन कॉलिंग वापरणे](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [ONNX सह फंक्शन कॉलिंग वापरणे](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- मल्टीमोडल मिक्सिंग नमुने  
  - Phi-4 नमुने 🆕  
    - [📓] [तंत्रज्ञान पत्रकार म्हणून Phi-4-multimodal वापरणे](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [Phi-4-multimodal वापरून प्रतिमा विश्लेषण करणारे .NET कन्सोल अॅप्लिकेशन](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Phi फाइन-ट्यूनिंग  
  - [फाइन-ट्यूनिंग परिस्थिती](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [फाइन-ट्यूनिंग विरुद्ध RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Phi-3 ला उद्योग तज्ञ बनविण्यासाठी फाइन-ट्यूनिंग](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [VS Code साठी AI Toolkit वापरून Phi-3 चे फाइन-ट्यूनिंग](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Azure Machine Learning Service सह Phi-3 चे फाइन-ट्यूनिंग](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Lora सह Phi-3 चे फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Lora.md)  
  - [QLora सह Phi-3 चे फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Azure AI Foundry सह Phi-3 चे फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Azure ML CLI/SDK सह Phi-3 चे फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Microsoft Olive सह फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Microsoft Olive Hands-On Lab सह फाइन-ट्यूनिंग](./md/03.FineTuning/olive-lab/readme.md)  
  - [Weights and Bias सह Phi-3-vision चे फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Apple MLX Framework सह Phi-3 चे फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Phi-3-vision चे फाइन-ट्यूनिंग (अधिकृत समर्थन)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Kaito AKS, Azure Containers सह Phi-3 चे फाइन-ट्यूनिंग (अधिकृत समर्थन)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Phi-3 आणि 3.5 Vision चे फाइन-ट्यूनिंग](https://github.com/2U1/Phi3-Vision-Finetune)  

- Hands on Lab  
  - [आधुनिक मॉडेल्सचा अभ्यास: LLMs, SLMs, स्थानिक विकास आणि बरेच काही](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [NLP क्षमता अनलॉक करणे: Microsoft Olive सह फाइन-ट्यूनिंग](https://github.com/azure/Ignite_FineTuning_workshop)  

- शैक्षणिक संशोधन पेपर्स आणि प्रकाशने  
  - [Textbooks Are All You Need II: phi-1.5 तांत्रिक अहवाल](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 तांत्रिक अहवाल: तुमच्या फोनवर स्थानिकपणे एक अत्यंत सक्षम भाषा मॉडेल](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 तांत्रिक अहवाल](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini तांत्रिक अहवाल: Mixture-of-LoRAs द्वारे कॉम्पॅक्ट पण शक्तिशाली मल्टीमोडल भाषा मॉडेल्स](https://arxiv.org/abs/2503.01743)  
  - [वाहनातील फंक्शन-कॉलिंगसाठी लहान भाषा मॉडेल्सचे ऑप्टिमायझेशन](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) बहुविकल्पीय प्रश्नोत्तरेसाठी PHI-3 चे फाइन-ट्यूनिंग: पद्धतशास्त्र, निकाल आणि आव्हाने](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning Technical Report](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [Phi-4-mini-reasoning Technical Report](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi मॉडेल्सचा वापर

### Azure AI Foundry वरील Phi

Microsoft Phi कसा वापरायचा आणि तुमच्या विविध हार्डवेअर उपकरणांमध्ये E2E सोल्यूशन्स कसे तयार करायचे हे तुम्ही शिकू शकता. स्वतःसाठी Phi अनुभवण्यासाठी, आधी मॉडेल्ससह प्रयोग करा आणि तुमच्या परिस्थितींसाठी Phi सानुकूलित करा, [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) वापरून. अधिक जाणून घेण्यासाठी [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) या मार्गदर्शकाचा अभ्यास करा.

**प्लेलँड**
प्रत्येक मॉडेलसाठी त्याचं स्वतःचं प्लेलँड आहे जिथे तुम्ही मॉडेलची चाचणी करू शकता [Azure AI Playground](https://aka.ms/try-phi3).

### GitHub मॉडेल्सवरील Phi

Microsoft Phi कसा वापरायचा आणि तुमच्या विविध हार्डवेअर उपकरणांमध्ये E2E सोल्यूशन्स कसे तयार करायचे हे तुम्ही शिकू शकता. स्वतःसाठी Phi अनुभवण्यासाठी, आधी मॉडेलसह प्रयोग करा आणि तुमच्या परिस्थितींसाठी Phi सानुकूलित करा, [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) वापरून. अधिक जाणून घेण्यासाठी [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) या मार्गदर्शकाचा अभ्यास करा.

**प्लेलँड**
प्रत्येक मॉडेलसाठी त्याचं स्वतःचं [प्लेलँड आहे जिथे तुम्ही मॉडेलची चाचणी करू शकता](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Hugging Face वरील Phi

तुम्हाला हा मॉडेल [Hugging Face](https://huggingface.co/microsoft) वरही सापडेल.

**प्लेलँड**
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## जबाबदार AI

Microsoft आमच्या ग्राहकांना आमची AI उत्पादने जबाबदारीने वापरण्यास मदत करण्यासाठी, आमच्या शिकवण्या शेअर करण्यासाठी आणि Transparency Notes आणि Impact Assessments सारख्या साधनांद्वारे विश्वासावर आधारित भागीदारी तयार करण्यासाठी कटिबद्ध आहे. या संसाधनांपैकी बरेच काही [https://aka.ms/RAI](https://aka.ms/RAI) येथे उपलब्ध आहेत.  
Microsoft चा जबाबदार AI कडे दृष्टिकोन आमच्या AI तत्त्वांवर आधारित आहे ज्यात न्याय, विश्वासार्हता आणि सुरक्षितता, गोपनीयता आणि सुरक्षा, समावेश, पारदर्शकता आणि जबाबदारी यांचा समावेश आहे.

मोठ्या प्रमाणावर नैसर्गिक भाषा, प्रतिमा आणि भाषण मॉडेल्स - जसे की या नमुन्यात वापरलेले - कधीकधी अन्यायकारक, अविश्वसनीय किंवा अपमानास्पद वर्तन करू शकतात, ज्यामुळे हानी होऊ शकते. कृपया धोके आणि मर्यादा जाणून घेण्यासाठी [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) पहा.

या धोके कमी करण्यासाठी शिफारस केलेला उपाय म्हणजे तुमच्या आर्किटेक्चरमध्ये एक सुरक्षा प्रणाली समाविष्ट करणे जी हानिकारक वर्तन ओळखू आणि प्रतिबंधित करू शकेल. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) स्वतंत्र संरक्षणाची एक पातळी प्रदान करते, जी अनुप्रयोगांमध्ये आणि सेवांमध्ये हानिकारक वापरकर्ता-निर्मित आणि AI-निर्मित सामग्री ओळखू शकते. Azure AI Content Safety मध्ये मजकूर आणि प्रतिमा API आहेत जे तुम्हाला हानिकारक सामग्री ओळखण्यास मदत करतात. Azure AI Foundry मध्ये, Content Safety सेवा तुम्हाला वेगवेगळ्या प्रकारच्या हानिकारक सामग्रीचा शोध घेण्यासाठी, तपासण्यासाठी आणि नमुना कोड वापरून प्रयत्न करण्याची परवानगी देते. खालील [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) तुम्हाला या सेवेवर विनंत्या कशा करायच्या हे मार्गदर्शन करते.

दुसरी बाब लक्षात घेण्यासारखी म्हणजे एकूण अनुप्रयोगाची कार्यक्षमता. मल्टी-मोडल आणि मल्टी-मॉडेल्स अनुप्रयोगांसह, कार्यक्षमता म्हणजे प्रणाली तुमच्या आणि तुमच्या वापरकर्त्यांच्या अपेक्षांनुसार कार्य करते, ज्यात हानिकारक आउटपुट तयार न करणे याचा समावेश आहे. तुमच्या एकूण अनुप्रयोगाची कार्यक्षमता [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) वापरून तपासणे महत्त्वाचे आहे. तुम्हाला [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) तयार करण्याची आणि त्यांचा वापर करून मूल्यांकन करण्याचीही संधी आहे.

तुम्ही तुमच्या विकास वातावरणात [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) वापरून तुमच्या AI अनुप्रयोगाचे मूल्यांकन करू शकता. चाचणी डेटासेट किंवा लक्ष्य दिल्यास, तुमच्या जनरेटिव्ह AI अनुप्रयोगाच्या निर्मितींचे प्रमाणात्मक मापन अंगभूत किंवा तुमच्या पसंतीनुसार कस्टम मूल्यांकनकर्त्यांद्वारे केले जाते. तुमच्या प्रणालीचे मूल्यांकन करण्यासाठी Azure AI Evaluation SDK वापरण्यास सुरुवात करण्यासाठी, तुम्ही [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) अनुसरू शकता. एकदा मूल्यांकन चालवल्यानंतर, तुम्ही [Azure AI Foundry मध्ये निकालांचे दृश्य](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) पाहू शकता.

## ट्रेडमार्क्स

हा प्रकल्प प्रकल्प, उत्पादने किंवा सेवा यांचे ट्रेडमार्क किंवा लोगो असू शकतो. Microsoft ट्रेडमार्क किंवा लोगोचा अधिकृत वापर [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) च्या अटींनुसार आणि त्यांचे पालन करूनच केला जावा.  
या प्रकल्पाच्या सुधारित आवृत्त्यांमध्ये Microsoft ट्रेडमार्क किंवा लोगोचा वापर गोंधळ निर्माण करू नये किंवा Microsoft च्या प्रायोजकत्वाचा भास देऊ नये. तृतीय पक्षांच्या ट्रेडमार्क किंवा लोगोचा वापर त्या तृतीय पक्षांच्या धोरणांनुसार असावा.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.