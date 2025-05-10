<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-05-09T21:49:51+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "hu"
}
-->
# Phi-3-Vision-128K-Instruct Projekt áttekintése

## A modell

A Phi-3-Vision-128K-Instruct egy könnyű, korszerű multimodális modell, amely ennek a projektnek a központi eleme. A Phi-3 modellcsalád része, és akár 128 000 token hosszúságú kontextust is támogat. A modellt egy sokszínű adathalmazon képezték, amely szintetikus adatokat és gondosan szűrt, nyilvánosan elérhető weboldalakat tartalmaz, különös hangsúlyt fektetve a magas minőségű, következtetés-igényes tartalomra. A tanítási folyamat magában foglalta a felügyelt finomhangolást és a közvetlen preferencia optimalizálást, hogy pontosan kövesse az utasításokat, valamint erős biztonsági intézkedéseket.

## Mintaadatok létrehozása több okból is fontos:

1. **Tesztelés**: A mintaadatok lehetővé teszik az alkalmazás különböző helyzetek alatti tesztelését anélkül, hogy a valós adatokat érintenék. Ez különösen fontos a fejlesztés és a tesztelési fázisokban.

2. **Teljesítményhangolás**: Olyan mintaadatokkal, amelyek a valós adatok méretét és összetettségét utánozzák, azonosíthatók a teljesítmény szűk keresztmetszetei, és ennek megfelelően optimalizálható az alkalmazás.

3. **Prototípus készítés**: A mintaadatok segítségével prototípusok és vázlatok hozhatók létre, amelyek segítenek a felhasználói igények megértésében és visszajelzés gyűjtésében.

4. **Adat elemzés**: Az adat tudományban a mintaadatokat gyakran használják felfedező adat elemzéshez, modell tanításhoz és algoritmus teszteléshez.

5. **Biztonság**: Fejlesztési és tesztelési környezetben mintaadatok használata segít elkerülni a valós, érzékeny adatok véletlen kiszivárgását.

6. **Tanulás**: Ha új technológiát vagy eszközt tanulsz, a mintaadatokkal való munka gyakorlati lehetőséget nyújt a tanultak alkalmazására.

Ne feledd, a mintaadatok minősége jelentősen befolyásolhatja ezeket a tevékenységeket. Lehetőleg minél közelebb kell állnia a valós adatokhoz szerkezet és változatosság szempontjából.

### Mintaadat létrehozása
[Generate DataSet Script](./CreatingSampleData.md)

## Adathalmaz

Jó példa egy mintaadat-halmazra a [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (elérhető a Huggingface-en).  
A Burberry termékek mintaadatai a termékkategóriára, árra és címre vonatkozó metaadatokkal együtt, összesen 3040 sorral, mindegyik egyedi terméket képvisel. Ez az adathalmaz lehetővé teszi, hogy teszteljük a modell képességét a vizuális adatok megértésére és értelmezésére, leíró szöveget generálva, amely részletes vizuális jellemzőket és márkára jellemző tulajdonságokat ragad meg.

**Megjegyzés:** Használhatsz bármilyen képeket tartalmazó adathalmazt.

## Összetett következtetés

A modellnek árakról és elnevezésekről kell következtetnie kizárólag a kép alapján. Ez megköveteli, hogy ne csak felismerje a vizuális jellemzőket, hanem megértse azok jelentőségét a termék értéke és márkája szempontjából. Azáltal, hogy pontos szöveges leírásokat állít elő képekből, a projekt kiemeli a vizuális adatok integrálásának lehetőségét a modellek teljesítményének és sokoldalúságának növelésére a valós alkalmazásokban.

## Phi-3 Vision architektúra

A modell architektúrája a Phi-3 multimodális változata. Mind szöveges, mind képi adatokat feldolgoz, és ezeket az inputokat egy egységes sorozatba integrálja az átfogó megértés és generálás érdekében. A modell külön beágyazási rétegeket használ szöveg és kép számára. A szöveges tokeneket sűrű vektorokká alakítja, míg a képeket egy CLIP vision modell dolgozza fel, hogy jellemző beágyazásokat nyerjen. Ezeket a képbeágyazásokat aztán úgy vetíti át, hogy illeszkedjenek a szövegbeágyazások dimenzióihoz, biztosítva a zökkenőmentes integrációt.

## Szöveg- és képbeágyazások integrációja

A szövegsorozaton belüli speciális tokenek jelzik, hol kell beilleszteni a képbeágyazásokat. Feldolgozás közben ezek a speciális tokenek a megfelelő képbeágyazásokkal helyettesítődnek, lehetővé téve, hogy a modell szöveget és képeket egyetlen sorozatként kezeljen. Az adataink promptja a speciális <|image|> token használatával van formázva, az alábbi módon:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Minta kód
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Nyilatkozat**:  
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum az anyanyelvén tekintendő hivatalos forrásnak. Kritikus információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből eredő félreértésekért vagy félreértelmezésekért.