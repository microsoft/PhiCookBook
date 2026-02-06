# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo for showcasing WebGPU and RAG Pattern

The RAG Pattern with the Phi-3.5 Onnx Hosted model uses the Retrieval-Augmented Generation approach, combining the strengths of Phi-3.5 models with ONNX hosting for efficient AI deployment. This pattern is key for fine-tuning models on domain-specific tasks, offering a balance of quality, cost-efficiency, and long-context understanding. It’s part of Azure AI’s portfolio, providing a wide range of models that are easy to find, test, and use, meeting the customization needs of various industries.

## What is WebGPU  
WebGPU is a modern web graphics API designed to give direct, efficient access to a device’s graphics processing unit (GPU) from web browsers. It is meant to replace WebGL, offering several important improvements:

1. **Compatibility with Modern GPUs**: WebGPU is designed to work smoothly with current GPU architectures, using system APIs like Vulkan, Metal, and Direct3D 12.
2. **Improved Performance**: It supports general-purpose GPU computing and faster operations, making it suitable for both graphics rendering and machine learning tasks.
3. **Advanced Features**: WebGPU provides access to more sophisticated GPU capabilities, enabling more complex and dynamic graphics and computational workloads.
4. **Reduced JavaScript Load**: By shifting more tasks to the GPU, WebGPU significantly lowers the workload on JavaScript, resulting in better performance and smoother user experiences.

WebGPU is currently supported in browsers like Google Chrome, with ongoing efforts to extend support to other platforms.

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
Type `chrome://flags` in the address bar and press Enter.

#### Search for the Flag:  
In the search box at the top, type 'enable-unsafe-webgpu'

#### Enable the Flag:  
Locate the #enable-unsafe-webgpu flag in the results.

Click the dropdown menu next to it and select Enabled.

#### Restart Your Browser:  

After enabling the flag, restart your browser for the changes to take effect. Click the Relaunch button that appears at the bottom of the page.

- On Linux, start the browser with `--enable-features=Vulkan`.  
- Safari 18 (macOS 15) has WebGPU enabled by default.  
- In Firefox Nightly, go to about:config in the address bar and set `dom.webgpu.enabled` to true.

### Setting up GPU for Microsoft Edge  

Follow these steps to configure a high-performance GPU for Microsoft Edge on Windows:

- **Open Settings:** Click the Start menu and select Settings.  
- **System Settings:** Go to System, then Display.  
- **Graphics Settings:** Scroll down and click Graphics settings.  
- **Choose App:** Under “Choose an app to set preference,” select Desktop app, then click Browse.  
- **Select Edge:** Navigate to the Edge installation folder (usually `C:\Program Files (x86)\Microsoft\Edge\Application`) and select `msedge.exe`.  
- **Set Preference:** Click Options, choose High performance, then click Save.  

This ensures Microsoft Edge uses your high-performance GPU for better performance.  
- **Restart** your computer for these settings to take effect.

### Samples : Please [click this link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.