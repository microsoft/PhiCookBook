<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:45:14+00:00",
  "source_file": "code/04.Finetuning/olive-ort-example/README.md",
  "language_code": "el"
}
-->
# Fine-tune Phi3 using Olive

Σε αυτό το παράδειγμα θα χρησιμοποιήσετε το Olive για να:

1. Κάνετε fine-tune έναν LoRA adapter ώστε να ταξινομεί φράσεις σε Sad, Joy, Fear, Surprise.
1. Συγχωνεύσετε τα βάρη του adapter στο βασικό μοντέλο.
1. Βελτιστοποιήσετε και ποσοτικοποιήσετε το μοντέλο σε `int4`.

Θα δείξουμε επίσης πώς να κάνετε inference στο fine-tuned μοντέλο χρησιμοποιώντας το ONNX Runtime (ORT) Generate API.

> **⚠️ Για το Fine-tuning, χρειάζεστε διαθέσιμη κατάλληλη GPU - για παράδειγμα, A10, V100, A100.**

## 💾 Εγκατάσταση

Δημιουργήστε ένα νέο Python virtual περιβάλλον (για παράδειγμα, χρησιμοποιώντας `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Στη συνέχεια, εγκαταστήστε το Olive και τις εξαρτήσεις για την ροή εργασίας fine-tuning:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fine-tune Phi3 χρησιμοποιώντας Olive
Το [Olive configuration file](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) περιέχει μια *workflow* με τις εξής *passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Σε γενικές γραμμές, αυτή η ροή εργασίας θα:

1. Κάνει fine-tune το Phi3 (για 150 βήματα, που μπορείτε να αλλάξετε) χρησιμοποιώντας τα δεδομένα από το [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Συγχωνεύσει τα βάρη του LoRA adapter στο βασικό μοντέλο. Αυτό θα δημιουργήσει ένα ενιαίο μοντέλο σε μορφή ONNX.
1. Ο Model Builder θα βελτιστοποιήσει το μοντέλο για το ONNX runtime *και* θα το ποσοτικοποιήσει σε `int4`.

Για να εκτελέσετε τη ροή εργασίας, τρέξτε:

```bash
olive run --config phrase-classification.json
```

Όταν το Olive ολοκληρώσει, το βελτιστοποιημένο και fine-tuned μοντέλο Phi3 σε `int4` είναι διαθέσιμο στο: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Ενσωματώστε το fine-tuned Phi3 στην εφαρμογή σας

Για να τρέξετε την εφαρμογή:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Η απάντηση θα πρέπει να είναι μια μονολεκτική ταξινόμηση της φράσης (Sad/Joy/Fear/Surprise).

**Αποποίηση Ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να λάβετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.