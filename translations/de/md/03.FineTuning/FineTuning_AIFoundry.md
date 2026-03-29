# Feinabstimmung von Phi-3 mit Microsoft Foundry

Lassen Sie uns erkunden, wie man das Sprachmodell Phi-3 Mini von Microsoft mit Microsoft Foundry feinabstimmt. Die Feinabstimmung ermöglicht es Ihnen, Phi-3 Mini an spezifische Aufgaben anzupassen und es dadurch noch leistungsfähiger und kontextbewusster zu machen.

## Überlegungen

- **Fähigkeiten:** Welche Modelle sind feinabstimmbar? Was kann das Basismodell durch Feinabstimmung lernen?
- **Kosten:** Wie sieht das Preismodell für die Feinabstimmung aus?
- **Anpassbarkeit:** Wie stark kann ich das Basismodell modifizieren – und auf welche Weise?
- **Bequemlichkeit:** Wie erfolgt die Feinabstimmung tatsächlich – muss ich eigenen Code schreiben? Muss ich eigene Rechenkapazitäten bereitstellen?
- **Sicherheit:** Feinabgestimmte Modelle können Sicherheitsrisiken bergen – gibt es Schutzmechanismen, die vor unbeabsichtigten Schäden schützen?

![AIFoundry Models](../../../../translated_images/de/AIFoundryModels.0e1b16f7d0b09b73.webp)

## Vorbereitung für die Feinabstimmung

### Voraussetzungen

> [!NOTE]
> Für die Modelle der Phi-3-Familie ist das pay-as-you-go Angebot zur Feinabstimmung nur mit Hubs verfügbar, die in der Region **East US 2** erstellt wurden.

- Ein Azure-Abonnement. Falls Sie noch kein Azure-Abonnement haben, erstellen Sie ein [kostenpflichtiges Azure-Konto](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go), um zu starten.

- Ein [AI Foundry-Projekt](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Azure rollenbasierte Zugriffssteuerungen (Azure RBAC) werden verwendet, um Zugriff auf Operationen in Microsoft Foundry zu gewähren. Um die Schritte in diesem Artikel durchführen zu können, muss Ihr Benutzerkonto die __Azure AI Developer Rolle__ auf der Ressourcengruppe zugewiesen bekommen haben.

### Registrierung des Abonnementanbieters

Stellen Sie sicher, dass das Abonnement für den Ressourcenanbieter `Microsoft.Network` registriert ist.

1. Melden Sie sich im [Azure-Portal](https://portal.azure.com) an.
1. Wählen Sie im linken Menü **Abonnements** aus.
1. Wählen Sie das Abonnement aus, das Sie nutzen möchten.
1. Wählen Sie im linken Menü **KI-Projekteinstellungen** > **Ressourcenanbieter** aus.
1. Bestätigen Sie, dass **Microsoft.Network** in der Liste der Ressourcenanbieter enthalten ist. Falls nicht, fügen Sie es hinzu.

### Datenvorbereitung

Bereiten Sie Ihre Trainings- und Validierungsdaten vor, um Ihr Modell fein abzustimmen. Ihre Trainings- und Validierungsdatensätze bestehen aus Eingabe- und Ausgabe-Beispielen, wie das Modell arbeiten soll.

Stellen Sie sicher, dass alle Trainingsbeispiele das erwartete Inferenzformat haben. Um Modelle effektiv fein abzustimmen, sorgen Sie für einen ausgewogenen und vielfältigen Datensatz.

Dies beinhaltet das Aufrechterhalten von Datenbalance, das Einbeziehen verschiedener Szenarien und eine regelmäßige Verfeinerung der Trainingsdaten, um Realwelterwartungen widerzuspiegeln, was letztlich zu genaueren und ausgewogeneren Modellantworten führt.

Unterschiedliche Modelltypen erfordern unterschiedliche Formate der Trainingsdaten.

### Chat Completion

Die Trainings- und Validierungsdaten müssen als JSON Lines (JSONL) Dokument formatiert sein. Für `Phi-3-mini-128k-instruct` muss der Feinabstimmungs-Datensatz im Konversationsformat vorliegen, das von der API für Chat Completions verwendet wird.

### Beispiel-Dateiformat

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Der unterstützte Dateityp ist JSON Lines. Dateien werden im Standard-Datenspeicher hochgeladen und in Ihrem Projekt verfügbar gemacht.

## Feinabstimmung von Phi-3 mit Microsoft Foundry

Microsoft Foundry ermöglicht es Ihnen, große Sprachmodelle an Ihre persönlichen Datensätze anzupassen, indem ein Prozess namens Feinabstimmung verwendet wird. Die Feinabstimmung bietet erheblichen Mehrwert, indem sie Anpassungen und Optimierungen für spezifische Aufgaben und Anwendungen ermöglicht. Das führt zu verbesserter Leistung, Kosteneffizienz, geringerer Latenz und maßgeschneiderten Ergebnissen.

![Finetune AI Foundry](../../../../translated_images/de/AIFoundryfinetune.193aaddce48d553c.webp)

### Neues Projekt erstellen

1. Melden Sie sich bei [Microsoft Foundry](https://ai.azure.com) an.

1. Wählen Sie **+Neues Projekt** aus, um ein neues Projekt in Microsoft Foundry zu erstellen.

    ![FineTuneSelect](../../../../translated_images/de/select-new-project.cd31c0404088d7a3.webp)

1. Führen Sie folgende Aufgaben durch:

    - Projekt-**Hub-Name**. Er muss eindeutig sein.
    - Wählen Sie den **Hub**, der verwendet werden soll (erstellen Sie einen neuen, falls erforderlich).

    ![FineTuneSelect](../../../../translated_images/de/create-project.ca3b71298b90e420.webp)

1. Führen Sie folgende Schritte aus, um einen neuen Hub zu erstellen:

    - Geben Sie den **Hub-Namen** ein. Er muss eindeutig sein.
    - Wählen Sie Ihr Azure-**Abonnement**.
    - Wählen Sie die **Ressourcengruppe**, die genutzt werden soll (erstellen Sie ggf. eine neue).
    - Wählen Sie den **Standort** aus, den Sie verwenden möchten.
    - Wählen Sie die **Verbindungsoption Azure AI Services** aus (erstellen Sie ggf. eine neue Verbindung).
    - Wählen Sie bei **Verbindung Azure AI Search** die Option **Verbindung überspringen**.

    ![FineTuneSelect](../../../../translated_images/de/create-hub.49e53d235e80779e.webp)

1. Klicken Sie auf **Weiter**.
1. Wählen Sie **Projekt erstellen**.

### Datenvorbereitung

Sammeln oder erstellen Sie vor der Feinabstimmung einen Datensatz, der für Ihre Aufgabe relevant ist, z. B. Chat-Anweisungen, Frage-Antwort-Paare oder andere relevante Textdaten. Bereinigen und verarbeiten Sie die Daten vor, indem Sie Rauschen entfernen, fehlende Werte behandeln und den Text tokenisieren.

### Feinabstimmung von Phi-3-Modellen in Microsoft Foundry

> [!NOTE]
> Die Feinabstimmung von Phi-3-Modellen wird aktuell nur in Projekten unterstützt, die in East US 2 liegen.

1. Wählen Sie in der linken Seitenleiste **Modellkatalog**.

1. Geben Sie *phi-3* in die **Suchleiste** ein und wählen Sie das Phi-3-Modell aus, das Sie verwenden möchten.

    ![FineTuneSelect](../../../../translated_images/de/select-model.60ef2d4a6a3cec57.webp)

1. Wählen Sie **Feinabstimmung**.

    ![FineTuneSelect](../../../../translated_images/de/select-finetune.a976213b543dd9d8.webp)

1. Geben Sie den **Namen für das feinabgestimmte Modell** ein.

    ![FineTuneSelect](../../../../translated_images/de/finetune1.c2b39463f0d34148.webp)

1. Klicken Sie auf **Weiter**.

1. Führen Sie folgende Aufgaben aus:

    - Wählen Sie den **Aufgabentyp** **Chat Completion**.
    - Wählen Sie die **Trainingsdaten** aus, die Sie verwenden möchten. Diese können Sie über Microsoft Foundrys Daten oder Ihre lokale Umgebung hochladen.

    ![FineTuneSelect](../../../../translated_images/de/finetune2.43cb099b1a94442d.webp)

1. Klicken Sie auf **Weiter**.

1. Laden Sie die **Validierungsdaten** hoch, die Sie verwenden möchten, oder wählen Sie die Option **Automatische Aufteilung der Trainingsdaten**.

    ![FineTuneSelect](../../../../translated_images/de/finetune3.fd96121b67dcdd92.webp)

1. Klicken Sie auf **Weiter**.

1. Führen Sie folgende Aufgaben aus:

    - Wählen Sie den gewünschten **Multiplikator für die Batchgröße**.
    - Wählen Sie die **Lernrate**.
    - Wählen Sie die Anzahl der **Epochen**.

    ![FineTuneSelect](../../../../translated_images/de/finetune4.e18b80ffccb5834a.webp)

1. Wählen Sie **Absenden**, um den Feinabstimmungsprozess zu starten.

    ![FineTuneSelect](../../../../translated_images/de/select-submit.0a3802d581bac271.webp)

1. Sobald Ihr Modell feinabgestimmt ist, wird der Status als **Abgeschlossen** angezeigt, wie im Bild unten zu sehen. Nun können Sie das Modell bereitstellen und in Ihrer eigenen Anwendung, im Playground oder in Prompt Flow verwenden. Für weitere Informationen siehe [Wie man die Phi-3-Familie kleiner Sprachmodelle mit Microsoft Foundry bereitstellt](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/de/completed.4dc8d2357144cdef.webp)

> [!NOTE]
> Für detailliertere Informationen zur Feinabstimmung von Phi-3 besuchen Sie bitte [Fine-tune Phi-3 Modelle in Microsoft Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Aufräumen Ihrer feinabgestimmten Modelle

Sie können ein feinabgestimmtes Modell aus der Liste der feinabgestimmten Modelle in [Microsoft Foundry](https://ai.azure.com) oder auf der Modell-Detailseite löschen. Wählen Sie das zu löschende feinabgestimmte Modell auf der Feinabstimmungsseite aus und klicken Sie dann auf die Schaltfläche „Löschen“, um das Modell zu entfernen.

> [!NOTE]
> Sie können ein benutzerdefiniertes Modell nicht löschen, wenn es eine bestehende Bereitstellung hat. Sie müssen zuerst die Modellausführung löschen, bevor Sie Ihr benutzerdefiniertes Modell löschen können.

## Kosten und Kontingente

### Kosten- und Kontingentüberlegungen für als Dienst feinabgestimmte Phi-3-Modelle

Phi-Modelle, die als Dienst feinabgestimmt sind, werden von Microsoft angeboten und in Microsoft Foundry integriert. Die Preise finden Sie beim [Bereitstellen](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) oder Feinabstimmen der Modelle unter dem Tab "Preise und Bedingungen" im Bereitstellungsassistenten.

## Inhaltsfilterung

Modelle, die als Service mit pay-as-you-go bereitgestellt werden, sind durch Azure AI Content Safety geschützt. Bei Bereitstellung an Echtzeitendpunkten können Sie diese Funktion deaktivieren. Mit aktiviertem Azure AI Content Safety werden sowohl Prompt als auch Completion durch ein Ensemble von Klassifikationsmodellen geleitet, die darauf abzielen, die Ausgabe schädlicher Inhalte zu erkennen und zu verhindern. Das Inhaltsfiltersystem erkennt bestimmte Kategorien potenziell schädlicher Inhalte in Eingabeprompts und Ausgabekomplettierungen und ergreift entsprechende Maßnahmen. Erfahren Sie mehr über [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Feinabstimmungs-Konfiguration**

Hyperparameter: Definieren Sie Hyperparameter wie Lernrate, Batch-Größe und Anzahl der Trainingsdurchläufe.

**Verlustfunktion**

Wählen Sie eine passende Verlustfunktion für Ihre Aufgabe (z. B. Kreuzentropie).

**Optimierer**

Wählen Sie einen Optimierer (z. B. Adam) für die Gradienten-Updates während des Trainings.

**Feinabstimmungsprozess**

- Vorgefertigtes Modell laden: Laden Sie den Phi-3 Mini Checkpoint.
- Benutzerdefinierte Schichten hinzufügen: Fügen Sie aufgabenspezifische Schichten hinzu (z. B. Klassifikationskopf für Chat-Anweisungen).

**Modell trainieren**

Feinabstimmen des Modells mit Ihrem vorbereiteten Datensatz. Überwachen Sie den Trainingsverlauf und passen Sie Hyperparameter bei Bedarf an.

**Evaluation und Validierung**

Validierungsdatensatz: Teilen Sie Ihre Daten in Trainings- und Validierungsdatensätze.

**Leistung bewerten**

Verwenden Sie Metriken wie Genauigkeit, F1-Score oder Perplexität, um die Modellleistung zu beurteilen.

## Feinabgestimmtes Modell speichern

**Checkpoint**

Speichern Sie den Checkpoint des feinabgestimmten Modells für die zukünftige Nutzung.

## Bereitstellung

- Als Webdienst bereitstellen: Stellen Sie Ihr feinabgestimmtes Modell als Webdienst in Microsoft Foundry bereit.
- Endpunkt testen: Senden Sie Testanfragen an den bereitgestellten Endpunkt, um dessen Funktionalität zu überprüfen.

## Iterieren und verbessern

Iterieren: Wenn die Leistung nicht zufriedenstellend ist, passen Sie Hyperparameter an, fügen Sie weitere Daten hinzu oder führen Sie die Feinabstimmung für zusätzliche Epochen durch.

## Überwachen und verfeinern

Überwachen Sie kontinuierlich das Verhalten des Modells und verfeinern Sie es bei Bedarf.

## Anpassen und erweitern

Benutzerdefinierte Aufgaben: Phi-3 Mini kann für verschiedene Aufgaben über Chat-Anweisungen hinaus feinabgestimmt werden. Erkunden Sie weitere Anwendungsfälle!
Experimentieren: Probieren Sie unterschiedliche Architekturen, Schichtkombinationen und Techniken aus, um die Leistung zu verbessern.

> [!NOTE]
> Feinabstimmung ist ein iterativer Prozess. Experimentieren Sie, lernen Sie dazu und passen Sie Ihr Modell an, um die besten Ergebnisse für Ihre spezifische Aufgabe zu erzielen!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatische Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->