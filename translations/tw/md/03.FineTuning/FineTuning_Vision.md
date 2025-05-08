<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-08T05:21:01+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "tw"
}
-->
# Phi-3.5-vision 微調教學

這是使用 huggingface 函式庫對 Phi-3.5-vision 進行微調的官方支援。
請先 `cd` 到程式碼目錄 [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning)，再執行以下指令。

## 安裝

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

## 快速開始

我們提供兩個範例微調腳本，一個用於 DocVQA，另一個用於 hateful meme 分類。

最低測試硬體為 4x RTX8000（每張 GPU 48GB 記憶體）

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision 現在正式支援多張圖片輸入。以下是針對 NLVR2 的微調範例。

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## 使用指南

根據硬體狀況，使用者可選擇不同的微調策略。我們支援
full-finetuning（搭配 Deepspeed Zero-2），可選擇凍結視覺參數，以及 LoRA（包含 4bit QLoRA）。
一般建議盡可能使用帶有 flash attention 和 bf16 的 full finetuning。

### 將自訂資料集轉換為所需格式的指南

我們使用一個最小的影片分類資料集（UCF-101 的子集）作為端到端範例，示範如何將自訂資料集轉換成所需格式並微調 Phi-3.5-vision。

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

轉換後的資料會長這樣：

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

對於 `jsonl` 標註，每行應該是如下的字典格式：

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

請注意 `conversations` 是一個列表，因此如果有多輪對話資料，也能支援。

## 申請 Azure GPU 配額

### 申請前準備

需要一個擁有 Contributor 角色（或含 Contributor 權限的其他角色）的 Azure 帳號。

如果還沒有 Azure 帳號，請先[免費註冊帳號](https://azure.microsoft.com)。

### 申請配額提升

你可以直接從「My quotas」頁面提交配額提升申請。以下步驟示範如何申請配額提升。此範例中，你可以選擇訂閱中的任一可調整配額。

登入 [Azure 入口網站](https://portal.azure.com)。

在搜尋框輸入「quotas」，然後選擇 Quotas。
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

在 Overview 頁面，選擇一個提供者，例如 Compute 或 AML。

**Note** 除了 Compute 之外，其他提供者會看到 Request increase 欄位，而非下方提到的 Adjustable 欄位。在那裡你可以申請特定配額的提升，或建立支援請求。

在 My quotas 頁面，於 Quota name 欄位選擇你想提升的配額。確認 Adjustable 欄位顯示 Yes。

在頁面上方，點選 New Quota Request，然後選擇 Enter a new limit。

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

在 New Quota Request 面板中，輸入新的數值限制，然後點 Submit。

你的申請將會被審核，並在幾分鐘內通知是否通過。

若申請未通過，會看到連結可建立支援請求。使用該連結後，支援工程師會協助你完成配額提升申請。

## Azure Compute GPU 機型建議

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

以下是一些範例：

### 如果你有 A100 或 H100 GPU

完整微調通常能達到最佳效能。你可以使用以下指令來微調 Phi-3-V 於 hateful memes 分類任務。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### 如果你有 Standard_ND40rs_v2 8x V100-32GB GPU

仍然可以完整微調 Phi-3-V 用於 hateful memes 分類。不過，由於不支援 flash attention，效能會比 A100 或 H100 低很多。
而且因為不支援 bf16（改用 fp16 混合精度訓練），準確率可能也會受到影響。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### 如果你無法使用資料中心 GPU

LoRA 可能是你的唯一選擇。你可以用以下指令微調 Phi-3-V 於 hateful memes 分類。

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU 支援 QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## 建議超參數與預期準確率

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

訓練方式 | 是否凍結視覺模型 | 資料類型 | LoRA rank | LoRA alpha | 批次大小 | 學習率 | 訓練週期 | 準確率
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA 結果即將公布 |  |  |  |  |  |  |  |  |

### NOTE
以下 DocVQA 與 Hateful memes 的結果基於舊版（Phi-3-vision）。
Phi-3.5-vision 的新結果將會陸續更新。

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

訓練方式 | 資料類型 | LoRA rank | LoRA alpha | 批次大小 | 學習率 | 訓練週期 | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
凍結影像模型 | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
凍結影像模型 | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

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

訓練方式 | 資料類型 | LoRA rank | LoRA alpha | 批次大小 | 學習率 | 訓練週期 | 準確率
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
凍結影像模型 | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
凍結影像模型 | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## 效能測試 (NOTE: Phi-3-vision)

Phi-3.5-vision 的新效能測試結果將會陸續更新。

效能測試在 DocVQA 資料集上進行。該資料集平均序列長度為 2443.23 個 token（影像模型使用 `num_crops=16`）。

### 8x A100-80GB (Ampere)

訓練方式 | 節點數 | GPU 數量 | flash attention | 實際批次大小 | 吞吐量 (張圖/秒) | 加速比 | GPU 記憶體峰值 (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | 約 42
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | 約 36
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | 約 29
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | 約 26
凍結影像模型 | 1 | 8 |  | 64 | 17.578 | 3.49x | 約 29
凍結影像模型 | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | 約 27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | 約 50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | 約 16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | 約 32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | 約 10

### 8x V100-32GB (Volta)

訓練方式 | 節點數 | GPU 數量 | flash attention | 實際批次大小 | 吞吐量 (張圖/秒) | 加速比 | GPU 記憶體峰值 (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 2.462 |  1x | 約 32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | 約 32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | 約 32
凍結影像模型 | 1 | 8 |  | 64 | 8.942 | 3.63x | 約 27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | 約 30

## 已知問題

- fp16 無法使用 flash attention（建議有條件都使用 bf16，且所有支援 flash attention 的 GPU 也支援 bf16）。
- 目前不支援儲存中間檢查點並恢復訓練。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於翻譯準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生之任何誤解或誤譯負責。