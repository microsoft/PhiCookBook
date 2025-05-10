<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:38:13+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "no"
}
-->
# Velkommen til din VS Code-utvidelse

## Hva som er i mappen

* Denne mappen inneholder alle filene som trengs for utvidelsen din.
* `package.json` - dette er manifestfilen hvor du deklarerer utvidelsen og kommandoen din.
  * Eksempelpluginen registrerer en kommando og definerer tittelen og kommandoens navn. Med denne informasjonen kan VS Code vise kommandoen i kommandopaletten. Pluginen trenger ikke lastes inn ennå.
* `src/extension.ts` - dette er hovedfilen hvor du skal implementere kommandoen din.
  * Filen eksporterer én funksjon, `activate`, som kalles første gang utvidelsen aktiveres (i dette tilfellet ved å kjøre kommandoen). Inne i `activate`-funksjonen kaller vi `registerCommand`.
  * Vi sender funksjonen som inneholder implementasjonen av kommandoen som andre parameter til `registerCommand`.

## Oppsett

* installer de anbefalte utvidelsene (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner og dbaeumer.vscode-eslint)


## Kom i gang med en gang

* Trykk `F5` for å åpne et nytt vindu med utvidelsen din lastet.
* Kjør kommandoen din fra kommandopaletten ved å trykke (`Ctrl+Shift+P` eller `Cmd+Shift+P` på Mac) og skrive `Hello World`.
* Sett brytepunkter i koden din inne i `src/extension.ts` for å feilsøke utvidelsen.
* Finn utdata fra utvidelsen i debug-konsollen.

## Gjør endringer

* Du kan starte utvidelsen på nytt fra debug-verktøylinjen etter å ha endret kode i `src/extension.ts`.
* Du kan også laste inn på nytt (`Ctrl+R` eller `Cmd+R` på Mac) VS Code-vinduet med utvidelsen for å laste inn endringene dine.


## Utforsk API-en

* Du kan åpne hele API-settet vårt ved å åpne filen `node_modules/@types/vscode/index.d.ts`.

## Kjør tester

* Installer [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Kjør "watch"-oppgaven via **Tasks: Run Task**-kommandoen. Sørg for at denne kjører, ellers kan det hende tester ikke blir oppdaget.
* Åpne Testing-visningen fra aktivitetslinjen og klikk på "Run Test"-knappen, eller bruk hurtigtasten `Ctrl/Cmd + ; A`
* Se testresultatet i Test Results-visningen.
* Gjør endringer i `src/test/extension.test.ts` eller lag nye testfiler i `test`-mappen.
  * Den medfølgende testløperen vil kun ta hensyn til filer som matcher navnemønsteret `**.test.ts`.
  * Du kan lage undermapper i `test`-mappen for å organisere testene dine slik du vil.

## Gå videre

* Reduser størrelsen på utvidelsen og forbedre oppstartstiden ved å [bundle utvidelsen din](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publiser utvidelsen din](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) på VS Code-utvidelsesmarkedet.
* Automatiser bygg ved å sette opp [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved bruk av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.