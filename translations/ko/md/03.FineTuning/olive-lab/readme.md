<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "76956c0c22e5686908a6d85ec72126af",
  "translation_date": "2025-04-04T07:20:59+00:00",
  "source_file": "md\\03.FineTuning\\olive-lab\\readme.md",
  "language_code": "ko"
}
-->
# Lab. AI 모델의 디바이스 내 추론 최적화

## 소개

> [!IMPORTANT]
> 이 실습에는 **Nvidia A10 또는 A100 GPU**와 관련 드라이버 및 CUDA 툴킷(버전 12+)이 설치되어 있어야 합니다.

> [!NOTE]
> 이 실습은 **35분**이 소요되며, OLIVE를 사용하여 디바이스 내 추론을 위해 모델을 최적화하는 핵심 개념에 대해 실습할 수 있습니다.

## 학습 목표

이 실습을 완료하면 OLIVE를 사용하여 다음을 수행할 수 있습니다:

- AWQ 양자화 방법을 사용하여 AI 모델을 양자화합니다.
- 특정 작업에 맞게 AI 모델을 미세 조정합니다.
- ONNX Runtime에서 효율적인 디바이스 내 추론을 위해 LoRA 어댑터(미세 조정된 모델)를 생성합니다.

### Olive란 무엇인가?

Olive (*O*NNX *live*)는 ONNX Runtime +++https://onnxruntime.ai+++용 모델을 품질과 성능을 갖춘 상태로 배포할 수 있게 해주는 모델 최적화 툴킷 및 CLI입니다.

![Olive Flow](../../../../../translated_images/olive-flow.9e6a284c256068568eb569a242b22dd2e7ec6e73f292d98272398739537ef513.ko.png)

Olive의 입력은 일반적으로 PyTorch 또는 Hugging Face 모델이며, 출력은 ONNX Runtime을 실행하는 디바이스(배포 대상)에서 실행되는 최적화된 ONNX 모델입니다. Olive는 하드웨어 벤더(예: Qualcomm, AMD, Nvidia 또는 Intel)가 제공하는 배포 대상의 AI 가속기(NPU, GPU, CPU)에 맞게 모델을 최적화합니다.

Olive는 개별 모델 최적화 작업인 *패스*로 구성된 순차적 워크플로를 실행합니다. 예시 패스로는 모델 압축, 그래프 캡처, 양자화, 그래프 최적화 등이 있습니다. 각 패스는 정확도와 지연 시간 같은 최적의 메트릭을 달성하기 위해 조정 가능한 매개변수를 가지고 있으며, 이는 해당 평가자가 평가합니다. Olive는 검색 알고리즘을 사용하여 각 패스를 개별적으로 또는 그룹으로 자동 조정하는 검색 전략을 채택합니다.

#### Olive의 이점

- 그래프 최적화, 압축 및 양자화를 위한 다양한 기술을 수동으로 실험하는 데 드는 **시간과 좌절감을 줄입니다**. 품질 및 성능 제약 조건을 정의하고 Olive가 자동으로 최적의 모델을 찾아줍니다.
- **최첨단 기술**을 포함하는 **40개 이상의 내장 모델 최적화 구성 요소**를 제공합니다.
- **사용하기 쉬운 CLI**로 일반적인 모델 최적화 작업을 수행합니다. 예: olive quantize, olive auto-opt, olive finetune.
- 모델 패키징 및 배포가 내장되어 있습니다.
- **멀티 LoRA 서빙**을 위한 모델 생성 지원.
- YAML/JSON을 사용하여 모델 최적화 및 배포 작업을 조율하는 워크플로 구성.
- **Hugging Face** 및 **Azure AI** 통합.
- **캐싱** 메커니즘이 내장되어 **비용 절감** 가능.

## 실습 지침
> [!NOTE]
> Azure AI Hub 및 프로젝트를 설정하고 Lab 1에서 A100 컴퓨팅을 구성했는지 확인하십시오.

### 단계 0: Azure AI 컴퓨팅 연결

**VS Code**의 원격 기능을 사용하여 Azure AI 컴퓨팅에 연결합니다.

1. **VS Code** 데스크톱 애플리케이션을 엽니다.
1. **명령 팔레트**를 **Shift+Ctrl+P**로 엽니다.
1. 명령 팔레트에서 **AzureML - remote: Connect to compute instance in New Window**를 검색합니다.
1. 화면의 지침을 따라 컴퓨팅에 연결합니다. 이는 Lab 1에서 설정한 Azure 구독, 리소스 그룹, 프로젝트 및 컴퓨팅 이름을 선택하는 과정을 포함합니다.
1. Azure ML 컴퓨팅 노드에 연결되면 **Visual Code의 왼쪽 하단**에 표시됩니다 `><Azure ML: Compute Name`

### 단계 1: 리포지토리 클론

VS Code에서 **Ctrl+J**로 새 터미널을 열고 이 리포지토리를 클론합니다.

터미널에서 다음 프롬프트를 확인하십시오:

```
azureuser@computername:~/cloudfiles/code$ 
```
솔루션 클론

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### 단계 2: VS Code에서 폴더 열기

관련 폴더에서 VS Code를 열려면 터미널에서 다음 명령을 실행하면 새 창이 열립니다:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

또는 **파일** > **폴더 열기**를 선택하여 폴더를 열 수 있습니다.

### 단계 3: 종속성 설치

Azure AI 컴퓨팅 인스턴스의 VS Code에서 터미널 창을 열고(팁: **Ctrl+J**) 다음 명령을 실행하여 종속성을 설치합니다:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> 모든 종속성을 설치하는 데 **약 5분**이 소요됩니다.

이 실습에서는 모델을 다운로드하고 Azure AI 모델 카탈로그에 업로드합니다. 모델 카탈로그에 액세스하려면 Azure에 로그인해야 합니다:

```bash
az login
```

> [!NOTE]
> 로그인 시 구독을 선택하라는 메시지가 표시됩니다. 이 실습에 제공된 구독을 설정했는지 확인하십시오.

### 단계 4: Olive 명령 실행

Azure AI 컴퓨팅 인스턴스의 VS Code에서 터미널 창을 열고(팁: **Ctrl+J**) `olive-ai` Conda 환경이 활성화되어 있는지 확인합니다:

```bash
conda activate olive-ai
```

다음 Olive 명령을 명령줄에서 실행합니다.

1. **데이터 확인:** 이번 예제에서는 여행 관련 질문에 답변할 수 있도록 Phi-3.5-Mini 모델을 미세 조정합니다. 아래 코드는 JSON 라인 형식으로 된 데이터셋의 첫 번째 몇 개의 레코드를 표시합니다:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **모델 양자화:** 모델을 학습시키기 전에 Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ 기법을 사용하는 다음 명령으로 양자화합니다. AWQ는 추론 중 생성된 활성화를 고려하여 모델의 가중치를 양자화합니다. 이는 활성화의 실제 데이터 분포를 고려하므로 전통적인 가중치 양자화 방법에 비해 모델 정확도를 더 잘 유지할 수 있습니다.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    AWQ 양자화를 완료하는 데 **약 8분**이 소요되며, **모델 크기가 약 7.5GB에서 약 2.5GB로 줄어듭니다**.
   
   이 실습에서는 Hugging Face에서 모델을 가져오는 방법을 보여줍니다(예: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` 명령은 양자화된 모델을 미세 조정합니다. 양자화 후가 아니라 *전에* 모델을 미세 조정하면 양자화로 인한 손실을 일부 회복하므로 더 나은 정확도를 제공합니다.
    
    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```
    
    미세 조정(100단계 완료)에 **약 6분**이 소요됩니다.

1. **최적화:** 모델이 학습된 후 Olive의 `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` 인수를 사용하여 모델을 최적화합니다 - 이 실습에서는 CPU를 사용합니다.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```
    
    최적화를 완료하는 데 **약 5분**이 소요됩니다.

### 단계 5: 모델 추론 간단 테스트

모델의 추론을 테스트하려면 **app.py**라는 Python 파일을 폴더에 생성하고 다음 코드를 복사하여 붙여넣으십시오:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

다음 명령으로 코드를 실행합니다:

```bash
python app.py
```

### 단계 6: 모델을 Azure AI에 업로드

모델을 Azure AI 모델 리포지토리에 업로드하면 개발 팀의 다른 멤버와 공유할 수 있으며 모델의 버전 관리를 처리할 수 있습니다. 모델을 업로드하려면 다음 명령을 실행하십시오:

> [!NOTE]
> `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"와 Azure AI 프로젝트 이름을 업데이트하고 다음 명령을 실행하십시오 

```
az ml workspace show
```

또는 +++ai.azure.com+++에 접속하여 **관리 센터** **프로젝트** **개요**를 선택하십시오.

`{}` 자리 표시자를 리소스 그룹 이름과 Azure AI 프로젝트 이름으로 업데이트하십시오.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
업로드된 모델을 확인하고 https://ml.azure.com/model/list에서 모델을 배포할 수 있습니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역은 오류나 부정확한 내용을 포함할 수 있음을 유의하시기 바랍니다. 원문이 작성된 언어의 원본 문서를 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 이 번역을 사용하여 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.