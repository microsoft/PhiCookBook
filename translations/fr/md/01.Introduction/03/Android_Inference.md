<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-07-16T20:10:26+00:00",
  "source_file": "md/01.Introduction/03/Android_Inference.md",
  "language_code": "fr"
}
-->
# **Inférence Phi-3 sur Android**

Découvrons comment effectuer une inférence avec Phi-3-mini sur des appareils Android. Phi-3-mini est une nouvelle série de modèles de Microsoft qui permet le déploiement de grands modèles de langage (LLM) sur des appareils edge et des objets connectés (IoT).

## Semantic Kernel et Inférence

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) est un cadre applicatif qui vous permet de créer des applications compatibles avec Azure OpenAI Service, les modèles OpenAI, et même des modèles locaux. Si vous débutez avec Semantic Kernel, nous vous recommandons de consulter le [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Pour accéder à Phi-3-mini avec Semantic Kernel

Vous pouvez le combiner avec le Hugging Face Connector dans Semantic Kernel. Consultez ce [code d’exemple](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Par défaut, cela correspond à l’ID du modèle sur Hugging Face. Cependant, vous pouvez aussi vous connecter à un serveur de modèle Phi-3-mini construit localement.

### Appeler des modèles quantifiés avec Ollama ou LlamaEdge

De nombreux utilisateurs préfèrent utiliser des modèles quantifiés pour exécuter les modèles localement. [Ollama](https://ollama.com/) et [LlamaEdge](https://llamaedge.com) permettent aux utilisateurs individuels d’appeler différents modèles quantifiés :

#### Ollama

Vous pouvez lancer directement `ollama run Phi-3` ou le configurer hors ligne en créant un `Modelfile` avec le chemin vers votre fichier `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Code d’exemple](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Si vous souhaitez utiliser des fichiers `.gguf` à la fois dans le cloud et sur des appareils edge, LlamaEdge est un excellent choix. Vous pouvez consulter ce [code d’exemple](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) pour commencer.

### Installer et lancer sur téléphones Android

1. **Téléchargez l’application MLC Chat** (gratuite) pour téléphones Android.  
2. Téléchargez le fichier APK (148 Mo) et installez-le sur votre appareil.  
3. Lancez l’application MLC Chat. Vous verrez une liste de modèles d’IA, y compris Phi-3-mini.

En résumé, Phi-3-mini ouvre des perspectives passionnantes pour l’IA générative sur les appareils edge, et vous pouvez commencer à explorer ses capacités sur Android.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.