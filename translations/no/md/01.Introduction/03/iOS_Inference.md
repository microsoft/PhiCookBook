<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-05-09T11:00:14+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "no"
}
-->
# **Inferens Phi-3 på iOS**

Phi-3-mini er en ny modellserie fra Microsoft som muliggjør distribusjon av store språkmodeller (LLMs) på edge-enheter og IoT-enheter. Phi-3-mini er tilgjengelig for iOS, Android og Edge Device-distribusjoner, noe som gjør det mulig å implementere generativ AI i BYOD-miljøer. Eksempelet nedenfor viser hvordan du distribuerer Phi-3-mini på iOS.

## **1. Forberedelser**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 eller nyere)
- **d.** Installer Python 3.10+ (Conda anbefales)
- **e.** Installer Python-biblioteket: `python-flatbuffers`
- **f.** Installer CMake

### Semantic Kernel og Inferens

Semantic Kernel er et applikasjonsrammeverk som lar deg lage applikasjoner kompatible med Azure OpenAI Service, OpenAI-modeller, og til og med lokale modeller. Å få tilgang til lokale tjenester gjennom Semantic Kernel gjør det enkelt å integrere med din selvhostede Phi-3-mini modellserver.

### Kalle kvantiserte modeller med Ollama eller LlamaEdge

Mange brukere foretrekker å bruke kvantiserte modeller for å kjøre modeller lokalt. [Ollama](https://ollama.com) og [LlamaEdge](https://llamaedge.com) lar brukere kalle ulike kvantiserte modeller:

#### **Ollama**

Du kan kjøre `ollama run phi3` direkte eller konfigurere det offline. Lag en Modelfile med stien til din `gguf`-fil. Eksempelkode for å kjøre Phi-3-mini kvantisert modell:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Hvis du ønsker å bruke `gguf` både i skyen og på edge-enheter samtidig, er LlamaEdge et godt valg.

## **2. Kompilere ONNX Runtime for iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **Merk**

- **a.** Før kompilering, sørg for at Xcode er riktig konfigurert og sett som aktiv utviklermappe i terminalen:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime må kompileres for ulike plattformer. For iOS kan du kompilere for `arm64` or `x86_64`.

- **c.** Det anbefales å bruke nyeste iOS SDK for kompilering. Du kan likevel bruke en eldre versjon om du trenger kompatibilitet med tidligere SDK-er.

## **3. Kompilere Generative AI med ONNX Runtime for iOS**

> **Note:** Fordi Generative AI med ONNX Runtime fortsatt er i preview, vær oppmerksom på mulige endringer.

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

## **4. Lag en App-applikasjon i Xcode**

Jeg valgte Objective-C som utviklingsmetode for appen, fordi ved bruk av Generative AI med ONNX Runtime C++ API er Objective-C bedre kompatibelt. Selvfølgelig kan du også gjøre de nødvendige kallene via Swift bridging.

![xcode](../../../../../translated_images/xcode.6c67033ca85b703e80cc51ecaa681fbcb6ac63cc0c256705ac97bc9ca039c235.no.png)

## **5. Kopier ONNX kvantisert INT4-modell til App-prosjektet**

Vi må importere INT4 kvantiseringsmodellen i ONNX-format, som må lastes ned først.

![hf](../../../../../translated_images/hf.b99941885c6561bb3bcc0155d409e713db6d47b4252fb6991a08ffeefc0170ec.no.png)

Etter nedlasting må du legge den til i Resources-mappen i prosjektet i Xcode.

![model](../../../../../translated_images/model.f0cb932ac2c7648211fbe5341ee1aa42b77cb7f956b6d9b084afb8fbf52927c7.no.png)

## **6. Legge til C++ API i ViewControllers**

> **Merk:**

- **a.** Legg til de tilsvarende C++ header-filene i prosjektet.

  ![Header File](../../../../../translated_images/head.2504a93b0be166afde6729fb193ebd14c5acb00a0bb6de1939b8a175b1f630fb.no.png)

- **b.** Inkluder `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../../translated_images/lib.86e12a925eb07e4e71a1466fa4f3ad27097e08505d25d34e98c33005d69b6f23.no.png)

- **c.** Use the C Samples code for testing. You can also add additional features like ChatUI for more functionality.

- **d.** Since you need to use C++ in your project, rename `ViewController.m` to `ViewController.mm` for å aktivere Objective-C++ støtte.

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

## **7. Kjøre applikasjonen**

Når oppsettet er ferdig, kan du kjøre applikasjonen for å se resultatene av Phi-3-mini modellinferens.

![Running Result](../../../../../translated_images/result.7ebd1fe614f809d776c46475275ec72e4ab898c4ec53ae62b29315c064ca6839.no.jpg)

For mer eksempel-kode og detaljerte instruksjoner, besøk [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår fra bruk av denne oversettelsen.