<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ffeb840575ff03dea81d2b2214f2e000",
  "translation_date": "2025-04-04T17:45:22+00:00",
  "source_file": "md\\01.Introduction\\03\\iOS_Inference.md",
  "language_code": "hk"
}
-->
# **在 iOS 上推理 Phi-3**

Phi-3-mini 是 Microsoft 推出的新系列模型，專為在邊緣設備和 IoT 設備上部署大型語言模型 (LLMs) 而設計。Phi-3-mini 支援 iOS、Android 和邊緣設備的部署，讓生成式 AI 能夠應用於 BYOD 環境。以下範例展示了如何在 iOS 上部署 Phi-3-mini。

## **1. 準備工作**

- **a.** macOS 14 以上版本  
- **b.** Xcode 15 以上版本  
- **c.** iOS SDK 17.x（iPhone 14 A16 或更高版本）  
- **d.** 安裝 Python 3.10 以上版本（建議使用 Conda）  
- **e.** 安裝 Python 庫：`python-flatbuffers`  
- **f.** 安裝 CMake  

### Semantic Kernel 與推理

Semantic Kernel 是一個應用框架，允許您構建可兼容 Azure OpenAI Service、OpenAI 模型甚至本地模型的應用程序。通過 Semantic Kernel 訪問本地服務，可以輕鬆整合您自託管的 Phi-3-mini 模型服務器。

### 使用 Ollama 或 LlamaEdge 調用量化模型

許多用戶偏好使用量化模型來本地運行模型。[Ollama](https://ollama.com) 和 [LlamaEdge](https://llamaedge.com) 允許用戶調用不同的量化模型：

#### **Ollama**

您可以直接運行 `ollama run phi3` 或離線配置。創建一個 Modelfile，並指向您的 `gguf` 文件。以下是運行 Phi-3-mini 量化模型的範例代碼：

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

如果您希望同時在雲端和邊緣設備上使用 `gguf`，LlamaEdge 是一個很好的選擇。

## **2. 編譯適用於 iOS 的 ONNX Runtime**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **注意事項**

- **a.** 在編譯之前，請確保 Xcode 已正確配置，並在終端中設置為活動開發者目錄：

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime 需要針對不同平台進行編譯。對於 iOS，您可以針對 `arm64` or `x86_64` 進行編譯。

- **c.** 建議使用最新的 iOS SDK 進行編譯。不過，如果需要與舊版 SDK 兼容，也可以使用舊版本。

## **3. 使用 ONNX Runtime 編譯生成式 AI 適用於 iOS**

> **注意：** 由於基於 ONNX Runtime 的生成式 AI 處於預覽階段，請注意可能的變更。

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

## **4. 在 Xcode 中創建一個 App 應用**

我選擇了 Objective-C 作為 App 的開發方式，因為使用基於 ONNX Runtime 的生成式 AI 的 C++ API 時，Objective-C 擁有更好的兼容性。當然，您也可以通過 Swift bridging 完成相關調用。

![xcode](../../../../../translated_images/xcode.6c67033ca85b703e80cc51ecaa681fbcb6ac63cc0c256705ac97bc9ca039c235.hk.png)

## **5. 將 ONNX 量化 INT4 模型複製到 App 應用項目中**

我們需要導入 ONNX 格式的 INT4 量化模型，首先需要下載該模型。

![hf](../../../../../translated_images/hf.b99941885c6561bb3bcc0155d409e713db6d47b4252fb6991a08ffeefc0170ec.hk.png)

下載後，您需要將其添加到 Xcode 項目的 Resources 目錄中。

![model](../../../../../translated_images/model.f0cb932ac2c7648211fbe5341ee1aa42b77cb7f956b6d9b084afb8fbf52927c7.hk.png)

## **6. 在 ViewControllers 中添加 C++ API**

> **注意：**

- **a.** 將相應的 C++ 標頭文件添加到項目中。

  ![Header File](../../../../../translated_images/head.2504a93b0be166afde6729fb193ebd14c5acb00a0bb6de1939b8a175b1f630fb.hk.png)

- **b.** 包含 `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../../translated_images/lib.86e12a925eb07e4e71a1466fa4f3ad27097e08505d25d34e98c33005d69b6f23.hk.png)

- **c.** Use the C Samples code for testing. You can also add additional features like ChatUI for more functionality.

- **d.** Since you need to use C++ in your project, rename `ViewController.m` to `ViewController.mm` 以啟用 Objective-C++ 支持。

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

## **7. 運行應用**

完成設置後，您可以運行應用來查看 Phi-3-mini 模型推理的結果。

![Running Result](../../../../../translated_images/result.7ebd1fe614f809d776c46475275ec72e4ab898c4ec53ae62b29315c064ca6839.hk.jpg)

有關更多範例代碼和詳細說明，請訪問 [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios)。

**免責聲明**：  
此文件是使用AI翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯的。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言版本的文件應被視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋概不負責。