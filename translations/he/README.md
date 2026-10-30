# ספר הבישול של Phi: דוגמאות מעשיות עם מודלי Phi של מייקרוסופט

[![פתח והשתמש בדוגמאות ב-GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![פתח במכלי פיתוח](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![תורמים ב-GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![נושאים ב-GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![בקשות משיכה ב-GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs ברוכים הבאים](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![צופים ב-GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![סניפים ב-GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![כוכבים ב-GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![דיסקורד Microsoft Foundry](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi הם סדרת מודלי AI בקוד פתוח שפותחה על ידי מייקרוסופט.

Phi הוא כיום מודל שפה קטן הכי חזק ויעיל מבחינת עלות, עם מדדים מצוינים בריבוי שפות, היגיון, יצירת טקסט/שיחה, קידוד, תמונות, אודיו ותרחישים נוספים.

ניתן לפרוס את Phi בענן או במכשירי קצה, וקל לבנות יישומי AI יצירתיים עם כוח מחשוב מוגבל.

עקבו אחרי השלבים הללו כדי להתחיל להשתמש במשאבים אלו:
1. **פיצלו את המאגר**: לחצו על [![סניפים ב-GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **שכפלו את המאגר**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**הצטרפו לקהילת Microsoft AI בדיסקורד ופגשו מומחים ומפתחים**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/he/cover.eb18d1b9605d754b.webp)

### 🌐 תמיכה בריבוי שפות

#### נתמך דרך GitHub Action (אוטומטי ותמיד מעודכן)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[ערבית](../ar/README.md) | [בנגלית](../bn/README.md) | [בולגרית](../bg/README.md) | [בורמזית (מיאנמר)](../my/README.md) | [סינית (מפושטת)](../zh-CN/README.md) | [סינית (מסורתית, הונג קונג)](../zh-HK/README.md) | [סינית (מסורתית, מאקאו)](../zh-MO/README.md) | [סינית (מסורתית, טייוואן)](../zh-TW/README.md) | [קרואטית](../hr/README.md) | [צ'כית](../cs/README.md) | [דנית](../da/README.md) | [הולנדית](../nl/README.md) | [אסטונית](../et/README.md) | [פינית](../fi/README.md) | [צרפתית](../fr/README.md) | [גרמנית](../de/README.md) | [יוונית](../el/README.md) | [עברית](./README.md) | [הודית](../hi/README.md) | [הונגרית](../hu/README.md) | [אינדונזית](../id/README.md) | [איטלקית](../it/README.md) | [יפנית](../ja/README.md) | [קנדה](../kn/README.md) | [חמרית](../km/README.md) | [קוריאנית](../ko/README.md) | [ליטאית](../lt/README.md) | [מלאית](../ms/README.md) | [מאליאלאם](../ml/README.md) | [מניפורי (מיטאי מאייק)](../mni/README.md) | [מרטהית](../mr/README.md) | [נפאלית](../ne/README.md) | [פיג'ין ניגרי](../pcm/README.md) | [נורווגית](../no/README.md) | [פרסית (פארסי)](../fa/README.md) | [פולנית](../pl/README.md) | [פורטוגזית (ברזיל)](../pt-BR/README.md) | [פורטוגזית (פורטוגל)](../pt-PT/README.md) | [פונג'אבי (גורמוכי)](../pa/README.md) | [רומנית](../ro/README.md) | [רוסית](../ru/README.md) | [סרבית (קירילי)](../sr/README.md) | [סלובקית](../sk/README.md) | [סלובנית](../sl/README.md) | [ספרדית](../es/README.md) | [סוואהילי](../sw/README.md) | [שוודית](../sv/README.md) | [טגלוג (פיליפינית)](../tl/README.md) | [טמילית](../ta/README.md) | [טלוגו](../te/README.md) | [תאית](../th/README.md) | [טורקית](../tr/README.md) | [אוקראינית](../uk/README.md) | [אורדו](../ur/README.md) | [ווייטנאמית](../vi/README.md)

> **מעדיפים לשכפל מקומית?**
>
> מאגר זה כולל מעל 50 תרגומים לשפות שמגדילים משמעותית את גודל ההורדה. כדי לשכפל ללא תרגומים, השתמשו ב-checkout דליל:
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
> זה נותן לכם את כל מה שצריך כדי להשלים את הקורס עם הורדה הרבה יותר מהירה.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## תוכן העניינים

- מבוא
  - [ברוכים הבאים למשפחת Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [הגדרת הסביבה שלך](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [הבנת טכנולוגיות מרכזיות](./md/01.Introduction/01/01.Understandingtech.md)
  - [בטיחות AI עבור מודלי Phi](./md/01.Introduction/01/01.AISafety.md)
  - [תמיכה בחומרת Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [מודלי Phi וזמינותם בפלטפורמות שונות](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [שימוש ב-Guidance-ai ו-Phi](./md/01.Introduction/01/01.Guidance.md)
  - [מודלים ב-GitHub Marketplace](https://github.com/marketplace/models)
  - [קטלוג המודלים של Azure AI](https://ai.azure.com)

- הפעלת Phi בסביבות שונות
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [מודלים ב-GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [קטלוג מודלים Microsoft Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [ערכת כלים AI ב-VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- משפחת Phi בהפעלה
    - [הפעלת Phi ב-iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [הפעלת Phi באנדרואיד](./md/01.Introduction/03/Android_Inference.md)
    - [הפעלת Phi ב-Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [הפעלת Phi במחשב AI](./md/01.Introduction/03/AIPC_Inference.md)
    - [הפעלת Phi עם מסגרת Apple MLX](./md/01.Introduction/03/MLX_Inference.md)
    - [הפעלת Phi בשרת מקומי](./md/01.Introduction/03/Local_Server_Inference.md)
    - [הפעלת Phi בשרת מרוחק בעזרת AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [הפעלת Phi עם Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [הפעלת Phi--חזון במקומי](./md/01.Introduction/03/Vision_Inference.md)
    - [הפעלת Phi עם Kaito AKS, מכולות Azure (תמיכה רשמית)](./md/01.Introduction/03/Kaito_Inference.md)
-  [כימות משפחת Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [כימות Phi-3.5 / 4 באמצעות llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [כימות Phi-3.5 / 4 באמצעות הרחבות AI יצירתיות ל-onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [כימות Phi-3.5 / 4 באמצעות Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [כימות Phi-3.5 / 4 באמצעות מסגרת Apple MLX](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  הערכת Phi
    - [תגובה AI](./md/01.Introduction/05/ResponsibleAI.md)
    - [Microsoft Foundry להערכה](./md/01.Introduction/05/AIFoundry.md)
    - [שימוש ב-Promptflow להערכה](./md/01.Introduction/05/Promptflow.md)
 
- RAG עם Azure AI Search
    - [כיצד להשתמש ב-Phi-4-mini ו-Phi-4-multimodal(RAG) עם Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)
    - [RAG היברידי מקומי ללא ענן עם SQLite FTS5 ו-phi-4-mini](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-mini_Local_Hybrid_RAG_SQLite_FTS5.ipynb)

- דוגמאות לפיתוח יישומים עם Phi
  - יישומי טקסט ושיחה
    - דוגמאות Phi-4
      - [📓] [שוחח עם מודל Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [שוחח עם מודל ONNX מקומי Phi-4 ב-.NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [אפליקציית קונסול שיחה ב-.NET עם Phi-4 ONNX בשימוש Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - דוגמאות Phi-3 / 3.5
      - [בוט שיחה מקומי בדפדפן באמצעות Phi3, ONNX Runtime Web ו-WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [צ'אט OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [ריבוי מודלים - Phi-3-mini אינטראקטיבי ו-OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - בניית עטיפה ושימוש ב-Phi-3 עם MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [אופטימיזציית מודלים - כיצד לאופטם מודל Phi-3-mini עבור ONNX Runtime Web באמצעות Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [אפליקציית WinUI3 עם Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [דוגמא לאפליקציית WinUI3 Multi Model AI Powered Notes](https://github.com/microsoft/ai-powered-notes-winui3-sample)
      - [כיוונון עדין ואינטגרציה של מודלי Phi-3 מותאמים אישית עם Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
      - [כיוונון עדין ואינטגרציה של מודלי Phi-3 מותאמים אישית עם Prompt flow ב-Microsoft Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
      - [הערכת מודל Phi-3 / Phi-3.5 המחודד במרכז על עקרונות האחראיות של AI של מייקרוסופט](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
      - [📓] [דוגמת חיזוי שפה Phi-3.5-mini-instruct (סינית/אנגלית)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
      - [צ'אט בוט RAG Phi-3.5-Instruct WebGPU](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
      - [שימוש ב-GPU של Windows ליצירת פתרון Prompt flow עם Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
      - [שימוש ב-Microsoft Phi-3.5 tflite ליצירת אפליקציית אנדרואיד](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
      - [דוגמת שאלות ותשובות ב-.NET באמצעות מודל Phi-3 מקומי ONNX בשימוש Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
      - [אפליקציית שיחה בקונסול ב-.NET עם Semantic Kernel ו-Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

  - דוגמאות מבוססות קוד בערכת הפיתוח של Azure AI Inference SDK
    - דוגמאות Phi-4
      - [📓] [יצירת קוד פרויקט באמצעות Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)
    - דוגמאות Phi-3 / 3.5
      - [בנה את סוכן השיחה GitHub Copilot ב-Visual Studio Code עם משפחת Microsoft Phi-3](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)
      - [צרו סוכן שיחה ב-Visual Studio Code עם Phi-3.5 על ידי מודלי GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)

  - דוגמאות מתקדמות להסקת מסקנות
    - דגימות Phi-4
      - [📓] [דוגמאות ל-Phi-4-mini-reasoning או Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)
      - [📓] [כיוונון עדין ל-Phi-4-mini-reasoning עם Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [כיוונון עדין ל-Phi-4-mini-reasoning עם Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)
      - [📓] [Phi-4-mini-reasoning עם מודלים של GitHub](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)
      - [📓] [Phi-4-mini-reasoning עם מודלים של Microsoft Foundry](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)
  - הדגמות
      - [הדגמות של Phi-4-mini שהותקנו ב-Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)
      - [הדגמות של Phi-4-multimodal שהותקנו ב-Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)
  - דוגמאות לראות (Vision)
    - דוגמאות ל-Phi-4
      - [📓] [שימוש ב-Phi-4-multimodal לקריאת תמונות ויצירת קוד](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) 
    - דוגמאות ל-Phi-3 / 3.5
      -  [📓][Phi-3-vision-טקסט מתמונה לטקסט](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)
      - [📓][Phi-3-vision CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)
      - [DEMO: מיחזור עם Phi-3](https://github.com/jennifermarsman/PhiRecycling/)
      - [Phi-3-vision - עוזר שפת ראייה - עם Phi3-Vision ו-OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)
      - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)
      - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)
      - [📓][דוגמה מרובת מסגרות או מרובות תמונות ל-Phi-3.5 Vision](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)
      - [מודל ONNX מקומי ל-Phi-3 Vision המשתמש ב-Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)
      - [מודל ONNX מקומי מבוסס תפריט ל-Phi-3 Vision המשתמש ב-Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)

  - דוגמאות ל-Vision Reasoning
    - Phi-4-Reasoning-Vision-15B 
      - [📓] [שימוש ב-Phi-4-Reasoning-Vision-15B לזיהוי חציית כביש לא במעבר חציה](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb)
      - [📓] [שימוש ב-Phi-4-Reasoning-Vision-15B במתמטיקה](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb)
      - [📓] [שימוש ב-Phi-4-Reasoning-Vision-15B לזיהוי ממשק משתמש](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb)

  - דוגמאות למתמטיקה
    -  דוגמאות Phi-4-Mini-Flash-Reasoning-Instruct  [הדגמת מתמטיקה עם Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb)

  - דוגמאות קוליות
    - דוגמאות ל-Phi-4
      - [📓] [חילוץ תמלול אודיו באמצעות Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)
      - [📓] [דוגמת אודיו ל-Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)
      - [📓] [דוגמת תרגום דיבור ל-Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)
      - [יישום קונסול .NET המשתמש ב-Phi-4-multimodal Audio לניתוח קובץ אודיו ויצירת תמלול](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)

  - דוגמאות MOE
    - דוגמאות ל-Phi-3 / 3.5
      - [📓] [דוגמה של Phi-3.5 Mixture of Experts Models (MoEs) במדיה חברתית](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)
      - [📓] [בניית צנרת יצירה מוגברת בהבאת מידע (RAG) עם NVIDIA NIM Phi-3 MOE, Azure AI Search, ו-LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)
      - 
  - דוגמאות קריאת פונקציות
    - דוגמאות Phi-4 🆕
      -  [📓] [שימוש בקריאת פונקציות עם Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)
      -  [📓] [שימוש בקריאת פונקציות ליצירת סוכנים מרובים עם Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)
      -  [📓] [שימוש בקריאת פונקציות עם Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)
      -  [📓] [שימוש בקריאת פונקציות עם ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)
  - דוגמאות לערבוב מולטימודלי
    - דוגמאות Phi-4 🆕
      -  [📓] [שימוש ב-Phi-4-multimodal כעיתונאי טכנולוגיה](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)
      - [אפליקציית קונסולה .NET המשתמשת ב-Phi-4-multimodal לניתוח תמונות](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)

- דוגמאות לכיול עדין של Phi
  - [תרחישי כיוונון עדין](./md/03.FineTuning/FineTuning_Scenarios.md)
  - [כיוונון עדין לעומת RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)
  - [כיוונון עדין - להפוך את Phi-3 למומחה תעשייתי](./md/03.FineTuning/LetPhi3gotoIndustriy.md)
  - [כיוונון עדין של Phi-3 עם ערכת כלים ל-AI עבור VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)
  - [כיוונון עדין של Phi-3 עם שירות Azure Machine Learning](./md/03.FineTuning/Introduce_AzureML.md)
  - [כיוונון עדין של Phi-3 עם Lora](./md/03.FineTuning/FineTuning_Lora.md)
  - [כיוונון עדין של Phi-3 עם QLora](./md/03.FineTuning/FineTuning_Qlora.md)
  - [כיוונון עדין של Phi-3 עם Microsoft Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)
  - [כיוונון עדין של Phi-3 עם Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)
  - [כיוונון עדין עם Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)
  - [כיוונון עדין עם Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)
  - [כיוונון עדין של Phi-3-vision עם Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)
  - [כיוונון עדין של Phi-3 עם Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)
  - [כיוונון עדין של Phi-3-vision (תמיכה רשמית)](./md/03.FineTuning/FineTuning_Vision.md)
  - [כיוונון עדין של Phi-3 עם Kaito AKS, Azure Containers (תמיכה רשמית)](./md/03.FineTuning/FineTuning_Kaito.md)
  - [כיוונון עדין של Phi-3 ושל 3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)

- מעבדת עבודה מעשית
  - [חקירת מודלים מתקדמים: LLMs, SLMs, פיתוח מקומי ועוד](https://github.com/microsoft/aitour-exploring-cutting-edge-models)
  - [שחרור הפוטנציאל של NLP: כיוונון עדין עם Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)

- מאמרי מחקר אקדמיים ופרסומים
  - [Textbooks Are All You Need II: דוח טכני על phi-1.5](https://arxiv.org/abs/2309.05463)
  - [דוח טכני של Phi-3: מודל שפה רב עוצמה הפועל במכשירך המקומי](https://arxiv.org/abs/2404.14219)
  - [דוח טכני של Phi-4](https://arxiv.org/abs/2412.08905)
  - [דוח טכני של Phi-4-Mini: מודלים מולטימודליים קומפקטיים אך רבי עוצמה באמצעות תערובת LoRAs](https://arxiv.org/abs/2503.01743)
  - [אופטימיזציה של מודלים קטנים לשפה לקריאת פונקציות ברכב](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) כיוונון עדין של PHI-3 למענה על שאלות רב-ברירתיות: מתודולוגיה, תוצאות ואתגרים](https://arxiv.org/abs/2501.01588)
  - [דוח טכני של Phi-4 למסקנות](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [דוח טכני של Phi-4-mini למסקנות](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## שימוש במודלים Phi

### Phi ב-Microsoft Foundry

ניתן ללמוד כיצד להשתמש ב-Microsoft Phi וכיצד לבנות פתרונות E2E במכשירים השונים שלך. כדי להתנסות ב-Phi בעצמך, התחל לשחק עם המודלים ולהתאים את Phi לתרחישים שלך באמצעות [Microsoft Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) ניתן ללמוד עוד ב-התחלת העבודה עם [Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**מגרש משחקים**
לכל מודל יש מגרש משחקים ייעודי לבדיקת המודל [Azure AI Playground](https://aka.ms/try-phi3).

### Phi במודלים ב-GitHub

ניתן ללמוד כיצד להשתמש ב-Microsoft Phi וכיצד לבנות פתרונות E2E במכשירים השונים שלך. כדי להתנסות ב-Phi בעצמך, התחל לשחק עם המודל ולהתאים את Phi לתרחישים שלך באמצעות [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) ניתן ללמוד עוד ב-התחלת העבודה עם [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**מגרש משחקים**
לכל מודל יש [מגרש משחקים ייעודי לבדוק את המודל](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi ב-Hugging Face

ניתן גם למצוא את המודל ב-[Hugging Face](https://huggingface.co/microsoft)

**מגרש משחקים**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

 ## 🎒 קורסים נוספים

הצוות שלנו מייצר קורסים נוספים! בדקו:

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
 
### סדרת AI גנרטיבית
[![AI גנרטיבי למתחילים](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI גנרטיבי (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![AI גנרטיבי (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![AI גנרטיבי (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### למידה בסיסית
[![למידת מכונה למתחילים](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![מדעי הנתונים למתחילים](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI למתחילים](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![סייברסקיוריטי למתחילים](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![פיתוח ווב למתחילים](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT למתחילים](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![פיתוח XR למתחילים](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### סדרת Copilot
[![Copilot לתכנות משולב עם AI](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot ל-C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![הרפתקת Copilot](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## אינטיליגנציה מלאכותית אחראית 

מיקרוסופט מחויבת לסייע ללקוחותינו להשתמש במוצרי AI שלנו באחריות, לשתף את הלמידות שלנו ולבנות שותפויות מבוססות אמון באמצעות כלים כמו הערות שקיפות והערכת השפעות. משאבים רבים אלה נמצאים ב-[https://aka.ms/RAI](https://aka.ms/RAI).
הגישה של מיקרוסופט ל-AI אחראי מבוססת על עקרונות ה-AI שלנו של הגינות, אמינות ובטיחות, פרטיות ואבטחה, הכללה, שקיפות, ואחריות.

מודלים בקנה מידה גדול לשפה טבעית, תמונה ודיבור - כמו המשמש בדוגמה זו - יכולים להתנהג בדרכים שאינן הוגנות, לא אמינות או פוגעניות, ולגרום לנזקים. נא לעיין ב-[הערת השקיפות של שירות Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) כדי להיות מודעים לסיכונים ולהגבלות.

הגישה המומלצת להפחתת סיכונים אלה היא לכלול מערכת בטיחות בארכיטקטורה שלך היכולה לזהות ולמנוע התנהגות מזיקה. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) מספק שכבת הגנה עצמאית, המסוגלת לזהות תוכן שנוצר על ידי משתמשים ובינה מלאכותית ומזיק ביישומים ושירותים. Azure AI Content Safety כוללת API-ים לטקסט ולתמונה המאפשרים לך לזהות חומר מזיק. בתוך Microsoft Foundry, שירות Content Safety מאפשר לך לצפות, לחקור ולנסות קוד דוגמה לזיהוי תוכן מזיק במצבים שונים. התיעוד הבא של [התחלה מהירה](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) מדריך אותך בביצוע בקשות לשירות.

היבט נוסף שיש לקחת בחשבון הוא ביצועי היישום הכוללים. עם יישומים רב-מודליים ורב-מודאליים, אנו מתייחסים לביצועים כאל כך שהמערכת פועלת כפי שאתה והמשתמשים שלך מצפים, כולל לא יצירת פלטים מזיקים. חשוב להעריך את ביצועי היישום הכולל שלך באמצעות [מודדי ביצועים, איכות, סיכון ובטיחות](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). יש לך גם אפשרות ליצור ולהעריך עם [מודדי הערכה מותאמים אישית](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

באפשרותך להעריך את יישום ה-AI שלך בסביבת הפיתוח שלך באמצעות [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). בהתבסס על מערך נתונים לבחינה או על יעד, דורות ה-AI הגנרטיביים שלך נמדדים כמותית בעזרת מודדים מובנים או מודדים מותאמים אישית לפי בחירתך. כדי להתחיל עם azure ai evaluation sdk להערכת המערכת שלך, תוכל לעקוב אחר [מדריך התחלה מהירה](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). לאחר הפעלת הריצה של ההערכה, תוכל [לראות את התוצאות ב-Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## סימני מסחר

פרויקט זה עשוי להכיל סימני מסחר או לוגואים לפרויקטים, מוצרים או שירותים. שימוש מורשה בסימני מסחר או לוגואים של מיקרוסופט כפוף וצריך לעמוד ב-[הנחיות סימני המסחר והמותג של מיקרוסופט](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
שימוש בסימני מסחר או לוגואים של מיקרוסופט בגרסאות מותאמות של פרויקט זה אסור שיעלה לבלבול או יגרום לרושם של חסות מצד מיקרוסופט. כל שימוש בסימני מסחר או לוגואים של צד שלישי כפוף למדיניות של אותם צדדים שלישיים.

## קבלת עזרה

אם אתה נתקל בבעיה או יש לך שאלות לגבי בניית יישומי AI, הצטרף ל:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

אם יש לך משוב על מוצר או שגיאות בעת הפיתוח בקר באתר:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->