<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b066fc29c1b2129df84e027cb75119ce",
  "translation_date": "2025-03-27T11:01:58+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\ORTWindowGPUGuideline.md",
  "language_code": "fa"
}
-->
# **راهنمای استفاده از OnnxRuntime GenAI در ویندوز با GPU**

این راهنما مراحل تنظیم و استفاده از ONNX Runtime (ORT) با GPU در ویندوز را ارائه می‌دهد. هدف آن کمک به شما در استفاده از شتاب‌دهنده GPU برای مدل‌هایتان و بهبود عملکرد و کارایی است.

این سند شامل موارد زیر است:

- تنظیم محیط: دستورالعمل‌هایی برای نصب وابستگی‌های ضروری مانند CUDA، cuDNN و ONNX Runtime.
- پیکربندی: نحوه پیکربندی محیط و ONNX Runtime برای استفاده بهینه از منابع GPU.
- نکات بهینه‌سازی: توصیه‌هایی برای تنظیم GPU جهت دستیابی به عملکرد بهتر.

### **1. Python 3.10.x /3.11.8**

   ***توجه*** پیشنهاد می‌شود از [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) به عنوان محیط Python خود استفاده کنید.

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***یادآوری*** اگر قبلاً کتابخانه‌ای مرتبط با ONNX Python نصب کرده‌اید، لطفاً آن را حذف کنید.

### **2. نصب CMake با winget**

   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. نصب Visual Studio 2022 - توسعه دسکتاپ با C++**

   ***توجه*** اگر قصد کامپایل ندارید، می‌توانید این مرحله را رد کنید.

![CPP](../../../../../../translated_images/01.8964c1fa47e00dc36af710b967e72dd2f8a2be498e49c8d4c65c11ba105dedf8.fa.png)

### **4. نصب درایور NVIDIA**

1. **درایور GPU NVIDIA**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***یادآوری*** لطفاً از تنظیمات پیش‌فرض در جریان نصب استفاده کنید.

### **5. تنظیم محیط NVIDIA**

فایل‌های lib، bin و include مربوط به NVIDIA CUDNN 9.4 را به مسیرهای lib، bin و include مربوط به NVIDIA CUDA 12.4 کپی کنید.

- فایل‌های موجود در *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* را به *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'* کپی کنید.

- فایل‌های موجود در *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* را به *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'* کپی کنید.

- فایل‌های موجود در *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* را به *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'* کپی کنید.

### **6. دانلود Phi-3.5-mini-instruct-onnx**

   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. اجرای InferencePhi35Instruct.ipynb**

   [دفترچه یادداشت](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) را باز کرده و اجرا کنید.

![RESULT](../../../../../../translated_images/02.be96d16e7b1007f1f3941f65561553e62ccbd49c962f3d4a9154b8326c033ec1.fa.png)

### **8. کامپایل ORT GenAI GPU**

   ***توجه*** 
   
   1. ابتدا تمام کتابخانه‌های مرتبط با onnx، onnxruntime و onnxruntime-genai را حذف کنید.

   
   ```bash

   pip list 
   
   ```

   سپس تمام کتابخانه‌های onnxruntime را حذف کنید، مانند:


   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. بررسی پشتیبانی افزونه Visual Studio

   مسیر C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras را بررسی کنید تا اطمینان حاصل شود که C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration موجود است. 

   اگر موجود نبود، پوشه visual_studio_integration و محتویات آن را از دیگر مسیرهای درایور CUDA کپی کرده و به C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration انتقال دهید.

   - اگر قصد کامپایل ندارید، می‌توانید این مرحله را رد کنید.

   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - دانلود [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip)

   - فایل onnxruntime-win-x64-gpu-1.19.2.zip را از حالت فشرده خارج کرده و نام آن را به **ort** تغییر دهید، سپس پوشه ort را به onnxruntime-genai کپی کنید.

   - با استفاده از Windows Terminal، به Developer Command Prompt برای VS 2022 بروید و به پوشه onnxruntime-genai وارد شوید.

![RESULT](../../../../../../translated_images/03.53bb08e3bde53edd1735c5546fb32b9b0bdba93d8241c5e6e3196d8bc01adbd7.fa.png)

   - آن را با محیط Python خود کامپایل کنید.

   
   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل اشتباهات یا نادقتی‌ها باشند. سند اصلی به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوءتفاهم‌ها یا برداشت‌های نادرست ناشی از استفاده از این ترجمه نداریم.