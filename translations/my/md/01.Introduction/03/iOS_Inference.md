<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-07-09T20:04:02+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "my"
}
-->
# **iOS တွင် Phi-3 အာရုံစူးစိုက်မှု**

Phi-3-mini သည် Microsoft မှ ထုတ်လုပ်သော မော်ဒယ်အသစ်တစ်ခုဖြစ်ပြီး Edge စက်ပစ္စည်းများနှင့် IoT စက်ပစ္စည်းများပေါ်တွင် Large Language Models (LLMs) ကို တပ်ဆင်အသုံးပြုနိုင်စေသည်။ Phi-3-mini ကို iOS, Android နှင့် Edge Device များတွင် အသုံးပြုနိုင်ပြီး BYOD ပတ်ဝန်းကျင်များတွင် generative AI ကို တပ်ဆင်နိုင်သည်။ အောက်ပါ ဥပမာတွင် iOS ပေါ်တွင် Phi-3-mini ကို မည်သို့ တပ်ဆင်ရမည်ကို ပြသထားသည်။

## **1. ပြင်ဆင်မှု**

- **က.** macOS 14+
- **ခ.** Xcode 15+
- **ဂ.** iOS SDK 17.x (iPhone 14 A16 သို့မဟုတ် အထက်)
- **ဃ.** Python 3.10+ တပ်ဆင်ရန် (Conda ကို အကြံပြုသည်)
- **င.** Python စာကြည့်တိုက် `python-flatbuffers` ကို တပ်ဆင်ရန်
- **စ.** CMake ကို တပ်ဆင်ရန်

### Semantic Kernel နှင့် အာရုံစူးစိုက်မှု

Semantic Kernel သည် Azure OpenAI Service, OpenAI မော်ဒယ်များနှင့် ဒေသခံ မော်ဒယ်များနှင့် ကိုက်ညီသော အက်ပလီကေးရှင်းများ ဖန်တီးနိုင်သော application framework ဖြစ်သည်။ Semantic Kernel မှတဆင့် ဒေသခံ ဝန်ဆောင်မှုများကို ချိတ်ဆက်နိုင်ပြီး သင့်ကိုယ်ပိုင် Phi-3-mini မော်ဒယ်ဆာဗာနှင့် လွယ်ကူစွာ ပေါင်းစည်းနိုင်သည်။

### Ollama သို့မဟုတ် LlamaEdge ဖြင့် Quantized မော်ဒယ်များ ခေါ်ယူခြင်း

အသုံးပြုသူများအများစုသည် မော်ဒယ်များကို ဒေသခံတွင် ပြေးဆွဲရန် quantized မော်ဒယ်များကို အသုံးပြုရန် နှစ်သက်ကြသည်။ [Ollama](https://ollama.com) နှင့် [LlamaEdge](https://llamaedge.com) သည် အသုံးပြုသူများအား quantized မော်ဒယ်အမျိုးမျိုးကို ခေါ်ယူနိုင်စေသည်။

#### **Ollama**

`ollama run phi3` ကို တိုက်ရိုက် ပြေးဆွဲနိုင်သလို offline အနေဖြင့်လည်း ပြင်ဆင်နိုင်သည်။ သင့် `gguf` ဖိုင်လမ်းကြောင်းပါသော Modelfile တစ်ခု ဖန်တီးပါ။ Phi-3-mini quantized မော်ဒယ်ကို ပြေးဆွဲရန် နမူနာကုဒ်မှာ အောက်ပါအတိုင်းဖြစ်သည်-

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Cloud နှင့် edge စက်ပစ္စည်းများတွင် `gguf` ကို တပြိုင်နက် အသုံးပြုလိုပါက LlamaEdge သည် အကောင်းဆုံးရွေးချယ်မှုဖြစ်သည်။

## **2. iOS အတွက် ONNX Runtime ကို ကုဒ်ဖိုင်ပြုလုပ်ခြင်း**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **သတိပေးချက်**

- **က.** ကုဒ်ဖိုင်ပြုလုပ်မတိုင်မီ Xcode ကို မှန်ကန်စွာ ပြင်ဆင်ထားပြီး terminal တွင် active developer directory အဖြစ် သတ်မှတ်ထားရန်လိုအပ်သည်-

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **ခ.** ONNX Runtime ကို မတူညီသော ပလက်ဖောင်းများအတွက် ကုဒ်ဖိုင်ပြုလုပ်ရမည်။ iOS အတွက် `arm64` သို့မဟုတ် `x86_64` အတွက် ကုဒ်ဖိုင်ပြုလုပ်နိုင်သည်။

- **ဂ.** ကုဒ်ဖိုင်ပြုလုပ်ရာတွင် နောက်ဆုံး iOS SDK ကို အသုံးပြုရန် အကြံပြုသည်။ သို့သော် ယခင် SDK များနှင့် ကိုက်ညီမှုလိုအပ်ပါက အဟောင်း SDK ကိုလည်း အသုံးပြုနိုင်သည်။

## **3. iOS အတွက် ONNX Runtime ဖြင့် Generative AI ကို ကုဒ်ဖိုင်ပြုလုပ်ခြင်း**

> **Note:** ONNX Runtime ဖြင့် Generative AI သည် preview အဆင့်တွင် ရှိသောကြောင့် ပြောင်းလဲမှုများ ဖြစ်ပေါ်နိုင်သည်ကို သတိပြုပါ။

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

## **4. Xcode တွင် App application တစ်ခု ဖန်တီးခြင်း**

App ဖန်တီးရာတွင် Objective-C ကို ရွေးချယ်ခဲ့သည်၊ ONNX Runtime C++ API ဖြင့် Generative AI ကို အသုံးပြုရာတွင် Objective-C သည် ပိုမိုကိုက်ညီသည်။ သို့သော် Swift bridging ဖြင့်လည်း ဆက်စပ်ခေါ်ယူမှုများ ပြီးမြောက်နိုင်သည်။

![xcode](../../../../../imgs/01/03/iOS/xcode.png)

## **5. ONNX quantized INT4 မော်ဒယ်ကို App application project သို့ ကူးယူထည့်သွင်းခြင်း**

ONNX ပုံစံဖြင့် INT4 quantization မော်ဒယ်ကို အရင်ဆုံး ဒေါင်းလုပ်ရယူရန် လိုအပ်သည်။

![hf](../../../../../imgs/01/03/iOS/hf.png)

ဒေါင်းလုပ်ပြီးနောက် Xcode တွင် project ၏ Resources ဖိုလ်ဒါထဲသို့ ထည့်သွင်းရမည်။

![model](../../../../../imgs/01/03/iOS/model.png)

## **6. ViewControllers တွင် C++ API ထည့်သွင်းခြင်း**

> **သတိပေးချက်**

- **က.** သင့် project တွင် သင့်တော်သော C++ header ဖိုင်များ ထည့်သွင်းပါ။

  ![Header File](../../../../../imgs/01/03/iOS/head.png)

- **ခ.** Xcode တွင် `onnxruntime-genai` dynamic library ကို ထည့်သွင်းပါ။

  ![Library](../../../../../imgs/01/03/iOS/lib.png)

- **ဂ.** စမ်းသပ်ရန် C Samples ကုဒ်ကို အသုံးပြုနိုင်သည်။ ChatUI ကဲ့သို့ အပိုဆောင်း လုပ်ဆောင်ချက်များလည်း ထည့်သွင်းနိုင်သည်။

- **ဃ.** Project တွင် C++ ကို အသုံးပြုရန် `ViewController.m` ကို `ViewController.mm` ဟု အမည်ပြောင်း၍ Objective-C++ ကို ပံ့ပိုးပေးရန် လိုအပ်သည်။

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

## **7. အက်ပလီကေးရှင်းကို ပြေးဆွဲခြင်း**

ပြင်ဆင်မှုများ ပြီးဆုံးသည့်အခါ Phi-3-mini မော်ဒယ်၏ အာရုံစူးစိုက်မှုရလဒ်များကို ကြည့်ရှုနိုင်ရန် အက်ပလီကေးရှင်းကို ပြေးဆွဲနိုင်သည်။

![Running Result](../../../../../imgs/01/03/iOS/result.jpg)

နမူနာကုဒ်များနှင့် အသေးစိတ် လမ်းညွှန်ချက်များအတွက် [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios) ကို လည်ပတ်ကြည့်ရှုနိုင်ပါသည်။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။