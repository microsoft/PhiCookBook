<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-08T06:37:18+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "ko"
}
-->
# Olive를 사용하여 Phi3 미세 조정하기

이 예제에서는 Olive를 사용하여:

1. LoRA 어댑터를 미세 조정해 문구를 Sad, Joy, Fear, Surprise로 분류합니다.
1. 어댑터 가중치를 기본 모델에 병합합니다.
1. 모델을 최적화하고 `int4` 형식으로 양자화합니다.

또한 ONNX Runtime(ORT) Generate API를 사용해 미세 조정된 모델을 추론하는 방법도 보여드립니다.

> **⚠️ 미세 조정을 위해서는 적절한 GPU가 필요합니다 - 예를 들어 A10, V100, A100 등이 있습니다.**

## 💾 설치

새 Python 가상 환경을 만듭니다 (예: `conda` 사용):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

다음으로 Olive와 미세 조정 워크플로우에 필요한 종속 항목을 설치하세요:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Olive를 사용하여 Phi3 미세 조정하기
[Olive 구성 파일](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json)에는 다음 *패스*로 구성된 *워크플로우*가 포함되어 있습니다:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

대략적으로, 이 워크플로우는 다음을 수행합니다:

1. [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) 데이터를 사용해 Phi3를 150 스텝(수정 가능) 동안 미세 조정합니다.
1. LoRA 어댑터 가중치를 기본 모델에 병합합니다. 이로써 ONNX 형식의 단일 모델 아티팩트를 얻게 됩니다.
1. Model Builder가 ONNX 런타임용으로 모델을 최적화하고 `int4`로 양자화합니다.

워크플로우를 실행하려면 다음을 실행하세요:

```bash
olive run --config phrase-classification.json
```

Olive가 완료되면 최적화된 `int4` 형식의 미세 조정된 Phi3 모델을 `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`에서 확인할 수 있습니다.

## 🧑‍💻 미세 조정된 Phi3를 애플리케이션에 통합하기

앱을 실행하려면:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

이 응답은 문구에 대한 단일 단어 분류 결과(Sad/Joy/Fear/Surprise)를 반환합니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있음을 유의하시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.