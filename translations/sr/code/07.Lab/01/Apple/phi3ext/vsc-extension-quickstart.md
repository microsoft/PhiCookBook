<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:10:41+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "sr"
}
-->
# Dobrodošli u vašu VS Code ekstenziju

## Šta se nalazi u fascikli

* Ova fascikla sadrži sve fajlove potrebne za vašu ekstenziju.
* `package.json` - ovo je manifest fajl u kojem deklarišete vašu ekstenziju i komandu.
  * Primer plugina registruje komandu i definiše njen naslov i ime komande. Sa ovim informacijama VS Code može prikazati komandu u paleti komandi. Još uvek nije potrebno učitavati plugin.
* `src/extension.ts` - ovo je glavni fajl u kome ćete implementirati vašu komandu.
  * Fajl eksportuje jednu funkciju, `activate`, koja se poziva prvi put kada se ekstenzija aktivira (u ovom slučaju izvršavanjem komande). Unutar funkcije `activate` pozivamo `registerCommand`.
  * Funkciju koja sadrži implementaciju komande prosleđujemo kao drugi parametar funkciji `registerCommand`.

## Podešavanje

* instalirajte preporučene ekstenzije (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, i dbaeumer.vscode-eslint)

## Pokrenite odmah

* Pritisnite `F5` da otvorite novi prozor sa učitanom vašom ekstenzijom.
* Pokrenite vašu komandu iz palete komandi pritiskom na (`Ctrl+Shift+P` ili `Cmd+Shift+P` na Mac-u) i kucanjem `Hello World`.
* Postavite tačke prekida u vašem kodu unutar `src/extension.ts` da biste debugovali vašu ekstenziju.
* Izlaz iz vaše ekstenzije pronađite u debug konzoli.

## Napravite izmene

* Možete ponovo pokrenuti ekstenziju iz debug trake nakon što promenite kod u `src/extension.ts`.
* Takođe možete ponovo učitati (`Ctrl+R` ili `Cmd+R` na Mac-u) VS Code prozor sa vašom ekstenzijom da biste učitali izmene.

## Istražite API

* Možete otvoriti kompletan skup našeg API-ja kada otvorite fajl `node_modules/@types/vscode/index.d.ts`.

## Pokrenite testove

* Instalirajte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Pokrenite "watch" zadatak preko komande **Tasks: Run Task**. Proverite da li je zadatak aktivan, jer u suprotnom testovi možda neće biti pronađeni.
* Otvorite Testing prikaz iz trake aktivnosti i kliknite na dugme Run Test, ili koristite prečicu `Ctrl/Cmd + ; A`
* Pogledajte rezultat testa u Test Results prikazu.
* Pravite izmene u `src/test/extension.test.ts` ili kreirajte nove test fajlove unutar fascikle `test`.
  * Test runner će uzimati u obzir samo fajlove koji odgovaraju obrascu imena `**.test.ts`.
  * Možete praviti podfascikle unutar `test` da strukturirate testove kako želite.

## Idite dalje

* Smanjite veličinu ekstenzije i poboljšajte vreme pokretanja tako što ćete [pakovati vašu ekstenziju](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Objavite vašu ekstenziju](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na VS Code marketplace-u.
* Automatizujte build procese podešavanjem [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Одрицање од одговорности**:  
Овај документ је преведен помоћу AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, имајте у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која могу настати употребом овог превода.