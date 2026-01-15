<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "743d7e9cb9c4e8ea642d77bee657a7fa",
  "translation_date": "2025-07-17T09:53:39+00:00",
  "source_file": "md/03.FineTuning/LetPhi3gotoIndustriy.md",
  "language_code": "ko"
}
-->
# **Phi-3를 산업 전문가로 만들기**

Phi-3 모델을 산업에 적용하려면 산업 비즈니스 데이터를 Phi-3 모델에 추가해야 합니다. 두 가지 옵션이 있는데, 첫 번째는 RAG(Retrieval Augmented Generation)이고 두 번째는 Fine Tuning입니다.

## **RAG와 Fine-Tuning 비교**

### **Retrieval Augmented Generation**

RAG는 데이터 검색과 텍스트 생성을 결합한 방식입니다. 기업의 구조화된 데이터와 비구조화된 데이터를 벡터 데이터베이스에 저장합니다. 관련 내용을 검색할 때, 관련 요약과 내용을 찾아 컨텍스트를 형성하고, LLM/SLM의 텍스트 완성 기능과 결합해 콘텐츠를 생성합니다.

### **Fine-tuning**

Fine-tuning은 특정 모델을 개선하는 방식입니다. 모델 알고리즘부터 시작할 필요는 없지만, 데이터를 지속적으로 축적해야 합니다. 산업 응용에서 더 정확한 용어와 언어 표현이 필요하다면 Fine-tuning이 더 적합합니다. 하지만 데이터가 자주 변경된다면 Fine-tuning은 복잡해질 수 있습니다.

### **선택 방법**

1. 외부 데이터 도입이 필요한 답변이라면 RAG가 최선의 선택입니다.

2. 안정적이고 정밀한 산업 지식 출력을 원한다면 Fine-tuning이 좋은 선택입니다. RAG는 관련 콘텐츠를 우선적으로 끌어오지만 전문적인 뉘앙스를 항상 완벽히 반영하지는 못할 수 있습니다.

3. Fine-tuning은 고품질 데이터 세트가 필요하며, 데이터 범위가 작으면 큰 차이를 만들지 못합니다. RAG는 더 유연합니다.

4. Fine-tuning은 내부 메커니즘을 이해하기 어려운 블랙박스 같은 성격이지만, RAG는 데이터 출처를 쉽게 찾을 수 있어 환각이나 콘텐츠 오류를 효과적으로 조정하고 투명성을 높일 수 있습니다.

### **적용 시나리오**

1. 특정 전문 용어와 표현이 필요한 수직 산업에는 ***Fine-tuning***이 최적입니다.

2. 다양한 지식 포인트를 종합하는 QA 시스템에는 ***RAG***가 최적입니다.

3. 자동화된 비즈니스 흐름 결합에는 ***RAG + Fine-tuning***이 최적입니다.

## **RAG 사용법**

![rag](../../../../translated_images/ko/rag.2014adc59e6f6007.png)

벡터 데이터베이스는 데이터를 수학적 형태로 저장한 집합입니다. 벡터 데이터베이스는 머신러닝 모델이 이전 입력을 기억하기 쉽게 만들어, 검색, 추천, 텍스트 생성 등 다양한 활용 사례를 지원할 수 있게 합니다. 데이터는 정확한 일치가 아닌 유사도 기준으로 식별되어 컴퓨터 모델이 데이터의 맥락을 이해할 수 있습니다.

벡터 데이터베이스는 RAG 구현의 핵심입니다. text-embedding-3, jina-ai-embedding 등 벡터 모델을 통해 데이터를 벡터 형태로 변환해 저장할 수 있습니다.

RAG 애플리케이션 생성에 대해 더 알아보기 [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?WT.mc_id=aiml-138114-kinfeylo)

## **Fine-tuning 사용법**

Fine-tuning에서 주로 사용하는 알고리즘은 Lora와 QLora입니다. 어떻게 선택할까요?
- [이 샘플 노트북에서 자세히 알아보기](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python FineTuning 샘플 예제](../../../../code/04.Finetuning/FineTrainingScript.py)

### **Lora와 QLora**

![lora](../../../../translated_images/ko/qlora.e6446c988ee04ca0.png)

LoRA(Low-Rank Adaptation)와 QLoRA(Quantized Low-Rank Adaptation)는 모두 Parameter Efficient Fine Tuning(PEFT)을 사용해 대형 언어 모델(LLM)을 미세 조정하는 기술입니다. PEFT는 전통적인 방법보다 더 효율적으로 모델을 학습시키도록 설계되었습니다.  
LoRA는 가중치 업데이트 행렬에 저랭크 근사를 적용해 메모리 사용량을 줄이는 독립적인 미세 조정 기법입니다. 빠른 학습 속도를 제공하며 전통적인 미세 조정 방법과 거의 비슷한 성능을 유지합니다.

QLoRA는 LoRA를 확장한 버전으로, 양자화 기법을 도입해 메모리 사용량을 더욱 줄입니다. QLoRA는 사전 학습된 LLM의 가중치 파라미터를 4비트 정밀도로 양자화하여 LoRA보다 메모리 효율적입니다. 다만, 추가적인 양자화 및 역양자화 과정 때문에 QLoRA 학습은 LoRA보다 약 30% 느립니다.

QLoRA는 양자화 과정에서 발생하는 오류를 보정하기 위해 LoRA를 보조적으로 사용합니다. QLoRA는 수십억 개의 파라미터를 가진 대형 모델도 상대적으로 적은 수의 GPU에서 미세 조정할 수 있게 해줍니다. 예를 들어, QLoRA는 36개의 GPU가 필요한 70B 파라미터 모델을 단 2개의 GPU로도 미세 조정할 수 있습니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.