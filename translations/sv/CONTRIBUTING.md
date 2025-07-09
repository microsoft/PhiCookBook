<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-09T18:27:40+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sv"
}
-->
# Bidra

Det här projektet välkomnar bidrag och förslag. De flesta bidrag kräver att du godkänner ett Contributor License Agreement (CLA) som intygar att du har rätt att, och faktiskt gör det, ge oss rättigheterna att använda ditt bidrag. För mer information, besök [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

När du skickar in en pull request kommer en CLA-bot automatiskt att avgöra om du behöver tillhandahålla en CLA och märka PR:n på lämpligt sätt (t.ex. statuskontroll, kommentar). Följ bara instruktionerna från boten. Du behöver bara göra detta en gång för alla repos som använder vår CLA.

## Uppförandekod

Det här projektet har antagit [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
För mer information, läs [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) eller kontakta [opencode@microsoft.com](mailto:opencode@microsoft.com) vid ytterligare frågor eller kommentarer.

## Varningar för att skapa ärenden

Vänligen öppna inte GitHub-ärenden för allmänna supportfrågor eftersom GitHub-listan ska användas för funktionsförfrågningar och bugg-rapporter. På så sätt kan vi enklare spåra faktiska problem eller buggar i koden och hålla den allmänna diskussionen separat från själva koden.

## Hur man bidrar

### Riktlinjer för Pull Requests

När du skickar in en pull request (PR) till Phi-3 CookBook-repositoriet, vänligen följ dessa riktlinjer:

- **Forka Repositoriet**: Forka alltid repositoriet till ditt eget konto innan du gör dina ändringar.

- **Separata pull requests (PR)**:
  - Skicka varje typ av ändring i en egen pull request. Till exempel bör buggfixar och dokumentationsuppdateringar skickas i separata PR:er.
  - Stavfel och mindre dokumentationsuppdateringar kan kombineras i en och samma PR där det är lämpligt.

- **Hantera merge-konflikter**: Om din pull request visar merge-konflikter, uppdatera din lokala `main`-gren så att den speglar huvudrepositoriet innan du gör dina ändringar.

- **Översättningsbidrag**: När du skickar in en översättnings-PR, se till att översättningsmappen innehåller översättningar för alla filer i originalmappen.

### Riktlinjer för skrivande

För att säkerställa enhetlighet i alla dokument, vänligen använd följande riktlinjer:

- **URL-formatering**: Omge alla URL:er med hakparenteser följt av parenteser, utan extra mellanslag runt eller inuti dem. Exempel: `[example](https://www.microsoft.com)`.

- **Relativa länkar**: Använd `./` för relativa länkar som pekar på filer eller mappar i den aktuella katalogen, och `../` för de i en överordnad katalog. Exempel: `[example](../../path/to/file)` eller `[example](../../../path/to/file)`.

- **Ej landspecifika lokaler**: Se till att dina länkar inte innehåller landspecifika lokaler. Undvik till exempel `/en-us/` eller `/en/`.

- **Bildlagring**: Spara alla bilder i mappen `./imgs`.

- **Beskrivande bildnamn**: Namnge bilder beskrivande med engelska tecken, siffror och bindestreck. Exempel: `example-image.jpg`.

## GitHub-arbetsflöden

När du skickar in en pull request kommer följande arbetsflöden att köras för att validera ändringarna. Följ instruktionerna nedan för att säkerställa att din pull request klarar arbetsflödeskontrollerna:

- [Check Broken Relative Paths](../..)  
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Detta arbetsflöde säkerställer att alla relativa sökvägar i dina filer är korrekta.

1. För att säkerställa att dina länkar fungerar korrekt, gör följande i VS Code:
    - Hovra över en länk i dina filer.
    - Tryck på **Ctrl + Klick** för att navigera till länken.
    - Om du klickar på en länk och den inte fungerar lokalt, kommer det att trigga arbetsflödet och inte fungera på GitHub.

1. För att åtgärda detta, gör följande med hjälp av sökvägsförslagen från VS Code:
    - Skriv `./` eller `../`.
    - VS Code kommer att föreslå tillgängliga alternativ baserat på vad du skrev.
    - Följ sökvägen genom att klicka på önskad fil eller mapp för att säkerställa att din sökväg är korrekt.

När du har lagt till rätt relativ sökväg, spara och pusha dina ändringar.

### Check URLs Don't Have Locale

Detta arbetsflöde säkerställer att webbadresser inte innehåller landspecifika lokaler. Eftersom detta repositorium är tillgängligt globalt är det viktigt att URL:er inte innehåller din landslokal.

1. För att verifiera att dina URL:er inte innehåller landslokaler, gör följande:

    - Kontrollera om det finns text som `/en-us/`, `/en/` eller någon annan språklokal i URL:erna.
    - Om dessa inte finns i dina URL:er, klarar du kontrollen.

1. För att åtgärda detta, gör följande:
    - Öppna filen som arbetsflödet markerat.
    - Ta bort landslokalen från URL:erna.

När du tagit bort landslokalen, spara och pusha dina ändringar.

### Check Broken Urls

Detta arbetsflöde säkerställer att alla webbadresser i dina filer fungerar och returnerar statuskod 200.

1. För att verifiera att dina URL:er fungerar korrekt, gör följande:
    - Kontrollera statusen för URL:erna i dina filer.

2. För att åtgärda trasiga URL:er, gör följande:
    - Öppna filen som innehåller den trasiga URL:en.
    - Uppdatera URL:en till rätt adress.

När du har åtgärdat URL:erna, spara och pusha dina ändringar.

> [!NOTE]  
>  
> Det kan finnas fall där URL-kontrollen misslyckas även om länken är tillgänglig. Detta kan bero på flera orsaker, bland annat:  
>  
> - **Nätverksbegränsningar:** GitHub Actions-servrar kan ha nätverksbegränsningar som hindrar åtkomst till vissa URL:er.  
> - **Timeout-problem:** URL:er som tar för lång tid att svara kan orsaka timeout-fel i arbetsflödet.  
> - **Tillfälliga serverproblem:** Tillfälliga driftstopp eller underhåll kan göra en URL otillgänglig under valideringen.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.