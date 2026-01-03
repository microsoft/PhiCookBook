<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-07-16T20:20:59+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "it"
}
-->
# **Inferenza Phi-3 su iOS**

Phi-3-mini è una nuova serie di modelli di Microsoft che consente il deployment di Large Language Models (LLM) su dispositivi edge e dispositivi IoT. Phi-3-mini è disponibile per iOS, Android e deployment su dispositivi Edge, permettendo di utilizzare l’AI generativa in ambienti BYOD. L’esempio seguente mostra come distribuire Phi-3-mini su iOS.

## **1. Preparazione**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 o superiore)
- **d.** Installare Python 3.10+ (si consiglia Conda)
- **e.** Installare la libreria Python: `python-flatbuffers`
- **f.** Installare CMake

### Semantic Kernel e Inferenza

Semantic Kernel è un framework applicativo che permette di creare applicazioni compatibili con Azure OpenAI Service, modelli OpenAI e anche modelli locali. Accedere ai servizi locali tramite Semantic Kernel consente una facile integrazione con il server del modello Phi-3-mini self-hosted.

### Chiamare modelli quantizzati con Ollama o LlamaEdge

Molti utenti preferiscono utilizzare modelli quantizzati per eseguire i modelli localmente. [Ollama](https://ollama.com) e [LlamaEdge](https://llamaedge.com) permettono di chiamare diversi modelli quantizzati:

#### **Ollama**

Puoi eseguire `ollama run phi3` direttamente o configurarlo offline. Crea un Modelfile con il percorso al tuo file `gguf`. Esempio di codice per eseguire il modello quantizzato Phi-3-mini:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Se vuoi usare `gguf` sia nel cloud che su dispositivi edge contemporaneamente, LlamaEdge è un’ottima scelta.

## **2. Compilare ONNX Runtime per iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **Avviso**

- **a.** Prima di compilare, assicurati che Xcode sia configurato correttamente e impostalo come directory attiva per lo sviluppatore nel terminale:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime deve essere compilato per diverse piattaforme. Per iOS, puoi compilare per `arm64` o `x86_64`.

- **c.** Si consiglia di usare l’ultima versione dell’iOS SDK per la compilazione. Tuttavia, puoi anche usare una versione precedente se necessiti compatibilità con SDK più vecchi.

## **3. Compilare Generative AI con ONNX Runtime per iOS**

> **Nota:** Poiché Generative AI con ONNX Runtime è in anteprima, tieni presente che potrebbero esserci modifiche.

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

## **4. Creare un’app in Xcode**

Ho scelto Objective-C come metodo di sviluppo dell’app, perché usando Generative AI con l’API C++ di ONNX Runtime, Objective-C è più compatibile. Naturalmente, puoi anche completare le chiamate correlate tramite bridging con Swift.

![xcode](../../../../../translated_images/xcode.8147789e6c25e3e2.it.png)

## **5. Copiare il modello ONNX quantizzato INT4 nel progetto dell’app**

Dobbiamo importare il modello quantizzato INT4 in formato ONNX, che deve essere scaricato prima

![hf](../../../../../translated_images/hf.6b8504fd88ee48dd.it.png)

Dopo il download, devi aggiungerlo alla cartella Resources del progetto in Xcode.

![model](../../../../../translated_images/model.3b879b14e0be877d.it.png)

## **6. Aggiungere l’API C++ in ViewControllers**

> **Avviso:**

- **a.** Aggiungi i file header C++ corrispondenti al progetto.

  ![Header File](../../../../../translated_images/head.64cad021ce70a333.it.png)

- **b.** Includi la libreria dinamica `onnxruntime-genai` in Xcode.

  ![Library](../../../../../translated_images/lib.a4209b9f21ddf344.it.png)

- **c.** Usa il codice di esempio in C per i test. Puoi anche aggiungere funzionalità extra come ChatUI per maggiori funzionalità.

- **d.** Poiché devi usare C++ nel progetto, rinomina `ViewController.m` in `ViewController.mm` per abilitare il supporto Objective-C++.

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

## **7. Eseguire l’applicazione**

Una volta completata la configurazione, puoi eseguire l’app per vedere i risultati dell’inferenza del modello Phi-3-mini.

![Running Result](../../../../../translated_images/result.326a947a6a2b9c51.it.jpg)

Per ulteriori esempi di codice e istruzioni dettagliate, visita il [repository Phi-3 Mini Samples](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.