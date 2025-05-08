<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-08T05:45:40+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "ja"
}
-->
# Fine-tune and Integrate custom Phi-3 models with Prompt flow in Azure AI Foundry

このエンドツーエンド（E2E）サンプルは、Microsoft Tech Communityのガイド「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)」に基づいています。Azure AI FoundryでカスタムPhi-3モデルをファインチューニング、デプロイ、Prompt flowと統合するプロセスを紹介します。ローカルでコードを実行するE2Eサンプル「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)」とは異なり、このチュートリアルはAzure AI / ML Studio内でのファインチューニングと統合に完全にフォーカスしています。

## 概要

このE2Eサンプルでは、Phi-3モデルのファインチューニングとAzure AI FoundryのPrompt flowとの統合方法を学びます。Azure AI / ML Studioを活用して、カスタムAIモデルのデプロイと利用のワークフローを構築します。このE2Eサンプルは3つのシナリオに分かれています。

**シナリオ1：Azureリソースのセットアップとファインチューニングの準備**

**シナリオ2：Phi-3モデルのファインチューニングとAzure Machine Learning Studioでのデプロイ**

**シナリオ3：Prompt flowとの統合とAzure AI Foundryでのカスタムモデルとのチャット**

以下はこのE2Eサンプルの概要です。

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.ja.png)

### 目次

1. **[シナリオ1：Azureリソースのセットアップとファインチューニングの準備](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning ワークスペースの作成](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [AzureサブスクリプションでのGPUクォータのリクエスト](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ロール割り当ての追加](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [プロジェクトのセットアップ](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ファインチューニング用データセットの準備](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[シナリオ2：Phi-3モデルのファインチューニングとAzure Machine Learning Studioでのデプロイ](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3モデルのファインチューニング](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [ファインチューニング済みPhi-3モデルのデプロイ](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[シナリオ3：Prompt flowとの統合とAzure AI Foundryでのカスタムモデルとのチャット](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [カスタムPhi-3モデルのPrompt flowとの統合](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [カスタムPhi-3モデルとのチャット](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## シナリオ1：Azureリソースのセットアップとファインチューニングの準備

### Azure Machine Learning ワークスペースの作成

1. ポータルページ上部の**検索バー**に「azure machine learning」と入力し、表示されたオプションから**Azure Machine Learning**を選択します。

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.ja.png)

2. ナビゲーションメニューから**+ 作成**を選択します。

3. ナビゲーションメニューから**新しいワークスペース**を選択します。

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.ja.png)

4. 以下の項目を設定します：

    - Azureの**サブスクリプション**を選択。
    - 使用する**リソースグループ**を選択（必要に応じて新規作成）。
    - **ワークスペース名**を入力。ユニークな値である必要があります。
    - 使用する**リージョン**を選択。
    - 使用する**ストレージアカウント**を選択（必要に応じて新規作成）。
    - 使用する**キーコンテナー**を選択（必要に応じて新規作成）。
    - 使用する**アプリケーションインサイト**を選択（必要に応じて新規作成）。
    - 使用する**コンテナレジストリ**を選択（必要に応じて新規作成）。

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.ja.png)

5. **確認および作成**を選択。

6. **作成**を選択。

### AzureサブスクリプションでのGPUクォータのリクエスト

このチュートリアルでは、Phi-3モデルのファインチューニングとデプロイにGPUを使用します。ファインチューニングには*Standard_NC24ads_A100_v4* GPUを使用し、これはクォータリクエストが必要です。デプロイには*Standard_NC6s_v3* GPUを使用し、こちらもクォータリクエストが必要です。

> [!NOTE]
>
> Pay-As-You-Goサブスクリプション（標準サブスクリプションタイプ）のみがGPU割り当ての対象であり、ベネフィットサブスクリプションは現在サポートされていません。
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)にアクセスします。

1. *Standard NCADSA100v4 Family*のクォータをリクエストするために、以下を実施します：

    - 左側のタブから**Quota**を選択。
    - 使用する**仮想マシンファミリー**を選択。例として、*Standard_NC24ads_A100_v4* GPUを含む**Standard NCADSA100v4 Family Cluster Dedicated vCPUs**を選択。
    - ナビゲーションメニューから**Request quota**を選択。

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.ja.png)

    - Request quotaページで使用したい**New cores limit**を入力。例：24。
    - **Submit**を選択してGPUクォータをリクエスト。

1. *Standard NCSv3 Family*のクォータをリクエストするために、以下を実施します：

    - 左側のタブから**Quota**を選択。
    - 使用する**仮想マシンファミリー**を選択。例として、*Standard_NC6s_v3* GPUを含む**Standard NCSv3 Family Cluster Dedicated vCPUs**を選択。
    - ナビゲーションメニューから**Request quota**を選択。
    - Request quotaページで使用したい**New cores limit**を入力。例：24。
    - **Submit**を選択してGPUクォータをリクエスト。

### ロール割り当ての追加

モデルのファインチューニングとデプロイを行うためには、まずUser Assigned Managed Identity（UAI）を作成し、適切な権限を割り当てる必要があります。このUAIはデプロイ時の認証に使用されます。

#### User Assigned Managed Identity (UAI)の作成

1. ポータルページ上部の**検索バー**に「managed identities」と入力し、表示されたオプションから**Managed Identities**を選択します。

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.ja.png)

1. **+ 作成**を選択。

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.ja.png)

1. 以下を設定します：

    - Azureの**サブスクリプション**を選択。
    - 使用する**リソースグループ**を選択（必要に応じて新規作成）。
    - 使用する**リージョン**を選択。
    - **名前**を入力。ユニークな値である必要があります。

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.ja.png)

1. **確認および作成**を選択。

1. **作成**を選択。

#### Managed IdentityにContributorロール割り当てを追加

1. 作成したManaged Identityリソースに移動。

1. 左側のタブから**Azure role assignments**を選択。

1. ナビゲーションメニューから**+ ロール割り当ての追加**を選択。

1. ロール割り当て追加ページで以下を実施：

    - **スコープ**を**リソースグループ**に設定。
    - Azureの**サブスクリプション**を選択。
    - 使用する**リソースグループ**を選択。
    - **ロール**を**Contributor**に設定。

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.ja.png)

2. **保存**を選択。

#### Managed IdentityにStorage Blob Data Readerロール割り当てを追加

1. ポータルページ上部の**検索バー**に「storage accounts」と入力し、表示されたオプションから**Storage accounts**を選択。

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.ja.png)

1. Azure Machine Learningワークスペースに関連付けられたストレージアカウントを選択。例：*finetunephistorage*。

1. ロール割り当て追加ページに移動するために以下を実施：

    - 作成したAzure Storageアカウントに移動。
    - 左側のタブから**アクセス制御 (IAM)**を選択。
    - ナビゲーションメニューから**+ 追加**を選択。
    - **ロール割り当ての追加**を選択。

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.ja.png)

1. ロール割り当て追加ページで以下を実施：

    - ロールページの検索バーに「Storage Blob Data Reader」と入力し、表示された**Storage Blob Data Reader**を選択。
    - **次へ**を選択。
    - メンバーのページで**アクセスを割り当てる先**を**Managed identity**に設定。
    - **+ メンバーの選択**を選択。
    - Managed identities選択ページでAzureの**サブスクリプション**を選択。
    - **Managed identity**の種類を**Manage Identity**に設定。
    - 作成したManaged Identity（例：*finetunephi-managedidentity*）を選択。
    - **選択**をクリック。

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.ja.png)

1. **確認および割り当て**を選択。

#### Managed IdentityにAcrPullロール割り当てを追加

1. ポータルページ上部の**検索バー**に「container registries」と入力し、表示されたオプションから**Container registries**を選択。

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.ja.png)

1. Azure Machine Learningワークスペースに関連付けられたコンテナレジストリを選択。例：*finetunephicontainerregistry*

1. ロール割り当て追加ページに移動するために以下を実施：

    - 左側のタブから**アクセス制御 (IAM)**を選択。
    - ナビゲーションメニューから**+ 追加**を選択。
    - **ロール割り当ての追加**を選択。

1. ロール割り当て追加ページで以下を実施：

    - ロールページの検索バーに「AcrPull」と入力し、表示された**AcrPull**を選択。
    - **次へ**を選択。
    - メンバーのページで**アクセスを割り当てる先**を**Managed identity**に設定。
    - **+ メンバーの選択**を選択。
    - Managed identities選択ページでAzureの**サブスクリプション**を選択。
    - **Managed identity**の種類を**Manage Identity**に設定。
    - 作成したManaged Identity（例：*finetunephi-managedidentity*）を選択。
    - **選択**をクリック。
    - **確認および割り当て**を選択。

### プロジェクトのセットアップ

ファインチューニングに必要なデータセットをダウンロードするため、ローカル環境をセットアップします。

この演習では、

- 作業用フォルダーを作成します。
- 仮想環境を作成します。
- 必要なパッケージをインストールします。
- データセットをダウンロードするための*download_dataset.py*ファイルを作成します。

#### 作業用フォルダーの作成

1. ターミナルを開き、以下のコマンドを入力してデフォルトパスに*finetune-phi*という名前のフォルダーを作成します。

    ```console
    mkdir finetune-phi
    ```

2. ターミナルで以下のコマンドを入力し、作成した*finetune-phi*フォルダーに移動します。

    ```console
    cd finetune-phi
    ```

#### 仮想環境の作成

1. ターミナルで以下のコマンドを入力し、*.venv*という名前の仮想環境を作成します。

    ```console
    python -m venv .venv
    ```

2. ターミナルで以下のコマンドを入力し、仮想環境をアクティブにします。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> 正しく動作していれば、コマンドプロンプトの前に*（.venv）*と表示されます。

#### 必要なパッケージのインストール

1. ターミナルで以下のコマンドを入力し、必要なパッケージをインストールします。

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py`の作成

> [!NOTE]
> フォルダー構成の例：
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code**を開きます。

1. メニューバーから**ファイル**を選択。

1. **フォルダーを開く**を選択。

1. 作成した*finetune-phi*フォルダー（例：*C:\Users\yourUserName\finetune-phi*）を選択。

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.ja.png)

1. Visual Studio Codeの左ペインで右クリックし、**新しいファイル**を選択して*download_dataset.py*ファイルを作成。

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.ja.png)

### ファインチューニング用データセットの準備

この演習では、*download_dataset.py*ファイルを実行して*ultrachat_200k*データセットをローカル環境にダウンロードします。その後、このデータセットを使ってAzure Machine LearningでPhi-3モデルをファインチューニングします。

この演習で行うこと：

- *download_dataset.py*ファイルにデータセットをダウンロードするコードを追加。
- *download_dataset.py*ファイルを実行し、データセットをローカル環境にダウンロード。

#### *download_dataset.py*を使ってデータセットをダウンロード

1. Visual Studio Codeで*download_dataset.py*ファイルを開く。

1. 以下のコードを*download_dataset.py*ファイルに追加。

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

1. ターミナルで以下のコマンドを入力し、スクリプトを実行してデータセットをローカル環境にダウンロード。

    ```console
    python download_dataset.py
    ```

1. データセットがローカルの*finetune-phi/data*ディレクトリに正常に
1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. 左側のタブから **Compute** を選択します。

1. ナビゲーションメニューから **Compute clusters** を選択します。

1. **+ New** を選択します。

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.ja.png)

1. 以下の作業を行います：

    - 使用したい **Region** を選択します。
    - **Virtual machine tier** を **Dedicated** に設定します。
    - **Virtual machine type** を **GPU** に設定します。
    - **Virtual machine size** のフィルターを **Select from all options** に設定します。
    - **Virtual machine size** を **Standard_NC24ads_A100_v4** に選択します。

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.ja.png)

1. **Next** を選択します。

1. 以下の作業を行います：

    - **Compute name** を入力します。ユニークな値である必要があります。
    - **Minimum number of nodes** を **0** に設定します。
    - **Maximum number of nodes** を **1** に設定します。
    - **Idle seconds before scale down** を **120** に設定します。

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.ja.png)

1. **Create** を選択します。

#### Phi-3モデルのファインチューニング

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. 作成した Azure Machine Learning ワークスペースを選択します。

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.ja.png)

1. 以下の作業を行います：

    - 左側のタブから **Model catalog** を選択します。
    - **検索バー** に *phi-3-mini-4k* と入力し、表示されたオプションから **Phi-3-mini-4k-instruct** を選択します。

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.ja.png)

1. ナビゲーションメニューから **Fine-tune** を選択します。

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.ja.png)

1. 以下の作業を行います：

    - **Select task type** を **Chat completion** に設定します。
    - **+ Select data** を選択して **Training data** をアップロードします。
    - Validation データのアップロードタイプを **Provide different validation data** に設定します。
    - **+ Select data** を選択して **Validation data** をアップロードします。

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.ja.png)

    > [!TIP]
    >
    > **Advanced settings** を選択すると、**learning_rate** や **lr_scheduler_type** などの設定をカスタマイズでき、ファインチューニングをより最適化できます。

1. **Finish** を選択します。

1. この演習では、Azure Machine Learning を使って Phi-3 モデルのファインチューニングに成功しました。ファインチューニングにはかなりの時間がかかる場合があります。ジョブを実行した後は完了するまで待つ必要があります。ファインチューニングジョブの状況は、Azure Machine Learning ワークスペースの左側にある Jobs タブで確認できます。次のシリーズでは、ファインチューニングしたモデルをデプロイし、Prompt flow と統合します。

    ![See finetuning job.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.ja.png)

### ファインチューニングした Phi-3 モデルのデプロイ

ファインチューニングした Phi-3 モデルを Prompt flow と連携させるには、モデルをデプロイしてリアルタイム推論ができるようにする必要があります。このプロセスでは、モデルの登録、オンラインエンドポイントの作成、モデルのデプロイが含まれます。

この演習では以下を行います：

- ファインチューニングしたモデルを Azure Machine Learning ワークスペースに登録する。
- オンラインエンドポイントを作成する。
- 登録済みのファインチューニングした Phi-3 モデルをデプロイする。

#### ファインチューニングしたモデルの登録

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. 作成した Azure Machine Learning ワークスペースを選択します。

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.ja.png)

1. 左側のタブから **Models** を選択します。
1. **+ Register** を選択します。
1. **From a job output** を選択します。

    ![Register model.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.ja.png)

1. 作成したジョブを選択します。

    ![Select job.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.ja.png)

1. **Next** を選択します。

1. **Model type** を **MLflow** に設定します。

1. **Job output** が選択されていることを確認します（通常は自動選択されます）。

    ![Select output.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.ja.png)

2. **Next** を選択します。

3. **Register** を選択します。

    ![Select register.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.ja.png)

4. 登録したモデルは、左側のタブの **Models** メニューから確認できます。

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.ja.png)

#### ファインチューニングしたモデルのデプロイ

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

1. ナビゲーションメニューから **Real-time endpoints** を選択します。

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.ja.png)

1. **Create** を選択します。

1. 登録したモデルを選択します。

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.ja.png)

1. **Select** を選択します。

1. 以下の作業を行います：

    - **Virtual machine** を *Standard_NC6s_v3* に設定します。
    - 使用したい **Instance count** を選択します（例：*1*）。
    - **Endpoint** を **New** に設定し、新しいエンドポイントを作成します。
    - **Endpoint name** を入力します。ユニークな値である必要があります。
    - **Deployment name** を入力します。ユニークな値である必要があります。

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.ja.png)

1. **Deploy** を選択します。

> [!WARNING]
> アカウントへの追加料金を防ぐため、Azure Machine Learning ワークスペースで作成したエンドポイントは不要になったら必ず削除してください。
>

#### Azure Machine Learning ワークスペースでデプロイ状況を確認する

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

1. 作成したエンドポイントを選択します。

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.ja.png)

1. このページで、デプロイ中のエンドポイントを管理できます。

> [!NOTE]
> デプロイが完了したら、**Live traffic** が **100%** に設定されていることを確認してください。もし設定されていなければ、**Update traffic** を選択してトラフィック設定を調整してください。トラフィックが 0% の場合、モデルのテストはできません。
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.ja.png)
>

## シナリオ3: Prompt flow と統合し、Azure AI Foundry でカスタムモデルとチャットする

### カスタム Phi-3 モデルを Prompt flow と統合する

ファインチューニングしたモデルをデプロイした後、Prompt Flow と統合してリアルタイムアプリケーションでモデルを利用できます。これにより、カスタム Phi-3 モデルを使ったさまざまな対話型タスクが可能になります。

この演習では以下を行います：

- Azure AI Foundry Hub の作成
- Azure AI Foundry Project の作成
- Prompt flow の作成
- ファインチューニングした Phi-3 モデル用のカスタム接続の追加
- カスタム Phi-3 モデルとチャットできるように Prompt flow の設定

> [!NOTE]
> Azure ML Studio を使っても Promptflow と統合できます。同様の統合手順が適用可能です。

#### Azure AI Foundry Hub の作成

Project を作成する前に Hub を作成する必要があります。Hub はリソースグループのような役割を果たし、Azure AI Foundry 内で複数の Project を整理・管理できます。

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) にアクセスします。

1. 左側のタブから **All hubs** を選択します。

1. ナビゲーションメニューから **+ New hub** を選択します。

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.ja.png)

1. 以下の作業を行います：

    - **Hub name** を入力します。ユニークな値である必要があります。
    - Azure の **Subscription** を選択します。
    - 使用する **Resource group** を選択します（必要に応じて新規作成）。
    - 使用したい **Location** を選択します。
    - 使用する **Connect Azure AI Services** を選択します（必要に応じて新規作成）。
    - **Connect Azure AI Search** は **Skip connecting** に設定します。

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.ja.png)

1. **Next** を選択します。

#### Azure AI Foundry Project の作成

1. 作成した Hub 内で、左側のタブから **All projects** を選択します。

1. ナビゲーションメニューから **+ New project** を選択します。

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.ja.png)

1. **Project name** を入力します。ユニークな値である必要があります。

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.ja.png)

1. **Create a project** を選択します。

#### ファインチューニングした Phi-3 モデル用のカスタム接続を追加

カスタム Phi-3 モデルを Prompt flow と統合するには、モデルのエンドポイントとキーをカスタム接続に保存する必要があります。これにより、Prompt flow からカスタム Phi-3 モデルにアクセスできるようになります。

#### ファインチューニングした Phi-3 モデルの api key と endpoint uri を設定

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) にアクセスします。

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.ja.png)

1. 作成したエンドポイントを選択します。

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.ja.png)

1. ナビゲーションメニューから **Consume** を選択します。

1. **REST endpoint** と **Primary key** をコピーします。
![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.ja.png)

#### カスタム接続を追加する

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) にアクセスします。

1. 作成した Azure AI Foundry プロジェクトに移動します。

1. 作成したプロジェクトで、左側のタブから **Settings** を選択します。

1. **+ New connection** を選択します。

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.ja.png)

1. ナビゲーションメニューから **Custom keys** を選択します。

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.ja.png)

1. 以下の操作を行います：

    - **+ Add key value pairs** を選択します。
    - キー名に **endpoint** を入力し、Azure ML Studio からコピーしたエンドポイントを値のフィールドに貼り付けます。
    - 再度 **+ Add key value pairs** を選択します。
    - キー名に **key** を入力し、Azure ML Studio からコピーしたキーを値のフィールドに貼り付けます。
    - キーを追加したら、キーの露出を防ぐために **is secret** を選択します。

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.ja.png)

1. **Add connection** を選択します。

#### Prompt flow を作成する

Azure AI Foundry にカスタム接続を追加しました。次に、以下の手順で Prompt flow を作成します。その後、この Prompt flow をカスタム接続に接続し、ファインチューニングしたモデルを Prompt flow 内で使用できるようにします。

1. 作成した Azure AI Foundry プロジェクトに移動します。

1. 左側のタブから **Prompt flow** を選択します。

1. ナビゲーションメニューから **+ Create** を選択します。

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.ja.png)

1. ナビゲーションメニューから **Chat flow** を選択します。

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.ja.png)

1. 使用する **Folder name** を入力します。

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.ja.png)

2. **Create** を選択します。

#### カスタム Phi-3 モデルとチャットできるように Prompt flow を設定する

ファインチューニングした Phi-3 モデルを Prompt flow に統合する必要があります。ただし、既存の Prompt flow はこの目的に対応していないため、カスタムモデルの統合が可能なように Prompt flow を再設計する必要があります。

1. Prompt flow で、既存のフローを再構築するために以下の操作を行います：

    - **Raw file mode** を選択します。
    - *flow.dag.yml* ファイル内の既存のコードをすべて削除します。
    - 以下のコードを *flow.dag.yml* ファイルに追加します。

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

    - **Save** を選択します。

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.ja.png)

1. *integrate_with_promptflow.py* ファイルに以下のコードを追加し、Prompt flow でカスタム Phi-3 モデルを使用できるようにします。

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.ja.png)

> [!NOTE]
> Azure AI Foundry での Prompt flow の詳細な使い方については、[Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) を参照してください。

1. **Chat input**、**Chat output** を選択して、モデルとのチャットを有効にします。

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.ja.png)

1. これでカスタム Phi-3 モデルとチャットできる準備が整いました。次の演習では、Prompt flow の起動方法と、ファインチューニングした Phi-3 モデルとチャットする方法を学びます。

> [!NOTE]
>
> 再構築したフローは以下の画像のようになります：
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.ja.png)
>

### カスタム Phi-3 モデルとチャットする

ファインチューニングしたカスタム Phi-3 モデルを Prompt flow と統合したので、いよいよ対話を開始できます。この演習では、Prompt flow を使ってモデルとチャットする設定と開始方法を案内します。これらの手順に従うことで、ファインチューニングした Phi-3 モデルの能力をさまざまなタスクや会話で最大限に活用できます。

- Prompt flow を使ってカスタム Phi-3 モデルとチャットします。

#### Prompt flow を開始する

1. **Start compute sessions** を選択して Prompt flow を開始します。

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.ja.png)

1. **Validate and parse input** を選択してパラメーターを更新します。

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.ja.png)

1. 作成したカスタム接続の **connection** の **Value** を選択します。例：*connection*。

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.ja.png)

#### カスタムモデルとチャットする

1. **Chat** を選択します。

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.ja.png)

1. 結果の例を示します：これでカスタム Phi-3 モデルとチャットできます。ファインチューニングに使ったデータに基づいた質問をすることをおすすめします。

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.ja.png)

**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を期しておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご承知おきください。原文の言語で記載された文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳について、一切の責任を負いかねます。