<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f0858a9f2cc1889ab0e90cb9c63c044",
  "translation_date": "2025-04-04T07:12:14+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Qlora.md",
  "language_code": "ko"
}
-->
**Phi-3을 QLoRA로 미세 조정하기**

[QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora)를 사용하여 Microsoft의 Phi-3 Mini 언어 모델을 미세 조정합니다.

QLoRA는 대화 이해와 응답 생성 능력을 향상시키는 데 도움을 줍니다.

transformers와 bitsandbytes를 사용하여 모델을 4비트로 로드하려면, accelerate와 transformers를 소스에서 설치하고 bitsandbytes 라이브러리의 최신 버전을 확인해야 합니다.

**샘플**
- [이 샘플 노트북에서 자세히 알아보기](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python 미세 조정 샘플 예제](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub에서 LORA를 사용한 미세 조정 예제](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub에서 QLORA를 사용한 미세 조정 예제](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원문 문서는 해당 언어로 작성된 권위 있는 자료로 간주되어야 합니다. 중요한 정보에 대해서는 전문 번역가의 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.