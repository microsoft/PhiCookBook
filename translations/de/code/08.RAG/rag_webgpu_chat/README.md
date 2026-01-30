Phi-3-mini WebGPU RAG Chatbot

## Demo zur Präsentation von WebGPU und dem RAG-Muster  
Das RAG-Muster mit dem Phi-3 Onnx Hosted Modell nutzt den Retrieval-Augmented Generation-Ansatz und kombiniert die Leistungsfähigkeit der Phi-3-Modelle mit ONNX-Hosting für effiziente KI-Einsätze. Dieses Muster ist besonders hilfreich, um Modelle für domänenspezifische Aufgaben zu optimieren und bietet eine Kombination aus Qualität, Kosteneffizienz und Verständnis für lange Kontexte. Es ist Teil der Azure AI-Suite, die eine breite Auswahl an Modellen bereitstellt, die leicht zu finden, auszuprobieren und zu verwenden sind und die Anpassungsbedürfnisse verschiedener Branchen abdecken. Die Phi-3-Modelle, darunter Phi-3-mini, Phi-3-small und Phi-3-medium, sind im Azure AI Model Catalog verfügbar und können selbst verwaltet oder über Plattformen wie HuggingFace und ONNX feinjustiert und bereitgestellt werden – ein Beleg für Microsofts Engagement für zugängliche und effiziente KI-Lösungen.

## Was ist WebGPU  
WebGPU ist eine moderne Web-Grafik-API, die einen effizienten Zugriff auf die Grafikeinheit (GPU) eines Geräts direkt aus Webbrowsern ermöglicht. Sie soll der Nachfolger von WebGL sein und bietet mehrere wichtige Verbesserungen:

1. **Kompatibilität mit modernen GPUs:** WebGPU ist so konzipiert, dass es nahtlos mit zeitgemäßen GPU-Architekturen zusammenarbeitet und System-APIs wie Vulkan, Metal und Direct3D 12 nutzt.  
2. **Verbesserte Leistung:** Es unterstützt allgemeine GPU-Berechnungen und schnellere Abläufe, was es sowohl für Grafik-Rendering als auch für maschinelles Lernen geeignet macht.  
3. **Erweiterte Funktionen:** WebGPU bietet Zugriff auf fortgeschrittene GPU-Fähigkeiten, die komplexere und dynamischere Grafik- und Rechenlasten ermöglichen.  
4. **Reduzierte JavaScript-Belastung:** Durch die Auslagerung weiterer Aufgaben an die GPU verringert WebGPU die Belastung von JavaScript erheblich, was zu besserer Performance und flüssigeren Abläufen führt.

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

Aktivieren Sie die Flagge `chrome://flags/#enable-unsafe-webgpu`.

#### Browser öffnen:  
Starten Sie Google Chrome oder Microsoft Edge.

#### Flags-Seite aufrufen:  
Geben Sie in der Adressleiste `chrome://flags` ein und drücken Sie Enter.

#### Nach der Flagge suchen:  
Geben Sie im Suchfeld oben auf der Seite 'enable-unsafe-webgpu' ein.

#### Flagge aktivieren:  
Suchen Sie die Flagge #enable-unsafe-webgpu in der Ergebnisliste.

Klicken Sie auf das Dropdown-Menü daneben und wählen Sie Aktiviert.

#### Browser neu starten:  
Nach dem Aktivieren der Flagge müssen Sie den Browser neu starten, damit die Änderungen wirksam werden. Klicken Sie auf die Schaltfläche „Neu starten“, die unten auf der Seite erscheint.

- Unter Linux starten Sie den Browser mit `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) hat WebGPU standardmäßig aktiviert.  
- In Firefox Nightly geben Sie in der Adressleiste about:config ein und setzen `dom.webgpu.enabled` auf true.

### GPU für Microsoft Edge einrichten  

So richten Sie eine Hochleistungs-GPU für Microsoft Edge unter Windows ein:

- **Einstellungen öffnen:** Klicken Sie auf das Startmenü und wählen Sie Einstellungen.  
- **Systemeinstellungen:** Gehen Sie zu System und dann Anzeige.  
- **Grafikeinstellungen:** Scrollen Sie nach unten und klicken Sie auf Grafikeinstellungen.  
- **App auswählen:** Unter „App zur Festlegung der Präferenz auswählen“ wählen Sie Desktop-App und dann Durchsuchen.  
- **Edge auswählen:** Navigieren Sie zum Edge-Installationsordner (normalerweise `C:\Program Files (x86)\Microsoft\Edge\Application`) und wählen Sie `msedge.exe` aus.  
- **Präferenz festlegen:** Klicken Sie auf Optionen, wählen Sie Hochleistung und klicken Sie dann auf Speichern.  
Dies stellt sicher, dass Microsoft Edge Ihre Hochleistungs-GPU für bessere Leistung verwendet.  
- **Neustart** Ihres Rechners, damit die Einstellungen wirksam werden.

### Codespace öffnen:  
Navigieren Sie zu Ihrem Repository auf GitHub.  
Klicken Sie auf die Schaltfläche Code und wählen Sie Open with Codespaces.

Falls Sie noch keinen Codespace haben, können Sie einen erstellen, indem Sie auf New codespace klicken.

**Hinweis** Node-Umgebung in Ihrem Codespace installieren  
Ein npm-Demo aus einem GitHub Codespace auszuführen, ist eine großartige Möglichkeit, Ihr Projekt zu testen und zu entwickeln. Hier eine Schritt-für-Schritt-Anleitung, um loszulegen:

### Umgebung einrichten:  
Sobald Ihr Codespace geöffnet ist, stellen Sie sicher, dass Node.js und npm installiert sind. Überprüfen Sie dies mit:  
```
node -v
```  
```
npm -v
```

Falls sie nicht installiert sind, können Sie sie mit folgendem Befehl installieren:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Zum Projektverzeichnis navigieren:  
Verwenden Sie das Terminal, um in das Verzeichnis zu wechseln, in dem sich Ihr npm-Projekt befindet:  
```
cd path/to/your/project
```

### Abhängigkeiten installieren:  
Führen Sie den folgenden Befehl aus, um alle notwendigen Abhängigkeiten aus Ihrer package.json zu installieren:  

```
npm install
```

### Demo starten:  
Sobald die Abhängigkeiten installiert sind, können Sie Ihr Demo-Skript ausführen. Dieses ist normalerweise im Abschnitt scripts Ihrer package.json definiert. Wenn Ihr Demo-Skript z. B. start heißt, führen Sie aus:  

```
npm run build
```  
```
npm run dev
```

### Demo aufrufen:  
Wenn Ihre Demo einen Webserver beinhaltet, stellt Codespaces eine URL zur Verfügung, über die Sie darauf zugreifen können. Achten Sie auf eine Benachrichtigung oder prüfen Sie den Ports-Tab, um die URL zu finden.

**Hinweis:** Das Modell muss im Browser zwischengespeichert werden, daher kann das Laden einige Zeit in Anspruch nehmen.

### RAG Demo  
Laden Sie die Markdown-Datei `intro_rag.md` hoch, um die RAG-Lösung abzuschließen. Wenn Sie Codespaces verwenden, können Sie die Datei im Verzeichnis `01.InferencePhi3/docs/` herunterladen.

### Datei auswählen:  
Klicken Sie auf die Schaltfläche „Choose File“, um das Dokument auszuwählen, das Sie hochladen möchten.

### Dokument hochladen:  
Nachdem Sie Ihre Datei ausgewählt haben, klicken Sie auf „Upload“, um Ihr Dokument für RAG (Retrieval-Augmented Generation) zu laden.

### Chat starten:  
Sobald das Dokument hochgeladen ist, können Sie eine Chat-Sitzung mit RAG starten, die auf dem Inhalt Ihres Dokuments basiert.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.