<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aed7639909ebbd1960507880cff2ae4c",
  "translation_date": "2025-04-04T11:28:48+00:00",
  "source_file": "code\\04.Finetuning\\olive-ort-example\\README.md",
  "language_code": "ja"
}
-->
# Oliveを使用してPhi3を微調整する

この例では、Oliveを使用して以下を行います：

1. LoRAアダプターを微調整し、フレーズを「悲しい」「喜び」「恐れ」「驚き」に分類します。
1. アダプターの重みをベースモデルに統合します。
1. モデルを最適化し、`int4`に量子化します。

さらに、ONNX Runtime (ORT) の Generate API を使用して微調整されたモデルを推論する方法も示します。

> **⚠️ 微調整を行うには、適切なGPUが必要です。例えば、A10、V100、A100などが挙げられます。**

## 💾 インストール

新しいPython仮想環境を作成します（例えば、`conda`を使用して）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

次に、Oliveと微調整ワークフローの依存関係をインストールします：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Oliveを使用してPhi3を微調整する
[Olive設定ファイル](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json)には、以下の*パス*を含む*ワークフロー*が記載されています：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

このワークフローの概要は以下の通りです：

1. [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json) のデータを使用してPhi3を微調整します（150ステップで設定されていますが、変更可能です）。
1. LoRAアダプターの重みをベースモデルに統合します。これにより、ONNX形式の単一モデルアーティファクトが得られます。
1. Model BuilderがモデルをONNX Runtime用に最適化し、`int4`に量子化します。

ワークフローを実行するには、以下を実行します：

```bash
olive run --config phrase-classification.json
```

Oliveの処理が完了すると、最適化された`int4`微調整Phi3モデルが以下に保存されます：  
`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`

## 🧑‍💻 微調整されたPhi3をアプリケーションに統合する

アプリを実行するには：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

この応答は、フレーズの分類結果（悲しい/喜び/恐れ/驚き）を表す単語である必要があります。

**免責事項**:  
この文書はAI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を公式な情報源とみなしてください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や解釈の誤りについて、当方は責任を負いかねます。