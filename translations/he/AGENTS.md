<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "72e00a4ddbe9d6c25907d1eb19d041b8",
  "translation_date": "2025-10-17T10:57:56+00:00",
  "source_file": "AGENTS.md",
  "language_code": "he"
}
-->
# AGENTS.md

## סקירת הפרויקט

PhiCookBook הוא מאגר מתכונים מקיף המכיל דוגמאות מעשיות, מדריכים ותיעוד לעבודה עם משפחת מודלי השפה הקטנים (SLMs) של Microsoft Phi. המאגר מציג מגוון שימושים, כולל הסקה, כיוונון עדין, כימות, יישומי RAG ואפליקציות מולטימודליות בפלטפורמות ובמסגרות שונות.

**טכנולוגיות מרכזיות:**
- **שפות:** Python, C#/.NET, JavaScript/Node.js
- **מסגרות:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **פלטפורמות:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **סוגי מודלים:** Phi-3, Phi-3.5, Phi-4 (טקסט, חזותי, מולטימודלי, וריאציות של הסקה)

**מבנה המאגר:**
- `/code/` - דוגמאות קוד עובדות ומימושים לדוגמה
- `/md/` - תיעוד מפורט, מדריכים והוראות שימוש  
- `/translations/` - תרגומים רב-שפתיים (50+ שפות באמצעות זרימת עבודה אוטומטית)
- `/.devcontainer/` - תצורת מיכל פיתוח (Python 3.12 עם Ollama)

## הגדרת סביבת פיתוח

### שימוש ב-GitHub Codespaces או מיכלי פיתוח (מומלץ)

1. פתיחה ב-GitHub Codespaces (המהירה ביותר):
   - לחץ על התג "Open in GitHub Codespaces" ב-README
   - המיכל מוגדר אוטומטית עם Python 3.12 ו-Ollama עם Phi-3

2. פתיחה ב-VS Code Dev Containers:
   - השתמש בתג "Open in Dev Containers" מ-README
   - המיכל דורש מינימום של 16GB זיכרון במחשב מארח

### הגדרה מקומית

**דרישות מוקדמות:**
- Python 3.12 או גרסה מאוחרת יותר
- .NET 8.0 SDK (לדוגמאות C#)
- Node.js 18+ ו-npm (לדוגמאות JavaScript)
- מומלץ מינימום של 16GB RAM

**התקנה:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**לדוגמאות Python:**
נווט לתיקיות הדוגמאות הספציפיות והתקן את התלויות:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**לדוגמאות .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**לדוגמאות JavaScript/Web:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## ארגון המאגר

### דוגמאות קוד (`/code/`)

- **01.Introduce/** - מבואות בסיסיים ודוגמאות התחלתיות
- **03.Finetuning/** ו-**04.Finetuning/** - דוגמאות לכיוונון עדין בשיטות שונות
- **03.Inference/** - דוגמאות הסקה על חומרה שונה (AIPC, MLX)
- **06.E2E/** - דוגמאות אפליקציה מקצה לקצה
- **07.Lab/** - מימושים מעבדתיים/ניסיוניים
- **08.RAG/** - דוגמאות ל-Retrieval-Augmented Generation
- **09.UpdateSamples/** - דוגמאות מעודכנות אחרונות

### תיעוד (`/md/`)

- **01.Introduction/** - מדריכי מבוא, הגדרת סביבה, מדריכי פלטפורמה
- **02.Application/** - דוגמאות אפליקציה מאורגנות לפי סוג (טקסט, קוד, חזותי, אודיו וכו')
- **02.QuickStart/** - מדריכי התחלה מהירה ל-Azure AI Foundry ו-GitHub Models
- **03.FineTuning/** - תיעוד ומדריכים לכיוונון עדין
- **04.HOL/** - מעבדות מעשיות (כולל דוגמאות .NET)

### פורמטי קבצים

- **מחברות Jupyter (`.ipynb`)** - מדריכי Python אינטראקטיביים מסומנים ב-📓 ב-README
- **סקריפטים Python (`.py`)** - דוגמאות Python עצמאיות
- **פרויקטים C# (`.csproj`, `.sln`)** - אפליקציות ודוגמאות .NET
- **JavaScript (`.js`, `package.json`)** - דוגמאות מבוססות אינטרנט ו-Node.js
- **Markdown (`.md`)** - תיעוד ומדריכים

## עבודה עם דוגמאות

### הרצת מחברות Jupyter

רוב הדוגמאות מסופקות כמחברות Jupyter:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### הרצת סקריפטים Python

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### הרצת דוגמאות .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

או בניית פתרון שלם:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### הרצת דוגמאות JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## בדיקות

מאגר זה מכיל קוד לדוגמה ומדריכים ולא פרויקט תוכנה מסורתי עם בדיקות יחידה. האימות מתבצע בדרך כלל על ידי:

1. **הרצת הדוגמאות** - כל דוגמה צריכה לפעול ללא שגיאות
2. **אימות תוצאות** - בדוק שהתגובות של המודל מתאימות
3. **מעקב אחר מדריכים** - מדריכים שלב-אחר-שלב צריכים לפעול כפי שמתועד

**גישה נפוצה לאימות:**
- בדוק את הרצת הדוגמאות בסביבת היעד
- וודא שהתלויות מותקנות כראוי
- בדוק שהמודל מורד/נטען בהצלחה
- אשר שההתנהגות הצפויה תואמת לתיעוד

## סגנון קוד וקונבנציות

### הנחיות כלליות

- הדוגמאות צריכות להיות ברורות, מתועדות היטב וחינוכיות
- עקוב אחר קונבנציות ספציפיות לשפה (PEP 8 עבור Python, סטנדרטים של C# עבור .NET)
- שמור על דוגמאות ממוקדות בהדגמת יכולות ספציפיות של מודל Phi
- כלול הערות המסבירות מושגים מרכזיים ופרמטרים ספציפיים למודל

### סטנדרטים לתיעוד

**עיצוב URL:**
- השתמש בפורמט `[text](../../url)` ללא רווחים נוספים
- קישורים יחסיים: השתמש ב-`./` עבור תיקיה נוכחית, `../` עבור תיקיית אב
- אין לכלול קודים של שפות ב-URL (להימנע מ-`/en-us/`, `/en/`)

**תמונות:**
- אחסן את כל התמונות בתיקיית `/imgs/`
- השתמש בשמות תיאוריים עם תווים באנגלית, מספרים ומקפים
- דוגמה: `phi-3-architecture.png`

**קבצי Markdown:**
- התייחס לדוגמאות עובדות אמיתיות בתיקיית `/code/`
- שמור על תיעוד מסונכרן עם שינויים בקוד
- השתמש באימוג'י 📓 לסימון קישורים למחברות Jupyter ב-README

### ארגון קבצים

- דוגמאות קוד בתיקיית `/code/` מאורגנות לפי נושא/תכונה
- תיעוד בתיקיית `/md/` משקף את מבנה הקוד כאשר ניתן
- שמור על קבצים קשורים (מחברות, סקריפטים, תצורות) יחד בתיקיות משנה

## הנחיות Pull Request

### לפני הגשה

1. **צור Fork למאגר** לחשבונך
2. **הפרד PRs לפי סוג:**
   - תיקוני באגים ב-PR אחד
   - עדכוני תיעוד ב-PR אחר
   - דוגמאות חדשות ב-PR נפרד
   - תיקוני שגיאות כתיב יכולים להיות משולבים

3. **טפל בהתנגשויות מיזוג:**
   - עדכן את ענף `main` המקומי שלך לפני ביצוע שינויים
   - סנכרן עם המקור לעיתים קרובות

4. **PRs לתרגום:**
   - חייבים לכלול תרגומים לכל הקבצים בתיקייה
   - שמור על מבנה עקבי עם השפה המקורית

### בדיקות נדרשות

PRs מריצים אוטומטית זרימות עבודה של GitHub לאימות:

1. **אימות נתיב יחסי** - כל הקישורים הפנימיים חייבים לעבוד
   - בדוק קישורים מקומית: Ctrl+Click ב-VS Code
   - השתמש בהצעות נתיב מ-VS Code (`./` או `../`)

2. **בדיקת קוד שפה ב-URL** - URLs אינטרנטיים לא צריכים לכלול קודי שפה
   - הסר `/en-us/`, `/en/` או קודי שפה אחרים
   - השתמש ב-URLs בינלאומיים כלליים

3. **בדיקת URL שבור** - כל ה-URLs חייבים להחזיר סטטוס 200
   - וודא שהקישורים נגישים לפני הגשה
   - הערה: ייתכן שחלק מהכישלונות נובעים ממגבלות רשת

### פורמט כותרת PR

```
[component] Brief description
```

דוגמאות:
- `[docs] Add Phi-4 inference tutorial`
- `[code] Fix ONNX Runtime integration example`
- `[translation] Add Japanese translation for intro guides`

## דפוסי פיתוח נפוצים

### עבודה עם מודלי Phi

**טעינת מודלים:**
- דוגמאות משתמשות במסגרות שונות: Transformers, ONNX Runtime, MLX, OpenVINO
- מודלים מורדים בדרך כלל מ-Hugging Face, Azure או GitHub Models
- בדוק תאימות המודל עם החומרה שלך (CPU, GPU, NPU)

**דפוסי הסקה:**
- יצירת טקסט: רוב הדוגמאות משתמשות בגרסאות chat/instruct
- חזותי: Phi-3-vision ו-Phi-4-multimodal להבנת תמונות
- אודיו: Phi-4-multimodal תומך בקלטי אודיו
- הסקה: גרסאות Phi-4-reasoning למשימות הסקה מתקדמות

### הערות ספציפיות לפלטפורמה

**Azure AI Foundry:**
- דורש מנוי Azure ומפתחות API
- ראה `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- זמין חינם לשימוש ניסיון
- ראה `/md/02.QuickStart/GitHubModel_QuickStart.md`

**הסקה מקומית:**
- ONNX Runtime: הסקה חוצת פלטפורמות ואופטימלית
- Ollama: ניהול מודלים מקומי קל (מוגדר מראש במיכל הפיתוח)
- Apple MLX: מותאם ל-Apple Silicon

## פתרון בעיות

### בעיות נפוצות

**בעיות זיכרון:**
- מודלי Phi דורשים זיכרון RAM משמעותי (במיוחד גרסאות חזותיות/מולטימודליות)
- השתמש במודלים מכומתים לסביבות עם משאבים מוגבלים
- ראה `/md/01.Introduction/04/QuantifyingPhi.md`

**קונפליקטים בתלויות:**
- לדוגמאות Python עשויות להיות דרישות גרסה ספציפיות
- השתמש בסביבות וירטואליות לכל דוגמה
- בדוק קבצי `requirements.txt` פרטניים

**כישלונות הורדת מודלים:**
- מודלים גדולים עשויים להיכשל בחיבור איטי
- שקול להשתמש בסביבות ענן (Codespaces, Azure)
- בדוק מטמון Hugging Face: `~/.cache/huggingface/`

**בעיות בפרויקטים .NET:**
- וודא ש-.NET 8.0 SDK מותקן
- השתמש ב-`dotnet restore` לפני בנייה
- חלק מהפרויקטים כוללים תצורות ספציפיות ל-CUDA (Debug_Cuda)

**דוגמאות JavaScript/Web:**
- השתמש ב-Node.js 18+ לתאימות
- נקה `node_modules` והתקן מחדש אם יש בעיות
- בדוק את קונסולת הדפדפן לבעיות תאימות WebGPU

### קבלת עזרה

- **Discord:** הצטרף לקהילת Azure AI Foundry ב-Discord
- **GitHub Issues:** דווח על באגים ובעיות במאגר
- **GitHub Discussions:** שאל שאלות ושתף ידע

## הקשר נוסף

### AI אחראי

כל שימוש במודלי Phi צריך לעקוב אחר עקרונות ה-AI האחראי של Microsoft:
- הוגנות, אמינות, בטיחות
- פרטיות ואבטחה  
- הכללה, שקיפות, אחריות
- השתמש ב-Azure AI Content Safety לאפליקציות ייצור
- ראה `/md/01.Introduction/01/01.AISafety.md`

### תרגומים

- תמיכה ב-50+ שפות באמצעות GitHub Action אוטומטי
- תרגומים בתיקיית `/translations/`
- מתוחזק על ידי זרימת עבודה co-op-translator
- אין לערוך ידנית קבצים מתורגמים (נוצרים אוטומטית)

### תרומה

- עקוב אחר ההנחיות ב-`CONTRIBUTING.md`
- הסכם ל-Contributor License Agreement (CLA)
- עמוד בקוד ההתנהגות של Microsoft Open Source
- שמור על אבטחה ואישורים מחוץ למחויבות

### תמיכה רב-שפתית

זהו מאגר רב-שפתי עם דוגמאות ב:
- **Python** - זרימות עבודה ML/AI, מחברות Jupyter, כיוונון עדין
- **C#/.NET** - אפליקציות ארגוניות, אינטגרציה עם ONNX Runtime
- **JavaScript** - AI מבוסס אינטרנט, הסקה בדפדפן עם WebGPU

בחר את השפה המתאימה ביותר למקרה השימוש שלך וליעד הפריסה.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו אחראים לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.