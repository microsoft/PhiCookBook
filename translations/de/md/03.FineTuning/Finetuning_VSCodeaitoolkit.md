<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c2bc0950f44919ac75a88c1a871680c2",
  "translation_date": "2025-07-17T09:00:22+00:00",
  "source_file": "md/03.FineTuning/Finetuning_VSCodeaitoolkit.md",
  "language_code": "de"
}
-->
## Willkommen beim AI Toolkit für VS Code

[AI Toolkit für VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) vereint verschiedene Modelle aus dem Azure AI Studio Catalog und anderen Katalogen wie Hugging Face. Das Toolkit vereinfacht die gängigen Entwicklungsschritte zum Erstellen von KI-Anwendungen mit generativen KI-Tools und Modellen durch:
- Einstieg mit Modellsuche und Playground.
- Modell-Feinabstimmung und Inferenz mit lokalen Rechenressourcen.
- Remote-Feinabstimmung und Inferenz mit Azure-Ressourcen.

[Installiere AI Toolkit für VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/de/Aitoolkit.7157953df04812dc.png)


**[Private Preview]** Ein-Klick-Bereitstellung für Azure Container Apps, um Modell-Feinabstimmung und Inferenz in der Cloud auszuführen.

Lass uns nun mit der Entwicklung deiner KI-Anwendung starten:

- [Willkommen beim AI Toolkit für VS Code](../../../../md/03.FineTuning)
- [Lokale Entwicklung](../../../../md/03.FineTuning)
  - [Vorbereitungen](../../../../md/03.FineTuning)
  - [Conda aktivieren](../../../../md/03.FineTuning)
  - [Nur Basis-Modell feinabstimmen](../../../../md/03.FineTuning)
  - [Modell-Feinabstimmung und Inferenz](../../../../md/03.FineTuning)
  - [Modell-Feinabstimmung](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [Beispiele und Ressourcen zur Feinabstimmung](../../../../md/03.FineTuning)
- [**\[Private Preview\]** Remote-Entwicklung](../../../../md/03.FineTuning)
  - [Voraussetzungen](../../../../md/03.FineTuning)
  - [Einrichten eines Remote-Entwicklungsprojekts](../../../../md/03.FineTuning)
  - [Azure-Ressourcen bereitstellen](../../../../md/03.FineTuning)
  - [\[Optional\] Huggingface-Token zum Azure Container App Secret hinzufügen](../../../../md/03.FineTuning)
  - [Feinabstimmung ausführen](../../../../md/03.FineTuning)
  - [Inference-Endpunkt bereitstellen](../../../../md/03.FineTuning)
  - [Inference-Endpunkt deployen](../../../../md/03.FineTuning)
  - [Erweiterte Nutzung](../../../../md/03.FineTuning)

## Lokale Entwicklung
### Vorbereitungen

1. Stelle sicher, dass der NVIDIA-Treiber auf dem Host installiert ist.  
2. Führe `huggingface-cli login` aus, falls du HF für die Datensatznutzung verwendest.  
3. Erläuterungen zu den `Olive`-Schlüsseleinstellungen für alles, was den Speicherverbrauch beeinflusst.

### Conda aktivieren
Da wir eine WSL-Umgebung verwenden, die geteilt wird, musst du die Conda-Umgebung manuell aktivieren. Nach diesem Schritt kannst du Feinabstimmung oder Inferenz ausführen.

```bash
conda activate [conda-env-name] 
```

### Nur Basis-Modell feinabstimmen
Um das Basismodell ohne Feinabstimmung auszuprobieren, kannst du diesen Befehl nach der Aktivierung von Conda ausführen.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### Modell-Feinabstimmung und Inferenz

Sobald der Arbeitsbereich in einem Dev-Container geöffnet ist, öffne ein Terminal (der Standardpfad ist das Projektverzeichnis) und führe den folgenden Befehl aus, um ein LLM auf dem ausgewählten Datensatz fein abzustimmen.

```bash
python finetuning/invoke_olive.py 
```

Checkpoints und das finale Modell werden im Ordner `models` gespeichert.

Führe anschließend die Inferenz mit dem feinabgestimmten Modell über Chats in einer `Konsole`, im `Webbrowser` oder mit `prompt flow` aus.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

Um `prompt flow` in VS Code zu verwenden, siehe bitte diese [Kurzanleitung](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

### Modell-Feinabstimmung

Lade als Nächstes das Modell herunter, das je nach Verfügbarkeit einer GPU auf deinem Gerät geeignet ist.

Um die lokale Feinabstimmungssitzung mit QLoRA zu starten, wähle ein Modell aus unserem Katalog aus, das du feinabstimmen möchtest.  
| Plattform(en) | GPU verfügbar | Modellname | Größe (GB) |
|---------|---------|--------|--------|
| Windows | Ja | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2,13GB |
| Linux | Ja | Phi-3-mini-4k-**cuda**-int4-onnx | 2,30GB |
| Windows<br>Linux | Nein | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2,72GB |

**_Hinweis_** Du benötigst kein Azure-Konto, um die Modelle herunterzuladen.

Das Phi3-mini (int4) Modell ist etwa 2GB bis 3GB groß. Je nach Netzwerkgeschwindigkeit kann der Download einige Minuten dauern.

Beginne mit der Auswahl eines Projektnamens und Speicherorts.  
Wähle anschließend ein Modell aus dem Modellkatalog aus. Du wirst aufgefordert, die Projektvorlage herunterzuladen. Danach kannst du auf „Projekt konfigurieren“ klicken, um verschiedene Einstellungen anzupassen.

### Microsoft Olive

Wir verwenden [Olive](https://microsoft.github.io/Olive/why-olive.html), um QLoRA-Feinabstimmung auf einem PyTorch-Modell aus unserem Katalog durchzuführen. Alle Einstellungen sind mit Standardwerten vorbelegt, um den Feinabstimmungsprozess lokal mit optimiertem Speicherverbrauch auszuführen, können aber an dein Szenario angepasst werden.

### Beispiele und Ressourcen zur Feinabstimmung

- [Einsteigerleitfaden zur Feinabstimmung](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [Feinabstimmung mit einem HuggingFace-Datensatz](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [Feinabstimmung mit einfachem Datensatz](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Private Preview]** Remote-Entwicklung

### Voraussetzungen

1. Um die Modell-Feinabstimmung in deiner Remote Azure Container App Umgebung auszuführen, stelle sicher, dass dein Abonnement über genügend GPU-Kapazität verfügt. Reiche ein [Support-Ticket](https://azure.microsoft.com/support/create-ticket/) ein, um die benötigte Kapazität für deine Anwendung anzufordern. [Weitere Infos zur GPU-Kapazität](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)  
2. Wenn du private Datensätze auf HuggingFace verwendest, stelle sicher, dass du ein [HuggingFace-Konto](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) hast und ein [Zugriffstoken generierst](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo)  
3. Aktiviere das Feature-Flag für Remote-Feinabstimmung und Inferenz im AI Toolkit für VS Code  
   1. Öffne die VS Code Einstellungen über *Datei -> Einstellungen -> Einstellungen*.  
   2. Navigiere zu *Erweiterungen* und wähle *AI Toolkit*.  
   3. Aktiviere die Option *"Enable Remote Fine-tuning And Inference"*.  
   4. Starte VS Code neu, damit die Änderung wirksam wird.

- [Remote-Feinabstimmung](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### Einrichten eines Remote-Entwicklungsprojekts
1. Führe die Befehlspalette `AI Toolkit: Focus on Resource View` aus.  
2. Navigiere zu *Model Fine-tuning*, um auf den Modellkatalog zuzugreifen. Vergib einen Projektnamen und wähle den Speicherort auf deinem Rechner aus. Klicke dann auf den Button *"Configure Project"*.  
3. Projektkonfiguration  
    1. Aktiviere nicht die Option *"Fine-tune locally"*.  
    2. Die Olive-Konfigurationseinstellungen werden mit voreingestellten Standardwerten angezeigt. Bitte passe diese Einstellungen nach Bedarf an.  
    3. Fahre mit *Generate Project* fort. Dieser Schritt nutzt WSL und richtet eine neue Conda-Umgebung ein, als Vorbereitung für zukünftige Updates mit Dev-Containern.  
4. Klicke auf *"Relaunch Window In Workspace"*, um dein Remote-Entwicklungsprojekt zu öffnen.

> **Hinweis:** Das Projekt funktioniert derzeit entweder lokal oder remote innerhalb des AI Toolkit für VS Code. Wenn du während der Projekterstellung *"Fine-tune locally"* auswählst, läuft es ausschließlich in WSL ohne Remote-Entwicklungsfunktionen. Wenn du *"Fine-tune locally"* nicht aktivierst, ist das Projekt auf die Remote Azure Container App Umgebung beschränkt.

### Azure-Ressourcen bereitstellen
Um zu starten, musst du die Azure-Ressource für die Remote-Feinabstimmung bereitstellen. Führe dazu den Befehl `AI Toolkit: Provision Azure Container Apps job for fine-tuning` aus der Befehlspalette aus.

Verfolge den Fortschritt der Bereitstellung über den Link, der im Ausgabefenster angezeigt wird.

### [Optional] Huggingface-Token zum Azure Container App Secret hinzufügen
Wenn du private HuggingFace-Datensätze verwendest, setze dein HuggingFace-Token als Umgebungsvariable, um die manuelle Anmeldung am Hugging Face Hub zu vermeiden.  
Das kannst du mit dem Befehl `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning` erledigen. Dabei kannst du den Geheimnisnamen als [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) festlegen und dein Hugging Face Token als Wert verwenden.

### Feinabstimmung ausführen
Um den Remote-Feinabstimmungsjob zu starten, führe den Befehl `AI Toolkit: Run fine-tuning` aus.

Um System- und Konsolenlogs einzusehen, kannst du das Azure-Portal über den Link im Ausgabefenster besuchen (weitere Schritte unter [Logs auf Azure anzeigen und abfragen](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). Alternativ kannst du die Konsolenlogs direkt im VSCode-Ausgabefenster anzeigen, indem du den Befehl `AI Toolkit: Show the running fine-tuning job streaming logs` ausführst.  
> **Hinweis:** Der Job kann aufgrund unzureichender Ressourcen in die Warteschlange gestellt werden. Wenn keine Logs angezeigt werden, führe den Befehl `AI Toolkit: Show the running fine-tuning job streaming logs` aus, warte kurz und führe ihn erneut aus, um die Streaming-Logs wieder zu verbinden.

Während dieses Prozesses wird QLoRA für die Feinabstimmung verwendet und erstellt LoRA-Adapter für das Modell, die während der Inferenz genutzt werden.  
Die Ergebnisse der Feinabstimmung werden in Azure Files gespeichert.

### Inference-Endpunkt bereitstellen
Nachdem die Adapter in der Remote-Umgebung trainiert wurden, kannst du mit einer einfachen Gradio-Anwendung mit dem Modell interagieren.  
Ähnlich wie bei der Feinabstimmung musst du die Azure-Ressourcen für die Remote-Inferenz einrichten, indem du den Befehl `AI Toolkit: Provision Azure Container Apps for inference` aus der Befehlspalette ausführst.

Standardmäßig sollten das Abonnement und die Ressourcengruppe für die Inferenz mit denen der Feinabstimmung übereinstimmen. Die Inferenz nutzt dieselbe Azure Container App Umgebung und greift auf das Modell sowie die Modelladapter zu, die in Azure Files gespeichert sind und während der Feinabstimmung erstellt wurden.

### Inference-Endpunkt deployen
Wenn du den Inferenzcode überarbeiten oder das Inferenzmodell neu laden möchtest, führe den Befehl `AI Toolkit: Deploy for inference` aus. Dadurch wird dein aktueller Code mit der Azure Container App synchronisiert und die Replik neu gestartet.

Nach erfolgreichem Deployment kannst du über den Button „*Go to Inference Endpoint*“ in der VSCode-Benachrichtigung auf die Inferenz-API zugreifen. Alternativ findest du den Web-API-Endpunkt unter `ACA_APP_ENDPOINT` in `./infra/inference.config.json` sowie im Ausgabefenster. Du bist nun bereit, das Modell über diesen Endpunkt zu evaluieren.

### Erweiterte Nutzung
Für weitere Informationen zur Remote-Entwicklung mit dem AI Toolkit siehe die Dokumentation zu [Modellen remote feinabstimmen](https://aka.ms/ai-toolkit/remote-provision) und [Inferenz mit dem feinabgestimmten Modell](https://aka.ms/ai-toolkit/remote-inference).

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.