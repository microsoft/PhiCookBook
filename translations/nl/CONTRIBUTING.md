<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-09T18:32:38+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "nl"
}
-->
# Bijdragen

Dit project verwelkomt bijdragen en suggesties. De meeste bijdragen vereisen dat je akkoord gaat met een Contributor License Agreement (CLA) waarin je verklaart dat je het recht hebt om, en daadwerkelijk, ons de rechten verleent om jouw bijdrage te gebruiken. Voor meer informatie, bezoek [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Wanneer je een pull request indient, bepaalt een CLA-bot automatisch of je een CLA moet aanleveren en voorziet het PR van de juiste aanduidingen (bijv. statuscontrole, commentaar). Volg gewoon de instructies van de bot. Dit hoef je maar één keer te doen voor alle repositories die onze CLA gebruiken.

## Gedragscode

Dit project heeft de [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) aangenomen.  
Voor meer informatie, lees de [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) of neem contact op via [opencode@microsoft.com](mailto:opencode@microsoft.com) bij vragen of opmerkingen.

## Waarschuwingen bij het aanmaken van issues

Open alsjeblieft geen GitHub-issues voor algemene ondersteuningsvragen, aangezien de GitHub-lijst bedoeld is voor functieverzoeken en bugrapporten. Zo kunnen we daadwerkelijke problemen of bugs in de code beter volgen en houden we algemene discussies gescheiden van de code zelf.

## Hoe bij te dragen

### Richtlijnen voor Pull Requests

Bij het indienen van een pull request (PR) voor de Phi-3 CookBook repository, gebruik je de volgende richtlijnen:

- **Fork de repository**: Fork altijd de repository naar je eigen account voordat je wijzigingen aanbrengt.

- **Gescheiden pull requests (PR)**:
  - Dien elk type wijziging in een aparte pull request in. Bijvoorbeeld, bugfixes en documentatie-updates moeten in aparte PR’s worden ingediend.
  - Typfouten en kleine documentatie-aanpassingen kunnen waar passend gecombineerd worden in één PR.

- **Omgaan met merge-conflicten**: Als je pull request merge-conflicten vertoont, werk dan je lokale `main` branch bij zodat deze overeenkomt met de hoofdrepository voordat je je wijzigingen aanbrengt.

- **Vertalingen indienen**: Zorg er bij het indienen van een vertaal-PR voor dat de vertaalmap vertalingen bevat voor alle bestanden uit de originele map.

### Schrijfrichtlijnen

Om consistentie in alle documenten te waarborgen, gebruik je de volgende richtlijnen:

- **URL-opmaak**: Plaats alle URL’s tussen vierkante haken gevolgd door ronde haakjes, zonder extra spaties eromheen. Bijvoorbeeld: `[example](https://www.microsoft.com)`.

- **Relatieve links**: Gebruik `./` voor relatieve links naar bestanden of mappen in de huidige directory, en `../` voor die in een bovenliggende directory. Bijvoorbeeld: `[example](../../path/to/file)` of `[example](../../../path/to/file)`.

- **Niet land-specifieke locale**: Zorg dat je links geen land-specifieke locale bevatten. Vermijd bijvoorbeeld `/en-us/` of `/en/`.

- **Afbeeldingen opslaan**: Bewaar alle afbeeldingen in de map `./imgs`.

- **Beschrijvende afbeeldingsnamen**: Geef afbeeldingen beschrijvende namen met Engelse letters, cijfers en streepjes. Bijvoorbeeld: `example-image.jpg`.

## GitHub Workflows

Wanneer je een pull request indient, worden de volgende workflows geactiveerd om de wijzigingen te valideren. Volg de onderstaande instructies om ervoor te zorgen dat je pull request de workflow-controles doorstaat:

- [Check Broken Relative Paths](../..)  
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Deze workflow controleert of alle relatieve paden in je bestanden correct zijn.

1. Om te controleren of je links goed werken, voer je de volgende taken uit met VS Code:
    - Beweeg met je muis over een link in je bestanden.
    - Druk op **Ctrl + Klik** om naar de link te navigeren.
    - Als je op een link klikt en deze werkt niet lokaal, zal dit de workflow activeren en werkt het ook niet op GitHub.

1. Om dit probleem op te lossen, voer je de volgende taken uit met de pad-suggesties van VS Code:
    - Typ `./` of `../`.
    - VS Code zal je opties tonen op basis van wat je hebt getypt.
    - Volg het pad door te klikken op het gewenste bestand of map om te controleren of je pad klopt.

Zodra je het juiste relatieve pad hebt toegevoegd, sla je op en push je je wijzigingen.

### Check URLs Don't Have Locale

Deze workflow controleert of web-URL’s geen land-specifieke locale bevatten. Omdat deze repository wereldwijd toegankelijk is, is het belangrijk dat URL’s geen land-specifieke locale bevatten.

1. Om te controleren of je URL’s geen land-locales bevatten, voer je de volgende taken uit:

    - Controleer op tekst zoals `/en-us/`, `/en/` of andere taal-locales in de URL’s.
    - Als deze niet aanwezig zijn, sla je deze controle.

1. Om dit probleem op te lossen, voer je de volgende taken uit:
    - Open het bestandspad dat door de workflow is gemarkeerd.
    - Verwijder de land-locale uit de URL’s.

Zodra je de land-locale hebt verwijderd, sla je op en push je je wijzigingen.

### Check Broken Urls

Deze workflow controleert of alle web-URL’s in je bestanden werken en een statuscode 200 teruggeven.

1. Om te controleren of je URL’s correct werken, voer je de volgende taken uit:
    - Controleer de status van de URL’s in je bestanden.

2. Om gebroken URL’s te repareren, voer je de volgende taken uit:
    - Open het bestand met de gebroken URL.
    - Werk de URL bij naar de juiste.

Zodra je de URL’s hebt aangepast, sla je op en push je je wijzigingen.

> [!NOTE]  
>  
> Er kunnen situaties zijn waarin de URL-controle faalt, ook al is de link bereikbaar. Dit kan verschillende oorzaken hebben, waaronder:  
>  
> - **Netwerkbeperkingen:** GitHub Actions-servers kunnen netwerkbeperkingen hebben die toegang tot bepaalde URL’s blokkeren.  
> - **Timeoutproblemen:** URL’s die te lang nodig hebben om te reageren, kunnen een time-out veroorzaken in de workflow.  
> - **Tijdelijke serverproblemen:** Incidentele serverstoringen of onderhoud kunnen een URL tijdelijk onbereikbaar maken tijdens de validatie.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.