<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "62b2632720dd39ef391d6b60b9b4bfb8",
  "translation_date": "2025-05-09T05:38:38+00:00",
  "source_file": "code/09.UpdateSamples/Aug/vscode/phiext/vsc-extension-quickstart.md",
  "language_code": "fi"
}
-->
# Tervetuloa VS Code -laajennukseesi

## Mitä kansiossa on

* Tämä kansio sisältää kaikki laajennuksesi tarvitsemat tiedostot.
* `package.json` - tämä on manifestitiedosto, jossa määrittelet laajennuksesi ja komennon.
  * Esimerkkilaajennus rekisteröi komennon ja määrittelee sen otsikon sekä komennon nimen. Näiden tietojen avulla VS Code voi näyttää komennon komentopalettissa. Laajennusta ei vielä tarvitse ladata.
* `src/extension.ts` - tämä on pääasiallinen tiedosto, jossa toteutat komennon toiminnallisuuden.
  * Tiedosto vie yhden funktion, `activate`, jota kutsutaan ensimmäisellä kerralla, kun laajennus aktivoidaan (tässä tapauksessa komennon suorittamisen yhteydessä). `activate`-funktion sisällä kutsumme `registerCommand`.
  * Annamme komennon toteutuksen sisältävän funktion toisena parametrina `registerCommand`:lle.

## Asennus

* Asenna suositellut laajennukset (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner ja dbaeumer.vscode-eslint)

## Pääset heti alkuun

* Paina `F5` avataksesi uuden ikkunan, jossa laajennuksesi on ladattu.
* Suorita komento komentopaletista painamalla (`Ctrl+Shift+P` tai Macilla `Cmd+Shift+P`) ja kirjoittamalla `Hello World`.
* Aseta taukopisteitä koodiisi tiedostossa `src/extension.ts` laajennuksen virheenkorjaukseen.
* Löydät laajennuksesi tulosteet debug-konsolista.

## Tee muutoksia

* Voit käynnistää laajennuksen uudelleen debug-työkalupalkista muuttaessasi koodia tiedostossa `src/extension.ts`.
* Voit myös ladata VS Code -ikkunan uudelleen (`Ctrl+R` tai Macilla `Cmd+R`) laajennuksesi kanssa, jotta muutokset tulevat voimaan.

## Tutustu API:in

* Voit avata koko API:n avaamalla tiedoston `node_modules/@types/vscode/index.d.ts`.

## Suorita testit

* Asenna [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* Suorita "watch"-tehtävä komennolla **Tasks: Run Task**. Varmista, että se on käynnissä, muuten testejä ei välttämättä löydetä.
* Avaa Testing-näkymä aktiviteettipalkista ja napsauta "Run Test" -painiketta tai käytä pikanäppäintä `Ctrl/Cmd + ; A`.
* Näet testitulokset Test Results -näkymässä.
* Tee muutoksia tiedostoon `src/test/extension.test.ts` tai luo uusia testitiedostoja `test`-kansioon.
  * Tarjottu testiajo ottaa huomioon vain tiedostot, joiden nimi vastaa kaavaa `**.test.ts`.
  * Voit luoda kansioita `test`-kansioon järjestelläksesi testejä haluamallasi tavalla.

## Mene pidemmälle

* Pienennä laajennuksen kokoa ja paranna käynnistysaikaa [paketoimalla laajennus](https://code.visualstudio.com/api/working-with-extensions/bundling-extension).
* [Julkaise laajennuksesi](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) VS Code -laajennusmarkkinapaikalla.
* Automatisoi käännökset ottamalla käyttöön [jatkuva integraatio](https://code.visualstudio.com/api/working-with-extensions/continuous-integration).

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ole hyvä ja huomioi, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää auktoritatiivisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaisen ihmiskääntäjän käyttöä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.