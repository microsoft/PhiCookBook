<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:20:41+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "sk"
}
-->
**Doladenie Phi-3 pomocou QLoRA**

Doladenie jazykového modelu Phi-3 Mini od Microsoftu pomocou [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA pomôže zlepšiť porozumenie konverzácií a generovanie odpovedí.

Na načítanie modelov v 4 bitoch s knižnicami transformers a bitsandbytes je potrebné nainštalovať accelerate a transformers zo zdroja a uistiť sa, že máte najnovšiu verziu knižnice bitsandbytes.

**Ukážky**
- [Viac informácií v tomto ukážkovom notebooku](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Príklad Python skriptu na doladenie](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Príklad doladenia na Hugging Face Hub pomocou LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Príklad doladenia na Hugging Face Hub pomocou QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.