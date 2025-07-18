<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:31:40+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "pl"
}
-->
# **Dostrajanie Phi-3 z użyciem Lora**

Dostrajanie modelu językowego Phi-3 Mini firmy Microsoft za pomocą [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) na niestandardowym zbiorze danych z instrukcjami do czatu.

LORA pomoże poprawić rozumienie konwersacji oraz generowanie odpowiedzi.

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

Możesz zdecydować się na adaptację niektórych warstw, zastępując je odpowiednikami zaimplementowanymi w loralib. Obecnie wspieramy tylko nn.Linear, nn.Embedding oraz nn.Conv2d. Obsługujemy także MergedLinear w przypadkach, gdy pojedyncza warstwa nn.Linear reprezentuje więcej niż jedną warstwę, na przykład w niektórych implementacjach projekcji qkv w mechanizmie uwagi (więcej informacji w Dodatkowych Notatkach).

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

Przed rozpoczęciem pętli treningowej oznacz jako trenowalne tylko parametry LoRA.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Podczas zapisywania checkpointu wygeneruj state_dict zawierający wyłącznie parametry LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Podczas ładowania checkpointu za pomocą load_state_dict pamiętaj, aby ustawić strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Teraz trening może przebiegać normalnie.

**Hiperparametry**

Zdefiniuj dwa słowniki: training_config oraz peft_config. training_config zawiera hiperparametry treningu, takie jak learning rate, batch size oraz ustawienia logowania.

peft_config określa parametry związane z LoRA, takie jak rank, dropout oraz typ zadania.

**Ładowanie modelu i tokenizera**

Wskaż ścieżkę do wstępnie wytrenowanego modelu Phi-3 (np. "microsoft/Phi-3-mini-4k-instruct"). Skonfiguruj ustawienia modelu, w tym użycie cache, typ danych (bfloat16 dla mieszanej precyzji) oraz implementację mechanizmu uwagi.

**Trening**

Dostrój model Phi-3 na niestandardowym zbiorze danych z instrukcjami do czatu. Wykorzystaj ustawienia LoRA z peft_config dla efektywnej adaptacji. Monitoruj postęp treningu za pomocą określonej strategii logowania.  
Ewaluacja i zapisywanie: Oceń dostrojony model.  
Zapisuj checkpointy podczas treningu do późniejszego wykorzystania.

**Przykłady**  
- [Dowiedz się więcej dzięki temu przykładowemu notatnikowi](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Przykład skryptu do dostrajania w Pythonie](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Przykład dostrajania na Hugging Face Hub z użyciem LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Przykład karty modelu Hugging Face - przykład dostrajania LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Przykład dostrajania na Hugging Face Hub z użyciem QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.