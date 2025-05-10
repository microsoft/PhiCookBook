<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:53:34+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "sk"
}
-->
**Doladenie Phi-3 pomocou QLoRA**

Doladenie jazykového modelu Phi-3 Mini od Microsoftu pomocou [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA pomáha zlepšiť porozumenie konverzácie a generovanie odpovedí.

Na načítanie modelov v 4 bitoch s knižnicami transformers a bitsandbytes je potrebné nainštalovať accelerate a transformers zo zdrojov a uistiť sa, že máte najnovšiu verziu knižnice bitsandbytes.

**Ukážky**
- [Viac informácií v tomto vzorovom notebooku](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Príklad Python FineTuning vzorky](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Príklad Fine Tuning na Hugging Face Hub s LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Príklad Fine Tuning na Hugging Face Hub s QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.