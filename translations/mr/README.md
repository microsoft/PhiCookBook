<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a73c59eecd7ad4ec494fd4333a29e208",
  "translation_date": "2025-10-11T10:47:45+00:00",
  "source_file": "README.md",
  "language_code": "mr"
}
-->
# Phi कुकबुक: Microsoft च्या Phi मॉडेल्ससह प्रॅक्टिकल उदाहरणे

Phi हे Microsoft द्वारे विकसित केलेले ओपन सोर्स AI मॉडेल्सचे एक मालिक आहे.

Phi सध्या सर्वात शक्तिशाली आणि किफायतशीर लहान भाषा मॉडेल (SLM) आहे, ज्यामध्ये बहुभाषा, तर्कशक्ती, मजकूर/चॅट निर्मिती, कोडिंग, प्रतिमा, ऑडिओ आणि इतर परिस्थितींमध्ये उत्कृष्ट बेंचमार्क आहेत.

Phi ला क्लाउड किंवा एज डिव्हाइसवर तैनात करता येते आणि मर्यादित संगणकीय शक्ती असलेल्या जनरेटिव्ह AI अनुप्रयोग सहजपणे तयार करता येतात.

या संसाधनांचा वापर सुरू करण्यासाठी खालील चरणांचे अनुसरण करा:
1. **रेपॉझिटरी फोर्क करा**: क्लिक करा [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **रेपॉझिटरी क्लोन करा**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Microsoft AI Discord समुदायामध्ये सामील व्हा आणि तज्ञ व इतर विकसकांशी भेटा**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 बहुभाषा समर्थन

#### GitHub Action द्वारे समर्थित (स्वयंचलित आणि नेहमी अद्ययावत)

[अरबी](../ar/README.md) | [बंगाली](../bn/README.md) | [बल्गेरियन](../bg/README.md) | [बर्मी (म्यानमार)](../my/README.md) | [चिनी (सरलीकृत)](../zh/README.md) | [चिनी (पारंपरिक, हाँगकाँग)](../hk/README.md) | [चिनी (पारंपरिक, मकाऊ)](../mo/README.md) | [चिनी (पारंपरिक, तैवान)](../tw/README.md) | [क्रोएशियन](../hr/README.md) | [झेक](../cs/README.md) | [डॅनिश](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियन](../et/README.md) | [फिनिश](../fi/README.md) | [फ्रेंच](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिंदी](../hi/README.md) | [हंगेरियन](../hu/README.md) | [इंडोनेशियन](../id/README.md) | [इटालियन](../it/README.md) | [जपानी](../ja/README.md) | [कोरियन](../ko/README.md) | [लिथुआनियन](../lt/README.md) | [मलय](../ms/README.md) | [मराठी](./README.md) | [नेपाळी](../ne/README.md) | [नॉर्वेजियन](../no/README.md) | [पर्शियन (फारसी)](../fa/README.md) | [पोलिश](../pl/README.md) | [पोर्तुगीज (ब्राझील)](../br/README.md) | [पोर्तुगीज (पोर्तुगाल)](../pt/README.md) | [पंजाबी (गुरमुखी)](../pa/README.md) | [रोमानियन](../ro/README.md) | [रशियन](../ru/README.md) | [सर्बियन (सिरिलिक)](../sr/README.md) | [स्लोव्हाक](../sk/README.md) | [स्लोव्हेनियन](../sl/README.md) | [स्पॅनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिश](../sv/README.md) | [टागालोग (फिलिपिनो)](../tl/README.md) | [तमिळ](../ta/README.md) | [थाई](../th/README.md) | [तुर्की](../tr/README.md) | [युक्रेनियन](../uk/README.md) | [उर्दू](../ur/README.md) | [व्हिएतनामी](../vi/README.md)

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

- विविध वातावरणात Phi चा अंदाज
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [GitHub मॉडेल्स](./md/01.Introduction/02/02.GitHubModel.md)
    - [Azure AI Foundry मॉडेल कॅटलॉग](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Phi कुटुंबाचा अंदाज
    - [iOS मध्ये Phi चा अंदाज](./md/01.Introduction/03/iOS_Inference.md)
    - [Android मध्ये Phi चा अंदाज](./md/01.Introduction/03/Android_Inference.md)
    - [Jetson मध्ये Phi चा अंदाज](./md/01.Introduction/03/Jetson_Inference.md)
    - [AI PC मध्ये Phi चा अंदाज](./md/01.Introduction/03/AIPC_Inference.md)
    - [Apple MLX Framework सह Phi चा अंदाज](./md/01.Introduction/03/MLX_Inference.md)
    - [स्थानिक सर्व्हरमध्ये Phi चा अंदाज](./md/01.Introduction/03/Local_Server_Inference.md)
    - [AI Toolkit वापरून रिमोट सर्व्हरमध्ये Phi चा अंदाज](./md/01.Introduction/03/Remote_Interence.md)
    - [Rust सह Phi चा अंदाज](./md/01.Introduction/03/Rust_Inference.md)
    - [स्थानिक Vision सह Phi चा अंदाज](./md/01.Introduction/03/Vision_Inference.md)
    - [Kaito AKS, Azure Containers सह Phi चा अंदाज (अधिकृत समर्थन)](./md/01.Introduction/03/Kaito_Inference.md)

- [Phi कुटुंबाचे प्रमाणित करणे](./md/01.Introduction/04/QuantifyingPhi.md)
    - [llama.cpp वापरून Phi-3.5 / 4 चे प्रमाणित करणे](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [onnxruntime साठी जनरेटिव्ह AI विस्तार वापरून Phi-3.5 / 4 चे प्रमाणित करणे](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Intel OpenVINO वापरून Phi-3.5 / 4 चे प्रमाणित करणे](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Apple MLX Framework वापरून Phi-3.5 / 4 चे प्रमाणित करणे](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

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
      - [Sementic Kernel वापरून Phi-4 ONNX सह .NET कन्सोल अॅप चॅट](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Phi-3 / 3.5 नमुने
      - [Phi3, ONNX Runtime Web आणि WebGPU वापरून ब्राउझरमध्ये स्थानिक चॅटबॉट](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [OpenVino चॅट](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [मल्टी मॉडेल - इंटरएक्टिव्ह Phi-3-mini आणि OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Wrapper तयार करणे आणि MLFlow सह Phi-3 वापरणे](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [मॉडेल ऑप्टिमायझेशन - Olive सह ONNX Runtime Web साठी Phi-3-min मॉडेल कसे ऑप्टिमाइझ करावे](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [WinUI3 अ‍ॅप Phi-3 mini-4k-instruct-onnx सह](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [WinUI3 मल्टी मॉडेल AI संचालित नोट्स अ‍ॅप नमुना](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [कस्टम Phi-3 मॉडेल्स Prompt flow सह फाइन-ट्यून आणि समाकलित करा](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Azure AI Foundry मध्ये कस्टम Phi-3 मॉडेल्स Prompt flow सह फाइन-ट्यून आणि समाकलित करा](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Microsoft च्या उत्तरदायी AI तत्त्वांवर लक्ष केंद्रित करून Azure AI Foundry मध्ये फाइन-ट्यून केलेल्या Phi-3 / Phi-3.5 मॉडेलचे मूल्यांकन करा](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Phi-3.5-mini-instruct भाषा अंदाज नमुना (चिनी/इंग्रजी)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Windows GPU वापरून Phi-3.5-Instruct ONNX सह Prompt flow सोल्यूशन तयार करा](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Microsoft Phi-3.5 tflite वापरून Android अ‍ॅप तयार करा](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Microsoft.ML.OnnxRuntime वापरून स्थानिक ONNX Phi-3 मॉडेलसह Q&A .NET उदाहरण](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Semantic Kernel आणि Phi-3 सह Console chat .NET अ‍ॅप](../../md/04.HOL/dotnet/src/LabsPhi302)

- Azure AI Inference SDK कोड आधारित नमुने
  - Phi-4 नमुने 🆕
    - [📓] [Phi-4-multimodal वापरून प्रोजेक्ट कोड तयार करा](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
  - Phi-3 / 3.5 नमुने
    - [Microsoft Phi-3 कुटुंबासह आपले स्वतःचे Visual Studio Code GitHub Copilot Chat तयार करा](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
    - [Phi-3.5 सह GitHub मॉडेल्स वापरून आपले स्वतःचे Visual Studio Code Chat Copilot Agent तयार करा](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

- प्रगत विचार नमुने
  - Phi-4 नमुने 🆕
    - [📓] [Phi-4-mini-reasoning किंवा Phi-4-reasoning नमुने](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
    - [📓] [Microsoft Olive सह Phi-4-mini-reasoning फाइन-ट्यूनिंग](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [Apple MLX सह Phi-4-mini-reasoning फाइन-ट्यूनिंग](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
    - [📓] [GitHub मॉडेल्ससह Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
    - [📓] [Azure AI Foundry मॉडेल्ससह Phi-4-mini-reasoning](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
- डेमो
    - [Hugging Face Spaces वर होस्ट केलेले Phi-4-mini डेमो](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
    - [Hugging Face Spaces वर होस्ट केलेले Phi-4-multimodal डेमो](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
- व्हिजन नमुने
  - Phi-4 नमुने 🆕
    - [📓] [Phi-4-multimodal वापरून प्रतिमा वाचा आणि कोड तयार करा](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
  - Phi-3 / 3.5 नमुने
    - [📓][Phi-3-vision-प्रतिमा मजकूर ते मजकूर](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
    - [📓][Phi-3-vision CLIP एम्बेडिंग](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
    - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)
    - [Phi-3-vision - Phi3-Vision आणि OpenVINO सह व्हिज्युअल भाषा सहाय्यक](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
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
    - [📓] [Phi-4-multimodal भाषांतर नमुना](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
    - [.NET कन्सोल अ‍ॅप्लिकेशन वापरून Phi-4-multimodal ऑडिओसह ऑडिओ फाइलचे विश्लेषण करा आणि ट्रान्सक्रिप्ट तयार करा](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

- MOE नमुने
  - Phi-3 / 3.5 नमुने
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) सोशल मीडिया नमुना](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
    - [📓] [NVIDIA NIM Phi-3 MOE, Azure AI Search, आणि LlamaIndex सह Retrieval-Augmented Generation (RAG) पाइपलाइन तयार करणे](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)

- फंक्शन कॉलिंग नमुने
  - Phi-4 नमुने 🆕
    - [📓] [Phi-4-mini सह फंक्शन कॉलिंग वापरणे](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
    - [📓] [Phi-4-mini सह मल्टी-एजंट्स तयार करण्यासाठी फंक्शन कॉलिंग वापरणे](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
    - [📓] [Ollama सह फंक्शन कॉलिंग वापरणे](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
    - [📓] [ONNX सह फंक्शन कॉलिंग वापरणे](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)

- मल्टीमॉडल मिक्सिंग नमुने
  - Phi-4 नमुने 🆕
    - [📓] [Phi-4-multimodal तंत्रज्ञान पत्रकार म्हणून वापरणे](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
    - [.NET कन्सोल अ‍ॅप्लिकेशन वापरून Phi-4-multimodal सह प्रतिमांचे विश्लेषण करा](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- Phi नमुन्यांचे फाइन-ट्यूनिंग
  - [फाइन-ट्यूनिंग परिस्थिती](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [फाइन-ट्यूनिंग vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [Phi-3 ला उद्योग तज्ञ बनवू द्या](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
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
  - [Phi-3 तांत्रिक अहवाल: आपल्या फोनवर स्थानिक पातळीवर अत्यंत सक्षम भाषा मॉडेल](https://arxiv.org/abs/2404.14219)
  - [Phi-4 तांत्रिक अहवाल](https://arxiv.org/abs/2412.08905)
  - [Phi-4-Mini तांत्रिक अहवाल: Mixture-of-LoRAs च्या माध्यमातून कॉम्पॅक्ट परंतु शक्तिशाली मल्टीमॉडल भाषा मॉडेल्स](https://arxiv.org/abs/2503.01743)
  - [वाहनातील फंक्शन-कॉलिंगसाठी लहान भाषा मॉडेल्सचे ऑप्टिमायझेशन](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) PHI-3 च्या मल्टीपल-चॉइस प्रश्न उत्तरासाठी फाइन-ट्यूनिंग: पद्धती, परिणाम आणि आव्हाने](https://arxiv.org/abs/2501.01588)
  - [Phi-4-reasoning तांत्रिक अहवाल](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [Phi-4-mini-reasoning तांत्रिक अहवाल](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Phi मॉडेल्सचा वापर

### Azure AI Foundry वर Phi

Microsoft Phi कसा वापरायचा आणि विविध हार्डवेअर उपकरणांमध्ये एंड-टू-एंड सोल्यूशन्स कसे तयार करायचे हे शिकता येईल. Phi चा अनुभव घेण्यासाठी, मॉडेल्ससह खेळून आणि तुमच्या परिस्थितीनुसार Phi सानुकूलित करून सुरुवात करा. [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) वरून अधिक माहिती मिळवा. [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md) शी सुरुवात करण्यासाठी येथे जाणून घ्या.

**Playground**
प्रत्येक मॉडेलसाठी [Azure AI Playground](https://aka.ms/try-phi3) वर चाचणी करण्यासाठी स्वतंत्र प्लेग्राउंड आहे.

### GitHub मॉडेल्सवर Phi

Microsoft Phi कसा वापरायचा आणि विविध हार्डवेअर उपकरणांमध्ये एंड-टू-एंड सोल्यूशन्स कसे तयार करायचे हे शिकता येईल. Phi चा अनुभव घेण्यासाठी, मॉडेलसह खेळून आणि तुमच्या परिस्थितीनुसार Phi सानुकूलित करून सुरुवात करा. [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) वरून अधिक माहिती मिळवा. [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) शी सुरुवात करण्यासाठी येथे जाणून घ्या.

**Playground**
प्रत्येक मॉडेलसाठी [प्लेग्राउंड चाचणी करण्यासाठी](/md/02.QuickStart/GitHubModel_QuickStart.md) स्वतंत्र जागा आहे.

### Hugging Face वर Phi

तुम्ही मॉडेल [Hugging Face](https://huggingface.co/microsoft) वर देखील शोधू शकता.

**Playground**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## जबाबदार AI 

Microsoft आपल्या ग्राहकांना आमची AI उत्पादने जबाबदारीने वापरण्यास मदत करण्यासाठी, आमचे अनुभव सामायिक करण्यासाठी आणि पारदर्शकता नोट्स आणि प्रभाव मूल्यांकनासारख्या साधनांद्वारे विश्वास-आधारित भागीदारी तयार करण्यासाठी वचनबद्ध आहे. या संसाधनांपैकी अनेक [https://aka.ms/RAI](https://aka.ms/RAI) येथे सापडू शकतात. Microsoft चा जबाबदार AI चा दृष्टिकोन निष्पक्षता, विश्वासार्हता आणि सुरक्षितता, गोपनीयता आणि सुरक्षा, समावेशकता, पारदर्शकता आणि उत्तरदायित्व यावर आधारित आहे.

प्राकृतिक भाषा, प्रतिमा आणि भाषण यासारख्या मोठ्या प्रमाणातील मॉडेल्स - जसे की या नमुन्यात वापरले जातात - संभाव्यतः अन्यायकारक, अविश्वसनीय किंवा आक्षेपार्ह वर्तन करू शकतात, ज्यामुळे नुकसान होऊ शकते. जोखीम आणि मर्यादांबद्दल माहिती मिळवण्यासाठी कृपया [Azure OpenAI सेवा पारदर्शकता नोट](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) वाचा.

या जोखमी कमी करण्यासाठी शिफारस केलेला दृष्टिकोन म्हणजे तुमच्या आर्किटेक्चरमध्ये एक सुरक्षा प्रणाली समाविष्ट करणे जे हानिकारक वर्तन शोधू आणि रोखू शकते. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) एक स्वतंत्र संरक्षण स्तर प्रदान करते, जे अनुप्रयोग आणि सेवांमध्ये वापरकर्त्याने तयार केलेल्या आणि AI-निर्मित सामग्री शोधू शकते. Azure AI Content Safety मध्ये मजकूर आणि प्रतिमा API समाविष्ट आहेत जे तुम्हाला हानिकारक सामग्री शोधण्यास अनुमती देतात. Azure AI Foundry मध्ये, Content Safety सेवा तुम्हाला विविध प्रकारांमध्ये हानिकारक सामग्री शोधण्यासाठी नमुना कोड पाहण्यास, एक्सप्लोर करण्यास आणि प्रयत्न करण्यास अनुमती देते. [त्वरित प्रारंभ दस्तऐवज](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) तुम्हाला सेवेसाठी विनंत्या कशा करायच्या याबद्दल मार्गदर्शन करते.

एकूणच अनुप्रयोग कार्यक्षमता विचारात घेणे देखील महत्त्वाचे आहे. मल्टी-मोडल आणि मल्टी-मॉडेल्स अनुप्रयोगांसह, कार्यक्षमता म्हणजे प्रणाली तुमच्या आणि तुमच्या वापरकर्त्यांच्या अपेक्षेनुसार कार्य करते, ज्यामध्ये हानिकारक आउटपुट तयार करणे समाविष्ट नाही. तुमच्या एकूण अनुप्रयोगाची कार्यक्षमता [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) वापरून मूल्यांकन करणे महत्त्वाचे आहे. तुम्हाला [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators) तयार करण्याची आणि मूल्यांकन करण्याची क्षमता देखील आहे.

तुमच्या विकासाच्या वातावरणात तुमच्या AI अनुप्रयोगाचे मूल्यांकन [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html) वापरून करू शकता. चाचणी डेटासेट किंवा लक्ष्य दिल्यास, तुमच्या जनरेटिव्ह AI अनुप्रयोगाच्या निर्मितीचे तुमच्या निवडीच्या अंगभूत मूल्यांकनकर्त्यांद्वारे किंवा सानुकूल मूल्यांकनकर्त्यांद्वारे प्रमाणात्मक मोजमाप केले जाते. तुमच्या प्रणालीचे मूल्यांकन करण्यासाठी Azure AI Evaluation SDK सह सुरुवात करण्यासाठी तुम्ही [त्वरित प्रारंभ मार्गदर्शक](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) अनुसरण करू शकता. एकदा तुम्ही मूल्यांकन चालविल्यानंतर, तुम्ही [Azure AI Foundry मध्ये परिणामांचे व्हिज्युअलायझेशन करू शकता](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## ट्रेडमार्क्स

या प्रकल्पामध्ये प्रकल्प, उत्पादने किंवा सेवांसाठी ट्रेडमार्क किंवा लोगो असू शकतात. Microsoft ट्रेडमार्क किंवा लोगोचा अधिकृत वापर [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) चे पालन करणे आवश्यक आहे. या प्रकल्पाच्या सुधारित आवृत्त्यांमध्ये Microsoft ट्रेडमार्क किंवा लोगोचा वापर गोंधळ निर्माण करू नये किंवा Microsoft प्रायोजकत्वाचा संकेत देऊ नये. तृतीय-पक्ष ट्रेडमार्क किंवा लोगोचा कोणताही वापर त्या तृतीय-पक्षाच्या धोरणांच्या अधीन आहे.

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून निर्माण होणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.