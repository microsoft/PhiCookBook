<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-07-16T16:24:48+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "ja"
}
-->
# Oliveを使ってPhi3をファインチューニングする

この例では、Oliveを使って以下を行います：

1. LoRAアダプターをファインチューニングして、フレーズをSad、Joy、Fear、Surpriseに分類する。
1. アダプターの重みをベースモデルにマージする。
1. モデルを`int4`に最適化および量子化する。

また、ONNX Runtime (ORT) Generate APIを使ってファインチューニング済みモデルを推論する方法も紹介します。

> **⚠️ ファインチューニングには、適切なGPU（例：A10、V100、A100）が必要です。**

## 💾 インストール

新しいPython仮想環境を作成します（例：`conda`を使用）：

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

## 🧪 Oliveを使ってPhi3をファインチューニングする
[Oliveの設定ファイル](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json)には、以下の*パス*を含む*ワークフロー*が定義されています：

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

大まかにこのワークフローは以下を行います：

1. [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)のデータを使ってPhi3を150ステップ（変更可能）ファインチューニングする。
1. LoRAアダプターの重みをベースモデルにマージする。これによりONNX形式の単一モデルアーティファクトが得られる。
1. Model BuilderがONNXランタイム用にモデルを最適化し、`int4`に量子化する。

ワークフローを実行するには、以下を実行してください：

```bash
olive run --config phrase-classification.json
```

Oliveの処理が完了すると、最適化された`int4`ファインチューニング済みPhi3モデルが以下に保存されます：`code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`

## 🧑‍💻 ファインチューニング済みPhi3をアプリケーションに統合する

アプリを実行するには：

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

このレスポンスはフレーズの単語分類（Sad/Joy/Fear/Surprise）のみを返します。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。