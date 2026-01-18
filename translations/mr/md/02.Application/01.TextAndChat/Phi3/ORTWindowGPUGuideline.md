<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b066fc29c1b2129df84e027cb75119ce",
  "translation_date": "2025-07-17T02:41:34+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/ORTWindowGPUGuideline.md",
  "language_code": "mr"
}
-->
# **OnnxRuntime GenAI Windows GPU साठी मार्गदर्शक**

हा मार्गदर्शक Windows वर GPU सह ONNX Runtime (ORT) सेटअप आणि वापरण्याच्या पायऱ्या देतो. यामुळे तुम्हाला तुमच्या मॉडेलसाठी GPU वेग वाढवण्याचा फायदा घेता येईल, ज्यामुळे कामगिरी आणि कार्यक्षमता सुधारेल.

हे दस्तऐवज खालील बाबींवर मार्गदर्शन करतो:

- पर्यावरण सेटअप: CUDA, cuDNN आणि ONNX Runtime सारख्या आवश्यक अवलंबनांची स्थापना कशी करावी याचे निर्देश.
- कॉन्फिगरेशन: GPU संसाधने प्रभावीपणे वापरण्यासाठी पर्यावरण आणि ONNX Runtime कसे कॉन्फिगर करावे.
- ऑप्टिमायझेशन टिप्स: सर्वोत्तम कामगिरीसाठी GPU सेटिंग्ज कशा सुधाराव्यात याबाबत सल्ला.

### **1. Python 3.10.x /3.11.8**

   ***Note*** तुमच्या Python पर्यावरणासाठी [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) वापरण्याचा सल्ला दिला आहे

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***Reminder*** जर तुम्ही Python ONNX लायब्ररी आधीच इन्स्टॉल केली असेल तर ती अनइन्स्टॉल करा

### **2. winget वापरून CMake इन्स्टॉल करा**

   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Visual Studio 2022 - Desktop Development with C++ इन्स्टॉल करा**

   ***Note*** जर तुम्हाला कंपाईल करायचे नसेल तर हा टप्पा वगळू शकता

![CPP](../../../../../../translated_images/mr/01.42f52a2b2aedff02.webp)

### **4. NVIDIA ड्रायव्हर इन्स्टॉल करा**

1. **NVIDIA GPU Driver**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***Reminder*** इन्स्टॉलेशन प्रक्रियेत डीफॉल्ट सेटिंग्ज वापरा

### **5. NVIDIA पर्यावरण सेट करा**

NVIDIA CUDNN 9.4 च्या lib, bin, include फोल्डरमधील फायली NVIDIA CUDA 12.4 च्या lib, bin, include मध्ये कॉपी करा

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* मधील फायली *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'* मध्ये कॉपी करा

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* मधील फायली *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'* मध्ये कॉपी करा

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* मधील फायली *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'* मध्ये कॉपी करा

### **6. Phi-3.5-mini-instruct-onnx डाउनलोड करा**

   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. InferencePhi35Instruct.ipynb चालवा**

   [Notebook](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) उघडा आणि चालवा

![RESULT](../../../../../../translated_images/mr/02.b9b06996cf7255d5.webp)

### **8. ORT GenAI GPU कंपाईल करा**

   ***Note*** 
   
   1. सर्व onnx, onnxruntime आणि onnxruntime-genai आधी अनइन्स्टॉल करा

   ```bash

   pip list 
   
   ```

   नंतर सर्व onnxruntime लायब्ररी अनइन्स्टॉल करा, उदा. 

   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Visual Studio Extension सपोर्ट तपासा

   C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras मध्ये जाऊन तपासा की C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration आहे का. 

   नसेल तर इतर CUDA toolkit ड्रायव्हर फोल्डरमध्ये तपासा आणि visual_studio_integration फोल्डर आणि त्यातील फायली C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration मध्ये कॉपी करा

   - जर तुम्हाला कंपाईल करायचे नसेल तर हा टप्पा वगळू शकता

   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip) डाउनलोड करा

   - onnxruntime-win-x64-gpu-1.19.2.zip अनझिप करा, त्याचे नाव **ort** असे बदला आणि ort फोल्डर onnxruntime-genai मध्ये कॉपी करा

   - Windows Terminal वापरून Developer Command Prompt for VS 2022 मध्ये जा आणि onnxruntime-genai फोल्डरमध्ये जा

![RESULT](../../../../../../translated_images/mr/03.b83ce473d5ff9b9b.webp)

   - तुमच्या Python पर्यावरणासह ते कंपाईल करा

   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेचा अभाव असू शकतो. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.