<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2e042b12a63c59931dc121c2c638bc58",
  "translation_date": "2025-07-09T18:32:53+00:00",
  "source_file": "README.md",
  "language_code": "he"
}
-->
# ספר המתכונים של Phi: דוגמאות מעשיות עם דגמי Phi של מיקרוסופט

[![פתח והשתמש בדוגמאות ב-GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![פתח ב-Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![תורמים ב-GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![בעיות ב-GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![בקשות משיכה ב-GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![ברוכים הבאים ל-PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![עוקבים ב-GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![מזלגות ב-GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![כוכבים ב-GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![קהילת Azure AI ב-Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi היא סדרת דגמי AI בקוד פתוח שפותחה על ידי מיקרוסופט.

Phi כיום הוא הדגם הקטן (SLM) החזק והיעיל ביותר מבחינת עלות, עם ביצועים מצוינים במבחנים במגוון שפות, יכולות הסקה, יצירת טקסט/שיחה, קידוד, תמונות, אודיו ותסריטים נוספים.

ניתן לפרוס את Phi בענן או במכשירי קצה, וניתן בקלות לבנות יישומי AI גנרטיביים עם כוח מחשוב מוגבל.

עקבו אחר השלבים הבאים כדי להתחיל להשתמש במשאבים אלו:  
1. **צור מזלג של המאגר**: לחץ על [![מזלגות ב-GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **שכפל את המאגר**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**הצטרף לקהילת ה-Discord של מיקרוסופט AI ופגוש מומחים ומפתחים נוספים**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

## 🌐 תמיכה בריבוי שפות

### נתמך באמצעות GitHub Action (אוטומטי ותמיד מעודכן)

[צרפתית](../fr/README.md) | [ספרדית](../es/README.md) | [גרמנית](../de/README.md) | [רוסית](../ru/README.md) | [ערבית](../ar/README.md) | [פרסית (פרסי)](../fa/README.md) | [אורדו](../ur/README.md) | [סינית (מפושטת)](../zh/README.md) | [סינית (מסורתית, מקאו)](../mo/README.md) | [סינית (מסורתית, הונג קונג)](../hk/README.md) | [סינית (מסורתית, טייוואן)](../tw/README.md) | [יפנית](../ja/README.md) | [קוריאנית](../ko/README.md) | [הינדי](../hi/README.md)  
[בנגלית](../bn/README.md) | [מרטהי](../mr/README.md) | [נפאלית](../ne/README.md) | [פונג'אבית (גורמוכי)](../pa/README.md) | [פורטוגזית (פורטוגל)](../pt/README.md) | [פורטוגזית (ברזיל)](../br/README.md) | [איטלקית](../it/README.md) | [פולנית](../pl/README.md) | [טורקית](../tr/README.md) | [יוונית](../el/README.md) | [תאית](../th/README.md) | [שוודית](../sv/README.md) | [דנית](../da/README.md) | [נורווגית](../no/README.md) | [פינית](../fi/README.md) | [הולנדית](../nl/README.md) | [עברית](./README.md) | [וייטנאמית](../vi/README.md) | [אינדונזית](../id/README.md) | [מלאית](../ms/README.md) | [טגלוג (פיליפינית)](../tl/README.md) | [סווהילית](../sw/README.md) | [הונגרית](../hu/README.md) | [צ'כית](../cs/README.md) | [סלובקית](../sk/README.md) | [רומנית](../ro/README.md) | [בולגרית](../bg/README.md) | [סרבית (קירילית)](../sr/README.md) | [קרואטית](../hr/README.md) | [סלובנית](../sl/README.md)

## תוכן העניינים

- מבוא  
  - [ברוכים הבאים למשפחת Phi](./md/01.Introduction/01/01.PhiFamily.md)  
  - [הגדרת הסביבה שלך](./md/01.Introduction/01/01.EnvironmentSetup.md)  
  - [הבנת טכנולוגיות מפתח](./md/01.Introduction/01/01.Understandingtech.md)  
  - [בטיחות AI לדגמי Phi](./md/01.Introduction/01/01.AISafety.md)  
  - [תמיכה בחומרה של Phi](./md/01.Introduction/01/01.Hardwaresupport.md)  
  - [דגמי Phi וזמינות בפלטפורמות שונות](./md/01.Introduction/01/01.Edgeandcloud.md)  
  - [שימוש ב-Guidance-ai ו-Phi](./md/01.Introduction/01/01.Guidance.md)  
  - [דגמים ב-GitHub Marketplace](https://github.com/marketplace/models)  
  - [קטלוג דגמי Azure AI](https://ai.azure.com)

- הפעלת Phi בסביבות שונות  
  - [Hugging face](./md/01.Introduction/02/01.HF.md)  
  - [דגמי GitHub](./md/01.Introduction/02/02.GitHubModel.md)  
  - [קטלוג דגמי Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)  
  - [Ollama](./md/01.Introduction/02/04.Ollama.md)  
  - [AI Toolkit ב-VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)  
  - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)  
  - [Foundry מקומי](./md/01.Introduction/02/07.FoundryLocal.md)

- הפעלת משפחת Phi  
  - [הפעלה ב-iOS](./md/01.Introduction/03/iOS_Inference.md)  
  - [הפעלה באנדרואיד](./md/01.Introduction/03/Android_Inference.md)  
  - [הפעלה ב-Jetson](./md/01.Introduction/03/Jetson_Inference.md)  
  - [הפעלה במחשב AI](./md/01.Introduction/03/AIPC_Inference.md)  
  - [הפעלה עם Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)  
  - [הפעלה בשרת מקומי](./md/01.Introduction/03/Local_Server_Inference.md)  
  - [הפעלה בשרת מרוחק באמצעות AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)  
  - [הפעלה עם Rust](./md/01.Introduction/03/Rust_Inference.md)  
  - [הפעלה של Phi--Vision במחשב מקומי](./md/01.Introduction/03/Vision_Inference.md)  
  - [הפעלה עם Kaito AKS, Azure Containers (תמיכה רשמית)](./md/01.Introduction/03/Kaito_Inference.md)  
- [כימות משפחת Phi](./md/01.Introduction/04/QuantifyingPhi.md)  
  - [כימות Phi-3.5 / 4 באמצעות llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)  
  - [כימות Phi-3.5 / 4 באמצעות הרחבות AI גנרטיביות ל-onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)  
  - [כימות Phi-3.5 / 4 באמצעות Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)  
  - [כימות Phi-3.5 / 4 באמצעות Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- הערכת Phi  
  - [AI אחראי](./md/01.Introduction/05/ResponsibleAI.md)  
  - [Azure AI Foundry להערכה](./md/01.Introduction/05/AIFoundry.md)  
  - [שימוש ב-Promptflow להערכה](./md/01.Introduction/05/Promptflow.md)

- RAG עם Azure AI Search  
  - [כיצד להשתמש ב-Phi-4-mini ו-Phi-4-multimodal (RAG) עם Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- דוגמאות לפיתוח יישומי Phi  
  - יישומי טקסט ושיחה  
    - דוגמאות Phi-4 🆕  
      - [📓] [שיחה עם דגם Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)  
      - [שיחה עם דגם Phi-4 מקומי ONNX ב-.NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)  
      - [אפליקציית שיחה בקונסולה .NET עם Phi-4 ONNX באמצעות Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)  
    - דוגמאות Phi-3 / 3.5  
      - [צ'אטבוט מקומי בדפדפן באמצעות Phi3, ONNX Runtime Web ו-WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)  
      - [צ'אט OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)  
      - [רב-דגם - אינטראקטיבי Phi-3-mini ו-OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)  
      - [MLFlow - בניית עטיפה ושימוש ב-Phi-3 עם MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)  
      - [אופטימיזציית דגם - איך לאופטימיזציה של דגם Phi-3-min עבור ONNX Runtime Web עם Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)  
      - [אפליקציית WinUI3 עם Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)  
      - [דוגמת אפליקציית WinUI3 לרשימות מופעלות AI עם דגמים מרובים](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [כיוונון עדין ואינטגרציה של דגמי Phi-3 מותאמים אישית עם Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [כיוונון עדין ואינטגרציה של דגמי Phi-3 מותאמים אישית עם Prompt flow ב-Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [הערכת דגם Phi-3 / Phi-3.5 מכוונן עדין ב-Azure AI Foundry עם דגש על עקרונות ה-AI האחראי של מיקרוסופט](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [דוגמת חיזוי שפה Phi-3.5-mini-instruct (סינית/אנגלית)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [צ׳אטבוט RAG מבוסס Phi-3.5-Instruct WebGPU](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [שימוש ב-GPU של Windows ליצירת פתרון Prompt flow עם Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [שימוש ב-Microsoft Phi-3.5 tflite ליצירת אפליקציית אנדרואיד](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [דוגמת שאלות ותשובות ב-.NET עם דגם Phi-3 מקומי מבוסס ONNX באמצעות Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [אפליקציית צ׳אט קונסול ב-.NET עם Semantic Kernel ו-Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- דוגמאות קוד מבוססות Azure AI Inference SDK  
  - דוגמאות Phi-4 🆕  
    - [📓] [יצירת קוד פרויקט באמצעות Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - דוגמאות Phi-3 / 3.5  
    - [בנה את סוכן הצ׳אט GitHub Copilot שלך ב-Visual Studio Code עם משפחת Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [צור סוכן צ׳אט GitHub ב-Visual Studio Code עם Phi-3.5 באמצעות דגמי GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- דוגמאות חשיבה מתקדמת  
  - דוגמאות Phi-4 🆕  
    - [📓] [דוגמאות Phi-4-mini-reasoning או Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [כיוונון עדין של Phi-4-mini-reasoning עם Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [כיוונון עדין של Phi-4-mini-reasoning עם Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Phi-4-mini-reasoning עם דגמי GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Phi-4-mini-reasoning עם דגמי Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- הדגמות  
    - [הדגמות Phi-4-mini מתארחות ב-Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [הדגמות Phi-4-multimodal מתארחות ב-Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- דוגמאות ראייה  
  - דוגמאות Phi-4 🆕  
    - [📓] [שימוש ב-Phi-4-multimodal לקריאת תמונות ויצירת קוד](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - דוגמאות Phi-3 / 3.5  
    - [📓][Phi-3-vision - המרת טקסט מתמונה לטקסט](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [הדגמה: מיחזור Phi-3](https://github.com/jennifermarsman/PhiRecycling/)  
    - [עוזר שפה חזותית Phi-3-vision עם Phi3-Vision ו-OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][דוגמת Phi-3.5 Vision עם מסגרות מרובות או תמונות מרובות](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [דגם מקומי של Phi-3 Vision מבוסס ONNX עם Microsoft.ML.OnnxRuntime ב-.NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [דגם מקומי מבוסס תפריט של Phi-3 Vision ONNX עם Microsoft.ML.OnnxRuntime ב-.NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- דוגמאות מתמטיקה  
  - דוגמאות Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [הדגמת מתמטיקה עם Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)  

- דוגמאות אודיו  
  - דוגמאות Phi-4 🆕  
    - [📓] [חילוץ תמלולים מאודיו באמצעות Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [דוגמת אודיו Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [דוגמת תרגום דיבור Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [אפליקציית קונסול .NET המשתמשת ב-Phi-4-multimodal לניתוח קובץ אודיו ויצירת תמלול](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- דוגמאות MOE  
  - דוגמאות Phi-3 / 3.5  
    - [📓] [דוגמת דגמי Phi-3.5 Mixture of Experts (MoEs) לרשתות חברתיות](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [בניית צינור Retrieval-Augmented Generation (RAG) עם NVIDIA NIM Phi-3 MOE, Azure AI Search ו-LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- דוגמאות קריאת פונקציות  
  - דוגמאות Phi-4 🆕  
    - [📓] [שימוש בקריאת פונקציות עם Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [שימוש בקריאת פונקציות ליצירת סוכנים מרובים עם Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [שימוש בקריאת פונקציות עם Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [שימוש בקריאת פונקציות עם ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- דוגמאות מיקס מולטימודלי  
  - דוגמאות Phi-4 🆕  
    - [📓] [שימוש ב-Phi-4-multimodal כעיתונאי טכנולוגיה](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [אפליקציית קונסול .NET המשתמשת ב-Phi-4-multimodal לניתוח תמונות](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- כיוונון עדין של דגמי Phi  
  - [תרחישי כיוונון עדין](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [כיוונון עדין מול RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [כיוונון עדין: הפוך את Phi-3 למומחה תעשייתי](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [כיוונון עדין של Phi-3 עם AI Toolkit ל-VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [כיוונון עדין של Phi-3 עם Azure Machine Learning Service](./md/03.FineTuning/Introduce_AzureML.md)  
  - [כיוונון עדין של Phi-3 עם Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [כיוונון עדין של Phi-3 עם QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [כיוונון עדין של Phi-3 עם Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [כיוונון עדין של Phi-3 עם Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [כיוונון עדין עם Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [כיוונון עדין עם Microsoft Olive - מעבדה מעשית](./md/03.FineTuning/olive-lab/readme.md)  
  - [כיוונון עדין של Phi-3-vision עם Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [כיוונון עדין של Phi-3 עם Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)  
  - [כיוונון עדין של Phi-3-vision (תמיכה רשמית)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [כיוונון עדין של Phi-3 עם Kaito AKS, Azure Containers (תמיכה רשמית)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [כיוונון עדין של Phi-3 ו-Phi-3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- מעבדות מעשיות  
  - [חקירת דגמים מתקדמים: LLMs, SLMs, פיתוח מקומי ועוד](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [שחרור הפוטנציאל של NLP: כיוונון עדין עם Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- מאמרים אקדמיים ופרסומים  
  - [Textbooks Are All You Need II: דוח טכני phi-1.5](https://arxiv.org/abs/2309.05463)  
  - [דוח טכני Phi-3: דגם שפה מתקדם הפועל מקומית בטלפון שלך](https://arxiv.org/abs/2404.14219)  
  - [דוח טכני Phi-4](https://arxiv.org/abs/2412.08905)  
  - [דוח טכני Phi-4-Mini: דגמי שפה מולטימודל קומפקטיים וחזקים באמצעות Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [אופטימיזציה של דגמי שפה קטנים לקריאת פונקציות ברכב](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) כיוונון עדין של PHI-3 למענה על שאלות רב-ברירתיות: מתודולוגיה, תוצאות ואתגרים](https://arxiv.org/abs/2501.01588)
- [Phi-4-reasoning דוח טכני](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning דוח טכני](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## שימוש במודלים של Phi

### Phi ב-Azure AI Foundry

ניתן ללמוד כיצד להשתמש ב-Microsoft Phi וכיצד לבנות פתרונות E2E במכשירים שונים שלך. כדי לחוות את Phi בעצמך, התחל לשחק עם המודלים ולהתאים את Phi לתרחישים שלך באמצעות [קטלוג המודלים של Azure AI Foundry](https://aka.ms/phi3-azure-ai). ניתן ללמוד עוד ב-Getting Started עם [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**Playground**  
לכל מודל יש מגרש משחקים ייעודי לבחינת המודל [Azure AI Playground](https://aka.ms/try-phi3).

### Phi במודלים של GitHub

ניתן ללמוד כיצד להשתמש ב-Microsoft Phi וכיצד לבנות פתרונות E2E במכשירים שונים שלך. כדי לחוות את Phi בעצמך, התחל לשחק עם המודל ולהתאים את Phi לתרחישים שלך באמצעות [קטלוג המודלים של GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). ניתן ללמוד עוד ב-Getting Started עם [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**  
לכל מודל יש [playground ייעודי לבחינת המודל](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi ב-Hugging Face

ניתן גם למצוא את המודל ב-[Hugging Face](https://huggingface.co/microsoft)

**Playground**  
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## AI אחראי

Microsoft מחויבת לסייע ללקוחותינו להשתמש במוצרי ה-AI שלנו באחריות, לשתף את הידע שצברנו ולבנות שותפויות מבוססות אמון באמצעות כלים כמו Transparency Notes ו-Impact Assessments. משאבים רבים אלה זמינים ב-[https://aka.ms/RAI](https://aka.ms/RAI).  
הגישה של Microsoft ל-AI אחראי מבוססת על עקרונות ה-AI שלנו: הוגנות, אמינות ובטיחות, פרטיות ואבטחה, הכללה, שקיפות ואחריות.

מודלים רחבי היקף של שפה טבעית, תמונה ודיבור - כמו אלה שבדוגמה זו - עלולים להתנהג בצורה לא הוגנת, לא אמינה או פוגענית, ולגרום לנזקים. יש לעיין ב-[Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) כדי להתעדכן בסיכונים והמגבלות.

הגישה המומלצת להפחתת סיכונים אלה היא לכלול מערכת בטיחות בארכיטקטורה שלך שיכולה לזהות ולמנוע התנהגות מזיקה. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) מספק שכבת הגנה עצמאית, המסוגלת לזהות תוכן מזיק שנוצר על ידי משתמשים או על ידי AI באפליקציות ושירותים. Azure AI Content Safety כוללת APIs לטקסט ותמונה המאפשרים לזהות חומר מזיק. בתוך Azure AI Foundry, שירות Content Safety מאפשר לך לצפות, לחקור ולנסות דוגמאות קוד לזיהוי תוכן מזיק במגוון מודאליות. התיעוד הבא [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) מדריך אותך כיצד לבצע בקשות לשירות.

היבט נוסף שיש לקחת בחשבון הוא ביצועי האפליקציה הכוללים. באפליקציות רב-מודאליות ורב-מודליות, אנו מגדירים ביצועים כהתנהגות המערכת כפי שאתה והמשתמשים שלך מצפים, כולל אי יצירת פלטים מזיקים. חשוב להעריך את ביצועי האפליקציה הכוללת שלך באמצעות [Performance and Quality and Risk and Safety evaluators](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). בנוסף, יש לך אפשרות ליצור ולהעריך באמצעות [custom evaluators](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

ניתן להעריך את אפליקציית ה-AI שלך בסביבת הפיתוח שלך באמצעות [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). בהתבסס על מערך נתונים לבחינה או יעד, הדורות של אפליקציית ה-AI הגנרטיבית שלך נמדדים כמותית באמצעות evaluators מובנים או evaluators מותאמים אישית לבחירתך. כדי להתחיל עם azure ai evaluation sdk להערכת המערכת שלך, ניתן לעקוב אחר [מדריך quickstart](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). לאחר ביצוע ריצת הערכה, ניתן [להציג את התוצאות ב-Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## סימני מסחר

פרויקט זה עשוי להכיל סימני מסחר או לוגואים של פרויקטים, מוצרים או שירותים. השימוש המורשה בסימני המסחר או בלוגואים של Microsoft כפוף ל-[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
שימוש בסימני המסחר או בלוגואים של Microsoft בגרסאות מותאמות של פרויקט זה אסור שיגרום לבלבול או ייצור רושם של חסות מצד Microsoft. כל שימוש בסימני מסחר או לוגואים של צדדים שלישיים כפוף למדיניות של אותם צדדים.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.