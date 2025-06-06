<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-05-09T17:36:39+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "fi"
}
-->
# Hienosäädä ja integroi mukautetut Phi-3-mallit Prompt flow’n kanssa

Tämä end-to-end (E2E) -esimerkki perustuu Microsoft Tech Communityn oppaaseen "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)". Se esittelee mukautettujen Phi-3-mallien hienosäädön, käyttöönoton ja integroinnin Prompt flow’n kanssa.

## Yleiskatsaus

Tässä E2E-esimerkissä opit, kuinka hienosäätää Phi-3-malli ja integroida se Prompt flow’hun. Hyödyntämällä Azure Machine Learningiä ja Prompt flow’ta luot työnkulun mukautettujen tekoälymallien käyttöönottoa ja hyödyntämistä varten. Tämä E2E-esimerkki on jaettu kolmeen skenaarioon:

**Skenaario 1: Azure-resurssien perustaminen ja valmistautuminen hienosäätöön**

**Skenaario 2: Phi-3-mallin hienosäätö ja käyttöönotto Azure Machine Learning Studiossa**

**Skenaario 3: Integrointi Prompt flow’n kanssa ja keskustelu mukautetun mallin kanssa**

Tässä on yleiskatsaus tähän E2E-esimerkkiin.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.dfeb1f15c7d3c8989fb267a05ac83a25485a7230bde037df9d3d92336afc1993.fi.png)

### Sisällysluettelo

1. **[Skenaario 1: Azure-resurssien perustaminen ja valmistautuminen hienosäätöön](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Luo Azure Machine Learning -työtila](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Pyydä GPU-kiintiö Azure-tilauksessa](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Lisää roolimääritys](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Perusta projekti](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Valmistele aineisto hienosäätöä varten](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Skenaario 2: Phi-3-mallin hienosäätö ja käyttöönotto Azure Machine Learning Studiossa](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Ota Azure CLI käyttöön](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Hienosäädä Phi-3-malli](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ota hienosäädetty malli käyttöön](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Skenaario 3: Integroi Prompt flow’n kanssa ja keskustele mukautetun mallisi kanssa](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integroi mukautettu Phi-3-malli Prompt flow’hun](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Keskustele mukautetun mallisi kanssa](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Skenaario 1: Azure-resurssien perustaminen ja valmistautuminen hienosäätöön

### Luo Azure Machine Learning -työtila

1. Kirjoita *azure machine learning* **hakupalkkiin** portaalin sivun yläosassa ja valitse **Azure Machine Learning** ilmestyvistä vaihtoehdoista.

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.321cff72d18a51c06dee2db7463868f3ca6619559a5d68b7795d70f4a8b3a683.fi.png)

1. Valitse navigaatiovalikosta **+ Create**.

1. Valitse navigaatiovalikosta **New workspace**.

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.9bd9208488fcf38226fc8d3cefffecb2cb14f414f6d8d982492c1bde8634e24a.fi.png)

1. Tee seuraavat toimet:

    - Valitse Azure-**Subscription**.
    - Valitse käytettävä **Resource group** (luo uusi tarvittaessa).
    - Kirjoita **Workspace Name**. Sen on oltava yksilöllinen.
    - Valitse haluamasi **Region**.
    - Valitse käytettävä **Storage account** (luo uusi tarvittaessa).
    - Valitse käytettävä **Key vault** (luo uusi tarvittaessa).
    - Valitse käytettävä **Application insights** (luo uusi tarvittaessa).
    - Valitse käytettävä **Container registry** (luo uusi tarvittaessa).

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.b2ebbef59952cd17d16b1f82adc252bf7616f8638d451e3c6595ffefe44f2cfa.fi.png)

1. Valitse **Review + Create**.

1. Valitse **Create**.

### Pyydä GPU-kiintiö Azure-tilauksessa

Tässä E2E-esimerkissä käytät hienosäätöön *Standard_NC24ads_A100_v4 GPU*:ta, joka vaatii kiintiöpyynnön, ja käyttöönottoon *Standard_E4s_v3* CPU:ta, joka ei vaadi kiintiöpyyntöä.

> [!NOTE]
>
> Vain Pay-As-You-Go -tilaukset (vakio-tilauksen tyyppi) voivat saada GPU-kiintiöitä; benefit-tilauksia ei tällä hetkellä tueta.
>
> Benefit-tilauksia (kuten Visual Studio Enterprise Subscription) käyttävät tai hienosäätöä ja käyttöönottoa nopeasti testaavat voivat käyttää tässä oppaassa myös pienellä aineistolla CPU:lla hienosäätöä. On kuitenkin tärkeää huomata, että hienosäädön tulokset ovat merkittävästi parempia GPU:lla ja suuremmilla aineistoilla.

1. Siirry osoitteeseen [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Tee seuraavat toimet pyytääksesi *Standard NCADSA100v4 Family* -kiintiötä:

    - Valitse vasemman reunan välilehdeltä **Quota**.
    - Valitse käytettävä **Virtual machine family**. Esimerkiksi **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, joka sisältää *Standard_NC24ads_A100_v4* GPU:n.
    - Valitse navigaatiovalikosta **Request quota**.

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.ddf063c7cda9799b8ef6fbde6c3c796201578fe9078feb1c624ed75c7705ad18.fi.png)

    - Request quota -sivulla syötä haluamasi **New cores limit**. Esimerkiksi 24.
    - Valitse Request quota -sivulla **Submit** GPU-kiintiön pyytämiseksi.

> [!NOTE]
> Voit valita tarpeisiisi sopivan GPU:n tai CPU:n tutustumalla [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) -dokumentaatioon.

### Lisää roolimääritys

Hienosäätöä ja käyttöönottoa varten sinun täytyy ensin luoda User Assigned Managed Identity (UAI) ja antaa sille tarvittavat oikeudet. Tätä UAI:ta käytetään todennuksessa käyttöönoton aikana.

#### Luo User Assigned Managed Identity (UAI)

1. Kirjoita *managed identities* **hakupalkkiin** portaalin sivun yläosassa ja valitse **Managed Identities** ilmestyvistä vaihtoehdoista.

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.8bf5dc5a4fa3e852f897ec1a983e506c2bc7b7113d159598bf0adeb66d20a5c4.fi.png)

1. Valitse **+ Create**.

    ![Select create.](../../../../../../translated_images/01-06-select-create.025632b7b54fe323f7d38edabbae05dd23f4665d0731f7143719c27c32e7e84f.fi.png)

1. Tee seuraavat toimet:

    - Valitse Azure-**Subscription**.
    - Valitse käytettävä **Resource group** (luo uusi tarvittaessa).
    - Valitse haluamasi **Region**.
    - Kirjoita **Name**. Sen on oltava yksilöllinen.

1. Valitse **Review + create**.

1. Valitse **+ Create**.

#### Lisää Contributor-roolimääritys Managed Identitylle

1. Siirry luomaasi Managed Identity -resurssiin.

1. Valitse vasemman reunan välilehdeltä **Azure role assignments**.

1. Valitse navigaatiovalikosta **+ Add role assignment**.

1. Add role assignment -sivulla tee seuraavat toimet:
    - Valitse **Scope** arvoksi **Resource group**.
    - Valitse Azure-**Subscription**.
    - Valitse käytettävä **Resource group**.
    - Valitse **Role** arvoksi **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.8936866326c7cdc3b876f14657e03422cca9dbff8b193dd541a693ce34407b26.fi.png)

1. Valitse **Save**.

#### Lisää Storage Blob Data Reader -roolimääritys Managed Identitylle

1. Kirjoita *storage accounts* **hakupalkkiin** portaalin sivun yläosassa ja valitse **Storage accounts** ilmestyvistä vaihtoehdoista.

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.83554a27ff3edb5099ee3fbf7f467b843dabcc0e0e5fbb829a341eab3469ffa5.fi.png)

1. Valitse se tallennustili, joka liittyy luomaasi Azure Machine Learning -työtilaan. Esimerkiksi *finetunephistorage*.

1. Tee seuraavat toimet siirtyäksesi Add role assignment -sivulle:

    - Siirry luomaasi Azure Storage -tiliin.
    - Valitse vasemman reunan välilehdeltä **Access Control (IAM)**.
    - Valitse navigaatiovalikosta **+ Add**.
    - Valitse navigaatiovalikosta **Add role assignment**.

    ![Add role.](../../../../../../translated_images/01-09-add-role.4fef55886792c7e860da4c5a808044e6f7067fb5694f3ed4819a5758c6cc574e.fi.png)

1. Add role assignment -sivulla tee seuraavat toimet:

    - Roolisivulla kirjoita *Storage Blob Data Reader* **hakupalkkiin** ja valitse **Storage Blob Data Reader** vaihtoehdoista.
    - Valitse roolisivulla **Next**.
    - Jäsenet-sivulla valitse **Assign access to** arvoksi **Managed identity**.
    - Jäsenet-sivulla valitse **+ Select members**.
    - Valitse Select managed identities -sivulla Azure-**Subscription**.
    - Valitse Select managed identities -sivulla **Managed identity** arvoksi **Manage Identity**.
    - Valitse Select managed identities -sivulla luomasi Manage Identity. Esimerkiksi *finetunephi-managedidentity*.
    - Valitse Select managed identities -sivulla **Select**.

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.fffa802e4e6ce2de4fe50e64d37d3f2ef268c2ee16f30ec6f92bd1829b5f19c1.fi.png)

1. Valitse **Review + assign**.

#### Lisää AcrPull-roolimääritys Managed Identitylle

1. Kirjoita *container registries* **hakupalkkiin** portaalin sivun yläosassa ja valitse **Container registries** ilmestyvistä vaihtoehdoista.

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.62e58403d73d16a0cc715571c8a7b4105a0e97b1422aa5f26106aff1c0e8a47d.fi.png)

1. Valitse se container registry, joka liittyy Azure Machine Learning -työtilaasi. Esimerkiksi *finetunephicontainerregistries*.

1. Tee seuraavat toimet siirtyäksesi Add role assignment -sivulle:

    - Valitse vasemman reunan välilehdeltä **Access Control (IAM)**.
    - Valitse navigaatiovalikosta **+ Add**.
    - Valitse navigaatiovalikosta **Add role assignment**.

1. Add role assignment -sivulla tee seuraavat toimet:

    - Roolisivulla kirjoita *AcrPull* **hakupalkkiin** ja valitse **AcrPull** vaihtoehdoista.
    - Valitse roolisivulla **Next**.
    - Jäsenet-sivulla valitse **Assign access to** arvoksi **Managed identity**.
    - Jäsenet-sivulla valitse **+ Select members**.
    - Valitse Select managed identities -sivulla Azure-**Subscription**.
    - Valitse Select managed identities -sivulla **Managed identity** arvoksi **Manage Identity**.
    - Valitse Select managed identities -sivulla luomasi Manage Identity. Esimerkiksi *finetunephi-managedidentity*.
    - Valitse Select managed identities -sivulla **Select**.
    - Valitse **Review + assign**.

### Perusta projekti

Nyt luot kansion työtä varten ja asetat virtuaaliympäristön kehittääksesi ohjelman, joka kommunikoi käyttäjien kanssa ja käyttää Azure Cosmos DB:stä tallennettua keskusteluhistoriaa vastauksien tueksi.

#### Luo kansio työtä varten

1. Avaa komentorivi ja kirjoita seuraava komento luodaksesi kansion nimeltä *finetune-phi* oletuspolkuun.

    ```console
    mkdir finetune-phi
    ```

1. Kirjoita komentoriville seuraava komento siirtyäksesi luomaasi *finetune-phi* -kansioon.

    ```console
    cd finetune-phi
    ```

#### Luo virtuaaliympäristö

1. Kirjoita komentoriville seuraava komento luodaksesi virtuaaliympäristön nimeltä *.venv*.

    ```console
    python -m venv .venv
    ```

1. Kirjoita komentoriville seuraava komento aktivoidaksesi virtuaaliympäristön.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> Jos onnistui, näet *(.venv)* ennen komentokehotetta.

#### Asenna tarvittavat paketit

1. Kirjoita komentoriville seuraavat komennot asentaaksesi tarvittavat paketit.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Luo projektitiedostot

Tässä harjoituksessa luot projektimme olennaiset tiedostot. Näihin kuuluvat skriptit aineiston lataamiseen, Azure Machine Learning -ympäristön perustamiseen, Phi-3-mallin hienosäätöön aineiston avulla ja hienosäädetyn mallin käyttöönottoon. Luot myös *conda.yml* -tiedoston hienosäätöympäristön määrittämiseen.

Tässä harjoituksessa:

- Luo *download_dataset.py* tiedosto aineiston lataamista varten.
- Luo *setup_ml.py* tiedosto Azure Machine Learning -ympäristön perustamista varten.
- Luo *fine_tune.py* tiedosto *finetuning_dir* -kansioon hienosäätääksesi Phi-3-mallin aineiston avulla.
- Luo *conda.yml* tiedosto hienosäätöympäristön määrittämiseen.
- Luo *deploy_model.py* tiedosto hienosäädetyn mallin käyttöönottoa varten.
- Luo *integrate_with_promptflow.py* tiedosto hienosäädetyn mallin integroimiseksi ja suorittamiseksi Prompt flow’n avulla.
- Luo flow.dag.yml -tiedosto työnkulun rakenteen määrittämiseksi Prompt flow’hun.
- Luo *config.py* tiedosto Azure-tietojen syöttämiseen.

> [!NOTE]
>
> Koko kansiorakenne:
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

1. Avaa **Visual Studio Code**.

1. Valitse valikkoriviltä **File**.

1. Valitse **Open Folder**.

1. Valitse luomasi *finetune-phi* -kansio, joka sijaitsee polussa *C:\Users\yourUserName\finetune-phi*.

    ![Open project floder.](../../../../../../translated_images/01-12-open-project-folder.1f7f0f79e5d4d62e546e906e1ce5a480cd98d06062ce292b7b99c6cfcd434fdf.fi.png)

1. Visual Studio Coden vasemmassa paneelissa napsauta hiiren oikealla ja valitse **New File** luodaksesi uuden tiedoston nimeltä *download_dataset.py*.

1. Visual Studio Coden vasemmassa paneelissa napsauta hiiren oikealla ja valitse **New File** luodaksesi uuden tiedoston nimeltä *setup_ml.py*.

1. Visual Studio Coden vasemmassa paneelissa napsauta hiiren oikealla ja valitse **New File** luodaksesi uuden tiedoston nimeltä *deploy_model.py*.

    ![Create new file.](../../../../../../translated_images/01-13-create-new-file.40698c2e0415929e7b6dc2b30925677e413f965bac4134d3aefa0b44d443deaf.fi.png)

1. Visual Studio Coden vasemmassa paneelissa napsauta hiiren oikealla ja valitse **New Folder** luodaksesi uuden kansion nimeltä *finetuning_dir*.

1. Luo *finetuning_dir* -kansioon uusi tiedosto nimeltä *fine_tune.py*.

#### Luo ja määritä *conda.yml* -tiedosto

1. Visual Studio Coden vasemmassa paneelissa napsauta hiiren oikealla ja valitse **New File** luodaksesi uuden tiedoston nimeltä *conda.yml*.

1. Lisää seuraava koodi *conda.yml* -tiedostoon hienosäätöympäristön määrittämiseksi Phi-3-mallille.

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

#### Luo ja määritä *config.py* -tiedosto

1. Visual Studio Coden vasemmassa paneelissa napsauta hiiren oikealla ja valitse **New File** luodaksesi uuden tiedoston nimeltä *config.py*.

1. Lisää seuraava koodi *config.py* -tiedostoon Azure-tietojesi lisäämiseksi.

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

#### Lisää Azure-ympäristömuutt
![Löydä tilauksen tunnus.](../../../../../../translated_images/01-14-find-subscriptionid.4daef33360f6d3808a9f1acea2b6b6121c498c75c36cb6ecc6c6b211f0d3b725.fi.png)

1. Suorita seuraavat tehtävät lisätäksesi Azure Workspace -nimen:

    - Siirry luomaasi Azure Machine Learning -resurssiin.
    - Kopioi ja liitä tilisi nimi *config.py* -tiedostoon.

    ![Löydä Azure Machine Learning -nimi.](../../../../../../translated_images/01-15-find-AZML-name.c8efdc5a8f2e594260004695c145fafb4fd903e96715f495a43733560cd706b5.fi.png)

1. Suorita seuraavat tehtävät lisätäksesi Azure Resource Group -nimen:

    - Siirry luomaasi Azure Machine Learning -resurssiin.
    - Kopioi ja liitä Azure Resource Group -nimesi *config.py* -tiedostoon.

    ![Löydä resurssiryhmän nimi.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.0647be51d3f1b8183995949df5866455e5532ef1c3d1f93b33dc9a91d615e882.fi.png)

2. Suorita seuraavat tehtävät lisätäksesi Azure Managed Identity -nimen:

    - Siirry luomaasi Managed Identities -resurssiin.
    - Kopioi ja liitä Azure Managed Identity -nimesi *config.py* -tiedostoon.

    ![Löydä UAI.](../../../../../../translated_images/01-17-find-uai.b0fe7164cacc93b03c3c534daee68da244de6de4e6dcbc2a4e9df43403eb0f1b.fi.png)

### Valmistele aineisto hienosäätöä varten

Tässä harjoituksessa suoritat *download_dataset.py* -tiedoston ladataksesi *ULTRACHAT_200k* -aineistot paikalliseen ympäristöösi. Käytät tätä aineistoa hienosäätämään Phi-3-mallin Azure Machine Learningissä.

#### Lataa aineisto käyttämällä *download_dataset.py* -tiedostoa

1. Avaa *download_dataset.py* -tiedosto Visual Studio Codessa.

1. Lisää seuraava koodi *download_dataset.py* -tiedostoon.

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
> **Ohjeita pienen aineiston kanssa tapahtuvaan hienosäätöön CPU:lla**
>
> Jos haluat käyttää CPU:ta hienosäätöön, tämä menetelmä sopii erityisesti hyötytilauksia (kuten Visual Studio Enterprise Subscription) käyttäville tai nopeaan hienosäädön ja käyttöönoton testaamiseen.
>
> Korvaa `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` with `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Kirjoita seuraava komento terminaaliisi suorittaaksesi skriptin ja ladataksesi aineiston paikalliseen ympäristöön.

    ```console
    python download_data.py
    ```

1. Varmista, että aineistot tallentuivat onnistuneesti paikalliseen *finetune-phi/data* -hakemistoon.

> [!NOTE]
>
> **Aineiston koko ja hienosäädön kesto**
>
> Tässä E2E-esimerkissä käytät vain 1 % aineistosta (`train_sft[:1%]`). Tämä vähentää merkittävästi datan määrää, nopeuttaen sekä latausta että hienosäätöprosessia. Voit säätää prosenttiosuutta löytääksesi sopivan tasapainon koulutusajan ja mallin suorituskyvyn välillä. Pienempi aineistomäärä lyhentää hienosäädön kestoa, mikä tekee prosessista hallittavamman E2E-esimerkissä.

## Tapaus 2: Hienosäädä Phi-3-malli ja ota käyttöön Azure Machine Learning Studiolla

### Määritä Azure CLI

Sinun täytyy määrittää Azure CLI todennusta varten. Azure CLI mahdollistaa Azure-resurssien hallinnan komentoriviltä ja tarjoaa tarvittavat tunnistetiedot Azure Machine Learningin pääsyä varten. Aloita asentamalla [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli).

1. Avaa terminaali ja kirjoita seuraava komento kirjautuaksesi Azure-tilillesi.

    ```console
    az login
    ```

1. Valitse käytettävä Azure-tilisi.

1. Valitse käytettävä Azure-tilauksesi.

    ![Löydä resurssiryhmän nimi.](../../../../../../translated_images/02-01-login-using-azure-cli.b6e8fb6255e8d09673cb48eca2b12aebbb84dfb8817af8a6b1dfd4bb2759d68f.fi.png)

> [!TIP]
>
> Jos sinulla on ongelmia kirjautumisessa Azureen, kokeile käyttää laitekoodia. Avaa terminaali ja kirjoita seuraava komento kirjautuaksesi Azure-tilillesi:
>
> ```console
> az login --use-device-code
> ```
>

### Hienosäädä Phi-3-malli

Tässä harjoituksessa hienosäädät Phi-3-mallin käyttämällä annettua aineistoa. Ensin määrittelet hienosäätöprosessin *fine_tune.py* -tiedostossa. Sitten konfiguroit Azure Machine Learning -ympäristön ja käynnistät hienosäädön suorittamalla *setup_ml.py* -tiedoston. Tämä skripti varmistaa, että hienosäätö tapahtuu Azure Machine Learning -ympäristössä.

Suorittamalla *setup_ml.py* käynnistät hienosäätöprosessin Azure Machine Learning -ympäristössä.

#### Lisää koodi *fine_tune.py* -tiedostoon

1. Siirry *finetuning_dir* -kansioon ja avaa *fine_tune.py* Visual Studio Codessa.

1. Lisää seuraava koodi *fine_tune.py* -tiedostoon.

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

1. Tallenna ja sulje *fine_tune.py* -tiedosto.

> [!TIP]
> **Voit hienosäätää myös Phi-3.5-mallia**
>
> *fine_tune.py* -tiedostossa voit muuttaa `pretrained_model_name` from `"microsoft/Phi-3-mini-4k-instruct"` to any model you want to fine-tune. For example, if you change it to `"microsoft/Phi-3.5-mini-instruct"`, you'll be using the Phi-3.5-mini-instruct model for fine-tuning. To find and use the model name you prefer, visit [Hugging Face](https://huggingface.co/), search for the model you're interested in, and then copy and paste its name into the `pretrained_model_name` -kenttää skriptissäsi.
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Hienosäädä Phi-3.5.":::
>

#### Lisää koodi *setup_ml.py* -tiedostoon

1. Avaa *setup_ml.py* Visual Studio Codessa.

1. Lisää seuraava koodi *setup_ml.py* -tiedostoon.

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

1. Korvaa `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `LOCATION` omilla tiedoillasi.

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **Ohjeita pienen aineiston kanssa tapahtuvaan hienosäätöön CPU:lla**
>
> Jos haluat käyttää CPU:ta hienosäätöön, tämä menetelmä sopii erityisesti hyötytilauksia (kuten Visual Studio Enterprise Subscription) käyttäville tai nopeaan hienosäädön ja käyttöönoton testaamiseen.
>
> 1. Avaa *setup_ml* -tiedosto.
> 1. Korvaa `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `DOCKER_IMAGE_NAME` with the following. If you do not have access to *Standard_E16s_v3*, you can use an equivalent CPU instance or request a new quota.
> 1. Replace `LOCATION` omilla tiedoillasi.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Kirjoita seuraava komento suorittaaksesi *setup_ml.py* -skriptin ja aloittaaksesi hienosäätöprosessin Azure Machine Learningissä.

    ```python
    python setup_ml.py
    ```

1. Tässä harjoituksessa hienosäädit onnistuneesti Phi-3-mallin Azure Machine Learningillä. Suorittamalla *setup_ml.py* -skriptin olet määrittänyt Azure Machine Learning -ympäristön ja käynnistänyt hienosäätöprosessin, joka on määritelty *fine_tune.py* -tiedostossa. Huomaa, että hienosäätö voi kestää jonkin aikaa. Suorittamisen jälkeen `python setup_ml.py` command, you need to wait for the process to complete. You can monitor the status of the fine-tuning job by following the link provided in the terminal to the Azure Machine Learning portal.

    ![See finetuning job.](../../../../../../translated_images/02-02-see-finetuning-job.a28c8552f7b7bc088ccd67dd0c522f7fc1944048d3554bb1b24f95a1169ad538.fi.png)

### Deploy the fine-tuned model

To integrate the fine-tuned Phi-3 model with Prompt Flow, you need to deploy the model to make it accessible for real-time inference. This process involves registering the model, creating an online endpoint, and deploying the model.

#### Set the model name, endpoint name, and deployment name for deployment

1. Open *config.py* file.

1. Replace `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` with the desired name for your model.

1. Replace `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` with the desired name for your endpoint.

1. Replace `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` käytä haluamaasi nimeä käyttöönotollesi.

#### Lisää koodi *deploy_model.py* -tiedostoon

*deploy_model.py* -tiedoston suorittaminen automatisoi koko käyttöönoton. Se rekisteröi mallin, luo endpointin ja suorittaa käyttöönoton config.py -tiedostoon määriteltyjen asetusten mukaan, jotka sisältävät mallin nimen, endpointin nimen ja käyttöönoton nimen.

1. Avaa *deploy_model.py* Visual Studio Codessa.

1. Lisää seuraava koodi *deploy_model.py* -tiedostoon.

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

1. Suorita seuraavat tehtävät saadaksesi `JOB_NAME`:

    - Navigate to Azure Machine Learning resource that you created.
    - Select **Studio web URL** to open the Azure Machine Learning workspace.
    - Select **Jobs** from the left side tab.
    - Select the experiment for fine-tuning. For example, *finetunephi*.
    - Select the job that you created.
    - Copy and paste your job Name into the `JOB_NAME = "your-job-name"` in *deploy_model.py* file.

1. Replace `COMPUTE_INSTANCE_TYPE` omilla tiedoillasi.

1. Kirjoita seuraava komento suorittaaksesi *deploy_model.py* -skriptin ja aloittaaksesi käyttöönoton Azure Machine Learningissä.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> Välttääksesi lisämaksuja, muista poistaa luotu endpoint Azure Machine Learning -työpisteestä.
>

#### Tarkista käyttöönoton tila Azure Machine Learning -työpisteessä

1. Käy osoitteessa [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Siirry luomaasi Azure Machine Learning -työpisteeseen.

1. Valitse **Studio web URL** avataksesi Azure Machine Learning -työpisteen.

1. Valitse vasemman sivupalkin valikosta **Endpoints**.

    ![Valitse endpoints.](../../../../../../translated_images/02-03-select-endpoints.a32f4eb2854cd54ee997f9bec0e842c3084bbc24bd693457b5c6b132fe966bf4.fi.png)

2. Valitse luomasi endpoint.

    ![Valitse luomasi endpoint.](../../../../../../translated_images/02-04-select-endpoint-created.048b4f0f6479c1885b62711a151227a24408679be65dd1039cd2f64448ec5842.fi.png)

3. Tällä sivulla voit hallita käyttöönoton aikana luotuja endpointteja.

## Tapaus 3: Integroi Prompt Flow’n kanssa ja keskustele mukautetulla mallillasi

### Integroi mukautettu Phi-3-malli Prompt Flow’hun

Onnistuneen käyttöönoton jälkeen voit integroida mallisi Prompt Flow’hun käyttääksesi sitä reaaliaikaisissa sovelluksissa, mikä mahdollistaa monenlaiset vuorovaikutteiset tehtävät mukautetulla Phi-3-mallillasi.

#### Aseta api-avain ja endpoint URI hienosäädetyllä Phi-3-mallilla

1. Siirry luomaasi Azure Machine Learning -työpisteeseen.
1. Valitse vasemman sivupalkin valikosta **Endpoints**.
1. Valitse luomasi endpoint.
1. Valitse navigointivalikosta **Consume**.
1. Kopioi ja liitä **REST endpoint** *config.py* -tiedostoon korvaten `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` with your **REST endpoint**.
1. Copy and paste your **Primary key** into the *config.py* file, replacing `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` omalla **Primary keylläsi**.

    ![Kopioi api-avain ja endpoint URI.](../../../../../../translated_images/02-05-copy-apikey-endpoint.602de7450770e9984149dc7da7472bacafbf0e8447e2adb53896ad93b1dc7684.fi.png)

#### Lisää koodi *flow.dag.yml* -tiedostoon

1. Avaa *flow.dag.yml* Visual Studio Codessa.

1. Lisää seuraava koodi *flow.dag.yml* -tiedostoon.

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

#### Lisää koodi *integrate_with_promptflow.py* -tiedostoon

1. Avaa *integrate_with_promptflow.py* Visual Studio Codessa.

1. Lisää seuraava koodi *integrate_with_promptflow.py* -tiedostoon.

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

### Keskustele mukautetulla mallillasi

1. Kirjoita seuraava komento suorittaaksesi *deploy_model.py* -skriptin ja aloittaaksesi käyttöönoton Azure Machine Learningissä.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Tässä esimerkki tuloksista: nyt voit keskustella mukautetun Phi-3 -mallisi kanssa. On suositeltavaa esittää kysymyksiä aineiston pohjalta, jota käytettiin hienosäätöön.

    ![Prompt flow -esimerkki.](../../../../../../translated_images/02-06-promptflow-example.023c07a4be8f02199e04eaf49f40ba24415da1be2274cbda9a7aa39776acd0bb.fi.png)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa mahdollisista väärinymmärryksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.