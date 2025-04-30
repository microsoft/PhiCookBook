<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c7a7f2a07dc176c19e1ab9f249b548c9",
  "translation_date": "2025-04-03T06:28:33+00:00",
  "source_file": "code\\08.RAG\\rag_webgpu_chat\\README.md",
  "language_code": "zh"
}
-->
Phi-3-mini WebGPU RAG 聊天机器人

## 展示 WebGPU 和 RAG 模式的演示
基于 Phi-3 Onnx 托管模型的 RAG 模式利用了检索增强生成（Retrieval-Augmented Generation）方法，将 Phi-3 模型的强大能力与 ONNX 托管相结合，实现高效的 AI 部署。这种模式在针对特定领域任务进行模型微调时尤为重要，提供了质量、成本效益和长上下文理解的平衡。它是 Azure AI 套件的一部分，提供了广泛的模型选择，便于查找、试用和使用，满足各行业的定制需求。Phi-3 系列模型，包括 Phi-3-mini、Phi-3-small 和 Phi-3-medium，可在 Azure AI 模型目录中找到，并可通过自托管或 HuggingFace 和 ONNX 平台进行微调和部署，展示了微软致力于提供可访问且高效的 AI 解决方案的承诺。

## 什么是 WebGPU
WebGPU 是一种现代化的网页图形 API，旨在从网络浏览器直接高效访问设备的图形处理单元（GPU）。它被设计为 WebGL 的继任者，并提供了以下几个关键改进：

1. **与现代 GPU 的兼容性**：WebGPU 专为当代 GPU 架构设计，利用 Vulkan、Metal 和 Direct3D 12 等系统 API 实现无缝协作。
2. **性能提升**：支持通用 GPU 计算和更快的操作，适用于图形渲染和机器学习任务。
3. **高级功能**：提供对更高级 GPU 功能的访问，支持更复杂和动态的图形及计算工作负载。
4. **减少 JavaScript 工作量**：通过将更多任务交给 GPU 处理，大幅减轻 JavaScript 的工作负担，从而提升性能并带来更流畅的体验。

目前，WebGPU 已在 Google Chrome 等浏览器中得到支持，且正在努力扩展到其他平台。

### 03.WebGPU
所需环境：

**支持的浏览器：**
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18（macOS 15）
- Firefox Nightly。

### 启用 WebGPU：

- 在 Chrome/Microsoft Edge 中

启用 `chrome://flags/#enable-unsafe-webgpu` 标志。

#### 打开浏览器：
启动 Google Chrome 或 Microsoft Edge。

#### 访问 Flags 页面：
在地址栏中输入 `chrome://flags`，然后按 Enter。

#### 搜索标志：
在页面顶部的搜索框中输入“enable-unsafe-webgpu”。

#### 启用标志：
在搜索结果中找到 #enable-unsafe-webgpu 标志。

点击旁边的下拉菜单并选择 Enabled。

#### 重启浏览器：
启用标志后，需要重启浏览器以使更改生效。点击页面底部出现的 Relaunch 按钮。

- 对于 Linux，使用 `--enable-features=Vulkan` 启动浏览器。
- Safari 18（macOS 15）默认启用 WebGPU。
- 在 Firefox Nightly 中，进入地址栏输入 about:config 并 `set dom.webgpu.enabled to true`。

### 为 Microsoft Edge 设置 GPU

以下是在 Windows 上为 Microsoft Edge 设置高性能 GPU 的步骤：

- **打开设置：** 点击开始菜单并选择设置。
- **系统设置：** 进入系统，然后选择显示。
- **图形设置：** 向下滚动并点击图形设置。
- **选择应用程序：** 在“选择一个应用程序设置偏好”下，选择桌面应用程序，然后点击浏览。
- **选择 Edge：** 导航到 Edge 的安装文件夹（通常为 `C:\Program Files (x86)\Microsoft\Edge\Application`），然后选择 `msedge.exe`。
- **设置偏好：** 点击选项，选择高性能，然后点击保存。
这将确保 Microsoft Edge 使用高性能 GPU，以获得更好的性能。
- **重启** 计算机以使设置生效。

### 打开你的 Codespace：
导航到 GitHub 上的存储库。
点击 Code 按钮并选择 Open with Codespaces。

如果你还没有 Codespace，可以点击 New codespace 创建一个。

**注意** 在你的 Codespace 中安装 Node 环境
从 GitHub Codespace 运行 npm 演示是测试和开发项目的好方法。以下是帮助你开始的分步指南：

### 设置环境：
打开 Codespace 后，确保已安装 Node.js 和 npm。你可以通过运行以下命令检查：
```
node -v
```
```
npm -v
```

如果尚未安装，可以使用以下命令安装：
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### 导航到项目目录：
使用终端导航到你的 npm 项目所在的目录：
```
cd path/to/your/project
```

### 安装依赖：
运行以下命令安装 package.json 文件中列出的所有必要依赖：

```
npm install
```

### 运行演示：
安装依赖后，你可以运行演示脚本。通常在 package.json 的 scripts 部分指定。例如，如果演示脚本名为 start，可以运行：

```
npm run build
```
```
npm run dev
```

### 访问演示：
如果演示涉及到一个 Web 服务器，Codespaces 将提供一个 URL 来访问它。请查看通知或检查 Ports 标签以找到 URL。

**注意：** 模型需要在浏览器中缓存，因此加载可能需要一些时间。

### RAG 演示
上传 markdown 文件 `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### 选择文件：
点击“选择文件”按钮，选择你想上传的文档。

### 上传文档：
选择文件后，点击“上传”按钮，将文档加载到 RAG（检索增强生成）中。

### 开始聊天：
文档上传后，你可以基于文档内容开始一个 RAG 聊天会话。

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原文档的母语版本应被视为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而导致的任何误解或错误解释，我们概不负责。