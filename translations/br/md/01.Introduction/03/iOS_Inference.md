<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-07-16T20:20:49+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "br"
}
-->
# **Inferência Phi-3 no iOS**

Phi-3-mini é uma nova série de modelos da Microsoft que permite a implantação de Large Language Models (LLMs) em dispositivos de borda e dispositivos IoT. Phi-3-mini está disponível para implantações em iOS, Android e dispositivos de borda, possibilitando que a IA generativa seja usada em ambientes BYOD. O exemplo a seguir demonstra como implantar o Phi-3-mini no iOS.

## **1. Preparação**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 ou superior)
- **d.** Instale Python 3.10+ (Conda é recomendado)
- **e.** Instale a biblioteca Python: `python-flatbuffers`
- **f.** Instale CMake

### Semantic Kernel e Inferência

Semantic Kernel é um framework de aplicação que permite criar apps compatíveis com Azure OpenAI Service, modelos OpenAI e até modelos locais. Acessar serviços locais via Semantic Kernel facilita a integração com seu servidor de modelo Phi-3-mini auto-hospedado.

### Chamando Modelos Quantizados com Ollama ou LlamaEdge

Muitos usuários preferem usar modelos quantizados para rodar localmente. [Ollama](https://ollama.com) e [LlamaEdge](https://llamaedge.com) permitem chamar diferentes modelos quantizados:

#### **Ollama**

Você pode rodar `ollama run phi3` diretamente ou configurá-lo offline. Crie um Modelfile com o caminho para seu arquivo `gguf`. Código de exemplo para rodar o modelo quantizado Phi-3-mini:

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Se quiser usar `gguf` tanto na nuvem quanto em dispositivos de borda simultaneamente, LlamaEdge é uma ótima opção.

## **2. Compilando ONNX Runtime para iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **Aviso**

- **a.** Antes de compilar, certifique-se de que o Xcode está configurado corretamente e defina-o como diretório ativo de desenvolvedor no terminal:

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** O ONNX Runtime precisa ser compilado para diferentes plataformas. Para iOS, você pode compilar para `arm64` ou `x86_64`.

- **c.** Recomenda-se usar a versão mais recente do iOS SDK para compilação. Porém, você também pode usar uma versão anterior se precisar de compatibilidade com SDKs antigos.

## **3. Compilando IA Generativa com ONNX Runtime para iOS**

> **Note:** Como a IA Generativa com ONNX Runtime está em prévia, esteja ciente de possíveis mudanças.

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

## **4. Criar um aplicativo no Xcode**

Escolhi Objective-C como método de desenvolvimento do app, pois ao usar a API C++ do ONNX Runtime para IA Generativa, o Objective-C tem melhor compatibilidade. Claro, você também pode fazer as chamadas relacionadas via bridging com Swift.

![xcode](../../../../../translated_images/xcode.8147789e6c25e3e2.br.png)

## **5. Copiar o modelo ONNX quantizado INT4 para o projeto do app**

Precisamos importar o modelo quantizado INT4 no formato ONNX, que deve ser baixado primeiro.

![hf](../../../../../translated_images/hf.6b8504fd88ee48dd.br.png)

Após o download, adicione-o ao diretório Resources do projeto no Xcode.

![model](../../../../../translated_images/model.3b879b14e0be877d.br.png)

## **6. Adicionando a API C++ nos ViewControllers**

> **Aviso:**

- **a.** Adicione os arquivos de cabeçalho C++ correspondentes ao projeto.

  ![Header File](../../../../../translated_images/head.64cad021ce70a333.br.png)

- **b.** Inclua a biblioteca dinâmica `onnxruntime-genai` no Xcode.

  ![Library](../../../../../translated_images/lib.a4209b9f21ddf344.br.png)

- **c.** Use o código de exemplo em C para testes. Você também pode adicionar recursos extras como ChatUI para mais funcionalidades.

- **d.** Como será necessário usar C++ no projeto, renomeie `ViewController.m` para `ViewController.mm` para habilitar suporte a Objective-C++.

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

## **7. Executando o Aplicativo**

Com a configuração concluída, você pode rodar o aplicativo para ver os resultados da inferência do modelo Phi-3-mini.

![Running Result](../../../../../translated_images/result.326a947a6a2b9c51.br.jpg)

Para mais exemplos de código e instruções detalhadas, visite o [repositório Phi-3 Mini Samples](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.