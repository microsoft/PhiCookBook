# **Erstellen Sie Ihren eigenen Visual Studio Code GitHub Copilot Chat mit der Microsoft Phi-3 Familie**

Haben Sie den Workspace-Agent in GitHub Copilot Chat verwendet? Möchten Sie den Code-Agent Ihres eigenen Teams erstellen? Dieses praktische Labor möchte das Open-Source-Modell kombinieren, um einen Code-Geschäftsagenten auf Unternehmensebene zu erstellen.

## **Grundlage**

### **Warum Microsoft Phi-3 wählen**

Phi-3 ist eine Familienserie, die phi-3-mini, phi-3-small und phi-3-medium basierend auf unterschiedlichen Trainingsparametern für Textgenerierung, Dialogvervollständigung und Codegenerierung umfasst. Es gibt auch phi-3-vision, basierend auf Vision. Es eignet sich für Unternehmen oder verschiedene Teams, um offline generative KI-Lösungen zu erstellen.

Empfohlen, diesen Link zu lesen [https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md](https://github.com/microsoft/PhiCookBook/blob/main/md/01.Introduction/01/01.PhiFamily.md)

### **Microsoft GitHub Copilot Chat**

Die GitHub Copilot Chat-Erweiterung bietet Ihnen eine Chat-Oberfläche, mit der Sie mit GitHub Copilot interagieren und Antworten auf codierungsbezogene Fragen direkt in VS Code erhalten können, ohne Dokumentationen durchsuchen oder Online-Foren konsultieren zu müssen.

Copilot Chat kann Syntaxhervorhebung, Einrückung und andere Formatierungsfunktionen verwenden, um die generierte Antwort klarer zu machen. Je nach Art der Frage des Benutzers kann das Ergebnis Links zu Kontext enthalten, den Copilot für die Generierung der Antwort verwendet hat, wie Quellcodedateien oder Dokumentationen, oder Schaltflächen für den Zugriff auf VS Code-Funktionen.

- Copilot Chat integriert sich in Ihren Entwicklerablauf und hilft Ihnen genau dort, wo Sie es brauchen:

- Starten Sie ein Inline-Chat-Gespräch direkt aus dem Editor oder Terminal für Hilfe beim Codieren

- Verwenden Sie die Chat-Ansicht, um einen KI-Assistenten an der Seite zu haben, der Ihnen jederzeit hilft

- Starten Sie Quick Chat, um eine schnelle Frage zu stellen und sofort wieder mit Ihrer Arbeit fortzufahren

Sie können GitHub Copilot Chat in verschiedenen Szenarien verwenden, wie zum Beispiel:

- Beantwortung von Programmierfragen, wie ein Problem am besten zu lösen ist

- Erläuterung des Codes anderer Personen und Vorschläge zur Verbesserung

- Vorschlagen von Code-Fixes

- Generieren von Unit-Tests

- Erstellen von Codierungsdokumentationen

Empfohlen, diesen Link zu lesen [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)


###  **Microsoft GitHub Copilot Chat @workspace**

Die Referenzierung von **@workspace** im Copilot Chat ermöglicht es Ihnen, Fragen zum gesamten Codebestand zu stellen. Basierend auf der Frage ruft Copilot intelligent relevante Dateien und Symbole ab, die es dann in seiner Antwort als Links und Codebeispiele referenziert.

Um Ihre Frage zu beantworten, durchsucht **@workspace** dieselben Quellen, die ein Entwickler beim Navigieren in einem Codebestand in VS Code verwenden würde:

- Alle Dateien im Workspace, außer Dateien, die durch eine .gitignore-Datei ignoriert werden

- Verzeichnisstruktur mit verschachtelten Ordnern und Dateinamen

- GitHubs Code-Suchindex, falls der Workspace ein GitHub-Repository ist und von der Code-Suche indexiert wurde

- Symbole und Definitionen im Workspace

- Aktuell ausgewählter Text oder sichtbarer Text im aktiven Editor

Hinweis: .gitignore wird umgangen, wenn Sie eine Datei geöffnet haben oder Text in einer ignorierten Datei ausgewählt ist.

Empfohlen, diesen Link zu lesen [[https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)]


## **Erfahren Sie mehr über dieses Labor**

GitHub Copilot hat die Programmier-Effizienz von Unternehmen erheblich verbessert, und jedes Unternehmen möchte die relevanten Funktionen von GitHub Copilot anpassen. Viele Unternehmen haben Erweiterungen ähnlich wie GitHub Copilot basierend auf ihren eigenen Geschäftsszenarien und Open-Source-Modellen angepasst. Für Unternehmen sind angepasste Erweiterungen leichter zu kontrollieren, aber das wirkt sich auch auf die Benutzererfahrung aus. Schließlich verfügt GitHub Copilot über stärkere Funktionen im Umgang mit allgemeinen Szenarien und Professionalität. Wenn die Erfahrung konsistent gehalten werden kann, wäre es besser, die eigene Erweiterung des Unternehmens anzupassen. GitHub Copilot Chat bietet relevante APIs für Unternehmen, um die Chat-Erfahrung zu erweitern. Eine konsistente Erfahrung bei gleichzeitig angepassten Funktionen ist eine bessere Benutzererfahrung.

Dieses Labor verwendet hauptsächlich das Phi-3-Modell kombiniert mit dem lokalen NPU und Azure-Hybrid, um einen benutzerdefinierten Agenten in GitHub Copilot Chat ***@PHI3*** zu erstellen, der Unternehmensentwickler bei der Codegenerierung ***(@PHI3 /gen)*** und der Generierung von Code basierend auf Bildern ***(@PHI3 /img)*** unterstützt.

![PHI3](../../../../../../../translated_images/de/cover.1017ebc9a7c46d09.webp)

### ***Hinweis:*** 

Dieses Labor wird derzeit im AIPC des Intel-CPU und Apple Silicon implementiert. Wir werden die Qualcomm-Version der NPU weiterhin aktualisieren.


## **Labor**


| Name | Beschreibung | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installationen(✅) | Konfigurieren und Installieren der relevanten Umgebungen und Installationswerkzeuge | [Gehe zu](./HOL/AIPC/01.Installations.md) |[Gehe zu](./HOL/Apple/01.Installations.md) |
| Lab1 - Ausführen des Promptflow mit Phi-3-mini (✅) | In Kombination mit AIPC / Apple Silicon wird mit lokalem NPU die Codegenerierung durch Phi-3-mini erstellt | [Gehe zu](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Gehe zu](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deployment von Phi-3-vision auf Azure Machine Learning Service(✅) | Codegenerierung durch Deployment des Model Catalog von Azure Machine Learning Service - Phi-3-vision Image | [Gehe zu](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Gehe zu](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Erstellen eines @phi-3 Agenten in GitHub Copilot Chat(✅)  | Erstellen eines benutzerdefinierten Phi-3-Agenten in GitHub Copilot Chat zur Vervollständigung von Codegenerierung, Grafgenerierungscode, RAG usw. | [Gehe zu](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Gehe zu](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Beispielcode (✅)  | Beispielcode herunterladen | [Gehe zu](../../../../../../../code/07.Lab/01/AIPC) | [Gehe zu](../../../../../../../code/07.Lab/01/Apple) |


## **Ressourcen**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. Mehr über GitHub Copilot erfahren [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. Mehr über GitHub Copilot Chat erfahren [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. Mehr über die GitHub Copilot Chat API erfahren [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Mehr über Microsoft Foundry erfahren [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Mehr über den Model-Katalog von Microsoft Foundry erfahren [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, bitten wir Sie zu beachten, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->