<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4164123a700fecd535d850f09506d72a",
  "translation_date": "2025-05-09T04:33:51+00:00",
  "source_file": "code/03.Finetuning/olive-ort-example/README.md",
  "language_code": "hu"
}
-->
# Phi3 finomhangolása Olive-dal

Ebben a példában az Olive segítségével:

1. Finomhangolunk egy LoRA adaptert, hogy a kifejezéseket Sad, Joy, Fear, Surprise kategóriákba sorolja.
1. Egyesítjük az adapter súlyait az alapmodellbe.
1. Optimalizáljuk és kvantáljuk a modellt `int4` formátumba.

Megmutatjuk azt is, hogyan lehet az ONNX Runtime (ORT) Generate API segítségével lekérdezni a finomhangolt modellt.

> **⚠️ Finomhangoláshoz megfelelő GPU szükséges, például A10, V100, A100.**

## 💾 Telepítés

Hozz létre egy új Python virtuális környezetet (például `conda` használatával):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Ezután telepítsd az Olive-t és a finomhangoláshoz szükséges függőségeket:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Phi3 finomhangolása Olive-dal
Az [Olive konfigurációs fájl](../../../../../code/03.Finetuning/olive-ort-example/phrase-classification.json) egy *workflow*-t tartalmaz a következő *lépésekkel*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Magyarán a folyamat:

1. Finomhangolja a Phi3-at (150 lépésig, amit módosíthatsz) a [dataset/data-classification.json](../../../../../code/03.Finetuning/olive-ort-example/dataset/dataset-classification.json) adatok alapján.
1. Egyesíti a LoRA adapter súlyait az alapmodellbe, így egyetlen ONNX formátumú modell jön létre.
1. A Model Builder optimalizálja a modellt az ONNX runtime-hoz *és* kvantálja `int4` formátumba.

A workflow futtatásához használd:

```bash
olive run --config phrase-classification.json
```

Amikor az Olive befejezte, az optimalizált `int4` finomhangolt Phi3 modell elérhető itt: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Finomhangolt Phi3 integrálása az alkalmazásodba

Az alkalmazás futtatásához:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

A válasznak egyetlen szó szerinti osztályozásnak kell lennie a kifejezésre (Sad/Joy/Fear/Surprise).

**Felelősségkizárás**:  
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum az anyanyelvén tekintendő hivatalos forrásnak. Kritikus információk esetén szakmai, emberi fordítást javasolunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.