<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T13:50:47+00:00",
  "source_file": "README.md",
  "language_code": "el"
}
-->
# Phi Cookbook: Παραδείγματα με τα μοντέλα Phi της Microsoft

Phi είναι μια σειρά από μοντέλα τεχνητής νοημοσύνης ανοιχτού κώδικα που έχουν αναπτυχθεί από τη Microsoft.

Το Phi είναι αυτή τη στιγμή το πιο ισχυρό και οικονομικά αποδοτικό μικρό γλωσσικό μοντέλο (SLM), με εξαιρετικά αποτελέσματα σε πολυγλωσσική υποστήριξη, λογική, δημιουργία κειμένου/συνομιλιών, προγραμματισμό, εικόνες, ήχο και άλλα σενάρια.

Μπορείτε να αναπτύξετε το Phi στο cloud ή σε συσκευές edge και να δημιουργήσετε εύκολα εφαρμογές γενετικής τεχνητής νοημοσύνης με περιορισμένη υπολογιστική ισχύ.

Ακολουθήστε αυτά τα βήματα για να ξεκινήσετε να χρησιμοποιείτε αυτούς τους πόρους:
1. **Κάντε Fork το Αποθετήριο**: Πατήστε [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **Κλωνοποιήστε το Αποθετήριο**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**Γίνετε μέλος της κοινότητας Microsoft AI Discord και γνωρίστε ειδικούς και άλλους προγραμματιστές**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 Υποστήριξη Πολλαπλών Γλωσσών

#### Υποστηρίζεται μέσω GitHub Action (Αυτοματοποιημένο & Πάντα Ενημερωμένο)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) 
[Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](./README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)

## Περιεχόμενα

- Εισαγωγή
  - [Καλωσορίσατε στην οικογένεια Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [Ρύθμιση του περιβάλλοντός σας](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [Κατανόηση βασικών τεχνολογιών](./md/01.Introduction/01/01.Understandingtech.md)
  - [Ασφάλεια AI για τα μοντέλα Phi](./md/01.Introduction/01/01.AISafety.md)
  - [Υποστήριξη υλικού για το Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [Μοντέλα Phi & Διαθεσιμότητα σε πλατφόρμες](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [Χρήση Guidance-ai και Phi](./md/01.Introduction/01/01.Guidance.md)
  - [Μοντέλα στο GitHub Marketplace](https://github.com/marketplace/models)
  - [Κατάλογος μοντέλων Azure AI](https://ai.azure.com)

- Εξαγωγή συμπερασμάτων με το Phi σε διαφορετικά περιβάλλοντα
    - [Hugging face](./md/01.Introduction/02/01.HF.md)
    - [Μοντέλα GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    - [Κατάλογος μοντέλων Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    - [Ollama](./md/01.Introduction/02/04.Ollama.md)
    - [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    - [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Εξαγωγή συμπερασμάτων με την οικογένεια Phi
    - [Εξαγωγή συμπερασμάτων με το Phi σε iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [Εξαγωγή συμπερασμάτων με το Phi σε Android](./md/01.Introduction/03/Android_Inference.md)
    - [Εξαγωγή συμπερασμάτων με το Phi σε Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [Εξαγωγή συμπερασμάτων με το Phi σε AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [Εξαγωγή συμπερασμάτων με το Phi μέσω του Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [Εξαγωγή συμπερασμάτων με το Phi σε τοπικό server](./md/01.Introduction/03/Local_Server_Inference.md)
    - [Εξαγωγή συμπερασμάτων με το Phi σε απομακρυσμένο server μέσω AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [Εξαγωγή συμπερασμάτων με το Phi μέσω Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [Εξαγωγή συμπερασμάτων με το Phi--Vision τοπικά](./md/01.Introduction/03/Vision_Inference.md)
    - [Εξαγωγή συμπερασμάτων με το Phi μέσω Kaito AKS, Azure Containers (επίσημη υποστήριξη)](./md/01.Introduction/03/Kaito_Inference.md)

- [Ποσοτικοποίηση της οικογένειας Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [Ποσοτικοποίηση του Phi-3.5 / 4 μέσω llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [Ποσοτικοποίηση του Phi-3.5 / 4 μέσω επεκτάσεων γενετικής AI για το onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [Ποσοτικοποίηση του Phi-3.5 / 4 μέσω Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [Ποσοτικοποίηση του Phi-3.5 / 4 μέσω του Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Αξιολόγηση του Phi
    - [Υπεύθυνη AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Αξιολόγηση μέσω του Azure AI Foundry](./md/01.Introduction/05/AIFoundry.md)
    - [Χρήση του Promptflow για αξιολόγηση](./md/01.Introduction/05/Promptflow.md)

- RAG με το Azure AI Search
    - [Πώς να χρησιμοποιήσετε το Phi-4-mini και το Phi-4-multimodal (RAG) με το Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Δείγματα ανάπτυξης εφαρμογών με το Phi
  - Εφαρμογές Κειμένου & Συνομιλιών
    - Δείγματα Phi-4 🆕
      - [📓] [Συνομιλία με το μοντέλο Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [Συνομιλία με το τοπικό μοντέλο Phi-4 ONNX μέσω .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [Συνομιλία μέσω εφαρμογής κονσόλας .NET με το Phi-4 ONNX χρησιμοποιώντας το Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - Δείγματα Phi-3 / 3.5
      - [Τοπικό chatbot στον browser χρησιμοποιώντας το Phi3, ONNX Runtime Web και WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [Συνομιλία μέσω OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [Διαδραστικό μοντέλο - Phi-3-mini και OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - Δημιουργία wrapper και χρήση του Phi-3 με το MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [Βελτιστοποίηση μοντέλου - Πώς να βελτιστοποιήσετε το μοντέλο Phi-3-min για το ONNX Runtime Web με το Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [Εφαρμογή WinUI3 με το Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [Δείγμα εφαρμογής σημειώσεων AI με πολλαπλά μοντέλα στο WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Προσαρμογή και Ενσωμάτωση προσαρμοσμένων μοντέλων Phi-3 με το Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Προσαρμογή και Ενσωμάτωση προσαρμοσμένων μοντέλων Phi-3 με το Prompt flow στο Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Αξιολόγηση του προσαρμοσμένου μοντέλου Phi-3 / Phi-3.5 στο Azure AI Foundry με έμφαση στις Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης της Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Δείγμα πρόβλεψης γλώσσας με το Phi-3.5-mini-instruct (Κινέζικα/Αγγλικά)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Chatbot RAG με WebGPU και Phi-3.5-Instruct](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Χρήση GPU των Windows για τη δημιουργία λύσης Prompt flow με το Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Χρήση του Microsoft Phi-3.5 tflite για τη δημιουργία εφαρμογής Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Παράδειγμα Ερωτήσεων και Απαντήσεων .NET με τοπικό μοντέλο ONNX Phi-3 χρησιμοποιώντας το Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Εφαρμογή συνομιλίας κονσόλας .NET με Semantic Kernel και Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Δείγματα Κώδικα SDK Εξαγωγής Συμπερασμάτων Azure AI  
  - Δείγματα Phi-4 🆕  
    - [📓] [Δημιουργία κώδικα έργου χρησιμοποιώντας το Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Δείγματα Phi-3 / 3.5  
    - [Δημιουργήστε το δικό σας Visual Studio Code GitHub Copilot Chat με την οικογένεια Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [Δημιουργήστε το δικό σας Visual Studio Code Chat Copilot Agent με το Phi-3.5 από τα μοντέλα GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- Δείγματα Προχωρημένης Λογικής  
  - Δείγματα Phi-4 🆕  
    - [📓] [Δείγματα Phi-4-mini-reasoning ή Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Προσαρμογή του Phi-4-mini-reasoning με το Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Προσαρμογή του Phi-4-mini-reasoning με το Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Phi-4-mini-reasoning με μοντέλα GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Phi-4-mini-reasoning με μοντέλα Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- Επιδείξεις  
    - [Επιδείξεις Phi-4-mini φιλοξενούμενες στο Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Επιδείξεις Phi-4-multimodal φιλοξενούμενες στο Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- Δείγματα Όρασης  
  - Δείγματα Phi-4 🆕  
    - [📓] [Χρήση του Phi-4-multimodal για ανάγνωση εικόνων και δημιουργία κώδικα](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Δείγματα Phi-3 / 3.5  
    - [📓][Phi-3-vision-Μετατροπή κειμένου εικόνας σε κείμενο](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Ενσωμάτωση CLIP με το Phi-3-vision](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [ΕΠΙΔΕΙΞΗ: Ανακύκλωση με το Phi-3](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - Οπτικός βοηθός γλώσσας - με το Phi3-Vision και το OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Δείγμα πολλαπλών καρέ ή πολλαπλών εικόνων με το Phi-3.5 Vision](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Τοπικό μοντέλο ONNX Phi-3 Vision χρησιμοποιώντας το Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Μενού με τοπικό μοντέλο ONNX Phi-3 Vision χρησιμοποιώντας το Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- Δείγματα Μαθηματικών  
  - Δείγματα Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [Επίδειξη Μαθηματικών με το Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)  

- Δείγματα Ήχου  
  - Δείγματα Phi-4 🆕  
    - [📓] [Εξαγωγή μεταγραφών ήχου χρησιμοποιώντας το Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Δείγμα ήχου με το Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Δείγμα μετάφρασης ομιλίας με το Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [Εφαρμογή κονσόλας .NET χρησιμοποιώντας το Phi-4-multimodal για ανάλυση αρχείου ήχου και δημιουργία μεταγραφής](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- Δείγματα MoE  
  - Δείγματα Phi-3 / 3.5  
    - [📓] [Δείγμα κοινωνικών μέσων με τα μοντέλα Mixture of Experts (MoEs) Phi-3.5](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [Δημιουργία αγωγού RAG με το NVIDIA NIM Phi-3 MOE, το Azure AI Search και το LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- Δείγματα Κλήσης Συναρτήσεων  
  - Δείγματα Phi-4 🆕  
    - [📓] [Χρήση Κλήσης Συναρτήσεων με το Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Χρήση Κλήσης Συναρτήσεων για δημιουργία πολλαπλών πρακτόρων με το Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Χρήση Κλήσης Συναρτήσεων με το Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [Χρήση Κλήσης Συναρτήσεων με το ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- Δείγματα Μίξης Πολυτροπικών Δεδομένων  
  - Δείγματα Phi-4 🆕  
    - [📓] [Χρήση του Phi-4-multimodal ως Τεχνολογικός δημοσιογράφος](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [Εφαρμογή κονσόλας .NET χρησιμοποιώντας το Phi-4-multimodal για ανάλυση εικόνων](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Δείγματα Προσαρμογής Phi  
  - [Σενάρια Προσαρμογής](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [Προσαρμογή vs RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Προσαρμογή: Αφήστε το Phi-3 να γίνει ειδικός στον κλάδο](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [Προσαρμογή του Phi-3 με το AI Toolkit για το VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Προσαρμογή του Phi-3 με την Υπηρεσία Azure Machine Learning](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Προσαρμογή του Phi-3 με το Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [Προσαρμογή του Phi-3 με το QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Προσαρμογή του Phi-3 με το Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Προσαρμογή του Phi-3 με το Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Προσαρμογή με το Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Προσαρμογή με το Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)  
  - [Προσαρμογή του Phi-3-vision με το Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Προσαρμογή του Phi-3 με το Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Προσαρμογή του Phi-3-vision (επίσημη υποστήριξη)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Προσαρμογή του Phi-3 με το Kaito AKS, Azure Containers (επίσημη υποστήριξη)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Προσαρμογή του Phi-3 και 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- Εργαστήριο Hands-On  
  - [Εξερεύνηση προηγμένων μοντέλων: LLMs, SLMs, τοπική ανάπτυξη και άλλα](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [Απελευθέρωση δυνατοτήτων NLP: Προσαρμογή με το Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- Ακαδημαϊκές Ερευνητικές Εργασίες και Δημοσιεύσεις  
  - [Textbooks Are All You Need II: τεχνική αναφορά phi-1.5](https://arxiv.org/abs/2309.05463)  
  - [Τεχνική Αναφορά Phi-3: Ένα εξαιρετικά ικανό μοντέλο γλώσσας τοπικά στο τηλέφωνό σας](https://arxiv.org/abs/2404.14219)  
  - [Τεχνική Αναφορά Phi-4](https://arxiv.org/abs/2412.08905)  
  - [Τεχνική Αναφορά Phi-4-Mini: Συμπαγή αλλά Ισχυρά Πολυτροπικά Μοντέλα Γλώσσας μέσω Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [Βελτιστοποίηση Μικρών Μοντέλων Γλώσσας για Κλήση Συναρτήσεων Εντός Οχήματος](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) Προσαρμογή του PHI-3 για Ερωτήσεις Πολλαπλής Επιλογής: Μεθοδολογία, Αποτελέσματα και Προκλήσεις](https://arxiv.org/abs/2501.01588)  
- [Phi-4-reasoning Τεχνική Αναφορά](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning Τεχνική Αναφορά](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)  

## Χρήση των Μοντέλων Phi  

### Phi στο Azure AI Foundry  

Μπορείτε να μάθετε πώς να χρησιμοποιείτε το Microsoft Phi και πώς να δημιουργείτε ολοκληρωμένες λύσεις στις διάφορες συσκευές υλικού σας. Για να δοκιμάσετε το Phi, ξεκινήστε παίζοντας με τα μοντέλα και προσαρμόζοντας το Phi στα σενάριά σας χρησιμοποιώντας τον [Κατάλογο Μοντέλων Azure AI Foundry](https://aka.ms/phi3-azure-ai). Μπορείτε να μάθετε περισσότερα στο Getting Started με το [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).  

**Playground**  
Κάθε μοντέλο διαθέτει έναν ειδικό χώρο δοκιμών [Azure AI Playground](https://aka.ms/try-phi3).  

### Phi στα Μοντέλα GitHub  

Μπορείτε να μάθετε πώς να χρησιμοποιείτε το Microsoft Phi και πώς να δημιουργείτε ολοκληρωμένες λύσεις στις διάφορες συσκευές υλικού σας. Για να δοκιμάσετε το Phi, ξεκινήστε παίζοντας με το μοντέλο και προσαρμόζοντας το Phi στα σενάριά σας χρησιμοποιώντας τον [Κατάλογο Μοντέλων GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Μπορείτε να μάθετε περισσότερα στο Getting Started με τον [Κατάλογο Μοντέλων GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md).  

**Playground**  
Κάθε μοντέλο διαθέτει έναν ειδικό [χώρο δοκιμών για το μοντέλο](/md/02.QuickStart/GitHubModel_QuickStart.md).  

### Phi στο Hugging Face  

Μπορείτε επίσης να βρείτε το μοντέλο στο [Hugging Face](https://huggingface.co/microsoft).  

**Playground**  
[Playground του Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct).  

## Υπεύθυνη AI  

Η Microsoft δεσμεύεται να βοηθήσει τους πελάτες της να χρησιμοποιούν τα προϊόντα AI με υπευθυνότητα, να μοιράζεται τις γνώσεις της και να χτίζει σχέσεις εμπιστοσύνης μέσω εργαλείων όπως οι Σημειώσεις Διαφάνειας και οι Αξιολογήσεις Επιπτώσεων. Πολλοί από αυτούς τους πόρους βρίσκονται στο [https://aka.ms/RAI](https://aka.ms/RAI).  
Η προσέγγιση της Microsoft για υπεύθυνη AI βασίζεται στις αρχές AI: δικαιοσύνη, αξιοπιστία και ασφάλεια, ιδιωτικότητα και ασφάλεια, συμπερίληψη, διαφάνεια και λογοδοσία.  

Τα μεγάλης κλίμακας μοντέλα φυσικής γλώσσας, εικόνας και ομιλίας - όπως αυτά που χρησιμοποιούνται σε αυτό το δείγμα - μπορεί να συμπεριφέρονται με τρόπους που είναι άδικοι, αναξιόπιστοι ή προσβλητικοί, προκαλώντας έτσι βλάβες. Παρακαλούμε συμβουλευτείτε τη [Σημείωση Διαφάνειας της υπηρεσίας Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) για να ενημερωθείτε σχετικά με τους κινδύνους και τους περιορισμούς.  

Η συνιστώμενη προσέγγιση για την αντιμετώπιση αυτών των κινδύνων είναι να συμπεριλάβετε ένα σύστημα ασφάλειας στην αρχιτεκτονική σας που μπορεί να ανιχνεύσει και να αποτρέψει επιβλαβή συμπεριφορά. Το [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) παρέχει ένα ανεξάρτητο επίπεδο προστασίας, ικανό να ανιχνεύει επιβλαβές περιεχόμενο που δημιουργείται από χρήστες ή AI σε εφαρμογές και υπηρεσίες. Το Azure AI Content Safety περιλαμβάνει APIs για κείμενο και εικόνες που σας επιτρέπουν να ανιχνεύετε επιβλαβές υλικό. Στο πλαίσιο του Azure AI Foundry, η υπηρεσία Content Safety σας επιτρέπει να δείτε, να εξερευνήσετε και να δοκιμάσετε δείγματα κώδικα για την ανίχνευση επιβλαβούς περιεχομένου σε διαφορετικές μορφές. Η ακόλουθη [τεκμηρίωση γρήγορης εκκίνησης](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) σας καθοδηγεί στη διαδικασία υποβολής αιτημάτων στην υπηρεσία.  

Ένας άλλος παράγοντας που πρέπει να ληφθεί υπόψη είναι η συνολική απόδοση της εφαρμογής. Σε εφαρμογές πολλαπλών μορφών και πολλαπλών μοντέλων, η απόδοση σημαίνει ότι το σύστημα λειτουργεί όπως εσείς και οι χρήστες σας περιμένετε, συμπεριλαμβανομένου του να μην παράγει επιβλαβή αποτελέσματα. Είναι σημαντικό να αξιολογήσετε την απόδοση της συνολικής εφαρμογής σας χρησιμοποιώντας [Αξιολογητές Απόδοσης και Ποιότητας και Κινδύνου και Ασφάλειας](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Έχετε επίσης τη δυνατότητα να δημιουργήσετε και να αξιολογήσετε με [προσαρμοσμένους αξιολογητές](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).  

Μπορείτε να αξιολογήσετε την εφαρμογή AI σας στο περιβάλλον ανάπτυξης χρησιμοποιώντας το [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Δεδομένου είτε ενός συνόλου δεδομένων δοκιμής είτε ενός στόχου, οι γεννήσεις της εφαρμογής AI σας μετριούνται ποσοτικά με ενσωματωμένους αξιολογητές ή προσαρμοσμένους αξιολογητές της επιλογής σας. Για να ξεκινήσετε με το Azure AI Evaluation SDK για να αξιολογήσετε το σύστημά σας, μπορείτε να ακολουθήσετε τον [οδηγό γρήγορης εκκίνησης](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Μόλις εκτελέσετε μια αξιολόγηση, μπορείτε να [οραματιστείτε τα αποτελέσματα στο Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).  

## Εμπορικά Σήματα  

Αυτό το έργο μπορεί να περιέχει εμπορικά σήματα ή λογότυπα για έργα, προϊόντα ή υπηρεσίες. Η εξουσιοδοτημένη χρήση των εμπορικών σημάτων ή λογοτύπων της Microsoft υπόκειται και πρέπει να ακολουθεί τις [Οδηγίες Χρήσης Εμπορικών Σημάτων και Επωνυμίας της Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Η χρήση εμπορικών σημάτων ή λογοτύπων της Microsoft σε τροποποιημένες εκδόσεις αυτού του έργου δεν πρέπει να προκαλεί σύγχυση ή να υπονοεί χορηγία από τη Microsoft. Οποιαδήποτε χρήση εμπορικών σημάτων ή λογοτύπων τρίτων υπόκειται στις πολιτικές αυτών των τρίτων.  

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.