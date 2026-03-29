# Feinabstimmung und Integration benutzerdefinierter Phi-3-Modelle mit Prompt Flow in Microsoft Foundry

Dieses End-to-End (E2E)-Beispiel basiert auf dem Leitfaden "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Microsoft Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" aus der Microsoft Tech Community. Es führt in die Prozesse des Feinabstimmens, Bereitstellens und Integrierens benutzerdefinierter Phi-3-Modelle mit Prompt Flow in Microsoft Foundry ein.
Im Gegensatz zum E2E-Beispiel, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", bei dem der Code lokal ausgeführt wurde, konzentriert sich dieses Tutorial vollständig auf das Feinabstimmen und Integrieren Ihres Modells innerhalb des Azure AI / ML Studios.

## Überblick

In diesem E2E-Beispiel lernen Sie, wie Sie das Phi-3-Modell feinabstimmen und es mit Prompt Flow in Microsoft Foundry integrieren. Mithilfe von Azure AI / ML Studio etablieren Sie einen Workflow zum Bereitstellen und Nutzen benutzerdefinierter KI-Modelle. Dieses E2E-Beispiel ist in drei Szenarien unterteilt:

**Szenario 1: Azure-Ressourcen einrichten und Vorbereitung für Feinabstimmung**

**Szenario 2: Feinabstimmung des Phi-3-Modells und Bereitstellung im Azure Machine Learning Studio**

**Szenario 3: Integration in Prompt Flow und Chat mit Ihrem benutzerdefinierten Modell in Microsoft Foundry**

Hier ist ein Überblick über dieses E2E-Beispiel.

![Phi-3-FineTuning_PromptFlow_Integration Überblick.](../../../../../../translated_images/de/00-01-architecture.198ba0f1ae6d841a.webp)

### Inhaltsverzeichnis

1. **[Szenario 1: Azure-Ressourcen einrichten und Vorbereitung für Feinabstimmung](#szenario-1-azure-ressourcen-einrichten-und-vorbereitung-für-feinabstimmung)**
    - [Erstellen eines Azure Machine Learning-Arbeitsbereichs](#erstellen-eines-azure-machine-learning-arbeitsbereichs)
    - [Anfordern von GPU-Kontingenten im Azure-Abonnement](#anfordern-von-gpu-kontingenten-im-azure-abonnement)
    - [Hinzufügen einer Rollenzuweisung](#hinzufügen-einer-rollenzuweisung)
    - [Projekt einrichten](#projekt-einrichten)
    - [Datensatz für Feinabstimmung vorbereiten](#bereiten-sie-den-datensatz-für-das-fein-tuning-vor)

1. **[Szenario 2: Feinabstimmung des Phi-3-Modells und Bereitstellung im Azure Machine Learning Studio](#szenario-2-feinabstimmung-des-phi-3-modells-und-bereitstellung-in-azure-machine-learning-studio)**
    - [Feinabstimmung des Phi-3-Modells](#feinabstimmung-des-phi-3-modells)
    - [Bereitstellung des feinabgestimmten Phi-3-Modells](#bereitstellung-des-feinabgestimmten-phi-3-modells)

1. **[Szenario 3: Integration in Prompt Flow und Chat mit Ihrem benutzerdefinierten Modell in Microsoft Foundry](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model-in-azure-ai-studio)**
    - [Integration des benutzerdefinierten Phi-3-Modells in Prompt Flow](#integration-des-benutzerdefinierten-phi-3-modells-mit-prompt-flow)
    - [Chat mit Ihrem benutzerdefinierten Phi-3-Modell](#chatten-sie-mit-ihrem-benutzerdefinierten-phi-3-modell)

## Szenario 1: Azure-Ressourcen einrichten und Vorbereitung für Feinabstimmung

### Erstellen eines Azure Machine Learning-Arbeitsbereichs

1. Geben Sie *azure machine learning* in die **Suchleiste** oben auf der Portalseite ein und wählen Sie **Azure Machine Learning** aus den angezeigten Optionen aus.

    ![Geben Sie azure machine learning ein.](../../../../../../translated_images/de/01-01-type-azml.acae6c5455e67b4b.webp)

2. Wählen Sie **+ Erstellen** im Navigationsmenü aus.

3. Wählen Sie **Neuer Arbeitsbereich** im Navigationsmenü aus.

    ![Wählen Sie neuen Arbeitsbereich aus.](../../../../../../translated_images/de/01-02-select-new-workspace.cd09cd0ec4a60ef2.webp)

4. Führen Sie die folgenden Aufgaben aus:

    - Wählen Sie Ihr Azure-**Abonnement**.
    - Wählen Sie die zu verwendende **Ressourcengruppe** aus (erstellen Sie bei Bedarf eine neue).
    - Geben Sie **Arbeitsbereichsname** ein. Er muss ein eindeutiger Wert sein.
    - Wählen Sie die **Region** aus, die Sie verwenden möchten.
    - Wählen Sie das zu verwendende **Speicherkonto** aus (erstellen Sie bei Bedarf ein neues).
    - Wählen Sie den zu verwendenden **Schlüsseltresor** aus (erstellen Sie bei Bedarf einen neuen).
    - Wählen Sie die zu verwendenden **Anwendungs-Insights** aus (erstellen Sie bei Bedarf neue).
    - Wählen Sie die zu verwendende **Container-Registrierung** aus (erstellen Sie bei Bedarf eine neue).

    ![Azure Machine Learning ausfüllen.](../../../../../../translated_images/de/01-03-fill-AZML.a1b6fd944be0090f.webp)

5. Wählen Sie **Überprüfen + Erstellen**.

6. Wählen Sie **Erstellen**.

### Anfordern von GPU-Kontingenten im Azure-Abonnement

In diesem Tutorial lernen Sie, wie Sie ein Phi-3-Modell mit GPUs feinabstimmen und bereitstellen. Für die Feinabstimmung verwenden Sie die GPU *Standard_NC24ads_A100_v4*, für die eine Kontingentanfrage erforderlich ist. Für die Bereitstellung verwenden Sie die GPU *Standard_NC6s_v3*, die ebenfalls eine Kontingentanfrage benötigt.

> [!NOTE]
>
> Nur Pay-As-You-Go-Abonnements (der Standard-Abonnementtyp) sind für GPU-Zuweisungen berechtigt; Vorteil-Abonnements werden derzeit nicht unterstützt.
>

1. Besuchen Sie [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Führen Sie die folgenden Aufgaben zur Anforderung des Kontingents für *Standard NCADSA100v4 Family* aus:

    - Wählen Sie **Kontingent** im linken Seitenregister.
    - Wählen Sie die zu verwendende **Virtuelle Maschinenfamilie** aus. Zum Beispiel **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, die die GPU *Standard_NC24ads_A100_v4* einschließt.
    - Wählen Sie **Kontingent anfordern** im Navigationsmenü aus.

        ![Kontingent anfordern.](../../../../../../translated_images/de/02-02-request-quota.c0428239a63ffdd5.webp)

    - Geben Sie auf der Seite zur Kontingentanfrage das **Neue Kernlimit** ein, das Sie verwenden möchten. Zum Beispiel 24.
    - Wählen Sie auf der Seite zur Kontingentanfrage **Absenden**, um das GPU-Kontingent anzufordern.

1. Führen Sie die folgenden Aufgaben zur Anforderung des Kontingents für *Standard NCSv3 Family* aus:

    - Wählen Sie **Kontingent** im linken Seitenregister.
    - Wählen Sie die zu verwendende **Virtuelle Maschinenfamilie** aus. Zum Beispiel **Standard NCSv3 Family Cluster Dedicated vCPUs**, die die GPU *Standard_NC6s_v3* einschließt.
    - Wählen Sie **Kontingent anfordern** im Navigationsmenü aus.
    - Geben Sie auf der Seite zur Kontingentanfrage das **Neue Kernlimit** ein, das Sie verwenden möchten. Zum Beispiel 24.
    - Wählen Sie auf der Seite zur Kontingentanfrage **Absenden**, um das GPU-Kontingent anzufordern.

### Hinzufügen einer Rollenzuweisung

Um Ihre Modelle feinabzustimmen und bereitzustellen, müssen Sie zunächst eine User Assigned Managed Identity (UAI) erstellen und ihr die entsprechenden Berechtigungen zuweisen. Diese UAI wird für die Authentifizierung während der Bereitstellung verwendet.

#### Erstellen einer User Assigned Managed Identity (UAI)

1. Geben Sie *managed identities* in die **Suchleiste** oben auf der Portalseite ein und wählen Sie **Managed Identities** aus den angezeigten Optionen aus.

    ![Geben Sie managed identities ein.](../../../../../../translated_images/de/03-01-type-managed-identities.24de763e0f1f37e5.webp)

1. Wählen Sie **+ Erstellen**.

    ![Wählen Sie erstellen aus.](../../../../../../translated_images/de/03-02-select-create.92bf8989a5cd98f2.webp)

1. Führen Sie die folgenden Aufgaben aus:

    - Wählen Sie Ihr Azure-**Abonnement**.
    - Wählen Sie die zu verwendende **Ressourcengruppe** aus (erstellen Sie bei Bedarf eine neue).
    - Wählen Sie die **Region** aus, die Sie verwenden möchten.
    - Geben Sie den **Namen** ein. Er muss ein eindeutiger Wert sein.

    ![Erstellen ausfüllen.](../../../../../../translated_images/de/03-03-fill-managed-identities-1.ef1d6a2261b449e0.webp)

1. Wählen Sie **Überprüfen + Erstellen**.

1. Wählen Sie **+ Erstellen**.

#### Hinzufügen der Rolle "Mitwirkender" zur Managed Identity

1. Navigieren Sie zur Managed Identity-Ressource, die Sie erstellt haben.

1. Wählen Sie **Azure Rollenzuweisungen** im linken Seitenregister.

1. Wählen Sie **+ Rollenzuweisung hinzufügen** im Navigationsmenü.

1. Führen Sie auf der Seite Rollenzuweisung hinzufügen folgende Aufgaben aus:
    - Wählen Sie den **Geltungsbereich** auf **Ressourcengruppe** aus.
    - Wählen Sie Ihr Azure-**Abonnement**.
    - Wählen Sie die zu verwendende **Ressourcengruppe**.
    - Wählen Sie die **Rolle** auf **Mitwirkender** aus.

    ![Mitwirkender Rolle ausfüllen.](../../../../../../translated_images/de/03-04-fill-contributor-role.73990bc6a32e140d.webp)

2. Wählen Sie **Speichern**.

#### Hinzufügen der Rolle "Storage Blob Data Reader" zur Managed Identity

1. Geben Sie *storage accounts* in die **Suchleiste** oben auf der Portalseite ein und wählen Sie **Storage accounts** aus den angezeigten Optionen aus.

    ![Geben Sie storage accounts ein.](../../../../../../translated_images/de/03-05-type-storage-accounts.9303de485e65e1e5.webp)

1. Wählen Sie das Speicherkonto aus, das mit dem Azure Machine Learning-Arbeitsbereich verknüpft ist, den Sie erstellt haben. Zum Beispiel *finetunephistorage*.

1. Führen Sie die folgenden Aufgaben aus, um zur Seite Rollenzuweisung hinzufügen zu navigieren:

    - Navigieren Sie zum erstellten Azure-Speicherkonto.
    - Wählen Sie **Zugriffskontrolle (IAM)** im linken Seitenregister.
    - Wählen Sie **+ Hinzufügen** im Navigationsmenü.
    - Wählen Sie **Rollenzuweisung hinzufügen** im Navigationsmenü.

    ![Rolle hinzufügen.](../../../../../../translated_images/de/03-06-add-role.353ccbfdcf0789c2.webp)

1. Führen Sie auf der Seite Rollenzuweisung hinzufügen folgende Aufgaben aus:

    - Geben Sie auf der Rollenseite *Storage Blob Data Reader* in die **Suchleiste** ein und wählen Sie **Storage Blob Data Reader** aus den angezeigten Optionen aus.
    - Wählen Sie auf der Rollenseite **Weiter** aus.
    - Wählen Sie auf der Seite Mitglieder **Zugriff zuweisen an** **Verwaltete Identität**.
    - Wählen Sie auf der Seite Mitglieder **+ Mitglieder auswählen**.
    - Wählen Sie auf der Seite Verwaltete Identitäten Ihr Azure-**Abonnement** aus.
    - Wählen Sie auf der Seite Verwaltete Identitäten die **Verwaltete Identität** unter **Managed Identity** aus.
    - Wählen Sie auf der Seite Verwaltete Identitäten die von Ihnen erstellte Managed Identity aus. Zum Beispiel *finetunephi-managedidentity*.
    - Wählen Sie auf der Seite Verwaltete Identitäten **Auswählen**.

    ![Managed Identity auswählen.](../../../../../../translated_images/de/03-08-select-managed-identity.e80a2aad5247eb25.webp)

1. Wählen Sie **Überprüfen + Zuweisen**.

#### Hinzufügen der Rolle "AcrPull" zur Managed Identity

1. Geben Sie *container registries* in die **Suchleiste** oben auf der Portalseite ein und wählen Sie **Container registries** aus den angezeigten Optionen aus.

    ![Geben Sie container registries ein.](../../../../../../translated_images/de/03-09-type-container-registries.7a4180eb2110e5a6.webp)

1. Wählen Sie die Container-Registrierung aus, die mit dem Azure Machine Learning-Arbeitsbereich verknüpft ist. Zum Beispiel *finetunephicontainerregistry*

1. Führen Sie die folgenden Aufgaben aus, um zur Seite Rollenzuweisung hinzufügen zu navigieren:

    - Wählen Sie **Zugriffskontrolle (IAM)** im linken Seitenregister.
    - Wählen Sie **+ Hinzufügen** im Navigationsmenü.
    - Wählen Sie **Rollenzuweisung hinzufügen** im Navigationsmenü.

1. Führen Sie auf der Seite Rollenzuweisung hinzufügen folgende Aufgaben aus:

    - Geben Sie auf der Rollenseite *AcrPull* in die **Suchleiste** ein und wählen Sie **AcrPull** aus den angezeigten Optionen aus.
    - Wählen Sie auf der Rollenseite **Weiter** aus.
    - Wählen Sie auf der Seite Mitglieder **Zugriff zuweisen an** **Verwaltete Identität**.
    - Wählen Sie auf der Seite Mitglieder **+ Mitglieder auswählen**.
    - Wählen Sie auf der Seite Verwaltete Identitäten Ihr Azure-**Abonnement** aus.
    - Wählen Sie auf der Seite Verwaltete Identitäten die **Verwaltete Identität** unter **Managed Identity** aus.
    - Wählen Sie auf der Seite Verwaltete Identitäten die von Ihnen erstellte Managed Identity aus. Zum Beispiel *finetunephi-managedidentity*.
    - Wählen Sie auf der Seite Verwaltete Identitäten **Auswählen**.
    - Wählen Sie **Überprüfen + Zuweisen**.

### Projekt einrichten

Um die für die Feinabstimmung benötigten Datensätze herunterzuladen, richten Sie eine lokale Umgebung ein.

In dieser Übung werden Sie

- Einen Ordner zum Arbeiten erstellen.
- Eine virtuelle Umgebung erstellen.
- Die erforderlichen Pakete installieren.
- Eine Datei *download_dataset.py* erstellen, um den Datensatz herunterzuladen.

#### Einen Ordner zum Arbeiten erstellen

1. Öffnen Sie ein Terminalfenster und geben Sie den folgenden Befehl ein, um einen Ordner mit dem Namen *finetune-phi* im Standardpfad zu erstellen.

    ```console
    mkdir finetune-phi
    ```

2. Geben Sie im Terminal den folgenden Befehl ein, um in den erstellten Ordner *finetune-phi* zu wechseln.

    ```console
    cd finetune-phi
    ```

#### Eine virtuelle Umgebung erstellen

1. Geben Sie im Terminal den folgenden Befehl ein, um eine virtuelle Umgebung mit dem Namen *.venv* zu erstellen.
    ```console
    python -m venv .venv
    ```

2. Geben Sie den folgenden Befehl in Ihrem Terminal ein, um die virtuelle Umgebung zu aktivieren.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Wenn es funktioniert hat, sollten Sie *(.venv)* vor der Eingabeaufforderung sehen.

#### Installieren Sie die erforderlichen Pakete

1. Geben Sie die folgenden Befehle in Ihrem Terminal ein, um die erforderlichen Pakete zu installieren.

    ```console
    pip install datasets==2.19.1
    ```

#### Erstellen Sie `donload_dataset.py`

> [!NOTE]
> Vollständige Ordnerstruktur:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Öffnen Sie **Visual Studio Code**.

1. Wählen Sie **Datei** aus der Menüleiste.

1. Wählen Sie **Ordner öffnen**.

1. Wählen Sie den Ordner *finetune-phi* aus, den Sie erstellt haben, der sich unter *C:\Users\IhrBenutzername\finetune-phi* befindet.

    ![Wählen Sie den Ordner aus, den Sie erstellt haben.](../../../../../../translated_images/de/04-01-open-project-folder.f734374bcfd5f9e6.webp)

1. Klicken Sie im linken Bereich von Visual Studio Code mit der rechten Maustaste und wählen Sie **Neue Datei**, um eine neue Datei namens *download_dataset.py* zu erstellen.

    ![Erstellen Sie eine neue Datei.](../../../../../../translated_images/de/04-02-create-new-file.cf9a330a3a9cff92.webp)

### Bereiten Sie den Datensatz für das Fein-Tuning vor

In dieser Übung führen Sie die Datei *download_dataset.py* aus, um die Datensätze *ultrachat_200k* in Ihre lokale Umgebung herunterzuladen. Anschließend verwenden Sie diese Datensätze, um das Phi-3-Modell in Azure Machine Learning fein abzustimmen.

In dieser Übung werden Sie:

- Code in der Datei *download_dataset.py* hinzufügen, um die Datensätze herunterzuladen.
- Die Datei *download_dataset.py* ausführen, um die Datensätze in Ihre lokale Umgebung herunterzuladen.

#### Laden Sie Ihren Datensatz mit *download_dataset.py* herunter

1. Öffnen Sie die Datei *download_dataset.py* in Visual Studio Code.

1. Fügen Sie den folgenden Code in die Datei *download_dataset.py* ein.

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Laden Sie den Datensatz mit dem angegebenen Namen, der Konfiguration und dem Aufteilungsverhältnis
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Teilen Sie den Datensatz in Trainings- und Testsets auf (80% Training, 20% Test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Erstellen Sie das Verzeichnis, wenn es nicht existiert
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Öffnen Sie die Datei im Schreibmodus
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterieren Sie über jeden Datensatz im Datensatz
            for record in dataset:
                # Dumpen Sie den Datensatz als JSON-Objekt und schreiben Sie ihn in die Datei
                json.dump(record, f)
                # Schreiben Sie ein Zeilenumbruchzeichen, um Datensätze zu trennen
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Laden und teilen Sie den ULTRACHAT_200k-Datensatz mit einer spezifischen Konfiguration und einem Aufteilungsverhältnis
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extrahieren Sie die Trainings- und Testdatensätze aus der Aufteilung
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Speichern Sie den Trainingsdatensatz in einer JSONL-Datei
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Speichern Sie den Testdatensatz in einer separaten JSONL-Datei
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Geben Sie den folgenden Befehl in Ihrem Terminal ein, um das Skript auszuführen und den Datensatz in Ihre lokale Umgebung herunterzuladen.

    ```console
    python download_dataset.py
    ```

1. Überprüfen Sie, ob die Datensätze erfolgreich in Ihrem lokalen Verzeichnis *finetune-phi/data* gespeichert wurden.

> [!NOTE]
>
> #### Hinweis zur Datensatzgröße und Feinabstimmungszeit
>
> In diesem Tutorial verwenden Sie nur 1 % des Datensatzes (`split='train[:1%]'`). Dies reduziert die Datenmenge erheblich und beschleunigt sowohl den Upload als auch den Feinabstimmungsprozess. Sie können den Prozentsatz anpassen, um die richtige Balance zwischen Trainingszeit und Modellleistung zu finden. Die Verwendung eines kleineren Teils des Datensatzes verringert die erforderliche Zeit für das Feinabstimmen, was den Prozess für ein Tutorial handhabbarer macht.

## Szenario 2: Feinabstimmung des Phi-3-Modells und Bereitstellung in Azure Machine Learning Studio

### Feinabstimmung des Phi-3-Modells

In dieser Übung werden Sie das Phi-3-Modell in Azure Machine Learning Studio fein abstimmen.

In dieser Übung werden Sie:

- Einen Computercluster für die Feinabstimmung erstellen.
- Das Phi-3-Modell in Azure Machine Learning Studio fein abstimmen.

#### Erstellen eines Computerclusters für die Feinabstimmung

1. Besuchen Sie [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Wählen Sie **Compute** im linken Seitenmenü.

1. Wählen Sie **Compute-Cluster** aus dem Navigationsmenü.

1. Wählen Sie **+ Neu**.

    ![Wählen Sie Compute aus.](../../../../../../translated_images/de/06-01-select-compute.a29cff290b480252.webp)

1. Führen Sie die folgenden Aufgaben aus:

    - Wählen Sie die **Region** aus, die Sie verwenden möchten.
    - Wählen Sie die **Virtuelle Maschinentier** auf **Dediziert**.
    - Wählen Sie den **Virtuellen Maschinentyp** auf **GPU**.
    - Wählen Sie den Filter für **Virtuelle Maschinengröße** auf **Alle Optionen auswählen**.
    - Wählen Sie die **Virtuelle Maschinengröße** auf **Standard_NC24ads_A100_v4**.

    ![Cluster erstellen.](../../../../../../translated_images/de/06-02-create-cluster.f221b65ae1221d4e.webp)

1. Wählen Sie **Weiter**.

1. Führen Sie die folgenden Aufgaben aus:

    - Geben Sie einen **Compute-Namen** ein. Er muss eindeutig sein.
    - Wählen Sie die **minimale Knotenzahl** auf **0**.
    - Wählen Sie die **maximale Knotenzahl** auf **1**.
    - Wählen Sie die **Leerlaufsekunden vor dem Scale-down** auf **120**.

    ![Cluster erstellen.](../../../../../../translated_images/de/06-03-create-cluster.4a54ba20914f3662.webp)

1. Wählen Sie **Erstellen**.

#### Feinabstimmung des Phi-3-Modells

1. Besuchen Sie [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Wählen Sie den Azure Machine Learning-Arbeitsbereich aus, den Sie erstellt haben.

    ![Wählen Sie den erstellten Arbeitsbereich aus.](../../../../../../translated_images/de/06-04-select-workspace.a92934ac04f4f181.webp)

1. Führen Sie die folgenden Schritte aus:

    - Wählen Sie **Modellkatalog** im linken Seitenmenü.
    - Geben Sie *phi-3-mini-4k* in die **Suchleiste** ein und wählen Sie **Phi-3-mini-4k-instruct** aus den angezeigten Optionen.

    ![Geben Sie phi-3-mini-4k ein.](../../../../../../translated_images/de/06-05-type-phi-3-mini-4k.8ab6d2a04418b250.webp)

1. Wählen Sie **Feinabstimmung** im Navigationsmenü.

    ![Wählen Sie Feinabstimmung aus.](../../../../../../translated_images/de/06-06-select-fine-tune.2918a59be55dfeec.webp)

1. Führen Sie die folgenden Aufgaben aus:

    - Wählen Sie **Aufgabentyp auswählen** auf **Chat-Vervollständigung**.
    - Wählen Sie **+ Daten auswählen**, um **Trainingsdaten** hochzuladen.
    - Wählen Sie den Validierungsdatenuploadtyp auf **Andere Validierungsdaten bereitstellen**.
    - Wählen Sie **+ Daten auswählen**, um **Validierungsdaten** hochzuladen.

    ![Füllen Sie die Feinabstimmungsseite aus.](../../../../../../translated_images/de/06-07-fill-finetuning.b6d14c89e7c27d0b.webp)

> [!TIP]
>
> Sie können **Erweiterte Einstellungen** auswählen, um Konfigurationen wie **learning_rate** und **lr_scheduler_type** anzupassen, um den Feinabstimmungsprozess entsprechend Ihren spezifischen Anforderungen zu optimieren.

1. Wählen Sie **Fertig stellen**.

1. In dieser Übung haben Sie erfolgreich das Phi-3-Modell mit Azure Machine Learning fein abgestimmt. Bitte beachten Sie, dass der Feinabstimmungsprozess erhebliche Zeit in Anspruch nehmen kann. Nach dem Starten des Feinabstimmungsjobs müssen Sie warten, bis er abgeschlossen ist. Sie können den Status des Feinabstimmungsjobs überwachen, indem Sie auf die Registerkarte Jobs im linken Bereich Ihres Azure Machine Learning-Arbeitsbereichs navigieren. Im nächsten Abschnitt werden Sie das feinabgestimmte Modell bereitstellen und mit Prompt Flow integrieren.

    ![Sehen Sie den Feinabstimmungsjob.](../../../../../../translated_images/de/06-08-output.2bd32e59930672b1.webp)

### Bereitstellung des feinabgestimmten Phi-3-Modells

Um das feinabgestimmte Phi-3-Modell mit Prompt Flow zu integrieren, müssen Sie das Modell bereitstellen, damit es für Echtzeit-Inferenz zugänglich ist. Dieser Prozess umfasst das Registrieren des Modells, das Erstellen eines Online-Endpunkts und die Bereitstellung des Modells.

In dieser Übung werden Sie:

- Das feinabgestimmte Modell im Azure Machine Learning-Arbeitsbereich registrieren.
- Einen Online-Endpunkt erstellen.
- Das registrierte feinabgestimmte Phi-3-Modell bereitstellen.

#### Registrieren des feinabgestimmten Modells

1. Besuchen Sie [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Wählen Sie den Azure Machine Learning-Arbeitsbereich aus, den Sie erstellt haben.

    ![Wählen Sie den erstellten Arbeitsbereich aus.](../../../../../../translated_images/de/06-04-select-workspace.a92934ac04f4f181.webp)

1. Wählen Sie **Modelle** im linken Seitenmenü.
1. Wählen Sie **+ Registrieren**.
1. Wählen Sie **Aus dem Job-Ausgang**.

    ![Modell registrieren.](../../../../../../translated_images/de/07-01-register-model.ad1e7cc05e4b2777.webp)

1. Wählen Sie den von Ihnen erstellten Job aus.

    ![Job auswählen.](../../../../../../translated_images/de/07-02-select-job.3e2e1144cd6cd093.webp)

1. Wählen Sie **Weiter**.

1. Wählen Sie **Modelltyp** auf **MLflow**.

1. Stellen Sie sicher, dass **Job-Ausgang** ausgewählt ist; dies sollte automatisch angewählt sein.

    ![Ausgabe auswählen.](../../../../../../translated_images/de/07-03-select-output.4cf1a0e645baea1f.webp)

2. Wählen Sie **Weiter**.

3. Wählen Sie **Registrieren**.

    ![Registrieren auswählen.](../../../../../../translated_images/de/07-04-register.fd82a3b293060bc7.webp)

4. Sie können Ihr registriertes Modell anzeigen, indem Sie zum Menü **Modelle** im linken Seitenmenü navigieren.

    ![Registriertes Modell.](../../../../../../translated_images/de/07-05-registered-model.7db9775f58dfd591.webp)

#### Bereitstellung des feinabgestimmten Modells

1. Navigieren Sie zu dem Azure Machine Learning-Arbeitsbereich, den Sie erstellt haben.

1. Wählen Sie **Endpunkte** im linken Seitenmenü.

1. Wählen Sie **Echtzeit-Endpunkte** im Navigationsmenü.

    ![Endpunkt erstellen.](../../../../../../translated_images/de/07-06-create-endpoint.1ba865c606551f09.webp)

1. Wählen Sie **Erstellen**.

1. Wählen Sie das von Ihnen registrierte Modell aus.

    ![Registriertes Modell auswählen.](../../../../../../translated_images/de/07-07-select-registered-model.29c947c37fa30cb4.webp)

1. Wählen Sie **Auswählen**.

1. Führen Sie die folgenden Aufgaben aus:

    - Wählen Sie **Virtuelle Maschine** auf *Standard_NC6s_v3*.
    - Wählen Sie die Anzahl der Instanzen, die Sie verwenden möchten. Zum Beispiel *1*.
    - Wählen Sie den **Endpunkt** auf **Neu**, um einen Endpunkt zu erstellen.
    - Geben Sie einen **Endpunktnamen** ein. Er muss eindeutig sein.
    - Geben Sie einen **Bereitstellungsnamen** ein. Er muss eindeutig sein.

    ![Füllen Sie die Einstellungen für die Bereitstellung aus.](../../../../../../translated_images/de/07-08-deployment-setting.43ddc4209e673784.webp)

1. Wählen Sie **Bereitstellen**.

> [!WARNING]
> Um zusätzliche Kosten für Ihr Konto zu vermeiden, stellen Sie sicher, dass Sie den erstellten Endpunkt im Azure Machine Learning-Arbeitsbereich löschen.
>

#### Überprüfen des Bereitstellungsstatus im Azure Machine Learning-Arbeitsbereich

1. Navigieren Sie zu dem Azure Machine Learning-Arbeitsbereich, den Sie erstellt haben.

1. Wählen Sie **Endpunkte** im linken Seitenmenü.

1. Wählen Sie den von Ihnen erstellten Endpunkt aus.

    ![Endpunkte auswählen](../../../../../../translated_images/de/07-09-check-deployment.325d18cae8475ef4.webp)

1. Auf dieser Seite können Sie die Endpunkte während des Bereitstellungsprozesses verwalten.

> [!NOTE]
> Sobald die Bereitstellung abgeschlossen ist, stellen Sie sicher, dass **Live-Traffic** auf **100 %** eingestellt ist. Falls dies nicht der Fall ist, wählen Sie **Traffic aktualisieren**, um die Verkehrssteuerung anzupassen. Beachten Sie, dass Sie das Modell nicht testen können, wenn der Traffic auf 0 % eingestellt ist.
>
> ![Traffic einstellen.](../../../../../../translated_images/de/07-10-set-traffic.085b847e5751ff3d.webp)
>

## Szenario 3: Integration mit Prompt Flow und Chatten mit Ihrem benutzerdefinierten Modell in Microsoft Foundry

### Integration des benutzerdefinierten Phi-3-Modells mit Prompt Flow

Nachdem Sie Ihr feinabgestimmtes Modell erfolgreich bereitgestellt haben, können Sie es nun mit Prompt Flow integrieren, um Ihr Modell in Echtzeit-Anwendungen zu verwenden und eine Vielzahl interaktiver Aufgaben mit Ihrem benutzerdefinierten Phi-3-Modell zu ermöglichen.

In dieser Übung werden Sie:

- Microsoft Foundry Hub erstellen.
- Microsoft Foundry Projekt erstellen.
- Prompt Flow erstellen.
- Eine benutzerdefinierte Verbindung für das feinabgestimmte Phi-3-Modell hinzufügen.
- Prompt Flow einrichten, um mit Ihrem benutzerdefinierten Phi-3-Modell zu chatten.

> [!NOTE]
> Sie können die Integration auch mit Azure ML Studio durchführen. Der gleiche Integrationsprozess kann auf Azure ML Studio angewendet werden.

#### Microsoft Foundry Hub erstellen

Sie müssen einen Hub erstellen, bevor Sie das Projekt erstellen. Ein Hub fungiert wie eine Ressourcengruppe, die es Ihnen ermöglicht, mehrere Projekte innerhalb von Microsoft Foundry zu organisieren und zu verwalten.
1. Besuchen Sie [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Wählen Sie **Alle Hubs** aus dem linken Seitenbereich.

1. Wählen Sie **+ Neuer Hub** aus dem Navigationsmenü.

    ![Create hub.](../../../../../../translated_images/de/08-01-create-hub.8f7dd615bb8d9834.webp)

1. Führen Sie die folgenden Aufgaben aus:

    - Geben Sie **Hub-Name** ein. Er muss ein einzigartiger Wert sein.
    - Wählen Sie Ihr Azure **Abonnement**.
    - Wählen Sie die **Ressourcengruppe** aus, die verwendet werden soll (erstellen Sie bei Bedarf eine neue).
    - Wählen Sie den **Standort** aus, den Sie verwenden möchten.
    - Wählen Sie die **Azure AI Services verbinden** aus (erstellen Sie bei Bedarf eine neue Verbindung).
    - Wählen Sie **Azure AI Search verbinden** auf **Verbindung überspringen**.

    ![Fill hub.](../../../../../../translated_images/de/08-02-fill-hub.c2d3b505bbbdba7c.webp)

1. Wählen Sie **Weiter**.

#### Erstellen eines Microsoft Foundry-Projekts

1. Wählen Sie im von Ihnen erstellten Hub **Alle Projekte** aus dem linken Seitenbereich.

1. Wählen Sie **+ Neues Projekt** aus dem Navigationsmenü.

    ![Select new project.](../../../../../../translated_images/de/08-04-select-new-project.390fadfc9c8f8f12.webp)

1. Geben Sie den **Projektnamen** ein. Er muss ein einzigartiger Wert sein.

    ![Create project.](../../../../../../translated_images/de/08-05-create-project.4d97f0372f03375a.webp)

1. Wählen Sie **Projekt erstellen**.

#### Hinzufügen einer benutzerdefinierten Verbindung für das feinabgestimmte Phi-3-Modell

Um Ihr benutzerdefiniertes Phi-3-Modell mit Prompt flow zu integrieren, müssen Sie den Endpunkt und den Schlüssel des Modells in einer benutzerdefinierten Verbindung speichern. Diese Einrichtung stellt den Zugriff auf Ihr benutzerdefiniertes Phi-3-Modell in Prompt flow sicher.

#### Festlegen von API-Schlüssel und Endpunkt-URI des feinabgestimmten Phi-3-Modells

1. Besuchen Sie [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navigieren Sie zum Azure Machine Learning-Arbeitsbereich, den Sie erstellt haben.

1. Wählen Sie **Endpunkte** im linken Seitenbereich.

    ![Select endpoints.](../../../../../../translated_images/de/08-06-select-endpoints.aff38d453bcf9605.webp)

1. Wählen Sie den von Ihnen erstellten Endpunkt aus.

    ![Select endpoints.](../../../../../../translated_images/de/08-07-select-endpoint-created.47f0dc09df2e275e.webp)

1. Wählen Sie **Verbrauchen** im Navigationsmenü.

1. Kopieren Sie Ihren **REST-Endpunkt** und den **Primärschlüssel**.

    ![Copy api key and endpoint uri.](../../../../../../translated_images/de/08-08-copy-endpoint-key.18f934b5953ae8cb.webp)

#### Hinzufügen der benutzerdefinierten Verbindung

1. Besuchen Sie [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navigieren Sie zu dem von Ihnen erstellten Microsoft Foundry-Projekt.

1. Wählen Sie im Projekt, das Sie erstellt haben, **Einstellungen** aus dem linken Seitenbereich.

1. Wählen Sie **+ Neue Verbindung**.

    ![Select new connection.](../../../../../../translated_images/de/08-09-select-new-connection.02eb45deadc401fc.webp)

1. Wählen Sie **Benutzerdefinierte Schlüssel** aus dem Navigationsmenü.

    ![Select custom keys.](../../../../../../translated_images/de/08-10-select-custom-keys.856f6b2966460551.webp)

1. Führen Sie die folgenden Aufgaben aus:

    - Wählen Sie **+ Schlüssel-Wert-Paare hinzufügen**.
    - Geben Sie für den Schlüsselnamen **endpoint** ein und fügen Sie den kopierten Endpunkt aus Azure ML Studio in das Wertfeld ein.
    - Wählen Sie erneut **+ Schlüssel-Wert-Paare hinzufügen**.
    - Geben Sie als Schlüsselnamen **key** ein und fügen Sie den kopierten Schlüssel aus Azure ML Studio in das Wertfeld ein.
    - Markieren Sie nach dem Hinzufügen der Schlüssel **ist geheim**, um zu verhindern, dass der Schlüssel offengelegt wird.

    ![Add connection.](../../../../../../translated_images/de/08-11-add-connection.785486badb4d2d26.webp)

1. Wählen Sie **Verbindung hinzufügen**.

#### Erstellen eines Prompt flow

Sie haben eine benutzerdefinierte Verbindung in Microsoft Foundry hinzugefügt. Erstellen wir nun einen Prompt flow mit den folgenden Schritten. Anschließend verbinden Sie diesen Prompt flow mit der benutzerdefinierten Verbindung, sodass Sie das feinabgestimmte Modell innerhalb des Prompt flows verwenden können.

1. Navigieren Sie zu dem von Ihnen erstellten Microsoft Foundry-Projekt.

1. Wählen Sie **Prompt flow** aus dem linken Seitenbereich.

1. Wählen Sie **+ Erstellen** aus dem Navigationsmenü.

    ![Select Promptflow.](../../../../../../translated_images/de/08-12-select-promptflow.6f4b451cb9821e5b.webp)

1. Wählen Sie **Chat flow** aus dem Navigationsmenü.

    ![Select chat flow.](../../../../../../translated_images/de/08-13-select-flow-type.2ec689b22da32591.webp)

1. Geben Sie den **Ordnernamen** ein, den Sie verwenden möchten.

    ![Enter name.](../../../../../../translated_images/de/08-14-enter-name.ff9520fefd89f40d.webp)

2. Wählen Sie **Erstellen**.

#### Einrichten des Prompt flows zum Chatten mit Ihrem benutzerdefinierten Phi-3-Modell

Sie müssen das feinabgestimmte Phi-3-Modell in einen Prompt flow integrieren. Der vorhandene bereitgestellte Prompt flow ist jedoch nicht für diesen Zweck ausgelegt. Daher müssen Sie den Prompt flow neu gestalten, um die Integration des benutzerdefinierten Modells zu ermöglichen.

1. Führen Sie im Prompt flow die folgenden Aufgaben aus, um den vorhandenen Flow neu aufzubauen:

    - Wählen Sie **Rohdateimodus**.
    - Löschen Sie alle vorhandenen Codes in der Datei *flow.dag.yml*.
    - Fügen Sie den folgenden Code in die Datei *flow.dag.yml* ein.

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

    - Wählen Sie **Speichern**.

    ![Select raw file mode.](../../../../../../translated_images/de/08-15-select-raw-file-mode.61d988b41df28985.webp)

1. Fügen Sie den folgenden Code in die Datei *integrate_with_promptflow.py* ein, um das benutzerdefinierte Phi-3-Modell in Prompt flow zu verwenden.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Protokollierungseinrichtung
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

        # "connection" ist der Name der benutzerdefinierten Verbindung, "endpoint", "key" sind die Schlüssel in der benutzerdefinierten Verbindung
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
            
            # Die vollständige JSON-Antwort protokollieren
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

    ![Paste prompt flow code.](../../../../../../translated_images/de/08-16-paste-promptflow-code.a6041b74a7d09777.webp)

> [!NOTE]
> Für detailliertere Informationen zur Verwendung von Prompt flow in Microsoft Foundry können Sie [Prompt flow in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) konsultieren.

1. Wählen Sie **Chat-Eingabe** und **Chat-Ausgabe**, um den Chat mit Ihrem Modell zu aktivieren.

    ![Input Output.](../../../../../../translated_images/de/08-17-select-input-output.64dbb39bbe59d03b.webp)

1. Nun sind Sie bereit, mit Ihrem benutzerdefinierten Phi-3-Modell zu chatten. Im nächsten Übungsteil lernen Sie, wie Sie den Prompt flow starten und ihn verwenden, um mit Ihrem feinabgestimmten Phi-3-Modell zu chatten.

> [!NOTE]
>
> Der neu aufgebaute Flow sollte wie im folgenden Bild aussehen:
>
> ![Flow example.](../../../../../../translated_images/de/08-18-graph-example.d6457533952e690c.webp)
>

### Chatten Sie mit Ihrem benutzerdefinierten Phi-3-Modell

Nachdem Sie Ihr benutzerdefiniertes Phi-3-Modell feinabgestimmt und in Prompt flow integriert haben, sind Sie bereit, mit ihm zu interagieren. Diese Übung führt Sie durch den Prozess der Einrichtung und des Startens eines Chats mit Ihrem Modell mittels Prompt flow. Wenn Sie diesen Schritten folgen, können Sie die Fähigkeiten Ihres feinabgestimmten Phi-3-Modells für verschiedene Aufgaben und Gespräche voll ausschöpfen.

- Chatten Sie mit Ihrem benutzerdefinierten Phi-3-Modell mithilfe von Prompt flow.

#### Starten des Prompt flows

1. Wählen Sie **Compute-Sitzungen starten**, um den Prompt flow zu starten.

    ![Start compute session.](../../../../../../translated_images/de/09-01-start-compute-session.a86fcf5be68e386b.webp)

1. Wählen Sie **Eingabe validieren und analysieren**, um Parameter zu erneuern.

    ![Validate input.](../../../../../../translated_images/de/09-02-validate-input.317c76ef766361e9.webp)

1. Wählen Sie den **Wert** der **Verbindung** zur benutzerdefinierten Verbindung, die Sie erstellt haben. Zum Beispiel *connection*.

    ![Connection.](../../../../../../translated_images/de/09-03-select-connection.99bdddb4b1844023.webp)

#### Chatten mit Ihrem benutzerdefinierten Modell

1. Wählen Sie **Chat**.

    ![Select chat.](../../../../../../translated_images/de/09-04-select-chat.61936dce6612a1e6.webp)

1. Hier ist ein Beispiel für die Ergebnisse: Nun können Sie mit Ihrem benutzerdefinierten Phi-3-Modell chatten. Es wird empfohlen, Fragen basierend auf den für das Fine-Tuning verwendeten Daten zu stellen.

    ![Chat with prompt flow.](../../../../../../translated_images/de/09-05-chat-with-promptflow.c8ca404c07ab126f.webp)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->