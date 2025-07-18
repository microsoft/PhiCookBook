<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-07-17T08:33:13+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "de"
}
-->
# Phi-3.5-vision Finetuning-Anleitung

Dies ist die offizielle Unterstützung für das Finetuning von Phi-3.5-vision mit den huggingface-Bibliotheken. Bitte wechsle vor dem Ausführen der folgenden Befehle in das Code-Verzeichnis [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning).

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

## Schnellstart

Wir stellen zwei Beispielskripte für das Finetuning bereit, eines für DocVQA und eines für die Klassifikation von hasserfüllten Memes.

Minimal getestete Hardware: 4x RTX8000 (48GB RAM pro GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision unterstützt jetzt offiziell Multi-Image-Eingaben. Hier ein Beispiel für das Finetuning von NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Gebrauchsanleitung

Je nach Hardware können Nutzer unterschiedliche Finetuning-Strategien wählen. Wir unterstützen
Full-Finetuning (mit Deepspeed Zero-2) mit optional eingefrorenen Vision-Parametern sowie LoRA (einschließlich 4bit QLoRA).
Generell empfehlen wir, wann immer möglich, Full-Finetuning mit Flash Attention und bf16 zu verwenden.

### Anleitung zur Umwandlung Ihres eigenen Datensatzes in das erforderliche Format

Wir verwenden einen minimalen Video-Klassifikationsdatensatz (ein Teil von UCF-101) als End-to-End-Beispiel, um zu zeigen, wie Sie Ihren eigenen Datensatz in das erforderliche Format konvertieren und Phi-3.5-vision darauf finetunen können.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Die konvertierten Daten sehen dann so aus:

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

Für die `jsonl`-Annotation sollte jede Zeile ein Dictionary sein, das wie folgt aussieht:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Beachten Sie, dass `conversations` eine Liste ist, sodass mehrstufige Gespräche unterstützt werden können, falls solche Daten vorliegen.

## Beantragung von Azure GPU-Kontingent

### Voraussetzungen

Ein Azure-Konto mit der Rolle Contributor (oder einer anderen Rolle, die Contributor-Zugriff beinhaltet).

Falls Sie kein Azure-Konto haben, erstellen Sie [vor Beginn ein kostenloses Konto](https://azure.microsoft.com).

### Beantragung einer Kontingenterhöhung

Sie können eine Anfrage zur Erhöhung des Kontingents direkt über „My quotas“ stellen. Folgen Sie den untenstehenden Schritten, um eine Erhöhung für ein Kontingent zu beantragen. Für dieses Beispiel können Sie ein beliebiges anpassbares Kontingent in Ihrem Abonnement auswählen.

Melden Sie sich im [Azure-Portal](https://portal.azure.com) an.

Geben Sie „quotas“ in das Suchfeld ein und wählen Sie dann „Quotas“ aus.
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Wählen Sie auf der Übersichtsseite einen Anbieter aus, z. B. Compute oder AML.

**Hinweis:** Für alle Anbieter außer Compute sehen Sie statt der Spalte „Adjustable“ eine Spalte „Request increase“. Dort können Sie eine Erhöhung für ein bestimmtes Kontingent anfordern oder eine Supportanfrage für die Erhöhung erstellen.

Wählen Sie auf der Seite „My quotas“ unter „Quota name“ das Kontingent aus, das Sie erhöhen möchten. Stellen Sie sicher, dass in der Spalte „Adjustable“ für dieses Kontingent „Yes“ angezeigt wird.

Wählen Sie oben auf der Seite „New Quota Request“ und dann „Enter a new limit“ aus.

![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

Geben Sie im Bereich „New Quota Request“ einen numerischen Wert für Ihr neues Kontingentlimit ein und wählen Sie „Submit“.

Ihre Anfrage wird geprüft und Sie werden benachrichtigt, ob die Anfrage erfüllt werden kann. Dies geschieht in der Regel innerhalb weniger Minuten.

Wenn Ihre Anfrage nicht erfüllt wird, sehen Sie einen Link, um eine Supportanfrage zu erstellen. Über diesen Link wird Ihnen ein Support-Mitarbeiter bei Ihrer Erhöhungsanfrage helfen.

## Vorschläge für Azure Compute GPU-Maschinen-SKUs

[ND A100 v4-Serie](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-Serie](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Hier einige Beispiele:

### Wenn Sie A100- oder H100-GPUs haben

Full-Finetuning liefert in der Regel die beste Leistung. Sie können den folgenden Befehl verwenden, um Phi-3-V für die Klassifikation hasserfüllter Memes zu finetunen.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Wenn Sie Standard_ND40rs_v2 mit 8x V100-32GB GPUs haben

Es ist weiterhin möglich, Phi-3-V vollständig für die Klassifikation hasserfüllter Memes zu finetunen. Allerdings ist mit deutlich geringerer Durchsatzrate im Vergleich zu A100- oder H100-GPUs zu rechnen, da Flash Attention nicht unterstützt wird.
Die Genauigkeit kann ebenfalls beeinträchtigt sein, da bf16 nicht unterstützt wird (stattdessen wird fp16 Mixed-Precision Training verwendet).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Wenn Sie keinen Zugriff auf Rechenzentrum-GPUs haben

LoRA könnte Ihre einzige Option sein. Sie können den folgenden Befehl verwenden, um Phi-3-V für die Klassifikation hasserfüllter Memes zu finetunen.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Für Turing+ GPUs wird QLoRA unterstützt

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Vorgeschlagene Hyperparameter und erwartete Genauigkeit

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

Trainingsmethode | Eingefrorenes Vision-Modell | Datentyp | LoRA-Rang | LoRA Alpha | Batch-Größe | Lernrate | Epochen | Genauigkeit
--- | --- | --- | --- | --- | --- | --- | --- | --- |
Full-Finetuning |  | bf16 | - | - | 64 | 1e-5 | 3 | 89,40 |
Full-Finetuning | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89,20 |
LoRA-Ergebnisse folgen bald |  |  |  |  |  |  |  |  |

### HINWEIS
Die untenstehenden Ergebnisse für DocVQA und Hateful Memes basieren auf der vorherigen Version (Phi-3-vision).
Die neuen Ergebnisse mit Phi-3.5-vision werden bald aktualisiert.

### DocVQA (HINWEIS: Phi-3-vision)

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

Trainingsmethode | Datentyp | LoRA-Rang | LoRA Alpha | Batch-Größe | Lernrate | Epochen | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
Full-Finetuning | bf16 | - | - | 64 | 5e-6 | 2 | 83,65 |
Full-Finetuning | fp16 | - | - | 64 | 5e-6 | 2 | 82,60 |
Eingefrorenes Bildmodell | bf16 | - | - | 64 | 1e-4 | 2 | 79,19 |
Eingefrorenes Bildmodell | fp16 | - | - | 64 | 1e-4 | 2 | 78,74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82,46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82,34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81,85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81,85 |

### Hateful Memes (HINWEIS: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Trainingsmethode | Datentyp | LoRA-Rang | LoRA Alpha | Batch-Größe | Lernrate | Epochen | Genauigkeit
--- | --- | --- | --- | --- | --- | --- | --- |
Full-Finetuning | bf16 | - | - | 64 | 5e-5 | 2 | 86,4 |
Full-Finetuning | fp16 | - | - | 64 | 5e-5 | 2 | 85,4 |
Eingefrorenes Bildmodell | bf16 | - | - | 64 | 1e-4 | 3 | 79,4 |
Eingefrorenes Bildmodell | fp16 | - | - | 64 | 1e-4 | 3 | 78,6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86,6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85,2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84,0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83,8 |

## Geschwindigkeits-Benchmarking (HINWEIS: Phi-3-vision)

Neue Benchmark-Ergebnisse mit Phi-3.5-vision werden bald veröffentlicht.

Das Benchmarking wurde auf dem DocVQA-Datensatz durchgeführt. Die durchschnittliche Sequenzlänge dieses Datensatzes beträgt 2443,23 Tokens (unter Verwendung von `num_crops=16` für das Bildmodell).

### 8x A100-80GB (Ampere)

Trainingsmethode | \# Knoten | GPUs | Flash Attention | Effektive Batch-Größe | Durchsatz (Bilder/s) | Beschleunigung | Max. GPU-Speicher (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
Full-Finetuning | 1 | 8 |  | 64 | 5,041 | 1x | ~42
Full-Finetuning | 1 | 8 | ✔ | 64 | 8,657 | 1,72x | ~36
Full-Finetuning | 2 | 16 | ✔ | 64 | 16,903 | 3,35x | ~29
Full-Finetuning | 4 | 32 | ✔ | 64 | 33,433 | 6,63x | ~26
Eingefrorenes Bildmodell | 1 | 8 |  | 64 | 17,578 | 3,49x | ~29
Eingefrorenes Bildmodell | 1 | 8 | ✔ | 64 | 31,736 | 6,30x | ~27
LoRA | 1 | 8 |  | 64 | 5,591 | 1,11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12,127 | 2,41x | ~16
QLoRA | 1 | 8 |  | 64 | 4,831 | 0,96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10,545 | 2,09x | ~10

### 8x V100-32GB (Volta)

Trainingsmethode | \# Knoten | GPUs | Flash Attention | Effektive Batch-Größe | Durchsatz (Bilder/s) | Beschleunigung | Max. GPU-Speicher (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
Full-Finetuning | 1 | 8 |  | 64 | 2,462 | 1x | ~32
Full-Finetuning | 2 | 16 |  | 64 | 4,182 | 1,70x | ~32
Full-Finetuning | 4 | 32 |  | 64 | 5,465 | 2,22x | ~32
Eingefrorenes Bildmodell | 1 | 8 |  | 64 | 8,942 | 3,63x | ~27
LoRA | 1 | 8 |  | 64 | 2,807 | 1,14x | ~30

## Bekannte Probleme

- Flash Attention kann nicht mit fp16 ausgeführt werden (bf16 wird immer empfohlen, wenn verfügbar, und alle GPUs, die Flash Attention unterstützen, unterstützen auch bf16).
- Das Speichern von Zwischen-Checkpoints und das Fortsetzen des Trainings wird derzeit nicht unterstützt.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.