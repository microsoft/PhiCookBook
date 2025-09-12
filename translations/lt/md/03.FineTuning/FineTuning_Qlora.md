<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "54b6b824568d4decb574b9e117c4f5f7",
  "translation_date": "2025-09-12T14:43:28+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Qlora.md",
  "language_code": "lt"
}
-->
**Phi-3 modelio pritaikymas naudojant QLoRA**

Microsoft Phi-3 Mini kalbos modelio pritaikymas naudojant [QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora).

QLoRA padės pagerinti pokalbių supratimą ir atsakymų generavimą.

Norint įkelti modelius 4 bitų formatu naudojant transformers ir bitsandbytes, reikia įdiegti accelerate ir transformers iš šaltinio kodo bei įsitikinti, kad turite naujausią bitsandbytes bibliotekos versiją.

**Pavyzdžiai**
- [Sužinokite daugiau naudodami šį pavyzdinį užrašų knygelės failą](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python pritaikymo pavyzdžio scenarijus](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub pritaikymo su LORA pavyzdys](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face Hub pritaikymo su QLORA pavyzdys](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.