# Microsoft FoundryのPrompt flowでカスタムPhi-3モデルをファインチューニングおよび統合する

このエンドツーエンド（E2E）サンプルは、Microsoft Tech Communityのガイド「[Microsoft FoundryのPrompt FlowでカスタムPhi-3モデルをファインチューニングおよび統合する](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)」をベースにしています。Microsoft FoundryのPrompt flowでカスタムPhi-3モデルをファインチューニング、展開、および統合するプロセスを紹介します。  
ローカルでコードを実行するE2Eサンプル「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)」とは異なり、このチュートリアルではAzure AI / ML Studio内でモデルのファインチューニングと統合に完全にフォーカスしています。

## 概要

このE2Eサンプルでは、Phi-3モデルをファインチューニングしてMicrosoft FoundryのPrompt flowと統合する方法を学びます。Azure AI / ML Studioを活用して、カスタムAIモデルの展開と利用のワークフローを構築します。このE2Eサンプルは3つのシナリオに分かれています。

**シナリオ1：Azureリソースのセットアップとファインチューニングの準備**

**シナリオ2：Phi-3モデルのファインチューニングとAzure Machine Learning Studioでの展開**

**シナリオ3：Prompt flowとの統合とMicrosoft Foundryでカスタムモデルとのチャット**

以下はこのE2Eサンプルの概要です。

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/ja/00-01-architecture.198ba0f1ae6d841a.webp)

### 目次

1. **[シナリオ1：Azureリソースのセットアップとファインチューニングの準備](#シナリオ1：azureリソースのセットアップとファインチューニングの準備)**
    - [Azure Machine Learningワークスペースの作成](#azure-machine-learningワークスペースの作成)
    - [AzureサブスクリプションでのGPUクォータのリクエスト](#azureサブスクリプションでのgpuクォータのリクエスト)
    - [ロール割り当ての追加](#ロール割り当ての追加)
    - [プロジェクトのセットアップ](#プロジェクトのセットアップ)
    - [ファインチューニング用データセットの準備](#ファインチューニング用のデータセット準備)

1. **[シナリオ2：Phi-3モデルのファインチューニングとAzure Machine Learning Studioでの展開](#シナリオ-2-phi-3-モデルのファインチューニングと-azure-machine-learning-studio-でのデプロイ)**
    - [Phi-3モデルのファインチューニング](#phi-3-モデルのファインチューニング)
    - [ファインチューニング済みPhi-3モデルの展開](#ファインチューニング済み-phi-3-モデルのデプロイ)

1. **[シナリオ3：Prompt flowとの統合とMicrosoft Foundryでカスタムモデルとチャット](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [カスタムPhi-3モデルのPrompt flowへの統合](#カスタム-phi-3-モデルを-prompt-flow-に統合)
    - [カスタムPhi-3モデルとのチャット](#カスタム-phi-3-モデルとチャットする)

## シナリオ1：Azureリソースのセットアップとファインチューニングの準備

### Azure Machine Learningワークスペースの作成

1. ポータルページ上部の<strong>検索バー</strong>に *azure machine learning* と入力し、表示されるオプションから<strong>Azure Machine Learning</strong>を選択します。

    ![Type azure machine learning.](../../../../../../translated_images/ja/01-01-type-azml.acae6c5455e67b4b.webp)

2. ナビゲーションメニューから<strong>+ Create</strong>を選択します。

3. ナビゲーションメニューから<strong>New workspace</strong>を選択します。

    ![Select new workspace.](../../../../../../translated_images/ja/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. 以下の項目を設定します：

    - Azureの<strong>Subscription</strong>を選択します。
    - 利用する<strong>Resource group</strong>を選択（必要に応じて新規作成）。
    - <strong>Workspace Name</strong>を入力します。一意の名前である必要があります。
    - 利用する<strong>Region</strong>を選択します。
    - 利用する<strong>Storage account</strong>を選択（必要に応じて新規作成）。
    - 利用する<strong>Key vault</strong>を選択（必要に応じて新規作成）。
    - 利用する<strong>Application insights</strong>を選択（必要に応じて新規作成）。
    - 利用する<strong>Container registry</strong>を選択（必要に応じて新規作成）。

    ![Fill azure machine learning.](../../../../../../translated_images/ja/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. <strong>Review + Create</strong>を選択します。

6. <strong>Create</strong>を選択します。

### AzureサブスクリプションでのGPUクォータのリクエスト

このチュートリアルでは、GPUを使ってPhi-3モデルのファインチューニングと展開を行います。ファインチューニングには<em>Standard_NC24ads_A100_v4</em> GPUを使用しますが、これはクォータの申請が必要です。展開には<em>Standard_NC6s_v3</em> GPUを使用しますが、こちらもクォータ申請が必要です。

> [!NOTE]
> 
> GPU割り当てが可能なのはPay-As-You-Goサブスクリプション（標準的なサブスクリプションタイプ）のみであり、ベネフィットサブスクリプションは現在サポートされていません。
> 

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)にアクセスします。

1. <em>Standard NCADSA100v4 Family</em>のクォータを申請するには、以下を実施します：

    - 左側のタブから<strong>Quota</strong>を選択。
    - 使用する<strong>Virtual machine family</strong>を選択します。例として、*Standard NCADSA100v4 Family Cluster Dedicated vCPUs*（*Standard_NC24ads_A100_v4* GPUを含む）を選択。
    - ナビゲーションメニューから<strong>Request quota</strong>を選択。

        ![Request quota.](../../../../../../translated_images/ja/02-02-request-quota.c0428239a63ffdd5.webp)

    - Request quotaページ内の<strong>New cores limit</strong>に使用したい数値を入力（例：24）。
    - Request quotaページ内で<strong>Submit</strong>を選択しGPUクォータを申請。

1. <em>Standard NCSv3 Family</em>のクォータを申請するには、以下を実施します：

    - 左側のタブから<strong>Quota</strong>を選択。
    - 使用する<strong>Virtual machine family</strong>を選択します。例として、*Standard NCSv3 Family Cluster Dedicated vCPUs*（*Standard_NC6s_v3* GPUを含む）を選択。
    - ナビゲーションメニューから<strong>Request quota</strong>を選択。
    - Request quotaページ内の<strong>New cores limit</strong>に使用したい数値を入力（例：24）。
    - Request quotaページ内で<strong>Submit</strong>を選択しGPUクォータを申請。

### ロール割り当ての追加

モデルのファインチューニングと展開には、まずユーザー割り当てマネージドアイデンティティ（UAI）を作成し、適切な権限を割り当てる必要があります。このUAIは展開時の認証に使用されます。

#### ユーザー割り当てマネージドアイデンティティ（UAI）の作成

1. ポータルページ上部の<strong>検索バー</strong>に *managed identities* と入力し、表示されるオプションから<strong>Managed Identities</strong>を選択します。

    ![Type managed identities.](../../../../../../translated_images/ja/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. <strong>+ Create</strong>を選択します。

    ![Select create.](../../../../../../translated_images/ja/03-02-select-create.92bf8989a5cd98f2.webp)

1. 以下を設定します：

    - Azureの<strong>Subscription</strong>を選択します。
    - 利用する<strong>Resource group</strong>を選択（必要に応じて作成）。
    - 利用する<strong>Region</strong>を選択します。
    - <strong>Name</strong>を入力します。一意の名前である必要があります。

    ![Select create.](../../../../../../translated_images/ja/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. <strong>Review + create</strong>を選択します。

1. <strong>+ Create</strong>を選択します。

#### マネージドアイデンティティにContributorロール割り当てを追加

1. 作成したマネージドアイデンティティのリソースに移動。

1. 左側のタブから<strong>Azure role assignments</strong>を選択。

1. ナビゲーションメニューから<strong>+Add role assignment</strong>を選択。

1. Add role assignmentページ内で以下を設定：
    - <strong>Scope</strong>を<strong>Resource group</strong>に設定。
    - Azureの<strong>Subscription</strong>を選択。
    - 利用する<strong>Resource group</strong>を選択。
    - <strong>Role</strong>を<strong>Contributor</strong>に設定。

    ![Fill contributor role.](../../../../../../translated_images/ja/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. <strong>Save</strong>を選択。

#### マネージドアイデンティティにStorage Blob Data Readerロール割り当てを追加

1. ポータルページ上部の<strong>検索バー</strong>に *storage accounts* と入力し、表示されるオプションから<strong>Storage accounts</strong>を選択します。

    ![Type storage accounts.](../../../../../../translated_images/ja/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Azure Machine Learningワークスペースに関連付けられたストレージアカウントを選択します。例：*finetunephistorage*。

1. Add role assignmentページへの移動操作：

    - 作成したAzure Storageアカウントに移動。
    - 左側のタブから<strong>Access Control (IAM)</strong>を選択。
    - ナビゲーションメニューから<strong>+ Add</strong>を選択。
    - ナビゲーションメニューから<strong>Add role assignment</strong>を選択。

    ![Add role.](../../../../../../translated_images/ja/03-06-add-role.353ccbfdcf0789c2.webp)

1. Add role assignmentページ内で以下を設定：

    - Roleページの検索バーに *Storage Blob Data Reader* と入力し、表示された<strong>Storage Blob Data Reader</strong>を選択。
    - Roleページで<strong>Next</strong>を選択。
    - Membersページで<strong>Assign access to</strong>を<strong>Managed identity</strong>に設定。
    - Membersページで<strong>+ Select members</strong>を選択。
    - Select managed identitiesページでAzureの<strong>Subscription</strong>を選択。
    - Select managed identitiesページで<strong>Managed identity</strong>を<strong>Manage Identity</strong>に設定。
    - Select managed identitiesページで作成したマネージドアイデンティティ（例：*finetunephi-managedidentity*）を選択。
    - Select managed identitiesページで<strong>Select</strong>を選択。

    ![Select managed identity.](../../../../../../translated_images/ja/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. <strong>Review + assign</strong>を選択。

#### マネージドアイデンティティにAcrPullロール割り当てを追加

1. ポータルページ上部の<strong>検索バー</strong>に *container registries* と入力し、表示されるオプションから<strong>Container registries</strong>を選択します。

    ![Type container registries.](../../../../../../translated_images/ja/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Azure Machine Learningワークスペースに関連付けられたコンテナレジストリを選択します。例：*finetunephicontainerregistry*

1. Add role assignmentページへの移動操作：

    - 左側のタブから<strong>Access Control (IAM)</strong>を選択。
    - ナビゲーションメニューから<strong>+ Add</strong>を選択。
    - ナビゲーションメニューから<strong>Add role assignment</strong>を選択。

1. Add role assignmentページ内で以下を設定：

    - Roleページの検索バーに *AcrPull* と入力し、表示された<strong>AcrPull</strong>を選択。
    - Roleページで<strong>Next</strong>を選択。
    - Membersページで<strong>Assign access to</strong>を<strong>Managed identity</strong>に設定。
    - Membersページで<strong>+ Select members</strong>を選択。
    - Select managed identitiesページでAzureの<strong>Subscription</strong>を選択。
    - Select managed identitiesページで<strong>Managed identity</strong>を<strong>Manage Identity</strong>に設定。
    - Select managed identitiesページで作成したマネージドアイデンティティ（例：*finetunephi-managedidentity*）を選択。
    - Select managed identitiesページで<strong>Select</strong>を選択。
    - <strong>Review + assign</strong>を選択。

### プロジェクトのセットアップ

ファインチューニングに必要なデータセットをダウンロードするため、ローカル環境をセットアップします。

この演習では、

- 作業用フォルダーの作成
- 仮想環境の作成
- 必須パッケージのインストール
- データセットをダウンロードする<em>download_dataset.py</em>ファイルの作成

を行います。

#### 作業用フォルダーの作成

1. ターミナルウィンドウを開き、デフォルトのパスに<em>finetune-phi</em>という名前のフォルダーを作成するために、以下のコマンドを入力します。

    ```console
    mkdir finetune-phi
    ```


2. ターミナルで以下を入力し、作成した<em>finetune-phi</em>フォルダーに移動します。

    ```console
    cd finetune-phi
    ```


#### 仮想環境の作成

1. ターミナルで以下のコマンドを入力し、<em>.venv</em>という名前の仮想環境を作成します。
    ```console
    python -m venv .venv
    ```

2. ターミナルで以下のコマンドを入力し、仮想環境を有効化します。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> うまくいくと、コマンドプロンプトの前に *(.venv)* と表示されます。

#### 必要なパッケージのインストール

1. ターミナルで以下のコマンドを入力し、必要なパッケージをインストールします。

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py` の作成

> [!NOTE]
> 完成したフォルダー構成：
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** を開きます。

1. メニューバーから <strong>ファイル</strong> を選択します。

1. <strong>フォルダーを開く</strong> を選択します。

1. 作成した *finetune-phi* フォルダーを選択します。場所は *C:\Users\yourUserName\finetune-phi* です。

    ![作成したフォルダーを選択します。](../../../../../../translated_images/ja/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Visual Studio Code の左ペインで右クリックし、<strong>新しいファイル</strong> を選択して *download_dataset.py* という名前のファイルを作成します。

    ![新しいファイルを作成します。](../../../../../../translated_images/ja/04-02-create-new-file.cf9a330a3a9cff92.webp)

### ファインチューニング用のデータセット準備

この演習では、*download_dataset.py* ファイルを実行して、*ultrachat_200k* データセットをローカル環境にダウンロードします。その後、このデータセットを使って Azure Machine Learning で Phi-3 モデルのファインチューニングを行います。

この演習で行うこと：

- *download_dataset.py* ファイルにデータセットをダウンロードするためのコードを追加します。
- *download_dataset.py* ファイルを実行し、データセットをローカル環境にダウンロードします。

#### *download_dataset.py* を使用してデータセットをダウンロードする

1. Visual Studio Code で *download_dataset.py* ファイルを開きます。

1. 以下のコードを *download_dataset.py* ファイルに追加します。

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # 指定された名前、設定、および分割比率でデータセットを読み込む
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # データセットを訓練用とテスト用に分割する（訓練80％、テスト20％）
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # もしディレクトリが存在しなければ作成する
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # ファイルを書き込みモードで開く
        with open(filepath, 'w', encoding='utf-8') as f:
            # データセットの各レコードを反復する
            for record in dataset:
                # レコードをJSONオブジェクトとしてダンプし、ファイルに書き込む
                json.dump(record, f)
                # レコードを区切るために改行文字を書く
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # 特定の設定と分割比率でULTRACHAT_200kデータセットを読み込み、分割する
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # 分割から訓練用とテスト用のデータセットを抽出する
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # 訓練用データセットをJSONLファイルに保存する
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # テスト用データセットを別のJSONLファイルに保存する
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. ターミナルで以下のコマンドを入力し、スクリプトを実行してデータセットをローカル環境にダウンロードします。

    ```console
    python download_dataset.py
    ```

1. データセットがローカルの *finetune-phi/data* ディレクトリに正常に保存されたことを確認します。

> [!NOTE]
>
> #### データセットのサイズとファインチューニング時間についての注意
>
> 本チュートリアルでは、データセットの1％のみを使用しています（`split='train[:1%]'`）。これによりデータ量が大幅に削減され、アップロードとファインチューニングの処理が高速化されます。トレーニング時間とモデルの性能のバランスを見ながら、割合を調整可能です。データセットの小さい部分集合を使うことで、ファインチューニングにかかる時間を短縮し、チュートリアルとして扱いやすくしています。

## シナリオ 2: Phi-3 モデルのファインチューニングと Azure Machine Learning Studio でのデプロイ

### Phi-3 モデルのファインチューニング

この演習では、Azure Machine Learning Studio で Phi-3 モデルのファインチューニングを行います。

この演習で行うこと：

- ファインチューニング用のコンピュータークラスターを作成します。
- Azure Machine Learning Studio で Phi-3 モデルをファインチューニングします。

#### ファインチューニング用のコンピュータークラスターの作成

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. 左側のタブから **Compute** を選択します。

1. ナビゲーションメニューから **Compute clusters** を選択します。

1. **+ 新規** を選択します。

    ![Compute を選択します。](../../../../../../translated_images/ja/06-01-select-compute.a29cff290b480252.webp)

1. 以下の設定を行います：

    - 使用したい <strong>リージョン</strong> を選択します。
    - <strong>仮想マシンの階層</strong> を **Dedicated** に設定します。
    - <strong>仮想マシンのタイプ</strong> を **GPU** に設定します。
    - <strong>仮想マシンサイズ</strong> フィルターを <strong>すべてのオプションから選択</strong> に設定します。
    - <strong>仮想マシンサイズ</strong> を **Standard_NC24ads_A100_v4** に設定します。

    ![クラスターを作成します。](../../../../../../translated_images/ja/06-02-create-cluster.f221b65ae1221d4e.webp)

1. <strong>次へ</strong> を選択します。

1. 以下の設定を行います：

    - <strong>コンピュート名</strong> を入力します。一意である必要があります。
    - <strong>最小ノード数</strong> を **0** に設定します。
    - <strong>最大ノード数</strong> を **1** に設定します。
    - <strong>スケールダウンするまでのアイドル秒数</strong> を **120** に設定します。

    ![クラスターを作成します。](../../../../../../translated_images/ja/06-03-create-cluster.4a54ba20914f3662.webp)

1. <strong>作成</strong> を選択します。

#### Phi-3 モデルのファインチューニング

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. 作成した Azure Machine Learning ワークスペースを選択します。

    ![作成したワークスペースを選択します。](../../../../../../translated_images/ja/06-04-select-workspace.a92934ac04f4f181.webp)

1. 以下の操作を行います：

    - 左側のタブから <strong>モデルカタログ</strong> を選択します。
    - <strong>検索バー</strong> に *phi-3-mini-4k* と入力し、表示されるオプションから **Phi-3-mini-4k-instruct** を選択します。

    ![phi-3-mini-4k を入力します。](../../../../../../translated_images/ja/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. ナビゲーションメニューから <strong>ファインチューニング</strong> を選択します。

    ![ファインチューニングを選択します。](../../../../../../translated_images/ja/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. 以下の設定を行います：

    - <strong>タスクタイプの選択</strong> を <strong>チャット完了</strong> に設定します。
    - **+ データを選択** を選択して <strong>トレーニングデータ</strong> をアップロードします。
    - 検証データのアップロードタイプを <strong>異なる検証データを提供</strong> に設定します。
    - **+ データを選択** を選択して <strong>検証データ</strong> をアップロードします。

    ![ファインチューニングページを入力します。](../../../../../../translated_images/ja/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> <strong>詳細設定</strong> を選択すると、**learning_rate** や **lr_scheduler_type** などの設定をカスタマイズでき、ファインチューニングプロセスをニーズに合わせて最適化できます。

1. <strong>完了</strong> を選択します。

1. この演習では、Azure Machine Learning を使って Phi-3 モデルのファインチューニングを成功裏に完了しました。ファインチューニングにはかなりの時間がかかる場合があります。ジョブを実行した後は完了まで待つ必要があります。Azure Machine Learning ワークスペースの左側にあるジョブタブでファインチューニングジョブの状態を確認できます。次のシリーズでは、ファインチューニングしたモデルをデプロイし、Prompt flow との統合を行います。

    ![ファインチューニングジョブの状態を確認します。](../../../../../../translated_images/ja/06-08-output.2bd32e59930672b1.webp)

### ファインチューニング済み Phi-3 モデルのデプロイ

ファインチューニング済みの Phi-3 モデルを Prompt flow と統合するには、モデルをデプロイしてリアルタイム推論で利用可能にする必要があります。このプロセスには、モデルの登録、オンラインエンドポイントの作成、およびモデルのデプロイが含まれます。

この演習で行うこと：

- ファインチューニング済みモデルを Azure Machine Learning ワークスペースに登録します。
- オンラインエンドポイントを作成します。
- 登録済みのファインチューニング済み Phi-3 モデルをデプロイします。

#### ファインチューニング済みモデルの登録

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. 作成した Azure Machine Learning ワークスペースを選択します。

    ![作成したワークスペースを選択します。](../../../../../../translated_images/ja/06-04-select-workspace.a92934ac04f4f181.webp)

1. 左側タブから <strong>モデル</strong> を選択します。
1. **+ 登録** を選択します。
1. <strong>ジョブ出力から</strong> を選択します。

    ![モデルを登録します。](../../../../../../translated_images/ja/07-01-register-model.ad1e7cc05e4b2777.webp)

1. 作成したジョブを選択します。

    ![ジョブを選択します。](../../../../../../translated_images/ja/07-02-select-job.3e2e1144cd6cd093.webp)

1. <strong>次へ</strong> を選択します。

1. <strong>モデルタイプ</strong> を **MLflow** に設定します。

1. <strong>ジョブ出力</strong> が選択されていることを確認します。通常、自動的に選択されています。

    ![出力を選択します。](../../../../../../translated_images/ja/07-03-select-output.4cf1a0e645baea1f.webp)

2. <strong>次へ</strong> を選択します。

3. <strong>登録</strong> を選択します。

    ![登録を選択します。](../../../../../../translated_images/ja/07-04-register.fd82a3b293060bc7.webp)

4. 左側のタブから <strong>モデル</strong> メニューに移動して登録済みのモデルを確認できます。

    ![登録済みモデル。](../../../../../../translated_images/ja/07-05-registered-model.7db9775f58dfd591.webp)

#### ファインチューニング済みモデルのデプロイ

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから <strong>エンドポイント</strong> を選択します。

1. ナビゲーションメニューから <strong>リアルタイムエンドポイント</strong> を選択します。

    ![エンドポイントを作成します。](../../../../../../translated_images/ja/07-06-create-endpoint.1ba865c606551f09.webp)

1. <strong>作成</strong> を選択します。

1. 登録済みモデルを選択します。

    ![登録済みモデルを選択します。](../../../../../../translated_images/ja/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. <strong>選択</strong> を選択します。

1. 以下の設定を行います：

    - <strong>仮想マシン</strong> を *Standard_NC6s_v3* に設定します。
    - 使用したい <strong>インスタンス数</strong> を設定します。例：*1*。
    - <strong>エンドポイント</strong> を <strong>新規</strong> に設定してエンドポイントを作成します。
    - <strong>エンドポイント名</strong> を入力します。一意である必要があります。
    - <strong>デプロイ名</strong> を入力します。一意である必要があります。

    ![デプロイ設定を入力します。](../../../../../../translated_images/ja/07-08-deployment-setting.43ddc4209e673784.webp)

1. <strong>デプロイ</strong> を選択します。

> [!WARNING]
> 追加請求を避けるため、Azure Machine Learning ワークスペースで作成したエンドポイントは不要になったら必ず削除してください。
>

#### Azure Machine Learning ワークスペースでデプロイ状況を確認

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから <strong>エンドポイント</strong> を選択します。

1. 作成したエンドポイントを選択します。

    ![エンドポイントを選択します。](../../../../../../translated_images/ja/07-09-check-deployment.325d18cae8475ef4.webp)

1. このページでデプロイ中のエンドポイントの管理が可能です。

> [!NOTE]
> デプロイが完了したら、<strong>ライブトラフィック</strong> が **100%** に設定されていることを確認してください。そうでない場合は <strong>トラフィック更新</strong> を選択してトラフィック設定を調整します。トラフィックが0％の場合はモデルのテストができません。
>
> ![トラフィックを設定します。](../../../../../../translated_images/ja/07-10-set-traffic.085b847e5751ff3d.webp)
>

## シナリオ 3: Prompt flow と統合し、Microsoft Foundry でカスタムモデルとチャット

### カスタム Phi-3 モデルを Prompt flow に統合

ファインチューニングしたモデルを正常にデプロイした後、Prompt Flow と統合してリアルタイムアプリケーションでモデルを利用できるようにします。これにより、カスタム Phi-3 モデルを使ったさまざまなインタラクティブタスクが可能になります。

この演習で行うこと：

- Microsoft Foundry Hub を作成します。
- Microsoft Foundry プロジェクトを作成します。
- Prompt flow を作成します。
- ファインチューニング済み Phi-3 モデル用のカスタム接続を追加します。
- カスタム Phi-3 モデルとチャットできるように Prompt flow を設定します。

> [!NOTE]
> Azure ML Studio を使っても Prompt flow と統合可能です。同じ統合プロセスが Azure ML Studio にも適用されます。

#### Microsoft Foundry Hub の作成

プロジェクトを作成する前に Hub を作成する必要があります。Hub はリソースグループのように機能し、Microsoft Foundry 内で複数のプロジェクトを整理・管理するためのものです。
1. [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) にアクセスします。

1. 左側のタブから **All hubs** を選択します。

1. ナビゲーションメニューから **+ New hub** を選択します。

    ![Create hub.](../../../../../../translated_images/ja/08-01-create-hub.8f7dd615bb8d9834.webp)

1. 次の作業を行います：

    - **Hub name** を入力します。これは一意の値でなければなりません。
    - Azure の **Subscription** を選択します。
    - 使用する **Resource group** を選択します（必要に応じて新規作成）。
    - 使用したい **Location** を選択します。
    - 使用する **Connect Azure AI Services** を選択します（必要に応じて新規作成）。
    - **Connect Azure AI Search** は **Skip connecting** を選択します。

    ![Fill hub.](../../../../../../translated_images/ja/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. **Next** を選択します。

#### Microsoft Foundry プロジェクトの作成

1. 作成した Hub で、左側のタブから **All projects** を選択します。

1. ナビゲーションメニューから **+ New project** を選択します。

    ![Select new project.](../../../../../../translated_images/ja/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. **Project name** を入力します。一意の値である必要があります。

    ![Create project.](../../../../../../translated_images/ja/08-05-create-project.4d97f0372f03375a.webp)

1. **Create a project** を選択します。

#### ファインチューニングした Phi-3 モデル用のカスタム接続を追加する

カスタム Phi-3 モデルを Prompt flow と統合するには、モデルのエンドポイントとキーをカスタム接続に保存する必要があります。この設定により、Prompt flow 内でカスタム Phi-3 モデルにアクセスできます。

#### ファインチューニングした Phi-3 モデルの api key と endpoint uri の設定

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) にアクセスします。

1. 作成した Azure Machine learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

    ![Select endpoints.](../../../../../../translated_images/ja/08-06-select-endpoints.aff38d453bcf9605.webp)

1. 作成したエンドポイントを選択します。

    ![Select endpoints.](../../../../../../translated_images/ja/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. ナビゲーションメニューから **Consume** を選択します。

1. **REST endpoint** と **Primary key** をコピーします。

    ![Copy api key and endpoint uri.](../../../../../../translated_images/ja/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### カスタム接続の追加

1. [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) にアクセスします。

1. 作成した Microsoft Foundry プロジェクトに移動します。

1. 作成したプロジェクトで、左側のタブから **Settings** を選択します。

1. **+ New connection** を選択します。

    ![Select new connection.](../../../../../../translated_images/ja/08-09-select-new-connection.02eb45deadc401fc.webp)

1. ナビゲーションメニューから **Custom keys** を選択します。

    ![Select custom keys.](../../../../../../translated_images/ja/08-10-select-custom-keys.856f6b2966460551.webp)

1. 次の作業を行います：

    - **+ Add key value pairs** を選択します。
    - キー名に **endpoint** と入力し、Azure ML Studio からコピーしたエンドポイントを値の欄に貼り付けます。
    - 再度 **+ Add key value pairs** を選択します。
    - キー名に **key** と入力し、Azure ML Studio からコピーしたキーを値の欄に貼り付けます。
    - キーを追加した後、キーが漏洩しないように **is secret** を選択します。

    ![Add connection.](../../../../../../translated_images/ja/08-11-add-connection.785486badb4d2d26.webp)

1. **Add connection** を選択します。

#### Prompt flow の作成

Microsoft Foundry にカスタム接続を追加しました。次に、以下の手順で Prompt flow を作成します。その後、この Prompt flow をカスタム接続に接続して、ファインチューニングしたモデルを Prompt flow 内で使用できるようにします。

1. 作成した Microsoft Foundry プロジェクトに移動します。

1. 左側のタブから **Prompt flow** を選択します。

1. ナビゲーションメニューから **+ Create** を選択します。

    ![Select Promptflow.](../../../../../../translated_images/ja/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. ナビゲーションメニューから **Chat flow** を選択します。

    ![Select chat flow.](../../../../../../translated_images/ja/08-13-select-flow-type.2ec689b22da32591.webp)

1. 使用する **Folder name** を入力します。

    ![Enter name.](../../../../../../translated_images/ja/08-14-enter-name.ff9520fefd89f40d.webp)

2. **Create** を選択します。

#### カスタム Phi-3 モデルとチャットするための Prompt flow 設定

ファインチューニングした Phi-3 モデルを Prompt flow に統合する必要があります。しかし、既存の Prompt flow はこの目的には設計されていません。そのため、カスタムモデルを統合できるように Prompt flow を再設計する必要があります。

1. Prompt flow で、既存のフローを再構築するために次の作業を行います：

    - **Raw file mode** を選択します。
    - *flow.dag.yml* ファイルの既存コードをすべて削除します。
    - *flow.dag.yml* ファイルに以下のコードを追加します。

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

    ![Select raw file mode.](../../../../../../translated_images/ja/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. *integrate_with_promptflow.py* ファイルに以下のコードを追加して、Prompt flow でカスタム Phi-3 モデルを使用します。

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # ロギング設定
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

        # 「connection」はカスタムコネクションの名前、「endpoint」、「key」はカスタムコネクション内のキーです
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
            
            # 完全なJSON応答をログに記録する
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

    ![Paste prompt flow code.](../../../../../../translated_images/ja/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Microsoft Foundry での Prompt flow の使用に関する詳細は、[Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) を参照してください。

1. **Chat input**、**Chat output** を選択して、モデルとチャットできるようにします。

    ![Input Output.](../../../../../../translated_images/ja/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. これでカスタム Phi-3 モデルとチャットする準備が整いました。次の演習では、Prompt flow の起動方法とファインチューニングした Phi-3 モデルを使ってチャットする方法を学びます。

> [!NOTE]
>
> 再構築したフローは以下の画像のようになります：
>
> ![Flow example.](../../../../../../translated_images/ja/08-18-graph-example.d6457533952e690c.webp)
>

### カスタム Phi-3 モデルとチャットする

ファインチューニングしたカスタム Phi-3 モデルを Prompt flow に統合したので、今すぐにでも対話を開始できます。この演習では、Prompt flow を使ってモデルとのチャットを設定し開始する手順を案内します。これらの手順に従うことで、ファインチューニングされた Phi-3 モデルの能力を様々なタスクや会話に最大限活用できるようになります。

- Prompt flow を使ってカスタム Phi-3 モデルとチャットします。

#### Prompt flow の開始

1. **Start compute sessions** を選択して Prompt flow を開始します。

    ![Start compute session.](../../../../../../translated_images/ja/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. **Validate and parse input** を選択してパラメータを更新します。

    ![Validate input.](../../../../../../translated_images/ja/09-02-validate-input.317c76ef766361e9.webp)

1. 作成したカスタム接続の **connection** の **Value** を選択します。例：*connection*。

    ![Connection.](../../../../../../translated_images/ja/09-03-select-connection.99bdddb4b1844023.webp)

#### カスタムモデルとチャットする

1. **Chat** を選択します。

    ![Select chat.](../../../../../../translated_images/ja/09-04-select-chat.61936dce6612a1e6.webp)

1. 結果の例は以下の通りです：これでカスタム Phi-3 モデルとチャットすることができます。ファインチューニングに使用したデータに基づいた質問をすることをお勧めします。

    ![Chat with prompt flow.](../../../../../../translated_images/ja/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文のネイティブ言語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じる誤解や誤訳について、当方は一切の責任を負いません。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->