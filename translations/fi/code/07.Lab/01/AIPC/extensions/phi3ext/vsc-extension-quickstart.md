<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "eae2c0ea18160a3e7a63ace7b53897d7",
  "translation_date": "2025-05-09T04:57:04+00:00",
  "source_file": "code/07.Lab/01/AIPC/extensions/phi3ext/vsc-extension-quickstart.md",
  "language_code": "fi"
}
-->
# Tervetuloa VS Code -laajennukseesi

## Mitä kansiossa on

* Tämä kansio sisältää kaikki laajennuksesi tarvitsemat tiedostot.
* `package.json` - tämä on manifestitiedosto, jossa määrittelet laajennuksesi ja komennon.
  * Esimerkkilaajennus rekisteröi komennon ja määrittelee sen otsikon sekä komennon nimen. Näiden tietojen avulla VS Code voi näyttää komennon komentopalettissa. Laajennusta ei vielä tarvitse ladata.
* `src/extension.ts` - tämä on pääasiallinen tiedosto, jossa toteutat komennon toiminnallisuuden.
  * Tiedosto vie ulos yhden funktion, `activate`, joka kutsutaan ensimmäisellä kerralla, kun laajennus aktivoituu (tässä tapauksessa komennon suorittamisen yhteydessä). `activate`-funktion sisällä kutsumme `registerCommand`.
  * Toimitamme komennon toteutuksen sisältävän funktion toisena parametrina `registerCommand`-funktiolle.

## Asennus

* asenna suositellut laajennukset (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner ja dbaeumer.vscode-eslint)


## Pääset alkuun heti

* Paina `F5` avataksesi uuden ikkunan, jossa laajennuksesi on ladattu.
* Suorita komento komentopaletista painamalla (`Ctrl+Shift+P` tai Macillä `Cmd+Shift+P`) ja kirjoittamalla `Hello World`.
* Aseta taukopisteitä koodiisi tiedostossa `src/extension.ts` laajennuksen virheenkorjausta varten.
* Löydät laajennuksen tulosteen virheenkorjauskonsolista.

## Tee muutoksia

* Voit käynnistää laajennuksen uudelleen virheenkorjaustyökaluriviltä muutettuasi koodia tiedostossa `src/extension.ts`.
* Voit myös ladata uudelleen (`Ctrl+R` tai Macillä `Cmd+R`) VS Code -ikkunan laajennuksesi kanssa, jotta muutokset tulevat voimaan.


## Tutustu APIin

* Voit avata koko API-kokoelman avaamalla tiedoston `node_modules/@types/vscode/index.d.ts`.

## Suorita testit

* Asenna [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Suorita "watch"-tehtävä komennolla **Tasks: Run Task**. Varmista, että se on käynnissä, muuten testejä ei välttämättä löydetä.
* Avaa Testausnäkymä aktiviteettipalkista ja napsauta "Run Test" -painiketta tai käytä pikanäppäintä `Ctrl/Cmd + ; A`.
* Näet testitulokset Test Results -näkymässä.
* Tee muutoksia tiedostoon `src/test/extension.test.ts` tai luo uusia testitiedostoja kansioon `test`.
  * Toimitettu testiajuri käsittelee vain tiedostoja, joiden nimi vastaa kaavaa `**.test.ts`.
  * Voit luoda alikansioita kansioon `test` järjestelläksesi testejäsi haluamallasi tavalla.

## Mene pidemmälle

* Pienennä laajennuksen kokoa ja nopeuta käynnistysaikaa [paketoimalla laajennuksesi](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo).
* [Julkaise laajennuksesi](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) VS Code -laajennusmarkkinapaikalla.
* Automatisoi käännökset asettamalla [jatkuva integraatio](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo).

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja omalla kielellään on pidettävä virallisena lähteenä. Tärkeissä asioissa suositellaan ammattilaisen tekemää ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.