<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7ca2c30fdb802664070e9cfbf92e24fe",
  "translation_date": "2026-01-05T08:19:25+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/E2E_Phi-3-FineTuning_PromptFlow_Integration.md",
  "language_code": "de"
}
-->
# Feinabstimmung und Integration benutzerdefinierter Phi-3-Modelle mit Prompt Flow

Dieses End-to-End (E2E) Beispiel basiert auf der Anleitung "[Feinabstimmung und Integration benutzerdefinierter Phi-3-Modelle mit Prompt Flow: Schritt-für-Schritt-Anleitung](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" aus der Microsoft Tech Community. Es stellt die Prozesse der Feinabstimmung, Bereitstellung und Integration benutzerdefinierter Phi-3-Modelle mit Prompt Flow vor.

## Überblick

In diesem E2E-Beispiel lernen Sie, wie Sie das Phi-3-Modell feinabstimmen und es mit Prompt Flow integrieren. Durch die Nutzung von Azure Machine Learning und Prompt Flow erstellen Sie einen Workflow zur Bereitstellung und Nutzung benutzerdefinierter KI-Modelle. Dieses E2E-Beispiel ist in drei Szenarien unterteilt:

**Szenario 1: Azure-Ressourcen einrichten und Vorbereitung für die Feinabstimmung**

**Szenario 2: Feinabstimmung des Phi-3-Modells und Bereitstellung im Azure Machine Learning Studio**

**Szenario 3: Integration mit Prompt Flow und Chat mit Ihrem benutzerdefinierten Modell**

Hier ist eine Übersicht zu diesem E2E-Beispiel.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.02fc569e266d468c.de.png)

### Inhaltsverzeichnis

1. **[Szenario 1: Azure-Ressourcen einrichten und Vorbereitung für die Feinabstimmung](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Erstellen eines Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Anfordern von GPU-Kontingenten im Azure-Abonnement](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Hinzufügen einer Rollenzuweisung](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Projekt einrichten](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Datensatz für Feinabstimmung vorbereiten](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Szenario 2: Feinabstimmung des Phi-3-Modells und Bereitstellung im Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure CLI einrichten](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Feinabstimmung des Phi-3-Modells](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Bereitstellen des feinabgestimmten Modells](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Szenario 3: Integration mit Prompt Flow und Chat mit Ihrem benutzerdefinierten Modell](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integration des benutzerdefinierten Phi-3-Modells mit Prompt Flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Chat mit Ihrem benutzerdefinierten Modell](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Szenario 1: Azure-Ressourcen einrichten und Vorbereitung für die Feinabstimmung

### Erstellen eines Azure Machine Learning Workspace

1. Geben Sie *azure machine learning* in der **Suchleiste** oben auf der Portalseite ein und wählen Sie **Azure Machine Learning** aus den angezeigten Optionen aus.

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.a5116f8454d98c60.de.png)

1. Wählen Sie im Navigationsmenü **+ Erstellen** aus.

1. Wählen Sie im Navigationsmenü **Neuen Workspace** aus.

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.83e17436f8898dc4.de.png)

1. Führen Sie folgende Aufgaben aus:

    - Wählen Sie Ihr Azure **Abonnement**.
    - Wählen Sie die **Ressourcengruppe** aus (bei Bedarf neu erstellen).
    - Geben Sie den **Workspace-Namen** ein. Er muss einzigartig sein.
    - Wählen Sie die **Region**, die Sie verwenden möchten.
    - Wählen Sie das **Speicherkonto** aus (bei Bedarf neu erstellen).
    - Wählen Sie den **Key Vault** aus (bei Bedarf neu erstellen).
    - Wählen Sie die **Application Insights** aus (bei Bedarf neu erstellen).
    - Wählen Sie das **Container-Registry** aus (bei Bedarf neu erstellen).

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.730a5177757bbebb.de.png)

1. Wählen Sie **Überprüfen + Erstellen**.

1. Wählen Sie **Erstellen**.

### Anfordern von GPU-Kontingenten im Azure-Abonnement

In diesem E2E-Beispiel verwenden Sie die *Standard_NC24ads_A100_v4 GPU* für die Feinabstimmung, die eine Kontingentanfrage erfordert, und die *Standard_E4s_v3* CPU für die Bereitstellung, die keine Kontingentanfrage benötigt.

> [!NOTE]
>
> Nur Pay-As-You-Go-Abonnements (Standard-Abonnementtyp) sind für die GPU-Zuweisung berechtigt; Vorteilsabonnements werden derzeit nicht unterstützt.
>
> Für Benutzer von Vorteilsabonnements (z. B. Visual Studio Enterprise Subscription) oder die den Feinabstimmungs- und Bereitstellungsprozess schnell testen möchten, bietet dieses Tutorial auch Hinweise zur Feinabstimmung mit einem minimalen Datensatz unter Verwendung einer CPU. Es ist jedoch wichtig zu beachten, dass die Feinabstimmungsergebnisse deutlich besser sind, wenn eine GPU mit größeren Datensätzen verwendet wird.

1. Besuchen Sie [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Führen Sie die folgenden Schritte aus, um das Kontingent *Standard NCADSA100v4 Family* anzufordern:

    - Wählen Sie auf der linken Seitenleiste **Kontingent** aus.
    - Wählen Sie die **Virtuelle Maschinen-Familie** aus, die Sie verwenden möchten. Beispielsweise wählen Sie **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, das die *Standard_NC24ads_A100_v4* GPU beinhaltet.
    - Wählen Sie im Navigationsmenü **Kontingent anfordern**.

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.3d3670c3221ab834.de.png)

    - Geben Sie auf der Seite Kontingent anfordern das **Neue Kernlimit** ein, das Sie verwenden möchten. Beispielsweise 24.
    - Wählen Sie auf der Seite Kontingent anfordern **Absenden**, um das GPU-Kontingent anzufordern.

> [!NOTE]
> Sie können die passende GPU oder CPU für Ihre Bedürfnisse anhand des Dokuments [Größen für virtuelle Maschinen in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) auswählen.

### Hinzufügen einer Rollenzuweisung

Um Ihre Modelle feinabzustimmen und bereitzustellen, müssen Sie zuerst eine benutzerzugewiesene verwaltete Identität (User Assigned Managed Identity, UAI) erstellen und ihr die entsprechenden Berechtigungen zuweisen. Diese UAI wird für die Authentifizierung während der Bereitstellung verwendet.

#### Erstellen einer benutzerzugewiesenen verwalteten Identität (UAI)

1. Geben Sie *managed identities* in der **Suchleiste** oben auf der Portalseite ein und wählen Sie **Verwaltete Identitäten** aus den angezeigten Optionen aus.

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.9297b6039874eff8.de.png)

1. Wählen Sie **+ Erstellen**.

    ![Select create.](../../../../../../translated_images/01-06-select-create.936d8d66d7144f9a.de.png)

1. Führen Sie die folgenden Aufgaben aus:

    - Wählen Sie Ihr Azure **Abonnement**.
    - Wählen Sie die **Ressourcengruppe** aus (bei Bedarf neu erstellen).
    - Wählen Sie die **Region**, die Sie verwenden möchten.
    - Geben Sie den **Namen** ein. Er muss einzigartig sein.

1. Wählen Sie **Überprüfen + Erstellen**.

1. Wählen Sie **+ Erstellen**.

#### Hinzufügen der Rolle Mitwirkender (Contributor) zu der verwalteten Identität

1. Navigieren Sie zur verwalteten Identitätsressource, die Sie erstellt haben.

1. Wählen Sie auf der linken Seitenleiste **Azure-Rollenzuweisungen** aus.

1. Wählen Sie im Navigationsmenü **+ Rolle zuweisen** aus.

1. Führen Sie auf der Seite Rolle zuweisen folgende Aufgaben aus:
    - Wählen Sie den **Geltungsbereich** als **Ressourcengruppe** aus.
    - Wählen Sie Ihr Azure **Abonnement** aus.
    - Wählen Sie die **Ressourcengruppe** aus.
    - Wählen Sie die **Rolle** als **Mitwirkender (Contributor)** aus.

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.29ca99b7c9f687e0.de.png)

1. Wählen Sie **Speichern**.

#### Hinzufügen der Rolle Storage Blob Data Reader zu der verwalteten Identität

1. Geben Sie *storage accounts* in der **Suchleiste** oben auf der Portalseite ein und wählen Sie **Speicherkonten** aus den angezeigten Optionen aus.

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.1186c8e42933e49b.de.png)

1. Wählen Sie das Speicherkonto aus, das mit dem Azure Machine Learning Workspace verbunden ist, den Sie erstellt haben. Zum Beispiel *finetunephistorage*.

1. Führen Sie die folgenden Schritte aus, um zur Seite Rolle hinzufügen zu navigieren:

    - Navigieren Sie zum Azure-Speicherkonto, das Sie erstellt haben.
    - Wählen Sie auf der linken Seitenleiste **Zugriffskontrolle (IAM)** aus.
    - Wählen Sie im Navigationsmenü **+ Hinzufügen**.
    - Wählen Sie im Navigationsmenü **Rolle hinzufügen**.

    ![Add role.](../../../../../../translated_images/01-09-add-role.d2db22fec1b187f0.de.png)

1. Führen Sie auf der Seite Rolle hinzufügen folgende Aufgaben aus:

    - Geben Sie auf der Rollenseite *Storage Blob Data Reader* in die **Suchleiste** ein und wählen Sie **Storage Blob Data Reader** aus den angezeigten Optionen aus.
    - Wählen Sie auf der Rollenseite **Weiter** aus.
    - Wählen Sie auf der Seite Mitglieder unter **Zugriff zuweisen an** **Verwaltete Identität** aus.
    - Wählen Sie auf der Seite Mitglieder **+ Mitglieder auswählen** aus.
    - Wählen Sie auf der Seite Auswahl verwalteter Identitäten Ihr Azure **Abonnement** aus.
    - Wählen Sie auf der Seite Auswahl verwalteter Identitäten die **Verwaltete Identität** als **Verwaltete Identität** aus.
    - Wählen Sie auf der Seite Auswahl verwalteter Identitäten die von Ihnen erstellte verwaltete Identität aus. Zum Beispiel *finetunephi-managedidentity*.
    - Wählen Sie auf der Seite Auswahl verwalteter Identitäten **Auswählen**.

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.5ce5ba181f72a4df.de.png)

1. Wählen Sie **Überprüfen + Zuweisen**.

#### Hinzufügen der Rolle AcrPull zu der verwalteten Identität

1. Geben Sie *container registries* in der **Suchleiste** oben auf der Portalseite ein und wählen Sie **Container-Registrierungen** aus den angezeigten Optionen aus.

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.ff3b8bdc49dc596c.de.png)

1. Wählen Sie die Container-Registrierung aus, die mit dem Azure Machine Learning Workspace verbunden ist. Zum Beispiel *finetunephicontainerregistries*

1. Führen Sie die folgenden Schritte aus, um zur Seite Rolle hinzufügen zu navigieren:

    - Wählen Sie auf der linken Seitenleiste **Zugriffskontrolle (IAM)** aus.
    - Wählen Sie im Navigationsmenü **+ Hinzufügen**.
    - Wählen Sie im Navigationsmenü **Rolle hinzufügen**.

1. Führen Sie auf der Seite Rolle hinzufügen folgende Aufgaben aus:

    - Geben Sie auf der Rollenseite *AcrPull* in die **Suchleiste** ein und wählen Sie **AcrPull** aus den angezeigten Optionen aus.
    - Wählen Sie auf der Rollenseite **Weiter** aus.
    - Wählen Sie auf der Seite Mitglieder unter **Zugriff zuweisen an** **Verwaltete Identität** aus.
    - Wählen Sie auf der Seite Mitglieder **+ Mitglieder auswählen** aus.
    - Wählen Sie auf der Seite Auswahl verwalteter Identitäten Ihr Azure **Abonnement** aus.
    - Wählen Sie auf der Seite Auswahl verwalteter Identitäten die **Verwaltete Identität** als **Verwaltete Identität** aus.
    - Wählen Sie auf der Seite Auswahl verwalteter Identitäten die von Ihnen erstellte verwaltete Identität aus. Zum Beispiel *finetunephi-managedidentity*.
    - Wählen Sie auf der Seite Auswahl verwalteter Identitäten **Auswählen**.
    - Wählen Sie **Überprüfen + Zuweisen**.

### Projekt einrichten

Jetzt erstellen Sie einen Ordner, in dem Sie arbeiten, und richten eine virtuelle Umgebung ein, um ein Programm zu entwickeln, das mit Benutzern interagiert und gespeicherte Chatverläufe aus Azure Cosmos DB verwendet, um seine Antworten zu informieren.

#### Erstellen eines Arbeitsordners

1. Öffnen Sie ein Terminalfenster und geben Sie den folgenden Befehl ein, um einen Ordner namens *finetune-phi* im Standardpfad zu erstellen.

    ```console
    mkdir finetune-phi
    ```

1. Geben Sie den folgenden Befehl in Ihrem Terminal ein, um zum erstellten Ordner *finetune-phi* zu navigieren.

    ```console
    cd finetune-phi
    ```

#### Erstellen einer virtuellen Umgebung

1. Geben Sie den folgenden Befehl in Ihrem Terminal ein, um eine virtuelle Umgebung mit dem Namen *.venv* zu erstellen.

    ```console
    python -m venv .venv
    ```

1. Geben Sie den folgenden Befehl in Ihrem Terminal ein, um die virtuelle Umgebung zu aktivieren.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> Wenn es funktioniert hat, sollten Sie *(.venv)* vor der Eingabeaufforderung sehen.

#### Installieren der erforderlichen Pakete

1. Geben Sie die folgenden Befehle in Ihrem Terminal ein, um die erforderlichen Pakete zu installieren.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Projektdateien erstellen
In dieser Übung erstellen Sie die wesentlichen Dateien für unser Projekt. Diese Dateien umfassen Skripte zum Herunterladen des Datensatzes, zum Einrichten der Azure Machine Learning-Umgebung, zum Feinabstimmen des Phi-3-Modells und zum Bereitstellen des feinabgestimmten Modells. Sie erstellen auch eine *conda.yml*-Datei für die Einrichtung der Feinabstimmungsumgebung.

In dieser Übung werden Sie:

- Eine *download_dataset.py*-Datei erstellen, um den Datensatz herunterzuladen.
- Eine *setup_ml.py*-Datei erstellen, um die Azure Machine Learning-Umgebung einzurichten.
- Eine *fine_tune.py*-Datei im Ordner *finetuning_dir* erstellen, um das Phi-3-Modell mit dem Datensatz fein abzustimmen.
- Eine *conda.yml*-Datei zur Einrichtung der Feinabstimmungsumgebung erstellen.
- Eine *deploy_model.py*-Datei erstellen, um das feinabgestimmte Modell bereitzustellen.
- Eine *integrate_with_promptflow.py*-Datei erstellen, um das feinabgestimmte Modell zu integrieren und das Modell mit Prompt Flow auszuführen.
- Eine flow.dag.yml-Datei erstellen, um die Arbeitsablaufstruktur für Prompt Flow einzurichten.
- Eine *config.py*-Datei erstellen, um die Azure-Informationen einzutragen.

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

1. Wählen Sie in der Menüleiste **Datei**.

1. Wählen Sie **Ordner öffnen**.

1. Wählen Sie den Ordner *finetune-phi* aus, den Sie erstellt haben, der sich unter *C:\Users\yourUserName\finetune-phi* befindet.

    ![Projektordner öffnen.](../../../../../../translated_images/01-12-open-project-folder.1fff9c7f41dd1639.de.png)

1. Klicken Sie im linken Bereich von Visual Studio Code mit der rechten Maustaste und wählen Sie **Neue Datei**, um eine neue Datei namens *download_dataset.py* zu erstellen.

1. Klicken Sie im linken Bereich von Visual Studio Code mit der rechten Maustaste und wählen Sie **Neue Datei**, um eine neue Datei namens *setup_ml.py* zu erstellen.

1. Klicken Sie im linken Bereich von Visual Studio Code mit der rechten Maustaste und wählen Sie **Neue Datei**, um eine neue Datei namens *deploy_model.py* zu erstellen.

    ![Neue Datei erstellen.](../../../../../../translated_images/01-13-create-new-file.c17c150fff384a39.de.png)

1. Klicken Sie im linken Bereich von Visual Studio Code mit der rechten Maustaste und wählen Sie **Neuer Ordner**, um einen neuen Ordner namens *finetuning_dir* zu erstellen.

1. Erstellen Sie im Ordner *finetuning_dir* eine neue Datei namens *fine_tune.py*.

#### Erstellen und Konfigurieren der *conda.yml*-Datei

1. Klicken Sie im linken Bereich von Visual Studio Code mit der rechten Maustaste und wählen Sie **Neue Datei**, um eine neue Datei namens *conda.yml* zu erstellen.

1. Fügen Sie den folgenden Code in die Datei *conda.yml* ein, um die Feinabstimmungsumgebung für das Phi-3-Modell einzurichten.

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

1. Fügen Sie den folgenden Code in die Datei *config.py* ein, um Ihre Azure-Informationen zu ergänzen.

    ```python
    # Azure-Einstellungen
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "Testgruppe"

    # Azure Machine Learning-Einstellungen
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-arbeitsbereich"

    # Azure Managed Identity-Einstellungen
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-managedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # Pfade zu Datensatzdateien
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # Einstellungen für feingetuntes Modell
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-modell"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpunkt"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-bereitstellung"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{Ihr-Endpunktname}.{Ihre-Region}.inference.ml.azure.com/score"
    ```

#### Azure-Umgebungsvariablen hinzufügen

1. Führen Sie folgende Aufgaben aus, um die Azure Subscription-ID hinzuzufügen:

    - Geben Sie *subscriptions* in die **Suchleiste** oben auf der Portal-Seite ein und wählen Sie **Subscriptions** aus den angezeigten Optionen.
    - Wählen Sie die Azure Subscription aus, die Sie aktuell verwenden.
    - Kopieren Sie Ihre Subscription-ID und fügen Sie sie in die Datei *config.py* ein.

    ![Subscription-ID finden.](../../../../../../translated_images/01-14-find-subscriptionid.4f4ca33555f1e637.de.png)

1. Führen Sie folgende Aufgaben aus, um den Azure Workspace-Namen hinzuzufügen:

    - Navigieren Sie zur erstellten Azure Machine Learning-Ressource.
    - Kopieren Sie Ihren Kontonamen und fügen Sie ihn in die Datei *config.py* ein.

    ![Azure Machine Learning Name finden.](../../../../../../translated_images/01-15-find-AZML-name.1975f0422bca19a7.de.png)

1. Führen Sie folgende Aufgaben aus, um den Azure Resource Group-Namen hinzuzufügen:

    - Navigieren Sie zur erstellten Azure Machine Learning-Ressource.
    - Kopieren Sie Ihren Azure Resource Group-Namen und fügen Sie ihn in die Datei *config.py* ein.

    ![Resource Group Name finden.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.855a349d0af134a3.de.png)

2. Führen Sie folgende Aufgaben aus, um den Azure Managed Identity-Namen hinzuzufügen:

    - Navigieren Sie zur erstellten Managed Identities-Ressource.
    - Kopieren Sie Ihren Azure Managed Identity-Namen und fügen Sie ihn in die Datei *config.py* ein.

    ![UAI finden.](../../../../../../translated_images/01-17-find-uai.3529464f53499827.de.png)

### Vorbereitung des Datensatzes für die Feinabstimmung

In dieser Übung führen Sie die Datei *download_dataset.py* aus, um die *ULTRACHAT_200k*-Datensätze in Ihre lokale Umgebung herunterzuladen. Anschließend verwenden Sie diesen Datensatz, um das Phi-3-Modell in Azure Machine Learning fein abzustimmen.

#### Laden Sie Ihren Datensatz mit *download_dataset.py* herunter

1. Öffnen Sie die Datei *download_dataset.py* in Visual Studio Code.

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
        # Laden Sie den Datensatz mit dem angegebenen Namen, der Konfiguration und dem Aufteilungsverhältnis
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Teilen Sie den Datensatz in Trainings- und Testsets auf (80 % Training, 20 % Test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Erstellen Sie das Verzeichnis, falls es nicht existiert
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Öffnen Sie die Datei im Schreibmodus
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterieren Sie über jeden Datensatz im Datensatz
            for record in dataset:
                # Speichern Sie den Datensatz als JSON-Objekt und schreiben Sie ihn in die Datei
                json.dump(record, f)
                # Schreiben Sie ein Zeilenumbruchzeichen, um Datensätze zu trennen
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Laden und Aufteilen des ULTRACHAT_200k-Datensatzes mit einer bestimmten Konfiguration und einem bestimmten Aufteilungsverhältnis
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extrahieren Sie die Trainings- und Testdatensätze aus der Aufteilung
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Speichern Sie den Trainingsdatensatz in einer JSONL-Datei
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Speichern Sie den Testdatensatz in einer separaten JSONL-Datei
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **Anleitung zur Feinabstimmung mit einem minimalen Datensatz auf einer CPU**
>
> Wenn Sie eine CPU für die Feinabstimmung verwenden möchten, ist dieser Ansatz ideal für diejenigen mit Vorteil-Abonnements (wie Visual Studio Enterprise Subscription) oder zum schnellen Testen des Feinabstimmungs- und Bereitstellungsprozesses.
>
> Ersetzen Sie `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` durch `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Geben Sie den folgenden Befehl im Terminal ein, um das Skript auszuführen und den Datensatz in Ihre lokale Umgebung herunterzuladen.

    ```console
    python download_data.py
    ```

1. Überprüfen Sie, ob die Datensätze erfolgreich im lokalen Verzeichnis *finetune-phi/data* gespeichert wurden.

> [!NOTE]
>
> **Datensatzgröße und Feinabstimmungszeit**
>
> In diesem E2E-Beispiel verwenden Sie nur 1 % des Datensatzes (`train_sft[:1%]`). Dies reduziert die Datenmenge erheblich und beschleunigt sowohl den Upload als auch den Feinabstimmungsprozess. Sie können den Prozentsatz anpassen, um ein ausgewogenes Verhältnis zwischen Trainingszeit und Modellleistung zu finden. Die Verwendung eines kleineren Teils des Datensatzes reduziert die benötigte Zeit für die Feinabstimmung und macht den Prozess für ein E2E-Beispiel besser handhabbar.

## Szenario 2: Feinabstimmung des Phi-3-Modells und Bereitstellung in Azure Machine Learning Studio

### Azure CLI einrichten

Sie müssen Azure CLI einrichten, um Ihre Umgebung zu authentifizieren. Azure CLI ermöglicht es Ihnen, Azure-Ressourcen direkt über die Befehlszeile zu verwalten und stellt die notwendigen Anmeldedaten bereit, damit Azure Machine Learning auf diese Ressourcen zugreifen kann. Zum Einstieg installieren Sie [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. Öffnen Sie ein Terminalfenster und geben Sie den folgenden Befehl ein, um sich bei Ihrem Azure-Konto anzumelden.

    ```console
    az login
    ```

1. Wählen Sie Ihr Azure-Konto aus.

1. Wählen Sie Ihr Azure-Abonnement aus.

    ![Resource Group Name finden.](../../../../../../translated_images/02-01-login-using-azure-cli.dfde31cb75e58a87.de.png)

> [!TIP]
>
> Falls Sie sich nicht bei Azure anmelden können, versuchen Sie es mit einem Gerätecode. Öffnen Sie ein Terminalfenster und geben Sie den folgenden Befehl ein, um sich bei Ihrem Azure-Konto anzumelden:
>
> ```console
> az login --use-device-code
> ```
>

### Feinabstimmung des Phi-3-Modells

In dieser Übung stimmen Sie das Phi-3-Modell mit dem bereitgestellten Datensatz fein ab. Zuerst definieren Sie den Feinabstimmungsprozess in der Datei *fine_tune.py*. Anschließend konfigurieren Sie die Azure Machine Learning-Umgebung und starten den Feinabstimmungsprozess durch Ausführen der Datei *setup_ml.py*. Dieses Skript sorgt dafür, dass die Feinabstimmung innerhalb der Azure Machine Learning-Umgebung erfolgt.

Indem Sie *setup_ml.py* ausführen, starten Sie den Feinabstimmungsprozess in der Azure Machine Learning-Umgebung.

#### Code zur *fine_tune.py*-Datei hinzufügen

1. Navigieren Sie zum Ordner *finetuning_dir* und öffnen Sie die Datei *fine_tune.py* in Visual Studio Code.

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

    # Um den INVALID_PARAMETER_VALUE-Fehler in MLflow zu vermeiden, deaktivieren Sie die MLflow-Integration
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Einrichtung der Protokollierung
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

1. Speichern und schließen Sie die Datei *fine_tune.py*.

> [!TIP]
> **Sie können das Phi-3.5-Modell feinabstimmen**
>
> In der Datei *fine_tune.py* können Sie den Parameter `pretrained_model_name` von `"microsoft/Phi-3-mini-4k-instruct"` auf jedes Modell ändern, das Sie feinabstimmen möchten. Wenn Sie es beispielsweise auf `"microsoft/Phi-3.5-mini-instruct"` ändern, verwenden Sie das Phi-3.5-mini-instruct-Modell für die Feinabstimmung. Um den Modellnamen zu finden und zu verwenden, besuchen Sie [Hugging Face](https://huggingface.co/), suchen Sie nach dem gewünschten Modell und kopieren Sie dessen Namen in das Feld `pretrained_model_name` in Ihrem Skript.
>
> <image type="content" src="../../../../imgs/02/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Fine tune Phi-3.5.">
>

#### Code zur *setup_ml.py*-Datei hinzufügen

1. Öffnen Sie die Datei *setup_ml.py* in Visual Studio Code.

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

    # Konstanten

    # Entfernen Sie das Kommentarzeichen bei den folgenden Zeilen, um eine CPU-Instanz für das Training zu verwenden
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Entfernen Sie das Kommentarzeichen bei den folgenden Zeilen, um eine GPU-Instanz für das Training zu verwenden
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Ersetzen Sie durch den Standort Ihres Compute-Clusters
    FINETUNING_DIR = "./finetuning_dir" # Pfad zum Fine-Tuning-Skript
    TRAINING_ENV_NAME = "phi-3-training-environment" # Name der Trainingsumgebung
    MODEL_OUTPUT_DIR = "./model_output" # Pfad zum Ausgabeordner des Modells in Azure ML

    # Protokollierungseinstellung zur Nachverfolgung des Prozesses
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
            image=DOCKER_IMAGE_NAME,  # Docker-Image für die Umgebung
            conda_file=CONDA_FILE,  # Conda-Umgebungsdatei
            name=TRAINING_ENV_NAME,  # Name der Umgebung
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
                tier="Dedicated",  # Ebene des Compute-Clusters
                min_instances=0,  # Minimale Anzahl von Instanzen
                max_instances=1  # Maximale Anzahl von Instanzen
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Warten, bis der Cluster erstellt wurde
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Pfad zu fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Trainingsumgebung
            compute=compute_name,  # Zu verwendender Compute-Cluster
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Pfad zur Trainingsdatendatei
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Pfad zur Bewertungsdatendatei
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # ML-Client initialisieren
        ml_client = get_ml_client()

        # Umgebung erstellen
        env = create_or_get_environment(ml_client)
        
        # Compute-Cluster erstellen oder bestehenden abrufen
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Fine-Tuning-Job erstellen und einreichen
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Job einreichen
        ml_client.jobs.stream(returned_job.name)  # Job-Protokolle streamen
        
        # Job-Namen erfassen
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. Ersetzen Sie `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` und `LOCATION` durch Ihre spezifischen Angaben.

    ```python
   # Entfernen Sie die Kommentarzeichen in den folgenden Zeilen, um eine GPU-Instanz für das Training zu verwenden
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Ersetzen Sie durch den Standort Ihres Rechenclusters
    ```

> [!TIP]
>
> **Anleitung zur Feinabstimmung mit einem minimalen Datensatz auf einer CPU**
>
> Wenn Sie eine CPU für die Feinabstimmung verwenden möchten, ist dieser Ansatz ideal für diejenigen mit Vorteil-Abonnements (wie Visual Studio Enterprise Subscription) oder zum schnellen Testen des Feinabstimmungs- und Bereitstellungsprozesses.
>
> 1. Öffnen Sie die Datei *setup_ml*.
> 1. Ersetzen Sie `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME` und `DOCKER_IMAGE_NAME` durch die folgenden Werte. Wenn Sie keinen Zugriff auf *Standard_E16s_v3* haben, können Sie eine entsprechende CPU-Instanz verwenden oder eine neue Quote anfordern.
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

1. Geben Sie den folgenden Befehl ein, um das Skript *setup_ml.py* auszuführen und den Feinabstimmungsprozess in Azure Machine Learning zu starten.

    ```python
    python setup_ml.py
    ```

1. In dieser Übung haben Sie das Phi-3-Modell erfolgreich mit Azure Machine Learning feinabgestimmt. Durch das Ausführen des Skripts *setup_ml.py* haben Sie die Azure Machine Learning-Umgebung eingerichtet und den in der Datei *fine_tune.py* definierten Feinabstimmungsprozess gestartet. Bitte beachten Sie, dass der Feinabstimmungsprozess eine beträchtliche Zeit in Anspruch nehmen kann. Nach Ausführung des Befehls `python setup_ml.py` müssen Sie warten, bis der Prozess abgeschlossen ist. Sie können den Status des Feinabstimmungsjobs über den in der Konsole bereitgestellten Link im Azure Machine Learning-Portal überwachen.

    ![Feinabstimmungsjob ansehen.](../../../../../../translated_images/02-02-see-finetuning-job.59393bc3b143871e.de.png)

### Das feinabgestimmte Modell bereitstellen

Um das feinabgestimmte Phi-3-Modell mit Prompt Flow zu integrieren, müssen Sie das Modell bereitstellen, um es für Echtzeit-Inferenz zugänglich zu machen. Dieser Vorgang umfasst das Registrieren des Modells, die Erstellung eines Online-Endpunkts und die Bereitstellung des Modells.

#### Legen Sie den Modellnamen, Endpunktnamen und Bereitstellungsnamen für die Bereitstellung fest

1. Öffnen Sie die Datei *config.py*.

1. Ersetzen Sie `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` durch den gewünschten Namen für Ihr Modell.

1. Ersetzen Sie `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` durch den gewünschten Namen für Ihren Endpunkt.

1. Ersetzen Sie `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` durch den gewünschten Namen für Ihre Bereitstellung.

#### Code zur *deploy_model.py*-Datei hinzufügen

Durch Ausführen der Datei *deploy_model.py* wird der gesamte Bereitstellungsprozess automatisiert. Es registriert das Modell, erstellt einen Endpunkt und führt die Bereitstellung basierend auf den in der Datei *config.py* angegebenen Einstellungen aus, welche den Modellnamen, Endpunktnamen und Bereitstellungsnamen umfassen.

1. Öffnen Sie die Datei *deploy_model.py* in Visual Studio Code.

1. Fügen Sie den folgenden Code in *deploy_model.py* ein.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Konfigurationsimporte
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

    # Konstanten
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Protokollierungseinrichtung
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
            # Abrufen der aktuellen Endpunktdetails
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Die aktuelle Verkehrszuweisung zur Fehlerbehebung protokollieren
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Die Verkehrszuweisung für die Bereitstellung festlegen
            endpoint.traffic = {deployment_name: 100}
            
            # Den Endpunkt mit der neuen Verkehrszuweisung aktualisieren
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Die aktualisierte Verkehrszuweisung zur Fehlerbehebung protokollieren
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Fehler protokollieren, die während des Prozesses auftreten
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

    - Navigieren Sie zur erstellten Azure Machine Learning-Ressource.
    - Wählen Sie **Studio web URL**, um den Azure Machine Learning-Arbeitsbereich zu öffnen.
    - Wählen Sie im linken Seitenbereich **Jobs**.
    - Wählen Sie das Experiment für die Feinabstimmung aus, z. B. *finetunephi*.
    - Wählen Sie den von Ihnen erstellten Job aus.
- Kopieren Sie den Namen Ihres Jobs und fügen Sie ihn in `JOB_NAME = "your-job-name"` in der Datei *deploy_model.py* ein.

1. Ersetzen Sie `COMPUTE_INSTANCE_TYPE` durch Ihre spezifischen Details.

1. Geben Sie den folgenden Befehl ein, um das Skript *deploy_model.py* auszuführen und den Bereitstellungsprozess in Azure Machine Learning zu starten.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> Um zusätzliche Kosten für Ihr Konto zu vermeiden, stellen Sie sicher, dass Sie den erstellten Endpunkt im Azure Machine Learning-Arbeitsbereich löschen.
>

#### Überprüfen Sie den Bereitstellungsstatus im Azure Machine Learning-Arbeitsbereich

1. Besuchen Sie [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Navigieren Sie zu dem von Ihnen erstellten Azure Machine Learning-Arbeitsbereich.

1. Wählen Sie **Studio web URL** aus, um den Azure Machine Learning-Arbeitsbereich zu öffnen.

1. Wählen Sie **Endpoints** aus dem linken Seitenregister.

    ![Endpoints auswählen.](../../../../../../translated_images/02-03-select-endpoints.c3136326510baff1.de.png)

2. Wählen Sie den von Ihnen erstellten Endpunkt aus.

    ![Von Ihnen erstellten Endpunkt auswählen.](../../../../../../translated_images/02-04-select-endpoint-created.0363e7dca51dabb4.de.png)

3. Auf dieser Seite können Sie die während des Bereitstellungsprozesses erstellten Endpunkte verwalten.

## Szenario 3: Integration mit Prompt Flow und Chatten mit Ihrem benutzerdefinierten Modell

### Integrieren Sie das benutzerdefinierte Phi-3-Modell mit Prompt Flow

Nachdem Sie Ihr feinabgestimmtes Modell erfolgreich bereitgestellt haben, können Sie es nun mit Prompt Flow integrieren, um Ihr Modell in Echtzeitanwendungen zu verwenden und eine Vielzahl von interaktiven Aufgaben mit Ihrem benutzerdefinierten Phi-3-Modell zu ermöglichen.

#### API-Schlüssel und Endpunkt-URI des feinabgestimmten Phi-3-Modells festlegen

1. Navigieren Sie zu dem von Ihnen erstellten Azure Machine Learning-Arbeitsbereich.
1. Wählen Sie **Endpoints** aus dem linken Seitenregister.
1. Wählen Sie den von Ihnen erstellten Endpunkt aus.
1. Wählen Sie im Navigationsmenü **Consume** aus.
1. Kopieren Sie Ihren **REST-Endpunkt** und fügen Sie ihn in die Datei *config.py* ein, indem Sie `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` durch Ihren **REST-Endpunkt** ersetzen.
1. Kopieren Sie Ihren **Primärschlüssel** und fügen Sie ihn in die Datei *config.py* ein, indem Sie `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` durch Ihren **Primärschlüssel** ersetzen.

    ![API-Schlüssel und Endpunkt-URI kopieren.](../../../../../../translated_images/02-05-copy-apikey-endpoint.88b5a92e6462c53b.de.png)

#### Code zur Datei *flow.dag.yml* hinzufügen

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

#### Code zur Datei *integrate_with_promptflow.py* hinzufügen

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

    # Protokollierungseinrichtung
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

### Chatten Sie mit Ihrem benutzerdefinierten Modell

1. Geben Sie den folgenden Befehl ein, um das Skript *deploy_model.py* auszuführen und den Bereitstellungsprozess in Azure Machine Learning zu starten.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Hier ein Beispiel für die Ergebnisse: Jetzt können Sie mit Ihrem benutzerdefinierten Phi-3-Modell chatten. Es wird empfohlen, Fragen basierend auf den für das Fine-Tuning verwendeten Daten zu stellen.

    ![Prompt-Flow-Beispiel.](../../../../../../translated_images/02-06-promptflow-example.89384abaf3ad71f6.de.png)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Originalsprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->