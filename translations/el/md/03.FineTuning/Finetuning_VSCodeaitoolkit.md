<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2bc0950f44919ac75a88c1a871680c2",
  "translation_date": "2025-07-17T09:12:09+00:00",
  "source_file": "md/03.FineTuning/Finetuning_VSCodeaitoolkit.md",
  "language_code": "el"
}
-->
## Καλωσορίσατε στο AI Toolkit για το VS Code

Το [AI Toolkit για το VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) συγκεντρώνει διάφορα μοντέλα από το Azure AI Studio Catalog και άλλα καταλόγους όπως το Hugging Face. Το toolkit απλοποιεί τις κοινές εργασίες ανάπτυξης για τη δημιουργία εφαρμογών AI με εργαλεία και μοντέλα γεννητικής AI μέσω:
- Ξεκινήστε με την ανακάλυψη μοντέλων και το playground.
- Βελτιστοποίηση μοντέλων και εκτέλεση inference χρησιμοποιώντας τοπικούς υπολογιστικούς πόρους.
- Απομακρυσμένη βελτιστοποίηση και inference χρησιμοποιώντας πόρους Azure.

[Εγκαταστήστε το AI Toolkit για VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/el/Aitoolkit.7157953df04812dc.png)

**[Private Preview]** Παροχή με ένα κλικ για Azure Container Apps για εκτέλεση fine-tuning και inference μοντέλων στο cloud.

Ας ξεκινήσουμε την ανάπτυξη της AI εφαρμογής σας:

- [Καλωσορίσατε στο AI Toolkit για το VS Code](../../../../md/03.FineTuning)
- [Τοπική Ανάπτυξη](../../../../md/03.FineTuning)
  - [Προετοιμασίες](../../../../md/03.FineTuning)
  - [Ενεργοποίηση Conda](../../../../md/03.FineTuning)
  - [Μόνο fine-tuning βασικού μοντέλου](../../../../md/03.FineTuning)
  - [Fine-tuning και inference μοντέλου](../../../../md/03.FineTuning)
  - [Fine-tuning μοντέλου](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [Δείγματα και Πόροι Fine Tuning](../../../../md/03.FineTuning)
- [**\[Private Preview\]** Απομακρυσμένη Ανάπτυξη](../../../../md/03.FineTuning)
  - [Προαπαιτούμενα](../../../../md/03.FineTuning)
  - [Ρύθμιση Απομακρυσμένου Έργου Ανάπτυξης](../../../../md/03.FineTuning)
  - [Παροχή Πόρων Azure](../../../../md/03.FineTuning)
  - [\[Προαιρετικό\] Προσθήκη Huggingface Token στο Azure Container App Secret](../../../../md/03.FineTuning)
  - [Εκτέλεση Fine-tuning](../../../../md/03.FineTuning)
  - [Παροχή Endpoint Inference](../../../../md/03.FineTuning)
  - [Ανάπτυξη Endpoint Inference](../../../../md/03.FineTuning)
  - [Προχωρημένη χρήση](../../../../md/03.FineTuning)

## Τοπική Ανάπτυξη
### Προετοιμασίες

1. Βεβαιωθείτε ότι ο οδηγός NVIDIA είναι εγκατεστημένος στον υπολογιστή.
2. Εκτελέστε `huggingface-cli login`, αν χρησιμοποιείτε HF για αξιοποίηση dataset.
3. Επεξηγήσεις ρυθμίσεων κλειδιού `Olive` για οτιδήποτε επηρεάζει τη χρήση μνήμης.

### Ενεργοποίηση Conda
Επειδή χρησιμοποιούμε περιβάλλον WSL και είναι κοινόχρηστο, πρέπει να ενεργοποιήσετε χειροκίνητα το περιβάλλον conda. Μετά από αυτό το βήμα μπορείτε να τρέξετε fine-tuning ή inference.

```bash
conda activate [conda-env-name] 
```

### Μόνο fine-tuning βασικού μοντέλου
Για να δοκιμάσετε απλά το βασικό μοντέλο χωρίς fine-tuning, μπορείτε να εκτελέσετε αυτή την εντολή μετά την ενεργοποίηση του conda.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### Fine-tuning και inference μοντέλου

Μόλις ανοίξετε το workspace σε dev container, ανοίξτε ένα τερματικό (η προεπιλεγμένη διαδρομή είναι η ρίζα του έργου) και εκτελέστε την παρακάτω εντολή για fine-tuning ενός LLM στο επιλεγμένο dataset.

```bash
python finetuning/invoke_olive.py 
```

Τα checkpoints και το τελικό μοντέλο θα αποθηκευτούν στον φάκελο `models`.

Στη συνέχεια, εκτελέστε inference με το fine-tuned μοντέλο μέσω συνομιλιών σε `console`, `web browser` ή `prompt flow`.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

Για να χρησιμοποιήσετε το `prompt flow` στο VS Code, ανατρέξτε σε αυτό το [Quick Start](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

### Fine-tuning μοντέλου

Κατεβάστε το παρακάτω μοντέλο ανάλογα με τη διαθεσιμότητα GPU στη συσκευή σας.

Για να ξεκινήσετε την τοπική συνεδρία fine-tuning με χρήση QLoRA, επιλέξτε ένα μοντέλο από τον κατάλογό μας που θέλετε να βελτιστοποιήσετε.
| Πλατφόρμα(ες) | Διαθέσιμη GPU | Όνομα μοντέλου | Μέγεθος (GB) |
|---------|---------|--------|--------|
| Windows | Ναι | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | Ναι | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | Όχι | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_Σημείωση_** Δεν χρειάζεστε λογαριασμό Azure για να κατεβάσετε τα μοντέλα.

Το μοντέλο Phi3-mini (int4) έχει μέγεθος περίπου 2GB-3GB. Ανάλογα με την ταχύτητα του δικτύου σας, η λήψη μπορεί να διαρκέσει μερικά λεπτά.

Ξεκινήστε επιλέγοντας όνομα και τοποθεσία έργου.
Στη συνέχεια, επιλέξτε μοντέλο από τον κατάλογο μοντέλων. Θα σας ζητηθεί να κατεβάσετε το πρότυπο έργου. Μπορείτε μετά να πατήσετε "Configure Project" για να προσαρμόσετε διάφορες ρυθμίσεις.

### Microsoft Olive

Χρησιμοποιούμε το [Olive](https://microsoft.github.io/Olive/why-olive.html) για να τρέξουμε fine-tuning QLoRA σε PyTorch μοντέλο από τον κατάλογό μας. Όλες οι ρυθμίσεις είναι προκαθορισμένες με τις προεπιλεγμένες τιμές για βέλτιστη εκτέλεση της διαδικασίας fine-tuning τοπικά με βελτιστοποιημένη χρήση μνήμης, αλλά μπορούν να προσαρμοστούν ανάλογα με το σενάριό σας.

### Δείγματα και Πόροι Fine Tuning

- [Οδηγός Ξεκινήματος Fine tuning](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [Fine tuning με Dataset HuggingFace](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [Fine tuning με Απλό Dataset](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Private Preview]** Απομακρυσμένη Ανάπτυξη

### Προαπαιτούμενα

1. Για να τρέξετε fine-tuning μοντέλου στο απομακρυσμένο περιβάλλον Azure Container App, βεβαιωθείτε ότι η συνδρομή σας έχει επαρκή χωρητικότητα GPU. Υποβάλετε [ticket υποστήριξης](https://azure.microsoft.com/support/create-ticket/) για να ζητήσετε την απαιτούμενη χωρητικότητα για την εφαρμογή σας. [Περισσότερες πληροφορίες για χωρητικότητα GPU](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)
2. Αν χρησιμοποιείτε ιδιωτικό dataset στο HuggingFace, βεβαιωθείτε ότι έχετε [λογαριασμό HuggingFace](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) και [δημιουργήστε access token](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo)
3. Ενεργοποιήστε τη σημαία λειτουργίας Remote Fine-tuning και Inference στο AI Toolkit για VS Code
   1. Ανοίξτε τις Ρυθμίσεις του VS Code επιλέγοντας *File -> Preferences -> Settings*.
   2. Μεταβείτε στα *Extensions* και επιλέξτε *AI Toolkit*.
   3. Επιλέξτε την επιλογή *"Enable Remote Fine-tuning And Inference"*.
   4. Επανεκκινήστε το VS Code για να εφαρμοστούν οι αλλαγές.

- [Απομακρυσμένο Fine tuning](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### Ρύθμιση Απομακρυσμένου Έργου Ανάπτυξης
1. Εκτελέστε την παλέτα εντολών `AI Toolkit: Focus on Resource View`.
2. Μεταβείτε στο *Model Fine-tuning* για να έχετε πρόσβαση στον κατάλογο μοντέλων. Ονομάστε το έργο σας και επιλέξτε την τοποθεσία στον υπολογιστή σας. Στη συνέχεια, πατήστε το κουμπί *"Configure Project"*.
3. Ρύθμιση Έργου
    1. Αποφύγετε την ενεργοποίηση της επιλογής *"Fine-tune locally"*.
    2. Οι ρυθμίσεις Olive θα εμφανιστούν με προκαθορισμένες τιμές. Παρακαλούμε προσαρμόστε και συμπληρώστε τις ρυθμίσεις όπως απαιτείται.
    3. Προχωρήστε στο *Generate Project*. Αυτό το στάδιο χρησιμοποιεί WSL και περιλαμβάνει τη δημιουργία νέου περιβάλλοντος Conda, προετοιμάζοντας για μελλοντικές ενημερώσεις που θα περιλαμβάνουν Dev Containers.
4. Πατήστε *"Relaunch Window In Workspace"* για να ανοίξετε το απομακρυσμένο έργο ανάπτυξης.

> **Σημείωση:** Το έργο λειτουργεί είτε τοπικά είτε απομακρυσμένα μέσα στο AI Toolkit για VS Code. Αν επιλέξετε *"Fine-tune locally"* κατά τη δημιουργία έργου, θα λειτουργεί αποκλειστικά σε WSL χωρίς δυνατότητες απομακρυσμένης ανάπτυξης. Αν δεν ενεργοποιήσετε το *"Fine-tune locally"*, το έργο θα περιοριστεί στο απομακρυσμένο περιβάλλον Azure Container App.

### Παροχή Πόρων Azure
Για να ξεκινήσετε, πρέπει να παρέχετε τον πόρο Azure για απομακρυσμένο fine-tuning. Κάντε το εκτελώντας την εντολή `AI Toolkit: Provision Azure Container Apps job for fine-tuning` από την παλέτα εντολών.

Παρακολουθήστε την πρόοδο της παροχής μέσω του συνδέσμου που εμφανίζεται στο κανάλι εξόδου.

### [Προαιρετικό] Προσθήκη Huggingface Token στο Azure Container App Secret
Αν χρησιμοποιείτε ιδιωτικό dataset HuggingFace, ορίστε το token HuggingFace ως μεταβλητή περιβάλλοντος για να αποφύγετε την ανάγκη χειροκίνητης σύνδεσης στο Hugging Face Hub.
Μπορείτε να το κάνετε με την εντολή `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning`. Με αυτή την εντολή, ορίστε το όνομα του μυστικού ως [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) και χρησιμοποιήστε το token Hugging Face ως την τιμή του μυστικού.

### Εκτέλεση Fine-tuning
Για να ξεκινήσετε την απομακρυσμένη εργασία fine-tuning, εκτελέστε την εντολή `AI Toolkit: Run fine-tuning`.

Για να δείτε τα συστήματα και τα logs της κονσόλας, μπορείτε να επισκεφθείτε το Azure portal μέσω του συνδέσμου στο πάνελ εξόδου (περισσότερα βήματα στο [View and Query Logs on Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). Εναλλακτικά, μπορείτε να δείτε τα logs της κονσόλας απευθείας στο πάνελ εξόδου του VSCode εκτελώντας την εντολή `AI Toolkit: Show the running fine-tuning job streaming logs`.
> **Σημείωση:** Η εργασία μπορεί να είναι σε ουρά λόγω ανεπαρκών πόρων. Αν δεν εμφανίζονται τα logs, εκτελέστε την εντολή `AI Toolkit: Show the running fine-tuning job streaming logs`, περιμένετε λίγο και εκτελέστε ξανά την εντολή για να επανασυνδεθείτε στο streaming των logs.

Κατά τη διάρκεια αυτής της διαδικασίας, το QLoRA θα χρησιμοποιηθεί για fine-tuning και θα δημιουργήσει LoRA adapters για το μοντέλο που θα χρησιμοποιηθούν κατά το inference.
Τα αποτελέσματα του fine-tuning θα αποθηκευτούν στα Azure Files.

### Παροχή Endpoint Inference
Αφού εκπαιδευτούν οι adapters στο απομακρυσμένο περιβάλλον, χρησιμοποιήστε μια απλή εφαρμογή Gradio για να αλληλεπιδράσετε με το μοντέλο.
Παρόμοια με τη διαδικασία fine-tuning, πρέπει να ρυθμίσετε τους πόρους Azure για απομακρυσμένο inference εκτελώντας την εντολή `AI Toolkit: Provision Azure Container Apps for inference` από την παλέτα εντολών.

Κατά προεπιλογή, η συνδρομή και η ομάδα πόρων για το inference πρέπει να ταιριάζουν με αυτές που χρησιμοποιήθηκαν για το fine-tuning. Το inference θα χρησιμοποιήσει το ίδιο περιβάλλον Azure Container App και θα έχει πρόσβαση στο μοντέλο και τον adapter που αποθηκεύτηκαν στα Azure Files, τα οποία δημιουργήθηκαν κατά το βήμα fine-tuning.

### Ανάπτυξη Endpoint Inference
Αν θέλετε να τροποποιήσετε τον κώδικα inference ή να φορτώσετε ξανά το μοντέλο inference, εκτελέστε την εντολή `AI Toolkit: Deploy for inference`. Αυτό θα συγχρονίσει τον πιο πρόσφατο κώδικά σας με το Azure Container App και θα επανεκκινήσει το αντίγραφο.

Μόλις ολοκληρωθεί επιτυχώς η ανάπτυξη, μπορείτε να έχετε πρόσβαση στο API inference πατώντας το κουμπί "*Go to Inference Endpoint*" που εμφανίζεται στην ειδοποίηση του VSCode. Εναλλακτικά, το web API endpoint βρίσκεται στο `ACA_APP_ENDPOINT` στο αρχείο `./infra/inference.config.json` και στο πάνελ εξόδου. Τώρα είστε έτοιμοι να αξιολογήσετε το μοντέλο χρησιμοποιώντας αυτό το endpoint.

### Προχωρημένη χρήση
Για περισσότερες πληροφορίες σχετικά με την απομακρυσμένη ανάπτυξη με το AI Toolkit, ανατρέξτε στην τεκμηρίωση [Fine-Tuning models remotely](https://aka.ms/ai-toolkit/remote-provision) και [Inferencing with the fine-tuned model](https://aka.ms/ai-toolkit/remote-inference).

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.