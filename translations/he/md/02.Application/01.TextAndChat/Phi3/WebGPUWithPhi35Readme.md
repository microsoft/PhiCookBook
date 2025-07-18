<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-07-17T03:11:24+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "he"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## הדגמה להצגת WebGPU ותבנית RAG

תבנית RAG עם מודל Phi-3.5 Onnx Hosted משתמשת בגישה של Retrieval-Augmented Generation, שמשלבת את כוחם של מודלי Phi-3.5 עם אירוח ONNX לפריסות AI יעילות. תבנית זו חשובה לכיול מדויק של מודלים למשימות ספציפיות לתחום, ומציעה שילוב של איכות, עלות-תועלת והבנה של הקשר ארוך. היא חלק מחבילת Azure AI, שמספקת מבחר רחב של מודלים שקל למצוא, לנסות ולהשתמש בהם, ומתאימה לצרכי ההתאמה האישית של תעשיות שונות.

## מה זה WebGPU  
WebGPU הוא API גרפי מודרני לאינטרנט, שנועד לספק גישה יעילה ליחידת העיבוד הגרפית (GPU) של המכשיר ישירות מדפדפני האינטרנט. הוא מיועד להחליף את WebGL, ומציע מספר שיפורים מרכזיים:

1. **תאימות עם GPUs מודרניים**: WebGPU בנוי לעבוד בצורה חלקה עם ארכיטקטורות GPU עכשוויות, תוך שימוש ב-APIs של המערכת כמו Vulkan, Metal ו-Direct3D 12.
2. **ביצועים משופרים**: הוא תומך בחישובים כלליים על ה-GPU ובפעולות מהירות יותר, מה שהופך אותו למתאים גם להצגת גרפיקה וגם למשימות למידת מכונה.
3. **תכונות מתקדמות**: WebGPU מספק גישה ליכולות GPU מתקדמות יותר, המאפשרות עבודה עם גרפיקה מורכבת ודינמית ועומסי חישוב מתקדמים.
4. **הפחתת עומס על JavaScript**: על ידי העברת יותר משימות ל-GPU, WebGPU מפחית משמעותית את העומס על JavaScript, מה שמוביל לביצועים טובים יותר וחוויות חלקות יותר.

כיום WebGPU נתמך בדפדפנים כמו Google Chrome, ומתקיימים מאמצים להרחיב את התמיכה לפלטפורמות נוספות.

### 03.WebGPU  
סביבת עבודה נדרשת:

**דפדפנים נתמכים:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### הפעלת WebGPU:

- ב-Chrome/Microsoft Edge  

הפעל את הדגל `chrome://flags/#enable-unsafe-webgpu`.

#### פתח את הדפדפן שלך:  
הפעל את Google Chrome או Microsoft Edge.

#### גש לעמוד הדגלים:  
בשורת הכתובת, הקלד `chrome://flags` ולחץ Enter.

#### חפש את הדגל:  
בתיבת החיפוש בראש העמוד, הקלד 'enable-unsafe-webgpu'

#### הפעל את הדגל:  
מצא את הדגל #enable-unsafe-webgpu ברשימת התוצאות.

לחץ על תפריט הנפתח שלצדו ובחר Enabled.

#### הפעל מחדש את הדפדפן שלך:  

לאחר הפעלת הדגל, תצטרך להפעיל מחדש את הדפדפן כדי שהשינויים ייכנסו לתוקף. לחץ על כפתור Relaunch שמופיע בתחתית העמוד.

- בלינוקס, הפעל את הדפדפן עם `--enable-features=Vulkan`.  
- ב-Safari 18 (macOS 15) WebGPU מופעל כברירת מחדל.  
- ב-Firefox Nightly, הקלד about:config בשורת הכתובת ו`set dom.webgpu.enabled to true`.

### הגדרת GPU עבור Microsoft Edge  

הנה השלבים להגדרת GPU ביצועים גבוהים עבור Microsoft Edge ב-Windows:

- **פתח הגדרות:** לחץ על תפריט התחל ובחר בהגדרות.  
- **הגדרות מערכת:** עבור ל-System ואז ל-Display.  
- **הגדרות גרפיקה:** גלול למטה ולחץ על Graphics settings.  
- **בחר אפליקציה:** תחת “Choose an app to set preference,” בחר Desktop app ואז Browse.  
- **בחר את Edge:** נווט לתיקיית ההתקנה של Edge (בדרך כלל `C:\Program Files (x86)\Microsoft\Edge\Application`) ובחר `msedge.exe`.  
- **הגדר העדפה:** לחץ על Options, בחר High performance ואז לחץ על Save.  
זה יבטיח ש-Microsoft Edge ישתמש ב-GPU ביצועים גבוהים שלך לביצועים טובים יותר.  
- **הפעל מחדש** את המחשב כדי שההגדרות ייכנסו לתוקף.

### דוגמאות : אנא [לחץ כאן](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.