<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:53:29+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "cs"
}
-->
**Fine-tuning Phi-3 with QLoRA**

Fine-tuning Microsoft’s Phi-3 Mini language model using [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA ayudará a mejorar la comprensión conversacional y la generación de respuestas.

Para cargar modelos en 4 bits con transformers y bitsandbytes, debes instalar accelerate y transformers desde la fuente y asegurarte de tener la versión más reciente de la biblioteca bitsandbytes.

**Samples**
- [Learn More with this sample notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Example of Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Example of Hugging Face Hub Fine Tuning with LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Example of Hugging Face Hub Fine Tuning with QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo mylné výklady vyplývající z použití tohoto překladu.