# ספר המתכונים של Phi: דוגמאות מעשיות עם דגמי Phi של מייקרוסופט

[![פתח והשתמש בדוגמאות ב-GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![פתח ב-Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![תורמים ב-GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![בעיות ב-GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![בקשות משיכה ב-GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![עוקבים ב-GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![מזלגות ב-GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![כוכבים ב-GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi היא סדרה של דגמי בינה מלאכותית בקוד פתוח שפותחו על ידי מייקרוסופט.

Phi היא כיום המודל הקטן ביותר בשפה (SLM) העוצמתי והיעיל ביותר מבחינת עלות, עם ביצועים גבוהים מאוד בשפות מרובות, בהיגיון, ביצירת טקסט/שיחה, תכנות, תמונות, אודיו ותרחישים נוספים.

ניתן לפרוס את Phi בענן או במכשירי קצה, ותוכלו לבנות בקלות יישומי בינה מלאכותית גנרטיבית עם כוח חישוב מוגבל.

עקבו אחר הצעדים הבאים כדי להתחיל להשתמש במשאבים אלה:
1. **העתק את המאגר**: לחץ על [![מזלגות ב-GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **שכפל את המאגר**: `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**הצטרף לקהילת ה-Discord של AI במייקרוסופט ופגוש מומחים ומפתחים נוספים**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/he/cover.eb18d1b9605d754b.webp)

### 🌐 תמיכה בשפות מרובות

#### נתמך באמצעות GitHub Action (אוטומטי ותמיד מעודכן)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[ערבית](../ar/README.md) | [בנגאלית](../bn/README.md) | [בולגרית](../bg/README.md) | [בורמזית (מיאנמר)](../my/README.md) | [סינית (מפושטת)](../zh-CN/README.md) | [סינית (מסורתית, הונג קונג)](../zh-HK/README.md) | [סינית (מסורתית, מקאו)](../zh-MO/README.md) | [סינית (מסורתית, טייוואן)](../zh-TW/README.md) | [קרואטית](../hr/README.md) | [צ'כית](../cs/README.md) | [דנית](../da/README.md) | [הולנדית](../nl/README.md) | [אסטונית](../et/README.md) | [פינית](../fi/README.md) | [צרפתית](../fr/README.md) | [גרמנית](../de/README.md) | [יוונית](../el/README.md) | [עברית](./README.md) | [הינדי](../hi/README.md) | [הונגרית](../hu/README.md) | [אינדונזית](../id/README.md) | [איטלקית](../it/README.md) | [יפנית](../ja/README.md) | [קנאדה](../kn/README.md) | [קמרית](../km/README.md) | [קוריאנית](../ko/README.md) | [ליטאית](../lt/README.md) | [מלאית](../ms/README.md) | [מלאיאלאם](../ml/README.md) | [מרטהית](../mr/README.md) | [נפאלית](../ne/README.md) | [פידג'ין ניגרי](../pcm/README.md) | [נורווגית](../no/README.md) | [פרסית (פארסית)](../fa/README.md) | [פולנית](../pl/README.md) | [פורטוגזית (ברזיל)](../pt-BR/README.md) | [פורטוגזית (פורטוגל)](../pt-PT/README.md) | [פונג'אבית (גורמוכי)](../pa/README.md) | [רומנית](../ro/README.md) | [רוסית](../ru/README.md) | [סרבית (קירילית)](../sr/README.md) | [סלובקית](../sk/README.md) | [סלובנית](../sl/README.md) | [ספרדית](../es/README.md) | [סוואהילי](../sw/README.md) | [שבדית](../sv/README.md) | [טאגאלוג (פיליפינית)](../tl/README.md) | [טמילית](../ta/README.md) | [טלוגו](../te/README.md) | [תאית](../th/README.md) | [טורקית](../tr/README.md) | [אוקראינית](../uk/README.md) | [אורדו](../ur/README.md) | [וייטנאמית](../vi/README.md)

> **מעדיפים לשכפל מקומית?**
>
> מאגר זה כולל מעל 50 תרגומים לשפות, מה שמגדיל משמעותית את גודל ההורדה. לשכפל ללא תרגומים, השתמשו ב-sparse checkout:
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
> זה נותן לכם את כל מה שצריך לסיים את הקורס עם הורדה מהירה יותר בהרבה.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## תוכן עניינים
- מבוא - [ברוכים הבאים למשפחת פי](./md/01.Introduction/01/01.PhiFamily.md) - [הכנת הסביבה שלך](./md/01.Introduction/01/01.EnvironmentSetup.md) - [הבנת טכנולוגיות מפתח](./md/01.Introduction/01/01.Understandingtech.md) - [בטיחות בינה מלאכותית למודלים של פי](./md/01.Introduction/01/01.AISafety.md) - [תמיכה בחומרה של פי](./md/01.Introduction/01/01.Hardwaresupport.md) - [מודלים של פי וזמינות בפלטפורמות שונות](./md/01.Introduction/01/01.Edgeandcloud.md) - [שימוש Guidance-ai ופִי](./md/01.Introduction/01/01.Guidance.md) - [מודלים של GitHub Marketplace](https://github.com/marketplace/models) - [קטלוג מודלים ב-Azure AI](https://ai.azure.com) - אינפרנציה של פי בסביבות שונות - [Hugging face](./md/01.Introduction/02/01.HF.md) - [מודלים ב-GitHub](./md/01.Introduction/02/02.GitHubModel.md) - [קטלוג מודלים Microsoft Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md) - [Ollama](./md/01.Introduction/02/04.Ollama.md) - [כלי AI ל-VSCode (AITK)](./md/01.Introduction/02/05.AITK.md) - [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md) - [Foundry מקומי](./md/01.Introduction/02/07.FoundryLocal.md) - אינפרנציה במשפחת פי - [אינפרנציה של פי ב-iOS](./md/01.Introduction/03/iOS_Inference.md) - [אינפרנציה של פי באנדרואיד](./md/01.Introduction/03/Android_Inference.md) - [אינפרנציה של פי ב-Jetson](./md/01.Introduction/03/Jetson_Inference.md) - [אינפרנציה של פי ב-AI PC](./md/01.Introduction/03/AIPC_Inference.md) - [אינפרנציה של פי עם מסגרת Apple MLX](./md/01.Introduction/03/MLX_Inference.md) - [אינפרנציה של פי בשרת מקומי](./md/01.Introduction/03/Local_Server_Inference.md) - [אינפרנציה של פי בשרת מרוחק באמצעות AI Toolkit](./md/01.Introduction/03/Remote_Interence.md) - [אינפרנציה של פי עם Rust](./md/01.Introduction/03/Rust_Inference.md) - [אינפרנציה של פי--חזון מקומי](./md/01.Introduction/03/Vision_Inference.md) - [אינפרנציה של פי עם Kaito AKS, Azure Containers (תמיכה רשמית)](./md/01.Introduction/03/Kaito_Inference.md) - [כימות משפחת פי](./md/01.Introduction/04/QuantifyingPhi.md) - [כימות פי-3.5 / 4 באמצעות llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md) - [כימות פי-3.5 / 4 באמצעות הרחבות AI גנרטיביות ל-onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md) - [כימות פי-3.5 / 4 באמצעות Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md) - [כימות פי-3.5 / 4 באמצעות מסגרת Apple MLX](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md) - הערכת פי - [אחריות AI](./md/01.Introduction/05/ResponsibleAI.md) - [Microsoft Foundry להערכה](./md/01.Introduction/05/AIFoundry.md) - [שימוש ב-Promptflow להערכה](./md/01.Introduction/05/Promptflow.md) - RAG עם Azure AI Search - [כיצד להשתמש ב-Phi-4-mini ו-Phi-4-multimodal (RAG) עם Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb) - דוגמאות לפיתוח אפליקציות לפי - אפליקציות טקסט וצ’אט - דוגמאות Phi-4 - [📓] [צ’אט עם מודל ONNX של Phi-4-mini](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md) - [צ’אט עם מודל ONNX מקומי של Phi-4 ב-.NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) - [אפליקציית קונסולה לצ’אט ב-.NET עם Phi-4 ONNX באמצעות Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) - דוגמאות Phi-3 / 3.5 - [בוט צ’אט מקומי בדפדפן המשתמש בפי-3, ONNX Runtime Web ו-WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat) - [צ’אט OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md) - [מודל מרובה - Phi-3-mini אינטראקטיבי ו-OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md) - [MLFlow - בניית עטיפה ושימוש בפי-3 עם MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md) - [אופטימיזציית מודלים - כיצד לאופטימיזציה של מודל Phi-3-min עבור ONNX Runtime Web עם Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3) - [אפליקציית WinUI3 עם Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/) - [דוגמה לאפליקציית WinUI3 עם מודלי AI מרובים](https://github.com/microsoft/ai-powered-notes-winui3-sample) - [כיוונון עדין ואינטגרציה של מודלים מותאמים אישית של Phi-3 עם Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md) - [כיוונון עדין ואינטגרציה של מודלים מותאמים אישית של Phi-3 עם Prompt flow ב-Microsoft Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md) - [הערכת המודל מכוונן העדין של Phi-3 / Phi-3.5 ב-Microsoft Foundry עם דגש על עקרונות אחריות AI של מיקרוסופט](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md) - [📓] [דוגמת ניבוי שפה Phi-3.5-mini-instruct (סינית/אנגלית)](./md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb) - [Phi-3.5-Instruct WebGPU רגל צ’אטבוט](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md) - [שימוש ב-GPU של Windows ליצירת פתרון Prompt flow עם Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md) - [שימוש ב-Microsoft Phi-3.5 tflite ליצירת אפליקציית Android](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md) - [דוגמת שאלות ותשובות .NET עם מודל ONNX מקומי של Phi-3 באמצעות Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301) - [אפליקציית קונסול לצ’אט ב-.NET עם Semantic Kernel ופִי-3](../../md/04.HOL/dotnet/src/LabsPhi302) - דוגמאות קוד מבוסס סנסור Azure AI Inference SDK - דוגמאות Phi-4 - [📓] [יצירת קוד פרויקט באמצעות Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md) - דוגמאות Phi-3 / 3.5 - [בניית סוכן צ’אט GitHub Copilot עבור Visual Studio Code עם משפחת Phi-3 של Microsoft](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md) - [יצירת סוכן צ’אט GitHub עבור Visual Studio Code עם Phi-3.5 בעזרת מודלים ב-GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md) - דוגמאות להסקת מסקנות מתקדמות - דוגמאות Phi-4 - [📓] [דוגמאות להשכלת Phi-4-mini או Phi-4 להסקה](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md) - [📓] [כיוונון עדין של Phi-4-mini להסקה עם Microsoft Olive](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [כיוונון עדין של Phi-4-mini להסקה עם Apple MLX](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb) - [📓] [Phi-4-mini להסקה עם מודלים של GitHub](./md/02.Application/02.Code/Phi4r/github_models_inference.ipynb) - [📓] [Phi-4-mini להסקה עם מודלים של Microsoft Foundry](./md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb) -
דמויות - [דמויות Phi-4-mini המתארחות ב-Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo) - [דמויות Phi-4-multimodal המתארחות ב-Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo) - דוגמאות ראייה - דוגמאות Phi-4 - [📓] [שימוש ב-Phi-4-multimodal לקריאת תמונות וליצירת קוד](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md) - דוגמאות Phi-3 / 3.5 - [📓][Phi-3-vision טקסט לתמונה לטקסט](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html) - [📓][Phi-3-vision CLIP Embedding](./md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb) - [DEMO: מחזור Phi-3](https://github.com/jennifermarsman/PhiRecycling/) - [Phi-3-vision - עוזר שפה חזותית - עם Phi3-Vision ו-OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html) - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md) - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md) - [📓][דוגמה מרובת מסגרות או תמונות מרובות ב-Phi-3.5 Vision](./md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb) - [מודל מקומי של Phi-3 Vision ONNX באמצעות Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303) - [מודל מקומי מבוסס תפריט של Phi-3 Vision ONNX באמצעות Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304) - דוגמאות ההיגיון-ראייה - Phi-4-Reasoning-Vision-15B - [📓] [שימוש ב-Phi-4-Reasoning-Vision-15B לזיהוי חציית כביש לא חוקית](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Jaywalking.ipynb) - [📓] [שימוש ב-Phi-4-Reasoning-Vision-15B במתמטיקה](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_Math.ipynb) - [📓] [שימוש ב-Phi-4-Reasoning-Vision-15B לזיהוי ממשק משתמש](./md/02.Application/10.ReasoningVision/Phi_4_reasoning_vision_15b_ui.ipynb) - דוגמאות מתמטיקה - דוגמאות Phi-4-Mini-Flash-Reasoning-Instruct [דמו מתמטיקה עם Phi-4-Mini-Flash-Reasoning-Instruct](./md/02.Application/09.Math/MathDemo.ipynb) - דוגמאות שמע - דוגמאות Phi-4 - [📓] [הפקת תמלולים משמע באמצעות Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md) - [📓] [דוגמת שמע Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Siri/demo.ipynb) - [📓] [דוגמת תרגום דיבור Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Translate/demo.ipynb) - [יישום קונסולה ב-.NET המשתמש ב-Phi-4-multimodal שמע לניתוח קובץ שמע ויצירת תמלול](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) - דוגמאות MOE - דוגמאות Phi-3 / 3.5 - [📓] [דוגמת מודלים רב-מומחים (MoEs) של Phi-3.5 ברשתות חברתיות](./md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb) - [📓] [בניית מסלול ייצור מבוסס שליפה (RAG) עם NVIDIA NIM Phi-3 MOE, חיפוש Azure AI, ו-LlamaIndex](./md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb) - - דוגמאות הקריאת פונקציות - דוגמאות Phi-4 🆕 - [📓] [שימוש בקריאת פונקציות עם Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md) - [📓] [שימוש בקריאת פונקציות ליצירת סוכנים מרובים עם Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb) - [📓] [שימוש בקריאת פונקציות עם Ollama](./md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb) - [📓] [שימוש בקריאת פונקציות עם ONNX](./md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb) - דוגמאות מיקס מולטימודלי - דוגמאות Phi-4 🆕 - [📓] [שימוש ב-Phi-4-multimodal כעיתונאי טכנולוגי](./md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb) - [יישום קונסולה ב-.NET המשתמש ב-Phi-4-multimodal לניתוח תמונות](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) - דוגמאות כוונון מדויק ל-Phi - [תרחישי כוונון מדויק](./md/03.FineTuning/FineTuning_Scenarios.md) - [כוונון מדויק לעומת RAG](./md/03.FineTuning/FineTuning_vs_RAG.md) - [כוונון מדויק: להפוך את Phi-3 למומחה תעשייתי](./md/03.FineTuning/LetPhi3gotoIndustriy.md) - [כוונון מדויק ל-Phi-3 עם AI Toolkit עבור VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md) - [כוונון מדויק ל-Phi-3 עם שירות Azure Machine Learning](./md/03.FineTuning/Introduce_AzureML.md) - [כוונון מדויק ל-Phi-3 עם Lora](./md/03.FineTuning/FineTuning_Lora.md) - [כוונון מדויק ל-Phi-3 עם QLora](./md/03.FineTuning/FineTuning_Qlora.md) - [כוונון מדויק ל-Phi-3 עם Microsoft Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md) - [כוונון מדויק ל-Phi-3 עם Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md) - [כוונון עם Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md) - [כוונון עם מעבדת Microsoft Olive Hands-On](./md/03.FineTuning/olive-lab/readme.md) - [כוונון ל-Phi-3-vision עם Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md) - [כוונון ל-Phi-3 עם Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md) - [כוונון ל-Phi-3-vision (תמיכה רשמית)](./md/03.FineTuning/FineTuning_Vision.md) - [כוונון מדויק ל-Phi-3 עם Kaito AKS, Azure Containers (תמיכה רשמית)](./md/03.FineTuning/FineTuning_Kaito.md) - [כוונון מדויק ל-Phi-3 ול-Phi-3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune) - מעבדת עבודה - [חקירת מודלים מתקדמים: LLMs, SLMs, פיתוח מקומי ועוד](https://github.com/microsoft/aitour-exploring-cutting-edge-models) - [שחרור פוטנציאל NLP: כוונון מדויק עם Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop) - מאמרים אקדמיים ופרסומים - [Textbooks Are All You Need II: דוח טכני ל-phi-1.5](https://arxiv.org/abs/2309.05463) - [דוח טכני ל-Phi-3: מודל שפה מתקדם במכשירך המקומי](https://arxiv.org/abs/2404.14219) - [דוח טכני ל-Phi-4](https://arxiv.org/abs/2412.08905) - [דוח טכני ל-Phi-4-Mini: מודלי שפה מרובי מצבים קומפקטיים ועוצמתיים באמצעות תערובת LoRA](https://arxiv.org/abs/2503.01743) - [אופטימיזציה למודלי שפה קטנים לקריאה לפונקציה ברכב](https://arxiv.org/abs/2501.02342) - [(WhyPHI) כוונון מדויק של PHI-3 לשאלות רב-ברירתיות: מתודולוגיה, תוצאות ואתגרים](https://arxiv.org/abs/2501.01588) - [דוח טכני ל-Phi-4-Reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
- [דו"ח טכני Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)
# ספר הבישול של Phi: דוגמאות מעשיות עם דגמי Phi של מייקרוסופט

[![פתחו והשתמשו בדוגמאות ב-GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)  
[![פתחו ב-Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![תורמים ל-GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)  
[![בעיות ב-GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)  
[![בקשות משיכה ב-GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)  
[![ברוכים הבאים לבקשות משיכה](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![צופים ב-GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)  
[![מקלות ב-GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
[![כוכבים ב-GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Discord של Microsoft Foundry](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi היא סדרה של דגמי בינה מלאכותית בקוד פתוח שפותחה על ידי מייקרוסופט.

כרגע Phi הוא הדגם הקטן (SLM) העוצמתי והמשתלם ביותר מבחינת עלות, עם ביצועים טובים במיוחד בריבוי שפות, חשיבה, יצירת טקסט/שיחה, קידוד, תמונות, שמע ותסריטים נוספים.

ניתן לפרוס את Phi בענן או במכשירי קצה, וניתן לבנות בקלות אפליקציות בינה מלאכותית יצירתית עם כוח מחשוב מוגבל.

עקבו אחר הצעדים הבאים כדי להתחיל להשתמש במשאבים אלו:  
1. **צור Fork למאגר**: לחץ [![מקלות ב-GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)  
2. **שכפל את המאגר**: `git clone https://github.com/microsoft/PhiCookBook.git`  
3. [**הצטרף לקהילת ה-Discord של מייקרוסופט AI ומפגש עם מומחים ומפתחים**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../translated_images/he/cover.eb18d1b9605d754b.webp)

### 🌐 תמיכה בריבוי שפות

#### נתמך דרך GitHub Action (אוטומטי ותמיד מעודכן)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[ערבית](../ar/README.md) | [בנגלית](../bn/README.md) | [בולגרית](../bg/README.md) | [בורמזית (מיאנמר)](../my/README.md) | [סינית (מפושטת)](../zh-CN/README.md) | [סינית (מסורתית, הונג קונג)](../zh-HK/README.md) | [סינית (מסורתית, מקאו)](../zh-MO/README.md) | [סינית (מסורתית, טייוואן)](../zh-TW/README.md) | [קרואטית](../hr/README.md) | [צ'כית](../cs/README.md) | [דנית](../da/README.md) | [הולנדית](../nl/README.md) | [אסטונית](../et/README.md) | [פינית](../fi/README.md) | [צרפתית](../fr/README.md) | [גרמנית](../de/README.md) | [יוונית](../el/README.md) | [עברית](./README.md) | [הינדי](../hi/README.md) | [הונגרית](../hu/README.md) | [אינדונזית](../id/README.md) | [איטלקית](../it/README.md) | [יפנית](../ja/README.md) | [קנדה](../kn/README.md) | [חמרית](../km/README.md) | [קוריאנית](../ko/README.md) | [ליטאית](../lt/README.md) | [מלאית](../ms/README.md) | [מלאלאית](../ml/README.md) | [מרטהית](../mr/README.md) | [נפאלית](../ne/README.md) | [פידג'ין ניגרי](../pcm/README.md) | [נורבגית](../no/README.md) | [פרסית (פרסית)](../fa/README.md) | [פולנית](../pl/README.md) | [פורטוגזית (ברזיל)](../pt-BR/README.md) | [פורטוגזית (פורטוגל)](../pt-PT/README.md) | [פונג'אבית (גורמוכי)](../pa/README.md) | [רומנית](../ro/README.md) | [רוסית](../ru/README.md) | [סרבית (קירילי)](../sr/README.md) | [סלובקית](../sk/README.md) | [סלובנית](../sl/README.md) | [ספרדית](../es/README.md) | [סווהילית](../sw/README.md) | [שוודית](../sv/README.md) | [טגלוג (פיליפינית)](../tl/README.md) | [טמילית](../ta/README.md) | [טלוגו](../te/README.md) | [תאית](../th/README.md) | [טורקית](../tr/README.md) | [אוקראינית](../uk/README.md) | [אורדו](../ur/README.md) | [וייטנאמית](../vi/README.md)

> **מעדיפים לשכפל מקומי?**  
>  
> מאגר זה כולל יותר מ-50 תרגומים בשפות שונות, מה שמגדיל משמעותית את גודל ההורדה. לשכפול ללא תרגומים, השתמשו ב-sparse checkout:  
>  
> **באש / macOS / לינוקס:**  
> > ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>  
> **CMD (ווינדוס):**  
> > ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/PhiCookBook.git
> cd PhiCookBook
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>  
> זה נותן לכם הכל שצריך כדי להשלים את הקורס במהירות הורדה גבוהה יותר.  
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## תוכן העניינים

## שימוש בדגמי Phi

### Phi ב-Microsoft Foundry

אתם יכולים ללמוד איך להשתמש ב-Microsoft Phi ואיך לבנות פתרונות מקצה לקצה במכשירי החומרה השונים שלכם. כדי לחוות את Phi בעצמכם, התחילו לשחק עם הדגמים ולהתאים אישית את Phi לתרחישים שלכם באמצעות [קטלוג דגמי הבינה המלאכותית של Microsoft Foundry Azure](https://aka.ms/phi3-azure-ai). תוכלו ללמוד עוד ב-התוודעות ל-[Microsoft Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md)

**חצר משחקים**  
לכל דגם יש חצר משחקים ייעודית לבדיקה [Azure AI Playground](https://aka.ms/try-phi3).

### Phi בדגמי GitHub

אתם יכולים ללמוד איך להשתמש ב-Microsoft Phi ואיך לבנות פתרונות מקצה לקצה במכשירי החומרה השונים שלכם. כדי לחוות את Phi בעצמכם, התחילו לשחק עם הדגם ולהתאים אישית את Phi לתרחישים שלכם באמצעות [קטלוג דגמי GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). תוכלו ללמוד עוד ב-התוודעות ל-[קטלוג דגמי GitHub](/md/02.QuickStart/GitHubModel_QuickStart.md)

**חצר משחקים**  
לכל דגם יש [חצר משחקים ייעודית לבדיקה](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi ב-Hugging Face

אתם יכולים גם למצוא את הדגם ב-[Hugging Face](https://huggingface.co/microsoft)

**חצר משחקים**  
[חצר המשחקים של Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

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

### סדרת בינה מלאכותית יצירתית  
[![בינה מלאכותית יצירתית למתחילים](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![בינה מלאכותית יצירתית (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  

[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Core Learning
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Series
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## AI אחראי

מיקרוסופט מחויבת לסייע ללקוחותינו להשתמש במוצרי ה-AI שלנו באחריות, לשתף את התובנות שלנו ולבנות שותפויות מבוססות אמון באמצעות כלים כמו הערות שקיפות והערכות השפעה. ניתן למצוא משאבים רבים אלה ב-[https://aka.ms/RAI](https://aka.ms/RAI).
הגישה של מיקרוסופט ל-AI אחראי מבוססת על עקרונות ה-AI שלנו הכוללים הוגנות, אמינות ובטיחות, פרטיות ואבטחה, הכללה, שקיפות ואחריות.

מודלים נרחבים של שפה טבעית, תמונות ודיבור - כמו אלו המשמשים בדוגמה זו - עשויים להתנהג באופן לא הוגן, לא אמין או פוגע, ובכך לגרום לנזקים. נא לעיין ב-[הערת השקיפות של שירות Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) כדי להתעדכן בסיכונים ובמגבלות.

הגישה המומלצת להפחתת סיכונים אלה היא לכלול מערכת בטיחות בארכיטקטורה שלך שיכולה לזהות ולמנוע התנהגויות מזיקות. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) מספק שכבת הגנה עצמאית, המסוגלת לזהות תוכן מזיק שנוצר על ידי משתמשים ו-AI ביישומים ובשירותים. שירות Content Safety של Azure AI כולל APIs לטקסט ותמונות המאפשרים לזהות חומר מזיק. בתוך Microsoft Foundry, שירות Content Safety מאפשר לך לצפות, לחקור ולנסות קוד לדוגמה לזיהוי תוכן מזיק במודלטיויות שונות. התיעוד הבא של [התחלה מהירה](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) מנחה אותך כיצד לבצע בקשות לשירות.

היבט נוסף שיש לקחת בחשבון הוא ביצועי היישום הכוללים. עם יישומים מרובי מודלים ומודלטיויות, אנו מחשיבים ביצועים כהתנהגות המערכת כמצופה על ידך ועל ידי המשתמשים, כולל אי יצירת פלט מזיק. חשוב להעריך את ביצועי היישום הכולל באמצעות [כלי הערכה של ביצועים, איכות וסיכונים ובטיחות](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). כמו כן, יש לך יכולת ליצור ולהעריך באמצעות [כלי הערכה מותאמים אישית](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

ניתן להעריך את יישום ה-AI שלך בסביבת הפיתוח באמצעות [ערכת הפיתוח Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). בהינתן קובץ נתונים לבדיקה או יעד, תוצרי ה- generative AI שלך נבחנים כמותית עם כלים מובנים או מותאמים אישית לפי בחירתך. כדי להתחיל עם Azure AI Evaluation SDK להערכת המערכת, ניתן לעקוב אחר [מדריך התחלה מהירה](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). לאחר הפעלת ריצת הערכה, ניתן [להציג את התוצאות ב- Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## סמליים מסחריים

פרויקט זה עשוי לכלול סמלילים או סמלילים של פרויקטים, מוצרים או שירותים. שימוש מורשה בסמלי המסחר או לוגואים של מיקרוסופט כפוף וצריך להיות בהתאם ל-[הנחיות הסימנים המסחריים והממותגים של מיקרוסופט](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
שימוש בסמלי המסחר של מיקרוסופט או לוגואים בגרסאות מותאמות של פרויקט זה אינו צריך לגרום לבלבול או להראות תמיכה מצד מיקרוסופט. כל שימוש בסמלים או לוגואים של צדדים שלישיים כפוף למדיניות של אותם צדדים.

## קבלת עזרה

אם תיתקל בבעיה או יהיו לך שאלות לגבי בניית יישומי AI, הצטרף ל:

[![Microsoft Foundry Discord](https://img.shields.io/badge/Discord-Microsoft_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

אם יש לך משוב על המוצר או שגיאות בבנייה, בקר:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתירגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. למידע קריטי מומלץ תרגום מקצועי על ידי אדם. אנו לא אחראים לכל אי-הבנה או פרשנות שגויה שנובעת משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->