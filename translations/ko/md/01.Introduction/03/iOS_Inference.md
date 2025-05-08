<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-05-08T05:56:16+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "ko"
}
-->
# **iOS에서 Phi-3 추론**

Phi-3-mini는 Microsoft에서 새롭게 선보인 모델 시리즈로, 엣지 디바이스와 IoT 기기에서 대형 언어 모델(LLM)을 배포할 수 있게 해줍니다. Phi-3-mini는 iOS, Android, 엣지 디바이스 배포용으로 제공되어, BYOD 환경에서도 생성형 AI를 활용할 수 있습니다. 아래 예제는 iOS에서 Phi-3-mini를 배포하는 방법을 보여줍니다.

## **1. 준비사항**

- **a.** macOS 14 이상
- **b.** Xcode 15 이상
- **c.** iOS SDK 17.x (iPhone 14 A16 이상)
- **d.** Python 3.10 이상 설치 (Conda 권장)
- **e.** Python 라이브러리 설치: `python-flatbuffers`
- **f.** CMake 설치

### Semantic Kernel과 추론

Semantic Kernel은 Azure OpenAI 서비스, OpenAI 모델, 그리고 로컬 모델과 호환되는 애플리케이션을 만들 수 있는 프레임워크입니다. Semantic Kernel을 통해 로컬 서비스를 호출하면 자체 호스팅하는 Phi-3-mini 모델 서버와 쉽게 연동할 수 있습니다.

### Ollama 또는 LlamaEdge로 양자화 모델 호출하기

많은 사용자가 로컬에서 모델을 실행하기 위해 양자화된 모델을 선호합니다. [Ollama](https://ollama.com)와 [LlamaEdge](https://llamaedge.com)는 다양한 양자화 모델을 호출할 수 있게 해줍니다:

#### **Ollama**

`ollama run phi3`를 직접 실행하거나 오프라인으로 설정할 수 있습니다. `gguf` 파일 경로가 포함된 Modelfile을 생성하세요. Phi-3-mini 양자화 모델 실행 샘플 코드:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

클라우드와 엣지 디바이스에서 `gguf`를 동시에 사용하고 싶다면 LlamaEdge가 좋은 선택입니다.

## **2. iOS용 ONNX Runtime 컴파일**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **주의사항**

- **a.** 컴파일 전에 Xcode가 제대로 설정되어 있는지 확인하고, 터미널에서 활성 개발자 디렉터리로 설정하세요:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime은 다양한 플랫폼용으로 컴파일해야 합니다. iOS의 경우 `arm64` or `x86_64`용으로 컴파일할 수 있습니다.

- **c.** 컴파일 시 최신 iOS SDK 사용을 권장하지만, 이전 SDK와의 호환이 필요하다면 구버전도 사용할 수 있습니다.

## **3. iOS용 ONNX Runtime으로 생성형 AI 컴파일**

> **Note:** ONNX Runtime을 이용한 생성형 AI는 현재 프리뷰 단계이므로, 변경 사항이 있을 수 있습니다.

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

## **4. Xcode에서 앱 애플리케이션 생성**

저는 Objective-C를 앱 개발 언어로 선택했습니다. ONNX Runtime C++ API를 사용하는 생성형 AI와의 호환성이 더 좋기 때문입니다. 물론 Swift 브리징을 통해 관련 호출을 완성할 수도 있습니다.

![xcode](../../../../../translated_images/xcode.8147789e6c25e3e289e6aa56c168089a2c277e3cd6af353fae6c2f4a56eba836.ko.png)

## **5. ONNX 양자화 INT4 모델을 앱 프로젝트에 복사**

ONNX 형식의 INT4 양자화 모델을 먼저 다운로드해야 합니다.

![hf](../../../../../translated_images/hf.6b8504fd88ee48dd512d76e0665cb76bd68c8e53d0b21b2a9e6f269f5b961173.ko.png)

다운로드 후 Xcode 프로젝트 내 Resources 디렉터리에 추가해야 합니다.

![model](../../../../../translated_images/model.3b879b14e0be877d12282beb83c953a82b62d4bc6b207a78937223f4798d0f4a.ko.png)

## **6. ViewControllers에 C++ API 추가**

> **주의:**

- **a.** 프로젝트에 해당 C++ 헤더 파일을 추가하세요.

  ![Header File](../../../../../translated_images/head.64cad021ce70a333ff5d59d4a1b4fb0f3dd2ca457413646191a18346067b2cc9.ko.png)

- **b.** Objective-C++ 지원을 위해 `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../../translated_images/lib.a4209b9f21ddf3445ba6ac69797d49e6586d68a57cea9f8bc9fc34ec3ee979ec.ko.png)

- **c.** Use the C Samples code for testing. You can also add additional features like ChatUI for more functionality.

- **d.** Since you need to use C++ in your project, rename `ViewController.m` to `ViewController.mm`을 포함하세요.

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

## **7. 애플리케이션 실행**

설정이 완료되면 애플리케이션을 실행하여 Phi-3-mini 모델 추론 결과를 확인할 수 있습니다.

![Running Result](../../../../../translated_images/result.326a947a6a2b9c5115a3e462b9c1b5412260f847478496c0fc7535b985c3f55a.ko.jpg)

더 많은 샘플 코드와 자세한 설명은 [Phi-3 Mini Samples 저장소](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios)를 참고하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의해 주시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.