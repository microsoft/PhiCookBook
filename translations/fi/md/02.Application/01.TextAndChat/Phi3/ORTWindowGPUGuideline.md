<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b066fc29c1b2129df84e027cb75119ce",
  "translation_date": "2025-05-09T18:44:35+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/ORTWindowGPUGuideline.md",
  "language_code": "fi"
}
-->
# **Ohjeet OnnxRuntime GenAI Windows GPU:lle**

Tässä ohjeessa käydään läpi, miten ONNX Runtime (ORT) asennetaan ja otetaan käyttöön GPU:illa Windows-ympäristössä. Tavoitteena on auttaa sinua hyödyntämään GPU-kiihdytystä malleissasi, parantaen suorituskykyä ja tehokkuutta.

Dokumentti sisältää ohjeita seuraaviin aiheisiin:

- Ympäristön asennus: Ohjeet tarvittavien riippuvuuksien, kuten CUDA:n, cuDNN:n ja ONNX Runtime:n asentamiseen.
- Konfigurointi: Kuinka määrittää ympäristö ja ONNX Runtime hyödyntämään GPU-resursseja tehokkaasti.
- Optimointivinkit: Neuvoja GPU-asetusten hienosäätöön optimaalisen suorituskyvyn saavuttamiseksi.

### **1. Python 3.10.x /3.11.8**

   ***Note*** Suositeltavaa käyttää [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) Python-ympäristönäsi

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***Reminder*** Jos olet asentanut jonkin python ONNX -kirjaston, poista se asennus

### **2. Asenna CMake wingetillä**

   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Asenna Visual Studio 2022 - Desktop Development with C++**

   ***Note*** Jos et halua kääntää, voit ohittaa tämän vaiheen

![CPP](../../../../../../translated_images/01.8964c1fa47e00dc36af710b967e72dd2f8a2be498e49c8d4c65c11ba105dedf8.fi.png)


### **4. Asenna NVIDIA-ajuri**

1. **NVIDIA GPU Driver**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***Reminder*** Käytä asennuksessa oletusasetuksia

### **5. Aseta NVIDIA-ympäristö**

Kopioi NVIDIA CUDNN 9.4:n lib-, bin- ja include-kansiot NVIDIA CUDA 12.4:n vastaaviin kansioihin

- kopioi *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* tiedostot kansioon *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'*

- kopioi *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* tiedostot kansioon *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'*

- kopioi *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* tiedostot kansioon *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'*


### **6. Lataa Phi-3.5-mini-instruct-onnx**

   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. Suorita InferencePhi35Instruct.ipynb**

   Avaa [Notebook](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) ja suorita

![RESULT](../../../../../../translated_images/02.be96d16e7b1007f1f3941f65561553e62ccbd49c962f3d4a9154b8326c033ec1.fi.png)

### **8. Käännä ORT GenAI GPU**

   ***Note*** 
   
   1. Poista ensin kaikki onnx-, onnxruntime- ja onnxruntime-genai-kirjastot

   ```bash

   pip list 
   
   ```

   Sen jälkeen poista kaikki onnxruntime-kirjastot, esimerkiksi:

   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Tarkista Visual Studio -laajennuksen tuki

   Tarkista kansio C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras, varmista että polusta löytyy C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration. 

   Jos kansiota ei löydy, etsi se muista CUDA toolkit -ajurien kansioista ja kopioi visual_studio_integration -kansio ja sen sisältö C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration -polkuun

   - Jos et halua kääntää, voit ohittaa tämän vaiheen

   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - Lataa [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip)

   - Pura onnxruntime-win-x64-gpu-1.19.2.zip, nimeä kansio uudelleen **ort** ja kopioi se onnxruntime-genai-kansioon

   - Käytä Windows Terminalia, avaa Developer Command Prompt for VS 2022 ja siirry onnxruntime-genai-kansioon

![RESULT](../../../../../../translated_images/03.53bb08e3bde53edd1735c5546fb32b9b0bdba93d8241c5e6e3196d8bc01adbd7.fi.png)

   - Käännä se Python-ympäristössäsi

   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.