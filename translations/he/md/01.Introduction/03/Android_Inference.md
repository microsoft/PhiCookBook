<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-05-09T10:47:53+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "he"
}
-->
# **Inference Phi-3 ב-Android**

בואו נחקור כיצד ניתן לבצע inference עם Phi-3-mini במכשירי Android. Phi-3-mini היא סדרת דגמים חדשה של Microsoft שמאפשרת פריסה של Large Language Models (LLMs) במכשירי edge ו-IoT.

## Semantic Kernel ו-Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) הוא מסגרת יישומים שמאפשרת ליצור יישומים התואמים ל-Azure OpenAI Service, לדגמי OpenAI, ואפילו לדגמים מקומיים. אם אתם חדשים ב-Semantic Kernel, מומלץ לעיין ב-[Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### גישה ל-Phi-3-mini באמצעות Semantic Kernel

ניתן לשלב אותו עם Hugging Face Connector ב-Semantic Kernel. עיינו ב-[קוד לדוגמה](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

ברירת המחדל היא התאמה ל-model ID ב-Hugging Face, אך ניתן גם להתחבר לשרת דגם Phi-3-mini שנבנה מקומית.

### קריאה לדגמים מקודדים עם Ollama או LlamaEdge

משתמשים רבים מעדיפים להשתמש בדגמים מקודדים כדי להריץ דגמים באופן מקומי. [Ollama](https://ollama.com/) ו-[LlamaEdge](https://llamaedge.com) מאפשרים למשתמשים פרטיים לקרוא לדגמים מקודדים שונים:

#### Ollama

ניתן להריץ ישירות `ollama run Phi-3` או להגדיר אותו באופן לא מקוון על ידי יצירת `Modelfile` עם הנתיב לקובץ `.gguf` שלך.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[קוד לדוגמה](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

אם רוצים להשתמש בקבצי `.gguf` בענן ובמכשירי edge בו-זמנית, LlamaEdge היא בחירה מצוינת. ניתן לעיין ב-[קוד לדוגמה](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) כדי להתחיל.

### התקנה והרצה בטלפונים מבוססי Android

1. **הורידו את אפליקציית MLC Chat** (חינמית) לטלפונים מבוססי Android.  
2. הורידו את קובץ ה-APK (גודלו 148MB) והתקינו אותו במכשיר.  
3. הפעלו את אפליקציית MLC Chat. תראו רשימת דגמי AI, כולל Phi-3-mini.

לסיכום, Phi-3-mini פותח אפשרויות מרגשות ל-AI גנרטיבי במכשירי edge, וניתן להתחיל לחקור את היכולות שלו ב-Android.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי מבוצע על ידי אדם. אנו לא נושאים באחריות לכל אי הבנה או פרשנות שגויה הנובעים משימוש בתרגום זה.