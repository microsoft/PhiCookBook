# AGENTS.md

## Muhtasari wa Mradi

PhiCookBook ni hazina kamili ya vitabu vya mapishi inayojumuisha mifano ya vitendo, mafunzo, na nyaraka za kufanya kazi na familia za Phi za Microsoft za Modeli Ndogo za Lugha (SLMs). Hazina hii inaonyesha matumizi mbalimbali ikiwa ni pamoja na kutabiri, kufanyia marekebisho model, kupunguza ukubwa wa modeli, utekelezaji wa RAG, na matumizi ya multimodal katika majukwaa na mifumo tofauti.

**Teknolojia Muhimu:**
- **Lugha:** Python, C#/.NET, JavaScript/Node.js
- **Mifumo:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Majukwaa:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Aina za Modeli:** Phi-3, Phi-3.5, Phi-4 (maandishi, kuona, multimodal, tofauti za kufikiri)

**Muundo wa Hazina:**
- `/code/` - Mifano ya kazi za kodi na utekelezaji wa sampuli
- `/md/` - Nyaraka za kina, mafunzo, na mwongozo wa jinsi ya kufanya
- `/translations/` - Tafsiri za lugha nyingi (lugha 50+ kupitia mtiririko otomatiki)
- `/.devcontainer/` - Usaidizi wa mazingira ya dev container (Python 3.12 na Ollama)

## Kuanzisha Mazingira ya Maendeleo

### Kutumia GitHub Codespaces au Dev Containers (Inapendekezwa)

1. Fungua katika GitHub Codespaces (haraka zaidi):
   - Bonyeza bendera ya "Open in GitHub Codespaces" katika README
   - Container hujiandaa kiotomatiki na Python 3.12 na Ollama na Phi-3

2. Fungua katika VS Code Dev Containers:
   - Tumia bendera ya "Open in Dev Containers" kutoka README
   - Container inahitaji angalau kumbukumbu ya mwenyeji 16GB

### Usanidi wa Kwenye Kompyuta Binafsi

**Mahitaji:**
- Python 3.12 au baadaye
- SDK ya .NET 8.0 (kwa mifano ya C#)
- Node.js 18+ na npm (kwa mifano ya JavaScript)
- Inashauriwa kumbukumbu ya angalau 16GB RAM

**Ufungaji:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Kwa Mifano ya Python:**
Nenda kwenye saraka za mifano maalum na usakinishe utegemezi:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # kama requirements.txt ipo
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
npm run dev  # Anzisha seva ya maendeleo
npm run build  # Tengeneza kwa ajili ya uzalishaji
```

## Mipangilio ya Hazina

### Mifano ya Kodi (`/code/`)

- **01.Introduce/** - Utangulizi wa msingi na mifano ya kuanza
- **03.Finetuning/** na **04.Finetuning/** - Mifano ya kufanyia marekebisho modeli kwa njia mbalimbali
- **03.Inference/** - Mifano ya kutabiri kwenye vifaa tofauti (AIPC, MLX)
- **06.E2E/** - Mifano ya matumizi ya mwisho-ku-mwisho
- **07.Lab/** - Utekelezaji wa maabara/majaribio
- **08.RAG/** - Mifano ya Uzalishaji Ulioongezwa kwa Ufanisi (RAG)
- **09.UpdateSamples/** - Sampuli za hivi karibuni zilizosasishwa

### Nyaraka (`/md/`)

- **01.Introduction/** - Mwongozo wa utangulizi, usanidi wa mazingira, mwongozo wa majukwaa
- **02.Application/** - Sampuli za matumizi zilizoandaliwa kwa aina (Maandishi, Kodi, Kuona, Sauti, n.k.)
- **02.QuickStart/** - Mwongozo wa kuanza haraka za Microsoft Foundry na GitHub Models
- **03.FineTuning/** - Nyaraka za kufanyia marekebisho na mafunzo
- **04.HOL/** - Maabara za vitendo (zinajumuisha mifano ya .NET)

### Aina za Faili

- **Notebooks za Jupyter (`.ipynb`)** - Mafunzo ya Python yenye mwingiliano yaliyoandikwa na 📓 katika README
- **Mafaili ya Python (`.py`)** - Mifano ya Python huru
- **Miradi ya C# (`.csproj`, `.sln`)** - Programu na mifano ya .NET
- **JavaScript (`.js`, `package.json`)** - Mifano ya wavuti na Node.js
- **Markdown (`.md`)** - Nyaraka na maelekezo

## Kufanya Kazi na Mifano

### Kuendesha Notebooks za Jupyter

Mifano mingi inatolewa kama notebooks za Jupyter:
```bash
pip install jupyter notebook
jupyter notebook  # Fungua kiolesura cha kivinjari
# Elekea faili la .ipynb unalotaka
```

### Kuendesha Skripti za Python

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

Au tengeneza suluhisho lote:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Kuendesha Mifano ya JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Maendeleo na upakiaji wa moto
```

## Upimaji

Hazina hii ina mifano ya kodi na mafunzo badala ya mradi wa kawaida wa programu wenye vipimo vya sehemu. Uthibitishaji kawaida hufanywa kwa:

1. **Kuendesha mifano** - Kila mfano unapaswa kuendesha bila makosa
2. **Kukagua matokeo** - Angalia majibu ya modeli yanavyofaa
3. **Kufuata mafunzo** - Mwongozo wa hatua kwa hatua unapaswa kufanya kazi kama ilivyoandikwa

**Njia ya kawaida ya uthibitishaji:**
- Kagua utekelezaji wa mifano katika mazingira lengwa
- Hakiki utegemezi umewekwa vizuri
- Angalia kupakuliwa/upakiaji wa modeli kufanyika kwa mafanikio
- Thibitisha tabia inayotegemewa inalingana na nyaraka

## Mtindo wa Kodi na Miongozo

### Miongozo ya Jumla

- Mifano inapaswa kuwa wazi, iliyoelezwa vizuri, na ya kielimu
- Fuata kanuni za lugha husika (PEP 8 kwa Python, viwango vya C# kwa .NET)
- Dumu na mifano inayolenga kuonyesha uwezo maalum wa modeli za Phi
- Jumuisha maelezo kuelezea dhana muhimu na vigezo maalum vya modeli

### Viwango vya Nyaraka

**Mwanzo wa URL:**
- Tumia muundo wa `[text](../../url)` bila nafasi za ziada
- Viungo vya jamaa: Tumia `./` kwa saraka ya sasa, `../` kwa saraka mama
- Epuka lugha maalum za nchi katika URL (kama `/en-us/`, `/en/`)

**Picha:**
- Weka picha zote katika saraka ya `/imgs/`
- Tumia majina yenye maelezo kwa herufi za Kiingereza, nambari, na dash
- Mfano: `phi-3-architecture.png`

**Faili za Markdown:**
- Rejelea mifano halisi ya kazi katika saraka ya `/code/`
- Dumu nyaraka zikilingana na mabadiliko ya kodi
- Tumia emoji ya 📓 kuashiria viungo vya notebooks za Jupyter katika README

### Muundo wa Faili

- Mifano ya kodi katika `/code/` imeandaliwa kwa mada/kipengele
- Nyaraka katika `/md/` zinaendana na muundo wa kodi inapowezekana
- Hifadhi faili zinazohusiana (notebooks, skripti, config) pamoja katika saraka ndogo

## Miongozo ya Ombi la Kuvuta (Pull Request)

### Kabla ya Kutuma

1. **Fanya fork ya hazina** kwa akaunti yako
2. **Toa PR tofauti kwa aina:**
   - Marekebisho ya hitilafu katika PR moja
   - Sasisho za nyaraka katika nyingine
   - Mifano mipya katika PR tofauti
   - Marekebisho ya tahajia yanaweza kutumwa pamoja

3. **Shughulikia migogoro ya mchanganyiko:**
   - Sasisha tawi lako la `main` kabla ya kufanya mabadiliko
   - Fanya upya maambukizi mara kwa mara

4. **PR za Tafsiri:**
   - Lazima zije na tafsiri za faili ZOTE katika folda
   - Dumisha muundo unaolingana na lugha ya awali

### Ukaguzi Unaohitajika

PR huendesha kiotomatiki mtiririko wa GitHub kuthibitisha:

1. **Uthibitishaji wa njia jamaa** - Viungo vyote vya ndani vinapaswa kufanya kazi
   - Jaribu viungo kwa ndani: Ctrl+Bonyeza katika VS Code
   - Tumia mapendekezo ya njia kutoka VS Code (`./` au `../`)

2. **Kukagua eneo la lugha la URL** - URL za wavuti hazipaswi kuwa na sehemu za nchi
   - Ondoa `/en-us/`, `/en/`, au msimbo mwingine wa lugha
   - Tumia URL za kimataifa zisizo maalum

3. **Kukagua URL zisizofanya kazi** - URL zote zipate hali ya 200
   - Hakiki viungo kuwa vinaweza kufikiwa kabla ya kutuma
   - Kumbuka: Kushindwa ni kwa sababu ya vizuizi vya mtandao vinaweza kutokea

### Muundo wa Kichwa cha PR

```
[component] Brief description
```

Mifano:
- `[docs] Ongeza mafunzo ya kutabiri kwa Phi-4`
- `[code] Rekebisha mfano wa kuunganisha ONNX Runtime`
- `[translation] Ongeza tafsiri ya Kijapani kwa mwongozo wa utangulizi`

## Mifumo ya Maendeleo ya Kawaida

### Kufanya Kazi na Modeli za Phi

**Kupakia Modeli:**
- Mifano hutumia mifumo mbalimbali: Transformers, ONNX Runtime, MLX, OpenVINO
- Modeli hupakuliwa kwa kawaida kutoka Hugging Face, Azure, au GitHub Models
- Angalia muafaka wa modeli na vifaa vyako (CPU, GPU, NPU)

**Mifumo ya Kutabiri:**
- Uundaji wa maandishi: Mifano mingi hutumia aina za chat/instruct
- Kuona: Phi-3-vision na Phi-4-multimodal kwa uelewa wa picha
- Sauti: Phi-4-multimodal inaunga mkono kiingilio cha sauti
- Kufikiri: Aina za Phi-4-reasoning kwa kazi za kufikiri za hali ya juu

### Vidokezo Maalum vya Jukwaa

**Microsoft Foundry:**
- Inahitaji usajili wa Azure na funguo za API
- Angalia `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Ngazi ya bure inapatikana kwa ajili ya majaribio
- Angalia `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Kutabiri Kwenye Kompyuta Binafsi:**
- ONNX Runtime: Utabiri wa kuvuka majukwaa, ulioboreshwa
- Ollama: Usimamizi rahisi wa modeli za ndani (imeandaliwa kabla ndani ya dev container)
- Apple MLX: Imeboreshwa kwa Apple Silicon

## Utatuzi wa Matatizo

### Masuala ya Kawaida

**Masuala ya Kumbukumbu:**
- Modeli za Phi zinahitaji kumbukumbu kubwa (hasa aina za kuona/multimodal)
- Tumia modeli zilizo na quantized kwa mazingira ya rasilimali chache
- Angalia `/md/01.Introduction/04/QuantifyingPhi.md`

**Migongano ya Utegemezi:**
- Mifano ya Python inaweza kuwa na mahitaji maalum ya toleo
- Tumia mazingira ya mtandao (virtual environments) kwa kila mfano
- Hakiki faili za `requirements.txt`

**Matatizo ya Kupakua Modeli:**
- Modeli kubwa zinaweza kuchukua muda mwingi kwenye muunganisho wenye mwendo polepole
- Fikiria kutumia mazingira ya wingu (Codespaces, Azure)
- Angalia cache ya Hugging Face: `~/.cache/huggingface/`

**Masuala ya Miradi ya .NET:**
- Hakikisha SDK ya .NET 8.0 imesakinishwa
- Tumia `dotnet restore` kabla ya kujenga
- Miradi baadhi ina usanidi maalum wa CUDA (Debug_Cuda)

**Mifano ya JavaScript/Web:**
- Tumia Node.js 18+ kwa mdundo
- Futa `node_modules` na sakinisha upya ikiwa matatizo yanaendelea
- Angalia koni ya kivinjari kwa matatizo ya WebGPU

### Kupata Msaada

- **Discord:** Jiunge na Microsoft Foundry Community Discord
- **Masuala ya GitHub:** Ripoti vidonda na matatizo katika hazina
- **Majadiliano ya GitHub:** Uliza maswali na shiriki maarifa

## Muktadha Zaidi

### AI Inayowajibika

Matumizi yote ya modeli za Phi yanapaswa kufuatilia kanuni za AI Inayowajibika za Microsoft:
- Usawa, kuaminika, usalama
- Faragha na usalama  
- Ushirikiano, uwazi, uwajibikaji
- Tumia Azure AI Content Safety kwa matumizi ya uzalishaji
- Angalia `/md/01.Introduction/01/01.AISafety.md`

### Tafsiri

- Lugha 50+ zinasaidiwa kupitia GitHub Action otomatiki
- Tafsiri zipo katika saraka ya `/translations/`
- Zinadumishwa na mtiririko wa co-op-translator
- Usihariri faili zilizotafsiriwa kwa mkono (zinatolewa moja kwa moja)

### Kuchangia

- Fuata miongozo katika `CONTRIBUTING.md`
- Kubali Mkataba wa Leseni ya Mchangiaji (CLA)
- Fuata Kanuni za Maadili za Microsoft Open Source
- Hifadhi usalama na siri nje ya michango

### Msaada wa Lugha Mbalimbali

Hii ni hazina ya lugha nyingi yenye mifano katika:
- **Python** - mtiririko wa ML/AI, notebooks za Jupyter, marekebisho modeli
- **C#/.NET** - programu za biashara, kuunganishwa na ONNX Runtime
- **JavaScript** - AI ya wavuti, kutabiri kwenye kivinjari kwa WebGPU

Chagua lugha inayofaa zaidi kwa matumizi yako na lengo la uwasilishaji.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiasi cha majina**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Wakati tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za mashine zinaweza kuwa na makosa au kasoro. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo chenye mamlaka. Kwa habari muhimu, tafsiri ya mtaalamu binadamu inashauriwa. Hatubeba dhamana kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->