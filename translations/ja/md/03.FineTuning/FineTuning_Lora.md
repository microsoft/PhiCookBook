<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "98eb289883c5e181a74e72a59e1ddc6d",
  "translation_date": "2025-04-04T13:12:47+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Lora.md",
  "language_code": "ja"
}
-->
# **Phi-3をLoRAでファインチューニングする**

MicrosoftのPhi-3 Mini言語モデルを、カスタムチャット指示データセットを使用して[LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo)でファインチューニングします。

LoRAを利用することで、会話の理解や応答生成を向上させることができます。

## Phi-3 Miniをファインチューニングする手順ガイド:

**インポートとセットアップ**

loralibのインストール

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

必要なライブラリ（datasets、transformers、peft、trl、torchなど）をインポートすることから始めます。
トレーニングプロセスを追跡するためにログを設定します。

いくつかのレイヤーをloralibで実装された対応するレイヤーに置き換えることができます。現在サポートされているのは、nn.Linear、nn.Embedding、nn.Conv2dのみです。また、注意のqkvプロジェクションの一部実装のように、単一のnn.Linearが複数のレイヤーを表す場合に対応するMergedLinearもサポートしています（詳細については追加の注記を参照してください）。

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

トレーニングループが始まる前に、LoRAのパラメータのみをトレーニング可能としてマークします。

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

チェックポイントを保存する際には、LoRAのパラメータのみを含むstate_dictを生成します。

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dictを使用してチェックポイントを読み込む際には、strict=Falseを設定することを忘れないでください。

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

これで通常通りトレーニングを進めることができます。

**ハイパーパラメータ**

2つの辞書を定義します：training_configとpeft_config。training_configには学習率、バッチサイズ、ログ設定など、トレーニング用のハイパーパラメータを含めます。

peft_configにはLoRA関連のパラメータ（rank、dropout、タスクタイプなど）を指定します。

**モデルとトークナイザーの読み込み**

事前学習済みPhi-3モデルのパスを指定します（例: "microsoft/Phi-3-mini-4k-instruct"）。キャッシュ使用、データ型（混合精度用のbfloat16）、注意実装など、モデル設定を構成します。

**トレーニング**

カスタムチャット指示データセットを使用してPhi-3モデルをファインチューニングします。peft_configで指定されたLoRA設定を活用して効率的に適応を行います。指定されたログ戦略を使用してトレーニングの進行状況を監視します。

**評価と保存**

ファインチューニングされたモデルを評価します。
後で使用するためにトレーニング中にチェックポイントを保存します。

**サンプル**
- [このサンプルノートブックでさらに学ぶ](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Pythonファインチューニングのサンプル例](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face HubでLoRAを使用したファインチューニング例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Faceモデルカードの例 - LoRAファインチューニングサンプル](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face HubでQLORAを使用したファインチューニング例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確さが含まれる場合がありますのでご了承ください。元の言語で記載された文書を公式の情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の利用に起因する誤解や解釈の誤りについて、当社は一切の責任を負いません。