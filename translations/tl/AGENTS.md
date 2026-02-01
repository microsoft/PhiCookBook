# AGENTS.md

## Pangkalahatang-ideya ng Proyekto

Ang PhiCookBook ay isang komprehensibong repository ng cookbook na naglalaman ng mga praktikal na halimbawa, tutorial, at dokumentasyon para sa paggamit ng Phi family ng Small Language Models (SLMs) ng Microsoft. Ipinapakita ng repository ang iba't ibang mga kaso ng paggamit kabilang ang inference, fine-tuning, quantization, mga implementasyon ng RAG, at multimodal na aplikasyon sa iba't ibang platform at framework.

**Pangunahing Teknolohiya:**
- **Mga Wika:** Python, C#/.NET, JavaScript/Node.js
- **Mga Framework:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Mga Platform:** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **Mga Uri ng Modelo:** Phi-3, Phi-3.5, Phi-4 (text, vision, multimodal, reasoning variants)

**Struktura ng Repository:**
- `/code/` - Mga gumaganang halimbawa ng code at sample na implementasyon
- `/md/` - Detalyadong dokumentasyon, mga tutorial, at mga gabay  
- `/translations/` - Mga pagsasalin sa iba't ibang wika (50+ wika sa pamamagitan ng automated workflow)
- `/.devcontainer/` - Konfigurasyon ng dev container (Python 3.12 gamit ang Ollama)

## Pag-set up ng Kapaligiran ng Pag-develop

### Paggamit ng GitHub Codespaces o Dev Containers (Inirerekomenda)

1. Buksan sa GitHub Codespaces (pinakamabilis):
   - I-click ang "Open in GitHub Codespaces" badge sa README
   - Ang container ay awtomatikong naka-configure gamit ang Python 3.12 at Ollama na may Phi-3

2. Buksan sa VS Code Dev Containers:
   - Gamitin ang "Open in Dev Containers" badge mula sa README
   - Ang container ay nangangailangan ng minimum na 16GB host memory

### Lokal na Pag-set up

**Mga Kinakailangan:**
- Python 3.12 o mas bago
- .NET 8.0 SDK (para sa mga halimbawa ng C#)
- Node.js 18+ at npm (para sa mga halimbawa ng JavaScript)
- Inirerekomendang minimum na 16GB RAM

**Pag-install:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Para sa mga Halimbawa ng Python:**
Pumunta sa mga partikular na direktoryo ng halimbawa at i-install ang mga dependencies:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**Para sa mga Halimbawa ng .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Para sa mga Halimbawa ng JavaScript/Web:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```

## Organisasyon ng Repository

### Mga Halimbawa ng Code (`/code/`)

- **01.Introduce/** - Mga pangunahing pagpapakilala at mga sample para sa pagsisimula
- **03.Finetuning/** at **04.Finetuning/** - Mga halimbawa ng fine-tuning gamit ang iba't ibang mga pamamaraan
- **03.Inference/** - Mga halimbawa ng inference sa iba't ibang hardware (AIPC, MLX)
- **06.E2E/** - Mga sample ng end-to-end na aplikasyon
- **07.Lab/** - Mga laboratoryo/eksperimental na implementasyon
- **08.RAG/** - Mga sample ng Retrieval-Augmented Generation
- **09.UpdateSamples/** - Pinakabagong mga updated na sample

### Dokumentasyon (`/md/`)

- **01.Introduction/** - Mga gabay sa pagpapakilala, pag-set up ng kapaligiran, mga gabay sa platform
- **02.Application/** - Mga sample ng aplikasyon na inayos ayon sa uri (Text, Code, Vision, Audio, atbp.)
- **02.QuickStart/** - Mga gabay sa mabilisang pagsisimula para sa Azure AI Foundry at GitHub Models
- **03.FineTuning/** - Dokumentasyon at mga tutorial sa fine-tuning
- **04.HOL/** - Mga hands-on na laboratoryo (kasama ang mga halimbawa ng .NET)

### Mga Format ng File

- **Jupyter Notebooks (`.ipynb`)** - Mga interactive na tutorial sa Python na may markang 📓 sa README
- **Python Scripts (`.py`)** - Mga standalone na halimbawa ng Python
- **C# Projects (`.csproj`, `.sln`)** - Mga aplikasyon at sample ng .NET
- **JavaScript (`.js`, `package.json`)** - Mga web-based at Node.js na halimbawa
- **Markdown (`.md`)** - Dokumentasyon at mga gabay

## Paggamit ng Mga Halimbawa

### Pagpapatakbo ng Jupyter Notebooks

Karamihan sa mga halimbawa ay ibinibigay bilang Jupyter notebooks:
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### Pagpapatakbo ng Python Scripts

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Pagpapatakbo ng Mga Halimbawa ng .NET

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

O buuin ang buong solusyon:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Pagpapatakbo ng Mga Halimbawa ng JavaScript/Web

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```

## Pagsusuri

Ang repository na ito ay naglalaman ng mga halimbawa ng code at mga tutorial sa halip na isang tradisyunal na proyekto ng software na may mga unit test. Ang pagsusuri ay karaniwang ginagawa sa pamamagitan ng:

1. **Pagpapatakbo ng mga halimbawa** - Ang bawat halimbawa ay dapat tumakbo nang walang error
2. **Pag-verify ng mga output** - Suriin na ang mga tugon ng modelo ay naaangkop
3. **Pagsunod sa mga tutorial** - Ang mga step-through na gabay ay dapat gumana ayon sa dokumentasyon

**Karaniwang paraan ng pagsusuri:**
- Subukan ang pagpapatakbo ng halimbawa sa target na kapaligiran
- I-verify na tama ang pag-install ng mga dependencies
- Suriin na matagumpay na na-download/naload ang modelo
- Kumpirmahin na ang inaasahang pag-uugali ay tumutugma sa dokumentasyon

## Estilo ng Code at Mga Kombensyon

### Pangkalahatang Gabay

- Ang mga halimbawa ay dapat malinaw, may tamang mga komento, at pang-edukasyon
- Sundin ang mga kombensyon ng wika (PEP 8 para sa Python, mga pamantayan ng C# para sa .NET)
- Panatilihing nakatuon ang mga halimbawa sa pagpapakita ng mga partikular na kakayahan ng Phi model
- Isama ang mga komento na nagpapaliwanag ng mga pangunahing konsepto at mga parameter ng modelo

### Mga Pamantayan sa Dokumentasyon

**Pag-format ng URL:**
- Gumamit ng format na `[text](../../url)` nang walang sobrang espasyo
- Mga relative na link: Gumamit ng `./` para sa kasalukuyang direktoryo, `../` para sa magulang
- Walang mga country-specific na locale sa mga URL (iwasan ang `/en-us/`, `/en/`)

**Mga Imahe:**
- Iimbak ang lahat ng mga imahe sa direktoryo ng `/imgs/`
- Gumamit ng mga deskriptibong pangalan na may mga English na karakter, numero, at mga dash
- Halimbawa: `phi-3-architecture.png`

**Mga Markdown File:**
- Sumangguni sa mga aktwal na gumaganang halimbawa sa direktoryo ng `/code/`
- Panatilihing naka-synchronize ang dokumentasyon sa mga pagbabago sa code
- Gumamit ng 📓 emoji para markahan ang mga link ng Jupyter notebook sa README

### Organisasyon ng File

- Mga halimbawa ng code sa `/code/` na inayos ayon sa paksa/tampok
- Dokumentasyon sa `/md/` na sumasalamin sa istruktura ng code kung naaangkop
- Panatilihing magkakasama ang mga kaugnay na file (notebooks, scripts, configs) sa mga subdirectory

## Mga Alituntunin sa Pull Request

### Bago Mag-submit

1. **I-fork ang repository** sa iyong account
2. **Paghiwalayin ang mga PR ayon sa uri:**
   - Mga pag-aayos ng bug sa isang PR
   - Mga update sa dokumentasyon sa isa pa
   - Mga bagong halimbawa sa hiwalay na PR
   - Ang mga pag-aayos ng typo ay maaaring pagsamahin

3. **Pamahalaan ang mga conflict sa merge:**
   - I-update ang iyong lokal na `main` branch bago gumawa ng mga pagbabago
   - I-sync sa upstream nang madalas

4. **Mga PR sa Pagsasalin:**
   - Dapat isama ang mga pagsasalin para sa LAHAT ng mga file sa folder
   - Panatilihin ang pare-parehong istruktura sa orihinal na wika

### Mga Kinakailangang Pagsusuri

Ang mga PR ay awtomatikong nagpapatakbo ng mga workflow ng GitHub upang i-validate:

1. **Pag-validate ng relative path** - Lahat ng internal na link ay dapat gumana
   - Subukan ang mga link nang lokal: Ctrl+Click sa VS Code
   - Gumamit ng mga mungkahi sa path mula sa VS Code (`./` o `../`)

2. **Pag-check ng URL locale** - Ang mga web URL ay hindi dapat maglaman ng mga country locale
   - Alisin ang `/en-us/`, `/en/`, o iba pang mga code ng wika
   - Gumamit ng generic na international URLs

3. **Pag-check ng sirang URL** - Lahat ng URL ay dapat magbalik ng 200 status
   - I-verify na maa-access ang mga link bago mag-submit
   - Tandaan: Ang ilang mga pagkabigo ay maaaring dahil sa mga limitasyon sa network

### Format ng PR Title

```
[component] Brief description
```

Mga Halimbawa:
- `[docs] Magdagdag ng Phi-4 inference tutorial`
- `[code] Ayusin ang halimbawa ng ONNX Runtime integration`
- `[translation] Magdagdag ng pagsasalin sa Japanese para sa mga gabay sa pagpapakilala`

## Karaniwang Mga Pattern ng Pag-develop

### Paggamit ng Mga Phi Model

**Pag-load ng Modelo:**
- Ang mga halimbawa ay gumagamit ng iba't ibang mga framework: Transformers, ONNX Runtime, MLX, OpenVINO
- Ang mga modelo ay karaniwang dina-download mula sa Hugging Face, Azure, o GitHub Models
- Suriin ang compatibility ng modelo sa iyong hardware (CPU, GPU, NPU)

**Mga Pattern ng Inference:**
- Text generation: Karamihan sa mga halimbawa ay gumagamit ng chat/instruct variants
- Vision: Phi-3-vision at Phi-4-multimodal para sa pag-unawa sa imahe
- Audio: Sinusuportahan ng Phi-4-multimodal ang mga audio input
- Reasoning: Phi-4-reasoning variants para sa advanced na mga reasoning task

### Mga Tala para sa Partikular na Platform

**Azure AI Foundry:**
- Nangangailangan ng subscription sa Azure at mga API key
- Tingnan ang `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- May libreng tier para sa pagsubok
- Tingnan ang `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Lokal na Inference:**
- ONNX Runtime: Cross-platform, optimized inference
- Ollama: Madaling lokal na pamamahala ng modelo (pre-configured sa dev container)
- Apple MLX: Na-optimize para sa Apple Silicon

## Pag-troubleshoot

### Karaniwang Mga Isyu

**Mga Isyu sa Memory:**
- Ang mga Phi model ay nangangailangan ng malaking RAM (lalo na ang vision/multimodal variants)
- Gumamit ng mga quantized na modelo para sa mga kapaligirang may limitadong resources
- Tingnan ang `/md/01.Introduction/04/QuantifyingPhi.md`

**Mga Conflict sa Dependency:**
- Ang mga halimbawa ng Python ay maaaring may partikular na mga kinakailangan sa bersyon
- Gumamit ng virtual environments para sa bawat halimbawa
- Suriin ang mga indibidwal na `requirements.txt` file

**Pagkabigo sa Pag-download ng Modelo:**
- Ang malalaking modelo ay maaaring mag-timeout sa mabagal na koneksyon
- Isaalang-alang ang paggamit ng cloud environments (Codespaces, Azure)
- Suriin ang Hugging Face cache: `~/.cache/huggingface/`

**Mga Isyu sa Proyekto ng .NET:**
- Siguraduhing naka-install ang .NET 8.0 SDK
- Gumamit ng `dotnet restore` bago mag-build
- Ang ilang mga proyekto ay may CUDA-specific na mga konfigurasyon (Debug_Cuda)

**Mga Halimbawa ng JavaScript/Web:**
- Gumamit ng Node.js 18+ para sa compatibility
- I-clear ang `node_modules` at muling i-install kung may mga isyu
- Suriin ang browser console para sa mga isyu sa WebGPU compatibility

### Pagkuha ng Tulong

- **Discord:** Sumali sa Azure AI Foundry Community Discord
- **GitHub Issues:** Mag-report ng mga bug at isyu sa repository
- **GitHub Discussions:** Magtanong at magbahagi ng kaalaman

## Karagdagang Konteksto

### Responsible AI

Ang lahat ng paggamit ng Phi model ay dapat sumunod sa mga prinsipyo ng Responsible AI ng Microsoft:
- Pagiging patas, pagiging maaasahan, kaligtasan
- Privacy at seguridad  
- Inclusiveness, transparency, accountability
- Gumamit ng Azure AI Content Safety para sa mga production application
- Tingnan ang `/md/01.Introduction/01/01.AISafety.md`

### Mga Pagsasalin

- Sinusuportahan ang 50+ wika sa pamamagitan ng automated na GitHub Action
- Mga pagsasalin sa direktoryo ng `/translations/`
- Pinapanatili ng co-op-translator workflow
- Huwag manu-manong i-edit ang mga file na isinalin (auto-generated)

### Pag-aambag

- Sundin ang mga alituntunin sa `CONTRIBUTING.md`
- Sumang-ayon sa Contributor License Agreement (CLA)
- Sumunod sa Microsoft Open Source Code of Conduct
- Panatilihing ligtas ang seguridad at mga kredensyal sa mga commit

### Suporta sa Multi-Language

Ito ay isang polyglot na repository na may mga halimbawa sa:
- **Python** - Mga workflow ng ML/AI, Jupyter notebooks, fine-tuning
- **C#/.NET** - Mga aplikasyon ng enterprise, ONNX Runtime integration
- **JavaScript** - Web-based na AI, inference sa browser gamit ang WebGPU

Piliin ang wika na pinakamahusay na angkop sa iyong kaso ng paggamit at target na deployment.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.