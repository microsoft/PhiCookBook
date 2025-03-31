<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-03-27T04:48:57+00:00",
  "source_file": "code\\08.RAG\\rag_webgpu_chat\\README.md",
  "language_code": "de"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo zur Präsentation von WebGPU und RAG-Muster
Das RAG-Muster mit dem Phi-3 Onnx Hosted Model nutzt den Retrieval-Augmented Generation-Ansatz und kombiniert die Leistungsfähigkeit der Phi-3-Modelle mit ONNX-Hosting für effiziente KI-Bereitstellungen. Dieses Muster ist entscheidend für das Feinabstimmen von Modellen für domänenspezifische Aufgaben und bietet eine Kombination aus Qualität, Kosteneffizienz und Verständnis für lange Kontexte. Es ist Teil der Azure AI-Suite, die eine breite Auswahl an Modellen bietet, die leicht zu finden, auszuprobieren und zu nutzen sind und den Anpassungsbedürfnissen verschiedener Branchen gerecht werden. Die Phi-3-Modelle, einschließlich Phi-3-mini, Phi-3-small und Phi-3-medium, sind im Azure AI Model Catalog verfügbar und können eigenständig oder über Plattformen wie HuggingFace und ONNX feinabgestimmt und bereitgestellt werden, was Microsofts Engagement für zugängliche und effiziente KI-Lösungen unterstreicht.

## Was ist WebGPU
WebGPU ist eine moderne Web-Grafik-API, die entwickelt wurde, um einen effizienten Zugriff auf die Grafikverarbeitungseinheit (GPU) eines Geräts direkt aus Webbrowsern zu ermöglichen. Sie soll der Nachfolger von WebGL sein und bietet mehrere wesentliche Verbesserungen:

1. **Kompatibilität mit modernen GPUs**: WebGPU wurde entwickelt, um nahtlos mit aktuellen GPU-Architekturen zu arbeiten und dabei System-APIs wie Vulkan, Metal und Direct3D 12 zu nutzen.
2. **Verbesserte Leistung**: Es unterstützt allgemeine GPU-Berechnungen und schnellere Operationen, was es sowohl für die Grafikdarstellung als auch für maschinelle Lernaufgaben geeignet macht.
3. **Erweiterte Funktionen**: WebGPU bietet Zugriff auf fortschrittlichere GPU-Funktionen und ermöglicht komplexere und dynamischere Grafik- und Rechenaufgaben.
4. **Reduzierte JavaScript-Belastung**: Durch die Verlagerung von mehr Aufgaben auf die GPU reduziert WebGPU die Belastung von JavaScript erheblich, was zu einer besseren Leistung und flüssigeren Erfahrungen führt.

WebGPU wird derzeit von Browsern wie Google Chrome unterstützt, und es wird daran gearbeitet, die Unterstützung auf andere Plattformen auszuweiten.

### 03.WebGPU
Erforderliche Umgebung:

**Unterstützte Browser:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### WebGPU aktivieren:

- In Chrome/Microsoft Edge 

Aktivieren Sie das `chrome://flags/#enable-unsafe-webgpu`-Flag.

#### Öffnen Sie Ihren Browser:
Starten Sie Google Chrome oder Microsoft Edge.

#### Greifen Sie auf die Flags-Seite zu:
Geben Sie in die Adressleiste `chrome://flags` ein und drücken Sie die Eingabetaste.

#### Suchen Sie das Flag:
Geben Sie im Suchfeld oben auf der Seite „enable-unsafe-webgpu“ ein.

#### Aktivieren Sie das Flag:
Suchen Sie das #enable-unsafe-webgpu-Flag in der Ergebnisliste.

Klicken Sie auf das Dropdown-Menü daneben und wählen Sie „Enabled“.

#### Starten Sie Ihren Browser neu:

Nachdem Sie das Flag aktiviert haben, müssen Sie Ihren Browser neu starten, damit die Änderungen wirksam werden. Klicken Sie auf die Schaltfläche „Relaunch“, die unten auf der Seite erscheint.

- Für Linux starten Sie den Browser mit `--enable-features=Vulkan`.
- Safari 18 (macOS 15) hat WebGPU standardmäßig aktiviert.
- In Firefox Nightly geben Sie about:config in die Adressleiste ein und `set dom.webgpu.enabled to true`.

### GPU für Microsoft Edge einrichten 

Hier sind die Schritte, um eine Hochleistungs-GPU für Microsoft Edge unter Windows einzurichten:

- **Einstellungen öffnen:** Klicken Sie auf das Startmenü und wählen Sie „Einstellungen“.
- **Systemeinstellungen:** Gehen Sie zu „System“ und dann zu „Anzeige“.
- **Grafikeinstellungen:** Scrollen Sie nach unten und klicken Sie auf „Grafikeinstellungen“.
- **App auswählen:** Wählen Sie unter „Eine App zur Festlegung der Präferenz auswählen“ die Option „Desktop-App“ und dann „Durchsuchen“.
- **Edge auswählen:** Navigieren Sie zum Edge-Installationsordner (normalerweise `C:\Program Files (x86)\Microsoft\Edge\Application`) und wählen Sie `msedge.exe`.
- **Präferenz festlegen:** Klicken Sie auf „Optionen“, wählen Sie „Hohe Leistung“ und klicken Sie dann auf „Speichern“.
Dies stellt sicher, dass Microsoft Edge Ihre Hochleistungs-GPU für eine bessere Leistung verwendet. 
- **Starten Sie Ihren Rechner neu**, damit diese Einstellungen wirksam werden.

### Öffnen Sie Ihre Codespace:
Navigieren Sie zu Ihrem Repository auf GitHub.
Klicken Sie auf die Schaltfläche „Code“ und wählen Sie „Mit Codespaces öffnen“.

Falls Sie noch keinen Codespace haben, können Sie einen erstellen, indem Sie auf „Neuer Codespace“ klicken.

**Hinweis** Installation der Node-Umgebung in Ihrem Codespace
Das Ausführen eines npm-Demos aus einem GitHub Codespace ist eine großartige Möglichkeit, Ihr Projekt zu testen und zu entwickeln. Hier ist eine Schritt-für-Schritt-Anleitung, um Ihnen den Einstieg zu erleichtern:

### Richten Sie Ihre Umgebung ein:
Sobald Ihr Codespace geöffnet ist, stellen Sie sicher, dass Node.js und npm installiert sind. Sie können dies überprüfen, indem Sie:
```
node -v
```
```
npm -v
```

Falls diese nicht installiert sind, können Sie sie installieren mit:
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
Führen Sie den folgenden Befehl aus, um alle notwendigen Abhängigkeiten zu installieren, die in Ihrer package.json-Datei aufgelistet sind:

```
npm install
```

### Demo ausführen:
Sobald die Abhängigkeiten installiert sind, können Sie Ihr Demo-Skript ausführen. Dieses ist normalerweise im Skriptabschnitt Ihrer package.json angegeben. Wenn Ihr Demo-Skript beispielsweise „start“ heißt, können Sie es wie folgt ausführen:

```
npm run build
```
```
npm run dev
```

### Auf die Demo zugreifen:
Falls Ihre Demo einen Webserver umfasst, stellt Codespaces eine URL bereit, um darauf zuzugreifen. Suchen Sie nach einer Benachrichtigung oder überprüfen Sie die Registerkarte „Ports“, um die URL zu finden.

**Hinweis:** Das Modell muss im Browser zwischengespeichert werden, daher kann das Laden etwas Zeit in Anspruch nehmen. 

### RAG-Demo
Laden Sie die Markdown-Datei `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/` hoch.

### Wählen Sie Ihre Datei:
Klicken Sie auf die Schaltfläche „Datei auswählen“, um das Dokument auszuwählen, das Sie hochladen möchten.

### Dokument hochladen:
Nachdem Sie Ihre Datei ausgewählt haben, klicken Sie auf die Schaltfläche „Hochladen“, um Ihr Dokument für RAG (Retrieval-Augmented Generation) zu laden.

### Starten Sie Ihren Chat:
Sobald das Dokument hochgeladen ist, können Sie eine Chat-Sitzung mit RAG basierend auf dem Inhalt Ihres Dokuments starten.

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.