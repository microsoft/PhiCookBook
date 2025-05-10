<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-05-09T10:59:46+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "da"
}
-->
# **Inference Phi-3 på iOS**

Phi-3-mini er en ny modelserie fra Microsoft, der gør det muligt at implementere Large Language Models (LLMs) på edge-enheder og IoT-enheder. Phi-3-mini er tilgængelig til iOS, Android og Edge Device-implementeringer, hvilket gør det muligt at udrulle generativ AI i BYOD-miljøer. Følgende eksempel viser, hvordan man implementerer Phi-3-mini på iOS.

## **1. Forberedelse**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 eller nyere)
- **d.** Installer Python 3.10+ (Conda anbefales)
- **e.** Installer Python-biblioteket: `python-flatbuffers`
- **f.** Installer CMake

### Semantic Kernel og Inference

Semantic Kernel er et applikationsframework, der giver dig mulighed for at skabe apps, der er kompatible med Azure OpenAI Service, OpenAI-modeller og endda lokale modeller. Adgang til lokale tjenester via Semantic Kernel gør det nemt at integrere med din selvhostede Phi-3-mini modelserver.

### Kald af kvantiserede modeller med Ollama eller LlamaEdge

Mange brugere foretrækker at bruge kvantiserede modeller til at køre modeller lokalt. [Ollama](https://ollama.com) og [LlamaEdge](https://llamaedge.com) giver brugere mulighed for at kalde forskellige kvantiserede modeller:

#### **Ollama**

Du kan køre `ollama run phi3` direkte eller konfigurere det offline. Opret en Modelfile med stien til din `gguf` fil. Eksempelkode til at køre Phi-3-mini kvantiserede model:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Hvis du ønsker at bruge `gguf` både i skyen og på edge-enheder samtidig, er LlamaEdge et godt valg.

## **2. Kompilering af ONNX Runtime til iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **Bemærk**

- **a.** Før kompilering, sørg for at Xcode er korrekt konfigureret og sat som aktiv udvikler-mappe i terminalen:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime skal kompileres til forskellige platforme. For iOS kan du kompilere til `arm64` or `x86_64`.

- **c.** Det anbefales at bruge den nyeste iOS SDK til kompilering. Dog kan du også bruge en ældre version, hvis du har brug for kompatibilitet med tidligere SDK’er.

## **3. Kompilering af Generative AI med ONNX Runtime til iOS**

> **Note:** Da Generative AI med ONNX Runtime stadig er i preview, skal du være opmærksom på mulige ændringer.

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

## **4. Opret en App-applikation i Xcode**

Jeg valgte Objective-C som udviklingsmetode til App’en, fordi brug af Generative AI med ONNX Runtime C++ API fungerer bedre med Objective-C. Selvfølgelig kan du også udføre de nødvendige kald via Swift bridging.

![xcode](../../../../../translated_images/xcode.6c67033ca85b703e80cc51ecaa681fbcb6ac63cc0c256705ac97bc9ca039c235.da.png)

## **5. Kopiér den ONNX kvantiserede INT4-model til App-projektet**

Vi skal importere INT4 kvantiseringsmodellen i ONNX-format, som først skal downloades.

![hf](../../../../../translated_images/hf.b99941885c6561bb3bcc0155d409e713db6d47b4252fb6991a08ffeefc0170ec.da.png)

Efter download skal den tilføjes til Resources-mappen i projektet i Xcode.

![model](../../../../../translated_images/model.f0cb932ac2c7648211fbe5341ee1aa42b77cb7f956b6d9b084afb8fbf52927c7.da.png)

## **6. Tilføjelse af C++ API i ViewControllers**

> **Bemærk:**

- **a.** Tilføj de relevante C++ header-filer til projektet.

  ![Header File](../../../../../translated_images/head.2504a93b0be166afde6729fb193ebd14c5acb00a0bb6de1939b8a175b1f630fb.da.png)

- **b.** Inkluder `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../../translated_images/lib.86e12a925eb07e4e71a1466fa4f3ad27097e08505d25d34e98c33005d69b6f23.da.png)

- **c.** Use the C Samples code for testing. You can also add additional features like ChatUI for more functionality.

- **d.** Since you need to use C++ in your project, rename `ViewController.m` to `ViewController.mm` for at aktivere Objective-C++ support.

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

## **7. Kørsel af applikationen**

Når opsætningen er færdig, kan du køre applikationen for at se resultaterne af Phi-3-mini modelinference.

![Running Result](../../../../../translated_images/result.7ebd1fe614f809d776c46475275ec72e4ab898c4ec53ae62b29315c064ca6839.da.jpg)

For flere eksempelkoder og detaljerede instruktioner, besøg [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.