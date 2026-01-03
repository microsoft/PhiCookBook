<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b066fc29c1b2129df84e027cb75119ce",
  "translation_date": "2025-07-17T02:38:14+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/ORTWindowGPUGuideline.md",
  "language_code": "fr"
}
-->
# **Guide pour OnnxRuntime GenAI Windows GPU**

Ce guide explique les étapes pour configurer et utiliser ONNX Runtime (ORT) avec des GPU sous Windows. Il est conçu pour vous aider à tirer parti de l’accélération GPU pour vos modèles, améliorant ainsi les performances et l’efficacité.

Le document couvre :

- Configuration de l’environnement : Instructions pour installer les dépendances nécessaires comme CUDA, cuDNN et ONNX Runtime.
- Configuration : Comment paramétrer l’environnement et ONNX Runtime pour exploiter efficacement les ressources GPU.
- Conseils d’optimisation : Recommandations pour ajuster vos réglages GPU afin d’obtenir des performances optimales.

### **1. Python 3.10.x /3.11.8**

   ***Note*** Il est recommandé d’utiliser [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) comme environnement Python

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***Rappel*** Si vous avez installé une bibliothèque ONNX pour Python, veuillez la désinstaller

### **2. Installer CMake avec winget**

   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Installer Visual Studio 2022 - Développement Desktop avec C++**

   ***Note*** Si vous ne souhaitez pas compiler, vous pouvez passer cette étape

![CPP](../../../../../../translated_images/01.42f52a2b2aedff02.fr.png)

### **4. Installer le pilote NVIDIA**

1. **Pilote GPU NVIDIA**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***Rappel*** Veuillez utiliser les paramètres par défaut lors de l’installation

### **5. Configurer l’environnement NVIDIA**

Copiez les dossiers lib, bin, include de NVIDIA CUDNN 9.4 vers NVIDIA CUDA 12.4 lib, bin, include

- copiez les fichiers de *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* vers *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'*

- copiez les fichiers de *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* vers *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'*

- copiez les fichiers de *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* vers *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'*

### **6. Télécharger Phi-3.5-mini-instruct-onnx**

   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. Exécuter InferencePhi35Instruct.ipynb**

   Ouvrez le [Notebook](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) et lancez l’exécution

![RESULT](../../../../../../translated_images/02.b9b06996cf7255d5.fr.png)

### **8. Compiler ORT GenAI GPU**

   ***Note*** 
   
   1. Veuillez désinstaller d’abord toutes les versions d’onnx, onnxruntime et onnxruntime-genai

   ```bash

   pip list 
   
   ```

   Ensuite, désinstallez toutes les bibliothèques onnxruntime, par exemple :

   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Vérifiez la prise en charge de l’extension Visual Studio

   Vérifiez dans C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras que le dossier C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration est présent. 
   
   S’il est absent, cherchez dans les autres dossiers du toolkit CUDA et copiez le dossier visual_studio_integration ainsi que son contenu dans C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration

   - Si vous ne souhaitez pas compiler, vous pouvez passer cette étape

   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - Téléchargez [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip)

   - Décompressez onnxruntime-win-x64-gpu-1.19.2.zip, renommez-le en **ort**, puis copiez le dossier ort dans onnxruntime-genai

   - Avec Windows Terminal, ouvrez Developer Command Prompt for VS 2022 et placez-vous dans onnxruntime-genai

![RESULT](../../../../../../translated_images/03.b83ce473d5ff9b9b.fr.png)

   - Compilez avec votre environnement Python

   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.