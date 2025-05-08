<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-08T05:47:30+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "ko"
}
-->
# Fine-tune 및 Azure AI Foundry의 Prompt flow와 맞춤 Phi-3 모델 통합하기

이 종단 간(E2E) 샘플은 Microsoft Tech Community의 "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" 가이드를 기반으로 합니다. 이 가이드는 Azure AI Foundry에서 Prompt flow와 함께 맞춤 Phi-3 모델을 미세 조정, 배포 및 통합하는 과정을 소개합니다. 로컬에서 코드를 실행하는 "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" E2E 샘플과 달리, 이 튜토리얼은 Azure AI / ML Studio 내에서 모델을 미세 조정하고 통합하는 데 집중합니다.

## 개요

이 E2E 샘플에서는 Phi-3 모델을 미세 조정하고 Azure AI Foundry의 Prompt flow와 통합하는 방법을 배웁니다. Azure AI / ML Studio를 활용하여 맞춤 AI 모델을 배포하고 활용하는 워크플로를 구축합니다. 이 E2E 샘플은 세 가지 시나리오로 나뉩니다:

**시나리오 1: Azure 리소스 설정 및 미세 조정 준비**

**시나리오 2: Phi-3 모델 미세 조정 및 Azure Machine Learning Studio에 배포**

**시나리오 3: Prompt flow와 통합하고 Azure AI Foundry에서 맞춤 모델과 채팅**

다음은 이 E2E 샘플의 개요입니다.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.ko.png)

### 목차

1. **[시나리오 1: Azure 리소스 설정 및 미세 조정 준비](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning 작업 영역 생성](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure 구독에서 GPU 할당량 요청](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [역할 할당 추가](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [프로젝트 설정](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [미세 조정용 데이터셋 준비](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[시나리오 2: Phi-3 모델 미세 조정 및 Azure Machine Learning Studio에 배포](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3 모델 미세 조정](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [미세 조정된 Phi-3 모델 배포](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[시나리오 3: Prompt flow와 통합하고 Azure AI Foundry에서 맞춤 모델과 채팅](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [맞춤 Phi-3 모델을 Prompt flow와 통합](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [맞춤 Phi-3 모델과 채팅](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## 시나리오 1: Azure 리소스 설정 및 미세 조정 준비

### Azure Machine Learning 작업 영역 생성

1. 포털 페이지 상단의 **검색창**에 *azure machine learning*을 입력하고 나타나는 옵션 중 **Azure Machine Learning**을 선택합니다.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.ko.png)

2. 탐색 메뉴에서 **+ 만들기**를 선택합니다.

3. 탐색 메뉴에서 **새 작업 영역**을 선택합니다.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.ko.png)

4. 다음 작업을 수행합니다:

    - Azure **구독**을 선택합니다.
    - 사용할 **리소스 그룹**을 선택합니다(필요 시 새로 만듭니다).
    - **작업 영역 이름**을 입력합니다. 고유해야 합니다.
    - 사용할 **지역**을 선택합니다.
    - 사용할 **스토리지 계정**을 선택합니다(필요 시 새로 만듭니다).
    - 사용할 **키 볼트**를 선택합니다(필요 시 새로 만듭니다).
    - 사용할 **애플리케이션 인사이트**를 선택합니다(필요 시 새로 만듭니다).
    - 사용할 **컨테이너 레지스트리**를 선택합니다(필요 시 새로 만듭니다).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.ko.png)

5. **검토 + 만들기**를 선택합니다.

6. **만들기**를 선택합니다.

### Azure 구독에서 GPU 할당량 요청

이 튜토리얼에서는 Phi-3 모델을 미세 조정하고 배포하기 위해 GPU를 사용합니다. 미세 조정에는 *Standard_NC24ads_A100_v4* GPU가 필요하며, 할당량 요청이 필요합니다. 배포에는 *Standard_NC6s_v3* GPU가 필요하며, 이 역시 할당량 요청이 필요합니다.

> [!NOTE]
>
> Pay-As-You-Go 구독(표준 구독 유형)만 GPU 할당 대상이며, 혜택 구독은 현재 지원되지 않습니다.
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)로 이동합니다.

1. *Standard NCADSA100v4 Family* 할당량을 요청하려면 다음 작업을 수행합니다:

    - 왼쪽 탭에서 **할당량**을 선택합니다.
    - 사용할 **가상 머신 패밀리**를 선택합니다. 예를 들어, *Standard_NC24ads_A100_v4* GPU가 포함된 **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**를 선택합니다.
    - 탐색 메뉴에서 **할당량 요청**을 선택합니다.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.ko.png)

    - 할당량 요청 페이지에서 원하는 **새 코어 제한**을 입력합니다. 예: 24
    - 할당량 요청 페이지에서 **제출**을 선택해 GPU 할당량을 요청합니다.

1. *Standard NCSv3 Family* 할당량을 요청하려면 다음 작업을 수행합니다:

    - 왼쪽 탭에서 **할당량**을 선택합니다.
    - 사용할 **가상 머신 패밀리**를 선택합니다. 예를 들어, *Standard_NC6s_v3* GPU가 포함된 **Standard NCSv3 Family Cluster Dedicated vCPUs**를 선택합니다.
    - 탐색 메뉴에서 **할당량 요청**을 선택합니다.
    - 할당량 요청 페이지에서 원하는 **새 코어 제한**을 입력합니다. 예: 24
    - 할당량 요청 페이지에서 **제출**을 선택해 GPU 할당량을 요청합니다.

### 역할 할당 추가

모델을 미세 조정하고 배포하려면 먼저 사용자 할당 관리 ID(User Assigned Managed Identity, UAI)를 생성하고 적절한 권한을 부여해야 합니다. 이 UAI는 배포 시 인증에 사용됩니다.

#### 사용자 할당 관리 ID(UAI) 생성

1. 포털 상단의 **검색창**에 *managed identities*를 입력하고 나타나는 옵션 중 **Managed Identities**를 선택합니다.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.ko.png)

1. **+ 만들기**를 선택합니다.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.ko.png)

1. 다음 작업을 수행합니다:

    - Azure **구독**을 선택합니다.
    - 사용할 **리소스 그룹**을 선택합니다(필요 시 새로 만듭니다).
    - 사용할 **지역**을 선택합니다.
    - **이름**을 입력합니다. 고유해야 합니다.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.ko.png)

1. **검토 + 만들기**를 선택합니다.

1. **+ 만들기**를 선택합니다.

#### Managed Identity에 Contributor 역할 할당 추가

1. 생성한 Managed Identity 리소스로 이동합니다.

1. 왼쪽 탭에서 **Azure 역할 할당**을 선택합니다.

1. 탐색 메뉴에서 **+ 역할 할당 추가**를 선택합니다.

1. 역할 할당 추가 페이지에서 다음 작업을 수행합니다:
    - **범위**를 **리소스 그룹**으로 설정합니다.
    - Azure **구독**을 선택합니다.
    - 사용할 **리소스 그룹**을 선택합니다.
    - **역할**을 **Contributor**로 선택합니다.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.ko.png)

2. **저장**을 선택합니다.

#### Managed Identity에 Storage Blob Data Reader 역할 할당 추가

1. 포털 상단의 **검색창**에 *storage accounts*를 입력하고 나타나는 옵션 중 **Storage accounts**를 선택합니다.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.ko.png)

1. 생성한 Azure Machine Learning 작업 영역과 연결된 스토리지 계정을 선택합니다. 예: *finetunephistorage*

1. 역할 할당 추가 페이지로 이동하기 위해 다음 작업을 수행합니다:

    - 생성한 Azure Storage 계정으로 이동합니다.
    - 왼쪽 탭에서 **액세스 제어 (IAM)**를 선택합니다.
    - 탐색 메뉴에서 **+ 추가**를 선택합니다.
    - **역할 할당 추가**를 선택합니다.

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.ko.png)

1. 역할 할당 추가 페이지에서 다음 작업을 수행합니다:

    - 역할 페이지의 **검색창**에 *Storage Blob Data Reader*를 입력하고 나타나는 옵션에서 **Storage Blob Data Reader**를 선택합니다.
    - 역할 페이지에서 **다음**을 선택합니다.
    - 구성원 페이지에서 **액세스 할당 대상**을 **Managed identity**로 선택합니다.
    - 구성원 페이지에서 **+ 구성원 선택**을 선택합니다.
    - 관리 ID 선택 페이지에서 Azure **구독**을 선택합니다.
    - 관리 ID 선택 페이지에서 **Managed identity**를 선택합니다.
    - 생성한 Managed Identity를 선택합니다. 예: *finetunephi-managedidentity*
    - 관리 ID 선택 페이지에서 **선택**을 클릭합니다.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.ko.png)

1. **검토 + 할당**을 선택합니다.

#### Managed Identity에 AcrPull 역할 할당 추가

1. 포털 상단의 **검색창**에 *container registries*를 입력하고 나타나는 옵션 중 **Container registries**를 선택합니다.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.ko.png)

1. Azure Machine Learning 작업 영역과 연결된 컨테이너 레지스트리를 선택합니다. 예: *finetunephicontainerregistry*

1. 역할 할당 추가 페이지로 이동하기 위해 다음 작업을 수행합니다:

    - 왼쪽 탭에서 **액세스 제어 (IAM)**를 선택합니다.
    - 탐색 메뉴에서 **+ 추가**를 선택합니다.
    - **역할 할당 추가**를 선택합니다.

1. 역할 할당 추가 페이지에서 다음 작업을 수행합니다:

    - 역할 페이지의 **검색창**에 *AcrPull*을 입력하고 나타나는 옵션에서 **AcrPull**을 선택합니다.
    - 역할 페이지에서 **다음**을 선택합니다.
    - 구성원 페이지에서 **액세스 할당 대상**을 **Managed identity**로 선택합니다.
    - 구성원 페이지에서 **+ 구성원 선택**을 선택합니다.
    - 관리 ID 선택 페이지에서 Azure **구독**을 선택합니다.
    - 관리 ID 선택 페이지에서 **Managed identity**를 선택합니다.
    - 생성한 Managed Identity를 선택합니다. 예: *finetunephi-managedidentity*
    - 관리 ID 선택 페이지에서 **선택**을 클릭합니다.
    - **검토 + 할당**을 선택합니다.

### 프로젝트 설정

미세 조정에 필요한 데이터셋을 다운로드하기 위해 로컬 환경을 설정합니다.

이 연습에서는

- 작업할 폴더를 생성합니다.
- 가상 환경을 생성합니다.
- 필요한 패키지를 설치합니다.
- 데이터셋 다운로드용 *download_dataset.py* 파일을 생성합니다.

#### 작업할 폴더 생성

1. 터미널 창을 열고 기본 경로에 *finetune-phi*라는 이름의 폴더를 생성하려면 다음 명령어를 입력합니다.

    ```console
    mkdir finetune-phi
    ```

2. 터미널에서 다음 명령어를 입력하여 생성한 *finetune-phi* 폴더로 이동합니다.

    ```console
    cd finetune-phi
    ```

#### 가상 환경 생성

1. 터미널에서 다음 명령어를 입력하여 *.venv*라는 이름의 가상 환경을 생성합니다.

    ```console
    python -m venv .venv
    ```

2. 터미널에서 다음 명령어를 입력하여 가상 환경을 활성화합니다.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> 성공적으로 활성화되면 명령 프롬프트 앞에 *(.venv)*가 표시됩니다.

#### 필요한 패키지 설치

1. 터미널에서 다음 명령어를 입력하여 필요한 패키지를 설치합니다.

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py` 생성

> [!NOTE]
> 완성된 폴더 구조:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code**를 엽니다.

1. 메뉴 바에서 **파일**을 선택합니다.

1. **폴더 열기**를 선택합니다.

1. *C:\Users\yourUserName\finetune-phi*에 위치한 생성한 *finetune-phi* 폴더를 선택합니다.

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.ko.png)

1. Visual Studio Code 왼쪽 창에서 우클릭 후 **새 파일**을 선택하여 *download_dataset.py* 파일을 생성합니다.

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.ko.png)

### 미세 조정용 데이터셋 준비

이 연습에서는 *download_dataset.py* 파일을 실행해 *ultrachat_200k* 데이터셋을 로컬 환경에 다운로드합니다. 이후 이 데이터셋을 사용해 Azure Machine Learning에서 Phi-3 모델을 미세 조정합니다.

이 연습에서는:

- *download_dataset.py* 파일에 데이터셋 다운로드 코드를 추가합니다.
- *download_dataset.py* 파일을 실행해 데이터셋을 로컬 환경에 다운로드합니다.

#### *download_dataset.py*를 사용해 데이터셋 다운로드

1. Visual Studio Code에서 *download_dataset.py* 파일을 엽니다.

1. *download_dataset.py* 파일에 다음 코드를 추가합니다.

    ```python
    import json
    import os
    from datasets import load_dataset

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
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. 터미널에서 다음 명령어를 입력해 스크립트를 실행하고 데이터셋을 로컬 환경에 다운로드합니다.

    ```console
    python download_dataset.py
    ```

1. 데이터셋이 로컬 *finetune-phi/data* 디렉터리에 성공적으로 저장되었는지 확인합니다.

> [!NOTE]
>
> #### 데이터셋 크기 및 미세 조정 시간 관련 참고
>
> 이 튜토리얼에서는 데이터셋의 1%(`split='train[:1%]'`)만 사용합니다. 이는 데이터 양을 크게 줄여 업로드 및 미세 조정 속도를 높입니다. 학습 시간과 모델 성능 간 적절한 균형을 위해 비율을 조정할 수 있습니다. 데이터셋의 작은 부분집합 사용은 미세 조정 시간을 단축해 튜토리얼 진행을 용이하게 만듭니다.

## 시나리오 2: Phi-3 모델 미세 조정 및 Azure Machine Learning Studio에 배포

### Phi-3 모델 미세 조정

이 연습에서는 Azure Machine Learning Studio에서 Phi-3 모델을 미세 조정합니다.

이 연습에서는:

- 미세 조정을 위한 컴퓨터 클러스터 생성
- Azure Machine Learning Studio에서 Phi-3 모델 미세 조정

#### 미세 조정을 위한 컴퓨터 클러스터 생성
1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)에 방문합니다.

1. 왼쪽 탭에서 **Compute**를 선택합니다.

1. 탐색 메뉴에서 **Compute clusters**를 선택합니다.

1. **+ New**를 선택합니다.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.ko.png)

1. 다음 작업을 수행합니다:

    - 사용하려는 **Region**을 선택합니다.
    - **Virtual machine tier**를 **Dedicated**로 선택합니다.
    - **Virtual machine type**을 **GPU**로 선택합니다.
    - **Virtual machine size** 필터를 **Select from all options**로 설정합니다.
    - **Virtual machine size**를 **Standard_NC24ads_A100_v4**로 선택합니다.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.ko.png)

1. **Next**를 선택합니다.

1. 다음 작업을 수행합니다:

    - **Compute name**을 입력합니다. 고유한 값이어야 합니다.
    - **Minimum number of nodes**를 **0**으로 설정합니다.
    - **Maximum number of nodes**를 **1**로 설정합니다.
    - **Idle seconds before scale down**을 **120**으로 설정합니다.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.ko.png)

1. **Create**를 선택합니다.

#### Phi-3 모델 미세 조정하기

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)에 방문합니다.

1. 생성한 Azure Machine Learning 작업 영역을 선택합니다.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.ko.png)

1. 다음 작업을 수행합니다:

    - 왼쪽 탭에서 **Model catalog**를 선택합니다.
    - **검색창**에 *phi-3-mini-4k*를 입력하고 나타나는 옵션 중 **Phi-3-mini-4k-instruct**를 선택합니다.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.ko.png)

1. 탐색 메뉴에서 **Fine-tune**를 선택합니다.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.ko.png)

1. 다음 작업을 수행합니다:

    - **Select task type**을 **Chat completion**으로 선택합니다.
    - **+ Select data**를 선택하여 **Training data**를 업로드합니다.
    - 검증 데이터 업로드 유형을 **Provide different validation data**로 선택합니다.
    - **+ Select data**를 선택하여 **Validation data**를 업로드합니다.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.ko.png)

    > [!TIP]
    >
    > **Advanced settings**를 선택하면 **learning_rate**나 **lr_scheduler_type** 같은 설정을 조정하여 미세 조정 과정을 최적화할 수 있습니다.

1. **Finish**를 선택합니다.

1. 이번 실습에서는 Azure Machine Learning을 사용해 Phi-3 모델을 성공적으로 미세 조정했습니다. 미세 조정 작업은 시간이 꽤 걸릴 수 있으니, 작업이 완료될 때까지 기다려야 합니다. 작업 상태는 Azure Machine Learning 작업 영역 왼쪽의 Jobs 탭에서 확인할 수 있습니다. 다음 시리즈에서는 미세 조정된 모델을 배포하고 Prompt flow와 통합할 예정입니다.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.ko.png)

### 미세 조정된 Phi-3 모델 배포하기

미세 조정된 Phi-3 모델을 Prompt flow와 통합하려면, 실시간 추론에 사용할 수 있도록 모델을 배포해야 합니다. 이 과정은 모델 등록, 온라인 엔드포인트 생성, 모델 배포를 포함합니다.

이번 실습에서는 다음을 수행합니다:

- Azure Machine Learning 작업 영역에 미세 조정된 모델 등록하기
- 온라인 엔드포인트 생성하기
- 등록된 미세 조정 Phi-3 모델 배포하기

#### 미세 조정된 모델 등록하기

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)에 방문합니다.

1. 생성한 Azure Machine Learning 작업 영역을 선택합니다.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.ko.png)

1. 왼쪽 탭에서 **Models**를 선택합니다.
1. **+ Register**를 선택합니다.
1. **From a job output**를 선택합니다.

    ![Register model.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.ko.png)

1. 생성한 작업을 선택합니다.

    ![Select job.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.ko.png)

1. **Next**를 선택합니다.

1. **Model type**을 **MLflow**로 선택합니다.

1. **Job output**이 자동으로 선택되어 있는지 확인합니다.

    ![Select output.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.ko.png)

2. **Next**를 선택합니다.

3. **Register**를 선택합니다.

    ![Select register.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.ko.png)

4. 등록된 모델은 왼쪽 탭의 **Models** 메뉴에서 확인할 수 있습니다.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.ko.png)

#### 미세 조정된 모델 배포하기

1. 생성한 Azure Machine Learning 작업 영역으로 이동합니다.

1. 왼쪽 탭에서 **Endpoints**를 선택합니다.

1. 탐색 메뉴에서 **Real-time endpoints**를 선택합니다.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.ko.png)

1. **Create**를 선택합니다.

1. 생성한 등록된 모델을 선택합니다.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.ko.png)

1. **Select**를 선택합니다.

1. 다음 작업을 수행합니다:

    - **Virtual machine**을 *Standard_NC6s_v3*로 선택합니다.
    - 사용할 **Instance count**를 선택합니다. 예: *1*.
    - **Endpoint**를 **New**로 선택하여 새 엔드포인트를 만듭니다.
    - **Endpoint name**을 입력합니다. 고유한 값이어야 합니다.
    - **Deployment name**을 입력합니다. 고유한 값이어야 합니다.

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.ko.png)

1. **Deploy**를 선택합니다.

> [!WARNING]
> 추가 요금이 발생하지 않도록, Azure Machine Learning 작업 영역에서 생성한 엔드포인트를 사용하지 않을 경우 반드시 삭제하세요.
>

#### Azure Machine Learning 작업 영역에서 배포 상태 확인하기

1. 생성한 Azure Machine Learning 작업 영역으로 이동합니다.

1. 왼쪽 탭에서 **Endpoints**를 선택합니다.

1. 생성한 엔드포인트를 선택합니다.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.ko.png)

1. 이 페이지에서 배포 과정 중 엔드포인트를 관리할 수 있습니다.

> [!NOTE]
> 배포가 완료되면 **Live traffic**이 **100%**로 설정되어 있는지 확인하세요. 그렇지 않으면 **Update traffic**을 선택해 트래픽 설정을 조정할 수 있습니다. 트래픽이 0%로 설정되어 있으면 모델 테스트가 불가능합니다.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.ko.png)
>

## 시나리오 3: Prompt flow와 통합하고 Azure AI Foundry에서 맞춤 모델로 채팅하기

### 맞춤 Phi-3 모델을 Prompt flow와 통합하기

미세 조정한 모델을 성공적으로 배포한 후, Prompt Flow와 통합하여 실시간 애플리케이션에서 맞춤 Phi-3 모델을 활용할 수 있습니다. 이를 통해 다양한 인터랙티브 작업이 가능합니다.

이번 실습에서는 다음을 수행합니다:

- Azure AI Foundry Hub 생성
- Azure AI Foundry 프로젝트 생성
- Prompt flow 생성
- 미세 조정된 Phi-3 모델을 위한 맞춤 연결 추가
- 맞춤 Phi-3 모델과 채팅할 수 있도록 Prompt flow 설정

> [!NOTE]
> Azure ML Studio를 사용해 Promptflow와 통합할 수도 있습니다. 동일한 통합 절차가 Azure ML Studio에도 적용됩니다.

#### Azure AI Foundry Hub 생성

프로젝트를 만들기 전에 Hub를 생성해야 합니다. Hub는 리소스 그룹처럼 여러 프로젝트를 조직하고 관리하는 역할을 합니다.

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)에 방문합니다.

1. 왼쪽 탭에서 **All hubs**를 선택합니다.

1. 탐색 메뉴에서 **+ New hub**를 선택합니다.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.ko.png)

1. 다음 작업을 수행합니다:

    - **Hub name**을 입력합니다. 고유한 값이어야 합니다.
    - Azure **Subscription**을 선택합니다.
    - 사용할 **Resource group**을 선택합니다(필요 시 새로 생성).
    - 사용할 **Location**을 선택합니다.
    - 사용할 **Connect Azure AI Services**를 선택합니다(필요 시 새로 생성).
    - **Connect Azure AI Search**는 **Skip connecting**으로 선택합니다.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.ko.png)

1. **Next**를 선택합니다.

#### Azure AI Foundry 프로젝트 생성

1. 생성한 Hub에서 왼쪽 탭의 **All projects**를 선택합니다.

1. 탐색 메뉴에서 **+ New project**를 선택합니다.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.ko.png)

1. **Project name**을 입력합니다. 고유한 값이어야 합니다.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.ko.png)

1. **Create a project**를 선택합니다.

#### 미세 조정된 Phi-3 모델을 위한 맞춤 연결 추가

맞춤 Phi-3 모델을 Prompt flow와 통합하려면, 모델의 엔드포인트와 키를 맞춤 연결에 저장해야 합니다. 이렇게 하면 Prompt flow에서 맞춤 모델에 접근할 수 있습니다.

#### 미세 조정된 Phi-3 모델의 api key와 endpoint uri 설정하기

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo)에 방문합니다.

1. 생성한 Azure Machine Learning 작업 영역으로 이동합니다.

1. 왼쪽 탭에서 **Endpoints**를 선택합니다.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.ko.png)

1. 생성한 엔드포인트를 선택합니다.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.ko.png)

1. 탐색 메뉴에서 **Consume**을 선택합니다.

1. **REST endpoint**와 **Primary key**를 복사합니다.
![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.ko.png)

#### 사용자 지정 연결 추가

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)에 접속합니다.

1. 생성한 Azure AI Foundry 프로젝트로 이동합니다.

1. 생성한 프로젝트에서 왼쪽 탭의 **Settings**를 선택합니다.

1. **+ New connection**을 선택합니다.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.ko.png)

1. 탐색 메뉴에서 **Custom keys**를 선택합니다.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.ko.png)

1. 다음 작업을 수행합니다:

    - **+ Add key value pairs**를 선택합니다.
    - 키 이름에 **endpoint**를 입력하고 Azure ML Studio에서 복사한 endpoint를 값 필드에 붙여넣습니다.
    - 다시 **+ Add key value pairs**를 선택합니다.
    - 키 이름에 **key**를 입력하고 Azure ML Studio에서 복사한 키를 값 필드에 붙여넣습니다.
    - 키를 추가한 후, 키가 노출되지 않도록 **is secret**을 선택합니다.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.ko.png)

1. **Add connection**을 선택합니다.

#### Prompt flow 생성

Azure AI Foundry에 사용자 지정 연결을 추가했습니다. 이제 다음 단계를 따라 Prompt flow를 생성해 보겠습니다. 이후 이 Prompt flow를 사용자 지정 연결과 연결하여 fine-tuned 모델을 Prompt flow 내에서 사용할 수 있습니다.

1. 생성한 Azure AI Foundry 프로젝트로 이동합니다.

1. 왼쪽 탭에서 **Prompt flow**를 선택합니다.

1. 탐색 메뉴에서 **+ Create**를 선택합니다.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.ko.png)

1. 탐색 메뉴에서 **Chat flow**를 선택합니다.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.ko.png)

1. 사용할 **Folder name**을 입력합니다.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.ko.png)

2. **Create**를 선택합니다.

#### 사용자 지정 Phi-3 모델과 채팅할 수 있도록 Prompt flow 설정하기

fine-tuned Phi-3 모델을 Prompt flow에 통합해야 합니다. 하지만 기본 제공되는 Prompt flow는 이를 위한 설계가 되어 있지 않으므로, 사용자 지정 모델을 통합할 수 있도록 Prompt flow를 재설계해야 합니다.

1. Prompt flow에서 기존 플로우를 다시 구성하기 위해 다음 작업을 수행합니다:

    - **Raw file mode**를 선택합니다.
    - *flow.dag.yml* 파일 내 기존 코드를 모두 삭제합니다.
    - *flow.dag.yml* 파일에 다음 코드를 추가합니다.

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

    - **Save**를 선택합니다.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.ko.png)

1. Prompt flow에서 사용자 지정 Phi-3 모델을 사용하기 위해 *integrate_with_promptflow.py* 파일에 다음 코드를 추가합니다.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
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
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.ko.png)

> [!NOTE]
> Azure AI Foundry에서 Prompt flow 사용에 관한 자세한 내용은 [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)를 참고하세요.

1. 모델과 채팅할 수 있도록 **Chat input**, **Chat output**을 선택합니다.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.ko.png)

1. 이제 사용자 지정 Phi-3 모델과 채팅할 준비가 되었습니다. 다음 실습에서는 Prompt flow를 시작하고 fine-tuned Phi-3 모델과 채팅하는 방법을 배웁니다.

> [!NOTE]
>
> 재구성된 플로우는 아래 이미지와 유사해야 합니다:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.ko.png)
>

### 사용자 지정 Phi-3 모델과 채팅하기

fine-tuned한 사용자 지정 Phi-3 모델을 Prompt flow와 통합했으니 이제 상호작용을 시작할 수 있습니다. 이 실습에서는 Prompt flow를 사용해 모델과 채팅을 설정하고 시작하는 과정을 안내합니다. 이 단계를 따라 하면 fine-tuned Phi-3 모델의 다양한 작업과 대화 기능을 최대한 활용할 수 있습니다.

- Prompt flow를 사용해 사용자 지정 Phi-3 모델과 채팅합니다.

#### Prompt flow 시작하기

1. **Start compute sessions**를 선택해 Prompt flow를 시작합니다.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.ko.png)

1. **Validate and parse input**을 선택해 파라미터를 갱신합니다.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.ko.png)

1. 생성한 사용자 지정 연결의 **connection** 값을 선택합니다. 예: *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.ko.png)

#### 사용자 지정 모델과 채팅하기

1. **Chat**을 선택합니다.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.ko.png)

1. 결과 예시는 다음과 같습니다: 이제 사용자 지정 Phi-3 모델과 채팅할 수 있습니다. fine-tuning에 사용된 데이터를 기반으로 질문하는 것을 권장합니다.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.ko.png)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.