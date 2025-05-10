<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:59:25+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "hr"
}
-->
# Dobrodošli u vašu VS Code ekstenziju

## Što se nalazi u mapi

* Ova mapa sadrži sve datoteke potrebne za vašu ekstenziju.
* `package.json` - ovo je manifest datoteka u kojoj deklarirate vašu ekstenziju i naredbu.
  * Primjer dodatka registrira naredbu i definira njen naslov i ime naredbe. S tim informacijama VS Code može prikazati naredbu u paleti naredbi. Još uvijek nije potrebno učitavati dodatak.
* `src/extension.ts` - ovo je glavna datoteka u kojoj ćete pružiti implementaciju vaše naredbe.
  * Datoteka izvozi jednu funkciju, `activate`, koja se poziva prvi put kada se vaša ekstenzija aktivira (u ovom slučaju izvršavanjem naredbe). Unutar funkcije `activate` pozivamo `registerCommand`.
  * Funkciju koja sadrži implementaciju naredbe prosljeđujemo kao drugi parametar funkciji `registerCommand`.

## Postavljanje

* instalirajte preporučene ekstenzije (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner i dbaeumer.vscode-eslint)

## Odmah započnite

* Pritisnite `F5` za otvaranje novog prozora s učitanom vašom ekstenzijom.
* Pokrenite svoju naredbu iz palete naredbi pritiskom (`Ctrl+Shift+P` ili `Cmd+Shift+P` na Macu) i upisivanjem `Hello World`.
* Postavite prekidne točke u vašem kodu unutar `src/extension.ts` za debugiranje vaše ekstenzije.
* Pronađite izlaz vaše ekstenzije u debug konzoli.

## Napravite promjene

* Ekstenziju možete ponovno pokrenuti s debug alatne trake nakon promjene koda u `src/extension.ts`.
* Također možete ponovno učitati (`Ctrl+R` ili `Cmd+R` na Macu) VS Code prozor s vašom ekstenzijom kako biste učitali promjene.

## Istražite API

* Puni skup našeg API-ja možete otvoriti kada otvorite datoteku `node_modules/@types/vscode/index.d.ts`.

## Pokrenite testove

* Instalirajte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Pokrenite zadatak "watch" preko naredbe **Tasks: Run Task**. Provjerite da je zadatak pokrenut, inače testovi možda neće biti pronađeni.
* Otvorite prikaz testiranja s trake aktivnosti i kliknite na gumb Run Test, ili koristite prečac `Ctrl/Cmd + ; A`
* Pogledajte rezultate testa u prikazu Test Results.
* Napravite promjene u `src/test/extension.test.ts` ili kreirajte nove test datoteke unutar mape `test`.
  * Dostavljeni test runner će uzimati u obzir samo datoteke koje odgovaraju obrascu naziva `**.test.ts`.
  * Unutar mape `test` možete kreirati podmape za organizaciju testova kako god želite.

## Idite dalje

* Smanjite veličinu ekstenzije i poboljšajte vrijeme pokretanja [pakiranjem vaše ekstenzije](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Objavite svoju ekstenziju](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) na VS Code marketplaceu.
* Automatizirajte buildove postavljanjem [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba se smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.