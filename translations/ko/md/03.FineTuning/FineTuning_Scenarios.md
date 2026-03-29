## 세밀 조정 시나리오

![FineTuning with MS Services](../../../../translated_images/ko/FinetuningwithMS.3d0cec8ae693e094.webp)

이 섹션에서는 Microsoft Foundry 및 Azure 환경에서의 세밀 조정 시나리오에 대해 배포 모델, 인프라 계층 및 일반적으로 사용되는 최적화 기법을 포함하여 개요를 제공합니다.

<strong>플랫폼</strong>  
이에는 Microsoft Foundry(구 Microsoft Foundry) 및 Azure Machine Learning과 같은 관리형 서비스가 포함되며, 모델 관리, 오케스트레이션, 실험 추적 및 배포 워크플로를 제공합니다.

<strong>인프라</strong>  
세밀 조정에는 확장 가능한 컴퓨팅 리소스가 필요합니다. Azure 환경에서는 일반적으로 GPU 기반 가상 머신과 경량 워크로드용 CPU 리소스, 데이터 세트 및 체크포인트용 확장 가능한 스토리지가 포함됩니다.

**도구 및 프레임워크**  
세밀 조정 워크플로는 일반적으로 Hugging Face Transformers, DeepSpeed, PEFT(Parameter-Efficient Fine-Tuning)와 같은 프레임워크 및 최적화 라이브러리에 의존합니다.

Microsoft 기술을 활용한 세밀 조정 프로세스는 플랫폼 서비스, 컴퓨팅 인프라 및 훈련 프레임워크에 걸쳐 있습니다. 이러한 구성 요소가 어떻게 함께 작동하는지 이해함으로써 개발자는 기본 모델을 특정 작업과 프로덕션 시나리오에 효율적으로 적응시킬 수 있습니다.

## 서비스로서의 모델

호스팅된 세밀 조정을 사용하여 컴퓨팅을 생성 및 관리할 필요 없이 모델을 세밀 조정합니다.

![MaaS Fine Tuning](../../../../translated_images/ko/MaaSfinetune.3eee4630607aff0d.webp)

서버리스 세밀 조정은 이제 Phi-3, Phi-3.5, Phi-4 모델 군에 제공되어, 개발자가 컴퓨팅을 준비하지 않고도 클라우드 및 엣지 시나리오에 맞게 모델을 빠르고 쉽게 맞춤화할 수 있습니다.

## 플랫폼으로서의 모델

사용자가 직접 컴퓨팅을 관리하여 모델을 세밀 조정합니다.

![Maap Fine Tuning](../../../../translated_images/ko/MaaPFinetune.fd3829c1122f5d1c.webp)

[Fine Tuning Sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## 세밀 조정 기법 비교

|시나리오|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DoRA|
|---|---|---|---|---|---|---|
|사전 학습된 LLM을 특정 작업 또는 도메인에 적합하게 조정|예|예|예|예|예|예|
|텍스트 분류, 개체명 인식, 기계 번역과 같은 NLP 작업용 세밀 조정|예|예|예|예|예|예|
|QA 작업용 세밀 조정|예|예|예|예|예|예|
|챗봇에서 인간과 같은 응답 생성용 세밀 조정|예|예|예|예|예|예|
|음악, 예술 또는 기타 창의적 형태 생성용 세밀 조정|예|예|예|예|예|예|
|계산 및 비용 절감|예|예|예|예|예|예|
|메모리 사용량 절감|예|예|예|예|예|예|
|효율적인 세밀 조정을 위한 적은 수 파라미터 사용|예|예|예|아니요|아니요|예|
|사용 가능한 모든 GPU 장치의 총 GPU 메모리에 접근 가능한 메모리 효율적 데이터 병렬 방식|아니요|아니요|아니요|예|예|아니요|

> [!NOTE]
> LoRA, QLoRA, PEFT 및 DoRA는 파라미터 효율적 세밀 조정 방식이며, DeepSpeed와 ZeRO는 분산 학습 및 메모리 최적화에 중점을 둡니다.

## 세밀 조정 성능 예제

![Finetuning Performance](../../../../translated_images/ko/Finetuningexamples.a9a41214f8f5afc1.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의해 주시기 바랍니다. 원본 문서는 해당 원어로 된 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->