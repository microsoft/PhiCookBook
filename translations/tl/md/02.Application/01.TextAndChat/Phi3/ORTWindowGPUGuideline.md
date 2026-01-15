<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b066fc29c1b2129df84e027cb75119ce",
  "translation_date": "2025-07-17T02:45:56+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/ORTWindowGPUGuideline.md",
  "language_code": "tl"
}
-->
# **Patnubay para sa OnnxRuntime GenAI Windows GPU**

Ang patnubay na ito ay naglalaman ng mga hakbang para sa pag-setup at paggamit ng ONNX Runtime (ORT) gamit ang mga GPU sa Windows. Layunin nitong tulungan kang magamit ang GPU acceleration para sa iyong mga modelo, upang mapabuti ang performance at kahusayan.

Ang dokumentong ito ay nagbibigay ng gabay sa:

- Pagsasaayos ng Kapaligiran: Mga tagubilin sa pag-install ng mga kinakailangang dependencies tulad ng CUDA, cuDNN, at ONNX Runtime.
- Konfigurasyon: Paano i-configure ang kapaligiran at ONNX Runtime upang epektibong magamit ang mga GPU resources.
- Mga Tip sa Pag-optimize: Mga payo kung paano i-fine-tune ang iyong mga GPU settings para sa pinakamainam na performance.

### **1. Python 3.10.x /3.11.8**

   ***Note*** Inirerekomenda ang paggamit ng [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) bilang iyong Python environment

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***Reminder*** Kung may naka-install kang anumang python ONNX library, pakibura muna ito

### **2. I-install ang CMake gamit ang winget**

   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. I-install ang Visual Studio 2022 - Desktop Development with C++**

   ***Note*** Kung ayaw mong mag-compile, maaari mong laktawan ang hakbang na ito

![CPP](../../../../../../translated_images/tl/01.42f52a2b2aedff02.png)

### **4. I-install ang NVIDIA Driver**

1. **NVIDIA GPU Driver**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***Reminder*** Gamitin ang default na mga setting sa proseso ng pag-install

### **5. I-set ang NVIDIA Env**

Kopyahin ang NVIDIA CUDNN 9.4 lib, bin, include papunta sa NVIDIA CUDA 12.4 lib, bin, include

- kopyahin ang mga file mula sa *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* papunta sa *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'*

- kopyahin ang mga file mula sa *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* papunta sa *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'*

- kopyahin ang mga file mula sa *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* papunta sa *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'*

### **6. I-download ang Phi-3.5-mini-instruct-onnx**

   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. Patakbuhin ang InferencePhi35Instruct.ipynb**

   Buksan ang [Notebook](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) at i-execute

![RESULT](../../../../../../translated_images/tl/02.b9b06996cf7255d5.png)

### **8. I-compile ang ORT GenAI GPU**

   ***Note*** 
   
   1. Pakibura muna lahat ng onnx, onnxruntime, at onnxruntime-genai na naka-install

   ```bash

   pip list 
   
   ```

   Pagkatapos ay burahin lahat ng onnxruntime libraries tulad ng

   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Suriin ang suporta ng Visual Studio Extension

   Tingnan ang C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras upang matiyak na nandiyan ang C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration. 
   
   Kung wala, tingnan ang ibang mga folder ng Cuda toolkit driver at kopyahin ang folder na visual_studio_integration kasama ang mga laman nito papunta sa C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration

   - Kung ayaw mong mag-compile, maaari mong laktawan ang hakbang na ito

   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - I-download ang [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip)

   - I-unzip ang onnxruntime-win-x64-gpu-1.19.2.zip, palitan ang pangalan nito sa **ort**, at kopyahin ang folder na ort papunta sa onnxruntime-genai

   - Gamit ang Windows Terminal, pumunta sa Developer Command Prompt para sa VS 2022 at pumunta sa onnxruntime-genai

![RESULT](../../../../../../translated_images/tl/03.b83ce473d5ff9b9b.png)

   - I-compile ito gamit ang iyong python environment

   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.