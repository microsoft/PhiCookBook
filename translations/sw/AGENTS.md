# AGENTS.md

## Muhtasari wa Mradi

PhiCookBook ni hifadhi ya kina ya vitabu vya mapishi inayojumuisha mifano ya vitendo, mafunzo, na nyaraka za kufanya kazi na familia ya Microsoft ya Small Language Models (SLMs). Hifadhi hii inaonyesha matumizi mbalimbali ikiwa ni pamoja na utabiri, kurekebisha, kupunguza ukubwa wa modeli, utekelezaji wa RAG, na matumizi ya multimodal kwenye majukwaa na mifumo tofauti.

**Teknolojia Muhimu:**
- **Lugha:** Python, C#/.NET, JavaScript/Node.js
- **Mifumo:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Majukwaa:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **Aina za Modeli:** Phi-3, Phi-3.5, Phi-4 (maandishi, maono, multimodal, lahaja za kufikiri)

**Muundo wa Hifadhi:**
- `/code/` - Mifano ya kazi ya msimbo na utekelezaji wa sampuli
- `/md/` - Nyaraka za kina, mafunzo, na mwongozo wa jinsi ya kufanya  
- `/translations/` - Tafsiri za lugha nyingi (lugha 50+ kupitia mtiririko wa kazi wa kiotomatiki)
- `/.devcontainer/` - Usanidi wa kontena la maendeleo (Python 3.12 na Ollama)

## Usanidi wa Mazingira ya Maendeleo

### Kutumia GitHub Codespaces au Dev Containers (Inapendekezwa)

1. Fungua kwenye GitHub Codespaces (haraka zaidi):
   - Bonyeza beji ya "Open in GitHub Codespaces" kwenye README
   - Kontena linajisanidi kiotomatiki na Python 3.12 na Ollama na Phi-3

2. Fungua kwenye VS Code Dev Containers:
   - Tumia beji ya "Open in Dev Containers" kutoka README
   - Kontena linahitaji angalau 16GB ya kumbukumbu ya mwenyeji

### Usanidi wa Kawaida

**Mahitaji ya Awali:**
- Python 3.12 au zaidi
- .NET 8.0 SDK (kwa mifano ya C#)
- Node.js 18+ na npm (kwa mifano ya JavaScript)
- Inapendekezwa angalau 16GB RAM

**Usakinishaji:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Kwa Mifano ya Python:**
Nenda kwenye saraka maalum za mifano na usakinishe utegemezi:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**Kwa Mifano ya .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Kwa Mifano ya JavaScript/Web:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Muundo wa Hifadhi

### Mifano ya Msimbo (`/code/`)

- **01.Introduce/** - Utangulizi wa msingi na sampuli za kuanza
- **03.Finetuning/** na **04.Finetuning/** - Mifano ya kurekebisha kwa njia mbalimbali
- **03.Inference/** - Mifano ya utabiri kwenye vifaa tofauti (AIPC, MLX)
- **06.E2E/** - Sampuli za programu za mwisho hadi mwisho
- **07.Lab/** - Utekelezaji wa maabara/majaribio
- **08.RAG/** - Sampuli za Uzalishaji Ulioimarishwa na Urejeshaji
- **09.UpdateSamples/** - Sampuli za hivi karibuni zilizosasishwa

### Nyaraka (`/md/`)

- **01.Introduction/** - Mwongozo wa utangulizi, usanidi wa mazingira, mwongozo wa majukwaa
- **02.Application/** - Sampuli za programu zilizopangwa kwa aina (Maandishi, Msimbo, Maono, Sauti, nk.)
- **02.QuickStart/** - Mwongozo wa kuanza haraka kwa Azure AI Foundry na GitHub Models
- **03.FineTuning/** - Nyaraka na mafunzo ya kurekebisha
- **04.HOL/** - Maabara ya vitendo (inajumuisha mifano ya .NET)

### Miundo ya Faili

- **Jupyter Notebooks (`.ipynb`)** - Mafunzo ya Python ya maingiliano yaliyowekwa alama na 📓 kwenye README
- **Python Scripts (`.py`)** - Mifano ya Python inayojitegemea
- **Miradi ya C# (`.csproj`, `.sln`)** - Programu na sampuli za .NET
- **JavaScript (`.js`, `package.json`)** - Mifano ya AI ya mtandao na Node.js
- **Markdown (`.md`)** - Nyaraka na miongozo

## Kufanya Kazi na Mifano

### Kuendesha Jupyter Notebooks

Mifano mingi inatolewa kama Jupyter notebooks:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Kuendesha Scripts za Python

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Kuendesha Mifano ya .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Au jenga suluhisho zima:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Kuendesha Mifano ya JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Upimaji

Hifadhi hii ina msimbo wa mfano na mafunzo badala ya mradi wa programu wa jadi wenye majaribio ya vitengo. Uthibitishaji hufanyika kwa kawaida kwa:

1. **Kuendesha mifano** - Kila mfano unapaswa kutekelezwa bila makosa
2. **Kuthibitisha matokeo** - Angalia kwamba majibu ya modeli ni sahihi
3. **Kufuata mafunzo** - Mwongozo wa hatua kwa hatua unapaswa kufanya kazi kama ulivyoelezwa

**Njia ya kawaida ya uthibitishaji:**
- Jaribu utekelezaji wa mfano katika mazingira lengwa
- Hakikisha utegemezi unasakinishwa kwa usahihi
- Angalia kwamba modeli inapakuliwa/inapakiwa kwa mafanikio
- Thibitisha tabia inayotarajiwa inalingana na nyaraka

## Mtindo wa Msimbo na Miongozo

### Miongozo ya Jumla

- Mifano inapaswa kuwa wazi, yenye maelezo, na ya kielimu
- Fuata miongozo maalum ya lugha (PEP 8 kwa Python, viwango vya C# kwa .NET)
- Weka mifano ikilenga kuonyesha uwezo maalum wa modeli za Phi
- Jumuisha maelezo yanayoelezea dhana muhimu na vigezo maalum vya modeli

### Viwango vya Nyaraka

**Muundo wa URL:**
- Tumia muundo `[text](../../url)` bila nafasi za ziada
- Viungo vya jamaa: Tumia `./` kwa saraka ya sasa, `../` kwa mzazi
- Hakuna maeneo maalum ya nchi katika URL (epuka `/en-us/`, `/en/`)

**Picha:**
- Hifadhi picha zote kwenye saraka ya `/imgs/`
- Tumia majina ya kuelezea yenye herufi za Kiingereza, namba, na dashes
- Mfano: `phi-3-architecture.png`

**Faili za Markdown:**
- Rejelea mifano halisi ya kazi katika saraka ya `/code/`
- Weka nyaraka zikiwa zimesawazishwa na mabadiliko ya msimbo
- Tumia emoji ya 📓 kuashiria viungo vya Jupyter notebook kwenye README

### Muundo wa Faili

- Mifano ya msimbo katika `/code/` imepangwa kwa mada/kipengele
- Nyaraka katika `/md/` zinaakisi muundo wa msimbo inapowezekana
- Weka faili zinazohusiana (notebooks, scripts, configs) pamoja katika saraka ndogo

## Miongozo ya Pull Request

### Kabla ya Kuwasilisha

1. **Fork hifadhi** kwenye akaunti yako
2. **Tenganisha PRs kwa aina:**
   - Marekebisho ya hitilafu katika PR moja
   - Sasisho za nyaraka katika nyingine
   - Mifano mpya katika PR tofauti
   - Marekebisho ya makosa ya tahajia yanaweza kuunganishwa

3. **Shughulikia migogoro ya kuunganisha:**
   - Sasisha tawi lako la `main` la ndani kabla ya kufanya mabadiliko
   - Sawazisha na hifadhi ya juu mara kwa mara

4. **PR za Tafsiri:**
   - Lazima zijumuishe tafsiri za FAILI ZOTE katika folda
   - Weka muundo thabiti na lugha ya asili

### Ukaguzi Unaohitajika

PRs zinaendesha mtiririko wa kazi wa GitHub kiotomatiki ili kuthibitisha:

1. **Uthibitishaji wa njia jamaa** - Viungo vyote vya ndani vinapaswa kufanya kazi
   - Jaribu viungo kwa ndani: Ctrl+Click katika VS Code
   - Tumia mapendekezo ya njia kutoka VS Code (`./` au `../`)

2. **Ukaguzi wa eneo la URL** - URL za wavuti hazipaswi kuwa na maeneo ya nchi
   - Ondoa `/en-us/`, `/en/`, au misimbo mingine ya lugha
   - Tumia URL za kimataifa za kawaida

3. **Ukaguzi wa URL zilizovunjika** - URL zote lazima zirudishe hali ya 200
   - Thibitisha viungo vinapatikana kabla ya kuwasilisha
   - Kumbuka: Baadhi ya kushindwa kunaweza kuwa kutokana na vizuizi vya mtandao

### Muundo wa Kichwa cha PR

```
[component] Brief description
```

Mifano:
- `[docs] Ongeza mafunzo ya utabiri ya Phi-4`
- `[code] Rekebisha mfano wa ujumuishaji wa ONNX Runtime`
- `[translation] Ongeza tafsiri ya Kijapani kwa miongozo ya utangulizi`

## Mifumo ya Kawaida ya Maendeleo

### Kufanya Kazi na Modeli za Phi

**Upakiaji wa Modeli:**
- Mifano hutumia mifumo mbalimbali: Transformers, ONNX Runtime, MLX, OpenVINO
- Modeli hupakuliwa kwa kawaida kutoka Hugging Face, Azure, au GitHub Models
- Angalia utangamano wa modeli na vifaa vyako (CPU, GPU, NPU)

**Mifumo ya Utabiri:**
- Uzalishaji wa maandishi: Mifano mingi hutumia lahaja za mazungumzo/maelekezo
- Maono: Phi-3-vision na Phi-4-multimodal kwa uelewa wa picha
- Sauti: Phi-4-multimodal inasaidia pembejeo za sauti
- Kufikiri: Lahaja za Phi-4-reasoning kwa kazi za kufikiri za hali ya juu

### Vidokezo Maalum vya Jukwaa

**Azure AI Foundry:**
- Inahitaji usajili wa Azure na funguo za API
- Tazama `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Kiwango cha bure kinapatikana kwa majaribio
- Tazama `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Utabiri wa Kawaida:**
- ONNX Runtime: Utabiri wa majukwaa yote, ulioboreshwa
- Ollama: Usimamizi rahisi wa modeli za ndani (zimesanidiwa awali katika kontena la maendeleo)
- Apple MLX: Imeboreshwa kwa Apple Silicon

## Utatuzi wa Matatizo

### Masuala ya Kawaida

**Masuala ya Kumbukumbu:**
- Modeli za Phi zinahitaji RAM kubwa (hasa lahaja za maono/multimodal)
- Tumia modeli zilizopunguzwa ukubwa kwa mazingira yenye rasilimali chache
- Tazama `/md/01.Introduction/04/QuantifyingPhi.md`

**Migogoro ya Utegemezi:**
- Mifano ya Python inaweza kuwa na mahitaji maalum ya toleo
- Tumia mazingira halisi kwa kila mfano
- Angalia faili za `requirements.txt` za kila mmoja

**Kushindwa kwa Upakuaji wa Modeli:**
- Modeli kubwa zinaweza kushindwa kupakuliwa kwenye muunganisho wa polepole
- Fikiria kutumia mazingira ya wingu (Codespaces, Azure)
- Angalia akiba ya Hugging Face: `~/.cache/huggingface/`

**Masuala ya Mradi wa .NET:**
- Hakikisha .NET 8.0 SDK imewekwa
- Tumia `dotnet restore` kabla ya kujenga
- Baadhi ya miradi ina usanidi maalum wa CUDA (Debug_Cuda)

**Mifano ya JavaScript/Web:**
- Tumia Node.js 18+ kwa utangamano
- Futa `node_modules` na usakinishe tena ikiwa kuna matatizo
- Angalia koni ya kivinjari kwa masuala ya utangamano wa WebGPU

### Kupata Msaada

- **Discord:** Jiunge na Jumuiya ya Azure AI Foundry kwenye Discord
- **GitHub Issues:** Ripoti hitilafu na masuala katika hifadhi
- **GitHub Discussions:** Uliza maswali na shiriki maarifa

## Muktadha wa Ziada

### AI ya Uwajibikaji

Matumizi yote ya modeli za Phi yanapaswa kufuata kanuni za Microsoft za AI ya Uwajibikaji:
- Usawa, uaminifu, usalama
- Faragha na usalama  
- Ujumuishaji, uwazi, uwajibikaji
- Tumia Usalama wa Maudhui ya Azure AI kwa programu za uzalishaji
- Tazama `/md/01.Introduction/01/01.AISafety.md`

### Tafsiri

- Lugha 50+ zinasaidiwa kupitia Hatua ya Kiotomatiki ya GitHub
- Tafsiri ziko kwenye saraka ya `/translations/`
- Zinadumishwa na mtiririko wa kazi wa co-op-translator
- Usihariri faili zilizotafsiriwa kwa mkono (zinazalishwa kiotomatiki)

### Kuchangia

- Fuata miongozo katika `CONTRIBUTING.md`
- Kubali Mkataba wa Leseni ya Mchangiaji (CLA)
- Zingatia Kanuni ya Maadili ya Microsoft Open Source
- Weka usalama na hati za siri nje ya ahadi

### Msaada wa Lugha Nyingi

Hii ni hifadhi ya lugha nyingi yenye mifano katika:
- **Python** - Mifumo ya ML/AI, Jupyter notebooks, kurekebisha
- **C#/.NET** - Programu za biashara, ujumuishaji wa ONNX Runtime
- **JavaScript** - AI ya mtandao, utabiri wa kivinjari na WebGPU

Chagua lugha inayofaa zaidi kwa matumizi yako na lengo la utekelezaji.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.