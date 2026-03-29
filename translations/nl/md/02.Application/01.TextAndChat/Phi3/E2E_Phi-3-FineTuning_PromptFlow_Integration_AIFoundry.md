# Fijn afstemmen en integreren van aangepaste Phi-3 modellen met Prompt flow in Microsoft Foundry

Deze end-to-end (E2E) voorbeeld is gebaseerd op de gids "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" van de Microsoft Tech Community. Het introduceert de processen van fijn afstemmen, implementeren en integreren van aangepaste Phi-3 modellen met Prompt flow in Microsoft Foundry.
In tegenstelling tot het E2E voorbeeld, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", dat lokaal code uitvoeren betrof, richt deze handleiding zich volledig op het fijn afstemmen en integreren van je model binnen de Azure AI / ML Studio.

## Overzicht

In deze E2E voorbeeld leer je hoe je het Phi-3 model fijn kunt afstemmen en kunt integreren met Prompt flow in Microsoft Foundry. Door gebruik te maken van Azure AI / ML Studio, stel je een workflow in voor het implementeren en gebruiken van aangepaste AI-modellen. Deze E2E voorbeeld is onderverdeeld in drie scenario's:

**Scenario 1: Azure-resources instellen en voorbereiden voor fijn afstemmen**

**Scenario 2: Fijn afstemmen van het Phi-3 model en implementeren in Azure Machine Learning Studio**

**Scenario 3: Integreren met Prompt flow en chatten met je aangepaste model in Microsoft Foundry**

Hier is een overzicht van deze E2E voorbeeld.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/nl/00-01-architecture.198ba0f1ae6d841a.webp)

### Inhoudsopgave

1. **[Scenario 1: Azure-resources instellen en voorbereiden voor fijn afstemmen](#scenario-1-azure-resources-instellen-en-voorbereiden-voor-fijn-afstemmen)**
    - [Een Azure Machine Learning Workspace maken](#een-azure-machine-learning-workspace-maken)
    - [GPU-quotums aanvragen in Azure-abonnement](#gpu-quotums-aanvragen-in-azure-abonnement)
    - [Roltoewijzing toevoegen](#roltoewijzing-toevoegen)
    - [Project opzetten](#project-opzetten)
    - [Datasets voorbereiden voor fijn afstemmen](#bereid-dataset-voor-op-fijn-afstemming)

1. **[Scenario 2: Fijn afstemmen Phi-3 model en implementeren in Azure Machine Learning Studio](#scenario-2-fijn-afstemmen-van-het-phi-3-model-en-implementeren-in-azure-machine-learning-studio)**
    - [Fijn afstemmen van het Phi-3 model](#fijn-afstemmen-van-het-phi-3-model)
    - [Het fijn afgestemde Phi-3 model implementeren](#implementeer-het-fijn-afgestelde-phi-3-model)

1. **[Scenario 3: Integreren met Prompt flow en chatten met je aangepaste model in Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Het aangepaste Phi-3 model integreren met Prompt flow](#integreer-het-aangepaste-phi-3-model-met-prompt-flow)
    - [Chatten met je aangepaste Phi-3 model](#chat-met-je-aangepaste-phi-3-model)

## Scenario 1: Azure-resources instellen en voorbereiden voor fijn afstemmen

### Een Azure Machine Learning Workspace maken

1. Typ *azure machine learning* in de **zoekbalk** bovenaan de portalpagina en selecteer **Azure Machine Learning** uit de opties die verschijnen.

    ![Type azure machine learning.](../../../../../../translated_images/nl/01-01-type-azml.acae6c5455e67b4b.webp)

2. Selecteer **+ Create** in het navigatiemenu.

3. Selecteer **New workspace** in het navigatiemenu.

    ![Select new workspace.](../../../../../../translated_images/nl/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Voer de volgende taken uit:

    - Selecteer je Azure **Abonnement**.
    - Selecteer de **Resourcegroep** die je wilt gebruiken (maak er een nieuwe aan indien nodig).
    - Voer een **Workspace Name** in. Dit moet een unieke waarde zijn.
    - Selecteer de **Regio** die je wilt gebruiken.
    - Selecteer de **Opslagaccount** die je wilt gebruiken (maak er een nieuwe aan indien nodig).
    - Selecteer de **Key vault** die je wilt gebruiken (maak er een nieuwe aan indien nodig).
    - Selecteer de **Application insights** die je wilt gebruiken (maak er een nieuwe aan indien nodig).
    - Selecteer de **Container registry** die je wilt gebruiken (maak er een nieuwe aan indien nodig).

    ![Fill azure machine learning.](../../../../../../translated_images/nl/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Selecteer **Review + Create**.

6. Selecteer **Create**.

### GPU-quotums aanvragen in Azure-abonnement

In deze handleiding leer je hoe je een Phi-3 model fijn kunt afstemmen en implementeren met gebruik van GPU's. Voor het fijn afstemmen gebruik je de *Standard_NC24ads_A100_v4* GPU, waarvoor een quotum aanvraag nodig is. Voor de implementatie gebruik je de *Standard_NC6s_v3* GPU, waarvoor eveneens een quotum aanvraag nodig is.

> [!NOTE]
>
> Alleen Pay-As-You-Go abonnementen (het standaard type abonnement) komen in aanmerking voor GPU-toewijzing; voordeelabonnementen worden momenteel niet ondersteund.
>

1. Bezoek [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Voer de volgende taken uit om *Standard NCADSA100v4 Family* quota aan te vragen:

    - Selecteer **Quota** in het tabblad aan de linkerkant.
    - Selecteer de **Virtual machine family** die je wilt gebruiken. Bijvoorbeeld, selecteer **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, welke de *Standard_NC24ads_A100_v4* GPU bevat.
    - Selecteer **Request quota** in het navigatiemenu.

        ![Request quota.](../../../../../../translated_images/nl/02-02-request-quota.c0428239a63ffdd5.webp)

    - Vul op de Request quota pagina de **New cores limit** in die je wilt gebruiken. Bijvoorbeeld, 24.
    - Selecteer op de Request quota pagina **Submit** om het GPU-quotum aan te vragen.

1. Voer de volgende taken uit om *Standard NCSv3 Family* quota aan te vragen:

    - Selecteer **Quota** in het tabblad aan de linkerkant.
    - Selecteer de **Virtual machine family** die je wilt gebruiken. Bijvoorbeeld, selecteer **Standard NCSv3 Family Cluster Dedicated vCPUs**, welke de *Standard_NC6s_v3* GPU bevat.
    - Selecteer **Request quota** in het navigatiemenu.
    - Vul op de Request quota pagina de **New cores limit** in die je wilt gebruiken. Bijvoorbeeld, 24.
    - Selecteer op de Request quota pagina **Submit** om het GPU-quotum aan te vragen.

### Roltoewijzing toevoegen

Om je modellen fijn af te stemmen en te implementeren, moet je eerst een Gebruikers Toegewezen Beheerde Identiteit (User Assigned Managed Identity - UAI) maken en hier de juiste rechten aan toewijzen. Deze UAI wordt gebruikt voor authenticatie tijdens implementatie.

#### Een User Assigned Managed Identity (UAI) aanmaken

1. Typ *managed identities* in de **zoekbalk** bovenaan de portalpagina en selecteer **Managed Identities** uit de opties die verschijnen.

    ![Type managed identities.](../../../../../../translated_images/nl/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Selecteer **+ Create**.

    ![Select create.](../../../../../../translated_images/nl/03-02-select-create.92bf8989a5cd98f2.webp)

1. Voer de volgende taken uit:

    - Selecteer je Azure **Abonnement**.
    - Selecteer de **Resourcegroep** die je wilt gebruiken (maak een nieuwe aan indien nodig).
    - Selecteer de **Regio** die je wilt gebruiken.
    - Voer de **Naam** in. Dit moet een unieke waarde zijn.

    ![Select create.](../../../../../../translated_images/nl/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Selecteer **Review + create**.

1. Selecteer **+ Create**.

#### Contributor roltoewijzing toevoegen aan Managed Identity

1. Navigeer naar de Managed Identity resource die je hebt gemaakt.

1. Selecteer **Azure role assignments** in het tabblad aan de linkerkant.

1. Selecteer **+Add role assignment** in het navigatiemenu.

1. Voer op de pagina Add role assignment de volgende taken uit:
    - Stel de **Scope** in op **Resource group**.
    - Selecteer je Azure **Abonnement**.
    - Selecteer de te gebruiken **Resourcegroep**.
    - Stel de **Rol** in op **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/nl/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Selecteer **Save**.

#### Storage Blob Data Reader roltoewijzing toevoegen aan Managed Identity

1. Typ *storage accounts* in de **zoekbalk** bovenaan de portalpagina en selecteer **Storage accounts** uit de opties die verschijnen.

    ![Type storage accounts.](../../../../../../translated_images/nl/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Selecteer de opslagaccount die gekoppeld is aan de Azure Machine Learning workspace die je hebt gemaakt. Bijvoorbeeld, *finetunephistorage*.

1. Voer de volgende taken uit om naar de pagina Add role assignment te navigeren:

    - Navigeer naar de Azure Storage account die je hebt gemaakt.
    - Selecteer **Access Control (IAM)** in het tabblad aan de linkerkant.
    - Selecteer **+ Add** in het navigatiemenu.
    - Selecteer **Add role assignment** in het navigatiemenu.

    ![Add role.](../../../../../../translated_images/nl/03-06-add-role.353ccbfdcf0789c2.webp)

1. Voer op de pagina Add role assignment de volgende taken uit:

    - Typ op de Role pagina *Storage Blob Data Reader* in de **zoekbalk** en selecteer **Storage Blob Data Reader** uit de opties die verschijnen.
    - Selecteer op de Role pagina **Next**.
    - Selecteer op de Members pagina **Assign access to** **Managed identity**.
    - Selecteer op de Members pagina **+ Select members**.
    - Selecteer op de Select managed identities pagina je Azure **Abonnement**.
    - Selecteer op de Select managed identities pagina de **Managed identity** bij **Manage Identity**.
    - Selecteer op de Select managed identities pagina de Manage Identity die je hebt gemaakt. Bijvoorbeeld, *finetunephi-managedidentity*.
    - Selecteer op de Select managed identities pagina **Select**.

    ![Select managed identity.](../../../../../../translated_images/nl/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Selecteer **Review + assign**.

#### AcrPull roltoewijzing toevoegen aan Managed Identity

1. Typ *container registries* in de **zoekbalk** bovenaan de portalpagina en selecteer **Container registries** uit de opties die verschijnen.

    ![Type container registries.](../../../../../../translated_images/nl/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Selecteer de container registry die gekoppeld is aan de Azure Machine Learning workspace. Bijvoorbeeld, *finetunephicontainerregistry*

1. Voer de volgende taken uit om naar de pagina Add role assignment te navigeren:

    - Selecteer **Access Control (IAM)** in het tabblad aan de linkerkant.
    - Selecteer **+ Add** in het navigatiemenu.
    - Selecteer **Add role assignment** in het navigatiemenu.

1. Voer op de pagina Add role assignment de volgende taken uit:

    - Typ op de Role pagina *AcrPull* in de **zoekbalk** en selecteer **AcrPull** uit de opties die verschijnen.
    - Selecteer op de Role pagina **Next**.
    - Selecteer op de Members pagina **Assign access to** **Managed identity**.
    - Selecteer op de Members pagina **+ Select members**.
    - Selecteer op de Select managed identities pagina je Azure **Abonnement**.
    - Selecteer op de Select managed identities pagina de **Managed identity** bij **Manage Identity**.
    - Selecteer op de Select managed identities pagina de Manage Identity die je hebt gemaakt. Bijvoorbeeld, *finetunephi-managedidentity*.
    - Selecteer op de Select managed identities pagina **Select**.
    - Selecteer **Review + assign**.

### Project opzetten

Om de datasets te downloaden die nodig zijn voor het fijn afstemmen, stel je een lokale omgeving in.

In deze oefening:

- Maak je een map aan om in te werken.
- Maak je een virtuele omgeving aan.
- Installeer je de vereiste pakketten.
- Maak je een *download_dataset.py* bestand om de dataset te downloaden.

#### Maak een map aan om in te werken

1. Open een terminalvenster en typ het volgende commando om een map met de naam *finetune-phi* aan te maken op het standaardpad.

    ```console
    mkdir finetune-phi
    ```

2. Typ het volgende commando in je terminal om naar de map *finetune-phi* te navigeren die je hebt aangemaakt.

    ```console
    cd finetune-phi
    ```

#### Maak een virtuele omgeving aan

1. Typ het volgende commando in je terminal om een virtuele omgeving met de naam *.venv* aan te maken.
    ```console
    python -m venv .venv
    ```

2. Typ het volgende commando in uw terminal om de virtuele omgeving te activeren.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Als het is gelukt, zou u *(.venv)* vóór de opdrachtprompt moeten zien.

#### Installeer de benodigde pakketten

1. Typ de volgende opdrachten in uw terminal om de benodigde pakketten te installeren.

    ```console
    pip install datasets==2.19.1
    ```

#### Maak `download_dataset.py`

> [!NOTE]
> Volledige mappenstructuur:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Open **Visual Studio Code**.

1. Selecteer **Bestand** in de menubalk.

1. Selecteer **Map openen**.

1. Selecteer de map *finetune-phi* die u hebt aangemaakt, deze bevindt zich in *C:\Users\yourUserName\finetune-phi*.

    ![Selecteer de map die u hebt aangemaakt.](../../../../../../translated_images/nl/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Klik in het linkerpaneel van Visual Studio Code met de rechtermuisknop en selecteer **Nieuw bestand** om een nieuw bestand genaamd *download_dataset.py* te maken.

    ![Maak een nieuw bestand aan.](../../../../../../translated_images/nl/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Bereid dataset voor op fijn-afstemming

In deze oefening voert u het bestand *download_dataset.py* uit om de *ultrachat_200k* datasets te downloaden naar uw lokale omgeving. Daarna gebruikt u deze datasets om het Phi-3 model fijn af te stemmen in Azure Machine Learning.

In deze oefening:

- Voegt u code toe aan het bestand *download_dataset.py* om de datasets te downloaden.
- Voert u het bestand *download_dataset.py* uit om de datasets naar uw lokale omgeving te downloaden.

#### Download uw dataset met *download_dataset.py*

1. Open het bestand *download_dataset.py* in Visual Studio Code.

1. Voeg de volgende code toe aan het bestand *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Laad de dataset met de opgegeven naam, configuratie en splitsingsverhouding
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Verdeel de dataset in train- en testsets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Maak de map aan als deze niet bestaat
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open het bestand in schrijfmodus
        with open(filepath, 'w', encoding='utf-8') as f:
            # Itereer over elk record in de dataset
            for record in dataset:
                # Dump het record als een JSON-object en schrijf het naar het bestand
                json.dump(record, f)
                # Schrijf een newline-teken om records te scheiden
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Laad en splits de ULTRACHAT_200k dataset met een specifieke configuratie en splitsingsverhouding
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extraheer de train- en testdatasets uit de splitsing
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Sla de train dataset op in een JSONL-bestand
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Sla de testdataset op in een apart JSONL-bestand
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Typ het volgende commando in uw terminal om het script uit te voeren en de dataset naar uw lokale omgeving te downloaden.

    ```console
    python download_dataset.py
    ```

1. Controleer of de datasets succesvol zijn opgeslagen in uw lokale map *finetune-phi/data*.

> [!NOTE]
>
> #### Opmerking over dataset grootte en tijd voor fijn-afstemming
>
> In deze tutorial gebruikt u slechts 1% van de dataset (`split='train[:1%]'`). Dit vermindert de hoeveelheid data aanzienlijk, wat zowel het uploaden als het fijn afstemmen versnelt. U kunt het percentage aanpassen om een goede balans te vinden tussen trainingstijd en modelprestatie. Het gebruik van een kleinere subset van de dataset vermindert de tijd die nodig is voor fijn-afstemming, wat het proces beter behapbaar maakt voor een tutorial.

## Scenario 2: Fijn-afstemmen van het Phi-3 model en implementeren in Azure Machine Learning Studio

### Fijn-afstemmen van het Phi-3 model

In deze oefening zult u het Phi-3 model fijn afstemmen in Azure Machine Learning Studio.

In deze oefening:

- Maakt u een computercluster voor fijn-afstemming.
- Stemmen u het Phi-3 model fijn af in Azure Machine Learning Studio.

#### Maak computercluster voor fijn-afstemming

1. Bezoek [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecteer **Compute** in de linker zijbalk.

1. Selecteer **Compute clusters** in het navigatiemenu.

1. Selecteer **+ Nieuw**.

    ![Selecteer compute.](../../../../../../translated_images/nl/06-01-select-compute.a29cff290b480252.webp)

1. Voer de volgende taken uit:

    - Selecteer de **Regio** die u wilt gebruiken.
    - Selecteer de **Virtuele machinetier** op **Dedicated**.
    - Selecteer het **Type virtuele machine** op **GPU**.
    - Selecteer de filter **Virtuele maat** op **Selecteer uit alle opties**.
    - Selecteer de **Virtuele machine maat** op **Standard_NC24ads_A100_v4**.

    ![Maak cluster aan.](../../../../../../translated_images/nl/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Selecteer **Volgende**.

1. Voer de volgende taken uit:

    - Voer een **Compute naam** in. Dit moet een unieke waarde zijn.
    - Stel het **Minimaal aantal nodes** in op **0**.
    - Stel het **Maximaal aantal nodes** in op **1**.
    - Stel de **Idle seconden voor schalen naar beneden** in op **120**.

    ![Maak cluster aan.](../../../../../../translated_images/nl/06-03-create-cluster.4a54ba20914f3662.webp)

1. Selecteer **Maken**.

#### Fijn-afstemmen van het Phi-3 model

1. Bezoek [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecteer de Azure Machine Learning workspace die u hebt aangemaakt.

    ![Selecteer de workspace die u hebt aangemaakt.](../../../../../../translated_images/nl/06-04-select-workspace.a92934ac04f4f181.webp)

1. Voer de volgende taken uit:

    - Selecteer **Model catalogus** in de linker zijbalk.
    - Typ *phi-3-mini-4k* in de **zoekbalk** en selecteer **Phi-3-mini-4k-instruct** uit de opties die verschijnen.

    ![Typ phi-3-mini-4k.](../../../../../../translated_images/nl/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Selecteer **Fijn afstemmen** in het navigatiemenu.

    ![Selecteer fijn afstemmen.](../../../../../../translated_images/nl/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Voer de volgende taken uit:

    - Selecteer **Taaktype selecteren** op **Chat completion**.
    - Selecteer **+ Gegevens selecteren** om **Trainingsgegevens** te uploaden.
    - Selecteer het uploadtype voor validatiegegevens op **Verschillende validatiegegevens opgeven**.
    - Selecteer **+ Gegevens selecteren** om **Validatiegegevens** te uploaden.

    ![Vul de pagina voor fijn-afstemming in.](../../../../../../translated_images/nl/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> U kunt **Geavanceerde instellingen** selecteren om configuraties zoals **learning_rate** en **lr_scheduler_type** aan te passen om het fijn-afstemproces te optimaliseren aan uw specifieke behoeften.

1. Selecteer **Voltooien**.

1. In deze oefening hebt u met succes het Phi-3 model fijn afgestemd met behulp van Azure Machine Learning. Houd er rekening mee dat het fijn-afstemproces aanzienlijke tijd kan kosten. Na het starten van de fijn-afstemtaken moet u wachten tot deze voltooid is. U kunt de status van de fijn-afstemtaken volgen door naar de tab *Jobs* aan de linkerzijde van uw Azure Machine Learning Workspace te navigeren. In de volgende reeks zult u het fijn-afgestelde model implementeren en integreren met Promptflow.

    ![Zie fijn-afstemtaken.](../../../../../../translated_images/nl/06-08-output.2bd32e59930672b1.webp)

### Implementeer het fijn-afgestelde Phi-3 model

Om het fijn-afgestelde Phi-3 model met Prompt flow te integreren, moet u het model implementeren zodat het toegankelijk is voor realtime inferentie. Dit proces omvat het registreren van het model, het maken van een online endpoint en het implementeren van het model.

In deze oefening:

- Registreert u het fijn-afgestelde model in de Azure Machine Learning workspace.
- Maakt u een online endpoint.
- Implementeert u het geregistreerde fijn-afgestelde Phi-3 model.

#### Registreer het fijn-afgestelde model

1. Bezoek [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecteer de Azure Machine Learning workspace die u hebt aangemaakt.

    ![Selecteer de workspace die u hebt aangemaakt.](../../../../../../translated_images/nl/06-04-select-workspace.a92934ac04f4f181.webp)

1. Selecteer **Modellen** in de linker zijbalk.
1. Selecteer **+ Registreren**.
1. Selecteer **Van een job-uitvoer**.

    ![Registreer model.](../../../../../../translated_images/nl/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Selecteer de job die u hebt aangemaakt.

    ![Selecteer job.](../../../../../../translated_images/nl/07-02-select-job.3e2e1144cd6cd093.webp)

1. Selecteer **Volgende**.

1. Selecteer **Modeltype** op **MLflow**.

1. Zorg ervoor dat **Job-uitvoer** is geselecteerd; dit zou automatisch geselecteerd moeten zijn.

    ![Selecteer uitvoer.](../../../../../../translated_images/nl/07-03-select-output.4cf1a0e645baea1f.webp)

2. Selecteer **Volgende**.

3. Selecteer **Registreren**.

    ![Selecteer registreren.](../../../../../../translated_images/nl/07-04-register.fd82a3b293060bc7.webp)

4. U kunt uw geregistreerde model bekijken door naar het menu **Modellen** aan de linkerzijde te gaan.

    ![Geregistreerd model.](../../../../../../translated_images/nl/07-05-registered-model.7db9775f58dfd591.webp)

#### Implementeer het fijn-afgestelde model

1. Navigeer naar de Azure Machine Learning workspace die u hebt aangemaakt.

1. Selecteer **Endpoints** in de linker zijbalk.

1. Selecteer **Realtime endpoints** in het navigatiemenu.

    ![Maak endpoint aan.](../../../../../../translated_images/nl/07-06-create-endpoint.1ba865c606551f09.webp)

1. Selecteer **Maken**.

1. Selecteer het geregistreerde model dat u hebt aangemaakt.

    ![Selecteer geregistreerd model.](../../../../../../translated_images/nl/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Selecteer **Selecteren**.

1. Voer de volgende taken uit:

    - Selecteer **Virtuele machine** op *Standard_NC6s_v3*.
    - Kies het **Aantal instanties** dat u wilt gebruiken. Bijvoorbeeld *1*.
    - Stel **Endpoint** in op **Nieuw** om een nieuw endpoint aan te maken.
    - Voer een **Endpoint naam** in. Dit moet een unieke waarde zijn.
    - Voer een **Implementatienaam** in. Dit moet een unieke waarde zijn.

    ![Vul de instellingen voor implementatie in.](../../../../../../translated_images/nl/07-08-deployment-setting.43ddc4209e673784.webp)

1. Selecteer **Implementeren**.

> [!WARNING]
> Om extra kosten op uw account te voorkomen, zorg ervoor dat u het aangemaakte endpoint verwijdert in de Azure Machine Learning workspace.
>

#### Controleer de implementatiestatus in Azure Machine Learning Workspace

1. Navigeer naar de Azure Machine Learning workspace die u hebt aangemaakt.

1. Selecteer **Endpoints** in de linker zijbalk.

1. Selecteer het endpoint dat u hebt aangemaakt.

    ![Selecteer endpoints](../../../../../../translated_images/nl/07-09-check-deployment.325d18cae8475ef4.webp)

1. Op deze pagina kunt u de endpoints beheren tijdens het implementatieproces.

> [!NOTE]
> Zodra de implementatie is voltooid, zorg ervoor dat **Live traffic** is ingesteld op **100%**. Als dit niet het geval is, selecteer dan **Traffic bijwerken** om de verkeersinstellingen aan te passen. Let op: u kunt het model niet testen als de traffic op 0% staat.
>
> ![Stel traffic in.](../../../../../../translated_images/nl/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Scenario 3: Integreren met Prompt flow en chatten met uw aangepaste model in Microsoft Foundry

### Integreer het aangepaste Phi-3 model met Prompt flow

Na het succesvol implementeren van uw fijn-afgestelde model, kunt u het nu integreren met Prompt Flow om uw model te gebruiken in realtime applicaties, waarmee u verschillende interactieve taken uitvoert met uw aangepaste Phi-3 model.

In deze oefening:

- Maakt u een Microsoft Foundry Hub aan.
- Maakt u een Microsoft Foundry Project aan.
- Maakt u Prompt flow aan.
- Voegt u een aangepaste verbinding toe voor het fijn-afgestelde Phi-3 model.
- Stelt u Prompt flow in om te chatten met uw aangepaste Phi-3 model.

> [!NOTE]
> U kunt ook integreren met Promptflow via Azure ML Studio. Hetzelfde integratieproces is ook van toepassing op Azure ML Studio.

#### Maak Microsoft Foundry Hub aan

U moet een Hub aanmaken voordat u een Project aanmaakt. Een Hub fungeert als een Resource Group, waarmee u meerdere projecten binnen Microsoft Foundry kunt organiseren en beheren.
1. Bezoek [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Selecteer **Alle hubs** in het tabblad aan de linkerkant.

1. Selecteer **+ Nieuwe hub** in het navigatiemenu.

    ![Maak hub aan.](../../../../../../translated_images/nl/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Voer de volgende taken uit:

    - Voer een **Hub-naam** in. Dit moet een unieke waarde zijn.
    - Selecteer je Azure **Abonnement**.
    - Selecteer de **Resourcegroep** die je wilt gebruiken (maak een nieuwe aan indien nodig).
    - Selecteer de **Locatie** die je wilt gebruiken.
    - Selecteer de **Verbinden met Azure AI Services** die je wilt gebruiken (maak een nieuwe aan indien nodig).
    - Selecteer **Verbinden met Azure AI Search** en kies **Verbinding overslaan**.

    ![Vul hub in.](../../../../../../translated_images/nl/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Selecteer **Volgende**.

#### Maak een Microsoft Foundry-project aan

1. Selecteer in de Hub die je hebt gemaakt **Alle projecten** in het tabblad aan de linkerkant.

1. Selecteer **+ Nieuw project** in het navigatiemenu.

    ![Selecteer nieuw project.](../../../../../../translated_images/nl/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Voer een **Projectnaam** in. Dit moet een unieke waarde zijn.

    ![Maak project aan.](../../../../../../translated_images/nl/08-05-create-project.4d97f0372f03375a.webp)

1. Selecteer **Maak een project aan**.

#### Voeg een aangepaste verbinding toe voor het fijn-afgestelde Phi-3 model

Om je aangepaste Phi-3 model te integreren met Prompt flow, moet je de endpoint en sleutel van het model opslaan in een aangepaste verbinding. Deze setup zorgt voor toegang tot je aangepaste Phi-3 model in Prompt flow.

#### Stel API-sleutel en endpoint-URI in van het fijn-afgestelde Phi-3 model

1. Bezoek [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navigeer naar de Azure Machine learning workspace die je hebt gemaakt.

1. Selecteer **Endpoints** in het tabblad aan de linkerkant.

    ![Selecteer endpoints.](../../../../../../translated_images/nl/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Selecteer de endpoint die je hebt aangemaakt.

    ![Selecteer aangemaakte endpoint.](../../../../../../translated_images/nl/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Selecteer **Consumeren** in het navigatiemenu.

1. Kopieer je **REST-endpoint** en **Primair sleutel**.

    ![Kopieer API-sleutel en endpoint-URI.](../../../../../../translated_images/nl/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Voeg de aangepaste verbinding toe

1. Bezoek [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navigeer naar het Microsoft Foundry-project dat je hebt aangemaakt.

1. Selecteer in het project dat je hebt gemaakt **Instellingen** in het tabblad aan de linkerkant.

1. Selecteer **+ Nieuwe verbinding**.

    ![Selecteer nieuwe verbinding.](../../../../../../translated_images/nl/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Selecteer **Aangepaste sleutels** in het navigatiemenu.

    ![Selecteer aangepaste sleutels.](../../../../../../translated_images/nl/08-10-select-custom-keys.856f6b2966460551.webp)

1. Voer de volgende taken uit:

    - Selecteer **+ Voeg sleutel-waardeparen toe**.
    - Voer als sleutelnaam **endpoint** in en plak de endpoint die je hebt gekopieerd uit Azure ML Studio in het waardeveld.
    - Selecteer opnieuw **+ Voeg sleutel-waardeparen toe**.
    - Voer als sleutelnaam **key** in en plak de sleutel die je hebt gekopieerd uit Azure ML Studio in het waardeveld.
    - Nadat je de sleutels hebt toegevoegd, selecteer je **is geheim** om te voorkomen dat de sleutel wordt blootgesteld.

    ![Voeg verbinding toe.](../../../../../../translated_images/nl/08-11-add-connection.785486badb4d2d26.webp)

1. Selecteer **Verbinding toevoegen**.

#### Maak Prompt flow aan

Je hebt een aangepaste verbinding toegevoegd in Microsoft Foundry. Laten we nu een Prompt flow maken met behulp van de volgende stappen. Daarna verbind je deze Prompt flow met de aangepaste verbinding zodat je het fijn-afgestelde model kunt gebruiken binnen Prompt flow.

1. Navigeer naar het Microsoft Foundry-project dat je hebt aangemaakt.

1. Selecteer **Prompt flow** in het tabblad aan de linkerkant.

1. Selecteer **+ Maken** in het navigatiemenu.

    ![Selecteer Promptflow.](../../../../../../translated_images/nl/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Selecteer **Chat flow** in het navigatiemenu.

    ![Selecteer chat flow.](../../../../../../translated_images/nl/08-13-select-flow-type.2ec689b22da32591.webp)

1. Voer de te gebruiken **Mapnaam** in.

    ![Voer naam in.](../../../../../../translated_images/nl/08-14-enter-name.ff9520fefd89f40d.webp)

2. Selecteer **Maken**.

#### Stel Prompt flow in om te chatten met je aangepaste Phi-3 model

Je moet het fijn-afgestelde Phi-3 model integreren in een Prompt flow. De bestaande Prompt flow is echter niet ontworpen voor dit doel. Daarom moet je de Prompt flow herontwerpen om de integratie van het aangepaste model mogelijk te maken.

1. Voer in de Prompt flow de volgende taken uit om de bestaande flow opnieuw op te bouwen:

    - Selecteer **Ruwe bestandsmodus**.
    - Verwijder alle bestaande code in het *flow.dag.yml* bestand.
    - Voeg de volgende code toe aan het *flow.dag.yml* bestand.

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

    - Selecteer **Opslaan**.

    ![Selecteer ruwe bestandsmodus.](../../../../../../translated_images/nl/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Voeg de volgende code toe aan het *integrate_with_promptflow.py* bestand om het aangepaste Phi-3 model te gebruiken in Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logboekopstelling
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

        # "connection" is de naam van de Aangepaste Verbinding, "endpoint", "key" zijn de sleutels in de Aangepaste Verbinding
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
            
            # Log de volledige JSON-respons
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

    ![Plak prompt flow code.](../../../../../../translated_images/nl/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Voor meer gedetailleerde informatie over het gebruik van Prompt flow in Microsoft Foundry kun je verwijzen naar [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selecteer **Chatinvoer**, **Chatafvoer** om de chat met je model in te schakelen.

    ![Invoer Uitvoer.](../../../../../../translated_images/nl/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Je bent nu klaar om te chatten met je aangepaste Phi-3 model. In de volgende oefening leer je hoe je Prompt flow start en gebruikt om te chatten met je fijn-afgestelde Phi-3 model.

> [!NOTE]
>
> De opnieuw opgebouwde flow zou er uit moeten zien zoals hieronder:
>
> ![Flow voorbeeld.](../../../../../../translated_images/nl/08-18-graph-example.d6457533952e690c.webp)
>

### Chat met je aangepaste Phi-3 model

Nu je je aangepaste Phi-3 model hebt fijn afgestemd en geïntegreerd met Prompt flow, ben je klaar om ermee te beginnen communiceren. Deze oefening leidt je door het proces van het opzetten en starten van een chat met je model via Prompt flow. Door deze stappen te volgen, kun je de mogelijkheden van je fijn-afgestelde Phi-3 model volledig benutten voor diverse taken en gesprekken.

- Chat met je aangepaste Phi-3 model met behulp van Prompt flow.

#### Start Prompt flow

1. Selecteer **Start computerrondes** om Prompt flow te starten.

    ![Start computerronde.](../../../../../../translated_images/nl/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Selecteer **Valideer en parse invoer** om de parameters te vernieuwen.

    ![Valideer invoer.](../../../../../../translated_images/nl/09-02-validate-input.317c76ef766361e9.webp)

1. Selecteer de **Waarde** van de **verbinding** naar de aangepaste verbinding die je hebt aangemaakt. Bijvoorbeeld *connection*.

    ![Verbinding.](../../../../../../translated_images/nl/09-03-select-connection.99bdddb4b1844023.webp)

#### Chat met je aangepaste model

1. Selecteer **Chat**.

    ![Selecteer chat.](../../../../../../translated_images/nl/09-04-select-chat.61936dce6612a1e6.webp)

1. Hier is een voorbeeld van de resultaten: Je kunt nu chatten met je aangepaste Phi-3 model. Het wordt aanbevolen om vragen te stellen gebaseerd op de data die gebruikt is voor het fijn afstemmen.

    ![Chatten met prompt flow.](../../../../../../translated_images/nl/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, verzoeken wij u te beseffen dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties voortvloeiend uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->