<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8de701a2f1eb12b1f82432288d709cf",
  "translation_date": "2025-05-08T05:26:26+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_Nvidia_NIM_Vision.md",
  "language_code": "ko"
}
-->
### 예제 시나리오

이미지(`demo.png`)가 있고 이 이미지를 처리한 후 새 버전(`phi-3-vision.jpg`)을 저장하는 Python 코드를 생성하고 싶다고 가정해봅시다.

위 코드는 다음과 같은 과정을 자동화합니다:

1. 환경과 필요한 설정을 구성합니다.
2. 모델이 필요한 Python 코드를 생성하도록 지시하는 프롬프트를 만듭니다.
3. 프롬프트를 모델에 보내고 생성된 코드를 수집합니다.
4. 생성된 코드를 추출하고 실행합니다.
5. 원본 이미지와 처리된 이미지를 표시합니다.

이 방법은 AI의 힘을 활용하여 이미지 처리 작업을 자동화함으로써 목표 달성을 더 쉽고 빠르게 만들어 줍니다.

[Sample Code Solution](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

전체 코드가 단계별로 무엇을 하는지 살펴보겠습니다:

1. **필요한 패키지 설치**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    이 명령은 `langchain_nvidia_ai_endpoints` 패키지를 최신 버전으로 설치합니다.

2. **필요한 모듈 임포트**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    이 임포트들은 NVIDIA AI 엔드포인트와 상호작용하고, 비밀번호를 안전하게 처리하며, 운영체제와 상호작용하고, base64 형식으로 데이터를 인코딩/디코딩하는 데 필요한 모듈들을 불러옵니다.

3. **API 키 설정**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    이 코드는 `NVIDIA_API_KEY` 환경 변수가 설정되어 있는지 확인합니다. 설정되어 있지 않으면 사용자가 안전하게 API 키를 입력하도록 요청합니다.

4. **모델 및 이미지 경로 정의**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    사용할 모델을 설정하고, 지정된 모델로 `ChatNVIDIA` 인스턴스를 생성하며, 이미지 파일 경로를 정의합니다.

5. **텍스트 프롬프트 생성**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    모델이 이미지를 처리하는 Python 코드를 생성하도록 지시하는 텍스트 프롬프트를 정의합니다.

6. **이미지를 Base64로 인코딩**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    이 코드는 이미지 파일을 읽고 base64로 인코딩한 뒤, 인코딩된 데이터를 포함하는 HTML 이미지 태그를 생성합니다.

7. **텍스트와 이미지를 프롬프트에 결합**:
    ```python
    prompt = f"{text} {image}"
    ```
    텍스트 프롬프트와 HTML 이미지 태그를 하나의 문자열로 결합합니다.

8. **ChatNVIDIA를 사용해 코드 생성**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    이 코드는 프롬프트를 `ChatNVIDIA`에 보내고 생성된 코드를 `code` 문자열로 받습니다.

9. **생성된 내용에서 Python 코드 추출**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    이 과정은 마크다운 형식을 제거하고 실제 Python 코드만 추출합니다.

10. **생성된 코드 실행**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    추출한 Python 코드를 서브프로세스로 실행하고 출력을 캡처합니다.

11. **이미지 표시**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    이 코드들은 `IPython.display` 모듈을 사용해 이미지를 화면에 표시합니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있음을 양지해 주시기 바랍니다. 원문 문서는 해당 언어의 원본이므로 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.