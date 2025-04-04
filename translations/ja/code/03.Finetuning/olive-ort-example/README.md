<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aed7639909ebbd1960507880cff2ae4c",
  "translation_date": "2025-04-04T11:25:53+00:00",
  "source_file": "code\\03.Finetuning\\olive-ort-example\\README.md",
  "language_code": "ja"
}
-->
# Oliveを使ってPhi3をファインチューニング

この例では、Oliveを使用して以下を行います：

1. LoRAアダプターをファインチューニングし、フレーズを「悲しい」「喜び」「恐怖」「驚き」に分類します。
1. アダプターの重みをベースモデルに統合します。
1. モデルを`int4`に最適化および量子化します。

さらに、ONNX Runtime (ORT) Generate APIを使用してファインチューニングされたモデルを推論する方法も紹介します。

> **⚠️ ファインチューニングを行うには、適切なGPUが必要です（例: A10, V100, A100）。**

## 💾 インストール

新しいPython仮想環境を作成します（例: `conda`を使用）：

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

次に、Oliveとファインチューニングワークフローに必要な依存関係をインストールします：

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Oliveを使ったPhi3のファインチューニング
[Oliveの設定ファイル](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json)には、以下の*パス*を含む*ワークフロー*が記載されています：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

このワークフローは以下を実行します：

1. [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json)データを使用してPhi3をファインチューニングします（150ステップ。ただし、これを変更可能）。
1. LoRAアダプターの重みをベースモデルに統合します。これにより、ONNX形式の単一モデルアーティファクトが生成されます。
1. Model BuilderがONNX Runtime用にモデルを最適化し、さらにモデルを`int4`に量子化します。

ワークフローを実行するには、以下を実行します：

```bash
olive run --config phrase-classification.json
```

Oliveが完了すると、最適化された`int4`ファインチューニングされたPhi3モデルが以下に保存されます：  
`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`

## 🧑‍💻 ファインチューニングされたPhi3をアプリケーションに統合

アプリを実行するには：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

この応答はフレーズの単語分類（「悲しい」「喜び」「恐怖」「驚き」）を返します。

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文書の母国語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の利用に起因する誤解や誤解釈について、当社は責任を負いません。