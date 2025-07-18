<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-07-17T06:32:03+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "el"
}
-->
# **Fine-tuning του Phi-3 με Lora**

Fine-tuning του γλωσσικού μοντέλου Phi-3 Mini της Microsoft χρησιμοποιώντας [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) σε ένα προσαρμοσμένο σύνολο δεδομένων με οδηγίες συνομιλίας.

Το LORA θα βοηθήσει στη βελτίωση της κατανόησης της συνομιλίας και της δημιουργίας απαντήσεων.

## Οδηγός βήμα προς βήμα για το fine-tuning του Phi-3 Mini:

**Εισαγωγές και Ρυθμίσεις**

Εγκατάσταση του loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Ξεκινήστε εισάγοντας τις απαραίτητες βιβλιοθήκες όπως datasets, transformers, peft, trl και torch.  
Ρυθμίστε το logging για να παρακολουθείτε τη διαδικασία εκπαίδευσης.

Μπορείτε να επιλέξετε να προσαρμόσετε ορισμένα στρώματα αντικαθιστώντας τα με αντίστοιχα που υλοποιούνται στο loralib. Προς το παρόν υποστηρίζουμε μόνο nn.Linear, nn.Embedding και nn.Conv2d. Υποστηρίζουμε επίσης το MergedLinear για περιπτώσεις όπου ένα μόνο nn.Linear αντιπροσωπεύει περισσότερα από ένα στρώματα, όπως σε κάποιες υλοποιήσεις της προβολής qkv της προσοχής (δείτε τις Επιπλέον Σημειώσεις για περισσότερα).

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

Πριν ξεκινήσει ο βρόχος εκπαίδευσης, ορίστε ως εκπαιδεύσιμες μόνο τις παραμέτρους του LoRA.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Κατά την αποθήκευση ενός checkpoint, δημιουργήστε ένα state_dict που περιέχει μόνο τις παραμέτρους του LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Κατά τη φόρτωση ενός checkpoint με τη χρήση του load_state_dict, βεβαιωθείτε ότι έχετε ορίσει strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Τώρα η εκπαίδευση μπορεί να συνεχιστεί κανονικά.

**Υπερπαράμετροι**

Ορίστε δύο λεξικά: training_config και peft_config. Το training_config περιλαμβάνει υπερπαραμέτρους για την εκπαίδευση, όπως learning rate, μέγεθος batch και ρυθμίσεις logging.

Το peft_config καθορίζει παραμέτρους σχετικές με το LoRA, όπως rank, dropout και τύπο εργασίας.

**Φόρτωση Μοντέλου και Tokenizer**

Καθορίστε τη διαδρομή προς το προεκπαιδευμένο μοντέλο Phi-3 (π.χ. "microsoft/Phi-3-mini-4k-instruct"). Ρυθμίστε τις παραμέτρους του μοντέλου, συμπεριλαμβανομένης της χρήσης cache, του τύπου δεδομένων (bfloat16 για μικτή ακρίβεια) και της υλοποίησης της προσοχής.

**Εκπαίδευση**

Κάντε fine-tune το μοντέλο Phi-3 χρησιμοποιώντας το προσαρμοσμένο σύνολο δεδομένων με οδηγίες συνομιλίας. Χρησιμοποιήστε τις ρυθμίσεις LoRA από το peft_config για αποδοτική προσαρμογή. Παρακολουθήστε την πρόοδο της εκπαίδευσης με τη συγκεκριμένη στρατηγική logging.  
Αξιολόγηση και Αποθήκευση: Αξιολογήστε το fine-tuned μοντέλο.  
Αποθηκεύστε checkpoints κατά τη διάρκεια της εκπαίδευσης για μελλοντική χρήση.

**Δείγματα**  
- [Μάθετε περισσότερα με αυτό το δείγμα notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Παράδειγμα Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Παράδειγμα Hugging Face Hub Fine Tuning με LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Παράδειγμα Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Παράδειγμα Hugging Face Hub Fine Tuning με QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.