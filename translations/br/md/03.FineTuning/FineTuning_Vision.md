<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-07-17T08:43:17+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "br"
}
-->
# Receita de fine-tuning do Phi-3.5-vision

Este é o suporte oficial para fine-tuning do Phi-3.5-vision usando as bibliotecas huggingface.  
Por favor, `cd` para o diretório de código [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) antes de executar os comandos a seguir.

## Instalação

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

## Início rápido

Fornecemos dois scripts de fine-tuning de exemplo, um para DocVQA e outro para classificação de memes de ódio.

Hardware mínimo testado: 4x RTX8000 (48GB RAM por GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

O Phi-3.5-vision agora suporta oficialmente entradas com múltiplas imagens. Aqui está um exemplo para fine-tuning no NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Guia de uso

Dependendo do hardware, os usuários podem escolher diferentes estratégias de fine-tuning. Suportamos  
full-finetuning (com Deepspeed Zero-2) com parâmetros de visão opcionalmente congelados, e LoRA (incluindo QLoRA 4bit).  
Em geral, recomendamos usar full finetuning com flash attention e bf16 sempre que possível.

### Guia para converter seu dataset customizado para o formato requerido

Usamos um dataset mínimo de classificação de vídeo (um subconjunto do UCF-101) como exemplo completo para demonstrar como converter seu dataset customizado para o formato necessário e fazer fine-tuning do Phi-3.5-vision nele.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Os dados convertidos ficarão assim:

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

Para a anotação `jsonl`, cada linha deve ser um dicionário como:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Note que `conversations` é uma lista, portanto conversas com múltiplas interações podem ser suportadas se esses dados estiverem disponíveis.

## Solicitando cota de GPU no Azure

### Pré-requisitos

Uma conta Azure com a função de Contributor (ou outra função que inclua acesso de Contributor).

Se você não tem uma conta Azure, crie uma [conta gratuita antes de começar](https://azure.microsoft.com).

### Solicitar aumento de cota

Você pode enviar uma solicitação de aumento de cota diretamente em My quotas. Siga os passos abaixo para solicitar um aumento de cota. Neste exemplo, você pode selecionar qualquer cota ajustável na sua assinatura.

Faça login no [portal Azure](https://portal.azure.com).

Digite "quotas" na caixa de busca e selecione Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Na página Overview, selecione um provedor, como Compute ou AML.

**Note** Para todos os provedores exceto Compute, você verá uma coluna Request increase em vez da coluna Adjustable descrita abaixo. Lá, você pode solicitar um aumento para uma cota específica ou criar uma solicitação de suporte para o aumento.

Na página My quotas, em Quota name, selecione a cota que deseja aumentar. Certifique-se de que a coluna Adjustable mostre Yes para essa cota.

No topo da página, selecione New Quota Request, depois selecione Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

No painel New Quota Request, insira um valor numérico para o novo limite de cota e selecione Submit.

Sua solicitação será analisada e você será notificado se ela puder ser atendida. Isso geralmente acontece em poucos minutos.

Se sua solicitação não for atendida, você verá um link para criar uma solicitação de suporte. Ao usar esse link, um engenheiro de suporte irá ajudá-lo com seu pedido de aumento.

## Sugestões de SKU para máquinas GPU Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Aqui estão alguns exemplos:

### Se você tem GPUs A100 ou H100

Full finetuning geralmente oferece o melhor desempenho. Você pode usar o comando abaixo para fazer fine-tuning do Phi-3-V na classificação de memes de ódio.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Se você tem GPUs Standard_ND40rs_v2 8x V100-32GB

Ainda é possível fazer fine-tuning completo do Phi-3-V na classificação de memes de ódio. No entanto, espere  
uma taxa de processamento muito menor comparada às GPUs A100 ou H100 devido à falta de suporte a flash attention.  
A acurácia também pode ser afetada pela ausência de suporte a bf16 (treinamento em precisão mista fp16 é usado no lugar).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Se você não tem acesso a GPUs de data center

LoRA pode ser sua única opção. Você pode usar o comando abaixo para fazer fine-tuning do Phi-3-V na classificação de memes de ódio.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Para GPUs Turing+ o QLoRA é suportado

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Hiperparâmetros sugeridos e acurácia esperada

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

Método de treinamento | Modelo de visão congelado | tipo de dado | rank LoRA | alpha LoRA | tamanho do batch | taxa de aprendizado | épocas | Acurácia
--- | --- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
Resultados LoRA em breve |  |  |  |  |  |  |  |  |

### NOTE  
Os resultados abaixo para DocVQA e Hateful memes são baseados na versão anterior (Phi-3-vision).  
Os novos resultados com Phi-3.5-vision serão atualizados em breve.

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

Método de treinamento | tipo de dado | rank LoRA | alpha LoRA | tamanho do batch | taxa de aprendizado | épocas | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
modelo de imagem congelado | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
modelo de imagem congelado | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
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

Método de treinamento | tipo de dado | rank LoRA | alpha LoRA | tamanho do batch | taxa de aprendizado | épocas | Acurácia
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
modelo de imagem congelado | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
modelo de imagem congelado | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Benchmark de velocidade (NOTE: Phi-3-vision)

Novos resultados de benchmark com Phi-3.5-vision serão atualizados em breve.

O benchmark de velocidade foi realizado no dataset DocVQA. O comprimento médio da sequência deste dataset  
é 2443.23 tokens (usando `num_crops=16` para o modelo de imagem).

### 8x A100-80GB (Ampere)

Método de treinamento | \# nós | GPUs | flash attention | Tamanho efetivo do batch | Throughput (img/s) | Aceleração | Pico de memória GPU (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
modelo de imagem congelado | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
modelo de imagem congelado | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Método de treinamento | \# nós | GPUs | flash attention | Tamanho efetivo do batch | Throughput (img/s) | Aceleração | Pico de memória GPU (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
modelo de imagem congelado | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Problemas conhecidos

- Não é possível rodar flash attention com fp16 (bf16 é sempre recomendado quando disponível, e todas as GPUs que suportam flash attention também suportam bf16).  
- Ainda não há suporte para salvar checkpoints intermediários e retomar o treinamento.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.