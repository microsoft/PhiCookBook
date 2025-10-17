<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "72e00a4ddbe9d6c25907d1eb19d041b8",
  "translation_date": "2025-10-17T10:48:44+00:00",
  "source_file": "AGENTS.md",
  "language_code": "zh"
}
-->
# AGENTS.md

## 项目概述

PhiCookBook 是一个全面的食谱库，包含关于使用微软 Phi 系列小型语言模型 (SLMs) 的实践示例、教程和文档。该库展示了多种使用场景，包括推理、微调、量化、RAG 实现以及跨不同平台和框架的多模态应用。

**关键技术：**
- **语言：** Python, C#/.NET, JavaScript/Node.js
- **框架：** ONNX Runtime, PyTorch, Transformers, MLX, OpenVINO, Semantic Kernel
- **平台：** Azure AI Foundry, GitHub Models, Hugging Face, Ollama
- **模型类型：** Phi-3, Phi-3.5, Phi-4（文本、视觉、多模态、推理变体）

**库结构：**
- `/code/` - 工作代码示例和样本实现
- `/md/` - 详细文档、教程和操作指南  
- `/translations/` - 多语言翻译（通过自动化工作流支持50多种语言）
- `/.devcontainer/` - 开发容器配置（Python 3.12，带 Ollama）

## 开发环境设置

### 使用 GitHub Codespaces 或开发容器（推荐）

1. 在 GitHub Codespaces 中打开（最快）：
   - 点击 README 中的 "Open in GitHub Codespaces" 徽章
   - 容器会自动配置 Python 3.12 和带有 Phi-3 的 Ollama

2. 在 VS Code 开发容器中打开：
   - 使用 README 中的 "Open in Dev Containers" 徽章
   - 容器需要至少 16GB 主机内存

### 本地设置

**前提条件：**
- Python 3.12 或更高版本
- .NET 8.0 SDK（用于 C# 示例）
- Node.js 18+ 和 npm（用于 JavaScript 示例）
- 推荐至少 16GB RAM

**安装：**
```bash
git clone https://github.com/microsoft/PhiCookBook.git
cd PhiCookBook
```

**对于 Python 示例：**
导航到特定示例目录并安装依赖项：
```bash
cd code/<example-directory>
pip install -r requirements.txt  # if requirements.txt exists
```

**对于 .NET 示例：**
```bash
cd md/04.HOL/dotnet/src
dotnet restore LabsPhi.sln
dotnet build LabsPhi.sln
```

**对于 JavaScript/Web 示例：**
```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Start development server
npm run build  # Build for production
```


## 库组织结构

### 代码示例 (`/code/`)

- **01.Introduce/** - 基础介绍和入门示例
- **03.Finetuning/** 和 **04.Finetuning/** - 使用各种方法的微调示例
- **03.Inference/** - 在不同硬件（AIPC、MLX）上的推理示例
- **06.E2E/** - 端到端应用示例
- **07.Lab/** - 实验室/实验性实现
- **08.RAG/** - 检索增强生成示例
- **09.UpdateSamples/** - 最新更新的示例

### 文档 (`/md/`)

- **01.Introduction/** - 介绍指南、环境设置、平台指南
- **02.Application/** - 按类型组织的应用示例（文本、代码、视觉、音频等）
- **02.QuickStart/** - Azure AI Foundry 和 GitHub Models 的快速入门指南
- **03.FineTuning/** - 微调文档和教程
- **04.HOL/** - 实践实验室（包括 .NET 示例）

### 文件格式

- **Jupyter Notebooks (`.ipynb`)** - README 中标记为 📓 的交互式 Python 教程
- **Python Scripts (`.py`)** - 独立的 Python 示例
- **C# Projects (`.csproj`, `.sln`)** - .NET 应用和示例
- **JavaScript (`.js`, `package.json`)** - 基于 Web 和 Node.js 的示例
- **Markdown (`.md`)** - 文档和指南

## 使用示例

### 运行 Jupyter Notebooks

大多数示例以 Jupyter Notebooks 提供：
```bash
pip install jupyter notebook
jupyter notebook  # Opens browser interface
# Navigate to desired .ipynb file
```

### 运行 Python 脚本

```bash
cd code/<example-directory>
pip install -r requirements.txt
python <script-name>.py
```

### 运行 .NET 示例

```bash
cd md/04.HOL/dotnet/src/<project-name>
dotnet run
```

或者构建整个解决方案：
```bash
cd md/04.HOL/dotnet/src
dotnet run --project <project-name>
```

### 运行 JavaScript/Web 示例

```bash
cd code/08.RAG/rag_webgpu_chat
npm install
npm run dev  # Development with hot reload
```


## 测试

此库包含示例代码和教程，而不是传统的软件项目单元测试。验证通常通过以下方式进行：

1. **运行示例** - 每个示例应无错误地执行
2. **验证输出** - 检查模型响应是否合适
3. **遵循教程** - 按文档操作指南逐步执行

**常见验证方法：**
- 在目标环境中测试示例执行
- 验证依赖项是否正确安装
- 检查模型是否成功下载/加载
- 确认预期行为与文档一致

## 代码风格和规范

### 通用指南

- 示例应清晰、注释充分且具有教育意义
- 遵循特定语言的规范（Python 使用 PEP 8，.NET 使用 C# 标准）
- 示例应专注于展示特定 Phi 模型的功能
- 包含解释关键概念和模型特定参数的注释

### 文档标准

**URL 格式：**
- 使用 `[text](../../url)` 格式，不要有额外空格
- 相对链接：当前目录使用 `./`，父目录使用 `../`
- URL 中不要包含国家/地区特定语言代码（避免 `/en-us/`，`/en/`）

**图片：**
- 所有图片存储在 `/imgs/` 目录
- 使用英文字符、数字和短横线的描述性名称
- 示例：`phi-3-architecture.png`

**Markdown 文件：**
- 参考 `/code/` 目录中的实际工作示例
- 确保文档与代码更改同步
- 在 README 中使用 📓 表情符号标记 Jupyter Notebook 链接

### 文件组织

- `/code/` 中的代码示例按主题/功能组织
- `/md/` 中的文档在适用时与代码结构保持一致
- 将相关文件（notebooks、scripts、configs）放在子目录中

## Pull Request 指南

### 提交前

1. **Fork 仓库** 到你的账户
2. **按类型分离 PR：**
   - Bug 修复放在一个 PR 中
   - 文档更新放在另一个 PR 中
   - 新示例放在单独的 PR 中
   - 拼写错误修复可以合并

3. **处理合并冲突：**
   - 在进行更改之前更新本地 `main` 分支
   - 经常与上游同步

4. **翻译 PR：**
   - 必须包含文件夹中所有文件的翻译
   - 保持与原语言一致的结构

### 必要检查

PR 会自动运行 GitHub 工作流以验证：

1. **相对路径验证** - 所有内部链接必须有效
   - 在本地测试链接：在 VS Code 中按 Ctrl+Click
   - 使用 VS Code 的路径建议（`./` 或 `../`）

2. **URL 语言代码检查** - Web URL 不得包含国家/地区语言代码
   - 删除 `/en-us/`，`/en/` 或其他语言代码
   - 使用通用国际 URL

3. **无效 URL 检查** - 所有 URL 必须返回 200 状态码
   - 提交前验证链接是否可访问
   - 注意：某些失败可能由于网络限制

### PR 标题格式

```
[component] Brief description
```

示例：
- `[docs] 添加 Phi-4 推理教程`
- `[code] 修复 ONNX Runtime 集成示例`
- `[translation] 添加介绍指南的日语翻译`

## 常见开发模式

### 使用 Phi 模型

**模型加载：**
- 示例使用各种框架：Transformers, ONNX Runtime, MLX, OpenVINO
- 模型通常从 Hugging Face、Azure 或 GitHub Models 下载
- 检查模型与硬件（CPU、GPU、NPU）的兼容性

**推理模式：**
- 文本生成：大多数示例使用聊天/指令变体
- 视觉：Phi-3-vision 和 Phi-4-multimodal 用于图像理解
- 音频：Phi-4-multimodal 支持音频输入
- 推理：Phi-4-reasoning 变体用于高级推理任务

### 平台特定注意事项

**Azure AI Foundry：**
- 需要 Azure 订阅和 API 密钥
- 参见 `/md/02.QuickStart/AzureAIFoundry_QuickStart.md`

**GitHub Models：**
- 免费层可用于测试
- 参见 `/md/02.QuickStart/GitHubModel_QuickStart.md`

**本地推理：**
- ONNX Runtime：跨平台优化推理
- Ollama：轻松管理本地模型（开发容器中预配置）
- Apple MLX：针对 Apple Silicon 优化

## 故障排除

### 常见问题

**内存问题：**
- Phi 模型需要大量 RAM（尤其是视觉/多模态变体）
- 对于资源受限环境，使用量化模型
- 参见 `/md/01.Introduction/04/QuantifyingPhi.md`

**依赖冲突：**
- Python 示例可能有特定版本要求
- 为每个示例使用虚拟环境
- 检查单独的 `requirements.txt` 文件

**模型下载失败：**
- 大型模型可能在慢速连接上超时
- 考虑使用云环境（Codespaces、Azure）
- 检查 Hugging Face 缓存：`~/.cache/huggingface/`

**.NET 项目问题：**
- 确保安装了 .NET 8.0 SDK
- 在构建之前使用 `dotnet restore`
- 某些项目有 CUDA 特定配置（Debug_Cuda）

**JavaScript/Web 示例：**
- 使用 Node.js 18+ 以确保兼容性
- 清除 `node_modules` 并重新安装以解决问题
- 检查浏览器控制台是否存在 WebGPU 兼容性问题

### 获取帮助

- **Discord：** 加入 Azure AI Foundry 社区 Discord
- **GitHub Issues：** 在仓库中报告错误和问题
- **GitHub Discussions：** 提问并分享知识

## 其他背景信息

### 负责任的 AI

所有 Phi 模型的使用应遵循微软的负责任 AI 原则：
- 公平性、可靠性、安全性
- 隐私和安全  
- 包容性、透明度、问责制
- 生产应用中使用 Azure AI 内容安全
- 参见 `/md/01.Introduction/01/01.AISafety.md`

### 翻译

- 通过自动化 GitHub Action 支持 50 多种语言
- 翻译存储在 `/translations/` 目录
- 由 co-op-translator 工作流维护
- 不要手动编辑翻译文件（自动生成）

### 贡献

- 遵循 `CONTRIBUTING.md` 中的指南
- 同意贡献者许可协议 (CLA)
- 遵守微软开源行为准则
- 不要在提交中包含安全信息和凭证

### 多语言支持

这是一个多语言库，包含以下语言的示例：
- **Python** - ML/AI 工作流、Jupyter Notebooks、微调
- **C#/.NET** - 企业应用、ONNX Runtime 集成
- **JavaScript** - 基于 Web 的 AI，支持 WebGPU 的浏览器推理

选择最适合您的使用场景和部署目标的语言。

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。