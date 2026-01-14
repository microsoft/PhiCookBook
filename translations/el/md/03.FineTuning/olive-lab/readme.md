<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6bbe47de3b974df7eea29dfeccf6032b",
  "translation_date": "2025-07-17T10:19:49+00:00",
  "source_file": "md/03.FineTuning/olive-lab/readme.md",
  "language_code": "el"
}
-->
# Εργαστήριο. Βελτιστοποίηση μοντέλων AI για εκτέλεση στη συσκευή

## Εισαγωγή

> [!IMPORTANT]  
> Αυτό το εργαστήριο απαιτεί **Nvidia A10 ή A100 GPU** με τους αντίστοιχους drivers και εγκατεστημένο το CUDA toolkit (έκδοση 12+).

> [!NOTE]  
> Πρόκειται για ένα εργαστήριο διάρκειας **35 λεπτών** που θα σας δώσει μια πρακτική εισαγωγή στις βασικές έννοιες της βελτιστοποίησης μοντέλων για εκτέλεση στη συσκευή χρησιμοποιώντας το OLIVE.

## Στόχοι Μάθησης

Στο τέλος αυτού του εργαστηρίου, θα μπορείτε να χρησιμοποιήσετε το OLIVE για να:

- Ποσοτικοποιήσετε ένα μοντέλο AI χρησιμοποιώντας τη μέθοδο ποσοτικοποίησης AWQ.  
- Κάνετε fine-tune ένα μοντέλο AI για μια συγκεκριμένη εργασία.  
- Δημιουργήσετε LoRA adapters (fine-tuned μοντέλο) για αποδοτική εκτέλεση στη συσκευή με το ONNX Runtime.

### Τι είναι το Olive

Το Olive (*O*NNX *live*) είναι ένα εργαλείο βελτιστοποίησης μοντέλων με συνοδευτικό CLI που σας επιτρέπει να παραδώσετε μοντέλα για το ONNX runtime +++https://onnxruntime.ai+++ με ποιότητα και απόδοση.

![Olive Flow](../../../../../translated_images/el/olive-flow.5daf97340275f8b6.png)

Η είσοδος στο Olive είναι συνήθως ένα μοντέλο PyTorch ή Hugging Face και η έξοδος είναι ένα βελτιστοποιημένο μοντέλο ONNX που εκτελείται σε μια συσκευή (στόχος ανάπτυξης) που τρέχει το ONNX runtime. Το Olive βελτιστοποιεί το μοντέλο για τον επιταχυντή AI του στόχου ανάπτυξης (NPU, GPU, CPU) που παρέχεται από κατασκευαστή υλικού όπως Qualcomm, AMD, Nvidia ή Intel.

Το Olive εκτελεί ένα *workflow*, που είναι μια διατεταγμένη ακολουθία μεμονωμένων εργασιών βελτιστοποίησης μοντέλου που ονομάζονται *passes* - παραδείγματα passes είναι: συμπίεση μοντέλου, καταγραφή γραφήματος, ποσοτικοποίηση, βελτιστοποίηση γραφήματος. Κάθε pass έχει ένα σύνολο παραμέτρων που μπορούν να ρυθμιστούν για να επιτευχθούν οι καλύτεροι μετρικοί δείκτες, όπως ακρίβεια και καθυστέρηση, οι οποίοι αξιολογούνται από τον αντίστοιχο αξιολογητή. Το Olive χρησιμοποιεί μια στρατηγική αναζήτησης που εφαρμόζει έναν αλγόριθμο αναζήτησης για να ρυθμίσει αυτόματα κάθε pass ένα προς ένα ή ένα σύνολο passes μαζί.

#### Οφέλη του Olive

- **Μειώνει την απογοήτευση και τον χρόνο** των πειραματισμών με δοκιμές και λάθη σε τεχνικές βελτιστοποίησης γραφήματος, συμπίεσης και ποσοτικοποίησης. Ορίστε τα όρια ποιότητας και απόδοσης και αφήστε το Olive να βρει αυτόματα το καλύτερο μοντέλο για εσάς.  
- **Πάνω από 40 ενσωματωμένα στοιχεία βελτιστοποίησης μοντέλων** που καλύπτουν σύγχρονες τεχνικές ποσοτικοποίησης, συμπίεσης, βελτιστοποίησης γραφήματος και fine-tuning.  
- **Εύχρηστο CLI** για κοινές εργασίες βελτιστοποίησης μοντέλων. Για παράδειγμα, olive quantize, olive auto-opt, olive finetune.  
- Ενσωματωμένη συσκευασία και ανάπτυξη μοντέλων.  
- Υποστηρίζει τη δημιουργία μοντέλων για **Multi LoRA serving**.  
- Δημιουργία workflows με YAML/JSON για τον συντονισμό εργασιών βελτιστοποίησης και ανάπτυξης μοντέλων.  
- Ενσωμάτωση με **Hugging Face** και **Azure AI**.  
- Ενσωματωμένος μηχανισμός **caching** για **εξοικονόμηση κόστους**.

## Οδηγίες Εργαστηρίου

> [!NOTE]  
> Βεβαιωθείτε ότι έχετε ρυθμίσει το Azure AI Hub και το Project σας και έχετε διαμορφώσει τον υπολογιστή A100 όπως στο Εργαστήριο 1.

### Βήμα 0: Σύνδεση με το Azure AI Compute

Θα συνδεθείτε στο Azure AI compute χρησιμοποιώντας τη λειτουργία απομακρυσμένης σύνδεσης στο **VS Code**.

1. Ανοίξτε την εφαρμογή **VS Code** στον υπολογιστή σας:  
2. Ανοίξτε την **παλέτα εντολών** με **Shift+Ctrl+P**  
3. Στην παλέτα εντολών αναζητήστε **AzureML - remote: Connect to compute instance in New Window**.  
4. Ακολουθήστε τις οδηγίες στην οθόνη για να συνδεθείτε στο Compute. Αυτό περιλαμβάνει την επιλογή της συνδρομής Azure, της Resource Group, του Project και του ονόματος Compute που έχετε ρυθμίσει στο Εργαστήριο 1.  
5. Μόλις συνδεθείτε στον κόμβο Azure ML Compute, αυτό θα εμφανιστεί κάτω αριστερά στο Visual Code ως `><Azure ML: Compute Name`

### Βήμα 1: Κλωνοποίηση αυτού του αποθετηρίου

Στο VS Code, ανοίξτε ένα νέο τερματικό με **Ctrl+J** και κλωνοποιήστε αυτό το αποθετήριο:

Στο τερματικό θα δείτε το prompt

```
azureuser@computername:~/cloudfiles/code$ 
```  
Κλωνοποιήστε τη λύση

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Βήμα 2: Άνοιγμα φακέλου στο VS Code

Για να ανοίξετε το VS Code στον σχετικό φάκελο, εκτελέστε την παρακάτω εντολή στο τερματικό, που θα ανοίξει ένα νέο παράθυρο:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Εναλλακτικά, μπορείτε να ανοίξετε το φάκελο επιλέγοντας **File** > **Open Folder**.

### Βήμα 3: Εξαρτήσεις

Ανοίξτε ένα τερματικό στο VS Code στην Azure AI Compute Instance σας (συντόμευση: **Ctrl+J**) και εκτελέστε τις παρακάτω εντολές για να εγκαταστήσετε τις εξαρτήσεις:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]  
> Η εγκατάσταση όλων των εξαρτήσεων θα διαρκέσει περίπου 5 λεπτά.

Σε αυτό το εργαστήριο θα κατεβάσετε και θα ανεβάσετε μοντέλα στον κατάλογο μοντέλων Azure AI. Για να έχετε πρόσβαση στον κατάλογο μοντέλων, πρέπει να κάνετε login στο Azure χρησιμοποιώντας:

```bash
az login
```

> [!NOTE]  
> Κατά τη σύνδεση θα σας ζητηθεί να επιλέξετε τη συνδρομή σας. Βεβαιωθείτε ότι έχετε ορίσει τη συνδρομή που παρέχεται για αυτό το εργαστήριο.

### Βήμα 4: Εκτέλεση εντολών Olive

Ανοίξτε ένα τερματικό στο VS Code στην Azure AI Compute Instance σας (συντόμευση: **Ctrl+J**) και βεβαιωθείτε ότι το περιβάλλον `olive-ai` είναι ενεργοποιημένο:

```bash
conda activate olive-ai
```

Στη συνέχεια, εκτελέστε τις παρακάτω εντολές Olive στη γραμμή εντολών.

1. **Επιθεώρηση των δεδομένων:** Σε αυτό το παράδειγμα, θα κάνετε fine-tune το μοντέλο Phi-3.5-Mini ώστε να εξειδικευτεί στην απάντηση ερωτήσεων σχετικών με ταξίδια. Ο παρακάτω κώδικας εμφανίζει τις πρώτες εγγραφές του dataset, που είναι σε μορφή JSON lines:

    ```bash
    head data/data_sample_travel.jsonl
    ```

1. **Ποσοτικοποίηση του μοντέλου:** Πριν την εκπαίδευση, ποσοτικοποιείτε το μοντέλο με την παρακάτω εντολή που χρησιμοποιεί μια τεχνική που ονομάζεται Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. Η AWQ ποσοτικοποιεί τα βάρη του μοντέλου λαμβάνοντας υπόψη τις ενεργοποιήσεις που παράγονται κατά την εκτέλεση. Αυτό σημαίνει ότι η διαδικασία ποσοτικοποίησης λαμβάνει υπόψη την πραγματική κατανομή των δεδομένων στις ενεργοποιήσεις, οδηγώντας σε καλύτερη διατήρηση της ακρίβειας του μοντέλου σε σύγκριση με τις παραδοσιακές μεθόδους ποσοτικοποίησης βαρών.

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```

    Η διαδικασία ποσοτικοποίησης AWQ διαρκεί περίπου **8 λεπτά** και θα **μειώσει το μέγεθος του μοντέλου από ~7.5GB σε ~2.5GB**.

    Σε αυτό το εργαστήριο, σας δείχνουμε πώς να εισάγετε μοντέλα από το Hugging Face (π.χ. `microsoft/Phi-3.5-mini-instruct`). Ωστόσο, το Olive επιτρέπει επίσης την εισαγωγή μοντέλων από τον κατάλογο Azure AI ενημερώνοντας το όρισμα `model_name_or_path` με ένα Azure AI asset ID (π.χ. `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`).

1. **Εκπαίδευση του μοντέλου:** Στη συνέχεια, η εντολή `olive finetune` κάνει fine-tune στο ποσοτικοποιημένο μοντέλο. Η ποσοτικοποίηση *πριν* το fine-tuning αντί για μετά δίνει καλύτερη ακρίβεια, καθώς η διαδικασία fine-tuning ανακτά μέρος της απώλειας από την ποσοτικοποίηση.

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```

    Η διαδικασία fine-tuning διαρκεί περίπου **6 λεπτά** (με 100 βήματα).

1. **Βελτιστοποίηση:** Μετά την εκπαίδευση, βελτιστοποιείτε το μοντέλο χρησιμοποιώντας την εντολή `auto-opt` του Olive, η οποία θα καταγράψει το γράφημα ONNX και θα εκτελέσει αυτόματα μια σειρά βελτιστοποιήσεων για να βελτιώσει την απόδοση του μοντέλου σε CPU, συμπιέζοντας το μοντέλο και κάνοντας fusion. Σημειώστε ότι μπορείτε να βελτιστοποιήσετε και για άλλες συσκευές όπως NPU ή GPU απλά ενημερώνοντας τα ορίσματα `--device` και `--provider` - αλλά για τους σκοπούς αυτού του εργαστηρίου θα χρησιμοποιήσουμε CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```

    Η βελτιστοποίηση διαρκεί περίπου **5 λεπτά**.

### Βήμα 5: Γρήγορος έλεγχος εκτέλεσης μοντέλου

Για να δοκιμάσετε την εκτέλεση του μοντέλου, δημιουργήστε ένα αρχείο Python στον φάκελό σας με όνομα **app.py** και αντιγράψτε-επικολλήστε τον παρακάτω κώδικα:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

Εκτελέστε τον κώδικα με:

```bash
python app.py
```

### Βήμα 6: Ανέβασμα μοντέλου στο Azure AI

Το ανέβασμα του μοντέλου σε αποθετήριο μοντέλων Azure AI το καθιστά διαθέσιμο σε άλλα μέλη της ομάδας ανάπτυξης και διαχειρίζεται τον έλεγχο εκδόσεων του μοντέλου. Για να ανεβάσετε το μοντέλο, εκτελέστε την παρακάτω εντολή:

> [!NOTE]  
> Ενημερώστε τα placeholders `{}` με το όνομα της resource group και του Azure AI Project σας.

Για να βρείτε το όνομα της resource group `"resourceGroup"` και του Azure AI Project, εκτελέστε την παρακάτω εντολή

```
az ml workspace show
```

Ή μεταβείτε στο +++ai.azure.com+++ και επιλέξτε **management center** > **project** > **overview**

Ενημερώστε τα placeholders `{}` με το όνομα της resource group και του Azure AI Project σας.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```

Στη συνέχεια, μπορείτε να δείτε το ανεβασμένο μοντέλο σας και να το αναπτύξετε στη διεύθυνση https://ml.azure.com/model/list

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.