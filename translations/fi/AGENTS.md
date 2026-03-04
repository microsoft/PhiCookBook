# AGENTS.md

## Projektin yleiskatsaus

PhiCookBook on kattava keittokirjasto, joka sisältää käytännön esimerkkejä, opetusmateriaaleja ja dokumentaatiota Microsoftin Phi-pienkielimallien (SLM) kanssa työskentelyyn. Kirjasto esittelee erilaisia käyttötapauksia, kuten päättelyä, hienosäätöä, kvantisointia, RAG-toteutuksia ja multimodaalisia sovelluksia eri alustoilla ja kehyksillä.

**Keskeiset teknologiat:**
- **Kielet:** Python, C#/.NET, JavaScript/Node.js
- **Kehykset:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Alustat:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Mallityypit:** Phi-3, Phi-3.5, Phi-4 (teksti, visio, multimodaali, päättelyvariantit)

**Arkiston rakenne:**
- `/code/` - Toimivia koodiesimerkkejä ja näytetoteutuksia
- `/md/` - Yksityiskohtainen dokumentaatio, opetusmateriaalit ja ohjeet  
- `/translations/` - Monikieliset käännökset (yli 50 kieltä automatisoidun työnkulun kautta)
- `/.devcontainer/` - Kehityskontin konfiguraatio (Python 3.12 Ollaman kanssa)

## Kehitysympäristön asennus

### GitHub Codespacesin tai kehityskonttien käyttö (suositeltu)

1. Avaa GitHub Codespacesissa (nopein tapa):
   - Klikkaa README-tiedoston "Open in GitHub Codespaces" -merkkiä
   - Kontti konfiguroituu automaattisesti Python 3.12:lla ja Ollamalla Phi-3:n kanssa

2. Avaa VS Code Dev Containersissa:
   - Käytä README-tiedoston "Open in Dev Containers" -merkkiä
   - Kontti vaatii vähintään 16GB RAM-muistia isäntäkoneelta

### Paikallinen asennus

**Edellytykset:**
- Python 3.12 tai uudempi
- .NET 8.0 SDK (C#-esimerkkejä varten)
- Node.js 18+ ja npm (JavaScript-esimerkkejä varten)
- Suositeltu vähintään 16GB RAM-muistia

**Asennus:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Python-esimerkkejä varten:**
Siirry tiettyihin esimerkkihakemistoihin ja asenna riippuvuudet:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**.NET-esimerkkejä varten:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**JavaScript/Web-esimerkkejä varten:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Arkiston järjestely

### Koodiesimerkit (`/code/`)

- **01.Introduce/** - Perusaloitukset ja ensimmäiset esimerkit
- **03.Finetuning/** ja **04.Finetuning/** - Hienosäätöesimerkit eri menetelmillä
- **03.Inference/** - Päättelyesimerkit eri laitteistoilla (AIPC, MLX)
- **06.E2E/** - Päästä päähän -sovellusesimerkit
- **07.Lab/** - Laboratorio-/kokeelliset toteutukset
- **08.RAG/** - Retrieval-Augmented Generation -esimerkit
- **09.UpdateSamples/** - Viimeisimmät päivitetyt esimerkit

### Dokumentaatio (`/md/`)

- **01.Introduction/** - Johdanto-oppaat, ympäristön asennus, alustaoppaat
- **02.Application/** - Sovellusesimerkit tyypin mukaan (Teksti, Koodi, Visio, Audio jne.)
- **02.QuickStart/** - Pikakäynnistysoppaat Microsoft Foundrylle ja GitHub-malleille
- **03.FineTuning/** - Hienosäätödokumentaatio ja opetusmateriaalit
- **04.HOL/** - Käytännön laboratoriot (sisältää .NET-esimerkkejä)

### Tiedostomuodot

- **Jupyter Notebooks (`.ipynb`)** - Interaktiiviset Python-opetusmateriaalit, merkitty 📓 README:ssa
- **Python Scripts (`.py`)** - Itsenäiset Python-esimerkit
- **C# Projects (`.csproj`, `.sln`)** - .NET-sovellukset ja esimerkit
- **JavaScript (`.js`, `package.json`)** - Web-pohjaiset ja Node.js-esimerkit
- **Markdown (`.md`)** - Dokumentaatio ja oppaat

## Esimerkkien käyttö

### Jupyter Notebooksin suorittaminen

Useimmat esimerkit ovat saatavilla Jupyter-notebookeina:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Python-skriptien suorittaminen

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### .NET-esimerkkien suorittaminen

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Tai rakenna koko ratkaisu:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### JavaScript/Web-esimerkkien suorittaminen

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Testaus

Tämä arkisto sisältää esimerkkikoodia ja opetusmateriaaleja, eikä ole perinteinen ohjelmistoprojekti yksikkötesteillä. Validointi tehdään yleensä seuraavasti:

1. **Esimerkkien suorittaminen** - Jokaisen esimerkin tulisi toimia ilman virheitä
2. **Tulosten tarkistaminen** - Varmista, että mallin vastaukset ovat asianmukaisia
3. **Opetusmateriaalien seuraaminen** - Ohjeiden tulisi toimia dokumentoidusti

**Yleinen validointitapa:**
- Testaa esimerkkien suoritus kohdeympäristössä
- Varmista, että riippuvuudet asentuvat oikein
- Tarkista, että mallit latautuvat onnistuneesti
- Vahvista, että odotettu käyttäytyminen vastaa dokumentaatiota

## Koodityyli ja käytännöt

### Yleiset ohjeet

- Esimerkkien tulee olla selkeitä, hyvin kommentoituja ja opettavaisia
- Noudata kieleen liittyviä käytäntöjä (PEP 8 Pythonille, C#-standardit .NET:lle)
- Pidä esimerkit keskittyneinä tiettyjen Phi-mallien ominaisuuksien esittelyyn
- Sisällytä kommentteja, jotka selittävät keskeiset käsitteet ja mallikohtaiset parametrit

### Dokumentaatiostandardit

**URL-muotoilu:**
- Käytä `[teksti](../../url)` -muotoa ilman ylimääräisiä välilyöntejä
- Suhteelliset linkit: Käytä `./` nykyiselle hakemistolle, `../` ylemmälle
- Älä käytä maakohtaisia kielikoodeja URL-osoitteissa (vältä `/en-us/`, `/en/`)

**Kuvat:**
- Tallenna kaikki kuvat `/imgs/`-hakemistoon
- Käytä kuvailevia nimiä englanninkielisin kirjaimin, numeroin ja viivoilla
- Esimerkki: `phi-3-architecture.png`

**Markdown-tiedostot:**
- Viittaa toimiviin esimerkkeihin `/code/`-hakemistossa
- Pidä dokumentaatio synkronoituna koodimuutosten kanssa
- Käytä 📓-emojia merkitsemään Jupyter-notebook-linkkejä README:ssa

### Tiedostojen järjestely

- Koodiesimerkit `/code/`-hakemistossa järjestetty aiheen/ominaisuuden mukaan
- Dokumentaatio `/md/`-hakemistossa peilaa koodirakennetta, kun mahdollista
- Pidä liittyvät tiedostot (notebookit, skriptit, konfiguraatiot) yhdessä alihakemistoissa

## Pull Request -ohjeet

### Ennen lähettämistä

1. **Forkkaa arkisto** omaan tiliisi
2. **Erota PR:t tyypin mukaan:**
   - Virhekorjaukset yhteen PR:ään
   - Dokumentaatiopäivitykset toiseen
   - Uudet esimerkit erillisiin PR:iin
   - Typokorjaukset voidaan yhdistää

3. **Käsittele yhdistämiskonfliktit:**
   - Päivitä paikallinen `main`-haara ennen muutosten tekemistä
   - Synkronoi upstreamin kanssa usein

4. **Käännös-PR:t:**
   - Sisältää käännökset KAIKILLE tiedostoille kansiossa
   - Säilytä alkuperäisen kielen rakenne

### Vaaditut tarkistukset

PR:t suorittavat automaattisesti GitHub-työnkulkuja, jotka validoivat:

1. **Suhteellisten polkujen validointi** - Kaikkien sisäisten linkkien tulee toimia
   - Testaa linkit paikallisesti: Ctrl+Klikkaa VS Codessa
   - Käytä VS Coden polkuehdotuksia (`./` tai `../`)

2. **URL-kielikoodien tarkistus** - Web-URL-osoitteissa ei saa olla kielikoodeja
   - Poista `/en-us/`, `/en/` tai muut kielikoodit
   - Käytä yleisiä kansainvälisiä URL-osoitteita

3. **Rikkoutuneiden URL-osoitteiden tarkistus** - Kaikkien URL-osoitteiden tulee palauttaa 200-tila
   - Varmista, että linkit ovat saavutettavissa ennen lähettämistä
   - Huom: Jotkut virheet voivat johtua verkkorajoituksista

### PR-otsikon muoto

```
[component] Brief description
```

Esimerkkejä:
- `[docs] Lisää Phi-4-päättelyopas`
- `[code] Korjaa ONNX Runtime -integraatioesimerkki`
- `[translation] Lisää japaninkielinen käännös johdanto-oppaista`

## Yleiset kehityskäytännöt

### Työskentely Phi-mallien kanssa

**Mallin lataaminen:**
- Esimerkit käyttävät erilaisia kehyksiä: Transformers, ONNX Runtime, MLX, OpenVINO
- Mallit ladataan yleensä Hugging Facesta, Azuresta tai GitHub-malleista
- Tarkista mallin yhteensopivuus laitteistosi kanssa (CPU, GPU, NPU)

**Päättelymallit:**
- Tekstintuotanto: Useimmat esimerkit käyttävät chat/instruct-variantteja
- Visio: Phi-3-vision ja Phi-4-multimodaali kuvien ymmärtämiseen
- Audio: Phi-4-multimodaali tukee äänisyötteitä
- Päättely: Phi-4-reasoning-variantit edistyneisiin päättelytehtäviin

### Alustakohtaiset huomiot

**Microsoft Foundry:**
- Vaatii Azure-tilauksen ja API-avaimet
- Katso `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Ilmainen taso testaukseen
- Katso `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Paikallinen päättely:**
- ONNX Runtime: Monialustainen, optimoitu päättely
- Ollama: Helppo paikallinen mallien hallinta (esikonfiguroitu kehityskontissa)
- Apple MLX: Optimoitu Apple Siliconille

## Vianmääritys

### Yleiset ongelmat

**Muistiongelmat:**
- Phi-mallit vaativat paljon RAM-muistia (erityisesti visio/multimodaali-variantit)
- Käytä kvantisoituja malleja resurssirajoitteisissa ympäristöissä
- Katso `/md/01.Introduction/04/QuantifyingPhi.md`

**Riippuvuuskonfliktit:**
- Python-esimerkeillä voi olla erityisiä versiorajoituksia
- Käytä virtuaaliympäristöjä jokaiselle esimerkille
- Tarkista yksittäiset `requirements.txt`-tiedostot

**Mallin latausvirheet:**
- Suuret mallit voivat aikakatkaista hitailla yhteyksillä
- Harkitse pilviympäristöjen käyttöä (Codespaces, Azure)
- Tarkista Hugging Face -välimuisti: `~/.cache/huggingface/`

**.NET-projektien ongelmat:**
- Varmista, että .NET 8.0 SDK on asennettu
- Käytä `dotnet restore` ennen rakentamista
- Jotkut projektit sisältävät CUDA-spesifisiä konfiguraatioita (Debug_Cuda)

**JavaScript/Web-esimerkit:**
- Käytä Node.js 18+ yhteensopivuuden varmistamiseksi
- Tyhjennä `node_modules` ja asenna uudelleen, jos ongelmia ilmenee
- Tarkista selaimen konsoli WebGPU-yhteensopivuusongelmien varalta

### Apua saatavilla

- **Discord:** Liity Microsoft Foundry Community Discordiin
- **GitHub Issues:** Ilmoita virheistä ja ongelmista arkistossa
- **GitHub Discussions:** Esitä kysymyksiä ja jaa tietoa

## Lisätietoa

### Vastuullinen tekoäly

Kaiken Phi-mallien käytön tulee noudattaa Microsoftin vastuullisen tekoälyn periaatteita:
- Oikeudenmukaisuus, luotettavuus, turvallisuus
- Yksityisyys ja turvallisuus  
- Osallistavuus, läpinäkyvyys, vastuullisuus
- Käytä Azure AI Content Safetyä tuotantosovelluksissa
- Katso `/md/01.Introduction/01/01.AISafety.md`

### Käännökset

- Yli 50 kieltä tuettuna automatisoidun GitHub Actionin kautta
- Käännökset `/translations/`-hakemistossa
- Ylläpidetään co-op-translator-työnkululla
- Älä muokkaa käännettyjä tiedostoja manuaalisesti (automaattisesti luotu)

### Osallistuminen

- Noudata `CONTRIBUTING.md`-ohjeita
- Hyväksy Contributor License Agreement (CLA)
- Noudata Microsoft Open Source Code of Conductia
- Älä sisällytä tietoturvaan liittyviä tietoja tai tunnuksia committeihin

### Monikielinen tuki

Tämä on monikielinen arkisto, joka sisältää esimerkkejä seuraavilla kielillä:
- **Python** - ML/AI-työnkulut, Jupyter-notebookit, hienosäätö
- **C#/.NET** - Yrityssovellukset, ONNX Runtime -integraatio
- **JavaScript** - Web-pohjainen tekoäly, selaimen päättely WebGPU:lla

Valitse kieli, joka parhaiten sopii käyttötarkoitukseesi ja käyttöympäristöösi.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.