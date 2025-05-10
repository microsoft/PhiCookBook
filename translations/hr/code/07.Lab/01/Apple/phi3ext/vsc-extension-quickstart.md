<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:10:52+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "hr"
}
-->
# Dobrodošli u vašu VS Code ekstenziju

## Što se nalazi u mapi

* Ova mapa sadrži sve datoteke potrebne za vašu ekstenziju.
* `package.json` - ovo je manifest datoteka u kojoj deklarirate svoju ekstenziju i naredbu.
  * Primjer plugina registrira naredbu i definira njen naslov i ime naredbe. S tim informacijama VS Code može prikazati naredbu u paleti naredbi. Plugin se pritom još ne mora učitavati.
* `src/extension.ts` - ovo je glavna datoteka u kojoj ćete implementirati svoju naredbu.
  * Datoteka izvozi jednu funkciju, `activate`, koja se poziva prvi put kad se ekstenzija aktivira (u ovom slučaju izvršavanjem naredbe). Unutar funkcije `activate` pozivamo `registerCommand`.
  * Funkciju koja sadrži implementaciju naredbe prosljeđujemo kao drugi parametar funkciji `registerCommand`.

## Postavljanje

* instalirajte preporučene ekstenzije (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner i dbaeumer.vscode-eslint)

## Pokrenite odmah

* Pritisnite `F5` da otvorite novi prozor s učitanom vašom ekstenzijom.
* Pokrenite svoju naredbu iz palete naredbi pritiskom (`Ctrl+Shift+P` ili `Cmd+Shift+P` na Macu) i upisivanjem `Hello World`.
* Postavite točke prekida u svom kodu unutar `src/extension.ts` za ispravljanje pogrešaka vaše ekstenzije.
* Izlaz vaše ekstenzije pronađite u konzoli za ispravljanje pogrešaka.

## Napravite promjene

* Možete ponovno pokrenuti ekstenziju s trake za ispravljanje pogrešaka nakon što promijenite kod u `src/extension.ts`.
* Također možete ponovno učitati (`Ctrl+R` ili `Cmd+R` na Macu) VS Code prozor s vašom ekstenzijom da biste učitali promjene.

## Istražite API

* Možete otvoriti kompletan skup našeg API-ja otvaranjem datoteke `node_modules/@types/vscode/index.d.ts`.

## Pokrenite testove

* Instalirajte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Pokrenite zadatak "watch" putem naredbe **Tasks: Run Task**. Provjerite da je zadatak pokrenut, inače testovi možda neće biti otkriveni.
* Otvorite prikaz testiranja s trake aktivnosti i kliknite na gumb "Run Test" ili koristite prečac `Ctrl/Cmd + ; A`
* Pogledajte rezultate testova u prikazu Test Results.
* Izmijenite `src/test/extension.test.ts` ili kreirajte nove testne datoteke unutar mape `test`.
  * Zadani test runner će uzimati u obzir samo datoteke koje odgovaraju obrascu imena `**.test.ts`.
  * Možete kreirati mape unutar `test` kako biste organizirali svoje testove kako god želite.

## Idite dalje

* Smanjite veličinu ekstenzije i poboljšajte vrijeme pokretanja [pakiranjem ekstenzije](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Objavite svoju ekstenziju](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na VS Code marketplaceu.
* Automatizirajte izgradnju postavljanjem [kontinuirane integracije](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.