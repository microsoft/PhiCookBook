# **הסקת מסקנות Phi-3 באנדרואיד**

בואו נבדוק כיצד ניתן לבצע הסקת מסקנות עם Phi-3-mini במכשירי אנדרואיד. Phi-3-mini היא סדרת דגמים חדשה של מיקרוסופט שמאפשרת פריסה של מודלים גדולים של שפה (LLMs) במכשירי קצה ומכשירי IoT.

## Semantic Kernel והסקת מסקנות

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) הוא מסגרת עבודה ליצירת אפליקציות התואמות לשירות Azure OpenAI, למודלים של OpenAI ואפילו למודלים מקומיים. אם אתם חדשים ב-Semantic Kernel, מומלץ לעיין ב-[Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### גישה ל-Phi-3-mini באמצעות Semantic Kernel

ניתן לשלב אותו עם Hugging Face Connector ב-Semantic Kernel. עיינו ב-[קוד לדוגמה](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

ברירת המחדל היא שהחיבור מתייחס ל-ID של המודל ב-Hugging Face. עם זאת, ניתן גם להתחבר לשרת מודל Phi-3-mini שנבנה מקומית.

### קריאה למודלים מקוונטים עם Ollama או LlamaEdge

רבים מהמשתמשים מעדיפים להשתמש במודלים מקוונטים כדי להריץ מודלים באופן מקומי. [Ollama](https://ollama.com/) ו-[LlamaEdge](https://llamaedge.com) מאפשרים למשתמשים פרטיים לקרוא למודלים מקוונטים שונים:

#### Ollama

ניתן להריץ ישירות `ollama run Phi-3` או להגדיר אותו במצב לא מקוון על ידי יצירת `Modelfile` עם הנתיב לקובץ ה-`.gguf` שלכם.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[קוד לדוגמה](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

אם ברצונכם להשתמש בקבצי `.gguf` בענן ובמכשירי קצה בו זמנית, LlamaEdge היא בחירה מצוינת. ניתן לעיין ב-[קוד לדוגמה](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) כדי להתחיל.

### התקנה והרצה בטלפונים עם אנדרואיד

1. **הורידו את אפליקציית MLC Chat** (חינמית) לטלפונים עם אנדרואיד.  
2. הורידו את קובץ ה-APK (גודל 148MB) והתקינו אותו במכשיר שלכם.  
3. הפעלו את אפליקציית MLC Chat. תראו רשימה של מודלים מבוססי AI, כולל Phi-3-mini.

לסיכום, Phi-3-mini פותח אפשרויות מרגשות ל-AI גנרטיבי במכשירי קצה, ואתם יכולים להתחיל לחקור את היכולות שלו באנדרואיד.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.