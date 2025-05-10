<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-05-09T12:28:23+00:00",
  "source_file": "md/01.Introduction/03/overview.md",
  "language_code": "he"
}
-->
בהקשר של Phi-3-mini, אינפרנס מתייחס לתהליך של שימוש במודל כדי לבצע תחזיות או ליצור פלטים בהתבסס על נתוני קלט. אתן לכם פרטים נוספים על Phi-3-mini ועל יכולות האינפרנס שלו.

Phi-3-mini הוא חלק מסדרת Phi-3 של מודלים שפורסמו על ידי מיקרוסופט. מודלים אלה מיועדים להגדיר מחדש את מה שאפשרי עם מודלי שפה קטנים (SLMs).

הנה כמה נקודות מרכזיות על Phi-3-mini ועל יכולות האינפרנס שלו:

## **סקירה כללית של Phi-3-mini:**
- ל-Phi-3-mini יש גודל פרמטרים של 3.8 מיליארד.
- הוא יכול לפעול לא רק על מכשירי מחשוב מסורתיים אלא גם על מכשירי קצה כמו מכשירים ניידים ומכשירי IoT.
- השחרור של Phi-3-mini מאפשר לאנשים פרטיים ולארגונים לפרוס SLMs על מכשירים שונים, במיוחד בסביבות עם משאבים מוגבלים.
- הוא תומך בפורמטים שונים של מודלים, כולל פורמט PyTorch המסורתי, גרסה מקודדת של פורמט gguf, וגרסה מקודדת מבוססת ONNX.

## **גישה ל-Phi-3-mini:**
כדי לגשת ל-Phi-3-mini, ניתן להשתמש ב-[Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) באפליקציית Copilot. Semantic Kernel תואם בדרך כלל לשירות Azure OpenAI, למודלים בקוד פתוח ב-Hugging Face ולמודלים מקומיים.
ניתן גם להשתמש ב-[Ollama](https://ollama.com) או ב-[LlamaEdge](https://llamaedge.com) לקריאה למודלים מקודדים. Ollama מאפשרת למשתמשים פרטיים לקרוא למודלים מקודדים שונים, בעוד ש-LlamaEdge מספקת זמינות חוצת פלטפורמות למודלי GGUF.

## **מודלים מקודדים:**
רבים מהמשתמשים מעדיפים להשתמש במודלים מקודדים לאינפרנס מקומי. לדוגמה, ניתן להריץ ישירות את Ollama עם Phi-3 או להגדיר אותו במצב לא מקוון באמצעות Modelfile. קובץ ה-Modelfile מגדיר את נתיב קובץ ה-GGUF ואת פורמט הפרומפט.

## **אפשרויות AI גנרטיבי:**
שילוב של SLMs כמו Phi-3-mini פותח אפשרויות חדשות ל-AI גנרטיבי. אינפרנס הוא רק הצעד הראשון; מודלים אלה יכולים לשמש למשימות שונות בסביבות עם מגבלות משאבים, מגבלות זמן תגובה ומגבלות תקציב.

## **שחרור ה-AI הגנרטיבי עם Phi-3-mini: מדריך לאינפרנס ופריסה**
למד כיצד להשתמש ב-Semantic Kernel, Ollama/LlamaEdge ו-ONNX Runtime כדי לגשת ולבצע אינפרנס על מודלי Phi-3-mini, וחקור את האפשרויות של AI גנרטיבי בתרחישי יישום שונים.

**תכונות**
אינפרנס למודל phi3-mini ב:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

לסיכום, Phi-3-mini מאפשר למפתחים לחקור פורמטים שונים של מודלים ולהשתמש ב-AI גנרטיבי בתרחישי יישום מגוונים.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפת המקור שלו צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו אחראים לכל אי הבנה או פרשנות שגויה הנובעים משימוש בתרגום זה.