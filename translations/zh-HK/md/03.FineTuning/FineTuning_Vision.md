# Phi-3.5-vision 微調指南

這是使用 huggingface 函式庫對 Phi-3.5-vision 進行微調的官方支援。
請在執行以下指令前，先 `cd` 到程式碼目錄 [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning)。

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

我們提供兩個範例微調腳本，一個用於 DocVQA，另一個用於仇恨迷因分類。

最低硬體測試為 4x RTX8000（每張 GPU 48GB 記憶體）

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision 現已正式支援多圖輸入。以下是微調 NLVR2 的範例。

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## 使用指南

根據硬體條件，使用者可選擇不同的微調策略。我們支援
全微調（搭配 Deepspeed Zero-2），可選擇凍結視覺參數，以及 LoRA（包含 4bit QLoRA）。
一般建議盡可能使用搭配 flash attention 和 bf16 的全微調。

### 自訂資料集轉換成所需格式的指南

我們使用一個最小化的影片分類資料集（UCF-101 的子集）作為端到端範例，示範如何將自訂資料集轉換成所需格式，並在其上微調 Phi-3.5-vision。

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

對於 `jsonl` 標註，每一行應該是一個字典，如下：

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

請注意，`conversations` 是一個列表，因此如果有此類資料，能支援多輪對話。

## 申請 Azure GPU 配額

### 先決條件

擁有 Azure 帳號且具備 Contributor 角色（或包含 Contributor 權限的其他角色）。

如果還沒有 Azure 帳號，請先[免費註冊帳號](https://azure.microsoft.com)。

### 申請配額提升

您可以直接從「My quotas」提交配額提升申請。以下步驟示範如何申請配額提升。此範例中，您可以選擇訂閱中任何可調整的配額。

登入 [Azure 入口網站](https://portal.azure.com)。

在搜尋框輸入「quotas」，然後選擇 Quotas。
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

在概覽頁面，選擇一個供應商，例如 Compute 或 AML。

**注意** 除 Compute 以外的供應商，您會看到「Request increase」欄位，而非下方所述的「Adjustable」欄位。在那裡，您可以申請特定配額的提升，或建立支援請求。

在「My quotas」頁面，於「Quota name」下選擇您想提升的配額。確保該配額的「Adjustable」欄位顯示為 Yes。

在頁面頂部附近，選擇「New Quota Request」，然後選擇「Enter a new limit」。

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

在「New Quota Request」面板中，輸入新的配額數值，然後選擇「Submit」。

您的申請將會被審核，若申請可被批准，您會收到通知。通常幾分鐘內會有結果。

若申請未被批准，您會看到建立支援請求的連結。使用該連結後，支援工程師會協助您完成配額提升申請。

## Azure 計算 GPU 機器 SKU 建議

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

以下是一些範例：

### 如果您有 A100 或 H100 GPU

全微調通常能達到最佳效能。您可以使用以下指令微調 Phi-3-V 於仇恨迷因分類任務。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### 如果您有 Standard_ND40rs_v2 8x V100-32GB GPU

仍然可以對仇恨迷因分類進行全微調，但由於缺乏 flash attention 支援，吞吐量會比 A100 或 H100 GPU 低很多。
同時因為不支援 bf16（改用 fp16 混合精度訓練），準確度也可能受到影響。

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### 如果您無法使用資料中心 GPU

LoRA 可能是您的唯一選擇。您可以使用以下指令微調 Phi-3-V 於仇恨迷因分類。

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

對於 Turing+ GPU，支援 QLoRA。

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## 建議超參數與預期準確度

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

訓練方法 | 凍結視覺模型 | 資料類型 | LoRA rank | LoRA alpha | 批次大小 | 學習率 | 訓練輪數 | 準確度
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA 結果即將公布 |  |  |  |  |  |  |  |  |

### 注意
以下 DocVQA 與仇恨迷因結果基於舊版本（Phi-3-vision）。
Phi-3.5-vision 的新結果將會很快更新。

### DocVQA（注意：Phi-3-vision）

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

訓練方法 | 資料類型 | LoRA rank | LoRA alpha | 批次大小 | 學習率 | 訓練輪數 | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
凍結影像模型 | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
凍結影像模型 | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### 仇恨迷因（注意：Phi-3-vision）

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

訓練方法 | 資料類型 | LoRA rank | LoRA alpha | 批次大小 | 學習率 | 訓練輪數 | 準確度
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
凍結影像模型 | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
凍結影像模型 | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## 效能基準測試（注意：Phi-3-vision）

Phi-3.5-vision 的新基準測試結果將會很快更新。

效能基準測試在 DocVQA 資料集上進行。該資料集的平均序列長度為 2443.23 個 token（影像模型使用 `num_crops=16`）。

### 8x A100-80GB (Ampere)

訓練方法 | 節點數 | GPU 數量 | flash attention | 有效批次大小 | 吞吐量（張圖/秒） | 加速比 | GPU 記憶體峰值 (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 5.041 | 1x | 約42
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | 約36
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | 約29
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | 約26
凍結影像模型 | 1 | 8 |  | 64 | 17.578 | 3.49x | 約29
凍結影像模型 | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | 約27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | 約50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | 約16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | 約32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | 約10

### 8x V100-32GB (Volta)

訓練方法 | 節點數 | GPU 數量 | flash attention | 有效批次大小 | 吞吐量（張圖/秒） | 加速比 | GPU 記憶體峰值 (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 2.462 | 1x | 約32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | 約32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | 約32
凍結影像模型 | 1 | 8 |  | 64 | 8.942 | 3.63x | 約27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | 約30

## 已知問題

- 無法在 fp16 下使用 flash attention（建議有條件時皆使用 bf16，所有支援 flash attention 的 GPU 也都支援 bf16）。
- 目前不支援儲存中間檢查點並恢復訓練。

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。