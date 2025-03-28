<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-03-27T07:12:18+00:00",
  "source_file": "md\\01.Introduction\\03\\iOS_Inference.md",
  "language_code": "de"
}
-->
# **Inference Phi-3 in iOS**

Phi-3-mini ist eine neue Modellreihe von Microsoft, die den Einsatz von Large Language Models (LLMs) auf Edge- und IoT-Geräten ermöglicht. Phi-3-mini ist für iOS, Android und Edge-Geräte verfügbar und erlaubt die Bereitstellung generativer KI in BYOD-Umgebungen. Das folgende Beispiel zeigt, wie Phi-3-mini auf iOS implementiert wird.

## **1. Vorbereitung**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 oder höher)
- **d.** Python 3.10+ installieren (Conda wird empfohlen)
- **e.** Die Python-Bibliothek installieren: `python-flatbuffers`
- **f.** CMake installieren

### Semantic Kernel und Inferenz

Semantic Kernel ist ein Anwendungsframework, das die Erstellung von Anwendungen ermöglicht, die mit Azure OpenAI Service, OpenAI-Modellen und sogar lokalen Modellen kompatibel sind. Der Zugriff auf lokale Dienste über Semantic Kernel vereinfacht die Integration mit Ihrem selbst gehosteten Phi-3-mini-Modellserver.

### Aufruf von quantisierten Modellen mit Ollama oder LlamaEdge

Viele Nutzer bevorzugen den Einsatz von quantisierten Modellen, um Modelle lokal auszuführen. [Ollama](https://ollama.com) und [LlamaEdge](https://llamaedge.com) ermöglichen den Aufruf verschiedener quantisierter Modelle:

#### **Ollama**

Sie können `ollama run phi3` direkt ausführen oder offline konfigurieren. Erstellen Sie eine Modelfile mit dem Pfad zu Ihrer `gguf` Datei. Beispielcode für die Ausführung des quantisierten Phi-3-mini-Modells:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Falls Sie `gguf` gleichzeitig in der Cloud und auf Edge-Geräten nutzen möchten, ist LlamaEdge eine hervorragende Option.

## **2. Kompilieren von ONNX Runtime für iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **Hinweis**

- **a.** Stellen Sie vor dem Kompilieren sicher, dass Xcode korrekt konfiguriert ist und setzen Sie es im Terminal als aktives Entwicklerverzeichnis:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime muss für verschiedene Plattformen kompiliert werden. Für iOS können Sie für `arm64` or `x86_64` kompilieren.

- **c.** Es wird empfohlen, die neueste iOS SDK-Version für die Kompilierung zu verwenden. Falls nötig, können Sie auch eine ältere Version nutzen, um die Kompatibilität mit früheren SDKs zu gewährleisten.

## **3. Kompilieren von Generativer KI mit ONNX Runtime für iOS**

> **Hinweis:** Da Generative KI mit ONNX Runtime sich noch in der Vorschau befindet, beachten Sie mögliche Änderungen.

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

## **4. Erstellen einer App-Anwendung in Xcode**

Ich habe mich für Objective-C als Entwicklungsmethode entschieden, da die Verwendung von Generativer KI mit der ONNX Runtime C++ API besser mit Objective-C kompatibel ist. Natürlich können Sie auch die entsprechenden Aufrufe über Swift Bridging durchführen.

![xcode](../../../../../translated_images/xcode.6c67033ca85b703e80cc51ecaa681fbcb6ac63cc0c256705ac97bc9ca039c235.de.png)

## **5. Kopieren des ONNX quantisierten INT4-Modells in das App-Projekt**

Das INT4-Quantisierungsmodell im ONNX-Format muss importiert werden, nachdem es heruntergeladen wurde.

![hf](../../../../../translated_images/hf.b99941885c6561bb3bcc0155d409e713db6d47b4252fb6991a08ffeefc0170ec.de.png)

Nach dem Download müssen Sie es dem Ressourcenverzeichnis des Projekts in Xcode hinzufügen.

![model](../../../../../translated_images/model.f0cb932ac2c7648211fbe5341ee1aa42b77cb7f956b6d9b084afb8fbf52927c7.de.png)

## **6. Hinzufügen der C++ API in ViewControllers**

> **Hinweis:**

- **a.** Fügen Sie die entsprechenden C++-Header-Dateien dem Projekt hinzu.

  ![Header File](../../../../../translated_images/head.2504a93b0be166afde6729fb193ebd14c5acb00a0bb6de1939b8a175b1f630fb.de.png)

- **b.** Integrieren Sie `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../../translated_images/lib.86e12a925eb07e4e71a1466fa4f3ad27097e08505d25d34e98c33005d69b6f23.de.png)

- **c.** Use the C Samples code for testing. You can also add additional features like ChatUI for more functionality.

- **d.** Since you need to use C++ in your project, rename `ViewController.m` to `ViewController.mm`, um Objective-C++-Unterstützung zu aktivieren.

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

## **7. Ausführen der Anwendung**

Nach Abschluss der Einrichtung können Sie die Anwendung ausführen, um die Ergebnisse der Phi-3-mini-Modellinferenz zu sehen.

![Running Result](../../../../../translated_images/result.7ebd1fe614f809d776c46475275ec72e4ab898c4ec53ae62b29315c064ca6839.de.jpg)

Weitere Beispielcodes und detaillierte Anweisungen finden Sie im [Phi-3 Mini Samples Repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.