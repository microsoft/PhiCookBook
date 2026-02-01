# **Inference Phi-3 iOS-is**

Phi-3-mini on Microsofti uus mudeliseeria, mis võimaldab suurte keelemudelite (LLM) kasutamist servaseadmetes ja IoT-seadmetes. Phi-3-mini on saadaval iOS-i, Androidi ja servaseadmete jaoks, võimaldades generatiivset tehisintellekti kasutada BYOD-keskkondades. Järgnevas näites näidatakse, kuidas Phi-3-mini iOS-is rakendada.

## **1. Ettevalmistus**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 või uuem)
- **d.** Paigalda Python 3.10+ (soovitatav on Conda)
- **e.** Paigalda Python'i teek: `python-flatbuffers`
- **f.** Paigalda CMake

### Semantic Kernel ja järeldamine

Semantic Kernel on rakenduste raamistik, mis võimaldab luua rakendusi, mis ühilduvad Azure OpenAI teenuse, OpenAI mudelite ja isegi lokaalsete mudelitega. Kohalike teenuste kasutamine läbi Semantic Kernel'i võimaldab lihtsat integreerimist teie enda hostitud Phi-3-mini mudeliserveriga.

### Kvantiseeritud mudelite kasutamine Ollama või LlamaEdge'iga

Paljud kasutajad eelistavad kvantiseeritud mudeleid, et mudeleid lokaalselt käivitada. [Ollama](https://ollama.com) ja [LlamaEdge](https://llamaedge.com) võimaldavad kasutajatel kasutada erinevaid kvantiseeritud mudeleid:

#### **Ollama**

Saate käivitada `ollama run phi3` otse või seadistada selle võrguühenduseta. Looge Modelfile, mis sisaldab teie `gguf` faili teed. Näidis kood Phi-3-mini kvantiseeritud mudeli käivitamiseks:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Kui soovite kasutada `gguf` nii pilves kui ka servaseadmetes samaaegselt, on LlamaEdge suurepärane valik.

## **2. ONNX Runtime'i kompileerimine iOS-i jaoks**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **Märkus**

- **a.** Enne kompileerimist veenduge, et Xcode on õigesti seadistatud ja määrake see terminalis aktiivseks arendaja kataloogiks:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime tuleb kompileerida erinevate platvormide jaoks. iOS-i jaoks saate kompileerida `arm64` või `x86_64`.

- **c.** Soovitatav on kasutada kompileerimiseks uusimat iOS SDK-d. Kuid vajadusel saate kasutada ka vanemat versiooni, et tagada ühilduvus varasemate SDK-dega.

## **3. Generatiivse AI kompileerimine ONNX Runtime'iga iOS-i jaoks**

> **Märkus:** Kuna Generatiivne AI ONNX Runtime'iga on eelvaates, olge teadlik võimalikest muudatustest.

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

## **4. Rakenduse loomine Xcode'is**

Valisin rakenduse arendamiseks Objective-C, kuna Generatiivse AI kasutamine ONNX Runtime C++ API-ga on Objective-C-ga paremini ühilduv. Loomulikult saate seotud kutsed teha ka Swift'i kaudu.

![xcode](../../../../../imgs/01/03/iOS/xcode.png)

## **5. ONNX kvantiseeritud INT4 mudeli kopeerimine rakenduse projekti**

Me peame importima ONNX formaadis INT4 kvantiseeritud mudeli, mille tuleb esmalt alla laadida.

![hf](../../../../../imgs/01/03/iOS/hf.png)

Pärast allalaadimist tuleb see lisada projekti Resources kataloogi Xcode'is.

![model](../../../../../imgs/01/03/iOS/model.png)

## **6. C++ API lisamine ViewControlleritesse**

> **Märkus:**

- **a.** Lisage projekti vastavad C++ päisefailid.

  ![Header File](../../../../../imgs/01/03/iOS/head.png)

- **b.** Lisage Xcode'i `onnxruntime-genai` dünaamiline teek.

  ![Library](../../../../../imgs/01/03/iOS/lib.png)

- **c.** Kasutage C näidiskoodi testimiseks. Samuti saate lisada täiendavaid funktsioone, nagu ChatUI, et pakkuda rohkem võimalusi.

- **d.** Kuna projektis tuleb kasutada C++, nimetage `ViewController.m` ümber `ViewController.mm`-ks, et lubada Objective-C++ tugi.

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

## **7. Rakenduse käivitamine**

Kui seadistus on lõpule viidud, saate rakenduse käivitada, et näha Phi-3-mini mudeli järeldamise tulemusi.

![Running Result](../../../../../imgs/01/03/iOS/result.jpg)

Lisakoodi ja üksikasjalike juhiste saamiseks külastage [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.