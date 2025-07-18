<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e0a07fd2a30fe2af30b1373df207a5bf",
  "translation_date": "2025-07-17T08:13:28+00:00",
  "source_file": "md/03.FineTuning/FineTuning_Phi-3-visionWandB.md",
  "language_code": "hu"
}
-->
# Phi-3-Vision-128K-Instruct Projekt Áttekintés

## A Modell

A Phi-3-Vision-128K-Instruct egy könnyű, csúcstechnológiás multimodális modell, amely ennek a projektnek a központi eleme. A Phi-3 modellcsalád része, és akár 128 000 token hosszúságú kontextust is támogat. A modellt egy sokszínű adathalmazon képezték, amely szintetikus adatokat és gondosan szűrt, nyilvánosan elérhető weboldalakat tartalmaz, különös hangsúlyt fektetve a magas minőségű, érvelést igénylő tartalmakra. A tanítási folyamat magában foglalta a felügyelt finomhangolást és a közvetlen preferencia-optimalizálást, hogy pontosan kövesse az utasításokat, valamint erős biztonsági intézkedéseket alkalmaztak.

## Mintaadatok létrehozása több okból is kulcsfontosságú:

1. **Tesztelés**: A mintaadatok lehetővé teszik, hogy különböző helyzetekben teszteld az alkalmazásodat anélkül, hogy a valós adatokat érintenéd. Ez különösen fontos a fejlesztési és tesztelési fázisokban.

2. **Teljesítményhangolás**: Olyan mintaadatokkal, amelyek hasonlítanak a valós adatok méretére és összetettségére, azonosíthatod a teljesítménybeli szűk keresztmetszeteket, és optimalizálhatod az alkalmazást.

3. **Prototípus készítés**: A mintaadatok segítségével prototípusokat és vázlatokat készíthetsz, amelyek segítenek megérteni a felhasználói igényeket és visszajelzést gyűjteni.

4. **Adat elemzés**: Az adat tudományban a mintaadatokat gyakran használják felfedező adat elemzéshez, modellképzéshez és algoritmus teszteléshez.

5. **Biztonság**: Fejlesztési és tesztelési környezetben mintaadatok használata segít megelőzni a valós, érzékeny adatok véletlen kiszivárgását.

6. **Tanulás**: Ha új technológiát vagy eszközt tanulsz, a mintaadatokkal való munka gyakorlati módot ad arra, hogy alkalmazd a tanultakat.

Ne feledd, a mintaadatok minősége jelentősen befolyásolhatja ezeket a tevékenységeket. Struktúrájukban és változatosságukban minél közelebb kell állniuk a valós adatokhoz.

### Mintaadat Létrehozása
[Generate DataSet Script](./CreatingSampleData.md)

## Adathalmaz

Egy jó példa mintaadat-halmazra a [DBQ/Burberry.Product.prices.United.States dataset](https://huggingface.co/datasets/DBQ/Burberry.Product.prices.United.States) (elérhető a Huggingface-en).  
A Burberry termékek mintaadat-halmaza, amely tartalmazza a termékek kategóriájára, árára és címére vonatkozó metaadatokat, összesen 3 040 sorral, mindegyik egyedi terméket képvisel. Ez az adathalmaz lehetővé teszi, hogy teszteljük a modell képességét a vizuális adatok megértésére és értelmezésére, valamint olyan leíró szövegek generálására, amelyek részletes vizuális jellemzőket és márkára jellemző tulajdonságokat ragadnak meg.

**Megjegyzés:** Bármilyen képeket tartalmazó adathalmaz használható.

## Összetett Érvelés

A modellnek az árakról és elnevezésekről kell érvelnie kizárólag a kép alapján. Ez megköveteli, hogy a modell ne csak felismerje a vizuális jellemzőket, hanem értse azok jelentőségét a termék értéke és márkázása szempontjából is. Azáltal, hogy pontos szöveges leírásokat szintetizál a képekből, a projekt rámutat arra, milyen lehetőségek rejlenek a vizuális adatok integrálásában a modellek valós alkalmazásokban történő teljesítményének és sokoldalúságának növelésére.

## Phi-3 Vision Architektúra

A modell architektúrája a Phi-3 multimodális változata. Egyszerre dolgozza fel a szöveges és képi adatokat, ezeket egy egységes szekvenciába integrálva a teljes körű megértés és generálás érdekében. A modell külön beágyazási rétegeket használ a szöveghez és a képekhez. A szövegtokeneket sűrű vektorokká alakítja, míg a képeket egy CLIP vision modell segítségével dolgozza fel, hogy jellemző beágyazásokat nyerjen. Ezeket a képi beágyazásokat aztán úgy vetíti át, hogy illeszkedjenek a szöveges beágyazások dimenzióihoz, így zökkenőmentesen integrálhatók.

## Szöveg- és Képbeágyazások Integrációja

A szövegszekvencián belül speciális tokenek jelzik, hová kell beilleszteni a képbeágyazásokat. Feldolgozás közben ezek a speciális tokenek a megfelelő képbeágyazásokra cserélődnek, lehetővé téve, hogy a modell a szöveget és a képeket egyetlen szekvenciaként kezelje. Az adatállományunk promptja a speciális <|image|> token használatával van formázva az alábbi módon:

```python
text = f"<|user|>\n<|image_1|>What is shown in this image?<|end|><|assistant|>\nProduct: {row['title']}, Category: {row['category3_code']}, Full Price: {row['full_price']}<|end|>"
```

## Minta Kód
- [Phi-3-Vision Training Script](../../../../code/03.Finetuning/Phi-3-vision-Trainingscript.py)
- [Weights and Bias Example walkthrough](https://wandb.ai/byyoung3/mlnews3/reports/How-to-fine-tune-Phi-3-vision-on-a-custom-dataset--Vmlldzo4MTEzMTg3)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.