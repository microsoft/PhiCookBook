<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "faa063cfc6d50047bbfdb58a90d520ad",
  "translation_date": "2025-04-04T06:34:16+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\WebGPUWithPhi35Readme.md",
  "language_code": "ko"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## WebGPU 및 RAG 패턴 데모

Phi-3.5 Onnx Hosted 모델과 함께하는 RAG 패턴은 Retrieval-Augmented Generation 접근 방식을 활용하여 효율적인 AI 배포를 가능하게 합니다. 이 패턴은 도메인별 작업에 맞춘 모델을 세밀하게 조정하는 데 유용하며, 품질, 비용 효율성, 긴 문맥 이해를 결합한 솔루션을 제공합니다. Azure AI 제품군의 일부로서 다양한 산업의 맞춤화 요구를 충족시키는 모델을 쉽게 찾고, 시도하고, 사용할 수 있는 광범위한 선택지를 제공합니다.

## WebGPU란 무엇인가
WebGPU는 웹 브라우저에서 장치의 그래픽 처리 장치(GPU)에 직접 효율적으로 접근할 수 있도록 설계된 현대적인 웹 그래픽 API입니다. WebGL의 후속 기술로, 다음과 같은 주요 개선 사항을 제공합니다:

1. **최신 GPU와의 호환성**: WebGPU는 현대적인 GPU 아키텍처와 원활하게 작동하도록 설계되었으며, Vulkan, Metal, Direct3D 12와 같은 시스템 API를 활용합니다.
2. **성능 향상**: 그래픽 렌더링과 머신러닝 작업 모두에 적합한 일반적인 GPU 계산과 빠른 작업을 지원합니다.
3. **고급 기능**: WebGPU는 더 복잡하고 역동적인 그래픽 및 계산 워크로드를 가능하게 하는 고급 GPU 기능에 접근할 수 있습니다.
4. **JavaScript 작업량 감소**: 더 많은 작업을 GPU로 오프로드하여 JavaScript의 작업량을 크게 줄이고 성능과 사용자 경험을 향상시킵니다.

현재 Google Chrome과 같은 브라우저에서 지원되며, 다른 플랫폼으로 지원을 확대하기 위한 작업이 진행 중입니다.

### 03.WebGPU
필수 환경:

**지원 브라우저:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU 활성화 방법:

- Chrome/Microsoft Edge에서 

`chrome://flags/#enable-unsafe-webgpu` 플래그를 활성화합니다.

#### 브라우저 열기:
Google Chrome 또는 Microsoft Edge를 실행합니다.

#### 플래그 페이지 접근:
주소창에 `chrome://flags`를 입력하고 Enter를 누릅니다.

#### 플래그 검색:
페이지 상단의 검색창에 'enable-unsafe-webgpu'를 입력합니다.

#### 플래그 활성화:
결과 목록에서 #enable-unsafe-webgpu 플래그를 찾습니다.

드롭다운 메뉴를 클릭하고 Enabled를 선택합니다.

#### 브라우저 재시작:

플래그를 활성화한 후 변경 사항을 적용하려면 브라우저를 재시작해야 합니다. 페이지 하단에 나타나는 Relaunch 버튼을 클릭하세요.

- Linux에서는 `--enable-features=Vulkan`로 브라우저를 실행합니다.
- Safari 18(macOS 15)에서는 WebGPU가 기본적으로 활성화되어 있습니다.
- Firefox Nightly에서는 주소창에 about:config를 입력하고 `set dom.webgpu.enabled to true`를 사용합니다.

### Microsoft Edge에서 GPU 설정

Windows에서 Microsoft Edge를 고성능 GPU로 설정하는 단계는 다음과 같습니다:

- **설정 열기:** 시작 메뉴를 클릭하고 설정을 선택합니다.
- **시스템 설정:** 시스템으로 이동한 후 디스플레이를 선택합니다.
- **그래픽 설정:** 아래로 스크롤하여 그래픽 설정을 클릭합니다.
- **앱 선택:** “선호도 설정할 앱 선택” 아래에서 데스크톱 앱을 선택한 후 찾아보기를 클릭합니다.
- **Edge 선택:** Edge 설치 폴더(보통 `C:\Program Files (x86)\Microsoft\Edge\Application`)로 이동하여 `msedge.exe`를 선택합니다.
- **선호도 설정:** 옵션을 클릭하고 고성능을 선택한 후 저장을 클릭합니다.
이 설정을 통해 Microsoft Edge가 고성능 GPU를 사용하여 더 나은 성능을 제공합니다.
- **재시작**: 설정이 적용되도록 컴퓨터를 재시작합니다.

### 샘플 : [여기를 클릭하세요](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서(원래 언어로 작성된 문서)가 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역을 사용함으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.