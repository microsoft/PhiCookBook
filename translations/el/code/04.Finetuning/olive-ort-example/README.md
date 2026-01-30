# Fine-tune το Phi3 χρησιμοποιώντας το Olive

Σε αυτό το παράδειγμα θα χρησιμοποιήσετε το Olive για να:

1. Fine-tune έναν LoRA adapter ώστε να ταξινομεί φράσεις σε Sad, Joy, Fear, Surprise.
1. Συγχωνεύσετε τα βάρη του adapter στο βασικό μοντέλο.
1. Βελτιστοποιήσετε και ποσοτικοποιήσετε το μοντέλο σε `int4`.

Επίσης, θα σας δείξουμε πώς να κάνετε inference στο fine-tuned μοντέλο χρησιμοποιώντας το ONNX Runtime (ORT) Generate API.

> **⚠️ Για Fine-tuning, θα χρειαστεί να έχετε διαθέσιμη μια κατάλληλη GPU - για παράδειγμα, A10, V100, A100.**

## 💾 Εγκατάσταση

Δημιουργήστε ένα νέο Python virtual περιβάλλον (για παράδειγμα, χρησιμοποιώντας `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Στη συνέχεια, εγκαταστήστε το Olive και τις εξαρτήσεις για μια ροή εργασίας fine-tuning:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Fine-tune το Phi3 χρησιμοποιώντας το Olive
Το [αρχείο ρύθμισης Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) περιέχει μια *ροή εργασίας* με τις εξής *διαδικασίες*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Σε γενικές γραμμές, αυτή η ροή εργασίας θα:

1. Κάνει fine-tune το Phi3 (για 150 βήματα, που μπορείτε να τροποποιήσετε) χρησιμοποιώντας τα δεδομένα από το [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Συγχωνεύει τα βάρη του LoRA adapter στο βασικό μοντέλο. Αυτό θα σας δώσει ένα ενιαίο μοντέλο σε μορφή ONNX.
1. Ο Model Builder θα βελτιστοποιήσει το μοντέλο για το ONNX runtime *και* θα το ποσοτικοποιήσει σε `int4`.

Για να εκτελέσετε τη ροή εργασίας, τρέξτε:

```bash
olive run --config phrase-classification.json
```

Όταν το Olive ολοκληρώσει, το βελτιστοποιημένο `int4` fine-tuned μοντέλο Phi3 θα είναι διαθέσιμο στο: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Ενσωματώστε το fine-tuned Phi3 στην εφαρμογή σας

Για να τρέξετε την εφαρμογή:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Η απάντηση θα πρέπει να είναι μια μονολεκτική ταξινόμηση της φράσης (Sad/Joy/Fear/Surprise).

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.