# Phi-3.5-vision ఫైన్‌ట్యూనింగ్ మార్గదర్శకము

ఇది huggingface లైబ్రరీలను ఉపయోగించి Phi-3.5-vision ఫైన్‌ట్యూనింగ్‌కు అధికారిక మద్దతు. క్రింది కమాండ్లను అమలు చేయటానికి ముందు దయచేసి కోడ్ డైరెక్టరీ [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning)కి `cd` చేయండి.

## సంస్థాపన

```bash
# కొత్త conda ఎన్విరాన్‌మెంట్ సృష్టించండి
conda create -n phi3v python=3.10
conda activate phi3v

# PyTorch ను ఇన్‌స్టాల్ చేయండి
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# ఉదాహరణ కోడ్ నడపడానికి అవసరమైన ఇతర లైబ్రరీలు
pip install -r requirements.txt

# (ఐచ్ఛికం) ఫ్లాష్ అటెన్షన్ -- Ampere+ GPUలు (ఉదా., A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (ఐచ్ఛికం) QLoRA -- Turing+ GPUలు (ఉదా., RTX 8000)
pip install bitsandbytes==0.43.1
```

## త్వరిత ప్రారంభం

మేము రెండు ఉదాహరణ ఫైన్‌ట్యూనింగ్ స్క్రిప్టులను అందిస్తున్నాము, ఒకటి DocVQA కోసం మరియు ఒకటి hateful meme వర్గీకరణ కోసం.

కనిష్ఠంగా పరీక్షించిన హార్డ్వేర్: 4x RTX8000 (ప్రతి GPUకి 48GB RAM)

```bash
# DocVQA యొక్క మినీ-ట్రైన్ స్ప్లిట్‌పై అత్యల్ప స్క్రిప్ట్
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision ఇప్పుడు అధికారీకంగా బహుళ-చిత్ర (multi-image) ఇన్పుట్లకు మద్దతు చేస్తుంది. ఇక్కడ NLVR2 ఫైన్‌ట్యూనింగ్ కోసం ఒక ఉదాహరణ ఉంది

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## ఉపయోగ మార్గదర్శకం

హార్డ్వేర్‌పై ఆధారపడి, వినియోగదారులు వేర్వేరు ఫైన్‌ట్యూనింగ్ వ్యూహాలను ఎంచుకోవచ్చు. మేము పూర్తి-ఫైన్‌ట్యూనింగ్ (Deepspeed Zero-2తో) ను ఐచ్ఛికంగా విజన్ పరామితులను ఫ్రోజన్ చేయడం తో, మరియు LoRA (4bit QLoRA సహా) మద్దతుతో అందిస్తున్నాము.
సాధారణంగా, సాధ్యమైతే flash attention మరియు bf16తో పూర్తి ఫైన్‌ట్యూనింగ్ చేయాలని మేము సిఫార్సు చేస్తాము.

### మీ అనుకూల dataset ను అవసరమైన ఫార్మాట్‌కు మార్చుకునేందుకు మార్గదర్శకం

మేము ఒక end-to-end ఉదాహరణగా కనీస వీడియో వర్గీకరణ dataset (UCF-101 యొక్క ఒక ఉపసెట్) ను ఉపయోగించి మీ అనుకూల dataset ను అవసరమైన ఫార్మాట్‌గా ఎలా మార్చాలో మరియు దానిపై Phi-3.5-vision ను ఎలా ఫైన్‌ట్యూన్ చేయాలో చూపిస్తున్నాము.

```bash
# డేటాను మార్చండి
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# శిక్షణ
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

మార్పిడి చేసిన డేటా ఈ విధంగా ఉంటుంది:

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

`jsonl` అనోటేషన్ కోసం, ప్రతి లైన్ ఒక డిక్షనరీలా ఉండాలి:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

గమనిక: `conversations` ఒక జాబితా (list), కాబట్టి multi-turn సంభాషణలు అందుబాటులో ఉంటే మద్దతు చేయబడతాయి.

## Azure GPU క్వోటా అభ్యర్థన

### ముందు అవసరాలు

Contributor పాత్ర (లేదా Contributor యాక్సెస్ కలిగే మరో పాత్ర) ఉన్న Azure ఖాతా అవసరం.

మీకు Azure ఖాతా లేకుంటే, మొదలు పెట్టేముందు [మొదలు పెట్టేముందు ఉచిత ఖాతా సృష్టించండి](https://azure.microsoft.com).

### క్వోటా పెంపు కోసం అభ్యర్థన చేయడం

మీరు My quotas నుండి నేరుగా క్వోటా పెంపు కోసం అభ్యర్థన పంపవచ్చు. క్వోటా పెంపు కోసం అభ్యర్థించడానికి క్రింది దశలను అనుసరించండి. ఈ ఉదాహరణకి, మీ సబ్స్క్రిప్షన్లో ఏదైనా సమాయోజ్యమైన (adjustable) క్వోటాను ఎంచుకోవచ్చు.

[Azure portal](https://portal.azure.com)లో సైన్-ఇన్ చేయండి.

సర్చ్ బాక్స్‌లో "quotas" ను ఎంటర్ చేసి, తర్వాత Quotas ను ఎంచుకోండి.
![క్వోటా](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Overview పేజీలో, Compute లేదా AML వంటి ఒక provider ని ఎంచుకోండి.

**గమనిక** Compute తప్పిన ఇతర అన్ని providers కోసం, మీరు క్రింద వివరించిన Adjustable column స్థానంలో Request increase column ను చూడవచ్చు. అక్క‌డ, మీరు నిర్దిష్ట క్వోటా కోసం పెంపును అభ్యర్థించవచ్చు, లేదా పెంపు కోసం ఒక support request సృష్టించవచ్చు.

My quotas పేజీలో, Quota name క్రింద, మీరు పెంచదలచుకున్న క్వాటాను ఎంచుకోండి. ఈ క్వోటాకు Adjustable column లో Yes కనిపిస్తోందో లేదో నిర్ధారించండి.

పేజీ టాప్ దగ్గర New Quota Request ఎంచుకుని, తదుపరిగా Enter a new limit ఎంచుకోండి.

![క్వోటా పెంపు](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

New Quota Request ప్యాన్‌లో, మీ కొత్త క్వోటా పరిమితి కోసం ఒక సంఖ్యాత్మక విలువ నమోదు చేసి, Submit ఎంచుకోండి.

మీ అభ్యర్థన సమీక్షించబడుతుంది, మరియు అభ్యర్థన నెరవేరగలదో లేదో మీకు తెలియజేస్తారు. ఇది సాధారణంగా కొన్ని నిమిషాల్లో జరుగుతుంది.

మీ అభ్యర్థన నెరవేరకపోతే, మీరు support request సృష్టించడానికి ఒక లింక్ చూడవచ్చు. మీరు ఆ లింక్ ఉపయోగించినప్పుడు, ఒక support ఇంజనీర్ మీ పెంపు అభ్యర్థనలో మీకు సహాయం చేస్తారు.

## Azure Compute GPU మెషిన్ SKU సూచనలు

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

క్రింద కొన్ని ఉదాహరణలు ఉన్నాయి:

### మీకు A100 లేదా H100 GPUs ఉంటే

పూర్తి ఫైన్‌ట్యూనింగ్ సాధారణంగా ఉత్తమ పనితీరును ఇస్తుంది. hateful memes వర్గీకరణపై Phi-3-V ను ఫైన్‌ట్యూన్ చేయటానికి మీరు క్రింది కమాండ్ ను ఉపయోగించవచ్చు.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### మీ వద్ద Standard_ND40rs_v2 8x V100-32GB GPUs ఉంటే

hateful memes వర్గీకరణపై Phi-3-V ను పూర్తి ఫైన్‌ట్యూన్ చేయటం ఇంకా సాధ్యమే. అయితే flash attention మద్దతు లేకపోవడంతో A100 లేదా H100 GPUsతో పోలిస్తే థ్రూపుట్ చాలా తక్కువగా ఉంటుంది. bf16 మద్దతు లేకపోవడం వల్ల ఖచ్చితత్వం ప్రభావితం కావచ్చు (దానివల్ల fp16 మిక్స్-ప్రెసిషన్ శిక్షణను ఉపయోగిస్తారు).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### మీకు డేటా సెంటర్ GPUs కు ప్రాప్తి లేకపోతే
LoRA మీకు единే ఎంపిక కావచ్చు. hateful memes వర్గీకరణపై Phi-3-V ను ఫైన్‌ట్యూన్ చేయటానికి మీరు క్రింది కమాండ్‌ను ఉపయోగించవచ్చు.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Turing+ GPUలకు QLoRA మద్దతు ఉంది

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## సూచించిన హైపర్‌పారామితులు మరియు ఆశించిన ఖచ్చితత్వం
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

శిక్షణ పద్ధతి | ఫ్రోజన్ విజన్ మోడల్ | డేటా రకం | LoRA ర్యాంక్ | LoRA ఆల్ఫా | బ్యాచ్ పరిమాణం | లెర్నింగ్ రేట్ | ఎపోక్స్ | ఖచ్చితత్వం
--- | --- | --- | --- | --- | --- | --- | --- | --- |
పూర్తి-ఫైన్‌ట్యూనింగ్ |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
పూర్తి-ఫైన్‌ట్యూనింగ్ | &#x2714; |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
LoRA ఫలితాలు త్వరలో అందుబాటులో ఉంటాయి |  |  |  |  |  |  |  |  |

### గమనిక
క్రింద ఉన్న DocVQA మరియు Hateful memes ఫలితాలు గత వెర్షన్ (Phi-3-vision) ఆధారంగా ఉన్నాయి.
Phi-3.5-vision సహా కొత్త ఫలితాలు త్వరలో అప్డేట్ చేయబడతాయి.

### DocVQA (గమనిక: Phi-3-vision)

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

శిక్షణ పద్ధతి | డేటా రకం | LoRA ర్యాంక్ | LoRA ఆల్ఫా | బ్యాచ్ పరిమాణం | లెర్నింగ్ రేట్ | ఎపోక్స్ | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
పూర్తి-ఫైన్‌ట్యూనింగ్ | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
పూర్తి-ఫైన్‌ట్యూనింగ్ | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
ఫ్రోజన్ ఇమేజ్ మోడల్| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
ఫ్రోజన్ ఇమేజ్ మోడల్| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Hateful memes (గమనిక: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

శిక్షణ పద్ధతి | డేటా రకం | LoRA ర్యాంక్ | LoRA ఆల్ఫా | బ్యాచ్ పరిమాణం | లెర్నింగ్ రేట్ | ఎపోక్స్ | ఖచ్చితత్వం
--- | --- | --- | --- | --- | --- | --- | --- |
పూర్తి-ఫైన్‌ట్యూనింగ్ | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
పూర్తి-ఫైన్‌ట్యూనింగ్ | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
ఫ్రోజన్ ఇమేజ్ మోడల్| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
ఫ్రోజన ఇమేజ్ మోడల్| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## వేగం బెంచ్‌మార్క్ (గమనిక: Phi-3-vision)

Phi-3.5-visionతో కొత్త బెంచ్‌మార్క్ ఫలితాలు త్వరలో అప్డేట్ చేయబడతాయి.

వేగం బెంచ్‌మార్క్ DocVQA dataset పై నిర్వహించబడింది. ఈ dataset యొక్క సగటు సీక్వెన్స్ పొడవు 2443.23 tokens (image model కోసం `num_crops=16` ఉపయోగించి).

### 8x A100-80GB (Ampere)

శిక్షణ పద్ధతి | \# నోడ్లు | GPUs | flash attention | ప్రభావవంతమైన బ్యాచ్ పరిమాణం | Throughput (img/s) | Speedup | గరిష్ఠ GPU మెమ్ (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
పూర్తి-ఫైన్‌ట్యూనింగ్ | 1 | 8 |  | 64 | 5.041 |  1x | ~42
పూర్తి-ఫైన్‌ట్యూనింగ్ | 1 | 8 | &#x2714; | 64 | 8.657 | 1.72x | ~36
పూర్తి-ఫైన్‌ట్యూనింగ్ | 2 | 16 | &#x2714; | 64 | 16.903 | 3.35x | ~29
పూర్తి-ఫైన్‌ట్యూనింగ్ | 4 | 32 | &#x2714; | 64 | 33.433 | 6.63x | ~26
ఫ్రోజన్ ఇమేజ్ మోడల్ | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
ఫ్రోజన్ ఇమేజ్ మోడల్ | 1 | 8 | &#x2714; | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | &#x2714; | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | &#x2714; | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

శిక్షణ పద్ధతి | \# నోడ్లు | GPUs | flash attention | ప్రభావవంతమైన బ్యాచ్ పరిమాణం | Throughput (img/s) | Speedup | గరిష్ఠ GPU మెమ్ (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
పూర్తి-ఫైన్‌ట్యూనింగ్ | 1 | 8 | | 64 | 2.462 |  1x | ~32
పూర్తి-ఫైన్‌ట్యూనింగ్ | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
పూర్తి-ఫైన్‌ట్యూనింగ్ | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
ఫ్రోజన్ ఇమేజ్ మోడల్ | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## తెలిసిన సమస్యలు

- fp16 తో flash attention నడపలేరు (లభ్యమైతే bf16 ను ఎప్పుడైనా సూచించబడుతుంది, మరియు flash attention ను మద్దతు చేసే అన్ని GPUs కూడా bf16 ను మద్దతు చేస్తాయి).
- మధ్యంతర చెక్పాయింట్లను సేవ్ చేసి శిక్షణను పునఃప్రారంభించడం ఇంకా మద్దతు చేయబడదు.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
అస్పష్టీకరణ:
ఈ పత్రాన్ని AI అనువాద సేవ అయిన [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి శ్రమిస్తామని అయితే కూడా, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా అవిశ్వసనీయతలు ఉండగలవని దయచేసి గమనించండి. స్థానిక языкаలోని (native language) అసలు పత్రాన్ని అధికారిక మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం నిపుణులైన మానవ అనువాదాన్ని సిఫార్సు చేయబడును. ఈ అనువాదం వాడినందున ఏర్పడినఏ అవగాహన లోపాలు లేదా తప్పుగా అర్థం చేసుకోవడాలపై మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->