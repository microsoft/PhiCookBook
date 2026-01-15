<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-07-16T20:19:36+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "hi"
}
-->
# **iOS में Inference Phi-3**

Phi-3-mini Microsoft की एक नई मॉडल श्रृंखला है जो एज डिवाइस और IoT डिवाइस पर Large Language Models (LLMs) को डिप्लॉय करने में सक्षम बनाती है। Phi-3-mini iOS, Android, और Edge Device डिप्लॉयमेंट के लिए उपलब्ध है, जिससे BYOD वातावरण में जनरेटिव AI को डिप्लॉय किया जा सकता है। निम्नलिखित उदाहरण में दिखाया गया है कि iOS पर Phi-3-mini को कैसे डिप्लॉय किया जाए।

## **1. तैयारी**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 या उससे ऊपर)
- **d.** Python 3.10+ इंस्टॉल करें (Conda की सलाह दी जाती है)
- **e.** Python लाइब्रेरी इंस्टॉल करें: `python-flatbuffers`
- **f.** CMake इंस्टॉल करें

### Semantic Kernel और Inference

Semantic Kernel एक एप्लिकेशन फ्रेमवर्क है जो आपको Azure OpenAI Service, OpenAI मॉडल्स, और यहां तक कि लोकल मॉडल्स के साथ संगत एप्लिकेशन बनाने की अनुमति देता है। Semantic Kernel के माध्यम से लोकल सर्विसेज़ तक पहुंचने से आप अपने स्वयं के होस्ट किए गए Phi-3-mini मॉडल सर्वर के साथ आसानी से इंटीग्रेट कर सकते हैं।

### Ollama या LlamaEdge के साथ Quantized मॉडल कॉल करना

कई उपयोगकर्ता मॉडल्स को लोकली चलाने के लिए quantized मॉडल्स का उपयोग करना पसंद करते हैं। [Ollama](https://ollama.com) और [LlamaEdge](https://llamaedge.com) उपयोगकर्ताओं को विभिन्न quantized मॉडल्स कॉल करने की सुविधा देते हैं:

#### **Ollama**

आप सीधे `ollama run phi3` चला सकते हैं या इसे ऑफलाइन कॉन्फ़िगर कर सकते हैं। अपने `gguf` फाइल के पाथ के साथ एक Modelfile बनाएं। Phi-3-mini quantized मॉडल चलाने के लिए नमूना कोड:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

यदि आप `gguf` को क्लाउड और एज डिवाइस दोनों पर एक साथ उपयोग करना चाहते हैं, तो LlamaEdge एक बेहतरीन विकल्प है।

## **2. iOS के लिए ONNX Runtime को कंपाइल करना**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **सूचना**

- **a.** कंपाइल करने से पहले, सुनिश्चित करें कि Xcode सही तरीके से कॉन्फ़िगर है और टर्मिनल में इसे सक्रिय डेवलपर डायरेक्टरी के रूप में सेट करें:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime को विभिन्न प्लेटफॉर्म्स के लिए कंपाइल करना होता है। iOS के लिए, आप `arm64` या `x86_64` के लिए कंपाइल कर सकते हैं।

- **c.** कंपाइलेशन के लिए नवीनतम iOS SDK का उपयोग करने की सलाह दी जाती है। हालांकि, यदि आपको पुराने SDK के साथ संगतता चाहिए तो आप पुराने संस्करण का भी उपयोग कर सकते हैं।

## **3. iOS के लिए ONNX Runtime के साथ Generative AI को कंपाइल करना**

> **Note:** चूंकि ONNX Runtime के साथ Generative AI अभी प्रीव्यू में है, कृपया संभावित बदलावों के प्रति सतर्क रहें।

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

## **4. Xcode में एक App एप्लिकेशन बनाएं**

मैंने App विकास के लिए Objective-C चुना क्योंकि ONNX Runtime C++ API के साथ Generative AI का उपयोग करते समय Objective-C बेहतर संगत होता है। बेशक, आप Swift ब्रिजिंग के माध्यम से संबंधित कॉल भी पूरा कर सकते हैं।

![xcode](../../../../../translated_images/hi/xcode.8147789e6c25e3e2.png)

## **5. ONNX क्वांटाइज्ड INT4 मॉडल को App एप्लिकेशन प्रोजेक्ट में कॉपी करें**

हमें ONNX फॉर्मेट में INT4 क्वांटाइजेशन मॉडल इम्पोर्ट करना होगा, जिसे पहले डाउनलोड करना आवश्यक है।

![hf](../../../../../translated_images/hi/hf.6b8504fd88ee48dd.png)

डाउनलोड करने के बाद, आपको इसे Xcode में प्रोजेक्ट के Resources डायरेक्टरी में जोड़ना होगा।

![model](../../../../../translated_images/hi/model.3b879b14e0be877d.png)

## **6. ViewControllers में C++ API जोड़ना**

> **सूचना:**

- **a.** संबंधित C++ हेडर फाइल्स को प्रोजेक्ट में जोड़ें।

  ![Header File](../../../../../translated_images/hi/head.64cad021ce70a333.png)

- **b.** Xcode में `onnxruntime-genai` डायनेमिक लाइब्रेरी को शामिल करें।

  ![Library](../../../../../translated_images/hi/lib.a4209b9f21ddf344.png)

- **c.** परीक्षण के लिए C Samples कोड का उपयोग करें। आप अधिक कार्यक्षमता के लिए ChatUI जैसी अतिरिक्त सुविधाएं भी जोड़ सकते हैं।

- **d.** चूंकि आपको अपने प्रोजेक्ट में C++ का उपयोग करना है, इसलिए `ViewController.m` का नाम बदलकर `ViewController.mm` करें ताकि Objective-C++ सपोर्ट सक्षम हो सके।

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

सेटअप पूरा होने के बाद, आप एप्लिकेशन चला सकते हैं और Phi-3-mini मॉडल के inference के परिणाम देख सकते हैं।

![Running Result](../../../../../translated_images/hi/result.326a947a6a2b9c51.jpg)

अधिक नमूना कोड और विस्तृत निर्देशों के लिए, [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios) पर जाएं।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।