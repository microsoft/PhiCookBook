<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b066fc29c1b2129df84e027cb75119ce",
  "translation_date": "2025-12-21T21:05:56+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/ORTWindowGPUGuideline.md",
  "language_code": "pcm"
}
-->
# **Guideline for OnnxRuntime GenAI  Windows GPU**

Dis guide dey show steps for how to set up an use ONNX Runtime (ORT) wit GPU for Windows. E dey designed to help you use GPU acceleration for your models, make performance and efficiency better.

The document dey give guidance on:

- Environment Setup: How to install wetin you need like CUDA, cuDNN, and ONNX Runtime.
- Configuration: How to set the environment an ONNX Runtime make dem use GPU resources well.
- Optimization Tips: Tips on how to tune your GPU settings make dem give best performance.

### **1. Python 3.10.x /3.11.8**

   ***Note*** Make you use [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) as your Python env

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***Reminder*** If you don install any python ONNX library before, abeg uninstall am

### **2. Install CMake with winget**


   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Install Visual Studio 2022 - Desktop Development with C++**

   ***Note*** If you no wan compile you fit skip this step

![CPP](../../../../../../translated_images/01.42f52a2b2aedff029e1c9beb13d2b09fcdab284ffd5fa8f3d7ac3cef5f347ad2.pcm.png)


### **4. Install NVIDIA Driver**

1. **NVIDIA GPU Driver**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***Reminder*** Abeg use default settings during the installation flow 

### **5. Set NVIDIA Env**

Copy NVIDIA CUDNN 9.4 lib,bin,include to NVIDIA CUDA 12.4 lib,bin,include

- copy *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* files to  *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin*

- copy *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* files to  *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include*

- copy *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* files to  *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'*


### **6. Download Phi-3.5-mini-instruct-onnx**


   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. Runing InferencePhi35Instruct.ipynb**

   Open [Notebook](../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) and run am


![RESULT](../../../../../../translated_images/02.b9b06996cf7255d5e5ee19a703c4352f4a96dd7a1068b2af227eda1f3104bfa0.pcm.png)


### **8. Compile ORT GenAI GPU**


   ***Note*** 
   
   1. Abeg uninstall any onnx, onnxruntime and onnxruntime-genai first

   
   ```bash

   pip list 
   
   ```

   After dat uninstall all onnxruntime libraries i.e. 


   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Check Visual Studio Extension support 

   Check C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras make sure C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration dey. 
   
   If you no see am check other Cuda toolkit driver folders and copy the visual_studio_integration folder and contents to C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration




   - If you no wan compile you fit skip this step


   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - Download [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip)

   - Unzip onnxruntime-win-x64-gpu-1.19.2.zip ,and rename am to **ort**, copy ort folder to onnxruntime-genai

   - Using Windows Terminal, go to Developer Command Prompt for VS 2022 and go to onnxruntime-genai 

![RESULT](../../../../../../translated_images/03.b83ce473d5ff9b9b94670a1b26fdb66a05320d534cbee2762f64e52fd12ef9c9.pcm.png)

   - Compile am with your python env

   
   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document na AI translation do (Co-op Translator: https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say machine translations fit get mistakes or no too accurate. The original document for im original language na the correct one wey you suppose consider as the authority. If na important information, better make professional human translator check am. We no go responsible for any misunderstanding or wrong interpretation wey fit happen because of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->