<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2e042b12a63c59931dc121c2c638bc58",
  "translation_date": "2025-07-09T18:23:57+00:00",
  "source_file": "README.md",
  "language_code": "el"
}
-->
# Phi Cookbook: Παραδείγματα με Πρακτική Εφαρμογή με τα Μοντέλα Phi της Microsoft

[![Άνοιγμα και χρήση των δειγμάτων στο GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![Άνοιγμα σε Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![Συνεισφέροντες στο GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![Θέματα στο GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![Αιτήματα έλξης στο GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![Παρακολουθητές στο GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![Forks στο GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![Αστέρια στο GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Το Phi είναι μια σειρά ανοιχτών μοντέλων τεχνητής νοημοσύνης που αναπτύχθηκαν από τη Microsoft.

Το Phi είναι αυτή τη στιγμή το πιο ισχυρό και οικονομικό μικρό γλωσσικό μοντέλο (SLM), με εξαιρετικές επιδόσεις σε πολυγλωσσικά περιβάλλοντα, συλλογιστική, δημιουργία κειμένου/συνομιλίας, κωδικοποίηση, εικόνες, ήχο και άλλες εφαρμογές.

Μπορείτε να αναπτύξετε το Phi στο cloud ή σε συσκευές άκρου, και να δημιουργήσετε εύκολα εφαρμογές γεννητικής AI με περιορισμένη υπολογιστική ισχύ.

Ακολουθήστε τα παρακάτω βήματα για να ξεκινήσετε με αυτούς τους πόρους:  
1. **Κάντε Fork το Αποθετήριο**: Κάντε κλικ [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **Κλωνοποιήστε το Αποθετήριο**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**Εγγραφείτε στην Κοινότητα Microsoft AI στο Discord και γνωρίστε ειδικούς και άλλους προγραμματιστές**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

## 🌐 Υποστήριξη Πολλών Γλωσσών

### Υποστηρίζεται μέσω GitHub Action (Αυτοματοποιημένο & Πάντα Ενημερωμένο)

[Γαλλικά](../fr/README.md) | [Ισπανικά](../es/README.md) | [Γερμανικά](../de/README.md) | [Ρωσικά](../ru/README.md) | [Αραβικά](../ar/README.md) | [Περσικά (Φαρσί)](../fa/README.md) | [Ουρντού](../ur/README.md) | [Κινέζικα (Απλοποιημένα)](../zh/README.md) | [Κινέζικα (Παραδοσιακά, Μακάο)](../mo/README.md) | [Κινέζικα (Παραδοσιακά, Χονγκ Κονγκ)](../hk/README.md) | [Κινέζικα (Παραδοσιακά, Ταϊβάν)](../tw/README.md) | [Ιαπωνικά](../ja/README.md) | [Κορεατικά](../ko/README.md) | [Χίντι](../hi/README.md)  
[Μπενγκάλι](../bn/README.md) | [Μαράθι](../mr/README.md) | [Νεπάλι](../ne/README.md) | [Πουντζάμπι (Γκουρμούκι)](../pa/README.md) | [Πορτογαλικά (Πορτογαλία)](../pt/README.md) | [Πορτογαλικά (Βραζιλία)](../br/README.md) | [Ιταλικά](../it/README.md) | [Πολωνικά](../pl/README.md) | [Τουρκικά](../tr/README.md) | [Ελληνικά](./README.md) | [Ταϊλανδικά](../th/README.md) | [Σουηδικά](../sv/README.md) | [Δανικά](../da/README.md) | [Νορβηγικά](../no/README.md) | [Φινλανδικά](../fi/README.md) | [Ολλανδικά](../nl/README.md) | [Εβραϊκά](../he/README.md) | [Βιετναμέζικα](../vi/README.md) | [Ινδονησιακά](../id/README.md) | [Μαλαϊκά](../ms/README.md) | [Ταγκάλογκ (Φιλιππινέζικα)](../tl/README.md) | [Σουαχίλι](../sw/README.md) | [Ουγγρικά](../hu/README.md) | [Τσέχικα](../cs/README.md) | [Σλοβακικά](../sk/README.md) | [Ρουμανικά](../ro/README.md) | [Βουλγαρικά](../bg/README.md) | [Σερβικά (Κυριλλικά)](../sr/README.md) | [Κροατικά](../hr/README.md) | [Σλοβενικά](../sl/README.md)

## Περιεχόμενα

- Εισαγωγή  
  - [Καλωσόρισμα στην Οικογένεια Phi](./md/01.Introduction/01/01.PhiFamily.md)  
  - [Ρύθμιση του περιβάλλοντός σας](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [Κατανόηση βασικών τεχνολογιών](./md/01.Introduction/01/01.Understandingtech.md)  
  - [Ασφάλεια AI για τα Μοντέλα Phi](./md/01.Introduction/01/01.AISafety.md)  
  - [Υποστήριξη Υλικού Phi](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [Μοντέλα Phi & Διαθεσιμότητα σε πλατφόρμες](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [Χρήση Guidance-ai και Phi](./md/01.Introduction/01/01.Guidance.md)  
  - [GitHub Marketplace Models](https://github.com/marketplace/models)  
  - [Κατάλογος Μοντέλων Azure AI](https://ai.azure.com)

- Εκτέλεση Phi σε διαφορετικά περιβάλλοντα  
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)  
    -  [GitHub Models](./md/01.Introduction/02/02.GitHubModel.md)  
    -  [Κατάλογος Μοντέλων Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)  
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)  
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)  
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- Εκτέλεση Phi Family  
    - [Εκτέλεση Phi σε iOS](./md/01.Introduction/03/iOS_Inference.md)  
    - [Εκτέλεση Phi σε Android](./md/01.Introduction/03/Android_Inference.md)  
    - [Εκτέλεση Phi σε Jetson](./md/01.Introduction/03/Jetson_Inference.md)  
    - [Εκτέλεση Phi σε AI PC](./md/01.Introduction/03/AIPC_Inference.md)  
    - [Εκτέλεση Phi με Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)  
    - [Εκτέλεση Phi σε Τοπικό Διακομιστή](./md/01.Introduction/03/Local_Server_Inference.md)  
    - [Εκτέλεση Phi σε Απομακρυσμένο Διακομιστή με AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)  
    - [Εκτέλεση Phi με Rust](./md/01.Introduction/03/Rust_Inference.md)  
    - [Εκτέλεση Phi--Vision τοπικά](./md/01.Introduction/03/Vision_Inference.md)  
    - [Εκτέλεση Phi με Kaito AKS, Azure Containers (επίσημη υποστήριξη)](./md/01.Introduction/03/Kaito_Inference.md)  
-  [Ποσοτικοποίηση Phi Family](./md/01.Introduction/04/QuantifyingPhi.md)  
    - [Ποσοτικοποίηση Phi-3.5 / 4 με llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
    - [Ποσοτικοποίηση Phi-3.5 / 4 με επεκτάσεις Generative AI για onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
    - [Ποσοτικοποίηση Phi-3.5 / 4 με Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
    - [Ποσοτικοποίηση Phi-3.5 / 4 με Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- Αξιολόγηση Phi  
    - [Υπεύθυνη AI](./md/01.Introduction/05/ResponsibleAI.md)  
    - [Azure AI Foundry για Αξιολόγηση](./md/01.Introduction/05/AIFoundry.md)  
    - [Χρήση Promptflow για Αξιολόγηση](./md/01.Introduction/05/Promptflow.md)

- RAG με Azure AI Search  
    - [Πώς να χρησιμοποιήσετε τα Phi-4-mini και Phi-4-multimodal (RAG) με Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- Παραδείγματα ανάπτυξης εφαρμογών Phi  
  - Εφαρμογές Κειμένου & Συνομιλίας  
    - Δείγματα Phi-4 🆕  
      - [📓] [Συνομιλία με το μοντέλο Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [Συνομιλία με το τοπικό μοντέλο Phi-4 ONNX σε .NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [Εφαρμογή κονσόλας .NET για συνομιλία με Phi-4 ONNX χρησιμοποιώντας Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - Δείγματα Phi-3 / 3.5  
      - [Τοπικό chatbot στον περιηγητή με χρήση Phi3, ONNX Runtime Web και WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [OpenVino Chat](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [Πολλαπλά μοντέλα - Διαδραστικό Phi-3-mini και OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - Δημιουργία wrapper και χρήση Phi-3 με MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [Βελτιστοποίηση μοντέλου - Πώς να βελτιστοποιήσετε το μοντέλο Phi-3-min για ONNX Runtime Web με Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [Εφαρμογή WinUI3 με Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [Δείγμα εφαρμογής WinUI3 με πολλαπλά μοντέλα και AI-powered σημειώσεις](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [Βελτιστοποίηση και Ενσωμάτωση προσαρμοσμένων μοντέλων Phi-3 με το Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [Βελτιστοποίηση και Ενσωμάτωση προσαρμοσμένων μοντέλων Phi-3 με το Prompt flow στο Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [Αξιολόγηση του βελτιστοποιημένου μοντέλου Phi-3 / Phi-3.5 στο Azure AI Foundry με έμφαση στις Αρχές Υπεύθυνης Τεχνητής Νοημοσύνης της Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [Δείγμα πρόβλεψης γλώσσας Phi-3.5-mini-instruct (Κινέζικα/Αγγλικά)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [Phi-3.5-Instruct WebGPU RAG Chatbot](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [Χρήση Windows GPU για δημιουργία λύσης Prompt flow με Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [Χρήση Microsoft Phi-3.5 tflite για δημιουργία εφαρμογής Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [Παράδειγμα Q&A .NET με τοπικό μοντέλο ONNX Phi-3 χρησιμοποιώντας το Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [Εφαρμογή συνομιλίας κονσόλας .NET με Semantic Kernel και Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- Παραδείγματα κώδικα Azure AI Inference SDK  
  - Παραδείγματα Phi-4 🆕  
    - [📓] [Δημιουργία κώδικα έργου με χρήση Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - Παραδείγματα Phi-3 / 3.5  
    - [Δημιουργήστε το δικό σας Visual Studio Code GitHub Copilot Chat με την οικογένεια Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [Δημιουργήστε τον δικό σας Visual Studio Code Chat Copilot Agent με Phi-3.5 χρησιμοποιώντας μοντέλα GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- Παραδείγματα Προχωρημένης Λογικής  
  - Παραδείγματα Phi-4 🆕  
    - [📓] [Παραδείγματα Phi-4-mini-reasoning ή Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [Βελτιστοποίηση Phi-4-mini-reasoning με Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Βελτιστοποίηση Phi-4-mini-reasoning με Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Phi-4-mini-reasoning με μοντέλα GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Phi-4-mini-reasoning με μοντέλα Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- Demo  
    - [Phi-4-mini demos φιλοξενούμενα στο Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [Phi-4-multimodal demos φιλοξενούμενα στο Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- Παραδείγματα Όρασης  
  - Παραδείγματα Phi-4 🆕  
    - [📓] [Χρήση Phi-4-multimodal για ανάγνωση εικόνων και δημιουργία κώδικα](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - Παραδείγματα Phi-3 / 3.5  
    - [📓][Phi-3-vision-Μετατροπή κειμένου εικόνας σε κείμενο](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [DEMO: Phi-3 Ανακύκλωση](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - Οπτικός βοηθός γλώσσας - με Phi3-Vision και OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision δείγμα πολλαπλών καρέ ή πολλαπλών εικόνων](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Τοπικό μοντέλο Phi-3 Vision ONNX με χρήση Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [Μενού βασισμένο σε τοπικό μοντέλο Phi-3 Vision ONNX με χρήση Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- Παραδείγματα Μαθηματικών  
  - Παραδείγματα Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [Demo Μαθηματικών με Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)  

- Παραδείγματα Ήχου  
  - Παραδείγματα Phi-4 🆕  
    - [📓] [Εξαγωγή απομαγνητοφωνήσεων ήχου με χρήση Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [Δείγμα ήχου Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [Δείγμα μετάφρασης ομιλίας Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [Εφαρμογή κονσόλας .NET που χρησιμοποιεί Phi-4-multimodal Audio για ανάλυση αρχείου ήχου και δημιουργία απομαγνητοφώνησης](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- Παραδείγματα MOE  
  - Παραδείγματα Phi-3 / 3.5  
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) Δείγμα Κοινωνικών Μέσων](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [Δημιουργία Pipeline Retrieval-Augmented Generation (RAG) με NVIDIA NIM Phi-3 MOE, Azure AI Search και LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- Παραδείγματα Κλήσης Συναρτήσεων  
  - Παραδείγματα Phi-4 🆕  
    - [📓] [Χρήση Function Calling με Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [Χρήση Function Calling για δημιουργία πολλαπλών πρακτόρων με Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [Χρήση Function Calling με Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [Χρήση Function Calling με ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- Παραδείγματα Πολυτροπικού Μείγματος  
  - Παραδείγματα Phi-4 🆕  
    - [📓] [Χρήση Phi-4-multimodal ως Τεχνολογικός δημοσιογράφος](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [Εφαρμογή κονσόλας .NET που χρησιμοποιεί Phi-4-multimodal για ανάλυση εικόνων](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- Βελτιστοποίηση Phi Παραδειγμάτων  
  - [Σενάρια Βελτιστοποίησης](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [Βελτιστοποίηση έναντι RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [Αφήστε το Phi-3 να γίνει ειδικός της βιομηχανίας](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [Βελτιστοποίηση Phi-3 με το AI Toolkit για VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [Βελτιστοποίηση Phi-3 με Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)  
  - [Βελτιστοποίηση Phi-3 με Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [Βελτιστοποίηση Phi-3 με QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [Βελτιστοποίηση Phi-3 με Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [Βελτιστοποίηση Phi-3 με Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [Βελτιστοποίηση με Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [Hands-On Lab Βελτιστοποίησης με Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)  
  - [Βελτιστοποίηση Phi-3-vision με Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [Βελτιστοποίηση Phi-3 με Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)  
  - [Βελτιστοποίηση Phi-3-vision (επίσημη υποστήριξη)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [Βελτιστοποίηση Phi-3 με Kaito AKS, Azure Containers (επίσημη υποστήριξη)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [Βελτιστοποίηση Phi-3 και 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- Hands on Lab  
  - [Εξερεύνηση προηγμένων μοντέλων: LLMs, SLMs, τοπική ανάπτυξη και άλλα](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [Απελευθέρωση του δυναμικού NLP: Βελτιστοποίηση με Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- Ακαδημαϊκές Ερευνητικές Εργασίες και Δημοσιεύσεις  
  - [Textbooks Are All You Need II: phi-1.5 τεχνική αναφορά](https://arxiv.org/abs/2309.05463)  
  - [Phi-3 Τεχνική Αναφορά: Ένα ιδιαίτερα ικανό γλωσσικό μοντέλο τοπικά στο τηλέφωνό σας](https://arxiv.org/abs/2404.14219)  
  - [Phi-4 Τεχνική Αναφορά](https://arxiv.org/abs/2412.08905)  
  - [Phi-4-Mini Τεχνική Αναφορά: Συμπαγή αλλά ισχυρά πολυτροπικά γλωσσικά μοντέλα μέσω Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [Βελτιστοποίηση μικρών γλωσσικών μοντέλων για κλήση συναρτήσεων εντός οχήματος](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) Βελτιστοποίηση PHI-3 για απαντήσεις σε ερωτήσεις πολλαπλής επιλογής: Μεθοδολογία, Αποτελέσματα και Προκλήσεις](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning Technical Report](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning Technical Report](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## Χρήση των Μοντέλων Phi

### Phi στο Azure AI Foundry

Μπορείτε να μάθετε πώς να χρησιμοποιείτε το Microsoft Phi και πώς να δημιουργείτε ολοκληρωμένες λύσεις (E2E) σε διάφορες συσκευές υλικού. Για να δοκιμάσετε το Phi μόνοι σας, ξεκινήστε παίζοντας με τα μοντέλα και προσαρμόζοντας το Phi για τα δικά σας σενάρια χρησιμοποιώντας τον [Κατάλογο Μοντέλων Azure AI Foundry](https://aka.ms/phi3-azure-ai). Μπορείτε να μάθετε περισσότερα στο Getting Started με το [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Playground**  
Κάθε μοντέλο διαθέτει έναν ειδικό χώρο δοκιμών για να το εξερευνήσετε [Azure AI Playground](https://aka.ms/try-phi3).

### Phi στα Μοντέλα GitHub

Μπορείτε να μάθετε πώς να χρησιμοποιείτε το Microsoft Phi και πώς να δημιουργείτε ολοκληρωμένες λύσεις (E2E) σε διάφορες συσκευές υλικού. Για να δοκιμάσετε το Phi μόνοι σας, ξεκινήστε παίζοντας με το μοντέλο και προσαρμόζοντας το Phi για τα δικά σας σενάρια χρησιμοποιώντας τον [Κατάλογο Μοντέλων GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). Μπορείτε να μάθετε περισσότερα στο Getting Started με τον [Κατάλογο Μοντέλων GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**  
Κάθε μοντέλο διαθέτει έναν [χώρο δοκιμών για να το εξερευνήσετε](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi στο Hugging Face

Μπορείτε επίσης να βρείτε το μοντέλο στο [Hugging Face](https://huggingface.co/microsoft)

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Υπεύθυνη Τεχνητή Νοημοσύνη

Η Microsoft δεσμεύεται να βοηθά τους πελάτες της να χρησιμοποιούν τα προϊόντα AI υπεύθυνα, μοιράζοντας τις γνώσεις της και χτίζοντας σχέσεις εμπιστοσύνης μέσω εργαλείων όπως τα Transparency Notes και τις Impact Assessments. Πολλοί από αυτούς τους πόρους είναι διαθέσιμοι στο [https://aka.ms/RAI](https://aka.ms/RAI).  
Η προσέγγιση της Microsoft για την υπεύθυνη AI βασίζεται στις αρχές της για δικαιοσύνη, αξιοπιστία και ασφάλεια, ιδιωτικότητα και ασφάλεια, συμπερίληψη, διαφάνεια και λογοδοσία.

Τα μεγάλης κλίμακας μοντέλα φυσικής γλώσσας, εικόνας και ομιλίας - όπως αυτά που χρησιμοποιούνται σε αυτό το παράδειγμα - ενδέχεται να συμπεριφέρονται με τρόπους που είναι άδικοι, αναξιόπιστοι ή προσβλητικοί, προκαλώντας βλάβες. Παρακαλούμε συμβουλευτείτε το [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) για να ενημερωθείτε σχετικά με τους κινδύνους και τους περιορισμούς.

Η προτεινόμενη προσέγγιση για την αντιμετώπιση αυτών των κινδύνων είναι η ενσωμάτωση ενός συστήματος ασφάλειας στην αρχιτεκτονική σας που μπορεί να ανιχνεύει και να αποτρέπει επιβλαβείς συμπεριφορές. Το [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) παρέχει ένα ανεξάρτητο επίπεδο προστασίας, ικανό να ανιχνεύει επιβλαβές περιεχόμενο που δημιουργείται από χρήστες ή AI σε εφαρμογές και υπηρεσίες. Το Azure AI Content Safety περιλαμβάνει APIs για κείμενο και εικόνα που σας επιτρέπουν να εντοπίζετε επιβλαβές υλικό. Μέσα στο Azure AI Foundry, η υπηρεσία Content Safety σας επιτρέπει να δείτε, να εξερευνήσετε και να δοκιμάσετε δείγματα κώδικα για την ανίχνευση επιβλαβούς περιεχομένου σε διάφορες μορφές. Η ακόλουθη [τεκμηρίωση quickstart](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) σας καθοδηγεί στο πώς να κάνετε αιτήματα στην υπηρεσία.

Ένα ακόμα σημείο που πρέπει να λάβετε υπόψη είναι η συνολική απόδοση της εφαρμογής. Σε εφαρμογές με πολλαπλές μορφές και πολλαπλά μοντέλα, η απόδοση σημαίνει ότι το σύστημα λειτουργεί όπως εσείς και οι χρήστες σας περιμένετε, συμπεριλαμβανομένου του να μην παράγει επιβλαβή αποτελέσματα. Είναι σημαντικό να αξιολογείτε την απόδοση της συνολικής εφαρμογής σας χρησιμοποιώντας τους [Performance and Quality και Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). Έχετε επίσης τη δυνατότητα να δημιουργήσετε και να αξιολογήσετε με [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

Μπορείτε να αξιολογήσετε την AI εφαρμογή σας στο περιβάλλον ανάπτυξης χρησιμοποιώντας το [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). Δίνοντας είτε ένα test dataset είτε έναν στόχο, οι γεννήσεις της γενετικής AI εφαρμογής σας μετρώνται ποσοτικά με ενσωματωμένους evaluators ή custom evaluators της επιλογής σας. Για να ξεκινήσετε με το azure ai evaluation sdk και να αξιολογήσετε το σύστημά σας, μπορείτε να ακολουθήσετε τον [οδηγό quickstart](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Μόλις εκτελέσετε μια αξιολόγηση, μπορείτε να [οπτικοποιήσετε τα αποτελέσματα στο Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Εμπορικά Σήματα

Αυτό το έργο μπορεί να περιέχει εμπορικά σήματα ή λογότυπα για έργα, προϊόντα ή υπηρεσίες. Η εξουσιοδοτημένη χρήση των εμπορικών σημάτων ή λογότυπων της Microsoft υπόκειται και πρέπει να ακολουθεί τις [Οδηγίες Χρήσης Εμπορικών Σημάτων & Επωνυμίας της Microsoft](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
Η χρήση των εμπορικών σημάτων ή λογότυπων της Microsoft σε τροποποιημένες εκδόσεις αυτού του έργου δεν πρέπει να προκαλεί σύγχυση ή να υπονοεί χορηγία από τη Microsoft. Οποιαδήποτε χρήση εμπορικών σημάτων ή λογότυπων τρίτων υπόκειται στις πολιτικές αυτών των τρίτων.

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.