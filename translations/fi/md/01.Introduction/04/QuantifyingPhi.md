# **Phi-perheen kvantifiointi**

Mallin kvantifiointi tarkoittaa parametrien (kuten painojen ja aktivaatioarvojen) kuvaamista neuroverkon mallissa suuresta arvovälistä (yleensä jatkuvasta arvovälistä) pienempään äärelliseen arvoväliin. Tämä teknologia voi vähentää mallin kokoa ja laskennallista monimutkaisuutta sekä parantaa mallin toiminnan tehokkuutta resursseiltaan rajatuissa ympäristöissä, kuten mobiililaitteissa tai sulautetuissa järjestelmissä. Mallin kvantifiointi saavuttaa pakkauksen vähentämällä parametrien tarkkuutta, mutta se tuo mukanaan myös tiettyä tarkkuuden menetystä. Siksi kvantifiointiprosessissa on tasapainotettava mallin koko, laskennallinen monimutkaisuus ja tarkkuus. Yleisiä kvantifiointimenetelmiä ovat esimerkiksi kiinteäpistekvantifiointi, liukulukukvantifiointi jne. Voit valita sopivan kvantifiointistrategian käyttötarkoituksen ja tarpeiden mukaan.

Toivomme saavuttavamme GenAI-mallien käyttöönoton reunalaitteissa ja sallivamme useampien laitteiden pääsyn GenAI-skenaarioihin, kuten mobiililaitteet, AI PC/Copilot+PC sekä perinteiset IoT-laitteet. Kvantifiointimallin avulla voimme ottaa sen käyttöön eri reunalaitteissa laitteen mukaan. Yhdistämällä laitteistovalmistajien tarjoamat malliakselerointikehykset ja kvantifiointimallit voimme rakentaa parempia SLM-sovellusskenaarioita.

Kvantifiointiskenaariossa meillä on eri tarkkuuksia (INT4, INT8, FP16, FP32). Seuraavassa on selitys yleisesti käytetyistä kvantifiointitarkkuuksista.

### **INT4**

INT4-kvantifiointi on radikaali kvantifiointimenetelmä, joka kvantifioi mallin painot ja aktivaatiot 4-bittisiksi kokonaisluvuiksi. INT4-kvantifiointi johtaa yleensä suurempaan tarkkuuden menetykseen pienen tiedon esityksen rajan ja alaistarkkuuden takia. INT8-kvantifiointiin verrattuna INT4-kvantifiointi voi kuitenkin edelleen vähentää mallin tallennustarvetta ja laskennallista monimutkaisuutta. On huomattava, että INT4-kvantifiointi on käytännön sovelluksissa melko harvinainen, koska liian alhainen tarkkuus voi aiheuttaa merkittävää heikkenemistä mallin suorituskyvyssä. Lisäksi kaikki laitteistot eivät tue INT4-operaatioita, joten laitteen yhteensopivuus on otettava huomioon kvantifiointimenetelmän valinnassa.

### **INT8**

INT8-kvantifiointi on prosessi, jossa mallin painot ja aktivaatioarvot muunnetaan liukuluvuista 8-bittisiksi kokonaisluvuiksi. Vaikka INT8-kokonaisluvut edustavat pienempää ja vähemmän tarkkaa numeerista aluetta, ne voivat merkittävästi vähentää tallennus- ja laskentavaatimuksia. INT8-kvantifioinnissa mallin painot ja aktivaatiot käyvät läpi kvantifiointiprosessin, joka sisältää skaalaamista ja siirtymää, säilyttääkseen alkuperäisen liukulukuinformaation mahdollisimman hyvin. Päättelyn aikana nämä kvantifioidut arvot dekvantifioidaan takaisin liukuluvuiksi laskentaa varten ja kvantifioidaan sitten takaisin INT8:ksi seuraavaa vaihetta varten. Tämä menetelmä tarjoaa useimmissa sovelluksissa riittävän tarkkuuden samalla kun se ylläpitää korkean laskennallisen tehokkuuden.

### **FP16**

FP16-muoto, eli 16-bittiset liukuluvut (float16), puolittaa muistitilan verrattuna 32-bittisiin liukulukuihin (float32), mikä tuo merkittäviä etuja suurissa syväoppimissovelluksissa. FP16-muoto mahdollistaa suurempien mallien lataamisen tai suuremman datamäärän käsittelyn samojen GPU-muistirajojen puitteissa. Kun nykyaikaiset GPU-laitteistot tukevat FP16-operaatioita, FP16-muodon käyttö voi myös parantaa laskennan nopeutta. FP16-muodolla on kuitenkin omaa heikkoutensa eli alhaisempi tarkkuus, joka voi johtaa numeeriseen epävakauteen tai tarkkuuden menetykseen joissakin tapauksissa.

### **FP32**

FP32-muoto tarjoaa korkeamman tarkkuuden ja voi tarkasti edustaa laajaa arvoaluetta. Monimutkaisten matemaattisten operaatioiden tai korkean tarkkuuden tulosten tarvittaessa FP32 on ensisijainen valinta. Korkea tarkkuus kuitenkin merkitsee enemmän muistinkulutusta ja pidempiä laskenta-aikoja. Suurissa syväoppimismalleissa, erityisesti kun parametreja on paljon ja dataa on valtavasti, FP32-muoto voi aiheuttaa riittämättömän GPU-muistin tai pienen suoritusnopeuden.

Mobiililaitteissa tai IoT-laitteissa voimme muuntaa Phi-3.x-mallit INT4-muotoon, kun taas AI PC / Copilot PC -laitteet voivat hyödyntää korkeampia tarkkuuksia kuten INT8, FP16, FP32.

Tällä hetkellä eri laitteistovalmistajilla on erilaiset kehykset generatiivisten mallien tukemiseen, kuten Intelin OpenVINO, Qualcommin QNN, Applen MLX ja Nvidian CUDA, joita yhdistetään mallin kvantifiointiin paikallista käyttöönottoa varten.

Teknologian kannalta meillä on kvantifioinnin jälkeen erilaisia muototukea, kuten PyTorch/TensorFlow-muoto, GGUF ja ONNX. Olen tehnyt vertailun GGUF:n ja ONNX:n muodoista ja käyttöskenaarioista. Tässä suosittelen ONNX-kvantifiointimuotoa, joka saa hyvän tuen mallikehystä ja laitteistoa myöten. Tässä luvussa keskitymme ONNX Runtimeen GenAI:lle, OpenVINOon ja Apple MLX:ään mallin kvantifioinnissa (jos sinulla on parempi menetelmä, voit toimittaa sen meille PR:n kautta).

**Tämä luku sisältää**

1. [Quantizing Phi-3.5 / 4 using llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizing Phi-3.5 / 4 using Generative AI extensions for onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizing Phi-3.5 / 4 using Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizing Phi-3.5 / 4 using Apple MLX Framework](./UsingAppleMLXQuantifyingPhi.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ota huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää auktoritatiivisena lähteenä. Kriittisissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->