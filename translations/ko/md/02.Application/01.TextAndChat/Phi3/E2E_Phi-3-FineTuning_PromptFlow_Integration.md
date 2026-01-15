<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7ca2c30fdb802664070e9cfbf92e24fe",
  "translation_date": "2026-01-05T16:24:14+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "ko"
}
-->
# Prompt flow로 맞춤형 Phi-3 모델 미세 조정 및 통합하기

이 종단 간(E2E) 샘플은 Microsoft Tech Community의 "[Prompt flow로 맞춤형 Phi-3 모델 미세 조정 및 통합하기: 단계별 가이드](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" 가이드를 기반으로 합니다. 맞춤형 Phi-3 모델을 미세 조정하고 배포하며 Prompt flow와 통합하는 과정을 소개합니다.

## 개요

이 E2E 샘플에서는 Phi-3 모델을 미세 조정하고 Prompt flow와 통합하는 방법을 배우게 됩니다. Azure Machine Learning과 Prompt flow를 활용하여 맞춤형 AI 모델을 배포하고 활용하는 워크플로우를 구축합니다. 이 E2E 샘플은 세 가지 시나리오로 나누어져 있습니다:

**시나리오 1: Azure 리소스 설정 및 미세 조정 준비**

**시나리오 2: Phi-3 모델 미세 조정 및 Azure Machine Learning Studio에 배포**

**시나리오 3: Prompt flow와 통합 및 맞춤형 모델과 대화하기**

다음은 이 E2E 샘플의 개요입니다.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/ko/00-01-architecture.02fc569e266d468c.png)

### 목차

1. **[시나리오 1: Azure 리소스 설정 및 미세 조정 준비](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning 작업 영역 만들기](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure 구독에서 GPU 할당량 요청](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [역할 할당 추가](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [프로젝트 설정](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [미세 조정용 데이터셋 준비](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[시나리오 2: Phi-3 모델 미세 조정 및 Azure Machine Learning Studio에 배포](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure CLI 설정](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 모델 미세 조정](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [미세 조정된 모델 배포](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[시나리오 3: Prompt flow와 통합 및 맞춤형 모델과 대화하기](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [맞춤형 Phi-3 모델을 Prompt flow와 통합](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [맞춤형 모델과 대화하기](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## 시나리오 1: Azure 리소스 설정 및 미세 조정 준비

### Azure Machine Learning 작업 영역 만들기

1. 포털 페이지 상단의 **검색창**에 *azure machine learning*을 입력하고 나타나는 옵션에서 **Azure Machine Learning**을 선택합니다.

    ![Type azure machine learning](../../../../../../translated_images/ko/01-01-type-azml.a5116f8454d98c60.png)

1. 탐색 메뉴에서 **+ 만들기**을 선택합니다.

1. 탐색 메뉴에서 **새 작업 영역**을 선택합니다.

    ![Select new workspace](../../../../../../translated_images/ko/01-02-select-new-workspace.83e17436f8898dc4.png)

1. 다음 작업을 수행합니다:

    - Azure **구독**을 선택합니다.
    - 사용할 **리소스 그룹**을 선택합니다 (필요 시 새로 만듭니다).
    - **작업 영역 이름**을 입력합니다. 고유한 값이어야 합니다.
    - 사용할 **지역**을 선택합니다.
    - 사용할 **저장소 계정**을 선택합니다 (필요 시 새로 만듭니다).
    - 사용할 **키 자격증명(Key vault)**을 선택합니다 (필요 시 새로 만듭니다).
    - 사용할 **애플리케이션 인사이트**를 선택합니다 (필요 시 새로 만듭니다).
    - 사용할 **컨테이너 레지스트리**를 선택합니다 (필요 시 새로 만듭니다).

    ![Fill AZML.](../../../../../../translated_images/ko/01-03-fill-AZML.730a5177757bbebb.png)

1. **검토 + 만들기**를 선택합니다.

1. **만들기**를 선택합니다.

### Azure 구독에서 GPU 할당량 요청

이 E2E 샘플에서는 미세 조정에 *Standard_NC24ads_A100_v4 GPU*를 사용하며, 이에는 할당량 요청이 필요합니다. 배포에는 할당량 요청이 필요 없는 *Standard_E4s_v3* CPU를 사용합니다.

> [!NOTE]
>
> GPU 할당은 표준 구독 유형인 Pay-As-You-Go 구독만 가능하며, 혜택 구독은 현재 지원되지 않습니다.
>
> 혜택 구독 (예: Visual Studio Enterprise Subscription)을 사용하거나 미세 조정 및 배포 과정을 빠르게 테스트하려는 경우, 이 튜토리얼에서 CPU를 사용하여 소규모 데이터셋으로 미세 조정하는 방법도 안내합니다. 다만 GPU를 사용하고 대규모 데이터셋을 활용할 때 미세 조정 결과가 훨씬 더 좋다는 점을 유념하세요.

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)에 접속합니다.

1. *Standard NCADSA100v4 Family* 할당량을 요청하기 위해 다음 작업을 수행합니다:

    - 왼쪽 탭에서 **할당량**을 선택합니다.
    - 사용할 **가상 머신 패밀리**를 선택합니다. 예를 들면, *Standard NCADSA100v4 Family Cluster Dedicated vCPUs*로, *Standard_NC24ads_A100_v4* GPU를 포함합니다.
    - 탐색 메뉴에서 **할당량 요청**을 선택합니다.

        ![Request quota.](../../../../../../translated_images/ko/01-04-request-quota.3d3670c3221ab834.png)

    - 할당량 요청 페이지에서 사용할 **새 코어 제한(New cores limit)** 값을 입력합니다. 예: 24
    - 할당량 요청 페이지에서 **제출**을 선택하여 GPU 할당량을 요청합니다.

> [!NOTE]
> 필요에 따라 [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) 문서를 참고해 적절한 GPU 또는 CPU를 선택할 수 있습니다.

### 역할 할당 추가

모델을 미세 조정하고 배포하려면 먼저 사용자 할당 관리 ID(User Assigned Managed Identity, UAI)를 생성하고 적절한 권한 역할을 할당해야 합니다. 이 UAI는 배포 시 인증에 사용됩니다.

#### 사용자 할당 관리 ID(UAI) 생성

1. 포털 페이지 상단의 **검색창**에 *managed identities*를 입력하고 나타나는 옵션에서 **Managed Identities**를 선택합니다.

    ![Type managed identities.](../../../../../../translated_images/ko/01-05-type-managed-identities.9297b6039874eff8.png)

1. **+ 만들기**를 선택합니다.

    ![Select create.](../../../../../../translated_images/ko/01-06-select-create.936d8d66d7144f9a.png)

1. 다음 작업을 수행합니다:

    - Azure **구독**을 선택합니다.
    - 사용할 **리소스 그룹**을 선택합니다 (필요 시 새로 만듭니다).
    - 사용할 **지역**을 선택합니다.
    - **이름**을 입력합니다. 고유해야 합니다.

1. **검토 + 만들기**를 선택합니다.

1. **+ 만들기**를 선택합니다.

#### 관리 ID에 기여자(Contributor) 역할 할당

1. 생성한 관리 ID 리소스로 이동합니다.

1. 왼쪽 탭에서 **Azure 역할 할당**을 선택합니다.

1. 탐색 메뉴에서 **+ 역할 할당 추가**를 선택합니다.

1. 역할 할당 추가 페이지에서 다음 작업을 수행합니다:
    - **범위**를 **리소스 그룹**으로 설정합니다.
    - Azure **구독**을 선택합니다.
    - 사용할 **리소스 그룹**을 선택합니다.
    - 역할을 **기여자(Contributor)**로 설정합니다.

    ![Fill contributor role.](../../../../../../translated_images/ko/01-07-fill-contributor-role.29ca99b7c9f687e0.png)

1. **저장**을 선택합니다.

#### 관리 ID에 Storage Blob Data Reader 역할 할당

1. 포털 페이지 상단의 **검색창**에 *storage accounts*를 입력하고 나타나는 옵션에서 **Storage accounts**를 선택합니다.

    ![Type storage accounts.](../../../../../../translated_images/ko/01-08-type-storage-accounts.1186c8e42933e49b.png)

1. Azure Machine Learning 작업 영역에 연관된 저장소 계정을 선택합니다. 예: *finetunephistorage*

1. 역할 할당 추가 페이지로 이동하기 위해 다음 작업을 수행합니다:

    - 생성한 Azure 저장소 계정으로 이동합니다.
    - 왼쪽 탭에서 **액세스 제어(IAM)**를 선택합니다.
    - 탐색 메뉴에서 **+ 추가**를 선택합니다.
    - **역할 할당 추가**를 선택합니다.

    ![Add role.](../../../../../../translated_images/ko/01-09-add-role.d2db22fec1b187f0.png)

1. 역할 할당 추가 페이지에서 다음 작업을 수행합니다:

    - 역할 페이지의 **검색창**에 *Storage Blob Data Reader*를 입력하고 나타나는 옵션에서 **Storage Blob Data Reader**를 선택합니다.
    - 역할 페이지에서 **다음**을 선택합니다.
    - 사용자 페이지에서 **액세스 권한 부여 대상**을 **Managed identity**로 선택합니다.
    - 사용자 페이지에서 **+ 구성원 선택**을 선택합니다.
    - 관리 ID 선택 페이지에서 Azure **구독**을 선택합니다.
    - 관리 ID 선택 페이지에서 **Managed identity**를 선택합니다.
    - 관리 ID 선택 페이지에서 생성한 관리 ID를 선택합니다. 예: *finetunephi-managedidentity*
    - 관리 ID 선택 페이지에서 **선택**을 클릭합니다.

    ![Select managed identity.](../../../../../../translated_images/ko/01-10-select-managed-identity.5ce5ba181f72a4df.png)

1. **검토 + 할당**을 선택합니다.

#### 관리 ID에 AcrPull 역할 할당

1. 포털 페이지 상단의 **검색창**에 *container registries*를 입력하고 나타나는 옵션에서 **Container registries**를 선택합니다.

    ![Type container registries.](../../../../../../translated_images/ko/01-11-type-container-registries.ff3b8bdc49dc596c.png)

1. Azure Machine Learning 작업 영역과 연관된 컨테이너 레지스트리를 선택합니다. 예: *finetunephicontainerregistries*

1. 역할 할당 추가 페이지로 이동하기 위해 다음 작업을 수행합니다:

    - 왼쪽 탭에서 **액세스 제어(IAM)**를 선택합니다.
    - 탐색 메뉴에서 **+ 추가**를 선택합니다.
    - **역할 할당 추가**를 선택합니다.

1. 역할 할당 추가 페이지에서 다음 작업을 수행합니다:

    - 역할 페이지의 **검색창**에 *AcrPull*을 입력하고 나타나는 옵션에서 **AcrPull**을 선택합니다.
    - 역할 페이지에서 **다음**을 선택합니다.
    - 사용자 페이지에서 **액세스 권한 부여 대상**을 **Managed identity**로 선택합니다.
    - 사용자 페이지에서 **+ 구성원 선택**을 선택합니다.
    - 관리 ID 선택 페이지에서 Azure **구독**을 선택합니다.
    - 관리 ID 선택 페이지에서 **Managed identity**를 선택합니다.
    - 관리 ID 선택 페이지에서 생성한 관리 ID를 선택합니다. 예: *finetunephi-managedidentity*
    - 관리 ID 선택 페이지에서 **선택**을 선택합니다.
    - **검토 + 할당**을 클릭합니다.

### 프로젝트 설정

이제 작업할 폴더를 만들고, 사용자와 상호작용하며 Azure Cosmos DB에 저장된 채팅 기록을 이용해 응답하는 프로그램 개발을 위해 가상 환경을 설정합니다.

#### 작업할 폴더 만들기

1. 터미널 창을 열고 기본 경로에 *finetune-phi*라는 이름의 폴더를 만들기 위해 다음 명령어를 입력합니다.

    ```console
    mkdir finetune-phi
    ```

1. 터미널에서 다음 명령어를 입력해 만든 *finetune-phi* 폴더로 이동합니다.

    ```console
    cd finetune-phi
    ```

#### 가상 환경 만들기

1. 터미널에서 *.venv*라는 이름의 가상 환경을 생성하려면 다음 명령어를 입력합니다.

    ```console
    python -m venv .venv
    ```

1. 터미널에서 가상 환경을 활성화하려면 다음 명령어를 입력합니다.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> 성공적으로 작동했다면 명령 프롬프트 앞에 *(.venv)*가 표시됩니다.

#### 필요한 패키지 설치

1. 터미널에서 필요한 패키지들을 설치하려면 다음 명령어를 입력합니다.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### 프로젝트 파일 만들기
이 연습에서는 프로젝트에 필요한 필수 파일들을 만듭니다. 이 파일들에는 데이터 세트 다운로드, Azure Machine Learning 환경 설정, Phi-3 모델 미세 조정, 미세 조정된 모델 배포를 위한 스크립트가 포함됩니다. 또한 미세 조정 환경을 설정하기 위한 *conda.yml* 파일도 만듭니다.

이 연습에서 수행할 작업:

- 데이터 세트를 다운로드하는 *download_dataset.py* 파일 생성
- Azure Machine Learning 환경을 설정하는 *setup_ml.py* 파일 생성
- *finetuning_dir* 폴더 내에 Phi-3 모델을 데이터 세트로 미세 조정하는 *fine_tune.py* 파일 생성
- 미세 조정 환경을 설정하는 *conda.yml* 파일 생성
- 미세 조정된 모델을 배포하는 *deploy_model.py* 파일 생성
- 미세 조정된 모델을 Prompt flow와 통합하고 실행하는 *integrate_with_promptflow.py* 파일 생성
- Prompt flow 워크플로우 구조를 설정하는 flow.dag.yml 파일 생성
- Azure 정보를 입력하는 *config.py* 파일 생성

> [!NOTE]
>
> 전체 폴더 구조:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        ├── finetuning_dir
> .        │      └── fine_tune.py
> .        ├── conda.yml
> .        ├── config.py
> .        ├── deploy_model.py
> .        ├── download_dataset.py
> .        ├── flow.dag.yml
> .        ├── integrate_with_promptflow.py
> .        └── setup_ml.py
> ```

1. **Visual Studio Code**를 엽니다.

1. 메뉴 바에서 **파일(File)**을 선택합니다.

1. **폴더 열기(Open Folder)**를 선택합니다.

1. *finetune-phi* 폴더를 선택합니다. 이 폴더는 *C:\Users\yourUserName\finetune-phi* 경로에 있습니다.

    ![프로젝트 폴더 열기](../../../../../../translated_images/ko/01-12-open-project-folder.1fff9c7f41dd1639.png)

1. Visual Studio Code의 왼쪽 창에서 우클릭 후 **새 파일(New File)**을 선택하여 *download_dataset.py* 파일을 생성합니다.

1. Visual Studio Code 왼쪽 창에서 우클릭 후 **새 파일(New File)**을 선택하여 *setup_ml.py* 파일을 생성합니다.

1. Visual Studio Code 왼쪽 창에서 우클릭 후 **새 파일(New File)**을 선택하여 *deploy_model.py* 파일을 생성합니다.

    ![새 파일 생성](../../../../../../translated_images/ko/01-13-create-new-file.c17c150fff384a39.png)

1. Visual Studio Code 왼쪽 창에서 우클릭 후 **새 폴더(New Folder)**를 선택하여 *finetuning_dir* 폴더를 생성합니다.

1. *finetuning_dir* 폴더 안에 *fine_tune.py* 파일을 생성합니다.

#### *conda.yml* 파일 생성 및 구성

1. Visual Studio Code 왼쪽 창에서 우클릭 후 **새 파일(New File)**을 선택하여 *conda.yml* 파일을 생성합니다.

1. Phi-3 모델 미세 조정 환경을 설정하기 위해 *conda.yml* 파일에 다음 코드를 추가합니다.

    ```yml
    name: phi-3-training-env
    channels:
      - defaults
      - conda-forge
    dependencies:
      - python=3.10
      - pip
      - numpy<2.0
      - pip:
          - torch==2.4.0
          - torchvision==0.19.0
          - trl==0.8.6
          - transformers==4.41
          - datasets==2.21.0
          - azureml-core==1.57.0
          - azure-storage-blob==12.19.0
          - azure-ai-ml==1.16
          - azure-identity==1.17.1
          - accelerate==0.33.0
          - mlflow==2.15.1
          - azureml-mlflow==1.57.0
    ```

#### *config.py* 파일 생성 및 구성

1. Visual Studio Code 왼쪽 창에서 우클릭 후 **새 파일(New File)**을 선택하여 *config.py* 파일을 생성합니다.

1. Azure 정보를 포함하기 위해 *config.py* 파일에 다음 코드를 추가합니다.

    ```python
    # Azure 설정
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Azure 머신 러닝 설정
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Azure 관리 ID 설정
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # 데이터셋 파일 경로
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # 미세 조정된 모델 설정
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### Azure 환경 변수 추가하기

1. Azure 구독 ID를 추가하기 위한 작업:

    - 포털 페이지 상단 검색창에 *subscriptions*를 입력하고 나타나는 옵션 중 **구독(Subscriptions)**을 선택합니다.
    - 현재 사용 중인 Azure 구독을 선택합니다.
    - 구독 ID를 복사하여 *config.py* 파일에 붙여넣기 합니다.

    ![구독 ID 찾기](../../../../../../translated_images/ko/01-14-find-subscriptionid.4f4ca33555f1e637.png)

1. Azure 작업 영역 이름을 추가하기 위한 작업:

    - 생성한 Azure Machine Learning 리소스로 이동합니다.
    - 계정 이름을 복사하여 *config.py* 파일에 붙여넣기 합니다.

    ![Azure Machine Learning 이름 찾기](../../../../../../translated_images/ko/01-15-find-AZML-name.1975f0422bca19a7.png)

1. Azure 리소스 그룹 이름을 추가하기 위한 작업:

    - 생성한 Azure Machine Learning 리소스로 이동합니다.
    - Azure 리소스 그룹 이름을 복사하여 *config.py* 파일에 붙여넣기 합니다.

    ![리소스 그룹 이름 찾기](../../../../../../translated_images/ko/01-16-find-AZML-resourcegroup.855a349d0af134a3.png)

2. Azure 관리 ID 이름 추가하기:

    - 생성한 관리 ID(Managed Identities) 리소스로 이동합니다.
    - Azure 관리 ID 이름을 복사하여 *config.py* 파일에 붙여넣기 합니다.

    ![UAI 찾기](../../../../../../translated_images/ko/01-17-find-uai.3529464f53499827.png)

### 미세 조정을 위한 데이터 세트 준비

이 연습에서는 *download_dataset.py* 파일을 실행하여 *ULTRACHAT_200k* 데이터 세트를 로컬 환경에 다운로드합니다. 이후 이 데이터 세트를 활용하여 Azure Machine Learning에서 Phi-3 모델을 미세 조정합니다.

#### *download_dataset.py* 파일로 데이터 세트 다운로드하기

1. Visual Studio Code에서 *download_dataset.py* 파일을 엽니다.

1. 다음 코드를 *download_dataset.py* 파일에 추가합니다.

    ```python
    import json
    import os
    from datasets import load_dataset
    from config import (
        TRAIN_DATA_PATH,
        TEST_DATA_PATH)

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # 지정된 이름, 구성 및 분할 비율로 데이터셋을 로드합니다
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # 데이터셋을 학습 세트와 테스트 세트로 분할합니다 (학습 80%, 테스트 20%)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # 디렉터리가 없으면 생성합니다
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # 파일을 쓰기 모드로 엽니다
        with open(filepath, 'w', encoding='utf-8') as f:
            # 데이터셋의 각 기록을 반복합니다
            for record in dataset:
                # 기록을 JSON 객체로 덤프하여 파일에 씁니다
                json.dump(record, f)
                # 기록을 구분하기 위해 줄 바꿈 문자를 씁니다
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # ULTRACHAT_200k 데이터셋을 특정 구성과 분할 비율로 로드하고 분할합니다
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # 분할된 데이터에서 학습 및 테스트 데이터셋을 추출합니다
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # 학습 데이터셋을 JSONL 파일로 저장합니다
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # 테스트 데이터셋을 별도의 JSONL 파일로 저장합니다
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **CPU를 사용하여 최소 데이터 세트로 미세 조정하는 가이드라인**
>
> CPU를 사용해 미세 조정하려는 경우, 이 방법은 Visual Studio Enterprise 구독과 같은 혜택 구독 보유자나 미세 조정 및 배포 과정을 빠르게 테스트하려는 분들에게 적합합니다.
>
> `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` 코드를 `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`로 변경하세요.
>

1. 터미널에 다음 명령을 입력하여 스크립트를 실행하고 데이터 세트를 로컬 환경에 다운로드합니다.

    ```console
    python download_data.py
    ```

1. 데이터 세트가 로컬 *finetune-phi/data* 디렉터리에 정상적으로 저장되었는지 확인합니다.

> [!NOTE]
>
> **데이터 세트 크기 및 미세 조정 시간**
>
> 이 E2E 샘플에서는 데이터의 1%만 사용(`train_sft[:1%]`)하므로 데이터 양이 현저히 줄어들어 업로드와 미세 조정 시간이 단축됩니다. 데이터 사용량 비율은 훈련 시간과 모델 성능 간 균형을 맞추기 위해 조절할 수 있습니다. 적은 데이터 세트를 사용할수록 미세 조정 시간이 줄어들어 E2E 샘플에 더 적합합니다.

## 시나리오 2: Phi-3 모델 미세 조정 및 Azure Machine Learning Studio에 배포하기

### Azure CLI 설정

Azure 환경을 인증하려면 Azure CLI를 설정해야 합니다. Azure CLI는 명령줄에서 직접 Azure 리소스를 관리하고 Azure Machine Learning이 이러한 리소스에 접근할 수 있는 자격 증명을 제공합니다. 시작하려면 [Azure CLI 설치](https://learn.microsoft.com/cli/azure/install-azure-cli)를 참고하세요.

1. 터미널을 열고 다음 명령으로 Azure 계정에 로그인합니다.

    ```console
    az login
    ```

1. 사용할 Azure 계정을 선택합니다.

1. 사용할 Azure 구독을 선택합니다.

    ![리소스 그룹 이름 확인](../../../../../../translated_images/ko/02-01-login-using-azure-cli.dfde31cb75e58a87.png)

> [!TIP]
>
> Azure 로그인에 문제가 있으면 디바이스 코드를 사용해 보세요. 터미널 창을 열고 다음 명령을 입력하여 Azure 계정에 로그인합니다:
>
> ```console
> az login --use-device-code
> ```
>

### Phi-3 모델 미세 조정

이 연습에서는 제공된 데이터 세트를 사용해 Phi-3 모델을 미세 조정합니다. 먼저 *fine_tune.py* 파일에서 미세 조정 과정을 정의합니다. 이후 Azure Machine Learning 환경을 구성하고 *setup_ml.py* 파일을 실행해 미세 조정을 시작합니다. 이 스크립트는 Azure Machine Learning 환경 내에서 미세 조정을 실행하게 합니다.

*setup_ml.py*를 실행하면 Azure Machine Learning 환경에서 미세 조정 과정이 실행됩니다.

#### *fine_tune.py* 파일에 코드 추가

1. *finetuning_dir* 폴더로 이동하여 Visual Studio Code에서 *fine_tune.py* 파일을 엽니다.

1. *fine_tune.py* 파일에 다음 코드를 추가합니다.

    ```python
    import argparse
    import sys
    import logging
    import os
    from datasets import load_dataset
    import torch
    import mlflow
    from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
    from trl import SFTTrainer

    # MLflow에서 INVALID_PARAMETER_VALUE 오류를 피하려면 MLflow 통합을 비활성화하세요
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # 로깅 설정
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
        level=logging.WARNING
    )
    logger = logging.getLogger(__name__)

    def initialize_model_and_tokenizer(model_name, model_kwargs):
        """
        Initialize the model and tokenizer with the given pretrained model name and arguments.
        """
        model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.model_max_length = 2048
        tokenizer.pad_token = tokenizer.unk_token
        tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids(tokenizer.pad_token)
        tokenizer.padding_side = 'right'
        return model, tokenizer

    def apply_chat_template(example, tokenizer):
        """
        Apply a chat template to tokenize messages in the example.
        """
        messages = example["messages"]
        if messages[0]["role"] != "system":
            messages.insert(0, {"role": "system", "content": ""})
        example["text"] = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        return example

    def load_and_preprocess_data(train_filepath, test_filepath, tokenizer):
        """
        Load and preprocess the dataset.
        """
        train_dataset = load_dataset('json', data_files=train_filepath, split='train')
        test_dataset = load_dataset('json', data_files=test_filepath, split='train')
        column_names = list(train_dataset.features)

        train_dataset = train_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to train dataset",
        )

        test_dataset = test_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to test dataset",
        )

        return train_dataset, test_dataset

    def train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, output_dir):
        """
        Train and evaluate the model.
        """
        training_args = TrainingArguments(
            bf16=True,
            do_eval=True,
            output_dir=output_dir,
            eval_strategy="epoch",
            learning_rate=5.0e-06,
            logging_steps=20,
            lr_scheduler_type="cosine",
            num_train_epochs=3,
            overwrite_output_dir=True,
            per_device_eval_batch_size=4,
            per_device_train_batch_size=4,
            remove_unused_columns=True,
            save_steps=500,
            seed=0,
            gradient_checkpointing=True,
            gradient_accumulation_steps=1,
            warmup_ratio=0.2,
        )

        trainer = SFTTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            max_seq_length=2048,
            dataset_text_field="text",
            tokenizer=tokenizer,
            packing=True
        )

        train_result = trainer.train()
        trainer.log_metrics("train", train_result.metrics)

        mlflow.transformers.log_model(
            transformers_model={"model": trainer.model, "tokenizer": tokenizer},
            artifact_path=output_dir,
        )

        tokenizer.padding_side = 'left'
        eval_metrics = trainer.evaluate()
        eval_metrics["eval_samples"] = len(test_dataset)
        trainer.log_metrics("eval", eval_metrics)

    def main(train_file, eval_file, model_output_dir):
        """
        Main function to fine-tune the model.
        """
        model_kwargs = {
            "use_cache": False,
            "trust_remote_code": True,
            "torch_dtype": torch.bfloat16,
            "device_map": None,
            "attn_implementation": "eager"
        }

        # pretrained_model_name = "microsoft/Phi-3-mini-4k-instruct"
        pretrained_model_name = "microsoft/Phi-3.5-mini-instruct"

        with mlflow.start_run():
            model, tokenizer = initialize_model_and_tokenizer(pretrained_model_name, model_kwargs)
            train_dataset, test_dataset = load_and_preprocess_data(train_file, eval_file, tokenizer)
            train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, model_output_dir)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--train-file", type=str, required=True, help="Path to the training data")
        parser.add_argument("--eval-file", type=str, required=True, help="Path to the evaluation data")
        parser.add_argument("--model_output_dir", type=str, required=True, help="Directory to save the fine-tuned model")
        args = parser.parse_args()
        main(args.train_file, args.eval_file, args.model_output_dir)

    ```

1. *fine_tune.py* 파일을 저장하고 닫습니다.

> [!TIP]
> **Phi-3.5 모델도 미세 조정할 수 있습니다**
>
> *fine_tune.py*에서 `pretrained_model_name` 값을 `"microsoft/Phi-3-mini-4k-instruct"`에서 원하는 모델로 변경할 수 있습니다. 예를 들어 `"microsoft/Phi-3.5-mini-instruct"`로 변경하면 Phi-3.5-mini-instruct 모델로 미세 조정합니다. 원하는 모델 이름을 찾으려면 [Hugging Face](https://huggingface.co/)를 방문해 모델을 검색 후 이름을 복사하여 스크립트의 `pretrained_model_name` 필드에 붙여 넣으세요.
>
> <image type="content" src="../../../../imgs/02/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Phi-3.5 미세 조정">
>

#### *setup_ml.py* 파일에 코드 추가

1. Visual Studio Code에서 *setup_ml.py* 파일을 엽니다.

1. *setup_ml.py*에 다음 코드를 추가합니다.

    ```python
    import logging
    from azure.ai.ml import MLClient, command, Input
    from azure.ai.ml.entities import Environment, AmlCompute
    from azure.identity import AzureCliCredential
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        TRAIN_DATA_PATH,
        TEST_DATA_PATH
    )

    # 상수

    # 훈련을 위해 CPU 인스턴스를 사용하려면 다음 줄 주석 처리를 해제하세요
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # 훈련을 위해 GPU 인스턴스를 사용하려면 다음 줄 주석 처리를 해제하세요
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # 컴퓨트 클러스터 위치로 교체하세요
    FINETUNING_DIR = "./finetuning_dir" # 미세 조정 스크립트 경로
    TRAINING_ENV_NAME = "phi-3-training-environment" # 훈련 환경 이름
    MODEL_OUTPUT_DIR = "./model_output" # Azure ML의 모델 출력 디렉터리 경로

    # 프로세스를 추적하기 위한 로깅 설정
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.WARNING
    )

    def get_ml_client():
        """
        Initialize the ML Client using Azure CLI credentials.
        """
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def create_or_get_environment(ml_client):
        """
        Create or update the training environment in Azure ML.
        """
        env = Environment(
            image=DOCKER_IMAGE_NAME,  # 환경용 도커 이미지
            conda_file=CONDA_FILE,  # Conda 환경 파일
            name=TRAINING_ENV_NAME,  # 환경 이름
        )
        return ml_client.environments.create_or_update(env)

    def create_or_get_compute_cluster(ml_client, compute_name, COMPUTE_INSTANCE_TYPE, location):
        """
        Create or update the compute cluster in Azure ML.
        """
        try:
            compute_cluster = ml_client.compute.get(compute_name)
            logger.info(f"Compute cluster '{compute_name}' already exists. Reusing it for the current run.")
        except Exception:
            logger.info(f"Compute cluster '{compute_name}' does not exist. Creating a new one with size {COMPUTE_INSTANCE_TYPE}.")
            compute_cluster = AmlCompute(
                name=compute_name,
                size=COMPUTE_INSTANCE_TYPE,
                location=location,
                tier="Dedicated",  # 컴퓨트 클러스터 등급
                min_instances=0,  # 최소 인스턴스 수
                max_instances=1  # 최대 인스턴스 수
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # 클러스터가 생성될 때까지 대기
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # fine_tune.py 경로
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # 훈련 환경
            compute=compute_name,  # 사용할 컴퓨트 클러스터
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # 훈련 데이터 파일 경로
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # 평가 데이터 파일 경로
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # ML 클라이언트 초기화
        ml_client = get_ml_client()

        # 환경 생성
        env = create_or_get_environment(ml_client)
        
        # 기존 컴퓨트 클러스터 생성 또는 가져오기
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # 미세 조정 작업 생성 및 제출
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # 작업 제출
        ml_client.jobs.stream(returned_job.name)  # 작업 로그 스트리밍
        
        # 작업 이름 캡처
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, `LOCATION`을 자신의 환경에 맞게 변경합니다.

    ```python
   # 훈련에 GPU 인스턴스를 사용하려면 다음 줄의 주석 처리를 해제하십시오
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # 컴퓨팅 클러스터 위치로 바꾸십시오
    ```

> [!TIP]
>
> **CPU를 사용해 최소 데이터 세트로 미세 조정하는 가이드라인**
>
> CPU를 사용하고자 한다면, 이 방법은 Visual Studio Enterprise 구독자 또는 미세 조정 및 배포를 신속 테스트하려는 분들에게 적합합니다.
>
> 1. *setup_ml* 파일을 엽니다.
> 1. `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, `DOCKER_IMAGE_NAME`을 다음과 같이 변경합니다. *Standard_E16s_v3*에 접근 권한이 없으면 동급의 CPU 인스턴스를 사용하거나 쿼터 증액을 요청할 수 있습니다.
> 1. `LOCATION`을 자신의 환경에 맞게 변경합니다.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. 터미널에서 다음 명령을 입력하여 *setup_ml.py* 스크립트를 실행하고 Azure Machine Learning에서 미세 조정을 시작합니다.

    ```python
    python setup_ml.py
    ```

1. 이번 연습에서 Azure Machine Learning을 사용해 Phi-3 모델을 성공적으로 미세 조정했습니다. *setup_ml.py*를 실행함으로써 Azure Machine Learning 환경이 설정되고 *fine_tune.py*에 정의된 미세 조정 과정이 시작됩니다. 미세 조정 작업은 상당한 시간이 걸릴 수 있으니, `python setup_ml.py` 명령어 실행 후 완료될 때까지 기다립니다. 터미널에 출력된 링크를 통해 Azure Machine Learning 포털에서 작업 상태를 실시간으로 확인할 수 있습니다.

    ![미세 조정 작업 확인](../../../../../../translated_images/ko/02-02-see-finetuning-job.59393bc3b143871e.png)

### 미세 조정된 모델 배포

미세 조정된 Phi-3 모델을 Prompt Flow와 통합하려면 모델을 배포하여 실시간 추론에 사용할 수 있도록 해야 합니다. 이 과정은 모델 등록, 온라인 엔드포인트 생성, 모델 배포 순으로 진행됩니다.

#### 배포용 모델 이름, 엔드포인트 이름, 배포 이름 설정

1. *config.py* 파일을 엽니다.

1. `AZURE_MODEL_NAME = "your_fine_tuned_model_name"`를 원하는 모델 이름으로 변경합니다.

1. `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"`를 원하는 엔드포인트 이름으로 변경합니다.

1. `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"`를 원하는 배포 이름으로 변경합니다.

#### *deploy_model.py* 파일에 코드 추가

*deploy_model.py* 파일을 실행하면 전체 배포 과정이 자동화됩니다. 이 스크립트는 *config.py*에 지정된 모델 이름, 엔드포인트 이름, 배포 이름 설정을 바탕으로 모델 등록, 엔드포인트 생성, 배포 작업을 수행합니다.

1. Visual Studio Code에서 *deploy_model.py* 파일을 엽니다.

1. *deploy_model.py* 파일에 다음 코드를 추가합니다.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # 구성 가져오기
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        AZURE_MANAGED_IDENTITY_RESOURCE_ID,
        AZURE_MANAGED_IDENTITY_CLIENT_ID,
        AZURE_MODEL_NAME,
        AZURE_ENDPOINT_NAME,
        AZURE_DEPLOYMENT_NAME
    )

    # 상수
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # 로깅 설정
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def get_ml_client():
        """Initialize and return the ML Client."""
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def register_model(ml_client, model_name, job_name):
        """Register a new model."""
        model_path = f"azureml://jobs/{job_name}/outputs/artifacts/paths/model_output"
        logger.info(f"Registering model {model_name} from job {job_name} at path {model_path}.")
        run_model = Model(
            path=model_path,
            name=model_name,
            description="Model created from run.",
            type=AssetTypes.MLFLOW_MODEL,
        )
        model = ml_client.models.create_or_update(run_model)
        logger.info(f"Registered model ID: {model.id}")
        return model

    def delete_existing_endpoint(ml_client, endpoint_name):
        """Delete existing endpoint if it exists."""
        try:
            endpoint_result = ml_client.online_endpoints.get(name=endpoint_name)
            logger.info(f"Deleting existing endpoint {endpoint_name}.")
            ml_client.online_endpoints.begin_delete(name=endpoint_name).result()
            logger.info(f"Deleted existing endpoint {endpoint_name}.")
        except Exception as e:
            logger.info(f"No existing endpoint {endpoint_name} found to delete: {e}")

    def create_or_update_endpoint(ml_client, endpoint_name, description=""):
        """Create or update an endpoint."""
        delete_existing_endpoint(ml_client, endpoint_name)
        logger.info(f"Creating new endpoint {endpoint_name}.")
        endpoint = ManagedOnlineEndpoint(
            name=endpoint_name,
            description=description,
            identity=IdentityConfiguration(
                type="user_assigned",
                user_assigned_identities=[ManagedIdentityConfiguration(resource_id=AZURE_MANAGED_IDENTITY_RESOURCE_ID)]
            )
        )
        endpoint_result = ml_client.online_endpoints.begin_create_or_update(endpoint).result()
        logger.info(f"Created new endpoint {endpoint_name}.")
        return endpoint_result

    def create_or_update_deployment(ml_client, endpoint_name, deployment_name, model):
        """Create or update a deployment."""

        logger.info(f"Creating deployment {deployment_name} for endpoint {endpoint_name}.")
        deployment = ManagedOnlineDeployment(
            name=deployment_name,
            endpoint_name=endpoint_name,
            model=model.id,
            instance_type=COMPUTE_INSTANCE_TYPE,
            instance_count=1,
            environment_variables=deployment_env_vars,
            request_settings=OnlineRequestSettings(
                max_concurrent_requests_per_instance=3,
                request_timeout_ms=180000,
                max_queue_wait_ms=120000
            ),
            liveness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
            readiness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
        )
        deployment_result = ml_client.online_deployments.begin_create_or_update(deployment).result()
        logger.info(f"Created deployment {deployment.name} for endpoint {endpoint_name}.")
        return deployment_result

    def set_traffic_to_deployment(ml_client, endpoint_name, deployment_name):
        """Set traffic to the specified deployment."""
        try:
            # 현재 엔드포인트 세부정보 가져오기
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # 디버깅을 위한 현재 트래픽 할당 로그 기록
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # 배포를 위한 트래픽 할당 설정
            endpoint.traffic = {deployment_name: 100}
            
            # 새로운 트래픽 할당으로 엔드포인트 업데이트
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # 디버깅을 위한 업데이트된 트래픽 할당 로그 기록
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # 프로세스 중 발생하는 오류 로그 기록
            logger.error(f"Failed to set traffic to deployment: {e}")
            raise


    def main():
        ml_client = get_ml_client()

        registered_model = register_model(ml_client, AZURE_MODEL_NAME, JOB_NAME)
        logger.info(f"Registered model ID: {registered_model.id}")

        endpoint = create_or_update_endpoint(ml_client, AZURE_ENDPOINT_NAME, "Endpoint for finetuned Phi-3 model")
        logger.info(f"Endpoint {AZURE_ENDPOINT_NAME} is ready.")

        try:
            deployment = create_or_update_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME, registered_model)
            logger.info(f"Deployment {AZURE_DEPLOYMENT_NAME} is created for endpoint {AZURE_ENDPOINT_NAME}.")

            set_traffic_to_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME)
            logger.info(f"Traffic is set to deployment {AZURE_DEPLOYMENT_NAME} at endpoint {AZURE_ENDPOINT_NAME}.")
        except Exception as e:
            logger.error(f"Failed to create or update deployment: {e}")

    if __name__ == "__main__":
        main()

    ```

1. `JOB_NAME`을 얻기 위한 작업:

    - 생성한 Azure Machine Learning 리소스로 이동합니다.
    - **Studio web URL**을 선택하여 Azure Machine Learning 작업 영역을 엽니다.
    - 왼쪽 탭에서 **Jobs**를 선택합니다.
    - 미세 조정 실험(예: *finetunephi*)을 선택합니다.
    - 생성된 작업(job)을 선택합니다.
- *deploy_model.py* 파일의 `JOB_NAME = "your-job-name"`에 작업 이름을 복사하여 붙여넣으세요.

1. `COMPUTE_INSTANCE_TYPE`을 자신의 세부 정보로 바꾸세요.

1. 다음 명령어를 입력하여 *deploy_model.py* 스크립트를 실행하고 Azure Machine Learning에서 배포 프로세스를 시작하세요.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> 추가 요금이 발생하지 않도록 Azure Machine Learning 작업 영역에서 생성한 엔드포인트를 반드시 삭제하세요.
>

#### Azure Machine Learning 작업 영역에서 배포 상태 확인

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)를 방문하세요.

1. 생성한 Azure Machine Learning 작업 영역으로 이동하세요.

1. Azure Machine Learning 작업 영역을 열려면 **Studio web URL**을 선택하세요.

1. 왼쪽 탭에서 **Endpoints**를 선택하세요.

    ![Select endpoints.](../../../../../../translated_images/ko/02-03-select-endpoints.c3136326510baff1.png)

2. 생성한 엔드포인트를 선택하세요.

    ![Select endpoints that you created.](../../../../../../translated_images/ko/02-04-select-endpoint-created.0363e7dca51dabb4.png)

3. 이 페이지에서 배포 과정 중 생성된 엔드포인트를 관리할 수 있습니다.

## 시나리오 3: Prompt flow와 통합하고 맞춤 모델과 채팅하기

### 맞춤 Phi-3 모델을 Prompt flow와 통합하기

미세 조정한 모델을 성공적으로 배포한 후, 이제 Prompt flow에 통합하여 맞춤 Phi-3 모델로 실시간 애플리케이션에서 다양한 인터랙티브 작업을 수행할 수 있습니다.

#### 미세 조정된 Phi-3 모델의 api 키 및 엔드포인트 URI 설정

1. 생성한 Azure Machine Learning 작업 영역으로 이동하세요.
1. 왼쪽 탭에서 **Endpoints**를 선택하세요.
1. 생성한 엔드포인트를 선택하세요.
1. 네비게이션 메뉴에서 **Consume**을 선택하세요.
1. **REST endpoint**를 복사하여 *config.py* 파일의 `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` 부분에 붙여넣으세요.
1. **Primary key**를 복사하여 *config.py* 파일의 `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` 부분에 붙여넣으세요.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/ko/02-05-copy-apikey-endpoint.88b5a92e6462c53b.png)

#### *flow.dag.yml* 파일에 코드 추가

1. Visual Studio Code에서 *flow.dag.yml* 파일을 엽니다.

1. *flow.dag.yml*에 다음 코드를 추가하세요.

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

#### *integrate_with_promptflow.py* 파일에 코드 추가

1. Visual Studio Code에서 *integrate_with_promptflow.py* 파일을 엽니다.

1. *integrate_with_promptflow.py*에 다음 코드를 추가하세요.

    ```python
    import logging
    import requests
    from promptflow.core import tool
    import asyncio
    import platform
    from config import (
        AZURE_ML_ENDPOINT,
        AZURE_ML_API_KEY
    )

    # 로깅 설정
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_azml_endpoint(input_data: list, endpoint_url: str, api_key: str) -> str:
        """
        Send a request to the Azure ML endpoint with the given input data.
        """
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
            result = response.json()[0]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    def setup_asyncio_policy():
        """
        Setup asyncio event loop policy for Windows.
        """
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            logger.info("Set Windows asyncio event loop policy.")

    @tool
    def my_python_tool(input_data: str) -> str:
        """
        Tool function to process input data and query the Azure ML endpoint.
        """
        setup_asyncio_policy()
        return query_azml_endpoint(input_data, AZURE_ML_ENDPOINT, AZURE_ML_API_KEY)

    ```

### 맞춤 모델과 채팅하기

1. 다음 명령어를 입력하여 *deploy_model.py* 스크립트를 실행하고 Azure Machine Learning에서 배포 프로세스를 시작하세요.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. 결과 예시는 다음과 같습니다: 이제 맞춤 Phi-3 모델과 채팅할 수 있습니다. 미세 조정에 사용된 데이터를 기반으로 질문하는 것이 권장됩니다.

    ![Prompt flow example.](../../../../../../translated_images/ko/02-06-promptflow-example.89384abaf3ad71f6.png)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 이용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->