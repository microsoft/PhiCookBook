<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:42:04+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "hu"
}
-->
# Üdvözlünk a VS Code kiterjesztésedben

## Mi található a mappában

* Ez a mappa tartalmazza az összes szükséges fájlt a kiterjesztésedhez.
* `package.json` - ez a manifest fájl, amelyben deklarálod a kiterjesztésedet és a parancsot.
  * A minta plugin regisztrál egy parancsot, és meghatározza annak címét és nevét. Ezekkel az információkkal a VS Code meg tudja jeleníteni a parancsot a parancspalettán, de még nem kell betöltenie a plugint.
* `src/extension.ts` - ez a fő fájl, ahol megvalósítod a parancsodat.
  * A fájl egyetlen függvényt exportál, `activate`-t, amelyet az első aktiváláskor hív meg a kiterjesztés (jelen esetben a parancs futtatásakor). Az `activate` függvényen belül meghívjuk `registerCommand`-et.
  * A parancs megvalósítását tartalmazó függvényt a második paraméterként adjuk át `registerCommand`-nek.

## Beállítás

* Telepítsd a javasolt kiterjesztéseket (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner és dbaeumer.vscode-eslint)

## Azonnali indulás

* Nyomd meg `F5`-t, hogy megnyiss egy új ablakot, amiben betöltődik a kiterjesztésed.
* Futtasd a parancsodat a parancspalettából a (`Ctrl+Shift+P` vagy Mac-en `Cmd+Shift+P`) megnyomásával, majd írd be `Hello World`-et.
* Állíts be töréspontokat a kódodban az `src/extension.ts` fájlban, hogy hibakeresést végezhess a kiterjesztéseden.
* A kiterjesztésed kimenetét a hibakereső konzolon találod.

## Változtatások végrehajtása

* A kód módosítása után újraindíthatod a kiterjesztést a hibakereső eszköztárról az `src/extension.ts` fájlban végzett változtatások után.
* Újratöltheted a VS Code ablakot a kiterjesztéseddel együtt (`Ctrl+R` vagy Mac-en `Cmd+R`), hogy betöltődjenek a változtatások.

## Ismerd meg az API-t

* A teljes API dokumentációt megnyithatod az `node_modules/@types/vscode/index.d.ts` fájl megnyitásával.

## Tesztek futtatása

* Telepítsd az [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) kiterjesztést
* Futtasd a "watch" feladatot a **Tasks: Run Task** parancson keresztül. Győződj meg róla, hogy fut, különben a tesztek nem lesznek felismerve.
* Nyisd meg a Teszt nézetet az aktivitássávból, és kattints a "Run Test" gombra, vagy használd a `Ctrl/Cmd + ; A` gyorsbillentyűt.
* A teszt eredményét a Teszteredmények nézetben láthatod.
* Változtass az `src/test/extension.test.ts` fájlon, vagy hozz létre új tesztfájlokat az `test` mappában.
  * A biztosított tesztfuttató csak az `**.test.ts` név mintának megfelelő fájlokat veszi figyelembe.
  * Az `test` mappán belül létrehozhatsz almappákat, hogy tetszés szerint strukturáld a tesztjeidet.

## Továbbfejlődés

* Csökkentsd a kiterjesztés méretét és javítsd az indítási időt azzal, hogy [csomagolod a kiterjesztésedet](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Tedd közzé a kiterjesztésedet](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) a VS Code kiterjesztés piacterén.
* Automatizáld a build folyamatokat a [Folyamatos integráció](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) beállításával.

**Nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hivatalos forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.