# Tervetuloa VS Code -laajennukseesi

## Mitä kansiossa on

* Tämä kansio sisältää kaikki laajennuksesi tarvitsemat tiedostot.
* `package.json` - tämä on manifestitiedosto, jossa määrittelet laajennuksesi ja komennon.
  * Esimerkkilaajennus rekisteröi komennon ja määrittelee sen otsikon sekä komennon nimen. Näiden tietojen avulla VS Code voi näyttää komennon komentopalettissa. Laajennusta ei vielä tarvitse ladata.
* `src/extension.ts` - tämä on pääasiallinen tiedosto, jossa toteutat komennon toiminnallisuuden.
  * Tiedosto vie yhden funktion, `activate`, joka kutsutaan ensimmäisellä kerralla, kun laajennus aktivoidaan (tässä tapauksessa komennon suorittamisen yhteydessä). `activate`-funktion sisällä kutsumme `registerCommand`-funktiota.
  * Toisena parametrina `registerCommand`-funktiolle annamme funktion, joka sisältää komennon toteutuksen.

## Asennus

* Asenna suositellut laajennukset (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner ja dbaeumer.vscode-eslint)

## Käynnistä heti

* Paina `F5` avataksesi uuden ikkunan, jossa laajennuksesi on ladattu.
* Suorita komento komentopalettista painamalla (`Ctrl+Shift+P` tai Macilla `Cmd+Shift+P`) ja kirjoittamalla `Hello World`.
* Aseta taukopisteitä koodiin tiedostossa `src/extension.ts` laajennuksen virheenkorjausta varten.
* Löydät laajennuksesi tulosteen virheenkorjauskonsolista.

## Tee muutoksia

* Voit käynnistää laajennuksen uudelleen virheenkorjaustyökaluriviltä sen jälkeen, kun olet muuttanut koodia tiedostossa `src/extension.ts`.
* Voit myös ladata VS Code -ikkunan uudelleen (`Ctrl+R` tai Macilla `Cmd+R`), jolloin laajennuksesi muutokset tulevat voimaan.

## Tutustu API:in

* Voit avata koko API-kokoelman avaamalla tiedoston `node_modules/@types/vscode/index.d.ts`.

## Suorita testit

* Asenna [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Suorita "watch"-tehtävä komennolla **Tasks: Run Task**. Varmista, että tämä on käynnissä, muuten testejä ei välttämättä löydy.
* Avaa Testing-näkymä toimintopalkista ja klikkaa "Run Test" -painiketta tai käytä pikanäppäintä `Ctrl/Cmd + ; A`
* Näet testitulokset Test Results -näkymässä.
* Tee muutoksia tiedostoon `src/test/extension.test.ts` tai luo uusia testitiedostoja `test`-kansioon.
  * Tarjottu testiajo suorittaa vain tiedostot, joiden nimi vastaa kaavaa `**.test.ts`.
  * Voit luoda kansioita `test`-kansioon järjestelläksesi testejä haluamallasi tavalla.

## Mene pidemmälle

* Pienennä laajennuksen kokoa ja paranna käynnistysaikaa [paketoimalla laajennuksesi](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Julkaise laajennuksesi](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) VS Code -laajennusmarkkinapaikassa.
* Automatisoi käännökset asettamalla [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.