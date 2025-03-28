<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1ff728038c4f554b660a36b76cbdd6e",
  "translation_date": "2025-03-27T07:54:12+00:00",
  "source_file": "md\\01.Introduction\\03\\overview.md",
  "language_code": "de"
}
-->
Im Kontext von Phi-3-mini bezieht sich "Inference" auf den Prozess, bei dem das Modell verwendet wird, um Vorhersagen zu treffen oder Ausgaben basierend auf Eingabedaten zu generieren. Hier sind weitere Details zu Phi-3-mini und seinen Fähigkeiten im Bereich Inference.

Phi-3-mini ist Teil der Phi-3-Serie von Modellen, die von Microsoft veröffentlicht wurden. Diese Modelle sind darauf ausgelegt, die Möglichkeiten von Small Language Models (SLMs) neu zu definieren.

Hier sind einige wichtige Punkte zu Phi-3-mini und seinen Inference-Fähigkeiten:

## **Phi-3-mini Überblick:**
- Phi-3-mini hat eine Parametergröße von 3,8 Milliarden.
- Es kann nicht nur auf herkömmlichen Computern, sondern auch auf Edge-Geräten wie Mobilgeräten und IoT-Geräten ausgeführt werden.
- Die Veröffentlichung von Phi-3-mini ermöglicht es Einzelpersonen und Unternehmen, SLMs auf verschiedenen Hardware-Geräten einzusetzen, insbesondere in ressourcenbeschränkten Umgebungen.
- Es unterstützt verschiedene Modellformate, darunter das traditionelle PyTorch-Format, die quantisierte Version des gguf-Formats und die ONNX-basierte quantisierte Version.

## **Zugriff auf Phi-3-mini:**
Um auf Phi-3-mini zuzugreifen, können Sie [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) in einer Copilot-Anwendung verwenden. Semantic Kernel ist im Allgemeinen kompatibel mit Azure OpenAI Service, Open-Source-Modellen auf Hugging Face und lokalen Modellen.
Alternativ können Sie [Ollama](https://ollama.com) oder [LlamaEdge](https://llamaedge.com) nutzen, um quantisierte Modelle aufzurufen. Ollama ermöglicht es Einzelanwendern, verschiedene quantisierte Modelle zu nutzen, während LlamaEdge plattformübergreifende Verfügbarkeit für GGUF-Modelle bietet.

## **Quantisierte Modelle:**
Viele Nutzer bevorzugen quantisierte Modelle für lokale Inference. Beispielsweise können Sie Ollama direkt ausführen, um Phi-3 zu nutzen, oder es offline mit einer Modelfile konfigurieren. Die Modelfile gibt den GGUF-Dateipfad und das Prompt-Format an.

## **Generative KI-Möglichkeiten:**
Die Kombination von SLMs wie Phi-3-mini eröffnet neue Möglichkeiten für generative KI. Inference ist nur der erste Schritt; diese Modelle können für verschiedene Aufgaben in ressourcenbeschränkten, latenzkritischen und kostenoptimierten Szenarien verwendet werden.

## **Generative KI mit Phi-3-mini freischalten: Ein Leitfaden zu Inference und Deployment**  
Erfahren Sie, wie Sie Semantic Kernel, Ollama/LlamaEdge und ONNX Runtime nutzen können, um auf Phi-3-mini-Modelle zuzugreifen und Inference durchzuführen, und entdecken Sie die Möglichkeiten der generativen KI in verschiedenen Anwendungsszenarien.

**Funktionen**  
Inference des Phi-3-mini-Modells in:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Zusammenfassend ermöglicht Phi-3-mini Entwicklern, verschiedene Modellformate zu erkunden und generative KI in unterschiedlichen Anwendungsszenarien zu nutzen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.