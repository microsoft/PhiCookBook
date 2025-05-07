<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-05-07T14:29:11+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "fr"
}
-->
# **Inférence Phi-3 sur iOS**

Phi-3-mini est une nouvelle série de modèles de Microsoft qui permet le déploiement de grands modèles de langage (LLMs) sur des appareils en périphérie et des dispositifs IoT. Phi-3-mini est disponible pour iOS, Android et les déploiements sur appareils Edge, permettant ainsi de déployer de l’IA générative dans des environnements BYOD. L’exemple suivant montre comment déployer Phi-3-mini sur iOS.

## **1. Préparation**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 ou supérieur)
- **d.** Installer Python 3.10+ (Conda est recommandé)
- **e.** Installer la bibliothèque Python : `python-flatbuffers`
- **f.** Installer CMake

### Semantic Kernel et Inférence

Semantic Kernel est un framework applicatif qui vous permet de créer des applications compatibles avec Azure OpenAI Service, les modèles OpenAI, et même les modèles locaux. Accéder aux services locaux via Semantic Kernel facilite l’intégration avec votre serveur de modèle Phi-3-mini auto-hébergé.

### Appeler des modèles quantifiés avec Ollama ou LlamaEdge

Beaucoup d’utilisateurs préfèrent utiliser des modèles quantifiés pour exécuter les modèles localement. [Ollama](https://ollama.com) et [LlamaEdge](https://llamaedge.com) permettent d’appeler différents modèles quantifiés :

#### **Ollama**

Vous pouvez exécuter `ollama run phi3` directement ou le configurer hors ligne. Créez un Modelfile avec le chemin vers votre fichier `gguf`. Exemple de code pour exécuter le modèle quantifié Phi-3-mini :

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

Si vous souhaitez utiliser `gguf` à la fois dans le cloud et sur des appareils edge simultanément, LlamaEdge est une excellente option.

## **2. Compiler ONNX Runtime pour iOS**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **Remarques**

- **a.** Avant la compilation, assurez-vous que Xcode est correctement configuré et défini comme répertoire de développement actif dans le terminal :

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime doit être compilé pour différentes plateformes. Pour iOS, vous pouvez compiler pour `arm64` or `x86_64`.

- **c.** Il est recommandé d’utiliser la dernière version du SDK iOS pour la compilation. Cependant, vous pouvez aussi utiliser une version plus ancienne si vous avez besoin de compatibilité avec des SDK précédents.

## **3. Compiler Generative AI avec ONNX Runtime pour iOS**

> **Note :** Comme Generative AI avec ONNX Runtime est en aperçu, soyez conscient des possibles modifications.

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

## **4. Créer une application App dans Xcode**

J’ai choisi Objective-C comme méthode de développement de l’application, car pour utiliser Generative AI avec l’API C++ ONNX Runtime, Objective-C offre une meilleure compatibilité. Bien sûr, vous pouvez aussi réaliser les appels nécessaires via un pont Swift.

![xcode](../../../../../translated_images/xcode.8147789e6c25e3e289e6aa56c168089a2c277e3cd6af353fae6c2f4a56eba836.fr.png)

## **5. Copier le modèle quantifié INT4 ONNX dans le projet de l’application**

Nous devons importer le modèle quantifié INT4 au format ONNX, qui doit être téléchargé au préalable.

![hf](../../../../../translated_images/hf.6b8504fd88ee48dd512d76e0665cb76bd68c8e53d0b21b2a9e6f269f5b961173.fr.png)

Après le téléchargement, il faut l’ajouter au répertoire Resources du projet dans Xcode.

![model](../../../../../translated_images/model.3b879b14e0be877d12282beb83c953a82b62d4bc6b207a78937223f4798d0f4a.fr.png)

## **6. Ajouter l’API C++ dans ViewControllers**

> **Remarque :**

- **a.** Ajoutez les fichiers header C++ correspondants au projet.

  ![Header File](../../../../../translated_images/head.64cad021ce70a333ff5d59d4a1b4fb0f3dd2ca457413646191a18346067b2cc9.fr.png)

- **b.** Incluez `onnxruntime-genai` dynamic library in Xcode.

  ![Library](../../../../../translated_images/lib.a4209b9f21ddf3445ba6ac69797d49e6586d68a57cea9f8bc9fc34ec3ee979ec.fr.png)

- **c.** Use the C Samples code for testing. You can also add additional features like ChatUI for more functionality.

- **d.** Since you need to use C++ in your project, rename `ViewController.m` to `ViewController.mm` pour activer le support Objective-C++.

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

## **7. Exécuter l’application**

Une fois la configuration terminée, vous pouvez lancer l’application pour voir les résultats de l’inférence du modèle Phi-3-mini.

![Running Result](../../../../../translated_images/result.326a947a6a2b9c5115a3e462b9c1b5412260f847478496c0fc7535b985c3f55a.fr.jpg)

Pour plus d’exemples de code et des instructions détaillées, consultez le [dépôt Phi-3 Mini Samples](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.