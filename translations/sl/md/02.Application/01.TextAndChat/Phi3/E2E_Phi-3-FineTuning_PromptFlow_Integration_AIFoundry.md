# Natančno prilagodi in integriraj prilagojene modele Phi-3 s Prompt flow v Microsoft Foundry

Ta vzorec od začetka do konca (E2E) temelji na vodiču "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" iz Microsoft Tech Community. Predstavlja postopke natančnega prilagajanja, uvajanja in integracije prilagojenih modelov Phi-3 s Prompt flow v Microsoft Foundry.
Za razliko od E2E vzorca, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", ki je vključeval lokalno izvajanje kode, se ta vadnica popolnoma osredotoča na natančno prilagajanje in integracijo vašega modela znotraj Azure AI / ML Studio.

## Pregled

V tem E2E vzorcu se boste naučili, kako natančno prilagoditi model Phi-3 in ga integrirati s Prompt flow v Microsoft Foundry. Z uporabo Azure AI / ML Studio boste vzpostavili delovni tok za uvajanje in uporabo prilagojenih AI modelov. Ta E2E vzorec je razdeljen na tri scenarije:

**Scenarij 1: Nastavitev Azure virov in priprava za natančno prilagajanje**

**Scenarij 2: Natančno prilagodite model Phi-3 in ga uvedite v Azure Machine Learning Studio**

**Scenarij 3: Integrirajte s Prompt flow in klepetajte s svojim prilagojenim modelom v Microsoft Foundry**

Tukaj je pregled tega E2E vzorca.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/sl/00-01-architecture.198ba0f1ae6d841a.webp)

### Kazalo

1. **[Scenarij 1: Nastavitev Azure virov in priprava za natančno prilagajanje](#scenarij-1-nastavitev-azure-virov-in-priprava-za-natančno-prilagajanje)**
    - [Ustvarite Azure Machine Learning delovno okolje](#ustvarite-azure-machine-learning-delovno-okolje)
    - [Zahtevajte kvote GPU v naročnini Azure](#zahtevajte-kvote-gpu-v-naročnini-azure)
    - [Dodajte dodelitev vlog](#dodajte-dodelitev-vlog)
    - [Nastavite projekt](#nastavite-projekt)
    - [Pripravite podatkovni niz za natančno prilagajanje](#priprava-podatkovnega-nabora-za-dodatno-usposabljanje)

1. **[Scenarij 2: Natančno prilagodite model Phi-3 in ga uvedite v Azure Machine Learning Studio](#scenarij-2-dodatno-usposabljanje-modela-phi-3-in-nameščanje-v-azure-machine-learning-studio)**
    - [Natančno prilagodite model Phi-3](#dodatno-usposabljanje-modela-phi-3)
    - [Uvedite natančno prilagojen model Phi-3](#namestitev-dodatno-usposobljenega-modela-phi-3)

1. **[Scenarij 3: Integrirajte s Prompt flow in klepetajte s svojim prilagojenim modelom v Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Integrirajte prilagojeni model Phi-3 s Prompt flow](#integracija-prilagojenega-modela-phi-3-s-prompt-flow)
    - [Klepetajte s svojim prilagojenim modelom Phi-3](#klepetajte-z-vašim-lastnim-modelom-phi-3)

## Scenarij 1: Nastavitev Azure virov in priprava za natančno prilagajanje

### Ustvarite Azure Machine Learning delovno okolje

1. V iskalno vrstico na vrhu portala vnesite *azure machine learning* in izberite **Azure Machine Learning** med prikazanimi možnostmi.

    ![Type azure machine learning.](../../../../../../translated_images/sl/01-01-type-azml.acae6c5455e67b4b.webp)

2. Izberite **+ Create** v navigacijskem meniju.

3. Izberite **New workspace** v navigacijskem meniju.

    ![Select new workspace.](../../../../../../translated_images/sl/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Izvedite naslednje korake:

    - Izberite svojo Azure **Naročnino**.
    - Izberite **Skupino virov** za uporabo (ustvarite novo, če je potrebno).
    - Vnesite **Ime delovnega okolja**. Mora biti unikatna vrednost.
    - Izberite **Regijo**, ki jo želite uporabiti.
    - Izberite **Račun za shranjevanje** za uporabo (ustvarite novega, če je potrebno).
    - Izberite **Key vault** za uporabo (ustvarite novega, če je potrebno).
    - Izberite **Application insights** za uporabo (ustvarite novega, če je potrebno).
    - Izberite **Registrsko mesto vsebnika** za uporabo (ustvarite novega, če je potrebno).

    ![Fill azure machine learning.](../../../../../../translated_images/sl/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Izberite **Review + Create**.

6. Izberite **Create**.

### Zahtevajte kvote GPU v naročnini Azure

V tej vadnici se boste naučili, kako natančno prilagoditi in uvesti model Phi-3 z uporabo GPUjev. Za natančno prilagajanje boste uporabili GPU *Standard_NC24ads_A100_v4*, ki zahteva zahtevo za kvoto. Za uvajanje boste uporabili GPU *Standard_NC6s_v3*, ki prav tako zahteva zahtevo za kvoto.

> [!NOTE]
>
> Za dodelitev GPU-jev so upravičene samo naročnine Pay-As-You-Go (standardni tip naročnine); naročnine za koristi trenutno niso podprte.
>

1. Obiščite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Izvedite naslednje korake za zahtevo kvote *Standard NCADSA100v4 Family*:

    - Izberite **Quota** na zavihku na levi strani.
    - Izberite **Družino virtualnih računalnikov** za uporabo. Na primer, izberite **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, ki vključuje GPU *Standard_NC24ads_A100_v4*.
    - Izberite **Request quota** v navigacijskem meniju.

        ![Request quota.](../../../../../../translated_images/sl/02-02-request-quota.c0428239a63ffdd5.webp)

    - Na strani zahteve kvote vnesite **Novo omejitev jeder**, ki jo želite uporabiti. Na primer, 24.
    - Na strani zahteve kvote izberite **Submit** za oddajo zahteve GPU kvote.

1. Izvedite naslednje korake za zahtevo kvote *Standard NCSv3 Family*:

    - Izberite **Quota** na zavihku na levi strani.
    - Izberite **Družino virtualnih računalnikov** za uporabo. Na primer, izberite **Standard NCSv3 Family Cluster Dedicated vCPUs**, ki vključuje GPU *Standard_NC6s_v3*.
    - Izberite **Request quota** v navigacijskem meniju.
    - Na strani zahteve kvote vnesite **Novo omejitev jeder**, ki jo želite uporabiti. Na primer, 24.
    - Na strani zahteve kvote izberite **Submit** za oddajo zahteve GPU kvote.

### Dodajte dodelitev vlog

Za natančno prilagajanje in uvajanje vaših modelov morate najprej ustvariti Uporabniško dodeljeno upravljano identiteto (User Assigned Managed Identity, UAI) in ji dodeliti ustrezna dovoljenja. Ta UAI bo uporabljena za overjanje med uvajanjem.

#### Ustvarite uporabniško dodeljeno upravljano identiteto (UAI)

1. V iskalno vrstico na vrhu portala vnesite *managed identities* in izberite **Managed Identities** med prikazanimi možnostmi.

    ![Type managed identities.](../../../../../../translated_images/sl/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Izberite **+ Create**.

    ![Select create.](../../../../../../translated_images/sl/03-02-select-create.92bf8989a5cd98f2.webp)

1. Izvedite naslednje korake:

    - Izberite svojo Azure **Naročnino**.
    - Izberite **Skupino virov** za uporabo (ustvarite novo, če je potrebno).
    - Izberite **Regijo**, ki jo želite uporabiti.
    - Vnesite **Ime**. Mora biti unikatna vrednost.

    ![Select create.](../../../../../../translated_images/sl/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Izberite **Review + create**.

1. Izberite **+ Create**.

#### Dodajte dodelitev vloge Contributor upravljani identiteti

1. Pojdite do vira upravljane identitete, ki ste jo ustvarili.

1. Izberite **Azure role assignments** na zavihku na levi strani.

1. Izberite **+Add role assignment** v navigacijskem meniju.

1. Na strani za dodajanje dodelitve vlog izvedite naslednje korake:
    - Izberite **Obseg** kot **Resource group**.
    - Izberite svojo Azure **Naročnino**.
    - Izberite **Skupino virov** za uporabo.
    - Izberite **Vlogo** kot **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/sl/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Izberite **Save**.

#### Dodajte dodelitev vloge Storage Blob Data Reader upravljani identiteti

1. V iskalno vrstico na vrhu portala vnesite *storage accounts* in izberite **Storage accounts** med prikazanimi možnostmi.

    ![Type storage accounts.](../../../../../../translated_images/sl/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Izberite račun za shranjevanje, povezan z delovnim okoljem Azure Machine Learning, ki ste ga ustvarili. Na primer, *finetunephistorage*.

1. Izvedite naslednje korake za dostop do strani za dodajanje dodelitve vlog:

    - Pojdite v Azure Storage račun, ki ste ga ustvarili.
    - Izberite **Access Control (IAM)** na zavihku na levi strani.
    - Izberite **+ Add** v navigacijskem meniju.
    - Izberite **Add role assignment** v navigacijskem meniju.

    ![Add role.](../../../../../../translated_images/sl/03-06-add-role.353ccbfdcf0789c2.webp)

1. Na strani za dodajanje dodelitve vlog izvedite naslednje korake:

    - Na strani vloge v iskalno polje vnesite *Storage Blob Data Reader* in izberite **Storage Blob Data Reader** med prikazanimi možnostmi.
    - Na strani vloge izberite **Next**.
    - Na strani za člane izberite **Assign access to** **Managed identity**.
    - Na strani za člane izberite **+ Select members**.
    - Na strani za izbiro upravljanih identitet izberite svojo Azure **Naročnino**.
    - Na strani za izbiro upravljanih identitet izberite upravljano identiteto kot **Manage Identity**.
    - Na strani za izbiro upravljanih identitet izberite upravljano identiteto, ki ste jo ustvarili. Na primer, *finetunephi-managedidentity*.
    - Na strani za izbiro upravljanih identitet izberite **Select**.

    ![Select managed identity.](../../../../../../translated_images/sl/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Izberite **Review + assign**.

#### Dodajte dodelitev vloge AcrPull upravljani identiteti

1. V iskalno vrstico na vrhu portala vnesite *container registries* in izberite **Container registries** med prikazanimi možnostmi.

    ![Type container registries.](../../../../../../translated_images/sl/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Izberite registrsko mesto vsebnika, povezano z delovnim okoljem Azure Machine Learning. Na primer, *finetunephicontainerregistry*.

1. Izvedite naslednje korake za dostop do strani za dodajanje dodelitve vlog:

    - Izberite **Access Control (IAM)** na zavihku na levi strani.
    - Izberite **+ Add** v navigacijskem meniju.
    - Izberite **Add role assignment** v navigacijskem meniju.

1. Na strani za dodajanje dodelitve vlog izvedite naslednje korake:

    - Na strani vloge v iskalno polje vnesite *AcrPull* in izberite **AcrPull** med prikazanimi možnostmi.
    - Na strani vloge izberite **Next**.
    - Na strani za člane izberite **Assign access to** **Managed identity**.
    - Na strani za člane izberite **+ Select members**.
    - Na strani za izbiro upravljanih identitet izberite svojo Azure **Naročnino**.
    - Na strani za izbiro upravljanih identitet izberite upravljano identiteto kot **Manage Identity**.
    - Na strani za izbiro upravljanih identitet izberite upravljano identiteto, ki ste jo ustvarili. Na primer, *finetunephi-managedidentity*.
    - Na strani za izbiro upravljanih identitet izberite **Select**.
    - Izberite **Review + assign**.

### Nastavite projekt

Za prenos podatkovnih nizov, potrebnih za natančno prilagajanje, boste nastavili lokalno okolje.

V tem vajenju boste

- ustvarili mapo za delo znotraj nje,
- ustvarili virtualno okolje,
- namestili potrebne pakete,
- ustvarili datoteko *download_dataset.py* za prenos podatkovnega niza.

#### Ustvarite mapo za delo znotraj nje

1. Odprite terminal in za ustvarjanje mape z imenom *finetune-phi* v privzeti poti vnesite naslednji ukaz.

    ```console
    mkdir finetune-phi
    ```

2. Vnesite naslednji ukaz v terminal, da se premaknete v mapo *finetune-phi*, ki ste jo ustvarili.

    ```console
    cd finetune-phi
    ```

#### Ustvarite virtualno okolje

1. Vnesite naslednji ukaz v terminal, da ustvarite virtualno okolje z imenom *.venv*.
    ```console
    python -m venv .venv
    ```

2. V terminal vnesite naslednji ukaz, da aktivirate virtualno okolje.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Če je uspelo, bi morali videti *(.venv)* pred pozivom ukaza.

#### Namestite zahtevane pakete

1. V terminal vnesite naslednje ukaze za namestitev zahtevanih paketov.

    ```console
    pip install datasets==2.19.1
    ```

#### Ustvarite `download_dataset.py`

> [!NOTE]
> Celotna struktura mape:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Odprite **Visual Studio Code**.

1. Izberite **Datoteka** v menijski vrstici.

1. Izberite **Odpri mapo**.

1. Izberite mapo *finetune-phi*, ki ste jo ustvarili, in se nahaja na *C:\Users\yourUserName\finetune-phi*.

    ![Izberite mapo, ki ste jo ustvarili.](../../../../../../translated_images/sl/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. V levem delu okna Visual Studio Code z desnim klikom izberite **Nova datoteka**, da ustvarite novo datoteko z imenom *download_dataset.py*.

    ![Ustvarite novo datoteko.](../../../../../../translated_images/sl/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Priprava podatkovnega nabora za dodatno usposabljanje

V tem vajah boste zagnali datoteko *download_dataset.py*, da prenesete podatkovne nabore *ultrachat_200k* v lokalno okolje. Nato boste uporabili te podatkovne nabore za dodatno usposabljanje modela Phi-3 v Azure Machine Learning.

V tem vaji boste:

- Dodali kodo v datoteko *download_dataset.py* za prenos podatkovnih zbirk.
- Zagnali datoteko *download_dataset.py*, da prenesete podatkovne nabore v lokalno okolje.

#### Prenesite svoj podatkovni nabor z uporabo *download_dataset.py*

1. Odprite datoteko *download_dataset.py* v Visual Studio Code.

1. Dodajte naslednjo kodo v datoteko *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Naložite podatkovni niz z določenim imenom, konfiguracijo in razmerjem delitve
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Razdelite podatkovni niz na učne in testne sete (80% učni, 20% testni)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Ustvarite imenik, če ne obstaja
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Odprite datoteko v načinu pisanja
        with open(filepath, 'w', encoding='utf-8') as f:
            # Ponovite za vsak zapis v podatkovnem nizu
            for record in dataset:
                # Izpišite zapis kot JSON objekt in ga zapišite v datoteko
                json.dump(record, f)
                # Zapišite znak za novo vrstico, da ločite zapise
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Naložite in razdelite podatkovni niz ULTRACHAT_200k s specifično konfiguracijo in razmerjem delitve
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Izvlecite učne in testne podatkovne nize iz razdelka
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Shrani učni podatkovni niz v JSONL datoteko
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Shrani testni podatkovni niz v ločeno JSONL datoteko
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. V terminal vnesite naslednji ukaz, da zaženete skripto in prenesete podatkovni nabor v lokalno okolje.

    ```console
    python download_dataset.py
    ```

1. Preverite, ali so bili podatkovni nabori uspešno shranjeni v lokalni imenik *finetune-phi/data*.

> [!NOTE]
>
> #### Opomba o velikosti podatkovnega nabora in času dodatnega usposabljanja
>
> V tem priročniku uporabljate le 1 % podatkovnega nabora (`split='train[:1%]'`). To bistveno zmanjša količino podatkov ter pospeši tako prenos kot tudi proces dodatnega usposabljanja. Lahko prilagodite odstotek, da najdete pravo ravnovesje med časom usposabljanja in zmogljivostjo modela. Uporaba manjše podmnožice podatkovnega nabora zmanjša čas, potreben za dodatno usposabljanje, kar olajša proces pri navodilih.

## Scenarij 2: Dodatno usposabljanje modela Phi-3 in nameščanje v Azure Machine Learning Studio

### Dodatno usposabljanje modela Phi-3

V tej vaji boste dodatno usposobili model Phi-3 v Azure Machine Learning Studio.

V tej vaji boste:

- Ustvarili računski grozd za dodatno usposabljanje.
- Dodatno usposobili model Phi-3 v Azure Machine Learning Studio.

#### Ustvarite računski grozd za dodatno usposabljanje

1. Obiščite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Izberite **Compute** v levem zavihku.

1. Izberite **Compute clusters** v navigacijskem meniju.

1. Izberite **+ New**.

    ![Izberite računalništvo.](../../../../../../translated_images/sl/06-01-select-compute.a29cff290b480252.webp)

1. Izvedite naslednje naloge:

    - Izberite **Regijo**, ki jo želite uporabiti.
    - Izberite **Virtualni računalniški nivo** na **Dedicated**.
    - Izberite **Vrsto virtualnega računalnika** na **GPU**.
    - Filtrirajte **Velikost virtualnega računalnika** na **Izberi iz vseh možnosti**.
    - Izberite **Velikost virtualnega računalnika** na **Standard_NC24ads_A100_v4**.

    ![Ustvarite grozd.](../../../../../../translated_images/sl/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Izberite **Next**.

1. Izvedite naslednje naloge:

    - Vnesite **Ime grozda**. Mora biti edinstvena vrednost.
    - Nastavite **Minimalno število vozlišč** na **0**.
    - Nastavite **Maksimalno število vozlišč** na **1**.
    - Nastavite **Nepremičnost po skaliranju navzdol** na **120** sekund.

    ![Ustvarite grozd.](../../../../../../translated_images/sl/06-03-create-cluster.4a54ba20914f3662.webp)

1. Izberite **Create**.

#### Dodatno usposobite model Phi-3

1. Obiščite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Izberite Azure Machine Learning delovno okolje, ki ste ga ustvarili.

    ![Izberite ustvarjeno delovno okolje.](../../../../../../translated_images/sl/06-04-select-workspace.a92934ac04f4f181.webp)

1. Izvedite naslednje naloge:

    - Izberite **Model catalog** v levem zavihku.
    - V iskalno polje vnesite *phi-3-mini-4k* in izberite **Phi-3-mini-4k-instruct** med prikazanimi možnostmi.

    ![Vnesite phi-3-mini-4k.](../../../../../../translated_images/sl/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Izberite **Fine-tune** v navigacijskem meniju.

    ![Izberite dodatno usposabljanje.](../../../../../../translated_images/sl/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Izvedite naslednje naloge:

    - Izberite **Izberite tip naloge** na **Chat completion**.
    - Izberite **+ Select data** za nalaganje **Trening podatkov**.
    - Izberite možnost nalaganja Validation podatkov na **Provide different validation data**.
    - Izberite **+ Select data** za nalaganje **Validation podatkov**.

    ![Izpolnite stran za dodatno usposabljanje.](../../../../../../translated_images/sl/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Lahko izberete **Napredne nastavitve** za prilagoditev nastavitev, kot sta **learning_rate** in **lr_scheduler_type**, da optimizirate proces dodatnega usposabljanja glede na vaše specifične potrebe.

1. Izberite **Finish**.

1. V tej vaji ste uspešno dodatno usposobili model Phi-3 z uporabo Azure Machine Learning. Upoštevajte, da lahko proces dodatnega usposabljanja traja precej časa. Po zagonu naloge dodatnega usposabljanja morate počakati, da se zaključi. Status naloge lahko spremljate na zavihku Jobs na levi strani delovnega okolja Azure Machine Learning. V naslednji seriji boste namestili dodatno usposobljen model in ga integrirali s Prompt flow.

    ![Poglejte nalogo dodatnega usposabljanja.](../../../../../../translated_images/sl/06-08-output.2bd32e59930672b1.webp)

### Namestitev dodatno usposobljenega modela Phi-3

Za integracijo dodatno usposobljenega modela Phi-3 s Prompt flow morate model namestiti, da bo dostopen za realnočasni sklepanje. Ta proces vključuje registracijo modela, ustvarjanje spletne točke in namestitev modela.

V tej vaji boste:

- Registrirali dodatno usposobljeni model v Azure Machine Learning delovnem okolju.
- Ustvarili spletno točko.
- Namestili registrirani dodatno usposobljeni model Phi-3.

#### Registrirajte dodatno usposobljeni model

1. Obiščite [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Izberite Azure Machine Learning delovno okolje, ki ste ga ustvarili.

    ![Izberite ustvarjeno delovno okolje.](../../../../../../translated_images/sl/06-04-select-workspace.a92934ac04f4f181.webp)

1. Izberite **Models** v levem zavihku.
1. Izberite **+ Register**.
1. Izberite **From a job output**.

    ![Registracija modela.](../../../../../../translated_images/sl/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Izberite nalogo, ki ste jo ustvarili.

    ![Izberite nalogo.](../../../../../../translated_images/sl/07-02-select-job.3e2e1144cd6cd093.webp)

1. Izberite **Next**.

1. Izberite **Model type** na **MLflow**.

1. Prepričajte se, da je izbran **Job output**; to bi moralo biti izbrano samodejno.

    ![Izberite izhod.](../../../../../../translated_images/sl/07-03-select-output.4cf1a0e645baea1f.webp)

2. Izberite **Next**.

3. Izberite **Register**.

    ![Izberite registracijo.](../../../../../../translated_images/sl/07-04-register.fd82a3b293060bc7.webp)

4. Registrirani model si lahko ogledate tako, da v levem zavihku izberete meni **Models**.

    ![Registrirani model.](../../../../../../translated_images/sl/07-05-registered-model.7db9775f58dfd591.webp)

#### Namestitev dodatno usposobljenega modela

1. Pojdite v Azure Machine Learning delovno okolje, ki ste ga ustvarili.

1. Izberite **Endpoints** v levem zavihku.

1. Izberite **Real-time endpoints** v navigacijskem meniju.

    ![Ustvarjanje točke.](../../../../../../translated_images/sl/07-06-create-endpoint.1ba865c606551f09.webp)

1. Izberite **Create**.

1. Izberite registrirani model, ki ste ga ustvarili.

    ![Izberite registriran model.](../../../../../../translated_images/sl/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Izberite **Select**.

1. Izvedite naslednje naloge:

    - Izberite **Virtualno napravo** na *Standard_NC6s_v3*.
    - Nastavite **Število instanc**, ki jih želite uporabiti, na primer *1*.
    - Izberite **Endpoint** na **New** za ustvarjanje točke.
    - Vnesite **Ime točke**. Mora biti edinstvena vrednost.
    - Vnesite **Ime namestitve**. Mora biti edinstvena vrednost.

    ![Izpolnite nastavitve namestitve.](../../../../../../translated_images/sl/07-08-deployment-setting.43ddc4209e673784.webp)

1. Izberite **Deploy**.

> [!WARNING]
> Da se izognete dodatnim stroškom na vašem računu, obvezno izbrišite ustvarjeno točko v Azure Machine Learning delovnem okolju.
>

#### Preverjanje stanja namestitve v Azure Machine Learning delovnem okolju

1. Pojdite v Azure Machine Learning delovno okolje, ki ste ga ustvarili.

1. Izberite **Endpoints** v levem zavihku.

1. Izberite točko, ki ste jo ustvarili.

    ![Izberite točke](../../../../../../translated_images/sl/07-09-check-deployment.325d18cae8475ef4.webp)

1. Na tej strani lahko upravljate z endpointi med procesom namestitve.

> [!NOTE]
> Ko je namestitev zaključena, se prepričajte, da je **Promet v živo** nastavljen na **100 %**. Če ni, izberite **Update traffic** za prilagoditev nastavitev prometa. Upoštevajte, da model ne morete testirati, če je promet nastavljen na 0 %.
>
> ![Nastavite promet.](../../../../../../translated_images/sl/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Scenarij 3: Integracija s Prompt flow in klepet z vašim prilagojenim modelom v Microsoft Foundry

### Integracija prilagojenega modela Phi-3 s Prompt flow

Po uspešni namestitvi vašega dodatno usposobljenega modela ga lahko zdaj integrirate s Prompt Flow, da uporabite svoj model v realnočasnih aplikacijah, kar omogoča različne interaktivne naloge z vašim prilagojenim modelom Phi-3.

V tej vaji boste:

- Ustvarili Microsoft Foundry Hub.
- Ustvarili Microsoft Foundry Projekt.
- Ustvarili Prompt flow.
- Dodali prilagojeno povezavo za dodatno usposobljen model Phi-3.
- Nastavili Prompt flow za klepet z vašim prilagojenim modelom Phi-3.

> [!NOTE]
> Prav tako lahko integrirate s Promptflow z uporabo Azure ML Studio. Enak postopek integracije lahko uporabite tudi za Azure ML Studio.

#### Ustvarite Microsoft Foundry Hub

Preden ustvarite Projekt, morate ustvariti Hub. Hub deluje kot skupina virov, ki vam omogoča organizacijo in upravljanje več projektov znotraj Microsoft Foundry.
1. Obiščite [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Izberite **Vsi vozli** v levem stranskem zavihku.

1. Izberite **+ Novo vozlišče** v navigacijskem meniju.

    ![Ustvari vozlišče.](../../../../../../translated_images/sl/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Izvedite naslednje naloge:

    - Vnesite **Ime vozlišča**. Morala bi biti edinstvena vrednost.
    - Izberite svoj Azure **Naročnino**.
    - Izberite **Skupino virov**, ki jo želite uporabiti (če je potrebno, ustvarite novo).
    - Izberite **Lokacijo**, ki jo želite uporabiti.
    - Izberite **Poveži Azure AI Services**, ki jih želite uporabiti (če je potrebno, ustvarite nove).
    - Izberite **Poveži Azure AI Search** na **Preskoči povezavo**.

    ![Izpolnite vozlišče.](../../../../../../translated_images/sl/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Izberite **Naprej**.

#### Ustvarite Microsoft Foundry projekt

1. V vozlišču, ki ste ga ustvarili, izberite **Vsi projekti** v levem stranskem zavihku.

1. Izberite **+ Nov projekt** v navigacijskem meniju.

    ![Izberite nov projekt.](../../../../../../translated_images/sl/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Vnesite **Ime projekta**. Morala bi biti edinstvena vrednost.

    ![Ustvari projekt.](../../../../../../translated_images/sl/08-05-create-project.4d97f0372f03375a.webp)

1. Izberite **Ustvari projekt**.

#### Dodajte lastno povezavo za fine-tuned model Phi-3

Za integracijo vašega lastnega modela Phi-3 s Prompt flow morate shraniti končno točko in ključ modela v lastno povezavo. Ta nastavitev zagotavlja dostop do vašega lastnega modela Phi-3 v Prompt flow.

#### Nastavite api ključ in uri končne točke fine-tuned modela Phi-3

1. Obiščite [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Pomaknite se do Azure Machine learning delovnega prostora, ki ste ga ustvarili.

1. Izberite **Končne točke** v levem stranskem zavihku.

    ![Izberite končne točke.](../../../../../../translated_images/sl/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Izberite končno točko, ki ste jo ustvarili.

    ![Izberite ustvarjeno končno točko.](../../../../../../translated_images/sl/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Izberite **Uporabi** v navigacijskem meniju.

1. Kopirajte svojo **REST končno točko** in **Primarni ključ**.

    ![Kopirajte api ključ in uri končne točke.](../../../../../../translated_images/sl/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Dodajte lastno povezavo

1. Obiščite [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Pomaknite se do Microsoft Foundry projekta, ki ste ga ustvarili.

1. V projektu, ki ste ga ustvarili, izberite **Nastavitve** v levem stranskem zavihku.

1. Izberite **+ Nova povezava**.

    ![Izberite novo povezavo.](../../../../../../translated_images/sl/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Izberite **Lastni ključi** v navigacijskem meniju.

    ![Izberite lastne ključe.](../../../../../../translated_images/sl/08-10-select-custom-keys.856f6b2966460551.webp)

1. Izvedite naslednje naloge:

    - Izberite **+ Dodaj par ključa in vrednosti**.
    - Za ime ključa vnesite **endpoint** in prilepite končno točko, ki ste jo kopirali iz Azure ML Studio, v polje za vrednost.
    - Izberite **+ Dodaj par ključa in vrednosti** ponovno.
    - Za ime ključa vnesite **key** in prilepite ključ, ki ste ga kopirali iz Azure ML Studio, v polje za vrednost.
    - Po dodajanju ključev izberite **je skrivnost**, da preprečite izpostavljanje ključa.

    ![Dodajte povezavo.](../../../../../../translated_images/sl/08-11-add-connection.785486badb4d2d26.webp)

1. Izberite **Dodaj povezavo**.

#### Ustvarite Prompt flow

Dodali ste lastno povezavo v Microsoft Foundry. Zdaj ustvarimo Prompt flow z naslednjimi koraki. Nato boste to Prompt flow povezali z lastno povezavo, da boste lahko uporabljali fine-tuned model znotraj Prompt flow.

1. Pomaknite se do Microsoft Foundry projekta, ki ste ga ustvarili.

1. Izberite **Prompt flow** v levem stranskem zavihku.

1. Izberite **+ Ustvari** v navigacijskem meniju.

    ![Izberite Promptflow.](../../../../../../translated_images/sl/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Izberite **Chat flow** v navigacijskem meniju.

    ![Izberite chat flow.](../../../../../../translated_images/sl/08-13-select-flow-type.2ec689b22da32591.webp)

1. Vnesite **Ime mape**, ki jo želite uporabiti.

    ![Vnesite ime.](../../../../../../translated_images/sl/08-14-enter-name.ff9520fefd89f40d.webp)

2. Izberite **Ustvari**.

#### Nastavite Prompt flow za klepet z vašim lastnim Phi-3 modelom

Potrebno je integrirati fine-tuned model Phi-3 v Prompt flow. Vendar pa obstoječi Prompt flow ni zasnovan za ta namen, zato morate prenoviti Prompt flow, da omogočite integracijo lastnega modela.

1. V Prompt flow izvedite naslednje naloge za prenovo obstoječega toka:

    - Izberite **Način surove datoteke**.
    - Izbrišite vso obstoječo kodo v datoteki *flow.dag.yml*.
    - Dodajte naslednjo kodo v datoteko *flow.dag.yml*.

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

    - Izberite **Shrani**.

    ![Izberite način surove datoteke.](../../../../../../translated_images/sl/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Dodajte naslednjo kodo v datoteko *integrate_with_promptflow.py*, da uporabite lastni model Phi-3 v Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Nastavitev beleženja
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

        # "connection" je ime po meri vzpostavljene povezave, "endpoint", "key" so ključi v po meri vzpostavljeni povezavi
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
            
            # Zabeleži celoten JSON odgovor
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

    ![Prilepite kodo za prompt flow.](../../../../../../translated_images/sl/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Za podrobnejše informacije o uporabi Prompt flow v Microsoft Foundry si oglejte [Prompt flow v Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Izberite **Vhod klepeta**, **Izhod klepeta**, da omogočite klepet z vašim modelom.

    ![Vhod Izhod.](../../../../../../translated_images/sl/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Zdaj ste pripravljeni za klepet z vašim lastnim modelom Phi-3. V naslednji vaji boste spoznali, kako zagnati Prompt flow in ga uporabiti za klepet z vašim fine-tuned modelom Phi-3.

> [!NOTE]
>
> Prenovljen tok bi moral izgledati kot na spodnji sliki:
>
> ![Primer toka.](../../../../../../translated_images/sl/08-18-graph-example.d6457533952e690c.webp)
>

### Klepetajte z vašim lastnim modelom Phi-3

Zdaj, ko ste fine-tunali in integrirali vaš lastni model Phi-3 s Prompt flow, ste pripravljeni za začetek interakcije z njim. Ta vaja vas bo vodila skozi postopek nastavitve in začetka klepeta z vašim modelom z uporabo Prompt flow. Sledi tem korakom, da boste lahko v celoti izkoristili zmogljivosti vašega fine-tuned modela Phi-3 za različne naloge in pogovore.

- Klepetajte z vašim lastnim modelom Phi-3 z uporabo Prompt flow.

#### Začnite Prompt flow

1. Izberite **Zaženi seje izračuna**, da začnete Prompt flow.

    ![Začni sejo izračuna.](../../../../../../translated_images/sl/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Izberite **Potrdi in razčleni vhod**, da osvežite parametre.

    ![Potrdi vhod.](../../../../../../translated_images/sl/09-02-validate-input.317c76ef766361e9.webp)

1. Izberite vrednost **povezave** za lastno povezavo, ki ste jo ustvarili. Na primer, *povezava*.

    ![Povezava.](../../../../../../translated_images/sl/09-03-select-connection.99bdddb4b1844023.webp)

#### Klepetajte z vašim lastnim modelom

1. Izberite **Klepet**.

    ![Izberite klepet.](../../../../../../translated_images/sl/09-04-select-chat.61936dce6612a1e6.webp)

1. Tukaj je primer rezultatov: Zdaj lahko klepetate z vašim lastnim modelom Phi-3. Priporočljivo je, da postavljate vprašanja na podlagi podatkov, uporabljenih za fine-tuning.

    ![Klepet z prompt flow.](../../../../../../translated_images/sl/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o omejitvi odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v izvorni jezik se šteje za avtoritativni vir. Za kritične informacije priporočamo profesionalni človeški prevod. Nismo odgovorni za kakršno koli nesporazumevanje ali napačno razlago, ki izhaja iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->