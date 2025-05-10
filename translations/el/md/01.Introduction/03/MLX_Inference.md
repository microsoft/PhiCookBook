<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dcb656f3d206fc4968e236deec5d4384",
  "translation_date": "2025-05-09T12:13:33+00:00",
  "source_file": "md/01.Introduction/03/MLX_Inference.md",
  "language_code": "el"
}
-->
# **Inference Phi-3 με το Apple MLX Framework**

## **Τι είναι το MLX Framework**

Το MLX είναι ένα πλαίσιο για μηχανική μάθηση σε Apple silicon, δημιουργημένο από την ομάδα έρευνας μηχανικής μάθησης της Apple.

Το MLX έχει σχεδιαστεί από ερευνητές μηχανικής μάθησης για ερευνητές μηχανικής μάθησης. Το πλαίσιο έχει ως στόχο να είναι φιλικό προς τον χρήστη, αλλά παράλληλα αποδοτικό για την εκπαίδευση και την ανάπτυξη μοντέλων. Ο σχεδιασμός του πλαισίου είναι επίσης απλός σε επίπεδο ιδεών. Σκοπός μας είναι να διευκολύνουμε τους ερευνητές να επεκτείνουν και να βελτιώσουν το MLX, ώστε να μπορούν γρήγορα να εξερευνήσουν νέες ιδέες.

Τα LLMs μπορούν να επιταχυνθούν σε συσκευές Apple Silicon μέσω του MLX, και τα μοντέλα μπορούν να τρέξουν τοπικά με μεγάλη ευκολία.

## **Χρήση του MLX για inference του Phi-3-mini**

### **1. Ρύθμιση του περιβάλλοντος MLX**

1. Python 3.11.x  
2. Εγκατάσταση της MLX Βιβλιοθήκης


```bash

pip install mlx-lm

```

### **2. Εκτέλεση του Phi-3-mini στο Terminal με MLX**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Το αποτέλεσμα (στο περιβάλλον μου Apple M1 Max, 64GB) είναι

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.el.png)

### **3. Ποσοτικοποίηση (Quantizing) του Phi-3-mini με MLX στο Terminal**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** Το μοντέλο μπορεί να ποσοτικοποιηθεί μέσω της mlx_lm.convert, και η προεπιλεγμένη ποσοτικοποίηση είναι INT4. Σε αυτό το παράδειγμα, το Phi-3-mini ποσοτικοποιείται σε INT4.

Το μοντέλο μπορεί να ποσοτικοποιηθεί μέσω της mlx_lm.convert, και η προεπιλεγμένη ποσοτικοποίηση είναι INT4. Σε αυτό το παράδειγμα ποσοτικοποιούμε το Phi-3-mini σε INT4. Μετά την ποσοτικοποίηση, το μοντέλο αποθηκεύεται στον προεπιλεγμένο φάκελο ./mlx_model

Μπορούμε να δοκιμάσουμε το ποσοτικοποιημένο μοντέλο με MLX από το terminal


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

Το αποτέλεσμα είναι

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.el.png)


### **4. Εκτέλεση του Phi-3-mini με MLX σε Jupyter Notebook**


![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.el.png)

***Note:*** Παρακαλώ διαβάστε το δείγμα [click this link](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **Πόροι**

1. Μάθετε για το Apple MLX Framework [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub Repo [https://github.com/ml-explore](https://github.com/ml-explore)

**Αποποίηση Ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική μετάφραση από ανθρώπους. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.