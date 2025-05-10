<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:53:50+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "sr"
}
-->
**Fino podešavanje Phi-3 pomoću QLoRA**

Fino podešavanje Microsoftovog Phi-3 Mini jezičkog modela korišćenjem [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA pomaže u poboljšanju razumevanja konverzacije i generisanja odgovora.

Da biste učitali modele u 4bita koristeći transformers i bitsandbytes, potrebno je da instalirate accelerate i transformers iz izvora i da se uverite da imate najnoviju verziju biblioteke bitsandbytes.

**Primeri**
- [Saznajte više sa ovim primerom beležnice](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Primer Python FineTuning skripte](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Primer Fine Tuning-a na Hugging Face Hub sa LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Primer Fine Tuning-a na Hugging Face Hub sa QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korišćenjem AI prevodilačke usluge [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo tačnosti, imajte na umu da automatski prevodi mogu sadržavati greške ili netačnosti. Originalni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prevod. Ne snosimo odgovornost za bilo kakva nesporazumevanja ili pogrešna tumačenja koja proisteknu iz korišćenja ovog prevoda.