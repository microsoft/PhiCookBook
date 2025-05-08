<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-08T05:17:08+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "ja"
}
-->
# **LoRAを使ったPhi-3のファインチューニング**

MicrosoftのPhi-3 Mini言語モデルを、カスタムチャット指示データセットで[LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo)を用いてファインチューニングします。

LoRAは会話の理解と応答生成の向上に役立ちます。

## Phi-3 Miniをファインチューニングする手順：

**インポートとセットアップ**

loralibのインストール

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

datasets、transformers、peft、trl、torchなどの必要なライブラリをインポートします。  
トレーニングの進行を追跡するためにログ設定を行います。

一部のレイヤーをloralibで実装されたものに置き換えて適応させることも可能です。現在サポートしているのはnn.Linear、nn.Embedding、nn.Conv2dのみです。さらに、単一のnn.Linearが複数のレイヤーを表す場合（例：attentionのqkv投影の一部実装）に対応するMergedLinearもサポートしています（詳細は追加の注意事項を参照）。

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

トレーニングループが始まる前に、LoRAパラメータのみを学習可能に設定します。

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

チェックポイントを保存するときは、LoRAパラメータだけを含むstate_dictを生成します。

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

training_configとpeft_configの2つの辞書を定義します。training_configには学習率、バッチサイズ、ログ設定などのトレーニング用ハイパーパラメータを含みます。

peft_configにはLoRAに関するパラメータ（rank、dropout、タスクタイプなど）を指定します。

**モデルとトークナイザーの読み込み**

事前学習済みのPhi-3モデル（例："microsoft/Phi-3-mini-4k-instruct"）のパスを指定します。キャッシュの利用、データタイプ（混合精度のためbfloat16）、アテンションの実装などモデル設定を行います。

**トレーニング**

カスタムチャット指示データセットを使ってPhi-3モデルをファインチューニングします。peft_configのLoRA設定を活用し効率的に適応させます。指定したログ設定でトレーニングの進行を監視します。  
評価と保存：ファインチューニングしたモデルを評価し、トレーニング中にチェックポイントを保存して後で利用できるようにします。

**サンプル**  
- [このサンプルノートブックでさらに学ぶ](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Pythonファインチューニングサンプルの例](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Hugging Face HubでのLoRAファインチューニング例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Hugging Faceモデルカードの例 - LoRAファインチューニングサンプル](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Hugging Face HubでのQLORAファインチューニング例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。正式な情報源としては、原文のオリジナル言語の文書を参照してください。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳について、当方は一切責任を負いません。