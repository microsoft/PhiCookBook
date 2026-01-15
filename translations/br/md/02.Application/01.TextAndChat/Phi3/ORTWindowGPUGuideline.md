<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b066fc29c1b2129df84e027cb75119ce",
  "translation_date": "2025-07-17T02:42:34+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/ORTWindowGPUGuideline.md",
  "language_code": "br"
}
-->
# **Guia para OnnxRuntime GenAI Windows GPU**

Este guia fornece os passos para configurar e usar o ONNX Runtime (ORT) com GPUs no Windows. Ele foi criado para ajudar você a aproveitar a aceleração por GPU em seus modelos, melhorando desempenho e eficiência.

O documento traz orientações sobre:

- Configuração do Ambiente: Instruções para instalar as dependências necessárias como CUDA, cuDNN e ONNX Runtime.
- Configuração: Como ajustar o ambiente e o ONNX Runtime para utilizar os recursos da GPU de forma eficaz.
- Dicas de Otimização: Recomendações para ajustar as configurações da GPU para obter o melhor desempenho.

### **1. Python 3.10.x /3.11.8**

   ***Nota*** Recomendamos usar [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) como seu ambiente Python

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***Lembrete*** Se você instalou alguma biblioteca ONNX para Python, por favor desinstale

### **2. Instalar CMake com winget**

   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Instalar Visual Studio 2022 - Desenvolvimento Desktop com C++**

   ***Nota*** Se você não quiser compilar, pode pular esta etapa

![CPP](../../../../../../translated_images/br/01.42f52a2b2aedff02.png)

### **4. Instalar Driver NVIDIA**

1. **Driver NVIDIA GPU**  [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4**  [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***Lembrete*** Use as configurações padrão durante a instalação

### **5. Configurar Ambiente NVIDIA**

Copie as pastas lib, bin e include do NVIDIA CUDNN 9.4 para as respectivas pastas do NVIDIA CUDA 12.4

- copie os arquivos de *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* para *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'*

- copie os arquivos de *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* para *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'*

- copie os arquivos de *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* para *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'*

### **6. Baixar Phi-3.5-mini-instruct-onnx**

   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. Executar InferencePhi35Instruct.ipynb**

   Abra o [Notebook](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb) e execute

![RESULT](../../../../../../translated_images/br/02.b9b06996cf7255d5.png)

### **8. Compilar ORT GenAI GPU**

   ***Nota*** 
   
   1. Por favor, desinstale todas as bibliotecas relacionadas a onnx, onnxruntime e onnxruntime-genai antes de começar

   ```bash

   pip list 
   
   ```

   Depois, desinstale todas as bibliotecas onnxruntime, por exemplo:

   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Verifique o suporte da extensão do Visual Studio

   Confira a pasta C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras para garantir que a pasta C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration esteja presente. 
   
   Se não encontrar, verifique outras pastas do driver do toolkit CUDA e copie a pasta visual_studio_integration e seu conteúdo para C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration

   - Se você não quiser compilar, pode pular esta etapa

   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - Baixe [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip)

   - Descompacte onnxruntime-win-x64-gpu-1.19.2.zip, renomeie para **ort** e copie a pasta ort para onnxruntime-genai

   - Usando o Windows Terminal, abra o Developer Command Prompt para VS 2022 e navegue até onnxruntime-genai

![RESULT](../../../../../../translated_images/br/03.b83ce473d5ff9b9b.png)

   - Compile usando seu ambiente Python

   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.