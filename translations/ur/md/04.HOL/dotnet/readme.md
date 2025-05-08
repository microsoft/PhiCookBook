<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-07T13:09:42+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "ur"
}
-->
﻿## C# استعمال کرتے ہوئے Phi لیبز میں خوش آمدید

.NET ماحول میں Phi ماڈلز کے مختلف طاقتور ورژنز کو انٹیگریٹ کرنے کے طریقے دکھانے کے لیے کئی لیبز کا انتخاب موجود ہے۔

## پیشگی ضروریات

نمونہ چلانے سے پہلے، یقینی بنائیں کہ آپ کے پاس درج ذیل انسٹال ہیں:

**.NET 9:** یقینی بنائیں کہ آپ کے کمپیوٹر پر [تازہ ترین .NET ورژن](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) انسٹال ہے۔

**(اختیاری) Visual Studio یا Visual Studio Code:** آپ کو ایک ایسا IDE یا کوڈ ایڈیٹر چاہیے جو .NET پروجیکٹس چلا سکے۔ [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) یا [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) کی سفارش کی جاتی ہے۔

**git کا استعمال کرتے ہوئے** مقامی طور پر Phi-3، Phi3.5 یا Phi-4 ورژنز میں سے کسی ایک کو [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) سے کلون کریں۔

**Phi-4 ONNX ماڈلز** اپنے لوکل کمپیوٹر پر ڈاؤن لوڈ کریں:

### ماڈلز کو محفوظ کرنے کے لیے فولڈر میں جائیں

```bash
cd c:\phi\models
```

### lfs کی سپورٹ شامل کریں

```bash
git lfs install 
```

### Phi-4 mini instruct ماڈل اور Phi-4 multi modal ماڈل کو کلون اور ڈاؤن لوڈ کریں

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX ماڈلز** اپنے لوکل کمپیوٹر پر ڈاؤن لوڈ کریں:

### Phi-3 mini 4K instruct ماڈل اور Phi-3 vision 128K ماڈل کو کلون اور ڈاؤن لوڈ کریں

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**اہم:** موجودہ ڈیموز ماڈل کے ONNX ورژنز استعمال کرنے کے لیے ڈیزائن کیے گئے ہیں۔ پچھلے مراحل درج ذیل ماڈلز کو کلون کرتے ہیں۔

## لیبز کے بارے میں

مین سلوشن میں کئی سیمپل لیبز شامل ہیں جو C# استعمال کرتے ہوئے Phi ماڈلز کی صلاحیتوں کو ظاہر کرتی ہیں۔

| پروجیکٹ | ماڈل | تفصیل |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 یا Phi-3.5 | سیمپل کنسول چیٹ جو صارف کو سوالات پوچھنے کی اجازت دیتا ہے۔ پروجیکٹ ایک لوکل ONNX Phi-3 ماڈل کو `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime` کے ذریعے لوڈ کرتا ہے۔

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. پروجیکٹ کو کمانڈ کے ساتھ چلائیں

    ```bash
    dotnet run
    ```

1. سیمپل پروجیکٹ صارف سے ان پٹ مانگتا ہے اور لوکل موڈ استعمال کرتے ہوئے جواب دیتا ہے۔

   چلنے والا ڈیمو اس جیسا ہے:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**دستخطی دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم نوٹ کریں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔