<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-09T05:19:58+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "fi"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo WebGPU:n ja RAG-mallin esittelyyn  
RAG-malli Phi-3 Onnx -isännöidyllä mallilla hyödyntää Retrieval-Augmented Generation -lähestymistapaa, yhdistäen Phi-3-mallien voiman ONNX-isännöintiin tehokkaissa tekoälyn käyttöönotossa. Tämä malli on keskeinen domain-spesifisten tehtävien hienosäätöön, tarjoten yhdistelmän laatua, kustannustehokkuutta ja pitkän kontekstin ymmärrystä. Se on osa Azure AI:n valikoimaa, joka tarjoaa laajan valikoiman helposti löydettäviä, kokeiltavia ja käytettäviä malleja, vastaten eri alojen räätälöintitarpeisiin. Phi-3-mallit, mukaan lukien Phi-3-mini, Phi-3-small ja Phi-3-medium, löytyvät Azure AI Model Catalogista ja niitä voi hienosäätää ja ottaa käyttöön itsehallinnoidusti tai alustoilla kuten HuggingFace ja ONNX, mikä korostaa Microsoftin sitoutumista saavutettaviin ja tehokkaisiin tekoälyratkaisuihin.

## Mikä on WebGPU  
WebGPU on moderni verkkografiikka-API, joka on suunniteltu tarjoamaan tehokas pääsy laitteen grafiikkasuorittimeen (GPU) suoraan verkkoselaimista. Sen on tarkoitus olla WebGL:n seuraaja, tarjoten useita keskeisiä parannuksia:

1. **Yhteensopivuus nykyaikaisten GPU:iden kanssa**: WebGPU on rakennettu toimimaan saumattomasti nykyaikaisten GPU-arkkitehtuurien kanssa hyödyntäen järjestelmä-API:ita kuten Vulkan, Metal ja Direct3D 12.
2. **Parannettu suorituskyky**: Se tukee yleiskäyttöisiä GPU-laskentatehtäviä ja nopeampia operaatioita, tehden siitä sopivan sekä grafiikan renderöintiin että koneoppimistehtäviin.
3. **Edistyneet ominaisuudet**: WebGPU tarjoaa pääsyn kehittyneempiin GPU-ominaisuuksiin, mahdollistaen monimutkaisempia ja dynaamisempia grafiikka- ja laskentatehtäviä.
4. **JavaScript-kuorman vähentäminen**: Siirtämällä enemmän tehtäviä GPU:lle WebGPU vähentää merkittävästi JavaScriptin kuormitusta, mikä parantaa suorituskykyä ja sujuvampaa käyttökokemusta.

WebGPU:tä tukevat tällä hetkellä selaimet kuten Google Chrome, ja tuen laajentaminen muille alustoille on työn alla.

### 03.WebGPU  
Vaadittu ympäristö:

**Tuetut selaimet:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### WebGPU:n käyttöönotto:

- Chrome/Microsoft Edge -selaimissa  

Ota käyttöön `chrome://flags/#enable-unsafe-webgpu` -lipuke.

#### Avaa selain:  
Käynnistä Google Chrome tai Microsoft Edge.

#### Siirry lipukkeiden sivulle:  
Kirjoita osoiteriville `chrome://flags` ja paina Enter.

#### Etsi lipuke:  
Kirjoita sivun yläreunan hakukenttään 'enable-unsafe-webgpu'.

#### Ota lipuke käyttöön:  
Löydä #enable-unsafe-webgpu lipuke hakutuloksista.

Klikkaa sen vieressä olevaa alasvetovalikkoa ja valitse Enabled.

#### Käynnistä selain uudelleen:  
Lipukkeen aktivoimisen jälkeen selain täytyy käynnistää uudelleen, jotta muutokset tulevat voimaan. Klikkaa sivun alareunassa näkyvää Relaunch-painiketta.

- Linuxissa käynnistä selain käyttämällä komentoa `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) -versiossa WebGPU on oletuksena käytössä.  
- Firefox Nightlyssä kirjoita osoiteriville about:config ja ota käyttöön `set dom.webgpu.enabled to true`.

### GPU:n asetukset Microsoft Edge -selaimelle  

Näin asetat korkean suorituskyvyn GPU:n Microsoft Edge -selaimelle Windowsissa:

- **Avaa Asetukset:** Klikkaa Käynnistä-valikkoa ja valitse Asetukset.  
- **Järjestelmäasetukset:** Mene Järjestelmä-kohtaan ja sieltä Näyttö.  
- **Grafiikka-asetukset:** Selaa alas ja klikkaa Grafiikka-asetukset.  
- **Valitse sovellus:** “Valitse sovellus, jolle asetetaan asetukset” -kohdassa valitse Työpöytäsovellus ja klikkaa Selaa.  
- **Valitse Edge:** Siirry Edge-asennuskansioon (yleensä `C:\Program Files (x86)\Microsoft\Edge\Application`) ja valitse `msedge.exe`.  
- **Aseta asetukset:** Klikkaa Asetukset, valitse Korkean suorituskyvyn vaihtoehto ja klikkaa Tallenna.  
Näin varmistat, että Microsoft Edge käyttää tehokasta GPU:ta paremman suorituskyvyn saavuttamiseksi.  
- **Käynnistä** tietokone uudelleen, jotta asetukset tulevat voimaan.

### Avaa Codespace:  
Siirry GitHub-repositorioon.  
Klikkaa Code-painiketta ja valitse Open with Codespaces.

Jos sinulla ei vielä ole Codespacea, voit luoda uuden klikkaamalla New codespace.

**Huom:** Node-ympäristön asentaminen Codespaceen  
Npm-demon suorittaminen GitHub Codespacessa on erinomainen tapa testata ja kehittää projektiasi. Tässä vaiheittainen ohje alkuun pääsemiseksi:

### Ympäristön valmistelu:  
Kun Codespace on auki, varmista, että Node.js ja npm ovat asennettuina. Tarkista tämä suorittamalla:  
```
node -v
```  
```
npm -v
```

Jos niitä ei ole asennettu, voit asentaa ne komennolla:  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Siirry projektihakemistoon:  
Käytä terminaalia siirtyäksesi hakemistoon, jossa npm-projektisi sijaitsee:  
```
cd path/to/your/project
```

### Asenna riippuvuudet:  
Suorita seuraava komento asentaaksesi kaikki package.json-tiedostossa luetellut riippuvuudet:  

```
npm install
```

### Suorita demo:  
Kun riippuvuudet on asennettu, voit käynnistää demo-skriptisi. Se on yleensä määritelty package.json-tiedoston scripts-osiossa. Esimerkiksi, jos demo-skripti on nimeltään start, suorita:  

```
npm run build
```  
```
npm run dev
```

### Käytä demo:  
Jos demosi sisältää web-palvelimen, Codespaces tarjoaa URL-osoitteen sen käyttämiseen. Tarkista ilmoitukset tai Ports-välilehti löytääksesi URL-osoitteen.

**Huom:** Malli täytyy välimuistittaa selaimessa, joten lataaminen saattaa kestää hetken.

### RAG-demo  
Lataa markdown-tiedosto `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Valitse tiedostosi:  
Klikkaa “Choose File” -painiketta valitaksesi ladattavan dokumentin.

### Lataa dokumentti:  
Kun tiedosto on valittu, klikkaa “Upload” ladataksesi dokumentin RAG:ia (Retrieval-Augmented Generation) varten.

### Aloita keskustelu:  
Kun dokumentti on ladattu, voit aloittaa keskustelun RAG:n avulla dokumentin sisällön pohjalta.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ole hyvä ja huomioi, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää auktoritatiivisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai virhetulkinnoista.