Phi-3-mini WebGPU RAG ചാറ്റ്ബോട്ട്

## WebGPU ആയും RAG മാതൃകയും പ്രദർശിപ്പിക്കാൻ ഉള്ള ഡെമോ
Phi-3 Onnx ഹോസ്റ്റഡ് മോഡലുമായി RAG മാതൃകം Retrieval-Augmented Generation സമീപനം ഉപയോഗിച്ച് Phi-3 മോഡലുകളുടെ ശക്തി ONNX ഹോസ്റ്റിംഗുമായി ചേർത്ത് കാര്യക്ഷമ AI ഡിപ്ലോയ്മെന്റുകൾ സാധ്യമാക്കുന്നു. ഈ മാതൃകം ഡൊമെയ്ൻ-നിശ്ചിത ജോലികൾക്കായി മോഡലുകൾ ഫൈൻ-ട്യൂൺ ചെയ്യുന്നതിനും ഗുണമേൻമ, ചെലവു കാര്യക്ഷമത, നീണ്ട-കോണ്ടെക്സ്റ്റ് ബോധം എന്നിവയുടെ സംയോജനം പ്രദാനം ചെയ്യുന്നതിനും നിർണായകമാണ്. ഇത് Azure AI-യുടെ സ്യൂട്ടിന്റെ ഭാഗമാവാണ്, വിവിധ വ്യവസായങ്ങളുടെ കസ്റ്റമൈസേഷന് ആവശ്യങ്ങൾ കണക്കിലെടുത്ത് എളുപ്പത്തിൽ കണ്ടെത്താനും പരീക്ഷിക്കാനും ഉപയോഗിക്കാനും കഴിയുന്ന മോണഗളുള്ള വിപുലമായ മോഡൽ തിരഞ്ഞെടുപ്പ് പ്രദാനം ചെയ്യുന്നു. Phi-3 മോഡലുകൾ, Phi-3-mini, Phi-3-small, Phi-3-medium എന്നിവ ഉൾപ്പെടെ, Azure AI Model Catalog-ൽ ലഭ്യവുമാണ് തുടർന്ന് സ്വയം-നയിക്കുന്ന രീതിയിൽ അല്ലെങ്കിൽ HuggingFace, ONNX പോലുള്ള പ്ലാറ്റ്‌ഫോമുകളിൽ ഫൈൻ-ട്യൂൺ ചെയ്ത് ഡിപ്ലോയ്മെന്റ് ചെയ്യാൻ സാധിക്കും — Microsoft-ന്റെ ആക്സസിബിൾവും കാര്യക്ഷമവുമായ AI പരിഹാരങ്ങളോടുള്ള പ്രതിബദ്ധതയെ ഇത് ദർശിപ്പിക്കുന്നു.

## WebGPU എന്താണ്
WebGPU ഒരു ആധുനിക വെബ് ഗ്രാഫിക്സ് API ആണ്, വെബ്ബ്രൗസറുകളിൽ നിന്ന് ഉപകരണമേഖലെ ഗ്രാഫിക്സ് പ്രോസസ്സിംഗ് യൂണിറ്റിയിലേക്ക് (GPU) കാര്യക്ഷമമായ ആക്സസ് നൽകാൻ രൂപകൽപ്പന ചെയ്തതാവുന്നു. ഇത് WebGL-ന്റെ ആശാരിയാണ് എന്ന് നിശ്ചയിച്ചിട്ടുണ്ട്, താഴെ ചില പ്രധാന മെച്ചപ്പെടുത്തലുകൾ നൽകുന്നു:

1. **സമകാലീന GPUs-lerle പൊരുത്തം**: WebGPU സമകാലീന GPU ആർക്കിടെക്ചറുകളുമായിട്ടുള്ള സ്മൂത്തിൽ പ്രവർത്തിക്കാൻ നിർമ്മിച്ചിട്ടുണ്ട്, Vulkan, Metal, Direct3D 12 പോലുള്ള സിസ്റ്റം API-കളെ ഉപയോഗപ്പെടുത്തുന്നു.
2. **വളർന്ന പ്രകടനം**: ഇത് ജനറൽ-പർപ്പസ് GPU കംപ്യൂട്ടേഷനുകൾക്കും വേഗതയേറിയ പ്രവർത്തനങ്ങൾക്ക് പിന്തുണ നൽകുന്നു, ഗ്രാഫിക്സ് റെൻഡറിംഗിനും മെഷീൻ ലേണിംഗ് ടാസ്കുകൾക്കും അനുയോജ്യമാണ്.
3. **ഉന്നത സവിശേഷതകൾ**: WebGPU കൂടുതൽ ആധുനിക GPU കഴിവുകൾ ഉപയോഗിക്കാൻ അനുവദിക്കുന്നതിനാൽ കൂടുതൽ സങ്കീർണ്ണവും ഡൈനാമിക് കൂടിയ ഗ്രാഫിക്സ്-സമൃദ്ധവും കംപ്യൂട്ടേഷണൽ വർക്‌ലോഡുകളും സജ്ജമാകും.
4. **JavaScript-ന്റെ വർക്ക്ലോഡ് കുറവ്**: കൂടുതൽ ടാസ്കുകൾ GPU-യിലേക്ക് ഔട്ട്സോഴ്‌സ് ചെയ്യുന്നത് വഴി WebGPU JavaScript-ലുള്ള വർക്ക്ലോഡ് משמעותമായും കുറച്ചുകൊണ്ട് മികച്ച പ്രകടനവും മെച്ചപ്പെട്ട അനുഭവവും സൃഷ്ടിക്കുന്നു.

WebGPU ഇപ്പോൾ Google Chrome പോലുള്ളബ്രൗസറുകളിൽ പിന്തുണയുണ്ടെങ്കിലും മറ്റു പ്ലാറ്റ്‌ഫോമുകളിലേക്കും പിന്തുണ വ്യാപിപ്പിക്കാൻ തുടരുന്ന പ്രവർത്തനങ്ങൾ നടക്കുകയാണ്.

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
- **പുനരാരംഭിക്കുക** നിങ്ങളുടെ യന്ത്രം ഈ ക്രമീകരണങ്ങൾ ബാധകമാകാൻ

### Open Your Codespace:
Navigate to your repository on GitHub.
Click on the Code button and select Open with Codespaces.

If you don’t have a Codespace yet, you can create one by clicking New codespace.

**കുറിപ്പ്** Codespace-ൽ Node പരിസരം ഇൻസ്റ്റാൾ ചെയ്യൽ
GitHub Codespace-ൽ നിന്നുള്ള npm ഡെമോ നടത്തുന്നത് നിങ്ങളുടെ പ്രോജക്ട് ടെസ്റ്റ് ചെയ്യാനും വികസിപ്പിക്കാനും വളരെ നല്ല മാർഗമാണ്. സുഗമമായി ആരംഭിക്കാൻ സഹായിക്കുന്ന ഘട്ടങ്ങളിലടക്കം ഇതാ ഒരു ദിശാനിര്‍ദ്ദേശം:

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

**കുറിപ്പ്:** മോഡൽ ബ്രൗസറിൽ കാഷെ ചെയ്യപ്പെടണം, അതുകൊണ്ട് ലോഡ് ആവാൻ കുറച്ച് സമയംҗиң്ജാവാം.

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
ഡിസ്‌ക്ലെയിമർ:
ഈ രേഖ AI വിവർത്തന സേവനമായ Co-op Translator (https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ അപകൃതതകൾ ഉണ്ടായിരിക്കാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. മൂലഭാഷയിലെ യഥാർത്ഥ രേഖയാണ് ഔദ്യോഗികമായും ആധാരപരമായും കരുതേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മാനവ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിച്ചതിന്റെ ഫലമായി ഉണ്ടാകുന്ന ഏതൊരു തെറ്റിദ്ധാരണയ്ക്കോ തെർജ്ജമാസംബന്ധമായ തെറ്റായ വ്യാഖ്യാനത്തിനോ ഞങ്ങൾക്ക് ഉത്തരവാദിത്വമില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->