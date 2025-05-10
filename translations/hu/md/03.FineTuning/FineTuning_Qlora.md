<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-05-09T21:53:23+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "hu"
}
-->
**Phi-3 finomhangolása QLoRA-val**

A Microsoft Phi-3 Mini nyelvi modelljének finomhangolása a [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) segítségével.

A QLoRA javítja a párbeszédértést és a válaszgenerálást.

Ahhoz, hogy 4 bites modelleket tölts be a transformers és bitsandbytes segítségével, telepítened kell az accelerate és transformers csomagokat forrásból, és győződj meg róla, hogy a bitsandbytes könyvtár legfrissebb verzióját használod.

**Minták**
- [Tudj meg többet erről a mintafüzetből](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python finomhangolási minta példája](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub LORA finomhangolási példa](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub QLORA finomhangolási példa](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Nyilatkozat**:  
Ezt a dokumentumot az AI fordítószolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum anyanyelvű változata tekintendő hiteles forrásnak. Kritikus információk esetén professzionális, emberi fordítást javaslunk. Nem vállalunk felelősséget az ezen fordítás használatából eredő félreértésekért vagy félreértelmezésekért.