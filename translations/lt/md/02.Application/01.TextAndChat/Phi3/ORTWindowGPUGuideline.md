# **Gairės OnnxRuntime GenAI Windows GPU**

Šios gairės pateikia žingsnius, kaip nustatyti ir naudoti ONNX Runtime (ORT) su GPU Windows aplinkoje. Jos skirtos padėti jums pasinaudoti GPU pagreičiu, siekiant pagerinti modelių našumą ir efektyvumą.

Dokumente pateikiama informacija apie:

- Aplinkos nustatymą: Instrukcijos, kaip įdiegti reikalingas priklausomybes, tokias kaip CUDA, cuDNN ir ONNX Runtime.
- Konfigūraciją: Kaip sukonfigūruoti aplinką ir ONNX Runtime, kad efektyviai naudotų GPU resursus.
- Optimizavimo patarimus: Rekomendacijos, kaip geriausiai sureguliuoti GPU nustatymus, siekiant optimalaus našumo.

### **1. Python 3.10.x /3.11.8**

   ***Pastaba*** Rekomenduojama naudoti [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) kaip Python aplinką.

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***Primename*** Jei jau įdiegėte bet kokią Python ONNX biblioteką, ją pašalinkite.

### **2. Įdiekite CMake su winget**

   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Įdiekite Visual Studio 2022 - Desktop Development with C++**

   ***Pastaba*** Jei nenorite kompiliuoti, galite praleisti šį žingsnį.

![CPP](../../../../../../imgs/02/pfonnx/01.png)

### **4. Įdiekite NVIDIA tvarkyklę**

1. **NVIDIA GPU tvarkyklė** [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4** [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***Primename*** Naudokite numatytuosius nustatymus diegimo metu.

### **5. Nustatykite NVIDIA aplinką**

Kopijuokite NVIDIA CUDNN 9.4 lib, bin, include į NVIDIA CUDA 12.4 lib, bin, include.

- kopijuokite *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* failus į *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin*

- kopijuokite *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* failus į *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include*

- kopijuokite *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* failus į *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'*

### **6. Atsisiųskite Phi-3.5-mini-instruct-onnx**

   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. Vykdykite InferencePhi35Instruct.ipynb**

   Atidarykite [Notebook](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) ir vykdykite.

![RESULT](../../../../../../imgs/02/pfonnx/02.png)

### **8. Kompiliuokite ORT GenAI GPU**

   ***Pastaba*** 

   1. Pirmiausia pašalinkite visas onnx, onnxruntime ir onnxruntime-genai bibliotekas.

   ```bash

   pip list 
   
   ```

   Tada pašalinkite visas onnxruntime bibliotekas, pvz.:

   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Patikrinkite Visual Studio Extension palaikymą.

   Patikrinkite C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras, kad įsitikintumėte, jog C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration yra. 

   Jei nerandate, patikrinkite kitus CUDA įrankių rinkinio tvarkyklės aplankus ir nukopijuokite visual_studio_integration aplanką bei jo turinį į C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration.

   - Jei nenorite kompiliuoti, galite praleisti šį žingsnį.

   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - Atsisiųskite [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip)

   - Išskleiskite onnxruntime-win-x64-gpu-1.19.2.zip, pervadinkite į **ort**, nukopijuokite ort aplanką į onnxruntime-genai.

   - Naudodami Windows Terminal, eikite į Developer Command Prompt for VS 2022 ir pereikite į onnxruntime-genai.

![RESULT](../../../../../../imgs/02/pfonnx/03.png)

   - Kompiliuokite naudodami savo Python aplinką.

   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.