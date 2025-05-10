<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:56:55+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "no"
}
-->
# Velkommen til din VS Code-utvidelse

## Hva finnes i mappen

* Denne mappen inneholder alle filene som trengs for utvidelsen din.
* `package.json` - dette er manifestfilen hvor du deklarerer utvidelsen og kommandoen din.
  * Eksempelpluginen registrerer en kommando og definerer tittelen og kommando-navnet. Med denne informasjonen kan VS Code vise kommandoen i kommandopaletten. Den trenger ikke å laste pluginet ennå.
* `src/extension.ts` - dette er hovedfilen hvor du implementerer kommandoen din.
  * Filen eksporterer en funksjon, `activate`, som kalles første gang utvidelsen aktiveres (i dette tilfellet ved å kjøre kommandoen). Inne i `activate`-funksjonen kaller vi `registerCommand`.
  * Vi sender funksjonen som inneholder kommando-implementasjonen som andre parameter til `registerCommand`.

## Oppsett

* installer de anbefalte utvidelsene (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner og dbaeumer.vscode-eslint)


## Kom i gang med en gang

* Trykk `F5` for å åpne et nytt vindu med utvidelsen lastet.
* Kjør kommandoen din fra kommandopaletten ved å trykke (`Ctrl+Shift+P` eller `Cmd+Shift+P` på Mac) og skrive `Hello World`.
* Sett breakpoints i koden din i `src/extension.ts` for å feilsøke utvidelsen.
* Finn utdata fra utvidelsen i debug-konsollen.

## Gjør endringer

* Du kan starte utvidelsen på nytt fra debug-verktøylinjen etter å ha endret kode i `src/extension.ts`.
* Du kan også laste VS Code-vinduet på nytt (`Ctrl+R` eller `Cmd+R` på Mac) med utvidelsen for å laste inn endringene dine.


## Utforsk API-et

* Du kan åpne hele API-et vårt ved å åpne filen `node_modules/@types/vscode/index.d.ts`.

## Kjør tester

* Installer [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Kjør "watch"-oppgaven via **Tasks: Run Task**-kommandoen. Pass på at denne kjører, ellers kan det hende tester ikke blir oppdaget.
* Åpne Testing-visningen fra aktivitetslinjen og klikk på "Run Test"-knappen, eller bruk hurtigtasten `Ctrl/Cmd + ; A`
* Se testresultatene i Test Results-visningen.
* Gjør endringer i `src/test/extension.test.ts` eller lag nye testfiler inne i `test`-mappen.
  * Den medfølgende testløperen vil bare ta hensyn til filer som matcher navnemønsteret `**.test.ts`.
  * Du kan lage undermapper inne i `test`-mappen for å organisere testene dine som du vil.

## Gå videre

* Reduser størrelsen på utvidelsen og forbedre oppstartstiden ved å [pakke utvidelsen din](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Publiser utvidelsen din](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) på VS Code-utvidelsesmarkedet.
* Automatiser bygg ved å sette opp [Kontinuerlig Integrasjon](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på det opprinnelige språket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.