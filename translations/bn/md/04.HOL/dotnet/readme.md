## C# ব্যবহার করে Phi ল্যাবসমূহে স্বাগতম

কিছু ল্যাব রয়েছে যা দেখায় কিভাবে শক্তিশালী Phi মডেলের বিভিন্ন সংস্করণ .NET পরিবেশে একত্রিত করা যায়।

## পূর্বশর্তসমূহ

নমুনাটি চালানোর আগে নিশ্চিত করুন আপনার কাছে নিম্নলিখিতগুলি ইনস্টল করা আছে:

**.NET 9:** নিশ্চিত করুন আপনার মেশিনে [সর্বশেষ .NET সংস্করণ](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) ইনস্টল করা আছে।

**(ঐচ্ছিক) Visual Studio বা Visual Studio Code:** আপনাকে এমন একটি IDE বা কোড এডিটর প্রয়োজন যা .NET প্রকল্প চালাতে সক্ষম। [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) অথবা [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) সুপারিশ করা হয়।

**git ব্যবহার করে** স্থানীয়ভাবে Phi-3, Phi3.5 বা Phi-4 সংস্করণগুলোর যেকোনো একটি [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c) থেকে ক্লোন করুন।

**Phi-4 ONNX মডেলগুলি** আপনার স্থানীয় মেশিনে ডাউনলোড করুন:

### মডেল সংরক্ষণের জন্য ফোল্ডারে যান

```bash
cd c:\phi\models
```

### lfs এর জন্য সাপোর্ট যোগ করুন

```bash
git lfs install 
```

### Phi-4 মিনি ইনস্ট্রাক্ট মডেল এবং Phi-4 মাল্টি মোডাল মডেল ক্লোন ও ডাউনলোড করুন

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX মডেলগুলি** আপনার স্থানীয় মেশিনে ডাউনলোড করুন:

### Phi-3 মিনি 4K ইনস্ট্রাক্ট মডেল এবং Phi-3 ভিশন 128K মডেল ক্লোন ও ডাউনলোড করুন

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**গুরুত্বপূর্ণ:** বর্তমান ডেমোগুলো মডেলের ONNX সংস্করণ ব্যবহার করার জন্য ডিজাইন করা হয়েছে। পূর্ববর্তী ধাপগুলো নিম্নলিখিত মডেলগুলো ক্লোন করে।

## ল্যাবসমূহ সম্পর্কে

মূল সলিউশনে বেশ কিছু নমুনা ল্যাব রয়েছে যা C# ব্যবহার করে Phi মডেলের ক্ষমতাগুলো প্রদর্শন করে।

| প্রকল্প | মডেল | বর্ণনা |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 বা Phi-3.5 | একটি নমুনা কনসোল চ্যাট যা ব্যবহারকারীকে প্রশ্ন করার সুযোগ দেয়। প্রকল্পটি `Microsoft.ML.OnnxRuntime` লাইব্রেরি ব্যবহার করে স্থানীয় ONNX Phi-3 মডেল লোড করে। |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 বা Phi-3.5 | একটি নমুনা কনসোল চ্যাট যা ব্যবহারকারীকে প্রশ্ন করার সুযোগ দেয়। প্রকল্পটি `Microsoft.Semantic.Kernel` লাইব্রেরি ব্যবহার করে স্থানীয় ONNX Phi-3 মডেল লোড করে। |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 বা Phi-3.5 | এটি একটি নমুনা প্রকল্প যা স্থানীয় phi3 ভিশন মডেল ব্যবহার করে ছবি বিশ্লেষণ করে। প্রকল্পটি `Microsoft.ML.OnnxRuntime` লাইব্রেরি ব্যবহার করে স্থানীয় ONNX Phi-3 ভিশন মডেল লোড করে। |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 বা Phi-3.5 | এটি একটি নমুনা প্রকল্প যা স্থানীয় phi3 ভিশন মডেল ব্যবহার করে ছবি বিশ্লেষণ করে। প্রকল্পটি `Microsoft.ML.OnnxRuntime` লাইব্রেরি ব্যবহার করে স্থানীয় ONNX Phi-3 ভিশন মডেল লোড করে। প্রকল্পটি ব্যবহারকারীর সাথে ইন্টারঅ্যাক্ট করার জন্য বিভিন্ন অপশনসহ একটি মেনুও প্রদান করে। | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | একটি নমুনা কনসোল চ্যাট যা ব্যবহারকারীকে প্রশ্ন করার সুযোগ দেয়। প্রকল্পটি `Microsoft.ML.OnnxRuntime` লাইব্রেরি ব্যবহার করে স্থানীয় ONNX Phi-4 মডেল লোড করে। |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | একটি নমুনা কনসোল চ্যাট যা ব্যবহারকারীকে প্রশ্ন করার সুযোগ দেয়। প্রকল্পটি `Semantic Kernel` লাইব্রেরি ব্যবহার করে স্থানীয় ONNX Phi-4 মডেল লোড করে। |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | একটি নমুনা কনসোল চ্যাট যা ব্যবহারকারীকে প্রশ্ন করার সুযোগ দেয়। প্রকল্পটি `Microsoft.ML.OnnxRuntimeGenAI` লাইব্রেরি ব্যবহার করে স্থানীয় ONNX Phi-4 মডেল লোড করে এবং `Microsoft.Extensions.AI` থেকে `IChatClient` ইমপ্লিমেন্ট করে। |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | একটি নমুনা কনসোল চ্যাট যা ব্যবহারকারীকে প্রশ্ন করার সুযোগ দেয়। চ্যাটে মেমোরি ইমপ্লিমেন্ট করা হয়েছে। |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | এটি একটি নমুনা প্রকল্প যা স্থানীয় Phi-4 মডেল ব্যবহার করে ছবি বিশ্লেষণ করে এবং ফলাফল কনসোলে প্রদর্শন করে। প্রকল্পটি `Microsoft.ML.OnnxRuntime` লাইব্রেরি ব্যবহার করে স্থানীয় Phi-4-`multimodal-instruct-onnx` মডেল লোড করে। |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | এটি একটি নমুনা প্রকল্প যা স্থানীয় Phi-4 মডেল ব্যবহার করে একটি অডিও ফাইল বিশ্লেষণ করে, ফাইলের ট্রান্সক্রিপ্ট তৈরি করে এবং ফলাফল কনসোলে প্রদর্শন করে। প্রকল্পটি `Microsoft.ML.OnnxRuntime` লাইব্রেরি ব্যবহার করে স্থানীয় Phi-4-`multimodal-instruct-onnx` মডেল লোড করে। |

## প্রকল্পগুলো কীভাবে চালাবেন

প্রকল্পগুলো চালানোর জন্য নিচের ধাপগুলো অনুসরণ করুন:

1. রিপোজিটরিটি আপনার স্থানীয় মেশিনে ক্লোন করুন।

1. একটি টার্মিনাল খুলুন এবং পছন্দসই প্রকল্পের ফোল্ডারে যান। উদাহরণস্বরূপ, `LabsPhi4-Chat-01OnnxRuntime` চালানো যাক।

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. নিচের কমান্ড দিয়ে প্রকল্পটি চালান

    ```bash
    dotnet run
    ```

1. নমুনা প্রকল্পটি ব্যবহারকারীর ইনপুট চায় এবং স্থানীয় মডেল ব্যবহার করে উত্তর দেয়।

   চলমান ডেমোটি এরকম দেখতে হবে:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।