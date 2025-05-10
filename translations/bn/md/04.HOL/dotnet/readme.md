<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-09T22:42:29+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "bn"
}
-->
﻿## C# ব্যবহার করে Phi ল্যাবগুলিতে স্বাগতম

একটি নির্বাচিত ল্যাব রয়েছে যা দেখায় কীভাবে শক্তিশালী বিভিন্ন Phi মডেল .NET পরিবেশে একত্রিত করা যায়।

## প্রয়োজনীয়তা

স্যাম্পল চালানোর আগে নিশ্চিত করুন যে আপনার কাছে নিম্নলিখিতগুলি ইনস্টল করা আছে:

**.NET 9:** নিশ্চিত করুন যে আপনার মেশিনে [সর্বশেষ .NET সংস্করণ](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) ইনস্টল করা আছে।

**(ঐচ্ছিক) Visual Studio বা Visual Studio Code:** আপনাকে এমন একটি IDE বা কোড এডিটর প্রয়োজন যা .NET প্রকল্প চালাতে সক্ষম। [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) অথবা [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) ব্যবহার করার পরামর্শ দেওয়া হয়।

**git ব্যবহার করে** স্থানীয়ভাবে Phi-3, Phi3.5 বা Phi-4 এর যেকোনো সংস্করণ [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) থেকে ক্লোন করুন।

**Phi-4 ONNX মডেলগুলি** আপনার স্থানীয় মেশিনে ডাউনলোড করুন:

### মডেল সংরক্ষণের জন্য ফোল্ডারে যান

```bash
cd c:\phi\models
```

### lfs সমর্থন যোগ করুন

```bash
git lfs install 
```

### Phi-4 mini instruct মডেল এবং Phi-4 multi modal মডেল ক্লোন ও ডাউনলোড করুন

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX মডেলগুলি** আপনার স্থানীয় মেশিনে ডাউনলোড করুন:

### Phi-3 mini 4K instruct মডেল এবং Phi-3 vision 128K মডেল ক্লোন ও ডাউনলোড করুন

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**গুরুত্বপূর্ণ:** বর্তমান ডেমোগুলো মডেলের ONNX সংস্করণ ব্যবহার করার জন্য ডিজাইন করা হয়েছে। পূর্বের ধাপগুলো নিম্নলিখিত মডেলগুলো ক্লোন করে।

## ল্যাব সম্পর্কে

মূল সলিউশনে বেশ কয়েকটি স্যাম্পল ল্যাব রয়েছে যা C# ব্যবহার করে Phi মডেলের সক্ষমতা প্রদর্শন করে।

| প্রকল্প | মডেল | বিবরণ |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 অথবা Phi-3.5 | একটি স্যাম্পল কনসোল চ্যাট যা ব্যবহারকারীকে প্রশ্ন করতে দেয়। প্রকল্পটি একটি স্থানীয় ONNX Phi-3 মডেল লোড করে `Microsoft.ML.OnnxRuntime` libraries. |
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

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime` ব্যবহার করে।

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. কমান্ড দিয়ে প্রকল্প চালান

    ```bash
    dotnet run
    ```

1. স্যাম্পল প্রকল্পটি ব্যবহারকারীর ইনপুট চায় এবং স্থানীয় মডেল ব্যবহার করে উত্তর দেয়।

   চলমান ডেমোটি এরকম দেখতে হবে:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বদেশী ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসাবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানুষের অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহার থেকে উদ্ভূত কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।