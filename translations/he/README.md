<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a73c59eecd7ad4ec494fd4333a29e208",
  "translation_date": "2025-10-11T11:08:56+00:00",
  "source_file": "README.md",
  "language_code": "he"
}
-->
# ספר מתכונים של Phi: דוגמאות מעשיות עם מודלים של Phi מבית Microsoft

[![פתח והשתמש בדוגמאות ב-GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phicookbook)
[![פתח ב-Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phicookbook)

[![תורמים ב-GitHub](https://img.shields.io/github/contributors/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![בעיות ב-GitHub](https://img.shields.io/github/issues/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![בקשות משיכה ב-GitHub](https://img.shields.io/github/issues-pr/microsoft/phicookbook.svg)](https://GitHub.com/microsoft/phicookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![ברוכים הבאים לבקשות משיכה](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![עוקבים ב-GitHub](https://img.shields.io/github/watchers/microsoft/phicookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phicookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![מזלגות ב-GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![כוכבים ב-GitHub](https://img.shields.io/github/stars/microsoft/phicookbook?style=social&label=Star)](https://GitHub.com/microsoft/phicookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Phi הוא סדרת מודלים AI בקוד פתוח שפותחה על ידי Microsoft.

Phi הוא כיום מודל שפה קטן (SLM) עוצמתי וחסכוני במיוחד, עם ביצועים מצוינים במבחנים רב-לשוניים, הסקת מסקנות, יצירת טקסט/צ'אט, קידוד, תמונות, אודיו ותסריטים נוספים.

ניתן לפרוס את Phi לענן או למכשירי קצה, ולבנות בקלות יישומי AI גנרטיביים עם כוח מחשוב מוגבל.

עקבו אחר השלבים הבאים כדי להתחיל להשתמש במשאבים אלו:
1. **צרו מזלג למאגר**: לחצו [![מזלגות ב-GitHub](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **שכפלו את המאגר**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**הצטרפו לקהילת Microsoft AI Discord ופגשו מומחים ומפתחים נוספים**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![תמונה ראשית](../../imgs/cover.png)

### 🌐 תמיכה רב-לשונית

#### נתמך באמצעות GitHub Action (אוטומטי ותמיד מעודכן)

<!-- טבלת שפות מתורגמות CO-OP TRANSLATOR LANGUAGES TABLE START -->
[ערבית](../ar/README.md) | [בנגלית](../bn/README.md) | [בולגרית](../bg/README.md) | [בורמזית (מיאנמר)](../my/README.md) | [סינית (פשוטה)](../zh/README.md) | [סינית (מסורתית, הונג קונג)](../hk/README.md) | [סינית (מסורתית, מקאו)](../mo/README.md) | [סינית (מסורתית, טייוואן)](../tw/README.md) | [קרואטית](../hr/README.md) | [צ'כית](../cs/README.md) | [דנית](../da/README.md) | [הולנדית](../nl/README.md) | [אסטונית](../et/README.md) | [פינית](../fi/README.md) | [צרפתית](../fr/README.md) | [גרמנית](../de/README.md) | [יוונית](../el/README.md) | [עברית](./README.md) | [הינדית](../hi/README.md) | [הונגרית](../hu/README.md) | [אינדונזית](../id/README.md) | [איטלקית](../it/README.md) | [יפנית](../ja/README.md) | [קוריאנית](../ko/README.md) | [ליטאית](../lt/README.md) | [מלאית](../ms/README.md) | [מרטהי](../mr/README.md) | [נפאלית](../ne/README.md) | [נורווגית](../no/README.md) | [פרסית (פארסי)](../fa/README.md) | [פולנית](../pl/README.md) | [פורטוגזית (ברזיל)](../br/README.md) | [פורטוגזית (פורטוגל)](../pt/README.md) | [פונג'בית (גורמוקי)](../pa/README.md) | [רומנית](../ro/README.md) | [רוסית](../ru/README.md) | [סרבית (קירילית)](../sr/README.md) | [סלובקית](../sk/README.md) | [סלובנית](../sl/README.md) | [ספרדית](../es/README.md) | [סוואהילית](../sw/README.md) | [שוודית](../sv/README.md) | [טאגאלוג (פיליפינית)](../tl/README.md) | [טמילית](../ta/README.md) | [תאית](../th/README.md) | [טורקית](../tr/README.md) | [אוקראינית](../uk/README.md) | [אורדו](../ur/README.md) | [וייטנאמית](../vi/README.md)
<!-- טבלת שפות מתורגמות CO-OP TRANSLATOR LANGUAGES TABLE END -->

## תוכן העניינים

- מבוא
  - [ברוכים הבאים למשפחת Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [הגדרת הסביבה שלכם](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [הבנת טכנולוגיות מפתח](./md/01.Introduction/01/01.Understandingtech.md)
  - [בטיחות AI עבור מודלים של Phi](./md/01.Introduction/01/01.AISafety.md)
  - [תמיכה בחומרה עבור Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [מודלים של Phi וזמינותם בפלטפורמות שונות](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [שימוש ב-Guidance-ai וב-Phi](./md/01.Introduction/01/01.Guidance.md)
  - [מודלים ב-GitHub Marketplace](https://github.com/marketplace/models)
  - [קטלוג מודלים של Azure AI](https://ai.azure.com)

- הסקת מסקנות עם Phi בסביבות שונות
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [מודלים ב-GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [קטלוג מודלים של Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- הסקת מסקנות עם משפחת Phi
    - [הסקת מסקנות עם Phi ב-iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [הסקת מסקנות עם Phi באנדרואיד](./md/01.Introduction/03/Android_Inference.md)
    - [הסקת מסקנות עם Phi ב-Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [הסקת מסקנות עם Phi במחשב AI](./md/01.Introduction/03/AIPC_Inference.md)
    - [הסקת מסקנות עם Phi באמצעות Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [הסקת מסקנות עם Phi בשרת מקומי](./md/01.Introduction/03/Local_Server_Inference.md)
    - [הסקת מסקנות עם Phi בשרת מרוחק באמצעות AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [הסקת מסקנות עם Phi באמצעות Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [הסקת מסקנות עם Phi--Vision באופן מקומי](./md/01.Introduction/03/Vision_Inference.md)
    - [הסקת מסקנות עם Phi באמצעות Kaito AKS, Azure Containers (תמיכה רשמית)](./md/01.Introduction/03/Kaito_Inference.md)
-  [כימות משפחת Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [כימות Phi-3.5 / 4 באמצעות llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [כימות Phi-3.5 / 4 באמצעות הרחבות AI גנרטיביות ל-onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [כימות Phi-3.5 / 4 באמצעות Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [כימות Phi-3.5 / 4 באמצעות Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

-  הערכת Phi
    - [AI אחראי](./md/01.Introduction/05/ResponsibleAI.md)
    - [Azure AI Foundry להערכה](./md/01.Introduction/05/AIFoundry.md)
    - [שימוש ב-Promptflow להערכה](./md/01.Introduction/05/Promptflow.md)
 
- RAG עם Azure AI Search
    - [כיצד להשתמש ב-Phi-4-mini וב-Phi-4-multimodal (RAG) עם Azure AI Search](https://github.com/microsoft/PhiCookBook/blob/main/code/06.E2E/E2E_Phi-4-RAG-Azure-AI-Search.ipynb)

- דוגמאות לפיתוח יישומים עם Phi
  - יישומי טקסט וצ'אט
    - דוגמאות Phi-4 🆕
      - [📓] [צ'אט עם מודל Phi-4-mini ONNX](./md/02.Application/01.TextAndChat/Phi4/ChatWithPhi4ONNX/README.md)
      - [צ'אט עם מודל Phi-4 מקומי ONNX ב-.NET](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime)
      - [צ'אט אפליקציית קונסול ב-.NET עם Phi-4 ONNX באמצעות Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - דוגמאות Phi-3 / 3.5
      - [צ'אט מקומי בדפדפן באמצעות Phi3, ONNX Runtime Web ו-WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [צ'אט OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [מודל רב-תפקודי - אינטראקטיבי Phi-3-mini ו-OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - בניית מעטפת ושימוש ב-Phi-3 עם MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [אופטימיזציית מודל - כיצד לאופטם את מודל Phi-3-min עבור ONNX Runtime Web עם Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
- [אפליקציית WinUI3 עם Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
- [דוגמה לאפליקציית הערות מבוססת AI עם מודלים מרובים ב-WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [כיוונון והתאמה של מודלים מותאמים אישית של Phi-3 עם Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)
- [כיוונון והתאמה של מודלים מותאמים אישית של Phi-3 עם Prompt flow ב-Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)
- [הערכת מודל Phi-3 / Phi-3.5 מכוונן ב-Azure AI Foundry תוך התמקדות בעקרונות AI אחראי של Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)
- [📓] [דוגמה לחיזוי שפה עם Phi-3.5-mini-instruct (סינית/אנגלית)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)
- [צ'אטבוט RAG מבוסס WebGPU עם Phi-3.5-Instruct](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)
- [שימוש ב-GPU של Windows ליצירת פתרון Prompt flow עם Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)
- [שימוש ב-Microsoft Phi-3.5 tflite ליצירת אפליקציית אנדרואיד](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)
- [דוגמת Q&A ב-.NET עם מודל Phi-3 מקומי באמצעות Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)
- [אפליקציית צ'אט קונסול ב-.NET עם Semantic Kernel ו-Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)

- דוגמאות קוד מבוססות SDK של Azure AI Inference  
  - דוגמאות Phi-4 🆕  
    - [📓] [יצירת קוד פרויקט באמצעות Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - דוגמאות Phi-3 / 3.5  
    - [בניית צ'אט GitHub Copilot משלך ב-Visual Studio Code עם משפחת Phi-3 של Microsoft](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [יצירת סוכן צ'אט Copilot משלך ב-Visual Studio Code עם Phi-3.5 באמצעות מודלים של GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- דוגמאות הסקה מתקדמות  
  - דוגמאות Phi-4 🆕  
    - [📓] [דוגמאות Phi-4-mini-reasoning או Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [כיוונון Phi-4-mini-reasoning עם Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [כיוונון Phi-4-mini-reasoning עם Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [Phi-4-mini-reasoning עם מודלים של GitHub](../../md/02.Application/02.Code/Phi4r/github_models_inference.ipynb)  
    - [📓] [Phi-4-mini-reasoning עם מודלים של Azure AI Foundry](../../md/02.Application/02.Code/Phi4r/azure_models_inference.ipynb)  
- הדגמות  
    - [הדגמות Phi-4-mini המתארחות ב-Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-mini?WT.mc_id=aiml-137032-kinfeylo)  
    - [הדגמות Phi-4-multimodal המתארחות ב-Hugging Face Spaces](https://huggingface.co/spaces/microsoft/phi-4-multimodal?WT.mc_id=aiml-137032-kinfeylo)  
- דוגמאות חזותיות  
  - דוגמאות Phi-4 🆕  
    - [📓] [שימוש ב-Phi-4-multimodal לקריאת תמונות ויצירת קוד](./md/02.Application/04.Vision/Phi4/CreateFrontend/README.md)  
  - דוגמאות Phi-3 / 3.5  
    - [📓][Phi-3-vision-Image text to text](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)  
    - [📓][Phi-3-vision CLIP Embedding](../../md/02.Application/04.Vision/Phi3/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)  
    - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)  
    - [Phi-3-vision - עוזר שפה חזותי - עם Phi3-Vision ו-OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)  
    - [Phi-3 Vision Nvidia NIM](./md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md)  
    - [Phi-3 Vision OpenVino](./md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md)  
    - [📓][Phi-3.5 Vision דוגמה רב-פריימית או רב-תמונתית](../../md/02.Application/04.Vision/Phi3/phi3-vision-demo.ipynb)  
    - [Phi-3 Vision מודל ONNX מקומי באמצעות Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [מודל ONNX מקומי מבוסס תפריט עם Phi-3 Vision באמצעות Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- דוגמאות מתמטיות  
  - דוגמאות Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [דוגמת מתמטיקה עם Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)  

- דוגמאות שמע  
  - דוגמאות Phi-4 🆕  
    - [📓] [חילוץ תמלולי שמע באמצעות Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [דוגמת שמע Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [דוגמת תרגום דיבור Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [אפליקציית קונסול .NET המשתמשת ב-Phi-4-multimodal לניתוח קובץ שמע ויצירת תמלול](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- דוגמאות MoE  
  - דוגמאות Phi-3 / 3.5  
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) דוגמת מדיה חברתית](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [בניית צינור RAG עם NVIDIA NIM Phi-3 MOE, Azure AI Search, ו-LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- דוגמאות קריאת פונקציות  
  - דוגמאות Phi-4 🆕  
    - [📓] [שימוש בקריאת פונקציות עם Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [שימוש בקריאת פונקציות ליצירת סוכנים מרובים עם Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [שימוש בקריאת פונקציות עם Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [שימוש בקריאת פונקציות עם ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- דוגמאות ערבוב מולטימודלי  
  - דוגמאות Phi-4 🆕  
    - [📓] [שימוש ב-Phi-4-multimodal כעיתונאי טכנולוגיה](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [אפליקציית קונסול .NET המשתמשת ב-Phi-4-multimodal לניתוח תמונות](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- דוגמאות כיוונון Phi  
  - [תרחישי כיוונון](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [כיוונון מול RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [כיוונון Phi-3 להפוך למומחה בתעשייה](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [כיוונון Phi-3 עם AI Toolkit ל-VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [כיוונון Phi-3 עם שירות Azure Machine Learning](./md/03.FineTuning/Introduce_AzureML.md)  
  - [כיוונון Phi-3 עם Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [כיוונון Phi-3 עם QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [כיוונון Phi-3 עם Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [כיוונון Phi-3 עם Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [כיוונון עם Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [כיוונון עם Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)  
  - [כיוונון Phi-3-vision עם Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [כיוונון Phi-3 עם מסגרת Apple MLX](./md/03.FineTuning/FineTuning_MLX.md)  
  - [כיוונון Phi-3-vision (תמיכה רשמית)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [כיוונון Phi-3 עם Kaito AKS, מכולות Azure (תמיכה רשמית)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [כיוונון Phi-3 ו-3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- מעבדת Hands-On  
  - [חקירת מודלים מתקדמים: LLMs, SLMs, פיתוח מקומי ועוד](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [שחרור הפוטנציאל של NLP: כיוונון עם Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- מאמרים ומחקרים אקדמיים  
  - [Textbooks Are All You Need II: דו"ח טכני phi-1.5](https://arxiv.org/abs/2309.05463)  
  - [דו"ח טכני Phi-3: מודל שפה בעל יכולות גבוהות מקומית על הטלפון שלך](https://arxiv.org/abs/2404.14219)  
  - [דו"ח טכני Phi-4](https://arxiv.org/abs/2412.08905)  
  - [דו"ח טכני Phi-4-Mini: מודלים שפה מולטימודלים קומפקטיים אך עוצמתיים באמצעות Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [אופטימיזציה של מודלים לשוניים קטנים לקריאה לפונקציות בתוך רכב](https://arxiv.org/abs/2501.02342)
  - [(WhyPHI) כיוונון עדין של PHI-3 למענה על שאלות רב-ברירה: מתודולוגיה, תוצאות ואתגרים](https://arxiv.org/abs/2501.01588)
  - [דו"ח טכני על Phi-4-reasoning](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)
  - [דו"ח טכני על Phi-4-mini-reasoning](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)

## שימוש במודלים של Phi

### Phi ב-Azure AI Foundry

ניתן ללמוד כיצד להשתמש ב-Microsoft Phi וכיצד לבנות פתרונות מקצה לקצה במכשירי החומרה השונים שלכם. כדי להתנסות ב-Phi בעצמכם, התחילו לשחק עם המודלים והתאימו את Phi לתרחישים שלכם באמצעות [קטלוג המודלים של Azure AI Foundry](https://aka.ms/phi3-azure-ai). ניתן ללמוד עוד במדריך ההתחלה של [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).

**Playground**  
לכל מודל יש סביבת ניסוי ייעודית לבדיקת המודל [Azure AI Playground](https://aka.ms/try-phi3).

### Phi ב-GitHub Models

ניתן ללמוד כיצד להשתמש ב-Microsoft Phi וכיצד לבנות פתרונות מקצה לקצה במכשירי החומרה השונים שלכם. כדי להתנסות ב-Phi בעצמכם, התחילו לשחק עם המודל והתאימו את Phi לתרחישים שלכם באמצעות [קטלוג המודלים של GitHub](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). ניתן ללמוד עוד במדריך ההתחלה של [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).

**Playground**  
לכל מודל יש [סביבת ניסוי ייעודית לבדיקת המודל](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi ב-Hugging Face

ניתן גם למצוא את המודל ב-[Hugging Face](https://huggingface.co/microsoft).

**Playground**  
[סביבת ניסוי של Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct).

## AI אחראי

מיקרוסופט מחויבת לעזור ללקוחותיה להשתמש במוצרי הבינה המלאכותית שלה באופן אחראי, לשתף את הלקחים שנלמדו ולבנות שותפויות מבוססות אמון באמצעות כלים כמו הערות שקיפות והערכות השפעה. ניתן למצוא משאבים רבים בנושא זה ב-[https://aka.ms/RAI](https://aka.ms/RAI).  
הגישה של מיקרוסופט לבינה מלאכותית אחראית מבוססת על עקרונות הבינה המלאכותית שלנו: הוגנות, אמינות ובטיחות, פרטיות ואבטחה, הכללה, שקיפות ואחריות.

מודלים רחבי היקף של שפה טבעית, תמונה ודיבור - כמו אלו המשמשים בדוגמה זו - עשויים להתנהג בדרכים לא הוגנות, לא אמינות או פוגעניות, ובכך לגרום לנזקים. אנא עיינו ב-[הערת השקיפות של שירות Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) כדי להיות מודעים לסיכונים ולמגבלות.

הגישה המומלצת להפחתת סיכונים אלו היא לכלול מערכת בטיחות בארכיטקטורה שלכם שיכולה לזהות ולמנוע התנהגות מזיקה. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) מספק שכבת הגנה עצמאית, המסוגלת לזהות תוכן מזיק שנוצר על ידי משתמשים או על ידי AI באפליקציות ושירותים. Azure AI Content Safety כולל APIs לטקסט ולתמונות שמאפשרים לזהות חומר מזיק. בתוך Azure AI Foundry, שירות Content Safety מאפשר לכם לצפות, לחקור ולנסות קוד לדוגמה לזיהוי תוכן מזיק במגוון אופנים. [תיעוד ההתחלה המהירה](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) מדריך אתכם כיצד לבצע בקשות לשירות.

היבט נוסף שיש לקחת בחשבון הוא ביצועי האפליקציה הכוללים. באפליקציות רב-מודליות ורב-מודלים, אנו מתייחסים לביצועים כאל היכולת של המערכת לפעול כפי שאתם והמשתמשים שלכם מצפים, כולל אי-יצירת פלטים מזיקים. חשוב להעריך את ביצועי האפליקציה הכוללת שלכם באמצעות [מדריכים להערכת ביצועים ואיכות וסיכונים ובטיחות](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). יש לכם גם את היכולת ליצור ולהעריך באמצעות [מדריכים מותאמים אישית](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).

ניתן להעריך את אפליקציית הבינה המלאכותית שלכם בסביבת הפיתוח באמצעות [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). בהתבסס על מערך נתונים לבדיקה או יעד, הפלטים של אפליקציית הבינה המלאכותית שלכם נמדדים באופן כמותי באמצעות מדריכים מובנים או מותאמים אישית לבחירתכם. כדי להתחיל עם Azure AI Evaluation SDK להערכת המערכת שלכם, ניתן לעקוב אחר [מדריך ההתחלה המהירה](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). לאחר ביצוע ריצת הערכה, ניתן [לראות את התוצאות ב-Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## סימנים מסחריים

פרויקט זה עשוי לכלול סימנים מסחריים או לוגואים של פרויקטים, מוצרים או שירותים. שימוש מורשה בסימנים המסחריים או בלוגואים של מיקרוסופט כפוף ל-[הנחיות השימוש בסימנים מסחריים ומותגים של מיקרוסופט](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
שימוש בסימנים המסחריים או בלוגואים של מיקרוסופט בגרסאות מותאמות של פרויקט זה חייב שלא לגרום לבלבול או לרמוז על חסות של מיקרוסופט. כל שימוש בסימנים מסחריים או בלוגואים של צד שלישי כפוף למדיניות של אותו צד שלישי.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי בני אדם. איננו אחראים לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.