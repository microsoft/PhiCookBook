# **Phi-3 finomhangolása Lora segítségével**

A Microsoft Phi-3 Mini nyelvi modelljének finomhangolása [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) használatával egy egyedi chat utasítás adatbázison.

A LORA segít javítani a beszélgetések megértését és a válaszok generálását.

## Lépésről lépésre útmutató a Phi-3 Mini finomhangolásához:

**Importálás és beállítás**

loralib telepítése

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Kezdésként importáljuk a szükséges könyvtárakat, mint a datasets, transformers, peft, trl és torch.
Állítsuk be a naplózást, hogy nyomon követhessük a tanulási folyamatot.

Választhatjuk, hogy bizonyos rétegeket lecserélünk loralib-ben megvalósított megfelelőikre. Jelenleg csak nn.Linear, nn.Embedding és nn.Conv2d támogatott. Továbbá támogatjuk a MergedLinear-t olyan esetekre, amikor egyetlen nn.Linear több réteget képvisel, például az attention qkv projekció egyes megvalósításaiban (lásd a További megjegyzéseket).

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

A tanulási ciklus megkezdése előtt csak a LoRA paramétereket jelöljük meg taníthatónak.

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

Most már a tanulás a szokásos módon folytatható.

**Hipermparaméterek**

Két szótárat definiáljunk: training_config és peft_config. A training_config tartalmazza a tanuláshoz szükséges hipermparamétereket, mint a tanulási ráta, batch méret és naplózási beállítások.

A peft_config a LoRA-hoz kapcsolódó paramétereket határozza meg, például a rangot, dropoutot és a feladat típusát.

**Modell és Tokenizer betöltése**

Adjuk meg az előre betanított Phi-3 modell elérési útját (pl. "microsoft/Phi-3-mini-4k-instruct"). Állítsuk be a modell beállításait, beleértve a cache használatát, az adattípust (bfloat16 a vegyes precizitáshoz) és az attention megvalósítást.

**Tanítás**

Finomhangoljuk a Phi-3 modellt az egyedi chat utasítás adatbázison. Használjuk a peft_config-ban megadott LoRA beállításokat a hatékony adaptációhoz. Kövessük nyomon a tanulás előrehaladását a megadott naplózási stratégia szerint.
Értékelés és mentés: Értékeljük a finomhangolt modellt.
Mentjük az ellenőrzőpontokat a tanulás során későbbi felhasználásra.

**Minták**
- [További információk ezzel a mintanotebookkal](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Python finomhangolási minta példa](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face Hub finomhangolás LORA-val példa](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face modellkártya példa - LORA finomhangolási minta](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Hugging Face Hub finomhangolás QLORA-val példa](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.