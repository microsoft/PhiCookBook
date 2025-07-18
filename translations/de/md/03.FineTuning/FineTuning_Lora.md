<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:27:10+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "de"
}
-->
# **Feinabstimmung von Phi-3 mit Lora**

Feinabstimmung von Microsofts Phi-3 Mini Sprachmodell mit [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) auf einem eigenen Chat-Instruktionsdatensatz.

LORA hilft dabei, das Verständnis von Gesprächen und die Antwortgenerierung zu verbessern.

## Schritt-für-Schritt-Anleitung zur Feinabstimmung von Phi-3 Mini:

**Imports und Einrichtung**

Installation von loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Beginnen Sie mit dem Import der benötigten Bibliotheken wie datasets, transformers, peft, trl und torch.  
Richten Sie das Logging ein, um den Trainingsverlauf zu verfolgen.

Sie können einige Schichten anpassen, indem Sie sie durch Pendants aus loralib ersetzen. Derzeit unterstützen wir nur nn.Linear, nn.Embedding und nn.Conv2d. Außerdem unterstützen wir MergedLinear für Fälle, in denen ein einzelnes nn.Linear mehrere Schichten repräsentiert, wie z. B. bei einigen Implementierungen der Attention qkv-Projektion (siehe Zusätzliche Hinweise für mehr Details).

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

Vor Beginn der Trainingsschleife markieren Sie nur die LoRA-Parameter als trainierbar.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Beim Speichern eines Checkpoints erzeugen Sie ein state_dict, das nur die LoRA-Parameter enthält.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Beim Laden eines Checkpoints mit load_state_dict stellen Sie sicher, dass strict=False gesetzt ist.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Nun kann das Training wie gewohnt fortgesetzt werden.

**Hyperparameter**

Definieren Sie zwei Dictionaries: training_config und peft_config. training_config enthält Hyperparameter für das Training, wie Lernrate, Batch-Größe und Logging-Einstellungen.

peft_config legt LoRA-bezogene Parameter wie Rang, Dropout und Aufgabentyp fest.

**Modell- und Tokenizer-Laden**

Geben Sie den Pfad zum vortrainierten Phi-3 Modell an (z. B. "microsoft/Phi-3-mini-4k-instruct"). Konfigurieren Sie die Modelleinstellungen, einschließlich Cache-Nutzung, Datentyp (bfloat16 für gemischte Präzision) und Attention-Implementierung.

**Training**

Feinabstimmung des Phi-3 Modells mit dem eigenen Chat-Instruktionsdatensatz. Nutzen Sie die LoRA-Einstellungen aus peft_config für eine effiziente Anpassung. Überwachen Sie den Trainingsfortschritt mit der angegebenen Logging-Strategie.  
Evaluation und Speicherung: Bewerten Sie das feinabgestimmte Modell.  
Speichern Sie Checkpoints während des Trainings für die spätere Verwendung.

**Beispiele**  
- [Mehr erfahren mit diesem Beispiel-Notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Beispiel für Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Beispiel für Hugging Face Hub Fine Tuning mit LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Beispiel Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Beispiel für Hugging Face Hub Fine Tuning mit QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.