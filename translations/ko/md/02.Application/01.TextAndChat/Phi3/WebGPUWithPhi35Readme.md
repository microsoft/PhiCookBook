<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-07-17T03:07:37+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "ko"
}
-->
# Phi-3.5-Instruct WebGPU RAG 챗봇

## WebGPU와 RAG 패턴 시연 데모

Phi-3.5 Onnx 호스팅 모델과 함께하는 RAG 패턴은 Retrieval-Augmented Generation 방식을 활용하여, Phi-3.5 모델의 강력함과 ONNX 호스팅의 효율적인 AI 배포를 결합합니다. 이 패턴은 도메인 특화 작업에 맞춘 모델 미세 조정에 유용하며, 품질, 비용 효율성, 그리고 긴 문맥 이해 능력을 모두 제공합니다. Azure AI 제품군의 일부로서, 다양한 산업의 맞춤화 요구를 충족시키기 위해 쉽게 찾고, 시도하며 사용할 수 있는 다양한 모델을 제공합니다.

## WebGPU란 무엇인가  
WebGPU는 웹 브라우저에서 장치의 그래픽 처리 장치(GPU)에 효율적으로 접근할 수 있도록 설계된 최신 웹 그래픽 API입니다. WebGL의 후속으로 개발되었으며, 다음과 같은 주요 개선점을 제공합니다:

1. **최신 GPU와의 호환성**: WebGPU는 Vulkan, Metal, Direct3D 12와 같은 시스템 API를 활용하여 현대 GPU 아키텍처와 원활하게 작동하도록 설계되었습니다.
2. **향상된 성능**: 그래픽 렌더링뿐만 아니라 머신러닝 작업에도 적합한 일반 목적 GPU 연산과 빠른 처리 속도를 지원합니다.
3. **고급 기능 제공**: 더 복잡하고 동적인 그래픽 및 계산 작업을 가능하게 하는 고급 GPU 기능에 접근할 수 있습니다.
4. **JavaScript 작업량 감소**: 더 많은 작업을 GPU에 맡김으로써 JavaScript의 부담을 크게 줄여, 더 나은 성능과 부드러운 사용자 경험을 제공합니다.

현재 WebGPU는 Google Chrome 등 일부 브라우저에서 지원되며, 다른 플랫폼으로의 지원 확대가 진행 중입니다.

### 03.WebGPU  
필수 환경:

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
주소창에 `chrome://flags`를 입력하고 Enter 키를 누릅니다.

#### 플래그 검색:  
페이지 상단 검색창에 'enable-unsafe-webgpu'를 입력합니다.

#### 플래그 활성화:  
검색 결과에서 #enable-unsafe-webgpu 플래그를 찾습니다.

옆의 드롭다운 메뉴를 클릭하고 Enabled를 선택합니다.

#### 브라우저 재시작:  
플래그를 활성화한 후 변경 사항을 적용하려면 브라우저를 재시작해야 합니다. 페이지 하단에 나타나는 Relaunch 버튼을 클릭하세요.

- Linux에서는 `--enable-features=Vulkan` 옵션을 사용해 브라우저를 실행하세요.  
- Safari 18 (macOS 15)에서는 WebGPU가 기본적으로 활성화되어 있습니다.  
- Firefox Nightly에서는 주소창에 about:config를 입력한 후 `dom.webgpu.enabled`를 true로 설정하세요.

### Microsoft Edge에서 GPU 설정하기  

Windows에서 Microsoft Edge에 고성능 GPU를 설정하는 방법은 다음과 같습니다:

- **설정 열기:** 시작 메뉴를 클릭하고 설정을 선택합니다.  
- **시스템 설정:** 시스템 > 디스플레이로 이동합니다.  
- **그래픽 설정:** 아래로 스크롤하여 그래픽 설정을 클릭합니다.  
- **앱 선택:** “선호도를 설정할 앱 선택”에서 데스크톱 앱을 선택한 후 찾아보기를 클릭합니다.  
- **Edge 선택:** Edge 설치 폴더(보통 `C:\Program Files (x86)\Microsoft\Edge\Application`)로 이동하여 `msedge.exe`를 선택합니다.  
- **선호도 설정:** 옵션을 클릭하고 고성능을 선택한 뒤 저장을 클릭합니다.  
이렇게 하면 Microsoft Edge가 더 나은 성능을 위해 고성능 GPU를 사용하게 됩니다.  
- 변경 사항을 적용하려면 **컴퓨터를 재시작**하세요.

### 샘플 : [이 링크를 클릭하세요](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.