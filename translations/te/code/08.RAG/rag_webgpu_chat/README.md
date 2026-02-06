Phi-3-mini WebGPU RAG చాట్‌బాట్

## WebGPU మరియు RAG ప్యాటర్న్‌ను ప్రదర్శించేందుకు డెమో
Phi-3 Onnx Hosted మోడల్‌తో కూడిన RAG ప్యాటర్న్ Retrieval-Augmented Generation పద్ధతిని ఉపయోగిస్తుంది, Phi-3 మోడళ్లు మరియు ONNX హోస్టింగ్ శక్తిని సమ్మిళితం చేసి సమర్థవంతమైన AI డిప్లాయ్‌మెంట్‌లను అందిస్తుంది. ఈ ప్యాటర్న్ డొమైన్-స్పెసిఫిక్ పనులకు మోడళ్లను ఫైన్-ట్యూన్ చేయటానికి సహాయకరంగా ఉంటుంది, నాణ్యత, ఖర్చు-సమర్థత మరియు లాంగ్-కాంటెక్స్ట్ అవగాహనను సమతుల్యంగా అందిస్తుంది. ఇది Azure AI యొక్క సూట్‌లో భాగంగా ఉంది, వినియోగదారులు కోసం బహుళ ఎంపికలైన మోడళ్లు సులభంగా కనుగొనగలిగేలా, ప్రయత్నించగలిగేలా మరియు ఉపయోగించదగ్గంగా అందిస్తుంది, వివిధ పరిశ్రమల అనుకూలీకరణ అవసరాలను తీర్చడానికి. Phi-3 మోడళ్లు, అందులో Phi-3-mini, Phi-3-small, మరియు Phi-3-medium కూడా ఉన్నాయి, Azure AI Model Catalog లో లభ్యమవుతాయి మరియు self-managed లేదా HuggingFace మరియు ONNX వంటి ప్లాట్‌ఫారమ్‌ల ద్వారా ఫైన్-ట్యూన్ చేసి డిప్లాయ్ చేయవచ్చు, ఇది Microsoft యొక్క సులభంగా అందుబాటులో ఉండే మరియు సమర్థవంతమైన AI పరిష్కారాల పట్ల సంకల్పాన్ని చూపుతుంది.

## WebGPU అంటే ఏమిటి
WebGPU అనేది ఆధునిక వెబ్ గ్రాఫిక్స్ API ఇది వెబ్ బ్రౌజర్ల నుండి పరికరం యొక్క గ్రాఫిక్స్ ప్రాసెసింగ్ యూనిట్ (GPU) కు సమర్థవంతమైన ప్రాప్తిని నేరుగా అందించేందుకు రూపొందించబడింది. ఇది WebGL కి స్థానంకోరుతున్నది, మరియు కొన్ని ముఖ్యమైన మెరుగుదలలను అందిస్తుంది:

1. **Compatibility with Modern GPUs**: WebGPU ఆధునిక GPU ఆర్కిటెక్చర్‌లతో సజావుగా పనిచేయడానికి రూపొందించబడింది, Vulkan, Metal, మరియు Direct3D 12 వంటి సిస్టమ్ APIలను ఉపయోగిస్తుంది.
2. **Enhanced Performance**: ఇది జనరల్-పర్పస్ GPU కంప్యూటేషన్లను మరియు వేగవంతమైన ఆపరేషన్లను మద్దతు ఇస్తుంది, దీన్ని గ్రాఫిక్స్ రెండరింగ్ మరియు మెషీన్ లెర్నింగ్ పనులకు అనుకూలంగా చేస్తుంది.
3. **Advanced Features**: WebGPU మరింత అధునిక GPU సామర్థ్యాలకు ప్రాప్తిని ఇస్తుంది, క్లిష్టమైన మరియు డైనమిక్ గ్రాఫిక్స్ మరియు కంప్యూటేషనల్ వర్క్‌లోడ్స్‌ను నడపడానికి సహాయపడుతుంది.
4. **Reduced JavaScript Workload**: GPU కు మరింత టాస్క్‌లను ఆఫ్‌లోడ్ చేస్తూ, WebGPU JavaScript పై పనిచేసే పనిభారం ను గణనీయంగా తగ్గిస్తుంది, తద్వారా మెరుగైన ప్రదర్శన మరియు స్మూత్ అనుభవాలు వస్తాయి.

WebGPU ప్రస్తుతం Google Chrome వంటి బ్రౌజర్లలో మద్దతు పొందుతోంది, మరియు ఇతర ప్లాట్‌ఫారమ్‌లపై మద్దతును విస్తరించేందుకు పని జరుగుతోంది.

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

**గమనిక** Installing Node Environment in your codespace
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

**గమనిక:** మోడల్ బ్రౌజర్‌లో క్యాష్ కావాలి, కాబట్టి లోడ్ అయ్యేందుకు కొంత సమయం పట్టవచ్చు. 

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
**డిస్క్లెయిమర్**:
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ అయిన [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, స్వయంచాలక అనువాదాలలో పొరపాట్లు లేదా అపూర్ణతలు ఉండే అవకాశం ఉంది. మూల భాషలోని అసలు డాక్యుమెంట్‌ను అధికారిక మూలంగా పరిగణించాలి. కీలకమైన సమాచారానికి ప్రొఫెషనల్ మానవ అనువాదం చేయించుకోవాలని సూచించబడుతుంది. ఈ అనువాదం వలన కలిగే ఏవైనా అవగాహనా లోపాలు లేదా తర్జుమా తప్పుల కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->