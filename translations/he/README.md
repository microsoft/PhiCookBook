<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "698f7f3d48ebc9e25a273d7c8b7e31c5",
  "translation_date": "2025-09-12T14:00:32+00:00",
  "source_file": "README.md",
  "language_code": "he"
}
-->
# ספר מתכונים של Phi: דוגמאות מעשיות עם מודלים של Phi מבית Microsoft

Phi הוא סדרת מודלים AI בקוד פתוח שפותחו על ידי Microsoft.

Phi הוא כיום מודל שפה קטן (SLM) עוצמתי וחסכוני במיוחד, עם ביצועים מצוינים במבחנים רב-לשוניים, הסקת מסקנות, יצירת טקסט/צ'אט, קידוד, תמונות, אודיו ותסריטים נוספים.

ניתן לפרוס את Phi לענן או למכשירי קצה, ולבנות בקלות יישומי AI גנרטיביים עם כוח מחשוב מוגבל.

עקבו אחר השלבים הבאים כדי להתחיל להשתמש במשאבים אלו:
1. **פיצול המאגר**: לחצו [![GitHub forks](https://img.shields.io/github/forks/microsoft/phicookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phicookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
2. **שכפול המאגר**:   `git clone https://github.com/microsoft/PhiCookBook.git`
3. [**הצטרפו לקהילת Microsoft AI ב-Discord ופגשו מומחים ומפתחים נוספים**](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

![cover](../../imgs/cover.png)

### 🌐 תמיכה רב-לשונית

#### נתמך באמצעות GitHub Action (אוטומטי ותמיד מעודכן)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) 
[Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](./README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md)

## תוכן עניינים

- מבוא
  - [ברוכים הבאים למשפחת Phi](./md/01.Introduction/01/01.PhiFamily.md)
  - [הגדרת סביבת העבודה שלכם](./md/01.Introduction/01/01.EnvironmentSetup.md)
  - [הבנת טכנולוגיות מרכזיות](./md/01.Introduction/01/01.Understandingtech.md)
  - [בטיחות AI עבור מודלים של Phi](./md/01.Introduction/01/01.AISafety.md)
  - [תמיכה בחומרה עבור Phi](./md/01.Introduction/01/01.Hardwaresupport.md)
  - [מודלים של Phi וזמינותם בפלטפורמות שונות](./md/01.Introduction/01/01.Edgeandcloud.md)
  - [שימוש ב-Guidance-ai וב-Phi](./md/01.Introduction/01/01.Guidance.md)
  - [מודלים ב-GitHub Marketplace](https://github.com/marketplace/models)
  - [קטלוג מודלים של Azure AI](https://ai.azure.com)

- ביצוע הסקה עם Phi בסביבות שונות
    -  [Hugging face](./md/01.Introduction/02/01.HF.md)
    -  [מודלים ב-GitHub](./md/01.Introduction/02/02.GitHubModel.md)
    -  [קטלוג מודלים של Azure AI Foundry](./md/01.Introduction/02/03.AzureAIFoundry.md)
    -  [Ollama](./md/01.Introduction/02/04.Ollama.md)
    -  [AI Toolkit VSCode (AITK)](./md/01.Introduction/02/05.AITK.md)
    -  [NVIDIA NIM](./md/01.Introduction/02/06.NVIDIA.md)
    -  [Foundry Local](./md/01.Introduction/02/07.FoundryLocal.md)

- ביצוע הסקה עם משפחת Phi
    - [ביצוע הסקה עם Phi ב-iOS](./md/01.Introduction/03/iOS_Inference.md)
    - [ביצוע הסקה עם Phi באנדרואיד](./md/01.Introduction/03/Android_Inference.md)
    - [ביצוע הסקה עם Phi ב-Jetson](./md/01.Introduction/03/Jetson_Inference.md)
    - [ביצוע הסקה עם Phi במחשב AI](./md/01.Introduction/03/AIPC_Inference.md)
    - [ביצוע הסקה עם Phi באמצעות Apple MLX Framework](./md/01.Introduction/03/MLX_Inference.md)
    - [ביצוע הסקה עם Phi בשרת מקומי](./md/01.Introduction/03/Local_Server_Inference.md)
    - [ביצוע הסקה עם Phi בשרת מרוחק באמצעות AI Toolkit](./md/01.Introduction/03/Remote_Interence.md)
    - [ביצוע הסקה עם Phi באמצעות Rust](./md/01.Introduction/03/Rust_Inference.md)
    - [ביצוע הסקה עם Phi--Vision באופן מקומי](./md/01.Introduction/03/Vision_Inference.md)
    - [ביצוע הסקה עם Phi באמצעות Kaito AKS, Azure Containers (תמיכה רשמית)](./md/01.Introduction/03/Kaito_Inference.md)

- [כימות משפחת Phi](./md/01.Introduction/04/QuantifyingPhi.md)
    - [כימות Phi-3.5 / 4 באמצעות llama.cpp](./md/01.Introduction/04/UsingLlamacppQuantifyingPhi.md)
    - [כימות Phi-3.5 / 4 באמצעות הרחבות AI גנרטיביות עבור onnxruntime](./md/01.Introduction/04/UsingORTGenAIQuantifyingPhi.md)
    - [כימות Phi-3.5 / 4 באמצעות Intel OpenVINO](./md/01.Introduction/04/UsingIntelOpenVINOQuantifyingPhi.md)
    - [כימות Phi-3.5 / 4 באמצעות Apple MLX Framework](./md/01.Introduction/04/UsingAppleMLXQuantifyingPhi.md)

- הערכת Phi
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
      - [אפליקציית קונסול .NET עם Phi-4 ONNX באמצעות Semantic Kernel](../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK)
    - דוגמאות Phi-3 / 3.5
      - [צ'אט מקומי בדפדפן באמצעות Phi3, ONNX Runtime Web ו-WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)
      - [צ'אט OpenVino](./md/02.Application/01.TextAndChat/Phi3/E2E_OpenVino_Chat.md)
      - [מודל רב-תפקודי - אינטראקטיבי עם Phi-3-mini ו-OpenAI Whisper](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-mini_with_whisper.md)
      - [MLFlow - בניית מעטפת ושימוש ב-Phi-3 עם MLFlow](./md//02.Application/01.TextAndChat/Phi3/E2E_Phi-3-MLflow.md)
      - [אופטימיזציה של מודל - כיצד לבצע אופטימיזציה למודל Phi-3-min עבור ONNX Runtime Web עם Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)
      - [אפליקציית WinUI3 עם Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)
      - [אפליקציית הערות AI רב-מודלית לדוגמה ב-WinUI3](https://github.com/microsoft/ai-powered-notes-winui3-sample)
- [התאמה אישית ושילוב של מודלים מותאמים אישית Phi-3 עם Prompt flow](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)  
- [התאמה אישית ושילוב של מודלים מותאמים אישית Phi-3 עם Prompt flow ב-Azure AI Foundry](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md)  
- [הערכת מודל Phi-3 / Phi-3.5 מותאם אישית ב-Azure AI Foundry תוך התמקדות בעקרונות AI אחראי של Microsoft](./md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-Evaluation_AIFoundry.md)  
- [📓] [דוגמה לחיזוי שפה עם Phi-3.5-mini-instruct (סינית/אנגלית)](../../md/02.Application/01.TextAndChat/Phi3/phi3-instruct-demo.ipynb)  
- [צ'אטבוט RAG מבוסס WebGPU עם Phi-3.5-Instruct](./md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md)  
- [שימוש ב-GPU של Windows ליצירת פתרון Prompt flow עם Phi-3.5-Instruct ONNX](./md/02.Application/01.TextAndChat/Phi3/UsingPromptFlowWithONNX.md)  
- [שימוש ב-Microsoft Phi-3.5 tflite ליצירת אפליקציית אנדרואיד](./md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md)  
- [דוגמת Q&A ב-.NET עם מודל Phi-3 מקומי באמצעות Microsoft.ML.OnnxRuntime](../../md/04.HOL/dotnet/src/LabsPhi301)  
- [אפליקציית צ'אט ב-.NET עם Semantic Kernel ו-Phi-3](../../md/04.HOL/dotnet/src/LabsPhi302)  

- דוגמאות קוד מבוססות SDK של Azure AI Inference  
  - דוגמאות Phi-4 🆕  
    - [📓] [יצירת קוד פרויקט באמצעות Phi-4-multimodal](./md/02.Application/02.Code/Phi4/GenProjectCode/README.md)  
  - דוגמאות Phi-3 / 3.5  
    - [בניית צ'אט GitHub Copilot משלך ב-Visual Studio Code עם משפחת Phi-3 של Microsoft](./md/02.Application/02.Code/Phi3/VSCodeExt/README.md)  
    - [יצירת סוכן צ'אט Copilot משלך ב-Visual Studio Code עם Phi-3.5 באמצעות מודלים של GitHub](/md/02.Application/02.Code/Phi3/CreateVSCodeChatAgentWithGitHubModels.md)  

- דוגמאות הסקה מתקדמות  
  - דוגמאות Phi-4 🆕  
    - [📓] [דוגמאות Phi-4-mini-reasoning או Phi-4-reasoning](./md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/README.md)  
    - [📓] [התאמה אישית של Phi-4-mini-reasoning עם Microsoft Olive](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/olive_ft_phi_4_reasoning_with_medicaldata.ipynb)  
    - [📓] [התאמה אישית של Phi-4-mini-reasoning עם Apple MLX](../../md/02.Application/03.AdvancedReasoning/Phi4/AdvancedResoningPhi4mini/mlx_ft_phi_4_reasoning_with_medicaldata.ipynb)  
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
    - [מודל ONNX מקומי של Phi-3 Vision באמצעות Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi303)  
    - [מודל ONNX מקומי של Phi-3 Vision מבוסס תפריט באמצעות Microsoft.ML.OnnxRuntime .NET](../../md/04.HOL/dotnet/src/LabsPhi304)  

- דוגמאות מתמטיות  
  - דוגמאות Phi-4-Mini-Flash-Reasoning-Instruct 🆕 [דוגמת מתמטיקה עם Phi-4-Mini-Flash-Reasoning-Instruct](../../md/02.Application/09.Math/MathDemo.ipynb)  

- דוגמאות שמע  
  - דוגמאות Phi-4 🆕  
    - [📓] [חילוץ תמלולי שמע באמצעות Phi-4-multimodal](./md/02.Application/05.Audio/Phi4/Transciption/README.md)  
    - [📓] [דוגמת שמע עם Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Siri/demo.ipynb)  
    - [📓] [דוגמת תרגום דיבור עם Phi-4-multimodal](../../md/02.Application/05.Audio/Phi4/Translate/demo.ipynb)  
    - [אפליקציית קונסולה ב-.NET המשתמשת ב-Phi-4-multimodal לניתוח קובץ שמע ויצירת תמלול](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio)  

- דוגמאות MOE  
  - דוגמאות Phi-3 / 3.5  
    - [📓] [Phi-3.5 Mixture of Experts Models (MoEs) דוגמת מדיה חברתית](../../md/02.Application/06.MoE/Phi3/phi3_moe_demo.ipynb)  
    - [📓] [בניית צינור RAG עם NVIDIA NIM Phi-3 MOE, Azure AI Search ו-LlamaIndex](../../md/02.Application/06.MoE/Phi3/azure-ai-search-nvidia-rag.ipynb)  

- דוגמאות קריאת פונקציות  
  - דוגמאות Phi-4 🆕  
    - [📓] [שימוש בקריאת פונקציות עם Phi-4-mini](./md/02.Application/07.FunctionCalling/Phi4/FunctionCallingBasic/README.md)  
    - [📓] [שימוש בקריאת פונקציות ליצירת סוכנים מרובים עם Phi-4-mini](../../md/02.Application/07.FunctionCalling/Phi4/Multiagents/Phi_4_mini_multiagent.ipynb)  
    - [📓] [שימוש בקריאת פונקציות עם Ollama](../../md/02.Application/07.FunctionCalling/Phi4/Ollama/ollama_functioncalling.ipynb)  
    - [📓] [שימוש בקריאת פונקציות עם ONNX](../../md/02.Application/07.FunctionCalling/Phi4/ONNX/onnx_parallel_functioncalling.ipynb)  

- דוגמאות ערבוב מולטימודלי  
  - דוגמאות Phi-4 🆕  
    - [📓] [שימוש ב-Phi-4-multimodal כעיתונאי טכנולוגיה](../../md/02.Application/08.Multimodel/Phi4/TechJournalist/phi_4_mm_audio_text_publish_news.ipynb)  
    - [אפליקציית קונסולה ב-.NET המשתמשת ב-Phi-4-multimodal לניתוח תמונות](../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images)  

- דוגמאות התאמה אישית של Phi  
  - [תרחישי התאמה אישית](./md/03.FineTuning/FineTuning_Scenarios.md)  
  - [התאמה אישית מול RAG](./md/03.FineTuning/FineTuning_vs_RAG.md)  
  - [התאמה אישית של Phi-3 להפוך למומחה תעשייתי](./md/03.FineTuning/LetPhi3gotoIndustriy.md)  
  - [התאמה אישית של Phi-3 עם AI Toolkit ל-VS Code](./md/03.FineTuning/Finetuning_VSCodeaitoolkit.md)  
  - [התאמה אישית של Phi-3 עם שירות Azure Machine Learning](./md/03.FineTuning/Introduce_AzureML.md)  
  - [התאמה אישית של Phi-3 עם Lora](./md/03.FineTuning/FineTuning_Lora.md)  
  - [התאמה אישית של Phi-3 עם QLora](./md/03.FineTuning/FineTuning_Qlora.md)  
  - [התאמה אישית של Phi-3 עם Azure AI Foundry](./md/03.FineTuning/FineTuning_AIFoundry.md)  
  - [התאמה אישית של Phi-3 עם Azure ML CLI/SDK](./md/03.FineTuning/FineTuning_MLSDK.md)  
  - [התאמה אישית עם Microsoft Olive](./md/03.FineTuning/FineTuning_MicrosoftOlive.md)  
  - [התאמה אישית עם Microsoft Olive Hands-On Lab](./md/03.FineTuning/olive-lab/readme.md)  
  - [התאמה אישית של Phi-3-vision עם Weights and Bias](./md/03.FineTuning/FineTuning_Phi-3-visionWandB.md)  
  - [התאמה אישית של Phi-3 עם Apple MLX Framework](./md/03.FineTuning/FineTuning_MLX.md)  
  - [התאמה אישית של Phi-3-vision (תמיכה רשמית)](./md/03.FineTuning/FineTuning_Vision.md)  
  - [התאמה אישית של Phi-3 עם Kaito AKS, Azure Containers (תמיכה רשמית)](./md/03.FineTuning/FineTuning_Kaito.md)  
  - [התאמה אישית של Phi-3 ו-3.5 Vision](https://github.com/2U1/Phi3-Vision-Finetune)  

- מעבדת Hands-On  
  - [חקר מודלים מתקדמים: LLMs, SLMs, פיתוח מקומי ועוד](https://github.com/microsoft/aitour-exploring-cutting-edge-models)  
  - [מימוש פוטנציאל NLP: התאמה אישית עם Microsoft Olive](https://github.com/azure/Ignite_FineTuning_workshop)  

- מאמרים ומחקרים אקדמיים  
  - [Textbooks Are All You Need II: דו"ח טכני phi-1.5](https://arxiv.org/abs/2309.05463)  
  - [דו"ח טכני Phi-3: מודל שפה מתקדם מקומי על הטלפון שלך](https://arxiv.org/abs/2404.14219)  
  - [דו"ח טכני Phi-4](https://arxiv.org/abs/2412.08905)  
  - [דו"ח טכני Phi-4-Mini: מודלים שפתיים מולטימודלים קומפקטיים אך עוצמתיים באמצעות Mixture-of-LoRAs](https://arxiv.org/abs/2503.01743)  
  - [אופטימיזציה של מודלים שפתיים קטנים לקריאת פונקציות בתוך רכב](https://arxiv.org/abs/2501.02342)  
  - [(WhyPHI) התאמה אישית של PHI-3 לשאלות רב-ברירה: מתודולוגיה, תוצאות ואתגרים](https://arxiv.org/abs/2501.01588)  
- [Phi-4-reasoning דוח טכני](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/phi_4_reasoning.pdf)  
- [Phi-4-mini-reasoning דוח טכני](https://huggingface.co/microsoft/Phi-4-mini-reasoning/blob/main/Phi-4-Mini-Reasoning.pdf)  

## שימוש במודלים של Phi  

### Phi ב-Azure AI Foundry  

ניתן ללמוד כיצד להשתמש ב-Microsoft Phi וכיצד לבנות פתרונות מקצה לקצה במכשירי החומרה השונים שלכם. כדי להתנסות ב-Phi בעצמכם, התחילו לשחק עם המודלים והתאימו את Phi לתרחישים שלכם באמצעות [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai). תוכלו ללמוד עוד במדריך ההתחלה [Azure AI Foundry](/md/02.QuickStart/AzureAIFoundry_QuickStart.md).  

**Playground**  
לכל מודל יש סביבת ניסוי ייעודית לבדיקת המודל [Azure AI Playground](https://aka.ms/try-phi3).  

### Phi ב-GitHub Models  

ניתן ללמוד כיצד להשתמש ב-Microsoft Phi וכיצד לבנות פתרונות מקצה לקצה במכשירי החומרה השונים שלכם. כדי להתנסות ב-Phi בעצמכם, התחילו לשחק עם המודל והתאימו את Phi לתרחישים שלכם באמצעות [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo). תוכלו ללמוד עוד במדריך ההתחלה [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md).  

**Playground**  
לכל מודל יש [סביבת ניסוי ייעודית לבדיקת המודל](/md/02.QuickStart/GitHubModel_QuickStart.md).  

### Phi ב-Hugging Face  

ניתן למצוא את המודל גם ב-[Hugging Face](https://huggingface.co/microsoft).  

**Playground**  
[סביבת ניסוי Hugging Chat](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct).  

## AI אחראי  

מיקרוסופט מחויבת לעזור ללקוחותיה להשתמש במוצרי הבינה המלאכותית שלה בצורה אחראית, לשתף את הידע שנצבר ולבנות שותפויות מבוססות אמון באמצעות כלים כמו הערות שקיפות והערכות השפעה. ניתן למצוא משאבים רבים ב-[https://aka.ms/RAI](https://aka.ms/RAI).  
הגישה של מיקרוסופט ל-AI אחראי מבוססת על עקרונות הבינה המלאכותית שלנו: הוגנות, אמינות ובטיחות, פרטיות ואבטחה, הכללה, שקיפות ואחריות.  

מודלים רחבי היקף של שפה טבעית, תמונה ודיבור - כמו אלו המשמשים בדוגמה זו - עשויים להתנהג בדרכים לא הוגנות, לא אמינות או פוגעניות, ובכך לגרום לנזקים. אנא עיינו ב-[הערת השקיפות של שירות Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) כדי להיות מודעים לסיכונים ולמגבלות.  

הגישה המומלצת להפחתת סיכונים אלו היא לכלול מערכת בטיחות בארכיטקטורה שלכם שיכולה לזהות ולמנוע התנהגות מזיקה. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) מספקת שכבת הגנה עצמאית, המסוגלת לזהות תוכן מזיק שנוצר על ידי משתמשים או על ידי AI באפליקציות ושירותים. Azure AI Content Safety כוללת APIs לטקסט ולתמונות שמאפשרים לזהות חומר מזיק. בתוך Azure AI Foundry, שירות Content Safety מאפשר לכם לצפות, לחקור ולנסות קוד לדוגמה לזיהוי תוכן מזיק במגוון אופנים. [תיעוד ההתחלה המהירה](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) מדריך אתכם כיצד לבצע בקשות לשירות.  

היבט נוסף שיש לקחת בחשבון הוא ביצועי האפליקציה הכוללים. באפליקציות רב-מודליות ורב-מודלים, אנו מגדירים ביצועים כיכולת המערכת לפעול כפי שאתם והמשתמשים שלכם מצפים, כולל אי-יצירת תוצאות מזיקות. חשוב להעריך את ביצועי האפליקציה הכוללת שלכם באמצעות [מדריכים להערכת ביצועים ואיכות וסיכונים ובטיחות](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in). יש לכם גם את היכולת ליצור ולהעריך באמצעות [מדריכים מותאמים אישית](https://learn.microsoft.com/azure/ai-studio/how-to/develop/evaluate-sdk#custom-evaluators).  

ניתן להעריך את אפליקציית הבינה המלאכותית שלכם בסביבת הפיתוח באמצעות [Azure AI Evaluation SDK](https://microsoft.github.io/promptflow/index.html). באמצעות סט נתונים לבדיקה או יעד, התוצאות של אפליקציית הבינה המלאכותית שלכם נמדדות באופן כמותי עם מדריכים מובנים או מותאמים אישית לבחירתכם. כדי להתחיל עם Azure AI Evaluation SDK להערכת המערכת שלכם, תוכלו לעקוב אחר [מדריך ההתחלה המהירה](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). לאחר ביצוע ריצת הערכה, תוכלו [לצפות בתוצאות ב-Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).  

## סימני מסחר  

פרויקט זה עשוי להכיל סימני מסחר או לוגואים עבור פרויקטים, מוצרים או שירותים. שימוש מורשה בסימני המסחר או הלוגואים של מיקרוסופט כפוף ל-[הנחיות סימני המסחר והמותג של מיקרוסופט](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).  
שימוש בסימני המסחר או הלוגואים של מיקרוסופט בגרסאות מותאמות של פרויקט זה חייב שלא לגרום לבלבול או לרמוז על חסות של מיקרוסופט. כל שימוש בסימני מסחר או לוגואים של צד שלישי כפוף למדיניות של אותם צדדים שלישיים.  

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. איננו נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.