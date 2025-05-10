<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "50b6a55a0831b417835087d8b57759fe",
  "translation_date": "2025-05-09T20:47:41+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Lora.md",
  "language_code": "hu"
}
-->
# **Phi-3 finomhangolása Lora-val**

A Microsoft Phi-3 Mini nyelvi modell finomhangolása [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) segítségével egy egyedi chat utasítás adatbázison.

A LoRA javítja a párbeszéd megértését és a válaszok generálását.

## Lépésről lépésre útmutató a Phi-3 Mini finomhangolásához:

**Importálás és beállítás**

loralib telepítése

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Kezdjük a szükséges könyvtárak importálásával, mint a datasets, transformers, peft, trl és torch.  
Állítsuk be a naplózást a tanítási folyamat nyomon követéséhez.

Dönthetsz úgy, hogy néhány réteget lecserélsz a loralib-ben megvalósított megfelelőikre. Jelenleg csak nn.Linear, nn.Embedding és nn.Conv2d támogatott. Támogatjuk továbbá a MergedLinear-t olyan esetekre, amikor egyetlen nn.Linear több réteget képvisel, például az attention qkv vetítés bizonyos megvalósításaiban (lásd További megjegyzések).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

A tanítási ciklus előtt csak a LoRA paramétereket jelöljük meg taníthatóként.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Ellenőrzőpont mentésekor csak a LoRA paramétereket tartalmazó state_dict-et generáljunk.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```  
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Ellenőrzőpont betöltésekor a load_state_dict használatakor állítsuk be a strict=False értéket.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Most már a tanítás a szokásos módon folytatható.

**Hipermparaméterek**

Két szótárat definiáljunk: training_config és peft_config. A training_config tartalmazza a tanításhoz szükséges hipermparamétereket, például a tanulási rátát, a batch méretet és a naplózási beállításokat.

A peft_config a LoRA-hoz kapcsolódó paramétereket határozza meg, mint a rank, dropout és a feladat típusa.

**Modell és Tokenizer betöltése**

Add meg az előre betanított Phi-3 modell elérési útját (pl. "microsoft/Phi-3-mini-4k-instruct"). Állítsd be a modell beállításait, beleértve a cache használatát, az adattípust (bfloat16 a kevert precízióhoz) és az attention megvalósítását.

**Tanítás**

Finomhangold a Phi-3 modellt az egyedi chat utasítás adatbázison. Használd a peft_config-ban megadott LoRA beállításokat a hatékony adaptációhoz. Kövesd nyomon a tanítás előrehaladását a megadott naplózási stratégiával.  
Értékelés és mentés: Értékeld ki a finomhangolt modellt.  
Tanítás közben ments ellenőrzőpontokat a későbbi felhasználáshoz.

**Példák**  
- [További információ ezzel a mintafüzettel](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)  
- [Python finomhangolási példa](../../../../code/03.Finetuning/FineTrainingScript.py)  
- [Hugging Face Hub finomhangolás LORA-val](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)  
- [Hugging Face modellkártya példa - LORA finomhangolás](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)  
- [Hugging Face Hub finomhangolás QLORA-val](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Felelősségkizárás**:  
Ezt a dokumentumot az AI fordítószolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén szakmai emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.