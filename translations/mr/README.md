<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T13:39:10+00:00",
  "source_file": "README.md",
  "language_code": "mr"
}
-->
# Phi Cookbook: Microsoft च्या Phi मॉडेल्ससह प्रॅक्टिकल उदाहरणे

Phi हे Microsoft द्वारे विकसित केलेले ओपन सोर्स AI मॉडेल्सचे एक मालिक आहे.

Phi सध्या सर्वात शक्तिशाली आणि किफायतशीर लहान भाषा मॉडेल (SLM) आहे, ज्यामध्ये बहुभाषिक, तर्कशास्त्र, मजकूर/चॅट निर्मिती, कोडिंग, प्रतिमा, ऑडिओ आणि इतर परिस्थितींमध्ये उत्कृष्ट बेंचमार्क आहेत.

तुम्ही Phi क्लाउडवर किंवा एज डिव्हाइसवर तैनात करू शकता आणि मर्यादित संगणकीय शक्तीने सहजपणे जनरेटिव्ह AI अनुप्रयोग तयार करू शकता.

या संसाधनांचा वापर सुरू करण्यासाठी खालील चरणांचे अनुसरण करा:
1. **रेपॉझिटरी फोर्क करा**: क्लिक करा [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **रेपॉझिटरी क्लोन करा**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord समुदायामध्ये सामील व्हा आणि तज्ञ व इतर विकसकांशी भेटा**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 बहुभाषिक समर्थन

#### GitHub Action द्वारे समर्थित (स्वयंचलित आणि नेहमी अद्ययावत)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) 
[Bengali](../bn/README.md) | [Marathi](./README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)

## विषय सूची

- परिचय
  - [Phi कुटुंबामध्ये आपले स्वागत आहे](./md/01.Introduction/01/01.PhiFamily.md)
  - [आपले वातावरण सेट करणे](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [महत्त्वाच्या तंत्रज्ञानाची समज](./md/01.Introduction/01/01.Understandingtech.md)
  - [Phi मॉडेल्ससाठी AI सुरक्षा](./md/01.Introduction/01/01.AISafety.md)
  - [Phi हार्डवेअर समर्थन](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Phi मॉडेल्स आणि प्लॅटफॉर्म्सवरील उपलब्धता](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Guidance-ai आणि Phi वापरणे](./md/01.Introduction/01/01.Guidance.md)
  - [GitHub मार्केटप्लेस मॉडेल्स](https://github.com/marketplace/models)
  - [Azure AI मॉडेल कॅटलॉग](https://ai.azure.com)

- विविध वातावरणात Phi चा उपयोग
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [GitHub मॉडेल्स](./md/01.Introduction/02/02.GitHubModel.md)
    - [Azure AI Foundry मॉडेल कॅटलॉग](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi कुटुंबाचा उपयोग
    - [iOS मध्ये Phi चा उपयोग](./md/01.Introduction/03/iOS_Inference.md)
    - [Android मध्ये Phi चा उपयोग](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson मध्ये Phi चा उपयोग](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC मध्ये Phi चा उपयोग](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework सह Phi चा उपयोग](./md/01.Introduction/03/MLX_Inference.md)
    - [स्थानिक सर्व्हरमध्ये Phi चा उपयोग](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit वापरून रिमोट सर्व्हरमध्ये Phi चा उपयोग](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust सह Phi चा उपयोग](./md/01.Introduction/03/Rust_Inference.md)
    - [स्थानिक Vision सह Phi चा उपयोग](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers सह Phi चा उपयोग (अधिकृत समर्थन)](./md/01.Introduction/03/Kaito_Inference.md)

- [Phi कुटुंबाचे प्रमाणित करणे](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp वापरून Phi-3.5 / 4 चे क्वांटायझेशन](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime साठी जनरेटिव्ह AI विस्तार वापरून Phi-3.5 / 4 चे क्वांटायझेशन](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO वापरून Phi-3.5 / 4 चे क्वांटायझेशन](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework वापरून Phi-3.5 / 4 चे क्वांटायझेशन](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Phi चे मूल्यांकन
    - [उत्तरदायी AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [मूल्यांकनासाठी Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [मूल्यांकनासाठी Promptflow वापरणे](./md/01.Introduction/05/Promptflow.md)

- Azure AI Search सह RAG
    - [Phi-4-mini आणि Phi-4-multimodal (RAG) Azure AI Search सह कसे वापरायचे](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Phi अनुप्रयोग विकास नमुने
  - मजकूर आणि चॅट अनुप्रयोग
    - Phi-4 नमुने 🆕
      - [📓] [Phi-4-mini ONNX मॉडेलसह चॅट करा](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Phi-4 स्थानिक ONNX मॉडेल .NET सह चॅट करा](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Phi-4 ONNX सह .NET कन्सोल अॅप, सिमेंटिक कर्नल वापरून चॅट करा](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 नमुने
      - [Phi3, ONNX Runtime Web आणि WebGPU वापरून ब्राउझरमध्ये स्थानिक चॅटबॉट](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino चॅट](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [मल्टी मॉडेल - Phi-3-mini आणि OpenAI Whisper सह संवादात्मक](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Wrapper तयार करणे आणि Phi-3 सह MLFlow वापरणे](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [मॉडेल ऑप्टिमायझेशन - Olive सह ONNX Runtime Web साठी Phi-3-min मॉडेल कसे ऑप्टिमाइझ करावे](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Phi-3 mini-4k-instruct-onnx सह WinUI3 अॅप](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [WinUI3 मल्टी मॉडेल AI पॉवर्ड नोट्स अॅप नमुना](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Phi-3 मॉडेल्सचे फाइन-ट्यूनिंग आणि Prompt flow सह एकत्रीकरण](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)  
- [Azure AI Foundry मध्ये Phi-3 मॉडेल्सचे फाइन-ट्यूनिंग आणि Prompt flow सह एकत्रीकरण](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)  
- [Microsoft च्या Responsible AI Principles वर लक्ष केंद्रित करून Azure AI Foundry मध्ये फाइन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलचे मूल्यांकन](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)  
- [📓] [Phi-3.5-mini-instruct भाषा अंदाज नमुना (चिनी/इंग्रजी)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)  
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)  
- [Windows GPU वापरून Phi-3.5-Instruct ONNX सह Prompt flow सोल्यूशन तयार करणे](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)  
- [Microsoft Phi-3.5 tflite वापरून Android अॅप तयार करणे](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)  
- [Microsoft.ML.OnnxRuntime वापरून स्थानिक ONNX Phi-3 मॉडेलसह Q&A .NET उदाहरण](../../md/04.HOL/dotnet/src/LabsPhi301)  
- [Semantic Kernel आणि Phi-3 सह Console chat .NET अॅप](../../md/04.HOL/dotnet/src/LabsPhi302)  

- Azure AI Inference SDK कोड आधारित नमुने  
  - Phi-4 नमुने 🆕  
    - [📓] [Phi-4-multimodal वापरून प्रोजेक्ट कोड तयार करणे](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Phi-3 / 3.5 नमुने  
    - [Microsoft Phi-3 Family सह Visual Studio Code GitHub Copilot Chat तयार करा](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [Phi-3.5 वापरून GitHub Models सह Visual Studio Code Chat Copilot Agent तयार करा](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- Advanced Reasoning नमुने  
  - Phi-4 नमुने 🆕  
    - [📓] [Phi-4-mini-reasoning किंवा Phi-4-reasoning नमुने](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Microsoft Olive सह Phi-4-mini-reasoning फाइन-ट्यून करणे](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Apple MLX सह Phi-4-mini-reasoning फाइन-ट्यून करणे](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [GitHub Models सह Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Azure AI Foundry Models सह Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- डेमो  
    - [Hugging Face Spaces वर होस्ट केलेले Phi-4-mini डेमो](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Hugging Face Spaces वर होस्ट केलेले Phi-4-multimodal डेमो](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- Vision नमुने  
  - Phi-4 नमुने 🆕  
    - [📓] [Phi-4-multimodal वापरून प्रतिमा वाचणे आणि कोड तयार करणे](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Phi-3 / 3.5 नमुने  
    - [📓][Phi-3-vision-प्रतिमा मजकूर ते मजकूर](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - Visual language assistant - Phi3-Vision आणि OpenVINO सह](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision मल्टी-फ्रेम किंवा मल्टी-प्रतिमा नमुना](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Microsoft.ML.OnnxRuntime .NET वापरून स्थानिक ONNX मॉडेलसह Phi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Microsoft.ML.OnnxRuntime .NET वापरून मेनू आधारित स्थानिक ONNX मॉडेलसह Phi-3 Vision](../../md/04.HOL/dotnet/src/LabsPhi304)  

- गणित नमुने  
  - Phi-4-Mini-Flash-Reasoning-Instruct नमुने 🆕 [Phi-4-Mini-Flash-Reasoning-Instruct सह गणित डेमो](../../md/02.Application/09.Math/MathDemo.ipynb)  

- ऑडिओ नमुने  
  - Phi-4 नमुने 🆕  
    - [📓] [Phi-4-multimodal वापरून ऑडिओ ट्रान्सक्रिप्ट्स काढणे](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Phi-4-multimodal ऑडिओ नमुना](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Phi-4-multimodal भाषण अनुवाद नमुना](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [.NET console application वापरून Phi-4-multimodal ऑडिओसह ऑडिओ फाइलचे विश्लेषण आणि ट्रान्सक्रिप्ट तयार करणे](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- MOE नमुने  
  - Phi-3 / 3.5 नमुने  
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) सोशल मीडिया नमुना](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, आणि LlamaIndex सह Retrieval-Augmented Generation (RAG) Pipeline तयार करणे](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- फंक्शन कॉलिंग नमुने  
  - Phi-4 नमुने 🆕  
    - [📓] [Phi-4-mini सह फंक्शन कॉलिंग वापरणे](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Phi-4-mini सह मल्टी-एजंट्स तयार करण्यासाठी फंक्शन कॉलिंग वापरणे](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Ollama सह फंक्शन कॉलिंग वापरणे](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [ONNX सह फंक्शन कॉलिंग वापरणे](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- मल्टीमोडल मिक्सिंग नमुने  
  - Phi-4 नमुने 🆕  
    - [📓] [Phi-4-multimodal वापरून तंत्रज्ञान पत्रकार म्हणून काम करणे](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [.NET console application वापरून Phi-4-multimodal सह प्रतिमांचे विश्लेषण करणे](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Phi नमुने फाइन-ट्यूनिंग  
  - [फाइन-ट्यूनिंग परिस्थिती](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [फाइन-ट्यूनिंग vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Phi-3 ला उद्योग तज्ञ बनवण्यासाठी फाइन-ट्यूनिंग](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [VS Code साठी AI Toolkit सह Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Azure Machine Learning Service सह Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Lora सह Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Lora.md)  
  - [QLora सह Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Azure AI Foundry सह Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Azure ML CLI/SDK सह Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Microsoft Olive सह फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Microsoft Olive Hands-On Lab सह फाइन-ट्यूनिंग](./md/03.FineTuning/olive-lab/readme.md)  
  - [Weights and Bias सह Phi-3-vision फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Apple MLX Framework सह Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Phi-3-vision (अधिकृत समर्थन) सह फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Kaito AKS, Azure Containers (अधिकृत समर्थन) सह Phi-3 फाइन-ट्यूनिंग](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Phi-3 आणि 3.5 Vision सह फाइन-ट्यूनिंग](https://github.com/2U1/Phi3-Vision-Finetune)  

- Hands on Lab  
  - [आधुनिक मॉडेल्स एक्सप्लोर करणे: LLMs, SLMs, स्थानिक विकास आणि अधिक](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [NLP क्षमता अनलॉक करणे: Microsoft Olive सह फाइन-ट्यूनिंग](https://github.com/azure/Ignite_FineTuning_workshop)  

- शैक्षणिक संशोधन पेपर्स आणि प्रकाशने  
  - [Textbooks Are All You Need II: phi-1.5 तांत्रिक अहवाल](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 तांत्रिक अहवाल: तुमच्या फोनवर स्थानिकपणे अत्यंत सक्षम भाषा मॉडेल](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 तांत्रिक अहवाल](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini तांत्रिक अहवाल: Mixture-of-LoRAs द्वारे कॉम्पॅक्ट परंतु शक्तिशाली मल्टीमोडल भाषा मॉडेल्स](https://arxiv.org/abs/2503.01743)  
  - [In-Vehicle Function-Calling साठी लहान भाषा मॉडेल्स ऑप्टिमाइझ करणे](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) Phi-3 साठी Multiple-Choice Question Answering फाइन-ट्यूनिंग: पद्धतशास्त्र, परिणाम, आणि आव्हाने](https://arxiv.org/abs/2501.01588)  
- [Phi-4-reasoning तांत्रिक अहवाल](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning तांत्रिक अहवाल](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)  

## Phi मॉडेल्सचा वापर  

### Azure AI Foundry वर Phi  

आपण Microsoft Phi कसा वापरायचा आणि आपल्या विविध हार्डवेअर उपकरणांमध्ये E2E सोल्यूशन्स कसे तयार करायचे हे शिकू शकता. Phi स्वतः अनुभवण्यासाठी, मॉडेल्ससह खेळून आणि आपल्या परिस्थितीनुसार Phi सानुकूलित करून सुरुवात करा. [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) येथे अधिक जाणून घ्या. [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) सह सुरुवात करण्यासाठी मार्गदर्शक पहा.  

**Playground**  
प्रत्येक मॉडेलसाठी मॉडेलची चाचणी घेण्यासाठी समर्पित प्लेग्राउंड आहे [Azure AI Playground](https://aka.ms/try-phi3).  

### GitHub मॉडेल्सवर Phi  

आपण Microsoft Phi कसा वापरायचा आणि आपल्या विविध हार्डवेअर उपकरणांमध्ये E2E सोल्यूशन्स कसे तयार करायचे हे शिकू शकता. Phi स्वतः अनुभवण्यासाठी, मॉडेलसह खेळून आणि आपल्या परिस्थितीनुसार Phi सानुकूलित करून सुरुवात करा. [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) येथे अधिक जाणून घ्या. [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) सह सुरुवात करण्यासाठी मार्गदर्शक पहा.  

**Playground**  
प्रत्येक मॉडेलसाठी [मॉडेलची चाचणी घेण्यासाठी समर्पित प्लेग्राउंड आहे](/md/02.QuickStart/GitHubModel_QuickStart.md).  

### Hugging Face वर Phi  

आपण मॉडेल [Hugging Face](https://huggingface.co/microsoft) वर देखील शोधू शकता.  

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)  

## जबाबदार AI  

Microsoft आपल्या ग्राहकांना आमची AI उत्पादने जबाबदारीने वापरण्यास मदत करण्यासाठी, आमचे अनुभव सामायिक करण्यासाठी आणि पारदर्शकता नोट्स आणि प्रभाव मूल्यांकन यासारख्या साधनांद्वारे विश्वासावर आधारित भागीदारी तयार करण्यासाठी वचनबद्ध आहे. या संसाधनांपैकी बरेच [https://aka.ms/RAI](https://aka.ms/RAI) येथे सापडू शकतात.  
Microsoft चा जबाबदार AI चा दृष्टिकोन आमच्या AI तत्त्वांवर आधारित आहे: न्याय, विश्वासार्हता आणि सुरक्षितता, गोपनीयता आणि सुरक्षा, समावेशकता, पारदर्शकता आणि जबाबदारी.  

प्राकृतिक भाषा, प्रतिमा आणि भाषण यासारख्या मोठ्या प्रमाणातील मॉडेल्स - जसे की या नमुन्यात वापरले जातात - संभाव्यतः अन्यायकारक, अविश्वसनीय किंवा आक्षेपार्ह वर्तन करू शकतात, ज्यामुळे हानी होऊ शकते. जोखीम आणि मर्यादांबद्दल माहिती मिळवण्यासाठी कृपया [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) पहा.  

या जोखमी कमी करण्यासाठी शिफारस केलेला दृष्टिकोन म्हणजे आपल्या आर्किटेक्चरमध्ये एक सुरक्षा प्रणाली समाविष्ट करणे जी हानिकारक वर्तन शोधू आणि रोखू शकते. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) एक स्वतंत्र संरक्षण स्तर प्रदान करते, जो अनुप्रयोग आणि सेवांमध्ये वापरकर्त्याने तयार केलेल्या आणि AI-निर्मित सामग्रीचा शोध घेऊ शकतो. Azure AI Content Safety मध्ये मजकूर आणि प्रतिमा API समाविष्ट आहेत जे हानिकारक सामग्री शोधण्यास अनुमती देतात. Azure AI Foundry मध्ये, Content Safety सेवा आपल्याला विविध प्रकारांमध्ये हानिकारक सामग्री शोधण्यासाठी नमुना कोड पाहण्यास, एक्सप्लोर करण्यास आणि प्रयत्न करण्यास अनुमती देते. [जलद प्रारंभ दस्तऐवज](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) सेवा विनंत्या कशा करायच्या याबद्दल मार्गदर्शन करते.  

एक आणखी महत्त्वाचा पैलू म्हणजे एकूण अनुप्रयोग कार्यक्षमता. मल्टी-मोडल आणि मल्टी-मॉडेल्स अनुप्रयोगांसह, कार्यक्षमता म्हणजे प्रणाली आपल्याला आणि आपल्या वापरकर्त्यांना अपेक्षित आहे तसे कार्य करते, ज्यामध्ये हानिकारक आउटपुट तयार न करणे समाविष्ट आहे. [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) वापरून आपल्या एकूण अनुप्रयोगाची कार्यक्षमता मूल्यांकन करणे महत्त्वाचे आहे. आपल्याला [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) तयार करण्याची आणि मूल्यांकन करण्याची क्षमता देखील आहे.  

आपण आपल्या विकास वातावरणात [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) वापरून आपल्या AI अनुप्रयोगाचे मूल्यांकन करू शकता. दिलेल्या चाचणी डेटासेट किंवा लक्ष्याच्या आधारे, आपले जनरेटिव्ह AI अनुप्रयोग निर्मिती अंगभूत मूल्यांकनकर्ते किंवा आपल्या पसंतीच्या सानुकूल मूल्यांकनकर्त्यांसह प्रमाणात्मकपणे मोजले जातात. Azure AI Evaluation SDK सह आपल्या प्रणालीचे मूल्यांकन करण्यासाठी सुरुवात करण्यासाठी [जलद प्रारंभ मार्गदर्शक](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) अनुसरण करा. एकदा आपण मूल्यांकन चालविल्यानंतर, आपण [Azure AI Foundry मध्ये परिणाम व्हिज्युअलाइझ करू शकता](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).  

## ट्रेडमार्क्स  

या प्रकल्पामध्ये प्रकल्प, उत्पादने किंवा सेवांसाठी ट्रेडमार्क्स किंवा लोगो असू शकतात. Microsoft ट्रेडमार्क्स किंवा लोगोचा अधिकृत वापर [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) चे पालन करणे आवश्यक आहे.  
या प्रकल्पाच्या सुधारित आवृत्त्यांमध्ये Microsoft ट्रेडमार्क्स किंवा लोगोचा वापर गोंधळ निर्माण करू नये किंवा Microsoft प्रायोजकत्व सूचित करू नये. तृतीय-पक्ष ट्रेडमार्क्स किंवा लोगोचा कोणताही वापर त्या तृतीय-पक्षाच्या धोरणांच्या अधीन आहे.  

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून निर्माण होणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.