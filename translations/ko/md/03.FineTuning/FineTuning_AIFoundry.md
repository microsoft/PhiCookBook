# Microsoft Foundry를 사용한 Phi-3 미세 조정

Microsoft Foundry를 사용하여 Microsoft의 Phi-3 Mini 언어 모델을 미세 조정하는 방법을 살펴보겠습니다. 미세 조정은 Phi-3 Mini를 특정 작업에 맞게 조정하여 더욱 강력하고 문맥을 잘 이해하는 모델로 만드는 것을 가능하게 합니다.

## 고려사항

- **기능:** 어떤 모델들이 미세 조정 가능한가요? 기본 모델을 미세 조정하여 무엇을 할 수 있나요?
- **비용:** 미세 조정의 가격 모델은 어떻게 되나요?
- **사용자 정의 가능성:** 기본 모델을 얼마만큼, 어떤 방식으로 수정할 수 있나요?
- **편의성:** 미세 조정은 실제로 어떻게 이루어지나요? 사용자 지정 코드를 작성해야 하나요? 직접 컴퓨팅 자원을 가져와야 하나요?
- **안전성:** 미세 조정된 모델은 안전성 위험이 알려져 있는데, 의도치 않은 피해를 방지할 수 있는 가드레일이 있나요?

![AIFoundry Models](../../../../translated_images/ko/AIFoundryModels.0e1b16f7d0b09b73.webp)

## 미세 조정을 위한 준비

### 사전 요구사항

> [!NOTE]
> Phi-3 계열 모델의 경우, 종량제(pay-as-you-go) 방식의 미세 조정 서비스는 **East US 2** 지역에 생성된 허브에서만 사용할 수 있습니다.

- Azure 구독. Azure 구독이 없으면, [유료 Azure 계정](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go)을 생성하여 시작하세요.

- [AI Foundry 프로젝트](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Microsoft Foundry에서의 작업 권한 부여는 Azure 역할 기반 액세스 제어(Azure RBAC)를 사용합니다. 이 글의 단계를 수행하려면, 사용자 계정에 리소스 그룹에 대한 __Azure AI Developer 역할__이 할당되어 있어야 합니다.

### 구독 공급자 등록

`Microsoft.Network` 리소스 공급자가 구독에 등록되어 있는지 확인하세요.

1. [Azure 포털](https://portal.azure.com)에 로그인합니다.
1. 왼쪽 메뉴에서 <strong>구독</strong>을 선택합니다.
1. 사용하려는 구독을 선택합니다.
1. 왼쪽 메뉴에서 **AI 프로젝트 설정** > <strong>리소스 공급자</strong>를 선택합니다.
1. 목록에 <strong>Microsoft.Network</strong>가 있는지 확인합니다. 없으면 추가하세요.

### 데이터 준비

모델을 미세 조정하기 위한 훈련 및 검증 데이터를 준비하세요. 훈련 데이터와 검증 데이터 세트는 모델이 수행하길 원하는 작업 방식에 대한 입력과 출력 예제로 구성됩니다.

모든 훈련 샘플이 추론을 위한 예상 형식인지 확인하세요. 모델을 효과적으로 미세 조정하려면 균형 잡히고 다양성이 확보된 데이터셋이 필요합니다.

이는 데이터 균형 유지, 다양한 시나리오 포함, 주기적인 훈련 데이터 개선을 포함하며, 궁극적으로 현실에 부합하는 보다 정확하고 균형 잡힌 모델 응답으로 이어집니다.

서로 다른 모델 유형에 따라 요구되는 훈련 데이터 형식도 다릅니다.

### 채팅 완성

사용하는 훈련 및 검증 데이터는 <strong>반드시</strong> JSON Lines (JSONL) 형식이어야 합니다. `Phi-3-mini-128k-instruct`의 경우, 미세 조정 데이터셋은 Chat completions API에서 사용하는 대화 형식을 따라야 합니다.

### 예제 파일 형식

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

지원되는 파일 유형은 JSON Lines입니다. 파일은 기본 데이터 저장소에 업로드되어 프로젝트에서 사용할 수 있습니다.

## Microsoft Foundry를 사용한 Phi-3 미세 조정

Microsoft Foundry는 미세 조정이라는 과정을 통해 대형 언어 모델을 개인 데이터 세트에 맞춤화할 수 있게 해줍니다. 미세 조정은 특정 작업과 응용 분야에 맞게 사용자 정의와 최적화를 가능하게 하여 큰 가치를 제공합니다. 이를 통해 성능 향상, 비용 효율성, 지연 시간 감소, 맞춤형 출력이 이루어집니다.

![Finetune AI Foundry](../../../../translated_images/ko/AIFoundryfinetune.193aaddce48d553c.webp)

### 새 프로젝트 생성

1. [Microsoft Foundry](https://ai.azure.com)에 로그인합니다.

1. Microsoft Foundry에서 <strong>+New project</strong>를 선택하여 새 프로젝트를 만듭니다.

    ![FineTuneSelect](../../../../translated_images/ko/select-new-project.cd31c0404088d7a3.webp)

1. 다음 작업을 수행합니다:

    - 프로젝트 **Hub 이름** 입력. 고유한 값이어야 합니다.
    - 사용할 **Hub** 선택(필요 시 새로 생성).

    ![FineTuneSelect](../../../../translated_images/ko/create-project.ca3b71298b90e420.webp)

1. 새 허브를 생성하려면 다음 작업을 수행합니다:

    - **Hub 이름** 입력(고유해야 함).
    - Azure <strong>구독</strong> 선택.
    - 사용할 **리소스 그룹** 선택(필요 시 새로 생성).
    - 사용할 <strong>지역</strong> 선택.
    - 사용할 **Connect Azure AI Services** 선택(필요 시 새로 생성).
    - <strong>Connect Azure AI Search</strong>는 **연결 건너뛰기** 선택.

    ![FineTuneSelect](../../../../translated_images/ko/create-hub.49e53d235e80779e.webp)

1. **Next** 선택
1. **Create a project** 선택

### 데이터 준비

미세 조정에 앞서, 채팅 지침, 질문-응답 쌍 등 작업과 관련된 데이터셋을 수집하거나 만드세요. 데이터에서 노이즈를 제거하고, 누락값을 처리하며, 텍스트 토큰화를 수행해 정제하고 전처리하세요.

### Microsoft Foundry에서 Phi-3 모델 미세 조정

> [!NOTE]
> Phi-3 모델 미세 조정은 현재 East US 2 지역에 위치한 프로젝트에서 지원됩니다.

1. 좌측 탭에서 **Model catalog** 선택

1. <strong>검색창</strong>에 *phi-3* 입력 후 사용하려는 phi-3 모델 선택

    ![FineTuneSelect](../../../../translated_images/ko/select-model.60ef2d4a6a3cec57.webp)

1. **Fine-tune** 선택

    ![FineTuneSelect](../../../../translated_images/ko/select-finetune.a976213b543dd9d8.webp)

1. **Fine-tuned 모델 이름** 입력

    ![FineTuneSelect](../../../../translated_images/ko/finetune1.c2b39463f0d34148.webp)

1. **Next** 선택

1. 다음 작업 수행:

    - 작업 유형 <strong>task type</strong>을 <strong>Chat completion</strong>으로 선택
    - 사용할 **Training data** 선택. Microsoft Foundry 데이터 또는 로컬에서 업로드 가능.

    ![FineTuneSelect](../../../../translated_images/ko/finetune2.43cb099b1a94442d.webp)

1. **Next** 선택

1. 사용할 **Validation data** 업로드 또는 **훈련 데이터 자동 분할(Automatic split of training data)** 선택

    ![FineTuneSelect](../../../../translated_images/ko/finetune3.fd96121b67dcdd92.webp)

1. **Next** 선택

1. 다음 작업 수행:

    - 사용할 **Batch size multiplier** 선택
    - 사용할 **Learning rate** 선택
    - 사용할 **Epochs** 선택

    ![FineTuneSelect](../../../../translated_images/ko/finetune4.e18b80ffccb5834a.webp)

1. **Submit** 선택하여 미세 조정 프로세스 시작

    ![FineTuneSelect](../../../../translated_images/ko/select-submit.0a3802d581bac271.webp)

1. 모델 미세 조정이 완료되면 상태가 <strong>Completed</strong>로 표시됩니다. 이제 모델을 배포하여 자체 애플리케이션, 플레이그라운드, 또는 프롬프트 플로우에서 사용할 수 있습니다. 자세한 내용은 [Microsoft Foundry를 사용한 Phi-3 계열 소형 언어 모델 배포 방법](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python)를 참조하세요.

    ![FineTuneSelect](../../../../translated_images/ko/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Phi-3 미세 조정에 대한 자세한 내용은 [Microsoft Foundry에서 Phi-3 모델 미세 조정](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini)을 참조하세요.

## 미세 조정 모델 정리

[Microsoft Foundry](https://ai.azure.com)에서 미세 조정 모델 목록 또는 모델 상세 페이지에서 미세 조정된 모델을 삭제할 수 있습니다. 미세 조정 페이지에서 삭제할 모델을 선택한 후, 삭제 버튼을 눌러 모델을 제거하세요.

> [!NOTE]
> 기존에 배포된 디플로이가 있는 경우 사용자 지정 모델을 삭제할 수 없습니다. 사용자 지정 모델 삭제 전에 먼저 모델 배포를 삭제해야 합니다.

## 비용 및 할당량

### 서비스를 통한 Phi-3 모델 미세 조정의 비용 및 할당량 고려사항

Phi 모델은 Microsoft가 제공하는 서비스 형태로, Microsoft Foundry와 통합되어 사용됩니다. 모델을 [배포](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python)하거나 미세 조정할 때는 배포 마법사의 가격 및 조건 탭에서 요금을 확인할 수 있습니다.

## 콘텐츠 필터링

종량제 방식으로 서비스에 배포된 모델은 Azure AI Content Safety의 보호를 받습니다. 실시간 엔드포인트에 배포 시 이 기능을 선택적으로 해제할 수 있습니다. Azure AI Content Safety가 활성화된 경우, 프롬프트와 출력이 모두 유해 콘텐츠 출력을 탐지하고 방지하기 위한 복합 분류 모델 집합을 통과합니다. 콘텐츠 필터링 시스템은 입력 프롬프트와 출력 결과 모두에서 잠재적 유해 콘텐츠의 특정 범주를 감지하여 조치를 취합니다. 자세한 내용은 [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering)를 참조하세요.

**미세 조정 구성**

학습률, 배치 크기, 에포크 수 등 하이퍼파라미터 정의

**손실 함수**

과제에 적합한 손실 함수 선택(예: 교차 엔트로피)

<strong>옵티마이저</strong>

훈련 시 그래디언트 갱신에 사용할 옵티마이저 선택(예: Adam)

**미세 조정 프로세스**

- 사전 학습된 모델 로드: Phi-3 Mini 체크포인트 로드
- 맞춤형 레이어 추가: 작업별 레이어 추가(예: 채팅 지침용 분류 헤드)

**모델 훈련**

준비한 데이터셋으로 모델 미세 조정. 훈련 진행을 모니터링하며 하이퍼파라미터 조정

**평가 및 검증**

검증 세트: 데이터를 훈련과 검증 세트로 분할

**성능 평가**

정확도, F1-스코어, 퍼플렉서티 등 지표 사용

## 미세 조정 모델 저장

<strong>체크포인트</strong>

미래 사용을 위한 미세 조정 모델 체크포인트 저장

## 배포

- 웹 서비스로 배포: Microsoft Foundry에서 미세 조정 모델 웹 서비스로 배포
- 엔드포인트 테스트: 배포된 엔드포인트에 테스트 쿼리를 보내 기능 검증

## 반복 및 개선

성능이 만족스럽지 않으면 하이퍼파라미터 조정, 더 많은 데이터 추가, 추가 에포크 미세 조정 등을 통해 반복 개선

## 모니터링 및 정제

모델 동작을 지속 모니터링하고 필요시 정제

## 사용자 정의 및 확장

사용자 지정 작업: Phi-3 Mini는 채팅 지침 이외에도 다양한 작업에 미세 조정 가능. 다른 활용 사례 탐색
실험: 다양한 아키텍처, 레이어 조합, 기법을 시험하여 성능 향상

> [!NOTE]
> 미세 조정은 반복적인 과정입니다. 실험하고, 배우고, 모델을 적응시켜 특정 작업에 최적의 결과를 얻으세요!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역은 오류나 부정확성을 포함할 수 있음을 유의해 주시기 바랍니다. 원본 문서는 해당 언어의 원문이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 당사가 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->