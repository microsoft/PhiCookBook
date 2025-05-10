<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:45:33+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "sr"
}
-->
# Dobrodošli u vašu VS Code ekstenziju

## Šta se nalazi u folderu

* Ovaj folder sadrži sve fajlove potrebne za vašu ekstenziju.
* `package.json` - ovo je manifest fajl u kojem deklarišete vašu ekstenziju i komandu.
  * Primer plugina registruje komandu i definiše njen naslov i ime komande. Sa ovim informacijama VS Code može prikazati komandu u paleti komandi. Plugin još uvek nije potrebno učitavati.
* `src/extension.ts` - ovo je glavni fajl u kome ćete implementirati vašu komandu.
  * Fajl eksportuje jednu funkciju, `activate`, koja se poziva prvi put kada se ekstenzija aktivira (u ovom slučaju izvršavanjem komande). Unutar funkcije `activate` pozivamo `registerCommand`.
  * Funkciju koja sadrži implementaciju komande prosleđujemo kao drugi parametar funkciji `registerCommand`.

## Podešavanje

* instalirajte preporučene ekstenzije (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner i dbaeumer.vscode-eslint)

## Počnite odmah

* Pritisnite `F5` da otvorite novi prozor sa učitanom vašom ekstenzijom.
* Pokrenite komandu iz palete komandi pritiskom na (`Ctrl+Shift+P` ili `Cmd+Shift+P` na Mac-u) i kucanjem `Hello World`.
* Postavite breakpoint-ove u kodu unutar `src/extension.ts` da biste debagovali vašu ekstenziju.
* Pronađite izlaz vaše ekstenzije u debug konzoli.

## Pravite izmene

* Ekstenziju možete ponovo pokrenuti sa debug toolbar-a nakon izmene koda u `src/extension.ts`.
* Takođe možete ponovo učitati (`Ctrl+R` ili `Cmd+R` na Mac-u) VS Code prozor sa vašom ekstenzijom da biste učitali izmene.

## Istražite API

* Možete otvoriti kompletan skup našeg API-ja kada otvorite fajl `node_modules/@types/vscode/index.d.ts`.

## Pokretanje testova

* Instalirajte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Pokrenite "watch" task preko komande **Tasks: Run Task**. Proverite da li je task aktivan, jer testovi možda neće biti otkriveni ako nije.
* Otvorite Testing prikaz sa activity bar-a i kliknite na dugme Run Test, ili koristite prečicu `Ctrl/Cmd + ; A`
* Pogledajte rezultate testova u Test Results prikazu.
* Pravite izmene u `src/test/extension.test.ts` ili kreirajte nove test fajlove unutar `test` foldera.
  * Test runner će uzimati u obzir samo fajlove koji odgovaraju obrascu imena `**.test.ts`.
  * Možete kreirati foldere unutar `test` foldera da organizujete testove kako želite.

## Idite dalje

* Smanjite veličinu ekstenzije i ubrzajte pokretanje [pakovanjem vaše ekstenzije](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Objavite vašu ekstenziju](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na VS Code extension marketplace-u.
* Automatizujte build procese podešavanjem [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења настала коришћењем овог превода.