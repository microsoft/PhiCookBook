<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-03-27T03:41:26+00:00",
  "source_file": "code\\03.Finetuning\\olive-ort-example\\README.md",
  "language_code": "de"
}
-->
# Fine-Tune Phi3 mit Olive

In diesem Beispiel verwenden Sie Olive, um:

1. Einen LoRA-Adapter zu feintunen, um Phrasen in die Kategorien Traurig, Freude, Angst, Überraschung zu klassifizieren.
1. Die Adapter-Gewichte mit dem Basismodell zu verschmelzen.
1. Das Modell zu optimieren und in `int4` zu quantisieren.

Außerdem zeigen wir Ihnen, wie Sie das feingetunte Modell mit der ONNX Runtime (ORT) Generate API für Inferenz verwenden können.

> **⚠️ Für das Feintuning benötigen Sie eine geeignete GPU, beispielsweise eine A10, V100, A100.**

## 💾 Installation

Erstellen Sie eine neue Python-Umgebung (zum Beispiel mit `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Installieren Sie anschließend Olive und die Abhängigkeiten für den Feintuning-Workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Feintune Phi3 mit Olive
Die [Olive-Konfigurationsdatei](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) enthält einen *Workflow* mit den folgenden *Passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Auf hoher Ebene führt dieser Workflow Folgendes aus:

1. Feintuning von Phi3 (für 150 Schritte, die Sie anpassen können) mit den Daten aus [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Verschmelzung der LoRA-Adapter-Gewichte mit dem Basismodell. Dadurch erhalten Sie ein einzelnes Modellartefakt im ONNX-Format.
1. Der Model Builder optimiert das Modell für die ONNX Runtime *und* quantisiert es in `int4`.

Um den Workflow auszuführen, verwenden Sie:

```bash
olive run --config phrase-classification.json
```

Nachdem Olive abgeschlossen ist, finden Sie Ihr optimiertes `int4` feingetuntes Phi3-Modell hier: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integration des feingetunten Phi3 in Ihre Anwendung 

Um die Anwendung auszuführen:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Die Antwort sollte eine einzelne Wortklassifikation der Phrase sein (Traurig/Freude/Angst/Überraschung).

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.