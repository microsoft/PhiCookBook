<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-09T21:59:33+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "pa"
}
-->
# Phi-3.5-vision ਫਾਈਨਟਿਊਨਿੰਗ ਰੇਸਿਪੀ

ਇਹ huggingface ਲਾਇਬ੍ਰੇਰੀਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5-vision ਫਾਈਨਟਿਊਨਿੰਗ ਦੀ ਅਧਿਕਾਰਿਕ ਸਹਾਇਤਾ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ `cd` ਨੂੰ ਕੋਡ ਡਾਇਰੈਕਟਰੀ [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) ਵਿੱਚ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਜਾਓ।

## ਇੰਸਟਾਲੇਸ਼ਨ

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

## ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ

ਅਸੀਂ ਦੋ ਉਦਾਹਰਣ ਫਾਈਨਟਿਊਨਿੰਗ ਸਕ੍ਰਿਪਟ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਾਂ, ਇੱਕ DocVQA ਲਈ ਅਤੇ ਦੂਜਾ hateful meme ਕਲਾਸੀਫਿਕੇਸ਼ਨ ਲਈ।

ਘੱਟੋ-ਘੱਟ ਹਾਰਡਵੇਅਰ 4x RTX8000 (ਹਰ GPU ਲਈ 48GB RAM) 'ਤੇ ਟੈਸਟ ਕੀਤਾ ਗਿਆ

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision ਹੁਣ ਬਹੁ-ਤਸਵੀਰ ਇਨਪੁੱਟਸ ਲਈ ਅਧਿਕਾਰਿਕ ਸਹਾਇਤਾ ਦਿੰਦਾ ਹੈ। ਇਹਾਂ NLVR2 ਲਈ ਫਾਈਨਟਿਊਨਿੰਗ ਦਾ ਇੱਕ ਉਦਾਹਰਣ ਹੈ

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## ਵਰਤੋਂ ਗਾਈਡ

ਹਾਰਡਵੇਅਰ ਦੇ ਅਨੁਸਾਰ, ਉਪਭੋਗਤਾ ਵੱਖ-ਵੱਖ ਫਾਈਨਟਿਊਨਿੰਗ ਤਕਨੀਕਾਂ ਚੁਣ ਸਕਦੇ ਹਨ। ਅਸੀਂ
full-finetuning (Deepspeed Zero-2 ਨਾਲ) ਸਹਾਇਤਾ ਕਰਦੇ ਹਾਂ ਜਿਸ ਵਿੱਚ vision ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਫ੍ਰੋਜ਼ ਕਰਨਾ ਵੀ ਚੁਣਿਆ ਜਾ ਸਕਦਾ ਹੈ, ਅਤੇ LoRA (ਜਿਸ ਵਿੱਚ 4bit QLoRA ਵੀ ਸ਼ਾਮਿਲ ਹੈ)।
ਆਮ ਤੌਰ 'ਤੇ, ਅਸੀਂ ਸੰਭਵ ਹੋਵੇ ਤਾਂ flash attention ਅਤੇ bf16 ਨਾਲ full finetuning ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ।

### ਆਪਣੇ ਕਸਟਮ ਡੇਟਾਸੈੱਟ ਨੂੰ ਲੋੜੀਂਦੇ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਲਈ ਗਾਈਡ

ਅਸੀਂ ਇੱਕ ਘੱਟੋ-ਘੱਟ ਵੀਡੀਓ ਕਲਾਸੀਫਿਕੇਸ਼ਨ ਡੇਟਾਸੈੱਟ (UCF-101 ਦਾ ਇੱਕ ਹਿੱਸਾ) ਨੂੰ ਇੱਕ ਅੰਤ-ਤੱਕ ਉਦਾਹਰਣ ਵਜੋਂ ਵਰਤਦੇ ਹਾਂ ਤਾਂ ਜੋ ਦਿਖਾ ਸਕੀਏ ਕਿ ਕਿਵੇਂ ਆਪਣੇ ਕਸਟਮ ਡੇਟਾਸੈੱਟ ਨੂੰ ਲੋੜੀਂਦੇ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਿਆ ਜਾਵੇ ਅਤੇ Phi-3.5-vision ਨੂੰ ਉਸ 'ਤੇ ਫਾਈਨਟਿਊਨ ਕੀਤਾ ਜਾਵੇ।

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

ਬਦਲਿਆ ਹੋਇਆ ਡੇਟਾ ਇਸ ਤਰ੍ਹਾਂ ਲੱਗੇਗਾ:

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

`jsonl` ਐਨੋਟੇਸ਼ਨ ਲਈ, ਹਰ ਲਾਈਨ ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ ਜਿਸਦਾ ਫਾਰਮੈਟ ਇਹ ਹੈ:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

ਧਿਆਨ ਦਿਓ ਕਿ `conversations` ਇੱਕ ਲਿਸਟ ਹੈ, ਇਸ ਲਈ ਜੇ ਅਜਿਹਾ ਡੇਟਾ ਮੌਜੂਦ ਹੋਵੇ ਤਾਂ ਬਹੁ-ਟਰਨ ਗੱਲਬਾਤ ਦਾ ਸਹਾਰਾ ਦਿੱਤਾ ਜਾ ਸਕਦਾ ਹੈ।

## Azure GPU ਕੋਟਾ ਮੰਗਣਾ

### ਜਰੂਰੀ ਸ਼ਰਤਾਂ

ਇੱਕ Azure ਖਾਤਾ ਜਿਸਦੇ ਕੋਲ Contributor ਭੂਮਿਕਾ ਹੋਵੇ (ਜਾਂ ਕੋਈ ਹੋਰ ਭੂਮਿਕਾ ਜਿਸ ਵਿੱਚ Contributor ਅਧਿਕਾਰ ਸ਼ਾਮਿਲ ਹੋਵੇ)।

ਜੇ ਤੁਹਾਡੇ ਕੋਲ Azure ਖਾਤਾ ਨਹੀਂ ਹੈ, ਤਾਂ [ਇਸ ਤੋਂ ਪਹਿਲਾਂ ਮੁਫ਼ਤ ਖਾਤਾ ਬਣਾਓ](https://azure.microsoft.com)।

### ਕੋਟਾ ਵਧਾਉਣ ਲਈ ਬੇਨਤੀ ਕਰੋ

ਤੁਸੀਂ My quotas ਤੋਂ ਸਿੱਧਾ ਕੋਟਾ ਵਧਾਉਣ ਦੀ ਬੇਨਤੀ ਕਰ ਸਕਦੇ ਹੋ। ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ ਕਿਸੇ ਵੀ ਸੁਧਾਰਯੋਗ ਕੋਟਾ ਲਈ ਬੇਨਤੀ ਕਰੋ। ਇਸ ਉਦਾਹਰਣ ਲਈ, ਤੁਸੀਂ ਆਪਣੀ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਵਿੱਚ ਕੋਈ ਵੀ ਸੁਧਾਰਯੋਗ ਕੋਟਾ ਚੁਣ ਸਕਦੇ ਹੋ।

[Azure portal](https://portal.azure.com) ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ।

ਖੋਜ ਬਾਕਸ ਵਿੱਚ "quotas" ਦਰਜ ਕਰੋ, ਫਿਰ Quotas ਚੁਣੋ।  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Overview ਪੰਨੇ 'ਤੇ, ਕਿਸੇ ਪ੍ਰੋਵਾਈਡਰ ਜਿਵੇਂ Compute ਜਾਂ AML ਨੂੰ ਚੁਣੋ।

**Note** Compute ਤੋਂ ਇਲਾਵਾ ਸਾਰੇ ਪ੍ਰੋਵਾਈਡਰਾਂ ਲਈ, ਤੁਸੀਂ Request increase ਕਾਲਮ ਦੇਖੋਗੇ ਨਾ ਕਿ Adjustable ਕਾਲਮ। ਇੱਥੇ ਤੁਸੀਂ ਕਿਸੇ ਖਾਸ ਕੋਟਾ ਲਈ ਵਾਧਾ ਮੰਗ ਸਕਦੇ ਹੋ ਜਾਂ ਵਾਧੇ ਲਈ ਸਪੋਰਟ ਬੇਨਤੀ ਬਣਾ ਸਕਦੇ ਹੋ।

My quotas ਪੰਨੇ 'ਤੇ, Quota name ਹੇਠਾਂ, ਉਹ ਕੋਟਾ ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਵਧਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਇਸ ਕੋਟਾ ਲਈ Adjustable ਕਾਲਮ ਵਿੱਚ Yes ਦਰਸਾਇਆ ਗਿਆ ਹੈ।

ਪੰਨੇ ਦੇ ਉੱਪਰ ਨੇੜੇ, New Quota Request ਚੁਣੋ, ਫਿਰ Enter a new limit ਚੁਣੋ।  
![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request ਪੈਨ ਵਿੱਚ, ਆਪਣੇ ਨਵੇਂ ਕੋਟਾ ਸੀਮਾ ਲਈ ਇੱਕ ਗਿਣਤੀ ਦਰਜ ਕਰੋ, ਫਿਰ Submit ਕਰੋ।

ਤੁਹਾਡੀ ਬੇਨਤੀ ਦੀ ਸਮੀਖਿਆ ਕੀਤੀ ਜਾਵੇਗੀ, ਅਤੇ ਜੇ ਬੇਨਤੀ ਪੂਰੀ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ ਤਾਂ ਤੁਹਾਨੂੰ ਸੂਚਿਤ ਕੀਤਾ ਜਾਵੇਗਾ। ਇਹ ਆਮ ਤੌਰ 'ਤੇ ਕੁਝ ਮਿੰਟਾਂ ਵਿੱਚ ਹੁੰਦਾ ਹੈ।

ਜੇ ਤੁਹਾਡੀ ਬੇਨਤੀ ਪੂਰੀ ਨਹੀਂ ਹੁੰਦੀ, ਤਾਂ ਤੁਹਾਨੂੰ ਸਪੋਰਟ ਬੇਨਤੀ ਬਣਾਉਣ ਲਈ ਲਿੰਕ ਦਿੱਤਾ ਜਾਵੇਗਾ। ਇਸ ਲਿੰਕ ਦੀ ਵਰਤੋਂ ਕਰਨ 'ਤੇ, ਇੱਕ ਸਪੋਰਟ ਇੰਜੀਨੀਅਰ ਤੁਹਾਡੇ ਵਾਧੇ ਦੀ ਮਦਦ ਕਰੇਗਾ।

## Azure Compute GPU ਮਸ਼ੀਨ SKU ਸੁਝਾਅ

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

ਇਹ ਕੁਝ ਉਦਾਹਰਣ ਹਨ:

### ਜੇ ਤੁਹਾਡੇ ਕੋਲ A100 ਜਾਂ H100 GPUs ਹਨ

ਪੂਰੀ ਫਾਈਨਟਿਊਨਿੰਗ ਆਮ ਤੌਰ 'ਤੇ ਸਭ ਤੋਂ ਵਧੀਆ ਪ੍ਰਦਰਸ਼ਨ ਦਿੰਦੀ ਹੈ। ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਵਰਤ ਕੇ Phi-3-V ਨੂੰ hateful memes ਕਲਾਸੀਫਿਕੇਸ਼ਨ 'ਤੇ ਫਾਈਨਟਿਊਨ ਕਰ ਸਕਦੇ ਹੋ।

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### ਜੇ ਤੁਹਾਡੇ ਕੋਲ Standard_ND40rs_v2 8x V100-32GB GPUs ਹਨ

Phi-3-V ਨੂੰ hateful memes ਕਲਾਸੀਫਿਕੇਸ਼ਨ 'ਤੇ ਪੂਰੀ ਤਰ੍ਹਾਂ ਫਾਈਨਟਿਊਨ ਕਰਨਾ ਅਜੇ ਵੀ ਸੰਭਵ ਹੈ। ਹਾਲਾਂਕਿ, A100 ਜਾਂ H100 GPUs ਨਾਲੋਂ ਕਾਫੀ ਘੱਟ throughput ਦੀ ਉਮੀਦ ਕਰੋ ਕਿਉਂਕਿ flash attention ਸਹਾਇਤਾ ਨਹੀਂ ਹੈ। accuracy ਵੀ ਪ੍ਰਭਾਵਿਤ ਹੋ ਸਕਦੀ ਹੈ ਕਿਉਂਕਿ bf16 ਸਹਾਇਤਾ ਨਹੀਂ ਹੈ (fp16 ਮਿਕਸਡ-ਪ੍ਰਿਸੀਜ਼ਨ ਟ੍ਰੇਨਿੰਗ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾਂਦੀ ਹੈ)।

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### ਜੇ ਤੁਹਾਨੂੰ ਡੇਟਾ ਸੈਂਟਰ GPUs ਦੀ ਪਹੁੰਚ ਨਹੀਂ ਹੈ

LoRA ਤੁਹਾਡੀ ਇਕੱਲੀ ਚੋਣ ਹੋ ਸਕਦੀ ਹੈ। ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਵਰਤ ਕੇ Phi-3-V ਨੂੰ hateful memes ਕਲਾਸੀਫਿਕੇਸ਼ਨ 'ਤੇ ਫਾਈਨਟਿਊਨ ਕਰ ਸਕਦੇ ਹੋ।

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU ਲਈ, QLoRA ਸਹਾਇਤਿਤ ਹੈ

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## ਸੁਝਾਏ ਗਏ ਹਾਈਪਰਪੈਰਾਮੀਟਰ ਅਤੇ ਉਮੀਦਵਾਰ ਸਹੀਤਾ
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

Training method | Frozen vision model | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | Accuracy
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA results comming soon |  |  |  |  |  |  |  |  |

### NOTE
ਹੇਠਾਂ ਦਿੱਤੇ DocVQA ਅਤੇ Hateful memes ਦੇ ਨਤੀਜੇ ਪਿਛਲੇ ਵਰਜਨ (Phi-3-vision) 'ਤੇ ਆਧਾਰਿਤ ਹਨ।  
ਨਵੇਂ ਨਤੀਜੇ Phi-3.5-vision ਨਾਲ ਜਲਦੀ ਅਪਡੇਟ ਕੀਤੇ ਜਾਣਗੇ।

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

Training method | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
frozen image model| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
frozen image model| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
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

Training method | data type | LoRA rank | LoRA alpha | batch size | learning rate | epochs | Accuracy
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
frozen image model| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
frozen image model| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## ਗਤੀ ਬੈਂਚਮਾਰਕਿੰਗ (NOTE: Phi-3-vision)

ਨਵੇਂ ਬੈਂਚਮਾਰਕਿੰਗ ਨਤੀਜੇ Phi-3.5-vision ਨਾਲ ਜਲਦੀ ਅਪਡੇਟ ਕੀਤੇ ਜਾਣਗੇ।

ਗਤੀ ਬੈਂਚਮਾਰਕਿੰਗ DocVQA ਡੇਟਾਸੈੱਟ 'ਤੇ ਕੀਤੀ ਗਈ ਹੈ। ਇਸ ਡੇਟਾਸੈੱਟ ਦੀ ਔਸਤ ਸੀਕਵੈਂਸ ਲੰਬਾਈ 2443.23 ਟੋਕਨ ਹੈ (`num_crops=16` ਇਮੇਜ ਮਾਡਲ ਲਈ)।

### 8x A100-80GB (Ampere)

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
frozen image model | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
frozen image model | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Training method | \# nodes | GPUs | flash attention | Effective batch size | Throughput (img/s) | Speedup | Peak GPU mem (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
frozen image model | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## ਮਾਲੂਮ ਸਮੱਸਿਆਵਾਂ

- fp16 ਨਾਲ flash attention ਚਲਾਇਆ ਨਹੀਂ ਜਾ ਸਕਦਾ (ਜਦੋਂ ਵੀ ਸੰਭਵ ਹੋ, bf16 ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਅਤੇ ਸਾਰੇ GPUs ਜੋ flash attention ਨੂੰ ਸਪੋਰਟ ਕਰਦੇ ਹਨ ਉਹ bf16 ਨੂੰ ਵੀ ਸਹਾਇਤਿਤ ਕਰਦੇ ਹਨ)।  
- ਅਜੇ ਤੱਕ ਮੱਧਵਰਤੀ ਚੈਕਪੌਇੰਟ ਸੇਵ ਕਰਨ ਅਤੇ ਟ੍ਰੇਨਿੰਗ ਦੁਬਾਰਾ ਸ਼ੁਰੂ ਕਰਨ ਦੀ ਸਹਾਇਤਾ ਨਹੀਂ ਹੈ।

**ਇਨਕਾਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਪਸ਼ਟਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਅਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।