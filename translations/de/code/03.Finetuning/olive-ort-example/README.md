<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-07T10:17:50+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "de"
}
-->
# Feinabstimmung von Phi3 mit Olive

In diesem Beispiel verwendest du Olive, um:

1. Einen LoRA-Adapter feinzujustieren, der Phrasen in Sad, Joy, Fear, Surprise klassifiziert.
1. Die Adapter-Gewichte in das Basismodell zu integrieren.
1. Das Modell zu optimieren und in `int4` zu quantisieren.

Wir zeigen dir außerdem, wie du das feinabgestimmte Modell mit der ONNX Runtime (ORT) Generate API ausführen kannst.

> **⚠️ Für die Feinabstimmung benötigst du eine geeignete GPU – zum Beispiel eine A10, V100 oder A100.**

## 💾 Installation

Erstelle eine neue Python-virtuelle Umgebung (zum Beispiel mit `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Installiere anschließend Olive und die Abhängigkeiten für den Feinabstimmungs-Workflow:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Feinabstimmung von Phi3 mit Olive
Die [Olive-Konfigurationsdatei](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) enthält einen *Workflow* mit den folgenden *Schritten*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Auf hoher Ebene führt dieser Workflow Folgendes aus:

1. Feinabstimmung von Phi3 (für 150 Schritte, die du anpassen kannst) mit den Daten aus [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Integration der LoRA-Adapter-Gewichte in das Basismodell. Dadurch erhältst du ein einzelnes Modell-Artefakt im ONNX-Format.
1. ModelBuilder optimiert das Modell für die ONNX Runtime *und* quantisiert das Modell in `int4`.

Um den Workflow auszuführen, verwende:

```bash
olive run --config phrase-classification.json
```

Nach Abschluss von Olive findest du dein optimiertes, feinabgestimmtes `int4` Phi3-Modell unter: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Feinabgestimmtes Phi3 in deine Anwendung integrieren

Um die App auszuführen:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Die Antwort sollte eine einzelne Wortklassifikation der Phrase sein (Sad/Joy/Fear/Surprise).

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.