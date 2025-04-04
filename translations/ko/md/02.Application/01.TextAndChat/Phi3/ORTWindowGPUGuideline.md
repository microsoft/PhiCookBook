<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9fe95f5575ecf5985eb9f67d205d0136",
  "translation_date": "2025-04-04T06:31:11+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\ORTWindowGPUGuideline.md",
  "language_code": "ko"
}
-->
# **OnnxRuntime GenAI Windows GPU 가이드라인**

이 가이드라인은 Windows에서 GPU를 사용하여 ONNX Runtime (ORT)을 설정하고 사용하는 방법을 제공합니다. GPU 가속을 활용하여 모델의 성능과 효율성을 향상시키는 데 도움을 주기 위해 작성되었습니다.

문서에서 다루는 내용:

- 환경 설정: CUDA, cuDNN, ONNX Runtime과 같은 필수 종속 항목 설치 방법.
- 구성: GPU 리소스를 효과적으로 활용하기 위한 환경 및 ONNX Runtime 설정 방법.
- 최적화 팁: GPU 설정을 미세 조정하여 최적의 성능을 얻는 방법.

### **1. Python 3.10.x / 3.11.8**

   ***참고*** Python 환경으로 [miniforge](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe)를 사용할 것을 권장합니다.

   ```bash

   conda create -n pydev python==3.11.8

   conda activate pydev

   ```

   ***알림*** Python ONNX 라이브러리를 이미 설치한 경우 제거해야 합니다.

### **2. winget을 사용하여 CMake 설치**

   ```bash

   winget install -e --id Kitware.CMake

   ```

### **3. Visual Studio 2022 - C++을 사용한 데스크톱 개발 설치**

   ***참고*** 컴파일을 원하지 않는 경우 이 단계를 건너뛸 수 있습니다.

![CPP](../../../../../../translated_images/01.8964c1fa47e00dc36af710b967e72dd2f8a2be498e49c8d4c65c11ba105dedf8.ko.png)

### **4. NVIDIA 드라이버 설치**

1. **NVIDIA GPU 드라이버** [https://www.nvidia.com/en-us/drivers/](https://www.nvidia.com/en-us/drivers/)

2. **NVIDIA CUDA 12.4** [https://developer.nvidia.com/cuda-12-4-0-download-archive](https://developer.nvidia.com/cuda-12-4-0-download-archive)

3. **NVIDIA CUDNN 9.4** [https://developer.nvidia.com/cudnn-downloads](https://developer.nvidia.com/cudnn-downloads)

***알림*** 설치 과정에서 기본 설정을 사용하십시오.

### **5. NVIDIA 환경 설정**

NVIDIA CUDNN 9.4의 lib, bin, include 파일을 NVIDIA CUDA 12.4의 lib, bin, include에 복사합니다.

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\bin\12.6'* 파일을 *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\bin'*으로 복사합니다.

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\include\12.6'* 파일을 *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\include'*으로 복사합니다.

- *'C:\Program Files\NVIDIA\CUDNN\v9.4\lib\12.6'* 파일을 *'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\lib\x64'*으로 복사합니다.

### **6. Phi-3.5-mini-instruct-onnx 다운로드**

   ```bash

   winget install -e --id Git.Git

   winget install -e --id GitHub.GitLFS

   git lfs install

   git clone https://huggingface.co/microsoft/Phi-3.5-mini-instruct-onnx

   ```

### **7. InferencePhi35Instruct.ipynb 실행**

   [Notebook](../../../../../../code/09.UpdateSamples/Aug/ortgpu-phi35-instruct.ipynb)을 열고 실행합니다.

![RESULT](../../../../../../translated_images/02.be96d16e7b1007f1f3941f65561553e62ccbd49c962f3d4a9154b8326c033ec1.ko.png)

### **8. ORT GenAI GPU 컴파일**

   ***참고*** 
   
   1. 먼저 onnx, onnxruntime 및 onnxruntime-genai 관련 모든 항목을 제거하십시오.

   ```bash

   pip list 
   
   ```

   그런 다음 모든 onnxruntime 라이브러리를 제거합니다. 예를 들어:

   ```bash

   pip uninstall onnxruntime

   pip uninstall onnxruntime-genai

   pip uninstall onnxruntume-genai-cuda
   
   ```

   2. Visual Studio 확장 지원 확인

   *C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras*에서 *C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration* 폴더가 있는지 확인합니다. 

   폴더가 없으면 다른 CUDA 툴킷 드라이버 폴더를 확인하고 해당 폴더와 내용을 *C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4\extras\visual_studio_integration*으로 복사하십시오.

   - 컴파일을 원하지 않는 경우 이 단계를 건너뛸 수 있습니다.

   ```bash

   git clone https://github.com/microsoft/onnxruntime-genai

   ```

   - [https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip](https://github.com/microsoft/onnxruntime/releases/download/v1.19.2/onnxruntime-win-x64-gpu-1.19.2.zip)을 다운로드합니다.

   - onnxruntime-win-x64-gpu-1.19.2.zip을 압축 해제한 후 **ort**로 이름을 변경하고 ort 폴더를 onnxruntime-genai로 복사합니다.

   - Windows Terminal을 사용하여 VS 2022 개발자 명령 프롬프트로 이동한 뒤 onnxruntime-genai로 이동합니다.

![RESULT](../../../../../../translated_images/03.53bb08e3bde53edd1735c5546fb32b9b0bdba93d8241c5e6e3196d8bc01adbd7.ko.png)

   - Python 환경을 사용하여 컴파일합니다.

   ```bash

   cd onnxruntime-genai

   python build.py --use_cuda  --cuda_home "C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4" --config Release
 

   cd build/Windows/Release/Wheel

   pip install .whl

   ```

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 알려드립니다. 원어로 작성된 원본 문서를 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.