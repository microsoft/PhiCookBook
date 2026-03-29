# AGENTS.md

## Pregled projekta

PhiCookBook je sveobuhvatni repozitorij kuharica koji sadrži praktične primjere, tutorijale i dokumentaciju za rad s Microsoftovom Phi obitelji malih jezičnih modela (SLMs). Repozitorij pokazuje različite slučajeve upotrebe uključujući izvođenje, fino podešavanje, kvantizaciju, RAG implementacije i multimodalne aplikacije na različitim platformama i okvirima.

**Ključne tehnologije:**
- **Jezici:** Python, C#/.NET, JavaScript/Node.js
- **Okviri:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platforme:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Tipovi modela:** Phi-3, Phi-3.5, Phi-4 (tekstu, viziji, multimodalne, varijante rezoniranja)

**Struktura repozitorija:**
- `/code/` - Funkcionalni primjeri koda i uzorci implementacija
- `/md/` - Detaljna dokumentacija, tutorijali i vodiči  
- `/translations/` - Prevođenja na više jezika (više od 50 jezika putem automatiziranog tijeka rada)
- `/.devcontainer/` - Konfiguracija razvojne okoline (Python 3.12 s Ollamom)

## Postavljanje razvojne okoline

### Korištenje GitHub Codespaces ili Dev Containers (preporučeno)

1. Otvorite u GitHub Codespaces (najjače i najbrže):
   - Kliknite na oznaku "Open in GitHub Codespaces" u README-u
   - Kontejner se automatski konfigurira s Python 3.12 i Ollama Phi-3 modelom

2. Otvorite u VS Code Dev Containers:
   - Koristite oznaku "Open in Dev Containers" iz README-a
   - Kontejner zahtijeva minimalno 16GB RAM-a na hostu

### Lokalno postavljanje

**Preduvjeti:**
- Python 3.12 ili noviji
- .NET 8.0 SDK (za C# primjere)
- Node.js 18+ i npm (za JavaScript primjere)
- Preporučeno minimum 16GB RAM-a

**Instalacija:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Za Python primjere:**
Idite u direktorije s određenim primjerima i instalirajte ovisnosti:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # ako datoteka requirements.txt postoji
```

**Za .NET primjere:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Za JavaScript/Web primjere:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Pokreni razvojni server
npm run build  # Izgradi za produkciju
```

## Organizacija repozitorija

### Primjeri koda (`/code/`)

- **01.Introduce/** - Osnovni uvodi i primjeri za početak rada
- **03.Finetuning/** i **04.Finetuning/** - Primjeri fino podešavanja s različitim metodama
- **03.Inference/** - Primjeri izvođenja na različitom hardveru (AIPC, MLX)
- **06.E2E/** - Primjeri cjelovitih aplikacija
- **07.Lab/** - Laboratorijske/eksperimentalne implementacije
- **08.RAG/** - Primjeri generacije s proširenom dohvatom (RAG)
- **09.UpdateSamples/** - Najnovije ažurirane primjere

### Dokumentacija (`/md/`)

- **01.Introduction/** - Uvodni vodiči, postavljanje okoline, vodiči za platforme
- **02.Application/** - Primjeri aplikacija raspoređeni po tipu (Tekst, Kod, Vizija, Audio itd.)
- **02.QuickStart/** - Vodiči za brzi početak s Microsoft Foundry i GitHub Models
- **03.FineTuning/** - Dokumentacija i tutorijali za fino podešavanje
- **04.HOL/** - Praktični laboratoriji (uključuje .NET primjere)

### Formati datoteka

- **Jupyter bilježnice (`.ipynb`)** - Interaktivni Python tutorijali označeni s 📓 u README-u
- **Python skripte (`.py`)** - Samostalni Python primjeri
- **C# projekti (`.csproj`, `.sln`)** - .NET aplikacije i uzorci
- **JavaScript (`.js`, `package.json`)** - Web i Node.js primjeri
- **Markdown (`.md`)** - Dokumentacija i vodiči

## Rad s primjerima

### Pokretanje Jupyter bilježnica

Većina primjera je dostupna kao Jupyter bilježnice:
```bash
pip install jupyter notebook
jupyter notebook  # Otvara sučelje preglednika
# Navigirajte do željene .ipynb datoteke
```

### Pokretanje Python skripti

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Pokretanje .NET primjera

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Ili izgradnja cijelog rješenja:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Pokretanje JavaScript/Web primjera

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Razvoj s vrućim ponovnim učitavanjem
```

## Testiranje

Ovaj repozitorij sadrži primjerni kod i tutorijale, a ne klasičan softverski projekt s jedinicama testova. Validacija se obično radi putem:

1. **Pokretanja primjera** - Svaki primjer treba raditi bez pogrešaka
2. **Provjere rezultata** - Provjerite jesu li odgovori modela primjereni
3. **Praćenja tutorijala** - Koraci u vodičima bi trebali funkcionirati kako je dokumentirano

**Uobičajeni pristup validaciji:**
- Testirati izvršenje primjera u ciljanom okruženju
- Provjeriti ispravnost instalacije ovisnosti
- Osigurati uspješno preuzimanje/učitavanje modela
- Potvrditi da se očekivano ponašanje slaže s dokumentacijom

## Stil koda i konvencije

### Opće smjernice

- Primjeri treba biti jasni, dobro komentirani i edukativni
- Slijediti konvencije specifične za jezik (PEP 8 za Python, standardi za C#/.NET)
- Primjeri se trebaju fokusirati na demonstraciju specifičnih sposobnosti Phi modela
- Uključiti komentare koji objašnjavaju ključne koncepte i parametre specifične za model

### Standardi dokumentacije

**Formatiranje URL-ova:**
- Koristiti format `[text](../../url)` bez dodatnih razmaka
- Relativne veze: koristiti `./` za trenutačni direktorij, `../` za roditeljski
- Ne koristiti lokalizacije zemalja u URL-ovima (izbjegavati `/en-us/`, `/en/`)

**Slike:**
- Sve slike pohraniti u direktorij `/imgs/`
- Koristiti opisne nazive s engleskim znakovima, brojkama i crticama
- Primjer: `phi-3-architecture.png`

**Markdown datoteke:**
- Reference na stvarne funkcionalne primjere u direktoriju `/code/`
- Održavati sinkronizaciju dokumentacije s promjenama u kodu
- Koristiti 📓 emoji za označavanje linkova na Jupyter bilježnice u README-u

### Organizacija datoteka

- Primjeri koda u `/code/` organizirani po temama/svojstvima
- Dokumentacija u `/md/` prati strukturu koda gdje je primjenjivo
- Povremeno držati povezane datoteke (bilježnice, skripte, konfiguracije) zajedno u poddirektorijima

## Smjernice za Pull Requestove

### Prije slanja

1. **Forkajte repozitorij** na svoj račun
2. **Razdvojite PR po tipu:**
   - Ispravke grešaka u jednom PR-u
   - Ažuriranja dokumentacije u drugom
   - Novi primjeri u zasebnim PR-ovima
   - Ispravke pravopisnih pogrešaka mogu biti spojene

3. **Rješavanje sukoba pri spajanju:**
   - Ažurirajte lokalni `main` prije izmjena
   - Često sinkronizirajte s glavnim repozitorijem

4. **PR-ovi za prijevode:**
   - Moraju uključivati prijevode za SVE datoteke u direktoriju
   - Održavati konzistentnu strukturu s izvornim jezikom

### Obavezne provjere

PR-ovi automatski pokreću GitHub tijekove rada za kontrolu:

1. **Provjera relativnih putanja** - Sve interne veze moraju raditi
   - Testirati linkove lokalno: Ctrl+Click u VS Codeu
   - Koristiti prijedloge putanja iz VS Codea (`./` ili `../`)

2. **Provjera lokalizacije URL-ova** - URL-ovi na webu ne smiju sadržavati lokalizacije država
   - Ukloniti `/en-us/`, `/en/` ili druge kodove jezika
   - Koristiti opće međunarodne URL-ove

3. **Provjera neispravnih URL-ova** - Svi URL-ovi moraju vratiti status 200
   - Provjeriti dostupnost linkova prije slanja
   - Napomena: neke greške mogu biti zbog mrežnih ograničenja

### Format naslova PR-a

```
[component] Brief description
```

Primjeri:
- `[docs] Dodaj tutorial za izvođenje s Phi-4`
- `[code] Ispravi primjer integracije ONNX Runtime`
- `[translation] Dodaj japanski prijevod za uvodne vodiče`

## Uobičajeni obrasci razvoja

### Rad s Phi modelima

**Učitavanje modela:**
- Primjeri koriste različite okvire: Transformers, ONNX Runtime, MLX, OpenVINO
- Modeli se obično preuzimaju s Hugging Face, Azure ili GitHub Models
- Provjeriti kompatibilnost modela s vašim hardverom (CPU, GPU, NPU)

**Obrasci izvođenja:**
- Generiranje teksta: Većina primjera koristi chat/instruct varijante
- Vizija: Phi-3-vision i Phi-4-multimodal za razumijevanje slika
- Audio: Phi-4-multimodal podržava audio ulaze
- Rezoniranje: Phi-4-reasoning varijante za napredne zadatke rezoniranja

### Bilješke vezane uz platforme

**Microsoft Foundry:**
- Zahtijeva Azure pretplatu i API ključeve
- Pogledajte `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Besplatni sloj za testiranje
- Pogledajte `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokalno izvođenje:**
- ONNX Runtime: Višeplatformski, optimizirano izvođenje
- Ollama: Jednostavno upravljanje lokalnim modelima (predkonfigurirano u dev kontejneru)
- Apple MLX: Optimizirano za Apple Silicon

## Rješavanje problema

### Česti problemi

**Problemi s memorijom:**
- Phi modeli zahtijevaju značajnu RAM memoriju (posebno vizija/multimodalne varijante)
- Koristite kvantizirane modele za ograničene resurse
- Pogledajte `/md/01.Introduction/04/QuantifyingPhi.md`

**Sukobi ovisnosti:**
- Python primjeri mogu imati specifične zahtjeve verzija
- Koristite virtualna okruženja za svaki primjer
- Provjerite pojedinačne datoteke `requirements.txt`

**Neuspjeh preuzimanja modela:**
- Veliki modeli mogu istekati na sporim vezama
- Razmislite o korištenju cloud okoline (Codespaces, Azure)
- Provjerite Hugging Face cache: `~/.cache/huggingface/`

**Problemi s .NET projektima:**
- Provjerite da je instaliran .NET 8.0 SDK
- Koristite `dotnet restore` prije izgradnje
- Neki projekti imaju CUDA specifične konfiguracije (Debug_Cuda)

**JavaScript/Web primjeri:**
- Koristiti Node.js 18+ za kompatibilnost
- Obrisite `node_modules` i ponovno instalirajte ako problemi ostaju
- Provjerite konzolu preglednika za probleme kompatibilnosti s WebGPU

### Dobivanje pomoći

- **Discord:** Pridružite se Microsoft Foundry zajednici na Discordu
- **GitHub Issues:** Prijavite greške i probleme u repozitorij
- **GitHub Discussions:** Postavljajte pitanja i dijelite znanje

## Dodatni kontekst

### Odgovorni AI

Sva upotreba Phi modela treba se pridržavati Microsoftovih principa Odgovornog AI:
- Pravednost, pouzdanost, sigurnost
- Privatnost i sigurnost  
- Uključenost, transparentnost, odgovornost
- Koristite Azure AI Content Safety za produkcijske aplikacije
- Pogledajte `/md/01.Introduction/01/01.AISafety.md`

### Prijevodi

- Podrška za 50+ jezika putem automatizirane GitHub akcije
- Prijevodi u direktoriju `/translations/`
- Održava suradnički proces prijevoda
- Nemojte ručno mijenjati prevedene datoteke (automatski generirano)

### Doprinos

- Slijedite smjernice u `CONTRIBUTING.md`
- Prihvatite Contributor License Agreement (CLA)
- Poštujte Microsoftov Kodeks ponašanja za otvoreni izvor
- Nemojte uključivati sigurnosne podatke ili vjerodajnice u commite

### Podrška za više jezika

Ovo je poliglotski repozitorij s primjerima u:
- **Python** - ML/AI tijekovi, Jupyter bilježnice, fino podešavanje
- **C#/.NET** - Enterprise aplikacije, integracija ONNX Runtime-a
- **JavaScript** - Web AI, izvođenje u pregledniku putem WebGPU

Odaberite jezik koji najbolje odgovara vašem slučaju i ciljanoj platformi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument preveden je korištenjem AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->