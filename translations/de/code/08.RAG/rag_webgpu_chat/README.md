<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-07T10:18:16+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "de"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo zur Präsentation von WebGPU und dem RAG-Muster
Das RAG-Muster mit dem Phi-3 Onnx Hosted Modell nutzt den Retrieval-Augmented Generation-Ansatz, der die Leistungsfähigkeit der Phi-3-Modelle mit ONNX-Hosting für effiziente KI-Einsätze kombiniert. Dieses Muster ist besonders nützlich für die Feinabstimmung von Modellen für domänenspezifische Aufgaben und bietet eine Kombination aus Qualität, Kosteneffizienz und Verständnis langer Kontexte. Es ist Teil der Azure AI Suite, die eine breite Auswahl an Modellen bereitstellt, die leicht zu finden, auszuprobieren und zu verwenden sind und den Anpassungsbedarf verschiedener Branchen abdecken. Die Phi-3-Modelle, einschließlich Phi-3-mini, Phi-3-small und Phi-3-medium, sind im Azure AI Model Catalog verfügbar und können selbstverwaltet oder über Plattformen wie HuggingFace und ONNX feinabgestimmt und bereitgestellt werden – ein Beleg für Microsofts Engagement für zugängliche und effiziente KI-Lösungen.

## Was ist WebGPU
WebGPU ist eine moderne Web-Grafik-API, die darauf ausgelegt ist, effizienten Zugriff auf die Grafikeinheit (GPU) eines Geräts direkt aus Webbrowsern zu ermöglichen. Sie soll WebGL ablösen und bietet dabei mehrere wichtige Verbesserungen:

1. **Kompatibilität mit modernen GPUs:** WebGPU ist so konzipiert, dass es nahtlos mit zeitgemäßen GPU-Architekturen zusammenarbeitet und System-APIs wie Vulkan, Metal und Direct3D 12 nutzt.
2. **Verbesserte Leistung:** Es unterstützt allgemeine GPU-Berechnungen und schnellere Abläufe, wodurch es sowohl für Grafik-Rendering als auch für Machine-Learning-Aufgaben geeignet ist.
3. **Erweiterte Funktionen:** WebGPU ermöglicht den Zugriff auf fortgeschrittenere GPU-Fähigkeiten, die komplexere und dynamischere Grafik- und Rechenlasten erlauben.
4. **Reduzierte JavaScript-Belastung:** Indem mehr Aufgaben an die GPU ausgelagert werden, verringert WebGPU die Last auf JavaScript erheblich, was zu besserer Leistung und flüssigeren Nutzererlebnissen führt.

WebGPU wird derzeit in Browsern wie Google Chrome unterstützt, und es wird daran gearbeitet, die Unterstützung auf weitere Plattformen auszuweiten.

### 03.WebGPU
Erforderliche Umgebung:

**Unterstützte Browser:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU aktivieren:

- In Chrome/Microsoft Edge 

Aktivieren Sie die `chrome://flags/#enable-unsafe-webgpu`-Flagge.

#### Öffnen Sie Ihren Browser:
Starten Sie Google Chrome oder Microsoft Edge.

#### Rufen Sie die Flags-Seite auf:
Geben Sie in der Adressleiste `chrome://flags` ein und drücken Sie Enter.

#### Suchen Sie die Flagge:
Geben Sie oben auf der Seite im Suchfeld 'enable-unsafe-webgpu' ein.

#### Aktivieren Sie die Flagge:
Suchen Sie in der Ergebnisliste die #enable-unsafe-webgpu-Flagge.

Klicken Sie auf das Dropdown-Menü daneben und wählen Sie Aktiviert.

#### Starten Sie Ihren Browser neu:

Nach dem Aktivieren der Flagge müssen Sie den Browser neu starten, damit die Änderungen wirksam werden. Klicken Sie auf die Schaltfläche „Neu starten“, die unten auf der Seite erscheint.

- Unter Linux starten Sie den Browser mit `--enable-features=Vulkan`.
- Safari 18 (macOS 15) hat WebGPU standardmäßig aktiviert.
- In Firefox Nightly geben Sie about:config in die Adressleiste ein und `set dom.webgpu.enabled to true`.

### GPU für Microsoft Edge einrichten

So richten Sie eine Hochleistungs-GPU für Microsoft Edge unter Windows ein:

- **Einstellungen öffnen:** Klicken Sie auf das Startmenü und wählen Sie Einstellungen.
- **Systemeinstellungen:** Gehen Sie zu System und dann Anzeige.
- **Grafikeinstellungen:** Scrollen Sie nach unten und klicken Sie auf Grafikeinstellungen.
- **App auswählen:** Unter „App zum Festlegen der Präferenz auswählen“ wählen Sie Desktop-App und dann Durchsuchen.
- **Edge auswählen:** Navigieren Sie zum Installationsordner von Edge (normalerweise `C:\Program Files (x86)\Microsoft\Edge\Application`) und wählen Sie `msedge.exe` aus.
- **Präferenz festlegen:** Klicken Sie auf Optionen, wählen Sie Hochleistung und klicken Sie dann auf Speichern.
Dies stellt sicher, dass Microsoft Edge Ihre Hochleistungs-GPU für bessere Leistung nutzt.
- **Starten Sie Ihren Rechner neu,** damit die Einstellungen wirksam werden.

### Öffnen Sie Ihren Codespace:
Navigieren Sie zu Ihrem Repository auf GitHub.
Klicken Sie auf die Schaltfläche Code und wählen Sie Open with Codespaces.

Wenn Sie noch keinen Codespace haben, können Sie einen erstellen, indem Sie auf New codespace klicken.

**Hinweis** Installation der Node-Umgebung in Ihrem Codespace
Das Ausführen einer npm-Demo aus einem GitHub Codespace ist eine hervorragende Möglichkeit, Ihr Projekt zu testen und zu entwickeln. Hier eine Schritt-für-Schritt-Anleitung, um loszulegen:

### Richten Sie Ihre Umgebung ein:
Sobald Ihr Codespace geöffnet ist, stellen Sie sicher, dass Node.js und npm installiert sind. Prüfen können Sie das mit:
```
node -v
```
```
npm -v
```

Falls diese nicht installiert sind, können Sie sie mit folgendem Befehl installieren:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navigieren Sie zu Ihrem Projektverzeichnis:
Verwenden Sie das Terminal, um in das Verzeichnis zu wechseln, in dem sich Ihr npm-Projekt befindet:
```
cd path/to/your/project
```

### Abhängigkeiten installieren:
Führen Sie den folgenden Befehl aus, um alle notwendigen Abhängigkeiten aus Ihrer package.json zu installieren:

```
npm install
```

### Demo ausführen:
Nachdem die Abhängigkeiten installiert sind, können Sie Ihr Demo-Skript starten. Dieses ist meist im Abschnitt scripts Ihrer package.json angegeben. Wenn Ihr Demo-Skript z. B. start heißt, führen Sie aus:

```
npm run build
```
```
npm run dev
```

### Demo aufrufen:
Falls Ihre Demo einen Webserver beinhaltet, stellt Codespaces eine URL zur Verfügung, über die Sie darauf zugreifen können. Achten Sie auf eine Benachrichtigung oder prüfen Sie den Ports-Tab, um die URL zu finden.

**Hinweis:** Das Modell muss im Browser zwischengespeichert werden, daher kann das Laden einige Zeit dauern.

### RAG Demo
Laden Sie die Markdown-Datei `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/` hoch.

### Datei auswählen:
Klicken Sie auf die Schaltfläche „Choose File“, um das Dokument auszuwählen, das Sie hochladen möchten.

### Dokument hochladen:
Nachdem Sie Ihre Datei ausgewählt haben, klicken Sie auf „Upload“, um Ihr Dokument für RAG (Retrieval-Augmented Generation) zu laden.

### Chat starten:
Sobald das Dokument hochgeladen ist, können Sie eine Chat-Sitzung starten, die auf dem Inhalt Ihres Dokuments basiert.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.