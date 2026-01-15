<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-07-16T20:24:55+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "sr"
}
-->
# **Извођење Phi-3 на iOS**

Phi-3-mini је нова серија модела из Microsoft-а која омогућава покретање великих језичких модела (LLM) на уређајима на ивици мреже и IoT уређајима. Phi-3-mini је доступан за iOS, Android и Edge Device имплементације, што омогућава коришћење генеративне вештачке интелигенције у BYOD окружењима. Следећи пример показује како да покренете Phi-3-mini на iOS.

## **1. Припрема**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 или новији)
- **d.** Инсталирајте Python 3.10+ (препоручује се Conda)
- **e.** Инсталирајте Python библиотеку: `python-flatbuffers`
- **f.** Инсталирајте CMake

### Semantic Kernel и извођење

Semantic Kernel је апликациони оквир који вам омогућава да креирате апликације компатибилне са Azure OpenAI Service, OpenAI моделима, па чак и локалним моделима. Приступање локалним сервисима преко Semantic Kernel-а олакшава интеграцију са вашим самостално хостованим Phi-3-mini сервером модела.

### Позивање квантованих модела помоћу Ollama или LlamaEdge

Многи корисници више воле да користе квантоване моделе за локално покретање. [Ollama](https://ollama.com) и [LlamaEdge](https://llamaedge.com) омогућавају корисницима да позивају различите квантоване моделе:

#### **Ollama**

Можете покренути `ollama run phi3` директно или га конфигурисати офлајн. Креирајте Modelfile са путањом до вашег `gguf` фајла. Пример кода за покретање Phi-3-mini квантованог модела:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Ако желите да користите `gguf` и у облаку и на уређајима на ивици мреже истовремено, LlamaEdge је одлична опција.

## **2. Компилација ONNX Runtime за iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **Напомена**

- **a.** Пре компилације, уверите се да је Xcode правилно подешен и поставите га као активни развојни директоријум у терминалу:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime треба компајлирати за различите платформе. За iOS можете компајлирати за `arm64` или `x86_64`.

- **c.** Препоручује се коришћење најновије iOS SDK верзије за компилацију. Међутим, можете користити и старију верзију ако вам је потребна компатибилност са претходним SDK-овима.

## **3. Компилација генеративне вештачке интелигенције са ONNX Runtime за iOS**

> **Напомена:** Пошто је генеративна вештачка интелигенција са ONNX Runtime у прегледној фази, имајте у виду могуће промене.

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

## **4. Креирање апликације у Xcode**

Изабрао сам Objective-C као метод развоја апликације, јер је коришћење генеративне вештачке интелигенције са ONNX Runtime C++ API-јем боље компатибилно са Objective-C. Наравно, можете и преко Swift bridging-а обавити релевантне позиве.

![xcode](../../../../../translated_images/sr/xcode.8147789e6c25e3e2.png)

## **5. Копирање ONNX квантованог INT4 модела у пројекат апликације**

Потребно је да увеземо INT4 квантовани модел у ONNX формату, који је потребно прво преузети.

![hf](../../../../../translated_images/sr/hf.6b8504fd88ee48dd.png)

Након преузимања, потребно је додати га у Resources директоријум пројекта у Xcode-у.

![model](../../../../../translated_images/sr/model.3b879b14e0be877d.png)

## **6. Додавање C++ API у ViewControllers**

> **Напомена:**

- **a.** Додајте одговарајуће C++ заглављене фајлове у пројекат.

  ![Header File](../../../../../translated_images/sr/head.64cad021ce70a333.png)

- **b.** Укључите `onnxruntime-genai` динамичку библиотеку у Xcode.

  ![Library](../../../../../translated_images/sr/lib.a4209b9f21ddf344.png)

- **c.** Користите C Samples код за тестирање. Такође можете додати додатне функције као што је ChatUI за више функционалности.

- **d.** Пошто је потребно користити C++ у пројекту, преименујте `ViewController.m` у `ViewController.mm` да бисте омогућили Objective-C++ подршку.

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

## **7. Покретање апликације**

Када је подешавање завршено, можете покренути апликацију и видети резултате извођења Phi-3-mini модела.

![Running Result](../../../../../translated_images/sr/result.326a947a6a2b9c51.jpg)

За више примера кода и детаљна упутства посетите [Phi-3 Mini Samples репозиторијум](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.