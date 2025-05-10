<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-05-09T17:28:28+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "it"
}
-->
# Messa a punto e integrazione di modelli Phi-3 personalizzati con Prompt flow

Questo esempio end-to-end (E2E) si basa sulla guida "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" della Microsoft Tech Community. Illustra i processi di messa a punto, distribuzione e integrazione di modelli Phi-3 personalizzati con Prompt flow.

## Panoramica

In questo esempio E2E imparerai come mettere a punto il modello Phi-3 e integrarlo con Prompt flow. Sfruttando Azure Machine Learning e Prompt flow, creerai un flusso di lavoro per distribuire e utilizzare modelli AI personalizzati. Questo esempio E2E è suddiviso in tre scenari:

**Scenario 1: Configurare le risorse Azure e prepararsi alla messa a punto**

**Scenario 2: Mettere a punto il modello Phi-3 e distribuirlo in Azure Machine Learning Studio**

**Scenario 3: Integrare con Prompt flow e chattare con il modello personalizzato**

Ecco una panoramica di questo esempio E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.dfeb1f15c7d3c8989fb267a05ac83a25485a7230bde037df9d3d92336afc1993.it.png)

### Sommario

1. **[Scenario 1: Configurare le risorse Azure e prepararsi alla messa a punto](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Creare un workspace di Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Richiedere quote GPU nell’abbonamento Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Aggiungere assegnazione di ruolo](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Configurare il progetto](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Preparare il dataset per la messa a punto](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 2: Mettere a punto il modello Phi-3 e distribuirlo in Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Configurare Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Mettere a punto il modello Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Distribuire il modello messo a punto](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 3: Integrare con Prompt flow e chattare con il modello personalizzato](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrare il modello Phi-3 personalizzato con Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Chattare con il modello personalizzato](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenario 1: Configurare le risorse Azure e prepararsi alla messa a punto

### Creare un workspace di Azure Machine Learning

1. Digita *azure machine learning* nella **barra di ricerca** in alto nella pagina del portale e seleziona **Azure Machine Learning** tra le opzioni visualizzate.

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.321cff72d18a51c06dee2db7463868f3ca6619559a5d68b7795d70f4a8b3a683.it.png)

1. Seleziona **+ Create** dal menu di navigazione.

1. Seleziona **New workspace** dal menu di navigazione.

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.9bd9208488fcf38226fc8d3cefffecb2cb14f414f6d8d982492c1bde8634e24a.it.png)

1. Esegui le seguenti operazioni:

    - Seleziona la tua **Subscription** di Azure.
    - Seleziona il **Resource group** da utilizzare (creane uno nuovo se necessario).
    - Inserisci il **Workspace Name**. Deve essere un valore univoco.
    - Seleziona la **Regione** che desideri utilizzare.
    - Seleziona l’**account di archiviazione** da utilizzare (creane uno nuovo se necessario).
    - Seleziona il **Key vault** da utilizzare (creane uno nuovo se necessario).
    - Seleziona gli **Application insights** da utilizzare (creane uno nuovo se necessario).
    - Seleziona il **Container registry** da utilizzare (creane uno nuovo se necessario).

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.b2ebbef59952cd17d16b1f82adc252bf7616f8638d451e3c6595ffefe44f2cfa.it.png)

1. Seleziona **Review + Create**.

1. Seleziona **Create**.

### Richiedere quote GPU nell’abbonamento Azure

In questo esempio E2E utilizzerai la GPU *Standard_NC24ads_A100_v4* per la messa a punto, che richiede una richiesta di quota, e la CPU *Standard_E4s_v3* per la distribuzione, che invece non necessita di richiesta quota.

> [!NOTE]
>
> Solo gli abbonamenti Pay-As-You-Go (il tipo standard) sono idonei per l’allocazione GPU; gli abbonamenti benefit non sono attualmente supportati.
>
> Per chi usa abbonamenti benefit (come Visual Studio Enterprise Subscription) o vuole testare rapidamente il processo di messa a punto e distribuzione, questo tutorial fornisce anche indicazioni per mettere a punto con un dataset minimo usando una CPU. Tuttavia, è importante sottolineare che i risultati della messa a punto sono decisamente migliori usando una GPU con dataset più grandi.

1. Visita [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Esegui le seguenti operazioni per richiedere la quota *Standard NCADSA100v4 Family*:

    - Seleziona **Quota** dalla scheda laterale sinistra.
    - Seleziona la **Virtual machine family** da utilizzare. Ad esempio, seleziona **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, che include la GPU *Standard_NC24ads_A100_v4*.
    - Seleziona **Request quota** dal menu di navigazione.

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.ddf063c7cda9799b8ef6fbde6c3c796201578fe9078feb1c624ed75c7705ad18.it.png)

    - Nella pagina Request quota, inserisci il **New cores limit** che desideri utilizzare. Ad esempio, 24.
    - Nella pagina Request quota, seleziona **Submit** per inviare la richiesta di quota GPU.

> [!NOTE]
> Puoi scegliere la GPU o la CPU più adatta alle tue esigenze consultando il documento [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### Aggiungere assegnazione di ruolo

Per mettere a punto e distribuire i modelli, devi prima creare una User Assigned Managed Identity (UAI) e assegnarle i permessi appropriati. Questa UAI sarà utilizzata per l’autenticazione durante la distribuzione.

#### Creare una User Assigned Managed Identity (UAI)

1. Digita *managed identities* nella **barra di ricerca** in alto nella pagina del portale e seleziona **Managed Identities** tra le opzioni visualizzate.

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.8bf5dc5a4fa3e852f897ec1a983e506c2bc7b7113d159598bf0adeb66d20a5c4.it.png)

1. Seleziona **+ Create**.

    ![Select create.](../../../../../../translated_images/01-06-select-create.025632b7b54fe323f7d38edabbae05dd23f4665d0731f7143719c27c32e7e84f.it.png)

1. Esegui le seguenti operazioni:

    - Seleziona la tua **Subscription** di Azure.
    - Seleziona il **Resource group** da utilizzare (creane uno nuovo se necessario).
    - Seleziona la **Regione** che desideri utilizzare.
    - Inserisci il **Name**. Deve essere un valore univoco.

1. Seleziona **Review + create**.

1. Seleziona **+ Create**.

#### Aggiungere l’assegnazione del ruolo Contributor alla Managed Identity

1. Vai alla risorsa Managed Identity che hai creato.

1. Seleziona **Azure role assignments** dalla scheda laterale sinistra.

1. Seleziona **+Add role assignment** dal menu di navigazione.

1. Nella pagina Add role assignment, esegui le seguenti operazioni:
    - Seleziona lo **Scope** su **Resource group**.
    - Seleziona la tua **Subscription** di Azure.
    - Seleziona il **Resource group** da utilizzare.
    - Seleziona il **Role** su **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.8936866326c7cdc3b876f14657e03422cca9dbff8b193dd541a693ce34407b26.it.png)

1. Seleziona **Save**.

#### Aggiungere l’assegnazione del ruolo Storage Blob Data Reader alla Managed Identity

1. Digita *storage accounts* nella **barra di ricerca** in alto nella pagina del portale e seleziona **Storage accounts** tra le opzioni visualizzate.

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.83554a27ff3edb5099ee3fbf7f467b843dabcc0e0e5fbb829a341eab3469ffa5.it.png)

1. Seleziona l’account di archiviazione associato al workspace Azure Machine Learning che hai creato. Ad esempio, *finetunephistorage*.

1. Esegui le seguenti operazioni per navigare alla pagina Add role assignment:

    - Vai all’account di archiviazione Azure che hai creato.
    - Seleziona **Access Control (IAM)** dalla scheda laterale sinistra.
    - Seleziona **+ Add** dal menu di navigazione.
    - Seleziona **Add role assignment** dal menu di navigazione.

    ![Add role.](../../../../../../translated_images/01-09-add-role.4fef55886792c7e860da4c5a808044e6f7067fb5694f3ed4819a5758c6cc574e.it.png)

1. Nella pagina Add role assignment, esegui le seguenti operazioni:

    - Nella pagina Role, digita *Storage Blob Data Reader* nella **barra di ricerca** e seleziona **Storage Blob Data Reader** tra le opzioni visualizzate.
    - Nella pagina Role, seleziona **Next**.
    - Nella pagina Members, seleziona **Assign access to** **Managed identity**.
    - Nella pagina Members, seleziona **+ Select members**.
    - Nella pagina Select managed identities, seleziona la tua **Subscription** di Azure.
    - Nella pagina Select managed identities, seleziona la **Managed identity** su **Manage Identity**.
    - Nella pagina Select managed identities, seleziona la Managed Identity che hai creato. Ad esempio, *finetunephi-managedidentity*.
    - Nella pagina Select managed identities, seleziona **Select**.

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.fffa802e4e6ce2de4fe50e64d37d3f2ef268c2ee16f30ec6f92bd1829b5f19c1.it.png)

1. Seleziona **Review + assign**.

#### Aggiungere l’assegnazione del ruolo AcrPull alla Managed Identity

1. Digita *container registries* nella **barra di ricerca** in alto nella pagina del portale e seleziona **Container registries** tra le opzioni visualizzate.

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.62e58403d73d16a0cc715571c8a7b4105a0e97b1422aa5f26106aff1c0e8a47d.it.png)

1. Seleziona il container registry associato al workspace Azure Machine Learning. Ad esempio, *finetunephicontainerregistries*.

1. Esegui le seguenti operazioni per navigare alla pagina Add role assignment:

    - Seleziona **Access Control (IAM)** dalla scheda laterale sinistra.
    - Seleziona **+ Add** dal menu di navigazione.
    - Seleziona **Add role assignment** dal menu di navigazione.

1. Nella pagina Add role assignment, esegui le seguenti operazioni:

    - Nella pagina Role, digita *AcrPull* nella **barra di ricerca** e seleziona **AcrPull** tra le opzioni visualizzate.
    - Nella pagina Role, seleziona **Next**.
    - Nella pagina Members, seleziona **Assign access to** **Managed identity**.
    - Nella pagina Members, seleziona **+ Select members**.
    - Nella pagina Select managed identities, seleziona la tua **Subscription** di Azure.
    - Nella pagina Select managed identities, seleziona la **Managed identity** su **Manage Identity**.
    - Nella pagina Select managed identities, seleziona la Managed Identity che hai creato. Ad esempio, *finetunephi-managedidentity*.
    - Nella pagina Select managed identities, seleziona **Select**.
    - Seleziona **Review + assign**.

### Configurare il progetto

Ora creerai una cartella di lavoro e configurerai un ambiente virtuale per sviluppare un programma che interagisce con gli utenti e utilizza la cronologia delle chat memorizzata in Azure Cosmos DB per informare le risposte.

#### Creare una cartella di lavoro

1. Apri una finestra del terminale e digita il seguente comando per creare una cartella chiamata *finetune-phi* nel percorso predefinito.

    ```console
    mkdir finetune-phi
    ```

1. Digita il seguente comando nel terminale per navigare nella cartella *finetune-phi* appena creata.

    ```console
    cd finetune-phi
    ```

#### Creare un ambiente virtuale

1. Digita il seguente comando nel terminale per creare un ambiente virtuale chiamato *.venv*.

    ```console
    python -m venv .venv
    ```

1. Digita il seguente comando nel terminale per attivare l’ambiente virtuale.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> Se tutto è andato a buon fine, dovresti vedere *(.venv)* prima del prompt dei comandi.

#### Installare i pacchetti necessari

1. Digita i seguenti comandi nel terminale per installare i pacchetti richiesti.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Creare i file di progetto

In questo esercizio creerai i file essenziali per il progetto. Questi includono script per scaricare il dataset, configurare l’ambiente Azure Machine Learning, mettere a punto il modello Phi-3 e distribuire il modello messo a punto. Creerai anche un file *conda.yml* per configurare l’ambiente di messa a punto.

In questo esercizio:

- Crea un file *download_dataset.py* per scaricare il dataset.
- Crea un file *setup_ml.py* per configurare l’ambiente Azure Machine Learning.
- Crea un file *fine_tune.py* nella cartella *finetuning_dir* per mettere a punto il modello Phi-3 usando il dataset.
- Crea un file *conda.yml* per configurare l’ambiente di messa a punto.
- Crea un file *deploy_model.py* per distribuire il modello messo a punto.
- Crea un file *integrate_with_promptflow.py* per integrare il modello messo a punto ed eseguirlo con Prompt flow.
- Crea un file *flow.dag.yml* per impostare la struttura del workflow per Prompt flow.
- Crea un file *config.py* per inserire le informazioni di Azure.

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

1. Dal menu, seleziona **File**.

1. Seleziona **Open Folder**.

1. Seleziona la cartella *finetune-phi* che hai creato, situata in *C:\Users\yourUserName\finetune-phi*.

    ![Open project floder.](../../../../../../translated_images/01-12-open-project-folder.1f7f0f79e5d4d62e546e906e1ce5a480cd98d06062ce292b7b99c6cfcd434fdf.it.png)

1. Nel pannello a sinistra di Visual Studio Code, fai clic destro e seleziona **New File** per creare un nuovo file chiamato *download_dataset.py*.

1. Nel pannello a sinistra di Visual Studio Code, fai clic destro e seleziona **New File** per creare un nuovo file chiamato *setup_ml.py*.

1. Nel pannello a sinistra di Visual Studio Code, fai clic destro e seleziona **New File** per creare un nuovo file chiamato *deploy_model.py*.

    ![Create new file.](../../../../../../translated_images/01-13-create-new-file.40698c2e0415929e7b6dc2b30925677e413f965bac4134d3aefa0b44d443deaf.it.png)

1. Nel pannello a sinistra di Visual Studio Code, fai clic destro e seleziona **New Folder** per creare una nuova cartella chiamata *finetuning_dir*.

1. Nella cartella *finetuning_dir*, crea un nuovo file chiamato *fine_tune.py*.

#### Creare e configurare il file *conda.yml*

1. Nel pannello a sinistra di Visual Studio Code, fai clic destro e seleziona **New File** per creare un nuovo file chiamato *conda.yml*.

1. Aggiungi il seguente codice al file *conda.yml* per configurare l’ambiente di messa a punto per il modello Phi-3.

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

#### Creare e configurare il file *config.py*

1. Nel pannello a sinistra di Visual Studio Code, fai clic destro e seleziona **New File** per creare un nuovo file chiamato *config.py*.

1. Aggiungi il seguente codice al file *config.py* per includere le tue informazioni Azure.

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

#### Aggiungere le variabili d’ambiente di Azure

1. Esegui le seguenti operazioni per aggiungere l’ID dell’abbonamento Azure:

    - Digita *subscriptions* nella **barra di ricerca** in alto nella pagina del portale e seleziona **Subscriptions** tra le opzioni visualizzate.
    - Seleziona l’abbonamento Azure che stai utilizzando.
    - Copia e incolla l’ID dell’abbonamento nel file *config.py*.
![Trova l'ID della sottoscrizione.](../../../../../../translated_images/01-14-find-subscriptionid.4daef33360f6d3808a9f1acea2b6b6121c498c75c36cb6ecc6c6b211f0d3b725.it.png)

1. Esegui le seguenti operazioni per aggiungere il nome dell'Azure Workspace:

    - Vai alla risorsa Azure Machine Learning che hai creato.
    - Copia e incolla il nome del tuo account nel file *config.py*.

    ![Trova il nome di Azure Machine Learning.](../../../../../../translated_images/01-15-find-AZML-name.c8efdc5a8f2e594260004695c145fafb4fd903e96715f495a43733560cd706b5.it.png)

1. Esegui le seguenti operazioni per aggiungere il nome del Resource Group di Azure:

    - Vai alla risorsa Azure Machine Learning che hai creato.
    - Copia e incolla il nome del tuo Resource Group di Azure nel file *config.py*.

    ![Trova il nome del resource group.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.0647be51d3f1b8183995949df5866455e5532ef1c3d1f93b33dc9a91d615e882.it.png)

2. Esegui le seguenti operazioni per aggiungere il nome dell'Azure Managed Identity

    - Vai alla risorsa Managed Identities che hai creato.
    - Copia e incolla il nome della tua Azure Managed Identity nel file *config.py*.

    ![Trova UAI.](../../../../../../translated_images/01-17-find-uai.b0fe7164cacc93b03c3c534daee68da244de6de4e6dcbc2a4e9df43403eb0f1b.it.png)

### Prepara il dataset per il fine-tuning

In questo esercizio eseguirai il file *download_dataset.py* per scaricare i dataset *ULTRACHAT_200k* nel tuo ambiente locale. Successivamente utilizzerai questi dataset per effettuare il fine-tuning del modello Phi-3 in Azure Machine Learning.

#### Scarica il tuo dataset usando *download_dataset.py*

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
> Se vuoi usare una CPU per il fine-tuning, questo metodo è ideale per chi ha sottoscrizioni con vantaggi (come Visual Studio Enterprise Subscription) o per testare rapidamente il processo di fine-tuning e deployment.
>
> Sostituisci `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` with `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
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
> In questo esempio end-to-end, usi solo l'1% del dataset (`train_sft[:1%]`). Questo riduce significativamente la quantità di dati, velocizzando sia l'upload che il processo di fine-tuning. Puoi regolare la percentuale per trovare il giusto equilibrio tra tempo di addestramento e performance del modello. Usare un sottoinsieme più piccolo del dataset riduce il tempo necessario per il fine-tuning, rendendo il processo più gestibile per un esempio end-to-end.

## Scenario 2: Fine-tuning del modello Phi-3 e deployment in Azure Machine Learning Studio

### Configura Azure CLI

Devi configurare Azure CLI per autenticare il tuo ambiente. Azure CLI ti permette di gestire le risorse Azure direttamente da riga di comando e fornisce le credenziali necessarie ad Azure Machine Learning per accedere a queste risorse. Per iniziare, installa [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. Apri una finestra del terminale e digita il seguente comando per effettuare il login al tuo account Azure.

    ```console
    az login
    ```

1. Seleziona l'account Azure da utilizzare.

1. Seleziona la sottoscrizione Azure da utilizzare.

    ![Trova il nome del resource group.](../../../../../../translated_images/02-01-login-using-azure-cli.b6e8fb6255e8d09673cb48eca2b12aebbb84dfb8817af8a6b1dfd4bb2759d68f.it.png)

> [!TIP]
>
> Se riscontri problemi nel login ad Azure, prova a usare un codice dispositivo. Apri una finestra del terminale e digita il seguente comando per accedere al tuo account Azure:
>
> ```console
> az login --use-device-code
> ```
>

### Fine-tuning del modello Phi-3

In questo esercizio eseguirai il fine-tuning del modello Phi-3 utilizzando il dataset fornito. Prima definirai il processo di fine-tuning nel file *fine_tune.py*. Poi configurerai l'ambiente Azure Machine Learning e avvierai il processo di fine-tuning eseguendo il file *setup_ml.py*. Questo script garantisce che il fine-tuning avvenga all'interno dell'ambiente Azure Machine Learning.

Eseguendo *setup_ml.py* avvierai il processo di fine-tuning nell'ambiente Azure Machine Learning.

#### Aggiungi codice al file *fine_tune.py*

1. Vai alla cartella *finetuning_dir* e apri il file *fine_tune.py* in Visual Studio Code.

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
> Nel file *fine_tune.py* puoi modificare il campo `pretrained_model_name` from `"microsoft/Phi-3-mini-4k-instruct"` to any model you want to fine-tune. For example, if you change it to `"microsoft/Phi-3.5-mini-instruct"`, you'll be using the Phi-3.5-mini-instruct model for fine-tuning. To find and use the model name you prefer, visit [Hugging Face](https://huggingface.co/), search for the model you're interested in, and then copy and paste its name into the `pretrained_model_name` nel tuo script.
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Fine tune Phi-3.5.":::
>

#### Aggiungi codice al file *setup_ml.py*

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

1. Sostituisci `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `LOCATION` con i tuoi dettagli specifici.

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
> Se vuoi usare una CPU per il fine-tuning, questo metodo è ideale per chi ha sottoscrizioni con vantaggi (come Visual Studio Enterprise Subscription) o per testare rapidamente il processo di fine-tuning e deployment.
>
> 1. Apri il file *setup_ml*.
> 1. Sostituisci `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `DOCKER_IMAGE_NAME` with the following. If you do not have access to *Standard_E16s_v3*, you can use an equivalent CPU instance or request a new quota.
> 1. Replace `LOCATION` con i tuoi dettagli specifici.
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

1. In questo esercizio hai effettuato con successo il fine-tuning del modello Phi-3 usando Azure Machine Learning. Eseguendo lo script *setup_ml.py* hai configurato l'ambiente Azure Machine Learning e avviato il processo di fine-tuning definito nel file *fine_tune.py*. Tieni presente che il processo di fine-tuning può richiedere un tempo considerevole. Dopo aver eseguito il comando `python setup_ml.py` command, you need to wait for the process to complete. You can monitor the status of the fine-tuning job by following the link provided in the terminal to the Azure Machine Learning portal.

    ![See finetuning job.](../../../../../../translated_images/02-02-see-finetuning-job.a28c8552f7b7bc088ccd67dd0c522f7fc1944048d3554bb1b24f95a1169ad538.it.png)

### Deploy the fine-tuned model

To integrate the fine-tuned Phi-3 model with Prompt Flow, you need to deploy the model to make it accessible for real-time inference. This process involves registering the model, creating an online endpoint, and deploying the model.

#### Set the model name, endpoint name, and deployment name for deployment

1. Open *config.py* file.

1. Replace `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` with the desired name for your model.

1. Replace `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` with the desired name for your endpoint.

1. Replace `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` con il nome desiderato per il tuo deployment.

#### Aggiungi codice al file *deploy_model.py*

Eseguendo il file *deploy_model.py* automatizzi l'intero processo di deployment. Questo registra il modello, crea un endpoint ed esegue il deployment in base alle impostazioni specificate nel file config.py, che include il nome del modello, il nome dell'endpoint e il nome del deployment.

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

1. Esegui le seguenti operazioni per ottenere `JOB_NAME`:

    - Navigate to Azure Machine Learning resource that you created.
    - Select **Studio web URL** to open the Azure Machine Learning workspace.
    - Select **Jobs** from the left side tab.
    - Select the experiment for fine-tuning. For example, *finetunephi*.
    - Select the job that you created.
    - Copy and paste your job Name into the `JOB_NAME = "your-job-name"` in *deploy_model.py* file.

1. Replace `COMPUTE_INSTANCE_TYPE` con i tuoi dettagli specifici.

1. Digita il seguente comando per eseguire lo script *deploy_model.py* e avviare il processo di deployment in Azure Machine Learning.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> Per evitare costi aggiuntivi sul tuo account, assicurati di eliminare l'endpoint creato nel workspace Azure Machine Learning.
>

#### Verifica lo stato del deployment nel workspace Azure Machine Learning

1. Visita [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vai al workspace Azure Machine Learning che hai creato.

1. Seleziona **Studio web URL** per aprire il workspace Azure Machine Learning.

1. Seleziona **Endpoints** dalla barra laterale sinistra.

    ![Seleziona endpoints.](../../../../../../translated_images/02-03-select-endpoints.a32f4eb2854cd54ee997f9bec0e842c3084bbc24bd693457b5c6b132fe966bf4.it.png)

2. Seleziona l'endpoint che hai creato.

    ![Seleziona l'endpoint che hai creato.](../../../../../../translated_images/02-04-select-endpoint-created.048b4f0f6479c1885b62711a151227a24408679be65dd1039cd2f64448ec5842.it.png)

3. In questa pagina puoi gestire gli endpoint creati durante il processo di deployment.

## Scenario 3: Integra con Prompt flow e chatta con il tuo modello personalizzato

### Integra il modello personalizzato Phi-3 con Prompt flow

Dopo aver distribuito con successo il tuo modello fine-tuned, puoi ora integrarlo con Prompt flow per usarlo in applicazioni in tempo reale, abilitando diverse attività interattive con il tuo modello Phi-3 personalizzato.

#### Imposta la chiave API e l'URI dell'endpoint del modello Phi-3 fine-tuned

1. Vai al workspace Azure Machine Learning che hai creato.
1. Seleziona **Endpoints** dalla barra laterale sinistra.
1. Seleziona l'endpoint che hai creato.
1. Seleziona **Consume** dal menu di navigazione.
1. Copia e incolla il tuo **REST endpoint** nel file *config.py*, sostituendo `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` with your **REST endpoint**.
1. Copy and paste your **Primary key** into the *config.py* file, replacing `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` con la tua **Primary key**.

    ![Copia chiave API e URI endpoint.](../../../../../../translated_images/02-05-copy-apikey-endpoint.602de7450770e9984149dc7da7472bacafbf0e8447e2adb53896ad93b1dc7684.it.png)

#### Aggiungi codice al file *flow.dag.yml*

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

#### Aggiungi codice al file *integrate_with_promptflow.py*

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

1. Ecco un esempio dei risultati: ora puoi chattare con il tuo modello Phi-3 personalizzato. Si consiglia di porre domande basate sui dati usati per il fine-tuning.

    ![Esempio di Prompt flow.](../../../../../../translated_images/02-06-promptflow-example.023c07a4be8f02199e04eaf49f40ba24415da1be2274cbda9a7aa39776acd0bb.it.png)

**Avvertenza**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua madre deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un esperto umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.