<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:18:54+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "el"
}
-->
**Fine-tuning του Phi-3 με QLoRA**

Fine-tuning του γλωσσικού μοντέλου Phi-3 Mini της Microsoft χρησιμοποιώντας [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

Το QLoRA θα βοηθήσει στη βελτίωση της κατανόησης συνομιλιών και της δημιουργίας απαντήσεων.

Για να φορτώσετε μοντέλα σε 4bits με transformers και bitsandbytes, πρέπει να εγκαταστήσετε το accelerate και το transformers από τον πηγαίο κώδικα και να βεβαιωθείτε ότι έχετε την πιο πρόσφατη έκδοση της βιβλιοθήκης bitsandbytes.

**Δείγματα**
- [Μάθετε περισσότερα με αυτό το δείγμα notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Παράδειγμα Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Παράδειγμα Fine Tuning στο Hugging Face Hub με LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Παράδειγμα Fine Tuning στο Hugging Face Hub με QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.