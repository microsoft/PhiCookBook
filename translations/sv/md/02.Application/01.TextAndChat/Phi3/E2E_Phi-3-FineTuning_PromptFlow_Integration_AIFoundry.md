<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ecbd9179a21edbaafaf114d47f09f3e3",
  "translation_date": "2025-05-09T18:09:35+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIFoundry.md",
  "language_code": "sv"
}
-->
# Fine-tune och integrera anpassade Phi-3-modeller med Prompt flow i Azure AI Foundry

Detta end-to-end (E2E) exempel baseras på guiden "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" från Microsoft Tech Community. Det introducerar processerna för finjustering, distribution och integration av anpassade Phi-3-modeller med Prompt flow i Azure AI Foundry. Till skillnad från E2E-exemplet, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", som involverade att köra kod lokalt, fokuserar denna handledning helt på finjustering och integration av din modell inom Azure AI / ML Studio.

## Översikt

I detta E2E-exempel kommer du att lära dig hur du finjusterar Phi-3-modellen och integrerar den med Prompt flow i Azure AI Foundry. Genom att använda Azure AI / ML Studio kommer du att skapa ett arbetsflöde för att distribuera och använda anpassade AI-modeller. Detta E2E-exempel är uppdelat i tre scenarier:

**Scenario 1: Sätt upp Azure-resurser och förbered för finjustering**

**Scenario 2: Finjustera Phi-3-modellen och distribuera i Azure Machine Learning Studio**

**Scenario 3: Integrera med Prompt flow och chatta med din anpassade modell i Azure AI Foundry**

Här är en översikt av detta E2E-exempel.

![Phi-3-FineTuning_PromptFlow_Integration Översikt.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.sv.png)

### Innehållsförteckning

1. **[Scenario 1: Sätt upp Azure-resurser och förbered för finjustering](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Skapa ett Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Begär GPU-kvoter i Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Lägg till rolltilldelning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Sätt upp projekt](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Förbered dataset för finjustering](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 2: Finjustera Phi-3-modellen och distribuera i Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Finjustera Phi-3-modellen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Distribuera den finjusterade Phi-3-modellen](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 3: Integrera med Prompt flow och chatta med din anpassade modell i Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrera den anpassade Phi-3-modellen med Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Chatta med din anpassade Phi-3-modell](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenario 1: Sätt upp Azure-resurser och förbered för finjustering

### Skapa ett Azure Machine Learning Workspace

1. Skriv *azure machine learning* i **sökfältet** högst upp på portalsidan och välj **Azure Machine Learning** från alternativen som visas.

    ![Skriv azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.sv.png)

2. Välj **+ Create** från navigationsmenyn.

3. Välj **New workspace** från navigationsmenyn.

    ![Välj nytt workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.sv.png)

4. Utför följande uppgifter:

    - Välj din Azure **Subscription**.
    - Välj den **Resource group** du vill använda (skapa en ny vid behov).
    - Ange **Workspace Name**. Det måste vara ett unikt namn.
    - Välj den **Region** du vill använda.
    - Välj det **Storage account** som ska användas (skapa ett nytt vid behov).
    - Välj den **Key vault** som ska användas (skapa en ny vid behov).
    - Välj den **Application insights** som ska användas (skapa en ny vid behov).
    - Välj den **Container registry** som ska användas (skapa en ny vid behov).

    ![Fyll i Azure Machine Learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.sv.png)

5. Välj **Review + Create**.

6. Välj **Create**.

### Begär GPU-kvoter i Azure Subscription

I denna handledning kommer du att lära dig hur du finjusterar och distribuerar en Phi-3-modell med hjälp av GPU:er. För finjustering använder du *Standard_NC24ads_A100_v4*-GPU, som kräver en kvotbegäran. För distribution använder du *Standard_NC6s_v3*-GPU, som också kräver en kvotbegäran.

> [!NOTE]
>
> Endast Pay-As-You-Go-abonnemang (standardabonnemangstypen) är berättigade till GPU-tilldelning; förmånsabonnemang stöds inte för närvarande.
>

1. Besök [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Utför följande steg för att begära kvot för *Standard NCADSA100v4 Family*:

    - Välj **Quota** i vänstermenyn.
    - Välj den **Virtual machine family** som ska användas. Till exempel, välj **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, som inkluderar *Standard_NC24ads_A100_v4*-GPU:n.
    - Välj **Request quota** i navigationsmenyn.

        ![Begär kvot.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.sv.png)

    - På sidan för kvotbegäran, ange **New cores limit** som du vill använda, till exempel 24.
    - På sidan för kvotbegäran, välj **Submit** för att skicka kvotbegäran.

1. Utför följande steg för att begära kvot för *Standard NCSv3 Family*:

    - Välj **Quota** i vänstermenyn.
    - Välj den **Virtual machine family** som ska användas. Till exempel, välj **Standard NCSv3 Family Cluster Dedicated vCPUs**, som inkluderar *Standard_NC6s_v3*-GPU:n.
    - Välj **Request quota** i navigationsmenyn.
    - På sidan för kvotbegäran, ange **New cores limit** som du vill använda, till exempel 24.
    - På sidan för kvotbegäran, välj **Submit** för att skicka kvotbegäran.

### Lägg till rolltilldelning

För att finjustera och distribuera dina modeller måste du först skapa en User Assigned Managed Identity (UAI) och tilldela den rätt behörigheter. Denna UAI kommer att användas för autentisering vid distribution.

#### Skapa User Assigned Managed Identity (UAI)

1. Skriv *managed identities* i **sökfältet** högst upp på portalsidan och välj **Managed Identities** från alternativen som visas.

    ![Skriv managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.sv.png)

1. Välj **+ Create**.

    ![Välj skapa.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.sv.png)

1. Utför följande uppgifter:

    - Välj din Azure **Subscription**.
    - Välj den **Resource group** du vill använda (skapa en ny vid behov).
    - Välj den **Region** du vill använda.
    - Ange **Name**. Det måste vara ett unikt namn.

    ![Fyll i Managed Identities.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.sv.png)

1. Välj **Review + create**.

1. Välj **+ Create**.

#### Lägg till Contributor-rolltilldelning till Managed Identity

1. Navigera till Managed Identity-resursen som du skapade.

1. Välj **Azure role assignments** i vänstermenyn.

1. Välj **+ Add role assignment** i navigationsmenyn.

1. På sidan för rolltilldelning, utför följande:

    - Välj **Scope** till **Resource group**.
    - Välj din Azure **Subscription**.
    - Välj den **Resource group** som ska användas.
    - Välj rollen **Contributor**.

    ![Fyll i Contributor-roll.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.sv.png)

2. Välj **Save**.

#### Lägg till Storage Blob Data Reader-rolltilldelning till Managed Identity

1. Skriv *storage accounts* i **sökfältet** högst upp på portalsidan och välj **Storage accounts** från alternativen som visas.

    ![Skriv storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.sv.png)

1. Välj det storage account som är kopplat till Azure Machine Learning workspace som du skapade, till exempel *finetunephistorage*.

1. Utför följande steg för att navigera till sidan för rolltilldelning:

    - Navigera till det Azure Storage-konto du skapade.
    - Välj **Access Control (IAM)** i vänstermenyn.
    - Välj **+ Add** i navigationsmenyn.
    - Välj **Add role assignment** i navigationsmenyn.

    ![Lägg till roll.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.sv.png)

1. På sidan för rolltilldelning, utför följande:

    - Skriv *Storage Blob Data Reader* i **sökfältet** och välj **Storage Blob Data Reader** från alternativen.
    - Välj **Next**.
    - På sidan Members, välj **Assign access to** **Managed identity**.
    - Välj **+ Select members**.
    - Välj din Azure **Subscription**.
    - Välj **Managed identity** till **Manage Identity**.
    - Välj den Managed Identity som du skapade, till exempel *finetunephi-managedidentity*.
    - Välj **Select**.

    ![Välj Managed Identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.sv.png)

1. Välj **Review + assign**.

#### Lägg till AcrPull-rolltilldelning till Managed Identity

1. Skriv *container registries* i **sökfältet** högst upp på portalsidan och välj **Container registries** från alternativen som visas.

    ![Skriv container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.sv.png)

1. Välj den container registry som är kopplad till Azure Machine Learning workspace, till exempel *finetunephicontainerregistry*.

1. Utför följande steg för att navigera till sidan för rolltilldelning:

    - Välj **Access Control (IAM)** i vänstermenyn.
    - Välj **+ Add** i navigationsmenyn.
    - Välj **Add role assignment** i navigationsmenyn.

1. På sidan för rolltilldelning, utför följande:

    - Skriv *AcrPull* i **sökfältet** och välj **AcrPull** från alternativen.
    - Välj **Next**.
    - På sidan Members, välj **Assign access to** **Managed identity**.
    - Välj **+ Select members**.
    - Välj din Azure **Subscription**.
    - Välj **Managed identity** till **Manage Identity**.
    - Välj den Managed Identity som du skapade, till exempel *finetunephi-managedidentity*.
    - Välj **Select**.
    - Välj **Review + assign**.

### Sätt upp projekt

För att ladda ner de dataset som behövs för finjustering kommer du att sätta upp en lokal miljö.

I denna övning kommer du att:

- Skapa en mapp att arbeta i.
- Skapa en virtuell miljö.
- Installera de nödvändiga paketen.
- Skapa en fil *download_dataset.py* för att ladda ner datasetet.

#### Skapa en mapp att arbeta i

1. Öppna ett terminalfönster och skriv följande kommando för att skapa en mapp med namnet *finetune-phi* i standardvägen.

    ```console
    mkdir finetune-phi
    ```

2. Skriv följande kommando i terminalen för att navigera till mappen *finetune-phi* som du skapade.

    ```console
    cd finetune-phi
    ```

#### Skapa en virtuell miljö

1. Skriv följande kommando i terminalen för att skapa en virtuell miljö med namnet *.venv*.

    ```console
    python -m venv .venv
    ```

2. Skriv följande kommando i terminalen för att aktivera den virtuella miljön.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Om det fungerade bör du se *(.venv)* före kommandoprompten.

#### Installera de nödvändiga paketen

1. Skriv följande kommandon i terminalen för att installera de nödvändiga paketen.

    ```console
    pip install datasets==2.19.1
    ```

#### Skapa `download_dataset.py`

> [!NOTE]
> Komplett mappstruktur:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Öppna **Visual Studio Code**.

1. Välj **File** i menyraden.

1. Välj **Open Folder**.

1. Välj mappen *finetune-phi* som du skapade, som finns på *C:\Users\yourUserName\finetune-phi*.

    ![Välj mappen som du skapade.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.sv.png)

1. I vänstra panelen i Visual Studio Code, högerklicka och välj **New File** för att skapa en ny fil med namnet *download_dataset.py*.

    ![Skapa en ny fil.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.sv.png)

### Förbered dataset för finjustering

I denna övning kommer du att köra filen *download_dataset.py* för att ladda ner *ultrachat_200k*-dataseten till din lokala miljö. Du kommer sedan att använda dessa dataset för att finjustera Phi-3-modellen i Azure Machine Learning.

I denna övning kommer du att:

- Lägga till kod i filen *download_dataset.py* för att ladda ner dataseten.
- Köra filen *download_dataset.py* för att ladda ner dataseten till din lokala miljö.

#### Ladda ner ditt dataset med hjälp av *download_dataset.py*

1. Öppna filen *download_dataset.py* i Visual Studio Code.

1. Lägg till följande kod i filen *download_dataset.py*.

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

1. Skriv följande kommando i terminalen för att köra skriptet och ladda ner datasetet till din lokala miljö.

    ```console
    python download_dataset.py
    ```

1. Kontrollera att dataseten sparades framgångsrikt i din lokala katalog *finetune-phi/data*.

> [!NOTE]
>
> #### Notering om datasetets storlek och finjusteringstid
>
> I denna handledning använder du endast 1% av datasetet (`split='train[:1%]'`). Detta minskar mängden data avsevärt, vilket snabbar upp både uppladdnings- och finjusteringsprocesserna. Du kan justera procentandelen för att hitta rätt balans mellan träningstid och modellprestanda. Att använda en mindre delmängd av datasetet minskar tiden som krävs för finjustering, vilket gör processen mer hanterbar för en handledning.

## Scenario 2: Finjustera Phi-3-modellen och distribuera i Azure Machine Learning Studio

### Finjustera Phi-3-modellen

I denna övning kommer du att finjustera Phi-3-modellen i Azure Machine Learning Studio.

I denna övning kommer du att:

- Skapa en datorcluster för finjustering.
- Finjustera Phi-3-modellen i Azure Machine Learning Studio.

#### Skapa datorcluster för finjustering
1. Besök [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Välj **Compute** från fliken på vänster sida.

1. Välj **Compute clusters** i navigationsmenyn.

1. Välj **+ New**.

    ![Select compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.sv.png)

1. Utför följande uppgifter:

    - Välj den **Region** du vill använda.
    - Välj **Virtual machine tier** till **Dedicated**.
    - Välj **Virtual machine type** till **GPU**.
    - Välj filtret för **Virtual machine size** till **Select from all options**.
    - Välj **Virtual machine size** till **Standard_NC24ads_A100_v4**.

    ![Create cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.sv.png)

1. Välj **Next**.

1. Utför följande uppgifter:

    - Ange **Compute name**. Det måste vara ett unikt värde.
    - Välj **Minimum number of nodes** till **0**.
    - Välj **Maximum number of nodes** till **1**.
    - Välj **Idle seconds before scale down** till **120**.

    ![Create cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.sv.png)

1. Välj **Create**.

#### Finjustera Phi-3-modellen

1. Besök [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Välj den Azure Machine Learning-arbetsyta som du skapade.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.sv.png)

1. Utför följande uppgifter:

    - Välj **Model catalog** från fliken på vänster sida.
    - Skriv *phi-3-mini-4k* i **sökfältet** och välj **Phi-3-mini-4k-instruct** från alternativen som visas.

    ![Type phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.sv.png)

1. Välj **Fine-tune** i navigationsmenyn.

    ![Select fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.sv.png)

1. Utför följande uppgifter:

    - Välj **Select task type** till **Chat completion**.
    - Välj **+ Select data** för att ladda upp **Training data**.
    - Välj valideringsdatauppladdningstyp till **Provide different validation data**.
    - Välj **+ Select data** för att ladda upp **Validation data**.

    ![Fill fine-tuning page.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.sv.png)

    > [!TIP]
    >
    > Du kan välja **Advanced settings** för att anpassa inställningar som **learning_rate** och **lr_scheduler_type** för att optimera finjusteringsprocessen efter dina specifika behov.

1. Välj **Finish**.

1. I denna övning har du framgångsrikt finjusterat Phi-3-modellen med hjälp av Azure Machine Learning. Observera att finjusteringsprocessen kan ta en betydande tid. Efter att du har startat finjusteringsjobbet behöver du vänta på att det ska slutföras. Du kan följa status för finjusteringsjobbet genom att gå till fliken Jobs på vänster sida i din Azure Machine Learning-arbetsyta. I nästa serie kommer du att distribuera den finjusterade modellen och integrera den med Prompt flow.

    ![See finetuning job.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.sv.png)

### Distribuera den finjusterade Phi-3-modellen

För att integrera den finjusterade Phi-3-modellen med Prompt flow måste du distribuera modellen för att göra den tillgänglig för realtidsinferens. Denna process innebär att registrera modellen, skapa en online-endpoint och distribuera modellen.

I denna övning kommer du att:

- Registrera den finjusterade modellen i Azure Machine Learning-arbetsytan.
- Skapa en online-endpoint.
- Distribuera den registrerade finjusterade Phi-3-modellen.

#### Registrera den finjusterade modellen

1. Besök [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Välj den Azure Machine Learning-arbetsyta som du skapade.

    ![Select workspace that you created.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.sv.png)

1. Välj **Models** från fliken på vänster sida.
1. Välj **+ Register**.
1. Välj **From a job output**.

    ![Register model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.sv.png)

1. Välj jobbet som du skapade.

    ![Select job.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.sv.png)

1. Välj **Next**.

1. Välj **Model type** till **MLflow**.

1. Kontrollera att **Job output** är valt; det bör väljas automatiskt.

    ![Select output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.sv.png)

2. Välj **Next**.

3. Välj **Register**.

    ![Select register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.sv.png)

4. Du kan se din registrerade modell genom att gå till menyn **Models** från fliken på vänster sida.

    ![Registered model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.sv.png)

#### Distribuera den finjusterade modellen

1. Navigera till den Azure Machine Learning-arbetsyta som du skapade.

1. Välj **Endpoints** från fliken på vänster sida.

1. Välj **Real-time endpoints** i navigationsmenyn.

    ![Create endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.sv.png)

1. Välj **Create**.

1. Välj den registrerade modell som du skapade.

    ![Select registered model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.sv.png)

1. Välj **Select**.

1. Utför följande uppgifter:

    - Välj **Virtual machine** till *Standard_NC6s_v3*.
    - Välj det antal instanser (**Instance count**) du vill använda. Till exempel *1*.
    - Välj **Endpoint** till **New** för att skapa en endpoint.
    - Ange **Endpoint name**. Det måste vara ett unikt värde.
    - Ange **Deployment name**. Det måste vara ett unikt värde.

    ![Fill the deployment setting.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.sv.png)

1. Välj **Deploy**.

> [!WARNING]
> För att undvika extra kostnader på ditt konto, se till att ta bort den skapade endpointen i Azure Machine Learning-arbetsytan.
>

#### Kontrollera distributionsstatus i Azure Machine Learning Workspace

1. Navigera till Azure Machine Learning-arbetsytan som du skapade.

1. Välj **Endpoints** från fliken på vänster sida.

1. Välj den endpoint som du skapade.

    ![Select endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.sv.png)

1. På denna sida kan du hantera endpoints under distributionsprocessen.

> [!NOTE]
> När distributionen är klar, se till att **Live traffic** är inställt på **100%**. Om det inte är det, välj **Update traffic** för att justera trafikinställningarna. Observera att du inte kan testa modellen om trafiken är inställd på 0%.
>
> ![Set traffic.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.sv.png)
>

## Scenario 3: Integrera med Prompt flow och chatta med din anpassade modell i Azure AI Foundry

### Integrera den anpassade Phi-3-modellen med Prompt flow

Efter att du framgångsrikt har distribuerat din finjusterade modell kan du nu integrera den med Prompt Flow för att använda din modell i realtidsapplikationer, vilket möjliggör en mängd interaktiva uppgifter med din anpassade Phi-3-modell.

I denna övning kommer du att:

- Skapa Azure AI Foundry Hub.
- Skapa Azure AI Foundry-projekt.
- Skapa Prompt flow.
- Lägg till en anpassad anslutning för den finjusterade Phi-3-modellen.
- Ställ in Prompt flow för att chatta med din anpassade Phi-3-modell.

> [!NOTE]
> Du kan också integrera med Promptflow via Azure ML Studio. Samma integrationsprocess kan tillämpas på Azure ML Studio.

#### Skapa Azure AI Foundry Hub

Du måste skapa en Hub innan du skapar projektet. En Hub fungerar som en resursgrupp och låter dig organisera och hantera flera projekt inom Azure AI Foundry.

1. Besök [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Välj **All hubs** från fliken på vänster sida.

1. Välj **+ New hub** i navigationsmenyn.

    ![Create hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.sv.png)

1. Utför följande uppgifter:

    - Ange **Hub name**. Det måste vara ett unikt värde.
    - Välj din Azure **Subscription**.
    - Välj **Resource group** att använda (skapa en ny om det behövs).
    - Välj den **Location** du vill använda.
    - Välj **Connect Azure AI Services** att använda (skapa en ny om det behövs).
    - Välj **Connect Azure AI Search** till **Skip connecting**.

    ![Fill hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.sv.png)

1. Välj **Next**.

#### Skapa Azure AI Foundry-projekt

1. I den Hub du skapade, välj **All projects** från fliken på vänster sida.

1. Välj **+ New project** i navigationsmenyn.

    ![Select new project.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.sv.png)

1. Ange **Project name**. Det måste vara ett unikt värde.

    ![Create project.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.sv.png)

1. Välj **Create a project**.

#### Lägg till en anpassad anslutning för den finjusterade Phi-3-modellen

För att integrera din anpassade Phi-3-modell med Prompt flow behöver du spara modellens endpoint och nyckel i en anpassad anslutning. Denna inställning säkerställer åtkomst till din anpassade Phi-3-modell i Prompt flow.

#### Ange api-nyckel och endpoint-uri för den finjusterade Phi-3-modellen

1. Besök [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navigera till den Azure Machine Learning-arbetsyta som du skapade.

1. Välj **Endpoints** från fliken på vänster sida.

    ![Select endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.sv.png)

1. Välj endpoint som du skapade.

    ![Select endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.sv.png)

1. Välj **Consume** i navigationsmenyn.

1. Kopiera din **REST endpoint** och **Primary key**.
![Kopiera api-nyckel och endpoint-uri.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.sv.png)

#### Lägg till den anpassade anslutningen

1. Besök [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navigera till det Azure AI Foundry-projekt som du skapade.

1. I projektet du skapade, välj **Settings** från fliken till vänster.

1. Välj **+ New connection**.

    ![Välj ny anslutning.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.sv.png)

1. Välj **Custom keys** från navigationsmenyn.

    ![Välj anpassade nycklar.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.sv.png)

1. Utför följande uppgifter:

    - Välj **+ Add key value pairs**.
    - För nyckelnamn, skriv **endpoint** och klistra in endpoint som du kopierade från Azure ML Studio i värdefältet.
    - Välj **+ Add key value pairs** igen.
    - För nyckelnamn, skriv **key** och klistra in nyckeln som du kopierade från Azure ML Studio i värdefältet.
    - Efter att ha lagt till nycklarna, välj **is secret** för att förhindra att nyckeln exponeras.

    ![Lägg till anslutning.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.sv.png)

1. Välj **Add connection**.

#### Skapa Prompt flow

Du har lagt till en anpassad anslutning i Azure AI Foundry. Nu ska vi skapa en Prompt flow med följande steg. Därefter kopplar du denna Prompt flow till den anpassade anslutningen så att du kan använda den finjusterade modellen inom Prompt flow.

1. Navigera till det Azure AI Foundry-projekt som du skapade.

1. Välj **Prompt flow** från fliken till vänster.

1. Välj **+ Create** från navigationsmenyn.

    ![Välj Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.sv.png)

1. Välj **Chat flow** från navigationsmenyn.

    ![Välj chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.sv.png)

1. Ange **Folder name** som ska användas.

    ![Ange namn.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.sv.png)

2. Välj **Create**.

#### Konfigurera Prompt flow för att chatta med din anpassade Phi-3-modell

Du behöver integrera den finjusterade Phi-3-modellen i en Prompt flow. Den befintliga Prompt flow som tillhandahålls är dock inte utformad för detta ändamål. Därför måste du bygga om Prompt flow för att möjliggöra integration av den anpassade modellen.

1. I Prompt flow, utför följande för att bygga om det befintliga flödet:

    - Välj **Raw file mode**.
    - Radera all befintlig kod i filen *flow.dag.yml*.
    - Lägg till följande kod i filen *flow.dag.yml*.

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

    - Välj **Save**.

    ![Välj raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.sv.png)

1. Lägg till följande kod i filen *integrate_with_promptflow.py* för att använda den anpassade Phi-3-modellen i Prompt flow.

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

    ![Klistra in prompt flow-koden.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.sv.png)

> [!NOTE]
> För mer detaljerad information om hur du använder Prompt flow i Azure AI Foundry kan du se [Prompt flow i Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Välj **Chat input**, **Chat output** för att aktivera chatt med din modell.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.sv.png)

1. Nu är du redo att chatta med din anpassade Phi-3-modell. I nästa övning lär du dig hur du startar Prompt flow och använder det för att chatta med din finjusterade Phi-3-modell.

> [!NOTE]
>
> Det ombyggda flödet bör se ut som bilden nedan:
>
> ![Flödesexempel.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.sv.png)
>

### Chatta med din anpassade Phi-3-modell

Nu när du har finjusterat och integrerat din anpassade Phi-3-modell med Prompt flow är du redo att börja interagera med den. Den här övningen guidar dig genom processen att ställa in och starta en chatt med din modell med hjälp av Prompt flow. Genom att följa dessa steg kommer du kunna utnyttja din finjusterade Phi-3-modells kapacitet fullt ut för olika uppgifter och konversationer.

- Chatta med din anpassade Phi-3-modell med hjälp av Prompt flow.

#### Starta Prompt flow

1. Välj **Start compute sessions** för att starta Prompt flow.

    ![Starta compute session.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.sv.png)

1. Välj **Validate and parse input** för att uppdatera parametrar.

    ![Validera input.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.sv.png)

1. Välj **Value** för **connection** till den anpassade anslutning du skapade. Till exempel, *connection*.

    ![Anslutning.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.sv.png)

#### Chatta med din anpassade modell

1. Välj **Chat**.

    ![Välj chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.sv.png)

1. Här är ett exempel på resultaten: Nu kan du chatta med din anpassade Phi-3-modell. Det rekommenderas att ställa frågor baserade på den data som användes för finjusteringen.

    ![Chatta med prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.sv.png)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig uppmärksam på att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.