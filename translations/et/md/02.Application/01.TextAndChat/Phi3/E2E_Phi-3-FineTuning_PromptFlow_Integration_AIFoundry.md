<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-10-11T12:01:31+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "et"
}
-->
# Kohanda ja integreeri kohandatud Phi-3 mudelid Prompt flow'ga Azure AI Foundry's

See algusest lõpuni (E2E) näidis põhineb juhendil "[Kohanda ja integreeri kohandatud Phi-3 mudelid Prompt flow'ga Azure AI Foundry's](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" Microsoft Tech Community's. Juhend tutvustab protsesse, mis hõlmavad mudelite kohandamist, juurutamist ja integreerimist Prompt flow'ga Azure AI Foundry's. 
Erinevalt E2E näidisest "[Kohanda ja integreeri kohandatud Phi-3 mudelid Prompt flow'ga](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", mis hõlmas koodi käivitamist lokaalselt, keskendub see juhend täielikult mudeli kohandamisele ja integreerimisele Azure AI / ML Studio's.

## Ülevaade

Selles E2E näidises õpid, kuidas kohandada Phi-3 mudelit ja integreerida seda Prompt flow'ga Azure AI Foundry's. Kasutades Azure AI / ML Studio't, loome töövoo kohandatud AI mudelite juurutamiseks ja kasutamiseks. Näidis jaguneb kolme stsenaariumi:

**Stsenaarium 1: Azure'i ressursside seadistamine ja ettevalmistus kohandamiseks**

**Stsenaarium 2: Phi-3 mudeli kohandamine ja juurutamine Azure Machine Learning Studio's**

**Stsenaarium 3: Integreerimine Prompt flow'ga ja vestlus kohandatud mudeliga Azure AI Foundry's**

Siin on selle E2E näidise ülevaade.

![Phi-3-FineTuning_PromptFlow_Integration Ülevaade.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/00-01-architecture.png)

### Sisukord

1. **[Stsenaarium 1: Azure'i ressursside seadistamine ja ettevalmistus kohandamiseks](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning tööruumi loomine](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [GPU kvootide taotlemine Azure'i tellimuses](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Rolli määramine](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Projekti seadistamine](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Andmestiku ettevalmistamine kohandamiseks](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Stsenaarium 2: Phi-3 mudeli kohandamine ja juurutamine Azure Machine Learning Studio's](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3 mudeli kohandamine](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Kohandatud Phi-3 mudeli juurutamine](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Stsenaarium 3: Integreerimine Prompt flow'ga ja vestlus kohandatud mudeliga Azure AI Foundry's](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Kohandatud Phi-3 mudeli integreerimine Prompt flow'ga](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Vestlus kohandatud Phi-3 mudeliga](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Stsenaarium 1: Azure'i ressursside seadistamine ja ettevalmistus kohandamiseks

### Azure Machine Learning tööruumi loomine

1. Sisesta **azure machine learning** portaali lehe ülaosas asuvasse **otsinguribasse** ja vali kuvatavatest valikutest **Azure Machine Learning**.

    ![Sisesta azure machine learning.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/01-01-type-azml.png)

2. Vali navigeerimismenüüst **+ Create**.

3. Vali navigeerimismenüüst **New workspace**.

    ![Vali uus tööruum.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/01-02-select-new-workspace.png)

4. Täida järgmised ülesanded:

    - Vali oma Azure'i **Subscription**.
    - Vali **Resource group**, mida kasutada (loo uus, kui vaja).
    - Sisesta **Workspace Name**. See peab olema unikaalne väärtus.
    - Vali **Region**, mida soovid kasutada.
    - Vali **Storage account**, mida kasutada (loo uus, kui vaja).
    - Vali **Key vault**, mida kasutada (loo uus, kui vaja).
    - Vali **Application insights**, mida kasutada (loo uus, kui vaja).
    - Vali **Container registry**, mida kasutada (loo uus, kui vaja).

    ![Täida Azure Machine Learning.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/01-03-fill-AZML.png)

5. Vali **Review + Create**.

6. Vali **Create**.

### GPU kvootide taotlemine Azure'i tellimuses

Selles juhendis õpid, kuidas kohandada ja juurutada Phi-3 mudelit, kasutades GPU-sid. Kohandamiseks kasutatakse *Standard_NC24ads_A100_v4* GPU-d, mis nõuab kvoodi taotlust. Juurutamiseks kasutatakse *Standard_NC6s_v3* GPU-d, mis samuti nõuab kvoodi taotlust.

> [!NOTE]
>
> GPU eraldamine on saadaval ainult Pay-As-You-Go tellimuste puhul (standardne tellimustüüp); soodustellimused ei ole praegu toetatud.
>

1. Külasta [Azure ML Studio't](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Täida järgmised ülesanded, et taotleda *Standard NCADSA100v4 Family* kvooti:

    - Vali vasakpoolsest menüüst **Quota**.
    - Vali **Virtual machine family**, mida kasutada. Näiteks vali **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, mis sisaldab *Standard_NC24ads_A100_v4* GPU-d.
    - Vali navigeerimismenüüst **Request quota**.

        ![Taotle kvooti.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/02-02-request-quota.png)

    - Sisesta **New cores limit**, mida soovid kasutada. Näiteks 24.
    - Vali **Submit**, et taotleda GPU kvooti.

1. Täida järgmised ülesanded, et taotleda *Standard NCSv3 Family* kvooti:

    - Vali vasakpoolsest menüüst **Quota**.
    - Vali **Virtual machine family**, mida kasutada. Näiteks vali **Standard NCSv3 Family Cluster Dedicated vCPUs**, mis sisaldab *Standard_NC6s_v3* GPU-d.
    - Vali navigeerimismenüüst **Request quota**.
    - Sisesta **New cores limit**, mida soovid kasutada. Näiteks 24.
    - Vali **Submit**, et taotleda GPU kvooti.

### Rolli määramine

Mudelite kohandamiseks ja juurutamiseks tuleb esmalt luua Kasutaja Määratud Hallatav Identiteet (UAI) ja määrata sellele sobivad õigused. Seda UAI-d kasutatakse autentimiseks juurutamise ajal.

#### Kasutaja Määratud Hallatava Identiteedi (UAI) loomine

1. Sisesta **managed identities** portaali lehe ülaosas asuvasse **otsinguribasse** ja vali kuvatavatest valikutest **Managed Identities**.

    ![Sisesta managed identities.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-01-type-managed-identities.png)

1. Vali **+ Create**.

    ![Vali loo.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-02-select-create.png)

1. Täida järgmised ülesanded:

    - Vali oma Azure'i **Subscription**.
    - Vali **Resource group**, mida kasutada (loo uus, kui vaja).
    - Vali **Region**, mida soovid kasutada.
    - Sisesta **Name**. See peab olema unikaalne väärtus.

    ![Täida managed identities.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-03-fill-managed-identities-1.png)

1. Vali **Review + create**.

1. Vali **+ Create**.

#### Lisa Contributor rolli määramine Hallatavale Identiteedile

1. Navigeeri loodud Hallatava Identiteedi ressursile.

1. Vali vasakpoolsest menüüst **Azure role assignments**.

1. Vali navigeerimismenüüst **+Add role assignment**.

1. Rolli määramise lehel täida järgmised ülesanded:
    - Vali **Scope** **Resource group**.
    - Vali oma Azure'i **Subscription**.
    - Vali **Resource group**, mida kasutada.
    - Vali **Role** **Contributor**.

    ![Täida Contributor roll.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-04-fill-contributor-role.png)

2. Vali **Save**.

#### Lisa Storage Blob Data Reader rolli määramine Hallatavale Identiteedile

1. Sisesta **storage accounts** portaali lehe ülaosas asuvasse **otsinguribasse** ja vali kuvatavatest valikutest **Storage accounts**.

    ![Sisesta storage accounts.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-05-type-storage-accounts.png)

1. Vali Azure Machine Learning tööruumiga seotud salvestuskonto. Näiteks *finetunephistorage*.

1. Täida järgmised ülesanded, et navigeerida Rolli määramise lehele:

    - Navigeeri loodud Azure'i salvestuskontole.
    - Vali vasakpoolsest menüüst **Access Control (IAM)**.
    - Vali navigeerimismenüüst **+ Add**.
    - Vali navigeerimismenüüst **Add role assignment**.

    ![Lisa roll.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-06-add-role.png)

1. Rolli määramise lehel täida järgmised ülesanded:

    - Rolli lehel sisesta **Storage Blob Data Reader** otsinguribasse ja vali kuvatavatest valikutest **Storage Blob Data Reader**.
    - Rolli lehel vali **Next**.
    - Liikmete lehel vali **Assign access to** **Managed identity**.
    - Liikmete lehel vali **+ Select members**.
    - Hallatavate identiteetide valimise lehel vali oma Azure'i **Subscription**.
    - Hallatavate identiteetide valimise lehel vali **Managed identity** **Manage Identity**.
    - Hallatavate identiteetide valimise lehel vali loodud Hallatav Identiteet. Näiteks *finetunephi-managedidentity*.
    - Hallatavate identiteetide valimise lehel vali **Select**.

    ![Vali managed identity.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-08-select-managed-identity.png)

1. Vali **Review + assign**.

#### Lisa AcrPull rolli määramine Hallatavale Identiteedile

1. Sisesta **container registries** portaali lehe ülaosas asuvasse **otsinguribasse** ja vali kuvatavatest valikutest **Container registries**.

    ![Sisesta container registries.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/03-09-type-container-registries.png)

1. Vali Azure Machine Learning tööruumiga seotud konteineriregister. Näiteks *finetunephicontainerregistry*.

1. Täida järgmised ülesanded, et navigeerida Rolli määramise lehele:

    - Vali vasakpoolsest menüüst **Access Control (IAM)**.
    - Vali navigeerimismenüüst **+ Add**.
    - Vali navigeerimismenüüst **Add role assignment**.

1. Rolli määramise lehel täida järgmised ülesanded:

    - Rolli lehel sisesta **AcrPull** otsinguribasse ja vali kuvatavatest valikutest **AcrPull**.
    - Rolli lehel vali **Next**.
    - Liikmete lehel vali **Assign access to** **Managed identity**.
    - Liikmete lehel vali **+ Select members**.
    - Hallatavate identiteetide valimise lehel vali oma Azure'i **Subscription**.
    - Hallatavate identiteetide valimise lehel vali **Managed identity** **Manage Identity**.
    - Hallatavate identiteetide valimise lehel vali loodud Hallatav Identiteet. Näiteks *finetunephi-managedidentity*.
    - Hallatavate identiteetide valimise lehel vali **Select**.
    - Vali **Review + assign**.

### Projekti seadistamine

Andmestike allalaadimiseks, mida on vaja kohandamiseks, seadistame lokaalse keskkonna.

Selles harjutuses:

- Loome kausta, kus töötada.
- Loome virtuaalse keskkonna.
- Installime vajalikud paketid.
- Loome *download_dataset.py* faili andmestiku allalaadimiseks.

#### Loome kausta, kus töötada

1. Ava terminaliaken ja sisesta järgmine käsk, et luua kaust nimega *finetune-phi* vaikimisi asukohta.

    ```console
    mkdir finetune-phi
    ```

2. Sisesta oma terminali järgmine käsk, et liikuda *finetune-phi* kausta, mille sa lõid.

    ```console
    cd finetune-phi
    ```

#### Loo virtuaalne keskkond

1. Sisesta oma terminali järgmine käsk, et luua virtuaalne keskkond nimega *.venv*.

    ```console
    python -m venv .venv
    ```

2. Sisesta oma terminali järgmine käsk, et aktiveerida virtuaalne keskkond.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Kui see õnnestus, peaksid nägema *(.venv)* käsurea ees.

#### Paigalda vajalikud paketid

1. Sisesta oma terminali järgmised käsud, et paigaldada vajalikud paketid.

    ```console
    pip install datasets==2.19.1
    ```

#### Loo `download_dataset.py`

> [!NOTE]
> Täielik kaustastruktuur:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Ava **Visual Studio Code**.

1. Vali menüüribalt **File**.

1. Vali **Open Folder**.

1. Vali *finetune-phi* kaust, mille sa lõid ja mis asub *C:\Users\yourUserName\finetune-phi*.

    ![Vali kaust, mille sa lõid.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/04-01-open-project-folder.png)

1. Visual Studio Code'i vasakus paneelis klõpsa paremklõpsuga ja vali **New File**, et luua uus fail nimega *download_dataset.py*.

    ![Loo uus fail.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/04-02-create-new-file.png)

### Valmista andmestik peenhäälestamiseks

Selles harjutuses käivitatakse *download_dataset.py* fail, et laadida *ultrachat_200k* andmestikud kohalikku keskkonda. Seejärel kasutatakse neid andmestikke Phi-3 mudeli peenhäälestamiseks Azure Machine Learningus.

Selles harjutuses:

- Lisad koodi *download_dataset.py* faili, et andmestikud alla laadida.
- Käivitatakse *download_dataset.py* fail, et andmestikud kohalikku keskkonda alla laadida.

#### Laadi oma andmestik *download_dataset.py* abil

1. Ava *download_dataset.py* fail Visual Studio Code'is.

1. Lisa järgmine kood *download_dataset.py* faili.

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

1. Sisesta oma terminali järgmine käsk, et skript käivitada ja andmestik kohalikku keskkonda alla laadida.

    ```console
    python download_dataset.py
    ```

1. Kontrolli, et andmestikud salvestati edukalt kohalikku *finetune-phi/data* kataloogi.

> [!NOTE]
>
> #### Märkus andmestiku suuruse ja peenhäälestamise aja kohta
>
> Selles juhendis kasutatakse ainult 1% andmestikust (`split='train[:1%]'`). See vähendab oluliselt andmete mahtu, kiirendades nii üleslaadimist kui ka peenhäälestamise protsessi. Protsendi kohandamine aitab leida tasakaalu treeningu aja ja mudeli jõudluse vahel. Väiksema andmestiku kasutamine muudab peenhäälestamise protsessi juhendi jaoks hallatavaks.

## Stsenaarium 2: Phi-3 mudeli peenhäälestamine ja juurutamine Azure Machine Learning Studios

### Phi-3 mudeli peenhäälestamine

Selles harjutuses peenhäälestatakse Phi-3 mudel Azure Machine Learning Studios.

Selles harjutuses:

- Luuakse arvutuskobar peenhäälestamiseks.
- Peenhäälestatakse Phi-3 mudel Azure Machine Learning Studios.

#### Loo arvutuskobar peenhäälestamiseks

1. Külasta [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vali vasakult menüüst **Compute**.

1. Vali navigeerimismenüüst **Compute clusters**.

1. Vali **+ New**.

    ![Vali arvutus.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-01-select-compute.png)

1. Tee järgmised toimingud:

    - Vali **Region**, mida soovid kasutada.
    - Vali **Virtual machine tier** väärtuseks **Dedicated**.
    - Vali **Virtual machine type** väärtuseks **GPU**.
    - Vali **Virtual machine size** filtriks **Select from all options**.
    - Vali **Virtual machine size** väärtuseks **Standard_NC24ads_A100_v4**.

    ![Loo kobar.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-02-create-cluster.png)

1. Vali **Next**.

1. Tee järgmised toimingud:

    - Sisesta **Compute name**. See peab olema unikaalne väärtus.
    - Vali **Minimum number of nodes** väärtuseks **0**.
    - Vali **Maximum number of nodes** väärtuseks **1**.
    - Vali **Idle seconds before scale down** väärtuseks **120**.

    ![Loo kobar.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-03-create-cluster.png)

1. Vali **Create**.

#### Phi-3 mudeli peenhäälestamine

1. Külasta [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vali Azure Machine Learning tööruum, mille sa lõid.

    ![Vali tööruum, mille sa lõid.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-04-select-workspace.png)

1. Tee järgmised toimingud:

    - Vali vasakult menüüst **Model catalog**.
    - Sisesta **search bar** otsingusse *phi-3-mini-4k* ja vali kuvatud valikutest **Phi-3-mini-4k-instruct**.

    ![Sisesta phi-3-mini-4k.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-05-type-phi-3-mini-4k.png)

1. Vali navigeerimismenüüst **Fine-tune**.

    ![Vali peenhäälestamine.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-06-select-fine-tune.png)

1. Tee järgmised toimingud:

    - Vali **Select task type** väärtuseks **Chat completion**.
    - Vali **+ Select data**, et üles laadida **Training data**.
    - Vali valideerimisandmete üleslaadimise tüübiks **Provide different validation data**.
    - Vali **+ Select data**, et üles laadida **Validation data**.

    ![Täida peenhäälestamise leht.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-07-fill-finetuning.png)

    > [!TIP]
    >
    > Saad valida **Advanced settings**, et kohandada konfiguratsioone nagu **learning_rate** ja **lr_scheduler_type**, et optimeerida peenhäälestamise protsessi vastavalt oma vajadustele.

1. Vali **Finish**.

1. Selles harjutuses peenhäälestati edukalt Phi-3 mudel Azure Machine Learningus. Pane tähele, et peenhäälestamise protsess võib võtta märkimisväärselt aega. Pärast peenhäälestamise töö käivitamist tuleb oodata selle lõpuleviimist. Töö edenemist saab jälgida, navigeerides Azure Machine Learning tööruumi vasakult menüüst **Jobs** vahekaardile. Järgmises osas juurutatakse peenhäälestatud mudel ja integreeritakse see Prompt flow'ga.

    ![Vaata peenhäälestamise tööd.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-08-output.png)

### Juuruta peenhäälestatud Phi-3 mudel

Et integreerida peenhäälestatud Phi-3 mudel Prompt flow'ga, tuleb mudel juurutada, et see oleks reaalajas päringuteks kättesaadav. See protsess hõlmab mudeli registreerimist, veebipõhise lõpp-punkti loomist ja mudeli juurutamist.

Selles harjutuses:

- Registreeritakse peenhäälestatud mudel Azure Machine Learning tööruumis.
- Luakse veebipõhine lõpp-punkt.
- Juurutatakse registreeritud peenhäälestatud Phi-3 mudel.

#### Registreeri peenhäälestatud mudel

1. Külasta [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vali Azure Machine Learning tööruum, mille sa lõid.

    ![Vali tööruum, mille sa lõid.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/06-04-select-workspace.png)

1. Vali vasakult menüüst **Models**.
1. Vali **+ Register**.
1. Vali **From a job output**.

    ![Registreeri mudel.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-01-register-model.png)

1. Vali töö, mille sa lõid.

    ![Vali töö.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-02-select-job.png)

1. Vali **Next**.

1. Vali **Model type** väärtuseks **MLflow**.

1. Veendu, et **Job output** on valitud; see peaks olema automaatselt valitud.

    ![Vali väljund.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-03-select-output.png)

2. Vali **Next**.

3. Vali **Register**.

    ![Vali registreerimine.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-04-register.png)

4. Registreeritud mudelit saab vaadata, navigeerides vasakult menüüst **Models** menüüsse.

    ![Registreeritud mudel.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-05-registered-model.png)

#### Juuruta peenhäälestatud mudel

1. Navigeeri Azure Machine Learning tööruumi, mille sa lõid.

1. Vali vasakult menüüst **Endpoints**.

1. Vali navigeerimismenüüst **Real-time endpoints**.

    ![Loo lõpp-punkt.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-06-create-endpoint.png)

1. Vali **Create**.

1. Vali registreeritud mudel, mille sa lõid.

    ![Vali registreeritud mudel.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-07-select-registered-model.png)

1. Vali **Select**.

1. Tee järgmised toimingud:

    - Vali **Virtual machine** väärtuseks *Standard_NC6s_v3*.
    - Vali **Instance count**, mida soovid kasutada, näiteks *1*.
    - Vali **Endpoint** väärtuseks **New**, et luua lõpp-punkt.
    - Sisesta **Endpoint name**. See peab olema unikaalne väärtus.
    - Sisesta **Deployment name**. See peab olema unikaalne väärtus.

    ![Täida juurutamise seaded.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-08-deployment-setting.png)

1. Vali **Deploy**.

> [!WARNING]
> Et vältida täiendavaid kulusid oma kontole, veendu, et kustutad loodud lõpp-punkti Azure Machine Learning tööruumis.
>

#### Kontrolli juurutamise staatust Azure Machine Learning tööruumis

1. Navigeeri Azure Machine Learning tööruumi, mille sa lõid.

1. Vali vasakult menüüst **Endpoints**.

1. Vali lõpp-punkt, mille sa lõid.

    ![Vali lõpp-punktid](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-09-check-deployment.png)

1. Sellel lehel saad hallata lõpp-punkte juurutamise protsessi ajal.

> [!NOTE]
> Kui juurutamine on lõpule viidud, veendu, et **Live traffic** on seatud väärtuseks **100%**. Kui see ei ole, vali **Update traffic**, et liiklusseadeid kohandada. Pane tähele, et mudelit ei saa testida, kui liiklus on seatud väärtuseks 0%.
>
> ![Sea liiklus.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/07-10-set-traffic.png)
>

## Stsenaarium 3: Integreeri Prompt flow'ga ja vestle oma kohandatud mudeliga Azure AI Foundry's

### Integreeri kohandatud Phi-3 mudel Prompt flow'ga

Pärast peenhäälestatud mudeli edukat juurutamist saad selle nüüd integreerida Prompt flow'ga, et kasutada mudelit reaalajas rakendustes, võimaldades mitmesuguseid interaktiivseid ülesandeid oma kohandatud Phi-3 mudeliga.

Selles harjutuses:

- Loo Azure AI Foundry Hub.
- Loo Azure AI Foundry Project.
- Loo Prompt flow.
- Lisa kohandatud ühendus peenhäälestatud Phi-3 mudelile.
- Sea üles Prompt flow, et vestelda oma kohandatud Phi-3 mudeliga.

> [!NOTE]
> Promptflow'ga saab integreerida ka Azure ML Studio kaudu. Sama integreerimisprotsessi saab rakendada Azure ML Studios.

#### Loo Azure AI Foundry Hub

Enne projekti loomist tuleb luua Hub. Hub toimib nagu ressursigrupp, võimaldades hallata ja organiseerida mitut projekti Azure AI Foundry's.

1. Külasta [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Vali vasakult menüüst **All hubs**.

1. Vali navigeerimismenüüst **+ New hub**.
![Loo hub.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-01-create-hub.png)

1. Tehke järgmised toimingud:

   - Sisestage **Hubi nimi**. See peab olema unikaalne väärtus.
   - Valige oma Azure'i **Tellijaplaan**.
   - Valige kasutatav **Ressursigrupp** (vajadusel looge uus).
   - Valige **Asukoht**, mida soovite kasutada.
   - Valige kasutatav **Ühendage Azure AI teenused** (vajadusel looge uus).
   - Valige **Ühendage Azure AI otsing** ja **Jätke ühendamata**.

   ![Täida hub.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-02-fill-hub.png)

1. Valige **Järgmine**.

#### Loo Azure AI Foundry projekt

1. Valige loodud hubis vasakpoolsest menüüst **Kõik projektid**.

1. Valige navigeerimismenüüst **+ Uus projekt**.

   ![Vali uus projekt.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-04-select-new-project.png)

1. Sisestage **Projekti nimi**. See peab olema unikaalne väärtus.

   ![Loo projekt.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-05-create-project.png)

1. Valige **Loo projekt**.

#### Lisa kohandatud ühendus peenhäälestatud Phi-3 mudeli jaoks

Et integreerida oma kohandatud Phi-3 mudel Prompt flow'ga, peate salvestama mudeli lõpp-punkti ja võtme kohandatud ühendusse. See seadistus tagab juurdepääsu teie kohandatud Phi-3 mudelile Prompt flow's.

#### Määrake peenhäälestatud Phi-3 mudeli API-võti ja lõpp-punkti URI

1. Külastage [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Liikuge loodud Azure Machine Learning tööruumi.

1. Valige vasakpoolsest menüüst **Lõpp-punktid**.

   ![Vali lõpp-punktid.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-06-select-endpoints.png)

1. Valige loodud lõpp-punkt.

   ![Vali loodud lõpp-punkt.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-07-select-endpoint-created.png)

1. Valige navigeerimismenüüst **Kasutamine**.

1. Kopeerige oma **REST lõpp-punkt** ja **Primaarne võti**.

   ![Kopeeri API-võti ja lõpp-punkti URI.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-08-copy-endpoint-key.png)

#### Lisa kohandatud ühendus

1. Külastage [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Liikuge loodud Azure AI Foundry projekti.

1. Valige loodud projektis vasakpoolsest menüüst **Seaded**.

1. Valige **+ Uus ühendus**.

   ![Vali uus ühendus.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-09-select-new-connection.png)

1. Valige navigeerimismenüüst **Kohandatud võtmed**.

   ![Vali kohandatud võtmed.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-10-select-custom-keys.png)

1. Tehke järgmised toimingud:

   - Valige **+ Lisa võtme-väärtuse paarid**.
   - Sisestage võtme nimeks **endpoint** ja kleepige väärtuse väljale lõpp-punkt, mille kopeerisite Azure ML Studio'st.
   - Valige uuesti **+ Lisa võtme-väärtuse paarid**.
   - Sisestage võtme nimeks **key** ja kleepige väärtuse väljale võti, mille kopeerisite Azure ML Studio'st.
   - Pärast võtmete lisamist valige **on salajane**, et vältida võtme avalikustamist.

   ![Lisa ühendus.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-11-add-connection.png)

1. Valige **Lisa ühendus**.

#### Loo Prompt flow

Olete lisanud kohandatud ühenduse Azure AI Foundry's. Nüüd loome Prompt flow' ja ühendame selle kohandatud ühendusega, et saaksite kasutada peenhäälestatud mudelit Prompt flow's.

1. Liikuge loodud Azure AI Foundry projekti.

1. Valige vasakpoolsest menüüst **Prompt flow**.

1. Valige navigeerimismenüüst **+ Loo**.

   ![Vali Promptflow.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-12-select-promptflow.png)

1. Valige navigeerimismenüüst **Vestlusvoog**.

   ![Vali vestlusvoog.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-13-select-flow-type.png)

1. Sisestage kasutatav **Kausta nimi**.

   ![Sisesta nimi.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-14-enter-name.png)

2. Valige **Loo**.

#### Seadistage Prompt flow vestlemiseks oma kohandatud Phi-3 mudeliga

Te peate integreerima peenhäälestatud Phi-3 mudeli Prompt flow'ga. Kuid olemasolev Prompt flow ei ole selleks otstarbeks loodud. Seetõttu peate olemasoleva voogu ümber kujundama, et võimaldada kohandatud mudeli integreerimist.

1. Prompt flow's tehke järgmised toimingud, et olemasolev voog ümber ehitada:

   - Valige **Toores faili režiim**.
   - Kustutage kogu olemasolev kood *flow.dag.yml* failist.
   - Lisage järgmine kood *flow.dag.yml* faili.

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

   - Valige **Salvesta**.

   ![Vali toorfaili režiim.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-15-select-raw-file-mode.png)

1. Lisage järgmine kood *integrate_with_promptflow.py* faili, et kasutada kohandatud Phi-3 mudelit Prompt flow's.

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

   ![Kleebi prompt flow kood.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-16-paste-promptflow-code.png)

> [!NOTE]
> Täpsema teabe saamiseks Prompt flow kasutamise kohta Azure AI Foundry's vaadake [Prompt flow Azure AI Foundry's](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Valige **Vestluse sisend**, **Vestluse väljund**, et lubada vestlus oma mudeliga.

   ![Sisend Väljund.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-17-select-input-output.png)

1. Nüüd olete valmis vestlema oma kohandatud Phi-3 mudeliga. Järgmises harjutuses õpite, kuidas alustada Prompt flow'd ja kasutada seda oma peenhäälestatud Phi-3 mudeliga vestlemiseks.

> [!NOTE]
>
> Ümber ehitatud voog peaks välja nägema nagu alloleval pildil:
>
> ![Voo näide.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/08-18-graph-example.png)
>

### Vestlus oma kohandatud Phi-3 mudeliga

Nüüd, kui olete oma kohandatud Phi-3 mudeli peenhäälestanud ja integreerinud selle Prompt flow'ga, olete valmis alustama suhtlemist. See harjutus juhendab teid, kuidas seadistada ja alustada vestlust oma mudeliga, kasutades Prompt flow'd. Järgides neid samme, saate täielikult ära kasutada oma peenhäälestatud Phi-3 mudeli võimalusi erinevate ülesannete ja vestluste jaoks.

- Vestelge oma kohandatud Phi-3 mudeliga, kasutades Prompt flow'd.

#### Alustage Prompt flow'd

1. Valige **Käivita arvutusseansid**, et alustada Prompt flow'd.

   ![Käivita arvutusseanss.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-01-start-compute-session.png)

1. Valige **Kinnita ja parsi sisend**, et uuendada parameetreid.

   ![Kinnita sisend.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-02-validate-input.png)

1. Valige **ühenduse** **väärtus** kohandatud ühenduse jaoks, mille lõite. Näiteks *connection*.

   ![Ühendus.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-03-select-connection.png)

#### Vestlus oma kohandatud mudeliga

1. Valige **Vestlus**.

   ![Vali vestlus.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-04-select-chat.png)

1. Siin on näide tulemustest: Nüüd saate vestelda oma kohandatud Phi-3 mudeliga. Soovitatav on esitada küsimusi andmete põhjal, mida kasutati peenhäälestamiseks.

   ![Vestlus prompt flow'ga.](../../../../../../imgs/02/FineTuning-PromptFlow-AIFoundry/09-05-chat-with-promptflow.png)

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.