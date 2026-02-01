# Phi-3.5-vision ファインチューニングレシピ

これは huggingface ライブラリを使った Phi-3.5-vision ファインチューニングの公式サポートです。  
以下のコマンドを実行する前に、コードディレクトリ [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) に `cd` してください。

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

DocVQA 用と hateful meme 分類用の2つのファインチューニングスクリプトの例を提供しています。

最小ハードウェアは 4x RTX8000（GPUあたり48GB RAM）でテスト済みです。

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision はマルチイメージ入力を公式にサポートしました。以下は NLVR2 のファインチューニング例です。

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## 使用ガイド

ハードウェアに応じて、ユーザーは異なるファインチューニング戦略を選択できます。  
フルファインチューニング（Deepspeed Zero-2対応）で視覚パラメータを凍結するオプションや、LoRA（4bit QLoRAを含む）をサポートしています。  
一般的には、可能な限り flash attention と bf16 を使ったフルファインチューニングを推奨します。

### カスタムデータセットを必要な形式に変換するためのガイド

UCF-101 のサブセットである最小限の動画分類データセットをエンドツーエンドの例として使い、カスタムデータセットを必要な形式に変換し、Phi-3.5-vision でファインチューニングする方法を示します。

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

変換後のデータは以下のようになります：

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

`jsonl` アノテーションは、各行が以下のような辞書形式である必要があります：

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

`conversations` はリストなので、複数ターンの会話データがあれば対応可能です。

## Azure GPU クォータ申請

### 前提条件

Contributor ロール（または Contributor アクセスを含む他のロール）を持つ Azure アカウントが必要です。

Azure アカウントをお持ちでない場合は、[無料アカウントを作成してください](https://azure.microsoft.com)。

### クォータ増加の申請方法

My quotas から直接クォータ増加の申請が可能です。以下の手順で申請してください。例として、サブスクリプション内の任意の調整可能なクォータを選択できます。

[Azure ポータル](https://portal.azure.com) にサインインします。

検索ボックスに「quotas」と入力し、Quotas を選択します。  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

概要ページで、Compute や AML などのプロバイダーを選択します。

**注意** Compute 以外のプロバイダーでは、以下で説明する Adjustable 列の代わりに Request increase 列が表示されます。そこで特定のクォータの増加を申請するか、サポートリクエストを作成できます。

My quotas ページで、Quota name の下から増加したいクォータを選択します。Adjustable 列が Yes になっていることを確認してください。

ページ上部近くの New Quota Request を選択し、Enter a new limit を選びます。

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request ペインで新しいクォータ制限の数値を入力し、Submit を選択します。

申請は審査され、承認されれば通知が届きます。通常数分以内に処理されます。

申請が承認されなかった場合は、サポートリクエスト作成用のリンクが表示されます。このリンクを使うと、サポートエンジニアが増加申請を支援します。

## Azure Compute GPU マシン SKU の推奨

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

以下は例です：

### A100 または H100 GPU をお持ちの場合

フルファインチューニングが通常最良の性能を発揮します。以下のコマンドで Phi-3-V を hateful memes 分類でファインチューニングできます。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Standard_ND40rs_v2 8x V100-32GB GPU をお持ちの場合

hateful memes 分類で Phi-3-V をフルファインチューニングすることは可能ですが、flash attention 非対応のため A100 や H100 と比べてスループットはかなり低くなります。  
また bf16 非対応のため精度にも影響が出る可能性があります（代わりに fp16 混合精度トレーニングを使用）。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### データセンター GPU にアクセスできない場合

LoRA が唯一の選択肢かもしれません。以下のコマンドで Phi-3-V を hateful memes 分類でファインチューニングできます。

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU では QLoRA がサポートされています。

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

| トレーニング方法 | 凍結視覚モデル | データ型 | LoRAランク | LoRAアルファ | バッチサイズ | 学習率 | エポック数 | 精度 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
| full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
| LoRA 結果は近日公開予定 |  |  |  |  |  |  |  |  |

### 注記  
以下の DocVQA と Hateful memes の結果は前バージョン（Phi-3-vision）に基づいています。  
Phi-3.5-vision の新しい結果は近日更新予定です。

### DocVQA (NOTE: Phi-3-vision)

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

| トレーニング方法 | データ型 | LoRAランク | LoRAアルファ | バッチサイズ | 学習率 | エポック数 | ANLS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
| full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
| 凍結画像モデル | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
| 凍結画像モデル | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
| LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
| LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
| QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
| QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (NOTE: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

| トレーニング方法 | データ型 | LoRAランク | LoRAアルファ | バッチサイズ | 学習率 | エポック数 | 精度 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
| full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
| 凍結画像モデル | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
| 凍結画像モデル | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
| LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
| LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
| QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
| QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## スピードベンチマーク (NOTE: Phi-3-vision)

Phi-3.5-vision の新しいベンチマーク結果は近日更新予定です。

ベンチマークは DocVQA データセットで実施しました。  
このデータセットの平均シーケンス長は 2443.23 トークンです（画像モデルに `num_crops=16` を使用）。

### 8x A100-80GB (Ampere)

| トレーニング方法 | ノード数 | GPU数 | flash attention | 実効バッチサイズ | スループット (img/s) | 加速率 | 最大GPUメモリ (GB) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| full-finetuning | 1 | 8 |  | 64 | 5.041 | 1x | 約42 |
| full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | 約36 |
| full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | 約29 |
| full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | 約26 |
| 凍結画像モデル | 1 | 8 |  | 64 | 17.578 | 3.49x | 約29 |
| 凍結画像モデル | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | 約27 |
| LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | 約50 |
| LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | 約16 |
| QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | 約32 |
| QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | 約10 |

### 8x V100-32GB (Volta)

| トレーニング方法 | ノード数 | GPU数 | flash attention | 実効バッチサイズ | スループット (img/s) | 加速率 | 最大GPUメモリ (GB) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| full-finetuning | 1 | 8 |  | 64 | 2.462 | 1x | 約32 |
| full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | 約32 |
| full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | 約32 |
| 凍結画像モデル | 1 | 8 |  | 64 | 8.942 | 3.63x | 約27 |
| LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | 約30 |

## 既知の問題

- fp16 では flash attention を実行できません（bf16 が利用可能な場合は常に推奨されます。flash attention 対応GPUはすべて bf16 もサポートしています）。  
- 中間チェックポイントの保存やトレーニングの再開はまだサポートしていません。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。
