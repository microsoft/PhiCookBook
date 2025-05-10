<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-09T18:13:40+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "nl"
}
-->
# Fine-tunen en integreren van aangepaste Phi-3 modellen met Prompt flow in Azure AI Foundry

Deze end-to-end (E2E) voorbeeld is gebaseerd op de handleiding "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" van de Microsoft Tech Community. Het introduceert de processen van fine-tunen, implementeren en integreren van aangepaste Phi-3 modellen met Prompt flow in Azure AI Foundry. In tegenstelling tot het E2E voorbeeld, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", waarbij code lokaal werd uitgevoerd, richt deze tutorial zich volledig op het fine-tunen en integreren van je model binnen Azure AI / ML Studio.

## Overzicht

In dit E2E voorbeeld leer je hoe je het Phi-3 model fine-tunet en integreert met Prompt flow in Azure AI Foundry. Door gebruik te maken van Azure AI / ML Studio stel je een workflow op voor het implementeren en gebruiken van aangepaste AI modellen. Dit E2E voorbeeld is verdeeld in drie scenario's:

**Scenario 1: Azure resources opzetten en voorbereiden voor fine-tuning**

**Scenario 2: Fine-tunen van het Phi-3 model en implementeren in Azure Machine Learning Studio**

**Scenario 3: Integreren met Prompt flow en chatten met je aangepaste model in Azure AI Foundry**

Hier volgt een overzicht van dit E2E voorbeeld.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.nl.png)

### Inhoudsopgave

1. **[Scenario 1: Azure resources opzetten en voorbereiden voor fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Een Azure Machine Learning Workspace aanmaken](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [GPU-quotums aanvragen in Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Roltoewijzing toevoegen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Project opzetten](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Dataset voorbereiden voor fine-tuning](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 2: Fine-tunen van Phi-3 model en implementeren in Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Het Phi-3 model fine-tunen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Het fijn-afgestelde Phi-3 model implementeren](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 3: Integreren met Prompt flow en chatten met je aangepaste model in Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Het aangepaste Phi-3 model integreren met Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Chatten met je aangepaste Phi-3 model](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenario 1: Azure resources opzetten en voorbereiden voor fine-tuning

### Een Azure Machine Learning Workspace aanmaken

1. Typ *azure machine learning* in de **zoekbalk** bovenaan de portalpagina en selecteer **Azure Machine Learning** uit de opties die verschijnen.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.nl.png)

2. Selecteer **+ Create** in het navigatiemenu.

3. Selecteer **New workspace** in het navigatiemenu.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.nl.png)

4. Voer de volgende taken uit:

    - Selecteer je Azure **Subscription**.
    - Selecteer de **Resource group** die je wilt gebruiken (maak er een nieuwe aan indien nodig).
    - Voer een **Workspace Name** in. Dit moet een unieke naam zijn.
    - Selecteer de **Regio** die je wilt gebruiken.
    - Selecteer de **Storage account** die je wilt gebruiken (maak er een nieuwe aan indien nodig).
    - Selecteer de **Key vault** die je wilt gebruiken (maak er een nieuwe aan indien nodig).
    - Selecteer de **Application insights** die je wilt gebruiken (maak er een nieuwe aan indien nodig).
    - Selecteer de **Container registry** die je wilt gebruiken (maak er een nieuwe aan indien nodig).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.nl.png)

5. Selecteer **Review + Create**.

6. Selecteer **Create**.

### GPU-quotums aanvragen in Azure Subscription

In deze tutorial leer je hoe je een Phi-3 model fine-tunet en implementeert met gebruik van GPU's. Voor het fine-tunen gebruik je de *Standard_NC24ads_A100_v4* GPU, waarvoor een quotumaanvraag nodig is. Voor de implementatie gebruik je de *Standard_NC6s_v3* GPU, waarvoor ook een quotumaanvraag nodig is.

> [!NOTE]
>
> Alleen Pay-As-You-Go abonnementen (het standaard abonnements type) komen in aanmerking voor GPU-toewijzing; voordeelabonnementen worden momenteel niet ondersteund.
>

1. Bezoek [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Voer de volgende stappen uit om een quotum voor *Standard NCADSA100v4 Family* aan te vragen:

    - Selecteer **Quota** in het tabblad aan de linkerzijde.
    - Selecteer de **Virtual machine family** die je wilt gebruiken. Bijvoorbeeld, selecteer **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, dat de *Standard_NC24ads_A100_v4* GPU bevat.
    - Selecteer **Request quota** in het navigatiemenu.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.nl.png)

    - Vul op de pagina Request quota het veld **New cores limit** in met het aantal cores dat je wilt gebruiken. Bijvoorbeeld 24.
    - Klik op **Submit** om het GPU-quotum aan te vragen.

1. Voer de volgende stappen uit om een quotum voor *Standard NCSv3 Family* aan te vragen:

    - Selecteer **Quota** in het tabblad aan de linkerzijde.
    - Selecteer de **Virtual machine family** die je wilt gebruiken. Bijvoorbeeld, selecteer **Standard NCSv3 Family Cluster Dedicated vCPUs**, dat de *Standard_NC6s_v3* GPU bevat.
    - Selecteer **Request quota** in het navigatiemenu.
    - Vul op de pagina Request quota het veld **New cores limit** in met het aantal cores dat je wilt gebruiken. Bijvoorbeeld 24.
    - Klik op **Submit** om het GPU-quotum aan te vragen.

### Roltoewijzing toevoegen

Om je modellen te kunnen fine-tunen en implementeren, moet je eerst een User Assigned Managed Identity (UAI) aanmaken en deze de juiste rechten geven. Deze UAI wordt gebruikt voor authenticatie tijdens de implementatie.

#### User Assigned Managed Identity (UAI) aanmaken

1. Typ *managed identities* in de **zoekbalk** bovenaan de portalpagina en selecteer **Managed Identities** uit de opties die verschijnen.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.nl.png)

1. Selecteer **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.nl.png)

1. Voer de volgende taken uit:

    - Selecteer je Azure **Subscription**.
    - Selecteer de **Resource group** die je wilt gebruiken (maak er een nieuwe aan indien nodig).
    - Selecteer de **Regio** die je wilt gebruiken.
    - Voer een **Naam** in. Dit moet een unieke naam zijn.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.nl.png)

1. Selecteer **Review + create**.

1. Selecteer **+ Create**.

#### Contributor roltoewijzing toevoegen aan Managed Identity

1. Navigeer naar de Managed Identity resource die je hebt aangemaakt.

1. Selecteer **Azure role assignments** in het tabblad aan de linkerzijde.

1. Selecteer **+ Add role assignment** in het navigatiemenu.

1. Voer op de pagina Add role assignment de volgende taken uit:
    - Stel de **Scope** in op **Resource group**.
    - Selecteer je Azure **Subscription**.
    - Selecteer de **Resource group** die je wilt gebruiken.
    - Selecteer de **Rol** **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.nl.png)

2. Selecteer **Save**.

#### Storage Blob Data Reader roltoewijzing toevoegen aan Managed Identity

1. Typ *storage accounts* in de **zoekbalk** bovenaan de portalpagina en selecteer **Storage accounts** uit de opties die verschijnen.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.nl.png)

1. Selecteer de storage account die gekoppeld is aan de Azure Machine Learning workspace die je hebt aangemaakt. Bijvoorbeeld *finetunephistorage*.

1. Voer de volgende stappen uit om naar de pagina Add role assignment te navigeren:

    - Navigeer naar de Azure Storage account die je hebt aangemaakt.
    - Selecteer **Access Control (IAM)** in het tabblad aan de linkerzijde.
    - Selecteer **+ Add** in het navigatiemenu.
    - Selecteer **Add role assignment** in het navigatiemenu.

    ![Add role.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.nl.png)

1. Voer op de pagina Add role assignment de volgende taken uit:

    - Typ *Storage Blob Data Reader* in de **zoekbalk** en selecteer **Storage Blob Data Reader** uit de opties die verschijnen.
    - Klik op **Next**.
    - Selecteer bij **Assign access to** de optie **Managed identity**.
    - Klik op **+ Select members**.
    - Selecteer je Azure **Subscription**.
    - Selecteer de **Managed identity** optie **Manage Identity**.
    - Selecteer de Managed Identity die je hebt aangemaakt. Bijvoorbeeld *finetunephi-managedidentity*.
    - Klik op **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.nl.png)

1. Selecteer **Review + assign**.

#### AcrPull roltoewijzing toevoegen aan Managed Identity

1. Typ *container registries* in de **zoekbalk** bovenaan de portalpagina en selecteer **Container registries** uit de opties die verschijnen.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.nl.png)

1. Selecteer de container registry die gekoppeld is aan de Azure Machine Learning workspace. Bijvoorbeeld *finetunephicontainerregistry*

1. Voer de volgende stappen uit om naar de pagina Add role assignment te navigeren:

    - Selecteer **Access Control (IAM)** in het tabblad aan de linkerzijde.
    - Selecteer **+ Add** in het navigatiemenu.
    - Selecteer **Add role assignment** in het navigatiemenu.

1. Voer op de pagina Add role assignment de volgende taken uit:

    - Typ *AcrPull* in de **zoekbalk** en selecteer **AcrPull** uit de opties die verschijnen.
    - Klik op **Next**.
    - Selecteer bij **Assign access to** de optie **Managed identity**.
    - Klik op **+ Select members**.
    - Selecteer je Azure **Subscription**.
    - Selecteer de **Managed identity** optie **Manage Identity**.
    - Selecteer de Managed Identity die je hebt aangemaakt. Bijvoorbeeld *finetunephi-managedidentity*.
    - Klik op **Select**.
    - Selecteer **Review + assign**.

### Project opzetten

Om de datasets te downloaden die nodig zijn voor het fine-tunen, stel je een lokale omgeving in.

In deze oefening ga je:

- Een map aanmaken om in te werken.
- Een virtuele omgeving aanmaken.
- De benodigde pakketten installeren.
- Een *download_dataset.py* bestand aanmaken om de dataset te downloaden.

#### Een map aanmaken om in te werken

1. Open een terminalvenster en typ het volgende commando om een map genaamd *finetune-phi* aan te maken op de standaardlocatie.

    ```console
    mkdir finetune-phi
    ```

2. Typ het volgende commando in je terminal om naar de map *finetune-phi* te navigeren die je hebt aangemaakt.

    ```console
    cd finetune-phi
    ```

#### Een virtuele omgeving aanmaken

1. Typ het volgende commando in je terminal om een virtuele omgeving aan te maken met de naam *.venv*.

    ```console
    python -m venv .venv
    ```

2. Typ het volgende commando in je terminal om de virtuele omgeving te activeren.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Als het gelukt is, zie je *(.venv)* voor de opdrachtprompt verschijnen.

#### De benodigde pakketten installeren

1. Typ de volgende commando's in je terminal om de benodigde pakketten te installeren.

    ```console
    pip install datasets==2.19.1
    ```

#### Maak `download_dataset.py` aan

> [!NOTE]
> Volledige mappenstructuur:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Open **Visual Studio Code**.

1. Selecteer **File** in de menubalk.

1. Selecteer **Open Folder**.

1. Selecteer de map *finetune-phi* die je hebt aangemaakt, te vinden op *C:\Users\yourUserName\finetune-phi*.

    ![Select the folder that you created.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.nl.png)

1. Klik in het linkerpaneel van Visual Studio Code met de rechtermuisknop en kies **New File** om een nieuw bestand aan te maken met de naam *download_dataset.py*.

    ![Create a new file.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.nl.png)

### Dataset voorbereiden voor fine-tuning

In deze oefening voer je het bestand *download_dataset.py* uit om de *ultrachat_200k* datasets te downloaden naar je lokale omgeving. Je gebruikt deze datasets vervolgens om het Phi-3 model te fine-tunen in Azure Machine Learning.

In deze oefening ga je:

- Code toevoegen aan het bestand *download_dataset.py* om de datasets te downloaden.
- Het bestand *download_dataset.py* uitvoeren om de datasets naar je lokale omgeving te downloaden.

#### Download je dataset met *download_dataset.py*

1. Open het bestand *download_dataset.py* in Visual Studio Code.

1. Voeg de volgende code toe in het bestand *download_dataset.py*.

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

1. Typ het volgende commando in je terminal om het script uit te voeren en de dataset te downloaden naar je lokale omgeving.

    ```console
    python download_dataset.py
    ```

1. Controleer of de datasets succesvol zijn opgeslagen in je lokale map *finetune-phi/data*.

> [!NOTE]
>
> #### Opmerking over datasetgrootte en fine-tuning tijd
>
> In deze tutorial gebruik je slechts 1% van de dataset (`split='train[:1%]'`). Dit verkleint de hoeveelheid data aanzienlijk, waardoor zowel het uploaden als het fine-tunen sneller gaat. Je kunt het percentage aanpassen om een goede balans te vinden tussen trainingstijd en modelprestaties. Het gebruik van een kleinere subset van de dataset verkort de benodigde tijd voor fine-tuning, wat het proces beter beheersbaar maakt voor een tutorial.

## Scenario 2: Fine-tunen van Phi-3 model en implementeren in Azure Machine Learning Studio

### Het Phi-3 model fine-tunen

In deze oefening fine-tune je het Phi-3 model in Azure Machine Learning Studio.

In deze oefening ga je:

- Een computercluster aanmaken voor fine-tuning.
- Het Phi-3 model fine-tunen in Azure Machine Learning Studio.

#### Een computercluster aanmaken voor fine-tuning
1. Bezoek [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecteer **Compute** in het tabblad aan de linkerkant.

1. Selecteer **Compute clusters** in het navigatiemenu.

1. Selecteer **+ Nieuw**.

    ![Selecteer compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.nl.png)

1. Voer de volgende taken uit:

    - Selecteer de **Regio** die je wilt gebruiken.
    - Stel de **Virtual machine tier** in op **Dedicated**.
    - Stel het **Virtual machine type** in op **GPU**.
    - Stel het filter voor **Virtual machine size** in op **Select from all options**.
    - Selecteer de **Virtual machine size** op **Standard_NC24ads_A100_v4**.

    ![Cluster aanmaken.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.nl.png)

1. Selecteer **Volgende**.

1. Voer de volgende taken uit:

    - Vul een **Compute name** in. Dit moet een unieke waarde zijn.
    - Stel het **Minimum number of nodes** in op **0**.
    - Stel het **Maximum number of nodes** in op **1**.
    - Stel de **Idle seconds before scale down** in op **120**.

    ![Cluster aanmaken.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.nl.png)

1. Selecteer **Aanmaken**.

#### Fijn afstemmen van het Phi-3 model

1. Bezoek [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecteer de Azure Machine Learning workspace die je hebt aangemaakt.

    ![Selecteer de workspace die je hebt aangemaakt.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.nl.png)

1. Voer de volgende taken uit:

    - Selecteer **Model catalog** in het tabblad aan de linkerkant.
    - Typ *phi-3-mini-4k* in de **zoekbalk** en selecteer **Phi-3-mini-4k-instruct** uit de opties die verschijnen.

    ![Typ phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.nl.png)

1. Selecteer **Fine-tune** in het navigatiemenu.

    ![Selecteer fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.nl.png)

1. Voer de volgende taken uit:

    - Stel **Select task type** in op **Chat completion**.
    - Selecteer **+ Select data** om **Trainingsdata** te uploaden.
    - Stel het type validatiegegevens upload in op **Provide different validation data**.
    - Selecteer **+ Select data** om **Validatiegegevens** te uploaden.

    ![Vul de pagina voor fijn afstemmen in.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.nl.png)

    > [!TIP]
    >
    > Je kunt **Advanced settings** selecteren om configuraties zoals **learning_rate** en **lr_scheduler_type** aan te passen, zodat het fijn afstemmen beter aansluit bij jouw specifieke wensen.

1. Selecteer **Voltooien**.

1. In deze oefening heb je het Phi-3 model succesvol fijn afgestemd met behulp van Azure Machine Learning. Houd er rekening mee dat het fijn afstemmen enige tijd kan duren. Nadat je het fijn afstemmingsproces hebt gestart, moet je wachten tot het is voltooid. Je kunt de status van de taak volgen door naar het tabblad Jobs te gaan in jouw Azure Machine Learning Workspace. In de volgende serie ga je het fijn afgestemde model implementeren en integreren met Prompt flow.

    ![Bekijk de fijn afstemming job.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.nl.png)

### Implementeer het fijn afgestemde Phi-3 model

Om het fijn afgestemde Phi-3 model te integreren met Prompt flow, moet je het model implementeren zodat het toegankelijk is voor realtime inferentie. Dit proces omvat het registreren van het model, het aanmaken van een online endpoint en het implementeren van het model.

In deze oefening ga je:

- Het fijn afgestemde model registreren in de Azure Machine Learning workspace.
- Een online endpoint aanmaken.
- Het geregistreerde fijn afgestemde Phi-3 model implementeren.

#### Registreer het fijn afgestemde model

1. Bezoek [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Selecteer de Azure Machine Learning workspace die je hebt aangemaakt.

    ![Selecteer de workspace die je hebt aangemaakt.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.nl.png)

1. Selecteer **Models** in het tabblad aan de linkerkant.
1. Selecteer **+ Register**.
1. Selecteer **From a job output**.

    ![Registreer model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.nl.png)

1. Selecteer de job die je hebt aangemaakt.

    ![Selecteer job.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.nl.png)

1. Selecteer **Volgende**.

1. Stel **Model type** in op **MLflow**.

1. Controleer of **Job output** is geselecteerd; dit zou automatisch moeten gebeuren.

    ![Selecteer output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.nl.png)

2. Selecteer **Volgende**.

3. Selecteer **Register**.

    ![Selecteer register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.nl.png)

4. Je kunt je geregistreerde model bekijken door naar het menu **Models** te gaan in het tabblad aan de linkerkant.

    ![Geregistreerd model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.nl.png)

#### Implementeer het fijn afgestemde model

1. Ga naar de Azure Machine Learning workspace die je hebt aangemaakt.

1. Selecteer **Endpoints** in het tabblad aan de linkerkant.

1. Selecteer **Real-time endpoints** in het navigatiemenu.

    ![Maak endpoint aan.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.nl.png)

1. Selecteer **Create**.

1. Selecteer het geregistreerde model dat je hebt aangemaakt.

    ![Selecteer geregistreerd model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.nl.png)

1. Selecteer **Select**.

1. Voer de volgende taken uit:

    - Selecteer **Virtual machine** op *Standard_NC6s_v3*.
    - Selecteer het aantal instanties dat je wilt gebruiken. Bijvoorbeeld *1*.
    - Stel **Endpoint** in op **New** om een nieuw endpoint aan te maken.
    - Vul een **Endpoint name** in. Dit moet een unieke waarde zijn.
    - Vul een **Deployment name** in. Dit moet een unieke waarde zijn.

    ![Vul de instellingen voor de implementatie in.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.nl.png)

1. Selecteer **Deploy**.

> [!WARNING]
> Om extra kosten op je account te voorkomen, zorg ervoor dat je het aangemaakte endpoint verwijdert in de Azure Machine Learning workspace.
>

#### Controleer de status van de implementatie in Azure Machine Learning Workspace

1. Ga naar de Azure Machine Learning workspace die je hebt aangemaakt.

1. Selecteer **Endpoints** in het tabblad aan de linkerkant.

1. Selecteer het endpoint dat je hebt aangemaakt.

    ![Selecteer endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.nl.png)

1. Op deze pagina kun je de endpoints beheren tijdens het implementatieproces.

> [!NOTE]
> Zodra de implementatie is voltooid, zorg ervoor dat **Live traffic** is ingesteld op **100%**. Als dit niet het geval is, selecteer dan **Update traffic** om de verkeersinstellingen aan te passen. Houd er rekening mee dat je het model niet kunt testen als het verkeer op 0% staat.
>
> ![Verkeer instellen.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.nl.png)
>

## Scenario 3: Integreren met Prompt flow en chatten met je aangepaste model in Azure AI Foundry

### Integreer het aangepaste Phi-3 model met Prompt flow

Nadat je je fijn afgestemde model succesvol hebt geïmplementeerd, kun je het nu integreren met Prompt Flow om je model te gebruiken in realtime toepassingen, waarmee je verschillende interactieve taken met je aangepaste Phi-3 model kunt uitvoeren.

In deze oefening ga je:

- Azure AI Foundry Hub aanmaken.
- Azure AI Foundry Project aanmaken.
- Prompt flow aanmaken.
- Een aangepaste verbinding toevoegen voor het fijn afgestemde Phi-3 model.
- Prompt flow instellen om te chatten met je aangepaste Phi-3 model.

> [!NOTE]
> Je kunt ook integreren met Promptflow via Azure ML Studio. Hetzelfde integratieproces is toepasbaar op Azure ML Studio.

#### Maak een Azure AI Foundry Hub aan

Je moet eerst een Hub aanmaken voordat je een Project maakt. Een Hub werkt als een Resource Group, waarmee je meerdere projecten binnen Azure AI Foundry kunt organiseren en beheren.

1. Bezoek [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Selecteer **All hubs** in het tabblad aan de linkerkant.

1. Selecteer **+ New hub** in het navigatiemenu.

    ![Hub aanmaken.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.nl.png)

1. Voer de volgende taken uit:

    - Vul een **Hub name** in. Dit moet een unieke waarde zijn.
    - Selecteer je Azure **Subscription**.
    - Selecteer de **Resource group** die je wilt gebruiken (maak een nieuwe aan indien nodig).
    - Selecteer de **Location** die je wilt gebruiken.
    - Selecteer **Connect Azure AI Services** die je wilt gebruiken (maak een nieuwe aan indien nodig).
    - Selecteer **Connect Azure AI Search** op **Skip connecting**.

    ![Hub invullen.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.nl.png)

1. Selecteer **Volgende**.

#### Maak een Azure AI Foundry Project aan

1. Ga in de Hub die je hebt aangemaakt naar **All projects** in het tabblad aan de linkerkant.

1. Selecteer **+ New project** in het navigatiemenu.

    ![Selecteer nieuw project.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.nl.png)

1. Vul een **Project name** in. Dit moet een unieke waarde zijn.

    ![Project aanmaken.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.nl.png)

1. Selecteer **Create a project**.

#### Voeg een aangepaste verbinding toe voor het fijn afgestemde Phi-3 model

Om je aangepaste Phi-3 model te integreren met Prompt flow, moet je het endpoint en de sleutel van het model opslaan in een aangepaste verbinding. Deze setup zorgt ervoor dat je toegang hebt tot je aangepaste Phi-3 model binnen Prompt flow.

#### Stel de api key en endpoint uri in van het fijn afgestemde Phi-3 model

1. Bezoek [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navigeer naar de Azure Machine Learning workspace die je hebt aangemaakt.

1. Selecteer **Endpoints** in het tabblad aan de linkerkant.

    ![Selecteer endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.nl.png)

1. Selecteer het endpoint dat je hebt aangemaakt.

    ![Selecteer endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.nl.png)

1. Selecteer **Consume** in het navigatiemenu.

1. Kopieer je **REST endpoint** en **Primary key**.
![Kopieer api-sleutel en endpoint-uri.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.nl.png)

#### Voeg de aangepaste verbinding toe

1. Bezoek [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navigeer naar het Azure AI Foundry-project dat je hebt aangemaakt.

1. Selecteer in het project dat je hebt gemaakt **Settings** in het linkermenu.

1. Kies **+ New connection**.

    ![Selecteer nieuwe verbinding.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.nl.png)

1. Selecteer **Custom keys** in het navigatiemenu.

    ![Selecteer aangepaste sleutels.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.nl.png)

1. Voer de volgende stappen uit:

    - Klik op **+ Add key value pairs**.
    - Voer bij de sleutelnaam **endpoint** in en plak de endpoint die je uit Azure ML Studio hebt gekopieerd in het waardeveld.
    - Klik opnieuw op **+ Add key value pairs**.
    - Voer bij de sleutelnaam **key** in en plak de sleutel die je uit Azure ML Studio hebt gekopieerd in het waardeveld.
    - Nadat je de sleutels hebt toegevoegd, vink je **is secret** aan om te voorkomen dat de sleutel zichtbaar wordt.

    ![Voeg verbinding toe.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.nl.png)

1. Klik op **Add connection**.

#### Maak een Prompt flow aan

Je hebt een aangepaste verbinding toegevoegd in Azure AI Foundry. Laten we nu een Prompt flow maken met de volgende stappen. Daarna verbind je deze Prompt flow met de aangepaste verbinding zodat je het fijn-afgestelde model binnen de Prompt flow kunt gebruiken.

1. Navigeer naar het Azure AI Foundry-project dat je hebt aangemaakt.

1. Selecteer **Prompt flow** in het linkermenu.

1. Klik op **+ Create** in het navigatiemenu.

    ![Selecteer Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.nl.png)

1. Kies **Chat flow** in het navigatiemenu.

    ![Selecteer chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.nl.png)

1. Voer de **Folder name** in die je wilt gebruiken.

    ![Voer naam in.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.nl.png)

2. Klik op **Create**.

#### Stel Prompt flow in om te chatten met je aangepaste Phi-3 model

Je moet het fijn-afgestelde Phi-3 model integreren in een Prompt flow. De bestaande Prompt flow is echter niet ontworpen voor dit doel. Daarom moet je de Prompt flow herontwerpen om de integratie van het aangepaste model mogelijk te maken.

1. Voer in de Prompt flow de volgende stappen uit om de bestaande flow opnieuw op te bouwen:

    - Selecteer **Raw file mode**.
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

    - Klik op **Save**.

    ![Selecteer raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.nl.png)

1. Voeg de volgende code toe aan het *integrate_with_promptflow.py* bestand om het aangepaste Phi-3 model in Prompt flow te gebruiken.

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

    ![Plak prompt flow code.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.nl.png)

> [!NOTE]
> Voor meer gedetailleerde informatie over het gebruik van Prompt flow in Azure AI Foundry kun je terecht bij [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Selecteer **Chat input**, **Chat output** om chatten met je model mogelijk te maken.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.nl.png)

1. Je bent nu klaar om te chatten met je aangepaste Phi-3 model. In de volgende oefening leer je hoe je Prompt flow start en gebruikt om te chatten met je fijn-afgestelde Phi-3 model.

> [!NOTE]
>
> De opnieuw opgebouwde flow zou eruit moeten zien zoals in de onderstaande afbeelding:
>
> ![Voorbeeld flow.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.nl.png)
>

### Chat met je aangepaste Phi-3 model

Nu je je aangepaste Phi-3 model hebt fijn-afgesteld en geïntegreerd met Prompt flow, ben je klaar om ermee te communiceren. Deze oefening begeleidt je bij het instellen en starten van een chat met je model via Prompt flow. Door deze stappen te volgen, kun je de mogelijkheden van je fijn-afgestelde Phi-3 model optimaal benutten voor verschillende taken en gesprekken.

- Chat met je aangepaste Phi-3 model via Prompt flow.

#### Start Prompt flow

1. Klik op **Start compute sessions** om Prompt flow te starten.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.nl.png)

1. Klik op **Validate and parse input** om de parameters te vernieuwen.

    ![Valideer input.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.nl.png)

1. Selecteer de **Value** van de **connection** die verwijst naar de aangepaste verbinding die je hebt gemaakt. Bijvoorbeeld *connection*.

    ![Verbinding.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.nl.png)

#### Chat met je aangepaste model

1. Klik op **Chat**.

    ![Selecteer chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.nl.png)

1. Hier is een voorbeeld van de resultaten: nu kun je chatten met je aangepaste Phi-3 model. Het is aan te raden vragen te stellen die gebaseerd zijn op de data die voor het fijn-afstellen is gebruikt.

    ![Chat met prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.nl.png)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.