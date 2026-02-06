## Wie man Chat-Completion-Komponenten aus dem Azure ML System-Registry für die Feinabstimmung eines Modells verwendet

In diesem Beispiel werden wir die Feinabstimmung des Phi-3-mini-4k-instruct Modells durchführen, um ein Gespräch zwischen 2 Personen mit dem ultrachat_200k Datensatz zu vervollständigen.

![MLFineTune](../../../../translated_images/de/MLFineTune.928d4c6b3767dd35.webp)

Das Beispiel zeigt Ihnen, wie Sie die Feinabstimmung mit dem Azure ML SDK und Python durchführen und anschließend das feinabgestimmte Modell an einem Online-Endpunkt für Echtzeit-Inferenz bereitstellen.

### Trainingsdaten

Wir verwenden den ultrachat_200k Datensatz. Dies ist eine stark gefilterte Version des UltraChat-Datensatzes und wurde verwendet, um Zephyr-7B-β zu trainieren, ein hochmodernes 7b Chat-Modell.

### Modell

Wir verwenden das Phi-3-mini-4k-instruct Modell, um zu zeigen, wie Nutzer ein Modell für die Chat-Completion-Aufgabe feinabstimmen können. Wenn Sie dieses Notebook von einer bestimmten Modellkarte geöffnet haben, denken Sie daran, den spezifischen Modellnamen zu ersetzen.

### Aufgaben

- Wählen Sie ein Modell zur Feinabstimmung aus.
- Wählen und erkunden Sie Trainingsdaten.
- Konfigurieren Sie den Feinabstimmungsjob.
- Führen Sie den Feinabstimmungsjob aus.
- Überprüfen Sie Trainings- und Bewertungsmetriken.
- Registrieren Sie das feinabgestimmte Modell.
- Stellen Sie das feinabgestimmte Modell für Echtzeit-Inferenz bereit.
- Räumen Sie Ressourcen auf.

## 1. Einrichten der Voraussetzungen

- Abhängigkeiten installieren
- Verbindung zum AzureML Workspace herstellen. Erfahren Sie mehr unter Einrichtung der SDK-Authentifizierung. Ersetzen Sie <WORKSPACE_NAME>, <RESOURCE_GROUP> und <SUBSCRIPTION_ID> unten.
- Verbindung zum AzureML System-Registry herstellen
- Optionalen Experimentnamen setzen
- Compute prüfen oder erstellen.

> [!NOTE]
> Voraussetzungen: Ein einzelner GPU-Knoten kann mehrere GPU-Karten haben. Zum Beispiel hat ein Knoten des Typs Standard_NC24rs_v3 4 NVIDIA V100 GPUs, während Standard_NC12s_v3 2 NVIDIA V100 GPUs besitzt. Weitere Informationen finden Sie in der Dokumentation. Die Anzahl der GPU-Karten pro Knoten wird im Parameter gpus_per_node unten festgelegt. Die korrekte Einstellung dieses Werts gewährleistet die Nutzung aller GPUs im Knoten. Die empfohlenen GPU-Compute-SKUs finden Sie hier und hier.

### Python-Bibliotheken

Installieren Sie die Abhängigkeiten, indem Sie die folgende Zelle ausführen. Dies ist kein optionaler Schritt, wenn Sie in einer neuen Umgebung arbeiten.

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```
  
### Interaktion mit Azure ML

1. Dieses Python-Skript wird verwendet, um mit dem Azure Machine Learning (Azure ML) Service zu interagieren. Hier ist eine Zusammenfassung dessen, was es tut:

    - Es importiert notwendige Module aus den Paketen azure.ai.ml, azure.identity und azure.ai.ml.entities. Außerdem wird das Modul time importiert.

    - Es versucht, sich mit DefaultAzureCredential() zu authentifizieren, welches eine vereinfachte Authentifizierungserfahrung bietet, um Anwendungen, die in der Azure-Cloud laufen, schnell zu entwickeln. Falls dies fehlschlägt, wird auf InteractiveBrowserCredential() zurückgegriffen, das eine interaktive Login-Eingabeaufforderung bereitstellt.

    - Es versucht dann, eine MLClient-Instanz mit der from_config Methode zu erzeugen, die die Konfiguration aus der Standard-Konfigurationsdatei (config.json) ausliest. Falls dies fehlschlägt, wird eine MLClient-Instanz manuell mit subscription_id, resource_group_name und workspace_name erstellt.

    - Es erstellt eine weitere MLClient-Instanz, dieses Mal für das Azure ML Registry mit dem Namen "azureml". Dieses Registry ist der Speicherort für Modelle, Feinabstimmungs-Pipelines und Umgebungen.

    - Es setzt den experiment_name auf "chat_completion_Phi-3-mini-4k-instruct".

    - Es generiert einen eindeutigen Zeitstempel, indem die aktuelle Zeit (in Sekunden seit der Epoche, als Fließkommazahl) in einen Integer und anschließend in einen String konvertiert wird. Dieser Zeitstempel kann verwendet werden, um eindeutige Namen und Versionen zu erstellen.

    ```python
    # Importieren Sie die notwendigen Module von Azure ML und Azure Identity
    from azure.ai.ml import MLClient
    from azure.identity import (
        DefaultAzureCredential,
        InteractiveBrowserCredential,
    )
    from azure.ai.ml.entities import AmlCompute
    import time  # Importieren Sie das Zeitmodul
    
    # Versuchen Sie, sich mit DefaultAzureCredential zu authentifizieren
    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except Exception as ex:  # Falls DefaultAzureCredential fehlschlägt, verwenden Sie InteractiveBrowserCredential
        credential = InteractiveBrowserCredential()
    
    # Versuchen Sie, eine MLClient-Instanz mit der Standard-Konfigurationsdatei zu erstellen
    try:
        workspace_ml_client = MLClient.from_config(credential=credential)
    except:  # Falls dies fehlschlägt, erstellen Sie eine MLClient-Instanz durch manuelle Angabe der Details
        workspace_ml_client = MLClient(
            credential,
            subscription_id="<SUBSCRIPTION_ID>",
            resource_group_name="<RESOURCE_GROUP>",
            workspace_name="<WORKSPACE_NAME>",
        )
    
    # Erstellen Sie eine weitere MLClient-Instanz für das Azure ML-Register mit dem Namen "azureml"
    # Dieses Register ist der Speicherort für Modelle, Fine-Tuning-Pipelines und Umgebungen
    registry_ml_client = MLClient(credential, registry_name="azureml")
    
    # Setzen Sie den Namen des Experiments
    experiment_name = "chat_completion_Phi-3-mini-4k-instruct"
    
    # Generieren Sie einen eindeutigen Zeitstempel, der für Namen und Versionen verwendet werden kann, die eindeutig sein müssen
    timestamp = str(int(time.time()))
    ```
  
## 2. Wählen Sie ein Foundation-Modell zur Feinabstimmung aus

1. Phi-3-mini-4k-instruct ist ein 3,8 Milliarden Parameter leichtgewichtiges, hochmodernes Open-Model, das auf den für Phi-2 verwendeten Datensätzen basiert. Das Modell gehört zur Phi-3 Modellfamilie, und die Mini-Version gibt es in zwei Varianten 4K und 128K, welche die Kontextlänge (in Token) darstellen, die es unterstützen kann. Wir müssen das Modell für unseren spezifischen Zweck feinabstimmen, um es zu verwenden. Diese Modelle können Sie im Model Catalog im AzureML Studio durchsuchen, gefiltert nach der Chat-Completion-Aufgabe. In diesem Beispiel verwenden wir das Phi-3-mini-4k-instruct Modell. Wenn Sie dieses Notebook für ein anderes Modell geöffnet haben, ersetzen Sie den Modellnamen und die Version entsprechend.

> [!NOTE]
> die Eigenschaft model id des Modells. Diese wird als Eingabe für den Feinabstimmungsjob verwendet. Diese ist auch als Asset-ID-Feld auf der Modell-Detailseite im AzureML Studio Model Catalog verfügbar.

2. Dieses Python-Skript interagiert mit dem Azure Machine Learning (Azure ML) Service. Hier ist eine Zusammenfassung dessen, was es tut:

    - Es setzt model_name auf "Phi-3-mini-4k-instruct".

    - Es verwendet die get-Methode der models-Eigenschaft des registry_ml_client-Objekts, um die neueste Version des Modells mit dem angegebenen Namen aus dem Azure ML Registry abzurufen. Die get-Methode wird mit zwei Argumenten aufgerufen: dem Namen des Modells und einem Label, das angibt, dass die neueste Version des Modells abgerufen werden soll.

    - Es gibt eine Meldung auf der Konsole aus, die den Namen, die Version und die ID des Modells angibt, das für die Feinabstimmung verwendet wird. Die format-Methode des Strings wird verwendet, um den Namen, die Version und die ID des Modells in die Meldung einzufügen. Name, Version und ID des Modells werden als Eigenschaften des foundation_model-Objekts abgerufen.

    ```python
    # Setzen Sie den Modellnamen
    model_name = "Phi-3-mini-4k-instruct"
    
    # Holen Sie die neueste Version des Modells aus dem Azure ML-Register
    foundation_model = registry_ml_client.models.get(model_name, label="latest")
    
    # Drucken Sie den Modellnamen, die Version und die ID aus
    # Diese Informationen sind nützlich für die Nachverfolgung und Fehlerbehebung
    print(
        "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
            foundation_model.name, foundation_model.version, foundation_model.id
        )
    )
    ```
  
## 3. Erstellen Sie einen Compute zur Verwendung im Job

Der Feinabstimmungs-Job arbeitet NUR mit GPU-Compute. Die Größe des Compute hängt davon ab, wie groß das Modell ist, und meist ist es schwierig, die richtige Größe für den Job zu identifizieren. In dieser Zelle leiten wir den Nutzer an, den richtigen Compute für den Job auszuwählen.

> [!NOTE]
> Die unten aufgelisteten Compute-Instanzen arbeiten mit der am besten optimierten Konfiguration. Änderungen an der Konfiguration können zu Cuda Out Of Memory Fehlern führen. In solchen Fällen versuchen Sie, den Compute auf eine größere Größe zu upgraden.

> [!NOTE]
> Achten Sie beim Auswählen der compute_cluster_size unten darauf, dass der Compute in Ihrer Ressourcengruppe verfügbar ist. Wenn ein bestimmter Compute nicht verfügbar ist, können Sie einen Antrag stellen, um Zugang zu den Compute-Ressourcen zu erhalten.

### Überprüfung des Modells auf Unterstützung für Feinabstimmung

1. Dieses Python-Skript interagiert mit einem Azure Machine Learning (Azure ML) Modell. Hier eine Zusammenfassung dessen, was es tut:

    - Es importiert das ast-Modul, das Funktionen bereitstellt, um Bäume der abstrakten Syntax von Python zu verarbeiten.

    - Es prüft, ob das foundation_model-Objekt (das ein Modell in Azure ML repräsentiert) einen Tag namens finetune_compute_allow_list besitzt. Tags in Azure ML sind Schlüssel-Wert-Paare, die Sie erstellen und zum Filtern und Sortieren von Modellen verwenden können.

    - Falls der Tag finetune_compute_allow_list vorhanden ist, wird der Wert des Tags (ein String) mit der Funktion ast.literal_eval sicher in eine Python-Liste geparst. Diese Liste wird dann der Variable computes_allow_list zugewiesen. Es wird eine Meldung ausgegeben, die angibt, dass ein Compute aus der Liste erstellt werden sollte.

    - Falls der Tag finetune_compute_allow_list nicht vorhanden ist, wird computes_allow_list auf None gesetzt und eine Meldung ausgegeben, die angibt, dass der Tag finetune_compute_allow_list nicht zu den Tags des Modells gehört.

    - Zusammenfassend prüft dieses Skript auf einen bestimmten Tag in den Metadaten des Modells, wandelt den Wert des Tags bei Vorhandensein in eine Liste um und gibt entsprechende Rückmeldung an den Nutzer.

    ```python
    # Importiere das ast-Modul, das Funktionen zur Verarbeitung von Bäumen der Python-abstrakten Syntaxgrammatik bereitstellt
    import ast
    
    # Überprüfe, ob der Tag 'finetune_compute_allow_list' in den Tags des Modells vorhanden ist
    if "finetune_compute_allow_list" in foundation_model.tags:
        # Wenn der Tag vorhanden ist, verwende ast.literal_eval, um den Wert des Tags (einen String) sicher in eine Python-Liste zu parsen
        computes_allow_list = ast.literal_eval(
            foundation_model.tags["finetune_compute_allow_list"]
        )  # Konvertiere String in Python-Liste
        # Gib eine Nachricht aus, die anzeigt, dass ein Compute aus der Liste erstellt werden soll
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Wenn der Tag nicht vorhanden ist, setze computes_allow_list auf None
        computes_allow_list = None
        # Gib eine Nachricht aus, die anzeigt, dass der Tag 'finetune_compute_allow_list' nicht zu den Tags des Modells gehört
        print("`finetune_compute_allow_list` is not part of model tags")
    ```
  
### Überprüfung der Compute-Instanz

1. Dieses Python-Skript interagiert mit dem Azure Machine Learning (Azure ML) Service und führt mehrere Prüfungen an einer Compute-Instanz durch. Hier eine Zusammenfassung dessen, was es tut:

    - Es versucht die Compute-Instanz mit dem im compute_cluster gespeicherten Namen aus dem Azure ML Workspace abzurufen. Wenn der Bereitstellungsstatus des Compute-Clusters "failed" ist, wird ein ValueError ausgelöst.

    - Es prüft, ob computes_allow_list nicht None ist. Wenn dies der Fall ist, werden alle Compute-Größen in der Liste in Kleinbuchstaben umgewandelt und geprüft, ob die Größe der aktuellen Compute-Instanz in der Liste enthalten ist. Wenn nicht, wird ein ValueError ausgelöst.

    - Wenn computes_allow_list None ist, wird geprüft, ob die Größe der Compute-Instanz in einer Liste von nicht unterstützten GPU-VM-Größen enthalten ist. Wenn ja, wird ein ValueError ausgelöst.

    - Es holt eine Liste aller verfügbaren Compute-Größen im Workspace. Danach wird über diese Liste iteriert, und für jede Compute-Größe geprüft, ob deren Name mit der Größe der aktuellen Compute-Instanz übereinstimmt. Wenn ja, wird die Anzahl der GPUs für diese Compute-Größe abgerufen und gpu_count_found auf True gesetzt.

    - Wenn gpu_count_found True ist, wird die Anzahl der GPUs in der Compute-Instanz ausgegeben. Falls gpu_count_found False ist, wird ein ValueError ausgelöst.

    - Zusammengefasst führt das Skript mehrere Prüfungen an einer Compute-Instanz in einem Azure ML Workspace durch, inklusive des Bereitstellungsstatus, der Größe im Vergleich zu einer Allow-Liste oder Deny-Liste und der Anzahl der GPUs, die vorhanden sind.

    ```python
    # Gib die Ausnahmemeldung aus
    print(e)
    # Löst einen ValueError aus, wenn die Berechnungsgröße im Workspace nicht verfügbar ist
    raise ValueError(
        f"WARNING! Compute size {compute_cluster_size} not available in workspace"
    )
    
    # Ruft die Compute-Instanz aus dem Azure ML-Workspace ab
    compute = workspace_ml_client.compute.get(compute_cluster)
    # Prüft, ob der Bereitstellungsstatus der Compute-Instanz "fehlerhaft" ist
    if compute.provisioning_state.lower() == "failed":
        # Löst einen ValueError aus, wenn der Bereitstellungsstatus "fehlerhaft" ist
        raise ValueError(
            f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
            f"please try creating a different compute"
        )
    
    # Prüft, ob computes_allow_list nicht None ist
    if computes_allow_list is not None:
        # Konvertiert alle Berechnungsgrößen in computes_allow_list in Kleinbuchstaben
        computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
        # Prüft, ob die Größe der Compute-Instanz in computes_allow_list_lower_case enthalten ist
        if compute.size.lower() not in computes_allow_list_lower_case:
            # Löst einen ValueError aus, wenn die Größe der Compute-Instanz nicht in computes_allow_list_lower_case enthalten ist
            raise ValueError(
                f"VM size {compute.size} is not in the allow-listed computes for finetuning"
            )
    else:
        # Definiert eine Liste von nicht unterstützten GPU-VM-Größen
        unsupported_gpu_vm_list = [
            "standard_nc6",
            "standard_nc12",
            "standard_nc24",
            "standard_nc24r",
        ]
        # Prüft, ob die Größe der Compute-Instanz in unsupported_gpu_vm_list enthalten ist
        if compute.size.lower() in unsupported_gpu_vm_list:
            # Löst einen ValueError aus, wenn die Größe der Compute-Instanz in unsupported_gpu_vm_list enthalten ist
            raise ValueError(
                f"VM size {compute.size} is currently not supported for finetuning"
            )
    
    # Initialisiert eine Variable, um zu überprüfen, ob die Anzahl der GPUs in der Compute-Instanz gefunden wurde
    gpu_count_found = False
    # Ruft eine Liste aller verfügbaren Berechnungsgrößen im Workspace ab
    workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
    available_sku_sizes = []
    # Iteriert über die Liste der verfügbaren Berechnungsgrößen
    for compute_sku in workspace_compute_sku_list:
        available_sku_sizes.append(compute_sku.name)
        # Prüft, ob der Name der Berechnungsgröße mit der Größe der Compute-Instanz übereinstimmt
        if compute_sku.name.lower() == compute.size.lower():
            # Falls ja, wird die Anzahl der GPUs für diese Berechnungsgröße abgerufen und gpu_count_found auf True gesetzt
            gpus_per_node = compute_sku.gpus
            gpu_count_found = True
    # Wenn gpu_count_found True ist, wird die Anzahl der GPUs in der Compute-Instanz ausgegeben
    if gpu_count_found:
        print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
    else:
        # Wenn gpu_count_found False ist, wird ein ValueError ausgelöst
        raise ValueError(
            f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
            f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
        )
    ```
  
## 4. Wählen Sie den Datensatz zur Feinabstimmung des Modells aus

1. Wir verwenden den ultrachat_200k Datensatz. Der Datensatz hat vier Splits, geeignet für überwachtes Feinabstimmen (sft).
Generierung-Ranking (gen). Die Anzahl der Beispiele pro Split ist wie folgt angezeigt:

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```
  
1. Die nächsten Zellen zeigen die Basis-Datenvorbereitung für die Feinabstimmung:

### Einige Datenzeilen visualisieren

Wir möchten, dass dieses Beispiel schnell läuft, daher speichern wir die Dateien train_sft, test_sft mit 5% der bereits reduzierten Zeilen. Das bedeutet, dass das feinabgestimmte Modell eine geringere Genauigkeit hat und daher nicht für den produktiven Einsatz geeignet ist.  
Das download-dataset.py Skript wird verwendet, um den ultrachat_200k Datensatz herunterzuladen und den Datensatz in ein Format umzuwandeln, das von der Finetune-Pipeline-Komponente konsumiert werden kann. Da der Datensatz sehr groß ist, haben wir hier nur einen Teil davon.

1. Das Ausführen des nachfolgenden Skripts lädt nur 5% der Daten herunter. Dies kann erhöht werden, indem der Parameter dataset_split_pc auf den gewünschten Prozentsatz gesetzt wird.

> [!NOTE]
> Einige Sprachmodelle verwenden unterschiedliche Sprachcodes, weshalb die Spaltennamen im Datensatz entsprechend angepasst sein sollten.

1. Hier ein Beispiel, wie die Daten aussehen sollten:  
Der Chat-Completion-Datensatz wird im Parquet-Format gespeichert, wobei jeder Eintrag folgendem Schema folgt:

    - Dies ist ein JSON (JavaScript Object Notation) Dokument, ein populäres Datenformat zum Austausch von Daten. Es ist kein ausführbarer Code, sondern eine Möglichkeit, Daten zu speichern und zu transportieren. Hier ist eine Gliederung seiner Struktur:

    - "prompt": Dieser Schlüssel enthält einen String-Wert, der eine Aufgabe oder Frage an eine KI-Assistentin repräsentiert.

    - "messages": Dieser Schlüssel enthält ein Array von Objekten. Jedes Objekt stellt eine Nachricht in einer Unterhaltung zwischen einem Nutzer und einem KI-Assistenten dar. Jedes Nachrichtenobjekt hat zwei Schlüssel:

    - "content": Dieser Schlüssel enthält einen String-Wert, der den Inhalt der Nachricht repräsentiert.
    - "role": Dieser Schlüssel enthält einen String-Wert, der die Rolle der Entität angibt, die die Nachricht gesendet hat. Dies kann entweder "user" oder "assistant" sein.
    - "prompt_id": Dieser Schlüssel enthält eine eindeutige Kennung für den Prompt.

1. In diesem speziellen JSON-Dokument wird eine Unterhaltung dargestellt, in der ein Nutzer einen KI-Assistenten bittet, einen Protagonisten für eine dystopische Geschichte zu erstellen. Der Assistent antwortet und der Nutzer bittet dann um mehr Details. Der Assistent stimmt zu, mehr Details zu liefern. Die gesamte Unterhaltung ist mit einer spezifischen Prompt-ID verknüpft.

    ```python
    {
        // The task or question posed to an AI assistant
        "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
        
        // An array of objects, each representing a message in a conversation between a user and an AI assistant
        "messages":[
            {
                // The content of the user's message
                "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
                // The role of the entity that sent the message
                "role": "user"
            },
            {
                // The content of the assistant's message
                "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
                // The role of the entity that sent the message
                "role": "assistant"
            },
            {
                // The content of the user's message
                "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
                // The role of the entity that sent the message
                "role": "user"
            }, 
            {
                // The content of the assistant's message
                "content": "Certainly! ....",
                // The role of the entity that sent the message
                "role": "assistant"
            }
        ],
        
        // A unique identifier for the prompt
        "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
    }
    ```
  
### Daten herunterladen

1. Dieses Python-Skript dient dazu, einen Datensatz mit einem Hilfsskript namens download-dataset.py herunterzuladen. Hier eine Zusammenfassung dessen, was es tut:

    - Es importiert das os-Modul, das eine plattformübergreifende Nutzung Betriebssystem-abhängiger Funktionen ermöglicht.

    - Es verwendet die Funktion os.system, um das Skript download-dataset.py mit bestimmten Kommandozeilenargumenten in der Shell auszuführen. Die Argumente geben an, welcher Datensatz heruntergeladen werden soll (HuggingFaceH4/ultrachat_200k), in welches Verzeichnis (ultrachat_200k_dataset), und welcher Prozentsatz des Datensatzes (5). Die Funktion os.system gibt den Exit-Status des Befehls zurück; dieser Wert wird in der Variable exit_status gespeichert.

    - Es prüft, ob exit_status ungleich 0 ist. In Unix-ähnlichen Betriebssystemen weist ein Exit-Status von 0 meist darauf hin, dass ein Befehl erfolgreich war, während jeder andere Wert einen Fehler signalisiert. Ist exit_status ungleich 0, wird eine Exception mit einer Nachricht ausgelöst, die einen Fehler beim Herunterladen des Datensatzes beschreibt.

    - Zusammengefasst wird ein Befehl zum Herunterladen eines Datensatzes mittels eines Hilfsskripts ausgeführt, und falls dieser Befehl fehlschlägt, wird eine Ausnahme ausgelöst. 

    ```python
    # Importieren Sie das os-Modul, das eine Möglichkeit bietet, betriebssystemabhängige Funktionen zu verwenden
    import os
    
    # Verwenden Sie die Funktion os.system, um das Skript download-dataset.py mit spezifischen Befehlszeilenargumenten in der Shell auszuführen
    # Die Argumente geben den herunterzuladenden Datensatz an (HuggingFaceH4/ultrachat_200k), das Verzeichnis, in das heruntergeladen werden soll (ultrachat_200k_dataset), und den Prozentsatz des Datensatzes zum Aufteilen (5)
    # Die Funktion os.system gibt den Exit-Status des ausgeführten Befehls zurück; dieser Status wird in der Variablen exit_status gespeichert
    exit_status = os.system(
        "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
    )
    
    # Prüfen Sie, ob exit_status nicht 0 ist
    # In Unix-ähnlichen Betriebssystemen zeigt ein Exit-Status von 0 normalerweise an, dass ein Befehl erfolgreich war, während jede andere Zahl einen Fehler anzeigt
    # Wenn exit_status nicht 0 ist, werfen Sie eine Ausnahme mit einer Meldung, die angibt, dass es einen Fehler beim Herunterladen des Datensatzes gab
    if exit_status != 0:
        raise Exception("Error downloading dataset")
    ```
  
### Laden der Daten in ein DataFrame

1. Dieses Python-Skript lädt eine JSON Lines-Datei in ein pandas DataFrame und zeigt die ersten 5 Zeilen an. Hier eine Zusammenfassung dessen, was es tut:

    - Es importiert die pandas-Bibliothek, welche eine leistungsstarke Bibliothek zur Datenmanipulation und -analyse ist.

    - Es setzt die maximale Spaltenbreite für die pandas-Anzeigeoptionen auf 0. Das bedeutet, dass der vollständige Text jeder Spalte angezeigt wird, ohne dass abgeschnitten wird, wenn das DataFrame ausgegeben wird.
    - Es verwendet die Funktion pd.read_json, um die Datei train_sft.jsonl aus dem Verzeichnis ultrachat_200k_dataset in ein DataFrame zu laden. Das Argument lines=True gibt an, dass die Datei im JSON Lines-Format vorliegt, bei dem jede Zeile ein separates JSON-Objekt ist.

    - Es verwendet die Methode head, um die ersten 5 Zeilen des DataFrames anzuzeigen. Wenn das DataFrame weniger als 5 Zeilen hat, werden alle angezeigt.

    - Zusammenfassend lädt dieses Skript eine JSON Lines-Datei in ein DataFrame und zeigt die ersten 5 Zeilen mit vollem Spaltentext an.
    
    ```python
    # Importiere die pandas-Bibliothek, die eine leistungsstarke Bibliothek zur Datenmanipulation und -analyse ist
    import pandas as pd
    
    # Setze die maximale Spaltenbreite für die Anzeigeoptionen von pandas auf 0
    # Das bedeutet, dass der volle Text jeder Spalte ohne Abschneidung angezeigt wird, wenn der DataFrame ausgegeben wird
    pd.set_option("display.max_colwidth", 0)
    
    # Verwende die Funktion pd.read_json, um die Datei train_sft.jsonl aus dem Verzeichnis ultrachat_200k_dataset in einen DataFrame zu laden
    # Das Argument lines=True zeigt an, dass die Datei im JSON Lines-Format vorliegt, bei dem jede Zeile ein separates JSON-Objekt ist
    df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)
    
    # Verwende die Methode head, um die ersten 5 Zeilen des DataFrames anzuzeigen
    # Wenn der DataFrame weniger als 5 Zeilen hat, werden alle angezeigt
    df.head()
    ```

## 5. Senden Sie den Feinabstimmungsauftrag unter Verwendung des Modells und der Daten als Eingaben

Erstellen Sie den Auftrag, der die Chat-Completion-Pipeline-Komponente verwendet. Erfahren Sie mehr über alle für die Feinabstimmung unterstützten Parameter.

### Definieren Sie Feinabstimmungsparameter

1. Feinabstimmungsparameter können in 2 Kategorien eingeteilt werden – Trainingsparameter, Optimierungsparameter

1. Trainingsparameter definieren die Trainingsaspekte wie -

    - Der zu verwendende Optimierer, Scheduler
    - Die Metrik zur Optimierung der Feinabstimmung
    - Anzahl der Trainingsschritte und die Batchgröße usw.
    - Optimierungsparameter helfen, den GPU-Speicher zu optimieren und die Rechenressourcen effektiv zu nutzen. 

1. Nachfolgend einige der Parameter, die zu dieser Kategorie gehören. Die Optimierungsparameter unterscheiden sich je nach Modell und werden mit dem Modell geliefert, um diese Unterschiede zu handhaben.

    - Aktivieren Sie DeepSpeed und LoRA
    - Aktivieren Sie das Training mit gemischter Genauigkeit
    - Aktivieren Sie das Training auf mehreren Knoten

> [!NOTE]
> Überwachtes Feinabstimmen kann zu Verlust der Ausrichtung oder katastrophalem Vergessen führen. Wir empfehlen, dieses Problem zu überprüfen und nach der Feinabstimmung eine Ausrichtungsphase durchzuführen.

### Feinabstimmungsparameter

1. Dieses Python-Skript richtet Parameter für das Feinabstimmen eines Machine-Learning-Modells ein. Hier eine Übersicht dessen, was es macht:

    - Es legt Standard-Trainingsparameter wie die Anzahl der Trainings-Epochen, Batch-Größen für Training und Evaluation, Lernrate und Typ des Lernraten-Schedulers fest.

    - Es legt Standard-Optimierungsparameter fest, wie z.B. ob Layer-wise Relevance Propagation (LoRa) und DeepSpeed angewendet werden, sowie die DeepSpeed-Stufe.

    - Es kombiniert die Trainings- und Optimierungsparameter in einem einzigen Dictionary namens finetune_parameters.

    - Es prüft, ob das Foundation Model modell-spezifische Standardparameter hat. Falls ja, wird eine Warnmeldung ausgegeben und das finetune_parameters-Dictionary mit diesen modell-spezifischen Standardeinstellungen aktualisiert. Die Funktion ast.literal_eval wird verwendet, um die modell-spezifischen Standardwerte von einem String in ein Python Dictionary zu konvertieren.

    - Es gibt die endgültigen Feinabstimmungsparameter aus, die für den Lauf verwendet werden.

    - Zusammengefasst richtet dieses Skript die Parameter für die Feinabstimmung eines Machine-Learning-Modells ein und zeigt sie an, wobei es möglich ist, die Standardparameter durch modell-spezifische zu überschreiben.

    ```python
    # Standard-Trainingsparameter wie die Anzahl der Trainingsepochen, Batch-Größen für Training und Bewertung, Lernrate und Typ des Lernraten-Schedulers festlegen
    training_parameters = dict(
        num_train_epochs=3,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        learning_rate=5e-6,
        lr_scheduler_type="cosine",
    )
    
    # Standard-Optimierungsparameter festlegen, wie z.B. ob Layer-wise Relevance Propagation (LoRa) und DeepSpeed angewendet werden sollen, sowie die DeepSpeed-Stufe
    optimization_parameters = dict(
        apply_lora="true",
        apply_deepspeed="true",
        deepspeed_stage=2,
    )
    
    # Die Trainings- und Optimierungsparameter in einem einzigen Wörterbuch namens finetune_parameters zusammenfassen
    finetune_parameters = {**training_parameters, **optimization_parameters}
    
    # Überprüfen, ob das foundation_model modell-spezifische Standardparameter hat
    # Falls ja, eine Warnmeldung ausgeben und das finetune_parameters-Wörterbuch mit diesen modell-spezifischen Standardwerten aktualisieren
    # Die Funktion ast.literal_eval wird verwendet, um die modell-spezifischen Standardwerte von einem String in ein Python-Wörterbuch umzuwandeln
    if "model_specific_defaults" in foundation_model.tags:
        print("Warning! Model specific defaults exist. The defaults could be overridden.")
        finetune_parameters.update(
            ast.literal_eval(  # String in Python-Dictionary umwandeln
                foundation_model.tags["model_specific_defaults"]
            )
        )
    
    # Die endgültigen Fine-Tuning-Parameter ausgeben, die für den Durchlauf verwendet werden
    print(
        f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
    )
    ```

### Trainings-Pipeline

1. Dieses Python-Skript definiert eine Funktion, um einen Anzeigennamen für eine Machine-Learning-Trainings-Pipeline zu generieren, und ruft diese Funktion dann auf, um den Anzeigennamen zu generieren und auszugeben. Hier eine Übersicht dessen, was es macht:

1. Die Funktion get_pipeline_display_name wird definiert. Diese Funktion erzeugt einen Anzeigennamen basierend auf verschiedenen Parametern, die mit der Trainings-Pipeline zusammenhängen.

1. Innerhalb der Funktion berechnet sie die Gesamt-Batchgröße, indem sie die Batchgröße pro Gerät mit der Anzahl der Gradienten-Akkumulationsschritte, der Anzahl der GPUs pro Knoten und der Anzahl der für die Feinabstimmung verwendeten Knoten multipliziert.

1. Sie ruft verschiedene weitere Parameter ab, wie z.B. den Typ des Lernraten-Schedulers, ob DeepSpeed angewendet wird, die DeepSpeed-Stufe, ob Layer-wise Relevance Propagation (LoRa) angewendet wird, die Begrenzung der Anzahl der zu behaltenden Modell-Checkpoints und die maximale Sequenzlänge.

1. Sie erstellt einen String, der all diese Parameter enthält, getrennt durch Bindestriche. Wenn DeepSpeed oder LoRa angewendet wird, enthält der String "ds" gefolgt von der DeepSpeed-Stufe oder "lora". Wenn nicht, enthält er stattdessen "nods" oder "nolora".

1. Die Funktion gibt diesen String zurück, der als Anzeigename für die Trainings-Pipeline dient.

1. Nachdem die Funktion definiert wurde, wird sie aufgerufen, um den Anzeigennamen zu generieren, welcher dann ausgegeben wird.

1. Zusammengefasst generiert dieses Skript basierend auf verschiedenen Parametern einen Anzeigennamen für eine Machine-Learning-Trainings-Pipeline und gibt diesen Anzeigennamen aus.

    ```python
    # Definieren Sie eine Funktion, um einen Anzeigenamen für die Trainingspipeline zu generieren
    def get_pipeline_display_name():
        # Berechnen Sie die gesamte Batch-Größe, indem Sie die Batch-Größe pro Gerät, die Anzahl der Gradienten-Akkumulationsschritte, die Anzahl der GPUs pro Knoten und die Anzahl der für das Fine-Tuning verwendeten Knoten multiplizieren
        batch_size = (
            int(finetune_parameters.get("per_device_train_batch_size", 1))
            * int(finetune_parameters.get("gradient_accumulation_steps", 1))
            * int(gpus_per_node)
            * int(finetune_parameters.get("num_nodes_finetune", 1))
        )
        # Rufen Sie den Typ des Lernraten-Schedulers ab
        scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
        # Rufen Sie ab, ob DeepSpeed angewendet wird
        deepspeed = finetune_parameters.get("apply_deepspeed", "false")
        # Rufen Sie die DeepSpeed-Stufe ab
        ds_stage = finetune_parameters.get("deepspeed_stage", "2")
        # Wenn DeepSpeed angewendet wird, fügen Sie "ds" gefolgt von der DeepSpeed-Stufe im Anzeigenamen hinzu; wenn nicht, fügen Sie "nods" hinzu
        if deepspeed == "true":
            ds_string = f"ds{ds_stage}"
        else:
            ds_string = "nods"
        # Rufen Sie ab, ob Layer-wise Relevance Propagation (LoRa) angewendet wird
        lora = finetune_parameters.get("apply_lora", "false")
        # Wenn LoRa angewendet wird, fügen Sie "lora" im Anzeigenamen hinzu; wenn nicht, fügen Sie "nolora" hinzu
        if lora == "true":
            lora_string = "lora"
        else:
            lora_string = "nolora"
        # Rufen Sie das Limit für die Anzahl der aufzubewahrenden Modellprüfpunkte ab
        save_limit = finetune_parameters.get("save_total_limit", -1)
        # Rufen Sie die maximale Sequenzlänge ab
        seq_len = finetune_parameters.get("max_seq_length", -1)
        # Erstellen Sie den Anzeigenamen, indem Sie alle diese Parameter durch Bindestriche getrennt zusammenfügen
        return (
            model_name
            + "-"
            + "ultrachat"
            + "-"
            + f"bs{batch_size}"
            + "-"
            + f"{scheduler}"
            + "-"
            + ds_string
            + "-"
            + lora_string
            + f"-save_limit{save_limit}"
            + f"-seqlen{seq_len}"
        )
    
    # Rufen Sie die Funktion zum Generieren des Anzeigennamens auf
    pipeline_display_name = get_pipeline_display_name()
    # Geben Sie den Anzeigenamen aus
    print(f"Display name used for the run: {pipeline_display_name}")
    ```

### Pipeline konfigurieren

Dieses Python-Skript definiert und konfiguriert eine Machine-Learning-Pipeline mithilfe des Azure Machine Learning SDK. Hier eine Übersicht dessen, was es macht:

1. Es importiert erforderliche Module aus dem Azure AI ML SDK.

1. Es holt eine Pipeline-Komponente namens „chat_completion_pipeline“ aus dem Registrierungsdienst.

1. Es definiert einen Pipeline-Job mithilfe des `@pipeline`-Dekorators und der Funktion `create_pipeline`. Der Name der Pipeline wird auf `pipeline_display_name` gesetzt.

1. Innerhalb der Funktion `create_pipeline` wird die abgerufene Pipeline-Komponente mit verschiedenen Parametern initialisiert, darunter der Modellpfad, Compute-Cluster für verschiedene Phasen, Dataset-Splits für Training und Test, die Anzahl der für die Feinabstimmung zu verwendenden GPUs und weitere Feinabstimmungsparameter.

1. Es ordnet die Ausgabe des Feinabstimmungs-Jobs der Ausgabe des Pipeline-Jobs zu. Dies geschieht, damit das feinabgestimmte Modell einfach registriert werden kann, was erforderlich ist, um das Modell an einen Online- oder Batch-Endpunkt zu deployen.

1. Es erstellt eine Instanz der Pipeline, indem die Funktion `create_pipeline` aufgerufen wird.

1. Die Einstellung `force_rerun` der Pipeline wird auf `True` gesetzt, was bedeutet, dass gecachte Ergebnisse aus vorherigen Jobs nicht verwendet werden.

1. Die Einstellung `continue_on_step_failure` der Pipeline wird auf `False` gesetzt, was bedeutet, dass die Pipeline bei einem fehlgeschlagenen Schritt stoppt.

1. Zusammengefasst definiert und konfiguriert dieses Skript eine Machine-Learning-Pipeline für eine Chat Completion-Aufgabe mit dem Azure Machine Learning SDK.

    ```python
    # Notwendige Module aus dem Azure AI ML SDK importieren
    from azure.ai.ml.dsl import pipeline
    from azure.ai.ml import Input
    
    # Die Pipeline-Komponente mit dem Namen "chat_completion_pipeline" aus dem Register abrufen
    pipeline_component_func = registry_ml_client.components.get(
        name="chat_completion_pipeline", label="latest"
    )
    
    # Die Pipeline-Job mit dem @pipeline-Dekorator und der Funktion create_pipeline definieren
    # Der Name der Pipeline wird auf pipeline_display_name gesetzt
    @pipeline(name=pipeline_display_name)
    def create_pipeline():
        # Die abgerufene Pipeline-Komponente mit verschiedenen Parametern initialisieren
        # Diese umfassen den Modellpfad, Compute-Cluster für verschiedene Phasen, Datensatzaufteilungen für Training und Test, die Anzahl der GPUs für das Fine-Tuning und weitere Fine-Tuning-Parameter
        chat_completion_pipeline = pipeline_component_func(
            mlflow_model_path=foundation_model.id,
            compute_model_import=compute_cluster,
            compute_preprocess=compute_cluster,
            compute_finetune=compute_cluster,
            compute_model_evaluation=compute_cluster,
            # Die Datensatzaufteilungen den Parametern zuordnen
            train_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
            ),
            test_file_path=Input(
                type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
            ),
            # Trainingseinstellungen
            number_of_gpu_to_use_finetuning=gpus_per_node,  # Wird auf die Anzahl der verfügbaren GPUs im Compute gesetzt
            **finetune_parameters
        )
        return {
            # Die Ausgabe des Fine-Tuning-Jobs auf die Ausgabe des Pipeline-Jobs abbilden
            # Dies wird gemacht, damit wir das feinabgestimmte Modell leicht registrieren können
            # Die Registrierung des Modells ist erforderlich, um das Modell an einem Online- oder Batch-Endpunkt bereitzustellen
            "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
        }
    
    # Eine Instanz der Pipeline durch Aufrufen der Funktion create_pipeline erstellen
    pipeline_object = create_pipeline()
    
    # Keine zwischengespeicherten Ergebnisse früherer Jobs verwenden
    pipeline_object.settings.force_rerun = True
    
    # Continue on Step Failure auf False setzen
    # Das bedeutet, dass die Pipeline stoppt, wenn ein Schritt fehlschlägt
    pipeline_object.settings.continue_on_step_failure = False
    ```

### Job senden

1. Dieses Python-Skript sendet einen Machine-Learning-Pipeline-Job an einen Azure Machine Learning-Arbeitsbereich und wartet dann auf die Fertigstellung des Jobs. Hier eine Übersicht dessen, was es macht:

    - Es ruft die Methode create_or_update des Jobs-Objekts in workspace_ml_client auf, um den Pipeline-Job zu senden. Die auszuführende Pipeline wird durch pipeline_object angegeben, und das Experiment unter dem der Job ausgeführt wird, wird durch experiment_name angegeben.

    - Anschließend ruft es die Methode stream des Jobs-Objekts in workspace_ml_client auf, um auf die Fertigstellung des Pipeline-Jobs zu warten. Der zu wartende Job wird durch das Attribut name des Pipeline_Job-Objekts angegeben.

    - Zusammenfassend sendet dieses Skript einen Machine-Learning-Pipeline-Job an einen Azure Machine Learning-Arbeitsbereich und wartet auf dessen Fertigstellung.

    ```python
    # Senden Sie den Pipeline-Job an den Azure Machine Learning-Arbeitsbereich
    # Die auszuführende Pipeline wird durch pipeline_object angegeben
    # Das Experiment, unter dem der Job ausgeführt wird, wird durch experiment_name angegeben
    pipeline_job = workspace_ml_client.jobs.create_or_update(
        pipeline_object, experiment_name=experiment_name
    )
    
    # Warten Sie darauf, dass der Pipeline-Job abgeschlossen wird
    # Der zu wartende Job wird durch das Namensattribut des pipeline_job-Objekts angegeben
    workspace_ml_client.jobs.stream(pipeline_job.name)
    ```

## 6. Registrieren Sie das feinabgestimmte Modell im Arbeitsbereich

Wir registrieren das Modell aus der Ausgabe des Feinabstimmungs-Jobs. Dies verfolgt die Herkunft zwischen dem feinabgestimmten Modell und dem Feinabstimmungs-Job. Der Feinabstimmungs-Job verfolgt außerdem die Herkunft vom Foundation Model, den Daten und dem Trainingscode.

### Registrierung des ML-Modells

1. Dieses Python-Skript registriert ein Machine-Learning-Modell, das in einer Azure Machine Learning-Pipeline trainiert wurde. Hier eine Übersicht dessen, was es macht:

    - Es importiert notwendige Module aus dem Azure AI ML SDK.

    - Es prüft, ob die Ausgabe trained_model vom Pipeline-Job verfügbar ist, indem es die Methode get des Jobs-Objekts in workspace_ml_client aufruft und auf das outputs-Attribut zugreift.

    - Es erstellt einen Pfad zum trainierten Modell, indem es einen String formatiert, der den Namen des Pipeline-Jobs und den Namen der Ausgabe ("trained_model") enthält.

    - Es definiert einen Namen für das feinabgestimmte Modell, indem "-ultrachat-200k" an den ursprünglichen Modellnamen angehängt und alle Schrägstriche durch Bindestriche ersetzt werden.

    - Es bereitet die Registrierung des Modells vor, indem es ein Model-Objekt mit verschiedenen Parametern erstellt, darunter der Pfad zum Modell, der Modelltyp (MLflow-Modell), der Name und die Version des Modells sowie eine Beschreibung des Modells.

    - Es registriert das Modell, indem es die Methode create_or_update des Models-Objekts in workspace_ml_client mit dem Model-Objekt als Argument aufruft.

    - Es gibt das registrierte Modell aus.

1. Zusammengefasst registriert dieses Skript ein Machine-Learning-Modell, das in einer Azure Machine Learning-Pipeline trainiert wurde.
    
    ```python
    # Importieren Sie notwendige Module aus dem Azure AI ML SDK
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    
    # Überprüfen Sie, ob die Ausgabe `trained_model` vom Pipeline-Job verfügbar ist
    print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)
    
    # Konstruieren Sie einen Pfad zum trainierten Modell, indem Sie einen String mit dem Namen des Pipeline-Jobs und dem Namen der Ausgabe ("trained_model") formatieren
    model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
        pipeline_job.name, "trained_model"
    )
    
    # Definieren Sie einen Namen für das feinabgestimmte Modell, indem Sie "-ultrachat-200k" an den ursprünglichen Modellnamen anhängen und alle Schrägstriche durch Bindestriche ersetzen
    finetuned_model_name = model_name + "-ultrachat-200k"
    finetuned_model_name = finetuned_model_name.replace("/", "-")
    
    print("path to register model: ", model_path_from_job)
    
    # Bereiten Sie die Registrierung des Modells vor, indem Sie ein Model-Objekt mit verschiedenen Parametern erstellen
    # Diese umfassen den Pfad zum Modell, den Typ des Modells (MLflow-Modell), den Namen und die Version des Modells sowie eine Beschreibung des Modells
    prepare_to_register_model = Model(
        path=model_path_from_job,
        type=AssetTypes.MLFLOW_MODEL,
        name=finetuned_model_name,
        version=timestamp,  # Verwenden Sie den Zeitstempel als Version, um Versionskonflikte zu vermeiden
        description=model_name + " fine tuned model for ultrachat 200k chat-completion",
    )
    
    print("prepare to register model: \n", prepare_to_register_model)
    
    # Registrieren Sie das Modell, indem Sie die Methode create_or_update des models-Objekts im workspace_ml_client mit dem Model-Objekt als Argument aufrufen
    registered_model = workspace_ml_client.models.create_or_update(
        prepare_to_register_model
    )
    
    # Geben Sie das registrierte Modell aus
    print("registered model: \n", registered_model)
    ```

## 7. Deployment des feinabgestimmten Modells zu einem Online-Endpunkt

Online-Endpunkte bieten eine dauerhafte REST-API, die zur Integration mit Anwendungen verwendet werden kann, die das Modell nutzen müssen.

### Endpoint verwalten

1. Dieses Python-Skript erstellt einen verwalteten Online-Endpunkt in Azure Machine Learning für ein registriertes Modell. Hier eine Übersicht dessen, was es macht:

    - Es importiert notwendige Module aus dem Azure AI ML SDK.

    - Es definiert einen eindeutigen Namen für den Online-Endpunkt, indem es einen Zeitstempel an den String "ultrachat-completion-" anhängt.

    - Es bereitet die Erstellung des Online-Endpunkts vor, indem es ein ManagedOnlineEndpoint-Objekt mit verschiedenen Parametern erstellt, darunter den Namen des Endpunkts, eine Beschreibung des Endpunkts und den Authentifizierungsmodus ("key").

    - Es erstellt den Online-Endpunkt, indem es die Methode begin_create_or_update des workspace_ml_client mit dem ManagedOnlineEndpoint-Objekt als Argument aufruft und anschließend mit wait auf den Abschluss der Erstellung wartet.

1. Zusammengefasst erstellt dieses Skript einen verwalteten Online-Endpunkt in Azure Machine Learning für ein registriertes Modell.

    ```python
    # Importieren Sie notwendige Module aus dem Azure AI ML SDK
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        ProbeSettings,
        OnlineRequestSettings,
    )
    
    # Definieren Sie einen eindeutigen Namen für den Online-Endpunkt, indem Sie einen Zeitstempel an den String "ultrachat-completion-" anhängen
    online_endpoint_name = "ultrachat-completion-" + timestamp
    
    # Bereiten Sie die Erstellung des Online-Endpunkts vor, indem Sie ein ManagedOnlineEndpoint-Objekt mit verschiedenen Parametern erstellen
    # Diese umfassen den Namen des Endpunkts, eine Beschreibung des Endpunkts und den Authentifizierungsmodus ("key")
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="Online endpoint for "
        + registered_model.name
        + ", fine tuned model for ultrachat-200k-chat-completion",
        auth_mode="key",
    )
    
    # Erstellen Sie den Online-Endpunkt, indem Sie die Methode begin_create_or_update des workspace_ml_client mit dem ManagedOnlineEndpoint-Objekt als Argument aufrufen
    # Warten Sie dann auf den Abschluss des Erstellungsvorgangs, indem Sie die Methode wait aufrufen
    workspace_ml_client.begin_create_or_update(endpoint).wait()
    ```

> [!NOTE]
> Hier finden Sie die Liste der für das Deployment unterstützten SKUs – [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Deployment des ML-Modells

1. Dieses Python-Skript deployed ein registriertes Machine-Learning-Modell zu einem verwalteten Online-Endpunkt in Azure Machine Learning. Hier eine Übersicht dessen, was es macht:

    - Es importiert das Modul ast, welches Funktionen zur Verarbeitung von Bäumen der Python-Abstraktsyntaxgrammatik bereitstellt.

    - Es legt den Instanztyp für das Deployment auf "Standard_NC6s_v3" fest.

    - Es prüft, ob im Foundation Model das Tag inference_compute_allow_list vorhanden ist. Falls ja, wird der Wert des Tags von einem String in eine Python-Liste konvertiert und inference_computes_allow_list zugewiesen. Falls nicht, wird inference_computes_allow_list auf None gesetzt.

    - Es überprüft, ob der angegebene Instanztyp in der Allow-Liste enthalten ist. Falls nicht, wird eine Nachricht ausgegeben, die den Benutzer bittet, einen Instanztyp aus der Allow-Liste auszuwählen.

    - Es bereitet die Erstellung des Deployments vor, indem es ein ManagedOnlineDeployment-Objekt mit verschiedenen Parametern erstellt, darunter der Name des Deployments, der Name des Endpunkts, die ID des Modells, Instanztyp und Anzahl, die Einstellungen für den Liveness Probe und die Anforderungseinstellungen.

    - Es erstellt das Deployment, indem es die Methode begin_create_or_update des workspace_ml_client mit dem ManagedOnlineDeployment-Objekt als Argument aufruft und anschließend mit wait auf den Abschluss wartet.

    - Es setzt den Traffic des Endpunkts so, dass 100 % des Traffics auf das "demo"-Deployment geleitet werden.

    - Es aktualisiert den Endpunkt, indem es die Methode begin_create_or_update des workspace_ml_client mit dem Endpunktobjekt als Argument aufruft und anschließend mit result auf den Abschluss der Aktualisierung wartet.

1. Zusammengefasst deployed dieses Skript ein registriertes Machine-Learning-Modell zu einem verwalteten Online-Endpunkt in Azure Machine Learning.

    ```python
    # Importieren Sie das ast-Modul, das Funktionen zur Verarbeitung von Bäumen der abstrakten Syntaxgrammatik von Python bereitstellt
    import ast
    
    # Legen Sie den Instanztyp für die Bereitstellung fest
    instance_type = "Standard_NC6s_v3"
    
    # Überprüfen Sie, ob das Tag `inference_compute_allow_list` im Foundation-Modell vorhanden ist
    if "inference_compute_allow_list" in foundation_model.tags:
        # Falls ja, wandeln Sie den Tag-Wert von einem String in eine Python-Liste um und weisen Sie ihn `inference_computes_allow_list` zu
        inference_computes_allow_list = ast.literal_eval(
            foundation_model.tags["inference_compute_allow_list"]
        )
        print(f"Please create a compute from the above list - {computes_allow_list}")
    else:
        # Falls nicht, setzen Sie `inference_computes_allow_list` auf `None`
        inference_computes_allow_list = None
        print("`inference_compute_allow_list` is not part of model tags")
    
    # Überprüfen Sie, ob der angegebene Instanztyp in der Erlaubnisliste enthalten ist
    if (
        inference_computes_allow_list is not None
        and instance_type not in inference_computes_allow_list
    ):
        print(
            f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
        )
    
    # Bereiten Sie die Erstellung der Bereitstellung vor, indem Sie ein `ManagedOnlineDeployment`-Objekt mit verschiedenen Parametern erstellen
    demo_deployment = ManagedOnlineDeployment(
        name="demo",
        endpoint_name=online_endpoint_name,
        model=registered_model.id,
        instance_type=instance_type,
        instance_count=1,
        liveness_probe=ProbeSettings(initial_delay=600),
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )
    
    # Erstellen Sie die Bereitstellung, indem Sie die Methode `begin_create_or_update` des `workspace_ml_client` mit dem `ManagedOnlineDeployment`-Objekt als Argument aufrufen
    # Warten Sie dann auf den Abschluss des Erstellungsvorgangs, indem Sie die Methode `wait` aufrufen
    workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()
    
    # Setzen Sie den Datenverkehr des Endpunkts so, dass 100 % des Datenverkehrs an die „demo“-Bereitstellung geleitet werden
    endpoint.traffic = {"demo": 100}
    
    # Aktualisieren Sie den Endpunkt, indem Sie die Methode `begin_create_or_update` des `workspace_ml_client` mit dem `endpoint`-Objekt als Argument aufrufen
    # Warten Sie dann auf den Abschluss des Aktualisierungsvorgangs, indem Sie die Methode `result` aufrufen
    workspace_ml_client.begin_create_or_update(endpoint).result()
    ```

## 8. Testen des Endpunkts mit Beispieldaten

Wir werden einige Beispieldaten aus dem Test-Datensatz abrufen und an den Online-Endpunkt zur Inferenz senden. Anschließend zeigen wir die vorhergesagten Labels zusammen mit den Ground-Truth-Labels an.

### Ergebnisse lesen

1. Dieses Python-Skript liest eine JSON Lines-Datei in ein pandas DataFrame ein, nimmt eine Zufallsstichprobe und setzt den Index zurück. Hier eine Übersicht dessen, was es macht:

    - Es liest die Datei ./ultrachat_200k_dataset/test_gen.jsonl in ein pandas DataFrame ein. Die Funktion read_json wird mit dem Argument lines=True verwendet, weil die Datei im JSON Lines-Format vorliegt, bei dem jede Zeile ein separates JSON-Objekt ist.

    - Es nimmt eine Zufallsstichprobe von 1 Zeile aus dem DataFrame. Die Funktion sample wird mit dem Argument n=1 verwendet, um die Anzahl der zufällig auszuwählenden Zeilen zu spezifizieren.

    - Es setzt den Index des DataFrames zurück. Die Funktion reset_index wird mit dem Argument drop=True verwendet, um den ursprünglichen Index zu verwerfen und ihn durch einen neuen Standard-Integer-Index zu ersetzen.

    - Es zeigt die ersten 2 Zeilen des DataFrames mit der Funktion head und dem Argument 2 an. Da das DataFrame nach der Stichprobe jedoch nur eine Zeile enthält, wird nur diese eine Zeile angezeigt.

1. Zusammengefasst liest dieses Skript eine JSON Lines-Datei in ein pandas DataFrame ein, nimmt eine Zufallsstichprobe von 1 Zeile, setzt den Index zurück und zeigt die erste Zeile an.
    
    ```python
    # Importiere die Pandas-Bibliothek
    import pandas as pd
    
    # Lese die JSON Lines Datei './ultrachat_200k_dataset/test_gen.jsonl' in ein Pandas DataFrame ein
    # Das Argument 'lines=True' zeigt an, dass die Datei im JSON Lines Format vorliegt, bei dem jede Zeile ein separates JSON-Objekt ist
    test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)
    
    # Ziehe eine zufällige Stichprobe von 1 Zeile aus dem DataFrame
    # Das Argument 'n=1' gibt die Anzahl der zufällig auszuwählenden Zeilen an
    test_df = test_df.sample(n=1)
    
    # Setze den Index des DataFrames zurück
    # Das Argument 'drop=True' zeigt an, dass der ursprüngliche Index verworfen und durch einen neuen Index mit Standard-Ganzzahlwerten ersetzt werden soll
    # Das Argument 'inplace=True' zeigt an, dass das DataFrame direkt verändert werden soll (ohne ein neues Objekt zu erstellen)
    test_df.reset_index(drop=True, inplace=True)
    
    # Zeige die ersten 2 Zeilen des DataFrames an
    # Da das DataFrame nach der Stichprobenziehung jedoch nur eine Zeile enthält, wird nur diese eine Zeile angezeigt
    test_df.head(2)
    ```

### Erstellen eines JSON-Objekts

1. Dieses Python-Skript erstellt ein JSON-Objekt mit bestimmten Parametern und speichert es in einer Datei. Hier eine Übersicht dessen, was es macht:

    - Es importiert das json-Modul, das Funktionen zum Arbeiten mit JSON-Daten bereitstellt.
    - Es erstellt ein Dictionary parameters mit Schlüsseln und Werten, die Parameter für ein Machine Learning Modell darstellen. Die Schlüssel sind "temperature", "top_p", "do_sample" und "max_new_tokens" mit den entsprechenden Werten 0,6, 0,9, True und 200.

    - Es erstellt ein weiteres Dictionary test_json mit zwei Schlüsseln: "input_data" und "params". Der Wert von "input_data" ist ein weiteres Dictionary mit den Schlüsseln "input_string" und "parameters". Der Wert von "input_string" ist eine Liste, die die erste Nachricht aus dem DataFrame test_df enthält. Der Wert von "parameters" ist das zuvor erstellte parameters Dictionary. Der Wert von "params" ist ein leeres Dictionary.

    - Es öffnet eine Datei namens sample_score.json
    
    ```python
    # Importieren Sie das json-Modul, das Funktionen zum Arbeiten mit JSON-Daten bereitstellt
    import json
    
    # Erstellen Sie ein Wörterbuch `parameters` mit Schlüsseln und Werten, die Parameter für ein Machine-Learning-Modell darstellen
    # Die Schlüssel sind "temperature", "top_p", "do_sample" und "max_new_tokens" und ihre entsprechenden Werte sind 0.6, 0.9, True und 200
    parameters = {
        "temperature": 0.6,
        "top_p": 0.9,
        "do_sample": True,
        "max_new_tokens": 200,
    }
    
    # Erstellen Sie ein weiteres Wörterbuch `test_json` mit zwei Schlüsseln: "input_data" und "params"
    # Der Wert von "input_data" ist ein weiteres Wörterbuch mit den Schlüsseln "input_string" und "parameters"
    # Der Wert von "input_string" ist eine Liste, die die erste Nachricht aus dem DataFrame `test_df` enthält
    # Der Wert von "parameters" ist das zuvor erstellte Wörterbuch `parameters`
    # Der Wert von "params" ist ein leeres Wörterbuch
    test_json = {
        "input_data": {
            "input_string": [test_df["messages"][0]],
            "parameters": parameters,
        },
        "params": {},
    }
    
    # Öffnen Sie eine Datei mit dem Namen `sample_score.json` im Verzeichnis `./ultrachat_200k_dataset` im Schreibmodus
    with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
        # Schreiben Sie das Wörterbuch `test_json` im JSON-Format mit der Funktion `json.dump` in die Datei
        json.dump(test_json, f)
    ```

### Aufrufen des Endpunkts

1. Dieses Python-Skript ruft einen Online-Endpunkt in Azure Machine Learning auf, um eine JSON-Datei zu bewerten. Hier ist eine Aufschlüsselung dessen, was es tut:

    - Es ruft die Methode invoke der Eigenschaft online_endpoints des Objekts workspace_ml_client auf. Diese Methode wird verwendet, um eine Anfrage an einen Online-Endpunkt zu senden und eine Antwort zu erhalten.

    - Es gibt den Namen des Endpunkts und der Bereitstellung über die Argumente endpoint_name und deployment_name an. In diesem Fall ist der Name des Endpunkts in der Variablen online_endpoint_name gespeichert und der Name der Bereitstellung ist "demo".

    - Es gibt den Pfad zur zu bewertenden JSON-Datei über das Argument request_file an. In diesem Fall ist die Datei ./ultrachat_200k_dataset/sample_score.json.

    - Es speichert die Antwort vom Endpunkt in der Variablen response.

    - Es gibt die rohe Antwort aus.

1. Zusammenfassend ruft dieses Skript einen Online-Endpunkt in Azure Machine Learning auf, um eine JSON-Datei zu bewerten, und gibt die Antwort aus.

    ```python
    # Rufen Sie den Online-Endpunkt in Azure Machine Learning auf, um die Datei `sample_score.json` zu bewerten
    # Die `invoke`-Methode der Eigenschaft `online_endpoints` des Objekts `workspace_ml_client` wird verwendet, um eine Anfrage an einen Online-Endpunkt zu senden und eine Antwort zu erhalten
    # Das Argument `endpoint_name` gibt den Namen des Endpunkts an, der in der Variablen `online_endpoint_name` gespeichert ist
    # Das Argument `deployment_name` gibt den Namen der Bereitstellung an, der "demo" lautet
    # Das Argument `request_file` gibt den Pfad zur zu bewertenden JSON-Datei an, der `./ultrachat_200k_dataset/sample_score.json` ist
    response = workspace_ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        deployment_name="demo",
        request_file="./ultrachat_200k_dataset/sample_score.json",
    )
    
    # Geben Sie die rohe Antwort des Endpunkts aus
    print("raw response: \n", response, "\n")
    ```

## 9. Löschen des Online-Endpunkts

1. Vergessen Sie nicht, den Online-Endpunkt zu löschen, sonst läuft der Abrechnungsmesser für die vom Endpunkt verwendete Rechenleistung weiter. Diese Python-Codezeile löscht einen Online-Endpunkt in Azure Machine Learning. Hier ist eine Aufschlüsselung dessen, was sie tut:

    - Es ruft die Methode begin_delete der Eigenschaft online_endpoints des workspace_ml_client Objekts auf. Diese Methode wird verwendet, um die Löschung eines Online-Endpunkts zu starten.

    - Es gibt den Namen des zu löschenden Endpunkts mit dem Argument name an. In diesem Fall ist der Endpunktname in der Variablen online_endpoint_name gespeichert.

    - Es ruft die Methode wait auf, um auf den Abschluss der Löschoperation zu warten. Dies ist eine blockierende Operation, das bedeutet, dass sie verhindert, dass das Skript fortfährt, bis die Löschung abgeschlossen ist.

    - Zusammenfassend startet diese Codezeile die Löschung eines Online-Endpunkts in Azure Machine Learning und wartet auf den Abschluss der Operation.

    ```python
    # Löschen Sie den Online-Endpunkt in Azure Machine Learning
    # Die `begin_delete`-Methode der Eigenschaft `online_endpoints` des Objekts `workspace_ml_client` wird verwendet, um die Löschung eines Online-Endpunkts zu starten
    # Das Argument `name` gibt den Namen des zu löschenden Endpunkts an, der in der Variablen `online_endpoint_name` gespeichert ist
    # Die Methode `wait` wird aufgerufen, um auf den Abschluss der Löschoperation zu warten. Dies ist eine blockierende Operation, was bedeutet, dass das Skript nicht fortgesetzt wird, bis die Löschung abgeschlossen ist
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, kann es bei automatischen Übersetzungen zu Fehlern oder Ungenauigkeiten kommen. Das Originaldokument in der Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->