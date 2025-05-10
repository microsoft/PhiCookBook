<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:59:13+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "sr"
}
-->
# Dobrodošli u vaš VS Code Extension

## Šta se nalazi u fascikli

* Ova fascikla sadrži sve fajlove potrebne za vašu ekstenziju.
* `package.json` - ovo je manifest fajl u kome deklarišete vašu ekstenziju i komandu.
  * Primer plugina registruje komandu i definiše njen naslov i ime komande. Sa ovim informacijama VS Code može prikazati komandu u paleti komandi. Još uvek nije potrebno da učitava plugin.
* `src/extension.ts` - ovo je glavni fajl gde ćete implementirati vašu komandu.
  * Fajl eksportuje jednu funkciju, `activate`, koja se poziva prvi put kada se ekstenzija aktivira (u ovom slučaju izvršavanjem komande). Unutar funkcije `activate` pozivamo `registerCommand`.
  * Funkciju koja sadrži implementaciju komande prosleđujemo kao drugi parametar funkciji `registerCommand`.

## Podešavanje

* instalirajte preporučene ekstenzije (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner i dbaeumer.vscode-eslint)


## Počnite odmah

* Pritisnite `F5` da otvorite novi prozor sa učitanom vašom ekstenzijom.
* Pokrenite vašu komandu iz palete komandi pritiskom na (`Ctrl+Shift+P` ili `Cmd+Shift+P` na Mac-u) i ukucajte `Hello World`.
* Postavite tačke prekida u kodu unutar `src/extension.ts` da biste debug-ovali vašu ekstenziju.
* Izlaz vaše ekstenzije pronađite u debug konzoli.

## Napravite izmene

* Možete ponovo pokrenuti ekstenziju sa debug trake nakon izmene koda u `src/extension.ts`.
* Takođe možete ponovo učitati (`Ctrl+R` ili `Cmd+R` na Mac-u) VS Code prozor sa vašom ekstenzijom da biste učitali izmene.


## Istražite API

* Možete otvoriti kompletan skup našeg API-ja tako što ćete otvoriti fajl `node_modules/@types/vscode/index.d.ts`.

## Pokrenite testove

* Instalirajte [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Pokrenite zadatak "watch" preko komande **Tasks: Run Task**. Proverite da li je zadatak aktivan, jer u suprotnom testovi možda neće biti otkriveni.
* Otvorite Testing prikaz sa activity bara i kliknite na dugme Run Test, ili koristite prečicu `Ctrl/Cmd + ; A`
* Pogledajte rezultat testa u Test Results prikazu.
* Pravite izmene u `src/test/extension.test.ts` ili kreirajte nove test fajlove unutar fascikle `test`.
  * Dati test runner će uzimati u obzir samo fajlove koji odgovaraju obrascu imena `**.test.ts`.
  * Možete kreirati podfascikle unutar `test` fascikle da organizujete testove kako god želite.

## Idite dalje

* Smanjite veličinu ekstenzije i poboljšajte vreme pokretanja tako što ćete [pakovati vašu ekstenziju](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Objavite vašu ekstenziju](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) na VS Code marketplace-u.
* Automatizujte build procese podešavanjem [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korišćenjem AI prevodilačke usluge [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo tačnosti, imajte na umu da automatski prevodi mogu sadržavati greške ili netačnosti. Originalni dokument na izvornom jeziku treba smatrati zvaničnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešna tumačenja koja proisteknu iz korišćenja ovog prevoda.