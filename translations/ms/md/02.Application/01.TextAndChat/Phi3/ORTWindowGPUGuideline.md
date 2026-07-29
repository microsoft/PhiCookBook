# **Garis Panduan untuk OnnxRuntime GenAI Windows GPU**

Garis panduan ini menyediakan langkah-langkah untuk menyediakan dan menggunakan ONNX Runtime (ORT) dengan GPU pada Windows. Ia direka untuk membantu anda menggunakan pemajuan GPU untuk model anda, meningkatkan prestasi dan kecekapan.

Dokumen ini memberikan panduan mengenai:

- Penyediaan Persekitaran: Arahan untuk memasang kebergantungan yang diperlukan seperti CUDA, cuDNN, dan ONNX Runtime.
- Konfigurasi: Cara mengkonfigurasi persekitaran dan ONNX Runtime untuk menggunakan sumber GPU dengan efektif.
- Petua Pengoptimuman: Nasihat tentang cara menyesuaikan tetapan GPU anda untuk prestasi optimum.

### **1. Python 3.10.x /3.11.8**

   ***Nota*** Disyorkan menggunakan [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) sebagai persekitaran Python anda

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***Peringatan*** Jika anda telah memasang mana-mana perpustakaan python ONNX, sila nyahpasangnya

### **2. Pasang CMake dengan winget**


   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Pasang Visual Studio 2022 - Pembangunan Desktop dengan C++**

   ***Nota*** Jika anda tidak mahu menyusun, anda boleh langkau langkah ini

![CPP](../../../../../../translated_images/ms/01.42f52a2b2aedff02.webp)


### **4. Pasang Pemacu NVIDIA**

1. **Pemacu GPU NVIDIA** [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4** [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***Peringatan*** Sila gunakan tetapan lalai dengan aliran Pemasangan

### **5. Tetapkan Persekitaran NVIDIA**

Salin perpustakaan NVIDIA CUDNN 9.4 lib, bin, include ke NVIDIA CUDA 12.4 lib, bin, include

- Salin fail *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* ke *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'*

- Salin fail *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* ke *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'*

- Salin fail *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* ke *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'*


### **6. Muat Turun Phi-3.5-mini-instruct-onnx**


   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. Menjalankan InferencePhi35Instruct.ipynb**

   Buka [Notebook](../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) dan jalankan


![RESULT](../../../../../../translated_images/ms/02.b9b06996cf7255d5.webp)


### **8. Susun ORT GenAI GPU**


   ***Nota*** 
   
   1. Sila nyahpasang semua berkaitan onnx dan onnxruntime dan onnxruntime-genai terlebih dahulu

   
   ```bash

   pip list 
   
   ```

   Kemudian nyahpasang semua perpustakaan onnxruntime iaitu


   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Semak sokongan Sambungan Visual Studio

   Semak C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras untuk memastikan C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration dijumpai.
   
   Jika tidak dijumpai semak folder pemacu Cuda toolkit yang lain dan salin folder visual_studio_integration beserta kandungannya ke C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration




   - Jika anda tidak mahu menyusun, anda boleh langkau langkah ini


   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - Muat turun [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip)

   - Nyahzip onnxruntime-win-x64-gpu-1.19.2.zip, dan namakan semula kepada **ort**, salin folder ort ke onnxruntime-genai

   - Menggunakan Windows Terminal, pergi ke Developer Command Prompt untuk VS 2022 dan pergi ke onnxruntime-genai 

![RESULT](../../../../../../translated_images/ms/03.b83ce473d5ff9b9b.webp)

   - Susun ia dengan persekitaran python anda

   
   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->