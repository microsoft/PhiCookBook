<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4fe7f589d179be96a5577b0b8cba6aa",
  "translation_date": "2025-05-09T18:48:50+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/UsingPhi35TFLiteCreateAndroidApp.md",
  "language_code": "el"
}
-->
# **Χρήση του Microsoft Phi-3.5 tflite για δημιουργία εφαρμογής Android**

Αυτό είναι ένα δείγμα Android που χρησιμοποιεί τα μοντέλα Microsoft Phi-3.5 tflite.

## **📚 Γνώση**

Το Android LLM Inference API σας επιτρέπει να εκτελείτε μεγάλα γλωσσικά μοντέλα (LLMs) εντελώς στη συσκευή για εφαρμογές Android, τα οποία μπορείτε να χρησιμοποιήσετε για να εκτελέσετε μια μεγάλη γκάμα εργασιών, όπως δημιουργία κειμένου, ανάκτηση πληροφοριών σε φυσική γλώσσα και περίληψη εγγράφων. Η λειτουργία παρέχει ενσωματωμένη υποστήριξη για πολλαπλά μεγάλα γλωσσικά μοντέλα κειμένου-σε-κείμενο, ώστε να μπορείτε να εφαρμόσετε τα πιο πρόσφατα γενετικά μοντέλα AI στη συσκευή στις εφαρμογές Android σας.

Το Googld AI Edge Torch είναι μια βιβλιοθήκη Python που υποστηρίζει τη μετατροπή μοντέλων PyTorch σε μορφή .tflite, η οποία μπορεί στη συνέχεια να εκτελεστεί με TensorFlow Lite και MediaPipe. Αυτό επιτρέπει εφαρμογές για Android, iOS και IoT που μπορούν να τρέχουν μοντέλα πλήρως στη συσκευή. Το AI Edge Torch προσφέρει ευρεία υποστήριξη CPU, με αρχική υποστήριξη GPU και NPU. Το AI Edge Torch επιδιώκει στενή ενσωμάτωση με το PyTorch, βασιζόμενο στο torch.export() και παρέχοντας καλή κάλυψη των Core ATen operators.

## **🪬 Οδηγός**

### **🔥 Μετατροπή Microsoft Phi-3.5 σε υποστήριξη tflite**

0. Αυτό το δείγμα είναι για Android 14+

1. Εγκαταστήστε Python 3.10.12

***Πρόταση:*** χρησιμοποιήστε conda για να εγκαταστήσετε το περιβάλλον Python σας

2. Ubuntu 20.04 / 22.04 (παρακαλώ εστιάστε στο [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch))

***Πρόταση:*** Χρησιμοποιήστε Azure Linux VM ή κάποιο cloud vm τρίτου μέρους για να δημιουργήσετε το περιβάλλον σας

3. Μεταβείτε στο Linux bash σας, για να εγκαταστήσετε τη βιβλιοθήκη Python 

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. Κατεβάστε το Microsoft-3.5-Instruct από το Hugging face

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. Μετατρέψτε το Microsoft Phi-3.5 σε tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 Μετατροπή Microsoft Phi-3.5 σε Android Mediapipe Bundle**

παρακαλώ εγκαταστήστε πρώτα το mediapipe

```bash

pip install mediapipe

```

τρέξτε αυτόν τον κώδικα στο [notebook σας](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb)

```python

import mediapipe as mp
from mediapipe.tasks.python.genai import bundler

config = bundler.BundleConfig(
    tflite_model='Your Phi-3.5 tflite model path',
    tokenizer_model='Your Phi-3.5 tokenizer model path',
    start_token='start_token',
    stop_tokens=[STOP_TOKENS],
    output_filename='Your Phi-3.5 task model path',
    enable_bytes_to_unicode_mapping=True or Flase,
)
bundler.create_bundle(config)

```

### **🔥 Χρήση adb push για τοποθέτηση του μοντέλου task στη διαδρομή της συσκευής Android σας**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 Εκτέλεση του κώδικα Android σας**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.el.png)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η επίσημη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για οποιεσδήποτε παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.