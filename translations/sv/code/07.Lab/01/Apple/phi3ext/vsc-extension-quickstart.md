<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-07-16T17:01:52+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "sv"
}
-->
# Välkommen till din VS Code Extension

## Vad finns i mappen

* Den här mappen innehåller alla filer som behövs för din extension.
* `package.json` - detta är manifestfilen där du deklarerar din extension och kommando.
  * Exempelpluginet registrerar ett kommando och definierar dess titel och kommando-namn. Med denna information kan VS Code visa kommandot i kommandopaletten. Det behöver ännu inte ladda pluginet.
* `src/extension.ts` - detta är huvudfilen där du implementerar ditt kommando.
  * Filen exporterar en funktion, `activate`, som anropas första gången din extension aktiveras (i detta fall genom att köra kommandot). Inuti `activate`-funktionen anropar vi `registerCommand`.
  * Vi skickar funktionen som innehåller implementeringen av kommandot som andra parameter till `registerCommand`.

## Installation

* installera de rekommenderade extensionerna (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner och dbaeumer.vscode-eslint)

## Kom igång direkt

* Tryck på `F5` för att öppna ett nytt fönster med din extension laddad.
* Kör ditt kommando från kommandopaletten genom att trycka (`Ctrl+Shift+P` eller `Cmd+Shift+P` på Mac) och skriva `Hello World`.
* Sätt brytpunkter i din kod i `src/extension.ts` för att felsöka din extension.
* Hitta utdata från din extension i debugkonsolen.

## Gör ändringar

* Du kan starta om extensionen från debugverktygsfältet efter att ha ändrat kod i `src/extension.ts`.
* Du kan också ladda om (`Ctrl+R` eller `Cmd+R` på Mac) VS Code-fönstret med din extension för att ladda dina ändringar.

## Utforska API:et

* Du kan öppna hela vårt API genom att öppna filen `node_modules/@types/vscode/index.d.ts`.

## Kör tester

* Installera [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Kör "watch"-uppgiften via kommandot **Tasks: Run Task**. Se till att detta körs, annars kanske tester inte upptäcks.
* Öppna Testvyn från aktivitetsfältet och klicka på knappen "Run Test", eller använd snabbkommandot `Ctrl/Cmd + ; A`
* Se testresultatets utdata i Test Results-vyn.
* Gör ändringar i `src/test/extension.test.ts` eller skapa nya testfiler i `test`-mappen.
  * Den medföljande testrunnern tar bara hänsyn till filer som matchar namn-mönstret `**.test.ts`.
  * Du kan skapa mappar i `test`-mappen för att strukturera dina tester som du vill.

## Gå vidare

* Minska extensionens storlek och förbättra starttiden genom att [bundla din extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Publicera din extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) på VS Code extension marketplace.
* Automatisera byggen genom att sätta upp [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.