# AGENTS.md

## Projektübersicht

PhiCookBook ist ein umfassendes Kochbuch-Repository mit praktischen Beispielen, Tutorials und Dokumentationen für die Arbeit mit der Phi-Familie von Small Language Models (SLMs) von Microsoft. Das Repository zeigt verschiedene Anwendungsfälle, darunter Inferenz, Feinabstimmung, Quantisierung, RAG-Implementierungen und multimodale Anwendungen auf verschiedenen Plattformen und Frameworks.

**Wichtige Technologien:**
- **Sprachen:** Python, C#/.NET, JavaScript/Node.js
- **Frameworks:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Plattformen:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **Modelltypen:** Phi-3, Phi-3.5, Phi-4 (Text-, Bild-, Multimodal- und Argumentationsvarianten)

**Repository-Struktur:**
- `/code/` - Funktionierende Code-Beispiele und Musterimplementierungen
- `/md/` - Detaillierte Dokumentation, Tutorials und Anleitungen  
- `/translations/` - Übersetzungen in mehrere Sprachen (über 50 Sprachen durch automatisierte Workflows)
- `/.devcontainer/` - Dev-Container-Konfiguration (Python 3.12 mit Ollama)

## Einrichtung der Entwicklungsumgebung

### Verwendung von GitHub Codespaces oder Dev-Containern (empfohlen)

1. Öffnen in GitHub Codespaces (am schnellsten):
   - Klicken Sie auf das "Open in GitHub Codespaces"-Badge in der README
   - Der Container wird automatisch mit Python 3.12 und Ollama mit Phi-3 konfiguriert

2. Öffnen in VS Code Dev-Containern:
   - Verwenden Sie das "Open in Dev Containers"-Badge aus der README
   - Der Container benötigt mindestens 16 GB Arbeitsspeicher auf dem Host

### Lokale Einrichtung

**Voraussetzungen:**
- Python 3.12 oder höher
- .NET 8.0 SDK (für C#-Beispiele)
- Node.js 18+ und npm (für JavaScript-Beispiele)
- Mindestens 16 GB RAM empfohlen

**Installation:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Für Python-Beispiele:**
Navigieren Sie zu den spezifischen Beispielverzeichnissen und installieren Sie die Abhängigkeiten:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**Für .NET-Beispiele:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Für JavaScript/Web-Beispiele:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Repository-Organisation

### Code-Beispiele (`/code/`)

- **01.Introduce/** - Grundlegende Einführungen und Einstiegsmuster
- **03.Finetuning/** und **04.Finetuning/** - Feinabstimmungsbeispiele mit verschiedenen Methoden
- **03.Inference/** - Inferenzbeispiele auf unterschiedlicher Hardware (AIPC, MLX)
- **06.E2E/** - End-to-End-Anwendungsbeispiele
- **07.Lab/** - Labor-/experimentelle Implementierungen
- **08.RAG/** - Beispiele für Retrieval-Augmented Generation
- **09.UpdateSamples/** - Neueste aktualisierte Beispiele

### Dokumentation (`/md/`)

- **01.Introduction/** - Einführungshandbücher, Einrichtung der Umgebung, Plattformanleitungen
- **02.Application/** - Anwendungsbeispiele nach Typ organisiert (Text, Code, Bild, Audio usw.)
- **02.QuickStart/** - Schnellstartanleitungen für Azure AI Foundry und GitHub Models
- **03.FineTuning/** - Dokumentation und Tutorials zur Feinabstimmung
- **04.HOL/** - Praktische Übungen (einschließlich .NET-Beispiele)

### Dateiformate

- **Jupyter Notebooks (`.ipynb`)** - Interaktive Python-Tutorials, in README mit 📓 markiert
- **Python-Skripte (`.py`)** - Eigenständige Python-Beispiele
- **C#-Projekte (`.csproj`, `.sln`)** - .NET-Anwendungen und Beispiele
- **JavaScript (`.js`, `package.json`)** - Webbasierte und Node.js-Beispiele
- **Markdown (`.md`)** - Dokumentation und Anleitungen

## Arbeiten mit Beispielen

### Ausführen von Jupyter Notebooks

Die meisten Beispiele werden als Jupyter Notebooks bereitgestellt:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Ausführen von Python-Skripten

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Ausführen von .NET-Beispielen

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Oder die gesamte Lösung erstellen:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Ausführen von JavaScript/Web-Beispielen

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Tests

Dieses Repository enthält Beispielcode und Tutorials, anstatt ein traditionelles Softwareprojekt mit Unit-Tests zu sein. Die Validierung erfolgt typischerweise durch:

1. **Ausführen der Beispiele** - Jedes Beispiel sollte fehlerfrei ausgeführt werden
2. **Überprüfen der Ausgaben** - Überprüfen Sie, ob die Modellantworten angemessen sind
3. **Befolgen der Tutorials** - Schritt-für-Schritt-Anleitungen sollten wie dokumentiert funktionieren

**Allgemeiner Validierungsansatz:**
- Testen der Beispielausführung in der Zielumgebung
- Überprüfen, ob Abhängigkeiten korrekt installiert werden
- Sicherstellen, dass Modelle erfolgreich heruntergeladen/geladen werden
- Bestätigen, dass das erwartete Verhalten der Dokumentation entspricht

## Code-Stil und Konventionen

### Allgemeine Richtlinien

- Beispiele sollten klar, gut kommentiert und lehrreich sein
- Befolgen Sie sprachspezifische Konventionen (PEP 8 für Python, C#-Standards für .NET)
- Halten Sie Beispiele darauf fokussiert, spezifische Phi-Modellfähigkeiten zu demonstrieren
- Fügen Sie Kommentare hinzu, die wichtige Konzepte und modellbezogene Parameter erklären

### Dokumentationsstandards

**URL-Formatierung:**
- Verwenden Sie das Format `[text](../../url)` ohne zusätzliche Leerzeichen
- Relative Links: Verwenden Sie `./` für das aktuelle Verzeichnis, `../` für das übergeordnete
- Keine länderspezifischen Lokalisierungen in URLs (vermeiden Sie `/en-us/`, `/en/`)

**Bilder:**
- Speichern Sie alle Bilder im Verzeichnis `/imgs/`
- Verwenden Sie beschreibende Namen mit englischen Zeichen, Zahlen und Bindestrichen
- Beispiel: `phi-3-architecture.png`

**Markdown-Dateien:**
- Verweisen Sie auf tatsächlich funktionierende Beispiele im Verzeichnis `/code/`
- Halten Sie die Dokumentation synchron mit Codeänderungen
- Verwenden Sie das 📓 Emoji, um Jupyter-Notebook-Links in der README zu markieren

### Dateiorganisation

- Code-Beispiele in `/code/` nach Thema/Funktion organisiert
- Dokumentation in `/md/` spiegelt die Code-Struktur wider, wenn möglich
- Halten Sie verwandte Dateien (Notebooks, Skripte, Konfigurationen) zusammen in Unterverzeichnissen

## Richtlinien für Pull Requests

### Vor dem Einreichen

1. **Forken Sie das Repository** in Ihrem Konto
2. **Trennen Sie PRs nach Typ:**
   - Fehlerbehebungen in einem PR
   - Dokumentationsaktualisierungen in einem anderen
   - Neue Beispiele in separaten PRs
   - Tippfehler können kombiniert werden

3. **Behandeln Sie Merge-Konflikte:**
   - Aktualisieren Sie Ihren lokalen `main`-Branch, bevor Sie Änderungen vornehmen
   - Synchronisieren Sie häufig mit dem Upstream

4. **Übersetzungs-PRs:**
   - Müssen Übersetzungen für ALLE Dateien im Ordner enthalten
   - Behalten Sie eine konsistente Struktur mit der Originalsprache bei

### Erforderliche Prüfungen

PRs führen automatisch GitHub-Workflows aus, um zu validieren:

1. **Relative Pfadvalidierung** - Alle internen Links müssen funktionieren
   - Testen Sie Links lokal: Strg+Klick in VS Code
   - Verwenden Sie Pfadvorschläge von VS Code (`./` oder `../`)

2. **URL-Lokalisierungsprüfung** - Web-URLs dürfen keine Länder-Lokalisierungen enthalten
   - Entfernen Sie `/en-us/`, `/en/` oder andere Sprachcodes
   - Verwenden Sie generische internationale URLs

3. **Defekte URL-Prüfung** - Alle URLs müssen den Status 200 zurückgeben
   - Überprüfen Sie, ob Links vor dem Einreichen zugänglich sind
   - Hinweis: Einige Fehler können durch Netzwerkbeschränkungen verursacht werden

### PR-Titelformat

```
[component] Brief description
```

Beispiele:
- `[docs] Add Phi-4 inference tutorial`
- `[code] Fix ONNX Runtime integration example`
- `[translation] Add Japanese translation for intro guides`

## Häufige Entwicklungsmuster

### Arbeiten mit Phi-Modellen

**Modellladen:**
- Beispiele verwenden verschiedene Frameworks: Transformers, ONNX Runtime, MLX, OpenVINO
- Modelle werden typischerweise von Hugging Face, Azure oder GitHub Models heruntergeladen
- Überprüfen Sie die Modellkompatibilität mit Ihrer Hardware (CPU, GPU, NPU)

**Inferenzmuster:**
- Textgenerierung: Die meisten Beispiele verwenden Chat-/Instruct-Varianten
- Bild: Phi-3-vision und Phi-4-multimodal für Bildverständnis
- Audio: Phi-4-multimodal unterstützt Audioeingaben
- Argumentation: Phi-4-reasoning-Varianten für fortgeschrittene Argumentationsaufgaben

### Plattformspezifische Hinweise

**Azure AI Foundry:**
- Erfordert ein Azure-Abonnement und API-Schlüssel
- Siehe `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Kostenloser Tarif für Tests verfügbar
- Siehe `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokale Inferenz:**
- ONNX Runtime: Plattformübergreifend, optimierte Inferenz
- Ollama: Einfaches lokales Modellmanagement (vorkonfiguriert im Dev-Container)
- Apple MLX: Optimiert für Apple Silicon

## Fehlerbehebung

### Häufige Probleme

**Speicherprobleme:**
- Phi-Modelle benötigen erheblichen RAM (insbesondere Bild-/Multimodal-Varianten)
- Verwenden Sie quantisierte Modelle für ressourcenbeschränkte Umgebungen
- Siehe `/md/01.Introduction/04/QuantifyingPhi.md`

**Abhängigkeitskonflikte:**
- Python-Beispiele können spezifische Versionsanforderungen haben
- Verwenden Sie virtuelle Umgebungen für jedes Beispiel
- Überprüfen Sie die einzelnen `requirements.txt`-Dateien

**Fehler beim Herunterladen von Modellen:**
- Große Modelle können bei langsamen Verbindungen Zeitüberschreitungen verursachen
- Ziehen Sie Cloud-Umgebungen in Betracht (Codespaces, Azure)
- Überprüfen Sie den Hugging Face Cache: `~/.cache/huggingface/`

**.NET-Projektprobleme:**
- Stellen Sie sicher, dass .NET 8.0 SDK installiert ist
- Verwenden Sie `dotnet restore`, bevor Sie die Lösung erstellen
- Einige Projekte haben CUDA-spezifische Konfigurationen (Debug_Cuda)

**JavaScript/Web-Beispiele:**
- Verwenden Sie Node.js 18+ für Kompatibilität
- Löschen Sie `node_modules` und installieren Sie neu, wenn Probleme auftreten
- Überprüfen Sie die Browserkonsole auf WebGPU-Kompatibilitätsprobleme

### Hilfe erhalten

- **Discord:** Treten Sie der Azure AI Foundry Community Discord bei
- **GitHub Issues:** Melden Sie Fehler und Probleme im Repository
- **GitHub Discussions:** Stellen Sie Fragen und teilen Sie Ihr Wissen

## Zusätzlicher Kontext

### Verantwortungsvolle KI

Die Nutzung von Phi-Modellen sollte den Prinzipien der verantwortungsvollen KI von Microsoft folgen:
- Fairness, Zuverlässigkeit, Sicherheit
- Datenschutz und Sicherheit  
- Inklusivität, Transparenz, Verantwortlichkeit
- Verwenden Sie Azure AI Content Safety für Produktionsanwendungen
- Siehe `/md/01.Introduction/01/01.AISafety.md`

### Übersetzungen

- Über 50 Sprachen werden durch automatisierte GitHub Action unterstützt
- Übersetzungen im Verzeichnis `/translations/`
- Verwaltet durch den co-op-translator Workflow
- Bearbeiten Sie übersetzte Dateien nicht manuell (automatisch generiert)

### Beitrag leisten

- Befolgen Sie die Richtlinien in `CONTRIBUTING.md`
- Stimmen Sie der Contributor License Agreement (CLA) zu
- Halten Sie sich an den Microsoft Open Source Code of Conduct
- Halten Sie Sicherheit und Anmeldeinformationen aus Commits heraus

### Mehrsprachige Unterstützung

Dies ist ein mehrsprachiges Repository mit Beispielen in:
- **Python** - ML/AI-Workflows, Jupyter Notebooks, Feinabstimmung
- **C#/.NET** - Unternehmensanwendungen, ONNX Runtime-Integration
- **JavaScript** - Webbasierte KI, Browser-Inferenz mit WebGPU

Wählen Sie die Sprache, die am besten zu Ihrem Anwendungsfall und Ziel passt.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.