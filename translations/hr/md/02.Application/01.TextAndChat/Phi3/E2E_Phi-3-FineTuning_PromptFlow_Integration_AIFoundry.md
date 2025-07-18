<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-07-17T02:00:57+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "hr"
}
-->
# Fino podešavanje i integracija prilagođenih Phi-3 modela s Prompt flow u Azure AI Foundry

Ovaj end-to-end (E2E) primjer temelji se na vodiču "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" iz Microsoft Tech Community. Uvodi procese fino podešavanja, implementacije i integracije prilagođenih Phi-3 modela s Prompt flow u Azure AI Foundry.
Za razliku od E2E primjera, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", koji je uključivao lokalno pokretanje koda, ovaj vodič se u potpunosti fokusira na fino podešavanje i integraciju vašeg modela unutar Azure AI / ML Studija.

## Pregled

U ovom E2E primjeru naučit ćete kako fino podesiti Phi-3 model i integrirati ga s Prompt flow u Azure AI Foundry. Korištenjem Azure AI / ML Studija uspostavit ćete tijek rada za implementaciju i korištenje prilagođenih AI modela. Ovaj E2E primjer podijeljen je u tri scenarija:

**Scenarij 1: Postavljanje Azure resursa i priprema za fino podešavanje**

**Scenarij 2: Fino podešavanje Phi-3 modela i implementacija u Azure Machine Learning Studio**

**Scenarij 3: Integracija s Prompt flow i razgovor s vašim prilagođenim modelom u Azure AI Foundry**

Evo pregleda ovog E2E primjera.

![Phi-3-FineTuning_PromptFlow_Integration Pregled.](../../../../../../translated_images/00-01-architecture.198ba0f1ae6d841a2ceacdc6401c688bdf100d874fe8d55169f7723ed024781e.hr.png)

### Sadržaj

1. **[Scenarij 1: Postavljanje Azure resursa i priprema za fino podešavanje](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Kreiranje Azure Machine Learning Workspace-a](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Zahtjev za GPU kvote u Azure pretplati](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Dodavanje dodjele uloga](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Postavljanje projekta](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Priprema skupa podataka za fino podešavanje](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenarij 2: Fino podešavanje Phi-3 modela i implementacija u Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Fino podešavanje Phi-3 modela](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Implementacija fino podešenog Phi-3 modela](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenarij 3: Integracija s Prompt flow i razgovor s vašim prilagođenim modelom u Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integracija prilagođenog Phi-3 modela s Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Razgovor s vašim prilagođenim Phi-3 modelom](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenarij 1: Postavljanje Azure resursa i priprema za fino podešavanje

### Kreiranje Azure Machine Learning Workspace-a

1. Upišite *azure machine learning* u **tražilicu** na vrhu stranice portala i odaberite **Azure Machine Learning** iz ponuđenih opcija.

    ![Upišite azure machine learning.](../../../../../../translated_images/01-01-type-azml.acae6c5455e67b4b9780de8accc31e4e1de7254e9c34a7836a955d455339e77d.hr.png)

2. Odaberite **+ Create** iz navigacijskog izbornika.

3. Odaberite **New workspace** iz navigacijskog izbornika.

    ![Odaberite new workspace.](../../../../../../translated_images/01-02-select-new-workspace.cd09cd0ec4a60ef2cf04946c36873223099fd568e0c3ab0377c096868892fdda.hr.png)

4. Obavite sljedeće zadatke:

    - Odaberite svoju Azure **Pretplatu**.
    - Odaberite **Resource group** koju želite koristiti (ako je potrebno, kreirajte novu).
    - Unesite **Ime Workspace-a**. Mora biti jedinstvena vrijednost.
    - Odaberite **Regiju** koju želite koristiti.
    - Odaberite **Storage account** koji želite koristiti (ako je potrebno, kreirajte novi).
    - Odaberite **Key vault** koji želite koristiti (ako je potrebno, kreirajte novi).
    - Odaberite **Application insights** koji želite koristiti (ako je potrebno, kreirajte novi).
    - Odaberite **Container registry** koji želite koristiti (ako je potrebno, kreirajte novi).

    ![Ispunite azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.a1b6fd944be0090ff9ec341c724c1493e7f96726f5c810a89a7409b782a7b04a.hr.png)

5. Odaberite **Review + Create**.

6. Odaberite **Create**.

### Zahtjev za GPU kvote u Azure pretplati

U ovom vodiču naučit ćete kako fino podesiti i implementirati Phi-3 model koristeći GPU-ove. Za fino podešavanje koristit ćete *Standard_NC24ads_A100_v4* GPU, za koji je potreban zahtjev za kvotu. Za implementaciju koristit ćete *Standard_NC6s_v3* GPU, koji također zahtijeva zahtjev za kvotu.

> [!NOTE]
>
> Samo Pay-As-You-Go pretplate (standardni tip pretplate) imaju pravo na dodjelu GPU-a; pretplate s pogodnostima trenutno nisu podržane.
>

1. Posjetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Obavite sljedeće zadatke za zahtjev kvote *Standard NCADSA100v4 Family*:

    - Odaberite **Quota** s lijevog izbornika.
    - Odaberite **Virtual machine family** koju želite koristiti. Na primjer, odaberite **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, koja uključuje *Standard_NC24ads_A100_v4* GPU.
    - Odaberite **Request quota** iz navigacijskog izbornika.

        ![Zahtjev za kvotu.](../../../../../../translated_images/02-02-request-quota.c0428239a63ffdd536f2e4a305c8528a34914370813bc2cda4d7bbdd2de873f0.hr.png)

    - Na stranici Request quota unesite **New cores limit** koju želite koristiti. Na primjer, 24.
    - Na stranici Request quota odaberite **Submit** za podnošenje zahtjeva za GPU kvotu.

1. Obavite sljedeće zadatke za zahtjev kvote *Standard NCSv3 Family*:

    - Odaberite **Quota** s lijevog izbornika.
    - Odaberite **Virtual machine family** koju želite koristiti. Na primjer, odaberite **Standard NCSv3 Family Cluster Dedicated vCPUs**, koja uključuje *Standard_NC6s_v3* GPU.
    - Odaberite **Request quota** iz navigacijskog izbornika.
    - Na stranici Request quota unesite **New cores limit** koju želite koristiti. Na primjer, 24.
    - Na stranici Request quota odaberite **Submit** za podnošenje zahtjeva za GPU kvotu.

### Dodavanje dodjele uloga

Za fino podešavanje i implementaciju vaših modela, prvo morate kreirati User Assigned Managed Identity (UAI) i dodijeliti joj odgovarajuće dozvole. Ova UAI će se koristiti za autentifikaciju tijekom implementacije.

#### Kreiranje User Assigned Managed Identity (UAI)

1. Upišite *managed identities* u **tražilicu** na vrhu stranice portala i odaberite **Managed Identities** iz ponuđenih opcija.

    ![Upišite managed identities.](../../../../../../translated_images/03-01-type-managed-identities.24de763e0f1f37e52f52a152187b230243fe884f58a9940cd9b534db3dcea383.hr.png)

1. Odaberite **+ Create**.

    ![Odaberite create.](../../../../../../translated_images/03-02-select-create.92bf8989a5cd98f27b6680cd94ef6ec7557394022dafdcfba2a92777b11e4817.hr.png)

1. Obavite sljedeće zadatke:

    - Odaberite svoju Azure **Pretplatu**.
    - Odaberite **Resource group** koju želite koristiti (ako je potrebno, kreirajte novu).
    - Odaberite **Regiju** koju želite koristiti.
    - Unesite **Ime**. Mora biti jedinstvena vrijednost.

    ![Ispunite podatke za managed identities.](../../../../../../translated_images/03-03-fill-managed-identities-1.ef1d6a2261b449e0e313fffaecf7d6ce4ee5e86c0badcd038f03519cac63b76b.hr.png)

1. Odaberite **Review + create**.

1. Odaberite **+ Create**.

#### Dodavanje uloge Contributor Managed Identity

1. Idite na Managed Identity resurs koji ste kreirali.

1. Odaberite **Azure role assignments** s lijevog izbornika.

1. Odaberite **+Add role assignment** iz navigacijskog izbornika.

1. Na stranici Add role assignment obavite sljedeće zadatke:
    - Odaberite **Scope** na **Resource group**.
    - Odaberite svoju Azure **Pretplatu**.
    - Odaberite **Resource group** koju želite koristiti.
    - Odaberite **Role** na **Contributor**.

    ![Ispunite podatke za ulogu contributor.](../../../../../../translated_images/03-04-fill-contributor-role.73990bc6a32e140d1d62333e91b4d2719284f0dad14bd9b4c3459510a0c44fab.hr.png)

2. Odaberite **Save**.

#### Dodavanje uloge Storage Blob Data Reader Managed Identity

1. Upišite *storage accounts* u **tražilicu** na vrhu stranice portala i odaberite **Storage accounts** iz ponuđenih opcija.

    ![Upišite storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.9303de485e65e1e55b6b4dda10841d74d1c7463a2e4f23b9c45ffbb84219deb2.hr.png)

1. Odaberite storage account povezan s Azure Machine Learning workspace-om koji ste kreirali. Na primjer, *finetunephistorage*.

1. Obavite sljedeće zadatke za navigaciju do stranice Add role assignment:

    - Idite na Azure Storage account koji ste kreirali.
    - Odaberite **Access Control (IAM)** s lijevog izbornika.
    - Odaberite **+ Add** iz navigacijskog izbornika.
    - Odaberite **Add role assignment** iz navigacijskog izbornika.

    ![Dodajte ulogu.](../../../../../../translated_images/03-06-add-role.353ccbfdcf0789c25fb73e63b957e214a2b651375a640a3aa54159a3731f495b.hr.png)

1. Na stranici Add role assignment obavite sljedeće zadatke:

    - U polje za pretraživanje uloga upišite *Storage Blob Data Reader* i odaberite **Storage Blob Data Reader** iz ponuđenih opcija.
    - Odaberite **Next**.
    - Na stranici Members odaberite **Assign access to** **Managed identity**.
    - Odaberite **+ Select members**.
    - Na stranici Select managed identities odaberite svoju Azure **Pretplatu**.
    - Odaberite **Managed identity** na **Manage Identity**.
    - Odaberite Managed Identity koju ste kreirali. Na primjer, *finetunephi-managedidentity*.
    - Odaberite **Select**.

    ![Odaberite managed identity.](../../../../../../translated_images/03-08-select-managed-identity.e80a2aad5247eb25289f2f121da05d114934d21d26aae9cb779334cbbccdf9e8.hr.png)

1. Odaberite **Review + assign**.

#### Dodavanje uloge AcrPull Managed Identity

1. Upišite *container registries* u **tražilicu** na vrhu stranice portala i odaberite **Container registries** iz ponuđenih opcija.

    ![Upišite container registries.](../../../../../../translated_images/03-09-type-container-registries.7a4180eb2110e5a69b003f7a698dac908ffc2f355e675c10939fdd0bb09f790e.hr.png)

1. Odaberite container registry povezan s Azure Machine Learning workspace-om. Na primjer, *finetunephicontainerregistry*

1. Obavite sljedeće zadatke za navigaciju do stranice Add role assignment:

    - Odaberite **Access Control (IAM)** s lijevog izbornika.
    - Odaberite **+ Add** iz navigacijskog izbornika.
    - Odaberite **Add role assignment** iz navigacijskog izbornika.

1. Na stranici Add role assignment obavite sljedeće zadatke:

    - U polje za pretraživanje uloga upišite *AcrPull* i odaberite **AcrPull** iz ponuđenih opcija.
    - Odaberite **Next**.
    - Na stranici Members odaberite **Assign access to** **Managed identity**.
    - Odaberite **+ Select members**.
    - Na stranici Select managed identities odaberite svoju Azure **Pretplatu**.
    - Odaberite **Managed identity** na **Manage Identity**.
    - Odaberite Managed Identity koju ste kreirali. Na primjer, *finetunephi-managedidentity*.
    - Odaberite **Select**.
    - Odaberite **Review + assign**.

### Postavljanje projekta

Za preuzimanje skupova podataka potrebnih za fino podešavanje, postavit ćete lokalno okruženje.

U ovom zadatku ćete:

- Kreirati mapu u kojoj ćete raditi.
- Kreirati virtualno okruženje.
- Instalirati potrebne pakete.
- Kreirati datoteku *download_dataset.py* za preuzimanje skupa podataka.

#### Kreiranje mape u kojoj ćete raditi

1. Otvorite terminal i upišite sljedeću naredbu za kreiranje mape nazvane *finetune-phi* u zadanoj putanji.

    ```console
    mkdir finetune-phi
    ```

2. Upišite sljedeću naredbu u terminalu da biste ušli u mapu *finetune-phi* koju ste kreirali.
#### Kreirajte virtualno okruženje

1. Upišite sljedeću naredbu u terminal da biste kreirali virtualno okruženje pod nazivom *.venv*.

    ```console
    python -m venv .venv
    ```

2. Upišite sljedeću naredbu u terminal da biste aktivirali virtualno okruženje.

    ```console
    .venv\Scripts\activate.bat
    ```


> [!NOTE]
> Ako je uspjelo, trebali biste vidjeti *(.venv)* ispred prompta naredbe.

#### Instalirajte potrebne pakete

1. Upišite sljedeće naredbe u terminal da biste instalirali potrebne pakete.

    ```console
    pip install datasets==2.19.1
    ```

#### Kreirajte `download_dataset.py`

> [!NOTE]
> Kompletna struktura mape:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Otvorite **Visual Studio Code**.

1. Iz izbornika odaberite **File**.

1. Odaberite **Open Folder**.

1. Odaberite mapu *finetune-phi* koju ste kreirali, a nalazi se na putanji *C:\Users\yourUserName\finetune-phi*.

    ![Odaberite mapu koju ste kreirali.](../../../../../../translated_images/04-01-open-project-folder.f734374bcfd5f9e6f63a0a50961e51a39cc6de7a7ddc86da5f4896e815f28abd.hr.png)

1. U lijevom dijelu Visual Studio Code-a kliknite desnom tipkom i odaberite **New File** za kreiranje nove datoteke pod nazivom *download_dataset.py*.

    ![Kreirajte novu datoteku.](../../../../../../translated_images/04-02-create-new-file.cf9a330a3a9cff927ede875300e1b5c91ab90d1e486c77a43bb9494880cf9b6f.hr.png)

### Pripremite skup podataka za fino podešavanje

U ovom zadatku pokrenut ćete datoteku *download_dataset.py* kako biste preuzeli skupove podataka *ultrachat_200k* na lokalno računalo. Zatim ćete koristiti te skupove podataka za fino podešavanje Phi-3 modela u Azure Machine Learning.

U ovom zadatku ćete:

- Dodati kod u datoteku *download_dataset.py* za preuzimanje skupova podataka.
- Pokrenuti datoteku *download_dataset.py* kako biste preuzeli skupove podataka na lokalno računalo.

#### Preuzmite svoj skup podataka koristeći *download_dataset.py*

1. Otvorite datoteku *download_dataset.py* u Visual Studio Code-u.

1. Dodajte sljedeći kod u datoteku *download_dataset.py*.

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

1. Upišite sljedeću naredbu u terminal da biste pokrenuli skriptu i preuzeli skup podataka na lokalno računalo.

    ```console
    python download_dataset.py
    ```

1. Provjerite jesu li skupovi podataka uspješno spremljeni u lokalni direktorij *finetune-phi/data*.

> [!NOTE]
>
> #### Napomena o veličini skupa podataka i vremenu fino podešavanja
>
> U ovom vodiču koristite samo 1% skupa podataka (`split='train[:1%]'`). To značajno smanjuje količinu podataka, ubrzavajući prijenos i proces fino podešavanja. Možete prilagoditi postotak kako biste pronašli pravi balans između vremena treniranja i performansi modela. Korištenje manjeg dijela skupa podataka smanjuje vrijeme potrebno za fino podešavanje, što ovaj proces čini lakšim za praćenje u vodiču.

## Scenarij 2: Fino podesite Phi-3 model i implementirajte ga u Azure Machine Learning Studio

### Fino podesite Phi-3 model

U ovom zadatku fino ćete podesiti Phi-3 model u Azure Machine Learning Studio.

U ovom zadatku ćete:

- Kreirati računalni klaster za fino podešavanje.
- Fino podesiti Phi-3 model u Azure Machine Learning Studio.

#### Kreirajte računalni klaster za fino podešavanje

1. Posjetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. S lijevog izbornika odaberite **Compute**.

1. Iz navigacijskog izbornika odaberite **Compute clusters**.

1. Odaberite **+ New**.

    ![Odaberite compute.](../../../../../../translated_images/06-01-select-compute.a29cff290b480252d04ffd0142c073486df7d3b7256335964a98b87e28072523.hr.png)

1. Obavite sljedeće zadatke:

    - Odaberite **Region** koji želite koristiti.
    - Odaberite **Virtual machine tier** na **Dedicated**.
    - Odaberite **Virtual machine type** na **GPU**.
    - Filtrirajte **Virtual machine size** na **Select from all options**.
    - Odaberite **Virtual machine size** na **Standard_NC24ads_A100_v4**.

    ![Kreirajte klaster.](../../../../../../translated_images/06-02-create-cluster.f221b65ae1221d4e4baa9c5ccf86510f21df87515c231b2a255e1ee545496458.hr.png)

1. Odaberite **Next**.

1. Obavite sljedeće zadatke:

    - Unesite **Compute name**. Mora biti jedinstven.
    - Postavite **Minimum number of nodes** na **0**.
    - Postavite **Maximum number of nodes** na **1**.
    - Postavite **Idle seconds before scale down** na **120**.

    ![Kreirajte klaster.](../../../../../../translated_images/06-03-create-cluster.4a54ba20914f3662edc0f95ad364a869b4dbb7f7be08ff259528fea96312e77e.hr.png)

1. Odaberite **Create**.

#### Fino podesite Phi-3 model

1. Posjetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Odaberite Azure Machine Learning workspace koji ste kreirali.

    ![Odaberite workspace koji ste kreirali.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.hr.png)

1. Obavite sljedeće zadatke:

    - S lijevog izbornika odaberite **Model catalog**.
    - Upišite *phi-3-mini-4k* u **search bar** i odaberite **Phi-3-mini-4k-instruct** iz ponuđenih opcija.

    ![Upišite phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.8ab6d2a04418b25018a7e7353ce6525d8f5803b0af9bc9a60a9be4204dd77578.hr.png)

1. Iz navigacijskog izbornika odaberite **Fine-tune**.

    ![Odaberite fine tune.](../../../../../../translated_images/06-06-select-fine-tune.2918a59be55dfeecb897ac74882792b59086893b8a7448a89be3628aee62fc1b.hr.png)

1. Obavite sljedeće zadatke:

    - Odaberite **Select task type** na **Chat completion**.
    - Odaberite **+ Select data** za prijenos **Training data**.
    - Za vrstu prijenosa validacijskih podataka odaberite **Provide different validation data**.
    - Odaberite **+ Select data** za prijenos **Validation data**.

    ![Ispunite stranicu za fino podešavanje.](../../../../../../translated_images/06-07-fill-finetuning.b6d14c89e7c27d0bbc6b248af9e7369ca98379770badec9f73b6bced7a8b7806.hr.png)

    > [!TIP]
    >
    > Možete odabrati **Advanced settings** za prilagodbu postavki poput **learning_rate** i **lr_scheduler_type** kako biste optimizirali proces fino podešavanja prema vašim potrebama.

1. Odaberite **Finish**.

1. U ovom zadatku ste uspješno fino podesili Phi-3 model koristeći Azure Machine Learning. Imajte na umu da proces fino podešavanja može potrajati. Nakon pokretanja zadatka fino podešavanja, potrebno je pričekati da se završi. Status zadatka možete pratiti u kartici Jobs na lijevoj strani vašeg Azure Machine Learning Workspace-a. U sljedećem dijelu implementirat ćete fino podešeni model i integrirati ga s Prompt flow.

    ![Pogledajte zadatak fino podešavanja.](../../../../../../translated_images/06-08-output.2bd32e59930672b1cc1de86056e2fbc91e338f59e2a29d7dac86ede49a9714b2.hr.png)

### Implementirajte fino podešeni Phi-3 model

Da biste integrirali fino podešeni Phi-3 model s Prompt flow, potrebno je implementirati model kako bi bio dostupan za izvođenje u stvarnom vremenu. Ovaj proces uključuje registraciju modela, kreiranje online endpointa i implementaciju modela.

U ovom zadatku ćete:

- Registrirati fino podešeni model u Azure Machine Learning workspace-u.
- Kreirati online endpoint.
- Implementirati registrirani fino podešeni Phi-3 model.

#### Registrirajte fino podešeni model

1. Posjetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Odaberite Azure Machine Learning workspace koji ste kreirali.

    ![Odaberite workspace koji ste kreirali.](../../../../../../translated_images/06-04-select-workspace.a92934ac04f4f18133117ca7d6a6c6f03a6d9267dae544308b8df243835a21d0.hr.png)

1. S lijevog izbornika odaberite **Models**.
1. Odaberite **+ Register**.
1. Odaberite **From a job output**.

    ![Registrirajte model.](../../../../../../translated_images/07-01-register-model.ad1e7cc05e4b2777c8c39906ce5cd57f16b54fb3887dd4e4de1ce963b26499ad.hr.png)

1. Odaberite zadatak koji ste kreirali.

    ![Odaberite zadatak.](../../../../../../translated_images/07-02-select-job.3e2e1144cd6cd09315953b4eb2cc9d62d0d77ab0d9d877e34c6827fa6d2b6be4.hr.png)

1. Odaberite **Next**.

1. Odaberite **Model type** na **MLflow**.

1. Provjerite je li odabran **Job output**; trebao bi biti automatski odabran.

    ![Odaberite output.](../../../../../../translated_images/07-03-select-output.4cf1a0e645baea1f267b40f73de77f092a5b02808ade72f8eb94e5fe9723feb3.hr.png)

2. Odaberite **Next**.

3. Odaberite **Register**.

    ![Odaberite register.](../../../../../../translated_images/07-04-register.fd82a3b293060bc78399e613293032d3d301c02a6fd8092bec52bfaf4f3104de.hr.png)

4. Registrirani model možete vidjeti u izborniku **Models** s lijeve strane.

    ![Registrirani model.](../../../../../../translated_images/07-05-registered-model.7db9775f58dfd591b7995686b95396ffd8c185ba66f0a1f6be18f4aea05e93d5.hr.png)

#### Implementirajte fino podešeni model

1. Idite u Azure Machine Learning workspace koji ste kreirali.

1. S lijevog izbornika odaberite **Endpoints**.

1. Iz navigacijskog izbornika odaberite **Real-time endpoints**.

    ![Kreirajte endpoint.](../../../../../../translated_images/07-06-create-endpoint.1ba865c606551f09618ce29b467276523838b8cc766d79ebfecdb052fef2c4df.hr.png)

1. Odaberite **Create**.

1. Odaberite registrirani model koji ste kreirali.

    ![Odaberite registrirani model.](../../../../../../translated_images/07-07-select-registered-model.29c947c37fa30cb4460f7646dfaa59121fb1384ed1957755427d358462c25225.hr.png)

1. Odaberite **Select**.

1. Obavite sljedeće zadatke:

    - Odaberite **Virtual machine** na *Standard_NC6s_v3*.
    - Odaberite broj instanci koje želite koristiti, npr. *1*.
    - Odaberite **Endpoint** na **New** za kreiranje novog endpointa.
    - Unesite **Endpoint name**. Mora biti jedinstven.
    - Unesite **Deployment name**. Mora biti jedinstven.

    ![Ispunite postavke implementacije.](../../../../../../translated_images/07-08-deployment-setting.43ddc4209e67378494bb8d81418bc3bdaceb8c57151727d538594cb378697f36.hr.png)

1. Odaberite **Deploy**.

> [!WARNING]
> Kako biste izbjegli dodatne troškove, obavezno izbrišite kreirani endpoint u Azure Machine Learning workspace-u nakon korištenja.
>

#### Provjerite status implementacije u Azure Machine Learning Workspace-u

1. Idite u Azure Machine Learning workspace koji ste kreirali.

1. S lijevog izbornika odaberite **Endpoints**.

1. Odaberite endpoint koji ste kreirali.

    ![Odaberite endpoints](../../../../../../translated_images/07-09-check-deployment.325d18cae8475ef4a302f0efc8875002e1c382167083c7fefbdb42ede274d0da.hr.png)

1. Na ovoj stranici možete upravljati endpointima tijekom procesa implementacije.

> [!NOTE]
> Nakon što je implementacija završena, provjerite je li **Live traffic** postavljen na **100%**. Ako nije, odaberite **Update traffic** za prilagodbu postavki prometa. Imajte na umu da ne možete testirati model ako je promet postavljen na 0%.
>
> ![Postavite promet.](../../../../../../translated_images/07-10-set-traffic.085b847e5751ff3d30c64ecabac4b17a7b5dc004ba52ad387cbaaf7b266eeadf.hr.png)
>

## Scenarij 3: Integrirajte s Prompt flow i razgovarajte sa svojim prilagođenim modelom u Azure AI Foundry

### Integrirajte prilagođeni Phi-3 model s Prompt flow

Nakon što ste uspješno implementirali svoj fino podešeni model, sada ga možete integrirati s Prompt Flow kako biste koristili model u aplikacijama u stvarnom vremenu, omogućujući razne interaktivne zadatke s vašim prilagođenim Phi-3 modelom.

U ovom zadatku ćete:

- Kreirati Azure AI Foundry Hub.
- Kreirati Azure AI Foundry projekt.
- Kreirati Prompt flow.
- Dodati prilagođenu vezu za fino podešeni Phi-3 model.
- Postaviti Prompt flow za razgovor s vašim prilagođenim Phi-3 modelom.
> [!NOTE]
> Također se možete integrirati s Promptflow koristeći Azure ML Studio. Isti proces integracije može se primijeniti i na Azure ML Studio.
#### Kreirajte Azure AI Foundry Hub

Prije nego što kreirate Projekt, potrebno je napraviti Hub. Hub funkcionira kao Resource Group, omogućujući vam organizaciju i upravljanje više Projekata unutar Azure AI Foundry.

1. Posjetite [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Izaberite **All hubs** s lijevog izbornika.

1. Izaberite **+ New hub** iz navigacijskog izbornika.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.8f7dd615bb8d9834e092dcf9dda773276fbee65f40252ed4a9af4f9aa4fef5d7.hr.png)

1. Obavite sljedeće zadatke:

    - Unesite **Hub name**. Mora biti jedinstvena vrijednost.
    - Odaberite svoju Azure **Subscription**.
    - Odaberite **Resource group** koju želite koristiti (ako je potrebno, kreirajte novu).
    - Odaberite **Location** koju želite koristiti.
    - Odaberite **Connect Azure AI Services** koje želite koristiti (ako je potrebno, kreirajte nove).
    - Za **Connect Azure AI Search** odaberite **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.c2d3b505bbbdba7c44658a87c2ed01d9e588581f157480ff1ac3312085c51d25.hr.png)

1. Kliknite **Next**.

#### Kreirajte Azure AI Foundry Projekt

1. U Hubu koji ste kreirali, izaberite **All projects** s lijevog izbornika.

1. Izaberite **+ New project** iz navigacijskog izbornika.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.390fadfc9c8f8f1251c487d98aed0641bd057100b8e5d6fba9062bfb7d752ce9.hr.png)

1. Unesite **Project name**. Mora biti jedinstvena vrijednost.

    ![Create project.](../../../../../../translated_images/08-05-create-project.4d97f0372f03375a192b4ed3dde6b1136c860fc85352d612aa2f3ae8a4d54eb4.hr.png)

1. Kliknite **Create a project**.

#### Dodajte prilagođenu vezu za fino podešeni Phi-3 model

Da biste integrirali svoj prilagođeni Phi-3 model s Prompt flow, potrebno je spremiti endpoint i ključ modela u prilagođenu vezu. Ova postavka osigurava pristup vašem prilagođenom Phi-3 modelu unutar Prompt flow.

#### Postavite api ključ i endpoint uri fino podešenog Phi-3 modela

1. Posjetite [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Idite u Azure Machine learning workspace koji ste kreirali.

1. Izaberite **Endpoints** s lijevog izbornika.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.aff38d453bcf960519c1ac95116d1a7e5b8d0bdea5cd42281930766fbfad1929.hr.png)

1. Odaberite endpoint koji ste kreirali.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.47f0dc09df2e275ea16f689f59b70d5b0162fff1781204e389edcb63b42b95b2.hr.png)

1. Izaberite **Consume** iz navigacijskog izbornika.

1. Kopirajte svoj **REST endpoint** i **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.18f934b5953ae8cbe30a20b889154d04109bf17c5c09816060a8689933dc0fd7.hr.png)

#### Dodajte prilagođenu vezu

1. Posjetite [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Idite u Azure AI Foundry projekt koji ste kreirali.

1. U projektu koji ste kreirali, izaberite **Settings** s lijevog izbornika.

1. Izaberite **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.02eb45deadc401fc77130c3a16fbb8ee59407ecbf74fd3502cb8720c61384446.hr.png)

1. Izaberite **Custom keys** iz navigacijskog izbornika.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.856f6b29664605513ccc134f1adaefaf27f951981c511783a6a0d1118c9178a5.hr.png)

1. Obavite sljedeće zadatke:

    - Kliknite **+ Add key value pairs**.
    - Za naziv ključa unesite **endpoint** i zalijepite endpoint koji ste kopirali iz Azure ML Studija u polje za vrijednost.
    - Ponovno kliknite **+ Add key value pairs**.
    - Za naziv ključa unesite **key** i zalijepite ključ koji ste kopirali iz Azure ML Studija u polje za vrijednost.
    - Nakon dodavanja ključeva, označite **is secret** kako biste spriječili izlaganje ključa.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.785486badb4d2d26e8df1bbd0948e06aa20aa0dc102faa96c8144722ef7f0b72.hr.png)

1. Kliknite **Add connection**.

#### Kreirajte Prompt flow

Dodali ste prilagođenu vezu u Azure AI Foundry. Sada ćemo kreirati Prompt flow koristeći sljedeće korake. Nakon toga ćete povezati ovaj Prompt flow s prilagođenom vezom kako biste mogli koristiti fino podešeni model unutar Prompt flow.

1. Idite u Azure AI Foundry projekt koji ste kreirali.

1. Izaberite **Prompt flow** s lijevog izbornika.

1. Izaberite **+ Create** iz navigacijskog izbornika.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.6f4b451cb9821e5ba79bedfd35e2f2fb430f344844994375680fcfc111a994ae.hr.png)

1. Izaberite **Chat flow** iz navigacijskog izbornika.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.2ec689b22da32591f6cc6360bc35c8fca8d63519c09111c6c431de9b46eed143.hr.png)

1. Unesite **Folder name** koji želite koristiti.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.ff9520fefd89f40d824bad779a54e55d808a09394b6b730fbea55d78421f52ff.hr.png)

2. Kliknite **Create**.

#### Postavite Prompt flow za razgovor s vašim prilagođenim Phi-3 modelom

Potrebno je integrirati fino podešeni Phi-3 model u Prompt flow. Međutim, postojeći Prompt flow nije dizajniran za ovu svrhu. Stoga morate redizajnirati Prompt flow kako biste omogućili integraciju prilagođenog modela.

1. U Prompt flow-u obavite sljedeće zadatke za rekonstrukciju postojećeg toka:

    - Odaberite **Raw file mode**.
    - Izbrišite sav postojeći kod u datoteci *flow.dag.yml*.
    - Dodajte sljedeći kod u datoteku *flow.dag.yml*.

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

    - Kliknite **Save**.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.61d988b41df28985b76e070bf170e1d0d0d26b38d93bc635624642191f715a6d.hr.png)

1. Dodajte sljedeći kod u datoteku *integrate_with_promptflow.py* kako biste koristili prilagođeni Phi-3 model u Prompt flow.

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.a6041b74a7d097779ab1c429be9fc07e3f4171e41fbbfb747a6e755816411e6d.hr.png)

> [!NOTE]
> Za detaljnije informacije o korištenju Prompt flow u Azure AI Foundry, možete pogledati [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Odaberite **Chat input**, **Chat output** kako biste omogućili razgovor s vašim modelom.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.64dbb39bbe59d03ba022a21159e51d544c6e063e73c10e772c942d4e44da0d30.hr.png)

1. Sada ste spremni za razgovor s vašim prilagođenim Phi-3 modelom. U sljedećoj vježbi naučit ćete kako pokrenuti Prompt flow i koristiti ga za razgovor s vašim fino podešenim Phi-3 modelom.

> [!NOTE]
>
> Rekonstruirani tok trebao bi izgledati kao na slici ispod:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.d6457533952e690c10b7375192511a8e2aba847e442b294a2e65d88ffac8f63b.hr.png)
>

### Razgovarajte s vašim prilagođenim Phi-3 modelom

Sada kada ste fino podesili i integrirali svoj prilagođeni Phi-3 model s Prompt flow, spremni ste za interakciju s njim. Ova vježba će vas provesti kroz proces postavljanja i pokretanja razgovora s vašim modelom koristeći Prompt flow. Slijedeći ove korake, moći ćete u potpunosti iskoristiti mogućnosti vašeg fino podešenog Phi-3 modela za razne zadatke i razgovore.

- Razgovarajte s vašim prilagođenim Phi-3 modelom koristeći Prompt flow.

#### Pokrenite Prompt flow

1. Kliknite **Start compute sessions** za pokretanje Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.a86fcf5be68e386b4809b60d75ce9b0ad53e0729cc1449935ccbe90b954401dc.hr.png)

1. Kliknite **Validate and parse input** za osvježavanje parametara.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.317c76ef766361e97038d7529b9060a23dc59d7ddbeb38ac9c4562ef4f5b32f7.hr.png)

1. Odaberite **Value** za **connection** na prilagođenu vezu koju ste kreirali. Na primjer, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.99bdddb4b184402368a6ec383814b139686118331a5b2eefa489678902269dfc.hr.png)

#### Razgovarajte s vašim prilagođenim modelom

1. Kliknite **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.61936dce6612a1e636a5e1516b6c64fdf2345ceb3142db2bed93ab7e6f03bbb2.hr.png)

1. Evo primjera rezultata: sada možete razgovarati s vašim prilagođenim Phi-3 modelom. Preporučuje se postavljati pitanja temeljena na podacima korištenim za fino podešavanje.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.c8ca404c07ab126fa4886e6fd0e7482cfdc6c907fa36f7f2f13d04126f9eda14.hr.png)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.