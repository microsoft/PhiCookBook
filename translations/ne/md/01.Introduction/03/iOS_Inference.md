<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-05-09T10:54:38+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "ne"
}
-->
# **iOS मा Phi-3 इनफरेंस**

Phi-3-mini माइक्रोसफ्टबाट आएको नयाँ मोडल श्रृंखला हो जसले एज उपकरणहरू र IoT उपकरणहरूमा ठूलो भाषा मोडलहरू (LLMs) तैनाथ गर्न सक्षम बनाउँछ। Phi-3-mini iOS, Android, र एज डिभाइस तैनाथीका लागि उपलब्ध छ, जसले BYOD वातावरणमा जेनेरेटिभ AI तैनाथ गर्न अनुमति दिन्छ। तलको उदाहरणले iOS मा Phi-3-mini कसरी तैनाथ गर्ने देखाउँछ।

## **1. तयारी**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 वा माथि)
- **d.** Python 3.10+ इन्स्टल गर्नुहोस् (Conda सिफारिस गरिएको)
- **e.** Python लाइब्रेरी इन्स्टल गर्नुहोस्: `python-flatbuffers`
- **f.** CMake इन्स्टल गर्नुहोस्

### Semantic Kernel र इनफरेंस

Semantic Kernel एउटा एप्लिकेशन फ्रेमवर्क हो जसले Azure OpenAI Service, OpenAI मोडलहरू, र स्थानीय मोडलहरूसँग मिल्ने एप्लिकेशनहरू बनाउन अनुमति दिन्छ। Semantic Kernel मार्फत स्थानीय सेवा पहुँच गर्दा तपाईंको स्व-होस्ट गरिएको Phi-3-mini मोडल सर्भरसँग सजिलै एकीकरण गर्न सकिन्छ।

### Ollama वा LlamaEdge मार्फत क्वान्टाइज्ड मोडलहरू कल गर्ने

धेरै प्रयोगकर्ताहरू मोडलहरू स्थानीय रूपमा चलाउन क्वान्टाइज्ड मोडलहरू प्रयोग गर्न रुचाउँछन्। [Ollama](https://ollama.com) र [LlamaEdge](https://llamaedge.com) ले विभिन्न क्वान्टाइज्ड मोडलहरू कल गर्न अनुमति दिन्छन्:

#### **Ollama**

तपाईं `ollama run phi3` सिधै चलाउन सक्नुहुन्छ वा अफलाइन कन्फिगर गर्न सक्नुहुन्छ। आफ्नो `gguf` फाइलको पथ सहित Modelfile बनाउनुहोस्। Phi-3-mini क्वान्टाइज्ड मोडल चलाउन नमूना कोड:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

यदि तपाईंले `gguf` लाई क्लाउड र एज दुवै उपकरणमा एकै समयमा प्रयोग गर्न चाहनुहुन्छ भने, LlamaEdge राम्रो विकल्प हो।

## **2. iOS का लागि ONNX Runtime कम्पाइल गर्ने**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **सूचना**

- **a.** कम्पाइल गर्नु अघि, Xcode ठीकसँग कन्फिगर गरिएको छ र टर्मिनलमा सक्रिय डेभलपर डिरेक्टरीको रूपमा सेट गरिएको छ भनी सुनिश्चित गर्नुहोस्:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime विभिन्न प्लेटफर्महरूका लागि कम्पाइल गर्न आवश्यक छ। iOS का लागि, तपाईं `arm64` or `x86_64` को लागि कम्पाइल गर्न सक्नुहुन्छ।

- **c.** कम्पाइल गर्दा नवीनतम iOS SDK प्रयोग गर्न सिफारिस गरिन्छ। यद्यपि, यदि पुरानो SDK सँग कम्प्याटिबिलिटी चाहिन्छ भने पुरानो संस्करण पनि प्रयोग गर्न सकिन्छ।

## **3. iOS का लागि ONNX Runtime सँग जेनेरेटिभ AI कम्पाइल गर्ने**

> **Note:** ONNX Runtime सँग जेनेरेटिभ AI प्रिभ्यु अवस्थामा भएकाले सम्भावित परिवर्तनहरू हुन सक्छन्।

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

## **4. Xcode मा App एप्लिकेशन बनाउने**

मैले App विकास विधि रूपमा Objective-C रोजेको छु, किनकि ONNX Runtime C++ API सँग जेनेरेटिभ AI प्रयोग गर्दा Objective-C बढी अनुकूल हुन्छ। पक्कै पनि, Swift bridging मार्फत सम्बन्धित कलहरू पनि पूरा गर्न सकिन्छ।

![xcode](../../../../../translated_images/xcode.6c67033ca85b703e80cc51ecaa681fbcb6ac63cc0c256705ac97bc9ca039c235.ne.png)

## **5. ONNX क्वान्टाइज्ड INT4 मोडल App एप्लिकेशन प्रोजेक्टमा कपी गर्ने**

हामीले ONNX ढाँचामा INT4 क्वान्टाइजेशन मोडल आयात गर्न आवश्यक छ, जुन पहिले डाउनलोड गर्नुपर्छ।

![hf](../../../../../translated_images/hf.b99941885c6561bb3bcc0155d409e713db6d47b4252fb6991a08ffeefc0170ec.ne.png)

डाउनलोड पछि, यसलाई Xcode मा प्रोजेक्टको Resources डिरेक्टरीमा थप्नुहोस्।

![model](../../../../../translated_images/model.f0cb932ac2c7648211fbe5341ee1aa42b77cb7f956b6d9b084afb8fbf52927c7.ne.png)

## **6. ViewControllers मा C++ API थप्ने**

> **सूचना:**

- **a.** सम्बन्धित C++ हेडर फाइलहरू प्रोजेक्टमा थप्नुहोस्।

  ![Header File](../../../../../translated_images/head.2504a93b0be166afde6729fb193ebd14c5acb00a0bb6de1939b8a175b1f630fb.ne.png)

- **b.** Objective-C++ समर्थन सक्षम गर्न `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../../translated_images/lib.86e12a925eb07e4e71a1466fa4f3ad27097e08505d25d34e98c33005d69b6f23.ne.png)

- **c.** Use the C Samples code for testing. You can also add additional features like ChatUI for more functionality.

- **d.** Since you need to use C++ in your project, rename `ViewController.m` to `ViewController.mm` समावेश गर्नुहोस्।

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

## **7. एप्लिकेशन चलाउने**

सेटअप पूरा भएपछि, Phi-3-mini मोडल इनफरेंसको परिणाम हेर्न एप्लिकेशन चलाउन सक्नुहुन्छ।

![Running Result](../../../../../translated_images/result.7ebd1fe614f809d776c46475275ec72e4ab898c4ec53ae62b29315c064ca6839.ne.jpg)

थप नमूना कोड र विस्तृत निर्देशनहरूका लागि [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios) मा जानुहोस्।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) को प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्दछ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा व्याख्यामा हामी जिम्मेवार छैनौं।