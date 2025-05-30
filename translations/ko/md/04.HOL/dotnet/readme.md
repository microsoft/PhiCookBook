<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "903c509a6d0d1ecce00b849d7f753bdd",
  "translation_date": "2025-05-08T05:02:05+00:00",
  "source_file": "md/04.HOL/dotnet/readme.md",
  "language_code": "ko"
}
-->
﻿## C#를 사용하는 Phi 실험실에 오신 것을 환영합니다

.NET 환경에서 다양한 Phi 모델 버전을 강력하게 통합하는 방법을 보여주는 여러 실험실이 준비되어 있습니다.

## 사전 준비 사항

샘플을 실행하기 전에 다음이 설치되어 있는지 확인하세요:

**.NET 9:** [최신 버전의 .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo)이 컴퓨터에 설치되어 있어야 합니다.

**(선택 사항) Visual Studio 또는 Visual Studio Code:** .NET 프로젝트를 실행할 수 있는 IDE나 코드 편집기가 필요합니다. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) 또는 [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo)를 권장합니다.

**git 사용:** [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c)에서 Phi-3, Phi3.5 또는 Phi-4 버전 중 하나를 로컬로 클론하세요.

**Phi-4 ONNX 모델을** 로컬 컴퓨터에 다운로드하세요:

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

**Phi-3 ONNX 모델을** 로컬 컴퓨터에 다운로드하세요:

### Phi-3 미니 4K 인스트럭트 모델과 Phi-3 비전 128K 모델 클론 및 다운로드

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**중요:** 현재 데모는 모델의 ONNX 버전을 사용하도록 설계되었습니다. 위 단계에서 다음 모델들을 클론합니다.

## 실험실 소개

메인 솔루션에는 C#을 사용하여 Phi 모델의 기능을 보여주는 여러 샘플 실험실이 포함되어 있습니다.

| 프로젝트 | 모델 | 설명 |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 또는 Phi-3.5 | 사용자가 질문할 수 있는 콘솔 채팅 샘플입니다. 이 프로젝트는 `Microsoft.ML.OnnxRuntime` libraries. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 or Phi-3.5 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-3 model using the `Microsoft.Semantic.Kernel` libraries. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 or Phi-3.5 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Semantic Kernel` libraries. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Sample console chat that allows the user to ask questions. The project load a local ONNX Phi-4 model using the `Microsoft.ML.OnnxRuntimeGenAI` libraries and implements the `IChatClient` from `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Sample console chat that allows the user to ask questions. The chat implements memory. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | This is a sample project that uses a local Phi-4 model to analyze images showing the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 |This is a sample project that uses a local Phi-4 model to analyze an audio file, generate the transcript of the file and show the result in the console. The project load a local Phi-4-`multimodal-instruct-onnx` model using the `Microsoft.ML.OnnxRuntime` libraries. |

## How to Run the Projects

To run the projects, follow these steps:

1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi4-Chat-01OnnxRuntime`를 사용해 로컬 ONNX Phi-3 모델을 로드합니다.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. 다음 명령어로 프로젝트를 실행하세요

    ```bash
    dotnet run
    ```

1. 샘플 프로젝트는 사용자 입력을 받고 로컬 모델을 사용해 응답합니다.

   실행 중인 데모는 다음과 유사합니다:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역은 오류나 부정확성이 포함될 수 있음을 유의해 주시기 바랍니다. 원문은 해당 언어로 작성된 원본 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.