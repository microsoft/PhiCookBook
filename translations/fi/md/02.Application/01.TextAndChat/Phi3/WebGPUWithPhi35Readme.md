<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-09T18:58:30+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "fi"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo WebGPU:n ja RAG-mallin esittelyyn

RAG-malli Phi-3.5 Onnx Hosted -mallin kanssa hyödyntää Retrieval-Augmented Generation -lähestymistapaa, yhdistäen Phi-3.5-mallien tehon ja ONNX-isännöinnin tehokkaisiin tekoälysovelluksiin. Tämä malli on keskeinen domain-spesifisten tehtävien hienosäätöön, tarjoten yhdistelmän laatua, kustannustehokkuutta ja pitkän kontekstin ymmärrystä. Se on osa Azure AI:n valikoimaa, joka tarjoaa laajan mallivalikoiman, jotka on helppo löytää, kokeilla ja käyttää, vastaten eri alojen räätälöintitarpeisiin.

## Mikä on WebGPU  
WebGPU on moderni verkkografiikka-API, joka tarjoaa tehokkaan pääsyn laitteen grafiikkasuorittimeen (GPU) suoraan verkkoselaimesta. Sen on tarkoitus korvata WebGL, tarjoten useita keskeisiä parannuksia:

1. **Yhteensopivuus nykyaikaisten GPU:iden kanssa**: WebGPU on suunniteltu toimimaan saumattomasti nykyaikaisten GPU-arkkitehtuurien kanssa hyödyntäen järjestelmä-API:eja kuten Vulkan, Metal ja Direct3D 12.
2. **Parannettu suorituskyky**: Se tukee yleiskäyttöisiä GPU-laskelmia ja nopeampia operaatioita, mikä tekee siitä sopivan sekä grafiikan renderöintiin että koneoppimistehtäviin.
3. **Edistyneet ominaisuudet**: WebGPU tarjoaa pääsyn monipuolisempiin GPU-ominaisuuksiin, mahdollistaen monimutkaisempia ja dynaamisempia grafiikka- ja laskentatehtäviä.
4. **Vähemmän JavaScript-kuormaa**: Siirtämällä enemmän tehtäviä GPU:lle, WebGPU vähentää merkittävästi JavaScriptin kuormitusta, mikä johtaa parempaan suorituskykyyn ja sujuvampaan käyttökokemukseen.

WebGPU:ta tukevat tällä hetkellä selaimet kuten Google Chrome, ja tukea laajennetaan jatkuvasti muille alustoille.

### 03.WebGPU  
Vaadittu ympäristö:

**Tuetut selaimet:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### WebGPU:n ottaminen käyttöön:

- Chrome/Microsoft Edge -selaimissa

Ota käyttöön `chrome://flags/#enable-unsafe-webgpu` -lipuke.

#### Avaa selain:  
Käynnistä Google Chrome tai Microsoft Edge.

#### Siirry lippusivulle:  
Kirjoita osoiteriville `chrome://flags` ja paina Enter.

#### Etsi lippu:  
Kirjoita sivun yläosassa olevaan hakukenttään 'enable-unsafe-webgpu'.

#### Ota lippu käyttöön:  
Etsi tuloksista #enable-unsafe-webgpu -lippu.

Klikkaa sen vieressä olevaa pudotusvalikkoa ja valitse Enabled.

#### Käynnistä selain uudelleen:  
Lipukkeen käyttöönoton jälkeen selain täytyy käynnistää uudelleen, jotta muutokset astuvat voimaan. Klikkaa sivun alareunassa näkyvää Relaunch-painiketta.

- Linuxissa käynnistä selain käyttäen `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) -versiossa WebGPU on oletuksena käytössä.  
- Firefox Nightlyssä kirjoita osoiteriville about:config ja `set dom.webgpu.enabled to true`.

### GPU:n määrittäminen Microsoft Edgeä varten  

Näin asetat korkean suorituskyvyn GPU:n Microsoft Edgelle Windowsissa:

- **Avaa asetukset:** Klikkaa Käynnistä-valikkoa ja valitse Asetukset.  
- **Järjestelmäasetukset:** Siirry Järjestelmä ja sitten Näyttö.  
- **Grafiikka-asetukset:** Selaa alas ja klikkaa Grafiikka-asetukset.  
- **Valitse sovellus:** Valitse ”Valitse sovellus asetusten määrittämistä varten”, valitse Työpöytäsovellus ja sitten Selaa.  
- **Valitse Edge:** Siirry Edge-asennuskansioon (yleensä `C:\Program Files (x86)\Microsoft\Edge\Application`) ja valitse `msedge.exe`.  
- **Aseta mieltymys:** Klikkaa Asetukset, valitse Korkea suorituskyky ja tallenna.  
Tämä varmistaa, että Microsoft Edge käyttää tehokasta GPU:tasi paremman suorituskyvyn takaamiseksi.  
- **Käynnistä tietokone uudelleen**, jotta asetukset tulevat voimaan.

### Esimerkit: Katso [tämä linkki](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää auktoritatiivisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä aiheutuvista väärinymmärryksistä tai tulkinnoista.