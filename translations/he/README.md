# ספר המתכונים של Phi: דוגמאות מעשיות עם דגמי Phi של מיקרוסופט

[![פתח והשתמש בדוגמאות בתוך GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![פתח ב-Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![תורמים ב-GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![נושאים ב-GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![בקשות משיכה ב-GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![עוקבים ב-GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![מזלגות ב-GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![כוכבים ב-GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi היא סדרה של דגמי AI בקוד פתוח שפותחה על ידי מיקרוסופט.

כיום, Phi הוא דגם שפה קטן (SLM) החזק והיעיל ביותר מבחינת עלות, עם מדדי ביצועים טובים מאוד בריבוי שפות, היגיון, יצירת טקסט/שיחות, קידוד, תמונות, שמע וסצנריואים אחרים.

ניתן לפרוס את Phi לענן או למכשירי קצה, וניתן לבנות בקלות יישומי AI גנרטיביים עם כוח מחשוב מוגבל.

עקבו אחרי השלבים הבאים כדי להתחיל להשתמש במשאבים האלו:
1. **יצירת מזלג מהמאגר**: לחץ על [![מזלגות ב-GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **שכפול המאגר**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**הצטרף לקהילת Microsoft AI ב-Discord ופגש מומחים ומפתחים נוספים**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/he/cover.eb18d1b9605d754b.webp)

### 🌐 תמיכה מרובת שפות

#### נתמכת באמצעות GitHub Action (אוטומטית ותמיד מעודכנת)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[ערבית](../ar/README.md) | [בנגלית](../bn/README.md) | [בולגרית](../bg/README.md) | [בירמזית (מיאנמר)](../my/README.md) | [סינית (מפושטת)](../zh-CN/README.md) | [סינית (מסורתית, הונג קונג)](../zh-HK/README.md) | [סינית (מסורתית, מקאו)](../zh-MO/README.md) | [סינית (מסורתית, טאיוואן)](../zh-TW/README.md) | [קרואטית](../hr/README.md) | [צ'כית](../cs/README.md) | [דנית](../da/README.md) | [הולנדית](../nl/README.md) | [אסטונית](../et/README.md) | [פינית](../fi/README.md) | [צרפתית](../fr/README.md) | [גרמנית](../de/README.md) | [יוונית](../el/README.md) | [עברית](./README.md) | [הינדית](../hi/README.md) | [הונגרית](../hu/README.md) | [אינדונזית](../id/README.md) | [איטלקית](../it/README.md) | [יפנית](../ja/README.md) | [קנאדה](../kn/README.md) | [קוריאנית](../ko/README.md) | [ליטאית](../lt/README.md) | [מלאית](../ms/README.md) | [מאליאלאם](../ml/README.md) | [מרטהית](../mr/README.md) | [נפאלית](../ne/README.md) | [פידג׳ין ניגרי](../pcm/README.md) | [נורווגית](../no/README.md) | [פרסית (פרסית)](../fa/README.md) | [פולנית](../pl/README.md) | [פורטוגזית (ברזיל)](../pt-BR/README.md) | [פורטוגזית (פורטוגל)](../pt-PT/README.md) | [פנג'אבי (גורמוקי)](../pa/README.md) | [רומנית](../ro/README.md) | [רוסית](../ru/README.md) | [סרבית (קירילית)](../sr/README.md) | [סלובקית](../sk/README.md) | [סלובנית](../sl/README.md) | [ספרדית](../es/README.md) | [סווהילית](../sw/README.md) | [שוודית](../sv/README.md) | [טגאלוג (פיליפינית)](../tl/README.md) | [טמילית](../ta/README.md) | [טלוגו](../te/README.md) | [תאית](../th/README.md) | [טורקית](../tr/README.md) | [אוקראינית](../uk/README.md) | [אורדו](../ur/README.md) | [וייטנאמית](../vi/README.md)

> **מעדיפים שכפול מקומי?**

> מאגר זה כולל למעלה מ-50 תרגומים לשפות שונות שמגבירים משמעותית את גודל ההורדה. כדי לשכפל ללא תרגומים, השתמשו בספיירס אאוט:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> כך תקבלו את כל מה שצריך לסיים את הקורס במהירות הורדה רבה יותר.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## תוכן העניינים

- מבוא
  - [ברוכים הבאים למשפחת Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [הגדרת הסביבה שלך](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [הבנת טכנולוגיות מרכזיות](./md/01.Introduction/01/01.Understandingtech.md)
  - [בטיחות AI לדגמי Phi](./md/01.Introduction/01/01.AISafety.md)
  - [תמיכה בחומרה של Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [דגמי Phi וזמינות בפלטפורמות השונות](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [שימוש ב-Guidance-ai ו-Phi](./md/01.Introduction/01/01.Guidance.md)
  - [דגמים ב-GitHub Marketplace](https://github.com/marketplace/models)
  - [קטלוג דגמים של Azure AI](https://ai.azure.com)

- אינפרנס Phi בסביבות שונות
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [דגמים ב-GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [קטלוג דגמי Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- אינפרנס משפחת Phi
    - [אינפרנס Phi ב-iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [אינפרנס Phi באנדרואיד](./md/01.Introduction/03/Android_Inference.md)
    - [אינפרנס Phi ב-Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [אינפרנס Phi במחשב AI PC](./md/01.Introduction/03/AIPC_Inference.md)
    - [אינפרנס Phi עם Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [אינפרנס Phi בשרת מקומי](./md/01.Introduction/03/Local_Server_Inference.md)
    - [אינפרנס Phi בשרת מרוחק באמצעות AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [אינפרנס Phi עם Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [אינפרנס Phi--חזון במחשב מקומי](./md/01.Introduction/03/Vision_Inference.md)
    - [אינפרנס Phi עם Kaito AKS, Azure Containers (תמיכה רשמית)](./md/01.Introduction/03/Kaito_Inference.md)
-  [כימות משפחת Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [כימות Phi-3.5 / 4 באמצעות llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [כימות Phi-3.5 / 4 באמצעות הרחבות AI גנרטיביות ל-onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [כימות Phi-3.5 / 4 באמצעות Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [כימות Phi-3.5 / 4 באמצעות Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  הערכה של Phi
    - [AI אחראי](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry להערכה](./md/01.Introduction/05/AIFoundry.md)
    - [שימוש ב-Promptflow להערכה](./md/01.Introduction/05/Promptflow.md)
 
- RAG עם חיפוש Azure AI
    - [כיצד להשתמש ב-Phi-4-mini ו-Phi-4-multimodal(RAG) עם חיפוש Azure AI](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- דוגמאות פיתוח יישומים עם Phi
  - יישומי טקסט ושיחות
    - דוגמאות Phi-4 🆕
      - [📓] [שיחה עם דגם Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [שיחה עם דגם Phi-4 ONNX מקומי ב-.NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [שיחת Console App ב-.NET עם Phi-4 ONNX באמצעות Sementic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - דוגמאות Phi-3 / 3.5
      - [צ׳אטבוט מקומי בדפדפן המשתמש ב-Phi3, ONNX Runtime Web ו-WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [שיחת OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [רב-מודל - Phi-3-mini אינטראקטיבי ו-OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - בניית עטיפה ושימוש ב-Phi-3 עם MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [אופטימיזציית מודל - כיצד לאופטם את מודל Phi-3-min עבור ONNX Runtime Web עם Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [אפליקציית WinUI3 עם Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [דוגמת אפליקציית הערות מבוססת AI רב-מודלית WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [כיוונון עדין ואינטגרציה של מודלים מותאמים אישית Phi-3 עם Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [כיוונון עדין ואינטגרציה של מודלים מותאמים אישית Phi-3 עם Prompt flow ב-Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [הערכת מודל Phi-3 / Phi-3.5 מכוונן עדין ב-Azure AI Foundry עם מיקוד בעקרונות AI אחראי של מיקרוסופט](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [דוגמת חיזוי שפה Phi-3.5-mini-instruct (סינית/אנגלית)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [צ'אטבוט Phi-3.5-Instruct WebGPU RAG](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [שימוש ב-GPU של Windows ליצירת פתרון Prompt flow עם Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [שימוש ב-Phi-3.5 tflite של מיקרוסופט ליצירת אפליקציית אנדרואיד](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [דוגמת שאלות ותשובות .NET עם מודל ONNX מקומי של Phi-3 בעזרת Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [אפליקציית צ'אט קונסול .NET עם Semantic Kernel ו-Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - דוגמאות מבוססות קוד של Azure AI Inference SDK 
    - דוגמאות Phi-4 🆕
      - [📓] [יצירת קוד פרויקט באמצעות Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - דוגמאות Phi-3 / 3.5
      - [בנה את צ'אט GitHub Copilot שלך בוויז'ואל סטודיו קוד עם משפחת Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [צור סוכן צ'אט משולב בוויז'ואל סטודיו קוד עם Phi-3.5 בעזרת מודלים של GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - דוגמאות הסקה מתקדמת
    - דוגמאות Phi-4 🆕
      - [📓] [דוגמאות Phi-4-mini-reasoning או Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [כיוונון עדין של Phi-4-mini-reasoning עם Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [כיוונון עדין של Phi-4-mini-reasoning עם Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning עם מודלים של GitHub](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-reasoning עם מודלים של Azure AI Foundry](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - הדגמות
      - [דוגמאות Phi-4-mini המתארחות ב-Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [דוגמאות Phi-4-multimodal המתארחות ב-Hugginge Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - דוגמאות ראייה
    - דוגמאות Phi-4 🆕
      - [📓] [שימוש ב-Phi-4-multimodal לקריאת תמונות ויצירת קוד](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - דוגמאות Phi-3 / 3.5
      -  [📓][Phi-3-vision-טקסט תמונה לטקסט](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [הדגמה: מיחזור Phi-3](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - עוזר שפה חזותית - עם Phi3-Vision ו-OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][דוגמת ראייה רב-מסגרת או רב-תמונה של Phi-3.5 Vision](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [מודל ONNX לוקאלי של Phi-3 Vision באמצעות Microsoft.ML.OnnxRuntime ב-.NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [מודל ONNX לוקאלי של Phi-3 Vision מבוסס תפריט באמצעות Microsoft.ML.OnnxRuntime ב-.NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - דוגמאות מתמטיקה
    -  דוגמאות Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [דמו מתמטי עם Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - דוגמאות שמע
    - דוגמאות Phi-4 🆕
      - [📓] [הפקת תמלילים של שמע באמצעות Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [דוגמת שמע Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [דוגמת תרגום דיבור Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [אפליקציית קונסול .NET המשתמשת ב-Phi-4-multimodal שמע לניתוח קובץ שמע ויצירת תמלול](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - דוגמאות MOE
    - דוגמאות Phi-3 / 3.5
      - [📓] [מודלי אריזת מומחים מעורבת (MoEs) Phi-3.5 - דוגמת רשתות חברתיות](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [בניית צינור ייצור הנתמך בשאילתות (RAG) עם NVIDIA NIM Phi-3 MOE, Azure AI Search ו-LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - דוגמאות קריאת פונקציות
    - דוגמאות Phi-4 🆕
      -  [📓] [שימוש בקריאת פונקציה עם Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [שימוש בקריאת פונקציה ליצירת סוכנים מרובים עם Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [שימוש בקריאת פונקציה עם Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [שימוש בקריאת פונקציה עם ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - דוגמאות מיקס רב-מודלי
    - דוגמאות Phi-4 🆕
      -  [📓] [שימוש ב-Phi-4-multimodal כתב טכנולוגי](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [אפליקציית קונסול .NET המשתמשת ב-Phi-4-multimodal לניתוח תמונות](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- כיוונון עדין של דוגמאות Phi
  - [תסריטי כיוונון עדין](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [כיוונון עדין מול RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [כיוונון עדין כדי לאפשר ל-Phi-3 להפוך למומחה תעשייתי](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [כיוונון עדין של Phi-3 עם כלי AI עבור VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [כיוונון עדין של Phi-3 עם שירות Azure Machine Learning](./md/03.FineTuning/Introduce_AzureML.md)
  - [כיוונון עדין של Phi-3 עם Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [כיוונון עדין של Phi-3 עם QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [כיוונון עדין של Phi-3 עם Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [כיוונון עדין של Phi-3 עם Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [כיוונון עדין עם Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [כיוונון עדין עם מעבדה מעשית של Microsoft Olive](./md/03.FineTuning/olive-lab/readme.md)
  - [כיוונון עדין של Phi-3-vision עם Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [כיוונון עדין של Phi-3 עם Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [כיוונון עדין של Phi-3-vision (תמיכה רשמית)](./md/03.FineTuning/FineTuning_Vision.md)
  - [כיוונון עדין של Phi-3 עם Kaito AKS , מכולות Azure (תמיכה רשמית)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [כיוונון עדין של Phi-3 ו-3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- מעבדה מעשית
  - [חקירת מודלים מתקדמים: LLMs, SLMs, פיתוח מקומי ועוד](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [שחרור פוטנציאל NLP: כיוונון עדין עם Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- מאמרים אקדמיים ופרסומים
  - [ספרי לימוד הם כל מה שצריך II: הדו"ח הטכני של phi-1.5](https://arxiv.org/abs/2309.05463)
  - [דו"ח טכני של Phi-3: דגם שפה רב-יכולת לזמין מקומית בטלפון שלך](https://arxiv.org/abs/2404.14219)
  - [דו"ח טכני של Phi-4](https://arxiv.org/abs/2412.08905)
  - [דו"ח טכני של Phi-4-Mini: דגמי שפה מולטימודל קומפקטיים אך רבי עוצמה באמצעות תערובת של LoRA](https://arxiv.org/abs/2503.01743)
  - [אופטימיזציה של דגמי שפה קטנים לפונקציית קריאת פונקציות ברכב](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) כיוונון עדין של PHI-3 למענה על שאלות רב-ברירתיות: שיטה, תוצאות ואתגרים](https://arxiv.org/abs/2501.01588)
  - [דו"ח טכני על נימוקים של Phi-4](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [דו"ח טכני על נימוקים של Phi-4-mini](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## שימוש בדגמי Phi

### Phi ב-Azure AI Foundry

אתה יכול ללמוד כיצד להשתמש ב-Microsoft Phi וכיצד לבנות פתרונות מקצה לקצה במכשירי החומרה השונים שלך. כדי לחוות את Phi בעצמך, התחל לשחק עם הדגמים ולהתאים את Phi לתרחישים שלך באמצעות קטלוג דגמי Azure AI Foundry ב-[Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). תוכל ללמוד עוד ב-Getting Started עם [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**מגרש משחקים**  
לכל דגם יש מגרש משחקים ייעודי לבדיקת הדגם ב-[Azure AI Playground](https://aka.ms/try-phi3).

### Phi בדגמי GitHub

אתה יכול ללמוד כיצד להשתמש ב-Microsoft Phi וכיצד לבנות פתרונות מקצה לקצה במכשירי החומרה השונים שלך. כדי לחוות את Phi בעצמך, התחל לשחק עם הדגם ולהתאים את Phi לתרחישים שלך באמצעות קטלוג דגמי GitHub ב-[GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). תוכל ללמוד עוד ב-Getting Started עם [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**מגרש משחקים**  
לכל דגם יש [מגרש משחקים ייעודי לבדיקת הדגם](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi ב-Hugging Face

תוכל גם למצוא את הדגם ב-[Hugging Face](https://huggingface.co/microsoft)

**מגרש משחקים**  
[מגרש משחקים של Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 קורסים נוספים

הצוות שלנו מייצר קורסים נוספים! בדוק:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j למתחילים](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js למתחילים](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain למתחילים](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / סוכנים
[![AZD למתחילים](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI למתחילים](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP למתחילים](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![סוכני AI למתחילים](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### סדרת AI מייצר
[![AI מייצר למתחילים](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI מייצר (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![AI מייצר (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![AI מייצר (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### לימוד יסוד
[![ML למתחילים](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![מדע נתונים למתחילים](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI למתחילים](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![סייברסקיוריטי למתחילים](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![פיתוח ווב למתחילים](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT למתחילים](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![פיתוח XR למתחילים](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### סדרת Copilot
[![Copilot לתכנות משותף עם AI](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot ל-C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![הרפתקה עם Copilot](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## AI אחראי

מיקרוסופט מתחייבת לסייע ללקוחותיה להשתמש במוצרי ה-AI שלנו באחריות, לשתף את הלמידות שלנו ולבנות שותפויות מבוססות אמון באמצעות כלים כמו הערות שקיפות והערכות השפעה. משאבים רבים אלה ניתן למצוא ב-[https://aka.ms/RAI](https://aka.ms/RAI).  
הגישה של מיקרוסופט ל-AI אחראי נשענת על עקרונות ה-AI שלנו: הוגנות, אמינות ובטיחות, פרטיות ואבטחה, הכללה, שקיפות ואחריות.

דגמי שפה, תמונה ודיבור בקנה מידה גדול - כמו אלה שבדוגמה זו - עלולים להתנהג באופן לא הוגן, לא אמין או פוגעני, ובכך לגרום נזק. אנא עיין ב-[הערת שקיפות שירות Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) כדי להתעדכן בסיכונים והמגבלות.

הגישה המומלצת למיתון סיכונים אלה היא לכלול מערכת בטיחות באדריכלות שלך שיכולה לזהות ולמנוע התנהגות מזיקה. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) מספק שכבת הגנה עצמאית, המסוגלת לזהות תוכן מזיק שנוצר על ידי משתמשים ו-AI באפליקציות ובשירותים. שירות Content Safety של Azure AI כולל API לטקסט ותמונה המאפשרים לזהות חומר מזיק. בתוך Azure AI Foundry, שירות Content Safety מאפשר לך לצפות, לחקור ולנסות דוגמאות קוד לזיהוי תוכן מזיק במגוון מדיומים. התיעוד הבא של [התחלת עבודה מהירה](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ידריך אותך כיצד לבצע בקשות לשירות.
היבט נוסף שיש לקחת בחשבון הוא ביצועי היישום הכוללים. עם יישומים רב-מודאליים ורב-מודליים, אנו מתייחסים לביצועים כאל כך שהמערכת מתפקדת כפי שאתה והמשתמשים שלך מצפים, כולל אי-יצירת פלטים מזיקים. חשוב להעריך את ביצועי היישום הכולל שלך באמצעות [בוחני ביצועים, איכות, סיכון ובטיחות](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). בנוסף, יש לך אפשרות ליצור ולהעריך באמצעות [בוחנים מותאמים אישית](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

אתה יכול להעריך את יישום ה-AI שלך בסביבת הפיתוח שלך באמצעות ה-[Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). כאשר יש לך סט נתוני בדיקה או מטרה, הדורות של יישום ה-AI שלך נמדדים כמותית באמצעות בוחנים מובנים או בוחנים מותאמים אישית שבחרת. כדי להתחיל עם Azure AI Evaluation SDK להערכת המערכת שלך, תוכל לעקוב אחר [מדריך ההתחלה המהירה](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). לאחר ביצוע ריצת הערכה, תוכל [להציג את התוצאות ב-Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## סימני מסחר

פרויקט זה עשוי לכלול סימני מסחר או לוגואים של פרויקטים, מוצרים או שירותים. שימוש מורשה בסימני המסחר או הלוגואים של מיקרוסופט כפוף וצריך לעמוד ב-[הנחיות סימני מסחר ומותג של מיקרוסופט](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
שימוש בסימני מסחר או לוגואים של מיקרוסופט בגרסאות שעברו שינוי של פרויקט זה אסור שיהיה מבלבל או ירמז על חסות מיקרוסופט. כל שימוש בסימני מסחר או לוגואים של צד שלישי כפוף למדיניות של אותו צד שלישי.

## לקבלת עזרה

אם נתקעת או יש לך שאלות בנוגע לבניית אפליקציות AI, הצטרף ל:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

אם יש לך משוב על מוצר או שגיאות בעת הבנייה, בקר ב:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עלולים להכיל טעויות או אי-דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור הסמכותי. למידע קריטי מומלץ להיעזר בתרגום מקצועי של אדם. איננו אחראים לכל אי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->