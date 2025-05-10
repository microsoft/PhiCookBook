<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-09T18:12:40+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "fi"
}
-->
# Hienosäädä ja integroi mukautetut Phi-3-mallit Prompt flow’n kanssa Azure AI Foundryssa

Tämä kokonaisvaltainen (E2E) esimerkki perustuu Microsoft Tech Communityn oppaaseen "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)". Se esittelee mukautettujen Phi-3-mallien hienosäätö-, käyttöönotto- ja integrointiprosessit Prompt flow’n kanssa Azure AI Foundryssa. Toisin kuin E2E-esimerkki "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", jossa koodi ajettiin paikallisesti, tässä opetusohjelmassa keskitytään täysin mallin hienosäätöön ja integrointiin Azure AI / ML Studiossa.

## Yleiskatsaus

Tässä E2E-esimerkissä opit hienosäätämään Phi-3-mallin ja integroimaan sen Prompt flow’n kanssa Azure AI Foundryssa. Hyödyntämällä Azure AI / ML Studiota luot työnkulun mukautettujen tekoälymallien käyttöönottoon ja hyödyntämiseen. Tämä E2E-esimerkki on jaettu kolmeen skenaarioon:

**Skenaario 1: Azure-resurssien perustaminen ja valmistautuminen hienosäätöön**

**Skenaario 2: Phi-3-mallin hienosäätö ja käyttöönotto Azure Machine Learning Studiossa**

**Skenaario 3: Integrointi Prompt flow’n kanssa ja keskustelu mukautetulla mallillasi Azure AI Foundryssa**

Tässä on yleiskatsaus tähän E2E-esimerkkiin.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.fi.png)

### Sisällysluettelo

1. **[Skenaario 1: Azure-resurssien perustaminen ja valmistautuminen hienosäätöön](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Luo Azure Machine Learning -työtila](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Pyydä GPU-kiintiöt Azure-tilauksessa](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Lisää roolimääritys](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Perusta projekti](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Valmistele aineisto hienosäätöä varten](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Skenaario 2: Phi-3-mallin hienosäätö ja käyttöönotto Azure Machine Learning Studiossa](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Hienosäädä Phi-3-malli](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ota hienosäädetty Phi-3-malli käyttöön](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Skenaario 3: Integroi Prompt flow’n kanssa ja keskustele mukautetulla mallillasi Azure AI Foundryssa](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integroi mukautettu Phi-3-malli Prompt flow’n kanssa](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Keskustele mukautetun Phi-3-mallisi kanssa](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Skenaario 1: Azure-resurssien perustaminen ja valmistautuminen hienosäätöön

### Luo Azure Machine Learning -työtila

1. Kirjoita *azure machine learning* **hakupalkkiin** portaalin sivun yläosassa ja valitse ilmestyvistä vaihtoehdoista **Azure Machine Learning**.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.fi.png)

2. Valitse navigointivalikosta **+ Create**.

3. Valitse navigointivalikosta **New workspace**.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.fi.png)

4. Tee seuraavat toimenpiteet:

    - Valitse Azure-**Subscription**.
    - Valitse käytettävä **Resource group** (luo uusi tarvittaessa).
    - Syötä **Workspace Name**. Sen on oltava yksilöllinen.
    - Valitse käytettävä **Region**.
    - Valitse käytettävä **Storage account** (luo uusi tarvittaessa).
    - Valitse käytettävä **Key vault** (luo uusi tarvittaessa).
    - Valitse käytettävä **Application insights** (luo uusi tarvittaessa).
    - Valitse käytettävä **Container registry** (luo uusi tarvittaessa).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.fi.png)

5. Valitse **Review + Create**.

6. Valitse **Create**.

### Pyydä GPU-kiintiöt Azure-tilauksessa

Tässä opetusohjelmassa opit hienosäätämään ja ottamaan käyttöön Phi-3-mallin käyttäen GPU:ita. Hienosäätöön käytät *Standard_NC24ads_A100_v4* GPU:ta, johon tarvitaan kiintiöpyyntö. Käyttöönottoon käytät *Standard_NC6s_v3* GPU:ta, johon myös tarvitaan kiintiöpyyntö.

> [!NOTE]
>
> Vain Pay-As-You-Go -tilaukset (vakio-tilauksen tyyppi) ovat oikeutettuja GPU-resurssien käyttöön; etuustilaukset eivät tällä hetkellä ole tuettuja.
>

1. Siirry osoitteeseen [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Tee seuraavat toimenpiteet pyytääksesi *Standard NCADSA100v4 Family* -kiintiötä:

    - Valitse vasemman sivun välilehdeltä **Quota**.
    - Valitse käytettävä **Virtual machine family**. Esimerkiksi **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, joka sisältää *Standard_NC24ads_A100_v4* GPU:n.
    - Valitse navigointivalikosta **Request quota**.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.fi.png)

    - Syötä Request quota -sivulla haluamasi **New cores limit**, esimerkiksi 24.
    - Valitse Request quota -sivulla **Submit** pyytääksesi GPU-kiintiön.

1. Tee seuraavat toimenpiteet pyytääksesi *Standard NCSv3 Family* -kiintiötä:

    - Valitse vasemman sivun välilehdeltä **Quota**.
    - Valitse käytettävä **Virtual machine family**. Esimerkiksi **Standard NCSv3 Family Cluster Dedicated vCPUs**, joka sisältää *Standard_NC6s_v3* GPU:n.
    - Valitse navigointivalikosta **Request quota**.
    - Syötä Request quota -sivulla haluamasi **New cores limit**, esimerkiksi 24.
    - Valitse Request quota -sivulla **Submit** pyytääksesi GPU-kiintiön.

### Lisää roolimääritys

Malliesi hienosäätöä ja käyttöönottoa varten sinun on ensin luotava käyttäjän määrittämä hallittu identiteetti (User Assigned Managed Identity, UAI) ja annettava sille tarvittavat käyttöoikeudet. Tätä UAI:ta käytetään todennuksessa käyttöönoton aikana.

#### Luo User Assigned Managed Identity (UAI)

1. Kirjoita *managed identities* **hakupalkkiin** portaalin sivun yläosassa ja valitse ilmestyvistä vaihtoehdoista **Managed Identities**.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.fi.png)

1. Valitse **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.fi.png)

1. Tee seuraavat toimenpiteet:

    - Valitse Azure-**Subscription**.
    - Valitse käytettävä **Resource group** (luo uusi tarvittaessa).
    - Valitse käytettävä **Region**.
    - Syötä **Name**. Sen on oltava yksilöllinen.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.fi.png)

1. Valitse **Review + create**.

1. Valitse **+ Create**.

#### Lisää Contributor-roolimääritys hallitulle identiteetille

1. Siirry luomaasi Managed Identity -resurssiin.

1. Valitse vasemman sivun välilehdeltä **Azure role assignments**.

1. Valitse navigointivalikosta **+Add role assignment**.

1. Lisää roolimäärityksen sivulla tee seuraavat toimenpiteet:
    - Valitse **Scope**ksi **Resource group**.
    - Valitse Azure-**Subscription**.
    - Valitse käytettävä **Resource group**.
    - Valitse **Role**ksi **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.fi.png)

2. Valitse **Save**.

#### Lisää Storage Blob Data Reader -roolimääritys hallitulle identiteetille

1. Kirjoita *storage accounts* **hakupalkkiin** portaalin sivun yläosassa ja valitse ilmestyvistä vaihtoehdoista **Storage accounts**.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.fi.png)

1. Valitse tallennustili, joka liittyy luomaasi Azure Machine Learning -työtilaan. Esimerkiksi *finetunephistorage*.

1. Siirry Add role assignment -sivulle seuraavasti:

    - Siirry luomaasi Azure Storage -tiliin.
    - Valitse vasemman sivun välilehdeltä **Access Control (IAM)**.
    - Valitse navigointivalikosta **+ Add**.
    - Valitse navigointivalikosta **Add role assignment**.

    ![Add role.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.fi.png)

1. Lisää roolimäärityksessä tee seuraavat toimenpiteet:

    - Kirjoita roolisivun **hakupalkkiin** *Storage Blob Data Reader* ja valitse vaihtoehdoista **Storage Blob Data Reader**.
    - Valitse roolisivulla **Next**.
    - Jäsen-sivulla valitse **Assign access to** -kohdasta **Managed identity**.
    - Jäsen-sivulla valitse **+ Select members**.
    - Valitse Azure-**Subscription**.
    - Valitse **Managed identity**ksi **Manage Identity**.
    - Valitse luomasi hallittu identiteetti, esimerkiksi *finetunephi-managedidentity*.
    - Valitse **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.fi.png)

1. Valitse **Review + assign**.

#### Lisää AcrPull-roolimääritys hallitulle identiteetille

1. Kirjoita *container registries* **hakupalkkiin** portaalin sivun yläosassa ja valitse ilmestyvistä vaihtoehdoista **Container registries**.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.fi.png)

1. Valitse Azure Machine Learning -työtilaan liittyvä container registry, esimerkiksi *finetunephicontainerregistry*.

1. Siirry Add role assignment -sivulle seuraavasti:

    - Valitse vasemman sivun välilehdeltä **Access Control (IAM)**.
    - Valitse navigointivalikosta **+ Add**.
    - Valitse navigointivalikosta **Add role assignment**.

1. Lisää roolimäärityksessä tee seuraavat toimenpiteet:

    - Kirjoita roolisivun **hakupalkkiin** *AcrPull* ja valitse vaihtoehdoista **AcrPull**.
    - Valitse roolisivulla **Next**.
    - Jäsen-sivulla valitse **Assign access to** -kohdasta **Managed identity**.
    - Jäsen-sivulla valitse **+ Select members**.
    - Valitse Azure-**Subscription**.
    - Valitse **Managed identity**ksi **Manage Identity**.
    - Valitse luomasi hallittu identiteetti, esimerkiksi *finetunephi-managedidentity*.
    - Valitse **Select**.
    - Valitse **Review + assign**.

### Perusta projekti

Ladataksesi hienosäätöön tarvittavat aineistot, perustat paikallisen ympäristön.

Tässä harjoituksessa:

- Luo kansio, jossa työskentelet.
- Luo virtuaaliympäristö.
- Asenna tarvittavat paketit.
- Luo *download_dataset.py* -tiedosto aineiston lataamista varten.

#### Luo kansio työskentelyä varten

1. Avaa komentorivi ja kirjoita seuraava komento luodaksesi *finetune-phi* -nimisen kansion oletuspolkuun.

    ```console
    mkdir finetune-phi
    ```

2. Kirjoita komentoriville seuraava komento siirtyäksesi luomaasi *finetune-phi* -kansioon.

    ```console
    cd finetune-phi
    ```

#### Luo virtuaaliympäristö

1. Kirjoita komentoriville seuraava komento luodaksesi *.venv* -nimisen virtuaaliympäristön.

    ```console
    python -m venv .venv
    ```

2. Aktivoi virtuaaliympäristö kirjoittamalla komentoriville seuraava komento.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Jos aktivointi onnistui, komentokehotteessa näkyy *(.venv)*.

#### Asenna tarvittavat paketit

1. Asenna vaaditut paketit kirjoittamalla komentoriville seuraavat komennot.

    ```console
    pip install datasets==2.19.1
    ```

#### Luo `download_dataset.py`

> [!NOTE]
> Koko kansiorakenne:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Avaa **Visual Studio Code**.

1. Valitse valikkoriviltä **File**.

1. Valitse **Open Folder**.

1. Valitse luomasi *finetune-phi* -kansio, joka sijaitsee polussa *C:\Users\yourUserName\finetune-phi*.

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.fi.png)

1. Visual Studio Coden vasemmassa paneelissa napsauta hiiren oikealla ja valitse **New File** luodaksesi uuden tiedoston nimeltä *download_dataset.py*.

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.fi.png)

### Valmistele aineisto hienosäätöä varten

Tässä harjoituksessa suoritat *download_dataset.py* -tiedoston ladataksesi *ultrachat_200k* -aineistot paikalliseen ympäristöösi. Käytät tätä aineistoa Phi-3-mallin hienosäätöön Azure Machine Learningissä.

Harjoituksessa:

- Lisää koodi *download_dataset.py* -tiedostoon aineiston lataamista varten.
- Suorita *download_dataset.py* -tiedosto ladataksesi aineiston paikalliseen ympäristöön.

#### Lataa aineisto käyttämällä *download_dataset.py* -tiedostoa

1. Avaa *download_dataset.py* Visual Studio Codessa.

1. Lisää seuraava koodi tiedostoon.

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

1. Kirjoita komentoriville seuraava komento suorittaaksesi skriptin ja ladataksesi aineiston paikalliseen ympäristöön.

    ```console
    python download_dataset.py
    ```

1. Varmista, että aineistot tallentuivat onnistuneesti paikalliseen *finetune-phi/data* -hakemistoon.

> [!NOTE]
>
> #### Huomautus aineiston koosta ja hienosäätöajasta
>
> Tässä opetusohjelmassa käytät vain 1 % aineistosta (`split='train[:1%]'`). Tämä pienentää merkittävästi datamäärää, nopeuttaen sekä latausta että hienosäätöä. Voit säätää prosenttiosuutta löytääksesi sopivan tasapainon koulutusajan ja mallin suorituskyvyn välillä. Pienemmän osajoukon käyttö lyhentää hienosäätöön kuluvaa aikaa, mikä tekee prosessista helpommin hallittavan opetusohjelmassa.

## Skenaario 2: Phi-3-mallin hienosäätö ja käyttöönotto Azure Machine Learning Studiossa

### Hienosäädä Phi-3-malli

Tässä harjoituksessa hienosäädät
1. Siirry osoitteeseen [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Valitse vasemman puolen välilehdeltä **Compute**.

1. Valitse navigointivalikosta **Compute clusters**.

1. Valitse **+ New**.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.fi.png)

1. Suorita seuraavat toimenpiteet:

    - Valitse haluamasi **Region**.
    - Valitse **Virtual machine tier** arvoksi **Dedicated**.
    - Valitse **Virtual machine type** arvoksi **GPU**.
    - Valitse **Virtual machine size** suodattimeksi **Select from all options**.
    - Valitse **Virtual machine size** arvoksi **Standard_NC24ads_A100_v4**.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.fi.png)

1. Valitse **Next**.

1. Suorita seuraavat toimenpiteet:

    - Anna **Compute name**. Sen täytyy olla ainutlaatuinen.
    - Aseta **Minimum number of nodes** arvoksi **0**.
    - Aseta **Maximum number of nodes** arvoksi **1**.
    - Aseta **Idle seconds before scale down** arvoksi **120**.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.fi.png)

1. Valitse **Create**.

#### Hienosäädä Phi-3-malli

1. Siirry osoitteeseen [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Valitse luomasi Azure Machine Learning -työtila.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.fi.png)

1. Suorita seuraavat toimenpiteet:

    - Valitse vasemman puolen välilehdeltä **Model catalog**.
    - Kirjoita **hakupalkkiin** *phi-3-mini-4k* ja valitse vaihtoehdoista **Phi-3-mini-4k-instruct**.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.fi.png)

1. Valitse navigointivalikosta **Fine-tune**.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.fi.png)

1. Suorita seuraavat toimenpiteet:

    - Valitse **Select task type** arvoksi **Chat completion**.
    - Valitse **+ Select data** ladataksesi **Training data**.
    - Valitse validointidatan lataustavaksi **Provide different validation data**.
    - Valitse **+ Select data** ladataksesi **Validation data**.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.fi.png)

    > [!TIP]
    >
    > Voit valita **Advanced settings** mukauttaaksesi asetuksia, kuten **learning_rate** ja **lr_scheduler_type**, optimoidaksesi hienosäätöprosessia tarpeidesi mukaan.

1. Valitse **Finish**.

1. Tässä harjoituksessa hienosäädit Phi-3-mallin onnistuneesti Azure Machine Learningin avulla. Huomioithan, että hienosäätöprosessi voi kestää jonkin aikaa. Kun hienosäätötyö on käynnissä, sinun täytyy odottaa sen valmistumista. Voit seurata hienosäätötyön tilaa siirtymällä Azure Machine Learning -työtilasi vasemman puolen välilehdeltä **Jobs**-osioon. Seuraavassa osassa otat käyttöön hienosäädetyn mallin ja yhdistät sen Prompt flow -järjestelmään.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.fi.png)

### Ota käyttöön hienosäädetty Phi-3-malli

Jotta voit integroida hienosäädetyn Phi-3-mallin Prompt flow -järjestelmään ja tehdä siitä reaaliaikaisesti käytettävän, sinun tulee ottaa malli käyttöön. Tämä prosessi sisältää mallin rekisteröinnin, online-päätepisteen luomisen ja mallin käyttöönoton.

Tässä harjoituksessa teet seuraavaa:

- Rekisteröit hienosäädetyn mallin Azure Machine Learning -työtilaan.
- Luot online-päätepisteen.
- Otat käyttöön rekisteröidyn hienosäädetyn Phi-3-mallin.

#### Rekisteröi hienosäädetty malli

1. Siirry osoitteeseen [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Valitse luomasi Azure Machine Learning -työtila.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.fi.png)

1. Valitse vasemman puolen välilehdeltä **Models**.
1. Valitse **+ Register**.
1. Valitse **From a job output**.

    ![Register model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.fi.png)

1. Valitse luomasi työ.

    ![Select job.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.fi.png)

1. Valitse **Next**.

1. Valitse **Model type** arvoksi **MLflow**.

1. Varmista, että **Job output** on valittuna; sen pitäisi olla automaattisesti valittu.

    ![Select output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.fi.png)

2. Valitse **Next**.

3. Valitse **Register**.

    ![Select register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.fi.png)

4. Voit tarkastella rekisteröityä malliasi valitsemalla vasemman puolen välilehdeltä **Models**.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.fi.png)

#### Ota hienosäädetty malli käyttöön

1. Siirry luomaasi Azure Machine Learning -työtilaan.

1. Valitse vasemman puolen välilehdeltä **Endpoints**.

1. Valitse navigointivalikosta **Real-time endpoints**.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.fi.png)

1. Valitse **Create**.

1. Valitse luomasi rekisteröity malli.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.fi.png)

1. Valitse **Select**.

1. Suorita seuraavat toimenpiteet:

    - Valitse **Virtual machine** arvoksi *Standard_NC6s_v3*.
    - Valitse haluamasi **Instance count**, esimerkiksi *1*.
    - Valitse **Endpoint** arvoksi **New** luodaksesi uuden päätepisteen.
    - Anna **Endpoint name**. Sen täytyy olla ainutlaatuinen.
    - Anna **Deployment name**. Sen täytyy olla ainutlaatuinen.

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.fi.png)

1. Valitse **Deploy**.

> [!WARNING]
> Välttääksesi ylimääräiset maksut, muista poistaa luomasi päätepiste Azure Machine Learning -työtilasta, kun et enää tarvitse sitä.
>

#### Tarkista käyttöönoton tila Azure Machine Learning -työtilassa

1. Siirry luomaasi Azure Machine Learning -työtilaan.

1. Valitse vasemman puolen välilehdeltä **Endpoints**.

1. Valitse luomasi päätepiste.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.fi.png)

1. Tällä sivulla voit hallita päätepisteitä käyttöönoton aikana.

> [!NOTE]
> Kun käyttöönotto on valmis, varmista, että **Live traffic** on asetettu arvoon **100%**. Jos näin ei ole, valitse **Update traffic** säätääksesi liikenneasetuksia. Huomioithan, että mallia ei voi testata, jos liikenne on asetettu arvoon 0%.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.fi.png)
>

## Tapaus 3: Integroi Prompt flow -järjestelmään ja keskustele omalla mallillasi Azure AI Foundryssa

### Integroi oma Phi-3-malli Prompt flow -järjestelmään

Kun olet ottanut hienosäädetyn mallisi käyttöön, voit nyt yhdistää sen Prompt Flow'hun käyttääksesi malliasi reaaliaikaisissa sovelluksissa. Tämä mahdollistaa monipuoliset vuorovaikutteiset tehtävät omalla Phi-3-mallillasi.

Tässä harjoituksessa teet seuraavaa:

- Luo Azure AI Foundry Hub.
- Luo Azure AI Foundry Project.
- Luo Prompt flow.
- Lisää mukautettu yhteys hienosäädetylle Phi-3-mallille.
- Määritä Prompt flow keskustelemaan omalla Phi-3-mallillasi.

> [!NOTE]
> Voit myös integroida Promptflow'n käyttämällä Azure ML Studiota. Sama integraatioprosessi toimii myös Azure ML Studion kanssa.

#### Luo Azure AI Foundry Hub

Hub täytyy luoda ennen projektia. Hub toimii kuin resurssiryhmä, jonka avulla voit järjestellä ja hallita useita projekteja Azure AI Foundryssa.

1. Siirry osoitteeseen [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Valitse vasemman puolen välilehdeltä **All hubs**.

1. Valitse navigointivalikosta **+ New hub**.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.fi.png)

1. Suorita seuraavat toimenpiteet:

    - Anna **Hub name**. Sen täytyy olla ainutlaatuinen.
    - Valitse Azure-tilauksesi (**Subscription**).
    - Valitse käytettävä **Resource group** (luo tarvittaessa uusi).
    - Valitse haluamasi **Location**.
    - Valitse käytettävä **Connect Azure AI Services** (luo tarvittaessa uusi).
    - Valitse **Connect Azure AI Search** arvoksi **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.fi.png)

1. Valitse **Next**.

#### Luo Azure AI Foundry Project

1. Valitse luomassasi Hubissa vasemman puolen välilehdeltä **All projects**.

1. Valitse navigointivalikosta **+ New project**.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.fi.png)

1. Anna **Project name**. Sen täytyy olla ainutlaatuinen.

    ![Create project.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.fi.png)

1. Valitse **Create a project**.

#### Lisää mukautettu yhteys hienosäädetylle Phi-3-mallille

Jotta voit integroida oman Phi-3-mallisi Prompt flow'hun, sinun tulee tallentaa mallin päätepiste ja avain mukautettuun yhteyteen. Tämä varmistaa pääsyn omaan Phi-3-malliisi Prompt flow'ssa.

#### Aseta hienosäädetyn Phi-3-mallin api-avain ja päätepisteen URI

1. Siirry osoitteeseen [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Siirry luomaasi Azure Machine Learning -työtilaan.

1. Valitse vasemman puolen välilehdeltä **Endpoints**.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.fi.png)

1. Valitse luomasi päätepiste.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.fi.png)

1. Valitse navigointivalikosta **Consume**.

1. Kopioi **REST endpoint** ja **Primary key**.
![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.fi.png)

#### Lisää mukautettu yhteys

1. Siirry osoitteeseen [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Siirry luomaasi Azure AI Foundry -projektiin.

1. Valitse luomassasi projektissa vasemman puolen välilehdestä **Settings**.

1. Valitse **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.fi.png)

1. Valitse navigaatiovalikosta **Custom keys**.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.fi.png)

1. Suorita seuraavat toimenpiteet:

    - Valitse **+ Add key value pairs**.
    - Kirjoita avaimen nimeksi **endpoint** ja liitä Azure ML Studiosta kopioimasi endpoint arvokenttään.
    - Valitse uudelleen **+ Add key value pairs**.
    - Kirjoita avaimen nimeksi **key** ja liitä Azure ML Studiosta kopioimasi avain arvokenttään.
    - Avaimien lisäämisen jälkeen valitse **is secret** estääksesi avaimen paljastumisen.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.fi.png)

1. Valitse **Add connection**.

#### Luo Prompt flow

Olet lisännyt mukautetun yhteyden Azure AI Foundryssa. Luodaan nyt Prompt flow seuraavien ohjeiden mukaisesti. Tämän jälkeen yhdistät Prompt flown mukautettuun yhteyteen, jotta voit käyttää hienosäädettyä mallia Prompt flowssa.

1. Siirry luomaasi Azure AI Foundry -projektiin.

1. Valitse vasemman puolen välilehdestä **Prompt flow**.

1. Valitse navigaatiovalikosta **+ Create**.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.fi.png)

1. Valitse navigaatiovalikosta **Chat flow**.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.fi.png)

1. Kirjoita käytettävä **Folder name**.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.fi.png)

2. Valitse **Create**.

#### Määritä Prompt flow keskustelemaan mukautetun Phi-3 mallisi kanssa

Sinun täytyy integroida hienosäädetty Phi-3 malli Prompt flowhun. Kuitenkin olemassa oleva Prompt flow ei ole suunniteltu tätä tarkoitusta varten. Siksi sinun tulee suunnitella Prompt flow uudelleen, jotta mukautettu malli voidaan integroida.

1. Prompt flowssa tee seuraavat toimenpiteet olemassa olevan flown uudelleen rakentamiseksi:

    - Valitse **Raw file mode**.
    - Poista kaikki nykyinen koodi *flow.dag.yml* tiedostosta.
    - Lisää seuraava koodi *flow.dag.yml* tiedostoon.

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

    - Valitse **Save**.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.fi.png)

1. Lisää seuraava koodi *integrate_with_promptflow.py* tiedostoon käyttääksesi mukautettua Phi-3 mallia Prompt flowssa.

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.fi.png)

> [!NOTE]
> Lisätietoja Prompt flown käytöstä Azure AI Foundryssa löydät osoitteesta [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Valitse **Chat input**, **Chat output** ottaaksesi chat-toiminnon käyttöön mallisi kanssa.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.fi.png)

1. Nyt olet valmis keskustelemaan mukautetun Phi-3 mallisi kanssa. Seuraavassa harjoituksessa opit, miten käynnistät Prompt flown ja käytät sitä keskusteluun hienosäädetyn Phi-3 mallisi kanssa.

> [!NOTE]
>
> Uudelleen rakennettu flow näyttää tältä:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.fi.png)
>

### Keskustele mukautetun Phi-3 mallisi kanssa

Nyt kun olet hienosäätänyt ja integroinut mukautetun Phi-3 mallisi Prompt flowhin, olet valmis aloittamaan vuorovaikutuksen sen kanssa. Tämä harjoitus ohjaa sinut mallisi kanssa keskustelun aloittamisessa ja asetusten tekemisessä Prompt flown avulla. Näiden vaiheiden avulla voit hyödyntää hienosäädetyn Phi-3 mallisi kyvykkyyksiä monenlaisissa tehtävissä ja keskusteluissa.

- Keskustele mukautetun Phi-3 mallisi kanssa Prompt flown avulla.

#### Käynnistä Prompt flow

1. Valitse **Start compute sessions** käynnistääksesi Prompt flown.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.fi.png)

1. Valitse **Validate and parse input** päivittääksesi parametrit.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.fi.png)

1. Valitse **Value** kentästä **connection** luomasi mukautetun yhteyden arvo, esimerkiksi *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.fi.png)

#### Keskustele mukautetun mallisi kanssa

1. Valitse **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.fi.png)

1. Tässä esimerkki tuloksista: nyt voit keskustella mukautetun Phi-3 mallisi kanssa. Suositeltavaa on esittää kysymyksiä, jotka perustuvat hienosäädössä käytettyyn aineistoon.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.fi.png)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.