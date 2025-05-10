<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:41:35+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "nl"
}
-->
# Bijdragen

Dit project verwelkomt bijdragen en suggesties. Voor de meeste bijdragen moet je akkoord gaan met een Contributor License Agreement (CLA) waarin je verklaart dat je het recht hebt om ons de rechten te geven om je bijdrage te gebruiken. Voor meer details, bezoek [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Wanneer je een pull request indient, bepaalt een CLA-bot automatisch of je een CLA moet aanleveren en voorziet het PR van de juiste aanduidingen (bijv. statuscontrole, commentaar). Volg simpelweg de instructies van de bot. Dit hoef je slechts één keer te doen voor alle repositories die onze CLA gebruiken.

## Gedragscode

Dit project heeft de [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) aangenomen.  
Voor meer informatie lees de [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) of neem contact op via [opencode@microsoft.com](mailto:opencode@microsoft.com) bij vragen of opmerkingen.

## Waarschuwingen bij het aanmaken van issues

Open alsjeblieft geen GitHub-issues voor algemene ondersteuningsvragen, aangezien de GitHub-lijst bedoeld is voor functieverzoeken en bugrapporten. Zo kunnen we echte problemen of bugs in de code beter volgen en houden we algemene discussies gescheiden van de daadwerkelijke code.

## Hoe bij te dragen

### Richtlijnen voor Pull Requests

Bij het indienen van een pull request (PR) voor de Phi-3 CookBook repository, gebruik de volgende richtlijnen:

- **Fork de repository**: Fork altijd de repository naar je eigen account voordat je wijzigingen aanbrengt.

- **Gescheiden pull requests (PR)**:
  - Dien elk type wijziging in een aparte pull request in. Bijvoorbeeld, bugfixes en documentatie-updates moeten in aparte PR's worden ingediend.
  - Typfouten en kleine documentatie-aanpassingen kunnen waar passend worden gecombineerd in één PR.

- **Omgaan met merge-conflicten**: Als je pull request merge-conflicten vertoont, werk dan je lokale `main` branch bij zodat deze overeenkomt met de hoofdrepository voordat je wijzigingen aanbrengt.

- **Vertalingen indienen**: Zorg er bij het indienen van een vertalings-PR voor dat de vertaalmap vertalingen bevat voor alle bestanden in de originele map.

### Richtlijnen voor vertalingen

> [!IMPORTANT]
>
> Gebruik bij het vertalen van tekst in deze repository geen machinale vertaling. Doe alleen vrijwilligerswerk voor vertalingen in talen waarin je vaardig bent.

Als je een niet-Engelse taal beheerst, kun je helpen met het vertalen van de inhoud. Volg deze stappen om ervoor te zorgen dat je vertaalbijdragen goed worden geïntegreerd:

- **Maak een vertaalmap aan**: Ga naar de juiste sectiemap en maak een vertaalmap aan voor de taal waarin je bijdraagt. Bijvoorbeeld:
  - Voor de introductiesectie: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Voor de quick start sectie: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Volg dit patroon voor andere secties (03.Inference, 04.Finetuning, enz.)

- **Werk relatieve paden bij**: Pas bij het vertalen de mappenstructuur aan door `../../` aan het begin van relatieve paden in de markdownbestanden toe te voegen zodat links correct werken. Bijvoorbeeld, verander:
  - `(../../imgs/01/phi3aisafety.png)` naar `(../../../../imgs/01/phi3aisafety.png)`

- **Organiseer je vertalingen**: Elk vertaald bestand moet in de vertaalmap van de bijbehorende sectie worden geplaatst. Bijvoorbeeld, als je de introductiesectie in het Spaans vertaalt, maak je het volgende aan:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Dien een complete PR in**: Zorg ervoor dat alle vertaalde bestanden voor een sectie in één PR zijn opgenomen. We accepteren geen gedeeltelijke vertalingen per sectie. Bij het indienen van een vertaal-PR moet de vertaalmap vertalingen voor alle bestanden in de originele map bevatten.

### Schrijfrichtlijnen

Om consistentie in alle documenten te waarborgen, gebruik de volgende richtlijnen:

- **URL-formattering**: Plaats alle URL's tussen vierkante haken gevolgd door haakjes, zonder extra spaties eromheen of erin. Bijvoorbeeld: `[example](https://www.microsoft.com)`.

- **Relatieve links**: Gebruik `./` voor relatieve links naar bestanden of mappen in de huidige directory, en `../` voor die in een bovenliggende directory. Bijvoorbeeld: `[example](../../path/to/file)` of `[example](../../../path/to/file)`.

- **Geen land-specifieke locale**: Zorg ervoor dat je links geen land-specifieke locale bevatten. Vermijd bijvoorbeeld `/en-us/` of `/en/`.

- **Afbeeldingen opslaan**: Bewaar alle afbeeldingen in de `./imgs` map.

- **Beschrijvende afbeeldingsnamen**: Geef afbeeldingen beschrijvende namen met Engelse letters, cijfers en streepjes. Bijvoorbeeld: `example-image.jpg`.

## GitHub Workflows

Wanneer je een pull request indient, worden de volgende workflows geactiveerd om de wijzigingen te valideren. Volg onderstaande instructies om ervoor te zorgen dat je pull request slaagt bij de workflow-controles:

- [Controleer gebroken relatieve paden](../..)
- [Controleer of URL's geen locale bevatten](../..)

### Controleer gebroken relatieve paden

Deze workflow controleert of alle relatieve paden in je bestanden correct zijn.

1. Om te controleren of je links correct werken, voer je de volgende taken uit met VS Code:
    - Beweeg de muis over een link in je bestanden.
    - Druk op **Ctrl + Klik** om naar de link te navigeren.
    - Als je op een link klikt en deze werkt lokaal niet, zal de workflow geactiveerd worden en werkt het ook niet op GitHub.

1. Om dit probleem op te lossen, voer je de volgende taken uit met behulp van de pad-suggesties van VS Code:
    - Typ `./` of `../`.
    - VS Code geeft je opties op basis van wat je hebt getypt.
    - Volg het pad door te klikken op het gewenste bestand of de gewenste map om zeker te zijn dat je pad correct is.

Sla je wijzigingen op en push ze zodra je het juiste relatieve pad hebt toegevoegd.

### Controleer of URL's geen locale bevatten

Deze workflow controleert of web-URL's geen land-specifieke locale bevatten. Aangezien deze repository wereldwijd toegankelijk is, is het belangrijk dat URL's geen landlocale bevatten.

1. Om te controleren dat je URL's geen landlocale bevatten, voer je de volgende taken uit:

    - Controleer op tekst zoals `/en-us/`, `/en/` of andere taallocales in de URL's.
    - Als deze niet aanwezig zijn, slaag je voor deze controle.

1. Om dit probleem op te lossen, voer je de volgende taken uit:
    - Open het bestandspad dat door de workflow is gemarkeerd.
    - Verwijder de landlocale uit de URL's.

Sla je wijzigingen op en push ze zodra je de landlocale hebt verwijderd.

### Controleer gebroken URL's

Deze workflow controleert of alle web-URL's in je bestanden werken en een statuscode 200 teruggeven.

1. Om te controleren of je URL's correct werken, voer je de volgende taken uit:
    - Controleer de status van de URL's in je bestanden.

2. Om gebroken URL's te herstellen, voer je de volgende taken uit:
    - Open het bestand met de gebroken URL.
    - Werk de URL bij naar de juiste.

Sla je wijzigingen op en push ze zodra je de URL's hebt hersteld.

> [!NOTE]
>
> Het kan voorkomen dat de URL-controle faalt terwijl de link wel toegankelijk is. Dit kan verschillende oorzaken hebben, waaronder:
>
> - **Netwerkrestricties:** GitHub Actions-servers kunnen netwerkrestricties hebben die toegang tot bepaalde URL's blokkeren.
> - **Timeout-problemen:** URL's die te lang duren om te reageren kunnen een time-out veroorzaken in de workflow.
> - **Tijdelijke serverproblemen:** Af en toe kan een server tijdelijk onbereikbaar zijn vanwege onderhoud of storingen tijdens de validatie.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.