# AGENTS.md

## Project Overview

Ang PhiCookBook ay isang komprehensibong repositoryo ng cookbook na naglalaman ng mga praktikal na halimbawa, tutorial, at dokumentasyon para sa paggamit ng pamilya ng Small Language Models (SLMs) ng Microsoft na Phi. Ipinapakita ng repositoryo ang iba't ibang mga kaso ng paggamit kabilang ang inference, fine-tuning, quantization, RAG implementations, at multimodal na aplikasyon sa iba't ibang mga platform at framework.

**Pangunahing Teknolohiya:**
- **Mga Wika:** Python, C#/.NET, JavaScript/Node.js
- **Mga Framework:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Mga Platform:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Mga Uri ng Modelo:** Phi-3, Phi-3.5, Phi-4 (text, vision, multimodal, reasoning variants)

**Estruktura ng Repositoryo:**
- `/code/` - Mga gumaganang halimbawa ng code at implementasyon ng sample
- `/md/` - Detalyadong dokumentasyon, tutorial, at mga gabay kung paano  
- `/translations/` - Mga pagsasalin sa iba't ibang wika (50+ na wika sa pamamagitan ng automated workflow)
- `/.devcontainer/` - Configuration ng dev container (Python 3.12 na may Ollama)

## Development Environment Setup

### Paggamit ng GitHub Codespaces o Dev Containers (Inirerekomenda)

1. Buksan sa GitHub Codespaces (pinakamabilis):
   - I-click ang "Open in GitHub Codespaces" na badge sa README
   - Awtomatikong nako-configure ang container na may Python 3.12 at Ollama kasama ang Phi-3

2. Buksan sa VS Code Dev Containers:
   - Gamitin ang "Open in Dev Containers" na badge mula sa README
   - Nangangailangan ang container ng minimum na 16GB host memory

### Lokal na Setup

**Mga Kinakailangan:**
- Python 3.12 o mas bago
- .NET 8.0 SDK (para sa mga C# na halimbawa)
- Node.js 18+ at npm (para sa mga JavaScript na halimbawa)
- 16GB RAM minimum na inirerekomenda

**Pag-install:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Para sa mga Halimbawa gamit ang Python:**
Pumunta sa mga partikular na directory ng halimbawa at i-install ang mga dependencies:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # kung umiiral ang requirements.txt
```

**Para sa mga Halimbawa gamit ang .NET:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**Para sa mga Halimbawa gamit ang JavaScript/Web:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Simulan ang development server
npm run build  # Gumawa para sa produksyon
```

## Organisasyon ng Repositoryo

### Mga Halimbawa ng Code (`/code/`)

- **01.Introduce/** - Mga pangunahing pagpapakilala at mga sample para sa pagsisimula
- **03.Finetuning/** at **04.Finetuning/** - Mga halimbawa ng fine-tuning gamit ang iba't ibang pamamaraan
- **03.Inference/** - Mga halimbawa ng inference sa iba't ibang hardware (AIPC, MLX)
- **06.E2E/** - Mga halimbawa ng end-to-end na aplikasyon
- **07.Lab/** - Laboratoryo/eksperimentong implementasyon
- **08.RAG/** - Mga halimbawa ng Retrieval-Augmented Generation
- **09.UpdateSamples/** - Pinakabagong mga na-update na sample

### Dokumentasyon (`/md/`)

- **01.Introduction/** - Mga gabay sa pagpapakilala, setup ng environment, mga gabay para sa platform
- **02.Application/** - Mga halimbawa ng aplikasyon na nakaayos ayon sa uri (Text, Code, Vision, Audio, atbp.)
- **02.QuickStart/** - Mga mabilisang gabay para sa Microsoft Foundry at GitHub Models
- **03.FineTuning/** - Dokumentasyon at tutorial sa fine-tuning
- **04.HOL/** - Hands-on labs (kabilang ang mga halimbawa ng .NET)

### Uri ng File

- **Jupyter Notebooks (`.ipynb`)** - Interaktibong Python tutorial na may markang 📓 sa README
- **Python Scripts (`.py`)** - Mga standalone Python example
- **C# Projects (`.csproj`, `.sln`)** - Mga aplikasyon at sample sa .NET
- **JavaScript (`.js`, `package.json`)** - Mga halimbawa para sa web at Node.js
- **Markdown (`.md`)** - Dokumentasyon at mga gabay

## Paggamit ng mga Halimbawa

### Pagpapatakbo ng Jupyter Notebooks

Karamihan sa mga halimbawa ay ibinibigay bilang mga Jupyter notebook:
```bash
pip install jupyter notebook
jupyter notebook  # Binubuksan ang interface ng browser
# Mag-navigate sa nais na .ipynb na file
```

### Pagpapatakbo ng Python Scripts

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Pagpapatakbo ng .NET na Halimbawa

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

O buuin ang buong solusyon:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Pagpapatakbo ng JavaScript/Web na Halimbawa

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Pag-unlad na may mainit na pag-reload
```

## Pagsubok

Ang repositoryong ito ay naglalaman ng halimbawa ng code at mga tutorial sa halip na tradisyunal na software project na may unit tests. Karaniwang ginagawang validasyon ang:

1. **Pagpapatakbo ng mga halimbawa** - Dapat tumakbo ang bawat halimbawa nang walang error
2. **Pag-verify ng output** - Suriin na ang mga sagot ng modelo ay angkop
3. **Pagsunod sa mga tutorial** - Ang mga step-through na gabay ay dapat gumana ayon sa dokumentasyon

**Karaniwang paraan ng validasyon:**
- Subukang patakbuhin ang halimbawa sa target na environment
- I-verify ang tamang pag-install ng mga dependencies
- Siguraduhing matagumpay ang pag-download/pag-load ng modelo
- Kumpirmahin na ang inaasahang pag-uugali ay tugma sa dokumentasyon

## Estilo ng Code at mga Konbensiyon

### Pangkalahatang Gabay

- Dapat malinaw, mahusay ang komentaryo, at pang-edukasyon ang mga halimbawa
- Sumunod sa mga konbensiyon ng partikular na wika (PEP 8 para sa Python, C# standards para sa .NET)
- Panatilihin ang mga halimbawa na nakatutok sa pagpapakita ng mga tiyak na kakayahan ng Phi models
- Maglagay ng mga komentaryo na nagpapaliwanag ng mga pangunahing konsepto at partikular na mga parameter ng modelo

### Mga Pamantayan sa Dokumentasyon

**Pag-format ng URL:**
- Gumamit ng format na `[text](../../url)` nang walang dagdag na espasyo
- Mga relative link: Gumamit ng `./` para sa kasalukuyang direktoryo, `../` para sa parent
- Iwasan ang mga bansa-specific na locale sa mga URL (iwasan ang `/en-us/`, `/en/`)

**Mga Larawan:**
- Itago lahat ng mga larawan sa direktoryo na `/imgs/`
- Gumamit ng mga deskriptibong pangalan na may mga English na karakter, numero, at gitling
- Halimbawa: `phi-3-architecture.png`

**Markdown Files:**
- Itukoy ang mga tunay na gumaganang halimbawa sa direktoryo ng `/code/`
- Panatilihing naka-sync ang dokumentasyon sa mga pagbabago sa code
- Gumamit ng 📓 emoji upang markahan ang mga link ng Jupyter notebook sa README

### Organisasyon ng File

- Code examples sa `/code/` na nakaayos ayon sa paksa/katangian
- Dokumentasyon sa `/md/` na sumasalamin sa estruktura ng code kung naaangkop
- Panatilihin ang mga kaugnay na file (notebook, script, config) magkasama sa mga subdirectory

## Patnubay sa Pull Requests

### Bago Mag-submit

1. **I-fork ang repositoryo** sa iyong account
2. **Ihiwalay ang mga PR ayon sa uri:**
   - Mga bug fix sa isang PR
   - Mga update sa dokumentasyon sa isa pa
   - Mga bagong halimbawa sa magkahiwalay na PR
   - Ang mga typo fix ay maaaring pagsamahin

3. **Pagharap sa mga merge conflict:**
   - I-update ang lokal na `main` branch bago gumawa ng mga pagbabago
   - Regular na i-sync sa upstream

4. **Mga Translation PR:**
   - Dapat magsama ng mga pagsasalin para sa LAHAT ng mga file sa folder
   - Panatilihin ang pare-parehong estruktura ng orihinal na wika

### Mga Kailangang Check

Awtomatikong pinapatakbo ng GitHub workflows ang mga PR upang i-validate:

1. **Validasyon sa relative path** - Lahat ng internal links ay dapat gumana
   - Subukang i-test ang mga link locally: Ctrl+Click sa VS Code
   - Gumamit ng mga suhestiyon ng path mula sa VS Code (`./` o `../`)

2. **Pagsusuri sa URL locale** - Hindi dapat naglalaman ng country locale ang mga URL ng web
   - Alisin ang `/en-us/`, `/en/`, o iba pang language code
   - Gumamit ng pangkalahatang international na URLs

3. **Pagsusuri ng broken URL** - Ang lahat ng URL ay dapat magbalik ng 200 status
   - Siguraduhing accessible ang mga link bago magsubmit
   - Tandaan: Maaaring ang ilang pagkabigo ay dahil sa mga network restriction

### Format ng Pamagat ng PR

```
[component] Brief description
```

Mga Halimbawa:
- `[docs] Add Phi-4 inference tutorial`
- `[code] Fix ONNX Runtime integration example`
- `[translation] Add Japanese translation for intro guides`

## Mga Karaniwang Pattern sa Development

### Paggamit ng Phi Models

**Pag-load ng Modelo:**
- Gumagamit ang mga halimbawa ng iba't ibang framework: Transformers, ONNX Runtime, MLX, OpenVINO
- Kadalasang dinadownload ang mga modelo mula sa Hugging Face, Azure, o GitHub Models
- Suriin ang kompatibilidad ng modelo sa iyong hardware (CPU, GPU, NPU)

**Mga Pattern sa Inference:**
- Text generation: Karamihan sa mga halimbawa ay gumagamit ng chat/instruct variants
- Vision: Phi-3-vision at Phi-4-multimodal para sa pag-unawa ng imahe
- Audio: Sinusuportahan ng Phi-4-multimodal ang mga audio inputs
- Reasoning: Phi-4-reasoning variants para sa advanced na mga gawain sa pangangatwiran

### Mga Tala na Tungo sa Platform

**Microsoft Foundry:**
- Nangangailangan ng Azure subscription at API keys
- Tingnan ang `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- May libreng tier para sa testing
- Tingnan ang `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Local Inference:**
- ONNX Runtime: Cross-platform, optimized inference
- Ollama: Madaling local na pamamahala ng modelo (pre-configured sa dev container)
- Apple MLX: Optimized para sa Apple Silicon

## Pag-aayos ng Problema

### Karaniwang Isyu

**Problema sa Memorya:**
- Nangangailangan ng malaking RAM ang Phi models (lalo na ang vision/multimodal variants)
- Gumamit ng quantized models para sa mga environment na may limitadong resources
- Tingnan ang `/md/01.Introduction/04/QuantifyingPhi.md`

**Mga Conflict sa Dependency:**
- Maaaring may partikular na bersyon ang kinakailangan sa mga halimbawa ng Python
- Gumamit ng virtual environments para sa bawat halimbawa
- Suriin ang mga `requirements.txt` na file ng indibidwal

**Pagkabigo sa Pag-download ng Modelo:**
- Maaaring ma-timeout ang malaking modelo sa mabagal na koneksyon
- Isaalang-alang ang paggamit ng cloud environment (Codespaces, Azure)
- Suriin ang Hugging Face cache: `~/.cache/huggingface/`

**Mga Isyu sa .NET Project:**
- Siguraduhing naka-install ang .NET 8.0 SDK
- Gamitin ang `dotnet restore` bago mag-build
- Ang ilang proyekto ay may CUDA-specific na configuration (Debug_Cuda)

**Mga Halimbawa ng JavaScript/Web:**
- Gumamit ng Node.js 18+ para sa compatibility
- Linisin ang `node_modules` at i-reinstall kung may problema
- Suriin ang console ng browser para sa mga isyu sa WebGPU compatibility

### Paghahanap ng Tulong

- **Discord:** Sumali sa Microsoft Foundry Community Discord
- **GitHub Issues:** I-report ang mga bug at isyu sa repositoryo
- **GitHub Discussions:** Magtanong at magbahagi ng kaalaman

## Karagdagang Konteksto

### Responsableng AI

Dapat sundin ang lahat ng paggamit ng Phi model ang mga prinsipyo ng Responsible AI ng Microsoft:
- Katarungan, pagiging maaasahan, kaligtasan
- Privacy at seguridad  
- Inclusiveness, transparency, pananagutan
- Gumamit ng Azure AI Content Safety para sa mga production na aplikasyon
- Tingnan ang `/md/01.Introduction/01/01.AISafety.md`

### Mga Pagsasalin

- Suportado ang 50+ na wika sa pamamagitan ng automated GitHub Action
- Mga pagsasalin nasa direktoryo na `/translations/`
- Pinamamahalaan ng co-op-translator workflow
- Huwag mano-manong baguhin ang mga isinalin na file (auto-generated)

### Pagsisidlan

- Sundin ang mga gabay sa `CONTRIBUTING.md`
- Sumang-ayon sa Contributor License Agreement (CLA)
- Sundin ang Microsoft Open Source Code of Conduct
- Panatilihin malayo sa commits ang seguridad at mga kredensyal

### Multi-Language Support

Ito ay isang polyglot repositoryo na may mga halimbawa sa:
- **Python** - ML/AI workflows, Jupyter notebooks, fine-tuning
- **C#/.NET** - Enterprise na aplikasyon, ONNX Runtime integration
- **JavaScript** - Web-based AI, browser inference gamit ang WebGPU

Pumili ng wikang pinakaangkop sa iyong kaso ng paggamit at target na deployment.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagsasabi ng Paunawa**:  
Ang dokumentong ito ay naisalin gamit ang serbisyo ng AI na pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tiyak na impormasyon. Ang orihinal na dokumento sa katutubong wika nito ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmana mula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->