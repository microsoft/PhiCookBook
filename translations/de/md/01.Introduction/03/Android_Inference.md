# **Inference Phi-3 auf Android**

Lassen Sie uns erkunden, wie Sie Inferenz mit Phi-3-mini auf Android-Geräten durchführen können. Phi-3-mini ist eine neue Modellreihe von Microsoft, die die Bereitstellung von Large Language Models (LLMs) auf Edge- und IoT-Geräten ermöglicht.

## Semantic Kernel und Inferenz

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) ist ein Anwendungsframework, das Ihnen ermöglicht, Anwendungen zu erstellen, die mit Azure OpenAI Service, OpenAI-Modellen und sogar lokalen Modellen kompatibel sind. Wenn Sie neu bei Semantic Kernel sind, empfehlen wir Ihnen, sich das [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) anzusehen.

### Zugriff auf Phi-3-mini mit Semantic Kernel

Sie können es mit dem Hugging Face Connector im Semantic Kernel kombinieren. Siehe hierzu diesen [Beispielcode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Standardmäßig entspricht dies der Modell-ID auf Hugging Face. Sie können jedoch auch eine lokal erstellte Phi-3-mini Modelserver anbinden.

### Aufruf quantisierter Modelle mit Ollama oder LlamaEdge

Viele Nutzer bevorzugen quantisierte Modelle, um Modelle lokal laufen zu lassen. [Ollama](https://ollama.com/) und [LlamaEdge](https://llamaedge.com) ermöglichen es einzelnen Nutzern, verschiedene quantisierte Modelle aufzurufen:

#### Ollama

Sie können `ollama run Phi-3` direkt ausführen oder es offline konfigurieren, indem Sie eine `Modelfile` mit dem Pfad zu Ihrer `.gguf` Datei erstellen.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Beispielcode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Wenn Sie `.gguf` Dateien gleichzeitig in der Cloud und auf Edge-Geräten verwenden möchten, ist LlamaEdge eine ausgezeichnete Wahl. Sie können sich an diesem [Beispielcode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) orientieren, um loszulegen.

### Installation und Ausführung auf Android-Handys

1. **Laden Sie die MLC Chat-App** (kostenlos) für Android-Handys herunter.
2. Laden Sie die APK-Datei (148MB) herunter und installieren Sie sie auf Ihrem Gerät.
3. Starten Sie die MLC Chat-App. Sie sehen eine Liste von KI-Modellen, einschließlich Phi-3-mini.

### Führen Sie Phi-4-mini-reasoning mit LiteRT-LM aus

[Phi-4-mini-reasoning](https://huggingface.co/litert-community/Phi-4-mini-reasoning) ist als gemeinschaftlich konvertiertes int4 `.litertlm` Bundle für Googles On-Device-Runtime [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) verfügbar. Auf Android läuft es auf CPU oder GPU über die [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) App (Import des Bundles von Hugging Face innerhalb der App) oder über die LiteRT-LM Kotlin-API; dasselbe Bundle läuft auch auf iOS, macOS, Linux und Windows. Die Modellkarte listet die gemessenen Geschwindigkeiten und die Ausführungsbefehle auf.

Zusammenfassend eröffnet Phi-3-mini spannende Möglichkeiten für generative KI auf Edge-Geräten, und Sie können seine Fähigkeiten auf Android erkunden.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->