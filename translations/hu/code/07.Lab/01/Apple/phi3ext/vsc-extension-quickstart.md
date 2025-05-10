<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:09:53+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "hu"
}
-->
# Üdvözlünk a VS Code bővítményedben

## Mi található a mappában

* Ez a mappa tartalmazza az összes fájlt, ami a bővítményedhez szükséges.
* `package.json` - ez a manifest fájl, amelyben deklarálod a bővítményedet és a parancsot.
  * A mintaplugin regisztrál egy parancsot, és megadja a címét és a parancs nevét. Ezekkel az információkkal a VS Code meg tudja jeleníteni a parancsot a parancspalettán. Maga a plugin még nem töltődik be.
* `src/extension.ts` - ez a fő fájl, ahol megvalósítod a parancsodat.
  * A fájl egy függvényt exportál, `activate`-t, amelyet az első alkalommal hív meg a bővítmény aktiválásakor (ebben az esetben a parancs végrehajtásakor). Az `activate` függvényen belül meghívjuk az `registerCommand`-et.
  * A parancs megvalósítását tartalmazó függvényt a második paraméterként adjuk át az `registerCommand`-nek.

## Beállítás

* Telepítsd a javasolt bővítményeket (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner és dbaeumer.vscode-eslint)


## Azonnali indítás

* Nyomd meg `F5`-t, hogy új ablakot nyiss a bővítményeddel.
* Futtasd a parancsodat a parancspalettából (`Ctrl+Shift+P` vagy Mac-en `Cmd+Shift+P` megnyomásával), majd írd be `Hello World`-t.
* Állíts be töréspontokat a kódodban az `src/extension.ts` fájlban, hogy hibakeresést végezhess a bővítményeden.
* A bővítményed kimenetét megtalálod a hibakeresési konzolon.

## Változtatások végrehajtása

* A kód módosítása után az `src/extension.ts` fájlban újraindíthatod a bővítményt a hibakereső eszköztárról.
* Újratöltheted is a VS Code ablakot (`Ctrl+R` vagy Mac-en `Cmd+R`), hogy betöltse a változtatásaidat.

## Az API felfedezése

* Megnyithatod az API teljes készletét, ha megnyitod az `node_modules/@types/vscode/index.d.ts` fájlt.

## Tesztek futtatása

* Telepítsd az [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) bővítményt.
* Futtasd a "watch" feladatot a **Tasks: Run Task** parancson keresztül. Győződj meg róla, hogy ez fut, különben a tesztek nem lesznek észlelve.
* Nyisd meg a Teszt nézetet az aktivitássávból, és kattints a "Run Test" gombra, vagy használd a `Ctrl/Cmd + ; A` gyorsbillentyűt.
* A tesztek eredményét a Teszt eredmények nézetben láthatod.
* Módosítsd az `src/test/extension.test.ts` fájlt, vagy hozz létre új tesztfájlokat az `test` mappában.
  * A tesztfuttató csak azokat a fájlokat veszi figyelembe, amelyek megfelelnek az `**.test.ts` név mintának.
  * Létrehozhatsz mappákat az `test` mappán belül, hogy tetszés szerint rendezd a teszteket.

## Továbbfejlődés

* Csökkentsd a bővítmény méretét és gyorsítsd az indulást azáltal, hogy [csomagolod a bővítményedet](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Tedd közzé a bővítményedet](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) a VS Code bővítmény piacterén.
* Automatizáld a build folyamatokat a [Folyamatos Integráció](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) beállításával.

**Nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum a saját nyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.