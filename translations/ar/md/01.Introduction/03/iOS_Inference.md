<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-03-27T07:14:20+00:00",
  "source_file": "md\\01.Introduction\\03\\iOS_Inference.md",
  "language_code": "ar"
}
-->
# **استنتاج Phi-3 في iOS**

Phi-3-mini هي سلسلة جديدة من النماذج التي تقدمها مايكروسوفت، تتيح نشر نماذج اللغة الكبيرة (LLMs) على الأجهزة الطرفية وأجهزة إنترنت الأشياء. تتوفر Phi-3-mini لنشرها على iOS، Android، والأجهزة الطرفية، مما يتيح استخدام الذكاء الاصطناعي التوليدي في بيئات الأجهزة الشخصية. المثال التالي يوضح كيفية نشر Phi-3-mini على iOS.

## **1. التحضير**

- **أ.** macOS 14+  
- **ب.** Xcode 15+  
- **ج.** iOS SDK 17.x (iPhone 14 A16 أو أعلى)  
- **د.** تثبيت Python 3.10+ (يوصى باستخدام Conda)  
- **هـ.** تثبيت مكتبة Python: `python-flatbuffers`  
- **و.** تثبيت CMake  

### إطار عمل Semantic Kernel والاستنتاج

Semantic Kernel هو إطار عمل للتطبيقات يتيح لك إنشاء تطبيقات متوافقة مع خدمة Azure OpenAI، نماذج OpenAI، وحتى النماذج المحلية. الوصول إلى الخدمات المحلية من خلال Semantic Kernel يسهل التكامل مع خادم النموذج Phi-3-mini المستضاف ذاتيًا.

### استدعاء النماذج المضغوطة باستخدام Ollama أو LlamaEdge

يفضل العديد من المستخدمين تشغيل النماذج المضغوطة محليًا. [Ollama](https://ollama.com) و [LlamaEdge](https://llamaedge.com) يتيحان للمستخدمين استدعاء نماذج مضغوطة مختلفة:

#### **Ollama**

يمكنك تشغيل `ollama run phi3` مباشرة أو تكوينه بدون اتصال. قم بإنشاء ملف Modelfile مع مسار ملف `gguf` الخاص بك. مثال على كود تشغيل نموذج Phi-3-mini المضغوط:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

إذا كنت ترغب في استخدام `gguf` على كل من السحابة والأجهزة الطرفية في نفس الوقت، فإن LlamaEdge خيار رائع.

## **2. تجميع ONNX Runtime لنظام iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **ملاحظة**

- **أ.** قبل التجميع، تأكد من أن Xcode قد تم تكوينه بشكل صحيح واضبطه كدليل المطور النشط في الطرفية:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **ب.** يحتاج ONNX Runtime إلى التجميع لمنصات مختلفة. بالنسبة لنظام iOS، يمكنك التجميع لـ `arm64` or `x86_64`.

- **ج.** يُوصى باستخدام أحدث إصدار من iOS SDK للتجميع. ومع ذلك، يمكنك أيضًا استخدام إصدار أقدم إذا كنت بحاجة إلى التوافق مع SDKs السابقة.

## **3. تجميع الذكاء الاصطناعي التوليدي باستخدام ONNX Runtime لنظام iOS**

> **ملاحظة:** لأن الذكاء الاصطناعي التوليدي باستخدام ONNX Runtime ما زال في المعاينة، يرجى الانتباه إلى أي تغييرات محتملة.

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

## **4. إنشاء تطبيق App في Xcode**

اخترت Objective-C كطريقة لتطوير التطبيق، لأن استخدام الذكاء الاصطناعي التوليدي مع واجهة برمجة تطبيقات C++ الخاصة بـ ONNX Runtime يتوافق بشكل أفضل مع Objective-C. بالطبع، يمكنك أيضًا إكمال الاستدعاءات ذات الصلة من خلال Swift bridging.

![xcode](../../../../../translated_images/xcode.6c67033ca85b703e80cc51ecaa681fbcb6ac63cc0c256705ac97bc9ca039c235.ar.png)

## **5. نسخ نموذج ONNX المضغوط INT4 إلى مشروع تطبيق App**

نحتاج إلى استيراد نموذج INT4 المضغوط بتنسيق ONNX، والذي يجب تنزيله أولاً.

![hf](../../../../../translated_images/hf.b99941885c6561bb3bcc0155d409e713db6d47b4252fb6991a08ffeefc0170ec.ar.png)

بعد التنزيل، يجب إضافته إلى دليل Resources الخاص بالمشروع في Xcode.

![model](../../../../../translated_images/model.f0cb932ac2c7648211fbe5341ee1aa42b77cb7f956b6d9b084afb8fbf52927c7.ar.png)

## **6. إضافة واجهة برمجة تطبيقات C++ في ViewControllers**

> **ملاحظة:**

- **أ.** أضف ملفات الترويسة C++ المناسبة إلى المشروع.

  ![Header File](../../../../../translated_images/head.2504a93b0be166afde6729fb193ebd14c5acb00a0bb6de1939b8a175b1f630fb.ar.png)

- **ب.** قم بتضمين `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../../translated_images/lib.86e12a925eb07e4e71a1466fa4f3ad27097e08505d25d34e98c33005d69b6f23.ar.png)

- **c.** Use the C Samples code for testing. You can also add additional features like ChatUI for more functionality.

- **d.** Since you need to use C++ in your project, rename `ViewController.m` to `ViewController.mm` لتمكين دعم Objective-C++.

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

## **7. تشغيل التطبيق**

بمجرد اكتمال الإعداد، يمكنك تشغيل التطبيق لرؤية نتائج استنتاج نموذج Phi-3-mini.

![Running Result](../../../../../translated_images/result.7ebd1fe614f809d776c46475275ec72e4ab898c4ec53ae62b29315c064ca6839.ar.jpg)

لمزيد من عينات الكود والتعليمات التفصيلية، قم بزيارة [مستودع Phi-3 Mini Samples](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حساسة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.