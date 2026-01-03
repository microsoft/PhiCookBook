<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-07-17T00:15:08+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "ko"
}
-->
# Fine-tune 및 Prompt flow와 함께 맞춤형 Phi-3 모델 통합하기

이 종합 샘플은 Microsoft Tech Community의 가이드 "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)"를 기반으로 합니다. 이 가이드는 맞춤형 Phi-3 모델을 미세 조정하고, 배포하며, Prompt flow와 통합하는 과정을 소개합니다.

## 개요

이 종합 샘플에서는 Phi-3 모델을 미세 조정하고 Prompt flow와 통합하는 방법을 배웁니다. Azure Machine Learning과 Prompt flow를 활용하여 맞춤형 AI 모델을 배포하고 활용하는 워크플로우를 구축할 수 있습니다. 이 샘플은 세 가지 시나리오로 나누어져 있습니다:

**시나리오 1: Azure 리소스 설정 및 미세 조정 준비**

**시나리오 2: Phi-3 모델 미세 조정 및 Azure Machine Learning Studio에 배포**

**시나리오 3: Prompt flow와 통합하고 맞춤형 모델과 채팅하기**

아래는 이 종합 샘플의 개요입니다.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.02fc569e266d468c.ko.png)

### 목차

1. **[시나리오 1: Azure 리소스 설정 및 미세 조정 준비](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning 작업 영역 생성](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure 구독에서 GPU 할당량 요청](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [역할 할당 추가](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [프로젝트 설정](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [미세 조정을 위한 데이터셋 준비](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[시나리오 2: Phi-3 모델 미세 조정 및 Azure Machine Learning Studio에 배포](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure CLI 설정](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 모델 미세 조정](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [미세 조정된 모델 배포](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[시나리오 3: Prompt flow와 통합하고 맞춤형 모델과 채팅하기](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [맞춤형 Phi-3 모델을 Prompt flow와 통합](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [맞춤형 모델과 채팅하기](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## 시나리오 1: Azure 리소스 설정 및 미세 조정 준비

### Azure Machine Learning 작업 영역 생성

1. 포털 페이지 상단의 **검색창**에 *azure machine learning*을 입력하고 나타나는 옵션 중 **Azure Machine Learning**을 선택합니다.

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.a5116f8454d98c60.ko.png)

1. 탐색 메뉴에서 **+ 생성**을 선택합니다.

1. 탐색 메뉴에서 **새 작업 영역**을 선택합니다.

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.83e17436f8898dc4.ko.png)

1. 다음 작업을 수행합니다:

    - Azure **구독**을 선택합니다.
    - 사용할 **리소스 그룹**을 선택합니다(필요 시 새로 만듭니다).
    - **작업 영역 이름**을 입력합니다. 고유한 값이어야 합니다.
    - 사용할 **지역**을 선택합니다.
    - 사용할 **스토리지 계정**을 선택합니다(필요 시 새로 만듭니다).
    - 사용할 **키 볼트**를 선택합니다(필요 시 새로 만듭니다).
    - 사용할 **애플리케이션 인사이트**를 선택합니다(필요 시 새로 만듭니다).
    - 사용할 **컨테이너 레지스트리**를 선택합니다(필요 시 새로 만듭니다).

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.730a5177757bbebb.ko.png)

1. **검토 + 생성**을 선택합니다.

1. **생성**을 선택합니다.

### Azure 구독에서 GPU 할당량 요청

이 샘플에서는 미세 조정을 위해 *Standard_NC24ads_A100_v4 GPU*를 사용하며, 이 GPU는 할당량 요청이 필요합니다. 배포에는 할당량 요청이 필요 없는 *Standard_E4s_v3* CPU를 사용합니다.

> [!NOTE]
>
> GPU 할당은 Pay-As-You-Go 구독(표준 구독 유형)에서만 가능하며, 혜택 구독은 현재 지원되지 않습니다.
>
> 혜택 구독(예: Visual Studio Enterprise Subscription)을 사용하거나 미세 조정 및 배포 과정을 빠르게 테스트하려는 경우, 이 튜토리얼에서는 CPU를 사용해 최소한의 데이터셋으로 미세 조정하는 방법도 안내합니다. 다만, GPU와 더 큰 데이터셋을 사용할 때 미세 조정 결과가 훨씬 우수하다는 점을 참고하세요.

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)에 접속합니다.

1. *Standard NCADSA100v4 Family* 할당량을 요청하려면 다음 작업을 수행합니다:

    - 왼쪽 탭에서 **할당량**을 선택합니다.
    - 사용할 **가상 머신 패밀리**를 선택합니다. 예를 들어, *Standard NCADSA100v4 Family Cluster Dedicated vCPUs*를 선택하면 *Standard_NC24ads_A100_v4* GPU가 포함됩니다.
    - 탐색 메뉴에서 **할당량 요청**을 선택합니다.

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.3d3670c3221ab834.ko.png)

    - 할당량 요청 페이지에서 원하는 **새 코어 제한**을 입력합니다. 예: 24.
    - 할당량 요청 페이지에서 **제출**을 선택해 GPU 할당량을 요청합니다.

> [!NOTE]
> 필요에 따라 적합한 GPU 또는 CPU를 선택하려면 [Azure 가상 머신 크기](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) 문서를 참고하세요.

### 역할 할당 추가

모델을 미세 조정하고 배포하려면 먼저 사용자 할당 관리 ID(User Assigned Managed Identity, UAI)를 생성하고 적절한 권한을 부여해야 합니다. 이 UAI는 배포 시 인증에 사용됩니다.

#### 사용자 할당 관리 ID(UAI) 생성

1. 포털 페이지 상단의 **검색창**에 *managed identities*를 입력하고 나타나는 옵션 중 **Managed Identities**를 선택합니다.

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.9297b6039874eff8.ko.png)

1. **+ 생성**을 선택합니다.

    ![Select create.](../../../../../../translated_images/01-06-select-create.936d8d66d7144f9a.ko.png)

1. 다음 작업을 수행합니다:

    - Azure **구독**을 선택합니다.
    - 사용할 **리소스 그룹**을 선택합니다(필요 시 새로 만듭니다).
    - 사용할 **지역**을 선택합니다.
    - **이름**을 입력합니다. 고유한 값이어야 합니다.

1. **검토 + 생성**을 선택합니다.

1. **+ 생성**을 선택합니다.

#### 관리 ID에 Contributor 역할 할당 추가

1. 생성한 관리 ID 리소스로 이동합니다.

1. 왼쪽 탭에서 **Azure 역할 할당**을 선택합니다.

1. 탐색 메뉴에서 **+ 역할 할당 추가**를 선택합니다.

1. 역할 할당 추가 페이지에서 다음 작업을 수행합니다:
    - **범위**를 **리소스 그룹**으로 선택합니다.
    - Azure **구독**을 선택합니다.
    - 사용할 **리소스 그룹**을 선택합니다.
    - **역할**을 **Contributor**로 선택합니다.

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.29ca99b7c9f687e0.ko.png)

1. **저장**을 선택합니다.

#### 관리 ID에 Storage Blob Data Reader 역할 할당 추가

1. 포털 페이지 상단의 **검색창**에 *storage accounts*를 입력하고 나타나는 옵션 중 **Storage accounts**를 선택합니다.

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.1186c8e42933e49b.ko.png)

1. 생성한 Azure Machine Learning 작업 영역과 연결된 스토리지 계정을 선택합니다. 예: *finetunephistorage*.

1. 역할 할당 추가 페이지로 이동하려면 다음 작업을 수행합니다:

    - 생성한 Azure 스토리지 계정으로 이동합니다.
    - 왼쪽 탭에서 **액세스 제어(IAM)**를 선택합니다.
    - 탐색 메뉴에서 **+ 추가**를 선택합니다.
    - **역할 할당 추가**를 선택합니다.

    ![Add role.](../../../../../../translated_images/01-09-add-role.d2db22fec1b187f0.ko.png)

1. 역할 할당 추가 페이지에서 다음 작업을 수행합니다:

    - 역할 페이지에서 **검색창**에 *Storage Blob Data Reader*를 입력하고 나타나는 옵션 중 **Storage Blob Data Reader**를 선택합니다.
    - 역할 페이지에서 **다음**을 선택합니다.
    - 멤버 페이지에서 **액세스 할당 대상**을 **Managed identity**로 선택합니다.
    - 멤버 페이지에서 **+ 멤버 선택**을 선택합니다.
    - 관리 ID 선택 페이지에서 Azure **구독**을 선택합니다.
    - 관리 ID 선택 페이지에서 **Managed identity**를 선택합니다.
    - 관리 ID 선택 페이지에서 생성한 관리 ID를 선택합니다. 예: *finetunephi-managedidentity*.
    - 관리 ID 선택 페이지에서 **선택**을 클릭합니다.

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.5ce5ba181f72a4df.ko.png)

1. **검토 + 할당**을 선택합니다.

#### 관리 ID에 AcrPull 역할 할당 추가

1. 포털 페이지 상단의 **검색창**에 *container registries*를 입력하고 나타나는 옵션 중 **Container registries**를 선택합니다.

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.ff3b8bdc49dc596c.ko.png)

1. Azure Machine Learning 작업 영역과 연결된 컨테이너 레지스트리를 선택합니다. 예: *finetunephicontainerregistries*

1. 역할 할당 추가 페이지로 이동하려면 다음 작업을 수행합니다:

    - 왼쪽 탭에서 **액세스 제어(IAM)**를 선택합니다.
    - 탐색 메뉴에서 **+ 추가**를 선택합니다.
    - **역할 할당 추가**를 선택합니다.

1. 역할 할당 추가 페이지에서 다음 작업을 수행합니다:

    - 역할 페이지에서 **검색창**에 *AcrPull*을 입력하고 나타나는 옵션 중 **AcrPull**을 선택합니다.
    - 역할 페이지에서 **다음**을 선택합니다.
    - 멤버 페이지에서 **액세스 할당 대상**을 **Managed identity**로 선택합니다.
    - 멤버 페이지에서 **+ 멤버 선택**을 선택합니다.
    - 관리 ID 선택 페이지에서 Azure **구독**을 선택합니다.
    - 관리 ID 선택 페이지에서 **Managed identity**를 선택합니다.
    - 관리 ID 선택 페이지에서 생성한 관리 ID를 선택합니다. 예: *finetunephi-managedidentity*.
    - 관리 ID 선택 페이지에서 **선택**을 클릭합니다.
    - **검토 + 할당**을 선택합니다.

### 프로젝트 설정

이제 작업할 폴더를 만들고, 사용자와 상호작용하며 Azure Cosmos DB에 저장된 채팅 기록을 활용해 응답하는 프로그램을 개발하기 위한 가상 환경을 설정합니다.

#### 작업할 폴더 생성

1. 터미널 창을 열고 기본 경로에 *finetune-phi*라는 이름의 폴더를 생성하려면 다음 명령어를 입력합니다.

    ```console
    mkdir finetune-phi
    ```

1. 터미널에서 다음 명령어를 입력해 생성한 *finetune-phi* 폴더로 이동합니다.

    ```console
    cd finetune-phi
    ```

#### 가상 환경 생성

1. 터미널에서 다음 명령어를 입력해 *.venv*라는 이름의 가상 환경을 생성합니다.

    ```console
    python -m venv .venv
    ```

1. 터미널에서 다음 명령어를 입력해 가상 환경을 활성화합니다.

    ```console
    .venv\Scripts\activate.bat
    ```
> [!NOTE]
>
> 제대로 작동했다면, 명령 프롬프트 앞에 *(.venv)*가 표시될 것입니다.
#### 필요한 패키지 설치하기

1. 터미널에서 다음 명령어를 입력하여 필요한 패키지를 설치하세요.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### 프로젝트 파일 생성하기

이번 실습에서는 프로젝트에 필요한 기본 파일들을 생성합니다. 이 파일들은 데이터셋 다운로드, Azure Machine Learning 환경 설정, Phi-3 모델 미세 조정, 미세 조정된 모델 배포를 위한 스크립트를 포함합니다. 또한 미세 조정 환경을 설정하기 위한 *conda.yml* 파일도 생성합니다.

이번 실습에서 할 일은 다음과 같습니다:

- 데이터셋을 다운로드하는 *download_dataset.py* 파일 생성
- Azure Machine Learning 환경을 설정하는 *setup_ml.py* 파일 생성
- *finetuning_dir* 폴더 내에 Phi-3 모델을 데이터셋으로 미세 조정하는 *fine_tune.py* 파일 생성
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

1. 메뉴 바에서 **File**을 선택합니다.

1. **Open Folder**를 선택합니다.

1. *C:\Users\yourUserName\finetune-phi* 경로에 생성한 *finetune-phi* 폴더를 선택합니다.

    ![프로젝트 폴더 열기](../../../../../../translated_images/01-12-open-project-folder.1fff9c7f41dd1639.ko.png)

1. Visual Studio Code 왼쪽 창에서 마우스 오른쪽 버튼을 클릭하고 **New File**을 선택하여 *download_dataset.py* 파일을 생성합니다.

1. 같은 방법으로 *setup_ml.py* 파일을 생성합니다.

1. 같은 방법으로 *deploy_model.py* 파일을 생성합니다.

    ![새 파일 생성](../../../../../../translated_images/01-13-create-new-file.c17c150fff384a39.ko.png)

1. 왼쪽 창에서 마우스 오른쪽 버튼을 클릭하고 **New Folder**를 선택하여 *finetuning_dir* 폴더를 생성합니다.

1. *finetuning_dir* 폴더 내에 *fine_tune.py* 파일을 생성합니다.

#### *conda.yml* 파일 생성 및 설정

1. Visual Studio Code 왼쪽 창에서 마우스 오른쪽 버튼을 클릭하고 **New File**을 선택하여 *conda.yml* 파일을 생성합니다.

1. *conda.yml* 파일에 다음 코드를 추가하여 Phi-3 모델 미세 조정 환경을 설정합니다.

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

#### *config.py* 파일 생성 및 설정

1. Visual Studio Code 왼쪽 창에서 마우스 오른쪽 버튼을 클릭하고 **New File**을 선택하여 *config.py* 파일을 생성합니다.

1. *config.py* 파일에 Azure 정보를 입력하기 위해 다음 코드를 추가합니다.

    ```python
    # Azure settings
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Azure Machine Learning settings
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Azure Managed Identity settings
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Dataset file paths
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Fine-tuned model settings
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### Azure 환경 변수 추가하기

1. Azure 구독 ID를 추가하려면 다음 작업을 수행하세요:

    - 포털 페이지 상단의 **검색창**에 *subscriptions*를 입력하고 나타나는 옵션 중 **Subscriptions**를 선택합니다.
    - 현재 사용 중인 Azure 구독을 선택합니다.
    - 구독 ID를 복사하여 *config.py* 파일에 붙여넣습니다.

    ![구독 ID 찾기](../../../../../../translated_images/01-14-find-subscriptionid.4f4ca33555f1e637.ko.png)

1. Azure 작업 영역 이름을 추가하려면 다음 작업을 수행하세요:

    - 생성한 Azure Machine Learning 리소스로 이동합니다.
    - 계정 이름을 복사하여 *config.py* 파일에 붙여넣습니다.

    ![Azure Machine Learning 이름 찾기](../../../../../../translated_images/01-15-find-AZML-name.1975f0422bca19a7.ko.png)

1. Azure 리소스 그룹 이름을 추가하려면 다음 작업을 수행하세요:

    - 생성한 Azure Machine Learning 리소스로 이동합니다.
    - Azure 리소스 그룹 이름을 복사하여 *config.py* 파일에 붙여넣습니다.

    ![리소스 그룹 이름 찾기](../../../../../../translated_images/01-16-find-AZML-resourcegroup.855a349d0af134a3.ko.png)

2. Azure 관리 ID 이름을 추가하려면 다음 작업을 수행하세요:

    - 생성한 Managed Identities 리소스로 이동합니다.
    - Azure 관리 ID 이름을 복사하여 *config.py* 파일에 붙여넣습니다.

    ![UAI 찾기](../../../../../../translated_images/01-17-find-uai.3529464f53499827.ko.png)

### 미세 조정을 위한 데이터셋 준비

이번 실습에서는 *download_dataset.py* 파일을 실행하여 *ULTRACHAT_200k* 데이터셋을 로컬 환경에 다운로드합니다. 이후 이 데이터셋을 사용해 Azure Machine Learning에서 Phi-3 모델을 미세 조정합니다.

#### *download_dataset.py* 파일로 데이터셋 다운로드하기

1. Visual Studio Code에서 *download_dataset.py* 파일을 엽니다.

1. *download_dataset.py* 파일에 다음 코드를 추가합니다.

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
        # Load the dataset with the specified name, configuration, and split ratio
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Split the dataset into train and test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open the file in write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterate over each record in the dataset
            for record in dataset:
                # Dump the record as a JSON object and write it to the file
                json.dump(record, f)
                # Write a newline character to separate records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load and split the ULTRACHAT_200k dataset with a specific configuration and split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract the train and test datasets from the split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save the train dataset to a JSONL file
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **CPU를 사용한 최소 데이터셋 미세 조정 가이드**
>
> CPU를 사용해 미세 조정하려는 경우, 이 방법은 Visual Studio Enterprise Subscription과 같은 혜택 구독자나 미세 조정 및 배포 과정을 빠르게 테스트하려는 분들에게 적합합니다.
>
> `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')`를 `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`로 변경하세요.
>

1. 터미널에서 다음 명령어를 입력하여 스크립트를 실행하고 데이터셋을 로컬 환경에 다운로드합니다.

    ```console
    python download_data.py
    ```

1. 데이터셋이 로컬 *finetune-phi/data* 디렉터리에 정상적으로 저장되었는지 확인합니다.

> [!NOTE]
>
> **데이터셋 크기와 미세 조정 시간**
>
> 이 E2E 샘플에서는 데이터셋의 1%(`train_sft[:1%]`)만 사용합니다. 이렇게 하면 데이터 양이 크게 줄어들어 업로드와 미세 조정 시간이 단축됩니다. 학습 시간과 모델 성능 간 적절한 균형을 위해 비율을 조절할 수 있습니다. 데이터셋의 작은 부분집합을 사용하면 미세 조정에 필요한 시간이 줄어들어 E2E 샘플에 적합합니다.

## 시나리오 2: Phi-3 모델 미세 조정 및 Azure Machine Learning Studio에 배포하기

### Azure CLI 설정하기

환경 인증을 위해 Azure CLI를 설정해야 합니다. Azure CLI는 명령줄에서 Azure 리소스를 관리할 수 있게 해주며, Azure Machine Learning이 리소스에 접근할 수 있도록 필요한 자격 증명을 제공합니다. 시작하려면 [Azure CLI 설치](https://learn.microsoft.com/cli/azure/install-azure-cli)를 참고하세요.

1. 터미널 창을 열고 다음 명령어를 입력하여 Azure 계정에 로그인합니다.

    ```console
    az login
    ```

1. 사용할 Azure 계정을 선택합니다.

1. 사용할 Azure 구독을 선택합니다.

    ![리소스 그룹 이름 찾기](../../../../../../translated_images/02-01-login-using-azure-cli.dfde31cb75e58a87.ko.png)

> [!TIP]
>
> Azure 로그인에 문제가 있을 경우, 디바이스 코드를 사용해 보세요. 터미널 창을 열고 다음 명령어를 입력하여 Azure 계정에 로그인할 수 있습니다:
>
> ```console
> az login --use-device-code
> ```
>

### Phi-3 모델 미세 조정하기

이번 실습에서는 제공된 데이터셋을 사용해 Phi-3 모델을 미세 조정합니다. 먼저 *fine_tune.py* 파일에서 미세 조정 과정을 정의합니다. 그 다음 *setup_ml.py* 파일을 실행해 Azure Machine Learning 환경을 구성하고 미세 조정 프로세스를 시작합니다. 이 스크립트는 미세 조정이 Azure Machine Learning 환경 내에서 실행되도록 합니다.

*setup_ml.py*를 실행하면 Azure Machine Learning 환경에서 미세 조정이 진행됩니다.

#### *fine_tune.py* 파일에 코드 추가하기

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

    # To avoid the INVALID_PARAMETER_VALUE error in MLflow, disable MLflow integration
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Logging setup
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
> *fine_tune.py* 파일에서 `pretrained_model_name`을 `"microsoft/Phi-3-mini-4k-instruct"`에서 원하는 모델 이름으로 변경할 수 있습니다. 예를 들어 `"microsoft/Phi-3.5-mini-instruct"`로 변경하면 Phi-3.5-mini-instruct 모델로 미세 조정합니다. 원하는 모델 이름을 찾으려면 [Hugging Face](https://huggingface.co/)에서 검색 후 이름을 복사하여 스크립트의 `pretrained_model_name` 필드에 붙여넣으세요.
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Phi-3.5 미세 조정":::
>

#### *setup_ml.py* 파일에 코드 추가하기

1. Visual Studio Code에서 *setup_ml.py* 파일을 엽니다.

1. *setup_ml.py* 파일에 다음 코드를 추가합니다.

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

    # Constants

    # Uncomment the following lines to use a CPU instance for training
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    FINETUNING_DIR = "./finetuning_dir" # Path to the fine-tuning script
    TRAINING_ENV_NAME = "phi-3-training-environment" # Name of the training environment
    MODEL_OUTPUT_DIR = "./model_output" # Path to the model output directory in azure ml

    # Logging setup to track the process
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
            image=DOCKER_IMAGE_NAME,  # Docker image for the environment
            conda_file=CONDA_FILE,  # Conda environment file
            name=TRAINING_ENV_NAME,  # Name of the environment
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
                tier="Dedicated",  # Tier of the compute cluster
                min_instances=0,  # Minimum number of instances
                max_instances=1  # Maximum number of instances
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Wait for the cluster to be created
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Path to fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Training environment
            compute=compute_name,  # Compute cluster to use
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Path to the training data file
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Path to the evaluation data file
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Initialize ML Client
        ml_client = get_ml_client()

        # Create Environment
        env = create_or_get_environment(ml_client)
        
        # Create or get existing compute cluster
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Create and Submit Fine-Tuning Job
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Submit the job
        ml_client.jobs.stream(returned_job.name)  # Stream the job logs
        
        # Capture the job name
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, `LOCATION`을 본인 환경에 맞게 변경합니다.

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **CPU를 사용한 최소 데이터셋 미세 조정 가이드**
>
> CPU를 사용해 미세 조정하려는 경우, 이 방법은 Visual Studio Enterprise Subscription과 같은 혜택 구독자나 미세 조정 및 배포 과정을 빠르게 테스트하려는 분들에게 적합합니다.
>
> 1. *setup_ml* 파일을 엽니다.
> 2. `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, `DOCKER_IMAGE_NAME`을 다음과 같이 변경하세요. *Standard_E16s_v3*에 접근 권한이 없으면 동등한 CPU 인스턴스를 사용하거나 새 쿼터를 요청할 수 있습니다.
> 3. `LOCATION`을 본인 환경에 맞게 변경하세요.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. 다음 명령어를 입력하여 *setup_ml.py* 스크립트를 실행하고 Azure Machine Learning에서 미세 조정 프로세스를 시작합니다.

    ```python
    python setup_ml.py
    ```

1. 이번 실습에서 Azure Machine Learning을 사용해 Phi-3 모델을 성공적으로 미세 조정했습니다. *setup_ml.py* 스크립트를 실행하면 Azure Machine Learning 환경이 설정되고 *fine_tune.py* 파일에 정의된 미세 조정 프로세스가 시작됩니다. 미세 조정은 상당한 시간이 소요될 수 있으니, `python setup_ml.py` 명령어 실행 후 완료될 때까지 기다리세요. 터미널에 표시된 링크를 통해 Azure Machine Learning 포털에서 미세 조정 작업 상태를 확인할 수 있습니다.

    ![미세 조정 작업 확인](../../../../../../translated_images/02-02-see-finetuning-job.59393bc3b143871e.ko.png)

### 미세 조정된 모델 배포하기

미세 조정된 Phi-3 모델을 Prompt Flow와 통합하려면, 실시간 추론이 가능하도록 모델을 배포해야 합니다. 이 과정은 모델 등록, 온라인 엔드포인트 생성, 모델 배포를 포함합니다.

#### 배포를 위한 모델 이름, 엔드포인트 이름, 배포 이름 설정하기

1. *config.py* 파일을 엽니다.

1. `AZURE_MODEL_NAME = "your_fine_tuned_model_name"`을 원하는 모델 이름으로 변경합니다.

1. `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"`을 원하는 엔드포인트 이름으로 변경합니다.

1. `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"`을 원하는 배포 이름으로 변경합니다.

#### *deploy_model.py* 파일에 코드 추가하기

*deploy_model.py* 파일을 실행하면 전체 배포 과정이 자동으로 진행됩니다. 이 스크립트는 모델을 등록하고, 엔드포인트를 생성하며, *config.py* 파일에 지정된 설정(모델 이름, 엔드포인트 이름, 배포 이름)을 기반으로 배포를 수행합니다.

1. Visual Studio Code에서 *deploy_model.py* 파일을 엽니다.

1. *deploy_model.py* 파일에 다음 코드를 추가합니다.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Configuration imports
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

    # Constants
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Logging setup
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
            # Fetch the current endpoint details
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Log the current traffic allocation for debugging
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Set the traffic allocation for the deployment
            endpoint.traffic = {deployment_name: 100}
            
            # Update the endpoint with the new traffic allocation
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Log the updated traffic allocation for debugging
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Log any errors that occur during the process
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

1. `JOB_NAME`을 확인하려면 다음 작업을 수행하세요:

    - 생성한 Azure Machine Learning 리소스로 이동합니다.
    - **Studio web URL**을 선택하여 Azure Machine Learning 작업 영역을 엽니다.
    - 왼쪽 탭에서 **Jobs**를 선택합니다.
    - 미세 조정 실험(예: *finetunephi*)을 선택합니다.
    - 생성한 작업을 선택합니다.
- *deploy_model.py* 파일의 `JOB_NAME = "your-job-name"`에 작업 이름을 복사하여 붙여넣으세요.

1. `COMPUTE_INSTANCE_TYPE`을 본인 환경에 맞게 변경하세요.

1. 다음 명령어를 입력하여 *deploy_model.py* 스크립트를 실행하고 Azure Machine Learning에서 배포를 시작하세요.

    ```python
    python deploy_model.py
    ```


> [!WARNING]
> 추가 요금이 발생하지 않도록 Azure Machine Learning 작업 영역에서 생성한 엔드포인트를 반드시 삭제하세요.
>

#### Azure Machine Learning 작업 영역에서 배포 상태 확인하기

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)에 접속하세요.

1. 생성한 Azure Machine Learning 작업 영역으로 이동하세요.

1. **Studio web URL**을 선택하여 Azure Machine Learning 작업 영역을 엽니다.

1. 왼쪽 탭에서 **Endpoints**를 선택하세요.

    ![Select endpoints.](../../../../../../translated_images/02-03-select-endpoints.c3136326510baff1.ko.png)

2. 생성한 엔드포인트를 선택하세요.

    ![Select endpoints that you created.](../../../../../../translated_images/02-04-select-endpoint-created.0363e7dca51dabb4.ko.png)

3. 이 페이지에서 배포 과정 중 생성된 엔드포인트를 관리할 수 있습니다.

## 시나리오 3: Prompt flow와 통합하여 맞춤형 모델과 대화하기

### 맞춤형 Phi-3 모델을 Prompt flow와 통합하기

파인튜닝한 모델을 성공적으로 배포한 후, Prompt flow와 통합하여 실시간 애플리케이션에서 모델을 활용할 수 있습니다. 이를 통해 맞춤형 Phi-3 모델로 다양한 인터랙티브 작업을 수행할 수 있습니다.

#### 파인튜닝한 Phi-3 모델의 API 키와 엔드포인트 URI 설정하기

1. 생성한 Azure Machine Learning 작업 영역으로 이동하세요.
1. 왼쪽 탭에서 **Endpoints**를 선택하세요.
1. 생성한 엔드포인트를 선택하세요.
1. 탐색 메뉴에서 **Consume**을 선택하세요.
1. **REST endpoint**를 복사하여 *config.py* 파일의 `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` 부분에 붙여넣으세요.
1. **Primary key**를 복사하여 *config.py* 파일의 `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` 부분에 붙여넣으세요.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/02-05-copy-apikey-endpoint.88b5a92e6462c53b.ko.png)

#### *flow.dag.yml* 파일에 코드 추가하기

1. Visual Studio Code에서 *flow.dag.yml* 파일을 엽니다.

1. 다음 코드를 *flow.dag.yml*에 추가하세요.

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

#### *integrate_with_promptflow.py* 파일에 코드 추가하기

1. Visual Studio Code에서 *integrate_with_promptflow.py* 파일을 엽니다.

1. 다음 코드를 *integrate_with_promptflow.py*에 추가하세요.

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

    # Logging setup
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

### 맞춤형 모델과 대화하기

1. 다음 명령어를 입력하여 *deploy_model.py* 스크립트를 실행하고 Azure Machine Learning에서 배포를 시작하세요.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. 결과 예시는 다음과 같습니다: 이제 맞춤형 Phi-3 모델과 대화할 수 있습니다. 파인튜닝에 사용한 데이터를 기반으로 질문하는 것을 권장합니다.

    ![Prompt flow example.](../../../../../../translated_images/02-06-promptflow-example.89384abaf3ad71f6.ko.png)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.