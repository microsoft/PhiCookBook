<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-07T14:09:57+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "zh"
}
-->
# Phi-3.5-Instruct WebGPU RAG 聊天机器人

## 展示 WebGPU 和 RAG 模式的演示

结合 Phi-3.5 Onnx 托管模型的 RAG 模式采用了检索增强生成（Retrieval-Augmented Generation）方法，将 Phi-3.5 模型的强大能力与 ONNX 托管结合，实现高效的 AI 部署。该模式对于针对特定领域任务进行模型微调非常有帮助，兼顾了质量、成本效益和长上下文理解能力。它是 Azure AI 套件的一部分，提供了丰富的模型选择，方便查找、试用和应用，满足各行各业的定制化需求。

## 什么是 WebGPU  
WebGPU 是一款现代网页图形 API，旨在让网页浏览器能够高效直接访问设备的图形处理单元（GPU）。它被设计为 WebGL 的继任者，带来了多项关键改进：

1. **兼容现代 GPU**：WebGPU 可无缝支持当前主流 GPU 架构，利用 Vulkan、Metal 和 Direct3D 12 等系统 API。
2. **性能提升**：支持通用 GPU 计算和更快速的操作，适用于图形渲染和机器学习任务。
3. **高级功能**：提供更丰富的 GPU 功能访问，支持更复杂且动态的图形和计算工作负载。
4. **减轻 JavaScript 负担**：通过将更多任务转移到 GPU，WebGPU 大幅减少了 JavaScript 的工作量，提升性能和流畅度。

目前，WebGPU 已在 Google Chrome 等浏览器中支持，相关工作正在推进以扩展至更多平台。

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

#### 访问 Flags 页面：  
在地址栏输入 `chrome://flags` 并回车。

#### 搜索标志：  
在页面顶部的搜索框输入 'enable-unsafe-webgpu'。

#### 启用标志：  
在结果列表中找到 #enable-unsafe-webgpu 标志。

点击其旁边的下拉菜单，选择 Enabled。

#### 重启浏览器：

启用标志后，需要重启浏览器使更改生效。点击页面底部出现的 Relaunch 按钮。

- Linux 用户请使用 `--enable-features=Vulkan` 启动浏览器。  
- Safari 18（macOS 15）默认启用 WebGPU。  
- Firefox Nightly 中，在地址栏输入 about:config 并 `set dom.webgpu.enabled to true`。

### 为 Microsoft Edge 设置 GPU  

以下是在 Windows 上为 Microsoft Edge 设置高性能 GPU 的步骤：

- **打开设置：** 点击开始菜单，选择 设置。  
- **系统设置：** 进入 系统，然后选择 显示。  
- **图形设置：** 向下滚动，点击 图形设置。  
- **选择应用：** 在“选择要设置偏好的应用”下，选择 桌面应用，然后点击 浏览。  
- **选择 Edge：** 定位到 Edge 安装文件夹（通常为 `C:\Program Files (x86)\Microsoft\Edge\Application`），选择 `msedge.exe`。  
- **设置偏好：** 点击 选项，选择 高性能，然后点击 保存。  
这样可以确保 Microsoft Edge 使用高性能 GPU 来提升性能。  
- **重启** 计算机以使设置生效。

### 示例：请点击[此链接](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。虽然我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或曲解，我们概不负责。