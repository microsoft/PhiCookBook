<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c7a7f2a07dc176c19e1ab9f249b548c9",
  "translation_date": "2025-04-04T05:34:01+00:00",
  "source_file": "code\\08.RAG\\rag_webgpu_chat\\README.md",
  "language_code": "ko"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## WebGPU 및 RAG 패턴 데모
Phi-3 Onnx Hosted 모델을 활용한 RAG 패턴은 Retrieval-Augmented Generation 접근 방식을 기반으로 하며, Phi-3 모델과 ONNX 호스팅의 강력함을 결합하여 효율적인 AI 배포를 제공합니다. 이 패턴은 도메인별 작업을 위한 모델을 세밀하게 조정하는 데 유용하며, 품질, 비용 효율성, 긴 문맥 이해를 균형 있게 제공합니다. 이는 Azure AI의 제품군 일부로, 다양한 산업의 맞춤형 요구를 충족시키기 위해 사용하기 쉽고 찾기 쉬운 모델을 제공합니다. Phi-3 모델(Phi-3-mini, Phi-3-small, Phi-3-medium 포함)은 Azure AI 모델 카탈로그에서 제공되며, HuggingFace와 ONNX 같은 플랫폼을 통해 자체 관리하거나 배포할 수 있습니다. 이는 접근 가능하고 효율적인 AI 솔루션을 제공하려는 Microsoft의 의지를 보여줍니다.

## WebGPU란 무엇인가
WebGPU는 웹 브라우저에서 장치의 그래픽 처리 장치(GPU)에 직접 효율적으로 접근할 수 있도록 설계된 현대적인 웹 그래픽 API입니다. 이는 WebGL의 후속 기술로서 여러 주요 개선 사항을 제공합니다:

1. **최신 GPU와의 호환성**: WebGPU는 Vulkan, Metal, Direct3D 12 같은 시스템 API를 활용하여 현대적인 GPU 아키텍처와 원활하게 작동하도록 설계되었습니다.
2. **성능 향상**: 일반적인 GPU 계산과 빠른 작업을 지원하여 그래픽 렌더링뿐만 아니라 머신 러닝 작업에도 적합합니다.
3. **고급 기능**: WebGPU는 더 복잡하고 동적인 그래픽 및 계산 워크로드를 가능하게 하는 고급 GPU 기능에 접근할 수 있습니다.
4. **JavaScript 작업량 감소**: 더 많은 작업을 GPU에 넘겨줌으로써 JavaScript의 작업량을 크게 줄여 성능 향상과 매끄러운 사용자 경험을 제공합니다.

현재 WebGPU는 Google Chrome 같은 브라우저에서 지원되며, 다른 플랫폼으로 지원을 확장하기 위한 작업이 진행 중입니다.

### 03.WebGPU
필요한 환경:

**지원 브라우저:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU 활성화:

- Chrome/Microsoft Edge에서 

`chrome://flags/#enable-unsafe-webgpu` 플래그를 활성화하세요.

#### 브라우저 열기:
Google Chrome 또는 Microsoft Edge를 실행하세요.

#### 플래그 페이지 접근:
주소창에 `chrome://flags`를 입력하고 Enter를 누르세요.

#### 플래그 검색:
페이지 상단의 검색창에 'enable-unsafe-webgpu'를 입력하세요.

#### 플래그 활성화:
결과 목록에서 #enable-unsafe-webgpu 플래그를 찾으세요.

드롭다운 메뉴를 클릭하고 Enabled를 선택하세요.

#### 브라우저 재시작:

플래그를 활성화한 후 변경 사항을 적용하려면 브라우저를 재시작해야 합니다. 페이지 하단에 나타나는 Relaunch 버튼을 클릭하세요.

- Linux의 경우 `--enable-features=Vulkan`로 브라우저를 실행하세요.
- Safari 18(macOS 15)은 기본적으로 WebGPU가 활성화되어 있습니다.
- Firefox Nightly에서는 주소창에 about:config를 입력하고 `set dom.webgpu.enabled to true`를 사용하세요.

### Microsoft Edge용 GPU 설정 

Windows에서 Microsoft Edge에 고성능 GPU를 설정하는 단계는 다음과 같습니다:

- **설정 열기:** 시작 메뉴를 클릭하고 설정을 선택하세요.
- **시스템 설정:** 시스템으로 이동한 후 디스플레이를 선택하세요.
- **그래픽 설정:** 아래로 스크롤하여 그래픽 설정을 클릭하세요.
- **앱 선택:** "앱 선택하여 설정 선호도 지정"에서 데스크톱 앱을 선택한 후 찾아보기를 클릭하세요.
- **Edge 선택:** Edge 설치 폴더(일반적으로 `C:\Program Files (x86)\Microsoft\Edge\Application`)로 이동하여 `msedge.exe`를 선택하세요.
- **선호도 설정:** 옵션을 클릭하고 고성능을 선택한 후 저장을 클릭하세요.
이 설정은 Microsoft Edge가 더 나은 성능을 위해 고성능 GPU를 사용하도록 보장합니다. 
- **재시작**: 설정이 적용되도록 컴퓨터를 재시작하세요.

### Codespace 열기:
GitHub의 저장소로 이동하세요.
코드 버튼을 클릭하고 Codespaces로 열기를 선택하세요.

Codespace가 아직 없다면 새 Codespace를 생성할 수 있습니다.

**참고** Codespace에 Node 환경 설치하기
GitHub Codespace에서 npm 데모를 실행하는 것은 프로젝트를 테스트하고 개발하는 훌륭한 방법입니다. 다음은 시작하는 데 도움이 되는 단계별 가이드입니다:

### 환경 설정:
Codespace가 열리면 Node.js와 npm이 설치되어 있는지 확인하세요. 아래 명령어를 실행하여 확인할 수 있습니다:
```
node -v
```
```
npm -v
```

설치되어 있지 않다면 다음을 사용하여 설치할 수 있습니다:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### 프로젝트 디렉터리로 이동:
터미널을 사용하여 npm 프로젝트가 있는 디렉터리로 이동하세요:
```
cd path/to/your/project
```

### 종속성 설치:
package.json 파일에 나열된 필요한 모든 종속성을 설치하려면 다음 명령어를 실행하세요:

```
npm install
```

### 데모 실행:
종속성이 설치되면 데모 스크립트를 실행할 수 있습니다. 이는 일반적으로 package.json의 scripts 섹션에 지정되어 있습니다. 예를 들어, 데모 스크립트 이름이 start라면 다음 명령어를 실행하세요:

```
npm run build
```
```
npm run dev
```

### 데모 접근:
데모가 웹 서버와 관련이 있다면 Codespaces에서 URL을 제공하여 접근할 수 있습니다. 알림을 확인하거나 Ports 탭에서 URL을 찾아보세요.

**참고:** 모델은 브라우저에 캐시되어야 하므로 로드하는 데 시간이 걸릴 수 있습니다.

### RAG 데모
마크다운 파일 `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`를 업로드하세요.

### 파일 선택:
"파일 선택" 버튼을 클릭하여 업로드할 문서를 선택하세요.

### 문서 업로드:
파일을 선택한 후 "업로드" 버튼을 클릭하여 RAG(Retrieval-Augmented Generation)를 위한 문서를 로드하세요.

### 채팅 시작:
문서를 업로드한 후 문서 내용을 기반으로 RAG를 사용하여 채팅 세션을 시작할 수 있습니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역은 오류나 부정확한 내용이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태로 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역을 사용하는 과정에서 발생하는 오해나 잘못된 해석에 대해 책임지지 않습니다.