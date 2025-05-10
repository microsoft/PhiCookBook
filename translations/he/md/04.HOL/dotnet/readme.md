<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-09T22:44:50+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "he"
}
-->
﻿## ברוכים הבאים למעבדות Phi עם C#

יש מבחר של מעבדות שמדגימות כיצד לשלב את הגרסאות החזקות השונות של מודלי Phi בסביבת .NET.

## דרישות מוקדמות

לפני הפעלת הדוגמה, ודאו שהתקנתם את הדברים הבאים:

**.NET 9:** ודאו שיש לכם את [הגרסה העדכנית ביותר של .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) מותקנת במחשב שלכם.

**(אופציונלי) Visual Studio או Visual Studio Code:** תזדקקו ל-IDE או עורך קוד שיכול להריץ פרויקטים של .NET. מומלץ להשתמש ב-[Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) או [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**שימוש ב-git**: שיבטו מקומית אחת מהגרסאות הזמינות Phi-3, Phi3.5 או Phi-4 מ-[Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**הורדת מודלי Phi-4 ONNX** למחשב המקומי שלכם:

### נווטו לתיקייה לאחסון המודלים

```bash
cd c:\phi\models
```

### הוספת תמיכה ל-lfs

```bash
git lfs install 
```

### שיבט והורדת מודל Phi-4 mini instruct והמודל Phi-4 multi modal

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**הורדת מודלי Phi-3 ONNX** למחשב המקומי שלכם:

### שיבט והורדת מודל Phi-3 mini 4K instruct ומודל Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**חשוב:** הדגמות הנוכחיות מתוכננות לשימוש בגרסאות ONNX של המודל. השלבים הקודמים משיבים את המודלים הבאים.

## אודות המעבדות

הפתרון הראשי כולל מספר מעבדות דוגמה שמדגימות את היכולות של מודלי Phi באמצעות C#.

| פרויקט | מודל | תיאור |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 או Phi-3.5 | דוגמת שיחה בקונסולה שמאפשרת למשתמש לשאול שאלות. הפרויקט טוען מודל Phi-3 מקומי בפורמט ONNX באמצעות `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Sample console chat that allows the user to ask questions. The chat implements memory. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. הריצו את הפרויקט עם הפקודה

    ```bash
    dotnet run
    ```

1. פרויקט הדוגמה מבקש קלט מהמשתמש ומשיב באמצעות המודל המקומי.

   הדמו הרץ דומה לזה:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו צריך להיחשב כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא אחראים לכל אי הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.