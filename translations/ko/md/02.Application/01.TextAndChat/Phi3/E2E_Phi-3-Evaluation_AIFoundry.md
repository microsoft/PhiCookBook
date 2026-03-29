# Microsoft의 책임 있는 AI 원칙에 중점을 두고 Microsoft Foundry에서 미세 조정된 Phi-3 / Phi-3.5 모델 평가하기

이 종합 샘플은 Microsoft Tech Community의 "[Microsoft의 책임 있는 AI에 중점을 둔 Microsoft Foundry에서 미세 조정된 Phi-3 / 3.5 모델 평가하기](https://techcommunity.microsoft.com/blog/educatordeveloperblog/evaluate-fine-tuned-phi-3--3-5-models-in-azure-ai-studio-focusing-on-microsofts-/4227850?WT.mc_id=aiml-137032-kinfeylo)" 가이드를 기반으로 합니다.

## 개요

### Microsoft Foundry에서 미세 조정된 Phi-3 / Phi-3.5 모델의 안전성과 성능은 어떻게 평가할 수 있나요?

모델을 미세 조정하면 때때로 의도치 않거나 원하지 않는 응답이 나올 수 있습니다. 모델이 안전하고 효과적으로 작동하도록 하려면 모델이 유해한 콘텐츠를 생성할 가능성과 정확하고 관련성 있으며 일관된 응답을 생성하는 능력을 평가하는 것이 중요합니다. 이 자습서에서는 Microsoft Foundry에 Prompt flow와 통합된 미세 조정된 Phi-3 / Phi-3.5 모델의 안전성과 성능을 평가하는 방법을 배웁니다.

다음은 Microsoft Foundry의 평가 프로세스입니다.

![Architecture of tutorial.](../../../../../../translated_images/ko/architecture.10bec55250f5d6a4.webp)

*이미지 출처: [생성 AI 애플리케이션 평가](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5에 대한 자세한 정보와 추가 리소스를 탐색하려면 [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)을 방문하세요.

### 사전 준비 사항

- [Python](https://www.python.org/downloads)
- [Azure 구독](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- 미세 조정된 Phi-3 / Phi-3.5 모델

### 목차

1. [**시나리오 1: Microsoft Foundry의 Prompt flow 평가 소개**](#scenario-1-introduction-to-azure-ai-studios-prompt-flow-evaluation)

    - [안전성 평가 소개](#안전성-평가-소개)
    - [성능 평가 소개](#성능-평가-소개)

1. [**시나리오 2: Microsoft Foundry에서 Phi-3 / Phi-3.5 모델 평가하기**](#scenario-2-evaluating-the-phi-3--phi-35-model-in-azure-ai-studio)

    - [시작하기 전에](#시작하기-전에)
    - [Phi-3 / Phi-3.5 모델 평가를 위한 Azure OpenAI 배포](#deploy-azure-openai-to-evaluate-the-phi-3--phi-35-model)
    - [Microsoft Foundry의 Prompt flow 평가를 사용하여 미세 조정된 Phi-3 / Phi-3.5 모델 평가하기](#evaluate-the-fine-tuned-phi-3--phi-35-model-using-azure-ai-studios-prompt-flow-evaluation)

1. [축하합니다!](#축하합니다)

## **시나리오 1: Microsoft Foundry의 Prompt flow 평가 소개**

### 안전성 평가 소개

AI 모델이 윤리적이고 안전하다는 것을 보장하기 위해서는 Microsoft의 책임 있는 AI 원칙에 따라 평가하는 것이 중요합니다. Microsoft Foundry에서는 안전성 평가를 통해 모델이 잠금 해제 공격에 얼마나 취약한지와 유해한 콘텐츠를 생성할 가능성을 평가할 수 있으며, 이는 이러한 원칙들과 직접적으로 일치합니다.

![Safaty evaluation.](../../../../../../translated_images/ko/safety-evaluation.083586ec88dfa950.webp)

*이미지 출처: [생성 AI 애플리케이션 평가](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft의 책임 있는 AI 원칙

기술적 절차를 시작하기 전에, Microsoft의 책임 있는 AI 원칙을 이해하는 것이 필수적입니다. 이는 AI 시스템의 책임 있는 개발, 배포 및 운영을 안내하는 윤리적 프레임워크입니다. 이 원칙들은 AI 시스템이 공정하고 투명하며 포괄적으로 구축되도록 지침을 제공하며, AI 모델 안전성 평가의 토대가 됩니다.

Microsoft의 책임 있는 AI 원칙은 다음과 같습니다:

- **공정성과 포용성**: AI 시스템은 모두에게 공평하게 대우하며, 동일한 상황에 놓인 집단을 다르게 대우하지 않아야 합니다. 예를 들어 의료 처방, 대출 신청, 고용 안내를 제공할 때, AI 시스템은 유사한 증상, 재정 상태 또는 직업 자격을 가진 모든 사람에게 동일한 권고를 해야 합니다.

- **신뢰성 및 안전성**: 신뢰를 구축하려면 AI 시스템이 안정적이고 안전하며 일관되게 작동해야 합니다. 이 시스템은 원래 설계대로 작동하고, 예기치 않은 조건에 안전하게 대응하며, 유해한 조작을 견뎌야 합니다. 작동 방식과 처리할 수 있는 다양한 조건은 설계 및 테스트 중 개발자가 예상한 상황과 환경을 반영합니다.

- <strong>투명성</strong>: AI 시스템이 사람의 삶에 큰 영향을 미치는 결정을 도울 때, 결정이 어떻게 내려졌는지 사람들이 이해하는 것이 중요합니다. 예를 들어 은행은 AI 시스템으로 신용 적합성을 결정할 수 있고, 회사는 AI로 가장 적합한 채용 후보를 선택할 수 있습니다.

- **프라이버시 및 보안**: AI가 널리 퍼짐에 따라 프라이버시 보호와 개인정보 및 기업 정보 보안은 더욱 중요하고 복잡해지고 있습니다. AI는 데이터 접근이 예측과 결정을 정확하고 정보에 기반해 내리는 데 필수적이기 때문에 프라이버시와 보안에 세심한 주의가 필요합니다.

- <strong>책임성</strong>: AI 시스템을 설계하고 배포하는 사람들은 시스템 작동 방식에 대해 책임을 져야 합니다. 조직은 업계 표준을 참고해 책임성 규범을 개발해야 합니다. 이는 AI 시스템이 사람의 삶에 영향을 미치는 결정의 최종 권한자가 되지 않도록 하고, 인간이 고도로 자율적인 AI 시스템을 의미 있게 통제할 수 있도록 합니다.

![Fill hub.](../../../../../../translated_images/ko/responsibleai2.c07ef430113fad8c.webp)

*이미지 출처: [책임 있는 AI란?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoft의 책임 있는 AI 원칙에 대해 더 알아보려면 [책임 있는 AI란?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)을 방문하세요.

#### 안전성 지표

이 자습서에서는 Microsoft Foundry의 안전성 지표를 활용하여 미세 조정된 Phi-3 모델의 안전성을 평가합니다. 이 지표들은 모델이 유해한 콘텐츠를 생성할 가능성과 잠금 해제 공격에 대한 취약성을 평가하는 데 도움을 줍니다. 안전성 지표는 다음과 같습니다:

- **자해 관련 콘텐츠**: 모델이 자해 관련 콘텐츠를 생성하는 경향이 있는지 평가합니다.
- **혐오 및 불공정 콘텐츠**: 모델이 혐오성 또는 불공정한 콘텐츠를 생성하는 경향이 있는지 평가합니다.
- **폭력적 콘텐츠**: 모델이 폭력적 콘텐츠를 생성하는 경향이 있는지 평가합니다.
- **성적 콘텐츠**: 모델이 부적절한 성적 콘텐츠를 생성하는 경향이 있는지 평가합니다.

이러한 측면들을 평가함으로써 AI 모델이 유해하거나 모욕적인 콘텐츠를 생성하지 않도록 하여 사회적 가치 및 규제 기준과 일치시키게 됩니다.

![Evaluate based on safety.](../../../../../../translated_images/ko/evaluate-based-on-safety.c5df819f5b0bfc07.webp)

### 성능 평가 소개

AI 모델이 기대한 대로 작동하는지 확인하기 위해 성능 지표에 기반해 평가하는 것이 중요합니다. Microsoft Foundry에서 성능 평가는 모델이 정확하고 관련성 있으며 일관된 응답을 생성하는 효과성을 평가할 수 있게 해줍니다.

![Safaty evaluation.](../../../../../../translated_images/ko/performance-evaluation.48b3e7e01a098740.webp)

*이미지 출처: [생성 AI 애플리케이션 평가](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### 성능 지표

이 자습서에서는 Microsoft Foundry의 성능 지표를 사용하여 미세 조정된 Phi-3 / Phi-3.5 모델의 성능을 평가합니다. 이 지표들은 모델이 정확하고 관련성 있으며 일관된 응답을 생성하는 효과성을 평가하는 데 도움을 줍니다. 성능 지표는 다음과 같습니다:

- **근거성 (Groundedness)**: 생성된 답변이 입력 소스 정보와 얼마나 잘 일치하는지 평가합니다.
- **관련성 (Relevance)**: 생성한 응답이 주어진 질문과 얼마나 관련이 있는지 평가합니다.
- **일관성 (Coherence)**: 생성된 텍스트가 얼마나 자연스럽게 흐르고, 읽기 쉽고, 인간과 같은 언어인지 평가합니다.
- **유창성 (Fluency)**: 생성된 텍스트의 언어 능력을 평가합니다.
- **GPT 유사도 (GPT Similarity)**: 생성된 응답과 기준 응답을 비교하여 유사성을 평가합니다.
- **F1 점수 (F1 Score)**: 생성된 응답과 원본 데이터 간에 공유된 단어 비율을 계산합니다.

이 지표들은 모델이 정확하고 관련성 있으며 일관된 응답을 생성하는 효과성을 평가하는 데 도움을 줍니다.

![Evaluate based on performance.](../../../../../../translated_images/ko/evaluate-based-on-performance.3e801c647c7554e8.webp)

## **시나리오 2: Microsoft Foundry에서 Phi-3 / Phi-3.5 모델 평가하기**

### 시작하기 전에

이 자습서는 앞선 블로그 게시물 "[Prompt Flow와 함께 커스텀 Phi-3 모델 미세 조정 및 통합: 단계별 가이드](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" 및 "[Microsoft Foundry에서 Prompt Flow와 함께 커스텀 Phi-3 모델 미세 조정 및 통합](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)"을 연계한 내용입니다. 이 게시물들에서는 Microsoft Foundry에서 Phi-3 / Phi-3.5 모델을 미세 조정하고 Prompt flow와 통합하는 과정을 안내합니다.

이 자습서에서는 Microsoft Foundry에서 평가자로 Azure OpenAI 모델을 배포하고 이를 사용하여 미세 조정된 Phi-3 / Phi-3.5 모델을 평가합니다.

이 자습서를 시작하기 전에, 이전 자습서에서 설명한 다음 사항들을 준비했는지 확인하세요:

1. 미세 조정된 Phi-3 / Phi-3.5 모델을 평가할 데이터셋 준비.
1. 미세 조정 및 Azure Machine Learning에 배포된 Phi-3 / Phi-3.5 모델.
1. Microsoft Foundry에서 미세 조정된 Phi-3 / Phi-3.5 모델과 통합된 Prompt flow.

> [!NOTE]
> 이전 블로그 게시물에서 다운로드한 **ULTRACHAT_200k** 데이터셋의 data 폴더에 있는 *test_data.jsonl* 파일을 미세 조정된 Phi-3 / Phi-3.5 모델을 평가할 데이터셋으로 사용할 예정입니다.

#### Microsoft Foundry에서 Prompt flow와 커스텀 Phi-3 / Phi-3.5 모델 통합하기 (코드 우선 접근)

> [!NOTE]
> "[Microsoft Foundry에서 Prompt Flow와 함께 커스텀 Phi-3 모델 미세 조정 및 통합](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)"에 설명된 로우코드 접근법을 따랐다면 이 연습을 건너뛰고 다음 단계로 넘어가도 됩니다.
> 그러나 "[Prompt Flow와 함께 커스텀 Phi-3 모델 미세 조정 및 통합: 단계별 가이드](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)"에 설명된 코드 우선 접근법을 따라 Phi-3 / Phi-3.5 모델을 미세 조정 및 배포했다면, 모델을 Prompt flow에 연결하는 과정이 약간 다릅니다. 이 연습에서 그 과정을 배우게 됩니다.

계속 진행하려면 Microsoft Foundry에서 미세 조정된 Phi-3 / Phi-3.5 모델을 Prompt flow에 통합해야 합니다.

#### Microsoft Foundry Hub 만들기

프로젝트를 생성하기 전에 Hub를 생성해야 합니다. Hub는 리소스 그룹과 같이 작동하며, Microsoft Foundry 내 여러 프로젝트를 조직하고 관리할 수 있게 해줍니다.
1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)에 로그인합니다.

1. 왼쪽 탭에서 <strong>All hubs</strong>를 선택합니다.

1. 탐색 메뉴에서 <strong>+ New hub</strong>를 선택합니다.

    ![Create hub.](../../../../../../translated_images/ko/create-hub.5be78fb1e21ffbf1.webp)

1. 다음 작업을 수행합니다:

    - <strong>Hub name</strong>을 입력합니다. 고유한 값이어야 합니다.
    - Azure <strong>Subscription</strong>을 선택합니다.
    - 사용할 <strong>Resource group</strong>을 선택합니다(필요한 경우 새로 만듭니다).
    - 사용할 <strong>Location</strong>을 선택합니다.
    - 사용할 <strong>Connect Azure AI Services</strong>를 선택합니다(필요한 경우 새로 만듭니다).
    - <strong>Connect Azure AI Search</strong>에서 <strong>Skip connecting</strong>을 선택합니다.

    ![Fill hub.](../../../../../../translated_images/ko/fill-hub.baaa108495c71e34.webp)

1. <strong>Next</strong>를 선택합니다.

#### Microsoft Foundry 프로젝트 생성

1. 생성한 Hub에서 왼쪽 탭의 <strong>All projects</strong>를 선택합니다.

1. 탐색 메뉴에서 <strong>+ New project</strong>를 선택합니다.

    ![Select new project.](../../../../../../translated_images/ko/select-new-project.cd31c0404088d7a3.webp)

1. <strong>Project name</strong>을 입력합니다. 고유한 값이어야 합니다.

    ![Create project.](../../../../../../translated_images/ko/create-project.ca3b71298b90e420.webp)

1. <strong>Create a project</strong>를 선택합니다.

#### 맞춤 조정된 Phi-3 / Phi-3.5 모델을 위한 사용자 지정 연결 추가

맞춤 조정된 Phi-3 / Phi-3.5 모델을 Prompt flow와 통합하려면 모델의 엔드포인트 및 키를 사용자 지정 연결에 저장해야 합니다. 이 설정으로 Prompt flow에서 맞춤 Phi-3 / Phi-3.5 모델에 접근할 수 있습니다.

#### 맞춤 조정된 Phi-3 / Phi-3.5 모델의 API 키 및 엔드포인트 URI 설정

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)를 방문합니다.

1. 생성한 Azure Machine learning 워크스페이스로 이동합니다.

1. 왼쪽 탭에서 <strong>Endpoints</strong>를 선택합니다.

    ![Select endpoints.](../../../../../../translated_images/ko/select-endpoints.ee7387ecd68bd18d.webp)

1. 생성한 엔드포인트를 선택합니다.

    ![Select endpoints.](../../../../../../translated_images/ko/select-endpoint-created.9f63af5e4cf98b2e.webp)

1. 탐색 메뉴에서 <strong>Consume</strong>를 선택합니다.

1. <strong>REST endpoint</strong>와 <strong>Primary key</strong>를 복사합니다.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/ko/copy-endpoint-key.0650c3786bd646ab.webp)

#### 사용자 지정 연결 추가

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)를 방문합니다.

1. 생성한 Microsoft Foundry 프로젝트로 이동합니다.

1. 생성한 프로젝트에서 왼쪽 탭의 <strong>Settings</strong>를 선택합니다.

1. <strong>+ New connection</strong>을 선택합니다.

    ![Select new connection.](../../../../../../translated_images/ko/select-new-connection.fa0f35743758a74b.webp)

1. 탐색 메뉴에서 <strong>Custom keys</strong>를 선택합니다.

    ![Select custom keys.](../../../../../../translated_images/ko/select-custom-keys.5a3c6b25580a9b67.webp)

1. 다음 작업을 수행합니다:

    - <strong>+ Add key value pairs</strong>를 선택합니다.
    - 키 이름에는 <strong>endpoint</strong>를 입력하고, Azure ML Studio에서 복사한 엔드포인트를 값 필드에 붙여넣습니다.
    - 다시 <strong>+ Add key value pairs</strong>를 선택합니다.
    - 키 이름에는 <strong>key</strong>를 입력하고, Azure ML Studio에서 복사한 키를 값 필드에 붙여넣습니다.
    - 키를 추가한 후, 키가 노출되지 않도록 <strong>is secret</strong>를 선택합니다.

    ![Add connection.](../../../../../../translated_images/ko/add-connection.ac7f5faf8b10b0df.webp)

1. <strong>Add connection</strong>을 선택합니다.

#### Prompt flow 생성

Microsoft Foundry에 맞춤 연결을 추가했습니다. 이제 다음 단계를 통해 Prompt flow를 생성합니다. 그런 다음 이 Prompt flow를 맞춤 연결과 연결하여 맞춤 조정된 모델을 Prompt flow 내에서 사용할 수 있습니다.

1. 생성한 Microsoft Foundry 프로젝트로 이동합니다.

1. 왼쪽 탭에서 <strong>Prompt flow</strong>를 선택합니다.

1. 탐색 메뉴에서 <strong>+ Create</strong>를 선택합니다.

    ![Select Promptflow.](../../../../../../translated_images/ko/select-promptflow.18ff2e61ab9173eb.webp)

1. 탐색 메뉴에서 <strong>Chat flow</strong>를 선택합니다.

    ![Select chat flow.](../../../../../../translated_images/ko/select-flow-type.28375125ec9996d3.webp)

1. 사용할 <strong>Folder name</strong>을 입력합니다.

    ![Select chat flow.](../../../../../../translated_images/ko/enter-name.02ddf8fb840ad430.webp)

1. <strong>Create</strong>를 선택합니다.

#### 맞춤 조정된 Phi-3 / Phi-3.5 모델과 채팅하도록 Prompt flow 설정

맞춤 조정된 Phi-3 / Phi-3.5 모델을 Prompt flow에 통합해야 합니다. 그러나 제공된 기존 Prompt flow는 이 목적에 부합하지 않으므로, 맞춤 모델 통합을 위해 Prompt flow를 재설계해야 합니다.

1. Prompt flow에서 기존 흐름을 재구성하기 위해 다음 작업을 수행합니다:

    - <strong>Raw file mode</strong>를 선택합니다.
    - *flow.dag.yml* 파일 안의 모든 기존 코드를 삭제합니다.
    - <em>flow.dag.yml</em>에 다음 코드를 추가합니다.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - <strong>Save</strong>를 선택합니다.

    ![Select raw file mode.](../../../../../../translated_images/ko/select-raw-file-mode.06c1eca581ce4f53.webp)

1. Prompt flow에서 맞춤 Phi-3 / Phi-3.5 모델을 사용하려면 <em>integrate_with_promptflow.py</em>에 다음 코드를 추가합니다.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # 로깅 설정
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection"은 사용자 정의 연결 이름이고, "endpoint"와 "key"는 사용자 정의 연결의 키입니다
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # 전체 JSON 응답을 기록합니다
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/ko/paste-promptflow-code.cd6d95b101c0ec28.webp)

> [!NOTE]
> Microsoft Foundry에서 Prompt flow 사용에 대한 자세한 내용은 [Microsoft Foundry에서의 Prompt flow](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)를 참조하세요.

1. **Chat input**, <strong>Chat output</strong>을 선택하여 모델과 채팅할 수 있도록 설정합니다.

    ![Select Input Output.](../../../../../../translated_images/ko/select-input-output.c187fc58f25fbfc3.webp)

1. 이제 맞춤 조정된 Phi-3 / Phi-3.5 모델과 채팅할 준비가 되었습니다. 다음 연습에서는 Prompt flow를 시작하고 이를 통해 맞춤 조정된 Phi-3 / Phi-3.5 모델과 채팅하는 방법을 배웁니다.

> [!NOTE]
>
> 재구성된 흐름은 아래 이미지와 같아야 합니다:
>
> ![Flow example](../../../../../../translated_images/ko/graph-example.82fd1bcdd3fc545b.webp)
>

#### Prompt flow 시작

1. <strong>Start compute sessions</strong>를 선택하여 Prompt flow를 시작합니다.

    ![Start compute session.](../../../../../../translated_images/ko/start-compute-session.9acd8cbbd2c43df1.webp)

1. <strong>Validate and parse input</strong>을 선택하여 파라미터를 갱신합니다.

    ![Validate input.](../../../../../../translated_images/ko/validate-input.c1adb9543c6495be.webp)

1. 생성한 사용자 지정 연결의 **connection** 값을 선택합니다. 예를 들어, *connection*.

    ![Connection.](../../../../../../translated_images/ko/select-connection.1f2b59222bcaafef.webp)

#### 맞춤 조정된 Phi-3 / Phi-3.5 모델과 채팅

1. <strong>Chat</strong>을 선택합니다.

    ![Select chat.](../../../../../../translated_images/ko/select-chat.0406bd9687d0c49d.webp)

1. 결과 예시는 다음과 같습니다: 이제 맞춤 조정된 Phi-3 / Phi-3.5 모델과 채팅할 수 있습니다. 미리 학습한 데이터 기반 질문을 권장합니다.

    ![Chat with prompt flow.](../../../../../../translated_images/ko/chat-with-promptflow.1cf8cea112359ada.webp)

### Phi-3 / Phi-3.5 모델 평가를 위한 Azure OpenAI 배포

Microsoft Foundry에서 Phi-3 / Phi-3.5 모델을 평가하려면 Azure OpenAI 모델을 배포해야 합니다. 이 모델은 Phi-3 / Phi-3.5 모델의 성능 평가에 사용됩니다.

#### Azure OpenAI 배포

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)에 로그인합니다.

1. 생성한 Microsoft Foundry 프로젝트로 이동합니다.

    ![Select Project.](../../../../../../translated_images/ko/select-project-created.5221e0e403e2c9d6.webp)

1. 생성한 프로젝트에서 왼쪽 탭의 <strong>Deployments</strong>를 선택합니다.

1. 탐색 메뉴에서 <strong>+ Deploy model</strong>을 선택합니다.

1. <strong>Deploy base model</strong>을 선택합니다.

    ![Select Deployments.](../../../../../../translated_images/ko/deploy-openai-model.95d812346b25834b.webp)

1. 사용할 Azure OpenAI 모델을 선택합니다. 예: **gpt-4o**

    ![Select Azure OpenAI model you'd like to use.](../../../../../../translated_images/ko/select-openai-model.959496d7e311546d.webp)

1. <strong>Confirm</strong>을 선택합니다.

### Microsoft Foundry의 Prompt flow 평가를 통한 맞춤 조정 Phi-3 / Phi-3.5 모델 평가

### 새 평가 시작

1. [Microsoft Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)를 방문합니다.

1. 생성한 Microsoft Foundry 프로젝트로 이동합니다.

    ![Select Project.](../../../../../../translated_images/ko/select-project-created.5221e0e403e2c9d6.webp)

1. 생성한 프로젝트에서 왼쪽 탭의 <strong>Evaluation</strong>을 선택합니다.

1. 탐색 메뉴에서 <strong>+ New evaluation</strong>을 선택합니다.

    ![Select evaluation.](../../../../../../translated_images/ko/select-evaluation.2846ad7aaaca7f4f.webp)

1. **Prompt flow** 평가를 선택합니다.

    ![Select Prompt flow evaluation.](../../../../../../translated_images/ko/promptflow-evaluation.cb9758cc19b4760f.webp)

1. 다음 작업을 수행합니다:

    - 평가 이름을 입력합니다. 고유한 값이어야 합니다.
    - 작업 유형으로 <strong>Question and answer without context</strong>를 선택합니다. 이 튜토리얼에서 사용하는 **UlTRACHAT_200k** 데이터셋은 문맥을 포함하지 않기 때문입니다.
    - 평가할 Prompt flow를 선택합니다.

    ![Prompt flow evaluation.](../../../../../../translated_images/ko/evaluation-setting1.4aa08259ff7a536e.webp)

1. <strong>Next</strong>를 선택합니다.

1. 다음 작업을 수행합니다:

    - <strong>Add your dataset</strong>를 선택하여 데이터셋을 업로드합니다. 예를 들어, **ULTRACHAT_200k** 데이터셋을 다운로드하면 포함된 *test_data.json1* 같은 테스트 데이터셋 파일을 업로드할 수 있습니다.
    - 데이터셋에 맞는 <strong>Dataset column</strong>을 선택합니다. 예를 들어, **ULTRACHAT_200k** 데이터셋을 사용하는 경우 <strong>${data.prompt}</strong>를 선택합니다.

    ![Prompt flow evaluation.](../../../../../../translated_images/ko/evaluation-setting2.07036831ba58d64e.webp)

1. <strong>Next</strong>를 선택합니다.

1. 성능 및 품질 메트릭 구성을 위해 다음 작업을 수행합니다:

    - 사용할 성능 및 품질 메트릭을 선택합니다.
    - 평가를 위해 생성한 Azure OpenAI 모델을 선택합니다. 예: **gpt-4o**

    ![Prompt flow evaluation.](../../../../../../translated_images/ko/evaluation-setting3-1.d1ae69e3bf80914e.webp)

1. 위험 및 안전성 메트릭 구성을 위해 다음 작업을 수행합니다:

    - 사용할 위험 및 안전성 메트릭을 선택합니다.
    - 결함률 계산에 사용할 임계값을 선택합니다. 예: **Medium**
    - <strong>question</strong>에는 <strong>Data source</strong>를 <strong>{$data.prompt}</strong>로 설정합니다.
    - <strong>answer</strong>에는 <strong>Data source</strong>를 <strong>{$run.outputs.answer}</strong>로 설정합니다.
    - <strong>ground_truth</strong>에는 <strong>Data source</strong>를 <strong>{$data.message}</strong>로 설정합니다.

    ![Prompt flow evaluation.](../../../../../../translated_images/ko/evaluation-setting3-2.d53bd075c60a45a2.webp)

1. <strong>Next</strong>를 선택합니다.

1. 평가를 시작하려면 <strong>Submit</strong>을 선택합니다.

1. 평가는 완료까지 시간이 걸릴 수 있습니다. 진행 상황은 **Evaluation** 탭에서 모니터링할 수 있습니다.

### 평가 결과 검토

> [!NOTE]
> 아래에 제시된 결과는 평가 과정을 설명하기 위한 것입니다. 이 튜토리얼에서는 상대적으로 작은 데이터셋으로 조정된 모델을 사용하였기 때문에 결과가 최적이 아닐 수 있습니다. 실제 결과는 데이터셋의 크기, 품질, 다양성 및 모델의 구체적 구성에 따라 크게 달라질 수 있습니다.

평가가 완료되면 성능 및 안전성 메트릭에 대한 결과를 검토할 수 있습니다.
1. 성능 및 품질 지표:

    - 일관되고 유창하며 관련성 있는 응답을 생성하는 모델의 효과성을 평가합니다.

    ![평가 결과.](../../../../../../translated_images/ko/evaluation-result-gpu.85f48b42dfb74254.webp)

1. 위험 및 안전 지표:

    - 모델의 출력이 안전하며 책임 있는 AI 원칙에 부합하도록 하여 해롭거나 공격적인 콘텐츠를 피합니다.

    ![평가 결과.](../../../../../../translated_images/ko/evaluation-result-gpu-2.1b74e336118f4fd0.webp)

1. 아래로 스크롤하여 <strong>상세 지표 결과</strong>를 확인할 수 있습니다.

    ![평가 결과.](../../../../../../translated_images/ko/detailed-metrics-result.afa2f5c39a4f5f17.webp)

1. 맞춤형 Phi-3 / Phi-3.5 모델을 성능 및 안전 지표와 함께 평가함으로써 모델이 효과적일 뿐만 아니라 책임 있는 AI 관행을 준수하여 실제 배포 준비가 되었음을 확인할 수 있습니다.

## 축하합니다!

### 튜토리얼을 완료하셨습니다

Microsoft Foundry에서 Prompt flow와 통합된 파인튜닝된 Phi-3 모델을 성공적으로 평가했습니다. 이는 AI 모델이 성능뿐 아니라 Microsoft의 책임 있는 AI 원칙을 준수하여 신뢰할 수 있고 안정적인 AI 애플리케이션을 구축하는 데 중요한 단계입니다.

![아키텍처.](../../../../../../translated_images/ko/architecture.10bec55250f5d6a4.webp)

## Azure 리소스 정리

추가 비용 발생을 방지하기 위해 Azure 리소스를 정리하세요. Azure 포털로 이동하여 다음 리소스를 삭제하십시오:

- Azure Machine learning 리소스
- Azure Machine learning 모델 엔드포인트
- Microsoft Foundry 프로젝트 리소스
- Microsoft Foundry Prompt flow 리소스

### 다음 단계

#### 문서

- [책임 있는 AI 대시보드를 사용하여 AI 시스템 평가하기](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [생성형 AI 평가 및 모니터링 지표](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Microsoft Foundry 문서](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow 문서](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### 교육 콘텐츠

- [Microsoft의 책임 있는 AI 접근법 소개](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Microsoft Foundry 소개](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### 참고

- [책임 있는 AI란?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [더 안전하고 신뢰할 수 있는 생성형 AI 애플리케이션 빌드를 돕는 Azure AI의 새로운 도구 발표](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [생성형 AI 애플리케이션 평가](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 양지해 주시기 바랍니다. 원문 문서는 원어로 된 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문 인간 번역을 권장합니다. 본 번역 사용으로 인한 어떠한 오해나 잘못된 해석에 대해서도 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->