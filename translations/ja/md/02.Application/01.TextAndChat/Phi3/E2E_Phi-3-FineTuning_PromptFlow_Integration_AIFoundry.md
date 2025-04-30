<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ed86d361ac6d4cc8bfb47428e6a2a247",
  "translation_date": "2025-04-04T12:38:48+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "ja"
}
-->
# Phi-3モデルをAzure AI FoundryのPrompt flowでカスタマイズ・統合する方法

このエンドツーエンド（E2E）サンプルは、Microsoft Tech Communityのガイド「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)」に基づいています。Azure AI FoundryでPrompt flowを活用し、カスタムPhi-3モデルを微調整、デプロイ、統合するプロセスを紹介します。ローカル環境でコードを実行するE2Eサンプル「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)」とは異なり、このチュートリアルではAzure AI / ML Studio内でモデルを完全に微調整・統合することに焦点を当てています。

## 概要

このE2Eサンプルでは、Phi-3モデルを微調整し、Azure AI FoundryのPrompt flowに統合する方法を学びます。Azure AI / ML Studioを活用して、カスタムAIモデルをデプロイ・利用するワークフローを確立します。このE2Eサンプルは以下の3つのシナリオに分かれています：

**シナリオ1: Azureリソースのセットアップと微調整準備**

**シナリオ2: Phi-3モデルを微調整し、Azure Machine Learning Studioでデプロイ**

**シナリオ3: Prompt flowに統合し、Azure AI Foundryでカスタムモデルとチャット**

以下はこのE2Eサンプルの概要です。

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.ja.png)

### 目次

1. **[シナリオ1: Azureリソースのセットアップと微調整準備](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning Workspaceを作成](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [AzureサブスクリプションでGPUクォータをリクエスト](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ロール割り当てを追加](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [プロジェクトをセットアップ](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [微調整用データセットの準備](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[シナリオ2: Phi-3モデルを微調整し、Azure Machine Learning Studioでデプロイ](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3モデルを微調整](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [微調整したPhi-3モデルをデプロイ](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[シナリオ3: Prompt flowに統合し、Azure AI Foundryでカスタムモデルとチャット](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [カスタムPhi-3モデルをPrompt flowに統合](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [カスタムPhi-3モデルとチャット](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## シナリオ1: Azureリソースのセットアップと微調整準備

### Azure Machine Learning Workspaceを作成

1. ポータルページ上部の**検索バー**に「*azure machine learning*」と入力し、表示されたオプションから**Azure Machine Learning**を選択します。

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.ja.png)

2. ナビゲーションメニューから**+ Create**を選択します。

3. ナビゲーションメニューから**New workspace**を選択します。

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.ja.png)

4. 以下のタスクを実行します：

    - Azure **Subscription**を選択。
    - 使用する**Resource group**を選択（必要に応じて新規作成）。
    - **Workspace Name**を入力（一意の値である必要があります）。
    - 使用する**Region**を選択。
    - 使用する**Storage account**を選択（必要に応じて新規作成）。
    - 使用する**Key vault**を選択（必要に応じて新規作成）。
    - 使用する**Application insights**を選択（必要に応じて新規作成）。
    - 使用する**Container registry**を選択（必要に応じて新規作成）。

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.ja.png)

5. **Review + Create**を選択します。

6. **Create**を選択します。

### AzureサブスクリプションでGPUクォータをリクエスト

このチュートリアルでは、GPUを使用してPhi-3モデルを微調整およびデプロイします。微調整には*Standard_NC24ads_A100_v4* GPUを使用し、デプロイには*Standard_NC6s_v3* GPUを使用します。これらのGPUにはクォータリクエストが必要です。

> [!NOTE]
>
> GPU割り当てが可能なのはPay-As-You-Goサブスクリプション（標準的なサブスクリプションタイプ）のみです。特典付きサブスクリプションは現在サポートされていません。
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)を訪問します。

1. 以下のタスクを実行して*Standard NCADSA100v4 Family*のクォータをリクエストします：

    - 左側のタブから**Quota**を選択。
    - 使用する**Virtual machine family**を選択。例えば、**Standard NCADSA100v4 Family Cluster Dedicated vCPUs**を選択し、*Standard_NC24ads_A100_v4* GPUを含めます。
    - ナビゲーションメニューから**Request quota**を選択。

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.ja.png)

    - Request quotaページ内で、使用したい**New cores limit**を入力。例えば、24。
    - Request quotaページ内で**Submit**を選択してGPUクォータをリクエスト。

1. 以下のタスクを実行して*Standard NCSv3 Family*のクォータをリクエストします：

    - 左側のタブから**Quota**を選択。
    - 使用する**Virtual machine family**を選択。例えば、**Standard NCSv3 Family Cluster Dedicated vCPUs**を選択し、*Standard_NC6s_v3* GPUを含めます。
    - ナビゲーションメニューから**Request quota**を選択。
    - Request quotaページ内で、使用したい**New cores limit**を入力。例えば、24。
    - Request quotaページ内で**Submit**を選択してGPUクォータをリクエスト。

### ロール割り当てを追加

モデルの微調整とデプロイを行うには、まずUser Assigned Managed Identity（UAI）を作成し、適切な権限を割り当てる必要があります。このUAIはデプロイ中の認証に使用されます。

#### User Assigned Managed Identity(UAI)を作成

1. ポータルページ上部の**検索バー**に「*managed identities*」と入力し、表示されたオプションから**Managed Identities**を選択します。

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.ja.png)

1. **+ Create**を選択します。

    ![Select create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.ja.png)

1. 以下のタスクを実行します：

    - Azure **Subscription**を選択。
    - 使用する**Resource group**を選択（必要に応じて新規作成）。
    - 使用する**Region**を選択。
    - **Name**を入力（一意の値である必要があります）。

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.ja.png)

1. **Review + create**を選択します。

1. **+ Create**を選択します。

#### Managed IdentityにContributorロール割り当てを追加

1. 作成したManaged Identityリソースに移動します。

1. 左側のタブから**Azure role assignments**を選択します。

1. ナビゲーションメニューから**+Add role assignment**を選択します。

1. Add role assignmentページ内で以下のタスクを実行します：
    - **Scope**を**Resource group**に設定。
    - Azure **Subscription**を選択。
    - 使用する**Resource group**を選択。
    - **Role**を**Contributor**に設定。

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.ja.png)

2. **Save**を選択します。

#### Managed IdentityにStorage Blob Data Readerロール割り当てを追加

1. ポータルページ上部の**検索バー**に「*storage accounts*」と入力し、表示されたオプションから**Storage accounts**を選択します。

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.ja.png)

1. 作成したAzure Machine Learning Workspaceに関連付けられたストレージアカウントを選択します。例えば、*finetunephistorage*。

1. Add role assignmentページに移動するため、以下のタスクを実行します：

    - 作成したAzureストレージアカウントに移動。
    - 左側のタブから**Access Control (IAM)**を選択。
    - ナビゲーションメニューから**+ Add**を選択。
    - ナビゲーションメニューから**Add role assignment**を選択。

    ![Add role.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.ja.png)

1. Add role assignmentページ内で以下のタスクを実行します：

    - Roleページ内で**Storage Blob Data Reader**を検索バーに入力し、表示されたオプションから**Storage Blob Data Reader**を選択。
    - Roleページ内で**Next**を選択。
    - Membersページ内で**Assign access to**を**Managed identity**に設定。
    - Membersページ内で**+ Select members**を選択。
    - Select managed identitiesページ内でAzure **Subscription**を選択。
    - Select managed identitiesページ内で**Managed identity**を**Manage Identity**に設定。
    - Select managed identitiesページ内で作成したManaged Identityを選択。例えば、*finetunephi-managedidentity*。
    - Select managed identitiesページ内で**Select**を選択。

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.ja.png)

1. **Review + assign**を選択します。

#### Managed IdentityにAcrPullロール割り当てを追加

1. ポータルページ上部の**検索バー**に「*container registries*」と入力し、表示されたオプションから**Container registries**を選択します。

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.ja.png)

1. 作成したAzure Machine Learning Workspaceに関連付けられたコンテナレジストリを選択します。例えば、*finetunephicontainerregistry*

1. Add role assignmentページに移動するため、以下のタスクを実行します：

    - 左側のタブから**Access Control (IAM)**を選択。
    - ナビゲーションメニューから**+ Add**を選択。
    - ナビゲーションメニューから**Add role assignment**を選択。

1. Add role assignmentページ内で以下のタスクを実行します：

    - Roleページ内で**AcrPull**を検索バーに入力し、表示されたオプションから**AcrPull**を選択。
    - Roleページ内で**Next**を選択。
    - Membersページ内で**Assign access to**を**Managed identity**に設定。
    - Membersページ内で**+ Select members**を選択。
    - Select managed identitiesページ内でAzure **Subscription**を選択。
    - Select managed identitiesページ内で**Managed identity**を**Manage Identity**に設定。
    - Select managed identitiesページ内で作成したManaged Identityを選択。例えば、*finetunephi-managedidentity*。
    - Select managed identitiesページ内で**Select**を選択。
    - **Review + assign**を選択。

### プロジェクトをセットアップ

微調整に必要なデータセットをダウンロードするため、ローカル環境をセットアップします。

この演習では以下を行います：

- 作業フォルダーを作成。
- 仮想環境を作成。
- 必要なパッケージをインストール。
- データセットをダウンロードする*download_dataset.py*ファイルを作成。

#### 作業フォルダーを作成

1. ターミナルウィンドウを開き、以下のコマンドを入力して、デフォルトのパスに*finetune-phi*という名前のフォルダーを作成します。

    ```console
    mkdir finetune-phi
    ```

2. 作成した*finetune-phi*フォルダーに移動するため、以下のコマンドをターミナルで入力します。

    ```console
    cd finetune-phi
    ```

#### 仮想環境を作成

1. 以下のコマンドをターミナルで入力して*.venv*という名前の仮想環境を作成します。

    ```console
    python -m venv .venv
    ```

2. 仮想環境を有効化するため、以下のコマンドをターミナルで入力します。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> 仮想環境が有効化されている場合、コマンドプロンプトの前に*（.venv）*が表示されます。

#### 必要なパッケージをインストール

1. 以下のコマンドをターミナルで入力して、必要なパッケージをインストールします。

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py`を作成

> [!NOTE]
> 完全なフォルダー構造：
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code**を開きます。

1. メニューバーから**File**を選択します。

1. **Open Folder**を選択します。

1. 作成した*finetune-phi*フォルダーを選択します（例：*C:\Users\yourUserName\finetune-phi*）。

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.ja.png)

1. Visual Studio Codeの左ペインで右クリックし、**New File**を選択して*download_dataset.py*という名前の新しいファイルを作成します。

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.ja.png)

### 微調整用データセットの準備

この演習では、*download_dataset.py*ファイルを実行して*ultrachat_200k*データセットをローカル環境にダウンロードします。このデータセットを使用して、Azure Machine LearningでPhi-3モデルを微調整します。

この演習では以下を行います：

- *download_dataset.py*ファイルにデータセットをダウンロードするコードを追加。
- *download_dataset.py*ファイルを実行してローカル環境にデータセットをダウンロード。

#### *download_dataset.py*を使用してデータセットをダウンロード

1. Visual Studio Codeで*download_dataset.py*ファイルを開きます。

1. *download_dataset.py*ファイルに以下のコードを追加します。

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

1. ターミナルで以下のコマンドを入力してスクリプトを実行し、データセットをローカル環境にダウンロードします。

    ```console
    python download_dataset.py
    ```

1. データセットがローカルの*finetune-phi/data*ディレクトリに正常に保存されていることを確認します。

> [!NOTE]
>
> #### データセットサイズと微調整時間に関する注意
>
> このチュートリアルでは、データセットの1％のみ（`split='train[:1%]'`）を使用します。これにより、データ量が
1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. 左側のタブから **Compute** を選択します。

1. ナビゲーションメニューから **Compute clusters** を選択します。

1. **+ New** を選択します。

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.ja.png)

1. 以下のタスクを実行します：

    - 使用する **Region** を選択します。
    - **Virtual machine tier** を **Dedicated** に設定します。
    - **Virtual machine type** を **GPU** に設定します。
    - **Virtual machine size** のフィルターを **Select from all options** に設定します。
    - **Virtual machine size** を **Standard_NC24ads_A100_v4** に設定します。

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.ja.png)

1. **Next** を選択します。

1. 以下のタスクを実行します：

    - **Compute name** を入力します。これは一意の値である必要があります。
    - **Minimum number of nodes** を **0** に設定します。
    - **Maximum number of nodes** を **1** に設定します。
    - **Idle seconds before scale down** を **120** に設定します。

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.ja.png)

1. **Create** を選択します。

#### Phi-3 モデルのファインチューニング

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. 作成した Azure Machine Learning ワークスペースを選択します。

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.ja.png)

1. 以下のタスクを実行します：

    - 左側のタブから **Model catalog** を選択します。
    - **検索バー**に *phi-3-mini-4k* と入力し、表示されるオプションから **Phi-3-mini-4k-instruct** を選択します。

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.ja.png)

1. ナビゲーションメニューから **Fine-tune** を選択します。

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.ja.png)

1. 以下のタスクを実行します：

    - **Select task type** を **Chat completion** に設定します。
    - **+ Select data** を選択して **Training data** をアップロードします。
    - Validation data のアップロードタイプを **Provide different validation data** に設定します。
    - **+ Select data** を選択して **Validation data** をアップロードします。

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.ja.png)

    > [!TIP]
    >
    > **Advanced settings** を選択すると、**learning_rate** や **lr_scheduler_type** などの設定をカスタマイズして、ファインチューニングプロセスを最適化することができます。

1. **Finish** を選択します。

1. この演習では、Azure Machine Learning を使用して Phi-3 モデルのファインチューニングに成功しました。ファインチューニングプロセスはかなりの時間がかかる場合があります。ジョブを実行した後は、完了するまで待つ必要があります。Azure Machine Learning ワークスペースの左側の **Jobs** タブに移動して、ファインチューニングジョブのステータスを確認できます。次のシリーズでは、ファインチューニング済みモデルをデプロイし、Prompt flow と統合します。

    ![See finetuning job.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.ja.png)

### ファインチューニング済み Phi-3 モデルのデプロイ

ファインチューニング済み Phi-3 モデルを Prompt flow と統合するには、モデルをデプロイしてリアルタイム推論にアクセスできるようにする必要があります。このプロセスには、モデルの登録、オンラインエンドポイントの作成、モデルのデプロイが含まれます。

この演習では以下を行います：

- Azure Machine Learning ワークスペースにファインチューニング済みモデルを登録する
- オンラインエンドポイントを作成する
- 登録したファインチューニング済み Phi-3 モデルをデプロイする

#### ファインチューニング済みモデルの登録

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. 作成した Azure Machine Learning ワークスペースを選択します。

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.ja.png)

1. 左側のタブから **Models** を選択します。
1. **+ Register** を選択します。
1. **From a job output** を選択します。

    ![Register model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.ja.png)

1. 作成したジョブを選択します。

    ![Select job.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.ja.png)

1. **Next** を選択します。

1. **Model type** を **MLflow** に設定します。

1. **Job output** が選択されていることを確認します。これは自動的に選択されるはずです。

    ![Select output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.ja.png)

2. **Next** を選択します。

3. **Register** を選択します。

    ![Select register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.ja.png)

4. 左側のタブから **Models** メニューに移動すると、登録済みモデルを確認できます。

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.ja.png)

#### ファインチューニング済みモデルのデプロイ

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

1. ナビゲーションメニューから **Real-time endpoints** を選択します。

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.ja.png)

1. **Create** を選択します。

1. 作成した登録済みモデルを選択します。

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.ja.png)

1. **Select** を選択します。

1. 以下のタスクを実行します：

    - **Virtual machine** を *Standard_NC6s_v3* に設定します。
    - 使用する **Instance count** を選択します（例：*1*）。
    - **Endpoint** を **New** に設定してエンドポイントを作成します。
    - **Endpoint name** を入力します。一意の値である必要があります。
    - **Deployment name** を入力します。一意の値である必要があります。

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.ja.png)

1. **Deploy** を選択します。

> [!WARNING]
> アカウントに追加料金が発生しないようにするために、Azure Machine Learning ワークスペースで作成したエンドポイントを削除してください。
>

#### Azure Machine Learning ワークスペースでデプロイ状況を確認

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

1. 作成したエンドポイントを選択します。

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.ja.png)

1. このページでは、デプロイプロセス中にエンドポイントを管理できます。

> [!NOTE]
> デプロイが完了したら、**Live traffic** が **100%** に設定されていることを確認してください。設定されていない場合は、**Update traffic** を選択してトラフィック設定を調整してください。トラフィックが 0% に設定されている場合、モデルをテストすることはできません。
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.ja.png)
>

## シナリオ 3: Prompt flow を統合し、Azure AI Foundry でカスタムモデルとチャットする

### Prompt flow を使ってカスタム Phi-3 モデルを統合する

ファインチューニング済みモデルを正常にデプロイした後は、Prompt Flow と統合してリアルタイムアプリケーションでモデルを使用できるようにします。これにより、カスタム Phi-3 モデルを使用したさまざまな対話型タスクが可能になります。

この演習では以下を行います：

- Azure AI Foundry Hub を作成する
- Azure AI Foundry Project を作成する
- Prompt flow を作成する
- ファインチューニング済み Phi-3 モデルのカスタム接続を追加する
- Prompt flow を設定してカスタム Phi-3 モデルとチャットする

> [!NOTE]
> Promptflow は Azure ML Studio を使用して統合することもできます。同じ統合プロセスを Azure ML Studio に適用できます。

#### Azure AI Foundry Hub を作成する

Project を作成する前に Hub を作成する必要があります。Hub はリソースグループのように機能し、Azure AI Foundry 内で複数の Project を整理および管理できます。

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) にアクセスします。

1. 左側のタブから **All hubs** を選択します。

1. ナビゲーションメニューから **+ New hub** を選択します。

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.ja.png)

1. 以下のタスクを実行します：

    - **Hub name** を入力します。一意の値である必要があります。
    - Azure **Subscription** を選択します。
    - 使用する **Resource group** を選択します（必要に応じて新しいものを作成します）。
    - 使用する **Location** を選択します。
    - 使用する **Connect Azure AI Services** を選択します（必要に応じて新しいものを作成します）。
    - **Connect Azure AI Search** を **Skip connecting** に設定します。

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.ja.png)

1. **Next** を選択します。

#### Azure AI Foundry Project を作成する

1. 作成した Hub で、左側のタブから **All projects** を選択します。

1. ナビゲーションメニューから **+ New project** を選択します。

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.ja.png)

1. **Project name** を入力します。一意の値である必要があります。

    ![Create project.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.ja.png)

1. **Create a project** を選択します。

#### ファインチューニング済み Phi-3 モデルのカスタム接続を追加する

カスタム Phi-3 モデルを Prompt flow と統合するには、モデルのエンドポイントとキーをカスタム接続に保存する必要があります。この設定により、Prompt flow 内でカスタム Phi-3 モデルにアクセスできるようになります。

#### ファインチューニング済み Phi-3 モデルの API キーとエンドポイント URI を設定する

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) にアクセスします。

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.ja.png)

1. 作成したエンドポイントを選択します。

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.ja.png)

1. ナビゲーションメニューから **Consume** を選択します。

1. **REST endpoint** と **Primary key** をコピーします。
![APIキーとエンドポイントURIをコピーします。](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.ja.png)

#### カスタム接続を追加する

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)にアクセスします。

1. 作成したAzure AI Foundryプロジェクトに移動します。

1. 作成したプロジェクト内で、左側のタブから**設定**を選択します。

1. **+ 新しい接続**を選択します。

    ![新しい接続を選択します。](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.ja.png)

1. ナビゲーションメニューから**カスタムキー**を選択します。

    ![カスタムキーを選択します。](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.ja.png)

1. 以下のタスクを実行します：

    - **+ キーと値のペアを追加**を選択します。
    - キー名には**endpoint**を入力し、Azure ML Studioからコピーしたエンドポイントを値フィールドに貼り付けます。
    - 再度**+ キーと値のペアを追加**を選択します。
    - キー名には**key**を入力し、Azure ML Studioからコピーしたキーを値フィールドに貼り付けます。
    - キーを追加した後、**is secret**を選択してキーが公開されないようにします。

    ![接続を追加します。](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.ja.png)

1. **接続を追加**を選択します。

#### プロンプトフローを作成する

Azure AI Foundryにカスタム接続を追加しました。次に、以下の手順を使用してプロンプトフローを作成します。その後、このプロンプトフローをカスタム接続に接続し、プロンプトフロー内で微調整されたモデルを使用できるようにします。

1. 作成したAzure AI Foundryプロジェクトに移動します。

1. 左側のタブから**プロンプトフロー**を選択します。

1. ナビゲーションメニューから**+ 作成**を選択します。

    ![プロンプトフローを選択します。](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.ja.png)

1. ナビゲーションメニューから**チャットフロー**を選択します。

    ![チャットフローを選択します。](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.ja.png)

1. 使用する**フォルダ名**を入力します。

    ![名前を入力します。](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.ja.png)

2. **作成**を選択します。

#### カスタムPhi-3モデルとチャットできるプロンプトフローのセットアップ

微調整されたPhi-3モデルをプロンプトフローに統合する必要があります。ただし、既存のプロンプトフローはこの目的に適していません。そのため、カスタムモデルの統合を可能にするようにプロンプトフローを再設計する必要があります。

1. プロンプトフロー内で以下のタスクを実行して既存のフローを再構築します：

    - **Raw file mode**を選択します。
    - *flow.dag.yml*ファイル内の既存のコードをすべて削除します。
    - 以下のコードを*flow.dag.yml*ファイルに追加します。

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

    - **保存**を選択します。

    ![Raw file modeを選択します。](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.ja.png)

1. カスタムPhi-3モデルをプロンプトフローで使用するために、以下のコードを*integrate_with_promptflow.py*ファイルに追加します。

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

    ![プロンプトフローコードを貼り付けます。](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.ja.png)

> [!NOTE]
> Azure AI Foundryでプロンプトフローを使用する詳細情報については、[Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)を参照してください。

1. **チャット入力**、**チャット出力**を選択してモデルとのチャットを有効にします。

    ![入力と出力を選択します。](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.ja.png)

1. これでカスタムPhi-3モデルとのチャットの準備が整いました。次の演習では、プロンプトフローを開始し、微調整されたPhi-3モデルとチャットする方法を学びます。

> [!NOTE]
>
> 再構築されたフローは以下の画像のようになります：
>
> ![フロー例。](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.ja.png)
>

### カスタムPhi-3モデルとチャットする

微調整されたカスタムPhi-3モデルをプロンプトフローに統合したので、モデルとの対話を開始する準備が整いました。この演習では、プロンプトフローを設定し、モデルとのチャットを開始する手順を案内します。これらのステップを実行することで、微調整されたPhi-3モデルの能力を最大限に活用し、さまざまなタスクや会話を行うことができます。

- プロンプトフローを使用してカスタムPhi-3モデルとチャットします。

#### プロンプトフローを開始する

1. **計算セッションを開始**を選択してプロンプトフローを開始します。

    ![計算セッションを開始します。](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.ja.png)

1. **入力を検証して解析**を選択してパラメーターを更新します。

    ![入力を検証します。](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.ja.png)

1. 作成したカスタム接続の**接続**の**値**を選択します。例：*connection*。

    ![接続を選択します。](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.ja.png)

#### カスタムモデルとチャットする

1. **チャット**を選択します。

    ![チャットを選択します。](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.ja.png)

1. 以下は結果の例です：これでカスタムPhi-3モデルとチャットできます。微調整に使用したデータに基づいた質問をすることをお勧めします。

    ![プロンプトフローでチャットします。](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.ja.png)

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知おきください。元の言語で作成された原文を信頼できる情報源としてください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の利用に起因する誤解や誤解釈について、当方は一切責任を負いません。