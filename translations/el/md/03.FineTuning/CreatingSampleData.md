<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3cd0b727945d57998f1096763df56a84",
  "translation_date": "2025-07-17T05:48:49+00:00",
  "source_file": "md/03.FineTuning/CreatingSampleData.md",
  "language_code": "el"
}
-->
# Δημιουργία Συνόλου Δεδομένων Εικόνων κατεβάζοντας το DataSet από το Hugging Face και τις αντίστοιχες εικόνες


### Επισκόπηση

Αυτό το σενάριο προετοιμάζει ένα σύνολο δεδομένων για μηχανική μάθηση κατεβάζοντας τις απαιτούμενες εικόνες, φιλτράροντας τις γραμμές όπου η λήψη εικόνων αποτυγχάνει, και αποθηκεύοντας το σύνολο δεδομένων ως αρχείο CSV.

### Προαπαιτούμενα

Πριν εκτελέσετε αυτό το σενάριο, βεβαιωθείτε ότι έχετε εγκαταστήσει τις ακόλουθες βιβλιοθήκες: `Pandas`, `Datasets`, `requests`, `PIL` και `io`. Θα χρειαστεί επίσης να αντικαταστήσετε το `'Insert_Your_Dataset'` στη γραμμή 2 με το όνομα του dataset σας από το Hugging Face.

Απαιτούμενες Βιβλιοθήκες:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Λειτουργικότητα

Το σενάριο εκτελεί τα εξής βήματα:

1. Κατεβάζει το dataset από το Hugging Face χρησιμοποιώντας τη συνάρτηση `load_dataset()`.
2. Μετατρέπει το dataset του Hugging Face σε Pandas DataFrame για ευκολότερη διαχείριση χρησιμοποιώντας τη μέθοδο `to_pandas()`.
3. Δημιουργεί φακέλους για την αποθήκευση του dataset και των εικόνων.
4. Φιλτράρει τις γραμμές όπου η λήψη εικόνας αποτυγχάνει, διατρέχοντας κάθε γραμμή του DataFrame, κατεβάζοντας την εικόνα με τη custom συνάρτηση `download_image()`, και προσθέτοντας τη φιλτραρισμένη γραμμή σε ένα νέο DataFrame με όνομα `filtered_rows`.
5. Δημιουργεί ένα νέο DataFrame με τις φιλτραρισμένες γραμμές και το αποθηκεύει στο δίσκο ως αρχείο CSV.
6. Εκτυπώνει μήνυμα που υποδεικνύει πού έχουν αποθηκευτεί το dataset και οι εικόνες.

### Προσαρμοσμένη Συνάρτηση

Η συνάρτηση `download_image()` κατεβάζει μια εικόνα από ένα URL και την αποθηκεύει τοπικά χρησιμοποιώντας τη βιβλιοθήκη Pillow (PIL) και το module `io`. Επιστρέφει True αν η εικόνα κατέβηκε επιτυχώς, και False σε αντίθετη περίπτωση. Η συνάρτηση επίσης πετάει εξαίρεση με το μήνυμα λάθους όταν η αίτηση αποτύχει.

### Πώς λειτουργεί

Η συνάρτηση download_image παίρνει δύο παραμέτρους: το image_url, που είναι το URL της εικόνας που θα κατέβει, και το save_path, που είναι η διαδρομή όπου θα αποθηκευτεί η εικόνα.

Ακολουθεί ο τρόπος λειτουργίας της συνάρτησης:

Ξεκινά κάνοντας ένα GET αίτημα στο image_url χρησιμοποιώντας τη μέθοδο requests.get. Αυτό ανακτά τα δεδομένα της εικόνας από το URL.

Η γραμμή response.raise_for_status() ελέγχει αν το αίτημα ήταν επιτυχές. Αν ο κωδικός κατάστασης της απόκρισης υποδεικνύει σφάλμα (π.χ. 404 - Δεν βρέθηκε), θα πετάξει εξαίρεση. Αυτό διασφαλίζει ότι προχωράμε στη λήψη της εικόνας μόνο αν το αίτημα ήταν επιτυχές.

Τα δεδομένα της εικόνας περνιούνται στη συνέχεια στη μέθοδο Image.open από το module PIL (Python Imaging Library). Αυτή η μέθοδος δημιουργεί ένα αντικείμενο Image από τα δεδομένα της εικόνας.

Η γραμμή image.save(save_path) αποθηκεύει την εικόνα στη συγκεκριμένη διαδρομή save_path. Η διαδρομή save_path πρέπει να περιλαμβάνει το επιθυμητό όνομα αρχείου και την επέκταση.

Τέλος, η συνάρτηση επιστρέφει True για να υποδείξει ότι η εικόνα κατέβηκε και αποθηκεύτηκε επιτυχώς. Αν προκύψει οποιαδήποτε εξαίρεση κατά τη διαδικασία, την πιάνει, εκτυπώνει μήνυμα λάθους που υποδεικνύει την αποτυχία, και επιστρέφει False.

Αυτή η συνάρτηση είναι χρήσιμη για τη λήψη εικόνων από URLs και την τοπική αποθήκευσή τους. Διαχειρίζεται πιθανά σφάλματα κατά τη διαδικασία λήψης και παρέχει ανατροφοδότηση για το αν η λήψη ήταν επιτυχής ή όχι.

Αξίζει να σημειωθεί ότι η βιβλιοθήκη requests χρησιμοποιείται για την εκτέλεση HTTP αιτημάτων, η βιβλιοθήκη PIL για την επεξεργασία εικόνων, και η κλάση BytesIO για τη διαχείριση των δεδομένων της εικόνας ως ροή bytes.



### Συμπέρασμα

Αυτό το σενάριο παρέχει έναν εύκολο τρόπο προετοιμασίας ενός συνόλου δεδομένων για μηχανική μάθηση, κατεβάζοντας τις απαιτούμενες εικόνες, φιλτράροντας τις γραμμές όπου η λήψη εικόνων αποτυγχάνει, και αποθηκεύοντας το dataset ως αρχείο CSV.

### Παράδειγμα Σεναρίου

```python
import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO

def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Check if the request was successful
        image = Image.open(BytesIO(response.content))
        image.save(save_path)
        return True
    except Exception as e:
        print(f"Failed to download {image_url}: {e}")
        return False


# Download the dataset from Hugging Face
dataset = load_dataset('Insert_Your_Dataset')


# Convert the Hugging Face dataset to a Pandas DataFrame
df = dataset['train'].to_pandas()


# Create directories to save the dataset and images
dataset_dir = './data/DataSetName'
images_dir = os.path.join(dataset_dir, 'images')
os.makedirs(images_dir, exist_ok=True)


# Filter out rows where image download fails
filtered_rows = []
for idx, row in df.iterrows():
    image_url = row['imageurl']
    image_name = f"{row['product_code']}.jpg"
    image_path = os.path.join(images_dir, image_name)
    if download_image(image_url, image_path):
        row['local_image_path'] = image_path
        filtered_rows.append(row)


# Create a new DataFrame with the filtered rows
filtered_df = pd.DataFrame(filtered_rows)


# Save the updated dataset to disk
dataset_path = os.path.join(dataset_dir, 'Dataset.csv')
filtered_df.to_csv(dataset_path, index=False)


print(f"Dataset and images saved to {dataset_dir}")
```

### Παράδειγμα Κώδικα Λήψης  
[Generate a new Data Set script](../../../../code/04.Finetuning/generate_dataset.py)

### Παράδειγμα Συνόλου Δεδομένων  
[Sample Data Set example from finetuning with LORA example](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.