Phi-3-mini WebGPU RAG ಚಾಟ್‌ಬಾಟ್

## WebGPU ಮತ್ತು RAG ಮಾದರಿಯನ್ನು ಪ್ರದರ್ಶಿಸಲು ಡೆಮೋ
Phi-3 Onnx Hosted ಮಾದರಿಯೊಂದಿಗೆ RAG ಮಾದರಿ Retrieval-Augmented Generation ವಿಧಾನವನ್ನು ಬಳಸುತ್ತದೆ, ಪರಿಣಾಮಕಾರಿಯಾದ AI ನೇಮಕಾತಿಗಳಿಗೆ Phi-3 ಮಾದರಿಗಳ ಶಕ್ತಿ ಮತ್ತು ONNX ಹೋಸ್ಟಿಂಗ್ ಅನ್ನು ಸಂಯೋಜಿಸುತ್ತದೆ. ಈ ಮಾದರಿ ಡೊಮೇನ್-ನಿರ್ದಿಷ್ಟ ಕೆಲಸಗಳಿಗಾಗಿ ಮಾದರಿಗಳನ್ನು ಫೈನ್-ಟ್ಯೂನಿಂಗ್ ಮಾಡಲು ಪ್ರಮುಖವಾಗಿದೆ, ಗುಣಮಟ್ಟ, ವೆಚ್ಚ-ದಕ್ಷತೆ ಮತ್ತು ದೀರ್ಘ-ಸಂದರ್ಭದ ಅರ್ಥಮಾಡಿಕೆಯನ್ನು ಒದಗಿಸುತ್ತದೆ. ಇದು Azure AI ಹೊರಗಿನ_suite_ನ一 ಭಾಗವಾಗಿದ್ದು, ಹುಡುಕಲು, ಪ್ರಯತ್ನಿಸಲು ಮತ್ತು ಬಳಸಲು ಸುಲಭವಾಗಿರುವ ವಿವಿಧ ಮಾದರಿಗಳ ಪರಿಚಯವನ್ನು ಒದಗಿಸುತ್ತದೆ ಮತ್ತು ವಿವಿಧ ಕೈಗಾರಿಕಾ ಕಸ್ಟಮೈಜೆಶನ್ ಅಗತ್ಯಗಳನ್ನು ಪೂರೈಸುತ್ತದೆ. Phi-3 ಮಾದರಿಗಳು, ಇವುಗಳಲ್ಲಿದ್ದು Phi-3-mini, Phi-3-small, ಮತ್ತು Phi-3-medium, Azure AI Model Catalog ನಲ್ಲಿ ಲಭ್ಯವಿದ್ದು ಸ್ವ-ನಿರ್ವಹಣೆ ಅಥವಾ HuggingFace ಮತ್ತು ONNX പോലಿನ ವೇದಿಕೆಗಳ ಮೂಲಕ ಫೈನ್-ಟ್ಯೂನ್ ಮಾಡಿ ನಿಯೋಜಿಸಬಹುದು, ಇದು ಪ್ರವೇಶযোগ্য ಮತ್ತು ಪರಿಣಾಮಕಾರಿಯಾದ AI ಪರಿಹಾರಗಳಿಗೆ Microsoft ನ ಬದ್ಧತೆಯನ್ನು ತೋರಿಸುತ್ತದೆ.

## WebGPU ಎನದು
WebGPU হল ಒಂದು ಆಧುನಿಕ ವೆಬ್ ಗ್ರಾಫಿಕ್ಸ್ API, ಇದು ವೆಬ್ ಬ್ರೌಸರ್‌ಗಳಿಂದ ನೇರವಾಗಿ ಸಾಧನದ ಗ್ರಾಫಿಕ್ಸ್ ಪ್ರೊಸೆಸಿಂಗ್ ಯೂನಿಟ್ (GPU) ಗೆ ಪರಿಣಾಮಕಾರಿಯಾಗಿ ಪ್ರವೇಶ ನೀಡಲು ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ. ಇದು WebGL ಗೆ ಹೀಗೆಯೇ ಮುಂದುವರಿಯುವದಾಗಿ ಉದ್ದೇಶಿಸಲಾಗಿದೆ ಮತ್ತು ಹಲವು ಮುಖ್ಯ ಸುಧಾರಣೆಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ:

1. **Compatibility with Modern GPUs**: WebGPU ಹೆಚ್ಚು ಆಧುನಿಕ GPU ವಾಸ್ತುಶಿಲ್ಪಗಳೊಂದಿಗೆ ಸುಗಮವಾಗಿ ಕೆಲಸ ಮಾಡಲು ನಿರ್ಮಿಸಲಾಗಿದೆ, Vulkan, Metal, ಮತ್ತು Direct3D 12 ಮುಂತಾದ ಸಿಸ್ಟಂ API ಗಳನ್ನು ಉಪಯೋಗಿಸುತ್ತದೆ.
2. **Enhanced Performance**: ಇದು ಜನರಲ್‑ಪರ್ಪಸ್ GPU ಲెక్కಾಚಾರಗಳನ್ನು ಮತ್ತು ವೇಗವಾದ ಕಾರ್ಯಾಚರಣೆಗಳನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ, ಇದರಿಂದ ಅದು ಗ್ರಾಫಿಕ್ಸ್ ರೆಂಡರಿಂಗ್ ಮತ್ತು ಯಂತ್ರ ಅಭ್ಯಾಸ (machine learning) ಕಾರ್ಯಗಳಿಗೆ ಸೂಕ್ತವಾಗಿದೆ.
3. **Advanced Features**: WebGPU ಹೆಚ್ಚಿನ GPU ಸಾಮರ್ಥ್ಯಗಳಿಗೆ ಪ್ರವೇಶವನ್ನು ಒದಗಿಸುತ್ತದೆ, ಇದರಿಂದ ಹೆಚ್ಚು ಸಂಕೀರ್ಣ ಮತ್ತು ಡೈನಾಮಿಕ್ ಗ್ರಾಫಿಕ್ಸ್ ಮತ್ತು ಲೆಕ್ಕಾಚಾರ ಕಾರ್ಯಭಾರಗಳು ಸಾಧ್ಯವಾಗುತ್ತವೆ.
4. **Reduced JavaScript Workload**: ಹೆಚ್ಚುವರಿ ಕಾರ್ಯಗಳನ್ನು GPU ಗೆ ಹೊತ್ತುಕೊಡುವ ಮೂಲಕ, WebGPU ಜಾವಾಸ್ಕ್ರಿಪ್ಟ್ ಮೇಲಿನ ಕಾರ್ಯಭಾರವನ್ನು ಗಣನೀಯವಾಗಿ ಕಡಿಮೆ ಮಾಡುತ್ತದೆ, ಇದರಿಂದ ಉತ್ತಮ ಪ್ರದರ್ಶನ ಮತ್ತು ತೊಳಕು ಅನುಭವಗಳು ಸಿಗುತ್ತವೆ.

WebGPU ಪ್ರಸ್ತುತ Google Chrome ಮೊದಲಾದ ಬ್ರೌಸರ್‌ಗಳಲ್ಲಿ ಬೆಂಬಲಿತವಾಗಿದೆ, ಇतर ವೇದಿಕೆಗಳಿಗೆ ಬೆಂಬಲವನ್ನು ವಿಸ್ತರಿಸಲು ನಿರಂತರ ಕೆಲಸ ನಡೆಯುತ್ತಿದೆ.

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

After enabling the flag, you’ll need to restart your browser for the changes to take effect. Click the Relaunch button that appears at the bottom of the page.

- For Linux, launch the browser with `--enable-features=Vulkan`.
- Safari 18 (macOS 15) has WebGPU enabled by default.
- In Firefox Nightly, enter about:config in the address bar and `set dom.webgpu.enabled to true`.

### Setting up GPU for Microsoft Edge 

Here are the steps to set up a high-performance GPU for Microsoft Edge on Windows:

- **Open Settings:** Click on the Start menu and select Settings.
- **System Settings:** Go to System and then Display.
- **Graphics Settings:** Scroll down and click on Graphics settings.
- **Choose App:** Under “Choose an app to set preference,” select Desktop app and then Browse.
- **Select Edge:** Navigate to the Edge installation folder (usually `C:\Program Files (x86)\Microsoft\Edge\Application`) and select `msedge.exe`.
- **Set Preference:** Click Options, choose High performance, and then click Save.
This will ensure that Microsoft Edge uses your high-performance GPU for better performance. 
- **Restart** your machine for these setting to take effect 

### Open Your Codespace:
Navigate to your repository on GitHub.
Click on the Code button and select Open with Codespaces.

If you don’t have a Codespace yet, you can create one by clicking New codespace.

**Note** Installing Node Environment in your codespace
Running an npm demo from a GitHub Codespace is a great way to test and develop your project. Here’s a step-by-step guide to help you get started:

### Set Up Your Environment:
Once your Codespace is open, ensure you have Node.js and npm installed. You can check this by running:
```
node -v
```
```
npm -v
```

If they are not installed, you can install them using:
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### Navigate to Your Project Directory:
Use the terminal to navigate to the directory where your npm project is located:
```
cd path/to/your/project
```

### Install Dependencies:
Run the following command to install all the necessary dependencies listed in your package.json file:

```
npm install
```

### Run the Demo:
Once the dependencies are installed, you can run your demo script. This is usually specified in the scripts section of your package.json. For example, if your demo script is named start, you can run:

```
npm run build
```
```
npm run dev
```

### Access the Demo:
If your demo involves a web server, Codespaces will provide a URL to access it. Look for a notification or check the Ports tab to find the URL.

**Note:** The model needs to be cached in the browser, so it may take some time to load. 

### RAG Demo
Upload the markdown file `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### Select Your File:
Click on the button that says “Choose File” to pick the document you want to upload.

### Upload the Document:
After selecting your file, click the “Upload” button to load your document for RAG (Retrieval-Augmented Generation).

### Start Your Chat:
Once the document is uploaded, you can start a chat session using RAG based on the content of your document.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಅಸ್ವೀಕರಣ:
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಭಾಷಾಂತರ ಸೇವೆ Co-op Translator (https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗಾಗಿ ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಭಾಷಾಂತರಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ತಪ್ಪು ಅರಿವುಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಭಾಷಾಂತರವನ್ನು ಉಪಯೋಗಿಸುವುದು ಶಿಫಾರಸ್ಸಾಗುತ್ತದೆ. ಈ ಭಾಷಾಂತರವನ್ನು ಬಳಸುವುದರಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಗ್ರಹಿಕೆಗಳು ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->