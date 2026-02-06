# Phi-3.5-vision συνταγή fine-tuning

Αυτή είναι η επίσημη υποστήριξη για το fine-tuning του Phi-3.5-vision χρησιμοποιώντας τις βιβλιοθήκες huggingface.  
Παρακαλώ κάντε `cd` στον φάκελο κώδικα [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning) πριν εκτελέσετε τις παρακάτω εντολές.

## Εγκατάσταση

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

## Γρήγορη εκκίνηση

Παρέχουμε δύο παραδείγματα σεναρίων fine-tuning, ένα για DocVQA και ένα για ταξινόμηση hateful memes.

Ελάχιστος εξοπλισμός που έχει δοκιμαστεί: 4x RTX8000 (48GB RAM ανά GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Το Phi-3.5-vision πλέον υποστηρίζει επίσημα εισόδους με πολλαπλές εικόνες. Εδώ είναι ένα παράδειγμα για fine-tuning στο NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Οδηγός χρήσης

Ανάλογα με τον εξοπλισμό, οι χρήστες μπορούν να επιλέξουν διαφορετικές στρατηγικές fine-tuning. Υποστηρίζουμε  
full-finetuning (με Deepspeed Zero-2) με προαιρετικά παγωμένες παραμέτρους όρασης, καθώς και LoRA (συμπεριλαμβανομένου του 4bit QLoRA).  
Γενικά, προτείνουμε τη χρήση full fine-tuning με flash attention και bf16 όπου είναι δυνατόν.

### Οδηγός για τη μετατροπή του δικού σας dataset στη απαιτούμενη μορφή

Χρησιμοποιούμε ένα ελάχιστο dataset ταξινόμησης βίντεο (υποσύνολο του UCF-101) ως παράδειγμα end-to-end για να δείξουμε πώς να μετατρέψετε το δικό σας dataset στη σωστή μορφή και να κάνετε fine-tuning το Phi-3.5-vision πάνω σε αυτό.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Τα μετατρεπόμενα δεδομένα θα μοιάζουν ως εξής:

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

Για την `jsonl` ανάλυση, κάθε γραμμή πρέπει να είναι ένα λεξικό όπως:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Σημειώστε ότι το `conversations` είναι λίστα, επομένως υποστηρίζεται πολυ-γύρος συνομιλίας αν υπάρχουν τέτοια δεδομένα.

## Αίτηση για Azure GPU Quota

### Προαπαιτούμενα

Λογαριασμός Azure με ρόλο Contributor (ή άλλο ρόλο που περιλαμβάνει πρόσβαση Contributor).

Αν δεν έχετε λογαριασμό Azure, δημιουργήστε έναν [δωρεάν λογαριασμό πριν ξεκινήσετε](https://azure.microsoft.com).

### Αίτηση για αύξηση quota

Μπορείτε να υποβάλετε αίτηση για αύξηση quota απευθείας από το My quotas. Ακολουθήστε τα παρακάτω βήματα για να ζητήσετε αύξηση quota. Για το παράδειγμα αυτό, μπορείτε να επιλέξετε οποιοδήποτε ρυθμιζόμενο quota στη συνδρομή σας.

Συνδεθείτε στο [Azure portal](https://portal.azure.com).

Πληκτρολογήστε "quotas" στο πεδίο αναζήτησης και επιλέξτε Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Στη σελίδα Overview, επιλέξτε έναν πάροχο, όπως Compute ή AML.

**Note** Για όλους τους παρόχους εκτός του Compute, θα δείτε τη στήλη Request increase αντί για την Adjustable που περιγράφεται παρακάτω. Εκεί μπορείτε να ζητήσετε αύξηση για συγκεκριμένο quota ή να δημιουργήσετε αίτημα υποστήριξης για την αύξηση.

Στη σελίδα My quotas, κάτω από το Quota name, επιλέξτε το quota που θέλετε να αυξήσετε. Βεβαιωθείτε ότι η στήλη Adjustable δείχνει Yes για αυτό το quota.

Κοντά στην κορυφή της σελίδας, επιλέξτε New Quota Request και μετά Enter a new limit.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

Στο παράθυρο New Quota Request, εισάγετε μια αριθμητική τιμή για το νέο όριο quota και επιλέξτε Submit.

Η αίτησή σας θα εξεταστεί και θα ενημερωθείτε αν μπορεί να ικανοποιηθεί. Αυτό συνήθως συμβαίνει μέσα σε λίγα λεπτά.

Αν η αίτησή σας δεν ικανοποιηθεί, θα δείτε έναν σύνδεσμο για να δημιουργήσετε αίτημα υποστήριξης. Χρησιμοποιώντας αυτόν τον σύνδεσμο, ένας μηχανικός υποστήριξης θα σας βοηθήσει με το αίτημα αύξησης.

## Προτάσεις για Azure Compute GPU μηχανές SKU

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Εδώ μερικά παραδείγματα:

### Αν έχετε GPUs A100 ή H100

Το full fine-tuning συνήθως δίνει την καλύτερη απόδοση. Μπορείτε να χρησιμοποιήσετε την παρακάτω εντολή για fine-tuning του Phi-3-V στην ταξινόμηση hateful memes.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Αν έχετε Standard_ND40rs_v2 8x V100-32GB GPUs

Είναι ακόμα εφικτό να κάνετε πλήρες fine-tuning του Phi-3-V στην ταξινόμηση hateful memes. Ωστόσο, αναμένετε πολύ χαμηλότερο throughput σε σύγκριση με A100 ή H100 GPUs λόγω της έλλειψης υποστήριξης flash attention.  
Η ακρίβεια μπορεί επίσης να επηρεαστεί λόγω της έλλειψης υποστήριξης bf16 (αντί αυτού χρησιμοποιείται εκπαίδευση μικτής ακρίβειας fp16).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Αν δεν έχετε πρόσβαση σε GPUs data center

Το LoRA μπορεί να είναι η μόνη σας επιλογή. Μπορείτε να χρησιμοποιήσετε την παρακάτω εντολή για fine-tuning του Phi-3-V στην ταξινόμηση hateful memes.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Για GPU Turing+ υποστηρίζεται QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Προτεινόμενες υπερπαραμέτρους και αναμενόμενη ακρίβεια

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

Μέθοδος εκπαίδευσης | Παγωμένο μοντέλο όρασης | τύπος δεδομένων | LoRA rank | LoRA alpha | μέγεθος batch | ρυθμός μάθησης | εποχές | Ακρίβεια  
--- | --- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |  
full-finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |  
Αποτελέσματα LoRA σύντομα |  |  |  |  |  |  |  |  |

### NOTE  
Τα παρακάτω αποτελέσματα για DocVQA και Hateful memes βασίζονται στην προηγούμενη έκδοση (Phi-3-vision).  
Τα νέα αποτελέσματα με το Phi-3.5-vision θα ανανεωθούν σύντομα.

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

Μέθοδος εκπαίδευσης | τύπος δεδομένων | LoRA rank | LoRA alpha | μέγεθος batch | ρυθμός μάθησης | εποχές | ANLS  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |  
full-finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |  
παγωμένο μοντέλο εικόνας | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |  
παγωμένο μοντέλο εικόνας | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |  
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

Μέθοδος εκπαίδευσης | τύπος δεδομένων | LoRA rank | LoRA alpha | μέγεθος batch | ρυθμός μάθησης | εποχές | Ακρίβεια  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |  
full-finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |  
παγωμένο μοντέλο εικόνας | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |  
παγωμένο μοντέλο εικόνας | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |  
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |  
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |  
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |  
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Μέτρηση ταχύτητας (NOTE: Phi-3-vision)

Νέα αποτελέσματα benchmarking με το Phi-3.5-vision θα ανανεωθούν σύντομα.

Η μέτρηση ταχύτητας γίνεται στο dataset DocVQA. Το μέσο μήκος ακολουθίας αυτού του dataset είναι 2443.23 tokens (χρησιμοποιώντας `num_crops=16` για το μοντέλο εικόνας).

### 8x A100-80GB (Ampere)

Μέθοδος εκπαίδευσης | \# κόμβοι | GPUs | flash attention | Αποτελεσματικό μέγεθος batch | Throughput (εικόνες/δευτ.) | Επιτάχυνση | Μέγιστη μνήμη GPU (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 5.041 | 1x | ~42  
full-finetuning | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36  
full-finetuning | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29  
full-finetuning | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26  
παγωμένο μοντέλο εικόνας | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29  
παγωμένο μοντέλο εικόνας | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27  
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50  
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16  
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32  
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10  

### 8x V100-32GB (Volta)

Μέθοδος εκπαίδευσης | \# κόμβοι | GPUs | flash attention | Αποτελεσματικό μέγεθος batch | Throughput (εικόνες/δευτ.) | Επιτάχυνση | Μέγιστη μνήμη GPU (GB)  
--- | --- | --- | --- | --- | --- | --- | --- |  
full-finetuning | 1 | 8 |  | 64 | 2.462 | 1x | ~32  
full-finetuning | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32  
full-finetuning | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32  
παγωμένο μοντέλο εικόνας | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27  
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30  

## Γνωστά προβλήματα

- Δεν μπορεί να τρέξει flash attention με fp16 (το bf16 προτείνεται πάντα όταν είναι διαθέσιμο, και όλες οι GPUs που υποστηρίζουν flash attention υποστηρίζουν επίσης bf16).  
- Δεν υποστηρίζεται ακόμα η αποθήκευση ενδιάμεσων checkpoints και η συνέχιση της εκπαίδευσης.

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να λάβετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.