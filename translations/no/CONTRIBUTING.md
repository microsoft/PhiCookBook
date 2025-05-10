<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:41:01+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "no"
}
-->
# Bidra

Dette prosjektet ønsker bidrag og forslag velkommen. De fleste bidrag krever at du godtar en Contributor License Agreement (CLA) som bekrefter at du har rett til, og faktisk gir oss, rettighetene til å bruke ditt bidrag. For detaljer, besøk [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Når du sender inn en pull request, vil en CLA-bot automatisk avgjøre om du må levere en CLA og merke PR-en deretter (f.eks. statuskontroll, kommentar). Følg bare instruksjonene fra boten. Du trenger kun å gjøre dette én gang for alle repoer som bruker vår CLA.

## Adferdskodeks

Dette prosjektet har tatt i bruk [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For mer informasjon, les [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) eller kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) med spørsmål eller kommentarer.

## Viktig ved opprettelse av issues

Vennligst ikke opprett GitHub-issues for generelle supportspørsmål, da GitHub-listen skal brukes til funksjonsforespørsler og feilrapporter. På denne måten kan vi lettere spore faktiske problemer eller feil i koden og holde generell diskusjon adskilt fra selve koden.

## Hvordan bidra

### Retningslinjer for pull requests

Når du sender inn en pull request (PR) til Phi-3 CookBook-repositoriet, vennligst følg disse retningslinjene:

- **Fork repositoriet**: Alltid fork repositoriet til din egen konto før du gjør endringer.

- **Separate pull requests (PR)**:
  - Send hver type endring i sin egen pull request. For eksempel bør feilrettinger og dokumentasjonsoppdateringer sendes i separate PR-er.
  - Små skrivefeil og mindre dokumentasjonsoppdateringer kan kombineres i én PR der det passer.

- **Håndter merge-konflikter**: Hvis din pull request viser merge-konflikter, oppdater din lokale `main` branch for å speile hovedrepositoriet før du gjør endringer.

- **Innsending av oversettelser**: Når du sender inn en oversettelses-PR, sørg for at oversettelsesmappen inkluderer oversettelser for alle filer i den opprinnelige mappen.

### Retningslinjer for oversettelse

> [!IMPORTANT]
>
> Når du oversetter tekst i dette repositoriet, ikke bruk maskinoversettelse. Meld deg kun som frivillig for oversettelser i språk du behersker godt.

Hvis du er dyktig i et ikke-engelsk språk, kan du hjelpe med oversettelse av innholdet. Følg disse stegene for å sikre at oversettelsesbidragene dine blir riktig integrert, og bruk følgende retningslinjer:

- **Opprett oversettelsesmapp**: Gå til riktig seksjonsmappe og lag en oversettelsesmapp for språket du bidrar til. For eksempel:
  - For introduksjonsseksjonen: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - For rask start-seksjonen: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Fortsett på samme måte for andre seksjoner (03.Inference, 04.Finetuning, osv.)

- **Oppdater relative stier**: Når du oversetter, juster mappestrukturen ved å legge til `../../` foran relative stier i markdown-filene for å sikre at lenker fungerer riktig. For eksempel, endre:
  - Fra `(../../imgs/01/phi3aisafety.png)` til `(../../../../imgs/01/phi3aisafety.png)`

- **Organiser oversettelsene dine**: Hver oversatt fil skal plasseres i riktig seksjons oversettelsesmapp. For eksempel, hvis du oversetter introduksjonsseksjonen til spansk, lager du som følger:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Send inn en komplett PR**: Sørg for at alle oversatte filer for en seksjon er inkludert i én PR. Vi godtar ikke delvise oversettelser for en seksjon. Når du sender inn en oversettelses-PR, sørg for at oversettelsesmappen inkluderer oversettelser for alle filer i originalmappen.

### Skriveretningslinjer

For å sikre konsistens på tvers av alle dokumenter, vennligst følg disse retningslinjene:

- **URL-formatering**: Pakk alle URL-er i firkantede parenteser etterfulgt av vanlige parenteser, uten ekstra mellomrom rundt eller inni. For eksempel: `[example](https://www.microsoft.com)`.

- **Relative lenker**: Bruk `./` for relative lenker til filer eller mapper i gjeldende katalog, og `../` for de i en overordnet katalog. For eksempel: `[example](../../path/to/file)` eller `[example](../../../path/to/file)`.

- **Ikke lands-spesifikke lokaliteter**: Sørg for at lenkene dine ikke inneholder lands-spesifikke lokaliteter. For eksempel, unngå `/en-us/` eller `/en/`.

- **Bilde-lagring**: Lagre alle bilder i `./imgs`-mappen.

- **Beskrivende bildnavn**: Gi bilder beskrivende navn med engelske bokstaver, tall og bindestreker. For eksempel: `example-image.jpg`.

## GitHub arbeidsflyter

Når du sender inn en pull request, vil følgende arbeidsflyter bli trigget for å validere endringene. Følg instruksjonene nedenfor for å sikre at pull requesten din passerer arbeidsflytsjekkene:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Denne arbeidsflyten sørger for at alle relative stier i filene dine er korrekte.

1. For å sikre at lenkene dine fungerer som de skal, gjør følgende i VS Code:
    - Hold musepekeren over en lenke i filene dine.
    - Trykk **Ctrl + Klikk** for å navigere til lenken.
    - Hvis du klikker på en lenke og den ikke fungerer lokalt, vil det utløse arbeidsflyten og ikke fungere på GitHub.

1. For å fikse dette, gjør følgende med stiforslagene fra VS Code:
    - Skriv `./` eller `../`.
    - VS Code vil foreslå valg basert på det du skrev.
    - Følg stien ved å klikke på ønsket fil eller mappe for å sikre at stien er riktig.

Når du har lagt til korrekt relativ sti, lagre og push endringene dine.

### Check URLs Don't Have Locale

Denne arbeidsflyten sikrer at ingen web-URL-er inneholder lands-spesifikke lokaliteter. Siden dette repositoriet er tilgjengelig globalt, er det viktig at URL-er ikke inneholder lokaliteter for ditt land.

1. For å verifisere at URL-ene dine ikke har landslokaliteter, gjør følgende:

    - Sjekk etter tekst som `/en-us/`, `/en/`, eller andre språk-lokaliteter i URL-ene.
    - Hvis disse ikke finnes i URL-ene dine, vil du bestå sjekken.

1. For å fikse dette, gjør følgende:
    - Åpne filen som er markert av arbeidsflyten.
    - Fjern landslokaliteten fra URL-ene.

Når du har fjernet landslokaliteten, lagre og push endringene dine.

### Check Broken Urls

Denne arbeidsflyten sikrer at alle web-URL-er i filene dine fungerer og returnerer statuskode 200.

1. For å verifisere at URL-ene dine fungerer korrekt, gjør følgende:
    - Sjekk statusen til URL-ene i filene dine.

2. For å fikse eventuelle ødelagte URL-er, gjør følgende:
    - Åpne filen som inneholder den ødelagte URL-en.
    - Oppdater URL-en til korrekt adresse.

Når du har fikset URL-ene, lagre og push endringene dine.

> [!NOTE]
>
> Det kan være tilfeller der URL-sjekken feiler selv om lenken er tilgjengelig. Dette kan skyldes flere grunner, inkludert:
>
> - **Nettverksbegrensninger:** GitHub actions-servere kan ha nettverksbegrensninger som hindrer tilgang til visse URL-er.
> - **Timeout-problemer:** URL-er som bruker for lang tid på å svare kan utløse timeout-feil i arbeidsflyten.
> - **Midlertidige serverproblemer:** Periodisk servernedetid eller vedlikehold kan gjøre en URL midlertidig utilgjengelig under validering.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.