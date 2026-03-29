# AGENTS.md

## Project Overview

PhiCookBook na one complete cookbook repo wey get beta beta practical examples, tutorials, and documentation wey show how to work with Microsoft's Phi family of Small Language Models (SLMs). Dis repo dey show different kain use case like inference, fine-tuning, quantization, RAG implementations, and multimodal applications for different platforms and frameworks.

**Key Technologies:**
- **Languages:** Python, C#/.NET, JavaScript/Node.js
- **Frameworks:** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **Platforms:** Microsoft Foundry, GitHub Models, Hugging Face, Ollama
- **Model Types:** Phi-3, Phi-3.5, Phi-4 (text, vision, multimodal, reasoning variants)

**Repository Structure:**
- `/code/` - Working code examples and sample implementations
- `/md/` - Detailed documentation, tutorials, and how-to guides  
- `/translations/` - Multi-language translations (50+ languages via automated workflow)
- `/.devcontainer/` - Dev container configuration (Python 3.12 with Ollama)

## Development Environment Setup

### Using GitHub Codespaces or Dev Containers (Recommended)

1. Open for GitHub Codespaces (fastest):
   - Click the "Open in GitHub Codespaces" badge inside README
   - Container go auto-configure with Python 3.12 and Ollama with Phi-3

2. Open for VS Code Dev Containers:
   - Use the "Open in Dev Containers" badge from README
   - Container need 16GB host memory minimum

### Local Setup

**Prerequisites:**
- Python 3.12 or later
- .NET 8.0 SDK (for C# examples)
- Node.js 18+ and npm (for JavaScript examples)
- 16GB RAM minimum recommended

**Installation:**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**For Python Examples:**
Go inside specific example directories and install dependencies:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt de kam
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
npm run dev  # Start development server
npm run build  # Build for production
```

## Repository Organization

### Code Examples (`/code/`)

- **01.Introduce/** - Basic introductions and getting started samples
- **03.Finetuning/** and **04.Finetuning/** - Fine-tuning examples with different methods
- **03.Inference/** - Inference examples on different hardware (AIPC, MLX)
- **06.E2E/** - End-to-end application samples
- **07.Lab/** - Laboratory/experimental implementations
- **08.RAG/** - Retrieval-Augmented Generation samples
- **09.UpdateSamples/** - Latest updated samples

### Documentation (`/md/`)

- **01.Introduction/** - Intro guides, environment setup, platform guides
- **02.Application/** - Application samples arranged by type (Text, Code, Vision, Audio, etc.)
- **02.QuickStart/** - Quick start guides for Microsoft Foundry and GitHub Models
- **03.FineTuning/** - Fine-tuning documentation and tutorials
- **04.HOL/** - Hands-on labs (includes .NET examples)

### File Formats

- **Jupyter Notebooks (`.ipynb`)** - Interactive Python tutorials wey dem mark with 📓 inside README
- **Python Scripts (`.py`)** - Standalone Python examples
- **C# Projects (`.csproj`, `.sln`)** - .NET applications and samples
- **JavaScript (`.js`, `package.json`)** - Web-based and Node.js examples
- **Markdown (`.md`)** - Documentation and guides

## Working with Examples

### Running Jupyter Notebooks

Most examples na Jupyter notebooks:
```bash
pip install jupyter notebook
jupyter notebook  # Opɛn di browser interface
# Go enter di .ipynb file wey you want
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

Or build complete solution:
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### Running JavaScript/Web Examples

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development wit hot reload
```

## Testing

Dis repo get example code and tutorials, no be like normal software project wey get unit tests. Validation dey usually done by:

1. **Running the examples** - Make sure each example fit run without wahala
2. **Verifying outputs** - Check say model responses dey correct
3. **Following tutorials** - Step-by-step guides suppose work as e dey document

**Common validation approach:**
- Test execution for the example inside the correct environment
- Verify say all dependencies install well
- Check say model downloads and loads properly
- Confirm say expected behavior match the documentation

## Code Style and Conventions

### General Guidelines

- Examples suppose clear, well-commented, and educational
- Follow language-specific conventions (PEP 8 for Python, C# standards for .NET)
- Make examples dey focus on showing specific Phi model capabilities
- Put comments wey explain key concepts and model-specific parameters

### Documentation Standards

**URL Formatting:**
- Use `[text](../../url)` format without extra spaces
- Relative links: Use `./` for current directory, `../` for parent
- No country-specific locales inside URLs (no use `/en-us/`, `/en/`)

**Images:**
- Keep all images for `/imgs/` directory
- Use descriptive names wey get English characters, numbers, and dashes
- Example: `phi-3-architecture.png`

**Markdown Files:**
- Reference actual working examples inside `/code/` directory
- Keep documentation sabi with code updates
- Use 📓 emoji to show Jupyter notebook links inside README

### File Organization

- Code examples inside `/code/` arranged by topic/feature
- Documentation for `/md/` dey mirror code structure if e apply
- Keep related files (notebooks, scripts, configs) together inside subdirectories

## Pull Request Guidelines

### Before Submitting

1. **Fork the repository** go your own account
2. **Separate PRs by type:**
   - Bug fixes for one PR
   - Documentation updates for another
   - New examples for separate PRs
   - Typo fixes fit combine

3. **Handle merge conflicts:**
   - Update your local `main` branch before you do changes
   - Sync with upstream often

4. **Translation PRs:**
   - Must get translations for ALL files inside the folder
   - Keep structure same as original language

### Required Checks

PRs dey automatically run GitHub workflows to check:

1. **Relative path validation** - All internal links suppose work well
   - Test links local: Ctrl+Click for VS Code
   - Use path suggestions from VS Code (`./` or `../`)

2. **URL locale check** - Web URLs no suppose get country locales
   - Remove `/en-us/`, `/en/`, or other language codes
   - Use generic international URLs

3. **Broken URL check** - All URLs must return 200 status code
   - Verify links dey accessible before you submit
   - Note: Some failure fit be because network restrictions

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
- Examples dey use different frameworks: Transformers, ONNX Runtime, MLX, OpenVINO
- Models dey mostly download from Hugging Face, Azure, or GitHub Models
- Check model compatibility with your hardware (CPU, GPU, NPU)

**Inference Patterns:**
- Text generation: Most examples dey use chat/instruct variants
- Vision: Phi-3-vision and Phi-4-multimodal for image understanding
- Audio: Phi-4-multimodal support audio inputs
- Reasoning: Phi-4-reasoning variants for advanced reasoning tasks

### Platform-Specific Notes

**Microsoft Foundry:**
- You need Azure subscription and API keys
- See `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Get free tier for testing
- See `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Local Inference:**
- ONNX Runtime: Cross-platform, optimized inference
- Ollama: Easy local model management (pre-configured in dev container)
- Apple MLX: Optimized for Apple Silicon

## Troubleshooting

### Common Issues

**Memory Issues:**
- Phi models need plenty RAM (especially vision/multimodal variants)
- Use quantized models for resource-constrained environments
- See `/md/01.Introduction/04/QuantifyingPhi.md`

**Dependency Conflicts:**
- Python examples fit get specific version requirements
- Use virtual environments for each example
- Check individual `requirements.txt` files

**Model Download Failures:**
- Big models fit timeout on slow connections
- Consider using cloud environments (Codespaces, Azure)
- Check Hugging Face cache: `~/.cache/huggingface/`

**.NET Project Issues:**
- Make sure .NET 8.0 SDK dey installed
- Use `dotnet restore` before you build
- Some projects get CUDA-specific configurations (Debug_Cuda)

**JavaScript/Web Examples:**
- Use Node.js 18+ for compatibility
- Clear `node_modules` and reinstall if yawa still dey
- Check browser console for WebGPU compatibility issues

### Getting Help

- **Discord:** Join the Microsoft Foundry Community Discord
- **GitHub Issues:** Report bugs and issues inside the repo
- **GitHub Discussions:** Ask questions and share knowledge

## Additional Context

### Responsible AI

All Phi model usage suppose follow Microsoft's Responsible AI principles:
- Fairness, reliability, safety
- Privacy and security  
- Inclusiveness, transparency, accountability
- Use Azure AI Content Safety for production applications
- See `/md/01.Introduction/01/01.AISafety.md`

### Translations

- 50+ languages dey supported via automated GitHub Action
- Translations dey for `/translations/` directory
- Maintained by co-op-translator workflow
- No make you edit translated files manually (auto-generated)

### Contributing

- Follow guidelines for `CONTRIBUTING.md`
- Agree to Contributor License Agreement (CLA)
- Follow Microsoft Open Source Code of Conduct
- Keep security and credentials outside your commits

### Multi-Language Support

Dis na polyglot repo with examples for:
- **Python** - ML/AI workflows, Jupyter notebooks, fine-tuning
- **C#/.NET** - Enterprise applications, ONNX Runtime integration
- **JavaScript** - Web-based AI, browser inference with WebGPU

Choose the language wey fit your use case and deployment target well well.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translation fit get errors or mistakes. Di original document wey dey im native language na di correct source. For important info, e better make person wey sabi translate human translation. We no go responsible for any misunderstanding or wrong interpretation wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->