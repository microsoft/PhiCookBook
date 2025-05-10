<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d658062de70b131ef4c0bff69b5fc70e",
  "translation_date": "2025-05-09T13:30:14+00:00",
  "source_file": "md/01.Introduction/04/QuantifyingPhi.md",
  "language_code": "fi"
}
-->
# **Phi-perheen kvantifiointi**

Mallin kvantifiointi tarkoittaa prosessia, jossa neuroverkkopohjaisen mallin parametrit (kuten painot ja aktivaatioarvot) muunnetaan suuresta arvoalueesta (yleensä jatkuvasta arvoalueesta) pienempään, rajalliseen arvoalueeseen. Tämä tekniikka voi pienentää mallin kokoa ja laskennallista monimutkaisuutta sekä parantaa mallin toimintatehokkuutta resurssirajoitteisissa ympäristöissä, kuten mobiililaitteissa tai sulautetuissa järjestelmissä. Mallin kvantifiointi saavuttaa pakkaamisen vähentämällä parametrien tarkkuutta, mutta se aiheuttaa myös jonkin verran tarkkuuden menetystä. Siksi kvantifiointiprosessissa on tärkeää tasapainottaa mallin koko, laskennallinen monimutkaisuus ja tarkkuus. Yleisiä kvantifiointimenetelmiä ovat muun muassa kiinteäpistekvantifiointi ja liukulukukvantifiointi. Voit valita tilanteeseen ja tarpeisiin sopivan kvantifiointistrategian.

Toivomme voivamme ottaa GenAI-mallit käyttöön reunalaitteissa ja mahdollistaa useammille laitteille pääsy GenAI-skenaarioihin, kuten mobiililaitteille, AI PC/Copilot+PC:lle ja perinteisille IoT-laitteille. Kvantifioidun mallin avulla voimme ottaa sen käyttöön eri reunalaitteissa laitekohtaisesti. Yhdistettynä laitteistovalmistajien tarjoamiin mallin kiihdytys- ja kvantifiointikehyksiin voimme rakentaa parempia SLM-sovellusskenaarioita.

Kvantifiointiskenaariossa meillä on erilaisia tarkkuuksia (INT4, INT8, FP16, FP32). Seuraavassa selitetään yleisimmin käytetyt kvantifiointitarkkuudet.

### **INT4**

INT4-kvantifiointi on radikaali kvantifiointimenetelmä, jossa mallin painot ja aktivaatioarvot muunnetaan 4-bittisiksi kokonaisluvuiksi. INT4-kvantifiointi aiheuttaa yleensä suuremman tarkkuuden menetyksen pienemmän esitysalueen ja alhaisemman tarkkuuden vuoksi. Verrattuna INT8-kvantifiointiin INT4 voi kuitenkin edelleen vähentää mallin tallennustarvetta ja laskennallista monimutkaisuutta. On syytä huomata, että INT4-kvantifiointi on käytännössä melko harvinaista, koska liian alhainen tarkkuus voi heikentää mallin suorituskykyä merkittävästi. Lisäksi kaikki laitteistot eivät tue INT4-operaatioita, joten laitteistoyhteensopivuus on otettava huomioon kvantifiointimenetelmää valittaessa.

### **INT8**

INT8-kvantifiointi tarkoittaa mallin painojen ja aktivaatioiden muuntamista liukuluvuista 8-bittisiksi kokonaisluvuiksi. Vaikka INT8-kokonaisluvut edustavat pienempää ja vähemmän tarkkaa arvoaluetta, ne voivat merkittävästi vähentää tallennus- ja laskentavaatimuksia. INT8-kvantifioinnissa mallin painot ja aktivaatioarvot käyvät läpi kvantifiointiprosessin, johon sisältyy skaalaus ja siirto, jotta alkuperäinen liukulukutieto säilyy mahdollisimman hyvin. Päättelyvaiheessa nämä kvantifioidut arvot muunnetaan takaisin liukuluvuiksi laskentaa varten ja kvantifioidaan uudelleen INT8-muotoon seuraavaa vaihetta varten. Tämä menetelmä tarjoaa useimmissa sovelluksissa riittävän tarkkuuden säilyttäen samalla korkean laskentatehokkuuden.

### **FP16**

FP16-muoto, eli 16-bittiset liukuluvut (float16), vähentää muistinkäyttöä puoleen verrattuna 32-bittisiin liukulukuihin (float32), mikä on merkittävä etu suurissa syväoppimissovelluksissa. FP16-muoto mahdollistaa suurempien mallien lataamisen tai suuremman datamäärän käsittelyn samalla GPU-muistin rajoituksella. Koska nykyaikaiset GPU-laitteistot tukevat yhä enemmän FP16-operaatioita, FP16-muodon käyttö voi myös parantaa laskentanopeutta. FP16:lla on kuitenkin myös omat rajoituksensa, kuten alhaisempi tarkkuus, joka voi joissain tapauksissa aiheuttaa numeerista epävakautta tai tarkkuuden menetystä.

### **FP32**

FP32-muoto tarjoaa korkeamman tarkkuuden ja pystyy tarkasti esittämään laajan arvovalikoiman. Monimutkaisia matemaattisia operaatioita suoritettaessa tai korkeaa tarkkuutta vaadittaessa FP32 on suositeltava. Korkea tarkkuus tarkoittaa kuitenkin myös suurempaa muistinkulutusta ja pidempiä laskenta-aikoja. Suurissa syväoppimismalleissa, joissa on paljon parametreja ja valtava määrä dataa, FP32 voi aiheuttaa GPU-muistin riittämättömyyttä tai hidastaa päättelyä.

Mobiililaitteissa tai IoT-laitteissa voimme muuntaa Phi-3.x-mallit INT4-muotoon, kun taas AI PC / Copilot PC voi käyttää korkeampaa tarkkuutta kuten INT8, FP16 tai FP32.

Tällä hetkellä eri laitteistovalmistajilla on erilaisia kehyksiä generatiivisten mallien tukemiseen, kuten Intelin OpenVINO, Qualcommin QNN, Applen MLX ja Nvidian CUDA, joita yhdistetään mallin kvantifiointiin paikallisen käyttöönoton toteuttamiseksi.

Teknologian osalta meillä on kvantifioinnin jälkeen tuki eri formaateille, kuten PyTorch / Tensorflow, GGUF ja ONNX. Olen tehnyt vertailun GGUF:n ja ONNX:n formaattien ja käyttöskenaarioiden välillä. Suosittelen tässä ONNX:n kvantifiointiformaattia, jolla on hyvä tuki mallikehyksistä laitteistoon. Tässä luvussa keskitymme ONNX Runtimeen GenAI:lle, OpenVINOon ja Apple MLX:ään mallin kvantifioinnissa (jos sinulla on parempi tapa, voit myös antaa sen meille lähettämällä PR:n).

**Tämä luku sisältää**

1. [Phi-3.5 / 4 kvantifiointi käyttämällä llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Phi-3.5 / 4 kvantifiointi käyttämällä Generative AI -laajennuksia onnxruntimeen](./UsingORTGenAIQuantifyingPhi.md)

3. [Phi-3.5 / 4 kvantifiointi Intel OpenVINOlla](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Phi-3.5 / 4 kvantifiointi Apple MLX Frameworkilla](./UsingAppleMLXQuantifyingPhi.md)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä tulee katsoa auktoriteettiseksi lähteeksi. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.