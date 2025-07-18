<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-07-16T17:04:31+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "hr"
}
-->
# Dobrodošli u vašu VS Code ekstenziju

## Što se nalazi u mapi

* Ova mapa sadrži sve datoteke potrebne za vašu ekstenziju.
* `package.json` - ovo je manifest datoteka u kojoj deklarirate svoju ekstenziju i naredbu.
  * Primjer dodatka registrira naredbu i definira njen naslov i ime naredbe. S tim informacijama VS Code može prikazati naredbu u paleti naredbi. Još uvijek nije potrebno učitavati dodatak.
* `src/extension.ts` - glavna datoteka u kojoj ćete implementirati svoju naredbu.
  * Datoteka izveze jednu funkciju, `activate`, koja se poziva prvi put kada se vaša ekstenzija aktivira (u ovom slučaju izvršavanjem naredbe). Unutar funkcije `activate` pozivamo `registerCommand`.
  * Funkciju koja sadrži implementaciju naredbe prosljeđujemo kao drugi parametar funkciji `registerCommand`.

## Postavljanje

* instalirajte preporučene ekstenzije (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner i dbaeumer.vscode-eslint)

## Pokrenite odmah

* Pritisnite `F5` za otvaranje novog prozora s učitanom vašom ekstenzijom.
* Pokrenite svoju naredbu iz palete naredbi pritiskom na (`Ctrl+Shift+P` ili `Cmd+Shift+P` na Macu) i upišite `Hello World`.
* Postavite točke prekida u svom kodu unutar `src/extension.ts` za ispravljanje pogrešaka vaše ekstenzije.
* Izlaz vaše ekstenzije pronađite u konzoli za ispravljanje pogrešaka.

## Izmjene

* Ekstenziju možete ponovno pokrenuti s trake za ispravljanje pogrešaka nakon promjene koda u `src/extension.ts`.
* Također možete ponovno učitati (`Ctrl+R` ili `Cmd+R` na Macu) VS Code prozor s vašom ekstenzijom da biste učitali promjene.

## Istražite API

* Cijeli skup našeg API-ja možete otvoriti otvaranjem datoteke `node_modules/@types/vscode/index.d.ts`.

## Pokretanje testova

* Instalirajte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Pokrenite zadatak "watch" putem naredbe **Tasks: Run Task**. Provjerite da je zadatak pokrenut, inače testovi možda neće biti otkriveni.
* Otvorite prikaz testiranja s trake aktivnosti i kliknite gumb "Run Test", ili koristite prečac `Ctrl/Cmd + ; A`
* Rezultate testova pogledajte u prikazu Test Results.
* Izmijenite `src/test/extension.test.ts` ili kreirajte nove testne datoteke unutar mape `test`.
  * Dostavljeni test runner će uzimati u obzir samo datoteke koje odgovaraju obrascu imena `**.test.ts`.
  * Unutar mape `test` možete kreirati podmape za organizaciju testova kako želite.

## Daljnji koraci

* Smanjite veličinu ekstenzije i poboljšajte vrijeme pokretanja [pakiranjem vaše ekstenzije](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Objavite svoju ekstenziju](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) na VS Code marketplaceu.
* Automatizirajte izgradnju postavljanjem [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.