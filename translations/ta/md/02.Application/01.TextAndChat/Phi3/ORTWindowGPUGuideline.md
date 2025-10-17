<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b066fc29c1b2129df84e027cb75119ce",
  "translation_date": "2025-10-11T12:05:39+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/ORTWindowGPUGuideline.md",
  "language_code": "ta"
}
-->
# **OnnxRuntime GenAI Windows GPU க்கான வழிகாட்டுதல்**

இந்த வழிகாட்டுதல் Windows-ல் GPUக்களுடன் ONNX Runtime (ORT) அமைக்க மற்றும் பயன்படுத்துவதற்கான படிகளை வழங்குகிறது. உங்கள் மாதிரிகளுக்கான செயல்திறன் மற்றும் திறனைக் கூட்ட GPU வேகத்தைப் பயன்படுத்த உதவ இது வடிவமைக்கப்பட்டுள்ளது.

இந்த ஆவணம் கீழ்க்காணும் வழிகாட்டுதல்களை வழங்குகிறது:

- சூழல் அமைப்பு: CUDA, cuDNN மற்றும் ONNX Runtime போன்ற தேவையான சார்புகளை நிறுவுவதற்கான வழிமுறைகள்.
- கட்டமைப்பு: GPU வளங்களை பயனுள்ளதாக பயன்படுத்த சூழல் மற்றும் ONNX Runtime ஐ எப்படி அமைப்பது.
- மேம்படுத்தல் குறிப்புகள்: உச்ச செயல்திறனைப் பெற உங்கள் GPU அமைப்புகளை நன்றாகச் சரிசெய்வதற்கான ஆலோசனைகள்.

### **1. Python 3.10.x /3.11.8**

   ***குறிப்பு*** Python சூழலுக்காக [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) பயன்படுத்த பரிந்துரைக்கப்படுகிறது.

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***நினைவூட்டல்*** Python ONNX நூலகத்தை ஏதேனும் நிறுவியிருந்தால், தயவுசெய்து அதை அகற்றவும்.

### **2. winget மூலம் CMake ஐ நிறுவவும்**

   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Visual Studio 2022 - C++ உடன் Desktop Development ஐ நிறுவவும்**

   ***குறிப்பு*** நீங்கள் தொகுக்க விரும்பவில்லை என்றால், இந்த படியை தவிர்க்கலாம்.

![CPP](../../../../../../imgs/02/pfonnx/01.png)

### **4. NVIDIA டிரைவர் நிறுவவும்**

1. **NVIDIA GPU டிரைவர்** [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4** [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***நினைவூட்டல்*** நிறுவல் செயல்முறையில் இயல்புநிலை அமைப்புகளை பயன்படுத்தவும்.

### **5. NVIDIA சூழலை அமைக்கவும்**

NVIDIA CUDNN 9.4 lib, bin, include ஐ NVIDIA CUDA 12.4 lib, bin, include க்கு நகலெடுக்கவும்.

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* கோப்புகளை *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'* க்கு நகலெடுக்கவும்.

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* கோப்புகளை *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'* க்கு நகலெடுக்கவும்.

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* கோப்புகளை *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'* க்கு நகலெடுக்கவும்.

### **6. Phi-3.5-mini-instruct-onnx ஐ பதிவிறக்கவும்**

   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. InferencePhi35Instruct.ipynb ஐ இயக்கவும்**

   [Notebook](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) ஐ திறந்து செயல்படுத்தவும்.

![RESULT](../../../../../../imgs/02/pfonnx/02.png)

### **8. ORT GenAI GPU ஐ தொகுக்கவும்**

   ***குறிப்பு*** 
   
   1. முதலில் onnx, onnxruntime மற்றும் onnxruntime-genai பற்றிய அனைத்தையும் அகற்றவும்.

   ```bash

   pip list 
   
   ```

   பின்னர் அனைத்து onnxruntime நூலகங்களையும் அகற்றவும், உதாரணமாக:

   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Visual Studio Extension ஆதரவைச் சரிபார்க்கவும்.

   C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras ஐச் சரிபார்த்து, C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration காணப்படுகிறதா என்பதை உறுதிப்படுத்தவும்.

   காணப்படவில்லை என்றால், பிற CUDA toolkit டிரைவர் கோப்பகங்களைச் சரிபார்த்து, visual_studio_integration கோப்பகத்தையும் உள்ளடக்கங்களையும் C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration க்கு நகலெடுக்கவும்.

   - நீங்கள் தொகுக்க விரும்பவில்லை என்றால், இந்த படியை தவிர்க்கலாம்.

   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip) ஐ பதிவிறக்கவும்.

   - onnxruntime-win-x64-gpu-1.19.2.zip ஐ unzip செய்து, **ort** என பெயரிடவும், ort கோப்பகத்தை onnxruntime-genai க்கு நகலெடுக்கவும்.

   - Windows Terminal ஐப் பயன்படுத்தி, Developer Command Prompt for VS 2022 க்கு சென்று onnxruntime-genai க்கு செல்லவும்.

![RESULT](../../../../../../imgs/02/pfonnx/03.png)

   - உங்கள் Python சூழலுடன் அதை தொகுக்கவும்.

   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.