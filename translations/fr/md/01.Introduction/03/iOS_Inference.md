<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "82af197df38d25346a98f1f0e84d1698",
  "translation_date": "2025-07-16T20:17:14+00:00",
  "source_file": "md/01.Introduction/03/iOS_Inference.md",
  "language_code": "fr"
}
-->
# **Inférence Phi-3 sur iOS**

Phi-3-mini est une nouvelle série de modèles de Microsoft qui permet le déploiement de grands modèles de langage (LLMs) sur des appareils edge et des objets connectés (IoT). Phi-3-mini est disponible pour iOS, Android et les déploiements sur appareils edge, permettant ainsi de déployer de l’IA générative dans des environnements BYOD. L’exemple suivant montre comment déployer Phi-3-mini sur iOS.

## **1. Préparation**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 ou supérieur)
- **d.** Installer Python 3.10+ (Conda est recommandé)
- **e.** Installer la bibliothèque Python : `python-flatbuffers`
- **f.** Installer CMake

### Semantic Kernel et Inférence

Semantic Kernel est un framework applicatif qui vous permet de créer des applications compatibles avec Azure OpenAI Service, les modèles OpenAI, et même des modèles locaux. Accéder aux services locaux via Semantic Kernel facilite l’intégration avec votre serveur de modèle Phi-3-mini auto-hébergé.

### Appeler des modèles quantifiés avec Ollama ou LlamaEdge

De nombreux utilisateurs préfèrent utiliser des modèles quantifiés pour exécuter les modèles localement. [Ollama](https://ollama.com) et [LlamaEdge](https://llamaedge.com) permettent d’appeler différents modèles quantifiés :

#### **Ollama**

Vous pouvez exécuter `ollama run phi3` directement ou le configurer en mode hors ligne. Créez un Modelfile avec le chemin vers votre fichier `gguf`. Exemple de code pour exécuter le modèle quantifié Phi-3-mini :

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

- **a.** Avant la compilation, assurez-vous que Xcode est correctement configuré et définissez-le comme répertoire développeur actif dans le terminal :

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime doit être compilé pour différentes plateformes. Pour iOS, vous pouvez compiler pour `arm64` ou `x86_64`.

- **c.** Il est recommandé d’utiliser la dernière version du SDK iOS pour la compilation. Cependant, vous pouvez aussi utiliser une version plus ancienne si vous avez besoin de compatibilité avec des SDK précédents.

## **3. Compiler l’IA générative avec ONNX Runtime pour iOS**

> **Note :** Comme l’IA générative avec ONNX Runtime est en version preview, soyez conscient des éventuels changements.

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

J’ai choisi Objective-C comme méthode de développement de l’application, car en utilisant l’API C++ d’ONNX Runtime pour l’IA générative, Objective-C offre une meilleure compatibilité. Bien sûr, vous pouvez aussi réaliser les appels nécessaires via un pont Swift.

![xcode](../../../../../translated_images/fr/xcode.8147789e6c25e3e2.png)

## **5. Copier le modèle ONNX quantifié INT4 dans le projet de l’application**

Nous devons importer le modèle quantifié INT4 au format ONNX, qui doit d’abord être téléchargé.

![hf](../../../../../translated_images/fr/hf.6b8504fd88ee48dd.png)

Après le téléchargement, il faut l’ajouter au répertoire Resources du projet dans Xcode.

![model](../../../../../translated_images/fr/model.3b879b14e0be877d.png)

## **6. Ajouter l’API C++ dans les ViewControllers**

> **Remarques :**

- **a.** Ajoutez les fichiers d’en-tête C++ correspondants au projet.

  ![Header File](../../../../../translated_images/fr/head.64cad021ce70a333.png)

- **b.** Incluez la bibliothèque dynamique `onnxruntime-genai` dans Xcode.

  ![Library](../../../../../translated_images/fr/lib.a4209b9f21ddf344.png)

- **c.** Utilisez le code d’exemples en C pour les tests. Vous pouvez aussi ajouter des fonctionnalités supplémentaires comme ChatUI pour plus de possibilités.

- **d.** Comme vous devez utiliser du C++ dans votre projet, renommez `ViewController.m` en `ViewController.mm` pour activer le support Objective-C++.

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

![Running Result](../../../../../translated_images/fr/result.326a947a6a2b9c51.jpg)

Pour plus d’exemples de code et des instructions détaillées, consultez le [dépôt Phi-3 Mini Samples](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios).

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.