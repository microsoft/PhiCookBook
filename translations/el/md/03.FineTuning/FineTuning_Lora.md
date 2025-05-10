<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:45:38+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "el"
}
-->
# **Λεπτομερής εκπαίδευση του Phi-3 με Lora**

Λεπτομερής εκπαίδευση του μοντέλου γλώσσας Phi-3 Mini της Microsoft χρησιμοποιώντας [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) σε ένα προσαρμοσμένο σύνολο δεδομένων οδηγίας συνομιλίας.

Το LORA θα βοηθήσει στη βελτίωση της κατανόησης της συνομιλίας και της δημιουργίας απαντήσεων.

## Οδηγός βήμα-βήμα για το πώς να εκπαιδεύσετε το Phi-3 Mini:

**Εισαγωγές και Ρυθμίσεις**

Εγκατάσταση του loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Ξεκινήστε εισάγοντας τις απαραίτητες βιβλιοθήκες όπως datasets, transformers, peft, trl και torch.  
Ρυθμίστε το logging για να παρακολουθείτε τη διαδικασία εκπαίδευσης.

Μπορείτε να επιλέξετε να προσαρμόσετε κάποια στρώματα αντικαθιστώντας τα με αντίστοιχα υλοποιημένα στο loralib. Προς το παρόν υποστηρίζουμε μόνο nn.Linear, nn.Embedding και nn.Conv2d. Επίσης, υποστηρίζουμε το MergedLinear για περιπτώσεις όπου ένα μόνο nn.Linear αντιπροσωπεύει περισσότερα από ένα στρώματα, όπως σε κάποιες υλοποιήσεις της προβολής qkv του attention (δείτε τις Επιπλέον Σημειώσεις για περισσότερα).

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

Πριν ξεκινήσει ο βρόχος εκπαίδευσης, επισημάνετε μόνο τις παραμέτρους του LoRA ως εκπαιδεύσιμες.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Κατά την αποθήκευση ενός checkpoint, δημιουργήστε ένα state_dict που να περιέχει μόνο τις παραμέτρους του LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Κατά τη φόρτωση ενός checkpoint με load_state_dict, βεβαιωθείτε ότι το strict έχει οριστεί σε False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Τώρα η εκπαίδευση μπορεί να συνεχιστεί κανονικά.

**Υπερπαράμετροι**

Ορίστε δύο λεξικά: training_config και peft_config. Το training_config περιλαμβάνει υπερπαράμετρους για την εκπαίδευση, όπως learning rate, μέγεθος παρτίδας και ρυθμίσεις logging.

Το peft_config καθορίζει παραμέτρους σχετικές με το LoRA, όπως rank, dropout και τύπο εργασίας.

**Φόρτωση Μοντέλου και Tokenizer**

Καθορίστε τη διαδρομή προς το προεκπαιδευμένο μοντέλο Phi-3 (π.χ. "microsoft/Phi-3-mini-4k-instruct"). Ρυθμίστε τις παραμέτρους του μοντέλου, συμπεριλαμβανομένης της χρήσης cache, τύπου δεδομένων (bfloat16 για μικτή ακρίβεια) και υλοποίησης attention.

**Εκπαίδευση**

Εκπαιδεύστε εκ νέου το μοντέλο Phi-3 χρησιμοποιώντας το προσαρμοσμένο σύνολο δεδομένων οδηγιών συνομιλίας. Χρησιμοποιήστε τις ρυθμίσεις LoRA από το peft_config για αποδοτική προσαρμογή. Παρακολουθήστε την πρόοδο της εκπαίδευσης με τη συγκεκριμένη στρατηγική logging.  
Αξιολόγηση και Αποθήκευση: Αξιολογήστε το λεπτομερώς εκπαιδευμένο μοντέλο.  
Αποθηκεύστε checkpoints κατά τη διάρκεια της εκπαίδευσης για μελλοντική χρήση.

**Δείγματα**  
- [Μάθετε περισσότερα με αυτό το δείγμα notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Παράδειγμα Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Παράδειγμα Hugging Face Hub Fine Tuning με LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Παράδειγμα Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Παράδειγμα Hugging Face Hub Fine Tuning με QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται η επαγγελματική μετάφραση από άνθρωπο. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.