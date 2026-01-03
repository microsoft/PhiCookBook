<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-17T01:28:33+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "el"
}
-->
# Fine-tune και Ενσωμάτωση προσαρμοσμένων μοντέλων Phi-3 με το Prompt flow στο Azure AI Foundry

Αυτό το ολοκληρωμένο (E2E) παράδειγμα βασίζεται στον οδηγό "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" από την κοινότητα Microsoft Tech Community. Παρουσιάζει τις διαδικασίες fine-tuning, ανάπτυξης και ενσωμάτωσης προσαρμοσμένων μοντέλων Phi-3 με το Prompt flow στο Azure AI Foundry.  
Σε αντίθεση με το E2E παράδειγμα, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", που περιελάμβανε εκτέλεση κώδικα τοπικά, αυτό το σεμινάριο εστιάζει αποκλειστικά στο fine-tuning και την ενσωμάτωση του μοντέλου σας μέσα στο Azure AI / ML Studio.

## Επισκόπηση

Σε αυτό το E2E παράδειγμα, θα μάθετε πώς να κάνετε fine-tune το μοντέλο Phi-3 και να το ενσωματώσετε με το Prompt flow στο Azure AI Foundry. Αξιοποιώντας το Azure AI / ML Studio, θα δημιουργήσετε μια ροή εργασίας για την ανάπτυξη και χρήση προσαρμοσμένων μοντέλων AI. Το παράδειγμα χωρίζεται σε τρία σενάρια:

**Σενάριο 1: Ρύθμιση πόρων Azure και Προετοιμασία για fine-tuning**

**Σενάριο 2: Fine-tune του μοντέλου Phi-3 και Ανάπτυξη στο Azure Machine Learning Studio**

**Σενάριο 3: Ενσωμάτωση με το Prompt flow και Συνομιλία με το προσαρμοσμένο μοντέλο σας στο Azure AI Foundry**

Ακολουθεί μια επισκόπηση αυτού του E2E παραδείγματος.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a.el.png)

### Πίνακας Περιεχομένων

1. **[Σενάριο 1: Ρύθμιση πόρων Azure και Προετοιμασία για fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Δημιουργία Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Αίτηση για GPU quotas στο Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Προσθήκη ανάθεσης ρόλου](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ρύθμιση έργου](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Προετοιμασία dataset για fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Σενάριο 2: Fine-tune του μοντέλου Phi-3 και Ανάπτυξη στο Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Fine-tune του μοντέλου Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ανάπτυξη του fine-tuned μοντέλου Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Σενάριο 3: Ενσωμάτωση με το Prompt flow και Συνομιλία με το προσαρμοσμένο μοντέλο σας στο Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Ενσωμάτωση του προσαρμοσμένου μοντέλου Phi-3 με το Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Συνομιλία με το προσαρμοσμένο μοντέλο Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Σενάριο 1: Ρύθμιση πόρων Azure και Προετοιμασία για fine-tuning

### Δημιουργία Azure Machine Learning Workspace

1. Πληκτρολογήστε *azure machine learning* στη **γραμμή αναζήτησης** στο πάνω μέρος της σελίδας του portal και επιλέξτε **Azure Machine Learning** από τις επιλογές που εμφανίζονται.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b.el.png)

2. Επιλέξτε **+ Create** από το μενού πλοήγησης.

3. Επιλέξτε **New workspace** από το μενού πλοήγησης.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2.el.png)

4. Εκτελέστε τις παρακάτω ενέργειες:

    - Επιλέξτε το Azure **Subscription** σας.
    - Επιλέξτε την **Resource group** που θα χρησιμοποιήσετε (δημιουργήστε νέα αν χρειάζεται).
    - Εισάγετε το **Workspace Name**. Πρέπει να είναι μοναδικό.
    - Επιλέξτε την **Περιοχή (Region)** που θέλετε να χρησιμοποιήσετε.
    - Επιλέξτε τον **Λογαριασμό αποθήκευσης (Storage account)** που θα χρησιμοποιήσετε (δημιουργήστε νέο αν χρειάζεται).
    - Επιλέξτε το **Key vault** που θα χρησιμοποιήσετε (δημιουργήστε νέο αν χρειάζεται).
    - Επιλέξτε το **Application insights** που θα χρησιμοποιήσετε (δημιουργήστε νέο αν χρειάζεται).
    - Επιλέξτε το **Container registry** που θα χρησιμοποιήσετε (δημιουργήστε νέο αν χρειάζεται).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090f.el.png)

5. Επιλέξτε **Review + Create**.

6. Επιλέξτε **Create**.

### Αίτηση για GPU quotas στο Azure Subscription

Σε αυτό το σεμινάριο, θα μάθετε πώς να κάνετε fine-tune και να αναπτύξετε ένα μοντέλο Phi-3, χρησιμοποιώντας GPUs. Για το fine-tuning, θα χρησιμοποιήσετε την GPU *Standard_NC24ads_A100_v4*, που απαιτεί αίτηση για quota. Για την ανάπτυξη, θα χρησιμοποιήσετε την GPU *Standard_NC6s_v3*, που επίσης απαιτεί αίτηση για quota.

> [!NOTE]
>
> Μόνο οι συνδρομές τύπου Pay-As-You-Go (τυπικός τύπος συνδρομής) είναι επιλέξιμες για κατανομή GPU· οι συνδρομές με οφέλη δεν υποστηρίζονται προς το παρόν.
>

1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Εκτελέστε τις παρακάτω ενέργειες για να ζητήσετε quota για την οικογένεια *Standard NCADSA100v4*:

    - Επιλέξτε **Quota** από την αριστερή καρτέλα.
    - Επιλέξτε την **οικογένεια εικονικών μηχανών (Virtual machine family)** που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, επιλέξτε **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, που περιλαμβάνει την GPU *Standard_NC24ads_A100_v4*.
    - Επιλέξτε **Request quota** από το μενού πλοήγησης.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd5.el.png)

    - Στη σελίδα Request quota, εισάγετε το **Νέο όριο πυρήνων (New cores limit)** που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, 24.
    - Στη σελίδα Request quota, επιλέξτε **Submit** για να υποβάλετε το αίτημα για το quota GPU.

1. Εκτελέστε τις παρακάτω ενέργειες για να ζητήσετε quota για την οικογένεια *Standard NCSv3*:

    - Επιλέξτε **Quota** από την αριστερή καρτέλα.
    - Επιλέξτε την **οικογένεια εικονικών μηχανών (Virtual machine family)** που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, επιλέξτε **Standard NCSv3 Family Cluster Dedicated vCPUs**, που περιλαμβάνει την GPU *Standard_NC6s_v3*.
    - Επιλέξτε **Request quota** από το μενού πλοήγησης.
    - Στη σελίδα Request quota, εισάγετε το **Νέο όριο πυρήνων (New cores limit)** που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, 24.
    - Στη σελίδα Request quota, επιλέξτε **Submit** για να υποβάλετε το αίτημα για το quota GPU.

### Προσθήκη ανάθεσης ρόλου

Για να κάνετε fine-tune και να αναπτύξετε τα μοντέλα σας, πρέπει πρώτα να δημιουργήσετε μια User Assigned Managed Identity (UAI) και να της αναθέσετε τα κατάλληλα δικαιώματα. Αυτή η UAI θα χρησιμοποιηθεί για την αυθεντικοποίηση κατά την ανάπτυξη.

#### Δημιουργία User Assigned Managed Identity (UAI)

1. Πληκτρολογήστε *managed identities* στη **γραμμή αναζήτησης** στο πάνω μέρος της σελίδας του portal και επιλέξτε **Managed Identities** από τις επιλογές που εμφανίζονται.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e5.el.png)

1. Επιλέξτε **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f2.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Επιλέξτε το Azure **Subscription** σας.
    - Επιλέξτε την **Resource group** που θα χρησιμοποιήσετε (δημιουργήστε νέα αν χρειάζεται).
    - Επιλέξτε την **Περιοχή (Region)** που θέλετε να χρησιμοποιήσετε.
    - Εισάγετε το **Όνομα (Name)**. Πρέπει να είναι μοναδικό.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0.el.png)

1. Επιλέξτε **Review + create**.

1. Επιλέξτε **+ Create**.

#### Προσθήκη ανάθεσης ρόλου Contributor στη Managed Identity

1. Μεταβείτε στον πόρο Managed Identity που δημιουργήσατε.

1. Επιλέξτε **Azure role assignments** από την αριστερή καρτέλα.

1. Επιλέξτε **+Add role assignment** από το μενού πλοήγησης.

1. Στη σελίδα Add role assignment, εκτελέστε τις παρακάτω ενέργειες:
    - Επιλέξτε το **Scope** σε **Resource group**.
    - Επιλέξτε το Azure **Subscription** σας.
    - Επιλέξτε την **Resource group** που θα χρησιμοποιήσετε.
    - Επιλέξτε το **Role** σε **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d.el.png)

2. Επιλέξτε **Save**.

#### Προσθήκη ανάθεσης ρόλου Storage Blob Data Reader στη Managed Identity

1. Πληκτρολογήστε *storage accounts* στη **γραμμή αναζήτησης** στο πάνω μέρος της σελίδας του portal και επιλέξτε **Storage accounts** από τις επιλογές που εμφανίζονται.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e5.el.png)

1. Επιλέξτε τον λογαριασμό αποθήκευσης που σχετίζεται με το Azure Machine Learning workspace που δημιουργήσατε. Για παράδειγμα, *finetunephistorage*.

1. Εκτελέστε τις παρακάτω ενέργειες για να μεταβείτε στη σελίδα Add role assignment:

    - Μεταβείτε στον λογαριασμό Azure Storage που δημιουργήσατε.
    - Επιλέξτε **Access Control (IAM)** από την αριστερή καρτέλα.
    - Επιλέξτε **+ Add** από το μενού πλοήγησης.
    - Επιλέξτε **Add role assignment** από το μενού πλοήγησης.

    ![Add role.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c2.el.png)

1. Στη σελίδα Add role assignment, εκτελέστε τις παρακάτω ενέργειες:

    - Στη σελίδα Role, πληκτρολογήστε *Storage Blob Data Reader* στη **γραμμή αναζήτησης** και επιλέξτε **Storage Blob Data Reader** από τις επιλογές που εμφανίζονται.
    - Στη σελίδα Role, επιλέξτε **Next**.
    - Στη σελίδα Members, επιλέξτε **Assign access to** **Managed identity**.
    - Στη σελίδα Members, επιλέξτε **+ Select members**.
    - Στη σελίδα Select managed identities, επιλέξτε το Azure **Subscription** σας.
    - Στη σελίδα Select managed identities, επιλέξτε τη **Managed identity** που δημιουργήσατε.
    - Στη σελίδα Select managed identities, επιλέξτε τη Managed Identity που δημιουργήσατε. Για παράδειγμα, *finetunephi-managedidentity*.
    - Στη σελίδα Select managed identities, επιλέξτε **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25.el.png)

1. Επιλέξτε **Review + assign**.

#### Προσθήκη ανάθεσης ρόλου AcrPull στη Managed Identity

1. Πληκτρολογήστε *container registries* στη **γραμμή αναζήτησης** στο πάνω μέρος της σελίδας του portal και επιλέξτε **Container registries** από τις επιλογές που εμφανίζονται.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a6.el.png)

1. Επιλέξτε το container registry που σχετίζεται με το Azure Machine Learning workspace. Για παράδειγμα, *finetunephicontainerregistry*

1. Εκτελέστε τις παρακάτω ενέργειες για να μεταβείτε στη σελίδα Add role assignment:

    - Επιλέξτε **Access Control (IAM)** από την αριστερή καρτέλα.
    - Επιλέξτε **+ Add** από το μενού πλοήγησης.
    - Επιλέξτε **Add role assignment** από το μενού πλοήγησης.

1. Στη σελίδα Add role assignment, εκτελέστε τις παρακάτω ενέργειες:

    - Στη σελίδα Role, πληκτρολογήστε *AcrPull* στη **γραμμή αναζήτησης** και επιλέξτε **AcrPull** από τις επιλογές που εμφανίζονται.
    - Στη σελίδα Role, επιλέξτε **Next**.
    - Στη σελίδα Members, επιλέξτε **Assign access to** **Managed identity**.
    - Στη σελίδα Members, επιλέξτε **+ Select members**.
    - Στη σελίδα Select managed identities, επιλέξτε το Azure **Subscription** σας.
    - Στη σελίδα Select managed identities, επιλέξτε τη **Managed identity** που δημιουργήσατε.
    - Στη σελίδα Select managed identities, επιλέξτε τη Managed Identity που δημιουργήσατε. Για παράδειγμα, *finetunephi-managedidentity*.
    - Στη σελίδα Select managed identities, επιλέξτε **Select**.
    - Επιλέξτε **Review + assign**.

### Ρύθμιση έργου

Για να κατεβάσετε τα datasets που χρειάζονται για το fine-tuning, θα ρυθμίσετε ένα τοπικό περιβάλλον.

Σε αυτή την άσκηση, θα

- Δημιουργήσετε έναν φάκελο για να εργαστείτε μέσα σε αυτόν.
- Δημιουργήσετε ένα virtual environment.
- Εγκαταστήσετε τα απαιτούμενα πακέτα.
- Δημιουργήσετε ένα αρχείο *download_dataset.py* για να κατεβάσετε το dataset.

#### Δημιουργία φακέλου για εργασία

1. Ανοίξτε ένα παράθυρο τερματικού και πληκτρολογήστε την παρακάτω εντολή για να δημιουργήσετε έναν φάκελο με όνομα *finetune-phi* στην προεπιλεγμένη διαδρομή.

    ```console
    mkdir finetune-phi
    ```

2. Πληκτρολογήστε την παρακάτω εντολή μέσα στο τερματικό σας για να μεταβείτε στον φάκελο *finetune-phi* που δημιουργήσατε.
#### Δημιουργία εικονικού περιβάλλοντος

1. Πληκτρολογήστε την παρακάτω εντολή στο τερματικό σας για να δημιουργήσετε ένα εικονικό περιβάλλον με όνομα *.venv*.

    ```console
    python -m venv .venv
    ```

2. Πληκτρολογήστε την παρακάτω εντολή στο τερματικό σας για να ενεργοποιήσετε το εικονικό περιβάλλον.

    ```console
    .venv\Scripts\activate.bat
    ```


> [!NOTE]
> Αν λειτούργησε, θα πρέπει να δείτε το *(.venv)* πριν από το prompt της εντολής.

#### Εγκατάσταση των απαιτούμενων πακέτων

1. Πληκτρολογήστε τις παρακάτω εντολές στο τερματικό σας για να εγκαταστήσετε τα απαιτούμενα πακέτα.

    ```console
    pip install datasets==2.19.1
    ```

#### Δημιουργία `download_dataset.py`

> [!NOTE]
> Πλήρης δομή φακέλων:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Ανοίξτε το **Visual Studio Code**.

1. Επιλέξτε **File** από τη γραμμή μενού.

1. Επιλέξτε **Open Folder**.

1. Επιλέξτε τον φάκελο *finetune-phi* που δημιουργήσατε, ο οποίος βρίσκεται στο *C:\Users\yourUserName\finetune-phi*.

    ![Επιλέξτε τον φάκελο που δημιουργήσατε.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6.el.png)

1. Στο αριστερό πάνελ του Visual Studio Code, κάντε δεξί κλικ και επιλέξτε **New File** για να δημιουργήσετε ένα νέο αρχείο με όνομα *download_dataset.py*.

    ![Δημιουργία νέου αρχείου.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff92.el.png)

### Προετοιμασία dataset για fine-tuning

Σε αυτή την άσκηση, θα εκτελέσετε το αρχείο *download_dataset.py* για να κατεβάσετε τα datasets *ultrachat_200k* στο τοπικό σας περιβάλλον. Στη συνέχεια, θα χρησιμοποιήσετε αυτά τα datasets για να κάνετε fine-tune το μοντέλο Phi-3 στο Azure Machine Learning.

Σε αυτή την άσκηση, θα:

- Προσθέσετε κώδικα στο αρχείο *download_dataset.py* για να κατεβάσετε τα datasets.
- Εκτελέσετε το αρχείο *download_dataset.py* για να κατεβάσετε τα datasets στο τοπικό σας περιβάλλον.

#### Κατεβάστε το dataset σας χρησιμοποιώντας το *download_dataset.py*

1. Ανοίξτε το αρχείο *download_dataset.py* στο Visual Studio Code.

1. Προσθέστε τον παρακάτω κώδικα στο αρχείο *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Load the dataset with the specified name, configuration, and split ratio
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Split the dataset into train and test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open the file in write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterate over each record in the dataset
            for record in dataset:
                # Dump the record as a JSON object and write it to the file
                json.dump(record, f)
                # Write a newline character to separate records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load and split the ULTRACHAT_200k dataset with a specific configuration and split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract the train and test datasets from the split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save the train dataset to a JSONL file
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Πληκτρολογήστε την παρακάτω εντολή στο τερματικό σας για να εκτελέσετε το script και να κατεβάσετε το dataset στο τοπικό σας περιβάλλον.

    ```console
    python download_dataset.py
    ```

1. Επιβεβαιώστε ότι τα datasets αποθηκεύτηκαν επιτυχώς στον τοπικό φάκελο *finetune-phi/data*.

> [!NOTE]
>
> #### Σημείωση σχετικά με το μέγεθος του dataset και τον χρόνο fine-tuning
>
> Σε αυτό το tutorial, χρησιμοποιείτε μόνο το 1% του dataset (`split='train[:1%]'`). Αυτό μειώνει σημαντικά τον όγκο των δεδομένων, επιταχύνοντας τόσο τη μεταφόρτωση όσο και τη διαδικασία fine-tuning. Μπορείτε να προσαρμόσετε το ποσοστό για να βρείτε την κατάλληλη ισορροπία μεταξύ χρόνου εκπαίδευσης και απόδοσης του μοντέλου. Η χρήση μικρότερου υποσυνόλου του dataset μειώνει τον χρόνο που απαιτείται για το fine-tuning, καθιστώντας τη διαδικασία πιο διαχειρίσιμη για ένα tutorial.

## Σενάριο 2: Fine-tune του μοντέλου Phi-3 και Ανάπτυξη στο Azure Machine Learning Studio

### Fine-tune του μοντέλου Phi-3

Σε αυτή την άσκηση, θα κάνετε fine-tune το μοντέλο Phi-3 στο Azure Machine Learning Studio.

Σε αυτή την άσκηση, θα:

- Δημιουργήσετε cluster υπολογιστών για fine-tuning.
- Κάνετε fine-tune το μοντέλο Phi-3 στο Azure Machine Learning Studio.

#### Δημιουργία cluster υπολογιστών για fine-tuning

1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Επιλέξτε **Compute** από την αριστερή καρτέλα.

1. Επιλέξτε **Compute clusters** από το μενού πλοήγησης.

1. Επιλέξτε **+ New**.

    ![Επιλέξτε compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Επιλέξτε την **Περιοχή** που θέλετε να χρησιμοποιήσετε.
    - Επιλέξτε το **Virtual machine tier** σε **Dedicated**.
    - Επιλέξτε τον **τύπο εικονικής μηχανής** σε **GPU**.
    - Επιλέξτε το φίλτρο **Virtual machine size** σε **Select from all options**.
    - Επιλέξτε το μέγεθος **Virtual machine size** σε **Standard_NC24ads_A100_v4**.

    ![Δημιουργία cluster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e.el.png)

1. Επιλέξτε **Next**.

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Εισάγετε το **Compute name**. Πρέπει να είναι μοναδικό.
    - Επιλέξτε τον **Ελάχιστο αριθμό κόμβων** σε **0**.
    - Επιλέξτε τον **Μέγιστο αριθμό κόμβων** σε **1**.
    - Επιλέξτε τα **Idle seconds before scale down** σε **120**.

    ![Δημιουργία cluster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662.el.png)

1. Επιλέξτε **Create**.

#### Fine-tune του μοντέλου Phi-3

1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Επιλέξτε το Azure Machine Learning workspace που δημιουργήσατε.

    ![Επιλέξτε το workspace που δημιουργήσατε.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f181.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Επιλέξτε **Model catalog** από την αριστερή καρτέλα.
    - Πληκτρολογήστε *phi-3-mini-4k* στη **γραμμή αναζήτησης** και επιλέξτε **Phi-3-mini-4k-instruct** από τις επιλογές που εμφανίζονται.

    ![Πληκτρολογήστε phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.el.png)

1. Επιλέξτε **Fine-tune** από το μενού πλοήγησης.

    ![Επιλέξτε fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeec.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Επιλέξτε **Select task type** σε **Chat completion**.
    - Επιλέξτε **+ Select data** για να ανεβάσετε τα **Training data**.
    - Επιλέξτε τον τύπο ανεβάσματος Validation data σε **Provide different validation data**.
    - Επιλέξτε **+ Select data** για να ανεβάσετε τα **Validation data**.

    ![Συμπληρώστε τη σελίδα fine-tuning.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0b.el.png)

    > [!TIP]
    >
    > Μπορείτε να επιλέξετε **Advanced settings** για να προσαρμόσετε ρυθμίσεις όπως **learning_rate** και **lr_scheduler_type** ώστε να βελτιστοποιήσετε τη διαδικασία fine-tuning σύμφωνα με τις ανάγκες σας.

1. Επιλέξτε **Finish**.

1. Σε αυτή την άσκηση, ολοκληρώσατε επιτυχώς το fine-tuning του μοντέλου Phi-3 χρησιμοποιώντας το Azure Machine Learning. Σημειώστε ότι η διαδικασία fine-tuning μπορεί να διαρκέσει αρκετό χρόνο. Μετά την εκκίνηση της εργασίας fine-tuning, πρέπει να περιμένετε να ολοκληρωθεί. Μπορείτε να παρακολουθείτε την κατάσταση της εργασίας από την καρτέλα Jobs στην αριστερή πλευρά του Azure Machine Learning Workspace σας. Στη συνέχεια, θα αναπτύξετε το fine-tuned μοντέλο και θα το ενσωματώσετε με το Prompt flow.

    ![Δείτε την εργασία fine-tuning.](../../../../../../translated_images/06-08-output.2bd32e59930672b1.el.png)

### Ανάπτυξη του fine-tuned μοντέλου Phi-3

Για να ενσωματώσετε το fine-tuned μοντέλο Phi-3 με το Prompt flow, πρέπει να αναπτύξετε το μοντέλο ώστε να είναι προσβάσιμο για πραγματικό χρόνο inference. Αυτή η διαδικασία περιλαμβάνει την καταχώρηση του μοντέλου, τη δημιουργία online endpoint και την ανάπτυξη του μοντέλου.

Σε αυτή την άσκηση, θα:

- Καταχωρήσετε το fine-tuned μοντέλο στο Azure Machine Learning workspace.
- Δημιουργήσετε ένα online endpoint.
- Αναπτύξετε το καταχωρημένο fine-tuned μοντέλο Phi-3.

#### Καταχώρηση του fine-tuned μοντέλου

1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Επιλέξτε το Azure Machine Learning workspace που δημιουργήσατε.

    ![Επιλέξτε το workspace που δημιουργήσατε.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f181.el.png)

1. Επιλέξτε **Models** από την αριστερή καρτέλα.
1. Επιλέξτε **+ Register**.
1. Επιλέξτε **From a job output**.

    ![Καταχώρηση μοντέλου.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777.el.png)

1. Επιλέξτε την εργασία που δημιουργήσατε.

    ![Επιλέξτε εργασία.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd093.el.png)

1. Επιλέξτε **Next**.

1. Επιλέξτε **Model type** σε **MLflow**.

1. Βεβαιωθείτε ότι το **Job output** είναι επιλεγμένο· θα πρέπει να είναι επιλεγμένο αυτόματα.

    ![Επιλέξτε output.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f.el.png)

2. Επιλέξτε **Next**.

3. Επιλέξτε **Register**.

    ![Επιλέξτε register.](../../../../../../translated_images/07-04-register.fd82a3b293060bc7.el.png)

4. Μπορείτε να δείτε το καταχωρημένο μοντέλο σας πηγαίνοντας στο μενού **Models** από την αριστερή καρτέλα.

    ![Καταχωρημένο μοντέλο.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591.el.png)

#### Ανάπτυξη του fine-tuned μοντέλου

1. Μεταβείτε στο Azure Machine Learning workspace που δημιουργήσατε.

1. Επιλέξτε **Endpoints** από την αριστερή καρτέλα.

1. Επιλέξτε **Real-time endpoints** από το μενού πλοήγησης.

    ![Δημιουργία endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09.el.png)

1. Επιλέξτε **Create**.

1. Επιλέξτε το καταχωρημένο μοντέλο που δημιουργήσατε.

    ![Επιλέξτε καταχωρημένο μοντέλο.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4.el.png)

1. Επιλέξτε **Select**.

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Επιλέξτε **Virtual machine** σε *Standard_NC6s_v3*.
    - Επιλέξτε τον αριθμό **Instance count** που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, *1*.
    - Επιλέξτε το **Endpoint** σε **New** για να δημιουργήσετε ένα endpoint.
    - Εισάγετε το **Endpoint name**. Πρέπει να είναι μοναδικό.
    - Εισάγετε το **Deployment name**. Πρέπει να είναι μοναδικό.

    ![Συμπληρώστε τις ρυθμίσεις ανάπτυξης.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e673784.el.png)

1. Επιλέξτε **Deploy**.

> [!WARNING]
> Για να αποφύγετε επιπλέον χρεώσεις στον λογαριασμό σας, βεβαιωθείτε ότι διαγράψατε το δημιουργημένο endpoint στο Azure Machine Learning workspace.
>

#### Έλεγχος κατάστασης ανάπτυξης στο Azure Machine Learning Workspace

1. Μεταβείτε στο Azure Machine Learning workspace που δημιουργήσατε.

1. Επιλέξτε **Endpoints** από την αριστερή καρτέλα.

1. Επιλέξτε το endpoint που δημιουργήσατε.

    ![Επιλέξτε endpoints](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4.el.png)

1. Σε αυτή τη σελίδα, μπορείτε να διαχειριστείτε τα endpoints κατά τη διάρκεια της διαδικασίας ανάπτυξης.

> [!NOTE]
> Μόλις ολοκληρωθεί η ανάπτυξη, βεβαιωθείτε ότι το **Live traffic** είναι ρυθμισμένο στο **100%**. Αν δεν είναι, επιλέξτε **Update traffic** για να προσαρμόσετε τις ρυθμίσεις κίνησης. Σημειώστε ότι δεν μπορείτε να δοκιμάσετε το μοντέλο αν η κίνηση είναι στο 0%.
>
> ![Ρύθμιση κίνησης.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d.el.png)
>

## Σενάριο 3: Ενσωμάτωση με Prompt flow και συνομιλία με το προσαρμοσμένο μοντέλο σας στο Azure AI Foundry

### Ενσωμάτωση του προσαρμοσμένου μοντέλου Phi-3 με το Prompt flow

Αφού αναπτύξετε επιτυχώς το fine-tuned μοντέλο σας, μπορείτε τώρα να το ενσωματώσετε με το Prompt Flow για να το χρησιμοποιήσετε σε εφαρμογές πραγματικού χρόνου, επιτρέποντας μια ποικιλία διαδραστικών εργασιών με το προσαρμοσμένο μοντέλο Phi-3.

Σε αυτή την άσκηση, θα:

- Δημιουργήσετε Azure AI Foundry Hub.
- Δημιουργήσετε Azure AI Foundry Project.
- Δημιουργήσετε Prompt flow.
- Προσθέσετε μια προσαρμοσμένη σύνδεση για το fine-tuned μοντέλο Phi-3.
- Ρυθμίσετε το Prompt flow για να συνομιλείτε με το προσαρμοσμένο μοντέλο Phi-3.
> [!NOTE]  
> Μπορείτε επίσης να ενσωματώσετε με το Promptflow χρησιμοποιώντας το Azure ML Studio. Η ίδια διαδικασία ενσωμάτωσης μπορεί να εφαρμοστεί και στο Azure ML Studio.
#### Δημιουργία Azure AI Foundry Hub

Πρέπει να δημιουργήσετε ένα Hub πριν δημιουργήσετε το Project. Ένα Hub λειτουργεί σαν ένα Resource Group, επιτρέποντάς σας να οργανώσετε και να διαχειριστείτε πολλαπλά Projects μέσα στο Azure AI Foundry.

1. Επισκεφθείτε το [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Επιλέξτε **All hubs** από την αριστερή καρτέλα.

1. Επιλέξτε **+ New hub** από το μενού πλοήγησης.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Εισάγετε **Hub name**. Πρέπει να είναι μια μοναδική τιμή.
    - Επιλέξτε την Azure **Subscription** σας.
    - Επιλέξτε το **Resource group** που θέλετε να χρησιμοποιήσετε (δημιουργήστε νέο αν χρειάζεται).
    - Επιλέξτε την **Location** που επιθυμείτε.
    - Επιλέξτε το **Connect Azure AI Services** που θέλετε να χρησιμοποιήσετε (δημιουργήστε νέο αν χρειάζεται).
    - Επιλέξτε **Connect Azure AI Search** και επιλέξτε **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c.el.png)

1. Επιλέξτε **Next**.

#### Δημιουργία Azure AI Foundry Project

1. Στο Hub που δημιουργήσατε, επιλέξτε **All projects** από την αριστερή καρτέλα.

1. Επιλέξτε **+ New project** από το μενού πλοήγησης.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f12.el.png)

1. Εισάγετε **Project name**. Πρέπει να είναι μια μοναδική τιμή.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a.el.png)

1. Επιλέξτε **Create a project**.

#### Προσθήκη προσαρμοσμένης σύνδεσης για το fine-tuned μοντέλο Phi-3

Για να ενσωματώσετε το προσαρμοσμένο μοντέλο Phi-3 με το Prompt flow, πρέπει να αποθηκεύσετε το endpoint και το κλειδί του μοντέλου σε μια προσαρμοσμένη σύνδεση. Αυτή η ρύθμιση εξασφαλίζει την πρόσβαση στο προσαρμοσμένο μοντέλο Phi-3 μέσα στο Prompt flow.

#### Ορισμός api key και endpoint uri του fine-tuned μοντέλου Phi-3

1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Μεταβείτε στο Azure Machine learning workspace που δημιουργήσατε.

1. Επιλέξτε **Endpoints** από την αριστερή καρτέλα.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf9605.el.png)

1. Επιλέξτε το endpoint που δημιουργήσατε.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275e.el.png)

1. Επιλέξτε **Consume** από το μενού πλοήγησης.

1. Αντιγράψτε το **REST endpoint** και το **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cb.el.png)

#### Προσθήκη της Προσαρμοσμένης Σύνδεσης

1. Επισκεφθείτε το [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Μεταβείτε στο Azure AI Foundry project που δημιουργήσατε.

1. Στο Project που δημιουργήσατε, επιλέξτε **Settings** από την αριστερή καρτέλα.

1. Επιλέξτε **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc.el.png)

1. Επιλέξτε **Custom keys** από το μενού πλοήγησης.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b2966460551.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Επιλέξτε **+ Add key value pairs**.
    - Για το όνομα του κλειδιού, εισάγετε **endpoint** και επικολλήστε το endpoint που αντιγράψατε από το Azure ML Studio στο πεδίο τιμής.
    - Επιλέξτε ξανά **+ Add key value pairs**.
    - Για το όνομα του κλειδιού, εισάγετε **key** και επικολλήστε το κλειδί που αντιγράψατε από το Azure ML Studio στο πεδίο τιμής.
    - Αφού προσθέσετε τα κλειδιά, επιλέξτε **is secret** για να αποτρέψετε την έκθεση του κλειδιού.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26.el.png)

1. Επιλέξτε **Add connection**.

#### Δημιουργία Prompt flow

Έχετε προσθέσει μια προσαρμοσμένη σύνδεση στο Azure AI Foundry. Τώρα, ας δημιουργήσουμε ένα Prompt flow ακολουθώντας τα παρακάτω βήματα. Στη συνέχεια, θα συνδέσετε αυτό το Prompt flow με την προσαρμοσμένη σύνδεση ώστε να μπορείτε να χρησιμοποιήσετε το fine-tuned μοντέλο μέσα στο Prompt flow.

1. Μεταβείτε στο Azure AI Foundry project που δημιουργήσατε.

1. Επιλέξτε **Prompt flow** από την αριστερή καρτέλα.

1. Επιλέξτε **+ Create** από το μενού πλοήγησης.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5b.el.png)

1. Επιλέξτε **Chat flow** από το μενού πλοήγησης.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591.el.png)

1. Εισάγετε **Folder name** που θέλετε να χρησιμοποιήσετε.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d.el.png)

2. Επιλέξτε **Create**.

#### Ρύθμιση Prompt flow για συνομιλία με το προσαρμοσμένο μοντέλο Phi-3

Πρέπει να ενσωματώσετε το fine-tuned μοντέλο Phi-3 σε ένα Prompt flow. Ωστόσο, το υπάρχον Prompt flow που παρέχεται δεν είναι σχεδιασμένο για αυτόν τον σκοπό. Επομένως, πρέπει να ανασχεδιάσετε το Prompt flow ώστε να επιτρέπεται η ενσωμάτωση του προσαρμοσμένου μοντέλου.

1. Στο Prompt flow, εκτελέστε τις παρακάτω ενέργειες για να αναδημιουργήσετε τη ροή:

    - Επιλέξτε **Raw file mode**.
    - Διαγράψτε όλο τον υπάρχοντα κώδικα στο αρχείο *flow.dag.yml*.
    - Προσθέστε τον παρακάτω κώδικα στο αρχείο *flow.dag.yml*.

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

    - Επιλέξτε **Save**.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985.el.png)

1. Προσθέστε τον παρακάτω κώδικα στο αρχείο *integrate_with_promptflow.py* για να χρησιμοποιήσετε το προσαρμοσμένο μοντέλο Phi-3 στο Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
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

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
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
            
            # Log the full JSON response
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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d09777.el.png)

> [!NOTE]
> Για περισσότερες λεπτομέρειες σχετικά με τη χρήση του Prompt flow στο Azure AI Foundry, μπορείτε να ανατρέξετε στο [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Επιλέξτε **Chat input**, **Chat output** για να ενεργοποιήσετε τη συνομιλία με το μοντέλο σας.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03b.el.png)

1. Τώρα είστε έτοιμοι να συνομιλήσετε με το προσαρμοσμένο μοντέλο Phi-3. Στην επόμενη άσκηση, θα μάθετε πώς να ξεκινήσετε το Prompt flow και να το χρησιμοποιήσετε για συνομιλία με το fine-tuned μοντέλο Phi-3.

> [!NOTE]
>
> Η αναδημιουργημένη ροή θα πρέπει να μοιάζει με την εικόνα παρακάτω:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c.el.png)
>

### Συνομιλία με το προσαρμοσμένο μοντέλο Phi-3

Τώρα που έχετε fine-tune και ενσωματώσει το προσαρμοσμένο μοντέλο Phi-3 με το Prompt flow, είστε έτοιμοι να ξεκινήσετε την αλληλεπίδραση μαζί του. Αυτή η άσκηση θα σας καθοδηγήσει στη διαδικασία ρύθμισης και εκκίνησης μιας συνομιλίας με το μοντέλο σας χρησιμοποιώντας το Prompt flow. Ακολουθώντας αυτά τα βήματα, θα μπορέσετε να αξιοποιήσετε πλήρως τις δυνατότητες του fine-tuned μοντέλου Phi-3 για διάφορες εργασίες και συζητήσεις.

- Συνομιλήστε με το προσαρμοσμένο μοντέλο Phi-3 χρησιμοποιώντας το Prompt flow.

#### Εκκίνηση Prompt flow

1. Επιλέξτε **Start compute sessions** για να ξεκινήσετε το Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b.el.png)

1. Επιλέξτε **Validate and parse input** για να ανανεώσετε τις παραμέτρους.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e9.el.png)

1. Επιλέξτε την **Value** της **connection** στην προσαρμοσμένη σύνδεση που δημιουργήσατε. Για παράδειγμα, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b1844023.el.png)

#### Συνομιλία με το προσαρμοσμένο μοντέλο

1. Επιλέξτε **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e6.el.png)

1. Ακολουθεί ένα παράδειγμα αποτελεσμάτων: Τώρα μπορείτε να συνομιλήσετε με το προσαρμοσμένο μοντέλο Phi-3. Συνιστάται να κάνετε ερωτήσεις βασισμένες στα δεδομένα που χρησιμοποιήθηκαν για το fine-tuning.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126f.el.png)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.