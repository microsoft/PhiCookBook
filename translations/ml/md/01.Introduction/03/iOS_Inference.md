<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-12-22T00:34:48+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "ml"
}
-->
# **iOS-ൽ Phi-3 ഇൻഫറൻസ്**

Phi-3-mini Microsoft നിർമാണമുള്ള ഒരു പുതിയ മോഡൽ പരമ്പരയാണ്, ഇത് Edge ഡിവൈസുകളിലും IoT ഉപകരണങ്ങളിലുമുള്ള Large Language Models (LLMs) ഡിപ്ലോയ് ചെയ്യാൻ സാധ്യമാക്കുന്നു. Phi-3-mini iOS, Android, Edge Device ഡിപ്ലോയ്മെന്റുകൾക്കായി ലഭ്യമാണ്, BYOD പരിസ്ഥിതികളിൽ Generative AI ഡിപ്ലോയ് ചെയ്യാൻ ഇത് അനുവദിക്കുന്നു. താഴെയുള്ള ഉദാഹരണം iOS-ൽ Phi-3-mini എങ്ങനെ ഡിപ്ലോയ് ചെയ്യാമെന്ന് കാണിക്കുന്നു.

## **1. തയ്യാറെടുപ്പ്**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 or greater)
- **d.** Python 3.10+ ഇൻസ്റ്റാൾ ചെയ്യുക (Conda ശുപാർശ ചെയ്യപ്പെടുന്നു)
- **e.** Python ലൈബ്രറി ഇൻസ്റ്റാൾ ചെയ്യുക: `python-flatbuffers`
- **f.** CMake ഇൻസ്റ്റാൾ ചെയ്യുക

### സെമാന്റിക് കർണൽ (Semantic Kernel) மற்றும் ഇൻഫറൻസ്

Semantic Kernel ഒരു അപ്ലിക്കേഷൻ ഫ്രെയിമ്വർക്കാണ്, ഇത് Azure OpenAI Service, OpenAI മോഡലുകൾ, പോലും ലോക്കൽ മോഡലുകൾ എന്നിവയ്ക്ക് അനുയോജ്യമായ ആപ്പുകൾ സൃഷ്ടിക്കാൻ നിങ്ങളെ പ്രേരിപ്പിക്കുന്നു. Semantic Kernel വഴി ലോക്കൽ സർവീസുകളിലേക്ക് ആക്‌സസ് ചെയ്യുന്നതിലൂടെ നിങ്ങളുടെ സ്വയം ഹോസ്റ്റ് ചെയ്ത Phi-3-mini മോഡൽ സർവറുമായി ലളിതമായ ഇന്റഗ്രേഷൻ സാധ്യമാണ്.

### Ollama അല്ലെങ്കിൽ LlamaEdge ഉപയോഗിച്ച് ക്വാന്റ്റൈസ്ഡ് മോഡലുകൾ കോളുചെയ്യൽ

ലോകത്തിൽ പല ഉപയോക്താക്കൾക്കും മോഡലുകൾ ലോക്കലായി ഓടിക്കാൻ ക്വാന്റൈസ്ഡ് മോഡലുകൾ ഉപയോഗിക്കാൻ പ്രാധാന്യമുണ്ട്. [Ollama](https://ollama.com)യും [LlamaEdge](https://llamaedge.com)ഉം വ്യത്യസ്ത ക്വാന്റൈസ്ഡ് മോഡലുകൾ കോളുചെയ്യാൻ ഉപയോക്താക്കളെ അനുവദിക്കുന്നു:

#### **Ollama**

നിങ്ങൾക്ക് നേരിട്ട് `ollama run phi3` റൺ ചെയ്യാവുന്നതാണ് അല്ലെങ്കിൽ അത് ഓഫ്‌ലൈനായി കോൺഫിഗർ ചെയ്യാം. നിങ്ങളുടെ `gguf` ഫയലിന്റെ പാത്ത് ഉപയോഗിച്ച് ഒരു Modelfile സൃഷ്ടിക്കുക. Phi-3-mini ക്വാന്റൈസ്ഡ് മോഡൽ റൺ ചെയ്യുന്നതിനുള്ള സാമ്പിൾ കോഡ്:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

താനൊരു സമയത്ത് ക്ലൗഡ് மற்றும் എഡ്ജ് ഡിവൈസുകളിൽ `gguf` ഉപയോഗിക്കാൻ ആഗ്രഹമുണ്ടെങ്കിൽ, LlamaEdge നല്ലൊരു ഓപ്ഷനാണ്.

## **2. iOS-ക്കുള്ള ONNX Runtime കമ്പൈൽ ചെയ്യൽ**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **കുറിപ്പ്**

- **a.** കമ്പൈൽ ചെയ്യുന്നതിന് മുൻപ്, Xcode ശരിയായി കോൺഫിഗർ ചെയ്തിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക மற்றும் ടർമിനലിൽ അത് ആക്ടീവ് ഡെവലപ്പർ ഡയറക്ടറിയായി സജ്ജമാക്കി:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime വ്യത്യസ്ത പ്ലാറ്റ്ഫോമുകൾക്കായി കമ്പൈൽ ചെയ്യേണ്ടതുണ്ട്. iOS-ിന്, നിങ്ങൾക്ക് `arm64` അല്ലെങ്കിൽ `x86_64` සඳහා കമ്പൈൽ ചെയ്യാം.

- **c.** കമ്പൈലേഷനുമായി ചേർന്നുള്ള ഏറ്റവും പുതിയ iOS SDK ഉപയോഗിക്കണമെന്ന് ശുപാർശ ചെയ്യപ്പെടുന്നു. എന്നിരുന്നാലും, മുൻപ് ഉപയോഗിച്ചിരുന്ന SDK-കളുമായി പൊരുൾക്കപ്പെടേണ്ടതുണ്ടെങ്കിൽ നിങ്ങൾ പഴയ ভার്ഷൻ ഉപയോഗിക്കാവുന്നതാണ്.

## **3. iOS-ക്കുള്ള ONNX Runtime ഉപയോഗിച്ച് Generative AI കമ്പൈൽ ചെയ്യൽ**

> **കുറിപ്പ്:** Generative AI with ONNX Runtime ഇപ്പോൾ പ്രിവ്യൂ ഘട്ടത്തിലാണ്, അതുകൊണ്ട് സാധ്യതയുള്ള മാറ്റങ്ങളെ കുറിച്ച് ദയവായി ശ്രദ്ധിക്കുക.

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

## **4. Xcode-ൽ ഒരു ആപ്പ് ആപ്ലിക്കേഷൻ സൃഷ്ടിക്കുക**

ഞാൻ ആപ്പ് ഡെവലപ്‌മെന്റിനായി Objective-C തിരഞ്ഞെടുക്കുകയാണ്, കാരണം ONNX Runtime C++ API ഉപയോഗിച്ചുള്ള Generative AI-യിൽ Objective-C കൂടുതൽ അനുയോജ്യമാണ്. φυσικά, നിങ്ങൾ Swift bridging വഴി ബന്ധപ്പെട്ട কলുകൾ പൂര്‍ത്തിയാക്കുകയും ചെയ്യാം.

![Xcode](../../../../../translated_images/xcode.8147789e6c25e3e289e6aa56c168089a2c277e3cd6af353fae6c2f4a56eba836.ml.png)

## **5. ONNX ക്വാന്റൈസ്ഡ് INT4 മോഡൽ App ആപ്ലിക്കേഷൻ പ്രോജക്റ്റിലേക്ക് കോപ്പി ചെയ്യുക**

ഞങ്ങൾയ്ക്ക് ആദ്യം ഡൗൺലോഡ് ചെയ്യേണ്ട ONNX ഫോർമാറ്റിലുള്ള INT4 ക്വാന്റൈസേഷൻ മോഡൽ ഇറക്കുമതി ചെയ്യേണ്ടതുണ്ട്

![hf](../../../../../translated_images/hf.6b8504fd88ee48dd512d76e0665cb76bd68c8e53d0b21b2a9e6f269f5b961173.ml.png)

ഡൗൺലോഡ് കഴിഞ്ഞ്, അത് Xcode പ്രോജക്റ്റിലെ Resources ഡയറക്ടറിയിലേക്ക് ചേർക്കേണ്ടതുണ്ട്.

![മോഡൽ](../../../../../translated_images/model.3b879b14e0be877d12282beb83c953a82b62d4bc6b207a78937223f4798d0f4a.ml.png)

## **6. ViewControllers-ലിൽ C++ API ചേർക്കൽ**

> **കുറിപ്പ്:**

- **a.** അനുയോജ്യമായ C++ ഹെഡർ ഫയലുകൾ പ്രോജക്റ്റിലേക്ക് ചേർക്കുക.

  ![ഹെഡർ ഫയൽ](../../../../../translated_images/head.64cad021ce70a333ff5d59d4a1b4fb0f3dd2ca457413646191a18346067b2cc9.ml.png)

- **b.** Xcode-ൽ `onnxruntime-genai` ഡൈനാമിക് ലൈബ്രറി ഉൾപ്പെടുത്തുക.

  ![ലൈബ്രറി](../../../../../translated_images/lib.a4209b9f21ddf3445ba6ac69797d49e6586d68a57cea9f8bc9fc34ec3ee979ec.ml.png)

- **c.** ടെസ്റ്റിംഗിന് C Samples കോഡ് ഉപയോഗിക്കുക. കൂടുതൽ പ്രവർത്തനക്ഷമതക്കായി ChatUI പോലുള്ള അധിക ഫീച്ചറുകൾ നിങ്ങൾക്ക് ചേർക്കാവുന്നതാണ്.

- **d.** നിങ്ങളുടെ പ്രോജക്റ്റിൽ C++ ഉപയോഗിക്കേണ്ടതിനാൽ, Objective-C++ പിന്തുണ സജ്ജമാക്കാൻ `ViewController.m` നാമം `ViewController.mm` എന്നാക്കി മാറ്റുക.

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

## **7. ആപ് റൺ ചെയ്യൽ**

സെറ്റപ്പ് പൂര്‍ത്തിയായ ശേഷം, Phi-3-mini മോഡൽ ഇൻഫറൻസിന്റെ ഫലങ്ങൾ കാണാൻ നിങ്ങൾ ആപ്പ് റൺ ചെയ്യാം.

![പ്രവർത്തന ഫലം](../../../../../translated_images/result.326a947a6a2b9c5115a3e462b9c1b5412260f847478496c0fc7535b985c3f55a.ml.jpg)

കൂടുതൽ സാമ്പിൾ കോഡ് மற்றும் വിശദമായ നിർദേശങ്ങൾക്ക്, സന്ദർശിക്കുക [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
അവകാശവിമുക്തി:
ഈ രേഖ [Co-op Translator](https://github.com/Azure/co-op-translator) എന്ന എഐ (കൃത്രിമ ബുദ്ധി) പരിഭാഷാ സേവനം ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്ക് ശ്രമിച്ചിരുന്നാലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്നതിൽ ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ മാത്രമേ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടൂ. നിർണായകമായ വിവരങ്ങൾക്കായി പ്രൊഫഷണൽ മനുഷ്യപരിഭാഷ ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ചതിനാൽ ഉണ്ടാകുന്ന ഏതൊരു തെറ്റിദ്ധാരണകൾക്കും അല്ലെങ്കിൽ തെറ്റായി വ്യാഖ്യാനിക്കലുകൾക്കും ഞങ്ങൾ ഉത്തരവാദികളുമായി നിൽക്കുന്നില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->