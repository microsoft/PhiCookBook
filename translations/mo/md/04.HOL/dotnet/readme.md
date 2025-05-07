<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-07T13:10:12+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "mo"
}
-->
﻿## ברוכים הבאים למעבדות Phi עם C#

יש מבחר מעבדות שמדגימות כיצד לשלב את הגרסאות השונות והעוצמתיות של דגמי Phi בסביבת .NET.

## דרישות מוקדמות

לפני הרצת הדוגמה, ודא שיש ברשותך את הדברים הבאים מותקנים:

**.NET 9:** ודא שהתקנת את [הגרסה העדכנית ביותר של .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) במחשב שלך.

**(אופציונלי) Visual Studio או Visual Studio Code:** תזדקק ל-IDE או עורך קוד שיכול להריץ פרויקטים של .NET. מומלץ להשתמש ב-[Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) או [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo).

**שימוש ב-git** – שיכפל באופן מקומי אחת מגרסאות Phi-3, Phi3.5 או Phi-4 הזמינות מ-[Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**הורדת דגמי Phi-4 ONNX** למחשב המקומי שלך:

### נווט לתיקייה לאחסון הדגמים

```bash
cd c:\phi\models
```

### הוסף תמיכה ב-lfs

```bash
git lfs install 
```

### שיכפל והורד את דגם Phi-4 mini instruct ואת דגם Phi-4 multi modal

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**הורדת דגמי Phi-3 ONNX** למחשב המקומי שלך:

### שיכפל והורד את דגם Phi-3 mini 4K instruct ואת דגם Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**חשוב:** הדגמות הנוכחיות מתוכננות להשתמש בגרסאות ONNX של הדגם. השלבים הקודמים משכפלים את הדגמים הבאים.

## אודות המעבדות

הפתרון הראשי כולל מספר מעבדות לדוגמה שמדגימות את היכולות של דגמי Phi באמצעות C#.

| פרויקט | דגם | תיאור |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 או Phi-3.5 | דוגמת שיחה בקונסולה שמאפשרת למשתמש לשאול שאלות. הפרויקט טוען דגם ONNX מקומי של Phi-3 באמצעות `Microsoft.ML.OnnxRuntime` libraries. |
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

1. הרץ את הפרויקט עם הפקודה

    ```bash
    dotnet run
    ```

1. דוגמת הפרויקט מבקשת קלט מהמשתמש ומשיבה באמצעות המודל המקומי.

   הדמו הרץ דומה לזה:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Disclaimer**:  
Dis document haz been translated usin AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, pleez be aware dat automated translations may contain errors or inaccuracies. Da original document in its native language should be considered da authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from da use of dis translation.