<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-05-09T11:01:32+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "he"
}
-->
# **Inference Phi-3 ב-iOS**

Phi-3-mini היא סדרת דגמים חדשה של Microsoft שמאפשרת פריסה של Large Language Models (LLMs) במכשירי קצה ומכשירי IoT. Phi-3-mini זמינה לפריסות iOS, Android ו-Edge Device, ומאפשרת פריסה של AI גנרטיבי בסביבות BYOD. הדוגמה הבאה ממחישה כיצד לפרוס את Phi-3-mini ב-iOS.

## **1. הכנה**

- **א.** macOS 14+
- **ב.** Xcode 15+
- **ג.** iOS SDK 17.x (iPhone 14 A16 או חדש יותר)
- **ד.** התקן Python 3.10+ (מומלץ Conda)
- **ה.** התקן את ספריית ה-Python: `python-flatbuffers`
- **ו.** התקן CMake

### Semantic Kernel ו-Inference

Semantic Kernel הוא מסגרת יישומים שמאפשרת יצירת יישומים התואמים ל-Azure OpenAI Service, דגמי OpenAI, ואפילו דגמים מקומיים. גישה לשירותים מקומיים דרך Semantic Kernel מאפשרת אינטגרציה קלה עם שרת הדגם Phi-3-mini המופעל בעצמך.

### קריאה לדגמים מקוונטים עם Ollama או LlamaEdge

משתמשים רבים מעדיפים להשתמש בדגמים מקוונטים כדי להריץ דגמים מקומית. [Ollama](https://ollama.com) ו-[LlamaEdge](https://llamaedge.com) מאפשרים למשתמשים לקרוא לדגמים מקוונטים שונים:

#### **Ollama**

ניתן להריץ את `ollama run phi3` ישירות או להגדיר אותה במצב לא מקוון. צור Modelfile עם הנתיב לקובץ `gguf` שלך. קוד לדוגמה להרצת דגם Phi-3-mini מקוון:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

אם ברצונך להשתמש ב-`gguf` גם בענן וגם במכשירי קצה בו זמנית, LlamaEdge היא אפשרות מצוינת.

## **2. קומפילציה של ONNX Runtime עבור iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **הערה**

- **א.** לפני הקומפילציה, ודא ש-Xcode מוגדר כראוי והגדר אותו כספריית המפתח הפעילה בטרמינל:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **ב.** יש לקמפל את ONNX Runtime לפלטפורמות שונות. עבור iOS, ניתן לקמפל ל-`arm64` or `x86_64`.

- **ג.** מומלץ להשתמש בגרסת iOS SDK העדכנית ביותר לקומפילציה, אך ניתן להשתמש גם בגרסאות ישנות יותר לצורך תאימות.

## **3. קומפילציה של Generative AI עם ONNX Runtime עבור iOS**

> **הערה:** מאחר ש-Generative AI עם ONNX Runtime נמצא בגרסת תצוגה מוקדמת, יש לקחת בחשבון שינויים אפשריים.

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

## **4. יצירת אפליקציית App ב-Xcode**

בחרתי ב-Objective-C כשיטת פיתוח האפליקציה, מאחר שבשימוש עם Generative AI דרך ONNX Runtime C++ API, Objective-C תואם טוב יותר. כמובן, ניתן גם לבצע קריאות רלוונטיות דרך Swift bridging.

![xcode](../../../../../translated_images/xcode.6c67033ca85b703e80cc51ecaa681fbcb6ac63cc0c256705ac97bc9ca039c235.he.png)

## **5. העתקת דגם ONNX מקוון INT4 לפרויקט אפליקציית ה-App**

יש לייבא את דגם הקווניזציה INT4 בפורמט ONNX, שצריך להוריד קודם לכן

![hf](../../../../../translated_images/hf.b99941885c6561bb3bcc0155d409e713db6d47b4252fb6991a08ffeefc0170ec.he.png)

לאחר ההורדה, יש להוסיף אותו לתיקיית Resources של הפרויקט ב-Xcode.

![model](../../../../../translated_images/model.f0cb932ac2c7648211fbe5341ee1aa42b77cb7f956b6d9b084afb8fbf52927c7.he.png)

## **6. הוספת ה-API של C++ ב-ViewControllers**

> **הערה:**

- **א.** הוסף את קבצי הכותרת המתאימים של C++ לפרויקט.

  ![Header File](../../../../../translated_images/head.2504a93b0be166afde6729fb193ebd14c5acb00a0bb6de1939b8a175b1f630fb.he.png)

- **ב.** כלול את `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../../translated_images/lib.86e12a925eb07e4e71a1466fa4f3ad27097e08505d25d34e98c33005d69b6f23.he.png)

- **c.** Use the C Samples code for testing. You can also add additional features like ChatUI for more functionality.

- **d.** Since you need to use C++ in your project, rename `ViewController.m` to `ViewController.mm` כדי לאפשר תמיכה ב-Objective-C++.

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

## **7. הרצת האפליקציה**

לאחר שההגדרות הושלמו, ניתן להריץ את האפליקציה ולראות את תוצאות ה-inference של דגם Phi-3-mini.

![Running Result](../../../../../translated_images/result.7ebd1fe614f809d776c46475275ec72e4ab898c4ec53ae62b29315c064ca6839.he.jpg)

לקוד לדוגמה נוסף והוראות מפורטות, בקר ב-[Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו הוא המקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי אנושי. איננו אחראים לכל אי-הבנה או פרשנות שגויה הנובעות משימוש בתרגום זה.