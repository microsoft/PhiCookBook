<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-07-17T08:41:42+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "pa"
}
-->
# Phi-3.5-vision ਫਾਈਨਟਿਊਨਿੰਗ ਰੈਸੀਪੀ

ਇਹ huggingface ਲਾਇਬ੍ਰੇਰੀਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5-vision ਫਾਈਨਟਿਊਨਿੰਗ ਦੀ ਅਧਿਕਾਰਿਕ ਸਹਾਇਤਾ ਹੈ।  
ਕਿਰਪਾ ਕਰਕੇ ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡਾਂ ਨੂੰ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਕੋਡ ਡਾਇਰੈਕਟਰੀ [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) ਵਿੱਚ `cd` ਕਰੋ।

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

## ਤੇਜ਼ ਸ਼ੁਰੂਆਤ

ਅਸੀਂ ਦੋ ਉਦਾਹਰਨ ਫਾਈਨਟਿਊਨਿੰਗ ਸਕ੍ਰਿਪਟ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਾਂ, ਇੱਕ DocVQA ਲਈ ਅਤੇ ਇੱਕ hateful meme ਵਰਗੀਕਰਨ ਲਈ।

ਘੱਟੋ-ਘੱਟ ਹਾਰਡਵੇਅਰ 4x RTX8000 (48GB RAM ਪ੍ਰਤੀ GPU) 'ਤੇ ਟੈਸਟ ਕੀਤਾ ਗਿਆ

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision ਹੁਣ ਅਧਿਕਾਰਿਕ ਤੌਰ 'ਤੇ ਮਲਟੀ-ਇਮੇਜ ਇਨਪੁੱਟਸ ਨੂੰ ਸਹਿਯੋਗ ਦਿੰਦਾ ਹੈ। ਇੱਥੇ NLVR2 ਲਈ ਫਾਈਨਟਿਊਨਿੰਗ ਦਾ ਇੱਕ ਉਦਾਹਰਨ ਦਿੱਤਾ ਗਿਆ ਹੈ

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## ਵਰਤੋਂ ਗਾਈਡ

ਹਾਰਡਵੇਅਰ ਦੇ ਅਨੁਸਾਰ, ਯੂਜ਼ਰ ਵੱਖ-ਵੱਖ ਫਾਈਨਟਿਊਨਿੰਗ ਰਣਨੀਤੀਆਂ ਚੁਣ ਸਕਦੇ ਹਨ। ਅਸੀਂ  
ਪੂਰੀ ਫਾਈਨਟਿਊਨਿੰਗ (Deepspeed Zero-2 ਨਾਲ) ਨੂੰ ਸਹਿਯੋਗ ਦਿੰਦੇ ਹਾਂ ਜਿਸ ਵਿੱਚ ਵਿਜ਼ਨ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਜਮ੍ਹਾ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਅਤੇ LoRA (ਜਿਸ ਵਿੱਚ 4bit QLoRA ਵੀ ਸ਼ਾਮਲ ਹੈ)।  
ਆਮ ਤੌਰ 'ਤੇ, ਅਸੀਂ ਸੰਭਵ ਹੋਣ 'ਤੇ ਫਲੈਸ਼ ਅਟੈਂਸ਼ਨ ਅਤੇ bf16 ਨਾਲ ਪੂਰੀ ਫਾਈਨਟਿਊਨਿੰਗ ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ।

### ਆਪਣਾ ਕਸਟਮ ਡੇਟਾਸੈੱਟ ਲੋੜੀਂਦੇ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਲਈ ਗਾਈਡ

ਅਸੀਂ ਇੱਕ ਘੱਟੋ-ਘੱਟ ਵੀਡੀਓ ਵਰਗੀਕਰਨ ਡੇਟਾਸੈੱਟ (UCF-101 ਦਾ ਇੱਕ ਸਬਸੈੱਟ) ਨੂੰ ਇੱਕ ਅੰਤ-ਤੱਕ ਉਦਾਹਰਨ ਵਜੋਂ ਵਰਤਦੇ ਹਾਂ ਤਾਂ ਜੋ ਦਿਖਾ ਸਕੀਏ ਕਿ ਕਿਵੇਂ ਆਪਣਾ ਕਸਟਮ ਡੇਟਾਸੈੱਟ ਲੋੜੀਂਦੇ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਿਆ ਜਾ ਸਕਦਾ ਹੈ ਅਤੇ Phi-3.5-vision 'ਤੇ ਫਾਈਨਟਿਊਨ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

ਬਦਲਿਆ ਹੋਇਆ ਡੇਟਾ ਇਸ ਤਰ੍ਹਾਂ ਦਿਖਾਈ ਦੇਵੇਗਾ:

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

`jsonl` ਐਨੋਟੇਸ਼ਨ ਲਈ, ਹਰ ਲਾਈਨ ਇੱਕ ਡਿਕਸ਼ਨਰੀ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ ਜਿਵੇਂ:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

ਧਿਆਨ ਦਿਓ ਕਿ `conversations` ਇੱਕ ਲਿਸਟ ਹੈ, ਇਸ ਲਈ ਜੇ ਐਸਾ ਡੇਟਾ ਉਪਲਬਧ ਹੋਵੇ ਤਾਂ ਮਲਟੀ-ਟਰਨ ਗੱਲਬਾਤ ਦਾ ਸਹਿਯੋਗ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

## Azure GPU ਕੋਟਾ ਦੀ ਮੰਗ

### ਜ਼ਰੂਰੀ ਸ਼ਰਤਾਂ

ਇੱਕ Azure ਖਾਤਾ ਜਿਸ ਵਿੱਚ Contributor ਰੋਲ (ਜਾਂ ਕੋਈ ਹੋਰ ਰੋਲ ਜਿਸ ਵਿੱਚ Contributor ਐਕਸੈਸ ਸ਼ਾਮਲ ਹੋਵੇ) ਹੋਵੇ।  
ਜੇ ਤੁਹਾਡੇ ਕੋਲ Azure ਖਾਤਾ ਨਹੀਂ ਹੈ, ਤਾਂ [ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਮੁਫ਼ਤ ਖਾਤਾ ਬਣਾਓ](https://azure.microsoft.com)।

### ਕੋਟਾ ਵਾਧੇ ਦੀ ਮੰਗ ਕਰੋ

ਤੁਸੀਂ My quotas ਤੋਂ ਸਿੱਧਾ ਕੋਟਾ ਵਾਧੇ ਦੀ ਮੰਗ ਕਰ ਸਕਦੇ ਹੋ। ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ ਤਾਂ ਜੋ ਕਿਸੇ ਕੋਟਾ ਲਈ ਵਾਧਾ ਮੰਗਿਆ ਜਾ ਸਕੇ। ਇਸ ਉਦਾਹਰਨ ਲਈ, ਤੁਸੀਂ ਆਪਣੀ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਵਿੱਚ ਕੋਈ ਵੀ ਸਮਰਥਿਤ ਕੋਟਾ ਚੁਣ ਸਕਦੇ ਹੋ।

[Azure portal](https://portal.azure.com) ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ।  
ਖੋਜ ਬਾਕਸ ਵਿੱਚ "quotas" ਦਰਜ ਕਰੋ, ਫਿਰ Quotas ਚੁਣੋ।  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Overview ਪੇਜ਼ 'ਤੇ, ਕਿਸੇ ਪ੍ਰੋਵਾਈਡਰ ਨੂੰ ਚੁਣੋ, ਜਿਵੇਂ Compute ਜਾਂ AML।  

**Note** Compute ਤੋਂ ਇਲਾਵਾ ਸਾਰੇ ਪ੍ਰੋਵਾਈਡਰਾਂ ਲਈ, ਤੁਸੀਂ Adjustable ਕਾਲਮ ਦੀ ਥਾਂ Request increase ਕਾਲਮ ਵੇਖੋਗੇ। ਉੱਥੇ, ਤੁਸੀਂ ਕਿਸੇ ਖਾਸ ਕੋਟਾ ਲਈ ਵਾਧਾ ਮੰਗ ਸਕਦੇ ਹੋ ਜਾਂ ਵਾਧੇ ਲਈ ਸਹਾਇਤਾ ਬੇਨਤੀ ਬਣਾ ਸਕਦੇ ਹੋ।

My quotas ਪੇਜ਼ 'ਤੇ, Quota name ਹੇਠਾਂ, ਉਹ ਕੋਟਾ ਚੁਣੋ ਜਿਸਦਾ ਵਾਧਾ ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਇਸ ਕੋਟਾ ਲਈ Adjustable ਕਾਲਮ ਵਿੱਚ Yes ਦਿਖਾਈ ਦੇ ਰਿਹਾ ਹੈ।

ਪੇਜ਼ ਦੇ ਉੱਪਰ ਨੇੜੇ, New Quota Request ਚੁਣੋ, ਫਿਰ Enter a new limit ਚੁਣੋ।  
![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request ਪੈਨ ਵਿੱਚ, ਆਪਣੇ ਨਵੇਂ ਕੋਟਾ ਸੀਮਾ ਲਈ ਇੱਕ ਗਿਣਤੀ ਦਰਜ ਕਰੋ, ਫਿਰ Submit ਚੁਣੋ।

ਤੁਹਾਡੀ ਮੰਗ ਦੀ ਸਮੀਖਿਆ ਕੀਤੀ ਜਾਵੇਗੀ, ਅਤੇ ਤੁਹਾਨੂੰ ਸੂਚਿਤ ਕੀਤਾ ਜਾਵੇਗਾ ਕਿ ਮੰਗ ਪੂਰੀ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ ਜਾਂ ਨਹੀਂ। ਇਹ ਆਮ ਤੌਰ 'ਤੇ ਕੁਝ ਮਿੰਟਾਂ ਵਿੱਚ ਹੁੰਦਾ ਹੈ।

ਜੇ ਤੁਹਾਡੀ ਮੰਗ ਪੂਰੀ ਨਹੀਂ ਹੁੰਦੀ, ਤਾਂ ਤੁਹਾਨੂੰ ਸਹਾਇਤਾ ਬੇਨਤੀ ਬਣਾਉਣ ਲਈ ਇੱਕ ਲਿੰਕ ਦਿੱਤਾ ਜਾਵੇਗਾ। ਇਸ ਲਿੰਕ ਦੀ ਵਰਤੋਂ ਕਰਨ 'ਤੇ, ਇੱਕ ਸਹਾਇਤਾ ਇੰਜੀਨੀਅਰ ਤੁਹਾਡੀ ਵਾਧੇ ਦੀ ਮੰਗ ਵਿੱਚ ਮਦਦ ਕਰੇਗਾ।

## Azure Compute GPU ਮਸ਼ੀਨ SKU ਸੁਝਾਅ

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)  
[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)  
[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

ਇੱਥੇ ਕੁਝ ਉਦਾਹਰਨਾਂ ਹਨ:

### ਜੇ ਤੁਹਾਡੇ ਕੋਲ A100 ਜਾਂ H100 GPUs ਹਨ

ਪੂਰੀ ਫਾਈਨਟਿਊਨਿੰਗ ਆਮ ਤੌਰ 'ਤੇ ਸਭ ਤੋਂ ਵਧੀਆ ਪ੍ਰਦਰਸ਼ਨ ਦਿੰਦੀ ਹੈ। ਤੁਸੀਂ hateful memes ਵਰਗੀਕਰਨ ਲਈ Phi-3-V ਨੂੰ ਫਾਈਨਟਿਊਨ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਵਰਤ ਸਕਦੇ ਹੋ।

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

Phi-3-V ਨੂੰ hateful memes ਵਰਗੀਕਰਨ ਲਈ ਪੂਰੀ ਤਰ੍ਹਾਂ ਫਾਈਨਟਿਊਨ ਕਰਨਾ ਅਜੇ ਵੀ ਸੰਭਵ ਹੈ। ਪਰ, A100 ਜਾਂ H100 GPUs ਨਾਲੋਂ ਕਾਫੀ ਘੱਟ throughput ਦੀ ਉਮੀਦ ਕਰੋ ਕਿਉਂਕਿ ਫਲੈਸ਼ ਅਟੈਂਸ਼ਨ ਸਹਿਯੋਗ ਨਹੀਂ ਹੈ।  
ਸਹੀਤਾ 'ਤੇ ਵੀ ਪ੍ਰਭਾਵ ਪੈ ਸਕਦਾ ਹੈ ਕਿਉਂਕਿ bf16 ਸਹਿਯੋਗ ਨਹੀਂ ਹੈ (ਇਸ ਦੀ ਥਾਂ fp16 ਮਿਕਸਡ-ਪ੍ਰਿਸੀਜ਼ਨ ਟ੍ਰੇਨਿੰਗ ਵਰਤੀ ਜਾਂਦੀ ਹੈ)।

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### ਜੇ ਤੁਹਾਨੂੰ ਡੇਟਾ ਸੈਂਟਰ GPUs ਦੀ ਪਹੁੰਚ ਨਹੀਂ ਹੈ

LoRA ਤੁਹਾਡਾ ਇਕੱਲਾ ਵਿਕਲਪ ਹੋ ਸਕਦਾ ਹੈ। ਤੁਸੀਂ hateful memes ਵਰਗੀਕਰਨ ਲਈ Phi-3-V ਨੂੰ ਫਾਈਨਟਿਊਨ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਵਰਤ ਸਕਦੇ ਹੋ।

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPU ਲਈ, QLoRA ਸਹਿਯੋਗਿਤ ਹੈ

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

## ਸਪੀਡ ਬੈਂਚਮਾਰਕਿੰਗ (NOTE: Phi-3-vision)

ਨਵੇਂ ਬੈਂਚਮਾਰਕਿੰਗ ਨਤੀਜੇ Phi-3.5-vision ਨਾਲ ਜਲਦੀ ਅਪਡੇਟ ਕੀਤੇ ਜਾਣਗੇ।

ਸਪੀਡ ਬੈਂਚਮਾਰਕਿੰਗ DocVQA ਡੇਟਾਸੈੱਟ 'ਤੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਇਸ ਡੇਟਾਸੈੱਟ ਦੀ ਔਸਤ ਸੀਕਵੈਂਸ ਲੰਬਾਈ 2443.23 ਟੋਕਨ ਹੈ (`num_crops=16` ਇਮੇਜ ਮਾਡਲ ਲਈ ਵਰਤਿਆ ਗਿਆ)।

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

## ਜਾਣੀਆਂ ਸਮੱਸਿਆਵਾਂ

- fp16 ਨਾਲ ਫਲੈਸ਼ ਅਟੈਂਸ਼ਨ ਨਹੀਂ ਚੱਲ ਸਕਦਾ (ਜਦੋਂ ਵੀ ਉਪਲਬਧ ਹੋਵੇ, bf16 ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ, ਅਤੇ ਸਾਰੇ GPUs ਜੋ ਫਲੈਸ਼ ਅਟੈਂਸ਼ਨ ਸਹਿਯੋਗ ਕਰਦੇ ਹਨ ਉਹ bf16 ਨੂੰ ਵੀ ਸਹਿਯੋਗ ਦਿੰਦੇ ਹਨ)।  
- ਅਜੇ ਤੱਕ ਮੱਧਵਰਤੀ ਚੈਕਪੌਇੰਟ ਸੇਵ ਕਰਨ ਅਤੇ ਟ੍ਰੇਨਿੰਗ ਮੁੜ ਸ਼ੁਰੂ ਕਰਨ ਦਾ ਸਹਿਯੋਗ ਨਹੀਂ ਹੈ।

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।