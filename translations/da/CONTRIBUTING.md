<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-16T14:42:14+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "da"
}
-->
# Bidrag

Dette projekt byder velkommen til bidrag og forslag. De fleste bidrag kræver, at du accepterer en Contributor License Agreement (CLA), der erklærer, at du har ret til, og faktisk giver os, rettighederne til at bruge dit bidrag. For detaljer, besøg [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Når du indsender en pull request, vil en CLA-bot automatisk afgøre, om du skal levere en CLA og markere PR'en passende (f.eks. statuscheck, kommentar). Følg blot instruktionerne fra botten. Du skal kun gøre dette én gang på tværs af alle repositories, der bruger vores CLA.

## Adfærdskodeks

Dette projekt har vedtaget [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
For mere information, læs [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) eller kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) med eventuelle yderligere spørgsmål eller kommentarer.

## Forsigtighed ved oprettelse af issues

Åbn venligst ikke GitHub issues for generelle supportspørgsmål, da GitHub-listen bør bruges til funktionsanmodninger og fejlrapporter. På den måde kan vi lettere spore faktiske problemer eller fejl i koden og holde den generelle diskussion adskilt fra den faktiske kode.

## Sådan bidrager du

### Retningslinjer for Pull Requests

Når du indsender en pull request (PR) til Phi-3 CookBook repository, bedes du følge disse retningslinjer:

- **Fork repositoryet**: Fork altid repositoryet til din egen konto, før du laver dine ændringer.

- **Separate pull requests (PR)**:
  - Indsend hver type ændring i sin egen pull request. For eksempel bør fejlrettelser og dokumentationsopdateringer indsendes i separate PR'er.
  - Rettelser af stavefejl og mindre dokumentationsopdateringer kan kombineres i en enkelt PR, hvor det er passende.

- **Håndtering af merge-konflikter**: Hvis din pull request viser merge-konflikter, opdater da din lokale `main`-gren, så den matcher hovedrepositoryet, før du laver dine ændringer.

- **Indsendelse af oversættelser**: Når du indsender en oversættelses-PR, skal du sikre, at oversættelsesmappen indeholder oversættelser for alle filer i den oprindelige mappe.

### Skriveretningslinjer

For at sikre konsistens på tværs af alle dokumenter, bedes du følge disse retningslinjer:

- **URL-formatering**: Indsæt alle URL'er i firkantede parenteser efterfulgt af runde parenteser, uden ekstra mellemrum omkring eller indeni. For eksempel: `[example](https://www.microsoft.com)`.

- **Relative links**: Brug `./` for relative links, der peger på filer eller mapper i den aktuelle mappe, og `../` for dem i en overordnet mappe. For eksempel: `[example](../../path/to/file)` eller `[example](../../../path/to/file)`.

- **Ikke landespecifikke lokaliteter**: Sørg for, at dine links ikke indeholder landespecifikke lokaliteter. For eksempel undgå `/en-us/` eller `/en/`.

- **Billedlagring**: Gem alle billeder i `./imgs` mappen.

- **Beskrivende billednavne**: Navngiv billeder beskrivende med engelske tegn, tal og bindestreger. For eksempel: `example-image.jpg`.

## GitHub Workflows

Når du indsender en pull request, vil følgende workflows blive aktiveret for at validere ændringerne. Følg instruktionerne nedenfor for at sikre, at din pull request består workflow-tjek:

- [Check Broken Relative Paths](../..)  
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Denne workflow sikrer, at alle relative stier i dine filer er korrekte.

1. For at sikre, at dine links fungerer korrekt, udfør følgende opgaver i VS Code:  
    - Hold musen over et link i dine filer.  
    - Tryk på **Ctrl + Klik** for at navigere til linket.  
    - Hvis du klikker på et link, og det ikke virker lokalt, vil det udløse workflowet og heller ikke virke på GitHub.

1. For at rette dette problem, udfør følgende opgaver ved hjælp af sti-forslagene fra VS Code:  
    - Skriv `./` eller `../`.  
    - VS Code vil foreslå valgmuligheder baseret på det, du har skrevet.  
    - Følg stien ved at klikke på den ønskede fil eller mappe for at sikre, at din sti er korrekt.

Når du har tilføjet den korrekte relative sti, gem og push dine ændringer.

### Check URLs Don't Have Locale

Denne workflow sikrer, at web-URL'er ikke indeholder landespecifikke lokaliteter. Da dette repository er tilgængeligt globalt, er det vigtigt at sikre, at URL'er ikke indeholder din landslokalitet.

1. For at kontrollere, at dine URL'er ikke har landespecifikke lokaliteter, udfør følgende:  
    - Tjek for tekst som `/en-us/`, `/en/` eller andre sproglokaliteter i URL'erne.  
    - Hvis disse ikke findes i dine URL'er, består du tjekket.

1. For at rette dette problem, udfør følgende:  
    - Åbn den filsti, som workflowet har markeret.  
    - Fjern landeslokaliteten fra URL'erne.

Når du har fjernet landeslokaliteten, gem og push dine ændringer.

### Check Broken Urls

Denne workflow sikrer, at alle web-URL'er i dine filer fungerer og returnerer statuskode 200.

1. For at kontrollere, at dine URL'er fungerer korrekt, udfør følgende:  
    - Tjek status for URL'erne i dine filer.

2. For at rette eventuelle ødelagte URL'er, udfør følgende:  
    - Åbn filen, der indeholder den ødelagte URL.  
    - Opdater URL'en til den korrekte.

Når du har rettet URL'erne, gem og push dine ændringer.

> [!NOTE]  
>  
> Der kan være tilfælde, hvor URL-tjekket fejler, selvom linket er tilgængeligt. Dette kan ske af flere årsager, herunder:  
>  
> - **Netværksbegrænsninger:** GitHub actions-servere kan have netværksbegrænsninger, der forhindrer adgang til visse URL'er.  
> - **Timeout-problemer:** URL'er, der tager for lang tid at svare, kan udløse en timeout-fejl i workflowet.  
> - **Midlertidige serverproblemer:** Periodisk nedetid eller vedligeholdelse kan gøre en URL midlertidigt utilgængelig under valideringen.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.