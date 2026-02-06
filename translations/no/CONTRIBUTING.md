# Bidra

Dette prosjektet ønsker bidrag og forslag velkommen. De fleste bidrag krever at du godtar en Contributor License Agreement (CLA) som bekrefter at du har rettighetene til, og faktisk gir oss, rettighetene til å bruke ditt bidrag. For detaljer, besøk [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Når du sender inn en pull request, vil en CLA-bot automatisk avgjøre om du må levere en CLA og merke PR-en deretter (f.eks. statuskontroll, kommentar). Følg bare instruksjonene gitt av boten. Du trenger kun å gjøre dette én gang for alle repos som bruker vår CLA.

## Adferdskodeks

Dette prosjektet har tatt i bruk [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
For mer informasjon, les [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) eller kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) ved spørsmål eller kommentarer.

## Forsiktighetsregler ved opprettelse av issues

Vennligst ikke opprett GitHub-issues for generelle supportspørsmål, da GitHub-listen skal brukes til funksjonsforespørsler og feilrapporter. På denne måten kan vi lettere spore faktiske problemer eller feil i koden og holde generell diskusjon adskilt fra selve koden.

## Hvordan bidra

### Retningslinjer for pull requests

Når du sender inn en pull request (PR) til Phi-3 CookBook-repositoriet, vennligst følg disse retningslinjene:

- **Fork repositoriet**: Alltid fork repositoriet til din egen konto før du gjør endringer.

- **Separate pull requests (PR)**:
  - Send hver type endring i sin egen pull request. For eksempel bør feilrettinger og dokumentasjonsoppdateringer sendes i separate PR-er.
  - Rettelser av skrivefeil og mindre dokumentasjonsoppdateringer kan kombineres i én PR der det passer.

- **Håndter merge-konflikter**: Hvis pull requesten din viser merge-konflikter, oppdater din lokale `main`-gren for å speile hovedrepositoriet før du gjør endringer.

- **Oversettelsesinnleveringer**: Når du sender inn en oversettelses-PR, sørg for at oversettelsesmappen inkluderer oversettelser for alle filer i originalmappen.

### Skriveretningslinjer

For å sikre konsistens i alle dokumenter, vennligst bruk følgende retningslinjer:

- **URL-formatering**: Pakk alle URL-er inn i hakeparenteser etterfulgt av parenteser, uten ekstra mellomrom rundt eller inni. For eksempel: `[example](https://www.microsoft.com)`.

- **Relative lenker**: Bruk `./` for relative lenker som peker til filer eller mapper i gjeldende katalog, og `../` for de i en overordnet katalog. For eksempel: `[example](../../path/to/file)` eller `[example](../../../path/to/file)`.

- **Ikke landsspesifikke lokaliteter**: Sørg for at lenkene dine ikke inneholder landsspesifikke lokaliteter. For eksempel, unngå `/en-us/` eller `/en/`.

- **Bildeoppbevaring**: Lagre alle bilder i `./imgs`-mappen.

- **Beskrivende bildnavn**: Gi bilder beskrivende navn med engelske bokstaver, tall og bindestreker. For eksempel: `example-image.jpg`.

## GitHub Workflows

Når du sender inn en pull request, vil følgende workflows bli utløst for å validere endringene. Følg instruksjonene under for å sikre at pull requesten din passerer workflow-sjekkene:

- [Check Broken Relative Paths](../..)  
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Denne workflowen sikrer at alle relative stier i filene dine er korrekte.

1. For å sikre at lenkene dine fungerer som de skal, gjør følgende i VS Code:
    - Hold musepekeren over en lenke i filene dine.
    - Trykk **Ctrl + Klikk** for å navigere til lenken.
    - Hvis du klikker på en lenke og den ikke fungerer lokalt, vil workflowen bli utløst og lenken vil ikke fungere på GitHub.

1. For å fikse dette, gjør følgende med stiforslagene fra VS Code:
    - Skriv `./` eller `../`.
    - VS Code vil foreslå tilgjengelige alternativer basert på det du skrev.
    - Følg stien ved å klikke på ønsket fil eller mappe for å sikre at stien er korrekt.

Når du har lagt til riktig relativ sti, lagre og push endringene dine.

### Check URLs Don't Have Locale

Denne workflowen sikrer at ingen nettadresser inneholder landsspesifikke lokaliteter. Siden dette repositoriet er tilgjengelig globalt, er det viktig at URL-er ikke inneholder lokalitet for ditt land.

1. For å verifisere at URL-ene dine ikke har landsspesifikke lokaliteter, gjør følgende:

    - Sjekk etter tekst som `/en-us/`, `/en/` eller andre språkspesifikke lokaliteter i URL-ene.
    - Hvis disse ikke finnes i URL-ene dine, vil du bestå denne sjekken.

1. For å fikse dette, gjør følgende:
    - Åpne filstien som workflowen har markert.
    - Fjern landsspesifikk lokalitet fra URL-ene.

Når du har fjernet lokaliteten, lagre og push endringene dine.

### Check Broken Urls

Denne workflowen sikrer at alle nettadresser i filene dine fungerer og returnerer statuskode 200.

1. For å verifisere at URL-ene dine fungerer korrekt, gjør følgende:
    - Sjekk statusen til URL-ene i filene dine.

2. For å fikse eventuelle ødelagte URL-er, gjør følgende:
    - Åpne filen som inneholder den ødelagte URL-en.
    - Oppdater URL-en til den korrekte.

Når du har fikset URL-ene, lagre og push endringene dine.

> [!NOTE]  
> Det kan forekomme tilfeller der URL-sjekken feiler selv om lenken er tilgjengelig. Dette kan skje av flere grunner, blant annet:  
>  
> - **Nettverksbegrensninger:** GitHub Actions-servere kan ha nettverksbegrensninger som hindrer tilgang til enkelte URL-er.  
> - **Timeout-problemer:** URL-er som bruker for lang tid på å svare kan utløse timeout-feil i workflowen.  
> - **Midlertidige serverproblemer:** Periodisk nedetid eller vedlikehold kan gjøre en URL midlertidig utilgjengelig under validering.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.