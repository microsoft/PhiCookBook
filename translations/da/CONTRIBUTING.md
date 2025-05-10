<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:40:45+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "da"
}
-->
# Bidrag

Dette projekt byder velkommen til bidrag og forslag. De fleste bidrag kræver, at du accepterer en Contributor License Agreement (CLA), der erklærer, at du har ret til, og faktisk giver os retten til at bruge dit bidrag. For detaljer, besøg [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Når du indsender en pull request, vil en CLA-bot automatisk afgøre, om du skal indsende en CLA og markere PR'en passende (fx statuscheck, kommentar). Følg blot instruktionerne fra botten. Du skal kun gøre dette én gang på tværs af alle repositories, der bruger vores CLA.

## Adfærdskodeks

Dette projekt har tilsluttet sig [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For mere information, læs [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) eller kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) med yderligere spørgsmål eller kommentarer.

## Forsigtighed ved oprettelse af issues

Undlad venligst at oprette GitHub issues til generelle supportspørgsmål, da GitHub-listen skal bruges til funktionsanmodninger og fejlrapporter. På den måde kan vi lettere spore faktiske problemer eller fejl i koden og holde den generelle diskussion adskilt fra den faktiske kode.

## Sådan bidrager du

### Retningslinjer for pull requests

Når du indsender en pull request (PR) til Phi-3 CookBook repository, bedes du følge disse retningslinjer:

- **Fork repositoryet**: Fork altid repositoryet til din egen konto, før du foretager ændringer.

- **Separate pull requests (PR)**:
  - Indsend hver type ændring i sin egen pull request. For eksempel bør fejlrettelser og dokumentationsopdateringer indsendes i separate PR’er.
  - Rettelser af tastefejl og mindre dokumentationsopdateringer kan kombineres i en enkelt PR, hvor det er passende.

- **Håndter merge-konflikter**: Hvis din pull request viser merge-konflikter, opdater din lokale `main` branch, så den matcher hovedrepositoryet, før du foretager ændringer.

- **Indsendelse af oversættelser**: Når du indsender en oversættelses-PR, skal du sikre, at oversættelsesmappen indeholder oversættelser for alle filer i den originale mappe.

### Retningslinjer for oversættelser

> [!IMPORTANT]
>
> Når du oversætter tekst i dette repository, må du ikke bruge maskinoversættelse. Frivillige oversættere bør kun bidrage på sprog, de behersker.

Hvis du mestrer et ikke-engelsk sprog, kan du hjælpe med at oversætte indholdet. Følg disse trin for at sikre, at dine oversættelsesbidrag integreres korrekt, og brug følgende retningslinjer:

- **Opret oversættelsesmappe**: Gå til den relevante afsnitsmappe, og opret en oversættelsesmappe for det sprog, du bidrager til. For eksempel:
  - For introduktionsafsnittet: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - For hurtigstart-afsnittet: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Fortsæt denne struktur for andre afsnit (03.Inference, 04.Finetuning osv.)

- **Opdater relative stier**: Når du oversætter, juster mappestrukturen ved at tilføje `../../` foran relative stier i markdown-filerne, så links fungerer korrekt. For eksempel, ændr:
  - `(../../imgs/01/phi3aisafety.png)` til `(../../../../imgs/01/phi3aisafety.png)`

- **Organiser dine oversættelser**: Hver oversat fil skal placeres i den tilsvarende afsnits oversættelsesmappe. For eksempel, hvis du oversætter introduktionsafsnittet til spansk, skal du oprette:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Indsend en komplet PR**: Sørg for, at alle oversatte filer for et afsnit er inkluderet i én PR. Vi accepterer ikke delvise oversættelser for et afsnit. Når du indsender en oversættelses-PR, skal du sikre, at oversættelsesmappen indeholder oversættelser for alle filer i den originale mappe.

### Skriveregler

For at sikre ensartethed på tværs af alle dokumenter, bedes du følge disse retningslinjer:

- **URL-formatering**: Indsæt alle URLs i firkantede parenteser efterfulgt af runde parenteser, uden ekstra mellemrum omkring eller inden i dem. For eksempel: `[example](https://www.microsoft.com)`.

- **Relative links**: Brug `./` for relative links, der peger på filer eller mapper i den aktuelle mappe, og `../` for links til en overordnet mappe. For eksempel: `[example](../../path/to/file)` eller `[example](../../../path/to/file)`.

- **Ikke landespecifikke lokaliteter**: Sørg for, at dine links ikke indeholder landespecifikke lokaliteter. Undgå for eksempel `/en-us/` eller `/en/`.

- **Billedopbevaring**: Gem alle billeder i `./imgs` mappen.

- **Beskrivende billednavne**: Navngiv billeder beskrivende med engelske bogstaver, tal og bindestreger. For eksempel: `example-image.jpg`.

## GitHub Workflows

Når du indsender en pull request, vil følgende workflows blive udløst for at validere ændringerne. Følg nedenstående instruktioner for at sikre, at din pull request består workflow-tjek:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Denne workflow sikrer, at alle relative stier i dine filer er korrekte.

1. For at sikre, at dine links fungerer korrekt, udfør følgende opgaver i VS Code:
    - Hold musen over ethvert link i dine filer.
    - Tryk **Ctrl + Klik** for at navigere til linket.
    - Hvis du klikker på et link, og det ikke virker lokalt, vil workflowen blive udløst, og det virker ikke på GitHub.

1. For at rette dette problem, udfør følgende opgaver med de sti-forslag, VS Code giver:
    - Skriv `./` eller `../`.
    - VS Code vil bede dig vælge blandt tilgængelige muligheder baseret på, hvad du skrev.
    - Følg stien ved at klikke på den ønskede fil eller mappe for at sikre, at stien er korrekt.

Når du har tilføjet den korrekte relative sti, skal du gemme og pushe dine ændringer.

### Check URLs Don't Have Locale

Denne workflow sikrer, at ingen web-URL indeholder en landespecifik lokalitet. Da dette repository er globalt tilgængeligt, er det vigtigt at sikre, at URLs ikke indeholder dit lands lokalitet.

1. For at kontrollere, at dine URLs ikke indeholder landelokaliteter, udfør følgende opgaver:

    - Tjek for tekst som `/en-us/`, `/en/` eller andre sprogrelaterede lokaliteter i URLs.
    - Hvis disse ikke findes i dine URLs, består du dette tjek.

1. For at rette dette problem, udfør følgende opgaver:
    - Åbn den filsti, som workflowen har fremhævet.
    - Fjern landelokaliteten fra URLs.

Når du har fjernet landelokaliteten, skal du gemme og pushe dine ændringer.

### Check Broken Urls

Denne workflow sikrer, at enhver web-URL i dine filer fungerer og returnerer statuskode 200.

1. For at kontrollere, at dine URLs fungerer korrekt, udfør følgende opgaver:
    - Tjek status for URLs i dine filer.

2. For at rette eventuelle brudte URLs, udfør følgende opgaver:
    - Åbn filen, der indeholder den brudte URL.
    - Opdater URL’en til den korrekte.

Når du har rettet URLs, skal du gemme og pushe dine ændringer.

> [!NOTE]
>
> Der kan være tilfælde, hvor URL-tjekket fejler, selvom linket er tilgængeligt. Dette kan skyldes flere årsager, herunder:
>
> - **Netværksbegrænsninger:** GitHub Actions-servere kan have netværksbegrænsninger, der forhindrer adgang til visse URLs.
> - **Timeout-problemer:** URLs, der tager for lang tid at svare, kan udløse timeout-fejl i workflowen.
> - **Midlertidige serverproblemer:** Tilfældig servernedetid eller vedligeholdelse kan gøre en URL midlertidigt utilgængelig under validering.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.