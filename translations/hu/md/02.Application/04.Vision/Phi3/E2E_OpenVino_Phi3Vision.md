<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-09T20:01:53+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "hu"
}
-->
Ez a bemutató azt mutatja be, hogyan használhatunk egy előre betanított modellt Python kód generálására egy kép és egy szöveges utasítás alapján.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Lépésről lépésre a magyarázat:

1. **Importálás és beállítás**:
   - A szükséges könyvtárak és modulok importálása történik, többek között `requests`, `PIL` a képfeldolgozáshoz, valamint `transformers` a modell és a feldolgozás kezeléséhez.

2. **A kép betöltése és megjelenítése**:
   - Egy kép fájl (`demo.png`) megnyitása a `PIL` könyvtár segítségével, majd megjelenítése.

3. **Az utasítás definiálása**:
   - Egy üzenet létrehozása, amely tartalmazza a képet és kérést fogalmaz meg Python kód generálására a kép feldolgozásához és `plt` (matplotlib) használatával történő mentéséhez.

4. **A feldolgozó betöltése**:
   - A `AutoProcessor` betöltése egy előre betanított modellből, amely a `out_dir` könyvtárban található. Ez a feldolgozó kezeli a szöveges és képi bemeneteket.

5. **Az utasítás létrehozása**:
   - A `apply_chat_template` metódus használata az üzenet olyan formázására, amely alkalmas a modell számára promptként.

6. **A bemenetek feldolgozása**:
   - Az utasítás és a kép tensorokká alakítása, amelyeket a modell képes értelmezni.

7. **A generálási paraméterek beállítása**:
   - A modell generálási folyamatának paraméterei megadása, például a generálandó új tokenek maximális száma és az output mintavételezésének engedélyezése.

8. **A kód generálása**:
   - A modell a bemenetek és a generálási paraméterek alapján létrehozza a Python kódot. Az `TextStreamer` az output kezelésére szolgál, kihagyva az utasítást és a speciális tokeneket.

9. **Eredmény**:
   - A generált kód kiírásra kerül, amelynek tartalmaznia kell a képfeldolgozáshoz és a kép mentéséhez szükséges Python kódot, ahogy az utasításban szerepel.

Ez a bemutató szemlélteti, hogyan használhatjuk az OpenVino előre betanított modelljét dinamikus kódgenerálásra felhasználói input és képek alapján.

**Nyilatkozat**:  
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum az anyanyelvén tekintendő hivatalos forrásnak. Kritikus információk esetén szakmai emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.