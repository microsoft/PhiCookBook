Phi-3-mini WebGPU RAG Chatbot

## Demo for showcasing WebGPU and RAG Pattern
Di RAG Pattern wey dey use Phi-3 Onnx Hosted model dey use Retrieval-Augmented Generation approach, wey combine Phi-3 models power with ONNX hosting make AI deployments dey efficient. Dis pattern dey help for fine-tuning models for domain-specific work, e dey give correct balance between quality, cost-effectiveness, and sabi long-context. E dey part of Azure AI suite, wey get plenty models wey easy to find, try, and use, plus e fit support customization for different industries. Phi-3 models like Phi-3-mini, Phi-3-small, and Phi-3-medium dey for Azure AI Model Catalog and you fit fine-tune and deploy am self-managed or through platforms like HuggingFace and ONNX, wey show Microsoft commitment to make AI easy to access and efficient.

## What is WebGPU 
Wetin be WebGPU
WebGPU na modern web graphics API wey dem design make e give efficient access to device GPU directly from web browsers. Na the successor wey dem intend for WebGL, and e get plenty better things:

1. **Compatibility with Modern GPUs**: WebGPU build to work well with modern GPU architectures, e dey leverage system APIs like Vulkan, Metal, and Direct3D 12.
2. **Enhanced Performance**: E support general-purpose GPU computations and faster operations, so e good for graphics rendering and machine learning tasks.
3. **Advanced Features**: WebGPU dey give access to advanced GPU capabilities, make you fit run more complex and dynamic graphics and computational workloads.
4. **Reduced JavaScript Workload**: By offloading more tasks to the GPU, WebGPU go reduce JavaScript workload, so performance go better and experience go smooth.

WebGPU dey supported for browsers like Google Chrome, and dem still dey work to expand support to other platforms.

### 03.WebGPU
Required Environment:

**Supported browsers:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Enable WebGPU:

- In Chrome/Microsoft Edge 

Turn on the `chrome://flags/#enable-unsafe-webgpu` flag.

#### Open Your Browser:
Open your browser like Google Chrome or Microsoft Edge.

#### Access the Flags Page:
For the address bar, type `chrome://flags` and press Enter.

#### Search for the Flag:
For the search box at the top of the page, type 'enable-unsafe-webgpu'

#### Enable the Flag:
Find the #enable-unsafe-webgpu flag for the result list.

Click the dropdown menu next to am and choose Enabled.

#### Restart Your Browser:

After you enable the flag, you go need to restart your browser make the changes start work. Click the Relaunch button wey go show for bottom of the page.

- For Linux, launch the browser with `--enable-features=Vulkan`.
- Safari 18 (macOS 15) get WebGPU enabled by default.
- For Firefox Nightly, open about:config for the address bar and `set dom.webgpu.enabled to true`.

### Setting up GPU for Microsoft Edge 

Here na the steps to set up high-performance GPU for Microsoft Edge on Windows:

- **Open Settings:** Click the Start menu and choose Settings.
- **System Settings:** Go to System then Display.
- **Graphics Settings:** Scroll down and click on Graphics settings.
- **Choose App:** Under “Choose an app to set preference,” pick Desktop app then click Browse.
- **Select Edge:** Go to the Edge installation folder (usually `C:\Program Files (x86)\Microsoft\Edge\Application`) and select `msedge.exe`.
- **Set Preference:** Click Options, choose High performance, then click Save.
This one go make sure Microsoft Edge dey use your high-performance GPU for better performance. 
- **Restart** your machine make these settings take effect 

### Open Your Codespace:
Go your repository for GitHub.
Click the Code button and choose Open with Codespaces.

If you no get Codespace yet, you fit create one by clicking New codespace.

**Note** Installing Node Environment in your codespace
Running an npm demo from a GitHub Codespace na good way to test and develop your project. Below na step-by-step guide wey go help you start:

### Set Up Your Environment:
When your Codespace don open, make sure say Node.js and npm dey installed. You fit check by running:
```
node -v
```
```
npm -v
```

If dem no dey installed, you fit install dem using:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navigate to Your Project Directory:
Use terminal make you enter the directory wey your npm project dey:
```
cd path/to/your/project
```

### Install Dependencies:
Run dis command to install all the dependencies wey dey your package.json file:

```
npm install
```

### Run the Demo:
After dependencies don install, you fit run your demo script. Normally dem go specify am for scripts section of package.json. For example, if your demo script name na start, you go run:

```
npm run build
```
```
npm run dev
```

### Access the Demo:
If your demo get web server, Codespaces go provide URL to access am. Look for notification or check the Ports tab to see the URL.

**Note:** The model need to dey cached for the browser, so e fit take small time to load. 

### RAG Demo
Upload the markdown file `intro_rag.md` to complete the RAG solution. If you dey use codespaces you fit download the file wey dey `01.InferencePhi3/docs/`

### Select Your File:
Click the button wey talk “Choose File” to pick the document wey you wan upload.

### Upload the Document:
After you don select your file, click the “Upload” button to load your document for RAG (Retrieval-Augmented Generation).

### Start Your Chat:
Once the document don upload, you fit start chat session wey use RAG based on the content wey dey your document.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Abeg note:
Dis dokument don translate wit AI translation service [Co-op Translator] (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translations fit get mistakes or dey inaccurate. Di original dokument for im original language na di correct/authority source. For important matter, we dey recommend make professional human translator do di translation. We no dey responsible for any misunderstanding or wrong interpretation wey fit come from di use of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->