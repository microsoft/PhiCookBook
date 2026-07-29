# **OnnxRuntime GenAI Windows GPU 指南**

本指南提供了在 Windows 平台上使用 GPU 設定與使用 ONNX Runtime (ORT) 的步驟。旨在幫助您利用 GPU 加速模型，提高效能與效率。

本文件涵蓋指引包括：

- 環境設定：安裝必要依賴如 CUDA、cuDNN 及 ONNX Runtime 的說明。
- 配置：如何有效配置環境與 ONNX Runtime 以利用 GPU 資源。
- 優化建議：有關調整 GPU 設定以達最佳效能的建議。

### **1. Python 3.10.x /3.11.8**

   <strong><em>注意</em></strong> 建議使用 [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) 作為您的 Python 環境

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   <strong><em>提醒</em></strong> 如果您安裝過任何關於 python ONNX 的套件，請先將其卸載

### **2. 使用 winget 安裝 CMake**


   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. 安裝 Visual Studio 2022 - 使用 C++ 的桌面開發**

   <strong><em>注意</em></strong> 若不需自行編譯可跳過此步驟

![CPP](../../../../../../translated_images/zh-MO/01.42f52a2b2aedff02.webp)


### **4. 安裝 NVIDIA 驅動程式**

1. **NVIDIA GPU 驅動程式**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

<strong><em>提醒</em></strong> 請使用預設設定進行安裝流程 

### **5. 設定 NVIDIA 環境**

將 NVIDIA CUDNN 9.4 的 lib、bin、include 複製到 NVIDIA CUDA 12.4 的相對應目錄

- 複製 *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* 目錄內的檔案至 *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'*

- 複製 *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* 目錄內的檔案至 *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'*

- 複製 *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* 目錄內的檔案至 *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'*


### **6. 下載 Phi-3.5-mini-instruct-onnx**


   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. 執行 InferencePhi35Instruct.ipynb**

   開啟 [Notebook](../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) 並執行


![RESULT](../../../../../../translated_images/zh-MO/02.b9b06996cf7255d5.webp)


### **8. 編譯 ORT GenAI GPU**


   <strong><em>注意</em></strong> 
   
   1. 請先卸載所有關於 onnx、onnxruntime 及 onnxruntime-genai 的套件

   
   ```bash

   pip list 
   
   ```

   接著卸載所有 onnxruntime 套件，例如 


   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. 檢查 Visual Studio 擴充功能支援 

   檢查 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras，確認存在 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration
   
   若未找到，檢查其他 Cuda Toolkit 驅動程式資料夾並將 visual_studio_integration 資料夾及內容複製到 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration




   - 若不需要編譯，此步驟可跳過


   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - 下載 [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip)

   - 解壓 onnxruntime-win-x64-gpu-1.19.2.zip，並將資料夾重新命名為 **ort**，將 ort 資料夾複製到 onnxruntime-genai

   - 使用 Windows Terminal，開啟 VS 2022 的開發人員命令提示字元，並切換到 onnxruntime-genai 資料夾

![RESULT](../../../../../../translated_images/zh-MO/03.b83ce473d5ff9b9b.webp)

   - 以您的 python 環境進行編譯

   
   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->