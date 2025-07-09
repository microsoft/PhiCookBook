<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-09T18:31:25+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "fi"
}
-->
# Osallistuminen

Tämä projekti toivottaa tervetulleiksi panokset ja ehdotukset. Useimmat panokset edellyttävät, että hyväksyt Contributor License Agreementin (CLA), jossa vahvistat, että sinulla on oikeus ja että myönnät meille oikeudet käyttää panostasi. Lisätietoja löytyy osoitteesta [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Kun lähetät pull requestin, CLA-botti tarkistaa automaattisesti, tarvitsetko CLA:n ja merkitsee PR:n asianmukaisesti (esim. tilantarkistus, kommentti). Noudata vain botin antamia ohjeita. Tämä riittää tekemään vain kerran kaikissa CLA:ta käyttävissä repositorioissa.

## Käyttäytymissäännöt

Tämä projekti on ottanut käyttöön [Microsoft Open Source Code of Conductin](https://opensource.microsoft.com/codeofconduct/). Lisätietoja löydät [Code of Conduct FAQ:sta](https://opensource.microsoft.com/codeofconduct/faq/) tai ota yhteyttä osoitteeseen [opencode@microsoft.com](mailto:opencode@microsoft.com) jos sinulla on lisäkysymyksiä tai kommentteja.

## Varotoimet issueiden luomisessa

Älä avaa GitHub-issueita yleisiin tukikysymyksiin, sillä GitHub-listaa tulisi käyttää ominaisuuspyyntöihin ja bugiraportteihin. Näin voimme helpommin seurata todellisia ongelmia tai bugeja koodissa ja pitää yleisen keskustelun erillään varsinaisesta koodista.

## Kuinka osallistua

### Pull requestien ohjeet

Kun lähetät pull requestin (PR) Phi-3 CookBook -repositorioosi, noudata seuraavia ohjeita:

- **Forkkaa repositorio**: Forkkaa aina repositorio omaan tiliisi ennen kuin teet muutoksia.

- **Eri pull requestit (PR)**:
  - Lähetä jokainen muutostyyppi omassa pull requestissaan. Esimerkiksi bugikorjaukset ja dokumentaatiopäivitykset tulisi lähettää erillisinä PR:inä.
  - Kirjoitusvirheiden korjaukset ja pienet dokumentaatiopäivitykset voidaan yhdistää yhdeksi PR:ksi, kun se on tarkoituksenmukaista.

- **Ratkaise yhdistämiskonfliktit**: Jos pull requestissasi on yhdistämiskonflikteja, päivitä paikallinen `main`-haara vastaamaan päärepositoriota ennen muutosten tekemistä.

- **Käännösten lähettäminen**: Kun lähetät käännöspull requestin, varmista, että käännöskansio sisältää käännökset kaikista alkuperäisen kansion tiedostoista.

### Kirjoitusohjeet

Johdonmukaisuuden varmistamiseksi kaikissa dokumenteissa, käytä seuraavia ohjeita:

- **URL-muotoilu**: Laita kaikki URL-osoitteet hakasulkeisiin ja sulkuihin ilman ylimääräisiä välilyöntejä niiden ympärillä tai sisällä. Esimerkiksi: `[example](https://www.microsoft.com)`.

- **Suhteelliset linkit**: Käytä `./` suhteellisissa linkeissä, jotka osoittavat nykyisen kansion tiedostoihin tai kansioihin, ja `../` ylemmän tason kansioon. Esimerkiksi: `[example](../../path/to/file)` tai `[example](../../../path/to/file)`.

- **Ei maakohtaisia paikallisasetuksia**: Varmista, ettei linkeissäsi ole maakohtaisia paikallisasetuksia. Esimerkiksi vältä `/en-us/` tai `/en/`.

- **Kuvien tallennus**: Tallenna kaikki kuvat `./imgs`-kansioon.

- **Kuvien kuvaavat nimet**: Nimeä kuvat kuvaavasti käyttäen englanninkielisiä merkkejä, numeroita ja väliviivoja. Esimerkiksi: `example-image.jpg`.

## GitHub-työnkulut

Kun lähetät pull requestin, seuraavat työnkulut käynnistyvät muutosten tarkistamiseksi. Noudata alla olevia ohjeita varmistaaksesi, että pull requestisi läpäisee työnkulun tarkistukset:

- [Tarkista rikkinäiset suhteelliset polut](../..)
- [Tarkista, ettei URL-osoitteissa ole paikallisasetusta](../..)

### Tarkista rikkinäiset suhteelliset polut

Tämä työnkulku varmistaa, että kaikki suhteelliset polut tiedostoissasi ovat oikein.

1. Varmistaaksesi, että linkkisi toimivat oikein, tee seuraavat toimet VS Codella:
    - Vie hiiri minkä tahansa linkin päälle tiedostoissasi.
    - Paina **Ctrl + Klikkaus** siirtyäksesi linkkiin.
    - Jos linkki ei toimi paikallisesti, työnkulku käynnistyy eikä linkki toimi GitHubissa.

1. Korjataksesi tämän ongelman, tee seuraavat toimet VS Coden tarjoamien polkuvinkkien avulla:
    - Kirjoita `./` tai `../`.
    - VS Code ehdottaa vaihtoehtoja kirjoittamasi perusteella.
    - Seuraa polkua klikkaamalla haluamaasi tiedostoa tai kansiota varmistaaksesi, että polku on oikea.

Kun olet lisännyt oikean suhteellisen polun, tallenna ja työnnä muutokset.

### Tarkista, ettei URL-osoitteissa ole paikallisasetusta

Tämä työnkulku varmistaa, ettei mikään verkkourli sisällä maakohtaista paikallisasetusta. Koska tämä repositorio on maailmanlaajuisesti saatavilla, on tärkeää varmistaa, ettei URL-osoitteissa ole oman maasi paikallisasetusta.

1. Tarkista, ettei URL-osoitteissasi ole maakohtaisia paikallisasetuksia tekemällä seuraavat toimet:

    - Etsi tekstiä kuten `/en-us/`, `/en/` tai muita kielikohtaisia paikallisasetuksia URL-osoitteista.
    - Jos näitä ei ole URL-osoitteissasi, tarkistus menee läpi.

1. Korjataksesi tämän ongelman, tee seuraavat toimet:
    - Avaa työnkulun korostama tiedostopolku.
    - Poista maakohtainen paikallisasetus URL-osoitteista.

Kun olet poistanut paikallisasetuksen, tallenna ja työnnä muutokset.

### Tarkista rikkinäiset URL-osoitteet

Tämä työnkulku varmistaa, että kaikki verkkourlit tiedostoissasi toimivat ja palauttavat 200-tilakoodin.

1. Tarkista, että URL-osoitteesi toimivat oikein tekemällä seuraavat toimet:
    - Tarkista URL-osoitteiden tila tiedostoissasi.

2. Korjataksesi rikkinäiset URL-osoitteet, tee seuraavat toimet:
    - Avaa tiedosto, joka sisältää rikkinäisen URL-osoitteen.
    - Päivitä URL oikeaksi.

Kun olet korjannut URL-osoitteet, tallenna ja työnnä muutokset.

> [!NOTE]
>
> On tilanteita, joissa URL-tarkistus epäonnistuu, vaikka linkki olisi saavutettavissa. Tämä voi johtua useista syistä, kuten:
>
> - **Verkkorajoitukset:** GitHubin toimintapalvelimilla voi olla verkkorajoituksia, jotka estävät pääsyn tiettyihin URL-osoitteisiin.
> - **Aikakatkaisuongelmat:** URL-osoitteet, jotka vastaavat hitaasti, voivat aiheuttaa aikakatkaisun työnkulussa.
> - **Väliaikaiset palvelinongelmat:** Satunnaiset palvelinkatkokset tai huollot voivat tehdä URL-osoitteen tilapäisesti saavuttamattomaksi tarkistuksen aikana.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.