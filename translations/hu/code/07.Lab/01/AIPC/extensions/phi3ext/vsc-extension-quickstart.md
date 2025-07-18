<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-07-16T16:45:36+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "hu"
}
-->
# Üdvözlünk a VS Code bővítményedben

## Mi található a mappában

* Ez a mappa tartalmazza a bővítményedhez szükséges összes fájlt.
* `package.json` - ez a manifest fájl, amelyben deklarálod a bővítményedet és a parancsot.
  * A minta plugin regisztrál egy parancsot, és meghatározza annak címét és nevét. Ezekkel az információkkal a VS Code meg tudja jeleníteni a parancsot a parancspalettán. Maga a plugin még nem töltődik be.
* `src/extension.ts` - ez a fő fájl, ahol megvalósítod a parancsodat.
  * A fájl egy `activate` nevű függvényt exportál, amelyet először hív meg a rendszer, amikor a bővítményed aktiválódik (jelen esetben a parancs futtatásakor). Az `activate` függvényen belül hívjuk meg a `registerCommand`-ot.
  * A parancs megvalósítását tartalmazó függvényt a `registerCommand` második paramétereként adjuk át.

## Beállítás

* Telepítsd a javasolt bővítményeket (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner és dbaeumer.vscode-eslint)


## Azonnali indítás

* Nyomd meg az `F5`-öt, hogy egy új ablakban megnyisd a bővítményedet.
* Futtasd a parancsodat a parancspalettából (`Ctrl+Shift+P` vagy Mac-en `Cmd+Shift+P`), és írd be, hogy `Hello World`.
* Állíts be töréspontokat a kódodban a `src/extension.ts` fájlban, hogy hibakeresést végezhess.
* A bővítményed kimenetét a hibakereső konzolon találod.

## Változtatások végrehajtása

* A `src/extension.ts` fájl módosítása után újraindíthatod a bővítményt a hibakereső eszköztárról.
* Újratöltheted a VS Code ablakot a bővítményeddel (`Ctrl+R` vagy Mac-en `Cmd+R`), hogy betöltse a változtatásokat.


## Fedezd fel az API-t

* Megnyithatod az API teljes készletét a `node_modules/@types/vscode/index.d.ts` fájl megnyitásával.

## Tesztek futtatása

* Telepítsd az [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) bővítményt
* Futtasd a "watch" feladatot a **Tasks: Run Task** parancson keresztül. Győződj meg róla, hogy ez fut, különben a tesztek nem lesznek felismerve.
* Nyisd meg a Teszt nézetet az aktivitás sávból, és kattints a "Run Test" gombra, vagy használd a `Ctrl/Cmd + ; A` gyorsbillentyűt.
* A teszteredményeket a Teszt eredmények nézetben láthatod.
* Módosítsd a `src/test/extension.test.ts` fájlt, vagy hozz létre új tesztfájlokat a `test` mappán belül.
  * A teszt futtató csak azokat a fájlokat veszi figyelembe, amelyek neve `**.test.ts` mintára illeszkedik.
  * A `test` mappán belül létrehozhatsz almappákat, hogy tetszés szerint rendszerezd a teszteket.

## Tovább lépés

* Csökkentsd a bővítmény méretét és gyorsítsd az indítást azzal, hogy [csomagolod a bővítményedet](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Tedd közzé a bővítményedet](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) a VS Code bővítmény piacterén.
* Automatizáld a build folyamatokat a [Folyamatos integráció](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo) beállításával.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.