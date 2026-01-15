<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-07-16T20:24:11+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "cs"
}
-->
# **Inference Phi-3 v iOS**

Phi-3-mini je nová řada modelů od Microsoftu, která umožňuje nasazení velkých jazykových modelů (LLM) na edge zařízeních a IoT zařízeních. Phi-3-mini je dostupný pro iOS, Android a nasazení na edge zařízeních, což umožňuje využití generativní AI v BYOD prostředích. Následující příklad ukazuje, jak nasadit Phi-3-mini na iOS.

## **1. Příprava**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 nebo novější)
- **d.** Nainstalujte Python 3.10+ (doporučujeme Conda)
- **e.** Nainstalujte Python knihovnu: `python-flatbuffers`
- **f.** Nainstalujte CMake

### Semantic Kernel a inference

Semantic Kernel je aplikační framework, který umožňuje vytvářet aplikace kompatibilní s Azure OpenAI Service, OpenAI modely a dokonce i lokálními modely. Přístup k lokálním službám přes Semantic Kernel usnadňuje integraci s vlastním serverem modelu Phi-3-mini.

### Volání kvantovaných modelů pomocí Ollama nebo LlamaEdge

Mnoho uživatelů preferuje použití kvantovaných modelů pro lokální běh. [Ollama](https://ollama.com) a [LlamaEdge](https://llamaedge.com) umožňují volání různých kvantovaných modelů:

#### **Ollama**

Můžete spustit `ollama run phi3` přímo nebo jej nakonfigurovat offline. Vytvořte Modelfile s cestou k vašemu `gguf` souboru. Ukázkový kód pro spuštění kvantovaného modelu Phi-3-mini:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Pokud chcete používat `gguf` současně v cloudu i na edge zařízeních, LlamaEdge je skvělá volba.

## **2. Kompilace ONNX Runtime pro iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **Upozornění**

- **a.** Před kompilací se ujistěte, že máte správně nastavený Xcode a nastavte jej jako aktivní vývojářský adresář v terminálu:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime je potřeba kompilovat pro různé platformy. Pro iOS můžete kompilovat pro `arm64` nebo `x86_64`.

- **c.** Doporučuje se použít nejnovější iOS SDK pro kompilaci, ale můžete použít i starší verzi, pokud potřebujete kompatibilitu se staršími SDK.

## **3. Kompilace Generative AI s ONNX Runtime pro iOS**

> **Poznámka:** Protože Generative AI s ONNX Runtime je ve fázi preview, mějte prosím na paměti možné změny.

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

## **4. Vytvoření aplikace v Xcode**

Zvolil jsem Objective-C jako způsob vývoje aplikace, protože při použití Generative AI s ONNX Runtime C++ API je Objective-C lépe kompatibilní. Samozřejmě můžete také provádět příslušné volání přes Swift bridging.

![xcode](../../../../../translated_images/cs/xcode.8147789e6c25e3e2.png)

## **5. Zkopírujte kvantovaný INT4 ONNX model do projektu aplikace**

Potřebujeme importovat INT4 kvantovaný model ve formátu ONNX, který je potřeba nejprve stáhnout.

![hf](../../../../../translated_images/cs/hf.6b8504fd88ee48dd.png)

Po stažení je potřeba jej přidat do složky Resources v projektu v Xcode.

![model](../../../../../translated_images/cs/model.3b879b14e0be877d.png)

## **6. Přidání C++ API do ViewControllers**

> **Upozornění:**

- **a.** Přidejte odpovídající C++ hlavičkové soubory do projektu.

  ![Header File](../../../../../translated_images/cs/head.64cad021ce70a333.png)

- **b.** Zahrňte dynamickou knihovnu `onnxruntime-genai` v Xcode.

  ![Library](../../../../../translated_images/cs/lib.a4209b9f21ddf344.png)

- **c.** Pro testování použijte C Samples kód. Můžete také přidat další funkce, jako je ChatUI, pro rozšířenou funkcionalitu.

- **d.** Protože v projektu potřebujete používat C++, přejmenujte `ViewController.m` na `ViewController.mm`, aby bylo povoleno Objective-C++.

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

## **7. Spuštění aplikace**

Po dokončení nastavení můžete aplikaci spustit a zobrazit výsledky inference modelu Phi-3-mini.

![Running Result](../../../../../translated_images/cs/result.326a947a6a2b9c51.jpg)

Pro více ukázkového kódu a podrobné instrukce navštivte [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.