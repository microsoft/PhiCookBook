<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-05-09T11:05:35+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "sk"
}
-->
# **Inference Phi-3 na iOS**

Phi-3-mini je nová séria modelov od Microsoftu, ktorá umožňuje nasadenie veľkých jazykových modelov (LLM) na okrajových zariadeniach a IoT zariadeniach. Phi-3-mini je dostupný pre iOS, Android a Edge Device nasadenia, čo umožňuje využitie generatívnej AI v BYOD prostrediach. Nasledujúci príklad ukazuje, ako nasadiť Phi-3-mini na iOS.

## **1. Príprava**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 alebo novší)
- **d.** Nainštalujte Python 3.10+ (odporúča sa Conda)
- **e.** Nainštalujte Python knižnicu: `python-flatbuffers`
- **f.** Nainštalujte CMake

### Semantic Kernel a Inference

Semantic Kernel je aplikačný framework, ktorý vám umožňuje vytvárať aplikácie kompatibilné so službou Azure OpenAI, OpenAI modelmi a dokonca aj lokálnymi modelmi. Prístup k lokálnym službám cez Semantic Kernel umožňuje jednoduchú integráciu s vaším vlastným Phi-3-mini modelovým serverom.

### Volanie kvantizovaných modelov cez Ollama alebo LlamaEdge

Mnohí používatelia uprednostňujú používanie kvantizovaných modelov na lokálne spúšťanie. [Ollama](https://ollama.com) a [LlamaEdge](https://llamaedge.com) umožňujú používateľom volať rôzne kvantizované modely:

#### **Ollama**

Môžete spustiť `ollama run phi3` priamo alebo ho nakonfigurovať offline. Vytvorte Modelfile s cestou k vášmu súboru `gguf`. Ukážkový kód na spustenie Phi-3-mini kvantizovaného modelu:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Ak chcete používať `gguf` súčasne v cloude aj na edge zariadeniach, LlamaEdge je skvelá voľba.

## **2. Kompilácia ONNX Runtime pre iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **Upozornenie**

- **a.** Pred kompiláciou sa uistite, že Xcode je správne nastavený a nastavte ho ako aktívny vývojársky adresár v termináli:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime je potrebné kompilovať pre rôzne platformy. Pre iOS môžete kompilovať pre `arm64` or `x86_64`.

- **c.** Odporúča sa používať najnovšiu verziu iOS SDK na kompiláciu, no môžete použiť aj staršiu verziu, ak potrebujete kompatibilitu so staršími SDK.

## **3. Kompilácia Generatívnej AI s ONNX Runtime pre iOS**

> **Note:** Keďže Generatívna AI s ONNX Runtime je vo fáze preview, majte na pamäti možné zmeny.

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

## **4. Vytvorenie App aplikácie v Xcode**

Zvolil som Objective-C ako spôsob vývoja aplikácie, pretože pri používaní Generatívnej AI s ONNX Runtime C++ API je Objective-C lepšie kompatibilný. Samozrejme, môžete tiež vykonať príslušné volania cez Swift bridging.

![xcode](../../../../../translated_images/xcode.6c67033ca85b703e80cc51ecaa681fbcb6ac63cc0c256705ac97bc9ca039c235.sk.png)

## **5. Skopírovanie ONNX kvantizovaného INT4 modelu do projektu App aplikácie**

Potrebujeme importovať INT4 kvantizačný model v ONNX formáte, ktorý je potrebné najprv stiahnuť.

![hf](../../../../../translated_images/hf.b99941885c6561bb3bcc0155d409e713db6d47b4252fb6991a08ffeefc0170ec.sk.png)

Po stiahnutí ho pridajte do adresára Resources v projekte v Xcode.

![model](../../../../../translated_images/model.f0cb932ac2c7648211fbe5341ee1aa42b77cb7f956b6d9b084afb8fbf52927c7.sk.png)

## **6. Pridanie C++ API vo ViewControllers**

> **Upozornenie:**

- **a.** Pridajte príslušné C++ hlavičkové súbory do projektu.

  ![Header File](../../../../../translated_images/head.2504a93b0be166afde6729fb193ebd14c5acb00a0bb6de1939b8a175b1f630fb.sk.png)

- **b.** Zahrňte `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../../translated_images/lib.86e12a925eb07e4e71a1466fa4f3ad27097e08505d25d34e98c33005d69b6f23.sk.png)

- **c.** Use the C Samples code for testing. You can also add additional features like ChatUI for more functionality.

- **d.** Since you need to use C++ in your project, rename `ViewController.m` to `ViewController.mm` pre povolenie Objective-C++ podpory.

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

## **7. Spustenie aplikácie**

Keď je nastavenie dokončené, môžete spustiť aplikáciu a vidieť výsledky inferencie modelu Phi-3-mini.

![Running Result](../../../../../translated_images/result.7ebd1fe614f809d776c46475275ec72e4ab898c4ec53ae62b29315c064ca6839.sk.jpg)

Pre viac ukážkového kódu a podrobné inštrukcie navštívte [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, berte prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.