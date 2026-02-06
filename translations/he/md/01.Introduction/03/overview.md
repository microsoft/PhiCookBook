בהקשר של Phi-3-mini, אינפרנס מתייחס לתהליך של שימוש במודל כדי לבצע תחזיות או לייצר פלטים בהתבסס על נתוני קלט. הרשה לי לספק לך פרטים נוספים על Phi-3-mini ועל יכולות האינפרנס שלו.

Phi-3-mini הוא חלק מסדרת המודלים Phi-3 שפורסמה על ידי מיקרוסופט. מודלים אלו נועדו להגדיר מחדש את מה שאפשרי עם מודלים שפתיים קטנים (SLMs).

להלן כמה נקודות מפתח על Phi-3-mini ועל יכולות האינפרנס שלו:

## **סקירה כללית של Phi-3-mini:**
- ל-Phi-3-mini יש גודל פרמטרים של 3.8 מיליארד.
- הוא יכול לפעול לא רק על מכשירי מחשוב מסורתיים אלא גם על מכשירי קצה כמו מכשירים ניידים ומכשירי IoT.
- השחרור של Phi-3-mini מאפשר לאנשים פרטיים ולארגונים לפרוס SLMs על מכשירים שונים, במיוחד בסביבות עם משאבים מוגבלים.
- הוא תומך בפורמטים שונים של מודלים, כולל פורמט PyTorch המסורתי, הגרסה הכמותית של פורמט gguf, והגרסה הכמותית מבוססת ONNX.

## **גישה ל-Phi-3-mini:**
כדי לגשת ל-Phi-3-mini, ניתן להשתמש ב-[Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) באפליקציית Copilot. Semantic Kernel תואם בדרך כלל לשירות Azure OpenAI, למודלים בקוד פתוח ב-Hugging Face ולמודלים מקומיים.
ניתן גם להשתמש ב-[Ollama](https://ollama.com) או ב-[LlamaEdge](https://llamaedge.com) כדי לקרוא למודלים כמותיים. Ollama מאפשר למשתמשים פרטיים לקרוא למודלים כמותיים שונים, בעוד ש-LlamaEdge מספק זמינות חוצת פלטפורמות למודלים בפורמט GGUF.

## **מודלים כמותיים:**
רבים מהמשתמשים מעדיפים להשתמש במודלים כמותיים לאינפרנס מקומי. לדוגמה, ניתן להריץ ישירות ב-Ollama את Phi-3 או להגדיר אותו במצב לא מקוון באמצעות Modelfile. קובץ ה-Modelfile מגדיר את נתיב הקובץ GGUF ואת פורמט הפקודה.

## **אפשרויות AI גנרטיבי:**
שילוב של SLMs כמו Phi-3-mini פותח אפשרויות חדשות ל-AI גנרטיבי. אינפרנס הוא רק השלב הראשון; מודלים אלו יכולים לשמש למשימות שונות בסביבות עם משאבים מוגבלים, מגבלות זמן תגובה ועלויות.

## **שחרור ה-AI הגנרטיבי עם Phi-3-mini: מדריך לאינפרנס ופריסה**  
למד כיצד להשתמש ב-Semantic Kernel, Ollama/LlamaEdge ו-ONNX Runtime כדי לגשת ולבצע אינפרנס עם מודלים של Phi-3-mini, וחקור את האפשרויות של AI גנרטיבי בתרחישי יישום שונים.

**תכונות**  
אינפרנס של מודל phi3-mini ב:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

לסיכום, Phi-3-mini מאפשר למפתחים לחקור פורמטים שונים של מודלים ולנצל את ה-AI הגנרטיבי בתרחישי יישום מגוונים.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.