# AGENTS.md

## Projektin yleiskatsaus

PhiCookBook on kattava reseptikirjavarasto, joka sisältää käytännön esimerkkejä, tutoriaaleja ja dokumentaatiota Microsoftin Phi-pienen kielimalliperheen (SLM) käyttöön. Varasto esittelee erilaisia käyttötapauksia, kuten päättelyä, hienosäätöä, kvantisointia, RAG-toteutuksia ja multimodaalisia sovelluksia eri alustoilla ja kehyksissä.

**Keskeiset teknologiat:**
- **Kielet:** Python, C#/.NET, JavaScript/Node.js
- **Kehykset:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Alustat:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Mallityypit:** Phi-3, Phi-3.5, Phi-4 (teksti-, näkö-, multimodaaliset ja päättelyvariantit)

**Varaston rakenne:**
- `/code/` - Toimivia koodiesimerkkejä ja näytetoteutuksia
- `/md/` - Yksityiskohtainen dokumentaatio, tutoriaalit ja käyttöohjeet  
- `/translations/` - Monikieliset käännökset (yli 50 kieltä automatisoidun työnkulun kautta)
- `/.devcontainer/` - Kehityskonttikonfiguraatio (Python 3.12 Ollaman kanssa)

## Kehitysympäristön asennus

### GitHub Codespacesin tai dev-konttien käyttö (suositeltu)

1. Avaa GitHub Codespacesissa (nopein):
   - Klikkaa README-tiedoston "Open in GitHub Codespaces" -merkkiä
   - Kontti konfiguroituu automaattisesti Python 3.12:lla ja Ollamalla Phi-3:n kanssa

2. Avaa VS Code Dev Containers -ympäristössä:
   - Käytä README-tiedoston "Open in Dev Containers" -merkkiä
   - Kontti vaatii vähintään 16 Gt isäntämuistia

### Paikallinen asennus

**Esivaatimukset:**
- Python 3.12 tai uudempi
- .NET 8.0 SDK (C#-esimerkkeihin)
- Node.js 18+ ja npm (JavaScript-esimerkkeihin)
- Suositus vähintään 16 Gt RAM

**Asennus:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Python-esimerkeille:**
Siirry kunkin esimerkin hakemistoon ja asenna riippuvuudet:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # jos requirements.txt on olemassa
```

**.NET-esimerkeille:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**JavaScript-/Web-esimerkeille:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Käynnistä kehityspalvelin
npm run build  # Rakenna tuotantoon
```

## Varaston järjestys

### Koodiesimerkit (`/code/`)

- **01.Introduce/** - Perusesittelyt ja aloitusesimerkit
- **03.Finetuning/** ja **04.Finetuning/** - Hienosäätöesimerkkejä eri menetelmillä
- **03.Inference/** - Päättelyesimerkkejä eri laitteilla (AIPC, MLX)
- **06.E2E/** - Päätepisteestä päähän sovellusnäytteitä
- **07.Lab/** - Laboratorio- ja kokeelliset toteutukset
- **08.RAG/** - Retrieval-Augmented Generation -näytteitä
- **09.UpdateSamples/** - Viimeisimmät päivitetyt näytteet

### Dokumentaatio (`/md/`)

- **01.Introduction/** - Johdanto-oppaat, ympäristön asennus, alustaoppaat
- **02.Application/** - Sovellusnäytteet tyypin mukaan (Teksti, Koodi, Näkö, Ääni jne.)
- **02.QuickStart/** - Pikakäynnistysoppaat Microsoft Foundrylle ja GitHub Malleille
- **03.FineTuning/** - Hienosäätöön liittyvä dokumentaatio ja tutoriaalit
- **04.HOL/** - Käytännön laboratoriot (sisältää .NET-esimerkkejä)

### Tiedostomuodot

- **Jupyter-muistikirjat (`.ipynb`)** - Interaktiiviset Python-tutoriaalit, merkitty 📓 README-tiedostossa
- **Python-skriptit (`.py`)** - Itsenäiset Python-esimerkit
- **C#-projektit (`.csproj`, `.sln`)** - .NET-sovellukset ja näytteet
- **JavaScript (`.js`, `package.json`)** - Web- ja Node.js-esimerkit
- **Markdown (`.md`)** - Dokumentaatio ja oppaat

## Esimerkkien käyttö

### Jupyter-muistikirjojen ajaminen

Suurin osa esimerkeistä on Jupyter-muistikirjoina:
```bash
pip install jupyter notebook
jupyter notebook  # Avaa selaimen käyttöliittymän
# Siirry haluttuun .ipynb-tiedostoon
```

### Python-skriptien ajaminen

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### .NET-esimerkkien ajaminen

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Tai käännä kokonainen ratkaisu:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### JavaScript/Web-esimerkkien ajaminen

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Kehitys kuuman uudelleenlatauksen kanssa
```

## Testaus

Tämä varasto sisältää esimerkkikoodeja ja tutoriaaleja, ei perinteistä yksikkötestattua ohjelmistoprojektia. Varmennus tehdään tyypillisesti seuraavasti:

1. **Esimerkkien suoritus** - Kunkin esimerkin tulee suorittua ilman virheitä
2. **Tulosten tarkastus** - Tarkista, että mallin vastaukset ovat asianmukaisia
3. **Tutoriaalien seuraaminen** - Opastuksia noudattamalla tulisi toimia kuten dokumentoitu

**Yleinen validointimenetelmä:**
- Testaa esimerkkien suoritus kohdeympäristössä
- Varmista riippuvuuksien asennus onnistuu
- Tarkista, että mallit ladataan oikein
- Vahvista odotettu käyttäytyminen dokumentaation mukaiseksi

## Koodityyli ja käytännöt

### Yleiset ohjeet

- Esimerkkien tulee olla selkeitä, hyvin kommentoituja ja opettavia
- Noudata kielen omia konventioita (PEP 8 Pythonille, C#-standardit .NET:lle)
- Keskity näyttämään Phi-mallien ominaisuudet
- Sisällytä kommentteja keskeisistä käsitteistä ja mallikohtaisista parametreista

### Dokumentaation standardit

**URL-muotoilu:**
- Käytä `[teksti](../../url)`-muotoa ilman ylimääräisiä välilyöntejä
- Relatiiviset linkit: Käytä `./` nykyinen hakemisto, `../` ylempi hakemisto
- Ei maa- tai aluekohtaisia paikallisia koodeja URL:issa (vältä esim. `/en-us/`, `/en/`)

**Kuvat:**
- Säilytä kaikki kuvat `/imgs/`-hakemistossa
- Käytä kuvaavia nimiä, joissa on englanninkielisiä merkkejä, numeroita ja viivoja
- Esim. `phi-3-architecture.png`

**Markdown-tiedostot:**
- Viittaa toimiviin esimerkkeihin `/code/`-hakemistossa
- Pidä dokumentaatio synkronoitu koodimuutosten kanssa
- Merkitse Jupyter-muistikirja-linkit README:ssa 📓-emojilla

### Tiedostojen järjestäminen

- Koodiesimerkit `/code/` järjestetty aiheen/ominaisuuden mukaan
- Dokumentaatio `/md/` peilaa koodirakennetta tarvittaessa
- Pidä liittyvät tiedostot (muistikirjat, skriptit, konfiguraatiot) yhdessä alihakemistoissa

## Pull request -ohjeet

### Ennen lähettämistä

1. **Forkkaa varasto** omaan tiliin
2. **Erota PR:it tyypin mukaan:**
   - Korjaukset yhdessä PR:ssa
   - Dokumentaatiopäivitykset toisessa
   - Uudet esimerkit omissa PR:issaan
   - Kirjoitusvirheiden korjaukset voi yhdistää

3. **Sulautusristiriitojen käsittely:**
   - Päivitä paikallinen `main`-haara ennen muutoksia
   - Synkronoi upstreamin kanssa säännöllisesti

4. **Käännös-PR:t:**
   - Sisällytä käännökset KAIKILLE tiedostoille kyseisessä kansiossa
   - Pidä rakenne yhdenmukaisena alkuperäiskielen kanssa

### Pakolliset tarkistukset

PR:t ajavat automaattisesti GitHub-työnkulkuja varmistaakseen:

1. **Relatiivisten polkujen validointi** - Kaikkien sisäisten linkkien on toimittava
   - Testaa linkit paikallisesti: Ctrl+Klikkaa VS Codessa
   - Käytä VS Coden polkujen ehdotuksia (`./` tai `../`)

2. **URL:n paikallisuus-tarkistus** - Verkkourleissa ei saa olla maan paikalliskoodia
   - Poista `/en-us/`, `/en/` tai muut kielikoodit
   - Käytä yleismaailmallisia URL-osoitteita

3. **Rikkoutuneiden URL:ien tarkistus** - Kaikkien URL:ien on palautettava 200-statustila
   - Varmista linkkien toimivuus ennen lähettämistä
   - Huom: Jotkin virheet voivat johtua verkkorajoituksista

### PR-otsikon muoto

```
[component] Brief description
```

Esimerkkejä:
- `[docs] Lisää Phi-4 päättelytutoriaali`
- `[code] Korjaa ONNX Runtime -integraatio-esimerkki`
- `[translation] Lisää japaninkielinen käännös johdanto-oppaalle`

## Yleisiä kehitysmalleja

### Phi-mallien käyttö

**Mallin lataus:**
- Esimerkeissä käytetään erilaisia kehyksiä: Transformers, ONNX Runtime, MLX, OpenVINO
- Malleja ladataan tyypillisesti Hugging Facesta, Azuren kautta tai GitHub Models -palvelusta
- Tarkista mallin yhteensopivuus laitteesi kanssa (CPU, GPU, NPU)

**Päättelymallit:**
- Tekstin generointi: Useimmissa esimerkeissä chat-/ohjeistusvariantit
- Näkö: Phi-3-vision ja Phi-4-multimodal kuvantunnistukseen
- Ääni: Phi-4-multimodal tukee ääniosioita
- Päättely: Phi-4-reasoning -variantit edistyneeseen päättelyyn

### Alustakohtaiset huomiot

**Microsoft Foundry:**
- Vaatii Azure-tilauksen ja API-avaimet
- Ks. `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Ilmainen taso testaukseen
- Ks. `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Paikallinen päättely:**
- ONNX Runtime: Alustariippumaton ja optimoitu päättely
- Ollama: Helppo paikallinen mallinhallinta (esiasetettu kehityskontissa)
- Apple MLX: Optimoitu Apple Siliconille

## Vianmääritys

### Yleiset ongelmat

**Muistiongelmat:**
- Phi-mallit vaativat merkittävästi RAM-muistia (erityisesti näkö-/multimodaaliset variantit)
- Käytä kvantisoituja malleja resurssirajoitteisissa tilanteissa
- Ks. `/md/01.Introduction/04/QuantifyingPhi.md`

**Riippuvuusristiriidat:**
- Python-esimerkit voivat vaatia tarkkoja versioita
- Käytä virtuaaliympäristöjä kullekin esimerkkikansioille
- Tarkista yksittäiset `requirements.txt` -tiedostot

**Mallin latausvirheet:**
- Suuret mallit voivat aikakatketa hitaisilla yhteyksillä
- Harkitse pilviympäristöjä (Codespaces, Azure)
- Tarkista Hugging Face -välimuisti: `~/.cache/huggingface/`

**.NET-projektien ongelmat:**
- Varmista, että .NET 8.0 SDK on asennettu
- Käytä `dotnet restore` ennen rakentamista
- Joissain projekteissa on CUDA-spesifisiä asetuksia (Debug_Cuda)

**JavaScript/Web-esimerkit:**
- Käytä Node.js 18+:aa yhteensopivuuden takia
- Tyhjennä `node_modules` ja asenna uudelleen, jos ongelmia ilmenee
- Tarkista selaimen konsolista WebGPU-yhteensopivuusvirheet

### Apua saat:

- **Discord:** Liity Microsoft Foundry Community Discordiin
- **GitHub Issues:** Raportoi bugit ja ongelmat
- **GitHub Discussions:** Kysy, jaa tietoa ja keskustele

## Lisätietoa

### Vastuullinen tekoäly

Kaikkien Phi-mallien käytön tulee noudattaa Microsoftin vastuullisen tekoälyn periaatteita:
- Reiluus, luotettavuus, turvallisuus
- Yksityisyys ja tietoturva  
- Osallisuus, läpinäkyvyys, vastuullisuus
- Käytä Azure AI Content Safetya tuotantosovelluksissa
- Ks. `/md/01.Introduction/01/01.AISafety.md`

### Käännökset

- Yli 50 kieltä tuettu automaattisella GitHub Action -prosessilla
- Käännökset `/translations/`-hakemistossa
- Ylläpidetään co-op-translator-työnkululla
- Älä muokkaa käännettyjä tiedostoja manuaalisesti (automaattisesti tuotettu)

### Osallistuminen

- Noudata ohjeita `CONTRIBUTING.md`-tiedostossa
- Hyväksy Contributor License Agreement (CLA)
- Noudata Microsoftin avoimen lähdekoodin käytäntöjä
- Pidä turhat tiedot, kuten salasanat ja avaimet, pois commit-teista

### Monikielinen tuki

Tämä on polyglotti-varasto, jossa esimerkkejä näillä kielillä:
- **Python** - ML/AI-työnkulut, Jupyter-muistikirjat, hienosäätö
- **C#/.NET** - Yrityssovellukset, ONNX Runtime -integraatio
- **JavaScript** - Web-pohjainen tekoäly, selaimen päättely WebGPU:n avulla

Valitse kieli, joka parhaiten sopii käyttötarkoitukseesi ja käyttöönottoympäristöösi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttäen tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen ja päätösvaltainen lähde. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskääntäjän tekemää käännöstä. Emme ole vastuussa mahdollisista väärinymmärryksistä tai tulkintaongelmista, jotka johtuvat tämän käännöksen käytöstä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->