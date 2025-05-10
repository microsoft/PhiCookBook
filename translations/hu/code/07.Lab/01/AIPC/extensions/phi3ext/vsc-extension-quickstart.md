<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:58:23+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "hu"
}
-->
# Üdvözlünk a VS Code bővítményedben

## Mi található a mappában

* Ez a mappa tartalmazza az összes fájlt, ami a bővítményedhez szükséges.
* `package.json` - ez a manifest fájl, amelyben deklarálod a bővítményedet és a parancsot.
  * A mintaplugin regisztrál egy parancsot, és meghatározza annak címét és nevét. Ezekkel az adatokkal a VS Code meg tudja jeleníteni a parancsot a parancspalettán. Maga a plugin még nem töltődik be.
* `src/extension.ts` - ez a fő fájl, ahol megvalósítod a parancsodat.
  * A fájl egyetlen függvényt exportál, `activate`-t, amely az első alkalommal hívódik meg, amikor a bővítményed aktiválódik (ebben az esetben a parancs futtatásakor). Az `activate` függvényen belül meghívjuk az `registerCommand`-et.
  * A parancs megvalósítását tartalmazó függvényt a második paraméterként adjuk át az `registerCommand`-nek.

## Beállítás

* Telepítsd a javasolt bővítményeket (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, és dbaeumer.vscode-eslint)


## Azonnali indulás

* Nyomd meg `F5`-t, hogy megnyiss egy új ablakot a bővítményeddel betöltve.
* Futtasd a parancsodat a parancspalettából, nyomd meg (`Ctrl+Shift+P` vagy Mac-en `Cmd+Shift+P`), majd írd be `Hello World`-t.
* Állíts be töréspontokat a kódodban, az `src/extension.ts` fájlban, hogy hibakeresd a bővítményedet.
* A bővítményed kimenetét megtalálod a hibakereső konzolban.

## Változtatások végrehajtása

* A hibakereső eszköztárról újraindíthatod a bővítményt, miután módosítottad az `src/extension.ts` fájlt.
* Újratöltheted a VS Code ablakot (`Ctrl+R` vagy Mac-en `Cmd+R`), hogy betöltse a változtatásokat.

## Fedezd fel az API-t

* Megnyithatod az API teljes készletét, ha megnyitod az `node_modules/@types/vscode/index.d.ts` fájlt.

## Tesztek futtatása

* Telepítsd az [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) bővítményt
* Futtasd a "watch" feladatot a **Tasks: Run Task** paranccsal. Győződj meg róla, hogy ez fut, különben a tesztek nem kerülnek felismerésre.
* Nyisd meg a Tesztelés nézetet az aktivitássávból, és kattints a "Run Test" gombra, vagy használd a `Ctrl/Cmd + ; A` gyorsbillentyűt.
* A teszt eredményét a Teszt Eredmények nézetben láthatod.
* Végezz módosításokat az `src/test/extension.test.ts` fájlban, vagy hozz létre új tesztfájlokat az `test` mappában.
  * A teszt futtató csak az `**.test.ts` névmintának megfelelő fájlokat veszi figyelembe.
  * Létrehozhatsz almappákat az `test` mappán belül, hogy tetszőlegesen strukturáld a tesztjeidet.

## Tovább lépés

* Csökkentsd a bővítmény méretét és gyorsítsd a betöltési időt az [bővítmény csomagolásával](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Tedd közzé a bővítményedet](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) a VS Code bővítmény piacterén.
* Automatizáld a build folyamatokat [Folyamatos integráció beállításával](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Nyilatkozat**:  
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális, emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy félreértelmezésekért.