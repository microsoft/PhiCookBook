<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-07T13:34:51+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "fr"
}
-->
# Phi-3.5-vision recette de fine-tuning

Ceci est le support officiel du fine-tuning de Phi-3.5-vision utilisant les bibliothèques huggingface.  
Veuillez `cd` vers le répertoire de code [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) avant d’exécuter les commandes suivantes.

## Installation

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

## Démarrage rapide

Nous fournissons deux scripts d’exemple pour le fine-tuning, un pour DocVQA et un pour la classification de memes haineux.

Matériel minimal testé sur 4x RTX8000 (48GB RAM par GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision prend désormais officiellement en charge les entrées multi-images. Voici un exemple de fine-tuning sur NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Guide d’utilisation

Selon le matériel, les utilisateurs peuvent choisir différentes stratégies de fine-tuning. Nous supportons  
le fine-tuning complet (avec Deepspeed Zero-2) avec la possibilité de geler les paramètres vision, ainsi que LoRA (y compris QLoRA 4 bits).  
En général, nous recommandons d’utiliser le fine-tuning complet avec flash attention et bf16 dès que possible.

### Guide pour convertir votre jeu de données personnalisé au format requis

Nous utilisons un jeu de données minimal de classification vidéo (un sous-ensemble de UCF-101) comme exemple complet pour montrer comment convertir votre jeu de données personnalisé au format requis et fine-tuner Phi-3.5-vision dessus.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Les données converties ressembleront à ceci :

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

Pour l’annotation `jsonl`, chaque ligne doit être un dictionnaire comme :

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Notez que `conversations` est une liste, ce qui permet de supporter des conversations multi-tours si ce type de données est disponible.

## Demande de quota GPU Azure

### Prérequis

Un compte Azure avec le rôle Contributor (ou un autre rôle incluant l’accès Contributor).

Si vous n’avez pas de compte Azure, créez un [compte gratuit avant de commencer](https://azure.microsoft.com).

### Demander une augmentation de quota

Vous pouvez soumettre une demande d’augmentation de quota directement depuis Mes quotas. Suivez les étapes ci-dessous pour demander une augmentation de quota. Pour cet exemple, vous pouvez sélectionner n’importe quel quota ajustable dans votre abonnement.

Connectez-vous au [portail Azure](https://portal.azure.com).

Tapez « quotas » dans la barre de recherche, puis sélectionnez Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Sur la page Aperçu, sélectionnez un fournisseur, comme Compute ou AML.

**Note** Pour tous les fournisseurs autres que Compute, vous verrez une colonne Demander une augmentation au lieu de la colonne Ajustable décrite ci-dessous. Là, vous pouvez demander une augmentation pour un quota spécifique ou créer une demande de support pour cette augmentation.

Sur la page Mes quotas, sous Nom du quota, sélectionnez le quota que vous souhaitez augmenter. Assurez-vous que la colonne Ajustable affiche Oui pour ce quota.

En haut de la page, sélectionnez Nouvelle demande de quota, puis sélectionnez Saisir une nouvelle limite.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

Dans le panneau Nouvelle demande de quota, saisissez une valeur numérique pour votre nouvelle limite de quota, puis cliquez sur Soumettre.

Votre demande sera examinée et vous serez informé si elle peut être satisfaite. Cela se produit généralement en quelques minutes.

Si votre demande n’est pas satisfaite, un lien vous permettra de créer une demande de support. En utilisant ce lien, un ingénieur support vous assistera pour votre demande d’augmentation.

## Suggestions de SKU de machines GPU Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Voici quelques exemples :

### Si vous disposez de GPU A100 ou H100

Le fine-tuning complet offre généralement les meilleures performances. Vous pouvez utiliser la commande suivante pour fine-tuner Phi-3-V sur la classification de memes haineux.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Si vous disposez de GPU Standard_ND40rs_v2 8x V100-32GB

Il est toujours possible de fine-tuner complètement Phi-3-V sur la classification de memes haineux. Cependant, attendez-vous à un débit beaucoup plus faible comparé aux GPU A100 ou H100 à cause de l’absence de support pour flash attention.  
La précision peut aussi être impactée du fait de l’absence de support bf16 (l’entraînement en précision mixte fp16 est utilisé à la place).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Si vous n’avez pas accès à des GPU de centre de données

LoRA pourrait être votre seule option. Vous pouvez utiliser la commande suivante pour fine-tuner Phi-3-V sur la classification de memes haineux.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Pour les GPU Turing+ QLoRA est supporté

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Hyperparamètres suggérés et précision attendue

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

Méthode d’entraînement | Modèle vision gelé | type de données | rang LoRA | alpha LoRA | taille de batch | taux d’apprentissage | époques | Précision  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20  
Résultats LoRA à venir |  |  |  |  |  |  |  |  

### NOTE  
Les résultats DocVQA et Hateful memes ci-dessous sont basés sur la version précédente (Phi-3-vision).  
Les nouveaux résultats avec Phi-3.5-vision seront bientôt mis à jour.

### DocVQA (NOTE : Phi-3-vision)

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

Méthode d’entraînement | type de données | rang LoRA | alpha LoRA | taille de batch | taux d’apprentissage | époques | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60  
modèle image gelé | bf16 | - | - | 64 | 1e-4 | 2 | 79.19  
modèle image gelé | fp16 | - | - | 64 | 1e-4 | 2 | 78.74  
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46  
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34  
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85  
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85  

### Hateful memes (NOTE : Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Méthode d’entraînement | type de données | rang LoRA | alpha LoRA | taille de batch | taux d’apprentissage | époques | Précision  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4  
modèle image gelé | bf16 | - | - | 64 | 1e-4 | 3 | 79.4  
modèle image gelé | fp16 | - | - | 64 | 1e-4 | 3 | 78.6  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8  

## Benchmark de vitesse (NOTE : Phi-3-vision)

Les nouveaux résultats de benchmark avec Phi-3.5-vision seront bientôt mis à jour.

Le benchmark de vitesse est réalisé sur le dataset DocVQA. La longueur moyenne des séquences dans ce dataset est de 2443.23 tokens (en utilisant `num_crops=16` pour le modèle image).

### 8x A100-80GB (Ampere)

Méthode d’entraînement | \# nœuds | GPUs | flash attention | Taille effective du batch | Débit (img/s) | Accélération | Mémoire GPU max (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 |  1x | ~42  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
modèle image gelé | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
modèle image gelé | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Méthode d’entraînement | \# nœuds | GPUs | flash attention | Taille effective du batch | Débit (img/s) | Accélération | Mémoire GPU max (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 | | 64 | 2.462 |  1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
modèle image gelé | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Problèmes connus

- Impossible d’exécuter flash attention avec fp16 (bf16 est toujours recommandé quand disponible, et tous les GPU supportant flash attention supportent aussi bf16).  
- Le sauvegarde des checkpoints intermédiaires et la reprise de l’entraînement ne sont pas encore supportés.

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.