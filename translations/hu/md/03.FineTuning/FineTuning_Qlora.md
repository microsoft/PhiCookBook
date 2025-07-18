<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-07-17T08:20:25+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "hu"
}
-->
**Phi-3 finomhangolása QLoRA-val**

A Microsoft Phi-3 Mini nyelvi modelljének finomhangolása a [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora) segítségével.

A QLoRA javítja a párbeszédek megértését és a válaszgenerálást.

Ahhoz, hogy 4 bites modelleket tölts be a transformers és bitsandbytes könyvtárakkal, telepítened kell az accelerate és transformers csomagokat forrásból, és győződj meg róla, hogy a bitsandbytes könyvtár legfrissebb verzióját használod.

**Minták**
- [Tudj meg többet erről a mintapéldányról](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python finomhangolási minta példa](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub finomhangolás LORA-val példa](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub finomhangolás QLORA-val példa](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.