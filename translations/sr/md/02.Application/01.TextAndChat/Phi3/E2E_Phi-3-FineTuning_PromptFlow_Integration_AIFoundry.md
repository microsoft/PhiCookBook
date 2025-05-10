<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-09T18:26:23+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "sr"
}
-->
# Fino podešavanje i integracija prilagođenih Phi-3 modela sa Prompt flow u Azure AI Foundry

Ovaj end-to-end (E2E) primer zasnovan je na vodiču "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" sa Microsoft Tech Community. Upoznaje vas sa procesima fino podešavanja, implementacije i integracije prilagođenih Phi-3 modela sa Prompt flow u Azure AI Foundry.
Za razliku od E2E primera "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", koji je uključivao lokalno pokretanje koda, ovaj tutorijal se u potpunosti fokusira na fino podešavanje i integraciju vašeg modela unutar Azure AI / ML Studija.

## Pregled

U ovom E2E primeru naučićete kako da fino podesite Phi-3 model i integrišete ga sa Prompt flow u Azure AI Foundry. Korišćenjem Azure AI / ML Studija, uspostavićete tok rada za implementaciju i korišćenje prilagođenih AI modela. Ovaj E2E primer je podeljen u tri scenarija:

**Scenario 1: Postavljanje Azure resursa i priprema za fino podešavanje**

**Scenario 2: Fino podešavanje Phi-3 modela i implementacija u Azure Machine Learning Studio**

**Scenario 3: Integracija sa Prompt flow i razgovor sa vašim prilagođenim modelom u Azure AI Foundry**

Evo pregleda ovog E2E primera.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.sr.png)

### Sadržaj

1. **[Scenario 1: Postavljanje Azure resursa i priprema za fino podešavanje](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Kreiranje Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Zahtev za GPU kvote u Azure pretplati](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Dodavanje dodeljivanja uloge](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Postavljanje projekta](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Priprema skupa podataka za fino podešavanje](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 2: Fino podešavanje Phi-3 modela i implementacija u Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Fino podešavanje Phi-3 modela](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Implementacija fino podešenog Phi-3 modela](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 3: Integracija sa Prompt flow i razgovor sa vašim prilagođenim modelom u Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integracija prilagođenog Phi-3 modela sa Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Razgovor sa vašim prilagođenim Phi-3 modelom](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenario 1: Postavljanje Azure resursa i priprema za fino podešavanje

### Kreiranje Azure Machine Learning Workspace

1. Upišite *azure machine learning* u **traku za pretragu** na vrhu portala i izaberite **Azure Machine Learning** iz ponuđenih opcija.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.sr.png)

2. Izaberite **+ Create** iz navigacionog menija.

3. Izaberite **New workspace** iz navigacionog menija.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.sr.png)

4. Izvršite sledeće zadatke:

    - Izaberite vašu Azure **Subscription**.
    - Izaberite **Resource group** koju ćete koristiti (napravite novu ako je potrebno).
    - Unesite **Workspace Name**. Mora biti jedinstvena vrednost.
    - Izaberite **Region** koju želite da koristite.
    - Izaberite **Storage account** koji ćete koristiti (napravite novi ako je potrebno).
    - Izaberite **Key vault** koji ćete koristiti (napravite novi ako je potrebno).
    - Izaberite **Application insights** koji ćete koristiti (napravite novi ako je potrebno).
    - Izaberite **Container registry** koji ćete koristiti (napravite novi ako je potrebno).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.sr.png)

5. Izaberite **Review + Create**.

6. Izaberite **Create**.

### Zahtev za GPU kvote u Azure pretplati

U ovom tutorijalu naučićete kako da fino podesite i implementirate Phi-3 model koristeći GPU-ove. Za fino podešavanje koristićete *Standard_NC24ads_A100_v4* GPU, za koji je potrebno podneti zahtev za kvotu. Za implementaciju koristićete *Standard_NC6s_v3* GPU, za koji je takođe potreban zahtev za kvotu.

> [!NOTE]
>
> Samo Pay-As-You-Go pretplate (standardni tip pretplate) su podobne za dodelu GPU resursa; pretplate sa benefitima trenutno nisu podržane.
>

1. Posetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Izvršite sledeće korake da zatražite *Standard NCADSA100v4 Family* kvotu:

    - Izaberite **Quota** sa leve strane.
    - Izaberite **Virtual machine family** koju želite da koristite. Na primer, izaberite **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, koji uključuje *Standard_NC24ads_A100_v4* GPU.
    - Izaberite **Request quota** iz navigacionog menija.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.sr.png)

    - Na stranici za zahtev kvote unesite **New cores limit** koju želite da koristite. Na primer, 24.
    - Na stranici za zahtev kvote izaberite **Submit** da podnesete zahtev za GPU kvotu.

1. Izvršite sledeće korake da zatražite *Standard NCSv3 Family* kvotu:

    - Izaberite **Quota** sa leve strane.
    - Izaberite **Virtual machine family** koju želite da koristite. Na primer, izaberite **Standard NCSv3 Family Cluster Dedicated vCPUs**, koji uključuje *Standard_NC6s_v3* GPU.
    - Izaberite **Request quota** iz navigacionog menija.
    - Na stranici za zahtev kvote unesite **New cores limit** koju želite da koristite. Na primer, 24.
    - Na stranici za zahtev kvote izaberite **Submit** da podnesete zahtev za GPU kvotu.

### Dodavanje dodeljivanja uloge

Da biste fino podesili i implementirali vaše modele, prvo morate kreirati User Assigned Managed Identity (UAI) i dodeliti joj odgovarajuće dozvole. Ova UAI će se koristiti za autentifikaciju tokom implementacije.

#### Kreiranje User Assigned Managed Identity (UAI)

1. Upišite *managed identities* u **traku za pretragu** na vrhu portala i izaberite **Managed Identities** iz ponuđenih opcija.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.sr.png)

1. Izaberite **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.sr.png)

1. Izvršite sledeće zadatke:

    - Izaberite vašu Azure **Subscription**.
    - Izaberite **Resource group** koju ćete koristiti (napravite novu ako je potrebno).
    - Izaberite **Region** koju želite da koristite.
    - Unesite **Name**. Mora biti jedinstvena vrednost.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.sr.png)

1. Izaberite **Review + create**.

1. Izaberite **+ Create**.

#### Dodavanje Contributor uloge Managed Identity

1. Idite na Managed Identity resurs koji ste kreirali.

1. Izaberite **Azure role assignments** sa leve strane.

1. Izaberite **+Add role assignment** iz navigacionog menija.

1. Na stranici za dodavanje uloge, izvršite sledeće:

    - Izaberite **Scope** na **Resource group**.
    - Izaberite vašu Azure **Subscription**.
    - Izaberite **Resource group** koju koristite.
    - Izaberite **Role** na **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.sr.png)

2. Izaberite **Save**.

#### Dodavanje Storage Blob Data Reader uloge Managed Identity

1. Upišite *storage accounts* u **traku za pretragu** na vrhu portala i izaberite **Storage accounts** iz ponuđenih opcija.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.sr.png)

1. Izaberite storage account povezan sa Azure Machine Learning workspace koji ste kreirali. Na primer, *finetunephistorage*.

1. Izvršite sledeće da biste stigli do stranice za dodavanje uloge:

    - Idite na Azure Storage account koji ste kreirali.
    - Izaberite **Access Control (IAM)** sa leve strane.
    - Izaberite **+ Add** iz navigacionog menija.
    - Izaberite **Add role assignment** iz navigacionog menija.

    ![Add role.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.sr.png)

1. Na stranici za dodavanje uloge, izvršite sledeće:

    - U polje za pretragu ulogu upišite *Storage Blob Data Reader* i izaberite **Storage Blob Data Reader** iz ponuđenih opcija.
    - Izaberite **Next**.
    - Na stranici za članove izaberite **Assign access to** na **Managed identity**.
    - Izaberite **+ Select members**.
    - Izaberite vašu Azure **Subscription**.
    - Izaberite **Managed identity** na **Manage Identity**.
    - Izaberite Managed Identity koju ste kreirali. Na primer, *finetunephi-managedidentity*.
    - Izaberite **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.sr.png)

1. Izaberite **Review + assign**.

#### Dodavanje AcrPull uloge Managed Identity

1. Upišite *container registries* u **traku za pretragu** na vrhu portala i izaberite **Container registries** iz ponuđenih opcija.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.sr.png)

1. Izaberite container registry povezan sa Azure Machine Learning workspace. Na primer, *finetunephicontainerregistry*.

1. Izvršite sledeće da biste stigli do stranice za dodavanje uloge:

    - Izaberite **Access Control (IAM)** sa leve strane.
    - Izaberite **+ Add** iz navigacionog menija.
    - Izaberite **Add role assignment** iz navigacionog menija.

1. Na stranici za dodavanje uloge, izvršite sledeće:

    - U polje za pretragu upišite *AcrPull* i izaberite **AcrPull** iz ponuđenih opcija.
    - Izaberite **Next**.
    - Na stranici za članove izaberite **Assign access to** na **Managed identity**.
    - Izaberite **+ Select members**.
    - Izaberite vašu Azure **Subscription**.
    - Izaberite **Managed identity** na **Manage Identity**.
    - Izaberite Managed Identity koju ste kreirali. Na primer, *finetunephi-managedidentity*.
    - Izaberite **Select**.
    - Izaberite **Review + assign**.

### Postavljanje projekta

Da biste preuzeli skupove podataka potrebne za fino podešavanje, postavićete lokalno okruženje.

U ovom zadatku ćete:

- Kreirati folder u kojem ćete raditi.
- Kreirati virtuelno okruženje.
- Instalirati potrebne pakete.
- Kreirati fajl *download_dataset.py* za preuzimanje skupa podataka.

#### Kreiranje foldera za rad

1. Otvorite terminal i otkucajte sledeću komandu da kreirate folder pod nazivom *finetune-phi* u podrazumevanoj putanji.

    ```console
    mkdir finetune-phi
    ```

2. U terminalu otkucajte sledeću komandu da uđete u folder *finetune-phi* koji ste kreirali.

    ```console
    cd finetune-phi
    ```

#### Kreiranje virtuelnog okruženja

1. U terminalu otkucajte sledeću komandu da kreirate virtuelno okruženje pod nazivom *.venv*.

    ```console
    python -m venv .venv
    ```

2. U terminalu otkucajte sledeću komandu da aktivirate virtuelno okruženje.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Ako je uspešno, trebalo bi da vidite *(.venv)* ispred komandne linije.

#### Instalacija potrebnih paketa

1. U terminalu otkucajte sledeće komande da instalirate potrebne pakete.

    ```console
    pip install datasets==2.19.1
    ```

#### Kreiranje `download_dataset.py`

> [!NOTE]
> Kompletna struktura foldera:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Otvorite **Visual Studio Code**.

1. Izaberite **File** iz menija.

1. Izaberite **Open Folder**.

1. Izaberite folder *finetune-phi* koji ste kreirali, koji se nalazi na putanji *C:\Users\yourUserName\finetune-phi*.

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.sr.png)

1. U levom delu Visual Studio Code, kliknite desnim tasterom i izaberite **New File** da kreirate novi fajl pod nazivom *download_dataset.py*.

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.sr.png)

### Priprema skupa podataka za fino podešavanje

U ovom zadatku pokrenućete fajl *download_dataset.py* da preuzmete *ultrachat_200k* skupove podataka u vaše lokalno okruženje. Nakon toga ćete koristiti ove skupove podataka za fino podešavanje Phi-3 modela u Azure Machine Learning.

U ovom zadatku ćete:

- Dodati kod u fajl *download_dataset.py* za preuzimanje skupova podataka.
- Pokrenuti fajl *download_dataset.py* da preuzmete skupove podataka u lokalno okruženje.

#### Preuzimanje skupa podataka pomoću *download_dataset.py*

1. Otvorite fajl *download_dataset.py* u Visual Studio Code.

1. Dodajte sledeći kod u fajl *download_dataset.py*.

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

1. U terminalu otkucajte sledeću komandu da pokrenete skriptu i preuzmete skup podataka u lokalno okruženje.

    ```console
    python download_dataset.py
    ```

1. Proverite da li su skupovi podataka uspešno sačuvani u lokalnom direktorijumu *finetune-phi/data*.

> [!NOTE]
>
> #### Napomena o veličini skupa podataka i vremenu fino podešavanja
>
> U ovom tutorijalu koristite samo 1% skupa podataka (`split='train[:1%]'`). Ovo značajno smanjuje količinu podataka, ubrzavajući i proces otpremanja i fino podešavanja. Možete prilagoditi procenat da pronađete pravi balans između vremena treniranja i performansi modela. Korišćenje manjeg dela skupa podataka smanjuje vreme potrebno za fino podešavanje, čineći proces lakšim za tutorijal.

## Scenario 2: Fino podešavanje Phi-3 modela i implementacija u Azure Machine Learning Studio

### Fino podešavanje Phi-3 modela

U ovom zadatku fino ćete podesiti Phi-3 model u Azure Machine Learning Studio.

U ovom zadatku ćete:

- Kreirati računski klaster za fino podešavanje.
- Fino podesiti Phi-3 model u Azure Machine Learning Studio.

#### Kreiranje računskog klastera za fino podešavanje
1. Posetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Izaberite **Compute** sa leve strane taba.

1. Izaberite **Compute clusters** iz navigacionog menija.

1. Izaberite **+ New**.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.sr.png)

1. Uradite sledeće:

    - Izaberite **Region** koji želite da koristite.
    - Izaberite **Virtual machine tier** na **Dedicated**.
    - Izaberite **Virtual machine type** na **GPU**.
    - Izaberite filter za **Virtual machine size** na **Select from all options**.
    - Izaberite **Virtual machine size** na **Standard_NC24ads_A100_v4**.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.sr.png)

1. Izaberite **Next**.

1. Uradite sledeće:

    - Unesite **Compute name**. Mora biti jedinstvena vrednost.
    - Izaberite **Minimum number of nodes** na **0**.
    - Izaberite **Maximum number of nodes** na **1**.
    - Izaberite **Idle seconds before scale down** na **120**.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.sr.png)

1. Izaberite **Create**.

#### Fino podešavanje Phi-3 modela

1. Posetite ponovo [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Izaberite Azure Machine Learning workspace koji ste kreirali.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.sr.png)

1. Uradite sledeće:

    - Izaberite **Model catalog** sa leve strane taba.
    - Ukucajte *phi-3-mini-4k* u **search bar** i izaberite **Phi-3-mini-4k-instruct** iz ponuđenih opcija.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.sr.png)

1. Izaberite **Fine-tune** iz navigacionog menija.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.sr.png)

1. Uradite sledeće:

    - Izaberite **Select task type** na **Chat completion**.
    - Izaberite **+ Select data** da otpremite **Training data**.
    - Izaberite tip otpremanja Validation podataka na **Provide different validation data**.
    - Izaberite **+ Select data** da otpremite **Validation data**.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.sr.png)

    > [!TIP]
    >
    > Možete izabrati **Advanced settings** da prilagodite podešavanja kao što su **learning_rate** i **lr_scheduler_type** kako biste optimizovali proces fino podešavanja prema vašim potrebama.

1. Izaberite **Finish**.

1. U ovoj vežbi ste uspešno fino podesili Phi-3 model koristeći Azure Machine Learning. Imajte na umu da proces fino podešavanja može potrajati. Nakon pokretanja posla za fino podešavanje, potrebno je sačekati da se završi. Status posla možete pratiti u tabu Jobs sa leve strane u vašem Azure Machine Learning Workspace-u. U narednom delu ćete postaviti fino podešeni model i integrisati ga sa Prompt flow.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.sr.png)

### Postavljanje fino podešenog Phi-3 modela

Da biste integrisali fino podešeni Phi-3 model sa Prompt flow, potrebno je da postavite model kako bi bio dostupan za real-time inferencu. Ovaj proces uključuje registraciju modela, kreiranje online endpoint-a i postavljanje modela.

U ovoj vežbi ćete:

- Registrovati fino podešeni model u Azure Machine Learning workspace-u.
- Kreirati online endpoint.
- Postaviti registrovani fino podešeni Phi-3 model.

#### Registracija fino podešenog modela

1. Posetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Izaberite Azure Machine Learning workspace koji ste kreirali.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.sr.png)

1. Izaberite **Models** sa leve strane taba.
1. Izaberite **+ Register**.
1. Izaberite **From a job output**.

    ![Register model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.sr.png)

1. Izaberite posao koji ste kreirali.

    ![Select job.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.sr.png)

1. Izaberite **Next**.

1. Izaberite **Model type** na **MLflow**.

1. Proverite da je **Job output** izabran; trebalo bi da bude automatski izabran.

    ![Select output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.sr.png)

2. Izaberite **Next**.

3. Izaberite **Register**.

    ![Select register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.sr.png)

4. Registrovani model možete videti u meniju **Models** sa leve strane taba.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.sr.png)

#### Postavljanje fino podešenog modela

1. Idite u Azure Machine Learning workspace koji ste kreirali.

1. Izaberite **Endpoints** sa leve strane taba.

1. Izaberite **Real-time endpoints** iz navigacionog menija.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.sr.png)

1. Izaberite **Create**.

1. Izaberite registrovani model koji ste kreirali.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.sr.png)

1. Izaberite **Select**.

1. Uradite sledeće:

    - Izaberite **Virtual machine** na *Standard_NC6s_v3*.
    - Izaberite broj instanci koje želite da koristite. Na primer, *1*.
    - Izaberite **Endpoint** na **New** da kreirate novi endpoint.
    - Unesite **Endpoint name**. Mora biti jedinstvena vrednost.
    - Unesite **Deployment name**. Mora biti jedinstvena vrednost.

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.sr.png)

1. Izaberite **Deploy**.

> [!WARNING]
> Da biste izbegli dodatne troškove, obavezno obrišite kreirani endpoint u Azure Machine Learning workspace-u kada vam više nije potreban.
>

#### Provera statusa postavljanja u Azure Machine Learning Workspace-u

1. Idite u Azure Machine Learning workspace koji ste kreirali.

1. Izaberite **Endpoints** sa leve strane taba.

1. Izaberite endpoint koji ste kreirali.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.sr.png)

1. Na ovoj stranici možete upravljati endpoint-ima tokom procesa postavljanja.

> [!NOTE]
> Kada postavljanje bude završeno, proverite da je **Live traffic** podešen na **100%**. Ako nije, izaberite **Update traffic** da prilagodite saobraćaj. Ne možete testirati model ako je saobraćaj podešen na 0%.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.sr.png)
>

## Scenario 3: Integracija sa Prompt flow i razgovor sa vašim prilagođenim modelom u Azure AI Foundry

### Integracija prilagođenog Phi-3 modela sa Prompt flow

Nakon uspešnog postavljanja fino podešenog modela, sada ga možete integrisati sa Prompt Flow kako biste koristili model u real-time aplikacijama, omogućavajući različite interaktivne zadatke sa vašim prilagođenim Phi-3 modelom.

U ovoj vežbi ćete:

- Kreirati Azure AI Foundry Hub.
- Kreirati Azure AI Foundry Projekat.
- Kreirati Prompt flow.
- Dodati prilagođenu konekciju za fino podešeni Phi-3 model.
- Podesiti Prompt flow za razgovor sa vašim prilagođenim Phi-3 modelom.

> [!NOTE]
> Takođe možete integrisati sa Promptflow koristeći Azure ML Studio. Isti proces integracije važi i za Azure ML Studio.

#### Kreiranje Azure AI Foundry Hub-a

Pre nego što kreirate Projekat, potrebno je da kreirate Hub. Hub funkcioniše kao Resource Group, omogućavajući organizaciju i upravljanje više Projekata unutar Azure AI Foundry.

1. Posetite [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Izaberite **All hubs** sa leve strane taba.

1. Izaberite **+ New hub** iz navigacionog menija.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.sr.png)

1. Uradite sledeće:

    - Unesite **Hub name**. Mora biti jedinstvena vrednost.
    - Izaberite vašu Azure **Subscription**.
    - Izaberite **Resource group** koju želite da koristite (kreirajte novu ako je potrebno).
    - Izaberite **Location** koju želite da koristite.
    - Izaberite **Connect Azure AI Services** (kreirajte novu ako je potrebno).
    - Izaberite **Connect Azure AI Search** na **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.sr.png)

1. Izaberite **Next**.

#### Kreiranje Azure AI Foundry Projekta

1. U Hub-u koji ste kreirali, izaberite **All projects** sa leve strane taba.

1. Izaberite **+ New project** iz navigacionog menija.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.sr.png)

1. Unesite **Project name**. Mora biti jedinstvena vrednost.

    ![Create project.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.sr.png)

1. Izaberite **Create a project**.

#### Dodavanje prilagođene konekcije za fino podešeni Phi-3 model

Da biste integrisali vaš prilagođeni Phi-3 model sa Prompt flow, potrebno je da sačuvate endpoint i ključ modela u prilagođenoj konekciji. Ovo omogućava pristup vašem prilagođenom Phi-3 modelu u Prompt flow-u.

#### Podesite api ključ i endpoint URI fino podešenog Phi-3 modela

1. Posetite [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Idite u Azure Machine Learning workspace koji ste kreirali.

1. Izaberite **Endpoints** sa leve strane taba.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.sr.png)

1. Izaberite endpoint koji ste kreirali.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.sr.png)

1. Izaberite **Consume** iz navigacionog menija.

1. Kopirajte vaš **REST endpoint** i **Primary key**.
![Copy api key and endpoint uri.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.sr.png)

#### Dodajte prilagođenu konekciju

1. Posetite [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Idite do Azure AI Foundry projekta koji ste kreirali.

1. U projektu koji ste napravili, izaberite **Settings** sa leve strane.

1. Izaberite **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.sr.png)

1. Izaberite **Custom keys** iz navigacionog menija.

    ![Select custom keys.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.sr.png)

1. Uradite sledeće:

    - Izaberite **+ Add key value pairs**.
    - Za ime ključa unesite **endpoint** i nalepite endpoint koji ste kopirali iz Azure ML Studija u polje za vrednost.
    - Ponovo izaberite **+ Add key value pairs**.
    - Za ime ključa unesite **key** i nalepite ključ koji ste kopirali iz Azure ML Studija u polje za vrednost.
    - Nakon dodavanja ključeva, označite **is secret** da biste sprečili da ključ bude vidljiv.

    ![Add connection.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.sr.png)

1. Izaberite **Add connection**.

#### Kreirajte Prompt flow

Dodali ste prilagođenu konekciju u Azure AI Foundry. Sada ćemo kreirati Prompt flow koristeći sledeće korake. Nakon toga povezaćete ovaj Prompt flow sa prilagođenom konekcijom kako biste mogli da koristite fino podešeni model unutar Prompt flow-a.

1. Idite do Azure AI Foundry projekta koji ste kreirali.

1. Izaberite **Prompt flow** sa leve strane.

1. Izaberite **+ Create** iz navigacionog menija.

    ![Select Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.sr.png)

1. Izaberite **Chat flow** iz navigacionog menija.

    ![Select chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.sr.png)

1. Unesite **Folder name** koji želite da koristite.

    ![Enter name.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.sr.png)

2. Izaberite **Create**.

#### Podesite Prompt flow za ćaskanje sa vašim prilagođenim Phi-3 modelom

Potrebno je da integrišete fino podešeni Phi-3 model u Prompt flow. Međutim, postojeći Prompt flow nije dizajniran za ovu svrhu. Zato je potrebno da redizajnirate Prompt flow kako biste omogućili integraciju prilagođenog modela.

1. U Prompt flow-u, uradite sledeće da biste prepravili postojeći tok:

    - Izaberite **Raw file mode**.
    - Obrišite sav postojeći kod u *flow.dag.yml* fajlu.
    - Dodajte sledeći kod u *flow.dag.yml* fajl.

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

    - Izaberite **Save**.

    ![Select raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.sr.png)

1. Dodajte sledeći kod u *integrate_with_promptflow.py* fajl da biste koristili prilagođeni Phi-3 model u Prompt flow-u.

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

    ![Paste prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.sr.png)

> [!NOTE]
> Za detaljnije informacije o korišćenju Prompt flow u Azure AI Foundry, možete pogledati [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Izaberite **Chat input**, **Chat output** da omogućite ćaskanje sa vašim modelom.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.sr.png)

1. Sada ste spremni da ćaskate sa vašim prilagođenim Phi-3 modelom. U sledećem zadatku naučićete kako da pokrenete Prompt flow i koristite ga za razgovor sa fino podešenim Phi-3 modelom.

> [!NOTE]
>
> Prepravljeni tok treba da izgleda kao na slici ispod:
>
> ![Flow example.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.sr.png)
>

### Ćaskajte sa vašim prilagođenim Phi-3 modelom

Sada kada ste fino podesili i integrisali vaš prilagođeni Phi-3 model sa Prompt flow-om, spremni ste da počnete interakciju sa njim. Ovaj zadatak će vas voditi kroz proces podešavanja i pokretanja ćaskanja sa vašim modelom koristeći Prompt flow. Prateći ove korake, moći ćete u potpunosti da iskoristite mogućnosti vašeg fino podešenog Phi-3 modela za različite zadatke i razgovore.

- Ćaskajte sa vašim prilagođenim Phi-3 modelom koristeći Prompt flow.

#### Pokrenite Prompt flow

1. Izaberite **Start compute sessions** da pokrenete Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.sr.png)

1. Izaberite **Validate and parse input** da osvežite parametre.

    ![Validate input.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.sr.png)

1. Izaberite **Value** za **connection** i povežite ga sa prilagođenom konekcijom koju ste napravili. Na primer, *connection*.

    ![Connection.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.sr.png)

#### Ćaskajte sa vašim prilagođenim modelom

1. Izaberite **Chat**.

    ![Select chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.sr.png)

1. Evo primera rezultata: Sada možete da ćaskate sa vašim prilagođenim Phi-3 modelom. Preporučuje se da postavljate pitanja na osnovu podataka korišćenih za fino podešavanje.

    ![Chat with prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.sr.png)

**Ограничење одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да превод буде прецизан, молимо имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.