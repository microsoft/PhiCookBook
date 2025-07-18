<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:31:52+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "ur"
}
-->
﻿## C# استعمال کرتے ہوئے Phi لیبز میں خوش آمدید

.NET ماحول میں Phi ماڈلز کے مختلف طاقتور ورژنز کو انٹیگریٹ کرنے کے طریقے دکھانے والی چند لیبز کا انتخاب موجود ہے۔

## ضروریات

نمونہ چلانے سے پہلے، یقینی بنائیں کہ آپ کے پاس درج ذیل انسٹال ہیں:

**.NET 9:** اس بات کو یقینی بنائیں کہ آپ کے کمپیوٹر پر [تازہ ترین .NET ورژن](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) انسٹال ہے۔

**(اختیاری) Visual Studio یا Visual Studio Code:** آپ کو ایسا IDE یا کوڈ ایڈیٹر چاہیے جو .NET پروجیکٹس چلا سکے۔ [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) یا [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) تجویز کیے جاتے ہیں۔

**git استعمال کرتے ہوئے** Hugging Face سے دستیاب Phi-3، Phi3.5 یا Phi-4 ورژنز میں سے کسی ایک کو مقامی طور پر کلون کریں: [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c)۔

**Phi-4 ONNX ماڈلز** اپنے مقامی کمپیوٹر پر ڈاؤن لوڈ کریں:

### ماڈلز کو محفوظ کرنے کے لیے فولڈر پر جائیں

```bash
cd c:\phi\models
```

### lfs کی سپورٹ شامل کریں

```bash
git lfs install 
```

### Phi-4 mini instruct ماڈل اور Phi-4 multi modal ماڈل کلون اور ڈاؤن لوڈ کریں

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX ماڈلز** اپنے مقامی کمپیوٹر پر ڈاؤن لوڈ کریں:

### Phi-3 mini 4K instruct ماڈل اور Phi-3 vision 128K ماڈل کلون اور ڈاؤن لوڈ کریں

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**اہم:** موجودہ ڈیموز ماڈل کے ONNX ورژنز استعمال کرنے کے لیے بنائے گئے ہیں۔ پچھلے مراحل میں درج ذیل ماڈلز کلون کیے گئے ہیں۔

## لیبز کے بارے میں

مین سلوشن میں کئی سیمپل لیبز شامل ہیں جو C# استعمال کرتے ہوئے Phi ماڈلز کی صلاحیتوں کو ظاہر کرتی ہیں۔

| پروجیکٹ | ماڈل | وضاحت |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 یا Phi-3.5 | سیمپل کنسول چیٹ جو صارف کو سوالات پوچھنے کی اجازت دیتی ہے۔ پروجیکٹ `Microsoft.ML.OnnxRuntime` لائبریریز استعمال کرتے ہوئے مقامی ONNX Phi-3 ماڈل لوڈ کرتا ہے۔ |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 یا Phi-3.5 | سیمپل کنسول چیٹ جو صارف کو سوالات پوچھنے کی اجازت دیتی ہے۔ پروجیکٹ `Microsoft.Semantic.Kernel` لائبریریز استعمال کرتے ہوئے مقامی ONNX Phi-3 ماڈل لوڈ کرتا ہے۔ |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 یا Phi-3.5 | یہ ایک سیمپل پروجیکٹ ہے جو مقامی phi3 vision ماڈل استعمال کرکے تصاویر کا تجزیہ کرتا ہے۔ پروجیکٹ `Microsoft.ML.OnnxRuntime` لائبریریز استعمال کرتے ہوئے مقامی ONNX Phi-3 Vision ماڈل لوڈ کرتا ہے۔ |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 یا Phi-3.5 | یہ ایک سیمپل پروجیکٹ ہے جو مقامی phi3 vision ماڈل استعمال کرکے تصاویر کا تجزیہ کرتا ہے۔ پروجیکٹ `Microsoft.ML.OnnxRuntime` لائبریریز استعمال کرتے ہوئے مقامی ONNX Phi-3 Vision ماڈل لوڈ کرتا ہے۔ پروجیکٹ صارف کے ساتھ بات چیت کے لیے مختلف اختیارات کے ساتھ مینو بھی پیش کرتا ہے۔ | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | سیمپل کنسول چیٹ جو صارف کو سوالات پوچھنے کی اجازت دیتی ہے۔ پروجیکٹ `Microsoft.ML.OnnxRuntime` لائبریریز استعمال کرتے ہوئے مقامی ONNX Phi-4 ماڈل لوڈ کرتا ہے۔ |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | سیمپل کنسول چیٹ جو صارف کو سوالات پوچھنے کی اجازت دیتی ہے۔ پروجیکٹ `Semantic Kernel` لائبریریز استعمال کرتے ہوئے مقامی ONNX Phi-4 ماڈل لوڈ کرتا ہے۔ |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | سیمپل کنسول چیٹ جو صارف کو سوالات پوچھنے کی اجازت دیتی ہے۔ پروجیکٹ `Microsoft.ML.OnnxRuntimeGenAI` لائبریریز استعمال کرتے ہوئے مقامی ONNX Phi-4 ماڈل لوڈ کرتا ہے اور `Microsoft.Extensions.AI` سے `IChatClient` کو نافذ کرتا ہے۔ |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | سیمپل کنسول چیٹ جو صارف کو سوالات پوچھنے کی اجازت دیتی ہے۔ چیٹ میں میموری کا نفاذ کیا گیا ہے۔ |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | یہ ایک سیمپل پروجیکٹ ہے جو مقامی Phi-4 ماڈل استعمال کرکے تصاویر کا تجزیہ کرتا ہے اور نتیجہ کنسول میں دکھاتا ہے۔ پروجیکٹ `Microsoft.ML.OnnxRuntime` لائبریریز استعمال کرتے ہوئے مقامی Phi-4-`multimodal-instruct-onnx` ماڈل لوڈ کرتا ہے۔ |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | یہ ایک سیمپل پروجیکٹ ہے جو مقامی Phi-4 ماڈل استعمال کرکے آڈیو فائل کا تجزیہ کرتا ہے، فائل کا ٹرانسکرپٹ تیار کرتا ہے اور نتیجہ کنسول میں دکھاتا ہے۔ پروجیکٹ `Microsoft.ML.OnnxRuntime` لائبریریز استعمال کرتے ہوئے مقامی Phi-4-`multimodal-instruct-onnx` ماڈل لوڈ کرتا ہے۔ |

## پروجیکٹس کیسے چلائیں

پروجیکٹس چلانے کے لیے درج ذیل مراحل پر عمل کریں:

1. ریپوزیٹری کو اپنے مقامی کمپیوٹر پر کلون کریں۔

1. ٹرمینل کھولیں اور مطلوبہ پروجیکٹ کی ڈائریکٹری میں جائیں۔ مثال کے طور پر، `LabsPhi4-Chat-01OnnxRuntime` چلائیں۔

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. درج ذیل کمانڈ سے پروجیکٹ چلائیں

    ```bash
    dotnet run
    ```

1. سیمپل پروجیکٹ صارف سے ان پٹ طلب کرتا ہے اور مقامی ماڈل استعمال کرتے ہوئے جواب دیتا ہے۔

   چل رہا ڈیمو اس طرح کا ہوگا:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔