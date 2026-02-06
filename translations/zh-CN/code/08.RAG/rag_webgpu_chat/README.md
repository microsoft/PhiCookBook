Phi-3-mini WebGPU RAG 聊天机器人

## 展示 WebGPU 和 RAG 模式的演示
结合 Phi-3 Onnx 托管模型的 RAG 模式利用了检索增强生成（Retrieval-Augmented Generation）方法，将 Phi-3 模型的强大能力与 ONNX 托管相结合，实现高效的 AI 部署。该模式在针对特定领域任务的模型微调中发挥重要作用，兼顾了质量、成本效益和长上下文理解能力。它是 Azure AI 套件的一部分，提供了丰富的模型选择，方便查找、试用和使用，满足各行业的定制化需求。Phi-3 系列模型，包括 Phi-3-mini、Phi-3-small 和 Phi-3-medium，均可在 Azure AI 模型目录中找到，支持自主管理微调和部署，也可通过 HuggingFace 和 ONNX 等平台使用，体现了微软致力于提供易用高效 AI 解决方案的承诺。

## 什么是 WebGPU
WebGPU 是一种现代网页图形 API，旨在直接从浏览器高效访问设备的图形处理单元（GPU）。它被设计为 WebGL 的继任者，带来了多项关键改进：

1. **兼容现代 GPU**：WebGPU 兼容当代 GPU 架构，利用 Vulkan、Metal 和 Direct3D 12 等系统 API。
2. **性能提升**：支持通用 GPU 计算和更快的操作，适用于图形渲染和机器学习任务。
3. **高级功能**：提供更丰富的 GPU 功能，支持更复杂和动态的图形及计算工作负载。
4. **减少 JavaScript 负担**：通过将更多任务交给 GPU，显著减轻 JavaScript 的工作量，提升性能和流畅度。

目前，WebGPU 已在 Google Chrome 等浏览器中支持，正在逐步扩展到其他平台。

### 03.WebGPU
所需环境：

**支持的浏览器：**  
- Google Chrome 113 及以上  
- Microsoft Edge 113 及以上  
- Safari 18（macOS 15）  
- Firefox Nightly  

### 启用 WebGPU：

- 在 Chrome/Microsoft Edge 中

启用 `chrome://flags/#enable-unsafe-webgpu` 标志。

#### 打开浏览器：
启动 Google Chrome 或 Microsoft Edge。

#### 进入 Flags 页面：
在地址栏输入 `chrome://flags` 并回车。

#### 搜索标志：
在页面顶部的搜索框输入 'enable-unsafe-webgpu'

#### 启用标志：
在结果列表中找到 #enable-unsafe-webgpu 标志。

点击其旁边的下拉菜单，选择 Enabled。

#### 重启浏览器：

启用标志后，需要重启浏览器使更改生效。点击页面底部出现的 Relaunch 按钮。

- Linux 用户请使用 `--enable-features=Vulkan` 启动浏览器。  
- Safari 18（macOS 15）默认启用 WebGPU。  
- Firefox Nightly 中，在地址栏输入 about:config，将 `dom.webgpu.enabled` 设置为 true。

### 为 Microsoft Edge 设置 GPU

以下是在 Windows 上为 Microsoft Edge 配置高性能 GPU 的步骤：

- **打开设置：** 点击开始菜单，选择设置。  
- **系统设置：** 进入系统，然后选择显示。  
- **图形设置：** 向下滚动，点击图形设置。  
- **选择应用：** 在“选择要设置偏好的应用”下，选择桌面应用，然后点击浏览。  
- **选择 Edge：** 定位到 Edge 安装目录（通常是 `C:\Program Files (x86)\Microsoft\Edge\Application`），选择 `msedge.exe`。  
- **设置偏好：** 点击选项，选择高性能，然后点击保存。  
这样可以确保 Microsoft Edge 使用高性能 GPU 以获得更佳性能。  
- **重启** 电脑以使设置生效。

### 打开你的 Codespace：
进入你的 GitHub 仓库。  
点击 Code 按钮，选择 Open with Codespaces。

如果还没有 Codespace，可以点击 New codespace 创建一个。

**注意** 在你的 Codespace 中安装 Node 环境  
从 GitHub Codespace 运行 npm 演示是测试和开发项目的好方法。以下是入门步骤：

### 设置环境：
打开 Codespace 后，确保已安装 Node.js 和 npm。可通过运行以下命令检查：  
```
node -v
```  
```
npm -v
```

如果未安装，可以使用以下命令安装：  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### 进入项目目录：
使用终端进入你的 npm 项目所在目录：  
```
cd path/to/your/project
```

### 安装依赖：
运行以下命令安装 package.json 中列出的所有依赖：  

```
npm install
```

### 运行演示：
依赖安装完成后，可以运行演示脚本。通常在 package.json 的 scripts 部分定义，例如脚本名为 start，则运行：  

```
npm run build
```  
```
npm run dev
```

### 访问演示：
如果演示包含 Web 服务器，Codespaces 会提供访问 URL。请留意通知或查看 Ports 标签页获取链接。

**注意：** 模型需要在浏览器缓存，因此加载可能需要一些时间。

### RAG 演示
上传 markdown 文件 `intro_rag.md` 以完成 RAG 解决方案。如果使用 Codespaces，可下载位于 `01.InferencePhi3/docs/` 的文件。

### 选择文件：
点击“Choose File”按钮，选择要上传的文档。

### 上传文档：
选择文件后，点击“Upload”按钮加载文档以进行 RAG（检索增强生成）。

### 开始聊天：
文档上传完成后，即可基于文档内容开始 RAG 聊天会话。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。