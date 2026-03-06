# AGENTS.md

## Project Overview

PhiCookBook 是一个综合性的食谱仓库，包含了使用微软 Phi 系列小型语言模型（SLMs）的实践示例、教程和文档。该仓库展示了多种用例，包括推理、微调、量化、RAG 实现以及跨不同平台和框架的多模态应用。

**关键技术：**
- **语言：** Python、C#/.NET、JavaScript/Node.js
- **框架：** ONNX Runtime、PyTorch、Transformers、MLX、OpenVINO、Semantic Kernel
- **平台：** Microsoft Foundry、GitHub Models、Hugging Face、Ollama
- **模型类型：** Phi-3、Phi-3.5、Phi-4（文本、视觉、多模态、推理变体）

**仓库结构：**
- `/code/` - 工作代码示例和示范实现
- `/md/` - 详细文档、教程和操作指南  
- `/translations/` - 多语言翻译（通过自动化工作流支持50多种语言）
- `/.devcontainer/` - 开发容器配置（Python 3.12 + Ollama）

## Development Environment Setup

### Using GitHub Codespaces or Dev Containers (Recommended)

1. Open in GitHub Codespaces (fastest):
   - Click the "Open in GitHub Codespaces" badge in README
   - Container auto-configures with Python 3.12 and Ollama with Phi-3

2. Open in VS Code Dev Containers:
   - Use the "Open in Dev Containers" badge from README
   - Container requires 16GB host memory minimum

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
Navigate to specific example directories and install dependencies:
```bash
cd code/<example-directory>
pip install -r requirements.txt  # 如果 requirements.txt 存在
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
npm run dev  # 启动开发服务器
npm run build  # 生产环境构建
```

## Repository Organization

### Code Examples (`/code/`)

- **01.Introduce/** - 基础介绍和入门示例
- **03.Finetuning/** 和 **04.Finetuning/** - 各类微调示例
- **03.Inference/** - 不同硬件（AIPC、MLX）上的推理示例
- **06.E2E/** - 端到端应用示例
- **07.Lab/** - 实验室/实验性实现
- **08.RAG/** - 检索增强生成示例
- **09.UpdateSamples/** - 最新更新示例

### Documentation (`/md/`)

- **01.Introduction/** - 介绍指南、环境搭建、平台指引
- **02.Application/** - 按类型组织的应用示例（文本、代码、视觉、音频等）
- **02.QuickStart/** - Microsoft Foundry 和 GitHub Models 快速启动指南
- **03.FineTuning/** - 微调文档和教程
- **04.HOL/** - 实战实验室（包括 .NET 示例）

### File Formats

- **Jupyter Notebooks (`.ipynb`)** - 交互式 Python 教程，README 中标记有 📓
- **Python Scripts (`.py`)** - 独立的 Python 示例
- **C# Projects (`.csproj`, `.sln`)** - .NET 应用及示例
- **JavaScript (`.js`, `package.json`)** - 基于网页和 Node.js 的示例
- **Markdown (`.md`)** - 文档和指南

## Working with Examples

### Running Jupyter Notebooks

Most examples are provided as Jupyter notebooks:
```bash
pip install jupyter notebook
jupyter notebook  # 打开浏览器界面
# 导航到所需的 .ipynb 文件
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
npm run dev  # 支持热重载的开发
```

## Testing

This repository contains example code and tutorials rather than a traditional software project with unit tests. Validation is typically done by:

1. **Running the examples** - Each example should execute without errors
2. **Verifying outputs** - Check that model responses are appropriate
3. **Following tutorials** - Step-through guides should work as documented

**Common validation approach:**
- Test example execution in the target environment
- Verify dependencies install correctly
- Check that model downloads/loads successfully
- Confirm expected behavior matches documentation

## Code Style and Conventions

### General Guidelines

- Examples should be clear, well-commented, and educational
- Follow language-specific conventions (PEP 8 for Python, C# standards for .NET)
- Keep examples focused on demonstrating specific Phi model capabilities
- Include comments explaining key concepts and model-specific parameters

### Documentation Standards

**URL Formatting:**
- Use `[text](../../url)` format without extra spaces
- Relative links: Use `./` for current directory, `../` for parent
- No country-specific locales in URLs (avoid `/en-us/`, `/en/`)

**Images:**
- Store all images in `/imgs/` directory
- Use descriptive names with English characters, numbers, and dashes
- Example: `phi-3-architecture.png`

**Markdown Files:**
- Reference actual working examples in `/code/` directory
- Keep documentation synchronized with code changes
- Use 📓 emoji to mark Jupyter notebook links in README

### File Organization

- Code examples in `/code/` organized by topic/feature
- Documentation in `/md/` mirrors code structure when applicable
- Keep related files (notebooks, scripts, configs) together in subdirectories

## Pull Request Guidelines

### Before Submitting

1. **Fork the repository** to your account
2. **Separate PRs by type:**
   - Bug fixes in one PR
   - Documentation updates in another
   - New examples in separate PRs
   - Typo fixes can be combined

3. **Handle merge conflicts:**
   - Update your local `main` branch before making changes
   - Sync with upstream frequently

4. **Translation PRs:**
   - Must include translations for ALL files in the folder
   - Maintain consistent structure with original language

### Required Checks

PRs automatically run GitHub workflows to validate:

1. **Relative path validation** - All internal links must work
   - Test links locally: Ctrl+Click in VS Code
   - Use path suggestions from VS Code (`./` or `../`)

2. **URL locale check** - Web URLs must not contain country locales
   - Remove `/en-us/`, `/en/`, or other language codes
   - Use generic international URLs

3. **Broken URL check** - All URLs must return 200 status
   - Verify links are accessible before submitting
   - Note: Some failures may be due to network restrictions

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
- Examples use various frameworks: Transformers, ONNX Runtime, MLX, OpenVINO
- Models are typically downloaded from Hugging Face, Azure, or GitHub Models
- Check model compatibility with your hardware (CPU, GPU, NPU)

**Inference Patterns:**
- Text generation: Most examples use chat/instruct variants
- Vision: Phi-3-vision and Phi-4-multimodal for image understanding
- Audio: Phi-4-multimodal supports audio inputs
- Reasoning: Phi-4-reasoning variants for advanced reasoning tasks

### Platform-Specific Notes

**Microsoft Foundry:**
- Requires Azure subscription and API keys
- See `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models:**
- Free tier available for testing
- See `/md/02.QuickStart/GitHubModel_QuickStart.md`

**Local Inference:**
- ONNX Runtime: Cross-platform, optimized inference
- Ollama: Easy local model management (pre-configured in dev container)
- Apple MLX: Optimized for Apple Silicon

## Troubleshooting

### Common Issues

**Memory Issues:**
- Phi models require significant RAM (especially vision/multimodal variants)
- Use quantized models for resource-constrained environments
- See `/md/01.Introduction/04/QuantifyingPhi.md`

**Dependency Conflicts:**
- Python examples may have specific version requirements
- Use virtual environments for each example
- Check individual `requirements.txt` files

**Model Download Failures:**
- Large models may timeout on slow connections
- Consider using cloud environments (Codespaces, Azure)
- Check Hugging Face cache: `~/.cache/huggingface/`

**.NET Project Issues:**
- Ensure .NET 8.0 SDK is installed
- Use `dotnet restore` before building
- Some projects have CUDA-specific configurations (Debug_Cuda)

**JavaScript/Web Examples:**
- Use Node.js 18+ for compatibility
- Clear `node_modules` and reinstall if issues persist
- Check browser console for WebGPU compatibility issues

### Getting Help

- **Discord:** Join the Microsoft Foundry Community Discord
- **GitHub Issues:** Report bugs and issues in the repository
- **GitHub Discussions:** Ask questions and share knowledge

## Additional Context

### Responsible AI

All Phi model usage should follow Microsoft's Responsible AI principles:
- Fairness, reliability, safety
- Privacy and security  
- Inclusiveness, transparency, accountability
- Use Azure AI Content Safety for production applications
- See `/md/01.Introduction/01/01.AISafety.md`

### Translations

- 50+ languages supported via automated GitHub Action
- Translations in `/translations/` directory
- Maintained by co-op-translator workflow
- Do not manually edit translated files (auto-generated)

### Contributing

- Follow guidelines in `CONTRIBUTING.md`
- Agree to Contributor License Agreement (CLA)
- Adhere to Microsoft Open Source Code of Conduct
- Keep security and credentials out of commits

### Multi-Language Support

This is a polyglot repository with examples in:
- **Python** - ML/AI workflows, Jupyter notebooks, fine-tuning
- **C#/.NET** - Enterprise applications, ONNX Runtime integration
- **JavaScript** - Web-based AI, browser inference with WebGPU

Choose the language that best fits your use case and deployment target.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由人工智能翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。尽管我们努力确保准确性，但请注意自动翻译可能包含错误或不准确之处。原始的母语版本文件应被视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->