<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-03-27T15:07:57+00:00",
  "source_file": "md\\03.FineTuning\\FineTuning_Qlora.md",
  "language_code": "de"
}
-->
**Feinabstimmung von Phi-3 mit QLoRA**

Feinabstimmung von Microsofts Phi-3 Mini Sprachmodell mithilfe von [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora). 

QLoRA wird helfen, das Verständnis für Gespräche und die Generierung von Antworten zu verbessern. 

Um Modelle in 4-Bit mit transformers und bitsandbytes zu laden, müssen Sie accelerate und transformers aus dem Quellcode installieren und sicherstellen, dass Sie die neueste Version der bitsandbytes-Bibliothek verwenden.

**Beispiele**
- [Erfahren Sie mehr mit diesem Beispiel-Notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Beispiel eines Python FineTuning Scripts](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Beispiel für Hugging Face Hub Feinabstimmung mit LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Beispiel für Hugging Face Hub Feinabstimmung mit QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.