<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-05-08T05:11:23+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "ko"
}
-->
## Azure ML 시스템 레지스트리의 chat-completion 컴포넌트를 사용해 모델 미세 조정하기

이 예제에서는 ultrachat_200k 데이터셋을 사용해 Phi-3-mini-4k-instruct 모델을 두 사람 간의 대화를 완성하도록 미세 조정하는 과정을 진행합니다.

![MLFineTune](../../../../translated_images/MLFineTune.928d4c6b3767dd35fbd9d20d56e4116e17c55b0e0eb45500069eeee3a2d6fa0a.ko.png)

예제에서는 Azure ML SDK와 Python을 사용해 미세 조정을 수행하고, 미세 조정된 모델을 실시간 추론을 위한 온라인 엔드포인트에 배포하는 방법을 보여줍니다.

### 학습 데이터

ultrachat_200k 데이터셋을 사용합니다. 이 데이터셋은 UltraChat 데이터셋을 강력히 필터링한 버전으로, 최신 7b 채팅 모델인 Zephyr-7B-β를 학습하는 데 사용되었습니다.

### 모델

채팅 완성 작업에 대해 사용자가 모델을 미세 조정하는 방법을 보여주기 위해 Phi-3-mini-4k-instruct 모델을 사용합니다. 특정 모델 카드에서 이 노트북을 열었다면, 해당 모델 이름으로 교체해야 합니다.

### 작업 목록

- 미세 조정할 모델 선택
- 학습 데이터 선택 및 탐색
- 미세 조정 작업 구성
- 미세 조정 작업 실행
- 학습 및 평가 지표 검토
- 미세 조정된 모델 등록
- 실시간 추론을 위한 모델 배포
- 리소스 정리

## 1. 사전 준비 설정

- 종속성 설치
- AzureML 워크스페이스 연결. SDK 인증 설정에 대해 더 알아보세요. 아래에서 <WORKSPACE_NAME>, <RESOURCE_GROUP>, <SUBSCRIPTION_ID>를 교체하세요.
- azureml 시스템 레지스트리 연결
- 선택적 실험 이름 설정
- 컴퓨트 확인 또는 생성

> [!NOTE]
> 단일 GPU 노드는 여러 GPU 카드를 가질 수 있습니다. 예를 들어, Standard_NC24rs_v3 노드 하나에는 4개의 NVIDIA V100 GPU가 있고, Standard_NC12s_v3 노드에는 2개의 NVIDIA V100 GPU가 있습니다. 자세한 내용은 문서를 참고하세요. 노드 당 GPU 카드 수는 아래 param gpus_per_node에서 설정합니다. 이 값을 올바르게 설정하면 노드 내 모든 GPU를 활용할 수 있습니다. 권장 GPU 컴퓨트 SKU는 여기와 여기에서 확인할 수 있습니다.

### Python 라이브러리

아래 셀을 실행해 종속성을 설치하세요. 새 환경에서 실행할 경우 필수 단계입니다.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML과 상호작용하기

1. 이 Python 스크립트는 Azure Machine Learning(Azure ML) 서비스와 상호작용하는 데 사용됩니다. 주요 내용은 다음과 같습니다:

    - azure.ai.ml, azure.identity, azure.ai.ml.entities 패키지에서 필요한 모듈을 임포트하며, time 모듈도 임포트합니다.

    - DefaultAzureCredential()을 사용해 인증을 시도합니다. 이 방식은 Azure 클라우드에서 애플리케이션 개발을 빠르게 시작할 수 있도록 간편한 인증 경험을 제공합니다. 실패 시 InteractiveBrowserCredential()로 대체하여 대화형 로그인 프롬프트를 띄웁니다.

    - from_config 메서드를 사용해 기본 설정 파일(config.json)에서 구성 정보를 읽어 MLClient 인스턴스를 생성하려 시도합니다. 실패하면 subscription_id, resource_group_name, workspace_name을 직접 제공해 MLClient 인스턴스를 만듭니다.

    - Azure ML 레지스트리인 "azureml"용 MLClient 인스턴스를 추가로 생성합니다. 이 레지스트리는 모델, 미세 조정 파이프라인, 환경 등이 저장되는 곳입니다.

    - experiment_name을 "chat_completion_Phi-3-mini-4k-instruct"로 설정합니다.

    - 현재 시간을 정수형 문자열로 변환해 고유 타임스탬프를 생성합니다. 이 타임스탬프는 고유한 이름과 버전을 생성하는 데 사용됩니다.

    ```python
    # Import necessary modules from Azure ML and Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Import time module
    
    # Try to authenticate using DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # If DefaultAzureCredential fails, use InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Try to create an MLClient instance using the default config file
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # If that fails, create an MLClient instance by manually providing the details
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Create another MLClient instance for the Azure ML registry named "azureml"
    # This registry is where models, fine-tuning pipelines, and environments are stored
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Set the experiment name
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generate a unique timestamp that can be used for names and versions that need to be unique
    timestamp = str(int(time.time()))
    ```

## 2. 미세 조정할 기본 모델 선택

1. Phi-3-mini-4k-instruct는 38억 개의 파라미터를 가진 경량 최신 오픈 모델로, Phi-2에 사용된 데이터셋을 기반으로 만들어졌습니다. 이 모델은 Phi-3 모델군에 속하며, Mini 버전은 컨텍스트 길이(토큰 수)에 따라 4K와 128K 두 가지 변형이 있습니다. 특정 목적에 맞게 모델을 미세 조정해야 합니다. AzureML Studio의 모델 카탈로그에서 채팅 완성 작업 필터를 적용해 이 모델들을 탐색할 수 있습니다. 이 예제에서는 Phi-3-mini-4k-instruct 모델을 사용합니다. 다른 모델로 이 노트북을 열었다면 모델 이름과 버전을 적절히 바꾸세요.

    > [!NOTE]
    > 모델 ID 속성은 미세 조정 작업에 입력으로 전달됩니다. AzureML Studio 모델 카탈로그의 모델 세부 정보 페이지에서 Asset ID 필드로도 확인할 수 있습니다.

2. 이 Python 스크립트는 Azure Machine Learning 서비스와 상호작용합니다. 주요 내용은 다음과 같습니다:

    - model_name을 "Phi-3-mini-4k-instruct"로 설정합니다.

    - registry_ml_client 객체의 models 속성에서 get 메서드를 사용해 지정한 이름의 최신 버전 모델을 Azure ML 레지스트리에서 가져옵니다. get 메서드는 모델 이름과 최신 버전을 가져오라는 라벨을 인수로 받습니다.

    - 선택한 모델의 이름, 버전, ID를 출력해 미세 조정에 사용할 모델 정보를 콘솔에 표시합니다.

    ```python
    # Set the model name
    model_name = "Phi-3-mini-4k-instruct"
    
    # Get the latest version of the model from the Azure ML registry
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Print the model name, version, and id
    # This information is useful for tracking and debugging
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. 작업에 사용할 컴퓨트 생성

미세 조정 작업은 GPU 컴퓨트에서만 작동합니다. 컴퓨트 크기는 모델 크기에 따라 달라지며, 적절한 컴퓨트를 선택하는 것이 까다로울 수 있습니다. 이 셀에서는 적합한 컴퓨트를 선택하도록 안내합니다.

> [!NOTE]
> 아래에 나열된 컴퓨트는 최적화된 구성으로 작동합니다. 구성을 변경하면 Cuda Out Of Memory 오류가 발생할 수 있습니다. 이런 경우 더 큰 컴퓨트 크기로 업그레이드하세요.

> [!NOTE]
> compute_cluster_size를 선택할 때, 해당 컴퓨트가 리소스 그룹에 존재하는지 확인하세요. 특정 컴퓨트가 없다면 컴퓨트 리소스 접근 요청을 할 수 있습니다.

### 미세 조정 지원 여부 확인

1. 이 Python 스크립트는 Azure Machine Learning 모델과 상호작용하며, 다음 작업을 수행합니다:

    - Python 추상 구문 트리 처리를 위한 ast 모듈을 임포트합니다.

    - foundation_model 객체에 finetune_compute_allow_list라는 태그가 있는지 확인합니다. Azure ML에서 태그는 모델 필터링과 정렬에 사용하는 키-값 쌍입니다.

    - finetune_compute_allow_list 태그가 있으면 ast.literal_eval 함수를 사용해 문자열 값을 안전하게 파이썬 리스트로 변환한 뒤 computes_allow_list 변수에 할당하고, 해당 리스트에서 컴퓨트를 생성해야 한다는 메시지를 출력합니다.

    - 태그가 없으면 computes_allow_list를 None으로 설정하고, 해당 태그가 모델 태그에 없다는 메시지를 출력합니다.

    - 요약하면, 이 스크립트는 모델 메타데이터에서 특정 태그를 검사하고, 태그가 있으면 값을 리스트로 변환해 사용자에게 알려줍니다.

    ```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Check if the 'finetune_compute_allow_list' tag is present in the model's tags
    if "finetune_compute_allow_list" in foundation_model.tags:
        # If the tag is present, use ast.literal_eval to safely parse the tag's value (a string) into a Python list
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # convert string to python list
        # Print a message indicating that a compute should be created from the list
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If the tag is not present, set computes_allow_list to None
        computes_allow_list = None
        # Print a message indicating that the 'finetune_compute_allow_list' tag is not part of the model's tags
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### 컴퓨트 인스턴스 확인

1. 이 Python 스크립트는 Azure ML 서비스와 상호작용하며, 컴퓨트 인스턴스에 대해 여러 검사를 수행합니다. 주요 내용은 다음과 같습니다:

    - compute_cluster에 저장된 이름으로 컴퓨트 인스턴스를 워크스페이스에서 가져오려 시도합니다. 프로비저닝 상태가 "failed"이면 ValueError를 발생시킵니다.

    - computes_allow_list가 None이 아니면, 리스트 내 모든 컴퓨트 크기를 소문자로 변환한 뒤 현재 컴퓨트 인스턴스 크기가 리스트에 있는지 확인합니다. 없으면 ValueError를 발생시킵니다.

    - computes_allow_list가 None이면, 현재 컴퓨트 크기가 지원하지 않는 GPU VM 크기 목록에 있는지 확인하고, 있으면 ValueError를 발생시킵니다.

    - 워크스페이스 내 모든 사용 가능한 컴퓨트 크기 목록을 가져온 뒤, 현재 컴퓨트 크기와 이름이 일치하는 항목을 찾아 GPU 수를 가져옵니다. gpu_count_found 플래그를 True로 설정합니다.

    - gpu_count_found가 True면 컴퓨트 인스턴스 내 GPU 수를 출력하고, False면 ValueError를 발생시킵니다.

    - 요약하면, 이 스크립트는 컴퓨트 인스턴스의 프로비저닝 상태, 크기 허용 여부, GPU 수를 검사합니다.

    ```python
    # Print the exception message
    print(e)
    # Raise a ValueError if the compute size is not available in the workspace
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Retrieve the compute instance from the Azure ML workspace
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Check if the provisioning state of the compute instance is "failed"
    if compute.provisioning_state.lower() == "failed":
        # Raise a ValueError if the provisioning state is "failed"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Check if computes_allow_list is not None
    if computes_allow_list is not None:
        # Convert all compute sizes in computes_allow_list to lowercase
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Check if the size of the compute instance is in computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Raise a ValueError if the size of the compute instance is not in computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Define a list of unsupported GPU VM sizes
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Check if the size of the compute instance is in unsupported_gpu_vm_list
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Raise a ValueError if the size of the compute instance is in unsupported_gpu_vm_list
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialize a flag to check if the number of GPUs in the compute instance has been found
    gpu_count_found = False
    # Retrieve a list of all available compute sizes in the workspace
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iterate over the list of available compute sizes
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Check if the name of the compute size matches the size of the compute instance
        if compute_sku.name.lower() == compute.size.lower():
            # If it does, retrieve the number of GPUs for that compute size and set gpu_count_found to True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # If gpu_count_found is True, print the number of GPUs in the compute instance
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # If gpu_count_found is False, raise a ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. 모델 미세 조정을 위한 데이터셋 선택

1. ultrachat_200k 데이터셋을 사용합니다. 데이터셋은 감독 학습 미세 조정(SFT)에 적합한 4개 분할로 나뉘어 있습니다.
생성 랭킹(gen)이며, 분할별 예제 수는 다음과 같습니다:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. 다음 셀들은 미세 조정을 위한 기본 데이터 준비 과정을 보여줍니다:

### 일부 데이터 행 시각화

이 샘플은 빠르게 실행되도록 train_sft, test_sft 파일에 이미 다듬어진 행의 5%만 저장합니다. 이로 인해 미세 조정된 모델의 정확도는 낮아지므로 실제 환경에 적용해서는 안 됩니다.
download-dataset.py는 ultrachat_200k 데이터셋을 다운로드하고, 미세 조정 파이프라인 컴포넌트에서 사용할 수 있는 형식으로 변환하는 데 사용됩니다. 데이터셋이 크기 때문에 여기서는 일부만 포함되어 있습니다.

1. 아래 스크립트를 실행하면 데이터의 5%만 다운로드됩니다. dataset_split_pc 파라미터를 원하는 비율로 변경해 증가시킬 수 있습니다.

    > [!NOTE]
    > 일부 언어 모델은 언어 코드가 다르므로, 데이터셋 내 컬럼 이름도 이에 맞게 설정해야 합니다.

1. 데이터는 다음과 같은 형식으로 저장됩니다.
chat-completion 데이터셋은 각 항목이 다음 스키마를 따르는 parquet 형식으로 저장됩니다:

    - JSON(JavaScript Object Notation) 문서로, 실행 가능한 코드는 아니며 데이터를 저장하고 전달하는 형식입니다. 구조는 다음과 같습니다:

    - "prompt": AI 어시스턴트에게 제시되는 작업 또는 질문을 나타내는 문자열 값입니다.

    - "messages": 객체 배열로, 사용자와 AI 어시스턴트 간 대화 메시지를 나타냅니다. 각 메시지 객체는 두 개의 키를 가집니다:

    - "content": 메시지 내용을 나타내는 문자열 값입니다.
    - "role": 메시지를 보낸 주체의 역할을 나타내는 문자열 값으로, "user" 또는 "assistant"가 될 수 있습니다.
    - "prompt_id": 프롬프트의 고유 식별자를 나타내는 문자열 값입니다.

1. 이 JSON 문서에서는 사용자가 AI 어시스턴트에게 디스토피아 이야기의 주인공을 만들어 달라고 요청하는 대화가 표현되어 있습니다. 어시스턴트가 응답하고, 사용자가 더 자세한 내용을 요청하면 어시스턴트가 동의해 더 자세한 내용을 제공합니다. 대화 전체는 특정 prompt_id와 연결되어 있습니다.

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### 데이터 다운로드

1. 이 Python 스크립트는 download-dataset.py라는 헬퍼 스크립트를 사용해 데이터셋을 다운로드합니다. 주요 내용은 다음과 같습니다:

    - 운영 체제 기능을 포팅 가능한 방식으로 제공하는 os 모듈을 임포트합니다.

    - os.system 함수를 사용해 쉘에서 download-dataset.py 스크립트를 실행하며, 데이터셋 이름(HuggingFaceH4/ultrachat_200k), 다운로드 디렉터리(ultrachat_200k_dataset), 데이터셋 분할 비율(5%)을 명령줄 인수로 전달합니다. 실행 상태 코드를 exit_status 변수에 저장합니다.

    - exit_status가 0이 아니면(Unix 계열 OS에서 0은 성공을 의미), 데이터셋 다운로드 중 오류가 발생했다는 예외를 발생시킵니다.

    - 요약하면, 이 스크립트는 헬퍼 스크립트를 통해 데이터셋을 다운로드하며, 실패 시 예외를 발생시킵니다.

    ```python
    # Import the os module, which provides a way of using operating system dependent functionality
    import os
    
    # Use the os.system function to run the download-dataset.py script in the shell with specific command-line arguments
    # The arguments specify the dataset to download (HuggingFaceH4/ultrachat_200k), the directory to download it to (ultrachat_200k_dataset), and the percentage of the dataset to split (5)
    # The os.system function returns the exit status of the command it executed; this status is stored in the exit_status variable
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Check if exit_status is not 0
    # In Unix-like operating systems, an exit status of 0 usually indicates that a command has succeeded, while any other number indicates an error
    # If exit_status is not 0, raise an Exception with a message indicating that there was an error downloading the dataset
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### 데이터프레임으로 데이터 로드

1. 이 Python 스크립트는 JSON Lines 파일을 pandas DataFrame으로 불러와 처음 5개 행을 출력합니다. 주요 내용은 다음과 같습니다:

    - 강력한 데이터 조작 및 분석 라이브러리인 pandas를 임포트합니다.

    - pandas 출력 옵션에서 최대 열 너비를 0으로 설정해, DataFrame을 출력할 때 각 열의 전체 텍스트가 잘리지 않고 표시되도록 합니다.

    - pd.read_json 함수를 사용해 ultrachat_200k_dataset 디렉터리 내 train_sft.jsonl 파일을 DataFrame으로 불러옵니다. lines=True는 JSON Lines 형식임을 나타냅니다.

    - head 메서드를 사용해 DataFrame의 처음 5개 행을 출력합니다. 데이터가 5개 미만이면 모두 출력합니다.

    - 요약하면, 이 스크립트는 JSON Lines 파일을 DataFrame으로 불러와 전체 텍스트가 보이도록 출력합니다.

    ```python
    # Import the pandas library, which is a powerful data manipulation and analysis library
    import pandas as pd
    
    # Set the maximum column width for pandas' display options to 0
    # This means that the full text of each column will be displayed without truncation when the DataFrame is printed
    pd.set_option("display.max_colwidth", 0)
    
    # Use the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame
    # The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Use the head method to display the first 5 rows of the DataFrame
    # If the DataFrame has less than 5 rows, it will display all of them
    df.head()
    ```

## 5. 모델과 데이터를 입력으로 하여 미세 조정 작업 제출

chat-completion 파이프라인 컴포넌트를 사용하는 작업을 생성합니다. 미세 조정에 지원되는 모든 파라미터에 대해 더 알아보세요.

### 미세 조정 파라미터 정의

1. 미세 조정 파라미터는 크게 두 가지로 나뉩니다 - 학습 파라미터와 최적화 파라미터

1. 학습 파라미터는 다음과 같은 학습 관련 설정을 정의합니다 -

    - 사용할 옵티마이저와 스케줄러
    - 미세 조정 최적화에 사용할 지표
    - 학습 스텝 수, 배치 크기 등
    - 최적화 파라미터는 GPU 메모리 최적화와 컴퓨트 자원 효율적 사용에 도움을 줍니다.

1. 다음은 최적화 파라미터에 속하는 몇 가지 예시입니다. 최적화 파라미터는 모델마다 다르며, 모델과 함께 패키징되어 있어 변동을 처리합니다.

    - deepspeed 및 LoRA 활성화
    - 혼합 정밀도 학습 활성화
    - 다중 노드 학습 활성화

> [!NOTE]
> 감독 학습 기반 미세 조정은 정렬(alignment) 손실이나 치명적인 망각(catastrophic forgetting)을 초래할 수 있습니다. 이를 확인하고 미세 조정 후 정렬 단계를 실행하는 것을 권장합니다.

### 미세 조정 파라미터 설정

1. 이 Python 스크립트는 머신러닝 모델 미세 조정을 위한 파라미터를 설정합니다. 주요 내용은 다음과 같습니다:

    - 기본 학습 파라미터로 학습 에폭 수, 학습 및 평가 배치 크기, 학습률, 학습률 스케줄러 타입 등을 설정합니다.

    - 기본 최적화 파라미터로 Layer-wise Relevance Propagation(LoRa) 및 DeepSpeed 적용 여부, DeepSpeed 단계 등을 설정합니다.

    - 학습 및 최적화 파라미터를 결합해 finetune_parameters라는 하나의 딕셔너리로 만듭니다.

    - foundation_model에 모델별 기본 파라미터가 있으면 경고 메시지를 출력하고, ast.literal_eval 함수를 사용해 문자열로 된 모델별 기본값을 파이썬 딕셔너리로 변환 후 finetune_parameters를 업데이트합니다.

    - 최종적으로 미세 조정에 사용할 파라미터를 출력합니다.

    - 요약하면, 이 스크립트는 머신러닝 모델 미세 조정을 위한 파라미터를 설정하고, 모델별 기본값으로 덮어쓸 수 있도록 합니다.

    ```python
    # Set up default training parameters such as the number of training epochs, batch sizes for training and evaluation, learning rate, and learning rate scheduler type
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Set up default optimization parameters such as whether to apply Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and the DeepSpeed stage
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Combine the training and optimization parameters into a single dictionary called finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Check if the foundation_model has any model-specific default parameters
    # If it does, print a warning message and update the finetune_parameters dictionary with these model-specific defaults
    # The ast.literal_eval function is used to convert the model-specific defaults from a string to a Python dictionary
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # convert string to python dict
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Print the final set of fine-tuning parameters that will be used for the run
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### 학습 파이프라인

1. 이 Python 스크립트는 머신러닝 학습 파이프라인의 표시 이름을 생성하는 함수를 정의하고, 이를 호출해 표시 이름을 생성 및 출력합니다. 주요 내용은 다음과 같습니다:

    1. get_pipeline_display_name 함수가 정의됩니다. 이 함수는 학습 파이프라인과 관련된 여러 파라미터를 기반으로 표시 이름을 생성합니다.

    2. 함수 내부에서 전체 배치 크기를, 디바이스 당 배치 크기, 그래디언트 누적 단계 수, 노드 당 GPU 수, 미세 조정에 사용되는 노드 수를 곱해 계산합니다.

    3. 학습률 스케줄러 타입, DeepSpeed 적용 여부 및 단계, LoRa 적용 여부, 유지할 모델 체크포인트 수 제한, 최대 시퀀스 길이 등의 다른 파라미터를 가져옵니다.

    4. 이 파라미터들을 하이픈(-)으로 구분해 문자열로 만듭니다. DeepSpeed 또는 LoRa가 적용되면 각각 "ds"와 DeepSpeed 단계, 또는 "lora"를 포함시키고, 적용 안 됐으면 "nods" 또는 "nolora"를 포함합니다.

    5. 함수는 이 문자열을 반환하며, 학습 파이프라인의 표시 이름으로 사용됩니다.

    6. 함수 정의 후 호출해 표시 이름을 생성하고 출력합니다.

    7. 요약하면, 이 스크립트는 머신러닝 학습 파이프라인의 표시 이름을 생성합니다.
다양한 매개변수에 기반한 학습 파이프라인을 생성한 후 이 표시 이름을 출력합니다. ```python
    # Define a function to generate a display name for the training pipeline
    def get_pipeline_display_name():
        # Calculate the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Retrieve the learning rate scheduler type
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Retrieve whether DeepSpeed is applied
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Retrieve the DeepSpeed stage
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # If DeepSpeed is applied, include "ds" followed by the DeepSpeed stage in the display name; if not, include "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Retrieve whether Layer-wise Relevance Propagation (LoRa) is applied
        lora = finetune_parameters.get("apply_lora", "false")
        # If LoRa is applied, include "lora" in the display name; if not, include "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Retrieve the limit on the number of model checkpoints to keep
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Retrieve the maximum sequence length
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Construct the display name by concatenating all these parameters, separated by hyphens
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # Call the function to generate the display name
    pipeline_display_name = get_pipeline_display_name()
    # Print the display name
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### 파이프라인 구성하기

이 Python 스크립트는 Azure Machine Learning SDK를 사용하여 머신러닝 파이프라인을 정의하고 구성합니다. 주요 내용은 다음과 같습니다:

1. Azure AI ML SDK에서 필요한 모듈을 가져옵니다.
1. 레지스트리에서 "chat_completion_pipeline"이라는 이름의 파이프라인 컴포넌트를 가져옵니다.
1. `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False`를 사용해 파이프라인 작업을 정의합니다. 이는 파이프라인 내 어느 단계라도 실패하면 작업이 중단됨을 의미합니다.
1. 요약하자면, 이 스크립트는 Azure Machine Learning SDK를 이용해 챗 완료 작업을 위한 머신러닝 파이프라인을 정의하고 구성합니다.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Fetch the pipeline component named "chat_completion_pipeline" from the registry
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Define the pipeline job using the @pipeline decorator and the function create_pipeline
    # The name of the pipeline is set to pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Initialize the fetched pipeline component with various parameters
        # These include the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Map the dataset splits to parameters
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Training settings
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Set to the number of GPUs available in the compute
            **finetune_parameters
        )
        return {
            # Map the output of the fine tuning job to the output of pipeline job
            # This is done so that we can easily register the fine tuned model
            # Registering the model is required to deploy the model to an online or batch endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Create an instance of the pipeline by calling the create_pipeline function
    pipeline_object = create_pipeline()
    
    # Don't use cached results from previous jobs
    pipeline_object.settings.force_rerun = True
    
    # Set continue on step failure to False
    # This means that the pipeline will stop if any step fails
    pipeline_object.settings.continue_on_step_failure = False
    ```

### 작업 제출하기

1. 이 Python 스크립트는 Azure Machine Learning 작업 공간에 머신러닝 파이프라인 작업을 제출하고 작업 완료를 기다립니다. 주요 내용은 다음과 같습니다:

   - workspace_ml_client의 jobs 객체의 create_or_update 메서드를 호출해 pipeline_object로 지정된 파이프라인 작업을 제출합니다. 작업은 experiment_name 아래에서 실행됩니다.

   - 이후 jobs 객체의 stream 메서드를 호출해 pipeline_job 객체의 name 속성으로 지정된 작업이 완료될 때까지 대기합니다.

1. 요약하자면, 이 스크립트는 Azure Machine Learning 작업 공간에 머신러닝 파이프라인 작업을 제출하고 작업 완료를 기다립니다.

```python
    # Submit the pipeline job to the Azure Machine Learning workspace
    # The pipeline to be run is specified by pipeline_object
    # The experiment under which the job is run is specified by experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Wait for the pipeline job to complete
    # The job to wait for is specified by the name attribute of the pipeline_job object
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. 미세 조정된 모델을 작업 공간에 등록하기

미세 조정 작업의 출력에서 모델을 등록합니다. 이를 통해 미세 조정된 모델과 미세 조정 작업 간의 계보를 추적할 수 있습니다. 미세 조정 작업은 다시 기초 모델, 데이터, 학습 코드와의 계보를 추적합니다.

### ML 모델 등록하기

1. 이 Python 스크립트는 Azure Machine Learning 파이프라인에서 학습된 머신러닝 모델을 등록합니다. 주요 내용은 다음과 같습니다:

   - Azure AI ML SDK에서 필요한 모듈을 가져옵니다.

   - workspace_ml_client의 jobs 객체의 get 메서드를 호출해 pipeline 작업에서 trained_model 출력이 있는지 확인합니다.

   - 파이프라인 작업 이름과 출력 이름("trained_model")을 사용해 학습된 모델 경로를 만듭니다.

   - 원본 모델 이름에 "-ultrachat-200k"를 덧붙이고 슬래시를 하이픈으로 바꿔 미세 조정 모델 이름을 정의합니다.

   - Model 객체를 생성하여 모델 경로, 모델 유형(MLflow 모델), 이름, 버전, 설명 등 여러 매개변수를 지정해 모델 등록 준비를 합니다.

   - workspace_ml_client의 models 객체의 create_or_update 메서드를 호출해 모델을 등록합니다.

   - 등록된 모델 정보를 출력합니다.

1. 요약하자면, 이 스크립트는 Azure Machine Learning 파이프라인에서 학습된 머신러닝 모델을 등록합니다.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Check if the `trained_model` output is available from the pipeline job
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Construct a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Define a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Prepare to register the model by creating a Model object with various parameters
    # These include the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Use timestamp as version to avoid version conflict
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Register the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Print the registered model
    print("registered model: \n", registered_model)
    ```

## 7. 미세 조정된 모델을 온라인 엔드포인트에 배포하기

온라인 엔드포인트는 모델을 사용하는 애플리케이션과 통합할 수 있는 내구성 있는 REST API를 제공합니다.

### 엔드포인트 관리

1. 이 Python 스크립트는 등록된 모델을 위해 Azure Machine Learning에서 관리형 온라인 엔드포인트를 생성합니다. 주요 내용은 다음과 같습니다:

   - Azure AI ML SDK에서 필요한 모듈을 가져옵니다.

   - "ultrachat-completion-" 문자열에 타임스탬프를 붙여 고유한 온라인 엔드포인트 이름을 정의합니다.

   - ManagedOnlineEndpoint 객체를 생성해 엔드포인트 이름, 설명, 인증 모드("key") 등 여러 매개변수를 지정해 온라인 엔드포인트 생성 준비를 합니다.

   - workspace_ml_client의 begin_create_or_update 메서드를 호출해 온라인 엔드포인트를 생성하고, wait 메서드로 완료를 대기합니다.

1. 요약하자면, 이 스크립트는 Azure Machine Learning에서 등록된 모델을 위한 관리형 온라인 엔드포인트를 생성합니다.

```python
    # Import necessary modules from the Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Define a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Prepare to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters
    # These include the name of the endpoint, a description of the endpoint, and the authentication mode ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Create the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument
    # Then wait for the creation operation to complete by calling the wait method
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> 배포에 지원되는 SKU 목록은 여기에서 확인할 수 있습니다 - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### ML 모델 배포하기

1. 이 Python 스크립트는 Azure Machine Learning에서 등록된 머신러닝 모델을 관리형 온라인 엔드포인트에 배포합니다. 주요 내용은 다음과 같습니다:

   - Python 추상 구문 트리를 처리하는 ast 모듈을 가져옵니다.

   - 배포에 사용할 인스턴스 유형을 "Standard_NC6s_v3"로 설정합니다.

   - 기초 모델에 inference_compute_allow_list 태그가 있는지 확인합니다. 있으면 문자열을 Python 리스트로 변환해 inference_computes_allow_list에 할당하고, 없으면 None으로 설정합니다.

   - 지정된 인스턴스 유형이 허용 목록에 있는지 확인합니다. 없으면 허용 목록에 있는 인스턴스 유형을 선택하라는 메시지를 출력합니다.

   - ManagedOnlineDeployment 객체를 생성해 배포 이름, 엔드포인트 이름, 모델 ID, 인스턴스 유형과 수, 라이브니스 프로브 설정, 요청 설정 등 여러 매개변수를 지정해 배포 준비를 합니다.

   - workspace_ml_client의 begin_create_or_update 메서드를 호출해 배포를 생성하고, wait 메서드로 완료를 대기합니다.

   - 엔드포인트 트래픽을 "demo" 배포로 100% 지정합니다.

   - workspace_ml_client의 begin_create_or_update 메서드를 호출해 엔드포인트를 업데이트하고, result 메서드로 완료를 대기합니다.

1. 요약하자면, 이 스크립트는 Azure Machine Learning에서 등록된 머신러닝 모델을 관리형 온라인 엔드포인트에 배포합니다.

```python
    # Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
    import ast
    
    # Set the instance type for the deployment
    instance_type = "Standard_NC6s_v3"
    
    # Check if the `inference_compute_allow_list` tag is present in the foundation model
    if "inference_compute_allow_list" in foundation_model.tags:
        # If it is, convert the tag value from a string to a Python list and assign it to `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # If it's not, set `inference_computes_allow_list` to `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Check if the specified instance type is in the allow list
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Prepare to create the deployment by creating a `ManagedOnlineDeployment` object with various parameters
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Create the deployment by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `ManagedOnlineDeployment` object as the argument
    # Then wait for the creation operation to complete by calling the `wait` method
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Set the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment
    endpoint.traffic = {"demo": 100}
    
    # Update the endpoint by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `endpoint` object as the argument
    # Then wait for the update operation to complete by calling the `result` method
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. 샘플 데이터로 엔드포인트 테스트하기

테스트 데이터셋에서 샘플 데이터를 가져와 온라인 엔드포인트에 추론을 요청합니다. 이후 예측된 레이블과 실제 레이블을 함께 표시합니다.

### 결과 읽기

1. 이 Python 스크립트는 JSON Lines 파일을 pandas DataFrame으로 읽고, 무작위 샘플을 추출한 뒤 인덱스를 재설정합니다. 주요 내용은 다음과 같습니다:

   - ./ultrachat_200k_dataset/test_gen.jsonl 파일을 pandas DataFrame으로 읽습니다. read_json 함수에 lines=True를 지정하는 이유는 파일이 JSON Lines 형식으로 각 줄이 별도의 JSON 객체이기 때문입니다.

   - DataFrame에서 무작위로 1개의 행을 샘플링합니다. sample 함수에 n=1을 지정해 샘플 개수를 정합니다.

   - reset_index 함수에 drop=True를 지정해 기존 인덱스를 버리고 기본 정수 인덱스로 재설정합니다.

   - head 함수에 2를 지정해 DataFrame 상위 2개 행을 출력합니다. 그러나 샘플링 후 데이터가 1행뿐이므로 한 행만 출력됩니다.

1. 요약하자면, 이 스크립트는 JSON Lines 파일을 pandas DataFrame으로 읽고, 1개 행을 무작위 샘플링하며 인덱스를 재설정한 뒤 첫 행을 출력합니다.

```python
    # Import pandas library
    import pandas as pd
    
    # Read the JSON Lines file './ultrachat_200k_dataset/test_gen.jsonl' into a pandas DataFrame
    # The 'lines=True' argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Take a random sample of 1 row from the DataFrame
    # The 'n=1' argument specifies the number of random rows to select
    test_df = test_df.sample(n=1)
    
    # Reset the index of the DataFrame
    # The 'drop=True' argument indicates that the original index should be dropped and replaced with a new index of default integer values
    # The 'inplace=True' argument indicates that the DataFrame should be modified in place (without creating a new object)
    test_df.reset_index(drop=True, inplace=True)
    
    # Display the first 2 rows of the DataFrame
    # However, since the DataFrame only contains one row after the sampling, this will only display that one row
    test_df.head(2)
    ```

### JSON 객체 생성하기

1. 이 Python 스크립트는 특정 매개변수를 가진 JSON 객체를 생성하고 파일로 저장합니다. 주요 내용은 다음과 같습니다:

   - JSON 데이터를 다루기 위한 json 모듈을 가져옵니다.

   - 머신러닝 모델 매개변수를 나타내는 딕셔너리 parameters를 만듭니다. 키는 "temperature", "top_p", "do_sample", "max_new_tokens"이며, 각각 0.6, 0.9, True, 200의 값을 가집니다.

   - test_json이라는 또 다른 딕셔너리를 만듭니다. 키는 "input_data"와 "params"이며, "input_data"는 "input_string"과 "parameters"를 키로 갖는 딕셔너리입니다. "input_string" 값은 test_df DataFrame에서 첫 번째 메시지를 담은 리스트이고, "parameters" 값은 앞서 만든 parameters 딕셔너리입니다. "params"는 빈 딕셔너리입니다.

   - sample_score.json 파일을 엽니다.

```python
    # Import the json module, which provides functions to work with JSON data
    import json
    
    # Create a dictionary `parameters` with keys and values that represent parameters for a machine learning model
    # The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Create another dictionary `test_json` with two keys: "input_data" and "params"
    # The value of "input_data" is another dictionary with keys "input_string" and "parameters"
    # The value of "input_string" is a list containing the first message from the `test_df` DataFrame
    # The value of "parameters" is the `parameters` dictionary created earlier
    # The value of "params" is an empty dictionary
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Open a file named `sample_score.json` in the `./ultrachat_200k_dataset` directory in write mode
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Write the `test_json` dictionary to the file in JSON format using the `json.dump` function
        json.dump(test_json, f)
    ```

### 엔드포인트 호출하기

1. 이 Python 스크립트는 Azure Machine Learning의 온라인 엔드포인트를 호출해 JSON 파일을 평가합니다. 주요 내용은 다음과 같습니다:

   - workspace_ml_client 객체의 online_endpoints 속성의 invoke 메서드를 호출합니다. 이 메서드는 온라인 엔드포인트에 요청을 보내고 응답을 받는 데 사용됩니다.

   - endpoint_name과 deployment_name 인수로 엔드포인트 이름과 배포 이름을 지정합니다. 이 경우 엔드포인트 이름은 online_endpoint_name 변수에 저장되어 있고, 배포 이름은 "demo"입니다.

   - request_file 인수로 평가할 JSON 파일 경로를 지정합니다. 이 경우 파일은 ./ultrachat_200k_dataset/sample_score.json입니다.

   - 엔드포인트 응답을 response 변수에 저장합니다.

   - 원시 응답을 출력합니다.

1. 요약하자면, 이 스크립트는 Azure Machine Learning의 온라인 엔드포인트를 호출해 JSON 파일을 평가하고 응답을 출력합니다.

```python
    # Invoke the online endpoint in Azure Machine Learning to score the `sample_score.json` file
    # The `invoke` method of the `online_endpoints` property of the `workspace_ml_client` object is used to send a request to an online endpoint and get a response
    # The `endpoint_name` argument specifies the name of the endpoint, which is stored in the `online_endpoint_name` variable
    # The `deployment_name` argument specifies the name of the deployment, which is "demo"
    # The `request_file` argument specifies the path to the JSON file to be scored, which is `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Print the raw response from the endpoint
    print("raw response: \n", response, "\n")
    ```

## 9. 온라인 엔드포인트 삭제하기

1. 온라인 엔드포인트를 삭제하지 않으면 엔드포인트가 사용하는 컴퓨팅 자원에 대한 과금이 계속 발생합니다. 이 Python 코드는 Azure Machine Learning에서 온라인 엔드포인트를 삭제합니다. 주요 내용은 다음과 같습니다:

   - workspace_ml_client 객체의 online_endpoints 속성의 begin_delete 메서드를 호출해 온라인 엔드포인트 삭제를 시작합니다.

   - name 인수로 삭제할 엔드포인트 이름을 지정합니다. 이 경우 online_endpoint_name 변수에 저장된 이름입니다.

   - wait 메서드를 호출해 삭제 작업이 완료될 때까지 대기합니다. 이 작업은 블로킹이며, 삭제가 완료될 때까지 스크립트가 진행되지 않습니다.

1. 요약하자면, 이 코드는 Azure Machine Learning에서 온라인 엔드포인트 삭제를 시작하고 작업 완료를 기다립니다.

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.