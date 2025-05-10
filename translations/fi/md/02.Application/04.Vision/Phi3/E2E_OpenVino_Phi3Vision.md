<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7d7afa242a4a041ff4193546d4baf16",
  "translation_date": "2025-05-09T20:00:58+00:00",
  "source_file": "md/02.Application/04.Vision/Phi3/E2E_OpenVino_Phi3Vision.md",
  "language_code": "fi"
}
-->
Tämä demo esittelee, miten esikoulutettua mallia käytetään Python-koodin generointiin kuvan ja tekstikehotteen perusteella.

[Sample Code](../../../../../../code/06.E2E/E2E_OpenVino_Phi3-vision.ipynb)

Tässä vaiheittainen selitys:

1. **Tuonnit ja asetukset**:
   - Tarvittavat kirjastot ja moduulit tuodaan, mukaan lukien `requests`, `PIL` kuvankäsittelyyn sekä `transformers` mallin ja prosessoinnin hallintaan.

2. **Kuvan lataaminen ja näyttäminen**:
   - Kuv tiedosto (`demo.png`) avataan `PIL`-kirjastolla ja näytetään.

3. **Kehotteen määrittely**:
   - Luodaan viesti, joka sisältää kuvan ja pyynnön generoida Python-koodi kuvan käsittelyyn ja tallentamiseen `plt` (matplotlib) avulla.

4. **Prosessorin lataaminen**:
   - `AutoProcessor` ladataan esikoulutetusta mallista, joka sijaitsee `out_dir`-hakemistossa. Tämä prosessori käsittelee teksti- ja kuva-inputit.

5. **Kehotteen luominen**:
   - `apply_chat_template`-metodia käytetään muotoilemaan viesti mallille sopivaksi kehotteeksi.

6. **Inputtien prosessointi**:
   - Kehote ja kuva muunnetaan tensoreiksi, joita malli pystyy käsittelemään.

7. **Generointiparametrien asettaminen**:
   - Määritellään mallin generointiprosessin argumentit, kuten maksimimäärä luotavia uusia tokeneita ja otetaanko outputista otos.

8. **Koodin generointi**:
   - Malli generoi Python-koodin inputtien ja generointiparametrien perusteella. `TextStreamer` huolehtii outputista, ohittaen kehotteen ja erikoistokenit.

9. **Tulostus**:
   - Generoitu koodi tulostetaan, ja sen pitäisi sisältää Python-koodi kuvan käsittelyyn ja tallentamiseen kehotteen mukaisesti.

Tämä demo havainnollistaa, miten OpenVinoa hyödyntämällä esikoulutettua mallia voidaan käyttää dynaamiseen koodin generointiin käyttäjän syötteen ja kuvien perusteella.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää auktoritatiivisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaisen ihmiskääntäjän käyttöä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkintojen seurauksista.