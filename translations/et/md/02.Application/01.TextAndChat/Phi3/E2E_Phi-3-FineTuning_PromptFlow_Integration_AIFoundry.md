# Kohanda ja integreeri kohandatud Phi-3 mudeleid Prompt flow’ga Microsoft Foundrys

See end-to-end (E2E) näidis põhineb juhendil "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" Microsoft Tech Community's. See tutvustab protsesse, kuidas kohandatud Phi-3 mudeleid lihvida, juurutada ja integreerida Prompt flow'ga Microsoft Foundrys.
Erinevalt E2E näidisest, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", mis hõlmas koodi lokaalset käivitamist, keskendub see juhend täielikult teie mudeli lihvimisele ja integreerimisele Azure AI / ML Studios.

## Ülevaade

Selles E2E näidises õpite, kuidas lihvida Phi-3 mudelit ja integreerida see Prompt flow’ga Microsoft Foundrys. Kasutades Azure AI / ML Studiod, loote töövoo kohandatud tehisintellekti mudelite juurutamiseks ja kasutamiseks. See E2E näidis jaguneb kolme stsenaariumiks:

**Stsenaarium 1: Azure’i ressursside seadistamine ja ettevalmistus lihvimiseks**

**Stsenaarium 2: Phi-3 mudeli lihvimine ja juurutamine Azure Machine Learning Studios**

**Stsenaarium 3: Integreerimine Prompt flow’ga ja vestlus oma kohandatud mudeliga Microsoft Foundrys**

Siin on ülevaade sellest E2E näidisest.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/et/00-01-architecture.198ba0f1ae6d841a.webp)

### Sisukord

1. **[Stsenaarium 1: Azure’i ressursside seadistamine ja ettevalmistus lihvimiseks](#stsenaarium-1-azure’i-ressursside-seadistamine-ja-ettevalmistus-lihvimiseks)**
    - [Loo Azure Machine Learning tööruum](#loo-azure-machine-learning-tööruum)
    - [Taotle GPU kvote Azure’i tellimuses](#taotle-gpu-kvote-azure’i-tellimuses)
    - [Lisa rolli määramine](#lisa-rolli-määramine)
    - [Sea üles projekt](#sea-projekt-üles)
    - [Valmista andmekogum lihvimiseks ette](#andmekogu-ettevalmistamine-täpsustamiseks)

1. **[Stsenaarium 2: Phi-3 mudeli lihvimine ja juurutamine Azure Machine Learning Studios](#stsenaarium-2-phi-3-mudeli-täpsustamine-ja-juurutamine-azure-machine-learning-studios)**
    - [Lihvi Phi-3 mudelit](#phi-3-mudeli-täpsustamine)
    - [Juuruta lihvitud Phi-3 mudel](#juurutage-täpsustatud-phi-3-mudel)

1. **[Stsenaarium 3: Integreerimine Prompt flow’ga ja vestlus oma kohandatud mudeliga Microsoft Foundrys](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Integreeri kohandatud Phi-3 mudel Prompt flow’ga](#kohandatud-phi-3-mudeli-integreerimine-prompt-flow’ga)
    - [Vesta oma kohandatud Phi-3 mudeliga](#suhtle-oma-kohandatud-phi-3-mudeliga)

## Stsenaarium 1: Azure’i ressursside seadistamine ja ettevalmistus lihvimiseks

### Loo Azure Machine Learning tööruum

1. Tippige *azure machine learning* portaalilehe ülaosas asuvasse **otsinguribale** ja valige kuvatavatest valikutest **Azure Machine Learning**.

    ![Type azure machine learning.](../../../../../../translated_images/et/01-01-type-azml.acae6c5455e67b4b.webp)

2. Valige navigeerimismenüüst **+ Create**.

3. Valige navigeerimismenüüst **New workspace**.

    ![Select new workspace.](../../../../../../translated_images/et/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Tehke järgmised toimingud:

    - Valige oma Azure’i **Subscription**.
    - Valige kasutatav **Resource group** (vajadusel looge uus).
    - Sisestage **Workspace Name**. See peab olema unikaalne väärtus.
    - Valige soovitud **Region**.
    - Valige kasutatav **Storage account** (vajadusel looge uus).
    - Valige kasutatav **Key vault** (vajadusel looge uus).
    - Valige kasutatav **Application insights** (vajadusel looge uus).
    - Valige kasutatav **Container registry** (vajadusel looge uus).

    ![Fill azure machine learning.](../../../../../../translated_images/et/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Valige **Review + Create**.

6. Valige **Create**.

### Taotle GPU kvote Azure’i tellimuses

Selles juhendis õpite, kuidas lihvida ja juurutada Phi-3 mudelit, kasutades GPU-sid. Lihvimiseks kasutate *Standard_NC24ads_A100_v4* GPU-d, mis vajab kvotitaotlust. Juurutamiseks kasutate *Standard_NC6s_v3* GPU-d, mis samuti vajab kvotitaotlust.

> [!NOTE]
>
> Ainult Pay-As-You-Go tellimused (tavapärane tellimuste tüüp) on GPU eraldamiseks sobivad; soodustellimused praegu ei toeta seda.
>

1. Külastage [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Järgige järgmisi samme *Standard NCADSA100v4 Family* kvoti taotlemiseks:

    - Valige vasakpoolsest vahekaardist **Quota**.
    - Valige kasutatav **Virtual machine family**. Näiteks valige **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, mis sisaldab *Standard_NC24ads_A100_v4* GPU-d.
    - Valige navigeerimismenüüst **Request quota**.

        ![Request quota.](../../../../../../translated_images/et/02-02-request-quota.c0428239a63ffdd5.webp)

    - Taotluslehel sisestage soovitav **New cores limit**. Näiteks 24.
    - Taotluslehel valige **Submit**, et esitada GPU kvoti taotlus.

1. Järgige järgmisi samme *Standard NCSv3 Family* kvoti taotlemiseks:

    - Valige vasakpoolsest vahekaardist **Quota**.
    - Valige kasutatav **Virtual machine family**. Näiteks valige **Standard NCSv3 Family Cluster Dedicated vCPUs**, mis sisaldab *Standard_NC6s_v3* GPU-d.
    - Valige navigeerimismenüüst **Request quota**.
    - Taotluslehel sisestage soovitav **New cores limit**. Näiteks 24.
    - Taotluslehel valige **Submit**, et esitada GPU kvoti taotlus.

### Lisa rolli määramine

Et lihvida ja juurutada oma mudeleid, peate esmalt looma kasutajale määratud hallatava identiteedi (UAI) ja määrama sellele sobivad õigused. Seda UAI-d kasutatakse autentimiseks juurutamise ajal.

#### Loo kasutajale määratud hallatav identiteet (UAI)

1. Tippige portaalilehe ülaosas otsinguribale *managed identities* ja valige kuvatavatest valikutest **Managed Identities**.

    ![Type managed identities.](../../../../../../translated_images/et/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Valige **+ Create**.

    ![Select create.](../../../../../../translated_images/et/03-02-select-create.92bf8989a5cd98f2.webp)

1. Tehke järgmised toimingud:

    - Valige oma Azure’i **Subscription**.
    - Valige kasutatav **Resource group** (vajadusel looge uus).
    - Valige soovitud **Region**.
    - Sisestage **Name**. See peab olema unikaalne väärtus.

    ![Select create.](../../../../../../translated_images/et/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Valige **Review + create**.

1. Valige **+ Create**.

#### Lisa hallatavale identiteedile Contributor rolli määramine

1. Liikuge loodud hallatava identiteedi ressursile.

1. Valige vasakpoolsest vahekaardist **Azure role assignments**.

1. Valige navigeerimismenüüst **+Add role assignment**.

1. Lehel Add role assignment tehke järgmised toimingud:
    - Valige **Scope** väärtuseks **Resource group**.
    - Valige oma Azure’i **Subscription**.
    - Valige kasutatav **Resource group**.
    - Valige **Role** väärtuseks **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/et/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Valige **Save**.

#### Lisa hallatavale identiteedile Storage Blob Data Reader rolli määramine

1. Tippige portaalilehe ülaosas otsinguribale *storage accounts* ja valige kuvatavatest valikutest **Storage accounts**.

    ![Type storage accounts.](../../../../../../translated_images/et/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Valige see salvestuskonto, mis on seotud loodud Azure Machine Learning tööruumiga. Näiteks *finetunephistorage*.

1. Järgige järgmisi samme, et jõuda Add role assignment lehele:

    - Avage loodud Azure Storage konto.
    - Valige vasakpoolsest vahekaardist **Access Control (IAM)**.
    - Valige navigeerimismenüüst **+ Add**.
    - Valige navigeerimismenüüst **Add role assignment**.

    ![Add role.](../../../../../../translated_images/et/03-06-add-role.353ccbfdcf0789c2.webp)

1. Lehel Add role assignment tehke järgmised toimingud:

    - Rolli lehel kirjutage otsinguribale *Storage Blob Data Reader* ja valige kuvatavatest valikutest **Storage Blob Data Reader**.
    - Rolli lehel valige **Next**.
    - Liikmete lehel valige **Assign access to** suvandiks **Managed identity**.
    - Liikmete lehel valige **+ Select members**.
    - Lehel Select managed identities valige oma Azure’i **Subscription**.
    - Lehel Select managed identities valige **Managed identity**.
    - Lehel Select managed identities valige loodud hallatav identiteet. Näiteks *finetunephi-managedidentity*.
    - Lehel Select managed identities valige **Select**.

    ![Select managed identity.](../../../../../../translated_images/et/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Valige **Review + assign**.

#### Lisa hallatavale identiteedile AcrPull rolli määramine

1. Tippige portaalilehe ülaosas otsinguribale *container registries* ja valige kuvatavatest valikutest **Container registries**.

    ![Type container registries.](../../../../../../translated_images/et/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Valige konteineriregister, mis on seotud Azure Machine Learning tööruumiga. Näiteks *finetunephicontainerregistry*.

1. Järgige järgmisi samme, et jõuda Add role assignment lehele:

    - Valige vasakpoolsest vahekaardist **Access Control (IAM)**.
    - Valige navigeerimismenüüst **+ Add**.
    - Valige navigeerimismenüüst **Add role assignment**.

1. Lehel Add role assignment tehke järgmised toimingud:

    - Rolli lehel kirjutage otsinguribale *AcrPull* ja valige kuvatavatest valikutest **AcrPull**.
    - Rolli lehel valige **Next**.
    - Liikmete lehel valige **Assign access to** suvandiks **Managed identity**.
    - Liikmete lehel valige **+ Select members**.
    - Lehel Select managed identities valige oma Azure’i **Subscription**.
    - Lehel Select managed identities valige **Managed identity**.
    - Lehel Select managed identities valige loodud hallatav identiteet. Näiteks *finetunephi-managedidentity*.
    - Lehel Select managed identities valige **Select**.
    - Valige **Review + assign**.

### Sea projekt üles

Selleks, et alla laadida lihvimiseks vajalikud andmekogumid, seadistate lokaalse keskkonna.

Selles harjutuses:

- Loote kausta, kus töötate.
- Loote virtuaalse keskkonna.
- Installite vajalikud paketid.
- Loote faili *download_dataset.py*, et andmekogum alla laadida.

#### Looge kaust, kus töötate

1. Avage terminaliakna ja tippige järgmine käsklus, et luua kaust nimega *finetune-phi* vaikeasukohta.

    ```console
    mkdir finetune-phi
    ```

2. Tippige terminalis järgmine käsklus, et liikuda loodud *finetune-phi* kausta.

    ```console
    cd finetune-phi
    ```

#### Looge virtuaalne keskkond

1. Tippige terminalis järgmine käsklus, et luua virtuaalne keskkond nimega *.venv*.
    ```console
    python -m venv .venv
    ```

2. Tippige oma terminali järgmine käsk virtuaalse keskkonna aktiveerimiseks.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Kui see õnnestus, peaksite nägema käsurea ees *(.venv)*.

#### Paigaldage vajalikud paketid

1. Tippige oma terminali järgmised käsud vajalike pakettide paigaldamiseks.

    ```console
    pip install datasets==2.19.1
    ```

#### Looge `donload_dataset.py`

> [!NOTE]
> Täielik kaustastruktuur:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Avage **Visual Studio Code**.

1. Valige menüüribalt **File**.

1. Valige **Open Folder**.

1. Valige *finetune-phi* kaust, mille ise lõite, see asub aadressil *C:\Users\yourUserName\finetune-phi*.

    ![Valige loodud kaust.](../../../../../../translated_images/et/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Visual Studio Code vasakul paanil paremklõpsake ja valige **New File**, et luua uus fail nimega *download_dataset.py*.

    ![Looge uus fail.](../../../../../../translated_images/et/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Andmekogu ettevalmistamine täpsustamiseks

Selles ülesandes jooksutate faili *download_dataset.py*, et alla laadida *ultrachat_200k* andmekogud oma kohalikku keskkonda. Seejärel kasutate neid andmekogusid Phi-3 mudeli täpsustamiseks Azure Machine Learningis.

Selles ülesandes te:

- Lisate *download_dataset.py* faili koodi andmekogude allalaadimiseks.
- Jooksete faili *download_dataset.py*, et laadida andmed oma kohalikku keskkonda.

#### Laadige oma andmekogu alla kasutades *download_dataset.py*

1. Avage *download_dataset.py* fail Visual Studio Codes.

1. Lisage järgmine kood *download_dataset.py* faili.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Laadi andmekogu määratud nime, konfiguratsiooni ja jagamissuhtega
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Jaga andmekogu treening- ja testkogumiks (80% treening, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Loo kataloog, kui seda pole olemas
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Ava fail kirjutamisrežiimis
        with open(filepath, 'w', encoding='utf-8') as f:
            # Korda läbi iga kirje andmekogus
            for record in dataset:
                # Salvesta kirje JSON-objektina ja kirjuta see faili
                json.dump(record, f)
                # Kirjuta uue rea märk, et eraldada kirjeid
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Laadi ja jaga ULTRACHAT_200k andmekogu kindla konfiguratsiooni ja jagamissuhtega
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Ekstrakti treening- ja testandmed jagatud kogumist
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Salvesta treeningandmed JSONL-faili
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Salvesta testandmed eraldi JSONL-faili
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Tippige oma terminali järgmine käsk skripti jooksutamiseks ja andmekogu allalaadimiseks oma kohalikku keskkonda.

    ```console
    python download_dataset.py
    ```

1. Kontrollige, et andmekogud salvestati edukalt teie kohalikku *finetune-phi/data* kausta.

> [!NOTE]
>
> #### Märkus andmekogu suuruse ja täpsustamise aja kohta
>
> Selles juhendis kasutate vaid 1% andmekogust (`split='train[:1%]'`). See vähendab oluliselt andmemahtu, kiirendades nii üleslaadimist kui ka täpsustamist. Saate protsenti vastavalt vajadusele reguleerida, et leida sobiv tasakaal õppimisaja ja mudeli jõudluse vahel. Väiksema osa andmetest kasutamine vähendab täpsustamiseks kuluvat aega, muutes protsessi juhendamiseks paremini hallatavaks.

## Stsenaarium 2: Phi-3 mudeli täpsustamine ja juurutamine Azure Machine Learning Studio´s

### Phi-3 mudeli täpsustamine

Selles ülesandes täpsustate Phi-3 mudelit Azure Machine Learning Studios.

Selles ülesandes te:

- Loote arvutiklastri täpsustamiseks.
- Täpsustate Phi-3 mudelit Azure Machine Learning Studios.

#### Looge arvutiklaster täpsustamiseks

1. Minge aadressile [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Valige vasakpoolsest vahekaardist **Compute**.

1. Valige navigeerimismenüüst **Compute clusters**.

1. Valige **+ New**.

    ![Valige compute.](../../../../../../translated_images/et/06-01-select-compute.a29cff290b480252.webp)

1. Täitke järgmised ülesanded:

    - Valige soovitud **Region**.
    - Valige **Virtual machine tier** väärtuseks **Dedicated**.
    - Valige **Virtual machine type** väärtuseks **GPU**.
    - Valige **Virtual machine size** filtrist **Select from all options**.
    - Valige **Virtual machine size** väärtuseks **Standard_NC24ads_A100_v4**.

    ![Looge klaster.](../../../../../../translated_images/et/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Valige **Next**.

1. Täitke järgmised ülesanded:

    - Sisestage **Compute name**. See peab olema unikaalne väärtus.
    - Valige **Minimum number of nodes** väärtuseks **0**.
    - Valige **Maximum number of nodes** väärtuseks **1**.
    - Valige **Idle seconds before scale down** väärtuseks **120**.

    ![Looge klaster.](../../../../../../translated_images/et/06-03-create-cluster.4a54ba20914f3662.webp)

1. Valige **Create**.

#### Täpsustage Phi-3 mudelit

1. Minge aadressile [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Valige Azure Machine Learning tööruum, mille ise lõite.

    ![Valige loodud tööruum.](../../../../../../translated_images/et/06-04-select-workspace.a92934ac04f4f181.webp)

1. Täitke järgmised ülesanded:

    - Valige vasakpoolsest vahekaardist **Model catalog**.
    - Tippige **otsinguribale** *phi-3-mini-4k* ja valige ilmuvate valikute seast **Phi-3-mini-4k-instruct**.

    ![Tippige phi-3-mini-4k.](../../../../../../translated_images/et/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Valige navigeerimismenüüst **Fine-tune**.

    ![Valige fine tune.](../../../../../../translated_images/et/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Täitke järgmised ülesanded:

    - Valige **Select task type** väärtuseks **Chat completion**.
    - Valige **+ Select data**, et üles laadida **Traning data**.
    - Valige valideerimisandmete üleslaadimise tüübiks **Provide different validation data**.
    - Valige **+ Select data**, et üles laadida **Validation data**.

    ![Täidake täpsustamise leht.](../../../../../../translated_images/et/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Täpsemate seadete kohandamiseks, nagu **learning_rate** ja **lr_scheduler_type**, saate valida **Advanced settings**, et optimeerida täpsustamisprotsessi vastavalt oma vajadustele.

1. Valige **Finish**.

1. Selles ülesandes täpsustasite edukalt Phi-3 mudeli Azure Machine Learningis. Pange tähele, et täpsustamisprotsess võib võtta märkimisväärselt aega. Pärast täpsustamistöö käivitamist peate ootama selle lõpulejõudmist. Jälgida saate täpsustamistöö olekut, liikudes Azure Machine Learning tööruumi vasakpoolsesse menüüsse, valides Jobs lehe. Järgmise seeria jooksul juurutate täpsustatud mudeli ja integreerite selle Prompt Flow’ga.

    ![Vaata täpsustamistööd.](../../../../../../translated_images/et/06-08-output.2bd32e59930672b1.webp)

### Juurutage täpsustatud Phi-3 mudel

Et integreerida täpsustatud Phi-3 mudelit Prompt Flow’ga, tuleb mudel juurutada, et see oleks reaalajas tõlgendamiseks ligipääsetav. See protsess hõlmab mudeli registreerimist, veebipõhise lõpp-punkti loomist ja mudeli juurutamist.

Selles ülesandes te:

- Registreerite täpsustatud mudeli Azure Machine Learning tööruumis.
- Loote veebipõhise lõpp-punkti.
- Juurutate registreeritud täpsustatud Phi-3 mudeli.

#### Registreerige täpsustatud mudel

1. Minge aadressile [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Valige Azure Machine Learning tööruum, mille ise lõite.

    ![Valige loodud tööruum.](../../../../../../translated_images/et/06-04-select-workspace.a92934ac04f4f181.webp)

1. Valige vasakpoolsest vahekaardist **Models**.
1. Valige **+ Register**.
1. Valige **From a job output**.

    ![Registreeri mudel.](../../../../../../translated_images/et/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Valige loodud töö.

    ![Valige töö.](../../../../../../translated_images/et/07-02-select-job.3e2e1144cd6cd093.webp)

1. Valige **Next**.

1. Valige **Model type** väärtuseks **MLflow**.

1. Veenduge, et oleks valitud **Job output**; see peaks olema automaatselt valitud.

    ![Valige väljund.](../../../../../../translated_images/et/07-03-select-output.4cf1a0e645baea1f.webp)

2. Valige **Next**.

3. Valige **Register**.

    ![Valige registreerimine.](../../../../../../translated_images/et/07-04-register.fd82a3b293060bc7.webp)

4. Oma registreeritud mudelit saate vaadata, liikudes vasakpoolsest menüüst **Models** menüüsse.

    ![Registreeritud mudel.](../../../../../../translated_images/et/07-05-registered-model.7db9775f58dfd591.webp)

#### Juurutage täpsustatud mudel

1. Minge Azure Machine Learning tööruumi, mille ise lõite.

1. Valige vasakpoolsest vahekaardist **Endpoints**.

1. Valige navigeerimismenüüst **Real-time endpoints**.

    ![Loo lõpp-punkt.](../../../../../../translated_images/et/07-06-create-endpoint.1ba865c606551f09.webp)

1. Valige **Create**.

1. Valige loodud registreeritud mudel.

    ![Valige registreeritud mudel.](../../../../../../translated_images/et/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Valige **Select**.

1. Täitke järgmised väljad:

    - Valige **Virtual machine** väärtuseks *Standard_NC6s_v3*.
    - Valige soovitud **Instance count**, näiteks *1*.
    - Valige **Endpoint** väärtuseks **New**, et luua lõpp-punkt.
    - Sisestage **Endpoint name**. See peab olema unikaalne.
    - Sisestage **Deployment name**. See peab olema unikaalne.

    ![Täidake juurutamise seaded.](../../../../../../translated_images/et/07-08-deployment-setting.43ddc4209e673784.webp)

1. Valige **Deploy**.

> [!WARNING]
> Konto täiendavate tasude vältimiseks kustutage Azure Machine Learning tööruumis loodud lõpp-punkt.
>

#### Kontrollige juurutamise olekut Azure Machine Learning tööruumis

1. Minge loodud Azure Machine Learning tööruumi.

1. Valige vasakpoolsest menüüst **Endpoints**.

1. Valige loodud lõpp-punkt.

    ![Valige lõpp-punktid](../../../../../../translated_images/et/07-09-check-deployment.325d18cae8475ef4.webp)

1. Sellel lehel saate hallata lõpp-punkte juurutamise protsessi ajal.

> [!NOTE]
> Kui juurutamine on lõppenud, veenduge, et **Live traffic** oleks seatud väärtusele **100%**. Kui ei ole, valige **Update traffic**, et liiklust reguleerida. Märkige, et mudelit ei saa testida, kui liiklus on seatud 0%-le.
>
> ![Seadistage liiklus.](../../../../../../translated_images/et/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Stsenaarium 3: Integreerimine Prompt Flow’ga ja vestlemine oma kohandatud mudeliga Microsoft Foundry’s

### Kohandatud Phi-3 mudeli integreerimine Prompt Flow’ga

Pärast edukat täpsustatud mudeli juurutamist saate nüüd selle Prompt Flow’ga integreerida, et kasutada mudelit reaalajas rakendustes, võimaldades mitmesuguseid interaktiivseid ülesandeid oma kohandatud Phi-3 mudeliga.

Selles ülesandes te:

- Loote Microsoft Foundry Hubi.
- Loote Microsoft Foundry Projekti.
- Loote Prompt Flow.
- Lisate kohandatud ühenduse täpsustatud Phi-3 mudelile.
- Seadistate Prompt Flow, et vestelda oma kohandatud Phi-3 mudeliga.

> [!NOTE]
> Promptflow’ga saab integreerida ka Azure ML Studio abil. Sama integreerimisprotsessi saab rakendada Azure ML Studios.

#### Looge Microsoft Foundry Hub

Enne Projekti loomist peate looma Hubi. Hub toimib nagu Resource Group, võimaldades organiseerida ja hallata mitut projekti Microsoft Foundry keskkonnas.
1. Külastage [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Valige vasakpoolsest vahekaardilt **Kõik keskused**.

1. Valige navigeerimismenüüst **+ Uus keskus**.

    ![Loo keskus.](../../../../../../translated_images/et/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Tehke järgmised toimingud:

    - Sisestage **Keskuse nimi**. See peab olema unikaalne.
    - Valige oma Azure’i **Tellimus**.
    - Valige kasutatav **Resource group** (kui vaja, looge uus).
    - Valige soovitud **Asukoht**.
    - Valige kasutatav **Connect Azure AI Services** (kui vaja, looge uus).
    - Valige **Connect Azure AI Search** ja valige **Jäta ühendamine vahele**.

    ![Täida keskus.](../../../../../../translated_images/et/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Valige **Järgmine**.

#### Loo Microsoft Foundry projekt

1. Loodud keskusest valige vasakpoolsest vahekaardilt **Kõik projektid**.

1. Valige navigeerimismenüüst **+ Uus projekt**.

    ![Vali uus projekt.](../../../../../../translated_images/et/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Sisestage **Projekti nimi**. See peab olema unikaalne.

    ![Loo projekt.](../../../../../../translated_images/et/08-05-create-project.4d97f0372f03375a.webp)

1. Valige **Loo projekt**.

#### Lisa kohandatud ühendus peenhäälestatud Phi-3 mudelile

Et integreerida oma kohandatud Phi-3 mudel Prompt flow’sse, peate salvestama mudeli lõpp-punkti ja võtme kohandatud ühendusse. See seade tagab juurdepääsu teie kohandatud Phi-3 mudelile Prompt flow’s.

#### Määra peenhäälestatud Phi-3 mudeli api-võti ja lõpp-punkti URI

1. Külastage [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navigeerige loodud Azure Machine learning tööruumi.

1. Valige vasakpoolsest vahekaardilt **Endpoints**.

    ![Vali lõpp-punktid.](../../../../../../translated_images/et/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Valige loodud lõpp-punkt.

    ![Vali loodud lõpp-punkt.](../../../../../../translated_images/et/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Valige navigeerimismenüüst **Tarbi**.

1. Kopeerige oma **REST lõpp-punkt** ja **Esialgne võti**.

    ![Kopeeri api-võti ja lõpp-punkti URI.](../../../../../../translated_images/et/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Lisa kohandatud ühendus

1. Külastage [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navigeerige loodud Microsoft Foundry projekti.

1. Loodud projektist valige vasakpoolsest vahekaardilt **Seaded**.

1. Valige **+ Uus ühendus**.

    ![Vali uus ühendus.](../../../../../../translated_images/et/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Valige navigeerimismenüüst **Kohandatud võtmed**.

    ![Vali kohandatud võtmed.](../../../../../../translated_images/et/08-10-select-custom-keys.856f6b2966460551.webp)

1. Tehke järgmised toimingud:

    - Valige **+ Lisa võtme-väärtuse paarid**.
    - Sisestage võtme nimeks **endpoint** ja kleepige väärtuse välja Azure ML Studio’st kopeeritud lõpp-punkt.
    - Valige jälle **+ Lisa võtme-väärtuse paarid**.
    - Sisestage võtme nimeks **key** ja kleepige väärtuse välja Azure ML Studio’st kopeeritud võti.
    - Pärast võtmete lisamist valige **on salajane**, et vältida võtme avalikustamist.

    ![Lisa ühendus.](../../../../../../translated_images/et/08-11-add-connection.785486badb4d2d26.webp)

1. Valige **Lisa ühendus**.

#### Loo Prompt flow

Olete Microsoft Foundrys lisanud kohandatud ühenduse. Nüüd loome Prompt flow kasutades järgmisi samme. Seejärel ühendate selle Prompt flow kohandatud ühendusega, et kasutada peenhäälestatud mudelit Prompt flow sees.

1. Navigeerige loodud Microsoft Foundry projekti.

1. Valige vasakpoolsest vahekaardilt **Prompt flow**.

1. Valige navigeerimismenüüst **+ Loo**.

    ![Vali Promptflow.](../../../../../../translated_images/et/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Valige navigeerimismenüüst **Vestluse voog**.

    ![Vali vestluse voog.](../../../../../../translated_images/et/08-13-select-flow-type.2ec689b22da32591.webp)

1. Sisestage kasutatav **Kausta nimi**.

    ![Sisesta nimi.](../../../../../../translated_images/et/08-14-enter-name.ff9520fefd89f40d.webp)

2. Valige **Loo**.

#### Määra Prompt flow suhtlemiseks kohandatud Phi-3 mudeliga

Peate integreerima peenhäälestatud Phi-3 mudeli Prompt flow’sse. Kuid olemasolev Prompt flow ei ole selleks otstarbeks loodud. Seetõttu tuleb Prompt flow ümber kujundada, et võimaldada kohandatud mudeli integreerimist.

1. Prompt flow’s tehke järgmised toimingud olemasoleva voo taastamiseks:

    - Valige **Toore faili režiim**.
    - Kustutage kogu olemasolev kood failist *flow.dag.yml*.
    - Lisage faili *flow.dag.yml* järgmine kood.

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

    ![Vali toore faili režiim.](../../../../../../translated_images/et/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Lisage faili *integrate_with_promptflow.py* järgmine kood, et kasutada kohandatud Phi-3 mudelit Prompt flow’s.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logimise seadistamine
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

        # "connection" on kohandatud ühenduse nimi, "endpoint", "key" on võtmed kohandatud ühenduses
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
            
            # Logi kogu JSON vastus
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

    ![Kleebi prompt flow kood.](../../../../../../translated_images/et/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Microsoft Foundrys Prompt flow kasutamise kohta leiate rohkem teavet aadressilt [Prompt flow Microsoft Foundrys](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Valige **Vestluse sisend**, **Vestluse väljund**, et lubada mudeliga vestlemine.

    ![Sisend Väljund.](../../../../../../translated_images/et/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Nüüd olete valmis vestlema oma kohandatud Phi-3 mudeliga. Järgmises harjutuses õpite, kuidas alustada Prompt flow’d ja kasutada seda vestlemiseks oma peenhäälestatud Phi-3 mudeliga.

> [!NOTE]
>
> Taastatud voo peaks välja nägema alloleva pildina:
>
> ![Voo näide.](../../../../../../translated_images/et/08-18-graph-example.d6457533952e690c.webp)
>

### Suhtle oma kohandatud Phi-3 mudeliga

Nüüd, kui olete peenhäälestanud ja integreerinud oma kohandatud Phi-3 mudeli Prompt flow’sse, olete valmis sellega vestlema. See harjutus juhendab teid mudeliga suhtlemise seadistamise ja alustamise protsessis Prompt flow abil. Järgides neid samme, saate täielikult ära kasutada oma peenhäälestatud Phi-3 mudeli võimeid erinevate ülesannete ja vestluste jaoks.

- Suhtle oma kohandatud Phi-3 mudeliga kasutades Prompt flow’d.

#### Alusta Prompt flow’d

1. Valige **Alusta arvutusstsenaariume**, et käivitada Prompt flow.

    ![Alusta arvutusstsenaariumi.](../../../../../../translated_images/et/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Valige **Kinnita ja parsi sisend**, et uuendada parameetreid.

    ![Kinnita sisend.](../../../../../../translated_images/et/09-02-validate-input.317c76ef766361e9.webp)

1. Valige **Ühenduse** väärtuseks loodud kohandatud ühendus, näiteks *connection*.

    ![Ühendus.](../../../../../../translated_images/et/09-03-select-connection.99bdddb4b1844023.webp)

#### Vestle oma kohandatud mudeliga

1. Valige **Vestlus**.

    ![Vali vestlus.](../../../../../../translated_images/et/09-04-select-chat.61936dce6612a1e6.webp)

1. Siin on näide tulemustest: nüüd saate vestelda oma kohandatud Phi-3 mudeliga. Soovitatav on esitada küsimusi andmete põhjal, mida kasutati peenhäälestamiseks.

    ![Vestlus prompt flow’s.](../../../../../../translated_images/et/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest vabastamine**:  
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüame täpsust, palun arvestage, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles on usaldusväärne allikas. Olulise info puhul soovitatakse professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->