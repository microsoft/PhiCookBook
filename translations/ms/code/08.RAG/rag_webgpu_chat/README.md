<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4aac6b8a5dcbbe9a32b47be30340cac2",
  "translation_date": "2025-05-09T05:21:26+00:00",
  "source_file": "code/08.RAG/rag_webgpu_chat/README.md",
  "language_code": "ms"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Demo for showcasing WebGPU and RAG Pattern
The RAG Pattern with Phi-3 Onnx Hosted model uses the Retrieval-Augmented Generation approach, combining the strengths of Phi-3 models with ONNX hosting for efficient AI deployment. This pattern is key for fine-tuning models on domain-specific tasks, offering a balance of quality, cost efficiency, and long-context understanding. It’s part of Azure AI’s portfolio, providing a broad range of models that are easy to find, test, and use, meeting customization needs across industries. Phi-3 models, including Phi-3-mini, Phi-3-small, and Phi-3-medium, are available on Azure AI Model Catalog and can be fine-tuned and deployed either self-managed or through platforms like HuggingFace and ONNX, highlighting Microsoft’s commitment to accessible and efficient AI solutions.

## What is WebGPU 
WebGPU is a modern web graphics API designed to give efficient access to a device’s graphics processing unit (GPU) directly from web browsers. It is meant to replace WebGL, offering several important improvements:

1. **Compatibility with Modern GPUs**: WebGPU is designed to work smoothly with current GPU architectures, using system APIs like Vulkan, Metal, and Direct3D 12.
2. **Enhanced Performance**: It supports general-purpose GPU computing and faster operations, suitable for both graphics rendering and machine learning tasks.
3. **Advanced Features**: WebGPU provides access to more advanced GPU capabilities, enabling more complex and dynamic graphics and computation workloads.
4. **Reduced JavaScript Workload**: By shifting more tasks to the GPU, WebGPU significantly lowers the workload on JavaScript, resulting in better performance and smoother user experiences.

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
In the search box at the top, enter 'enable-unsafe-webgpu'

#### Enable the Flag:
Locate the #enable-unsafe-webgpu flag in the results.

Click the dropdown menu next to it and select Enabled.

#### Restart Your Browser:

After enabling the flag, restart your browser to apply the changes. Click the Relaunch button at the bottom of the page.

- For Linux, launch the browser with `--enable-features=Vulkan`.
- Safari 18 (macOS 15) has WebGPU enabled by default.
- In Firefox Nightly, type about:config in the address bar and `set dom.webgpu.enabled to true`.

### Setting up GPU for Microsoft Edge 

Follow these steps to configure a high-performance GPU for Microsoft Edge on Windows:

- **Open Settings:** Click the Start menu and select Settings.
- **System Settings:** Navigate to System, then Display.
- **Graphics Settings:** Scroll down and click Graphics settings.
- **Choose App:** Under “Choose an app to set preference,” select Desktop app, then click Browse.
- **Select Edge:** Go to the Edge installation folder (usually `C:\Program Files (x86)\Microsoft\Edge\Application`) and select `msedge.exe`.
- **Set Preference:** Click Options, choose High performance, then click Save.

This ensures Microsoft Edge uses your high-performance GPU for better performance.  
- **Restart** your computer for the changes to take effect.

### Open Your Codespace:
Go to your repository on GitHub.  
Click the Code button and select Open with Codespaces.

If you don’t have a Codespace yet, create one by clicking New codespace.

**Note** Installing Node Environment in your codespace  
Running an npm demo from a GitHub Codespace is a great way to test and develop your project. Here’s a step-by-step guide to get you started:

### Set Up Your Environment:
Once your Codespace is open, make sure Node.js and npm are installed. Check by running:
```
node -v
```  
```
npm -v
```

If not installed, you can install them using:
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```

### Navigate to Your Project Directory:
Use the terminal to go to the directory containing your npm project:
```
cd path/to/your/project
```

### Install Dependencies:
Run this command to install all dependencies listed in your package.json:

```
npm install
```

### Run the Demo:
After installing dependencies, run your demo script, usually defined in the scripts section of your package.json. For example, if your demo script is named start, run:

```
npm run build
```  
```
npm run dev
```

### Access the Demo:
If your demo runs a web server, Codespaces will provide a URL to access it. Look for a notification or check the Ports tab for the URL.

**Note:** The model needs to be cached in the browser, so loading may take some time.

### RAG Demo
Upload the markdown file `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Select Your File:
Click the “Choose File” button to select the document you want to upload.

### Upload the Document:
After selecting your file, click “Upload” to load your document for RAG (Retrieval-Augmented Generation).

### Start Your Chat:
Once uploaded, you can start a chat session using RAG based on your document’s content.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.