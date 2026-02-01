Phi-3-mini WebGPU RAG Chatbot

## Demo WebGPU:n ja RAG-mallin esittelyyn
RAG-malli Phi-3 Onnx -isännöidyllä mallilla hyödyntää Retrieval-Augmented Generation -lähestymistapaa, yhdistäen Phi-3-mallien voiman ONNX-isännöintiin tehokkaita tekoälysovelluksia varten. Tämä malli on keskeinen domain-spesifisten tehtävien hienosäädössä, tarjoten yhdistelmän laatua, kustannustehokkuutta ja pitkän kontekstin ymmärrystä. Se on osa Azure AI:n valikoimaa, joka tarjoaa laajan mallivalikoiman, joita on helppo löytää, kokeilla ja käyttää, vastaten eri toimialojen räätälöintitarpeisiin. Phi-3-mallit, mukaan lukien Phi-3-mini, Phi-3-small ja Phi-3-medium, ovat saatavilla Azure AI Model Catalogissa ja niitä voi hienosäätää ja ottaa käyttöön itsehallinnoidusti tai alustoilla kuten HuggingFace ja ONNX, mikä osoittaa Microsoftin sitoutumisen saavutettaviin ja tehokkaisiin tekoälyratkaisuihin.

## Mikä on WebGPU
WebGPU on moderni verkkografiikka-API, joka on suunniteltu tarjoamaan tehokas pääsy laitteen grafiikkasuorittimeen (GPU) suoraan verkkoselaimista. Sen on tarkoitus olla WebGL:n seuraaja, tarjoten useita keskeisiä parannuksia:

1. **Yhteensopivuus nykyaikaisten GPU:iden kanssa**: WebGPU on rakennettu toimimaan saumattomasti nykyaikaisten GPU-arkkitehtuurien kanssa hyödyntäen järjestelmä-API:ita kuten Vulkan, Metal ja Direct3D 12.
2. **Parannettu suorituskyky**: Se tukee yleiskäyttöisiä GPU-laskelmia ja nopeampia operaatioita, tehden siitä sopivan sekä grafiikan renderöintiin että koneoppimistehtäviin.
3. **Edistyneet ominaisuudet**: WebGPU tarjoaa pääsyn kehittyneempiin GPU-ominaisuuksiin, mahdollistaen monimutkaisempia ja dynaamisempia grafiikka- ja laskentatehtäviä.
4. **Vähentynyt JavaScript-kuormitus**: Siirtämällä enemmän tehtäviä GPU:lle, WebGPU vähentää merkittävästi JavaScriptin kuormitusta, mikä johtaa parempaan suorituskykyyn ja sujuvampaan käyttökokemukseen.

WebGPU:tä tukevat tällä hetkellä selaimet kuten Google Chrome, ja tukea laajennetaan jatkuvasti muille alustoille.

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

Näin asetat korkean suorituskyvyn GPU:n Microsoft Edge -selaimelle Windowsissa:

- **Avaa Asetukset:** Klikkaa Käynnistä-valikkoa ja valitse Asetukset.
- **Järjestelmäasetukset:** Mene kohtaan Järjestelmä ja sitten Näyttö.
- **Grafiikka-asetukset:** Selaa alas ja klikkaa Grafiikka-asetukset.
- **Valitse sovellus:** Valitse "Valitse sovellus asetuksen määrittämiseksi", valitse Työpöytäsovellus ja klikkaa Selaa.
- **Valitse Edge:** Siirry Edge-asennuskansioon (yleensä `C:\Program Files (x86)\Microsoft\Edge\Application`) ja valitse `msedge.exe`.
- **Aseta mieltymys:** Klikkaa Asetukset, valitse Korkea suorituskyky ja tallenna.
Näin varmistat, että Microsoft Edge käyttää tehokasta GPU:tasi paremman suorituskyvyn saavuttamiseksi.  
- **Käynnistä tietokone uudelleen**, jotta asetukset tulevat voimaan.

### Avaa Codespace:
Siirry GitHub-repositorioon.
Klikkaa Code-painiketta ja valitse Open with Codespaces.

Jos sinulla ei vielä ole Codespacea, voit luoda uuden klikkaamalla New codespace.

**Huom:** Node-ympäristön asentaminen Codespaceen  
npm-demon suorittaminen GitHub Codespacesta on erinomainen tapa testata ja kehittää projektiasi. Tässä vaiheittainen ohje aloittamiseen:

### Ympäristön valmistelu:
Kun Codespace on auki, varmista, että Node.js ja npm ovat asennettuina. Tarkista tämä suorittamalla:
```
node -v
```  
```
npm -v
```

Jos ne eivät ole asennettuina, voit asentaa ne komennolla:
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
Suorita seuraava komento asentaaksesi kaikki package.json -tiedostossa listatut riippuvuudet:

```
npm install
```

### Suorita demo:
Kun riippuvuudet on asennettu, voit käynnistää demosi. Tämä on yleensä määritelty package.jsonin scripts-osiossa. Esimerkiksi, jos demosi skripti on nimeltään start, suorita:

```
npm run build
```  
```
npm run dev
```

### Pääsy demoon:
Jos demosi käyttää web-palvelinta, Codespaces tarjoaa URL-osoitteen sen käyttämiseen. Etsi ilmoitus tai tarkista Ports-välilehti löytääksesi URL:n.

**Huom:** Malli täytyy välimuistittaa selaimessa, joten lataus voi kestää hetken.

### RAG Demo
Lataa markdown-tiedosto `intro_rag.md` viimeistelläksesi RAG-ratkaisun. Codespacesia käytettäessä tiedoston voi ladata sijainnista `01.InferencePhi3/docs/`

### Valitse tiedostosi:
Klikkaa “Choose File” -painiketta valitaksesi ladattavan dokumentin.

### Lataa dokumentti:
Valittuasi tiedoston, klikkaa “Upload” ladataksesi dokumentin RAG:ia (Retrieval-Augmented Generation) varten.

### Aloita keskustelu:
Kun dokumentti on ladattu, voit aloittaa keskustelun RAG:in avulla dokumentin sisällön pohjalta.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.