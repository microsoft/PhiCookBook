<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:40:27+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "sv"
}
-->
# Contributing

Detta projekt välkomnar bidrag och förslag. De flesta bidrag kräver att du godkänner ett Contributor License Agreement (CLA) som intygar att du har rätt att, och faktiskt ger oss, rättigheterna att använda ditt bidrag. För detaljer, besök [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

När du skickar in en pull request kommer en CLA-bot automatiskt att avgöra om du behöver lämna in ett CLA och märka PR:n på lämpligt sätt (t.ex. statuskontroll, kommentar). Följ helt enkelt instruktionerna från boten. Du behöver bara göra detta en gång för alla repos som använder vårt CLA.

## Code of Conduct

Detta projekt har antagit [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
För mer information, läs [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) eller kontakta [opencode@microsoft.com](mailto:opencode@microsoft.com) om du har ytterligare frågor eller kommentarer.

## Cautions for creating issues

Vänligen öppna inte GitHub-ärenden för allmänna supportfrågor eftersom GitHub-listan bör användas för funktionsförfrågningar och bugg-rapporter. På så sätt kan vi enklare spåra faktiska problem eller buggar i koden och hålla allmän diskussion separat från själva koden.

## How to Contribute

### Pull Requests Guidelines

När du skickar in en pull request (PR) till Phi-3 CookBook-repositoriet, vänligen använd följande riktlinjer:

- **Forka repositoriet**: Forka alltid repositoriet till ditt eget konto innan du gör dina ändringar.

- **Separata pull requests (PR)**:
  - Skicka in varje typ av ändring i en egen pull request. Till exempel bör buggfixar och dokumentationsuppdateringar skickas i separata PR:er.
  - Stavfel och mindre dokumentationsuppdateringar kan kombineras i en enda PR där det är lämpligt.

- **Hantera merge-konflikter**: Om din pull request visar merge-konflikter, uppdatera din lokala `main`-gren för att spegla huvudrepositoriet innan du gör dina ändringar.

- **Översättningsbidrag**: När du skickar in en översättnings-PR, se till att översättningsmappen innehåller översättningar för alla filer i den ursprungliga mappen.

### Translation Guidelines

> [!IMPORTANT]
>
> När du översätter text i detta repository, använd inte maskinöversättning. Anmäl dig endast som volontär för översättningar på språk där du är skicklig.

Om du är skicklig i ett icke-engelskt språk kan du hjälpa till att översätta innehållet. Följ dessa steg för att säkerställa att dina översättningsbidrag integreras korrekt, använd följande riktlinjer:

- **Skapa översättningsmapp**: Navigera till rätt avsnittsmapp och skapa en översättningsmapp för det språk du bidrar till. Till exempel:
  - För introduktionsavsnittet: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - För snabbstartavsnittet: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Fortsätt med samma mönster för andra avsnitt (03.Inference, 04.Finetuning, osv.)

- **Uppdatera relativa sökvägar**: När du översätter, justera mappstrukturen genom att lägga till `../../` i början av relativa sökvägar inom markdown-filerna för att säkerställa att länkarna fungerar korrekt. Till exempel, ändra följande:
  - Ändra `(../../imgs/01/phi3aisafety.png)` till `(../../../../imgs/01/phi3aisafety.png)`

- **Organisera dina översättningar**: Varje översatt fil ska placeras i motsvarande avsnitts översättningsmapp. Till exempel, om du översätter introduktionsavsnittet till spanska, skulle du skapa följande:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Skicka in en komplett PR**: Se till att alla översatta filer för ett avsnitt ingår i en och samma PR. Vi accepterar inte partiella översättningar för ett avsnitt. När du skickar in en översättnings-PR, kontrollera att översättningsmappen innehåller översättningar för alla filer i den ursprungliga mappen.

### Writing Guidelines

För att säkerställa konsekvens i alla dokument, vänligen använd följande riktlinjer:

- **URL-formatering**: Sätt alla URL:er inom hakparenteser följt av parenteser, utan extra mellanslag runt eller inuti dem. Till exempel: `[example](https://www.microsoft.com)`.

- **Relativa länkar**: Använd `./` för relativa länkar som pekar på filer eller mappar i den aktuella katalogen, och `../` för sådana i en överordnad katalog. Till exempel: `[example](../../path/to/file)` eller `[example](../../../path/to/file)`.

- **Ej landspecifika lokaler**: Se till att dina länkar inte innehåller landspecifika lokaler. Undvik till exempel `/en-us/` eller `/en/`.

- **Bildlagring**: Spara alla bilder i `./imgs`-mappen.

- **Beskrivande bildnamn**: Namnge bilder beskrivande med engelska tecken, siffror och bindestreck. Till exempel: `example-image.jpg`.

## GitHub Workflows

När du skickar in en pull request kommer följande arbetsflöden att startas för att validera ändringarna. Följ instruktionerna nedan för att säkerställa att din pull request klarar arbetsflödeskontrollerna:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Detta arbetsflöde säkerställer att alla relativa sökvägar i dina filer är korrekta.

1. För att säkerställa att dina länkar fungerar korrekt, utför följande uppgifter med VS Code:
    - Hovra över vilken länk som helst i dina filer.
    - Tryck på **Ctrl + Klick** för att navigera till länken.
    - Om du klickar på en länk och den inte fungerar lokalt, kommer arbetsflödet att triggas och det fungerar inte på GitHub.

1. För att åtgärda detta problem, utför följande uppgifter med hjälp av sökvägsförslagen från VS Code:
    - Skriv `./` eller `../`.
    - VS Code kommer att be dig välja bland tillgängliga alternativ baserat på vad du skrev.
    - Följ sökvägen genom att klicka på önskad fil eller mapp för att säkerställa att din sökväg är korrekt.

När du har lagt till rätt relativa sökväg, spara och pusha dina ändringar.

### Check URLs Don't Have Locale

Detta arbetsflöde säkerställer att inga webbadresser innehåller landspecifika lokaler. Eftersom detta repository är tillgängligt globalt är det viktigt att säkerställa att URL:er inte innehåller ditt lands locale.

1. För att verifiera att dina URL:er inte har landslokaler, utför följande uppgifter:

    - Kontrollera efter text som `/en-us/`, `/en/` eller någon annan språklokal i URL:erna.
    - Om dessa inte finns i dina URL:er, klarar du kontrollen.

1. För att åtgärda detta problem, utför följande uppgifter:
    - Öppna filvägen som arbetsflödet markerat.
    - Ta bort landslokalen från URL:erna.

När du har tagit bort landslokalen, spara och pusha dina ändringar.

### Check Broken Urls

Detta arbetsflöde säkerställer att alla webbadresser i dina filer fungerar och returnerar statuskod 200.

1. För att verifiera att dina URL:er fungerar korrekt, utför följande uppgifter:
    - Kontrollera statusen för URL:erna i dina filer.

2. För att åtgärda trasiga URL:er, utför följande uppgifter:
    - Öppna filen som innehåller den trasiga URL:en.
    - Uppdatera URL:en till den korrekta.

När du har fixat URL:erna, spara och pusha dina ändringar.

> [!NOTE]
>
> Det kan finnas fall där URL-kontrollen misslyckas även om länken är åtkomlig. Detta kan bero på flera orsaker, bland annat:
>
> - **Nätverksbegränsningar:** GitHub Actions-servrar kan ha nätverksbegränsningar som hindrar åtkomst till vissa URL:er.
> - **Timeout-problem:** URL:er som tar för lång tid att svara kan orsaka timeout-fel i arbetsflödet.
> - **Tillfälliga serverproblem:** Tillfälliga driftstopp eller underhåll kan göra en URL tillfälligt otillgänglig under valideringen.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.