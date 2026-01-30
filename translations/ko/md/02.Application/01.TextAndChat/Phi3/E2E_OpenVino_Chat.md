[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

이 코드는 모델을 OpenVINO 형식으로 내보내고, 불러와서 주어진 프롬프트에 대한 응답을 생성하는 데 사용합니다.

1. **모델 내보내기**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - 이 명령은 `optimum-cli` 도구를 사용하여 모델을 효율적인 추론에 최적화된 OpenVINO 형식으로 내보냅니다.
   - 내보내는 모델은 `"microsoft/Phi-3-mini-4k-instruct"`이며, 과거 문맥을 기반으로 텍스트를 생성하는 작업에 맞춰져 있습니다.
   - 모델의 가중치는 4비트 정수(`int4`)로 양자화되어 모델 크기를 줄이고 처리 속도를 높입니다.
   - `group-size`, `ratio`, `sym` 같은 다른 매개변수들은 양자화 과정을 세밀하게 조정하는 데 사용됩니다.
   - 내보낸 모델은 `./model/phi3-instruct/int4` 디렉터리에 저장됩니다.

2. **필요한 라이브러리 가져오기**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - 이 부분은 모델을 불러오고 사용하기 위해 `transformers` 라이브러리와 `optimum.intel.openvino` 모듈에서 클래스를 가져옵니다.

3. **모델 디렉터리 및 설정 구성**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir`는 모델 파일이 저장된 위치를 지정합니다.
   - `ov_config`는 OpenVINO 모델이 낮은 지연 시간을 우선시하고, 하나의 추론 스트림을 사용하며, 캐시 디렉터리를 사용하지 않도록 설정하는 딕셔너리입니다.

4. **모델 불러오기**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - 이 코드는 앞서 정의한 설정을 사용해 지정된 디렉터리에서 모델을 불러옵니다. 필요 시 원격 코드 실행도 허용합니다.

5. **토크나이저 불러오기**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - 이 코드는 텍스트를 모델이 이해할 수 있는 토큰으로 변환하는 토크나이저를 불러옵니다.

6. **토크나이저 인자 설정**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - 이 딕셔너리는 특수 토큰이 토크나이즈된 출력에 추가되지 않도록 지정합니다.

7. **프롬프트 정의하기**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - 이 문자열은 사용자가 AI 어시스턴트에게 자기소개를 요청하는 대화 프롬프트를 설정합니다.

8. **프롬프트 토크나이즈하기**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - 이 코드는 프롬프트를 모델이 처리할 수 있는 토큰으로 변환하며, 결과를 PyTorch 텐서 형태로 반환합니다.

9. **응답 생성하기**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - 이 코드는 입력 토큰을 바탕으로 최대 1024개의 새로운 토큰을 생성하여 모델이 응답을 만듭니다.

10. **응답 디코딩하기**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - 이 코드는 생성된 토큰을 사람이 읽을 수 있는 문자열로 변환하며, 특수 토큰은 건너뛰고 첫 번째 결과를 가져옵니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.