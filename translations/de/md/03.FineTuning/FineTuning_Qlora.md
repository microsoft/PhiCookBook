<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:16:30+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "de"
}
-->
**Feinabstimmung von Phi-3 mit QLoRA**

Feinabstimmung des Microsoft Phi-3 Mini-Sprachmodells mit [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA hilft dabei, das Verständnis von Gesprächen und die Generierung von Antworten zu verbessern.

Um Modelle in 4-Bit mit transformers und bitsandbytes zu laden, müssen Sie accelerate und transformers aus dem Quellcode installieren und sicherstellen, dass Sie die neueste Version der bitsandbytes-Bibliothek verwenden.

**Beispiele**
- [Mehr erfahren mit diesem Beispiel-Notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Beispiel für Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Beispiel für Hugging Face Hub Fine Tuning mit LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Beispiel für Hugging Face Hub Fine Tuning mit QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.