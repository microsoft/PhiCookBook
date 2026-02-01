# **iOS-ல் Phi-3 inference**

Phi-3-mini என்பது Microsoft நிறுவனத்தின் புதிய மாடல்களின் தொடர் ஆகும், இது edge சாதனங்கள் மற்றும் IoT சாதனங்களில் பெரிய மொழி மாடல்களை (LLMs) செயல்படுத்த அனுமதிக்கிறது. Phi-3-mini iOS, Android மற்றும் Edge Device செயல்பாடுகளுக்கு கிடைக்கிறது, இது BYOD சூழல்களில் Generative AI-ஐ செயல்படுத்த அனுமதிக்கிறது. கீழே உள்ள உதாரணம் iOS-ல் Phi-3-mini-ஐ எப்படி செயல்படுத்துவது என்பதை விளக்குகிறது.

## **1. தயாரிப்பு**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 அல்லது அதற்கு மேல்)
- **d.** Python 3.10+ நிறுவவும் (Conda பரிந்துரைக்கப்படுகிறது)
- **e.** Python நூலகத்தை நிறுவவும்: `python-flatbuffers`
- **f.** CMake நிறுவவும்

### Semantic Kernel மற்றும் Inference

Semantic Kernel என்பது Azure OpenAI Service, OpenAI மாடல்கள் மற்றும் உள்ளூர் மாடல்களுடன் இணக்கமான பயன்பாடுகளை உருவாக்க அனுமதிக்கும் ஒரு பயன்பாட்டு கட்டமைப்பாகும். Semantic Kernel மூலம் உள்ளூர் சேவைகளை அணுகுவது உங்கள் சொந்த-ஹோஸ்ட் செய்யப்பட்ட Phi-3-mini மாடல் சர்வருடன் எளிதாக ஒருங்கிணைக்க அனுமதிக்கிறது.

### Ollama அல்லது LlamaEdge மூலம் Quantized மாடல்களை அழைப்பது

பல பயனர்கள் மாடல்களை உள்ளூரில் இயக்க Quantized மாடல்களை பயன்படுத்த விரும்புகிறார்கள். [Ollama](https://ollama.com) மற்றும் [LlamaEdge](https://llamaedge.com) பயனர்களுக்கு பல Quantized மாடல்களை அழைக்க அனுமதிக்கின்றன:

#### **Ollama**

நீங்கள் `ollama run phi3` ஐ நேரடியாக இயக்கலாம் அல்லது அதை ஆஃப்லைனில் அமைக்கலாம். உங்கள் `gguf` கோப்புக்கான பாதையுடன் ஒரு Modelfile உருவாக்கவும். Phi-3-mini Quantized மாடலை இயக்குவதற்கான மாதிரி குறியீடு:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Cloud மற்றும் Edge சாதனங்களில் ஒரே நேரத்தில் `gguf` ஐ பயன்படுத்த விரும்பினால், LlamaEdge ஒரு சிறந்த விருப்பமாகும்.

## **2. iOS-க்கு ONNX Runtime ஐ Compile செய்வது**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **கவனிக்கவும்**

- **a.** Compile செய்வதற்கு முன், Xcode சரியாக அமைக்கப்பட்டுள்ளதா என்பதை உறுதிப்படுத்தவும் மற்றும் டெர்மினலில் அதை செயலில் உள்ள developer directory ஆக அமைக்கவும்:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime பல தளங்களுக்கு Compile செய்ய வேண்டும். iOS க்காக, நீங்கள் `arm64` அல்லது `x86_64` க்காக Compile செய்யலாம்.

- **c.** Compile செய்ய iOS SDK இன் சமீபத்திய பதிப்பைப் பயன்படுத்த பரிந்துரைக்கப்படுகிறது. இருப்பினும், முந்தைய SDKகளுடன் இணக்கமாக இருக்க வேண்டும் என்றால், பழைய பதிப்பைப் பயன்படுத்தலாம்.

## **3. iOS-க்கு ONNX Runtime உடன் Generative AI ஐ Compile செய்வது**

> **குறிப்பு:** ONNX Runtime உடன் Generative AI Preview நிலையில் இருப்பதால், சாத்தியமான மாற்றங்களை கவனத்தில் கொள்ளவும்.

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

## **4. Xcode-ல் ஒரு App application உருவாக்கவும்**

App அப்ளிகேஷன் உருவாக்க முறைமையாக Objective-C ஐ நான் தேர்ந்தெடுத்தேன், ஏனெனில் ONNX Runtime C++ API உடன் Generative AI பயன்படுத்துவதில் Objective-C சிறந்த இணக்கத்தன்மை கொண்டது. நிச்சயமாக, Swift bridging மூலம் தொடர்புடைய அழைப்புகளை முடிக்கவும் முடியும்.

![xcode](../../../../../imgs/01/03/iOS/xcode.png)

## **5. ONNX Quantized INT4 மாடலை App application திட்டத்திற்கு நகலெடுக்கவும்**

ONNX வடிவத்தில் உள்ள INT4 Quantization மாடலை இறக்குமதி செய்ய வேண்டும், முதலில் அதை பதிவிறக்க வேண்டும்.

![hf](../../../../../imgs/01/03/iOS/hf.png)

பதிவிறக்கிய பிறகு, அதை Xcode-ல் திட்டத்தின் Resources கோப்பகத்தில் சேர்க்க வேண்டும்.

![model](../../../../../imgs/01/03/iOS/model.png)

## **6. ViewControllers-ல் C++ API ஐ சேர்க்கவும்**

> **கவனிக்கவும்:**

- **a.** திட்டத்திற்கு தொடர்புடைய C++ தலைப்பு கோப்புகளைச் சேர்க்கவும்.

  ![Header File](../../../../../imgs/01/03/iOS/head.png)

- **b.** Xcode-ல் `onnxruntime-genai` dynamic library ஐ சேர்க்கவும்.

  ![Library](../../../../../imgs/01/03/iOS/lib.png)

- **c.** சோதனைக்கான C Samples குறியீட்டை பயன்படுத்தவும். மேலும் செயல்பாடுகளுக்கு ChatUI போன்ற கூடுதல் அம்சங்களைச் சேர்க்கவும்.

- **d.** உங்கள் திட்டத்தில் C++ ஐ பயன்படுத்த வேண்டும் என்பதால், Objective-C++ ஆதரவை இயக்க `ViewController.m` ஐ `ViewController.mm` ஆக மறுபெயரிடவும்.

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

## **7. அப்ளிகேஷனை இயக்குவது**

அமைப்பு முடிந்தவுடன், Phi-3-mini மாடல் inference இன் முடிவுகளைப் பார்க்க நீங்கள் அப்ளிகேஷனை இயக்கலாம்.

![Running Result](../../../../../imgs/01/03/iOS/result.jpg)

மேலும் மாதிரி குறியீடு மற்றும் விரிவான வழிமுறைகளுக்கு, [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios) ஐ பார்வையிடவும்.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.