# Βελτιστοποίηση και Ενσωμάτωση προσαρμοσμένων μοντέλων Phi-3 με το Prompt flow στο Microsoft Foundry

Αυτό το δείγμα end-to-end (E2E) βασίζεται στον οδηγό "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" από την Κοινότητα Τεχνολογίας της Microsoft. Εισάγει τις διαδικασίες βελτιστοποίησης, ανάπτυξης και ενσωμάτωσης προσαρμοσμένων μοντέλων Phi-3 με το Prompt flow στο Microsoft Foundry. 
Σε αντίθεση με το δείγμα E2E, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", το οποίο περιλάμβανε εκτέλεση κώδικα τοπικά, αυτό το σεμινάριο εστιάζει πλήρως στη βελτιστοποίηση και στην ενσωμάτωση του μοντέλου σας μέσα στο Azure AI / ML Studio.

## Επισκόπηση

Σε αυτό το δείγμα E2E, θα μάθετε πώς να βελτιστοποιήσετε το μοντέλο Phi-3 και να το ενσωματώσετε με το Prompt flow στο Microsoft Foundry. Αξιοποιώντας το Azure AI / ML Studio, θα δημιουργήσετε μια ροή εργασίας για την ανάπτυξη και αξιοποίηση προσαρμοσμένων μοντέλων AI. Αυτό το δείγμα E2E διαιρείται σε τρία σενάρια:

**Σενάριο 1: Ρύθμιση πόρων Azure και Προετοιμασία για βελτιστοποίηση**

**Σενάριο 2: Βελτιστοποίηση του μοντέλου Phi-3 και Ανάπτυξη στο Azure Machine Learning Studio**

**Σενάριο 3: Ενσωμάτωση με το Prompt flow και συνομιλία με το προσαρμοσμένο μοντέλο σας στο Microsoft Foundry**

Ακολουθεί μια επισκόπηση αυτού του δείγματος E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/el/00-01-architecture.198ba0f1ae6d841a.webp)

### Πίνακας Περιεχομένων

1. **[Σενάριο 1: Ρύθμιση πόρων Azure και Προετοιμασία για βελτιστοποίηση](#σενάριο-1-ρύθμιση-πόρων-azure-και-προετοιμασία-για-βελτιστοποίηση)**
    - [Δημιουργία χώρου εργασίας Azure Machine Learning](#δημιουργία-χώρου-εργασίας-azure-machine-learning)
    - [Αίτηση για όρια GPU στην συνδρομή Azure](#αίτηση-για-όρια-gpu-στην-συνδρομή-azure)
    - [Προσθήκη ανάθεσης ρόλου](#προσθήκη-ανάθεσης-ρόλου)
    - [Ρύθμιση έργου](#ρύθμιση-έργου)
    - [Προετοιμασία συνόλου δεδομένων για βελτιστοποίηση](#προετοιμασία-του-συνόλου-δεδομένων-για-fine-tuning)

1. **[Σενάριο 2: Βελτιστοποίηση μοντέλου Phi-3 και Ανάπτυξη στο Azure Machine Learning Studio](#σενάριο-2-κάντε-fine-tuning-στο-μοντέλο-phi-3-και-ανάπτυξη-στο-azure-machine-learning-studio)**
    - [Βελτιστοποίηση του μοντέλου Phi-3](#κάντε-fine-tuning-στο-μοντέλο-phi-3)
    - [Ανάπτυξη του βελτιστοποιημένου μοντέλου Phi-3](#ανάπτυξη-του-fine-tuned-μοντέλου-phi-3)

1. **[Σενάριο 3: Ενσωμάτωση με το Prompt flow και Συνομιλία με το προσαρμοσμένο μοντέλο σας στο Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Ενσωμάτωση του προσαρμοσμένου μοντέλου Phi-3 με το Prompt flow](#ενσωμάτωση-του-προσαρμοσμένου-μοντέλου-phi-3-με-prompt-flow)
    - [Συνομιλία με το προσαρμοσμένο μοντέλο Phi-3](#συνομιλία-με-το-προσαρμοσμένο-μοντέλο-phi-3)

## Σενάριο 1: Ρύθμιση πόρων Azure και Προετοιμασία για βελτιστοποίηση

### Δημιουργία χώρου εργασίας Azure Machine Learning

1. Πληκτρολογήστε *azure machine learning* στη **γραμμή αναζήτησης** στο πάνω μέρος της σελίδας του portal και επιλέξτε **Azure Machine Learning** από τις διαθέσιμες επιλογές.

    ![Type azure machine learning.](../../../../../../translated_images/el/01-01-type-azml.acae6c5455e67b4b.webp)

2. Επιλέξτε **+ Δημιουργία** από το μενού πλοήγησης.

3. Επιλέξτε **Νέος χώρος εργασίας** από το μενού πλοήγησης.

    ![Select new workspace.](../../../../../../translated_images/el/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Εκτελέστε τις ακόλουθες ενέργειες:

    - Επιλέξτε τη **Συνδρομή** Azure.
    - Επιλέξτε την **Ομάδα πόρων** για χρήση (δημιουργήστε μία νέα αν χρειάζεται).
    - Εισάγετε το **Όνομα χώρου εργασίας**. Πρέπει να είναι μοναδικό.
    - Επιλέξτε την **Περιοχή** που θέλετε να χρησιμοποιήσετε.
    - Επιλέξτε τον **λογαριασμό αποθήκευσης** για χρήση (δημιουργήστε έναν νέο αν χρειάζεται).
    - Επιλέξτε το **key vault** για χρήση (δημιουργήστε ένα νέο αν χρειάζεται).
    - Επιλέξτε τα **Application insights** για χρήση (δημιουργήστε νέα αν χρειάζεται).
    - Επιλέξτε το **Κατάλογο κοντέινερ** για χρήση (δημιουργήστε έναν νέο αν χρειάζεται).

    ![Fill azure machine learning.](../../../../../../translated_images/el/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Επιλέξτε **Έλεγχος + Δημιουργία**.

6. Επιλέξτε **Δημιουργία**.

### Αίτηση για όρια GPU στην συνδρομή Azure

Σε αυτό το σεμινάριο, θα μάθετε πώς να βελτιστοποιήσετε και να αναπτύξετε ένα μοντέλο Phi-3, χρησιμοποιώντας GPUs. Για τη βελτιστοποίηση, θα χρησιμοποιήσετε το *Standard_NC24ads_A100_v4* GPU, που απαιτεί αίτηση ορίων. Για την ανάπτυξη, θα χρησιμοποιήσετε το *Standard_NC6s_v3* GPU, που επίσης απαιτεί αίτηση ορίων.

> [!NOTE]
>
> Μόνο οι συνδρομές Pay-As-You-Go (ο τυπικός τύπος συνδρομής) είναι επιλέξιμες για κατανομή GPU· οι συνδρομές με οφέλη δεν υποστηρίζονται προς το παρόν.
>

1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Εκτελέστε τις ακόλουθες ενέργειες για να αιτηθείτε το όριο *Standard NCADSA100v4 Family*:

    - Επιλέξτε **Όριο** από την αριστερή πλευρική καρτέλα.
    - Επιλέξτε την **Οικογένεια εικονικής μηχανής** που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, επιλέξτε **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, που περιλαμβάνει το GPU *Standard_NC24ads_A100_v4*.
    - Επιλέξτε το **Αίτημα ορίου** από το μενού πλοήγησης.

        ![Request quota.](../../../../../../translated_images/el/02-02-request-quota.c0428239a63ffdd5.webp)

    - Στην σελίδα Αίτησης ορίου, εισάγετε το **Νέο όριο πυρήνων** που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, 24.
    - Στην σελίδα Αίτησης ορίου, επιλέξτε **Υποβολή** για να αιτηθείτε το όριο GPU.

1. Εκτελέστε τις ακόλουθες ενέργειες για να αιτηθείτε το όριο *Standard NCSv3 Family*:

    - Επιλέξτε **Όριο** από την αριστερή πλευρική καρτέλα.
    - Επιλέξτε την **Οικογένεια εικονικής μηχανής** που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, επιλέξτε **Standard NCSv3 Family Cluster Dedicated vCPUs**, που περιλαμβάνει το GPU *Standard_NC6s_v3*.
    - Επιλέξτε το **Αίτημα ορίου** από το μενού πλοήγησης.
    - Στην σελίδα Αίτησης ορίου, εισάγετε το **Νέο όριο πυρήνων** που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, 24.
    - Στην σελίδα Αίτησης ορίου, επιλέξτε **Υποβολή** για να αιτηθείτε το όριο GPU.

### Προσθήκη ανάθεσης ρόλου

Για να βελτιστοποιήσετε και να αναπτύξετε τα μοντέλα σας, πρέπει πρώτα να δημιουργήσετε Μηχανισμό Διαχείρισης Ανάθεσης Χρήστη (User Assigned Managed Identity - UAI) και να του αναθέσετε τα κατάλληλα δικαιώματα. Αυτή η UAI θα χρησιμοποιηθεί για την πιστοποίηση κατά την ανάπτυξη.

#### Δημιουργία Μηχανισμού Διαχείρισης Ανάθεσης Χρήστη (UAI)

1. Πληκτρολογήστε *managed identities* στη **γραμμή αναζήτησης** στο πάνω μέρος της σελίδας του portal και επιλέξτε **Managed Identities** από τις διαθέσιμες επιλογές.

    ![Type managed identities.](../../../../../../translated_images/el/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Επιλέξτε **+ Δημιουργία**.

    ![Select create.](../../../../../../translated_images/el/03-02-select-create.92bf8989a5cd98f2.webp)

1. Εκτελέστε τις ακόλουθες εργασίες:

    - Επιλέξτε τη **Συνδρομή** Azure.
    - Επιλέξτε την **Ομάδα πόρων** για χρήση (δημιουργήστε μία νέα αν χρειάζεται).
    - Επιλέξτε την **Περιοχή** που θέλετε να χρησιμοποιήσετε.
    - Εισάγετε το **Όνομα**. Πρέπει να είναι μοναδικό.

    ![Select create.](../../../../../../translated_images/el/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Επιλέξτε **Έλεγχος + δημιουργία**.

1. Επιλέξτε **+ Δημιουργία**.

#### Προσθήκη ανάθεσης ρόλου Contributor στον Managed Identity

1. Πλοηγηθείτε στον πόρο Managed Identity που δημιουργήσατε.

1. Επιλέξτε **Αναθέσεις ρόλων Azure** από την αριστερή πλευρική καρτέλα.

1. Επιλέξτε **+ Προσθήκη ανάθεσης ρόλου** από το μενού πλοήγησης.

1. Στη σελίδα Προσθήκη ανάθεσης ρόλου, εκτελέστε τις ακόλουθες εργασίες:
    - Επιλέξτε το **Πεδίο εφαρμογής** ως **Ομάδα πόρων**.
    - Επιλέξτε τη **Συνδρομή** Azure.
    - Επιλέξτε την **Ομάδα πόρων** για χρήση.
    - Επιλέξτε τον **Ρόλο** ως **Συνεισφέρων (Contributor)**.

    ![Fill contributor role.](../../../../../../translated_images/el/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Επιλέξτε **Αποθήκευση**.

#### Προσθήκη ανάθεσης ρόλου Storage Blob Data Reader στον Managed Identity

1. Πληκτρολογήστε *storage accounts* στη **γραμμή αναζήτησης** στο πάνω μέρος της σελίδας του portal και επιλέξτε **Storage accounts** από τις διαθέσιμες επιλογές.

    ![Type storage accounts.](../../../../../../translated_images/el/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Επιλέξτε τον λογαριασμό αποθήκευσης που συνδέεται με τον χώρο εργασίας Azure Machine Learning που δημιουργήσατε. Για παράδειγμα, *finetunephistorage*.

1. Εκτελέστε τις ακόλουθες ενέργειες για να πλοηγηθείτε στη σελίδα Προσθήκης ανάθεσης ρόλου:

    - Πλοηγηθείτε στον λογαριασμό Azure Storage που δημιουργήσατε.
    - Επιλέξτε **Έλεγχος πρόσβασης (IAM)** από την αριστερή πλευρική καρτέλα.
    - Επιλέξτε **+ Προσθήκη** από το μενού πλοήγησης.
    - Επιλέξτε **Προσθήκη ανάθεσης ρόλου** από το μενού πλοήγησης.

    ![Add role.](../../../../../../translated_images/el/03-06-add-role.353ccbfdcf0789c2.webp)

1. Στη σελίδα Προσθήκη ανάθεσης ρόλου, εκτελέστε τις ακόλουθες εργασίες:

    - Στη σελίδα Ρόλου, πληκτρολογήστε *Storage Blob Data Reader* στη **γραμμή αναζήτησης** και επιλέξτε **Storage Blob Data Reader** από τις διαθέσιμες επιλογές.
    - Στη σελίδα Ρόλου, επιλέξτε **Επόμενο**.
    - Στη σελίδα Μελών, επιλέξτε **Ανάθεση πρόσβασης σε** **Managed identity**.
    - Στη σελίδα Μελών, επιλέξτε **+ Επιλογή μελών**.
    - Στη σελίδα Επιλογής managed identities, επιλέξτε τη **Συνδρομή** Azure.
    - Στη σελίδα Επιλογής managed identities, επιλέξτε την **Managed identity** στο πεδίο **Manage Identity**.
    - Στη σελίδα Επιλογής managed identities, επιλέξτε το Manage Identity που δημιουργήσατε. Για παράδειγμα, *finetunephi-managedidentity*.
    - Στη σελίδα Επιλογής managed identities, επιλέξτε **Επιλογή**.

    ![Select managed identity.](../../../../../../translated_images/el/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Επιλέξτε **Έλεγχος + ανάθεση**.

#### Προσθήκη ανάθεσης ρόλου AcrPull στον Managed Identity

1. Πληκτρολογήστε *container registries* στη **γραμμή αναζήτησης** στο πάνω μέρος της σελίδας του portal και επιλέξτε **Container registries** από τις διαθέσιμες επιλογές.

    ![Type container registries.](../../../../../../translated_images/el/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Επιλέξτε τον κατάλογο κοντέινερ που συνδέεται με τον χώρο εργασίας Azure Machine Learning. Για παράδειγμα, *finetunephicontainerregistry*

1. Εκτελέστε τις ακόλουθες ενέργειες για να πλοηγηθείτε στη σελίδα Προσθήκης ανάθεσης ρόλου:

    - Επιλέξτε **Έλεγχος πρόσβασης (IAM)** από την αριστερή πλευρική καρτέλα.
    - Επιλέξτε **+ Προσθήκη** από το μενού πλοήγησης.
    - Επιλέξτε **Προσθήκη ανάθεσης ρόλου** από το μενού πλοήγησης.

1. Στη σελίδα Προσθήκης ανάθεσης ρόλου, εκτελέστε τις ακόλουθες εργασίες:

    - Στη σελίδα Ρόλου, πληκτρολογήστε *AcrPull* στη **γραμμή αναζήτησης** και επιλέξτε **AcrPull** από τις διαθέσιμες επιλογές.
    - Στη σελίδα Ρόλου, επιλέξτε **Επόμενο**.
    - Στη σελίδα Μελών, επιλέξτε **Ανάθεση πρόσβασης σε** **Managed identity**.
    - Στη σελίδα Μελών, επιλέξτε **+ Επιλογή μελών**.
    - Στη σελίδα Επιλογής managed identities, επιλέξτε τη **Συνδρομή** Azure.
    - Στη σελίδα Επιλογής managed identities, επιλέξτε την **Managed identity** στο πεδίο **Manage Identity**.
    - Στη σελίδα Επιλογής managed identities, επιλέξτε το Manage Identity που δημιουργήσατε. Για παράδειγμα, *finetunephi-managedidentity*.
    - Στη σελίδα Επιλογής managed identities, επιλέξτε **Επιλογή**.
    - Επιλέξτε **Έλεγχος + ανάθεση**.

### Ρύθμιση έργου

Για να κατεβάσετε τα σύνολα δεδομένων που απαιτούνται για βελτιστοποίηση, θα ρυθμίσετε ένα τοπικό περιβάλλον.

Σε αυτή την άσκηση, θα

- Δημιουργήσετε έναν φάκελο εργασίας.
- Δημιουργήσετε ένα εικονικό περιβάλλον.
- Εγκαταστήσετε τα απαραίτητα πακέτα.
- Δημιουργήσετε ένα αρχείο *download_dataset.py* για να πραγματοποιήσετε λήψη του συνόλου δεδομένων.

#### Δημιουργία φακέλου εργασίας

1. Ανοίξτε ένα τερματικό και πληκτρολογήστε την ακόλουθη εντολή για να δημιουργήσετε έναν φάκελο με όνομα *finetune-phi* στην προεπιλεγμένη διαδρομή.

    ```console
    mkdir finetune-phi
    ```

2. Πληκτρολογήστε την ακόλουθη εντολή μέσα στο τερματικό για να πλοηγηθείτε στον φάκελο *finetune-phi* που δημιουργήσατε.

    ```console
    cd finetune-phi
    ```

#### Δημιουργία εικονικού περιβάλλοντος

1. Πληκτρολογήστε την ακόλουθη εντολή μέσα στο τερματικό για να δημιουργήσετε ένα εικονικό περιβάλλον με όνομα *.venv*.
    ```console
    python -m venv .venv
    ```

2. Πληκτρολογήστε την ακόλουθη εντολή μέσα στο τερματικό σας για να ενεργοποιήσετε το εικονικό περιβάλλον.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Εάν λειτούργησε, θα πρέπει να δείτε το *(.venv)* πριν από τη γραμμή εντολών.

#### Εγκατάσταση των απαιτούμενων πακέτων

1. Πληκτρολογήστε τις ακόλουθες εντολές μέσα στο τερματικό σας για να εγκαταστήσετε τα απαιτούμενα πακέτα.

    ```console
    pip install datasets==2.19.1
    ```

#### Δημιουργία `donload_dataset.py`

> [!NOTE]
> Ολοκληρωμένη δομή φακέλου:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Ανοίξτε το **Visual Studio Code**.

1. Επιλέξτε **File** από τη γραμμή μενού.

1. Επιλέξτε **Open Folder**.

1. Επιλέξτε το φάκελο *finetune-phi* που δημιουργήσατε, ο οποίος βρίσκεται στο *C:\Users\yourUserName\finetune-phi*.

    ![Select the folder that you created.](../../../../../../translated_images/el/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Στην αριστερή πλαϊνή μπάρα του Visual Studio Code, κάντε δεξί κλικ και επιλέξτε **New File** για να δημιουργήσετε ένα νέο αρχείο με όνομα *download_dataset.py*.

    ![Create a new file.](../../../../../../translated_images/el/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Προετοιμασία του συνόλου δεδομένων για fine-tuning

Σε αυτή την άσκηση, θα εκτελέσετε το αρχείο *download_dataset.py* για να κατεβάσετε τα σύνολα δεδομένων *ultrachat_200k* στο τοπικό σας περιβάλλον. Στη συνέχεια, θα χρησιμοποιήσετε αυτά τα σύνολα δεδομένων για να κάνετε fine-tuning του μοντέλου Phi-3 στο Azure Machine Learning.

Σε αυτή την άσκηση, θα:

- Προσθέσετε κώδικα στο αρχείο *download_dataset.py* για να κατεβάσετε τα σύνολα δεδομένων.
- Εκτελέσετε το αρχείο *download_dataset.py* για να κατεβάσετε τα σύνολα δεδομένων στο τοπικό σας περιβάλλον.

#### Κατέβασμα του συνόλου δεδομένων σας χρησιμοποιώντας το *download_dataset.py*

1. Ανοίξτε το αρχείο *download_dataset.py* στο Visual Studio Code.

1. Προσθέστε τον ακόλουθο κώδικα μέσα στο αρχείο *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Φόρτωση του συνόλου δεδομένων με το καθορισμένο όνομα, διαμόρφωση και αναλογία διαχωρισμού
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Διαχωρισμός του συνόλου δεδομένων σε σύνολα εκπαίδευσης και δοκιμής (80% εκπαίδευση, 20% δοκιμή)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Δημιουργία του καταλόγου αν δεν υπάρχει
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Άνοιγμα του αρχείου σε λειτουργία εγγραφής
        with open(filepath, 'w', encoding='utf-8') as f:
            # Επανάληψη για κάθε εγγραφή στο σύνολο δεδομένων
            for record in dataset:
                # Εξαγωγή της εγγραφής ως αντικείμενο JSON και εγγραφή στο αρχείο
                json.dump(record, f)
                # Εγγραφή χαρακτήρα νέας γραμμής για διαχωρισμό εγγραφών
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Φόρτωση και διαχωρισμός του συνόλου δεδομένων ULTRACHAT_200k με συγκεκριμένη διαμόρφωση και αναλογία διαχωρισμού
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Εξαγωγή των συνόλων εκπαίδευσης και δοκιμής από τον διαχωρισμό
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Αποθήκευση του συνόλου εκπαίδευσης σε αρχείο JSONL
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Αποθήκευση του συνόλου δοκιμής σε ξεχωριστό αρχείο JSONL
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Πληκτρολογήστε την ακόλουθη εντολή μέσα στο τερματικό σας για να εκτελέσετε το script και να κατεβάσετε το σύνολο δεδομένων στο τοπικό σας περιβάλλον.

    ```console
    python download_dataset.py
    ```

1. Επιβεβαιώστε ότι τα σύνολα δεδομένων αποθηκεύτηκαν επιτυχώς στον τοπικό φάκελο *finetune-phi/data*.

> [!NOTE]
>
> #### Σημείωση σχετικά με το μέγεθος του συνόλου δεδομένων και τον χρόνο fine-tuning
>
> Σε αυτό το σεμινάριο, χρησιμοποιείτε μόνο το 1% του συνόλου δεδομένων (`split='train[:1%]'`). Αυτό μειώνει σημαντικά τον όγκο των δεδομένων, επιταχύνοντας τόσο τη διαδικασία ανέβασματος όσο και τη διαδικασία fine-tuning. Μπορείτε να ρυθμίσετε το ποσοστό για να βρείτε τη σωστή ισορροπία μεταξύ χρόνου εκπαίδευσης και απόδοσης του μοντέλου. Η χρήση μικρότερου υποσυνόλου του συνόλου δεδομένων μειώνει τον χρόνο που απαιτείται για το fine-tuning, καθιστώντας τη διαδικασία πιο διαχειρίσιμη για ένα σεμινάριο.

## Σενάριο 2: Κάντε fine-tuning στο μοντέλο Phi-3 και Ανάπτυξη στο Azure Machine Learning Studio

### Κάντε fine-tuning στο μοντέλο Phi-3

Σε αυτή την άσκηση, θα κάνετε fine-tuning στο μοντέλο Phi-3 στο Azure Machine Learning Studio.

Σε αυτή την άσκηση, θα:

- Δημιουργήσετε cluster υπολογιστών για το fine-tuning.
- Κάνετε fine-tuning στο μοντέλο Phi-3 στο Azure Machine Learning Studio.

#### Δημιουργία cluster υπολογιστών για fine-tuning

1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Επιλέξτε **Compute** από την αριστερή καρτέλα.

1. Επιλέξτε **Compute clusters** από το μενού πλοήγησης.

1. Επιλέξτε **+ New**.

    ![Select compute.](../../../../../../translated_images/el/06-01-select-compute.a29cff290b480252.webp)

1. Εκτελέστε τις εξής ενέργειες:

    - Επιλέξτε την **Περιοχή** που θα χρησιμοποιήσετε.
    - Επιλέξτε το **Virtual machine tier** σε **Dedicated**.
    - Επιλέξτε το **Virtual machine type** σε **GPU**.
    - Επιλέξτε το φίλτρο **Virtual machine size** σε **Select from all options**.
    - Επιλέξτε το **Virtual machine size** σε **Standard_NC24ads_A100_v4**.

    ![Create cluster.](../../../../../../translated_images/el/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Επιλέξτε **Next**.

1. Εκτελέστε τις εξής ενέργειες:

    - Εισάγετε **Compute name**. Πρέπει να είναι μοναδική τιμή.
    - Επιλέξτε τον **Ελάχιστο αριθμό κόμβων** σε **0**.
    - Επιλέξτε τον **Μέγιστο αριθμό κόμβων** σε **1**.
    - Επιλέξτε την **Αδράνεια προ της κλιμάκωσης προς τα κάτω** σε **120**.

    ![Create cluster.](../../../../../../translated_images/el/06-03-create-cluster.4a54ba20914f3662.webp)

1. Επιλέξτε **Create**.

#### Κάντε fine-tuning στο μοντέλο Phi-3

1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Επιλέξτε τον χώρο εργασίας Azure Machine Learning που δημιουργήσατε.

    ![Select workspace that you created.](../../../../../../translated_images/el/06-04-select-workspace.a92934ac04f4f181.webp)

1. Εκτελέστε τις εξής ενέργειες:

    - Επιλέξτε **Model catalog** από την αριστερή καρτέλα.
    - Πληκτρολογήστε *phi-3-mini-4k* στη **γραμμή αναζήτησης** και επιλέξτε **Phi-3-mini-4k-instruct** από τις επιλογές που εμφανίζονται.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/el/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Επιλέξτε **Fine-tune** από το μενού πλοήγησης.

    ![Select fine tune.](../../../../../../translated_images/el/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Εκτελέστε τις εξής ενέργειες:

    - Επιλέξτε **Select task type** σε **Chat completion**.
    - Επιλέξτε **+ Select data** για να ανεβάσετε τα **Training data**.
    - Ορίστε τον τύπο ανέβασμα των Validation data σε **Provide different validation data**.
    - Επιλέξτε **+ Select data** για να ανεβάσετε τα **Validation data**.

    ![Fill fine-tuning page.](../../../../../../translated_images/el/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Μπορείτε να επιλέξετε **Advanced settings** για να προσαρμόσετε ρυθμίσεις όπως **learning_rate** και **lr_scheduler_type** ώστε να βελτιστοποιήσετε τη διαδικασία fine-tuning σύμφωνα με τις συγκεκριμένες ανάγκες σας.

1. Επιλέξτε **Finish**.

1. Σε αυτή την άσκηση, ολοκληρώσατε με επιτυχία το fine-tuning του μοντέλου Phi-3 χρησιμοποιώντας το Azure Machine Learning. Σημειώστε ότι η διαδικασία fine-tuning μπορεί να πάρει σημαντικό χρόνο. Μετά την εκτέλεση της εργασίας fine-tuning, πρέπει να περιμένετε να ολοκληρωθεί. Μπορείτε να παρακολουθείτε την κατάσταση της εργασίας fine-tuning μεταβαίνοντας στην καρτέλα Jobs στην αριστερή πλευρά του χώρου εργασίας Azure Machine Learning. Στην επόμενη σειρά, θα αναπτύξετε το μοντέλο fine-tuned και θα το ενσωματώσετε με το Prompt flow.

    ![See finetuning job.](../../../../../../translated_images/el/06-08-output.2bd32e59930672b1.webp)

### Ανάπτυξη του fine-tuned μοντέλου Phi-3

Για να ενσωματώσετε το fine-tuned μοντέλο Phi-3 με το Prompt flow, πρέπει να αναπτύξετε το μοντέλο ώστε να είναι προσβάσιμο για πραγματικό χρόνο inferencing. Αυτή η διαδικασία περιλαμβάνει την εγγραφή του μοντέλου, τη δημιουργία online endpoint, και την ανάπτυξη του μοντέλου.

Σε αυτή την άσκηση, θα:

- Εγγράψετε το fine-tuned μοντέλο στον χώρο εργασίας Azure Machine Learning.
- Δημιουργήσετε ένα online endpoint.
- Αναπτύξετε το εγγεγραμμένο fine-tuned μοντέλο Phi-3.

#### Εγγραφή του fine-tuned μοντέλου

1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Επιλέξτε τον χώρο εργασίας Azure Machine Learning που δημιουργήσατε.

    ![Select workspace that you created.](../../../../../../translated_images/el/06-04-select-workspace.a92934ac04f4f181.webp)

1. Επιλέξτε **Models** από την αριστερή καρτέλα.
1. Επιλέξτε **+ Register**.
1. Επιλέξτε **From a job output**.

    ![Register model.](../../../../../../translated_images/el/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Επιλέξτε την εργασία που δημιουργήσατε.

    ![Select job.](../../../../../../translated_images/el/07-02-select-job.3e2e1144cd6cd093.webp)

1. Επιλέξτε **Next**.

1. Επιλέξτε τον **Τύπο μοντέλου** σε **MLflow**.

1. Βεβαιωθείτε ότι το **Job output** είναι επιλεγμένο· θα πρέπει να επιλέγεται αυτόματα.

    ![Select output.](../../../../../../translated_images/el/07-03-select-output.4cf1a0e645baea1f.webp)

2. Επιλέξτε **Next**.

3. Επιλέξτε **Register**.

    ![Select register.](../../../../../../translated_images/el/07-04-register.fd82a3b293060bc7.webp)

4. Μπορείτε να δείτε το εγγεγραμμένο σας μοντέλο μεταβαίνοντας στο μενού **Models** από την αριστερή καρτέλα.

    ![Registered model.](../../../../../../translated_images/el/07-05-registered-model.7db9775f58dfd591.webp)

#### Ανάπτυξη του fine-tuned μοντέλου

1. Μεταβείτε στον χώρο εργασίας Azure Machine Learning που δημιουργήσατε.

1. Επιλέξτε **Endpoints** από την αριστερή καρτέλα.

1. Επιλέξτε **Real-time endpoints** από το μενού πλοήγησης.

    ![Create endpoint.](../../../../../../translated_images/el/07-06-create-endpoint.1ba865c606551f09.webp)

1. Επιλέξτε **Create**.

1. Επιλέξτε το εγγεγραμμένο μοντέλο που δημιουργήσατε.

    ![Select registered model.](../../../../../../translated_images/el/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Επιλέξτε **Select**.

1. Εκτελέστε τις ακόλουθες ενέργειες:

    - Επιλέξτε **Virtual machine** σε *Standard_NC6s_v3*.
    - Επιλέξτε τον **Αριθμό περιπτώσεων (Instance count)** που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, *1*.
    - Ορίστε το **Endpoint** σε **New** για να δημιουργήσετε ένα νέο endpoint.
    - Εισάγετε το **Όνομα Endpoint**. Πρέπει να είναι μοναδική τιμή.
    - Εισάγετε το **Όνομα Ανάπτυξης (Deployment name)**. Πρέπει να είναι μοναδική τιμή.

    ![Fill the deployment setting.](../../../../../../translated_images/el/07-08-deployment-setting.43ddc4209e673784.webp)

1. Επιλέξτε **Deploy**.

> [!WARNING]
> Για να αποφύγετε επιπλέον χρεώσεις στο λογαριασμό σας, βεβαιωθείτε ότι έχετε διαγράψει το δημιουργημένο endpoint στον χώρο εργασίας Azure Machine Learning.
>

#### Έλεγχος κατάστασης ανάπτυξης στο Azure Machine Learning Workspace

1. Μεταβείτε στον χώρο εργασίας Azure Machine Learning που δημιουργήσατε.

1. Επιλέξτε **Endpoints** από την αριστερή καρτέλα.

1. Επιλέξτε το endpoint που δημιουργήσατε.

    ![Select endpoints](../../../../../../translated_images/el/07-09-check-deployment.325d18cae8475ef4.webp)

1. Σε αυτή τη σελίδα, μπορείτε να διαχειριστείτε τα endpoints κατά τη διάρκεια της διαδικασίας ανάπτυξης.

> [!NOTE]
> Μόλις ολοκληρωθεί η ανάπτυξη, βεβαιωθείτε ότι η επιλογή **Live traffic** είναι ρυθμισμένη στο **100%**. Αν δεν είναι, επιλέξτε **Update traffic** για να προσαρμόσετε τις ρυθμίσεις κυκλοφορίας. Σημειώστε ότι δεν μπορείτε να δοκιμάσετε το μοντέλο αν η κυκλοφορία είναι στο 0%.
>
> ![Set traffic.](../../../../../../translated_images/el/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Σενάριο 3: Ενσωμάτωση με Prompt flow και συνομιλία με το προσαρμοσμένο μοντέλο σας στο Microsoft Foundry

### Ενσωμάτωση του προσαρμοσμένου μοντέλου Phi-3 με Prompt flow

Αφού αναπτύξετε επιτυχώς το fine-tuned μοντέλο σας, μπορείτε τώρα να το ενσωματώσετε με το Prompt Flow για να χρησιμοποιήσετε το μοντέλο σας σε εφαρμογές πραγματικού χρόνου, επιτρέποντας μια ποικιλία διαδραστικών εργασιών με το προσαρμοσμένο μοντέλο Phi-3.

Σε αυτή την άσκηση, θα:

- Δημιουργήσετε Microsoft Foundry Hub.
- Δημιουργήσετε Microsoft Foundry Project.
- Δημιουργήσετε Prompt flow.
- Προσθέσετε μια προσαρμοσμένη σύνδεση για το fine-tuned μοντέλο Phi-3.
- Ρυθμίσετε το Prompt flow για να συνομιλεί με το προσαρμοσμένο μοντέλο Phi-3.

> [!NOTE]
> Μπορείτε επίσης να ενσωματώσετε με το Promptflow χρησιμοποιώντας το Azure ML Studio. Η ίδια διαδικασία ενσωμάτωσης μπορεί να εφαρμοστεί και στο Azure ML Studio.

#### Δημιουργία Microsoft Foundry Hub

Πρέπει να δημιουργήσετε ένα Hub πριν δημιουργήσετε το Project. Ένα Hub λειτουργεί ως Resource Group, επιτρέποντάς σας να οργανώσετε και να διαχειριστείτε πολλαπλά Projects μέσα στο Microsoft Foundry.
1. Επισκεφτείτε το [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Επιλέξτε **Όλοι οι κόμβοι** από την καρτέλα στην αριστερή πλευρά.

1. Επιλέξτε **+ Νέος κόμβος** από το μενού πλοήγησης.

    ![Create hub.](../../../../../../translated_images/el/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Εκτελέστε τις ακόλουθες εργασίες:

    - Εισαγάγετε **Όνομα κόμβου**. Πρέπει να είναι μια μοναδική τιμή.
    - Επιλέξτε την **Συνδρομή** Azure.
    - Επιλέξτε την **Ομάδα πόρων** που θα χρησιμοποιήσετε (δημιουργήστε νέα αν χρειάζεται).
    - Επιλέξτε την **Τοποθεσία** που θέλετε να χρησιμοποιήσετε.
    - Επιλέξτε την **Σύνδεση με υπηρεσίες AI Azure** που θα χρησιμοποιήσετε (δημιουργήστε νέα αν χρειάζεται).
    - Επιλέξτε **Σύνδεση με Azure AI Search** για **Παράλειψη σύνδεσης**.

    ![Fill hub.](../../../../../../translated_images/el/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Επιλέξτε **Επόμενο**.

#### Δημιουργία έργου Microsoft Foundry

1. Στον κόμβο που δημιουργήσατε, επιλέξτε **Όλα τα έργα** από την καρτέλα στην αριστερή πλευρά.

1. Επιλέξτε **+ Νέο έργο** από το μενού πλοήγησης.

    ![Select new project.](../../../../../../translated_images/el/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Εισαγάγετε **Όνομα έργου**. Πρέπει να είναι μια μοναδική τιμή.

    ![Create project.](../../../../../../translated_images/el/08-05-create-project.4d97f0372f03375a.webp)

1. Επιλέξτε **Δημιουργία έργου**.

#### Προσθήκη προσαρμοσμένης σύνδεσης για το fine-tuned μοντέλο Phi-3

Για να ενσωματώσετε το προσαρμοσμένο μοντέλο Phi-3 με το Prompt flow, πρέπει να αποθηκεύσετε το endpoint και το κλειδί του μοντέλου σε μια προσαρμοσμένη σύνδεση. Αυτή η ρύθμιση εξασφαλίζει την πρόσβαση στο προσαρμοσμένο μοντέλο Phi-3 μέσα στο Prompt flow.

#### Ρύθμιση api key και endpoint uri του fine-tuned μοντέλου Phi-3

1. Επισκεφτείτε το [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Μεταβείτε στον χώρο εργασίας Azure Machine learning που δημιουργήσατε.

1. Επιλέξτε **Endpoints** από την καρτέλα στην αριστερή πλευρά.

    ![Select endpoints.](../../../../../../translated_images/el/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Επιλέξτε το endpoint που δημιουργήσατε.

    ![Select endpoints.](../../../../../../translated_images/el/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Επιλέξτε **Κατανάλωση** από το μενού πλοήγησης.

1. Αντιγράψτε το **REST endpoint** και το **Πρωτεύον κλειδί** σας.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/el/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Προσθήκη της προσαρμοσμένης σύνδεσης

1. Επισκεφτείτε το [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Μεταβείτε στο έργο Microsoft Foundry που δημιουργήσατε.

1. Στο έργο που δημιουργήσατε, επιλέξτε **Ρυθμίσεις** από την καρτέλα στην αριστερή πλευρά.

1. Επιλέξτε **+ Νέα σύνδεση**.

    ![Select new connection.](../../../../../../translated_images/el/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Επιλέξτε **Προσαρμοσμένα κλειδιά** από το μενού πλοήγησης.

    ![Select custom keys.](../../../../../../translated_images/el/08-10-select-custom-keys.856f6b2966460551.webp)

1. Εκτελέστε τις ακόλουθες εργασίες:

    - Επιλέξτε **+ Προσθήκη ζευγών κλειδιών-τιμών**.
    - Για το όνομα του κλειδιού, εισαγάγετε **endpoint** και επικολλήστε το endpoint που αντιγράψατε από το Azure ML Studio στο πεδίο τιμής.
    - Επιλέξτε ξανά **+ Προσθήκη ζευγών κλειδιών-τιμών**.
    - Για το όνομα του κλειδιού, εισαγάγετε **key** και επικολλήστε το κλειδί που αντιγράψατε από το Azure ML Studio στο πεδίο τιμής.
    - Αφού προσθέσετε τα κλειδιά, επιλέξτε **is secret** για να αποτρέψετε την έκθεση του κλειδιού.

    ![Add connection.](../../../../../../translated_images/el/08-11-add-connection.785486badb4d2d26.webp)

1. Επιλέξτε **Προσθήκη σύνδεσης**.

#### Δημιουργία Prompt flow

Έχετε προσθέσει μια προσαρμοσμένη σύνδεση στο Microsoft Foundry. Τώρα, ας δημιουργήσουμε ένα Prompt flow χρησιμοποιώντας τα παρακάτω βήματα. Στη συνέχεια, θα συνδέσετε αυτό το Prompt flow με την προσαρμοσμένη σύνδεση ώστε να μπορείτε να χρησιμοποιήσετε το fine-tuned μοντέλο μέσα στο Prompt flow.

1. Μεταβείτε στο έργο Microsoft Foundry που δημιουργήσατε.

1. Επιλέξτε **Prompt flow** από την καρτέλα στην αριστερή πλευρά.

1. Επιλέξτε **+ Δημιουργία** από το μενού πλοήγησης.

    ![Select Promptflow.](../../../../../../translated_images/el/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Επιλέξτε **Chat flow** από το μενού πλοήγησης.

    ![Select chat flow.](../../../../../../translated_images/el/08-13-select-flow-type.2ec689b22da32591.webp)

1. Εισαγάγετε **Όνομα φακέλου** για χρήση.

    ![Enter name.](../../../../../../translated_images/el/08-14-enter-name.ff9520fefd89f40d.webp)

2. Επιλέξτε **Δημιουργία**.

#### Ρύθμιση Prompt flow για συνομιλία με το προσαρμοσμένο μοντέλο Phi-3

Πρέπει να ενσωματώσετε το fine-tuned μοντέλο Phi-3 σε ένα Prompt flow. Ωστόσο, το υπάρχον Prompt flow που παρέχεται δεν είναι σχεδιασμένο για αυτόν τον σκοπό. Επομένως, πρέπει να επανασχεδιάσετε το Prompt flow ώστε να επιτραπεί η ενσωμάτωση του προσαρμοσμένου μοντέλου.

1. Στο Prompt flow, εκτελέστε τις ακόλουθες εργασίες για να αναδημιουργήσετε τη ροή που υπάρχει:

    - Επιλέξτε **Κατάσταση ακατέργαστου αρχείου**.
    - Διαγράψτε όλο τον υπάρχοντα κώδικα στο αρχείο *flow.dag.yml*.
    - Προσθέστε τον ακόλουθο κώδικα στο αρχείο *flow.dag.yml*.

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - Επιλέξτε **Αποθήκευση**.

    ![Select raw file mode.](../../../../../../translated_images/el/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Προσθέστε τον ακόλουθο κώδικα στο αρχείο *integrate_with_promptflow.py* για να χρησιμοποιήσετε το προσαρμοσμένο μοντέλο Phi-3 στο Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Ρύθμιση καταγραφής
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" είναι το όνομα της Προσαρμοσμένης Σύνδεσης, "endpoint", "key" είναι τα κλειδιά στην Προσαρμοσμένη Σύνδεση
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Καταγράψτε την πλήρη απόκριση JSON
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../../../translated_images/el/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Για περισσότερες λεπτομερείς πληροφορίες σχετικά με τη χρήση του Prompt flow στο Microsoft Foundry, μπορείτε να ανατρέξετε στο [Prompt flow στο Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Επιλέξτε **Είσοδος συνομιλίας**, **Έξοδος συνομιλίας** για να ενεργοποιήσετε τη συνομιλία με το μοντέλο σας.

    ![Input Output.](../../../../../../translated_images/el/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Τώρα είστε έτοιμοι να συνομιλήσετε με το προσαρμοσμένο μοντέλο Phi-3. Στην επόμενη άσκηση, θα μάθετε πώς να ξεκινήσετε το Prompt flow και να το χρησιμοποιήσετε για να συνομιλήσετε με το fine-tuned μοντέλο Phi-3.

> [!NOTE]
>
> Η ανακατασκευασμένη ροή θα πρέπει να μοιάζει με την παρακάτω εικόνα:
>
> ![Flow example.](../../../../../../translated_images/el/08-18-graph-example.d6457533952e690c.webp)
>

### Συνομιλία με το προσαρμοσμένο μοντέλο Phi-3

Τώρα που έχετε fine-tune και ενσωματώσει το προσαρμοσμένο μοντέλο Phi-3 με το Prompt flow, είστε έτοιμοι να ξεκινήσετε την αλληλεπίδραση μαζί του. Αυτή η άσκηση θα σας καθοδηγήσει στη διαδικασία ρύθμισης και εκκίνησης μιας συνομιλίας με το μοντέλο σας χρησιμοποιώντας το Prompt flow. Ακολουθώντας αυτά τα βήματα, θα μπορείτε να αξιοποιήσετε πλήρως τις δυνατότητες του fine-tuned μοντέλου Phi-3 για διάφορες εργασίες και συζητήσεις.

- Συνομιλήστε με το προσαρμοσμένο μοντέλο Phi-3 χρησιμοποιώντας το Prompt flow.

#### Εκκίνηση Prompt flow

1. Επιλέξτε **Έναρξη συνεδριών υπολογισμού** για να ξεκινήσετε το Prompt flow.

    ![Start compute session.](../../../../../../translated_images/el/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Επιλέξτε **Επικύρωση και ανάλυση εισόδου** για ανανέωση παραμέτρων.

    ![Validate input.](../../../../../../translated_images/el/09-02-validate-input.317c76ef766361e9.webp)

1. Επιλέξτε την **Τιμή** της **σύνδεσης** στην προσαρμοσμένη σύνδεση που δημιουργήσατε. Για παράδειγμα, *connection*.

    ![Connection.](../../../../../../translated_images/el/09-03-select-connection.99bdddb4b1844023.webp)

#### Συνομιλία με το προσαρμοσμένο μοντέλο σας

1. Επιλέξτε **Συνομιλία**.

    ![Select chat.](../../../../../../translated_images/el/09-04-select-chat.61936dce6612a1e6.webp)

1. Ακολουθεί ένα παράδειγμα αποτελεσμάτων: Τώρα μπορείτε να συνομιλήσετε με το προσαρμοσμένο μοντέλο Phi-3. Συνιστάται να κάνετε ερωτήσεις βασισμένες στα δεδομένα που χρησιμοποιήθηκαν για το fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/el/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να σημειώσετε ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται η επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για οποιεσδήποτε παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->