<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "455be2b7b9c3390d367d528f8fab2aa0",
  "translation_date": "2025-07-17T00:05:21+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "de"
}
-->
# Feinabstimmung und Integration benutzerdefinierter Phi-3-Modelle mit Prompt flow

Dieses End-to-End (E2E) Beispiel basiert auf der Anleitung "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" aus der Microsoft Tech Community. Es stellt die Prozesse der Feinabstimmung, Bereitstellung und Integration benutzerdefinierter Phi-3-Modelle mit Prompt flow vor.

## Überblick

In diesem E2E-Beispiel lernen Sie, wie Sie das Phi-3-Modell feinabstimmen und mit Prompt flow integrieren. Durch die Nutzung von Azure Machine Learning und Prompt flow erstellen Sie einen Workflow zur Bereitstellung und Nutzung benutzerdefinierter KI-Modelle. Dieses E2E-Beispiel ist in drei Szenarien unterteilt:

**Szenario 1: Azure-Ressourcen einrichten und Vorbereitung der Feinabstimmung**

**Szenario 2: Feinabstimmung des Phi-3-Modells und Bereitstellung im Azure Machine Learning Studio**

**Szenario 3: Integration mit Prompt flow und Chat mit Ihrem benutzerdefinierten Modell**

Hier ist eine Übersicht über dieses E2E-Beispiel.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.02fc569e266d468cf3bbb3158cf273380cbdf7fcec042c7328e1559c6b2e2632.de.png)

### Inhaltsverzeichnis

1. **[Szenario 1: Azure-Ressourcen einrichten und Vorbereitung der Feinabstimmung](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Erstellen eines Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Anfordern von GPU-Kontingenten im Azure-Abonnement](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Rollen-Zuweisung hinzufügen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Projekt einrichten](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Datensatz für Feinabstimmung vorbereiten](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Szenario 2: Feinabstimmung des Phi-3-Modells und Bereitstellung im Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure CLI einrichten](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Phi-3-Modell feinabstimmen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Feinabgestimmtes Modell bereitstellen](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Szenario 3: Integration mit Prompt flow und Chat mit Ihrem benutzerdefinierten Modell](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Benutzerdefiniertes Phi-3-Modell mit Prompt flow integrieren](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Chat mit Ihrem benutzerdefinierten Modell](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Szenario 1: Azure-Ressourcen einrichten und Vorbereitung der Feinabstimmung

### Erstellen eines Azure Machine Learning Workspace

1. Geben Sie *azure machine learning* in die **Suchleiste** oben auf der Portal-Seite ein und wählen Sie **Azure Machine Learning** aus den angezeigten Optionen aus.

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.a5116f8454d98c600d87008fb78206d2cf90c0b920c231618a8ec8baaa6f46c3.de.png)

1. Wählen Sie **+ Erstellen** im Navigationsmenü aus.

1. Wählen Sie **Neuen Workspace** im Navigationsmenü aus.

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.83e17436f8898dc4fbb808d1bbcd92962692b1fa687f4c5d3952f453177825bc.de.png)

1. Führen Sie die folgenden Schritte aus:

    - Wählen Sie Ihr Azure **Abonnement**.
    - Wählen Sie die **Ressourcengruppe** aus (erstellen Sie bei Bedarf eine neue).
    - Geben Sie den **Workspace-Namen** ein. Dieser muss eindeutig sein.
    - Wählen Sie die **Region** aus, die Sie verwenden möchten.
    - Wählen Sie das **Speicherkonto** aus (erstellen Sie bei Bedarf ein neues).
    - Wählen Sie den **Key Vault** aus (erstellen Sie bei Bedarf einen neuen).
    - Wählen Sie die **Application Insights** aus (erstellen Sie bei Bedarf eine neue).
    - Wählen Sie die **Container-Registry** aus (erstellen Sie bei Bedarf eine neue).

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.730a5177757bbebb141b9e8c16f31834e82e831275bd9faad0b70343f46255de.de.png)

1. Wählen Sie **Überprüfen + Erstellen**.

1. Wählen Sie **Erstellen**.

### Anfordern von GPU-Kontingenten im Azure-Abonnement

In diesem E2E-Beispiel verwenden Sie die *Standard_NC24ads_A100_v4 GPU* für die Feinabstimmung, die eine Kontingentanfrage erfordert, und die *Standard_E4s_v3* CPU für die Bereitstellung, die keine Kontingentanfrage benötigt.

> [!NOTE]
>
> Nur Pay-As-You-Go-Abonnements (der Standard-Abonnementtyp) sind für die GPU-Zuweisung berechtigt; Benefit-Abonnements werden derzeit nicht unterstützt.
>
> Für Nutzer von Benefit-Abonnements (wie Visual Studio Enterprise Subscription) oder für diejenigen, die den Feinabstimmungs- und Bereitstellungsprozess schnell testen möchten, bietet dieses Tutorial auch Anleitungen zur Feinabstimmung mit einem minimalen Datensatz auf einer CPU. Es ist jedoch wichtig zu beachten, dass die Feinabstimmungsergebnisse mit einer GPU und größeren Datensätzen deutlich besser sind.

1. Besuchen Sie [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Führen Sie die folgenden Schritte aus, um das Kontingent für die *Standard NCADSA100v4 Family* anzufordern:

    - Wählen Sie **Kontingent** im linken Seitenmenü.
    - Wählen Sie die **Virtuelle Maschinenfamilie** aus. Zum Beispiel **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, die die *Standard_NC24ads_A100_v4* GPU enthält.
    - Wählen Sie **Kontingent anfordern** im Navigationsmenü.

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.3d3670c3221ab8348515fcfba9d0279114f04065df8bd6fb78e3d3704e627545.de.png)

    - Geben Sie auf der Seite zur Kontingentanfrage das gewünschte **Neue Kernlimit** ein, z. B. 24.
    - Wählen Sie **Absenden**, um das GPU-Kontingent anzufordern.

> [!NOTE]
> Sie können die passende GPU oder CPU für Ihre Anforderungen anhand des Dokuments [Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) auswählen.

### Rollen-Zuweisung hinzufügen

Um Ihre Modelle feinabzustimmen und bereitzustellen, müssen Sie zunächst eine User Assigned Managed Identity (UAI) erstellen und ihr die entsprechenden Berechtigungen zuweisen. Diese UAI wird für die Authentifizierung während der Bereitstellung verwendet.

#### Erstellen einer User Assigned Managed Identity (UAI)

1. Geben Sie *managed identities* in die **Suchleiste** oben auf der Portal-Seite ein und wählen Sie **Managed Identities** aus den angezeigten Optionen aus.

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.9297b6039874eff8a95d6e7762f1b087275a9634677f0a4e355717550ace3c02.de.png)

1. Wählen Sie **+ Erstellen**.

    ![Select create.](../../../../../../translated_images/01-06-select-create.936d8d66d7144f9a8c70af922bf28a573c0744fb642f8228d62214b010a070d9.de.png)

1. Führen Sie die folgenden Schritte aus:

    - Wählen Sie Ihr Azure **Abonnement**.
    - Wählen Sie die **Ressourcengruppe** aus (erstellen Sie bei Bedarf eine neue).
    - Wählen Sie die **Region** aus, die Sie verwenden möchten.
    - Geben Sie den **Namen** ein. Dieser muss eindeutig sein.

1. Wählen Sie **Überprüfen + Erstellen**.

1. Wählen Sie **+ Erstellen**.

#### Zuweisung der Rolle „Contributor“ zur Managed Identity hinzufügen

1. Navigieren Sie zur Managed Identity-Ressource, die Sie erstellt haben.

1. Wählen Sie **Azure-Rollen-Zuweisungen** im linken Seitenmenü.

1. Wählen Sie **+ Rolle zuweisen** im Navigationsmenü.

1. Führen Sie auf der Seite „Rolle zuweisen“ die folgenden Schritte aus:
    - Wählen Sie den **Geltungsbereich** auf **Ressourcengruppe**.
    - Wählen Sie Ihr Azure **Abonnement**.
    - Wählen Sie die **Ressourcengruppe** aus.
    - Wählen Sie die **Rolle** **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.29ca99b7c9f687e008e224cf336687c04c9fe24740e47e34ce041b50b47e0ed1.de.png)

1. Wählen Sie **Speichern**.

#### Zuweisung der Rolle „Storage Blob Data Reader“ zur Managed Identity hinzufügen

1. Geben Sie *storage accounts* in die **Suchleiste** oben auf der Portal-Seite ein und wählen Sie **Storage accounts** aus den angezeigten Optionen aus.

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.1186c8e42933e49bcd9cce3ffd1b6218afb6e5c3700b628da7b7c294be71b911.de.png)

1. Wählen Sie das Speicherkonto aus, das mit dem Azure Machine Learning Workspace verknüpft ist, den Sie erstellt haben. Zum Beispiel *finetunephistorage*.

1. Führen Sie die folgenden Schritte aus, um zur Seite „Rolle zuweisen“ zu gelangen:

    - Navigieren Sie zum Azure Storage-Konto, das Sie erstellt haben.
    - Wählen Sie **Zugriffssteuerung (IAM)** im linken Seitenmenü.
    - Wählen Sie **+ Hinzufügen** im Navigationsmenü.
    - Wählen Sie **Rolle zuweisen** im Navigationsmenü.

    ![Add role.](../../../../../../translated_images/01-09-add-role.d2db22fec1b187f0ae84790d65dc5726a9b57c496d916b8700d41e0b3b468451.de.png)

1. Führen Sie auf der Seite „Rolle zuweisen“ die folgenden Schritte aus:

    - Geben Sie im Suchfeld der Rolle *Storage Blob Data Reader* ein und wählen Sie **Storage Blob Data Reader** aus den angezeigten Optionen aus.
    - Wählen Sie **Weiter**.
    - Wählen Sie auf der Seite „Mitglieder“ unter **Zugriff zuweisen an** die Option **Managed identity**.
    - Wählen Sie **+ Mitglieder auswählen**.
    - Wählen Sie auf der Seite „Managed Identities auswählen“ Ihr Azure **Abonnement**.
    - Wählen Sie die **Managed Identity** unter **Managed Identity** aus.
    - Wählen Sie die Managed Identity aus, die Sie erstellt haben, z. B. *finetunephi-managedidentity*.
    - Wählen Sie **Auswählen**.

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.5ce5ba181f72a4df788963e1dc0a68c39ee297363aabe979b487c60b3037662f.de.png)

1. Wählen Sie **Überprüfen + zuweisen**.

#### Zuweisung der Rolle „AcrPull“ zur Managed Identity hinzufügen

1. Geben Sie *container registries* in die **Suchleiste** oben auf der Portal-Seite ein und wählen Sie **Container registries** aus den angezeigten Optionen aus.

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.ff3b8bdc49dc596c64c0f778633c652ce08e4ac28f142a17afc10de81bb8c336.de.png)

1. Wählen Sie die Container-Registry aus, die mit dem Azure Machine Learning Workspace verknüpft ist. Zum Beispiel *finetunephicontainerregistries*.

1. Führen Sie die folgenden Schritte aus, um zur Seite „Rolle zuweisen“ zu gelangen:

    - Wählen Sie **Zugriffssteuerung (IAM)** im linken Seitenmenü.
    - Wählen Sie **+ Hinzufügen** im Navigationsmenü.
    - Wählen Sie **Rolle zuweisen** im Navigationsmenü.

1. Führen Sie auf der Seite „Rolle zuweisen“ die folgenden Schritte aus:

    - Geben Sie im Suchfeld der Rolle *AcrPull* ein und wählen Sie **AcrPull** aus den angezeigten Optionen aus.
    - Wählen Sie **Weiter**.
    - Wählen Sie auf der Seite „Mitglieder“ unter **Zugriff zuweisen an** die Option **Managed identity**.
    - Wählen Sie **+ Mitglieder auswählen**.
    - Wählen Sie auf der Seite „Managed Identities auswählen“ Ihr Azure **Abonnement**.
    - Wählen Sie die **Managed Identity** unter **Managed Identity** aus.
    - Wählen Sie die Managed Identity aus, die Sie erstellt haben, z. B. *finetunephi-managedidentity*.
    - Wählen Sie **Auswählen**.
    - Wählen Sie **Überprüfen + zuweisen**.

### Projekt einrichten

Nun erstellen Sie einen Ordner, in dem Sie arbeiten, und richten eine virtuelle Umgebung ein, um ein Programm zu entwickeln, das mit Benutzern interagiert und gespeicherte Chatverläufe aus Azure Cosmos DB nutzt, um seine Antworten zu verbessern.

#### Erstellen eines Arbeitsordners

1. Öffnen Sie ein Terminalfenster und geben Sie den folgenden Befehl ein, um einen Ordner namens *finetune-phi* im Standardpfad zu erstellen.

    ```console
    mkdir finetune-phi
    ```

1. Geben Sie im Terminal den folgenden Befehl ein, um in den erstellten Ordner *finetune-phi* zu wechseln.

    ```console
    cd finetune-phi
    ```

#### Erstellen einer virtuellen Umgebung

1. Geben Sie im Terminal den folgenden Befehl ein, um eine virtuelle Umgebung namens *.venv* zu erstellen.

    ```console
    python -m venv .venv
    ```

1. Geben Sie im Terminal den folgenden Befehl ein, um die virtuelle Umgebung zu aktivieren.

    ```console
    .venv\Scripts\activate.bat
    ```
> [!NOTE]
>
> Wenn es geklappt hat, solltest du *(.venv)* vor der Eingabeaufforderung sehen.
#### Installieren Sie die erforderlichen Pakete

1. Geben Sie die folgenden Befehle in Ihrem Terminal ein, um die benötigten Pakete zu installieren.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Erstellen Sie Projektdateien

In dieser Übung erstellen Sie die wichtigsten Dateien für unser Projekt. Diese Dateien umfassen Skripte zum Herunterladen des Datensatzes, zum Einrichten der Azure Machine Learning-Umgebung, zum Feinabstimmen des Phi-3-Modells und zum Bereitstellen des feinabgestimmten Modells. Außerdem erstellen Sie eine *conda.yml*-Datei, um die Feinabstimmungsumgebung einzurichten.

In dieser Übung werden Sie:

- Eine *download_dataset.py*-Datei erstellen, um den Datensatz herunterzuladen.
- Eine *setup_ml.py*-Datei erstellen, um die Azure Machine Learning-Umgebung einzurichten.
- Eine *fine_tune.py*-Datei im Ordner *finetuning_dir* erstellen, um das Phi-3-Modell mit dem Datensatz fein abzustimmen.
- Eine *conda.yml*-Datei erstellen, um die Feinabstimmungsumgebung einzurichten.
- Eine *deploy_model.py*-Datei erstellen, um das feinabgestimmte Modell bereitzustellen.
- Eine *integrate_with_promptflow.py*-Datei erstellen, um das feinabgestimmte Modell zu integrieren und mit Prompt Flow auszuführen.
- Eine flow.dag.yml-Datei erstellen, um die Workflow-Struktur für Prompt Flow einzurichten.
- Eine *config.py*-Datei erstellen, um Azure-Informationen einzutragen.

> [!NOTE]
>
> Vollständige Ordnerstruktur:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        ├── finetuning_dir
> .        │      └── fine_tune.py
> .        ├── conda.yml
> .        ├── config.py
> .        ├── deploy_model.py
> .        ├── download_dataset.py
> .        ├── flow.dag.yml
> .        ├── integrate_with_promptflow.py
> .        └── setup_ml.py
> ```

1. Öffnen Sie **Visual Studio Code**.

1. Wählen Sie in der Menüleiste **Datei** aus.

1. Wählen Sie **Ordner öffnen**.

1. Wählen Sie den Ordner *finetune-phi* aus, den Sie erstellt haben, der sich unter *C:\Users\yourUserName\finetune-phi* befindet.

    ![Projektordner öffnen.](../../../../../../translated_images/01-12-open-project-folder.1fff9c7f41dd1639c12e7da258ac8b3deca260786edb07598e206725cd1593ce.de.png)

1. Klicken Sie im linken Bereich von Visual Studio Code mit der rechten Maustaste und wählen Sie **Neue Datei**, um eine neue Datei namens *download_dataset.py* zu erstellen.

1. Klicken Sie im linken Bereich von Visual Studio Code mit der rechten Maustaste und wählen Sie **Neue Datei**, um eine neue Datei namens *setup_ml.py* zu erstellen.

1. Klicken Sie im linken Bereich von Visual Studio Code mit der rechten Maustaste und wählen Sie **Neue Datei**, um eine neue Datei namens *deploy_model.py* zu erstellen.

    ![Neue Datei erstellen.](../../../../../../translated_images/01-13-create-new-file.c17c150fff384a398766a39eac9f15240a9a4da566bd8dca86f471e78eadc69e.de.png)

1. Klicken Sie im linken Bereich von Visual Studio Code mit der rechten Maustaste und wählen Sie **Neuer Ordner**, um einen neuen Ordner namens *finetuning_dir* zu erstellen.

1. Erstellen Sie im Ordner *finetuning_dir* eine neue Datei namens *fine_tune.py*.

#### Erstellen und Konfigurieren der *conda.yml*-Datei

1. Klicken Sie im linken Bereich von Visual Studio Code mit der rechten Maustaste und wählen Sie **Neue Datei**, um eine neue Datei namens *conda.yml* zu erstellen.

1. Fügen Sie den folgenden Code in die *conda.yml*-Datei ein, um die Feinabstimmungsumgebung für das Phi-3-Modell einzurichten.

    ```yml
    name: phi-3-training-env
    channels:
      - defaults
      - conda-forge
    dependencies:
      - python=3.10
      - pip
      - numpy<2.0
      - pip:
          - torch==2.4.0
          - torchvision==0.19.0
          - trl==0.8.6
          - transformers==4.41
          - datasets==2.21.0
          - azureml-core==1.57.0
          - azure-storage-blob==12.19.0
          - azure-ai-ml==1.16
          - azure-identity==1.17.1
          - accelerate==0.33.0
          - mlflow==2.15.1
          - azureml-mlflow==1.57.0
    ```

#### Erstellen und Konfigurieren der *config.py*-Datei

1. Klicken Sie im linken Bereich von Visual Studio Code mit der rechten Maustaste und wählen Sie **Neue Datei**, um eine neue Datei namens *config.py* zu erstellen.

1. Fügen Sie den folgenden Code in die *config.py*-Datei ein, um Ihre Azure-Informationen einzutragen.

    ```python
    # Azure settings
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Azure Machine Learning settings
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Azure Managed Identity settings
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Dataset file paths
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Fine-tuned model settings
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### Azure-Umgebungsvariablen hinzufügen

1. Führen Sie die folgenden Schritte aus, um die Azure Subscription ID hinzuzufügen:

    - Geben Sie *subscriptions* in die **Suchleiste** oben auf der Portal-Seite ein und wählen Sie **Subscriptions** aus den angezeigten Optionen aus.
    - Wählen Sie die Azure Subscription aus, die Sie aktuell verwenden.
    - Kopieren Sie Ihre Subscription ID und fügen Sie sie in die *config.py*-Datei ein.

    ![Subscription-ID finden.](../../../../../../translated_images/01-14-find-subscriptionid.4f4ca33555f1e637e01163bfdd2a606e7d06f05455ab56e05cb5107e938e7a90.de.png)

1. Führen Sie die folgenden Schritte aus, um den Azure Workspace-Namen hinzuzufügen:

    - Navigieren Sie zur Azure Machine Learning-Ressource, die Sie erstellt haben.
    - Kopieren Sie Ihren Kontonamen und fügen Sie ihn in die *config.py*-Datei ein.

    ![Azure Machine Learning-Namen finden.](../../../../../../translated_images/01-15-find-AZML-name.1975f0422bca19a702b1bb5e9d8e9f5e5424abe066a0ff310da980582e65721f.de.png)

1. Führen Sie die folgenden Schritte aus, um den Azure Resource Group-Namen hinzuzufügen:

    - Navigieren Sie zur Azure Machine Learning-Ressource, die Sie erstellt haben.
    - Kopieren Sie den Namen Ihrer Azure Resource Group und fügen Sie ihn in die *config.py*-Datei ein.

    ![Resource Group-Namen finden.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.855a349d0af134a399243d7c94d5aabd86070ab6535d3cf2ec38c78538626666.de.png)

2. Führen Sie die folgenden Schritte aus, um den Azure Managed Identity-Namen hinzuzufügen:

    - Navigieren Sie zur Managed Identities-Ressource, die Sie erstellt haben.
    - Kopieren Sie den Namen Ihrer Azure Managed Identity und fügen Sie ihn in die *config.py*-Datei ein.

    ![UAI finden.](../../../../../../translated_images/01-17-find-uai.3529464f534998271ea7c5aebafa887051567417f3b4244ff58fdd443192b6d7.de.png)

### Datensatz für die Feinabstimmung vorbereiten

In dieser Übung führen Sie die *download_dataset.py*-Datei aus, um die *ULTRACHAT_200k*-Datensätze in Ihre lokale Umgebung herunterzuladen. Anschließend verwenden Sie diese Datensätze, um das Phi-3-Modell in Azure Machine Learning fein abzustimmen.

#### Laden Sie Ihren Datensatz mit *download_dataset.py* herunter

1. Öffnen Sie die *download_dataset.py*-Datei in Visual Studio Code.

1. Fügen Sie den folgenden Code in *download_dataset.py* ein.

    ```python
    import json
    import os
    from datasets import load_dataset
    from config import (
        TRAIN_DATA_PATH,
        TEST_DATA_PATH)

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
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **Hinweise zur Feinabstimmung mit einem minimalen Datensatz auf einer CPU**
>
> Wenn Sie eine CPU für die Feinabstimmung verwenden möchten, ist dieser Ansatz ideal für Nutzer mit Benefit-Subscriptions (wie Visual Studio Enterprise Subscription) oder um den Feinabstimmungs- und Bereitstellungsprozess schnell zu testen.
>
> Ersetzen Sie `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` durch `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Geben Sie den folgenden Befehl in Ihrem Terminal ein, um das Skript auszuführen und den Datensatz in Ihre lokale Umgebung herunterzuladen.

    ```console
    python download_data.py
    ```

1. Überprüfen Sie, ob die Datensätze erfolgreich im lokalen Verzeichnis *finetune-phi/data* gespeichert wurden.

> [!NOTE]
>
> **Datensatzgröße und Feinabstimmungsdauer**
>
> In diesem End-to-End-Beispiel verwenden Sie nur 1 % des Datensatzes (`train_sft[:1%]`). Dies reduziert die Datenmenge erheblich und beschleunigt sowohl den Upload als auch den Feinabstimmungsprozess. Sie können den Prozentsatz anpassen, um das richtige Gleichgewicht zwischen Trainingszeit und Modellleistung zu finden. Die Verwendung eines kleineren Teils des Datensatzes verkürzt die Feinabstimmungszeit und macht den Prozess für ein End-to-End-Beispiel besser handhabbar.

## Szenario 2: Feinabstimmung des Phi-3-Modells und Bereitstellung in Azure Machine Learning Studio

### Azure CLI einrichten

Sie müssen die Azure CLI einrichten, um Ihre Umgebung zu authentifizieren. Die Azure CLI ermöglicht es Ihnen, Azure-Ressourcen direkt über die Befehlszeile zu verwalten und stellt die erforderlichen Anmeldeinformationen bereit, damit Azure Machine Learning auf diese Ressourcen zugreifen kann. Um zu beginnen, installieren Sie [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. Öffnen Sie ein Terminalfenster und geben Sie den folgenden Befehl ein, um sich bei Ihrem Azure-Konto anzumelden.

    ```console
    az login
    ```

1. Wählen Sie Ihr Azure-Konto aus, das Sie verwenden möchten.

1. Wählen Sie Ihre Azure-Subscription aus, die Sie verwenden möchten.

    ![Resource Group-Namen finden.](../../../../../../translated_images/02-01-login-using-azure-cli.dfde31cb75e58a8792c687d36e4fc4f4ee37fd76640e6e4e5aed3329513f2328.de.png)

> [!TIP]
>
> Wenn Sie Probleme bei der Anmeldung bei Azure haben, versuchen Sie es mit einem Gerätecode. Öffnen Sie ein Terminalfenster und geben Sie den folgenden Befehl ein, um sich bei Ihrem Azure-Konto anzumelden:
>
> ```console
> az login --use-device-code
> ```
>

### Feinabstimmung des Phi-3-Modells

In dieser Übung stimmen Sie das Phi-3-Modell mit dem bereitgestellten Datensatz fein ab. Zuerst definieren Sie den Feinabstimmungsprozess in der *fine_tune.py*-Datei. Anschließend konfigurieren Sie die Azure Machine Learning-Umgebung und starten den Feinabstimmungsprozess, indem Sie die *setup_ml.py*-Datei ausführen. Dieses Skript stellt sicher, dass die Feinabstimmung innerhalb der Azure Machine Learning-Umgebung erfolgt.

Durch Ausführen von *setup_ml.py* starten Sie den Feinabstimmungsprozess in der Azure Machine Learning-Umgebung.

#### Code zur *fine_tune.py*-Datei hinzufügen

1. Navigieren Sie zum Ordner *finetuning_dir* und öffnen Sie die *fine_tune.py*-Datei in Visual Studio Code.

1. Fügen Sie den folgenden Code in *fine_tune.py* ein.

    ```python
    import argparse
    import sys
    import logging
    import os
    from datasets import load_dataset
    import torch
    import mlflow
    from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
    from trl import SFTTrainer

    # To avoid the INVALID_PARAMETER_VALUE error in MLflow, disable MLflow integration
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
        level=logging.WARNING
    )
    logger = logging.getLogger(__name__)

    def initialize_model_and_tokenizer(model_name, model_kwargs):
        """
        Initialize the model and tokenizer with the given pretrained model name and arguments.
        """
        model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.model_max_length = 2048
        tokenizer.pad_token = tokenizer.unk_token
        tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids(tokenizer.pad_token)
        tokenizer.padding_side = 'right'
        return model, tokenizer

    def apply_chat_template(example, tokenizer):
        """
        Apply a chat template to tokenize messages in the example.
        """
        messages = example["messages"]
        if messages[0]["role"] != "system":
            messages.insert(0, {"role": "system", "content": ""})
        example["text"] = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        return example

    def load_and_preprocess_data(train_filepath, test_filepath, tokenizer):
        """
        Load and preprocess the dataset.
        """
        train_dataset = load_dataset('json', data_files=train_filepath, split='train')
        test_dataset = load_dataset('json', data_files=test_filepath, split='train')
        column_names = list(train_dataset.features)

        train_dataset = train_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to train dataset",
        )

        test_dataset = test_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to test dataset",
        )

        return train_dataset, test_dataset

    def train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, output_dir):
        """
        Train and evaluate the model.
        """
        training_args = TrainingArguments(
            bf16=True,
            do_eval=True,
            output_dir=output_dir,
            eval_strategy="epoch",
            learning_rate=5.0e-06,
            logging_steps=20,
            lr_scheduler_type="cosine",
            num_train_epochs=3,
            overwrite_output_dir=True,
            per_device_eval_batch_size=4,
            per_device_train_batch_size=4,
            remove_unused_columns=True,
            save_steps=500,
            seed=0,
            gradient_checkpointing=True,
            gradient_accumulation_steps=1,
            warmup_ratio=0.2,
        )

        trainer = SFTTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            max_seq_length=2048,
            dataset_text_field="text",
            tokenizer=tokenizer,
            packing=True
        )

        train_result = trainer.train()
        trainer.log_metrics("train", train_result.metrics)

        mlflow.transformers.log_model(
            transformers_model={"model": trainer.model, "tokenizer": tokenizer},
            artifact_path=output_dir,
        )

        tokenizer.padding_side = 'left'
        eval_metrics = trainer.evaluate()
        eval_metrics["eval_samples"] = len(test_dataset)
        trainer.log_metrics("eval", eval_metrics)

    def main(train_file, eval_file, model_output_dir):
        """
        Main function to fine-tune the model.
        """
        model_kwargs = {
            "use_cache": False,
            "trust_remote_code": True,
            "torch_dtype": torch.bfloat16,
            "device_map": None,
            "attn_implementation": "eager"
        }

        # pretrained_model_name = "microsoft/Phi-3-mini-4k-instruct"
        pretrained_model_name = "microsoft/Phi-3.5-mini-instruct"

        with mlflow.start_run():
            model, tokenizer = initialize_model_and_tokenizer(pretrained_model_name, model_kwargs)
            train_dataset, test_dataset = load_and_preprocess_data(train_file, eval_file, tokenizer)
            train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, model_output_dir)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--train-file", type=str, required=True, help="Path to the training data")
        parser.add_argument("--eval-file", type=str, required=True, help="Path to the evaluation data")
        parser.add_argument("--model_output_dir", type=str, required=True, help="Directory to save the fine-tuned model")
        args = parser.parse_args()
        main(args.train_file, args.eval_file, args.model_output_dir)

    ```

1. Speichern und schließen Sie die *fine_tune.py*-Datei.

> [!TIP]
> **Sie können das Phi-3.5-Modell fein abstimmen**
>
> In der *fine_tune.py*-Datei können Sie den Wert von `pretrained_model_name` von `"microsoft/Phi-3-mini-4k-instruct"` auf jedes beliebige Modell ändern, das Sie fein abstimmen möchten. Wenn Sie es beispielsweise auf `"microsoft/Phi-3.5-mini-instruct"` ändern, verwenden Sie das Phi-3.5-mini-instruct-Modell für die Feinabstimmung. Um den Modellnamen zu finden und zu verwenden, den Sie bevorzugen, besuchen Sie [Hugging Face](https://huggingface.co/), suchen Sie nach dem gewünschten Modell und kopieren Sie dessen Namen in das Feld `pretrained_model_name` in Ihrem Skript.
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Phi-3.5 fein abstimmen.":::
>

#### Code zur *setup_ml.py*-Datei hinzufügen

1. Öffnen Sie die *setup_ml.py*-Datei in Visual Studio Code.

1. Fügen Sie den folgenden Code in *setup_ml.py* ein.

    ```python
    import logging
    from azure.ai.ml import MLClient, command, Input
    from azure.ai.ml.entities import Environment, AmlCompute
    from azure.identity import AzureCliCredential
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        TRAIN_DATA_PATH,
        TEST_DATA_PATH
    )

    # Constants

    # Uncomment the following lines to use a CPU instance for training
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    FINETUNING_DIR = "./finetuning_dir" # Path to the fine-tuning script
    TRAINING_ENV_NAME = "phi-3-training-environment" # Name of the training environment
    MODEL_OUTPUT_DIR = "./model_output" # Path to the model output directory in azure ml

    # Logging setup to track the process
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.WARNING
    )

    def get_ml_client():
        """
        Initialize the ML Client using Azure CLI credentials.
        """
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def create_or_get_environment(ml_client):
        """
        Create or update the training environment in Azure ML.
        """
        env = Environment(
            image=DOCKER_IMAGE_NAME,  # Docker image for the environment
            conda_file=CONDA_FILE,  # Conda environment file
            name=TRAINING_ENV_NAME,  # Name of the environment
        )
        return ml_client.environments.create_or_update(env)

    def create_or_get_compute_cluster(ml_client, compute_name, COMPUTE_INSTANCE_TYPE, location):
        """
        Create or update the compute cluster in Azure ML.
        """
        try:
            compute_cluster = ml_client.compute.get(compute_name)
            logger.info(f"Compute cluster '{compute_name}' already exists. Reusing it for the current run.")
        except Exception:
            logger.info(f"Compute cluster '{compute_name}' does not exist. Creating a new one with size {COMPUTE_INSTANCE_TYPE}.")
            compute_cluster = AmlCompute(
                name=compute_name,
                size=COMPUTE_INSTANCE_TYPE,
                location=location,
                tier="Dedicated",  # Tier of the compute cluster
                min_instances=0,  # Minimum number of instances
                max_instances=1  # Maximum number of instances
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Wait for the cluster to be created
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Path to fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Training environment
            compute=compute_name,  # Compute cluster to use
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Path to the training data file
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Path to the evaluation data file
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Initialize ML Client
        ml_client = get_ml_client()

        # Create Environment
        env = create_or_get_environment(ml_client)
        
        # Create or get existing compute cluster
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Create and Submit Fine-Tuning Job
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Submit the job
        ml_client.jobs.stream(returned_job.name)  # Stream the job logs
        
        # Capture the job name
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. Ersetzen Sie `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` und `LOCATION` durch Ihre spezifischen Angaben.

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **Hinweise zur Feinabstimmung mit einem minimalen Datensatz auf einer CPU**
>
> Wenn Sie eine CPU für die Feinabstimmung verwenden möchten, ist dieser Ansatz ideal für Nutzer mit Benefit-Subscriptions (wie Visual Studio Enterprise Subscription) oder um den Feinabstimmungs- und Bereitstellungsprozess schnell zu testen.
>
> 1. Öffnen Sie die *setup_ml*-Datei.
> 1. Ersetzen Sie `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` und `DOCKER_IMAGE_NAME` wie folgt. Wenn Sie keinen Zugriff auf *Standard_E16s_v3* haben, können Sie eine gleichwertige CPU-Instanz verwenden oder eine neue Kontingentanforderung stellen.
> 1. Ersetzen Sie `LOCATION` durch Ihre spezifischen Angaben.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Geben Sie den folgenden Befehl ein, um das *setup_ml.py*-Skript auszuführen und den Feinabstimmungsprozess in Azure Machine Learning zu starten.

    ```python
    python setup_ml.py
    ```

1. In dieser Übung haben Sie das Phi-3-Modell erfolgreich mit Azure Machine Learning fein abgestimmt. Durch Ausführen des *setup_ml.py*-Skripts haben Sie die Azure Machine Learning-Umgebung eingerichtet und den in der *fine_tune.py*-Datei definierten Feinabstimmungsprozess gestartet. Bitte beachten Sie, dass der Feinabstimmungsprozess eine beträchtliche Zeit in Anspruch nehmen kann. Nach dem Ausführen des Befehls `python setup_ml.py` müssen Sie warten, bis der Prozess abgeschlossen ist. Sie können den Status des Feinabstimmungsjobs über den im Terminal bereitgestellten Link zum Azure Machine Learning-Portal überwachen.

    ![Feinabstimmungsjob anzeigen.](../../../../../../translated_images/02-02-see-finetuning-job.59393bc3b143871ee8ba32fa508cc4018c0f04e51ad14b95c421ad77151f768f.de.png)

### Bereitstellen des feinabgestimmten Modells

Um das feinabgestimmte Phi-3-Modell mit Prompt Flow zu integrieren, müssen Sie das Modell bereitstellen, damit es für Echtzeit-Inferenz zugänglich ist. Dieser Prozess umfasst die Registrierung des Modells, das Erstellen eines Online-Endpunkts und die Bereitstellung des Modells.

#### Legen Sie den Modellnamen, Endpunktnamen und Bereitstellungsnamen für die Bereitstellung fest

1. Öffnen Sie die *config.py*-Datei.

1. Ersetzen Sie `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` durch den gewünschten Namen für Ihr Modell.

1. Ersetzen Sie `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` durch den gewünschten Namen für Ihren Endpunkt.

1. Ersetzen Sie `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` durch den gewünschten Namen für Ihre Bereitstellung.

#### Code zur *deploy_model.py*-Datei hinzufügen

Das Ausführen der *deploy_model.py*-Datei automatisiert den gesamten Bereitstellungsprozess. Sie registriert das Modell, erstellt einen Endpunkt und führt die Bereitstellung basierend auf den in der *config.py*-Datei angegebenen Einstellungen aus, die den Modellnamen, Endpunktnamen und Bereitstellungsnamen enthalten.

1. Öffnen Sie die *deploy_model.py*-Datei in Visual Studio Code.

1. Fügen Sie den folgenden Code in *deploy_model.py* ein.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Configuration imports
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        AZURE_MANAGED_IDENTITY_RESOURCE_ID,
        AZURE_MANAGED_IDENTITY_CLIENT_ID,
        AZURE_MODEL_NAME,
        AZURE_ENDPOINT_NAME,
        AZURE_DEPLOYMENT_NAME
    )

    # Constants
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def get_ml_client():
        """Initialize and return the ML Client."""
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def register_model(ml_client, model_name, job_name):
        """Register a new model."""
        model_path = f"azureml://jobs/{job_name}/outputs/artifacts/paths/model_output"
        logger.info(f"Registering model {model_name} from job {job_name} at path {model_path}.")
        run_model = Model(
            path=model_path,
            name=model_name,
            description="Model created from run.",
            type=AssetTypes.MLFLOW_MODEL,
        )
        model = ml_client.models.create_or_update(run_model)
        logger.info(f"Registered model ID: {model.id}")
        return model

    def delete_existing_endpoint(ml_client, endpoint_name):
        """Delete existing endpoint if it exists."""
        try:
            endpoint_result = ml_client.online_endpoints.get(name=endpoint_name)
            logger.info(f"Deleting existing endpoint {endpoint_name}.")
            ml_client.online_endpoints.begin_delete(name=endpoint_name).result()
            logger.info(f"Deleted existing endpoint {endpoint_name}.")
        except Exception as e:
            logger.info(f"No existing endpoint {endpoint_name} found to delete: {e}")

    def create_or_update_endpoint(ml_client, endpoint_name, description=""):
        """Create or update an endpoint."""
        delete_existing_endpoint(ml_client, endpoint_name)
        logger.info(f"Creating new endpoint {endpoint_name}.")
        endpoint = ManagedOnlineEndpoint(
            name=endpoint_name,
            description=description,
            identity=IdentityConfiguration(
                type="user_assigned",
                user_assigned_identities=[ManagedIdentityConfiguration(resource_id=AZURE_MANAGED_IDENTITY_RESOURCE_ID)]
            )
        )
        endpoint_result = ml_client.online_endpoints.begin_create_or_update(endpoint).result()
        logger.info(f"Created new endpoint {endpoint_name}.")
        return endpoint_result

    def create_or_update_deployment(ml_client, endpoint_name, deployment_name, model):
        """Create or update a deployment."""

        logger.info(f"Creating deployment {deployment_name} for endpoint {endpoint_name}.")
        deployment = ManagedOnlineDeployment(
            name=deployment_name,
            endpoint_name=endpoint_name,
            model=model.id,
            instance_type=COMPUTE_INSTANCE_TYPE,
            instance_count=1,
            environment_variables=deployment_env_vars,
            request_settings=OnlineRequestSettings(
                max_concurrent_requests_per_instance=3,
                request_timeout_ms=180000,
                max_queue_wait_ms=120000
            ),
            liveness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
            readiness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
        )
        deployment_result = ml_client.online_deployments.begin_create_or_update(deployment).result()
        logger.info(f"Created deployment {deployment.name} for endpoint {endpoint_name}.")
        return deployment_result

    def set_traffic_to_deployment(ml_client, endpoint_name, deployment_name):
        """Set traffic to the specified deployment."""
        try:
            # Fetch the current endpoint details
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Log the current traffic allocation for debugging
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Set the traffic allocation for the deployment
            endpoint.traffic = {deployment_name: 100}
            
            # Update the endpoint with the new traffic allocation
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Log the updated traffic allocation for debugging
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Log any errors that occur during the process
            logger.error(f"Failed to set traffic to deployment: {e}")
            raise


    def main():
        ml_client = get_ml_client()

        registered_model = register_model(ml_client, AZURE_MODEL_NAME, JOB_NAME)
        logger.info(f"Registered model ID: {registered_model.id}")

        endpoint = create_or_update_endpoint(ml_client, AZURE_ENDPOINT_NAME, "Endpoint for finetuned Phi-3 model")
        logger.info(f"Endpoint {AZURE_ENDPOINT_NAME} is ready.")

        try:
            deployment = create_or_update_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME, registered_model)
            logger.info(f"Deployment {AZURE_DEPLOYMENT_NAME} is created for endpoint {AZURE_ENDPOINT_NAME}.")

            set_traffic_to_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME)
            logger.info(f"Traffic is set to deployment {AZURE_DEPLOYMENT_NAME} at endpoint {AZURE_ENDPOINT_NAME}.")
        except Exception as e:
            logger.error(f"Failed to create or update deployment: {e}")

    if __name__ == "__main__":
        main()

    ```

1. Führen Sie die folgenden Schritte aus, um den `JOB_NAME` zu erhalten:

    - Navigieren Sie zur Azure Machine Learning-Ressource, die Sie erstellt haben.
    - Wählen Sie **Studio web URL** aus, um den Azure Machine Learning-Arbeitsbereich zu öffnen.
    - Wählen Sie im linken Bereich **Jobs** aus.
    - Wählen Sie das Experiment für die Feinabstimmung aus, z. B. *finetunephi*.
    - Wählen Sie den Job aus, den Sie erstellt haben.
- Kopieren Sie Ihren Jobnamen und fügen Sie ihn in `JOB_NAME = "your-job-name"` in der Datei *deploy_model.py* ein.

1. Ersetzen Sie `COMPUTE_INSTANCE_TYPE` durch Ihre spezifischen Angaben.

1. Geben Sie den folgenden Befehl ein, um das Skript *deploy_model.py* auszuführen und den Bereitstellungsprozess in Azure Machine Learning zu starten.

    ```python
    python deploy_model.py
    ```


> [!WARNING]
> Um zusätzliche Kosten auf Ihrem Konto zu vermeiden, stellen Sie sicher, dass Sie den erstellten Endpunkt im Azure Machine Learning Workspace löschen.
>

#### Überprüfen des Bereitstellungsstatus im Azure Machine Learning Workspace

1. Besuchen Sie [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navigieren Sie zu dem Azure Machine Learning Workspace, den Sie erstellt haben.

1. Wählen Sie **Studio web URL**, um den Azure Machine Learning Workspace zu öffnen.

1. Wählen Sie **Endpoints** im linken Seitenmenü aus.

    ![Select endpoints.](../../../../../../translated_images/02-03-select-endpoints.c3136326510baff109f3b7a6b6e4e9689f99b2d7bf021b057f6c0ecbd1ba90c0.de.png)

2. Wählen Sie den von Ihnen erstellten Endpunkt aus.

    ![Select endpoints that you created.](../../../../../../translated_images/02-04-select-endpoint-created.0363e7dca51dabb4b726505fcfb7d262b0510de029dcbaf36422bb75b77f25dd.de.png)

3. Auf dieser Seite können Sie die während des Bereitstellungsprozesses erstellten Endpunkte verwalten.

## Szenario 3: Integration mit Prompt flow und Chatten mit Ihrem benutzerdefinierten Modell

### Integration des benutzerdefinierten Phi-3 Modells mit Prompt flow

Nachdem Sie Ihr feinabgestimmtes Modell erfolgreich bereitgestellt haben, können Sie es nun mit Prompt flow integrieren, um Ihr Modell in Echtzeitanwendungen zu verwenden und so eine Vielzahl interaktiver Aufgaben mit Ihrem benutzerdefinierten Phi-3 Modell zu ermöglichen.

#### API-Schlüssel und Endpunkt-URI des feinabgestimmten Phi-3 Modells festlegen

1. Navigieren Sie zu dem Azure Machine Learning Workspace, den Sie erstellt haben.
1. Wählen Sie **Endpoints** im linken Seitenmenü aus.
1. Wählen Sie den von Ihnen erstellten Endpunkt aus.
1. Wählen Sie **Consume** im Navigationsmenü.
1. Kopieren Sie Ihren **REST endpoint** und fügen Sie ihn in die Datei *config.py* ein, indem Sie `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` durch Ihren **REST endpoint** ersetzen.
1. Kopieren Sie Ihren **Primary key** und fügen Sie ihn in die Datei *config.py* ein, indem Sie `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` durch Ihren **Primary key** ersetzen.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/02-05-copy-apikey-endpoint.88b5a92e6462c53bf44401e184f65a0a088daa76a65f5df5eb4489ae40b890f6.de.png)

#### Code zur *flow.dag.yml* Datei hinzufügen

1. Öffnen Sie die Datei *flow.dag.yml* in Visual Studio Code.

1. Fügen Sie den folgenden Code in *flow.dag.yml* ein.

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

#### Code zur *integrate_with_promptflow.py* Datei hinzufügen

1. Öffnen Sie die Datei *integrate_with_promptflow.py* in Visual Studio Code.

1. Fügen Sie den folgenden Code in *integrate_with_promptflow.py* ein.

    ```python
    import logging
    import requests
    from promptflow.core import tool
    import asyncio
    import platform
    from config import (
        AZURE_ML_ENDPOINT,
        AZURE_ML_API_KEY
    )

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_azml_endpoint(input_data: list, endpoint_url: str, api_key: str) -> str:
        """
        Send a request to the Azure ML endpoint with the given input data.
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": [input_data],
            "params": {
                "temperature": 0.7,
                "max_new_tokens": 128,
                "do_sample": True,
                "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()[0]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    def setup_asyncio_policy():
        """
        Setup asyncio event loop policy for Windows.
        """
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            logger.info("Set Windows asyncio event loop policy.")

    @tool
    def my_python_tool(input_data: str) -> str:
        """
        Tool function to process input data and query the Azure ML endpoint.
        """
        setup_asyncio_policy()
        return query_azml_endpoint(input_data, AZURE_ML_ENDPOINT, AZURE_ML_API_KEY)

    ```

### Chatten mit Ihrem benutzerdefinierten Modell

1. Geben Sie den folgenden Befehl ein, um das Skript *deploy_model.py* auszuführen und den Bereitstellungsprozess in Azure Machine Learning zu starten.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Hier ein Beispiel für die Ergebnisse: Nun können Sie mit Ihrem benutzerdefinierten Phi-3 Modell chatten. Es wird empfohlen, Fragen basierend auf den für das Fine-Tuning verwendeten Daten zu stellen.

    ![Prompt flow example.](../../../../../../translated_images/02-06-promptflow-example.89384abaf3ad71f6412447c9786c562be969a8c3b19791eadffce725fa84f014.de.png)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.