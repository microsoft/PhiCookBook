Im Kontext von Phi-3-mini bezieht sich Inferenz auf den Prozess, bei dem das Modell verwendet wird, um Vorhersagen zu treffen oder Ausgaben basierend auf Eingabedaten zu erzeugen. Lassen Sie mich Ihnen mehr Details zu Phi-3-mini und seinen Inferenzfähigkeiten geben.

Phi-3-mini ist Teil der Phi-3-Modellreihe, die von Microsoft veröffentlicht wurde. Diese Modelle sind darauf ausgelegt, die Möglichkeiten von Small Language Models (SLMs) neu zu definieren.

Hier sind einige wichtige Punkte zu Phi-3-mini und seinen Inferenzfähigkeiten:

## **Phi-3-mini Überblick:**
- Phi-3-mini hat eine Parametergröße von 3,8 Milliarden.
- Es kann nicht nur auf herkömmlichen Rechengeräten, sondern auch auf Edge-Geräten wie Mobilgeräten und IoT-Geräten ausgeführt werden.
- Die Veröffentlichung von Phi-3-mini ermöglicht es Einzelpersonen und Unternehmen, SLMs auf verschiedenen Hardwaregeräten einzusetzen, insbesondere in ressourcenbeschränkten Umgebungen.
- Es unterstützt verschiedene Modellformate, darunter das traditionelle PyTorch-Format, die quantisierte Version des gguf-Formats und die ONNX-basierte quantisierte Version.

## **Zugriff auf Phi-3-mini:**
Um auf Phi-3-mini zuzugreifen, können Sie [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) in einer Copilot-Anwendung verwenden. Semantic Kernel ist im Allgemeinen kompatibel mit Azure OpenAI Service, Open-Source-Modellen auf Hugging Face und lokalen Modellen.  
Sie können auch [Ollama](https://ollama.com) oder [LlamaEdge](https://llamaedge.com) nutzen, um quantisierte Modelle aufzurufen. Ollama ermöglicht es einzelnen Nutzern, verschiedene quantisierte Modelle zu verwenden, während LlamaEdge plattformübergreifende Verfügbarkeit für GGUF-Modelle bietet.

## **Quantisierte Modelle:**
Viele Nutzer bevorzugen quantisierte Modelle für lokale Inferenz. Zum Beispiel können Sie Ollama direkt verwenden, um Phi-3 auszuführen, oder es offline mit einer Modelfile konfigurieren. Die Modelfile gibt den Pfad zur GGUF-Datei und das Prompt-Format an.

## **Möglichkeiten der generativen KI:**
Die Kombination von SLMs wie Phi-3-mini eröffnet neue Möglichkeiten für generative KI. Inferenz ist nur der erste Schritt; diese Modelle können für verschiedene Aufgaben in ressourcenbeschränkten, latenzgebundenen und kostenbewussten Szenarien eingesetzt werden.

## **Generative KI mit Phi-3-mini freischalten: Ein Leitfaden für Inferenz und Deployment**  
Erfahren Sie, wie Sie Semantic Kernel, Ollama/LlamaEdge und ONNX Runtime nutzen, um auf Phi-3-mini-Modelle zuzugreifen und Inferenz durchzuführen, und entdecken Sie die Möglichkeiten generativer KI in verschiedenen Anwendungsszenarien.

**Funktionen**  
Inferenz des phi3-mini Modells in:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)  
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)  
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)  
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)  
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)  

Zusammenfassend ermöglicht Phi-3-mini Entwicklern, verschiedene Modellformate zu erkunden und generative KI in unterschiedlichen Anwendungsszenarien zu nutzen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.