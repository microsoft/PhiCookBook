<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bcf5dd7031db0031abdb9dd0c05ba118",
  "translation_date": "2025-07-16T20:54:58+00:00",
  "source_file": "md/01.Introduction/03/Local_Server_Inference.md",
  "language_code": "de"
}
-->
# **Inference Phi-3 auf lokalem Server**

Wir können Phi-3 auf einem lokalen Server bereitstellen. Nutzer können sich für die Lösungen von [Ollama](https://ollama.com) oder [LM Studio](https://llamaedge.com) entscheiden oder ihren eigenen Code schreiben. Phi-3s lokale Dienste lassen sich über [Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo) oder [Langchain](https://www.langchain.com/) anbinden, um Copilot-Anwendungen zu erstellen.

## **Semantic Kernel zur Nutzung von Phi-3-mini**

In der Copilot-Anwendung erstellen wir Anwendungen über Semantic Kernel / LangChain. Dieses Anwendungsframework ist im Allgemeinen kompatibel mit Azure OpenAI Service / OpenAI-Modellen und unterstützt auch Open-Source-Modelle auf Hugging Face sowie lokale Modelle. Was tun, wenn wir Semantic Kernel nutzen wollen, um auf Phi-3-mini zuzugreifen? Am Beispiel von .NET können wir es mit dem Hugging Face Connector im Semantic Kernel kombinieren. Standardmäßig entspricht dieser der Modell-ID auf Hugging Face (beim ersten Gebrauch wird das Modell von Hugging Face heruntergeladen, was einige Zeit in Anspruch nimmt). Alternativ kann man sich auch mit dem selbst aufgebauten lokalen Dienst verbinden. Wir empfehlen Letzteres, da es eine höhere Autonomie bietet, besonders bei Unternehmenseinsätzen.

![sk](../../../../../translated_images/de/sk.d03785c25edc6d44.png)

Aus der Abbildung wird deutlich, dass der Zugriff auf lokale Dienste über Semantic Kernel eine einfache Verbindung zum selbst erstellten Phi-3-mini Modellserver ermöglicht. Hier das Ergebnis der Ausführung:

![skrun](../../../../../translated_images/de/skrun.5aafc1e7197dca20.png)

***Beispielcode*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.