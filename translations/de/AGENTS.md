# AGENTS.md

## Projektübersicht

PhiCookBook ist ein umfassendes Repository für Kochbücher mit praxisnahen Beispielen, Tutorials und Dokumentationen für die Arbeit mit der Phi-Familie von Small Language Models (SLMs) von Microsoft. Das Repository demonstriert verschiedene Anwendungsfälle, darunter Inferenz, Feinabstimmung, Quantisierung, RAG-Implementierungen und multimodale Anwendungen auf unterschiedlichen Plattformen und Frameworks.

**Wichtige Technologien:**
- **Programmiersprachen:** Python, C#/.NET, JavaScript/Node.js
- **Frameworks:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Plattformen:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Modelltypen:** Phi-3, Phi-3.5, Phi-4 (Text-, Vision-, multimodale und Reasoning-Varianten)

**Repository-Struktur:**
- `/code/` - Arbeitscode-Beispiele und Beispielimplementierungen
- `/md/` - Ausführliche Dokumentation, Tutorials und Anleitungen  
- `/translations/` - Mehrsprachige Übersetzungen (50+ Sprachen über automatisierten Workflow)
- `/.devcontainer/` - Dev-Container-Konfiguration (Python 3.12 mit Ollama)

## Einrichtung der Entwicklungsumgebung

### Verwendung von GitHub Codespaces oder Dev-Containern (empfohlen)

1. In GitHub Codespaces öffnen (schnellste Variante):
   - Klicken Sie auf das "Open in GitHub Codespaces"-Abzeichen in der README
   - Container wird automatisch mit Python 3.12 und Ollama mit Phi-3 konfiguriert

2. In VS Code Dev Containern öffnen:
   - Verwenden Sie das "Open in Dev Containers"-Abzeichen in der README
   - Container benötigt mindestens 16 GB Host-Speicher

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
Navigieren Sie zu spezifischen Beispielverzeichnissen und installieren Sie Abhängigkeiten:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # falls requirements.txt existiert
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
npm run dev  # Entwicklungsserver starten
npm run build  # Für Produktion bauen
```

## Repository-Organisation

### Code-Beispiele (`/code/`)

- **01.Introduce/** - Grundlagen und Einstiegsbeispiele
- **03.Finetuning/** und **04.Finetuning/** - Feinabstimmungsbeispiele mit verschiedenen Methoden
- **03.Inference/** - Inferenzbeispiele auf unterschiedlichen Hardwareplattformen (AIPC, MLX)
- **06.E2E/** - End-to-End-Anwendungsbeispiele
- **07.Lab/** - Labor- und experimentelle Implementierungen
- **08.RAG/** - Retrieval-Augmented Generation-Beispiele
- **09.UpdateSamples/** - Neueste aktualisierte Beispiele

### Dokumentation (`/md/`)

- **01.Introduction/** - Einführung, Umgebungssetup, Plattformanleitungen
- **02.Application/** - Anwendungsbeispiele nach Typ organisiert (Text, Code, Vision, Audio etc.)
- **02.QuickStart/** - Schnellstartanleitungen für Microsoft Foundry und GitHub Models
- **03.FineTuning/** - Dokumentation und Tutorials zum Fein-Tuning
- **04.HOL/** - Hands-on-Labs (inkl. .NET-Beispiele)

### Dateiformate

- **Jupyter Notebooks (`.ipynb`)** - Interaktive Python-Tutorials, mit 📓 in README markiert
- **Python-Skripte (`.py`)** - Eigenständige Python-Beispiele
- **C#-Projekte (`.csproj`, `.sln`)** - .NET-Anwendungen und Beispiele
- **JavaScript (`.js`, `package.json`)** - Web- und Node.js-Beispiele
- **Markdown (`.md`)** - Dokumentation und Anleitungen

## Arbeit mit Beispielen

### Ausführen von Jupyter Notebooks

Die meisten Beispiele werden als Jupyter Notebooks bereitgestellt:
```bash
pip install jupyter notebook
jupyter notebook  # Öffnet die Browser-Schnittstelle
# Navigiere zur gewünschten .ipynb-Datei
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

Oder gesamten Lösung bauen:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Ausführen von JavaScript/Web-Beispielen

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Entwicklung mit Hot Reload
```

## Testen

Dieses Repository enthält Beispielcode und Tutorials anstelle eines traditionellen Softwareprojekts mit Unit-Tests. Die Validierung erfolgt typischerweise durch:

1. **Ausführen der Beispiele** – Jedes Beispiel soll fehlerfrei laufen
2. **Überprüfen der Ausgaben** – Prüfen, ob die Modellantworten angemessen sind
3. **Befolgen der Tutorials** – Schritt-für-Schritt-Anleitungen sollen wie dokumentiert funktionieren

**Üblicher Validierungsansatz:**
- Testen der Ausführung der Beispiele in der Zielumgebung
- Überprüfen, ob Abhängigkeiten richtig installiert werden
- Sicherstellen, dass Modelle erfolgreich heruntergeladen/geladen werden
- Bestätigen, dass erwartetes Verhalten der Dokumentation entspricht

## Code-Stil und Konventionen

### Allgemeine Richtlinien

- Beispiele sollen klar, gut kommentiert und lehrreich sein
- Sprachspezifische Konventionen einhalten (PEP 8 für Python, C#-Standards für .NET)
- Beispiele sollen sich auf spezifische Phi-Modellfähigkeiten konzentrieren
- Kommentare zu Schlüsselkonzepten und modell-spezifischen Parametern einfügen

### Dokumentationsstandards

**URL-Formatierung:**
- Verwenden Sie das Format `[Text](../../URL)` ohne zusätzliche Leerzeichen
- Relative Links: `./` für aktuelles Verzeichnis, `../` für übergeordnetes Verzeichnis
- Keine länderspezifischen URLs (keine `/en-us/` oder `/en/`)

**Bilder:**
- Alle Bilder im Verzeichnis `/imgs/` speichern
- Beschreibende Namen mit englischen Buchstaben, Zahlen und Bindestrichen verwenden
- Beispiel: `phi-3-architecture.png`

**Markdown-Dateien:**
- Bezug auf tatsächlich funktionierende Beispiele im Verzeichnis `/code/`
- Dokumentation mit Änderungen im Code synchron halten
- Verwenden Sie das 📓-Emoji, um Jupyter Notebook-Links in der README zu kennzeichnen

### Dateiorganisation

- Code-Beispiele in `/code/` nach Themen/Funktionen organisiert
- Dokumentation in `/md/` spiegelt die Code-Struktur nach Möglichkeit wider
- Verwandte Dateien (Notebooks, Skripte, Konfigurationen) zusammen in Unterverzeichnissen halten

## Pull-Request-Richtlinien

### Vor dem Einreichen

1. **Forken Sie das Repository** in Ihr Konto
2. **PRs nach Typ trennen:**
   - Fehlerbehebungen in einem PR
   - Dokumentationsupdates in einem anderen
   - Neue Beispiele in separaten PRs
   - Tippfehlerkorrekturen können kombiniert werden

3. **Merge-Konflikte behandeln:**
   - Aktuellen `main`-Branch lokal aktualisieren, bevor Änderungen gemacht werden
   - Häufig mit Upstream synchronisieren

4. **Übersetzungs-PRs:**
   - Müssen Übersetzungen für ALLE Dateien im Ordner enthalten
   - Struktur sollte mit Originalsprache übereinstimmen

### Erforderliche Prüfungen

PRs führen automatisch GitHub-Workflows zur Validierung aus:

1. **Validierung relativer Pfade** – Alle internen Links müssen funktionieren
   - Testen Sie Links lokal: Strg+Klick in VS Code
   - Pfadvorschläge von VS Code verwenden (`./` oder `../`)

2. **URL-Lokalisierungsprüfun**g – Web-URLs dürfen keine länderspezifischen Codes enthalten
   - Entfernen Sie `/en-us/`, `/en/` oder andere Sprachcodes
   - Verwenden Sie generische internationale URLs

3. **Überprüfung auf defekte URLs** – Alle URLs müssen HTTP 200 zurückgeben
   - Links vor dem Einreichen auf Erreichbarkeit prüfen
   - Hinweis: Manchmal sind Ausfälle auf Netzwerkeinschränkungen zurückzuführen

### PR-Titelformat

```
[component] Brief description
```

Beispiele:
- `[docs] Anleitung für Phi-4 Inferenz hinzufügen`
- `[code] ONNX Runtime-Integrationsbeispiel beheben`
- `[translation] Japanische Übersetzung für Einführungsanleitungen hinzufügen`

## Häufige Entwicklungs-Muster

### Arbeit mit Phi-Modellen

**Modell-Laden:**
- Beispiele verwenden verschiedene Frameworks: Transformers, ONNX Runtime, MLX, OpenVINO
- Modelle werden typischerweise von Hugging Face, Azure oder GitHub Models heruntergeladen
- Prüfen Sie die Kompatibilität der Modelle mit Ihrer Hardware (CPU, GPU, NPU)

**Inferenzmuster:**
- Textgenerierung: Die meisten Beispiele verwenden Chat-/Instruct-Varianten
- Vision: Phi-3-vision und Phi-4-multimodal für Bildverstehen
- Audio: Phi-4-multimodal unterstützt Audioeingaben
- Reasoning: Phi-4-reasoning-Varianten für fortgeschrittene Reasoning-Aufgaben

### Plattform-spezifische Hinweise

**Microsoft Foundry:**
- Benötigt Azure-Abonnement und API-Schlüssel
- Siehe `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Kostenlose Stufe verfügbar zum Testen
- Siehe `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokale Inferenz:**
- ONNX Runtime: plattformübergreifend, optimierte Inferenz
- Ollama: Einfache lokale Modellverwaltung (vorkonfiguriert im Dev-Container)
- Apple MLX: Optimiert für Apple Silicon

## Fehlerbehebung

### Häufige Probleme

**Speicherprobleme:**
- Phi-Modelle benötigen viel RAM (insbesondere Vision-/multimodale Varianten)
- Verwenden Sie quantisierte Modelle für ressourcenbeschränkte Umgebungen
- Siehe `/md/01.Introduction/04/QuantifyingPhi.md`

**Abhängigkeitskonflikte:**
- Python-Beispiele können spezifische Versionsanforderungen haben
- Verwenden Sie virtuelle Umgebungen für jedes Beispiel
- Prüfen Sie die einzelnen `requirements.txt`-Dateien

**Fehler beim Modelldownload:**
- Große Modelle können bei langsamer Verbindung Timeouts verursachen
- Verwenden Sie ggf. Cloud-Umgebungen (Codespaces, Azure)
- Prüfen Sie den Hugging Face Cache: `~/.cache/huggingface/`

**Probleme mit .NET-Projekten:**
- Stellen Sie sicher, dass .NET 8.0 SDK installiert ist
- Verwenden Sie `dotnet restore` vor dem Bauen
- Einige Projekte haben CUDA-spezifische Konfigurationen (Debug_Cuda)

**JavaScript/Web-Beispiele:**
- Node.js 18+ für Kompatibilität verwenden
- Löschen Sie `node_modules` und installieren Sie neu bei Problemen
- Prüfen Sie die Browserkonsole auf WebGPU-Kompatibilitätsprobleme

### Hilfe erhalten

- **Discord:** Treten Sie dem Microsoft Foundry Community Discord bei
- **GitHub Issues:** Melden Sie Fehler und Probleme im Repository
- **GitHub Discussions:** Stellen Sie Fragen und teilen Sie Wissen

## Zusätzlicher Kontext

### Verantwortungsbewusstes KI-Handeln

Alle Phi-Modellnutzungen sollten Microsofts Prinzipien für verantwortungsbewusste KI befolgen:
- Fairness, Zuverlässigkeit, Sicherheit
- Datenschutz und Sicherheit  
- Inklusivität, Transparenz, Verantwortlichkeit
- Verwenden Sie Azure AI Content Safety für Produktionsanwendungen
- Siehe `/md/01.Introduction/01/01.AISafety.md`

### Übersetzungen

- 50+ Sprachen werden über automatisierten GitHub Action Workflow unterstützt
- Übersetzungen im Verzeichnis `/translations/`
- Werden vom co-op-translator Workflow gepflegt
- Bitte übersetzte Dateien nicht manuell bearbeiten (automatisch generiert)

### Mitwirken

- Folgen Sie den Richtlinien in `CONTRIBUTING.md`
- Stimmen Sie der Contributor License Agreement (CLA) zu
- Beachten Sie den Microsoft Open Source Code of Conduct
- Halten Sie Sicherheit und Zugangsdaten aus Commits heraus

### Mehrsprachige Unterstützung

Dies ist ein mehrsprachiges Repository mit Beispielen in:
- **Python** - ML/AI-Workflows, Jupyter Notebooks, Feinabstimmung
- **C#/.NET** - Unternehmensanwendungen, ONNX Runtime Integration
- **JavaScript** - Webbasierte KI, Browser-Inferenz mit WebGPU

Wählen Sie die Sprache, die für Ihren Anwendungsfall und Ihr Deployment-Ziel am besten geeignet ist.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->