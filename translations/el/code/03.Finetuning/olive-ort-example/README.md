<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:32:12+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "el"
}
-->
# Fine-tune Phi3 using Olive

Σε αυτό το παράδειγμα θα χρησιμοποιήσετε το Olive για να:

1. Κάνετε fine-tune σε έναν LoRA adapter για να ταξινομήσετε φράσεις σε Sad, Joy, Fear, Surprise.
1. Συγχωνεύσετε τα βάρη του adapter στο βασικό μοντέλο.
1. Βελτιστοποιήσετε και ποσοτικοποιήσετε το μοντέλο σε `int4`.

Θα δείξουμε επίσης πώς να κάνετε inference με το fine-tuned μοντέλο χρησιμοποιώντας το ONNX Runtime (ORT) Generate API.

> **⚠️ Για fine-tuning, θα χρειαστεί να έχετε διαθέσιμη μια κατάλληλη GPU - για παράδειγμα, A10, V100, A100.**

## 💾 Εγκατάσταση

Δημιουργήστε ένα νέο Python virtual περιβάλλον (για παράδειγμα, χρησιμοποιώντας `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Στη συνέχεια, εγκαταστήστε το Olive και τις εξαρτήσεις για το fine-tuning workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fine-tune Phi3 using Olive
Το [Olive configuration file](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) περιέχει ένα *workflow* με τις εξής *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Σε γενικές γραμμές, αυτό το workflow θα:

1. Κάνει fine-tune στο Phi3 (για 150 βήματα, που μπορείτε να αλλάξετε) χρησιμοποιώντας τα δεδομένα από το [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Συγχωνεύει τα βάρη του LoRA adapter στο βασικό μοντέλο. Αυτό θα σας δώσει ένα ενιαίο μοντέλο σε μορφή ONNX.
1. Το Model Builder θα βελτιστοποιήσει το μοντέλο για το ONNX runtime *και* θα το ποσοτικοποιήσει σε `int4`.

Για να εκτελέσετε το workflow, τρέξτε:

```bash
olive run --config phrase-classification.json
```

Όταν το Olive ολοκληρωθεί, το βελτιστοποιημένο `int4` fine-tuned μοντέλο Phi3 θα είναι διαθέσιμο στο: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Ενσωμάτωση του fine-tuned Phi3 στην εφαρμογή σας

Για να τρέξετε την εφαρμογή:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Η απάντηση θα είναι μία λέξη που ταξινομεί τη φράση (Sad/Joy/Fear/Surprise).

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική μετάφραση από άνθρωπο. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.