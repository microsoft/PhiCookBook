# AGENTS.md

## Projekti ülevaade

PhiCookBook on põhjalik kokaraamatute hoidla, mis sisaldab praktilisi näiteid, õpetusi ja dokumentatsiooni Microsofti Phi väikeste keelemudelite (SLM) kasutamiseks. Hoidla demonstreerib erinevaid kasutusviise, sealhulgas järeldamist, peenhäälestamist, kvantiseerimist, RAG-i rakendusi ja multimodaalseid rakendusi erinevatel platvormidel ja raamistikus.

**Peamised tehnoloogiad:**
- **Keeled:** Python, C#/.NET, JavaScript/Node.js
- **Raamistikud:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platvormid:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Mudelitüübid:** Phi-3, Phi-3.5, Phi-4 (tekst, visioon, multimodaalsed, põhjendusvariandid)

**Hoidla struktuur:**
- `/code/` - Töötavad koodinäited ja näidisrakendused
- `/md/` - Üksikasjalik dokumentatsioon, õpetused ja juhendid  
- `/translations/` - Mitmekeelsed tõlked (50+ keelt automatiseeritud töövoo kaudu)
- `/.devcontainer/` - Arenduskonteineri konfiguratsioon (Python 3.12 koos Ollama)

## Arenduskeskkonna seadistamine

### GitHub Codespaces'i või arenduskonteinerite kasutamine (soovitatav)

1. Ava GitHub Codespaces'is (kiireim):
   - Klõpsa README-s "Open in GitHub Codespaces" märgisel
   - Konteiner konfigureerib automaatselt Python 3.12 ja Ollama koos Phi-3-ga

2. Ava VS Code arenduskonteinerites:
   - Kasuta README-s "Open in Dev Containers" märgist
   - Konteiner vajab vähemalt 16GB hostmälu

### Kohalik seadistamine

**Eeltingimused:**
- Python 3.12 või uuem
- .NET 8.0 SDK (C# näidete jaoks)
- Node.js 18+ ja npm (JavaScripti näidete jaoks)
- Soovitatav vähemalt 16GB RAM

**Paigaldamine:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Python näidete jaoks:**
Liigu konkreetsete näidiste kataloogidesse ja paigalda sõltuvused:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**.NET näidete jaoks:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**JavaScripti/veebi näidete jaoks:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Hoidla korraldus

### Koodinäited (`/code/`)

- **01.Introduce/** - Põhilised sissejuhatused ja alustamisnäidised
- **03.Finetuning/** ja **04.Finetuning/** - Peenhäälestamise näited erinevate meetoditega
- **03.Inference/** - Järeldamise näited erineval riistvaral (AIPC, MLX)
- **06.E2E/** - Lõpuni viidud rakenduste näited
- **07.Lab/** - Laboratoorsed/eksperimentaalsed rakendused
- **08.RAG/** - Retrieval-Augmented Generation näited
- **09.UpdateSamples/** - Viimati uuendatud näited

### Dokumentatsioon (`/md/`)

- **01.Introduction/** - Sissejuhatusjuhendid, keskkonna seadistamine, platvormijuhendid
- **02.Application/** - Rakenduste näited, mis on organiseeritud tüübi järgi (Tekst, Kood, Visioon, Audio jne)
- **02.QuickStart/** - Kiire alustamise juhendid Microsoft Foundry ja GitHub Models jaoks
- **03.FineTuning/** - Peenhäälestamise dokumentatsioon ja õpetused
- **04.HOL/** - Praktilised laborid (sisaldab .NET näiteid)

### Failiformaadid

- **Jupyter Notebookid (`.ipynb`)** - Interaktiivsed Python õpetused, tähistatud 📓 README-s
- **Python skriptid (`.py`)** - Iseseisvad Python näited
- **C# projektid (`.csproj`, `.sln`)** - .NET rakendused ja näited
- **JavaScript (`.js`, `package.json`)** - Veebipõhised ja Node.js näited
- **Markdown (`.md`)** - Dokumentatsioon ja juhendid

## Näidete kasutamine

### Jupyter Notebookide käivitamine

Enamik näiteid on esitatud Jupyter Notebookidena:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Python skriptide käivitamine

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### .NET näidete käivitamine

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Või kogu lahenduse ehitamine:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### JavaScripti/veebi näidete käivitamine

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Testimine

See hoidla sisaldab näidiskoodi ja õpetusi, mitte traditsioonilist tarkvaraprojekti koos ühikutestidega. Valideerimine toimub tavaliselt järgmiselt:

1. **Näidete käivitamine** - Iga näide peaks töötama ilma vigadeta
2. **Väljundite kontrollimine** - Kontrolli, et mudeli vastused oleksid sobivad
3. **Õpetuste järgimine** - Juhendid peaksid töötama nagu dokumenteeritud

**Tavaline valideerimisviis:**
- Testi näidise käivitamist sihtkeskkonnas
- Kontrolli, et sõltuvused paigaldatakse korrektselt
- Veendu, et mudelid laaditakse edukalt alla ja töötavad
- Kinnita, et oodatav käitumine vastab dokumentatsioonile

## Koodistiil ja konventsioonid

### Üldised juhised

- Näited peaksid olema selged, hästi kommenteeritud ja harivad
- Järgi keelespetsiifilisi konventsioone (PEP 8 Pythonile, C# standardid .NET jaoks)
- Hoia näited keskendunud Phi mudelite konkreetsete võimete demonstreerimisele
- Lisa kommentaare, mis selgitavad olulisi kontseptsioone ja mudelispetsiifilisi parameetreid

### Dokumentatsiooni standardid

**URL-i vormindamine:**
- Kasuta `[tekst](../../url)` vormingut ilma lisaruumideta
- Suhtelised lingid: Kasuta `./` praeguse kataloogi jaoks, `../` vanema jaoks
- Väldi URL-ides riigispetsiifilisi lokaale (väldi `/en-us/`, `/en/`)

**Pildid:**
- Salvesta kõik pildid `/imgs/` kataloogi
- Kasuta kirjeldavaid nimesid ingliskeelsete tähemärkide, numbrite ja sidekriipsudega
- Näide: `phi-3-architecture.png`

**Markdown failid:**
- Viita tegelikele töötavatele näidetele `/code/` kataloogis
- Hoia dokumentatsioon sünkroonis koodimuudatustega
- Kasuta 📓 emotikoni Jupyter Notebooki linkide tähistamiseks README-s

### Failide korraldus

- Koodinäited `/code/` kataloogis organiseeritud teema/funktsiooni järgi
- Dokumentatsioon `/md/` peegeldab koodistruktuuri, kui võimalik
- Hoia seotud failid (notebookid, skriptid, konfiguratsioonid) koos alamkataloogides

## Pull Request'i juhised

### Enne esitamist

1. **Forki hoidla** oma kontole
2. **Eralda PR-id tüübi järgi:**
   - Veaparandused ühes PR-is
   - Dokumentatsiooni uuendused teises
   - Uued näited eraldi PR-is
   - Tippvead võib kombineerida

3. **Lahenda ühendamise konfliktid:**
   - Uuenda oma kohalikku `main` haru enne muudatuste tegemist
   - Sünkroniseeri sageli ülesvooluga

4. **Tõlke PR-id:**
   - Peavad sisaldama tõlkeid KÕIGILE failidele kaustas
   - Säilita originaalkeele struktuur

### Nõutavad kontrollid

PR-id käivitavad automaatselt GitHubi töövood, et valideerida:

1. **Suhtelise tee valideerimine** - Kõik sisemised lingid peavad töötama
   - Testi linke lokaalselt: Ctrl+Click VS Code'is
   - Kasuta VS Code'i tee soovitusi (`./` või `../`)

2. **URL-i lokaali kontroll** - Veebi URL-id ei tohi sisaldada riigikoode
   - Eemalda `/en-us/`, `/en/` või muud keelekoodid
   - Kasuta üldisi rahvusvahelisi URL-e

3. **Katkise URL-i kontroll** - Kõik URL-id peavad tagastama 200 staatuse
   - Veendu, et lingid on enne esitamist ligipääsetavad
   - Märkus: Mõned tõrked võivad olla tingitud võrgu piirangutest

### PR-i pealkirja vorming

```
[component] Brief description
```

Näited:
- `[docs] Lisa Phi-4 järeldamise õpetus`
- `[code] Paranda ONNX Runtime integratsiooni näide`
- `[translation] Lisa jaapani tõlge sissejuhatuse juhenditele`

## Tavalised arendusmustrid

### Phi mudelitega töötamine

**Mudeli laadimine:**
- Näited kasutavad erinevaid raamistikke: Transformers, ONNX Runtime, MLX, OpenVINO
- Mudelid laaditakse tavaliselt Hugging Face'ist, Azure'ist või GitHub Models'ist
- Kontrolli mudeli ühilduvust oma riistvaraga (CPU, GPU, NPU)

**Järeldamise mustrid:**
- Teksti genereerimine: Enamik näiteid kasutab vestlus-/juhendvariante
- Visioon: Phi-3-vision ja Phi-4-multimodaalsed pilditöötluseks
- Audio: Phi-4-multimodaalsed toetavad helisisendeid
- Põhjendus: Phi-4-reasoning variandid keerukate põhjenduste jaoks

### Platvormispetsiifilised märkused

**Microsoft Foundry:**
- Vajab Azure'i tellimust ja API võtmeid
- Vaata `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Tasuta tase testimiseks saadaval
- Vaata `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Kohalik järeldamine:**
- ONNX Runtime: Platvormideülene, optimeeritud järeldamine
- Ollama: Lihtne kohalike mudelite haldamine (eelkonfigureeritud arenduskonteineris)
- Apple MLX: Optimeeritud Apple Siliconi jaoks

## Tõrkeotsing

### Tavalised probleemid

**Mälu probleemid:**
- Phi mudelid vajavad märkimisväärset RAM-i (eriti visiooni/multimodaalsed variandid)
- Kasuta kvantiseeritud mudeleid ressursipiiratud keskkondades
- Vaata `/md/01.Introduction/04/QuantifyingPhi.md`

**Sõltuvuste konfliktid:**
- Python näidetel võivad olla spetsiifilised versiooninõuded
- Kasuta iga näite jaoks virtuaalkeskkondi
- Kontrolli individuaalseid `requirements.txt` faile

**Mudeli allalaadimise tõrked:**
- Suured mudelid võivad aeglaste ühenduste korral aeguda
- Kaalu pilvekeskkondade kasutamist (Codespaces, Azure)
- Kontrolli Hugging Face'i vahemikku: `~/.cache/huggingface/`

**.NET projekti probleemid:**
- Veendu, et .NET 8.0 SDK on paigaldatud
- Kasuta `dotnet restore` enne ehitamist
- Mõned projektid sisaldavad CUDA-spetsiifilisi konfiguratsioone (Debug_Cuda)

**JavaScripti/veebi näited:**
- Kasuta Node.js 18+ ühilduvuse tagamiseks
- Tühjenda `node_modules` ja paigalda uuesti, kui probleemid püsivad
- Kontrolli brauseri konsooli WebGPU ühilduvusprobleemide osas

### Abi saamine

- **Discord:** Liitu Microsoft Foundry Community Discordiga
- **GitHub Issues:** Teata vigadest ja probleemidest hoidlas
- **GitHub Discussions:** Esita küsimusi ja jaga teadmisi

## Täiendav kontekst

### Vastutustundlik AI

Kõik Phi mudelite kasutused peaksid järgima Microsofti vastutustundliku AI põhimõtteid:
- Õiglus, usaldusväärsus, ohutus
- Privaatsus ja turvalisus  
- Kaasatus, läbipaistvus, vastutus
- Kasuta Azure AI Content Safety't tootmisrakenduste jaoks
- Vaata `/md/01.Introduction/01/01.AISafety.md`

### Tõlked

- 50+ keelt toetatud automatiseeritud GitHub Actioni kaudu
- Tõlked `/translations/` kataloogis
- Hallatud co-op-translator töövoo poolt
- Ära muuda käsitsi tõlgitud faile (automaatselt genereeritud)

### Kaastöö

- Järgi juhiseid failis `CONTRIBUTING.md`
- Nõustu kaastöölise litsentsilepinguga (CLA)
- Järgi Microsofti avatud lähtekoodi käitumiskoodeksit
- Hoia turvalisus ja mandaadid commiti välistes failides

### Mitmekeelne tugi

See on polüglotne hoidla, mis sisaldab näiteid:
- **Python** - ML/AI töövood, Jupyter Notebookid, peenhäälestamine
- **C#/.NET** - Ettevõtterakendused, ONNX Runtime integratsioon
- **JavaScript** - Veebipõhine AI, brauseri järeldamine WebGPU-ga

Vali keel, mis sobib kõige paremini sinu kasutusjuhtumi ja juurutamise sihtmärgiga.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.