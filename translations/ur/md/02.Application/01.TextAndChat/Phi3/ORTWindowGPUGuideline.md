<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b066fc29c1b2129df84e027cb75119ce",
  "translation_date": "2025-07-17T02:39:27+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/ORTWindowGPUGuideline.md",
  "language_code": "ur"
}
-->
# **OnnxRuntime GenAI Windows GPU کے لیے رہنما اصول**

یہ رہنما اصول ونڈوز پر GPUs کے ساتھ ONNX Runtime (ORT) کو سیٹ اپ اور استعمال کرنے کے اقدامات فراہم کرتا ہے۔ یہ آپ کے ماڈلز کے لیے GPU کی تیز رفتاری کو استعمال کرنے میں مدد دینے کے لیے ڈیزائن کیا گیا ہے، جس سے کارکردگی اور مؤثریت بہتر ہوتی ہے۔

دستاویز میں درج ذیل رہنمائی شامل ہے:

- ماحول کی ترتیب: CUDA، cuDNN، اور ONNX Runtime جیسی ضروری dependencies انسٹال کرنے کی ہدایات۔
- ترتیب: ماحول اور ONNX Runtime کو GPU وسائل مؤثر طریقے سے استعمال کرنے کے لیے کیسے ترتیب دیا جائے۔
- اصلاحی نکات: بہترین کارکردگی کے لیے GPU کی ترتیبات کو بہتر بنانے کے مشورے۔

### **1. Python 3.10.x /3.11.8**

   ***Note*** اپنے Python ماحول کے لیے [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) استعمال کرنے کی تجویز دی جاتی ہے۔

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***Reminder*** اگر آپ نے Python ONNX لائبریری انسٹال کی ہے تو براہ کرم اسے ان انسٹال کریں۔

### **2. winget کے ذریعے CMake انسٹال کریں**


   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Visual Studio 2022 - Desktop Development with C++ انسٹال کریں**

   ***Note*** اگر آپ کمپائل نہیں کرنا چاہتے تو اس مرحلے کو چھوڑ سکتے ہیں۔

![CPP](../../../../../../translated_images/ur/01.42f52a2b2aedff02.png)


### **4. NVIDIA ڈرائیور انسٹال کریں**

1. **NVIDIA GPU Driver**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***Reminder*** انسٹالیشن کے دوران ڈیفالٹ سیٹنگز استعمال کریں۔

### **5. NVIDIA ماحول سیٹ کریں**

NVIDIA CUDNN 9.4 کے lib، bin، include فولڈرز کو NVIDIA CUDA 12.4 کے lib، bin، include فولڈرز میں کاپی کریں۔

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* کی فائلیں *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'* میں کاپی کریں۔

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* کی فائلیں *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'* میں کاپی کریں۔

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* کی فائلیں *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'* میں کاپی کریں۔

### **6. Phi-3.5-mini-instruct-onnx ڈاؤن لوڈ کریں**


   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. InferencePhi35Instruct.ipynb چلائیں**

   [نوٹ بک](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) کھولیں اور اسے چلائیں۔

![RESULT](../../../../../../translated_images/ur/02.b9b06996cf7255d5.png)


### **8. ORT GenAI GPU کمپائل کریں**


   ***Note*** 
   
   1. براہ کرم سب سے پہلے onnx، onnxruntime، اور onnxruntime-genai سے متعلق تمام پیکجز ان انسٹال کریں۔

   
   ```bash

   pip list 
   
   ```

   پھر تمام onnxruntime لائبریریز ان انسٹال کریں، مثلاً:


   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Visual Studio ایکسٹینشن کی سپورٹ چیک کریں۔

   چیک کریں کہ C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras میں C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration فولڈر موجود ہو۔ 
   
   اگر نہیں ملے تو دوسرے CUDA toolkit ڈرائیور فولڈرز چیک کریں اور visual_studio_integration فولڈر اور اس کے مواد کو C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration میں کاپی کریں۔




   - اگر آپ کمپائل نہیں کرنا چاہتے تو اس مرحلے کو چھوڑ سکتے ہیں۔


   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip) ڈاؤن لوڈ کریں۔

   - onnxruntime-win-x64-gpu-1.19.2.zip کو ان زپ کریں، اور اسے **ort** کے نام سے ری نیم کریں، پھر ort فولڈر کو onnxruntime-genai میں کاپی کریں۔

   - Windows Terminal استعمال کرتے ہوئے، VS 2022 کے Developer Command Prompt پر جائیں اور onnxruntime-genai فولڈر میں جائیں۔

![RESULT](../../../../../../translated_images/ur/03.b83ce473d5ff9b9b.png)

   - اسے اپنے Python ماحول کے ساتھ کمپائل کریں۔

   
   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔