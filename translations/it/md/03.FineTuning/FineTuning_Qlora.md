<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:51:56+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "it"
}
-->
**Fine-tuning di Phi-3 con QLoRA**

Fine-tuning del modello linguistico Phi-3 Mini di Microsoft utilizzando [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA aiuta a migliorare la comprensione delle conversazioni e la generazione delle risposte.

Per caricare modelli in 4 bit con transformers e bitsandbytes, è necessario installare accelerate e transformers dalla sorgente e assicurarsi di avere l’ultima versione della libreria bitsandbytes.

**Esempi**
- [Scopri di più con questo notebook di esempio](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Esempio di FineTuning in Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Esempio di Fine Tuning su Hugging Face Hub con LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Esempio di Fine Tuning su Hugging Face Hub con QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale umana. Non ci assumiamo alcuna responsabilità per malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.