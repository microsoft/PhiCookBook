<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-07-16T17:14:44+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "ko"
}
-->
Phi-3-mini WebGPU RAG 챗봇

## WebGPU와 RAG 패턴 시연 데모
Phi-3 Onnx 호스팅 모델과 함께하는 RAG 패턴은 Retrieval-Augmented Generation 방식을 활용하여 Phi-3 모델의 강력함과 ONNX 호스팅의 효율적인 AI 배포를 결합합니다. 이 패턴은 도메인 특화 작업에 맞춘 모델 미세 조정에 유용하며, 품질, 비용 효율성, 그리고 긴 문맥 이해 능력을 모두 제공합니다. Azure AI의 제품군 중 하나로, 다양한 산업의 맞춤화 요구를 충족시키기 위해 쉽게 찾고, 시도하며 사용할 수 있는 다양한 모델을 제공합니다. Phi-3-mini, Phi-3-small, Phi-3-medium을 포함한 Phi-3 모델들은 Azure AI 모델 카탈로그에서 제공되며, 자체 관리 또는 HuggingFace, ONNX 같은 플랫폼을 통해 미세 조정 및 배포가 가능하여 마이크로소프트의 접근성 높고 효율적인 AI 솔루션에 대한 의지를 보여줍니다.

## WebGPU란 무엇인가
WebGPU는 웹 브라우저에서 장치의 그래픽 처리 장치(GPU)에 효율적으로 접근할 수 있도록 설계된 최신 웹 그래픽 API입니다. WebGL의 후속으로 개발되었으며, 다음과 같은 주요 개선점을 제공합니다:

1. **최신 GPU와의 호환성**: Vulkan, Metal, Direct3D 12 같은 시스템 API를 활용하여 현대 GPU 아키텍처와 원활하게 작동합니다.
2. **향상된 성능**: 그래픽 렌더링뿐만 아니라 머신러닝 작업에도 적합한 범용 GPU 연산과 빠른 처리 속도를 지원합니다.
3. **고급 기능 제공**: 더 복잡하고 동적인 그래픽 및 계산 작업을 가능하게 하는 고급 GPU 기능에 접근할 수 있습니다.
4. **JavaScript 작업량 감소**: 더 많은 작업을 GPU에 오프로드하여 JavaScript의 부담을 크게 줄이고, 더 나은 성능과 부드러운 사용자 경험을 제공합니다.

현재 WebGPU는 Google Chrome 등 일부 브라우저에서 지원되며, 다른 플랫폼으로의 지원 확대가 진행 중입니다.

### 03.WebGPU
필요 환경:

**지원 브라우저:**  
- Google Chrome 113 이상  
- Microsoft Edge 113 이상  
- Safari 18 (macOS 15)  
- Firefox Nightly

### WebGPU 활성화 방법:

- Chrome/Microsoft Edge에서

`chrome://flags/#enable-unsafe-webgpu` 플래그를 활성화하세요.

#### 브라우저 열기:
Google Chrome 또는 Microsoft Edge를 실행합니다.

#### 플래그 페이지 접속:
주소창에 `chrome://flags`를 입력하고 Enter를 누릅니다.

#### 플래그 검색:
페이지 상단 검색창에 'enable-unsafe-webgpu'를 입력합니다.

#### 플래그 활성화:
검색 결과에서 #enable-unsafe-webgpu 플래그를 찾습니다.

옆의 드롭다운 메뉴를 클릭하고 Enabled를 선택합니다.

#### 브라우저 재시작:
플래그를 활성화한 후 변경 사항을 적용하려면 브라우저를 재시작해야 합니다. 페이지 하단에 나타나는 Relaunch 버튼을 클릭하세요.

- Linux에서는 `--enable-features=Vulkan` 옵션을 사용해 브라우저를 실행하세요.
- Safari 18 (macOS 15)은 기본적으로 WebGPU가 활성화되어 있습니다.
- Firefox Nightly에서는 주소창에 about:config를 입력한 후 `dom.webgpu.enabled`를 true로 설정하세요.

### Microsoft Edge용 GPU 설정 방법

Windows에서 Microsoft Edge에 고성능 GPU를 설정하는 방법은 다음과 같습니다:

- **설정 열기:** 시작 메뉴에서 설정을 선택합니다.
- **시스템 설정:** 시스템 > 디스플레이로 이동합니다.
- **그래픽 설정:** 아래로 스크롤하여 그래픽 설정을 클릭합니다.
- **앱 선택:** “선호도를 설정할 앱 선택”에서 데스크톱 앱을 선택한 후 찾아보기를 클릭합니다.
- **Edge 선택:** Edge 설치 폴더(보통 `C:\Program Files (x86)\Microsoft\Edge\Application`)로 이동하여 `msedge.exe`를 선택합니다.
- **선호도 설정:** 옵션을 클릭하고 고성능을 선택한 후 저장을 클릭합니다.  
이렇게 하면 Microsoft Edge가 더 나은 성능을 위해 고성능 GPU를 사용하게 됩니다.  
- 변경 사항 적용을 위해 컴퓨터를 재시작하세요.

### Codespace 열기:
GitHub에서 저장소로 이동합니다.  
Code 버튼을 클릭하고 Open with Codespaces를 선택합니다.

Codespace가 없다면 New codespace를 클릭해 새로 만들 수 있습니다.

**참고** Codespace에서 Node 환경 설치하기  
GitHub Codespace에서 npm 데모를 실행하는 것은 프로젝트를 테스트하고 개발하는 좋은 방법입니다. 시작하는 데 도움이 되는 단계별 가이드입니다:

### 환경 설정:
Codespace가 열리면 Node.js와 npm이 설치되어 있는지 확인하세요. 다음 명령어로 확인할 수 있습니다:  
```
node -v
```  
```
npm -v
```

설치되어 있지 않다면 다음 명령어로 설치하세요:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### 프로젝트 디렉터리로 이동:
터미널에서 npm 프로젝트가 위치한 디렉터리로 이동하세요:  
```
cd path/to/your/project
```

### 의존성 설치:
package.json에 명시된 모든 의존성을 설치하려면 다음 명령어를 실행하세요:  
```
npm install
```

### 데모 실행:
의존성 설치가 완료되면 데모 스크립트를 실행할 수 있습니다. 보통 package.json의 scripts 섹션에 정의되어 있습니다. 예를 들어 데모 스크립트 이름이 start라면 다음과 같이 실행합니다:  
```
npm run build
```  
```
npm run dev
```

### 데모 접속:
웹 서버가 포함된 데모라면 Codespaces가 접속할 수 있는 URL을 제공합니다. 알림을 확인하거나 Ports 탭에서 URL을 찾으세요.

**참고:** 모델이 브라우저에 캐시되어야 하므로 로딩에 시간이 걸릴 수 있습니다.

### RAG 데모
RAG 솔루션을 완성하려면 마크다운 파일 `intro_rag.md`를 업로드하세요. Codespaces를 사용하는 경우 `01.InferencePhi3/docs/` 경로에서 파일을 다운로드할 수 있습니다.

### 파일 선택:
“Choose File” 버튼을 클릭해 업로드할 문서를 선택하세요.

### 문서 업로드:
파일을 선택한 후 “Upload” 버튼을 눌러 RAG(검색 증강 생성)를 위한 문서를 불러옵니다.

### 채팅 시작:
문서가 업로드되면 해당 문서 내용을 기반으로 RAG를 사용해 채팅 세션을 시작할 수 있습니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.