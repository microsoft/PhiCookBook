<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:45:57+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "hr"
}
-->
# Dobrodošli u vašu VS Code ekstenziju

## Što se nalazi u mapi

* Ova mapa sadrži sve datoteke potrebne za vašu ekstenziju.
* `package.json` - ovo je manifest datoteka u kojoj deklarirate svoju ekstenziju i naredbu.
  * Primjer plugina registrira naredbu i definira njen naslov i ime naredbe. S tim informacijama VS Code može prikazati naredbu u paleti naredbi. Plugin još uvijek nije potrebno učitavati.
* `src/extension.ts` - ovo je glavna datoteka u kojoj ćete implementirati svoju naredbu.
  * Datoteka izveze jednu funkciju, `activate`, koja se poziva prvi put kada se vaša ekstenzija aktivira (u ovom slučaju izvršavanjem naredbe). Unutar funkcije `activate` pozivamo `registerCommand`.
  * Funkciju koja sadrži implementaciju naredbe prosljeđujemo kao drugi parametar funkciji `registerCommand`.

## Postavljanje

* instalirajte preporučene ekstenzije (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner i dbaeumer.vscode-eslint)

## Počnite odmah

* Pritisnite `F5` da otvorite novi prozor s učitanom vašom ekstenzijom.
* Pokrenite svoju naredbu iz palete naredbi pritiskom na (`Ctrl+Shift+P` ili `Cmd+Shift+P` na Macu) i upišite `Hello World`.
* Postavite točke prekida u vašem kodu unutar `src/extension.ts` da biste debugirali ekstenziju.
* Pronađite izlaz iz vaše ekstenzije u debug konzoli.

## Izmjene

* Možete ponovno pokrenuti ekstenziju s debug alatne trake nakon promjene koda u `src/extension.ts`.
* Također možete ponovno učitati (`Ctrl+R` ili `Cmd+R` na Macu) VS Code prozor s vašom ekstenzijom da biste učitali promjene.

## Istražite API

* Možete otvoriti kompletan skup našeg API-ja kada otvorite datoteku `node_modules/@types/vscode/index.d.ts`.

## Pokretanje testova

* Instalirajte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Pokrenite zadatak "watch" putem naredbe **Tasks: Run Task**. Provjerite da je zadatak pokrenut, inače testovi možda neće biti otkriveni.
* Otvorite prikaz Testiranja s trake aktivnosti i kliknite gumb "Run Test", ili koristite tipkovni prečac `Ctrl/Cmd + ; A`
* Pogledajte rezultate testova u prikazu Test Results.
* Izmijenite `src/test/extension.test.ts` ili kreirajte nove test datoteke unutar mape `test`.
  * Dostavljeni test runner će uzimati u obzir samo datoteke koje odgovaraju obrascu imena `**.test.ts`.
  * Unutar mape `test` možete kreirati podmape za organizaciju testova kako želite.

## Idite dalje

* Smanjite veličinu ekstenzije i poboljšajte vrijeme pokretanja [pakiranjem vaše ekstenzije](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Objavite svoju ekstenziju](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na VS Code marketplace-u.
* Automatizirajte buildove postavljanjem [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba se smatrati službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazumevanja ili kriva tumačenja koja proizlaze iz korištenja ovog prijevoda.