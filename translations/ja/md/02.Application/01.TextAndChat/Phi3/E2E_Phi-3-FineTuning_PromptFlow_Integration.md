<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7ca2c30fdb802664070e9cfbf92e24fe",
  "translation_date": "2026-01-05T01:11:59+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "ja"
}
-->
# Phi-3 カスタムモデルをファインチューニングして Prompt flow と統合する

このエンドツーエンド (E2E) サンプルは、Microsoft Tech Community のガイド「"[Phi-3 カスタムモデルを Prompt Flow とファインチューニングおよび統合する: ステップバイステップガイド](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)"」に基づいています。ファインチューニング、デプロイ、Prompt flow との統合という Phi-3 カスタムモデルのプロセスを紹介します。

## 概要

この E2E サンプルでは、Phi-3 モデルをファインチューニングし、Prompt flow と統合する方法を学びます。Azure Machine Learning と Prompt flow を活用して、カスタム AI モデルをデプロイおよび利用するためのワークフローを確立します。この E2E サンプルは 3 つのシナリオに分かれています:

**シナリオ 1: Azure リソースのセットアップとファインチューニングの準備**

**シナリオ 2: Phi-3 モデルのファインチューニングと Azure Machine Learning Studio へのデプロイ**

**シナリオ 3: Prompt flow と統合しカスタムモデルとチャットする**

ここにこの E2E サンプルの概要があります。

![Phi-3 ファインチューニング_PromptFlow_統合 概要](../../../../../../translated_images/00-01-architecture.02fc569e266d468c.ja.png)

### Table of Contents

1. **[シナリオ 1: Azure リソースのセットアップとファインチューニングの準備](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning ワークスペースの作成](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Azure サブスクリプションで GPU クォータをリクエストする](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ロール割り当てを追加する](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [プロジェクトをセットアップする](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ファインチューニング用データセットの準備](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[シナリオ 2: Phi-3 モデルをファインチューニングし Azure Machine Learning Studio にデプロイする](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure CLI のセットアップ](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 モデルのファインチューニング](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ファインチューニング済みモデルのデプロイ](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[シナリオ 3: Prompt flow と統合してカスタムモデルとチャットする](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [カスタム Phi-3 モデルを Prompt flow と統合する](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [カスタムモデルとチャットする](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## シナリオ 1: Azure リソースのセットアップとファインチューニングの準備

### Azure Machine Learning ワークスペースの作成

1. ポータルページ上部の **検索バー** に *azure machine learning* と入力し、表示されるオプションから **Azure Machine Learning** を選択します。

    ![azure machine learning を入力](../../../../../../translated_images/01-01-type-azml.a5116f8454d98c60.ja.png)

1. ナビゲーションメニューから **+ Create** を選択します。

1. ナビゲーションメニューから **New workspace** を選択します。

    ![新しいワークスペースを選択する](../../../../../../translated_images/01-02-select-new-workspace.83e17436f8898dc4.ja.png)

1. 次の操作を行います:

    - 使用する Azure **Subscription** を選択します。
    - 使用する **Resource group** を選択します（必要に応じて新規作成）。
    - **Workspace Name** を入力します。固有の値でなければなりません。
    - 使用する **Region** を選択します。
    - 使用する **Storage account** を選択します（必要に応じて新規作成）。
    - 使用する **Key vault** を選択します（必要に応じて新規作成）。
    - 使用する **Application insights** を選択します（必要に応じて新規作成）。
    - 使用する **Container registry** を選択します（必要に応じて新規作成）。

    ![AZML を入力する](../../../../../../translated_images/01-03-fill-AZML.730a5177757bbebb.ja.png)

1. **Review + Create** を選択します。

1. **Create** を選択します。

### Azure サブスクリプションで GPU クォータをリクエストする

この E2E サンプルでは、ファインチューニングに *Standard_NC24ads_A100_v4 GPU* を使用します（クォータのリクエストが必要）。デプロイには *Standard_E4s_v3* CPU を使用します（クォータのリクエストは不要）。

> [!NOTE]
>
> GPU 割り当ての対象となるのは Pay-As-You-Go サブスクリプション（標準のサブスクリプションタイプ）のみで、特典付きサブスクリプションは現在サポートされていません。
>
> 特典付きサブスクリプション（例: Visual Studio Enterprise Subscription）を使用している場合や、ファインチューニングとデプロイのプロセスを手早くテストしたい場合は、CPU を用いた最小データセットでのファインチューニングについてのガイダンスも本チュートリアルで提供しています。ただし、より大きなデータセットと GPU を使用した場合のほうがファインチューニングの結果が大幅に向上する点に注意してください。

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. *Standard NCADSA100v4 Family* クォータをリクエストするために次の操作を行います:

    - 左側のタブから **Quota** を選択します。
    - 使用する **Virtual machine family** を選択します。たとえば *Standard NCADSA100v4 Family Cluster Dedicated vCPUs*（*Standard_NC24ads_A100_v4* GPU を含む）を選択します。
    - ナビゲーションメニューから **Request quota** を選択します。

        ![クォータをリクエスト](../../../../../../translated_images/01-04-request-quota.3d3670c3221ab834.ja.png)

    - Request quota ページで、使用したい **New cores limit** を入力します。例: 24。
    - Request quota ページで **Submit** を選択して GPU クォータをリクエストします。

> [!NOTE]
> 適切な GPU や CPU は [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) のドキュメントを参照して選択できます。

### ロール割り当ての追加

モデルをファインチューニングおよびデプロイするには、まず User Assigned Managed Identity (UAI) を作成し、適切なアクセス許可を割り当てる必要があります。この UAI はデプロイ時の認証に使用されます。

#### ユーザー割り当てマネージド ID (UAI) の作成

1. ポータルページ上部の **検索バー** に *managed identities* と入力し、表示されるオプションから **Managed Identities** を選択します。

    ![managed identities を入力](../../../../../../translated_images/01-05-type-managed-identities.9297b6039874eff8.ja.png)

1. **+ Create** を選択します。

    ![Create を選択する](../../../../../../translated_images/01-06-select-create.936d8d66d7144f9a.ja.png)

1. 次の操作を行います:

    - 使用する Azure **Subscription** を選択します。
    - 使用する **Resource group** を選択します（必要に応じて新規作成）。
    - 使用する **Region** を選択します。
    - **Name** を入力します。固有の値でなければなりません。

1. **Review + create** を選択します。

1. **+ Create** を選択します。

#### Managed Identity に Contributor ロールを追加する

1. 作成した Managed Identity リソースに移動します。

1. 左側のタブから **Azure role assignments** を選択します。

1. ナビゲーションメニューから **+Add role assignment** を選択します。

1. Add role assignment ページ内で次の操作を行います:
    - **Scope** を **Resource group** に設定します。
    - 使用する Azure **Subscription** を選択します。
    - 使用する **Resource group** を選択します。
    - **Role** を **Contributor** に設定します。

    ![Contributor ロールを入力する](../../../../../../translated_images/01-07-fill-contributor-role.29ca99b7c9f687e0.ja.png)

1. **Save** を選択します。

#### Managed Identity に Storage Blob Data Reader ロールを追加する

1. ポータルページ上部の **検索バー** に *storage accounts* と入力し、表示されるオプションから **Storage accounts** を選択します。

    ![storage accounts を入力](../../../../../../translated_images/01-08-type-storage-accounts.1186c8e42933e49b.ja.png)

1. Azure Machine Learning ワークスペースに関連付けられたストレージアカウントを選択します。例: *finetunephistorage*。

1. Add role assignment ページに移動するために次の操作を行います:

    - 作成した Azure Storage アカウントに移動します。
    - 左側のタブから **Access Control (IAM)** を選択します。
    - ナビゲーションメニューから **+ Add** を選択します。
    - ナビゲーションメニューから **Add role assignment** を選択します。

    ![ロールを追加する](../../../../../../translated_images/01-09-add-role.d2db22fec1b187f0.ja.png)

1. Add role assignment ページ内で次の操作を行います:

    - Role ページの検索バーに *Storage Blob Data Reader* と入力し、表示されるオプションから **Storage Blob Data Reader** を選択します。
    - Role ページで **Next** を選択します。
    - Members ページで **Assign access to** を **Managed identity** に設定します。
    - Members ページで **+ Select members** を選択します。
    - Select managed identities ページで使用する Azure **Subscription** を選択します。
    - Select managed identities ページで **Managed identity** を選択します。
    - Select managed identities ページで作成した Managed Identity を選択します。例: *finetunephi-managedidentity*。
    - Select managed identities ページで **Select** を選択します。

    ![マネージド ID を選択する](../../../../../../translated_images/01-10-select-managed-identity.5ce5ba181f72a4df.ja.png)

1. **Review + assign** を選択します。

#### Managed Identity に AcrPull ロールを追加する

1. ポータルページ上部の **検索バー** に *container registries* と入力し、表示されるオプションから **Container registries** を選択します。

    ![container registries を入力](../../../../../../translated_images/01-11-type-container-registries.ff3b8bdc49dc596c.ja.png)

1. Azure Machine Learning ワークスペースに関連付けられたコンテナ レジストリを選択します。例: *finetunephicontainerregistries*

1. Add role assignment ページに移動するために次の操作を行います:

    - 左側のタブから **Access Control (IAM)** を選択します。
    - ナビゲーションメニューから **+ Add** を選択します。
    - ナビゲーションメニューから **Add role assignment** を選択します。

1. Add role assignment ページ内で次の操作を行います:

    - Role ページの検索バーに *AcrPull* と入力し、表示されるオプションから **AcrPull** を選択します。
    - Role ページで **Next** を選択します。
    - Members ページで **Assign access to** を **Managed identity** に設定します。
    - Members ページで **+ Select members** を選択します。
    - Select managed identities ページで使用する Azure **Subscription** を選択します。
    - Select managed identities ページで **Managed identity** を選択します。
    - Select managed identities ページで作成した Managed Identity を選択します。例: *finetunephi-managedidentity*。
    - Select managed identities ページで **Select** を選択します。
    - **Review + assign** を選択します。

### プロジェクトのセットアップ

ここからは、作業用フォルダーを作成し、仮想環境をセットアップして、ユーザーと対話し Azure Cosmos DB に保存されたチャット履歴を参照して応答を生成するプログラムを開発します。

#### 作業用フォルダーの作成

1. ターミナル ウィンドウを開き、デフォルトのパスに *finetune-phi* という名前のフォルダーを作成するには、次のコマンドを入力します。

    ```console
    mkdir finetune-phi
    ```

1. 作成した *finetune-phi* フォルダーに移動するには、ターミナルで次のコマンドを入力します。

    ```console
    cd finetune-phi
    ```

#### 仮想環境の作成

1. *.venv* という名前の仮想環境を作成するには、ターミナルで次のコマンドを入力します。

    ```console
    python -m venv .venv
    ```

1. 仮想環境を有効化するには、ターミナルで次のコマンドを入力します。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> 正しく実行されていれば、コマンドプロンプトの前に *(.venv)* が表示されます。

#### 必要なパッケージのインストール

1. 必要なパッケージをインストールするには、ターミナルで次のコマンドを入力します。

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### プロジェクト ファイルの作成
In this演習では、プロジェクトに必要なファイルを作成します。これらのファイルには、データセットのダウンロード、Azure Machine Learning 環境の設定、Phi-3 モデルのファインチューニング、ファインチューニング済みモデルのデプロイ用のスクリプトが含まれます。ファインチューニング環境を設定するための *conda.yml* ファイルも作成します。

この演習では、次のことを行います:

- *download_dataset.py* ファイルを作成してデータセットをダウンロードします。
- *setup_ml.py* ファイルを作成して Azure Machine Learning 環境を設定します。
- *finetuning_dir* フォルダー内に *fine_tune.py* ファイルを作成し、データセットを使用して Phi-3 モデルをファインチューニングします。
- ファインチューニング環境を設定するための *conda.yml* ファイルを作成します。
- ファインチューニング済みモデルをデプロイするための *deploy_model.py* ファイルを作成します。
- ファインチューニング済みモデルを Prompt flow と統合して実行するための *integrate_with_promptflow.py* ファイルを作成します。
- Prompt flow のワークフロー構造を設定するための flow.dag.yml ファイルを作成します。
- Azure 情報を入力するための *config.py* ファイルを作成します。

> [!NOTE]
>
> 完成したフォルダー構成:
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

1. **Visual Studio Code** を開きます。

1. メニューバーから **File** を選択します。

1. **Open Folder** を選択します。

1. 作成した *finetune-phi* フォルダーを選択します。フォルダーは *C:\Users\yourUserName\finetune-phi* にあります。

    ![プロジェクトフォルダーを開く。](../../../../../../translated_images/01-12-open-project-folder.1fff9c7f41dd1639.ja.png)

1. Visual Studio Code の左ペインで右クリックし、**New File** を選択して *download_dataset.py* という新しいファイルを作成します。

1. Visual Studio Code の左ペインで右クリックし、**New File** を選択して *setup_ml.py* という新しいファイルを作成します。

1. Visual Studio Code の左ペインで右クリックし、**New File** を選択して *deploy_model.py* という新しいファイルを作成します。

    ![新しいファイルを作成します。](../../../../../../translated_images/01-13-create-new-file.c17c150fff384a39.ja.png)

1. Visual Studio Code の左ペインで右クリックし、**New Folder** を選択して *finetuning_dir* という名前の新しいフォルダーを作成します。

1. *finetuning_dir* フォルダー内に *fine_tune.py* という新しいファイルを作成します。

#### Create and Configure *conda.yml* file

1. Visual Studio Code の左ペインで右クリックし、**New File** を選択して *conda.yml* という名前の新しいファイルを作成します。

1. Phi-3 モデルのファインチューニング環境を設定するために、次のコードを *conda.yml* ファイルに追加します。

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

#### Create and Configure *config.py* file

1. Visual Studio Code の左ペインで右クリックし、**New File** を選択して *config.py* という名前の新しいファイルを作成します。

1. Azure 情報を含めるために、次のコードを *config.py* ファイルに追加します。

    ```python
    # Azure の設定
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Azure Machine Learning の設定
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Azure マネージド ID の設定
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # データセットのファイルパス
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # 微調整済みモデルの設定
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### Add Azure environment variables

1. Azure サブスクリプション ID を追加するには、次の手順を実行します:

    - ポータル ページ上部の **検索バー** に *subscriptions* と入力し、表示されるオプションから **Subscriptions** を選択します。
    - 現在使用している Azure サブスクリプションを選択します。
    - サブスクリプション ID をコピーして *config.py* ファイルに貼り付けます。

    ![サブスクリプション ID を見つける。](../../../../../../translated_images/01-14-find-subscriptionid.4f4ca33555f1e637.ja.png)

1. Azure ワークスペース名を追加するには、次の手順を実行します:

    - 作成した Azure Machine Learning リソースに移動します。
    - アカウント名をコピーして *config.py* ファイルに貼り付けます。

    ![Azure Machine Learning の名前を見つける。](../../../../../../translated_images/01-15-find-AZML-name.1975f0422bca19a7.ja.png)

1. Azure リソース グループ名を追加するには、次の手順を実行します:

    - 作成した Azure Machine Learning リソースに移動します。
    - Azure リソース グループ名をコピーして *config.py* ファイルに貼り付けます。

    ![リソースグループ名を見つける。](../../../../../../translated_images/01-16-find-AZML-resourcegroup.855a349d0af134a3.ja.png)

2. Azure マネージド ID 名を追加するには、次の手順を実行します:

    - 作成した Managed Identities リソースに移動します。
    - Azure マネージド ID 名をコピーして *config.py* ファイルに貼り付けます。

    ![UAI を見つける。](../../../../../../translated_images/01-17-find-uai.3529464f53499827.ja.png)

### Prepare dataset for fine-tuning

この演習では、*download_dataset.py* ファイルを実行して *ULTRACHAT_200k* データセットをローカル環境にダウンロードします。次に、このデータセットを使用して Azure Machine Learning で Phi-3 モデルをファインチューニングします。

#### Download your dataset using *download_dataset.py*

1. Visual Studio Code で *download_dataset.py* ファイルを開きます。

1. 次のコードを *download_dataset.py* に追加します。

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
        # 指定された名前、構成、および分割比率でデータセットを読み込む
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # データセットを訓練用とテスト用に分割する（訓練80%、テスト20%）
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # 存在しない場合はディレクトリを作成する
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # 書き込みモードでファイルを開く
        with open(filepath, 'w', encoding='utf-8') as f:
            # データセット内の各レコードを反復処理する
            for record in dataset:
                # レコードをJSONオブジェクトとしてダンプしてファイルに書き込む
                json.dump(record, f)
                # レコードを区切るために改行文字を書き込む
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # 特定の構成と分割比率でULTRACHAT_200kデータセットを読み込み、分割する
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # 分割から訓練用とテスト用のデータセットを抽出する
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # 訓練データセットをJSONLファイルに保存する
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # テストデータセットを別のJSONLファイルに保存する
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **CPU を使用して最小限のデータセットでファインチューニングするためのガイダンス**
>
> CPU を使用してファインチューニングを行う場合、このアプローチは（Visual Studio Enterprise Subscription などの）ベネフィット サブスクリプションをお持ちの方や、ファインチューニングとデプロイのプロセスを素早くテストしたい方に適しています。
>
> `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` を `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')` に置き換えてください。
>

1. ターミナルで次のコマンドを入力してスクリプトを実行し、データセットをローカル環境にダウンロードします。

    ```console
    python download_data.py
    ```

1. データセットがローカルの *finetune-phi/data* ディレクトリに正しく保存されたことを確認します。

> [!NOTE]
>
> **データセットのサイズとファインチューニング時間**
>
> この E2E サンプルでは、データセットの 1%（`train_sft[:1%]`）のみを使用しています。これによりデータ量が大幅に削減され、アップロードとファインチューニングの両方が高速化されます。トレーニング時間とモデル性能のバランスを見つけるために、パーセンテージを調整できます。データセットのサブセットを小さくすることで、ファインチューニングに必要な時間が短くなり、E2E サンプルとして扱いやすくなります。

## Scenario 2: Fine-tune Phi-3 model and Deploy in Azure Machine Learning Studio

### Set up Azure CLI

Azure CLI を設定して環境を認証する必要があります。Azure CLI によりコマンドラインから Azure リソースを管理でき、Azure Machine Learning がこれらのリソースにアクセスするために必要な資格情報が提供されます。開始するには [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) をインストールしてください

1. ターミナル ウィンドウを開き、Azure アカウントにログインするために次のコマンドを入力します。

    ```console
    az login
    ```

1. 使用する Azure アカウントを選択します。

1. 使用する Azure サブスクリプションを選択します。

    ![リソースグループ名を見つける。](../../../../../../translated_images/02-01-login-using-azure-cli.dfde31cb75e58a87.ja.png)

> [!TIP]
>
> サインインに問題がある場合は、デバイスコードを使用してみてください。ターミナル ウィンドウを開き、Azure アカウントにサインインするために次のコマンドを入力します:
>
> ```console
> az login --use-device-code
> ```
>

### Fine-tune the Phi-3 model

この演習では、提供されたデータセットを使用して Phi-3 モデルをファインチューニングします。まず、*fine_tune.py* ファイル内でファインチューニングのプロセスを定義します。次に、Azure Machine Learning 環境を構成し、*setup_ml.py* ファイルを実行してファインチューニング プロセスを開始します。このスクリプトは、ファインチューニングが Azure Machine Learning 環境内で行われるようにします。

*setup_ml.py* を実行すると、Azure Machine Learning 環境でファインチューニング プロセスが実行されます。

#### Add code to the *fine_tune.py* file

1. *finetuning_dir* フォルダーに移動し、Visual Studio Code で *fine_tune.py* ファイルを開きます。

1. 次のコードを *fine_tune.py* に追加します。

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

    # MLflowでINVALID_PARAMETER_VALUEエラーを回避するには、MLflow統合を無効にしてください
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # ログの設定
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

1. *fine_tune.py* ファイルを保存して閉じます。

> [!TIP]
> **Phi-3.5 モデルをファインチューニングすることもできます**
>
> *fine_tune.py* ファイル内で、`pretrained_model_name` を `"microsoft/Phi-3-mini-4k-instruct"` から任意のモデル名に変更できます。たとえば、`"microsoft/Phi-3.5-mini-instruct"` に変更すると、Phi-3.5-mini-instruct モデルをファインチューニングに使用します。使用したいモデル名を探すには、[Hugging Face](https://huggingface.co/) を訪問し、興味のあるモデルを検索して、その名前を `pretrained_model_name` フィールドにコピーして貼り付けてください。
>
> <image type="content" src="../../../../imgs/02/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Phi-3.5 のファインチューニング。">
>

#### Add code to the *setup_ml.py* file

1. Visual Studio Code で *setup_ml.py* ファイルを開きます。

1. 次のコードを *setup_ml.py* に追加します。

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

    # 定数

    # トレーニングにCPUインスタンスを使用するには、以下の行のコメントを外してください
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # CPU を使用
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # トレーニングにGPUインスタンスを使用するには、以下の行のコメントを外してください
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # コンピュート クラスターの場所に置き換えてください
    FINETUNING_DIR = "./finetuning_dir" # ファインチューニングスクリプトへのパス
    TRAINING_ENV_NAME = "phi-3-training-environment" # トレーニング環境の名前
    MODEL_OUTPUT_DIR = "./model_output" # Azure ML のモデル出力ディレクトリへのパス

    # プロセスを追跡するためのログ設定
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
            image=DOCKER_IMAGE_NAME,  # 環境用の Docker イメージ
            conda_file=CONDA_FILE,  # Conda 環境ファイル
            name=TRAINING_ENV_NAME,  # 環境の名前
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
                tier="Dedicated",  # コンピュート クラスターの階層
                min_instances=0,  # インスタンスの最小数
                max_instances=1  # インスタンスの最大数
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # クラスターが作成されるまで待機する
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # fine_tune.py へのパス
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # トレーニング環境
            compute=compute_name,  # 使用するコンピュート クラスター
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # トレーニングデータファイルへのパス
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # 評価データファイルへのパス
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # ML クライアントを初期化する
        ml_client = get_ml_client()

        # 環境を作成する
        env = create_or_get_environment(ml_client)
        
        # コンピュート クラスターを作成するか既存のものを取得する
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # ファインチューニング ジョブを作成して送信する
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # ジョブを送信する
        ml_client.jobs.stream(returned_job.name)  # ジョブのログをストリーミングする
        
        # ジョブ名を取得する
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. `COMPUTE_INSTANCE_TYPE`、`COMPUTE_NAME`、および `LOCATION` をご自身の詳細に置き換えます。

    ```python
   # トレーニングでGPUインスタンスを使用するには、次の行のコメントを外してください
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # 計算クラスターの場所に置き換えてください
    ```

> [!TIP]
>
> **CPU を使用して最小限のデータセットでファインチューニングするためのガイダンス**
>
> CPU を使用してファインチューニングを行う場合、このアプローチは（Visual Studio Enterprise Subscription などの）ベネフィット サブスクリプションをお持ちの方や、ファインチューニングとデプロイのプロセスを素早くテストしたい方に適しています。
>
> 1. *setup_ml* ファイルを開きます。
> 1. `COMPUTE_INSTANCE_TYPE`、`COMPUTE_NAME`、および `DOCKER_IMAGE_NAME` を次の値に置き換えます。*Standard_E16s_v3* にアクセスできない場合は、同等の CPU インスタンスを使用するか、新しいクォータを要求してください。
> 1. `LOCATION` をご自身の詳細に置き換えます。
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. *setup_ml.py* スクリプトを実行して Azure Machine Learning でファインチューニング プロセスを開始するには、次のコマンドを入力します。

    ```python
    python setup_ml.py
    ```

1. この演習では、Azure Machine Learning を使用して Phi-3 モデルのファインチューニングに成功しました。*setup_ml.py* スクリプトを実行することで、Azure Machine Learning 環境を設定し、*fine_tune.py* ファイルで定義されたファインチューニング プロセスを開始しました。ファインチューニングはかなりの時間がかかることがある点にご注意ください。`python setup_ml.py` コマンドを実行した後は、プロセスが完了するまで待つ必要があります。ファインチューニング ジョブのステータスは、ターミナルに表示されるリンクから Azure Machine Learning ポータルで確認できます。

    ![ファインチューニング ジョブを確認します。](../../../../../../translated_images/02-02-see-finetuning-job.59393bc3b143871e.ja.png)

### Deploy the fine-tuned model

Prompt Flow とファインチューニング済みの Phi-3 モデルを統合するには、モデルをリアルタイム推論用にアクセス可能な状態でデプロイする必要があります。このプロセスには、モデルの登録、オンライン エンドポイントの作成、およびモデルのデプロイが含まれます。

#### Set the model name, endpoint name, and deployment name for deployment

1. *config.py* ファイルを開きます。

1. `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` を希望するモデル名に置き換えます。

1. `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` を希望するエンドポイント名に置き換えます。

1. `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` を希望するデプロイ名に置き換えます。

#### Add code to the *deploy_model.py* file

*deploy_model.py* ファイルを実行すると、デプロイ プロセス全体が自動化されます。これにより、モデルが登録され、エンドポイントが作成され、config.py ファイルに指定された設定（モデル名、エンドポイント名、デプロイ名）に基づいてデプロイが実行されます。

1. Visual Studio Code で *deploy_model.py* ファイルを開きます。

1. 次のコードを *deploy_model.py* に追加します。

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # 設定のインポート
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

    # 定数
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # ログの設定
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
            # 現在のエンドポイントの詳細を取得する
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # デバッグのために現在のトラフィック割り当てをログに記録する
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # デプロイメントのトラフィック割り当てを設定する
            endpoint.traffic = {deployment_name: 100}
            
            # 新しいトラフィック割り当てでエンドポイントを更新する
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # デバッグのために更新されたトラフィック割り当てをログに記録する
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # 処理中に発生したエラーをログに記録する
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

1. `JOB_NAME` を取得するには、次の手順を実行します:

    - 作成した Azure Machine Learning リソースに移動します。
    - **Studio web URL** を選択して Azure Machine Learning ワークスペースを開きます。
    - 左側のタブから **Jobs** を選択します。
    - ファインチューニング用の実験（例: *finetunephi*）を選択します。
    - 作成したジョブを選択します。
    - ジョブ名をコピーして、*deploy_model.py* ファイル内の `JOB_NAME = "your-job-name"` に貼り付けます。

1. `COMPUTE_INSTANCE_TYPE` をあなたの環境に合わせて置き換えます。

1. 次のコマンドを入力して *deploy_model.py* スクリプトを実行し、Azure Machine Learning でデプロイを開始します。

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> 追加の料金が発生しないように、作成したエンドポイントを Azure Machine Learning ワークスペースで削除することを確認してください。
>

#### Azure Machine Learning ワークスペースでデプロイの状態を確認する

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. **Studio の Web URL** を選択して Azure Machine Learning ワークスペースを開きます。

1. 左側のタブから **エンドポイント** を選択します。

    ![エンドポイントを選択します。](../../../../../../translated_images/02-03-select-endpoints.c3136326510baff1.ja.png)

2. 作成したエンドポイントを選択します。

    ![作成したエンドポイントを選択します。](../../../../../../translated_images/02-04-select-endpoint-created.0363e7dca51dabb4.ja.png)

3. このページで、デプロイプロセス中に作成されたエンドポイントを管理できます。

## シナリオ 3: Prompt flow と統合し、カスタムモデルとチャットする

### カスタム Phi-3 モデルを Prompt flow と統合する

ファインチューニングしたモデルのデプロイが正常に完了したら、Prompt flow と統合してリアルタイムアプリケーションでモデルを使用できるようになります。これにより、カスタム Phi-3 モデルを使ったさまざまなインタラクティブなタスクが可能になります。

#### ファインチューニングした Phi-3 モデルの API キーとエンドポイント URI を設定する

1. 作成した Azure Machine Learning ワークスペースに移動します。
1. 左側のタブから **エンドポイント** を選択します。
1. 作成したエンドポイントを選択します。
1. ナビゲーションメニューから **使用** を選択します。
1. **REST エンドポイント** をコピーして *config.py* ファイルに貼り付け、`AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` をあなたの **REST エンドポイント** に置き換えます。
1. **プライマリ キー** をコピーして *config.py* ファイルに貼り付け、`AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` をあなたの **プライマリ キー** に置き換えます。

    ![API キーとエンドポイント URI をコピーします。](../../../../../../translated_images/02-05-copy-apikey-endpoint.88b5a92e6462c53b.ja.png)

#### *flow.dag.yml* ファイルにコードを追加する

1. Visual Studio Code で *flow.dag.yml* ファイルを開きます。

1. 次のコードを *flow.dag.yml* に追加します。

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

#### *integrate_with_promptflow.py* ファイルにコードを追加する

1. Visual Studio Code で *integrate_with_promptflow.py* ファイルを開きます。

1. 次のコードを *integrate_with_promptflow.py* に追加します。

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

    # ロギングの設定
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

### カスタムモデルとチャットする

1. 次のコマンドを入力して *deploy_model.py* スクリプトを実行し、Azure Machine Learning でデプロイを開始します。

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. 結果の例は次のとおりです: これでカスタム Phi-3 モデルとチャットできます。ファインチューニングに使用したデータに基づいた質問をすることを推奨します。

    ![Prompt flow の例。](../../../../../../translated_images/02-06-promptflow-example.89384abaf3ad71f6.ja.png)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責事項：
この文書は AI 翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を用いて翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な箇所が含まれる場合があることにご注意ください。原文（原言語の文書）が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因するいかなる誤解や誤訳についても、当社は責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->