## Πώς να χρησιμοποιήσετε τα components chat-completion από το σύστημα καταλόγου Azure ML για την προσαρμογή (fine tune) ενός μοντέλου

Σε αυτό το παράδειγμα θα κάνουμε fine tuning του μοντέλου Phi-3-mini-4k-instruct για να ολοκληρώσουμε μια συνομιλία μεταξύ 2 ατόμων χρησιμοποιώντας το dataset ultrachat_200k.

![MLFineTune](../../../../translated_images/el/MLFineTune.928d4c6b3767dd35.webp)

Το παράδειγμα θα σας δείξει πώς να κάνετε fine tuning χρησιμοποιώντας το Azure ML SDK και Python και στη συνέχεια να αναπτύξετε το fine tuned μοντέλο σε ένα online endpoint για πραγματικό χρόνο συμπερασμάτων.

### Δεδομένα εκπαίδευσης

Θα χρησιμοποιήσουμε το dataset ultrachat_200k. Πρόκειται για μια πολύ φιλτραρισμένη έκδοση του dataset UltraChat και χρησιμοποιήθηκε για την εκπαίδευση του Zephyr-7B-β, ενός state of the art 7b μοντέλου συνομιλίας.

### Μοντέλο

Θα χρησιμοποιήσουμε το μοντέλο Phi-3-mini-4k-instruct για να δείξουμε πώς μπορεί ο χρήστης να προσαρμόσει (finetune) ένα μοντέλο για εργασία ολοκλήρωσης συζήτησης (chat-completion). Αν ανοίξατε αυτό το σημειωματάριο από συγκεκριμένη κάρτα μοντέλου, θυμηθείτε να αντικαταστήσετε το συγκεκριμένο όνομα μοντέλου.

### Εργασίες

- Επιλογή μοντέλου προς προσαρμογή.
- Επιλογή και εξερεύνηση των δεδομένων εκπαίδευσης.
- Διαμόρφωση της εργασίας fine tuning.
- Εκτέλεση της εργασίας fine tuning.
- Επισκόπηση μετρικών εκπαίδευσης και αξιολόγησης.
- Καταχώριση του fine tuned μοντέλου.
- Ανάπτυξη του fine tuned μοντέλου για συμπεράσματα σε πραγματικό χρόνο.
- Καθαρισμός πόρων.

## 1. Ρύθμιση προαπαιτούμενων

- Εγκατάσταση εξαρτήσεων
- Σύνδεση με το AzureML Workspace. Μάθετε περισσότερα στο set up SDK authentication. Αντικαταστήστε τα <WORKSPACE_NAME>, <RESOURCE_GROUP> και <SUBSCRIPTION_ID> παρακάτω.
- Σύνδεση με το σύστημα καταλόγου azureml
- Ορισμός προαιρετικού ονόματος πειράματος
- Έλεγχος ή δημιουργία υπολογιστικού πόρου.

> [!NOTE]
> Απαιτείται ένας κόμβος GPU που μπορεί να έχει πολλαπλές κάρτες GPU. Για παράδειγμα, σε έναν κόμβο Standard_NC24rs_v3 υπάρχουν 4 GPU NVIDIA V100 ενώ σε Standard_NC12s_v3, υπάρχουν 2 GPU NVIDIA V100. Ανατρέξτε στην τεκμηρίωση για αυτές τις πληροφορίες. Ο αριθμός των καρτών GPU ανά κόμβο ορίζεται στην παράμετρο gpus_per_node παρακάτω. Η σωστή ρύθμιση αυτής της τιμής εξασφαλίζει αξιοποίηση όλων των GPUs στον κόμβο. Οι προτεινόμενοι τύποι υπολογιστικής GPU μπορούν να βρεθούν εδώ και εδώ.

### Βιβλιοθήκες Python

Εγκαταστήστε τις εξαρτήσεις εκτελώντας το παρακάτω κελί. Αυτό δεν είναι προαιρετικό αν τρέχετε σε νέο περιβάλλον.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Αλληλεπίδραση με Azure ML

1. Αυτό το Python script χρησιμοποιείται για αλληλεπίδραση με την υπηρεσία Azure Machine Learning (Azure ML). Ακολουθεί η ανάλυση των βημάτων του:

    - Εισάγει τα απαραίτητα modules από τα πακέτα azure.ai.ml, azure.identity, και azure.ai.ml.entities. Επίσης εισάγει το module time.

    - Προσπαθεί να πιστοποιηθεί χρησιμοποιώντας το DefaultAzureCredential(), το οποίο παρέχει μια απλοποιημένη εμπειρία πιστοποίησης για ταχύ ξεκίνημα ανάπτυξης εφαρμογών που λειτουργούν στο Azure cloud. Αν αποτύχει, επιστρέφει στην InteractiveBrowserCredential(), που παρέχει ένα διαδραστικό παράθυρο σύνδεσης.

    - Στη συνέχεια επιχειρεί να δημιουργήσει ένα instance του MLClient με τη μέθοδο from_config, που διαβάζει τη ρύθμιση από το προεπιλεγμένο αρχείο ρύθμισης (config.json). Αν αποτύχει, δημιουργεί το MLClient παρέχοντας χειροκίνητα τα subscription_id, resource_group_name και workspace_name.

    - Δημιουργεί ένα ακόμα MLClient instance, αυτή τη φορά για το Azure ML registry με όνομα "azureml". Αυτός ο κατάλογος είναι ο τόπος αποθήκευσης μοντέλων, pipeline fine-tuning και περιβαλλόντων.

    - Ορίζει το όνομα του πειράματος ως "chat_completion_Phi-3-mini-4k-instruct".

    - Δημιουργεί ένα μοναδικό timestamp μετατρέποντας τον τρέχοντα χρόνο (σε δευτερόλεπτα από την εποχή, ως αριθμό κινητής υποδιαστολής) σε ακέραιο και κατόπιν σε συμβολοσειρά. Αυτό το timestamp μπορεί να χρησιμοποιηθεί για τη δημιουργία μοναδικών ονομάτων και εκδόσεων.

    ```python
    # Εισαγωγή των απαραίτητων μονάδων από το Azure ML και το Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Εισαγωγή της μονάδας χρόνου
    
    # Προσπάθεια αυθεντικοποίησης με χρήση του DefaultAzureCredential
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # Αν αποτύχει το DefaultAzureCredential, χρήση του InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Προσπάθεια δημιουργίας στιγμιότυπου MLClient χρησιμοποιώντας το προεπιλεγμένο αρχείο ρυθμίσεων
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # Αν αποτύχει, δημιουργία στιγμιότυπου MLClient παρέχοντας χειροκίνητα τα στοιχεία
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Δημιουργία άλλου στιγμιότυπου MLClient για το μητρώο Azure ML με όνομα "azureml"
    # Αυτό το μητρώο είναι όπου αποθηκεύονται τα μοντέλα, τα pipelines βελτιστοποίησης και τα περιβάλλοντα
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Ορισμός του ονόματος του πειράματος
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Δημιουργία μοναδικής χρονικής σήμανσης που μπορεί να χρησιμοποιηθεί για ονόματα και εκδόσεις που πρέπει να είναι μοναδικές
    timestamp = str(int(time.time()))
    ```

## 2. Επιλογή μοντέλου βάσης για fine tuning

1. Το Phi-3-mini-4k-instruct είναι ένα μοντέλο 3.8 δισεκατομμυρίων παραμέτρων, ελαφρύ, state-of-the-art ανοιχτό μοντέλο, βασισμένο σε datasets που χρησιμοποιήθηκαν για το Phi-2. Το μοντέλο ανήκει στην οικογένεια μοντέλων Phi-3, και η έκδοση Mini κυκλοφορεί σε δύο παραλλαγές 4K και 128K που αντιστοιχούν στο μήκος του context (σε tokens) που μπορεί να υποστηρίξει. Πρέπει να προσαρμόσουμε (finetune) το μοντέλο για τον συγκεκριμένο σκοπό μας προκειμένου να το χρησιμοποιήσουμε. Μπορείτε να περιηγηθείτε σε αυτά τα μοντέλα στο Κατάλογο Μοντέλων (Model Catalog) στο AzureML Studio, φιλτράροντας ανά εργασία chat-completion. Σε αυτό το παράδειγμα χρησιμοποιούμε το μοντέλο Phi-3-mini-4k-instruct. Αν έχετε ανοίξει αυτό το σημειωματάριο για διαφορετικό μοντέλο, αντικαταστήστε το όνομα και την έκδοση του μοντέλου αναλόγως.

> [!NOTE]
> το id του μοντέλου. Αυτό θα περαστεί ως είσοδος στην εργασία fine tuning. Είναι επίσης διαθέσιμο ως πεδίο Asset ID στη σελίδα λεπτομερειών μοντέλου στον Κατάλογο Μοντέλων AzureML Studio.

2. Αυτό το Python script αλληλεπιδρά με την υπηρεσία Azure Machine Learning (Azure ML). Ακολουθεί η ανάλυση των βημάτων του:

    - Ορίζει το model_name ως "Phi-3-mini-4k-instruct".

    - Χρησιμοποιεί τη μέθοδο get της ιδιότητας models του αντικειμένου registry_ml_client για να ανακτήσει την τελευταία έκδοση του μοντέλου με το συγκεκριμένο όνομα από το Azure ML registry. Η μέθοδος get καλείται με δύο ορίσματα: το όνομα του μοντέλου και μια ετικέτα που δηλώνει ότι θα ληφθεί η τελευταία έκδοση.

    - Εκτυπώνει ένα μήνυμα στην κονσόλα που ενημερώνει το όνομα, την έκδοση και το id του μοντέλου που θα χρησιμοποιηθεί για το fine-tuning. Η μέθοδος format της συμβολοσειράς χρησιμοποιείται για να εισάγει το όνομα, την έκδοση και το id του μοντέλου στο μήνυμα. Τα ονόματα, οι εκδόσεις και τα ids του μοντέλου προσεγγίζονται ως ιδιότητες του αντικειμένου foundation_model.

    ```python
    # Ορισμός του ονόματος του μοντέλου
    model_name = "Phi-3-mini-4k-instruct"
    
    # Λήψη της πιο πρόσφατης έκδοσης του μοντέλου από το μητρώο Azure ML
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Εκτύπωση του ονόματος, της έκδοσης και του αναγνωριστικού του μοντέλου
    # Αυτές οι πληροφορίες είναι χρήσιμες για παρακολούθηση και αποσφαλμάτωση
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```

## 3. Δημιουργία υπολογιστικού πόρου για χρήση με την εργασία

Η εργασία fine tune λειτουργεί ΜΟΝΟ με υπολογιστική ισχύ GPU. Το μέγεθος του υπολογιστικού πόρου εξαρτάται από το πόσο μεγάλο είναι το μοντέλο και στις περισσότερες περιπτώσεις είναι δύσκολο να βρεθεί το κατάλληλο μέγεθος υπολογιστικού πόρου. Σε αυτό το κελί, καθοδηγούμε τον χρήστη να επιλέξει το σωστό υπολογιστικό πόρο για την εργασία.

> [!NOTE]
> Οι παρακάτω υπολογιστικές μονάδες λειτουργούν με την πιο βελτιστοποιημένη διαμόρφωση. Οποιαδήποτε αλλαγή στη διαμόρφωση μπορεί να οδηγήσει σε σφάλμα Cuda Out Of Memory. Σε τέτοια περίπτωση, δοκιμάστε να αναβαθμίσετε τον υπολογιστικό πόρο σε μεγαλύτερο μέγεθος.

> [!NOTE]
> Κατά την επιλογή του compute_cluster_size παρακάτω, βεβαιωθείτε ότι ο υπολογιστικός πόρος είναι διαθέσιμος στο resource group σας. Αν κάποιος υπολογιστικός πόρος δεν είναι διαθέσιμος, μπορείτε να υποβάλετε αίτηση για πρόσβαση στους υπολογιστικούς πόρους.

### Έλεγχος αν το μοντέλο υποστηρίζει Fine Tuning

1. Αυτό το Python script αλληλεπιδρά με ένα μοντέλο Azure Machine Learning (Azure ML). Ακολουθεί η ανάλυση των βημάτων του:

    - Εισάγει το module ast, που παρέχει λειτουργίες για επεξεργασία δέντρων σύνταξης Python.

    - Ελέγχει αν το αντικείμενο foundation_model (που αναπαριστά ένα μοντέλο στο Azure ML) έχει μια ετικέτα (tag) με όνομα finetune_compute_allow_list. Οι ετικέτες στο Azure ML είναι ζεύγη κλειδιού-τιμής που μπορείτε να δημιουργήσετε και να χρησιμοποιήσετε για φιλτράρισμα και ταξινόμηση μοντέλων.

    - Αν υπάρχει η ετικέτα finetune_compute_allow_list, χρησιμοποιεί τη λειτουργία ast.literal_eval για να αναλύσει με ασφάλεια την τιμή της ετικέτας (μια συμβολοσειρά) σε λίστα Python. Αυτή η λίστα ανατίθεται στη μεταβλητή computes_allow_list. Κατόπιν εκτυπώνει μήνυμα που υποδεικνύει ότι πρέπει να δημιουργηθεί υπολογιστικός πόρος από τη λίστα.

    - Αν δεν υπάρχει η ετικέτα finetune_compute_allow_list, θέτει την computes_allow_list σε None και εμφανίζει μήνυμα που δηλώνει ότι η ετικέτα δεν ανήκει στις ετικέτες του μοντέλου.

    - Συνοπτικά, το script ελέγχει για συγκεκριμένη ετικέτα στα μεταδεδομένα του μοντέλου, μετατρέπει την τιμή της σε λίστα αν υπάρχει και δίνει ενημερωτικά μηνύματα στον χρήστη.

    ```python
    # Εισαγωγή του module ast, που παρέχει συναρτήσεις για την επεξεργασία δέντρων της αφηρημένης σύνταξης της Python
    import ast
    
    # Έλεγχος αν η ετικέτα 'finetune_compute_allow_list' υπάρχει στις ετικέτες του μοντέλου
    if "finetune_compute_allow_list" in foundation_model.tags:
        # Αν η ετικέτα υπάρχει, χρήση του ast.literal_eval για ασφαλή ανάλυση της τιμής της ετικέτας (μιας συμβολοσειράς) σε λίστα Python
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # μετατροπή συμβολοσειράς σε λίστα Python
        # Εκτύπωση μηνύματος που δείχνει ότι πρέπει να δημιουργηθεί ένας υπολογιστής από τη λίστα
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Αν η ετικέτα δεν υπάρχει, ορισμός του computes_allow_list ως None
        computes_allow_list = None
        # Εκτύπωση μηνύματος που δείχνει ότι η ετικέτα 'finetune_compute_allow_list' δεν είναι μέρος των ετικετών του μοντέλου
        print("`finetune_compute_allow_list` is not part of model tags")
    ```

### Έλεγχος της Compute Instance

1. Αυτό το Python script αλληλεπιδρά με την υπηρεσία Azure Machine Learning (Azure ML) και πραγματοποιεί ελέγχους σε μια υπολογιστική μονάδα. Ακολουθεί η ανάλυση των βημάτων του:

    - Προσπαθεί να ανακτήσει την υπολογιστική μονάδα με το όνομα που είναι αποθηκευμένο στο compute_cluster από το Azure ML workspace. Αν η κατάσταση παροχής της υπολογιστικής μονάδας (provisioning state) είναι "failed", προκαλεί σφάλμα ValueError.

    - Ελέγχει αν το computes_allow_list δεν είναι None. Αν δεν είναι, μετατρέπει όλα τα μεγέθη υπολογιστικού πόρου στη λίστα σε πεζούς χαρακτήρες και ελέγχει αν το μέγεθος της τρέχουσας υπολογιστικής μονάδας είναι στη λίστα. Αν όχι, προκαλεί ValueError.

    - Αν η computes_allow_list είναι None, ελέγχει αν το μέγεθος της υπολογιστικής μονάδας είναι σε λίστα με μη υποστηριζόμενα μεγέθη VM GPU. Αν είναι, προκαλεί ValueError.

    - Ανακτά τη λίστα όλων των διαθέσιμων μεγεθών υπολογιστικών πόρων στο workspace. Στη συνέχεια, επαναλαμβάνει τη λίστα, και για κάθε μέγεθος ελέγχει αν το όνομά του ταιριάζει με το μέγεθος της τρέχουσας υπολογιστικής μονάδας. Αν ναι, ανακτά τον αριθμό των GPUs για αυτό το μέγεθος υπολογιστικού πόρου και θέτει gpu_count_found σε True.

    - Αν το gpu_count_found είναι True, εκτυπώνει τον αριθμό των GPUs στην υπολογιστική μονάδα. Αν όχι, προκαλεί ValueError.

    - Συνοπτικά, το script εκτελεί αρκετούς ελέγχους σε μια υπολογιστική μονάδα σε ένα Azure ML workspace, συμπεριλαμβανομένων ελέγχου της κατάστασης παροχής, του μεγέθους της έναντι λίστας αποδεκτών ή μη μέγεθος και του αριθμού των GPUs που διαθέτει.

    ```python
    # Εκτύπωση του μηνύματος εξαίρεσης
    print(e)
    # Υψώστε έναν ValueError αν το μέγεθος υπολογισμού δεν είναι διαθέσιμο στον χώρο εργασίας
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Ανάκτηση της παρουσίας υπολογισμού από τον χώρο εργασίας Azure ML
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Ελέγξτε αν η κατάσταση παροχής της παρουσίας υπολογισμού είναι "αποτυχία"
    if compute.provisioning_state.lower() == "failed":
        # Υψώστε έναν ValueError αν η κατάσταση παροχής είναι "αποτυχία"
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Ελέγξτε αν το computes_allow_list δεν είναι None
    if computes_allow_list is not None:
        # Μετατρέψτε όλα τα μεγέθη υπολογισμού στο computes_allow_list σε πεζά
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Ελέγξτε αν το μέγεθος της παρουσίας υπολογισμού είναι στη computes_allow_list_lower_case
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Υψώστε έναν ValueError αν το μέγεθος της παρουσίας υπολογισμού δεν είναι στη computes_allow_list_lower_case
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Ορίστε μια λίστα με μη υποστηριζόμενα μεγέθη GPU VM
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Ελέγξτε αν το μέγεθος της παρουσίας υπολογισμού είναι στη μη υποστηριζόμενη λίστα gpu_vm
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Υψώστε έναν ValueError αν το μέγεθος της παρουσίας υπολογισμού είναι στη μη υποστηριζόμενη λίστα gpu_vm
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Αρχικοποιήστε μια σημαία για να ελέγξετε αν έχει βρεθεί ο αριθμός των GPUs στην παρουσία υπολογισμού
    gpu_count_found = False
    # Ανακτήστε μια λίστα με όλα τα διαθέσιμα μεγέθη υπολογισμού στον χώρο εργασίας
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Διατρέξτε τη λίστα με τα διαθέσιμα μεγέθη υπολογισμού
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Ελέγξτε αν το όνομα του μεγέθους υπολογισμού ταιριάζει με το μέγεθος της παρουσίας υπολογισμού
        if compute_sku.name.lower() == compute.size.lower():
            # Αν ναι, ανακτήστε τον αριθμό των GPUs για εκείνο το μέγεθος υπολογισμού και ορίστε το gpu_count_found σε True
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # Αν το gpu_count_found είναι True, εκτυπώστε τον αριθμό των GPUs στην παρουσία υπολογισμού
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # Αν το gpu_count_found είναι False, υψώστε έναν ValueError
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```

## 4. Επιλογή dataset για fine tuning του μοντέλου

1. Χρησιμοποιούμε το dataset ultrachat_200k. Το dataset έχει τέσσερις διαχωρισμούς, κατάλληλους για Επιβλεπόμενο fine tuning (supervised fine-tuning, sft).
Generation ranking (gen). Ο αριθμός παραδειγμάτων ανά διαχωρισμό φαίνεται παρακάτω:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. Τα επόμενα κελιά δείχνουν βασική προετοιμασία δεδομένων για fine tuning:

### Οπτικοποίηση μερικών γραμμών δεδομένων

Θέλουμε αυτό το δείγμα να τρέξει γρήγορα, οπότε αποθηκεύουμε τα αρχεία train_sft, test_sft που περιέχουν το 5% των ήδη περικομμένων γραμμών. Αυτό σημαίνει ότι το fine tuned μοντέλο θα έχει χαμηλότερη ακρίβεια, συνεπώς δεν θα πρέπει να χρησιμοποιηθεί σε πραγματική χρήση.
Το download-dataset.py χρησιμοποιείται για τη λήψη του dataset ultrachat_200k και τη μετατροπή του dataset σε μορφή κατανάλωσης για το pipeline fine tuning. Επίσης, καθώς το dataset είναι μεγάλο, εδώ έχουμε μόνο μέρος του.

1. Εκτέλεση του script παρακάτω κατεβάζει μόνο το 5% των δεδομένων. Αυτό μπορεί να αυξηθεί αλλάζοντας την παράμετρο dataset_split_pc στο επιθυμητό ποσοστό.

> [!NOTE]
> Ορισμένα μοντέλα γλώσσας έχουν διαφορετικούς κωδικούς γλώσσας και γι' αυτό τα ονόματα στηλών στο dataset πρέπει να αντανακλούν τα ίδια.

1. Παράδειγμα της μορφής των δεδομένων
Το dataset chat-completion αποθηκεύεται σε μορφή parquet με κάθε εγγραφή να χρησιμοποιεί το παρακάτω σχήμα:

    - Πρόκειται για έγγραφο JSON (JavaScript Object Notation), που είναι μια δημοφιλής μορφή ανταλλαγής δεδομένων. Δεν είναι εκτελέσιμος κώδικας, αλλά ένας τρόπος αποθήκευσης και μεταφοράς δεδομένων. Δείτε τη δομή του:

    - "prompt": Αυτό το κλειδί κρατά μια συμβολοσειρά που αναπαριστά μια εργασία ή ερώτηση προς έναν AI βοηθό.

    - "messages": Αυτό το κλειδί κρατά έναν πίνακα αντικειμένων. Κάθε αντικείμενο αναπαριστά ένα μήνυμα σε συνομιλία μεταξύ χρήστη και AI βοηθού. Κάθε μήνυμα έχει δύο κλειδιά:

    - "content": Κρατά μια συμβολοσειρά που είναι το περιεχόμενο του μηνύματος.
    - "role": Κρατά μια συμβολοσειρά που δηλώνει το ρόλο του οντός που έστειλε το μήνυμα. Μπορεί να είναι "user" ή "assistant".
    - "prompt_id": Κρατά μια συμβολοσειρά που είναι ένας μοναδικός αναγνωριστικός κωδικός για το prompt.

1. Σε αυτό το συγκεκριμένο έγγραφο JSON, αναπαρίσταται μια συνομιλία όπου ένας χρήστης ζητά από ένα AI βοηθό να δημιουργήσει έναν πρωταγωνιστή για μια δυστοπική ιστορία. Ο βοηθός απαντά, και ο χρήστης ζητά περισσότερες λεπτομέρειες. Ο βοηθός συμφωνεί να δώσει περισσότερες λεπτομέρειες. Ολόκληρη η συνομιλία συνδέεται με συγκεκριμένο prompt id.

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```

### Λήψη δεδομένων

1. Αυτό το Python script χρησιμοποιείται για τη λήψη ενός dataset χρησιμοποιώντας ένα βοηθητικό script ονόματι download-dataset.py. Ακολουθεί η ανάλυση των βημάτων:

    - Εισάγει το module os, που παρέχει φορητούς τρόπους χρήσης λειτουργιών λειτουργικού συστήματος.

    - Χρησιμοποιεί τη συνάρτηση os.system για να τρέξει το script download-dataset.py στο shell με συγκεκριμένα ορίσματα γραμμής εντολών. Τα ορίσματα καθορίζουν το dataset προς λήψη (HuggingFaceH4/ultrachat_200k), τον κατάλογο προορισμού της λήψης (ultrachat_200k_dataset), και το ποσοστό του dataset για διαχωρισμό (5). Η os.system επιστρέφει τον κωδικό εξόδου της εντολής, που αποθηκεύεται στη μεταβλητή exit_status.

    - Ελέγχει αν exit_status δεν είναι 0. Σε συστήματα τύπου Unix, ο κωδικός εξόδου 0 σημαίνει επιτυχία, ενώ οποιοσδήποτε άλλος αριθμός σφάλμα. Αν το exit_status δεν είναι 0, προκαλεί εξαίρεση (Exception) με μήνυμα ότι υπήρξε σφάλμα κατά τη λήψη του dataset.

    - Συνοπτικά, το script εκτελεί εντολή λήψης dataset μέσω βοηθητικού script και προκαλεί εξαίρεση αν η εντολή αποτύχει.

    ```python
    # Εισαγωγή του module os, το οποίο παρέχει έναν τρόπο χρήσης λειτουργικότητας που εξαρτάται από το λειτουργικό σύστημα
    import os
    
    # Χρησιμοποιήστε τη συνάρτηση os.system για να εκτελέσετε το script download-dataset.py στο shell με συγκεκριμένα ορίσματα γραμμής εντολών
    # Τα ορίσματα καθορίζουν το σύνολο δεδομένων που θα κατέβει (HuggingFaceH4/ultrachat_200k), τον φάκελο στον οποίο θα αποθηκευτεί (ultrachat_200k_dataset) και το ποσοστό του συνόλου δεδομένων για διαίρεση (5)
    # Η συνάρτηση os.system επιστρέφει την κατάσταση εξόδου της εντολής που εκτέλεσε· αυτή η κατάσταση αποθηκεύεται στη μεταβλητή exit_status
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Ελέγξτε αν η exit_status δεν είναι 0
    # Σε λειτουργικά συστήματα τύπου Unix, η κατάσταση εξόδου 0 συνήθως υποδεικνύει ότι μια εντολή εκτελέστηκε με επιτυχία, ενώ οποιοσδήποτε άλλος αριθμός υποδηλώνει σφάλμα
    # Εάν η exit_status δεν είναι 0, προκαλέστε εξαίρεση (Exception) με μήνυμα που υποδεικνύει ότι υπήρξε σφάλμα κατά τη λήψη του συνόλου δεδομένων
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```

### Φόρτωση δεδομένων σε DataFrame

1. Αυτό το Python script φορτώνει ένα αρχείο JSON Lines σε ένα pandas DataFrame και εμφανίζει τις πρώτες 5 γραμμές. Ακολουθεί η ανάλυση των βημάτων του:

    - Εισάγει τη βιβλιοθήκη pandas, που είναι μια ισχυρή βιβλιοθήκη για χειρισμό και ανάλυση δεδομένων.

    - Ορίζει το μέγιστο πλάτος στήλης για τις επιλογές εμφάνισης του pandas σε 0. Αυτό σημαίνει ότι το πλήρες κείμενο κάθε στήλης θα εμφανίζεται ατελείωτα χωρίς περικοπή κατά την εκτύπωση του DataFrame.
    - Χρησιμοποιεί τη συνάρτηση pd.read_json για να φορτώσει το αρχείο train_sft.jsonl από τον κατάλογο ultrachat_200k_dataset σε ένα DataFrame. Το όρισμα lines=True υποδεικνύει ότι το αρχείο είναι σε μορφή JSON Lines, όπου κάθε γραμμή είναι ένα ξεχωριστό αντικείμενο JSON.

    - Χρησιμοποιεί τη μέθοδο head για να εμφανίσει τις πρώτες 5 γραμμές του DataFrame. Αν το DataFrame έχει λιγότερες από 5 γραμμές, θα εμφανίσει όλες αυτές.

    - Συνοπτικά, αυτό το σενάριο φορτώνει ένα αρχείο JSON Lines σε ένα DataFrame και εμφανίζει τις πρώτες 5 γραμμές με πλήρες κείμενο στηλών.
    
    ```python
    # Εισάγετε τη βιβλιοθήκη pandas, η οποία είναι μια ισχυρή βιβλιοθήκη για χειρισμό και ανάλυση δεδομένων
    import pandas as pd
    
    # Ορίστε το μέγιστο πλάτος στήλης για τις επιλογές εμφάνισης του pandas στο 0
    # Αυτό σημαίνει ότι θα εμφανίζεται ο πλήρης κείμενος κάθε στήλης χωρίς περικοπή όταν εκτυπώνεται το DataFrame
    pd.set_option("display.max_colwidth", 0)
    
    # Χρησιμοποιήστε τη συνάρτηση pd.read_json για να φορτώσετε το αρχείο train_sft.jsonl από τον κατάλογο ultrachat_200k_dataset σε ένα DataFrame
    # Το όρισμα lines=True υποδηλώνει ότι το αρχείο είναι σε μορφή JSON Lines, όπου κάθε γραμμή είναι ένα ξεχωριστό αντικείμενο JSON
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Χρησιμοποιήστε τη μέθοδο head για να εμφανίσετε τις πρώτες 5 γραμμές του DataFrame
    # Εάν το DataFrame έχει λιγότερες από 5 γραμμές, θα εμφανίσει όλες αυτές
    df.head()
    ```

## 5. Υποβολή της εργασίας σχολαστικής ρύθμισης χρησιμοποιώντας το μοντέλο και τα δεδομένα ως εισόδους

Δημιουργήστε την εργασία που χρησιμοποιεί το συστατικό pipeline chat-completion. Μάθετε περισσότερα σχετικά με όλες τις παραμέτρους που υποστηρίζονται για τη σχολαστική ρύθμιση.

### Ορισμός παραμέτρων λεπτομερούς ρύθμισης

1. Οι παράμετροι λεπτομερούς ρύθμισης μπορούν να ομαδοποιηθούν σε 2 κατηγορίες - παράμετροι εκπαίδευσης, παράμετροι βελτιστοποίησης

1. Οι παράμετροι εκπαίδευσης ορίζουν τις πτυχές της εκπαίδευσης όπως -

    - Τον βελτιστοποιητή, τον προγραμματιστή που θα χρησιμοποιηθεί
    - Το μετρικό για να βελτιστοποιηθεί η λεπτομερής ρύθμιση
    - Τον αριθμό βημάτων εκπαίδευσης και το μέγεθος παρτίδας κ.ά.
    - Οι παράμετροι βελτιστοποίησης βοηθούν στην βελτιστοποίηση της μνήμης GPU και στην αποτελεσματική χρήση των υπολογιστικών πόρων.

1. Παρακάτω είναι μερικές από τις παραμέτρους που ανήκουν σε αυτή την κατηγορία. Οι παράμετροι βελτιστοποίησης διαφέρουν για κάθε μοντέλο και περιλαμβάνονται με το μοντέλο για να διαχειρίζονται αυτές τις διαφοροποιήσεις.

    - Ενεργοποίηση των deepspeed και LoRA
    - Ενεργοποίηση εκπαίδευσης με μικτή ακρίβεια
    - Ενεργοποίηση εκπαίδευσης πολλαπλών κόμβων

> [!NOTE]
> Η εποπτευόμενη λεπτομερής ρύθμιση μπορεί να οδηγήσει σε απώλεια ευθυγράμμισης ή καταστροφική λήθη. Συνιστούμε να ελέγξετε για αυτό το πρόβλημα και να εκτελέσετε ένα στάδιο ευθυγράμμισης μετά τη λεπτομερή ρύθμιση.

### Παράμετροι λεπτομερούς ρύθμισης

1. Αυτό το σενάριο Python ορίζει παραμέτρους για τη λεπτομερή ρύθμιση ενός μοντέλου μηχανικής μάθησης. Ακολουθεί μια ανάλυση του τι κάνει:

    - Ορίζει προεπιλεγμένες παραμέτρους εκπαίδευσης όπως ο αριθμός εποχών εκπαίδευσης, τα μεγέθη παρτίδας για εκπαίδευση και αξιολόγηση, τον ρυθμό μάθησης και τον τύπο προγραμματιστή ρυθμού μάθησης.

    - Ορίζει προεπιλεγμένες παραμέτρους βελτιστοποίησης όπως αν θα εφαρμοστεί Layer-wise Relevance Propagation (LoRa) και DeepSpeed, και το στάδιο DeepSpeed.

    - Συνδυάζει τις παραμέτρους εκπαίδευσης και βελτιστοποίησης σε ένα ενιαίο λεξικό που ονομάζεται finetune_parameters.

    - Ελέγχει αν το foundation_model έχει κάποιες προεπιλεγμένες παραμέτρους συγκεκριμένες για το μοντέλο. Αν ναι, εμφανίζει ένα μήνυμα προειδοποίησης και ενημερώνει το λεξικό finetune_parameters με αυτές τις προεπιλεγμένες παραμέτρους συγκεκριμένες για το μοντέλο. Η συνάρτηση ast.literal_eval χρησιμοποιείται για να μετατρέψει τις προεπιλεγμένες παραμέτρους από συμβολοσειρά σε λεξικό Python.

    - Εμφανίζει το τελικό σύνολο παραμέτρων λεπτομερούς ρύθμισης που θα χρησιμοποιηθούν στο τρέξιμο.

    - Συνοπτικά, αυτό το σενάριο ρυθμίζει και εμφανίζει τις παραμέτρους για τη λεπτομερή ρύθμιση ενός μοντέλου μηχανικής μάθησης, με τη δυνατότητα να υπερισχύσουν οι προεπιλεγμένες παράμετροι με παραμέτρους συγκεκριμένες για το μοντέλο.

    ```python
    # Ορίστε τις προεπιλεγμένες παραμέτρους εκπαίδευσης όπως ο αριθμός των εποχών εκπαίδευσης, τα μεγέθη παρτίδων για εκπαίδευση και αξιολόγηση, ο ρυθμός εκμάθησης και ο τύπος του προγραμματιστή ρυθμού εκμάθησης
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Ορίστε τις προεπιλεγμένες παραμέτρους βελτιστοποίησης όπως το αν θα εφαρμοστεί η Layer-wise Relevance Propagation (LoRa) και DeepSpeed, και το στάδιο του DeepSpeed
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Συγχωνεύστε τις παραμέτρους εκπαίδευσης και βελτιστοποίησης σε ένα ενιαίο λεξικό που ονομάζεται finetune_parameters
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Ελέγξτε αν το foundation_model έχει συγκεκριμένες προεπιλεγμένες παραμέτρους μοντέλου
    # Αν ναι, εκτυπώστε ένα προειδοποιητικό μήνυμα και ενημερώστε το λεξικό finetune_parameters με αυτές τις συγκεκριμένες προεπιλεγμένες τιμές μοντέλου
    # Η συνάρτηση ast.literal_eval χρησιμοποιείται για τη μετατροπή των συγκεκριμένων προεπιλεγμένων τιμών μοντέλου από συμβολοσειρά σε λεξικό Python
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # Μετατρέψτε τη συμβολοσειρά σε λεξικό Python
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Εκτυπώστε το τελικό σύνολο παραμέτρων fine-tuning που θα χρησιμοποιηθούν για την εκτέλεση
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Pipeline Εκπαίδευσης

1. Αυτό το σενάριο Python ορίζει μια συνάρτηση για να δημιουργήσει ένα εμφανιζόμενο όνομα για ένα pipeline εκπαίδευσης μηχανικής μάθησης και στη συνέχεια καλεί αυτή τη συνάρτηση για να δημιουργήσει και να τυπώσει το εμφανιζόμενο όνομα. Ακολουθεί μια ανάλυση του τι κάνει:

1. Ορίζεται η συνάρτηση get_pipeline_display_name. Αυτή η συνάρτηση δημιουργεί ένα εμφανιζόμενο όνομα βασισμένο σε διάφορες παραμέτρους που σχετίζονται με το pipeline εκπαίδευσης.

1. Μέσα στη συνάρτηση, υπολογίζεται το συνολικό μέγεθος παρτίδας πολλαπλασιάζοντας το μέγεθος παρτίδας ανά συσκευή, τον αριθμό βημάτων συσσώρευσης βαθμίδων, τον αριθμό GPUs ανά κόμβο και τον αριθμό κόμβων που χρησιμοποιούνται για λεπτομερή ρύθμιση.

1. Λαμβάνονται διάφορες άλλες παράμετροι όπως ο τύπος προγραμματιστή του ρυθμιστή ρυθμού μάθησης, αν εφαρμόζεται DeepSpeed, το στάδιο DeepSpeed, αν εφαρμόζεται Layer-wise Relevance Propagation (LoRa), το όριο για τον αριθμό των σημείων ελέγχου μοντέλου που κρατούνται και το μέγιστο μήκος ακολουθίας.

1. Κατασκευάζεται μια συμβολοσειρά που περιλαμβάνει όλες αυτές τις παραμέτρους, διαχωρισμένες με παύλες. Αν εφαρμόζεται DeepSpeed ή LoRa, η συμβολοσειρά περιλαμβάνει "ds" ακολουθούμενο από το στάδιο DeepSpeed ή "lora" αντίστοιχα. Αν όχι, περιλαμβάνει "nods" ή "nolora" αντίστοιχα.

1. Η συνάρτηση επιστρέφει αυτή τη συμβολοσειρά, η οποία χρησιμεύει ως εμφανιζόμενο όνομα για το pipeline εκπαίδευσης.

1. Μετά τον ορισμό της συνάρτησης, αυτή καλείται για να δημιουργήσει το εμφανιζόμενο όνομα, το οποίο στη συνέχεια τυπώνεται.

1. Συνοπτικά, αυτό το σενάριο δημιουργεί ένα εμφανιζόμενο όνομα για ένα pipeline εκπαίδευσης μηχανικής μάθησης βάσει διαφόρων παραμέτρων και στη συνέχεια τυπώνει αυτό το εμφανιζόμενο όνομα.

    ```python
    # Ορίστε μια συνάρτηση για τη δημιουργία ενός εμφανιζόμενου ονόματος για τη διαδικασία εκπαίδευσης
    def get_pipeline_display_name():
        # Υπολογίστε το συνολικό μέγεθος παρτίδας πολλαπλασιάζοντας το μέγεθος παρτίδας ανά συσκευή, τον αριθμό βημάτων συσσώρευσης βαθμίδας, τον αριθμό GPU ανά κόμβο και τον αριθμό κόμβων που χρησιμοποιούνται για προσαρμογή
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Ανάκτηση του τύπου προγραμματιστή ρυθμού μάθησης
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Ανάκτηση αν εφαρμόζεται το DeepSpeed
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Ανάκτηση του σταδίου DeepSpeed
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # Εάν εφαρμόζεται το DeepSpeed, περιλάβετε "ds" ακολουθούμενο από το στάδιο DeepSpeed στο εμφανιζόμενο όνομα· αν όχι, περιλάβετε "nods"
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Ανάκτηση αν εφαρμόζεται το Layer-wise Relevance Propagation (LoRa)
        lora = finetune_parameters.get("apply_lora", "false")
        # Εάν εφαρμόζεται το LoRa, περιλάβετε "lora" στο εμφανιζόμενο όνομα· αν όχι, περιλάβετε "nolora"
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Ανάκτηση του ορίου στον αριθμό των σημείων ελέγχου μοντέλου που θα κρατηθούν
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Ανάκτηση του μέγιστου μήκους ακολουθίας
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Δημιουργήστε το εμφανιζόμενο όνομα συνδυάζοντας όλες αυτές τις παραμέτρους, διαχωρισμένες με παύλες
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # Καλέστε τη συνάρτηση για να δημιουργήσετε το εμφανιζόμενο όνομα
    pipeline_display_name = get_pipeline_display_name()
    # Εκτυπώστε το εμφανιζόμενο όνομα
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Διαμόρφωση Pipeline

Αυτό το σενάριο Python ορίζει και διαμορφώνει ένα pipeline μηχανικής μάθησης χρησιμοποιώντας το Azure Machine Learning SDK. Ακολουθεί μια ανάλυση του τι κάνει:

1. Εισάγει απαραίτητα modules από το Azure AI ML SDK.

1. Αντλεί ένα συστατικό pipeline με το όνομα "chat_completion_pipeline" από το μητρώο.

1. Ορίζει μια εργασία pipeline χρησιμοποιώντας τον διακοσμητή `@pipeline` και τη συνάρτηση `create_pipeline`. Το όνομα του pipeline ορίζεται ως `pipeline_display_name`.

1. Μέσα στη συνάρτηση `create_pipeline`, αρχικοποιεί το αντληθέν συστατικό pipeline με διάφορες παραμέτρους, συμπεριλαμβανομένης της διαδρομής μοντέλου, των υπολογιστικών συστοιχιών για διάφορα στάδια, των συνόλων δεδομένων για εκπαίδευση και δοκιμές, του αριθμού GPUs για λεπτομερή ρύθμιση, και άλλων παραμέτρων λεπτομερούς ρύθμισης.

1. Χαρτογραφεί την έξοδο της εργασίας λεπτομερούς ρύθμισης στην έξοδο της εργασίας pipeline. Αυτό γίνεται ώστε το λεπτομερώς ρυθμισμένο μοντέλο να μπορεί να καταχωρηθεί εύκολα, κάτι που απαιτείται για την ανάπτυξη του μοντέλου σε διαδικτυακό ή παρτίδας endpoint.

1. Δημιουργεί ένα στιγμιότυπο του pipeline καλώντας τη συνάρτηση `create_pipeline`.

1. Ορίζει τη ρύθμιση `force_rerun` του pipeline σε `True`, που σημαίνει ότι δεν θα χρησιμοποιηθούν αποθηκευμένα αποτελέσματα από προηγούμενες εργασίες.

1. Ορίζει τη ρύθμιση `continue_on_step_failure` του pipeline σε `False`, που σημαίνει ότι το pipeline θα σταματήσει αν αποτύχει κάποιο βήμα.

1. Συνοπτικά, αυτό το σενάριο ορίζει και διαμορφώνει ένα pipeline μηχανικής μάθησης για εργασία chat completion χρησιμοποιώντας το Azure Machine Learning SDK.

    ```python
    # Εισαγάγετε τα απαραίτητα modules από το Azure AI ML SDK
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Ανακτήστε το συστατικό pipeline με το όνομα "chat_completion_pipeline" από το μητρώο
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Ορίστε την εργασία pipeline χρησιμοποιώντας το διακοσμητή @pipeline και τη συνάρτηση create_pipeline
    # Το όνομα του pipeline ορίζεται σε pipeline_display_name
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Αρχικοποιήστε το ανακτηθέν συστατικό pipeline με διάφορες παραμέτρους
        # Αυτές περιλαμβάνουν τη διαδρομή του μοντέλου, υπολογιστικές συστοιχίες για διαφορετικά στάδια, κατανομές δεδομένων για εκπαίδευση και δοκιμή, τον αριθμό των GPU για fine-tuning και άλλες παραμέτρους fine-tuning
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Χαρτογραφήστε τις κατανομές δεδομένων σε παραμέτρους
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Ρυθμίσεις εκπαίδευσης
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Ορισμένο στον διαθέσιμο αριθμό GPU στον υπολογιστή
            **finetune_parameters
        )
        return {
            # Χαρτογραφήστε την έξοδο της εργασίας fine tuning στην έξοδο της εργασίας pipeline
            # Αυτό γίνεται έτσι ώστε να μπορούμε εύκολα να καταχωρήσουμε το fine tuned μοντέλο
            # Η καταχώρηση του μοντέλου απαιτείται για την ανάπτυξη του μοντέλου σε διαδικτυακό ή παρτίδα endpoint
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Δημιουργήστε ένα στιγμιότυπο του pipeline καλώντας τη συνάρτηση create_pipeline
    pipeline_object = create_pipeline()
    
    # Μην χρησιμοποιείτε αποθηκευμένα αποτελέσματα από προηγούμενες εργασίες
    pipeline_object.settings.force_rerun = True
    
    # Ορίστε το continue on step failure σε False
    # Αυτό σημαίνει ότι το pipeline θα σταματήσει αν οποιοδήποτε βήμα αποτύχει
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Υποβολή της εργασίας

1. Αυτό το σενάριο Python υποβάλλει μια εργασία pipeline μηχανικής μάθησης σε έναν χώρο εργασίας Azure Machine Learning και στη συνέχεια περιμένει την ολοκλήρωση της εργασίας. Ακολουθεί μια ανάλυση του τι κάνει:

    - Καλεί τη μέθοδο create_or_update του αντικειμένου jobs στον workspace_ml_client για να υποβάλει την εργασία pipeline. Το pipeline που θα εκτελεστεί καθορίζεται από το pipeline_object, και το πείραμα υπό το οποίο εκτελείται η εργασία καθορίζεται από το experiment_name.

    - Στη συνέχεια καλεί τη μέθοδο stream του αντικειμένου jobs στον workspace_ml_client για να περιμένει την ολοκλήρωση της εργασίας pipeline. Η εργασία που περιμένει καθορίζεται από το χαρακτηριστικό name του αντικειμένου pipeline_job.

    - Συνοπτικά, αυτό το σενάριο υποβάλλει μια εργασία pipeline μηχανικής μάθησης σε έναν χώρο εργασίας Azure Machine Learning και στη συνέχεια περιμένει την ολοκλήρωση της εργασίας.

    ```python
    # Υποβάλετε την εργασία pipeline στον χώρο εργασίας Azure Machine Learning
    # Το pipeline που θα εκτελεστεί καθορίζεται από το pipeline_object
    # Το πείραμα υπό το οποίο εκτελείται η εργασία καθορίζεται από το experiment_name
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Περιμένετε να ολοκληρωθεί η εργασία pipeline
    # Η εργασία για την οποία γίνεται αναμονή καθορίζεται από το χαρακτηριστικό name του αντικειμένου pipeline_job
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Καταχώριση του λεπτομερώς ρυθμισμένου μοντέλου στο χώρο εργασίας

Θα καταχωρίσουμε το μοντέλο από την έξοδο της εργασίας λεπτομερούς ρύθμισης. Αυτό θα παρακολουθεί τη συνάφεια μεταξύ του λεπτομερώς ρυθμισμένου μοντέλου και της εργασίας λεπτομερούς ρύθμισης. Η εργασία λεπτομερούς ρύθμισης, επιπλέον, παρακολουθεί τη συνάφεια με το foundation model, τα δεδομένα και τον κώδικα εκπαίδευσης.

### Καταχώριση του Μοντέλου ML

1. Αυτό το σενάριο Python καταχωρίζει ένα μοντέλο μηχανικής μάθησης που εκπαιδεύτηκε σε ένα pipeline Azure Machine Learning. Ακολουθεί μια ανάλυση του τι κάνει:

    - Εισάγει τα απαραίτητα modules από το Azure AI ML SDK.

    - Ελέγχει αν η έξοδος trained_model είναι διαθέσιμη από την εργασία pipeline καλώντας τη μέθοδο get του αντικειμένου jobs στον workspace_ml_client και προσπελάζοντας το χαρακτηριστικό outputs.

    - Κατασκευάζει μια διαδρομή προς το εκπαιδευμένο μοντέλο μορφοποιώντας μια συμβολοσειρά με το όνομα της εργασίας pipeline και το όνομα της εξόδου ("trained_model").

    - Ορίζει ένα όνομα για το λεπτομερώς ρυθμισμένο μοντέλο προσθέτοντας "-ultrachat-200k" στο αρχικό όνομα μοντέλου και αντικαθιστώντας τα όποια / με παύλες.

    - Ετοιμάζει την καταχώριση του μοντέλου δημιουργώντας ένα αντικείμενο Model με διάφορες παραμέτρους, συμπεριλαμβανομένης της διαδρομής προς το μοντέλο, του τύπου του μοντέλου (μοντέλο MLflow), του ονόματος και της έκδοσης του μοντέλου, και μιας περιγραφής του μοντέλου.

    - Καταχωρίζει το μοντέλο καλώντας τη μέθοδο create_or_update του αντικειμένου models στον workspace_ml_client με το αντικείμενο Model ως όρισμα.

    - Τυπώνει το καταχωρημένο μοντέλο.

1. Συνοπτικά, αυτό το σενάριο καταχωρεί ένα μοντέλο μηχανικής μάθησης που εκπαιδεύτηκε σε ένα pipeline Azure Machine Learning.
    
    ```python
    # Εισαγωγή των απαραίτητων μονάδων από το Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Ελέγξτε αν η έξοδος `trained_model` είναι διαθέσιμη από την εργασία pipeline
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Κατασκευάστε μια διαδρομή προς το εκπαιδευμένο μοντέλο μορφοποιώντας μια συμβολοσειρά με το όνομα της εργασίας pipeline και το όνομα της εξόδου ("trained_model")
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Ορίστε ένα όνομα για το fine-tuned μοντέλο προσθέτοντας "-ultrachat-200k" στο αρχικό όνομα του μοντέλου και αντικαθιστώντας τυχόν καθέτους με παύλες
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Ετοιμαστείτε να εγγράψετε το μοντέλο δημιουργώντας ένα αντικείμενο Model με διάφορες παραμέτρους
    # Αυτές περιλαμβάνουν τη διαδρομή προς το μοντέλο, τον τύπο του μοντέλου (μοντέλο MLflow), το όνομα και την έκδοση του μοντέλου, και μια περιγραφή του μοντέλου
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Χρησιμοποιήστε χρονική σήμανση ως έκδοση για να αποφύγετε σύγκρουση εκδόσεων
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Εγγράψτε το μοντέλο καλώντας τη μέθοδο create_or_update του αντικειμένου models στο workspace_ml_client με το αντικείμενο Model ως όρισμα
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Εκτυπώστε το εγγεγραμμένο μοντέλο
    print("registered model: \n", registered_model)
    ```

## 7. Ανάπτυξη του λεπτομερώς ρυθμισμένου μοντέλου σε διαδικτυακό endpoint

Τα διαδικτυακά endpoints παρέχουν ένα ανθεκτικό REST API που μπορεί να χρησιμοποιηθεί για την ενσωμάτωση με εφαρμογές που χρειάζονται να χρησιμοποιήσουν το μοντέλο.

### Διαχείριση Endpoint

1. Αυτό το σενάριο Python δημιουργεί ένα διαχειριζόμενο διαδικτυακό endpoint στο Azure Machine Learning για ένα καταχωρημένο μοντέλο. Ακολουθεί μια ανάλυση του τι κάνει:

    - Εισάγει τα απαραίτητα modules από το Azure AI ML SDK.

    - Ορίζει ένα μοναδικό όνομα για το διαδικτυακό endpoint προσθέτοντας έναν χρονικό σφραγίδα στη συμβολοσειρά "ultrachat-completion-".

    - Ετοιμάζει τη δημιουργία του διαδικτυακού endpoint δημιουργώντας ένα αντικείμενο ManagedOnlineEndpoint με διάφορες παραμέτρους, συμπεριλαμβανομένου του ονόματος του endpoint, μιας περιγραφής του endpoint και της λειτουργίας αυθεντικοποίησης ("key").

    - Δημιουργεί το διαδικτυακό endpoint καλώντας τη μέθοδο begin_create_or_update του workspace_ml_client με το αντικείμενο ManagedOnlineEndpoint ως όρισμα. Στη συνέχεια περιμένει την ολοκλήρωση της δημιουργίας καλώντας τη μέθοδο wait.

1. Συνοπτικά, αυτό το σενάριο δημιουργεί ένα διαχειριζόμενο διαδικτυακό endpoint στο Azure Machine Learning για ένα καταχωρημένο μοντέλο.

    ```python
    # Εισαγωγή των απαραίτητων μονάδων από το Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Ορισμός ενός μοναδικού ονόματος για το διαδικτυακό endpoint προσθέτοντας ένα χρονικό σήμα στη συμβολοσειρά "ultrachat-completion-"
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Προετοιμασία για τη δημιουργία του διαδικτυακού endpoint δημιουργώντας ένα αντικείμενο ManagedOnlineEndpoint με διάφορες παραμέτρους
    # Αυτές περιλαμβάνουν το όνομα του endpoint, μια περιγραφή του endpoint, και τη λειτουργία ελέγχου ταυτότητας ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Δημιουργία του διαδικτυακού endpoint καλώντας τη μέθοδο begin_create_or_update του workspace_ml_client με το αντικείμενο ManagedOnlineEndpoint ως όρισμα
    # Στη συνέχεια, αναμονή για την ολοκλήρωση της λειτουργίας δημιουργίας καλώντας τη μέθοδο wait
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Μπορείτε να βρείτε εδώ τη λίστα των υποστηριζόμενων SKU για ανάπτυξη - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Ανάπτυξη Μοντέλου ML

1. Αυτό το σενάριο Python αναπτύσσει ένα καταχωρημένο μοντέλο μηχανικής μάθησης σε ένα διαχειριζόμενο διαδικτυακό endpoint στο Azure Machine Learning. Ακολουθεί μια ανάλυση του τι κάνει:

    - Εισάγει το module ast, που παρέχει λειτουργίες για επεξεργασία δέντρων της αφηρημένης σύνταξης Python.

    - Ορίζει τον τύπο της περίπτωσης για την ανάπτυξη στο "Standard_NC6s_v3".

    - Ελέγχει αν η ετικέτα inference_compute_allow_list υπάρχει στο foundation model. Αν υπάρχει, μετατρέπει την τιμή της ετικέτας από συμβολοσειρά σε λίστα Python και την αναθέτει στην inference_computes_allow_list. Αν δεν υπάρχει, ορίζει την inference_computes_allow_list ως None.

    - Ελέγχει αν ο καθορισμένος τύπος περίπτωσης βρίσκεται στη λίστα επιτρεπόμενων. Αν όχι, εμφανίζει μήνυμα που ζητά από τον χρήστη να επιλέξει έναν τύπο περίπτωσης από τη λίστα επιτρεπόμενων.

    - Ετοιμάζει τη δημιουργία της ανάπτυξης δημιουργώντας ένα αντικείμενο ManagedOnlineDeployment με διάφορες παραμέτρους, συμπεριλαμβανομένου του ονόματος της ανάπτυξης, του ονόματος του endpoint, του ID του μοντέλου, του τύπου και του αριθμού περιπτώσεων, των ρυθμίσεων ελέγχου ζωντάνιας και των ρυθμίσεων αιτημάτων.

    - Δημιουργεί την ανάπτυξη καλώντας τη μέθοδο begin_create_or_update του workspace_ml_client με το αντικείμενο ManagedOnlineDeployment ως όρισμα. Στη συνέχεια περιμένει να ολοκληρωθεί η δημιουργία καλώντας τη μέθοδο wait.

    - Ορίζει την κυκλοφορία του endpoint ώστε να κατευθύνει το 100% της κίνησης στην ανάπτυξη "demo".

    - Ενημερώνει το endpoint καλώντας τη μέθοδο begin_create_or_update του workspace_ml_client με το αντικείμενο endpoint ως όρισμα. Στη συνέχεια περιμένει την ολοκλήρωση της ενημέρωσης καλώντας τη μέθοδο result.

1. Συνοπτικά, αυτό το σενάριο αναπτύσσει ένα καταχωρημένο μοντέλο μηχανικής μάθησης σε ένα διαχειριζόμενο διαδικτυακό endpoint στο Azure Machine Learning.

    ```python
    # Εισαγωγή της ενότητας ast, η οποία παρέχει λειτουργίες για την επεξεργασία δέντρων της αφηρημένης συντακτικής γραμματικής της Python
    import ast
    
    # Ορισμός του τύπου παρουσίας για την ανάπτυξη
    instance_type = "Standard_NC6s_v3"
    
    # Έλεγχος αν το tag `inference_compute_allow_list` υπάρχει στο θεμελιώδες μοντέλο
    if "inference_compute_allow_list" in foundation_model.tags:
        # Αν υπάρχει, μετατροπή της τιμής του tag από συμβολοσειρά σε λίστα Python και ανάθεση στο `inference_computes_allow_list`
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Αν δεν υπάρχει, ορισμός του `inference_computes_allow_list` σε `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Έλεγχος αν ο καθορισμένος τύπος παρουσίας είναι στη λίστα επιτρεπόμενων
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Προετοιμασία για δημιουργία της ανάπτυξης δημιουργώντας ένα αντικείμενο `ManagedOnlineDeployment` με διάφορες παραμέτρους
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Δημιουργία της ανάπτυξης καλώντας τη μέθοδο `begin_create_or_update` του `workspace_ml_client` με το αντικείμενο `ManagedOnlineDeployment` ως όρισμα
    # Στη συνέχεια αναμονή για να ολοκληρωθεί η λειτουργία δημιουργίας καλώντας τη μέθοδο `wait`
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Ορισμός της κυκλοφορίας του endpoint για να κατευθύνει το 100% της κίνησης στην ανάπτυξη "demo"
    endpoint.traffic = {"demo": 100}
    
    # Ενημέρωση του endpoint καλώντας τη μέθοδο `begin_create_or_update` του `workspace_ml_client` με το αντικείμενο `endpoint` ως όρισμα
    # Στη συνέχεια αναμονή για να ολοκληρωθεί η λειτουργία ενημέρωσης καλώντας τη μέθοδο `result`
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Δοκιμή του endpoint με δείγμα δεδομένων

Θα πάρουμε μερικά δείγματα δεδομένων από το δοκιμαστικό σύνολο δεδομένων και θα τα υποβάλουμε στο διαδικτυακό endpoint για συμπερασματολογία. Στη συνέχεια θα εμφανίσουμε τις βαθμολογημένες ετικέτες μαζί με τις ετικέτες της αλήθειας.

### Ανάγνωση αποτελεσμάτων

1. Αυτό το σενάριο Python διαβάζει ένα αρχείο JSON Lines σε ένα pandas DataFrame, επιλέγει ένα τυχαίο δείγμα, και επαναφέρει τον δείκτη. Ακολουθεί μια ανάλυση του τι κάνει:

    - Διαβάζει το αρχείο ./ultrachat_200k_dataset/test_gen.jsonl σε ένα pandas DataFrame. Η συνάρτηση read_json χρησιμοποιείται με το όρισμα lines=True γιατί το αρχείο είναι σε μορφή JSON Lines, όπου κάθε γραμμή είναι ξεχωριστό αντικείμενο JSON.

    - Παίρνει ένα τυχαίο δείγμα 1 γραμμής από το DataFrame. Η συνάρτηση sample χρησιμοποιείται με το όρισμα n=1 για να ορίσει τον αριθμό των τυχαίων γραμμών που επιλέγονται.

    - Επαναφέρει τον δείκτη του DataFrame. Η συνάρτηση reset_index χρησιμοποιείται με το όρισμα drop=True για να απορριφθεί ο αρχικός δείκτης και να αντικατασταθεί με νέο δείκτη με προεπιλεγμένες ακέραιες τιμές.

    - Εμφανίζει τις πρώτες 2 γραμμές του DataFrame χρησιμοποιώντας τη συνάρτηση head με όρισμα 2. Ωστόσο, καθώς το DataFrame περιέχει μόνο μία γραμμή μετά το δείγμα, αυτό θα εμφανίσει μόνο αυτή τη μία γραμμή.

1. Συνοπτικά, αυτό το σενάριο διαβάζει ένα αρχείο JSON Lines σε ένα pandas DataFrame, παίρνει ένα τυχαίο δείγμα 1 γραμμής, επαναφέρει τον δείκτη και εμφανίζει την πρώτη γραμμή.
    
    ```python
    # Εισαγωγή της βιβλιοθήκης pandas
    import pandas as pd
    
    # Ανάγνωση του αρχείου JSON Lines './ultrachat_200k_dataset/test_gen.jsonl' σε ένα pandas DataFrame
    # Το όρισμα 'lines=True' υποδηλώνει ότι το αρχείο είναι σε μορφή JSON Lines, όπου κάθε γραμμή είναι ένα ξεχωριστό αντικείμενο JSON
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Λήψη τυχαίου δείγματος 1 γραμμής από το DataFrame
    # Το όρισμα 'n=1' καθορίζει τον αριθμό των τυχαίων γραμμών που θα επιλεγούν
    test_df = test_df.sample(n=1)
    
    # Επαναφορά του ευρετηρίου του DataFrame
    # Το όρισμα 'drop=True' υποδηλώνει ότι το αρχικό ευρετήριο πρέπει να απορριφθεί και να αντικατασταθεί με νέο ευρετήριο με προεπιλεγμένες ακέραιες τιμές
    # Το όρισμα 'inplace=True' υποδηλώνει ότι το DataFrame θα τροποποιηθεί επιτόπου (χωρίς να δημιουργηθεί νέο αντικείμενο)
    test_df.reset_index(drop=True, inplace=True)
    
    # Εμφάνιση των πρώτων 2 γραμμών του DataFrame
    # Ωστόσο, επειδή το DataFrame περιέχει μόνο μία γραμμή μετά τη δειγματοληψία, αυτό θα εμφανίσει μόνο εκείνη τη μία γραμμή
    test_df.head(2)
    ```

### Δημιουργία αντικειμένου JSON

1. Αυτό το σενάριο Python δημιουργεί ένα αντικείμενο JSON με συγκεκριμένες παραμέτρους και το αποθηκεύει σε αρχείο. Ακολουθεί μια ανάλυση του τι κάνει:

    - Εισάγει το module json, που παρέχει λειτουργίες για εργασία με δεδομένα JSON.
- Δημιουργεί ένα λεξικό parameters με κλειδιά και τιμές που αναπαριστούν παραμέτρους για ένα μοντέλο μηχανικής μάθησης. Τα κλειδιά είναι "temperature", "top_p", "do_sample" και "max_new_tokens", και οι αντίστοιχες τιμές τους είναι 0.6, 0.9, True και 200 αντίστοιχα.

- Δημιουργεί ένα άλλο λεξικό test_json με δύο κλειδιά: "input_data" και "params". Η τιμή του "input_data" είναι ένα άλλο λεξικό με κλειδιά "input_string" και "parameters". Η τιμή του "input_string" είναι μια λίστα που περιέχει το πρώτο μήνυμα από το DataFrame test_df. Η τιμή του "parameters" είναι το λεξικό parameters που δημιουργήθηκε νωρίτερα. Η τιμή του "params" είναι ένα κενό λεξικό.

- Ανοίγει ένα αρχείο με όνομα sample_score.json
    
    ```python
    # Εισάγετε το module json, το οποίο παρέχει συναρτήσεις για εργασία με δεδομένα JSON
    import json
    
    # Δημιουργήστε ένα λεξικό `parameters` με κλειδιά και τιμές που αναπαριστούν παραμέτρους για ένα μοντέλο μηχανικής μάθησης
    # Τα κλειδιά είναι "temperature", "top_p", "do_sample" και "max_new_tokens", και οι αντίστοιχες τιμές τους είναι 0.6, 0.9, True, και 200 αντίστοιχα
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Δημιουργήστε ένα άλλο λεξικό `test_json` με δύο κλειδιά: "input_data" και "params"
    # Η τιμή του "input_data" είναι ένα άλλο λεξικό με κλειδιά "input_string" και "parameters"
    # Η τιμή του "input_string" είναι μια λίστα που περιέχει το πρώτο μήνυμα από το DataFrame `test_df`
    # Η τιμή του "parameters" είναι το λεξικό `parameters` που δημιουργήθηκε νωρίτερα
    # Η τιμή του "params" είναι ένα κενό λεξικό
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Ανοίξτε ένα αρχείο με όνομα `sample_score.json` στον κατάλογο `./ultrachat_200k_dataset` σε λειτουργία εγγραφής
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Γράψτε το λεξικό `test_json` στο αρχείο σε μορφή JSON χρησιμοποιώντας τη συνάρτηση `json.dump`
        json.dump(test_json, f)
    ```

### Εκκίνηση Endpoint

1. Αυτό το script Python εκκινεί ένα online endpoint στο Azure Machine Learning για να βαθμολογήσει ένα αρχείο JSON. Ακολουθεί ανάλυση των ενεργειών του:

    - Καλεί τη μέθοδο invoke της ιδιότητας online_endpoints του αντικειμένου workspace_ml_client. Αυτή η μέθοδος χρησιμοποιείται για να στείλει ένα αίτημα σε ένα online endpoint και να λάβει μια απάντηση.

    - Προσδιορίζει το όνομα του endpoint και της ανάπτυξης με τα ορίσματα endpoint_name και deployment_name. Σε αυτή την περίπτωση, το όνομα του endpoint αποθηκεύεται στη μεταβλητή online_endpoint_name και το όνομα της ανάπτυξης είναι "demo".

    - Προσδιορίζει τη διαδρομή προς το αρχείο JSON που θα βαθμολογηθεί με το όρισμα request_file. Σε αυτή την περίπτωση, το αρχείο είναι ./ultrachat_200k_dataset/sample_score.json.

    - Αποθηκεύει την απάντηση από το endpoint στη μεταβλητή response.

    - Εκτυπώνει την ακατέργαστη απάντηση.

1. Επιγραμματικά, το script εκκινεί ένα online endpoint στο Azure Machine Learning για να βαθμολογήσει ένα αρχείο JSON και τυπώνει την απάντηση.

    ```python
    # Εκτελέστε το διαδικτυακό σημείο τερματισμού στο Azure Machine Learning για να αξιολογήσετε το αρχείο `sample_score.json`
    # Η μέθοδος `invoke` της ιδιότητας `online_endpoints` του αντικειμένου `workspace_ml_client` χρησιμοποιείται για την αποστολή αιτήματος σε διαδικτυακό σημείο τερματισμού και λήψη απάντησης
    # Το όρισμα `endpoint_name` καθορίζει το όνομα του σημείου τερματισμού, το οποίο αποθηκεύεται στη μεταβλητή `online_endpoint_name`
    # Το όρισμα `deployment_name` καθορίζει το όνομα της ανάπτυξης, το οποίο είναι "demo"
    # Το όρισμα `request_file` καθορίζει τη διαδρομή προς το αρχείο JSON που θα αξιολογηθεί, το οποίο είναι `./ultrachat_200k_dataset/sample_score.json`
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Εκτυπώστε την ακατέργαστη απάντηση από το σημείο τερματισμού
    print("raw response: \n", response, "\n")
    ```

## 9. Διαγραφή του online endpoint

1. Μη ξεχάσετε να διαγράψετε το online endpoint, αλλιώς θα συνεχίζει να μετράτε το κόστος χρήσης του υπολογιστικού πόρου που χρησιμοποιεί το endpoint. Αυτή η γραμμή κώδικα Python διαγράφει ένα online endpoint στο Azure Machine Learning. Ακολουθεί ανάλυση των ενεργειών της:

    - Καλεί τη μέθοδο begin_delete της ιδιότητας online_endpoints του αντικειμένου workspace_ml_client. Αυτή η μέθοδος χρησιμοποιείται για να ξεκινήσει η διαγραφή ενός online endpoint.

    - Προσδιορίζει το όνομα του endpoint που θα διαγραφεί με το όρισμα name. Σε αυτή την περίπτωση, το όνομα του endpoint αποθηκεύεται στη μεταβλητή online_endpoint_name.

    - Καλεί τη μέθοδο wait για να περιμένει μέχρι να ολοκληρωθεί η διαδικασία διαγραφής. Πρόκειται για μια λειτουργία που μπλοκάρει, δηλαδή εμποδίζει το script να συνεχίσει μέχρι να τελειώσει η διαγραφή.

    - Επιγραμματικά, αυτή η γραμμή κώδικα ξεκινά τη διαγραφή ενός online endpoint στο Azure Machine Learning και περιμένει να ολοκληρωθεί η διαδικασία.

    ```python
    # Διαγραφή του online endpoint στο Azure Machine Learning
    # Η μέθοδος `begin_delete` της ιδιότητας `online_endpoints` του αντικειμένου `workspace_ml_client` χρησιμοποιείται για να ξεκινήσει η διαγραφή ενός online endpoint
    # Το όρισμα `name` καθορίζει το όνομα του endpoint που θα διαγραφεί, το οποίο αποθηκεύεται στη μεταβλητή `online_endpoint_name`
    # Καλείται η μέθοδος `wait` για να περιμένει μέχρι να ολοκληρωθεί η λειτουργία διαγραφής. Πρόκειται για μια λειτουργία αποκλεισμού, δηλαδή θα αποτρέψει το script από το να συνεχίσει μέχρι να ολοκληρωθεί η διαγραφή
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η επίσημη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->