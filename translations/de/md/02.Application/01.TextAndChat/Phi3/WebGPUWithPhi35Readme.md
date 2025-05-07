<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-07T11:00:10+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "de"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo zur Präsentation von WebGPU und dem RAG-Muster

Das RAG-Muster mit dem Phi-3.5 Onnx Hosted Modell nutzt den Retrieval-Augmented Generation-Ansatz und kombiniert die Leistungsfähigkeit der Phi-3.5-Modelle mit ONNX-Hosting für effiziente KI-Einsätze. Dieses Muster ist besonders hilfreich beim Feinabstimmen von Modellen für domänenspezifische Aufgaben und bietet eine Mischung aus Qualität, Kosteneffizienz und Verständnis von Langzeitkontexten. Es ist Teil der Azure AI-Suite und stellt eine breite Auswahl an Modellen bereit, die einfach zu finden, auszuprobieren und zu verwenden sind, um den Anpassungsbedarf verschiedener Branchen zu erfüllen.

## Was ist WebGPU  
WebGPU ist eine moderne Web-Grafik-API, die einen effizienten Zugriff auf die Grafikeinheit (GPU) eines Geräts direkt aus Webbrowsern ermöglicht. Sie soll der Nachfolger von WebGL werden und bietet mehrere wesentliche Verbesserungen:

1. **Kompatibilität mit modernen GPUs**: WebGPU ist darauf ausgelegt, nahtlos mit zeitgemäßen GPU-Architekturen zusammenzuarbeiten und nutzt System-APIs wie Vulkan, Metal und Direct3D 12.
2. **Verbesserte Leistung**: Es unterstützt allgemeine GPU-Berechnungen und schnellere Abläufe, wodurch es sowohl für Grafikrendering als auch für maschinelles Lernen geeignet ist.
3. **Erweiterte Funktionen**: WebGPU bietet Zugriff auf fortgeschrittene GPU-Fähigkeiten, die komplexere und dynamischere Grafik- und Rechenaufgaben ermöglichen.
4. **Reduzierte JavaScript-Belastung**: Durch die Auslagerung weiterer Aufgaben an die GPU verringert WebGPU die Last auf JavaScript erheblich, was zu besserer Performance und flüssigeren Abläufen führt.

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

#### Greifen Sie auf die Flags-Seite zu:  
Geben Sie in der Adressleiste `chrome://flags` ein und drücken Sie Enter.

#### Suchen Sie nach der Flagge:  
Geben Sie im Suchfeld oben auf der Seite 'enable-unsafe-webgpu' ein.

#### Aktivieren Sie die Flagge:  
Suchen Sie in der Ergebnisliste die #enable-unsafe-webgpu-Flagge.

Klicken Sie auf das Dropdown-Menü daneben und wählen Sie Enabled.

#### Starten Sie Ihren Browser neu:  

Nach der Aktivierung der Flagge müssen Sie den Browser neu starten, damit die Änderungen wirksam werden. Klicken Sie dazu auf die Schaltfläche Relaunch, die unten auf der Seite erscheint.

- Unter Linux starten Sie den Browser mit `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) hat WebGPU standardmäßig aktiviert.  
- In Firefox Nightly geben Sie about:config in die Adressleiste ein und `set dom.webgpu.enabled to true`.

### Einrichtung der GPU für Microsoft Edge  

Hier sind die Schritte zur Einrichtung einer Hochleistungs-GPU für Microsoft Edge unter Windows:

- **Einstellungen öffnen:** Klicken Sie auf das Startmenü und wählen Sie Einstellungen.  
- **Systemeinstellungen:** Gehen Sie zu System und dann Anzeige.  
- **Grafikeinstellungen:** Scrollen Sie nach unten und klicken Sie auf Grafikeinstellungen.  
- **App auswählen:** Unter „App zur Einstellung der Präferenz auswählen“ wählen Sie Desktop-App und dann Durchsuchen.  
- **Edge auswählen:** Navigieren Sie zum Edge-Installationsordner (normalerweise `C:\Program Files (x86)\Microsoft\Edge\Application`) und wählen Sie `msedge.exe` aus.  
- **Präferenz festlegen:** Klicken Sie auf Optionen, wählen Sie Hochleistung und klicken Sie dann auf Speichern.  
Dies stellt sicher, dass Microsoft Edge Ihre Hochleistungs-GPU für bessere Leistung nutzt.  
- **Starten Sie** Ihren Rechner neu, damit die Einstellungen wirksam werden.

### Beispiele: Bitte [klicken Sie auf diesen Link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.