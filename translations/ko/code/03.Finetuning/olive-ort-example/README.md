<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aed7639909ebbd1960507880cff2ae4c",
  "translation_date": "2025-04-04T05:23:28+00:00",
  "source_file": "code\\03.Finetuning\\olive-ort-example\\README.md",
  "language_code": "ko"
}
-->
# Olive을 사용하여 Phi3 미세 조정하기

이 예제에서는 Olive를 사용하여 다음 작업을 수행합니다:

1. LoRA 어댑터를 미세 조정하여 문구를 Sad, Joy, Fear, Surprise로 분류합니다.
1. 어댑터 가중치를 기본 모델에 병합합니다.
1. 모델을 `int4`로 최적화하고 양자화합니다.

또한 ONNX Runtime (ORT) Generate API를 사용하여 미세 조정된 모델을 추론하는 방법도 보여드립니다.

> **⚠️ 미세 조정을 위해서는 적합한 GPU가 필요합니다 - 예를 들어, A10, V100, A100 등이 있습니다.**

## 💾 설치

새로운 Python 가상 환경을 만듭니다 (예: `conda` 사용):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

다음으로, Olive와 미세 조정 워크플로우에 필요한 종속성을 설치합니다:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive을 사용하여 Phi3 미세 조정하기
[Olive 구성 파일](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json)에는 다음 *패스*를 포함한 *워크플로우*가 포함되어 있습니다:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

이 워크플로우는 다음과 같은 고수준 작업을 수행합니다:

1. [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) 데이터를 사용하여 Phi3를 미세 조정합니다 (150 스텝으로 설정되어 있으며 수정 가능).
1. LoRA 어댑터 가중치를 기본 모델에 병합합니다. 이를 통해 ONNX 형식의 단일 모델 아티팩트를 얻을 수 있습니다.
1. Model Builder는 모델을 ONNX 런타임에 최적화하고 모델을 `int4`로 양자화합니다.

워크플로우를 실행하려면 다음 명령을 실행합니다:

```bash
olive run --config phrase-classification.json
```

Olive 작업이 완료되면, 최적화된 `int4` 미세 조정된 Phi3 모델은 `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`에 저장됩니다.

## 🧑‍💻 미세 조정된 Phi3를 애플리케이션에 통합하기 

애플리케이션을 실행하려면:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

응답은 문구에 대한 단어 하나로 분류됩니다 (Sad/Joy/Fear/Surprise).

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하지만, 자동 번역은 오류나 부정확성을 포함할 수 있습니다. 원어로 작성된 원본 문서를 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역을 사용함으로써 발생할 수 있는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.