## Bienvenue dans les labs Phi utilisant C#

Une sélection de labs montre comment intégrer les différentes versions puissantes des modèles Phi dans un environnement .NET.

## Prérequis

Avant d’exécuter l’exemple, assurez-vous d’avoir installé les éléments suivants :

**.NET 9 :** Vérifiez que vous avez la [dernière version de .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) installée sur votre machine.

**(Optionnel) Visual Studio ou Visual Studio Code :** Vous aurez besoin d’un IDE ou d’un éditeur de code capable d’exécuter des projets .NET. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) ou [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) sont recommandés.

**Utilisation de git** : clonez localement l’une des versions disponibles Phi-3, Phi3.5 ou Phi-4 depuis [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Téléchargez les modèles Phi-4 ONNX** sur votre machine locale :

### naviguez vers le dossier où stocker les modèles

```bash
cd c:\phi\models
```

### ajoutez le support pour lfs

```bash
git lfs install 
```

### clonez et téléchargez le modèle Phi-4 mini instruct et le modèle Phi-4 multimodal

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Téléchargez les modèles Phi-3 ONNX** sur votre machine locale :

### clonez et téléchargez le modèle Phi-3 mini 4K instruct et le modèle Phi-3 vision 128K

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Important :** Les démos actuelles sont conçues pour utiliser les versions ONNX des modèles. Les étapes précédentes permettent de cloner les modèles suivants.

## À propos des Labs

La solution principale contient plusieurs labs d’exemples qui démontrent les capacités des modèles Phi en C#.

| Projet | Modèle | Description |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 ou Phi-3.5 | Exemple de chat console permettant à l’utilisateur de poser des questions. Le projet charge un modèle local ONNX Phi-3 en utilisant les bibliothèques `Microsoft.ML.OnnxRuntime`. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 ou Phi-3.5 | Exemple de chat console permettant à l’utilisateur de poser des questions. Le projet charge un modèle local ONNX Phi-3 en utilisant les bibliothèques `Microsoft.Semantic.Kernel`. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 ou Phi-3.5 | Projet exemple utilisant un modèle local phi3 vision pour analyser des images. Le projet charge un modèle local ONNX Phi-3 Vision avec les bibliothèques `Microsoft.ML.OnnxRuntime`. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 ou Phi-3.5 | Projet exemple utilisant un modèle local phi3 vision pour analyser des images. Le projet charge un modèle local ONNX Phi-3 Vision avec les bibliothèques `Microsoft.ML.OnnxRuntime`. Le projet propose également un menu avec différentes options pour interagir avec l’utilisateur. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Exemple de chat console permettant à l’utilisateur de poser des questions. Le projet charge un modèle local ONNX Phi-4 avec les bibliothèques `Microsoft.ML.OnnxRuntime`. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Exemple de chat console permettant à l’utilisateur de poser des questions. Le projet charge un modèle local ONNX Phi-4 avec les bibliothèques `Semantic Kernel`. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Exemple de chat console permettant à l’utilisateur de poser des questions. Le projet charge un modèle local ONNX Phi-4 avec les bibliothèques `Microsoft.ML.OnnxRuntimeGenAI` et implémente `IChatClient` de `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Exemple de chat console permettant à l’utilisateur de poser des questions. Le chat intègre une mémoire. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Projet exemple utilisant un modèle local Phi-4 pour analyser des images et afficher le résultat dans la console. Le projet charge un modèle local Phi-4-`multimodal-instruct-onnx` avec les bibliothèques `Microsoft.ML.OnnxRuntime`. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Projet exemple utilisant un modèle local Phi-4 pour analyser un fichier audio, générer la transcription et afficher le résultat dans la console. Le projet charge un modèle local Phi-4-`multimodal-instruct-onnx` avec les bibliothèques `Microsoft.ML.OnnxRuntime`. |

## Comment exécuter les projets

Pour lancer les projets, suivez ces étapes :

1. Clonez le dépôt sur votre machine locale.

1. Ouvrez un terminal et naviguez vers le projet souhaité. Par exemple, lançons `LabsPhi4-Chat-01OnnxRuntime`.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Exécutez le projet avec la commande

    ```bash
    dotnet run
    ```

1. Le projet exemple demande une saisie utilisateur et répond en utilisant le modèle local.

   La démo en cours d’exécution ressemble à ceci :

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.