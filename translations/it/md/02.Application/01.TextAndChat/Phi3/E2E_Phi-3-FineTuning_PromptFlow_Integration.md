<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7ca2c30fdb802664070e9cfbf92e24fe",
  "translation_date": "2026-01-05T03:10:46+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "it"
}
-->
# Messa a punto e integrazione dei modelli Phi-3 personalizzati con Prompt flow

Questo esempio end-to-end (E2E) si basa sulla guida "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" dalla Microsoft Tech Community. Introduce i processi di messa a punto, distribuzione e integrazione dei modelli Phi-3 personalizzati con Prompt flow.

## Panoramica

In questo esempio E2E, imparerai come mettere a punto il modello Phi-3 e integrarlo con Prompt flow. Sfruttando Azure Machine Learning e Prompt flow, stabilirai un flusso di lavoro per distribuire e utilizzare modelli di IA personalizzati. Questo esempio E2E è suddiviso in tre scenari:

**Scenario 1: Configurare le risorse di Azure e prepararsi alla messa a punto**

**Scenario 2: Messa a punto del modello Phi-3 e distribuzione in Azure Machine Learning Studio**

**Scenario 3: Integrazione con Prompt flow e chat con il tuo modello personalizzato**

Ecco una panoramica di questo esempio E2E.

![Panoramica Phi-3-FineTuning_PromptFlow_Integration](../../../../../../translated_images/00-01-architecture.02fc569e266d468c.it.png)

### Indice

1. **[Scenario 1: Configurare le risorse di Azure e prepararsi alla messa a punto](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Creare un'area di lavoro Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Richiedere quote GPU nella sottoscrizione Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Aggiungere assegnazione del ruolo](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Impostare il progetto](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Preparare il dataset per la messa a punto](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 2: Messa a punto del modello Phi-3 e distribuzione in Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Impostare Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Mettere a punto il modello Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Distribuire il modello messo a punto](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 3: Integrare con Prompt flow e chattare con il tuo modello personalizzato](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrare il modello Phi-3 personalizzato con Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Chattare con il tuo modello personalizzato](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenario 1: Configurare le risorse di Azure e prepararsi alla messa a punto

### Creare un'area di lavoro Azure Machine Learning

1. Digita *azure machine learning* nella **barra di ricerca** nella parte superiore della pagina del portale e seleziona **Azure Machine Learning** dalle opzioni che compaiono.

    ![Digita azure machine learning](../../../../../../translated_images/01-01-type-azml.a5116f8454d98c60.it.png)

1. Seleziona **+ Crea** dal menu di navigazione.

1. Seleziona **Nuovo workspace** dal menu di navigazione.

    ![Seleziona nuovo workspace](../../../../../../translated_images/01-02-select-new-workspace.83e17436f8898dc4.it.png)

1. Esegui le seguenti operazioni:

    - Seleziona la tua Azure **Sottoscrizione**.
    - Seleziona il **Gruppo di risorse** da usare (creane uno nuovo se necessario).
    - Inserisci il **Nome area di lavoro**. Deve essere un valore univoco.
    - Seleziona la **Regione** che desideri utilizzare.
    - Seleziona l'**Account di archiviazione** da usare (creane uno nuovo se necessario).
    - Seleziona il **Key vault** da usare (creane uno nuovo se necessario).
    - Seleziona le **Application Insights** da usare (creane uno nuove se necessario).
    - Seleziona il **Container registry** da usare (creane uno nuovo se necessario).

    ![Compila AZML.](../../../../../../translated_images/01-03-fill-AZML.730a5177757bbebb.it.png)

1. Seleziona **Rivedi + Crea**.

1. Seleziona **Crea**.

### Richiedere quote GPU nella sottoscrizione Azure

In questo esempio E2E, utilizzerai la *Standard_NC24ads_A100_v4 GPU* per la messa a punto, che richiede una richiesta di quota, e la *Standard_E4s_v3* CPU per la distribuzione, che non richiede una richiesta di quota.

> [!NOTE]
>
> Solo le sottoscrizioni Pay-As-You-Go (il tipo di sottoscrizione standard) sono idonee per l'allocazione GPU; le sottoscrizioni benefit non sono attualmente supportate.
>
> Per chi utilizza sottoscrizioni benefit (come Visual Studio Enterprise Subscription) o per chi desidera testare rapidamente il processo di messa a punto e distribuzione, questo tutorial fornisce anche indicazioni per mettere a punto con un set di dati minimale utilizzando una CPU. Tuttavia, è importante notare che i risultati della messa a punto sono significativamente migliori quando si utilizza una GPU con set di dati più grandi.

1. Visita [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Esegui le seguenti operazioni per richiedere la quota *Standard NCADSA100v4 Family*:

    - Seleziona **Quota** dalla scheda a sinistra.
    - Seleziona la **famiglia di macchine virtuali** da utilizzare. Ad esempio, seleziona **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, che include la *Standard_NC24ads_A100_v4* GPU.
    - Seleziona **Request quota** dal menu di navigazione.

        ![Richiedi quota.](../../../../../../translated_images/01-04-request-quota.3d3670c3221ab834.it.png)

    - Nella pagina Request quota, inserisci il **New cores limit** che desideri utilizzare. Ad esempio, 24.
    - Nella pagina Request quota, seleziona **Submit** per richiedere la quota GPU.

> [!NOTE]
> Puoi selezionare la GPU o la CPU appropriata per le tue esigenze facendo riferimento al documento [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### Aggiungi assegnazione del ruolo

Per mettere a punto e distribuire i tuoi modelli, è necessario creare prima un'Identity Gestita Assegnata dall'Utente (User Assigned Managed Identity, UAI) e assegnarle le autorizzazioni appropriate. Questa UAI verrà utilizzata per l'autenticazione durante la distribuzione

#### Crea un'Identity Gestita Assegnata dall'Utente (UAI)

1. Digita *managed identities* nella **barra di ricerca** nella parte superiore della pagina del portale e seleziona **Managed Identities** dalle opzioni che compaiono.

    ![Digita managed identities.](../../../../../../translated_images/01-05-type-managed-identities.9297b6039874eff8.it.png)

1. Seleziona **+ Crea**.

    ![Seleziona crea.](../../../../../../translated_images/01-06-select-create.936d8d66d7144f9a.it.png)

1. Esegui le seguenti operazioni:

    - Seleziona la tua Azure **Sottoscrizione**.
    - Seleziona il **Gruppo di risorse** da usare (creane uno nuovo se necessario).
    - Seleziona la **Regione** che desideri utilizzare.
    - Inserisci il **Nome**. Deve essere un valore univoco.

1. Seleziona **Rivedi + crea**.

1. Seleziona **+ Crea**.

#### Aggiungi l'assegnazione del ruolo Contributor all'Identity gestita

1. Vai alla risorsa Managed Identity che hai creato.

1. Seleziona **Azure role assignments** dalla scheda a sinistra.

1. Seleziona **+Add role assignment** dal menu di navigazione.

1. Nella pagina Add role assignment, esegui le seguenti operazioni:
    - Seleziona lo **Scope** su **Resource group**.
    - Seleziona la tua Azure **Sottoscrizione**.
    - Seleziona il **Gruppo di risorse** da usare.
    - Seleziona il **Ruolo** su **Contributor**.

    ![Compila ruolo Contributor.](../../../../../../translated_images/01-07-fill-contributor-role.29ca99b7c9f687e0.it.png)

1. Seleziona **Salva**.

#### Aggiungi l'assegnazione del ruolo Storage Blob Data Reader all'Identity gestita

1. Digita *storage accounts* nella **barra di ricerca** nella parte superiore della pagina del portale e seleziona **Storage accounts** dalle opzioni che compaiono.

    ![Digita storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.1186c8e42933e49b.it.png)

1. Seleziona l'account di archiviazione associato all'area di lavoro Azure Machine Learning che hai creato. Ad esempio, *finetunephistorage*.

1. Esegui le seguenti operazioni per navigare alla pagina per aggiungere l'assegnazione del ruolo:

    - Vai all'account di archiviazione Azure che hai creato.
    - Seleziona **Access Control (IAM)** dalla scheda a sinistra.
    - Seleziona **+ Add** dal menu di navigazione.
    - Seleziona **Add role assignment** dal menu di navigazione.

    ![Aggiungi ruolo.](../../../../../../translated_images/01-09-add-role.d2db22fec1b187f0.it.png)

1. Nella pagina Add role assignment, esegui le seguenti operazioni:

    - Nella pagina Role, digita *Storage Blob Data Reader* nella **barra di ricerca** e seleziona **Storage Blob Data Reader** dalle opzioni che compaiono.
    - Nella pagina Role, seleziona **Next**.
    - Nella pagina Members, seleziona **Assign access to** **Managed identity**.
    - Nella pagina Members, seleziona **+ Select members**.
    - Nella pagina Select managed identities, seleziona la tua Azure **Sottoscrizione**.
    - Nella pagina Select managed identities, seleziona la **Managed identity** come **Manage Identity**.
    - Nella pagina Select managed identities, seleziona la Manage Identity che hai creato. Ad esempio, *finetunephi-managedidentity*.
    - Nella pagina Select managed identities, seleziona **Select**.

    ![Seleziona managed identity.](../../../../../../translated_images/01-10-select-managed-identity.5ce5ba181f72a4df.it.png)

1. Seleziona **Rivedi + assegna**.

#### Aggiungi l'assegnazione del ruolo AcrPull all'Identity gestita

1. Digita *container registries* nella **barra di ricerca** nella parte superiore della pagina del portale e seleziona **Container registries** dalle opzioni che compaiono.

    ![Digita container registries.](../../../../../../translated_images/01-11-type-container-registries.ff3b8bdc49dc596c.it.png)

1. Seleziona il registro dei container associato all'area di lavoro Azure Machine Learning. Ad esempio, *finetunephicontainerregistries*

1. Esegui le seguenti operazioni per navigare alla pagina per aggiungere l'assegnazione del ruolo:

    - Seleziona **Access Control (IAM)** dalla scheda a sinistra.
    - Seleziona **+ Add** dal menu di navigazione.
    - Seleziona **Add role assignment** dal menu di navigazione.

1. Nella pagina Add role assignment, esegui le seguenti operazioni:

    - Nella pagina Role, digita *AcrPull* nella **barra di ricerca** e seleziona **AcrPull** dalle opzioni che compaiono.
    - Nella pagina Role, seleziona **Next**.
    - Nella pagina Members, seleziona **Assign access to** **Managed identity**.
    - Nella pagina Members, seleziona **+ Select members**.
    - Nella pagina Select managed identities, seleziona la tua Azure **Sottoscrizione**.
    - Nella pagina Select managed identities, seleziona la **Managed identity** come **Manage Identity**.
    - Nella pagina Select managed identities, seleziona la Manage Identity che hai creato. Ad esempio, *finetunephi-managedidentity*.
    - Nella pagina Select managed identities, seleziona **Select**.
    - Seleziona **Rivedi + assegna**.

### Imposta il progetto

Ora, creerai una cartella in cui lavorare e configurerai un ambiente virtuale per sviluppare un programma che interagisca con gli utenti e utilizzi la cronologia delle chat memorizzata in Azure Cosmos DB per informare le sue risposte.

#### Crea una cartella in cui lavorare

1. Apri una finestra del terminale e digita il seguente comando per creare una cartella chiamata *finetune-phi* nel percorso predefinito.

    ```console
    mkdir finetune-phi
    ```

1. Digita il seguente comando nel terminale per navigare nella cartella *finetune-phi* che hai creato.

    ```console
    cd finetune-phi
    ```

#### Crea un ambiente virtuale

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

1. Digita i seguenti comandi nel terminale per installare i pacchetti richiesti.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Crea i file del progetto
In questo esercizio, creerai i file essenziali per il nostro progetto. Questi file includono script per scaricare il dataset, configurare l'ambiente Azure Machine Learning, mettere a punto il modello Phi-3 e distribuire il modello messo a punto. Creerai inoltre un file *conda.yml* per configurare l'ambiente di fine-tuning.

In questo esercizio, eseguirai:

- Crea un file *download_dataset.py* per scaricare il dataset.
- Crea un file *setup_ml.py* per configurare l'ambiente Azure Machine Learning.
- Crea un file *fine_tune.py* nella cartella *finetuning_dir* per mettere a punto il modello Phi-3 usando il dataset.
- Crea un file *conda.yml* per configurare l'ambiente di fine-tuning.
- Crea un file *deploy_model.py* per distribuire il modello messo a punto.
- Crea un file *integrate_with_promptflow.py* per integrare il modello messo a punto ed eseguire il modello usando Prompt flow.
- Crea un file flow.dag.yml per impostare la struttura del workflow per Prompt flow.
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

1. Seleziona **File** dalla barra dei menu.

1. Seleziona **Open Folder**.

1. Seleziona la cartella *finetune-phi* che hai creato, situata in *C:\Users\yourUserName\finetune-phi*.

    ![Apri la cartella del progetto.](../../../../../../translated_images/01-12-open-project-folder.1fff9c7f41dd1639.it.png)

1. Nel riquadro a sinistra di Visual Studio Code, fai clic con il tasto destro e seleziona **New File** per creare un nuovo file chiamato *download_dataset.py*.

1. Nel riquadro a sinistra di Visual Studio Code, fai clic con il tasto destro e seleziona **New File** per creare un nuovo file chiamato *setup_ml.py*.

1. Nel riquadro a sinistra di Visual Studio Code, fai clic con il tasto destro e seleziona **New File** per creare un nuovo file chiamato *deploy_model.py*.

    ![Crea nuovo file.](../../../../../../translated_images/01-13-create-new-file.c17c150fff384a39.it.png)

1. Nel riquadro a sinistra di Visual Studio Code, fai clic con il tasto destro e seleziona **New Folder** per creare una nuova cartella chiamata *finetuning_dir*.

1. Nella cartella *finetuning_dir*, crea un nuovo file chiamato *fine_tune.py*.

#### Create and Configure *conda.yml* file

1. Nel riquadro a sinistra di Visual Studio Code, fai clic con il tasto destro e seleziona **New File** per creare un nuovo file chiamato *conda.yml*.

1. Aggiungi il codice seguente al file *conda.yml* per configurare l'ambiente di fine-tuning per il modello Phi-3.

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

#### Create and Configure *config.py* file

1. Nel riquadro a sinistra di Visual Studio Code, fai clic con il tasto destro e seleziona **New File** per creare un nuovo file chiamato *config.py*.

1. Aggiungi il codice seguente al file *config.py* per includere le tue informazioni di Azure.

    ```python
    # Impostazioni di Azure
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Impostazioni di Azure Machine Learning
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Impostazioni dell'identità gestita di Azure
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Percorsi dei file del dataset
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Impostazioni del modello messo a punto
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### Add Azure environment variables

1. Esegui le seguenti operazioni per aggiungere l'ID di sottoscrizione di Azure:

    - Digita *subscriptions* nella **barra di ricerca** in alto nella pagina del portale e seleziona **Subscriptions** dalle opzioni che appaiono.
    - Seleziona la sottoscrizione Azure che stai utilizzando.
    - Copia e incolla il tuo Subscription ID nel file *config.py*.

    ![Trova subscription id.](../../../../../../translated_images/01-14-find-subscriptionid.4f4ca33555f1e637.it.png)

1. Esegui le seguenti operazioni per aggiungere il nome del Workspace di Azure:

    - Vai alla risorsa Azure Machine Learning che hai creato.
    - Copia e incolla il nome del tuo account nel file *config.py*.

    ![Trova il nome di Azure Machine Learning.](../../../../../../translated_images/01-15-find-AZML-name.1975f0422bca19a7.it.png)

1. Esegui le seguenti operazioni per aggiungere il nome del Resource Group di Azure:

    - Vai alla risorsa Azure Machine Learning che hai creato.
    - Copia e incolla il nome del tuo Azure Resource Group nel file *config.py*.

    ![Trova il nome del resource group.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.855a349d0af134a3.it.png)

2. Esegui le seguenti operazioni per aggiungere il nome dell'Azure Managed Identity

    - Vai alla risorsa Managed Identities che hai creato.
    - Copia e incolla il nome della tua Azure Managed Identity nel file *config.py*.

    ![Trova UAI.](../../../../../../translated_images/01-17-find-uai.3529464f53499827.it.png)

### Prepara il dataset per la messa a punto

In questo esercizio, eseguirai il file *download_dataset.py* per scaricare i dataset *ULTRACHAT_200k* nel tuo ambiente locale. Utilizzerai quindi questi dataset per mettere a punto il modello Phi-3 in Azure Machine Learning.

#### Scarica il dataset usando *download_dataset.py*

1. Apri il file *download_dataset.py* in Visual Studio Code.

1. Aggiungi il codice seguente in *download_dataset.py*.

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
        # Carica il dataset con il nome, la configurazione e il rapporto di suddivisione specificati
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Suddividi il dataset in set di addestramento e test (80% addestramento, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Crea la directory se non esiste
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Apri il file in modalità scrittura
        with open(filepath, 'w', encoding='utf-8') as f:
            # Itera su ogni record nel dataset
            for record in dataset:
                # Serializza il record come oggetto JSON e scrivilo nel file
                json.dump(record, f)
                # Scrivi una nuova riga per separare i record
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Carica e suddividi il dataset ULTRACHAT_200k con una configurazione specifica e un rapporto di suddivisione
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Estrai i dataset di addestramento e test dalla suddivisione
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Salva il dataset di addestramento in un file JSONL
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Salva il dataset di test in un file JSONL separato
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **Indicazioni per la messa a punto con un dataset minimo usando una CPU**
>
> Se vuoi usare una CPU per la messa a punto, questo approccio è ideale per chi ha sottoscrizioni con vantaggi (come Visual Studio Enterprise Subscription) o per testare rapidamente il processo di messa a punto e distribuzione.
>
> Sostituisci `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` con `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Digita il comando seguente nel tuo terminale per eseguire lo script e scaricare il dataset nel tuo ambiente locale.

    ```console
    python download_data.py
    ```

1. Verifica che i dataset siano stati salvati correttamente nella tua directory locale *finetune-phi/data*.

> [!NOTE]
>
> **Dimensione del dataset e tempo di messa a punto**
>
> In questo esempio E2E, usi solo l'1% del dataset (`train_sft[:1%]`). Questo riduce significativamente la quantità di dati, accelerando sia il caricamento che i processi di messa a punto. Puoi regolare la percentuale per trovare il giusto equilibrio tra tempo di addestramento e prestazioni del modello. L'uso di un sottoinsieme più piccolo del dataset riduce il tempo necessario per la messa a punto, rendendo il processo più gestibile per un esempio E2E.

## Scenario 2: Mettere a punto il modello Phi-3 e distribuire in Azure Machine Learning Studio

### Configura Azure CLI

Devi configurare Azure CLI per autenticare il tuo ambiente. Azure CLI ti consente di gestire le risorse Azure direttamente dalla riga di comando e fornisce le credenziali necessarie ad Azure Machine Learning per accedere a queste risorse. Per iniziare, installa [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. Apri una finestra del terminale e digita il comando seguente per eseguire l'accesso al tuo account Azure.

    ```console
    az login
    ```

1. Seleziona l'account Azure da usare.

1. Seleziona la sottoscrizione Azure da usare.

    ![Trova il nome del resource group.](../../../../../../translated_images/02-01-login-using-azure-cli.dfde31cb75e58a87.it.png)

> [!TIP]
>
> Se riscontri problemi nell'accesso ad Azure, prova a usare un device code. Apri una finestra del terminale e digita il comando seguente per effettuare l'accesso al tuo account Azure:
>
> ```console
> az login --use-device-code
> ```
>

### Mettere a punto il modello Phi-3

In questo esercizio, metterai a punto il modello Phi-3 usando il dataset fornito. Prima definirai il processo di messa a punto nel file *fine_tune.py*. Poi configurerai l'ambiente Azure Machine Learning e avvierai il processo di messa a punto eseguendo il file *setup_ml.py*. Questo script assicura che la messa a punto avvenga all'interno dell'ambiente Azure Machine Learning.

Eseguendo *setup_ml.py*, avvierai il processo di messa a punto nell'ambiente Azure Machine Learning.

#### Aggiungi codice al file *fine_tune.py*

1. Vai nella cartella *finetuning_dir* e apri il file *fine_tune.py* in Visual Studio Code.

1. Aggiungi il codice seguente in *fine_tune.py*.

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

    # Per evitare l'errore INVALID_PARAMETER_VALUE in MLflow, disabilita l'integrazione di MLflow
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Configurazione del logging
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
> **Puoi mettere a punto il modello Phi-3.5**
>
> Nel file *fine_tune.py*, puoi modificare il valore di `pretrained_model_name` da `"microsoft/Phi-3-mini-4k-instruct"` a qualsiasi modello tu voglia mettere a punto. Ad esempio, se lo cambi in `"microsoft/Phi-3.5-mini-instruct"`, userai il modello Phi-3.5-mini-instruct per la messa a punto. Per trovare e usare il nome del modello che preferisci, visita [Hugging Face](https://huggingface.co/), cerca il modello di tuo interesse e poi copia e incolla il suo nome nel campo `pretrained_model_name` nel tuo script.
>
> <image type="content" src="../../../../imgs/02/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Messa a punto di Phi-3.5.">
>

#### Aggiungi codice al file *setup_ml.py*

1. Apri il file *setup_ml.py* in Visual Studio Code.

1. Aggiungi il codice seguente in *setup_ml.py*.

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

    # Costanti

    # Rimuovi il commento dalle righe seguenti per usare un'istanza CPU per l'addestramento
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Rimuovi il commento dalle righe seguenti per usare un'istanza GPU per l'addestramento
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Sostituisci con la posizione del tuo cluster di calcolo
    FINETUNING_DIR = "./finetuning_dir" # Percorso allo script di fine-tuning
    TRAINING_ENV_NAME = "phi-3-training-environment" # Nome dell'ambiente di addestramento
    MODEL_OUTPUT_DIR = "./model_output" # Percorso della directory di output del modello in Azure ML

    # Configurazione del logging per tracciare il processo
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
            image=DOCKER_IMAGE_NAME,  # Immagine Docker per l'ambiente
            conda_file=CONDA_FILE,  # File dell'ambiente Conda
            name=TRAINING_ENV_NAME,  # Nome dell'ambiente
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
                tier="Dedicated",  # Tier del cluster di calcolo
                min_instances=0,  # Numero minimo di istanze
                max_instances=1  # Numero massimo di istanze
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Attendere la creazione del cluster
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Percorso a fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Ambiente di addestramento
            compute=compute_name,  # Cluster di calcolo da utilizzare
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Percorso del file dei dati di addestramento
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Percorso del file dei dati di valutazione
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Inizializza ML Client
        ml_client = get_ml_client()

        # Crea ambiente
        env = create_or_get_environment(ml_client)
        
        # Crea o ottieni un cluster di calcolo esistente
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Crea e invia il job di fine-tuning
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Invia il job
        ml_client.jobs.stream(returned_job.name)  # Mostra in streaming i log del job
        
        # Cattura il nome del job
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. Sostituisci `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `LOCATION` con i dettagli specifici.

    ```python
   # Rimuovi il commento dalle righe seguenti per usare un'istanza GPU per l'addestramento
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Sostituisci con la posizione del tuo cluster di calcolo
    ```

> [!TIP]
>
> **Indicazioni per la messa a punto con un dataset minimo usando una CPU**
>
> Se vuoi usare una CPU per la messa a punto, questo approccio è ideale per chi ha sottoscrizioni con vantaggi (come Visual Studio Enterprise Subscription) o per testare rapidamente il processo di messa a punto e distribuzione.
>
> 1. Apri il file *setup_ml*.
> 1. Sostituisci `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, e `DOCKER_IMAGE_NAME` con i valori seguenti. Se non hai accesso a *Standard_E16s_v3*, puoi usare un'istanza CPU equivalente o richiedere una nuova quota.
> 1. Sostituisci `LOCATION` con i tuoi dettagli specifici.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Digita il comando seguente per eseguire lo script *setup_ml.py* e avviare il processo di messa a punto in Azure Machine Learning.

    ```python
    python setup_ml.py
    ```

1. In questo esercizio, hai messo a punto con successo il modello Phi-3 usando Azure Machine Learning. Eseguendo lo script *setup_ml.py*, hai configurato l'ambiente Azure Machine Learning e avviato il processo di messa a punto definito nel file *fine_tune.py*. Tieni presente che il processo di messa a punto può richiedere un tempo considerevole. Dopo aver eseguito il comando `python setup_ml.py`, devi attendere il completamento del processo. Puoi monitorare lo stato del job di messa a punto seguendo il link fornito nel terminale verso il portale Azure Machine Learning.

    ![Visualizza il job di fine-tuning.](../../../../../../translated_images/02-02-see-finetuning-job.59393bc3b143871e.it.png)

### Distribuire il modello messo a punto

Per integrare il modello Phi-3 messo a punto con Prompt Flow, devi distribuire il modello per renderlo accessibile per inferenze in tempo reale. Questo processo comporta la registrazione del modello, la creazione di un endpoint online e la distribuzione del modello.

#### Imposta il nome del modello, il nome dell'endpoint e il nome della distribuzione per il deployment

1. Apri il file *config.py*.

1. Sostituisci `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` con il nome desiderato per il tuo modello.

1. Sostituisci `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` con il nome desiderato per il tuo endpoint.

1. Sostituisci `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` con il nome desiderato per la tua distribuzione.

#### Aggiungi codice al file *deploy_model.py*

L'esecuzione del file *deploy_model.py* automatizza l'intero processo di distribuzione. Registra il modello, crea un endpoint e esegue la distribuzione in base alle impostazioni specificate nel file config.py, che include il nome del modello, il nome dell'endpoint e il nome della distribuzione.

1. Apri il file *deploy_model.py* in Visual Studio Code.

1. Aggiungi il codice seguente in *deploy_model.py*.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Importazioni di configurazione
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

    # Costanti
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Configurazione del logging
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
            # Recupera i dettagli dell'endpoint corrente
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Registra l'allocazione del traffico corrente per il debug
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Imposta l'allocazione del traffico per la distribuzione
            endpoint.traffic = {deployment_name: 100}
            
            # Aggiorna l'endpoint con la nuova allocazione del traffico
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Registra l'allocazione del traffico aggiornata per il debug
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Registra eventuali errori che si verificano durante il processo
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
    - Seleziona **Studio web URL** per aprire lo spazio di lavoro di Azure Machine Learning.
    - Seleziona **Jobs** dalla scheda a sinistra.
    - Seleziona l'esperimento per la messa a punto. Ad esempio, *finetunephi*.
    - Seleziona il job che hai creato.
    - Copia e incolla il nome del tuo job in `JOB_NAME = "your-job-name"` nel file *deploy_model.py*.

1. Sostituisci `COMPUTE_INSTANCE_TYPE` con i tuoi dettagli specifici.

1. Digita il comando seguente per eseguire lo script *deploy_model.py* e avviare il processo di deployment in Azure Machine Learning.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> Per evitare addebiti aggiuntivi sul tuo account, assicurati di eliminare l'endpoint creato nell'area di lavoro di Azure Machine Learning.
>

#### Verifica lo stato del deployment nell'area di lavoro di Azure Machine Learning

1. Visita [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Naviga all'area di lavoro di Azure Machine Learning che hai creato.

1. Seleziona **Studio web URL** per aprire l'area di lavoro di Azure Machine Learning.

1. Seleziona **Endpoints** dalla scheda sul lato sinistro.

    ![Seleziona gli endpoint.](../../../../../../translated_images/02-03-select-endpoints.c3136326510baff1.it.png)

2. Seleziona l'endpoint che hai creato.

    ![Seleziona l'endpoint che hai creato.](../../../../../../translated_images/02-04-select-endpoint-created.0363e7dca51dabb4.it.png)

3. In questa pagina, puoi gestire gli endpoint creati durante il processo di deployment.

## Scenario 3: Integra con Prompt flow e chatta con il tuo modello personalizzato

### Integra il modello personalizzato Phi-3 con Prompt flow

Dopo aver distribuito con successo il tuo modello messo a punto, puoi ora integrarlo con Prompt flow per utilizzare il tuo modello in applicazioni in tempo reale, consentendo una varietà di attività interattive con il tuo modello Phi-3 personalizzato.

#### Imposta la chiave API e l'URI dell'endpoint del modello Phi-3 messo a punto

1. Vai all'area di lavoro di Azure Machine Learning che hai creato.
1. Seleziona **Endpoints** dalla scheda sul lato sinistro.
1. Seleziona l'endpoint che hai creato.
1. Seleziona **Consume** dal menu di navigazione.
1. Copia e incolla il tuo **REST endpoint** nel file *config.py*, sostituendo `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` con il tuo **REST endpoint**.
1. Copia e incolla la tua **Primary key** nel file *config.py*, sostituendo `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` con la tua **Primary key**.

    ![Copia la chiave API e l'URI dell'endpoint.](../../../../../../translated_images/02-05-copy-apikey-endpoint.88b5a92e6462c53b.it.png)

#### Aggiungi codice al file *flow.dag.yml*

1. Apri il file *flow.dag.yml* in Visual Studio Code.

1. Aggiungi il codice seguente in *flow.dag.yml*.

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

1. Aggiungi il codice seguente in *integrate_with_promptflow.py*.

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

    # Configurazione del logging
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

1. Digita il comando seguente per eseguire lo script *deploy_model.py* e avviare il processo di deployment in Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Ecco un esempio dei risultati: ora puoi chattare con il tuo modello personalizzato Phi-3. Si consiglia di porre domande basate sui dati utilizzati per la messa a punto.

    ![Esempio di Prompt flow.](../../../../../../translated_images/02-06-promptflow-example.89384abaf3ad71f6.it.png)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Dichiarazione di non responsabilità**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci a garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua madre deve essere considerato la fonte autorevole. Per informazioni critiche è consigliata una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->