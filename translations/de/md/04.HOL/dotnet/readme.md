## Willkommen bei den Phi-Labs mit C#

Es gibt eine Auswahl an Labs, die zeigen, wie man die leistungsstarken verschiedenen Versionen der Phi-Modelle in einer .NET-Umgebung integriert.

## Voraussetzungen

Bevor Sie das Beispiel ausführen, stellen Sie sicher, dass Sie Folgendes installiert haben:

**.NET 9:** Vergewissern Sie sich, dass Sie die [neueste Version von .NET](https://dotnet.microsoft.com/download/dotnet?WT.mc_id=aiml-137032-kinfeylo) auf Ihrem Rechner installiert haben.

**(Optional) Visual Studio oder Visual Studio Code:** Sie benötigen eine IDE oder einen Code-Editor, der .NET-Projekte ausführen kann. [Visual Studio](https://visualstudio.microsoft.com?WT.mc_id=aiml-137032-kinfeylo) oder [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo) werden empfohlen.

**Mit git** klonen Sie lokal eine der verfügbaren Phi-3, Phi3.5 oder Phi-4 Versionen von [Hugging Face](https://huggingface.co/collections/lokinfey/phi-4-family-679c6f234061a1ab60f5547c).

**Laden Sie Phi-4 ONNX-Modelle** auf Ihren lokalen Rechner herunter:

### Navigieren Sie zum Ordner, in dem die Modelle gespeichert werden sollen

```bash
cd c:\phi\models
```

### Fügen Sie Unterstützung für lfs hinzu

```bash
git lfs install 
```

### Klonen und laden Sie das Phi-4 mini instruct Modell und das Phi-4 multimodale Modell herunter

```bash
git clone https://huggingface.co/microsoft/Phi-4-mini-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-4-multimodal-instruct-onnx
```

**Laden Sie die Phi-3 ONNX-Modelle** auf Ihren lokalen Rechner herunter:

### Klonen und laden Sie das Phi-3 mini 4K instruct Modell und das Phi-3 vision 128K Modell herunter

```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx

git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```

**Wichtig:** Die aktuellen Demos sind darauf ausgelegt, die ONNX-Versionen der Modelle zu verwenden. Die vorherigen Schritte klonen die folgenden Modelle.

## Über die Labs

Die Hauptlösung enthält mehrere Beispiel-Labs, die die Fähigkeiten der Phi-Modelle mit C# demonstrieren.

| Projekt | Modell | Beschreibung |
| ------------ | -----------| ----------- |
| [LabsPhi301](../../../../../md/04.HOL/dotnet/src/LabsPhi301) | Phi-3 oder Phi-3.5 | Beispiel für einen Konsolen-Chat, der es dem Benutzer ermöglicht, Fragen zu stellen. Das Projekt lädt ein lokales ONNX Phi-3 Modell mit den `Microsoft.ML.OnnxRuntime` Bibliotheken. |
| [LabsPhi302](../../../../../md/04.HOL/dotnet/src/LabsPhi302) | Phi-3 oder Phi-3.5 | Beispiel für einen Konsolen-Chat, der es dem Benutzer ermöglicht, Fragen zu stellen. Das Projekt lädt ein lokales ONNX Phi-3 Modell mit den `Microsoft.Semantic.Kernel` Bibliotheken. |
| [LabPhi303](../../../../../md/04.HOL/dotnet/src/LabsPhi303) | Phi-3 oder Phi-3.5 | Dies ist ein Beispielprojekt, das ein lokales phi3 Vision Modell zur Bildanalyse verwendet. Das Projekt lädt ein lokales ONNX Phi-3 Vision Modell mit den `Microsoft.ML.OnnxRuntime` Bibliotheken. |
| [LabPhi304](../../../../../md/04.HOL/dotnet/src/LabsPhi304) | Phi-3 oder Phi-3.5 | Dies ist ein Beispielprojekt, das ein lokales phi3 Vision Modell zur Bildanalyse verwendet. Das Projekt lädt ein lokales ONNX Phi-3 Vision Modell mit den `Microsoft.ML.OnnxRuntime` Bibliotheken. Das Projekt bietet außerdem ein Menü mit verschiedenen Optionen zur Interaktion mit dem Benutzer. | 
| [LabPhi4-Chat](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-01OnnxRuntime) | Phi-4 | Beispiel für einen Konsolen-Chat, der es dem Benutzer ermöglicht, Fragen zu stellen. Das Projekt lädt ein lokales ONNX Phi-4 Modell mit den `Microsoft.ML.OnnxRuntime` Bibliotheken. |
| [LabPhi-4-SK](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-02SK) | Phi-4 | Beispiel für einen Konsolen-Chat, der es dem Benutzer ermöglicht, Fragen zu stellen. Das Projekt lädt ein lokales ONNX Phi-4 Modell mit den `Semantic Kernel` Bibliotheken. |
| [LabsPhi4-Chat-03GenAIChatClient](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-03GenAIChatClient) | Phi-4 | Beispiel für einen Konsolen-Chat, der es dem Benutzer ermöglicht, Fragen zu stellen. Das Projekt lädt ein lokales ONNX Phi-4 Modell mit den `Microsoft.ML.OnnxRuntimeGenAI` Bibliotheken und implementiert das `IChatClient` aus `Microsoft.Extensions.AI`. |
| [LabsPhi4-Chat-04-ChatMode](../../../../../md/04.HOL/dotnet/src/LabsPhi4-Chat-04-ChatMode) | Phi-4 | Beispiel für einen Konsolen-Chat, der es dem Benutzer ermöglicht, Fragen zu stellen. Der Chat implementiert ein Gedächtnis. |
| [Phi-4multimodal-vision](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-01Images) | Phi-4 | Dies ist ein Beispielprojekt, das ein lokales Phi-4 Modell zur Bildanalyse verwendet und das Ergebnis in der Konsole anzeigt. Das Projekt lädt ein lokales Phi-4-`multimodal-instruct-onnx` Modell mit den `Microsoft.ML.OnnxRuntime` Bibliotheken. |
| [LabPhi4-MM-Audio](../../../../../md/04.HOL/dotnet/src/LabsPhi4-MultiModal-02Audio) | Phi-4 | Dies ist ein Beispielprojekt, das ein lokales Phi-4 Modell verwendet, um eine Audiodatei zu analysieren, das Transkript der Datei zu erstellen und das Ergebnis in der Konsole anzuzeigen. Das Projekt lädt ein lokales Phi-4-`multimodal-instruct-onnx` Modell mit den `Microsoft.ML.OnnxRuntime` Bibliotheken. |

## So führen Sie die Projekte aus

Um die Projekte auszuführen, gehen Sie wie folgt vor:

1. Klonen Sie das Repository auf Ihren lokalen Rechner.

1. Öffnen Sie ein Terminal und navigieren Sie zum gewünschten Projekt. Zum Beispiel führen wir `LabsPhi4-Chat-01OnnxRuntime` aus.

    ```bash
    cd .\src\LabsPhi4-Chat-01OnnxRuntime \
    ```

1. Führen Sie das Projekt mit dem Befehl aus

    ```bash
    dotnet run
    ```

1. Das Beispielprojekt fordert eine Benutzereingabe an und antwortet mit dem lokalen Modell.

   Die laufende Demo sieht ungefähr so aus:

   ```bash
   PS D:\phi\PhiCookBook\md\04.HOL\dotnet\src\LabsPhi4-Chat-01OnnxRuntime> dotnet run
   Ask your question. Type an empty string to Exit.
   Q: 2+2
   Phi4: The sum of 2 and 2 is 4.
   Q:
   ```

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.