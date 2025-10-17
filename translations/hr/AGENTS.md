<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "72e00a4ddbe9d6c25907d1eb19d041b8",
  "translation_date": "2025-10-17T11:02:59+00:00",
  "source_file": "AGENTS.md",
  "language_code": "hr"
}
-->
# AGENTS.md

## Pregled projekta

PhiCookBook je sveobuhvatan repozitorij kuharica koji sadrži praktične primjere, vodiče i dokumentaciju za rad s Microsoftovom Phi obitelji malih jezičnih modela (SLM). Repozitorij prikazuje različite primjene, uključujući inferenciju, fino podešavanje, kvantizaciju, implementacije RAG-a i multimodalne aplikacije na različitim platformama i okvirima.

**Ključne tehnologije:**
- **Jezici:** Python, C#/.NET, JavaScript/Node.js
- **Okviri:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platforme:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **Tipovi modela:** Phi-3, Phi-3.5, Phi-4 (tekst, vizija, multimodalni, varijante za zaključivanje)

**Struktura repozitorija:**
- `/code/` - Primjeri koda i uzorci implementacija
- `/md/` - Detaljna dokumentacija, vodiči i upute  
- `/translations/` - Prijevodi na više jezika (50+ jezika putem automatiziranog tijeka rada)
- `/.devcontainer/` - Konfiguracija razvojnih spremnika (Python 3.12 s Ollama)

## Postavljanje razvojnog okruženja

### Korištenje GitHub Codespaces ili razvojnih spremnika (preporučeno)

1. Otvorite u GitHub Codespaces (najbrže):
   - Kliknite na oznaku "Open in GitHub Codespaces" u README
   - Spremnik se automatski konfigurira s Python 3.12 i Ollama s Phi-3

2. Otvorite u VS Code razvojnim spremnicima:
   - Koristite oznaku "Open in Dev Containers" iz README
   - Spremnik zahtijeva minimalno 16GB memorije na hostu

### Lokalno postavljanje

**Preduvjeti:**
- Python 3.12 ili noviji
- .NET 8.0 SDK (za primjere u C#)
- Node.js 18+ i npm (za primjere u JavaScriptu)
- Preporučeno minimalno 16GB RAM-a

**Instalacija:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Za primjere u Pythonu:**
Idite u specifične direktorije s primjerima i instalirajte ovisnosti:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**Za primjere u .NET-u:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Za primjere u JavaScriptu/Webu:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Organizacija repozitorija

### Primjeri koda (`/code/`)

- **01.Introduce/** - Osnovni uvodi i uzorci za početak
- **03.Finetuning/** i **04.Finetuning/** - Primjeri fino podešavanja različitim metodama
- **03.Inference/** - Primjeri inferencije na različitim hardverima (AIPC, MLX)
- **06.E2E/** - Uzorci aplikacija od početka do kraja
- **07.Lab/** - Laboratorijske/eksperimentalne implementacije
- **08.RAG/** - Uzorci generacije uz pomoć pretraživanja
- **09.UpdateSamples/** - Najnoviji ažurirani uzorci

### Dokumentacija (`/md/`)

- **01.Introduction/** - Uvodni vodiči, postavljanje okruženja, vodiči za platforme
- **02.Application/** - Uzorci aplikacija organizirani po tipu (Tekst, Kod, Vizija, Audio, itd.)
- **02.QuickStart/** - Brzi vodiči za Azure AI Foundry i GitHub Models
- **03.FineTuning/** - Dokumentacija i vodiči za fino podešavanje
- **04.HOL/** - Praktične laboratorijske vježbe (uključuje primjere u .NET-u)

### Formati datoteka

- **Jupyter bilježnice (`.ipynb`)** - Interaktivni Python vodiči označeni s 📓 u README
- **Python skripte (`.py`)** - Samostalni primjeri u Pythonu
- **C# projekti (`.csproj`, `.sln`)** - .NET aplikacije i uzorci
- **JavaScript (`.js`, `package.json`)** - Web-bazirani i Node.js primjeri
- **Markdown (`.md`)** - Dokumentacija i vodiči

## Rad s primjerima

### Pokretanje Jupyter bilježnica

Većina primjera dostupna je kao Jupyter bilježnice:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
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

Ili izgradite cijelo rješenje:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Pokretanje JavaScript/Web primjera

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Testiranje

Ovaj repozitorij sadrži primjere koda i vodiče, a ne tradicionalni softverski projekt s jedinicnim testovima. Validacija se obično provodi:

1. **Pokretanjem primjera** - Svaki primjer treba se izvršiti bez grešaka
2. **Provjerom izlaza** - Provjerite da su odgovori modela odgovarajući
3. **Slijeđenjem vodiča** - Vodiči korak po korak trebaju raditi kako je dokumentirano

**Uobičajeni pristup validaciji:**
- Testirajte izvršenje primjera u ciljanom okruženju
- Provjerite da se ovisnosti ispravno instaliraju
- Provjerite da se modeli uspješno preuzimaju/učitavaju
- Potvrdite da očekivano ponašanje odgovara dokumentaciji

## Stil koda i konvencije

### Opće smjernice

- Primjeri trebaju biti jasni, dobro komentirani i edukativni
- Slijedite konvencije specifične za jezik (PEP 8 za Python, standardi za C# u .NET-u)
- Primjeri trebaju biti usmjereni na demonstraciju specifičnih mogućnosti Phi modela
- Uključite komentare koji objašnjavaju ključne koncepte i parametre specifične za model

### Standardi dokumentacije

**Formatiranje URL-ova:**
- Koristite format `[tekst](../../url)` bez dodatnih razmaka
- Relativne poveznice: Koristite `./` za trenutni direktorij, `../` za nadređeni
- Izbjegavajte lokalizirane URL-ove (izbjegavajte `/en-us/`, `/en/`)

**Slike:**
- Pohranite sve slike u direktorij `/imgs/`
- Koristite opisne nazive s engleskim znakovima, brojevima i crticama
- Primjer: `phi-3-architecture.png`

**Markdown datoteke:**
- Referencirajte stvarne radne primjere u direktoriju `/code/`
- Održavajte dokumentaciju sinkroniziranu s promjenama koda
- Koristite 📓 emoji za označavanje poveznica na Jupyter bilježnice u README

### Organizacija datoteka

- Primjeri koda u `/code/` organizirani po temi/značajci
- Dokumentacija u `/md/` prati strukturu koda kad je primjenjivo
- Držite povezane datoteke (bilježnice, skripte, konfiguracije) zajedno u poddirektorijima

## Smjernice za Pull Requestove

### Prije slanja

1. **Forkajte repozitorij** na svoj račun
2. **Razdvojite PR-ove po tipu:**
   - Ispravci grešaka u jednom PR-u
   - Ažuriranja dokumentacije u drugom
   - Novi primjeri u zasebnim PR-ovima
   - Ispravci tipografskih grešaka mogu se kombinirati

3. **Rješavanje sukoba pri spajanju:**
   - Ažurirajte svoju lokalnu granu `main` prije nego što napravite promjene
   - Često sinkronizirajte s izvornim repozitorijem

4. **PR-ovi za prijevode:**
   - Moraju uključivati prijevode za SVE datoteke u mapi
   - Održavajte dosljednu strukturu s izvornim jezikom

### Obavezne provjere

PR-ovi automatski pokreću GitHub tijekove rada za validaciju:

1. **Validacija relativnih putanja** - Sve interne poveznice moraju raditi
   - Testirajte poveznice lokalno: Ctrl+Klik u VS Code
   - Koristite prijedloge putanja iz VS Code (`./` ili `../`)

2. **Provjera lokalizacije URL-ova** - Web URL-ovi ne smiju sadržavati lokalizacijske kodove
   - Uklonite `/en-us/`, `/en/` ili druge jezične kodove
   - Koristite generičke međunarodne URL-ove

3. **Provjera neispravnih URL-ova** - Svi URL-ovi moraju vraćati status 200
   - Provjerite da su poveznice dostupne prije slanja
   - Napomena: Neki neuspjesi mogu biti zbog mrežnih ograničenja

### Format naslova PR-a

```
[component] Brief description
```

Primjeri:
- `[docs] Dodaj vodič za inferenciju Phi-4`
- `[code] Ispravi primjer integracije ONNX Runtime`
- `[translation] Dodaj japanski prijevod za uvodne vodiče`

## Uobičajeni razvojni obrasci

### Rad s Phi modelima

**Učitavanje modela:**
- Primjeri koriste različite okvire: Transformers, ONNX Runtime, MLX, OpenVINO
- Modeli se obično preuzimaju s Hugging Face, Azure ili GitHub Models
- Provjerite kompatibilnost modela s vašim hardverom (CPU, GPU, NPU)

**Obrasci inferencije:**
- Generiranje teksta: Većina primjera koristi chat/instruct varijante
- Vizija: Phi-3-vision i Phi-4-multimodal za razumijevanje slika
- Audio: Phi-4-multimodal podržava audio ulaze
- Zaključivanje: Phi-4-reasoning varijante za napredne zadatke zaključivanja

### Napomene specifične za platformu

**Azure AI Foundry:**
- Zahtijeva Azure pretplatu i API ključeve
- Pogledajte `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Dostupan besplatni sloj za testiranje
- Pogledajte `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokalna inferencija:**
- ONNX Runtime: Višestruka platforma, optimizirana inferencija
- Ollama: Jednostavno lokalno upravljanje modelima (predkonfigurirano u razvojnom spremniku)
- Apple MLX: Optimizirano za Apple Silicon

## Rješavanje problema

### Uobičajeni problemi

**Problemi s memorijom:**
- Phi modeli zahtijevaju značajnu RAM memoriju (posebno vizualne/multimodalne varijante)
- Koristite kvantizirane modele za okruženja s ograničenim resursima
- Pogledajte `/md/01.Introduction/04/QuantifyingPhi.md`

**Sukobi ovisnosti:**
- Primjeri u Pythonu mogu imati specifične zahtjeve za verzijama
- Koristite virtualna okruženja za svaki primjer
- Provjerite pojedinačne `requirements.txt` datoteke

**Neuspjesi preuzimanja modela:**
- Veliki modeli mogu isteći na sporim vezama
- Razmislite o korištenju cloud okruženja (Codespaces, Azure)
- Provjerite Hugging Face cache: `~/.cache/huggingface/`

**Problemi s .NET projektima:**
- Provjerite je li instaliran .NET 8.0 SDK
- Koristite `dotnet restore` prije izgradnje
- Neki projekti imaju CUDA-specifične konfiguracije (Debug_Cuda)

**JavaScript/Web primjeri:**
- Koristite Node.js 18+ za kompatibilnost
- Očistite `node_modules` i ponovno instalirajte ako se pojave problemi
- Provjerite konzolu preglednika za probleme s kompatibilnošću WebGPU-a

### Dobivanje pomoći

- **Discord:** Pridružite se Azure AI Foundry Community Discordu
- **GitHub Issues:** Prijavite greške i probleme u repozitoriju
- **GitHub Discussions:** Postavljajte pitanja i dijelite znanje

## Dodatni kontekst

### Odgovorna AI

Sva upotreba Phi modela treba slijediti Microsoftova načela odgovorne AI:
- Pravednost, pouzdanost, sigurnost
- Privatnost i sigurnost  
- Uključivost, transparentnost, odgovornost
- Koristite Azure AI Content Safety za produkcijske aplikacije
- Pogledajte `/md/01.Introduction/01/01.AISafety.md`

### Prijevodi

- Podržano 50+ jezika putem automatizirane GitHub akcije
- Prijevodi u direktoriju `/translations/`
- Održava ih co-op-translator tijek rada
- Nemojte ručno uređivati prevedene datoteke (automatski generirane)

### Doprinos

- Slijedite smjernice u `CONTRIBUTING.md`
- Pristanite na Contributor License Agreement (CLA)
- Pridržavajte se Microsoft Open Source Code of Conduct
- Nemojte uključivati sigurnosne podatke i vjerodajnice u commitove

### Podrška za više jezika

Ovo je poliglot repozitorij s primjerima u:
- **Python** - ML/AI tijekovi rada, Jupyter bilježnice, fino podešavanje
- **C#/.NET** - Poslovne aplikacije, integracija ONNX Runtime-a
- **JavaScript** - AI za web, inferencija u pregledniku s WebGPU-om

Odaberite jezik koji najbolje odgovara vašem slučaju upotrebe i cilju implementacije.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne odgovaramo za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.