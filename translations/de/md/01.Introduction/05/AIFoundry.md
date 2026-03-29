# **Verwendung von Microsoft Foundry zur Bewertung**

![aistudo](../../../../../translated_images/de/AIFoundry.9e0b513e999a1c5a.webp)

Wie Sie Ihre generative KI-Anwendung mit [Microsoft Foundry](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) bewerten. Egal, ob Sie Einzel- oder Mehrfachgespräche bewerten, Microsoft Foundry bietet Werkzeuge zur Bewertung der Modellleistung und Sicherheit.

![aistudo](../../../../../translated_images/de/AIPortfolio.69da59a8e1eaa70f.webp)

## So bewerten Sie generative KI-Apps mit Microsoft Foundry
Für ausführlichere Anleitungen siehe die [Microsoft Foundry Dokumentation](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo)

Hier sind die Schritte, um zu beginnen:

## Bewertung generativer KI-Modelle in Microsoft Foundry

**Voraussetzungen**

- Ein Testdatensatz im CSV- oder JSON-Format.
- Ein bereitgestelltes generatives KI-Modell (wie Phi-3, GPT 3.5, GPT 4 oder Davinci-Modelle).
- Eine Laufzeit mit einer Compute-Instanz, um die Bewertung durchzuführen.

## Eingebaute Bewertungsmetriken

Microsoft Foundry ermöglicht die Bewertung sowohl von Einzel- als auch von komplexen Mehrfachgesprächen.
Für Retrieval Augmented Generation (RAG)-Szenarien, bei denen das Modell auf spezifischen Daten basiert, können Sie die Leistung mit eingebauten Bewertungsmetriken beurteilen.
Zusätzlich können Sie allgemeine Einzel-Fragen-Antwort-Szenarien (nicht-RAG) bewerten.

## Erstellen eines Bewertungsdurchlaufs

Navigieren Sie in der Microsoft Foundry-Benutzeroberfläche entweder zur Bewertungsseite oder zur Prompt Flow-Seite.
Folgen Sie dem Assistenten zur Erstellung der Bewertung, um einen Bewertungsdurchlauf einzurichten. Geben Sie optional einen Namen für Ihre Bewertung an.
Wählen Sie das Szenario, das zu den Zielen Ihrer Anwendung passt.
Wählen Sie eine oder mehrere Bewertungsmetriken aus, um die Ausgabe des Modells zu beurteilen.

## Benutzerdefinierter Bewertungsablauf (optional)

Für mehr Flexibilität können Sie einen benutzerdefinierten Bewertungsablauf einrichten. Passen Sie den Bewertungsprozess an Ihre spezifischen Anforderungen an.

## Ergebnisse ansehen

Nach dem Ausführen der Bewertung können Sie detaillierte Bewertungsmetriken in Microsoft Foundry protokollieren, ansehen und analysieren. Gewinnen Sie Einblicke in die Fähigkeiten und Grenzen Ihrer Anwendung.

**Hinweis** Microsoft Foundry befindet sich derzeit in der öffentlichen Vorschauphase, verwenden Sie es daher für Experimente und Entwicklungszwecke. Für produktive Workloads sollten Sie andere Optionen in Betracht ziehen. Erkunden Sie die offizielle [AI Foundry-Dokumentation](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) für weitere Details und Schritt-für-Schritt-Anleitungen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir Genauigkeit anstreben, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Verwendung dieser Übersetzung ergeben.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->