<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9481b07dda8f9715a5d1ff43fb27568b",
  "translation_date": "2025-03-27T07:06:14+00:00",
  "source_file": "md\\01.Introduction\\03\\Android_Inference.md",
  "language_code": "de"
}
-->
# **Inference Phi-3 auf Android**

Lassen Sie uns erkunden, wie Sie Inferenz mit Phi-3-mini auf Android-Geräten durchführen können. Phi-3-mini ist eine neue Modellreihe von Microsoft, die den Einsatz von Large Language Models (LLMs) auf Edge- und IoT-Geräten ermöglicht.

## Semantic Kernel und Inferenz

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) ist ein Anwendungsframework, mit dem Sie Anwendungen erstellen können, die mit Azure OpenAI Service, OpenAI-Modellen und sogar lokalen Modellen kompatibel sind. Wenn Sie neu bei Semantic Kernel sind, empfehlen wir Ihnen, einen Blick in das [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) zu werfen.

### Zugriff auf Phi-3-mini mit Semantic Kernel

Sie können es mit dem Hugging Face Connector in Semantic Kernel kombinieren. Siehe diesen [Beispielcode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Standardmäßig entspricht dies der Modell-ID auf Hugging Face. Sie können jedoch auch eine lokal eingerichtete Phi-3-mini-Modellserver-Verbindung herstellen.

### Aufruf quantisierter Modelle mit Ollama oder LlamaEdge

Viele Nutzer bevorzugen die Verwendung quantisierter Modelle, um Modelle lokal auszuführen. [Ollama](https://ollama.com/) und [LlamaEdge](https://llamaedge.com) ermöglichen es einzelnen Nutzern, verschiedene quantisierte Modelle aufzurufen:

#### Ollama

Sie können `ollama run Phi-3` direkt ausführen oder es offline konfigurieren, indem Sie eine `Modelfile` erstellen, die den Pfad zu Ihrer `.gguf`-Datei enthält.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Beispielcode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Wenn Sie `.gguf`-Dateien gleichzeitig in der Cloud und auf Edge-Geräten verwenden möchten, ist LlamaEdge eine großartige Wahl. Sie können diesen [Beispielcode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) verwenden, um loszulegen.

### Installation und Ausführung auf Android-Telefonen

1. **Laden Sie die MLC Chat-App** (kostenlos) für Android-Telefone herunter.
2. Laden Sie die APK-Datei (148 MB) herunter und installieren Sie sie auf Ihrem Gerät.
3. Starten Sie die MLC Chat-App. Sie sehen eine Liste von KI-Modellen, einschließlich Phi-3-mini.

Zusammenfassend eröffnet Phi-3-mini spannende Möglichkeiten für generative KI auf Edge-Geräten, und Sie können seine Fähigkeiten auf Android erkunden.

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.