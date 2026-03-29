# Microsoft Foundry에서 Prompt flow와 함께 맞춤 Phi-3 모델 미세 조정 및 통합

이 종단 간(E2E) 샘플은 Microsoft Tech Community의 가이드 "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)"를 기반으로 합니다. 이 가이드는 Microsoft Foundry에서 Prompt flow와 함께 맞춤 Phi-3 모델을 미세 조정, 배포 및 통합하는 프로세스를 소개합니다.
"[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" E2E 샘플과 달리, 해당 샘플은 로컬에서 코드를 실행하는 반면, 이 튜토리얼은 Azure AI / ML Studio 내에서 모델을 미세 조정하고 통합하는 데 중점을 둡니다.

## 개요

이 E2E 샘플에서는 Phi-3 모델을 미세 조정하고 Microsoft Foundry에서 Prompt flow와 통합하는 방법을 배웁니다. Azure AI / ML Studio를 활용하여 맞춤 AI 모델을 배포하고 활용하는 워크플로우를 구축합니다. 이 E2E 샘플은 세 가지 시나리오로 나누어집니다:

**시나리오 1: Azure 리소스 설정 및 미세 조정 준비**

**시나리오 2: Phi-3 모델 미세 조정 및 Azure Machine Learning Studio에서 배포**

**시나리오 3: Prompt flow와 통합 및 Microsoft Foundry에서 맞춤 모델과 채팅**

다음은 이 E2E 샘플의 개요입니다.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/ko/00-01-architecture.198ba0f1ae6d841a.webp)

### 목차

1. **[시나리오 1: Azure 리소스 설정 및 미세 조정 준비](#시나리오-1-azure-리소스-설정-및-미세-조정-준비)**
    - [Azure Machine Learning 작업 영역 만들기](#azure-machine-learning-작업-영역-만들기)
    - [Azure 구독에서 GPU 할당량 요청](#azure-구독에서-gpu-할당량-요청)
    - [역할 할당 추가](#역할-할당-추가)
    - [프로젝트 설정](#프로젝트-설정)
    - [미세 조정용 데이터세트 준비](#파인튜닝용-데이터셋-준비하기)

1. **[시나리오 2: Phi-3 모델 미세 조정 및 Azure Machine Learning Studio에 배포](#시나리오-2-phi-3-모델-파인튜닝-및-azure-machine-learning-studio에-배포)**
    - [Phi-3 모델 미세 조정](#phi-3-모델-파인튜닝하기)
    - [미세 조정된 Phi-3 모델 배포](#파인튜닝된-phi-3-모델-배포하기)

1. **[시나리오 3: Prompt flow와 통합 및 Microsoft Foundry에서 맞춤 모델과 채팅](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [맞춤 Phi-3 모델을 Prompt flow와 통합](#맞춤형-phi-3-모델을-prompt-flow와-통합하기)
    - [맞춤 Phi-3 모델로 채팅](#사용자-지정-phi-3-모델과-대화하기)

## 시나리오 1: Azure 리소스 설정 및 미세 조정 준비

### Azure Machine Learning 작업 영역 만들기

1. 포털 페이지 상단의 <strong>검색 창</strong>에 <em>azure machine learning</em>을 입력하고 나타나는 옵션에서 <strong>Azure Machine Learning</strong>을 선택합니다.

    ![Type azure machine learning.](../../../../../../translated_images/ko/01-01-type-azml.acae6c5455e67b4b.webp)

2. 탐색 메뉴에서 <strong>+ 만들기</strong>를 선택합니다.

3. 탐색 메뉴에서 <strong>새 작업 영역</strong>을 선택합니다.

    ![Select new workspace.](../../../../../../translated_images/ko/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. 다음 작업을 수행합니다:

    - Azure <strong>구독</strong> 선택.
    - 사용할 **리소스 그룹** 선택 (필요시 새로 생성).
    - **작업 영역 이름** 입력. 고유한 값이어야 합니다.
    - 사용할 <strong>지역</strong> 선택.
    - 사용할 **저장소 계정** 선택 (필요시 새로 생성).
    - 사용할 **키 자격증명(Key vault)** 선택 (필요시 새로 생성).
    - 사용할 **애플리케이션 인사이트** 선택 (필요시 새로 생성).
    - 사용할 **컨테이너 레지스트리** 선택 (필요시 새로 생성).

    ![Fill azure machine learning.](../../../../../../translated_images/ko/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. <strong>검토 + 만들기</strong>를 선택합니다.

6. <strong>만들기</strong>를 선택합니다.

### Azure 구독에서 GPU 할당량 요청

이 튜토리얼에서는 GPU를 사용하여 Phi-3 모델을 미세 조정하고 배포하는 방법을 배웁니다. 미세 조정에는 *Standard_NC24ads_A100_v4* GPU를 사용하며, 할당량 요청이 필요합니다. 배포에는 *Standard_NC6s_v3* GPU를 사용하며 역시 할당량 요청이 필요합니다.

> [!NOTE]
>
> Pay-As-You-Go 구독(표준 구독 유형)만 GPU 할당 대상이며, 혜택 구독은 현재 지원되지 않습니다.
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)를 방문합니다.

1. *Standard NCADSA100v4 Family* 할당량을 요청하는 절차:

    - 왼쪽 탭에서 <strong>할당량</strong> 선택.
    - 사용할 **가상 머신 패밀리** 선택. 예: *Standard NCADSA100v4 Family Cluster Dedicated vCPUs* (여기에 *Standard_NC24ads_A100_v4* GPU 포함).
    - 탐색 메뉴에서 **할당량 요청** 선택.

        ![Request quota.](../../../../../../translated_images/ko/02-02-request-quota.c0428239a63ffdd5.webp)

    - 할당량 요청 페이지에서 원하는 **새 코어 제한** 입력. 예: 24.
    - <strong>제출</strong> 선택하여 GPU 할당량 요청.

1. *Standard NCSv3 Family* 할당량을 요청하는 절차:

    - 왼쪽 탭에서 <strong>할당량</strong> 선택.
    - 사용할 **가상 머신 패밀리** 선택. 예: *Standard NCSv3 Family Cluster Dedicated vCPUs* (여기에 *Standard_NC6s_v3* GPU 포함).
    - 탐색 메뉴에서 **할당량 요청** 선택.
    - 할당량 요청 페이지에서 원하는 **새 코어 제한** 입력. 예: 24.
    - <strong>제출</strong> 선택하여 GPU 할당량 요청.

### 역할 할당 추가

모델을 미세 조정하고 배포하려면, 먼저 사용자 할당 관리 ID(User Assigned Managed Identity, UAI)를 만들고 적절한 권한을 부여해야 합니다. 이 UAI는 배포 시 인증에 사용됩니다.

#### 사용자 할당 관리 ID(UAI) 만들기

1. 포털 페이지 상단 검색 창에 <em>managed identities</em>를 입력하고 나타나는 옵션에서 <strong>Managed Identities</strong>를 선택합니다.

    ![Type managed identities.](../../../../../../translated_images/ko/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. <strong>+ 만들기</strong>를 선택합니다.

    ![Select create.](../../../../../../translated_images/ko/03-02-select-create.92bf8989a5cd98f2.webp)

1. 다음 작업을 수행합니다:

    - Azure <strong>구독</strong> 선택.
    - 사용할 **리소스 그룹** 선택 (필요시 새로 생성).
    - 사용할 <strong>지역</strong> 선택.
    - <strong>이름</strong> 입력. 고유한 값이어야 합니다.

    ![Select create.](../../../../../../translated_images/ko/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. <strong>검토 + 만들기</strong>를 선택합니다.

1. <strong>+ 만들기</strong>를 선택합니다.

#### Managed Identity에 Contributor 역할 할당 추가

1. 만든 Managed Identity 리소스로 이동합니다.

1. 왼쪽 탭에서 **Azure 역할 할당** 선택.

1. 탐색 메뉴에서 **+ 역할 할당 추가** 선택.

1. 역할 할당 추가 페이지에서 다음 작업 수행:
    - <strong>범위</strong>를 <strong>리소스 그룹</strong>으로 선택.
    - Azure <strong>구독</strong> 선택.
    - 사용할 **리소스 그룹** 선택.
    - <strong>역할</strong>을 <strong>Contributor</strong>로 선택.

    ![Fill contributor role.](../../../../../../translated_images/ko/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. <strong>저장</strong>을 선택합니다.

#### Managed Identity에 Storage Blob Data Reader 역할 할당 추가

1. 포털 페이지 상단 검색 창에 <em>storage accounts</em>를 입력하고 나타나는 옵션에서 <strong>Storage accounts</strong>를 선택합니다.

    ![Type storage accounts.](../../../../../../translated_images/ko/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. 만든 Azure Machine Learning 작업 영역과 연관된 저장소 계정 선택. 예: *finetunephistorage*.

1. 역할 할당 추가 페이지로 이동하기 위한 절차:

    - 만든 Azure Storage 계정으로 이동.
    - 왼쪽 탭에서 **액세스 제어 (IAM)** 선택.
    - 탐색 메뉴에서 **+ 추가** 선택.
    - **역할 할당 추가** 선택.

    ![Add role.](../../../../../../translated_images/ko/03-06-add-role.353ccbfdcf0789c2.webp)

1. 역할 할당 추가 페이지에서 다음 작업 수행:

    - 역할 페이지에서 검색 창에 *Storage Blob Data Reader* 입력 후 해당 역할 선택.
    - <strong>다음</strong> 선택.
    - 멤버 페이지에서 <strong>액세스 할당 대상</strong>을 <strong>Managed identity</strong>로 선택.
    - **+ 구성원 선택** 선택.
    - 관리 ID 선택 페이지에서 Azure <strong>구독</strong> 선택.
    - 관리 ID 선택 페이지에서 <strong>Managed identity</strong>를 선택.
    - 관리 ID 선택 페이지에서 만든 Managed Identity 선택. 예: *finetunephi-managedidentity*.
    - <strong>선택</strong> 선택.

    ![Select managed identity.](../../../../../../translated_images/ko/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. **검토 + 할당** 선택.

#### Managed Identity에 AcrPull 역할 할당 추가

1. 포털 페이지 상단 검색 창에 <em>container registries</em>를 입력하고 나타나는 옵션에서 <strong>Container registries</strong>를 선택합니다.

    ![Type container registries.](../../../../../../translated_images/ko/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Azure Machine Learning 작업 영역과 연관된 컨테이너 레지스트리 선택. 예: *finetunephicontainerregistry*

1. 역할 할당 추가 페이지로 이동하기 위한 절차:

    - 왼쪽 탭에서 **액세스 제어 (IAM)** 선택.
    - 탐색 메뉴에서 **+ 추가** 선택.
    - **역할 할당 추가** 선택.

1. 역할 할당 추가 페이지에서 다음 작업 수행:

    - 역할 페이지의 검색창에 *AcrPull* 입력 후 해당 역할 선택.
    - <strong>다음</strong> 선택.
    - 멤버 페이지에서 <strong>액세스 할당 대상</strong>을 <strong>Managed identity</strong>로 선택.
    - **+ 구성원 선택** 선택.
    - 관리 ID 선택 페이지에서 Azure <strong>구독</strong> 선택.
    - 관리 ID 선택 페이지에서 **Managed identity** 선택.
    - 관리 ID 선택 페이지에서 만든 Managed Identity 선택. 예: *finetunephi-managedidentity*.
    - <strong>선택</strong> 선택.
    - **검토 + 할당** 선택.

### 프로젝트 설정

미세 조정에 필요한 데이터세트를 다운로드하기 위해 로컬 환경을 설정합니다.

이 연습에서는

- 작업할 폴더 생성.
- 가상 환경 생성.
- 필수 패키지 설치.
- 데이터세트를 다운로드하는 *download_dataset.py* 파일 생성.

#### 작업할 폴더 생성

1. 터미널 창을 열고 기본 경로에 <em>finetune-phi</em>라는 이름의 폴더를 생성하는 다음 명령어를 입력합니다.

    ```console
    mkdir finetune-phi
    ```

2. 터미널에서 다음 명령어를 입력하여 생성한 *finetune-phi* 폴더로 이동합니다.

    ```console
    cd finetune-phi
    ```

#### 가상 환경 생성

1. 터미널에서 다음 명령어를 입력하여 <em>.venv</em>라는 이름의 가상 환경을 생성합니다.
    ```console
    python -m venv .venv
    ```

2. 가상 환경을 활성화하려면 터미널에서 다음 명령어를 입력하세요.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> 성공했다면 명령 프롬프트 앞에 *(.venv)* 가 표시될 것입니다.

#### 필요한 패키지 설치

1. 필요한 패키지를 설치하려면 터미널에서 다음 명령어들을 입력하세요.

    ```console
    pip install datasets==2.19.1
    ```

#### `donload_dataset.py` 생성하기

> [!NOTE]
> 전체 폴더 구조:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. <strong>Visual Studio Code</strong>를 엽니다.

1. 메뉴 바에서 **파일(File)** 을 선택합니다.

1. **폴더 열기(Open Folder)** 를 선택합니다.

1. *C:\Users\yourUserName\finetune-phi* 경로에 생성한 *finetune-phi* 폴더를 선택합니다.

    ![Select the folder that you created.](../../../../../../translated_images/ko/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Visual Studio Code의 왼쪽 창에서 마우스 오른쪽 버튼을 클릭하고 **새 파일(New File)** 을 선택하여 *download_dataset.py* 라는 새 파일을 만듭니다.

    ![Create a new file.](../../../../../../translated_images/ko/04-02-create-new-file.cf9a330a3a9cff92.webp)

### 파인튜닝용 데이터셋 준비하기

이번 실습에서는 *download_dataset.py* 파일을 실행하여 *ultrachat_200k* 데이터셋을 로컬 환경에 다운로드합니다. 그런 다음 이 데이터셋을 사용해 Azure Machine Learning에서 Phi-3 모델을 파인튜닝합니다.

이 실습에서는 다음 작업들을 수행합니다:

- *download_dataset.py* 파일에 데이터셋 다운로드 코드를 추가합니다.
- *download_dataset.py* 파일을 실행하여 데이터셋을 로컬 환경에 다운로드합니다.

#### <em>download_dataset.py</em>를 사용해 데이터셋 다운로드하기

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
        # 지정된 이름, 구성 및 분할 비율로 데이터셋을 로드합니다
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # 데이터셋을 학습 세트와 테스트 세트로 분할합니다 (80% 학습, 20% 테스트)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # 디렉토리가 없으면 생성합니다
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # 파일을 쓰기 모드로 엽니다
        with open(filepath, 'w', encoding='utf-8') as f:
            # 데이터셋의 각 레코드를 반복 처리합니다
            for record in dataset:
                # 레코드를 JSON 객체로 덤프하여 파일에 기록합니다
                json.dump(record, f)
                # 레코드를 구분하기 위해 줄 바꿈 문자을 작성합니다
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # 특정 구성 및 분할 비율로 ULTRACHAT_200k 데이터셋을 로드하고 분할합니다
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # 분할된 데이터에서 학습 및 테스트 데이터셋을 추출합니다
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # 학습 데이터셋을 JSONL 파일로 저장합니다
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # 테스트 데이터셋을 별도의 JSONL 파일로 저장합니다
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. 터미널에서 다음 명령어를 입력해 스크립트를 실행하고 데이터셋을 로컬 환경에 다운로드합니다.

    ```console
    python download_dataset.py
    ```

1. 데이터셋이 성공적으로 로컬 *finetune-phi/data* 디렉토리에 저장되었는지 확인합니다.

> [!NOTE]
>
> #### 데이터셋 크기 및 파인튜닝 시간 참고
>
> 이 튜토리얼에서는 데이터의 1%(`split='train[:1%]'`)만 사용합니다. 이렇게 하면 데이터양이 크게 줄어 업로드 및 파인튜닝 시간이 단축됩니다. 훈련 시간과 모델 성능 간의 적절한 균형을 위해 비율을 조정할 수 있습니다. 작은 데이터셋 부분집합 사용은 파인튜닝에 소요되는 시간을 줄여 튜토리얼을 더 관리하기 쉽게 만듭니다.

## 시나리오 2: Phi-3 모델 파인튜닝 및 Azure Machine Learning Studio에 배포

### Phi-3 모델 파인튜닝하기

이번 실습에서는 Azure Machine Learning Studio에서 Phi-3 모델을 파인튜닝합니다.

실습 내용:

- 파인튜닝을 위한 컴퓨터 클러스터 생성.
- Azure Machine Learning Studio에서 Phi-3 모델 파인튜닝.

#### 파인튜닝용 컴퓨터 클러스터 생성하기

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) 를 방문하세요.

1. 왼쪽 탭에서 **Compute** 를 선택합니다.

1. 탐색 메뉴에서 **Compute clusters** 를 선택합니다.

1. **+ New** 를 선택합니다.

    ![Select compute.](../../../../../../translated_images/ko/06-01-select-compute.a29cff290b480252.webp)

1. 다음을 수행합니다:

    - 사용할 **Region** 선택
    - **가상 머신 계층(Virtual machine tier)** 을 **Dedicated** 로 선택
    - **가상 머신 유형(Virtual machine type)** 을 **GPU** 로 선택
    - **가상 머신 크기 필터(Virtual machine size filter)** 를 **모든 옵션에서 선택(Select from all options)** 으로 선택
    - **가상 머신 크기(Virtual machine size)** 를 **Standard_NC24ads_A100_v4** 로 선택

    ![Create cluster.](../../../../../../translated_images/ko/06-02-create-cluster.f221b65ae1221d4e.webp)

1. **Next** 를 선택합니다.

1. 다음 작업을 수행합니다:

    - **컴퓨트 이름(Compute name)** 입력 (고유 값이어야 함)
    - **최소 노드 수(Minimum number of nodes)** 를 **0** 으로 선택
    - **최대 노드 수(Maximum number of nodes)** 를 **1** 로 선택
    - **스케일 다운 전 대기 시간(Idle seconds before scale down)** 을 **120** 으로 선택

    ![Create cluster.](../../../../../../translated_images/ko/06-03-create-cluster.4a54ba20914f3662.webp)

1. **Create** 를 선택합니다.

#### Phi-3 모델 파인튜닝하기

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) 를 방문하세요.

1. 생성한 Azure Machine Learning 작업 공간을 선택합니다.

    ![Select workspace that you created.](../../../../../../translated_images/ko/06-04-select-workspace.a92934ac04f4f181.webp)

1. 다음 작업을 수행합니다:

    - 왼쪽 탭에서 **Model catalog** 를 선택
    - <strong>검색창</strong> 에 *phi-3-mini-4k* 입력 후 나타나는 옵션에서 **Phi-3-mini-4k-instruct** 선택

    ![Type phi-3-mini-4k.](../../../../../../translated_images/ko/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. 탐색 메뉴에서 **Fine-tune** 을 선택합니다.

    ![Select fine tune.](../../../../../../translated_images/ko/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. 다음 작업을 수행합니다:

    - **작업 유형 선택(Select task type)** 에서 **Chat completion** 선택
    - **+ Select data** 를 눌러 **훈련 데이터(Training data)** 업로드
    - 검증 데이터 업로드 종류를 **다른 검증 데이터 제공(Provide different validation data)** 로 선택
    - **+ Select data** 를 눌러 **검증 데이터(Validation data)** 업로드

    ![Fill fine-tuning page.](../../../../../../translated_images/ko/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> **고급 설정(Advanced settings)** 에서 **learning_rate** 와 **lr_scheduler_type** 등 설정을 조절하여 파인튜닝을 최적화할 수 있습니다.

1. **Finish** 를 선택합니다.

1. 이 실습에서는 Azure Machine Learning을 사용해 Phi-3 모델을 성공적으로 파인튜닝했습니다. 파인튜닝에는 상당한 시간이 소요될 수 있습니다. 파인튜닝 작업을 실행한 후 완료될 때까지 기다려야 합니다. Azure Machine Learning 작업 공간 왼쪽의 작업 탭(Jobs tab)에서 파인튜닝 작업 상태를 확인할 수 있습니다. 다음 시리즈에서는 파인튜닝된 모델을 배포하고 Prompt Flow에 통합할 예정입니다.

    ![See finetuning job.](../../../../../../translated_images/ko/06-08-output.2bd32e59930672b1.webp)

### 파인튜닝된 Phi-3 모델 배포하기

파인튜닝된 Phi-3 모델을 Prompt Flow와 통합하려면, 실시간 추론을 위해 모델을 배포해야 합니다. 이 과정은 모델 등록, 온라인 엔드포인트 생성 그리고 모델 배포를 포함합니다.

이번 실습에서는 다음을 수행합니다:

- Azure Machine Learning 작업 공간에 파인튜닝된 모델 등록
- 온라인 엔드포인트 생성
- 등록한 파인튜닝된 Phi-3 모델 배포

#### 파인튜닝된 모델 등록하기

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) 를 방문하세요.

1. 생성한 Azure Machine Learning 작업 공간을 선택합니다.

    ![Select workspace that you created.](../../../../../../translated_images/ko/06-04-select-workspace.a92934ac04f4f181.webp)

1. 왼쪽 탭에서 **Models** 를 선택합니다.
1. **+ Register** 를 선택합니다.
1. **작업 출력에서(From a job output)** 선택합니다.

    ![Register model.](../../../../../../translated_images/ko/07-01-register-model.ad1e7cc05e4b2777.webp)

1. 생성한 작업을 선택합니다.

    ![Select job.](../../../../../../translated_images/ko/07-02-select-job.3e2e1144cd6cd093.webp)

1. **Next** 를 선택합니다.

1. **모델 유형(Model type)** 을 **MLflow** 로 선택합니다.

1. **작업 출력(Job output)** 이 선택되어 있는지 확인합니다. 자동으로 선택됩니다.

    ![Select output.](../../../../../../translated_images/ko/07-03-select-output.4cf1a0e645baea1f.webp)

2. **Next** 를 선택합니다.

3. **Register** 를 선택합니다.

    ![Select register.](../../../../../../translated_images/ko/07-04-register.fd82a3b293060bc7.webp)

4. 왼쪽 탭의 **Models** 메뉴에서 등록한 모델을 확인할 수 있습니다.

    ![Registered model.](../../../../../../translated_images/ko/07-05-registered-model.7db9775f58dfd591.webp)

#### 파인튜닝된 모델 배포하기

1. 생성한 Azure Machine Learning 작업 공간으로 이동합니다.

1. 왼쪽 탭에서 **Endpoints** 를 선택합니다.

1. 탐색 메뉴에서 **실시간 엔드포인트(Real-time endpoints)** 를 선택합니다.

    ![Create endpoint.](../../../../../../translated_images/ko/07-06-create-endpoint.1ba865c606551f09.webp)

1. **Create** 를 선택합니다.

1. 등록한 모델을 선택합니다.

    ![Select registered model.](../../../../../../translated_images/ko/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. **Select** 를 선택합니다.

1. 다음 작업을 수행합니다:

    - **가상 머신(Virtual machine)** 을 *Standard_NC6s_v3* 로 선택
    - 원하는 **인스턴스 수(Instance count)** 를 선택 (예: *1*)
    - **엔드포인트(Endpoint)** 를 **새로 만들기(New)** 로 선택
    - **엔드포인트 이름(Endpoint name)** 입력 (고유 값이어야 함)
    - **배포 이름(Deployment name)** 입력 (고유 값이어야 함)

    ![Fill the deployment setting.](../../../../../../translated_images/ko/07-08-deployment-setting.43ddc4209e673784.webp)

1. **Deploy** 를 선택합니다.

> [!WARNING]
> 추가 요금 부과를 방지하려면 Azure Machine Learning 작업 공간에서 생성한 엔드포인트를 반드시 삭제하세요.
>

#### Azure Machine Learning Workspace에서 배포 상태 확인하기

1. 생성한 Azure Machine Learning 작업 공간으로 이동합니다.

1. 왼쪽 탭에서 **Endpoints** 를 선택합니다.

1. 생성한 엔드포인트를 선택합니다.

    ![Select endpoints](../../../../../../translated_images/ko/07-09-check-deployment.325d18cae8475ef4.webp)

1. 이 페이지에서 배포 과정 중 엔드포인트를 관리할 수 있습니다.

> [!NOTE]
> 배포가 완료되면 **실시간 트래픽(Live traffic)** 이 **100%** 로 설정되어 있는지 확인하세요. 설정되어 있지 않다면 **업데이트 트래픽(Update traffic)** 를 선택해 설정할 수 있습니다. 트래픽이 0% 이면 모델 테스트를 할 수 없습니다.
>
> ![Set traffic.](../../../../../../translated_images/ko/07-10-set-traffic.085b847e5751ff3d.webp)
>

## 시나리오 3: Prompt Flow와 통합 및 Microsoft Foundry에서 맞춤형 모델과 대화하기

### 맞춤형 Phi-3 모델을 Prompt Flow와 통합하기

파인튜닝 모델을 성공적으로 배포한 후, Prompt Flow와 통합하여 실시간 애플리케이션에서 맞춤형 Phi-3 모델을 사용할 수 있습니다. 이를 통해 다양한 대화형 작업이 가능합니다.

이번 실습에서는 다음을 수행합니다:

- Microsoft Foundry Hub 생성
- Microsoft Foundry 프로젝트 생성
- Prompt Flow 생성
- 파인튜닝한 Phi-3 모델의 맞춤 연결 추가
- Prompt Flow 설정하여 맞춤형 Phi-3 모델과 대화

> [!NOTE]
> Azure ML Studio를 사용해 Promptflow와 통합할 수도 있습니다. 동일한 통합 프로세스를 Azure ML Studio에 적용할 수 있습니다.

#### Microsoft Foundry Hub 생성하기

프로젝트를 만들기 전에 Hub를 생성해야 합니다. Hub는 리소스 그룹과 유사한 역할을 하며 Microsoft Foundry 내 여러 프로젝트를 조직하고 관리할 수 있게 해줍니다.
1. [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) 방문

1. 왼쪽 탭에서 **All hubs** 선택

1. 내비게이션 메뉴에서 **+ New hub** 선택

    ![Create hub.](../../../../../../translated_images/ko/08-01-create-hub.8f7dd615bb8d9834.webp)

1. 다음 작업 수행:

    - **Hub name** 입력. 반드시 고유한 값이어야 합니다.
    - Azure **Subscription** 선택
    - 사용할 **Resource group** 선택 (필요 시 새로 만듦)
    - 사용할 **Location** 선택
    - 사용할 **Connect Azure AI Services** 선택 (필요 시 새로 만듦)
    - <strong>Connect Azure AI Search</strong>는 **Skip connecting** 선택

    ![Fill hub.](../../../../../../translated_images/ko/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. **Next** 선택

#### Microsoft Foundry 프로젝트 생성

1. 생성한 Hub에서 왼쪽 탭에서 **All projects** 선택

1. 내비게이션 메뉴에서 **+ New project** 선택

    ![Select new project.](../../../../../../translated_images/ko/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. **Project name** 입력. 반드시 고유한 값이어야 합니다.

    ![Create project.](../../../../../../translated_images/ko/08-05-create-project.4d97f0372f03375a.webp)

1. **Create a project** 선택

#### 파인튜닝된 Phi-3 모델을 위한 사용자 지정 연결 추가

사용자 지정 Phi-3 모델을 Prompt flow와 통합하려면 모델의 엔드포인트와 키를 사용자 지정 연결에 저장해야 합니다. 이 설정을 통해 Prompt flow에서 사용자 지정 Phi-3 모델에 접근할 수 있습니다.

#### 파인튜닝된 Phi-3 모델의 api 키와 엔드포인트 uri 설정

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) 방문

1. 생성한 Azure Machine learning 작업 영역으로 이동

1. 왼쪽 탭에서 **Endpoints** 선택

    ![Select endpoints.](../../../../../../translated_images/ko/08-06-select-endpoints.aff38d453bcf9605.webp)

1. 생성한 엔드포인트 선택

    ![Select endpoints.](../../../../../../translated_images/ko/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. 내비게이션 메뉴에서 **Consume** 선택

1. <strong>REST endpoint</strong>와 **Primary key** 복사

    ![Copy api key and endpoint uri.](../../../../../../translated_images/ko/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### 사용자 지정 연결 추가

1. [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) 방문

1. 생성한 Microsoft Foundry 프로젝트로 이동

1. 생성한 프로젝트에서 왼쪽 탭의 **Settings** 선택

1. **+ New connection** 선택

    ![Select new connection.](../../../../../../translated_images/ko/08-09-select-new-connection.02eb45deadc401fc.webp)

1. 내비게이션 메뉴에서 **Custom keys** 선택

    ![Select custom keys.](../../../../../../translated_images/ko/08-10-select-custom-keys.856f6b2966460551.webp)

1. 다음 작업 수행:

    - **+ Add key value pairs** 선택
    - 키 이름에 **endpoint** 입력 후 Azure ML Studio에서 복사한 엔드포인트를 값 필드에 붙여넣기
    - 다시 **+ Add key value pairs** 선택
    - 키 이름에 **key** 입력 후 Azure ML Studio에서 복사한 키를 값 필드에 붙여넣기
    - 키 추가 후 **is secret** 체크하여 키가 노출되지 않도록 설정

    ![Add connection.](../../../../../../translated_images/ko/08-11-add-connection.785486badb4d2d26.webp)

1. **Add connection** 선택

#### Prompt flow 생성

Microsoft Foundry에 사용자 지정 연결을 추가했습니다. 이제 다음 단계를 통해 Prompt flow를 생성하세요. 그런 다음 이 Prompt flow를 사용자 지정 연결에 연결하여 파인튜닝된 모델을 Prompt flow 내에서 사용할 수 있습니다.

1. 생성한 Microsoft Foundry 프로젝트로 이동

1. 왼쪽 탭에서 **Prompt flow** 선택

1. 내비게이션 메뉴에서 **+ Create** 선택

    ![Select Promptflow.](../../../../../../translated_images/ko/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. 내비게이션 메뉴에서 **Chat flow** 선택

    ![Select chat flow.](../../../../../../translated_images/ko/08-13-select-flow-type.2ec689b22da32591.webp)

1. 사용할 **Folder name** 입력

    ![Enter name.](../../../../../../translated_images/ko/08-14-enter-name.ff9520fefd89f40d.webp)

2. **Create** 선택

#### 파인튜닝된 Phi-3 모델과 대화할 수 있도록 Prompt flow 설정

파인튜닝된 Phi-3 모델을 Prompt flow에 통합해야 합니다. 기존 제공된 Prompt flow는 이를 위해 설계되지 않았으므로, 사용자 지정 모델 통합이 가능하도록 Prompt flow를 다시 설계해야 합니다.

1. Prompt flow에서 기존 흐름을 재구성하기 위해 다음 작업 수행:

    - **Raw file mode** 선택
    - *flow.dag.yml* 파일 내 모든 코드를 삭제
    - 다음 코드를 *flow.dag.yml* 파일에 추가

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

    - **Save** 선택

    ![Select raw file mode.](../../../../../../translated_images/ko/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. *integrate_with_promptflow.py* 파일에 다음 코드를 추가하여 Prompt flow에서 사용자 지정 Phi-3 모델을 사용

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
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection"은 사용자 정의 연결의 이름이고, "endpoint", "key"는 사용자 정의 연결의 키입니다
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
            
            # 전체 JSON 응답을 기록하세요
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

    ![Paste prompt flow code.](../../../../../../translated_images/ko/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Microsoft Foundry에서 Prompt flow를 사용하는 자세한 내용은 [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)에서 참고할 수 있습니다.

1. **Chat input**, **Chat output** 선택하여 모델과 채팅 활성화

    ![Input Output.](../../../../../../translated_images/ko/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. 이제 사용자 지정 Phi-3 모델과 채팅할 준비가 되었습니다. 다음 연습에서 Prompt flow를 시작하고 파인튜닝된 Phi-3 모델과 채팅하는 방법을 배울 것입니다.

> [!NOTE]
>
> 재구성된 흐름은 아래 이미지와 같이 보여야 합니다:
>
> ![Flow example.](../../../../../../translated_images/ko/08-18-graph-example.d6457533952e690c.webp)
>

### 사용자 지정 Phi-3 모델과 대화하기

이제 파인튜닝된 사용자 지정 Phi-3 모델을 Prompt flow와 통합했으므로 상호작용을 시작할 준비가 되었습니다. 이 연습에서는 Prompt flow를 사용하여 모델과 채팅을 설정하고 시작하는 과정을 안내합니다. 이 단계를 따라 파인튜닝된 Phi-3 모델의 다양한 작업 및 대화 기능을 완벽히 활용할 수 있습니다.

- Prompt flow를 사용하여 사용자 지정 Phi-3 모델과 채팅하기

#### Prompt flow 시작

1. **Start compute sessions** 선택하여 Prompt flow 시작

    ![Start compute session.](../../../../../../translated_images/ko/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. **Validate and parse input** 선택하여 매개변수 갱신

    ![Validate input.](../../../../../../translated_images/ko/09-02-validate-input.317c76ef766361e9.webp)

1. <strong>connection</strong>의 <strong>Value</strong>에서 생성한 사용자 지정 연결 선택. 예: *connection*

    ![Connection.](../../../../../../translated_images/ko/09-03-select-connection.99bdddb4b1844023.webp)

#### 사용자 지정 모델과 채팅하기

1. **Chat** 선택

    ![Select chat.](../../../../../../translated_images/ko/09-04-select-chat.61936dce6612a1e6.webp)

1. 다음은 결과 예시입니다: 이제 사용자 지정 Phi-3 모델과 채팅할 수 있습니다. 파인튜닝에 사용된 데이터에 기반한 질문을 하는 것이 권장됩니다.

    ![Chat with prompt flow.](../../../../../../translated_images/ko/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문은 해당 언어의 원본 문서를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우 전문가에 의한 인적 번역을 권장합니다. 본 번역 사용으로 발생하는 어떠한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->