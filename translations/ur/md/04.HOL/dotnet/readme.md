<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0e3a4453db505856d5d991285dd6001",
  "translation_date": "2025-04-03T08:30:34+00:00",
  "source_file": "md\\04.HOL\\dotnet\\readme.md",
  "language_code": "ur"
}
-->
## Phi لیبز میں خوش آمدید C# استعمال کرتے ہوئے

یہاں مختلف لیبز کا انتخاب موجود ہے جو یہ دکھاتے ہیں کہ کس طرح طاقتور Phi ماڈلز کے مختلف ورژنز کو .NET ماحول میں ضم کیا جا سکتا ہے۔

## ضروریات

نمونے کو چلانے سے پہلے، یقینی بنائیں کہ آپ کے پاس درج ذیل چیزیں موجود ہیں:

**.NET 9:** اپنے کمپیوٹر پر [.NET کا تازہ ترین ورژن](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) انسٹال کریں۔

**(اختیاری) Visual Studio یا Visual Studio Code:** آپ کو ایک IDE یا کوڈ ایڈیٹر کی ضرورت ہوگی جو .NET پروجیکٹس چلانے کی صلاحیت رکھتا ہو۔ [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) یا [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) تجویز کیے جاتے ہیں۔

**git کا استعمال:** Phi-3، Phi3.5 یا Phi-4 ورژنز میں سے کسی ایک کو [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) سے لوکل طور پر کلون کریں۔

**Phi-4 ONNX ماڈلز** کو اپنی مشین پر ڈاؤن لوڈ کریں:

### ماڈلز کو اسٹور کرنے کے فولڈر پر جائیں

```bash
cd c:\phi\models
```

### lfs کے لیے سپورٹ شامل کریں

```bash
git lfs install 
```

### Phi-4 mini instruct ماڈل اور Phi-4 multi modal ماڈل کو کلون اور ڈاؤن لوڈ کریں

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX ماڈلز** کو اپنی مشین پر ڈاؤن لوڈ کریں:

### Phi-3 mini 4K instruct ماڈل اور Phi-3 vision 128K ماڈل کو کلون اور ڈاؤن لوڈ کریں

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**اہم:** موجودہ ڈیموز ONNX ورژن ماڈلز استعمال کرنے کے لیے ڈیزائن کیے گئے ہیں۔ اوپر دیے گئے مراحل درج ذیل ماڈلز کو کلون کرتے ہیں۔

## لیبز کے بارے میں

مرکزی سلوشن میں کئی نمونہ لیبز شامل ہیں جو C# کے ذریعے Phi ماڈلز کی صلاحیتوں کو ظاہر کرتے ہیں۔

| پروجیکٹ | ماڈل | تفصیل |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 یا Phi-3.5 | ایک نمونہ کنسول چیٹ جو صارف کو سوالات پوچھنے کی اجازت دیتا ہے۔ پروجیکٹ لوکل ONNX Phi-3 ماڈل کو لوڈ کرتا ہے `Microsoft.ML.OnnxRuntime` libraries. |
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

1. پروجیکٹ کو درج ذیل کمانڈ کے ساتھ چلائیں:

    ```bash
    dotnet run
    ```

1. نمونہ پروجیکٹ صارف سے ان پٹ طلب کرتا ہے اور لوکل ماڈل کے ذریعے جواب دیتا ہے۔

   چلنے والا ڈیمو اس طرح کا ہوگا:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستگی ہو سکتی ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔