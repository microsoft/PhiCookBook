# Phi-3.5-Instruct WebGPU RAG ಚಾಟ್‌ಬಾಟ್

## WebGPU ಮತ್ತು RAG ಪ್ಯಾಟರ್ನ್ ಪ್ರದರ್ಶನದ ಡೆಮೋ

Phi-3.5 Onnx Hosted ಮಾದರಿಯೊಂದಿಗೆ RAG ಪ್ಯಾಟರ್ನ್ Retrieval-Augmented Generation ಕ್ರಮವನ್ನು ಬಳಸಿಕೊಂಡು Phi-3.5 ಮಾದರಿಗಳ ಶಕ್ತಿ ಮತ್ತು ONNX ہوس್ಟಿಂಗ್ ಅನ್ನು ಸಮರ್ಥ AI ನಿಯೋಜನೆಗಳಿಗಾಗಿ ಸಂಯೋಜಿಸುತ್ತದೆ. ಈ ಪ್ಯಾಟರ್ನ್ ಡೊಮೇನ್-ನಿರ್ದಿಷ್ಟ ಕಾರ್ಯಗಳಿಗೆ ಮಾದರಿಗಳನ್ನು ಸೂಕ್ತಗೊಳಿಸಲು ಸಹಾಯಕವಾಗಿದ್ದು, ಗುಣಮಟ್ಟ, ವೆಚ್ಚ-ಫಲಕಾರಿತ್ವ ಮತ್ತು ದೀರ್ಘ-ಕ контೆಕ್ಸ್ಟ್ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ. ಇದು Azure AI ಗಳ ಸಿಟ್ರಿಯಲ್ಲಿ ಭಾಗವಾಗಿದೆ, ವಿವಿಧ ಉದ್ಯಮಗಳ ಕಸ್ಟಮೈಸೇಶನ್ ಅಗತ್ಯಗಳನ್ನು ಪೂರೈಸಲು ಸುಲಭವಾಗಿ ಕಂಡುಹಿಡಿಯಲು, ಪ್ರಯೋಗಿಸಲು ಮತ್ತು ಬಳಸಲು ಆಗುವ ಮಾದರಿಗಳ кең ಆಯ್ಕೆಯನ್ನು ಒದಗಿಸುತ್ತದೆ.

## WebGPU ಎಂದರೆ ಏನು
WebGPU ಎಂದರೆ ಬ್ರೌಸರ್‌ಗಳಿಂದ ನೇರವಾಗಿ ಸಾಧನದ ಗ್ರಾಫಿಕ್ಸ್ ಪ್ರೊಸೆಸಿಂಗ್ ಯೂನಿಟ್ (GPU) ಗೆ ಪರಿಣಾಮಕಾರಿಯಾಗಿ ಪ್ರವೇಶವನ್ನು ನೀಡಲು ರೂಪಿತ ಆಧುನಿಕ ವೆಬ್ ಗ್ರಾಫಿಕ್ಸ್ API. ಇದು WebGL ನ ಆನಂತರದ ಆವೃತ್ತಿಯಾಗಲು ಉದ್ದೇಶಿಸಲಾಗಿದೆ ಮತ್ತು ಕೆಲವು ಪ್ರಮುಖ ಸುಧಾರಣೆಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ:

1. **ಆಧುನಿಕ GPU ಗಳೊಂದಿಗೆ ಹೊಂದಿಕೊಳ್ಳುವಿಕೆ**: WebGPU ಅನ್ನು ಆಧುನಿಕ GPU ವಾಸ್ತುಶಿಲ್ಪಗಳೊಂದಿಗೆ ಸಮರಾಸವಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸಲು ನಿರ್ಮಿಸಲಾಗಿದೆ, Vulkan, Metal, ಮತ್ತು Direct3D 12 ಮುಂತಾದ ಸಿಸ್ಟಂ API ಗಳನ್ನು ಉಪಯೋಗಿಸುತ್ತದೆ.
2. **ಉನ್ನತ ಕಾರ್ಯಕ್ಷಮತೆ**: ಇದು ಸಾಮಾನ್ಯ-ಉದ್ದೇಶ GPU ಗಣನೆಗಳನ್ನು ಮತ್ತು ವೇಗವಾದ ಕಾರ್ಯಾಚರಣೆಗಳನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ, ಇದನ್ನು ಗ್ರಾಫಿಕ್ಸ್ ರೆಂಡರಿಂಗ್ ಮತ್ತು ಯಂತ್ರಅಧ್ಯಯನ ಕಾರ್ಯಗಳಿಗಾಗಿ ಸೂಕ್ತವಾಗಿಸುತ್ತದೆ.
3. **ಅಧುನತ ವೈಶಿಷ್ಟ್ಯಗಳು**: WebGPU ಹೆಚ್ಚಿನ GPU ಸಾಮರ್ಥ್ಯಗಳಿಗೆ ಪ್ರವೇಶವನ್ನು ಒದಗಿಸುತ್ತದೆ, ಹೆಚ್ಚು ಸಂಕೀರ್ಣ ಮತ್ತು ડೈನಾಮಿಕ್ ಗ್ರಾಫಿಕ್ಸ್ ಮತ್ತು ಗಣನಾತ್ಮಕ ಕೆಲಸಗಳನ್ನು ಸಾಧ್ಯವಾಗಿಸುತ್ತದೆ.
4. **JavaScript ಕಾರ್ಯಭಾರದ ಕಡಿತ**: ಹೆಚ್ಚಿನ ಕಾರ್ಯಗಳನ್ನು GPU ಗೆ ನಿಲುಗಡೆಮಾಡುವ ಮೂಲಕ, WebGPU JavaScript ಮೇಲಿನ ಕಾರ್ಯಭಾರವನ್ನು ಗಮನಾರ್ಹವಾಗಿ ಕಡಿಮೆ ಮಾಡುತ್ತದೆ, ಪರಿಣಾಮವಾಗಿ ಉತ್ತಮ ಕಾರ್ಯಕ್ಷಮತೆ ಮತ್ತು ಮೃದುವಾದ ಅನುಭವಗಳನ್ನು ಪಡೆಯಬಹುದು.

WebGPU ಪ್ರಸ್ತುತ Google Chrome ಮುಂತಾದ ಬ್ರೌಸರ್‌ಗಳಲ್ಲಿ ಬೆಂಬಲಿತವಾಗಿದೆ, ಮತ್ತು ಇತರ ವೇದಿಕೆಗಳಿಗೆ ಬೆಂಬಲವನ್ನು ವಿಸ್ತರಿಸಲು ಮುಂದುವರೆದ ಕೆಲಸ ನಡೆಯುತ್ತಿದೆ.

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
ನಿಮ್ಮ ಬ್ರೌಸರ್ ತೆರೆಯಿರಿ: Google Chrome ಅಥವಾ Microsoft Edge ಚಲಾಯಿಸಿ.

#### Access the Flags Page:
ಸರಾಸರಿ ಪಟ್ಟಿಯಲ್ಲಿ ವಿಳಾಸ ಬಾರ್ನಲ್ಲಿ `chrome://flags` ಟೈಪ್ ಮಾಡಿ ಮತ್ತು Enter ಒತ್ತಿ.

#### Search for the Flag:
ಪುಟದ ಮೇಲ್ಭಾಗದಲ್ಲಿರುವ ಹುಡುಕಾಟ ಬಾಕ್ಸ್‌ನಲ್ಲಿ 'enable-unsafe-webgpu' ಟೈಪ್ ಮಾಡಿ

#### Enable the Flag:
ಫಲಿತಾಂಶಗಳ ಪಟ್ಟಿಯಲ್ಲಿ #enable-unsafe-webgpu ಧ್ವಜವನ್ನು ಹುಡುಕಿ.

ಬದಲಾಗುವ ಅವತರಣಿಕೆ ಮెనುವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿರಿ ಮತ್ತು Enabled ಆಯ್ಕೆಮಾಡಿ.

#### Restart Your Browser:

ಧ್ವಜವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿದ ನಂತರ, ಬದಲಾವಣೆಗಳು ಪರಿಣಾಮಕಾರಿಯಾಗಲು ನಿಮ್ಮ ಬ್ರೌಸರನ್ನು ಪುನರಾರಂಭಿಸಬೇಕಾಗುತ್ತದೆ. ಪುಟದ ತಿರುವಿನಡಿಯಲ್ಲಿ ಕಾಣುವ Relaunch ಬಟನ್ ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ.

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

### Samples : ದಯವಿಟ್ಟು [ಈ ಲಿಂಕ್‌ಗೆ ಕ್ಲิ๊ก ಮಾಡಿ](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ನಿರಾಕರಣೆ:
ಈ ದಸ್ತಾವೇಜನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗಾಗಿ ಪ್ರಯತ್ನಿಸಿದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅನಿಖರತೆಗಳು ಇರಬಹುದಾಗಿದೆ. ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅದರ ಸ್ವಭಾಷೆಯಲ್ಲಿ ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಗ್ರಹಿಕೆಗಳು ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->