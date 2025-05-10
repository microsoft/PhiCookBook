<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:54:01+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "sl"
}
-->
**Fine-tuning Phi-3 s QLoRA**

Fine-tuning Microsoftovega jezikovnega modela Phi-3 Mini z uporabo [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA bo pomagal izboljšati razumevanje pogovorov in generiranje odgovorov.

Za nalaganje modelov v 4bitih z uporabo transformers in bitsandbytes morate namestiti accelerate in transformers iz vira ter poskrbeti, da imate najnovejšo različico knjižnice bitsandbytes.

**Vzorce**
- [Več informacij s tem vzorčnim zvezkom](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Primer Python FineTuning vzorca](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Primer Fine Tuning z LORA na Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Primer Fine Tuning z QLORA na Hugging Face Hub](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.