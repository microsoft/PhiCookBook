<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b066fc29c1b2129df84e027cb75119ce",
  "translation_date": "2025-10-11T12:05:53+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/ORTWindowGPUGuideline.md",
  "language_code": "et"
}
-->
# **Juhend OnnxRuntime GenAI Windows GPU jaoks**

See juhend sisaldab samme ONNX Runtime (ORT) seadistamiseks ja kasutamiseks GPU-dega Windowsis. Selle eesmärk on aidata teil kasutada GPU kiirendust oma mudelite jaoks, parandades jõudlust ja efektiivsust.

Dokument sisaldab juhiseid:

- Keskkonna seadistamine: Juhised vajalike sõltuvuste, nagu CUDA, cuDNN ja ONNX Runtime, installimiseks.
- Konfiguratsioon: Kuidas seadistada keskkonda ja ONNX Runtime'i, et kasutada GPU ressursse tõhusalt.
- Optimeerimisnõuanded: Soovitused GPU seadete peenhäälestamiseks parima jõudluse saavutamiseks.

### **1. Python 3.10.x /3.11.8**

   ***Märkus*** Soovitatav kasutada [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) kui Python keskkonda.

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***Meeldetuletus*** Kui olete installinud mõne ONNX Python teegi, desinstallige see esmalt.

### **2. Installige CMake wingetiga**

   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Installige Visual Studio 2022 - Desktop Development with C++**

   ***Märkus*** Kui te ei soovi kompileerida, võite selle sammu vahele jätta.

![CPP](../../../../../../imgs/02/pfonnx/01.png)

### **4. Installige NVIDIA draiver**

1. **NVIDIA GPU draiver**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***Meeldetuletus*** Kasutage installimisel vaikeseadeid.

### **5. Seadistage NVIDIA keskkond**

Kopeerige NVIDIA CUDNN 9.4 lib, bin, include kaustad NVIDIA CUDA 12.4 lib, bin, include kaustadesse.

- kopeerige *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* failid *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'* kausta.

- kopeerige *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* failid *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'* kausta.

- kopeerige *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* failid *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'* kausta.

### **6. Laadige alla Phi-3.5-mini-instruct-onnx**

   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. Käivitage InferencePhi35Instruct.ipynb**

   Avage [Notebook](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) ja käivitage.

![RESULT](../../../../../../imgs/02/pfonnx/02.png)

### **8. Kompileerige ORT GenAI GPU**

   ***Märkus*** 
   
   1. Desinstallige esmalt kõik ONNX, ONNX Runtime ja ONNX Runtime GenAI seotud teegid.

   ```bash

   pip list 
   
   ```

   Seejärel desinstallige kõik ONNX Runtime teegid, näiteks:

   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Kontrollige Visual Studio laienduse tuge.

   Kontrollige, kas kaust *C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras* sisaldab *visual_studio_integration* kausta. 

   Kui seda ei leidu, otsige teistest CUDA tööriistakomplekti draiveri kaustadest ja kopeerige *visual_studio_integration* kaust koos sisuga *C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration* kausta.

   - Kui te ei soovi kompileerida, võite selle sammu vahele jätta.

   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - Laadige alla [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip).

   - Pakkige lahti *onnxruntime-win-x64-gpu-1.19.2.zip*, nimetage see ümber **ort**-ks ja kopeerige *ort* kaust *onnxruntime-genai* kausta.

   - Kasutage Windows Terminali, avage VS 2022 arendaja käsuviip ja minge *onnxruntime-genai* kausta.

![RESULT](../../../../../../imgs/02/pfonnx/03.png)

   - Kompileerige see oma Python keskkonnas.

   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.