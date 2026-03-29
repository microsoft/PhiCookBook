# AGENTS.md

## Project Overview

PhiCookBook은 Microsoft의 Phi 계열 소규모 언어 모델(SLM)을 다루는 실습 예제, 튜토리얼 및 문서가 포함된 종합 요리책 저장소입니다. 이 저장소는 추론, 미세 조정, 양자화, RAG 구현 및 다양한 플랫폼과 프레임워크에서의 멀티모달 응용 프로그램 등 다양한 사용 사례를 보여줍니다.

**주요 기술:**
- **언어:** Python, C#/.NET, JavaScript/Node.js
- **프레임워크:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **플랫폼:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **모델 유형:** Phi-3, Phi-3.5, Phi-4 (텍스트, 비전, 멀티모달, 추론 변종)

**저장소 구조:**
- `/code/` - 실제 동작 코드 예제 및 샘플 구현
- `/md/` - 상세 문서, 튜토리얼, 사용 방법 가이드  
- `/translations/` - 다국어 번역 (자동화 워크플로우로 50개 이상 언어)
- `/.devcontainer/` - 개발 컨테이너 구성 (Python 3.12 및 Ollama 포함)

## Development Environment Setup

### Using GitHub Codespaces or Dev Containers (Recommended)

1. GitHub Codespaces에서 열기 (가장 빠름):
   - README의 "Open in GitHub Codespaces" 뱃지 클릭
   - Python 3.12와 Ollama가 Phi-3과 함께 자동 구성

2. VS Code Dev Containers에서 열기:
   - README의 "Open in Dev Containers" 뱃지 사용
   - 최소 16GB 호스트 메모리 필요

### Local Setup

**필수 사항:**
- Python 3.12 이상
- .NET 8.0 SDK (C# 예제용)
- Node.js 18 이상 및 npm (JavaScript 예제용)
- 최소 16GB RAM 권장

**설치:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Python 예제용:**
특정 예제 디렉터리로 이동하여 종속성 설치:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # requirements.txt 파일이 존재하는 경우
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
npm run dev  # 개발 서버 시작
npm run build  # 프로덕션 빌드
```

## Repository Organization

### Code Examples (`/code/`)

- **01.Introduce/** - 기본 소개 및 시작 샘플
- **03.Finetuning/** 및 **04.Finetuning/** - 다양한 방법의 미세 조정 예제
- **03.Inference/** - 다양한 하드웨어 (AIPC, MLX)에서의 추론 예제
- **06.E2E/** - 엔드 투 엔드 애플리케이션 샘플
- **07.Lab/** - 실험실/시험적 구현
- **08.RAG/** - Retrieval-Augmented Generation 샘플
- **09.UpdateSamples/** - 최신 업데이트 샘플

### Documentation (`/md/`)

- **01.Introduction/** - 소개 가이드, 환경 설정, 플랫폼 안내
- **02.Application/** - 유형별 애플리케이션 샘플 (텍스트, 코드, 비전, 오디오 등)
- **02.QuickStart/** - Microsoft Foundry 및 GitHub Models 빠른 시작 가이드
- **03.FineTuning/** - 미세 조정 문서 및 튜토리얼
- **04.HOL/** - 실습 실험실 (.NET 예제 포함)

### File Formats

- **Jupyter Notebooks (`.ipynb`)** - README에 📓 표시된 대화형 Python 튜토리얼
- **Python Scripts (`.py`)** - 독립 실행형 Python 예제
- **C# Projects (`.csproj`, `.sln`)** - .NET 애플리케이션 및 샘플
- **JavaScript (`.js`, `package.json`)** - 웹 및 Node.js 기반 예제
- **Markdown (`.md`)** - 문서 및 가이드

## Working with Examples

### Running Jupyter Notebooks

대부분의 예제가 Jupyter 노트북 형태로 제공됩니다:
```bash
pip install jupyter notebook
jupyter notebook  # 브라우저 인터페이스를 엽니다
# 원하는 .ipynb 파일로 이동합니다
```

### Running Python Scripts

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Running .NET Examples

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

또는 전체 솔루션 빌드:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Running JavaScript/Web Examples

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # 핫 리로드 개발
```

## Testing

이 저장소는 전통적 소프트웨어 프로젝트의 단위 테스트보다는 예제 코드 및 튜토리얼 중심입니다. 검증 방법은 일반적으로 다음과 같습니다:

1. **예제 실행** – 각 예제가 오류 없이 실행되어야 함
2. **출력 검증** – 모델 응답이 적절한지 확인
3. **튜토리얼 따르기** – 단계별 가이드가 문서대로 작동해야 함

**일반적인 검증 방법:**
- 대상 환경에서 예제 실행 테스트
- 종속성 올바르게 설치 확인
- 모델 다운로드/로딩 성공 여부 확인
- 기대되는 동작이 문서와 일치하는지 확인

## Code Style and Conventions

### General Guidelines

- 예제는 명확하고 주석이 잘 달려 있어 교육적이어야 함
- 언어별 코딩 관례 준수 (Python은 PEP 8, .NET은 C# 표준)
- 특정 Phi 모델 기능을 보여주는 데 집중
- 주요 개념과 모델별 매개변수를 설명하는 주석 포함

### Documentation Standards

**URL 형식:**
- `[text](../../url)` 형식을 사용하며 추가 공백 없음
- 상대 링크: 현재 디렉터리는 `./`, 상위는 `../` 사용
- 국가별 로케일 포함 URL 금지 (`/en-us/`, `/en/` 등)

**이미지:**
- 모든 이미지는 `/imgs/` 디렉터리에 저장
- 영어 문자, 숫자, 대시 사용하여 설명적 이름 부여
- 예: `phi-3-architecture.png`

**Markdown 파일:**
- 실제 동작하는 `/code/` 예제 참조
- 문서와 코드 변경을 동기화 유지
- README에서 Jupyter 노트북 링크는 📓 이모지로 표시

### File Organization

- 주제/기능별로 `/code/` 내 코드 예제 구성
- 문서는 적용 시 코드 구조를 `/md/`에서 반영
- 관련 파일(노트북, 스크립트, 구성 등)은 하위 디렉터리에 함께 배치

## Pull Request Guidelines

### Before Submitting

1. 자신의 계정으로 저장소 포크
2. PR 유형 분리:
   - 버그 수정은 별도 PR
   - 문서 업데이트는 별도 PR
   - 신규 예제는 각각 별도 PR
   - 오타 수정은 합쳐도 무방

3. 병합 충돌 처리:
   - 변경 전 로컬 `main` 브랜치 최신 상태 유지
   - 자주 업스트림과 동기화

4. 번역 PR:
   - 해당 폴더의 모든 파일 번역 포함 필수
   - 원본 구조 일관성 유지

### Required Checks

PR 제출 시 GitHub 워크플로우가 자동으로 검증 수행:

1. **상대 경로 검증** – 내부 링크 모두 작동해야 함
   - VS Code에서 Ctrl+클릭으로 로컬 링크 테스트
   - VS Code 경로 제안(`./`, `../`) 활용

2. **URL 로케일 체크** – 국가별 로케일 포함 URL 없음
   - `/en-us/`, `/en/` 등 제거
   - 일반 국제 URL 사용

3. **깨진 URL 검사** – 모든 URL이 200 상태 반환
   - 제출 전 링크 접근 가능 확인
   - 일부 실패는 네트워크 제한 탓일 수 있음

### PR Title Format

```
[component] Brief description
```

예시:
- `[docs] Phi-4 추론 튜토리얼 추가`
- `[code] ONNX Runtime 연동 예제 수정`
- `[translation] 소개 가이드 일본어 번역 추가`

## Common Development Patterns

### Working with Phi Models

**모델 로드:**
- Transformers, ONNX Runtime, MLX, OpenVINO 등 다양한 프레임워크 활용
- 모델은 주로 Hugging Face, Azure, GitHub Models에서 다운로드
- 하드웨어(CPU, GPU, NPU)와 모델 호환성 확인 필수

**추론 패턴:**
- 텍스트 생성: 대부분 챗/지침 변종 사용
- 비전: Phi-3-vision, Phi-4-multimodal로 이미지 이해
- 오디오: Phi-4-multimodal로 오디오 입력 지원
- 추론: Phi-4-reasoning 변종으로 고급 추론 작업

### Platform-Specific Notes

**Microsoft Foundry:**
- Azure 구독 및 API 키 필요
- `/md/02.QuickStart/AzureAIFoundry_QuickStart.md` 참조

**GitHub Models:**
- 테스트용 무료 플랜 제공
- `/md/02.QuickStart/GitHubModel_QuickStart.md` 참조

**로컬 추론:**
- ONNX Runtime: 크로스 플랫폼, 최적화된 추론
- Ollama: 쉬운 로컬 모델 관리 (개발 컨테이너에 사전 구성)
- Apple MLX: Apple Silicon 최적화

## Troubleshooting

### Common Issues

**메모리 문제:**
- Phi 모델은 많은 RAM 필요 (특히 비전/멀티모달 변종)
- 자원이 제한된 환경에서는 양자화 모델 사용 권장
- `/md/01.Introduction/04/QuantifyingPhi.md` 참고

**종속성 충돌:**
- Python 예제는 특정 버전 요구 가능성 있음
- 각 예제 별 가상 환경 사용 권장
- 개별 `requirements.txt` 파일 확인

**모델 다운로드 실패:**
- 대형 모델은 느린 연결에서 시간 초과 가능성
- 클라우드 환경(Codespaces, Azure) 사용 고려
- Hugging Face 캐시 경로: `~/.cache/huggingface/`

**.NET 프로젝트 문제:**
- .NET 8.0 SDK 설치 확인
- 빌드 전에 `dotnet restore` 실행
- 일부 프로젝트는 CUDA 전용 설정 포함(Debug_Cuda)

**JavaScript/웹 예제:**
- Node.js 18 이상 필요
- 문제 발생 시 `node_modules` 삭제 후 재설치
- 브라우저 콘솔에서 WebGPU 호환성 문제 확인

### Getting Help

- **Discord:** Microsoft Foundry 커뮤니티 Discord 참여
- **GitHub Issues:** 버그 및 문제 보고
- **GitHub Discussions:** 질문 및 정보 공유

## Additional Context

### Responsible AI

모든 Phi 모델 사용은 Microsoft 책임감 있는 AI 원칙 준수:
- 공정성, 신뢰성, 안전성
- 개인정보 보호 및 보안  
- 포괄성, 투명성, 책임성
- 프로덕션 애플리케이션에 Azure AI 콘텐츠 안전성 사용
- `/md/01.Introduction/01/01.AISafety.md` 참고

### Translations

- 50개 이상 언어 자동 GitHub Action 지원
- 번역 파일은 `/translations/` 디렉터리에 위치
- 공동 번역자 워크플로우로 유지 관리
- 번역 파일은 수동 수정 금지 (자동 생성됨)

### Contributing

- `CONTRIBUTING.md` 가이드라인 준수
- 기여자 라이선스 계약(CLA) 동의 필수
- Microsoft 오픈 소스 행동 강령 준수
- 커밋에는 보안 정보 및 인증 정보 포함 금지

### Multi-Language Support

이 저장소는 다음 언어로 된 예제를 포함하는 다중 언어 저장소입니다:
- **Python** - ML/AI 워크플로우, Jupyter 노트북, 미세 조정
- **C#/.NET** - 엔터프라이즈 애플리케이션, ONNX Runtime 통합
- **JavaScript** - 웹 기반 AI, WebGPU를 사용한 브라우저 추론

사용 사례 및 배포 대상에 가장 적합한 언어를 선택하세요.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 된 원문이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->