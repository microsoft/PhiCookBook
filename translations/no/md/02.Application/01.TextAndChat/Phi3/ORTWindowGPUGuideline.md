<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b066fc29c1b2129df84e027cb75119ce",
  "translation_date": "2025-05-09T18:44:24+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/ORTWindowGPUGuideline.md",
  "language_code": "no"
}
-->
# **Retningslinje for OnnxRuntime GenAI Windows GPU**

Denne retningslinjen gir trinn for å sette opp og bruke ONNX Runtime (ORT) med GPUer på Windows. Den er laget for å hjelpe deg med å utnytte GPU-akselerasjon for modellene dine, og dermed forbedre ytelse og effektivitet.

Dokumentet gir veiledning om:

- Miljøoppsett: Instruksjoner for installasjon av nødvendige avhengigheter som CUDA, cuDNN og ONNX Runtime.
- Konfigurasjon: Hvordan konfigurere miljøet og ONNX Runtime for effektiv bruk av GPU-ressurser.
- Optimaliseringstips: Råd om hvordan du finjusterer GPU-innstillingene for best mulig ytelse.

### **1. Python 3.10.x /3.11.8**

   ***Note*** Anbefaler å bruke [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) som ditt Python-miljø

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***Reminder*** Hvis du har installert noen Python ONNX-biblioteker, vennligst avinstaller dem

### **2. Installer CMake med winget**


   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Installer Visual Studio 2022 - Desktop Development med C++**

   ***Note*** Hvis du ikke ønsker å kompilere, kan du hoppe over dette steget

![CPP](../../../../../../translated_images/01.8964c1fa47e00dc36af710b967e72dd2f8a2be498e49c8d4c65c11ba105dedf8.no.png)


### **4. Installer NVIDIA-driver**

1. **NVIDIA GPU-driver**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***Reminder*** Vennligst bruk standardinnstillinger under installasjonen

### **5. Sett NVIDIA-miljø**

Kopier NVIDIA CUDNN 9.4 lib, bin, include til NVIDIA CUDA 12.4 lib, bin, include

- kopier *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* filer til  *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'*

- kopier *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* filer til  *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'*

- kopier *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* filer til  *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'*


### **6. Last ned Phi-3.5-mini-instruct-onnx**


   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. Kjør InferencePhi35Instruct.ipynb**

   Åpne [Notebook](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) og kjør 


![RESULT](../../../../../../translated_images/02.be96d16e7b1007f1f3941f65561553e62ccbd49c962f3d4a9154b8326c033ec1.no.png)


### **8. Kompiler ORT GenAI GPU**


   ***Note*** 
   
   1. Avinstaller først alle onnx, onnxruntime og onnxruntime-genai pakker

   
   ```bash

   pip list 
   
   ```

   Avinstaller deretter alle onnxruntime-biblioteker, for eksempel 


   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Sjekk støtte for Visual Studio-utvidelser

   Sjekk at C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras inneholder mappen C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration. 
   
   Hvis den ikke finnes, sjekk andre CUDA toolkit-driver-mapper og kopier visual_studio_integration-mappen og innholdet til C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration




   - Hvis du ikke ønsker å kompilere, kan du hoppe over dette steget


   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - Last ned [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip)

   - Pakk ut onnxruntime-win-x64-gpu-1.19.2.zip, gi mappen navnet **ort**, og kopier ort-mappen til onnxruntime-genai

   - Bruk Windows Terminal, åpne Developer Command Prompt for VS 2022 og gå til onnxruntime-genai 

![RESULT](../../../../../../translated_images/03.53bb08e3bde53edd1735c5546fb32b9b0bdba93d8241c5e6e3196d8bc01adbd7.no.png)

   - Kompiler med ditt Python-miljø

   
   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på det opprinnelige språket bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.