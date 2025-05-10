<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-05-09T10:53:27+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "bn"
}
-->
# **iOS-এ Inference Phi-3**

Phi-3-mini হলো Microsoft-এর একটি নতুন মডেল সিরিজ যা এজ ডিভাইস এবং IoT ডিভাইসে Large Language Models (LLMs) ডিপ্লয়মেন্ট সম্ভব করে। Phi-3-mini iOS, Android এবং Edge Device ডিপ্লয়মেন্টের জন্য উপলব্ধ, যা BYOD পরিবেশে জেনারেটিভ AI ডিপ্লয় করতে দেয়। নিচের উদাহরণটি দেখায় কিভাবে iOS-এ Phi-3-mini ডিপ্লয় করবেন।

## **1. প্রস্তুতি**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 বা তার উপরে)
- **d.** Python 3.10+ ইনস্টল করুন (Conda ব্যবহার করার পরামর্শ দেওয়া হয়)
- **e.** Python লাইব্রেরি ইনস্টল করুন: `python-flatbuffers`
- **f.** CMake ইনস্টল করুন

### Semantic Kernel এবং Inference

Semantic Kernel একটি অ্যাপ্লিকেশন ফ্রেমওয়ার্ক যা Azure OpenAI Service, OpenAI মডেল এবং এমনকি লোকাল মডেলের সাথে সামঞ্জস্যপূর্ণ অ্যাপ্লিকেশন তৈরি করতে দেয়। Semantic Kernel এর মাধ্যমে লোকাল সার্ভিস অ্যাক্সেস করলে আপনার নিজস্ব Phi-3-mini মডেল সার্ভারের সাথে সহজ ইন্টিগ্রেশন সম্ভব হয়।

### Ollama বা LlamaEdge দিয়ে Quantized মডেল কল করা

অনেক ব্যবহারকারী স্থানীয়ভাবে মডেল চালানোর জন্য quantized মডেল ব্যবহার করতে পছন্দ করেন। [Ollama](https://ollama.com) এবং [LlamaEdge](https://llamaedge.com) ব্যবহারকারীদের বিভিন্ন quantized মডেল কল করার সুযোগ দেয়:

#### **Ollama**

আপনি সরাসরি `ollama run phi3` চালাতে পারেন বা অফলাইন কনফিগার করতে পারেন। আপনার `gguf` ফাইলের পাথসহ একটি Modelfile তৈরি করুন। Phi-3-mini quantized মডেল চালানোর নমুনা কোড:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

যদি আপনি একই সময়ে ক্লাউড এবং এজ ডিভাইসে `gguf` ব্যবহার করতে চান, তাহলে LlamaEdge একটি ভালো অপশন।

## **2. iOS-এর জন্য ONNX Runtime কম্পাইল করা**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **দ্রষ্টব্য**

- **a.** কম্পাইল করার আগে নিশ্চিত করুন Xcode সঠিকভাবে কনফিগার করা আছে এবং টার্মিনালে এটি অ্যাকটিভ ডেভেলপার ডিরেক্টরি হিসেবে সেট করা হয়েছে:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime বিভিন্ন প্ল্যাটফর্মের জন্য কম্পাইল করতে হয়। iOS-এর জন্য আপনি `arm64` or `x86_64` কম্পাইল করতে পারেন।

- **c.** কম্পাইলেশনের জন্য সর্বশেষ iOS SDK ব্যবহার করার পরামর্শ দেওয়া হয়। তবে, পূর্ববর্তী SDK-র সাথে সামঞ্জস্য রাখতে চাইলে পুরানো ভার্সনও ব্যবহার করতে পারেন।

## **3. iOS-এর জন্য ONNX Runtime দিয়ে Generative AI কম্পাইল করা**

> **Note:** ONNX Runtime দিয়ে Generative AI এখনও প্রিভিউ পর্যায়ে রয়েছে, তাই সম্ভাব্য পরিবর্তনের কথা মাথায় রাখুন।

```bash

git clone https://github.com/microsoft/onnxruntime-genai
 
cd onnxruntime-genai
 
mkdir ort
 
cd ort
 
mkdir include
 
mkdir lib
 
cd ../
 
cp ../onnxruntime/include/onnxruntime/core/session/onnxruntime_c_api.h ort/include
 
cp ../onnxruntime/build_ios/Release/Release-iphoneos/libonnxruntime*.dylib* ort/lib
 
export OPENCV_SKIP_XCODEBUILD_FORCE_TRYCOMPILE_DEBUG=1
 
python3 build.py --parallel --build_dir ./build_ios --ios --ios_sysroot iphoneos --ios_arch arm64 --ios_deployment_target 17.5 --cmake_generator Xcode --cmake_extra_defines CMAKE_XCODE_ATTRIBUTE_CODE_SIGNING_ALLOWED=NO

```

## **4. Xcode-এ একটি App অ্যাপ্লিকেশন তৈরি করা**

আমি App ডেভেলপমেন্টের জন্য Objective-C বেছে নিয়েছি, কারণ ONNX Runtime C++ API দিয়ে Generative AI ব্যবহারে Objective-C বেশি সামঞ্জস্যপূর্ণ। অবশ্যই, Swift ব্রিজিং এর মাধ্যমে সম্পর্কিত কলও সম্পন্ন করতে পারেন।

![xcode](../../../../../translated_images/xcode.6c67033ca85b703e80cc51ecaa681fbcb6ac63cc0c256705ac97bc9ca039c235.bn.png)

## **5. ONNX quantized INT4 মডেল App অ্যাপ্লিকেশন প্রকল্পে কপি করা**

আমাদের ONNX ফরম্যাটের INT4 quantization মডেল ইম্পোর্ট করতে হবে, যা প্রথমে ডাউনলোড করতে হবে।

![hf](../../../../../translated_images/hf.b99941885c6561bb3bcc0155d409e713db6d47b4252fb6991a08ffeefc0170ec.bn.png)

ডাউনলোডের পর, Xcode-র প্রকল্পের Resources ডিরেক্টরিতে এটি যোগ করতে হবে।

![model](../../../../../translated_images/model.f0cb932ac2c7648211fbe5341ee1aa42b77cb7f956b6d9b084afb8fbf52927c7.bn.png)

## **6. ViewControllers-এ C++ API যোগ করা**

> **দ্রষ্টব্য:**

- **a.** প্রোজেক্টে সংশ্লিষ্ট C++ হেডার ফাইলগুলো যোগ করুন।

  ![Header File](../../../../../translated_images/head.2504a93b0be166afde6729fb193ebd14c5acb00a0bb6de1939b8a175b1f630fb.bn.png)

- **b.** Objective-C++ সাপোর্ট সক্ষম করতে `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../../translated_images/lib.86e12a925eb07e4e71a1466fa4f3ad27097e08505d25d34e98c33005d69b6f23.bn.png)

- **c.** Use the C Samples code for testing. You can also add additional features like ChatUI for more functionality.

- **d.** Since you need to use C++ in your project, rename `ViewController.m` to `ViewController.mm` অন্তর্ভুক্ত করুন।

```objc

    NSString *llmPath = [[NSBundle mainBundle] resourcePath];
    char const *modelPath = llmPath.cString;

    auto model =  OgaModel::Create(modelPath);

    auto tokenizer = OgaTokenizer::Create(*model);

    const char* prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>Can you introduce yourself?<|end|><|assistant|>";

    auto sequences = OgaSequences::Create();
    tokenizer->Encode(prompt, *sequences);

    auto params = OgaGeneratorParams::Create(*model);
    params->SetSearchOption("max_length", 100);
    params->SetInputSequences(*sequences);

    auto output_sequences = model->Generate(*params);
    const auto output_sequence_length = output_sequences->SequenceCount(0);
    const auto* output_sequence_data = output_sequences->SequenceData(0);
    auto out_string = tokenizer->Decode(output_sequence_data, output_sequence_length);
    
    auto tmp = out_string;

```

## **7. অ্যাপ্লিকেশন চালানো**

সেটআপ সম্পন্ন হলে, Phi-3-mini মডেল ইনফারেন্সের ফলাফল দেখতে অ্যাপ্লিকেশন চালাতে পারেন।

![Running Result](../../../../../translated_images/result.7ebd1fe614f809d776c46475275ec72e4ab898c4ec53ae62b29315c064ca6839.bn.jpg)

অধিক নমুনা কোড এবং বিস্তারিত নির্দেশনার জন্য, [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios) দেখুন।

**দায়বদ্ধতা প্রত্যাহার**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।