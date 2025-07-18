<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-07-17T10:33:26+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "ko"
}
-->
﻿## C#를 사용한 Phi 실습실에 오신 것을 환영합니다

.NET 환경에서 다양한 버전의 강력한 Phi 모델을 통합하는 방법을 보여주는 여러 실습실 샘플이 준비되어 있습니다.

## 사전 준비 사항

샘플을 실행하기 전에 다음이 설치되어 있는지 확인하세요:

**.NET 9:** [최신 버전의 .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo)이 컴퓨터에 설치되어 있어야 합니다.

**(선택 사항) Visual Studio 또는 Visual Studio Code:** .NET 프로젝트를 실행할 수 있는 IDE나 코드 편집기가 필요합니다. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) 또는 [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo)를 권장합니다.

**git 사용:** [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c)에서 Phi-3, Phi3.5 또는 Phi-4 버전 중 하나를 로컬에 클론하세요.

**Phi-4 ONNX 모델을 로컬에 다운로드하세요:**

### 모델을 저장할 폴더로 이동

```bash
cd c:\phi\models
```

### lfs 지원 추가

```bash
git lfs install 
```

### Phi-4 미니 인스트럭트 모델과 Phi-4 멀티모달 모델 클론 및 다운로드

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Phi-3 ONNX 모델을 로컬에 다운로드하세요:**

### Phi-3 미니 4K 인스트럭트 모델과 Phi-3 비전 128K 모델 클론 및 다운로드

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**중요:** 현재 데모는 모델의 ONNX 버전을 사용하도록 설계되었습니다. 위 단계에서 다음 모델들이 클론됩니다.

## 실습실 소개

메인 솔루션에는 C#을 사용하여 Phi 모델의 기능을 보여주는 여러 샘플 실습실이 포함되어 있습니다.

| 프로젝트 | 모델 | 설명 |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 또는 Phi-3.5 | 사용자가 질문할 수 있는 콘솔 채팅 샘플입니다. `Microsoft.ML.OnnxRuntime` 라이브러리를 사용해 로컬 ONNX Phi-3 모델을 로드합니다. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 또는 Phi-3.5 | 사용자가 질문할 수 있는 콘솔 채팅 샘플입니다. `Microsoft.Semantic.Kernel` 라이브러리를 사용해 로컬 ONNX Phi-3 모델을 로드합니다. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 또는 Phi-3.5 | 로컬 phi3 비전 모델을 사용해 이미지를 분석하는 샘플 프로젝트입니다. `Microsoft.ML.OnnxRuntime` 라이브러리를 사용해 로컬 ONNX Phi-3 Vision 모델을 로드합니다. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 또는 Phi-3.5 | 로컬 phi3 비전 모델을 사용해 이미지를 분석하는 샘플 프로젝트입니다. `Microsoft.ML.OnnxRuntime` 라이브러리를 사용해 로컬 ONNX Phi-3 Vision 모델을 로드하며, 사용자와 상호작용할 수 있는 다양한 옵션 메뉴도 제공합니다. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | 사용자가 질문할 수 있는 콘솔 채팅 샘플입니다. `Microsoft.ML.OnnxRuntime` 라이브러리를 사용해 로컬 ONNX Phi-4 모델을 로드합니다. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | 사용자가 질문할 수 있는 콘솔 채팅 샘플입니다. `Semantic Kernel` 라이브러리를 사용해 로컬 ONNX Phi-4 모델을 로드합니다. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | 사용자가 질문할 수 있는 콘솔 채팅 샘플입니다. `Microsoft.ML.OnnxRuntimeGenAI` 라이브러리를 사용해 로컬 ONNX Phi-4 모델을 로드하며, `Microsoft.Extensions.AI`의 `IChatClient`를 구현합니다. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | 사용자가 질문할 수 있는 콘솔 채팅 샘플입니다. 채팅에 메모리 기능이 구현되어 있습니다. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | 로컬 Phi-4 모델을 사용해 이미지를 분석하고 결과를 콘솔에 출력하는 샘플 프로젝트입니다. `Microsoft.ML.OnnxRuntime` 라이브러리를 사용해 로컬 Phi-4-`multimodal-instruct-onnx` 모델을 로드합니다. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | 로컬 Phi-4 모델을 사용해 오디오 파일을 분석하고, 파일의 전사본을 생성하여 콘솔에 결과를 보여주는 샘플 프로젝트입니다. `Microsoft.ML.OnnxRuntime` 라이브러리를 사용해 로컬 Phi-4-`multimodal-instruct-onnx` 모델을 로드합니다. |

## 프로젝트 실행 방법

프로젝트를 실행하려면 다음 단계를 따르세요:

1. 저장소를 로컬 컴퓨터에 클론합니다.

1. 터미널을 열고 원하는 프로젝트 폴더로 이동합니다. 예를 들어, `LabsPhi4-Chat-01OnnxRuntime`을 실행해 보겠습니다.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. 다음 명령어로 프로젝트를 실행합니다.

    ```bash
    dotnet run
    ```

1. 샘플 프로젝트가 사용자 입력을 요청하고 로컬 모델을 사용해 응답합니다.

   실행 중인 데모는 다음과 유사합니다:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.