<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:08:22+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "da"
}
-->
# Velkommen til din VS Code Extension

## Hvad er i mappen

* Denne mappe indeholder alle filer, der er nødvendige for din extension.
* `package.json` - dette er manifestfilen, hvor du erklærer din extension og kommando.
  * Eksempelpluginet registrerer en kommando og definerer dens titel og kommandonavn. Med disse oplysninger kan VS Code vise kommandoen i kommandopaletten. Det behøver endnu ikke at indlæse plugin'et.
* `src/extension.ts` - dette er hovedfilen, hvor du leverer implementeringen af din kommando.
  * Filen eksporterer én funktion, `activate`, som kaldes første gang din extension aktiveres (i dette tilfælde ved at udføre kommandoen). Inde i funktionen `activate` kalder vi `registerCommand`.
  * Vi sender funktionen, der indeholder implementeringen af kommandoen, som det andet parameter til `registerCommand`.

## Opsætning

* installer de anbefalede extensions (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner og dbaeumer.vscode-eslint)

## Kom i gang med det samme

* Tryk `F5` for at åbne et nyt vindue med din extension indlæst.
* Kør din kommando fra kommandopaletten ved at trykke (`Ctrl+Shift+P` eller `Cmd+Shift+P` på Mac) og skrive `Hello World`.
* Sæt breakpoints i din kode inde i `src/extension.ts` for at debugge din extension.
* Find output fra din extension i debugkonsollen.

## Foretag ændringer

* Du kan genstarte extensionen fra debugværktøjslinjen efter at have ændret kode i `src/extension.ts`.
* Du kan også genindlæse (`Ctrl+R` eller `Cmd+R` på Mac) VS Code-vinduet med din extension for at indlæse dine ændringer.

## Udforsk API'et

* Du kan åbne det komplette sæt af vores API ved at åbne filen `node_modules/@types/vscode/index.d.ts`.

## Kør tests

* Installer [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Kør "watch"-opgaven via kommandoen **Tasks: Run Task**. Sørg for, at denne kører, ellers bliver tests måske ikke fundet.
* Åbn Testing-visningen fra aktivitetsbjælken og klik på knappen "Run Test" eller brug genvejstasten `Ctrl/Cmd + ; A`
* Se outputtet af testrapporten i Test Results-visningen.
* Foretag ændringer i `src/test/extension.test.ts` eller opret nye testfiler inde i `test`-mappen.
  * Den medfølgende test runner vil kun tage filer i betragtning, der matcher navnemønsteret `**.test.ts`.
  * Du kan oprette undermapper inde i `test`-mappen for at strukturere dine tests, som du vil.

## Gå videre

* Reducer extensionens størrelse og forbedr opstartstiden ved at [bundle din extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publicer din extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) på VS Code extension-markedet.
* Automatiser builds ved at sætte [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) op.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.