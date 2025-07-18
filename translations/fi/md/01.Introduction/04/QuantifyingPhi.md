<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-07-16T21:47:50+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "fi"
}
-->
# **Phi-perheen kvantifiointi**

Mallin kvantifiointi tarkoittaa prosessia, jossa neuroverkkopohjaisen mallin parametrit (kuten painot ja aktivaatioarvot) muunnetaan laajasta arvoalueesta (yleensä jatkuvasta arvoalueesta) pienempään, rajalliseen arvoalueeseen. Tämä teknologia voi pienentää mallin kokoa ja laskennallista monimutkaisuutta sekä parantaa mallin suorituskykyä resurssirajoitteisissa ympäristöissä, kuten mobiililaitteissa tai sulautetuissa järjestelmissä. Mallin kvantifiointi saavuttaa pakkaamisen vähentämällä parametrien tarkkuutta, mutta se tuo mukanaan myös tietyn tarkkuuden menetyksen. Siksi kvantifiointiprosessissa on tasapainotettava mallin koko, laskennallinen monimutkaisuus ja tarkkuus. Yleisiä kvantifiointimenetelmiä ovat muun muassa kiinteäpistekvantifiointi ja liukulukukvantifiointi. Voit valita sopivan kvantifiointistrategian tilanteen ja tarpeiden mukaan.

Toivomme voivamme ottaa GenAI-mallit käyttöön reunalaitteissa ja mahdollistaa useampien laitteiden pääsy GenAI-skenaarioihin, kuten mobiililaitteisiin, AI PC/Copilot+PC:hin ja perinteisiin IoT-laitteisiin. Kvantifioidun mallin avulla voimme ottaa sen käyttöön eri reunalaitteissa laitteesta riippuen. Yhdistämällä laitteistovalmistajien tarjoamat mallin kiihdytys- ja kvantifiointikehykset voimme rakentaa parempia SLM-sovellusskenaarioita.

Kvantifiointiskenaariossa käytämme eri tarkkuuksia (INT4, INT8, FP16, FP32). Seuraavassa on selitys yleisesti käytetyistä kvantifiointitarkkuuksista.

### **INT4**

INT4-kvantifiointi on radikaali kvantifiointimenetelmä, jossa mallin painot ja aktivaatioarvot kvantifioidaan 4-bittisiksi kokonaisluvuiksi. INT4-kvantifiointi aiheuttaa yleensä suuremman tarkkuuden menetyksen pienemmän esitysalueen ja alhaisemman tarkkuuden vuoksi. Verrattuna INT8-kvantifiointiin INT4 voi kuitenkin edelleen vähentää mallin tallennustarvetta ja laskennallista monimutkaisuutta. On syytä huomioida, että INT4-kvantifiointi on käytännössä melko harvinaista, koska liian alhainen tarkkuus voi heikentää mallin suorituskykyä merkittävästi. Lisäksi kaikki laitteistot eivät tue INT4-operaatioita, joten laitteistoyhteensopivuus on otettava huomioon kvantifiointimenetelmää valittaessa.

### **INT8**

INT8-kvantifiointi tarkoittaa mallin painojen ja aktivaatioiden muuntamista liukuluvuista 8-bittisiksi kokonaisluvuiksi. Vaikka INT8-kokonaislukujen esitysalue on pienempi ja vähemmän tarkka, se voi merkittävästi vähentää tallennus- ja laskentavaatimuksia. INT8-kvantifioinnissa mallin painot ja aktivaatioarvot käyvät läpi kvantifiointiprosessin, joka sisältää skaalaamisen ja siirron, jotta alkuperäinen liukulukutieto säilyy mahdollisimman hyvin. Päättelyvaiheessa nämä kvantifioidut arvot muunnetaan takaisin liukuluvuiksi laskentaa varten ja sen jälkeen uudelleen INT8-muotoon seuraavaa vaihetta varten. Tämä menetelmä tarjoaa useimmissa sovelluksissa riittävän tarkkuuden säilyttäen samalla korkean laskentatehokkuuden.

### **FP16**

FP16-muoto, eli 16-bittiset liukuluvut (float16), puolittaa muistinkäytön verrattuna 32-bittisiin liukulukuihin (float32), mikä on merkittävä etu suurissa syväoppimissovelluksissa. FP16-muoto mahdollistaa suurempien mallien lataamisen tai suuremman datamäärän käsittelyn samalla GPU-muistirajoituksella. Koska nykyaikaiset GPU-laitteistot tukevat yhä enemmän FP16-operaatioita, FP16-muodon käyttö voi myös nopeuttaa laskentaa. FP16-muodolla on kuitenkin myös omat haittansa, kuten alhaisempi tarkkuus, mikä voi joissain tapauksissa johtaa numeeriseen epävakauteen tai tarkkuuden menetykseen.

### **FP32**

FP32-muoto tarjoaa korkeamman tarkkuuden ja pystyy tarkasti esittämään laajan arvovalikoiman. Monimutkaisia matemaattisia operaatioita suoritettaessa tai kun tarvitaan erittäin tarkkoja tuloksia, FP32-muoto on suositeltava. Korkea tarkkuus tarkoittaa kuitenkin myös suurempaa muistinkulutusta ja pidempiä laskenta-aikoja. Suurissa syväoppimismalleissa, erityisesti kun malliparametreja ja datamäärä on paljon, FP32-muoto voi aiheuttaa GPU-muistin riittämättömyyttä tai hidastaa päättelyä.

Mobiililaitteissa tai IoT-laitteissa voimme muuntaa Phi-3.x -mallit INT4-muotoon, kun taas AI PC / Copilot PC voi käyttää korkeampaa tarkkuutta, kuten INT8, FP16 tai FP32.

Tällä hetkellä eri laitteistovalmistajilla on erilaisia kehyksiä generatiivisten mallien tukemiseen, kuten Intelin OpenVINO, Qualcommin QNN, Applen MLX ja Nvidian CUDA, joita yhdistetään mallin kvantifiointiin paikallisen käyttöönoton toteuttamiseksi.

Teknologian osalta meillä on kvantifioinnin jälkeen tuki eri formaateille, kuten PyTorch / Tensorflow, GGUF ja ONNX. Olen tehnyt vertailun GGUF:n ja ONNX:n formaattien välillä sekä niiden sovellusskenaarioista. Tässä suosittelen ONNX-kvantifiointiformaattia, joka saa hyvän tuen mallikehyksiltä aina laitteistoon asti. Tässä luvussa keskitymme ONNX Runtimeen GenAI:lle, OpenVINOon ja Apple MLX:ään mallin kvantifioinnissa (jos sinulla on parempi tapa, voit myös lähettää meille PR:n).

**Tässä luvussa käsitellään**

1. [Phi-3.5 / 4 kvantifiointi käyttäen llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Phi-3.5 / 4 kvantifiointi käyttäen Generative AI -laajennuksia onnxruntimeen](./UsingORTGenAIQuantifyingPhi.md)

3. [Phi-3.5 / 4 kvantifiointi käyttäen Intel OpenVINOa](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Phi-3.5 / 4 kvantifiointi käyttäen Apple MLX -kehystä](./UsingAppleMLXQuantifyingPhi.md)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.