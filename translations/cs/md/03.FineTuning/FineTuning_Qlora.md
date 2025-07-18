<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:20:33+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "cs"
}
-->
**Doladění Phi-3 pomocí QLoRA**

Doladění jazykového modelu Phi-3 Mini od Microsoftu pomocí [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA pomůže zlepšit porozumění konverzaci a generování odpovědí.

Pro načtení modelů ve 4 bitech s transformers a bitsandbytes je potřeba nainstalovat accelerate a transformers ze zdroje a ujistit se, že máte nejnovější verzi knihovny bitsandbytes.

**Ukázky**
- [Více informací v tomto ukázkovém notebooku](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Příklad Python skriptu pro doladění](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Příklad doladění na Hugging Face Hub pomocí LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Příklad doladění na Hugging Face Hub pomocí QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.