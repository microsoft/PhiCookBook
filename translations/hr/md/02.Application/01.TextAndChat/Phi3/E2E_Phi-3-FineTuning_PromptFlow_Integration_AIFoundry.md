# Doradi i integriraj prilagođene Phi-3 modele s Prompt flow u Microsoft Foundry

Ovaj uzorak od početka do kraja (E2E) temelji se na vodiču "[Doradi i integriraj prilagođene Phi-3 modele s Prompt Flow u Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" iz Microsoft Tech Communityja. Uvodi procese dorađivanja, implementacije i integracije prilagođenih Phi-3 modela s Prompt flow u Microsoft Foundry.
Za razliku od E2E uzorka, "[Doradi i integriraj prilagođene Phi-3 modele s Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", koji je uključivao lokalno pokretanje koda, ovaj vodič se u potpunosti fokusira na dorađivanje i integraciju vašeg modela unutar Azure AI / ML Studia.

## Pregled

U ovom E2E uzorku naučit ćete kako doraditi Phi-3 model i integrirati ga s Prompt flow u Microsoft Foundry. Korištenjem Azure AI / ML Studia uspostavit ćete radni tijek za implementaciju i korištenje prilagođenih AI modela. Ovaj E2E uzorak podijeljen je u tri scenarija:

**Scenarij 1: Postavljanje Azure resursa i priprema za dorađivanje**

**Scenarij 2: Dorađivanje Phi-3 modela i implementacija u Azure Machine Learning Studio**

**Scenarij 3: Integracija s Prompt flow i razgovor s vašim prilagođenim modelom u Microsoft Foundry**

Evo pregleda ovog E2E uzorka.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/hr/00-01-architecture.198ba0f1ae6d841a.webp)

### Sadržaj

1. **[Scenarij 1: Postavljanje Azure resursa i priprema za dorađivanje](#scenarij-1-postavljanje-azure-resursa-i-priprema-za-dorađivanje)**
    - [Kreirajte Azure Machine Learning Workspace](#kreirajte-azure-machine-learning-workspace)
    - [Zatražite GPU kvote u Azure pretplati](#zatražite-gpu-kvote-u-azure-pretplati)
    - [Dodajte dodjelu uloge](#dodajte-dodjelu-uloge)
    - [Postavite projekt](#postavite-projekt)
    - [Pripremite skup podataka za dorađivanje](#pripremite-skup-podataka-za-fino-podešavanje)

1. **[Scenarij 2: Doradite Phi-3 model i implementirajte u Azure Machine Learning Studio](#scenarij-2-fino-podesite-phi-3-model-i-implementirajte-u-azure-machine-learning-studio)**
    - [Doradite Phi-3 model](#fino-podesite-phi-3-model)
    - [Implementirajte doradeni Phi-3 model](#implementirajte-fino-podešeni-phi-3-model)

1. **[Scenarij 3: Integrirajte s Prompt flow i razgovarajte s prilagođenim modelom u Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Integrirajte prilagođeni Phi-3 model s Prompt flow](#integrirajte-prilagođeni-phi-3-model-s-prompt-flow)
    - [Razgovarajte s prilagođenim Phi-3 modelom](#chat-s-vašim-prilagođenim-phi-3-modelom)

## Scenarij 1: Postavljanje Azure resursa i priprema za dorađivanje

### Kreirajte Azure Machine Learning Workspace

1. Upišite *azure machine learning* u **traku za pretraživanje** na vrhu stranice portala i odaberite **Azure Machine Learning** iz prikazanih opcija.

    ![Type azure machine learning.](../../../../../../translated_images/hr/01-01-type-azml.acae6c5455e67b4b.webp)

2. Odaberite **+ Create** iz navigacijskog izbornika.

3. Odaberite **New workspace** iz navigacijskog izbornika.

    ![Select new workspace.](../../../../../../translated_images/hr/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Obavite sljedeće zadatke:

    - Odaberite svoju Azure **pretplatu**.
    - Odaberite **Resource group** koju želite koristiti (kreirajte novu ako je potrebno).
    - Unesite **Workspace Name**. Mora biti jedinstvena vrijednost.
    - Odaberite **Region** koji želite koristiti.
    - Odaberite **Storage account** za korištenje (kreirajte novi ako je potrebno).
    - Odaberite **Key vault** za korištenje (kreirajte novi ako je potrebno).
    - Odaberite **Application insights** za korištenje (kreirajte novi ako je potrebno).
    - Odaberite **Container registry** za korištenje (kreirajte novi ako je potrebno).

    ![Fill azure machine learning.](../../../../../../translated_images/hr/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Odaberite **Review + Create**.

6. Odaberite **Create**.

### Zatražite GPU kvote u Azure pretplati

U ovom vodiču naučit ćete kako doraditi i implementirati Phi-3 model koristeći GPU-ove. Za dorađivanje ćete koristiti *Standard_NC24ads_A100_v4* GPU, za što je potrebna prijava kvote. Za implementaciju ćete koristiti *Standard_NC6s_v3* GPU, za što je također potrebna prijava kvote.

> [!NOTE]
>
> Samo pretplate po modelu Pay-As-You-Go (standardna vrsta pretplate) imaju pravo na dodjelu GPU; pretplate s benefitima trenutno nisu podržane.
>

1. Posjetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Obavite sljedeće zadatke da biste zatražili kvotu *Standard NCADSA100v4 Family*:

    - Odaberite **Quota** u lijevom izborniku.
    - Odaberite **Virtual machine family** koju želite koristiti. Na primjer, odaberite **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, koja uključuje *Standard_NC24ads_A100_v4* GPU.
    - Odaberite **Request quota** u navigacijskom izborniku.

        ![Request quota.](../../../../../../translated_images/hr/02-02-request-quota.c0428239a63ffdd5.webp)

    - Na stranici Request quota unesite **New cores limit** koju želite koristiti. Na primjer, 24.
    - Na stranici Request quota odaberite **Submit** da biste poslali zahtjev za GPU kvotu.

1. Obavite sljedeće zadatke da biste zatražili kvotu *Standard NCSv3 Family*:

    - Odaberite **Quota** u lijevom izborniku.
    - Odaberite **Virtual machine family** koju želite koristiti. Na primjer, odaberite **Standard NCSv3 Family Cluster Dedicated vCPUs**, koja uključuje *Standard_NC6s_v3* GPU.
    - Odaberite **Request quota** u navigacijskom izborniku.
    - Na stranici Request quota unesite **New cores limit** koju želite koristiti. Na primjer, 24.
    - Na stranici Request quota odaberite **Submit** da biste poslali zahtjev za GPU kvotu.

### Dodajte dodjelu uloge

Za dorađivanje i implementaciju vaših modela, prvo morate kreirati Korisnički dodijeljeni upravljani identitet (User Assigned Managed Identity - UAI) i dodijeliti mu odgovarajuće dozvole. Taj UAI koristit će se za autentifikaciju tijekom implementacije.

#### Kreirajte Korisnički dodijeljeni upravljani identitet (UAI)

1. Upišite *managed identities* u **traku za pretraživanje** na vrhu portala i odaberite **Managed Identities** iz prikazanih opcija.

    ![Type managed identities.](../../../../../../translated_images/hr/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Odaberite **+ Create**.

    ![Select create.](../../../../../../translated_images/hr/03-02-select-create.92bf8989a5cd98f2.webp)

1. Obavite sljedeće zadatke:

    - Odaberite svoju Azure **pretplatu**.
    - Odaberite **Resource group** koju želite koristiti (kreirajte novu ako je potrebno).
    - Odaberite **Region** koji želite koristiti.
    - Unesite **Name**. Mora biti jedinstvena vrijednost.

    ![Select create.](../../../../../../translated_images/hr/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Odaberite **Review + create**.

1. Odaberite **+ Create**.

#### Dodajte Contributor ulogu upravljanom identitetu

1. Idi na resurs Managed Identity koji ste kreirali.

1. Odaberite **Azure role assignments** na lijevom izborniku.

1. Odaberite **+Add role assignment** u navigacijskom izborniku.

1. Na stranici Add role assignment obavite sljedeće:

    - Odaberite **Scope** na **Resource group**.
    - Odaberite svoju Azure **pretplatu**.
    - Odaberite **Resource group** koju želite koristiti.
    - Odaberite **Role** na **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/hr/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Odaberite **Save**.

#### Dodajte Storage Blob Data Reader ulogu upravljanom identitetu

1. Upišite *storage accounts* u **traku za pretraživanje** na vrhu portala i odaberite **Storage accounts** iz prikazanih opcija.

    ![Type storage accounts.](../../../../../../translated_images/hr/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Odaberite storage account povezan s Azure Machine Learning workspaceom koji ste kreirali. Na primjer, *finetunephistorage*.

1. Obavite sljedeće zadatke za navigaciju do stranice Add role assignment:

    - Idi na Azure Storage račun koji ste kreirali.
    - Odaberite **Access Control (IAM)** na lijevom izborniku.
    - Odaberite **+ Add** u navigacijskom izborniku.
    - Odaberite **Add role assignment** u navigacijskom izborniku.

    ![Add role.](../../../../../../translated_images/hr/03-06-add-role.353ccbfdcf0789c2.webp)

1. Na stranici Add role assignment obavite sljedeće:

    - Na stranici Role upišite *Storage Blob Data Reader* u **traku za pretraživanje** i odaberite **Storage Blob Data Reader** iz prikazanih opcija.
    - Na stranici Role odaberite **Next**.
    - Na stranici Members odaberite **Assign access to** **Managed identity**.
    - Na stranici Members odaberite **+ Select members**.
    - Na stranici Select managed identities odaberite svoju Azure **pretplatu**.
    - Na stranici Select managed identities odaberite **Managed identity** na **Manage Identity**.
    - Na stranici Select managed identities odaberite Managed Identity koju ste kreirali. Na primjer, *finetunephi-managedidentity*.
    - Na stranici Select managed identities odaberite **Select**.

    ![Select managed identity.](../../../../../../translated_images/hr/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Odaberite **Review + assign**.

#### Dodajte AcrPull ulogu upravljanom identitetu

1. Upišite *container registries* u **traku za pretraživanje** na vrhu portala i odaberite **Container registries** iz prikazanih opcija.

    ![Type container registries.](../../../../../../translated_images/hr/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Odaberite container registry povezan s Azure Machine Learning workspaceom. Na primjer, *finetunephicontainerregistry*

1. Obavite sljedeće zadatke za navigaciju do stranice Add role assignment:

    - Odaberite **Access Control (IAM)** na lijevom izborniku.
    - Odaberite **+ Add** u navigacijskom izborniku.
    - Odaberite **Add role assignment** u navigacijskom izborniku.

1. Na stranici Add role assignment obavite sljedeće:

    - Na stranici Role upišite *AcrPull* u **traku za pretraživanje** i odaberite **AcrPull** iz prikazanih opcija.
    - Na stranici Role odaberite **Next**.
    - Na stranici Members odaberite **Assign access to** **Managed identity**.
    - Na stranici Members odaberite **+ Select members**.
    - Na stranici Select managed identities odaberite svoju Azure **pretplatu**.
    - Na stranici Select managed identities odaberite **Managed identity** na **Manage Identity**.
    - Na stranici Select managed identities odaberite Managed Identity koju ste kreirali. Na primjer, *finetunephi-managedidentity*.
    - Na stranici Select managed identities odaberite **Select**.
    - Odaberite **Review + assign**.

### Postavite projekt

Za preuzimanje skupova podataka potrebnih za dorađivanje, postavit ćete lokalno okruženje.

U ovom zadatku ćete

- Kreirati mapu u kojoj ćete raditi.
- Kreirati virtualno okruženje.
- Instalirati potrebne pakete.
- Kreirati datoteku *download_dataset.py* za preuzimanje skupa podataka.

#### Kreirajte mapu u kojoj ćete raditi

1. Otvorite terminal i upišite sljedeću naredbu da biste kreirali mapu nazvanu *finetune-phi* u zadanoj putanji.

    ```console
    mkdir finetune-phi
    ```

2. Upišite sljedeću naredbu u terminal da biste se prebacili u mapu *finetune-phi* koju ste kreirali.

    ```console
    cd finetune-phi
    ```

#### Kreirajte virtualno okruženje

1. Upišite sljedeću naredbu u terminal da biste kreirali virtualno okruženje nazvano *.venv*.
    ```console
    python -m venv .venv
    ```

2. Upišite sljedeću naredbu u svoj terminal za aktivaciju virtualnog okruženja.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Ako je uspjelo, trebali biste vidjeti *(.venv)* ispred prompta naredbenog retka.

#### Instalirajte potrebne pakete

1. Upišite sljedeće naredbe u svoj terminal za instalaciju potrebnih paketa.

    ```console
    pip install datasets==2.19.1
    ```

#### Kreirajte `donload_dataset.py`

> [!NOTE]
> Kompletna struktura mapa:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Otvorite **Visual Studio Code**.

1. Odaberite **File** iz izbornika.

1. Odaberite **Open Folder**.

1. Odaberite mapu *finetune-phi* koju ste kreirali, a koja se nalazi na *C:\Users\yourUserName\finetune-phi*.

    ![Odaberite mapu koju ste kreirali.](../../../../../../translated_images/hr/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. U lijevom oknu Visual Studio Code-a, desnim klikom odaberite **New File** za kreiranje nove datoteke nazvane *download_dataset.py*.

    ![Kreirajte novu datoteku.](../../../../../../translated_images/hr/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Pripremite skup podataka za fino podešavanje

U ovom zadatku pokrenut ćete datoteku *download_dataset.py* kako biste preuzeli *ultrachat_200k* skupove podataka na svoje lokalno okruženje. Potom ćete te skupove podataka koristiti za fino podešavanje Phi-3 modela u Azure Machine Learning.

U ovom zadatku ćete:

- Dodati kod u datoteku *download_dataset.py* za preuzimanje skupova podataka.
- Pokrenuti datoteku *download_dataset.py* za preuzimanje skupova podataka na lokalno okruženje.

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
        # Učitaj skup podataka sa specificiranim imenom, konfiguracijom i omjerom podjele
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Podijeli skup podataka na trening i test skupove (80% trening, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Kreiraj direktorij ako ne postoji
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Otvori datoteku u načinu pisanja
        with open(filepath, 'w', encoding='utf-8') as f:
            # Prođi kroz svaki zapis u skupu podataka
            for record in dataset:
                # Spremi zapis kao JSON objekt i upiši ga u datoteku
                json.dump(record, f)
                # Upisi znak za novi red kako bi se zapisi odvojili
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Učitaj i podijeli ULTRACHAT_200k skup podataka sa specifičnom konfiguracijom i omjerom podjele
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Izvuci trening i test setove iz podjele
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Spremi trening skup podataka u JSONL datoteku
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Spremi test skup podataka u zasebnu JSONL datoteku
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Upišite sljedeću naredbu u svoj terminal za pokretanje skripte i preuzimanje skupa podataka na svoje lokalno okruženje.

    ```console
    python download_dataset.py
    ```

1. Provjerite jesu li skupovi podataka uspješno spremljeni u lokalni direktorij *finetune-phi/data*.

> [!NOTE]
>
> #### Napomena o veličini skupa podataka i vremenu finog podešavanja
>
> U ovom vodiču koristite samo 1% skupa podataka (`split='train[:1%]'`). To značajno smanjuje količinu podataka, ubrzavajući prijenos i proces finog podešavanja. Možete prilagoditi postotak kako biste pronašli pravu ravnotežu između vremena treniranja i performansi modela. Korištenje manjeg dijela skupa podataka smanjuje vrijeme potrebno za fino podešavanje, čineći proces upravljivijim za vodič.

## Scenarij 2: Fino podesite Phi-3 model i implementirajte u Azure Machine Learning Studio

### Fino podesite Phi-3 model

U ovom zadatku fino ćete podesiti Phi-3 model u Azure Machine Learning Studio.

U ovom zadatku ćete:

- Kreirati računalni klaster za fino podešavanje.
- Fino podesiti Phi-3 model u Azure Machine Learning Studio.

#### Kreirajte računalni klaster za fino podešavanje

1. Posjetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Odaberite **Compute** s lijevog izbornika.

1. Odaberite **Compute clusters** iz navigacijskog izbornika.

1. Odaberite **+ New**.

    ![Odaberite compute.](../../../../../../translated_images/hr/06-01-select-compute.a29cff290b480252.webp)

1. Obavite sljedeće radnje:

    - Odaberite **Regiju** koju želite koristiti.
    - Odaberite **Virtual machine tier** na **Dedicated**.
    - Odaberite **Virtual machine type** na **GPU**.
    - Odaberite filtar **Virtual machine size** na **Select from all options**.
    - Odaberite **Virtual machine size** na **Standard_NC24ads_A100_v4**.

    ![Kreirajte klaster.](../../../../../../translated_images/hr/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Odaberite **Next**.

1. Obavite sljedeće radnje:

    - Unesite **Ime klastera**. Mora biti jedinstvena vrijednost.
    - Odaberite **Minimalan broj čvorova** na **0**.
    - Odaberite **Maksimalan broj čvorova** na **1**.
    - Odaberite **Idle seconds before scale down** na **120**.

    ![Kreirajte klaster.](../../../../../../translated_images/hr/06-03-create-cluster.4a54ba20914f3662.webp)

1. Odaberite **Create**.

#### Fino podesite Phi-3 model

1. Posjetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Odaberite Azure Machine Learning radni prostor koji ste kreirali.

    ![Odaberite radni prostor koji ste kreirali.](../../../../../../translated_images/hr/06-04-select-workspace.a92934ac04f4f181.webp)

1. Obavite sljedeće radnje:

    - Odaberite **Model catalog** s lijevog izbornika.
    - Upišite *phi-3-mini-4k* u **traku za pretraživanje** i odaberite **Phi-3-mini-4k-instruct** iz ponuđenih opcija.

    ![Upišite phi-3-mini-4k.](../../../../../../translated_images/hr/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Odaberite **Fine-tune** iz navigacijskog izbornika.

    ![Odaberite fino podešavanje.](../../../../../../translated_images/hr/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Obavite sljedeće radnje:

    - Odaberite **Select task type** na **Chat completion**.
    - Odaberite **+ Select data** za učitavanje **Trening podataka**.
    - Odaberite opciju za učitavanje podataka za validaciju na **Provide different validation data**.
    - Odaberite **+ Select data** za učitavanje **Validation data**.

    ![Ispunite stranicu za fino podešavanje.](../../../../../../translated_images/hr/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Možete odabrati **Advanced settings** da prilagodite konfiguracije poput **learning_rate** i **lr_scheduler_type** kako biste optimizirali proces finog podešavanja prema svojim potrebama.

1. Odaberite **Finish**.

1. U ovom zadatku uspješno ste fino podesili Phi-3 model koristeći Azure Machine Learning. Imajte na umu da proces finog podešavanja može potrajati. Nakon pokretanja posla finog podešavanja, trebate pričekati da se završi. Status posla možete pratiti u kartici Jobs na lijevoj strani vašeg Azure Machine Learning radnog prostora. U sljedećem nizu zadataka implementirat ćete fino podešeni model i integrirati ga s Prompt flow.

    ![Pogledajte posao finog podešavanja.](../../../../../../translated_images/hr/06-08-output.2bd32e59930672b1.webp)

### Implementirajte fino podešeni Phi-3 model

Kako biste integrirali fino podešeni Phi-3 model s Prompt flow, morate implementirati model da bude dostupan za predviđanja u stvarnom vremenu. Taj proces uključuje registraciju modela, kreiranje online krajnje točke i implementaciju modela.

U ovom ćete zadatku:

- Registrirati fino podešeni model u Azure Machine Learning radnom prostoru.
- Kreirati online krajnju točku.
- Implementirati registrirani fino podešeni Phi-3 model.

#### Registrirajte fino podešeni model

1. Posjetite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Odaberite Azure Machine Learning radni prostor koji ste kreirali.

    ![Odaberite radni prostor koji ste kreirali.](../../../../../../translated_images/hr/06-04-select-workspace.a92934ac04f4f181.webp)

1. Odaberite **Models** s lijevog izbornika.
1. Odaberite **+ Register**.
1. Odaberite **From a job output**.

    ![Registrirajte model.](../../../../../../translated_images/hr/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Odaberite posao koji ste kreirali.

    ![Odaberite posao.](../../../../../../translated_images/hr/07-02-select-job.3e2e1144cd6cd093.webp)

1. Odaberite **Next**.

1. Odaberite **Model type** na **MLflow**.

1. Provjerite je li odabrana opcija **Job output**; trebala bi biti automatski odabrana.

    ![Odaberite output.](../../../../../../translated_images/hr/07-03-select-output.4cf1a0e645baea1f.webp)

2. Odaberite **Next**.

3. Odaberite **Register**.

    ![Odaberite registraciju.](../../../../../../translated_images/hr/07-04-register.fd82a3b293060bc7.webp)

4. Registrirani model možete pregledati odabirom izbornika **Models** s lijevog izbornika.

    ![Registrirani model.](../../../../../../translated_images/hr/07-05-registered-model.7db9775f58dfd591.webp)

#### Implementirajte fino podešeni model

1. Idite na Azure Machine Learning radni prostor koji ste kreirali.

1. Odaberite **Endpoints** s lijevog izbornika.

1. Odaberite **Real-time endpoints** iz navigacijskog izbornika.

    ![Kreirajte krajnju točku.](../../../../../../translated_images/hr/07-06-create-endpoint.1ba865c606551f09.webp)

1. Odaberite **Create**.

1. Odaberite registrirani model koji ste kreirali.

    ![Odaberite registrirani model.](../../../../../../translated_images/hr/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Odaberite **Select**.

1. Obavite sljedeće radnje:

    - Odaberite **Virtual machine** na *Standard_NC6s_v3*.
    - Odaberite broj instanci koje želite koristiti. Na primjer, *1*.
    - Postavite **Endpoint** na **New** za kreiranje nove krajnje točke.
    - Unesite **Ime krajnje točke**. Mora biti jedinstvena vrijednost.
    - Unesite **Ime implementacije**. Mora biti jedinstvena vrijednost.

    ![Ispunite postavke implementacije.](../../../../../../translated_images/hr/07-08-deployment-setting.43ddc4209e673784.webp)

1. Odaberite **Deploy**.

> [!WARNING]
> Kako biste izbjegli dodatne troškove na svom računu, obavezno izbrišite kreiranu krajnju točku u Azure Machine Learning radnom prostoru.
>

#### Provjerite status implementacije u Azure Machine Learning Workspaceu

1. Idite u Azure Machine Learning radni prostor koji ste kreirali.

1. Odaberite **Endpoints** s lijevog izbornika.

1. Odaberite krajnju točku koju ste kreirali.

    ![Odaberite krajnje točke](../../../../../../translated_images/hr/07-09-check-deployment.325d18cae8475ef4.webp)

1. Na ovoj stranici možete upravljati krajnjim točkama tijekom procesa implementacije.

> [!NOTE]
> Nakon završetka implementacije, provjerite je li **Live traffic** postavljen na **100%**. Ako nije, odaberite **Update traffic** da podesite promet. Imajte na umu da ne možete testirati model ako je promet postavljen na 0%.
>
> ![Postavite promet.](../../../../../../translated_images/hr/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Scenarij 3: Integracija s Prompt flow i razgovor s vlastitim modelom u Microsoft Foundry

### Integrirajte prilagođeni Phi-3 model s Prompt flow

Nakon uspješne implementacije vašeg fino podešenog modela, sada ga možete integrirati s Prompt Flow kako biste koristili model u aplikacijama u stvarnom vremenu, omogućujući niz interaktivnih zadataka s vašim prilagođenim Phi-3 modelom.

U ovom zadatku ćete:

- Kreirati Microsoft Foundry Hub.
- Kreirati Microsoft Foundry Projekt.
- Kreirati Prompt flow.
- Dodati prilagođenu vezu za fino podešeni Phi-3 model.
- Postaviti Prompt flow za razgovor s vašim prilagođenim Phi-3 modelom.

> [!NOTE]
> Također se možete integrirati s Promptflow koristeći Azure ML Studio. Isti proces integracije primjenjiv je u Azure ML Studio.

#### Kreirajte Microsoft Foundry Hub

Prije kreiranja Projekta, morate kreirati Hub. Hub djeluje kao Resource Group, omogućujući organizaciju i upravljanje više Projekata unutar Microsoft Foundry.
1. Posjetite [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Odaberite **All hubs** s lijevog izbornika.

1. Odaberite **+ New hub** iz navigacijskog izbornika.

    ![Create hub.](../../../../../../translated_images/hr/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Izvršite sljedeće zadatke:

    - Unesite **Hub name**. Mora biti jedinstvena vrijednost.
    - Odaberite svoj Azure **Subscription**.
    - Odaberite **Resource group** koji želite koristiti (stvorite novi po potrebi).
    - Odaberite **Location** koju želite koristiti.
    - Odaberite **Connect Azure AI Services** koji želite koristiti (stvorite novi po potrebi).
    - Odaberite **Connect Azure AI Search** na **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/hr/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Odaberite **Next**.

#### Stvaranje Microsoft Foundry projekta

1. U hubu koji ste stvorili, odaberite **All projects** s lijevog izbornika.

1. Odaberite **+ New project** iz navigacijskog izbornika.

    ![Select new project.](../../../../../../translated_images/hr/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Unesite **Project name**. Mora biti jedinstvena vrijednost.

    ![Create project.](../../../../../../translated_images/hr/08-05-create-project.4d97f0372f03375a.webp)

1. Odaberite **Create a project**.

#### Dodavanje prilagođene veze za fino podešeni Phi-3 model

Za integraciju vašeg prilagođenog Phi-3 modela s Prompt flow, potrebno je spremiti endpoint i ključ modela u prilagođenu vezu. Ova postavka osigurava pristup vašem prilagođenom Phi-3 modelu unutar Prompt flow.

#### Postavljanje api ključa i endpoint URI-ja fino podešenog Phi-3 modela

1. Posjetite [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navigirajte do Azure Machine learning workspace-a koji ste stvorili.

1. Odaberite **Endpoints** s lijevog izbornika.

    ![Select endpoints.](../../../../../../translated_images/hr/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Odaberite endpoint koji ste stvorili.

    ![Select endpoints.](../../../../../../translated_images/hr/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Odaberite **Consume** iz navigacijskog izbornika.

1. Kopirajte svoj **REST endpoint** i **Primary key**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/hr/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Dodavanje prilagođene veze

1. Posjetite [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navigirajte do Microsoft Foundry projekta koji ste stvorili.

1. U projektu koji ste stvorili, odaberite **Settings** s lijevog izbornika.

1. Odaberite **+ New connection**.

    ![Select new connection.](../../../../../../translated_images/hr/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Odaberite **Custom keys** iz navigacijskog izbornika.

    ![Select custom keys.](../../../../../../translated_images/hr/08-10-select-custom-keys.856f6b2966460551.webp)

1. Izvršite sljedeće zadatke:

    - Odaberite **+ Add key value pairs**.
    - Za ime ključa unesite **endpoint** i zalijepite endpoint koji ste kopirali iz Azure ML Studija u polje za vrijednost.
    - Ponovno odaberite **+ Add key value pairs**.
    - Za ime ključa unesite **key** i zalijepite ključ koji ste kopirali iz Azure ML Studija u polje za vrijednost.
    - Nakon dodavanja ključeva, odaberite **is secret** kako biste spriječili izlaganje ključa.

    ![Add connection.](../../../../../../translated_images/hr/08-11-add-connection.785486badb4d2d26.webp)

1. Odaberite **Add connection**.

#### Stvaranje Prompt flow

Dodali ste prilagođenu vezu u Microsoft Foundry. Sada, kreirajte Prompt flow slijedeći dolje navedene korake. Zatim ćete povezati ovaj Prompt flow s prilagođenom vezom kako biste mogli koristiti fino podešeni model unutar Prompt flow.

1. Navigirajte do Microsoft Foundry projekta koji ste stvorili.

1. Odaberite **Prompt flow** s lijevog izbornika.

1. Odaberite **+ Create** iz navigacijskog izbornika.

    ![Select Promptflow.](../../../../../../translated_images/hr/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Odaberite **Chat flow** iz navigacijskog izbornika.

    ![Select chat flow.](../../../../../../translated_images/hr/08-13-select-flow-type.2ec689b22da32591.webp)

1. Unesite **Folder name** za korištenje.

    ![Enter name.](../../../../../../translated_images/hr/08-14-enter-name.ff9520fefd89f40d.webp)

2. Odaberite **Create**.

#### Postavljanje Prompt flow za chat s vašim prilagođenim Phi-3 modelom

Potrebno je integrirati fino podešeni Phi-3 model u Prompt flow. Međutim, postojeći Prompt flow nije dizajniran za ovu svrhu. Stoga je potrebno redizajnirati Prompt flow kako bi se omogućila integracija prilagođenog modela.

1. U Prompt flow-u izvršite sljedeće zadatke kako biste obnovili postojeći tok:

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

    - Odaberite **Save**.

    ![Select raw file mode.](../../../../../../translated_images/hr/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Dodajte sljedeći kod u *integrate_with_promptflow.py* datoteku za korištenje prilagođenog Phi-3 modela u Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Postavljanje zapisivanja
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

        # "connection" je ime Prilagođene veze, "endpoint", "key" su ključevi u Prilagođenoj vezi
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
            
            # Zabilježite puni JSON odgovor
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

    ![Paste prompt flow code.](../../../../../../translated_images/hr/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Za detaljnije informacije o korištenju Prompt flow u Microsoft Foundry, možete pogledati [Prompt flow u Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Odaberite **Chat input**, **Chat output** da omogućite chat s vašim modelom.

    ![Input Output.](../../../../../../translated_images/hr/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Sada ste spremni za chat s vašim prilagođenim Phi-3 modelom. U sljedećoj vježbi naučit ćete kako pokrenuti Prompt flow i koristiti ga za chat s vašim fino podešenim Phi-3 modelom.

> [!NOTE]
>
> Obnovljeni tok bi trebao izgledati kao na slici ispod:
>
> ![Flow example.](../../../../../../translated_images/hr/08-18-graph-example.d6457533952e690c.webp)
>

### Chat s vašim prilagođenim Phi-3 modelom

Sada kada ste fino podesili i integrirali svoj prilagođeni Phi-3 model s Prompt flow, spremni ste započeti interakciju s njim. Ova vježba će vas voditi kroz postupak postavljanja i pokretanja chata s vašim modelom korištenjem Prompt flow. Slijedeći ove korake, moći ćete u potpunosti iskoristiti mogućnosti vašeg fino podešenog Phi-3 modela za razne zadatke i razgovore.

- Čavrljajte s vašim prilagođenim Phi-3 modelom koristeći Prompt flow.

#### Pokretanje Prompt flow

1. Odaberite **Start compute sessions** za pokretanje Prompt flow.

    ![Start compute session.](../../../../../../translated_images/hr/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Odaberite **Validate and parse input** za osvježavanje parametara.

    ![Validate input.](../../../../../../translated_images/hr/09-02-validate-input.317c76ef766361e9.webp)

1. Odaberite **Value** od **connection** prema prilagođenoj vezi koju ste stvorili. Na primjer, *connection*.

    ![Connection.](../../../../../../translated_images/hr/09-03-select-connection.99bdddb4b1844023.webp)

#### Chat s vašim prilagođenim modelom

1. Odaberite **Chat**.

    ![Select chat.](../../../../../../translated_images/hr/09-04-select-chat.61936dce6612a1e6.webp)

1. Evo primjera rezultata: sada možete chatati s vašim prilagođenim Phi-3 modelom. Preporuča se postavljati pitanja temeljena na podacima korištenim za fino podešavanje.

    ![Chat with prompt flow.](../../../../../../translated_images/hr/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje odgovornosti**:
Ovaj dokument je preveden korištenjem AI usluge za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, molimo imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporuča se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->