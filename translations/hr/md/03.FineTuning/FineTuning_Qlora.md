<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:53:55+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "hr"
}
-->
**Fine-tuning Phi-3 with QLoRA**

Fino podešavanje Microsoftovog jezičnog modela Phi-3 Mini koristeći [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA pomaže u poboljšanju razumijevanja razgovora i generiranju odgovora.

Za učitavanje modela u 4bita s transformers i bitsandbytes, potrebno je instalirati accelerate i transformers iz izvornog koda te provjeriti imate li najnoviju verziju bitsandbytes biblioteke.

**Samples**
- [Learn More with this sample notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Example of Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Example of Hugging Face Hub Fine Tuning with LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Example of Hugging Face Hub Fine Tuning with QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je pomoću AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.