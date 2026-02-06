# AGENTS.md

## 프로젝트 개요

PhiCookBook는 Microsoft의 Phi 소형 언어 모델(SLM) 제품군을 활용한 실습 예제, 튜토리얼 및 문서를 포함한 종합적인 요리책 저장소입니다. 이 저장소는 추론, 미세 조정, 양자화, RAG 구현 및 다양한 플랫폼과 프레임워크를 활용한 멀티모달 애플리케이션을 포함한 다양한 사용 사례를 보여줍니다.

**주요 기술:**
- **언어:** Python, C#/.NET, JavaScript/Node.js
- **프레임워크:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **플랫폼:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **모델 유형:** Phi-3, Phi-3.5, Phi-4 (텍스트, 비전, 멀티모달, 추론 변형)

**저장소 구조:**
- `/code/` - 작동 코드 예제 및 샘플 구현
- `/md/` - 상세 문서, 튜토리얼 및 사용 방법 가이드  
- `/translations/` - 다국어 번역 (자동화 워크플로를 통해 50개 이상의 언어 지원)
- `/.devcontainer/` - 개발 컨테이너 구성 (Python 3.12 및 Ollama 포함)

## 개발 환경 설정

### GitHub Codespaces 또는 Dev Containers 사용 (권장)

1. GitHub Codespaces에서 열기 (가장 빠름):
   - README에서 "Open in GitHub Codespaces" 배지를 클릭
   - 컨테이너가 Python 3.12 및 Phi-3이 포함된 Ollama로 자동 구성됨

2. VS Code Dev Containers에서 열기:
   - README에서 "Open in Dev Containers" 배지를 사용
   - 컨테이너는 최소 16GB의 호스트 메모리가 필요

### 로컬 설정

**필수 조건:**
- Python 3.12 이상
- .NET 8.0 SDK (C# 예제용)
- Node.js 18+ 및 npm (JavaScript 예제용)
- 최소 16GB RAM 권장

**설치:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Python 예제용:**
특정 예제 디렉토리로 이동하여 종속성을 설치:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**.NET 예제용:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**JavaScript/웹 예제용:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## 저장소 구성

### 코드 예제 (`/code/`)

- **01.Introduce/** - 기본 소개 및 시작 샘플
- **03.Finetuning/** 및 **04.Finetuning/** - 다양한 방법을 사용한 미세 조정 예제
- **03.Inference/** - 다양한 하드웨어(AIPC, MLX)에서의 추론 예제
- **06.E2E/** - 엔드 투 엔드 애플리케이션 샘플
- **07.Lab/** - 실험적 구현
- **08.RAG/** - 검색 증강 생성 샘플
- **09.UpdateSamples/** - 최신 업데이트된 샘플

### 문서 (`/md/`)

- **01.Introduction/** - 소개 가이드, 환경 설정, 플랫폼 가이드
- **02.Application/** - 텍스트, 코드, 비전, 오디오 등 유형별로 정리된 애플리케이션 샘플
- **02.QuickStart/** - Azure AI Foundry 및 GitHub Models에 대한 빠른 시작 가이드
- **03.FineTuning/** - 미세 조정 문서 및 튜토리얼
- **04.HOL/** - 실습 랩 (.NET 예제 포함)

### 파일 형식

- **Jupyter 노트북 (`.ipynb`)** - README에서 📓로 표시된 대화형 Python 튜토리얼
- **Python 스크립트 (`.py`)** - 독립 실행형 Python 예제
- **C# 프로젝트 (`.csproj`, `.sln`)** - .NET 애플리케이션 및 샘플
- **JavaScript (`.js`, `package.json`)** - 웹 기반 및 Node.js 예제
- **Markdown (`.md`)** - 문서 및 가이드

## 예제 작업

### Jupyter 노트북 실행

대부분의 예제는 Jupyter 노트북으로 제공됩니다:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Python 스크립트 실행

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### .NET 예제 실행

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

전체 솔루션 빌드:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### JavaScript/웹 예제 실행

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## 테스트

이 저장소는 단위 테스트가 포함된 전통적인 소프트웨어 프로젝트가 아니라 예제 코드와 튜토리얼을 포함하고 있습니다. 검증은 일반적으로 다음과 같이 수행됩니다:

1. **예제 실행** - 각 예제가 오류 없이 실행되어야 합니다
2. **출력 확인** - 모델 응답이 적절한지 확인
3. **튜토리얼 따라하기** - 문서화된 대로 가이드가 작동해야 합니다

**일반적인 검증 방법:**
- 대상 환경에서 예제 실행 테스트
- 종속성이 올바르게 설치되었는지 확인
- 모델 다운로드/로드가 성공적으로 이루어지는지 확인
- 예상되는 동작이 문서와 일치하는지 확인

## 코드 스타일 및 규칙

### 일반 지침

- 예제는 명확하고 주석이 잘 달려 있어야 하며 교육적이어야 합니다
- 언어별 규칙을 따르세요 (Python은 PEP 8, .NET은 C# 표준)
- 예제는 특정 Phi 모델 기능을 보여주는 데 초점을 맞춰야 합니다
- 주요 개념 및 모델별 매개변수를 설명하는 주석을 포함하세요

### 문서화 기준

**URL 형식:**
- `[text](../../url)` 형식을 사용하며 추가 공백은 피하세요
- 상대 링크: 현재 디렉토리는 `./`, 상위 디렉토리는 `../` 사용
- URL에 국가별 로케일을 포함하지 마세요 (`/en-us/`, `/en/` 등은 피하세요)

**이미지:**
- 모든 이미지는 `/imgs/` 디렉토리에 저장
- 영어 문자, 숫자 및 대시를 사용하여 설명적인 이름 사용
- 예: `phi-3-architecture.png`

**Markdown 파일:**
- `/code/` 디렉토리의 실제 작동 예제를 참조
- 코드 변경과 문서를 동기화 유지
- README에서 Jupyter 노트북 링크에 📓 이모지를 사용

### 파일 구성

- `/code/`의 코드 예제는 주제/기능별로 정리
- 문서는 가능할 경우 코드 구조를 반영하여 `/md/`에 정리
- 관련 파일(노트북, 스크립트, 구성 파일)을 하위 디렉토리에 함께 보관

## Pull Request 지침

### 제출 전

1. **저장소를 포크**하여 계정에 복사
2. **PR 유형별로 분리:**
   - 버그 수정은 하나의 PR로
   - 문서 업데이트는 다른 PR로
   - 새로운 예제는 별도의 PR로
   - 오타 수정은 결합 가능

3. **병합 충돌 처리:**
   - 변경 작업 전에 로컬 `main` 브랜치를 업데이트
   - 자주 업스트림과 동기화

4. **번역 PR:**
   - 폴더 내 모든 파일에 대한 번역 포함 필수
   - 원본 언어와 일관된 구조 유지

### 필수 확인 사항

PR은 GitHub 워크플로를 통해 자동으로 검증됩니다:

1. **상대 경로 검증** - 모든 내부 링크가 작동해야 함
   - 로컬에서 링크 테스트: VS Code에서 Ctrl+Click
   - VS Code의 경로 제안 사용 (`./` 또는 `../`)

2. **URL 로케일 확인** - 웹 URL에 국가 로케일이 포함되지 않아야 함
   - `/en-us/`, `/en/` 또는 기타 언어 코드를 제거
   - 일반 국제 URL 사용

3. **URL 깨짐 확인** - 모든 URL이 200 상태를 반환해야 함
   - 제출 전에 링크가 접근 가능한지 확인
   - 참고: 일부 실패는 네트워크 제한 때문일 수 있음

### PR 제목 형식

```
[component] Brief description
```

예제:
- `[docs] Phi-4 추론 튜토리얼 추가`
- `[code] ONNX Runtime 통합 예제 수정`
- `[translation] 소개 가이드 일본어 번역 추가`

## 일반적인 개발 패턴

### Phi 모델 작업

**모델 로딩:**
- 예제는 Transformers, ONNX Runtime, MLX, OpenVINO 등 다양한 프레임워크를 사용
- 모델은 주로 Hugging Face, Azure 또는 GitHub Models에서 다운로드
- 하드웨어(CPU, GPU, NPU)와 모델 호환성 확인

**추론 패턴:**
- 텍스트 생성: 대부분의 예제는 채팅/명령 변형 사용
- 비전: 이미지 이해를 위한 Phi-3-vision 및 Phi-4-multimodal
- 오디오: 오디오 입력을 지원하는 Phi-4-multimodal
- 추론: 고급 추론 작업을 위한 Phi-4-reasoning 변형

### 플랫폼별 참고 사항

**Azure AI Foundry:**
- Azure 구독 및 API 키 필요
- `/md/02.QuickStart/AzureAIFoundry_QuickStart.md` 참조

**GitHub Models:**
- 테스트를 위한 무료 계층 제공
- `/md/02.QuickStart/GitHubModel_QuickStart.md` 참조

**로컬 추론:**
- ONNX Runtime: 크로스 플랫폼, 최적화된 추론
- Ollama: 로컬 모델 관리 용이 (개발 컨테이너에 사전 구성됨)
- Apple MLX: Apple Silicon에 최적화

## 문제 해결

### 일반적인 문제

**메모리 문제:**
- Phi 모델은 상당한 RAM을 요구 (특히 비전/멀티모달 변형)
- 리소스 제한 환경에서는 양자화된 모델 사용
- `/md/01.Introduction/04/QuantifyingPhi.md` 참조

**종속성 충돌:**
- Python 예제는 특정 버전 요구 사항이 있을 수 있음
- 각 예제에 대해 가상 환경 사용
- 개별 `requirements.txt` 파일 확인

**모델 다운로드 실패:**
- 대형 모델은 느린 연결에서 시간 초과될 수 있음
- 클라우드 환경(Codespaces, Azure) 사용 고려
- Hugging Face 캐시 확인: `~/.cache/huggingface/`

**.NET 프로젝트 문제:**
- .NET 8.0 SDK가 설치되어 있는지 확인
- 빌드 전에 `dotnet restore` 사용
- 일부 프로젝트는 CUDA 특정 구성 포함 (Debug_Cuda)

**JavaScript/웹 예제:**
- 호환성을 위해 Node.js 18+ 사용
- 문제가 지속되면 `node_modules`를 삭제하고 재설치
- 브라우저 콘솔에서 WebGPU 호환성 문제 확인

### 도움 받기

- **Discord:** Azure AI Foundry 커뮤니티 Discord에 참여
- **GitHub Issues:** 저장소에서 버그 및 문제 보고
- **GitHub Discussions:** 질문하고 지식 공유

## 추가 정보

### 책임 있는 AI

모든 Phi 모델 사용은 Microsoft의 책임 있는 AI 원칙을 따라야 합니다:
- 공정성, 신뢰성, 안전성
- 개인정보 보호 및 보안  
- 포괄성, 투명성, 책임감
- 프로덕션 애플리케이션에 Azure AI Content Safety 사용
- `/md/01.Introduction/01/01.AISafety.md` 참조

### 번역

- 자동화된 GitHub Action을 통해 50개 이상의 언어 지원
- `/translations/` 디렉토리에 번역 포함
- co-op-translator 워크플로에 의해 관리
- 번역된 파일을 수동으로 편집하지 마세요 (자동 생성됨)

### 기여

- `CONTRIBUTING.md`의 지침을 따르세요
- Contributor License Agreement (CLA)에 동의
- Microsoft 오픈 소스 행동 강령 준수
- 커밋에 보안 및 자격 증명을 포함하지 않도록 주의

### 다국어 지원

이 저장소는 다음 언어로 된 예제를 포함한 다국어 저장소입니다:
- **Python** - ML/AI 워크플로, Jupyter 노트북, 미세 조정
- **C#/.NET** - 엔터프라이즈 애플리케이션, ONNX Runtime 통합
- **JavaScript** - 웹 기반 AI, WebGPU를 활용한 브라우저 추론

사용 사례와 배포 대상에 가장 적합한 언어를 선택하세요.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임지지 않습니다.