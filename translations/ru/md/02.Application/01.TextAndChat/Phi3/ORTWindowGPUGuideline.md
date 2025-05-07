<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b066fc29c1b2129df84e027cb75119ce",
  "translation_date": "2025-05-07T14:19:50+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/ORTWindowGPUGuideline.md",
  "language_code": "ru"
}
-->
# **Руководство по OnnxRuntime GenAI для Windows GPU**

Это руководство описывает шаги по настройке и использованию ONNX Runtime (ORT) с GPU на Windows. Оно поможет вам использовать ускорение на GPU для ваших моделей, улучшая производительность и эффективность.

В документе приведены рекомендации по:

- Настройке окружения: инструкции по установке необходимых зависимостей, таких как CUDA, cuDNN и ONNX Runtime.
- Конфигурации: как настроить окружение и ONNX Runtime для эффективного использования ресурсов GPU.
- Советы по оптимизации: рекомендации по тонкой настройке параметров GPU для максимальной производительности.

### **1. Python 3.10.x /3.11.8**

   ***Примечание*** Рекомендуется использовать [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) в качестве среды Python

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***Напоминание*** Если у вас установлен какой-либо Python ONNX пакет, пожалуйста, удалите его

### **2. Установка CMake с помощью winget**

   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Установка Visual Studio 2022 - разработка для рабочего стола с C++**

   ***Примечание*** Если вы не планируете компилировать, этот шаг можно пропустить

![CPP](../../../../../../translated_images/01.42f52a2b2aedff029e1c9beb13d2b09fcdab284ffd5fa8f3d7ac3cef5f347ad2.ru.png)

### **4. Установка драйвера NVIDIA**

1. **Драйвер NVIDIA GPU**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***Напоминание*** Используйте настройки по умолчанию во время установки

### **5. Настройка окружения NVIDIA**

Скопируйте файлы NVIDIA CUDNN 9.4 из папок lib, bin, include в соответствующие папки NVIDIA CUDA 12.4

- скопируйте файлы из *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* в  *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'*

- скопируйте файлы из *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* в  *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'*

- скопируйте файлы из *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* в  *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'*

### **6. Скачайте Phi-3.5-mini-instruct-onnx**

   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. Запуск InferencePhi35Instruct.ipynb**

   Откройте [Notebook](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) и выполните его

![RESULT](../../../../../../translated_images/02.b9b06996cf7255d5e5ee19a703c4352f4a96dd7a1068b2af227eda1f3104bfa0.ru.png)

### **8. Компиляция ORT GenAI GPU**

   ***Примечание*** 
   
   1. Сначала удалите все пакеты, связанные с onnx, onnxruntime и onnxruntime-genai

   ```bash

   pip list 
   
   ```

   Затем удалите все библиотеки onnxruntime, например:

   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Проверьте поддержку расширения Visual Studio

   Проверьте папку C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras, чтобы убедиться, что там есть C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration. 
   
   Если её нет, проверьте другие папки драйверов Cuda toolkit и скопируйте папку visual_studio_integration со всем содержимым в C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration

   - Если вы не планируете компилировать, этот шаг можно пропустить

   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - Скачайте [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip)

   - Распакуйте onnxruntime-win-x64-gpu-1.19.2.zip, переименуйте папку в **ort** и скопируйте её в onnxruntime-genai

   - В Windows Terminal откройте Developer Command Prompt для VS 2022 и перейдите в папку onnxruntime-genai

![RESULT](../../../../../../translated_images/03.b83ce473d5ff9b9b94670a1b26fdb66a05320d534cbee2762f64e52fd12ef9c9.ru.png)

   - Скомпилируйте с вашей Python средой

   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется использовать профессиональный человеческий перевод. Мы не несем ответственности за любые недоразумения или неверные толкования, возникшие в результате использования данного перевода.