# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo WebGPU:n ja RAG-mallin esittelyyn

RAG-malli Phi-3.5 Onnx -isännöidyllä mallilla hyödyntää Retrieval-Augmented Generation -lähestymistapaa, yhdistäen Phi-3.5-mallien tehon ONNX-isännöintiin tehokkaita tekoälysovelluksia varten. Tämä malli on keskeinen domain-spesifisten tehtävien hienosäädössä, tarjoten yhdistelmän laatua, kustannustehokkuutta ja pitkän kontekstin ymmärrystä. Se on osa Azure AI:n valikoimaa, joka tarjoaa laajan mallivalikoiman, joita on helppo löytää, kokeilla ja käyttää, vastaten eri toimialojen räätälöintitarpeisiin.

## Mikä on WebGPU  
WebGPU on moderni web-grafiikka-API, joka tarjoaa tehokkaan pääsyn laitteen grafiikkasuorittimeen (GPU) suoraan verkkoselaimista. Se on tarkoitettu WebGL:n seuraajaksi ja tarjoaa useita keskeisiä parannuksia:

1. **Yhteensopivuus nykyaikaisten GPU:iden kanssa**: WebGPU on rakennettu toimimaan saumattomasti nykyaikaisten GPU-arkkitehtuurien kanssa hyödyntäen järjestelmärajapintoja kuten Vulkan, Metal ja Direct3D 12.
2. **Parannettu suorituskyky**: Se tukee yleiskäyttöisiä GPU-laskentoja ja nopeampia operaatioita, tehden siitä sopivan sekä grafiikan renderöintiin että koneoppimistehtäviin.
3. **Edistyneet ominaisuudet**: WebGPU tarjoaa pääsyn kehittyneempiin GPU-ominaisuuksiin, mahdollistaen monimutkaisempia ja dynaamisempia grafiikka- ja laskentatehtäviä.
4. **Vähemmän JavaScript-kuormitusta**: Siirtämällä enemmän tehtäviä GPU:lle, WebGPU vähentää merkittävästi JavaScriptin kuormitusta, mikä parantaa suorituskykyä ja sujuvuutta.

WebGPU on tällä hetkellä tuettuna selaimissa kuten Google Chrome, ja tukea laajennetaan jatkuvasti muille alustoille.

### 03.WebGPU  
Vaadittu ympäristö:

**Tuetut selaimet:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### WebGPU:n käyttöönotto:

- Chrome/Microsoft Edge -selaimissa

Ota käyttöön `chrome://flags/#enable-unsafe-webgpu` -lippu.

#### Avaa selain:  
Käynnistä Google Chrome tai Microsoft Edge.

#### Siirry lippujen sivulle:  
Kirjoita osoiteriville `chrome://flags` ja paina Enter.

#### Etsi lippu:  
Kirjoita sivun yläosan hakukenttään 'enable-unsafe-webgpu'

#### Ota lippu käyttöön:  
Etsi #enable-unsafe-webgpu -lippu tuloslistasta.

Klikkaa sen vieressä olevaa alasvetovalikkoa ja valitse Enabled.

#### Käynnistä selain uudelleen:  

Liputuksen jälkeen selain täytyy käynnistää uudelleen, jotta muutokset tulevat voimaan. Klikkaa sivun alareunassa näkyvää Relaunch-painiketta.

- Linuxissa käynnistä selain komennolla `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) tukee WebGPU:ta oletuksena.  
- Firefox Nightlyssä kirjoita osoiteriville about:config ja aseta `dom.webgpu.enabled` arvoksi true.

### GPU:n asetukset Microsoft Edge -selaimelle  

Näin asetat korkean suorituskyvyn GPU:n Microsoft Edgelle Windowsissa:

- **Avaa Asetukset:** Klikkaa Käynnistä-valikkoa ja valitse Asetukset.  
- **Järjestelmäasetukset:** Mene kohtaan Järjestelmä ja sitten Näyttö.  
- **Grafiikka-asetukset:** Selaa alas ja klikkaa Grafiikka-asetukset.  
- **Valitse sovellus:** Valitse "Valitse sovellus asetuksen määrittämiseksi", valitse Työpöytäsovellus ja klikkaa Selaa.  
- **Valitse Edge:** Siirry Edge-asennuskansioon (yleensä `C:\Program Files (x86)\Microsoft\Edge\Application`) ja valitse `msedge.exe`.  
- **Aseta mieltymys:** Klikkaa Asetukset, valitse Korkea suorituskyky ja tallenna.  
Tämä varmistaa, että Microsoft Edge käyttää tehokasta GPU:ta paremman suorituskyvyn saavuttamiseksi.  
- **Käynnistä tietokone uudelleen**, jotta asetukset tulevat voimaan.

### Esimerkit: Katso [tästä linkistä](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.