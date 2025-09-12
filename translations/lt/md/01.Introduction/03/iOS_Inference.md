<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-09-12T14:53:39+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "lt"
}
-->
# **Inference Phi-3 iOS sistemoje**

Phi-3-mini yra nauja Microsoft modelių serija, leidžianti diegti didelius kalbos modelius (LLMs) kraštiniuose įrenginiuose ir IoT įrenginiuose. Phi-3-mini yra prieinamas iOS, Android ir kraštinių įrenginių diegimui, suteikiant galimybę generatyvųjį AI naudoti BYOD aplinkose. Toliau pateiktas pavyzdys parodo, kaip diegti Phi-3-mini iOS sistemoje.

## **1. Paruošimas**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 arba naujesnis)
- **d.** Įdiegti Python 3.10+ (rekomenduojama Conda)
- **e.** Įdiegti Python biblioteką: `python-flatbuffers`
- **f.** Įdiegti CMake

### Semantic Kernel ir Inference

Semantic Kernel yra aplikacijų kūrimo sistema, leidžianti kurti programas, suderinamas su Azure OpenAI Service, OpenAI modeliais ir net vietiniais modeliais. Naudojant Semantic Kernel vietinėms paslaugoms pasiekti, lengvai integruojamas jūsų paties Phi-3-mini modelio serveris.

### Kvantizuotų modelių naudojimas su Ollama arba LlamaEdge

Daugelis vartotojų renkasi kvantizuotus modelius, kad galėtų juos vykdyti vietoje. [Ollama](https://ollama.com) ir [LlamaEdge](https://llamaedge.com) leidžia vartotojams naudoti įvairius kvantizuotus modelius:

#### **Ollama**

Galite vykdyti `ollama run phi3` tiesiogiai arba konfigūruoti jį neprisijungus. Sukurkite Modelfile su keliu į jūsų `gguf` failą. Pavyzdinis kodas Phi-3-mini kvantizuoto modelio vykdymui:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Jei norite naudoti `gguf` tiek debesų, tiek kraštiniuose įrenginiuose vienu metu, LlamaEdge yra puikus pasirinkimas.

## **2. ONNX Runtime kompiliavimas iOS sistemai**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **Pastaba**

- **a.** Prieš kompiliavimą įsitikinkite, kad Xcode yra tinkamai sukonfigūruotas ir nustatytas kaip aktyvus kūrėjo katalogas terminale:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime reikia kompiliuoti skirtingoms platformoms. iOS sistemai galite kompiliuoti `arm64` arba `x86_64`.

- **c.** Rekomenduojama naudoti naujausią iOS SDK kompiliavimui. Tačiau, jei reikia suderinamumo su ankstesnėmis SDK versijomis, galite naudoti senesnę versiją.

## **3. Generatyvaus AI kompiliavimas su ONNX Runtime iOS sistemai**

> **Pastaba:** Kadangi Generatyvus AI su ONNX Runtime yra peržiūros stadijoje, atkreipkite dėmesį į galimus pakeitimus.

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

## **4. Sukurkite App aplikaciją Xcode**

Aš pasirinkau Objective-C kaip aplikacijos kūrimo metodą, nes naudojant Generatyvų AI su ONNX Runtime C++ API, Objective-C yra geriau suderinamas. Žinoma, susijusius iškvietimus galite atlikti ir per Swift bridging.

![xcode](../../../../../imgs/01/03/iOS/xcode.png)

## **5. Kopijuokite ONNX kvantizuotą INT4 modelį į App aplikacijos projektą**

Reikia importuoti INT4 kvantizacijos modelį ONNX formatu, kurį pirmiausia reikia atsisiųsti.

![hf](../../../../../imgs/01/03/iOS/hf.png)

Po atsisiuntimo, modelį reikia pridėti prie projekto Resources katalogo Xcode.

![model](../../../../../imgs/01/03/iOS/model.png)

## **6. C++ API pridėjimas ViewControllers**

> **Pastaba:**

- **a.** Pridėkite atitinkamus C++ antraštinius failus į projektą.

  ![Header File](../../../../../imgs/01/03/iOS/head.png)

- **b.** Įtraukite `onnxruntime-genai` dinaminę biblioteką į Xcode.

  ![Library](../../../../../imgs/01/03/iOS/lib.png)

- **c.** Naudokite C pavyzdinį kodą testavimui. Taip pat galite pridėti papildomų funkcijų, tokių kaip ChatUI, norėdami išplėsti funkcionalumą.

- **d.** Kadangi projekte reikia naudoti C++, pervadinkite `ViewController.m` į `ViewController.mm`, kad įjungtumėte Objective-C++ palaikymą.

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

## **7. Aplikacijos vykdymas**

Kai nustatymai baigti, galite vykdyti aplikaciją ir pamatyti Phi-3-mini modelio inferencijos rezultatus.

![Running Result](../../../../../imgs/01/03/iOS/result.jpg)

Daugiau pavyzdinio kodo ir išsamių instrukcijų rasite [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.