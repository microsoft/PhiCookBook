# AGENTS.md

## Projekti ülevaade

PhiCookBook on põhjalik retseptide hoidla, mis sisaldab praktilisi näiteid, juhendeid ja dokumentatsiooni Microsofti Phi väikeste keelemudelite (SLM-id) kasutamiseks. Hoidla demonstreerib erinevaid kasutusjuhtumeid, sealhulgas järeldamist, peenhäälestamist, kvantiseerimist, RAG-teostusi ja multimodaalseid rakendusi erinevatel platvormidel ja raamistikudel.

**Peamised tehnoloogiad:**
- **Keeled:** Python, C#/.NET, JavaScript/Node.js
- **Raamistikud:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platvormid:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Mudelitüübid:** Phi-3, Phi-3.5, Phi-4 (teksti-, nägemis-, multimodaalsed ja järeldusvariandid)

**Hoidla struktuur:**
- `/code/` - Töökoodinäited ja prooviteostused
- `/md/` - Detailne dokumentatsioon, juhendid ja kuidas teha õpetused  
- `/translations/` - Mitmekeelsed tõlked (50+ keelt läbi automatiseeritud töövoo)
- `/.devcontainer/` - Arenduskonteineri konfiguratsioon (Python 3.12 koos Ollamaga)

## Arenduskeskkonna seadistus

### Kasutades GitHub Codespaces või Dev konteinerid (Soovitatav)

1. Ava GitHub Codespaces'is (kiireim):
   - Klõpsa README failis "Open in GitHub Codespaces" märgisel
   - Konteiner seadistub automaatselt Python 3.12 ja Phi-3 Ollama mudeliga

2. Ava VS Code Dev konteinerites:
   - Kasuta README faili märgist "Open in Dev Containers"
   - Konteiner vajab vähemalt 16GB mälu hostilt

### Kohalik seadistus

**Eeltingimused:**
- Python 3.12 või uuem
- .NET 8.0 SDK (C# näidete jaoks)
- Node.js 18+ ja npm (JavaScripti näidete jaoks)
- Soovitatav vähemalt 16GB RAM

**Paigaldus:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Pythoni näidete jaoks:**
Mine konkreetsete näidiste kataloogidesse ja paigalda sõltuvused:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # kui faili requirements.txt eksisteerib
```

**.NET näidete jaoks:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**JavaScripti/veebinäidete jaoks:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Käivita arendusserver
npm run build  # Ehita tootmiseks
```

## Hoidla korraldus

### Koodinäited (`/code/`)

- **01.Introduce/** - Põhilised sissejuhatused ja alustamisnäited
- **03.Finetuning/** ja **04.Finetuning/** - Peenhäälestamise näited erinevate meetoditega
- **03.Inference/** - Järeldamise näited erinevatel riistvaradel (AIPC, MLX)
- **06.E2E/** - Otse-üles lõpprakenduste näited
- **07.Lab/** - Laboratoorsed/katseliseksotused
- **08.RAG/** - Väljavahtutugev genereerimine (RAG) näited
- **09.UpdateSamples/** - Viimased uuendatud näited

### Dokumentatsioon (`/md/`)

- **01.Introduction/** - Sissejuhatus, keskkonna seadistus, platvormijuhised
- **02.Application/** - Rakendusnäited kategooriate kaupa (tekst, kood, nägemine, heli jne)
- **02.QuickStart/** - Kiirjuhendid Microsoft Foundry ja GitHub Mudelite jaoks
- **03.FineTuning/** - Peenhäälestamise dokumentatsioon ja juhendid
- **04.HOL/** - Käed-külge laborid (sisaldab .NET näiteid)

### Failivormingud

- **Jupyter Notebook'id (`.ipynb`)** - Interaktiivsed Python juhtnöörid, märgitud 📓 README-s
- **Pythoni skriptid (`.py`)** - Iseseisvad Pythoni näited
- **C# projektid (`.csproj`, `.sln`)** - .NET rakendused ja näited
- **JavaScript (`.js`, `package.json`)** - Veebipõhised ja Node.js näited
- **Markdown (`.md`)** - Dokumentatsioon ja juhendid

## Näidete kasutamine

### Jupyter Notebook'ide käivitamine

Enamik näiteid on esitatud Jupyter notebook'idena:
```bash
pip install jupyter notebook
jupyter notebook  # Avab brauseri liidese
# Navigeeri soovitud .ipynb faili juurde
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

### JavaScripti/veebinäidete käivitamine

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Arendus koos kuuma laadimisega
```

## Testimine

See hoidla sisaldab näitekoodi ja juhendeid, mitte traditsioonilist tarkvaraprojekti koos üksustestidega. Kinnitamine toimub tavaliselt järgmiselt:

1. **Näidete käivitamine** - Iga näide peaks veata jooksma
2. **Väljundite kontroll** - Mudeli vastused peavad olema sobivad
3. **Juhendite järgiv käivitamine** - Samm-sammult juhiste alusel töötamine peab õnnestuma

**Tavaline valideerimise lähenemine:**
- Testi näidete täitmist sihtkeskkonnas
- Veendu, et sõltuvused paigaldatakse õigesti
- Kontrolli, et mudeli allalaadimine/laadimine õnnestub
- Kinnita, et oodatud käitumine vastab dokumentatsioonile

## Koodistiil ja konventsioonid

### Üldised juhised

- Näited peavad olema selged, hästi kommenteeritud ja harivad
- Järgi keele spetsiifilisi konventsioone (PEP 8 Pythonile, C# standardid .NET-le)
- Hoia näited konkreetsetele Phi mudeli võimalustele keskendunud
- Lisa kommentaarid, mis selgitavad võtmekontsepte ja mudeli spetsiifilisi parameetreid

### Dokumentatsiooni standardid

**URL-e vormindamine:**
- Kasuta vormingut `[tekst](../../url)` ilma lisatühikuteta
- Suhtelised viited: kasuta `./` praeguse kataloogi jaoks, `../` ülemkataloogi jaoks
- Vältida riigipõhiseid kohalikke keeli URL-ides (väldi `/en-us/`, `/en/`)

**Pildid:**
- Talleta kõik pildid kataloogi `/imgs/`
- Kasuta kirjeldavaid nimesid ingliskeelsete tähtede, numbrite ja kriipsudega
- Näide: `phi-3-architecture.png`

**Markdown failid:**
- Viita reaalselt töötavatele näidetele kataloogis `/code/`
- Hoia dokumentatsioon sünkroonis koodi muudatustega
- Märgista Jupyter notebook'i lingid README-s 📓 emotikoniga

### Failide korraldus

- Koodinäited kataloogis `/code/` organiseeritud teema/funktsiooni järgi
- Dokumentatsioon kataloogis `/md/` peegeldab vajadusel koodi struktuuri
- Hoia seotud failid (notebookid, skriptid, konfiguratsioonid) koos kaustades

## Pull requesti juhised

### Enne esitust

1. **Forki hoidla** oma kontole
2. **Eralda PR-id tüübi järgi:**
   - Veaparandused ühes PR-is
   - Dokumentatsiooni uuendused teises
   - Uued näited eraldi PR-idena
   - Kirjaveaparandused võib ühendada

3. **Lahenda ühinemis konfliktid:**
   - Uuenda oma lokaalset `main` haru enne muudatuste tegemist
   - Sünkrooni regulaarselt upstream'iga

4. **Tõlke PR-id:**
   - Peavad sisaldama tõlkeid KÕIGILE kausta failidele
   - Säilita originaalkeele struktuur

### Nõutavad kontrollid

PR-id käivitavad automaatselt GitHub töövood valideerimiseks:

1. **Suhtelise tee valideerimine** - Kõik sisemised lingid peavad töötama
   - Testi linke lokaalsetes tingimustes: Ctrl+klõps VS Code'is
   - Kasuta VS Code soovitusi teedele (`./` või `../`)

2. **URL-i keelekontroll** - Veebiaadressid ei tohi sisaldada riiklike keeli
   - Eemalda `/en-us/`, `/en/` või muud keelekoodid
   - Kasuta üldist rahvusvahelist URL-i

3. **Katkiste URL-ide kontroll** - Kõik URL-id peavad tagastama 200 staatuse
   - Kontrolli linkide ligipääsetavust enne esitamist
   - Märkus: Mõned ebaõnnestumised võivad olla võrgu piirangute tõttu

### PR pealkirja vorming

```
[component] Brief description
```

Näited:
- `[docs] Lisa Phi-4 järeldamise juhend`
- `[code] Paranda ONNX Runtime'i integratsiooni näide`
- `[translation] Lisa jaapani tõlge sissejuhatuse juhenditele`

## Tavalised arenduse mustrid

### Phi mudelitega töötamine

**Mudelite laadimine:**
- Näited kasutavad erinevaid raamistikke: Transformers, ONNX Runtime, MLX, OpenVINO
- Mudelid allalaaditavad tavaliselt Hugging Face, Azure või GitHub Models kaudu
- Kontrolli mudeli ühilduvust oma riistvaraga (CPU, GPU, NPU)

**Järeldamise mustrid:**
- Tekstigeneratsioon: enamik näiteid kasutab vestlus- või juhendvarianti
- Nägemine: Phi-3-nägemine ja Phi-4-multimodaalne pildi mõistmiseks
- Heli: Phi-4-multimodaalne toetab helisisendeid
- Järeldamine: Phi-4-järeldus variandid keerukamate ülesannete jaoks

### Platvormispetsiifilised märkused

**Microsoft Foundry:**
- Vajab Azure tellimust ja API-võtmeid
- Vaata `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Testimiseks olemas tasuta kiht
- Vaata `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Kohalik järeldamine:**
- ONNX Runtime: platvormideülene, optimeeritud järeldamine
- Ollama: lihtne kohalik mudelite haldus (eelkonfigureeritud dev konteineris)
- Apple MLX: optimeeritud Apple Siliconile

## Tõrkeotsing

### Tavalised probleemid

**Mälu probleemid:**
- Phi mudelid vajavad märkimisväärselt RAM-i (eriti nägemis- ja multimodaalsed variandid)
- Kasuta kvantiseeritud mudeleid madalamate ressursside puhul
- Vaata `/md/01.Introduction/04/QuantifyingPhi.md`

**Sõltuvuste konfliktid:**
- Pythoni näidetel võivad olla spetsiifilised versiooninõuded
- Kasuta iga näite jaoks virtuaalset keskkonda
- Kontrolli individuaalseid `requirements.txt` faile

**Mudeli allalaadimise ebaõnnestumised:**
- Suured mudelid võivad aeglustuda aeglastel ühendustel
- Mõtle pilvekeskkondadele (Codespaces, Azure)
- Kontrolli Hugging Face'i vahemälu: `~/.cache/huggingface/`

**.NET projekti probleemid:**
- Veendu, et .NET 8.0 SDK on paigaldatud
- Kasuta `dotnet restore` enne ehitamist
- Mõnel projektil CUDA-spetsiifilised konfiguratsioonid (Debug_Cuda)

**JavaScripti/veebinäited:**
- Kasuta Node.js 18+ ühilduvuse tagamiseks
- Kui probleemid jätkuvad, kustuta `node_modules` ja paigalda uuesti
- Kontrolli brauseri konsool WebGPU ühilduvuse vigade osas

### Abi saamine

- **Discord:** Liitu Microsoft Foundry kogukonna Discordiga
- **GitHub Issues:** Teata vigadest ja probleemidest hoidlasse
- **GitHub Discussions:** Küsi küsimusi ja jaga teadmisi

## Täiendav kontekst

### Vastutustundlik tehisintellekt

Kõik Phi mudelite kasutamine peab järgima Microsofti vastutustundliku tehisintellekti põhimõtteid:
- Õiglus, usaldusväärsus, ohutus
- Privaatsus ja turvalisus  
- Kaasatus, läbipaistvus, vastutustundlikkus
- Kasuta Azure AI Content Safety tootmiskasutuses
- Vaata `/md/01.Introduction/01/01.AISafety.md`

### Tõlked

- 50+ keelt toetatud automaatse GitHub Actions töövoo kaudu
- Tõlked kataloogis `/translations/`
- Halda ko-opia-tõlkija töövoo kaudu
- Ära muuda käsitsi tõlgitud faile (automaatselt genereeritud)

### Panustamine

- Järgi juhiseid failis `CONTRIBUTING.md`
- Luba panustajate litsentsileping (CLA)
- Järgi Microsofti avatud lähtekoodi käitumiskoodi
- Hoia turva- ja volituste andmed commit'idest eemal

### Mitmekeelne tugi

See on mitmekeelne hoidla näidetega:
- **Python** - ML/AI töövood, Jupyter notebook'id, peenhäälestamine
- **C#/.NET** - Mudelintegreerimine, ettevõtte rakendused
- **JavaScript** - Veebipõhine tehisintellekt, brauseri järeldamine WebGPU abil

Vali keel, mis sobib kõige paremini sinu kasutusjuhtumi ja juurutamise sihtkohaga.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest vabastamine**:
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selles originaalkeeles tuleks pidada autoriteetseks allikaks. Kritiliste andmete puhul soovitatakse professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->