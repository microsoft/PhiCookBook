<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "faa063cfc6d50047bbfdb58a90d520ad",
  "translation_date": "2025-04-03T07:38:55+00:00",
  "source_file": "md\\02.Application\\01.TextAndChat\\Phi3\\WebGPUWithPhi35Readme.md",
  "language_code": "zh"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## 展示 WebGPU 和 RAG 模式的演示

基于 Phi-3.5 Onnx 托管模型的 RAG 模式采用了检索增强生成（RAG）方法，将 Phi-3.5 模型的强大能力与 ONNX 托管相结合，实现高效的 AI 部署。这种模式在针对领域特定任务进行模型微调方面非常重要，提供了质量、成本效益和长上下文理解的完美结合。它是 Azure AI 套件的一部分，提供了丰富的模型选择，易于查找、试用和使用，满足不同行业的定制需求。

## 什么是 WebGPU
WebGPU 是一种现代化的网页图形 API，旨在直接通过网页浏览器高效访问设备的图形处理单元（GPU）。它被设计为 WebGL 的继任者，提供了以下几个关键改进：

1. **与现代 GPU 的兼容性**：WebGPU 专为当代 GPU 架构设计，与 Vulkan、Metal 和 Direct3D 12 等系统 API 无缝协作。
2. **性能提升**：支持通用 GPU 计算和更快的操作，适用于图形渲染和机器学习任务。
3. **高级功能**：WebGPU 提供对更高级 GPU 功能的访问，支持更复杂和动态的图形及计算工作负载。
4. **降低 JavaScript 工作负载**：通过将更多任务交给 GPU 处理，WebGPU 大幅减少了 JavaScript 的工作负载，从而提升性能并带来更流畅的体验。

目前，WebGPU 已在 Google Chrome 等浏览器中得到支持，并正在努力扩展到其他平台。

### 03.WebGPU
所需环境：

**支持的浏览器：** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### 启用 WebGPU：

- 在 Chrome/Microsoft Edge 中

启用 `chrome://flags/#enable-unsafe-webgpu` 标志。

#### 打开浏览器：
启动 Google Chrome 或 Microsoft Edge。

#### 访问 Flags 页面：
在地址栏中输入 `chrome://flags` 并按 Enter。

#### 搜索标志：
在页面顶部的搜索框中输入 'enable-unsafe-webgpu'。

#### 启用标志：
在搜索结果中找到 #enable-unsafe-webgpu 标志。

点击旁边的下拉菜单并选择 Enabled。

#### 重启浏览器：

启用标志后，需要重启浏览器以使更改生效。点击页面底部出现的 Relaunch 按钮。

- 对于 Linux，使用 `--enable-features=Vulkan` 启动浏览器。
- Safari 18 (macOS 15) 默认启用 WebGPU。
- 在 Firefox Nightly 中，在地址栏输入 about:config 并 `set dom.webgpu.enabled to true`。

### 在 Microsoft Edge 上设置 GPU

以下是在 Windows 上为 Microsoft Edge 设置高性能 GPU 的步骤：

- **打开设置：** 点击开始菜单并选择设置。
- **系统设置：** 进入系统，然后选择显示。
- **图形设置：** 向下滚动并点击图形设置。
- **选择应用：** 在“选择一个应用以设置偏好”下，选择桌面应用，然后点击浏览。
- **选择 Edge：** 导航到 Edge 安装文件夹（通常为 `C:\Program Files (x86)\Microsoft\Edge\Application`）并选择 `msedge.exe`。
- **设置偏好：** 点击选项，选择高性能，然后点击保存。
确保 Microsoft Edge 使用您的高性能 GPU，以获得更好的性能。
- **重启**您的机器以使这些设置生效。

### 示例：请[点击此链接](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**免责声明**:  
本文档使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们尽力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言版本的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。因使用本翻译而引发的任何误解或误读，我们不承担责任。