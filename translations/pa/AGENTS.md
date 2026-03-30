# AGENTS.md

## Project Overview

PhiCookBook ਮਾਈਕ੍ਰੋਸੌਫਟ ਦੇ Phi ਪਰਿਵਾਰ ਦੇ ਛੋਟੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ (SLMs) ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ ਹੱਥ-ਉੱਤੇ ਉਦਾਹਰਨਾਂ, ਟਿਊਟੋਰੀਅਲਾਂ ਅਤੇ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਵਾਲਾ ਇੱਕ ਵਿਸ਼ਤ੍ਰਿਤ ਕੂਕਬੁੱਕ ਰਿਪੋਜ਼ਟਰੀ ਹੈ। ਇਹ ਰਿਪੋਜ਼ਟਰੀ ਵੱਖ ਵੱਖ ਪਲੇਟਫਾਰਮਾਂ ਅਤੇ ਫਰੇਮਵਰਕਾਂ 'ਤੇ ਇੰਫਰੰਸ, ਫਾਈਨ-ਟਿਊਨਿੰਗ, ਕੁਆੰਟਾਈਜੇਸ਼ਨ, RAG ਹਲਾਂ ਅਤੇ ਮਲਟੀਮੋਡਲ ਐਪਲੀਕੇਸ਼ਨਾਂ ਸਮੇਤ ਕਈ ਵਰਤੋਂ ਦੇ ਕੇਸ ਦਰਸਾਉਂਦੀ ਹੈ।

**ਮੁੱਖ ਤਕਨਾਲੋਜੀਆਂ:**
- **ਭਾਸ਼ਾਵਾਂ:** Python, C#/.NET, JavaScript/Node.js
- **ਫਰੇਮਵਰਕ:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **ਪਲੇਟਫਾਰਮ:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **ਮਾਡਲ ਕਿਸਮਾਂ:** Phi-3, Phi-3.5, Phi-4 (ਟੈਕਸਟ, ਵਿਜ਼ਨ, ਮਲਟੀਮੋਡਲ, ਕਾਰਨ ਦਾਰ ਵਰਜਨ)

**ਰਿਪੋਜ਼ਟਰੀ ਢਾਂਚਾ:**
- `/code/` - ਕੰਮ ਕਰਨ ਵਾਲੀ ਕੋਡ ਦੀਆਂ ਉਦਾਹਰਨਾਂ ਅਤੇ ਸੈਂਪਲ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ
- `/md/` - ਵਿਸਥਾਰਸਤ ਦਸਤਾਵੇਜ਼ੀਕਰਨ, ਟਿਊਟੋਰੀਅਲ ਅਤੇ ਕਿਵੇਂ-ਕਰਨਾ ਗਾਈਡ
- `/translations/` - ਬਹੁ-ਭਾਸ਼ਾਈ ਅਨੁਵਾਦ (50+ ਭਾਸ਼ਾਵਾਂ ਆਟੋਮੈਟਿਕ ਵਰਕਫਲੋ ਰਾਹੀਂ)
- `/.devcontainer/` - ਡਿਵ ਕੰਟੇਨਰ ਸੰਰਚਨਾ (Python 3.12 ਨਾਲ Ollama)

## Development Environment Setup

### Using GitHub Codespaces or Dev Containers (Recommended)

1. GitHub Codespaces ਵਿੱਚ ਖੋਲ੍ਹੋ (ਸਭ ਤੋਂ ਤੇਜ਼):
   - README ਵਿੱਚ "Open in GitHub Codespaces" ਬੈਜ 'ਤੇ ਕਲਿੱਕ ਕਰੋ
   - ਕੰਟੇਨਰ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ Python 3.12 ਅਤੇ Ollama ਫਿ-3 ਨਾਲ ਕਾਨੂੰਫਿਗਰ ਹੁੰਦਾ ਹੈ

2. VS Code Dev Containers ਵਿੱਚ ਖੋਲ੍ਹੋ:
   - README ਤੋਂ "Open in Dev Containers" ਬੈਜ ਦੀ ਵਰਤੋਂ ਕਰੋ
   - ਕੰਟੇਨਰ ਲਈ ਘੱਟੋ-ਘੱਟ 16GB ਮੈਮੋਰੀ ਦੀ ਲੋੜ ਹੈ

### Local Setup

**ਜ਼ਰੂਰੀ ਸ਼ਰਤਾਂ:**
- Python 3.12 ਜਾਂ ਉਪਰ
- .NET 8.0 SDK (C# ਉਦਾਹਰਨ ਲਈ)
- Node.js 18+ ਅਤੇ npm (JavaScript ਉਦਾਹਰਨ ਲਈ)
- ਘੱਟੋ-ਘੱਟ 16GB RAM ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਗਈ ਹੈ

**ਇਨਸਟਾਲੇਸ਼ਨ:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**Python ਉਦਾਹਰਨਾਂ ਲਈ:**
ਨਿਰਧਾਰਿਤ ਉਦਾਹਰਨ ਡਾਇਰੈਕਟਰੀਜ਼ ਵਿੱਚ ਜਾਕੇ Dependencies ਇਨਸਟਾਲ ਕਰੋ:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # ਜੇ requirements.txt ਮੌਜੂਦ ਹੈ
```

**.NET ਉਦਾਹਰਨਾਂ ਲਈ:**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**JavaScript/Web ਉਦਾਹਰਨਾਂ ਲਈ:**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # ਵਿਕਾਸ ਸਰਵਰ ਸ਼ੁਰੂ ਕਰੋ
npm run build  # ਉਤਪਾਦਨ ਲਈ ਬਿਲਡ ਕਰੋ
```


## Repository Organization

### Code Examples (`/code/`)

- **01.Introduce/** - ਬੁਨਿਆਦੀ ਤਰ੍ਹਾਂ ਪਛਾਣ ਅਤੇ ਸ਼ੁਰੂਆਤੀ ਸੈਂਪਲ
- **03.Finetuning/** ਅਤੇ **04.Finetuning/** - ਵੱਖ-ਵੱਖ ਤਰੀਕਿਆਂ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਉਦਾਹਰਨਾਂ
- **03.Inference/** - ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ (AIPC, MLX) ਤੇ ਇੰਫਰੰਸ ਉਦਾਹਰਨਾਂ
- **06.E2E/** - ਅੰਤ ਤੋਂ ਅੰਤ ਤੱਕ ਐਪਲੀਕੇਸ਼ਨ ਸੈਂਪਲ
- **07.Lab/** - ਪ੍ਰਯੋਗਸ਼ਾਲਾ/ਪ੍ਰਯੋਗਾਤਮਕ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ
- **08.RAG/** - ਰੀਟਰੀਵਲ-ਅੱਗਮੈਂਟਡ ਜਨਰੇਸ਼ਨ ਸੈਂਪਲ
- **09.UpdateSamples/** - ਨਵੀਂ ਅਪਡੇਟ ਕੀਤੀਆਂ ਉਦਾਹਰਨਾਂ

### Documentation (`/md/`)

- **01.Introduction/** - ਪਰਚਿਆਲੇ ਗਾਈਡ, ਵਾਤਾਵਰਣ ਸੈਟਅੱਪ, ਪਲੇਟਫਾਰਮ ਗਾਈਡ
- **02.Application/** - ਟੈਕਸਟ, ਕੋਡ, ਵਿਜ਼ਨ, ਆਡੀਓ ਆਦਿ ਅਨੁਸਾਰ ਐਪਲੀਕੇਸ਼ਨ ਸੈਂਪਲ
- **02.QuickStart/** - Microsoft Foundry ਅਤੇ GitHub Models ਲਈ ਤੁਰੰਤ ਸ਼ੁਰੂਆਤੀ ਗਾਈਡ
- **03.FineTuning/** - ਫਾਈਨ-ਟਿਊਨਿੰਗ ਦਸਤਾਵੇਜ਼ ਅਤੇ ਟਿਊਟੋਰੀਅਲ
- **04.HOL/** - ਹੱਥੋਂ-ਹੱਥ ਲੈਬ (ਜਿਸ ਵਿੱਚ .NET ਉਦਾਹਰਨ ਸ਼ਾਮਲ ਹਨ)

### File Formats

- **Jupyter Notebooks (`.ipynb`)** - ਇੰਟਰਐਕਟਿਵ Python ਟਿਊਟੋਰੀਅਲ ਜਿਨ੍ਹਾਂ ਨੂੰ README ਵਿੱਚ 📓 ਨਾਲ ਦਰਸਾਇਆ ਗਿਆ ਹੈ
- **Python Scripts (`.py`)** - ਅਕੇਲਾ Python ਉਦਾਹਰਨ
- **C# Projects (`.csproj`, `.sln`)** - .NET ਐਪਲੀਕੇਸ਼ਨ ਅਤੇ ਸੈਂਪਲ
- **JavaScript (`.js`, `package.json`)** - ਵੈੱਬ-ਅਧਾਰਿਤ ਅਤੇ Node.js ਉਦਾਹਰਨ
- **Markdown (`.md`)** - ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਅਤੇ ਗਾਈਡ

## Working with Examples

### Running Jupyter Notebooks

ਜ਼ਿਆਦਾਤਰ ਉਦਾਹਰਨਾਂ Jupyter ਨੋਟਬੁੱਕ ਆਕਾਰ ਵਿੱਚ ਪ੍ਰਦਾਨ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ:
```bash
pip install jupyter notebook
jupyter notebook  # ਬਰਾਊਜ਼ਰ ਇੰਟਰਫੇਸ ਖੋਲ੍ਹੋ
# ਮਨਪਸੰਦ .ipynb ਫਾਈਲ 'ਤੇ ਜਾਓ
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

ਜਾਂ ਪੂਰੀ ਸੋਲੁਸ਼ਨ ਬਣਾਓ:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```


### Running JavaScript/Web Examples

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # ਹਾਟ ਰਿਲੋਡ ਨਾਲ ਵਿਕਾਸ
```


## Testing

ਇਹ ਰਿਪੋਜ਼ਟਰੀ ਇਕ ਪਰੰਪਰਾਗਤ ਸੌਫਟਵੇਅਰ ਪ੍ਰੋਜੈਕਟ ਵਰਗੀ ਯੂਨਿਟ ਟੈਸਟਾਂ ਦੇ ਬਜਾਏ ਉਦਾਹਰਨ ਕੋਡ ਅਤੇ ਟਿਊਟੋਰੀਅਲ ਮੁਹੱਈਆ ਕਰਵਾਉਂਦੀ ਹੈ। ਪ੍ਰਮਾਣੀਕਰਨ ਆਮ ਤੌਰ 'ਤੇ ਇਸ ਤਰ੍ਹਾਂ ਹੁੰਦਾ ਹੈ:

1. **ਉਦਾਹਰਨ ਚਲਾਉਣਾ** - ਹਰ ਉਦਾਹਰਨ ਗਲਤੀ ਤੋਂ ਬਿਨਾਂ ਚਲਾਉਣੀ ਚਾਹੀਦੀ ਹੈ  
2. **ਆਉਟਪੁੱਟ ਦੀ ਪੁਸ਼ਟੀ ਕਰਨਾ** - ਚੈੱਕ ਕਰੋ ਕਿ ਮਾਡਲ ਦੇ ਜਵਾਬ ਸਹੀ ਹਨ  
3. **ਟਿਊਟੋਰੀਅਲ ਦੀ ਪਾਲਣਾ ਕਰਨਾ** - ਕਦਮ-ਦਰ-कਦਮ ਗਾਈਡਾਂ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਅਨੁਸਾਰ ਕੰਮ ਕਰਦੀਆਂ ਹੋਣ

**ਸਾਂਝਾ ਪ੍ਰਮਾਣੀਕਰਨ ਢੰਗ:**
- ਟਾਰਗੇਟ ਵਾਤਾਵਰਣ ਵਿੱਚ ਉਦਾਹਰਨਾਂ ਦੀ ਚਲਾਣਾ
- Dependencies ਦੀ ਸਹੀ ਤਰ੍ਹਾਂ ਇਨਸਟਾਲੇਸ਼ਨ ਜਾਂਚੋ
- ਮਾਡਲ ਕੇ ਡਾਊਨਲੋਡ/ਲੋਡ ਮਹੱਤਵਪੂਰਨ ਹੈ ਜਾਂ ਨਹੀਂ ਇਸ ਦੀ ਜਾਂਚ
- ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਨਾਲ ਉਮੀਦਵਾਰ ਵਿਹਾਰ ਦੀ ਪੁਸ਼ਟੀ ਕਰਨਾ

## Code Style and Conventions

### General Guidelines

- ਉਦਾਹਰਨ ਸਪਸ਼ਟ, ਚੰਗੀ ਤਰ੍ਹਾਂ ਟਿੱਪਣੀ ਵਾਲੀਆਂ ਅਤੇ ਸਿੱਖਣਯੋਗ ਹੋਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ
- ਭਾਸ਼ਾ-ਖਾਸ ਕਥਾਵਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ (Python ਲਈ PEP 8, .NET ਲਈ C# ਮਿਆਰ)
- ਉਦਾਹਰਨ ਨੂੰ ਖਾਸ Phi ਮਾਡਲ ਦੀਆਂ ਖੂਬੀਆਂ ਦਰਸਾਉਣ 'ਤੇ ਧਿਆਨ ਰੱਖੋ
- ਮੁੱਖ ਅਸਲਾਂ ਅਤੇ ਮਾਡਲ-ਖਾਸ ਪੈਰਾਮੀਟਰਾਂ ਨੂੰ ਸਮਝਾਉਣ ਵਾਲੀਆਂ ਟਿੱਪਣੀਆਂ ਸ਼ਾਮਲ ਕਰੋ

### Documentation Standards

**URL ਫਾਰਮੇਟਿੰਗ:**
- `[text](../../url)` ਫਾਰਮੈਟ ਬਿਨਾਂ ਵਾਧੂ ਖਾਲੀ ਥਾਂਵਾਂ ਦੇ ਵਰਤੋਂ
- ਰਿਲੇਟਿਵ ਲਿੰਕ: ਮੌਜੂਦਾ ਡਾਇਰੈਕਟਰੀ ਲਈ `./`, ਵਾਲੀ ਡਾਇਰੈਕਟਰੀ ਲਈ `../` ਵਰਤੋਂ
- URLs ਵਿੱਚ ਦੇਸ਼-ਵਿਸ਼ੇਸ਼ ਭਾਸ਼ਾ ਕੋਡ ਨਾ ਹੋਣ (ਜਿਵੇਂ `/en-us/`, `/en/`)

**ਚਿੱਤਰ:**
- ਸਾਰੇ ਚਿੱਤਰ `/imgs/` ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਰੱਖੋ
- ਨਾਮ ਅੰਗਰੇਜ਼ੀ ਅੱਖਰਾਂ, ਨੰਬਰਾਂ ਅਤੇ ਡੈਸ਼ਾਂ ਨਾਲ ਵਰਨਣਸ਼ੀਲ ਹੋਣ  
- ਉਦਾਹਰਨ: `phi-3-architecture.png`

**Markdown Files:**
- `/code/` ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਵਾਸਤੇ ਡਾਟਾ ਕੰਮ ਕਰਨ ਵਾਲੀਆਂ ਉਦਾਹਰਨਾਂ ਦਾ ਹਵਾਲਾ
- ਦਸਤਾਵੇਜ਼ਾਂ ਨੂੰ ਕੋਡ ਬਦਲਾਵਾਂ ਨਾਲ ਸਿੰਕ੍ਰੋਨਾਈਜ਼ ਰੱਖੋ
- README ਵਿੱਚ Jupyter ਨੋਟਬੁੱਕ ਲਿੰਕਾਂ ਲਈ 📓 ਇਮੋਜੀ ਵਰਤੋਂ

### File Organization

- `/code/` ਵਿੱਚ ਟਾਪਿਕ/ਫੀਚਰ ਅਨੁਸਾਰ ਕੋਡ ਦੀਆਂ ਉਦਾਹਰਨਾਂ ਸੰਖਿਆਤਮਕ
- `/md/` ਵਿੱਚ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਕੋਡ ਜੇ ਤਕ ਕਰਨਯੋਗ ਹੋਵੇ ਤਾਂ ਉਸ ਦੇ ਅਨੁਰੂਪ
- ਨੋਟਬੁੱਕ, ਸਕ੍ਰਿਪਟ ਅਤੇ ਸੰਰਚਨਾ ਫਾਈਲਾਂ ਨਾਲ ਸਬੰਧਤ ਫਾਈਲਾਂ ਇੱਕੱਠੇ ਰੱਖੋ

## Pull Request Guidelines

### Before Submitting

1. ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਆਪਣੇ ਖਾਤੇ ਵਿੱਚ ਫੋਰਕ ਕਰੋ
2. PR ਤਰ੍ਹਾਂ ਵੱਖ ਕਰੋ:
   - ਇੱਕ PR ਵਿੱਚ ਬਗ ਫਿਕਸ
   - ਦੂਜੇ PR ਵਿੱਚ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਅਪਡੇਟ
   - ਨਵੇਂ ਉਦਾਹਰਨ ਵੱਖ PR ਵਿੱਚ
   - ਟਾਈਪੋ ਫਿਕਸ ਇੱਕੱਠੇ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ

3. ਮਰਜ ਕਨਫਲਿਕਟ ਸੰਭਾਲੋ:
   - ਬਦਲਾਅ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਆਪਣੀ ਲੋਕਲ `main` ਸ਼ਾਖਾ ਅਪਡੇਟ ਕਰੋ
   - ਅੱਪਸਟਰੀਮ ਰੇਪੋ ਨਾਲ ਰੈਗੁਲਰ ਤੌਰ 'ਤੇ ਸਿੰਕ ਕਰਨਾ

4. ਅਨੁਵਾਦ PR:
   - ਫੋਲਡਰ ਵਾਲੇ ਸਾਰੇ ਫਾਈਲਾਂ ਲਈ ਅਨੁਵਾਦ ਸ਼ਾਮਲ ਹੋਣ ਚਾਹੀਦੇ ਹਨ
   - ਅਸਲ ਭਾਸ਼ਾ ਦੇ ਢਾਂਚੇ ਨਾਲ ਸਾੈਧ ਜਾਰੂਰੀ

### Required Checks

PR ਸਵੈਚਾਲਿਤ GitHub ਵਰਕਫਲੋਜ਼ ਚਲਾਈ ਜਾਂਦੀਆਂ ਹਨ ਜੋ ਕਿ ਪੁਸ਼ਟੀ ਕਰਦੀਆਂ ਹਨ:

1. ਰਿਲੇਟਿਵ ਪਾਥ ਚੈੱਕ - ਸਾਰੇ ਅੰਦਰੂਨੀ ਲਿੰਕ ਕੰਮ ਕਰਨਗੇ
   - VS Code ਵਿੱਚ Ctrl+ਕਲਿੱਕ ਕਰਕੇ ਟੈਸਟ ਕਰੋ
   - VS Code ਤੋਂ ਪਾਥ ਸਝਾਵ (./ ਜਾਂ ../) ਵਰਤੋਂ

2. URL locale ਚੈੱਕ - ਵੈੱਬ URLs ਵਿੱਚ ਦੇਸ਼-ਵਿਸ਼ੇਸ਼ ਭਾਸ਼ਾਈ ਕੋਡ ਨਾ ਹੋਣ
   - `/en-us/`, `/en/` ਜਾਂ ਹੋਰ ਭਾਸ਼ਾ ਕੋਡ ਹਟਾਓ
   - ਜਨਰਿਕ ਇੰਟਰਨੈਸ਼ਨਲ URLs ਵਰਤੋਂ

3. ਟੁੱਟੇ ਹੋਏ URL ਚੈੱਕ - ਸਾਰੇ URLs 200 ਸਟੇਟਸ ਰਿਟਰਨ ਕਰਣ
   - ਲਿੰਕਾਂ ਸਬਮਿਟ ਕਰਨ ਤੋਂ ਪਹਿੱਲਾਂ ਐਕਸੈਸੀਬਲ ਹੋਣ ਦੀ ਜਾਂਚ ਕਰੋ
   - ਨੋਟ: ਕੁਝ ਫੇਲ੍ਹ ਨੈੱਟਵਰਕ ਪ੍ਰਤੀਬੰਧਾਂ ਕਾਰਨ ਵੀ ਹੋ ਸਕਦੇ ਹਨ

### PR Title Format

```
[component] Brief description
```

ਉਦਾਹਰਨ:
- `[docs] Add Phi-4 inference tutorial`
- `[code] Fix ONNX Runtime integration example`
- `[translation] Add Japanese translation for intro guides`

## Common Development Patterns

### Working with Phi Models

**Model Loading:**
- ਉਦਾਹਰਨ ਵੱਖ ਫਰੇਮਵਰਕ ਵਰਤਦੀਆਂ ਹਨ: Transformers, ONNX Runtime, MLX, OpenVINO
- ਮਾਡਲ ਆਮ ਤੌਰ ਤੇ Hugging Face, Azure ਜਾਂ GitHub Models ਤੋਂ ਡਾਊਨਲੋਡ ਕੀਤੇ ਜਾਂਦੇ ਹਨ
- ਆਪਣੇ ਹਾਰਡਵੇਅਰ (CPU, GPU, NPU) ਨਾਲ ਮਾਡਲ ਦੀ ਮੇਲ ਖਾਂਚੀ ਜਾਂਚੋ

**Inference Patterns:**
- ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ: ਸਭ ਤੋਂ ਵੱਧ ਚੈਟ/ਨਿਰਦੇਸ਼ ਵਰਜਨਾਂ ਦੀ ਵਰਤੋਂ
- ਵਿਜ਼ਨ: ਚਿੱਤਰ ਸਮਝਣ ਲਈ Phi-3-vision ਅਤੇ Phi-4-multimodal
- ਆਡੀਓ: ਆਡੀਓ ਇੰਪੁੱਟ ਲਈ Phi-4-multimodal ਸਹਾਇਤਾ
- ਕਾਰਨ ਦਾਰੀ: ਉੱਨਤ ਕਾਰਨ ਦਾਰ ਕੰਮਾਂ ਲਈ Phi-4-reasoning ਵਰਜਨ

### Platform-Specific Notes

**Microsoft Foundry:**
- Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਅਤੇ API ਕੁੰਜੀਆਂ ਦੀ ਲੋੜ
- ਵੇਖੋ `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- ਟੈਸਟਿੰਗ ਲਈ ਮੁਫ਼ਤ ਪੱਧਰ ਉਪਲਬਧ
- ਵੇਖੋ `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Local Inference:**
- ONNX Runtime: ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ, ਅਪਟੀਮਾਈਜ਼ਡ ਇੰਫਰੰਸ
- Ollama: ਸੌਖਾ ਲੋਕਲ ਮਾਡਲ ਮੈਂਜਮੈਂਟ (ਡਿਵ ਕੰਟੇਨਰ ਵਿੱਚ ਪਹਿਲਾਂ ਨਾਲ ਕਨਫਿਗਰ ਕੀਤਾ)
- Apple MLX: Apple Silicon ਲਈ ਅਪਟੀਮਾਈਜ਼ਡ

## Troubleshooting

### Common Issues

**Memory Issues:**
- Phi ਮਾਡਲਾਂ ਨੂੰ ਵਧੀਆ RAM ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ (ਖ਼ਾਸ ਕਰਕੇ ਵਿਜ਼ਨ/ਮਲਟੀਮੋਡਲ)
- ਸੀਮਿਤ ਸਰੋਤਾਂ ਵਾਲੇ ਵਾਤਾਵਰਣ ਲਈ ਕੁਆਂਟਾਈਜਡ ਮਾਡਲ ਵਰਤੋਂ
- ਵੇਖੋ `/md/01.Introduction/04/QuantifyingPhi.md`

**Dependency Conflicts:**
- Python ਉਦਾਹਰਨਾਂ ਵਿੱਚ ਖ਼ਾਸ ਵਰਜ਼ਨ ਦੀਆਂ ਲੋੜਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ
- ਹਰ ਉਦਾਹਰਨ ਲਈ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ
- ਵੱਖ-ਵੱਖ `requirements.txt` ਫਾਈਲਾਂ ਚੈੱਕ ਕਰੋ

**Model Download Failures:**
- ਵੱਡੇ ਮਾਡਲਾਂ ਦੀ ਡਾਊਨਲੋਡ ਤੇਜ਼ ਨੈੱਟਕਨੈਕਸ਼ਨ ਤੇ ਸਮੇਂ ਬੰਦੀ ਹੋ ਸਕਦੀ ਹੈ
- ਕਲਾਊਡ ਵਾਤਾਵਰਣਾਂ (Codespaces, Azure) ਦੀ ਵਰਤੋਂ ਸੋਚੋ
- Hugging Face cache ਦੀ ਜਾਂਚ ਕਰੋ: `~/.cache/huggingface/`

**.NET Project Issues:**
- .NET 8.0 SDK ਹੁਣੇਹੀ ਇਨਸਟਾਲ ਕਰੋ
- `dotnet restore` ਪਹਿਲਾਂ ਚਲਾਓ ਤਾਹਿ ਕੰਪਾਇਲ ਕਰੋ
- ਕੁਝ ਪ੍ਰੋਜੈਕਟ CUDA ਖਾਸ ਸੰਰਚਨਾ (Debug_Cuda) ਰੱਖਦੇ ਹਨ

**JavaScript/Web Examples:**
- ਸਮਰਥਿਤਤਾ ਲਈ Node.js 18+ ਵਰਤੋਂ
- node_modules ਮਿਟਾ ਕੇ ਦੁਬਾਰਾ ਇੰਸਟਾਲ ਕਰੋ ਜੇ ਮਸਲਾ ਧਰੇਰਾ ਹੋਵੇ
- WebGPU ਸਮਰਥਾ ਦੀ ਜਾਂਚ ਲਈ ਬ੍ਰਾਉਜ਼ਰ ਕਨਸੋਲ ਵੇਖੋ

### Getting Help

- **Discord:** Microsoft Foundry Community Discord ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਵੋ
- **GitHub Issues:** ਰਿਪੋਰਟ ਬੱਗ ਅਤੇ ਮੁੱਦੇ
- **GitHub Discussions:** ਪ੍ਰਸ਼ਨ ਪੁੱਛੋ ਅਤੇ ਗਿਆਨ ਸਾਂਝਾ ਕਰੋ

## Additional Context

### Responsible AI

ਸਭ Phi ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਮਾਇਕ੍ਰੋਸੌਫਟ ਦੇ ਸ਼ੁਮਾਰਦਾਰ ਜ਼ਿੰਮੇਵਾਰ AI ਸਿਧਾਂਤਾਂ ਅਨੁਸਾਰ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ:  
- ਇਨਸਾਫ਼, ਭਰੋਸਾ, ਸੁਰੱਖਿਆ  
- ਗੋਪਨੀਯਤਾ ਅਤੇ ਸੁਰੱਖਿਆ  
- ਸਮਾਵੇਸ਼ੀਤਾ, ਪਾਰਦਰਸ਼ਤਾ, ਜ਼ਿੰਮੇਵਾਰੀ  
- ਪ੍ਰੋਡਕਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ Azure AI Content Safety ਵਰਤੋਂ  
- ਵੇਖੋ `/md/01.Introduction/01/01.AISafety.md`

### Translations

- 50+ ਭਾਸ਼ਾਵਾਂ ਆਟੋਮੈਟਿਕ GitHub Action ਰਾਹੀਂ ਸਹਾਇਤਾ ਮੁਹੱਈਆ  
- `/translations/` ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਅਨੁਵਾਦ  
- ਕੋ-ਆਪ-ਟਰਾਂਸਲੇਟਰ ਵਰਕਫਲੋ ਦੁਆਰਾ ਵਿਚਾਲਨ  
- ਅਨੁਵਾਦ ਫਾਈਲਾਂ ਨੂੰ ਹੱਥੋਂ-ਹੱਥ ਸੋਧ ਨਾ ਕਰੋ (ਆਪੋ ਆਪ ਬਣਦਾ ਹੈ)

### Contributing

- `CONTRIBUTING.md` ਵਿੱਚ ਦਿਓ ਗਾਈਡਲਾਈਨਜ਼ ਦੀ ਪਾਲਣਾ ਕਰੋ  
- Contributor License Agreement (CLA) 'ਤੇ ਸਹਿਮਤ ਹੋਵੋ  
- ਮਾਇਕ੍ਰੋਸੌਫਟ ਦਾ ਖੁੱਲ੍ਹਾ ਸੋਰਸ ਕੋਡ ਅਚਰਣ ਮਾਨਦੇ ਹੋ ਜਾਓ  
- ਸੁਰੱਖਿਆ ਅਤੇ ਕ੍ਰੈਡੈਂਸ਼ਲ ਕਮਿਟਾਂ ਵਿੱਚ ਨਾ ਪਾਓ

### Multi-Language Support

ਇਹ ਇੱਕ ਬਹੁ-ਭਾਸ਼ਾ ਰਿਪੋਜ਼ਟਰੀ ਹੈ ਜਿਸ ਵਿੱਚ ਉਦਾਹਰਨ ਹਨ:  
- **Python** - ML/AI ਵਰਕਫਲੋ, Jupyter ਨੋਟਬੁੱਕ, ਫਾਈਨ-ਟਿਊਨਿੰਗ  
- **C#/.NET** - ਐਂਟਰਪ੍ਰਾਇਜ਼ ਐਪਲੀਕੇਸ਼ਨ, ONNX Runtime ਇੰਟੇਗ੍ਰੇਸ਼ਨ  
- **JavaScript** - ਵੈੱਬ-ਅਧਾਰਿਤ AI, ਬ੍ਰਾਉਜ਼ਰ ਇੰਫਰੰਸ WebGPU ਨਾਲ  

ਆਪਣੇ ਵਰਤੋਂ ਕੇਸ ਅਤੇ ਡਿਪਲոյਮੈਂਟ ਟਾਰਗੇਟ ਅਨੁਸਾਰ ਸਭ ਤੋਂ ਵਧੀਆ ਭਾਸ਼ਾ ਚੁਣੋ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਇਜ਼ਾਹੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸ਼ੁੱਧਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਗਲਤਫਹਮੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ 'ਚ ਸರ್ವਸੱਤਾ ਵਾਲਾ ਸਰੋਤ ਮੰਨਿਆ ਜਾਵੇ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਦੇ ਕਾਰਨ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀ ਜਾਂ ਗਲਤ ਅਰਥ ਨਿਕਾਸ ਦੇ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->