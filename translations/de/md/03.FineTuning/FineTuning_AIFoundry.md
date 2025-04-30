<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c1559c5af6caccf6f623fd43a6b3a9a3",
  "translation_date": "2025-03-27T13:40:44+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_AIFoundry.md",
  "language_code": "de"
}
-->
# Feinabstimmung von Phi-3 mit Azure AI Foundry

Lassen Sie uns untersuchen, wie Microsofts Phi-3 Mini-Sprachmodell mit Azure AI Foundry feinabgestimmt werden kann. Feinabstimmung ermöglicht es Ihnen, Phi-3 Mini an spezifische Aufgaben anzupassen und es noch leistungsfähiger und kontextbewusster zu machen.

## Überlegungen

- **Fähigkeiten:** Welche Modelle können feinabgestimmt werden? Was kann das Basismodell nach der Feinabstimmung leisten?
- **Kosten:** Wie sieht das Preismodell für die Feinabstimmung aus?
- **Anpassbarkeit:** Wie stark kann ich das Basismodell modifizieren – und in welcher Weise?
- **Benutzerfreundlichkeit:** Wie läuft die Feinabstimmung ab – muss ich benutzerdefinierten Code schreiben? Muss ich eigene Rechenressourcen bereitstellen?
- **Sicherheit:** Feinabgestimmte Modelle können Sicherheitsrisiken bergen – gibt es Schutzmaßnahmen, um unbeabsichtigten Schaden zu vermeiden?

![AIFoundry-Modelle](../../../../translated_images/AIFoundryModels.4440430c9f07dbd6c625971422e7b9a5b9cb91fa046e447ba9ea41457860532f.de.png)

## Vorbereitung auf die Feinabstimmung

### Voraussetzungen

> [!NOTE]
> Für Modelle der Phi-3-Familie ist das Pay-as-you-go-Modell für die Feinabstimmung nur in Hubs verfügbar, die in den Regionen **East US 2** erstellt wurden.

- Ein Azure-Abonnement. Wenn Sie noch kein Azure-Abonnement haben, erstellen Sie ein [kostenpflichtiges Azure-Konto](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go), um loszulegen.

- Ein [AI Foundry-Projekt](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo).
- Azure-Rollenbasierte Zugriffssteuerungen (Azure RBAC) werden verwendet, um Zugriff auf Vorgänge in Azure AI Foundry zu gewähren. Um die Schritte in diesem Artikel auszuführen, muss Ihrem Benutzerkonto die Rolle __Azure AI Developer__ für die Ressourcengruppe zugewiesen sein.

### Registrierung des Abonnementanbieters

Überprüfen Sie, ob das Abonnement beim Ressourcenanbieter `Microsoft.Network` registriert ist.

1. Melden Sie sich im [Azure-Portal](https://portal.azure.com) an.
1. Wählen Sie **Abonnements** aus dem linken Menü.
1. Wählen Sie das Abonnement, das Sie verwenden möchten.
1. Wählen Sie **AI-Projekteinstellungen** > **Ressourcenanbieter** aus dem linken Menü.
1. Stellen Sie sicher, dass **Microsoft.Network** in der Liste der Ressourcenanbieter aufgeführt ist. Falls nicht, fügen Sie es hinzu.

### Datenvorbereitung

Bereiten Sie Ihre Trainings- und Validierungsdaten vor, um Ihr Modell feinabzustimmen. Ihre Trainings- und Validierungsdatensätze bestehen aus Eingabe- und Ausgabebeispielen, die zeigen, wie das Modell funktionieren soll.

Stellen Sie sicher, dass alle Ihre Trainingsbeispiele dem erwarteten Format für Inferenz entsprechen. Um Modelle effektiv feinabzustimmen, sorgen Sie für einen ausgewogenen und vielfältigen Datensatz.

Dies umfasst die Sicherstellung eines Daten-Gleichgewichts, die Einbeziehung verschiedener Szenarien und die regelmäßige Verfeinerung der Trainingsdaten, um sie an realistische Erwartungen anzupassen. Dadurch werden letztendlich genauere und ausgewogenere Modellantworten erzielt.

Verschiedene Modelltypen erfordern ein unterschiedliches Format der Trainingsdaten.

### Chat Completion

Die von Ihnen verwendeten Trainings- und Validierungsdaten **müssen** als JSON Lines (JSONL)-Dokument formatiert sein. Für `Phi-3-mini-128k-instruct` muss der Feinabstimmungsdatensatz im Konversationsformat vorliegen, das von der Chat Completions API verwendet wird.

### Beispiel-Dateiformat

```json
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Can I play PC games on my Xbox?"}, {"role": "assistant", "content": "While Xbox consoles don't natively support PC games, they can play an array of Xbox games, many of which are also available on PC. Can I assist you with finding games compatible with your Xbox device?"}]}
    {"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "I'm having trouble connecting my Xbox to the Wi-Fi."}, {"role": "assistant", "content": "No worries, let's go through the network settings on your Xbox. Can you please tell me what happens when you try to connect it to the Wi-Fi?"}]}
```

Der unterstützte Dateityp ist JSON Lines. Dateien werden in den Standard-Datenspeicher hochgeladen und in Ihrem Projekt verfügbar gemacht.

## Feinabstimmung von Phi-3 mit Azure AI Foundry

Azure AI Foundry ermöglicht es Ihnen, große Sprachmodelle mit Ihren eigenen Datensätzen anzupassen, indem Sie einen Prozess namens Feinabstimmung verwenden. Feinabstimmung bietet erheblichen Mehrwert, indem sie Anpassung und Optimierung für spezifische Aufgaben und Anwendungen ermöglicht. Dies führt zu verbesserter Leistung, Kosteneffizienz, reduzierter Latenz und maßgeschneiderten Ausgaben.

![Feinabstimmung AI Foundry](../../../../translated_images/AIFoundryfinetune.69ddc22d1ab08167a7e53a911cd33c749d99fea4047801a836ceb6eec66c5719.de.png)

### Ein neues Projekt erstellen

1. Melden Sie sich bei [Azure AI Foundry](https://ai.azure.com) an.

1. Wählen Sie **+Neues Projekt**, um ein neues Projekt in Azure AI Foundry zu erstellen.

    ![FineTuneSelect](../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.de.png)

1. Führen Sie die folgenden Aufgaben aus:

    - Projekt **Hub-Name**. Dieser muss eindeutig sein.
    - Wählen Sie den **Hub**, den Sie verwenden möchten (erstellen Sie bei Bedarf einen neuen).

    ![FineTuneSelect](../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.de.png)

1. Führen Sie die folgenden Aufgaben aus, um einen neuen Hub zu erstellen:

    - Geben Sie den **Hub-Namen** ein. Dieser muss eindeutig sein.
    - Wählen Sie Ihr Azure-**Abonnement**.
    - Wählen Sie die **Ressourcengruppe**, die Sie verwenden möchten (erstellen Sie bei Bedarf eine neue).
    - Wählen Sie den **Standort**, den Sie verwenden möchten.
    - Wählen Sie die **Azure AI Services verbinden**, die Sie verwenden möchten (erstellen Sie bei Bedarf eine neue).
    - Wählen Sie **Azure AI Search verbinden**, um **Überspringen** auszuwählen.

    ![FineTuneSelect](../../../../translated_images/create-hub.b93d390a6d3eebd4c33eb7e4ea6ef41fd69c4d39f21339d4bda51af9ed70505f.de.png)

1. Wählen Sie **Weiter**.
1. Wählen Sie **Projekt erstellen**.

### Datenvorbereitung

Bevor Sie mit der Feinabstimmung beginnen, sammeln oder erstellen Sie einen Datensatz, der für Ihre Aufgabe relevant ist, z. B. Chat-Anweisungen, Frage-Antwort-Paare oder andere relevante Textdaten. Bereinigen und bereiten Sie diese Daten vor, indem Sie Rauschen entfernen, fehlende Werte behandeln und den Text tokenisieren.

### Feinabstimmung von Phi-3-Modellen in Azure AI Foundry

> [!NOTE]
> Die Feinabstimmung von Phi-3-Modellen wird derzeit nur in Projekten unterstützt, die in East US 2 angesiedelt sind.

1. Wählen Sie **Modellkatalog** aus der linken Seitenleiste.

1. Geben Sie *phi-3* in die **Suchleiste** ein und wählen Sie das gewünschte Phi-3-Modell aus.

    ![FineTuneSelect](../../../../translated_images/select-model.02eef2cbb5b7e61a86526b05bd5ec9822fd6b2abae4e38fd5d9bdef541dfb967.de.png)

1. Wählen Sie **Feinabstimmen**.

    ![FineTuneSelect](../../../../translated_images/select-finetune.88cf562034f78baf0b7f41511fd4c45e1f068104238f1397661b9402ff9e2e09.de.png)

1. Geben Sie den **Namen des feinabgestimmten Modells** ein.

    ![FineTuneSelect](../../../../translated_images/finetune1.8a20c66f797cc7ede7feb789a45c42713b7aeadfeb01dbc34446019db5c189d4.de.png)

1. Wählen Sie **Weiter**.

1. Führen Sie die folgenden Aufgaben aus:

    - Wählen Sie den **Aufgabentyp** **Chat Completion**.
    - Wählen Sie die **Trainingsdaten**, die Sie verwenden möchten. Sie können diese über Azure AI Foundry hochladen oder aus Ihrer lokalen Umgebung auswählen.

    ![FineTuneSelect](../../../../translated_images/finetune2.47df1aa177096dbaa01e4d64a06eb3f46a29718817fa706167af3ea01419a32f.de.png)

1. Wählen Sie **Weiter**.

1. Laden Sie die **Validierungsdaten** hoch, die Sie verwenden möchten, oder wählen Sie **Automatische Aufteilung der Trainingsdaten**.

    ![FineTuneSelect](../../../../translated_images/finetune3.e887e47240626c31f969532610c965594635c91cf3f94639fa60fb5d2bbd8f93.de.png)

1. Wählen Sie **Weiter**.

1. Führen Sie die folgenden Aufgaben aus:

    - Wählen Sie den **Batch-Größen-Multiplikator**, den Sie verwenden möchten.
    - Wählen Sie die **Lernrate**, die Sie verwenden möchten.
    - Wählen Sie die **Epochen**, die Sie verwenden möchten.

    ![FineTuneSelect](../../../../translated_images/finetune4.9f47c2fad66fddd0f091b62a2fa6ac23260226ab841287805d843ebc83761801.de.png)

1. Wählen Sie **Einreichen**, um den Feinabstimmungsprozess zu starten.

    ![FineTuneSelect](../../../../translated_images/select-submit.b5344fd77e49bfb6d4efe72e713f6a46f04323d871c118bbf59bf0217698dfee.de.png)

1. Sobald Ihr Modell feinabgestimmt ist, wird der Status als **Abgeschlossen** angezeigt, wie im Bild unten dargestellt. Jetzt können Sie das Modell bereitstellen und in Ihrer eigenen Anwendung, im Playground oder im Prompt Flow verwenden. Weitere Informationen finden Sie unter [Bereitstellung von Phi-3-Modellen mit Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python).

    ![FineTuneSelect](../../../../translated_images/completed.f4be2c6e660d8ba908d1d23e2102925cc31e57cbcd60fb10e7ad3b7925f585c4.de.png)

> [!NOTE]
> Weitere detaillierte Informationen zur Feinabstimmung von Phi-3 finden Sie unter [Feinabstimmung von Phi-3-Modellen in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/fine-tune-phi-3?tabs=phi-3-mini).

## Bereinigung Ihrer feinabgestimmten Modelle

Sie können ein feinabgestimmtes Modell aus der Liste der Feinabstimmungsmodelle in [Azure AI Foundry](https://ai.azure.com) oder von der Modell-Detailseite löschen. Wählen Sie das feinabgestimmte Modell aus, das Sie löschen möchten, und klicken Sie dann auf die Schaltfläche Löschen.

> [!NOTE]
> Sie können ein benutzerdefiniertes Modell nicht löschen, wenn es über eine bestehende Bereitstellung verfügt. Sie müssen zuerst die Bereitstellung des Modells löschen, bevor Sie das benutzerdefinierte Modell löschen können.

## Kosten und Kontingente

### Kosten- und Kontingentüberlegungen für die Feinabstimmung von Phi-3-Modellen

Phi-Modelle, die als Service feinabgestimmt werden, werden von Microsoft angeboten und sind in Azure AI Foundry integriert. Die Preise finden Sie beim [Bereitstellen](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?tabs=phi-3-5&pivots=programming-language-python) oder Feinabstimmen der Modelle unter dem Tab „Preise und Bedingungen“ im Bereitstellungsassistenten.

## Inhaltsfilterung

Modelle, die als Service mit Pay-as-you-go bereitgestellt werden, sind durch Azure AI Content Safety geschützt. Bei der Bereitstellung für Echtzeit-Endpunkte können Sie diese Funktion deaktivieren. Mit aktiviertem Azure AI Content Safety durchlaufen sowohl die Eingabeaufforderung als auch die Ausgabe eine Reihe von Klassifikationsmodellen, die darauf abzielen, schädliche Inhalte zu erkennen und zu verhindern. Das Inhaltsfiltersystem erkennt und ergreift Maßnahmen bei bestimmten Kategorien potenziell schädlicher Inhalte in Eingabeaufforderungen und Ausgaben. Weitere Informationen finden Sie unter [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-studio/concepts/content-filtering).

**Konfiguration der Feinabstimmung**

Hyperparameter: Definieren Sie Hyperparameter wie Lernrate, Batch-Größe und Anzahl der Trainingsepochen.

**Verlustfunktion**

Wählen Sie eine geeignete Verlustfunktion für Ihre Aufgabe (z. B. Kreuzentropie).

**Optimierer**

Wählen Sie einen Optimierer (z. B. Adam) für die Gradientenaktualisierungen während des Trainings.

**Feinabstimmungsprozess**

- Vortrainiertes Modell laden: Laden Sie den Phi-3 Mini-Checkpoint.
- Benutzerdefinierte Schichten hinzufügen: Fügen Sie aufgabenspezifische Schichten hinzu (z. B. Klassifikationskopf für Chat-Anweisungen).

**Modell trainieren**
Feinabstimmen des Modells mit Ihrem vorbereiteten Datensatz. Überwachen Sie den Trainingsfortschritt und passen Sie die Hyperparameter bei Bedarf an.

**Evaluation und Validierung**

Validierungssatz: Teilen Sie Ihre Daten in Trainings- und Validierungssätze auf.

**Leistung bewerten**

Verwenden Sie Metriken wie Genauigkeit, F1-Score oder Perplexität, um die Modellleistung zu bewerten.

## Feinabgestimmtes Modell speichern

**Checkpoint**
Speichern Sie den Checkpoint des feinabgestimmten Modells für die zukünftige Nutzung.

## Bereitstellung

- Als Webdienst bereitstellen: Stellen Sie Ihr feinabgestimmtes Modell als Webdienst in Azure AI Foundry bereit.
- Endpunkt testen: Senden Sie Testanfragen an den bereitgestellten Endpunkt, um dessen Funktionalität zu überprüfen.

## Iterieren und verbessern

Iterieren: Wenn die Leistung nicht zufriedenstellend ist, iterieren Sie, indem Sie Hyperparameter anpassen, mehr Daten hinzufügen oder das Modell über zusätzliche Epochen feinabstimmen.

## Überwachen und verfeinern

Überwachen Sie kontinuierlich das Verhalten des Modells und nehmen Sie bei Bedarf Anpassungen vor.

## Anpassen und erweitern

Benutzerdefinierte Aufgaben: Phi-3 Mini kann für verschiedene Aufgaben über Chat-Anweisungen hinaus feinabgestimmt werden. Erkunden Sie weitere Anwendungsfälle!
Experimentieren: Probieren Sie unterschiedliche Architekturen, Schichtkombinationen und Techniken aus, um die Leistung zu verbessern.

> [!NOTE]
> Feinabstimmung ist ein iterativer Prozess. Experimentieren Sie, lernen Sie und passen Sie Ihr Modell an, um die besten Ergebnisse für Ihre spezifische Aufgabe zu erzielen!

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.