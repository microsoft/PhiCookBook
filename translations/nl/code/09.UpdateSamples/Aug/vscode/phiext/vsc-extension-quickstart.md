# Welkom bij je VS Code-extensie

## Wat zit er in de map

* Deze map bevat alle bestanden die nodig zijn voor je extensie.
* `package.json` - dit is het manifestbestand waarin je je extensie en commando declareert.
  * De voorbeeldplugin registreert een commando en definieert de titel en de naam van het commando. Met deze informatie kan VS Code het commando tonen in de commandopalet. De plugin hoeft nog niet geladen te worden.
* `src/extension.ts` - dit is het hoofdbestand waarin je de implementatie van je commando schrijft.
  * Het bestand exporteert één functie, `activate`, die wordt aangeroepen de allereerste keer dat je extensie wordt geactiveerd (in dit geval door het uitvoeren van het commando). Binnen de `activate` functie roepen we `registerCommand` aan.
  * We geven de functie met de implementatie van het commando als tweede parameter door aan `registerCommand`.

## Installatie

* Installeer de aanbevolen extensies (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner en dbaeumer.vscode-eslint)

## Direct aan de slag

* Druk op `F5` om een nieuw venster te openen met je extensie geladen.
* Voer je commando uit via de commandopalet door (`Ctrl+Shift+P` of `Cmd+Shift+P` op Mac) te drukken en `Hello World` te typen.
* Zet breakpoints in je code in `src/extension.ts` om je extensie te debuggen.
* Bekijk de output van je extensie in de debugconsole.

## Wijzigingen aanbrengen

* Je kunt de extensie opnieuw starten vanuit de debugwerkbalk nadat je code in `src/extension.ts` hebt aangepast.
* Je kunt ook het VS Code-venster met je extensie herladen (`Ctrl+R` of `Cmd+R` op Mac) om je wijzigingen te laden.

## Verken de API

* Je kunt de volledige set van onze API openen door het bestand `node_modules/@types/vscode/index.d.ts` te openen.

## Tests uitvoeren

* Installeer de [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Voer de "watch" taak uit via de **Tasks: Run Task** opdracht. Zorg dat deze actief is, anders worden tests mogelijk niet gevonden.
* Open de Testing-weergave via de activiteitenbalk en klik op de knop "Run Test", of gebruik de sneltoets `Ctrl/Cmd + ; A`
* Bekijk de testresultaten in de Test Results-weergave.
* Breng wijzigingen aan in `src/test/extension.test.ts` of maak nieuwe testbestanden aan in de `test` map.
  * De meegeleverde test runner kijkt alleen naar bestanden die voldoen aan het naam patroon `**.test.ts`.
  * Je kunt mappen aanmaken binnen de `test` map om je tests op elke gewenste manier te organiseren.

## Verder gaan

* Verminder de grootte van de extensie en verbeter de opstarttijd door [je extensie te bundelen](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publiceer je extensie](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) op de VS Code extensiemarkt.
* Automatiseer builds door [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) in te stellen.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.