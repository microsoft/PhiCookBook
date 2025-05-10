<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:45:12+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "it"
}
-->
# **Fine-tuning di Phi-3 con Lora**

Fine-tuning del modello linguistico Phi-3 Mini di Microsoft utilizzando [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) su un dataset personalizzato di istruzioni per chat.

LORA aiuterà a migliorare la comprensione conversazionale e la generazione delle risposte.

## Guida passo passo per il fine-tuning di Phi-3 Mini:

**Importazioni e configurazione**

Installazione di loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Inizia importando le librerie necessarie come datasets, transformers, peft, trl e torch.  
Configura il logging per monitorare il processo di training.

Puoi scegliere di adattare alcuni layer sostituendoli con equivalenti implementati in loralib. Al momento supportiamo solo nn.Linear, nn.Embedding e nn.Conv2d. Supportiamo anche MergedLinear per i casi in cui un singolo nn.Linear rappresenta più layer, come in alcune implementazioni della proiezione qkv dell’attenzione (vedi Note Aggiuntive per maggiori dettagli).

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

Prima di iniziare il ciclo di training, imposta come addestrabili solo i parametri di LoRA.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Quando salvi un checkpoint, genera uno state_dict che contenga solo i parametri di LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Quando carichi un checkpoint usando load_state_dict, assicurati di impostare strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Ora il training può procedere normalmente.

**Iperparametri**

Definisci due dizionari: training_config e peft_config. training_config contiene gli iperparametri per il training, come learning rate, batch size e impostazioni di logging.

peft_config specifica i parametri relativi a LoRA, come rank, dropout e tipo di task.

**Caricamento del modello e del tokenizer**

Specifica il percorso del modello Phi-3 pre-addestrato (es. "microsoft/Phi-3-mini-4k-instruct"). Configura le impostazioni del modello, incluso l’uso della cache, il tipo di dato (bfloat16 per precisione mista) e l’implementazione dell’attenzione.

**Training**

Esegui il fine-tuning del modello Phi-3 usando il dataset personalizzato di istruzioni per chat. Usa le impostazioni LoRA da peft_config per un’adattamento efficiente. Monitora il progresso del training con la strategia di logging specificata.  
Valutazione e salvataggio: valuta il modello fine-tuned.  
Salva checkpoint durante il training per usi successivi.

**Esempi**  
- [Scopri di più con questo notebook di esempio](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Esempio di Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Esempio di Fine Tuning su Hugging Face Hub con LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Esempio Hugging Face Model Card - Campione di Fine Tuning con LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Esempio di Fine Tuning su Hugging Face Hub con QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.