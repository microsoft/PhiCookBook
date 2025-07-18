<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-07-17T00:24:59+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "it"
}
-->
# Fine-tune e integra modelli Phi-3 personalizzati con Prompt flow

Questo esempio end-to-end (E2E) si basa sulla guida "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" della Microsoft Tech Community. Introduce i processi di fine-tuning, distribuzione e integrazione di modelli Phi-3 personalizzati con Prompt flow.

## Panoramica

In questo esempio E2E imparerai come effettuare il fine-tuning del modello Phi-3 e integrarlo con Prompt flow. Sfruttando Azure Machine Learning e Prompt flow, stabilirai un flusso di lavoro per distribuire e utilizzare modelli AI personalizzati. Questo esempio E2E è suddiviso in tre scenari:

**Scenario 1: Configurare le risorse Azure e prepararsi al fine-tuning**

**Scenario 2: Effettuare il fine-tuning del modello Phi-3 e distribuirlo in Azure Machine Learning Studio**

**Scenario 3: Integrare con Prompt flow e chattare con il tuo modello personalizzato**

Ecco una panoramica di questo esempio E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.02fc569e266d468cf3bbb3158cf273380cbdf7fcec042c7328e1559c6b2e2632.it.png)

### Indice

1. **[Scenario 1: Configurare le risorse Azure e prepararsi al fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Creare un Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Richiedere quote GPU nella sottoscrizione Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Aggiungere un'assegnazione di ruolo](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Configurare il progetto](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Preparare il dataset per il fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 2: Effettuare il fine-tuning del modello Phi-3 e distribuirlo in Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Configurare Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Effettuare il fine-tuning del modello Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Distribuire il modello fine-tuned](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 3: Integrare con Prompt flow e chattare con il tuo modello personalizzato](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrare il modello Phi-3 personalizzato con Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Chattare con il tuo modello personalizzato](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenario 1: Configurare le risorse Azure e prepararsi al fine-tuning

### Creare un Azure Machine Learning Workspace

1. Digita *azure machine learning* nella **barra di ricerca** in alto nella pagina del portale e seleziona **Azure Machine Learning** tra le opzioni che appaiono.

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.a5116f8454d98c600d87008fb78206d2cf90c0b920c231618a8ec8baaa6f46c3.it.png)

1. Seleziona **+ Crea** dal menu di navigazione.

1. Seleziona **Nuovo workspace** dal menu di navigazione.

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.83e17436f8898dc4fbb808d1bbcd92962692b1fa687f4c5d3952f453177825bc.it.png)

1. Esegui le seguenti operazioni:

    - Seleziona la tua **Sottoscrizione** Azure.
    - Seleziona il **Gruppo di risorse** da utilizzare (creane uno nuovo se necessario).
    - Inserisci il **Nome del workspace**. Deve essere un valore univoco.
    - Seleziona la **Regione** che desideri utilizzare.
    - Seleziona l'**Account di archiviazione** da utilizzare (creane uno nuovo se necessario).
    - Seleziona il **Key vault** da utilizzare (creane uno nuovo se necessario).
    - Seleziona gli **Application insights** da utilizzare (creane uno nuovo se necessario).
    - Seleziona il **Container registry** da utilizzare (creane uno nuovo se necessario).

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.730a5177757bbebb141b9e8c16f31834e82e831275bd9faad0b70343f46255de.it.png)

1. Seleziona **Rivedi + crea**.

1. Seleziona **Crea**.

### Richiedere quote GPU nella sottoscrizione Azure

In questo esempio E2E utilizzerai la *Standard_NC24ads_A100_v4 GPU* per il fine-tuning, che richiede una richiesta di quota, e la *Standard_E4s_v3* CPU per la distribuzione, che non richiede una richiesta di quota.

> [!NOTE]
>
> Solo le sottoscrizioni Pay-As-You-Go (il tipo di sottoscrizione standard) sono idonee per l'allocazione GPU; le sottoscrizioni benefit non sono attualmente supportate.
>
> Per chi utilizza sottoscrizioni benefit (come Visual Studio Enterprise Subscription) o desidera testare rapidamente il processo di fine-tuning e distribuzione, questo tutorial fornisce anche indicazioni per effettuare il fine-tuning con un dataset minimo usando una CPU. Tuttavia, è importante notare che i risultati del fine-tuning sono significativamente migliori utilizzando una GPU con dataset più grandi.

1. Visita [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Esegui le seguenti operazioni per richiedere la quota *Standard NCADSA100v4 Family*:

    - Seleziona **Quota** dalla scheda a sinistra.
    - Seleziona la **famiglia di macchine virtuali** da utilizzare. Ad esempio, seleziona **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, che include la GPU *Standard_NC24ads_A100_v4*.
    - Seleziona **Richiedi quota** dal menu di navigazione.

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.3d3670c3221ab8348515fcfba9d0279114f04065df8bd6fb78e3d3704e627545.it.png)

    - Nella pagina Richiedi quota, inserisci il **Nuovo limite di core** che desideri utilizzare. Ad esempio, 24.
    - Nella pagina Richiedi quota, seleziona **Invia** per richiedere la quota GPU.

> [!NOTE]
> Puoi selezionare la GPU o CPU più adatta alle tue esigenze consultando il documento [Dimensioni delle macchine virtuali in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### Aggiungere un'assegnazione di ruolo

Per effettuare il fine-tuning e distribuire i tuoi modelli, devi prima creare un'Identità Gestita Assegnata all'Utente (User Assigned Managed Identity, UAI) e assegnarle i permessi appropriati. Questa UAI sarà utilizzata per l'autenticazione durante la distribuzione.

#### Creare un'Identità Gestita Assegnata all'Utente (UAI)

1. Digita *managed identities* nella **barra di ricerca** in alto nella pagina del portale e seleziona **Managed Identities** tra le opzioni che appaiono.

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.9297b6039874eff8a95d6e7762f1b087275a9634677f0a4e355717550ace3c02.it.png)

1. Seleziona **+ Crea**.

    ![Select create.](../../../../../../translated_images/01-06-select-create.936d8d66d7144f9a8c70af922bf28a573c0744fb642f8228d62214b010a070d9.it.png)

1. Esegui le seguenti operazioni:

    - Seleziona la tua **Sottoscrizione** Azure.
    - Seleziona il **Gruppo di risorse** da utilizzare (creane uno nuovo se necessario).
    - Seleziona la **Regione** che desideri utilizzare.
    - Inserisci il **Nome**. Deve essere un valore univoco.

1. Seleziona **Rivedi + crea**.

1. Seleziona **+ Crea**.

#### Aggiungere l'assegnazione del ruolo Contributor all'Identità Gestita

1. Vai alla risorsa Identità Gestita che hai creato.

1. Seleziona **Assegnazioni ruolo Azure** dalla scheda a sinistra.

1. Seleziona **+ Aggiungi assegnazione ruolo** dal menu di navigazione.

1. Nella pagina Aggiungi assegnazione ruolo, esegui le seguenti operazioni:
    - Seleziona l'**Ambito** su **Gruppo di risorse**.
    - Seleziona la tua **Sottoscrizione** Azure.
    - Seleziona il **Gruppo di risorse** da utilizzare.
    - Seleziona il **Ruolo** su **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.29ca99b7c9f687e008e224cf336687c04c9fe24740e47e34ce041b50b47e0ed1.it.png)

1. Seleziona **Salva**.

#### Aggiungere l'assegnazione del ruolo Storage Blob Data Reader all'Identità Gestita

1. Digita *storage accounts* nella **barra di ricerca** in alto nella pagina del portale e seleziona **Storage accounts** tra le opzioni che appaiono.

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.1186c8e42933e49bcd9cce3ffd1b6218afb6e5c3700b628da7b7c294be71b911.it.png)

1. Seleziona l'account di archiviazione associato al workspace Azure Machine Learning che hai creato. Ad esempio, *finetunephistorage*.

1. Esegui le seguenti operazioni per navigare alla pagina Aggiungi assegnazione ruolo:

    - Vai all'account di archiviazione Azure che hai creato.
    - Seleziona **Controllo accessi (IAM)** dalla scheda a sinistra.
    - Seleziona **+ Aggiungi** dal menu di navigazione.
    - Seleziona **Aggiungi assegnazione ruolo** dal menu di navigazione.

    ![Add role.](../../../../../../translated_images/01-09-add-role.d2db22fec1b187f0ae84790d65dc5726a9b57c496d916b8700d41e0b3b468451.it.png)

1. Nella pagina Aggiungi assegnazione ruolo, esegui le seguenti operazioni:

    - Nella pagina Ruolo, digita *Storage Blob Data Reader* nella **barra di ricerca** e seleziona **Storage Blob Data Reader** tra le opzioni che appaiono.
    - Nella pagina Ruolo, seleziona **Avanti**.
    - Nella pagina Membri, seleziona **Assegna accesso a** **Identità gestita**.
    - Nella pagina Membri, seleziona **+ Seleziona membri**.
    - Nella pagina Seleziona identità gestite, seleziona la tua **Sottoscrizione** Azure.
    - Nella pagina Seleziona identità gestite, seleziona l'**Identità gestita** su **Managed Identity**.
    - Nella pagina Seleziona identità gestite, seleziona l'Identità gestita che hai creato. Ad esempio, *finetunephi-managedidentity*.
    - Nella pagina Seleziona identità gestite, seleziona **Seleziona**.

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.5ce5ba181f72a4df788963e1dc0a68c39ee297363aabe979b487c60b3037662f.it.png)

1. Seleziona **Rivedi + assegna**.

#### Aggiungere l'assegnazione del ruolo AcrPull all'Identità Gestita

1. Digita *container registries* nella **barra di ricerca** in alto nella pagina del portale e seleziona **Container registries** tra le opzioni che appaiono.

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.ff3b8bdc49dc596c64c0f778633c652ce08e4ac28f142a17afc10de81bb8c336.it.png)

1. Seleziona il container registry associato al workspace Azure Machine Learning. Ad esempio, *finetunephicontainerregistries*

1. Esegui le seguenti operazioni per navigare alla pagina Aggiungi assegnazione ruolo:

    - Seleziona **Controllo accessi (IAM)** dalla scheda a sinistra.
    - Seleziona **+ Aggiungi** dal menu di navigazione.
    - Seleziona **Aggiungi assegnazione ruolo** dal menu di navigazione.

1. Nella pagina Aggiungi assegnazione ruolo, esegui le seguenti operazioni:

    - Nella pagina Ruolo, digita *AcrPull* nella **barra di ricerca** e seleziona **AcrPull** tra le opzioni che appaiono.
    - Nella pagina Ruolo, seleziona **Avanti**.
    - Nella pagina Membri, seleziona **Assegna accesso a** **Identità gestita**.
    - Nella pagina Membri, seleziona **+ Seleziona membri**.
    - Nella pagina Seleziona identità gestite, seleziona la tua **Sottoscrizione** Azure.
    - Nella pagina Seleziona identità gestite, seleziona l'**Identità gestita** su **Managed Identity**.
    - Nella pagina Seleziona identità gestite, seleziona l'Identità gestita che hai creato. Ad esempio, *finetunephi-managedidentity*.
    - Nella pagina Seleziona identità gestite, seleziona **Seleziona**.
    - Seleziona **Rivedi + assegna**.

### Configurare il progetto

Ora creerai una cartella in cui lavorare e configurerai un ambiente virtuale per sviluppare un programma che interagisca con gli utenti e utilizzi la cronologia delle chat memorizzata in Azure Cosmos DB per informare le sue risposte.

#### Creare una cartella in cui lavorare

1. Apri una finestra del terminale e digita il seguente comando per creare una cartella chiamata *finetune-phi* nel percorso predefinito.

    ```console
    mkdir finetune-phi
    ```

1. Digita il seguente comando nel terminale per spostarti nella cartella *finetune-phi* che hai creato.

    ```console
    cd finetune-phi
    ```

#### Creare un ambiente virtuale

1. Digita il seguente comando nel terminale per creare un ambiente virtuale chiamato *.venv*.

    ```console
    python -m venv .venv
    ```

1. Digita il seguente comando nel terminale per attivare l'ambiente virtuale.

    ```console
    .venv\Scripts\activate.bat
    ```
> [!NOTE]
>
> Se ha funzionato, dovresti vedere *(.venv)* prima del prompt dei comandi.
#### Installa i pacchetti richiesti

1. Digita i seguenti comandi nel terminale per installare i pacchetti necessari.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Crea i file del progetto

In questo esercizio, creerai i file essenziali per il nostro progetto. Questi file includono script per scaricare il dataset, configurare l'ambiente Azure Machine Learning, effettuare il fine-tuning del modello Phi-3 e distribuire il modello fine-tuned. Creerai anche un file *conda.yml* per configurare l'ambiente di fine-tuning.

In questo esercizio, dovrai:

- Creare un file *download_dataset.py* per scaricare il dataset.
- Creare un file *setup_ml.py* per configurare l'ambiente Azure Machine Learning.
- Creare un file *fine_tune.py* nella cartella *finetuning_dir* per effettuare il fine-tuning del modello Phi-3 usando il dataset.
- Creare un file *conda.yml* per configurare l'ambiente di fine-tuning.
- Creare un file *deploy_model.py* per distribuire il modello fine-tuned.
- Creare un file *integrate_with_promptflow.py* per integrare il modello fine-tuned ed eseguire il modello usando Prompt flow.
- Creare un file flow.dag.yml per impostare la struttura del workflow per Prompt flow.
- Creare un file *config.py* per inserire le informazioni di Azure.

> [!NOTE]
>
> Struttura completa delle cartelle:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        ├── finetuning_dir
> .        │      └── fine_tune.py
> .        ├── conda.yml
> .        ├── config.py
> .        ├── deploy_model.py
> .        ├── download_dataset.py
> .        ├── flow.dag.yml
> .        ├── integrate_with_promptflow.py
> .        └── setup_ml.py
> ```

1. Apri **Visual Studio Code**.

1. Seleziona **File** dalla barra del menu.

1. Seleziona **Apri cartella**.

1. Seleziona la cartella *finetune-phi* che hai creato, situata in *C:\Users\yourUserName\finetune-phi*.

    ![Apri cartella progetto.](../../../../../../translated_images/01-12-open-project-folder.1fff9c7f41dd1639c12e7da258ac8b3deca260786edb07598e206725cd1593ce.it.png)

1. Nel pannello a sinistra di Visual Studio Code, clicca con il tasto destro e seleziona **Nuovo file** per creare un nuovo file chiamato *download_dataset.py*.

1. Nel pannello a sinistra di Visual Studio Code, clicca con il tasto destro e seleziona **Nuovo file** per creare un nuovo file chiamato *setup_ml.py*.

1. Nel pannello a sinistra di Visual Studio Code, clicca con il tasto destro e seleziona **Nuovo file** per creare un nuovo file chiamato *deploy_model.py*.

    ![Crea nuovo file.](../../../../../../translated_images/01-13-create-new-file.c17c150fff384a398766a39eac9f15240a9a4da566bd8dca86f471e78eadc69e.it.png)

1. Nel pannello a sinistra di Visual Studio Code, clicca con il tasto destro e seleziona **Nuova cartella** per creare una nuova cartella chiamata *finetuning_dir*.

1. Nella cartella *finetuning_dir*, crea un nuovo file chiamato *fine_tune.py*.

#### Crea e configura il file *conda.yml*

1. Nel pannello a sinistra di Visual Studio Code, clicca con il tasto destro e seleziona **Nuovo file** per creare un nuovo file chiamato *conda.yml*.

1. Aggiungi il seguente codice al file *conda.yml* per configurare l'ambiente di fine-tuning per il modello Phi-3.

    ```yml
    name: phi-3-training-env
    channels:
      - defaults
      - conda-forge
    dependencies:
      - python=3.10
      - pip
      - numpy<2.0
      - pip:
          - torch==2.4.0
          - torchvision==0.19.0
          - trl==0.8.6
          - transformers==4.41
          - datasets==2.21.0
          - azureml-core==1.57.0
          - azure-storage-blob==12.19.0
          - azure-ai-ml==1.16
          - azure-identity==1.17.1
          - accelerate==0.33.0
          - mlflow==2.15.1
          - azureml-mlflow==1.57.0
    ```

#### Crea e configura il file *config.py*

1. Nel pannello a sinistra di Visual Studio Code, clicca con il tasto destro e seleziona **Nuovo file** per creare un nuovo file chiamato *config.py*.

1. Aggiungi il seguente codice al file *config.py* per inserire le tue informazioni di Azure.

    ```python
    # Azure settings
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Azure Machine Learning settings
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Azure Managed Identity settings
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Dataset file paths
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Fine-tuned model settings
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### Aggiungi le variabili d'ambiente di Azure

1. Esegui le seguenti operazioni per aggiungere l'ID della sottoscrizione Azure:

    - Digita *subscriptions* nella **barra di ricerca** in alto nella pagina del portale e seleziona **Sottoscrizioni** tra le opzioni che appaiono.
    - Seleziona la sottoscrizione Azure che stai utilizzando.
    - Copia e incolla il tuo Subscription ID nel file *config.py*.

    ![Trova subscription id.](../../../../../../translated_images/01-14-find-subscriptionid.4f4ca33555f1e637e01163bfdd2a606e7d06f05455ab56e05cb5107e938e7a90.it.png)

1. Esegui le seguenti operazioni per aggiungere il nome del Workspace Azure:

    - Vai alla risorsa Azure Machine Learning che hai creato.
    - Copia e incolla il nome del tuo account nel file *config.py*.

    ![Trova nome Azure Machine Learning.](../../../../../../translated_images/01-15-find-AZML-name.1975f0422bca19a702b1bb5e9d8e9f5e5424abe066a0ff310da980582e65721f.it.png)

1. Esegui le seguenti operazioni per aggiungere il nome del Resource Group Azure:

    - Vai alla risorsa Azure Machine Learning che hai creato.
    - Copia e incolla il nome del tuo Azure Resource Group nel file *config.py*.

    ![Trova nome resource group.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.855a349d0af134a399243d7c94d5aabd86070ab6535d3cf2ec38c78538626666.it.png)

2. Esegui le seguenti operazioni per aggiungere il nome dell'Azure Managed Identity:

    - Vai alla risorsa Managed Identities che hai creato.
    - Copia e incolla il nome della tua Azure Managed Identity nel file *config.py*.

    ![Trova UAI.](../../../../../../translated_images/01-17-find-uai.3529464f534998271ea7c5aebafa887051567417f3b4244ff58fdd443192b6d7.it.png)

### Prepara il dataset per il fine-tuning

In questo esercizio, eseguirai il file *download_dataset.py* per scaricare i dataset *ULTRACHAT_200k* nel tuo ambiente locale. Userai poi questi dataset per effettuare il fine-tuning del modello Phi-3 in Azure Machine Learning.

#### Scarica il dataset usando *download_dataset.py*

1. Apri il file *download_dataset.py* in Visual Studio Code.

1. Aggiungi il seguente codice in *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset
    from config import (
        TRAIN_DATA_PATH,
        TEST_DATA_PATH)

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
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **Consigli per il fine-tuning con un dataset minimo usando una CPU**
>
> Se vuoi usare una CPU per il fine-tuning, questo approccio è ideale per chi ha sottoscrizioni con benefici (come Visual Studio Enterprise Subscription) o per testare rapidamente il processo di fine-tuning e distribuzione.
>
> Sostituisci `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` con `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Digita il seguente comando nel terminale per eseguire lo script e scaricare il dataset nel tuo ambiente locale.

    ```console
    python download_data.py
    ```

1. Verifica che i dataset siano stati salvati correttamente nella directory locale *finetune-phi/data*.

> [!NOTE]
>
> **Dimensione del dataset e tempo di fine-tuning**
>
> In questo esempio E2E, usi solo l'1% del dataset (`train_sft[:1%]`). Questo riduce significativamente la quantità di dati, accelerando sia il caricamento che il processo di fine-tuning. Puoi regolare la percentuale per trovare il giusto equilibrio tra tempo di addestramento e prestazioni del modello. Usare un sottoinsieme più piccolo del dataset riduce il tempo necessario per il fine-tuning, rendendo il processo più gestibile per un esempio E2E.

## Scenario 2: Fine-tuning del modello Phi-3 e distribuzione in Azure Machine Learning Studio

### Configura Azure CLI

Devi configurare Azure CLI per autenticare il tuo ambiente. Azure CLI ti permette di gestire le risorse Azure direttamente dalla riga di comando e fornisce le credenziali necessarie ad Azure Machine Learning per accedere a queste risorse. Per iniziare, installa [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. Apri una finestra del terminale e digita il seguente comando per effettuare il login al tuo account Azure.

    ```console
    az login
    ```

1. Seleziona l'account Azure da utilizzare.

1. Seleziona la sottoscrizione Azure da utilizzare.

    ![Trova nome resource group.](../../../../../../translated_images/02-01-login-using-azure-cli.dfde31cb75e58a8792c687d36e4fc4f4ee37fd76640e6e4e5aed3329513f2328.it.png)

> [!TIP]
>
> Se hai problemi ad accedere ad Azure, prova a usare un codice dispositivo. Apri una finestra del terminale e digita il seguente comando per accedere al tuo account Azure:
>
> ```console
> az login --use-device-code
> ```
>

### Effettua il fine-tuning del modello Phi-3

In questo esercizio, effettuerai il fine-tuning del modello Phi-3 usando il dataset fornito. Prima definirai il processo di fine-tuning nel file *fine_tune.py*. Poi configurerai l'ambiente Azure Machine Learning e avvierai il processo di fine-tuning eseguendo il file *setup_ml.py*. Questo script assicura che il fine-tuning avvenga all'interno dell'ambiente Azure Machine Learning.

Eseguendo *setup_ml.py*, avvierai il processo di fine-tuning nell'ambiente Azure Machine Learning.

#### Aggiungi il codice al file *fine_tune.py*

1. Vai nella cartella *finetuning_dir* e apri il file *fine_tune.py* in Visual Studio Code.

1. Aggiungi il seguente codice in *fine_tune.py*.

    ```python
    import argparse
    import sys
    import logging
    import os
    from datasets import load_dataset
    import torch
    import mlflow
    from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
    from trl import SFTTrainer

    # To avoid the INVALID_PARAMETER_VALUE error in MLflow, disable MLflow integration
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
        level=logging.WARNING
    )
    logger = logging.getLogger(__name__)

    def initialize_model_and_tokenizer(model_name, model_kwargs):
        """
        Initialize the model and tokenizer with the given pretrained model name and arguments.
        """
        model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.model_max_length = 2048
        tokenizer.pad_token = tokenizer.unk_token
        tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids(tokenizer.pad_token)
        tokenizer.padding_side = 'right'
        return model, tokenizer

    def apply_chat_template(example, tokenizer):
        """
        Apply a chat template to tokenize messages in the example.
        """
        messages = example["messages"]
        if messages[0]["role"] != "system":
            messages.insert(0, {"role": "system", "content": ""})
        example["text"] = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        return example

    def load_and_preprocess_data(train_filepath, test_filepath, tokenizer):
        """
        Load and preprocess the dataset.
        """
        train_dataset = load_dataset('json', data_files=train_filepath, split='train')
        test_dataset = load_dataset('json', data_files=test_filepath, split='train')
        column_names = list(train_dataset.features)

        train_dataset = train_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to train dataset",
        )

        test_dataset = test_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to test dataset",
        )

        return train_dataset, test_dataset

    def train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, output_dir):
        """
        Train and evaluate the model.
        """
        training_args = TrainingArguments(
            bf16=True,
            do_eval=True,
            output_dir=output_dir,
            eval_strategy="epoch",
            learning_rate=5.0e-06,
            logging_steps=20,
            lr_scheduler_type="cosine",
            num_train_epochs=3,
            overwrite_output_dir=True,
            per_device_eval_batch_size=4,
            per_device_train_batch_size=4,
            remove_unused_columns=True,
            save_steps=500,
            seed=0,
            gradient_checkpointing=True,
            gradient_accumulation_steps=1,
            warmup_ratio=0.2,
        )

        trainer = SFTTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            max_seq_length=2048,
            dataset_text_field="text",
            tokenizer=tokenizer,
            packing=True
        )

        train_result = trainer.train()
        trainer.log_metrics("train", train_result.metrics)

        mlflow.transformers.log_model(
            transformers_model={"model": trainer.model, "tokenizer": tokenizer},
            artifact_path=output_dir,
        )

        tokenizer.padding_side = 'left'
        eval_metrics = trainer.evaluate()
        eval_metrics["eval_samples"] = len(test_dataset)
        trainer.log_metrics("eval", eval_metrics)

    def main(train_file, eval_file, model_output_dir):
        """
        Main function to fine-tune the model.
        """
        model_kwargs = {
            "use_cache": False,
            "trust_remote_code": True,
            "torch_dtype": torch.bfloat16,
            "device_map": None,
            "attn_implementation": "eager"
        }

        # pretrained_model_name = "microsoft/Phi-3-mini-4k-instruct"
        pretrained_model_name = "microsoft/Phi-3.5-mini-instruct"

        with mlflow.start_run():
            model, tokenizer = initialize_model_and_tokenizer(pretrained_model_name, model_kwargs)
            train_dataset, test_dataset = load_and_preprocess_data(train_file, eval_file, tokenizer)
            train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, model_output_dir)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--train-file", type=str, required=True, help="Path to the training data")
        parser.add_argument("--eval-file", type=str, required=True, help="Path to the evaluation data")
        parser.add_argument("--model_output_dir", type=str, required=True, help="Directory to save the fine-tuned model")
        args = parser.parse_args()
        main(args.train_file, args.eval_file, args.model_output_dir)

    ```

1. Salva e chiudi il file *fine_tune.py*.

> [!TIP]
> **Puoi fare il fine-tuning del modello Phi-3.5**
>
> Nel file *fine_tune.py*, puoi cambiare il valore di `pretrained_model_name` da `"microsoft/Phi-3-mini-4k-instruct"` a qualsiasi modello tu voglia fine-tunare. Ad esempio, se lo cambi in `"microsoft/Phi-3.5-mini-instruct"`, userai il modello Phi-3.5-mini-instruct per il fine-tuning. Per trovare e usare il nome del modello che preferisci, visita [Hugging Face](https://huggingface.co/), cerca il modello di tuo interesse e copia-incolla il nome nel campo `pretrained_model_name` nel tuo script.
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Fine tune Phi-3.5.":::
>

#### Aggiungi il codice al file *setup_ml.py*

1. Apri il file *setup_ml.py* in Visual Studio Code.

1. Aggiungi il seguente codice in *setup_ml.py*.

    ```python
    import logging
    from azure.ai.ml import MLClient, command, Input
    from azure.ai.ml.entities import Environment, AmlCompute
    from azure.identity import AzureCliCredential
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        TRAIN_DATA_PATH,
        TEST_DATA_PATH
    )

    # Constants

    # Uncomment the following lines to use a CPU instance for training
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    FINETUNING_DIR = "./finetuning_dir" # Path to the fine-tuning script
    TRAINING_ENV_NAME = "phi-3-training-environment" # Name of the training environment
    MODEL_OUTPUT_DIR = "./model_output" # Path to the model output directory in azure ml

    # Logging setup to track the process
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.WARNING
    )

    def get_ml_client():
        """
        Initialize the ML Client using Azure CLI credentials.
        """
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def create_or_get_environment(ml_client):
        """
        Create or update the training environment in Azure ML.
        """
        env = Environment(
            image=DOCKER_IMAGE_NAME,  # Docker image for the environment
            conda_file=CONDA_FILE,  # Conda environment file
            name=TRAINING_ENV_NAME,  # Name of the environment
        )
        return ml_client.environments.create_or_update(env)

    def create_or_get_compute_cluster(ml_client, compute_name, COMPUTE_INSTANCE_TYPE, location):
        """
        Create or update the compute cluster in Azure ML.
        """
        try:
            compute_cluster = ml_client.compute.get(compute_name)
            logger.info(f"Compute cluster '{compute_name}' already exists. Reusing it for the current run.")
        except Exception:
            logger.info(f"Compute cluster '{compute_name}' does not exist. Creating a new one with size {COMPUTE_INSTANCE_TYPE}.")
            compute_cluster = AmlCompute(
                name=compute_name,
                size=COMPUTE_INSTANCE_TYPE,
                location=location,
                tier="Dedicated",  # Tier of the compute cluster
                min_instances=0,  # Minimum number of instances
                max_instances=1  # Maximum number of instances
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Wait for the cluster to be created
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Path to fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Training environment
            compute=compute_name,  # Compute cluster to use
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Path to the training data file
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Path to the evaluation data file
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Initialize ML Client
        ml_client = get_ml_client()

        # Create Environment
        env = create_or_get_environment(ml_client)
        
        # Create or get existing compute cluster
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Create and Submit Fine-Tuning Job
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Submit the job
        ml_client.jobs.stream(returned_job.name)  # Stream the job logs
        
        # Capture the job name
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. Sostituisci `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` e `LOCATION` con i tuoi dati specifici.

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **Consigli per il fine-tuning con un dataset minimo usando una CPU**
>
> Se vuoi usare una CPU per il fine-tuning, questo approccio è ideale per chi ha sottoscrizioni con benefici (come Visual Studio Enterprise Subscription) o per testare rapidamente il processo di fine-tuning e distribuzione.
>
> 1. Apri il file *setup_ml*.
> 1. Sostituisci `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` e `DOCKER_IMAGE_NAME` con i seguenti valori. Se non hai accesso a *Standard_E16s_v3*, puoi usare un'istanza CPU equivalente o richiedere una nuova quota.
> 1. Sostituisci `LOCATION` con i tuoi dati specifici.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Digita il seguente comando per eseguire lo script *setup_ml.py* e avviare il processo di fine-tuning in Azure Machine Learning.

    ```python
    python setup_ml.py
    ```

1. In questo esercizio, hai effettuato con successo il fine-tuning del modello Phi-3 usando Azure Machine Learning. Eseguendo lo script *setup_ml.py*, hai configurato l'ambiente Azure Machine Learning e avviato il processo di fine-tuning definito nel file *fine_tune.py*. Tieni presente che il processo di fine-tuning può richiedere molto tempo. Dopo aver eseguito il comando `python setup_ml.py`, devi attendere il completamento del processo. Puoi monitorare lo stato del job di fine-tuning seguendo il link fornito nel terminale verso il portale Azure Machine Learning.

    ![Visualizza job di fine-tuning.](../../../../../../translated_images/02-02-see-finetuning-job.59393bc3b143871ee8ba32fa508cc4018c0f04e51ad14b95c421ad77151f768f.it.png)

### Distribuisci il modello fine-tuned

Per integrare il modello Phi-3 fine-tuned con Prompt Flow, devi distribuire il modello per renderlo accessibile per inferenze in tempo reale. Questo processo include la registrazione del modello, la creazione di un endpoint online e la distribuzione del modello.

#### Imposta il nome del modello, il nome dell'endpoint e il nome della distribuzione per la distribuzione

1. Apri il file *config.py*.

1. Sostituisci `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` con il nome desiderato per il tuo modello.

1. Sostituisci `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` con il nome desiderato per il tuo endpoint.

1. Sostituisci `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` con il nome desiderato per la tua distribuzione.

#### Aggiungi il codice al file *deploy_model.py*

Eseguendo il file *deploy_model.py* automatizzi l'intero processo di distribuzione. Questo registra il modello, crea un endpoint e avvia la distribuzione basandosi sulle impostazioni specificate nel file *config.py*, che includono il nome del modello, il nome dell'endpoint e il nome della distribuzione.

1. Apri il file *deploy_model.py* in Visual Studio Code.

1. Aggiungi il seguente codice in *deploy_model.py*.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Configuration imports
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        AZURE_MANAGED_IDENTITY_RESOURCE_ID,
        AZURE_MANAGED_IDENTITY_CLIENT_ID,
        AZURE_MODEL_NAME,
        AZURE_ENDPOINT_NAME,
        AZURE_DEPLOYMENT_NAME
    )

    # Constants
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def get_ml_client():
        """Initialize and return the ML Client."""
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def register_model(ml_client, model_name, job_name):
        """Register a new model."""
        model_path = f"azureml://jobs/{job_name}/outputs/artifacts/paths/model_output"
        logger.info(f"Registering model {model_name} from job {job_name} at path {model_path}.")
        run_model = Model(
            path=model_path,
            name=model_name,
            description="Model created from run.",
            type=AssetTypes.MLFLOW_MODEL,
        )
        model = ml_client.models.create_or_update(run_model)
        logger.info(f"Registered model ID: {model.id}")
        return model

    def delete_existing_endpoint(ml_client, endpoint_name):
        """Delete existing endpoint if it exists."""
        try:
            endpoint_result = ml_client.online_endpoints.get(name=endpoint_name)
            logger.info(f"Deleting existing endpoint {endpoint_name}.")
            ml_client.online_endpoints.begin_delete(name=endpoint_name).result()
            logger.info(f"Deleted existing endpoint {endpoint_name}.")
        except Exception as e:
            logger.info(f"No existing endpoint {endpoint_name} found to delete: {e}")

    def create_or_update_endpoint(ml_client, endpoint_name, description=""):
        """Create or update an endpoint."""
        delete_existing_endpoint(ml_client, endpoint_name)
        logger.info(f"Creating new endpoint {endpoint_name}.")
        endpoint = ManagedOnlineEndpoint(
            name=endpoint_name,
            description=description,
            identity=IdentityConfiguration(
                type="user_assigned",
                user_assigned_identities=[ManagedIdentityConfiguration(resource_id=AZURE_MANAGED_IDENTITY_RESOURCE_ID)]
            )
        )
        endpoint_result = ml_client.online_endpoints.begin_create_or_update(endpoint).result()
        logger.info(f"Created new endpoint {endpoint_name}.")
        return endpoint_result

    def create_or_update_deployment(ml_client, endpoint_name, deployment_name, model):
        """Create or update a deployment."""

        logger.info(f"Creating deployment {deployment_name} for endpoint {endpoint_name}.")
        deployment = ManagedOnlineDeployment(
            name=deployment_name,
            endpoint_name=endpoint_name,
            model=model.id,
            instance_type=COMPUTE_INSTANCE_TYPE,
            instance_count=1,
            environment_variables=deployment_env_vars,
            request_settings=OnlineRequestSettings(
                max_concurrent_requests_per_instance=3,
                request_timeout_ms=180000,
                max_queue_wait_ms=120000
            ),
            liveness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
            readiness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
        )
        deployment_result = ml_client.online_deployments.begin_create_or_update(deployment).result()
        logger.info(f"Created deployment {deployment.name} for endpoint {endpoint_name}.")
        return deployment_result

    def set_traffic_to_deployment(ml_client, endpoint_name, deployment_name):
        """Set traffic to the specified deployment."""
        try:
            # Fetch the current endpoint details
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Log the current traffic allocation for debugging
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Set the traffic allocation for the deployment
            endpoint.traffic = {deployment_name: 100}
            
            # Update the endpoint with the new traffic allocation
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Log the updated traffic allocation for debugging
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Log any errors that occur during the process
            logger.error(f"Failed to set traffic to deployment: {e}")
            raise


    def main():
        ml_client = get_ml_client()

        registered_model = register_model(ml_client, AZURE_MODEL_NAME, JOB_NAME)
        logger.info(f"Registered model ID: {registered_model.id}")

        endpoint = create_or_update_endpoint(ml_client, AZURE_ENDPOINT_NAME, "Endpoint for finetuned Phi-3 model")
        logger.info(f"Endpoint {AZURE_ENDPOINT_NAME} is ready.")

        try:
            deployment = create_or_update_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME, registered_model)
            logger.info(f"Deployment {AZURE_DEPLOYMENT_NAME} is created for endpoint {AZURE_ENDPOINT_NAME}.")

            set_traffic_to_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME)
            logger.info(f"Traffic is set to deployment {AZURE_DEPLOYMENT_NAME} at endpoint {AZURE_ENDPOINT_NAME}.")
        except Exception as e:
            logger.error(f"Failed to create or update deployment: {e}")

    if __name__ == "__main__":
        main()

    ```

1. Esegui le seguenti operazioni per ottenere il `JOB_NAME`:

    - Vai alla risorsa Azure Machine Learning che hai creato.
    - Seleziona **Studio web URL** per aprire lo workspace di Azure Machine Learning.
    - Seleziona **Jobs** dalla scheda a sinistra.
    - Seleziona l'esperimento di fine-tuning. Ad esempio, *finetunephi*.
    - Seleziona il job che hai creato.
- Copia e incolla il nome del tuo job in `JOB_NAME = "your-job-name"` nel file *deploy_model.py*.

1. Sostituisci `COMPUTE_INSTANCE_TYPE` con i tuoi dettagli specifici.

1. Digita il seguente comando per eseguire lo script *deploy_model.py* e avviare il processo di deployment in Azure Machine Learning.

    ```python
    python deploy_model.py
    ```


> [!WARNING]
> Per evitare addebiti aggiuntivi sul tuo account, assicurati di eliminare l'endpoint creato nel workspace di Azure Machine Learning.
>

#### Controlla lo stato del deployment nel workspace di Azure Machine Learning

1. Visita [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Naviga nel workspace di Azure Machine Learning che hai creato.

1. Seleziona **Studio web URL** per aprire il workspace di Azure Machine Learning.

1. Seleziona **Endpoints** dalla scheda laterale sinistra.

    ![Seleziona endpoints.](../../../../../../translated_images/02-03-select-endpoints.c3136326510baff109f3b7a6b6e4e9689f99b2d7bf021b057f6c0ecbd1ba90c0.it.png)

2. Seleziona l'endpoint che hai creato.

    ![Seleziona gli endpoint che hai creato.](../../../../../../translated_images/02-04-select-endpoint-created.0363e7dca51dabb4b726505fcfb7d262b0510de029dcbaf36422bb75b77f25dd.it.png)

3. In questa pagina puoi gestire gli endpoint creati durante il processo di deployment.

## Scenario 3: Integra con Prompt flow e chatta con il tuo modello personalizzato

### Integra il modello personalizzato Phi-3 con Prompt flow

Dopo aver distribuito con successo il tuo modello fine-tuned, puoi ora integrarlo con Prompt flow per utilizzare il modello in applicazioni in tempo reale, abilitando una varietà di attività interattive con il tuo modello personalizzato Phi-3.

#### Imposta la chiave API e l'URI dell'endpoint del modello Phi-3 fine-tuned

1. Naviga nel workspace di Azure Machine Learning che hai creato.
1. Seleziona **Endpoints** dalla scheda laterale sinistra.
1. Seleziona l'endpoint che hai creato.
1. Seleziona **Consume** dal menu di navigazione.
1. Copia e incolla il tuo **REST endpoint** nel file *config.py*, sostituendo `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` con il tuo **REST endpoint**.
1. Copia e incolla la tua **Primary key** nel file *config.py*, sostituendo `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` con la tua **Primary key**.

    ![Copia chiave API e URI endpoint.](../../../../../../translated_images/02-05-copy-apikey-endpoint.88b5a92e6462c53bf44401e184f65a0a088daa76a65f5df5eb4489ae40b890f6.it.png)

#### Aggiungi il codice al file *flow.dag.yml*

1. Apri il file *flow.dag.yml* in Visual Studio Code.

1. Aggiungi il seguente codice in *flow.dag.yml*.

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

#### Aggiungi il codice al file *integrate_with_promptflow.py*

1. Apri il file *integrate_with_promptflow.py* in Visual Studio Code.

1. Aggiungi il seguente codice in *integrate_with_promptflow.py*.

    ```python
    import logging
    import requests
    from promptflow.core import tool
    import asyncio
    import platform
    from config import (
        AZURE_ML_ENDPOINT,
        AZURE_ML_API_KEY
    )

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_azml_endpoint(input_data: list, endpoint_url: str, api_key: str) -> str:
        """
        Send a request to the Azure ML endpoint with the given input data.
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": [input_data],
            "params": {
                "temperature": 0.7,
                "max_new_tokens": 128,
                "do_sample": True,
                "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()[0]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    def setup_asyncio_policy():
        """
        Setup asyncio event loop policy for Windows.
        """
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            logger.info("Set Windows asyncio event loop policy.")

    @tool
    def my_python_tool(input_data: str) -> str:
        """
        Tool function to process input data and query the Azure ML endpoint.
        """
        setup_asyncio_policy()
        return query_azml_endpoint(input_data, AZURE_ML_ENDPOINT, AZURE_ML_API_KEY)

    ```

### Chatta con il tuo modello personalizzato

1. Digita il seguente comando per eseguire lo script *deploy_model.py* e avviare il processo di deployment in Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Ecco un esempio dei risultati: ora puoi chattare con il tuo modello personalizzato Phi-3. Si consiglia di porre domande basate sui dati utilizzati per il fine-tuning.

    ![Esempio di Prompt flow.](../../../../../../translated_images/02-06-promptflow-example.89384abaf3ad71f6412447c9786c562be969a8c3b19791eadffce725fa84f014.it.png)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.