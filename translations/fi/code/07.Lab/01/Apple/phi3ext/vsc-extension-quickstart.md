<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:08:42+00:00",
  "source_file": "code/07.Lab/01/Apple/phi3ext/vsc-extension-quickstart.md",
  "language_code": "fi"
}
-->
# Tervetuloa VS Code -laajennukseesi

## Mitä kansiossa on

* Tämä kansio sisältää kaikki laajennukseesi tarvittavat tiedostot.
* `package.json` - tämä on manifestitiedosto, jossa määrittelet laajennuksesi ja komennon.
  * Esimerkkilaajennus rekisteröi komennon ja määrittelee sen otsikon sekä komennon nimen. Näiden tietojen avulla VS Code voi näyttää komennon komentopalettissa. Laajennusta ei kuitenkaan tarvitse vielä ladata.
* `src/extension.ts` - tämä on pääasiallinen tiedosto, jossa toteutat komennon toiminnallisuuden.
  * Tiedosto vie yhden funktion, `activate`, joka kutsutaan ensimmäisellä kerralla, kun laajennuksesi aktivoidaan (tässä tapauksessa komennon suorittamisen yhteydessä). `activate`-funktion sisällä kutsumme `registerCommand`.
  * Toisena parametrina `registerCommand`-funktiolle annamme funktion, joka sisältää komennon toteutuksen.

## Asennus

* Asenna suositellut laajennukset (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner ja dbaeumer.vscode-eslint)

## Pääset nopeasti alkuun

* Paina `F5` avataksesi uuden ikkunan, jossa laajennuksesi on ladattu.
* Suorita komento komentopaletista painamalla (`Ctrl+Shift+P` tai Macilla `Cmd+Shift+P`) ja kirjoittamalla `Hello World`.
* Aseta taukopaikkoja koodissasi tiedostossa `src/extension.ts` laajennuksen virheenkorjausta varten.
* Löydät laajennuksesi tulosteet virheenkorjauskonsolista.

## Tee muutoksia

* Voit käynnistää laajennuksen uudelleen virheenkorjaustyökaluriviltä muokatessasi koodia tiedostossa `src/extension.ts`.
* Voit myös ladata (`Ctrl+R` tai Macilla `Cmd+R`) VS Code -ikkunan uudelleen laajennuksesi muutosten aktivoimiseksi.

## Tutustu API:in

* Voit avata koko API:n avaamalla tiedoston `node_modules/@types/vscode/index.d.ts`.

## Suorita testit

* Asenna [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Suorita "watch"-tehtävä komennolla **Tasks: Run Task**. Varmista, että tämä on käynnissä, muuten testejä ei välttämättä löydetä.
* Avaa Testing-näkymä toiminta-palkista ja napsauta "Run Test" -painiketta tai käytä pikanäppäintä `Ctrl/Cmd + ; A`.
* Näet testitulosten tulosteet Test Results -näkymässä.
* Tee muutoksia tiedostoon `src/test/extension.test.ts` tai luo uusia testitiedostoja `test`-kansioon.
  * Testaaja huomioi vain tiedostot, joiden nimet vastaavat kaavaa `**.test.ts`.
  * Voit luoda kansioita `test`-kansion sisälle järjestelläksesi testejä haluamallasi tavalla.

## Mene pidemmälle

* Pienennä laajennuksen kokoa ja nopeuta käynnistysaikaa [paketoimalla laajennuksesi](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Julkaise laajennuksesi](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) VS Code -laajennusmarkkinapaikassa.
* Automatisoi buildit ottamalla käyttöön [jatkuva integrointi](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa mahdollisista väärinymmärryksistä tai tulkinnoista, jotka johtuvat tämän käännöksen käytöstä.