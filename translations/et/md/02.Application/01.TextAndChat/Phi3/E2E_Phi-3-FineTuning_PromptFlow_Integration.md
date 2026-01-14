<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7ca2c30fdb802664070e9cfbf92e24fe",
  "translation_date": "2026-01-05T14:45:10+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "et"
}
-->
# Täpsusta ja integreeri kohandatud Phi-3 mudeleid Prompt flow’ga

See lõpp-lõpuni (E2E) näidis põhineb juhendil "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" Microsofti Tech Community'st. Selles tutvustatakse kohandatud Phi-3 mudelite täpsustamise, juurutamise ja integreerimise protsesse Prompt flow’ga.

## Ülevaade

Selles E2E näidises õpid, kuidas Phi-3 mudelit täpsustada ja integreerida see Prompt flow’ga. Kasutades Azure Machine Learningut ja Prompt flow’d, seadistad töövoo kohandatud tehisintellektimudelite juurutamiseks ja kasutamiseks. See E2E näidis on jagatud kolmeks stsenaariumiks:

**Stsenaarium 1: Azure’i ressursside seadistamine ja täpsustamiseks ettevalmistamine**

**Stsenaarium 2: Phi-3 mudeli täpsustamine ja juurutamine Azure Machine Learning Studios**

**Stsenaarium 3: Integreerimine Prompt flow’ga ja suhtlus kohandatud mudeliga**

Siin on selle E2E näidise ülevaade.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/et/00-01-architecture.02fc569e266d468c.png)

### Sisukord

1. **[Stsenaarium 1: Azure’i ressursside seadistamine ja täpsustamiseks ettevalmistamine](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning tööruumi loomine](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [GPU kvantide taotlemine Azure’i tellimuses](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Rolli määramise lisamine](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Projekti seadistamine](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Andmekogumi ettevalmistamine täpsustamiseks](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Stsenaarium 2: Phi-3 mudeli täpsustamine ja juurutamine Azure Machine Learning Studios](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure CLI seadistamine](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3 mudeli täpsustamine](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Täpsustatud mudeli juurutamine](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Stsenaarium 3: Integreerimine Prompt flow’ga ja suhtlus kohandatud mudeliga](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Kohandatud Phi-3 mudeli integreerimine Prompt flow’ga](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Suhtlus kohandatud mudeliga](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Stsenaarium 1: Azure’i ressursside seadistamine ja täpsustamiseks ettevalmistamine

### Azure Machine Learning tööruumi loomine

1. Tippige portaalilehe ülaosas otsiribale *azure machine learning* ja valige kuvatud valikute hulgast **Azure Machine Learning**.

    ![Type azure machine learning](../../../../../../translated_images/et/01-01-type-azml.a5116f8454d98c60.png)

1. Valige navigeerimismenüüst **+ Create**.

1. Valige navigeerimismenüüst **New workspace**.

    ![Select new workspace](../../../../../../translated_images/et/01-02-select-new-workspace.83e17436f8898dc4.png)

1. Täitke järgmised ülesanded:

    - Valige oma Azure **Subscription**.
    - Valige kasutatav **Resource group** (looge vajadusel uus).
    - Sisestage **Workspace Name**. See peab olema ainulaadne väärtus.
    - Valige soovitud **Region**.
    - Valige kasutatav **Storage account** (looge vajadusel uus).
    - Valige kasutatav **Key vault** (looge vajadusel uus).
    - Valige kasutatav **Application insights** (looge vajadusel uus).
    - Valige kasutatav **Container registry** (looge vajadusel uus).

    ![Fill AZML.](../../../../../../translated_images/et/01-03-fill-AZML.730a5177757bbebb.png)

1. Valige **Review + Create**.

1. Valige **Create**.

### GPU kvantide taotlemine Azure’i tellimuses

Selles E2E näidises kasutate täpsustamiseks *Standard_NC24ads_A100_v4 GPU*-d, mis nõuab kvandi taotlust, ning juurutamiseks *Standard_E4s_v3* CPU-d, mis kvandi taotlust ei vaja.

> [!NOTE]
>
> Ainult Pay-As-You-Go tüüpi tellimused (tavapärane tellimustüüp) on GPU koguste jaoks sobivad; hüvede tellimused ei ole hetkel toetatud.
>
> Kasutajatele, kes kasutavad hüvede tellimusi (nt Visual Studio Enterprise Subscription) või soovivad kiiresti testida täpsustamist ja juurutamisprotsessi, pakub see juhend ka juhised CPU-põhiseks täpsustamiseks väikese andmekogumiga. Siiski on oluline märkida, et täpsustamise tulemused on märgatavalt paremad, kui kasutatakse GPU-d koos suuremate andmekogumitega.

1. Külastage [Azure ML Studio't](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Täitke järgmised ülesanded, et taotleda *Standard NCADSA100v4 Family* kvanti:

    - Valige vasakult vahekaardilt **Quota**.
    - Valige kasutatav **Virtual machine family**. Näiteks valige **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, mis sisaldab *Standard_NC24ads_A100_v4* GPU-d.
    - Valige navigeerimismenüüst **Request quota**.

        ![Request quota.](../../../../../../translated_images/et/01-04-request-quota.3d3670c3221ab834.png)

    - Kvandi taotlemise lehel sisestage soovitav **New cores limit**. Näiteks 24.
    - Kvandi taotlemise lehel valige **Submit**, et taotleda GPU kvanti.

> [!NOTE]
> Sobivat GPU-d või CPU-d saate valida, viidates [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) dokumentatsioonile.

### Rolli määramise lisamine

Mudelite täpsustamiseks ja juurutamiseks peate esmalt looma kasutajale määratud haldatud identiteedi (UAI) ja sellele sobivad õigused määrama. Seda UAI-d kasutatakse juurutamise autentimiseks.

#### Kasutajale määratud hallatud identiteedi (UAI) loomine

1. Tippige portaalilehe ülaosas otsiribale *managed identities* ja valige kuvatud valikute hulgast **Managed Identities**.

    ![Type managed identities.](../../../../../../translated_images/et/01-05-type-managed-identities.9297b6039874eff8.png)

1. Valige **+ Create**.

    ![Select create.](../../../../../../translated_images/et/01-06-select-create.936d8d66d7144f9a.png)

1. Täitke järgmised ülesanded:

    - Valige oma Azure **Subscription**.
    - Valige kasutatav **Resource group** (looge vajadusel uus).
    - Valige soovitud **Region**.
    - Sisestage **Name**. See peab olema ainulaadne väärtus.

1. Valige **Review + create**.

1. Valige **+ Create**.

#### Pane hallatud identiteedile lisaks Contributor rolli määramine

1. Navigeerige loodud hallatud identiteedini.

1. Valige vasakul vahekaardil **Azure role assignments**.

1. Valige navigeerimismenüüst **+Add role assignment**.

1. Rolli määramise lisamise lehel täitke järgmised ülesanded:
    - Valige **Scope** väärtuseks **Resource group**.
    - Valige oma Azure **Subscription**.
    - Valige kasutatav **Resource group**.
    - Valige rolliks **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/et/01-07-fill-contributor-role.29ca99b7c9f687e0.png)

1. Valige **Save**.

#### Pane hallatud identiteedile Storage Blob Data Reader rolli määramine

1. Tippige portaalilehe ülaosas otsiribale *storage accounts* ja valige kuvatud valikute hulgast **Storage accounts**.

    ![Type storage accounts.](../../../../../../translated_images/et/01-08-type-storage-accounts.1186c8e42933e49b.png)

1. Valige see salvestuskonto, mis on seotud loodud Azure Machine Learning tööruumiga. Näiteks *finetunephistorage*.

1. Täitke järgmised ülesanded, et jõuda rolli määramise lisamise lehele:

    - Navigeerige loodud Azure Storage kontole.
    - Valige vasakul vahekaardil **Access Control (IAM)**.
    - Valige navigeerimismenüüst **+ Add**.
    - Valige navigeerimismenüüst **Add role assignment**.

    ![Add role.](../../../../../../translated_images/et/01-09-add-role.d2db22fec1b187f0.png)

1. Rolli määramise lisamise lehel täitke järgmised ülesanded:

    - Rolli lehel tippige otsiribale *Storage Blob Data Reader* ja valige vastav valik.
    - Rolli lehel valige **Next**.
    - Liikmesuse lehel valige **Assign access to** **Managed identity**.
    - Liikmesuse lehel valige **+ Select members**.
    - Hallatud identiteetide valimise lehel valige oma Azure **Subscription**.
    - Hallatud identiteetide valimise lehel valige hallatud identiteediks **Manage Identity**.
    - Hallatud identiteetide lehel valige loodud haldatud identiteet, nt *finetunephi-managedidentity*.
    - Hallatud identiteetide lehel valige **Select**.

    ![Select managed identity.](../../../../../../translated_images/et/01-10-select-managed-identity.5ce5ba181f72a4df.png)

1. Valige **Review + assign**.

#### Pane hallatud identiteedile AcrPull rolli määramine

1. Tippige portaalilehe ülaosas otsiribale *container registries* ja valige kuvatud valikute hulgast **Container registries**.

    ![Type container registries.](../../../../../../translated_images/et/01-11-type-container-registries.ff3b8bdc49dc596c.png)

1. Valige konteineriregister, mis on seotud Azure Machine Learning tööruumiga. Näiteks *finetunephicontainerregistries*.

1. Täitke järgmised ülesanded, et jõuda rolli määramise lisamise lehele:

    - Valige vasakul vahekaardil **Access Control (IAM)**.
    - Valige navigeerimismenüüst **+ Add**.
    - Valige navigeerimismenüüst **Add role assignment**.

1. Rolli määramise lisamise lehel täitke järgmised ülesanded:

    - Rolli lehel tippige otsiribale *AcrPull* ja valige vastav valik.
    - Rolli lehel valige **Next**.
    - Liikmesuse lehel valige **Assign access to** **Managed identity**.
    - Liikmesuse lehel valige **+ Select members**.
    - Hallatud identiteetide valimise lehel valige oma Azure **Subscription**.
    - Hallatud identiteetide valimise lehel valige hallatud identiteediks **Manage Identity**.
    - Hallatud identiteetide lehel valige loodud haldatud identiteet, nt *finetunephi-managedidentity*.
    - Hallatud identiteetide lehel valige **Select**.
    - Valige **Review + assign**.

### Projekti seadistamine

Nüüd loote kausta, milles töötada, ja seadistate virtuaalkeskkonna, et arendada programmi, mis suhtleb kasutajatega ja kasutab Azure Cosmos DB-s salvestatud vestlusajaloo infot vastuste koostamisel.

#### Looge kaust, milles töötada

1. Avage terminaliakna ja sisestage käsk kausta *finetune-phi* loomiseks vaikeasukohta.

    ```console
    mkdir finetune-phi
    ```

1. Sisestage järgmine käsk terminalis, et minna äsja loodud *finetune-phi* kausta.

    ```console
    cd finetune-phi
    ```

#### Looge virtuaalkeskkond

1. Sisestage järgmine käsk terminalis, et luua virtuaalkeskkond nimega *.venv*.

    ```console
    python -m venv .venv
    ```

1. Sisestage järgmine käsk terminalis, et aktiveerida virtuaalkeskkond.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> Kui see õnnestus, peaksite käsureale eelnema nägema *(.venv)*.

#### Paigaldage vajalikud paketid

1. Sisestage järgmised käsud terminalis, et paigaldada vajalikud paketid.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Looge projekti failid
Selles harjutuses loote oma projekti jaoks põhifailid. Need failid sisaldavad skripte andmekogumi allalaadimiseks, Azure Machine Learning keskkonna seadistamiseks, Phi-3 mudeli peenhäälestamiseks ja peenhäälestatud mudeli juurutamiseks. Samuti loote *conda.yml* faili, et seadistada peenhäälestuse keskkond.

Selles harjutuses teete järgmist:

- Loote *download_dataset.py* faili andmekogumi allalaadimiseks.
- Loote *setup_ml.py* faili Azure Machine Learning keskkonna seadistamiseks.
- Loote *fine_tune.py* faili kaustas *finetuning_dir* Phi-3 mudeli peenhäälestamiseks andmekogumi abil.
- Loote *conda.yml* faili peenhäälestamise keskkonna seadistamiseks.
- Loote *deploy_model.py* faili peenhäälestatud mudeli juurutamiseks.
- Loote *integrate_with_promptflow.py* faili peenhäälestatud mudeli integreerimiseks ja mudeli käivitamiseks Prompt flow abil.
- Loote flow.dag.yml faili, et seadistada töölõigu struktuur Prompt flow jaoks.
- Loote *config.py* faili, kuhu sisestate Azure teabe.

> [!NOTE]
>
> Täielik kaustastruktuur:
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

1. Valige loodud *finetune-phi* kaust, mis asub aadressil *C:\Users\yourUserName\finetune-phi*.

    ![Ava projekti kaust.](../../../../../../translated_images/et/01-12-open-project-folder.1fff9c7f41dd1639.png)

1. Visual Studio Code vasaku paneeli sees paremklõpsake ja valige **New File**, et luua uus fail nimega *download_dataset.py*.

1. Visual Studio Code vasaku paneeli sees paremklõpsake ja valige **New File**, et luua uus fail nimega *setup_ml.py*.

1. Visual Studio Code vasaku paneeli sees paremklõpsake ja valige **New File**, et luua uus fail nimega *deploy_model.py*.

    ![Loo uus fail.](../../../../../../translated_images/et/01-13-create-new-file.c17c150fff384a39.png)

1. Visual Studio Code vasaku paneeli sees paremklõpsake ja valige **New Folder**, et luua uus kaust nimega *finetuning_dir*.

1. *finetuning_dir* kaustas looge uus fail nimega *fine_tune.py*.

#### Looge ja seadistage *conda.yml* fail

1. Visual Studio Code vasaku paneeli sees paremklõpsake ja valige **New File**, et luua uus fail nimega *conda.yml*.

1. Lisa järgmine kood *conda.yml* faili, et seadistada Phi-3 mudeli peenhäälestuse keskkond.

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

1. Visual Studio Code vasaku paneeli sees paremklõpsake ja valige **New File**, et luua uus fail nimega *config.py*.

1. Lisa järgmine kood *config.py* faili, et sisestada oma Azure teave.

    ```python
    # Azure seaded
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "Testirühm"

    # Azure Masinõppe sätted
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-tööruum"

    # Azure Haldusega Identiteedi sätted
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-halduseidentiteet"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Andmekogu failirajad
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Peenhäälestatud mudeli sätted
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-mudel"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-lõpp-punkt"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-lansseerimine"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{teie-lõpp-punkti-nimi}.{teie-regioon}.inference.ml.azure.com/score"
    ```

#### Lisage Azure keskkonnamuutujad

1. Tehke järgmised toimingud Azure tellimuse ID lisamiseks:

    - Tippige portaali lehe ülaosas otsinguribale *subscriptions* ja valige kuvatavast valikust **Subscriptions**.
    - Valige Azure tellimus, mida hetkel kasutate.
    - Kopeerige ja kleepige oma tellimuse ID *config.py* faili.

    ![Leia tellimuse ID.](../../../../../../translated_images/et/01-14-find-subscriptionid.4f4ca33555f1e637.png)

1. Tehke järgmised toimingud Azure tööruumi nime lisamiseks:

    - Navigeerige loodud Azure Machine Learning ressursile.
    - Kopeerige ja kleepige oma konto nimi *config.py* faili.

    ![Leia Azure Machine Learning nimi.](../../../../../../translated_images/et/01-15-find-AZML-name.1975f0422bca19a7.png)

1. Tehke järgmised toimingud Azure ressursside grupi nime lisamiseks:

    - Navigeerige loodud Azure Machine Learning ressursile.
    - Kopeerige ja kleepige oma Azure ressursside grupi nimi *config.py* faili.

    ![Leia ressursside grupi nimi.](../../../../../../translated_images/et/01-16-find-AZML-resourcegroup.855a349d0af134a3.png)

2. Tehke järgmised toimingud Azure hallatava identiteedi nime lisamiseks:

    - Navigeerige loodud Hallatavate identiteetide ressursile.
    - Kopeerige ja kleepige oma Azure hallatava identiteedi nimi *config.py* faili.

    ![Leia UAI.](../../../../../../translated_images/et/01-17-find-uai.3529464f53499827.png)

### Valmistage andmekogum ette peenhäälestuseks

Selles harjutuses käivitate faili *download_dataset.py*, et alla laadida *ULTRACHAT_200k* andmekogumid oma lokaalsesse keskkonda. Seejärel kasutate neid andmekogumeid Phi-3 mudeli peenhäälestamiseks Azure Machine Learning keskkonnas.

#### Laadige oma andmekogum alla, kasutades *download_dataset.py*

1. Avage Visual Studio Code-is fail *download_dataset.py*.

1. Lisage *download_dataset.py* järgmine kood.

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
        # Laadi andmestik määratud nime, konfiguratsiooni ja jagunemissuhtega
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Jaga andmestik treening- ja testkomplektideks (80% treening, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Loo kataloog, kui see puudub
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Ava fail kirjutamisrežiimis
        with open(filepath, 'w', encoding='utf-8') as f:
            # Läbi iga kirje andmestikus
            for record in dataset:
                # Kirjuta kirje JSON-objektina faili
                json.dump(record, f)
                # Kirjuta uue rea märk eraldamaks kirjeid
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Laadi ja jaga ULTRACHAT_200k andmestik konkreetse konfiguratsiooni ja jagunemissuhtega
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Eristu treening- ja testandmestikud jagunemusest
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Salvesta treeningandmestik JSONL faili
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Salvesta testandmestik eraldi JSONL faili
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **Juhised minimaalse andmekogumiga peenhäälestamiseks CPU abil**
>
> Kui soovite peenhäälestuseks kasutada CPU-d, on see lähenemine ideaalne neile, kellel on õigus tellimustele (nt Visual Studio Enterprise Subscription) või kui soovite kiiresti testida peenhäälestust ja juurutamisprotsessi.
>
> Asendage `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` väärtusega `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Tippige terminali järgmine käsk skripti käivitamiseks ja andmekogumi allalaadimiseks oma lokaalsesse keskkonda.

    ```console
    python download_data.py
    ```

1. Kontrollige, kas andmekogumid salvestati edukalt teie kohalikku *finetune-phi/data* kausta.

> [!NOTE]
>
> **Andmekogumi suurus ja peenhäälestuse aeg**
>
> Selles E2E näites kasutate ainult 1% andmekogumist (`train_sft[:1%]`). See vähendab oluliselt andmemahtu, kiirendades nii üleslaadimist kui ka peenhäälestust. Võite reguleerida protsenti, et leida sobiv tasakaal treeningaja ja mudeli jõudluse vahel. Väiksema andmekogumi valimine vähendab peenhäälestuseks vajalikku aega, muutes protsessi E2E näite jaoks hallatavaks.

## Stsenaarium 2: Peenhäälestage Phi-3 mudel ja juurutage Azure Machine Learning Studio's

### Seadistage Azure CLI

Peate seadistama Azure CLI, et autentida oma keskkond. Azure CLI võimaldab hallata Azure ressursse otse käsurealt ja pakub õigused, mis on vajalikud Azure Machine Learningu ressurssidele juurdepääsuks. Alustamiseks paigaldage [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. Avage terminali aken ja tippige järgmine käsk, et sisse logida oma Azure kontole.

    ```console
    az login
    ```

1. Valige kasutatav Azure konto.

1. Valige kasutatav Azure tellimus.

    ![Leia ressursside grupi nimi.](../../../../../../translated_images/et/02-01-login-using-azure-cli.dfde31cb75e58a87.png)

> [!TIP]
>
> Kui teil on raske Azure'i sisse logida, proovige kasutada seadmekoodi. Avage terminali aken ja tippige järgmine käsk Azure kontole sisselogimiseks:
>
> ```console
> az login --use-device-code
> ```
>

### Peenhäälestage Phi-3 mudel

Selles harjutuses peenhäälestate Phi-3 mudeli, kasutades antud andmekogumit. Esiteks määratlete peenhäälestuse protsessi failis *fine_tune.py*. Seejärel seadistate Azure Machine Learning keskkonna ja käivitate peenhäälestuse protsessi skripti *setup_ml.py* abil. See skript tagab, et peenhäälestus toimub Azure Machine Learning keskkonnas.

Käivitades *setup_ml.py*, käivitate peenhäälestusprotsessi Azure Machine Learning keskkonnas.

#### Lisage kood *fine_tune.py* faili

1. Navigeerige kausta *finetuning_dir* ja avage Visual Studio Code-is fail *fine_tune.py*.

1. Lisage *fine_tune.py* järgmine kood.

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

    # Vea INVALID_PARAMETER_VALUE vältimiseks MLflow-s, keelake MLflow integratsioon
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Logimise seadistus
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

1. Salvestage ja sulgege fail *fine_tune.py*.

> [!TIP]
> **Võite peenhäälestada Phi-3.5 mudelit**
>
> Failis *fine_tune.py* võite muuta `pretrained_model_name` väärtuse `"microsoft/Phi-3-mini-4k-instruct"` mistahes soovitud mudeli nimeks. Näiteks kui muudate selle `"microsoft/Phi-3.5-mini-instruct"`-iks, kasutate peenhäälestusel Phi-3.5-mini-instruct mudelit. Mudeli nime leidmiseks ja kasutamiseks külastage saidilt [Hugging Face](https://huggingface.co/) mudelit, mis teile huvi pakub, ja kopeerige seejärel selle nimi oma skripti `pretrained_model_name` väljale.
>
> <image type="content" src="../../../../imgs/02/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Phi-3.5 peenhäälestus.">
>

#### Lisage kood *setup_ml.py* faili

1. Avage Visual Studio Code-is fail *setup_ml.py*.

1. Lisage *setup_ml.py* järgmine kood.

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

    # Konstandid

    # Järgnevate ridade lahtikommenteerimiseks kasuta treenimiseks CPU eksemplari
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Järgnevate ridade lahtikommenteerimiseks kasuta treenimiseks GPU eksemplari
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Asenda oma arvutusklastri asukohaga
    FINETUNING_DIR = "./finetuning_dir" # Tee peenhäälestusskriptini
    TRAINING_ENV_NAME = "phi-3-training-environment" # Treeningkeskkonna nimi
    MODEL_OUTPUT_DIR = "./model_output" # Tee mudeli väljundkaustani Azure ML-s

    # Logimise seadistus protsessi jälgimiseks
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
            image=DOCKER_IMAGE_NAME,  # Dokkeri pilt keskkonna jaoks
            conda_file=CONDA_FILE,  # Conda keskkonna fail
            name=TRAINING_ENV_NAME,  # Keskkonna nimi
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
                tier="Dedicated",  # Arvutusklastri tase
                min_instances=0,  # Miinimum eksemplaride arv
                max_instances=1  # Maksimum eksemplaride arv
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Oota, kuni klaster luuakse
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Tee fine_tune.py faili
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Treeningkeskkond
            compute=compute_name,  # Kasutatav arvutusklaster
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Tee treeningandmete faili
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Tee hindamisandmete faili
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # ML kliendi initsialiseerimine
        ml_client = get_ml_client()

        # Keskkonna loomine
        env = create_or_get_environment(ml_client)
        
        # Olemasoleva arvutusklastri loomine või kasutamine
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Peenhäälestustöö loomine ja esitlemine
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Töötöö esitamine
        ml_client.jobs.stream(returned_job.name)  # Töötöö logide voogesitus
        
        # Töötöö nime talletamine
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. Asendage `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` ja `LOCATION` oma konkreetsete andmetega.

    ```python
   # Eemaldage järgmiste ridade kommentaarid, et kasutada koolituseks GPU-d
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Asendage oma arvutusklastri asukohaga
    ```

> [!TIP]
>
> **Juhised minimaalse andmekogumiga peenhäälestuseks CPU abil**
>
> Kui soovite peenhäälestuseks kasutada CPU-d, on see lähenemine ideaalne neile, kellel on õigus tellimustele (nt Visual Studio Enterprise Subscription) või kui soovite kiiresti testida peenhäälestust ja juurutamisprotsessi.
>
> 1. Avage fail *setup_ml*.
> 1. Asendage `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` ja `DOCKER_IMAGE_NAME` järgmiselt. Kui teil ei ole juurdepääsu *Standard_E16s_v3* instantsile, võite kasutada võrdväärset CPU instantsi või taotleda uut kvooti.
> 1. Asendage `LOCATION` oma teemakohase andmega.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Tippige järgmine käsk skripti *setup_ml.py* käivitamiseks ja peenhäälestuse alustamiseks Azure Machine Learning keskkonnas.

    ```python
    python setup_ml.py
    ```

1. Selles harjutuses peenhäälestasite edukalt Phi-3 mudeli, kasutades Azure Machine Learningut. Käivitades skripti *setup_ml.py*, seadistasite Azure Machine Learning keskkonna ja käivitasite *fine_tune.py* failis määratletud peenhäälestusprotsessi. Pange tähele, et peenhäälestus võib võtta märkimisväärselt aega. Pärast `python setup_ml.py` käivitamist peate protsessi lõpuni ootama. Peenhäälestuse töö olekut saate jälgida terminalis kuvatava lingi kaudu Azure Machine Learning portaali.

    ![Vaata peenhäälestustöö olekut.](../../../../../../translated_images/et/02-02-see-finetuning-job.59393bc3b143871e.png)

### Juurutage peenhäälestatud mudel

Et integreerida peenhäälestatud Phi-3 mudel Prompt Flow’ga, tuleb mudel juurutada, et see oleks reaalajas päringuteks kättesaadav. See protsess hõlmab mudeli registreerimist, võrgupunkti loomist ja mudeli juurutamist.

#### Määrake mudeli nimi, endpoini nimi ja juurutuse nimi

1. Avage fail *config.py*.

1. Asendage `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` soovitud mudeli nimega.

1. Asendage `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` soovitud endpoini nimega.

1. Asendage `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` soovitud juurutuse nimega.

#### Lisage kood faili *deploy_model.py*

Faili *deploy_model.py* käivitamine automatiseerib kogu juurutamisprotsessi. See registreerib mudeli, loob endpoini ja täidab juurutuse vastavalt *config.py* failis määratud seadetele, sealhulgas mudeli nimele, endpoini nimele ja juurutuse nimele.

1. Avage Visual Studio Code’is fail *deploy_model.py*.

1. Lisage *deploy_model.py* järgmine kood.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Konfiguratsiooni importimine
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

    # Konstandid
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Logimise seadistamine
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
            # Praeguste lõpp-punkti andmete hankimine
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Praeguse liikluse jaotuse logimine silumiseks
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Liikluse jaotuse seadistamine juurutamiseks
            endpoint.traffic = {deployment_name: 100}
            
            # Lõpp-punkti uuendamine uue liikluse jaotusega
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Uuendatud liikluse jaotuse logimine silumiseks
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Protsessi käigus tekkivate vigade logimine
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

1. Tehke järgmised toimingud töö nime (JOB_NAME) saamiseks:

    - Navigeerige loodud Azure Machine Learning ressursile.
    - Valige **Studio web URL**, et avada Azure Machine Learning tööruum.
    - Vasakpoolsest menüüst valige **Jobs**.
    - Valige peenhäälestuse eksperiment, nt *finetunephi*.
    - Valige loodud töö.
- Kopeeri ja kleebi oma töö nimi faili *deploy_model.py* ritta `JOB_NAME = "your-job-name"`.

1. Asenda `COMPUTE_INSTANCE_TYPE` oma konkreetsete andmetega.

1. Sisesta järgmine käsk, et käivitada *deploy_model.py* skript ja alustada paigaldusprotsessi Azure Machine Learningis.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> Selleks, et vältida täiendavaid kulutusi oma kontol, veendu, et kustutad loodud otspunkti Azure Machine Learningi tööruumis.
>

#### Kontrolli paigalduse olekut Azure Machine Learningi tööruumis

1. Mine aadressile [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Ava Azure Machine Learningi tööruum, mille sa lõid.

1. Vali **Studio web URL**, et avada Azure Machine Learningi tööruum.

1. Vali vasakpoolsest menüüst **Endpoints**.

    ![Select endpoints.](../../../../../../translated_images/et/02-03-select-endpoints.c3136326510baff1.png)

2. Vali loodud otspunkt.

    ![Select endpoints that you created.](../../../../../../translated_images/et/02-04-select-endpoint-created.0363e7dca51dabb4.png)

3. Sellel lehel saad hallata paigalduse protsessi käigus loodud otspunkte.

## Stsenaarium 3: Integreeri Prompt flow'ga ja suhtle oma kohandatud mudeliga

### Integreeri kohandatud Phi-3 mudel Prompt flow'ga

Pärast edukat peenhäälestatud mudeli paigaldust saad selle nüüd integreerida Prompt flow'ga, et kasutada oma mudelit reaalajas rakendustes, võimaldades mitmesuguseid interaktiivseid ülesandeid oma kohandatud Phi-3 mudeliga.

#### Määra api võti ja otspunkti URI peenhäälestatud Phi-3 mudelile

1. Mine Azure Machine Learningi tööruumi, mille sa lõid.
1. Vali vasakpoolsest menüüst **Endpoints**.
1. Vali loodud otspunkt.
1. Vali navigeerimismenüüst **Consume**.
1. Kopeeri ja kleebi oma **REST endpoint** faili *config.py*, asendades `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` oma **REST endpoint**-i aadressiga.
1. Kopeeri ja kleebi oma **Primary key** faili *config.py*, asendades `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` oma **Primary key**-ga.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/et/02-05-copy-apikey-endpoint.88b5a92e6462c53b.png)

#### Lisa kood faili *flow.dag.yml*

1. Ava *flow.dag.yml* fail Visual Studio Code'is.

1. Lisa järgmine kood faili *flow.dag.yml*.

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

#### Lisa kood faili *integrate_with_promptflow.py*

1. Ava *integrate_with_promptflow.py* fail Visual Studio Code'is.

1. Lisa järgmine kood faili *integrate_with_promptflow.py*.

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

    # Logimise seadistamine
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

### Suhtle oma kohandatud mudeliga

1. Sisesta järgmine käsk, et käivitada *deploy_model.py* skript ja alustada paigaldusprotsessi Azure Machine Learningis.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Näide tulemustest: nüüd saad suhelda oma kohandatud Phi-3 mudeliga. Soovitatav on esitada küsimusi, mis põhinevad peenhäälestamiseks kasutatud andmetel.

    ![Prompt flow example.](../../../../../../translated_images/et/02-06-promptflow-example.89384abaf3ad71f6.png)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud kasutades tehisintellekti tõlke teenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüame täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument oma algkeeles tuleks pidada autoriteetseks allikaks. Kriitilise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisel tekkida võivate arusaamatuste või valesti tõlgendamise eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->