# **OnnxRuntime GenAI Windows GPU 指南**

本指南提供在 Windows 上使用帶有 GPU 的 ONNX Runtime (ORT) 的設置和使用步驟。旨在幫助您利用 GPU 加速模型，提升效能與效率。

文件指導內容包括：

- 環境設置：安裝 CUDA、cuDNN 及 ONNX Runtime 等必要依賴的說明。
- 配置：如何配置環境與 ONNX Runtime 以有效利用 GPU 資源。
- 優化建議：如何微調 GPU 設定以獲得最佳效能的建議。

### **1. Python 3.10.x /3.11.8**

   <strong><em>注意</em></strong> 建議使用 [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) 作為您的 Python 環境

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   <strong><em>提醒</em></strong> 如果安裝過任何 python ONNX 函式庫，請先卸載

### **2. 使用 winget 安裝 CMake**


   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. 安裝 Visual Studio 2022 - C++ 桌面開發**

   <strong><em>注意</em></strong> 如果不需要編譯，可以跳過此步驟

![CPP](../../../../../../translated_images/zh-TW/01.42f52a2b2aedff02.webp)


### **4. 安裝 NVIDIA 驅動程序**

1. **NVIDIA GPU 驅動程序**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

<strong><em>提醒</em></strong> 請使用安裝流程中的預設設定

### **5. 設置 NVIDIA 環境變數**

將 NVIDIA CUDNN 9.4 的 lib、bin、include 複製到 NVIDIA CUDA 12.4 的 lib、bin、include 目錄

- 將 *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* 下的文件複製到  *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin*

- 將 *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* 下的文件複製到  *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include*

- 將 *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* 下的文件複製到  *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'*


### **6. 下載 Phi-3.5-mini-instruct-onnx**


   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. 執行 InferencePhi35Instruct.ipynb**

   開啟 [Notebook](../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) 並執行 


![RESULT](../../../../../../translated_images/zh-TW/02.b9b06996cf7255d5.webp)


### **8. 編譯 ORT GenAI GPU**


   <strong><em>注意</em></strong> 
   
   1. 請先卸載所有跟 onnx、onnxruntime 及 onnxruntime-genai 有關的套件

   
   ```bash

   pip list 
   
   ```

   之後卸載所有 onnxruntime 函式庫，例如


   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. 檢查 Visual Studio 擴充支援 

   確認 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras 目錄下存在 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration
   
   若未找到，請檢查其他 Cuda 工具包驅動資料夾，將 visual_studio_integration 資料夾及內容複製到 C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration




   - 如果不想編譯，可以跳過此步驟


   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - 下載 [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip)

   - 解壓 onnxruntime-win-x64-gpu-1.19.2.zip，並將資料夾重命名為 **ort** ，將 ort 資料夾複製到 onnxruntime-genai

   - 使用 Windows Terminal，切換至 VS 2022 的 Developer Command Prompt，並進入 onnxruntime-genai 目錄

![RESULT](../../../../../../translated_images/zh-TW/03.b83ce473d5ff9b9b.webp)

   - 使用您的 python 環境編譯

   
   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->