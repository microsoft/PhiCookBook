<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "944949f040e61b2ea25b3460f7394fd4",
  "translation_date": "2025-07-17T07:06:57+00:00",
  "source_file": "md/03.FineTuning/FineTuning_MLSDK.md",
  "language_code": "ja"
}
-->
## Azure ML システムレジストリの chat-completion コンポーネントを使ってモデルをファインチューニングする方法

この例では、Phi-3-mini-4k-instruct モデルを ultrachat_200k データセットを使って2人の会話を完結させるタスクでファインチューニングします。

![MLFineTune](../../../../translated_images/MLFineTune.928d4c6b3767dd35.ja.png)

この例では、Azure ML SDK と Python を使ってファインチューニングを行い、その後ファインチューニング済みモデルをオンラインエンドポイントにデプロイしてリアルタイム推論を行う方法を示します。

### トレーニングデータ

ultrachat_200k データセットを使用します。これは UltraChat データセットを厳選したもので、最先端の7Bチャットモデルである Zephyr-7B-β のトレーニングに使われました。

### モデル

Phi-3-mini-4k-instruct モデルを使って、チャット完了タスクのためにモデルをファインチューニングする方法を示します。このノートブックを特定のモデルカードから開いた場合は、モデル名を適宜置き換えてください。

### タスク

- ファインチューニングするモデルを選ぶ
- トレーニングデータを選び、確認する
- ファインチューニングジョブを設定する
- ファインチューニングジョブを実行する
- トレーニングと評価のメトリクスを確認する
- ファインチューニング済みモデルを登録する
- ファインチューニング済みモデルをリアルタイム推論用にデプロイする
- リソースをクリーンアップする

## 1. 前提条件のセットアップ

- 依存関係をインストールする
- AzureML ワークスペースに接続する。SDK 認証のセットアップについてはこちらを参照。以下の <WORKSPACE_NAME>、<RESOURCE_GROUP>、<SUBSCRIPTION_ID> を置き換えてください。
- azureml システムレジストリに接続する
- 任意で実験名を設定する
- コンピュートを確認または作成する

> [!NOTE]
> 要件として、単一の GPU ノードは複数の GPU カードを持つことができます。例えば、Standard_NC24rs_v3 の1ノードには4つの NVIDIA V100 GPU が搭載されており、Standard_NC12s_v3 には2つの NVIDIA V100 GPU があります。この情報はドキュメントを参照してください。ノードあたりの GPU カード数は下記のパラメータ gpus_per_node で設定します。この値を正しく設定することでノード内のすべての GPU を活用できます。推奨される GPU コンピュート SKU はこちらとこちらで確認できます。

### Python ライブラリ

以下のセルを実行して依存関係をインストールします。新しい環境で実行する場合は必須のステップです。

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML とのやり取り

1. この Python スクリプトは Azure Machine Learning (Azure ML) サービスとやり取りするためのものです。内容を簡単に説明します：

    - azure.ai.ml、azure.identity、azure.ai.ml.entities パッケージから必要なモジュールをインポートします。また time モジュールもインポートします。

    - DefaultAzureCredential() を使って認証を試みます。これは Azure クラウド上でアプリケーションを素早く開発するための簡易認証方法です。失敗した場合は InteractiveBrowserCredential() にフォールバックし、対話的なログインを促します。

    - from_config メソッドを使って MLClient インスタンスを作成し、デフォルトの設定ファイル (config.json) から設定を読み込みます。失敗した場合は subscription_id、resource_group_name、workspace_name を手動で指定して MLClient インスタンスを作成します。

    - Azure ML レジストリ "azureml" 用の MLClient インスタンスも作成します。このレジストリにはモデル、ファインチューニングパイプライン、環境が保存されています。

    - experiment_name を "chat_completion_Phi-3-mini-4k-instruct" に設定します。

    - 現在の時刻（エポック秒の浮動小数点数）を整数に変換し文字列化して一意のタイムスタンプを生成します。これはユニークな名前やバージョン作成に使えます。

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

## 2. ファインチューニングする基盤モデルを選ぶ

1. Phi-3-mini-4k-instruct は38億パラメータの軽量で最先端のオープンモデルで、Phi-2 のデータセットを基に構築されています。このモデルは Phi-3 ファミリーに属し、Mini バージョンはコンテキスト長（トークン数）4K と 128K の2種類があります。特定の用途に使うためにはファインチューニングが必要です。AzureML Studio のモデルカタログでチャット完了タスクでフィルタリングしてこれらのモデルを閲覧できます。この例では Phi-3-mini-4k-instruct モデルを使用します。別のモデル用にこのノートブックを開いた場合は、モデル名とバージョンを適宜置き換えてください。

    > [!NOTE]
    > モデルの id プロパティはファインチューニングジョブの入力として渡されます。これは AzureML Studio のモデルカタログのモデル詳細ページの Asset ID フィールドでも確認できます。

2. この Python スクリプトは Azure Machine Learning (Azure ML) サービスとやり取りしています。内容を簡単に説明します：

    - model_name を "Phi-3-mini-4k-instruct" に設定します。

    - registry_ml_client オブジェクトの models プロパティの get メソッドを使い、指定した名前のモデルの最新バージョンを Azure ML レジストリから取得します。get メソッドはモデル名と最新バージョンを取得するラベルの2つの引数を取ります。

    - fine-tuning に使うモデルの名前、バージョン、id をコンソールに表示します。文字列の format メソッドで foundation_model オブジェクトの name、version、id プロパティを挿入しています。

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

## 3. ジョブで使うコンピュートを作成する

ファインチューニングジョブは GPU コンピュートでのみ動作します。コンピュートのサイズはモデルの大きさによって異なり、適切なコンピュートを選ぶのは難しい場合があります。このセルではユーザーが適切なコンピュートを選べるよう案内します。

> [!NOTE]
> 以下に挙げるコンピュートは最適化された構成で動作します。設定を変更すると Cuda Out Of Memory エラーが発生する可能性があります。その場合はより大きなコンピュートサイズにアップグレードしてください。

> [!NOTE]
> compute_cluster_size を選ぶ際は、そのコンピュートがリソースグループ内で利用可能か確認してください。利用できない場合はアクセス権のリクエストを行うことができます。

### ファインチューニング対応モデルの確認

1. この Python スクリプトは Azure Machine Learning (Azure ML) モデルとやり取りしています。内容を簡単に説明します：

    - Python の抽象構文木を処理する ast モジュールをインポートします。

    - foundation_model オブジェクト（Azure ML のモデルを表す）が finetune_compute_allow_list というタグを持っているか確認します。Azure ML のタグはキーと値のペアで、モデルのフィルタリングやソートに使えます。

    - finetune_compute_allow_list タグがあれば、その値（文字列）を ast.literal_eval で安全に Python のリストに変換し、computes_allow_list 変数に代入します。その後、リストからコンピュートを作成すべき旨のメッセージを表示します。

    - タグがなければ computes_allow_list を None に設定し、タグが存在しない旨のメッセージを表示します。

    - 要約すると、このスクリプトはモデルのメタデータに特定のタグがあるかを確認し、あればリストに変換してユーザーに知らせます。

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

### コンピュートインスタンスの確認

1. この Python スクリプトは Azure Machine Learning (Azure ML) サービスとやり取りし、コンピュートインスタンスに対して複数のチェックを行います。内容を簡単に説明します：

    - compute_cluster に格納された名前のコンピュートインスタンスを Azure ML ワークスペースから取得しようとします。プロビジョニング状態が "failed" なら ValueError を発生させます。

    - computes_allow_list が None でなければ、リスト内のすべてのコンピュートサイズを小文字に変換し、現在のコンピュートインスタンスのサイズがリストに含まれているか確認します。含まれていなければ ValueError を発生させます。

    - computes_allow_list が None の場合は、現在のコンピュートインスタンスのサイズがサポートされていない GPU VM サイズのリストに含まれているか確認し、含まれていれば ValueError を発生させます。

    - ワークスペース内の利用可能なすべてのコンピュートサイズのリストを取得し、現在のコンピュートインスタンスのサイズと一致するものを探します。一致した場合、そのコンピュートサイズの GPU 数を取得し、gpu_count_found を True に設定します。

    - gpu_count_found が True ならコンピュートインスタンスの GPU 数を表示し、False なら ValueError を発生させます。

    - 要約すると、このスクリプトは Azure ML ワークスペース内のコンピュートインスタンスに対して、プロビジョニング状態、許可リストや禁止リストとの照合、GPU 数の確認を行っています。

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

## 4. モデルのファインチューニング用データセットを選ぶ

1. ultrachat_200k データセットを使用します。このデータセットは4つの分割があり、教師ありファインチューニング（sft）に適しています。生成ランキング（gen）も含まれます。各分割のサンプル数は以下の通りです：

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. 次のいくつかのセルではファインチューニングのための基本的なデータ準備を示します：

### データの一部を可視化する

このサンプルは素早く実行できるように、すでに絞り込んだ行の5%を含む train_sft、test_sft ファイルを保存します。これによりファインチューニング済みモデルの精度は低くなり、実運用には適しません。download-dataset.py は ultrachat_200k データセットをダウンロードし、ファインチューニングパイプラインコンポーネントで利用可能な形式に変換します。データセットが大きいため、ここでは一部のみ扱います。

1. 以下のスクリプトはデータの5%のみをダウンロードします。dataset_split_pc パラメータを変更することで割合を増やせます。

    > [!NOTE]
    > 一部の言語モデルは異なる言語コードを持つため、データセットのカラム名もそれに合わせる必要があります。

1. データの例は以下のようになります。チャット完了データセットは parquet 形式で保存され、各エントリは以下のスキーマを持ちます：

    - これは JSON (JavaScript Object Notation) ドキュメントで、データ交換に広く使われる形式です。実行可能なコードではなく、データの保存・転送方法です。構造は以下の通りです：

    - "prompt": AI アシスタントに対するタスクや質問を表す文字列です。

    - "messages": 配列で、ユーザーと AI アシスタント間の会話のメッセージを表します。各メッセージはオブジェクトで、2つのキーを持ちます：

    - "content": メッセージの内容を表す文字列です。
    - "role": メッセージを送った主体の役割を表す文字列で、"user" または "assistant" です。
    - "prompt_id": プロンプトの一意識別子を表す文字列です。

1. この JSON ドキュメントでは、ユーザーがディストピア小説の主人公を作成するよう AI アシスタントに依頼し、アシスタントが応答し、さらに詳細を求める会話が表現されています。会話全体は特定の prompt_id に紐づいています。

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

### データのダウンロード

1. この Python スクリプトは download-dataset.py というヘルパースクリプトを使ってデータセットをダウンロードします。内容を簡単に説明します：

    - os モジュールをインポートします。これは OS 依存の機能を扱うためのモジュールです。

    - os.system 関数を使い、download-dataset.py スクリプトをシェルで実行します。引数としてダウンロードするデータセット（HuggingFaceH4/ultrachat_200k）、保存先ディレクトリ（ultrachat_200k_dataset）、分割割合（5%）を指定しています。os.system は実行したコマンドの終了ステータスを返し、exit_status 変数に格納します。

    - exit_status が 0 でなければ（Unix系 OS では0が成功を示す）、例外を発生させてデータセットのダウンロードに失敗したことを通知します。

    - 要約すると、このスクリプトはヘルパースクリプトを使ってデータセットをダウンロードし、失敗した場合は例外を投げます。

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

### データを DataFrame に読み込む

1. この Python スクリプトは JSON Lines 形式のファイルを pandas の DataFrame に読み込み、最初の5行を表示します。内容を簡単に説明します：

    - pandas ライブラリをインポートします。これは強力なデータ操作・分析ライブラリです。

    - pandas の表示オプションで最大カラム幅を0に設定します。これにより DataFrame を表示する際に各カラムのテキストが切り捨てられず全て表示されます。

    - pd.read_json 関数を使い、ultrachat_200k_dataset ディレクトリ内の train_sft.jsonl ファイルを DataFrame に読み込みます。lines=True はファイルが JSON Lines 形式であることを示し、各行が独立した JSON オブジェクトであることを意味します。
- DataFrameの最初の5行を表示するためにheadメソッドを使用しています。DataFrameの行数が5未満の場合は、すべての行を表示します。

- 要約すると、このスクリプトはJSON LinesファイルをDataFrameに読み込み、最初の5行を全カラムのテキストとともに表示しています。

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

## 5. モデルとデータを入力としてファインチューニングジョブを送信する

chat-completionパイプラインコンポーネントを使用するジョブを作成します。ファインチューニングでサポートされているすべてのパラメーターについてはこちらをご覧ください。

### ファインチューニングパラメーターの定義

1. ファインチューニングパラメーターは大きく2つのカテゴリに分けられます - トレーニングパラメーターと最適化パラメーター

1. トレーニングパラメーターは以下のようなトレーニングに関する設定を定義します -

    - 使用するオプティマイザーやスケジューラー
    - ファインチューニングで最適化するメトリック
    - トレーニングステップ数やバッチサイズなど
    - 最適化パラメーターはGPUメモリの最適化や計算リソースの効率的な利用を助けます。

1. 以下はこのカテゴリに属するいくつかのパラメーターです。最適化パラメーターはモデルごとに異なり、これらの違いを処理するためにモデルと一緒にパッケージ化されています。

    - deepspeedとLoRAの有効化
    - 混合精度トレーニングの有効化
    - マルチノードトレーニングの有効化


> [!NOTE]
> 教師ありファインチューニングはアライメントの喪失や壊滅的忘却を引き起こす可能性があります。この問題を確認し、ファインチューニング後にアライメントステージを実行することを推奨します。

### ファインチューニングパラメーター

1. このPythonスクリプトは機械学習モデルのファインチューニング用パラメーターを設定しています。内容は以下の通りです：

    - トレーニングエポック数、トレーニングおよび評価のバッチサイズ、学習率、学習率スケジューラーの種類などのデフォルトのトレーニングパラメーターを設定しています。

    - Layer-wise Relevance Propagation (LoRa)やDeepSpeedの適用有無、DeepSpeedのステージなどのデフォルトの最適化パラメーターを設定しています。

    - トレーニングパラメーターと最適化パラメーターをfinetune_parametersという1つの辞書にまとめています。

    - foundation_modelにモデル固有のデフォルトパラメーターがあるかをチェックし、あれば警告メッセージを表示して、これらのモデル固有のデフォルトでfinetune_parametersを更新します。ast.literal_eval関数を使って文字列からPython辞書に変換しています。

    - 実行に使用される最終的なファインチューニングパラメーターを表示しています。

    - 要約すると、このスクリプトは機械学習モデルのファインチューニング用パラメーターを設定し、モデル固有のパラメーターで上書き可能にして表示しています。

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

### トレーニングパイプライン

1. このPythonスクリプトは機械学習トレーニングパイプラインの表示名を生成する関数を定義し、その関数を呼び出して表示名を生成・表示しています。内容は以下の通りです：

1. get_pipeline_display_name関数が定義されています。この関数はトレーニングパイプラインに関する様々なパラメーターに基づいて表示名を生成します。

1. 関数内で、デバイスあたりのバッチサイズ、勾配蓄積ステップ数、ノードあたりのGPU数、ファインチューニングに使用するノード数を掛け合わせて総バッチサイズを計算しています。

1. 学習率スケジューラーの種類、DeepSpeedの適用有無、DeepSpeedのステージ、LoRaの適用有無、保持するモデルチェックポイントの上限、最大シーケンス長などのパラメーターを取得しています。

1. これらのパラメーターをハイフンで区切った文字列を作成します。DeepSpeedやLoRaが適用されている場合は、それぞれ「ds」＋DeepSpeedステージや「lora」が含まれ、適用されていなければ「nods」や「nolora」が含まれます。

1. 関数はこの文字列を返し、トレーニングパイプラインの表示名として使われます。

1. 関数定義後に呼び出され、生成された表示名が表示されます。

1. 要約すると、このスクリプトは様々なパラメーターに基づいて機械学習トレーニングパイプラインの表示名を生成し、それを表示しています。

```python
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

### パイプラインの設定

このPythonスクリプトはAzure Machine Learning SDKを使って機械学習パイプラインを定義・設定しています。内容は以下の通りです：

1. Azure AI ML SDKから必要なモジュールをインポートしています。

1. レジストリから"chat_completion_pipeline"という名前のパイプラインコンポーネントを取得しています。

1. `@pipeline`デコレーターと`create_pipeline`関数を使ってパイプラインジョブを定義しています。パイプライン名は`pipeline_display_name`に設定されています。

1. `create_pipeline`関数内で、取得したパイプラインコンポーネントをモデルパス、各ステージのコンピュートクラスター、トレーニング・テスト用のデータセット分割、ファインチューニングに使用するGPU数、その他のファインチューニングパラメーターなどを指定して初期化しています。

1. ファインチューニングジョブの出力をパイプラインジョブの出力にマッピングしています。これはファインチューニング済みモデルを簡単に登録できるようにするためで、オンラインまたはバッチエンドポイントへのデプロイに必要です。

1. `create_pipeline`関数を呼び出してパイプラインのインスタンスを作成しています。

1. パイプラインの`force_rerun`設定を`True`にして、以前のジョブのキャッシュ結果を使わないようにしています。

1. パイプラインの`continue_on_step_failure`設定を`False`にして、いずれかのステップが失敗した場合にパイプラインを停止するようにしています。

1. 要約すると、このスクリプトはAzure Machine Learning SDKを使ってチャット完了タスク用の機械学習パイプラインを定義・設定しています。

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

### ジョブの送信

1. このPythonスクリプトはAzure Machine Learningワークスペースに機械学習パイプラインジョブを送信し、ジョブの完了を待機しています。内容は以下の通りです：

    - workspace_ml_clientのjobsオブジェクトのcreate_or_updateメソッドを呼び出してパイプラインジョブを送信します。実行するパイプラインはpipeline_objectで指定し、ジョブを実行する実験はexperiment_nameで指定します。

    - 続いて、workspace_ml_clientのjobsオブジェクトのstreamメソッドを呼び出してパイプラインジョブの完了を待ちます。待機対象のジョブはpipeline_jobオブジェクトのname属性で指定します。

    - 要約すると、このスクリプトはAzure Machine Learningワークスペースに機械学習パイプラインジョブを送信し、ジョブの完了を待機しています。

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

## 6. ファインチューニング済みモデルをワークスペースに登録する

ファインチューニングジョブの出力からモデルを登録します。これにより、ファインチューニング済みモデルとファインチューニングジョブ間の系譜が追跡されます。さらにファインチューニングジョブは基盤モデル、データ、トレーニングコードとの系譜を追跡します。

### MLモデルの登録

1. このPythonスクリプトはAzure Machine Learningパイプラインでトレーニングされた機械学習モデルを登録しています。内容は以下の通りです：

    - Azure AI ML SDKから必要なモジュールをインポートしています。

    - workspace_ml_clientのjobsオブジェクトのgetメソッドを呼び出し、パイプラインジョブのoutputs属性からtrained_model出力が利用可能かを確認しています。

    - パイプラインジョブ名と出力名("trained_model")を使ってトレーニング済みモデルのパスを構築しています。

    - 元のモデル名に"-ultrachat-200k"を付加し、スラッシュをハイフンに置き換えた名前をファインチューニング済みモデルの名前として定義しています。

    - Modelオブジェクトを作成し、モデルのパス、モデルタイプ(MLflowモデル)、名前、バージョン、説明などのパラメーターを指定してモデル登録の準備をしています。

    - workspace_ml_clientのmodelsオブジェクトのcreate_or_updateメソッドを呼び出してモデルを登録しています。

    - 登録されたモデルを表示しています。

1. 要約すると、このスクリプトはAzure Machine Learningパイプラインでトレーニングされた機械学習モデルを登録しています。

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

## 7. ファインチューニング済みモデルをオンラインエンドポイントにデプロイする

オンラインエンドポイントは、モデルを利用するアプリケーションと統合可能な耐久性のあるREST APIを提供します。

### エンドポイントの管理

1. このPythonスクリプトはAzure Machine Learningで登録済みモデル用のマネージドオンラインエンドポイントを作成しています。内容は以下の通りです：

    - Azure AI ML SDKから必要なモジュールをインポートしています。

    - "ultrachat-completion-"にタイムスタンプを付加した一意のオンラインエンドポイント名を定義しています。

    - ManagedOnlineEndpointオブジェクトを作成し、エンドポイント名、説明、認証モード("key")などのパラメーターを指定してオンラインエンドポイントの作成準備をしています。

    - workspace_ml_clientのbegin_create_or_updateメソッドを呼び出してオンラインエンドポイントを作成し、waitメソッドで作成完了を待機しています。

1. 要約すると、このスクリプトはAzure Machine Learningで登録済みモデル用のマネージドオンラインエンドポイントを作成しています。

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
> デプロイに対応しているSKUの一覧はこちらで確認できます - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### MLモデルのデプロイ

1. このPythonスクリプトはAzure Machine Learningのマネージドオンラインエンドポイントに登録済み機械学習モデルをデプロイしています。内容は以下の通りです：

    - Pythonの抽象構文木を処理するためのastモジュールをインポートしています。

    - デプロイに使用するインスタンスタイプを"Standard_NC6s_v3"に設定しています。

    - foundation_modelにinference_compute_allow_listタグがあるかをチェックし、あれば文字列からPythonリストに変換してinference_computes_allow_listに代入し、なければNoneに設定しています。

    - 指定したインスタンスタイプが許可リストに含まれているかを確認し、含まれていなければ許可リストから選択するようメッセージを表示しています。

    - ManagedOnlineDeploymentオブジェクトを作成し、デプロイ名、エンドポイント名、モデルID、インスタンスタイプと数、ライブネスプローブ設定、リクエスト設定などのパラメーターを指定してデプロイの準備をしています。

    - workspace_ml_clientのbegin_create_or_updateメソッドを呼び出してデプロイを作成し、waitメソッドで作成完了を待機しています。

    - エンドポイントのトラフィックを"demo"デプロイに100%割り当てるよう設定しています。

    - workspace_ml_clientのbegin_create_or_updateメソッドを呼び出してエンドポイントを更新し、resultメソッドで更新完了を待機しています。

1. 要約すると、このスクリプトはAzure Machine Learningのマネージドオンラインエンドポイントに登録済み機械学習モデルをデプロイしています。

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

## 8. サンプルデータでエンドポイントをテストする

テストデータセットからサンプルデータを取得し、オンラインエンドポイントに推論を送信します。その後、推論結果のラベルと正解ラベルを並べて表示します。

### 結果の読み込み

1. このPythonスクリプトはJSON LinesファイルをpandasのDataFrameに読み込み、ランダムサンプルを取得し、インデックスをリセットしています。内容は以下の通りです：

    - ./ultrachat_200k_dataset/test_gen.jsonlファイルをpandasのread_json関数で読み込んでいます。lines=True引数を指定しているのは、ファイルがJSON Lines形式で各行が独立したJSONオブジェクトだからです。

    - DataFrameからランダムに1行を抽出しています。sample関数のn=1引数で抽出行数を指定しています。

    - reset_index関数のdrop=True引数を使って元のインデックスを破棄し、デフォルトの整数インデックスに置き換えています。

    - head関数の引数2でDataFrameの最初の2行を表示しています。ただし、サンプリング後は1行しかないため、その1行のみ表示されます。

1. 要約すると、このスクリプトはJSON LinesファイルをpandasのDataFrameに読み込み、1行のランダムサンプルを取得してインデックスをリセットし、最初の行を表示しています。

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

### JSONオブジェクトの作成

1. このPythonスクリプトは特定のパラメーターを持つJSONオブジェクトを作成し、ファイルに保存しています。内容は以下の通りです：

    - JSONデータを扱うためのjsonモジュールをインポートしています。

    - 機械学習モデルのパラメーターを表す辞書parametersを作成しています。キーは"temperature"、"top_p"、"do_sample"、"max_new_tokens"で、それぞれの値は0.6、0.9、True、200です。

    - もう1つの辞書test_jsonを作成し、"input_data"と"params"の2つのキーを持ちます。"input_data"の値はさらに辞書で、"input_string"と"parameters"をキーに持ちます。"input_string"の値はtest_df DataFrameの最初のメッセージをリストにしたもの、"parameters"の値は先に作成したparameters辞書です。"params"の値は空の辞書です。
- sample_score.jsonという名前のファイルを開きます

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

### エンドポイントの呼び出し

1. このPythonスクリプトは、Azure Machine Learningのオンラインエンドポイントを呼び出してJSONファイルをスコアリングしています。以下はその内容の説明です：

    - workspace_ml_clientオブジェクトのonline_endpointsプロパティのinvokeメソッドを呼び出しています。このメソッドはオンラインエンドポイントにリクエストを送り、レスポンスを受け取るために使われます。

    - endpoint_nameとdeployment_name引数でエンドポイント名とデプロイメント名を指定しています。この場合、エンドポイント名はonline_endpoint_name変数に格納されており、デプロイメント名は「demo」です。

    - request_file引数でスコアリング対象のJSONファイルのパスを指定しています。この場合、ファイルは./ultrachat_200k_dataset/sample_score.jsonです。

    - エンドポイントからのレスポンスをresponse変数に格納しています。

    - 生のレスポンスを出力しています。

1. まとめると、このスクリプトはAzure Machine Learningのオンラインエンドポイントを呼び出してJSONファイルをスコアリングし、そのレスポンスを表示しています。

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

## 9. オンラインエンドポイントの削除

1. オンラインエンドポイントを削除するのを忘れないでください。そうしないと、エンドポイントで使用されたコンピューティングリソースの課金が続いてしまいます。このPythonコードはAzure Machine Learningのオンラインエンドポイントを削除しています。以下はその内容の説明です：

    - workspace_ml_clientオブジェクトのonline_endpointsプロパティのbegin_deleteメソッドを呼び出しています。このメソッドはオンラインエンドポイントの削除を開始するために使われます。

    - name引数で削除するエンドポイントの名前を指定しています。この場合、エンドポイント名はonline_endpoint_name変数に格納されています。

    - waitメソッドを呼び出して削除処理が完了するまで待機しています。これはブロッキング操作であり、削除が完了するまでスクリプトの実行が停止します。

    - まとめると、このコードはAzure Machine Learningのオンラインエンドポイントの削除を開始し、その処理が完了するまで待機しています。

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。