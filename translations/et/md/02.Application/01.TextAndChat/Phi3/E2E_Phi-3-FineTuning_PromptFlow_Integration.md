<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-10-11T12:04:07+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "et"
}
-->
# Kohanda ja integreeri kohandatud Phi-3 mudelid Prompt flow'ga

See algusest lõpuni (E2E) näidis põhineb juhendil "[Kohanda ja integreeri kohandatud Phi-3 mudelid Prompt flow'ga: samm-sammuline juhend](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" Microsoft Tech Community lehelt. Juhend tutvustab kohandatud Phi-3 mudelite häälestamise, juurutamise ja integreerimise protsesse Prompt flow'ga.

## Ülevaade

Selles E2E näidises õpid, kuidas häälestada Phi-3 mudelit ja integreerida seda Prompt flow'ga. Kasutades Azure Machine Learningut ja Prompt flow'd, luuakse töövoog kohandatud AI mudelite juurutamiseks ja kasutamiseks. Näidis jaguneb kolme stsenaariumi:

**Stsenaarium 1: Azure'i ressursside seadistamine ja häälestamiseks ettevalmistamine**

**Stsenaarium 2: Phi-3 mudeli häälestamine ja juurutamine Azure Machine Learning Studios**

**Stsenaarium 3: Integreerimine Prompt flow'ga ja vestlemine kohandatud mudeliga**

Siin on selle E2E näidise ülevaade.

![Phi-3-FineTuning_PromptFlow_Integration Ülevaade](../../../../../../imgs/02/FineTuning-PromptFlow/00-01-architecture.png)

### Sisukord

1. **[Stsenaarium 1: Azure'i ressursside seadistamine ja häälestamiseks ettevalmistamine](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning Workspace'i loomine](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [GPU kvootide taotlemine Azure'i tellimuses](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Rolli määramine](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Projekti seadistamine](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Andmestiku ettevalmistamine häälestamiseks](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Stsenaarium 2: Phi-3 mudeli häälestamine ja juurutamine Azure Machine Learning Studios](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure CLI seadistamine](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 mudeli häälestamine](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Häälestatud mudeli juurutamine](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Stsenaarium 3: Integreerimine Prompt flow'ga ja vestlemine kohandatud mudeliga](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Kohandatud Phi-3 mudeli integreerimine Prompt flow'ga](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Vestlemine kohandatud mudeliga](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Stsenaarium 1: Azure'i ressursside seadistamine ja häälestamiseks ettevalmistamine

### Azure Machine Learning Workspace'i loomine

1. Sisesta **azure machine learning** portaali lehe ülaosas asuvasse **otsinguribasse** ja vali kuvatavatest valikutest **Azure Machine Learning**.

    ![Sisesta azure machine learning](../../../../../../imgs/02/FineTuning-PromptFlow/01-01-type-azml.png)

1. Vali navigeerimismenüüst **+ Create**.

1. Vali navigeerimismenüüst **New workspace**.

    ![Vali uus tööruum](../../../../../../imgs/02/FineTuning-PromptFlow/01-02-select-new-workspace.png)

1. Tee järgmised toimingud:

    - Vali oma Azure'i **Subscription**.
    - Vali kasutatav **Resource group** (loo uus, kui vaja).
    - Sisesta **Workspace Name**. See peab olema unikaalne väärtus.
    - Vali kasutatav **Region**.
    - Vali kasutatav **Storage account** (loo uus, kui vaja).
    - Vali kasutatav **Key vault** (loo uus, kui vaja).
    - Vali kasutatav **Application insights** (loo uus, kui vaja).
    - Vali kasutatav **Container registry** (loo uus, kui vaja).

    ![Täida AZML.](../../../../../../imgs/02/FineTuning-PromptFlow/01-03-fill-AZML.png)

1. Vali **Review + Create**.

1. Vali **Create**.

### GPU kvootide taotlemine Azure'i tellimuses

Selles E2E näidises kasutatakse häälestamiseks *Standard_NC24ads_A100_v4 GPU*-d, mis nõuab kvoodi taotlemist, ja juurutamiseks *Standard_E4s_v3* CPU-d, mis ei nõua kvoodi taotlemist.

> [!NOTE]
>
> Ainult Pay-As-You-Go tellimused (standardne tellimustüüp) on GPU eraldamiseks sobilikud; soodustellimused ei ole praegu toetatud.
>
> Kasutajatele, kellel on soodustellimused (nt Visual Studio Enterprise Subscription) või kes soovivad kiiresti testida häälestamise ja juurutamise protsessi, pakub see juhend ka juhiseid minimaalse andmestikuga CPU kasutamiseks. Siiski tuleb märkida, et häälestamise tulemused on oluliselt paremad, kui kasutada GPU-d suuremate andmestikega.

1. Külasta [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Tee järgmised toimingud, et taotleda *Standard NCADSA100v4 Family* kvooti:

    - Vali vasakpoolsest menüüst **Quota**.
    - Vali kasutatav **Virtual machine family**. Näiteks vali **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, mis sisaldab *Standard_NC24ads_A100_v4* GPU-d.
    - Vali navigeerimismenüüst **Request quota**.

        ![Taotle kvooti.](../../../../../../imgs/02/FineTuning-PromptFlow/01-04-request-quota.png)

    - Sisesta **Request quota** lehel soovitud **New cores limit**. Näiteks 24.
    - Vali **Submit**, et taotleda GPU kvooti.

> [!NOTE]
> Sobiva GPU või CPU valimiseks oma vajaduste järgi vaata [Virtuaalmasinate suurused Azure'is](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) dokumenti.

### Rolli määramine

Mudelite häälestamiseks ja juurutamiseks tuleb esmalt luua kasutaja määratud hallatav identiteet (UAI) ja määrata sellele sobivad õigused. Seda UAI-d kasutatakse autentimiseks juurutamise ajal.

#### Kasutaja määratud hallatava identiteedi (UAI) loomine

1. Sisesta **managed identities** portaali lehe ülaosas asuvasse **otsinguribasse** ja vali kuvatavatest valikutest **Managed Identities**.

    ![Sisesta managed identities.](../../../../../../imgs/02/FineTuning-PromptFlow/01-05-type-managed-identities.png)

1. Vali **+ Create**.

    ![Vali create.](../../../../../../imgs/02/FineTuning-PromptFlow/01-06-select-create.png)

1. Tee järgmised toimingud:

    - Vali oma Azure'i **Subscription**.
    - Vali kasutatav **Resource group** (loo uus, kui vaja).
    - Vali kasutatav **Region**.
    - Sisesta **Name**. See peab olema unikaalne väärtus.

1. Vali **Review + create**.

1. Vali **+ Create**.

#### Lisa hallatavale identiteedile Contributor rolli määramine

1. Navigeeri loodud hallatava identiteedi ressursile.

1. Vali vasakpoolsest menüüst **Azure role assignments**.

1. Vali navigeerimismenüüst **+Add role assignment**.

1. Lisa rolli määramise lehel järgmised toimingud:
    - Vali **Scope** väärtuseks **Resource group**.
    - Vali oma Azure'i **Subscription**.
    - Vali kasutatav **Resource group**.
    - Vali **Role** väärtuseks **Contributor**.

    ![Täida Contributor roll.](../../../../../../imgs/02/FineTuning-PromptFlow/01-07-fill-contributor-role.png)

1. Vali **Save**.

#### Lisa hallatavale identiteedile Storage Blob Data Reader rolli määramine

1. Sisesta **storage accounts** portaali lehe ülaosas asuvasse **otsinguribasse** ja vali kuvatavatest valikutest **Storage accounts**.

    ![Sisesta storage accounts.](../../../../../../imgs/02/FineTuning-PromptFlow/01-08-type-storage-accounts.png)

1. Vali Azure Machine Learning tööruumiga seotud salvestuskonto. Näiteks *finetunephistorage*.

1. Tee järgmised toimingud, et navigeerida rolli määramise lehele:

    - Navigeeri loodud Azure'i salvestuskontole.
    - Vali vasakpoolsest menüüst **Access Control (IAM)**.
    - Vali navigeerimismenüüst **+ Add**.
    - Vali navigeerimismenüüst **Add role assignment**.

    ![Lisa roll.](../../../../../../imgs/02/FineTuning-PromptFlow/01-09-add-role.png)

1. Lisa rolli määramise lehel järgmised toimingud:

    - Rolli lehel sisesta **Storage Blob Data Reader** otsinguribasse ja vali kuvatavatest valikutest **Storage Blob Data Reader**.
    - Rolli lehel vali **Next**.
    - Liikmete lehel vali **Assign access to** väärtuseks **Managed identity**.
    - Liikmete lehel vali **+ Select members**.
    - Hallatavate identiteetide valimise lehel vali oma Azure'i **Subscription**.
    - Hallatavate identiteetide valimise lehel vali **Managed identity** väärtuseks **Manage Identity**.
    - Hallatavate identiteetide valimise lehel vali loodud hallatav identiteet. Näiteks *finetunephi-managedidentity*.
    - Hallatavate identiteetide valimise lehel vali **Select**.

    ![Vali hallatav identiteet.](../../../../../../imgs/02/FineTuning-PromptFlow/01-10-select-managed-identity.png)

1. Vali **Review + assign**.

#### Lisa hallatavale identiteedile AcrPull rolli määramine

1. Sisesta **container registries** portaali lehe ülaosas asuvasse **otsinguribasse** ja vali kuvatavatest valikutest **Container registries**.

    ![Sisesta container registries.](../../../../../../imgs/02/FineTuning-PromptFlow/01-11-type-container-registries.png)

1. Vali Azure Machine Learning tööruumiga seotud konteineriregister. Näiteks *finetunephicontainerregistries*.

1. Tee järgmised toimingud, et navigeerida rolli määramise lehele:

    - Vali vasakpoolsest menüüst **Access Control (IAM)**.
    - Vali navigeerimismenüüst **+ Add**.
    - Vali navigeerimismenüüst **Add role assignment**.

1. Lisa rolli määramise lehel järgmised toimingud:

    - Rolli lehel sisesta **AcrPull** otsinguribasse ja vali kuvatavatest valikutest **AcrPull**.
    - Rolli lehel vali **Next**.
    - Liikmete lehel vali **Assign access to** väärtuseks **Managed identity**.
    - Liikmete lehel vali **+ Select members**.
    - Hallatavate identiteetide valimise lehel vali oma Azure'i **Subscription**.
    - Hallatavate identiteetide valimise lehel vali **Managed identity** väärtuseks **Manage Identity**.
    - Hallatavate identiteetide valimise lehel vali loodud hallatav identiteet. Näiteks *finetunephi-managedidentity*.
    - Hallatavate identiteetide valimise lehel vali **Select**.
    - Vali **Review + assign**.

### Projekti seadistamine

Nüüd lood kausta, kus töötada, ja seadistad virtuaalse keskkonna, et arendada programmi, mis suhtleb kasutajatega ja kasutab Azure Cosmos DB-s salvestatud vestlusajalugu vastuste koostamiseks.

#### Loo kaust, kus töötada

1. Ava terminaliaken ja sisesta järgmine käsk, et luua kaust nimega *finetune-phi* vaikimisi asukohta.

    ```console
    mkdir finetune-phi
    ```

1. Sisesta terminalis järgmine käsk, et liikuda loodud *finetune-phi* kausta.

    ```console
    cd finetune-phi
    ```

#### Loo virtuaalne keskkond

1. Sisesta terminalis järgmine käsk, et luua virtuaalne keskkond nimega *.venv*.

    ```console
    python -m venv .venv
    ```

1. Sisesta terminalis järgmine käsk, et aktiveerida virtuaalne keskkond.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> Kui see õnnestus, peaksid nägema *(.venv)* käsurea ees.

#### Paigalda vajalikud paketid

1. Sisesta terminalis järgmised käsud, et paigaldada vajalikud paketid.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Loo projekti failid
Selles harjutuses loote meie projekti jaoks vajalikud failid. Need failid hõlmavad skripte andmestiku allalaadimiseks, Azure Machine Learning keskkonna seadistamiseks, Phi-3 mudeli peenhäälestamiseks ja peenhäälestatud mudeli juurutamiseks. Samuti loote *conda.yml* faili peenhäälestamise keskkonna seadistamiseks.

Selles harjutuses teete järgmist:

- Looge *download_dataset.py* fail andmestiku allalaadimiseks.
- Looge *setup_ml.py* fail Azure Machine Learning keskkonna seadistamiseks.
- Looge *fine_tune.py* fail *finetuning_dir* kausta, et peenhäälestada Phi-3 mudelit andmestiku abil.
- Looge *conda.yml* fail peenhäälestamise keskkonna seadistamiseks.
- Looge *deploy_model.py* fail peenhäälestatud mudeli juurutamiseks.
- Looge *integrate_with_promptflow.py* fail, et integreerida peenhäälestatud mudel ja käivitada mudel Prompt Flow abil.
- Looge *flow.dag.yml* fail, et seadistada Prompt Flow töövoo struktuur.
- Looge *config.py* fail Azure'i teabe sisestamiseks.

> [!NOTE]
>
> Kogu kaustastruktuur:
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

1. Avage **Visual Studio Code**.

1. Valige menüüribalt **File**.

1. Valige **Open Folder**.

1. Valige *finetune-phi* kaust, mille loote, ja mis asub aadressil *C:\Users\yourUserName\finetune-phi*.

    ![Avage projekti kaust.](../../../../../../imgs/02/FineTuning-PromptFlow/01-12-open-project-folder.png)

1. Visual Studio Code'i vasakpaanil paremklõpsake ja valige **New File**, et luua uus fail nimega *download_dataset.py*.

1. Visual Studio Code'i vasakpaanil paremklõpsake ja valige **New File**, et luua uus fail nimega *setup_ml.py*.

1. Visual Studio Code'i vasakpaanil paremklõpsake ja valige **New File**, et luua uus fail nimega *deploy_model.py*.

    ![Looge uus fail.](../../../../../../imgs/02/FineTuning-PromptFlow/01-13-create-new-file.png)

1. Visual Studio Code'i vasakpaanil paremklõpsake ja valige **New Folder**, et luua uus kaust nimega *finetuning_dir*.

1. Looge *finetuning_dir* kaustas uus fail nimega *fine_tune.py*.

#### Looge ja seadistage *conda.yml* fail

1. Visual Studio Code'i vasakpaanil paremklõpsake ja valige **New File**, et luua uus fail nimega *conda.yml*.

1. Lisage *conda.yml* faili järgmine kood, et seadistada Phi-3 mudeli peenhäälestamise keskkond.

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

#### Looge ja seadistage *config.py* fail

1. Visual Studio Code'i vasakpaanil paremklõpsake ja valige **New File**, et luua uus fail nimega *config.py*.

1. Lisage *config.py* faili järgmine kood, et sisestada oma Azure'i teave.

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

#### Lisage Azure'i keskkonnamuutujad

1. Tehke järgmised toimingud, et lisada Azure'i tellimuse ID:

    - Sisestage **subscriptions** portaali lehe ülaosas asuvasse otsinguribasse ja valige kuvatavatest valikutest **Subscriptions**.
    - Valige Azure'i tellimus, mida praegu kasutate.
    - Kopeerige ja kleepige oma tellimuse ID *config.py* faili.

    ![Leidke tellimuse ID.](../../../../../../imgs/02/FineTuning-PromptFlow/01-14-find-subscriptionid.png)

1. Tehke järgmised toimingud, et lisada Azure'i tööruumi nimi:

    - Navigeerige loodud Azure Machine Learning ressursile.
    - Kopeerige ja kleepige oma konto nimi *config.py* faili.

    ![Leidke Azure Machine Learning nimi.](../../../../../../imgs/02/FineTuning-PromptFlow/01-15-find-AZML-name.png)

1. Tehke järgmised toimingud, et lisada Azure'i ressursigrupi nimi:

    - Navigeerige loodud Azure Machine Learning ressursile.
    - Kopeerige ja kleepige oma Azure'i ressursigrupi nimi *config.py* faili.

    ![Leidke ressursigrupi nimi.](../../../../../../imgs/02/FineTuning-PromptFlow/01-16-find-AZML-resourcegroup.png)

2. Tehke järgmised toimingud, et lisada Azure'i hallatud identiteedi nimi:

    - Navigeerige loodud hallatud identiteedi ressursile.
    - Kopeerige ja kleepige oma Azure'i hallatud identiteedi nimi *config.py* faili.

    ![Leidke UAI.](../../../../../../imgs/02/FineTuning-PromptFlow/01-17-find-uai.png)

### Valmistage andmestik peenhäälestamiseks

Selles harjutuses käivitate *download_dataset.py* faili, et laadida *ULTRACHAT_200k* andmestikud oma kohalikku keskkonda. Seejärel kasutate neid andmestikke Phi-3 mudeli peenhäälestamiseks Azure Machine Learning keskkonnas.

#### Laadige andmestik alla *download_dataset.py* abil

1. Avage *download_dataset.py* fail Visual Studio Code'is.

1. Lisage *download_dataset.py* faili järgmine kood.

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
> **Juhised peenhäälestamiseks minimaalse andmestikuga, kasutades CPU-d**
>
> Kui soovite kasutada CPU-d peenhäälestamiseks, sobib see lähenemine ideaalselt neile, kellel on soodustellimused (näiteks Visual Studio Enterprise Subscription) või kes soovivad kiiresti testida peenhäälestamise ja juurutamise protsessi.
>
> Asendage `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` väärtusega `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Sisestage oma terminali järgmine käsk, et käivitada skript ja laadida andmestik oma kohalikku keskkonda.

    ```console
    python download_data.py
    ```

1. Kontrollige, kas andmestikud salvestati edukalt teie kohalikku *finetune-phi/data* kataloogi.

> [!NOTE]
>
> **Andmestiku suurus ja peenhäälestamise aeg**
>
> Selles E2E näites kasutate ainult 1% andmestikust (`train_sft[:1%]`). See vähendab oluliselt andmete mahtu, kiirendades nii üleslaadimise kui ka peenhäälestamise protsessi. Protsessi ja mudeli jõudluse tasakaalu leidmiseks saate protsenti kohandada. Väiksema andmestiku alamhulga kasutamine vähendab peenhäälestamiseks vajalikku aega, muutes protsessi hallatavaks E2E näite jaoks.

## Stsenaarium 2: Peenhäälestage Phi-3 mudel ja juurutage see Azure Machine Learning Studios

### Seadistage Azure CLI

Peate seadistama Azure CLI, et autentida oma keskkonda. Azure CLI võimaldab teil hallata Azure'i ressursse otse käsurealt ja pakub vajalikke mandaate, et Azure Machine Learning saaks neile ressurssidele juurde pääseda. Alustamiseks installige [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli).

1. Avage terminaliaken ja sisestage järgmine käsk, et logida sisse oma Azure'i kontole.

    ```console
    az login
    ```

1. Valige Azure'i konto, mida kasutada.

1. Valige Azure'i tellimus, mida kasutada.

    ![Leidke ressursigrupi nimi.](../../../../../../imgs/02/FineTuning-PromptFlow/02-01-login-using-azure-cli.png)

> [!TIP]
>
> Kui teil on probleeme Azure'i sisselogimisega, proovige kasutada seadme koodi. Avage terminaliaken ja sisestage järgmine käsk, et logida sisse oma Azure'i kontole:
>
> ```console
> az login --use-device-code
> ```
>

### Peenhäälestage Phi-3 mudel

Selles harjutuses peenhäälestate Phi-3 mudelit antud andmestiku abil. Kõigepealt määratlete peenhäälestamise protsessi *fine_tune.py* failis. Seejärel konfigureerite Azure Machine Learning keskkonna ja alustate peenhäälestamise protsessi, käivitades *setup_ml.py* faili. See skript tagab, et peenhäälestamine toimub Azure Machine Learning keskkonnas.

Käivitades *setup_ml.py*, käivitate peenhäälestamise protsessi Azure Machine Learning keskkonnas.

#### Lisage kood *fine_tune.py* faili

1. Navigeerige *finetuning_dir* kausta ja avage *fine_tune.py* fail Visual Studio Code'is.

1. Lisage *fine_tune.py* faili järgmine kood.

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

1. Salvestage ja sulgege *fine_tune.py* fail.

> [!TIP]
> **Võite peenhäälestada Phi-3.5 mudelit**
>
> *fine_tune.py* failis saate muuta `pretrained_model_name` väärtust `"microsoft/Phi-3-mini-4k-instruct"` mis tahes mudeliks, mida soovite peenhäälestada. Näiteks, kui muudate selle väärtuseks `"microsoft/Phi-3.5-mini-instruct"`, kasutate Phi-3.5-mini-instruct mudelit peenhäälestamiseks. Mudeli nime leidmiseks ja kasutamiseks külastage [Hugging Face](https://huggingface.co/), otsige mudelit, mis teid huvitab, ja kopeerige ning kleepige selle nimi `pretrained_model_name` väljale oma skriptis.
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Peenhäälestage Phi-3.5.":::
>

#### Lisage kood *setup_ml.py* faili

1. Avage *setup_ml.py* fail Visual Studio Code'is.

1. Lisage *setup_ml.py* faili järgmine kood.

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

1. Asendage `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` ja `LOCATION` oma konkreetsete andmetega.

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **Juhised peenhäälestamiseks minimaalse andmestikuga, kasutades CPU-d**
>
> Kui soovite kasutada CPU-d peenhäälestamiseks, sobib see lähenemine ideaalselt neile, kellel on soodustellimused (näiteks Visual Studio Enterprise Subscription) või kes soovivad kiiresti testida peenhäälestamise ja juurutamise protsessi.
>
> 1. Avage *setup_ml* fail.
> 1. Asendage `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` ja `DOCKER_IMAGE_NAME` järgmisega. Kui teil pole juurdepääsu *Standard_E16s_v3*-le, võite kasutada samaväärset CPU eksemplari või taotleda uut kvooti.
> 1. Asendage `LOCATION` oma konkreetsete andmetega.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Sisestage järgmine käsk, et käivitada *setup_ml.py* skript ja alustada peenhäälestamise protsessi Azure Machine Learning keskkonnas.

    ```python
    python setup_ml.py
    ```

1. Selles harjutuses peenhäälestasite edukalt Phi-3 mudelit Azure Machine Learning abil. Käivitades *setup_ml.py* skripti, seadistasite Azure Machine Learning keskkonna ja alustasite peenhäälestamise protsessi, mis on määratletud *fine_tune.py* failis. Pange tähele, et peenhäälestamise protsess võib võtta märkimisväärselt aega. Pärast `python setup_ml.py` käsu käivitamist peate ootama, kuni protsess lõpeb. Peenhäälestamise töö olekut saate jälgida, järgides terminalis kuvatud linki Azure Machine Learning portaalile.

    ![Vaadake peenhäälestamise tööd.](../../../../../../imgs/02/FineTuning-PromptFlow/02-02-see-finetuning-job.png)

### Juurutage peenhäälestatud mudel

Peenhäälestatud Phi-3 mudeli integreerimiseks Prompt Flow'ga peate mudeli juurutama, et see oleks reaalajas järelduste jaoks kättesaadav. See protsess hõlmab mudeli registreerimist, veebipõhise lõpp-punkti loomist ja mudeli juurutamist.

#### Määrake mudeli nimi, lõpp-punkti nimi ja juurutamise nimi

1. Avage *config.py* fail.

1. Asendage `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` soovitud mudeli nimega.

1. Asendage `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` soovitud lõpp-punkti nimega.

1. Asendage `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` soovitud juurutamise nimega.

#### Lisage kood *deploy_model.py* faili

Käivitades *deploy_model.py* faili, automatiseeritakse kogu juurutamise protsess. See registreerib mudeli, loob lõpp-punkti ja teostab juurutamise vastavalt *config.py* failis määratud seadetele, mis hõlmavad mudeli nime, lõpp-punkti nime ja juurutamise nime.

1. Avage *deploy_model.py* fail Visual Studio Code'is.

1. Lisage *deploy_model.py* faili järgmine kood.

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

1. Tehke järgmised toimingud, et saada `JOB_NAME`:

    - Navigeerige loodud Azure Machine Learning ressursile.
    - Valige **Studio web URL**, et avada Azure Machine Learning tööruum.
    - Valige vasakpoolsest vahekaardist **Jobs**.
    - Valige peenhäälestamise eksperiment. Näiteks *finetunephi*.
    - Valige loodud töö.
- Kopeeri ja kleebi oma töö nimi `JOB_NAME = "your-job-name"` *deploy_model.py* faili.

1. Asenda `COMPUTE_INSTANCE_TYPE` oma konkreetsete andmetega.

1. Sisesta järgmine käsk, et käivitada *deploy_model.py* skript ja alustada juurutusprotsessi Azure Machine Learning keskkonnas.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> Et vältida täiendavaid kulusid oma kontole, veendu, et kustutad loodud lõpp-punkti Azure Machine Learning tööruumis.
>

#### Kontrolli juurutuse staatust Azure Machine Learning tööruumis

1. Külasta [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Liigu loodud Azure Machine Learning tööruumi.

1. Vali **Studio web URL**, et avada Azure Machine Learning tööruum.

1. Vali vasakult menüüst **Endpoints**.

    ![Vali lõpp-punktid.](../../../../../../imgs/02/FineTuning-PromptFlow/02-03-select-endpoints.png)

2. Vali loodud lõpp-punkt.

    ![Vali loodud lõpp-punktid.](../../../../../../imgs/02/FineTuning-PromptFlow/02-04-select-endpoint-created.png)

3. Sellel lehel saad hallata juurutusprotsessi käigus loodud lõpp-punkte.

## Stsenaarium 3: Integreeri Prompt flow'ga ja vestle oma kohandatud mudeliga

### Kohandatud Phi-3 mudeli integreerimine Prompt flow'ga

Pärast oma peenhäälestatud mudeli edukat juurutamist saad selle nüüd integreerida Prompt flow'ga, et kasutada mudelit reaalajas rakendustes, võimaldades mitmesuguseid interaktiivseid ülesandeid oma kohandatud Phi-3 mudeliga.

#### Määra peenhäälestatud Phi-3 mudeli API võti ja lõpp-punkti URI

1. Liigu loodud Azure Machine Learning tööruumi.
1. Vali vasakult menüüst **Endpoints**.
1. Vali loodud lõpp-punkt.
1. Vali navigeerimismenüüst **Consume**.
1. Kopeeri ja kleebi oma **REST endpoint** *config.py* faili, asendades `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` oma **REST endpoint** väärtusega.
1. Kopeeri ja kleebi oma **Primary key** *config.py* faili, asendades `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` oma **Primary key** väärtusega.

    ![Kopeeri API võti ja lõpp-punkti URI.](../../../../../../imgs/02/FineTuning-PromptFlow/02-05-copy-apikey-endpoint.png)

#### Lisa kood *flow.dag.yml* faili

1. Ava *flow.dag.yml* fail Visual Studio Code'is.

1. Lisa järgmine kood *flow.dag.yml* faili.

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

#### Lisa kood *integrate_with_promptflow.py* faili

1. Ava *integrate_with_promptflow.py* fail Visual Studio Code'is.

1. Lisa järgmine kood *integrate_with_promptflow.py* faili.

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

### Vestle oma kohandatud mudeliga

1. Sisesta järgmine käsk, et käivitada *deploy_model.py* skript ja alustada juurutusprotsessi Azure Machine Learning keskkonnas.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Näide tulemustest: Nüüd saad vestelda oma kohandatud Phi-3 mudeliga. Soovitatav on esitada küsimusi, mis põhinevad peenhäälestamiseks kasutatud andmetel.

    ![Prompt flow näide.](../../../../../../imgs/02/FineTuning-PromptFlow/02-06-promptflow-example.png)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.