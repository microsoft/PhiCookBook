<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:21:10+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "hr"
}
-->
**Fino podešavanje Phi-3 s QLoRA**

Fino podešavanje Microsoftovog jezičnog modela Phi-3 Mini koristeći [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA će pomoći u poboljšanju razumijevanja razgovora i generiranju odgovora.

Za učitavanje modela u 4bita s transformers i bitsandbytes, potrebno je instalirati accelerate i transformers iz izvornog koda te osigurati da imate najnoviju verziju biblioteke bitsandbytes.

**Primjeri**
- [Saznajte više s ovim uzorkom bilježnice](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Primjer Python uzorka za fino podešavanje](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Primjer fino podešavanja s Hugging Face Hub koristeći LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Primjer fino podešavanja s Hugging Face Hub koristeći QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.