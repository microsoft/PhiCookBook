<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-03-27T03:59:50+00:00",
  "source_file": "code\\04.Finetuning\\olive-ort-example\\README.md",
  "language_code": "de"
}
-->
# Fine-Tune Phi3 mit Olive

In diesem Beispiel wirst du Olive verwenden, um:

1. Einen LoRA-Adapter zu trainieren, der Phrasen in Sad, Joy, Fear, Surprise klassifiziert.
1. Die Adapter-Gewichte mit dem Basismodell zu verschmelzen.
1. Das Modell zu optimieren und in `int4` zu quantisieren.

Außerdem zeigen wir dir, wie du das feinabgestimmte Modell mit der ONNX Runtime (ORT) Generate API inferieren kannst.

> **⚠️ Für das Fine-Tuning benötigst du eine geeignete GPU - zum Beispiel eine A10, V100, A100.**

## 💾 Installation

Erstelle eine neue Python-Umgebung (zum Beispiel mit `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Installiere anschließend Olive und die Abhängigkeiten für den Fine-Tuning-Workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Phi3 mit Olive Fine-Tunen

Die [Olive-Konfigurationsdatei](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) enthält einen *Workflow* mit den folgenden *Passes*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Auf hoher Ebene führt dieser Workflow folgende Schritte aus:

1. Fine-Tune Phi3 (für 150 Schritte, die du anpassen kannst) mit den Daten aus [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Die LoRA-Adapter-Gewichte werden mit dem Basismodell verschmolzen. Dies erzeugt ein einzelnes Modellartefakt im ONNX-Format.
1. Der Model Builder optimiert das Modell für die ONNX Runtime *und* quantisiert das Modell in `int4`.

Um den Workflow auszuführen, verwende:

```bash
olive run --config phrase-classification.json
```

Sobald Olive abgeschlossen ist, steht dir dein optimiertes `int4` feinabgestimmtes Phi3-Modell unter folgendem Pfad zur Verfügung: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Integration des feinabgestimmten Phi3 in deine Anwendung 

Um die Anwendung auszuführen:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Die Antwort sollte eine Einzelwort-Klassifikation der Phrase sein (Sad/Joy/Fear/Surprise).

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.