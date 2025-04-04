<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e42c399dcc2fa477925d3ef4038d403",
  "translation_date": "2025-04-04T12:42:15+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\E2E_Phi-3-MLflow.md",
  "language_code": "ja"
}
-->
# MLflow

[MLflow](https://mlflow.org/) は、機械学習ライフサイクル全体を管理するために設計されたオープンソースプラットフォームです。

![MLFlow](../../../../../../translated_images/MlFlowmlops.e5d74ef39e988d267f5da3174105d728e556b25cee7d686689174acb1f07a11a.ja.png)

MLFlowは、実験、再現性、デプロイメント、中央モデルレジストリを含むMLライフサイクルを管理するために使用されます。現在、MLFlowは以下の4つのコンポーネントを提供しています。

- **MLflow Tracking:** 実験、コード、データ構成、結果を記録し、クエリを実行します。
- **MLflow Projects:** データサイエンスコードを任意のプラットフォームで再現可能な形式でパッケージ化します。
- **Mlflow Models:** 様々なサービング環境に機械学習モデルをデプロイします。
- **Model Registry:** モデルを中央リポジトリに保存、注釈付け、管理します。

MLFlowは、実験の追跡、コードを再現可能な実行形式にパッケージ化、モデルの共有およびデプロイメントの機能を備えています。MLFlowはDatabricksに統合されており、さまざまなMLライブラリをサポートしているため、ライブラリに依存しません。REST APIとCLIを提供しているため、任意の機械学習ライブラリやプログラミング言語で使用できます。

![MLFlow](../../../../../../translated_images/MLflow2.74e3f1a430b83b5379854d81f4d2d125b6e5a0f35f46b57625761d1f0597bc53.ja.png)

MLFlowの主な特徴は以下の通りです：

- **実験追跡:** パラメータと結果を記録して比較します。
- **モデル管理:** モデルを様々なサービングおよび推論プラットフォームにデプロイします。
- **モデルレジストリ:** MLFlowモデルのライフサイクルを共同で管理し、バージョン管理や注釈付けを行います。
- **プロジェクト:** MLコードを共有または本番環境で使用できるようにパッケージ化します。

MLFlowは、データ準備、モデルの登録と管理、モデルの実行用パッケージ化、サービスのデプロイメント、モデルの監視を含むMLOpsループをサポートしています。特にクラウドやエッジ環境において、プロトタイプから本番ワークフローへの移行プロセスを簡素化することを目指しています。

## E2Eシナリオ - ラッパーを構築し、Phi-3をMLFlowモデルとして使用する

このE2Eサンプルでは、Phi-3の小型言語モデル（SLM）をラップする2つの異なるアプローチを示し、それをMLFlowモデルとしてローカルまたはクラウド（例えばAzure Machine Learningワークスペース）で実行します。

![MLFlow](../../../../../../translated_images/MlFlow1.03b29de8b4a8f3706a3e7b229c94a81ece6e3ba983c78592ed332f3ef6efcfe0.ja.png)

| プロジェクト | 説明 | 場所 |
| ------------ | ----------- | -------- |
| Transformer Pipeline | Transformer Pipelineは、HuggingFaceモデルをMLFlowの実験的なtransformersフレーバーと共に使用したい場合に最も簡単なラッパー構築オプションです。 | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| Custom Python Wrapper | 記述時点では、transformer pipelineはONNX形式のHuggingFaceモデルに対するMLFlowラッパー生成をサポートしていませんでした。こうしたケースでは、MLFlowモード用のカスタムPythonラッパーを構築できます。 | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## プロジェクト: Transformer Pipeline

1. MLFlowとHuggingFaceから必要なPythonパッケージを準備します：

    ``` Python
    import mlflow
    import transformers
    ```

2. 次に、HuggingFaceレジストリ内のターゲットPhi-3モデルを参照してtransformer pipelineを開始します。_Phi-3-mini-4k-instruct_のモデルカードを見ると、そのタスクが「テキスト生成」タイプであることがわかります：

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. Phi-3モデルのtransformer pipelineをMLFlow形式で保存し、ターゲットアーティファクトパス、特定のモデル設定、推論APIタイプなどの追加詳細を提供します：

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## プロジェクト: Custom Python Wrapper

1. ここではMicrosoftの[ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai)を利用してONNXモデルの推論およびトークンのエンコード/デコードを行います。以下の例では、ターゲット計算環境としてCPUを対象に_onnxruntime_genai_パッケージを選択します：

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

2. カスタムクラスは2つのメソッドを実装します：_load_context()_はPhi-3 Mini 4K Instructの**ONNXモデル**、**ジェネレータパラメータ**、**トークナイザー**を初期化し、_predict()_は提供されたプロンプトに対して出力トークンを生成します：

    ``` Python
    class Phi3Model(mlflow.pyfunc.PythonModel):
        def load_context(self, context):
            # Retrieving model from the artifacts
            model_path = context.artifacts["phi3-mini-onnx"]
            model_options = {
                 "max_length": 300,
                 "temperature": 0.2,         
            }
        
            # Defining the model
            self.phi3_model = og.Model(model_path)
            self.params = og.GeneratorParams(self.phi3_model)
            self.params.set_search_options(**model_options)
            
            # Defining the tokenizer
            self.tokenizer = og.Tokenizer(self.phi3_model)
    
        def predict(self, context, model_input):
            # Retrieving prompt from the input
            prompt = model_input["prompt"][0]
            self.params.input_ids = self.tokenizer.encode(prompt)
    
            # Generating the model's response
            response = self.phi3_model.generate(self.params)
    
            return self.tokenizer.decode(response[0][len(self.params.input_ids):])
    ```

3. _mlflow.pyfunc.log_model()_関数を使用して、Phi-3モデル用のカスタムPythonラッパー（pickle形式）を生成し、元のONNXモデルおよび必要な依存関係を含めます：

    ``` Python
    model_info = mlflow.pyfunc.log_model(
        artifact_path = artifact_path,
        python_model = Phi3Model(),
        artifacts = {
            "phi3-mini-onnx": "cpu_and_mobile/cpu-int4-rtn-block-32-acc-level-4",
        },
        input_example = input_example,
        signature = infer_signature(input_example, ["Run"]),
        extra_pip_requirements = ["torch", "onnxruntime_genai", "numpy"],
    )
    ```

## 生成されたMLFlowモデルのシグネチャ

1. 上記のTransformer Pipelineプロジェクトのステップ3では、MLFlowモデルのタスクを「_llm/v1/chat_」に設定しました。この指示により、以下のようにOpenAIのChat APIと互換性のあるモデルのAPIラッパーが生成されます：

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

2. その結果、以下の形式でプロンプトを送信できます：

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

3. 次に、OpenAI API互換の後処理（例：_response[0][‘choices’][0][‘message’][‘content’]_）を使用して、出力を以下のように整えることができます：

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

4. 上記のCustom Python Wrapperプロジェクトのステップ3では、与えられた入力例からMLFlowパッケージがモデルのシグネチャを生成することを許可しました。我々のMLFlowラッパーのシグネチャは以下のようになります：

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

5. そのため、プロンプトには以下のように「prompt」辞書キーを含める必要があります：

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

6. モデルの出力は文字列形式で提供されます：

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記述された文書が正式な情報源とみなされるべきです。重要な情報については、専門的な人間による翻訳を推奨します。この翻訳の利用によって生じる誤解や誤解釈について、当方は一切責任を負いません。