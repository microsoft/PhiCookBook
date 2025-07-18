<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:39:01+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "he"
}
-->
﻿## ברוכים הבאים למעבדות Phi עם C#

קיימת מבחר של מעבדות שמדגימות כיצד לשלב את הגרסאות החזקות השונות של דגמי Phi בסביבת .NET.

## דרישות מוקדמות

לפני הרצת הדוגמה, ודאו שהתקנתם את הדברים הבאים:

**.NET 9:** ודאו שיש לכם את [הגרסה העדכנית ביותר של .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) מותקנת במחשב שלכם.

**(אופציונלי) Visual Studio או Visual Studio Code:** תזדקקו לסביבת פיתוח או עורך קוד שיכולים להריץ פרויקטים של .NET. מומלץ להשתמש ב-[Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) או [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**שימוש ב-git** - שיבטו מקומית אחת מהגרסאות הזמינות של Phi-3, Phi3.5 או Phi-4 מ-[Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**הורדת דגמי Phi-4 ONNX** למחשב המקומי שלכם:

### נווטו לתיקייה לאחסון הדגמים

```bash
cd c:\phi\models
```

### הוספת תמיכה ב-lfs

```bash
git lfs install 
```

### שיבוט והורדת דגם Phi-4 mini instruct ודגם Phi-4 multi modal

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**הורדת דגמי Phi-3 ONNX** למחשב המקומי שלכם:

### שיבוט והורדת דגם Phi-3 mini 4K instruct ודגם Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**חשוב:** הדגמות הנוכחיות מתוכננות להשתמש בגרסאות ONNX של הדגם. השלבים הקודמים משכפלים את הדגמים הבאים.

## אודות המעבדות

הפתרון הראשי כולל מספר מעבדות לדוגמה שמדגימות את היכולות של דגמי Phi באמצעות C#.

| פרויקט | דגם | תיאור |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 או Phi-3.5 | שיחת קונסולה לדוגמה המאפשרת למשתמש לשאול שאלות. הפרויקט טוען דגם ONNX מקומי של Phi-3 באמצעות ספריות `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 או Phi-3.5 | שיחת קונסולה לדוגמה המאפשרת למשתמש לשאול שאלות. הפרויקט טוען דגם ONNX מקומי של Phi-3 באמצעות ספריות `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 או Phi-3.5 | פרויקט לדוגמה שמשתמש בדגם מקומי של phi3 vision לניתוח תמונות. הפרויקט טוען דגם ONNX מקומי של Phi-3 Vision באמצעות ספריות `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 או Phi-3.5 | פרויקט לדוגמה שמשתמש בדגם מקומי של phi3 vision לניתוח תמונות. הפרויקט טוען דגם ONNX מקומי של Phi-3 Vision באמצעות ספריות `Microsoft.ML.OnnxRuntime`. הפרויקט גם מציג תפריט עם אפשרויות שונות לאינטראקציה עם המשתמש. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | שיחת קונסולה לדוגמה המאפשרת למשתמש לשאול שאלות. הפרויקט טוען דגם ONNX מקומי של Phi-4 באמצעות ספריות `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | שיחת קונסולה לדוגמה המאפשרת למשתמש לשאול שאלות. הפרויקט טוען דגם ONNX מקומי של Phi-4 באמצעות ספריות `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | שיחת קונסולה לדוגמה המאפשרת למשתמש לשאול שאלות. הפרויקט טוען דגם ONNX מקומי של Phi-4 באמצעות ספריות `Microsoft.ML.OnnxRuntimeGenAI` ומממש את `IChatClient` מתוך `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | שיחת קונסולה לדוגמה המאפשרת למשתמש לשאול שאלות. השיחה כוללת זיכרון. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | פרויקט לדוגמה שמשתמש בדגם מקומי של Phi-4 לניתוח תמונות ומציג את התוצאה בקונסולה. הפרויקט טוען דגם מקומי של Phi-4-`multimodal-instruct-onnx` באמצעות ספריות `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | פרויקט לדוגמה שמשתמש בדגם מקומי של Phi-4 לניתוח קובץ שמע, מייצר תמלול של הקובץ ומציג את התוצאה בקונסולה. הפרויקט טוען דגם מקומי של Phi-4-`multimodal-instruct-onnx` באמצעות ספריות `Microsoft.ML.OnnxRuntime`. |

## איך להריץ את הפרויקטים

להרצת הפרויקטים, בצעו את השלבים הבאים:

1. שיבטו את המאגר למחשב המקומי שלכם.

1. פתחו טרמינל ונווטו לפרויקט הרצוי. לדוגמה, נריץ את `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. הריצו את הפרויקט עם הפקודה

    ```bash
    dotnet run
    ```

1. פרויקט הדוגמה יבקש קלט מהמשתמש ויענה באמצעות הדגם המקומי.

   הדגמה רצה דומה לזו:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.