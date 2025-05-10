<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:53:39+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "ro"
}
-->
**Fine-tuning Phi-3 cu QLoRA**

Fine-tuning al modelului de limbaj Phi-3 Mini de la Microsoft folosind [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA va ajuta la îmbunătățirea înțelegerii conversaționale și generării răspunsurilor.

Pentru a încărca modelele în 4 biți cu transformers și bitsandbytes, trebuie să instalezi accelerate și transformers din sursă și să te asiguri că ai cea mai recentă versiune a bibliotecii bitsandbytes.

**Exemple**
- [Află mai multe cu acest notebook exemplu](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exemplu de FineTuning Python](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Exemplu de Fine Tuning Hugging Face Hub cu LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Exemplu de Fine Tuning Hugging Face Hub cu QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.