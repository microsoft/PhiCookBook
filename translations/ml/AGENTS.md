# AGENTS.md

## Project Overview

PhiCookBook Microsoft-ന്റെ Phi കുടുംബം സാമ്പത്തികമായി ചെറിയ ഭാഷാ മോഡലുകളുമായി (SLMs) ജോലി ചെയ്യുന്നതിന് കൈകൊള്ളാനുള്ള ഉദാഹരണങ്ങൾ, ട്യൂട്ടോറിയലുകൾ, ഡോക്യുമെന്റേഷൻ എന്നിവ അടങ്ങിയ ഒരു സമഗ്രമായ കുക്ക്ബുക്ക് റിപോസിറ്ററിയാണ്. റിപോസിറ്ററി ഇൻഫറൻസ്, ഫൈൻ-ട്യുണിംഗ്, ക്വാണ്ടൈസേഷൻ, RAG നടപ്പാക്കലുകൾ, മൾട്ടിമോഡൽ അപേക്ഷകൾ തുടങ്ങിയ വിവിധ ഉപയോഗ കേസുകൾ വിവിധ പ്ലാറ്റ്ഫോമുകളിലും ഫ്രെയിംവർക്കുകളിലുമായി പ്രദർശിപ്പിക്കുന്നു.

**Key Technologies:**
- **Languages:** Python, C#/.NET, JavaScript/Node.js
- **Frameworks:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platforms:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Model Types:** Phi-3, Phi-3.5, Phi-4 (text, vision, multimodal, reasoning variants)

**Repository Structure:**
- `/code/` - പ്രവർത്തനക്ഷമമായ കോഡ് ഉദാഹരണങ്ങളും സാമ്പിൾ നടപ്പിലാക്കലുകളും
- `/md/` - വിശദമായ ഡോക്യുമെന്റേഷൻ, ട്യൂട്ടോറിയൽകൾ, ശ്രമശീല മാർഗ്ഗദർശനങ്ങൾ  
- `/translations/` - സ്വയംപ്രവർത്തനപ്പെടുന്ന പ്രവൃത്തി പ്രവൃത്തിയിലൂടെ ബഹുഭാഷാ പരിഭാഷകൾ (50+ ഭാഷകൾ)
- `/.devcontainer/` - ഡെവ് കണ്ടെയ്‌നർ കോൺഫിഗർ (Python 3.12 Ollama-വോടെ)

## Development Environment Setup

### Using GitHub Codespaces or Dev Containers (Recommended)

1. Open in GitHub Codespaces (fastest):
   - README-ൽ ഉള്ള "Open in GitHub Codespaces" ബാഡ്ജിൽ ക്ലിക്കുചെയ്യുക
   - കണ്ടെയ്‌നറിന് Python 3.12 ಮತ್ತು Phi-3 ഉള്ള Ollama മുൻകൂട്ടി കോൺഫിഗർ ചെയ്യുന്നു

2. Open in VS Code Dev Containers:
   - README-ൽ നിന്ന് "Open in Dev Containers" ബാഡ്ജ് ഉപയോഗിക്കുക
   - കണ്ടെയ്‌നറിന് കുറഞ്ഞത് 16GB ഹോസ്റ്റ് മെമ്മറി ആവശ്യമുണ്ട്

### Local Setup

**Prerequisites:**
- Python 3.12 അല്ലെങ്കിൽ പിന്നീട് വന്നത്
- .NET 8.0 SDK (C# ഉദാഹരണങ്ങള്ക്ക്)
- Node.js 18+ and npm (JavaScript ഉദാഹരണങ്ങള്ക്ക്)
- കുറഞ്ഞത് 16GB RAM ശുപാർശ ചെയ്യുന്നു

**Installation:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**For Python Examples:**
നിർദ്ദിഷ്ട ഉദാഹരണ ഡയറക്ടറികളിലേക്ക് പോകുകയും ആവശ്യമായ ഡിപ്പൻഡൻസികൾ ഇൻസ്റ്റാൾ ചെയ്യുകയും ചെയ്യുക:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # requirements.txt ഉണ്ടെങ്കിൽ
```

**For .NET Examples:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**For JavaScript/Web Examples:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # വികസന സെർവർ ആരംഭിക്കുക
npm run build  # ഉൽപ്പാദനത്തിനായി നിർമ്മിക്കുക
```

## Repository Organization

### Code Examples (`/code/`)

- **01.Introduce/** - അടിസ്ഥാന പരിചയപ്പെടുത്തലുകളും തുടക്കം കുറിക്കുന്ന സാമ്പിളുകളും
- **03.Finetuning/** and **04.Finetuning/** - വിവിധ രീതികളിലുള്ള ഫൈൻ-ട്യുണിംഗ് ഉദാഹരണങ്ങൾ
- **03.Inference/** - വിവിധ ഹാർഡ്‌വെയറുകളിലെ (AIPC, MLX) ഇൻഫറൻസ് ഉദാഹരണങ്ങൾ
- **06.E2E/** - end-to-end ആപ്ലിക്കേഷൻ സാമ്പിളുകൾ
- **07.Lab/** - ലാബോറട്ടറി/പ്രയോഗപരമായ നടപ്പിലാക്കലുകൾ
- **08.RAG/** - Retrieval-Augmented Generation സാമ്പിളുകൾ
- **09.UpdateSamples/** - ഏറ്റവും പുതിയ അപ്‌ഡേറ്റുകൾ ഉള്ള സാമ്പിളുകൾ

### Documentation (`/md/`)

- **01.Introduction/** - പരിചയ ഗൈഡുകൾ, എന്വയോൺമെന്റ് സെറ്റ്‌അപ്പ്, പ്ലാറ്റ്ഫോം ഗൈഡുകൾ
- **02.Application/** - വാചക, കോഡ്, ദൃശ്യ, ഓഡിയോ തുടങ്ങിയ തരങ്ങളിൽ തെരഞ്ഞെടുത്ത ആപ്ലിക്കേഷൻ സാമ്പിളുകൾ
- **02.QuickStart/** - Microsoft Foundry and GitHub Models-ക്കുള്ള ക്വിക് സ്റ്റാർട്ട് ഗൈഡുകൾ
- **03.FineTuning/** - ഫൈൻ-ട്യുണിംഗ് ഡോക്യുമെന്റേഷൻ এবং ട്യൂട്ടോറിയലുകൾ
- **04.HOL/** - ഹാൻഡ്സ്-ഓൺ ലാബുകൾ (.NET ഉദാഹരണങ്ങൾ ഉൾപ്പെടുന്നു)

### File Formats

- **Jupyter Notebooks (`.ipynb`)** - README-ൽ 📓 ചിഹ്നം ഉള്ള ഇന്ററാക്ടീവ് Python ട്യൂട്ടോറിയലുകൾ
- **Python Scripts (`.py`)** - ഒറ്റക്കേ ഓടി പ്രവർത്തിക്കുന്ന Python ഉദാഹരണങ്ങൾ
- **C# Projects (`.csproj`, `.sln`)** - .NET ആപ്ലിക്കേഷനുകളും സാമ്പിളുകളും
- **JavaScript (`.js`, `package.json`)** - വെബ് അടിസ്ഥാനമാക്കിയുള്ളവും Node.js ഉദാഹരണങ്ങളും
- **Markdown (`.md`)** - ഡോക്യുമെന്റേഷൻയും ഗൈഡുകളും

## Working with Examples

### Running Jupyter Notebooks

മൊതമുകളായ ഉദാഹരണങ്ങൾ Jupyter നോട്ട്ബുക്കുകളായി നൽകപ്പെട്ടിരിക്കുന്നു:
```bash
pip install jupyter notebook
jupyter notebook  # ബ്രൗസർ ഇന്റർഫേസ് തുറക്കുന്നു
# ആവശ്യമായ .ipynb ഫയലിലേക്ക് നാവിഗേറ്റ് ചെയ്യുക
```

### Running Python Scripts

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### Running .NET Examples

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

Or build entire solution:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Running JavaScript/Web Examples

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # ഹോട്ട് റീലോഡ് ഉപയോഗിച്ചുള്ള വികസനം
```

## Testing

ഈ റിപോസിറ്ററി യൂണിറ്റ് ടെസ്റ്റുകളുള്ള ഒരു പരമ്പരാഗത സോഫ്റ്റ്വെയർ പ്രോജക്റ്റ് ആവരും, മറിച്ച് ഉദാഹരണ കോഡ് এবং ട്യൂട്ടോറിയലുകൾ ഉൾക്കൊള്ളുന്നു. സാധാരണമായി അവലോകനം നിർവഹിക്കുന്നത് താഴെപ്പറയുന്നവയിലൂടെ ആണ്:

1. **Running the examples** - ഓരോ ഉദാഹരണമും തെറ്റുകൾ ഇല്ലാതെ പ്രവർത്തിക്കണം
2. **Verifying outputs** - മോഡൽ പ്രതികരണങ്ങൾ അനുയോജ്യമാണ് എന്ന് പരിശോധിക്കുക
3. **Following tutorials** - ട്യൂട്ടോറിയലുകൾ രേഖപ്പെടുത്തിയതുപോലെ പ്രവൃത്തി ചെയ്യണം

**Common validation approach:**
- ലക്ഷ്യ എൻവയോൺമെന്റിൽ ഉദാഹരണങ്ങളുടെ എക്‌സിക്യൂഷൻ ടെസ്റ്റുചെയ്യുക
- ഡിപ്പൻഡൻസികൾ ശരിയായി ഇൻസ്റ്റാൾ ആക്കപ്പെട്ടിട്ടുണ്ടോ എന്ന് പരിശോധിക്കുക
- മോഡലുകൾ ഡൗൺലോഡ്/ലോഡ് ശരിയായി നടക്കുന്നുണ്ടോ എന്ന് പരിശോധിക്കുക
- പ്രതീക്ഷിക്കപ്പെട്ട പെരുമാറ്റം ഡോക്യുമെന്റേഷനുമായി പൊരുത്തപ്പെടുന്നുണ്ടോ എന്ന് സ്ഥിരീകരിക്കുക

## Code Style and Conventions

### General Guidelines

- ഉദാഹരണങ്ങൾ വ്യക്തവും, വിശദമായ കമന്റുകളോടെ ആയിരിക്കണം, വിദ്യാഭ്യാസ ലക്ഷ്യത്തോടെ ഒരുക്കണം
- ഭാഷാ-നിർദിഷ്ട ചട്ടങ്ങൾ പാലിക്കുക (Python-ക്ക് PEP 8, .NET-ക്കുള്ള C# സ്റ്റാൻഡാർഡുകൾ)
- ഉദാഹരണങ്ങൾ Phi മോഡൽ ശേഷികളെ പ്രദർശിപ്പിക്കുന്നതിനാണ് കേന്ദ്രീകരിക്കുകയും ചെയ്യുക
- പ്രധാന ആശയങ്ങളും മോഡൽ-നിർദിഷ്ട പാരാമീറ്ററുകൾ വിശദീകരിക്കുന്ന കമന്റുകൾ ഉൾപ്പെടുത്തുക

### Documentation Standards

**URL Formatting:**
- അധിക സ്ഥലം കൂടാതെ `[text](../../url)` ഫോർമാറ്റ് ഉപയോഗിക്കുക
- റെലറ്റിവ് ലിങ്കുകൾ: നിലവിലെ ഡയറക്ടറിയ്ക്ക് `./` ഉപയോഗിക്കുക, മാതൃ ഡയറക്ടറിയ്ക്ക് `../` ഉപയോഗിക്കുക
- URLs-ൽ നാട്-നിർദിഷ്ട ലോക്കൽ ചേർക്കരുത് ( `/en-us/`, `/en/` ഒഴിവാക്കുക )

**Images:**
- എല്ലാ ചിത്രങ്ങളും `/imgs/` ഡയറക്ടറിയിൽ സൂക്ഷിക്കുക
- ഇംഗ്ലീഷ് അക്ഷരങ്ങൾ, സംഖ്യകൾ, ഡാഷ് എന്നിവ ഉപയോഗിച്ച് വിവരണാത്മക നാമങ്ങൾ ഉപയോഗിക്കുക
- ഉദാഹരണം: `phi-3-architecture.png`

**Markdown Files:**
- `/code/` ഡയറക്ടറിയിലുള്ള പ്രവർത്തനക്ഷമ ഉദാഹരണങ്ങൾ നേരെ റഫറൻസ് ചെയ്യുക
- ഡോക്യുമെന്റേഷൻ കോഡ് മാറ്റങ്ങളോടൊപ്പം സമന്വയിപ്പിച്ചുകൊണ്ടിരിക്കുക
- README-ൽ Jupyter നോട്ട്ബുക്ക് ലിങ്കുകൾ അടയാളപ്പെടുത്താൻ 📓 എമോജി ഉപയോഗിക്കുക

### File Organization

- `/code/`-ലെ കോഡ് ഉദാഹരണങ്ങൾ വിഷയം/ഫീച്ചർ പ്രകാരം ക്രമീകരിക്കുക
- ഡോക്യുമെന്റേഷൻ `/md/` കോഡ് ഘടനയെ സ്വഭാവതത്പരമായി അനുകരിക്കുകയും ചെയ്യുക
- ബന്ധപ്പെട്ട ഫയലുകൾ (നോട്ട്ബുക്കുകൾ, സ്‌ക്രിപ്റ്റുകൾ, കോൺഫിഗുകൾ) സബ്ഡയറക്ടറികളിൽ ചേർത്തുനിരത്തി വെക്കുക

## Pull Request Guidelines

### Before Submitting

1. **Fork the repository** to your account
2. **Separate PRs by type:**
   - ഒരു PR-ൽ ഓരോ ബഗ് ഫിക്‌സ് ചെയ്യുക
   - ഡോക്യുമെന്റേഷൻ അപ്ഡേറ്റുകൾ വേറെ PR-ൽ ചെയ്യുക
   - പുതിയ ഉദാഹരണങ്ങൾ വേറെ PR-കളിൽ സബ്മിറ്റ് ചെയ്യുക
   - ടൈപ്പോ ഫിക്‌സുകൾ സംയോജിപ്പിക്കാവുന്നതാണ്

3. **Handle merge conflicts:**
   - മാറ്റങ്ങൾ ചെയ്യുന്നതിനു മുമ്പ് നിങ്ങളുടെ ലൊക്കൽ `main` ബ്രാഞ്ച് അപ്ഡേറ്റ് ചെയ്യുക
   - അപ്സ്ട്രീമുമായി സ്ഥിരം സമന്വയം বজায় നിലനിർത്തുക

4. **Translation PRs:**
   - ഫോൾഡറിലുള്ള എല്ലാ ഫയലുകൾക്കും പരിഭാഷകൾ ഉള്‍പ്പെടണം
   - മുൽഭാഷാനിലയവുമായി പൊരുത്തം നിലനിർത്തുക

### Required Checks

PR-കൾ ഓട്ടോമാറ്റിക്കായി GitHub വർക്ഫ്ലോകൾ ഓടിച്ച് താഴെ പരിശോധിക്കുന്നു:

1. **Relative path validation** - എല്ലാ അകത്ത് ലിങ്കുകളും പ്രവർത്തിക്കണം
   - ലിങ്കുകൾ ലോക്കലായി പരീക്ഷിക്കാൻ: VS Code-ൽ Ctrl+Click ഉപയോഗിക്കുക
   - VS Code-ലെ പാത്ത് നിർദ്ദേശങ്ങൾ ഉപയോഗിക്കുക (`./` അല്ലെങ്കിൽ `../`)

2. **URL locale check** - വെബ് URLs-ൽ നാട്-നിർദിഷ്ട ലോക്കൽ അടങ്ങിയിരിക്കരുത്
   - `/en-us/`, `/en/` അല്ലെങ്കിൽ മറ്റ് ഭാഷാ കോഡുകൾ നീക്കംചെയ്യുക
   - സർവധാന ലക്ഷ്യ URL-കൾ ഉപയോഗിക്കുക

3. **Broken URL check** - എല്ലാ URLs-ഉം 200 സ്റ്റാറ്റസ് റിട്ടേൺ ചെയ്യണം
   - ലിങ്കുകൾ സബ്മിഷനു മുമ്പ് ലഭ്യമായിട്ടുണ്ടെന്ന് പരിശോധിക്കുക
   - കുറച്ച് തകരാറുകൾ നെറ്റ്‌വർക്കു കാരണം ഉണ്ടായിരിക്കും എന്ന് ശ്രദ്ധിക്കുക

### PR Title Format

```
[component] Brief description
```

Examples:
- `[docs] Add Phi-4 inference tutorial`
- `[code] Fix ONNX Runtime integration example`
- `[translation] Add Japanese translation for intro guides`

## Common Development Patterns

### Working with Phi Models

**Model Loading:**
- ഉദാഹരണങ്ങൾ വിവിധ ഫ്രെയിംവർക്കുകൾ ഉപയോഗിക്കുന്നു: Transformers, ONNX Runtime, MLX, OpenVINO
- മോഡലുകൾ സാധാരണയായി Hugging Face, Azure, അല്ലെങ്കിൽ GitHub Models-ൽ നിന്ന് ഡൗൺലോഡ് ചെയ്യപ്പെടുന്നു
- നിങ്ങളുടെ ഹാർഡ്‌വെയറുമായി മോഡൽ പൊരുത്തപ്പെടുന്നുണ്ടോ എന്ന് പരിശോധിക്കുക (CPU, GPU, NPU)

**Inference Patterns:**
- ടെക്സ്റ്റ് ജനറേഷൻ: പലതവണ ചാറ്റ്/ഇൻസ്ട്രക്റ്റ് വകഭാഗങ്ങൾ ഉപയോഗിക്കുന്നു
- വിഷൻ: ചിത്രം മനസിലാക്കുന്നതിന് Phi-3-vision and Phi-4-multimodal
- ഓഡിയോ: Phi-4-multimodal ഓഡിയോ ഇൻപുട്ടുകൾ പിന്തുണയ്ക്കുന്നു
- വീക്ഷണശക്തി: സമഗ്രമായ പ്രശ്നപരിഹാരങ്ങൾക്കായി Phi-4-reasoning വകഭാഗങ്ങൾ

### Platform-Specific Notes

**Microsoft Foundry:**
- Azure സബ്‌സ്‌ക്രിപ്ഷനും API കീകളും ആവശ്യമാണ്
- കാണുക `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- പരീക്ഷണത്തിനായി ഫ്രീ ടിയർ ലഭ്യമാണ്
- കാണുക `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Local Inference:**
- ONNX Runtime: ക്രോസ്-പ്ലാറ്റ്ഫോം, ഓപ്റ്റിമൈസ്ഡ് ഇൻഫറൻസ്
- Ollama: ലൊക്കൽ മോഡൽ മാനേജ്‌മെന്റ് എളുപ്പമാക്കി (dev container-ൽ മുൻകൂട്ടി കോൺഫിഗർ ചെയ്തിരിക്കുന്നു)
- Apple MLX: Apple Silicon-നു അനുയോജ്യമായി ഓപ്റ്റിമൈസ്ഡ്

## Troubleshooting

### Common Issues

**Memory Issues:**
- Phi മോഡലുകൾ വലിയ RAM ആവശ്യപ്പെടുന്നു (പ്രത്യേകം വിഷൻ/മൾട്ടി മോഡൽ വകഭാഗങ്ങൾ)
- റിസോഴ്സ്-പരിമിത സാഹചര്യങ്ങളിൽ ക്വാണ്ടൈസ്ഡ് മോഡലുകൾ ഉപയോഗിക്കുക
- കാണുക `/md/01.Introduction/04/QuantifyingPhi.md`

**Dependency Conflicts:**
- Python ഉദാഹരണങ്ങൾക്ക് പ്രത്യേക വേർഷൻ ആവശ്യങ്ങൾ ഉണ്ടായിരിക്കാൻ സാധ്യതയുണ്ട്
- ഓരോ ഉദാഹരണത്തിനും വേർതിരിച്ചിരിക്കുമായ വിർച്വൽ എൻവയോൺമെന്റ് ഉപയോഗിക്കുക
- ഓരോ പദ്ധതിയുടെയും `requirements.txt` ഫയലുകൾ പരിശോധിക്കുക

**Model Download Failures:**
- വലിയ മോഡലുകൾ മന്ദഗതിക്കുള്ള കണക്ഷനിൽ ടൈമ്ഔട്ട് ചെയ്യാം
- Codespaces, Azure പോലുള്ള ക്ലൗഡ് എൻവയോൺമെന്റുകൾ ഉപയോഗിക്കmayı പരിഗണിക്കുക
- Hugging Face cache പരിശോധിക്കുക: `~/.cache/huggingface/`

**.NET Project Issues:**
- .NET 8.0 SDK ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക
- ബിൽഡ് ചെയ്യുന്നതിനു മുമ്പ് `dotnet restore` നടത്തുക
- ചില പ്രോജക്റ്റുകൾക്ക് CUDA-പ്രത്യക്ഷമായ കോൺഫിഗറേഷനുകൾ (Debug_Cuda) ഉണ്ടായിരിക്കും

**JavaScript/Web Examples:**
- ഇൻകമ്പാറ്റിബിലിറ്റിക്ക് Node.js 18+ ഉപയോഗിക്കുക
- പ്രശ്നങ്ങൾ തുടരുകയാണെങ്കിൽ `node_modules` ക്ലിയർ ചെയ്ത് വീണ്ടും ഇൻസ്റ്റാൾ ചെയ്യുക
- WebGPU സംവേദനത്വം പരിശോധിക്കാൻ ബ്രൗസർ കോൺസോൾ പരിശോധിക്കുക

### Getting Help

- **Discord:** Microsoft Foundry Community Discord-ൽ ചേക്കേറി സഹായം തേടുക
- **GitHub Issues:** ബഗ്ഗുകളും പ്രശ്നങ്ങളും റിപോർട്ട് ചെയ്യുക
- **GitHub Discussions:** ചോദ്യങ്ങൾ ചോദിക്കുക અને അറിവ് പങ്കിടുക

## Additional Context

### Responsible AI

Phi മോഡലുകളുടെ എല്ലാ ഉപയോഗവും Microsoft's Responsible AI തത്വങ്ങൾ പാലിക്കണം:
- നീതിമാന്യം, വിശ്വാസ്യത, സുരക്ഷ
- פרטത്വവും സുരക്ഷയും  
- ഉൾക്കൊള്ളൽ, പരദർശിത്വം, ഉത്തരവാദിത്തം
- പ്രൊഡക്ഷൻ ആപ്ലിക്കേഷനുകൾക്കായി Azure AI Content Safety ഉപയോഗിക്കുക
- കാണുക `/md/01.Introduction/01/01.AISafety.md`

### Translations

- ഓട്ടോമേറ്റഡ് GitHub Action വഴിയാണ് 50+ ഭാഷകൾക്കുള്ള പിന്തുണ
- പരിഭാഷകൾ `/translations/` ഡയറക്ടറിയിൽ ലഭ്യമാണ്
- co-op-translator പ്രവൃത്തി ഫ്‌ളോ നേതൃത്വത്തിൽ നന്യഥമായി പരിപാലിക്കുന്നു
- കൈമാറി പരിഭാഷിച്ച ഫയലുകൾ കൈക്കൊണ്ടുള്ള തിരുത്തൽ ചെയ്യരുത് (ഓട്ടോ-ജനറേറ്റഡ്)

### Contributing

- `CONTRIBUTING.md`-ൽ ഉള്ള മാർഗ്ഗനിർദ്ദേശങ്ങൾ പാലിക്കുക
- Contributor License Agreement (CLA)-ക്ക് അനുമതി നൽകുക
- Microsoft Open Source Code of Conduct പാലിക്കുക
- സുരക്ഷയും ക്രെഡൻഷ്യലുകളും കമ്മിറ്റുകളിൽ ഉൾപ്പെടുത്തരുത്

### Multi-Language Support

ഇത് വിവിധ ഭാഷകളിലുള്ള ഉദാഹരണങ്ങളുള്ള പലഭാഷാ റിപോസിറ്ററിയാണ്:
- **Python** - ML/AI വർക്ക്‌ഫ്ലോക്സ്, Jupyter നോട്ട്ബുക്കുകൾ, ഫൈൻ-ട്യുണിംഗ്
- **C#/.NET** - എന്റർപ്രൈസ് ആപ്ലിക്കേഷനുകൾ, ONNX Runtime ഇന്റഗ്രേഷൻ
- **JavaScript** - വെബ് അടിസ്ഥാനമാക്കിയുള്ള AI, WebGPU ഉപയോഗിച്ച് ബ്രൗസർ ഇൻഫറൻസ്

നിങ്ങളുടെ ഉപയോഗ കേസിനും വിന്യാസ ലക്ഷ്യത്തിനും ഏറ്റവും അനുയോജ്യമായ ഭാഷ തിരഞ്ഞെടുക്കുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്‌ക്ലെയിമർ:
ഈ ഡോക്യുമെന്റ് AI വിവർത്തന സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്‌തതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ തെറ്റുകൾ അല്ലെങ്കിൽ അപൂർണ്ണതകൾ ഉണ്ടാകാവുന്നതാണ് എന്ന് ദയവായി ശ്രദ്ധിക്കുക. മൂല രേഖയുടെ പ്രാഥമിക ഭാഷയിലെ പതിപ്പ് ആണ് അധികാരപരമായ ഉറവിടം എന്ന നിലയിൽ പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം നിർദേശിക്കുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണങ്ങൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->