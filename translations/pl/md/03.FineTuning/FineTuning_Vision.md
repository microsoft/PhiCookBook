<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5a67308d3b2c5af97baf01067c6f007",
  "translation_date": "2025-05-09T22:00:54+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Vision.md",
  "language_code": "pl"
}
-->
# Phi-3.5-vision przepis na dostrajanie

To jest oficjalne wsparcie dla dostrajania Phi-3.5-vision z użyciem bibliotek huggingface.  
Przed uruchomieniem poniższych poleceń, przejdź `cd` do katalogu z kodem [vision_finetuning](../../../../code/03.Finetuning/vision_finetuning).

## Instalacja

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

## Szybki start

Udostępniamy dwa przykładowe skrypty do dostrajania, jeden dla DocVQA i jeden dla klasyfikacji obraźliwych memów.

Minimalny sprzęt testowany to 4x RTX8000 (48GB RAM na GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision oficjalnie wspiera teraz wejścia z wieloma obrazami. Oto przykład dostrajania NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Przewodnik użytkowania

W zależności od sprzętu, użytkownicy mogą wybrać różne strategie dostrajania. Wspieramy  
pełne dostrajanie (z Deepspeed Zero-2) z opcjonalnie zamrożonymi parametrami wizji oraz LoRA (w tym 4bit QLoRA).  
Zalecamy generalnie korzystanie z pełnego dostrajania z flash attention i bf16, gdy tylko jest to możliwe.

### przewodnik konwersji własnego zbioru danych do wymaganego formatu

Używamy minimalnego zbioru danych do klasyfikacji wideo (podzbiór UCF-101) jako przykładu end-to-end, aby pokazać, jak przekonwertować własny zbiór danych do wymaganego formatu i dostroić na nim Phi-3.5-vision.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Przekonwertowane dane będą wyglądać tak:

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

Dla adnotacji `jsonl` każda linia powinna być słownikiem w formacie:

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Zwróć uwagę, że `conversations` jest listą, więc możliwe jest wsparcie konwersacji wieloetapowych, jeśli takie dane są dostępne.

## Jak uzyskać limit GPU na Azure

### Wymagania wstępne

Konto Azure z rolą Contributor (lub inną rolą zawierającą dostęp Contributor).

Jeśli nie masz konta Azure, utwórz [konto darmowe zanim zaczniesz](https://azure.microsoft.com).

### Jak złożyć wniosek o zwiększenie limitu

Możesz złożyć wniosek o zwiększenie limitu bezpośrednio w My quotas. Postępuj według poniższych kroków, aby poprosić o zwiększenie limitu. W tym przykładzie możesz wybrać dowolny regulowany limit w swojej subskrypcji.

Zaloguj się do [Azure portal](https://portal.azure.com).

Wpisz "quotas" w polu wyszukiwania, a następnie wybierz Quotas.  
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Na stronie Overview wybierz dostawcę, np. Compute lub AML.

**Note** Dla wszystkich dostawców poza Compute, zobaczysz kolumnę Request increase zamiast kolumny Adjustable opisanej poniżej. Tam możesz poprosić o zwiększenie konkretnego limitu lub utworzyć zgłoszenie wsparcia.

Na stronie My quotas, w kolumnie Quota name wybierz limit, który chcesz zwiększyć. Upewnij się, że w kolumnie Adjustable dla tego limitu jest wartość Yes.

Na górze strony wybierz New Quota Request, a następnie Enter a new limit.  
![Increase Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

W panelu New Quota Request wpisz wartość numeryczną nowego limitu, a następnie kliknij Submit.

Twój wniosek zostanie rozpatrzony, a Ty zostaniesz powiadomiony, czy został zaakceptowany. Zazwyczaj dzieje się to w ciągu kilku minut.

Jeśli wniosek nie zostanie zaakceptowany, pojawi się link do utworzenia zgłoszenia wsparcia. Korzystając z tego linku, inżynier wsparcia pomoże Ci z Twoim wnioskiem o zwiększenie limitu.

## Propozycje SKU maszyn GPU w Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Oto kilka przykładów:

### Jeśli masz GPU A100 lub H100

Pełne dostrajanie zwykle daje najlepsze wyniki. Możesz użyć poniższego polecenia, aby dostroić Phi-3-V do klasyfikacji obraźliwych memów.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Jeśli masz Standard_ND40rs_v2 8x V100-32GB GPU

Nadal możliwe jest pełne dostrajanie Phi-3-V do klasyfikacji obraźliwych memów. Jednak spodziewaj się znacznie niższej przepustowości w porównaniu do GPU A100 lub H100 ze względu na brak wsparcia dla flash attention.  
Dokładność może również być niższa z powodu braku wsparcia bf16 (zamiast tego stosowane jest mieszane precyzyjne uczenie fp16).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Jeśli nie masz dostępu do GPU w centrum danych

LoRA może być Twoim jedynym wyborem. Możesz użyć poniższego polecenia, aby dostroić Phi-3-V do klasyfikacji obraźliwych memów.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Dla GPU Turing+ obsługiwane jest QLoRA

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Sugerowane hiperparametry i oczekiwana dokładność

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

Metoda treningu | Zamrożony model wizji | typ danych | ranga LoRA | alfa LoRA | rozmiar batcha | współczynnik uczenia | epoki | Dokładność
--- | --- | --- | --- | --- | --- | --- | --- | --- |
pełne dostrajanie |  |bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
pełne dostrajanie | ✔ |bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
Wyniki LoRA wkrótce |  |  |  |  |  |  |  |  |

### NOTE  
Poniższe wyniki DocVQA i Hateful memes opierają się na poprzedniej wersji (Phi-3-vision).  
Nowe wyniki z Phi-3.5-vision zostaną wkrótce opublikowane.

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

Metoda treningu | typ danych | ranga LoRA | alfa LoRA | rozmiar batcha | współczynnik uczenia | epoki | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
pełne dostrajanie | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
pełne dostrajanie | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
zamrożony model obrazu | bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
zamrożony model obrazu | fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
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

Metoda treningu | typ danych | ranga LoRA | alfa LoRA | rozmiar batcha | współczynnik uczenia | epoki | Dokładność
--- | --- | --- | --- | --- | --- | --- | --- |
pełne dostrajanie | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
pełne dostrajanie | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
zamrożony model obrazu | bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
zamrożony model obrazu | fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Testy wydajności (NOTE: Phi-3-vision)

Nowe wyniki testów wydajności z Phi-3.5-vision zostaną wkrótce opublikowane.

Testy wydajności wykonano na zbiorze DocVQA. Średnia długość sekwencji w tym zbiorze to  
2443.23 tokenów (przy użyciu `num_crops=16` dla modelu obrazu).

### 8x A100-80GB (Ampere)

Metoda treningu | \# węzłów | GPU | flash attention | Efektywny rozmiar batcha | Przepustowość (img/s) | Przyspieszenie | Maks. pamięć GPU (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
pełne dostrajanie | 1 | 8 |  | 64 | 5.041 |  1x | ~42
pełne dostrajanie | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
pełne dostrajanie | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
pełne dostrajanie | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
zamrożony model obrazu | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
zamrożony model obrazu | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Metoda treningu | \# węzłów | GPU | flash attention | Efektywny rozmiar batcha | Przepustowość (img/s) | Przyspieszenie | Maks. pamięć GPU (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
pełne dostrajanie | 1 | 8 | | 64 | 2.462 |  1x | ~32
pełne dostrajanie | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
pełne dostrajanie | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
zamrożony model obrazu | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Znane problemy

- Nie można uruchomić flash attention z fp16 (zawsze zalecamy bf16, gdy jest dostępne, a wszystkie GPU wspierające flash attention obsługują też bf16).  
- Nie obsługujemy jeszcze zapisywania pośrednich checkpointów i wznawiania treningu.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiążące. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.