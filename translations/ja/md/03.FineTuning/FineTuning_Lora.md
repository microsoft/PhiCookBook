<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:29:04+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "ja"
}
-->
# **LoRAを使ったPhi-3のファインチューニング**

MicrosoftのPhi-3 Mini言語モデルを、カスタムチャット指示データセットで[LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo)を用いてファインチューニングします。

LoRAは会話の理解力と応答生成の向上に役立ちます。

## Phi-3 Miniをファインチューニングする手順：

**インポートとセットアップ**

loralibのインストール

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

datasets、transformers、peft、trl、torchなど必要なライブラリをインポートして始めます。  
トレーニングの進行を追跡するためにログ設定を行います。

一部のレイヤーをloralibで実装された対応レイヤーに置き換えて適応させることも可能です。現在サポートしているのはnn.Linear、nn.Embedding、nn.Conv2dのみです。  
また、単一のnn.Linearが複数のレイヤーを表す場合（例えば一部のattentionのqkvプロジェクション実装など）に対応するMergedLinearもサポートしています（詳細は追加の注意事項を参照）。

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

トレーニングループ開始前に、LoRAパラメータのみを学習可能にマークします。

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

チェックポイントを保存する際は、LoRAパラメータのみを含むstate_dictを生成します。

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

load_state_dictでチェックポイントを読み込む際は、strict=Falseに設定してください。

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

これで通常通りトレーニングを進められます。

**ハイパーパラメータ**

training_configとpeft_configの2つの辞書を定義します。  
training_configには学習率、バッチサイズ、ログ設定などトレーニングに関するハイパーパラメータを含みます。

peft_configはLoRAに関するパラメータ（ランク、ドロップアウト、タスクタイプなど）を指定します。

**モデルとトークナイザーの読み込み**

事前学習済みPhi-3モデルのパス（例："microsoft/Phi-3-mini-4k-instruct"）を指定します。  
モデル設定にはキャッシュの使用、データ型（混合精度用のbfloat16）、アテンションの実装方法などを含めます。

**トレーニング**

カスタムチャット指示データセットを使ってPhi-3モデルをファインチューニングします。  
peft_configのLoRA設定を活用して効率的に適応させます。  
指定したログ戦略でトレーニングの進行を監視します。  
評価と保存：ファインチューニング済みモデルを評価し、トレーニング中にチェックポイントを保存します。

**サンプル**  
- [このサンプルノートブックでさらに学ぶ](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Pythonファインチューニングサンプルの例](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Hugging Face HubでのLoRAファインチューニング例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Hugging Faceモデルカードの例 - LoRAファインチューニングサンプル](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Hugging Face HubでのQLORAファインチューニング例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。