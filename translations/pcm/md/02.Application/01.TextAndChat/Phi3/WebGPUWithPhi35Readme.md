# Phi-3.5-Instruct WebGPU RAG Chatbot

## Demo wey dey show WebGPU and RAG Pattern

Di RAG Pattern wey use Phi-3.5 Onnx Hosted model dey use di Retrieval-Augmented Generation approach, e combine di power of Phi-3.5 models with ONNX hosting for efficient AI deployments. Dis pattern dey help fine-tune models for domain-specific tasks, e dey offer mix of quality, cost-effectiveness, and long-context understanding. E part of Azure AI’s suite, wey dey provide plenty models wey easy to find, try, and use, to fit di customization needs of different industries. 

## Wetin be WebGPU 
WebGPU na modern web graphics API wey dem design make e give efficient access to device graphics processing unit (GPU) straight from web browsers. Dem intend am to be di successor to WebGL, and e get plenti key improvements:

1. **Compatibility with Modern GPUs**: WebGPU build make e work well with contemporary GPU architectures, e dey leverage system APIs like Vulkan, Metal, and Direct3D 12.
2. **Enhanced Performance**: E support general-purpose GPU computations and faster operations, make am suitable for both graphics rendering and machine learning tasks.
3. **Advanced Features**: WebGPU dey provide access to more advanced GPU capabilities, enabling more complex and dynamic graphics and computational workloads.
4. **Reduced JavaScript Workload**: By offloading more tasks to di GPU, WebGPU dey reduce di workload on JavaScript, wey dey lead to better performance and smoother experiences.

WebGPU dey currently supported for browsers like Google Chrome, with ongoing work to expand support to other platforms.

### 03.WebGPU
Wetins you need:

**Supported browsers:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Enable WebGPU:

- For Chrome/Microsoft Edge 
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

After enabling the flag, you go need to restart your browser make di changes take effect. Click the Relaunch button wey go appear at di bottom of the page.

- For Linux, launch the browser with `--enable-features=Vulkan`.
- Safari 18 (macOS 15) get WebGPU enabled by default.
- In Firefox Nightly, enter about:config in the address bar and `set dom.webgpu.enabled to true`.

### Setting up GPU for Microsoft Edge 

Here are the steps to set up a high-performance GPU for Microsoft Edge on Windows:

- **Open Settings:** Click di Start menu and select Settings.
- **System Settings:** Go to System and then Display.
- **Graphics Settings:** Scroll down and click on Graphics settings.
- **Choose App:** Under “Choose an app to set preference,” select Desktop app and then Browse.
- **Select Edge:** Navigate to the Edge installation folder (usually `C:\Program Files (x86)\Microsoft\Edge\Application`) and select `msedge.exe`.
- **Set Preference:** Click Options, choose High performance, and then click Save.
This one go make sure say Microsoft Edge go use your high-performance GPU for better performance. 
- **Restart** your machine make these settings take effect 

### Samples : Abeg [click this link](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document don translate with AI translation service Co-op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg note say automatic translations fit get mistakes or wrong parts. The original document for im own language na the main source wey you suppose rely on. If na important information, better make professional human translator check am. We no go take any blame for any misunderstandings or wrong meaning wey fit come from using this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->