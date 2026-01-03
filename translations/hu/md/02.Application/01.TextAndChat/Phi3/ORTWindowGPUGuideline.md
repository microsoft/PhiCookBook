<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b066fc29c1b2129df84e027cb75119ce",
  "translation_date": "2025-07-17T02:46:26+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/ORTWindowGPUGuideline.md",
  "language_code": "hu"
}
-->
# **Útmutató az OnnxRuntime GenAI Windows GPU használatához**

Ez az útmutató lépéseket tartalmaz az ONNX Runtime (ORT) GPU-val történő használatának beállításához Windows rendszeren. Célja, hogy segítsen kihasználni a GPU gyorsítását a modellekhez, javítva a teljesítményt és a hatékonyságot.

A dokumentum az alábbiakról nyújt tájékoztatást:

- Környezet beállítása: Útmutató a szükséges függőségek, például CUDA, cuDNN és ONNX Runtime telepítéséhez.
- Konfiguráció: Hogyan állítsuk be a környezetet és az ONNX Runtime-ot a GPU erőforrások hatékony kihasználásához.
- Optimalizálási tippek: Tanácsok a GPU beállítások finomhangolásához a legjobb teljesítmény érdekében.

### **1. Python 3.10.x /3.11.8**

   ***Megjegyzés*** Javasolt a [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) használata Python környezetként

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***Emlékeztető*** Ha telepítettél bármilyen python ONNX könyvtárat, kérlek távolítsd el

### **2. CMake telepítése winget segítségével**

   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Visual Studio 2022 telepítése - Desktop Development with C++**

   ***Megjegyzés*** Ha nem szeretnél fordítani, ezt a lépést kihagyhatod

![CPP](../../../../../../translated_images/01.42f52a2b2aedff02.hu.png)

### **4. NVIDIA Driver telepítése**

1. **NVIDIA GPU Driver**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***Emlékeztető*** Kérlek, az alapértelmezett beállításokat használd a telepítés során

### **5. NVIDIA környezet beállítása**

Másold át az NVIDIA CUDNN 9.4 lib, bin, include fájlokat az NVIDIA CUDA 12.4 lib, bin, include mappákba

- Másold a *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* fájlokat a *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'* mappába

- Másold a *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* fájlokat a *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'* mappába

- Másold a *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* fájlokat a *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'* mappába

### **6. Phi-3.5-mini-instruct-onnx letöltése**

   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. InferencePhi35Instruct.ipynb futtatása**

   Nyisd meg a [Notebookot](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) és futtasd

![RESULT](../../../../../../translated_images/02.b9b06996cf7255d5.hu.png)

### **8. ORT GenAI GPU fordítása**

   ***Megjegyzés*** 
   
   1. Először távolíts el minden onnx, onnxruntime és onnxruntime-genai csomagot

   ```bash

   pip list 
   
   ```

   Ezután távolíts el minden onnxruntime könyvtárat, például

   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Ellenőrizd a Visual Studio kiterjesztés támogatását

   Nézd meg a C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras mappát, hogy megtalálható-e a C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration mappa. 

   Ha nem találod, keresd meg más CUDA toolkit driver mappákban, majd másold át a visual_studio_integration mappát és tartalmát a C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration helyre

   - Ha nem szeretnél fordítani, ezt a lépést kihagyhatod

   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - Töltsd le a [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip) fájlt

   - Csomagold ki az onnxruntime-win-x64-gpu-1.19.2.zip fájlt, nevezd át **ort**-ra, majd másold az ort mappát az onnxruntime-genai könyvtárba

   - Windows Terminalban nyisd meg a Developer Command Prompt for VS 2022-t, majd lépj be az onnxruntime-genai mappába

![RESULT](../../../../../../translated_images/03.b83ce473d5ff9b9b.hu.png)

   - Fordítsd le a projektet a python környezeteddel

   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.