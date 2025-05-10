<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:41:17+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "fi"
}
-->
# Contributing

Tämä projekti ottaa mielellään vastaan panoksia ja ehdotuksia. Useimmat panokset edellyttävät, että hyväksyt Contributor License Agreementin (CLA), jossa vahvistat, että sinulla on oikeus ja että todella myönnät meille oikeudet käyttää panostasi. Lisätietoja saat osoitteesta [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Kun lähetät pull requestin, CLA-botti määrittää automaattisesti, tarvitsetko CLA:n ja merkitsee PR:n asianmukaisesti (esim. tilantarkistus, kommentti). Noudata vain botin antamia ohjeita. Tätä tarvitaan vain kerran kaikissa CLA:ta käyttävissä repositorioissa.

## Code of Conduct

Tämä projekti on ottanut käyttöön [Microsoft Open Source Code of Conductin](https://opensource.microsoft.com/codeofconduct/).
Lisätietoja löydät lukemalla [Code of Conduct FAQ:n](https://opensource.microsoft.com/codeofconduct/faq/) tai ottamalla yhteyttä osoitteeseen [opencode@microsoft.com](mailto:opencode@microsoft.com) mahdollisissa lisäkysymyksissä tai kommenteissa.

## Cautions for creating issues

Älä avaa GitHub-issueita yleisiin tukikysymyksiin, sillä GitHub-listaa tulisi käyttää ominaisuuspyyntöihin ja bugiraportteihin. Näin voimme helpommin seurata varsinaisia ongelmia tai virheitä koodissa ja pitää yleisen keskustelun erillään varsinaisesta koodista.

## How to Contribute

### Pull Requests Guidelines

Kun lähetät pull requestin (PR) Phi-3 CookBook -repositorioosi, käytä seuraavia ohjeita:

- **Forkkaa repositorio**: Forkkaa aina repositorio omaan tiliisi ennen kuin teet muutoksia.

- **Eri pull requestit (PR)**:
  - Lähetä jokainen muutos omassa pull requestissaan. Esimerkiksi bugikorjaukset ja dokumentaatiopäivitykset tulisi lähettää erillisinä PR:inä.
  - Kirjoitusvirheiden korjaukset ja pienet dokumentaatiopäivitykset voi tarvittaessa yhdistää yhdeksi PR:iksi.

- **Ratkaise merge-konfliktit**: Jos pull requestissasi on merge-konflikteja, päivitä paikallinen `main`-haara vastaamaan päärepositoriota ennen muutosten tekemistä.

- **Käännösten lähettäminen**: Kun lähetät käännöksen PR:nä, varmista, että käännöskansio sisältää käännökset kaikista alkuperäisen kansion tiedostoista.

### Translation Guidelines

> [!IMPORTANT]
>
> Kun käännät tekstiä tässä repositoriossa, älä käytä konekäännöstä. Osallistu käännöksiin vain kielillä, joita hallitset hyvin.

Jos hallitset jonkin muun kuin englannin kielen, voit auttaa kääntämään sisältöä. Noudata seuraavia ohjeita, jotta käännöspanoksesi integroidaan oikein:

- **Luo käännöskansio**: Siirry oikeaan osion kansioon ja luo käännöskansio kielelle, johon käännät. Esimerkiksi:
  - Johdanto-osioon: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Quick start -osioon: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Jatka samalla kaavalla muihin osioihin (03.Inference, 04.Finetuning jne.)

- **Päivitä suhteelliset polut**: Kääntäessäsi muokkaa kansion rakennetta lisäämällä `../../` suhteellisten polkujen alkuun markdown-tiedostoissa, jotta linkit toimivat oikein. Esimerkiksi vaihda:
  - `(../../imgs/01/phi3aisafety.png)` muotoon `(../../../../imgs/01/phi3aisafety.png)`

- **Järjestä käännöksesi**: Kukin käännetty tiedosto tulisi sijoittaa vastaavan osion käännöskansioon. Esimerkiksi jos käännät johdanto-osion espanjaksi, luot kansioksi:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Lähetä täydellinen PR**: Varmista, että kaikki osion käännetyt tiedostot ovat yhdessä PR:ssä. Emme hyväksy osittaisia käännöksiä osioissa. Kun lähetät käännös-PR:n, varmista, että käännöskansio sisältää käännökset kaikista alkuperäisen kansion tiedostoista.

### Writing Guidelines

Johdonmukaisuuden varmistamiseksi kaikissa dokumenteissa, käytä seuraavia ohjeita:

- **URL-muotoilu**: Laita kaikki URL-osoitteet hakasulkeisiin ja sulkuihin ilman ylimääräisiä välilyöntejä niiden ympärillä tai sisällä. Esimerkiksi: `[example](https://www.microsoft.com)`.

- **Suhteelliset linkit**: Käytä `./` suhteellisissa linkeissä, jotka osoittavat nykyisen hakemiston tiedostoihin tai kansioihin, ja `../`, kun linkki osoittaa ylempään hakemistoon. Esimerkiksi: `[example](../../path/to/file)` tai `[example](../../../path/to/file)`.

- **Ei maakohtaisia paikallisia asetuksia**: Varmista, etteivät linkkisi sisällä maakohtaisia paikallisia asetuksia. Esimerkiksi vältä `/en-us/` tai `/en/`.

- **Kuvien säilytys**: Tallenna kaikki kuvat kansioon `./imgs`.

- **Kuvien kuvaavat nimet**: Nimeä kuvat kuvaavasti käyttäen englanninkielisiä merkkejä, numeroita ja viivoja. Esimerkiksi: `example-image.jpg`.

## GitHub Workflows

Kun lähetät pull requestin, seuraavat työnkulut käynnistyvät tarkistamaan muutokset. Noudata alla olevia ohjeita, jotta PR läpäisee työnkulkujen tarkistukset:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Tämä työnkulku varmistaa, että kaikki suhteelliset polut tiedostoissasi ovat oikein.

1. Varmistaaksesi, että linkkisi toimivat oikein, tee seuraavat toimet VS Codessa:
    - Vie hiiri minkä tahansa linkin päälle tiedostoissasi.
    - Paina **Ctrl + Click** siirtyäksesi linkin kohteeseen.
    - Jos linkki ei toimi paikallisesti, työnkulku käynnistyy eikä linkki toimi GitHubissa.

1. Korjataksesi ongelman, tee seuraavat toimet VS Coden ehdottamien polkujen avulla:
    - Kirjoita `./` tai `../`.
    - VS Code ehdottaa sinulle vaihtoehtoja kirjoittamasi perusteella.
    - Seuraa polkua klikkaamalla haluamaasi tiedostoa tai kansiota varmistaaksesi, että polku on oikea.

Kun olet lisännyt oikean suhteellisen polun, tallenna ja työnnä muutokset.

### Check URLs Don't Have Locale

Tämä työnkulku varmistaa, ettei mikään verkkourli sisällä maakohtaista paikallista asetusta. Koska tämä repositorio on maailmanlaajuisesti saatavilla, on tärkeää varmistaa, ettei URL-osoitteissa ole oman maan paikallista asetusta.

1. Tarkista, että URL-osoitteissasi ei ole maakohtaisia paikallisia asetuksia tekemällä seuraavat toimet:

    - Etsi tekstiä kuten `/en-us/`, `/en/` tai muita kielikohtaisia asetuksia URL-osoitteista.
    - Jos näitä ei ole URL-osoitteissasi, tarkistus menee läpi.

1. Korjataksesi ongelman, tee seuraavat toimet:
    - Avaa työnkulun korostama tiedostopolku.
    - Poista URL-osoitteista maakohtainen paikallinen asetus.

Kun olet poistanut paikallisen asetuksen, tallenna ja työnnä muutokset.

### Check Broken Urls

Tämä työnkulku varmistaa, että kaikki verkkourlit tiedostoissasi toimivat ja palauttavat 200-tilakoodin.

1. Tarkista, että URL-osoitteesi toimivat oikein tekemällä seuraavat toimet:
    - Tarkista URL-osoitteiden tila tiedostoissasi.

2. Korjataksesi rikkoutuneet URL-osoitteet, tee seuraavat toimet:
    - Avaa tiedosto, jossa rikkinäinen URL on.
    - Päivitä URL oikeaan osoitteeseen.

Kun olet korjannut URL-osoitteet, tallenna ja työnnä muutokset.

> [!NOTE]
>
> On tilanteita, joissa URL-tarkistus epäonnistuu, vaikka linkki olisi saavutettavissa. Tämä voi johtua useista syistä, kuten:
>
> - **Verkkorajoitukset:** GitHubin toimintapalvelimilla voi olla verkkorajoituksia, jotka estävät pääsyn tiettyihin URL-osoitteisiin.
> - **Aikakatkaisuepäonnistumiset:** URL-osoitteet, jotka vastaavat liian hitaasti, voivat aiheuttaa aikakatkaisun työnkulussa.
> - **Väliaikaiset palvelinongelmat:** Satunnaiset palvelimen katkokset tai huollot voivat tehdä URL-osoitteen tilapäisesti saavuttamattomaksi tarkistuksen aikana.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai tulkinnoista.