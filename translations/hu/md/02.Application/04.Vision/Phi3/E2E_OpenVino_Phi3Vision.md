<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-07-17T05:05:12+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "hu"
}
-->
Ez a demó bemutatja, hogyan lehet egy előre betanított modellt használni Python kód generálására egy kép és egy szöveges utasítás alapján.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Lépésről lépésre a magyarázat:

1. **Importálás és beállítás**:
   - A szükséges könyvtárak és modulok importálása, beleértve a `requests`-et, a képfeldolgozáshoz a `PIL`-t, valamint a modellt és feldolgozást kezelő `transformers`-t.

2. **A kép betöltése és megjelenítése**:
   - Egy képfájl (`demo.png`) megnyitása a `PIL` könyvtárral, majd megjelenítése.

3. **Az utasítás definiálása**:
   - Egy üzenet létrehozása, amely tartalmazza a képet és egy kérést, hogy generáljon Python kódot a kép feldolgozására és mentésére `plt` (matplotlib) használatával.

4. **A processzor betöltése**:
   - Az `AutoProcessor` betöltése egy előre betanított modellből, amelyet az `out_dir` könyvtár határoz meg. Ez a processzor kezeli a szöveges és képi bemeneteket.

5. **Az utasítás elkészítése**:
   - Az `apply_chat_template` metódus segítségével az üzenet formázása a modell számára megfelelő prompttá.

6. **A bemenetek feldolgozása**:
   - A prompt és a kép átalakítása tenzorokká, amelyeket a modell értelmezni tud.

7. **A generálási paraméterek beállítása**:
   - A modell generálási folyamatának paraméterei, például a generálandó új tokenek maximális száma és az output mintavételezésének beállítása.

8. **A kód generálása**:
   - A modell a bemenetek és a generálási paraméterek alapján létrehozza a Python kódot. A `TextStreamer` kezeli a kimenetet, kihagyva az utasítást és a speciális tokeneket.

9. **Kimenet**:
   - A generált kód kiírása, amelynek tartalmaznia kell a kép feldolgozására és mentésére szolgáló Python kódot, ahogy az utasításban szerepel.

Ez a demó bemutatja, hogyan lehet egy előre betanított modellt kihasználni OpenVino segítségével, hogy dinamikusan generáljunk kódot felhasználói input és képek alapján.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.