<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:56:34+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "sv"
}
-->
# Välkommen till din VS Code Extension

## Vad finns i mappen

* Den här mappen innehåller alla filer som behövs för din extension.
* `package.json` - detta är manifestfilen där du deklarerar din extension och kommando.
  * Exempelpluginet registrerar ett kommando och definierar dess titel och kommando namn. Med denna information kan VS Code visa kommandot i kommandopaletten. Pluginet behöver ännu inte laddas.
* `src/extension.ts` - detta är huvudfilen där du implementerar ditt kommando.
  * Filen exporterar en funktion, `activate`, som anropas första gången din extension aktiveras (i detta fall genom att köra kommandot). Inuti funktionen `activate` anropar vi `registerCommand`.
  * Vi skickar funktionen som innehåller kommandots implementation som andra parameter till `registerCommand`.

## Installation

* installera de rekommenderade extensionerna (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner och dbaeumer.vscode-eslint)

## Kom igång direkt

* Tryck `F5` för att öppna ett nytt fönster med din extension laddad.
* Kör ditt kommando från kommandopaletten genom att trycka (`Ctrl+Shift+P` eller `Cmd+Shift+P` på Mac) och skriva `Hello World`.
* Sätt brytpunkter i din kod i `src/extension.ts` för att felsöka din extension.
* Hitta utdata från din extension i debugkonsolen.

## Gör ändringar

* Du kan starta om extensionen från debugverktygsfältet efter att ha ändrat kod i `src/extension.ts`.
* Du kan också ladda om (`Ctrl+R` eller `Cmd+R` på Mac) VS Code-fönstret med din extension för att ladda dina ändringar.

## Utforska API:et

* Du kan öppna hela vårt API när du öppnar filen `node_modules/@types/vscode/index.d.ts`.

## Kör tester

* Installera [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Kör "watch"-uppgiften via kommandot **Tasks: Run Task**. Se till att detta körs, annars kanske tester inte upptäcks.
* Öppna testvyn från aktivitetsfältet och klicka på knappen "Run Test", eller använd snabbtangenten `Ctrl/Cmd + ; A`
* Se testresultatets utdata i Test Results-vyn.
* Gör ändringar i `src/test/extension.test.ts` eller skapa nya testfiler i `test`-mappen.
  * Den medföljande testrunnern kommer endast att ta hänsyn till filer som matchar namn mönstret `**.test.ts`.
  * Du kan skapa mappar i `test`-mappen för att organisera dina tester på valfritt sätt.

## Gå vidare

* Minska extensionens storlek och förbättra uppstartstiden genom att [paketera din extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Publicera din extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) på VS Code extension marketplace.
* Automatisera byggen genom att konfigurera [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.