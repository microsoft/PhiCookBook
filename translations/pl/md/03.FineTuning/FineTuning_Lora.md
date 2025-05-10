<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:45:21+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "pl"
}
-->
# **Dostrajanie Phi-3 z Lora**

Dostrajanie modelu językowego Phi-3 Mini firmy Microsoft za pomocą [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) na niestandardowym zbiorze danych instrukcji czatu.

LORA pomoże poprawić rozumienie konwersacji i generowanie odpowiedzi.

## Przewodnik krok po kroku, jak dostroić Phi-3 Mini:

**Importy i konfiguracja**

Instalacja loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Na początek zaimportuj niezbędne biblioteki, takie jak datasets, transformers, peft, trl oraz torch.  
Skonfiguruj logowanie, aby śledzić przebieg treningu.

Możesz zdecydować się na dostosowanie niektórych warstw, zastępując je odpowiednikami zaimplementowanymi w loralib. Obecnie obsługujemy tylko nn.Linear, nn.Embedding oraz nn.Conv2d. Wspieramy też MergedLinear dla przypadków, gdy pojedynczy nn.Linear reprezentuje więcej niż jedną warstwę, np. w niektórych implementacjach projekcji qkv w mechanizmie uwagi (więcej w Dodatkowych Notatkach).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Przed rozpoczęciem pętli treningowej oznacz jako trenowalne wyłącznie parametry LoRA.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Podczas zapisywania checkpointu wygeneruj state_dict zawierający tylko parametry LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Podczas wczytywania checkpointu za pomocą load_state_dict ustaw parametr strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Teraz trening może przebiegać jak zwykle.

**Hiperparametry**

Zdefiniuj dwa słowniki: training_config oraz peft_config. training_config zawiera hiperparametry treningu, takie jak learning rate, batch size i ustawienia logowania.

peft_config określa parametry związane z LoRA, takie jak rank, dropout i typ zadania.

**Ładowanie modelu i tokenizera**

Podaj ścieżkę do wstępnie wytrenowanego modelu Phi-3 (np. "microsoft/Phi-3-mini-4k-instruct"). Skonfiguruj ustawienia modelu, w tym użycie cache, typ danych (bfloat16 dla mieszanej precyzji) oraz implementację uwagi.

**Trening**

Dostrój model Phi-3 za pomocą niestandardowego zbioru instrukcji czatu. Wykorzystaj ustawienia LoRA z peft_config do efektywnej adaptacji. Monitoruj postępy treningu zgodnie z wybraną strategią logowania.  
Ewaluacja i zapisywanie: oceń dostrojony model.  
Zapisuj checkpointy podczas treningu do późniejszego wykorzystania.

**Przykłady**  
- [Dowiedz się więcej dzięki temu przykładowi notebooka](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Przykład skryptu FineTuning w Pythonie](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Przykład dostrajania na Hugging Face Hub z LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Przykład karty modelu Hugging Face - przykład dostrajania LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Przykład dostrajania na Hugging Face Hub z QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być uznawany za wiarygodne źródło. W przypadku informacji o istotnym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.