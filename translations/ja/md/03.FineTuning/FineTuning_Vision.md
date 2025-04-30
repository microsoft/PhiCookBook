<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dd1b570422a819b39b14a4c7be06c8fa",
  "translation_date": "2025-04-04T13:30:19+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Vision.md",
  "language_code": "ja"
}
-->
# Phi-3.5-vision ファインチューニング レシピ

これは、huggingfaceライブラリを使用したPhi-3.5-visionファインチューニングの公式サポートです。以下のコマンドを実行する前に、コードディレクトリ [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) に移動してください。

## インストール

```bash
# create a new conda environment
conda create -n phi3v python=3.10
conda activate phi3v

# install pytorch
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# other libraries needed to run the example code
pip install -r requirements.txt

# (optional) flash attention -- Ampere+ GPUs (e.g., A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (optional) QLoRA -- Turing+ GPUs (e.g., RTX 8000)
pip install bitsandbytes==0.43.1
```

## クイックスタート

DocVQAとヘイトフルミーム分類用の2つのファインチューニングスクリプトを提供しています。

最小限のハードウェア要件: 4x RTX8000 (GPUごとに48GB RAM)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-visionは現在、マルチイメージ入力を公式にサポートしています。以下はNLVR2のファインチューニング例です。

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## 使用ガイド

ハードウェアに応じて、ユーザーは異なるファインチューニング戦略を選択できます。完全ファインチューニング（Deepspeed Zero-2を使用）と、オプションで視覚パラメータを固定する方法、またはLoRA（4bit QLoRAを含む）をサポートしています。一般的には、可能であればフラッシュアテンションとbf16を使用した完全ファインチューニングを推奨します。

### カスタムデータセットを必要な形式に変換するためのガイド

最小限のビデオ分類データセット（UCF-101のサブセット）を使用して、カスタムデータセットを必要な形式に変換し、Phi-3.5-visionをファインチューニングする方法を示すエンドツーエンドの例を提供します。

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

変換後のデータは以下のようになります:

```bash
> tree --filelimit=10 /path/to/converted_ucf101
/path/to/converted_ucf101
├── images
│   ├── test
│   │   ├── ApplyEyeMakeup [48 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [32 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [56 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [72 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [32 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [72 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [80 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [88 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [48 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [72 entries exceeds filelimit, not opening dir]
│   ├── train
│   │   ├── ApplyEyeMakeup [240 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [240 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [240 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [240 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [240 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [240 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [240 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [240 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [240 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [240 entries exceeds filelimit, not opening dir]
│   └── val
│       ├── ApplyEyeMakeup [24 entries exceeds filelimit, not opening dir]
│       ├── ApplyLipstick [24 entries exceeds filelimit, not opening dir]
│       ├── Archery [24 entries exceeds filelimit, not opening dir]
│       ├── BabyCrawling [24 entries exceeds filelimit, not opening dir]
│       ├── BalanceBeam [24 entries exceeds filelimit, not opening dir]
│       ├── BandMarching [24 entries exceeds filelimit, not opening dir]
│       ├── BaseballPitch [24 entries exceeds filelimit, not opening dir]
│       ├── Basketball [24 entries exceeds filelimit, not opening dir]
│       ├── BasketballDunk [24 entries exceeds filelimit, not opening dir]
│       └── BenchPress [24 entries exceeds filelimit, not opening dir]
├── ucf101_test.jsonl
├── ucf101_train.jsonl
└── ucf101_val.jsonl

34 directories, 3 files
```

`jsonl`アノテーションでは、各行が以下のような辞書である必要があります:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

`conversations`はリストであるため、マルチターンの会話がサポートされます（そのようなデータが利用可能な場合）。

## Azure GPU クォータのリクエスト方法

### 前提条件

Contributorロール（またはContributorアクセスを含む他のロール）が付与されたAzureアカウント。

Azureアカウントをお持ちでない場合は、[無料アカウントを作成してください](https://azure.microsoft.com)。

### クォータ増加のリクエスト方法

My quotasから直接クォータ増加をリクエストできます。以下の手順に従ってクォータ増加をリクエストしてください。この例では、サブスクリプション内の調整可能なクォータを選択できます。

Azureポータルにサインインします。[Azure portal](https://portal.azure.com)。

検索ボックスに「quotas」と入力し、Quotasを選択します。
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

概要ページで、ComputeやAMLなどのプロバイダーを選択します。

**注意** Compute以外のすべてのプロバイダーでは、以下で説明されているAdjustable列の代わりにRequest increase列が表示されます。そこで特定のクォータの増加をリクエストするか、増加のサポートリクエストを作成できます。

My quotasページで、Quota nameの下から増加したいクォータを選択します。このクォータがAdjustable列でYesと表示されていることを確認してください。

ページ上部でNew Quota Requestを選択し、Enter a new limitを選択します。

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Requestペインで、新しいクォータ制限の数値を入力し、Submitを選択します。

リクエストがレビューされ、リクエストが満たされるかどうか通知されます。通常、数分以内に通知されます。

リクエストが満たされない場合は、サポートリクエストを作成するリンクが表示されます。このリンクを使用すると、サポートエンジニアが増加リクエストの支援を行います。

## Azure Compute GPU マシン SKUの提案

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

以下はいくつかの例です:

### A100またはH100 GPUを持っている場合

完全ファインチューニングは通常、最高のパフォーマンスを提供します。以下のコマンドを使用して、Phi-3-Vをヘイトフルミーム分類でファインチューニングできます。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Standard_ND40rs_v2 8x V100-32GB GPUを持っている場合

Phi-3-Vをヘイトフルミーム分類で完全ファインチューニングすることは可能ですが、フラッシュアテンションのサポートがないため、A100またはH100 GPUと比較してスループットが大幅に低下することが予想されます。また、bf16サポートがないため、精度にも影響が出る可能性があります（fp16混合精度トレーニングが代わりに使用されます）。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### データセンターGPUにアクセスできない場合
Loraが唯一の選択肢となる可能性があります。以下のコマンドを使用して、Phi-3-Vをヘイトフルミーム分類でファインチューニングできます。

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPUの場合、QLoRAがサポートされています。

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## 推奨ハイパーパラメータと期待される精度
### NLVR2

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_nlvr2.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

トレーニング方法 | 視覚モデル固定 | データ型 | LoRAランク | LoRAアルファ | バッチサイズ | 学習率 | エポック数 | 精度
--- | --- | --- | --- | --- | --- | --- | --- | --- |
完全ファインチューニング |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
完全ファインチューニング | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA結果は近日公開 |  |  |  |  |  |  |  |  |

### 注意
以下のDocVQAとヘイトフルミーム結果は以前のバージョン（Phi-3-vision）に基づいています。Phi-3.5-visionによる新しい結果は近日更新されます。

### DocVQA (注意: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_docvqa.py \
  --full_train \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

トレーニング方法 | データ型 | LoRAランク | LoRAアルファ | バッチサイズ | 学習率 | エポック数 | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
完全ファインチューニング | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
完全ファインチューニング | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
視覚モデル固定 | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
視覚モデル固定 | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### ヘイトフルミーム (注意: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

トレーニング方法 | データ型 | LoRAランク | LoRAアルファ | バッチサイズ | 学習率 | エポック数 | 精度
--- | --- | --- | --- | --- | --- | --- | --- |
完全ファインチューニング | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
完全ファインチューニング | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
視覚モデル固定 | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
視覚モデル固定 | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## スピードベンチマーク (注意: Phi-3-vision)

Phi-3.5-visionによる新しいベンチマーク結果は近日更新されます。

スピードベンチマークはDocVQAデータセットで実施されます。このデータセットの平均シーケンス長は2443.23トークンです（画像モデルで`num_crops=16`を使用）。

### 8x A100-80GB (Ampere)

トレーニング方法 | ノード数 | GPU数 | フラッシュアテンション | 実効バッチサイズ | スループット (img/s) | スピードアップ | GPUメモリのピーク (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
完全ファインチューニング | 1 | 8 |  | 64 | 5.041 |  1x | ~42
完全ファインチューニング | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
完全ファインチューニング | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
完全ファインチューニング | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
視覚モデル固定 | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
視覚モデル固定 | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

トレーニング方法 | ノード数 | GPU数 | フラッシュアテンション | 実効バッチサイズ | スループット (img/s) | スピードアップ | GPUメモリのピーク (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
完全ファインチューニング | 1 | 8 | | 64 | 2.462 |  1x | ~32
完全ファインチューニング | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
完全ファインチューニング | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
視覚モデル固定 | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## 既知の問題

- fp16ではフラッシュアテンションを実行できません（bf16が利用可能な場合は常に推奨され、フラッシュアテンションをサポートするすべてのGPUはbf16もサポートしています）。
- 中間チェックポイントの保存とトレーニングの再開はまだサポートされていません。

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な点が含まれる可能性があります。原文の母国語で書かれた文書を正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用により生じた誤解や誤認について、当方は一切の責任を負いません。