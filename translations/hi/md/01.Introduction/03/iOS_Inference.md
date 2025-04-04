<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ffeb840575ff03dea81d2b2214f2e000",
  "translation_date": "2025-04-04T17:46:06+00:00",
  "source_file": "md\\01.Introduction\\03\\iOS_Inference.md",
  "language_code": "hi"
}
-->
# **iOS में Phi-3 का उपयोग**

Phi-3-mini Microsoft की एक नई मॉडल श्रृंखला है, जो बड़े भाषा मॉडल (LLMs) को एज डिवाइस और IoT डिवाइस पर तैनात करने में सक्षम बनाती है। Phi-3-mini iOS, Android और एज डिवाइस पर तैनात करने के लिए उपलब्ध है, जिससे जनरेटिव AI को BYOD वातावरण में लागू किया जा सकता है। निम्नलिखित उदाहरण दिखाता है कि iOS पर Phi-3-mini कैसे तैनात करें।

## **1. तैयारी**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 या उससे अधिक)
- **d.** Python 3.10+ इंस्टॉल करें (Conda की सिफारिश की जाती है)
- **e.** Python लाइब्रेरी इंस्टॉल करें: `python-flatbuffers`
- **f.** CMake इंस्टॉल करें

### Semantic Kernel और Inference

Semantic Kernel एक एप्लिकेशन फ्रेमवर्क है जो Azure OpenAI Service, OpenAI मॉडल और यहां तक कि लोकल मॉडल के साथ संगत एप्लिकेशन बनाने की अनुमति देता है। Semantic Kernel के माध्यम से लोकल सर्विसेज तक पहुंचने से आपके स्वयं-होस्टेड Phi-3-mini मॉडल सर्वर के साथ आसानी से इंटीग्रेशन संभव होता है।

### Ollama या LlamaEdge के साथ क्वांटाइज्ड मॉडल्स का उपयोग करना

कई उपयोगकर्ता मॉडल्स को लोकल रूप से चलाने के लिए क्वांटाइज्ड मॉडल्स का उपयोग करना पसंद करते हैं। [Ollama](https://ollama.com) और [LlamaEdge](https://llamaedge.com) उपयोगकर्ताओं को विभिन्न क्वांटाइज्ड मॉडल्स को कॉल करने की अनुमति देते हैं:

#### **Ollama**

आप `ollama run phi3` को सीधे चला सकते हैं या इसे ऑफलाइन कॉन्फ़िगर कर सकते हैं। अपने `gguf` फाइल के पथ के साथ एक Modelfile बनाएं। Phi-3-mini क्वांटाइज्ड मॉडल चलाने के लिए सैंपल कोड:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

अगर आप `gguf` को क्लाउड और एज डिवाइस दोनों पर एक साथ उपयोग करना चाहते हैं, तो LlamaEdge एक बेहतरीन विकल्प है।

## **2. iOS के लिए ONNX Runtime को कम्पाइल करना**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **ध्यान दें**

- **a.** कम्पाइल करने से पहले, सुनिश्चित करें कि Xcode सही तरीके से कॉन्फ़िगर किया गया है और इसे टर्मिनल में एक्टिव डेवलपर डायरेक्टरी के रूप में सेट करें:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime को विभिन्न प्लेटफॉर्म्स के लिए कम्पाइल करना होता है। iOS के लिए, आप `arm64` or `x86_64` के लिए कम्पाइल कर सकते हैं।

- **c.** कम्पाइल करने के लिए नवीनतम iOS SDK का उपयोग करने की सिफारिश की जाती है। हालांकि, अगर आपको पुराने SDKs के साथ संगतता चाहिए तो आप पुराने संस्करण का भी उपयोग कर सकते हैं।

## **3. iOS के लिए ONNX Runtime के साथ जनरेटिव AI को कम्पाइल करना**

> **ध्यान दें:** चूंकि ONNX Runtime के साथ जनरेटिव AI अभी प्रीव्यू में है, कृपया संभावित परिवर्तनों से अवगत रहें।

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

## **4. Xcode में एक App एप्लिकेशन बनाना**

मैंने App डेवलपमेंट के लिए Objective-C को चुना क्योंकि ONNX Runtime C++ API के साथ जनरेटिव AI का उपयोग करने में Objective-C बेहतर संगतता प्रदान करता है। बेशक, आप Swift ब्रिजिंग के माध्यम से संबंधित कॉल्स भी पूरा कर सकते हैं।

![xcode](../../../../../translated_images/xcode.6c67033ca85b703e80cc51ecaa681fbcb6ac63cc0c256705ac97bc9ca039c235.hi.png)

## **5. ONNX क्वांटाइज्ड INT4 मॉडल को App एप्लिकेशन प्रोजेक्ट में कॉपी करना**

हमें ONNX फॉर्मेट में INT4 क्वांटाइजेशन मॉडल को इम्पोर्ट करने की आवश्यकता है, जिसे पहले डाउनलोड करना होगा।

![hf](../../../../../translated_images/hf.b99941885c6561bb3bcc0155d409e713db6d47b4252fb6991a08ffeefc0170ec.hi.png)

डाउनलोड करने के बाद, आपको इसे Xcode में प्रोजेक्ट की Resources डायरेक्टरी में जोड़ना होगा।

![model](../../../../../translated_images/model.f0cb932ac2c7648211fbe5341ee1aa42b77cb7f956b6d9b084afb8fbf52927c7.hi.png)

## **6. ViewControllers में C++ API जोड़ना**

> **ध्यान दें:**

- **a.** प्रोजेक्ट में संबंधित C++ हेडर फाइल्स जोड़ें।

  ![Header File](../../../../../translated_images/head.2504a93b0be166afde6729fb193ebd14c5acb00a0bb6de1939b8a175b1f630fb.hi.png)

- **b.** `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../../translated_images/lib.86e12a925eb07e4e71a1466fa4f3ad27097e08505d25d34e98c33005d69b6f23.hi.png)

- **c.** Use the C Samples code for testing. You can also add additional features like ChatUI for more functionality.

- **d.** Since you need to use C++ in your project, rename `ViewController.m` to `ViewController.mm` को शामिल करें ताकि Objective-C++ सपोर्ट सक्षम हो सके।

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

## **7. एप्लिकेशन चलाना**

सेटअप पूरा होने के बाद, आप एप्लिकेशन को चला सकते हैं और Phi-3-mini मॉडल इन्फरेंस के परिणाम देख सकते हैं।

![Running Result](../../../../../translated_images/result.7ebd1fe614f809d776c46475275ec72e4ab898c4ec53ae62b29315c064ca6839.hi.jpg)

अधिक सैंपल कोड और विस्तृत निर्देशों के लिए [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios) पर जाएं।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।