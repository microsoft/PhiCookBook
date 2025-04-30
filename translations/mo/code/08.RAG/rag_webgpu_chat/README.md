<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c7a7f2a07dc176c19e1ab9f249b548c9",
  "translation_date": "2025-04-04T11:36:39+00:00",
  "source_file": "code\\08.RAG\\rag_webgpu_chat\\README.md",
  "language_code": "mo"
}
-->
Phi-3-mini WebGPU RAG Chatbot

## Phi-3 WebGPU RAG Pattern Demonstration
The RAG Pattern, combined with the Phi-3 Onnx Hosted model, utilizes the Retrieval-Augmented Generation approach to enhance AI capabilities. By integrating Phi-3 models with ONNX hosting, it ensures efficient deployment of AI solutions tailored to specific domains. This approach provides a balance between high-quality results, cost-efficiency, and the ability to process longer contexts. As part of Azure AI's offerings, it delivers a wide range of models that are easy to locate, experiment with, and apply, meeting diverse industry requirements for customization. The Phi-3 models, including Phi-3-mini, Phi-3-small, and Phi-3-medium, are accessible via the Azure AI Model Catalog. They can be fine-tuned and deployed independently or through platforms like HuggingFace and ONNX, reflecting Microsoft's dedication to making AI solutions more approachable and effective.

## What is WebGPU
WebGPU is a cutting-edge web graphics API that enables direct access to a device's GPU from web browsers. It is designed to succeed WebGL, offering significant improvements in various areas:

1. **Modern GPU Compatibility**: WebGPU is tailored to work effortlessly with the latest GPU architectures, utilizing system APIs such as Vulkan, Metal, and Direct3D 12.
2. **Improved Performance**: It supports general-purpose GPU tasks and faster computations, making it suitable for both graphics rendering and machine learning applications.
3. **Advanced Functionalities**: WebGPU grants access to more sophisticated GPU features, facilitating complex and dynamic workloads in graphics and computation.
4. **Reduced JavaScript Processing**: By shifting more operations to the GPU, WebGPU minimizes JavaScript's workload, enhancing performance and providing smoother user experiences.

WebGPU is currently available in browsers like Google Chrome, with ongoing efforts to extend its compatibility to other platforms.

### 03.WebGPU
Required Environment:

**Supported browsers:** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### Activating WebGPU:

- In Chrome/Microsoft Edge 

Activate the `chrome://flags/#enable-unsafe-webgpu` flag.

#### Launch Your Browser:
Open Google Chrome or Microsoft Edge.

#### Navigate to Flags Page:
Enter `chrome://flags` in the address bar and hit Enter.

#### Locate the Flag:
Search for 'enable-unsafe-webgpu' in the search box at the top of the page.

#### Enable the Flag:
Identify the #enable-unsafe-webgpu flag in the results.

Select Enabled from the dropdown menu next to it.

#### Restart Your Browser:

After enabling the flag, restart your browser to apply the changes. Click the Relaunch button at the bottom of the page.

- For Linux, open the browser using `--enable-features=Vulkan`.
- Safari 18 (macOS 15) comes with WebGPU enabled by default.
- In Firefox Nightly, type about:config in the address bar and `set dom.webgpu.enabled to true`.

### Configuring GPU for Microsoft Edge

Follow these steps to enable a high-performance GPU for Microsoft Edge on Windows:

- **Open Settings:** Access Settings from the Start menu.
- **System Settings:** Navigate to System and then Display.
- **Graphics Settings:** Scroll down and select Graphics settings.
- **Choose Application:** Under “Choose an app to set preference,” pick Desktop app and then Browse.
- **Locate Edge:** Go to the Edge installation directory (commonly `C:\Program Files (x86)\Microsoft\Edge\Application`) and select `msedge.exe`.
- **Set Preference:** Click Options, choose High performance, and save the changes.
This ensures Microsoft Edge utilizes your high-performance GPU for optimal performance. 
- **Restart** your computer to apply these settings.

### Open Your Codespace:
Access your repository on GitHub.
Click the Code button and choose Open with Codespaces.

If you don’t have a Codespace yet, create one by clicking New codespace.

**Note** Installing Node Environment in your codespace
Running an npm demo within a GitHub Codespace is a convenient way to test and develop your project. Here's how you can get started:

### Prepare Your Environment:
Once your Codespace is active, ensure Node.js and npm are installed. Verify by executing:
```
node -v
```
```
npm -v
```

If they aren’t installed, install them using:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navigate to Your Project Directory:
Use the terminal to move to the directory containing your npm project:
```
cd path/to/your/project
```

### Install Dependencies:
Execute the following command to install all dependencies listed in your package.json file:

```
npm install
```

### Run the Demo:
After installing the dependencies, execute your demo script. For example, if your demo script is named start, run:

```
npm run build
```
```
npm run dev
```

### Access the Demo:
If your demo involves a web server, Codespaces will provide a URL for access. Check the notification or the Ports tab for the URL.

**Note:** The model requires caching in the browser, so loading might take some time.

### RAG Demo
Upload the markdown file `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Select Your File:
Click the “Choose File” button to select the document you wish to upload.

### Upload the Document:
After selecting the file, click the “Upload” button to load your document for Retrieval-Augmented Generation (RAG).

### Start Your Chat:
Once the document is uploaded, initiate a chat session using RAG based on the document’s content.

It seems like "mo" might refer to a specific language or abbreviation, but I need more context to determine what "mo" stands for. Could you clarify or provide more details about the language or format you're requesting the translation in?