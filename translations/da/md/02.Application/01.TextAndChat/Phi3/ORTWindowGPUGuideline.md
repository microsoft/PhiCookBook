<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b066fc29c1b2129df84e027cb75119ce",
  "translation_date": "2025-05-09T18:44:13+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/ORTWindowGPUGuideline.md",
  "language_code": "da"
}
-->
# **Retningslinje for OnnxRuntime GenAI Windows GPU**

Denne retningslinje giver trin til opsætning og brug af ONNX Runtime (ORT) med GPU’er på Windows. Den er designet til at hjælpe dig med at udnytte GPU-acceleration for dine modeller og dermed forbedre ydeevne og effektivitet.

Dokumentet indeholder vejledning om:

- Miljøopsætning: Instruktioner til installation af nødvendige afhængigheder som CUDA, cuDNN og ONNX Runtime.
- Konfiguration: Hvordan man konfigurerer miljøet og ONNX Runtime til effektiv udnyttelse af GPU-ressourcer.
- Optimeringstips: Råd om, hvordan du finjusterer dine GPU-indstillinger for optimal ydeevne.

### **1. Python 3.10.x /3.11.8**

   ***Note*** Vi anbefaler at bruge [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) som dit Python-miljø

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***Reminder*** Hvis du har installeret nogen python ONNX-biblioteker, så afinstaller dem venligst

### **2. Installér CMake med winget**

   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Installér Visual Studio 2022 - Desktopudvikling med C++**

   ***Note*** Hvis du ikke ønsker at kompilere, kan du springe dette trin over

![CPP](../../../../../../translated_images/01.8964c1fa47e00dc36af710b967e72dd2f8a2be498e49c8d4c65c11ba105dedf8.da.png)

### **4. Installér NVIDIA-driver**

1. **NVIDIA GPU Driver**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***Reminder*** Brug venligst standardindstillingerne under installationen

### **5. Sæt NVIDIA-miljø**

Kopier NVIDIA CUDNN 9.4 lib, bin, include til NVIDIA CUDA 12.4 lib, bin, include

- kopier *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* filer til  *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin*

- kopier *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* filer til  *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include*

- kopier *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* filer til  *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'*

### **6. Download Phi-3.5-mini-instruct-onnx**

   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. Kør InferencePhi35Instruct.ipynb**

   Åbn [Notebook](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) og kør den

![RESULT](../../../../../../translated_images/02.be96d16e7b1007f1f3941f65561553e62ccbd49c962f3d4a9154b8326c033ec1.da.png)

### **8. Kompiler ORT GenAI GPU**

   ***Note*** 
   
   1. Afinstaller venligst først alle onnx, onnxruntime og onnxruntime-genai pakker

   ```bash

   pip list 
   
   ```

   Afinstaller derefter alle onnxruntime-biblioteker, f.eks.

   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Tjek Visual Studio Extension support

   Tjek i C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras om mappen C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration findes. 
   
   Hvis den ikke findes, så kig i andre Cuda toolkit driver-mapper og kopier mappen visual_studio_integration og dens indhold til C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration

   - Hvis du ikke ønsker at kompilere, kan du springe dette trin over

   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - Download [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip)

   - Pak onnxruntime-win-x64-gpu-1.19.2.zip ud, omdøb mappen til **ort**, og kopier ort-mappen til onnxruntime-genai

   - Brug Windows Terminal, åbn Developer Command Prompt for VS 2022 og gå til onnxruntime-genai

![RESULT](../../../../../../translated_images/03.53bb08e3bde53edd1735c5546fb32b9b0bdba93d8241c5e6e3196d8bc01adbd7.da.png)

   - Kompiler med dit python-miljø

   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

**Ansvarsfraskrivelse**:  
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.