<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b62864faf628eb07f5231d4885555198",
  "translation_date": "2025-05-07T14:10:06+00:00",
  "source_file": "md/02.Application/01.TextAndChat/Phi3/WebGPUWithPhi35Readme.md",
  "language_code": "mo"
}
-->
# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo for showcasing WebGPU and RAG Pattern

The RAG Pattern with Phi-3.5 Onnx Hosted model uses the Retrieval-Augmented Generation approach, combining the strengths of Phi-3.5 models with ONNX hosting for efficient AI deployments. This pattern is key for fine-tuning models on domain-specific tasks, offering a balance of quality, cost-effectiveness, and long-context understanding. It’s part of Azure AI’s collection, providing a wide range of models that are easy to find, try, and use, meeting the customization needs of various industries.

## What is WebGPU  
WebGPU is a modern web graphics API designed to give efficient access to a device’s graphics processing unit (GPU) directly from web browsers. It aims to replace WebGL, offering several important improvements:

1. **Compatibility with Modern GPUs**: WebGPU is designed to work smoothly with current GPU architectures, using system APIs like Vulkan, Metal, and Direct3D 12.  
2. **Enhanced Performance**: It supports general-purpose GPU computations and faster operations, making it ideal for both graphics rendering and machine learning tasks.  
3. **Advanced Features**: WebGPU grants access to more advanced GPU capabilities, enabling more complex and dynamic graphics and computational workloads.  
4. **Reduced JavaScript Workload**: By shifting more tasks to the GPU, WebGPU significantly lowers the load on JavaScript, resulting in better performance and smoother experiences.

WebGPU is currently supported in browsers such as Google Chrome, with ongoing efforts to extend support to other platforms.

### 03.WebGPU  
Required Environment:

**Supported browsers:**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18 (macOS 15)  
- Firefox Nightly.

### Enable WebGPU:

- In Chrome/Microsoft Edge  

Enable the `chrome://flags/#enable-unsafe-webgpu` flag.

#### Open Your Browser:  
Launch Google Chrome or Microsoft Edge.

#### Access the Flags Page:  
In the address bar, type `chrome://flags` and press Enter.

#### Search for the Flag:  
In the search box at the top of the page, type 'enable-unsafe-webgpu'

#### Enable the Flag:  
Find the #enable-unsafe-webgpu flag in the list of results.

Click the dropdown menu next to it and select Enabled.

#### Restart Your Browser:  

After enabling the flag, you need to restart your browser for the changes to take effect. Click the Relaunch button that appears at the bottom of the page.

- For Linux, launch the browser with `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) has WebGPU enabled by default.  
- In Firefox Nightly, enter about:config in the address bar and `set dom.webgpu.enabled to true`.

### Setting up GPU for Microsoft Edge  

Here are the steps to configure a high-performance GPU for Microsoft Edge on Windows:

- **Open Settings:** Click the Start menu and select Settings.  
- **System Settings:** Go to System and then Display.  
- **Graphics Settings:** Scroll down and click Graphics settings.  
- **Choose App:** Under “Choose an app to set preference,” select Desktop app and then Browse.  
- **Select Edge:** Navigate to the Edge installation folder (usually `C:\Program Files (x86)\Microsoft\Edge\Application`) and select `msedge.exe`.  
- **Set Preference:** Click Options, choose High performance, and then click Save.  

This ensures Microsoft Edge uses your high-performance GPU for improved performance.  
- **Restart** your computer for these settings to take effect.

### Samples : Please [click this link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Disclaimer**:  
Dis documont has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware dat automated translations may contain errors or inaccuracies. De original documont in its native language should be considered de authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from de use of dis translation.